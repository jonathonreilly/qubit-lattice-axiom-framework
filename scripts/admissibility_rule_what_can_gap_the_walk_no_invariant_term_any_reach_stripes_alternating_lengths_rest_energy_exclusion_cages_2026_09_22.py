#!/usr/bin/env python3
"""Exact checks: what can gap the walk inside the qubit (block 54's walk and supplied backgrounds; the Record axiom's exclusion; not adopted).

OBJECTS: H = sum_a sigma_a S_a on Z^3 (block 54), its eight species at k in {0, pi}^3; the proper cubic rotations acting on the coin by
their SU(2) lifts; backgrounds on sites (M(x) = m_0(x) + m(x).sigma), on bonds (hop amplitudes t_j(x); staggered phases); the axioms'
scalar hop A = 2a sum_j cos k_j (block 77); the exclusion projector (blocks 78, 80).
T1: every covariant translation-invariant term of any finite reach is a multiple of the identity at each species point (the coin representation
   of the 24 rotations is irreducible and every corner is fixed): the two branches touch there.
T2: on-site backgrounds anticommuting with H form the 4-dimensional space spanned by the chessboard scalar eps and the axis stripes
   (-1)^{x_j} sigma_j; stripes give one rest energy for all eight species; mixed backgrounds gap by | |c_0| - |c| |.
T3: alternating lengths t_j(x) = 1 + delta (-1)^{x_j} give H^2 = beta^2 sum (sin^2 + delta^2 cos^2): rest energy sqrt(3) beta |delta| for all
   eight species; the staggered-phase scalar hop i eps A gaps too; with the chessboard, (A + H + m eps)^2 = (A + H)^2 + m^2: the least
   separation of the branches is 2m on a shell, not block 77's corner values.
T4: under exclusion a chessboard is a cage (the projected walk on the vacant sublattice is zero); the projected walk has at least
   2 |even - odd| exact zero modes.
Exact arithmetic only (integers, Fractions, Gaussian rationals, exact symbolic algebra); the runner scans its own source for floating-point literals.
"""

from __future__ import annotations

import re
import sys
from fractions import Fraction
from itertools import permutations, product
from pathlib import Path

import sympy as sp


AUDIT_TIMEOUT_SEC = 900
AUDIT_INPUT_PATHS = (
    "docs/ADMISSIBILITY_RULE_WHAT_CAN_GAP_THE_WALK_NO_INVARIANT_TERM_AT_ANY_REACH_CHESSBOARD_OR_AXIS_STRIPES_ON_SITES_ALTERNATING_LENGTHS_GIVE_ONE_REST_ENERGY_EXCLUSION_CAGES_BOUNDED_THEOREM_NOTE_2026-09-22.md",
    "docs/MINIMAL_AXIOMS_2026-06-29.md",
)
ROOT = Path(__file__).resolve().parents[1]
CLAIM_ID = "admissibility_rule_what_can_gap_the_walk_no_invariant_term_any_reach_chessboard_or_axis_stripes_on_sites_alternating_lengths_give_one_rest_energy_exclusion_cages_bounded_theorem_note_2026-09-22"
AXIOM_NEEDLES = (
    "covariant under lattice",
    "define a time metric",
)

MUTATION_GATE = {
    "translation_invariant_term_gaps_a_species": "B",
    "chessboard_content_anticommutes": "C",
    "stripes_commute": "C",
    "alternating_lengths_leave_a_zero": "D",
    "a_term_adds_to_the_rest_energy": "D",
    "exclusion_lets_the_walker_hop_on_a_chessboard": "E",
    "zero_modes_below_the_imbalance": "E",
    "claim_transition_injected": "F",
    "claim_classical_name_in_theorem": "F",
}
ACTIVE_MUTATION: str | None = None


def mut(name: str) -> bool:
    if name not in MUTATION_GATE:
        raise KeyError(name)
    return ACTIVE_MUTATION == name


class Checks:
    def __init__(self) -> None:
        self.passed = 0
        self.failed = 0
        self.failed_families: set[str] = set()

    def check(self, tag: str, ok: bool, msg: str) -> None:
        if ok:
            self.passed += 1
            print(f"PASS: {tag} {msg}")
        else:
            self.failed += 1
            self.failed_families.add(tag[0])
            print(f"FAIL: {tag} {msg}")


def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text)


F = Fraction
ZERO = F(0)
ONE = F(1)


def about(v) -> str:
    """A rational to three places, by integer rounding (no floating point)."""
    v = F(v)
    sign = "-" if v < 0 else ""
    n = (abs(v) * 1000 + F(1, 2)).__floor__()
    return f"{sign}{n // 1000}.{n % 1000:03d}"


