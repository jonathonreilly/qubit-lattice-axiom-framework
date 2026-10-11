import numpy as np, time
from w1_core import *
m=1.0
for n,b in [(20,9.),(28,9.),(36,9.)]:
    tn,wn=tquad(n,b); print('tquad',n,b,'max rel err 1/s on [3.9,16]:',check_tquad(tn,wn,3.9,16.0))
for r in [1,2,3]:
    t0=time.time(); mon=enumerate_monomials(r); orbs=orbits(mon)
    print('r',r,'monomials',len(mon),'orbits',len(orbs),'%.1fs'%(time.time()-t0))
    for ch in ['E','T2']:
        fs=channel_functions(orbs,ch); print('   ch',ch,'raw functions',len(fs))
# control A vs L2 (I4'' = 2.422366e-05 E ; -3.865936e-07 T2), and L check of gdot vs FD
tn,wn=tquad(28,9.)
for L in [16,24]:
    for ch in ['E','T2']:
        d=0.04; I={e:onsite_I(L,m,e,ch,tn,wn) for e in [-d,-d/2,0,d/2,d]}
        D=lambda e:(I[e]+I[-e]-2*I[0])/e**2; A=(4*D(d/2)-D(d))/3
        # first derivative of a non-symmetric monomial via FD vs gdot
        mono=((0,0,0),(0,0,0),(1,0,0),(0,1,0))
        J,W=strained(L,m,0,ch); fld=Field(gx_from_k(J,W,tn),wn); fd=Field(gdot_x(L,m,ch,tn),wn)
        Lex=L_mono(fld,fd,mono)
        vals={}
        for e in [-d/2,d/2,-d,d]:
            J,W=strained(L,m,e,ch); f2=Field(gx_from_k(J,W,tn),wn)
            p=f2.sh(mono[0])*f2.sh(mono[1])*f2.sh(mono[2])*f2.sh(mono[3]); vals[e]=float(np.dot(wn,p.reshape(len(tn),-1).sum(1)))
        Lfd=(8*(vals[d/2]-vals[-d/2])/d - (vals[d]-vals[-d])/(2*d))/3*1.0
        Lfd=(4*(vals[d/2]-vals[-d/2])/d-(vals[d]-vals[-d])/(2*d))/3
        print(f'L={L} ch={ch}: I4={I[0]:.9e} A=I4\'\'={A:.7e} mu_undressed=-A/24={-A/24:.5e} | L_mono exact {Lex:.9e} FD {Lfd:.9e}')
