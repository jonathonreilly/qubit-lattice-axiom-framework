"""
Check B (route 1): liquid vs glass vs crystal vacuum, static TT modulus, d = 2 and 3.

Object: free scalar on a periodic Delaunay complex, P1 (Whitney 0-form) stiffness K_T,
unit mass per site (triangulation-independent), vacuum energy E = 1/2 sum sqrt(lambda(K)).
Uniform volume-preserving metric strain g = M^T M, applied covariantly
(E computed from (X, g) == E computed from (M X, delta)).

  liquid  : Poisson points, adjacency = Delaunay in the CURRENT metric (re-triangulate)
  glass   : Poisson points, adjacency frozen at the eps = 0 Delaunay complex
  crystal : jittered square/cubic grid (jitter 1e-3), adjacency re-triangulated
            (= metric-following diagonals on a fixed label crystal)

Lemma (exact, symmetry): for SL(d) M the Poisson process is invariant in law and
Del_g(X) = Del(MX), so <E_liquid>(M) = <E_liquid>(1) up to torus-shape (Casimir) terms.

PRE-STATED READING (written before running)
  L  (lemma)   PASS iff |<G_liq>| <= 3 SE  and  |<G_liq>| <= 0.1 |<G_glass>|.
  H1 (glass)   PASS ("a glass is a solid") iff |<G_glass>| > 5 SE.  2D predicts sign > 0
               (Rippa + operator monotonicity of sqrt); 3D sign not predicted.
  C  (crystal) PASS ("re-triangulating a crystal is not enough") iff |G_crys| > 5 SE.
  R  (Rippa)   2D: lambda_min(K_glass - K_liq) >= -1e-9 always.  3D: reported, not predicted.
"""
import numpy as np, sys
from scipy.spatial import Delaunay
from itertools import product

rng = np.random.default_rng(20261009)

def expm_sym(S, e):
    w, V = np.linalg.eigh(S); return V @ np.diag(np.exp(e * w)) @ V.T

def periodic_delaunay(Y, A):
    """Y: N x d points in the cell spanned by rows of A (periods). Returns list of
    simplices as (vertex index mod N, integer image offsets)."""
    N, d = Y.shape
    shifts = np.array(list(product((-1, 0, 1), repeat=d)))
    P = np.concatenate([Y + s @ A for s in shifts])
    idx = np.tile(np.arange(N), len(shifts))
    off = np.repeat(shifts, N, axis=0)
    tri = Delaunay(P, qhull_options="Qbb Qc Qz Q12" if d == 3 else "Qbb Qc Qz").simplices
    cen = P[tri].mean(axis=1)
    frac = cen @ np.linalg.inv(A)
    keep = np.all((frac >= 0) & (frac < 1), axis=1)
    tri = tri[keep]
    return idx[tri], off[tri]

def stiffness(Y, A, vid, voff):
    N, d = Y.shape
    pos = Y[vid] + np.einsum("tvk,kl->tvl", voff, A)       # T x (d+1) x d
    D = pos[:, 1:, :] - pos[:, :1, :]                         # T x d x d
    vol = np.abs(np.linalg.det(D)) / (1 if d == 1 else (2 if d == 2 else 6))
    Dinv = np.linalg.inv(D)                                   # grads of bary coords 1..d
    G = np.concatenate([-Dinv.sum(axis=2, keepdims=True), Dinv], axis=2)  # T x d x (d+1)
    Kloc = vol[:, None, None] * np.einsum("tka,tkb->tab", G, G)
    K = np.zeros((N, N))
    for a in range(d + 1):
        for b in range(d + 1):
            np.add.at(K, (vid[:, a], vid[:, b]), Kloc[:, a, b])
    return K

def E_vac(K):
    lam = np.linalg.eigvalsh(K)
    return 0.5 * np.sqrt(np.clip(lam, 0, None)).sum(), lam

def run(d, N, R, epss, chans, kind):
    L = N ** (1 / d)
    A0 = L * np.eye(d)
    out = {c: [] for c in chans}
    rip = []
    for r in range(R):
        if kind == "crystal":
            m = int(round(L)); g1 = np.arange(m) + 0.5
            X = np.array(list(product(g1, repeat=d)), float) + 1e-3 * rng.standard_normal((m ** d, d))
            Lc = m; A0c = Lc * np.eye(d)
        else:
            X = rng.uniform(0, L, size=(N, d)); A0c = A0
        vid0, voff0 = periodic_delaunay(X, A0c)
        for cname, S in chans.items():
            Eg, El = [], []
            for e in epss:
                M = expm_sym(S, e)
                Y, A = X @ M.T, A0c @ M.T
                Kg = stiffness(Y, A, vid0, voff0)
                vid, voff = periodic_delaunay(Y, A)
                Kl = stiffness(Y, A, vid, voff)
                eg, _ = E_vac(Kg); el, _ = E_vac(Kl)
                Eg.append(eg / len(X)); El.append(el / len(X))
                if kind != "crystal" and e != 0:
                    rip.append(np.linalg.eigvalsh(Kg - Kl)[0])
            Gg = 2 * np.polyfit(epss, Eg, 4)[-3]; Gl = 2 * np.polyfit(epss, El, 4)[-3]
            out[cname].append((Gg, Gl, El[len(epss) // 2]))
    return out, rip

def report(tag, out, rip):
    for c, rows in out.items():
        a = np.array(rows); n = len(a)
        mg, sg = a[:, 0].mean(), a[:, 0].std(ddof=1) / np.sqrt(n)
        ml, sl = a[:, 1].mean(), a[:, 1].std(ddof=1) / np.sqrt(n)
        e0 = a[:, 2].mean()
        print(f"{tag:10s} {c:4s}  e0/site={e0:.4f}  G_frozen={mg:+.5f}+-{sg:.5f}  G_retri={ml:+.5f}+-{sl:.5f}"
              f"  (G/e0: {mg/e0:+.4f}, {ml/e0:+.4f})")
    if rip:
        print(f"{tag:10s} min eig(K_frozen-K_retri) over all strains/realizations = {min(rip):+.3e}")

epss = np.array([-0.06, -0.04, -0.02, 0.0, 0.02, 0.04, 0.06])
ch2 = {"Eg": np.diag([1.0, -1.0]), "T2g": np.array([[0, 1.0], [1.0, 0]])}
S3 = np.zeros((3, 3)); S3[0, 1] = S3[1, 0] = 1.0
ch3 = {"Eg": np.diag([1.0, -1.0, 0.0]), "T2g": S3}

which = sys.argv[1] if len(sys.argv) > 1 else "2d"
if which == "2d":
    out, rip = run(2, 2500, 12, epss, ch2, "poisson"); report("2D poisson", out, rip)
    out, rip = run(2, 2500, 4, epss, ch2, "crystal"); report("2D crystal", out, rip)
else:
    out, rip = run(3, 1000, 12, epss, ch3, "poisson"); report("3D poisson", out, rip)
    out, rip = run(3, 1000, 4, epss, ch3, "crystal"); report("3D crystal", out, rip)
