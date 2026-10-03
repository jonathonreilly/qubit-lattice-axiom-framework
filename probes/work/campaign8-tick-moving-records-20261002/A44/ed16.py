"""A44 ed16: exact cross-check on 16-site periodic clusters (supplied toys).
argv[1] = 'fcc16' (Z^3 mod <(2,2,0),(2,0,2),(0,2,2)>, full cubic symmetry, no doubled bonds)
        | '224'   (2x2x4 periodic; x,y bonds doubled, Moriya cancels on them).
Parts: (a) sparse H_J, H_K, H_D; (b) projected parton states by full enumeration for
(t, lam) = (cos th, sin th), th = k pi/12, plus the KS pi-flux scalar ansatz; Klein-frame check;
(c) named product states; (d) Lanczos ground states on a (J,K,D) grid (D >= 0; D -> -D is the
inversion image) with overlaps."""
import sys, time, signal, numpy as np, scipy.sparse.linalg as sla
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a44lib import *
t0 = time.time()
which = sys.argv[1]
T = {'fcc16': [[2, 2, 0], [2, 0, 2], [0, 2, 2]], '224': np.diag([2, 2, 4])}[which]
cl = Cluster(T); N = cl.N; nb = len(cl.bonds)
bits = bits_table(N)
mats = sparse_terms(cl)
print(f"[a] {which}: N={N}, oriented bonds {nb}; nnz J/K/D = {mats['J'].nnz}/{mats['K'].nnz}/{mats['D'].nnz}; "
      f"hermitian defect D {abs(mats['D'] - mats['D'].conj().T).max():.1e}; t={time.time()-t0:.1f}s", flush=True)

def ev3(psi):
    psi = psi / np.linalg.norm(psi)
    return np.array([np.vdot(psi, mats[k] @ psi).real for k in "JKD"]) / nb, psi

# ---- (b) partons
ths = [k * np.pi / 12 for k in range(12)]
part = {}
for th in ths:
    Phi, gap, lev = mf_orbitals(cl, np.cos(th), np.sin(th))
    if gap < 1e-8:
        print(f"[b] th={th/np.pi:.3f}pi: open shell (gap {gap:.1e}) -> skipped"); continue
    psi = projected_vector(Phi, bits)
    nrm = np.linalg.norm(psi)
    v, psi = ev3(psi)
    part[th] = (v, psi)
    print(f"[b] th={th/np.pi:.3f}pi (t={np.cos(th):+.3f}, lam={np.sin(th):+.3f}): MF gap {gap:.3f}, |P psi| {nrm:.2e}; "
          f"e_J={v[0]:+.5f} e_K={v[1]:+.5f} e_D={v[2]:+.5f}", flush=True)
for tw, lab in (((np.pi,) * 3, 'APBC'), ((0., 0., 0.), 'PBC')):
    Phi, gap, lev = mf_orbitals(cl, 1.0, 0.0, twist=tw, kind="pi")
    if gap < 1e-8:
        print(f"[b] KS pi-flux scalar ansatz {lab}: open shell"); continue
    v, psi_pi = ev3(projected_vector(Phi, bits))
    print(f"[b] KS pi-flux scalar ansatz {lab}: MF gap {gap:.3f}; e_J={v[0]:+.5f} e_K={v[1]:+.5f} e_D={v[2]:+.5f}")
    part['pi_' + lab] = (v, psi_pi)

# total spin^2 of a vector
b = np.arange(2 ** N, dtype=np.int64)
def S2(psi):
    out = 0.
    zsum = sum((1 - 2 * ((b >> i) & 1)) for i in range(N))
    out += np.linalg.norm(zsum * psi) ** 2
    out += np.linalg.norm(sum(psi[b ^ (1 << i)] for i in range(N))) ** 2
    out += np.linalg.norm(sum(-1j * (1 - 2 * ((b >> i) & 1)) * psi[b ^ (1 << i)] for i in range(N))) ** 2
    return out / 4
def apply_sites(psi, Ws):
    v = psi.reshape((2,) * N)
    for i, W in enumerate(Ws):
        ax = N - 1 - i
        v = np.moveaxis(np.tensordot(W, v, axes=([1], [ax])), 0, ax)
    return v.reshape(-1)
A = [1j * s for s in SIG]
def Vx(x):
    return np.linalg.matrix_power(A[0], int(x[0]) % 4) @ np.linalg.matrix_power(A[1], int(x[1]) % 4) @ np.linalg.matrix_power(A[2], int(x[2]) % 4)
sold = part[np.pi / 2][1]
dual = apply_sites(sold, [Vx(x).conj().T for x in cl.sites])
print(f"[b] Klein frame: S^2 of soldered state = {S2(sold):.4f}; S^2 of V^dag-rotated soldered state = {S2(dual):.2e} (0 = singlet)")
for k in part:
    if isinstance(k, str):
        print(f"[b]   |<V^dag soldered | {k}>| = {abs(np.vdot(dual, part[k][1])):.6f}")
