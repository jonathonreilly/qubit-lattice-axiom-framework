#!/usr/bin/env python3
"""(LIFT-I) of `library/sector-values.md` in the abelian sector: the gradient energy of the lift falls by L^-2 in d = 4, with an absolute constant, and the comb has no effect. Consumer: the value clause (VAL_k), whose geometric sum over levels rests on this fall.

Written before running. An energy bound alone would not give a geometric sum: the lift of a parent with gradient energy e has a response with energy of order e, with no gain in L. The gain needs an H^2 bound. For the abelian part the note has an exact route. The minimiser has d^* F = Q^* lambda; by gauge invariance lambda is conserved at the parent level; on a conserved lambda the contour parts of Q^* cancel exactly, leaving the line part, of size L^-3 per fine bond; and on the torus ||grad F||^2 = ||d^* F||^2 since dF = 0. So sum over a parent cell of |grad F|^2 = ||Q_line^* lambda||^2.

Model: abelian, d dimensions, odd L, block side L_eff = L^n for a composite of n levels, whose line averages compose to one line average of side L^n. Bloch momentum P at the parent level, fine momenta k = (P + 2 pi l)/L^n. Dual energy, on lambda conserved, that is transverse to P-hat: G_{mu mu}(P) := sum_k q_mu(k)^2 / |k-hat|^2, diagonal, with q_mu(k) = (-1)^{l_mu} L^n D(k_mu) prod_nu D(k_nu), D the Dirichlet kernel. For a parent mode A' transverse to P-hat: lambda = the transverse inverse of G on A', fine field A_mu(k) = q_mu(k) lambda_mu / |k-hat|^2, level-(n-1) field a by the composite of the first n - 1 levels, F_j := kappa-hat wedge a. With F' := P-hat wedge A':

  rho := sum over the L^d level-(n-1) cells of a parent of |grad F_j|^2, divided by |P-hat|^2 |F'|^2,
  C(d, L, n) := L^(6-d) sup_P sup_A' rho,
  R(d, L, n) := sup_P sup_A' sum over the cells of | F_j - F'/L^2 e^{i kappa_0 x} |^2 / ( L^(d-4) |P-hat|^2 |F'|^2 ).

PRE-STATED criteria.
 L0. Controls in position space, d = 2, L = 3, 5, by a saddle solve on a torus of 8 parents. (a) The minimiser's plaquette angles with the comb constraint equal those with the line-only constraint, to 1e-7. (b) The ratio ||grad F||^2 / ||grad' F'||^2 of a real mode agrees with the Fourier formula, to 1e-6.
 L1. Normalisation: at the smallest P of the grid, the energy of F_j per parent over |F'|^2 is L^(d-4) within 2 percent.
 L2. d = 4: C(4, 11, 1) <= 1.15 C(4, 7, 1), C(4, 3, 3) <= 1.15 C(4, 3, 2), and C(4, 5, 2) <= 1.15 C(4, 5, 1), and every C at most 30. A failure means the fall is not L^-2 with an absolute constant, so the geometric sum needs another reading.
 L3. d = 4: R(4, 11, 1) <= 1.15 R(4, 7, 1), and every R at most 30: the response has energy at most an absolute constant times the parent's gradient energy, which the local form of the bound reads.
FAIL if any of these fails.

Limits. Abelian only: the comb's non-abelian residual is bounded by a count, (AD) of `library/composite-adjoint.md`, not tested here. A grid of momenta, each direction from 0, pi/8, pi/4, pi/2, 3 pi/4, pi, up to permutations of axes. RSS guard 2 GB.
"""
import itertools
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


def dirichlet(k, B):
    s = np.sin(k / 2)
    small = np.abs(s) < 1e-12
    out = np.empty_like(k)
    out[~small] = np.sin(B * k[~small] / 2) / (B * s[~small])
    # k = 2 pi m with B odd: the limit is +1 or -1, with the sign of the exact sum.
    out[small] = np.cos(B * k[small] / 2) / np.cos(k[small] / 2)
    return out


