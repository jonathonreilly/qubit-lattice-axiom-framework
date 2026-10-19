import sys, itertools, numpy as np
sys.path.insert(0,'/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/c20')
import os; os.chdir('/tmp/claude-0/-home-user-qubit-lattice-axiom-framework/b589b2bf-7a67-5c50-b4cf-6f5868f1e728/scratchpad/c20')
exec(open('diraclib.py').read().split("Xb=np.load")[0])
Hon=H0(1.0,0.0); Hli=H0(0.0,1.0)
blon=blocks_from(Hon); blli=blocks_from(Hli)
Hon0=Hk(blon,np.zeros(3)).real
w_on,V_on=np.linalg.eigh(Hon0)
Ps=[V_on[:,np.abs(w_on-l)<1e-6]@V_on[:,np.abs(w_on-l)<1e-6].T for l in (-1-np.sqrt(3),np.sqrt(3)-1,2.0)]
Lam=np.zeros((12,12),complex)
for s in itertools.product((1,-1),repeat=3):
    x,y,z=(s[0],0,0),(0,s[1],0),(0,0,s[2])
    cy=[frozenset((x,y)),frozenset((y,z)),frozenset((z,x))]
    if round(np.linalg.det(np.array([x,y,z])))<0: cy=cy[::-1]
    for a in range(3):
        q,r=cy[a],cy[(a+1)%3]; i,j=C.VID[((0,0,0),q)],C.VID[((0,0,0),r)]
        amp=1j*(-1.0)**u[C.EID[frozenset((i,j))]]
        Lam[CI[r],CI[q]]+=amp; Lam[CI[q],CI[r]]+=np.conj(amp)
def msign(H):
    w,V=np.linalg.eigh(H); assert np.abs(w).min()>1e-9; return V@np.diag(np.sign(w))@V.conj().T
RL=lambda k: Hk(blli,k)/np.sqrt(2)
def wrap(x): return np.angle(np.exp(1j*x))
def levels(W,k,tol=1e-7):
    e=np.sort(np.angle(np.linalg.eigvals(W(k)))); lv=[]
    for x in e:
        if lv and abs(wrap(x-lv[-1][0]))<tol: lv[-1][1]+=1
        else: lv.append([x,1])
    if len(lv)>1 and abs(wrap(lv[0][0]-lv[-1][0]))<tol: lv[0][1]+=lv[-1][1]; lv.pop()
    return lv
rng=np.random.default_rng(2); DIRS=rng.normal(size=(60,3)); DIRS/=np.linalg.norm(DIRS,axis=1)[:,None]
KG=[rng.uniform(-np.pi,np.pi,3) for _ in range(6)]
def analyse(W,name,k0=None):
    k0=kst if k0 is None else k0
    out=[]
    for E,m in levels(W,k0):
        flat=max(sum(abs(wrap(np.angle(np.linalg.eigvals(W(k)))-E))<1e-6) for k in KG)
        sp={}
        for q in (2e-3,1e-3):
            S=[]
            for d in DIRS:
                ee=wrap(np.angle(np.linalg.eigvals(W(k0+q*d)))-E); S.append(np.sort(ee[np.abs(ee)<0.05])/q)
            sp[q]=np.array(S)
        out.append((round(E,4),m,flat,np.round(sp[1e-3].mean(0),5),np.round(np.ptp(sp[1e-3],0),8),np.round(np.ptp(sp[2e-3],0),8)))
    print(name)
    for o in out: print("   ",o)
    return out
