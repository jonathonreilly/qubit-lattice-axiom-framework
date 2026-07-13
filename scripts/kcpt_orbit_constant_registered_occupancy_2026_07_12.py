#!/usr/bin/env python3
"""Exact certificate for the K/CPT orbit-constant registered-occupancy note."""

from pathlib import Path
import sympy as sp

ROOT = Path(__file__).resolve().parents[1]
PASS = 0
FAIL = 0
FAILURES = []


def check(block, name, condition, detail=""):
    """Print one exact, computed PASS/FAIL result."""
    global PASS, FAIL
    ok = bool(condition)
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        FAILURES.append(f"{block}:{name}")
        status = "FAIL"
    suffix = f" :: {detail}" if detail else ""
    print(f"{block} {status} {name}{suffix}")
    return ok


def matrix_zero(matrix):
    return matrix.applyfunc(sp.simplify) == sp.zeros(*matrix.shape)


def scalar_zero(value):
    return sp.simplify(value) == 0


def flattened(path):
    return " ".join(path.read_text(encoding="utf-8").split())


# Shared exact algebra; no floating-point values occur.
I = sp.I
sqrt3 = sp.sqrt(3)
w = -sp.Rational(1, 2) + sqrt3 * I / 2
wb = sp.conjugate(w)
I2, I3 = sp.eye(2), sp.eye(3)
s1 = sp.Matrix([[0, 1], [1, 0]])
s2 = sp.Matrix([[0, -I], [I, 0]])
s3 = sp.diag(1, -1)
C = sp.Matrix([[0, 1, 0], [0, 0, 1], [1, 0, 0]])
C2 = C**2


def P(chi):
    return sp.simplify((I3 + sp.conjugate(chi) * C
                        + sp.conjugate(chi)**2 * C2) / 3)


P1, Pw, Pwb = P(sp.Integer(1)), P(w), P(wb)


# V1 -- current memo clauses, verbatim after whitespace flattening.
minimal_path = ROOT / "docs/MINIMAL_AXIOMS_2026-06-29.md"
minimal_flat = flattened(minimal_path)
v1_needles = {
    "qubit_real_presentation": (
        "A `Cl(3,0)`-compatible real-algebra presentation may be used "
        "equivalently and adds no further primitive structure."
    ),
    "no_possibility_privileged": "No possibility is privileged.",
    "qualification_choice": (
        "A choice not fixed by the supplied structure remains a named "
        "conditional or open dependency."
    ),
    "state_configuration_of_records": "A state is a configuration of records.",
    "law_no_state_privilege": (
        "A law privileges no states. Its domain is a supplied condition, and "
        "at every state where the condition holds it gives exactly one answer."
    ),
    "record_additivity": (
        "For any finite collection of pairwise-disjoint records, scalar "
        "readout `I` is additive, with `I(empty)=0`."
    ),
}
for name, needle in v1_needles.items():
    check("V1", name, " ".join(needle.split()) in minimal_flat)


# V2 -- L-K1 joint real-algebra structure and positive-list K closure.
qubit_basis = [("I2", I2), ("s1", s1), ("s2", s2), ("s3", s3)]
corner_basis = [("I3", I3), ("C", C), ("C2", C2)]
G = [(f"{qn}x{cn}", sp.kronecker_product(qm, cm))
     for qn, qm in qubit_basis for cn, cm in corner_basis]
pair_products = [A * B for _, A in G for _, B in G]
check(
    "V2", "joint_conjugation_multiplicative_all_G_pairs",
    all(matrix_zero(sp.conjugate(A * B) - sp.conjugate(A) * sp.conjugate(B))
        for _, A in G for _, B in G),
    detail=f"generators={len(G)} pair_products={len(pair_products)}",
)
real_coeffs = sp.symbols(f"a0:{len(G)}", real=True)
general_real_span = sum((a * A for a, (_, A) in zip(real_coeffs, G)), sp.zeros(6, 6))
check(
    "V2", "joint_conjugation_real_linear_on_G_span",
    matrix_zero(sp.conjugate(general_real_span)
                - sum((a * sp.conjugate(A) for a, (_, A) in zip(real_coeffs, G)),
                      sp.zeros(6, 6))),
)
qubit_k_image = {
    "I2": (sp.Integer(1), I2), "s1": (sp.Integer(1), s1),
    "s2": (-sp.Integer(1), s2), "s3": (sp.Integer(1), s3),
}
explicit_k_closure = []
for qn, qm in qubit_basis:
    for cn, cm in corner_basis:
        coefficient, qimage = qubit_k_image[qn]
        reexpressed = coefficient * sp.kronecker_product(qimage, cm)
        explicit_k_closure.append(matrix_zero(
            sp.conjugate(sp.kronecker_product(qm, cm)) - reexpressed
        ))
