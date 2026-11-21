#!/usr/bin/env python3
"""Fibre problem with a gauge term on ker r only. Consumer: `library/preconditioned-covariance.md`, the fast rate of M^-1 at a background.

Written before running. Fine bond field H, fine units (D = T - 1). r_U := covariant block average on sites, Q^o := Q - D' Phi, with Q^o D = D' r_U. P_r := 1 - r^* (r r^*)^-1 r.
 K# := d^dagger d + D P_r D^dagger,   Sad# := [[K#, Q^o*], [Q^o, 0]],   phi := D^dagger H.
The claim under test. (i) ||H||^2_Eps <= C# (||d H||^2 + ||P_r phi||^2) on ker Q^o, C# free of L, in level-1 units. (ii) Sad#^-1 solves the class problem: for a current J that vanishes on D omega with r omega = 0, the solution has P_r phi = 0 and it represents M^-1 J. (iii) It decays at a rate per box free of L.
Why K = -Delta (Theorem 6 of the energy package) is not enough: there the gauge term is ||D^dagger H||^2 in full. On ker Q^o only omega with r omega = 0 is left as gauge, so the part r D^dagger H cannot be gauged away, and the K solution is not the class solution. C0 below shows this.

PRE-STATED criteria.

Part A, real space, d = 2, constant flux, charged components, L = 3, 5, m = 0, 1, 2.
 A0. ||Q^o D omega - D' r omega|| <= 1e-10 ||omega||, random omega.
 A1. Source eta on free bonds, random and local to a box. xi_tree := M^-1 eta by the KKT system in tree gauge with the true constraint Q. xi_sharp := read from Sad#: build J#(H) := eta . xi(H), with xi(H) the tree-gauge free bonds of H~ := H - D chi, chi := the function with values Phi H at centres and 0 elsewhere (local); solve Sad# (H, lam) = (J#, 0); then xi_sharp := xi(H). Pass: ||xi_tree - xi_sharp|| <= 1e-7 ||xi_tree||.
 A2. On that solution ||P_r D^dagger H|| <= 1e-8 ||H||.
 FAIL if any of these fails: the identification of the two problems would be false.

Part B, trivial background, Bloch sum over coarse momentum p. d = 2: L = 3, 5, 7, 9, 11. d = 3: L = 3, 5, 7. d = 4: L = 3, 5.
 lam#(p) := min on ker Q^o(p) of L^2 (||d H||^2 + ||P_r phi||^2) / (L^2 (||d H||^2 + ||phi||^2) + ||H||^2).
 B1. For each d, min_p lam#(L) >= 0.5 min_p lam#(smallest L).
 B2. For each d and L, min_p lam# >= 0.02.
 FAIL if either fails: then (i) is false as stated.

Part C, trivial background, real-space profile by inverse Bloch sum, from the source J := d^dagger e_p at the centre of box 0.
 A(D) := sup of the l^2 norm of H on a box at sup-distance D from the source box; AF(D) the same for d H. rate := slope of -log A over the range where A > 1e-10 A(0), excluding D = 0 and the last D (the antipode).
 C0 (control). At p != 0, the solution of the K problem, with ||D^dagger H||^2 in full, has r phi != 0: the largest value of ||r phi|| / ||H||, in the same normalisation as (i), is above 1e-3. Failure would mean this new form was unneeded, which I would report; it does not fail the run.
 C1. rate >= 0.7 for each d, L.
 C2. rate(L) >= 0.5 rate(smallest L), each d.
 C3. d = 2: rate of AF at the largest L within 15 percent of arccosh 2 = 1.3170, the pole of the inverse Gram matrix of the plaquette weights tri x tri, measured from D = 2 to D = nc/2 - 1. This is a prediction made before the run.
 FAIL if C1, C2 or C3 fails.

Part D, real space at flux, d = 2, L = 3, nc = 12, m = 0, 1, 2, 4; L = 5, nc = 8, m = 0, 1, 2. Level-1 flux a' <= 0.2 for the criteria.
 D1. lam#(m) >= 0.5 lam#(0).
 D2. rate of H from S1 at flux >= 0.5 rate(m = 0).
FAIL if D1 or D2 fails.

Limitations: one level; constant flux for A, D; no Lagrange term; the form ||d H||^2 and not the full Hessian. RSS guard 2 GB.
"""
import importlib.util
import itertools
import os
import resource
import sys

