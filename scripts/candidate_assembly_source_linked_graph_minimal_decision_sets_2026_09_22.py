#!/usr/bin/env python3
"""Candidate assembly, twelfth edition: the source-linked graph from the axioms
to the eleven preserved targets, with results as AND nodes, route choices as
OR nodes, and the exact minimal decision sets of every target.

TOE derivation campaign by underdetermination witnesses and its next-steps
continuation.  The graph is supplied structure assembled from cited
results; the theorems are its verified properties: well-formedness,
acyclicity with a negative control, source linking on disk, and the exact
minimal decision sets under AND/OR semantics.  No completion percentage and
no physical identification.  Changes from the first edition: nearest-
neighbour locality is Admissibility text (its decision group is withdrawn);
the clock group becomes the order-law group without its order-blind
candidate; roles can be supplied or registered by formation; the photon
route runs through the static reading or through formation.  Third edition:
registered frames (open PR 8676) give soldering an alternative, coordinate
letters with an order law, in both formation routes.  Fourth edition: the
static route needs a frame source as well (open PR #8679): soldered vertex
records with supplied roles, or coordinate letters with roles read from labels.
Fifth edition: the formed photon route reaches the uniform ice measure only
through a coordinator (open PR #8686), formed ice is otherwise directed (open
PR #8687), and the letters may be fixed or relational (open PR #8691).  Sixth
edition: a positive static rule selects the equal-time Coulomb law (open PR
#8698), and formed flux moves as a persistent walk (open PR #8701).  Seventh
edition: single-site formation reaches the uniform ice measure beyond one top
cell only with plan letters (two planar squares, open PR #8715; two adjacent
cubes, open PR #8719; plans, open PR #8686); finite joint cell units reach
rows but not blocks, in the plane and in three dimensions (open PR #8720);
and relational spirals are rigid on the lattice and under the static reading
but amplified by the sweep (open PR #8717).  Eighth edition: beyond rows,
exact joint formation needs units unbounded along an axis formed as a chain,
so the joint-unit route needs an order law as well (open PR #8720), and the
static spiral is locally rigid in the full nonlinear relations (open PR
#8724).  Ninth edition: the landed torus ice measure has no local formation
order (open PR #8727), every linear ice sweep rule moves flux as a damped or
rigid Markov walk (open PR #8726), and seven relational letters carry the
frame (open PR #8729); the minimal sets are unchanged.  Tenth edition: no
planar window of two to five squares admits a single-site order (open PR
#8735), under local formation multi-qubit units leave relational first
formations a fair coin (open PR #8731), under the static reading with its
fixed octant relational frames with Sidon angles are globally rigid,
carrying the frame but no role pattern (open PR #8743), that rigidity needs
a global octant (open PR #8744), and layer units form uniform ice on
infinite prisms in the zero-flux sector (open PR #8740), whose flux sectors
carry a Gaussian stiffness (open PR #8746); the minimal sets are unchanged.
Eleventh edition: relational letters in alternating pairs record the role
pattern under the static reading away from the side-4 torus (open PR
#8750), and four-angle cycles record it on the landed ice torus (open PR
#8752), so with relational letters only, as under possibility covariance,
gravity's one unsoldered set becomes {alphabet, reading}; under the sweep
reading the cycle letters record no role pattern (open PR #8756), so that
route needs the static reading.  Twelfth edition: that route needs no
supplied octant.  Under the rotation-covariant rule the cycle letters record
their octant on the landed torus (open PR #8854), strong cycle letters record
the frame and the roles on every window (open PR #8856), and strong letters
are generic (open PR #8857); the minimal sets are unchanged.

Prints one line per check and `TOTAL: PASS=N FAIL=M`.
"""
import os
import sys

RESULTS = []


def check(label, ok, detail=""):
    ok = bool(ok)
    RESULTS.append(ok)
    tag = "PASS" if ok else "FAIL"
    print(f"[{tag}] {label}" + (f" :: {detail}" if detail else ""))
    return ok


