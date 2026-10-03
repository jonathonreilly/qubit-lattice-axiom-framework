"""Lane G check 2: sparse box solves on a 31^3 grid (sites 0..30).

Geometry (shared with the Monte Carlo check 3):
  reservoir layer R = sites with a coordinate equal to 0 or 30 (carrier density held at u_inf);
  lump B = 3^3 cube 14..16 (centre 15,15,15); contact shell S = sites face-adjacent to B, not in B.
  Perfect capture on S  => u = 0 on S.
  h = harmonic in the interior, h = 1 on S (and B), h = 0 on R.  Prediction: u/u_inf = 1 - h = 1 + Phi.

C1  h_box vs the exact infinite-lattice h_inf (Dyson with the Z^3 Green function), and the 1/r tail.
C2  capture flux: Cap_box(S) = sum_{x in S} (-Delta h)(x)  (Gauss: monopole = net capture current).
C3  background absorption qbar on every interior site (screening): lump field ratio vs r.
C4  autocatalytic background (negative mass^2, chi = 0.1): indefinite operator, MINRES; sign changes.
"""
import os
for k in ["OMP_NUM_THREADS", "OPENBLAS_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "MKL_NUM_THREADS"]:
    os.environ[k] = "1"
import time
import numpy as np
import scipy.sparse as sp
from scipy.sparse.linalg import cg, minres
from scipy.special import ive
from scipy.integrate import quad

t0 = time.time()
HERE = os.path.dirname(os.path.abspath(__file__))
L = 31
C = 15
idx = np.arange(L ** 3).reshape(L, L, L)
I, J, K = np.meshgrid(np.arange(L), np.arange(L), np.arange(L), indexing="ij")
res_mask = (I == 0) | (I == L - 1) | (J == 0) | (J == L - 1) | (K == 0) | (K == L - 1)
lump = (abs(I - C) <= 1) & (abs(J - C) <= 1) & (abs(K - C) <= 1)
dil = np.zeros_like(lump)
for d in range(3):
    for s in (1, -1):
        dil |= np.roll(lump, s, axis=d)
shell = dil & ~lump
print(f"|B| = {lump.sum()}, |S| = {shell.sum()}, reservoir sites = {res_mask.sum()}")

# neighbour pairs (no wrap): build Laplacian on full grid
rows, cols = [], []
for d in range(3):
    a = [slice(None)] * 3; b = [slice(None)] * 3
    a[d] = slice(0, L - 1); b[d] = slice(1, L)
    p = idx[tuple(a)].ravel(); q = idx[tuple(b)].ravel()
    rows += [p, q]; cols += [q, p]
rows = np.concatenate(rows); cols = np.concatenate(cols)
A_adj = sp.csr_matrix((np.ones(len(rows)), (rows, cols)), shape=(L ** 3, L ** 3))


def dirichlet_solve(fixed_mask, fixed_vals, extra_diag=None, rhs_extra=None, tol=1e-11, solver="cg"):
    """Solve (6 - Adj + extra_diag) u = rhs on free sites; u fixed on fixed_mask.
    Sites outside the grid count as fixed zero (never used here: reservoir layer covers the border)."""
    free = ~fixed_mask.ravel()
    fidx = np.flatnonzero(free)
    ufix = np.zeros(L ** 3); ufix[fixed_mask.ravel()] = np.asarray(fixed_vals).ravel()[fixed_mask.ravel()]
    Aff = A_adj[fidx][:, fidx]
    diag = 6.0 * np.ones(len(fidx))
    if extra_diag is not None:
        diag = diag + extra_diag.ravel()[fidx]
    M = sp.diags(diag) - Aff
    b = (A_adj[fidx] @ ufix)
    if rhs_extra is not None:
        b = b + rhs_extra.ravel()[fidx]
    if solver == "cg":
        x, info = cg(M, b, rtol=tol, maxiter=20000)
    else:
        x, info = minres(M, b, rtol=tol, maxiter=20000)
    u = ufix.copy(); u[fidx] = x
    resid = np.linalg.norm(M @ x - b) / np.linalg.norm(b)
    return u.reshape(L, L, L), info, resid


# ---------- C1/C2: hitting probability of the shell ----------
fixed = res_mask | dil
vals = np.where(dil, 1.0, 0.0)
h, info, resid = dirichlet_solve(fixed, vals)
print(f"C1 solve: info={info}, rel residual={resid:.1e}")
np.save(os.path.join(HERE, "h_box.npy"), h)
lap = -6 * h
for d in range(3):
    lap += np.roll(h, 1, axis=d) + np.roll(h, -1, axis=d)  # roll wraps only at border where h=0 anyway
capbox = float((-lap)[shell].sum())
print(f"C2 Cap_box(S) = sum_S (-Delta h) = {capbox:.4f}   (infinite-lattice Cap(B+S) = 29.4124 from check 1)")

# infinite-lattice h via Dyson with exact Z^3 Green function
PREF = (4 * np.pi) ** -1.5
_c = {}
def G(x):
    a, b, c = sorted(abs(int(v)) for v in x)
    key = (a, b, c)
    if key in _c:
        return _c[key]
    T = max(4000.0, 60.0 * (a * a + b * b + c * c))
    f = lambda t: ive(a, 2 * t) * ive(b, 2 * t) * ive(c, 2 * t)
    e = [0.0] + list(np.geomspace(0.25, T, 24))
    v = sum(quad(f, lo, hi, limit=200, epsabs=1e-15, epsrel=1e-12)[0] for lo, hi in zip(e[:-1], e[1:]))
    s = (4 * a * a - 1) + (4 * b * b - 1) + (4 * c * c - 1)
    _c[key] = v + PREF * (2 * T ** -0.5 - (s / 16.0) * (2.0 / 3.0) * T ** -1.5)
    return _c[key]

D = np.argwhere(dil) - C
GD = np.array([[G(D[i] - D[j]) for j in range(len(D))] for i in range(len(D))])
eD = np.linalg.solve(GD, np.ones(len(D)))
capD = eD.sum()
print(f"    infinite-lattice Cap(B+S) recomputed = {capD:.4f}")

def h_inf(x):
    return sum(G(np.array(x) - D[j]) * eD[j] for j in range(len(D)))

print("\n r  | axis: h_box    h_inf    4pi r h_inf/Cap | body diag: h_box   h_inf   4pi r h_inf/Cap")
for r in [3, 4, 5, 6, 8, 10, 12, 14]:
    hb = h[C + r, C, C]; hi = h_inf((r, 0, 0))
    out = f"{r:2d}  |      {hb:.4f}   {hi:.4f}   {4*np.pi*r*hi/capD:.4f}         |"
    m = int(round(r / np.sqrt(3)))
    if 2 <= m <= 8:
        rr = m * np.sqrt(3)
        hb2 = h[C + m, C + m, C + m]; hi2 = h_inf((m, m, m))
        out += f" (m={m}) {hb2:.4f}  {hi2:.4f}  {4*np.pi*rr*hi2/capD:.4f}"
    print(out)
for r in [20, 30, 40]:
    hi = h_inf((r, 0, 0))
    print(f"{r:2d}  |   (no box)        {hi:.5f}  {4*np.pi*r*hi/capD:.5f}")

# ---------- C3: screening by background absorption ----------
print("\nC3 screening: carrier density with uniform background absorption qbar (u=1 on reservoir).")
print("    lump field ratio Phi_L(r) = u_with_lump/u_without - 1 on the axis, times r")
interior_free = ~(res_mask)
for qbar in [0.0, 0.01, 0.05]:
    ed = np.where(interior_free, qbar, 0.0)
    u0, i0, r0 = dirichlet_solve(res_mask, np.where(res_mask, 1.0, 0.0), extra_diag=ed)
    fixed1 = res_mask | dil
    vals1 = np.where(res_mask, 1.0, 0.0)
    u1, i1, r1 = dirichlet_solve(fixed1, vals1, extra_diag=ed)
    prof = [(u1[C + r, C, C] / u0[C + r, C, C] - 1.0) * r for r in [3, 5, 7, 9, 11, 13]]
    print(f"  qbar={qbar:5}: u0(centre)={u0[C,C,C]:.4f}  r*Phi_L at r=3,5,7,9,11,13: " + " ".join(f"{v:+.4f}" for v in prof))

# ---------- C4: anti-screening (negative mass^2) ----------
print("\nC4 anti-screening: (-Delta - chi) Phi = -q delta_centre, Phi=0 on reservoir layer, chi=0.1, q=1 (MINRES)")
chi = 0.1
ed = np.where(res_mask, 0.0, -chi)
src = np.zeros((L, L, L)); src[C, C, C] = -1.0
phi, i4, r4 = dirichlet_solve(res_mask, np.zeros((L, L, L)), extra_diag=ed, rhs_extra=src, solver="minres", tol=1e-10)
print(f"  MINRES info={i4}, rel residual={r4:.1e}")
print("  Phi on axis r=0..14: " + " ".join(f"{phi[C+r,C,C]:+.3f}" for r in range(0, 15)))
phi0, _, _ = dirichlet_solve(res_mask, np.zeros((L, L, L)), extra_diag=None, rhs_extra=src)
print("  (chi=0 control)    : " + " ".join(f"{phi0[C+r,C,C]:+.3f}" for r in range(0, 15)))
print(f"\nelapsed {time.time()-t0:.1f} s")
