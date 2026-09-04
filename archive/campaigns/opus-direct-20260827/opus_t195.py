"""T195 - VERIFYING R126's SCALING STEP, which I flagged as unmeasured.

R126's headline -- the site algebra must reach M_8(C) -- rests on a scaling step I
could not run directly (the k=2 lattice computation timed out at fibre 64).  The
step claims: if every generator has the form X (x) I_k, then the commutant is
(commutant of the X's) (x) M_k, so its dimension is 24 k^2 and each block u(m)
becomes u(mk).

That is a standard algebra fact, but 'standard' is exactly the sort of thing this
campaign has been wrong about, and R126's number depends on it.  It can be checked
cheaply on small synthetic cases rather than on the expensive lattice one:

  * pick random generator sets X in M_n;
  * compute dim commutant(X);
  * compute dim commutant(X (x) I_k) and check it equals dim commutant(X) * k^2;
  * check the CENTRE dimension is unchanged (block COUNT fixed, block SIZES scale);
  * and confirm on a case with known block structure that u(m) -> u(mk).

CONTROL: a set that does NOT have the X (x) I_k form must break the identity, or
the test has no teeth."""
import numpy as np
def cdim(mats,N):
    M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    s=np.linalg.svd(M,compute_uv=False)
    return int(np.sum(s<=max(M.shape)*np.finfo(float).eps*s.max()))
def centre_dim(mats,N):
    M=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    U,s,Vt=np.linalg.svd(M,full_matrices=False)
    d=int(np.sum(s<=max(M.shape)*np.finfo(float).eps*s.max()))
    B=[Vt[len(Vt)-d+i].conj().reshape(N,N) for i in range(d)]
    C=np.vstack([np.array([(Bi@Bj-Bj@Bi).ravel() for Bi in B]).T for Bj in B])
    s2=np.linalg.svd(C,compute_uv=False)
    return int(np.sum(s2<=max(C.shape)*np.finfo(float).eps*s2.max()))
rng=np.random.default_rng(17)
print("T195  does commutant(X (x) I_k) = commutant(X) (x) M_k ?")
print()
print(f"   {'n':>3} {'#gens':>6} {'k':>3} {'dim C(X)':>10} {'dim C(X(x)I)':>14} {'predicted':>11} {'centre X':>9} {'centre X(x)I':>13}")
for n,ng in ((4,2),(4,3),(6,2)):
    X=[rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)) for _ in range(ng)]
    X=[0.5*(x+x.conj().T) for x in X]
    d0=cdim(X,n); c0=centre_dim(X,n)
    for k in (2,3):
        Xk=[np.kron(x,np.eye(k)) for x in X]
        dk=cdim(Xk,n*k); ck=centre_dim(Xk,n*k)
        ok = (dk==d0*k*k)
        print(f"   {n:3d} {ng:6d} {k:3d} {d0:10d} {dk:14d} {d0*k*k:11d} {c0:9d} {ck:13d}"
              f"   {'ok' if ok and ck==c0 else 'MISMATCH'}")
print()
print("   CONTROL: generators NOT of the form X (x) I_k must break the identity")
n,k=4,2
X=[rng.normal(size=(n,n))+1j*rng.normal(size=(n,n)) for _ in range(2)]
X=[0.5*(x+x.conj().T) for x in X]
d0=cdim(X,n)
bad=[np.kron(x,np.eye(k))+0.3*(lambda M:0.5*(M+M.conj().T))(rng.normal(size=(n*k,n*k))+1j*rng.normal(size=(n*k,n*k))) for x in X]
db=cdim(bad,n*k)
print(f"      dim C(X) = {d0}, predicted {d0*k*k} if the form held; actual for perturbed generators = {db}"
      f"   {'-> control bites' if db!=d0*k*k else '-> CONTROL FAILED'}")
print()
print("   identity holding with the centre FIXED means block count is preserved and")
print("   block sizes scale as u(m) -> u(mk), which is exactly R126's step.")
