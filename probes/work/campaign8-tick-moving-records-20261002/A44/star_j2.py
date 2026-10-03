"""A44 star_j2 (optional Q4): the Klein dual of the face-diagonal Heisenberg term.
Dual frame (SU(2)-invariant): H' = sum_NN s.s + j sum_fd s.s  (fd = face diagonals, 6 bonds/site).
Original frame (soldered-covariant, star-local): H = sum_NN (2 s^a s^a - s.s) + j sum_fd (2 s^c s^c - s.s),
c = normal of the face.  (a) FCC16 exact: ground state vs j, overlap with the projected pi-flux singlet
(= Klein image of the soldered state), product-state energies; (b) LSWT (A43 library + appended second-
neighbour bonds) for Neel and collinear (pi,pi,0) vs j.  Energies per site."""
import sys, time, signal, itertools, numpy as np, scipy.sparse as sp, scipy.sparse.linalg as sla
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a44lib import *
t0 = time.time()
FD = [(1, 1, 0), (1, -1, 0), (1, 0, 1), (1, 0, -1), (0, 1, 1), (0, 1, -1)]
js = [0.0, 0.1, 0.2, 0.25, 0.3, 0.4, 0.5]

# (a) FCC16
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N; bits = bits_table(N)
H1 = sparse_terms(cl)["J"]
b = np.arange(2 ** N, dtype=np.int64)
def heis(pairs):
    diag = np.zeros(2 ** N); rows, cols, vals = [], [], []
    for i, j in pairs:
        zi = 1 - 2 * ((b >> i) & 1); zj = 1 - 2 * ((b >> j) & 1)
        diag += zi * zj
        sel = zi != zj
        rows.append((b ^ ((1 << i) | (1 << j)))[sel]); cols.append(b[sel]); vals.append(np.full(sel.sum(), 2.0))
    M = sp.csr_matrix((np.concatenate(vals), (np.concatenate(rows), np.concatenate(cols))), shape=(2 ** N, 2 ** N))
    return (M + sp.diags(diag)).tocsr()
pairs2 = [(i, cl.idx[tuple(cl.canon(np.array(cl.sites[i]) + np.array(d))[0])]) for i in range(N) for d in FD]
H2 = heis(pairs2)
print(f"[a] FCC16: {len(pairs2)} oriented face-diagonal bonds (each unordered pair twice: x+d = x-d on this cluster); "
      f"check H1 vs heis(NN) {abs(H1 - heis([(i, j) for (i, j, a, n) in cl.bonds])).max():.1e}", flush=True)
Phi, gap, _ = mf_orbitals(cl, 1.0, 0.0, kind="pi"); psi = projected_vector(Phi, bits); psi /= np.linalg.norm(psi)
e1, e2 = np.vdot(psi, H1 @ psi).real / N, np.vdot(psi, H2 @ psi).real / N
X = cl.X
neel = ((-1.) ** X.sum(1))[:, None] * np.array([0, 0, 1.]); col = ((-1.) ** (X[:, 0] + X[:, 1]))[:, None] * np.array([0, 0, 1.])
def cl_e(ms, pairs):
    return sum(ms[i] @ ms[j] for i, j in pairs) / N
nn_pairs = [(i, j) for (i, j, a, n) in cl.bonds]
pv = {k: product_vector(m, bits) for k, m in (("Neel", neel), ("collinear", col))}
pv = {k: v / np.linalg.norm(v) for k, v in pv.items()}
print(f"[a] pi-flux singlet: <H1>/N = {e1:+.5f}, <H2>/N = {e2:+.5f}  (per face-diagonal bond {e2/6:+.5f})")
print("    j   | E0/N exact  gap/N | pi-flux E/N  overlap | Neel cl E/N ov | collinear cl E/N ov")
for j in js:
    H = H1 + j * H2
    vals, vecs = sla.eigsh(H, k=3, which='SA', tol=1e-10)
    o = np.argsort(vals); vals, vecs = vals[o], vecs[:, o]
    deg = int(np.sum(vals - vals[0] < 1e-7)); gs = vecs[:, :deg]
    ov = lambda v: float(np.sum(np.abs(gs.conj().T @ v) ** 2))
    print(f"  {j:4.2f}  | {vals[0]/N:+.5f} (deg {deg}) {(vals[deg]-vals[0])/N if deg < 3 else np.nan:.4f} | {e1 + j*e2:+.5f} {ov(psi):.4f} | "
          f"{cl_e(neel, nn_pairs) + j*cl_e(neel, pairs2):+.4f} {ov(pv['Neel']):.4f} | {cl_e(col, nn_pairs) + j*cl_e(col, pairs2):+.4f} {ov(pv['collinear']):.4f}", flush=True)

# (b) LSWT with face-diagonal bonds (A43 library)
src = open(__file__.rsplit('/', 2)[0] + "/A43/w2_lswt.py").read().split("# 1. Heisenberg ferromagnet")[0]
ns = {}; exec(compile(src, "A43_w2lib", "exec"), ns); Lattice, couplings = ns["Lattice"], ns["couplings"]
cell8 = [list(p) for p in itertools.product([0, 1], repeat=3)]
def make(ms, j):
    lat = Lattice(2 * np.eye(3), cell8, ms, couplings(J=1.))
    for r in range(lat.n):
        for d in FD:
            yv = lat.tau[r] + np.array(d, float)
            for rp in range(lat.n):
                nn = lat.Binv @ (yv - lat.tau[rp])
                if np.allclose(nn, np.round(nn)):
                    lat.bonds.append((r, rp, lat.B @ np.round(nn), 4 * j * np.eye(3))); break
    return lat
def lswt(lat, nk=6):
    g = (np.arange(nk) + 0.5) / nk * 2 * np.pi - np.pi; Rb = 2 * np.pi * np.linalg.inv(lat.B)
    tot = 0.; minM = np.inf
    for f in itertools.product(g, g, g):
        k = (np.array(f) / (2 * np.pi)) @ Rb
        A, Bm = lat.blocks(k); minM = min(minM, np.linalg.eigvalsh(lat.M(k)).min())
        tot += np.sum(lat.omega(k).real) - np.trace(A).real
    return lat.energy() + 0.5 * tot / nk ** 3 / lat.n, minM
neel8 = [((-1) ** sum(p)) * np.array([0, 0, 1.]) for p in cell8]
col8 = [((-1) ** (p[0] + p[1])) * np.array([0, 0, 1.]) for p in cell8]
print("[b] LSWT per site (infinite lattice):  j | Neel: E_cl E_LSWT stable | collinear (pi,pi,0): E_cl E_LSWT stable")
for j in js:
    out = []
    for ms in (neel8, col8):
        lat = make(ms, j); e, mM = lswt(lat)
        out.append(f"{lat.energy():+.4f} {e:+.4f} {'yes' if mM > -1e-7 else 'NO'}")
    print(f"     {j:4.2f} | {out[0]} | {out[1]}", flush=True)
print(f"done {time.time()-t0:.0f}s")
