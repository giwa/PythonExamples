'''
    ref 
    http://www.python.org/workshops/1997-10/proceedings/savikko.html

    >>> rgb = RGB( 100, 192, 240 )
    >>> rgb.Red()
    100
    >>> proxy = Proxy( rgb )
    >>> proxy.Green()
    192
    >>> noblue = NoBlueProxy( rgb )
    >>> noblue.Green()
    192
    >>> noblue.Blue()
    0
'''


class RGB:
    def __init__( self, red, green, blue ):
        self.__red = red
        self.__green = green
        self.__blue = blue
    def Red( self ):
        return self.__red
    def Green( self ):
        return self.__green
    def Blue( self ):
        return self.__blue    

class Proxy:
    def __init__( self, subject ):
        self.__subject = subject
    def __getattr__( self, name ):
        return getattr( self.__subject, name )  

class NoBlueProxy( Proxy ):
    def Blue( self ):
        return 0    
