import numpy as np
from w1_core import *
m=1.0; tn,wn=tquad(24,9.); L=16; d=0.02
for ch,mono in [('E',((0,0,0),(0,0,0),(0,0,0),(1,0,0))),('E',((0,0,0),(0,0,0),(1,0,0),(1,0,0))),('T2',((0,0,0),(0,0,0),(1,0,0),(0,1,0)))]:
    J,W=strained(L,m,0,ch); fld=Field(gx_from_k(J,W,tn),wn); fd=Field(gdot_x(L,m,ch,tn),wn)
    Lex=L_mono(fld,fd,mono); vals={}
    for e in [-d/2,d/2,-d,d]:
        J,W=strained(L,m,e,ch); f2=Field(gx_from_k(J,W,tn),wn)
        p=f2.sh(mono[0])*f2.sh(mono[1])*f2.sh(mono[2])*f2.sh(mono[3]); vals[e]=float(np.dot(wn,p.reshape(len(tn),-1).sum(1)))
    Lfd=(4*(vals[d/2]-vals[-d/2])/d-(vals[d]-vals[-d])/(2*d))/3
    print(f'{ch} mono {mono}: exact gdot L = {Lex:.10e}  FD = {Lfd:.10e}  rel diff {abs(Lex-Lfd)/abs(Lfd):.1e}')
