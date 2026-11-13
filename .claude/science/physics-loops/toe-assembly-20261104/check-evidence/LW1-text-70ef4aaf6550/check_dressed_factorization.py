# Instance test of the dressed factorization claim: exp(theta*(X1+X2)) is an EXACT finite word in exp(t X1), exp(t X2).
# Instance: 3 sites in a row (two edges sharing a site), spin-S links. Different implementation from the text:
# direct nonlinear least squares for a fixed-length alternating word (no Ad-basis / inverse function construction).
import numpy as np
from functools import reduce
from scipy.optimize import least_squares
def kron(*ms): return reduce(np.kron,ms)
def spin(S):
    d=int(round(2*S+1)); m=np.array([-S+k for k in range(d)]); J=np.zeros((d,d),complex)
    for k in range(d-1): J[k+1,k]=np.sqrt(S*(S+1)-m[k]*(m[k]+1))
    return np.diag(m).astype(complex),J
def fermions(n):
    a=np.array([[0,1],[0,0]],complex); Z=np.diag([1,-1]).astype(complex); I=np.eye(2)
    return [kron(*([Z]*k+[a]+[I]*(n-k-1))) for k in range(n)]
def comm(a,b): return a@b-b@a
for S in (0.5,1):
    E,J=spin(S); d=E.shape[0]; c=[np.kron(x,np.eye(d*d)) for x in fermions(3)]
    J1=np.kron(np.eye(8),np.kron(J,np.eye(d))); J2=np.kron(np.eye(8),np.kron(np.eye(d),J))
    A1=c[1].conj().T@J1@c[0]; A2=c[2].conj().T@J2@c[1]
    H1=(A1+A1.conj().T)/np.sqrt(3); H2=-(A2+A2.conj().T)/np.sqrt(3)   # arbitrary signs eta
    X=[-1j*H1,-1j*H2]; D=X[0].shape[0]
    # dimension of generated Lie algebra
    def span_basis(mats):
        V=np.array([np.concatenate([m.real.ravel(),m.imag.ravel()]) for m in mats])
        u,s,vt=np.linalg.svd(V,full_matrices=False); return vt[:(s>1e-9).sum()]
    tomat=lambda v:(v[:D*D]+1j*v[D*D:]).reshape(D,D)
    basis=span_basis(X)
    while True:
        mats=[tomat(v) for v in basis]; nb=span_basis(mats+[comm(a,b) for a in mats for b in X])
        if len(nb)==len(basis): break
        basis=nb
    g=len(basis)
    eig=[np.linalg.eigh(1j*x) for x in X]   # i*X Hermitian ; exp(tX)=U exp(-i t w) U^dag
    def ex(j,t): w,U=eig[j]; return (U*np.exp(-1j*t*w))@U.conj().T
    wS,US=np.linalg.eigh(1j*(X[0]+X[1]))
    for theta in (0.4,1.3):
        target=(US*np.exp(-1j*theta*wS))@US.conj().T
        best=None
        for m in (g+1,g+3,2*g+2):
            def word(t): return reduce(lambda a,b:a@b,[ex(k%2,t[k]) for k in range(m)])
            def res(t):
                R=word(t)-target; return np.concatenate([R.real.ravel(),R.imag.ravel()])
            rng=np.random.default_rng(3)
            for trial in range(6):
                t0=rng.normal(scale=0.7,size=m)
                sol=least_squares(res,t0,xtol=1e-15,ftol=1e-15,gtol=1e-15,max_nfev=4000)
                err=abs(word(sol.x)-target).max()
                if best is None or err<best[0]: best=(err,m)
                if err<1e-10: break
            if best[0]<1e-10: break
        # Trotter comparison of the same length: not exact
        tro=np.linalg.matrix_power(ex(0,theta/(best[1]//2))@ex(1,theta/(best[1]//2)),best[1]//2)
        print(f"S={S}: dim g={g}; theta={theta}: word length {best[1]} reproduces exp(theta(X1+X2)) to {best[0]:.1e}; Trotter word of same length error {abs(tro-target).max():.1e}")
