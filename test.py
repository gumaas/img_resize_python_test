from PIL import Image
import numpy

# im = Image.open("lena512.bmp")
# 
# arr = numpy.asarray(im)
# 
# im2 = Image.fromarray(arr)
# 
# im2.show()


class line_buffer:
    
    def __init__( self, file  ):
        self.file = file
        self.img = Image.open(self.file)
        self.arr = numpy.asarray(self.img)
        self.line = 0
        
    def get_line( self, line ):
        # return 1dim array
        return self.arr[line]
    
    def new_frame(self):
        self.line =0

class line_buffer_arr:
    
    def __init__( self, arr  ):
        self.arr = numpy.asarray(arr)
        self.line = 0
        
    def get_line( self, line ):
        # return 1dim array
        return self.arr[line]
    
    def new_frame(self):
        self.line =0

    
class image_creator:
    def __init__(self):
        self.arr = numpy.array([])
        
    def show(self):
        print self.arr
        Image.fromarray(self.arr).show()
        
    def add_line(self,line):
        if len( self.arr ) > 0:
            self.arr = numpy.vstack( (self.arr, line) )
        else:
            self.arr = numpy.array( line )
        
    def new_image(self):
        self.arr = numpy.array([])


class resize_config:
    def __init__(self):
        self.xtarget = 800;
        self.ytarget = 800;
        self.xsize = 512
        self.ysize = 512
        

class resize:
    def __init__ (self, source, sinc, config ):
        self.getline = source
        self.putline = sinc
        self.config = config
        
        
    def change_config(self, cfg):
        self.config = cfg;
        
    def bilinear( self ):
        
        low_data = []
        high_data = []
        new_data = numpy.zeros(self.config.xsize)

        
        for l in xrange(self.config.ytarget-1):
            ideal=float(l*(self.config.ysize-1)/float(self.config.ytarget) )
            
            high = ideal - numpy.floor(ideal)
            low = 1 - high
            # low = 1 if low == 0 else low


            # high = numpy.ceil(ideal) - ideal
            print "ideal: %f. Low:%d*%f, H:%d*%f" % ( ideal, numpy.floor(ideal), low, numpy.ceil(ideal), high )
            low_data=self.getline( numpy.floor(ideal) )
            high_data=self.getline( numpy.ceil(ideal) )

            for i in xrange( self.config.xsize ):
                new_data[i] = low*low_data[i] + high*high_data[i]

            self.putline( new_data )
            
        print"done"
        return
    
    def repeat( self ):
        for l in xrange(self.config.ytarget):
            
            self.putline( self.getline(int(l*self.config.ysize/self.config.ytarget)))
            
        print"done"
        return
        
        
lb = line_buffer("lena512.bmp")
arr = numpy.array( [ [ 1, 1, 1 ],
        [ 5, 5, 5 ],
        [ 8, 8, 8 ] ] )


# lb = line_buffer_arr(arr)
ic = image_creator()
cfg = resize_config()

cfg.ytarget = 500
cfg.ysize = 200
# cfg.xtarget = 7
# cfg.ytarget = 7
# cfg.xsize   = 3
# cfg.ysize   = 3

rsz = resize(lb.get_line, ic.add_line, cfg )
rsz.repeat()
rsz.bilinear()
ic.show()