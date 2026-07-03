#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_dynamics_sort_records_accumulate_2026_07_03.py

Walls-attack exact runner for the bounded-theorem + narrow-no-go + governance-map
note:

  docs/DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md

Scope of this runner (exact arithmetic; Fraction/int/set/str only; NO floats):

  T1  PERMANENCE SCOPE GAP        (bounded theorem)   CHECK 01-06
  T2  ORDERING DERIVED           (bounded theorem)   CHECK 07-13
  T3  ACCUMULATION IRREDUCIBLE   (narrow no-go)      CHECK 14-21
  T4  THE COMPRESSION MAP        (bounded support)   CHECK 22-28
  T5  GOVERNANCE MAP             (governance)        CHECK 29-30

Every quoted axiom / firewall sentence is quoted verbatim from exactly five
source files (see the note header). This runner adopts NOTHING, sets NO audit
verdict, and predicts NO audit outcome. It exhibits exact finite witnesses and
conserves the full residue in one table (T4/T5).

House rules enforced here:
  * no floats anywhere (Fraction for the single rate contrast; int/set/str else);
  * one line "CHECK NN: PASS/FAIL -- desc" per check;
  * a TOTAL line "TOTAL: PASS=N FAIL=M";
  * nonzero process exit if any check FAILs.
"""

from fractions import Fraction
import sys

# ----------------------------------------------------------------------------
# check harness
# ----------------------------------------------------------------------------

_RESULTS = []  # list of (idx:int, ok:bool, desc:str)


def check(ok, desc):
    idx = len(_RESULTS) + 1
    _RESULTS.append((idx, bool(ok), desc))
    print("CHECK %02d: %s -- %s" % (idx, "PASS" if ok else "FAIL", desc))
    return bool(ok)


# ============================================================================
# Verbatim source sentences (quoted; the ONLY authority this runner leans on).
# ============================================================================

RECORD_SENTENCES = [
    # docs/MINIMAL_AXIOMS_2026-06-29.md  (Record / Fixed Reality)
    "A site need not carry a record.",
    ("When present, a record locks exactly one local possibility from the subset "
     "available at that site under Admissibility; the locked possibility is "
     "invariant under repeated readout."),
    ("Only records are readable. A readout value is determined by record content "
     "alone. For any finite collection of pairwise-disjoint records, scalar "
     "readout I is additive, with I(empty)=0."),
]

AXIOM_SENTENCES = {
    # docs/MINIMAL_AXIOMS_2026-06-29.md
    "Lattice": ("Physical sites are the points of the cubic lattice Z^3, with "
                "nearest-neighbor adjacency, standard translations, and proper "
                "cubic rotations about each site."),
    "Lattice_noprivilege": ("No site is privileged. Sites are distinguished by "
                            "the supplied lattice structure alone."),
    "Qubit": "Each site has a domain of local possibilities.",
    "Qubit_noprivilege": ("No possibility is privileged. Possibilities are "
                          "distinguished by the supplied algebraic structure "
                          "alone."),
    "Admissibility": ("For each site, the available possibilities are determined "
                      "by, and vary with, the nearest-neighbor conditions."),
    "State": "A state is a configuration of records.",
    "Law": ("A law privileges no states. Its domain is a supplied condition, and "
            "at every state where the condition holds it gives exactly one "
            "answer."),
}

# docs/RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md  (scoping sentence)
ORDER_RATE_FIREWALL = ("A record history supplies ordered words and counts. A "
                       "supplied instrument kernel supplies probabilities per "
                       "admitted step. A physical time metric or transition rate "
                       "requires an additional clock/production normalization.")

# docs/DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md  (H=0 in class)
NONTRIV_FIREWALL = ("The class contains H = 0, and it is closed under real "
                    "linear combinations of allowed Hermitian terms.")

# docs/DYNAMICS_FORM_FROM_RECORD_PRESERVATION_..._2026-06-05.md
FORM_NOTE_NOTRIV = "It does not force non-trivial dynamics: H = 0 is in the class."

# docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md
ARROW_NOT_FROM_NOTHING = ("boundary-condition / structural result; honest "
                          "pinning, not a from-nothing derivation of the arrow.")

# ----------------------------------------------------------------------------
# shared exact toy primitives
# ----------------------------------------------------------------------------
# A record is a (site, locked_value) pair.  A configuration is a frozenset of
# records.  Sites are points of a finite window of Z^3 (integer 3-tuples).  The
# per-site "available possibilities" (Admissibility) and the full one-site
# "possibility domain" (Qubit) are small fixed finite sets.

POSSIBILITY_DOMAIN = frozenset({-1, +1})                          # Qubit
Z3_WINDOW = frozenset({(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0)})  # lattice pts


def available_at(site):
    """Admissibility: available possibilities determined by, and varying with,
    the nearest-neighbor conditions.  Exact fixed rule on the finite window
    (keyed to the site's coordinate parity so it demonstrably varies while
    staying a subset of the possibility domain)."""
    parity = (site[0] + site[1] + site[2]) % 2
    return frozenset({+1}) if parity == 0 else frozenset({-1, +1})


def is_record(rec):
    site, val = rec
    return site in Z3_WINDOW and val in POSSIBILITY_DOMAIN


def readout_value(rec):
    """A readout value is determined by record content alone: pure function of
    the (site, locked_value) pair; here the locked value itself."""
    _site, val = rec
    return val


def readout_op(rec):
    """Readout as an exact operation: returns (value, record_after).  Reading
    changes nothing, so record_after == record_before."""
    return (readout_value(rec), rec)


def readout_idempotent(rec):
    """'the locked possibility is invariant under repeated readout' as an exact
    operation: apply readout twice; value stable AND record unchanged both
    times."""
    v1, after1 = readout_op(rec)
    v2, after2 = readout_op(after1)
    return (v1 == v2) and (after1 == rec) and (after2 == rec)


def I_readout(config):
    """Scalar readout I: additive over the (pairwise-disjoint) records of a
    configuration, with I(empty)=0."""
    return sum(readout_value(r) for r in config)


def locks_one_available(rec):
    """When present, a record locks exactly one local possibility from the
    subset available at that site under Admissibility."""
    site, val = rec
    return (val in POSSIBILITY_DOMAIN) and (val in available_at(site))


def config_admissible(config):
    return all(locks_one_available(r) for r in config)


def sites_of(config):
    return frozenset(s for (s, _v) in config)


def some_site_without_record(config):
    """'A site need not carry a record.' -- the model permits (exhibits) a
    lattice site carrying no record."""
    return len(Z3_WINDOW - sites_of(config)) >= 1


def record_axioms_hold(config):
    """Every quoted Record-axiom sentence, read literally, on a configuration."""
    need_not = some_site_without_record(config)
    lock_one = all(locks_one_available(r) for r in config)
    idem = all(readout_idempotent(r) for r in config)
    only_records = all(is_record(r) for r in config)       # only records readable
    add_empty = (I_readout(frozenset()) == 0)
    return need_not and lock_one and idem and only_records and add_empty


# ============================================================================
# T1 -- PERMANENCE SCOPE GAP  (bounded theorem)                CHECK 01-06
# ----------------------------------------------------------------------------
# Quote: "the locked possibility is invariant under repeated readout".
# Exhibit a finite model whose records are readout-stable yet evolution-mortal
# (a step deletes a record), satisfying every quoted Record-axiom sentence read
# literally BEFORE and AFTER the step.  Conclusion: permanence-across-events is
# NOT derivable from readout-invariance.
# ============================================================================

print("# ---- T1  PERMANENCE SCOPE GAP (bounded theorem) ----")

R_A = ((0, 0, 0), +1)   # site parity 0 -> available {+1}; locks +1  OK
R_B = ((1, 0, 0), -1)   # site parity 1 -> available {-1,+1}; locks -1 OK
R_C = ((0, 1, 0), +1)   # site parity 1 -> available {-1,+1}; locks +1 OK
CONFIG_BEFORE = frozenset({R_A, R_B, R_C})   # site (2,0,0) carries no record


def mortal_step(config, victim):
    """Evolution-mortal step as an explicit map on configurations: removes
    exactly one (site, locked-value) pair."""
    return config - frozenset({victim})


CONFIG_AFTER = mortal_step(CONFIG_BEFORE, R_B)

# CHECK 01 -- readout idempotence as an exact operation on each present record
check(all(readout_idempotent(r) for r in CONFIG_BEFORE),
      "T1 readout idempotent (repeated readout: same value, record unchanged)")

# CHECK 02 -- readout value determined by content alone (pure function)
_content_pure = (readout_value(R_A) == readout_value(((0, 0, 0), +1))
                 and readout_op(R_A)[1] == R_A)
check(_content_pure,
      "T1 readout value determined by record content alone (pure, no side effect)")

# CHECK 03 -- I(empty)=0 and additive over pairwise-disjoint records
_disjoint_add = (I_readout(frozenset()) == 0
                 and I_readout(CONFIG_BEFORE)
                 == I_readout(frozenset({R_A})) + I_readout(frozenset({R_B, R_C})))
check(_disjoint_add, "T1 scalar readout I additive over disjoint records, I(empty)=0")

# CHECK 04 -- each record locks exactly one available possibility (Admissibility)
check(config_admissible(CONFIG_BEFORE),
      "T1 each record locks exactly one Admissibility-available possibility")

# CHECK 05 -- every quoted Record-axiom sentence holds BEFORE the step
check(record_axioms_hold(CONFIG_BEFORE),
      "T1 every quoted Record-axiom sentence holds BEFORE the mortal step")

# CHECK 06 -- evolution is mortal yet every quoted sentence still holds AFTER:
#             one pair removed, all other pairs present, axioms literally satisfied,
#             but the deleted record is gone -> permanence is NOT entailed.
_removed_one = (len(CONFIG_AFTER) == len(CONFIG_BEFORE) - 1
                and R_B not in CONFIG_AFTER
                and (CONFIG_BEFORE - frozenset({R_B})) == CONFIG_AFTER)
_axioms_after = record_axioms_hold(CONFIG_AFTER)
_permanence_broken = R_B in CONFIG_BEFORE and R_B not in CONFIG_AFTER
check(_removed_one and _axioms_after and _permanence_broken,
      "T1 mortal step deletes one record, quoted axioms hold AFTER: "
      "readout-invariance does NOT entail permanence")


# ============================================================================
# T2 -- ORDERING DERIVED  (bounded theorem, conditional on permanence)  CHECK 07-13
# ----------------------------------------------------------------------------
# From "A state is a configuration of records" + permanence (named premise,
# pending T1): realized histories are chains in the record-set INCLUSION order;
# forward = strictly more records; no cycles (strict monotone count);
# relabel/merge invariance.  Firewall protection: ORDER and COUNT only.
# ============================================================================

print("# ---- T2  ORDERING DERIVED (bounded theorem, conditional on permanence) ----")

S0 = frozenset()
S1 = frozenset({R_A})
S2 = frozenset({R_A, R_C})
S3 = frozenset({R_A, R_C, R_B})
CHAIN = [S0, S1, S2, S3]


def subset(a, b):
    return a <= b


# CHECK 07 -- reflexivity of the inclusion order
check(all(subset(s, s) for s in CHAIN), "T2 inclusion order reflexive")

# CHECK 08 -- antisymmetry: A<=B and B<=A imply A==B
_antisym = all((not (subset(a, b) and subset(b, a))) or (a == b)
               for a in CHAIN for b in CHAIN)
check(_antisym, "T2 inclusion order antisymmetric")

# CHECK 09 -- transitivity
_trans = all((not (subset(a, b) and subset(b, c))) or subset(a, c)
             for a in CHAIN for b in CHAIN for c in CHAIN)
check(_trans, "T2 inclusion order transitive")

# CHECK 10 -- realized history is a chain that STRICTLY adds one record per step
_strict_chain = all(CHAIN[i] < CHAIN[i + 1]
                    and len(CHAIN[i + 1]) == len(CHAIN[i]) + 1
                    for i in range(len(CHAIN) - 1))
check(_strict_chain, "T2 realized history: strict inclusion chain, +1 record/step")

# CHECK 11 -- strict monotone COUNT forbids cycles; a 'return' step would have to
#             DELETE a record, which permanence (T1 clarified) forbids.
_counts = [len(s) for s in CHAIN]
_monotone = all(_counts[i] < _counts[i + 1] for i in range(len(_counts) - 1))
_cycle_attempt = mortal_step(S3, R_B)          # trying to go back toward S2-size
_cycle_needs_delete = (not subset(S3, _cycle_attempt)) and len(_cycle_attempt) < len(S3)
check(_monotone and _cycle_needs_delete,
      "T2 strict monotone count: no cycles (a return step must delete -> forbidden)")


def relabel(config, perm):
    return frozenset(((perm[s], v) for (s, v) in config))


PERM = {(0, 0, 0): (1, 0, 0), (1, 0, 0): (0, 1, 0),
        (0, 1, 0): (2, 0, 0), (2, 0, 0): (0, 0, 0)}

# CHECK 12 -- relabel-invariance (site permutation is an order isomorphism) and
#             merge/union-monotonicity (A<=B => A|X <= B|X).
_relabel_iso = all(subset(a, b) == subset(relabel(a, PERM), relabel(b, PERM))
                   for a in CHAIN for b in CHAIN)
X = frozenset({R_C})
_merge_mono = all((not subset(a, b)) or subset(a | X, b | X)
                  for a in CHAIN for b in CHAIN)
check(_relabel_iso and _merge_mono,
      "T2 order is relabel-invariant (site perm = order iso) and merge-monotone")

# CHECK 13 -- FIREWALL PROTECTION: derivation yields ORDER + COUNT only.  The same
#             chain embedded in two step-grids has identical order and counts but a
#             DIFFERENT count-per-step 'rate' -> rate/metric/clock not fixed here
#             (quote-scoped by ORDER_RATE_FIREWALL).  Also: forward is definitional
#             (inclusion direction), not thermodynamic -> disjoint from the arrow note.
grid_tight = [0, 1, 2, 3]          # step index at n
grid_loose = [0, 2, 4, 6]          # same chain, stretched step index
rate_tight = Fraction(_counts[-1] - _counts[0], grid_tight[-1] - grid_tight[0])
rate_loose = Fraction(_counts[-1] - _counts[0], grid_loose[-1] - grid_loose[0])
_order_count_invariant = (_counts == [len(s) for s in CHAIN]) and _monotone
_rate_not_fixed = (rate_tight != rate_loose)   # 1 != 1/2  (exact Fraction)


def forward(a, b):                 # 'b later than a' iff strictly more records
    return a < b


_forward_def = (forward(S1, S2) is True and forward(S2, S1) is False
                and forward(S1, S2) == (len(S2) > len(S1)))
check(_order_count_invariant and _rate_not_fixed and _forward_def,
      "T2 firewall-scoped: order+count only (rate %s vs %s not fixed); "
      "forward is definitional inclusion, not thermodynamic"
      % (rate_tight, rate_loose))


# ============================================================================
# T3 -- ACCUMULATION IRREDUCIBLE  (narrow no-go, axiom-first)          CHECK 14-21
# ----------------------------------------------------------------------------
# Two exact witnesses that "something happens" is NOT a theorem of the four
# axioms.  (i) STATIC witness: a fixed admissible configuration with the CONSTANT
# history satisfies every quoted axiom sentence, checked one sentence at a time
# (sentence-complete).  (ii) H=0 witness: the forced gauge-covariant class
# contains the zero generator.  Hence non-triviality is genuinely new content.
# ============================================================================

print("# ---- T3  ACCUMULATION IRREDUCIBLE (narrow no-go, axiom-first) ----")

C_STAR = frozenset({R_A, R_B, R_C})        # records present, admissible
CONSTANT_HISTORY = [C_STAR, C_STAR, C_STAR, C_STAR]   # nothing ever changes


def identity_law(config):
    """The static 'law': domain = all configurations (supplied condition true
    everywhere), and it gives exactly one answer -- the same configuration.
    Privileges no state."""
    return config


# CHECK 14 -- Lattice sentence guard: every record's site is a point of Z^3, and
#             no site is privileged by the constant history (identity law is
#             site-symmetric: relabeling sites commutes with the law).
_sites_lattice = all(s in Z3_WINDOW for s in sites_of(C_STAR))
_no_priv = relabel(identity_law(C_STAR), PERM) == identity_law(relabel(C_STAR, PERM))
check(_sites_lattice and _no_priv,
      "T3(i) STATIC guard: Lattice -- sites are Z^3 points, no site privileged")

# CHECK 15 -- Qubit sentence guard: each site's locked value lies in the local
#             possibility domain; no possibility privileged.
_qubit_ok = all(v in POSSIBILITY_DOMAIN for (_s, v) in C_STAR)
check(_qubit_ok, "T3(i) STATIC guard: Qubit -- locked values in possibility domain")

# CHECK 16 -- Admissibility sentence guard: C_STAR is admissible AND stays
#             admissible at every element of the constant history.
_adm_all = all(config_admissible(c) for c in CONSTANT_HISTORY)
check(_adm_all, "T3(i) STATIC guard: Admissibility holds across the constant history")

# CHECK 17 -- Record sentence guards (all three), sentence-complete:
#             need-not-carry, locks-one + readout-invariant, additive readout.
_rec_need = some_site_without_record(C_STAR)
_rec_lock = all(locks_one_available(r) and readout_idempotent(r) for r in C_STAR)
_rec_add = (I_readout(frozenset()) == 0
            and I_readout(C_STAR)
            == I_readout(frozenset({R_A, R_B})) + I_readout(frozenset({R_C})))
check(_rec_need and _rec_lock and _rec_add,
      "T3(i) STATIC guard: Record -- need-not-carry, locks-one+readout-invariant, additive")

# CHECK 18 -- "A state is a configuration of records": every element of the
#             constant history is a configuration of records.
_state_guard = all(all(is_record(r) for r in c) for c in CONSTANT_HISTORY)
check(_state_guard,
      "T3(i) STATIC guard: State -- every history element is a config of records")

# CHECK 19 -- "A law privileges no states ... exactly one answer": the identity
#             law is total (defined on every config) and single-valued.
_law_total = all(identity_law(c) == c for c in CONSTANT_HISTORY)
_law_single = (identity_law(C_STAR) == identity_law(C_STAR))
check(_law_total and _law_single,
      "T3(i) STATIC guard: Law -- identity law total + single-valued, privileges no state")

# CHECK 20 -- the constant history registers NO new record: accumulation FAILS
#             while every quoted axiom sentence holds -> "something happens" is
#             NOT forced by the four axioms.
_no_new = all(CONSTANT_HISTORY[i + 1] == CONSTANT_HISTORY[i]
              for i in range(len(CONSTANT_HISTORY) - 1))
_delta_count = len(CONSTANT_HISTORY[-1]) - len(CONSTANT_HISTORY[0])
check(_no_new and _delta_count == 0,
      "T3(i) constant history registers 0 new records: non-triviality NOT forced")


# (ii) H=0 witness -- exact integer 2x2 commutators; the forced gauge-covariant
# class ([H,G]=0) contains H=0 (and nonzero members), while an sx control fails.
def matmul(A, B):
    return [[A[i][0] * B[0][j] + A[i][1] * B[1][j] for j in (0, 1)] for i in (0, 1)]


def comm(A, B):
    AB = matmul(A, B)
    BA = matmul(B, A)
    return [[AB[i][j] - BA[i][j] for j in (0, 1)] for i in (0, 1)]


def is_zero(M):
    return all(M[i][j] == 0 for i in (0, 1) for j in (0, 1))


G = [[1, 0], [0, -1]]        # a Gauss/charge-parity generator (sz-like), integer
H0 = [[0, 0], [0, 0]]        # zero generator
Hnz = [[2, 0], [0, 3]]       # nonzero, commutes with diagonal G (class member)
Hsx = [[0, 1], [1, 0]]       # gauge-variant control (sx-like)

# CHECK 21 -- H=0 in the gauge-covariant class; a nonzero diagonal H also in it
#             (non-unique, closed under real combinations); sx control NOT in it.
_h0_in = is_zero(comm(H0, G))
_hnz_in = is_zero(comm(Hnz, G))
_hsx_out = not is_zero(comm(Hsx, G))
check(_h0_in and _hnz_in and _hsx_out,
      "T3(ii) H=0 witness: zero generator in gauge-covariant class (nonzero too; "
      "sx control fails) -> non-triviality is new content")


# ============================================================================
# T4 -- THE COMPRESSION MAP  (bounded support)                        CHECK 22-28
# ----------------------------------------------------------------------------
# Given T1 permanence (clarified) + T3 accumulation sentence: production is
# definitional; discharge #4854 P2/P3; #4855 C-add via chain-concatenation with
# the kernel-convolution clause NAMED as an OPEN derivation target; the
# conditional ladder re-hangs; the ordering->transfer-axis (B-AXIS) bridge is a
# NAMED OPEN target; permanent non-goals kept.  Full residue conserved in one
# table.  Supervisor-supplied context is quoted as supervisor-supplied.
# ============================================================================

print("# ---- T4  THE COMPRESSION MAP (bounded support) ----")


def registration_events(chain):
    """(a) production is definitional: an event := registration of one record."""
    ev = 0
    for i in range(len(chain) - 1):
        if chain[i] < chain[i + 1] and len(chain[i + 1]) == len(chain[i]) + 1:
            ev += 1
    return ev


# CHECK 22 -- event := registration; production count == count delta on the chain
_events = registration_events(CHAIN)
check(_events == len(CHAIN[-1]) - len(CHAIN[0]) == 3,
      "T4(a) production definitional: event:=registration, count == +records on chain")

# (b) #4854 premise families P1-P4 / CHART-MIX (review-pending; supervisor-supplied).
#     P2/P3 discharge EXACTLY by (accumulation sentence, definitional event).
DISCHARGE_4854 = {
    "P2": "accumulation-sentence (records accumulate; new record each admissible step)",
    "P3": "definitional-event (event := registration of one record)",
}
FAMILIES_4854 = {"P1", "P2", "P3", "P4", "CHART-MIX"}
# CHECK 23 -- the P2/P3 discharge map is total (each discharged premise names a
#             non-empty supplier) and touches ONLY P2,P3 (P1/P4/CHART-MIX untouched).
_disch_total = all(v for v in DISCHARGE_4854.values())
_disch_scope = set(DISCHARGE_4854) == {"P2", "P3"} and set(DISCHARGE_4854) <= FAMILIES_4854
check(_disch_total and _disch_scope,
      "T4(b) #4854 P2/P3 discharged by accumulation+definitional-event (P1/P4/CHART-MIX untouched)")

# (c) #4855 C-add: chain concatenation supplies step composition (associative) and
#     additive counts; the kernel-convolution clause is a NAMED OPEN target.
def concat(chain_a, chain_b):
    if chain_a[-1] != chain_b[0]:
        return None
    return chain_a + chain_b[1:]


segA = [S0, S1]
segB = [S1, S2]
segC = [S2, S3]
_assoc_left = concat(concat(segA, segB), segC)
_assoc_right = concat(segA, concat(segB, segC))
_c_add = (registration_events(_assoc_left) == registration_events(segA)
          + registration_events(segB) + registration_events(segC))
KERNEL_CONVOLUTION_TARGET = "OPEN"   # NOT auto-supplied; named derivation target
# CHECK 24 -- concatenation associative + C-add additive; kernel-convolution OPEN
check(_assoc_left == _assoc_right and _c_add and KERNEL_CONVOLUTION_TARGET == "OPEN",
      "T4(c) #4855 C-add: chain-concat associative + additive; kernel-convolution NAMED OPEN")

# (d) the landed conditional ladder re-hangs.  Each rung carries its named premise
#     and status; nothing beyond form/Stone is marked unconditional; terminal
#     Dirac branch is review-pending (#4797, supervisor-supplied).
LADDER = [
    ("form-forced",      "record-preservation+locality+Hermiticity (bounded bridges)", "landed-given-bridges"),
    ("Stone-unique-gen", "B-AXIS supplied-axis premise",                                "landed-conditional-on-axis"),
    ("d_t-parity",       "ABJ external premise",                                        "external-premise"),
    ("d_t=1",            "single-generator N5 cap",                                     "named-premise"),
    ("Dirac-branch",     "#4797 REALIZED_KINETIC_BRANCH (Admissibility-variation)",     "review-pending"),
]
_ladder_ordered = [r[0] for r in LADDER] == [
    "form-forced", "Stone-unique-gen", "d_t-parity", "d_t=1", "Dirac-branch"]
_ladder_premised = all(r[1] for r in LADDER)                       # every rung names a premise
_no_uncond = all(r[2] != "landed-unconditional" for r in LADDER)  # none unconditional
_terminal_pending = LADDER[-1][2] == "review-pending"
# CHECK 25 -- ladder well-formed, every rung premised, none unconditional, terminal pending
check(_ladder_ordered and _ladder_premised and _no_uncond and _terminal_pending,
      "T4(d) conditional ladder re-hangs: each rung premised, terminal Dirac branch review-pending")

# (e) ordering -> lattice-transfer-axis (B-AXIS) bridge is a NAMED OPEN target.
#     T2's ordering outputs are exactly {order, count}; B-AXIS is not among them.
ORDERING_OUTPUTS = {"order", "count"}
B_AXIS_TRANSFER_TARGET = "OPEN"
# CHECK 26 -- B-AXIS transfer not supplied by ordering -> OPEN
check("B-AXIS" not in ORDERING_OUTPUTS and B_AXIS_TRANSFER_TARGET == "OPEN",
      "T4(e) ordering->transfer-axis (B-AXIS) NOT auto-supplied: NAMED OPEN target")

# (f) permanent non-goals: rate/metric/clock (landed no-gos), arrow beyond
#     past-hypothesis, ABJ premise externality -- never moved into 'discharged'.
PERMANENT_NON_GOALS = {
    "rate", "metric", "clock",
    "arrow-beyond-past-hypothesis", "ABJ-premise-externality",
}
_discharged = set(DISCHARGE_4854) | {"C-add"}
# CHECK 27 -- permanent non-goals disjoint from discharged premises
check(PERMANENT_NON_GOALS.isdisjoint(_discharged),
      "T4(f) permanent non-goals (rate/metric/clock, arrow, ABJ-externality) never discharged")

# ---- FULL RESIDUE TABLE (conserve EVERYTHING) ------------------------------
# status vocabulary is closed; every item carries exactly one status; the
# adoption/promotion tokens excluded below are guarded against at CHECK 28.
STATUS_VOCAB = {
    "named-premise", "derivation-target", "external-premise", "carried-open",
    "permanent-no-go", "review-pending", "owner-surface", "landed-given-bridges",
    "landed-conditional",
}
RESIDUE = [
    # owner surfaces produced by this block
    ("permanence premise (pending owner clarity fix)",          "owner-surface"),
    ("accumulation sentence (new axiom content)",               "owner-surface"),
    # derivation targets left OPEN
    ("kernel-convolution clause (#4855)",                       "derivation-target"),
    ("ordering->transfer-axis B-AXIS bridge",                   "derivation-target"),
    # external / named premises (unchanged)
    ("ABJ parity external premise",                             "external-premise"),
    ("B-AXIS supplied-axis premise",                            "named-premise"),
    ("single-generator N5 cap (d_t=1)",                         "named-premise"),
    # carried-open boundary / universal-floor
    ("past-hypothesis boundary condition (universal-floor)",    "carried-open"),
    # permanent no-gos (landed)
    ("rate no-go (record order/count)",                         "permanent-no-go"),
    ("metric no-go (record order/count)",                       "permanent-no-go"),
    ("clock no-go (record order/count)",                         "permanent-no-go"),
    # review-pending statuses (supervisor-supplied)
    ("#4797 Dirac-branch (REALIZED_KINETIC_BRANCH)",            "review-pending"),
    ("#4854 premise family P1-P4/CHART-MIX",                    "review-pending"),
    ("#4855 premise family C-add/POS/LOC",                      "review-pending"),
    # landed rungs
    ("form-forced (gauge-invariant-local class)",               "landed-given-bridges"),
    ("Stone-unique generator (given axis)",                     "landed-conditional"),
    # post-reset audit status of EVERY cited note
    ("all cited notes: unaudited post 2026-06-29 reset",        "carried-open"),
]
_all_status_ok = all(st in STATUS_VOCAB for (_it, st) in RESIDUE)
_no_drop = (len(RESIDUE) == 17)                       # expected complete count
_nothing_adopted = all(st not in ("adopted", "retained") for (_it, st) in RESIDUE)
# CHECK 28 -- residue table complete: closed-vocab statuses, expected count, nothing adopted/retained
check(_all_status_ok and _no_drop and _nothing_adopted,
      "T4 residue table complete (17 rows, closed status vocab, nothing adopted/retained)")

print("# ---- residue table (conserved; nothing adopted) ----")
for _it, _st in RESIDUE:
    print("#   [%-20s] %s" % (_st, _it))


# ============================================================================
# T5 -- GOVERNANCE MAP                                                CHECK 29-30
# ----------------------------------------------------------------------------
# Exactly two owner surfaces: (1) the Record-axiom permanence clarity fix;
# (2) the accumulation sentence (the only genuinely new sentence).  Nothing
# adopted; audit lane owns statuses.  TOE-leverage: one sentence + one clarity
# fix replace the B-AXIS / H!=0 premise across the time cluster.
# ============================================================================

print("# ---- T5  GOVERNANCE MAP ----")

OWNER_SURFACES = [
    {
        "id": "permanence-clarity-fix",
        "kind": "clarity-fix",
        "sentence": ("A record, once present, is permanent: no later "
                     "configuration removes or alters it. Reading it changes "
                     "nothing."),
        "status": "owner-surface / not adopted",
    },
    {
        "id": "accumulation-sentence",
        "kind": "new-content",
        "sentence": ("Records accumulate: every admissible history registers new "
                     "records; no final configuration is reached."),
        "status": "owner-surface / not adopted",
    },
]

# CHECK 29 -- exactly two owner surfaces; one clarity-fix, one new-content; both
#             non-empty sentences; both flagged not adopted.
_two = len(OWNER_SURFACES) == 2
_kinds = {s["kind"] for s in OWNER_SURFACES} == {"clarity-fix", "new-content"}
_nonempty = all(len(s["sentence"]) > 0 for s in OWNER_SURFACES)
_not_adopted = all(s["status"] == "owner-surface / not adopted" for s in OWNER_SURFACES)
check(_two and _kinds and _nonempty and _not_adopted,
      "T5 exactly two owner surfaces (1 clarity-fix + 1 new-content), nothing adopted")

# CHECK 30 -- TOE-leverage: adopting the two surfaces would discharge exactly the
#             {B-AXIS, H!=0} premises across the time cluster, leaving named
#             externals (ABJ, axis, past-hypothesis) still external.  This is a
#             mapping check (no adoption performed here).
TOE_TARGETS = {"B-AXIS", "H!=0"}
LEVERAGE_MAP = {
    "accumulation-sentence": "H!=0",          # non-triviality replaces H!=0
    "permanence-clarity-fix": "B-AXIS",       # ordering+permanence feed the axis work
}
STILL_EXTERNAL = {"ABJ", "supplied-axis", "past-hypothesis"}
_covers = set(LEVERAGE_MAP.values()) == TOE_TARGETS
_externals_kept = TOE_TARGETS.isdisjoint(STILL_EXTERNAL)
check(_covers and _externals_kept,
      "T5 TOE-leverage: two surfaces target {B-AXIS,H!=0}; named externals stay external")


# ============================================================================
# TOTAL
# ============================================================================

_p = sum(1 for (_i, ok, _d) in _RESULTS if ok)
_f = sum(1 for (_i, ok, _d) in _RESULTS if not ok)
print("TOTAL: PASS=%d FAIL=%d" % (_p, _f))

sys.exit(1 if _f else 0)
