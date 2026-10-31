"""c19b: reflection-matters control for Lemma GT (criteria: checks/c19b_criteria.md, written before this script).

Q_eps = sum eps^{mu nu rho sigma} (-1/2) Re tr(C_mu nu C_rho sigma), C = clover average of the anti-Hermitian parts of
the four leaves at the site 0. Invariant under gauge and B_4 cap SO(4) (incl. iota), odd under reflections.
Reuses c19's backgrounds, transporters and paths (imported, not copied).
"""
import itertools
import os
import sys

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import c19_gauge_taylor as c19  # noqa: E402

E = c19.E
ORIGIN = np.zeros(4)


def eps4():
    T = np.zeros((4, 4, 4, 4))
    for p in itertools.permutations(range(4)):
        sgn = np.linalg.det(np.eye(4)[list(p)])
        T[p] = sgn
    return T


EPS = eps4()


def neg(m):
    return -m - 1


def clover(U, mu, nu):
    leaves = [[mu, nu, neg(mu), neg(nu)], [nu, neg(mu), neg(nu), mu],
              [neg(mu), neg(nu), mu, nu], [neg(nu), mu, nu, neg(mu)]]
    C = np.zeros((2, 2), dtype=complex)
    for st in leaves:
        W = c19.path(U, ORIGIN, st)
        C += 0.5 * (W - c19.dag(W))
    return C / 4


def Qeps(U):
    C = {(m, n): clover(U, m, n) for m in range(4) for n in range(4) if m != n}
    tot = 0.0
    for m, n, r, s in itertools.permutations(range(4)):
        tot += EPS[m, n, r, s] * (-0.5) * np.real(np.trace(C[(m, n)] @ C[(r, s)]))
    return tot


FUNCS = {'Q': Qeps, 'G': lambda U: c19.F1(U) + Qeps(U)}
RREF = np.diag([-1.0, 1, 1, 1])


def reflect(A):
    def Ar(x):
        Ax = A(x @ RREF.T)  # A(R^{-1} x), R = R^{-1}
        return np.einsum('nm,...mij->...nij', RREF, Ax)
    return Ar


def main():
    kinds = ['abelian', 'sd', 'asd', 'generic', 'generic']
    svals = [0.4, 0.2, 0.1, 0.05, 0.025]
    U0 = np.broadcast_to(c19.I2, (len(c19.LINKS), 2, 2)).copy()
    f0 = {k: fn(U0) for k, fn in FUNCS.items()}
    ok = {f'Q{i}': True for i in range(1, 7)}
    out = []
    cvals = {k: {} for k in FUNCS}
    q4_seen = False
    for ib, kind in enumerate(kinds):
        A, F0 = c19.make_background(kind)
        FF = sum(np.sum(np.abs(c19.alg(F0[m, n])) ** 2) for m, n in c19.PAIRS)
        vals = {k: {} for k in FUNCS}
        for s in svals:
            for sg in (1, -1):
                U = c19.transporters(A, sg * s)
                for k, fn in FUNCS.items():
                    vals[k][sg * s] = fn(U)
        Ag = c19.make_gauge()(A)
        Ug = c19.transporters(Ag, 0.2, nsteps=256)
        Ur = c19.transporters(A, 0.2, nsteps=256)
        gd = abs(Qeps(Ug) - Qeps(Ur))
        if gd > 1e-10:
            ok['Q1'] = False
        for s in (0.4, 0.2, 0.1):
            if abs(vals['Q'][s] - vals['Q'][-s]) > 1e-11 * max(1, abs(vals['Q'][s])):
                ok['Q2'] = False
        for k in FUNCS:
            r = {s: (vals[k][s] - f0[k]) / s ** 4 for s in svals}
            R1 = {s: (4 * r[s / 2] - r[s]) / 3 for s in svals[:-1]}
            cvals[k][(ib, kind)] = (16 * R1[0.05] - R1[0.1]) / 15 / FF
        rq = {s: (vals['Q'][s] - f0['Q']) / s ** 4 for s in svals}
        ratio = np.nan
        if abs(rq[0.1]) > 1e-8:
            d1, d2 = abs(rq[0.2] - rq[0.1]), abs(rq[0.1] - rq[0.05])
            ratio = d1 / d2 if d2 > 0 else np.inf
            if not (3 <= ratio <= 5 or (d1 <= 1e-9 * abs(rq[0.1]) and d2 <= 1e-9 * abs(rq[0.1]))):
                ok['Q3'] = False
        refl = ''
        if kind == 'generic':
            Urf = c19.transporters(reflect(A), 0.2)
            qa, qr = vals['Q'][0.2], Qeps(Urf)
            refl = f"  refl: Q(A)={qa:.4e} Q(RA)={qr:.4e} |sum|={abs(qa + qr):.1e}"
            if abs(qa + qr) > 1e-10 or abs(qa) <= 1e-6:
                ok['Q4'] = False
            q4_seen = True
        out.append(f"  {kind:8s} Q: c={cvals['Q'][(ib, kind)]:+.10f}  G: c={cvals['G'][(ib, kind)]:+.10f}  "
                   f"r-diff ratio={ratio:.4f}  even|0.2|={abs(vals['Q'][0.2]-vals['Q'][-0.2]):.1e}  "
                   f"gauge={gd:.1e}{refl}")
    if not q4_seen:
        ok['Q4'] = False
    csd = cvals['Q'][(1, 'sd')]; casd = cvals['Q'][(2, 'asd')]
    m = max(abs(csd), abs(casd))
    out.append(f"Q5 c_sd = {csd:+.10f}, c_asd = {casd:+.10f}, |diff|/max = {abs(csd - casd) / m if m else 0:.3f}")
    ok['Q5'] = m > 1e-6 and abs(csd - casd) > 0.10 * m
    cg = np.array(list(cvals['G'].values()))
    spread = (cg.max() - cg.min()) / abs(cg.mean())
    out.append(f"Q6 G = F1 + Q_eps: c values {np.array2string(cg, precision=6)}, relative spread {spread:.3f}")
    ok['Q6'] = spread > 0.10
    for key in sorted(ok, key=lambda t: int(t[1:])):
        out.append(f"{key}: {'PASS' if ok[key] else 'FAIL'}")
    out.append(f"c19b overall: {'PASS' if all(ok.values()) else 'FAIL'} ({sum(ok.values())}/{len(ok)})")
    print("\n".join(out))


if __name__ == '__main__':
    main()
