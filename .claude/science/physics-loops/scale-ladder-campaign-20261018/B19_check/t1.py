import time, sympy as sp
from grav_common import *
t=time.time(); R1,R2=sqrtgR(); print("R built", time.time()-t, len(R2.args))
import pickle; pickle.dump((R1,R2), open("R12.pkl","wb"))
