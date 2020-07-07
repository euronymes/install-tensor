sudo apt install python3.6 python3.6-pip3 python3.6-dev python-dev python3-pip
sudo apt install nvidia-cuda-toolkit
sudo dpkg -i libcudnn7_7.6.5.32-1+cuda10.1_amd64.deb
sudo dpkg -i libcudnn7-dev_7.6.5.32-1+cuda10.1_amd64.deb
sudo dpkg -i libcudnn7-doc_7.6.5.32-1+cuda10.1_amd64.deb
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.6 2
sudo update-alternatives  --set python /usr/bin/python3.6

pip3 install tensorflow
pip3 install PyQt5
pip3 install pyqtgraph

#gpus = tf.config.experimental.list_physical_devices('GPU')
#if gpus:
#   for gpu in gpus:   #permet de faire fonctionner plusieur gpu en parrallele 
#    tf.config.experimental.set_memory_growth(gpu, True) #besoin de cette ligne sous linux
