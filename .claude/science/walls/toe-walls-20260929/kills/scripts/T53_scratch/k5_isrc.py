"""I_src = Im(H12 H23 H31) sign on the boundary roots and far-interior roots, gamma=+/-1/2 (0-indexed H[0,1]*H[1,2]*H[2,0])."""
import numpy as np
from chart import H, obs, SQ
def Isrc(x,g):
    Hm=H(*x,g); return (Hm[0,1]*Hm[1,2]*Hm[2,0]).imag
rows=[('B-root Basin0',(-0.0149,1.0614,SQ-1.0614)),('B-root Basin1',(0.6793,0.9285,SQ-0.9285)),('B-root 3',(1.5041,5.1962,SQ-5.1962)),('B-root 4',(43.5163,21.2866,SQ-21.2866)),
      ('interior Basin1 pin',(0.657061342210,0.933806343759,0.715042329587)),('interior Basin2',(28.006188289565,20.721831213931,5.011599458305)),('interior BasinX',(21.128263668694,12.680028023619,2.089234805861))]
for n,x in rows:
    print('%-22s'%n,'x=(%.4f,%.4f,%.4f)'%x,' Isrc(g=+.5)=%+.4f  Isrc(g=-.5)=%+.4f'%(Isrc(x,0.5),Isrc(x,-0.5)))