t_only = part[0.0][1]
print(f"[b] S^2 of t-only state = {S2(t_only):.2e}; t={time.time()-t0:.1f}s", flush=True)

# ---- (c) named product states
X = cl.X.astype(float)
named = {}
named['aligned z'] = np.tile([0, 0, 1.], (N, 1))
named['aligned 111'] = np.tile(np.ones(3) / np.sqrt(3), (N, 1))
named['Neel z'] = ((-1.) ** X.sum(1))[:, None] * np.array([0, 0, 1.])
named['compass stag'] = ((-1.) ** X) / np.sqrt(3)
w = -np.ones(3) / np.sqrt(3); u = np.array([1, -1, 0]) / np.sqrt(2); vv = np.cross(w, u)
ph = (np.pi / 2) * X.sum(1)
named['Moriya spiral'] = np.cos(ph)[:, None] * u + np.sin(ph)[:, None] * vv
nvec = {}
for k, ms in named.items():
    cv = classical_vector(cl, ms); pv = product_vector(ms, bits)
    qv, _ = ev3(pv)
    nvec[k] = (cv, pv / np.linalg.norm(pv))
    print(f"[c] {k:14s}: classical (e_J,e_K,e_D) = {np.round(cv, 5)}  (quantum check {np.abs(qv - cv).max():.1e})")

# ---- (d) directions
dirs = [(0., ph) for ph in np.arange(0, 360, 15)] + [(be, ph) for be in (30., 60.) for ph in np.arange(0, 360, 30)] + [(90., 0.)]
rng = np.random.default_rng(44)
print("[d] columns: beta,phi (deg) | J K D | E0/bond deg gap | E_cl(greedy) E_named_best | "
      "parton: E_sold ov_sold | best th E ov | t-only E ov | pi-flux E ov | named-product best ov")
rows = []
for be, phd in dirs:
    bR, pR = np.radians(be), np.radians(phd)
    Jv = np.array([np.cos(bR) * np.cos(pR), np.cos(bR) * np.sin(pR), np.sin(bR)])
    H = Jv[0] * mats['J'] + Jv[1] * mats['K'] + (Jv[2] * mats['D'] if abs(Jv[2]) > 1e-12 else 0)
    vals, vecs = sla.eigsh(H, k=4, which='SA', tol=1e-10, maxiter=5000)
    o = np.argsort(vals); vals, vecs = vals[o], vecs[:, o]
    deg = int(np.sum(vals - vals[0] < 1e-7)); gs = vecs[:, :deg]
    ovl = lambda psi: float(np.sum(np.abs(gs.conj().T @ psi) ** 2))
    E0 = vals[0] / nb; gap = (vals[deg] - vals[0]) / nb if deg < 4 else np.nan
    Ecl, mcl = greedy_classical(cl, Jv, rng, starts=8, iters=200, seeds=list(named.values()))
    En = min(c[0] @ Jv for c in nvec.values())
    pe = {th: (part[th][0] @ Jv, ovl(part[th][1])) for th in part if not isinstance(th, str)}
    thb = min(pe, key=lambda th: pe[th][0])
    pik = [k for k in part if isinstance(k, str)]
    pi_e, pi_o = (part[pik[0]][0] @ Jv, ovl(part[pik[0]][1])) if pik else (np.nan, np.nan)
    pov = max(ovl(c[1]) for c in nvec.values())
    pcl = product_vector(mcl, bits); pov = max(pov, ovl(pcl / np.linalg.norm(pcl)))
    rows.append((be, phd, *Jv, E0, deg, gap, Ecl, En, *pe[np.pi / 2], thb, *pe[thb], *pe[0.0], pi_e, pi_o, pov))
    print(f"{be:4.0f} {phd:5.0f} | {Jv[0]:+.3f} {Jv[1]:+.3f} {Jv[2]:+.3f} | {E0:+.5f} {deg}{'+' if deg == 4 else ' '} {gap:.4f} | "
          f"{Ecl:+.5f} {En:+.5f} | {pe[np.pi/2][0]:+.5f} {pe[np.pi/2][1]:.4f} | {thb/np.pi:.3f}pi {pe[thb][0]:+.5f} {pe[thb][1]:.4f} | "
          f"{pe[0.0][0]:+.5f} {pe[0.0][1]:.4f} | {pi_e:+.5f} {pi_o:.4f} | {pov:.4f}", flush=True)
np.save(f"ed16_{which}.npy", np.array(rows, float))
print(f"[d] done; total {time.time()-t0:.1f}s")
