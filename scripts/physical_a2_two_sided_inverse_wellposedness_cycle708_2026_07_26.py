#!/usr/bin/env python3
"""Cycle 708 - A2's two-sided-inverse proviso on a finite covariant lattice.

The critical root row `gravity_full_self_consistency_note` carries this
verdict rationale:

    "The scoped implication is mathematically valid PROVIDED THE STATED
     TWO-SIDED INVERSES EXIST: substituting `L^{-1} = G_0 = H^{-1}` and
     inverting gives `L = H`."

The proviso has never been checked. This runner checks it, finds it fails on
every finite translation-covariant lattice, and shows the repair is already
available inside the framework.

Everything is exact rational arithmetic on explicit finite matrices.

Rows:

  Z1  ker(-Delta_lat) on the L^3 torus is exactly the constants, dimension 1
  Z2  hence H is singular and has no two-sided inverse -- the proviso fails
  Z3  the repo's own periodic convention (Bell D5: "graph Laplacian
      pseudoinverse ... excluding the zero mode") is also singular, so
      `L^{-1} = G_0` has NO full-space solution under it either
  Z4  restricted to the zero-mean sector, H is invertible and A2 determines
      L there
  Z5  adding covariance closes the gap: matching on the zero-mean sector
      forces the range-1 covariant law uniquely to A = 0, B = -1
  Z6  control: a mass term restores full invertibility, but changes the
      operator away from -Delta_lat
  Z7  control: a Dirichlet box restores invertibility but is NOT
      translation-invariant, which is a property the parent note derives
      FROM A2
"""

from fractions import Fraction
from itertools import product

FAILURES = []
PASSES = []


def check(name: str, ok: bool, detail: str = "") -> None:
    (PASSES if ok else FAILURES).append(name)
    print(f"[{'PASS' if ok else 'FAIL'}] {name}" + (f"  --  {detail}" if detail else ""))


# ---------------------------------------------------------------------------
# lattices
# ---------------------------------------------------------------------------


def torus_laplacian(L):
    """H = -Delta_lat on the periodic L^3 torus, exact."""
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    H = [[Fraction(0)] * n for _ in range(n)]
    for s in sites:
        i = idx[s]
        H[i][i] += Fraction(6)
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] = (t[ax] + d) % L
                H[i][idx[tuple(t)]] -= 1
    return H, sites, idx


def box_laplacian(L):
    """H on an OPEN L^3 box (Dirichlet): no wraparound."""
    sites = list(product(range(L), repeat=3))
    idx = {s: i for i, s in enumerate(sites)}
    n = len(sites)
    H = [[Fraction(0)] * n for _ in range(n)]
    for s in sites:
        i = idx[s]
        H[i][i] += Fraction(6)
        for ax in range(3):
            for d in (1, -1):
                t = list(s)
                t[ax] += d
                if 0 <= t[ax] < L:
                    H[i][idx[tuple(t)]] -= 1
    return H, sites, idx


# ---------------------------------------------------------------------------
# exact linear algebra
# ---------------------------------------------------------------------------


def rref(M):
    """Reduced row echelon form over Fraction; returns (R, pivots)."""
    R = [row[:] for row in M]
    rows, cols = len(R), len(R[0])
    piv = []
    r = 0
    for c in range(cols):
        p = next((k for k in range(r, rows) if R[k][c] != 0), None)
        if p is None:
            continue
        R[r], R[p] = R[p], R[r]
        pv = R[r][c]
        R[r] = [x / pv for x in R[r]]
        for k in range(rows):
            if k != r and R[k][c] != 0:
                f = R[k][c]
                R[k] = [a - f * b for a, b in zip(R[k], R[r])]
        piv.append(c)
        r += 1
        if r == rows:
            break
    return R, piv


def nullspace(M):
    """Exact basis of the null space."""
    R, piv = rref(M)
    cols = len(M[0])
    free = [c for c in range(cols) if c not in piv]
    basis = []
    for f in free:
        v = [Fraction(0)] * cols
        v[f] = Fraction(1)
        for r, c in enumerate(piv):
            v[c] = -R[r][f]
        basis.append(v)
    return basis


def matvec(M, v):
    return [sum(M[i][j] * v[j] for j in range(len(v))) for i in range(len(M))]


# ---------------------------------------------------------------------------
# rows
# ---------------------------------------------------------------------------


def z1_kernel_is_the_constants():
    detail = []
    ok = True
    for L in (2, 3):
        H, sites, _ = torus_laplacian(L)
        ns = nullspace(H)
        n = len(sites)
        const = [Fraction(1)] * n
        annihilates_const = all(x == 0 for x in matvec(H, const))
        dim_one = len(ns) == 1
        # the single basis vector must be proportional to the constant
        prop = False
        if dim_one:
            v = ns[0]
            nz = [x for x in v if x != 0]
            prop = bool(nz) and all(x == nz[0] for x in v)
        detail.append(f"L={L}: dim ker = {len(ns)}")
        if not (annihilates_const and dim_one and prop):
            ok = False
    check(
        "Z1 ker(-Delta_lat) on the periodic torus is exactly the constants, dimension 1",
        ok,
        "; ".join(detail),
    )