check(
    "V2", "K_closure_explicit_reexpression_each_G_generator",
    all(explicit_k_closure),
    detail="conj(s2 x C^j)=-s2 x C^j; all other listed tensors fixed",
)
check("V2", "conj_Pw_equals_Pwb", matrix_zero(sp.conjugate(Pw) - Pwb))
check("V2", "conj_fixes_C", matrix_zero(sp.conjugate(C) - C))
check("V2", "conj_fixes_P1", matrix_zero(sp.conjugate(P1) - P1))
check("V2", "conj_fixes_C_plus_C2",
      matrix_zero(sp.conjugate(C + C2) - (C + C2)))


# V3 -- the positive joint doublet-resolving witness.
Aodd = I * (C - C2)
Beven = C + C2
W = sp.kronecker_product(s2, Aodd)
U_C = sp.kronecker_product(I2, C)
check("V3", "W_Hermitian", matrix_zero(W - W.conjugate().T))
check("V3", "W_C3_invariant", matrix_zero(U_C * W * U_C.conjugate().T - W))
check("V3", "W_jointly_K_even", matrix_zero(sp.conjugate(W) - W))
check("V3", "W_in_positive_list_generated_real_algebra",
      matrix_zero(W - sp.kronecker_product(s1 * s2 * s3 * s2, C - C2)))
rho_q_plus_s2 = (I2 + s2) / 2
t_w = sp.simplify(sp.trace(W * sp.kronecker_product(rho_q_plus_s2, Pw)))
t_wb = sp.simplify(sp.trace(W * sp.kronecker_product(rho_q_plus_s2, Pwb)))
check(
    "V3", "W_resolves_doublet_with_s2_polarization",
    scalar_zero(t_w + sqrt3) and scalar_zero(t_wb - sqrt3)
    and not scalar_zero(t_w - t_wb),
    detail=f"Tr(W rho_qxPw)={t_w}; Tr(W rho_qxPwb)={t_wb}",
)
check("V3", "corner_iCminusC2_K_odd", matrix_zero(sp.conjugate(Aodd) + Aodd))
check("V3", "corner_iCminusC2_Hermitian", matrix_zero(Aodd - Aodd.conjugate().T))
check("V3", "corner_iCminusC2_eigenvalues",
      Aodd.eigenvals() == {-sqrt3: 1, sp.Integer(0): 1, sqrt3: 1},
      detail=str(Aodd.eigenvals()))
check("V3", "corner_CplusC2_K_even", matrix_zero(sp.conjugate(Beven) - Beven))
check("V3", "corner_CplusC2_eigenvalues",
      Beven.eigenvals() == {sp.Integer(2): 1, -sp.Integer(1): 2},
      detail=str(Beven.eigenvals()))


# V4 -- K covariance of real-pointer controlled-copy isometries (W1a form).
def ket(k, n):
    vector = sp.zeros(n, 1)
    vector[k, 0] = 1
    return vector


def copy_isometry(pvm):
    n = len(pvm)
    return sum((sp.kronecker_product(projector, ket(k, n))
                for k, projector in enumerate(pvm)),
               sp.zeros(pvm[0].rows * n, pvm[0].cols))


sector_pvm = [P1, Pw, Pwb]
sector_pvm_K = [sp.conjugate(projector) for projector in sector_pvm]
V3copy, V3copy_K = copy_isometry(sector_pvm), copy_isometry(sector_pvm_K)
check("V4", "sector_copy_isometry", matrix_zero(V3copy.conjugate().T * V3copy - I3))
check("V4", "sector_copy_conj_is_conjugated_PVM_copy",
      matrix_zero(sp.conjugate(V3copy) - V3copy_K))
