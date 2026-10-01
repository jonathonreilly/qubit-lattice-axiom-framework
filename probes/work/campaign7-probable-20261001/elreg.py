"""Which local features carry the variance of E_L (walker level, mixed population, guide exp(0.2 N_flip) + optional beta modes)?  usage: python3 elreg.py L NW SEED NGEN BETA
Regress E_L on N_flip; N_flip and N_flip^2; N_flip + per-orientation counts; and + adjacent flippable pair count (plaquettes sharing a link)."""
import sys, time
from scipy.sparse import coo_matrix
from gguide_lib import *

L, NW, SEED, NGEN, BETA = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4]), float(sys.argv[5])
t0 = time.time()
ice = Ice(L)
PH = cyclic_modes(ice, [1]); beta = np.full(3, BETA)
rr = np.random.default_rng(SEED * 100 + L + NW)
init = loop_vmc_g(ice, ALPHA, PH, beta, sweeps=max(40, 1600 // L), therm=60, r=rr, start=ice.sector_state(0), fix_winding=True)
pr = GProjector(ice, ALPHA, beta, PH, V=0.0, seed=SEED)
st = pr.make_state(init, NW, rr)
logw = np.zeros(NW); EL = np.zeros(NW)
rows, cols = [], []
for p in range(ice.np_):
    for q in pr.A[p]:
        if q >= 0 and q != p:
            rows.append(p); cols.append(q)
Adj = coo_matrix((np.ones(len(rows)), (rows, cols)), shape=(ice.np_, ice.np_)).tocsr()
orient = np.arange(ice.np_) % 3                       # plaquette index = 3 * vertex + (0: (0,1), 1: (1,2), 2: (0,2))
THERM = NGEN // 4
rowsE, rowsX = [], []
for g in range(NGEN):
    if g % 10 == 0 and g > 0:
        st["Om"] = np.ascontiguousarray(st["sig"].astype(np.float64) @ pr.PH)
    pr._walk(st, DTAU, logw, EL)
    mx = logw.max(); w = np.exp(logw - mx); wn = w / w.sum()
    if g >= THERM and g % 5 == 0:
        F = st["flp"].astype(np.float64)
        pairs = 0.5 * np.einsum("ij,ij->i", np.asarray(Adj.T @ F.T).T, F)
        no = np.stack([F[:, orient == k].sum(axis=1) for k in range(3)], axis=1)
        rowsE.append(EL.copy()); rowsX.append(np.column_stack([st["nflp"], no, pairs]))
    cum = np.cumsum(wn)
    picks = np.minimum(np.searchsorted(cum, (np.arange(NW) + rr.random()) / NW), NW - 1)
    for key in ("sig", "C", "flp", "dN", "rate0", "cls", "nflp", "Om"):
        st[key] = st[key][picks]
E = np.concatenate(rowsE); X = np.concatenate(rowsX)
Nf, No, Pr = X[:, 0], X[:, 1:4], X[:, 4]


def r2(y, F):
    F1 = np.column_stack([np.ones(len(y)), F])
    c, *_ = np.linalg.lstsq(F1, y, rcond=None)
    return 1 - (y - F1 @ c).var() / y.var(), c


print(f"L {L} NW {NW} seed {SEED} beta {BETA}: E_L mean {E.mean():.2f} sd {E.std():.3f}; N_flip mean {Nf.mean():.1f} sd {Nf.std():.3f} (Poisson sd would be {np.sqrt(Nf.mean()):.1f}); "
      f"R^2(E_L on N_flip) {r2(E, Nf)[0]:.4f} slope {r2(E, Nf)[1][1]:.4f}; on (N_flip, N_flip^2) {r2(E, np.column_stack([Nf, Nf ** 2]))[0]:.4f}; "
      f"on N_flip + 3 orientation counts {r2(E, np.column_stack([Nf, No]))[0]:.4f}; on N_flip + pair count {r2(E, np.column_stack([Nf, Pr]))[0]:.4f}; "
      f"on N_flip + orientations + pairs {r2(E, np.column_stack([Nf, No, Pr]))[0]:.4f}; sd of residual after N_flip + pairs {np.sqrt(E.var() * (1 - r2(E, np.column_stack([Nf, Pr]))[0])):.3f}; {time.time() - t0:.0f} s", flush=True)
