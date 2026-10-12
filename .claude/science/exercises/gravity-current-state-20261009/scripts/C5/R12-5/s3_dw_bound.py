# R12-5 s3: quantitative frozen-constraint bound (Lemma DW-q), checked on random states and on ground states.
# Setting: Z_N clocks, X|n>=w^n|n>, Z|n>=|n+1>, X^r Z^s = w^(r.s) Z^s X^r.  W = Z^s a constraint stabilizer, X^r an E-character with c=r.s != 0 mod N.
# Claim: |<X^r>| <= 2 sqrt(2 sigma) / |1-w^c|,  sigma = <1 - Re W>  (local constraint-violation of the state).
# Proof: <X^r> - <W^dag X^r W> = <X^r>(1-w^c) [since W^dag X^r W = w^c X^r]; |<a|X|a>-<b|X|b>| <= 2|a-b| for unit a,b, unitary X; |psi - W psi|^2 = 2 sigma.
import numpy as np, itertools, sys
rng=np.random.default_rng(5)
out=[]
def P(*a):
    s=' '.join(str(x) for x in a); print(s); out.append(s)
def clock(N):
    w=np.exp(2j*np.pi/N); X=np.diag(w**np.arange(N)); Z=np.roll(np.eye(N),1,axis=0); return X,Z,w
def kron_list(ms):
    M=np.array([[1.0+0j]])
    for m in ms: M=np.kron(M,m)
    return M
def opower(A,k):
    k=k%A.shape[0] if False else k
    return np.linalg.matrix_power(A,k) if k>=0 else np.linalg.matrix_power(A.conj().T,-k)
worst=0
for N in [2,3,5,8]:
    X,Z,w=clock(N)
    for (r,s) in [((1,0,0),(1,1,0)),((1,1,0),(1,-1,1)),((2,0,1),(1,0,-4))]:
        c=int(np.dot(r,s))%N
        if c==0: continue
        Xr=kron_list([opower(X,ri) for ri in r]); W=kron_list([opower(Z,si) for si in s])
        assert np.allclose(Xr@W, w**np.dot(r,s)*W@Xr)
        for t in range(300):
            psi=rng.normal(size=N**3)+1j*rng.normal(size=N**3)
            if t%3==0:   # bias toward nearly-frozen states: mix a W-eigenvector with noise
                ev,V=np.linalg.eig(W); v=V[:,np.argmin(np.abs(ev-1))]; psi=v+rng.uniform(0,0.3)*psi/np.linalg.norm(psi)
            psi/=np.linalg.norm(psi)
            ex=abs(psi.conj()@Xr@psi); sig=1-np.real(psi.conj()@W@psi)
            bound=2*np.sqrt(2*max(sig,0))/abs(1-w**c)
            worst=max(worst,ex-bound)
P(f"random-state check over N in (2,3,5,8), 3 (r,s) pairs, 300 states each: max(|<X^r>| - bound) = {worst:.3e} (<= 0 means bound holds)")
P("== ground states of H = -J Re X^r - U Re W (one clock pair, c=r.s=1): weak stiffness proxy <X^r> vs violation sigma ==")
for N in [5,16,64]:
    X,Z,w=clock(N); Xr=np.kron(X,np.eye(N)); W=np.kron(Z,Z)   # r=(1,0), s=(1,1): c=1
    for U in [0.0,0.3,1,3,10,100]:
        H=-0.5*(Xr+Xr.conj().T)-U*0.5*(W+W.conj().T)
        e,V=np.linalg.eigh(H); g=V[:,0]
        ex=abs(g.conj()@Xr@g); sig=1-np.real(g.conj()@W@g)
        P(f"N={N:3d} U/J={U:6.1f}: <X^r>={ex:.4f}  sigma={sig:.2e}  bound={min(1,2*np.sqrt(2*max(sig,0))/abs(1-w)):.4f}")
open(__file__.replace('.py','.out'),'w').write('\n'.join(out)+'\n')
