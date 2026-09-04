"""T116 - WHERE DOES THE DIFFEOMORPHISM FAILURE LIVE IN THE SPECTRUM?

R65 killed the Sakharov induced-gravity route: displacing VERTICES of a flat
complex and recomputing edge lengths gives an identical geometry (still flat,
every deficit 0, volume fixed) -- a pure re-triangulation of flat space -- yet
the matter effective action W = (1/2) log det(Delta + m^2) MOVED, by more than
the physical conformal mode did.  Any diffeomorphism-invariant functional must
be blind to a re-triangulation of flat space.  W is not.

But R23-R26 established the OPPOSITE for the same construction: the LOW spectrum
of the cell-complex operator IS chopping-independent, converging at O(h^2).

Both cannot be wrong.  The reconciliation must be that the failure lives in the
UV: the low eigenvalues track the continuum (geometry), the high ones are mesh
artifacts, and W sums ALL of them with equal weight -- so W is UV-dominated and
therefore mesh-dominated.

That is a sharp, falsifiable statement, and it is measurable directly:
   perturb the mesh by a pure diffeomorphism, and plot the eigenvalue shift
   against the eigenvalue index.
If the hypothesis is right the shift is tiny at the bottom and O(1) at the top.
If it is flat across the spectrum, the hypothesis is dead and the regulator
route with it.

Operator: the intrinsic simplicial (cotangent) Laplacian in general d.  For a
d-simplex with edge lengths ell_ij, the Gram matrix about vertex 0 is
   G_ab = (1/2)(ell^2_{0a} + ell^2_{0b} - ell^2_{ab}),
the barycentric gradients satisfy grad(phi_a).(p_b - p_0) = delta_ab, so
   grad(phi_a) . grad(phi_b) = (G^{-1})_ab,       V = sqrt(det G)/d!
giving K_ab = V (G^{-1})_ab, and grad(phi_0) = -sum_a grad(phi_a).
Mass lumped to vertices (V/(d+1) each) -- the framework's own "cells weigh
corners" weighting, i.e. R1.  Everything is a function of edge lengths alone,
so the same code handles a moved mesh and a curved metric."""
import numpy as np, itertools, sys

d = 4

def kuhn(L):
    """Kuhn/Freudenthal triangulation of the L^4 torus. Returns vertex list,
    the simplices as vertex-id 5-tuples, and the integer lattice offsets of each
    simplex's corners so positions can be recomputed under any displacement."""
    verts = list(itertools.product(range(L), repeat=d))
    vid = {v: i for i, v in enumerate(verts)}
    simp = []
    for base in verts:
        for perm in itertools.permutations(range(d)):
            ids = [vid[base]]
            offs = [np.zeros(d, dtype=np.int64)]
            cur = list(base); off = np.zeros(d, dtype=np.int64)
            for a in perm:
                cur[a] = (cur[a] + 1) % L
                off = off.copy(); off[a] += 1
                ids.append(vid[tuple(cur)]); offs.append(off)
            simp.append((np.array(ids), np.array(base), np.array(offs)))
    return verts, vid, simp

def positions(simp_entry, disp, L):
    """Embedded positions of a simplex's 5 corners, in the flat torus of side 1,
    under a vertex displacement field disp(x) (x = base+offset, in units of h)."""
    base, offs = simp_entry[1], simp_entry[2]
    h = 1.0 / L
    X = (base[None, :] + offs) * h          # unwrapped: no periodic seam inside a simplex
    return X + disp(X)

def lengths_from_positions(X):
    l2 = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        v = X[i] - X[j]; l2[i, j] = l2[j, i] = float(v @ v)
    return l2

def lengths_from_metric(simp_entry, L, gfun):
    """Edge lengths of the same combinatorial simplex in a CURVED metric:
    ell^2 = (dx)^T g(midpoint) (dx).  Genuinely different geometry, not a move."""
    base, offs = simp_entry[1], simp_entry[2]
    h = 1.0 / L
    X = (base[None, :] + offs) * h
    l2 = np.zeros((5, 5))
    for i, j in itertools.combinations(range(5), 2):
        dx = X[i] - X[j]; mid = 0.5 * (X[i] + X[j])
        l2[i, j] = l2[j, i] = float(dx @ gfun(mid) @ dx)
    return l2

