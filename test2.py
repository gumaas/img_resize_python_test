from PIL import Image
import numpy
import matplotlib.pyplot as plt


def linear_resize( data, coef ):
    
    new_size = int( len(data) * coef )
    new_data = numpy.zeros(new_size)
    new_range = numpy.zeros(new_size)

    print "old size: %d, new_size:%d coef : %f" %( len(data), new_size, coef )
    
    coef = float(new_size)/float(len(data)-1)

    coef_mod = new_size-1
    for i in xrange(new_size):
        x   = i/coef
        x0  = int( numpy.floor(x) )
        x1  = x0+1
        y0  = data[x0]
        y1  = data[x1]
        
        print "i:%d x:%f, x0:%d, x1:%d, y0:%d y1:%d" % ( i, x, x0, x1, y0, y1 )

        new_data[i] = y0 + (y1-y0)*(x-x0)/(x1-x0)
        new_range[i] = x

    return [ new_range, new_data]

def linear_resize2( data, coef ):
    
    new_size    = int( len(data) * coef )
    new_data    = numpy.zeros(new_size)
    new_range   = numpy.zeros(new_size)

    print "old size: %d, new_size:%d coef : %f" %( len(data), new_size, coef )
    
    coef = float(new_size)/float(len(data)-1)

    coef_mod = new_size-1
    # prev = [ 1, 0 ]
    for i in xrange(new_size):
        x   = i/coef
        x0  = int( numpy.floor(x) )
        x1  = x0+1
        y0  = data[x0]
        y1  = data[x1]
        
        print "i:%d x:%f, x0:%d, x1:%d, y0:%d y1:%d" % ( i, x, x0, x1, y0, y1 )

        new_data[i] = y0 + (y1-y0)*(x-x0)/(x1-x0)
        new_range[i] = x

    return [ new_range, new_data]

data = [1, 8, 10, 15, 19, 18, 13, 6, 8, 5 ]

[nrange, ndata] = linear_resize( data, 2.0 )

plt.plot( range( len(data) ), data, 'x', nrange, ndata )
plt.show()
