#!/usr/bin/env python3
"""
Derivation attempt J:derive:review-20261008-portfolio-next-bridge:a1

Target interface: family 265 (area-law upper bound vs the coefficient 1/4).
The portfolio's non-selection counterexample is a disjoint-dimer Hamiltonian,
which breaks lattice translation and cubic-rotation symmetry.  This script
checks a replacement that keeps those symmetries: the weighted-graph-state
parent Hamiltonian on qubits of an open box of Z^d,

    H_phi = sum_v h_v ,   h_v = U (1 - |+><+|_v) U^dagger ,
    U = prod_{edges (u,v)} CPhase_{uv}(phi),   CPhase = diag(1,1,1,exp(i phi)).

Exact arithmetic only (Fractions over the cyclotomic fields Q(zeta_m),
m in {2,3,4,6}, phi = 2 pi / m); mpmath only for the displayed entropy values.
One process, a few hundred MB, runtime well under ten minutes.
"""
import itertools
import sys
import time
from fractions import Fraction as Fr

import mpmath as mp

T0 = time.time()
PASS = 0
FAIL = 0


def report(ok, msg):
    global PASS, FAIL
    if ok:
        PASS += 1
        print("PASS " + msg)
    else:
        FAIL += 1
        print("FAIL " + msg)


# ---------------------------------------------------------------------------
# exact arithmetic in Q(zeta_m): elements are pairs (a0, a1) = a0 + a1*zeta
# with zeta^2 = R0 + R1*zeta (from the cyclotomic polynomial).
# m=2: zeta = -1 is rational; it is embedded with zeta^2 = 1 and the relation
# zeta = -1 is imposed by using the pair (a0 - a1, 0) at normalisation time.
# To keep things uniform we treat m=2 as the field Q(zeta_4)-free case below.
# ---------------------------------------------------------------------------
RED = {3: (-1, -1), 4: (-1, 0), 6: (-1, 1)}  # zeta^2 = R0 + R1 zeta


class Field:
    def __init__(self, m):
        assert m in (2, 3, 4, 6)
        self.m = m
        self.zero = (Fr(0), Fr(0))
        self.one = (Fr(1), Fr(0))
        # powers of zeta as pairs
        if m == 2:
            self.zpow = [self.one, (Fr(-1), Fr(0))]
        else:
            r0, r1 = RED[m]
            pw = [self.one]
            cur = (Fr(0), Fr(1))
            pw.append(cur)
            for _ in range(2, m):
                a0, a1 = pw[-1]
                # multiply by zeta: (a0 + a1 z) z = a0 z + a1 z^2
                pw.append((a1 * r0, a0 + a1 * r1))
            # consistency: zeta^m = 1
            a0, a1 = pw[-1]
            top = (a1 * r0, a0 + a1 * r1)
            assert top == self.one, (m, top)
            self.zpow = pw

    def add(self, a, b):
        return (a[0] + b[0], a[1] + b[1])

    def sub(self, a, b):
        return (a[0] - b[0], a[1] - b[1])

    def neg(self, a):
        return (-a[0], -a[1])

    def smul(self, c, a):
        return (c * a[0], c * a[1])

    def mul(self, a, b):
        if self.m == 2:
            return (a[0] * b[0], Fr(0))  # only the rational part is used
        r0, r1 = RED[self.m]
        c0 = a[0] * b[0]
        c1 = a[0] * b[1] + a[1] * b[0]
        c2 = a[1] * b[1]
        return (c0 + c2 * r0, c1 + c2 * r1)

    def z(self, k):
        return self.zpow[k % self.m]

    def is_zero(self, a):
        return a[0] == 0 and a[1] == 0

    def rational(self, a):
        return a[1] == 0


# ---------------------------------------------------------------------------
# geometry
# ---------------------------------------------------------------------------
def box_sites(dims):
    return list(itertools.product(*[range(n) for n in dims]))


