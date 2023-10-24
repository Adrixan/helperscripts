from fs import open_fs
from datetime import datetime
import os, sys

zim_files = open_fs('ftp://download.kiwix.org/zim/')
path = sys.argv[1]

current_dir_list = (file for file in os.listdir(path) 
         if os.path.isfile(os.path.join(path, file)))
print(current_dir_list)

date_format = '%Y-%m'

zims ={'wikipedia':'_en_all_nopic_', 'wiktionary':'_en_all_maxi_', 'wikiquote':'_en_all_maxi_'}
max_attempts = 10

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
        print("Newer version found!")
        download_success = False

        print("Downloading {}".format(server_zim_version_name))
        for attempts in range(0, max_attempts):
            try:
                with open(os.path.join(path, server_zim_version_name), 'wb') as write_file:
                    zim_files.download(zim + '/' + server_zim_version_name, write_file)
                print("Download finished")
                download_success = True
            except ConnectionResetError:
                print("Error downloading file on attempt:{} of {}".format(attempts +1, max_attempts))
                if attempts < max_attempts:
                    print("Retrying...")
                else:
                    print("Download of {} failed!".format(server_zim_version_name))
            if download_success:
                break
        
        print("Deleting old version: {}".format(local_zim_version_name))
        try:
            os.remove(os.path.join(path, local_zim_version_name))
        except FileNotFoundError:
            pass
    else:
        print("Already at the newest version!")