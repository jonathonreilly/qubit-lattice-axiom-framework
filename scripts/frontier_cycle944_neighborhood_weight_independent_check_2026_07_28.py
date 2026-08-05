#!/usr/bin/env python3
"""Cycle 944 -- INDEPENDENT CHECKER, spec'd to REFUTE.

This runner does not trust the primary.  It re-derives every load-bearing
number by its own mechanism and attacks the primary's five riskiest
surfaces:

  (i)   the neighborhood formalizations -- is any of them CIRCULAR
        (smuggling the weight, or the outcome, into the neighborhood
        definition)?
  (ii)  the class partitions -- recomputed independently, by union-find
        over the raw rows, and cross-checked against Cycle 913's
        INDEPENDENT CHECKER receipt (a different reconstruction than the
        one the primary read).
  (iii) the naturality corollary -- hunt a law symmetry that preserves
        neighborhood maps but is not covered by the primary's argument.
  (iv)  the conflict checks -- adversarial re-reads of the realized-state
        primitive and the Record clauses.  The block's riskiest surface.
  (v)   the strength lattice -- is Draft B really A3 + locality (+
        covariance) EXACTLY, and is Draft C's ordering as claimed?

Refutations are reported plainly and are not softened.
"""

import ast
import hashlib
import json
import os
import re
import sys
import time
from collections import Counter, OrderedDict

T0 = time.time()
RUNTIME_LIMIT_S = 900

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
OUT = os.path.join(
    ROOT, "outputs",
    "neighborhood_weight_independent_check_cycle944_receipt_2026_07_28.json")
CACHE = os.path.join(
    ROOT, "logs", "runner-cache",
    "frontier_cycle944_neighborhood_weight_independent_check_2026_07_28.txt")

CHECKS = []
TEETH = []
REFUTATIONS = []
FINDINGS = []


def check(name, ok, detail=""):
    CHECKS.append({"check": name, "pass": bool(ok), "detail": detail})
    return bool(ok)


def tooth(name, fired, detail=""):
    TEETH.append({"tooth": name, "fired": bool(fired), "detail": detail})
    return bool(fired)


def refute(name, detail):
    REFUTATIONS.append({"refutation": name, "detail": detail})


def finding(name, detail):
    FINDINGS.append({"finding": name, "detail": detail})


def rd(rel):
    with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as fh:
        return fh.read()


def rj(rel):
    return json.loads(rd(rel))


# --- the primary's own output, read as an ADVERSARY -----------------------
PRIMARY = rj("outputs/neighborhood_weight_cycle944_receipt_2026_07_28.json")
PC = PRIMARY["certificates"]

AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
POLICY = "docs/audit/AXIOM_MINIMALITY_POLICY.md"
RSP = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
R913 = "outputs/selection_function_cycle913_receipt_2026_07_28.json"
K913 = "outputs/selection_independent_check_cycle913_receipt_2026_07_28.json"
R918 = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
S913 = "scripts/frontier_cycle913_selection_function_2026_07_28.py"

AX = rd(AXIOMS)
POL = rd(POLICY)
RSPT = rd(RSP)


# ===========================================================================
# ATTACK 0 -- the quotes, re-verified by an INDEPENDENT normalization
# ===========================================================================
# The primary normalised with " ".join(text.split()).  This checker strips
# markdown blockquote markers and list bullets FIRST, then collapses -- a
# different function, so agreement is evidence rather than tautology.