def z2_no_two_sided_inverse():
    """A singular matrix has no two-sided inverse. The proviso fails."""
    L = 3
    H, sites, _ = torus_laplacian(L)
    n = len(sites)
    _, piv = rref(H)
    rank = len(piv)
    singular = rank < n
    # explicit witness: H maps two distinct vectors to the same image
    v1 = [Fraction(0)] * n
    v2 = [Fraction(1)] * n
    same_image = matvec(H, v1) == matvec(H, v2) and v1 != v2
    check(
        "Z2 H is singular, so no two-sided inverse exists and A2's stated proviso fails",
        singular and same_image,
        f"rank {rank} of {n}; H maps 0 and the all-ones vector to the same image",
    )


def z3_pseudoinverse_convention_has_no_solution():
    """Under the repo's periodic convention, `L^{-1} = G_0` has no solution.

    BELL_INEQUALITY_DERIVED_NOTE builds the periodic Poisson Green's function
    as the "graph Laplacian pseudoinverse ... excluding the zero mode". The
    pseudoinverse has the SAME kernel as H. If `L^{-1} = G_0` then `L^{-1}` is
    invertible by definition (its inverse is L), so a singular `G_0` makes the
    identity unsatisfiable on the full space.
    """
    L = 2
    H, sites, _ = torus_laplacian(L)
    n = len(sites)

    # Build H+ explicitly rather than asserting its properties. An earlier
    # draft of this row set `pinv_annihilates_const = True` with the comment
    # "by definition of the Moore-Penrose pinv" -- a row that cannot fail.
    # Here H+ is constructed column by column: solve H x = P v with x in the
    # zero-mean sector, where P projects off the constants.
    def project_off_constants(v):
        mean = sum(v) / n
        return [x - mean for x in v]

    def solve_zero_mean(rhs):
        """Unique x with H x = rhs and sum(x) = 0, for zero-mean rhs."""
        aug = [H[i][:] + [rhs[i]] for i in range(n)]
        aug.append([Fraction(1)] * n + [Fraction(0)])  # sum(x) = 0
        R, piv = rref(aug)
        x = [Fraction(0)] * n
        for r, c in enumerate(piv):
            if c < n:
                x[c] = R[r][n]
        return x

    Hplus_cols = []
    for j in range(n):
        e = [Fraction(1) if i == j else Fraction(0) for i in range(n)]
        Hplus_cols.append(solve_zero_mean(project_off_constants(e)))
    Hplus = [[Hplus_cols[j][i] for j in range(n)] for i in range(n)]

    const = [Fraction(1)] * n
    pinv_annihilates_const = all(x == 0 for x in matvec(Hplus, const))

    # Moore-Penrose defining property on this symmetric case: H H+ = P
    HHplus = [[sum(H[i][k] * Hplus[k][j] for k in range(n)) for j in range(n)]
              for i in range(n)]
    P = [[(Fraction(1) if i == j else Fraction(0)) - Fraction(1, n)
          for j in range(n)] for i in range(n)]
    is_projector_identity = HHplus == P

    # H+ is therefore singular too
    _, piv_plus = rref([row[:] for row in Hplus])
    pinv_singular = len(piv_plus) < n

    # and no X satisfies X H = I on the full space
    _, piv = rref(H)
    no_right_inverse = len(piv) < n

    check(
        "Z3 the periodic pseudoinverse convention is also singular, so `L^{-1} = G_0` "
        "has no full-space solution",
        pinv_annihilates_const and is_projector_identity and pinv_singular
        and no_right_inverse,
        f"H+ built explicitly: H·H+ = I - J/n exactly, H+ annihilates the constants, "
        f"rank(H+) = {len(piv_plus)} < {n}, rank(H) = {len(piv)} < {n}",
    )


def _zero_mean_basis(n):
    """Exact basis of the zero-mean subspace: e_i - e_0 for i >= 1."""
    B = []
    for i in range(1, n):
        v = [Fraction(0)] * n
        v[i] = Fraction(1)
        v[0] = Fraction(-1)
        B.append(v)
    return B


def z4_invertible_on_the_zero_mean_sector():
    L = 2
    H, sites, _ = torus_laplacian(L)
    n = len(sites)
    B = _zero_mean_basis(n)
    # matrix of H restricted to the zero-mean sector, in the basis B
    # (H preserves the sector because H is symmetric and kills the constants)
    preserved = True
    for v in B:
        img = matvec(H, v)
        if sum(img) != 0:
            preserved = False
    # express H|_sector in coordinates and check it is nonsingular
    cols = []
    for v in B:
        img = matvec(H, v)
        # coordinates in B: img = sum_i c_i (e_i - e_0)  =>  c_i = img_i (i>=1)
        cols.append([img[i] for i in range(1, n)])
    M = [[cols[j][i] for j in range(len(B))] for i in range(len(B))]
    _, piv = rref(M)
    invertible = len(piv) == len(B)
    check(
        "Z4 H restricted to the zero-mean sector is invertible, so A2 determines L there",
        preserved and invertible,
        f"sector dim {len(B)}, rank {len(piv)}",
    )


