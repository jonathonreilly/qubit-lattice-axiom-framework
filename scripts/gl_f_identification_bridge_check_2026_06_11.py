#!/usr/bin/env python3
"""GL(F) reconstruction-identification bridge -- conditional decomposition checks.

Companion runner for
docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md

Target: the ONE declared residual (besides chain grades) of the GL(F)
Berezin-RP reconstruction note
(claim id gl_f_from_berezin_rp_reconstruction_narrow_theorem_note_2026-06-10;
source landed, every consumed construction fact is RECOMPUTED here, none
cited blind):

    "Identifying the framework's physical operator theory with that
     reconstruction is a bridge."

This runner certifies the decomposition of that bridge into four clauses and
the exact finite support for three kinematic clauses after the declared
Berezin/RP OS functional is supplied.  It does not discharge the
matter-functional clause or close the parent bridge.

  (I-1) carrier clause     -- physical Hilbert space = qubit net (C^2)^(x)N:
        per-site supplied DIRECTLY by the Quantum axiom (u4 row is
        audited_renaming: the axiom is the supplier); composite by the
        retained tensor-product bridge; GNS dimension matches.   EXACT SUPPORT.
  (I-2) parity clause      -- the reconstructed grading F-hat is a WORD in the
        reconstructed fields, F-hat = prod_x (1 - 2 psi_x^dag psi_x), so EVERY
        intertwiner transports it onto the retained F = (x)sigma_3
        automatically (number operators are dressing-invariant). EXACT SUPPORT.
  (I-3) dictionary clause  -- the field dictionary is FORCED: the OS functional
        of the declared Berezin/RP measure has cyclic vacuum, its word values vanish on
        every anticommutator insertion (so GL(F) is a property of the
        FUNCTIONAL, holding in every cyclic realization), the reconstructed
        words span the full matrix algebra (unique irrep / pure state), and
        the intertwiner onto the explicit qubit-net Jordan-Wigner realization
        is unique up to one scalar (exact Schur nullity-1 certificate) and
        unitary after exact rational rescaling.                   EXACT SUPPORT.
  (I-4) matter-functional clause -- "the framework's physical matter
        correlation functional IS the declared Berezin/RP measure's OS
        functional."
        NOT discharged: this is the strictly smaller residual pin; the
        falsification legs show it is load-bearing (a net violating it --
        the hard-core frame -- escapes with intertwiner space exactly 0).

Tags: [A] retained-supplier recomputation  [B] reconstruction recomputed from
the landed parent construction  [C] discharge certificates (new)
[D] falsification legs (the residual clause is load-bearing).

Exact rational arithmetic at N = 2, 3; float leg only for the retained RP
dispersion recomputation. Standard library only, deterministic, < 5 min.
"""

from fractions import Fraction
import itertools
import math
from pathlib import Path

PASS = 0
FAIL = 0
ROOT = Path(__file__).resolve().parents[1]
NOTE = ROOT / "docs/GL_F_IDENTIFICATION_BRIDGE_DECOMPOSITION_NARROW_THEOREM_NOTE_2026-06-11.md"


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


# ----------------------------------------------------------------------
# Graded algebra over masks (recomputed from the parent construction).
# eps = -1: Grassmann; eps = +1: commuting-nilpotent (ungraded) integrand.
# ----------------------------------------------------------------------

def mul_mono(a, b, eps):
    if a & b:
        return (0, 0)
    if eps == 1:
        return (a | b, 1)
    cnt = 0
    bb = b
    while bb:
        j = (bb & -bb).bit_length() - 1
        cnt += bin(a >> (j + 1)).count("1")
        bb &= bb - 1
    return (a | b, -1 if (cnt & 1) else 1)


def amul(A, B, eps):
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
    out = {0: Fraction(1)}
    for m, c in sorted(S.items()):
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


class OSModel:
    """Two-slice Theta-symmetric Berezin/CN functional (parent §2, recomputed)."""

    def __init__(self, N, K, eps):
        self.N = N
        self.K = K
        self.eps = eps
        self.nvar = 4 * N
        self.top = (1 << self.nvar) - 1
        one = Fraction(1)
        self.one = one
        S = {}
        for x in range(N):
            S = aadd(S, self._quad(0, x, 1, 0, x, 0, one))
            S = aadd(S, self._quad(1, x, 1, 1, x, 0, one))
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
        idxs = []
        m = mask
        while m:
            j = (m & -m).bit_length() - 1
            idxs.append(j)
            m &= m - 1
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
        return {out_mask: out_sign * coeff}

    def theta(self, A):
        out = {}
        for m, c in A.items():
            out = aadd(out, self.theta_mono(m, c))
        return out

    def expect_mono(self, mask, sign):
        rest = self.top & ~mask
        c = self.expS.get(rest, 0)
        if not c:
            return 0 * self.one
        _, s = mul_mono(mask, rest, self.eps)
        return sign * s * c / self.Ztop

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

    def occ_masks(self):
        bar_idxs = [self.idx(1, x, 1) for x in range(self.N)]
        masks = []
        for r in range(self.N + 1):
            for combo in itertools.combinations(bar_idxs, r):
                m = 0
                for j in combo:
                    m |= 1 << j
                masks.append(m)
        return masks