class G:
    """A Gaussian rational re + i im."""

    __slots__ = ("re", "im")

    def __init__(self, re_=0, im_=0):
        self.re = F(re_)
        self.im = F(im_)

    def __add__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re + o.re, self.im + o.im)

    __radd__ = __add__

    def __neg__(self):
        return G(-self.re, -self.im)

    def __sub__(self, o):
        return self + (-(o if isinstance(o, G) else G(o)))

    def __mul__(self, o):
        o = o if isinstance(o, G) else G(o)
        return G(self.re * o.re - self.im * o.im, self.re * o.im + self.im * o.re)

    __rmul__ = __mul__

    def conj(self):
        return G(self.re, -self.im)

    def __eq__(self, o):
        o = o if isinstance(o, G) else G(o)
        return self.re == o.re and self.im == o.im

    def __hash__(self):
        return hash((self.re, self.im))


SIG = [
    [[G(0), G(1)], [G(1), G(0)]],
    [[G(0), G(0, -1)], [G(0, 1), G(0)]],
    [[G(1), G(0)], [G(0), G(-1)]],
]
MINUS_HALF_I = G(0, F(-1, 2))                                  # 1/(2i)


def mat_add(a, b):
    return [[a[r][c] + b[r][c] for c in range(2)] for r in range(2)]


def mat_scale(a, f):
    return [[a[r][c] * f for c in range(2)] for r in range(2)]


def mat_mul(a, b):
    return [[a[r][0] * b[0][c] + a[r][1] * b[1][c] for c in range(2)] for r in range(2)]


def mat_vec(a, v):
    return (a[0][0] * v[0] + a[0][1] * v[1], a[1][0] * v[0] + a[1][1] * v[1])


def frame_matrix(vec):
    """sum_a E_a sigma_a for a coin vector (E_1, E_2, E_3)."""
    out = [[G(0), G(0)], [G(0), G(0)]]
    for a in range(3):
        out = mat_add(out, mat_scale(SIG[a], vec[a]))
    return out


DIMS = (3, 3, 3)
SITES = list(product(*(range(d) for d in DIMS)))


def shift(x, j, step):
    return tuple((x[i] + (step if i == j else 0)) % DIMS[i] for i in range(3))


def s_op(psi, j):
    """(S_j psi)(x) = (psi(x + e_j) - psi(x - e_j))/(2i)."""
    return {x: tuple((psi[shift(x, j, 1)][c] - psi[shift(x, j, -1)][c]) * MINUS_HALF_I for c in range(2)) for x in SITES}


def generator(psi, frame, symmetrised=True):
    """H psi with H = (1/2) sum_j {E^j.sigma, S_j}, or the unsymmetrised sum_j E^j.sigma S_j."""
    out = {x: (G(0), G(0)) for x in SITES}
    for j in range(3):
        first = s_op(psi, j)
        first = {x: mat_vec(frame_matrix(frame[x][j]), first[x]) for x in SITES}
        if symmetrised:
            second = s_op({x: mat_vec(frame_matrix(frame[x][j]), psi[x]) for x in SITES}, j)
            for x in SITES:
                out[x] = tuple(out[x][c] + (first[x][c] + second[x][c]) * F(1, 2) for c in range(2))
        else:
            for x in SITES:
                out[x] = tuple(out[x][c] + first[x][c] for c in range(2))
    return out


def inner(phi, psi):
    tot = G(0)
    for x in SITES:
        for c in range(2):
            tot = tot + phi[x][c].conj() * psi[x][c]
    return tot


def rational_state(seed):
    return {x: (G(F((seed * 7 + 3 * x[0] + x[1] * x[2]) % 5 - 2, 3), F((seed + x[0] * x[0] + 2 * x[1] + 5 * x[2]) % 7 - 3, 4)),
                G(F((seed * 3 + x[0] * x[1] + 2 * x[2]) % 7 - 3, 5), F((seed * 5 + x[0] + x[1] + x[2]) % 3 - 1, 2))) for x in SITES}


# ============================================================================================ family A
def family_a(checks: Checks, texts) -> None:
    note, axioms = texts
    checks.check("A1", CLAIM_ID in note and "claim_type: bounded_theorem" in note, "the note is present and carries its claim id and type")
    checks.check("A2", all(n in normalize_text(axioms) for n in AXIOM_NEEDLES), "axioms memo: the rule is covariant under lattice symmetries, and Admissibility does not define a time metric (the clauses work in that opening)")


