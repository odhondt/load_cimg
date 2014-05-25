def load_cimg(fname):
    """This function is loading data from a .cimg file that may contain
 a single image or a list of images. All the images in the list 
must have identical dimensions."""

    # TODO: endianness
    
    # ctypes are used to handle types defined in C
    from ctypes import c_byte, c_ubyte, c_int, c_uint, c_long, c_ulong, c_float, c_double,c_longdouble
    import numpy as np

    # opening the file
    f = open(fname,'rb');

    # lines are read as one string, splitting and converting them to form arrays
    hdr1 = np.array([str(x) for x in f.readline().split()])
    hdr2 = np.array([int(x) for x in f.readline().split()])

    # number of images in the list
    n_img = int(hdr1[0])

    # image dimensions
    [dx, dy, dz, dv] = hdr2;

    # type handling
    mytypes = {'char': c_byte, 'unsigned char': c_ubyte, 
               'int': c_int, 'unsigned int': c_uint,
               'long': c_long, 'unsigned long': c_ulong,
               'float': c_float, 'double': c_double,
               'long double': c_longdouble
               }
    
    print "-- Loading from CImg file -----------"
    print ""
    print "Number of images: ", n_img
    print "Dimensions: dx =", dx, ", dy =", dy, ", dz =", dz, ", dv =", dv
    print "Data type: ", hdr1[1] 
    print "Endianness: ", hdr1[2]
    print ""
    print "-------------------------------------"
    print ""

    # Reading the data
    d = np.fromfile(f, dtype=mytypes[hdr1[1]], count=dx*dy*dz*dv)
    if n_img > 1:
        for n in range(n_img-1):
            l = f.readline()
            d = np.append(d, np.fromfile(f, dtype=mytypes[hdr1[1]], count=dx*dy*dz*dv))
    # reshaping the data in the form [n_im, n_line, n_col, depth, channel]
    d = d.reshape([n_img, dv, dz, dy, dx]).transpose([0, 3, 4, 2, 1]).squeeze();
    return d;

