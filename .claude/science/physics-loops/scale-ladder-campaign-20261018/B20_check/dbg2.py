from chklib import *
rng=np.random.default_rng(99)
def eigsp(M,lam):
    w,V=np.linalg.eigh(M); return V[:,np.abs(w-lam)<1e-6]
Dpm=eigsp(Hon0,2.0)
def Honly(): return sum(np.exp(1j*rng.uniform(0,2*np.pi))*P for P in PH)
kl=['S','Si','S2','S2i','R']
def rword(n):
    tuned=rng.random()<0.3; w=[]
    for _ in range(n): w+=[kl[rng.integers(5)], Honly() if tuned else rand_onsite_unitary(rng)]
    return w
worst=[]
for t in range(150):
    w=rword(int(rng.integers(1,5))); ns=nS(w)
    for k0 in (kst,-kst):
        W0=Wword(w,k0); e,V=np.linalg.eig(W0)
        for E,m in levels(W0):
            if m==4:
                Q,_=np.linalg.qr(V[:,np.abs(wrap(np.angle(e)-E))<1e-6])
                if abs(np.linalg.norm(Q.conj().T@Dpm)**2-4)>1e-6: continue
            elif m!=2: continue
            pred=abs(ns)*np.sqrt(2)/3; e2=sorted(np.abs(wrap(eigph(W0)-E)))[m]
            for h in (1e-4,1e-5,1e-6):
                errs=[]
                for d in [np.eye(3)[0],np.array([1,2,-.5])/np.linalg.norm([1,2,-.5])]:
                    a=closest(Wword(w,k0+h*d),E,m)/h
                    errs.append(np.abs(np.abs(a)-pred).max())
                worst.append((round(max(errs),7),h,m,ns,round(e2,6),t))
worst.sort(key=lambda x:-x[0])
for x in worst[:15]: print(x)
