"""R13-7 heavy-electron checks (literal edge, W = 0):
 (1) Richardson in 1/m of on-shell dc_e(m) vs the closed form dc_e(inf) = (1/4)<A(q_x)(W^2-d_x^2)/(d_x^2 W^3)>, N = 64 and 96;
 (2) hypotheses of the sign theorem on the edge [b1, pi]: (H1) S(q)^2 <= q^2, (H2) q_x -> w(q_x,q_perp) convex;
     plus the sign of A = (S^2)''/2 - 1 (A <= 0 is NOT needed);
 (3) the identity I(q_perp) = -pi w(pi) + 1/2 int_b^pi (S^2 - q^2) w'' dq  vs direct int_b^pi A w dq;
 (4) the photon mass lam -> 0 limit of dc_e(inf).
"""
import sys; sys.path.insert(0,'.')
import numpy as np
from r137_onshell import *
def inf_const(law,N,lam):
    q1=kgrid1(N); QX,QY,QZ=np.meshgrid(q1,q1,q1,indexing='ij')
    dx2,dy2,dz2=law.d(QX)**2,law.d(QY)**2,law.d(QZ)**2
    W2=dx2+dy2+dz2+lam**2; W=np.sqrt(W2)
    A=deriv(lambda k: law.S(k)**2,QX,2)/2-1
    return 0.25*np.mean(A*(W2-dx2)/(dx2*W**3))*U
lam=0.05
print('(1) on-shell dc_e*U at large m (literal edge), Richardson in 1/m, vs closed form')
for lab,b1,b2,c1,c2,nv in [('S1',1.0,2.0,1.0,2.0,False),('S3',2.0,3.0,2.0,3.0,False),('S5',0.5,1.5,0.5,1.5,False),('naive',None,None,None,None,True)]:
    for N in (64,96):
        vals={}
        for m in (25.6,51.2,102.4):
            law=Law(b1,b2,0.0,c1,c2,m,naive_photon=nv)
            ce,ct,_=ce2_minus_1(law,N,lam,h=0.02); vals[m]=ce/2*U
        r1=2*vals[51.2]-vals[25.6]; r2=2*vals[102.4]-vals[51.2]
        r3=(4*r2-r1)/3
        cf=inf_const(Law(b1,b2,0.0,c1,c2,1.0,naive_photon=nv),N,lam)
        print('%-6s N=%3d  m=25.6/51.2/102.4: %+.5f %+.5f %+.5f | Richardson(1/m) %+.5f, (1/m,1/m^2) %+.5f | closed form %+.5f'%(lab,N,vals[25.6],vals[51.2],vals[102.4],r2,r3,cf),flush=True)
print('(4) closed form vs lam (N=96):')
for lab,b1,b2,c1,c2,nv in [('S1',1.0,2.0,1.0,2.0,False),('S3',2.0,3.0,2.0,3.0,False)]:
    print('  %-4s'%lab+'  '.join('lam=%.3f: %+.5f'%(l,inf_const(Law(b1,b2,0.0,c1,c2,1.0),96,l)) for l in (0.1,0.05,0.02,0.0)))
print('(2)-(3) sign-theorem hypotheses on the edge (fine 1D grid in q_x, q_perp samples)')
for lab,b1,b2,c1,c2,nv in [('S1',1.0,2.0,1.0,2.0,False),('S3',2.0,3.0,2.0,3.0,False),('S5',0.5,1.5,0.5,1.5,False),('S7',1.0,3.0,1.0,3.0,False),('S8',2.5,3.1,2.5,3.1,False),('naive',0.0,None,None,None,True)]:
    law=Law(b1 if b1 else None,b2,0.0,c1,c2,1.0,naive_photon=nv)
    b=b1 if b1 else 0.0
    q=np.linspace(max(b,1e-3),np.pi,4001)
    S=law.S(q); H1=np.max(S**2-q**2)
    Aq=deriv(lambda k: law.S(k)**2,q,2)/2-1
    minconv=np.inf; maxdiff=0.0; maxI=-np.inf
    for dperp2 in (0.0,0.01,0.1,0.5,1.0,2.0,4.0,8.0):
        for l in (0.0,0.05):
            dx2=law.d(q)**2; W=np.sqrt(dx2+dperp2+l**2)
            w=(dperp2+l**2)/(dx2*W**3) if dperp2+l**2>0 else None
            if w is None: continue
            wpp=np.gradient(np.gradient(w,q),q)
            minconv=min(minconv,np.min(wpp[5:-5]/np.max(np.abs(w))))
            Idir=np.trapezoid(Aq*w,q)
            Iform=-np.pi*w[-1]+0.5*np.trapezoid((S**2-q**2)*wpp,q)
            maxdiff=max(maxdiff,abs(Idir-Iform)/abs(Idir)); maxI=max(maxI,Idir)
    print('  %-6s b=%.2f  max(S^2-q^2)=%+.2e (H1 %s)  min w\'\'/max|w| = %+.3e (H2 %s)  max_qperp I = %+.4e  |I-formula|/|I| <= %.1e  A range [%+.3f, %+.3f]'
          %(lab,b,H1,'ok' if H1<=1e-12 else 'FAILS',minconv,'ok' if minconv>=-1e-6 else 'FAILS',maxI,maxdiff,Aq.min(),Aq.max()),flush=True)