def aliases(P, B, d):
    """Momenta over P at block side B: k has shape (B^d, d), and signs (-1)^l."""
    grids = np.meshgrid(*[np.arange(B)] * d, indexing="ij")
    ls = np.stack([g.ravel() for g in grids], axis=-1)
    k = (np.asarray(P)[None, :] + 2 * np.pi * ls) / B
    return k, 1.0 - 2.0 * (ls % 2)


def qvec(P, B, d):
    k, sg = aliases(P, B, d)
    D = dirichlet(k, B)
    prod = np.prod(D, axis=1, keepdims=True)
    return k, sg * B * D * prod


def wedge2(khat, a):
    """|khat wedge a|^2 for arrays khat (.., d), a (.., d)."""
    return np.sum(khat**2, axis=-1) * np.sum(np.abs(a) ** 2, axis=-1) - np.abs(np.sum(khat * a, axis=-1)) ** 2


def mode(P, L, n, d):
    """Returns (rho_max, resp_max, energy ratio at the top eigenvector) for parent momentum P."""
    Pv = np.asarray(P, float)
    Phat = 2 * np.sin(Pv / 2)
    P2 = float(np.sum(Phat**2))
    B = L**n
    k, q = qvec(Pv, B, d)
    khat = 2 * np.sin(k / 2)
    k2 = np.sum(khat**2, axis=1)
    # On a conserved lambda, A(k) = q(k) lambda / |k-hat|^2 componentwise, so the dual energy is diagonal there.
    G = np.diag(np.sum(q * q / k2[:, None], axis=0))
    u = Phat / P2**0.5
    Perp = np.linalg.svd(np.eye(d) - np.outer(u, u))[0][:, : d - 1]
    Ginv = Perp @ np.linalg.inv(Perp.T @ G @ Perp) @ Perp.T
    # g(kappa_m) in lambda: for n = 1, the fine field itself.
    B1 = L ** (n - 1)
    grids = np.meshgrid(*[np.arange(L)] * d, indexing="ij")
    ms = np.stack([g.ravel() for g in grids], axis=-1)
    kappas = (Pv[None, :] + 2 * np.pi * ms) / L
    ghat = np.zeros((len(kappas), d, d))
    if B1 == 1:
        # At n = 1 the aliases k are the kappas; both come from the same meshgrid, so the order matches.
        ghat = np.einsum("mi,ij->mij", q / k2[:, None], np.eye(d))
    else:
        for m, ka in enumerate(kappas):
            kf, q1 = qvec(ka, B1, d)
            # The composite q of side B at kf.
            lk = np.rint((kf * B - Pv[None, :]) / (2 * np.pi)).astype(np.int64)
            sg = 1.0 - 2.0 * (lk % 2)
            Df = dirichlet(kf, B)
            qf = sg * B * Df * np.prod(Df, axis=1, keepdims=True)
            kh = 2 * np.sin(kf / 2)
            kk = np.sum(kh**2, axis=1)
            ghat[m] = np.diag(np.sum(q1 * qf / kk[:, None], axis=0))
        guard()
    ka_hat = 2 * np.sin(kappas / 2)
    ka2 = np.sum(ka_hat**2, axis=1)
    # Wedge forms T (gradient) and E (energy) on lambda.
    Sdot = np.einsum("mi,mij->mj", ka_hat, ghat)
    Fform = ka2[:, None, None] * np.einsum("mij,mik->mjk", ghat, ghat) - np.einsum("mj,mk->mjk", Sdot, Sdot)
    T = L**d * np.einsum("m,mjk->jk", ka2, Fform)
    E = L**d * np.sum(Fform, axis=0)
    # In A': N_T := Ginv T Ginv, on the transverse space.
    NT = Perp.T @ Ginv @ T @ Ginv @ Perp
    evals, evecs = np.linalg.eigh(0.5 * (NT + NT.T))
    rho = float(evals[-1]) / (P2 * P2)
    # The response: remove F'/L^2 from alias m = 0, with the same phases. F' := Phat wedge A', and F_j(kappa_0) in terms of A'.
    # Index of m = 0 is 0 in the meshgrid.
    # The response form on A' in the transverse basis, by forming each basis image.
    basis = np.eye(d - 1)
    images = []
    for b in basis:
        Ap = Perp @ b
        lam = Ginv @ Ap
        a_m = ghat @ lam
        F2_all = np.einsum("mi,mj->mij", ka_hat, a_m) - np.einsum("mi,mj->mji", ka_hat, a_m)
        Fp = np.outer(Phat, Ap) - np.outer(Ap, Phat)
        F2_all[0] -= Fp / L**2
        images.append(F2_all)
    images = np.stack(images, axis=1)  # (m, b, d, d)
    Rform = 0.5 * L**d * np.einsum("mbij,mcij->bc", images, images)
    Rvals = np.linalg.eigvalsh(0.5 * (Rform + Rform.T))
    # The denominator is P2 |F'|^2 = P2 * P2 |A'|^2 for A' transverse, in |F'|^2 := sum_{mu < nu} F_{mu nu}^2.
    resp = float(Rvals[-1]) / (P2 * P2)
    NE = Perp.T @ Ginv @ E @ Ginv @ Perp
    ener = float(np.linalg.eigvalsh(0.5 * (NE + NE.T))[-1]) / P2
    return rho, resp, ener


