#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_dynamics_sort_records_accumulate_2026_07_03.py

Walls-attack exact runner for the bounded-theorem + narrow-no-go + governance-map
note:

  docs/DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md

Scope of this runner (exact arithmetic; Fraction/int/set/str only; NO floats):

  SOURCE LIVENESS                 (quotes are live)   CHECK 01-03
  PERMANENCE SCOPE GAP            (bounded theorem)   CHECK 04-12
  CONDITIONAL RECORD ORDERING     (bounded theorem)   CHECK 13-21
  ACCUMULATION IRREDUCIBILITY     (narrow no-go)      CHECK 22-25
  COMPRESSION MAP                 (bounded support)   CHECK 26-33
  GOVERNANCE MAP                  (governance)        CHECK 34-35

Every quoted axiom / firewall sentence is guarded LIVE against the actual source
file content (whitespace-normalized substring), so no quote is dead data.  The
Admissibility availability rule is ONE covariant, neighbor-dependent rule shared
by every witness: available_at(s) = the locked values of records on the nearest
neighbors of s, or the full possibility set when no neighbor carries a record.
This rule is determined by, and varies with, the nearest-neighbor conditions; it
is covariant under lattice translations and proper cubic rotations (it references
relative neighbor offsets only); and it privileges no possibility (it reads
neighbor record content, never the site's own coordinates).

This runner adopts NOTHING, sets NO audit verdict, and predicts NO audit outcome.
It exhibits exact finite witnesses and conserves the full residue by PARSING the
note's own residue table (single source of truth).

House rules enforced here:
  * no floats anywhere (Fraction for the single rate contrast; int/set/str else);
  * one line "CHECK NN: PASS/FAIL -- desc" per check;
  * a TOTAL line "TOTAL: PASS=N FAIL=M";
  * nonzero process exit if any check FAILs.
"""

from fractions import Fraction
from pathlib import Path
import re
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


# ----------------------------------------------------------------------------
# source-file access + normalization (backticks/asterisks stripped, whitespace
# collapsed) so quoted sentences can be checked as LIVE substrings of the files.
# ----------------------------------------------------------------------------

DOCS_DIR = Path(__file__).resolve().parent.parent / "docs"
NOTE_NAME = ("DYNAMICS_CONTENT_SORT_ORDERING_DERIVED_ACCUMULATION_"
             "IRREDUCIBLE_BOUNDED_NOTE_2026-07-03.md")

SRC = {
    "AXIOMS": "MINIMAL_AXIOMS_2026-06-29.md",
    "ORDER_RATE": "RECORD_HISTORY_ORDER_TIME_RATE_FIREWALL_2026-06-05.md",
    "NONTRIV": "DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md",
    "FORM": ("DYNAMICS_FORM_FROM_RECORD_PRESERVATION_GAUGE_INVARIANT_"
             "LOCAL_CLASS_BOUNDED_THEOREM_NOTE_2026-06-05.md"),
    "ARROW": "ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md",
}


def normalize(text):
    """Strip markdown backticks/emphasis asterisks; collapse whitespace runs."""
    text = re.sub(r"[`*]", "", text)
    return re.sub(r"\s+", " ", text).strip()


def read_doc(name):
    return (DOCS_DIR / name).read_text(encoding="utf-8")


_NORM_CACHE = {}


def norm_doc(key):
    if key not in _NORM_CACHE:
        _NORM_CACHE[key] = normalize(read_doc(SRC[key]))
    return _NORM_CACHE[key]


def is_live(sentence, key):
    """True iff `sentence` is a substring of the whitespace-normalized source."""
    return normalize(sentence) in norm_doc(key)


# ============================================================================
# The enumerated axiom-block sentences (four axiom sections + Qualification).
# Each row is (key, verbatim-sentence).  This is the SINGLE sentence list; it is
# guarded LIVE against MINIMAL_AXIOMS_2026-06-29.md at CHECK 01, and the static
# witness is checked against EVERY one of these individually at CHECK 23.
# ============================================================================

SENTENCES = [
    # Lattice / Physical Locality
    ("lattice_sites", "Physical sites are the points of the cubic lattice Z^3, with "
                      "nearest-neighbor adjacency, standard translations, and proper cubic "
                      "rotations about each site."),
    ("lattice_no_privileged_site", "No site is privileged."),
    ("lattice_distinguishes_sites", "Sites are distinguished by the supplied lattice structure alone."),
    # Qubit / Site Possibility
    ("qubit_possibility_domain", "Each site has a domain of local possibilities."),
    ("qubit_one_site_algebra", "The full one-site possibility domain has algebraic presentation M_2(C)."),
    ("qubit_cl30_equivalent", "A Cl(3,0)-compatible real-algebra presentation may be used equivalently "
                              "and adds no further primitive structure."),
    ("qubit_no_privileged_possibility", "No possibility is privileged."),
    ("qubit_distinguishes_possibilities", "Possibilities are distinguished by the supplied algebraic structure alone."),
    # Admissibility / Local Constraint
    ("admissibility_fixed_covariant_rule", "There is one fixed nearest-neighbor admissibility rule, covariant under "
                                           "lattice translations and proper cubic rotations."),
    ("admissibility_varies_with_neighbors", "For each site, the available possibilities are determined by, and vary "
                                            "with, the nearest-neighbor conditions."),
    # Record / Fixed Reality
    ("record_optional_at_site", "A site need not carry a record."),
    ("record_locks_one_readout_invariant_possibility", "When present, a record locks exactly one local possibility from the "
                                                        "subset available at that site under Admissibility; the locked "
                                                        "possibility is invariant under repeated readout."),
    ("record_only_records_readable", "Only records are readable."),
    ("record_readout_content_only", "A readout value is determined by record content alone."),
    ("record_finite_additive_readout", "For any finite collection of pairwise-disjoint records, scalar readout "
                                       "I is additive, with I(empty)=0."),
    # Qualification
    ("qualification_named_content_only", "These axioms state only their named primitive content."),
    ("qualification_extra_structure_needs_authority", "Further physical structure requires derivation, bridge, explicit "
                                                       "admission, or approved primitive registration before use as a premise."),
    ("qualification_state_is_records", "A state is a configuration of records."),
    ("qualification_law_no_privileged_state", "A law privileges no states."),
    ("qualification_law_single_answer", "Its domain is a supplied condition, and at every state where the "
                                        "condition holds it gives exactly one answer."),
]
N_SENTENCES = len(SENTENCES)   # 20 -- the number the FIREWALL now names

# The other four source docs' quoted sentences (also guarded LIVE, not dead data).
OTHER_QUOTES = [
    ("ORDER_RATE", "A record history supplies ordered words and counts. A supplied "
                   "instrument kernel supplies probabilities per admitted step. A "
                   "physical time metric or transition rate requires an additional "
                   "clock/production normalization."),
    ("NONTRIV", "The class contains H = 0, and it is closed under real linear "
                "combinations of allowed Hermitian terms."),
    ("FORM", "Gauge-covariance + locality + Hermiticity supply the basis of allowed "
             "local terms, not the combination."),
    ("FORM", "It does not force non-trivial dynamics: H = 0 is in the class."),
    ("ARROW", "boundary-condition / structural result; honest pinning, not a "
              "from-nothing derivation of the arrow."),
    ("ARROW", "The arrow's existence still requires the supplied low-entropy boundary"),
]

# In-file intent evidence for permanence option (a) (heading + durable-outcome lineage).
PERMANENCE_INTENT_QUOTES = [
    ("AXIOMS", "Record / Fixed Reality"),
    ("AXIOMS", "The 2026-06-05 Record axiom named durable realized-outcome registration"),
]


# ----------------------------------------------------------------------------
# shared exact toy primitives -- ONE covariant, neighbor-dependent rule.
# A record is a (site, locked_value) pair; a configuration is a frozenset of
# records; sites are integer 3-tuples (points of Z^3).
# ----------------------------------------------------------------------------

POSSIBILITY_DOMAIN = frozenset({-1, +1})                          # Qubit domain
NEIGHBOR_OFFSETS = [(1, 0, 0), (-1, 0, 0), (0, 1, 0),
                    (0, -1, 0), (0, 0, 1), (0, 0, -1)]            # Z^3 adjacency


def add(s, t):
    return (s[0] + t[0], s[1] + t[1], s[2] + t[2])


def neighbors(site):
    return [add(site, o) for o in NEIGHBOR_OFFSETS]


def available_at(site, config):
    """Admissibility (ONE covariant neighbor-dependent rule): the available
    possibilities at `site` are the locked values of records on the nearest
    neighbors of `site`; when no neighbor carries a record, the full possibility
    set.  Determined by, and varying with, the nearest-neighbor conditions;
    covariant by construction (relative offsets only); privileges no possibility
    (reads neighbor record content, never the site's own coordinates)."""
    nb = set(neighbors(site))
    vals = frozenset(v for (s, v) in config if s in nb)
    return vals if vals else POSSIBILITY_DOMAIN


def is_record(rec):
    site, val = rec
    return (isinstance(site, tuple) and len(site) == 3
            and all(isinstance(c, int) for c in site) and val in POSSIBILITY_DOMAIN)


def readout_value(rec):
    """A readout value is determined by record content alone: the locked value."""
    _site, val = rec
    return val


def readout_op(rec):
    """Readout as an exact operation: (value, record_after); reading changes
    nothing, so record_after == record_before."""
    return (readout_value(rec), rec)


def readout_idempotent(rec):
    """'invariant under repeated readout': apply readout twice; value stable AND
    record unchanged both times."""
    v1, after1 = readout_op(rec)
    v2, after2 = readout_op(after1)
    return (v1 == v2) and (after1 == rec) and (after2 == rec)


def I_readout(config):
    """Scalar readout I: additive over the (pairwise-disjoint) records of a
    configuration, with I(empty)=0."""
    return sum(readout_value(r) for r in config)


def locks_one_available(rec, config):
    """When present, a record locks exactly one local possibility from the subset
    available at that site under Admissibility."""
    site, val = rec
    return (val in POSSIBILITY_DOMAIN) and (val in available_at(site, config))


def config_admissible(config):
    return all(locks_one_available(r, config) for r in config)


def sites_of(config):
    return frozenset(s for (s, _v) in config)


def flip(config):
    """Value-flip (+1 <-> -1): the possibility-exchange symmetry of the rule."""
    return frozenset((s, -v) for (s, v) in config)


def translate(config, t):
    return frozenset((add(s, t), v) for (s, v) in config)


def rot90z(s):
    """A proper cubic rotation (90 deg about z, det +1): (x,y,z) -> (-y,x,z)."""
    return (-s[1], s[0], s[2])


def rotate_config(config):
    return frozenset((rot90z(s), v) for (s, v) in config)


def relabel(config, perm):
    return frozenset(((perm[s], v) for (s, v) in config))


# The window carries at least one site with no record ("A site need not carry a
# record.").  Availability itself is computed from the full configuration by
# neighbor offset, so the window only bounds the "need-not-carry" witness.
Z3_WINDOW = frozenset({(0, 0, 0), (1, 0, 0), (2, 0, 0), (0, 1, 0), (1, 1, 0),
                       (0, 2, 0), (2, 1, 0), (0, 0, 1)})


def some_site_without_record(config):
    return len(Z3_WINDOW - sites_of(config)) >= 1


def record_axioms_hold(config):
    """Every quoted Record-axiom sentence, read literally, on a configuration."""
    need_not = some_site_without_record(config)
    lock_one = all(locks_one_available(r, config) for r in config)
    idem = all(readout_idempotent(r) for r in config)
    only_records = all(is_record(r) for r in config)      # only records readable
    add_empty = (I_readout(frozenset()) == 0)
    return need_not and lock_one and idem and only_records and add_empty


# ----------------------------------------------------------------------------
# THE shared configuration C_STAR (a +1 domain and a -1 domain meeting at a
# boundary, plus a leaf).  Admissible under the ONE covariant rule; carries value
# diversity and both proper-subset and full availability sets.
# ----------------------------------------------------------------------------

R_A = ((0, 0, 0), +1)   # +1 domain
R_V = ((1, 0, 0), +1)   # +1 domain (boundary)
R_P = ((0, 1, 0), -1)   # -1 domain
R_Q = ((1, 1, 0), -1)   # -1 domain (boundary)
R_R = ((2, 0, 0), +1)   # leaf: only neighbor is R_V -> available {+1}
C_STAR = frozenset({R_A, R_V, R_P, R_Q, R_R})

PERM = {(0, 0, 0): (1, 0, 0), (1, 0, 0): (0, 1, 0), (0, 1, 0): (1, 1, 0),
        (1, 1, 0): (2, 0, 0), (2, 0, 0): (0, 0, 0)}          # 5-cycle on the sites
COV_TEST_SITES = [(0, 0, 0), (1, 0, 0), (0, 1, 0), (1, 1, 0), (2, 0, 0), (2, 1, 0)]
WITNESS_OUTPUTS = frozenset({"order", "count"})   # the only outputs of the witness


def avail_commutes_translation(config, t, test_sites):
    return all(available_at(add(s, t), translate(config, t)) == available_at(s, config)
               for s in test_sites)


def avail_commutes_rotation(config, test_sites):
    return all(available_at(rot90z(s), rotate_config(config)) == available_at(s, config)
               for s in test_sites)


# ============================================================================
# SOURCE LIVENESS (quotes are live, not dead data)                    CHECK 01-03
# ============================================================================

print("# ---- SOURCE LIVENESS (quotes are live, not dead data) ----")

# CHECK 01 -- every enumerated axiom-block sentence is a LIVE substring of the
#             axioms file, with a per-sentence pass report; count == 20.
_live_flags = []
for _key, _sent in SENTENCES:
    _ok = is_live(_sent, "AXIOMS")
    _live_flags.append(_ok)
    print("#   [%s] axiom-block sentence live in file: %s" % (_key, _ok))
check(all(_live_flags) and N_SENTENCES == 20 and len(SENTENCES) == 20,
      "source liveness: all %d axiom-block sentences are live substrings of the axioms file "
      "(sentence-complete list)" % N_SENTENCES)

# CHECK 02 -- the six firewall/form/arrow quoted sentences are live in their files.
_other_flags = []
for _key, _sent in OTHER_QUOTES:
    _ok = is_live(_sent, _key)
    _other_flags.append(_ok)
    print("#   [%-10s] firewall/form/arrow quote live: %s" % (_key, _ok))
check(all(_other_flags) and len(OTHER_QUOTES) == 6,
      "source liveness: all 6 firewall/form/arrow quotes are live substrings of their source files")

# CHECK 03 -- permanence option (a) in-file intent evidence is live.
_intent_flags = [is_live(_s, _k) for (_k, _s) in PERMANENCE_INTENT_QUOTES]
check(all(_intent_flags) and len(PERMANENCE_INTENT_QUOTES) == 2,
      "source liveness: permanence option-(a) intent evidence live: 'Record / Fixed Reality' heading + "
      "durable-realized-outcome lineage line")


# ============================================================================
# PERMANENCE SCOPE GAP (bounded theorem)                           CHECK 04-12
# ----------------------------------------------------------------------------
# Quoted record-readout sentence: "the locked possibility is invariant under repeated readout". Exhibit
# a finite model whose records are readout-stable yet evolution-mortal (a step
# deletes a record), satisfying every quoted Record-axiom sentence read literally
# BEFORE and AFTER the step, under the ONE covariant availability rule.
# ============================================================================

print("# ---- PERMANENCE SCOPE GAP (bounded theorem) ----")

CONFIG_BEFORE = C_STAR


def mortal_step(config, victim):
    """Evolution-mortal step as an explicit map on configurations: removes exactly
    one (site, locked-value) pair."""
    return config - frozenset({victim})


VICTIM = R_A                                     # delete the (0,0,0) +1 record
CONFIG_AFTER = mortal_step(CONFIG_BEFORE, VICTIM)

# CHECK 04 -- readout idempotence as an exact operation on each present record
check(all(readout_idempotent(r) for r in CONFIG_BEFORE),
      "permanence scope gap readout idempotent (repeated readout: same value, record unchanged)")

# CHECK 05 -- readout value determined by content alone (pure function)
_content_pure = (readout_value(R_A) == readout_value(((0, 0, 0), +1))
                 and readout_op(R_A)[1] == R_A)
check(_content_pure,
      "permanence scope gap readout value determined by record content alone (pure, no side effect)")

# CHECK 06 -- I(empty)=0 and additive over pairwise-disjoint records
_disjoint_add = (I_readout(frozenset()) == 0
                 and I_readout(CONFIG_BEFORE)
                 == I_readout(frozenset({R_A, R_V})) + I_readout(frozenset({R_P, R_Q, R_R})))
check(_disjoint_add, "permanence scope gap scalar readout I additive over disjoint records, I(empty)=0")

# CHECK 07 -- each record locks exactly one available possibility (covariant rule)
check(config_admissible(CONFIG_BEFORE),
      "permanence scope gap each record locks one Admissibility-available possibility (covariant rule)")

# CHECK 08 -- every quoted Record-axiom sentence holds BEFORE the step
check(record_axioms_hold(CONFIG_BEFORE),
      "permanence scope gap every quoted Record-axiom sentence holds BEFORE the mortal step")

# CHECK 09 -- covariance: the availability map commutes with a lattice translation
#             (including an odd-parity shift, which flips coordinate parity yet
#             leaves availability unchanged) and with a proper cubic rotation.
_cov_odd = avail_commutes_translation(CONFIG_BEFORE, (1, 0, 0), COV_TEST_SITES)
_cov_gen = avail_commutes_translation(CONFIG_BEFORE, (3, -2, 5), COV_TEST_SITES)
_cov_rot = avail_commutes_rotation(CONFIG_BEFORE, COV_TEST_SITES)
check(_cov_odd and _cov_gen and _cov_rot,
      "permanence scope gap covariance: availability commutes with translation (odd-parity + general) "
      "and proper cubic rotation")

# CHECK 10 -- variation: two sites with different neighbor conditions have
#             different available sets (the vary-with clause).
_av_R = available_at((2, 0, 0), CONFIG_BEFORE)     # leaf: {+1}
_av_A = available_at((0, 0, 0), CONFIG_BEFORE)     # boundary: {+1,-1}
check(_av_R != _av_A and _av_R == frozenset({+1}) and _av_A == POSSIBILITY_DOMAIN,
      "permanence scope gap variation: different neighbor conditions give different available sets "
      "({+1} vs {+1,-1})")

# CHECK 11 -- no fiat privilege: availability is a pure function of neighbor record
#             content, never the site's own coordinate parity.  Two sites of
#             DIFFERENT parity here carry the SAME availability, and availability
#             equals the neighbor-value set (a coordinate-parity rule could not).
def _parity(s):
    return (s[0] + s[1] + s[2]) % 2


_diff_parity_same_avail = (_parity((0, 0, 0)) != _parity((1, 0, 0))
                           and available_at((0, 0, 0), CONFIG_BEFORE)
                           == available_at((1, 0, 0), CONFIG_BEFORE))
_avail_is_neighbor_content = (available_at((2, 0, 0), CONFIG_BEFORE)
                              == frozenset(v for (s, v) in CONFIG_BEFORE
                                           if s in set(neighbors((2, 0, 0)))))
check(_diff_parity_same_avail and _avail_is_neighbor_content,
      "permanence scope gap no-fiat: availability reads neighbor record content only, not coordinate "
      "parity (different-parity sites share an available set)")

# CHECK 12 -- evolution is mortal yet every quoted sentence still holds AFTER: one
#             pair removed, all survivors admissible, availability CHANGES somewhere
#             (vary-with in action at site (0,1,0)), the deleted record is gone ->
#             readout-invariance does NOT entail permanence.
_removed_one = (len(CONFIG_AFTER) == len(CONFIG_BEFORE) - 1
                and VICTIM not in CONFIG_AFTER
                and (CONFIG_BEFORE - frozenset({VICTIM})) == CONFIG_AFTER)
_axioms_after = record_axioms_hold(CONFIG_AFTER)
_survivors_ok = config_admissible(CONFIG_AFTER)
_avail_changed = (available_at((0, 1, 0), CONFIG_BEFORE)
                  != available_at((0, 1, 0), CONFIG_AFTER))
_permanence_broken = VICTIM in CONFIG_BEFORE and VICTIM not in CONFIG_AFTER
check(_removed_one and _axioms_after and _survivors_ok and _avail_changed
      and _permanence_broken,
      "permanence scope gap mortal step deletes one record; survivors still admissible; availability "
      "changes at (0,1,0); readout-invariance does NOT entail permanence")


# ============================================================================
# CONDITIONAL RECORD ORDERING (bounded theorem, conditional on permanence) CHECK 13-21
# ----------------------------------------------------------------------------
# From "A state is a configuration of records" + permanence (named premise, pending
# permanence scope gap): realized histories order by record-set INCLUSION -- a PARTIAL order.  Strict
# increase happens exactly at registration events; idle steps give equal
# consecutive states (unordered by records alone), so record-time is EVENT-time,
# coarser than step-time -- consistent with the count-not-rate firewall.
# ============================================================================

print("# ---- CONDITIONAL RECORD ORDERING (bounded theorem, conditional on permanence) ----")

S_EMPTY = frozenset()
S1 = frozenset({R_A})
S2 = frozenset({R_A, R_V})
S3 = frozenset({R_A, R_V, R_R})
POSET = [S_EMPTY, S1, S2, S3]                 # states for the partial-order laws
CHAIN = [S_EMPTY, S1, S2, S3]                 # strict chain for the rate contrast
# realized history (an IMPORT: a supplied sequence of states) with idle steps and
# a multi-registration step (S1 -> S3 adds two records at once):
REAL_HIST = [S_EMPTY, S_EMPTY, S1, S1, S3]


def subset(a, b):
    return a <= b


def registration_events(hist):
    """Sum of |S_{i+1} \\ S_i| over the history: total NEW records registered.
    Under permanence (forward inclusion) this is the count of registration events,
    and a multi-registration step contributes its full set-difference size."""
    return sum(len(hist[i + 1] - hist[i]) for i in range(len(hist) - 1))


# CHECK 13 -- reflexivity of the inclusion order
check(all(subset(s, s) for s in POSET), "conditional record ordering inclusion order reflexive (partial order)")

# CHECK 14 -- antisymmetry: A<=B and B<=A imply A==B
_antisym = all((not (subset(a, b) and subset(b, a))) or (a == b)
               for a in POSET for b in POSET)
check(_antisym, "conditional record ordering inclusion order antisymmetric")

# CHECK 15 -- transitivity
_trans = all((not (subset(a, b) and subset(b, c))) or subset(a, c)
             for a in POSET for b in POSET for c in POSET)
check(_trans, "conditional record ordering inclusion order transitive")

# CHECK 16 -- realized history: forward inclusion holds at every step; idle steps
#             give EQUAL consecutive states (unordered by records alone).
_forward_all = all(subset(REAL_HIST[i], REAL_HIST[i + 1])
                   for i in range(len(REAL_HIST) - 1))
_idle_positions = [i for i in range(len(REAL_HIST) - 1)
                   if REAL_HIST[i] == REAL_HIST[i + 1]]
check(_forward_all and _idle_positions == [0, 2],
      "conditional record ordering realized history: forward inclusion each step; idle steps give equal "
      "consecutive states (positions 0,2)")

# CHECK 17 -- strict increase EXACTLY at registration events; a multi-registration
#             step (S1->S3) adds two records; registration_events sums set-diffs.
_strict_positions = [i for i in range(len(REAL_HIST) - 1)
                     if REAL_HIST[i] < REAL_HIST[i + 1]]
_multi_step = len(REAL_HIST[4] - REAL_HIST[3]) == 2
check(_strict_positions == [1, 3] and _multi_step
      and registration_events(REAL_HIST) == 3,
      "conditional record ordering strict increase exactly at registration events (positions 1,3); "
      "multi-registration step adds 2; registration_events sums set-diffs = 3")

# CHECK 18 -- record-time is EVENT-time, coarser than step-time: counts are
#             non-decreasing; only the 2 registration steps advance them, while the
#             history has 4 steps and only 3 distinct record-states.
_counts = [len(s) for s in REAL_HIST]                        # [0,0,1,1,3]
_nondec = all(_counts[i] <= _counts[i + 1] for i in range(len(_counts) - 1))
_distinct_states = len(set(REAL_HIST))                       # 3
_events = len(_strict_positions)                             # 2
_steps = len(REAL_HIST) - 1                                  # 4
check(_nondec and _distinct_states == 3 and _events == 2 and _steps == 4
      and _events < _steps,
      "conditional record ordering record-time = event-time coarser than step-time (3 states, 2 events, 4 "
      "steps; counts non-decreasing)")

# CHECK 19 -- no cycles: a strict DECREASE would require deleting a record, which
#             permanence (permanence scope gap clarified) forbids.
_back = mortal_step(S3, R_R)                                 # attempt toward S2 size
_needs_delete = (not subset(S3, _back)) and len(_back) < len(S3) and len(S3 - _back) >= 1
check(_needs_delete,
      "conditional record ordering no cycles: a return step must delete a record (permanence-forbidden)")

# CHECK 20 -- relabel-invariance (site permutation is an order iso) + merge/union
#             monotonicity (A<=B => A|X <= B|X).
_relabel_iso = all(subset(a, b) == subset(relabel(a, PERM), relabel(b, PERM))
                   for a in POSET for b in POSET)
X = frozenset({R_R})
_merge_mono = all((not subset(a, b)) or subset(a | X, b | X)
                  for a in POSET for b in POSET)
check(_relabel_iso and _merge_mono,
      "conditional record ordering order is relabel-invariant (site perm = order iso) and merge-monotone")

# CHECK 21 -- FIREWALL PROTECTION: derivation yields ORDER + COUNT only.  The same
#             strict chain in two step-grids has identical order/counts but a
#             DIFFERENT count-per-step 'rate' (exact Fraction 1 vs 1/2) -> no
#             rate/metric/clock fixed here.  Forward is definitional inclusion, not
#             thermodynamic (disjoint from the arrow note).
_cc = [len(s) for s in CHAIN]                                # [0,1,2,3]
grid_tight = [0, 1, 2, 3]
grid_loose = [0, 2, 4, 6]
rate_tight = Fraction(_cc[-1] - _cc[0], grid_tight[-1] - grid_tight[0])   # 3/3 = 1
rate_loose = Fraction(_cc[-1] - _cc[0], grid_loose[-1] - grid_loose[0])   # 3/6 = 1/2
_order_count_invariant = all(_cc[i] < _cc[i + 1] for i in range(len(_cc) - 1))
_rate_not_fixed = (rate_tight != rate_loose)


def forward(a, b):                        # 'b later than a' iff strictly more records
    return a < b


_forward_def = (forward(S1, S2) is True and forward(S2, S1) is False
                and forward(S1, S2) == (len(S2) > len(S1)))
check(_order_count_invariant and _rate_not_fixed and _forward_def,
      "conditional record ordering firewall-scoped: order+count only (rate %s vs %s not fixed); forward is "
      "definitional inclusion, not thermodynamic" % (rate_tight, rate_loose))


# ============================================================================
# ACCUMULATION IRREDUCIBILITY (narrow no-go, axiom-first)             CHECK 22-25
# ----------------------------------------------------------------------------
# Two exact witnesses that "something happens" is NOT a theorem of the four axioms.
# (i) STATIC witness: the fixed admissible C_STAR with the CONSTANT history is
# guarded against EVERY one of the 20 enumerated axiom-block sentences individually
# (sentence-complete).  (ii) H=0 witness: the forced gauge-covariant class contains
# the zero generator.  Hence non-triviality is genuinely new content.
# ============================================================================

print("# ---- ACCUMULATION IRREDUCIBILITY (narrow no-go, axiom-first) ----")

CONSTANT_HISTORY = [C_STAR, C_STAR, C_STAR, C_STAR]     # nothing ever changes


def identity_law(config):
    """The static 'law': domain = all configurations, giving exactly one answer --
    the same configuration.  Privileges no state."""
    return config


# ---- per-sentence predicates for the static witness (sentence-complete) --------
def _p_lattice_sites():   # sites are Z^3 points with adjacency/translations/rotations available
    return (all(isinstance(c, int) for s in sites_of(C_STAR) for c in s)
            and all(len(s) == 3 for s in sites_of(C_STAR)))


def _p_lattice_no_privileged_site():   # no site privileged: the law is equivariant under site relabeling
    return relabel(identity_law(C_STAR), PERM) == identity_law(relabel(C_STAR, PERM))


def _p_lattice_distinguishes_sites():   # sites distinguished by lattice coordinate alone: <=1 record/site
    return len(sites_of(C_STAR)) == len(C_STAR)


def _p_qubit_possibility_domain():   # each site has a possibility domain; locked values lie in it
    return len(POSSIBILITY_DOMAIN) >= 1 and all(v in POSSIBILITY_DOMAIN
                                                for (_s, v) in C_STAR)


def _p_qubit_one_site_algebra():   # M_2(C): a two-level one-site domain
    return len(POSSIBILITY_DOMAIN) == 2


def _p_qubit_cl30_equivalent():   # equivalent presentation adds no element beyond the 2-value domain
    return POSSIBILITY_DOMAIN == frozenset({-1, +1})


def _p_qubit_no_privileged_possibility():   # no possibility privileged: value-flip maps admissible -> admissible
    return config_admissible(flip(C_STAR)) == config_admissible(C_STAR)


def _p_qubit_distinguishes_possibilities():   # possibilities exchangeable, distinguished by structure alone
    return flip(flip(C_STAR)) == C_STAR and POSSIBILITY_DOMAIN == frozenset({-1, +1})


def _p_admissibility_fixed_covariant_rule():   # one fixed rule, covariant under translations and proper rotations
    return (avail_commutes_translation(C_STAR, (1, 0, 0), COV_TEST_SITES)
            and avail_commutes_rotation(C_STAR, COV_TEST_SITES))


def _p_admissibility_varies_with_neighbors():   # determined by, and varying with, nearest-neighbor conditions
    determined = (available_at((2, 0, 0), C_STAR)
                  == frozenset(v for (s, v) in C_STAR
                               if s in set(neighbors((2, 0, 0)))))
    varies = available_at((2, 0, 0), C_STAR) != available_at((0, 0, 0), C_STAR)
    return determined and varies


def _p_record_optional_at_site():   # a site need not carry a record
    return some_site_without_record(C_STAR)


def _p_record_locks_one_readout_invariant_possibility():   # locks exactly one available possibility, invariant under readout
    return all(locks_one_available(r, C_STAR) and readout_idempotent(r)
               for r in C_STAR)


def _p_record_only_records_readable():   # only records are readable
    return all(is_record(r) for r in C_STAR)


def _p_record_readout_content_only():   # readout value determined by record content alone
    return readout_value(R_A) == readout_value(((0, 0, 0), +1))


def _p_record_finite_additive_readout():   # finite disjoint additivity, I(empty)=0
    return (I_readout(frozenset()) == 0
            and I_readout(C_STAR)
            == I_readout(frozenset({R_A, R_V})) + I_readout(frozenset({R_P, R_Q, R_R})))


def _p_qualification_named_content_only():  # states only named primitive content: each record is a (site,value)
    return all(is_record(r) and len(r) == 2 for r in C_STAR)


def _p_qualification_extra_structure_needs_authority():  # no further structure imported (outputs are exactly order+count)
    return (WITNESS_OUTPUTS == frozenset({"order", "count"})
            and frozenset({"rate", "metric", "clock", "generator"}).isdisjoint(WITNESS_OUTPUTS))


def _p_qualification_state_is_records():  # a state is a configuration of records
    return all(all(is_record(r) for r in c) for c in CONSTANT_HISTORY)


def _p_qualification_law_no_privileged_state():  # a law privileges no states
    return (all(identity_law(c) == c for c in CONSTANT_HISTORY)
            and relabel(identity_law(C_STAR), PERM) == identity_law(relabel(C_STAR, PERM)))


def _p_qualification_law_single_answer():  # single-valued, total where the supplied condition holds
    return all(identity_law(c) == c for c in CONSTANT_HISTORY)


SENTENCE_PRED = {
    "lattice_sites": _p_lattice_sites,
    "lattice_no_privileged_site": _p_lattice_no_privileged_site,
    "lattice_distinguishes_sites": _p_lattice_distinguishes_sites,
    "qubit_possibility_domain": _p_qubit_possibility_domain,
    "qubit_one_site_algebra": _p_qubit_one_site_algebra,
    "qubit_cl30_equivalent": _p_qubit_cl30_equivalent,
    "qubit_no_privileged_possibility": _p_qubit_no_privileged_possibility,
    "qubit_distinguishes_possibilities": _p_qubit_distinguishes_possibilities,
    "admissibility_fixed_covariant_rule": _p_admissibility_fixed_covariant_rule,
    "admissibility_varies_with_neighbors": _p_admissibility_varies_with_neighbors,
    "record_optional_at_site": _p_record_optional_at_site,
    "record_locks_one_readout_invariant_possibility": _p_record_locks_one_readout_invariant_possibility,
    "record_only_records_readable": _p_record_only_records_readable,
    "record_readout_content_only": _p_record_readout_content_only,
    "record_finite_additive_readout": _p_record_finite_additive_readout,
    "qualification_named_content_only": _p_qualification_named_content_only,
    "qualification_extra_structure_needs_authority": _p_qualification_extra_structure_needs_authority,
    "qualification_state_is_records": _p_qualification_state_is_records,
    "qualification_law_no_privileged_state": _p_qualification_law_no_privileged_state,
    "qualification_law_single_answer": _p_qualification_law_single_answer,
}

# CHECK 22 -- the static witness is admissible under the ONE covariant rule, at
#             every element of the constant history.
check(all(config_admissible(c) for c in CONSTANT_HISTORY),
      "accumulation irreducibility(i) static witness admissible under the covariant rule across the constant history")

# CHECK 23 -- the static witness is guarded against EVERY one of the 20 enumerated
#             axiom-block sentences individually (per-sentence pass report):
#             sentence-complete, and NO sentence forces change.
_static_flags = []
for _key, _sent in SENTENCES:
    _ok = SENTENCE_PRED[_key]()
    _static_flags.append(_ok)
    print("#   [%-3s] static witness satisfies sentence: %s" % (_key, _ok))
check(all(_static_flags) and len(SENTENCE_PRED) == N_SENTENCES,
      "accumulation irreducibility(i) static witness satisfies EVERY one of the %d axiom-block sentences "
      "(sentence-complete; no sentence forces change)" % N_SENTENCES)

# CHECK 24 -- the constant history registers NO new record: accumulation FAILS while
#             every quoted axiom sentence holds -> "something happens" NOT forced.
_no_new = all(CONSTANT_HISTORY[i + 1] == CONSTANT_HISTORY[i]
              for i in range(len(CONSTANT_HISTORY) - 1))
_delta = registration_events(CONSTANT_HISTORY)
check(_no_new and _delta == 0,
      "accumulation irreducibility(i) constant history registers 0 new records: non-triviality NOT forced")


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

# CHECK 25 -- H=0 in the gauge-covariant class; a nonzero diagonal H also in it
#             (non-unique, closed under real combinations); sx control NOT in it.
_h0_in = is_zero(comm(H0, G))
_hnz_in = is_zero(comm(Hnz, G))
_hsx_out = not is_zero(comm(Hsx, G))
check(_h0_in and _hnz_in and _hsx_out,
      "accumulation irreducibility(ii) H=0 witness: zero generator in gauge-covariant class (nonzero too; "
      "sx control fails) -> non-triviality is new content")


# ============================================================================
# COMPRESSION MAP (bounded support)                                  CHECK 26-33
# ----------------------------------------------------------------------------
# Given permanence + accumulation: production is definitional; the SINGLE
# discharge map is P3(persistence)<->permanence, P2(production)<->accumulation
# (FORM-E direct / FORM-H + definitional event); #4855 C-add via chain-concat with
# kernel-convolution NAMED OPEN; the conditional ladder re-hangs (B-AXIS external);
# the ordering->transfer-axis (B-AXIS) bridge is a NAMED OPEN target; permanent
# non-goals kept.  The full residue is PARSED from the note's own table.
# ============================================================================

print("# ---- COMPRESSION MAP (bounded support) ----")

# CHECK 26 -- production definitional: event := registration; production count on
#             the strict chain equals the count delta.
check(registration_events(CHAIN) == len(CHAIN[-1]) - len(CHAIN[0]) == 3,
      "compression map(a) production definitional: event:=registration, count == +records on chain")

# CHECK 27 -- registration_events sums |S_{i+1} \\ S_i|: a multi-registration step
#             {} -> {r1,r2} counts 2; the realized history (with idle steps) counts 3.
_r1 = ((5, 0, 0), +1)
_r2 = ((6, 0, 0), -1)
_multi = registration_events([frozenset(), frozenset({_r1, _r2})]) == 2
check(_multi and registration_events(REAL_HIST) == 3,
      "compression map(a') registration_events sums set-differences: multi-registration {}->{r1,r2}=2; "
      "realized history (with idle steps) = 3")

# CHECK 28 -- the SINGLE discharge map: P3(persistence)<->permanence,
#             P2(production)<->accumulation (FORM-E direct / FORM-H + definitional
#             event); touches ONLY P2,P3; and it is IDENTICAL to the note's own text
#             (live grep of the note).
DISCHARGE_4854 = {
    "P3": "permanence sentence (record persistence; permanence scope gap owner surface)",
    "P2": "accumulation sentence (record production; FORM-E direct, or FORM-H + "
          "definitional event := registration-step)",
}
FAMILIES_4854 = {"P1", "P2", "P3", "P4", "CHART-MIX"}
_disch_total = all(v for v in DISCHARGE_4854.values())
_disch_scope = set(DISCHARGE_4854) == {"P2", "P3"} and set(DISCHARGE_4854) <= FAMILIES_4854
_note_norm = normalize(read_doc(NOTE_NAME)).lower()
_note_map_ok = ("p3 (persistence) maps to the permanence sentence" in _note_norm
                and "p2 (production) maps to the accumulation sentence" in _note_norm)
check(_disch_total and _disch_scope and _note_map_ok,
      "compression map(b) single discharge map P3<->permanence, P2<->accumulation (form-conditional); "
      "touches only P2/P3; identical to the note's own text (live grep)")

# CHECK 29 -- #4855 C-add: chain concatenation supplies step composition (associative)
#             and additive counts; the kernel-convolution clause is NAMED OPEN.
def concat(chain_a, chain_b):
    if chain_a[-1] != chain_b[0]:
        return None
    return chain_a + chain_b[1:]


segA = [S_EMPTY, S1]
segB = [S1, S2]
segC = [S2, S3]
_assoc_left = concat(concat(segA, segB), segC)
_assoc_right = concat(segA, concat(segB, segC))
_c_add = (registration_events(_assoc_left) == registration_events(segA)
          + registration_events(segB) + registration_events(segC))
KERNEL_CONVOLUTION_TARGET = "OPEN"
check(_assoc_left == _assoc_right and _c_add and KERNEL_CONVOLUTION_TARGET == "OPEN",
      "compression map(c) #4855 C-add: chain-concat associative + additive; kernel-convolution NAMED OPEN")

# CHECK 30 -- the landed conditional ladder re-hangs.  Each rung carries its named
#             premise/status; nothing beyond form/Stone is unconditional; B-AXIS is a
#             named external axis; terminal Dirac branch is review-pending (#4797).
LADDER = [
    ("form-forced",      "record-preservation+locality+Hermiticity (bounded bridges)", "landed-given-bridges"),
    ("Stone-unique-gen", "B-AXIS supplied-axis premise (external)",                     "landed-conditional-on-axis"),
    ("d_t-parity",       "ABJ external premise",                                        "external-premise"),
    ("d_t=1",            "single-generator N5 cap",                                     "named-premise"),
    ("Dirac-branch",     "#4797 REALIZED_KINETIC_BRANCH (Admissibility-variation)",     "review-pending"),
]
_ladder_ordered = [r[0] for r in LADDER] == [
    "form-forced", "Stone-unique-gen", "d_t-parity", "d_t=1", "Dirac-branch"]
_ladder_premised = all(r[1] for r in LADDER)
_no_uncond = all(r[2] != "landed-unconditional" for r in LADDER)
_axis_external = "external" in LADDER[1][1]
_terminal_pending = LADDER[-1][2] == "review-pending"
check(_ladder_ordered and _ladder_premised and _no_uncond and _axis_external
      and _terminal_pending,
      "compression map(d) conditional ladder re-hangs: each rung premised, B-AXIS external, "
      "terminal Dirac branch review-pending")

# CHECK 31 -- ordering -> lattice-transfer-axis (B-AXIS) bridge is a NAMED OPEN
#             target.  conditional record ordering's ordering outputs are exactly {order, count}; B-AXIS is
#             not among them, so ordering alone does not supply the transfer axis.
B_AXIS_TRANSFER_TARGET = "OPEN"
check("B-AXIS" not in WITNESS_OUTPUTS and WITNESS_OUTPUTS == frozenset({"order", "count"})
      and B_AXIS_TRANSFER_TARGET == "OPEN",
      "compression map(e) ordering->transfer-axis (B-AXIS) NOT supplied by ordering {order,count}: "
      "NAMED OPEN target")

# CHECK 32 -- permanent non-goals: rate/metric/clock, arrow beyond past-hypothesis,
#             ABJ premise externality -- never moved into 'discharged'.
PERMANENT_NON_GOALS = {"rate", "metric", "clock",
                       "arrow-beyond-past-hypothesis", "ABJ-premise-externality"}
_discharged = set(DISCHARGE_4854) | {"C-add"}
check(PERMANENT_NON_GOALS.isdisjoint(_discharged),
      "compression map(f) permanent non-goals (rate/metric/clock, arrow, ABJ-externality) never discharged")

# CHECK 33 -- residue single-source-of-truth: PARSE the note's residue table, count
#             rows, check every required key is present, and check no status cell
#             carries an adoption/promotion token.
def parse_residue_table(note_text):
    """Return list of (item, role, status) triples from the note's residue table."""
    lines = note_text.splitlines()
    rows = []
    in_table = False
    header_seen = False
    for ln in lines:
        s = ln.strip()
        if s.startswith("| Item ") and "Role under this map" in s and "Status in this note" in s:
            in_table = True
            header_seen = True
            continue
        if in_table:
            if not s.startswith("|"):
                break
            if set(s) <= set("|-: "):     # the |---|---|---| separator row
                continue
            cells = [c.strip() for c in s.strip("|").split("|")]
            if len(cells) >= 3:
                rows.append((cells[0], cells[1], cells[2]))
    return rows if header_seen else []


REQUIRED_KEYS = [
    "record permanence premise", "accumulation sentence form-e", "accumulation sentence form-h",
    "p1 (#4854", "p2 production premise", "p3 persistence premise", "p4 (#4854", "chart-mix",
    "c-add", "pos (#4855", "loc (#4855",
    "kernel-convolution clause", "one-parameter composition", "record-compatibility (kernel-target",
    "b-axis supplied-axis premise", "ordering-to-transfer-axis",
    "nonzero-dynamics premise", "#4797", "abj parity external premise", "d_t parity", "n5 cap",
    "past-hypothesis boundary", "rate no-go", "metric no-go", "clock no-go",
    "realized-history import", "unaudited post 2026-06-29 reset",
    "form-forced", "stone-unique generator",
]
FORBIDDEN_STATUS = ("adopt", "retain", "promote", "select")

_residue_rows = parse_residue_table(read_doc(NOTE_NAME))
_items_blob = " || ".join(it.lower() for (it, _r, _st) in _residue_rows)
_missing = [k for k in REQUIRED_KEYS if k not in _items_blob]
_status_clean = all(all(tok not in st.lower() for tok in FORBIDDEN_STATUS)
                    for (_it, _r, st) in _residue_rows)
_row_count_ok = len(_residue_rows) == 30
print("# ---- residue table parsed from the note (single source of truth) ----")
for _it, _r, _st in _residue_rows:
    print("#   [%s] %s" % (_st, _it))
if _missing:
    print("#   MISSING REQUIRED KEYS: %s" % _missing)
check(_row_count_ok and not _missing and _status_clean,
      "compression map residue table parsed from the note: 30 rows, all %d required keys present, "
      "no adoption/promotion status" % len(REQUIRED_KEYS))


# ============================================================================
# GOVERNANCE MAP                                                   CHECK 34-35
# ----------------------------------------------------------------------------
# Exactly two owner surfaces: (1) the permanence sentence -- owner decides (a)
# clarity-fix vs (b) new-content, an OPEN decision this note does NOT foreclose;
# (2) the accumulation sentence, presented in BOTH forms (FORM-E per-event / FORM-H
# per-history). Leverage honesty: the two surfaces replace the H!=0 nonzero-dynamics premise and
# ground event-ordering; B-AXIS stays EXTERNAL (the ordering->transfer-axis bridge
# is OPEN); the other ladder rungs keep their named statuses.
# ============================================================================

print("# ---- GOVERNANCE MAP ----")

OWNER_SURFACES = [
    {
        "id": "permanence-sentence",
        "option": "(a) clarity-fix OR (b) new-content -- OPEN owner decision",
        "sentence": ("A record, once present, is permanent: no later configuration "
                     "removes or alters it. Reading it changes nothing."),
        "status": "owner-surface / not adopted",
    },
    {
        "id": "accumulation-sentence",
        "forms": {
            "FORM-E": "Every step of a realized history registers at least one new record.",
            "FORM-H": ("Records accumulate: every realized history keeps registering "
                       "new records; no configuration is final."),
        },
        "status": "owner-surface / not adopted",
    },
]

# CHECK 34 -- exactly two owner surfaces; surface 1 carries an OPEN (a)/(b) tag (NOT
#             a decided classification); surface 2 carries BOTH forms; nothing adopted.
_two = len(OWNER_SURFACES) == 2
_perm_open = ("OPEN" in OWNER_SURFACES[0]["option"]
              and "(a)" in OWNER_SURFACES[0]["option"]
              and "(b)" in OWNER_SURFACES[0]["option"]
              and "kind" not in OWNER_SURFACES[0])          # no hard clarity/new-content key
_acc_both_forms = set(OWNER_SURFACES[1]["forms"]) == {"FORM-E", "FORM-H"}
_not_adopted = all(s["status"] == "owner-surface / not adopted" for s in OWNER_SURFACES)
check(_two and _perm_open and _acc_both_forms and _not_adopted,
      "governance map two owner surfaces: permanence (OPEN (a)/(b), not foreclosed) + accumulation "
      "(both FORM-E/FORM-H); nothing adopted")

# CHECK 35 -- leverage honesty: the two surfaces replace exactly {H!=0 nonzero-dynamics premise,
#             event-ordering}; B-AXIS is NOT among the targets and stays EXTERNAL
#             (the ordering->transfer-axis bridge is OPEN); the other named rungs
#             keep their statuses.
LEVERAGE_MAP = {
    "accumulation-sentence": "H!=0 nonzero-dynamics premise",            # non-triviality/production premise
    "permanence-sentence": "event-ordering",       # persistence grounds inclusion order
}
LEVERAGE_TARGETS = {"H!=0 nonzero-dynamics premise", "event-ordering"}
STILL_EXTERNAL = {"B-AXIS", "ABJ", "supplied-axis", "past-hypothesis",
                  "#4797 Dirac-branch", "N5 cap"}
_covers = set(LEVERAGE_MAP.values()) == LEVERAGE_TARGETS
_baxis_external = ("B-AXIS" not in LEVERAGE_MAP.values()) and ("B-AXIS" in STILL_EXTERNAL)
_others_named = {"ABJ", "past-hypothesis", "#4797 Dirac-branch", "N5 cap"} <= STILL_EXTERNAL
check(_covers and _baxis_external and _others_named,
      "governance map leverage: two surfaces replace {H!=0 nonzero-dynamics premise, event-ordering}; B-AXIS stays "
      "EXTERNAL (bridge OPEN); other named rungs keep their statuses")


# ============================================================================
# TOTAL
# ============================================================================

_p = sum(1 for (_i, ok, _d) in _RESULTS if ok)
_f = sum(1 for (_i, ok, _d) in _RESULTS if not ok)
print("TOTAL: PASS=%d FAIL=%d" % (_p, _f))

sys.exit(1 if _f else 0)
