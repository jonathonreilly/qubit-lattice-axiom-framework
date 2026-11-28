# GUIDE-grade check of Lemma KIN's algebra on a finite non-abelian group (Q_8).
# One transverse link (two transverse sites x, x'), slice of n sites in direction 1.
# It may refute the identity R T R^-1 = S* D S; it proves nothing.
import itertools, sys
import numpy as np
np.set_printoptions(precision=6, suppress=True, linewidth=160)
I2=np.eye(2,dtype=complex); qi=np.array([[1j,0],[0,-1j]]); qj=np.array([[0,1],[-1,0]],dtype=complex); qk=qi@qj
els=[I2,-I2,qi,-qi,qj,-qj,qk,-qk]
def idx(m):
    for t,e in enumerate(els):
        if np.allclose(m,e): return t
    raise ValueError
mul=np.array([[idx(a@b) for b in els] for a in els]); inv=np.array([idx(a.conj().T) for a in els])
x=np.array([0.5*np.trace(e).real for e in els])
def wt(beta):
    w=np.exp(beta*x); return w/w.sum()
def build(n,bL,bM,face=False):
    N=8**n
    confs=list(itertools.product(range(8),repeat=n))
    pos={c:i for i,c in enumerate(confs)}
    wL=wt(bL); wM=wt(bM)
    # face potential: bonds k,k+1 : x(Phi_{k+1} Phi_k^{-1})
    Vf=np.array([-bM*sum(x[mul[c[k+1],inv[c[k]]]] for k in range(n-1)) for c in confs])
    # K_Phi
    K1=np.array([[wM[mul[b,inv[a]]] for b in range(8)] for a in range(8)])  # kernel w(Phi' Phi^-1)
    K=K1
    for _ in range(n-1): K=np.kron(K,K1)
    ev,U=np.linalg.eigh(K); ev=np.clip(ev,0,None); Ksq=(U*np.sqrt(ev))@U.T
    # M: h(Phi) -> sum w(V..)w(V'..) h(g_V Phi g_V'^-1), g(k)=V_1...V_{k-1}
    M=np.zeros((N,N))
    if face:
        M=np.eye(N)
    else:
        for Vs in itertools.product(range(8),repeat=n-1):
            pV=np.prod([wL[v] for v in Vs]); g=[0]
            for v in Vs: g.append(mul[g[-1],v])
            for Ws in itertools.product(range(8),repeat=n-1):
                pW=np.prod([wL[v] for v in Ws]); gp=[0]
                for v in Ws: gp.append(mul[gp[-1],v])
                for i,c in enumerate(confs):
                    c2=tuple(mul[mul[g[k],c[k]],inv[gp[k]]] for k in range(n))
                    M[i,pos[c2]]+=pV*pW
    E=np.diag(np.exp(-Vf/2))
    A=E@Ksq@M@Ksq@E
    # projector on G-invariant functions: Phi_k -> g Phi_k g'^-1
    P=np.zeros((N,N))
    for g in range(8):
        for gp in range(8):
            for i,c in enumerate(confs):
                P[i,pos[tuple(mul[mul[g,c[k]],inv[gp]] for k in range(n))]]+=1/64
    return dict(A=A,P=P,M=M,K=K,Vf=Vf,confs=confs,pos=pos,wL=wL,wM=wM,Ksq=Ksq,E=E)
def brute(n,bL,bM,d):
    # (T f)(1,Phi) with f(a,Phi)=h(g_a Phi g'_a^-1), computed from T=e^{-V/2}K_a K_Phi e^{-V/2}
    confs=d['confs']; pos=d['pos']; wL=d['wL']; wM=d['wM']; N=len(confs)
    B=np.zeros((N,N))
    for Vs in itertools.product(range(8),repeat=n-1):
        pV=np.prod([wL[v] for v in Vs]); g=[0]
        for v in Vs: g.append(mul[g[-1],v])
        for Vp in itertools.product(range(8),repeat=n-1):
            pVp=np.prod([wL[v] for v in Vp]); gp=[0]
            for v in Vp: gp.append(mul[gp[-1],v])
            for Ws in itertools.product(range(8),repeat=n):
                pW=np.prod([wM[v] for v in Ws])
                for i,c in enumerate(confs):
                    phi=[mul[Ws[k],c[k]] for k in range(n)]          # W Phi
                    # V(a=V, W Phi): plaquette a_x(k) Phi_{k+1} a_x'(k)^-1 Phi_k^-1
                    pot=sum(x[mul[mul[mul[Vs[k],phi[k+1]],inv[Vp[k]]],inv[phi[k]]]] for k in range(n-1))
                    c2=tuple(mul[mul[g[k],phi[k]],inv[gp[k]]] for k in range(n))
                    B[i,pos[c2]]+=pV*pVp*pW*np.exp(0.5*bM*pot)
    return d['E']@B
def gap(A,P):
    ev=np.sort(np.linalg.eigvalsh(P@((A+A.T)/2)@P))[::-1]
    return np.log(ev[0]/ev[1]), ev[:3]
if __name__=="__main__":
    n=2
    for bL,bM in [(0.7,1.1),(2.4,2.4)]:
        d=build(n,bL,bM); B=brute(n,bL,bM,d); A=d['A']; P=d['P']
        print("n=2 bL=%.2f bM=%.2f  ||P(B-A)P||=%.2e  ||B-A||=%.2e  ||[M,K]||=%.2e  M sym %.1e  spec(M) in [%.4f,%.4f]"%(
            bL,bM,np.abs(P@(B-A)@P).max(),np.abs(B-A).max(),np.abs(d['M']@d['K']-d['K']@d['M']).max(),np.abs(d['M']-d['M'].T).max(),np.linalg.eigvalsh((d['M']+d['M'].T)/2).min(),np.linalg.eigvalsh((d['M']+d['M'].T)/2).max()))
    for n in (2,3):
        for bM in (0.5,1.0,2.4):
            f=build(n,1.0,bM,face=True); mf,evf=gap(f['A'],f['P'])
            row=[]
            for bL in (0.0,0.5,1.0,2.4,5.0,10.0,20.0):
                d=build(n,bL,bM); m,ev=gap(d['A'],d['P']); row.append((bL,m,ev[0]/evf[0]))
            print("n=%d bM=%.1f face gap=%.6f  "%(n,bM,mf)+"  ".join("bL=%g: gap=%.5f lam0/face=%.4f"%r for r in row))
