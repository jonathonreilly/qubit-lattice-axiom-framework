"""R13-7: on-shell vs R8-5 off-shell (p0=0) electron speed at small m (lam = m), gapped and literal S1/S3."""
import sys; sys.path.insert(0,'.')
from r137_onshell import *
for lab,b1,b2,r,c1,c2 in [('S1 gapped',1.0,2.0,1.0,1.0,2.0),('S1 literal',1.0,2.0,0.0,1.0,2.0),('S3 gapped',2.0,3.0,1.0,2.0,3.0)]:
    for m,N in [(0.1,96),(0.05,128),(0.025,160)]:
        law=Law(b1,b2,r,c1,c2,m)
        ce,ct,_=ce2_minus_1(law,N,lam=m,h=0.01)
        off=fermion(law,N,lam=m)
        print('%-10s m=%.3f N=%3d  on-shell %+9.4f  off-shell(B-A) %+9.4f  diff %+7.4f  diff/m %+7.3f'%(lab,m,N,ce/2*U,off['dce']*U,ce/2*U-off['dce']*U,(ce/2*U-off['dce']*U)/m),flush=True)
