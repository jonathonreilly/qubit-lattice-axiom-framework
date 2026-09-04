import numpy as np, math, itertools, sys, time
from lattice import build, bloch_spectra

def dK(L, eps, P, k, svals, chunk=4096, improve=True, cov=True):
    rp = build(L,eps,P,k); rf = build(L,0.0,P,k)
    qs = np.array(list(itertools.product(range(L),repeat=3)),dtype=float)*(2*np.pi/L)
    acc = np.zeros(len(svals)); s = np.asarray(svals,float)
    for i in range(0,len(qs),chunk):
        q = qs[i:i+chunk]
        ep,_ = bloch_spectra(L, rp['stencil'], rp['mass'], q, improve, rp['C'] if cov else None)
        ef,_ = bloch_spectra(L, rf['stencil'], rf['mass'], q, improve, rf['C'] if cov else None)
        ep = np.sort(ep,axis=1); ef = np.sort(ef,axis=1)
        for j,sv in enumerate(s):
            acc[j] += np.sum(np.exp(-sv*ep)-np.exp(-sv*ef))
    return acc, rp['vol']-rf['vol'], rp['S']-rf['S']

def go(L, P, name, nwave=1, eps=0.05, svals=None, cov=True, improve=True):
    k = 2*math.pi*nwave/L
    if svals is None: svals = [2.0,3.0,4.0,5.0,6.0,8.0,10.0,13.0,16.0,20.0,25.0]
    t0=time.time(); d,dV,dS = dK(L,eps,P,k,svals,cov=cov,improve=improve); t=time.time()-t0
    print("=== L=%d n=%d eps=%g  %s   dVol=%.5f  dS_Regge=%.5f   [%.0fs]"%(L,nwave,eps,name,dV,dS,t))
    print("    s     (4pi s)^2 dK      minus dVol      s*dS/3        ratio")
    out=[]
    for sv,dd in zip(svals,d):
        F=(4*math.pi*sv)**2*dd; num=F-dV; den=sv*dS/3.0
        out.append((sv,F,num,den,num/den))
        print("  %5.1f   %14.6f   %13.6f  %13.6f   %9.5f"%(sv,F,num,den,num/den))
    a=np.array(out)
    # linear fit of F(s) over the window, slope should be dS/3
    m=(a[:,0]>=3)&(a[:,0]<=12)
    c=np.polyfit(a[m,0],a[m,1],1)
    print("    fit F(s)=A+B s on s in [3,12]:  A=%.5f (dVol=%.5f, rel %+.3e)   B=%.6f  3B/dS=%.5f"
          %(c[1],dV,c[1]/dV-1,c[0],3*c[0]/dS))
    return a

if __name__=="__main__":
    which=sys.argv[1]
    if which=="L32":
        go(32,(0,1,-1,0),"traceless (0,1,-1,0)",1)
        go(32,(1,1,1,1),"conformal (1,1,1,1)",1)
        go(32,(0,1,-1,0),"traceless, n=2",2)
        go(32,(1,1,1,1),"conformal, n=2",2)
    elif which=="eps":
        go(32,(0,1,-1,0),"traceless eps=0.1",1,eps=0.1)
        go(32,(0,1,-1,0),"traceless eps=0.025",1,eps=0.025)
    elif which=="L64":
        sv=[2.0,3.0,4.0,5.0,6.0,8.0,10.0,13.0,16.0,20.0,25.0,32.0,40.0,50.0]
        go(64,(0,1,-1,0),"traceless (0,1,-1,0)",1,svals=sv)
        go(64,(1,1,1,1),"conformal (1,1,1,1)",1,svals=sv)
