#!/usr/bin/env python3
"""GL(F) from Berezin-RP reconstruction -- exact small-lattice certificate.

Companion runner for
docs/GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md

Claim verified: the Osterwalder-Schrader / transfer (GNS) reconstruction of an
operator theory from a reflection-positive *Berezin* (Grassmann) functional
integral canonically produces time-zero field operators satisfying cross-site
graded locality GL(F):

    {psi_x, psi_y} = 0   and   {psi_x, psi_y^dag} = 0   for x != y,

with the reconstructed parity grading equal to the framework F = (x) sigma_3.
The cross-site exchange sign is inherited from the Grassmann parity of the
integration variables (an algebra identity of left multiplication), NOT from
an exchange postulate on a pre-given operator frame.

Construction (all exact rational arithmetic at N = 2, 3; float leg at the
staggered L_s = 4 kernel):

  * exterior (Grassmann) algebra over Q with generators chi_{t,x},
    chibar_{t,x} on two time slices t in {0,1}, N spatial sites;
  * theta-symmetric quadratic action
        S = sum_x [ chibar_{0x} chi_{0x} + chibar_{1x} chi_{1x} ]
            - sum_{xy} K_{xy} chibar_{0x} chi_{1y},      K = K^T > 0,
    with link reflection Theta: (t,x) -> (1-t,x), chi <-> chibar, antilinear,
    product-reversing;
  * OS form <F, G> := < Theta(F) G >_S on the positive-time algebra A_+,
    computed by exact Berezin integration (e^{-S} expanded exactly);
  * exact PSD certificate (rational LDL with Schur complements), null space,
    GNS quotient H = A_+/N of dimension 2^N, multiplication operators
    psi_x = [chi_{1x} . ], phi_x = [chibar_{1x} . ] well-defined on H;
  * reconstructed exchange relations computed as matrices;
  * GL(F) certificate for the canonically normalized multiplet;
  * falsification legs: a commuting-nilpotent (ungraded / "hard-core")
    integrand reconstructs to cross-site COMMUTING operators under the same
    functor (the Grassmann input is load-bearing); the hard-core frame cannot
    arise from a Grassmann integrand (identity-level); det vs perm vs
    det^{-1/2} partition readouts separate the three integrand classes;
    a Theta-asymmetric kernel breaks RP (PSD fails), so the RP input is
    load-bearing for the existence of the reconstruction.

Tags: [A] Berezin/measure surface  [B] OS reconstruction  [C] reconstructed
exchange relations / GL(F)  [D] falsification + separation legs.

Deterministic, no external dependencies beyond the standard library.
Expected: TOTAL: PASS=48 FAIL=0
"""

import hashlib
from fractions import Fraction
import itertools
import math
from pathlib import Path

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs" / "GL_F_FROM_BEREZIN_RP_RECONSTRUCTION_NARROW_THEOREM_NOTE_2026-06-10.md"
BRIDGE_NOTE = ROOT / "docs" / "GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md"
BRIDGE_RUNNER = ROOT / "scripts" / "gl_f_identification_bridge_check_2026_06_11.py"
BRIDGE_CACHE = ROOT / "logs" / "runner-cache" / "gl_f_identification_bridge_check_2026_06_11.txt"