check("V4", "sector_conjugation_swaps_doublet_projectors",
      matrix_zero(sector_pvm_K[1] - Pwb) and matrix_zero(sector_pvm_K[2] - Pw))
z = sp.symbols("z0:9")
rho3_generic = sp.Matrix(3, 3, z)
check(
    "V4", "sector_channel_intertwines_K",
    matrix_zero(sp.conjugate(V3copy * rho3_generic * V3copy.conjugate().T)
                - V3copy_K * sp.conjugate(rho3_generic) * V3copy_K.conjugate().T),
)
doublet = sp.simplify(Pw + Pwb)
two_block_pvm = [P1, doublet]
two_block_pvm_K = [sp.conjugate(projector) for projector in two_block_pvm]
V2copy, V2copy_K = copy_isometry(two_block_pvm), copy_isometry(two_block_pvm_K)
check("V4", "CplusC2_spectral_copy_isometry",
      matrix_zero(V2copy.conjugate().T * V2copy - I3))
check("V4", "CplusC2_spectral_PVM_K_fixed",
      all(matrix_zero(a - b) for a, b in zip(two_block_pvm_K, two_block_pvm)))
check("V4", "CplusC2_spectral_copy_K_fixed", matrix_zero(sp.conjugate(V2copy) - V2copy))
check(
    "V4", "CplusC2_spectral_channel_intertwines_K",
    matrix_zero(sp.conjugate(V2copy * rho3_generic * V2copy.conjugate().T)
                - V2copy_K * sp.conjugate(rho3_generic) * V2copy_K.conjugate().T),
)


# V5 -- L-K2 state face and orbit-constant joint-witness protocol.
real_rho_symbols = {(row, col): sp.Symbol(f"r{row}{col}", real=True)
                    for row in range(6) for col in range(row, 6)}
rho_real = sp.Matrix(6, 6, lambda row, col:
                     real_rho_symbols[(min(row, col), max(row, col))])
check("V5", "symbolic_input_K_real", matrix_zero(sp.conjugate(rho_real) - rho_real))
check("V5", "symbolic_input_Hermitian", matrix_zero(rho_real - rho_real.conjugate().T))
V3copy_joint = sum((sp.kronecker_product(I2, projector, ket(k, 3))
                    for k, projector in enumerate(sector_pvm)), sp.zeros(18, 6))
registered = sp.simplify(V3copy_joint * rho_real * V3copy_joint.conjugate().T)
pointer_projectors_3 = [sp.kronecker_product(sp.eye(6), ket(k, 3) * ket(k, 3).T)
                        for k in range(3)]
registered_weights = [sp.simplify(sp.trace(pointer_projectors_3[k] * registered))
                      for k in range(3)]
check(
    "V5", "K_real_sector_registered_weights_orbit_constant",
    scalar_zero(registered_weights[1] - registered_weights[2]),
    detail=f"w-Pw_minus_w-Pwb={sp.simplify(registered_weights[1]-registered_weights[2])}",
)
I6 = sp.eye(6)
Q0 = sp.simplify(I6 - W**2 / 3)
Qplus = sp.simplify((W**2 + sqrt3 * W) / 6)
Qminus = sp.simplify((W**2 - sqrt3 * W) / 6)
W_pvm = [("0", Q0), ("+sqrt3", Qplus), ("-sqrt3", Qminus)]
check("V5", "W_spectral_PVM_complete", matrix_zero(Q0 + Qplus + Qminus - I6))
check("V5", "W_spectral_PVM_projective",
      all(matrix_zero(Q * Q - Q) for _, Q in W_pvm)
      and all(matrix_zero(Qa * Qb) for ia, (_, Qa) in enumerate(W_pvm)
              for ib, (_, Qb) in enumerate(W_pvm) if ia != ib))
check("V5", "W_spectral_PVM_K_even",
      all(matrix_zero(sp.conjugate(Q) - Q) for _, Q in W_pvm))
