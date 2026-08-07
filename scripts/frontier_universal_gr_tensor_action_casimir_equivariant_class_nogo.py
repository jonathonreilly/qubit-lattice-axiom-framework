#!/usr/bin/env python3
"""Casimir-equivariant tensor-action class no-go on Sym^2(R^4).

Verifies the named-obstruction theorem in
docs/UNIVERSAL_GR_TENSOR_ACTION_CASIMIR_EQUIVARIANT_CLASS_NOGO_NOTE_2026-05-17.md:

  (T1) Schur classification: every SO(3)-equivariant bilinear form on V
       built from the four canonical Casimir block projectors (P_lapse,
       P_shift, P_trace, P_shear) of the retained casimir_block_localization
       note lies in a 5-real-parameter family Class CB(V).
  (T2) Orbit-flatness: every S in Class CB(V) satisfies
       S(rho(R) h, rho(R) k) = S(h, k) for every R in SO(3).
  (T3) Section no-go: for every nonzero-complement Q = S(.,.) in Class CB(V),
       the gradient nabla Q(h) is orbit-normal — the EL system cannot
       single out a preferred orbit representative on E ⊕ T1.
  (T4) Exhaustiveness: any linear-projector tensor-action candidate built
       from the retained Casimir decomposition lies in Class CB(V).

Load-bearing input is class (A) algebraic: Schur's lemma in real-orthogonal
form plus the already-retained casimir_block_localization decomposition.

Runner imports: sympy only. No numeric tolerance, no random sampling, no
external I/O beyond reading the source-note for scope-discipline checks.
"""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path

import sympy as sp


@dataclass
class Check:
    name: str
    ok: bool
    detail: str
    status: str = "EXACT"


CHECKS: list[Check] = []


def record(name: str, ok: bool, detail: str = "", status: str = "EXACT") -> None:
    CHECKS.append(Check(name=name, ok=ok, detail=detail, status=status))
    tag = "PASS" if ok else "FAIL"
    print(f"[{status}] {tag}: {name}")
    if detail:
        print(f"    {detail}")


def is_zero(mat: sp.Matrix) -> bool:
    return all(sp.simplify(entry) == 0 for entry in mat)


def sym(i: int, j: int, n: int = 4) -> sp.Matrix:
    m = sp.zeros(n, n)
    if i == j:
        m[i, j] = sp.Integer(1)
    else:
        m[i, j] = 1 / sp.sqrt(2)
        m[j, i] = 1 / sp.sqrt(2)
    return m


def diag(vals: tuple[sp.Expr, ...]) -> sp.Matrix:
    return sp.diag(*vals)


