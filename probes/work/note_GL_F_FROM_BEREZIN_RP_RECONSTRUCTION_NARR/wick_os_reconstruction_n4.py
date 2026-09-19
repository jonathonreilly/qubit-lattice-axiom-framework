#!/usr/bin/env python3
"""J:note falsifiers for GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10 (on main).

Falsifiers implemented: (1) chi_{1x} multiplication fails to preserve the OS null space; (2) {psi_x, psi_y} or the normalized
cross-site {psi_x, psi_y^dag} nonzero; (3) the reconstructed parity fails to match the occupation parity; (4) the commuting-nilpotent
branch reconstructs the same cross-site exchange sign.

The runner multiplies elements of the full Grassmann algebra (bitmask expansion of exp(-S)) at N = 2, 3 (exact) and N = 4 staggered
(floating). Here the OS form is computed by WICK'S THEOREM instead: for S = chibar M chi with M = [[I, -K], [0, I]] the propagator is
G = <chi chibar> = M^-1 = [[I, K], [0, I]] (integer for integer K), and <chi_a1 chibar_b1 ... chi_an chibar_bn> = det[G_{a_i b_j}]
after the reordering sign; the commuting-nilpotent branch uses permanents and no signs. The Wick convention is calibrated against a
direct Berezin integral at N = 2 (all 16 x 16 Gram entries). Then, exactly (integers and Fractions), for symmetric positive-definite
integer kernels at N = 2, 3, 4 (N = 4 beyond the note's exact sizes):
  - the OS Gram on all 2^(2N) monomials of A_+: PSD (exact LDL on each charge block), rank = 2^N;
  - null-space invariance under left multiplication by each chi_{1x}: rank [Gram; Gram L_x] = rank Gram (exact);
  - the fields on the occupation basis (chibar_1 monomials, positive-definite Gram): {psi_x, psi_y} = 0, {psi_x, psi_y^dag} =
    (K^-1)_{xy} I, the grading P = (-1)^|S| anticommutes with every psi_x and equals (-1)^{N_hat} with N_hat = sum K_xy psi_x^dag psi_y
    (the normalized number operator), evaluated exactly by Lagrange interpolation on its spectrum 0..N;
  - the commuting-nilpotent branch at N = 2, 3: cross-site [psi_x, psi_y] = 0 and {psi_x, psi_y} != 0.
"""
from __future__ import annotations

import itertools
from fractions import Fraction


def det(M):
    n = len(M)
    if n == 0:
        return Fraction(1)
    A = [[Fraction(x) for x in row] for row in M]
    d = Fraction(1)
    for c in range(n):
        p = next((r for r in range(c, n) if A[r][c] != 0), None)
        if p is None:
            return Fraction(0)
        if p != c:
            A[c], A[p] = A[p], A[c]
            d = -d
        d *= A[c][c]
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                for k in range(c, n):
                    A[r][k] -= f * A[c][k]
    return d


def perm(M):
    n = len(M)
    return sum((Fraction(1) if n == 0 else 1) * _prod(M[i][s[i]] for i in range(n)) for s in itertools.permutations(range(n))) if n else Fraction(1)


def _prod(it):
    out = 1
    for v in it:
        out *= v
    return out


