"""R2 steps 1-3: spectra, helicities, dispersion exponents, protection, mass terms,
lattice Brillouin-zone check and isotropy tuning count.
"""
import numpy as np
from r2_common import *
from r2_terms import functionals, weak_count, KS

rng = np.random.default_rng(11)
np.set_printoptions(precision=4, suppress=True, linewidth=150)
DGRP = [Drep(g) for g in GROUP]


def reyn(Qf):
    return lambda k: sum(D.T @ Qf(g @ k) @ D for g, D in zip(GROUP, DGRP)) / 24.0


def K0(kA1, kE, kT2):
    return kA1 * P_A1 + kE * P_E + kT2 * P_T2


def strong_Q(Vf, d0, seed=0):
    F = functionals(Vf, d0)
    r = np.random.default_rng(seed)
    G = r.normal(size=(len(F), len(F)))
    M = G @ G.T + 0.5 * np.eye(len(F))
    def Q(k):
        Fm = np.array([f(k) for f in F])
        return Fm.T @ M @ Fm
    return reyn(Q), len(F)


DIRS = {'[001]': np.array([0, 0, 1.]), '[110]': np.array([1, 1, 0.]) / S2,
        '[111]': np.ones(3) / np.sqrt(3), 'rand': np.array([0.31, -0.62, 0.72])}
DIRS['rand'] /= np.linalg.norm(DIRS['rand'])


def modes(K, Qf, Vf, n, kap, X=None, extraP=None, full=False):
    k = kap * n
    P = np.eye(6) if full else phys_projector(Vf(k), extraP)
    Xk = None if X is None else X(k)
    om, A, Pm = frequencies(K, Qf(k), P, Xk)
    out = []
    for j in range(len(om)):
        if om[j].real > -1e-14 or abs(om[j].imag) > 1e-12:
            a = Pm @ A[:, j]
            out.append((om[j], helicity_sq(a, n)))
    # keep positive-frequency (or unstable) half: pair (om, -om)
    out = sorted(out, key=lambda t: (round(t[0].real, 12), t[0].imag))
    return out


def summarize(name, K, Qf, Vf, extraP=None, X=None, full=False, kaps=(1e-3, 2e-3)):
    print(f'--- {name}')
    for dn, n in DIRS.items():
        m1 = modes(K, Qf, Vf, n, kaps[0], X, extraP, full)
        m2 = modes(K, Qf, Vf, n, kaps[1], X, extraP, full)
        rows = []
        for (o1, h1), (o2, h2) in zip(m1, m2):
            if abs(o1.imag) > 1e-12 * max(1, abs(o1)):
                rows.append(f'UNSTABLE(Im={o1.imag:.2e},m2={h1:.2f})')
                continue
            if o1.real < 1e-14:
                continue
            p = np.log(o2.real / o1.real) / np.log(kaps[1] / kaps[0])
            rows.append(f'w~k^{p:.2f} (m^2={h1:.2f}, w/k^p={o1.real / kaps[0] ** round(p):.3f})')
        print(f'  {dn:6s} n_phys_modes={len(rows)}: ' + '; '.join(rows))


if __name__ == '__main__':
    Kgen = K0(1.3, 0.8, 1.15)
    # ---------- step 1: generic strong Hamiltonians, each version
    print('STEP 1: generic STRONG cubic Hamiltonians (K0 generic cubic, Q = Reynolds(F^T M F), F lowest-degree invariants)')
    lowest = {'S': 1, 'S-tl': 1, 'V': 2, 'V-tl': 3}
    QS = {}
    for name, Vf in VERSIONS.items():
        Qf, nf = strong_Q(Vf, lowest[name], seed=3)
        QS[name] = Qf
        print(f'[{name}] invariant functionals of lowest degree {lowest[name]}: {nf}')
        summarize(name, Kgen, Qf, Vf)
    print()
    # ---------- step 2a: weak-only terms
    print('STEP 2a: add the weak-only (integrated-invariant) terms of lowest degree')
    for name, Vf, n in [('S', VERSIONS['S'], 1), ('V', VERSIONS['V'], 2), ('V-tl', VERSIONS['V-tl'], 3)]:
        w, N, basis, ms = weak_count(Vf, n)
        # weak symbols not in strong span: take nullspace vectors directly
        for j in range(N.shape[1]):
            c = N[:, j]
            def Qw(k, c=c, basis=basis, ms=ms):
                mv = np.array([np.prod(k ** np.array(m)) for m in ms])
                return eval_Q(c, basis, mv)
            Qw = reyn(Qw)
            # strength chosen so that it dominates at small k
            for sgn in (+1, -1):
                g = 0.5 * sgn
                Qtot = lambda k, g=g, Qw=Qw, Qs=QS[name]: Qs(k) + g * Qw(k) * np.linalg.norm(Qs(np.array([0, 0, 1.]))) / max(1e-12, np.linalg.norm(Qw(np.array([0, 0, 1.]))))
                summarize(f'{name} + ({"+" if sgn > 0 else "-"}) weak degree-{n} term #{j}', Kgen, Qtot, Vf, kaps=(1e-4, 2e-4))
    print()
    # ---------- step 2b: label-dependent shear (non-gauge-invariant) mass terms on S
    print('STEP 2b: S + cubic shear mass terms mu_E*P_E + mu_T2*P_T2 (gauge broken; full 6x6 phase space)')
    for muE, muT2 in [(0, 0), (1e-2, 0), (0, 1e-2), (1e-2, 2e-2)]:
        Qm = lambda k, muE=muE, muT2=muT2: QS['S'](k) + muE * P_E + muT2 * P_T2
        summarize(f'S + muE={muE}, muT2={muT2}', Kgen, Qm, VERSIONS['S'], full=True)
    print()
