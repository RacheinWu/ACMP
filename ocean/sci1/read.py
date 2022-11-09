# import os
#
# import pandas as pd
#
# import numpy as np
#
# number = -1;
#
# sudu=np.zeros(5247*5,dtype=float).reshape(5247,5)
#
# for files in filelist1:
#
# number +=1
#
# data = pd.read_csv(str(number+1)+'a.csv')
#
# sudu[:,number]=data['velocity']
#
# x = data['x']
#
# y = data['y']
#
# a = sudu[0:5184,0].reshape(81,64)
#
#
# import matplotlib.pyplot as plt
#
# extent = [np.min(x),np.max(x),np.min(y),np.max(y)]
#
# plt.subplot(231)
#
# u0 = sudu[0:5184,0].reshape(81,64)
#
# plt.imshow(u0,extent=extent,origin='lower')
#
# plt.subplot(232)
#
# u1 = sudu[0:5184,1].reshape(81,64)
#
# plt.imshow(u1,extent=extent,origin='lower')
#
# plt.subplot(233)
#
# u2 = sudu[0:5184,2].reshape(81,64)
#
# plt.imshow(u2,extent=extent,origin='lower')
#
# plt.subplot(234)
#
# u3 = sudu[0:5184,3].reshape(81,64)
#
# plt.imshow(u3,extent=extent,origin='lower')
#
# #plt.axis("equal")
#
# plt.subplot(235)
#
# u4 = sudu[0:5184,4].reshape(81,64)
#
# plt.imshow(u4,extent=extent,origin='lower')
#
# plt.subplot(236)
#
# u5 = sudu[0:5184,4].reshape(81,64)
#
# plt.imshow(u5,extent=extent,origin='lower')
#
# #contour
#
# cs = plt.contour(u5, 20,extent = extent)
#
# plt.xlim(-0.8,0.8)
#
# plt.ylim(0.6,2.2)
#
# plt.axis('equal')
