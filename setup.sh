cd ~
sudo chown -R administrator:administrator *
sudo apt-get update
sudo apt-get -y install python-pip
pip install futures
sudo apt-get -y install python-bs4
sudo apt-get -y install python-scapy
sudo apt-get -y install git
rm -rf ~/ics355
rm -rf ~/ics355_botnet
mkdir ~/ics355_botnet
cd ~
sudo chown -R administrator:administrator *
cd ~/ics355_botnet
git clone https://github.com/danman10000/IRC-Bot.git
echo "sudo python ~/ics355_botnet/IRC-Bot/src/ircbot.py" > ~/ics355_run_bot.sh
chmod +x ~/ics355_run_bot.sh
cd ~
sudo chown -R administrator:administrator *
