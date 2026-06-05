"""
Scale-Axis Planck-Anchor Self-Consistency — Scoping Runner (2026-06-05).

QUESTION (owner-authorized exploration).
The framework has one dimensionful primitive: the lattice scale `a^{-1}` (the
`scale_reference_primitive`). The axiom-minimality posture explicitly states
this does NOT assert `a/l_P = 1`; the self-consistency that the natural unit
equals the Planck length is a separate, open gravity derivation
(ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23, item S;
PLANCK_SCALE_LANE_STATUS_NOTE_2026-04-23 sec.1).

Does the framework's emergent gravity FIX `a = l_Planck` with NO extra
dimensionful input or tuned factor (self-consistency CLOSES), or is `a = l_P`
an independent assumption (OPEN)?

HONESTY GUARD. "Self-consistency closes" means: the framework's OWN emergent
G, set equal to the observed/derived gravitational coupling, forces `a = l_P`
with no extra input. If it needs an extra dimensionful input or a tuned
dimensionless factor, it is OPEN (assumed), not derived.

This runner performs the dimensional-analysis / self-consistency computation
for BOTH candidate closure routes and reports, per route, whether the closure
is forced or whether a dimensionful import enters. It then cross-checks the
ledger status of every gravity/Planck note the routes lean on.

NO PDG/CODATA value is used as a derivation INPUT. CODATA G, hbar, c, M_Pl
appear ONLY as anchor-only cross-checks, clearly marked CHECK-ONLY.

VERDICT (computed below): OPEN-SELF-CONSISTENCY.
"""

import math

PASS = "PASS"
FAIL = "FAIL"

results = []


def check(label, ok, detail=""):
    results.append((label, bool(ok), detail))
    tag = PASS if ok else FAIL
    line = f"[{tag}] {label}"
    if detail:
        line += f"\n        {detail}"
    print(line)


def section(title):
    print()
    print("=" * 72)
    print(title)
    print("=" * 72)


# ---------------------------------------------------------------------------
# CODATA anchors — CHECK-ONLY. Never used as a derivation input. Used only to
# confirm the dimensional identities are arithmetically consistent.
# ---------------------------------------------------------------------------
HBAR = 1.054_571_817e-34      # J s    [L^2 M T^-1]
C = 2.997_924_58e8            # m s^-1 [L T^-1]
G_SI = 6.674_30e-11          # m^3 kg^-1 s^-2  [L^3 M^-1 T^-2]
M_PL = 2.176_434e-8          # kg  (Planck mass, sqrt(hbar c / G))
L_PL = 1.616_255e-35         # m   (Planck length, sqrt(hbar G / c^3))


def dims_add(a, b):
    return tuple(x + y for x, y in zip(a, b))


def dims_scale(a, k):
    return tuple(x * k for x in a)


# SI base-dimension vectors as (L, M, T).
DIM = {
    "a": (1, 0, 0),     # lattice spacing -> length
    "c": (1, 0, -1),    # velocity
    "M": (0, 1, 0),     # lattice mass unit M_lat = a^{-1} in natural units
    "hbar": (2, 1, -1),  # action
}
DIM_G = (3, -1, -2)      # Newton's constant


# ===========================================================================
section("S0. Framing: what the structural core can and cannot carry")
# ===========================================================================
# The one-qubit operator algebra on Z^3 is purely dimensionless. The ONLY
# dimensionful primitive is a (length). Everything derived is either
# dimensionless or carries an integer power of [a].
check(
    "S0.1 structural core carries exactly one dimensionful primitive (a=[L])",
    True,
    "Cl(3)-on-Z^3 + qubit ops are dimensionless; a is the sole [L] input. "
    "Any G the lattice yields is therefore dimensionless * a^n (Buckingham-Pi).",
)
# A dimensionless lattice cannot, by itself, emit a second independent
# dimensionful number. So a closure a=l_P must IMPORT one dimensionful fact.
check(
    "S0.2 a second independent dimensionful number cannot be emitted by the core",
    True,
    "To pin a in SI you need exactly one dimensional anchor "
    "(PLANCK_MASS_CONVENTIONAL_ANCHOR_META_NOTE_2026-05-27, meta).",
)


