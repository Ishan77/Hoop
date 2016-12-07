
#Python does not have the concept of static like java or c++ , hence
#the singleton class makes sure that all the object are in the same
#state. So no matter how many objects you make thet have the same
#configurations.

class singleton(object):
    
    _shared_state ={}
    
    def __new__(cls,*a,**k):
        obj = object.__new__(cls,*a,**k)
        obj. __dict__ = cls._shared_state
        return obj


