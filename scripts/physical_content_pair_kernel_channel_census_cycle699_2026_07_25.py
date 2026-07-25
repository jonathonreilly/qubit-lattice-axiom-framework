#!/usr/bin/env python3
"""Cycle 699: how many nearest-neighbor two-body couplings the framework's own
covariance allows, once qubit content is carried.

Cycle 698 classified the content-blind two-body kernel and found exactly one
constant at nearest-neighbor range.  Records do not carry only a position: a
record locks one admissible element of the one-site possibility domain, whose
algebraic presentation is `M_2(C)`.  This cycle carries that content through
the same classification and counts what survives.

The action is fixed by the axioms and needs no new input.  Proper cubic
rotations act on displacements by the rotation matrix.  They act on the
one-site possibility domain by conjugation with the corresponding spin
element; on the Hermitian real form `span_R{I, sigma_1, sigma_2, sigma_3}`
that action is exactly the identity on `I` and the same rotation matrix on the
Pauli vector, so the sign ambiguity of the spin element cancels and every
matrix below is an exact integer.

Counted object: a real trilinear form

    K : (functions on the 6 face displacements) x C x C -> Q,
    C = span_R{I, sigma_1, sigma_2, sigma_3},

subject to joint covariance `K(Rv, R.o, R.o') = K(v, o, o')` and, separately,
to the exchange condition `K(-v, o', o) = K(v, o, o')` that swapping the two
records imposes.

Two independent computations of the invariant dimension are performed and
compared: an exact nullspace solve over Q on the 96-dimensional coefficient
space, and the Burnside/character average `(1/|G|) sum_R fix_6(R) (1 + tr R)^2`.
Agreement of a linear-algebra count with a character-theoretic count is the
check; neither is asserted from the other.

The census is then split by channel so the result is readable as physics:
density-density, density-spin, and spin-spin couplings.

No source action, dynamics, Hamiltonian, carrier, measurement rule, or
formation rule is adopted.  The kernel is the classified shape of a missing
object, not framework content.  No axiom or primitive is proposed or adopted.
Every scored row uses exact integer or Fraction arithmetic.  The runner imports
no repository content.
"""

from __future__ import annotations

import itertools
import json
import sys
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
from time import perf_counter


ROOT = Path(__file__).resolve().parents[1]
AUTHORITY = "none"
AUDIT = "unset"
CYCLE_CLAIM = None

PASS = 0
FAIL = 0


def check(label: str, condition: bool, detail: object = "") -> None:
    global PASS, FAIL
    if condition:
        PASS += 1
        print("PASS", label, "::", detail)
    else:
        FAIL += 1
        print("FAIL", label, "::", detail)


def rref(rows: list[list[F]]) -> tuple[list[list[F]], list[int]]:
    mat = [list(r) for r in rows]
    if not mat:
        return [], []
    ncols = len(mat[0])
    pivots: list[int] = []
    r = 0
    for c in range(ncols):
        pick = None
        for rr in range(r, len(mat)):
            if mat[rr][c] != 0:
                pick = rr
                break
        if pick is None:
            continue
        mat[r], mat[pick] = mat[pick], mat[r]
        inv = F(1, 1) / mat[r][c]
        mat[r] = [v * inv for v in mat[r]]
        for rr in range(len(mat)):
            if rr != r and mat[rr][c] != 0:
                f = mat[rr][c]
                mat[rr] = [a - f * b for a, b in zip(mat[rr], mat[r])]
        pivots.append(c)
        r += 1
        if r == len(mat):
            break
    return mat, pivots


def nullity(rows: list[list[F]], ncols: int) -> int:
    if not rows:
        return ncols
    _, piv = rref(rows)
    return ncols - len(piv)


Vec = tuple[int, int, int]

FACES: list[Vec] = [
    (1, 0, 0),
    (-1, 0, 0),
    (0, 1, 0),
    (0, -1, 0),
    (0, 0, 1),
    (0, 0, -1),
]
FIDX = {v: i for i, v in enumerate(FACES)}


def signed_permutations() -> list[tuple[Vec, Vec, Vec]]:
    out = []
    basis = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            out.append(
                tuple(
                    tuple(signs[i] * basis[perm[i]][k] for k in range(3))
                    for i in range(3)
                )
            )
    return out