D = "docs/"
L = "landed"
OP = "open"
NODES = {
    "AX": ("source", D + "MINIMAL_AXIOMS_2026-06-29.md"),
    "PRIM": ("source", "premise registry: scale_reference, kinetic_isotropy, realized_state"),
    "ORDER_LAW": (L, D + "ADMISSIBILITY_FORMATION_ORDER_MENU_ORDER_MIXTURE_MONOTONE_BOX_AND_CUBE_CENSUS_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "BINARY_ORDER_BLIND": (L, D + "FORMATION_ORDER_COVARIANCE_AND_ISOTROPIC_BINARY_ORDER_BLIND_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "HANDED_CENSUS": (L, D + "ADMISSIBILITY_HANDED_RULE_PSEUDOSCALAR_INVARIANT_CENSUS_AND_PARITY_ODD_RECORD_CORRELATORS_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "READABILITY": (L, D + "ADMISSIBILITY_READABILITY_CONTINUUM_ALPHABET_FISHER_RANK_AND_FORMATION_ORDER_SECOND_ORDER_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "COMPOSITION_ZEROS": (L, D + "COMPOSITION_LAW_SELECTION_GRADED_ZEROS_ORDER_BLIND_RULES_BOUNDED_THEOREM_NOTE_2026-09-13.md"),
    "GAUSS_SUPPORT": (L, D + "COVARIANT_NN_SUPPORT_RULES_GAUSS_LAW_AS_GLUED_SUPPORT_AND_HOLE_STATISTICS_BOUNDED_THEOREM_NOTE_2026-09-14.md"),
    "SOLDER_CENSUS": (L, D + "POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md"),
    "ROLES_NNN": (L, D + "THE_SUPERLATTICE_ROLE_PATTERN_IS_A_NEXT_NEAREST_NEIGHBOUR_SUPPORT_RULE_OVER_ROLES_AND_ROLES_ARE_NOT_RECORD_VALUES_BOUNDED_THEOREM_NOTE_2026-09-04.md"),
    "REPEAT_CERT_SELECTS": (L, D + "COVARIANT_EFFECT_MAP_NONSELECTION_AND_REPEAT_CERTAINTY_COLLAPSE_BOUNDED_THEOREM_NOTE_2026-07-11.md"),
    "BORN_PRICE": (L, D + "THE_BORN_PRICE_WORDINGS_HOMOGENEITY_IS_PAYABLE_ON_THE_CONTINUUM_LAW_AS_IT_STANDS_THE_COLLINEAR_MENUS_NEED_A_SCALE_READING_RULE_THE_FOUR_OUTCOME_MENU_PAYS_WITH_NO_CLAUSE_AND_NONE_REMOVES_THE_FAIR_COIN_BOUNDED_NOTE_2026-09-05.md"),
    "GLUED_HIERARCHY": (L, D + "A_HIERARCHY_OF_NEIGHBOURHOOD_CONDITIONS_GLUED_BREAKABLE_AND_FREE_RECORD_GROUPS_UNDER_SHIFTING_TICKS_BOUNDED_THEOREM_NOTE_2026-09-03.md"),
    "CUBIC_ICE_RK": (L, D + "SPIN_HALF_CUBIC_ICE_EXACT_RK_COULOMB_CORRELATIONS_AND_FINITE_QUBIT_PHOTON_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-03.md"),
    "GRAVITY_BOUNDARIES": (L, D + "LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md"),
    "FAIR_COIN_ANTIPARALLEL": (OP, "open PR #8637 (menus-and-Born)"),
    "SOLDERED_SPLIT": (OP, "open PR #8637 (menus-and-Born)"),
    "AFFINE_REDUCTION": (OP, "open PR #8637 (menus-and-Born)"),
    "CLOCK_INVISIBILITY": (OP, "open PR #8641 (clock-and-rate)"),
    "HOLE_READS_CLOCK": (OP, "open PR #8641 (clock-and-rate)"),
    "BLOCK_CHAIN_EQUALITY": (OP, "open PR #8643 (formation-unit)"),
    "UNIT_DIAL": (OP, "open PR #8643 (formation-unit)"),
    "KERNEL_MISMATCH": (OP, "open PR #8646 (record-dynamics)"),
    "NN_EXCLUSION": (OP, "open PR #8646 (record-dynamics)"),
    "CODE_RIGIDITY": (OP, "open PR #8646 (record-dynamics)"),
    "ORDER_BLIND_RANGE": (OP, "open PR #8663 (order-blind formation)"),
    "UNSOLDERED_CONSTANCY": (OP, "open PR #8664 (zeros and holes)"),
    "PAIR_FORM_HOLES": (OP, "open PR #8664 (zeros and holes)"),
    "ORDER_VISIBLE": (OP, "open PR #8666 (holes as unrecorded sites)"),
    "ICE_FORMATION": (OP, "open PR #8667 (ice support under formation)"),
    "STAR_BROADCAST": (OP, "open PR #8669 (star constraints)"),
    "ROLES_REGISTERED": (OP, "open PR #8669 (star constraints)"),
    "ORDER_LAW_FRONTS": (OP, "open PR #8670 (order laws)"),
    "SOLDER_MENU": (OP, "open PR #8671 (soldering menu)"),
    "FRAME_REGISTRATION": (OP, "open PR #8676 (registered frames)"),
    "STATIC_ICE_RECORDS": (OP, "open PR #8679 (static ice needs a frame source)"),
    "UNIFORM_ICE_COORDINATION": (OP, "open PR #8686 (uniform ice by formation needs a coordinator)"),
    "DIRECTED_ICE": (OP, "open PR #8687 (directed ice from sweep formation)"),
    "RELATIONAL_FRAMES": (OP, "open PR #8691 (relational frames in one qubit)"),
    "COULOMB_SELECTION": (OP, "open PR #8698 (positive static rules select the Coulomb measure)"),
    "FLUX_TRANSPORT": (OP, "open PR #8701 (formed flux as a persistent walk)"),
    "TWO_SQUARES_NO_ORDER": (OP, "open PR #8715 (two planar squares admit no local formation order; one cube needs its cube site)"),
    "TWO_CUBES_NO_ORDER": (OP, "open PR #8719 (two adjacent cubes admit no local formation order)"),
    "SPIRAL_RIGIDITY": (OP, "open PR #8717 (relational spirals rigid on the lattice and statically, amplified by the sweep)"),
    "JOINT_CELL_UNITS": (OP, "open PR #8720 (joint cell units: rows yes, blocks no, in the plane and in three dimensions)"),
    "STATIC_SPIRAL_RIGIDITY": (OP, "open PR #8724 (relational spirals locally rigid under the static reading, nonlinear)"),
    "LINEAR_SWEEP_TRANSPORT": (OP, "open PR #8726 (every linear ice sweep rule moves flux as a damped or rigid Markov walk)"),
    "TORUS_NO_ORDER": (OP, "open PR #8727 (the landed torus ice measure has no local formation order)"),
    "FINITE_RELATIONAL_LETTERS": (OP, "open PR #8729 (seven relational letters carry the lattice frame)"),
    "POLYOMINO_NO_ORDER": (OP, "open PR #8735 (no planar window of two to five squares admits a single-site order)"),
    "UNIT_FAIR_COIN": (OP, "open PR #8731 (multi-qubit units leave relational first formations a fair coin)"),
    "STATIC_GLOBAL_RIGIDITY": (OP, "open PR #8743 (static relational frames with a fixed octant are globally rigid for Sidon angles)"),
    "LAYER_UNITS_PRISMS": (OP, "open PR #8740 (layer units form uniform ice on infinite prisms at zero flux)"),
    "GLOBAL_OCTANT": (OP, "open PR #8744 (static relational rigidity needs a global octant)"),
    "FLUX_STIFFNESS": (OP, "open PR #8746 (layer flux sectors carry a Gaussian stiffness)"),
    "PAIR_LETTER_ROLES": (OP, "open PR #8750 (relational letters in alternating pairs record the role pattern, not on the side-4 torus)"),
    "CYCLE_LETTER_ROLES": (OP, "open PR #8752 (relational letters in four-angle cycles record the role pattern on the landed ice torus)"),
    "SWEEP_NO_ROLES": (OP, "open PR #8756 (under the sweep reading cycle letters record no role pattern)"),
    "OCTANT_RECORDED": (OP, "open PR #8854 (under the rotation-covariant rule cycle letters record their octant on the landed torus)"),
    "FOLDED_ROLES": (OP, "open PR #8856 (strong cycle letters record frame and roles on every window under the covariant rule)"),
    "GENERIC_LETTERS": (OP, "open PR #8857 (strong cycle letters are generic)"),
    "DEC_SOLDER": ("decision", "recorded in SOLDER_CENSUS and SOLDER_MENU"),
    "DEC_MIRROR": ("decision", "recorded in HANDED_CENSUS"),
    "DEC_ALPHABET": ("decision", "recorded in READABILITY, ROLES_REGISTERED, FRAME_REGISTRATION, STATIC_ICE_RECORDS and UNIFORM_ICE_COORDINATION"),
    "DEC_GRADING": ("decision", "recorded in COMPOSITION_ZEROS"),
    "DEC_ROLES": ("decision", "recorded in GAUSS_SUPPORT and ROLES_NNN"),
    "DEC_AFFINITY": ("decision", "recorded in AFFINE_REDUCTION"),
    "DEC_MENU_SUPPLIER": ("decision", "recorded in AFFINE_REDUCTION"),
    "DEC_REPEAT_CERT": ("decision", "recorded in AFFINE_REDUCTION and REPEAT_CERT_SELECTS"),
    "DEC_ORDER_LAW": ("decision", "recorded in HOLE_READS_CLOCK and ORDER_LAW_FRONTS"),
    "DEC_UNIT": ("decision", "recorded in UNIT_DIAL"),
    "DEC_RULE": ("decision", "recorded in ORDER_LAW and ORDER_VISIBLE"),
    "DEC_READING": ("decision", "recorded in ORDER_BLIND_RANGE and PAIR_FORM_HOLES"),
    "ROLES_SOURCE": ("choice", "supplied roles, roles registered by formation, or roles read from static coordinate or relational pair letters"),
    "PHOTON_ROUTE": ("choice", "static reading with the landed ice measure, or formation"),
    "STATIC_ICE_ROUTE": ("route", "static reading, the landed uniform ice measure, and a static frame source"),
    "STATIC_FRAME_SOURCE": ("choice", "soldered vertex records, or coordinate letters under the static reading"),
    "STATIC_LETTERS_ROUTE": ("route", "coordinate letters make the static ice records nearest-neighbour"),
    "ROLES_STATIC_LETTERS": ("route", "roles read from static coordinate letters"),
    "ROLES_PAIR_LETTERS": ("route", "roles read from static relational letters: pairs away from the side-4 torus, four-angle cycles on it, strong cycles on every window under the rotation-covariant rule"),
    "FORMED_ICE_ROUTE": ("route", "formation of the ice support (soldered or registered frame)"),
    "REGISTERED_FRAME_ROUTE": ("route", "coordinate letters with an order law register the lattice frame"),
    "FRAME_SOURCE": ("choice", "soldering, or a frame registered by coordinate letters"),
    "LETTER_SCHEME": ("choice", "fixed coordinate letters, or relational spiral letters under possibility covariance"),
    "ORDER_OR_UNIT": ("choice", "single sites with an order law, or joint formation units"),
    "SINGLE_SITE_ROUTE": ("route", "single-site formation with an order law; plan letters beyond one top cell"),
    "JOINT_UNIT_ROUTE": ("route", "joint formation units; beyond rows, units unbounded along an axis formed as a chain by an order law"),
    "T_FORMATION_LAW": ("target", "design note: formation law"),
    "T_MENUS": ("target", "design note: possibility domain and menus"),
    "T_HANDEDNESS": ("target", "design note: handedness"),
    "T_BORN": ("target", "design note: Born weights"),
    "T_READABILITY": ("target", "design note: readability"),
    "T_CLOCK_RATE": ("target", "design note: clock/rate"),
    "T_FORMATION_UNIT": ("target", "design note: formation unit"),
    "T_RECORD_DYNAMICS": ("target", "design note: record dynamics"),
    "T_MATTER": ("target", "design note: matter/composition"),
    "T_GAUGE": ("target", "design note: support/gauge structure"),
    "T_GRAVITY": ("target", "design note: downstream gravity"),
}
CANDIDATES = {
    "DEC_SOLDER": ["trivial action (unsoldered)", "sign twist", "axis soldering", "full soldering (the three Cl(3,0) generators are the lattice axes)"],
    "DEC_MIRROR": ["covariance under improper rotations", "mirror sense as registered content", "parity fix clause"],
    "DEC_ALPHABET": ["continuum Bloch alphabet", "finite orbit alphabet", "eight axis-labelled role letters",
                     "coordinate letters (Z_4^3 labels with tags)",
                     "relational spiral letters (Bloch sphere, possibility covariance; seven values suffice, open PR #8729)",
                     "plan letters carrying a window configuration (open PR #8686)"],
    "DEC_GRADING": ["graded composition", "ordinary composition with a supplied encoding"],
    "DEC_ROLES": ["window extension", "sector clause", "supplied next-nearest-neighbour role pattern"],
    "DEC_AFFINITY": ["affinity/mixture-linearity in the neighbour state", "leave the non-affine class open"],
    "DEC_MENU_SUPPLIER": ["own value", "second neighbour", "lattice axis"],
    "DEC_REPEAT_CERT": ["same-label repeat certainty", "flipped-label certainty (anti-Born)"],
    "DEC_ORDER_LAW": ["independent identical clocks", "eagerness (count) clock", "value clock",
                      "front-like law with no first formation", "time as record count"],
    "DEC_UNIT": ["single-site unit", "covariant set with product fill", "covariant set with block-chain fill", "support-aligned glued units",
                 "units unbounded along an axis, formed as a chain (open PR #8720)"],
    "DEC_RULE": ["order-sensitive nearest-neighbour rule", "soldered order-blind rule of nearest-neighbour reach", "support rule with holes"],
    "DEC_READING": ["formation reading of the distribution sentence", "static reading of the distribution sentence"],
}
WITHDRAWN = {"DEC_LOCALITY": "nearest-neighbour locality is Admissibility text (open PR #8646, corrected)",
             "order-blind physical rule": "excluded under the unsoldered reading by the text (open PRs #8663, #8664, #8666)"}
EDGES = [("AX", n) for n, (k, p) in NODES.items() if k in (L, OP)] + [
    ("PRIM", "ORDER_LAW"), ("PRIM", "ORDER_VISIBLE"), ("PRIM", "ORDER_LAW_FRONTS"),
    ("STAR_BROADCAST", "ROLES_REGISTERED"), ("FRAME_SOURCE", "ROLES_REGISTERED"),
    ("DEC_SOLDER", "FRAME_SOURCE"), ("REGISTERED_FRAME_ROUTE", "FRAME_SOURCE"),
    ("FRAME_REGISTRATION", "LETTER_SCHEME"), ("RELATIONAL_FRAMES", "LETTER_SCHEME"),
    ("LETTER_SCHEME", "REGISTERED_FRAME_ROUTE"), ("DEC_ALPHABET", "REGISTERED_FRAME_ROUTE"),
    ("DEC_ORDER_LAW", "REGISTERED_FRAME_ROUTE"),
    ("DEC_ORDER_LAW", "ROLES_REGISTERED"), ("DEC_ALPHABET", "ROLES_REGISTERED"),
    ("DEC_ROLES", "ROLES_SOURCE"), ("ROLES_REGISTERED", "ROLES_SOURCE"),
    ("CUBIC_ICE_RK", "STATIC_ICE_ROUTE"), ("DEC_READING", "STATIC_ICE_ROUTE"),
    ("STATIC_ICE_RECORDS", "STATIC_ICE_ROUTE"), ("STATIC_FRAME_SOURCE", "STATIC_ICE_ROUTE"), ("COULOMB_SELECTION", "STATIC_ICE_ROUTE"),
    ("DEC_SOLDER", "STATIC_FRAME_SOURCE"), ("STATIC_LETTERS_ROUTE", "STATIC_FRAME_SOURCE"),
    ("STATIC_ICE_RECORDS", "STATIC_LETTERS_ROUTE"), ("DEC_ALPHABET", "STATIC_LETTERS_ROUTE"),
    ("STATIC_ICE_RECORDS", "ROLES_STATIC_LETTERS"), ("DEC_READING", "ROLES_STATIC_LETTERS"),
    ("DEC_ALPHABET", "ROLES_STATIC_LETTERS"), ("ROLES_STATIC_LETTERS", "ROLES_SOURCE"),
    ("ICE_FORMATION", "FORMED_ICE_ROUTE"), ("FRAME_SOURCE", "FORMED_ICE_ROUTE"), ("UNIFORM_ICE_COORDINATION", "FORMED_ICE_ROUTE"), ("ORDER_OR_UNIT", "FORMED_ICE_ROUTE"),
    ("SINGLE_SITE_ROUTE", "ORDER_OR_UNIT"), ("JOINT_UNIT_ROUTE", "ORDER_OR_UNIT"),
    ("DEC_UNIT", "JOINT_UNIT_ROUTE"), ("JOINT_CELL_UNITS", "JOINT_UNIT_ROUTE"), ("DEC_ORDER_LAW", "JOINT_UNIT_ROUTE"),
    ("DEC_ORDER_LAW", "SINGLE_SITE_ROUTE"), ("DEC_ALPHABET", "SINGLE_SITE_ROUTE"),
    ("TWO_SQUARES_NO_ORDER", "SINGLE_SITE_ROUTE"), ("TWO_CUBES_NO_ORDER", "SINGLE_SITE_ROUTE"),
    ("SPIRAL_RIGIDITY", "RELATIONAL_FRAMES"), ("STATIC_SPIRAL_RIGIDITY", "RELATIONAL_FRAMES"),
    ("FINITE_RELATIONAL_LETTERS", "RELATIONAL_FRAMES"), ("TORUS_NO_ORDER", "SINGLE_SITE_ROUTE"),
    ("LINEAR_SWEEP_TRANSPORT", "T_RECORD_DYNAMICS"), ("POLYOMINO_NO_ORDER", "SINGLE_SITE_ROUTE"),
    ("UNIT_FAIR_COIN", "RELATIONAL_FRAMES"), ("STATIC_GLOBAL_RIGIDITY", "RELATIONAL_FRAMES"),
    ("LAYER_UNITS_PRISMS", "JOINT_UNIT_ROUTE"), ("GLOBAL_OCTANT", "RELATIONAL_FRAMES"),
    ("FLUX_STIFFNESS", "JOINT_UNIT_ROUTE"),
    ("PAIR_LETTER_ROLES", "ROLES_PAIR_LETTERS"), ("DEC_READING", "ROLES_PAIR_LETTERS"), ("DEC_ALPHABET", "ROLES_PAIR_LETTERS"),
    ("CYCLE_LETTER_ROLES", "ROLES_PAIR_LETTERS"), ("SWEEP_NO_ROLES", "ROLES_PAIR_LETTERS"),
    ("OCTANT_RECORDED", "ROLES_PAIR_LETTERS"), ("FOLDED_ROLES", "ROLES_PAIR_LETTERS"), ("GENERIC_LETTERS", "ROLES_PAIR_LETTERS"),
    ("ROLES_PAIR_LETTERS", "ROLES_SOURCE"),
    ("STATIC_ICE_ROUTE", "PHOTON_ROUTE"), ("FORMED_ICE_ROUTE", "PHOTON_ROUTE"),
    ("ORDER_LAW", "T_FORMATION_LAW"), ("ORDER_VISIBLE", "T_FORMATION_LAW"), ("UNSOLDERED_CONSTANCY", "T_FORMATION_LAW"),
    ("BINARY_ORDER_BLIND", "T_FORMATION_LAW"), ("DEC_RULE", "T_FORMATION_LAW"), ("DEC_ORDER_LAW", "T_FORMATION_LAW"),
    ("SOLDER_CENSUS", "T_MENUS"), ("FAIR_COIN_ANTIPARALLEL", "T_MENUS"), ("SOLDERED_SPLIT", "T_MENUS"),
    ("DEC_SOLDER", "T_MENUS"), ("DEC_MENU_SUPPLIER", "T_MENUS"),
    ("HANDED_CENSUS", "T_HANDEDNESS"), ("DEC_MIRROR", "T_HANDEDNESS"), ("DEC_SOLDER", "T_HANDEDNESS"),
    ("AFFINE_REDUCTION", "T_BORN"), ("BORN_PRICE", "T_BORN"), ("REPEAT_CERT_SELECTS", "T_BORN"),
    ("DEC_AFFINITY", "T_BORN"), ("DEC_REPEAT_CERT", "T_BORN"), ("DEC_MENU_SUPPLIER", "T_BORN"),
    ("READABILITY", "T_READABILITY"), ("DEC_ALPHABET", "T_READABILITY"),
    ("CLOCK_INVISIBILITY", "T_CLOCK_RATE"), ("HOLE_READS_CLOCK", "T_CLOCK_RATE"), ("ORDER_VISIBLE", "T_CLOCK_RATE"),
    ("PAIR_FORM_HOLES", "T_CLOCK_RATE"), ("ORDER_LAW_FRONTS", "T_CLOCK_RATE"), ("DEC_ORDER_LAW", "T_CLOCK_RATE"),
    ("BLOCK_CHAIN_EQUALITY", "T_FORMATION_UNIT"), ("UNIT_DIAL", "T_FORMATION_UNIT"),
    ("GLUED_HIERARCHY", "T_FORMATION_UNIT"), ("DEC_UNIT", "T_FORMATION_UNIT"),
    ("KERNEL_MISMATCH", "T_RECORD_DYNAMICS"), ("NN_EXCLUSION", "T_RECORD_DYNAMICS"), ("CODE_RIGIDITY", "T_RECORD_DYNAMICS"),
    ("ORDER_BLIND_RANGE", "T_RECORD_DYNAMICS"), ("PHOTON_ROUTE", "T_RECORD_DYNAMICS"), ("DIRECTED_ICE", "T_RECORD_DYNAMICS"), ("FLUX_TRANSPORT", "T_RECORD_DYNAMICS"),
    ("COMPOSITION_ZEROS", "T_MATTER"), ("DEC_GRADING", "T_MATTER"),
    ("GAUSS_SUPPORT", "T_GAUGE"), ("ROLES_NNN", "T_GAUGE"), ("GLUED_HIERARCHY", "T_GAUGE"), ("ROLES_SOURCE", "T_GAUGE"),
    ("GRAVITY_BOUNDARIES", "T_GRAVITY"), ("T_RECORD_DYNAMICS", "T_GRAVITY"), ("T_GAUGE", "T_GRAVITY"),
    ("HOLE_READS_CLOCK", "T_GRAVITY"),
]
OPEN_EDGES = {
    "T_GRAVITY": ["record-statistic bridge from a supported source to a curvature response (unproved)",
                  "continuum bridge (unproved)"],
    "T_RECORD_DYNAMICS": ["photon dynamics rests on the landed quantum Hamiltonian (supplied bridge; the equal-time law is selected by a positive static rule, open PR #8698; every linear sweep rule moves flux as a damped or rigid Markov walk, open PR #8726)",
                          "defect densities of front-like order laws on large windows (not computed)",
                          "first-formation orders beyond corner growth, broadcast and the designed order (not classified)",
                          "exact formation of the uniform ice measure by layer units with an infinite cross-section, or by single sites on planar windows beyond five squares or three-dimensional windows beyond two cubes (not searched; finite cell units fail around blocks, chains of units work, open PR #8720; on prisms of cross-section 2 x 2 layer units are exact in the zero-flux sector, open PR #8740; no planar window of two to five squares and no pair of adjacent cubes admits a single-site order, open PRs #8715, #8719, #8735)"],
    "T_MATTER": ["record/role bridge to physical fermions (unconstructed, per the support-rule note)"],
}
TARGET_BRIEF = ["formation law", "possibility domain and menus", "handedness", "Born weights", "readability",
                "clock/rate", "formation unit", "record dynamics", "matter/composition",
                "support/gauge structure", "downstream gravity"]
PARENTS = {}
for u, v in EDGES:
    PARENTS.setdefault(v, []).append(u)


def minimise(fam):
    fam = {frozenset(s) for s in fam}
    return {s for s in fam if not any(t < s for t in fam)}


def decision_sets(node, memo=None, parents=None):
    """Minimal decision sets under AND (results, routes, targets) and OR (choices)."""
    memo = {} if memo is None else memo
    parents = PARENTS if parents is None else parents
    if node in memo:
        return memo[node]
    kind = NODES[node][0]
    if kind == "decision":
        out = {frozenset([node])}
    elif kind == "choice":
        out = set()
        for p in parents.get(node, ()):
            out |= decision_sets(p, memo, parents)
        out = minimise(out)
    else:
        out = {frozenset()}
        for p in parents.get(node, ()):
            out = minimise({a | b for a in out for b in decision_sets(p, memo, parents)})
    memo[node] = out
    return out


def topo_order(nodes, parents):
    order, seen, done = [], set(), set()

    def visit(n):
        if n in done:
            return True
        if n in seen:
            return False
        seen.add(n)
        for p in parents.get(n, ()):
            if not visit(p):
                return False
        done.add(n)
        order.append(n)
        return True
    try:
        ok = all(visit(n) for n in nodes)
    except RecursionError:
        return False, order
    return ok, order


print("== 1. Well-formedness and source linking ==")
kinds = {k: sum(1 for n, (kk, p) in NODES.items() if kk == k) for k in ("source", L, OP, "decision", "choice", "route", "target")}
check("node ledger: 2 sources, 13 landed, 46 open, 12 decision groups, 6 choices, 8 routes, 11 targets",
      kinds == {"source": 2, L: 13, OP: 46, "decision": 12, "choice": 6, "route": 8, "target": 11} and len(NODES) == 98)
check("every edge endpoint is declared; no edge enters a source or a decision; target edges go to targets",
      all(u in NODES and v in NODES for u, v in EDGES)
      and all(NODES[v][0] not in ("source", "decision") for u, v in EDGES)
      and all(NODES[v][0] == "target" for u, v in EDGES if NODES[u][0] == "target"))
check("every landed node's provenance is a note path present on this revision of the repository",
      all(p.startswith(D) and os.path.exists(p) for n, (k, p) in NODES.items() if k == L))
check("every open node names a campaign pull request; the withdrawn locality group is absent",
      all(p.startswith("open PR #8") for n, (k, p) in NODES.items() if k == OP) and "DEC_LOCALITY" not in NODES)
check("decision groups carry >= 2 recorded candidates; the order-law group no longer lists an order-blind rule",
      set(CANDIDATES) == {n for n, (k, p) in NODES.items() if k == "decision"}
      and all(len(c) >= 2 for c in CANDIDATES.values())
      and not any("order-blind physical rule" in c for c in CANDIDATES["DEC_ORDER_LAW"]),
      f"{sum(len(c) for c in CANDIDATES.values())} recorded candidate clauses in 12 groups")
check("the eleven targets are exactly the design note's preserved list",
      [NODES[n][1].replace("design note: ", "") for n in NODES if NODES[n][0] == "target"] == TARGET_BRIEF)

print()
print("== 2. Acyclicity and minimal decision sets ==")
ACYC, ORD = topo_order(list(NODES), PARENTS)
check("the graph is acyclic over all 98 nodes, and the same sorter rejects a two-node cycle",
      ACYC and len(ORD) == 98 and topo_order(("a", "b"), {"a": ["b"], "b": ["a"]})[0] is False)
SETS = {t: decision_sets(t) for t in NODES if NODES[t][0] == "target"}
fmt = lambda fam: " | ".join(sorted("{" + ",".join(sorted(x.replace("DEC_", "") for x in s)) + "}" for s in fam))
EXPECT_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"})}
check("gravity has exactly four minimal decision sets: every formation set holds the order law, every static set the reading",
      SETS["T_GRAVITY"] == EXPECT_GRAVITY
      and all(("DEC_ORDER_LAW" in s) != ("DEC_READING" in s) for s in SETS["T_GRAVITY"]), fmt(SETS["T_GRAVITY"]))
NOLAYER = {k: [q for q in v if not (k == "JOINT_UNIT_ROUTE" and q == "DEC_ORDER_LAW")] for k, v in PARENTS.items()}
SEVENTH_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ROLES"})}
check("control: without the layer order, gravity's sets return to the seventh edition's",
      decision_sets("T_GRAVITY", parents=NOLAYER) == SEVENTH_GRAVITY, fmt(decision_sets("T_GRAVITY", parents=NOLAYER)))
check("single-site formation of the uniform measure needs plan letters, so soldering with an order law alone no longer reaches gravity",
      decision_sets("SINGLE_SITE_ROUTE") == {frozenset({"DEC_ORDER_LAW", "DEC_ALPHABET"})}
      and frozenset({"DEC_SOLDER", "DEC_ORDER_LAW", "DEC_ROLES"}) not in SETS["T_GRAVITY"],
      "single-site route: " + fmt(decision_sets("SINGLE_SITE_ROUTE")))
NOPLAN = {k: [q for q in v if not (k == "SINGLE_SITE_ROUTE" and q == "DEC_ALPHABET")] for k, v in NOLAYER.items()}
SIXTH_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_ALPHABET", "DEC_READING"},
    {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_ORDER_LAW", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_UNIT", "DEC_ROLES"})}
