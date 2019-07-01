echo "******* Anonymizer installer ********"
sudo apt-get install xterm -y
sudo apt-get install tor -y -qq
sudo apt-get install nmap
sudo pip install stem
echo "=====> W8 "
sudo cp torghost /usr/bin/torghost
sudo chmod +x /usr/bin/torghost
sudo chmod +x torghost
clear
sudo chmod +x start_scum.sh
sleep 4
sudo ./start_scum.sh
 