def box_edges(dims, periodic=False):
    sites = box_sites(dims)
    idx = {s: i for i, s in enumerate(sites)}
    edges = set()
    for s in sites:
        for ax in range(len(dims)):
            t = list(s)
            t[ax] += 1
            if t[ax] >= dims[ax]:
                if not periodic or dims[ax] < 3:
                    continue
                t[ax] = 0
            edges.add(tuple(sorted((idx[s], idx[tuple(t)]))))
    return sites, idx, sorted(edges)


def energy(z, edges):
    """E(z) = sum over edges of z_u z_v (z a bitmask)."""
    e = 0
    for (u, v) in edges:
        e += ((z >> u) & 1) & ((z >> v) & 1)
    return e


def nbrs(edges, n):
    nb = [[] for _ in range(n)]
    for (u, v) in edges:
        nb[u].append(v)
        nb[v].append(u)
    return nb


# ---------------------------------------------------------------------------
# sparse operators: dict column -> dict row -> field element
# ---------------------------------------------------------------------------
def op_apply_col(F, A, vec):
    """A applied to a sparse vector (dict row->elt)."""
    out = {}
    for r, c in vec.items():
        col = A.get(r)
        if col is None:
            continue
        for rr, val in col.items():
            t = F.mul(val, c)
            if rr in out:
                out[rr] = F.add(out[rr], t)
            else:
                out[rr] = t
    return {k: v for k, v in out.items() if not F.is_zero(v)}


def op_mul(F, A, B, ncols):
    out = {}
    for c in range(ncols):
        col = B.get(c)
        if col is None:
            continue
        res = op_apply_col(F, A, col)
        if res:
            out[c] = res
    return out


def op_add(F, A, B):
    out = {}
    for c in set(A) | set(B):
        col = dict(A.get(c, {}))
        for r, v in B.get(c, {}).items():
            col[r] = F.add(col[r], v) if r in col else v
        col = {k: v for k, v in col.items() if not F.is_zero(v)}
        if col:
            out[c] = col
    return out


def op_scale_sub_identity(F, A, k, ncols):
    """A - k*I."""
    out = {}
    for c in range(ncols):
        col = dict(A.get(c, {}))
        col[c] = F.sub(col.get(c, F.zero), (Fr(k), Fr(0)))
        col = {r: v for r, v in col.items() if not F.is_zero(v)}
        if col:
            out[c] = col
    return out


def op_equal(F, A, B):
    for c in set(A) | set(B):
        a, b = A.get(c, {}), B.get(c, {})
        for r in set(a) | set(b):
            x = a.get(r, F.zero)
            y = b.get(r, F.zero)
            if x != y:
                return False
    return True


def op_trace(F, A):
    t = F.zero
    for c, col in A.items():
        if c in col:
            t = F.add(t, col[c])
    return t


def build_local_terms(F, n, edges):
    """h_v from the LOCAL formula: (1 - |+_n><+_n|) on v, n = # occupied neighbours."""
    nb = nbrs(edges, n)
    half = Fr(1, 2)
    terms = []
    for v in range(n):
        T = {}
        for zc in range(1 << n):
            nn = sum((zc >> u) & 1 for u in nb[v])
            old = (zc >> v) & 1
            col = {zc: (half, Fr(0))}
            new_bit = 1 - old
            k = nn if new_bit > old else -nn
            col[zc ^ (1 << v)] = F.smul(-half, F.z(k))
            T[zc] = col
        terms.append(T)
    return terms


def build_conjugated_terms(F, n, edges):
    """U P_v U^dagger built from the global diagonal U, P_v = 1 - |+><+|_v (n=0 form)."""
    half = Fr(1, 2)
    Ez = [energy(z, edges) for z in range(1 << n)]
    terms = []
    for v in range(n):
        T = {}
        for zc in range(1 << n):
            col = {zc: (half, Fr(0))}
            zr = zc ^ (1 << v)
            col[zr] = F.smul(-half, F.z(Ez[zr] - Ez[zc]))
            T[zc] = col
        terms.append(T)
    return terms