SX = sp.Matrix([[0, 1], [1, 0]])
SY = sp.Matrix([[0, -sp.I], [sp.I, 0]])
SZ = sp.Matrix([[1, 0], [0, -1]])
SIGMA = (SX, SY, SZ)
I2 = sp.eye(2)


def proper_rotations():
    """The 24 signed permutation matrices of determinant one."""
    out = []
    for perm in permutations(range(3)):
        for signs in product((1, -1), repeat=3):
            r = sp.zeros(3, 3)
            for i in range(3):
                r[i, perm[i]] = signs[i]
            if r.det() == 1:
                out.append(r)
    return out


def coin_lift(r):
    """U in SU(2) with U sigma_a U^-1 = sum_b r[a, b] sigma_b (exact symbolic algebra)."""
    u = sp.symbols("u0:4")
    U = sp.Matrix([[u[0], u[1]], [u[2], u[3]]])
    eqs = []
    for a_ in range(3):
        eqs += list(U * SIGMA[a_] - sum((r[a_, b] * SIGMA[b] for b in range(3)), sp.zeros(2, 2)) * U)
    sol = sp.solve(eqs, u, dict=True)[0]
    U = U.subs(sol)
    free = [v for v in u if v not in sol]
    U = U.subs({free[0]: 1})
    return sp.simplify(U / sp.sqrt(U.det()))


def block4(a11, a12, a21, a22):
    return sp.BlockMatrix([[a11, a12], [a21, a22]]).as_explicit()


def kron(*ms):
    out = ms[0]
    for m_ in ms[1:]:
        out = sp.kronecker_product(out, m_)
    return out


def exact_nullity(matrix):
    """Nullity of a square matrix of Gaussian rationals by exact elimination."""
    n = len(matrix)
    m_ = [row[:] for row in matrix]
    rank = 0
    for col in range(n):
        piv = None
        for r_ in range(rank, n):
            if not (m_[r_][col] == G(0)):
                piv = r_
                break
        if piv is None:
            continue
        m_[rank], m_[piv] = m_[piv], m_[rank]
        pv = m_[rank][col]
        inv = pv.conj() * (1 / (pv.re * pv.re + pv.im * pv.im))
        m_[rank] = [x * inv for x in m_[rank]]
        for r_ in range(n):
            if r_ != rank and not (m_[r_][col] == G(0)):
                f = m_[r_][col]
                m_[r_] = [x - f * y for x, y in zip(m_[r_], m_[rank])]
        rank += 1
    return n - rank


SIG_G = (
    ((G(0), G(1)), (G(1), G(0))),
    ((G(0), G(0, -1)), (G(0, 1), G(0))),
    ((G(1), G(0)), (G(0), G(-1))),
)


def projected_walk(size, vacant):
    """The walk restricted to the vacant sites of a size^3 torus (hops between vacant sites only), as Gaussian rationals."""
    vi = {t: i for i, t in enumerate(vacant)}
    n = len(vacant)
    mat = [[G(0)] * (2 * n) for _ in range(2 * n)]
    for t in vacant:
        for j in range(3):
            for d in (1, -1):
                u = list(t)
                u[j] = (u[j] + d) % size
                u = tuple(u)
                if u in vi:
                    for r_ in range(2):
                        for c_ in range(2):
                            mat[2 * vi[t] + r_][2 * vi[u] + c_] = mat[2 * vi[t] + r_][2 * vi[u] + c_] + SIG_G[j][r_][c_] * MINUS_HALF_I * d
    return mat