import numpy as np


def rss_gb():
    r = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return r / 1024**3 if sys.platform == "darwin" else r / 1024**2


def guard():
    if rss_gb() > 2:
        raise SystemExit("RSS above 2 GB")


HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location("tp_flux", os.path.join(HERE, "hard-core--mapped_tp_flux.py"))
tp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tp)


# ------------------------------- Part A, D: real space at flux, d = 2 -------------------------------


def contour(g, y0, x):
    """Coefficients on bonds of the contour sum from y0 to x, and the transport."""
    (a, b), (c, d) = y0, x
    coef = {}
    om = 1.0 + 0j
    cur = [a, b]
    N = g.N
    for nu, target in ((0, c), (1, d)):
        step = 1 if target >= cur[nu] else -1
        while cur[nu] != target:
            if step > 0:
                s = (cur[0] % N, cur[1] % N)
                bd = g.idx(*s) + nu * N * N
                coef[bd] = coef.get(bd, 0) + om
                om = om * g.u[nu, s[0], s[1]]
            else:
                pr = list(cur)
                pr[nu] -= 1
                s = (pr[0] % N, pr[1] % N)
                bd = g.idx(*s) + nu * N * N
                om = om * np.conj(g.u[nu, s[0], s[1]])
                coef[bd] = coef.get(bd, 0) - om
            cur[nu] += step
    return om, coef


def build_sharp(L, nc, m):
    g, D, d, Q, Dc, ev = tp.build(L, nc, m)
    N, n = g.N, nc
    nb = 2 * N * N
    centres = [(g.h + L * i, g.h + L * j) for i in range(n) for j in range(n)]
    r = np.zeros((n * n, N * N), dtype=complex)
    Phi = np.zeros((n * n, nb), dtype=complex)
    h = g.h
    for ci, y0 in enumerate(centres):
        for r0 in range(-h, h + 1):
            for r1 in range(-h, h + 1):
                x = (y0[0] + r0, y0[1] + r1)
                om, coef = contour(g, y0, x)
                r[ci, g.idx(*x)] += om / L**2
                for b, v in coef.items():
                    Phi[ci, b] -= v / L**2
    Qo = Q - Dc @ Phi
    Pr = np.eye(N * N, dtype=complex) - r.conj().T @ np.linalg.solve(r @ r.conj().T, r)
    return g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres


def null_basis(C):
    _, s, vh = np.linalg.svd(C, full_matrices=True)
    rk = int(np.sum(s > 1e-10 * s[0]))
    return vh[rk:].conj().T


def lam_sharp_real(L, nc, m):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = build_sharp(L, nc, m)
    Z = null_basis(Qo)
    guard()
    dZ = d @ Z
    pZ = D.conj().T @ Z
    A = L**2 * (dZ.conj().T @ dZ + pZ.conj().T @ (Pr @ pZ))
    B = L**2 * (dZ.conj().T @ dZ + pZ.conj().T @ pZ) + np.eye(Z.shape[1])
    A, B = 0.5 * (A + A.conj().T), 0.5 * (B + B.conj().T)
    C = np.linalg.cholesky(B)
    Ci = np.linalg.inv(C)
    w = np.linalg.eigvalsh(Ci @ A @ Ci.conj().T)
    guard()
    return float(w[0])


