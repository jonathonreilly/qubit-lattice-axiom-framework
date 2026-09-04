"""
T226 - does the fourth direction also REMOVE the dynamics freedom?

R138 (on Z^3): the record measure fixes the ground state sqrt(mu), but the jump
RATES are free -- Metropolis and heat-bath gave the same ground state and
DIFFERENT gaps (2.055 vs 1.212).  The leftover freedom was exactly the formation
rate the axioms disclaim.

On Z^4 with x4 read as time there is no Markov process to choose rates for: the
dynamics is the TRANSFER MATRIX along x4, whose kernel is fixed by the same
measure with no remaining choice.

    T[c', c] = P(c)^{1/2} * prod_i phi(c_i, c'_i) * P(c')^{1/2}
    P(c)     = prod_{spatial edges} phi(c_a, c_b)          (within one slice)

Checks: T symmetric; T positive definite (reflection positivity => H = -log T
self-adjoint and bounded below); and NO free parameter anywhere in its
construction.
"""
import numpy as np, itertools

MENU = np.array([[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]], float)
M = 6; DOT = MENU @ MENU.T

def transfer(N, lam, ring=True):
    cfg = list(itertools.product(range(M), repeat=N))
    n = len(cfg)
    edges = [(i,(i+1) % N) for i in range(N)] if ring else [(i,i+1) for i in range(N-1)]
    if N == 2 and ring: edges = [(0,1)]
    P = np.array([np.prod([1+lam*DOT[c[a],c[b]] for a,b in edges]) for c in cfg])
    Tt = np.zeros((n,n))
    for i,c in enumerate(cfg):
        for j,d in enumerate(cfg):
            Tt[i,j] = np.prod([1+lam*DOT[c[k],d[k]] for k in range(N)])
    T = np.sqrt(P)[:,None]*Tt*np.sqrt(P)[None,:]
    return T, P, cfg

print("=== the Z^4-style transfer matrix (x4 = time) ===")
for N in (2, 3, 4):
    for lam in (0.5, 1.0):
        T, P, cfg = transfer(N, lam)
        sym = np.max(np.abs(T-T.T))
        ev = np.linalg.eigvalsh(T)
        tol = max(T.shape)*np.finfo(float).eps*np.max(np.abs(ev))
        rank = int(np.sum(ev > tol))
        # the single-site kernel 1+lam(v.v') has rank 4 (l=0 and l=1 only, T217),
        # so T has an exact kernel; the physical Hilbert space is its range.
        E = np.sort(-np.log(ev[ev > tol]))
        print(f"  N={N} spatial sites, lam={lam}: dim {len(cfg):5d}  "
              f"symmetry {sym:.1e}  min eig {ev.min():+.1e} (tol {tol:.1e}) -> "
              f"{'PSD' if ev.min() > -tol else 'NOT PSD'};  "
              f"rank {rank} (expect 4^N = {4**N})")
        print(f"      H = -log T :  E0 = {E[0]:+.6f}   gap = {E[1]-E[0]:.6f}"
              f"   (ONE value - nothing to choose)")

print("""
=== contrast with R138 on Z^3 ===
  Z^3, Markov: ground state fixed, RATES FREE.
      3-site path, lam=1: gap 2.055 (Metropolis) vs 1.212 (heat-bath)
      -> same ground state, different spectra; the free object is the rate,
         which is exactly what the axioms decline to supply.
  Z^4, transfer matrix: the kernel is built from the measure alone.
      There is no rate to choose.  The spectrum above is THE spectrum.""")

print("\n=== reflection positivity is what makes this work (T217) ===")
print("  the edge kernel 1 + lam (v.v') is PSD for lam >= 0 (Funk-Hecke:")
print("  eigenvalues 4pi and 4pi*lam/3), which is exactly the condition for the")
print("  transfer matrix to be positive and H = -log T to be self-adjoint.")