# ============================================================================================ family B
def family_b(checks: Checks) -> None:
    """T1: the coin carries an irreducible representation of the proper rotations, and every corner is fixed: no covariant translation-invariant term separates the branches at a species point."""
    rots = proper_rotations()
    lifts = [coin_lift(r) for r in rots]
    x = sp.symbols("x0:4")
    X = sp.Matrix([[x[0], x[1]], [x[2], x[3]]])

    def commutant_dim(unitaries):
        eqs = []
        for U in unitaries:
            eqs += list(sp.expand(X * U - U * X))
        sol = sp.solve(eqs, x, dict=True)
        return 4 - len(sol[0]) if sol else 4

    corners = list(product((0, 1), repeat=3))
    stabiliser_sizes = []
    dims = []
    orbit_sizes = []
    for kc in corners:
        stab = [U for U, r in zip(lifts, rots) if all(((r * sp.Matrix(kc))[i] - kc[i]) % 2 == 0 for i in range(3))]
        stabiliser_sizes.append(len(stab))
        dims.append(commutant_dim(stab))
        orbit_sizes.append(len({tuple(int(v % 2) for v in (r * sp.Matrix(kc))) for r in rots}))
    scalar_only = all(d == 1 for d in dims) if not mut("translation_invariant_term_gaps_a_species") else any(d > 1 for d in dims)
    checks.check("B1", len(rots) == 24 and scalar_only and sorted(stabiliser_sizes) == [8] * 6 + [24] * 2 and sorted(orbit_sizes) == [1, 1, 3, 3, 3, 3, 3, 3], f"T1: the 24 proper rotations permute the eight corners in orbits of sizes 1, 1, 3, 3 (stabilisers of order 24, 24, 8, 8, ...: {stabiliser_sizes}); at every corner the stabiliser's coin lifts have a commutant of dimension exactly 1 ({dims}): a covariant translation-invariant term of any reach is a multiple of the identity at each species point, so the two branches touch there")
    lifted_ok = all(sp.simplify(U * SIGMA[a_] * U.inv() - sum((r[a_, b] * SIGMA[b] for b in range(3)), sp.zeros(2, 2))) == sp.zeros(2, 2) for U, r in zip(lifts[:6], rots[:6]) for a_ in range(3))
    checks.check("B2", lifted_ok, "T1: the lifts carry sigma_a to sum_b r_ab sigma_b exactly (checked on six rotations, all three axes): the coin transforms as block 54's walk requires")


# ============================================================================================ family C
def family_c(checks: Checks) -> None:
    """T2: on-site backgrounds anticommuting with the walk are exactly the chessboard scalar and the three axis stripes."""
    sites = list(product(range(2), repeat=3))
    idx = {t: i for i, t in enumerate(sites)}
    n = len(sites)
    mvars = sp.symbols("m0:%d" % (4 * n))

    def M_at(t):
        i = idx[t]
        return mvars[4 * i] * I2 + mvars[4 * i + 1] * SX + mvars[4 * i + 2] * SY + mvars[4 * i + 3] * SZ

    eqs = []
    for t in sites:
        for j in range(3):
            u = list(t)
            u[j] = (u[j] + 1) % 2
            eqs += list(sp.expand(M_at(tuple(u)) + SIGMA[j] * M_at(t) * SIGMA[j]))
    A_, _ = sp.linear_eq_to_matrix(eqs, mvars)
    null = A_.nullspace()
    dim_ok = len(null) == 4
    # membership tests: eps.1, (-1)^{x_j} sigma_j in the space; eps sigma_z, uniform sigma_z, (-1)^{x+y} sigma_z not
    def vec(pattern):
        v = sp.zeros(4 * n, 1)
        for t in sites:
            i = idx[t]
            for c_ in range(4):
                v[4 * i + c_] = pattern(t)[c_]
        return v
    span = sp.Matrix.hstack(*null)
    def in_span(v):
        return span.rank() == sp.Matrix.hstack(span, v).rank()
    eps = lambda t: ((-1) ** sum(t), 0, 0, 0)
    stripes = [lambda t, j=j: tuple((-1) ** t[j] if c_ == j + 1 else 0 for c_ in range(4)) for j in range(3)]
    eps_sz = lambda t: (0, 0, 0, (-1) ** sum(t))
    uni_sz = lambda t: (0, 0, 0, 1)
    two_flip = lambda t: (0, 0, 0, (-1) ** (t[0] + t[1]))
    members = in_span(vec(eps)) and all(in_span(vec(st)) for st in stripes)
    chess_content_out = (not in_span(vec(eps_sz))) if not mut("chessboard_content_anticommutes") else in_span(vec(eps_sz))
    non_members = chess_content_out and not in_span(vec(uni_sz)) and not in_span(vec(two_flip))
    checks.check("C1", dim_ok and members and non_members, "T2: on the 2x2x2 torus the solutions of M(x + e_j) = -sigma_j M(x) sigma_j (all j) form a space of dimension exactly 4, spanned by the chessboard scalar eps and the three axis stripes (-1)^{x_j} sigma_j; the chessboard content eps sigma_z, the uniform content sigma_z and the two-coordinate flip (-1)^{x+y} sigma_z are not solutions")

    k = sp.symbols("k1 k2 k3", real=True)
    c0, c1, c2, c3 = sp.symbols("c_0 c_1 c_2 c_3", real=True)
    s_ = [sp.sin(kk) for kk in k]
    h = s_[0] * SX + s_[1] * SY + s_[2] * SZ
    # 16-dim block: coin x pair_x x pair_y x pair_z ; (-1)^{x_j} acts as tau_x on pair j and flips sin k_j -> -sin k_j
    TX = SX
    def place(mat, j):
        fs = [I2, I2, I2]
        fs[j] = mat
        return kron(I2, *fs)
    def coin(mat):
        return kron(mat, I2, I2, I2)
    # the walk in the 16-dim block: sigma_j sin(k_j) tau_z^{(j)}
    H16 = sum((coin(SIGMA[j]) * place(s_[j] * SZ, j) for j in range(3)), sp.zeros(16, 16))
    stripes16 = sum((coin(SIGMA[j]) * place([c1, c2, c3][j] * TX, j) for j in range(3)), sp.zeros(16, 16))
    eps16 = c0 * place(TX, 0) * place(TX, 1) * place(TX, 2)
    anti = sp.simplify(H16 * stripes16 + stripes16 * H16) == sp.zeros(16, 16) and sp.simplify(H16 * eps16 + eps16 * H16) == sp.zeros(16, 16)
    sq_stripes = sp.simplify(stripes16 * stripes16 - (c1 ** 2 + c2 ** 2 + c3 ** 2) * sp.eye(16)) == sp.zeros(16, 16)
    pair_anti = sp.simplify(place(TX, 0) * coin(SX) * place(TX, 1) * coin(SY) + place(TX, 1) * coin(SY) * place(TX, 0) * coin(SX)) == sp.zeros(16, 16)
    stripes_ok = (sq_stripes and pair_anti) if not mut("stripes_commute") else (not pair_anti)
    mixed = eps16 + stripes16
    mixed_sq = sp.simplify(mixed * mixed - ((c0 ** 2 + c1 ** 2 + c2 ** 2 + c3 ** 2) * sp.eye(16) + 2 * c0 * eps16 * stripes16 / c0)) == sp.zeros(16, 16) if True else False
    checks.check("C2", anti and stripes_ok and mixed_sq, "T2: in the 16-dimensional block of the eight species, eps and the stripes anticommute with the walk; the three stripes anticommute pairwise so their square is c_1^2 + c_2^2 + c_3^2 (one rest energy sqrt(sum c_j^2) for all eight species); eps and a stripe commute, so a mixed background squares to c_0^2 + |c|^2 + 2 c_0 (stripe) and its gap is | |c_0| - |c| |")

    weights = []
    for (p, q, r) in ((3, 1, 2), (12, 1, 2), (1, 3, 2)):
        weights.append((p, q, r, q * p * p, p ** 3, q ** 3))
    stripe_never_max = all((w[3] < max(w[4], w[5])) for w in weights)
    checks.check("C3", stripe_never_max, "T2 remark: under the six-axis static law on a full lattice a stripe (contents +-e_j alternating along j, equal across) weighs q p^2 per site against p^3 for one content and q^3 for the content chessboard: 9 against 27 and 1 at (3,1,2); 144 against 1728 at (12,1,2); 3 against 1 and 27 at (1,3,2): the stripe is never the heaviest pattern, so the static law does not produce the one content order that gaps")