def z5_covariance_closes_the_gap():
    """Matching on the zero-mean sector forces the covariant law uniquely.

    The range-1 covariant family is L = A*I + B*Delta (landed classification).
    Delta has eigenvalue Dhat(k) on each Fourier mode. Requiring L = H = -Delta
    on every nonzero mode gives, for each such k,

        A + B*Dhat(k) = -Dhat(k).

    Two distinct nonzero Dhat values make this an over-determined 2x2 system
    with the unique solution A = 0, B = -1. So the constant-mode ambiguity left
    by Z3/Z4 is closed by covariance, which the framework already supplies --
    it does NOT need to be added to A2.
    """
    L = 4
    # exact Dhat values on the L-torus: Dhat = 2*sum cos(2 pi n_i / L) - 6.
    # For L = 4 the cosines are in {1, 0, -1}, so Dhat is an exact integer.
    cos_vals = {0: Fraction(1), 1: Fraction(0), 2: Fraction(-1), 3: Fraction(0)}
    dhats = set()
    for nk in product(range(L), repeat=3):
        d = 2 * sum(cos_vals[x] for x in nk) - 6
        dhats.add(d)
    nonzero = sorted(d for d in dhats if d != 0)
    enough = len(nonzero) >= 2

    # solve A + B*d = -d on the first two distinct nonzero modes
    d1, d2 = nonzero[0], nonzero[1]
    # [1 d1][A]   [-d1]
    # [1 d2][B] = [-d2]
    det = d2 - d1
    A = (Fraction(-d1) * d2 - Fraction(-d2) * d1) / det
    B = (Fraction(-d2) - Fraction(-d1)) / det
    forced = (A == 0 and B == -1)

    # and the solution must satisfy EVERY nonzero mode, not just the two used
    consistent = all(A + B * d == -d for d in nonzero)

    # the zero mode is genuinely not used: it would read A + B*0 = 0, i.e. A = 0,
    # which is implied but not needed
    check(
        "Z5 covariance closes the gap: the zero-mean sector forces A = 0, B = -1 uniquely",
        enough and forced and consistent,
        f"{len(nonzero)} distinct nonzero Dhat values; solved A={A}, B={B}; "
        f"consistent on all of them",
    )


def z6_mass_repair_changes_the_operator():
    L = 2
    H, sites, _ = torus_laplacian(L)
    n = len(sites)
    m2 = Fraction(1, 4)
    Hm = [[H[i][j] + (m2 if i == j else 0) for j in range(n)] for i in range(n)]
    _, piv = rref(Hm)
    invertible = len(piv) == n
    differs = any(Hm[i][i] != H[i][i] for i in range(n))
    check(
        "Z6 control: a mass term restores invertibility but changes the operator",
        invertible and differs,
        f"rank {len(piv)} of {n} with m^2 = {m2}; diagonal shifted, so L != -Delta_lat",
    )


def z7_dirichlet_repair_breaks_translation_invariance():
    """The parent note derives translation invariance FROM A2 (L = H).

    If A2 needs a Dirichlet box to make G_0 exist, then H is the box operator,
    which is not translation-invariant -- so the derived property contradicts
    the repair its own antecedent requires. The parent note's CHECK 3 tests the
    stencil at "interior sites" only, which is where this shows up.
    """
    L = 3
    H, sites, idx = box_laplacian(L)
    n = len(sites)
    _, piv = rref(H)
    invertible = len(piv) == n

    # translation invariance would mean every site has the same diagonal;
    # on the box the corner and the centre differ
    corner = H[idx[(0, 0, 0)]][idx[(0, 0, 0)]]
    centre = H[idx[(1, 1, 1)]][idx[(1, 1, 1)]]
    row_sum_corner = sum(H[idx[(0, 0, 0)]])
    row_sum_centre = sum(H[idx[(1, 1, 1)]])
    not_ti = row_sum_corner != row_sum_centre

    check(
        "Z7 control: the Dirichlet repair restores invertibility but is not "
        "translation-invariant",
        invertible and not_ti,
        f"rank {len(piv)} of {n}; row sum at corner {row_sum_corner} vs centre "
        f"{row_sum_centre} -- the box annihilates no constant",
    )


def main() -> int:
    print("Cycle 708 - A2's two-sided-inverse proviso on a finite covariant lattice")
    print("=" * 74)
    z1_kernel_is_the_constants()
    z2_no_two_sided_inverse()
    z3_pseudoinverse_convention_has_no_solution()
    z4_invertible_on_the_zero_mean_sector()
    z5_covariance_closes_the_gap()
    z6_mass_repair_changes_the_operator()
    z7_dirichlet_repair_breaks_translation_invariance()
    print("=" * 74)
    print(f"{len(PASSES)} PASS / {len(FAILURES)} FAIL")
    for f in FAILURES:
        print(f"  FAILED: {f}")
    return 1 if FAILURES else 0


if __name__ == "__main__":
    raise SystemExit(main())
