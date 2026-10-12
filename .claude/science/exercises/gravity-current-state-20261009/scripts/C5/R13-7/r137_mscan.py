"""R13-7 mass scan: on-shell c_e(m) and the photon's c_gamma(m) (electron loop only, R10-1 Theorem D moment)
for BQ laws, light -> heavy electron.  Delta(m) = dc_e - dc_gamma in e^2/16pi^2 units.
NR prediction for the heavy literal edge (W = 0, u = S^2, A = u''/2 - 1):
   c_e^2 - 1 -> eps_inf = (e^2/2) < A(q_x) (omega^2 - d_x^2) / (d_x^2 omega^3) >   (A0 recoil + NR seagull; derived in report)
"""
import sys, time; sys.path.insert(0,'.')
import numpy as np
from r137_onshell import *
def nr_pred(law, N, lam):
    q1=kgrid1(N); QX,QY,QZ=np.meshgrid(q1,q1,q1,indexing='ij')
    dx2,dy2,dz2=law.d(QX)**2,law.d(QY)**2,law.d(QZ)**2
    w2=dx2+dy2+dz2+lam**2; w=np.sqrt(w2)
    u=lambda k: law.S(k)**2
    A=deriv(u,QX,2)/2-1
    seag=np.mean(A/(dx2*w)); coul=np.mean(A/w**3)
    return 0.5*(seag-coul), 0.5*seag, -0.5*coul
lam=0.05
laws=[('S1 gapped',1.0,2.0,1.0,1.0,2.0),('S1 literal',1.0,2.0,0.0,1.0,2.0),('S3 gapped',2.0,3.0,1.0,2.0,3.0),('S3 literal',2.0,3.0,0.0,2.0,3.0),('S5 literal',0.5,1.5,0.0,0.5,1.5)]
ms=[0.05,0.1,0.2,0.4,0.8,1.6,3.2,6.4,12.8,25.6,51.2]
print('lam = %.3f ; columns: m, N, dc_e(on-shell)*U, dc_gamma(moment)*U, Delta*U, m*dc_e*U, [tadpole part of dc_e]'%lam)
for lab,b1,b2,r,c1,c2 in laws:
    for m in ms:
        N = 96 if m < 0.1 else 64
        law=Law(b1,b2,r,c1,c2,m)
        ce,ct,dE0=ce2_minus_1(law,N,lam,h=0.02)
        mo=moment(law,N)
        dce=ce/2*U; dcg=mo['tot']
        print('%-11s m=%7.3f N=%3d  dc_e=%+10.4f  dc_g=%+10.4f  Delta=%+10.4f  m*dc_e=%+10.4f  [tad %+10.4f]'%(lab,m,N,dce,dcg,dce-dcg,m*dce,ct/2*U),flush=True)
    if r==0.0:
        e,s,c=nr_pred(Law(b1,b2,r,c1,c2,1.0),64,lam)
        print('   NR heavy-limit prediction dc_e*U -> eps_inf/2*U = %+10.4f  (seagull %+.4f, Coulomb-recoil %+.4f)'%(e/2*U,s/2*U,c/2*U),flush=True)