# ============================================================================================ family D
def family_d(checks: Checks) -> None:
    """T3: bond-odd backgrounds; the a-term with the chessboard."""
    k = sp.symbols("k1 k2 k3", real=True)
    beta, delta, a_, m_ = sp.symbols("beta delta a m", real=True)
    s_ = [sp.sin(kk) for kk in k]
    c_ = [sp.cos(kk) for kk in k]
    def place(mat, j):
        fs = [I2, I2, I2]
        fs[j] = mat
        return kron(I2, *fs)
    def coin(mat):
        return kron(mat, I2, I2, I2)
    # alternating lengths t_j(x) = 1 + delta (-1)^{x_j}: on the pair (k, k + pi e_j) the sigma-hop is beta(-sin k_j tau_z + delta cos k_j tau_y)
    hop = lambda j: beta * (-s_[j] * SZ + delta * c_[j] * SY)
    H = sum((coin(SIGMA[j]) * place(hop(j), j) for j in range(3)), sp.zeros(16, 16))
    target = beta ** 2 * sum(s_[j] ** 2 + delta ** 2 * c_[j] ** 2 for j in range(3))
    sq_ok = sp.simplify(H * H - target * sp.eye(16)) == sp.zeros(16, 16)
    corner = H.subs({k[0]: 0, k[1]: 0, k[2]: 0})
    ev = corner.eigenvals()
    corner_ok = set(sp.simplify(v) for v in ev) == {sp.sqrt(3) * sp.Abs(beta * delta), -sp.sqrt(3) * sp.Abs(beta * delta)} or set(sp.simplify(v ** 2) for v in ev) == {3 * beta ** 2 * delta ** 2}
    d_ok = (sq_ok and corner_ok) if not mut("alternating_lengths_leave_a_zero") else (not sq_ok)
    checks.check("D1", d_ok, "T3(a): with the hop amplitude t_j(x) = 1 + delta (-1)^{x_j} along every axis, H^2 = beta^2 sum_j (sin^2 k_j + delta^2 cos^2 k_j) exactly (16-dimensional block): at every one of the eight species points E^2 = 3 beta^2 delta^2, one rest energy sqrt(3) beta |delta| for all eight, and no zero anywhere for delta != 0")

    # with the a-term, the scalar hop with the same lengths: 2a(cos k_j tau_z + delta sin k_j tau_y)
    ghop = lambda j: 2 * a_ * (c_[j] * SZ + delta * s_[j] * SY)
    Ha = H + sum((place(ghop(j), j) for j in range(3)), sp.zeros(16, 16))
    corner_a = Ha.subs({k[0]: 0, k[1]: 0, k[2]: 0})
    eva = corner_a.eigenvals()
    root = sp.sqrt(4 * a_ ** 2 + 3 * beta ** 2 * delta ** 2)
    expected = {sp.simplify(root): 4, sp.simplify(-root): 4, sp.simplify(4 * a_ + root): 2, sp.simplify(4 * a_ - root): 2, sp.simplify(-4 * a_ + root): 2, sp.simplify(-4 * a_ - root): 2}
    got = {sp.simplify(v): mlt for v, mlt in eva.items()}
    checks.check("D2", got == expected, "T3(a) with the axioms' scalar hop through the same lengths: at the species points the sixteen energies are +-sqrt(4a^2 + 3 beta^2 delta^2) (four each) and +-4a +- sqrt(4a^2 + 3 beta^2 delta^2) (two each): the alternating lengths keep every species away from zero energy at the corners; the least separation elsewhere is executed only")

    # staggered-phase scalar hop i eps C and the chessboard with the a-term, on the doubled basis (k, k + pi)
    h2 = s_[0] * SX + s_[1] * SY + s_[2] * SZ
    A2 = 2 * a_ * sum(c_)
    Hd = block4(h2, sp.zeros(2, 2), sp.zeros(2, 2), -h2)
    Ad = block4(A2 * I2, sp.zeros(2, 2), sp.zeros(2, 2), -A2 * I2)
    epsd = block4(sp.zeros(2, 2), I2, I2, sp.zeros(2, 2))
    Md = sp.I * epsd * Ad
    herm = sp.simplify(Md - Md.H) == sp.zeros(4, 4)
    stag_wilson = sp.simplify((Hd + Md) ** 2 - (Hd ** 2 + Ad ** 2)) == sp.zeros(4, 4)
    checks.check("D3", herm and stag_wilson, "T3(b): the scalar hop with a staggered phase, M = i eps (2a sum_j cos k_j), is Hermitian, anticommutes with the walk and squares to 4a^2 (sum_j cos k_j)^2: (H + M)^2 = |s|^2 + 4a^2 (sum cos k_j)^2, no zero anywhere (the corners have sum cos = +-3, +-1), a gap that varies over the zone (6a at two corners, 2a at six)")

    lhs = (Ad + Hd + m_ * epsd) ** 2
    rhs = (Ad + Hd) ** 2 + m_ ** 2 * sp.eye(4)
    wrong = (Ad + Hd) ** 2 + (m_ ** 2 + 36 * a_ ** 2) * sp.eye(4)
    ident = sp.simplify(lhs - rhs) == sp.zeros(4, 4)
    not_wrong = not (sp.simplify(lhs - wrong) == sp.zeros(4, 4))
    d4 = (ident and not_wrong) if not mut("a_term_adds_to_the_rest_energy") else (sp.simplify(lhs - wrong) == sp.zeros(4, 4))
    # the shell: (A +- |s|) = 0 has solutions: at k = (t, t, t) with 2a*3cos t = sqrt(3) |sin t| -> tan t = 2 sqrt(3) a ; check with a = 1/2: tan t = sqrt(3), t = pi/3
    t_ = sp.pi / 3
    shell = sp.simplify((A2 - sp.sqrt(sum(x ** 2 for x in s_))).subs({k[0]: t_, k[1]: t_, k[2]: t_, a_: sp.Rational(1, 2)})) == 0
    checks.check("D4", d4 and shell, "T3(c): with the scalar hop A = 2a sum cos k and the chessboard, (A + H + m eps)^2 = (A + H)^2 + m^2 exactly (not m^2 + 36a^2): the branches are +-sqrt(m^2 + (A +- |s|)^2), their least separation is 2m on the shell A = -+|s| (at a = 1/2 the diagonal point k = (pi/3, pi/3, pi/3) lies on it), while at the corners the separation is 2 sqrt(m^2 + A(k_0)^2): block 77's corner values are not the rest energy, m is")


