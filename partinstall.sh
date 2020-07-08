#python3 install
sudo apt install python3.6 python3.6-pip3 python3.6-dev python-dev python3-pip
#cuva install
sudo mv cuda-ubuntu1804.pin /etc/apt/preferences.d/cuda-repository-pin-600
wget http://developer.download.nvidia.com/compute/cuda/10.2/Prod/local_installers/cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo dpkg -i cuda-repo-ubuntu1804-10-2-local-10.2.89-440.33.01_1.0-1_amd64.deb
sudo apt-key add /var/cuda-repo-10-2-local-10.2.89-440.33.01/7fa2af80.pub
sudo apt-get update
sudo apt-get -y install cuda
#libcudnn install
sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.2_amd64.deb 
#passage python systeme 2.7->3.6
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
sudo update-alternatives  --set python /usr/bin/python3.6

#gpus = tf.config.experimental.list_physical_devices('GPU')
#if gpus:
#   for gpu in gpus:   #permet de faire fonctionner plusieur gpu en parrallele 
#    tf.config.experimental.set_memory_growth(gpu, True) #besoin de cette ligne sous linux