check("control: without the layer order and the plan letters, gravity's sets return to the sixth edition's five",
      decision_sets("T_GRAVITY", parents=NOPLAN) == SIXTH_GRAVITY, fmt(decision_sets("T_GRAVITY", parents=NOPLAN)))
check("every minimal set of gravity contains a frame source: soldering or the alphabet",
      all("DEC_SOLDER" in s or "DEC_ALPHABET" in s for s in SETS["T_GRAVITY"]),
      "the static route's supplied Hamiltonian remains an open edge")
NOSTAT = {k: [q for q in v if q not in ("STATIC_ICE_RECORDS", "STATIC_FRAME_SOURCE", "ROLES_STATIC_LETTERS", "ROLES_PAIR_LETTERS")]
          for k, v in NOPLAN.items()}
OLD_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_ORDER_LAW"}, {"DEC_READING", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_ORDER_LAW", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_UNIT", "DEC_ROLES"})}
check("control: without those and the static frame source, gravity's sets return to the third edition's",
      decision_sets("T_GRAVITY", parents=NOSTAT) == OLD_GRAVITY, fmt(decision_sets("T_GRAVITY", parents=NOSTAT)))
PC = {k: list(v) for k, v in PARENTS.items()}
PC["LETTER_SCHEME"] = []
PC["ROLES_SOURCE"] = [p for p in PARENTS["ROLES_SOURCE"] if p not in ("ROLES_REGISTERED", "ROLES_STATIC_LETTERS")]
PC_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_READING"}, {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"}, {"DEC_ALPHABET", "DEC_ORDER_LAW", "DEC_ROLES", "DEC_SOLDER"})}
check("control: with relational letters only, as under possibility covariance, gravity's one unsoldered minimal set is {alphabet, reading}",
      decision_sets("T_GRAVITY", parents=PC) == PC_GRAVITY
      and {s for s in PC_GRAVITY if "DEC_SOLDER" not in s} == {frozenset({"DEC_ALPHABET", "DEC_READING"})},
      fmt(decision_sets("T_GRAVITY", parents=PC)) + "; fixed letters are unavailable and relational letters have no first "
      "formation (open PRs 8691, 8731), so the letter scheme is empty; registered roles need fixed parity letters, and "
      "relational letters record the role pattern: pairs away from the side-4 torus (open PR #8750), four-angle cycles on it "
      "(open PR #8752)")
