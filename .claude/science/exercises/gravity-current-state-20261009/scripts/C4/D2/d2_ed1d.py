"""D2 (c): exact diagonalization, one electron + acoustic phonons on an N-site ring,
phonon number truncated at M (all modes q = 2 pi p/N, p = 1..N-1; q = 0 decouples since M_0 = 0).
Electron twist phi gives continuous total momentum K = (2 pi J + phi)/N.
H = eps(k_e) + sum w(q) b_q^+ b_q + (1/sqrt N) sum |M_q| (emission + absorption),
phases of M_q gauged away (one-electron sector).  Lowest state per K, Z = |<K;0|psi>|^2.
Measures: face curvature C = 2[E(pi)-E(pi-d)]/d^2 vs N (diverges with N if a kink forms),
local exponent of D(d), Z(pi) vs N and M."""
import numpy as np, sys, time, itertools
import scipy.sparse as sp
from scipy.sparse.linalg import eigsh
from d2_common import eps_band, phonon, vertex2, TWO_PI

def build(N, M, c, g2, a):
    modes = list(range(1, N))
    confs = []
    for n in range(M + 1):
        confs.extend(itertools.combinations_with_replacement(modes, n))
    index = {cf: i for i, cf in enumerate(confs)}
    D = len(confs)
    q = TWO_PI * np.arange(N) / N
    w = phonon(q, c); Mabs = np.sqrt(vertex2(q, g2, a)) / np.sqrt(N)
    Om = np.array([w[list(cf)].sum() if cf else 0.0 for cf in confs])
    P = np.array([sum(cf) for cf in confs])
    rows, cols, vals = [], [], []
    for i, cf in enumerate(confs):
        if len(cf) == M:
            continue
        for p in modes:
            new = tuple(sorted(cf + (p,)))
            j = index[new]
            npl = new.count(p)          # occupation after emission
            amp = Mabs[p] * np.sqrt(npl)
            rows.append(j); cols.append(i); vals.append(amp)
    Hoff = sp.coo_matrix((vals, (rows, cols)), shape=(D, D)).tocsr()
    Hoff = (Hoff + Hoff.T).tocsr()
    return Hoff, Om, P, D

def lowest(Hoff, Om, P, N, K, kind, v0=None):
    ke = K - TWO_PI * P / N
    H = Hoff + sp.diags(eps_band(kind, ke) + Om)
    vals, vecs = eigsh(H, k=1, which='SA', tol=1e-13, v0=v0, ncv=40, maxiter=5000)
    v = vecs[:, 0]
    return vals[0], v[0] ** 2, v

def run(kind, N, M, c, g2, a, deltas):
    t = time.time()
    Hoff, Om, P, D = build(N, M, c, g2, a)
    Ks = [np.pi] + [np.pi - d for d in deltas] + [0.0]
    out = {}; v = None
    for K in Ks:
        e, z, v = lowest(Hoff, Om, P, N, K, kind, v0=v)
        out[K] = (e, z)
    Epi, Zpi = out[np.pi]
    Ds = [Epi - out[np.pi - d][0] for d in deltas]
    C = [2 * Dd / d ** 2 for Dd, d in zip(Ds, deltas)]
    pl = [np.log(Ds[i + 1] / Ds[i]) / np.log(deltas[i + 1] / deltas[i]) for i in range(len(deltas) - 1)]
    bw = Epi - out[0.0][0]
    # SLAC fit on [pi - w, pi] using the computed points (sparse; diagnostic only)
    print(f"{kind} N={N} M={M} D={D} c={c} a={a} g2={g2} | E0={out[0.0][0]:.6f} Epi={Epi:.6f} bw={bw:.5f} | "
          f"Z0={out[0.0][1]:.4f} Zpi={Zpi:.4f} | C(d)=" + " ".join(f"{x:.4f}" for x in C)
          + " | p=" + " ".join(f"{x:.3f}" for x in pl) + f" | t={time.time()-t:.1f}s", flush=True)
    return out

if __name__ == '__main__':
    deltas = [0.005, 0.02, 0.08, 0.32]
    which = sys.argv[1] if len(sys.argv) > 1 else 'main'
    print("# columns: C(d) = 2[E(pi)-E(pi-d)]/d^2 at d = " + ", ".join(map(str, deltas))
          + " (finite and N-stable = smooth max; growing ~N = kink forming); p = local exponents of D(d)")
    if which == 'Mconv':
        for M in [3, 4, 5, 6, 7]:
            run('TB', 12, M, 1.5, 1.0, 0.5, deltas)
        for M in [3, 4, 5, 6, 7]:
            run('TB', 12, M, 0.4, 0.3, 0.5, deltas)
    else:
        cases = [('TB', 1.5, 0.3, 0.5), ('TB', 1.5, 1.0, 0.5), ('TB', 1.5, 1.0, 1.0), ('TB', 1.5, 1.0, 0.25),
                 ('TB', 0.4, 0.3, 0.5), ('TB', 0.4, 0.05, 0.5), ('KG', 1.0, 1.0, 0.5)]
        NM = [(8, 8), (12, 7), (16, 6), (20, 5), (24, 5)]
        for kind, c, g2, a in cases:
            for N, M in NM:
                run(kind, N, M, c, g2, a, deltas)
