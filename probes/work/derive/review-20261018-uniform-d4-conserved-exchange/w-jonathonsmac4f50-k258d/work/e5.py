from e3 import *
def Ftil(Ts,qq,sgn,alpha,beta):
    ph=np.exp(sgn*0.5j*(qq[:,None]+qq[None,:]))
    Tc=[(T/2)*ph for T in Ts]
    return np.array([[alpha*np.sum(a.conj()*b)+beta*np.conj(np.trace(a))*np.trace(b) for b in Tc] for a in Tc])
for nm,d in dict(generic=[.3,-.5,.6,.55],g2=[.9,.2,-.4,.1],axis=[0,1,0,0],body=[1,1,1,1],g3=[.1,.2,.3,.9]).items():
    d=np.array(d,float);d/=np.linalg.norm(d)
    for t in (.04,.02,.01,.005):
        qq=t*d;Ts,w=cons_basis(qq);K,Bs=Kmat(C,qq,0.0,Ts,w);nF=np.linalg.norm(F(Ts,-4,4/3))
        out=[np.linalg.norm(K-Ftil(Ts,qq,s,-4,4/3))/nF for s in (+1,-1)]
        print(nm,t,'K-F',np.linalg.norm(K-F(Ts,-4,4/3))/nF,'K-Ftilde(+,-)',out)
