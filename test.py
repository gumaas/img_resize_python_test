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
        
    def get_line( self ):
        # return 1dim array
        self.line += 1
        return self.arr[self.line-1]
    
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
    def __init__(self, xres = 1, yres = 1):
        self.xresize = xres;
        self.yresize = yres;
        

class resize:
    def __init__ (self, source, sinc, config ):
        self.getline = source
        self.putline = sinc
        self.config = config
        
        
    def change_config(self, cfg):
        self.config = cfg;
        
    def go( self ):
        while 1:
            try:
                self.putline( self.getline() )
            except:
                print "Done"
                return
            
        
        
lb = line_buffer("lena512.bmp")
ic = image_creator()
cfg = resize_config

rsz = resize(lb.get_line, ic.add_line, cfg )
rsz.go()
ic.show()