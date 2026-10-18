import numpy as np
from chi import *
def proj_sector(char, part):
    """projector on the 144-dim operator space onto channels with O character `char` (A1/A2) and real/imag `part`"""
    S=np.zeros((144,144),complex)
    for k in range(24):
        sg=1.0 if char=='A1' else (-1.0)**W1[k]
        T=np.array([[np.vdot(Bm[a],SM[k]@Bm[b]@SM[k].T) for b in range(144)] for a in range(144)])
        S+=sg*T
    S/=24
    Kp=np.diag([1.0 if kinds[a]==part else 0.0 for a in range(144)])
    P=S@Kp; P=(P+P.conj().T)/2
    w,V=np.linalg.eigh(P); return V[:,w>0.5]
def report(params,label):
    bl,_=build(params); mu=np.linalg.eigvalsh(Hk(bl,kst))[0]
    out={}
    for name,Qv in (('0',np.zeros(3)),('Q',Q)):
        chi=chi_matrix(bl,mu,Qv)
        idv=np.array([np.trace(B).real for B in Bm])/np.sqrt(12); Pr=np.eye(144)-np.outer(idv,idv)
        out[(name,'all')]=np.linalg.eigvalsh(Pr@chi@Pr)[-1]
        for char in ('A1','A2'):
            for part in ('real','imag'):
                Vs=proj_sector(char,part)
                if Vs.shape[1]==0: continue
                Vs=Pr@Vs; Vs,_=np.linalg.qr(Vs); 
                w=np.linalg.eigvalsh(Vs.conj().T@chi@Vs)
                out[(name,char,part)]=(round(w[-1],4), Vs.shape[1])
    print(label); 
    for k,v in out.items(): print('   ',k,v)
if __name__=='__main__':
    rng=np.random.default_rng(11); xv=rng.normal(size=len(Xb)); xv/=np.linalg.norm(xv); X=np.tensordot(xv,Xb,1); xv=xv/np.abs(X).max()
    report((-1.0,0.2,0.05,xv),'C19 base parameters (metallic at the node)')
