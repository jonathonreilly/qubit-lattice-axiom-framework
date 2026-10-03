"""A44 lswt: classical energies and linear-spin-wave ground-state energies of the named product
backgrounds over the (J,K,D) sphere.  Reuses A43's Holstein-Primakoff library (SP/c8/A43/w2_lswt.py,
library part only, exactly as A43's w3 does).  E_LSWT/site = E_cl + (1/2) <sum_n w_n(k) - tr A(k)>_k / n_cell.
Also: greedy classical minimum on the 4^3 and 8^3 tori and the Luttinger-Tisza lower bound."""
import sys, time, signal, itertools, numpy as np
signal.alarm(285)
sys.path.insert(0, __file__.rsplit('/', 1)[0])
from a44lib import cube, greedy_classical, coupling_mats
A43 = __file__.rsplit('/', 2)[0] + "/A43/w2_lswt.py"
src = open(A43).read().split("# 1. Heisenberg ferromagnet")[0]
ns = {}; exec(compile(src, "A43_w2lib", "exec"), ns)
Lattice, couplings = ns["Lattice"], ns["couplings"]
t0 = time.time()

cell8 = [list(p) for p in itertools.product([0, 1], repeat=3)]
Bsp = np.array([[1, 1, 1], [-1, 0, 1], [0, -1, 2]], float); tau4 = [[0, 0, 0], [1, 0, 0], [2, 0, 0], [3, 0, 0]]
def spiral(sgn):
    w = -sgn * np.ones(3) / np.sqrt(3); u = np.array([1, -1, 0]) / np.sqrt(2); v = np.cross(w, u)
    return [u * np.cos(np.pi / 2 * sum(t)) + v * np.sin(np.pi / 2 * sum(t)) for t in tau4]
def states(Jv):
    J, K, D = Jv; cp = couplings(J=J, K=K, D=D)
    out = {}
    for lab, n in (("uniform z", [0, 0, 1]), ("uniform 111", [1, 1, 1]), ("uniform 110", [1, 1, 0])):
        out[lab] = Lattice(np.eye(3), [[0, 0, 0]], [n], cp)
    for lab, n in (("Neel z", [0, 0, 1]), ("Neel 111", [1, 1, 1])):
        out[lab] = Lattice(2 * np.eye(3), cell8, [((-1) ** sum(p)) * np.array(n, float) for p in cell8], cp)
    out["compass-stag 111"] = Lattice(2 * np.eye(3), cell8, [np.array([(-1) ** p[0], (-1) ** p[1], (-1) ** p[2]]) / np.sqrt(3) for p in cell8], cp)
    out["compass-stag z"] = Lattice(2 * np.eye(3), cell8, [np.array([0, 0, (-1) ** p[2]], float) for p in cell8], cp)
    out["Moriya spiral"] = Lattice(Bsp, tau4, spiral(1 if D >= 0 else -1), cp)
    return out

def lswt(lat, nk):
    g = (np.arange(nk) + 0.5) / nk * 2 * np.pi - np.pi       # shifted grid in units of the cell's reciprocal basis
    Rb = 2 * np.pi * np.linalg.inv(lat.B)                   # rows b_i with b_i . B[:, j] = 2 pi delta_ij
    tot = 0.; minM = np.inf; imag = 0.
    for f in itertools.product(g, g, g):
        k = (np.array(f) / (2 * np.pi)) @ Rb
        A, Bm = lat.blocks(k)
        M = lat.M(k); minM = min(minM, np.linalg.eigvalsh(M).min())
        w = lat.omega(k); imag = max(imag, np.abs(w.imag).max())
        tot += np.sum(w.real) - np.trace(A).real
    return lat.energy() + 0.5 * tot / nk ** 3 / lat.n, minM, imag

# convergence check at three points
print("[0] k-grid convergence (E_LSWT per bond):")
for Jv, lab in (((1, 0, 0), "Neel z @ J=1"), ((0, 1, 0), "compass-stag 111 @ K=1"), ((0, 0, 1), "Moriya spiral @ D=1"),
                ((-1, 1, 0), "uniform 111 @ (-1,1,0)/sqrt2")):
    Jv = np.array(Jv, float) / np.linalg.norm(Jv)
    lat = states(Jv)[lab.split(" @")[0]]
    vals = [lswt(lat, nk)[0] / 3 for nk in (4, 6, 8)]
    print(f"    {lab:32s}: nk=4,6,8 -> {vals[0]:+.6f} {vals[1]:+.6f} {vals[2]:+.6f}", flush=True)
print(f"    (comparator: Heisenberg AFM S=1/2 cubic LSWT ~ -1.193/bond in Pauli units); t={time.time()-t0:.0f}s", flush=True)

dirs = [(0., ph) for ph in np.arange(0, 360, 7.5)] + [(be, ph) for be in (30., 60.) for ph in np.arange(0, 360, 30)] + [(90., 0.)]
rng = np.random.default_rng(4444)
c4, c8 = cube(4), None
print("[1] beta phi | J K D | best named classical (state) | best stable LSWT (state) | greedy 4^3 | LT bound")
rows = []
for be, ph in dirs:
    bR, pR = np.radians(be), np.radians(ph)
    Jv = np.array([np.cos(bR) * np.cos(pR), np.cos(bR) * np.sin(pR), np.sin(bR)])
    st = states(Jv)
    cl_best = min(((lat.energy() / 3, lab) for lab, lat in st.items() if lat.stationarity() < 1e-9), default=(np.nan, "-"))
    lsw = []
    for lab, lat in st.items():
        if lat.stationarity() > 1e-9 or lat.energy() / 3 > cl_best[0] + 0.15:
            continue
        e, minM, im = lswt(lat, 6)
        if minM > -1e-7:
            lsw.append((e / 3, lab, lat.energy() / 3))
    lb = min(lsw) if lsw else (np.nan, "-", np.nan)
    Eg, _ = greedy_classical(c4, Jv, rng, starts=6, iters=150)
    # Luttinger-Tisza: E/bond >= min_q lambda_min(Lambda(q))/3, Lambda(q) = sum_a (M_a e^{iq_a} + M_a^T e^{-iq_a})
    Ms = coupling_mats(Jv)
    Q = np.array(list(itertools.product(np.linspace(-np.pi, np.pi, 25), repeat=3)))
    Lq = sum(Ms[a][None] * np.exp(1j * Q[:, a])[:, None, None] + Ms[a].T[None] * np.exp(-1j * Q[:, a])[:, None, None] for a in range(3))
    lt = np.linalg.eigvalsh((Lq + np.conj(np.transpose(Lq, (0, 2, 1)))) / 2).min()
    rows.append((be, ph, *Jv, cl_best[0], lb[0], Eg, lt / 3))
    print(f"{be:4.0f} {ph:6.1f} | {Jv[0]:+.3f} {Jv[1]:+.3f} {Jv[2]:+.3f} | {cl_best[0]:+.5f} ({cl_best[1]}) | "
          f"{lb[0]:+.5f} ({lb[1]}, cl {lb[2]:+.5f}) | {Eg:+.5f} | {lt/3:+.5f}", flush=True)
np.save("lswt_rows.npy", np.array(rows))
print(f"done {time.time()-t0:.0f}s")