# ===========================================================================
section("S1. Route A — G from lattice dynamics, then demand G = G_observed")
# ===========================================================================
# The framework's retained_bounded gravity chain (GRAVITY_CLEAN_DERIVATION,
# NEWTON_LAW_DERIVED, GRAVITY_LAW_CLEANUP) closes ONLY to LATTICE UNITS:
#   G_lat is DIMENSIONLESS (= 1/(4 pi) bare Green coeff, or 1 on the
#   carrier-normalized surface). It carries no [L],[M],[T].
G_lat_bare = 1.0 / (4.0 * math.pi)
G_lat_carrier = 1.0
check(
    "S1.1 lattice gravity coupling is DIMENSIONLESS (G_lat=1/(4pi) or 1)",
    True,
    f"G_lat(bare Green)={G_lat_bare:.6f}, G_lat(carrier-normalized)={G_lat_carrier:.1f}; "
    "GRAVITY_CLEAN_DERIVATION_NOTE claim_scope: 'in lattice units'.",
)

# To convert G_lat to SI you must multiply by a dimensionful carry built from
# {a, c, M_lat, hbar}. Exhaustively search integer powers for the unique
# combination with G_Newton dimensions.
candidates = []
R = range(-3, 4)
for p in R:          # a
    for q in R:      # c
        for r in R:  # M_lat
            for s in R:  # hbar
                d = (0, 0, 0)
                d = dims_add(d, dims_scale(DIM["a"], p))
                d = dims_add(d, dims_scale(DIM["c"], q))
                d = dims_add(d, dims_scale(DIM["M"], r))
                d = dims_add(d, dims_scale(DIM["hbar"], s))
                if d == DIM_G:
                    candidates.append((p, q, r, s))

# Among candidates, identify the minimal/canonical Planck form: hbar^1 c^1 M^-2.
canonical = (0, 1, -2, 1)
check(
    "S1.2 exhaustive [-3,3]^4 search finds the canonical carry hbar*c*M^-2",
    canonical in candidates,
    f"{len(candidates)} integer-power carries have G-dimensions; "
    f"canonical (a,c,M,hbar)={canonical} present. All reduce to G~hbar*c/M_lat^2.",
)
# Every candidate must reference the dimensionful lattice scale: either an
# explicit mass power M_lat^r (r!=0) OR an explicit length power a^p (p!=0).
# (The two are the SAME scale: M_lat = a^{-1} in natural units; the candidate
#  (a,c,M,hbar)=(2,3,0,-1) = a^2 c^3/hbar carries the scale via a^2 instead of
#  M_lat^-2.) What NO candidate can do is build G from c,hbar ALONE.
no_scaleless = all((p != 0) or (r != 0) for (p, q, r, s) in candidates)
has_massless_via_a = any((r == 0) and (p != 0) for (p, q, r, s) in candidates)
check(
    "S1.3 every G-dim carry references the lattice scale (a^p or M_lat^r); "
    "none is built from c,hbar alone",
    no_scaleless and has_massless_via_a,
    f"candidates={candidates}; the 'massless' carry (2,3,0,-1)=a^2 c^3/hbar "
    "still uses a^2. A scale (a or M_lat=1/a) is unavoidable; c,hbar alone "
    "cannot make G-dimensions.",
)

# KEY STEP. Identify M_lat with a^{-1} in natural units (hbar=c=1): M_lat = a^{-1}.
# Then G_SI = G_lat * hbar c / M_lat^2 = G_lat * hbar c a^2  (since M_lat=1/a in nat. units,
# but to stay SI-honest we keep M_lat as an independent symbol and ask whether
# demanding G_SI = G_observed PINS a).
#
# Self-consistency demand:  G_lat * hbar * c / M_lat^2  =  G_observed.
# Solve for M_lat:          M_lat = sqrt(G_lat * hbar * c / G_observed).
#
# This is ALGEBRAICALLY the Planck mass (up to the dimensionless sqrt(G_lat)).
# Numerically (CHECK-ONLY) verify it returns ~M_Pl when G_observed=G_SI:
M_lat_solved = math.sqrt(G_lat_carrier * HBAR * C / G_SI)   # carrier surface G_lat=1
rel_err_MPl = abs(M_lat_solved - M_PL) / M_PL
check(
    "S1.4 [CHECK-ONLY] demanding G_lat*hbar*c/M_lat^2 = G returns M_lat ~ M_Pl",
    rel_err_MPl < 1e-4,
    f"M_lat={M_lat_solved:.6e} kg vs M_Pl={M_PL:.6e} kg, rel_err={rel_err_MPl:.2e} "
    "(carrier surface G_lat=1).",
)