def part_a(L, nc, m, rng):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = build_sharp(L, nc, m)
    N, n = g.N, nc
    nb = 2 * N * N
    om = rng.standard_normal(N**2) + 1j * rng.standard_normal(N**2)
    a0 = np.linalg.norm(Qo @ (D @ om) - Dc @ (r @ om)) / np.linalg.norm(om)
    tree = tp.comb_bonds(g)
    keep = np.setdiff1d(np.arange(nb), tree)
    # A local random source on free bonds of the box of (h, h).
    box = []
    kset = set(keep.tolist())
    for r0 in range(-g.h, g.h + 1):
        for r1 in range(-g.h, g.h + 1):
            for mu in range(2):
                b = g.idx(g.h + r0, g.h + r1) + mu * N * N
                if b in kset:
                    box.append(b)
    eta = np.zeros(nb, dtype=complex)
    eta[box] = rng.standard_normal(len(box)) + 1j * rng.standard_normal(len(box))
    # Tree-gauge KKT with the true Q.
    K = d.conj().T @ d
    Kff = K[np.ix_(keep, keep)]
    Qf = Q[:, keep]
    n1, m1 = Kff.shape[0], Qf.shape[0]
    S = np.zeros((n1 + m1, n1 + m1), dtype=complex)
    S[:n1, :n1] = Kff
    S[:n1, n1:] = Qf.conj().T
    S[n1:, :n1] = Qf
    rhs = np.concatenate([eta[keep], np.zeros(m1)])
    sol = np.linalg.lstsq(S, rhs, rcond=1e-12)[0]
    xi_tree = np.zeros(nb, dtype=complex)
    xi_tree[keep] = sol[:n1]
    guard()
    # The map H -> tree-gauge free bonds of H~. chi: values Phi H at centres, 0 elsewhere.
    # Gauge to tree: omega along the tree from the centre, by solving D omega = H~ on tree bonds with omega = 0 at centres.
    idx_c = [g.idx(*y) for y in centres]
    Dt = D[tree, :]
    free_sites = np.setdiff1d(np.arange(N * N), idx_c)
    Dts = Dt[:, free_sites]
    # Dts is square and invertible on the forest with roots at the centres.
    Gt = np.linalg.solve(Dts, np.eye(len(tree), dtype=complex))
    Om = np.zeros((N * N, len(tree)), dtype=complex)
    Om[free_sites, :] = Gt
    TreeProj = np.eye(nb, dtype=complex) - D @ Om[:, :] @ np.eye(nb, dtype=complex)[tree, :]
    # H~ := H - D chi[H], chi[H] := e_c^T Phi H, with Q H~ = 0 on ker Q^o.
    Chi = ev.conj().T @ Phi
    Tilde = np.eye(nb, dtype=complex) - D @ Chi
    Xi = TreeProj @ Tilde
    guard()
    # The current J#(H) = eta^dagger Xi H, in the convention <X, K Y>.
    J = Xi.conj().T @ eta
    Ks = K + D @ Pr @ D.conj().T
    S2 = np.zeros((nb + m1, nb + m1), dtype=complex)
    S2[:nb, :nb] = Ks
    S2[:nb, nb:] = Qo.conj().T
    S2[nb:, :nb] = Qo
    sol2 = np.linalg.lstsq(S2, np.concatenate([J, np.zeros(m1)]), rcond=1e-12)[0]
    H = sol2[:nb]
    xi_sharp = Xi @ H
    a1 = np.linalg.norm(xi_tree - xi_sharp) / np.linalg.norm(xi_tree)
    a2 = np.linalg.norm(Pr @ (D.conj().T @ H)) / np.linalg.norm(H)
    res2 = np.linalg.norm(Q @ (Tilde @ H)) / np.linalg.norm(H)
    guard()
    return a0, a1, a2, res2


