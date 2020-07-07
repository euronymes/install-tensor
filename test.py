import pkg_resources.py2_warn
#Modules system
import os
import sys
import netifaces
import random
import string
import shutil
from threading import Thread
from queue import Queue
from scipy import signal
import time
import numba
from time import clock
from collections import deque, Counter 
from multiprocessing.pool import ThreadPool
import multiprocessing
import itertools
import pandas
import datetime
import re
import socket
import pickle
                             
#Modules interface
import PyQt5
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QStyle, QRubberBand, QSizePolicy
from PyQt5.QtCore import Qt, QPoint, QRect, QSize, QEvent
from PyQt5.QtGui import QIcon

#Modules de traitement images, fonctions mathematiques
from scipy.optimize import linear_sum_assignment
from scipy.fftpack import rfft, irfft
from detect_peaks import detect_peaks #ajouter detect_peaks.py dans ~/.local/lib/python3.6/site-packages
from smooth import smooth #ajouter smooth.py dans ~/.local/lib/python3.6/site-packages
import cv2
import numpy as np
from numpy.linalg import inv
from scipy.spatial.distance import cdist
from scipy import ndimage as ndi
from math import sqrt
from scipy.integrate import quad
from transform import four_point_transform #ajouter transform.py dans ~/.local/lib/python3.6/site-packages
from scipy import interpolate
import qimage2ndarray

from skimage.measure import label, regionprops
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)
from skimage.morphology import reconstruction
from skimage.segmentation import mark_boundaries
from skimage.util import img_as_float
import skimage.segmentation as seg
from unsharp_mask_fct import unsharp_mask #ajouter unsharp_mask_fct.py dans ~/.local/lib/python3.6/site-packages
import skimage.color as color
from skimage.filters import roberts, sobel, sobel_h, sobel_v, scharr, \
    scharr_h, scharr_v, prewitt, prewitt_v, prewitt_h
from skimage.feature import match_template
from skimage.restoration import (denoise_wavelet, estimate_sigma)

#Modules graphique
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib import style
style.use('dark_background')
from matplotlib.widgets import LassoSelector
from matplotlib import path
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.widgets  import RectangleSelector
from matplotlib import patches
import pyqtgraph as pg

#Modules format/API compatibilité
import tifffile as tifffile
import dm4reader #ajouter unsharp_mask_fct.py dans ~/.local/lib/python3.6/site-packages
#from json_reader import read_json_twoi
#from pyueye import ueye

#Modules learning
import tensorflow as tf
import label_map_util
import visualization_utils as vis_util #necessite d'extraire/installer objet_detection depuis le github https://github.com/tensorflow/models/tree/master/research/object_detection

#Modules protocols communication
from pyModbusTCP.client import ModbusClient
import snap7.client as c
from snap7.util import *
from snap7.snap7types import*
import snap7

#Module base de donnée
import sqlite3

#object labellisation
#import pascalLabel
#import yoloLabel

#from pyueye_example_camera import Camera
#from pyueye_example_utils import FrameThread

import logging

from PyQt5.QtCore import pyqtSlot
from PyQt5.QtCore import QObject, pyqtSignal