PC0 = {k: list(v) for k, v in PC.items()}
PC0["ROLES_SOURCE"] = [p for p in PC["ROLES_SOURCE"] if p != "ROLES_PAIR_LETTERS"]
PC0_GRAVITY = {frozenset(s) for s in (
    {"DEC_ALPHABET", "DEC_READING", "DEC_ROLES"}, {"DEC_SOLDER", "DEC_READING", "DEC_ROLES"},
    {"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW", "DEC_ROLES"}, {"DEC_ALPHABET", "DEC_ORDER_LAW", "DEC_ROLES", "DEC_SOLDER"})}
check("control: with single-angle relational letters only, the unsoldered set is {alphabet, reading, roles}",
      decision_sets("T_GRAVITY", parents=PC0) == PC0_GRAVITY,
      fmt(decision_sets("T_GRAVITY", parents=PC0)) + "; a single-angle static record carries no role pattern (open PR #8743)")
check("record dynamics: a frame source in every set (static or formed; soldering or letters)",
      SETS["T_RECORD_DYNAMICS"] == {frozenset({"DEC_READING", "DEC_SOLDER"}), frozenset({"DEC_READING", "DEC_ALPHABET"}),
                                    frozenset({"DEC_SOLDER", "DEC_UNIT", "DEC_ORDER_LAW"}), frozenset({"DEC_ALPHABET", "DEC_ORDER_LAW"})},
      fmt(SETS["T_RECORD_DYNAMICS"]))
