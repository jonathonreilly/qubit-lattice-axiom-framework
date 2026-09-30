# Independent recomputation of Test A with explicit low-rank character formulas (not Jacobi-Trudi) and a different grid.
import numpy as np
from scipy.optimize import brentq
n=500; off=0.123456
t=(np.arange(n)+off)*2*np.pi/n
t1,t2=np.meshgrid(t,t,indexing='ij'); t3=-(t1+t2)
z=[np.exp(1j*t1),np.exp(1j*t2),np.exp(1j*t3)]
tr=z[0]+z[1]+z[2]                      # chi_3
tr2=z[0]**2+z[1]**2+z[2]**2            # chi_3(U^2)
tr3=z[0]**3+z[1]**3+z[2]**3
chi={ '3':tr, '8':abs(tr)**2-1, '6':(tr**2+tr2)/2 }
# (3,0): sym^3 = (p1^3+3 p1 p2 + 2 p3)/6, dim 10
chi['10']=(tr**3+3*tr*tr2+2*tr3)/6
dim={'3':3,'8':8,'6':6,'10':10}
C2={'3':4/3,'8':3,'6':10/3,'10':6}
dens=np.abs((z[0]-z[1])*(z[0]-z[2])*(z[1]-z[2]))**2; dens/=dens.mean()
re=np.real(tr)
def ratio(b,R):
    e=np.exp(b/3*(re-3)); w0=(e*dens).mean()
    wr=(e*dens*np.real(chi[R])).mean()/dim[R]
    return wr/w0
for R in ['3','8','6','10']:
    g2=lambda b:2*(-np.log(ratio(b,R)))/C2[R]
    bR=brentq(lambda b:g2(b)-1,1,30)
    print(R, "w/w0(6)=%.8f"%ratio(6,R), "g_E^2(6)=%.5f"%g2(6), "beta_R=%.4f"%bR)
# sanity of character normalisation: int chi_R^2 dHaar = 1
for R in chi: print(R,"norm", (dens*np.abs(chi[R])**2).mean())