def grid(d):
    vals = [0.0, np.pi / 8, np.pi / 4, np.pi / 2, 3 * np.pi / 4, np.pi]
    out = []
    for t in itertools.combinations_with_replacement(vals, d):
        if max(t) > 0:
            out.append(t)
    return out


def scan(d, L, n):
    rho, resp = 0.0, 0.0
    where = None
    for P in grid(d):
        r, s, _ = mode(P, L, n, d)
        if r > rho:
            rho, where = r, P
        resp = max(resp, s)
    C = L ** (6 - d) * rho
    R = resp / L ** (d - 4)
    print(f" d={d} L={L} n={n}: C={C:.4f} at P/pi={tuple(round(x / np.pi, 3) for x in where)}, R={R:.4f}, rss={rss_gb():.2f}GB", flush=True)
    return C, R


def position_controls():
    ok = True
    for L in (3, 5):
        h = (L - 1) // 2
        Nc = 8
        N = Nc * L
        nl = 2 * N * N
        link = lambda x, y, m: m * N * N + (x % N) * N + (y % N)
        # Plaquettes.
        D = np.zeros((N * N, nl))
        for x in range(N):
            for y in range(N):
                k = x * N + y
                D[k, link(x, y, 0)] += 1
                D[k, link(x + 1, y, 1)] += 1
                D[k, link(x, y + 1, 0)] -= 1
                D[k, link(x, y, 1)] -= 1

        def contour(cx, cy, ox, oy):
            out = []
            x, y = cx, cy
            for _ in range(abs(ox)):
                if ox > 0:
                    out.append((link(x, y, 0), 1.0))
                    x += 1
                else:
                    x -= 1
                    out.append((link(x, y, 0), -1.0))
            for _ in range(abs(oy)):
                if oy > 0:
                    out.append((link(x, y, 1), 1.0))
                    y += 1
                else:
                    y -= 1
                    out.append((link(x, y, 1), -1.0))
            return out

        def constraints(comb):
            Q = np.zeros((2 * Nc * Nc, nl))
            r = 0
            for m in range(2):
                for a in range(Nc):
                    for b in range(Nc):
                        c = (L * a + h, L * b + h)
                        for ox in range(-h, h + 1):
                            for oy in range(-h, h + 1):
                                x, y = c[0] + ox, c[1] + oy
                                z = [x, y]
                                for _ in range(L):
                                    Q[r, link(z[0], z[1], m)] += 1.0 / L**2
                                    z[m] += 1
                                if comb:
                                    for bd, s in contour(c[0], c[1], ox, oy):
                                        Q[r, bd] += s / L**2
                                    cp = list(c)
                                    cp[m] += L
                                    for bd, s in contour(cp[0], cp[1], ox, oy):
                                        Q[r, bd] -= s / L**2
                        r += 1
            return Q

        Pint = (1, 2)
        P = (2 * np.pi * Pint[0] / Nc, 2 * np.pi * Pint[1] / Nc)
        Phat = np.array([2 * np.sin(P[0] / 2), 2 * np.sin(P[1] / 2)])
        perp = np.array([-Phat[1], Phat[0]])
        Ap = np.zeros(2 * Nc * Nc)
        r = 0
        for m in range(2):
            for a in range(Nc):
                for b in range(Nc):
                    mid = (a + 0.5 * (m == 0), b + 0.5 * (m == 1))
                    Ap[r] = perp[m] * np.cos(P[0] * mid[0] + P[1] * mid[1])
                    r += 1
        sols = {}
        for comb in (False, True):
            Q = constraints(comb)
            K = np.block([[D.T @ D + 1e-10 * np.eye(nl), Q.T], [Q, -1e-10 * np.eye(Q.shape[0])]])
            s = np.linalg.solve(K, np.concatenate([np.zeros(nl), Ap]))
            F = D @ s[:nl]
            sols[comb] = (F, float(np.max(np.abs(Q @ s[:nl] - Ap))))
        dF = float(np.max(np.abs(sols[True][0] - sols[False][0])))
        a = dF <= 1e-7 and sols[True][1] <= 1e-6 and sols[False][1] <= 1e-6
        F = sols[False][0].reshape(N, N)
        grad = float(np.sum((np.roll(F, -1, axis=0) - F) ** 2) + np.sum((np.roll(F, -1, axis=1) - F) ** 2))
        # Parent side: F' is the curl of Ap on the parent torus.
        Apx = Ap[: Nc * Nc].reshape(Nc, Nc)
        Apy = Ap[Nc * Nc :].reshape(Nc, Nc)
        Fp = Apx + np.roll(Apy, -1, axis=0) - np.roll(Apx, -1, axis=1) - Apy
        gradp = float(np.sum((np.roll(Fp, -1, axis=0) - Fp) ** 2) + np.sum((np.roll(Fp, -1, axis=1) - Fp) ** 2))
        direct = grad / gradp
        four = mode(P, L, 1, 2)[0]
        b = abs(direct / four - 1) <= 1e-6
        ok = ok and a and b
        print(f" L0 L={L}: comb against line-only, max difference in plaquette angles {dF:.1e}, constraint residuals {sols[True][1]:.1e} {sols[False][1]:.1e}: {a}; direct ratio {direct:.8f}, Fourier {four:.8f}: {b}", flush=True)
        guard()
    return ok