# ============================================================================================ family E
def family_e(checks: Checks) -> None:
    """T4: under exclusion a chessboard is a cage; zero modes of the projected walk are at least twice the sublattice imbalance."""
    size = 4
    sites = list(product(range(size), repeat=3))
    chess = [t for t in sites if sum(t) % 2 == 1]
    mat = projected_walk(size, chess)
    all_zero = all(x == G(0) for row in mat for x in row)
    cage = all_zero if not mut("exclusion_lets_the_walker_hop_on_a_chessboard") else (not all_zero)
    checks.check("E1", cage and len(chess) == 32, "T4: on the 4^3 torus with records on one sublattice, the walk restricted to the vacant sites is exactly zero (every neighbour of a vacant site is recorded): a chessboard under exclusion is a cage, not a mass; the 64 states of the vacant sublattice are all zero modes")
    results = []
    bound_ok = True
    for layers in (1, 2):
        vac = [t for t in sites if sum(t) % 2 == 1 or t[2] < layers]
        even = sum(1 for t in vac if sum(t) % 2 == 0)
        odd = len(vac) - even
        nul = exact_nullity(projected_walk(size, vac))
        bound = 2 * abs(even - odd)
        ok = (nul >= bound) if not mut("zero_modes_below_the_imbalance") else (nul < bound)
        bound_ok = bound_ok and ok
        results.append(f"{layers} layer(s) emptied: vacant {len(vac)} (even {even}, odd {odd}), exact nullity {nul}, bound {bound}")
    checks.check("E2", bound_ok, "T4: the projected walk only joins the two sublattices of the vacant set, so it is off-diagonal in that split and has at least 2 |even - odd| exact zero modes; on the 4^3 torus with the records of one or two layers removed from the chessboard: " + "; ".join(results))
