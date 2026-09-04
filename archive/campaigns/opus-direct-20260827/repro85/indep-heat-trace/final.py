import numpy as np, math, itertools, sys, time
from lattice import build, bloch_spectra
import a2 as A2

def measure(L, P, name, nwave=1, eps=0.05, svals=None, chunk=2048, cov=True):
    k = 2*math.pi*nwave/L
    rp = build(L,eps,P,k); rf = build(L,0.0,P,k)
    dV = rp['vol']-rf['vol']; dS = rp['S']-rf['S']
    _, Ia2 = A2.integrals(L,eps,P,k)
    qs = np.array(list(itertools.product(range(L),repeat=3)),dtype=float)*(2*np.pi/L)
    s = np.asarray(svals,float); acc = np.zeros(len(s)); t0=time.time()
    for i in range(0,len(qs),chunk):
        q = qs[i:i+chunk]
        ep,_ = bloch_spectra(L,rp['stencil'],rp['mass'],q,True,rp['C'] if cov else None)
        ef,_ = bloch_spectra(L,rf['stencil'],rf['mass'],q,True,rf['C'] if cov else None)
        ep=np.sort(ep,axis=1); ef=np.sort(ef,axis=1)
        for j,sv in enumerate(s): acc[j]+=np.sum(np.exp(-sv*ep)-np.exp(-sv*ef))
    F = (4*np.pi*s)**2*acc
    print("=== L=%d n=%d eps=%g  %s"%(L,nwave,eps,name))
    print("    dVol=%.5f  dS_Regge=%.5f  Int a2 (continuum)=%.5f   [%.0fs]"%(dV,dS,Ia2,time.time()-t0))
    print("      s    (4pi s)^2 dK       raw ratio    a2-corrected ratio")
    for sv,f in zip(s,F):
        print("   %6.1f  %15.5f   %10.5f   %10.5f"%(sv,f,(f-dV)/(sv*dS/3),(f-dV-sv*sv*Ia2)/(sv*dS/3)))
    return s,F,dV,dS,Ia2

def fit(s,F,dV,dS,Ia2,lo,hi):
    m=(s>=lo)&(s<=hi)
    Mx=np.vstack([s[m],s[m]**2]).T
    c,*_=np.linalg.lstsq(Mx,F[m]-dV,rcond=None)
    print("    fit (F-dVol)=B s + C s^2 on s in [%g,%g]:  3B/dS_Regge = %.5f   C/Int_a2 = %.4f"
          %(lo,hi,3*c[0]/dS,c[1]/Ia2))
    return 3*c[0]/dS

if __name__=="__main__":
    L=int(sys.argv[1]); which=sys.argv[2]
    sv = {32:[3,4,5,6,8,10,13,16,20,25],
          64:[6,8,10,13,16,20,25,32,40,50,64]}[L]
    if which in ("tt","all"):
        r=measure(L,(0,1,-1,0),"traceless (0,1,-1,0)",svals=sv); fit(*r,lo=sv[1],hi=sv[-3])
    if which in ("cf","all"):
        r=measure(L,(1,1,1,1),"conformal (1,1,1,1)",svals=sv); fit(*r,lo=sv[1],hi=sv[-3])