def assemble(simp, l2list, N):
    """Stiffness K (sparse-as-dense) and lumped mass Mv from per-simplex l^2."""
    K = np.zeros((N, N)); Mv = np.zeros(N)
    fact = float(np.math.factorial(d)) if hasattr(np, 'math') else 24.0
    for (ids, _, _), l2 in zip(simp, l2list):
        G = np.empty((d, d))
        for a in range(d):
            for b in range(d):
                G[a, b] = 0.5 * (l2[0, a + 1] + l2[0, b + 1] - l2[a + 1, b + 1])
        dg = np.linalg.det(G)
        if dg <= 0: return None, None
        V = np.sqrt(dg) / 24.0
        Gi = np.linalg.inv(G)
        loc = np.zeros((5, 5))
        loc[1:, 1:] = V * Gi
        loc[0, 1:] = -loc[1:, 1:].sum(axis=0)
        loc[1:, 0] = loc[0, 1:]
        loc[0, 0] = V * Gi.sum()
        K[np.ix_(ids, ids)] += loc
        Mv[ids] += V / 5.0
    return K, Mv

def spectrum(simp, l2list, N):
    K, Mv = assemble(simp, l2list, N)
    if K is None: return None
    s = 1.0 / np.sqrt(Mv)
    A = (K * s[None, :]) * s[:, None]
    A = 0.5 * (A + A.T)
    return np.linalg.eigvalsh(A)

# ---------------------------------------------------------------- run
L = int(sys.argv[1]) if len(sys.argv) > 1 else 6
AMP = float(sys.argv[2]) if len(sys.argv) > 2 else 0.15   # displacement, in units of h
verts, vid, simp = kuhn(L)
N = len(verts)
print(f"T116  L={L}: {N} vertices, {len(simp)} simplices, displacement amplitude {AMP} h")

# reference: the flat, undisplaced mesh
l2_0 = [lengths_from_positions(positions(s, lambda X: 0.0 * X, L)) for s in simp]
lam0 = spectrum(simp, l2_0, N)
print(f"      flat mesh: lambda_1 = {lam0[1]:.4f}  (continuum 4 pi^2 = {4*np.pi**2:.4f}),"
      f"  lambda_max = {lam0[-1]:.1f}")

# (A) PURE DIFFEOMORPHISM: move the vertices, same flat space, same geometry.
kvec = 2 * np.pi * np.array([1.0, 0.0, 0.0, 0.0])
def gauge(X, amp=AMP / L):
    out = np.zeros_like(X)
    out[:, 1] = amp * np.sin(X @ kvec)          # displace along x2, wave along x1
    out[:, 2] = amp * np.sin(X @ (2 * kvec))
    return out
l2_g = [lengths_from_positions(positions(s, gauge, L)) for s in simp]
lam_g = spectrum(simp, l2_g, N)

# (B) GENUINE GEOMETRY CHANGE: a curved metric of comparable size.
CURV = AMP / L
def gmet(x):
    g = np.eye(d)
    f = CURV * np.sin(float(x @ kvec))
    g[1, 1] += f; g[2, 2] -= f                  # traceless, so volume is 2nd order
    return g
l2_c = [lengths_from_metric(s, L, gmet) for s in simp]
lam_c = spectrum(simp, l2_c, N)

# sanity: the moved mesh really is the same geometry (total volume unchanged)
def totvol(l2list):
    t = 0.0
    for l2 in l2list:
        G = np.empty((d, d))
        for a in range(d):
            for b in range(d):
                G[a, b] = 0.5 * (l2[0, a+1] + l2[0, b+1] - l2[a+1][b+1])
        t += np.sqrt(max(np.linalg.det(G), 0.0)) / 24.0
    return t
V0, Vg, Vc = totvol(l2_0), totvol(l2_g), totvol(l2_c)
print(f"      total volume: flat {V0:.10f}  moved {Vg:.10f}  (rel diff {abs(Vg-V0)/V0:.2e})"
      f"   curved {Vc:.10f}")
print()
print("   eigenvalue shift by spectral position -- |dlambda|/lambda, averaged in bins")
print(f"   {'band':>16} {'lambda range':>22} {'GAUGE (a move)':>18} {'CURVATURE (real)':>18} {'ratio':>9}")
nz = np.arange(1, N)
nb = 8
edges = np.linspace(1, N, nb + 1).astype(int)
for b in range(nb):
    i0, i1 = edges[b], edges[b + 1]
    if i1 <= i0: continue
    sl = slice(i0, i1)
    rg = float(np.mean(np.abs(lam_g[sl] - lam0[sl]) / lam0[sl]))
    rc = float(np.mean(np.abs(lam_c[sl] - lam0[sl]) / lam0[sl]))
    print(f"   {f'{i0}-{i1-1}':>16} {f'{lam0[i0]:.1f} - {lam0[i1-1]:.1f}':>22}"
          f" {rg:18.3e} {rc:18.3e} {rg/rc if rc>0 else float('nan'):9.3f}")
print()
print("   VERDICT SHAPE: if the gauge column climbs steeply from bottom to top of")
print("   the spectrum while the curvature column stays flat, the diffeomorphism")
print("   failure is a UV effect and a cutoff regulator can remove it.")
np.save(f"/tmp/t116_lam_{L}.npy", np.vstack([lam0, lam_g, lam_c]))
