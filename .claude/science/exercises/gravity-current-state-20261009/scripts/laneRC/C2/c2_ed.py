"""C2 step 2: full ED on periodic clusters. Drude ratio r = sum_{E_n=E_m} p_n |J_nm|^2 / sum_{n,m} p_n |J_nm|^2
(ratio of ensemble sums), J = J_E^x from the exact infinite-lattice density placed by translations.
Lemma (report sec. 2): if a local conserved improvement J' = J + i[H,B] != 0 exists, r(N, beta=0) = ||j'||^2/||j||^2
is N-independent for clusters larger than its support. Decay of r(N) excludes all such J'.
usage: python3 c2_ed.py <model-substring> ...
"""
import sys, time
import numpy as np
from pauli_ti import energy_current, shift
import c2_models as M

def torus_cells(L1, L2):
    Lm = np.array([L1, L2], float).T; inv = np.linalg.inv(Lm)
    def red(x, y):
        f = inv @ np.array([x, y], float)
        m = np.floor(f + 1e-9)
        r = np.array([x, y]) - Lm @ m
        return (int(round(r[0])), int(round(r[1])))
    reps = set()
    R = abs(L1[0]) + abs(L1[1]) + abs(L2[0]) + abs(L2[1]) + 2
    for x in range(-R, R+1):
        for y in range(-R, R+1):
            reps.add(red(x, y))
    reps = sorted(reps)
    return reps, red

def build_ops(H, J, nsub, L1, L2):
    cells, red = torus_cells(L1, L2)
    cidx = {c: i for i, c in enumerate(cells)}
    N = len(cells)*nsub
    dim = 2**N
    states = np.arange(dim, dtype=np.int64)
    bad = [0]
    def place(D):
        Mx = np.zeros((dim, dim), complex)
        for s, c in D.items():
            for cell in cells:
                st = shift(s, cell)
                xm = 0; zm = 0; ny = 0; seen = set()
                for (x, y, k), p in st:
                    q = cidx[red(x, y)]*nsub + k
                    if q in seen: bad[0] += 1
                    seen.add(q)
                    if p in (1, 2): xm ^= (1 << q)
                    if p in (2, 3): zm ^= (1 << q)
                    if p == 2: ny += 1
                par = (np.bitwise_count(states & zm) % 2).astype(np.int64)
                vals = c*(1j**ny)*(1 - 2*par)
                Mx[states ^ xm, states] += vals
        return Mx
    Hm = place(H); Jm = place(J)
    return Hm, Jm, N, bad[0]

def drude(Hm, Jm, betas, tol=1e-8):
    if np.abs(Hm.imag).max() < 1e-12 and np.abs(Jm.real).max() < 1e-12:
        E, V = np.linalg.eigh(Hm.real)
        K = V.T @ Jm.imag @ V
    else:
        E, V = np.linalg.eigh(Hm)
        K = V.conj().T @ Jm @ V
    K2 = np.abs(K)**2
    same = np.abs(E[:, None] - E[None, :]) < tol*max(1, np.abs(E).max())
    out = []
    for b in betas:
        p = np.exp(-b*(E - E.min())); p /= p.sum()
        W = p[:, None]*K2
        out.append(W[same].sum()/W.sum())
    comm = np.linalg.norm(Hm@Jm - Jm@Hm)/(np.linalg.norm(Hm)*np.linalg.norm(Jm))*np.sqrt(Hm.shape[0])
    return out, comm

SQ_CL = [((2, 2), (-2, 2)), ((3, 0), (0, 3)), ((3, 1), (-1, 3)), ((3, 0), (0, 4))]   # N = 8, 9, 10, 12
HC_CL = [((2, 0), (0, 2)), ((2, 1), (-1, 2)), ((3, 0), (0, 2))]                      # cells 4, 5, 6 -> N = 8, 10, 12
TC_CL = [((2, 0), (0, 2)), ((2, 1), (-1, 2)), ((3, 0), (0, 2))]                      # 2 qubits/cell -> 8, 10, 12

MODELS = {
    "xxchains": (M.xx_chains(), 1, SQ_CL),
    "tfim3": (M.tfim(3.0), 1, SQ_CL),
    "tfim1": (M.tfim(1.0), 1, SQ_CL),
    "xx2d": (M.xx2d(), 1, SQ_CL),
    "compass": (M.compass(), 1, SQ_CL),
    "xumoore1": (M.plaquette_ising(1.0), 1, SQ_CL),
    "kitaev": (M.kitaev(), 2, HC_CL),
    "kitaevJz0": (M.kitaev(1.0, 1.0, 0.0), 2, HC_CL),
    "kitaevh": (M.kitaev(hfield=0.1), 2, HC_CL),
    "tc_hz": (M.toric(hz=0.3), 2, TC_CL),
}
if __name__ == "__main__":
    betas = (0.0, 0.5, 2.0)
    for name in sys.argv[1:]:
        (lat, H), nsub, cls = MODELS[name]
        J = energy_current(H, lat, comp=0)
        for L1, L2 in cls:
            t0 = time.time()
            Hm, Jm, N, bad = build_ops(H, J, nsub, L1, L2)
            if bad:
                print(f"{name:10s} N={N:2d} cluster {L1},{L2}: support wraps onto itself ({bad} placements) -- skipped", flush=True); continue
            rs, comm = drude(Hm, Jm, betas)
            print(f"{name:10s} N={N:2d} L1={L1} L2={L2}  ||[H,J]||_HS-density ratio={comm:.3e}  r(beta=0,0.5,2) = " +
                  "  ".join(f"{x:.4f}" for x in rs) + f"   ({time.time()-t0:.1f}s)", flush=True)