def main():
    ok = position_controls()
    print("L1", flush=True)
    for d, L in ((2, 5), (3, 5), (4, 3), (4, 5)):
        P = tuple([1e-3] + [0.0] * (d - 1))
        _, _, e = mode(P, L, 1, d)
        good = abs(e / L ** (d - 4) - 1) <= 0.02
        ok = ok and good
        print(f" d={d} L={L}: energy per parent over |F'|^2 {e:.5f}, expected {L ** (d - 4):.5f}: {good}", flush=True)
    print("Reported, d = 2, 3", flush=True)
    for d, L in ((2, 3), (2, 5), (2, 9), (2, 17), (2, 33), (3, 3), (3, 5), (3, 9), (3, 17)):
        scan(d, L, 1)
    print("L2, L3: d = 4", flush=True)
    res = {}
    for L, n in ((3, 1), (5, 1), (7, 1), (9, 1), (11, 1), (3, 2), (5, 2), (3, 3)):
        res[(L, n)] = scan(4, L, n)
        guard()
    C = {k: v[0] for k, v in res.items()}
    R = {k: v[1] for k, v in res.items()}
    l2 = C[(11, 1)] <= 1.15 * C[(7, 1)] and C[(3, 3)] <= 1.15 * C[(3, 2)] and C[(5, 2)] <= 1.15 * C[(5, 1)] and max(C.values()) <= 30
    l3 = R[(11, 1)] <= 1.15 * R[(7, 1)] and max(R.values()) <= 30
    ok = ok and l2 and l3
    print(f" L2 {l2}; L3 {l3}", flush=True)
    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