def profile_real(L, nc, m):
    g, D, d, Q, Qo, Dc, ev, r, Phi, Pr, centres = build_sharp(L, nc, m)
    N, n = g.N, nc
    nb = 2 * N * N
    e_p = np.zeros(N * N, dtype=complex)
    e_p[g.idx(g.h, g.h)] = 1
    J = d.conj().T @ e_p
    K = d.conj().T @ d + D @ Pr @ D.conj().T
    m1 = Qo.shape[0]
    S = np.zeros((nb + m1, nb + m1), dtype=complex)
    S[:nb, :nb] = K
    S[:nb, nb:] = Qo.conj().T
    S[nb:, :nb] = Qo
    sol = np.linalg.solve(S, np.concatenate([J, np.zeros(m1)]))
    H = sol[:nb]
    a = np.arange(N)
    AA, BB = np.meshgrid(a, a, indexing="ij")
    boxes = np.stack([AA // L, BB // L], axis=-1).reshape(-1, 2)
    bb = np.vstack([boxes, boxes])
    idx = bb[:, 0] * nc + bb[:, 1]
    norms = np.bincount(idx, weights=np.abs(H) ** 2, minlength=nc * nc)
    bx = np.array(np.unravel_index(np.arange(nc * nc), (nc, nc))).T
    dd = np.minimum(bx, nc - bx).max(axis=1)
    prof = [float(np.sqrt(norms[dd == k].max())) for k in range(nc // 2 + 1)]
    guard()
    return prof


def rate_of(prof, lo=1):
    top = len(prof) - 1
    ds = [k for k in range(lo, top) if prof[k] > 1e-10 * prof[0]]
    if len(ds) < 2:
        return float("nan")
    return float(np.polyfit(ds, -np.log([prof[k] for k in ds]), 1)[0])


# ------------------------------- Part B, C: trivial background, any d -------------------------------


class Bloch:
    """Fine sites of a block, x in {0..L-1}^d, with block centre at index h in each direction. Bond fields: d L^d complex numbers."""

    def __init__(self, d, L):
        self.d, self.L, self.h = d, L, (L - 1) // 2
        self.V = L**d
        self.sites = list(itertools.product(range(L), repeat=d))
        self.index = {s: i for i, s in enumerate(self.sites)}
        self.nb = d * self.V
        self.pairs = list(itertools.combinations(range(d), 2))
        # Next-site table.
        self.next = np.zeros((d, self.V), dtype=int)
        self.wrap = np.zeros((d, self.V), dtype=int)
        for i, s in enumerate(self.sites):
            for mu in range(d):
                t = list(s)
                t[mu] += 1
                self.wrap[mu, i] = t[mu] // L
                t[mu] %= L
                self.next[mu, i] = self.index[tuple(t)]
    
    def T(self, mu, p):
        """(T_mu f)(x) = f(x + e_mu), on Bloch functions f(x) = exp(i p.x / L) f~(x)."""
        M = np.zeros((self.V, self.V), dtype=complex)
        ph = np.exp(1j * p[mu] / self.L)
        for i in range(self.V):
            M[i, self.next[mu, i]] = ph
        return M

    def ops(self, p):
        d, V = self.d, self.V
        Ts = [self.T(mu, p) for mu in range(d)]
        I = np.eye(V, dtype=complex)
        Dd = np.zeros((V, self.nb), dtype=complex)  # D^dagger: bond field to site function
        for mu in range(d):
            Dd[:, mu * V : (mu + 1) * V] = (Ts[mu] - I).conj().T
        dm = np.zeros((len(self.pairs) * V, self.nb), dtype=complex)
        for k, (mu, nu) in enumerate(self.pairs):
            dm[k * V : (k + 1) * V, nu * V : (nu + 1) * V] = Ts[mu] - I
            dm[k * V : (k + 1) * V, mu * V : (mu + 1) * V] = -(Ts[nu] - I)
        # r: a row. Bloch phase exp(i p . t / L), t the displacement from the block centre, within the block.
        r = np.zeros(V, dtype=complex)
        for i, s in enumerate(self.sites):
            t = np.array(s) - self.h
            r[i] = np.exp(1j * np.dot(p, t) / self.L) / V
        # Q^o: d rows. Q^o H (y, mu) = avg over x in B(y) of the sum along the line from x, s = 0..L-1, of H_mu(x + s e_mu).
        Qo = np.zeros((d, self.nb), dtype=complex)
        for mu in range(d):
            for i, s in enumerate(self.sites):
                base = np.array(s) - self.h
                for sft in range(self.L):
                    t = base.copy()
                    t[mu] += sft
                    fine = tuple((t + self.h) % self.L)
                    Qo[mu, mu * V + self.index[fine]] += np.exp(1j * np.dot(p, t) / self.L) / V
        return Dd, dm, r, Qo


def lam_sharp_bloch(B, p):
    L = B.L
    Dd, dm, r, Qo = B.ops(p)
    _, s, vh = np.linalg.svd(Qo, full_matrices=True)
    Z = vh[int(np.sum(s > 1e-12)) :].conj().T
    dZ = dm @ Z
    pZ = Dd @ Z
    dd = dZ.conj().T @ dZ
    pp = pZ.conj().T @ pZ
    # P_r = 1 - rn^* rn, rn := r / ||r||, a row, so <phi, P_r phi> = ||phi||^2 - |rn phi|^2.
    R = (r / np.linalg.norm(r))[None, :] @ pZ
    A = L**2 * (dd + pp - R.conj().T @ R)
    Bm = L**2 * (dd + pp) + np.eye(Z.shape[1])
    A, Bm = 0.5 * (A + A.conj().T), 0.5 * (Bm + Bm.conj().T)
    C = np.linalg.cholesky(Bm)
    Ci = np.linalg.inv(C)
    return float(np.linalg.eigvalsh(Ci @ A @ Ci.conj().T)[0])


def grid(d, n):
    """Momenta up to reflections and permutations. The symmetry is tested once, in main."""
    vals = sorted({round(abs(2 * np.pi * k / n - np.pi), 12) for k in range(n)})
    return [np.array(q) for q in itertools.combinations_with_replacement(vals, d)]


def part_b(d, L, n):
    B = Bloch(d, L)
    vals = []
    for p in grid(d, n):
        vals.append(lam_sharp_bloch(B, p))
        guard()
    # Also near p = 0.
    for sc in (1e-3, 1e-2):
        pp = np.zeros(d)
        pp[0] = sc
        vals.append(lam_sharp_bloch(B, pp))
        vals.append(lam_sharp_bloch(B, sc * np.ones(d)))
    return min(vals)


def phase_of(B, p):
    return np.array([np.exp(1j * np.dot(p, np.array(x)) / B.L) for x in B.sites])


def part_c(d, L, nc):
    """Real-space profile, source d^dagger e_p of a plaquette at the block centre, plane (0, 1)."""
    B = Bloch(d, L)
    V, nb = B.V, B.nb
    # Profile at block displacement R: H(R, x) = (1/nc^d) sum_p exp(i p.R) H~(p, x), with the Bloch phase exp(i p.x/L) included.
    shape = (nc,) * d + (nb,)
    Hp = np.zeros(shape, dtype=complex)
    Fp = np.zeros((nc,) * d + (len(B.pairs) * V,), dtype=complex)
    rmax = 0.0
    ix0 = B.index[tuple([B.h] * d)]
    for idx in itertools.product(range(nc), repeat=d):
        p = 2 * np.pi * np.array(idx) / nc
        Dd, dm, r, Qo = B.ops(p)
        ep = np.zeros(len(B.pairs) * V, dtype=complex)
        ep[ix0] = np.exp(-1j * np.dot(p, np.array([B.h] * d)) / L)
        J = dm.conj().T @ ep
        rn = r / np.linalg.norm(r)
        Pr = np.eye(V, dtype=complex) - rn.conj()[:, None] @ rn[None, :]
        K = dm.conj().T @ dm + Dd.conj().T @ Pr @ Dd
        S = np.zeros((nb + d, nb + d), dtype=complex)
        S[:nb, :nb] = K
        S[:nb, nb:] = Qo.conj().T
        S[nb:, :nb] = Qo
        sol = np.linalg.solve(S, np.concatenate([J, np.zeros(d)]))
        h = sol[:nb]
        # The Bloch phase exp(i p . x / L) of each fine site, so that the inverse sum gives the field at block displacement R.
        Hp[idx] = h * np.tile(phase_of(B, p), d)
        Fp[idx] = (dm @ h) * np.tile(phase_of(B, p), len(B.pairs))
        # Control C0: the K problem with ||D^dagger H||^2 in full.
        K0 = dm.conj().T @ dm + Dd.conj().T @ Dd
        S0 = S.copy()
        S0[:nb, :nb] = K0
        h0 = np.linalg.solve(S0, np.concatenate([J, np.zeros(d)]))[:nb]
        if np.linalg.norm(h0) > 1e-12:
            rmax = max(rmax, float(abs(r @ (Dd @ h0)) * B.V**0.5 * L / np.linalg.norm(h0)))
        guard()
    Hx = np.fft.ifftn(Hp, axes=tuple(range(d)))
    Fx = np.fft.ifftn(Fp, axes=tuple(range(d)))
    # np.fft.ifftn uses exp(+2 pi i k n / N): H at block displacement R.
    prof = np.zeros(nc // 2 + 1)
    profF = np.zeros(nc // 2 + 1)
    for idx in itertools.product(range(nc), repeat=d):
        D = max(min(i, nc - i) for i in idx)
        prof[D] = max(prof[D], np.linalg.norm(Hx[idx]))
        profF[D] = max(profF[D], np.linalg.norm(Fx[idx]))
    return prof.tolist(), profF.tolist(), rmax


def main():
    ok = True
    rng = np.random.default_rng(77)

    print("Part A", flush=True)
    for L, nc in ((3, 4), (5, 4)):
        for m in (0, 1, 2):
            a0, a1, a2, res2 = part_a(L, nc, m, rng)
            good = a0 <= 1e-10 and a1 <= 1e-7 and a2 <= 1e-8
            ok = ok and good
            print(f" A L={L} nc={nc} m={m}: A0={a0:.1e} A1={a1:.2e} A2={a2:.1e} Q on H~={res2:.1e}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("Part B", flush=True)
    B0 = Bloch(2, 3)
    sym = abs(lam_sharp_bloch(B0, np.array([0.7, 1.9])) - lam_sharp_bloch(B0, np.array([-1.9, 0.7])))
    ok = ok and sym <= 1e-9
    print(f" symmetry of the reduced grid, d=2, L=3: {sym:.1e}", flush=True)
    for d, Ls, n in ((2, (3, 5, 7, 9, 11), 17), (3, (3, 5, 7), 7), (4, (3, 5), 5)):
        base = None
        for L in Ls:
            v = part_b(d, L, n)
            if base is None:
                base = v
            good = v >= 0.5 * base and v >= 0.02
            ok = ok and good
            print(f" B d={d} L={L} grid={n}: min lam#={v:.4f} C#={1/v:.2f}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("Part C", flush=True)
    for d, Ls, nc in ((2, (3, 5, 7, 9, 11), 16), (3, (3, 5), 8), (4, (3,), 6)):
        base = None
        for L in Ls:
            prof, profF, rmax = part_c(d, L, nc)
            rt = rate_of(prof)
            rtF = rate_of(profF)
            if base is None:
                base = rt
            good = rt >= 0.7 and rt >= 0.5 * base
            ok = ok and good
            print(f" C d={d} L={L} nc={nc}: rate H={rt:.3f} rate F={rtF:.3f} C0 r phi={rmax:.2e} prof={[f'{v:.1e}' for v in prof]} F={[f'{v:.1e}' for v in profF]}: {good} rss={rss_gb():.2f}GB", flush=True)
            if d == 2 and L == Ls[-1]:
                rc3 = rate_of(profF, lo=2)
                c3 = abs(rc3 - 1.3170) <= 0.15 * 1.3170
                ok = ok and c3
                print(f"  C3 d=2 L={L}: rate F from D=2: {rc3:.3f} against 1.317: {c3}", flush=True)

    print("Part D", flush=True)
    for L, nc, ms in ((3, 12, (0, 1, 2, 4)), (5, 8, (0, 1, 2))):
        base = None
        base_r = None
        for m in ms:
            v = lam_sharp_real(L, nc, m)
            prof = profile_real(L, nc, m)
            rt = rate_of(prof)
            ap = L**2 * 2 * np.pi * m / (L * nc) ** 2
            if m == 0:
                base, base_r = v, rt
            good = True
            if ap <= 0.2:
                good = v >= 0.5 * base and rt >= 0.5 * base_r
            ok = ok and good
            print(f" D L={L} nc={nc} m={m} a'={ap:.3f}: lam#={v:.4f} rate={rt:.3f} prof={[f'{x:.1e}' for x in prof]}: {good} rss={rss_gb():.2f}GB", flush=True)

    print("PASS" if ok else "FAIL")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