Rsector = [sp.kronecker_product(I2, projector) for projector in sector_pvm]
branch_weights, branch_differences = {}, []
for branch_name, Q in W_pvm:
    for sector_index, R in enumerate(Rsector):
        branch_weights[(branch_name, sector_index)] = sp.simplify(sp.trace(R * Q * rho_real * Q))
    difference = sp.simplify(branch_weights[(branch_name, 1)]
                             - branch_weights[(branch_name, 2)])
    branch_differences.append(difference)
    check("V5", f"W_branch_{branch_name}_sector_orbit_constant", scalar_zero(difference),
          detail=f"difference={difference}")
check("V5", "W_protocol_symmetric_ensemble",
      scalar_zero(sum(branch_differences, sp.Integer(0))),
      detail=f"summed_difference={sp.simplify(sum(branch_differences, sp.Integer(0)))}")


# V6 -- computed negative controls and dynamic authority checks.
eps = sp.Symbol("eps", real=True)
rho_eps = sp.kronecker_product((I2 + eps * s2) / 2, I3 / 3)
rho_minus_eps = sp.kronecker_product((I2 - eps * s2) / 2, I3 / 3)
check("V6", "K_odd_seed_conjugated_model_pair",
      matrix_zero(sp.conjugate(rho_eps) - rho_minus_eps)
      and scalar_zero(sp.trace(rho_eps) - sp.trace(rho_minus_eps)))
neg_branch_plus = [sp.simplify(sp.trace(Rsector[k] * Qplus * rho_eps * Qplus))
                   for k in range(3)]
neg_plus_difference = sp.factor(neg_branch_plus[1] - neg_branch_plus[2])
neg_plus_total = sp.simplify(sum(neg_branch_plus, sp.Integer(0)))
neg_plus_conditional_difference = sp.factor(neg_plus_difference / neg_plus_total)
neg_branch_minus = [sp.simplify(sp.trace(Rsector[k] * Qminus * rho_eps * Qminus))
                    for k in range(3)]
neg_minus_difference = sp.factor(neg_branch_minus[1] - neg_branch_minus[2])
neg_minus_total = sp.simplify(sum(neg_branch_minus, sp.Integer(0)))
neg_minus_conditional_difference = sp.factor(neg_minus_difference / neg_minus_total)
check("V6", "K_odd_seed_plus_branch_difference_exact",
      scalar_zero(neg_plus_difference + eps / 3),
      detail=f"joint_difference={neg_plus_difference}; normalized_within_branch={neg_plus_conditional_difference}")
check("V6", "K_odd_seed_nonzero_for_eps_nonzero",
      sp.solve(sp.Eq(neg_plus_difference, 0), eps) == [sp.Integer(0)])
check("V6", "K_odd_seed_zero_at_eps_zero", scalar_zero(neg_plus_difference.subs(eps, 0)))
check("V6", "K_odd_seed_minus_branch_difference_exact",
      scalar_zero(neg_minus_difference - eps / 3),
      detail=f"joint_difference={neg_minus_difference}; normalized_within_branch={neg_minus_conditional_difference}")
check("V6", "K_odd_seed_unconditioned_doublet_difference_cancels",
      scalar_zero(neg_plus_difference + neg_minus_difference),
      detail="the two resolved W branches carry opposite asymmetries")
sector_pvm_valid = (
    matrix_zero(sum(sector_pvm, sp.zeros(3, 3)) - I3)
    and all(matrix_zero(Pk * Pk - Pk) for Pk in sector_pvm)
    and all(matrix_zero(Pa * Pb) for ia, Pa in enumerate(sector_pvm)
            for ib, Pb in enumerate(sector_pvm) if ia != ib)
)
check("V6", "full_3sector_registration_PVM_and_copy_isometry",
      sector_pvm_valid and matrix_zero(V3copy.conjugate().T * V3copy - I3))


def pointer_distribution_for_sector(projector):
    output = sp.simplify(V3copy * projector * V3copy.conjugate().T)
    pointer_ops = [sp.kronecker_product(I3, ket(k, 3) * ket(k, 3).T)
                   for k in range(3)]
    return [sp.simplify(sp.trace(pointer_ops[k] * output)) for k in range(3)]


