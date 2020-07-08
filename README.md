# Info
Test réalisé sur:
_Ubuntu 18.04 (xubuntu Lubuntu Kubuntu auras juste de légére difference sur l'uttilisation des ressources de l'ordinateur)

_Python 3.6
_nvidia 440 (ubuntu release)

# linux
~=dossier personnel = /home/$USER

# install-cuda
Installation cuda:
nécessite de télécharger le ficher https://drive.google.com/uc?export=download&id=1uffdAM_4lyU0zBvRR7F70k-R_mFmqLw2  manuellement, puis lancer le script install-cuda dans le répertoire où est ce fichier

(~=dossier personnel = /home/$USER)
# install manuel python
mettre le paquet dans ~/.local/lib/python3.6/site-packages/
# pyinstaller 
nécessite l'ajout de hook (~/.local/lib/python3.6/site-packages/PyInstaller/hooks/) ou copier manuellement les fichier manquant ~/.local/lib/python3.x/site-packages
`cp -r /dist/nom/* build/nom/ corrige l'importation de librairie python`
# tensor
testé 1.14 1.15 et 2.2 version gpu avec uttilisation du gpu
download object_detection du github et le mettre dans ~/.local/lib/python3.x/site-packages 
il y a d'autres paquet du git qui n'ont pas encore était pull dans le build pip,
la manip est la meme (il est possible de mettre dans le dossier de tensor aussi)

Pour les GPU: 

`gpus = tf.config.experimental.list_physical_devices('GPU')
if gpus:
      tf.config.experimental.set_visible_devices(gpus[0], 'GPU')
      tf.config.experimental.set_memory_growth(gpu, True)`
# pip
écriture pour pip <= 20.0 
selon version
`$ pip install paquet`
`$ pip3 install paquet` 

pip => 20.0
python3 -m pip install paquet1 paquet2 
(l'ancienne éciture fonctione toujours)

# information GPU
`$ nvidia-smi` ou en gui avec actuallisation automatique `$ nvidia-settings`