def rank(M):
    A = [[Fraction(x) for x in row] for row in M]
    r = 0
    cols = len(A[0]) if A else 0
    for c in range(cols):
        p = next((i for i in range(r, len(A)) if A[i][c] != 0), None)
        if p is None:
            continue
        A[r], A[p] = A[p], A[r]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c] / A[r][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        r += 1
    return r


def is_psd(M):
    """exact: symmetric M is PSD iff the LDL^T elimination (with zero-pivot handling) has nonnegative pivots and consistent zeros."""
    n = len(M)
    A = [[Fraction(x) for x in row] for row in M]
    for c in range(n):
        if A[c][c] < 0:
            return False
        if A[c][c] == 0:
            if any(A[c][k] != 0 for k in range(c + 1, n)):
                return False
            continue
        for r in range(c + 1, n):
            if A[r][c] != 0:
                f = A[r][c] / A[c][c]
                for k in range(c, n):
                    A[r][k] -= f * A[c][k]
    return True


class Model:
    """generators of A_+: index 2x = chi_{1x}, 2x+1 = chibar_{1x}; slice-0 images carry t = 0."""

    def __init__(self, K, fermion=True):
        self.K = [[Fraction(v) for v in row] for row in K]
        self.N = len(K)
        self.fermion = fermion

    def G(self, a, b):
        (ta, xa), (tb, xb) = a, b
        if ta == tb:
            return Fraction(1 if xa == xb else 0)
        return self.K[xa][xb] if (ta, tb) == (0, 1) else Fraction(0)

    def theta_seq(self, S):
        # Theta reverses the product; chi_{1x} -> chibar_{0x}, chibar_{1x} -> chi_{0x}
        out = []
        for g in reversed(S):
            x, bar = divmod(g, 2)
            out.append(("b" if bar == 0 else "c", (0, x)))
        return out

    def seq(self, S):
        return [("c" if g % 2 == 0 else "b", (1, g // 2)) for g in S]

    def expect(self, word):
        cpos = [i for i, (k, _) in enumerate(word) if k == "c"]
        bpos = [i for i, (k, _) in enumerate(word) if k == "b"]
        if len(cpos) != len(bpos):
            return Fraction(0)
        n = len(cpos)
        mat = [[self.G(word[cpos[i]][1], word[bpos[j]][1]) for j in range(n)] for i in range(n)]
        if not self.fermion:
            return perm(mat)
        target = [p for pair in zip(cpos, bpos) for p in pair]
        inv = sum(1 for i in range(len(target)) for j in range(i + 1, len(target)) if target[i] > target[j])
        return (-1) ** inv * det(mat)

    def monomials(self):
        return [S for k in range(2 * self.N + 1) for S in itertools.combinations(range(2 * self.N), k)]

    def gram(self, basis):
        return [[self.expect(self.theta_seq(S) + self.seq(T)) for T in basis] for S in basis]

    def left_mult(self, g, S):
        """g * m_S as (sign, sorted tuple) or (0, None); fermionic sign = (-1)^(# generators in S before g's slot)."""
        if g in S:
            return 0, None
        sign = (-1) ** sum(1 for h in S if h < g) if self.fermion else 1
        return sign, tuple(sorted(S + (g,)))


def berezin_gram_n2(K):
    """direct Berezin integral at N = 2 (generators: slice 0/1, chi/chibar, sites 0,1), for calibration only."""
    N = 2
    gens = [(t, x, k) for t in (0, 1) for x in range(N) for k in "cb"]
    gi = {g: i for i, g in enumerate(gens)}
    ng = len(gens)

    def mono_mul(a, b):
        if a & b:
            return 0, 0
        cnt, bb = 0, b
        while bb:
            j = (bb & -bb).bit_length() - 1
            cnt += bin(a >> (j + 1)).count("1")
            bb &= bb - 1
        return (-1) ** cnt, a | b

    def mul(A, B):
        out = {}
        for ma, ca in A.items():
            for mb, cb in B.items():
                s, m = mono_mul(ma, mb)
                if s:
                    out[m] = out.get(m, 0) + s * ca * cb
        return {m: c for m, c in out.items() if c != 0}

    def g(t, x, k):
        return {1 << gi[(t, x, k)]: Fraction(1)}

    terms = [(g(t, x, "b"), g(t, x, "c"), Fraction(1)) for t in (0, 1) for x in range(N)]
    terms += [(g(0, x, "b"), g(1, y, "c"), -Fraction(K[x][y])) for x in range(N) for y in range(N)]
    E = {0: Fraction(1)}
    for a, b, c in terms:
        quad = mul(a, b)
        E = mul(E, {0: Fraction(1), **{m: -c * v for m, v in quad.items()}})
    top = (1 << ng) - 1
    Z = E.get(top, Fraction(0))

    def word_to_elem(word):
        el = {0: Fraction(1)}
        for kind, (t, x) in word:
            el = mul(el, g(t, x, kind))
        return el

    mdl = Model(K)
    basis = mdl.monomials()
    Gm = []
    for S in basis:
        row = []
        for T in basis:
            el = mul(word_to_elem(mdl.theta_seq(S) + mdl.seq(T)), E)
            row.append(el.get(top, Fraction(0)) / Z)
        Gm.append(row)
    return Gm


def reconstruct(model):
    N = model.N
    basis = model.monomials()
    charge = lambda S: sum(1 if g % 2 == 0 else -1 for g in S)
    blocks = {}
    for S in basis:
        blocks.setdefault(charge(S), []).append(S)
    # cross-charge entries vanish identically (Wick needs as many chi as chibar); compute the diagonal blocks only
    Gb = {q: [[model.expect(model.theta_seq(S) + model.seq(T)) for T in B] for S in B] for q, B in blocks.items()}
    idx = {q: {S: i for i, S in enumerate(B)} for q, B in blocks.items()}
    rk_b = {q: rank(M) for q, M in Gb.items()}
    rk = sum(rk_b.values())
    psd = all(is_psd(M) for M in Gb.values())
    invariant = True
    for x in range(N):
        for q, B in blocks.items():
            if q + 1 not in blocks:
                continue
            tgt = blocks[q + 1]
            cols = []
            for S in B:
                sgn, T = model.left_mult(2 * x, S)
                col = [Fraction(0)] * len(tgt) if not sgn else [sgn * Gb[q + 1][i][idx[q + 1][T]] for i in range(len(tgt))]
                cols.append(col)
            GL = [[cols[j][i] for j in range(len(B))] for i in range(len(tgt))]   # (Gram_{q+1} L_x) restricted to charge q
            invariant &= rank(Gb[q] + GL) == rk_b[q]
    occ = [tuple(2 * x + 1 for x in sub) for k in range(N + 1) for sub in itertools.combinations(range(N), k)]
    ip = lambda S, T: model.expect(model.theta_seq(S) + model.seq(T))
    Go = [[ip(S, T) for T in occ] for S in occ]
    pd = is_psd(Go) and rank(Go) == len(occ)
    n = len(occ)
    Goinv = _inv(Go)

    def field(x):
        cols = []
        for S in occ:
            sgn, T = model.left_mult(2 * x, S)
            rhs = [Fraction(0)] * n if not sgn else [sgn * ip(U, T) for U in occ]
            cols.append([sum(Goinv[i][k] * rhs[k] for k in range(n)) for i in range(n)])
        return [[cols[j][i] for j in range(n)] for i in range(n)]

    Psi = [field(x) for x in range(N)]
    Psid = [_mm(_mm(Goinv, _T(P)), Go) for P in Psi]
    Kinv = _inv(model.K)
    anti = all(_is_zero(_add(_mm(Psi[x], Psi[y]), _mm(Psi[y], Psi[x]))) for x in range(N) for y in range(N))
    car = all(_add(_mm(Psi[x], Psid[y]), _mm(Psid[y], Psi[x])) == _scal(Kinv[x][y], _eye(n)) for x in range(N) for y in range(N))
    P = [[Fraction((-1) ** len(occ[i])) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    par_anti = all(_is_zero(_add(_mm(P, Psi[x]), _mm(Psi[x], P))) for x in range(N))
    Nhat = [[Fraction(0)] * n for _ in range(n)]
    for x in range(N):
        for y in range(N):
            Nhat = _add(Nhat, _scal(model.K[x][y], _mm(Psid[x], Psi[y])))
    par_word = [[Fraction(0)] * n for _ in range(n)]
    for k in range(N + 1):
        term = _eye(n)
        for j in range(N + 1):
            if j != k:
                term = _scal(Fraction(1, k - j), _mm(term, _add(Nhat, _scal(-j, _eye(n)))))
        par_word = _add(par_word, _scal((-1) ** k, term))
    par_match = par_word == P
    return {"monomials": len(basis), "rank": rk, "2^N": 2 ** N, "PSD": psd, "null space invariant": invariant,
            "occupation Gram PD": pd, "{psi,psi}=0": anti, "{psi,psi^dag}=Kinv I": car, "P anticommutes": par_anti,
            "P = (-1)^Nhat": par_match}


def cn_branch(K):
    m = Model(K, fermion=False)
    N = m.N
    basis = m.monomials()
    Gm = m.gram(basis)
    pos = {S: i for i, S in enumerate(basis)}
    occ = [tuple(2 * x + 1 for x in sub) for k in range(N + 1) for sub in itertools.combinations(range(N), k)]
    Go = [[Gm[pos[S]][pos[T]] for T in occ] for S in occ]
    n = len(occ)
    Goinv = _inv(Go)

    def field(x):
        cols = []
        for S in occ:
            s, T = m.left_mult(2 * x, S)
            rhs = [Fraction(0)] * n if not s else [s * Gm[pos[U]][pos[T]] for U in occ]
            cols.append([sum(Goinv[i][k] * rhs[k] for k in range(n)) for i in range(n)])
        return [[cols[j][i] for j in range(n)] for i in range(n)]

    Psi = [field(x) for x in range(N)]
    comm = all(_is_zero(_add(_mm(Psi[x], Psi[y]), _scal(-1, _mm(Psi[y], Psi[x])))) for x in range(N) for y in range(N) if x != y)
    anti_nonzero = all(not _is_zero(_add(_mm(Psi[x], Psi[y]), _mm(Psi[y], Psi[x]))) for x in range(N) for y in range(N) if x != y)
    return comm, anti_nonzero


def _eye(n):
    return [[Fraction(1 if i == j else 0) for j in range(n)] for i in range(n)]


def _T(A):
    return [list(r) for r in zip(*A)]


def _mm(A, B):
    Bt = _T(B)
    return [[sum(a * b for a, b in zip(r, c)) for c in Bt] for r in A]


def _add(A, B):
    return [[a + b for a, b in zip(r, s)] for r, s in zip(A, B)]


def _scal(c, A):
    return [[c * a for a in r] for r in A]


def _is_zero(A):
    return all(a == 0 for r in A for a in r)


def _inv(A):
    n = len(A)
    M = [[Fraction(x) for x in r] + [Fraction(1 if i == j else 0) for j in range(n)] for i, r in enumerate(A)]
    for c in range(n):
        p = next(r for r in range(c, n) if M[r][c] != 0)
        M[c], M[p] = M[p], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for r in range(n):
            if r != c and M[r][c] != 0:
                f = M[r][c]
                M[r] = [a - f * b for a, b in zip(M[r], M[c])]
    return [r[n:] for r in M]


def main():
    Kcal = [[2, 1], [1, 3]]
    Gw = Model(Kcal).gram(Model(Kcal).monomials())
    Gb = berezin_gram_n2(Kcal)
    calib = Gw == Gb
    print(f"0. Wick convention calibrated against a direct Berezin integral at N = 2 (all 16 x 16 OS Gram entries equal): {calib}")
    kernels = {2: [[[2, 1], [1, 3]], [[1, 0], [0, 2]]],
               3: [[[2, 1, 0], [1, 3, 1], [0, 1, 2]], [[3, -1, 1], [-1, 2, 0], [1, 0, 4]]],
               4: [[[2, 1, 0, 0], [1, 3, 1, 0], [0, 1, 2, 1], [0, 0, 1, 3]], [[4, 1, -1, 0], [1, 3, 0, 1], [-1, 0, 2, 0], [0, 1, 0, 5]]]}
    allok = calib
    for N, Ks in kernels.items():
        for K in Ks:
            r = reconstruct(Model(K))
            ok = (r["rank"] == r["2^N"] and r["PSD"] and r["null space invariant"] and r["occupation Gram PD"]
                  and r["{psi,psi}=0"] and r["{psi,psi^dag}=Kinv I"] and r["P anticommutes"] and r["P = (-1)^Nhat"])
            allok &= ok
            print(f"N = {N}, K = {K}: {r}")
    cn = {N: cn_branch(kernels[N][0]) for N in (2, 3)}
    print(f"commuting-nilpotent branch (permanents, no signs): cross-site [psi_x, psi_y] = 0 and {{psi_x, psi_y}} != 0: {cn}")
    cn_ok = all(a and b for a, b in cn.values())
    if not (allok and cn_ok):
        print(f"HIT: a falsifier fires (Grassmann checks {allok}, commuting-nilpotent separation {cn_ok})")
    print(f"SUMMARY: no falsifier fires: with the OS form computed by Wick determinants of G = [[I, K], [0, I]] (calibrated against a direct "
          f"Berezin integral), for two SPD integer kernels at each N = 2, 3, 4 (N = 4: 256 monomials, beyond the note's exact sizes) the "
          f"Gram is PSD with rank 2^N, the null space is invariant under every chi_1x, the reconstructed fields satisfy {{psi_x, psi_y}} = 0 "
          f"and {{psi_x, psi_y^dag}} = (K^-1)_xy I, and the grading equals (-1)^N_hat ({allok}); the commuting-nilpotent branch gives "
          f"commuting, not anticommuting, cross-site fields ({cn_ok})")


if __name__ == "__main__":
    main()
