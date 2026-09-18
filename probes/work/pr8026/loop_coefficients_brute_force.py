#!/usr/bin/env python3
"""J:attack:PR8026 - spatial-loop area note (PR #8026), attack pattern (f) NORMALIZATION: the two stated open-geometry Taylor
coefficients of the real normalized loop trace in the supplied compact SU(3) Hamiltonian h(u) = a sum_e K_e + u V, u = av,
    omega_u(W_square) = u/144 + O(u^2),     omega_u(W_two-adjacent-faces) = (7/124416) u^2 + O(u^3),
with the intermediate values psi1 = S/96, I = int W_C S^2 = 2/9, <psi1, W_C psi1> = 1/41472 and 2Re<0, W_C psi2> = 1/31104, recomputed by
brute force in the actual Hilbert space of the smallest open graphs (one face: its 4 links; two adjacent faces: their 7 links), with
machinery disjoint from the note's hand algebra and its index checker:
  * the link Hilbert space in an explicit Peter-Weyl basis: SU(3) irreps (p, q) as traceless symmetric tensors, generators T_A =
    Gell-Mann/sqrt2 (Tr T_A T_B = delta_AB), link energy e(p,q) = (p^2 + pq + q^2 + 3p + 3q)/a (K_e = -3 Delta_e/(2a)), Clebsch-Gordan
    isometries for multiplication by a fundamental or antifundamental matrix entry (Casimir eigenspaces + intertwiner solve, checked on
    random SU(3) elements); gauge-invariant states only through the vacuum and gauge-invariant loop multiplications, so the three
    effective links (the two three-link arcs A, B and the shared link U; a single face uses A and U) carry kinetic weights 3, 1, 3;
  * the faces p = Tr(AU), q = Tr(U^dagger B) and the loop C = Tr(AB) act by exact multiplication through the CG isometries, with
    V_c = -(1/6) sum_f (chi_f + conj chi_f) (the centred perturbation; W = (chi + conj chi)/6 = ReTr/3);
  * route 1: Rayleigh-Schroedinger arrays psi1 = -R0 V_c 0, psi2 = -R0 V_c psi1 (R0 = Q h0^-1 Q exactly, block by block);
  * route 2: the ground state of the truncated h(u) (irreps p + q <= 2 per link, exact through second order) by Lanczos at small u,
    then Richardson extrapolation of omega/u and omega/u^2.
Supplement (INFO, pattern (a) witness): the order-0/1/2/3 centre-charge census for the six-link rectangle in the two-cube open graph
(12 vertices, 20 links, 11 faces), stated as 0/0/4 survivors at orders 0/1/2.
HIT if a brute-force coefficient differs from the stated rational beyond 1e-9 (route 1) or 1e-6 relative (route 2), or the census differs.
"""
import itertools
import math
import sys
import time
from fractions import Fraction as Fr

import numpy as np

rng = np.random.default_rng(8026)