dist_w = pointer_distribution_for_sector(Pw)
dist_wb = pointer_distribution_for_sector(Pwb)
check("V6", "full_registration_branchwise_resolves_doublet",
      dist_w == [sp.Integer(0), sp.Integer(1), sp.Integer(0)]
      and dist_wb == [sp.Integer(0), sp.Integer(0), sp.Integer(1)],
      detail=f"Pw->{dist_w}; Pwb->{dist_wb}")
check("V6", "K_real_full_registration_ensemble_orbit_constant",
      scalar_zero(registered_weights[1] - registered_weights[2]))
check("V6", "K_odd_monitor_spectral_PVM_matches_3sectors",
      matrix_zero(Aodd * P1)
      and matrix_zero((Aodd + sqrt3 * I3) * Pw)
      and matrix_zero((Aodd - sqrt3 * I3) * Pwb))
check("V6", "three_sector_monitor_in_positive_list_real_algebra",
      matrix_zero(sp.kronecker_product(sp.eye(2), Aodd)
                  - sp.kronecker_product(s1 * s2 * s3, C - C2)),
      detail="I2 x i(C-C^2) = (s1 s2 s3) x (C-C^2): a real product of "
             "positive-list generators; the 3-sector monitor needs no admission")

record_note_path = ROOT / "docs/RECORD_WRITE_ADMISSIBLE_ONE_STEP_CLASS_CONTROLLED_COPY_NARROW_THEOREM_NOTE_2026-07-11.md"
record_flat = flattened(record_note_path)
record_class_needle = (
    "Thus every admissible blank-input one-step write under these declared readings "
    "is, up to a register basis unitary and register phase choice, in the "
    "controlled-copy isometry class."
)
check("V6", "admissibility_authority_note_available",
      " ".join(record_class_needle.split()) in record_flat,
      detail="dynamic flattened-whitespace controlled-copy class quotation")
flavor_path = ROOT / "docs/FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02.md"
flavor_flat = flattened(flavor_path)
born_exact = (
    "The genuine **Born/tracial max-entropy** state `ρ=I/3` weights the blocks by "
    "**dimension** (`Tr P₀:Tr P₁ = 1:2`) → **r=1 → Q=1**."
)
check("V6", "flavor_note_Born_comparator_verbatim",
      " ".join(born_exact.split()) in flavor_flat)
w1b_path = ROOT / "docs/ACPHILAMBDA_OCCUPANCY_GRAIN_RULE_CLASS_UNIVERSALITY_BOUNDED_THEOREM_NOTE_2026-07-11.md"
w1b_flat = flattened(w1b_path)
grain_needle = "p_d=1/2 <=> 2r/(1+2r)=1/2 <=> 4r=1+2r <=> r=1/2."
check("V6", "W1b_grain_formula_authority_available",
      " ".join(grain_needle.split()) in w1b_flat,
      detail="dynamic flattened-whitespace p_d-to-r derivation")
r = sp.symbols("r", real=True)
born_r_solutions = sp.solve(sp.Eq(sp.Rational(2, 3), 2 * r / (1 + 2 * r)), r)
check("V6", "Born_2block_weights_imply_r_one_exact",
      born_r_solutions == [sp.Integer(1)], detail=f"solutions={born_r_solutions}")


# V7 -- exact W1b L2 family, embedded only on the swap-symmetric 3-label face.
l2_needle = (
    "T_f(q) = f(q) / (f(q)+f(1-q)), f : [0,1] -> [0,1], f continuous "
    "and strictly increasing, f(0)=0."
)
check("V7", "W1b_L2_update_family_source_available",
      " ".join(l2_needle.split()) in w1b_flat,
      detail="dynamic flattened-whitespace L2 family definition")