check("gauge: supplied roles, or roles read from coordinate letters under formation or the static reading",
      SETS["T_GAUGE"] == {frozenset({"DEC_ROLES"}), frozenset({"DEC_ALPHABET", "DEC_ORDER_LAW"}),
                          frozenset({"DEC_ALPHABET", "DEC_READING"})},
      fmt(SETS["T_GAUGE"]))
check("the formed photon route passes through the coordinator result; directed ice feeds record dynamics; letters are fixed or relational",
      "UNIFORM_ICE_COORDINATION" in PARENTS["FORMED_ICE_ROUTE"] and "DIRECTED_ICE" in PARENTS["T_RECORD_DYNAMICS"]
      and set(PARENTS["LETTER_SCHEME"]) == {"FRAME_REGISTRATION", "RELATIONAL_FRAMES"}
      and NODES["LETTER_SCHEME"][0] == "choice"
      and "COULOMB_SELECTION" in PARENTS["STATIC_ICE_ROUTE"] and "FLUX_TRANSPORT" in PARENTS["T_RECORD_DYNAMICS"]
      and {"TWO_SQUARES_NO_ORDER", "TWO_CUBES_NO_ORDER", "DEC_ALPHABET", "DEC_ORDER_LAW"} <= set(PARENTS["SINGLE_SITE_ROUTE"])
      and "SPIRAL_RIGIDITY" in PARENTS["RELATIONAL_FRAMES"] and "JOINT_CELL_UNITS" in PARENTS["JOINT_UNIT_ROUTE"]
      and "DEC_ORDER_LAW" in PARENTS["JOINT_UNIT_ROUTE"] and "STATIC_SPIRAL_RIGIDITY" in PARENTS["RELATIONAL_FRAMES"]
      and "FINITE_RELATIONAL_LETTERS" in PARENTS["RELATIONAL_FRAMES"] and "TORUS_NO_ORDER" in PARENTS["SINGLE_SITE_ROUTE"]
      and "LINEAR_SWEEP_TRANSPORT" in PARENTS["T_RECORD_DYNAMICS"] and "POLYOMINO_NO_ORDER" in PARENTS["SINGLE_SITE_ROUTE"]
      and "UNIT_FAIR_COIN" in PARENTS["RELATIONAL_FRAMES"] and "STATIC_GLOBAL_RIGIDITY" in PARENTS["RELATIONAL_FRAMES"]
      and "LAYER_UNITS_PRISMS" in PARENTS["JOINT_UNIT_ROUTE"] and "GLOBAL_OCTANT" in PARENTS["RELATIONAL_FRAMES"]
      and "FLUX_STIFFNESS" in PARENTS["JOINT_UNIT_ROUTE"] and "PAIR_LETTER_ROLES" in PARENTS["ROLES_PAIR_LETTERS"]
      and "CYCLE_LETTER_ROLES" in PARENTS["ROLES_PAIR_LETTERS"] and "SWEEP_NO_ROLES" in PARENTS["ROLES_PAIR_LETTERS"]
      and all(n in PARENTS["ROLES_PAIR_LETTERS"] for n in ("OCTANT_RECORDED", "FOLDED_ROLES", "GENERIC_LETTERS")),
      "the window results carry plan letters into single-site formation, the unit results carry the layer order into joint units, and the spiral, letter and multi-qubit unit results join the relational letters")
check("formation law {rule, order law}; clock/rate {order law}; no target is decision-free",
      SETS["T_FORMATION_LAW"] == {frozenset({"DEC_RULE", "DEC_ORDER_LAW"})}
      and SETS["T_CLOCK_RATE"] == {frozenset({"DEC_ORDER_LAW"})}
      and all(frozenset() not in fam for fam in SETS.values()))
check("every decision group appears in some target's minimal sets; open edges are declared",
      {d for fam in SETS.values() for s in fam for d in s} == {n for n in NODES if NODES[n][0] == "decision"}
      and sum(len(v) for v in OPEN_EDGES.values()) == 7)

print()
print(f"TOTAL: PASS={sum(RESULTS)} FAIL={len(RESULTS) - sum(RESULTS)}")
sys.exit(0 if all(RESULTS) else 1)
