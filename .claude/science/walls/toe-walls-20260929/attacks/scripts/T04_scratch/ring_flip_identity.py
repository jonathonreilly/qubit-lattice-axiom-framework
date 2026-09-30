#!/usr/bin/env python3
"""T04 test: ring flip as record motion; dependence on record distinguishability class.

Window (scaled Z^2 coordinates): links b r t l, vertices v1..v4, plaquette centre c.
Two hard-core records. Low states A={b,r} (CCW), B={t,l} (CW).
See PREREG.md for the readings fixed before running.
"""
import itertools, sys
import numpy as np

SITES = {
    'b': (1, 0), 'r': (2, 1), 't': (1, 2), 'l': (0, 1),
    'v1': (0, 0), 'v2': (2, 0), 'v3': (2, 2), 'v4': (0, 2),
    'c': (1, 1),
}
NAMES = list(SITES)                      # fixed mode order (used for fermion signs)
IDX = {n: i for i, n in enumerate(NAMES)}
LINKS = {'b', 'r', 't', 'l'}
VERTS = {'v1', 'v2', 'v3', 'v4'}
A_OCC = frozenset({'b', 'r'})
B_OCC = frozenset({'t', 'l'})
ADJ = {n: [m for m in NAMES if abs(SITES[n][0]-SITES[m][0]) + abs(SITES[n][1]-SITES[m][1]) == 1]
       for n in NAMES}


MODEL = 'U'   # 'U': ad-hoc on-link penalty; 'ice': G * sum_v (D_v/2)^2 with D_v the vertex divergence


def ice_pen(occ):
    s = {e: (1 if e in occ else -1) for e in LINKS}
    D = [s['b'] + s['l'], -s['b'] + s['r'], -s['r'] - s['t'], -s['l'] + s['t']]
    return sum((d / 2.0) ** 2 for d in D)


def energy(occ, Dv, Dc, U):
    occ = frozenset(occ)
    if MODEL == 'ice':
        return Dv * len(occ & VERTS) + (Dc if 'c' in occ else 0.0) + U * ice_pen(occ)
    e = Dv * len(occ & VERTS) + (Dc if 'c' in occ else 0.0)
    if occ <= LINKS and occ not in (A_OCC, B_OCC):
        e += U
    return e


# ---------- basis builders ----------
def basis_identical():
    return [tuple(sorted(s, key=lambda n: IDX[n])) for s in itertools.combinations(NAMES, 2)]


def basis_dist():
    return [(p, q) for p in NAMES for q in NAMES if p != q]


def build_identical(kind, t, Dv, Dc, U):
    B = basis_identical()
    ix = {s: i for i, s in enumerate(B)}
    n = len(B)
    H0 = np.zeros((n, n)); V = np.zeros((n, n))
    for s, i in ix.items():
        H0[i, i] = energy(s, Dv, Dc, U)
        for pos, src in enumerate(s):
            rest = [m for m in s if m != src]
            for dst in ADJ[src]:
                if dst in rest:
                    continue
                new = rest + [dst]
                new_sorted = tuple(sorted(new, key=lambda m: IDX[m]))
                sign = 1.0
                if kind == 'F':
                    sign = (-1.0) ** pos                      # remove src at position pos
                    sign *= (-1.0) ** sum(1 for m in rest if IDX[m] < IDX[dst])   # insert dst
                V[ix[new_sorted], i] += -t * sign
    return B, ix, H0, V


def build_dist(t, Dv, Dc, U):
    B = basis_dist()
    ix = {s: i for i, s in enumerate(B)}
    n = len(B)
    H0 = np.zeros((n, n)); V = np.zeros((n, n))
    for (p, q), i in ix.items():
        H0[i, i] = energy({p, q}, Dv, Dc, U)
        for dst in ADJ[p]:
            if dst != q:
                V[ix[(dst, q)], i] += -t
        for dst in ADJ[q]:
            if dst != p:
                V[ix[(p, dst)], i] += -t
    return B, ix, H0, V


# ---------- 4th-order effective Hamiltonian (degenerate P, E_P = 0, PVP = 0) ----------
def effective(H0, V, Pidx):
    n = H0.shape[0]
    P = np.zeros((n, n)); P[Pidx, Pidx] = 1.0
    Q = np.eye(n) - P
    e = np.diag(H0)
    assert np.allclose(e[Pidx], 0.0)
    R = np.zeros((n, n))
    for i in range(n):
        if Q[i, i] > 0:
            R[i, i] = -1.0 / e[i]                # R = Q/(E_P - H0)
    assert np.allclose(P @ V @ P, 0)
    H2 = P @ V @ R @ V @ P
    K2 = P @ V @ R @ R @ V @ P
    H4 = P @ V @ R @ V @ R @ V @ R @ V @ P - 0.5 * (K2 @ H2 + H2 @ K2)
    H3 = P @ V @ R @ V @ R @ V @ P
    assert np.allclose(H3, 0)
    return H2[np.ix_(Pidx, Pidx)], H4[np.ix_(Pidx, Pidx)]


def low_indices(B, kind):
    if kind in ('B', 'F'):
        return [i for i, s in enumerate(B) if frozenset(s) in (A_OCC, B_OCC)]
    return [i for i, s in enumerate(B) if frozenset(s) in (A_OCC, B_OCC)]