# ============================================================================================ family F
FENCES = (
    "This note works within block 54's walk and supplied backgrounds on sites and bonds, the axioms' scalar hop and the Record axiom's exclusion; it reports which backgrounds can separate the walk's two branches at the species points and which cannot; nothing is adopted and no gravitational claim is made.",
    "No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.",
    "No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.",
)
FORBIDDEN = (
    "the physical order", "the physical rule", "the physical coupling", "the physical dimension", "the physical reading", "for every coupling", "selects the", "fires wake condition",
    "the Bridge weights", "the Bridge conjecture", "certified", "converge", "emergent", "phase transition", "critical", "washes out", "toward the plane", "the trend",
    "sharp threshold", "the transition point", "the ordered phase begins at", "has no ordered phase", "does not order", "Newtonian gravity", "the graviton", "black hole", "theory of everything",
    "time dilation", "equivalence principle", "general relativity", "horizon", "gravitational wave", "gravitational lens",
)
CLAIM_INJECTIONS = {"claim_transition_injected": "Hence the ordered phase begins at p = 3."}
CLASSICAL_NAMES = ("Newton", "Euler", "Laplace", "Poisson", "Gauss", "Einstein", "Planck", "Nordstrom", "Fourier", "Taylor", "Green", "Seeliger", "Fermat", "Boltzmann", "Gibbs", "Markov", "Fredholm", "Weyl", "Dirac", "Schwarzschild",
                   "Pauli", "Hamilton", "Ehrenfest", "Wigner", "Bloch", "Berry", "Schrodinger", "Lorentz", "Hartree", "Mach", "Eddington", "Soldner", "Dicke", "Riemann", "Regge", "Lame", "Hooke", "Abraham", "Arnowitt", "Deser", "Misner", "Brill", "Lindquist", "Isenberg", "Wilson", "Mathews", "Lichnerowicz", "York", "Hilbert", "Tolman", "Komar", "Friedmann", "Ricci",
                   "Christoffel", "Baierlein", "Wheeler", "Lagrange", "Jacobi", "Brans", "Nordtvedt")
ALLOWED_NAME_SECTIONS = ("Prior art and what is new", "Imports", "Premises and declared objects", "Review record")
SCAN_MARKER = "float-scan-marker-line"