koide_path = ROOT / "docs/KOIDE_CONVENTION_INVARIANT_SCALAR_SELECTOR_DOUBLET_CONSTANCY_NARROW_THEOREM_NOTE_2026-07-12.md"
koide_flat = flattened(koide_path)
koide_needle = (
    "Thus the unlabeled three-block partition is convention-stable and resolves "
    "all three sectors without privileging either doublet member."
)
check("V7", "Koide_doublet_constancy_note_available",
      " ".join(koide_needle.split()) in koide_flat,
      detail="dynamic observable-face boundary quotation")
q = sp.symbols("q", real=True)
fq, f1q = sp.symbols("f_q f_1_minus_q", positive=True)
Tf = sp.factor(fq / (fq + f1q))
input_orbit = sp.Matrix([1 - q, q])
input_three = sp.Matrix([1 - q, q / 2, q / 2])
output_orbit = sp.Matrix([1 - Tf, Tf])
output_three = sp.Matrix([1 - Tf, Tf / 2, Tf / 2])
aggregate = sp.Matrix([[1, 0, 0], [0, 1, 1]])
split = sp.Matrix([[1, 0], [0, sp.Rational(1, 2)], [0, sp.Rational(1, 2)]])
swap = sp.Matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]])
family_restriction = (
    matrix_zero(aggregate * input_three - input_orbit)
    and matrix_zero(split * input_orbit - input_three)
    and matrix_zero(aggregate * output_three - output_orbit)
    and matrix_zero(split * output_orbit - output_three)
)
surface_invariant = matrix_zero(swap * output_three - output_three)
exchange_identity = scalar_zero(
    (f1q / (f1q + fq)) - (1 - Tf)
)
fixed_equivalence = scalar_zero(
    sp.together((Tf - q) - (fq * (1 - q) - q * f1q) / (fq + f1q))
)
power_fixed_sets = {}
for exponent in (sp.Integer(2), sp.Integer(3), sp.Rational(5, 2), sp.Integer(4)):
    x = sp.symbols("x", nonnegative=True)
    if exponent.q == 1:
        polynomial = sp.factor(x**exponent * (1 - x) - x * (1 - x)**exponent)
        solutions = {root for root in sp.solve(sp.Eq(polynomial, 0), x)
                     if root.is_real and 0 <= root <= 1}
    else:
        y = sp.symbols("y", nonnegative=True)
        squared_equation = sp.factor(x**5 * (1 - x)**2 - x**2 * (1 - x)**5)
        candidates = sp.solve(sp.Eq(squared_equation, 0), x)
        solutions = {root for root in candidates
                     if root.is_real and 0 <= root <= 1
                     and scalar_zero((root**exponent * (1 - root)
                                      - root * (1 - root)**exponent))}
    power_fixed_sets[str(exponent)] = solutions
expected_fix = {sp.Integer(0), sp.Rational(1, 2), sp.Integer(1)}
fixed_reproduced = all(solutions == expected_fix for solutions in power_fixed_sets.values())
check("V7", "W1b_common_f_exchange_identity", exchange_identity)
check("V7", "W1b_fixed_equation_reproved", fixed_equivalence,
      detail="T_f(q)=q iff f(q)(1-q)=q f(1-q); strict sharpening excludes off-center roots")
check("V7", "W1b_power_subfamily_Fix_0_half_1_exact", fixed_reproduced,
      detail=str(power_fixed_sets))
check("V7", "swap_symmetric_surface_invariance_and_Fix_0_half_1",
      family_restriction and surface_invariant and exchange_identity
      and fixed_equivalence and fixed_reproduced,
      detail="3-label face is the exact split of W1b's (p_s,p_d) family")


print("PATH note=docs/KCPT_ORBIT_CONSTANT_REGISTERED_OCCUPANCY_WEIGHTS_DERIVABLE_PROTOCOL_CLASS_BOUNDED_THEOREM_NOTE_2026-07-12.md")
print("PATH runner=scripts/kcpt_orbit_constant_registered_occupancy_2026_07_12.py")
print("PATH cache=logs/runner-cache/kcpt_orbit_constant_registered_occupancy_2026_07_12.txt")
print("PATH worklog=/tmp/kreality_p3_worklog.md")
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("FLAGS: none" if not FAILURES else "FLAGS: " + ", ".join(FAILURES))
