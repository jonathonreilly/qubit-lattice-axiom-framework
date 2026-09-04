"""T182 - R115's RECONCILIATION DOES NOT HOLD.  Two different 16s.

R115 claimed: "The Kahler-Dirac structure is the axioms' qubit plus lattice
doublers -- not a bigger fibre smuggled in", on the grounds that
      8 doublers x 2 spinor components = 16
matches the realization lane's 16-component fibre.  That matched the COUNT.  R116
then measured the taste algebra of the doubler construction and got u(2), while
T138 had measured the Kahler-Dirac taste algebra as u(4).  Those are DIFFERENT
ALGEBRAS, so the two 16s are not the same structure and the reconciliation fails.

The reason is that they come from different constructions entirely:
   Z^3 + a QUBIT per site   : 2^3 = 8 doublers x 2 spin = 16, taste u(2)   [R116]
   Z^4 + a SCALAR per site  : 2^4 = 16 per hypercube = 4 spin x 4 taste,
                              taste u(4)                                   [T138]
Same total, different lattice, different per-site content, different symmetry.

Check it directly: build both and compare their taste algebras side by side.  If
the dimensions differ, R115's reconciliation is refuted by R116's own data and
must be withdrawn -- the realization lane's Z^4 is NOT recovered from the axioms'
Z^3, and R91's original framing stands after all."""
import numpy as np, itertools
S=[np.array([[0,1],[1,0]],dtype=complex),np.array([[0,-1j],[1j,0]],dtype=complex),
   np.array([[1,0],[0,-1]],dtype=complex)]
def commutant_dim(mats,N):
    A=np.vstack([np.kron(m,np.eye(N))-np.kron(np.eye(N),m.T) for m in mats])
    s=np.linalg.svd(A,compute_uv=False)
    return int(np.sum(s<=max(A.shape)*np.finfo(float).eps*s.max()))
# --- (A) Z^3 + qubit, blocked into 2x2x2  (R116's construction)
R8=[tuple(r) for r in itertools.product([0,1],repeat=3)]; I8={r:i for i,r in enumerate(R8)}
def shift3(a,sg,p):
    M=np.zeros((8,8),dtype=complex)
    for r in R8:
        s=list(r)
        if sg>0:
            if r[a]==0: s[a]=1; ph=1.0
            else: s[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: s[a]=0; ph=1.0
            else: s[a]=1; ph=np.exp(-1j*p[a])
        M[I8[tuple(s)],I8[r]]+=ph
    return M
D3=lambda p: sum(np.kron(shift3(a,1,p)-shift3(a,-1,p),S[a]) for a in range(3))/2.0
# --- (B) Z^4 + scalar, blocked into 2^4  (the staggered / Kahler-Dirac construction)
R16=[tuple(r) for r in itertools.product([0,1],repeat=4)]; I16={r:i for i,r in enumerate(R16)}
def eta(r,a):           # staggered phase
    return (-1)**sum(r[:a])
def shift4(a,sg,p):
    M=np.zeros((16,16),dtype=complex)
    for r in R16:
        s=list(r)
        if sg>0:
            if r[a]==0: s[a]=1; ph=1.0
            else: s[a]=0; ph=np.exp(1j*p[a])
        else:
            if r[a]==1: s[a]=0; ph=1.0
            else: s[a]=1; ph=np.exp(-1j*p[a])
        M[I16[tuple(s)],I16[r]]+=eta(r,a)*ph
    return M
D4=lambda p: sum(shift4(a,1,p)-shift4(a,-1,p) for a in range(4))/2.0
rng=np.random.default_rng(11)
print("T182  are the two 16s the same structure?")
print()
p3=[rng.uniform(-np.pi,np.pi,size=3) for _ in range(40)]
p4=[rng.uniform(-np.pi,np.pi,size=4) for _ in range(40)]
d3=commutant_dim([D3(p) for p in p3],16)
d4=commutant_dim([D4(p) for p in p4],16)
print(f"   (A) Z^3 + qubit,  blocked 2x2x2   : fibre 16, taste algebra dim = {d3}"
      f"   -> u({int(round(np.sqrt(d3)))})")
print(f"   (B) Z^4 + scalar, blocked 2^4     : fibre 16, taste algebra dim = {d4}"
      f"   -> u({int(round(np.sqrt(d4)))})")
print()
print(f"   same total components: 16 = 16")
print(f"   same taste algebra?   {d3} vs {d4}  ->  {'YES' if d3==d4 else 'NO -- different structures'}")
print()
print("   CONTROL: both operators anti-hermitian")
print(f"      (A) max |D+D^dag| = {max(np.abs(D3(p)+D3(p).conj().T).max() for p in p3[:5]):.1e}")
print(f"      (B) max |D+D^dag| = {max(np.abs(D4(p)+D4(p).conj().T).max() for p in p4[:5]):.1e}")
