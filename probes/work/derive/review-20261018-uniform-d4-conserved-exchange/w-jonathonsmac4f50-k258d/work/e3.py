from ana import *
OFF,Sm=d4cone(); C=CA(OFF,Sm)
R0,D0,ls=segment_readings(C,np.zeros(4))
SYM=[(a,b) for a in range(4) for b in range(a,4)]
def tens(v):
    T=np.zeros((4,4),complex)
    for j,(a,b) in enumerate(SYM): T[a,b]=T[b,a]=v[j]
    return T
def cons_basis(qq):
    w=np.exp(-1j*qq);A=np.zeros((4,10),complex)
    for j,(a,b) in enumerate(SYM):
        E_=np.zeros((4,4));E_[a,b]=E_[b,a]=1;A[:,j]=(w-1)@E_
    U,sv,Vh=np.linalg.svd(A);N=Vh[4:].conj()
    return [tens(v) for v in N],w
def Kmat(C,qq,kap,Ts,w):
    # Q^+ on gauge complement (real q)
    Q=C.Q(qq);G=C.gauge(qq);U,sv,Vh=np.linalg.svd(G,full_matrices=True);B=U[:,32:]
    red=B.conj().T@Q@B;inv=np.linalg.inv(red);Qi=B@inv@B.conj().T
    Bs=np.array([couple(T,w,kap)/ls**2 for T in Ts])
    Rp=segment_readings(C,qq)[0];Rm=segment_readings(C,-qq)[0]
    K=np.conj(Bs)@Rp@Qi@Rm.T@Bs.T*(qq@qq)
    return K,Bs
def F(Ts,alpha,beta):
    Tc=[T/2 for T in Ts]
    return np.array([[alpha*np.sum(a.conj()*b)+beta*np.conj(np.trace(a))*np.trace(b) for b in Tc] for a in Tc])
if __name__=="__main__":
    np.set_printoptions(linewidth=200,precision=5)
    for nm,d in dict(axis=[0,1,0,0],tick=[0,0,0,1],generic=[.3,-.5,.6,.55],body=[1,1,1,1],g2=[.9,.2,-.4,.1]).items():
        d=np.array(d,float);d/=np.linalg.norm(d)
        for t in (.04,.02,.01,.005):
            qq=t*d;Ts,w=cons_basis(qq);K,Bs=Kmat(C,qq,0.0,Ts,w)
            X=np.array([[np.sum((a/2).conj()*(b/2)),np.conj(np.trace(a/2))*np.trace(b/2)] for a in Ts for b in Ts])
            co=np.linalg.lstsq(X,K.ravel(),rcond=None)[0];fit=np.linalg.norm(X@co-K.ravel())/np.linalg.norm(K.ravel())
            Fm=F(Ts,-4,4/3);rel=np.linalg.norm(K-Fm)/np.linalg.norm(Fm)
            print(nm,t,'fit',fit,'coef',co,'resid vs (-4,4/3)',rel, 'herm',np.abs(K-K.conj().T).max())