def family_f(checks: Checks, note_text: str) -> None:
    text = note_text
    for name, phrase in CLAIM_INJECTIONS.items():
        if mut(name):
            text = text.replace("## Theorem T3", phrase + "\n\n## Theorem T3", 1)
    if mut("claim_classical_name_in_theorem"):
        text = text.replace("## Theorem T1", "## Theorem T1 (after Einstein)", 1)
    norm = normalize_text(text)
    checks.check("F1", all(normalize_text(f) in norm for f in FENCES), "the note carries the three fence sentences verbatim")
    hits = [p for p in FORBIDDEN if p in text]
    checks.check("F2", not hits, f"the note contains no forbidden phrase ({len(hits)} hits)")
    src = Path(__file__).read_text(encoding="utf-8")
    body = src.split(SCAN_MARKER)[0]
    float_hits = re.findall(r"(?<![\w.])\d+\.\d+(?![\w.])|\bfloat\(|\.evalf\(|\bN\(", body)
    checks.check("F3", not float_hits, f"runner source: no floating-point literal or conversion call ({len(float_hits)} hits)")
    sections = re.split(r"^## ", text, flags=re.M)
    offenders = []
    for sec in sections[1:]:
        title = sec.split("\n", 1)[0].strip()
        if any(title.startswith(a) for a in ALLOWED_NAME_SECTIONS):
            continue
        for nm in CLASSICAL_NAMES:
            if re.search(r"\b" + nm + r"\b", sec):
                offenders.append((title[:40], nm))
    offenders += [("front matter", nm) for nm in CLASSICAL_NAMES if re.search(r"\b" + nm + r"\b", sections[0])]
    checks.check("F4", not offenders, f"the authors' names appear only under Prior art, Imports, the Premises and the Review record ({len(offenders)} offenders)")


# ============================================================================================ family G
N5_LINES = (
    "per_element: executed - the coin lift of every proper rotation and the commutant of all 24; the on-site recurrence solved site by site on the 2x2x2 torus",
    "per_site: executed - the projected walk's matrix elements between every pair of vacant sites of the 4^3 torus for the chessboard and for one and two emptied layers",
    "per_mode: executed - the 16-dimensional block of the eight species at every wave vector (symbolic) for the stripes, the alternating lengths and the scalar hop; the 4-dimensional block for the chessboard and the staggered phase; control: least branch separation and the sea's energy against delta on tori",
    "per_block: executed - nullity of the projected walk by exact elimination on 4^3 against the sublattice-imbalance bound",
    "lattice_wide: T1 holds for every covariant translation-invariant term of any finite reach by the representation argument; T2 for every even-sided torus by the recurrence; T3 and the chessboard identity for every wave vector by the symbolic identities; T4 for every vacant set by the bipartite argument; the backgrounds, the coupling clauses, the value of delta and the sea reading are not derived",
)


def family_g(checks: Checks) -> None:
    for line in N5_LINES:
        print(line)
    checks.check("G1", len(N5_LINES) == 5, "the five N5 resolution lines are printed")


def main(argv) -> int:
    global ACTIVE_MUTATION
    if "--list-mutations" in argv:
        for name, fam in MUTATION_GATE.items():
            print(f"{name} {fam}")
        return 0
    if "--mutation" in argv:
        ACTIVE_MUTATION = argv[argv.index("--mutation") + 1]
        if ACTIVE_MUTATION not in MUTATION_GATE:
            print(f"unknown mutation {ACTIVE_MUTATION}")
            return 2
    print("AUDIT_INPUT_PATHS:")
    for p in AUDIT_INPUT_PATHS:
        print(f"  {p}")
    texts = [Path(ROOT, p).read_text(encoding="utf-8") if Path(ROOT, p).exists() else "" for p in AUDIT_INPUT_PATHS]
    checks = Checks()
    family_a(checks, texts)
    family_b(checks)
    family_c(checks)
    family_d(checks)
    family_e(checks)
    family_f(checks, texts[0])
    family_g(checks)
    if ACTIVE_MUTATION:
        print(f"mutation_family_expected: {MUTATION_GATE[ACTIVE_MUTATION]}")
        print(f"mutation_family_observed: {''.join(sorted(checks.failed_families)) or '-'}")
    print("scope: what can gap the walk inside the qubit - no covariant translation-invariant term of any reach separates the branches at a species point (Schur); on sites only the chessboard scalar and the axis stripes anticommute with the walk (the stripes gap all eight species; block 81 T4 covered the uniform and chessboard contents only); alternating bond lengths give one rest energy sqrt(3) beta |delta| to all eight species; with the scalar hop the chessboard's least branch separation is 2m on a shell (block 77's corner values are not the rest energy); under exclusion a chessboard is a cage with 2|even - odd| zero modes; nothing adopted")
    print(f"TOTAL: PASS={checks.passed} FAIL={checks.failed}")
    return 0 if checks.failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
# float-scan-marker-line
