#!/data/data/com.termux/files/usr/bin/bash
pkg upgrade; 
pkg install -y  dnsutils mtr ncdu ripgrep libjpeg-turbo curl tmux zsh neovim yadm aria2 python gpgv science-repo game-repo unstable-repo x11-repo rsync dog topgrade python-yt-dlp

curl -LO https://its-pointless.github.io/setup-pointless-repo.sh 
bash setup-pointless-repo.sh 
rm setup-pointless-repo.sh pointless.gpg.1

ln -s storage/shared/Documents Documents
ln -s storage/shared/Downloads Downloads
ln -s storage/shared/Music Music
ln -s storage/shared/Pictures Pictures
ln -s storage/shared/Retrogaming Retrogaming

git config --global user.email "peter@code-alongsi.de"
git config --global user.name "Peter Aufner"

