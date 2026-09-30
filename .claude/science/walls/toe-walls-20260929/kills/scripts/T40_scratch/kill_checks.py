import numpy as np
from t40_consts import *
A2=a2()
print("=== K1: F1 in coupling form with different g2 definitions (v=v_GF)")
for lab,g in (("lattice-1/2 SM-b2 one-loop run (attack)",0.6378),("repo g_2(v) bounded, COMPLETE_PREDICTION_CHAIN",0.6480),("repo alt g_2(v)",0.6463),("SM MSbar g2(mZ)",0.6517),("on-shell 2mW/v (circular)",2*MW/V_GF)):
    print("  %-45s g2=%.4f  a2 dev %+.3f%%"%(lab,g,(g*V_GF/512/A2-1)*100))
print("=== K2: F2r sensitivity to which quenched P (0.5934 note vs 0.59374 infinite-volume beta=6 SU(3))")
for P in (0.5934,0.59374):
    print("  P=%.5f F2r dev %+.4f%%  F2a dev %+.3f%%  v_chain %.3f GeV (%+.3f%%)"%(P,(ABARE*alphaLM(P)*V_GF/MTAU-1)*100,(mtau_chain(P)/MTAU-1)*100,v_chain(P)/1000,(v_chain(P)/V_GF-1)*100))
print("=== K3: shape (Koide Q) in pole vs 1-loop-QED MSbar masses (same formula as attack test 5)")
M=np.array([ME,MMU,MTAU])
def Q(m): return sum(m)/sum(np.sqrt(m))**2
def shape(m):
    a=a2(tuple(m)); return m[2]/a
print("  pole:            Q=%.7f  mtau/a2=%.5f  (koide shape delta=2/9: %.5f)"%(Q(M),shape(M),koide_shape()))
for lab,mu in (("MSbar(m_tau)",MTAU),("MSbar(m_W)",MW)):
    m=M*(1-(1/137.036/np.pi)*(1+0.75*np.log(mu**2/M**2)))
    print("  %-16s Q=%.7f  (dev from 2/3 %+.3f%%)  mtau/a2=%.5f (vs 2/9 shape %+.3f%%)"%(lab,Q(m),(Q(m)/(2/3)-1)*100,shape(m),(shape(m)/koide_shape()-1)*100))
print("  pole Q dev from 2/3: %+.5f%%"%((Q(M)/(2/3)-1)*100))