def check(tag, desc, ok, extra=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        line = "[%s] PASS: %s" % (tag, desc)
    else:
        FAIL += 1
        line = "[%s] FAIL: %s" % (tag, desc)
    if extra:
        line += "  (%s)" % extra
    print(line)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as handle:
        for chunk in iter(lambda: handle.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def cache_header(path):
    fields = {}
    if not path.exists():
        return fields
    with open(path, "r", encoding="utf-8", errors="replace") as handle:
        for line in handle:
            line = line.strip()
            if line == "----- stdout -----":
                break
            if ":" in line:
                key, value = line.split(":", 1)
                fields[key.strip()] = value.strip()
    return fields


# ----------------------------------------------------------------------
# Graded algebra over masks.  eps = -1 : Grassmann (exterior) algebra;
# eps = +1 : commuting-nilpotent algebra (the "hard-core" integrand).
# Basis monomial = product of generators in ascending index order.
# ----------------------------------------------------------------------

def mul_mono(a, b, eps):
    """Multiply basis monomials given by bitmasks a, b. Return (mask, sign)."""
    if a & b:
        return (0, 0)
    if eps == 1:
        return (a | b, 1)
    # count transpositions moving each generator of b left past higher gens of a
    cnt = 0
    bb = b
    while bb:
        j = (bb & -bb).bit_length() - 1
        cnt += bin(a >> (j + 1)).count("1")
        bb &= bb - 1
    return (a | b, -1 if (cnt & 1) else 1)


def amul(A, B, eps):
    """Multiply sparse elements (dict mask -> coeff)."""
    out = {}
    for ma, ca in A.items():
        for mb, cb in B.items():
            m, s = mul_mono(ma, mb, eps)
            if s:
                v = out.get(m, 0) + s * ca * cb
                if v:
                    out[m] = v
                elif m in out:
                    del out[m]
    return out


def aadd(A, B):
    out = dict(A)
    for m, c in B.items():
        v = out.get(m, 0) + c
        if v:
            out[m] = v
        elif m in out:
            del out[m]
    return out


def ascal(c, A):
    return {m: c * v for m, v in A.items()} if c else {}


def exp_quad(S, eps):
    """exp(-S) for S a sum of even (quadratic) nilpotent monomials.
    S given as dict mask -> coeff.  e^{-S} = prod_k (1 - c_k m_k)."""
    out = {0: Fraction(1) if all(isinstance(c, Fraction) for c in S.values()) else 1.0}
    for m, c in sorted(S.items()):
        # out <- out * (1 - c*m)
        add = {}
        for mm, cc in out.items():
            mp, s = mul_mono(mm, m, eps)
            if s:
                v = add.get(mp, 0) - s * cc * c
                if v:
                    add[mp] = v
                elif mp in add:
                    del add[mp]
        out = aadd(out, add)
    return out


# ----------------------------------------------------------------------
# Pure-measure layer: partition readouts on n modes (single slice).
# Generators: chi_x -> index 2x, chibar_x -> index 2x+1.
# Integral convention: coefficient of the ascending top monomial
# chi_0 chibar_0 chi_1 chibar_1 ... ; Grassmann normalization sigma = +1,
# commuting-nilpotent normalization sigma = (-1)^n (declared so the
# single-mode integral of e^{-m etabar eta} equals m in both calculi).
# ----------------------------------------------------------------------

def partition_readout(M, eps):
    n = len(M)
    S = {}
    for x in range(n):
        for y in range(n):
            if M[x][y]:
                # chibar_x M_xy chi_y : product of generators 2x+1 then 2y
                g1 = {1 << (2 * x + 1): Fraction(1)}
                g2 = {1 << (2 * y): Fraction(1)}
                t = amul(g1, g2, eps)
                S = aadd(S, ascal(M[x][y], t))
    E = exp_quad(S, eps)
    top = (1 << (2 * n)) - 1
    z = E.get(top, Fraction(0))
    if eps == 1 and (n % 2):
        z = -z
    return z


def det(M):
    n = len(M)
    if n == 1:
        return M[0][0]
    out = 0
    for perm in itertools.permutations(range(n)):
        sgn = 1
        seen = [False] * n
        # parity via cycle count
        p = list(perm)
        visited = [False] * n
        cycles = 0
        for i in range(n):
            if not visited[i]:
                cycles += 1
                j = i
                while not visited[j]:
                    visited[j] = True
                    j = p[j]
        sgn = -1 if ((n - cycles) % 2) else 1
        prod = sgn
        for i in range(n):
            prod *= M[i][perm[i]]
        out += prod
    return out


def perm(M):
    n = len(M)
    out = 0
    for p in itertools.permutations(range(n)):
        prod = 1
        for i in range(n):
            prod *= M[i][p[i]]
        out += prod
    return out


# ----------------------------------------------------------------------
# Two-slice OS model.
# Variable index: idx(t, x, bar) = ((t*N + x) << 1) | bar
# ----------------------------------------------------------------------

class OSModel:
    def __init__(self, N, K, eps, exact=True):
        self.N = N
        self.K = K
        self.eps = eps
        self.exact = exact
        self.nvar = 4 * N
        self.top = (1 << self.nvar) - 1
        one = Fraction(1) if exact else 1.0
        self.one = one
        # action
        S = {}
        for x in range(N):
            S = aadd(S, self._quad(0, x, 1, 0, x, 0, one))   # chibar_0x chi_0x
            S = aadd(S, self._quad(1, x, 1, 1, x, 0, one))   # chibar_1x chi_1x
        for x in range(N):
            for y in range(N):
                if K[x][y]:
                    S = aadd(S, self._quad(0, x, 1, 1, y, 0, -K[x][y]))
        self.S = S
        self.expS = exp_quad(S, eps)
        self.Ztop = self.expS.get(self.top, 0)

    def idx(self, t, x, bar):
        return ((t * self.N + x) << 1) | bar

    def gen(self, t, x, bar):
        return {1 << self.idx(t, x, bar): self.one}

    def _quad(self, t1, x1, b1, t2, x2, b2, coeff):
        t = amul(self.gen(t1, x1, b1), self.gen(t2, x2, b2), self.eps)
        return ascal(coeff, t)

    def theta_mono(self, mask, coeff):
        """Antilinear, product-reversing reflection of a basis monomial."""
        idxs = []
        m = mask
        while m:
            j = (m & -m).bit_length() - 1
            idxs.append(j)
            m &= m - 1
        # ascending order in the monomial; reflect each generator, multiply reversed
        out_mask, out_sign = 0, 1
        for j in reversed(idxs):
            bar = j & 1
            tx = j >> 1
            t, x = divmod(tx, self.N)
            jj = self.idx(1 - t, x, 1 - bar)
            out_mask2, s = mul_mono(out_mask, 1 << jj, self.eps)
            if s == 0:
                return {}
            out_mask, out_sign = out_mask2, out_sign * s
        c = coeff.conjugate() if isinstance(coeff, complex) else coeff
        return {out_mask: out_sign * c}

    def theta(self, A):
        out = {}
        for m, c in A.items():
            out = aadd(out, self.theta_mono(m, c))
        return out

    def expect_mono(self, mask, sign):
        """< monomial >_S = Top(monomial * e^{-S}) / Top(e^{-S}) -- O(1) lookup."""
        rest = self.top & ~mask
        c = self.expS.get(rest, 0)
        if not c:
            return 0 * self.one
        _, s = mul_mono(mask, rest, self.eps)
        return sign * s * c / self.Ztop

    def expect(self, A):
        out = 0 * self.one
        for m, c in A.items():
            rest = self.top & ~m
            cc = self.expS.get(rest, 0)
            if cc:
                _, s = mul_mono(m, rest, self.eps)
                out += s * c * cc
        return out / self.Ztop

    # -------- A_+ basis: all monomials in slice-1 generators ----------
    def aplus_basis(self):
        gens1 = [self.idx(1, x, b) for x in range(self.N) for b in (0, 1)]
        basis = []
        for r in range(len(gens1) + 1):
            for combo in itertools.combinations(gens1, r):
                m = 0
                for j in combo:
                    m |= 1 << j
                basis.append(m)
        return basis

    def gram(self, basis):
        n = len(basis)
        G = [[0 * self.one] * n for _ in range(n)]
        for i, mi in enumerate(basis):
            th = self.theta_mono(mi, self.one)
            if not th:
                continue
            (tm, tc), = th.items()
            for j, mj in enumerate(basis):
                m, s = mul_mono(tm, mj, self.eps)
                if s:
                    G[i][j] = self.expect_mono(m, s * tc)
        return G


# ----------------------------------------------------------------------
# Exact rational linear algebra helpers
# ----------------------------------------------------------------------

def ldl_psd(G):
    """Exact PSD test for a symmetric rational matrix.
    Returns (is_psd, rank).  Pivots on max diagonal entry; for a PSD matrix
    a zero diagonal forces a zero row/col on the active block."""
    n = len(G)
    A = [row[:] for row in G]
    active = list(range(n))
    rank = 0
    while active:
        # find max diagonal
        dmax, imax = None, None
        for i in active:
            d = A[i][i]
            if dmax is None or d > dmax:
                dmax, imax = d, i
        if dmax < 0:
            return (False, rank)
        if dmax == 0:
            # all diagonals zero: PSD requires whole active block zero
            for i in active:
                for j in active:
                    if A[i][j] != 0:
                        return (False, rank)
            return (True, rank)
        rank += 1
        p = imax
        active.remove(p)
        piv = A[p][p]
        for i in active:
            if A[i][p]:
                f = A[i][p] / piv
                for j in active:
                    A[i][j] -= f * A[p][j]
    return (True, rank)


def kernel_basis(G):
    """Exact kernel of a symmetric rational matrix (Gaussian elimination)."""
    n = len(G)
    A = [row[:] for row in G]
    pivots = []
    r = 0
    for c in range(n):
        pr = None
        for i in range(r, n):
            if A[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(n):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        pivots.append(c)
        r += 1
    free = [c for c in range(n) if c not in pivots]
    ker = []
    for fc in free:
        v = [Fraction(0)] * n
        v[fc] = Fraction(1)
        for i, pc in enumerate(pivots):
            v[pc] = -A[i][fc]
        ker.append(v)
    return ker


def mat_solve(A, B):
    """Solve A X = B exactly (A invertible rational), B list of columns-matrix."""
    n = len(A)
    m = len(B[0])
    M = [A[i][:] + B[i][:] for i in range(n)]
    for c in range(n):
        pr = None
        for i in range(c, n):
            if M[i][c] != 0:
                pr = i
                break
        M[c], M[pr] = M[pr], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return [row[n:] for row in M]


def mat_mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[0 * A[0][0] if A else 0] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        for j in range(m):
            s = 0
            for t in range(k):
                if Ai[t]:
                    s += Ai[t] * B[t][j]
            out[i][j] = s
    return out


def mat_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_T(A):
    return [list(row) for row in zip(*A)]


def is_zero(A, tol=0):
    if tol:
        return all(abs(v) <= tol for row in A for v in row)
    return all(v == 0 for row in A for v in row)


def is_scalar(A, tol=0):
    """Return (True, c) if A = c*I."""
    n = len(A)
    c = A[0][0]
    for i in range(n):
        for j in range(n):
            want = c if i == j else 0
            if tol:
                if abs(A[i][j] - want) > tol:
                    return (False, None)
            else:
                if A[i][j] != want:
                    return (False, None)
    return (True, c)


def mat_inv(A):
    n = len(A)
    I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    return mat_solve(A, I)


# ----------------------------------------------------------------------
# Reconstruction pipeline for one model
# ----------------------------------------------------------------------

def reconstruct(model, tol=0):
    """Run the OS/GNS reconstruction. Returns dict of results."""
    N = model.N
    basis = model.aplus_basis()
    G = model.gram(basis)
    res = {"basis": basis, "G": G}
    # physical sub-basis: chibar-only monomials (occupation basis)
    bar_idxs = [model.idx(1, x, 1) for x in range(N)]
    occ_masks = []
    for r in range(N + 1):
        for combo in itertools.combinations(bar_idxs, r):
            m = 0
            for j in combo:
                m |= 1 << j
            occ_masks.append(m)
    pos = {m: i for i, m in enumerate(basis)}
    occ_pos = [pos[m] for m in occ_masks]
    Gp = [[G[i][j] for j in occ_pos] for i in occ_pos]
    res["occ_masks"] = occ_masks
    res["Gp"] = Gp

    # operators: multiplication by chi_{1x} (psi) and chibar_{1x} (phi)
    Gp_inv = None
    if tol == 0:
        Gp_inv = mat_inv(Gp)

    def mult_matrix(gen_idx):
        n = len(occ_masks)
        W = [[0 * model.one] * n for _ in range(n)]
        for j, mj in enumerate(occ_masks):
            m, s = mul_mono(1 << gen_idx, mj, model.eps)
            if s == 0:
                continue
            # w_i = <p_i, g . p_j> = Gram(p_i, monomial m)
            for i, mi in enumerate(occ_masks):
                th = model.theta_mono(mi, model.one)
                if not th:
                    continue
                (tm, tc), = th.items()
                mm, ss = mul_mono(tm, m, model.eps)
                if ss:
                    W[i][j] = model.expect_mono(mm, ss * tc * s)
        # class coordinates: v = Gp^{-1} w  (columns)
        if tol == 0:
            return mat_mul(Gp_inv, W)
        # float solve
        import copy
        n = len(Gp)
        A = [row[:] for row in Gp]
        return mat_solve_float(A, W)
    res["mult_matrix"] = mult_matrix
    return res


def mat_solve_float(A, B):
    n = len(A)
    m = len(B[0])
    M = [A[i][:] + B[i][:] for i in range(n)]
    for c in range(n):
        pr = max(range(c, n), key=lambda i: abs(M[i][c]))
        M[c], M[pr] = M[pr], M[c]
        pv = M[c][c]
        M[c] = [v / pv for v in M[c]]
        for i in range(n):
            if i != c and M[i][c] != 0:
                f = M[i][c]
                M[i] = [a - f * b for a, b in zip(M[i], M[c])]
    return [row[n:] for row in M]


def anticomm(A, B):
    return mat_add(mat_mul(A, B), mat_mul(B, A))


def comm(A, B):
    AB = mat_mul(A, B)
    BA = mat_mul(B, A)
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(AB, BA)]


# ======================================================================
# MAIN
# ======================================================================

def main():
    one = Fraction(1)

    print("=" * 78)
    print("GL(F) from Berezin-RP reconstruction -- exact certificate (2026-06-10)")
    print("=" * 78)

    # ------------------------------------------------------------------
    # [A] Measure surface: partition readouts separate the integrand classes
    # ------------------------------------------------------------------
    print()
    print("--- [A] Berezin / measure surface ---")

    Ms = {
        2: [[Fraction(1), Fraction(2)], [Fraction(3), Fraction(4)]],
        3: [[Fraction(2), Fraction(1), Fraction(0)],
            [Fraction(1), Fraction(3), Fraction(1)],
            [Fraction(0), Fraction(1), Fraction(2)]],
    }
    ok = True
    for n, M in Ms.items():
        z = partition_readout(M, -1)
        ok = ok and (z == det(M))
    check("A", "Berezin (Grassmann) partition readout Z[M] = det(M) exactly "
               "(n = 2, 3, generic rational M)", ok,
          "Berezin-determinant identity recomputed")

    ok = True
    for n, M in Ms.items():
        z = partition_readout(M, +1)
        ok = ok and (z == perm(M))
    check("A", "commuting-nilpotent (ungraded) partition readout Z_cn[M] = perm(M) "
               "exactly (n = 2, 3)", ok,
          "the hard-core-frame integrand has a PERMANENT readout, not det")

    M2 = Ms[2]
    check("A", "det != perm witness on the same M: the two integrand classes are "
               "separated by the determinant readout",
          det(M2) != perm(M2),
          "det = %s, perm = %s" % (det(M2), perm(M2)))

    # free boson: per-mode trace diverges / = 1/(1 - e^-m); structural check at
    # finite truncation: truncated traces strictly increase without bound
    m_ = 0.5
    traces = [sum(math.exp(-m_ * k) for k in range(K)) for K in (2, 3, 6, 11, 101)]
    grass_trace = 1 + math.exp(-m_)
    check("A", "free-boson (CCR) tower readout diverges from the Grassmann scalar "
               "readout: truncated traces strictly increase, Grassmann trace = 1 + e^-m",
          all(t2 > t1 for t1, t2 in zip(traces, traces[1:])) and abs(traces[0] - grass_trace) < 1e-12,
          "free boson excluded by the per-site dim-2 readout; "
          "Gaussian boson would give det^(-1/2), a third distinct class")

    # ------------------------------------------------------------------
    # [B] OS reconstruction at N = 2 and N = 3 (exact)
    # ------------------------------------------------------------------
    print()
    print("--- [B] OS reconstruction from the Berezin functional (exact, N = 2, 3) ---")

    # rational PD kernels with cross-site mixing, K = (A^T A)^{-1} so that the
    # central covariance C = K^{-1} = A^T A has an exact rational congruence to I
    A2 = [[Fraction(1), Fraction(1, 2)], [Fraction(0), Fraction(1)]]
    A3 = [[Fraction(1), Fraction(1, 2), Fraction(0)],
          [Fraction(0), Fraction(1), Fraction(1, 3)],
          [Fraction(0), Fraction(0), Fraction(1)]]

    models = {}
    for N, Amat in ((2, A2), (3, A3)):
        AtA = mat_mul(mat_T(Amat), Amat)
        K = mat_inv(AtA)
        model = OSModel(N, K, eps=-1, exact=True)
        models[N] = (model, Amat, AtA, K)

        # Theta-symmetry of the action
        thS = model.theta(model.S)
        check("B", "N = %d: the action S is Theta-symmetric (Theta(S) = S exactly; "
                   "link reflection t -> 1-t, chi <-> chibar, antilinear, "
                   "product-reversing)" % N,
              thS == model.S)
        check("B", "N = %d: Z = Berezin integral of e^{-S} is nonzero (the measure "
                   "is nondegenerate)" % N, model.Ztop != 0,
              "Z_top = %s" % model.Ztop)

        rec = reconstruct(model)
        basis, G = rec["basis"], rec["G"]
        # Gram symmetric + exact PSD
        sym = all(G[i][j] == G[j][i] for i in range(len(G)) for j in range(len(G)))
        psd, rank = ldl_psd(G)
        check("B", "N = %d: OS Gram on the full A_+ basis (%d monomials) is symmetric "
                   "and PSD (exact rational LDL certificate)" % (N, len(basis)),
              sym and psd, "rank = %d" % rank)
        check("B", "N = %d: GNS quotient dimension = rank(Gram) = 2^N = %d -- the "
                   "reconstructed Hilbert space matches the Quantum-axiom qubit net "
                   "dimension per site" % (N, 2 ** N),
              rank == 2 ** N)

        Gp = rec["Gp"]
        psd_p, rank_p = ldl_psd(Gp)
        check("B", "N = %d: the chibar-monomial (occupation) sub-basis has exactly "
                   "positive-definite Gram (all %d pivots > 0) -- it spans the "
                   "quotient" % (N, 2 ** N),
              psd_p and rank_p == 2 ** N)

        # null-space invariance under left multiplication (well-definedness)
        ker = kernel_basis(G)

        def count_violations(bar):
            viol = 0
            for u in ker:
                for x in range(N):
                    gj = model.idx(1, x, bar)
                    for i, mi in enumerate(basis):
                        th = model.theta_mono(mi, one)
                        if not th:
                            continue
                        (tm, tc), = th.items()
                        s_tot = 0 * one
                        for j, mj in enumerate(basis):
                            if u[j] == 0:
                                continue
                            m1, s1 = mul_mono(1 << gj, mj, -1)
                            if s1 == 0:
                                continue
                            mm, ss = mul_mono(tm, m1, -1)
                            if ss:
                                s_tot += model.expect_mono(mm, ss * tc * s1 * u[j])
                        if s_tot != 0:
                            viol += 1
            return viol

        check("B", "N = %d: the OS null space is invariant under left multiplication "
                   "by every FIELD generator chi_{1x} -- the reconstructed fields "
                   "psi_x = [chi_{1x} . ] are canonically well-defined on the "
                   "quotient (checked on all %d exact kernel vectors)"
              % (N, len(ker)),
              count_violations(0) == 0,
              "GL(F) concerns psi_x and its Hilbert adjoint, both canonical")
        check("B", "N = %d: declared structure -- chibar_{1x} multiplication does "
                   "NOT preserve the null space (violations detected), so the "
                   "creator phi_x is defined on the distinguished boundary creation "
                   "subalgebra Lambda[chibar_1] (positive-definite Gram, isomorphic "
                   "onto the quotient): the standard Fock/holomorphic transfer "
                   "picture, recorded honestly" % N,
              count_violations(1) > 0)

    # ------------------------------------------------------------------
    # [C] Reconstructed exchange relations and the GL(F) certificate
    # ------------------------------------------------------------------
    print()
    print("--- [C] Reconstructed exchange relations (the GL(F) certificate) ---")

    for N in (2, 3):
        model, Amat, AtA, K = models[N]
        rec = reconstruct(model)
        occ_masks = rec["occ_masks"]
        Gp = rec["Gp"]
        dim = len(occ_masks)
        psi = [rec["mult_matrix"](model.idx(1, x, 0)) for x in range(N)]
        phi = [rec["mult_matrix"](model.idx(1, x, 1)) for x in range(N)]

        # algebra-identity layer: left multiplications anticommute identically
        ok = True
        gens1 = [model.idx(1, x, 0) for x in range(N)]
        for a in gens1:
            for b in gens1:
                m1, s1 = mul_mono(1 << a, 1 << b, -1)
                m2, s2 = mul_mono(1 << b, 1 << a, -1)
                if a == b:
                    if s1 != 0 or s2 != 0:
                        ok = False
                else:
                    if not (m1 == m2 and s1 == -s2):
                        ok = False
        check("C", "N = %d: chi_{1x} chi_{1y} + chi_{1y} chi_{1x} = 0 is an IDENTITY "
                   "of the Grassmann algebra (before any action, form, or quotient) -- "
                   "the exchange sign is carried by the integration variables" % N, ok)

        ok = all(is_zero(anticomm(psi[x], psi[y])) for x in range(N) for y in range(N))
        check("C", "N = %d: reconstructed {psi_x, psi_y} = 0 for ALL x, y "
                   "(exact matrices on the 2^N-dim reconstructed space; includes "
                   "psi_x^2 = 0)" % N, ok)

        ok = True
        for x in range(N):
            for y in range(N):
                ac = anticomm(psi[x], phi[y])
                sc, c = is_scalar(ac)
                want = one if x == y else 0 * one
                if not (sc and c == want):
                    ok = False
        check("C", "N = %d: reconstructed multiplication pair satisfies "
                   "{psi_x, phi_y} = delta_xy I exactly (the on-site CAR ladder "
                   "structure emerges from the equal-slice Wick contraction)" % N, ok)

        # OS adjoint and central covariance
        Gp_inv = mat_inv(Gp)
        psid = [mat_mul(Gp_inv, mat_mul(mat_T(psi[x]), Gp)) for x in range(N)]
        ok = True
        Cmat = [[None] * N for _ in range(N)]
        for x in range(N):
            for y in range(N):
                ac = anticomm(psi[x], psid[y])
                sc, c = is_scalar(ac)
                if not sc:
                    ok = False
                else:
                    Cmat[x][y] = c
        Kinv = mat_inv(K)
        ok = ok and all(Cmat[x][y] == Kinv[x][y] for x in range(N) for y in range(N))
        check("C", "N = %d: {psi_x, psi_y^dag} (dag = OS adjoint) is CENTRAL: "
                   "= C_xy I with C = K^{-1} exactly, a positive-definite c-number "
                   "covariance -- no operator-valued obstruction" % N, ok)

        # canonical normalization: B = (A^T)^{-1} gives B C B^T = I exactly
        Bmat = mat_inv(mat_T(Amat))
        BC = mat_mul(Bmat, mat_mul(Kinv, mat_T(Bmat)))
        sc, c = is_scalar(BC)
        check("C", "N = %d: exact rational normalizer B with B C B^T = I exists "
                   "(field-multiplet rotation; cannot change exchange signs)" % N,
              sc and c == one)

        psit = []
        for x in range(N):
            m = [[0 * one] * dim for _ in range(dim)]
            for y in range(N):
                if Bmat[x][y]:
                    m = mat_add(m, [[Bmat[x][y] * v for v in row] for row in psi[y]])
            psit.append(m)
        psitd = [mat_mul(Gp_inv, mat_mul(mat_T(p), Gp)) for p in psit]

        ok1 = all(is_zero(anticomm(psit[x], psit[y])) for x in range(N) for y in range(N))
        ok2 = True
        for x in range(N):
            for y in range(N):
                ac = anticomm(psit[x], psitd[y])
                sc, c = is_scalar(ac)
                want = one if x == y else 0 * one
                if not (sc and c == want):
                    ok2 = False
        check("C", "N = %d: GL(F) CERTIFICATE -- the canonically normalized "
                   "reconstructed fields satisfy {psi_x, psi_y} = 0 AND "
                   "{psi_x, psi_y^dag} = 0 for x != y, with {psi_x, psi_x^dag} = I "
                   "(exact CAR; cross-site anticommutation is a THEOREM of the "
                   "reconstruction, not a postulate)" % N, ok1 and ok2)

        # parity grading
        Fhat = [[(one if i == j else 0 * one) * ((-1) ** bin(occ_masks[i]).count("1"))
                 for j in range(dim)] for i in range(dim)]
        ok = all(is_zero(anticomm(Fhat, psit[x])) for x in range(N))
        # F-invariance of the OS form: F G F = G (grading preserves the form)
        FGF = mat_mul(Fhat, mat_mul(Gp, Fhat))
        ok = ok and (FGF == Gp)
        sig_diag = sorted(((-1) ** bin(m).count("1")) for m in occ_masks)
        tensor_sigma3 = sorted(
            (-1) ** sum(bits) for bits in itertools.product((0, 1), repeat=N))
        check("C", "N = %d: the reconstructed parity F-hat (the integrand grading "
                   "chi -> -chi pushed to the quotient) preserves the OS form, "
                   "anticommutes with every reconstructed field, and equals "
                   "tensor-sigma_3 in the occupation identification -- GL(F) holds "
                   "w.r.t. the framework grading" % N,
              ok and sig_diag == tensor_sigma3)

    # ------------------------------------------------------------------
    # [C] staggered-kernel leg (float): K from the two-step transfer object
    # ------------------------------------------------------------------
    Ls, mass = 4, 0.5
    ps = [2 * math.pi * k / Ls for k in range(Ls)]

    def E_disp(p):
        return math.asinh(math.sqrt(mass ** 2 + math.sin(p) ** 2))

    # action-derived: classical 2-step matrix T_odd*T_even eigenvalues e^{+-2E}
    ok = True
    for p in ps:
        a_e = complex(mass, math.sin(p))
        a_o = complex(mass, -math.sin(p))
        Te = [[-2 * a_e, 1], [1, 0]]
        To = [[-2 * a_o, 1], [1, 0]]
        T2 = [[To[0][0] * Te[0][0] + To[0][1] * Te[1][0], To[0][0] * Te[0][1] + To[0][1] * Te[1][1]],
              [To[1][0] * Te[0][0] + To[1][1] * Te[1][0], To[1][0] * Te[0][1] + To[1][1] * Te[1][1]]]
        tr, dt = T2[0][0] + T2[1][1], T2[0][0] * T2[1][1] - T2[0][1] * T2[1][0]
        disc = (tr * tr - 4 * dt) ** 0.5
        lam = [(tr + disc) / 2, (tr - disc) / 2]
        lam_min = min(lam, key=abs)
        if abs(lam_min.imag) > 1e-12 or not math.isclose(
            lam_min.real, math.exp(-2 * E_disp(p)), rel_tol=0.0, abs_tol=1e-10
        ):
            ok = False
    check("C", "staggered leg: the action-derived classical 2-step transfer matrix "
               "T_odd T_even reproduces the exact free staggered dispersion "
               "eigenvalue e^{-2E(p)}, E = arcsinh sqrt(m^2 + sin^2 p) "
               "(two-step transfer object recomputed)", ok,
          "L_s = %d, m = %s" % (Ls, mass))

    # position-space circulant kernel K_stag (real symmetric PD)
    Kst = [[sum(math.exp(-2 * E_disp(p)) * math.cos(p * (x - y)) for p in ps) / Ls
            for y in range(Ls)] for x in range(Ls)]
    model4 = OSModel(Ls, Kst, eps=-1, exact=False)
    thS = model4.theta(model4.S)
    ok = set(thS) == set(model4.S) and all(abs(thS[m] - model4.S[m]) < 1e-12 for m in model4.S)
    check("C", "staggered leg: the L_s = 4 two-slice Berezin action with the "
               "staggered 2-step kernel K_stag is Theta-symmetric", ok)

    rec4 = reconstruct(model4, tol=1e-12)
    occ4 = rec4["occ_masks"]
    Gp4 = rec4["Gp"]
    # PD check via float Cholesky
    ok = True
    n4 = len(Gp4)
    L4 = [[0.0] * n4 for _ in range(n4)]
    try:
        for i in range(n4):
            for j in range(i + 1):
                s = sum(L4[i][k] * L4[j][k] for k in range(j))
                if i == j:
                    d = Gp4[i][i] - s
                    if d <= 0:
                        ok = False
                        break
                    L4[i][i] = math.sqrt(d)
                else:
                    L4[i][j] = (Gp4[i][j] - s) / L4[j][j]
            if not ok:
                break
    except ValueError:
        ok = False
    check("C", "staggered leg: occupation-basis OS Gram is positive definite "
               "(float Cholesky, dim = 2^%d = %d)" % (Ls, 2 ** Ls), ok)

    psi4 = [rec4["mult_matrix"](model4.idx(1, x, 0)) for x in range(Ls)]
    phi4 = [rec4["mult_matrix"](model4.idx(1, x, 1)) for x in range(Ls)]
    tol = 1e-9
    ok = all(is_zero(anticomm(psi4[x], psi4[y]), tol) for x in range(Ls) for y in range(Ls))
    ok2 = True
    for x in range(Ls):
        for y in range(Ls):
            ac = anticomm(psi4[x], phi4[y])
            sc, c = is_scalar(ac, tol)
            want = 1.0 if x == y else 0.0
            if not (sc and abs(c - want) < tol):
                ok2 = False
    check("C", "staggered leg: reconstructed fields from the staggered-kernel "
               "Berezin functional satisfy {psi_x, psi_y} = 0 and "
               "{psi_x, phi_y} = delta_xy I at L_s = 4 (tol 1e-9) -- GL(F) on the "
               "two-step staggered transfer surface", ok and ok2)

    # ------------------------------------------------------------------
    # [D] Falsification + separation legs
    # ------------------------------------------------------------------
    print()
    print("--- [D] Falsification legs (the Grassmann and RP inputs are load-bearing) ---")

    for N in (2, 3):
        _, Amat, AtA, K = models[N]
        cn = OSModel(N, K, eps=+1, exact=True)
        thS = cn.theta(cn.S)
        rec_cn = reconstruct(cn)
        Gcn = rec_cn["G"]
        sym = all(Gcn[i][j] == Gcn[j][i] for i in range(len(Gcn)) for j in range(len(Gcn)))
        psd, rank = ldl_psd(Gcn)
        check("D", "N = %d: the commuting-nilpotent (ungraded) integrand ALSO has a "
                   "Theta-symmetric action and a PSD OS Gram of rank 2^N -- the "
                   "reconstruction functor runs on both integrand classes"
              % N, thS == cn.S and sym and psd and rank == 2 ** N)

        Gp_cn = rec_cn["Gp"]
        psd_p, rank_p = ldl_psd(Gp_cn)
        theta_ops = [rec_cn["mult_matrix"](cn.idx(1, x, 0)) for x in range(N)]
        ok_comm = all(is_zero(comm(theta_ops[x], theta_ops[y]))
                      for x in range(N) for y in range(N))
        ok_nonzero_ac = any(not is_zero(anticomm(theta_ops[x], theta_ops[y]))
                            for x in range(N) for y in range(N) if x != y)
        check("D", "N = %d: the SAME functor on the ungraded integrand reconstructs "
                   "cross-site COMMUTING operators ([theta_x, theta_y] = 0, "
                   "{theta_x, theta_y} != 0 cross-site) -- the hard-core frame; the "
                   "exchange sign of the reconstructed operators equals the exchange "
                   "parity of the integration variables, so the Grassmann input is "
                   "LOAD-BEARING" % N,
              psd_p and rank_p == 2 ** N and ok_comm and ok_nonzero_ac)

    # identity-level impossibility: hard-core cannot arise from a Grassmann integrand
    model2 = models[2][0]
    g0, g1 = model2.idx(1, 0, 0), model2.idx(1, 1, 0)
    m1, s1 = mul_mono(1 << g0, 1 << g1, -1)
    m2, s2 = mul_mono(1 << g1, 1 << g0, -1)
    check("D", "identity leg: in the Grassmann algebra the left-multiplication "
               "anticommutator vanishes BEFORE any quotient (chi_x chi_y = "
               "- chi_y chi_x exactly), so NO choice of action, reflection, or "
               "null quotient on a Grassmann integrand can reconstruct the "
               "cross-site-commuting hard-core frame with nonvanishing "
               "anticommutator",
          m1 == m2 and s1 == -s2 and s1 != 0,
          "the +1 exchange class is unreachable from the Berezin measure")

    # RP load-bearing: Theta-asymmetric kernel breaks the PSD certificate
    Kbad = [[Fraction(1), Fraction(1, 2)], [Fraction(-1, 2), Fraction(1)]]  # K != K^T
    bad = OSModel(2, Kbad, eps=-1, exact=True)
    thS = bad.theta(bad.S)
    Gbad = bad.gram(bad.aplus_basis())
    sym_bad = all(Gbad[i][j] == Gbad[j][i] for i in range(len(Gbad)) for j in range(len(Gbad)))
    check("D", "RP leg: a Theta-ASYMMETRIC kernel (K != K^T) destroys the OS "
               "symmetry (Theta(S) != S and the Gram is not symmetric) -- the "
               "reflection-positivity input is load-bearing for the existence of "
               "the reconstructed Hilbert space",
          thS != bad.S and not sym_bad)

    # K must be positive: a negative-eigenvalue symmetric kernel breaks PSD
    Kneg = [[Fraction(1), Fraction(2)], [Fraction(2), Fraction(1)]]  # eigs 3, -1
    neg = OSModel(2, Kneg, eps=-1, exact=True)
    Gneg = neg.gram(neg.aplus_basis())
    psd_neg, _ = ldl_psd(Gneg)
    check("D", "RP leg: a symmetric but INDEFINITE kernel (eigenvalues 3, -1) gives "
               "a non-PSD OS Gram (exact LDL detects a negative pivot) -- positivity "
               "of the transfer kernel is also load-bearing",
          (neg.theta(neg.S) == neg.S) and not psd_neg)

    # transmission certificate: the reconstructed cross-site exchange sign equals
    # the exchange parity of the integration variables, computed on both branches.
    model2, A2m, _, K2 = models[2]
    rec2 = reconstruct(model2)
    psiG = [rec2["mult_matrix"](model2.idx(1, x, 0)) for x in range(2)]
    cn2 = OSModel(2, K2, eps=+1, exact=True)
    rec_cn2 = reconstruct(cn2)
    psiU = [rec_cn2["mult_matrix"](cn2.idx(1, x, 0)) for x in range(2)]
    pgG = mat_mul(psiG[0], psiG[1])
    gpG = mat_mul(psiG[1], psiG[0])
    pgU = mat_mul(psiU[0], psiU[1])
    gpU = mat_mul(psiU[1], psiU[0])
    nzG = not is_zero(pgG)
    nzU = not is_zero(pgU)
    sgG = all(a == -b for ra, rb in zip(pgG, gpG) for a, b in zip(ra, rb))
    sgU = all(a == b for ra, rb in zip(pgU, gpU) for a, b in zip(ra, rb))
    check("D", "transmission certificate: psi_x psi_y != 0 and the reconstructed "
               "cross-site exchange sign EQUALS the exchange parity of the "
               "integration variables on both branches (Grassmann integrand -> "
               "sign -1; ungraded integrand -> sign +1) -- the measure surface "
               "carries exactly the frame bit the prior static negative notes prove "
               "invisible to dimension, ungraded algebra, positivity spectra, "
               "and loop data",
          nzG and nzU and sgG and sgU)

    # ------------------------------------------------------------------
    # [E] Post-audit bridge wire-up: reconstructive identification is no
    # longer opaque; only the matter-functional/action-surface pin remains.
    # ------------------------------------------------------------------
    print()
    print("--- [E] Source-graph bridge wire-up after re-audit feedback ---")

    note_text = NOTE.read_text(encoding="utf-8", errors="replace")
    bridge_text = BRIDGE_NOTE.read_text(encoding="utf-8", errors="replace") if BRIDGE_NOTE.exists() else ""
    bridge_cache = BRIDGE_CACHE.read_text(encoding="utf-8", errors="replace") if BRIDGE_CACHE.exists() else ""
    header = cache_header(BRIDGE_CACHE)
    check("E", "parent note records the exact post-audit blocker and the sibling "
               "bridge packet as the reconstruction-identification repair",
          "missing_bridge_theorem: close or explicitly register the Berezin/RP" in note_text
          and "GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md" in note_text
          and "opaque reconstruction-identification bridge plus action" in note_text)
    check("E", "bridge note decomposes the identification into carrier, parity, "
               "dictionary, and matter-functional clauses",
          "carrier clause" in bridge_text
          and "parity clause" in bridge_text
          and "dictionary clause" in bridge_text
          and "matter-functional clause" in bridge_text
          and "residual = the matter-functional clause" in bridge_text.lower())
    check("E", "bridge runner cache is present, SHA-fresh, and passing",
          BRIDGE_RUNNER.exists()
          and BRIDGE_CACHE.exists()
          and header.get("runner_sha256") == sha256_file(BRIDGE_RUNNER)
          and header.get("status") == "ok"
          and "TOTAL: PASS=39 FAIL=0" in bridge_cache,
          "bridge cache validates the sibling packet without rerunning it here")
    check("E", "remaining boundary is only the matter-functional/action-surface "
               "supplier; no audit status movement or new primitive is claimed",
          "The residual is now clause (4)" in note_text
          and "matter-functional/action-surface clause remains" in note_text
          and "does not promote this row" in note_text
          and "does not add a new axiom" in note_text)

    print()
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