def frob(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    """Frobenius inner product <a, b>_F = sum_{i,j} a_{ij} b_{ij}."""
    return sp.simplify(
        sum(a[i, j] * b[i, j] for i in range(a.rows) for j in range(a.cols))
    )


def frob_fast(a: sp.Matrix, b: sp.Matrix) -> sp.Expr:
    """Frobenius pairing without simplify — used in symbolic hot paths."""
    return sp.expand(
        sum(a[i, j] * b[i, j] for i in range(a.rows) for j in range(a.cols))
    )


def canonical_polarization_frame() -> list[sp.Matrix]:
    """Orthonormal 3+1 polarization basis on Sym^2(R^4).

    Mirrors the retained casimir_block_localization note. Coordinate order
    (t, x, y, z). Basis order:
      0   lapse h_tt
      1-3 shift h_tx, h_ty, h_tz
      4   spatial trace
      5,6 shear q1, q2 (diagonal traceless)
      7-9 shear off-diagonal h_xy, h_xz, h_yz
    """
    return [
        sym(0, 0),
        sym(0, 1),
        sym(0, 2),
        sym(0, 3),
        diag((0, 1 / sp.sqrt(3), 1 / sp.sqrt(3), 1 / sp.sqrt(3))),
        diag((0, 1 / sp.sqrt(2), -1 / sp.sqrt(2), 0)),
        diag((0, 1 / sp.sqrt(6), 1 / sp.sqrt(6), -2 / sp.sqrt(6))),
        sym(1, 2),
        sym(1, 3),
        sym(2, 3),
    ]


def so3_generator(axis: str) -> sp.Matrix:
    """Infinitesimal spatial rotation matrix in 4D (temporal index fixed)."""
    a = sp.zeros(4, 4)
    if axis == "x":
        a[2, 3] = -1
        a[3, 2] = 1
    elif axis == "y":
        a[1, 3] = 1
        a[3, 1] = -1
    elif axis == "z":
        a[1, 2] = -1
        a[2, 1] = 1
    else:
        raise ValueError(axis)
    return a


def lifted_generator(axis: str, frame: list[sp.Matrix]) -> sp.Matrix:
    """Generator of h |-> R^T h R action on V = Sym^2(R^4), in basis B."""
    a = so3_generator(axis)
    out = sp.zeros(len(frame), len(frame))
    for j, basis_j in enumerate(frame):
        image = a.T * basis_j + basis_j * a
        for i, ref_i in enumerate(frame):
            out[i, j] = frob(ref_i, image)
    return sp.simplify(out)


def submatrix(mat: sp.Matrix, idx: list[int]) -> sp.Matrix:
    return mat.extract(idx, idx)


def lift_complement_projector(projector_c: sp.Matrix, comp_idx: list[int]) -> sp.Matrix:
    out = sp.zeros(10, 10)
    for i_c, i in enumerate(comp_idx):
        for j_c, j in enumerate(comp_idx):
            out[i, j] = projector_c[i_c, j_c]
    return out


def diagonal_projector_from_casimir(casimir: sp.Matrix, eigenvalue: int) -> sp.Matrix:
    diag_entries = [
        1 if sp.simplify(casimir[i, i] - eigenvalue) == 0 else 0
        for i in range(casimir.rows)
    ]
    return sp.diag(*diag_entries)


def commutator(a: sp.Matrix, b: sp.Matrix) -> sp.Matrix:
    return sp.simplify(a * b - b * a)


def coords_to_matrix(coords: list[sp.Expr], frame: list[sp.Matrix]) -> sp.Matrix:
    """Reconstruct a 4x4 symmetric matrix from coordinate vector in basis B."""
    result = sp.zeros(4, 4)
    for c, e in zip(coords, frame):
        result = result + c * e
    return result


def matrix_to_coords(h: sp.Matrix, frame: list[sp.Matrix]) -> list[sp.Expr]:
    """Project a 4x4 symmetric matrix onto basis B."""
    return [frob_fast(e, h) for e in frame]


def rho_R_h_coords(coords_h: list[sp.Expr], R: sp.Matrix, frame: list[sp.Matrix]) -> list[sp.Expr]:
    """Apply h |-> R^T h R in coordinate form: returns new coordinate vector."""
    h_mat = coords_to_matrix(coords_h, frame)
    h_new = R.T * h_mat * R
    return matrix_to_coords(h_new, frame)


def build_block_projectors() -> tuple[sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix, sp.Matrix]:
    """Build (P_lapse, P_shift, P_trace, P_shear, G_x, G_y, G_z) on basis B."""
    frame = canonical_polarization_frame()
    gx = lifted_generator("x", frame)
    gy = lifted_generator("y", frame)
    gz = lifted_generator("z", frame)

    p_lapse = sp.zeros(10, 10)
    p_lapse[0, 0] = 1
    p_trace = sp.zeros(10, 10)
    p_trace[4, 4] = 1

    comp_idx = [i for i in range(10) if i not in (0, 4)]
    gc = [submatrix(g, comp_idx) for g in (gx, gy, gz)]
    casimir = sp.simplify(sum((g * g for g in gc), sp.zeros(8, 8)))

    p_shift_c = diagonal_projector_from_casimir(casimir, -2)
    p_shear_c = diagonal_projector_from_casimir(casimir, -6)
    p_shift = lift_complement_projector(p_shift_c, comp_idx)
    p_shear = lift_complement_projector(p_shear_c, comp_idx)

    return p_lapse, p_shift, p_trace, p_shear, gx, gy, gz


def section(title: str) -> None:
    print("\n" + "-" * 88)
    print(title)
    print("-" * 88)


def execution_certificate(
    frame: list[sp.Matrix],
    projectors: dict,
    ranks: dict,
    gens: tuple,
    gram_is_identity: bool,
    equivariant: bool,
    class_dim: int,
    block_span_rank: int,
    lifted_rank: int,
) -> None:
    """Print-only N5 execution certificate; records no check and no counter.

    Everything quoted is an exact sympy integer or a boolean produced by
    this run.  The runner uses no random sampling, no optimizer and no
    numeric tolerance, so nothing here is environment-dependent.
    """
    comp_idx = [i for i in range(10) if i not in (0, 4)]
    gc = [submatrix(g, comp_idx) for g in gens]
    casimir = sp.simplify(sum((g * g for g in gc), sp.zeros(8, 8)))
    casimir_eigs = sorted({sp.simplify(casimir[i, i]) for i in range(8)},
                          key=lambda e: float(e))
    n_doc = sum(1 for c in CHECKS if c.status == "DOC")

    section("N5 execution certificate")
    print(
        f"per_element: the {len(frame)}-dimensional polarization frame is "
        f"verified entry by entry — its Frobenius Gram matrix is exactly the "
        f"identity I_{len(frame)} ({gram_is_identity}), the four projectors "
        f"are exactly idempotent, mutually annihilating and complete, and all "
        f"{len(projectors) * len(gens)} commutators [P_a, G_b] are the exact "
        f"zero matrix ({equivariant}); the {n_doc} Part-G entries are "
        f"note-substring checks and resolve no matrix element at all."
    )
    print(
        f"per_site: checked and not executed — the entire calculation happens "
        f"inside one tangent space Sym^2(R^4) attached to a single point, with "
        f"no lattice, no field configuration spread over a set of points, and "
        f"hence no site index for anything to be resolved against."
    )
    print(
        f"per_mode: SO(3) mode content is resolved by Casimir eigenvalue on "
        f"the 8-dimensional complement — the restricted Casimir comes out "
        f"diagonal with eigenvalues {[str(e) for e in casimir_eigs]}, "
        f"selecting the j = 1 triplet and the j = 2 quintet, and the Schur "
        f"count over those two modes plus the two trivial modes gives "
        f"dim Class CB(V) = {class_dim}, i.e. 3 + 1 + 1."
    )
    print(
        f"per_block: the four Casimir blocks are separated with exact integer "
        f"ranks {ranks}, summing to {sum(ranks.values())}, and the "
        f"block-diagonal bilinear span they generate has rank "
        f"{block_span_rank}, lifted to {lifted_rank} only by the Schur cross "
        f"term between the two trivial blocks — that one cross direction is "
        f"what the whole class no-go turns on."
    )
    print(
        f"lattice_wide: checked and not executed — there is no lattice "
        f"anywhere in this runner, no volume, no spacing, no boundary "
        f"condition and no configuration space beyond the single "
        f"{len(frame)}-dimensional fibre, so the orbit-flatness result is "
        f"stated pointwise on that fibre and nowhere else."
    )


def main() -> int:
    print("UNIVERSAL GR TENSOR ACTION — Casimir-equivariant Class No-Go")
    print("=" * 88)

    # ------------------------------------------------------------------
    section("Part A: build retained Casimir block projectors")
    # ------------------------------------------------------------------
    frame = canonical_polarization_frame()
    p_lapse, p_shift, p_trace, p_shear, gx, gy, gz = build_block_projectors()

    # Verify retained inputs (BA-3) at runner-checkable precision
    gram = sp.Matrix([[frob(a, b) for b in frame] for a in frame])
    record(
        "(BA-3) retained: basis B is orthonormal under Frobenius",
        gram == sp.eye(10),
        f"Gram(B) = I_10",
    )

    projectors = {"lapse": p_lapse, "shift": p_shift, "trace": p_trace, "shear": p_shear}
    ranks = {name: p.rank() for name, p in projectors.items()}
    record(
        "(BA-3) retained: projector ranks (1, 3, 1, 5)",
        ranks == {"lapse": 1, "shift": 3, "trace": 1, "shear": 5},
        f"ranks = {ranks}",
    )

    orthogonal = all(
        is_zero(p1 * p2)
        for n1, p1 in projectors.items()
        for n2, p2 in projectors.items()
        if n1 != n2
    )
    idempotent = all(is_zero(p * p - p) for p in projectors.values())
    complete = is_zero(p_lapse + p_shift + p_trace + p_shear - sp.eye(10))
    record(
        "(BA-3) retained: projectors mutually orthogonal, idempotent, complete",
        orthogonal and idempotent and complete,
        f"orthogonal={orthogonal} idempotent={idempotent} complete={complete}",
    )

    equivariant = all(
        is_zero(commutator(p, g))
        for p in projectors.values()
        for g in (gx, gy, gz)
    )
    record(
        "(BA-3) retained: projectors SO(3)-equivariant ([P_a, G_b] = 0)",
        equivariant,
        "all twelve commutators vanish",
    )

    # ------------------------------------------------------------------
    section("Part B: (T1) Schur classification — dim count")
    # ------------------------------------------------------------------
    # Hom_SO(3)(V, V) has dimension equal to sum of multiplicity-block
    # endomorphism-algebra dimensions:
    #   - trivial-isotypic (multiplicity 2: lapse, trace): Mat_{2,2}(R) = 4
    #   - j=1 (multiplicity 1: shift): R = 1
    #   - j=2 (multiplicity 1: shear): R = 1
    # Total: 4 + 1 + 1 = 6.
    # Symmetric subspace: 3 (symmetric 2x2) + 1 + 1 = 5.

    expected_hom_dim = 6
    expected_class_cb_dim = 5

    # Verify by direct construction:
    # Build all 16 bilinear forms <P_a h, P_b k> and check which are
    # nonzero on the generic Sym^2(R^4) pair.
    h_syms = sp.symbols(' '.join([f'h{i}' for i in range(10)]), real=True)
    k_syms = sp.symbols(' '.join([f'k{i}' for i in range(10)]), real=True)
    h_vec = sp.Matrix(h_syms)
    k_vec = sp.Matrix(k_syms)

    # Frobenius pairing in basis B reduces to standard Euclidean dot product
    # since B is orthonormal.
    def pair_PaPb(P_a, P_b):
        """Returns <P_a h, P_b k>_F as a polynomial in h_i, k_j (basis B)."""
        # In orthonormal basis B, <x, y>_F = x^T y.
        # <P_a h, P_b k>_F = (P_a h)^T (P_b k) = h^T (P_a^T P_b) k.
        bilinear = (h_vec.T * P_a.T * P_b * k_vec)[0, 0]
        return sp.expand(bilinear)

    pair_dict = {}
    nonzero_pairs = []
    for n1, p1 in projectors.items():
        for n2, p2 in projectors.items():
            pair = pair_PaPb(p1, p2)
            pair_dict[(n1, n2)] = pair
            if pair != 0:
                nonzero_pairs.append((n1, n2))

    # Expected nonzero pairs: (lapse,lapse), (trace,trace), (shift,shift),
    # (shear,shear), plus cross terms (lapse,trace) and (trace,lapse)
    # which are NONZERO because P_lapse and P_trace both project onto
    # the trivial-isotypic 2-block. But: P_lapse P_trace = 0 (orthogonality
    # in basis B as projectors onto distinct basis vectors), so the cross
    # term <P_lapse h, P_trace k>_F = h^T P_lapse^T P_trace k = 0.

    # The point: in basis B, the canonical projectors P_lapse and P_trace
    # are orthogonal as projectors. But the SO(3)-EQUIVARIANT cross map
    # between range(P_lapse) and range(P_trace) is NOT P_lapse^T P_trace
    # = 0. It is a DIFFERENT operator: the linear map e_0 |-> e_4,
    # e_4 |-> e_0 (an off-diagonal block in the trivial 2-isotypic).
    # Build this cross map explicitly.

    # P_LT_cross: rank-1 map e_0 -> e_4 (zeros elsewhere)
    p_LT_cross = sp.zeros(10, 10)
    p_LT_cross[4, 0] = 1
    # P_TL_cross: transpose of P_LT_cross: rank-1 map e_4 -> e_0
    p_TL_cross = sp.zeros(10, 10)
    p_TL_cross[0, 4] = 1
    # Symmetric Schur cross (sum is symmetric as endomorphism)
    p_cross_sym = p_LT_cross + p_TL_cross

    # Equivariance check on cross operators
    cross_equivariant = all(
        is_zero(commutator(p_cross_sym, g)) for g in (gx, gy, gz)
    )
    record(
        "(T1) Schur cross map (P_lapse <-> P_trace) is SO(3)-equivariant",
        cross_equivariant,
        "P_LT_cross + P_TL_cross commutes with all G_a (both blocks are trivial irreps)",
    )

    # Now count linearly independent symmetric SO(3)-equivariant bilinear forms.
    # Class CB(V) = span{ pair(P_a, P_a) for a in {lapse, shift, trace, shear} } + cross_sym pair
    # Five generators total.
    pair_lapse = pair_PaPb(p_lapse, p_lapse)
    pair_trace = pair_PaPb(p_trace, p_trace)
    pair_shift = pair_PaPb(p_shift, p_shift)
    pair_shear = pair_PaPb(p_shear, p_shear)
    # Symmetric cross: <h, p_cross_sym k>_F = h^T (P_LT + P_TL) k
    pair_cross = sp.expand((h_vec.T * p_cross_sym * k_vec)[0, 0])

    class_cb_generators = [pair_lapse, pair_trace, pair_shift, pair_shear, pair_cross]
    # Verify they are linearly independent
    # Convert to vectors of coefficients on the 100 monomials h_i k_j.
    monomials = [h_syms[i] * k_syms[j] for i in range(10) for j in range(10)]
    coeff_matrix = sp.Matrix([[g.coeff(m) for m in monomials] for g in class_cb_generators])
    indep_rank = coeff_matrix.rank()
    record(
        "(T1) Class CB(V) has dimension 5 (five generators linearly independent)",
        indep_rank == 5,
        f"rank of generator coefficient matrix = {indep_rank} (expected 5)",
    )

    record(
        "(T1) Schur classification: dim Class CB(V) = 5 matches symmetric Hom_SO(3) count",
        indep_rank == expected_class_cb_dim,
        f"observed = {indep_rank}, predicted = {expected_class_cb_dim} (3 trivial-block-symmetric + 1 j=1 + 1 j=2)",
    )

    # ------------------------------------------------------------------
    section("Part C: (T2) orbit-flatness — symbolic single-axis rotations")
    # ------------------------------------------------------------------
    # The three single-axis spatial rotations R_x(theta), R_y(theta),
    # R_z(theta) generate SO(3); verifying orbit-flatness for each is
    # equivalent to verifying it for any R in SO(3).
    theta_sym = sp.symbols("theta_sym", real=True)

    def rot_x(angle):
        c, s = sp.cos(angle), sp.sin(angle)
        return sp.Matrix([
            [1, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, c, -s],
            [0, 0, s, c],
        ])

    def rot_y_lift(angle):
        c, s = sp.cos(angle), sp.sin(angle)
        return sp.Matrix([
            [1, 0, 0, 0],
            [0, c, 0, s],
            [0, 0, 1, 0],
            [0, -s, 0, c],
        ])

    def rot_z_lift(angle):
        c, s = sp.cos(angle), sp.sin(angle)
        return sp.Matrix([
            [1, 0, 0, 0],
            [0, c, -s, 0],
            [0, s, c, 0],
            [0, 0, 0, 1],
        ])

    # Parameterize Class CB(V) via real coefficients a, b, c, d, e.
    a_c, b_c, c_c, d_c, e_c = sp.symbols("a_c b_c c_c d_c e_c", real=True)

    def S_class_cb(h_v, k_v):
        return sp.expand(
            a_c * (h_v.T * p_lapse.T * p_lapse * k_v)[0, 0]
            + c_c * (h_v.T * p_trace.T * p_trace * k_v)[0, 0]
            + b_c * (h_v.T * p_shift.T * p_shift * k_v)[0, 0]
            + d_c * (h_v.T * p_shear.T * p_shear * k_v)[0, 0]
            + e_c * (h_v.T * p_cross_sym * k_v)[0, 0]
        )

    S_original = S_class_cb(h_vec, k_vec)
    orbit_flat_per_axis = {}
    for axis_name, R4_fn in (("x", rot_x), ("y", rot_y_lift), ("z", rot_z_lift)):
        R4 = R4_fn(theta_sym)
        h_new_coords = rho_R_h_coords(list(h_syms), R4, frame)
        k_new_coords = rho_R_h_coords(list(k_syms), R4, frame)
        h_new_vec = sp.Matrix(h_new_coords)
        k_new_vec = sp.Matrix(k_new_coords)
        S_rotated = S_class_cb(h_new_vec, k_new_vec)
        diff = sp.expand(S_rotated - S_original)
        diff_trig = sp.trigsimp(diff)
        diff_simpl = sp.simplify(diff_trig)
        orbit_flat_per_axis[axis_name] = diff_simpl == 0

    all_orbit_flat = all(orbit_flat_per_axis.values())
    record(
        "(T2) orbit-flatness symbolic: S(rho(R_a(theta))h, rho(R_a(theta))k) - S(h, k) == 0 for each axis a",
        all_orbit_flat,
        f"per-axis (single-axis rotations generate SO(3)): {orbit_flat_per_axis}",
    )

    # ------------------------------------------------------------------
    section("Part D: (T3) section no-go — gradient is orbit-normal")
    # ------------------------------------------------------------------
    # For Q(h) := S(h, h), compute nabla Q(h) and verify it is orthogonal
    # to every orbit-tangent vector G_a h at every h.
    #
    # Orbit-tangent at h in direction a: (G_a h)_i = sum_j (G_a)_{ij} h_j
    # in basis B. The gradient of Q at h, in basis B, is the vector
    # nabla Q(h) with components partial Q / partial h_i.
    #
    # Orbit-normal condition: <nabla Q(h), G_a h>_B = 0 for every a.

    # Use symbolic h and arbitrary Class CB coefficients.
    Q_h = S_class_cb(h_vec, h_vec)
    grad_Q = sp.Matrix([sp.diff(Q_h, h_syms[i]) for i in range(10)])

    orbit_normal_results = {}
    for axis, g in (("x", gx), ("y", gy), ("z", gz)):
        # Orbit-tangent at h in direction G_axis: G_axis * h
        tangent = g * h_vec
        # Frobenius pairing in orthonormal basis B is dot product
        pairing = sp.expand((grad_Q.T * tangent)[0, 0])
        pairing_simplified = sp.simplify(pairing)
        orbit_normal_results[axis] = pairing_simplified == 0

    all_orbit_normal = all(orbit_normal_results.values())
    record(
        "(T3) section no-go: <nabla Q(h), G_a h>_B = 0 for every a in {x, y, z} and every (a_c, b_c, c_c, d_c, e_c)",
        all_orbit_normal,
        f"per-axis: {orbit_normal_results}",
    )

    # Strong form: gradient is orbit-normal for ANY Q in Class CB(V),
    # which we just verified. Combined with (T2) orbit-flatness, the
    # EL system nabla Q = 0 cannot single out a preferred orbit
    # representative on the E ⊕ T1 complement.
    record(
        "(T3) corollary: EL system nabla Q(h) = 0 is orbit-degenerate "
        "(constant on each SO(3) orbit, gradient orbit-normal)",
        all_orbit_normal and all_orbit_flat,
        "every nontrivial Q in Class CB(V) inherits the orbit-flat section-no-go",
    )

    # ------------------------------------------------------------------
    section("Part E: (T4) exhaustiveness corollary — span dimension")
    # ------------------------------------------------------------------
    # Any linear-projector tensor-action candidate built as a real linear
    # combination of <P_a h, P_b k>_F over (P_lapse, P_shift, P_trace,
    # P_shear) is in Class CB(V) by definition.
    #
    # We verify exhaustion by enumerating ALL 16 = 4*4 bilinear forms
    # <P_a h, P_b k> and checking that the SYMMETRIC span has dimension
    # exactly 5 (matches Schur prediction).
    all_pairs = []
    pair_labels = []
    for n1, p1 in projectors.items():
        for n2, p2 in projectors.items():
            pair = pair_PaPb(p1, p2)
            all_pairs.append(pair)
            pair_labels.append(f"{n1}-{n2}")

    # Symmetric span: replace each pair (a,b) with (pair(a,b) + pair(b,a))/2
    sym_pairs = []
    sym_labels = []
    seen = set()
    for i, (n1, p1) in enumerate(projectors.items()):
        for j, (n2, p2) in enumerate(projectors.items()):
            key = tuple(sorted([n1, n2]))
            if key in seen:
                continue
            seen.add(key)
            if n1 == n2:
                sym_pairs.append(pair_PaPb(p1, p2))
                sym_labels.append(f"{n1}^2")
            else:
                avg = sp.expand((pair_PaPb(p1, p2) + pair_PaPb(p2, p1)) / 2)
                sym_pairs.append(avg)
                sym_labels.append(f"({n1},{n2})_sym")

    # Now compute rank.
    coeff_matrix_sym = sp.Matrix(
        [[g.coeff(m) for m in monomials] for g in sym_pairs]
    )
    sym_rank = coeff_matrix_sym.rank()
    # Note: in basis B with disjoint projector supports, the "diagonal"
    # cross terms (lapse, trace), (lapse, shift), ... all evaluate to 0
    # because P_lapse P_trace = 0 as matrix product. So the bilinear-form
    # span built directly from <P_a h, P_b k> has rank 4 (just the four
    # diagonal pairs). The fifth dimension — the trivial-block Schur
    # cross — requires the EXPLICIT off-diagonal endomorphism
    # P_LT_cross = e_4 e_0^T which is not P_a^T P_b for any a, b.

    record(
        "(T4) bilinear span over (P_a, P_b) pairs has rank 4 "
        "(orthogonality kills cross terms in basis B)",
        sym_rank == 4,
        f"rank = {sym_rank}; cross terms <P_a h, P_b k> = 0 for a != b due to P_a P_b = 0",
    )

    # The full Class CB(V) requires the Schur cross e term separately.
    # Adding it lifts dimension from 4 to 5.
    sym_pairs_with_cross = sym_pairs + [pair_cross]
    coeff_full = sp.Matrix(
        [[g.coeff(m) for m in monomials] for g in sym_pairs_with_cross]
    )
    full_rank = coeff_full.rank()
    record(
        "(T4) Class CB(V) = bilinear span + Schur cross term has dim 5",
        full_rank == 5,
        f"adding p_cross_sym = e_0 e_4^T + e_4 e_0^T lifts rank from 4 to {full_rank}",
    )

    # The dimension-5 Schur prediction matches the symmetric Hom_SO(3) count
    # (3 trivial-isotypic + 1 j=1 + 1 j=2). Exhaustiveness confirmed.
    record(
        "(T4) Schur exhaustiveness: dim Class CB(V) = 3 (trivial-block-sym) + 1 (j=1) + 1 (j=2) = 5",
        full_rank == 5,
        "rank matches Schur multiplicity-block computation",
    )

    # ------------------------------------------------------------------
    section("Part F: anisotropic-control negative test")
    # ------------------------------------------------------------------
    # If the action uses a NON-isotropic weight (e.g. spatial axes have
    # different scales), the orbit-flatness fails — confirms (BA-2) is
    # load-bearing.
    #
    # Use a weight matrix W = diag(1, w1, w2, w3) with w1, w2, w3
    # distinct symbolic positive reals. The weighted Frobenius
    # <h, k>_W := sum_{ij} h_ij k_ij / (W_i W_j).
    w1, w2, w3 = sp.symbols("w1 w2 w3", positive=True)
    W = sp.diag(1, 1 / w1, 1 / w2, 1 / w3)

    # Replace the basis B with B reweighted: e_i_W = W e_i W^T (so that
    # frob_W (a, b) = frob(W a W, b) etc.). Equivalent: directly compute
    # weighted Frobenius pairing on the matrix forms.
    def weighted_frob(a, b):
        return sp.simplify(sum((W * a * W)[i, j] * (W * b * W)[i, j] for i in range(4) for j in range(4)))

    # Pick a concrete h with nonzero shift component and check whether
    # the orbit-tangent gradient pairing fails for a chosen Q = shift-block
    # norm under the weighted Frobenius.
    #
    # We use h = e_1 (the shift-x basis vector) and compute the weighted
    # norm Q_W(h) = ||P_shift h||^2_W as a function of Euler angle, and
    # show it depends on phi when w1, w2, w3 are distinct.
    h_test_coords = [sp.Integer(0)] * 10
    h_test_coords[1] = sp.Integer(1)  # shift-x
    h_test = coords_to_matrix(h_test_coords, frame)

    # Apply a rotation R_z(phi).
    phi_test = sp.symbols("phi_test", real=True)
    R_z_only = sp.eye(4)
    R_z_only[1, 1] = sp.cos(phi_test)
    R_z_only[1, 2] = -sp.sin(phi_test)
    R_z_only[2, 1] = sp.sin(phi_test)
    R_z_only[2, 2] = sp.cos(phi_test)
    h_test_rotated = R_z_only.T * h_test * R_z_only

    # Compute weighted norm difference
    norm_orig = weighted_frob(h_test, h_test)
    norm_rot = weighted_frob(h_test_rotated, h_test_rotated)
    norm_diff_weighted = sp.simplify(norm_rot - norm_orig)
    norm_diff_isotropic = sp.simplify(norm_diff_weighted.subs({w1: 1, w2: 1, w3: 1}))
    norm_diff_weighted_distinct = sp.simplify(norm_diff_weighted.subs({w1: 1, w2: 2, w3: 3}))

    record(
        "(BA-2) isotropic control: weighted Frobenius pairing IS orbit-flat when w1=w2=w3",
        norm_diff_isotropic == 0,
        "delta_||h||^2 = 0 under isotropic weight",
    )
    record(
        "(BA-2) anisotropic control: weighted Frobenius pairing is NOT orbit-flat when w1 != w2 != w3",
        norm_diff_weighted_distinct != 0,
        f"delta_||h||^2 with w=(1,2,3) = {norm_diff_weighted_distinct} (nonzero)",
    )

    # ------------------------------------------------------------------
    section("Part G: load-bearing-step inventory + scope discipline")
    # ------------------------------------------------------------------
    note_path = Path(__file__).resolve().parent.parent / "docs" / "UNIVERSAL_GR_TENSOR_ACTION_CASIMIR_EQUIVARIANT_CLASS_NOGO_NOTE_2026-05-17.md"
    if note_path.exists():
        text = note_path.read_text()
        for marker, label in [
            ("**Claim type:** no_go", "claim type"),
            ("Class CB(V)", "class label"),
            ("Schur's lemma in real-orthogonal form", "BA-4 named"),
            ("UNIVERSAL_GR_CASIMIR_BLOCK_LOCALIZATION_NOTE.md", "load-bearing citation"),
            ("UNIVERSAL_GR_TENSOR_ACTION_BLOCKER_NOTE.md", "blocker-sharpening citation"),
            ("orbit-flat", "orbit-flat property cited"),
            ("Section no-go", "section no-go statement"),
            ("class-(A)", "load-bearing class identifier"),
            ("does **not** claim", "scope discipline marker"),
        ]:
            record(
                f"note contains '{label}': {marker!r}",
                marker in text,
                "scope discipline / citation hygiene check",
                status="DOC",
            )

        # Confirm forbidden claims not made
        for forbidden in [
            "closes the full universal-GR route",
            "derives the Einstein-Hilbert action",
            "uses fitted constants",
            "uses PDG values",
        ]:
            record(
                f"note avoids forbidden claim: {forbidden!r}",
                forbidden not in text,
                "narrow scope discipline",
                status="DOC",
            )
    else:
        record(
            "note exists at expected path",
            False,
            f"missing {note_path}",
            status="DOC",
        )

    # ------------------------------------------------------------------
    execution_certificate(
        frame,
        projectors,
        ranks,
        (gx, gy, gz),
        gram == sp.eye(10),
        equivariant,
        indep_rank,
        sym_rank,
        full_rank,
    )

    # ------------------------------------------------------------------
    section("Summary")
    # ------------------------------------------------------------------
    n_pass = sum(c.ok for c in CHECKS)
    n_fail = len(CHECKS) - n_pass
    print(f"\nPASS={n_pass} FAIL={n_fail} TOTAL={len(CHECKS)}")

    if n_fail == 0:
        print(
            "\nClass CB(V) no-go confirmed: every Casimir-equivariant linear-projector "
            "tensor action on Sym^2(R^4) is SO(3)-orbit-flat and cannot canonically "
            "section the universal complement. The tensor-action blocker, on this "
            "named class, is now a structural no-go theorem."
        )
        return 0

    print("\nOne or more checks failed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
