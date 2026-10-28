"""Check x4: the free Gaussian soft chain (EXISTENCE §14). Criteria: checks/x4_criteria.md (written first).

d = 4, L = 3, one real abelian component. Everything exact (finite sums / exact linear maps), no sampling except the
seeded random test fields of part A.
"""
import itertools
import math
import numpy as np

L = 3
D = 4
O = (L - 1) // 2
TOL = 1e-12
out = []


def say(s):
    out.append(s)
    print(s)


def e(mu):
    v = [0] * D
    v[mu] = 1
    return v


# ---------------------------------------------------------------- A: one-step identity, literal S4' contours
def part_a():
    Tf, Tc = 9, 3
    rng = np.random.default_rng(20261027)
    perms = list(itertools.permutations(range(D)))
    offs = list(itertools.product(range(-O, O + 1), repeat=D))

    def lin(A, z, a, sgn):
        """signed value of A on the unit step from z in direction sgn*e_a (returns value, end point)"""
        z = list(z)
        if sgn > 0:
            v = A[a][tuple(c % Tf for c in z)]
            z[a] += 1
        else:
            z[a] -= 1
            v = -A[a][tuple(c % Tf for c in z)]
        return v, z

    def axial(A, start, u, sig):
        z, tot = list(start), 0.0
        for a in sig:
            for _ in range(abs(u[a])):
                v, z = lin(A, z, a, 1 if u[a] > 0 else -1)
                tot += v
        return tot, z

    def q_root_literal(A):
        Q = np.zeros((D, Tc, Tc, Tc, Tc))
        for X in itertools.product(range(Tc), repeat=D):
            cX = [L * x + O for x in X]
            for mu in range(D):
                cY = list(cX)
                cY[mu] += L
                acc = 0.0
                for sig in perms:
                    for u in offs:
                        t1, y = axial(A, cX, u, sig)            # c_X -> y
                        t2 = 0.0
                        z = list(y)
                        for _ in range(L):                       # straight leg y -> y + L e_mu
                            v, z = lin(A, z, mu, 1)
                            t2 += v
                        t3, w = axial(A, cY, u, sig)            # c_Y -> y + L e_mu, traversed backwards
                        assert [a % Tf for a in w] == [a % Tf for a in z]
                        acc += t1 + t2 - t3
                Q[(mu,) + X] = acc / (len(perms) * len(offs))
        return Q

    def q_str(A, Tc_):
        Q = np.zeros((D,) + (Tc_,) * D)
        for mu in range(D):
            S = sum(np.roll(A[mu], -j, axis=mu) for j in range(L))
            for a in range(D):
                S = sum(np.roll(S, -k, axis=a) for k in range(L))
            Q[mu] = S[tuple(slice(0, None, L) for _ in range(D))] / L ** D
        return Q

    def h_lit(A):
        H = np.zeros((Tc,) * D)
        for X in itertools.product(range(Tc), repeat=D):
            cX = [L * x + O for x in X]
            H[X] = np.mean([axial(A, cX, u, sig)[0] for sig in perms for u in offs])
        return H

    def dform0(H):
        return np.array([np.roll(H, -1, axis=mu) - H for mu in range(D)])

    def curv(B):
        return np.array([np.roll(B[n], -1, axis=m) - B[n] - np.roll(B[m], -1, axis=n) + B[m]
                         for m in range(D) for n in range(m + 1, D)])

    worst1 = worst2 = 0.0
    for t in range(3):
        A = rng.standard_normal((D, Tf, Tf, Tf, Tf))
        Qr = q_root_literal(A)
        Qs = q_str(A, Tc)
        H = h_lit(A)
        worst1 = max(worst1, np.abs(Qr - (Qs - dform0(H))).max())
        worst2 = max(worst2, np.abs(curv(Qr) - curv(Qs)).max())
    say(f"A1 max|Q_root - (Q_str - dh)| = {worst1:.2e}   A1' max|dQ_root - dQ_str| = {worst2:.2e}")
    passA = worst1 <= TOL and worst2 <= TOL
    # A2: coefficient vector of h at one site
    coef = {}
    for sig in perms:
        for u in offs:
            z = [O] * D
            for a in sig:
                for _ in range(abs(u[a])):
                    if u[a] > 0:
                        key = (a, tuple(z)); z[a] += 1; s = 1
                    else:
                        z[a] -= 1; key = (a, tuple(z)); s = -1
                    coef[key] = coef.get(key, 0.0) + s / (len(perms) * len(offs))
    c2 = sum(v * v for v in coef.values())
    say(f"A2 Var(h xi)/sigma^2 = ||c||^2 = {c2:.6f}  (gauge-variant; informational)")
    say(f"A: {'PASS' if passA else 'FAIL'}")
    return passA, q_str


