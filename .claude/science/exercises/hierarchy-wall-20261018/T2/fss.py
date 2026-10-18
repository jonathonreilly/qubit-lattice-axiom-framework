"""M1 finite-size scaling for T-LIGHTCONE. Single-histogram reweighting in the pair-law bond sum E, jackknife errors."""
import numpy as np, glob, re, sys
from scipy.optimize import brentq, curve_fit
NJ=20
def load():
    D={}
    for log in sorted(glob.glob('data/s[123]_L*.log')):
        txt=open(log).read(); m=re.search(r'L=(\d+) beta=([\d.]+)',txt)
        if not m or 'CAPPED' in txt or 'watchdog' not in txt: continue
        L=int(m.group(1)); b0=float(m.group(2)); f=log[:-4]+'.bin'
        raw=np.fromfile(f)
        cfg={8:0,12:0,16:2,24:2,32:3,48:3,64:4}
        rec=4+15*cfg[L]; w=raw.reshape(-1,rec)[:,:4]
        if L in D and D[L][0]==b0: w=np.vstack([D[L][1],w])   # same L and beta: concatenate independent runs
        elif L in D and len(D[L][1])>len(w): continue
        D[L]=(b0,w)
    return D
class Obs:
    def __init__(s,L,b0,w):
        s.L=L; s.b0=b0; s.NV=2*L**3; s.E=w[:,0]; s.m2=w[:,1]; s.fk=w[:,3]
        n=len(s.E)//NJ*NJ; s.E,s.m2,s.fk=s.E[:n],s.m2[:n],s.fk[:n]; s.n=n
        s.blk=np.arange(n)//(n//NJ)
    def q(s,beta,mask=None):
        E,m2,fk=(s.E,s.m2,s.fk) if mask is None else (s.E[mask],s.m2[mask],s.fk[mask])
        x=(beta-s.b0)*(E-E.mean()); w=np.exp(x-x.max()); w/=w.sum()
        M2=(w*m2).sum(); M4=(w*m2*m2).sum(); FK=(w*fk).sum()
        R=M4/M2**2; chi=M2/s.NV; xi=np.sqrt(max(M2/FK-1,1e-12))/(2*np.sin(np.pi/s.L))
        return np.array([R, xi/s.L, chi])
    def qj(s,beta):
        full=s.q(beta); jk=np.array([s.q(beta,s.blk!=j) for j in range(NJ)])
        return full, jk
def deriv(o,beta,h=2e-4,mask=None):
    return (o.q(beta+h,mask)-o.q(beta-h,mask))/(2*h)
def cross(o1,o2,k,lo,hi,mask1=None,mask2=None):
    f=lambda b: o1.q(b,mask1)[k]-o2.q(b,mask2)[k]
    return brentq(f,lo,hi)
def pairstats(o1,o2,k,lo,hi):
    """crossing beta, y_t from slope ratio, y_h from chi ratio; jackknife over blocks (independent runs, same block index)"""
    s=np.log(o2.L/o1.L)
    def one(m1,m2):
        b=cross(o1,o2,k,lo,hi,m1,m2)
        d1=deriv(o1,b,mask=m1)[k]; d2=deriv(o2,b,mask=m2)[k]
        c1=o1.q(b,m1)[2]; c2=o2.q(b,m2)[2]
        Q=o1.q(b,m1)[k]
        return np.array([b, np.log(d2/d1)/s, (3+np.log(c2/c1)/s)/2, Q])
    full=one(None,None)
    jk=np.array([one(o1.blk!=j,o2.blk!=j) for j in range(NJ)])
    err=np.sqrt((NJ-1)/NJ*((jk-jk.mean(0))**2).sum(0))
    return full,err
if __name__=='__main__':
    D=load(); O={L:Obs(L,*D[L]) for L in sorted(D)}
    print('sizes',{L:(O[L].b0,O[L].n) for L in O})
    lo,hi=0.548,0.564
    if len(sys.argv)>1: lo,hi=float(sys.argv[1]),float(sys.argv[2])
    for L in O:
        f,jk=O[L].qj(O[L].b0); e=np.sqrt((NJ-1)/NJ*((jk-jk.mean(0))**2).sum(0))
        print(f'L={L:2d} at beta0={O[L].b0}: R={f[0]:.4f}({e[0]:.4f}) xi/L={f[1]:.4f}({e[1]:.4f}) chi={f[2]:.2f}({e[2]:.2f})')
    Ls=sorted(O); pairs=[(a,b) for a in Ls for b in Ls if b>a and b/a in (1.5,2,4/3)]
    res={}
    for k,name in [(0,'R'),(1,'xi/L')]:
        print(f'--- crossings of {name}: beta_x, y_t, y_h, Q at crossing')
        for a,b in pairs:
            try:
                f,e=pairstats(O[a],O[b],k,lo,hi); res[(k,a,b)]=(f,e)
                print(f'({a:2d},{b:2d}) beta_x={f[0]:.5f}({e[0]:.5f}) y_t={f[1]:.4f}({e[1]:.4f}) y_h={f[2]:.4f}({e[2]:.4f}) Q={f[3]:.4f}({e[3]:.4f})')
            except Exception as ex: print(a,b,'fail',ex)
    np.save('data/fss_res.npy',np.array([(k,a,b,*f,*e) for (k,a,b),(f,e) in res.items()]))
