"""A46 ed16_ring: exact 16-site (cubic-symmetric cluster) check in the dual frame with ring exchange.
H' = J' sum s.s + K' sum s^a s^a + R sum_faces (P + P^-1); per-bond normalisation (3N bonds, 3N faces).
States by full enumeration: projected pi-flux singlet (Klein image of the soldered state), the AF family
(pi-flux + staggered field m), the 0-flux Fermi sea singlet, Neel product.  Grid J'=1, K' in {-1..1}, R."""
import sys, time, signal, numpy as np, scipy.sparse.linalg as sla
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a46lib import *
from a44lib import mf_orbitals
t0 = time.time()
KPS = [float(v) for v in sys.argv[1].split(",")] if len(sys.argv) > 1 else [0.0, -1.0, -0.5, 0.5]
RS = [float(v) for v in sys.argv[2].split(",")] if len(sys.argv) > 2 else [0.0, 0.2, 0.5, 1.0, -0.2, -0.5]
cl = Cluster([[2, 2, 0], [2, 0, 2], [0, 2, 2]]); N = cl.N; nb = 3 * N
bits = bits_table(N); plaq = plaquettes(cl)
mats = sparse_terms(cl); HJ, HK = mats["J"], mats["K"]; del mats
HR = ring_sparse(cl, plaq)
print(f"[a] {len(plaq)} faces; ring nnz {HR.nnz}; t={time.time()-t0:.0f}s", flush=True)
def vec3(psi):
    psi = psi / np.linalg.norm(psi)
    return np.array([np.vdot(psi, M @ psi).real for M in (HJ, HK, HR)]) / nb, psi
states = {}
for m in (0., 0.1, 0.3, 1.0, 3.0):
    Phi, gap = mf_dual(cl, 0., 1., m=m)
    v, psi = vec3(projected_vector(Phi, bits)); states[f"AF m={m}"] = (v, psi)
    print(f"[b] pi-flux + staggered field m={m}: MF gap {gap:.3f}; (e_J', e_K', ring) = {np.round(v, 5)}", flush=True)
Phi, gap, _ = mf_orbitals(cl, 1.0, 0.0)
v, psi = vec3(projected_vector(Phi, bits)); states["0-flux FS"] = (v, psi)
print(f"[b] 0-flux Fermi sea singlet: (e_J', e_K', ring) = {np.round(v, 5)}")
neel = ((-1.) ** cl.X.sum(1))[:, None] * np.array([0, 0, 1.])
v, psi = vec3(product_vector(neel, bits)); states["Neel product"] = (v, psi)
print(f"[b] Neel product: (e_J', e_K', ring) = {np.round(v, 5)}; t={time.time()-t0:.0f}s", flush=True)
print("[c] J'  K'    R   | E0/bond  gap  | pi-flux E ov | best AF-family E (m) ov | Neel E ov | ring<E0>")
rows = []
for Kp in KPS:
    for R in RS:
        Jv = np.array([1.0, Kp, R])
        H = HJ + Kp * HK + R * HR
        vals, vecs = sla.eigsh(H, k=3, which='SA', tol=1e-8)
        o = np.argsort(vals); vals, vecs = vals[o], vecs[:, o]
        deg = int(np.sum(vals - vals[0] < 1e-7)); gs = vecs[:, :deg]
        ov = lambda p: float(np.sum(np.abs(gs.conj().T @ p) ** 2))
        g0 = gs[:, 0]; rr = np.vdot(g0, HR @ g0).real / nb
        E = {k: (v @ Jv, ov(p)) for k, (v, p) in states.items()}
        afk = min((k for k in E if k.startswith("AF")), key=lambda k: E[k][0])
        rows.append((1.0, Kp, R, vals[0] / nb, E["AF m=0.0"][0], E["AF m=0.0"][1], E[afk][0], float(afk.split("=")[1]), E["Neel product"][0]))
        print(f"  1 {Kp:+.1f} {R:+.2f} | {vals[0]/nb:+.5f} {(vals[deg]-vals[0])/nb if deg < 3 else np.nan:.4f} (deg {deg}) | "
              f"{E['AF m=0.0'][0]:+.5f} {E['AF m=0.0'][1]:.4f} | {E[afk][0]:+.5f} ({afk.split('=')[1]}) {E[afk][1]:.4f} | "
              f"{E['Neel product'][0]:+.5f} {E['Neel product'][1]:.4f} | {rr:+.4f}", flush=True)
np.save(f"ed16_ring_{len(sys.argv)}.npy", np.array(rows))
print(f"done {time.time()-t0:.0f}s")