# ---------------------------------------------------------------- B: plaquette / link noise variance
def closed_plaq(s):
    return 4.0 / 3.0 * (2.0 / s ** 2 + 1.0 / s ** 4)


def closed_link(s):
    return (2.0 / s ** 2 + 1.0 / s ** 4) / 3.0


def part_b():
    ok = True
    # B1: position space, iterated one-step adjoint of Q_str
    def q_str_adj(c):
        Tc_ = c.shape[1]
        Tf_ = L * Tc_
        Afine = np.zeros((D,) + (Tf_,) * D)
        for mu in range(D):
            E = np.zeros((Tf_,) * D)
            E[tuple(slice(0, None, L) for _ in range(D))] = c[mu] / L ** D
            for a in range(D):
                E = sum(np.roll(E, k, axis=a) for k in range(L))
            Afine[mu] = sum(np.roll(E, j, axis=mu) for j in range(L))
        return Afine

    Tc = 3
    for n in (1, 2):
        s = L ** n
        # plaquette (0,1) at X = 0: F = A_1(X+e0) - A_1(X) - A_0(X+e1) + A_0(X)
        c = np.zeros((D,) + (Tc,) * D)
        c[(1, 1, 0, 0, 0)] += 1; c[(1, 0, 0, 0, 0)] -= 1; c[(0, 0, 1, 0, 0)] -= 1; c[(0, 0, 0, 0, 0)] += 1
        cl = np.zeros((D,) + (Tc,) * D)
        cl[(0, 0, 0, 0, 0)] = 1.0
        w, wl = c, cl
        for _ in range(n):
            w, wl = q_str_adj(w), q_str_adj(wl)
        vp, vl = float((w ** 2).sum()), float((wl ** 2).sum())
        rp, rl = abs(vp / closed_plaq(s) - 1), abs(vl / closed_link(s) - 1)
        ok &= rp <= 1e-10 and rl <= 1e-10
        say(f"B1 n={n}: plaq var {vp:.12e} (closed {closed_plaq(s):.12e}, rel {rp:.1e}); "
            f"link var {vl:.12e} (rel {rl:.1e})")
    # B2: exact finite Fourier alias sums, coarse torus side 4
    Tc = 4
    P = 2 * np.pi * np.arange(Tc) / Tc
    b2vals = [4.0]  # n = 0: four independent unit links
    for n in range(1, 9):
        s = L ** n
        a = np.arange(s)
        q = (P[:, None] + 2 * np.pi * a[None, :]) / s                 # (Tc, s)
        Ds = np.where(np.abs(np.exp(1j * q) - 1) < 1e-15, 1.0 + 0j,
                      (np.exp(1j * q * s) - 1) / (s * (np.exp(1j * q) - 1)))
        A2 = (np.abs(Ds) ** 2).sum(axis=1)
        A4 = (np.abs(Ds) ** 4).sum(axis=1)
        nu2 = np.abs(np.exp(1j * P) - 1) ** 2
        link = A4.mean() / s ** 2 * A2.mean() ** 3
        # plaquette (mu,nu): avg_P [|nu_mu|^2 C_nunu + |nu_nu|^2 C_mumu]; C_lam(P) = s^-2 A4(P_lam) prod A2
        plaq = 2 * float((nu2[:, None] * A4[None, :]).mean()) / s ** 2 * A2.mean() ** 2
        b2vals.append(plaq)
        rp, rl = abs(plaq / closed_plaq(s) - 1), abs(link / closed_link(s) - 1)
        ok &= rp <= 1e-10 and rl <= 1e-10 and np.abs(A2 - 1).max() < 1e-12
        say(f"B2 n={n}: plaq {plaq:.12e} rel {rp:.1e}; link {link:.12e} rel {rl:.1e}; max|A2-1| {np.abs(A2-1).max():.1e}")
    say(f"B: {'PASS' if ok else 'FAIL'}")
    return ok, b2vals


