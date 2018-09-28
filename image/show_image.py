# -*- coding: UTF-8 -*-

import matplotlib.pyplot as plt # plt 用于显示图片
import matplotlib.image as mpimg # mpimg 用于读取图片
import numpy as np
from PIL import Image


im = Image.open('lena.png')
im.show()