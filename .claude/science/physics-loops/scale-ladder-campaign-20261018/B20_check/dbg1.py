from chklib import *
exec(open('chk1_L1_L2.py').read().split('# --- L1 by finite differences')[0].split('# --- little group')[0])
def Honly(): return sum(np.exp(1j*rng.uniform(0,2*np.pi))*P for P in PH)
kl=['S','Si','S2','S2i','R']
def rword(n):
    tuned=rng.random()<0.3; w=[]
    for _ in range(n): w+=[kl[rng.integers(5)], Honly() if tuned else rand_onsite_unitary(rng)]
    return w
worst=[]
for t in range(120):
    w=rword(int(rng.integers(1,5))); ns=nS(w)
    for k0 in (kst,-kst):
        W0=Wword(w,k0)
        for E,m in levels(W0):
            if m not in (2,4): continue
            pred=abs(ns)*np.sqrt(2)/3
            for h in (1e-4,1e-5,1e-6):
                errs=[]
                for d in [np.eye(3)[0],np.array([1,2,-.5])/np.linalg.norm([1,2,-.5])]:
                    a=closest(Wword(w,k0+h*d),E,m)/h
                    errs.append(np.abs(np.abs(a)-pred).max())
                e2=sorted(np.abs(wrap(eigph(W0)-E)))[m]
                worst.append((max(errs),h,m,ns,round(e2,5)))
worst.sort(key=lambda x:-x[0])
for x in worst[:12]: print(x)
# flux control fixed
sx=np.array([[0,1],[1,0]]);sy=np.array([[0,-1j],[1j,0]]);sz=np.diag([1,-1])
def weyl_flux(sgn):
    n=14; th=np.linspace(0,np.pi,n+1); ph=np.linspace(0,2*np.pi,2*n,endpoint=False); U=np.zeros((n+1,2*n,2),complex)
    for i,t in enumerate(th):
        for j,p in enumerate(ph):
            q=np.array([np.sin(t)*np.cos(p),np.sin(t)*np.sin(p),np.cos(t)]); h=sgn*q[0]*sx+q[1]*sy+q[2]*sz
            U[i,j]=np.linalg.eigh(h)[1][:,0]
    tot=0
    for i in range(n):
        for j in range(2*n):
            a,b,c,d=U[i,j],U[i+1,j],U[i+1,(j+1)%(2*n)],U[i,(j+1)%(2*n)]; tot+=np.angle(np.vdot(a,b)*np.vdot(b,c)*np.vdot(c,d)*np.vdot(d,a))
    return tot/(2*np.pi)
print('flux(+)',weyl_flux(1),'flux(-)',weyl_flux(-1))
