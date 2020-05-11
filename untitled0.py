# -*- coding: utf-8 -*-
"""
Created on Mon May 11 14:57:31 2020

@author: Amin
"""

from netCDF4 import Dataset, MFDataset
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
rootgrp = Dataset("AVHRR-Land_v005_AVH13C1_NOAA-07_19810625_c20170610042839.nc", "a", format="NETCDF4")
print(rootgrp.variables)
rc=rootgrp.variables['NDVI'][:]
#f=MFDataset("AVHRR-Land_v005_AVH13C1_NOAA-07_19810625_c20170610042839.nc")
#print(f.variables["ncrs"][:])
rc=rc[0]
fig, ax = plt.subplots()
im = ax.imshow(rc)
lat=rootgrp.variables['latitude'][:]
long=rootgrp.variables['longitude'][:]