# ---------------------------------------------------------------- C: symbol sup bounds
def part_c():
    ok = True
    Tc = 16
    P = 2 * np.pi * np.arange(Tc) / Tc
    pairs = [(m, n) for m in range(D) for n in range(m + 1, D)]
    for n in range(0, 7):
        s = L ** n
        if n == 0:
            A4 = np.ones(Tc)
        else:
            a = np.arange(s)
            q = (P[:, None] + 2 * np.pi * a[None, :]) / s
            Ds = np.where(np.abs(np.exp(1j * q) - 1) < 1e-15, 1.0 + 0j,
                          (np.exp(1j * q * s) - 1) / (s * (np.exp(1j * q) - 1)))
            A4 = (np.abs(Ds) ** 4).sum(axis=1)
        grids = np.meshgrid(*([np.arange(Tc)] * D), indexing="ij")
        idx = [g.ravel() for g in grids]
        C = np.stack([A4[idx[l]] / s ** 2 for l in range(D)], axis=1)          # (Npts, 4) link symbol
        nu = np.stack([np.exp(1j * P[idx[l]]) - 1 for l in range(D)], axis=1)
        M = np.zeros((C.shape[0], 6, D), complex)
        for k, (m_, n_) in enumerate(pairs):
            M[:, k, n_] = nu[:, m_]
            M[:, k, m_] = -nu[:, n_]
        Cov = np.einsum("pkl,pl,pjl->pkj", M, C, M.conj())
        lam = np.linalg.eigvalsh(Cov).max()
        lsup = C.max()
        ok &= lsup <= s ** -2 * (1 + 1e-12) and lam <= 16 * s ** -2 * (1 + 1e-12)
        say(f"C n={n}: s^2*sup link symbol = {lsup * s**2:.6f} (<= 1); s^2*sup curvature eig = {lam * s**2:.6f} (<= 16)")
    say(f"C: {'PASS' if ok else 'FAIL'}")
    return ok


# ---------------------------------------------------------------- D: chain sums at fixed resolution m
def part_d(bvals):
    b = 22.0 / (48 * math.pi ** 2)
    seqs = {"D1 const": lambda r: 1.0,
            "D2 (F)-type": lambda r: 1.0 / (1.0 + b * r * math.log(L))}
    verdict = "CONVERGES"
    for name, sig2 in seqs.items():
        for m in (0, 2, 5):
            NK, crude = [], []
            for K in range(m + 1, m + 61):
                terms = [sig2(m + 1 + n) * (bvals[n] if n < len(bvals) else closed_plaq(L ** n))
                         for n in range(K - m)]
                NK.append(sum(terms))
                crude.append(16 * sum(sig2(m + 1 + n) for n in range(K - m)))
            formula = 4 / 3 * sum(sig2(m + 1 + n) * (2 * L ** (-2 * n) + L ** (-4 * n)) for n in range(60))
            mono = all(NK[i + 1] >= NK[i] - 1e-15 for i in range(len(NK) - 1))
            d = NK[59] - NK[29]
            if not mono or d > 1e-12 * NK[59]:
                verdict = "DIVERGES" if d > 1e-6 * NK[59] else "UNDECIDED"
            say(f"{name} m={m}: N_K for K-m=1,2,5,30,60: {NK[0]:.6f} {NK[1]:.6f} {NK[4]:.6f} {NK[29]:.9f} "
                f"{NK[59]:.9f}; |indep - formula| {abs(NK[59]-formula):.1e}; N_60-N_30 {d:.1e}; "
                f"crude 16*sum at K-m=1,30,60: {crude[0]:.2f} {crude[29]:.2f} {crude[59]:.2f}")
    say(f"D: {verdict}")
    return verdict


if __name__ == "__main__":
    pa, _ = part_a()
    pb, bvals = part_b()  # bvals: Fourier-computed per-depth plaquette variances, n = 0..8 (independent of the formula)
    pc = part_c()
    vd = part_d(bvals)
    say(f"SUMMARY A={'PASS' if pa else 'FAIL'} B={'PASS' if pb else 'FAIL'} C={'PASS' if pc else 'FAIL'} D={vd}")