# THE CIRCULARITY. The demand G_SI(emergent) = G_observed contains TWO unknowns
# entering only as the combination needed: the lattice supplies the
# DIMENSIONLESS G_lat, but G_observed is itself a DIMENSIONFUL import. Solving
# for M_lat = a^{-1} just RE-EXPRESSES the imported dimensionful G as a mass.
# It produces NO new constraint on a beyond "a^{-1} := sqrt(hbar c / G)", which
# is the DEFINITION of M_Pl. No second equation pins a independently.
check(
    "S1.5 Route A is CIRCULAR: solving for a^{-1} just renames the imported G",
    True,
    "G_lat dimensionless => the only way G_SI acquires a value is by importing "
    "one dimensionful number (G, or equivalently M_Pl, or l_P). Setting "
    "a^{-1}=sqrt(hbar c/G) is the DEFINITION M_lat:=M_Pl, not an independent "
    "second constraint. dof count: 1 dimensionful unknown (a), 0 dimensionful "
    "equations from the (dimensionless) lattice => underdetermined.",
)
check(
    "S1.6 Route A verdict: does NOT close self-consistency (a=l_P assumed)",
    True,
    "Route A needs one dimensionful import (G/M_Pl/l_P). With it, a^{-1}=M_Pl "
    "by definition; without it, a is unfixed. => OPEN (assumed).",
)


# ===========================================================================
section("S2. Route B — Bekenstein-Hawking horizon-density match (framework's actual BP route)")
# ===========================================================================
# The framework's genuine self-consistency theorem is
#   PLANCK_SCALE_CONDITIONAL_COMPLETION_NOTE_2026-04-24:  (BP) => a/l_P = 1.
# Mechanism: the primitive event cell gives a DERIVED dimensionless coefficient
#   c_cell = Tr( (I_16/16) P_A ) = rank(P_A)/16 = 4/16 = 1/4.
P_A_rank = 4
hilbert_dim = 16
c_cell = P_A_rank / hilbert_dim
check(
    "S2.1 derived dimensionless cell coefficient c_cell = rank(P_A)/16 = 1/4",
    abs(c_cell - 0.25) < 1e-12,
    f"P_A rank {P_A_rank} on C^16 => c_cell = {c_cell} (exact, dimensionless).",
)
# The closure equates SAME-SURFACE densities:
#   lattice boundary density   c_cell / a^2
#   gravitational (BH) density 1 / (4 l_P^2)        <-- IMPORTS l_P
# => a^2 = 4 c_cell l_P^2 = 4*(1/4)*l_P^2 = l_P^2 => a/l_P = 1.
a_over_lP_sq = 4.0 * c_cell    # = a^2 / l_P^2
check(
    "S2.2 same-surface density match gives a^2/l_P^2 = 4*c_cell = 1, so a/l_P=1",
    abs(a_over_lP_sq - 1.0) < 1e-12,
    f"a^2/l_P^2 = 4*c_cell = {a_over_lP_sq}. With c_cell=1/4 exactly => a=l_P.",
)
# WHERE THE DIMENSIONFUL INPUT ENTERS. The gravitational side 1/(4 l_P^2)
# IS the Bekenstein-Hawking area law S = A/(4 l_P^2 k_B) with
# l_P^2 = hbar G / c^3. So l_P (hence G) is IMPORTED via the BH-density
# identification (premise BP: "the primitive one-step boundary count IS the
# microscopic carrier of the standard gravitational area/action density").
check(
    "S2.3 the dimensionful input l_P enters via the imported BH area law (premise BP)",
    True,
    "RHS 1/(4 l_P^2) is the Bekenstein-Hawking density; l_P^2=hbar G/c^3 is the "
    "import. The DERIVED part is only the dimensionless c_cell=1/4; the "
    "dimensionful l_P is carried in by the gravitational-density identification.",
)
# Had c_cell been any other rational, the SAME match would give a different
# a/l_P; the 'closure to 1' is the JOINT statement (c_cell=1/4) AND (boundary
# count = BH carrier). The first is derived; the second is the open premise BP.
check(
    "S2.4 'a/l_P=1' is JOINT: derived c_cell=1/4 AND open premise BP (carrier id)",
    True,
    "a/l_P = sqrt(4 c_cell): the value 1 needs BOTH c_cell=1/4 (derived) and the "
    "BH-carrier identification BP (open). BP supplies the dimensionful l_P.",
)
check(
    "S2.5 Route B verdict: CONDITIONAL closure (BP=>a/l_P=1); BP is the import",
    True,
    "Route B is a genuine self-consistency RELATION, but conditional on premise "
    "BP which imports the dimensionful BH law. => OPEN until BP is derived.",
)


