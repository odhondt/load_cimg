# CImg file importer for numpy

- As the CImg library does not include advanced functions for plotting 2D and 3D graphs, it may be useful to import .cimg files into an interactive environment for further analysis. 
- The function `cimg_load` allows to import .cimg files into the python numpy environment. 
- It also works for cimg lists if all images have the same dimension. Then all images are written in a single nparray.