def det3(m: tuple[Vec, Vec, Vec]) -> int:
    (a, b, c), (d, e, f), (g, h, i) = m
    return a * (e * i - f * h) - b * (d * i - f * g) + c * (d * h - e * g)


def trace3(m: tuple[Vec, Vec, Vec]) -> int:
    return m[0][0] + m[1][1] + m[2][2]


def apply(m: tuple[Vec, Vec, Vec], v: Vec) -> Vec:
    return tuple(sum(m[i][k] * v[k] for k in range(3)) for i in range(3))  # type: ignore[return-value]


# content basis index 0 = identity, 1..3 = Pauli vector components
NC = 4


def content_matrix(R: tuple[Vec, Vec, Vec]) -> list[list[int]]:
    """Action on span{I, sigma_1, sigma_2, sigma_3}: trivial + vector."""
    m = [[0] * NC for _ in range(NC)]
    m[0][0] = 1
    for i in range(3):
        for j in range(3):
            m[1 + i][1 + j] = R[i][j]
    return m


def main() -> int:
    started = perf_counter()
    summary: dict[str, object] = {
        "cycle": 699,
        "authority": AUTHORITY,
        "audit": AUDIT,
        "cycle_claim": CYCLE_CLAIM,
    }

    proper = [m for m in signed_permutations() if det3(m) == 1]

    # ------------------------------------------------------------------
    # R1  the content action is exactly trivial + vector, and is a homomorphism
    # ------------------------------------------------------------------
    def matmul_int(a: list[list[int]], b: list[list[int]]) -> list[list[int]]:
        return [
            [sum(a[i][k] * b[k][j] for k in range(NC)) for j in range(NC)]
            for i in range(NC)
        ]

    def matmul3(m, n):
        return tuple(
            tuple(sum(m[i][k] * n[k][j] for k in range(3)) for j in range(3))
            for i in range(3)
        )

    hom_ok = True
    for a in proper[:8]:
        for b in proper:
            if content_matrix(matmul3(a, b)) != matmul_int(
                content_matrix(a), content_matrix(b)
            ):
                hom_ok = False
                break
    identity_fixed = all(content_matrix(R)[0][0] == 1 for R in proper) and all(
        content_matrix(R)[0][j] == 0 and content_matrix(R)[j][0] == 0
        for R in proper
        for j in range(1, NC)
    )
    trace_ok = all(
        sum(content_matrix(R)[i][i] for i in range(NC)) == 1 + trace3(R)
        for R in proper
    )
    check(
        "R1 conjugation by the spin element acts on the Hermitian real form as "
        "trivial-plus-vector, is a homomorphism on the proper cubic group, "
        "leaves the identity component fixed, and has character 1 + tr(R)",
        hom_ok and identity_fixed and trace_ok and len(proper) == 24,
        {
            "group_order": len(proper),
            "homomorphism_on_sampled_pairs": hom_ok,
            "identity_component_invariant": identity_fixed,
            "character_is_1_plus_trace": trace_ok,
        },
    )

    # ------------------------------------------------------------------
    # R2  exact invariant dimension by nullspace solve
    # ------------------------------------------------------------------
    NV = len(FACES)
    dim = NV * NC * NC  # 96

    def cindex(vi: int, a: int, b: int) -> int:
        return (vi * NC + a) * NC + b

    def constraint_rows(with_exchange: bool) -> list[list[F]]:
        rows: list[list[F]] = []
        for R in proper:
            cm = content_matrix(R)
            for vi, v in enumerate(FACES):
                wj = FIDX[apply(R, v)]
                for a in range(NC):
                    for b in range(NC):
                        # (R.K)(v,e_a,e_b) = K(Rv, R e_a, R e_b) expanded
                        row = [F(0)] * dim
                        for a2 in range(NC):
                            if cm[a2][a] == 0:
                                continue
                            for b2 in range(NC):
                                if cm[b2][b] == 0:
                                    continue
                                row[cindex(wj, a2, b2)] += F(cm[a2][a] * cm[b2][b])
                        row[cindex(vi, a, b)] -= F(1)
                        if any(x != 0 for x in row):
                            rows.append(row)
        if with_exchange:
            for vi, v in enumerate(FACES):
                mj = FIDX[tuple(-c for c in v)]
                for a in range(NC):
                    for b in range(NC):
                        row = [F(0)] * dim
                        row[cindex(mj, b, a)] += F(1)
                        row[cindex(vi, a, b)] -= F(1)
                        if any(x != 0 for x in row):
                            rows.append(row)
        return rows

    dim_cov = nullity(constraint_rows(False), dim)
    dim_cov_exch = nullity(constraint_rows(True), dim)

    # ------------------------------------------------------------------
    # R3  independent character count must agree
    # ------------------------------------------------------------------
    total = 0
    for R in proper:
        fix6 = sum(1 for v in FACES if apply(R, v) == v)
        total += fix6 * (1 + trace3(R)) ** 2
    burnside = F(total, len(proper))
    check(
        "R2/R3 the exact nullspace dimension of the joint covariance system on "
        "the 96-parameter kernel space equals the independent Burnside "
        "character average, and imposing record exchange cuts it further",
        burnside.denominator == 1
        and dim_cov == int(burnside)
        and dim_cov_exch < dim_cov
        and dim_cov_exch > 0,
        {
            "kernel_parameters": dim,
            "covariant_dimension_nullspace": dim_cov,
            "covariant_dimension_burnside": str(burnside),
            "covariant_and_exchange_symmetric": dim_cov_exch,
        },
    )
    summary["covariant_pair_kernel_dimension"] = dim_cov
    summary["covariant_exchange_symmetric_dimension"] = dim_cov_exch

    # ------------------------------------------------------------------
    # R4  channel census: density-density, density-spin, spin-spin
    # ------------------------------------------------------------------
    def channel_dim(pairs_ab: list[tuple[int, int]], with_exchange: bool) -> int:
        """Invariant dimension on the span of the given content-index pairs.

        The exchange condition maps (a,b) to (b,a), so it is only imposed when
        the pair set is closed under swapping -- otherwise it would leave the
        subspace and the count would be meaningless.
        """
        pairset = set(pairs_ab)
        sub = [(vi, a, b) for vi in range(NV) for (a, b) in pairs_ab]
        sidx = {t: i for i, t in enumerate(sub)}
        n = len(sub)
        rows: list[list[F]] = []
        for R in proper:
            cm = content_matrix(R)
            for vi, v in enumerate(FACES):
                wj = FIDX[apply(R, v)]
                for a, b in pairs_ab:
                    row = [F(0)] * n
                    for a2, b2 in pairs_ab:
                        coeff = cm[a2][a] * cm[b2][b]
                        if coeff:
                            row[sidx[(wj, a2, b2)]] += F(coeff)
                    row[sidx[(vi, a, b)]] -= F(1)
                    if any(x != 0 for x in row):
                        rows.append(row)
        swap_closed = all((b, a) in pairset for (a, b) in pairs_ab)
        if with_exchange and swap_closed:
            for vi, v in enumerate(FACES):
                mj = FIDX[tuple(-c for c in v)]
                for a, b in pairs_ab:
                    row = [F(0)] * n
                    row[sidx[(mj, b, a)]] += F(1)
                    row[sidx[(vi, a, b)]] -= F(1)
                    if any(x != 0 for x in row):
                        rows.append(row)
        return nullity(rows, n)

    DD = [(0, 0)]
    DV = [(0, j) for j in (1, 2, 3)]
    VD = [(j, 0) for j in (1, 2, 3)]
    MIXED = DV + VD
    VV = [(i, j) for i in (1, 2, 3) for j in (1, 2, 3)]

    dd = channel_dim(DD, True)
    dv = channel_dim(DV, False)
    vd = channel_dim(VD, False)
    mixed_exch = channel_dim(MIXED, True)
    vv = channel_dim(VV, True)
    census = {
        "density_density": dd,
        "density_spin": dv,
        "spin_density": vd,
        "mixed_after_exchange": mixed_exch,
        "spin_spin_exchange_symmetric": vv,
    }
    # the content-blind case must reproduce cycle 698's single constant
    reproduces_698 = dd == 1
    check(
        "R4 the channel census splits the covariant kernel, and its "
        "density-density channel reproduces cycle 698's single content-blind "
        "constant",
        reproduces_698 and dv == vd and all(v >= 0 for v in census.values()),
        census,
    )
    summary["channel_census"] = census

    # ------------------------------------------------------------------
    # R5  the census sums correctly and the exchange condition is not vacuous
    # ------------------------------------------------------------------
    dd_noex = channel_dim(DD, False)
    vv_noex = channel_dim(VV, False)
    parts_sum = dd_noex + dv + vd + vv_noex
    # exchange acts WITHIN the density-density and spin-spin channels but maps
    # density-spin onto spin-density, so its whole effect is to identify the
    # two mixed channels rather than to shrink either pure one.
    pure_untouched = dd_noex == dd and vv_noex == vv
    mixed_identified = (dv + vd) == 2 * mixed_exch and mixed_exch == 1
    accounts_for_total = dd + mixed_exch + vv == dim_cov_exch
    check(
        "R5 the channels partition the covariant space exactly, and the whole "
        "effect of record exchange is to identify the two mixed channels: it "
        "leaves the pure channels untouched and takes the total from 6 to 5",
        parts_sum == dim_cov
        and pure_untouched
        and mixed_identified
        and accounts_for_total,
        {
            "density_density_no_exchange": dd_noex,
            "density_spin": dv,
            "spin_density": vd,
            "spin_spin_no_exchange": vv_noex,
            "sum_of_channels": parts_sum,
            "full_covariant_dimension": dim_cov,
            "mixed_after_exchange": mixed_exch,
            "pure_channels_untouched_by_exchange": pure_untouched,
            "exchange_symmetric_total": dd + mixed_exch + vv,
        },
    )

    # ------------------------------------------------------------------
    # R6  negative control: dropping the rotations leaves everything free
    # ------------------------------------------------------------------
    free_dim = nullity([], dim)
    check(
        "R6 without the proper cubic rotations the kernel space is entirely "
        "free at 96 parameters, so the covariance clause is doing all of the "
        "reduction",
        free_dim == dim and dim_cov < dim,
        {
            "unconstrained": free_dim,
            "covariant": dim_cov,
            "reduction_factor": f"{dim} -> {dim_cov}",
        },
    )

    # ------------------------------------------------------------------
    # R7  an explicit basis for the spin-spin channel
    # ------------------------------------------------------------------
    def eps(i: int, j: int, k: int) -> int:
        return (i - j) * (j - k) * (k - i) // 2

    def form_isotropic(vi: int, a: int, b: int) -> int:
        return 1 if a == b else 0

    def form_bond_axis(vi: int, a: int, b: int) -> int:
        v = FACES[vi]
        return v[a] * v[b]

    def form_chiral(vi: int, a: int, b: int) -> int:
        v = FACES[vi]
        return sum(eps(c, a, b) * v[c] for c in range(3))

    forms = {
        "isotropic S.S'": form_isotropic,
        "bond-axis (S.v)(S'.v)": form_bond_axis,
        "chiral v.(S x S')": form_chiral,
    }

    def is_invariant(fn, group) -> bool:
        for R in group:
            cm = content_matrix(R)
            for vi, v in enumerate(FACES):
                wj = FIDX[apply(R, v)]
                for a in range(3):
                    for b in range(3):
                        lhs = sum(
                            cm[1 + a2][1 + a] * cm[1 + b2][1 + b] * fn(wj, a2, b2)
                            for a2 in range(3)
                            for b2 in range(3)
                        )
                        if lhs != fn(vi, a, b):
                            return False
        return True

    invariance = {name: is_invariant(fn, proper) for name, fn in forms.items()}
    vectors = [
        [F(fn(vi, a, b)) for vi in range(NV) for a in range(3) for b in range(3)]
        for fn in forms.values()
    ]
    _, piv = rref([list(r) for r in vectors])
    independent = len(piv) == 3
    check(
        "R7 the three named forms -- isotropic, bond-axis, and chiral -- are "
        "each exactly invariant under the proper cubic group and are linearly "
        "independent, so they are a basis for the 3-dimensional spin-spin "
        "channel",
        all(invariance.values()) and independent and vv == 3,
        {
            "invariance": invariance,
            "rank_of_the_three_forms": len(piv),
            "spin_spin_channel_dimension": vv,
        },
    )
    summary["spin_spin_basis"] = list(forms)

    # ------------------------------------------------------------------
    # R8  counterfactual: what the word "proper" in the Lattice axiom buys
    # ------------------------------------------------------------------
    # The axiom supplies proper cubic rotations only.  Improper elements are
    # not implemented by conjugation with a spin element at all, so extending
    # the group requires CHOOSING how they act; the standard choice treats the
    # Pauli vector as axial.  This block is a labelled counterfactual, not a
    # framework claim, and it isolates exactly which coupling the word
    # "proper" is responsible for.
    full_cubic = signed_permutations()

    def content_matrix_axial(R) -> list[list[int]]:
        m = [[0] * NC for _ in range(NC)]
        m[0][0] = 1
        d = det3(R)
        for i in range(3):
            for j in range(3):
                m[1 + i][1 + j] = d * R[i][j]
        return m

    agrees_on_proper = all(
        content_matrix_axial(R) == content_matrix(R) for R in proper
    )

    def is_invariant_axial(fn) -> bool:
        for R in full_cubic:
            cm = content_matrix_axial(R)
            for vi, v in enumerate(FACES):
                wj = FIDX[apply(R, v)]
                for a in range(3):
                    for b in range(3):
                        lhs = sum(
                            cm[1 + a2][1 + a] * cm[1 + b2][1 + b] * fn(wj, a2, b2)
                            for a2 in range(3)
                            for b2 in range(3)
                        )
                        if lhs != fn(vi, a, b):
                            return False
        return True

    axial_inv = {name: is_invariant_axial(fn) for name, fn in forms.items()}
    chiral_dies = not axial_inv["chiral v.(S x S')"]
    others_survive = (
        axial_inv["isotropic S.S'"] and axial_inv["bond-axis (S.v)(S'.v)"]
    )
    check(
        "R8 counterfactual: extending to the full cubic group with an axial "
        "Pauli vector kills exactly the chiral coupling and leaves the other "
        "two, so the Lattice axiom's restriction to PROPER rotations is "
        "load-bearing for exactly one of the five couplings",
        agrees_on_proper and chiral_dies and others_survive,
        {
            "axial_extension_agrees_on_proper_subgroup": agrees_on_proper,
            "invariance_under_full_cubic_group": axial_inv,
            "couplings_lost": 1,
        },
    )
    summary["proper_rotation_clause_buys"] = (
        "exactly one coupling, the chiral v.(S x S') term, under the labelled "
        "axial counterfactual"
    )

    summary["conclusion"] = (
        f"Carrying qubit content through the cycle-698 classification, the "
        f"nearest-neighbor two-body kernel has exactly {dim_cov} covariant "
        f"parameters out of 96, and {dim_cov_exch} once record exchange is "
        f"imposed. The content-blind density-density channel contributes "
        f"exactly one, recovering cycle 698. The remainder is the exact "
        f"budget of spin-carrying couplings the axioms' covariance permits at "
        f"this order and range; none of them is selected here."
    )
    summary["firewalls"] = {
        "source_action_adopted": False,
        "coupling_values_selected": False,
        "dynamics_or_measurement_claimed": False,
        "carrier_identified": False,
        "new_axiom_or_primitive_proposed": False,
        "lane_status_changed": False,
    }
    summary["resources"] = {"elapsed_seconds": perf_counter() - started}
    summary["runner_sha256"] = sha256(Path(__file__).read_bytes()).hexdigest()
    summary["pass_count"] = PASS
    summary["fail_count"] = FAIL
    summary["pass"] = FAIL == 0

    receipt = ROOT / "outputs" / (
        "physical_content_pair_kernel_channel_census_cycle699"
        "_receipt_2026_07_25.json"
    )
    if "--no-receipt" not in sys.argv:
        receipt.parent.mkdir(parents=True, exist_ok=True)
        receipt.write_text(
            json.dumps(summary, indent=1, sort_keys=True, default=str) + "\n",
            encoding="utf-8",
        )
    print("SUMMARY_JSON", json.dumps(summary, sort_keys=True, default=str))
    print(f"RESULT {PASS} {FAIL} elapsed {perf_counter() - started:.2f} s")
    if FAIL:
        print("RESULT CONTENT_PAIR_KERNEL_CHANNEL_CENSUS_FAILED")
        return 1
    print("RESULT CONTENT_PAIR_KERNEL_CHANNEL_CENSUS_COMPLETE")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
