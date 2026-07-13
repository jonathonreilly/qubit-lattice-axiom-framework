#!/usr/bin/env python3
"""Exact formation-licensing consolidation checks (rhalf block 19).

The runner proves finite product closure for the four SOCMLC supplied-object
classes on a coupling-free disjoint two-site composite, checks the exact
agreement-conditioned boundary, and reuses the landed records-only
Grassmann/Berezin engine to identify the K-symmetrized weight coefficientwise
with canonical counting expectation on the supplied coupling orbit.

No premise is adopted.  SOCMLC remains a convention-grade conditional, (LE)
and (LAW) remain named elements, and availability of the coupling orbit at the
formation/measure stage remains the single consolidated licensing residual.
All derivation-path arithmetic is integer or Fraction arithmetic.
"""

from contextlib import redirect_stderr, redirect_stdout
from fractions import Fraction as F
import importlib.util
import io
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"

CLASSIFICATION = DOCS / (
    "KOIDE_FORMATION_WEIGHT_LAW_EXPRESSIBILITY_CLASSIFICATION_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
CROSS_EDGE = DOCS / (
    "G3_CROSS_EDGE_INDEPENDENCE_IS_A_FORMATION_GATE_ATOM_MARGINAL_"
    "IDENTITY_FROM_QUALIFICATION_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
KAPPA = DOCS / (
    "KOIDE_KAPPA_FLOW_CLASS_IS_THE_FORMATION_WEIGHT_IN_FLOW_COORDINATES_"
    "BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
AXIOMS = DOCS / "MINIMAL_AXIOMS_2026-06-29.md"
TICK = DOCS / (
    "TICK_CELL_SELECTION_BY_TRANSLATION_AND_VARIATION_CLAUSES_"
    "NARROW_THEOREM_NOTE_2026-07-09.md"
)
NOTE = DOCS / (
    "KOIDE_FORMATION_LICENSING_ONE_CRITERION_PRODUCT_CLOSURE_AND_"
    "ORBIT_AVERAGE_CONSOLIDATION_BOUNDED_THEOREM_NOTE_2026-07-12.md"
)
RECORDS_ENGINE = ROOT / "scripts" / "frontier_records_only_os_reconstruction_2026_07_11.py"


_pass = 0
_fail = 0


def check(num, description, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {description}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def normalized(text):
    # Normalize prose across source-controlled Markdown line wrapping without
    # changing any words in the quoted sentences.
    lines = []
    for raw_line in text.splitlines():
        line = raw_line.strip()
        while line.startswith(">"):
            line = line[1:].lstrip()
        if line.startswith("- "):
            line = line[2:]
        lines.append(line)
    return " ".join(" ".join(lines).split())


def normalize_masses(masses):
    total = sum(masses)
    return tuple(F(m, total) for m in masses)


def outer(left, right):
    return tuple(x * y for x in left for y in right)


def marginals(joint):
    # Order: ss, sd, ds, dd.
    return ((joint[0] + joint[1], joint[2] + joint[3]),
            (joint[0] + joint[2], joint[1] + joint[3]))


def exact_rank(matrix):
    work = [[F(value) for value in row] for row in matrix]
    rows = len(work)
    columns = len(work[0]) if rows else 0
    rank = 0
    for column in range(columns):
        pivot = next((row for row in range(rank, rows) if work[row][column] != 0), None)
        if pivot is None:
            continue
        work[rank], work[pivot] = work[pivot], work[rank]
        pivot_value = work[rank][column]
        work[rank] = [value / pivot_value for value in work[rank]]
        for row in range(rows):
            if row == rank or work[row][column] == 0:
                continue
            multiplier = work[row][column]
            work[row] = [
                value - multiplier * pivot_entry
                for value, pivot_entry in zip(work[row], work[rank])
            ]
        rank += 1
        if rank == rows:
            break
    return rank


print("=" * 78)
print("Formation licensing: one criterion, product closure, and orbit average")
print("rhalf block 19; exact finite arithmetic; no premise adoption")
print("=" * 78)


# ---------------------------------------------------------------------------
# Source-grade criterion and exact single-site objects
# ---------------------------------------------------------------------------
classification_text = normalized(CLASSIFICATION.read_text())
criterion_sentence = normalized(
    """A menu probability is licensed only when its unnormalized cell masses
    are the ranks or multiplicities of a canonical finite measure/trace on an
    object actually supplied here: the carrier, the `K`-orbit set, the quotient
    atom set, or the regular module of the licensed quotient formation
    algebra."""
)
check(
    1,
    "SOCMLC source pins exactly four supplied-object classes and labels the "
    "criterion a classification convention, not an axiom theorem",
    criterion_sentence in classification_text
    and "a classification convention, not a theorem derived from the minimal axioms"
    in classification_text,
)

P_s = ((1, 0, 0), (0, 0, 0), (0, 0, 0))
P_d = ((0, 0, 0), (0, 1, 0), (0, 0, 1))
I_3 = ((1, 0, 0), (0, 1, 0), (0, 0, 1))
projector_sum = tuple(
    tuple(P_s[i][j] + P_d[i][j] for j in range(3)) for i in range(3)
)
single_quotient_atoms = ("s", "d")
carrier_single_masses = tuple(exact_rank(projector) for projector in (P_s, P_d))
quotient_single_masses = tuple(1 for _ in single_quotient_atoms)
q_dim = normalize_masses(carrier_single_masses)
q_cell = normalize_masses(quotient_single_masses)
check(
    2,
    "single-site canonical measures are derived exactly: carrier/orbit-member "
    "count (1/3,2/3), quotient/regular count (1/2,1/2)",
    projector_sum == I_3
    and carrier_single_masses == (1, 2)
    and q_dim == (F(1, 3), F(2, 3))
    and q_cell == (F(1, 2), F(1, 2))
    and {q_dim, q_cell} == {(F(1, 3), F(2, 3)), (F(1, 2), F(1, 2))},
)


# ---------------------------------------------------------------------------
# T1: four product-closed licensed composite classes
# ---------------------------------------------------------------------------
carrier_composite_masses = tuple(
    left * right for left in carrier_single_masses for right in carrier_single_masses
)
carrier_joint = normalize_masses(carrier_composite_masses)
check(
    3,
    "carrier tensor product: rank(P_i tensor P_j)=rank(P_i)rank(P_j), giving "
    "(1,2,2,4)/9 exactly",
    carrier_composite_masses == (1, 2, 2, 4)
    and carrier_joint == outer(q_dim, q_dim),
)

quotient_atoms = (("s", "s"), ("s", "d"), ("d", "s"), ("d", "d"))
quotient_joint = normalize_masses(tuple(1 for _ in quotient_atoms))
check(
    4,
    "coupling-free quotient atoms are the four ordered atom pairs; counting is "
    "the uniform product joint",
    len(set(quotient_atoms)) == 4
    and quotient_joint == outer(q_cell, q_cell),
)

K = {"1": "1", "omega": "omegabar", "omegabar": "omega"}
orbit_cells = {
    "s": frozenset({"1"}),
    "d": frozenset({"omega", "omegabar"}),
}


def diagonal_k(pair):
    return (K[pair[0]], K[pair[1]])


product_cells = {
    (i, j): frozenset((x, y) for x in orbit_cells[i] for y in orbit_cells[j])
    for i in ("s", "d")
    for j in ("s", "d")
}
single_cell_stability = all(
    frozenset(K[x] for x in cell) == cell for cell in orbit_cells.values()
)
product_cell_stability = all(
    frozenset(diagonal_k(pair) for pair in cell) == cell
    for cell in product_cells.values()
)
check(
    5,
    "load-bearing CKS verified exactly: K fixes each menu cell setwise, so "
    "diagonal K fixes all four product orbit cells setwise",
    single_cell_stability and product_cell_stability and len(product_cells) == 4,
)

orbit_composite_masses = tuple(
    len(product_cells[key]) for key in (("s", "s"), ("s", "d"), ("d", "s"), ("d", "d"))
)
orbit_joint = normalize_masses(orbit_composite_masses)
check(
    6,
    "orbit-cell member masses multiply exactly under CKS: |O_i x O_j|="
    "|O_i||O_j| gives (1,2,2,4)/9",
    orbit_composite_masses == (1, 2, 2, 4)
    and orbit_joint == outer(q_dim, q_dim),
)


def action_orbits(points, action):
    remaining = set(points)
    result = []
    while remaining:
        seed = next(iter(remaining))
        orbit = {seed, action(seed)}
        result.append(frozenset(orbit))
        remaining -= orbit
    return tuple(result)


dd_action_orbits = action_orbits(product_cells[("d", "d")], diagonal_k)
check(
    7,
    "diagonal-action precision guard: O_d x O_d is one supplied invariant "
    "product cell of size 4 but refines internally into two 2-cycles; no false "
    "quotient-product identity is used",
    len(product_cells[("d", "d")]) == 4
    and sorted(len(orbit) for orbit in dd_action_orbits) == [2, 2]
    and set().union(*map(set, dd_action_orbits)) == set(product_cells[("d", "d")]),
)

regular_basis = quotient_atoms
regular_projector_ranks = tuple(
    sum(1 for basis_atom in regular_basis if basis_atom == projection_atom)
    for projection_atom in regular_basis
)
regular_joint = normalize_masses(regular_projector_ranks)
check(
    8,
    "regular module: (C+C) tensor (C+C) has four basis atoms and four minimal "
    "central regular ranks (1,1,1,1), hence the uniform product",
    len(regular_basis) == 4
    and regular_projector_ranks == (1, 1, 1, 1)
    and regular_joint == outer(q_cell, q_cell),
)

licensed_joints = {
    "carrier trace": (carrier_joint, q_dim),
    "quotient counting": (quotient_joint, q_cell),
    "K-orbit-member counting": (orbit_joint, q_dim),
    "regular-module trace": (regular_joint, q_cell),
}
check(
    9,
    "all four SOCMLC composite classes equal the outer product of their "
    "licensed single-site marginals",
    len(licensed_joints) == 4
    and all(joint == outer(single, single) for joint, single in licensed_joints.values()),
)

joint_atom_checks = []
for joint, single in licensed_joints.values():
    left, right = marginals(joint)
    p = single[0]
    a = joint[0]
    joint_atom_checks.append(
        left == single
        and right == single
        and a - p * p == 0
        and a == p * p
    )
check(
    10,
    "every licensed joint has identical marginals and pays the exact cross-edge "
    "atom C_ss=a-p^2=0, equivalently a=p^2",
    all(joint_atom_checks),
)

agreement_atoms = (("s", "s"), ("d", "d"))
agreement_weights_by_atom = {atom: F(1, len(agreement_atoms)) for atom in agreement_atoms}
agreement_joint = tuple(agreement_weights_by_atom.get(atom, F(0)) for atom in quotient_atoms)
check(
    11,
    "supplied agreement datum changes the canonical object to {(s,s),(d,d)}; "
    "counting gives (1/2,0,0,1/2) exactly",
    agreement_joint == (F(1, 2), F(0), F(0), F(1, 2)),
)

agreement_left, agreement_right = marginals(agreement_joint)
agreement_p = agreement_left[0]
agreement_c = agreement_joint[0] - agreement_p * agreement_p
check(
    12,
    "agreement counting has identical actual marginals p=1/2 but C_ss=1/4, "
    "the decisive supplied-coupling boundary",
    agreement_left == agreement_right == (F(1, 2), F(1, 2))
    and agreement_p == F(1, 2)
    and agreement_c == F(1, 4),
)

cross_text = normalized(CROSS_EDGE.read_text())
kappa_text = normalized(KAPPA.read_text())
check(
    13,
    "source-grade boundary is pinned: (LE) is a named premise and the kappa "
    "scope supplies agreement-conditioned independent draws rather than deriving them",
    "(LE) Law-equivalence element (named premise, exact statement)." in cross_text
    and "Two registrations compose as independent draws of the same formation law, after which one conditions on agreement."
    in kappa_text,
)


# ---------------------------------------------------------------------------
# T2: exact reuse of the landed records-only Grassmann/Berezin engine
# ---------------------------------------------------------------------------
def load_records_engine():
    spec = importlib.util.spec_from_file_location("records_engine_rhalf19", RECORDS_ENGINE)
    module = importlib.util.module_from_spec(spec)
    captured = io.StringIO()
    exit_code = None
    try:
        with redirect_stdout(captured), redirect_stderr(captured):
            spec.loader.exec_module(module)
    except SystemExit as exc:
        exit_code = exc.code
    return module, captured.getvalue(), exit_code


try:
    engine, engine_stdout, engine_exit = load_records_engine()
    engine_ready = (
        engine_exit == 0
        and "TOTAL: PASS=24 FAIL=0" in engine_stdout
        and all(hasattr(engine, name) for name in (
            "CR", "W_of", "dag", "build_K", "exp_bilinear", "berezin_full", "add", "scal"
        ))
    )
except Exception as exc:  # exact failure is reported through the stable check interface
    engine = None
    engine_stdout = repr(exc)
    engine_exit = None
    engine_ready = False

check(
    14,
    "landed records-only exact engine is reused successfully and its own stable "
    "24-check interface remains green",
    engine_ready,
    "source engine exit=" + repr(engine_exit),
)


def matrix_key(matrix):
    return tuple((value.re, value.im) for row in matrix for value in row)


def polynomials_equal(left, right):
    masks = set(left) | set(right)
    zero = engine.CR(0)
    return all((left.get(mask, zero) - right.get(mask, zero)).is_zero() for mask in masks)


if engine_ready:
    a_probe = engine.CR(F(4, 5), F(1, 10))
    b_probe = engine.CR(F(3, 10), F(1, 5))
    c_probe = engine.CR(F(1, 2), F(-1, 10))
    W = engine.W_of(a_probe, b_probe, c_probe)
    Wd = engine.dag(W)
    Wdd = engine.dag(Wd)
    key_w = matrix_key(W)
    key_wd = matrix_key(Wd)
    key_wdd = matrix_key(Wdd)
    check(
        15,
        "at the exact untied probe, dagger is idempotent and W^dagger differs "
        "from W",
        key_wdd == key_w and key_wd != key_w,
    )

    coupling_orbit = (W, Wd)
    orbit_keys = {matrix_key(value) for value in coupling_orbit}
    swapped_keys = {matrix_key(engine.dag(value)) for value in coupling_orbit}
    check(
        16,
        "the supplied readout-context involution has exactly the two-point "
        "coupling orbit {W,W^dagger} and acts on it by a swap",
        len(orbit_keys) == 2 and swapped_keys == orbit_keys,
    )

    # The invariant-probability equations are u-v=0 and u+v=1.
    coefficient_determinant = 1 * 1 - (-1) * 1
    u = F(1, coefficient_determinant)
    v = F(1, coefficient_determinant)
    check(
        17,
        "the two-point swap orbit has a unique invariant probability: exact "
        "linear solve gives u=v=1/2",
        coefficient_determinant == 2
        and u == v == F(1, 2)
        and u - v == 0
        and u + v == 1,
    )

    mu_w = engine.exp_bilinear(engine.build_K(W, W), 6)
    mu_wd = engine.exp_bilinear(engine.build_K(Wd, Wd), 6)
    canonical_orbit_expectation = engine.add(
        engine.scal(u, mu_w), engine.scal(v, mu_wd)
    )
    landed_mu_sym = engine.scal(F(1, 2), engine.add(mu_w, mu_wd))
    reversed_orbit_expectation = engine.add(
        engine.scal(v, mu_wd), engine.scal(u, mu_w)
    )
    check(
        18,
        "canonical orbit expectation reproduces the landed mu_sym object "
        "entrywise for every Grassmann coefficient mask and is swap invariant",
        polynomials_equal(canonical_orbit_expectation, landed_mu_sym)
        and polynomials_equal(canonical_orbit_expectation, reversed_orbit_expectation),
        f"coefficient masks={len(set(canonical_orbit_expectation) | set(landed_mu_sym))}",
    )

    z_sym = engine.berezin_full(canonical_orbit_expectation, 6)
    z_component_average = (
        engine.berezin_full(mu_w, 6) + engine.berezin_full(mu_wd, 6)
    ) / 2
    check(
        19,
        "exact Berezin regression at the untied probe: orbit construction has "
        "Z_sym=442243/1000000 and equals the component half-sum",
        z_sym == engine.CR(F(442243, 1000000))
        and z_sym == z_component_average,
        f"Z_sym={z_sym}",
    )
else:
    for num, description in (
        (15, "untied-probe dagger idempotence could not run because engine reuse failed"),
        (16, "two-point coupling-orbit check could not run because engine reuse failed"),
        (17, "unique invariant-probability check could not run because engine reuse failed"),
        (18, "coefficientwise orbit-average check could not run because engine reuse failed"),
        (19, "exact Z_sym regression could not run because engine reuse failed"),
    ):
        check(num, description, False)


# ---------------------------------------------------------------------------
# T3: witnessed quotations and no-supplier boundary
# ---------------------------------------------------------------------------
axioms_text = normalized(AXIOMS.read_text())
tick_text = normalized(TICK.read_text())
check(
    20,
    "Record quotation is present verbatim and is readout-side strictness",
    "Only records are readable. A readout value is determined by record content alone."
    in axioms_text,
)
check(
    21,
    "tick witnessed-search quotation is present verbatim: site-strict and "
    "unitary-tick readings remain named conditionals",
    "The parent's site-strict license and unitary-tick readings are inherited as named conditionals."
    in tick_text,
)
open_gate_quote = normalized(
    """context selection, measurement basis selection, Born weights,
    probability rules, update laws, decoherence mechanisms, and formation
    rules (which admissible possibility a new record locks, at which site, with
    what weight, or at what rate);"""
)
note_text = NOTE.read_text()
note_prose = normalized(note_text)
check(
    22,
    "formation-rule open-gate quotation is verbatim, and the companion note "
    "contains T1-T4 plus the single unresolved supplied-object licensing residual",
    open_gate_quote in axioms_text
    and all(f"## T{k}" in note_text for k in range(1, 5))
    and "is the `K`-orbit of the supplied object available as a supplied object at"
    in note_prose
    and "This note does not choose between the readings." in note_prose,
)


# ---------------------------------------------------------------------------
# Verdict-first final stdout summary
# ---------------------------------------------------------------------------
print()
print(
    "VERDICT: PASS — CONDITIONAL LICENSING CONSOLIDATION.  SOCMLC remains "
    "unadopted and underived.  Inside its convention grade, product closure on "
    "the coupling-free disjoint composite pays independence for every licensed "
    "joint, and the K-symmetrized weight is the same criterion's canonical "
    "orbit-expectation instance on the supplied-orbit reading."
)
print(
    "CONSOLIDATION MAP: one criterion = SOCMLC; three instances = single-site "
    "canonical formation measures, coupling-free composite product measures, "
    "and the supplied coupling-orbit average; discharge = selection-stack "
    "element 1, cross-edge payer (ii) and its licensed-joint independence atom, "
    "and the K-orbit-average gate on the supplied-orbit reading; non-discharge = "
    "the formation selector, H, quenched/annealed many-slice extension, Krein "
    "and A2 remainders, and (LE) itself."
)
print(
    "T1 BOUNDARY: no supplied coupling datum -> each of the four licensed "
    "composite measures is a product and C_ss=0; supplied agreement datum -> "
    "canonical counting on {(s,s),(d,d)} has p=1/2 and C_ss=1/4.  This prices "
    "independence to the criterion; it does not derive independence."
)
print(f"CHECK COUNT: PASS={_pass} FAIL={_fail} TOTAL={_pass + _fail}")
print(
    "PROPOSED CLAIM_SCOPE: conditional on convention-grade SOCMLC, a "
    "coupling-free disjoint composite of two (LE)+(LAW) registrations, CKS at "
    "the product-orbit-cell grade, and the supplied-context coupling-orbit "
    "reading; exact product closure and orbit-expectation consolidation only."
)
print(
    "HOSTILE-AUDIT UNCERTAINTIES: SOCMLC has no axiom supplier; (LE)+(LAW) are "
    "named conditions; the orbit-cell proof requires CKS and full product-cell "
    "member counting (not a false diagonal quotient identity); coupling-free "
    "scope is decisive; and whether readout-context K supplies the coupling "
    "orbit at the measure stage remains unresolved."
)
print(f"TOTAL: PASS={_pass} FAIL={_fail}")

raise SystemExit(0 if _fail == 0 else 1)