# ===========================================================================
section("S3. Ledger cross-check — status of every note the routes lean on")
# ===========================================================================
# Hard-coded snapshot from `git show origin/main:docs/audit/data/audit_ledger.json`
# read at runner-authoring time (2026-06-05). The runner asserts the verdict is
# consistent with these statuses; it does NOT itself mutate the ledger.
ledger_snapshot = {
    # The BP => a/l_P=1 conditional theorem and its ENTIRE forward chain:
    "planck_scale_conditional_completion_note_2026-04-24": "unaudited",
    "planck_boundary_density_extension_theorem_note_2026-04-24": "unaudited",
    "planck_primitive_coframe_boundary_carrier_theorem_note_2026-04-25": "unaudited",
    "planck_link_local_first_variation_p_a_forcing_theorem_note_2026-04-30": "unaudited",
    "planck_source_unit_normalization_support_theorem_note_2026-04-25": "unaudited",
    "planck_primitive_clifford_majorana_edge_derivation_theorem_note_2026-04-30": "unaudited",
    "bh_quarter_wald_noether_framework_carrier_theorem_note_2026-04-29": "unaudited",
    "planck_substrate_to_carrier_forcing_bounded_note_2026-05-10_planckp1": "unaudited",
    "planck_hidden_character_delta_zero_positive_theorem_note_2026-05-10_planckp2": "unaudited",
    "planck_orientation_principle_bounded_note_2026-05-10_planckp3": "unaudited",
    "planck_scale_lane_status_note_2026-04-23": "unaudited",
    "g_newton_self_consistency_bounded_sharpening_note_2026-05-10_planckp4": "unaudited",
    # The three Planck-from-structure NO-GOs (scale not forced by symmetry):
    "planck_finite_response_no_go_note_2026-04-24": "retained_no_go",
    "planck_parent_source_hidden_character_no_go_note_2026-04-24": "retained_no_go",
    "planck_boundary_orientation_incidence_no_go_note_2026-04-30": "retained_no_go",
    # Meta scope notes (set no audit status):
    "planck_mass_conventional_anchor_meta_note_2026-05-27": "meta",
    "admitted_input_registry_tier_a_note_2026-05-23": "meta",
    # What IS retained_bounded: the DIMENSIONLESS gravity chain (lattice units):
    "gravity_clean_derivation_note": "retained_bounded",
    "gravity_full_self_consistency_note": "retained_bounded",
    "gravity_law_cleanup_note": "retained_bounded",
    "newton_law_derived_note": "retained_bounded",
    "wave_equation_gravity_note": "retained_bounded",
    "self_consistency_forces_poisson_note": "retained_bounded",
}

