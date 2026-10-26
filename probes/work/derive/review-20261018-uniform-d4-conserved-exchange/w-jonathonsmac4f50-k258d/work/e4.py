from e3 import *
def Fproj(Ts,P,alpha,beta):
    Tc=[P@(T/2)@P for T in Ts]
    return np.array([[alpha*np.sum(a.conj()*b)+beta*np.conj(np.trace(a))*np.trace(b) for b in Tc] for a in Tc])
for nm,d in dict(generic=[.3,-.5,.6,.55],g2=[.9,.2,-.4,.1],axis=[0,1,0,0]).items():
    d=np.array(d,float);d/=np.linalg.norm(d);P=np.eye(4)-np.outer(d,d)
    for t in (.04,.02,.01,.005):
        qq=t*d;Ts,w=cons_basis(qq);K,Bs=Kmat(C,qq,0.0,Ts,w)
        F0=F(Ts,-4,4/3);F1=Fproj(Ts,P,-4,4/3)
        nF=np.linalg.norm(F0)
        # also lattice-q projection: use P from sin(q)? 
        s=np.sin(qq)/np.linalg.norm(np.sin(qq));P2=np.eye(4)-np.outer(s,s);F2=Fproj(Ts,P2,-4,4/3)
        w1=(np.exp(-1j*qq)-1);w1=w1/np.linalg.norm(w1);P3=np.eye(4)-np.outer(w1.conj(),w1)
        print(nm,t,'K-F',np.linalg.norm(K-F0)/nF,'K-Fproj(n)',np.linalg.norm(K-F1)/nF,'K-Fproj(sin)',np.linalg.norm(K-F2)/nF, 'projdiff',np.linalg.norm(F0-F1)/nF)