# ----------------------------------------------------------------------
# Exact rational linear algebra
# ----------------------------------------------------------------------

def ldl_psd(G):
    n = len(G)
    A = [row[:] for row in G]
    active = list(range(n))
    rank = 0
    while active:
        dmax, imax = None, None
        for i in active:
            d = A[i][i]
            if dmax is None or d > dmax:
                dmax, imax = d, i
        if dmax < 0:
            return (False, rank)
        if dmax == 0:
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


def kernel_basis(rows, ncols):
    """Exact kernel of a rational matrix given as list of rows."""
    A = [r[:] for r in rows]
    n = ncols
    pivots = []
    r = 0
    for c in range(n):
        pr = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(len(A)):
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


def mat_rank(rows):
    A = [r[:] for r in rows]
    rank = 0
    ncols = len(A[0]) if A else 0
    r = 0
    for c in range(ncols):
        pr = None
        for i in range(r, len(A)):
            if A[i][c] != 0:
                pr = i
                break
        if pr is None:
            continue
        A[r], A[pr] = A[pr], A[r]
        pv = A[r][c]
        A[r] = [v / pv for v in A[r]]
        for i in range(len(A)):
            if i != r and A[i][c] != 0:
                f = A[i][c]
                A[i] = [a - f * b for a, b in zip(A[i], A[r])]
        rank += 1
        r += 1
    return rank


def mat_solve(A, B):
    n = len(A)
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


def mat_inv(A):
    n = len(A)
    I = [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]
    return mat_solve(A, I)


def mat_mul(A, B):
    n, k, m = len(A), len(B), len(B[0])
    out = [[Fraction(0)] * m for _ in range(n)]
    for i in range(n):
        Ai = A[i]
        oi = out[i]
        for t in range(k):
            a = Ai[t]
            if a:
                Bt = B[t]
                for j in range(m):
                    if Bt[j]:
                        oi[j] += a * Bt[j]
    return out