def run_case(Dv, Dc, U, tED=0.03):
    out = {}
    # ---- distinguishable ----
    t = 1.0
    Bd, ixd, H0d, Vd = build_dist(t, Dv, Dc, U)
    Pd = low_indices(Bd, 'D')
    H2d, H4d = effective(H0d, Vd, Pd)
    lab = [Bd[i] for i in Pd]
    def entry(dst, src):
        return H4d[lab.index(dst), lab.index(src)]
    A1 = ('b', 'r')
    a1 = entry(('l', 't'), A1)            # b->l, r->t  (adjacent shifts)
    a2 = entry(('t', 'l'), A1)            # b->t, r->l  (across the centre)
    a1b = entry(('t', 'l'), ('r', 'b'))   # relabelled check: (x@r,y@b) -> (x@t,y@l)
    cex = entry(('r', 'b'), A1)           # pure exchange at fixed occupancy
    out['a1'] = a1; out['a2'] = a2; out['cex'] = cex; out['a1_relabel_check'] = a1b
    # ---- identical ----
    for kind in ('B', 'F'):
        Bi, ixi, H0i, Vi = build_identical(kind, 1.0, Dv, Dc, U)
        Pi = low_indices(Bi, kind)
        H2i, H4i = effective(H0i, Vi, Pi)
        labi = [frozenset(Bi[i]) for i in Pi]
        iA, iB = labi.index(A_OCC), labi.index(B_OCC)
        out['J_' + kind] = H4i[iB, iA]
        out['diag_' + kind] = H4i[iA, iA]
        out['H2_' + kind] = H2i[iA, iA]
        # ---- exact diagonalisation at small t ----
        Bi, ixi, H0i, Vi = build_identical(kind, tED, Dv, Dc, U)
        H = H0i + Vi
        w, U_ = np.linalg.eigh(H)
        # two lowest states are in the A/B manifold
        lowpair = w[:2]
        split_half = 0.5 * (lowpair[1] - lowpair[0])
        out['ED_halfsplit_' + kind] = split_half
        out['ED_pred_' + kind] = abs(out['J_' + kind]) * tED ** 4 + 0.0
        # leakage: weight of ground state on non-link occupancies
        g = U_[:, 0]
        offl = sum(g[i] ** 2 for i, s in enumerate(Bi) if not frozenset(s) <= LINKS)
        out['leak_' + kind] = offl
        out['t_ED'] = tED
    return out


def main():
    global MODEL
    MODEL = sys.argv[1] if len(sys.argv) > 1 else 'U'
    print('MODEL =', MODEL, '(param U is the ad-hoc on-link penalty for MODEL=U, the Gauss coupling G for MODEL=ice)')
    params = [(1, 1, 1), (1, 2, 1), (1, 0.5, 1), (1, 1, 3), (1, 4, 1), (2, 1, 3), (1, 20, 1)]
    ok = True
    print(f"{'(Dv,Dc,U)':<14}{'a1':>12}{'a2':>12}{'a1+a2':>12}{'J_B':>12}{'a1-a2':>12}{'J_F':>12}{'|JF/JB|':>10}{'cex':>10}")
    rows = []
    for Dv, Dc, U in params:
        r = run_case(Dv, Dc, U)
        rows.append(((Dv, Dc, U), r))
        ratio = abs(r['J_F']) / abs(r['J_B']) if abs(r['J_B']) > 1e-14 else float('nan')
        print(f"{str((Dv,Dc,U)):<14}{r['a1']:12.6f}{r['a2']:12.6f}{r['a1']+r['a2']:12.6f}"
              f"{r['J_B']:12.6f}{r['a1']-r['a2']:12.6f}{r['J_F']:12.6f}{ratio:10.4f}{r['cex']:10.5f}")
        # P1 checks
        c1 = abs(abs(r['J_B']) - abs(r['a1'] + r['a2'])) < 1e-9
        c2 = abs(abs(r['J_F']) - abs(r['a1'] - r['a2'])) < 1e-9
        c3 = abs(r['a1'] - r['a1_relabel_check']) < 1e-9
        if not (c1 and c2 and c3):
            ok = False
            print('   P1 FAILED', c1, c2, c3)
    print()
    print('ED cross-check (half-splitting of the two lowest levels vs |J| t^4), t = 0.03')
    for (p, r) in rows:
        for kind in 'BF':
            pred = r['ED_pred_' + kind]; ed = r['ED_halfsplit_' + kind]
            rel = abs(ed - pred) / pred if pred > 1e-30 else float('nan')
            print(f"  {str(p):<12} {kind}: ED {ed:.4e}  4th-order {pred:.4e}  rel.diff {rel:.3%}   leak weight {r['leak_'+kind]:.3e}")
    print()
    # t-scaling of ED splitting and leakage for the symmetric set, bosons/fermions
    print('t-scaling at (1,1,1): half-splitting / t^4 and leak / t^2')
    for kind in 'BF':
        for tt in (0.10, 0.05, 0.025, 0.0125):
            Bi, ixi, H0i, Vi = build_identical(kind, tt, 1, 1, 1)
            w, U_ = np.linalg.eigh(H0i + Vi)
            g = U_[:, 0]
            leak = sum(g[i] ** 2 for i, s in enumerate(Bi) if not frozenset(s) <= LINKS)
            print(f"  {kind} t={tt:<7} halfsplit/t^4 = {0.5*(w[1]-w[0])/tt**4: .5f}   leak/t^2 = {leak/tt**2:.5f}")
    print()
    print('ALL P1 CHECKS OK' if ok else 'P1 CHECK FAILED')
    return 0 if ok else 1


if __name__ == '__main__':
    sys.exit(main())