# ---------------------------------------------------------------------------------------------------------------- SU(3) data
GM = [np.array(m, dtype=complex) for m in (
    [[0, 1, 0], [1, 0, 0], [0, 0, 0]], [[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], [[1, 0, 0], [0, -1, 0], [0, 0, 0]],
    [[0, 0, 1], [0, 0, 0], [1, 0, 0]], [[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], [[0, 0, 0], [0, 0, 1], [0, 1, 0]],
    [[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], [[1 / math.sqrt(3), 0, 0], [0, 1 / math.sqrt(3), 0], [0, 0, -2 / math.sqrt(3)]])]
T = [m / math.sqrt(2) for m in GM]


def c_lab(p, q):
    return p * p + p * q + q * q + 3 * p + 3 * q


def dim_lab(p, q):
    return (p + 1) * (q + 1) * (p + q + 2) // 2


def rand_su3():
    z = (rng.normal(size=(3, 3)) + 1j * rng.normal(size=(3, 3))) / math.sqrt(2)
    Q, Rm = np.linalg.qr(z)
    Q = Q * (np.diag(Rm) / np.abs(np.diag(Rm)))
    return Q / np.linalg.det(Q) ** (1 / 3)


def slot_op(X, slot, n):
    mats = [np.eye(3)] * n
    mats = list(mats)
    mats[slot] = X
    out = np.array([[1.0 + 0j]])
    for m in mats:
        out = np.kron(out, m)
    return out


class Irrep:
    def __init__(self, p, q):
        self.p, self.q = p, q
        n = p + q
        N = 3 ** n
        if n == 0:
            self.E = np.ones((1, 1), dtype=complex)
        else:
            # symmetrizer over the upper slots and over the lower slots
            S = np.zeros((N, N))
            perms = [(pu, pl) for pu in itertools.permutations(range(p)) for pl in itertools.permutations(range(p, n))]
            I = np.eye(N).reshape((N,) + (3,) * n)
            for pu, pl in perms:
                S += I.transpose((0,) + tuple(1 + x for x in pu + pl)).reshape(N, N)
            S /= len(perms)
            w, V = np.linalg.eigh(S)
            Bs = V[:, w > 0.5]
            # contractions of an upper slot with a lower slot must vanish
            rows = []
            for i in range(p):
                for j in range(p, n):
                    Cm = np.zeros((3 ** (n - 2), N))
                    for idx in itertools.product(range(3), repeat=n):
                        if idx[i] == idx[j]:
                            rest = tuple(x for s, x in enumerate(idx) if s not in (i, j))
                            r = int(np.ravel_multi_index(rest, (3,) * (n - 2))) if n > 2 else 0
                            Cm[r, int(np.ravel_multi_index(idx, (3,) * n))] += 1
                    rows.append(Cm)
            if rows:
                Cst = np.vstack(rows) @ Bs
                u, s, vh = np.linalg.svd(Cst)
                null = vh[np.sum(s > 1e-10):].conj().T
                self.E = (Bs @ null).astype(complex)
            else:
                self.E = Bs.astype(complex)
        self.d = self.E.shape[1]
        assert self.d == dim_lab(p, q), (p, q, self.d)
        self.gen = [self.E.conj().T @ self.tensor_gen(X) @ self.E for X in T]

    def tensor_gen(self, X):
        n = self.p + self.q
        if n == 0:
            return np.zeros((1, 1), dtype=complex)
        return sum(slot_op(X, s, n) for s in range(self.p)) + sum(slot_op(-X.T, s, n) for s in range(self.p, n))

    def D(self, g):
        n = self.p + self.q
        out = np.array([[1.0 + 0j]])
        for s in range(n):
            out = np.kron(out, g if s < self.p else g.conj())
        return self.E.conj().T @ out @ self.E


def cg(irr, target, anti):
    """Isometry W (3, d_mu, d_mu') with (fund or antifund (x) D^mu)(g) W = W D^mu'(g)."""
    d = irr.d
    Xs = [np.kron(-X.T if anti else X, np.eye(d)) + np.kron(np.eye(3), G) for X, G in zip(T, irr.gen)]
    cas = sum(x @ x for x in Xs)
    w, V = np.linalg.eigh(cas)
    lam = 2 * c_lab(target.p, target.q) / 3
    B = V[:, np.abs(w - lam) < 1e-8]
    assert B.shape[1] == target.d, (irr.p, irr.q, target.p, target.q, B.shape)
    dt = target.d
    blocks = [np.kron(np.eye(dt), B.conj().T @ x @ B) - np.kron(G.T, np.eye(dt)) for x, G in zip(Xs, target.gen)]
    u, s, vh = np.linalg.svd(np.vstack(blocks))
    Rm = vh[-1].conj().reshape(dt, dt, order="F")
    assert s[-1] < 1e-8 and (len(s) < 2 or s[-2] > 1e-6)
    Rm = Rm * math.sqrt(dt / np.real(np.trace(Rm.conj().T @ Rm)))
    W = B @ Rm
    return W.reshape(3, d, dt)




# ---------------------------------------------------------------------------------------------------------------- three effective links
LINKS = {"A": (0, "ij"), "U": (1, "kl"), "B": (2, "mn")}
WEIGHT = {"A": 3, "U": 1, "B": 3}          # the arcs A and B are three links each (bivalent unsourced vertices force one irrep per arc)


class Space:
    def __init__(self, Rt):
        self.Rt = Rt
        self.labs = [(p, q) for p in range(Rt + 1) for q in range(Rt + 1 - p)]
        self.irr = {l: Irrep(*l) for l in self.labs}
        self.CG = {}
        for l in self.labs:
            p, q = l
            for anti, outs in ((False, [(p + 1, q), (p - 1, q + 1), (p, q - 1)]), (True, [(p, q + 1), (p + 1, q - 1), (p - 1, q)])):
                for o in outs:
                    if min(o) >= 0 and sum(o) <= Rt:
                        self.CG[(l, o, anti)] = cg(self.irr[l], self.irr[o], anti)

    def cg_defect(self):
        worst = 0.0
        for (l, o, anti), Wt in self.CG.items():
            g = rand_su3()
            Wm = Wt.reshape(3 * self.irr[l].d, self.irr[o].d)
            worst = max(worst, np.abs(np.kron(g.conj() if anti else g, self.irr[l].D(g)) @ Wm - Wm @ self.irr[o].D(g)).max())
        return worst

    def vacuum(self):
        return {((0, 0), (0, 0), (0, 0)): np.ones((1, 1, 1, 1, 1, 1), dtype=complex)}

    def inner(self, F, G):
        s = 0j
        for key, a in F.items():
            if key in G:
                s += np.vdot(a, G[key]) / (self.irr[key[0]].d * self.irr[key[1]].d * self.irr[key[2]].d)
        return s

    @staticmethod
    def add(F, G, a=1.0, b=1.0):
        out = {k: a * v for k, v in F.items()}
        for k, v in G.items():
            out[k] = out.get(k, 0) + b * v
        return out

    def energy(self, key):
        return sum(WEIGHT[n] * c_lab(*key[LINKS[n][0]]) for n in LINKS)

    def mul_loop(self, F, f1, f2):
        """Multiply by Tr(X Y) = sum_{x,y} X_xy Y_yx, X, Y given as (link, dagger, conj): an entry of L is D^fund_(row, col)(L), of L^dagger
        is D^anti_(col, row)(L); complex conjugation swaps fund and anti."""
        out = {}
        (n1, dag1, cj1), (n2, dag2, cj2) = f1, f2
        rep1_anti = dag1 != cj1
        rep2_anti = dag2 != cj2
        r1, c1 = ("y", "x") if dag1 else ("x", "y")
        r2, c2 = ("x", "y") if dag2 else ("y", "x")
        for key, a in F.items():
            for (l1, o1, an1), W1 in self.CG.items():
                if l1 != key[LINKS[n1][0]] or an1 != rep1_anti:
                    continue
                for (l2, o2, an2), W2 in self.CG.items():
                    if l2 != key[LINKS[n2][0]] or an2 != rep2_anti:
                        continue
                    s_in = "ijklmn"
                    s_out = list(s_in)
                    i1, j1 = LINKS[n1][1]
                    i2, j2 = LINKS[n2][1]
                    s_out[s_in.index(i1)], s_out[s_in.index(j1)] = i1.upper(), j1.upper()
                    s_out[s_in.index(i2)], s_out[s_in.index(j2)] = i2.upper(), j2.upper()
                    expr = f"{s_in},{r1}{i1}{i1.upper()},{c1}{j1}{j1.upper()},{r2}{i2}{i2.upper()},{c2}{j2}{j2.upper()}->{''.join(s_out)}"
                    new = np.einsum(expr, a, W1, W1.conj(), W2, W2.conj(), optimize=True)
                    nk = list(key)
                    nk[LINKS[n1][0]] = o1
                    nk[LINKS[n2][0]] = o2
                    nk = tuple(nk)
                    out[nk] = out.get(nk, 0) + new
        return out

    def real_loop(self, F, f1, f2):
        """Multiply by (chi + conj chi)/6 = ReTr/3 of the loop X Y."""
        a = self.mul_loop(F, (f1[0], f1[1], False), (f2[0], f2[1], False))
        b = self.mul_loop(F, (f1[0], f1[1], True), (f2[0], f2[1], True))
        return self.add(a, b, 1 / 6, 1 / 6)


def faces_of(geom):
    if geom == "one":
        return [(("A", False), ("U", False))]
    return [(("A", False), ("U", False)), (("U", True), ("B", False))]


def observable(geom):
    return (("A", False), ("U", False)) if geom == "one" else (("A", False), ("B", False))


def Vc(sp, F, geom):
    out = {}
    for f1, f2 in faces_of(geom):
        out = sp.add(out, sp.real_loop(F, f1, f2), 1.0, -1.0)          # V_c = -(1/6) sum (chi + conj chi) = -sum ReTr/3
    return out


def R0(sp, F):
    return {k: v / sp.energy(k) for k, v in F.items() if sp.energy(k) > 0}


def H(sp, F, u, geom):
    h0 = {k: sp.energy(k) * v for k, v in F.items()}
    return sp.add(h0, Vc(sp, F, geom), 1.0, u)


def lanczos_ground(sp, u, geom, steps=14):
    v0 = sp.vacuum()
    basis = [v0]
    alph, bet = [], []
    for it in range(steps):
        w = H(sp, basis[-1], u, geom)
        a = np.real(sp.inner(basis[-1], w))
        alph.append(a)
        for b in basis:                                      # full reorthogonalization
            w = sp.add(w, b, 1.0, -sp.inner(b, w))
        nb = math.sqrt(max(np.real(sp.inner(w, w)), 0.0))
        if nb < 1e-14:
            break
        bet.append(nb)
        basis.append({k: v / nb for k, v in w.items()})
    k = len(alph)
    Tm = np.diag(alph) + np.diag(bet[:k - 1], 1) + np.diag(bet[:k - 1], -1)
    ev, evec = np.linalg.eigh(Tm)
    g = {}
    for c, b in zip(evec[:, 0], basis[:k]):
        g = sp.add(g, b, 1.0, c)
    nrm = np.real(sp.inner(g, g))
    return ev[0], {kk: v / math.sqrt(nrm) for kk, v in g.items()}


# ---------------------------------------------------------------------------------------------------------------- census
def census(max_order=3):
    """Two-cube open graph (3 x 2 x 2 vertices): oriented faces and the six-link rectangle bounding two adjacent xy faces at z = 0."""
    verts = list(itertools.product(range(3), range(2), range(2)))
    vid = {v: i for i, v in enumerate(verts)}
    edges = {}
    for v in verts:
        for ax in range(3):
            u = list(v); u[ax] += 1; u = tuple(u)
            if u in vid:
                edges[(v, u)] = len(edges)
    faces = []
    for v in verts:
        for a1, a2 in ((0, 1), (0, 2), (1, 2)):
            v1 = list(v); v1[a1] += 1; v1 = tuple(v1)
            v2 = list(v); v2[a2] += 1; v2 = tuple(v2)
            v12 = list(v1); v12[a2] += 1; v12 = tuple(v12)
            if v1 in vid and v2 in vid and v12 in vid:
                b = np.zeros(len(edges), dtype=int)
                b[edges[(v, v1)]] += 1; b[edges[(v1, v12)]] += 1; b[edges[(v2, v12)]] -= 1; b[edges[(v, v2)]] -= 1
                faces.append(((v, a1, a2), b))
    p = next(b for (v, a1, a2), b in faces if v == (0, 0, 0) and (a1, a2) == (0, 1))
    q = next(b for (v, a1, a2), b in faces if v == (1, 0, 0) and (a1, a2) == (0, 1))
    C = p + q
    counts = []
    for n in range(max_order + 1):
        cnt = 0
        pair_only = True
        for sc in (1, -1):
            for seq in itertools.product(range(len(faces)), repeat=n):
                for sg in itertools.product((1, -1), repeat=n):
                    tot = sc * C + sum(s * faces[f][1] for s, f in zip(sg, seq))
                    if not np.any(tot % 3):
                        cnt += 1
                        if n == 2 and sorted(faces[f][0] for f in seq) != sorted([((0, 0, 0), 0, 1), ((1, 0, 0), 0, 1)]):
                            pair_only = False
        counts.append((cnt, pair_only))
    return len(verts), len(edges), len(faces), int(np.count_nonzero(C)), counts


def main():
    t0 = time.time()
    hits, info = [], []
    sp = Space(2)
    cgd = sp.cg_defect()
    print(f"[setup] irreps p + q <= 2 per link, {len(sp.CG)} CG isometries, worst intertwining defect on random SU(3) {cgd:.1e}")
    if cgd > 1e-10:
        info.append(f"CG defect {cgd:.1e}")
    # ------------------------------------------------ route 1: Rayleigh-Schroedinger arrays
    res = {}
    for geom in ("one", "two"):
        v0 = sp.vacuum()
        psi1 = {k: -v for k, v in R0(sp, Vc(sp, v0, geom)).items()}
        psi2 = {k: -v for k, v in R0(sp, Vc(sp, psi1, geom)).items()}
        Wobs = observable(geom)
        Wpsi1 = sp.real_loop(psi1, *Wobs)
        Wpsi2 = sp.real_loop(psi2, *Wobs)
        c1 = 2 * np.real(sp.inner(v0, Wpsi1))
        mid = np.real(sp.inner(psi1, Wpsi1))
        end = 2 * np.real(sp.inner(v0, Wpsi2))
        # psi1 = S/96: compare with (1/96) sum_f (chi_f + conj chi_f) = (6/96) sum_f ReTr/3
        S96 = {}
        for f1, f2 in faces_of(geom):
            S96 = sp.add(S96, sp.real_loop(v0, f1, f2), 1.0, 6 / 96)
        dpsi = sp.add(psi1, S96, 1.0, -1.0)
        dev_psi1 = math.sqrt(max(np.real(sp.inner(dpsi, dpsi)), 0))
        res[geom] = (c1, mid, end, mid + end, dev_psi1)
    c1_one = res["one"][0]
    c1_two, mid, end, c2_two, dev2 = res["two"]
    I = mid * 96 ** 2
    print(f"[route 1] one face: c1 = {c1_one:.15f} vs 1/144 = {1 / 144:.15f}; psi1 = S/96 to {res['one'][4]:.1e}")
    print(f"[route 1] two adjacent faces: first-order {c1_two:.2e}; <psi1, W_C psi1> = {mid:.15e} vs 1/41472 = {1 / 41472:.15e}; 2Re<0, W_C psi2> = "
          f"{end:.15e} vs 1/31104 = {1 / 31104:.15e}; I = int W_C S^2 = 96^2 <psi1,W_C psi1> = {I:.15f} vs 2/9; c2 = {c2_two:.15e} vs 7/124416 = "
          f"{7 / 124416:.15e}; psi1 = S/96 to {dev2:.1e}")
    for name, got, want in (("u/144", c1_one, 1 / 144), ("1/41472", mid, 1 / 41472), ("1/31104", end, 1 / 31104), ("7/124416", c2_two, 7 / 124416),
                            ("I = 2/9", I, 2 / 9)):
        if abs(got - want) > 1e-9 * abs(want) + 1e-15:
            hits.append(f"route 1: {name} recomputed as {got:.15e}")
    if abs(c1_two) > 1e-15:
        hits.append(f"route 1: two-face first-order coefficient {c1_two:.2e} is not 0")
    # ------------------------------------------------ route 2: Lanczos ground states at small u, Richardson
    us = [0.04, 0.02, 0.01, 0.005]
    est = {}
    for geom, power in (("one", 1), ("two", 2)):
        vals = []
        for u in us:
            E0, g = lanczos_ground(sp, u, geom)
            om = np.real(sp.inner(g, sp.real_loop(g, *observable(geom))))
            vals.append(om / u ** power)
        # Richardson on c(u) = c + a u + b u^2 + ... at halving steps
        r1 = [2 * vals[i + 1] - vals[i] for i in range(len(vals) - 1)]
        r2 = [(4 * r1[i + 1] - r1[i]) / 3 for i in range(len(r1) - 1)]
        r3 = [(8 * r2[i + 1] - r2[i]) / 7 for i in range(len(r2) - 1)]
        est[geom] = (vals, r3[-1])
    e1, e2 = est["one"][1], est["two"][1]
    print(f"[route 2] Lanczos ground states at u = {us}: omega(W_p)/u = {', '.join(f'{x:.10f}' for x in est['one'][0])} -> Richardson {e1:.12f} "
          f"(1/144 = {1 / 144:.12f}); omega(W_C)/u^2 = {', '.join(f'{x:.10e}' for x in est['two'][0])} -> Richardson {e2:.12e} (7/124416 = {7 / 124416:.12e})")
    if abs(e1 - 1 / 144) > 1e-6 / 144:
        hits.append(f"route 2: one-face coefficient {e1:.12f}")
    if abs(e2 - 7 / 124416) > 1e-6 * 7 / 124416:
        hits.append(f"route 2: two-face coefficient {e2:.12e}")
    # adverse control of the note: the rectangle's free energy 24 replaced by 16
    wrong = mid + end * 24 / 16
    print(f"[control] replacing the rectangle energy 24 by 16 would give {wrong:.6e} = {Fr(wrong).limit_denominator(10 ** 7)} (the note: a different, "
          f"incorrect coefficient)")
    # ------------------------------------------------ supplement: census
    nv, ne, nf, nc, counts = census(3)
    print(f"[census] two-cube open graph: {nv} vertices, {ne} links, {nf} faces; rectangle with {nc} links; centre-charge survivors at orders "
          f"0/1/2/3: {'/'.join(str(c) for c, _ in counts)} (order-2 survivors all the planar pair: {counts[2][1]})")
    if (nv, ne, nf) != (12, 20, 11) or [c for c, _ in counts[:3]] != [0, 0, 4] or not counts[2][1]:
        hits.append(f"census: ({nv}, {ne}, {nf}) and order 0/1/2 survivors {[c for c, _ in counts[:3]]}")
    print(f"[time] {time.time() - t0:.0f}s")
    for i in info:
        print(f"UNRELIABLE: {i}")
    for h in hits:
        print("HIT: " + h)
    print(f"SUMMARY: attack pattern (f) NORMALIZATION - the open-geometry coefficients recomputed by brute force in an explicit Peter-Weyl basis of "
          f"the 4-link and 7-link graphs: one face c1 = {c1_one:.12f} (route 1) / {e1:.10f} (route 2, Lanczos + Richardson) vs 1/144 = {1 / 144:.12f}; "
          f"two faces c2 = {c2_two:.12e} / {e2:.10e} vs 7/124416 = {7 / 124416:.12e}, with 1/41472, 1/31104, I = 2/9 and psi1 = S/96 reproduced; "
          f"census 0/0/4 at orders 0/1/2 ({counts[3][0]} at order 3); {len(hits)} defects; attack {'FIRES' if hits else 'does not fire'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