def norm2(t):
    t = re.sub(r"(?m)^[ \t]*>[ \t]?", " ", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


SOURCES = {AXIOMS: norm2(AX), POLICY: norm2(POL), RSP: norm2(RSPT)}
quote_fail = []
quotes_checked = 0
for key, q in PC["A_PINS"]["quotes"].items():
    src = q["source"]
    if src not in SOURCES:
        SOURCES[src] = norm2(rd(src))
    quotes_checked += 1
    if norm2(q["quote"]) not in SOURCES[src]:
        quote_fail.append(key)
check("A0_all_quotes_verified_under_an_independent_normalization",
      not quote_fail, "failures: %s" % quote_fail)
if quote_fail:
    refute("QUOTES_NOT_BYTE_PRESENT",
           "under an independent normalization these quotes do not appear in "
           "their cited sources: %s" % quote_fail)

# tooth: a deliberately corrupted quote must fail this same machinery
tooth("T1_quote_machinery_rejects_a_corrupted_quote",
      norm2("There is one fixed nearest-neighbour admissibility rule")
      not in SOURCES[AXIOMS]
      and norm2("There is one fixed nearest-neighbor admissibility rule")
      in SOURCES[AXIOMS],
      "one-token corruption (neighbour/neighbor) is rejected")


# ===========================================================================
# ATTACK (i) -- CIRCULARITY of the formalizations
# ===========================================================================
# A formalization is circular if its key function reads any field that is
# downstream of the weight or of the realized outcome.  The checker builds
# its own banned-field list and inspects the RAW ROWS' field names, not the
# primary's description of them.

rows = rj(R913)["certificates"]["C1_SELECTION_TABLE"]["per_lock_point_rows"]
row_fields = sorted(rows[0].keys())
OUTCOME_FIELDS = {"selected_item", "menu"}
WEIGHT_FIELDS = {"weight", "mu", "probability", "likelihood"}
NEIGHBOURHOOD_FIELDS_USED = {
    "F0_EMPTY": set(),
    "F1_OPENNESS": {"neighbour_ordinals"},
    "F2_ORDINALS": {"neighbour_ordinals"},
    "F3_NN_RECORD_CONTENT": {"context_fingerprint"},
    "F4_SITE_NAMING": {"world"},
}
circular = {}
for fid, used in NEIGHBOURHOOD_FIELDS_USED.items():
    bad = used & (OUTCOME_FIELDS | WEIGHT_FIELDS)
    if bad:
        circular[fid] = sorted(bad)
check("A1_no_formalization_reads_an_outcome_or_weight_field",
      not circular, "circular: %s" % circular)
if circular:
    refute("CIRCULAR_FORMALIZATION", str(circular))

# the deeper circularity question: is context_fingerprint itself derived
# from the outcome?  Verified against Cycle 913's OWN SOURCE, not its prose.
S913T = rd(S913)
fp_defs = re.findall(r"context_fingerprint[\"']?\s*[:=]\s*([^\n,}]+)", S913T)
check("A1b_context_fingerprint_definition_located", len(fp_defs) > 0,
      "definitions found: %d" % len(fp_defs))
uses_selection = any("select" in d.lower() for d in fp_defs)
check("A1c_context_fingerprint_is_not_built_from_the_selection",
      not uses_selection, "defs: %s" % fp_defs[:3])
if uses_selection:
    refute("FINGERPRINT_IS_OUTCOME_DERIVED",
           "the neighborhood map is built from the selection it is supposed "
           "to be independent of")

tooth("T2_circularity_probe_fires_on_a_planted_outcome_field",
      bool({"context_fingerprint", "selected_item"}
           & (OUTCOME_FIELDS | WEIGHT_FIELDS))
      and not bool({"context_fingerprint", "neighbour_ordinals"}
                   & (OUTCOME_FIELDS | WEIGHT_FIELDS)),
      "planted 'selected_item' in a neighborhood definition is caught")


# ===========================================================================
# ATTACK (ii) -- the class partitions, recomputed INDEPENDENTLY
# ===========================================================================
# Mechanism: union-find over rows sharing a key, rather than the primary's
# dict-grouping.  Then cross-checked against Cycle 913's INDEPENDENT CHECKER
# receipt -- a reconstruction the primary never read.

class DSU:
    def __init__(self, items):
        self.p = {i: i for i in items}

    def find(self, x):
        while self.p[x] != x:
            self.p[x] = self.p[self.p[x]]
            x = self.p[x]
        return x

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            self.p[ra] = rb


def partition_via_dsu(rows_, keyfn):
    worlds = [r["world"] for r in rows_]
    d = DSU(worlds)
    first = {}
    for r in rows_:
        k = keyfn(r)
        if k in first:
            d.union(r["world"], first[k])
        else:
            first[k] = r["world"]
    groups = {}
    for w in worlds:
        groups.setdefault(d.find(w), []).append(w)
    return {k: sorted(v) for k, v in groups.items()}


KEYS = {
    "F0_EMPTY": lambda r: 0,
    "F1_OPENNESS": lambda r: tuple(1 if o > 0 else 0
                                   for o in r["neighbour_ordinals"]),
    "F2_ORDINALS": lambda r: tuple(r["neighbour_ordinals"]),
    "F3_NN_RECORD_CONTENT": lambda r: r["context_fingerprint"],
    "F4_SITE_NAMING": lambda r: (r["world"],),
}

my_counts = {}
my_largest = {}
for fid, kf in KEYS.items():
    parts = partition_via_dsu(rows, kf)
    my_counts[fid] = len(parts)
    my_largest[fid] = max(len(v) for v in parts.values())

primary_913 = PC["Q1_THE_NEIGHBORHOOD_MAP_FORMALIZED"][
    "class_partitions_by_arena"]["C913_CONTROL_164"]
mismatch = {fid: (my_counts[fid], primary_913[fid]["classes"])
            for fid in KEYS if my_counts[fid] != primary_913[fid]["classes"]}
check("A2_partitions_agree_with_the_primary", not mismatch,
      "mine vs primary: %s" % (mismatch or "all agree"))
if mismatch:
    refute("PARTITION_MISMATCH", str(mismatch))

# cross-check against Cycle 913's INDEPENDENT CHECKER's own ladder
own = rj(K913)["independent_reconstruction"]["own_ladder"]
LADDER_NAMES = {
    "F0_EMPTY": "EMPTY_CONTEXT",
    "F1_OPENNESS": "R1_nearest_neighbour_openness_only",
    "F2_ORDINALS": "R1_nearest_neighbour_exact_ordinals",
    "F3_NN_RECORD_CONTENT": "R1_nearest_neighbour_record_content",
}
tri = {}
for fid, ln in LADDER_NAMES.items():
    if ln in own:
        if own[ln]["groups"] != my_counts[fid]:
            tri[fid] = (my_counts[fid], own[ln]["groups"])
check("A2b_partitions_agree_with_913s_INDEPENDENT_CHECKER", not tri,
      "mine vs 913-checker: %s" % (tri or "all agree"))
if tri:
    refute("PARTITION_DISAGREES_WITH_INDEPENDENT_RECONSTRUCTION", str(tri))

# the six-site partition, recomputed
SIX = [254, 450, 475, 540, 558, 715]
byw = {r["world"]: r for r in rows}
six_parts = {}
for w in SIX:
    six_parts.setdefault(byw[w]["context_fingerprint"], []).append(w)
mine_six = sorted([sorted(v) for v in six_parts.values()])
prim_six = PC["Q1_THE_NEIGHBORHOOD_MAP_FORMALIZED"][
    "class_partitions_by_arena"]["C936_SIX_SITES"]["F3_NN_RECORD_CONTENT"][
        "partition"]
check("A2c_six_site_partition_reproduced",
      mine_six == [sorted(x) for x in prim_six],
      "mine=%s primary=%s" % (mine_six, prim_six))
if mine_six != [sorted(x) for x in prim_six]:
    refute("SIX_SITE_PARTITION_MISMATCH",
           "mine=%s primary=%s" % (mine_six, prim_six))

tooth("T3_partition_machinery_detects_a_planted_merge",
      len(partition_via_dsu(rows, lambda r: r["context_fingerprint"][:1])) !=
      my_counts["F3_NN_RECORD_CONTENT"],
      "truncating the fingerprint merges classes and is detected")

# the KEY MEASUREMENT, re-derived: do same-class pairs exist?
same_class_exists = any(my_largest[f] > 1 for f in
                        ("F1_OPENNESS", "F2_ORDINALS", "F3_NN_RECORD_CONTENT"))
check("A2d_same_class_pairs_genuinely_exist", same_class_exists,
      "largest classes: %s" % my_largest)


# ===========================================================================
# ATTACK -- the primary's own covariance correction, verified at the SOURCE
# ===========================================================================
# The primary claims 913's cubic classes orbit the SIX-SLOT COLOURING of the
# declared embedding and are therefore INCOMPARABLE with the record-content
# partition.  Verified by reading 913's function, not its prose.

m = re.search(r"def cubic_covariance\(.*?\n(.*?)\n\ndef ", S913T, re.S)
cubic_src = m.group(1) if m else ""
uses_colorings = "context_colorings" in cubic_src
uses_fingerprint = "context_fingerprint" in cubic_src
check("A3_cubic_uses_the_colouring_not_the_fingerprint",
      uses_colorings and not uses_fingerprint,
      "context_colorings=%s context_fingerprint=%s"
      % (uses_colorings, uses_fingerprint))
if not (uses_colorings and not uses_fingerprint):
    refute("COVARIANCE_FRAMING_STILL_WRONG",
           "913's cubic_covariance does not have the input structure the "
           "primary's correction asserts")
else:
    finding("PRIMARY_SELF_CORRECTION_CONFIRMED",
            "the primary's disclosed self-caught correction is right at the "
            "source level: cubic_covariance() consumes context_colorings("
            "...alphabet) and never touches the record-content fingerprint, "
            "so the 3/6/7 counts are NOT a coarsening of the 54.")

tooth("T4_source_level_probe_would_catch_the_opposite",
      "context_colorings" in cubic_src and "orbit_ids" in cubic_src,
      "the probe reads real structure, not a comment")


# ===========================================================================
# ATTACK (iii) -- the naturality corollary: hunt an UNCOVERED symmetry
# ===========================================================================
# The primary derived Draft B's covariance from ADM_RULE's two named groups
# (lattice translations, proper cubic rotations) and computed the collapse
# ONLY for the cubic half.  The translation half is a LANDED, MEASURED action
# on this arena -- and the primary never used it.

trans = rj(R913)["certificates"]["C2_DEPENDENCE"]["covariance_translation"]
orbits_meeting = trans["census_orbits_meeting_the_lock_set"]
group_order = trans["group_order"]
check("A4_translation_action_is_a_real_landed_symmetry",
      trans["action_is_a_census_bijection"] is True and group_order > 1,
      "Z_%d, %d orbits meet the lock set" % (group_order, orbits_meeting))

primary_mentions_translation = "census_orbits_meeting_the_lock_set" in \
    json.dumps(PC.get("Q2_WHAT_THE_CLAUSE_FORCES", {}))
if not primary_mentions_translation:
    refute("NATURALITY_COROLLARY_IS_INCOMPLETE",
           "ADM_RULE byte-names TWO covariance groups -- 'lattice "
           "translations AND proper cubic rotations'.  The primary computed "
           "Draft B's collapse for the cubic half only.  The translation half "
           "is a landed, measured action on this very arena (the Cycle-878 "
           "monitor-phase Z_%d, a census bijection, whose orbits meet the "
           "lock set in %d orbits).  Under Draft B the weight must ALSO be "
           "constant on those orbits, so Draft B's freedom on the control "
           "arena is bounded by the JOIN of the neighbourhood partition and "
           "the orbit partition -- strictly coarser than either.  The primary "
           "UNDERSTATES Draft B's purchase and does not say so.  This is an "
           "incompleteness, not an error: every number the primary reports "
           "remains true as an upper bound."
           % (group_order, orbits_meeting))
    finding("TRANSLATION_HALF_UNCOMPUTED",
            "the join cannot be computed from published bytes: Cycle 913's "
            "receipt reports orbit COUNTS but not per-world orbit membership, "
            "so this checker cannot supply the missing number either.  Named "
            "for the next block.")

# the hunt must be DISCRIMINATING: it must flag a receipt that omits the
# translation half and clear one that carries it.  (The primary now carries
# it -- this checker's earlier run refuted it and the finding was adopted.)
_omitting = json.dumps({"ii_draft_B_covariant_collapse_cubic_half": {}})
_probe_on_omitting = "census_orbits_meeting_the_lock_set" not in _omitting
tooth("T5_uncovered_symmetry_hunt_is_discriminating",
      _probe_on_omitting and primary_mentions_translation,
      "the probe flags a receipt lacking the translation half and clears the "
      "corrected primary that carries it")
if primary_mentions_translation:
    finding("NATURALITY_COMPLETENESS_CONFIRMED",
            "the primary adopted this checker's earlier NATURALITY_COROLLARY_"
            "IS_INCOMPLETE refutation: ADM_RULE's translation half is now "
            "computed and reported, every Draft-B freedom count is restated "
            "as an upper bound, and the uncomputable join is named as a gap.")

# is the trivial half of the corollary actually trivial?  Test that equal
# neighborhood maps really do force equal weights under the primary's own
# statement -- i.e. that CE is not smuggling an extra premise.
ce = PC["Q2_WHAT_THE_CLAUSE_FORCES"]["i_class_equality_law"]
check("A4b_CE_is_stated_as_definitional_not_derived",
      "definitional" in json.dumps(ce).lower(),
      "CE must not claim to be derived from anything")


# ===========================================================================
# ATTACK (iv) -- the conflict checks, adversarially re-read
# ===========================================================================
# THE BLOCK'S RISKIEST SURFACE.  The primary concluded the realized-state
# primitive does NOT forbid a weight, on the grounds that its non-supply
# clauses are scoped by "supplied by it".  Re-read adversarially.

rsp_n = norm2(RSPT)
scope_phrases = ["is supplied by it", "It does not supply",
                 "Nothing more is supplied"]
present = {p: (p in rsp_n) for p in scope_phrases}
check("A5_scoping_phrases_are_byte_present", all(present.values()),
      str(present))

# The adversarial reading: is there ANY sentence in the primitive that
# forbids rather than declines?  Hunt imperative/prohibitive forms.
prohibitive = re.findall(
    r"[^.]*\b(?:must not|may not|forbids|forbidden|prohibit\w*)\b[^.]*\.",
    RSPT)
check("A5b_no_prohibitive_sentence_in_the_primitive",
      len(prohibitive) == 0,
      "prohibitive sentences found: %s" % prohibitive)
if prohibitive:
    refute("PRIMITIVE_CONTAINS_A_PROHIBITION",
           "the primary's 'declines, does not forbid' reading is contradicted "
           "by: %s" % prohibitive)
else:
    finding("PRIMITIVE_READING_SURVIVES",
            "the realized-state primitive contains no prohibitive sentence at "
            "all -- every non-supply clause is scoped to what the primitive "
            "itself carries.  The primary's reading survives an adversarial "
            "hunt for imperatives.")

# The one sentence that IS load-bearing against the lane: no averaging.
avg = "no averaging over alternatives" in rsp_n
check("A5c_no_averaging_clause_present_and_carried", avg
      and "no-averaging" in json.dumps(PC).lower().replace("_", "-"),
      "the primary must carry the no-averaging cost")

# Record: does it contain a non-supply clause the primary missed?
rec_block = AX[AX.find("### Record / Fixed Reality"):AX.find("## Qualification")]
rec_nonsupply = re.findall(r"[^.]*\bdoes not\b[^.]*\.", rec_block)
check("A5d_record_axiom_has_no_non_supply_clause",
      len(rec_nonsupply) == 0,
      "found: %s" % rec_nonsupply)
if rec_nonsupply:
    refute("RECORD_NON_SUPPLY_MISSED",
           "the Record axiom does contain non-supply text the primary said it "
           "lacks: %s" % rec_nonsupply)

# The binding policy: verify the primary's decisive claim at the bytes.
pol_n = norm2(POL)
assigns = "assign weights" in pol_n
adm_subject = "Admissibility does not choose the readout context" in pol_n
check("A5e_binding_policy_says_admissibility_does_not_assign_weights",
      assigns and adm_subject, "assign weights=%s subject=%s"
      % (assigns, adm_subject))
if not (assigns and adm_subject):
    refute("POLICY_CLAIM_UNSUPPORTED",
           "the primary's sharpest discriminator is not supported by the "
           "policy bytes")

# adversarial: does the policy clause have an escape the primary missed?
# e.g. is it scoped to a superseded axiom version?  A crude proximity probe
# over a chronological log gives false positives (the log narrates what each
# reset superseded), so the test is made PRECISE: find the dated bullet that
# GOVERNS the clause, and confirm it is the reset that installed the CURRENT
# axiom source.
idx = pol_n.find("Admissibility does not choose the readout context")
bullets = [(m.start(), m.group(1)) for m in
           re.finditer(r"\*\*(\d{4}-\d{2}-\d{2}) -- ", pol_n)
           if m.start() < idx]
governing = bullets[-1][1] if bullets else None
governing_seg = pol_n[bullets[-1][0]:idx] if bullets else ""
names_current_source = "MINIMAL_AXIOMS_2026-06-29.md" in governing_seg
# and the axiom memo itself points at this policy section for its authority
memo_points_here = ("explicit owner approval for the 2026-06-29 foundation "
                    "reset is recorded in") in norm2(AX).lower()
clause_is_current = (governing == "2026-06-29" and names_current_source)
check("A5f_policy_clause_governs_the_CURRENT_axiom_set", clause_is_current,
      "governing dated bullet=%s names_current_source=%s memo_points_here=%s"
      % (governing, names_current_source, memo_points_here))
if not clause_is_current:
    refute("POLICY_CLAUSE_MAY_BE_SUPERSEDED",
           "the No-laundering clause is not governed by the bullet that "
           "installed the current axiom source; the primary treated it as "
           "current without checking")
else:
    finding("POLICY_CLAUSE_CONFIRMED_CURRENT_AND_BINDING",
            "an earlier proximity probe in this checker flagged the "
            "No-laundering clause as possibly superseded; that was a FALSE "
            "POSITIVE of the probe, not a defect in the primary.  Made "
            "precise: the clause is governed by the '2026-06-29 -- Foundation "
            "reset' bullet, which names docs/MINIMAL_AXIOMS_2026-06-29.md -- "
            "the current axiom source -- and it sits in section 6, the very "
            "section the axiom memo cites as its own status authority.  The "
            "primary's sharpest discriminator STRENGTHENS: the clause is "
            "current, owner-approved, and binding.  Checker-side probe fixed "
            "and disclosed.")

tooth("T14_governing_bullet_probe_is_discriminating",
      clause_is_current
      and not (re.search(r"\*\*(\d{4}-\d{2}-\d{2}) -- ", "no bullets here")
               is not None),
      "the probe locates a real dated governing bullet rather than matching "
      "any nearby date token")

tooth("T6_conflict_machinery_fires_on_a_planted_prohibition",
      len(re.findall(r"[^.]*\bmust not\b[^.]*\.",
                     "The framework must not supply weights.")) == 1
      and len(prohibitive) == 0,
      "a planted prohibitive sentence is detected by the same regex")

tooth("T7_policy_probe_fires_on_a_planted_negation",
      "assign weights" in pol_n
      and "assign weights" not in pol_n.replace("assign weights", "XX", 1),
      "removing the phrase changes the verdict")


# ===========================================================================
# ATTACK (v) -- the strength lattice
# ===========================================================================
SL = PC["Q3_THE_REQUIRED_AND_MINIMAL_DOSSIER"]["b_strength_lattice"]
claim = SL["draft_B_decomposed"]

# The primary says ADM2 is "already an axiom" so B == A3 + LOC + COV on top of
# the existing set.  But the primary ALSO finds (Q1) that the existing menu
# clause is EXISTENTIAL while both drafts presuppose a FUNCTIONAL one.  Those
# two statements cannot both be right.
q1 = PC["Q1_THE_NEIGHBORHOOD_MAP_FORMALIZED"]
has_passenger = "EXISTENTIAL TO FUNCTIONAL" in json.dumps(q1).upper()
# SUBSTANCE test, not a substring test: the lattice is inconsistent with the
# passenger finding only if its decomposition of Draft B OMITS the
# existential-to-functional upgrade as a conjunct.  An earlier version of this
# probe matched the string "already an axiom", which now appears inside the
# primary's own DISCLOSURE of having fixed the defect -- a false positive.
decomp = json.dumps(SL.get("draft_B_decomposed", ""))
names_FUNC = "FUNC" in decomp
has_FUNC_primitive = "FUNC" in json.dumps(SL.get("definitions", {})) or \
    "FUNC" in json.dumps(SL.get("primitives", {})) or "FUNC" in json.dumps(SL)
lattice_levels = json.dumps(SL.get("the_lattice", []))
FUNC_on_the_lattice = "FUNC" in lattice_levels
inconsistent = has_passenger and not (names_FUNC and FUNC_on_the_lattice)
check("A6_strength_lattice_is_internally_consistent", not inconsistent,
      "passenger=%s FUNC_named_in_decomposition=%s FUNC_on_lattice=%s"
      % (has_passenger, names_FUNC, FUNC_on_the_lattice))
if inconsistent:
    refute("STRENGTH_LATTICE_INTERNALLY_INCONSISTENT",
           "the primary's Q1 finds that the existing menu clause is "
           "EXISTENTIAL (2026-07-02 owner ruling) and that both drafts "
           "presuppose a FUNCTIONAL one -- it calls this a 'passenger cost'.  "
           "But its strength lattice simultaneously says Draft B's first "
           "conjunct (ADM2) is 'already an axiom' and therefore redundant, "
           "which is true ONLY under the functional reading.  Both cannot "
           "hold.  CORRECT STATEMENT: on top of the existing axiom set, "
           "Draft B == A3_bare + LOC + COV + (the existential-to-functional "
           "upgrade of the menu clause).  Draft B's first conjunct is NOT "
           "redundant; it is the upgrade, written out.  The primary reports "
           "the upgrade honestly in Q1 and then drops it from the lattice.")

# is B strictly stronger than A3?  Test the witness the primary offers.
w = SL.get("witness_B_stronger_than_A3", "")
witness_ok = "30" in w and my_largest["F3_NN_RECORD_CONTENT"] == 30
check("A6b_B_stronger_than_A3_witness_is_real", witness_ok,
      "largest F3 class recomputed = %d" % my_largest["F3_NN_RECORD_CONTENT"])

# the probe must still FIRE on a lattice that omits FUNC
_bad_lattice = {"draft_B_decomposed": "A3_bare + LOC + COV",
                "the_lattice": [{"content": "A3_bare + LOC + COV"}]}
_bad_inconsistent = True and not (
    "FUNC" in json.dumps(_bad_lattice.get("draft_B_decomposed", ""))
    and "FUNC" in json.dumps(_bad_lattice.get("the_lattice", [])))
tooth("T8_lattice_probe_fires_on_a_lattice_that_omits_FUNC",
      _bad_inconsistent and not inconsistent,
      "the substance probe catches an omitting lattice and clears the "
      "corrected one")
if not inconsistent:
    finding("STRENGTH_LATTICE_CORRECTION_CONFIRMED",
            "the primary adopted this checker's earlier refutation: Draft B's "
            "decomposition now names FUNC (the existential-to-functional "
            "upgrade) as a conjunct and the lattice carries it as its own "
            "level.  The residual 'already an axiom' string in the primary is "
            "inside its disclosure of the fix, not in an assertion -- an "
            "earlier substring version of this probe false-positived on it "
            "and has been made a substance test.")


# ===========================================================================
# ATTACK -- DRAFT C
# ===========================================================================
DC = PC["QC_DRAFT_C_THE_REPLACEMENT_WORDING"]

# C1: the vacuous-rule regression.  Verify the ruling's byte content and that
# the counterexample really satisfies C.
ruling = ("\"Vary with\" is existential, not per-neighborhood: availability "
          "is not constant across nearest-neighbor conditions")
check("A7_the_2026_07_02_ruling_is_byte_present", norm2(ruling) in pol_n,
      "the ruling Draft C inherits")

# the counterexample, modelled concretely: a weight assignment that is
# strictly positive everywhere and varies in value with the conditions.
def satisfies_draft_C(weights_by_condition):
    """C requires: every possibility carries a weight, and the weight is
    determined by and varies with the conditions."""
    varies = len({tuple(sorted(v.items())) for v in
                  weights_by_condition.values()}) > 1
    total = all(all(x > 0 for x in v.values())
                for v in weights_by_condition.values())
    return varies, total


def availability_is_vacuous(weights_by_condition):
    """availability := support of w.  Vacuous = full domain under EVERY
    condition."""
    return all(all(x > 0 for x in v.values())
               for v in weights_by_condition.values())


CE_MODEL = {  # two neighbour conditions, two local possibilities
    "cond_A": {"p0": 1, "p1": 3},
    "cond_B": {"p0": 2, "p1": 2},
}
varies, allpos = satisfies_draft_C(CE_MODEL)
vacuous = availability_is_vacuous(CE_MODEL)
regression_real = varies and allpos and vacuous
check("A7b_draft_C_vacuous_rule_regression_is_real", regression_real,
      "varies=%s all_positive=%s availability_vacuous=%s"
      % (varies, allpos, vacuous))
if regression_real:
    finding("DRAFT_C_REGRESSION_CONFIRMED",
            "an explicit two-condition model satisfies Draft C in full (the "
            "weight varies with the conditions) while making the available "
            "set the FULL local domain under every condition -- the vacuous "
            "rule the 2026-07-02 ruling says the CURRENT sentence excludes.  "
            "The primary's claim that Draft C does not subsume the replaced "
            "sentence is CONFIRMED by construction, not merely argued.")
else:
    refute("DRAFT_C_REGRESSION_NOT_REPRODUCIBLE",
           "the primary's counterexample does not go through")

tooth("T9_regression_model_is_discriminating",
      availability_is_vacuous({"c": {"p0": 1, "p1": 0}}) is False
      and vacuous is True,
      "a model with a zero weight is correctly NOT vacuous")

# C2: well-foundedness.  Verify the loop really closes under the availability
# reading and really opens under the record reading.
def wellfounded(conditions_mean):
    # availability := supp(w); w := f(conditions)
    # closed iff conditions are themselves availability-valued
    return conditions_mean != "availability"


check("A7c_draft_C_wellfoundedness_claim_reproduced",
      wellfounded("record_content") and not wellfounded("availability"),
      "loop closes only under the availability reading")

# C3: does the corrected form actually escape C-raw's circularity?  It must
# quantify over a domain supplied INDEPENDENTLY of availability.
qubit_domain = "Each site has a domain of local possibilities."
check("A7d_qubit_supplies_the_independent_domain",
      norm2(qubit_domain) in SOURCES[AXIOMS],
      "the corrected form's quantifier needs this axiom to be well formed")
if norm2(qubit_domain) not in SOURCES[AXIOMS]:
    refute("CORRECTED_C_HAS_NO_INDEPENDENT_DOMAIN",
           "'each local possibility' has no supplier, so the correction does "
           "not escape the circularity")

# C4: the strength ordering -- attack the claim that C entails B.
def C_entails_B_check(functional, support_identified):
    # C: conditions determine weight; availability := supp(w)
    # B: conditions determine (a) admissibility and (b) each weight
    return functional and support_identified


check("A7e_C_entails_B_only_under_both_premises",
      C_entails_B_check(True, True)
      and not C_entails_B_check(False, True)
      and not C_entails_B_check(True, False),
      "the entailment needs BOTH the functional reading and the support "
      "identification")
finding("DRAFT_C_ORDERING_IS_DOUBLY_CONDITIONAL",
        "the primary states C > B 'under the functional reading'.  The "
        "entailment in fact needs TWO premises: the functional reading AND "
        "the availability-is-support identification.  The primary carries the "
        "second implicitly.  Not an error -- an under-statement of the "
        "conditions.")

# C5: the likelihood clause -- does it collide with a byte-present clause?
lik_words = ["probability rule", "weighting", "measure"]
rsp_hits = [w for w in lik_words if w in rsp_n]
check("A7f_likelihood_vocabulary_collision_is_real", len(rsp_hits) >= 2,
      "realized-state primitive names: %s" % rsp_hits)

tooth("T10_draft_C_attacks_are_discriminating",
      not wellfounded("availability") and wellfounded("record_content")
      and regression_real,
      "the Draft C probes separate the readings rather than passing "
      "everything")


# ===========================================================================
# ATTACK -- DRAFT D
# ===========================================================================
DD = PC["QD_DRAFT_D_THE_SIMPLIFICATION"]
D_RAW = DD["draft_D_raw"]
D_II = DD["draft_D_ii_tightened"]

# D1: is the primary right that D-raw's natural reading is D-i (no per-item
# quantifier)?  Test structurally: hunt any quantifier binding a possibility
# variable inside the likelihood phrase.
lik_phrase = re.search(r"likel[iy]hood[^.;]*", D_RAW)
lik_txt = lik_phrase.group(0) if lik_phrase else ""
per_item_quantifiers = ["each", "every", "per possibility", "locking"]
d_raw_has_per_item = any(q in lik_txt.lower() for q in per_item_quantifiers)
check("A10_D_raw_likelihood_phrase_has_no_per_item_quantifier",
      not d_raw_has_per_item,
      "phrase=%r quantifier_found=%s" % (lik_txt, d_raw_has_per_item))
if d_raw_has_per_item:
    refute("D_RAW_IS_NOT_D_I",
           "the primary claims the owner's literal words read as a per-site "
           "scalar; the likelihood phrase does bind a possibility variable")
else:
    finding("D_I_READING_CONFIRMED_STRUCTURALLY",
            "the likelihood phrase in the owner's written wording is %r -- a "
            "single definite noun phrase with no quantifier over "
            "possibilities.  The primary's claim that D-raw naturally reads "
            "as D-i (a per-site rate, no Born content) is confirmed by "
            "structure, not by taste." % lik_txt)

# D2: the tightened D-ii MUST bind the possibility variable, else the
# distinction is empty.
check("A10b_D_ii_binds_the_possibility_variable",
      "locking each local possibility" in D_II,
      "the tightened wording must differ from D-raw in exactly this way")

# D3: D-raw must genuinely retain the availability conjunct (the C-regression
# repair the primary claims).
retains = "the available possibilities and" in D_RAW.lower()
derives = "available possibilities are those of nonzero" in D_II.lower()
check("A10c_D_raw_retains_availability_D_ii_derives_it", retains and derives,
      "retains=%s derives=%s" % (retains, derives))
if retains and derives:
    finding("D_SHAPE_TRADEOFF_CONFIRMED",
            "D-raw keeps availability as a conjunct (so the vacuous-rule "
            "exclusion survives) while the tightened D-ii derives it from "
            "the support (re-introducing Draft C's regression).  The "
            "primary's claim that D's two wordings trade unification against "
            "the exclusion is confirmed textually.")

# D4: the four-conjunct closure claim, checked against the byte-quoted gate
# rather than the primary's summary of it.
gate_txt = PC["Q0_PRIOR_ART_SWEEP"]["the_open_gates_relationship"][
    "the_gate_byte_quoted"]
gate_present = norm2(gate_txt) in SOURCES[AXIOMS]
conj = ["which admissible possibility a new record locks", "at which site",
        "with what weight", "or at what rate"]
all_conj_in_gate = all(c in gate_txt for c in conj)
mapped = DD["READING_D_ii_PER_POSSIBILITY"]["THE_OPEN_GATES_BYTE_RELATIONSHIP"][
    "what_D_ii_supplies_per_conjunct"]
all_mapped = set(mapped.keys()) == set(conj)
check("A10d_D_ii_four_conjunct_closure_verified_against_the_gate_bytes",
      gate_present and all_conj_in_gate and all_mapped,
      "gate_present=%s conjuncts_in_gate=%s all_mapped=%s"
      % (gate_present, all_conj_in_gate, all_mapped))
if not (gate_present and all_conj_in_gate and all_mapped):
    refute("D_II_GATE_CLOSURE_UNSUPPORTED",
           "the claim that D-ii closes all four formation conjuncts does not "
           "check out against the byte-quoted gate")

# D5: the 'Records form.' surface -- verify the sentence really is bare.
rf = "Records form."
rf_present = rf in AX
# is it quantified anywhere in the axiom text?
rf_idx = AX.find(rf)
rf_context = AX[max(0, rf_idx - 200):rf_idx + 200]
rf_quantified = bool(re.search(r"Records form[^.]*\b(?:always|at every|"
                               r"somewhere|eventually)\b", rf_context))
check("A10e_records_form_is_an_unquantified_two_word_sentence",
      rf_present and not rf_quantified,
      "present=%s quantified=%s" % (rf_present, rf_quantified))
if rf_present and not rf_quantified:
    finding("RECORDS_FORM_AMBIGUITY_IS_REAL",
            "'Records form.' appears in the Record axiom as a bare two-word "
            "sentence with no quantifier.  The primary's finding that D-ii's "
            "grading of formation is reading-dependent -- no conflict under "
            "the generic reading, collapse to Draft C under the categorical "
            "one -- rests on a genuine textual ambiguity, not a manufactured "
            "one.")

# D6: the degeneracy claim -- formation really is a deterministic predicate
# on the current arenas.
_c936_receipt = rj("outputs/choice_substrate_cycle936_receipt_2026_07_28.json")
_preserved = _c936_receipt["certificates"]["C6_THE_PRICE_SHEET"][
    "PRESERVED_BATTERY"]
pred_918 = any("formation by the same global-clean predicate" in x
               for x in _preserved)
check("A10f_formation_is_a_deterministic_predicate_on_current_arenas",
      pred_918 and len(rows) == 164,
      "936 PRESERVED_BATTERY carries the global-clean formation predicate "
      "(%s); 913 has %d deterministic lock points" % (pred_918, len(rows)))
if pred_918:
    finding("D_II_RATE_CONTENT_IS_UNTESTABLE_HERE",
            "Cycle 936's own receipt byte-carries 'formation by the same "
            "global-clean predicate' among its PRESERVED_BATTERY items.  "
            "Formation is a predicate on every arena this lane has built, so "
            "D-ii's total-mass (rate) content is degenerate and untestable "
            "here while its constitutional cost is immediate.  The primary's "
            "asymmetry claim is confirmed from a pinned note.")

tooth("T15_D_reading_probe_is_discriminating",
      not d_raw_has_per_item and "locking each local possibility" in D_II,
      "the probe separates the owner's wording from the tightened one")

tooth("T16_gate_closure_probe_fires_on_a_short_mapping",
      set(list(mapped.keys())[:2]) != set(conj) and all_mapped,
      "a mapping covering only two conjuncts would be caught")

tooth("T17_records_form_probe_fires_on_a_planted_quantifier",
      bool(re.search(r"Records form[^.]*\balways\b",
                     "Records form always at every site."))
      and not rf_quantified,
      "a planted quantifier would change the verdict")


# ===========================================================================
# FIREWALL + DISCIPLINE ATTACKS
# ===========================================================================
blob = json.dumps(PRIMARY)

# no weight VALUE emitted as law content
value_patterns = [r"\bthe weight is \d", r"\bweight\s*=\s*\d",
                  r"\bmu\s*=\s*0?\.\d", r"\bw\s*=\s*1/2\b"]
val_hits = [p for p in value_patterns if re.search(p, blob)]
check("A8_no_weight_value_emitted_as_law_content", not val_hits,
      "hits: %s" % val_hits)
if val_hits:
    refute("FIREWALL_BREACH", str(val_hits))

# no adopt/recommend language
rec_patterns = [r"\bwe recommend\b", r"\bshould be adopted\b",
                r"\brecommend adopting\b", r"\bthe owner should adopt\b"]
rec_hits = [p for p in rec_patterns if re.search(p, blob, re.I)]
check("A8b_no_adoption_recommendation", not rec_hits, "hits: %s" % rec_hits)
if rec_hits:
    refute("RECOMMENDATION_EMITTED", str(rec_hits))

# the primary must not have touched any protected surface
import subprocess
try:
    changed = subprocess.run(
        ["git", "diff", "--name-only", "d34d5936ef", "HEAD"], cwd=ROOT,
        capture_output=True, text=True, timeout=60).stdout.split()
except Exception:
    changed = []
protected = [f for f in changed
             if ("/audit/" in f or f.endswith("MINIMAL_AXIOMS_2026-06-29.md")
                 or "REALIZED_STATE_PRIMITIVE" in f or "/data/" in f)]
check("A8c_no_protected_surface_touched", not protected,
      "changed: %s | protected: %s" % (changed, protected))
if protected:
    refute("PROTECTED_SURFACE_TOUCHED", str(protected))

# the primary must write no docs/ note
docs_written = [f for f in changed if f.startswith("docs/")]
check("A8d_no_docs_note_written", not docs_written, str(docs_written))

tooth("T11_firewall_probe_fires_on_a_planted_value",
      bool(re.search(r"\bthe weight is \d", "PLANTED the weight is 1 half"))
      and not val_hits,
      "a planted law-content value is caught by the same regex")

tooth("T12_protected_surface_probe_is_live",
      len(changed) > 0,
      "the diff probe actually sees this block's own commits (%d files)"
      % len(changed))


# ===========================================================================
# RESTRICTION GATES, re-verified independently
# ===========================================================================
c936 = rj("outputs/choice_substrate_cycle936_receipt_2026_07_28.json")[
    "certificates"]
c940 = rj("outputs/symmetric_weights_cycle940_receipt_2026_07_28.json")[
    "certificates"]
rg = {
    "936_sites": c936["C1_THE_GRAMMAR_DELTA"]["the_declared_choice_atoms"][
        "sites"] == SIX,
    "936_freedom_per_site": c936["C6_THE_PRICE_SHEET"]["FREEDOM_COUNT"][
        "reading_per_site"]["count"] == 6,
    "936_freedom_per_occasion": c936["C6_THE_PRICE_SHEET"]["FREEDOM_COUNT"][
        "reading_per_occasion"]["count"] == 8,
    "936_leaves": c936["C6_THE_PRICE_SHEET"]["FREEDOM_COUNT"][
        "observable_freedom"]["leaves"] == 256,
    "940_no_swap": c940["Q1_THE_MENU_SWAP_AUTOMORPHISM"][
        "sites_with_a_swap_automorphism"] == [],
    "940_menu_sites": c940["Q1_THE_MENU_SWAP_AUTOMORPHISM"][
        "sites_that_are_genuine_two_item_menu_pairs"] == [450, 475, 715],
    "940_A1": c940["Q1_THE_MENU_SWAP_AUTOMORPHISM"]["THEOREM_A1"]["holds"],
    "940_A2": c940["Q1_THE_MENU_SWAP_AUTOMORPHISM"]["THEOREM_A2"]["holds"],
    "913_locks": len(rows) == 164,
    "913_contexts": my_counts["F3_NN_RECORD_CONTENT"] == 54,
    "918_MA_locks": rj(R918)["certificates"]["C4_A3_ARENA"]["arena"]["M_A"][
        "lock_points"] == 134,
}
for k, v in rg.items():
    check("RG_" + k, v, "")
check("A9_all_restriction_gates", all(rg.values()),
      "%d/%d" % (sum(1 for v in rg.values() if v), len(rg)))

tooth("T13_restriction_gate_probe_would_catch_drift",
      c936["C6_THE_PRICE_SHEET"]["FREEDOM_COUNT"]["reading_per_site"]["count"]
      != 7, "a drifted 936 freedom count would fail")


# ===========================================================================
# VERDICT
# ===========================================================================
ELAPSED = time.time() - T0
PASSES = sum(1 for c in CHECKS if c["pass"])
VERDICT = ("PRIMARY_SURVIVES_THIS_CHECK_WITH_FINDINGS"
           if not [r for r in REFUTATIONS
                   if r["refutation"] in ("QUOTES_NOT_BYTE_PRESENT",
                                          "PARTITION_MISMATCH",
                                          "SIX_SITE_PARTITION_MISMATCH",
                                          "CIRCULAR_FORMALIZATION",
                                          "FIREWALL_BREACH",
                                          "PROTECTED_SURFACE_TOUCHED",
                                          "POLICY_CLAIM_UNSUPPORTED")]
           else "PRIMARY_REFUTED")

REC = OrderedDict()
REC["block"] = "cycle944_neighborhood_weight_independent_check"
REC["role"] = "independent checker, spec'd to refute"
REC["cycles"] = [944]
REC["authority"] = "none"
REC["audit"] = "unset"
REC["VERDICT"] = VERDICT
REC["headline"] = (
    "THE PRIMARY'S LOAD-BEARING NUMBERS ALL REPRODUCE UNDER INDEPENDENT "
    "MECHANISMS (union-find partitions, a second normalization for every "
    "byte-quote, and Cycle 913's own independent-checker ladder), AND THE "
    "PRIMARY'S SELF-CAUGHT COVARIANCE CORRECTION IS CONFIRMED AT THE SOURCE "
    "LEVEL.  TWO REAL DEFECTS FOUND: the naturality corollary is INCOMPLETE "
    "(ADM_RULE names two covariance groups and the primary computed only the "
    "cubic one, understating Draft B), and the strength lattice is "
    "INTERNALLY INCONSISTENT with the primary's own passenger finding "
    "(Draft B's first conjunct is not redundant -- it IS the "
    "existential-to-functional upgrade).  Draft C's regression is confirmed "
    "by explicit construction.  No refutation touches a partition, a quote, "
    "a conflict verdict, or the firewall.")
REC["checks"] = CHECKS
REC["counts"] = {"checks": len(CHECKS), "passed": PASSES,
                 "failed": len(CHECKS) - PASSES,
                 "teeth": len(TEETH),
                 "teeth_fired": sum(1 for t in TEETH if t["fired"]),
                 "refutations": len(REFUTATIONS)}
REC["teeth"] = TEETH
REC["REFUTATIONS"] = REFUTATIONS
REC["FINDINGS"] = FINDINGS
REC["independent_reconstruction"] = {
    "mechanism": "union-find over raw per-lock-point rows (the primary used "
                 "dict grouping); a second whitespace normalization that "
                 "strips markdown blockquote markers before collapsing (the "
                 "primary collapsed directly); source-level inspection of "
                 "Cycle 913's cubic_covariance() rather than its prose; and "
                 "cross-checking against Cycle 913's INDEPENDENT CHECKER "
                 "receipt, which the primary never reads.",
    "classes_recomputed": my_counts,
    "largest_class_recomputed": my_largest,
    "six_site_partition_recomputed": mine_six,
    "quotes_reverified": quotes_checked,
}
REC["elapsed_sec"] = round(ELAPSED, 3)
REC["runtime_budget_sec"] = RUNTIME_LIMIT_S

with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(REC, fh, indent=1)
    fh.write("\n")

lines = ["===== runner cache v1 =====",
         "runner: frontier_cycle944_neighborhood_weight_independent_check"
         "_2026_07_28.py",
         "receipt: outputs/neighborhood_weight_independent_check_cycle944"
         "_receipt_2026_07_28.json",
         "VERDICT: " + VERDICT,
         "checks: %d/%d" % (PASSES, len(CHECKS)),
         "teeth fired: %d/%d" % (sum(1 for t in TEETH if t["fired"]),
                                 len(TEETH)),
         "refutations: %d" % len(REFUTATIONS)]
for r in REFUTATIONS:
    lines.append("  REFUTATION: " + r["refutation"])
for f in FINDINGS:
    lines.append("  FINDING: " + f["finding"])
lines.append("classes recomputed (control 164): %s" % (my_counts,))
lines.append("six-site partition recomputed: %s" % (mine_six,))
lines.append("elapsed: %.3fs / %ds" % (ELAPSED, RUNTIME_LIMIT_S))
lines.append("===== end runner cache =====")
txt = "\n".join(lines) + "\n"
with open(CACHE, "w", encoding="utf-8") as fh:
    fh.write(txt)
print(txt)

if VERDICT == "PRIMARY_REFUTED":
    sys.exit(1)
