"""Independent check of delta_CP extraction: build the PDG matrix at the chart's (s12^2,s13^2,s23^2,dCP) on each of the four sheets and
compare |U|^2 (all nine) and J with the chart's own U for the same sheet."""
import numpy as np, math
from chart import H, obs
pin=(0.657061342210,0.933806343759,0.715042329587)
def pdg(s12,s13,s23,d):
    t12,t13,t23=[math.asin(math.sqrt(x)) for x in (s12,s13,s23)]
    c12,s12_,c13,s13_,c23,s23_=math.cos(t12),math.sin(t12),math.cos(t13),math.sin(t13),math.cos(t23),math.sin(t23)
    e=np.exp(1j*d)
    return np.array([[c12*c13, s12_*c13, s13_*np.conj(e)],
                     [-s12_*c23-c12*s23_*s13_*e, c12*c23-s12_*s23_*s13_*e, s23_*c13],
                     [s12_*s23_-c12*c23*s13_*e, -c12*s23_-s12_*c23*s13_*e, c23*c13]])
def Jinv(U): return (U[0,0]*np.conj(U[0,1])*np.conj(U[1,0])*U[1,1]).imag
worst=0
for g in (0.5,-0.5):
    for perm in [(2,1,0),(2,0,1)]:
        o=obs(*pin,g,perm)
        w,V=np.linalg.eigh(H(*pin,g)); idx=np.argsort(w.real); P=V[:,idx][list(perm),:]
        U=pdg(o['s12'],o['s13'],o['s23'],math.radians(o['dcp']))
        dm=np.max(abs(abs(U)**2-abs(P)**2)); dJ=abs(Jinv(U)-Jinv(P))
        worst=max(worst,dm,dJ)
        print('gamma %+.1f perm %s dCP=%.3f  max||U|^2 diff|=%.2e  |J diff|=%.2e  J=%+.6f'%(g,perm,o['dcp'],dm,dJ,Jinv(P)))
print('worst',worst)
