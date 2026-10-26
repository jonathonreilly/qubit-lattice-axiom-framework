from e3 import *
def cons_basis_c(q):
    w=np.exp(-1j*q);A=np.zeros((4,10),complex)
    for j,(a,b) in enumerate(SYM):
        E_=np.zeros((4,4));E_[a,b]=E_[b,a]=1;A[:,j]=(w-1)@E_
    U,sv,Vh=np.linalg.svd(A);N=Vh[4:].conj()
    # null space of A: rows of Vh[4:]^* are null vectors v with A v = 0
    return [tens(v) for v in N],w
def Kc(C,q,kap,lam=1.0):
    Tr,w=cons_basis_c(q); Tl,wm=cons_basis_c(-q)
    Br=np.array([couple(T,w,kap)/ls**2 for T in Tr]); Bl=np.array([couple(T,wm,kap)/ls**2 for T in Tl])
    Rp=segment_readings(C,q)[0];Rm=segment_readings(C,-q)[0]
    Q=C.Q(q);G=C.gauge(q);Gm=C.gauge(-q)
    right=Rm.T@Br.T; left=Bl@Rp
    X=np.linalg.solve(Q+lam*G@Gm.T,right)
    K=left@X*(q@q)
    return K,Tl,Tr,w,wm,np.linalg.norm(Gm.T@right)/np.linalg.norm(right),np.linalg.norm(left@G)/np.linalg.norm(left)
def Fw(Tl,Tr,w,wm,al,be):
    return np.array([[al*np.sum((a/2)*(b/2))+be*np.sum(wm*np.diag(a/2))*np.sum(w*np.diag(b/2)) for b in Tr] for a in Tl])
def F0(Tl,Tr,al,be):
    return np.array([[al*np.sum((a/2)*(b/2))+be*np.trace(a/2)*np.trace(b/2) for b in Tr] for a in Tl])
if __name__=="__main__":
    OFF,Sm=d4cone();C=CA(OFF,Sm)
    rng=np.random.default_rng(1)
    # first check real q reproduces
    q=0.01*np.array([.3,-.5,.6,.55]);K,Tl,Tr,w,wm,gw1,gw2=Kc(C,q+0j,0.0);print('real q:',np.linalg.norm(K-Fw(Tl,Tr,w,wm,-4,4/3))/np.linalg.norm(Fw(Tl,Tr,w,wm,-4,4/3)),gw1,gw2)
    for trial in range(6):
        z=rng.standard_normal(4)+1j*rng.standard_normal(4);z/=np.sqrt(abs(z@z)); 
        out=[]
        for t in (.02,.01):
            q=t*z;K,Tl,Tr,w,wm,g1,g2=Kc(C,q,0.0)
            a=Fw(Tl,Tr,w,wm,-4,4/3);b=F0(Tl,Tr,-4,4/3)
            out.append((np.linalg.norm(K-a)/np.linalg.norm(a),np.linalg.norm(K-b)/np.linalg.norm(b),g1,g2))
        print('z.z=',z@z,'ratio Fw',out[0][0]/out[1][0],'ratio F0',out[0][1]/out[1][1],out[1])