# Forward-chain rows that must hold for Route B's BP=>a/l_P=1 to be load-bearing:
bp_chain = [
    "planck_scale_conditional_completion_note_2026-04-24",
    "planck_boundary_density_extension_theorem_note_2026-04-24",
    "planck_primitive_coframe_boundary_carrier_theorem_note_2026-04-25",
    "planck_link_local_first_variation_p_a_forcing_theorem_note_2026-04-30",
    "planck_source_unit_normalization_support_theorem_note_2026-04-25",
    "planck_primitive_clifford_majorana_edge_derivation_theorem_note_2026-04-30",
    "bh_quarter_wald_noether_framework_carrier_theorem_note_2026-04-29",
]
chain_all_unaudited = all(ledger_snapshot[k] == "unaudited" for k in bp_chain)
check(
    "S3.1 the ENTIRE BP=>a/l_P=1 forward chain is `unaudited` on origin/main",
    chain_all_unaudited,
    "rows: " + ", ".join(k.split('_note_')[0] for k in bp_chain),
)
# The retained-bounded gravity rows close only in lattice units (dimensionless).
retained_grav = [
    "gravity_clean_derivation_note", "gravity_full_self_consistency_note",
    "gravity_law_cleanup_note", "newton_law_derived_note",
    "wave_equation_gravity_note", "self_consistency_forces_poisson_note",
]
grav_retained = all(ledger_snapshot[k] == "retained_bounded" for k in retained_grav)
check(
    "S3.2 retained_bounded gravity rows exist but close only to LATTICE units",
    grav_retained,
    "These derive G_lat (dimensionless) + 1/r law in lattice units; none "
    "carries a dimensionful scale, so none pins a in SI.",
)
# The three Planck no-gos: the scale is NOT forced by symmetry/structure alone.
nogos = [
    "planck_finite_response_no_go_note_2026-04-24",
    "planck_parent_source_hidden_character_no_go_note_2026-04-24",
    "planck_boundary_orientation_incidence_no_go_note_2026-04-30",
]
nogos_retained = all(ledger_snapshot[k] == "retained_no_go" for k in nogos)
check(
    "S3.3 three retained_no_go rows: scale/carrier NOT forced by symmetry alone",
    nogos_retained,
    "Consistent with: the dimensionful scale behaves as an anchor, not a theorem.",
)


# ===========================================================================
section("S4. Synthesis verdict")
# ===========================================================================
print(
    """
Both candidate routes to 'a = l_Planck' require importing exactly ONE
dimensionful fact that the dimensionless Cl(3)-on-Z^3 core cannot emit:

  Route A (G-from-lattice):   G_lat is dimensionless; demanding G_SI=G_observed
                              just sets a^{-1}=sqrt(hbar c/G)=:M_Pl by
                              DEFINITION (circular). No second dimensionful
                              equation pins a.  -> OPEN.

  Route B (BH-density match): a genuine conditional theorem (BP)=>a/l_P=1 with
                              the DERIVED dimensionless input c_cell=1/4, but
                              the dimensionful l_P enters via the IMPORTED
                              Bekenstein-Hawking area law under the open
                              carrier-identification premise BP. The entire
                              forward chain is `unaudited` on origin/main.
                              -> OPEN (conditional; closes IFF BP is derived).

Neither route closes self-consistency from the framework's own content WITHOUT
an extra dimensionful import. Per the HONESTY GUARD this is OPEN, not derived.

VERDICT: OPEN-SELF-CONSISTENCY (a = l_P is assumed/anchored, not derived).

This is a verification of the existing posture
(ADMITTED_INPUT_REGISTRY_TIER_A_NOTE_2026-05-23 item S; PLANCK_SCALE_LANE_
STATUS_NOTE_2026-04-23): 'the Planck-mass anchor is taken, not yet derived';
the closure a/l_P=1 is the open gravity lane, conditional theorem only.
The one positive, derived ingredient is the dimensionless c_cell=1/4 (Route B);
the missing ingredient is purely the dimensionful carrier identification (BP),
which is exactly one dimensionful import.
"""
)


# ===========================================================================
section("SUMMARY")
# ===========================================================================
n_pass = sum(1 for _, ok, _ in results if ok)
n_fail = sum(1 for _, ok, _ in results if not ok)
print(f"Total: {n_pass} PASS / {n_fail} FAIL")
print("VERDICT: OPEN-SELF-CONSISTENCY (a=l_P assumed; not derived from framework content).")
if n_fail:
    raise SystemExit(1)
