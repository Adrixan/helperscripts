from fs import open_fs
from datetime import datetime
import os, sys, subprocess

serverpath = 'ftp://download.kiwix.org/zim/'
zim_files = open_fs(serverpath)
path = sys.argv[1]

current_dir_list = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
print(current_dir_list)

date_format = '%Y-%m'

zims ={'wikipedia':'_en_all_nopic_', 'wiktionary':'_en_all_maxi_', 'wikiquote':'_en_all_maxi_'}
max_attempts = 10

to_download = {}

for zim in zims.keys():
    base_name = zim + zims[zim]
    local_zim_version = datetime.strptime('1970-01', date_format)
    local_zim_version_name = base_name + '1970-01.zim'

    for file in current_dir_list:
        if base_name in file:
            local_zim_version = datetime.strptime(file.split(base_name)[1].split('.zim')[0], date_format)
            local_zim_version_name = file
            break

    print("Local zim version: " + str(local_zim_version))
    print("Local zim name: " + local_zim_version_name)

    current_zim = zim_files.opendir(zim)
    server_zim_version = datetime.strptime('1970-01', date_format)
    server_zim_version_name = ''
    for zim_version in current_zim.walk.files(filter=[base_name + '*.zim']):
        date = datetime.strptime(zim_version.split(base_name)[1].split('.zim')[0], date_format)
        if date > server_zim_version:
            server_zim_version = date
            server_zim_version_name = zim_version[1:]
    print("Server zim version: " + str(server_zim_version))
    print("Server zim name: " + server_zim_version_name)

    if server_zim_version > local_zim_version:
        print("Newer version found! Adding to queue")
        to_download["{}{}/{}".format(serverpath, zim, server_zim_version_name)] = local_zim_version_name

    else:
        print("Already at the newest version!")

for download in to_download.keys():
    download_success = False

    print("Downloading {}".format(download))

    for attempt in range(1, max_attempts + 1):
        result = subprocess.run(["aria2c", "-d {}".format(path), download])
        if result.returncode == 0:
            print("Download success!")

            print("Deleting old version: {}".format(to_download[download]))
            try:
                os.remove(os.path.join(path, to_download[download]))
            except FileNotFoundError:
                pass

            break
        else:
            print("Attempt {} of {} failed".format(attempt, max_attempts))
    
