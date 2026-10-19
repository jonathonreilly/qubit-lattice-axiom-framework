"""C3b s4 (candidate c): two-stage clock = level clocks in random body-diagonal directions on Poisson-Voronoi cells.

Clock (3D torus, side L): Poisson nuclei of intensity ell^-3; cell c gets iid w_c uniform on {+-1}^3 and offset
V_c ~ U[0, A]; T_x = <w_c, x - n_c> (minimum image) + V_c + s * Z_x + 1e-7 * Z'_x (tie-break).
This clock is a finitary factor of iid (Poisson + marks), hence translation-stationary and mixing; it is O_h-covariant
in law (w_c uniform over the 8 diagonals and the Poisson process is isotropic).  Inside a cell each site has exactly
three earlier neighbours (x - w_i e_i), so the noisy-majority rule there IS Toom's NEC-type majority PCA run along the
cell's diagonal (eroder; Toom 1980, imported).

Declared criteria: no-LRO if |slope| of log chi_L vs log L < 1.0 (LRO -> 3); colour correlation length reported vs ell.
Control: same rule, single level clock w=(1,1,1) on an OPEN box (no wrap), to show the within-cell ordering
mechanism (fraction of the majority colour in the late half of the box).
"""
import numpy as np
from scipy.spatial import cKDTree
import sys, os, time
sys.path.insert(0, os.path.dirname(__file__))
from c3b_common import check, total, nbr_table, depth_and_record, axis_corr, mean_se, fit_loglog

rng = np.random.default_rng(3141)


def two_stage_clock(L, ell, A, s):
    N = L ** 3
    X = np.indices((L, L, L)).reshape(3, -1).T.astype(float)
    m = max(1, rng.poisson(N / ell ** 3))
    nuc = rng.random((m, 3)) * L
    tree = cKDTree(nuc, boxsize=L)
    _, c = tree.query(X + 1e-9 * rng.random(X.shape))
    W = rng.choice([-1.0, 1.0], size=(m, 3))
    V = rng.random(m) * A
    disp = X - nuc[c]
    disp -= L * np.round(disp / L)
    T = (W[c] * disp).sum(1) + V[c] + s * rng.standard_normal(N) + 1e-7 * rng.standard_normal(N)
    return T


def run(L, ell, A, s, delta, ns, rmax):
    nbr = nbr_table((L, L, L))
    N = L ** 3
    Cs, chis, Lm, Lmax = [], [], [], []
    for _ in range(ns):
        T = two_stage_clock(L, ell, A, s)
        sig, Ld = depth_and_record(T, nbr, rng.random(N), rng.random(N), delta)
        F = sig.reshape(L, L, L)
        Cs.append(axis_corr(F, rmax)); chis.append(N * F.mean() ** 2)
        Lm.append(Ld.mean()); Lmax.append(Ld.max())
    return np.array(Cs), np.array(chis), np.array(Lm), np.array(Lmax)


def xi_of(C):
    thr = C[0] / np.e
    for r in range(1, len(C)):
        if C[r] < thr:
            return r - 1 + (C[r - 1] - thr) / (C[r - 1] - C[r])
    return np.nan


def open_box_level(Lb, delta, ns):
    """Open box, T_x = x1+x2+x3 + tiny noise, no periodic wrap: neighbour table with self-loops at the boundary."""
    shape = (Lb, Lb, Lb)
    idx = np.arange(Lb ** 3).reshape(shape)
    cols = []
    for ax in range(3):
        for sh in (1, -1):
            r = np.roll(idx, -sh, axis=ax)
            sl = [slice(None)] * 3
            sl[ax] = -1 if sh == 1 else 0
            r[tuple(sl)] = idx[tuple(sl)]  # self-loop = no neighbour (T_x < T_x is false)
            cols.append(r.ravel())
    nbr = np.stack(cols, 1).astype(np.int64)
    X = np.indices(shape).reshape(3, -1).T
    lev = X.sum(1)
    fr = []
    for _ in range(ns):
        T = lev + 1e-7 * rng.standard_normal(lev.size)
        sig, _ = depth_and_record(T, nbr, rng.random(lev.size), rng.random(lev.size), delta)
        late = sig[lev >= int(1.5 * (Lb - 1))]
        fr.append(abs(late.mean()))
    return np.array(fr)


if __name__ == "__main__":
    t0 = time.time()
    for Lb in (16, 32, 48):
        fr = open_box_level(Lb, 0.02, 12)
        m, se = mean_se(fr)
        print(f"control open box level clock Lb={Lb}: |m_late| = {m:.3f}+-{se:.3f}")
    print(f"  elapsed {time.time()-t0:.0f}s", flush=True)
    variants = [(4, 0.0, 0.0, 0.0), (8, 0.0, 0.0, 0.0), (8, 0.0, 0.0, 0.02), (8, 0.0, 0.3, 0.02), (12, 0.0, 0.0, 0.02)]
    xi_by_ell = {}
    for (ell, A, s, delta) in variants:
        Ls = [24, 48, 72] if ell <= 8 else [36, 72, 96]
        ch, che = [], []
        for L in Ls:
            ns = int(max(24, min(400, 2.0e7 / L ** 3)))
            Cs, chis, Lm, Lmax = run(L, ell, A, s, delta, ns, L // 2)
            m, se = mean_se(chis)
            ch.append(m); che.append(se)
            C = Cs.mean(0)
            print(f"ell={ell} A={A} s={s} delta={delta} L={L} ns={ns}: chi_L={m:.2f}+-{se:.2f} xi={xi_of(C):.2f}"
                  f" C(ell)={C[min(ell, L//2)]:.3f} C(L/2)={C[-1]:.4f}+-{Cs[:, -1].std(ddof=1)/np.sqrt(ns):.4f}"
                  f" <L(x)>={Lm.mean():.2f} maxL={Lmax.mean():.1f}", flush=True)
        xi_by_ell[(ell, A, s, delta)] = xi_of(C)
        sl, sse, _ = fit_loglog(np.array(Ls, float), np.array(ch), np.array(che))
        check(f"s4 ell={ell} s={s} delta={delta}: chi_L slope |.|<1 (no LRO; LRO->3)", abs(sl) < 1.0,
              f"slope={sl:.3f}+-{sse:.3f}")
        print(f"  elapsed {time.time()-t0:.0f}s", flush=True)
    r = [xi_by_ell[(e, 0.0, 0.0, 0.02)] / e for e in (8, 12)]
    print(f"NUMERICAL: xi/ell at delta=0.02: ell=8 -> {r[0]:.3f}, ell=12 -> {r[1]:.3f}")
    total()
