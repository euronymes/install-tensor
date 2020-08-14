#python3 install
sudo apt install python3.6 python3.6-pip3 python3.6-dev python-dev python3-pip
#passage python systeme 2.7->3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
sudo update-alternatives  --set python /usr/bin/python3.6
pip3 install -r requirement.txt

