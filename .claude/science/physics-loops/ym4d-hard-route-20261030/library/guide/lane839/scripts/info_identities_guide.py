#!/usr/bin/env python3
"""GUIDE run for FINISH row 839 (gap-compress-opus). Decides nothing.

Criteria written before the run (FAIL at any point means the algebra of the
note is wrong, or the code is):
  C1  S(2n) == I_chi2(X_0; X_n) of the Doob chain           (Identity I1)
  C2  S_-(2n) == (1/4) E_pi || f_x - f_Jx ||^2_{L2(pi)}      (Identity I3)
  C3  2F(n)-F(2n) == H_2(rho_n), log(1+S(n)) == H_inf(rho_n) (Identity I2)
  C4  log(1+S(T0; rho T0)) <= Phi/(rho-1); compare with (2/rho) Phi
      (2D form of Lemma Z'' and of Lemma Z')
  C5  (mu^-)^t <= eta_t := max_x TV(P^t(x,.), P^t(Jx,.))      (Prop. TB)
  C6  p(a) == (1/2)(1 - E_w ratio_t) <= (1/2) E_w|1 - ratio_t| (t-layer
      Identity L) on the torus of length a
Model: 2D Ising, transfer along direction 1, periodic width w, coupling K,
J = global spin flip (a LOCAL Z_2 sector; the gauge centre flip is non-local).
Spectra are computed blockwise on the J-even and J-odd subspaces, so that
degenerate eigenspaces cannot mix parities.
Also prints the numbers used in Propositions K, Q, TB2 of the note.
Memory: w <= 10 (1024 x 1024 matrices), well under 300 MB.
"""
import sys
import numpy as np
from scipy import integrate, special


def transfer(w, K):
    n = 1 << w
    idx = np.arange(n)
    spins = 1 - 2 * ((idx[:, None] >> np.arange(w)[None, :]) & 1)  # +-1
    horiz = (spins * np.roll(spins, -1, axis=1)).sum(axis=1)       # ring bonds
    overlap = spins @ spins.T                                       # sum s_i s'_i
    D = np.exp(0.5 * K * horiz)
    T = D[:, None] * np.exp(K * overlap) * D[None, :]
    J = (n - 1) - idx                                               # global flip
    return T, J


def parity_blocks(T, J):
    n = T.shape[0]
    reps = np.array([x for x in range(n) if x < J[x]])
    Ue = np.zeros((n, len(reps)))
    Uo = np.zeros((n, len(reps)))
    s = 1 / np.sqrt(2)
    Ue[reps, np.arange(len(reps))] = s
    Ue[J[reps], np.arange(len(reps))] = s
    Uo[reps, np.arange(len(reps))] = s
    Uo[J[reps], np.arange(len(reps))] = -s
    le, ve = np.linalg.eigh(Ue.T @ T @ Ue)
    lo, vo = np.linalg.eigh(Uo.T @ T @ Uo)
    return le[::-1], (Ue @ ve)[:, ::-1], lo[::-1], (Uo @ vo)[:, ::-1]