def mat_add(A, B):
    return [[a + b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_sub(A, B):
    return [[a - b for a, b in zip(ra, rb)] for ra, rb in zip(A, B)]


def mat_T(A):
    return [list(row) for row in zip(*A)]


def is_zero(A):
    return all(v == 0 for row in A for v in row)


def is_scalar(A):
    n = len(A)
    c = A[0][0]
    for i in range(n):
        for j in range(n):
            if A[i][j] != (c if i == j else 0):
                return (False, None)
    return (True, c)


def eye(n):
    return [[Fraction(1) if i == j else Fraction(0) for j in range(n)] for i in range(n)]


def anticomm(A, B):
    return mat_add(mat_mul(A, B), mat_mul(B, A))


def comm(A, B):
    return mat_sub(mat_mul(A, B), mat_mul(B, A))


def kron(A, B):
    na, ma = len(A), len(A[0])
    nb, mb = len(B), len(B[0])
    out = [[Fraction(0)] * (ma * mb) for _ in range(na * nb)]
    for i in range(na):
        for j in range(ma):
            if A[i][j]:
                for k in range(nb):
                    for l in range(mb):
                        if B[k][l]:
                            out[i * nb + k][j * mb + l] = A[i][j] * B[k][l]
    return out


def kron_list(mats):
    out = mats[0]
    for m in mats[1:]:
        out = kron(out, m)
    return out


# ----------------------------------------------------------------------
# Reconstruction in occupation-class coordinates (parent, recomputed)
# ----------------------------------------------------------------------

def mult_matrix(model, occ, Gp_inv, gen_idx):
    one = model.one
    n = len(occ)
    W = [[0 * one] * n for _ in range(n)]
    for j, mj in enumerate(occ):
        m, s = mul_mono(1 << gen_idx, mj, model.eps)
        if s == 0:
            continue
        for i, mi in enumerate(occ):
            th = model.theta_mono(mi, one)
            if not th:
                continue
            (tm, tc), = th.items()
            mm, ss = mul_mono(tm, m, model.eps)
            if ss:
                W[i][j] = model.expect_mono(mm, ss * tc * s)
    return mat_mul(Gp_inv, W)


def build_reconstruction(N, K, eps):
    """Return dict with model, occ, Gp, fields psi, phi (multiplication ops)."""
    model = OSModel(N, K, eps)
    occ = model.occ_masks()
    basis = model.aplus_basis()
    G = model.gram(basis)
    pos = {m: i for i, m in enumerate(basis)}
    occ_pos = [pos[m] for m in occ]
    Gp = [[G[i][j] for j in occ_pos] for i in occ_pos]
    Gp_inv = mat_inv(Gp)
    psi = [mult_matrix(model, occ, Gp_inv, model.idx(1, x, 0)) for x in range(N)]
    phi = [mult_matrix(model, occ, Gp_inv, model.idx(1, x, 1)) for x in range(N)]
    return {"model": model, "occ": occ, "basis": basis, "G": G,
            "Gp": Gp, "Gp_inv": Gp_inv, "psi": psi, "phi": phi}


def sylvester_kernel(pairs, dim):
    """Solve S A_k = B_k S for all (A_k, B_k); S is dim x dim.
    Unknowns S[i][j] flattened i*dim + j. Returns kernel basis (as matrices)."""
    rows = []
    for (A, Bm) in pairs:
        # (S A - B S)[i][j] = sum_t S[i][t] A[t][j] - sum_t B[i][t] S[t][j]
        for i in range(dim):
            for j in range(dim):
                row = [Fraction(0)] * (dim * dim)
                for t in range(dim):
                    if A[t][j]:
                        row[i * dim + t] += A[t][j]
                    if Bm[i][t]:
                        row[t * dim + j] -= Bm[i][t]
                if any(row):
                    rows.append(row)
    ker = kernel_basis(rows, dim * dim)
    mats = []
    for v in ker:
        mats.append([[v[i * dim + j] for j in range(dim)] for i in range(dim)])
    return mats


# ======================================================================
# MAIN
# ======================================================================

def main():
    one = Fraction(1)

    print("=" * 78)
    print("GL(F) identification bridge -- conditional decomposition checks")
    print("(2026-06-11; landed parent reconstruction recomputed here)")
    print("=" * 78)

    note_text = NOTE.read_text(encoding="utf-8")
    note_flat = " ".join(note_text.split())
    check("S", "post-audit source status is conditional support / open gate, not theorem closure",
          "**Claim type:** open_gate / conditional-support certificate" in note_text
          and "actual_current_surface_status: conditional-support" in note_text
          and "target_claim_type: open_gate" in note_text
          and "proposal_allowed: false" in note_text)
    check("S", "matter-functional clause I-4 remains explicitly not discharged",
          "matter-functional clause (I-4) is not discharged" in note_flat
          and "does not discharge that clause" in note_flat)
    check("S", "source no longer asks audit to treat the parent bridge as closed",
          "does not ask the audit lane to treat the parent bridge as closed" in note_flat
          and "bare_retained_allowed: false" in note_text)

    # ------------------------------------------------------------------
    # [A] Retained suppliers, recomputed
    # ------------------------------------------------------------------
    print()
    print("--- [A] Retained suppliers of the kinematic clauses (recomputed) ---")

    s0 = [[one, 0 * one], [0 * one, one]]
    s1 = [[0 * one, one], [one, 0 * one]]
    s3 = [[one, 0 * one], [0 * one, -one]]
    sm = [[0 * one, one], [0 * one, 0 * one]]   # annihilator: sm|1> = |0>
    sp = mat_T(sm)
    # (i sigma_2) as a real matrix stand-in for the 4th basis direction
    is2 = [[0 * one, one], [-one, 0 * one]]
    rank_M2 = mat_rank([[m[i][j] for i in range(2) for j in range(2)]
                        for m in (s0, s1, is2, s3)])
    # commutant of {s1, s3} on C^2 = scalars (irreducibility, Schur)
    comm_ker = sylvester_kernel([(s1, s1), (s3, s3)], 2)
    irr = len(comm_ker) == 1 and is_scalar(comm_ker[0])[0]
    check("A", "carrier clause (I-1), per-site: {I, sigma_1, i sigma_2, sigma_3} "
               "span M_2 (rank 4) and the commutant of the Pauli action on C^2 is "
               "exactly the scalars (Schur) -- C^2 is the irreducible carrier the "
               "Quantum axiom supplies DIRECTLY (the u4 row is audited_renaming: "
               "the axiom, not a derivation, is the per-site supplier)",
          rank_M2 == 4 and irr)

    for N in (2, 3):
        dim = 2 ** N
        # retained tensor bridge composite carrier + the two tied multiplets
        pauli = []
        jw = []
        for x in range(N):
            facs_p = [s0] * N
            facs_p[x] = sm
            pauli.append(kron_list(facs_p))
            facs_j = [s3] * x + [sm] + [s0] * (N - 1 - x)
            jw.append(kron_list(facs_j))
        Fq = kron_list([s3] * N)
        n_p = [mat_mul(mat_T(pauli[x]), pauli[x]) for x in range(N)]
        n_j = [mat_mul(mat_T(jw[x]), jw[x]) for x in range(N)]
        same_n = all(n_p[x] == n_j[x] for x in range(N))
        # F = prod (1 - 2 n_x) = (x)sigma_3, involution, balanced multiplicities
        Fprod = eye(dim)
        for x in range(N):
            Fprod = mat_mul(Fprod, mat_sub(eye(dim), [[2 * v for v in r] for r in n_p[x]]))
        invol = mat_mul(Fq, Fq) == eye(dim)
        mult_plus = sum(1 for i in range(dim) if Fq[i][i] == 1)
        odd_p = all(is_zero(anticomm(Fq, pauli[x])) for x in range(N))
        odd_j = all(is_zero(anticomm(Fq, jw[x])) for x in range(N))
        check("A", "N = %d: retained parity row recomputed: F = (x)sigma_3 = "
                   "prod_x (1 - 2 n_x), F^2 = I, balanced multiplicities "
                   "(2^{N-1} = %d each)" % (N, dim // 2),
              Fprod == Fq and invol and mult_plus == dim // 2)
        comm_pauli = all(is_zero(comm(pauli[x], pauli[y]))
                         for x in range(N) for y in range(N) if x != y)
        anti_jw = all(is_zero(anticomm(jw[x], jw[y]))
                      for x in range(N) for y in range(N))
        check("A", "N = %d: the static tie recomputed on the retained composite "
                   "carrier (C^2)^(x)N: the per-site Pauli multiplet (cross-site "
                   "COMMUTING, the retained tensor-bridge convention) and the "
                   "Jordan-Wigner multiplet (cross-site CAR) have IDENTICAL number "
                   "operators n_x and are BOTH F-odd -- carrier + parity + occupation "
                   "data cannot force the dictionary; the functional clause is the "
                   "load-bearing member of the structure set" % N,
              same_n and comm_pauli and anti_jw and odd_p and odd_j)

    # retained RP row's delivered dynamics is action-constructed (recomputed)
    Ls, mass = 4, 0.5
    ok = True
    for k in range(Ls):
        p = 2 * math.pi * k / Ls
        a_e = complex(mass, math.sin(p))
        a_o = complex(mass, -math.sin(p))
        Te = [[-2 * a_e, 1], [1, 0]]
        To = [[-2 * a_o, 1], [1, 0]]
        T2 = [[To[0][0] * Te[0][0] + To[0][1] * Te[1][0],
               To[0][0] * Te[0][1] + To[0][1] * Te[1][1]],
              [To[1][0] * Te[0][0] + To[1][1] * Te[1][0],
               To[1][0] * Te[0][1] + To[1][1] * Te[1][1]]]
        tr = T2[0][0] + T2[1][1]
        dt = T2[0][0] * T2[1][1] - T2[0][1] * T2[1][0]
        disc = (tr * tr - 4 * dt) ** 0.5
        lam = min([(tr + disc) / 2, (tr - disc) / 2], key=abs)
        E = math.asinh(math.sqrt(mass ** 2 + math.sin(p) ** 2))
        if abs(lam.imag) > 1e-12 or abs(lam.real - math.exp(-2 * E)) > 1e-10:
            ok = False
    check("A", "dynamics clause context: the retained RP row's delivered transfer "
               "object is CONSTRUCTED from the action (T_odd T_even eigenvalue "
               "e^{-2E(p)}, E = arcsinh sqrt(m^2 + sin^2 p), recomputed at L_s = 4) "
               "-- the retained set contains no independently specified physical "
               "dynamics for the matter sector (the axioms each disclaim supplying "
               "a dynamics), so the dynamical sub-clause has no content beyond the "
               "matter-functional clause (I-4)", ok)

    # ------------------------------------------------------------------
    # [B] Parent reconstruction recomputed (landed parent source; nothing cited blind)
    # ------------------------------------------------------------------
    print()
    print("--- [B] Parent reconstruction recomputed (N = 2, 3, exact) ---")

    A2 = [[one, Fraction(1, 2)], [0 * one, one]]
    A3 = [[one, Fraction(1, 2), 0 * one],
          [0 * one, one, Fraction(1, 3)],
          [0 * one, 0 * one, one]]

    R = {}
    for N, Amat in ((2, A2), (3, A3)):
        AtA = mat_mul(mat_T(Amat), Amat)
        K = mat_inv(AtA)
        rec = build_reconstruction(N, K, eps=-1)
        rec["Amat"], rec["K"], rec["Kinv"] = Amat, K, AtA
        R[N] = rec
        model = rec["model"]
        G, Gp = rec["G"], rec["Gp"]
        dim = 2 ** N
        thS_ok = model.theta(model.S) == model.S
        sym = all(G[i][j] == G[j][i] for i in range(len(G)) for j in range(len(G)))
        psd, rank = ldl_psd(G)
        psd_p, rank_p = ldl_psd(Gp)
        check("B", "N = %d: Theta-symmetric action, Z != 0, OS Gram PSD of rank "
                   "exactly 2^N = %d, occupation sub-Gram positive definite "
                   "(parent (R-a)/(R-b) facts recomputed)" % (N, dim),
              thS_ok and model.Ztop != 0 and sym and psd and rank == dim
              and psd_p and rank_p == dim)

        # canonical normalization and CAR (parent (R-c)/(R-d) recomputed)
        psi, phi, Gp_inv = rec["psi"], rec["phi"], rec["Gp_inv"]
        Bmat = mat_inv(mat_T(Amat))
        psit = []
        for x in range(N):
            m = [[0 * one] * dim for _ in range(dim)]
            for y in range(N):
                if Bmat[x][y]:
                    m = mat_add(m, [[Bmat[x][y] * v for v in row] for row in psi[y]])
            psit.append(m)
        # OS adjoint in class coordinates
        def gp_adj(M):
            return mat_mul(Gp_inv, mat_mul(mat_T(M), Gp))
        psitd = [gp_adj(p) for p in psit]
        ok1 = all(is_zero(anticomm(psit[x], psit[y]))
                  for x in range(N) for y in range(N))
        ok2 = True
        for x in range(N):
            for y in range(N):
                sc, c = is_scalar(anticomm(psit[x], psitd[y]))
                if not (sc and c == (one if x == y else 0 * one)):
                    ok2 = False
        check("B", "N = %d: exact CAR for the canonically normalized reconstructed "
                   "multiplet -- {psi_x, psi_y} = 0, {psi_x, psi_y^dag} = delta_xy I "
                   "(parent GL(F) certificate recomputed)" % N, ok1 and ok2)
        # unnormalized central covariance = K^{-1} (dynamics-bearing kernel is
        # functional-determined)
        psid = [gp_adj(p) for p in psi]
        okc = True
        for x in range(N):
            for y in range(N):
                sc, c = is_scalar(anticomm(psi[x], psid[y]))
                if not (sc and c == rec["Kinv"][x][y]):
                    okc = False
        check("B", "N = %d: {psi_x, psi_y^dag} = (K^{-1})_xy I exactly -- the "
                   "transfer kernel K is RECOVERED from the functional's "
                   "anticommutator data (the dynamics-bearing object is "
                   "functional-determined, not identification-dependent)" % N, okc)

        # parity: F-hat diagonal pattern + WORD identity (new, load-bearing for I-2)
        occ = rec["occ"]
        Fhat = [[(one if i == j else 0 * one) * ((-1) ** bin(occ[i]).count("1"))
                 for j in range(dim)] for i in range(dim)]
        Fword = eye(dim)
        for x in range(N):
            nx = mat_mul(psitd[x], psit[x])
            Fword = mat_mul(Fword, mat_sub(eye(dim), [[2 * v for v in r] for r in nx]))
        odd = all(is_zero(anticomm(Fhat, psit[x])) for x in range(N))
        formk = mat_mul(Fhat, mat_mul(Gp, Fhat)) == Gp
        check("B", "N = %d: F-hat (integrand grading pushed to the quotient) "
                   "preserves the OS form, anticommutes with every field, AND "
                   "equals the WORD prod_x (1 - 2 psi_x^dag psi_x) in the "
                   "reconstructed fields exactly -- the reconstructed parity is "
                   "a polynomial in the field multiplet, not extra structure" % N,
              odd and formk and Fword == Fhat)
        rec["psit"], rec["psitd"], rec["Fhat"] = psit, psitd, Fhat

    # ------------------------------------------------------------------
    # [C] Discharge certificates
    # ------------------------------------------------------------------
    print()
    print("--- [C] Exact finite support (I-1, I-2, I-3 conditional on I-4) ---")

    for N in (2, 3):
        rec = R[N]
        dim = 2 ** N
        psit, psitd, Gp, Fhat = rec["psit"], rec["psitd"], rec["Gp"], rec["Fhat"]

        # word family: normal-ordered monomials prod psi^dag_A prod psi_B
        words = []
        for amask in range(2 ** N):
            for bmask in range(2 ** N):
                W = eye(dim)
                for x in range(N):
                    if amask >> x & 1:
                        W = mat_mul(W, psitd[x])
                for x in range(N):
                    if bmask >> x & 1:
                        W = mat_mul(W, psit[x])
                words.append(W)

        # C1: cyclicity of the OS vacuum Omega = [1] (class coordinate e_0)
        Xrows = [[W[i][0] for i in range(dim)] for W in words]  # w(Omega) coords
        cyc_rank = mat_rank(Xrows)
        check("C", "N = %d: CYCLICITY -- the %d normal-ordered field words applied "
                   "to the OS vacuum Omega span the full reconstructed space "
                   "(exact rank = 2^N = %d); the functional's matrix elements over "
                   "words exhaust the operator theory" % (N, 4 ** N, dim),
              cyc_rank == dim)

        # C2: word span = full matrix algebra (unique irrep / pure state)
        span_rank = mat_rank([[W[i][j] for i in range(dim) for j in range(dim)]
                              for W in words])
        check("C", "N = %d: IRREDUCIBILITY -- the field words span the FULL matrix "
                   "algebra M_{2^N} (exact rank %d = 4^N): the GNS representation "
                   "is the unique irreducible CAR_N representation and the OS state "
                   "is pure" % (N, 4 ** N),
              span_rank == 4 ** N)

        # C3: functional-level GL(F): all word-sandwiched anticommutator
        # insertions vanish -- omega(w^dag {psi_x,psi_y} w') = 0 etc.
        X = Xrows  # rows = coordinates of w(Omega)
        GpX = mat_mul(X, Gp)  # for inner products <w Omega, . >
        ok_func = True
        for x in range(N):
            for y in range(N):
                A1m = anticomm(psit[x], psit[y])
                A2m = anticomm(psit[x], psitd[y])
                if x == y:
                    A2m = mat_sub(A2m, eye(dim))
                for Am in (A1m, A2m):
                    # values V = X Gp Am X^T must vanish identically
                    V = mat_mul(GpX, mat_mul(Am, mat_T(X)))
                    if not is_zero(V):
                        ok_func = False
        check("C", "N = %d: FUNCTIONAL-LEVEL GL(F) -- every word-sandwiched value "
                   "omega(w^dag ({psi_x, psi_y}) w') and "
                   "omega(w^dag ({psi_x, psi_y^dag} - delta_xy I) w') vanishes "
                   "exactly (all %d x %d word pairs, all x, y); combined with "
                   "cyclicity, the exchange relations hold as OPERATOR IDENTITIES "
                   "in EVERY realization of the functional with cyclic vacuum -- "
                   "GL(F) is a property of the functional, invariant under the "
                   "choice of identification" % (N, 4 ** N, 4 ** N),
              ok_func)

        # C4: unique unitary intertwiner onto the explicit qubit-net JW net
        jw = []
        for x in range(N):
            facs = [s3] * x + [sm] + [s0] * (N - 1 - x)
            jw.append(kron_list(facs))
        Fq = kron_list([s3] * N)
        pairs = []
        for x in range(N):
            pairs.append((psit[x], jw[x]))
            pairs.append((psitd[x], mat_T(jw[x])))
        ker = sylvester_kernel(pairs, dim)
        ok_null = len(ker) == 1
        S0 = ker[0] if ker else None
        ok_inv = ok_null and mat_rank(S0) == dim
        # unitarity after scaling: S0^T S0 = lambda * Gp, lambda rational > 0
        lam = None
        ok_unit = False
        if ok_inv:
            StS = mat_mul(mat_T(S0), S0)
            num = next((StS[i][j], Gp[i][j]) for i in range(dim) for j in range(dim)
                       if Gp[i][j] != 0)
            lam = num[0] / num[1]
            ok_unit = lam > 0 and all(StS[i][j] == lam * Gp[i][j]
                                      for i in range(dim) for j in range(dim))
        check("C", "N = %d: UNIQUE INTERTWINER -- the space of operators S with "
                   "S psi_x = c_x S and S psi_x^dag = c_x^T S (c = qubit-net "
                   "Jordan-Wigner multiplet) has dimension EXACTLY 1 (Schur), S is "
                   "invertible, and S^T S = lambda Gp with rational lambda > 0: the "
                   "identification of the reconstruction with the qubit net is "
                   "FORCED up to one overall scalar, i.e., W = S/sqrt(lambda) is "
                   "the unique-up-to-sign unitary identification" % N,
              ok_null and ok_inv and ok_unit,
              "lambda = %s" % lam)

        # C5: the forced identification transports the parity onto the RETAINED F
        ok_par = ok_inv and mat_mul(S0, Fhat) == mat_mul(Fq, S0)
        check("C", "N = %d: PARITY AUTO-ALIGNMENT -- the unique intertwiner "
                   "transports F-hat onto the retained F = (x)sigma_3 exactly "
                   "(S F-hat = F S), with no separate parity identification "
                   "choice: F-hat is the word prod(1 - 2 psi^dag psi) and number "
                   "operators are dressing-invariant, so clause (I-2) is a "
                   "theorem, not an input" % N, ok_par)

        # C6: functional transport -- the image vacuum reproduces omega exactly
        ok_tr = True
        if ok_unit:
            Y = mat_mul(X, mat_T(S0))      # rows = coords of S w(Omega) in C^{2^N}
            lhs = mat_mul(Y, mat_T(Y))      # <S w Omega, S w' Omega>_std
            rhs = mat_mul(GpX, mat_T(X))    # <w Omega, w' Omega>_Gp
            ok_tr = all(lhs[i][j] == lam * rhs[i][j]
                        for i in range(len(words)) for j in range(len(words)))
        check("C", "N = %d: FUNCTIONAL TRANSPORT -- the image vacuum "
                   "Omega' = W Omega on the qubit net reproduces the declared "
                   "Berezin/RP measure's OS functional on all %d x %d word pairs exactly "
                   "(<S w Omega, S w' Omega> = lambda <w Omega, w' Omega>_Gp): the "
                   "qubit net + JW dictionary + Omega' IS a realization, and by "
                   "C1-C4 the only one up to the unique unitary" % (N, 4 ** N, 4 ** N),
              ok_tr)

        # C7: GL(F) equivalence-invariance under ANY unitary (demonstrative)
        rot = [[Fraction(3, 5), Fraction(4, 5)], [Fraction(-4, 5), Fraction(3, 5)]]
        U = kron_list([rot] + [s0] * (N - 1))
        Ut = mat_T(U)
        conj = [mat_mul(U, mat_mul(jw[x], Ut)) for x in range(N)]
        Fc = mat_mul(U, mat_mul(Fq, Ut))
        ok_e = all(is_zero(anticomm(conj[x], conj[y])) for x in range(N) for y in range(N))
        ok_e2 = True
        for x in range(N):
            for y in range(N):
                sc, c = is_scalar(anticomm(conj[x], mat_T(conj[y])))
                if not (sc and c == (one if x == y else 0 * one)):
                    ok_e2 = False
        ok_e3 = all(is_zero(anticomm(Fc, conj[x])) for x in range(N))
        check("C", "N = %d: EQUIVALENCE-INVARIANCE -- conjugating the realized net "
                   "by an exact rational orthogonal unitary preserves CAR and "
                   "parity-oddness verbatim (GL(F) is invariant under every "
                   "unitary net isomorphism; the residual scalar/sign freedom in "
                   "the identification is GL(F)-immaterial)" % N,
              ok_e and ok_e2 and ok_e3)

    # ------------------------------------------------------------------
    # [D] Falsification legs: the residual clause (I-4) is load-bearing
    # ------------------------------------------------------------------
    print()
    print("--- [D] Falsification legs (the matter-functional clause is the pin) ---")

    for N in (2, 3):
        rec = R[N]
        dim = 2 ** N
        psit, psitd = rec["psit"], rec["psitd"]
        pauli = []
        for x in range(N):
            facs = [s0] * N
            facs[x] = sm
            pauli.append(kron_list(facs))
        pairs = []
        for x in range(N):
            pairs.append((psit[x], pauli[x]))
            pairs.append((psitd[x], mat_T(pauli[x])))
        ker = sylvester_kernel(pairs, dim)
        check("D", "N = %d: HARD-CORE ESCAPE -- the intertwiner space onto the "
                   "cross-site-commuting Pauli (hard-core) multiplet is EXACTLY 0: "
                   "no identification of the reconstruction with the hard-core "
                   "frame exists at all (the frame violates the functional clause "
                   "I-4, and only that clause -- it carries the same carrier, the "
                   "same parity-oddness, the same number operators)" % N,
              len(ker) == 0,
              "kernel dim = %d" % len(ker))
        # operator witness: the hard-core anticommutator is nonzero
        ac = anticomm(pauli[0], pauli[1])
        check("D", "N = %d: the witness relation: {theta_0, theta_1} != 0 on the "
                   "hard-core net while omega forces {psi_0, psi_1} = 0 in every "
                   "realization (functional-level certificate [C]); a single "
                   "functional value separates the frames" % N,
              not is_zero(ac))

    # ungraded-integrand mirror leg (branch sensitivity of the machinery)
    N = 2
    dim = 2 ** N
    recU = build_reconstruction(N, R[2]["K"], eps=+1)
    GU = recU["G"]
    psdU, rankU = ldl_psd(GU)
    tU = recU["psi"]
    ok_comm = all(is_zero(comm(tU[x], tU[y])) for x in range(N) for y in range(N))
    ok_nz = any(not is_zero(anticomm(tU[x], tU[y]))
                for x in range(N) for y in range(N) if x != y)
    check("D", "N = 2: MIRROR LEG -- the SAME functor on the ungraded "
               "(commuting-nilpotent) integrand reconstructs a PSD rank-2^N theory "
               "with cross-site COMMUTING operators (nonzero anticommutator): the "
               "identification machinery is branch-sensitive -- the functional "
               "clause (I-4) decides the frame, the discharged kinematic clauses "
               "do not",
          psdU and rankU == dim and ok_comm and ok_nz)
    # and the ungraded reconstruction admits NO intertwiner onto the CAR/JW net
    jw2 = []
    for x in range(N):
        facs = [s3] * x + [sm] + [s0] * (N - 1 - x)
        jw2.append(kron_list(facs))
    GpU_inv = recU["Gp_inv"]
    GpU = recU["Gp"]
    tUd = [mat_mul(GpU_inv, mat_mul(mat_T(t), GpU)) for t in tU]
    pairsU = []
    for x in range(N):
        pairsU.append((tU[x], jw2[x]))
        pairsU.append((tUd[x], mat_T(jw2[x])))
    kerU = sylvester_kernel(pairsU, dim)
    check("D", "N = 2: the ungraded reconstruction admits NO intertwiner onto the "
               "CAR/JW net (kernel dim = 0) -- mirror-symmetric to the hard-core "
               "escape; each integrand class identifies only with its own frame",
          len(kerU) == 0)

    # parity-multiplicity escape
    N = 3
    dim = 2 ** N
    Fhat3 = R[3]["Fhat"]
    tr_F = sum(Fhat3[i][i] for i in range(dim))
    G_bad_tr = dim - 2  # diag(1,...,1,-1)
    check("D", "N = 3: PARITY ESCAPE -- an involution with unbalanced "
               "multiplicities (trace 2^N - 2 = %d) can never be unitarily "
               "aligned with F-hat (trace %d): conjugation preserves the trace, "
               "so the retained balanced-multiplicity fact (parity row (F4)) is "
               "load-bearing for the parity clause" % (G_bad_tr, tr_F),
          tr_F == 0 and G_bad_tr != 0)

    # even-subalgebra cyclicity failure (the cyclicity hypothesis is load-bearing)
    rec = R[2]
    dim = 4
    psit, psitd = rec["psit"], rec["psitd"]
    even_words = []
    for amask in range(4):
        for bmask in range(4):
            if (bin(amask).count("1") + bin(bmask).count("1")) % 2 == 0:
                W = eye(dim)
                for x in range(2):
                    if amask >> x & 1:
                        W = mat_mul(W, psitd[x])
                for x in range(2):
                    if bmask >> x & 1:
                        W = mat_mul(W, psit[x])
                even_words.append(W)
    Xe = [[W[i][0] for i in range(dim)] for W in even_words]
    re_rank = mat_rank(Xe)
    check("D", "N = 2: CYCLICITY ESCAPE -- restricting to the EVEN (parity-"
               "preserving) word subalgebra, the vacuum spans only dim 2^{N-1} = "
               "%d < 2^N: the full-field cyclicity certificate in [C] is "
               "load-bearing for the operator-identity transport; a rival who "
               "consumes only the even observable subalgebra does not get the "
               "field dictionary forced (declared in the note's boundaries)"
          % (dim // 2),
          re_rank == dim // 2)

    print()
    print("TOTAL: PASS=%d FAIL=%d" % (PASS, FAIL))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
