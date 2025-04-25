#!/data/data/com.termux/files/usr/bin/bash
pkg upgrade; 
pkg install -y gcc-9 autoconf automake dnsutils mtr ncdu ripgrep libjpeg-turbo curl tmux zsh neovim mutt msmtp yadm tintin++ newsboat exa mc hub aria2 progress python ruby gpgv nodejs golang ncurses-utils root-repo science-repo game-repo unstable-repo x11-repo w3m irssi python2 rust rsync cmake go pdfgrep fzf broot dog git-delta topgrade


curl -LO https://its-pointless.github.io/setup-pointless-repo.sh 
bash setup-pointless-repo.sh 
rm setup-pointless-repo.sh pointless.gpg.1

pip install --upgrade pip 

pip install ddgr jrnl speedtest-cli rebound-cli glances manly neovim httpie yt-dlp

pip list --outdated --format=freeze | rg -v '^\-e' | cut -d = -f 1 | xargs -n1 pip install

gem install bro tmuxinator 

npm install -g tldr 

wget -c https://github.com/cheat/cheat/releases/download/3.6.0/cheat-linux-arm7.gz
gunzip cheat-linux-arm7.gz
mv cheat-linux-arm7 /data/data/com.termux/files/usr/bin/cheat
chmod +x /data/data/com.termux/files/usr/bin/cheat

git clone https://github.com/nelhage/reptyr.git
cd reptyr
make
make install PREFIX=$PREFIX
cd ..
rm -fr reptyr

git clone https://github.com/dvorka/hstr.git
cd hstr
autoreconf --install
./configure --prefix=$PREFIX
make
make install
cd ..
rm -fr hstr

go get -u github.com/nishanths/license
mv go/bin/license /data/data/com.termux/files/usr/bin/ 
chmod +x /data/data/com.termux/files/usr/bin/license
rm -fr go/

ln -s storage/shared/Documents Documents
ln -s storage/shared/Downloads Downloads
ln -s storage/shared/Music Music
ln -s storage/shared/Pictures Pictures
ln -s storage/shared/Retrogaming Retrogaming

#vdirsyncer discover 
#vdirsyncer sync  
# Certfile for offlineimap missing
# /data/data/com.termux/files/usr/etc/tls/cert.pem
pip2 install six rfc6555 offlineimap
#offlineimap 

git config --global user.email "peter@code-alongsi.de"
git config --global user.name "Peter Aufner"

git clone git://archivemail.git.sourceforge.net/gitroot/archivemail/archivemail
cd archivemail
python2 setup.py install
cd .. 
rm -fr archivemail