def analyse(w, K, ns=(1, 2, 3), ts=(1, 2, 3, 4)):
    T, J = transfer(w, K)
    le, ve, lo, vo = parity_blocks(T, J)
    lam0 = le[0]
    assert lam0 > lo[0]
    Om = ve[:, 0] * np.sign(ve[:, 0].sum())
    assert Om.min() > 0
    mu_e, mu_o = le / lam0, lo / lam0
    pi = Om ** 2
    P = T * Om[None, :] / (lam0 * Om[:, None])
    res = {'w': w, 'K': K, 'rowsum_err': float(np.abs(P.sum(1) - 1).max())}
    F = lambda t: t * np.log(lam0) + np.log((mu_e ** t).sum() + (mu_o ** t).sum())
    Pn = np.eye(len(Om))
    c1 = c2 = c3 = 0.0
    for n in range(1, max(ns) + 1):
        Pn = Pn @ P
        if n not in ns:
            continue
        S2n = (mu_e[1:] ** (2 * n)).sum() + (mu_o ** (2 * n)).sum()
        Ichi = (pi[:, None] * Pn ** 2 / pi[None, :]).sum() - 1.0
        c1 = max(c1, abs(Ichi - S2n) / S2n)
        Sm = (mu_o ** (2 * n)).sum()
        dist = 0.25 * (pi[:, None] * (Pn - Pn[J, :]) ** 2 / pi[None, :]).sum()
        c2 = max(c2, abs(dist - Sm) / Sm)
        Sn = (mu_e[1:] ** n).sum() + (mu_o ** n).sum()
        q = np.concatenate([mu_e, mu_o]) ** n / (1 + Sn)
        H2 = -np.log((q ** 2).sum())
        c3 = max(c3, abs((2 * F(n) - F(2 * n)) - H2) / H2,
                 abs(np.log1p(Sn) + np.log(q.max())))
    res.update(C1=c1, C2=c2, C3=c3)
    mum = mu_o[0]
    etas = {}
    Pt = np.eye(len(Om))
    for t in range(1, max(ts) + 1):
        Pt = Pt @ P
        if t in ts:
            tv = 0.5 * np.abs(Pt - Pt[J, :]).sum(axis=1).max()
            etas[t] = (float(tv), float(mum ** t))
    res['mu_minus'] = float(mum)
    res['mu_1'] = float(max(mu_e[1], mu_o[0]))
    res['eta'] = etas
    res['C5'] = all(v[1] <= v[0] * (1 + 1e-10) for v in etas.values())
    return res


def spectrum(w, K):
    T, _ = transfer(w, K)
    lam = np.sort(np.linalg.eigvalsh(T))[::-1]
    assert lam[-1] > 0
    return lam


def torus_F(w, n, K):
    lam = spectrum(w, K)
    return n * np.log(lam[0]) + np.log(((lam / lam[0]) ** n).sum())


def lemma_zpp(K, T0, rho):
    b = rho * T0
    Phi = rho ** 2 * torus_F(T0, T0, K) - torus_F(b, b, K)
    lam = spectrum(b, K)                         # cross-section b, time T0
    g = np.log1p(((lam[1:] / lam[0]) ** T0).sum())
    return g, Phi / (rho - 1), 2 * Phi / rho


def identity_L_t(w, a, t, K):
    """p(a) = Tr(P_- T^a)/Tr T^a vs (1/2) E_w|1 - A^(t)(u,Jv)/A^(t)(u,v)|."""
    T, J = transfer(w, K)
    le, ve, lo, vo = parity_blocks(T, J)
    l0 = le[0]
    Za = ((le / l0) ** a).sum() + ((lo / l0) ** a).sum()
    p = ((lo / l0) ** a).sum() / Za
    lam = np.concatenate([le, lo]) / l0
    vec = np.concatenate([ve, vo], axis=1)
    At = (vec * lam ** t) @ vec.T
    Ar = (vec * lam ** (a - t)) @ vec.T
    wgt = Ar.T * At                  # weight of (u, v): A^(a-t)(v,u) A^(t)(u,v)
    ratio = At[:, J] / At            # A^(t)(u, Jv)/A^(t)(u, v)
    rhs = 0.5 * (wgt * np.abs(1 - ratio)).sum() / wgt.sum()
    exact = 0.5 * (1 - (wgt * ratio).sum() / wgt.sum())
    kappa = 0.5 * np.abs(1 - ratio).max()
    return float(p), float(exact), float(rhs), float(kappa)


