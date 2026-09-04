"""
T261 - does the framework's ARENA survive partial records?

R132/R135's gravity result (induced Einstein-Hilbert = 1.00000) was computed on
a COMPLETE lattice.  R179/R180 established the axioms allow -- and permanence
implies -- PARTIAL record configurations, with long-range order needing a local
density around 0.5.

So: does the heat trace, the object the whole gravity lane is built on, still
behave like continuum diffusion when sites are missing?

On a diluted Z^3, the graph Laplacian over occupied sites should give
      K(s) = Tr e^{-s Delta}  ->  N / (4 pi D s)^{3/2}
for large s, with D an effective diffusion constant (D = 1 undiluted).  A good
fit means the arena still has a continuum limit; a bad one means dilution
destroys it.
"""
import numpy as np, time

L = 16
def build(p, seed=487):
    rng = np.random.default_rng(seed)
    occ = (rng.random((L,L,L)) < p) if p < 1.0 else np.ones((L,L,L), bool)
    idx = -np.ones((L,L,L), int)
    sites = np.argwhere(occ); idx[occ] = np.arange(len(sites))
    N = len(sites)
    A = np.zeros((N,N))
    for a,(i,j,k) in enumerate(sites):
        for ax,(di,dj,dk) in enumerate(((1,0,0),(0,1,0),(0,0,1))):
            q = ((i+di)%L,(j+dj)%L,(k+dk)%L)
            if occ[q]:
                b = idx[q]; A[a,b] -= 1; A[b,a] -= 1; A[a,a] += 1; A[b,b] += 1
    return A, N, occ

# CORRECTION: the first version fitted K(s) over s in [4,40].  On a periodic
# L=16 box the free-diffusion form only holds for 1 << s << L^2/(4 pi D) ~ 20;
# beyond that K saturates at the component count.  The p=1.00 CONTROL failed
# (fit error 0.62 where D=1 is known), which is how the bad window was caught.
# Measure D directly from the spectrum instead -- no window, no fit form:
#     the smallest non-zero eigenvalue of a diffusive Laplacian on a periodic
#     box is lambda_1 = D * khat^2 with khat^2 = 4 sin^2(pi/L).
print(f"L={L}, Z^3.  D_eff from the spectrum: lambda_1 = D * khat^2")
print("khat^2 = 4 sin^2(pi/L); D = 1 undiluted.  No fitting window involved.\n")
print(f"{'p':>5s} {'sites':>6s} {'components':>11s} {'lambda_1':>10s} {'D_eff':>8s}"
      f" {'lam2/lam1':>10s}")
kh2 = 4*np.sin(np.pi/L)**2
for p in (0.25, 0.35, 0.50, 0.70, 1.00):
    A, N, occ = build(p)
    ev = np.sort(np.maximum(np.linalg.eigvalsh(A), 0))
    ncomp = int(np.sum(ev < 1e-9))
    nz = ev[ev >= 1e-9]
    l1 = nz[0]; l2 = nz[1] if len(nz) > 1 else np.nan
    print(f"{p:5.2f} {N:6d} {ncomp:11d} {l1:10.5f} {l1/kh2:8.4f} {l2/l1:10.4f}")
print("""
   components > 1 means the recorded set has FRAGMENTED: each piece carries its
   own zero mode, there is no single connected arena, and no continuum limit on
   the whole.""")