# ---------------------------------------------------------------------------
# Part 1: Hamiltonian structure on small open boxes (exact)
# ---------------------------------------------------------------------------
def check_hamiltonian(dims, m, label, full_spectrum):
    F = Field(m)
    sites, idx, edges = box_edges(dims)
    n = len(sites)
    N = 1 << n
    loc = build_local_terms(F, n, edges)
    glo = build_conjugated_terms(F, n, edges)
    same = all(op_equal(F, loc[v], glo[v]) for v in range(n))
    report(same, f"{label} m={m}: local star formula h_v == U P_v U^dagger for all {n} sites")
    # locality: h_v changes only bit v and its entries depend only on bits of nbrs(v)
    nb = nbrs(edges, n)
    ok_loc = True
    for v in range(n):
        base_support = set(nb[v]) | {v}
        for zc in range(N):
            for zr in loc[v][zc]:
                diff = zc ^ zr
                if diff not in (0, 1 << v):
                    ok_loc = False
        # dependence only on neighbours: flipping a non-neighbour bit w not in star
        # leaves the column pattern unchanged
        for w in range(n):
            if w in base_support:
                continue
            for zc in range(0, N, max(1, N // 16)):
                a = loc[v][zc]
                b = loc[v][zc ^ (1 << w)]
                pa = {(r ^ zc): val for r, val in a.items()}
                pb = {(r ^ (zc ^ (1 << w))): val for r, val in b.items()}
                if pa != pb:
                    ok_loc = False
    report(ok_loc, f"{label} m={m}: each h_v acts on the star of v only (support radius 1)")
    idem = all(op_equal(F, op_mul(F, loc[v], loc[v], N), loc[v]) for v in range(n))
    report(idem, f"{label} m={m}: h_v^2 = h_v (norm-one projectors)")
    comm = True
    for u in range(n):
        for v in range(u + 1, n):
            if not op_equal(F, op_mul(F, loc[u], loc[v], N), op_mul(F, loc[v], loc[u], N)):
                comm = False
    report(comm, f"{label} m={m}: all pairs [h_u,h_v] = 0")
    tr_ok = all(op_trace(F, loc[v]) == (Fr(N, 2), Fr(0)) for v in range(n))
    report(tr_ok, f"{label} m={m}: Tr h_v = 2^(n-1) (rank 2^(n-1) projectors)")
    H = {}
    for v in range(n):
        H = op_add(F, H, loc[v])
    psi = {z: F.z(energy(z, edges)) for z in range(N)}
    Hpsi = op_apply_col(F, H, psi)
    report(len(Hpsi) == 0, f"{label} m={m}: H psi = 0 for psi(z)=zeta^E(z) (weighted graph state)")
    if full_spectrum:
        # prod_{k=0}^{n} (H - k) = 0 ; traces of H^p give multiplicities C(n,k)
        from math import comb
        P = None
        for k in range(n + 1):
            Hk = op_scale_sub_identity(F, H, k, N)
            P = Hk if P is None else op_mul(F, Hk, P, N)
        report(len(P) == 0, f"{label} m={m}: prod_(k=0..{n}) (H-k) = 0, spectrum within integers 0..{n}")
        okmult = True
        Hp = None
        for p in range(1, n + 1):
            Hp = H if Hp is None else op_mul(F, H, Hp, N)
            want = sum(comb(n, k) * k ** p for k in range(n + 1))
            if op_trace(F, Hp) != (Fr(want), Fr(0)):
                okmult = False
        report(okmult, f"{label} m={m}: Tr H^p (p=1..{n}) = sum_k C({n},k) k^p, so multiplicity of k is C({n},k); "
                       f"lowest eigenvalue 0 simple, gap exactly 1")


# ---------------------------------------------------------------------------
# Part 2: symmetry
# ---------------------------------------------------------------------------
def cube_rotations():
    """The 24 proper rotations of the cube as signed permutation matrices."""
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            # determinant of signed permutation
            sgn = 1
            p = list(perm)
            for i in range(3):
                for j in range(i + 1, 3):
                    if p[i] > p[j]:
                        sgn = -sgn
            det = sgn * signs[0] * signs[1] * signs[2]
            if det == 1:
                mats.append((perm, signs))
    return mats


def apply_sym(perm, signs, s, dims):
    c = [s[i] - (dims[i] - 1) / 2.0 for i in range(len(s))]
    t = [signs[i] * c[perm[i]] for i in range(len(s))]
    return tuple(int(round(t[i] + (dims[i] - 1) / 2.0)) for i in range(len(s)))


def check_symmetry_graph(dims, label):
    sites, idx, edges = box_edges(dims)
    eset = set(edges)
    syms = cube_rotations() if len(dims) == 3 else None
    ok = True
    count = 0
    for perm, signs in syms:
        # only symmetries of the box shape
        if any(dims[i] != dims[perm[i]] for i in range(3)):
            continue
        count += 1
        pi = {}
        for s in sites:
            pi[idx[s]] = idx[apply_sym(perm, signs, s, dims)]
        img = set(tuple(sorted((pi[u], pi[v]))) for (u, v) in edges)
        if img != eset:
            ok = False
    report(ok and count == 24, f"{label}: edge set invariant under all {count} proper cubic rotations of the box (so U and H are)")


def check_symmetry_operator_2x2(m):
    """Operator-level: conjugating h_v by the site permutation gives h_pi(v) for all 8 symmetries of the 2x2 box."""
    F = Field(m)
    sites, idx, edges = box_edges((2, 2))
    n = len(sites)
    N = 1 << n
    loc = build_local_terms(F, n, edges)
    ok = True
    syms = []
    for perm in itertools.permutations(range(2)):
        for signs in itertools.product((1, -1), repeat=2):
            syms.append((perm, signs))
    for perm, signs in syms:
        pi = {}
        for s in sites:
            c = [s[i] - 0.5 for i in range(2)]
            t = [signs[i] * c[perm[i]] for i in range(2)]
            pi[idx[s]] = idx[tuple(int(round(t[i] + 0.5)) for i in range(2))]

        def permute_bits(z):
            out = 0
            for u in range(n):
                if (z >> u) & 1:
                    out |= 1 << pi[u]
            return out
        for v in range(n):
            Tv = {}
            for zc, col in loc[v].items():
                Tv[permute_bits(zc)] = {permute_bits(zr): val for zr, val in col.items()}
            if not op_equal(F, Tv, loc[pi[v]]):
                ok = False
    report(ok, f"2x2 box m={m}: P_pi h_v P_pi^-1 = h_pi(v) for all 8 square symmetries (operator level)")


def check_translation_torus():
    """On a 3x3x3 torus every site has the same 6 neighbours up to translation, edge set translation invariant."""
    sites, idx, edges = box_edges((3, 3, 3), periodic=True)
    eset = set(edges)
    ok = len(edges) == 81
    for t in itertools.product(range(3), repeat=3):
        img = set()
        for (u, v) in edges:
            su, sv = sites[u], sites[v]
            tu = tuple((su[i] + t[i]) % 3 for i in range(3))
            tv = tuple((sv[i] + t[i]) % 3 for i in range(3))
            img.add(tuple(sorted((idx[tu], idx[tv]))))
        if img != eset:
            ok = False
    nb = nbrs(edges, len(sites))
    ok = ok and all(len(x) == 6 for x in nb)
    report(ok, "3x3x3 torus: 81 edges, every site has 6 neighbours, edge set invariant under all 27 translations")


# ---------------------------------------------------------------------------
# Part 3: flat-cut entropy (exact power sums + high-precision entropy)
# ---------------------------------------------------------------------------
def reduced_state(F, dims, cut_axis0_k, m):
    """Return (rhoTilde as list of lists of field elements, nA, L, nTotal).
    A = sites with first coordinate < cut_axis0_k.  rho = rhoTilde / 2^n."""
    sites, idx, edges = box_edges(dims)
    n = len(sites)
    Aset = [i for i, s in enumerate(sites) if s[0] < cut_axis0_k]
    Bset = [i for i in range(n) if i not in Aset]
    cut = [(u, v) for (u, v) in edges if (u in Aset) != (v in Aset)]
    nA, nB = len(Aset), len(Bset)
    # amplitude index by (a, b) bitmasks over Aset, Bset
    def zmask(a, b):
        z = 0
        for j, u in enumerate(Aset):
            if (a >> j) & 1:
                z |= 1 << u
        for j, u in enumerate(Bset):
            if (b >> j) & 1:
                z |= 1 << u
        return z
    E = [[energy(zmask(a, b), edges) for b in range(1 << nB)] for a in range(1 << nA)]
    dA = 1 << nA
    rho = [[F.zero for _ in range(dA)] for _ in range(dA)]
    for a in range(dA):
        for a2 in range(dA):
            acc = [0] * m
            for b in range(1 << nB):
                acc[(E[a][b] - E[a2][b]) % m] += 1
            tot = F.zero
            for k in range(m):
                if acc[k]:
                    tot = F.add(tot, F.smul(Fr(acc[k]), F.z(k)))
            rho[a][a2] = tot
    return rho, nA, len(cut), n, cut, Aset


def matmul(F, X, Y):
    d = len(X)
    out = [[F.zero] * d for _ in range(d)]
    for i in range(d):
        Xi = X[i]
        for k in range(d):
            x = Xi[k]
            if F.is_zero(x):
                continue
            Yk = Y[k]
            Oi = out[i]
            for j in range(d):
                y = Yk[j]
                if F.is_zero(y):
                    continue
                Oi[j] = F.add(Oi[j], F.mul(x, y))
    return out


def trace_mat(F, X):
    t = F.zero
    for i in range(len(X)):
        t = F.add(t, X[i][i])
    return t


def newton_s(p, e):
    s = [Fr(2), Fr(1)]
    for q in range(2, p + 1):
        s.append(s[-1] - e * s[-2])
    return s[p]


def check_entropy(dims, k, m, label):
    F = Field(m)
    rho, nA, L, n, cut, Aset = reduced_state(F, dims, k, m)
    # cut edges must form a matching (flat cut)
    ends = [u for e in cut for u in e]
    matching = len(set(ends)) == len(ends)
    cosphi = {2: Fr(-1), 3: Fr(-1, 2), 4: Fr(0), 6: Fr(1, 2)}[m]
    e = (1 - cosphi) / 8  # lambda+ * lambda- = sin^2(phi/2)/4
    scale = Fr(1, 2 ** n)
    dA = 1 << nA
    # exact power sums of rho = rhoTilde / 2^n, p = 1..dA
    ok = True
    P = rho
    for p in range(1, dA + 1):
        if p > 1:
            P = matmul(F, rho, P)
        t = trace_mat(F, P)
        val = t[0] * scale ** p
        want = newton_s(p, e) ** L if p >= 1 else Fr(1)
        if not (F.rational(t) and val == want):
            ok = False
            break
    report(matching and ok,
           f"{label} phi=2pi/{m}: cut has L={L} disjoint edges, A has {nA} sites; Tr rho_A^p = (lam+^p+lam-^p)^L exactly, p=1..{dA} "
           f"(so spec rho_A = spec ((c c^dag)/4)^(x)L)")
    # high-precision entropy from the exact rho (convert to mp matrix)
    mp.mp.dps = 40
    z = mp.e ** (2j * mp.pi / m)
    M = mp.matrix(dA, dA)
    for i in range(dA):
        for j in range(dA):
            a = rho[i][j]
            M[i, j] = (mp.mpf(a[0].numerator) / a[0].denominator + mp.mpf(a[1].numerator) / a[1].denominator * z) / mp.mpf(2) ** n
    ev = mp.eigh(M, eigvals_only=True)
    S = mp.mpf(0)
    for lam in ev:
        if lam > mp.mpf(10) ** (-30):
            S -= lam * mp.log(lam)
    c = mp.cos(mp.pi / m)  # cos(phi/2)
    q = (1 + c) / 2
    h = -(q * mp.log(q) + (1 - q) * mp.log(1 - q)) if q < 1 else mp.mpf(0)
    report(abs(S - L * h) < mp.mpf(10) ** (-25),
           f"{label} phi=2pi/{m}: S(A) = {mp.nstr(S, 14)} = L*h((1+cos(phi/2))/2) with L={L}, h={mp.nstr(h, 14)}")


def check_nonflat_scope(m):
    """Single interior site of the 3x3 grid: its 4 cut edges share the site, the additive formula must fail."""
    F = Field(m)
    sites, idx, edges = box_edges((3, 3))
    n = len(sites)
    centre = idx[(1, 1)]
    others = [i for i in range(n) if i != centre]
    def zmask(a, b):
        z = 0
        if a:
            z |= 1 << centre
        for j, u in enumerate(others):
            if (b >> j) & 1:
                z |= 1 << u
        return z
    rho = [[F.zero] * 2 for _ in range(2)]
    for a in range(2):
        for a2 in range(2):
            acc = [0] * m
            for b in range(1 << len(others)):
                acc[(energy(zmask(a, b), edges) - energy(zmask(a2, b), edges)) % m] += 1
            tot = F.zero
            for k in range(m):
                if acc[k]:
                    tot = F.add(tot, F.smul(Fr(acc[k]), F.z(k)))
            rho[a][a2] = tot
    scale = Fr(1, 2 ** n)
    purity = F.add(F.mul(rho[0][0], rho[0][0]), F.mul(rho[0][1], rho[1][0]))
    purity = F.add(purity, F.add(F.mul(rho[1][0], rho[0][1]), F.mul(rho[1][1], rho[1][1])))
    pur = purity[0] * scale ** 2
    cosphi = {2: Fr(-1), 3: Fr(-1, 2), 4: Fr(0), 6: Fr(1, 2)}[m]
    e = (1 - cosphi) / 8
    additive = newton_s(2, e) ** 4
    # exact value: (1 + |((1+e^{-i phi})/2)|^8)/2 = (1 + cos(phi/2)^8)/2 ; cos^2(phi/2) = (1+cos phi)/2
    c2 = (1 + cosphi) / 2
    exact = (1 + c2 ** 4) / 2
    report(F.rational(purity) and pur == exact and pur != additive,
           f"single site of 3x3 grid, phi=2pi/{m}: purity {pur} = (1+cos^8(phi/2))/2 differs from the matching formula {additive} "
           f"(additivity is specific to cuts made of disjoint edges)")


# ---------------------------------------------------------------------------
# Part 4: the coefficient function s(phi) = h((1 + cos(phi/2))/2)
# ---------------------------------------------------------------------------
def check_coefficient_function():
    import sympy as sp
    ph = sp.symbols("phi", positive=True)
    q = (1 + sp.cos(ph / 2)) / 2
    s = -(q * sp.log(q) + (1 - q) * sp.log(1 - q))
    ds = sp.simplify(sp.diff(s, ph))
    # ds = (dq/dphi) * log((1-q)/q); dq/dphi = -sin(phi/2)/4 < 0, log((1-q)/q) < 0 for q > 1/2
    mp.mp.dps = 30
    f = sp.lambdify(ph, ds, "mpmath")
    pts = [mp.mpf(k) * mp.pi / 400 for k in range(1, 400)]
    report(all(f(x) > 0 for x in pts), "ds/dphi > 0 on 399 grid points of (0,pi): s strictly increasing there")
    sf = sp.lambdify(ph, s, "mpmath")
    # endpoints via limits
    s0 = sp.limit(s, ph, 0, "+")
    spi = sp.simplify(s.subs(ph, sp.pi))
    report(s0 == 0 and sp.simplify(spi - sp.log(2)) == 0, "s(0+) = 0 and s(pi) = ln 2 (exact, sympy)")
    for target, name in ((mp.mpf(1) / 4, "1/4 nat"), (mp.log(2) / 4, "1/4 bit")):
        phi_star = mp.findroot(lambda x: sf(x) - target, (mp.mpf("1.0"), mp.pi - mp.mpf("0.01")), solver="anderson", tol=1e-25)
        ok = 0 < phi_star < mp.pi and abs(sf(phi_star) - target) < mp.mpf(10) ** (-20)
        report(ok, f"unique phi in (0,pi) with s(phi) = {name}: phi = {mp.nstr(phi_star, 12)}")
    return



def check_dimer_noncovariance():
    """Any edge set invariant under all translations of a torus Z_n^d (n >= 3) is a union of full direction classes, and
    contains two edges at every vertex, so it is never a dimer tiling (matching).  Checked exhaustively for n=4,d=2 and n=3,d=3."""
    ok = True
    for (n, d) in ((4, 2), (3, 3)):
        sites = list(itertools.product(range(n), repeat=d))
        for ax in range(d):
            edges = set()
            for s in sites:
                t = list(s)
                t[ax] = (t[ax] + 1) % n
                edges.add(frozenset((s, tuple(t))))
            deg = {s: 0 for s in sites}
            for e in edges:
                for u in e:
                    deg[u] += 1
            if set(deg.values()) != {2}:
                ok = False
    report(ok, "torus Z_4^2 and Z_3^3: the translation orbit of any single edge gives degree 2 at every vertex, "
               "so no translation-invariant dimer tiling exists (the dimer family breaks translations)")

# ---------------------------------------------------------------------------
def main():
    print("# Part 1: H_phi on small open boxes: local star terms, projectors, commutation, spectrum")
    for m in (2, 3, 4, 6):
        check_hamiltonian((4,), m, "chain n=4", True)
        check_hamiltonian((2, 2), m, "2x2 box", True)
    for m in (3, 4):
        check_hamiltonian((2, 3), m, "2x3 box", True)
    for m in (2, 3):
        check_hamiltonian((2, 2, 2), m, "2x2x2 cube", False)

    print("# Part 2: lattice symmetries")
    for m in (2, 3, 4, 6):
        check_symmetry_operator_2x2(m)
    check_symmetry_graph((3, 3, 3), "3x3x3 box")
    check_symmetry_graph((2, 2, 2), "2x2x2 box")
    check_translation_torus()
    check_dimer_noncovariance()

    print("# Part 3: flat-cut entanglement entropy is L * h((1+cos(phi/2))/2)")
    for m in (2, 3, 4, 6):
        check_entropy((2,), 1, m, "chain 1|1")
        check_entropy((2, 2), 1, m, "2x2 box, column cut")
        check_entropy((3, 3), 1, m, "3x3 box, column cut")
        check_entropy((4, 2), 2, m, "4x2 box, middle cut")
        check_entropy((2, 2, 2), 1, m, "2x2x2 cube, layer cut")
    for m in (2, 3, 4, 6):
        check_nonflat_scope(m)

    print("# Part 4: the coefficient function")
    check_coefficient_function()

    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("# runtime seconds: %.1f" % (time.time() - T0))
    if FAIL == 0:
        print("HIT: scoped counterexample - on qubits of open boxes of Z^d the translation- and cubic-rotation-invariant "
              "weighted-graph-state parent Hamiltonian has unique ground state, norm-one commuting star terms and gap exactly 1 "
              "for every size, while its flat-cut entropy per boundary edge h((1+cos(phi/2))/2) takes every value in [0, ln 2]; "
              "so the area-law upper bound with gap/locality/uniqueness does not select a coefficient even inside the "
              "Lattice-axiom symmetry class (dimer family was non-covariant)")
    print("SUMMARY: exact checks that the covariant weighted-graph-state family H_phi has commuting norm-one star projectors, "
          "ground state at 0, gap exactly 1, lattice-symmetric terms, and flat-cut entropy L*h((1+cos(phi/2))/2), "
          "tunable over [0, ln 2]; unrefereed, and the external theorem's exact interaction-range hypothesis is not re-read.")
    sys.exit(0 if FAIL == 0 else 1)


if __name__ == "__main__":
    main()