def main():
    out = []

    def pr(*a):
        line = ' '.join(str(x) for x in a)
        print(line)
        out.append(line)

    Kc = 0.5 * np.log(1 + np.sqrt(2))
    pr('# Identities C1-C3 and Prop TB (C5), 2D Ising, J = global flip')
    for K in (0.3, Kc, 0.6):
        for w in (4, 6, 8, 10):
            r = analyse(w, K)
            pr(f"K={K:.4f} w={w:2d} rowsum_err={r['rowsum_err']:.1e} "
               f"C1={r['C1']:.1e} C2={r['C2']:.1e} C3={r['C3']:.1e} "
               f"mu1={r['mu_1']:.4f} mu-={r['mu_minus']:.4f} C5={r['C5']} "
               + ' '.join(f"eta{t}={v[0]:.4f}(mu-^t={v[1]:.4f})"
                          for t, v in r['eta'].items()))
    pr("# C4: 2D Lemma Z'' vs Lemma Z': g <= Phi/(rho-1) vs (2/rho)Phi")
    for K in (0.3, 0.4, Kc):
        for (T0, rho) in ((3, 2), (4, 2), (5, 2), (3, 3)):
            g, zpp, zp = lemma_zpp(K, T0, rho)
            pr(f"K={K:.4f} T0={T0} rho={rho} g={g:.6e} Z''={zpp:.6e} "
               f"Z'={zp:.6e} holds={bool(g <= zpp * (1 + 1e-12))}")
    pr('# C6: t-layer Identity L: p(a) == identity, p <= (1/2)E|1-ratio|')
    for K in (0.3, 0.6):
        for (w, a, t) in ((6, 6, 1), (6, 6, 3), (8, 8, 1), (8, 8, 4)):
            p, ex, rhs, kap = identity_L_t(w, a, t, K)
            ok = abs(p - ex) < 1e-10 * max(1, p) and p <= rhs * (1 + 1e-12)
            pr(f"K={K} w={w} a={a} t={t} p={p:.6e} identity={ex:.6e} "
               f"bound={rhs:.6e} kappa_t={kap:.3e} ok={bool(ok)}")
    pr('# Prop K: two-state chain with a rare slow mode')
    for eps in (1e-3, 1e-6):
        dlt, n = 0.01, 10
        muK = 1 - dlt / (1 - eps)
        S2n = muK ** (2 * n)
        hb = -(eps * np.log(eps) + (1 - eps) * np.log(1 - eps))
        pr(f"eps={eps:g} delta={dlt} n={n}: S(2n)={S2n:.4f}  I_KL <= H(X0)={hb:.3e}")
    pr('# Prop Q: tree-SDPI arithmetic against lattice order')
    bc2 = 0.5 * np.log(1 + np.sqrt(2))
    lam = np.tanh(0.5)
    pr(f"2D: beta_c={bc2:.5f} tanh(beta_c)={np.tanh(bc2):.5f}; beta=0.5: "
       f"lambda={lam:.5f} 4lambda^2={4*lam**2:.4f} 3lambda^2={3*lam**2:.4f}")
    G3, err = integrate.quad(lambda t: special.ive(0, 2 * t) ** 3, 0, np.inf,
                             limit=400)
    for b3 in (0.26, 0.35):
        lam3 = np.tanh(b3)
        m2 = 1 - G3 / b3
        pr(f"3D: G_3={G3:.6f} (quad err {err:.1e}); beta={b3} > G_3: "
           f"m^2 >= {m2:.4f}, odd weight >= m^4/4 = {m2**2/4:.4e} "
           f"(1/5041 = {1/5041:.4e}); lambda={lam3:.5f} "
           f"6lambda^2={6*lam3**2:.4f} 5lambda^2={5*lam3**2:.4f}")
    pr('# Prop TB2: O(N) layer at the flat background, FSS threshold N*G_3')
    for N, name in ((4, 'O(4) = SU(2) layer'), (2, 'O(2) = U(1) layer')):
        thr = N * G3
        line = f"{name}: N*G_3={thr:.5f};"
        for beta in (1.5, 2.3, 2.6):
            m2 = 1 - thr / beta
            if m2 > 0:
                line += (f" beta={beta}: m^2>={m2:.4f}, 1-Z_anti/Z_per >= "
                         f"m^4/(2N^2)={m2**2/(2*N*N):.4e};")
        pr(line)
    for b in (4, 6, 9, 16):
        s = sum(1 / np.sin(np.pi * k / b) ** 2 for k in range(1, b))
        pr(f"csc^2 sum b={b}: {s:.6f} vs (b^2-1)/3={(b*b-1)/3:.6f}")
    with open(sys.argv[1], 'w') as fh:
        fh.write('\n'.join(out) + '\n')


if __name__ == '__main__':
    main()
