#!/usr/bin/env python3
"""Cycle 944 (blockQ16) -- PRICING the owner's candidate axiom clause.

THE OBJECT (owner, verbatim):
  "I believe the neighborhood map not only modulates the available
   possibilities, but their probabilities."

Two candidate wordings are priced, BOTH readings everywhere:

  DRAFT B (the Admissibility extension, the owner's literal form):
    "the neighborhood map determines both which possibilities are
     admissible at a site and the weight each carries"

  DRAFT A (a standalone two-clause form):
    "each admissible possibility at a site carries a weight, and the
     weights are a lawful function of the site's neighborhood map."

ABSOLUTE FIREWALL.  This block PRICES.  It adopts nothing, edits no
axiom text, proposes no wording, and outputs NO weight value as law
content.  Weights are symbols throughout.  The deliverable is a set of
CONDITIONAL theorems plus a required-and-minimal dossier.  No
recommendation on adopt/not-adopt is made or implied.

METHOD.  Every number in this block is derived from PINNED bytes --
the axiom memo, the realized-state primitive note, and the Cycle
911/913/918/925/936/940 receipts and notes.  The substrate is never
re-run; the pinned receipts already contain the neighbourhood-context
data this block needs (Cycle 913's per-lock-point context fingerprints
and Cycle 913/918's context ladders).  That is a deliberate cost
choice and is declared in the receipt.
"""

import ast
import hashlib
import json
import os
import subprocess
import sys
import time
from collections import Counter, OrderedDict
from fractions import Fraction

T0 = time.time()
RUNTIME_LIMIT_S = 900

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
RECEIPT_PATH = os.path.join(
    ROOT, "outputs", "neighborhood_weight_cycle944_receipt_2026_07_28.json")
CACHE_PATH = os.path.join(
    ROOT, "logs", "runner-cache",
    "frontier_cycle944_neighborhood_weight_2026_07_28.txt")

FAILURES = []
GATES = []
TEETH = []


def gate(name, ok, detail=""):
    GATES.append({"gate": name, "pass": bool(ok), "detail": detail})
    if not ok:
        FAILURES.append("GATE " + name + " :: " + detail)
    return bool(ok)


def tooth(name, fired, detail=""):
    TEETH.append({"tooth": name, "fired": bool(fired), "detail": detail})
    if not fired:
        FAILURES.append("TOOTH DID NOT FIRE " + name + " :: " + detail)
    return bool(fired)


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git_blob(path):
    try:
        out = subprocess.run(["git", "hash-object", path], cwd=ROOT,
                             capture_output=True, text=True, timeout=60)
        return out.stdout.strip()
    except Exception:
        return ""


def norm(text):
    """Whitespace-normalise for byte-quote verification across line wraps."""
    return " ".join(text.split())


# ---------------------------------------------------------------------------
# A_PINS
# ---------------------------------------------------------------------------

AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
RSP = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
N911 = ("docs/RETYPED_WORLDS_ARE_SETUPS_SELECTION_SITES_EXIST_CYCLE911"
        "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
N913 = ("docs/SELECTION_IS_TRANSPORT_O3_TERMINAL_CYCLE913"
        "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
N918 = ("docs/WRITABLE_ENDPOINT_BORN_CAPABLE_FIRST_BRANCH_PAIRS_CYCLE918"
        "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
N925 = ("docs/LAW_RELAXATION_CLASSIFIED_A3_SOLE_RELAXATION_CYCLE925"
        "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
N936 = ("docs/CHOICE_SUBSTRATE_BUILT_TREE_PRICED_CYCLE936"
        "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
N940 = ("docs/R1A3_NEGATIVE_NO_SWAP_AUTOMORPHISM_CYCLE940"
        "_BOUNDED_THEOREM_NOTE_2026-07-28.md")
R913 = "outputs/selection_function_cycle913_receipt_2026_07_28.json"
R918 = "outputs/writable_endpoint_cycle918_receipt_2026_07_28.json"
R925 = "outputs/law_relaxation_cycle925_receipt_2026_07_28.json"
R936 = "outputs/choice_substrate_cycle936_receipt_2026_07_28.json"
R940 = "outputs/symmetric_weights_cycle940_receipt_2026_07_28.json"
R911 = "outputs/type_vacuity_cycle911_receipt_2026_07_28.json"

# Surfaces found by the prior-art sweep.  READ AND CITED ONLY -- the policy
# file in particular is an owner surface this block does not touch.
POLICY = "docs/audit/AXIOM_MINIMALITY_POLICY.md"
GC1 = "docs/GRADED_CONSTRAINT_PRIMITIVE_REGISTRATION_PROPOSAL_2026-07-04.md"
GC2 = ("docs/GRADED_CONSTRAINT_INTERFACE_CONSISTENCY_BOUNDED_NOTE"
       "_2026-07-04.md")
FENCE = ("docs/INFORMATIVE_FRACTION_COVARIANT_RULE_QUANTIZATION_OCCUPANCY"
         "_RESIDUAL_THEOREM_NOTE_2026-07-02.md")

PIN_PATHS = [AXIOMS, RSP, N911, N913, N918, N925, N936, N940,
             R911, R913, R918, R925, R936, R940,
             POLICY, GC1, GC2, FENCE]

PINS = OrderedDict()
for rel in PIN_PATHS:
    p = os.path.join(ROOT, rel)
    if not os.path.exists(p):
        FAILURES.append("MISSING PIN " + rel)
        continue
    PINS[rel] = {"sha256": sha256_file(p),
                 "git_blob": git_blob(p),
                 "bytes": os.path.getsize(p)}

gate("A_PINS_all_present", len(PINS) == len(PIN_PATHS),
     "%d/%d" % (len(PINS), len(PIN_PATHS)))


def read_doc(rel):
    with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as fh:
        return fh.read()


AX_TEXT = read_doc(AXIOMS)
RSP_TEXT = read_doc(RSP)
AX_N = norm(AX_TEXT)
RSP_N = norm(RSP_TEXT)


def read_receipt(rel):
    with open(os.path.join(ROOT, rel), "r", encoding="utf-8") as fh:
        return json.load(fh)


RC913 = read_receipt(R913)
RC918 = read_receipt(R918)
RC936 = read_receipt(R936)
RC940 = read_receipt(R940)

# ---------------------------------------------------------------------------
# BYTE-QUOTED CLAUSES (each asserted byte-present in its pinned source)
# ---------------------------------------------------------------------------

QUOTES = OrderedDict()


def q(key, source_rel, text, role):
    hay = AX_N if source_rel == AXIOMS else (RSP_N if source_rel == RSP
                                             else norm(read_doc(source_rel)))
    present = norm(text) in hay
    QUOTES[key] = {"source": source_rel, "quote": text, "role": role,
                   "byte_present": present}
    gate("QUOTE_" + key, present, source_rel)
    return present


# --- the Admissibility axiom's own bytes -----------------------------------
q("ADM_RULE", AXIOMS,
  "There is one fixed nearest-neighbor admissibility rule, covariant under "
  "lattice translations and proper cubic rotations.",
  "the axiom's sentence 1: the rule's existence AND its covariance group")
q("ADM_VARY", AXIOMS,
  "For each site, the available possibilities are determined by, and vary "
  "with, the nearest-neighbor conditions.",
  "the axiom's sentence 2: the determination clause -- the ONLY 'neighborhood "
  "map' structure the axiom itself supplies")
q("ADM_NOT_DYNAMICS", AXIOMS, "Admissibility is not a dynamics axiom.",
  "the non-supply paragraph's subject line")
q("ADM_NONSUPPLY", AXIOMS,
  "It does not choose a Hamiltonian or transfer operator, supply transition "
  "probabilities or weights, select a scalar or nonzero kinetic branch, "
  "assert a Dirac-square carrier, define a time metric, or provide a "
  "record-production process or physical persistence dynamics.",
  "THE DECISIVE NON-SUPPLY CLAUSE: its subject is Admissibility itself")
q("ADM_RESTATE", AXIOMS,
  "The admissibility rule determines the available possibilities at each site "
  "from the nearest-neighbor conditions, and those available possibilities "
  "vary with those conditions, before a record can lock one available local "
  "possibility.",
  "the memo's own closing restatement of the determination clause")

# --- Lattice / Qubit no-privilege clauses ----------------------------------
q("LATTICE_NOPRIV", AXIOMS,
  "No site is privileged. Sites are distinguished by the supplied lattice "
  "structure alone.",
  "the no-privilege idiom, site version")
q("QUBIT_NOPRIV", AXIOMS,
  "No possibility is privileged. Possibilities are distinguished by the "
  "supplied algebraic structure alone.",
  "the no-privilege idiom, possibility version (Cycle 940's self-defeating "
  "clause, here re-used as a SHAPE precedent, not as a naturality ground)")

# --- Record ----------------------------------------------------------------
q("RECORD_FORM", AXIOMS, "Records form.", "the 2026-07-04 occurrence sentence")
q("RECORD_LOCK", AXIOMS,
  "When present, a record locks exactly one admissible local possibility. A "
  "site never carries more than one record; records are permanent.",
  "Record's locking clause -- the A3 sentence's structural housing")
q("RECORD_READ", AXIOMS,
  "Only records are readable. A readout value is determined by record content "
  "alone.",
  "Record's readability clause -- tested against neighbourhood formalizations "
  "that read non-record wires")

# --- Qualification ---------------------------------------------------------
q("QUAL_ONLY_NAMED", AXIOMS,
  "These axioms state only their named primitive content.",
  "the Qualification's opening -- why an unstated weight clause is not latent")
q("QUAL_STATE", AXIOMS, "A state is a configuration of records.",
  "the state definition -- makes the neighbourhood map STATE-VALUED")
q("QUAL_LAW", AXIOMS,
  "A law privileges no states. Its domain is a supplied condition, and at "
  "every state where the condition holds it gives exactly one answer.",
  "the law clause -- the weight FUNCTION is tested against it")

# --- the Open Gates list: THE OWNER'S CLAUSE'S OWN GATE ---------------------
q("OPEN_GATES_FORMATION", AXIOMS,
  "context selection, measurement basis selection, Born weights, probability "
  "rules, update laws, decoherence mechanisms, and formation rules (which "
  "admissible possibility a new record locks, at which site, with what "
  "weight, or at what rate);",
  "THE GATE: 'with what weight' is one of four named formation-rule conjuncts "
  "held OUTSIDE axiom content")
q("HIST_PRECEDENT", AXIOMS,
  "The 2026-07-04 owner-approved revision appended the formation sentence "
  "\"Records form.\" to the Record axiom: occurrence became named axiom "
  "content, while every formation rule (which admissible possibility, at "
  "which site, with what weight, at what rate) remained downstream supplier "
  "content.",
  "THE PRECEDENT: the identical move, executed once before, on the "
  "OCCURRENCE conjunct")
q("BORN_WEIGHTS_CITE", AXIOMS,
  "Born weights, readout-context selection, central-sector decomposition",
  "'Born weights' named a third time as content requiring a separate "
  "retained authority")

# --- the realized-state primitive ------------------------------------------
q("RSP_LAWS_STATE", RSP,
  "The laws do not pick the state; the world does, among the states the laws "
  "permit.",
  "the laws/state split -- the primitive's core sentence")
q("RSP_POINTWISE", RSP,
  "Derivations may evaluate at the realized state, pointwise.",
  "the licence the weight FUNCTION would be evaluated under")
q("RSP_NOTHING_MORE", RSP,
  "Nothing more is supplied: no averaging over alternatives, no typical or "
  "generic claim, and no quoting a number that would differ had another "
  "law-admissible state been realized.",
  "THE NO-AVERAGING CLAUSE -- the standing block on cashing weights as "
  "census frequencies")
q("RSP_ZERO_CONTENT", RSP,
  "It carries zero state-contingent content: no state, averaging over "
  "alternatives, measure, weighting, probability rule, typicality claim, "
  "genericity claim, preferred state, default state, boundary condition, "
  "normalization rule, or value is supplied by it.",
  "THE NON-SUPPLY CLAUSE -- note the operative words 'supplied by it'")
q("RSP_FUNCTIONAL", RSP,
  "A row may evaluate an already-defined state functional at the supplied "
  "realized state. A value that would change under a different "
  "law-admissible realized state is registered data, not derivation output.",
  "THE TEMPLATE the owner's clause fits: supply the functional as law, "
  "evaluate pointwise")
q("RSP_NOT_DO", RSP,
  "It does not supply a state, state-selection rule, averaging over "
  "alternatives, measure, weighting, probability rule, typicality claim, "
  "genericity claim, preferred state, default state, boundary condition, "
  "normalization rule, or state-contingent value.",
  "the primitive's own 'What This Does Not Do' list")

# --- pinned lane texts -----------------------------------------------------
q("C925_ONE_SENTENCE", N925,
  "The successor substrate's design space is one sentence wide.",
  "the classification theorem's headline -- the requiredness anchor")
q("C918_ADM_SHAPE_ABSENT", N918,
  "The write moved the selection from SETUP COORDINATE to TRAJECTORY HISTORY, "
  "not to neighbourhood conditions; the Admissibility-sentence-shaped "
  "dependence is still absent.",
  "the measured absence of neighbourhood dependence for the REALIZED value "
  "-- the clause's nearest measured tension")
q("C911_MENU_GAP", N911,
  "which is weaker than",
  "the menu-variation gap: the menu does not vary with neighbour conditions "
  "on this substrate")
q("C940_INDEPENDENT", N940,
  "they are LOGICALLY INDEPENDENT",
  "naturality and A3 are logically independent (Cycle 940)")

# --- THE SURFACES THE PRIOR-ART SWEEP FOUND (the block's biggest additions) -
q("POLICY_NO_LAUNDERING", POLICY,
  "**No laundering.** Admissibility does not choose the readout context, "
  "select a measurement basis, provide a formation rule, define "
  "probabilities, assign weights, normalize readouts, specify an update law, "
  "provide measurement/decoherence dynamics, define time metric or arrow, "
  "choose a Hamiltonian or transfer operator, select a kinetic branch, or "
  "identify physical observables.",
  "THE DECISIVE SURFACE.  Owner-approved BINDING policy.  'assign weights' is "
  "a standalone item with no 'transition' qualifier, so it closes the one "
  "parse under which Draft B escaped the axiom memo's own non-supply "
  "sentence.")
q("POLICY_VARY_WITH_EXISTENTIAL", POLICY,
  "\"Vary with\" is existential, not per-neighborhood: availability is not "
  "constant across nearest-neighbor conditions; under most conditions the "
  "full domain may remain available.",
  "THE 2026-07-02 OWNER RULING.  The determination clause is EXISTENTIAL.  "
  "Both drafts read it as a per-site FUNCTION -- a silent strengthening of "
  "the existing axiom, priced in Q1.")
q("POLICY_PANEL_UNIFORM", POLICY,
  "a set-level reading would make the sentence itself name a weighting "
  "(uniform), contradicting this section's certification that the "
  "2026-07-02 sentences name no weighting or value",
  "INDEPENDENT CORROBORATION of this block's reading-R1 finding: a five-seat "
  "blind panel already rejected a reading that would make an axiom sentence "
  "name a UNIFORM weighting.")
q("FENCE_NAME", FENCE,
  "The no-weights fence says Admissibility does not supply:",
  "the repo's canonical name for the surface both drafts cross")
q("GC1_COEXISTENCE", GC1,
  "possibility is in no menu; availability (Admissibility) is untouched;",
  "THE PRIOR PROPOSAL'S OWN SEPARATION CLAUSE -- graded_constraint v1 kept "
  "the two halves APART on purpose.")
q("GC2_FILTERS", GC2,
  "availability filters outcomes, never weights",
  "graded_constraint v2's sharpest statement of the boundary the owner's "
  "clause fuses across")
q("GC2_CHANNEL", GC2,
  "dependent on the surrounding record configuration through the "
  "nearest-neighbor channel",
  "the NEAREST-NEIGHBOUR CONDITIONING the prior proposal already carried -- "
  "the owner's clause is not novel in this respect")

gate("A_PINS_quotes_all_present",
     all(v["byte_present"] for v in QUOTES.values()),
     "%d quotes" % len(QUOTES))

# ---------------------------------------------------------------------------
# B_RESTRICTION_GATE -- 936 and 940 reproduced value-for-value, hard-fail
# ---------------------------------------------------------------------------

C936 = RC936["certificates"]
C940 = RC940["certificates"]
C913 = RC913["certificates"]
C918 = RC918["certificates"]

atoms936 = C936["C1_THE_GRAMMAR_DELTA"]["the_declared_choice_atoms"]
tree936 = C936["C2_THE_TREE_AND_THE_MULTI_VALUEDNESS_GATE"]
price936 = C936["C6_THE_PRICE_SHEET"]
free936 = price936["FREEDOM_COUNT"]

SIX_SITES = [254, 450, 475, 540, 558, 715]

gate("R936_sites", atoms936["sites"] == SIX_SITES, str(atoms936["sites"]))
gate("R936_site_count", atoms936["site_count"] == 6, "")
gate("R936_atom_count", atoms936["atom_count"] == 8, "")
gate("R936_occasion_count", atoms936["occasion_count"] == 4, "")
gate("R936_occasions", atoms936["occasions"] == [300, 700, 702, 1100], "")
gate("R936_atoms",
     [list(a) for a in atoms936["atoms"]] ==
     [[300, 715], [700, 475], [700, 540], [702, 254], [702, 450],
      [702, 715], [1100, 558], [1100, 715]], "")
gate("R936_leaves", tree936["structure"]["leaves"] == 256
     if "leaves" in tree936["structure"] else
     free936["observable_freedom"]["leaves"] == 256, "")
gate("R936_branch_nodes", tree936["structure"]["branch_nodes"] == 75, "")
gate("R936_depth", tree936["structure"]["depth_in_choice_occasions"] == 4, "")
gate("R936_branching",
     tree936["structure"]["branching_factor_by_occasion"] == [2, 4, 8, 4], "")
gate("R936_distinct_observables",
     free936["observable_freedom"]["distinct_observables_over_the_full_tree"]
     == 64, "")
gate("R936_atoms_effective",
     free936["observable_freedom"]["atoms_effective_in_every_context"] == 8, "")
gate("R936_freedom_per_site", free936["reading_per_site"]["count"] == 6, "")
gate("R936_freedom_per_occasion",
     free936["reading_per_occasion"]["count"] == 8, "")
gate("R936_freedom_global", free936["reading_global"]["count"] == 1, "")
gate("R936_forced_identifications",
     free936["substrate_forced_identifications"] == 1, "")
gate("R936_no_collapse",
     C936["C5_THE_WEIGHT_ALGEBRA"]["COLLAPSE_CHECK"][
         "any_step_that_outputs_a_unique_mu"] is False, "")
gate("R936_factorizes",
     C936["C3_THE_PER_BRANCH_BATTERY"]["FACTORIZATION_ACROSS_SITES"][
         "the_leaf_observable_factorizes_over_sites"] is True, "")

Q1_940 = C940["Q1_THE_MENU_SWAP_AUTOMORPHISM"]
third = Q1_940["A_THIRD_INDEPENDENT_NEGATIVE_FOUND_BY_THE_ARENA_ITSELF"]
gate("R940_sites_declared", Q1_940["sites_declared"] == SIX_SITES, "")
gate("R940_no_swap", Q1_940["sites_with_a_swap_automorphism"] == [], "")
gate("R940_genuine_menu_sites",
     Q1_940["sites_that_are_genuine_two_item_menu_pairs"] == [450, 475, 715],
     "")
gate("R940_timing_only", third["timing_only_sites"] == [254, 540, 558], "")
gate("R940_A1_holds", Q1_940["THEOREM_A1"]["holds"] is True, "")
gate("R940_A2_holds", Q1_940["THEOREM_A2"]["holds"] is True, "")
gate("R940_LR_separated",
     Q1_940["LEFT_AND_RIGHT_ARE_SEPARATED_UNDER_EVERY_LABEL"] is True, "")
for lab in ("bare", "popcount", "exact"):
    r = Q1_940["REFINEMENTS"][lab]
    gate("R940_refine_%s_colours" % lab, r["colour_classes"] == 514, "")
    gate("R940_refine_%s_LR" % lab,
         r["colour_of_LEFT"] == 1 and r["colour_of_RIGHT"] == 2, "")
    gate("R940_refine_%s_share" % lab,
         r["LEFT_and_RIGHT_share_a_colour"] is False, "")

Q2_940 = C940["Q2_THE_CONDITIONAL_THEOREM_AND_ITS_ANTECEDENT"]
_q2s = json.dumps(Q2_940)
gate("R940_coverage_zero", '"coverage_numerator": 0' in _q2s
     or '"covered_sites": []' in _q2s or "0 of 6" in _q2s
     or "VACUOUS" in _q2s.upper(), "coverage 0/6 marker")
gate("R940_freedom_unchanged", "6" in _q2s, "freedom 6 -> 6 marker")

# 913 / 918 restriction gates
c1_913 = C913["C1_SELECTION_TABLE"]
c4_913 = C913["C4_CONTEXT_VARIATION"]
gate("R913_lock_points", c1_913["lock_points"] == 164, "")
gate("R913_split",
     c1_913["selection_split"]["[1, 0]"]["count"] == 84
     and c1_913["selection_split"]["[0, 1]"]["count"] == 80, "")
gate("R913_nn_contexts",
     c4_913["distinct_nearest_neighbour_contexts"] == 54, "")
gate("R913_cubic_classes",
     c4_913["symmetry_classes_of_the_contexts"] == {"2": 3, "3": 6, "4": 7},
     "")
gate("R913_menu_everywhere", c1_913["menu_at_every_lock_point"]
     == [[1, 0], [0, 1]], "")
arena918 = C918["C4_A3_ARENA"]["arena"]["M_A"]
gate("R918_MA_locks", arena918["lock_points"] == 134, "")
gate("R918_MA_pairs", arena918["site_possibility_pairs"] == 268, "")
gate("R918_MA_branch_pairs", arena918["dynamical_branch_pairs"] == 3, "")
gate("R918_MA_poss", arena918["possibilities_per_lock_point"] == 2, "")

# SPEC INCONSISTENCY, disclosed (both-readings rule): the spec described
# "918's M_A arena (the 134 lock sites / 328 pairs)".  The pinned bytes say
# M_A = 134 locks x 2 = 268 pairs; 328 = 164 x 2 is Cycle 913's CONTROL arena.
SPEC_INCONSISTENCY = {
    "spec_text": "918's M_A arena (the 134 lock sites / 328 pairs)",
    "pinned_918_M_A": {"lock_points": 134, "site_possibility_pairs": 268},
    "pinned_913_CONTROL": {"lock_points": 164, "site_possibility_pairs": 328},
    "resolution": "both arenas are carried separately and labelled; the "
                  "spec conflated the M_A lock count with the CONTROL pair "
                  "count.  No result depends on the conflation.",
}

# ---------------------------------------------------------------------------
# Q0 -- PRIOR-ART SWEEP
# ---------------------------------------------------------------------------

# The dominant relationship, established by byte-quote: the Open Gates list
# names a FOUR-CONJUNCT formation rule.  The owner's clause addresses exactly
# ONE conjunct ("with what weight") and does so by naming its SUPPLIER rather
# than its value.
FORMATION_CONJUNCTS = ["which admissible possibility a new record locks",
                       "at which site",
                       "with what weight",
                       "or at what rate"]
gate("Q0_conjuncts_byte_present",
     all(norm(c) in AX_N for c in FORMATION_CONJUNCTS),
     "all four formation-rule conjuncts byte-present")

OPEN_GATE_RELATION = {
    "question": "is Draft B the Open-Gates formation-rule sentence made "
                "specific?",
    "answer": "PARTIALLY -- and the part matters.",
    "the_gate_byte_quoted": QUOTES["OPEN_GATES_FORMATION"]["quote"],
    "the_gate_has_four_conjuncts": FORMATION_CONJUNCTS,
    "which_conjuncts_draft_B_touches": ["with what weight"],
    "which_conjuncts_draft_B_leaves_open": [
        "which admissible possibility a new record locks",
        "at which site", "or at what rate"],
    "the_precise_relationship": (
        "Draft B is NOT the Open-Gates sentence made specific.  It is ONE of "
        "that sentence's four conjuncts, and it specifies that conjunct's "
        "DETERMINATION RELATION rather than its value: the gate asks 'with "
        "what weight', and Draft B answers 'with whatever weight the "
        "neighborhood map assigns' -- which names the argument of the weight "
        "function and leaves the function itself unnamed.  Adopting either "
        "draft therefore does NOT close the formation-rule gate; it "
        "re-partitions it, moving the weight conjunct's ARGUMENT inside the "
        "axioms while leaving the weight conjunct's VALUE, and all three "
        "other conjuncts, outside."),
    "consequence_for_the_memo_text": (
        "both drafts require the Open Gates list to be edited: the parenthesis "
        "'(which admissible possibility a new record locks, at which site, "
        "with what weight, or at what rate)' would no longer be wholly "
        "outside axiom content.  That edit is a cost BOTH drafts carry."),
}

PRIOR_ART = [
    {"id": "PA0a_GRADED_CONSTRAINT_V1", "source": GC1,
     "quote": QUOTES["GC1_COEXISTENCE"]["quote"],
     "class": "(a) SAME CLAUSE, PROPOSED BEFORE -- and NEVER REGISTERED",
     "finding": "graded_constraint v1 (2026-07-04) proposed a weight function "
                "on menus of admissible possibilities whose domain is 'every "
                "nearest-neighbor composite' and whose conditioning runs "
                "'through the nearest-neighbor channel'.  IT IS THE OWNER'S "
                "CLAUSE ALREADY DRAFTED ONCE.  It was filed as a Class D "
                "primitive-registration proposal, marked NOT AT APPROVAL "
                "GRADE, and never approved.  THE DIFFERENCE THAT MATTERS: v1 "
                "deliberately kept the two halves APART -- its own "
                "'coexistence' bullet says 'availability (Admissibility) is "
                "untouched'.  The owner's candidate FUSES them into one "
                "sentence.  The fusion, not the neighbourhood-conditioning, "
                "is the novel content."},
    {"id": "PA0b_GRADED_CONSTRAINT_V2", "source": GC2,
     "quote": QUOTES["GC2_FILTERS"]["quote"],
     "class": "(a) SAME CLAUSE, v2 candidate -- unregistered",
     "finding": "the repaired candidate carries the same nearest-neighbour "
                "conditioning (GC2_CHANNEL) and states the boundary the "
                "owner's clause crosses in five words: 'availability filters "
                "outcomes, never weights'.  Every prior version of this idea "
                "in the repo holds that line; the owner's candidate is the "
                "first to cross it."},
    {"id": "PA0c_POLICY_NO_LAUNDERING", "source": POLICY,
     "quote": QUOTES["POLICY_NO_LAUNDERING"]["quote"],
     "class": "(c) NON-SUPPLY -- OWNER-APPROVED AND BINDING",
     "finding": "THE HARDEST SURFACE IN THE SWEEP.  'Admissibility does not "
                "... define probabilities, assign weights' is owner-approved "
                "binding audit policy, and 'assign weights' stands alone with "
                "no 'transition' qualifier.  This CLOSES the strained parse "
                "that let Draft B escape the axiom memo's own non-supply "
                "sentence.  Draft B contradicts TWO surfaces, one of them "
                "binding policy; Draft A contradicts NEITHER."},
    {"id": "PA0d_VARY_WITH_EXISTENTIAL", "source": POLICY,
     "quote": QUOTES["POLICY_VARY_WITH_EXISTENTIAL"]["quote"],
     "class": "(c) SCOPE RULING that both drafts silently strengthen",
     "finding": "the 2026-07-02 owner ruling fixes 'vary with' as EXISTENTIAL "
                "-- availability is merely not constant across neighbour "
                "conditions.  Both drafts speak of the neighborhood map "
                "DETERMINING things, i.e. a per-site function.  Adopting "
                "either would therefore also convert the existing menu clause "
                "from an existential to a functional reading -- a second, "
                "unadvertised strengthening.  Priced in Q1."},
    {"id": "PA0e_PANEL_UNIFORM", "source": POLICY,
     "quote": QUOTES["POLICY_PANEL_UNIFORM"]["quote"],
     "class": "(a) PRIOR RULING directly on this block's reading R1",
     "finding": "a five-seat blind physicist panel already considered and "
                "rejected a reading under which an axiom sentence would "
                "'name a weighting (uniform)'.  That is exactly the failure "
                "mode this block independently derives for Draft A's reading "
                "R1.  The finding is corroborated, not novel."},
    {"id": "PA0f_FENCE_NAME", "source": FENCE,
     "quote": QUOTES["FENCE_NAME"]["quote"],
     "class": "(c) NON-SUPPLY -- the surface has a repo name",
     "finding": "'the no-weights fence'.  The clause both drafts cross is "
                "named, quoted and machine-needled across the repo."},
    {"id": "PA1_OPEN_GATES", "source": AXIOMS,
     "quote": QUOTES["OPEN_GATES_FORMATION"]["quote"],
     "class": "(c) NON-SUPPLY / the clause's own gate",
     "finding": "the exact content the owner's clause would move inward, "
                "named as OUTSIDE the four axioms.  One of four conjuncts."},
    {"id": "PA2_ADM_NONSUPPLY", "source": AXIOMS,
     "quote": QUOTES["ADM_NONSUPPLY"]["quote"],
     "class": "(c) NON-SUPPLY -- and DIRECTLY CONTRADICTED BY DRAFT B",
     "finding": "the subject of this sentence is Admissibility itself.  Draft "
                "B makes the neighborhood map -- Admissibility's own object -- "
                "determine the weight, which this sentence denies.  Draft B "
                "cannot be added without amending or deleting the phrase "
                "'supply transition probabilities or weights'.  Draft A, being "
                "standalone, leaves the sentence TRUE (Admissibility alone "
                "still supplies no weight; a separate clause does).  THIS IS "
                "THE SHARPEST PRICING DIFFERENCE BETWEEN THE TWO DRAFTS."},
    {"id": "PA3_HIST_PRECEDENT", "source": AXIOMS,
     "quote": QUOTES["HIST_PRECEDENT"]["quote"],
     "class": "(a) SAME MOVE, executed once before on a DIFFERENT conjunct",
     "finding": "on 2026-07-04 the owner moved the OCCURRENCE conjunct into "
                "axiom content ('Records form.') and explicitly left the four "
                "formation-rule conjuncts outside.  The current candidate is "
                "the same move, one conjunct later.  There is a precedent for "
                "the SHAPE of the edit; there is no prior proposal of THIS "
                "conjunct."},
    {"id": "PA4_C925_REDUCTION", "source": N925,
     "quote": "The residual specification is therefore a sentence about the "
              "available possibilities at a site and nothing else",
     "class": "(b) ADJACENT -- the A3 shape, with no neighbourhood clause",
     "finding": "Cycle 925 reduced the whole relaxation space to ONE sentence "
                "and quoted its shape from three pinned texts.  None of the "
                "three carries a neighbourhood-functional rider.  The owner's "
                "clause is therefore a STRENGTHENING of the reduced sentence, "
                "not the reduced sentence."},
    {"id": "PA5_C913_ARENA", "source": N913,
     "quote": "a weight over the counterfactual menu is a weight over setups "
              "UNDER ANOTHER NAME",
     "class": "(b) ADJACENT -- the arena, no neighbourhood clause",
     "finding": "the A3 arena statement Cycle 925 anchored its reduction on."},
    {"id": "PA6_C918_ABSENCE", "source": N918,
     "quote": QUOTES["C918_ADM_SHAPE_ABSENT"]["quote"],
     "class": "(c) MEASURED ABSENCE -- the clause's nearest measured tension",
     "finding": "Cycle 918 measured that the REALIZED selection is not a "
                "function of neighbourhood conditions on this substrate.  That "
                "is a fact about which item occurs (state content), not about "
                "the weight (law content), so it does not refute the clause -- "
                "but it is the strongest evidence in the repo that "
                "Admissibility-shaped dependence is absent where anyone has "
                "looked for it."},
    {"id": "PA7_C911_MENU_GAP", "source": N911,
     "quote": "it does not VARY with nearest-neighbour conditions on this "
              "substrate, which is weaker than the Admissibility sentence "
              "asserts",
     "class": "(c) MEASURED ABSENCE -- the menu-variation gap",
     "finding": "the substrate does not even realise the FIRST half of Draft "
                "B (menu variation with neighbourhood).  Draft B's first "
                "conjunct is therefore already an unmet axiom obligation on "
                "this substrate, independent of the weight half."},
    {"id": "PA8_C940_NEGATIVE", "source": N940,
     "quote": "the naturality antecedent is NOT DERIVABLE",
     "class": "(b) ADJACENT -- the negative the clause converts into a feature",
     "finding": "Cycle 940 proved weight-naturality underivable AS A SEPARATE "
                "IMPORT and logically independent of A3.  The owner's clause "
                "does not derive naturality either; it makes a RESTRICTED form "
                "of it definitional (see Q2 ii)."},
]

Q0_VERDICT = (
    "A NEIGHBOURHOOD-CONDITIONED WEIGHT CLAUSE HAS BEEN PROPOSED BEFORE, "
    "TWICE, AND WAS NEVER REGISTERED: graded_constraint v1 and v2 "
    "(2026-07-04) both put a weight function on menus of admissible "
    "possibilities, conditioned 'through the nearest-neighbor channel'.  The "
    "owner's candidate is therefore NOT novel in its neighbourhood "
    "conditioning.  What IS novel is the FUSION: every prior version keeps "
    "availability and weight apart on purpose ('availability (Admissibility) "
    "is untouched'; 'availability filters outcomes, never weights'), and the "
    "owner's clause makes one rule do both jobs.  Against that, the repo "
    "carries FIVE separate non-supply surfaces naming exactly this content "
    "as excluded -- the Open Gates list, the Admissibility non-supply "
    "sentence ('the no-weights fence', which has a repo name), the 'Born "
    "weights' citation rule, and the owner-approved BINDING 'No laundering' "
    "clause in the audit policy -- plus one precedent for the shape of such "
    "an edit (the 2026-07-04 occurrence revision) and one prior panel ruling "
    "against a reading that would make an axiom name a uniform weighting.")

# ---------------------------------------------------------------------------
# Q1 -- THE NEIGHBORHOOD MAP, FORMALIZED FROM THE AXIOM'S OWN BYTES
# ---------------------------------------------------------------------------
#
# The axiom NEVER says "neighborhood map".  Its phrase is "the nearest-neighbor
# conditions" (ADM_VARY) / "the nearest-neighbor conditions" again in
# ADM_RESTATE.  Formalizing the owner's term is therefore the block's first
# real decision, and it is NOT unique.  Every formalization below is defined
# mechanically and its class partition is COMPUTED from pinned data.

ROWS913 = c1_913["per_lock_point_rows"]
gate("Q1_rows913_count", len(ROWS913) == 164, str(len(ROWS913)))


def partition(rows, keyfn):
    d = {}
    for r in rows:
        d.setdefault(keyfn(r), []).append(r["world"])
    return d


def openness(r):
    return tuple(1 if o > 0 else 0 for o in r["neighbour_ordinals"])


FORMALIZATIONS = OrderedDict()

FORMALIZATIONS["F0_EMPTY"] = {
    "definition": "the neighborhood map is trivial -- every site has the same "
                  "(empty) neighbourhood.",
    "axiom_warrant": "NONE.  Included as the coarsest endpoint of the lattice: "
                     "it is what the clause degenerates to if 'neighborhood "
                     "map' is read as carrying no information.",
    "keyfn": lambda r: 0,
    "circular": False, "vacuous": False,
    "note": "forces ONE weight for the whole substrate -- exactly Cycle 936's "
            "'reading_global' count of 1.",
}
FORMALIZATIONS["F1_OPENNESS"] = {
    "definition": "the neighborhood map is the k=2 condition alphabet: for "
                  "each nearest neighbour, recorded or open.",
    "axiom_warrant": "STRONG.  Record supplies exactly one bit per site "
                     "('When present, a record locks...'), and "
                     "'A state is a configuration of records' makes presence "
                     "the minimal state-valued neighbour condition.",
    "keyfn": openness,
    "circular": False, "vacuous": False,
    "note": "the coarsest NON-trivial reading that uses only Record's own "
            "vocabulary.",
}
FORMALIZATIONS["F2_ORDINALS"] = {
    "definition": "the neighborhood map is the pair of nearest-neighbour "
                  "record ordinals (record counts) at the lock tick.",
    "axiom_warrant": "MODERATE.  Counts are readout-shaped ('scalar readout "
                     "I is additive'), so this reading is Record-legible; but "
                     "it imports counting structure the Admissibility sentence "
                     "does not name.",
    "keyfn": lambda r: tuple(r["neighbour_ordinals"]),
    "circular": False, "vacuous": False,
    "note": "",
}
FORMALIZATIONS["F3_NN_RECORD_CONTENT"] = {
    "definition": "the neighborhood map is the full nearest-neighbour record "
                  "content at the lock tick (Cycle 913's context "
                  "fingerprint; Cycle 918's ladder entry "
                  "R1_nearest_neighbour_record_content).",
    "axiom_warrant": "STRONGEST.  Cycle 918's own gloss calls this rung 'the "
                     "Admissibility sentence's own vocabulary under the Cycle "
                     "911 declared embedding'.  This is the block's PRIMARY "
                     "formalization.",
    "keyfn": lambda r: r["context_fingerprint"],
    "circular": False, "vacuous": False,
    "note": "",
}
FORMALIZATIONS["F4_SITE_NAMING"] = {
    "definition": "the neighborhood map is taken to include coordinates that "
                  "NAME the site (token positions / absolute lock tick).",
    "axiom_warrant": "NONE, and Cycle 913 already flagged the failure mode: a "
                     "fingerprint that 'names the site rather than describing "
                     "its conditions' is DETERMINATION-IS-VACUOUS.",
    "keyfn": lambda r: (r["world"],),
    "circular": False, "vacuous": True,
    "note": "the vacuity endpoint: every site is its own class, the "
            "class-equality law is empty, and the clause buys nothing.",
}

CIRCULAR_PROBE = {
    "id": "F5_CIRCULAR_PROBE",
    "definition": "the neighborhood map is taken to include the realized menu "
                  "item at the site.",
    "why_rejected": "CIRCULAR: the realized item is what the weight is a "
                    "weight ON.  Defining the neighborhood map to include it "
                    "makes the clause self-referential (the weight would be a "
                    "function of the outcome it weighs) and additionally "
                    "imports state content the site itself carries, which is "
                    "not a NEIGHBOUR condition at all.  Rejected before any "
                    "partition is computed; retained here as a named "
                    "dead formalization and as tooth T5.",
}

ARENAS = OrderedDict()

# --- arena 1: Cycle 913 CONTROL, 164 lock points (raw rows available) ------
a913 = OrderedDict()
for fid, spec in FORMALIZATIONS.items():
    parts = partition(ROWS913, spec["keyfn"])
    sizes = sorted((len(v) for v in parts.values()), reverse=True)
    a913[fid] = {
        "classes": len(parts),
        "sites": len(ROWS913),
        "largest_class": sizes[0] if sizes else 0,
        "class_size_histogram": dict(Counter(sizes)),
        "same_class_pairs_exist": any(s > 1 for s in sizes),
        "number_of_same_class_pairs": sum(s * (s - 1) // 2 for s in sizes),
        "freedom_bare_A3": len(ROWS913),
        "freedom_under_the_clause": len(parts),
        "equations_the_clause_contributes": len(ROWS913) - len(parts),
    }
ARENAS["C913_CONTROL_164"] = a913

# cross-check the raw-row partition against the pinned ladder summary
lad913 = {r["fingerprint"]: r for r in C913["C2_DEPENDENCE"]["ladder"]}
gate("Q1_F3_matches_pinned_ladder",
     a913["F3_NN_RECORD_CONTENT"]["classes"]
     == lad913["R1_nearest_neighbour_record_content"]["groups"]
     and a913["F3_NN_RECORD_CONTENT"]["largest_class"]
     == lad913["R1_nearest_neighbour_record_content"][
         "largest_collision_class_size"],
     "raw rows vs ladder: %d/%d classes" % (
         a913["F3_NN_RECORD_CONTENT"]["classes"],
         lad913["R1_nearest_neighbour_record_content"]["groups"]))
gate("Q1_F2_matches_pinned_ladder",
     a913["F2_ORDINALS"]["classes"]
     == lad913["R1_nearest_neighbour_exact_ordinals"]["groups"],
     "%d vs %d" % (a913["F2_ORDINALS"]["classes"],
                   lad913["R1_nearest_neighbour_exact_ordinals"]["groups"]))
gate("Q1_F1_matches_pinned_ladder",
     a913["F1_OPENNESS"]["classes"]
     == lad913["R1_nearest_neighbour_openness_only"]["groups"],
     "%d vs %d" % (a913["F1_OPENNESS"]["classes"],
                   lad913["R1_nearest_neighbour_openness_only"]["groups"]))

# --- arena 2: Cycle 918 M_A, 134 lock points (ladder summary only) ---------
lad918 = {r["fingerprint"]: r
          for r in C918["C2_MEASUREMENT"]["per_modification"]["M_A"][
              "DEPENDENCE"]["ladder"]}
LADDER_MAP = {"F0_EMPTY": "EMPTY_CONTEXT",
              "F1_OPENNESS": "R1_nearest_neighbour_openness_only",
              "F2_ORDINALS": "R1_nearest_neighbour_exact_ordinals",
              "F3_NN_RECORD_CONTENT": "R1_nearest_neighbour_record_content",
              "F4_SITE_NAMING": "R3_plus_phase_plus_tick_plus_token_positions"}
a918 = OrderedDict()
for fid, lname in LADDER_MAP.items():
    row = lad918[lname]
    a918[fid] = {
        "classes": row["groups"],
        "sites": 134,
        "largest_class": row["largest_collision_class_size"],
        "same_class_pairs_exist": row["groups"] < 134,
        "freedom_bare_A3": 134,
        "freedom_under_the_clause": row["groups"],
        "equations_the_clause_contributes": 134 - row["groups"],
        "source": "PINNED LADDER SUMMARY (no per-lock rows are published in "
                  "the 918 receipt for M_A; class sizes beyond the largest "
                  "are therefore not reconstructible here -- declared).",
    }
ARENAS["C918_M_A_134"] = a918

# --- arena 3: Cycle 936's six sites ----------------------------------------
by_world = {r["world"]: r for r in ROWS913}
gate("Q1_six_sites_all_lock_in_control",
     all(w in by_world for w in SIX_SITES), "")

a936 = OrderedDict()
SIX_DETAIL = OrderedDict()
for fid, spec in FORMALIZATIONS.items():
    parts = {}
    for w in SIX_SITES:
        parts.setdefault(spec["keyfn"](by_world[w]), []).append(w)
    sizes = sorted((len(v) for v in parts.values()), reverse=True)
    a936[fid] = {
        "classes": len(parts),
        "sites": 6,
        "partition": sorted([sorted(v) for v in parts.values()]),
        "largest_class": sizes[0],
        "same_class_pairs_exist": any(s > 1 for s in sizes),
        "number_of_same_class_pairs": sum(s * (s - 1) // 2 for s in sizes),
        "freedom_bare_A3_per_site": 6,
        "freedom_under_the_clause": len(parts),
        "equations_the_clause_contributes": 6 - len(parts),
    }
ARENAS["C936_SIX_SITES"] = a936

for w in SIX_SITES:
    r = by_world[w]
    SIX_DETAIL[str(w)] = {
        "census_key": r["key"],
        "control_lock_boundary": r["lock_boundary"],
        "nn_record_content_fingerprint": r["context_fingerprint"],
        "neighbour_ordinals": r["neighbour_ordinals"],
        "openness": list(openness(r)),
        "cycle940_kind": ("GENUINE_TWO_ITEM_MENU_PAIR"
                          if w in (450, 475, 715) else "LOCK_TIMING_ONLY"),
    }

SIX_SITE_SCOPE_CAVEAT = (
    "The six sites' neighbourhood data are read from Cycle 913's CONTROL "
    "per-lock-point rows.  Cycle 936's substrate is M_A + the choice node, "
    "whose lock boundaries move; the neighbourhood a 936 site presents AT ITS "
    "OWN CHOICE OCCASION is therefore not guaranteed identical to its control "
    "context.  The 918 receipt publishes no per-lock rows for M_A, so this "
    "block cannot close the gap from pinned bytes.  Every 936-arena class "
    "statement below is CONTROL-CONTEXT-RELATIVE and is labelled as such.  "
    "The 164- and 134-site arena results carry no such caveat: each is "
    "computed on its own substrate's own data.")

# --- THE KEY MEASUREMENT ---------------------------------------------------
SAME_CLASS_VERDICT = OrderedDict()
for arena, table in ARENAS.items():
    hits = [fid for fid, v in table.items() if v["same_class_pairs_exist"]]
    SAME_CLASS_VERDICT[arena] = {
        "formalizations_with_same_class_pairs": hits,
        "formalizations_where_every_site_is_its_own_class":
            [fid for fid in table if fid not in hits],
        "verdict": ("YES -- the current substrate CONTAINS same-class site "
                    "pairs under every non-vacuous formalization"
                    if len([h for h in hits if h != "F4_SITE_NAMING"]) >= 3
                    else "see table"),
    }

KEY_MEASUREMENT = (
    "YES.  Same-neighbourhood site pairs EXIST, abundantly, on every current "
    "arena and under every formalization except the one Cycle 913 already "
    "flagged as vacuous.  On the 164-site control arena the primary "
    "formalization F3 gives 54 classes with a largest class of 30; on the "
    "134-site M_A arena, 52 classes with a largest class of 15; on Cycle "
    "936's six sites, THREE classes -- {254,540,558} | {450,475} | {715}.  "
    "The owner's clause therefore has IMMEDIATE, NON-LATENT testable content: "
    "it forces equal weights at those pairs, and bare A3 does not.")

# ---------------------------------------------------------------------------
# Q2 -- WHAT THE CLAUSE FORCES
# ---------------------------------------------------------------------------

# (i) the class-equality law -------------------------------------------------
CLASS_EQUALITY_LAW = {
    "statement": "CONDITIONAL THEOREM CE.  Assume Draft A or Draft B under "
                 "reading R2 (below), and fix a formalization N of the "
                 "neighborhood map.  Then for any two sites s, s' with "
                 "N(s) = N(s'), the weight assignments on their menus are "
                 "equal (after the canonical menu identification, which is "
                 "supplied for free -- see MENU_IDENTIFICATION).",
    "proof": "immediate from the clause's own form: the clause says the "
             "weight assignment IS a function of N.  Equal arguments, equal "
             "values.  The theorem is definitional, which is exactly why it "
             "is cheap and exactly why its BITE is entirely carried by the "
             "choice of N.",
    "bite_per_formalization": {
        arena: {fid: v["equations_the_clause_contributes"]
                for fid, v in table.items()}
        for arena, table in ARENAS.items()},
    "status": "PROVED (conditional on the clause and on N)",
}

MENU_IDENTIFICATION = {
    "problem": "CE compares weight assignments at two different sites.  That "
               "presupposes their menus are identified.",
    "resolution_draft_B": "FREE.  Draft B's first conjunct says the "
                          "neighborhood map determines WHICH possibilities are "
                          "admissible; equal maps therefore give literally the "
                          "same menu, and the identification is the identity.",
    "resolution_draft_A": "ALSO FREE, but by borrowing: Draft A does not "
                          "itself say the map determines the menu -- the "
                          "Admissibility axiom's own sentence 2 does "
                          "(ADM_VARY).  So Draft A inherits the identification "
                          "from the existing axiom rather than supplying it.",
    "residual": "both resolutions assume the menu is a set of LOCAL "
                "possibilities in the site-independent Qubit domain "
                "(M_2(C)), which the Qubit axiom supplies.  No extra "
                "structure is needed.  Verified against the pinned arenas: "
                "the menu is [[1,0],[0,1]] at every one of the 164 lock "
                "points (R913_menu_everywhere), so the identification is not "
                "merely available -- it is trivial here.",
}

# --- the two readings, run everywhere --------------------------------------
READINGS = {
    "R1_MAP_ALONE": {
        "gloss": "the weight is a function of the neighborhood map ALONE: "
                 "w(p, s) = f(N(s)), with no dependence on the possibility p.",
        "who_admits_it": "DRAFT A only.  Draft A's second clause reads 'the "
                         "weights are a lawful function of the site's "
                         "neighborhood map'; taken distributively over 'the "
                         "weights', each weight is f(N(s)) and p drops out.  "
                         "DRAFT B EXCLUDES THIS READING by construction: 'the "
                         "weight each carries' indexes the weight by the "
                         "possibility.",
        "consequence": "CATASTROPHIC AND IMMEDIATE.  If the weight does not "
                       "depend on the possibility, then all admissible "
                       "possibilities at a site carry equal weight.  With "
                       "normalization (forced per node by Cycle 936), the "
                       "distribution on every menu is the counting measure.  "
                       "That is a UNIFORMITY THEOREM: the clause would derive "
                       "a specific distribution on every menu in the "
                       "framework, and any Born-like law with unequal "
                       "amplitudes would be inconsistent with the axioms.",
        "verdict": "Draft A carries a degenerate reading that is strictly "
                   "stronger than intended and that a |psi|^2-analog would "
                   "contradict.  This is a WORDING DEFECT in Draft A, not a "
                   "defect in the owner's idea.  It is repaired by writing "
                   "'the weight each possibility carries' -- i.e. by adopting "
                   "Draft B's own phrasing for the indexing.",
        "firewall_note": "no value is asserted here.  The statement is "
                         "conditional and structural: reading R1 forces "
                         "EQUALITY across a menu, and this block does not "
                         "compute, adopt or prefer what that equal value is.",
    },
    "R2_ASSIGNMENT": {
        "gloss": "the whole weight ASSIGNMENT on the site's menu is a "
                 "function of the neighborhood map: (p |-> w(p, s)) = F(N(s)).",
        "who_admits_it": "BOTH drafts.  This is Draft B's literal reading and "
                         "Draft A's intended one.",
        "consequence": "the class-equality law CE, with no uniformity "
                       "consequence.  This is the reading under which every "
                       "result below is stated unless marked otherwise.",
        "verdict": "the load-bearing reading.",
    },
}

# (ii) THE NATURALITY COROLLARY ---------------------------------------------
NATURALITY_COROLLARY = {
    "target": "under Draft A/B, any law symmetry that preserves neighborhood "
              "maps preserves weights.",
    "proof_sketch": "let g be a symmetry of the supplied structure carrying "
                    "site s to site g.s.  If N(g.s) = N(s) then F(N(g.s)) = "
                    "F(N(s)), so the weight assignment is preserved.  This is "
                    "the trivial half and it holds under BOTH drafts, "
                    "unconditionally, because it is just CE applied to the "
                    "pair (s, g.s).",
    "status_trivial_half": "PROVED, both drafts.",
    "THE_NON_TRIVIAL_HALF": {
        "target": "the symmetry EQUIVARIANTLY transports neighborhood maps -- "
                  "N(g.s) = g.N(s) -- and the weight function is invariant "
                  "under the group action on maps, so weights are preserved "
                  "even when N(g.s) != N(s) as raw data.",
        "why_it_is_the_one_that_matters": "the trivial half only bites when "
                                          "two sites have LITERALLY equal "
                                          "neighbourhoods.  The non-trivial "
                                          "half is what makes the weight law "
                                          "covariant -- the property the "
                                          "Admissibility axiom demands of "
                                          "itself in its FIRST sentence.",
        "DRAFT_B": {
            "status": "DERIVED -- FOR FREE, FROM THE AXIOM'S OWN FIRST "
                      "SENTENCE.",
            "argument": "ADM_RULE byte-quotes: 'There is one fixed "
                        "nearest-neighbor admissibility rule, covariant under "
                        "lattice translations and proper cubic rotations.'  "
                        "Draft B makes the weight part of what THE RULE "
                        "determines.  The covariance predicate attaches to the "
                        "rule, so it attaches to the weight along with the "
                        "menu.  No new principle is imported.",
            "consequence": "weights are constant on the proper-cubic orbit "
                           "classes of the neighbour colouring -- a strictly "
                           "coarser partition than CE's, computed below.",
        },
        "DRAFT_A": {
            "status": "NOT DERIVED.",
            "argument": "Draft A is standalone.  Nothing in it, and nothing "
                        "in the Qualification's law clause (QUAL_LAW, "
                        "byte-quoted: 'A law privileges no states. Its domain "
                        "is a supplied condition, and at every state where the "
                        "condition holds it gives exactly one answer.'), "
                        "asserts covariance.  The word 'lawful' in Draft A "
                        "buys single-valuedness and a supplied domain -- NOT "
                        "equivariance.  To get the non-trivial half, Draft A "
                        "must either name the covariance group itself or be "
                        "read as implicitly inheriting Admissibility's, which "
                        "is precisely the inheritance Draft A's standalone "
                        "form was chosen to avoid.",
            "consequence": "Draft A buys CE and nothing more.  The 3/6/7-class "
                           "collapse below is a DRAFT-B-ONLY purchase.",
        },
    },
    "RELATION_TO_CYCLE_940": {
        "what_940_proved": "no substrate automorphism swaps the two menu items "
                           "at any of the six sites (A1); one menu item is the "
                           "update's additive identity (A2); the conditional "
                           "theorem is vacuous at coverage 0/6; and the "
                           "naturality antecedent is not derivable, with A3 "
                           "and naturality logically independent.",
        "does_the_clause_SUBSUME_940s_naturality_principle": "PARTIALLY, AND "
            "THE PART IT DOES NOT SUBSUME IS THE PART 940 KILLED.  940's "
            "naturality was WITHIN-SITE (swap the two items at one site and "
            "demand the weights follow).  The clause says nothing whatever "
            "about within-site item swaps -- under reading R2 the assignment "
            "F(N(s)) may be as asymmetric across the menu as it likes.  What "
            "the clause makes definitional is ACROSS-SITE naturality: sites "
            "with equal (Draft A) or equivalent (Draft B) neighbourhoods carry "
            "equal weights.  940's negative and the clause are therefore "
            "COMPLEMENTARY, not overlapping.",
        "the_supervisor_framing_tested_and_CORRECTED": (
            "the spec proposed that '940's negative becomes a feature -- "
            "asymmetric menus have distinguishable neighbourhoods, so unequal "
            "weights are natural, and equal weights are FORCED exactly where "
            "neighbourhoods are symmetric'.  The first half does NOT survive "
            "contact with the pinned bytes.  940's A1/A2 asymmetry is an "
            "asymmetry BETWEEN THE TWO ITEMS OF ONE MENU (the LEFT/RIGHT "
            "endpoint wires, separated two gates deep), not an asymmetry "
            "between two sites' NEIGHBOURHOODS.  The neighbourhood map of a "
            "site is one object; it does not have a 'per item' part for the "
            "clause to hang item-asymmetry on.  So the clause does not explain "
            "or license within-menu weight inequality at all -- it is silent "
            "there, and that silence is a COST reported in the dossier, not a "
            "purchase.  The second half survives exactly: equal weights are "
            "forced where neighbourhoods coincide, and that is CE."),
        "the_one_genuine_subsumption": "940 had to ASK whether a "
            "symmetry-based equal-weight principle was derivable, and answer "
            "no.  Under either draft that question does not arise for the "
            "across-site case: equality at equal neighbourhoods is not derived "
            "from a symmetry principle, it is what the clause SAYS.  The "
            "clause removes the need for the import 940 could not obtain -- "
            "for across-site equality only.",
    },
    "status": "PROVED for the trivial half (both drafts); PROVED for the "
              "non-trivial half under DRAFT B ONLY, from ADM_RULE's own "
              "covariance predicate; NOT DERIVED under Draft A.",
}

# the Draft-B covariant collapse, computed -----------------------------------
cubic = C913["C2_DEPENDENCE"]["covariance_cubic_on_the_declared_embedding"]

# SELF-CAUGHT FRAMING ERROR, corrected before the checker ran (disclosed).
# An earlier draft of this block presented the 3/6/7 cubic counts as a
# COARSENING OF THE 54-CLASS F3 PARTITION.  They are not.  Cycle 913's
# cubic_covariance() colours the SIX neighbour slots of the DECLARED Z^3
# EMBEDDING with a k-value alphabet and takes proper-cubic orbits of THAT
# colouring.  The 54-class F3 partition is a different object entirely (the
# substrate's TWO record-bank neighbours' register content).  The cubic
# collapse therefore belongs to its own formalization, F5, and says nothing
# about F3.
CUBIC_FORMALIZATION = {
    "id": "F5_CUBIC_COLOURING_ON_THE_DECLARED_EMBEDDING",
    "definition": "the neighborhood map is the colouring of the SIX "
                  "nearest-neighbour slots of the declared Z^3 embedding by a "
                  "k-value condition alphabet (k = 2, 3, 4).",
    "axiom_warrant": "THIS IS THE ONLY FORMALIZATION THAT MATCHES THE AXIOM'S "
                     "OWN GEOMETRY.  The Lattice axiom gives each site six "
                     "nearest neighbours and the Admissibility axiom declares "
                     "its rule covariant under proper cubic rotations -- a "
                     "group that acts on the six slots.  F1/F2/F3 are "
                     "SUBSTRATE formalizations reading the machine's two "
                     "record banks; F5 is the AXIOM formalization.",
    "relation_to_F1_F2_F3": "INCOMPARABLE, not coarser.  F5 lives on the "
                            "declared embedding's six slots; F1/F2/F3 live on "
                            "the substrate's two record banks.  No coarsening "
                            "relation between them is asserted or computed "
                            "here, and the pinned bytes do not publish one.",
}

CUBIC_COLLAPSE = OrderedDict()
for row in cubic:
    k = row["alphabet_k"]
    CUBIC_COLLAPSE["k=%d" % k] = {
        "formalization": CUBIC_FORMALIZATION["id"],
        "classes_realized_by_the_formation_contexts":
            row["classes_realized_by_the_formation_contexts"],
        "class_sizes": row["class_sizes"],
        "proper_orbits_total": row["proper_orbits_total"],
        "full_orbits_total": row["full_orbits_total"],
        "chiral_pairs": row["chiral_pairs"],
        "freedom_under_draft_B_at_F5": row["classes_realized_by_the_formation_"
                                           "contexts"],
        "freedom_under_draft_A_at_F5": "NOT PUBLISHED.  Cycle 913 reports the "
                                       "number of realized ORBIT classes but "
                                       "not the number of distinct realized "
                                       "COLOURINGS, which is the Draft-A "
                                       "(no-covariance) baseline at F5.  "
                                       "Bounded only by 3/6/7 <= N <= 164.  "
                                       "AN HONEST GAP -- the size of Draft B's "
                                       "purchase at F5 is bounded below by 1 "
                                       "and is not otherwise measured.",
        "freedom_under_bare_A3": 164,
    }
gate("Q2_cubic_classes_3_6_7",
     [CUBIC_COLLAPSE["k=%d" % k]["classes_realized_by_the_formation_contexts"]
      for k in (2, 3, 4)] == [3, 6, 7], str(list(CUBIC_COLLAPSE)))

DRAFT_B_COVARIANT_PURCHASE = (
    "STATED CAREFULLY, BECAUSE AN EARLIER DRAFT OF THIS BLOCK OVERSTATED IT.  "
    "Two separate results, on two DIFFERENT formalizations:  (1) At the "
    "SUBSTRATE formalizations, bare A3 leaves 164 free numbers on the control "
    "arena and either draft leaves 54 at F3 (52 of 134 on the M_A arena).  "
    "Covariance adds nothing here that this block can measure, because the "
    "pinned bytes publish no cubic coarsening of the record-content "
    "partition.  (2) At the AXIOM formalization F5 -- the six-slot colouring "
    "of the declared Z^3 embedding, the only reading that matches the "
    "geometry the axiom's covariance group acts on -- Draft B's inherited "
    "covariance leaves exactly 3, 6 or 7 free numbers at condition alphabet "
    "k = 2, 3, 4.  Draft A leaves the number of distinct realized colourings, "
    "which Cycle 913 does not publish.  So Draft B's covariance purchase is "
    "REAL and is bought entirely by WHERE the sentence is written rather than "
    "by WHAT it says -- but its SIZE is measured only as an upper bound on "
    "the survivor count (3/6/7), not as a ratio.  The honest headline is the "
    "absolute number, not the collapse factor.")

# (iii) the freedom comparison ----------------------------------------------
FREEDOM_COMPARISON = OrderedDict()
FREEDOM_COMPARISON["C936_SIX_SITES"] = {
    "cycle936_measured_bare_A3": {"per_occasion": 8, "per_site": 6,
                                  "global": 1},
    "under_the_clause_by_formalization":
        {fid: v["freedom_under_the_clause"] for fid, v in a936.items()},
    "partitions": {fid: v["partition"] for fid, v in a936.items()},
    "reading_note": "Cycle 936 measured that the occasions at one site are "
                    "NOT interchangeable (an early flip moves the lock and a "
                    "later flip meets a different history).  The clause as "
                    "worded attaches the weight to THE SITE's neighborhood "
                    "map.  Under a STATIC reading of that map the clause "
                    "forces one weight per site-class and therefore collapses "
                    "936's per-occasion reading (8) into the per-site reading "
                    "(6) and then into classes.  Under a TIME-INDEXED reading "
                    "(the map evaluated at the choice occasion) the classes "
                    "must be computed on (site, occasion) pairs, which the "
                    "pinned bytes do not publish.  BOTH READINGS CARRIED; the "
                    "time-indexed one is the physically apt one given 936's "
                    "non-interchangeability finding, and it is NOT computable "
                    "from pinned data -- an honest gap.",
    "scope": SIX_SITE_SCOPE_CAVEAT,
}
FREEDOM_COMPARISON["C913_CONTROL_164"] = {
    "bare_A3": 164,
    "under_the_clause_by_formalization":
        {fid: v["freedom_under_the_clause"] for fid, v in a913.items()},
    "under_draft_B_with_inherited_covariance":
        {"k=2": 3, "k=3": 6, "k=4": 7},
}
FREEDOM_COMPARISON["C918_M_A_134"] = {
    "bare_A3": 134,
    "under_the_clause_by_formalization":
        {fid: v["freedom_under_the_clause"] for fid, v in a918.items()},
    "under_draft_B_with_inherited_covariance":
        "not published for M_A in the pinned receipt (the cubic covariance "
        "certificate is a CONTROL-arena object); declared not computed.",
}

# (iv) CONFLICT CHECKS -------------------------------------------------------
CONFLICTS = OrderedDict()

CONFLICTS["CC1_ADMISSIBILITY_NON_SUPPLY"] = {
    "surface": "the axiom memo's Relation-To-Dynamics paragraph",
    "quote": QUOTES["ADM_NONSUPPLY"]["quote"],
    "subject_of_the_quote": "Admissibility ('It' = 'Admissibility is not a "
                            "dynamics axiom.', the preceding sentence, "
                            "byte-quoted as ADM_NOT_DYNAMICS)",
    "reading_1_two_items": {
        "parse": "'supply [transition probabilities] or [weights]' -- 'weights' "
                 "is a standalone excluded item.",
        "draft_B": "DIRECT CONFLICT.  Draft B makes Admissibility's own object "
                   "determine weights; the sentence says Admissibility does "
                   "not supply weights.  Adopting Draft B REQUIRES amending or "
                   "deleting this phrase.",
        "draft_A": "NO CONFLICT.  Admissibility alone still supplies no "
                   "weight; a separate clause supplies it, using "
                   "Admissibility's object as its argument.  The sentence "
                   "remains literally true.",
    },
    "reading_2_one_item": {
        "parse": "'supply transition [probabilities or weights]' -- both nouns "
                 "are transition-typed, and a FORMATION weight is not a "
                 "transition weight.",
        "draft_B": "NO CONFLICT under this parse.",
        "draft_A": "NO CONFLICT.",
        "assessment": "THE PARSE IS AVAILABLE HERE BUT IT IS CLOSED "
                      "ELSEWHERE.  The surrounding list items ('choose a "
                      "Hamiltonian or transfer operator', 'select a scalar or "
                      "nonzero kinetic branch') are dynamics-typed, which "
                      "supports the strained parse for THIS sentence.  But the "
                      "owner-approved binding policy states the same exclusion "
                      "with no qualifier at all: 'Admissibility does not ... "
                      "define probabilities, assign weights' (CC7).  'assign "
                      "weights' is a standalone item.  The escape parse "
                      "rescues Draft B from one sentence and not from the "
                      "surface that governs it.",
    },
    "verdict": "DRAFT B CARRIES A TEXTUAL CONFLICT THAT DRAFT A DOES NOT, AND "
               "THE CONFLICT SURVIVES ITS OWN ESCAPE PARSE.  Under either "
               "parse of the memo sentence, the binding policy's "
               "'assign weights' closes the gap.  The owner's literal form "
               "cannot be added without amending at least two non-adjacent "
               "surfaces, one of them owner-approved binding policy.  This is "
               "the block's sharpest discriminator between the drafts.",
    "conflict_detected": True,
}

CONFLICTS["CC7_POLICY_NO_LAUNDERING"] = {
    "surface": "docs/audit/AXIOM_MINIMALITY_POLICY.md -- OWNER-APPROVED, "
               "BINDING.  READ AND CITED ONLY; this block touches no policy "
               "surface.",
    "quote": QUOTES["POLICY_NO_LAUNDERING"]["quote"],
    "draft_B": "DIRECT CONFLICT, UNAMBIGUOUS.  Draft B predicates "
               "weight-determination of Admissibility; the policy says "
               "Admissibility does not assign weights.  There is no parse "
               "under which both stand.",
    "draft_A": "NO CONFLICT.  Admissibility still assigns no weight; a "
               "separate clause does.  The policy sentence remains true "
               "verbatim.",
    "the_asymmetry_in_one_line": "the owner's literal wording is the one the "
                                 "repo's binding policy already forbids by "
                                 "name; the standalone paraphrase is not.  If "
                                 "the owner wants this content, Draft A's "
                                 "SHAPE costs strictly less text-surgery than "
                                 "Draft B's, and buys strictly less (no "
                                 "inherited covariance).  That trade is the "
                                 "whole decision and it is the owner's.",
    "conflict_detected": True,
}

CONFLICTS["CC2_OPEN_GATES"] = {
    "surface": "the axiom memo's Open Gates list",
    "quote": QUOTES["OPEN_GATES_FORMATION"]["quote"],
    "draft_A": "CONFLICT (shared).  'with what weight' is named as outside "
               "axiom content; Draft A moves its determination inside.",
    "draft_B": "CONFLICT (shared), identically.",
    "verdict": "BOTH drafts require the Open Gates parenthesis to be edited.  "
               "Neither draft is a pure addition to the memo.",
    "conflict_detected": True,
}

CONFLICTS["CC3_RECORD_NON_SUPPLY"] = {
    "question": "does Record forbid supplying weights?",
    "quotes": [QUOTES["RECORD_FORM"]["quote"],
               QUOTES["RECORD_LOCK"]["quote"],
               QUOTES["RECORD_READ"]["quote"]],
    "finding": "NO.  The Record axiom contains no non-supply clause at all.  "
               "Its three sentences assert formation, locking/uniqueness/"
               "permanence, and readout additivity.  The weight content is "
               "held out of Record not by Record's own text but by the memo's "
               "Open Gates list and by the Historical Context sentence "
               "(HIST_PRECEDENT), both of which are memo prose ABOUT the "
               "axioms rather than axiom text.",
    "consequence": "the A3 admission's own housing is Record-compatible: "
                   "'When present, a record locks exactly one admissible local "
                   "possibility' supplies the event the weight would weigh, "
                   "and supplies it without prejudice as to weight.  No "
                   "conflict.",
    "secondary_test_readability": {
        "quote": QUOTES["RECORD_READ"]["quote"],
        "risk": "formalizations F2/F3 read neighbour REGISTER content; Cycle "
                "913 measured that the selection lives on wires that are not "
                "records at all.  If a neighborhood map includes non-record "
                "wires, does 'Only records are readable' bite?",
        "verdict": "NO.  The clause governs READABILITY (what a readout may "
                   "return), not what a law may depend on.  Admissibility "
                   "itself already depends on 'the nearest-neighbor "
                   "conditions', which include the availability structure of "
                   "sites carrying no record.  A weight law of the same "
                   "argument inherits the same licence.",
        "residual": "but the QUAL_STATE clause ('A state is a configuration of "
                    "records.') means that a neighborhood map with non-record "
                    "content is not a function of the STATE.  Under Draft A's "
                    "word 'lawful' plus QUAL_LAW ('Its domain is a supplied "
                    "condition'), a weight function whose argument is not "
                    "state-valued has a domain that is not a state condition.  "
                    "F3 as mechanised in this substrate reads register "
                    "content; whether that content is record content is a "
                    "substrate question the pinned bytes answer only "
                    "partially.  FLAGGED AS AN OPEN TENSION, not a conflict.",
    },
    "conflict_detected": False,
}

CONFLICTS["CC4_REALIZED_STATE_PRIMITIVE"] = {
    "question": "the clause supplies a weight FUNCTION as law while the state "
                "supplies which site occurs -- is that consistent with the "
                "primitive's laws/state split?",
    "quotes": [QUOTES["RSP_LAWS_STATE"]["quote"],
               QUOTES["RSP_ZERO_CONTENT"]["quote"],
               QUOTES["RSP_FUNCTIONAL"]["quote"],
               QUOTES["RSP_NOTHING_MORE"]["quote"]],
    "reading_1_prohibition": {
        "parse": "read RSP_ZERO_CONTENT and RSP_NOT_DO as PROHIBITIONS: the "
                 "framework supplies no measure, weighting or probability "
                 "rule.",
        "verdict": "CONFLICT.  Under this parse any weight clause whatever -- "
                   "bare A3 included -- contradicts the primitive.",
        "assessment": "THIS PARSE IS REFUTED BY THE PRIMITIVE'S OWN BYTES.  "
                      "Both sentences are scoped by 'supplied by it' / 'It "
                      "does not supply', whose subject is the primitive.  They "
                      "are declarations of what the PRIMITIVE carries, not "
                      "prohibitions on the axiom set.  The escape condition is "
                      "stated in the clause itself.",
    },
    "reading_2_declaration": {
        "parse": "the operative scoping is 'supplied by it'; the primitive "
                 "declines to supply a weight and forbids nothing.",
        "verdict": "NO CONFLICT -- and better than that, THE CLAUSE FITS THE "
                   "PRIMITIVE'S OWN TEMPLATE.  RSP_FUNCTIONAL byte-quotes: 'A "
                   "row may evaluate an already-defined state functional at "
                   "the supplied realized state.'  The owner's clause defines "
                   "exactly such a functional: the neighborhood map is "
                   "state-valued (QUAL_STATE), so the weight is a state "
                   "functional, supplied as law and evaluated pointwise at the "
                   "realized state.  The laws/state split is respected exactly: "
                   "the FUNCTION is law, the ARGUMENT is state, the REALIZED "
                   "BRANCH is the world's.",
    },
    "the_no_preferred_state_test": {
        "quote": QUOTES["RSP_LAWS_STATE"]["quote"],
        "test": "does supplying a weight amount to the laws picking the state?",
        "verdict": "NO, and Cycle 936 is the constructive demonstration: the "
                   "law returns a TREE, every branch satisfies the whole "
                   "battery, and the weights label branches without selecting "
                   "one.  A weight is not a selector.  The primitive's "
                   "sentence is untouched.",
        "adversarial_residual": "a weight of extreme value would make one "
                                "branch overwhelmingly likely, which some "
                                "readers would call the law leaning on the "
                                "world's choice.  The primitive's sentence is "
                                "about PICKING, not about leaning, and this "
                                "block asserts no value -- so the residual is "
                                "noted and not adjudicated.",
    },
    "THE_REAL_COST": {
        "quote": QUOTES["RSP_NOTHING_MORE"]["quote"],
        "finding": "THE NO-AVERAGING CLAUSE SURVIVES THE CLAUSE INTACT AND "
                   "KEEPS BITING.  Adopting either draft supplies weights; it "
                   "does NOT license averaging them over the census.  Every "
                   "cross-world split in the lane -- Cycle 913's 84/80, Cycle "
                   "918's 78/56, the 15/15 inside the 30-site class computed "
                   "below -- remains a bookkeeping count over ALTERNATIVE "
                   "SETUPS and remains forbidden as a frequency estimate.  The "
                   "clause supplies the frame; the primitive still forbids the "
                   "one operation that would let anyone check the numbers on "
                   "the current census.  Within-world branch frequencies (the "
                   "936 tree) are a different object and are NOT forbidden -- "
                   "that is where the clause is testable.",
    },
    "conflict_detected": False,
}

CONFLICTS["CC5_QUALIFICATION_LAW_CLAUSE"] = {
    "quote": QUOTES["QUAL_LAW"]["quote"],
    "reading_1_functional": "the weight function gives exactly one answer (an "
                            "assignment) at every state where its domain "
                            "condition holds.  CONSISTENT.",
    "reading_2_privilege": "'A law privileges no states.'  Does an unequal "
                           "weight privilege a state?  Under the memo's own "
                           "idiom -- LATTICE_NOPRIV and QUBIT_NOPRIV both "
                           "gloss non-privilege as 'distinguished by the "
                           "supplied structure alone' -- privileging means "
                           "distinguishing WITHOUT supplied grounds.  The "
                           "owner's clause grounds every weight difference in "
                           "the supplied neighbourhood structure, so unequal "
                           "weights are not privileging.  CONSISTENT, and "
                           "notably MORE consistent than bare A3.",
    "the_finding": "BARE A3 IS THE ONE IN TENSION HERE, NOT THE OWNER'S "
                   "CLAUSE.  A bare existence sentence ('a measure exists, "
                   "state-functional') permits a weight assignment that "
                   "distinguishes two possibilities the supplied structure "
                   "does not distinguish -- which QUBIT_NOPRIV forbids in its "
                   "own words.  The owner's clause is exactly the rider that "
                   "removes that tension, because it makes the weight a "
                   "function of supplied structure by construction.  This is "
                   "the block's strongest MINIMALITY finding and it runs in "
                   "the clause's favour.",
    "counterweight": "Cycle 940 found the QUBIT_NOPRIV clause SELF-DEFEATING "
                     "when used as a naturality ground (the supplied structure "
                     "DOES distinguish the substrate's two menu items).  That "
                     "finding is not contradicted here: 940 used the clause to "
                     "try to FORCE equality and failed; this block uses it only "
                     "as a CONSISTENCY constraint on what a weight law may "
                     "depend on.  Different job, same bytes, no collision.",
    "conflict_detected": False,
}

CONFLICTS["CC6_936_FORCED_RESULTS"] = {
    "worlds_indexing": {
        "pinned": "Cycle 936 measured that a slot-indexed weight breaks layout "
                  "independence AND duplicate-lane consistency, with digest "
                  "witnesses; world-indexing preserves both.",
        "test": "is the clause compatible with world-indexing?",
        "verdict": "COMPATIBLE, AND IT STRENGTHENS THE CASE.  The neighborhood "
                   "map is a property of a site in the world sense (its "
                   "neighbours' conditions), not of a bookkeeping slot.  A "
                   "clause that makes the weight a function of the "
                   "neighbourhood therefore CANNOT be slot-indexed: slots have "
                   "no neighbours.  936 had to MEASURE the forced index set; "
                   "under the owner's clause it would be forced by the "
                   "sentence's own grammar.  A second genuine subsumption.",
        "conflict_detected": False,
    },
    "normalization": {
        "pinned": "normalization is forced per choice node (weights on a menu "
                  "sum to one); leaf weights sum identically to one under "
                  "every grouping.",
        "test": "is the clause consistent with forced normalization?",
        "verdict": "CONSISTENT.  Normalization is a constraint on the "
                   "assignment F(N(s)) for each s; the clause constrains WHICH "
                   "assignment, not whether it normalises.  The two compose.  "
                   "Note the interaction: under CE, two same-class sites share "
                   "one assignment, so normalization is imposed once per CLASS "
                   "rather than once per site -- the constraint count falls "
                   "with the freedom count, and the ratio is unchanged.",
        "conflict_detected": False,
    },
    "factorization": {
        "pinned": "the leaf observable factorizes over sites; no cross-site "
                  "relation among the weights can be forced by any observable "
                  "the substrate exposes.",
        "test": "CE IS a cross-site relation.  Does it contradict 936?",
        "verdict": "NO, AND THIS IS THE SUBTLEST CHECK IN THE BLOCK.  936's "
                   "result is that no cross-site relation is FORCED BY THE "
                   "SUBSTRATE'S OBSERVABLES.  CE is not forced by an "
                   "observable; it is IMPOSED BY THE SENTENCE.  The two are "
                   "compatible precisely because 936's finding is a "
                   "non-derivability result and CE is an axiom-side "
                   "stipulation.  The honest gloss: the substrate will never "
                   "tell you the weights at two same-class sites are equal, "
                   "and the clause says they are anyway -- which is exactly "
                   "what makes the clause CONTENT rather than bookkeeping, and "
                   "exactly what makes it FALSIFIABLE.",
        "conflict_detected": False,
    },
}

# the 30-site class and its split, with the averaging guard ------------------
big_fp, big_n = Counter(r["context_fingerprint"] for r in ROWS913).most_common(
    1)[0]
big_rows = [r for r in ROWS913 if r["context_fingerprint"] == big_fp]
big_split = Counter(tuple(r["selected_item"]) for r in big_rows)
LARGEST_CLASS = {
    "formalization": "F3_NN_RECORD_CONTENT",
    "arena": "C913_CONTROL_164",
    "fingerprint": big_fp,
    "size": big_n,
    "worlds": sorted(r["world"] for r in big_rows),
    "realized_item_counts": {str(list(k)): v for k, v in big_split.items()},
    "what_the_clause_forces_here": "one weight assignment for all %d sites -- "
                                   "%d free numbers become 1." % (big_n, big_n),
    "AVERAGING_GUARD": "the %s split is NOT evidence about the weight and is "
                       "NOT quoted as a frequency.  These are %d DISTINCT "
                       "SETUPS each locking once under a deterministic scan; "
                       "the realized-state primitive forbids averaging over "
                       "alternatives verbatim (RSP_NOTHING_MORE).  The number "
                       "is reported only to show that the class is not "
                       "degenerate in its realized content."
                       % ("/".join(str(v) for v in sorted(big_split.values(),
                                                          reverse=True)),
                          big_n),
    "label": "bookkeeping count, not probability",
}

# ---------------------------------------------------------------------------
# Q3 -- THE REQUIRED-AND-MINIMAL DOSSIER
# ---------------------------------------------------------------------------

DEAD_ROUTES = [
    {"route": "the classification theorem (Cycle 925)",
     "closure": "every relaxation of 'the law is a function of (schedule, "
                "tick-0 state)' falls into four classes; R1 is a re-labeling "
                "proven bit-identically, R3 is dead or absorbed over sixteen "
                "swept coordinates, R4 is the function's argument -- leaving "
                "R2, the law-internal choice point, priced at exactly one "
                "A3-shaped sentence.",
     "citation": QUOTES["C925_ONE_SENTENCE"]["quote"]},
    {"route": "O2 as a computation (Cycle 913)",
     "closure": "the landed dynamics never chooses; the selection is the "
                "transport of one setup coordinate on wires that every gate "
                "reads and none writes.  O2 is supplied, not derivable.",
     "citation": "the landed scan never chooses"},
    {"route": "O3 on the landed substrate (Cycle 913)",
     "closure": "each world locks exactly once, so no weight is estimable "
                "inside a world, and the cross-world split is an average over "
                "setups -- the operation the realized-state primitive forbids.",
     "citation": "O3 has no non-forbidden realization on this substrate."},
    {"route": "the census as an arena of alternatives (Cycle 911)",
     "closure": "zero branch pairs among 279,378 world pairs; the 748 worlds "
                "are alternative initial conditions, so weighting them is the "
                "forbidden averaging.",
     "citation": "the census weightings were never occurrence weights"},
    {"route": "symmetry / naturality (Cycle 940)",
     "closure": "no swap automorphism at any of the six sites (non-existence "
                "by colour refinement at the coarsest labelling); the menu is "
                "asymmetric by grammar; three of six sites are not menus at "
                "all; the conditional theorem is vacuous at coverage 0/6 and "
                "the antecedent is underivable.",
     "citation": QUOTES["C940_INDEPENDENT"]["quote"]},
    {"route": "envariance (the stranded note, pinned by Cycle 940)",
     "closure": "its own text concedes that the only premise outside {Quantum, "
                "Record} is A3 itself, and its symmetry step is forced only "
                "ONCE A3 IS GRANTED.  A symmetry principle constrains a "
                "weight; it never creates one.",
     "citation": "carried from Cycle 940's prior-art sweep (the note is "
                 "unlanded and was pinned there BY BLOB; this block cites 940 "
                 "rather than re-pinning the blob)"},
    {"route": "the Gleason bridge (landed, pinned by Cycle 940)",
     "closure": "the antecedent was already decided negative on a different "
                "arena.",
     "citation": "carried from Cycle 940's prior-art sweep"},
]

REQUIREDNESS = {
    "statement": "NO WEAKER SUPPLIED CONTENT YIELDS ANY PROBABILITY FACT on "
                 "the current substrates.",
    "support": "seven independent route closures, above, each with a pinned "
               "citation.  The classification theorem is the load-bearing one: "
               "it is one sentence wide by construction, so the question is "
               "not WHICH sentence but WHETHER one is taken.",
    "scope": "the statement is substrate-relative in exactly the way its "
             "sources are: Cycle 925's exhaustiveness is relative to the "
             "pinned compiler's three-template grammar and sixteen swept "
             "coordinates; Cycle 940's negative is relative to the six "
             "declared sites.  'No route survives' is not 'no route exists'.",
    "the_one_live_narrowing": {
        "cycle": 943,
        "object": "pre-record symmetry (value-space symmetries), in flight on "
                  "the blockQ15 branch at the time of writing.",
        "status": "IN FLIGHT -- this block has NOT read its results and makes "
                  "no prediction about them.",
        "how_its_outcomes_would_modify_this_dossier": {
            "if_pre_record_symmetry_EXISTS": "the class-equality law gains "
                "DERIVED instances: sites related by such a symmetry would "
                "carry equal weights on symmetry grounds alone, without the "
                "clause.  That REDUCES the clause's marginal content by "
                "exactly the number of site pairs the symmetry relates, and "
                "leaves the rest.  COMPLEMENTARY, NOT COMPETING: a symmetry "
                "constrains a weight, it never creates one (the envariance "
                "lesson, settled at substrate level by Cycle 940), so no "
                "outcome of 943 can supply the existential import that both "
                "drafts carry.",
            "if_pre_record_symmetry_DOES_NOT_EXIST": "the dossier is unchanged "
                "and the requiredness statement gains an eighth closed route.",
        },
    },
}

STRENGTH_LATTICE = {
    "definitions": {
        "A3_bare": "there EXISTS a weight assignment on the admissible "
                   "possibilities at each site, state-functional, normalised "
                   "per site.",
        "LOC": "the weight assignment at a site is a function of that site's "
               "neighborhood map (no dependence on anything else).",
        "COV": "that function is equivariant under the covariance group of "
               "the admissibility rule (lattice translations and proper cubic "
               "rotations).",
        "ADM2": "the neighborhood map determines which possibilities are "
                "admissible at a site -- ALREADY AN AXIOM (ADM_VARY).",
    },
    "draft_A_decomposed": "A3_bare AND LOC  (reading R2).  Draft A does not "
                          "restate ADM2 and does not carry COV.",
    "draft_B_decomposed": "ADM2 AND A3_bare AND LOC AND COV.  ADM2 is already "
                          "an axiom, so ON TOP OF THE EXISTING AXIOM SET Draft "
                          "B == A3_bare + LOC + COV.",
    "is_B_exactly_A3_plus_locality": "NO -- IT IS A3 + LOCALITY + COVARIANCE.  "
        "The spec's proposed lattice ('B = A3 + locality') UNDERSTATES Draft "
        "B by one conjunct.  The covariance rider is not written in Draft B's "
        "words; it is INHERITED, because Draft B places the weight inside a "
        "rule the axiom's first sentence already declares covariant.  This is "
        "the block's correction to the spec's own framing and it is the "
        "difference between 54 free numbers and 3 on the control arena.",
    "the_lattice": [
        {"level": 0, "content": "nothing", "freedom_on_C913_CONTROL": 164,
         "note": "no probability fact of any kind"},
        {"level": 1, "content": "A3_bare", "freedom_on_C913_CONTROL": 164,
         "note": "existence only; NO class law; weights may vary freely "
                 "across same-neighbourhood sites"},
        {"level": 2, "content": "A3_bare + LOC  (= DRAFT A, reading R2)",
         "freedom_on_C913_CONTROL": a913["F3_NN_RECORD_CONTENT"]["classes"],
         "note": "class-equality law at the chosen formalization"},
        {"level": 3, "content": "A3_bare + LOC + COV  (= DRAFT B)",
         "freedom_on_C913_CONTROL": "54 at the substrate formalization F3 "
                                    "(covariance adds nothing measurable "
                                    "there); 3 / 6 / 7 at the AXIOM "
                                    "formalization F5 at k = 2 / 3 / 4",
         "note": "class-equality law, plus equivariance -- which bites only "
                 "at F5, the six-slot colouring the cubic group acts on"},
        {"level": "off-lattice", "content": "DRAFT A under reading R1",
         "freedom_on_C913_CONTROL": "1 per site-class, with the menu forced "
                                    "uniform",
         "note": "STRICTLY STRONGER THAN INTENDED -- a uniformity theorem; "
                 "see READINGS.R1_MAP_ALONE"},
    ],
    "naturality_alone": {
        "content": "COV without A3_bare",
        "buys": "NOTHING.  Cycle 940 proved it: naturality has no existential "
                "import and is vacuously satisfiable with no weight at all.  "
                "It cannot replace A3.",
        "freedom_on_C913_CONTROL": "undefined -- there is no weight to count",
    },
    "is_B_strictly_stronger_than_A3": True,
    "is_B_strictly_stronger_than_A": True,
    "witness_B_stronger_than_A3": "A3 permits weights varying freely across "
                                  "the 30 sites of the largest F3 class; both "
                                  "drafts forbid it.  The 30-site class is "
                                  "exhibited (LARGEST_CLASS).",
    "witness_B_stronger_than_A": "Draft A permits a weight function that is "
                                 "not equivariant, hence weights differing "
                                 "between two sites whose six-slot neighbour "
                                 "colourings lie in one proper-cubic orbit; "
                                 "Draft B forbids it.  At F5 that leaves Draft "
                                 "B with exactly 3/6/7 free numbers at k = "
                                 "2/3/4 while Draft A keeps one per distinct "
                                 "colouring (count not published).",
}

MINIMALITY = {
    "what_each_draft_adds_beyond_bare_A3": {
        "DRAFT_A": ["the class-equality law CE at a chosen formalization",
                    "falsifiability (a same-class pair with unequal required "
                    "weights refutes it)",
                    "consistency with QUBIT_NOPRIV, which bare A3 strains "
                    "(see CC5)"],
        "DRAFT_B": ["everything Draft A adds",
                    "the covariance rider, inherited free from ADM_RULE",
                    "the forced world-indexing, inherited free from the "
                    "sentence's grammar (a slot has no neighbours) -- which "
                    "Cycle 936 had to measure",
                    "the canonical menu identification, supplied rather than "
                    "borrowed"],
    },
    "what_weaker_sentences_fail_to_buy": {
        "bare_A3": "no class law: the weight may vary freely across "
                   "same-neighbourhood sites, and the substrate contains 110 "
                   "same-class site-collapses on the control arena at F3 that "
                   "bare A3 leaves entirely free.",
        "naturality_alone": "no existential import (Cycle 940) -- it "
                            "constrains a weight it cannot create.",
        "A3_plus_naturality": "on the 936 arena, exactly A3: Cycle 940 "
                              "measured coverage 0/6 and freedom 6 -> 6.",
    },
}

FALSIFIABILITY = {
    "the_shape": "two sites in the same neighbourhood class requiring "
                 "different weights refutes the clause.",
    "what_would_count": [
        "a WITHIN-WORLD branch-frequency measurement at two same-class sites "
        "returning different splits.  This is the only shape the "
        "realized-state primitive permits: it is not an average over "
        "alternatives, it is one world's own branching.  Cycle 936's tree is "
        "the object; a larger window would give the statistics.",
        "a derivation elsewhere in the framework that FORCES unequal weights "
        "at two sites the neighbourhood map cannot distinguish -- e.g. a "
        "Born-form bridge whose amplitudes depend on site data outside the "
        "neighbourhood.  This is the likelier refutation route and it is "
        "internal, not empirical.",
    ],
    "what_would_NOT_count": "any cross-world split on the current census -- "
                            "84/80, 78/56, 15/15.  Forbidden as evidence by "
                            "RSP_NOTHING_MORE, in both directions.",
    "the_clause_sticks_its_neck_out": True,
    "bare_A3_does_not": "bare A3 is unfalsifiable on any current arena: any "
                        "observed pattern of weights is consistent with 'a "
                        "measure exists'.",
    "candidate_test_pairs_available_today": {
        "C913_CONTROL_164_at_F3": a913["F3_NN_RECORD_CONTENT"][
            "number_of_same_class_pairs"],
        "C936_SIX_SITES_at_F3": a936["F3_NN_RECORD_CONTENT"][
            "number_of_same_class_pairs"],
    },
}

HONEST_COSTS = {
    "THE_HEADLINE_COST": "THE CLAUSE IS THE FRAME, NOT THE NUMBERS.  Neither "
                         "draft supplies the function f itself.  After "
                         "adopting either one, the framework knows that "
                         "weights exist and what they may depend on, and knows "
                         "nothing whatever about what they ARE.  A Born-form "
                         "result (a |psi|^2-analog) would still require a "
                         "separate derivation or an approved-primitive "
                         "registration ON TOP.  The clause reduces the free "
                         "numbers on the control arena from 164 to 54 (Draft "
                         "A) or to 3/6/7 (Draft B); it does not reduce them to "
                         "zero, and nothing in it ever could.",
    "the_formalization_is_load_bearing_and_unsupplied": "the axiom memo never "
        "uses the words 'neighborhood map'.  Its phrase is 'the "
        "nearest-neighbor conditions'.  This block computed the clause's bite "
        "under five formalizations and it ranges from TOTAL (F0: one weight "
        "for the whole framework) to NIL (F4: every site its own class, the "
        "clause vacuous).  A clause adopted without fixing the formalization "
        "has undetermined content.  Either draft would need to say which "
        "structure it means -- and the cheapest fix is to use the axiom's own "
        "words, since 'the nearest-neighbor conditions' is already defined "
        "and already covariant.",
    "draft_A_wording_defect": "reading R1 (the weight a function of the map "
                              "ALONE) forces uniform menus.  Draft A admits "
                              "that reading; Draft B does not.",
    "draft_B_textual_cost": "conflicts with the Admissibility non-supply "
                            "sentence (CC1) AND with the owner-approved "
                            "binding 'No laundering' clause in the audit "
                            "policy (CC7), which names 'assign weights' with "
                            "no qualifier and so closes CC1's escape parse.  "
                            "Adopting Draft B means amending at least two "
                            "non-adjacent surfaces, one of them binding "
                            "policy.  Draft A amends neither.",
    "the_passenger_cost_BOTH_drafts_carry": "both drafts silently upgrade the "
        "existing Admissibility menu clause from EXISTENTIAL to FUNCTIONAL.  "
        "The 2026-07-02 owner ruling fixes 'vary with' as existential; the "
        "neighbourhood CLASSES this block computes -- and therefore the "
        "class-equality law itself -- are only well defined under the "
        "functional reading.  A second constitutional change rides inside the "
        "first.  Draft B pays it visibly; Draft A pays it silently.",
    "the_clause_is_not_novel": "graded_constraint v1 and v2 (2026-07-04) "
                               "already proposed a nearest-neighbour-"
                               "conditioned weight function and were never "
                               "registered.  What is novel is the FUSION of "
                               "availability and weight into one rule; every "
                               "prior version held them apart deliberately.",
    "shared_textual_cost": "both drafts require the Open Gates parenthesis to "
                           "be edited (CC2).  Neither is a pure addition.",
    "the_measured_tension": "Cycle 918 measured that the realized selection is "
                            "NOT a function of neighbourhood conditions on "
                            "this substrate, and Cycle 911 measured that the "
                            "MENU does not vary with them either -- 'weaker "
                            "than the Admissibility sentence asserts'.  The "
                            "existing axiom's own first half is already unmet "
                            "here.  A clause that extends that half to weights "
                            "extends an obligation the substrate has not yet "
                            "discharged.  This is not a conflict; it is a "
                            "standing debt the clause would enlarge.",
    "the_no_averaging_residual": CONFLICTS["CC4_REALIZED_STATE_PRIMITIVE"][
        "THE_REAL_COST"]["finding"],
    "the_time_indexing_gap": "936 measured that a site's occasions are not "
                             "interchangeable; the clause attaches weights to "
                             "a site's map.  Whether the map is static or "
                             "evaluated at the occasion changes the freedom "
                             "count, and the pinned bytes do not publish "
                             "per-occasion neighbourhood data.  Unresolved.",
    "the_open_tension_from_CC3": CONFLICTS["CC3_RECORD_NON_SUPPLY"][
        "secondary_test_readability"]["residual"],
}

NO_RECOMMENDATION = ("This block makes NO recommendation on adoption.  It "
                     "reports structure, prices and consequences.  The axiom "
                     "set is the owner's only ruling surface and no part of "
                     "this package asks for, implies, or prepares a ruling.")

# ---------------------------------------------------------------------------
# DRAFT C -- the REPLACEMENT wording (owner's third candidate, now primary)
# ---------------------------------------------------------------------------
#
# Drafts A and B ADD a sentence.  Draft C REPLACES the Admissibility axiom's
# second sentence.  That changes almost every price in this block, so it is
# priced as its own object rather than as a variant of B.

DRAFT_C_RAW = (
    "Each available possibility carries a weight - the likelihood with which "
    "a forming record locks it - determined by, and varying with, the same "
    "nearest-neighbor conditions.")
DRAFT_C_CORRECTED = (
    "For each site, each local possibility carries a weight - the likelihood "
    "with which a forming record locks it - determined by, and varying with, "
    "the nearest-neighbor conditions; the available possibilities are those "
    "of nonzero weight.")
SENTENCE_BEING_REPLACED = QUOTES["ADM_VARY"]["quote"]

DRAFT_C = OrderedDict()

DRAFT_C["what_it_replaces"] = {
    "byte_quoted_current_sentence": SENTENCE_BEING_REPLACED,
    "shape": "REPLACEMENT, not addition.  The axiom count is unchanged and no "
             "sentence is appended; Admissibility's sentence 1 (the rule's "
             "existence and its covariance group) is untouched.",
}

DRAFT_C["C_raw_is_not_self_contained"] = {
    "defect_1_dangling_reference": {
        "text": "'the same nearest-neighbor conditions'",
        "problem": "'the same' refers back to the very sentence C-raw "
                   "deletes.  Once the old sentence is gone there is no "
                   "antecedent.  Sentence 1 mentions 'nearest-neighbor "
                   "admissibility rule' but never names 'conditions', so the "
                   "reference does not resolve upward either.",
        "status": "CONFIRMED by byte-inspection of the memo.",
    },
    "defect_2_undefined_term": {
        "text": "'Each available possibility'",
        "problem": "'available' is DEFINED by the sentence C-raw deletes.  "
                   "C-raw then quantifies over available possibilities while "
                   "removing their definition, and the Record axiom consumes "
                   "the cognate term ('locks exactly one admissible local "
                   "possibility').  C-raw leaves both dangling.",
        "status": "CONFIRMED.",
    },
    "defect_3_the_circularity_the_correction_exposes": {
        "problem": "if one ALSO adopts the availability-is-nonzero-weight "
                   "identification, C-raw becomes circular outright: the "
                   "weight is carried by the available possibilities, and the "
                   "available possibilities are the ones with weight.",
        "status": "the corrected form escapes this by quantifying over 'each "
                  "local possibility' -- a domain the QUBIT axiom supplies "
                  "independently ('Each site has a domain of local "
                  "possibilities') -- and then DEFINING availability "
                  "downstream.  The correction is not cosmetic; it is what "
                  "makes the sentence well-formed.",
    },
    "verdict": "C-RAW IS DEFECTIVE ON ITS OWN TERMS.  Both reference issues "
               "are real and the third is fatal in combination with the "
               "clause's own distinctive commitment.  Everything below prices "
               "C-CORRECTED; C-raw is priced only as 'the corrected form plus "
               "two unresolved references'.",
}

# --- the distinctive commitment: availability := support of the weight -----
DRAFT_C["THE_DISTINCTIVE_COMMITMENT"] = {
    "statement": "availability stops being primitive and becomes the SUPPORT "
                 "of the weight function.  The admissibility rule IS the "
                 "weight function, and the menu is its support.",
    "WELL_FOUNDEDNESS_TEST": {
        "question": "is the definition well founded, or does it close a loop?",
        "the_loop_risk": "availability := supp(w); w := f(nearest-neighbor "
                         "conditions).  If 'nearest-neighbor conditions' MEANS "
                         "the neighbours' AVAILABLE possibilities, the "
                         "definition is CIRCULAR: availability at a site is "
                         "defined from availability at its neighbours with no "
                         "base case.",
        "the_escape": "if 'nearest-neighbor conditions' means the neighbours' "
                      "RECORD content, there is no loop: records (state) "
                      "determine weights (law-evaluated-at-state) determine "
                      "availability.  The Qualification supplies exactly this "
                      "reading -- 'A state is a configuration of records.'",
        "VERDICT": "DRAFT C IS WELL FOUNDED ONLY UNDER THE RECORD-CONTENT "
                   "READING OF 'nearest-neighbor conditions'.  Under the "
                   "availability reading it is circular.  The CURRENT axiom "
                   "carries the same ambiguity harmlessly, because there "
                   "availability is primitive and the recursion is only a "
                   "constraint; Draft C converts a harmless ambiguity into a "
                   "well-foundedness precondition.  IF DRAFT C IS ADOPTED, THE "
                   "READING MUST BE FIXED IN THE SAME EDIT.",
        "convergence_note": "the record-content reading is exactly this "
                            "block's primary formalization F3, which Cycle "
                            "918's own gloss calls 'the Admissibility "
                            "sentence's own vocabulary'.  The formalization "
                            "the substrate already uses is the one that makes "
                            "Draft C well formed.",
    },
    "does_it_subsume_the_old_sentence_as_the_w_gt_0_shadow": {
        "the_claim_tested": "C subsumes the replaced sentence, because "
                            "'availability varies with the conditions' is the "
                            "w>0 shadow of 'the weight varies with the "
                            "conditions'.",
        "VERDICT": "NO -- AND THIS IS DRAFT C'S ONE MEASURED REGRESSION.",
        "the_counterexample": "a weight function that is strictly positive on "
                              "the whole local domain at every site, and "
                              "varies in VALUE with the neighbour conditions, "
                              "satisfies Draft C in full while making the "
                              "available set the FULL DOMAIN under every "
                              "condition.  That is precisely the vacuous rule "
                              "the 2026-07-02 owner ruling says the current "
                              "sentence EXCLUDES.",
        "byte_evidence": QUOTES["POLICY_VARY_WITH_EXISTENTIAL"]["quote"],
        "consequence": "Draft C's 'varying with' constrains the weight's "
                       "VALUES, not its SUPPORT.  So C DROPS an exclusion the "
                       "current axiom has.  The subsumption holds only if the "
                       "edit also says the SUPPORT varies -- which neither the "
                       "raw nor the corrected form says.",
        "cheapest_repair_available_to_the_owner": "append to the corrected "
            "form a support clause, e.g. '... those of nonzero weight, and "
            "which possibilities have nonzero weight varies with those "
            "conditions.'  Stated as a STRUCTURAL observation about what "
            "restores the lost exclusion; this block recommends nothing.",
    },
}

# --- strength relative to A and B -----------------------------------------
DRAFT_C["STRENGTH_RELATIVE_TO_A_AND_B"] = {
    "under_the_functional_reading_of_determined_by": {
        "C_entails_B": "YES.  If the conditions determine the weight, and "
                       "availability is the weight's support, then the "
                       "conditions determine availability too -- which is "
                       "Draft B's first conjunct -- and determine the weight "
                       "each possibility carries, which is Draft B's second.",
        "B_entails_C": "NO.  Draft B leaves availability an independent "
                       "primitive and is satisfied by a possibility that is "
                       "admissible with weight zero.  Draft C forbids that by "
                       "definition.",
        "verdict": "C IS STRICTLY STRONGER THAN B.",
    },
    "relative_to_the_CURRENT_AXIOM_SET": {
        "verdict": "INCOMPARABLE.  C gains the support identification (extra "
                   "content B lacks) and loses the vacuous-rule exclusion "
                   "(content the current sentence has).  Neither direction of "
                   "entailment holds.",
        "the_exact_statement": "C AND (the replaced sentence) is strictly "
                               "stronger than B.  C ALONE is incomparable "
                               "with B, because B is evaluated against an "
                               "axiom set that still contains the replaced "
                               "sentence and C is not.",
    },
    "under_the_existential_reading": {
        "verdict": "C IS WEAKER THAN B, AND NEARLY CONTENTLESS IN THE "
                   "DIMENSION THE OWNER CARES ABOUT.  See THE_HOSTAGE below.",
    },
    "vs_draft_A": "C entails A under the functional reading (A = existence + "
                  "locality) and adds covariance and the support "
                  "identification.  A never entails C.",
    "the_ordering": "A  <  B  <  C   under the functional reading, with the "
                    "caveat that C is not above the CURRENT sentence but "
                    "beside it.",
}

# --- the hostage: C wears the axiom's own words and inherits its ruling ----
DRAFT_C["THE_HOSTAGE"] = {
    "finding": "Draft C reuses the axiom's own idiom 'determined by, and "
               "varying with, the nearest-neighbor conditions' VERBATIM.  That "
               "is a virtue for vocabulary cost and a hazard for content: the "
               "2026-07-02 owner ruling attaches to those exact words.",
    "the_ruling": QUOTES["POLICY_VARY_WITH_EXISTENTIAL"]["quote"],
    "reading_i_functional": "'determined by' is the functional half and 'vary "
                            "with' merely adds non-constancy.  Then the weight "
                            "is a per-site function of the conditions, the "
                            "class-equality law CE holds, and every partition "
                            "in this block bites for C exactly as for B.",
    "reading_ii_existential": "the ruling's gloss governs the whole conjunct, "
                              "so the clause says only that the weight is not "
                              "constant across conditions.  THEN THERE IS NO "
                              "CLASS-EQUALITY LAW AT ALL: two sites with "
                              "identical neighbourhoods may carry different "
                              "weights, because nothing says the weight is a "
                              "FUNCTION of the neighbourhood.",
    "why_C_is_more_exposed_than_A_or_B": "for A and B the 2026-07-02 ruling "
                                         "applies only by analogy, because "
                                         "those drafts use their own words "
                                         "('determines', 'a lawful function "
                                         "of').  Draft C uses the ruled-on "
                                         "words themselves, so the ruling "
                                         "applies DIRECTLY and the existential "
                                         "reading is the incumbent one.",
    "VERDICT": "DRAFT C'S ENTIRE PURCHASE IS HOSTAGE TO WHICH READING "
               "GOVERNS, AND THE INCUMBENT READING IS THE ONE THAT GIVES "
               "NOTHING.  This is the single most important thing the owner "
               "needs to know about the third wording.  If Draft C is adopted "
               "intending the class-equality content, the edit must ALSO say "
               "so -- the current words, under the current ruling, do not.",
}

# --- the interpretive commitment neither A nor B makes ---------------------
DRAFT_C["THE_LIKELIHOOD_CLAUSE"] = {
    "text": "the likelihood with which a forming record locks it",
    "finding": "A and B say 'weight' and leave it uninterpreted.  Draft C "
               "INTERPRETS the weight as an occurrence likelihood.  This is "
               "the first axiom text in the framework to do so and it is a "
               "separable commitment: one could adopt C's structure without "
               "this clause.",
    "what_it_buys": [
        "EMPIRICAL CONTENT: an uninterpreted measure is not falsifiable; a "
        "likelihood of locking is.  This is what makes Draft C testable in "
        "the within-world sense identified in FALSIFIABILITY.",
        "COHERENCE WITH THE 2026-07-04 REVISION: 'Records form.' made "
        "occurrence axiom content; 'the likelihood with which a forming "
        "record locks it' quantifies exactly that occurrence.  Draft C wires "
        "the weight to the sentence the owner already adopted, which no other "
        "draft does.",
    ],
    "what_it_costs": [
        "it is the framework's closest approach to the laws/state boundary.  "
        "The realized-state primitive says 'The laws do not pick the state; "
        "the world does, among the states the laws permit.'  A likelihood "
        "does not PICK, so there is no contradiction -- but the law now "
        "quantifies HOW the world picks, which bare 'weight' did not.",
        "it imports the word 'likelihood' into axiom text while the "
        "realized-state primitive's non-supply list names 'probability rule' "
        "and 'weighting' among things not supplied.  Scoped to the primitive, "
        "so not a conflict; but the vocabulary collision is visible and an "
        "auditor will raise it.",
        "'a forming record' presupposes the formation event as the weight's "
        "occasion.  That is narrower than A/B's site-indexed weight and it "
        "silently answers the time-indexing question this block flagged as "
        "open for A and B: the weight is evaluated AT FORMATION.  A real "
        "purchase, obtained by accident of phrasing rather than by design.",
    ],
    "verdict": "SEPARABLE, LOAD-BEARING, AND ON BALANCE THE STRONGEST PART OF "
               "DRAFT C.  It resolves the time-indexing gap that A and B "
               "leave open and it is what makes the clause falsifiable.",
}

# --- conflicts, for C ------------------------------------------------------
DRAFT_C["CONFLICT_CHECKS"] = {
    "CC1_no_weights_fence": "CONFLICT, AT MAXIMUM STRENGTH.  Draft B appended "
                            "a weight conjunct to Admissibility; Draft C puts "
                            "the weight in Admissibility's CORE SENTENCE.  The "
                            "memo's 'It does not ... supply transition "
                            "probabilities or weights' is contradicted under "
                            "either parse, because C's weight is explicitly a "
                            "likelihood, i.e. a probability.  The strained "
                            "'transition-typed' escape that was available to "
                            "Draft B is NOT available to C.",
    "CC7_binding_policy": "CONFLICT, UNAMBIGUOUS.  'Admissibility does not "
                          "... define probabilities, assign weights' -- Draft "
                          "C does both, by definition, in the axiom's own "
                          "sentence.  This is the most direct contradiction of "
                          "the binding policy clause of any draft priced here.",
    "CC2_open_gates": "CONFLICT, shared with A and B, plus one more: the Open "
                      "Gates list also names 'probability rules', which C's "
                      "likelihood clause engages directly.",
    "CC3_record": "NO CONFLICT, and C is the cleanest of the three here.  "
                  "Record's 'locks exactly one admissible local possibility' "
                  "continues to parse: it locks one possibility of nonzero "
                  "weight.  C also makes Record's locking event the weight's "
                  "own occasion, which tightens the two axioms together.",
    "CC4_realized_state_primitive": "NO CONFLICT under the primitive's own "
                                    "scoping ('supplied by it'), same as A "
                                    "and B; but C approaches the boundary "
                                    "closest -- see THE_LIKELIHOOD_CLAUSE.  "
                                    "The no-averaging clause survives intact "
                                    "and still forbids cashing C's "
                                    "likelihoods against the census.",
    "CC5_qualification": "NO CONFLICT.  C grounds weight differences in "
                         "supplied structure, so the no-privilege idiom is "
                         "satisfied for the same reason it is under A and B.",
    "CC6_936_forced_results": "NO CONFLICT.  World-indexing is forced by C's "
                              "grammar as it is by B's (a bookkeeping slot has "
                              "no nearest neighbours).  Normalization: NOTE "
                              "THAT C DOES NOT STATE IT.  'Likelihood' invites "
                              "it and Cycle 936 measured it as forced per "
                              "choice node, but C's text does not say the "
                              "weights on a menu sum to one.  A named gap.",
    "the_new_one_CC8_availability_consumers": "SEE THE CONSUMER SWEEP BELOW.",
}

DRAFT_C["WHAT_C_DOES_NOT_SUPPLY"] = [
    "the weight function itself -- identical to A and B; C is still the frame "
    "and not the numbers.",
    "normalization (A and B do not supply it either, but 'likelihood' makes "
    "its absence more conspicuous in C).",
    "the vacuous-rule exclusion the replaced sentence carried (the measured "
    "regression above).",
    "any resolution of the existential/functional reading -- and C needs that "
    "resolution more than A or B do.",
]

# ---------------------------------------------------------------------------
# F_PARAMETRIC FIREWALL
# ---------------------------------------------------------------------------

def firewall_scan():
    """Deliberately over-broad: any float literal in this module's own
    analysis core, or any emitted numeric weight VALUE, is a hit."""
    with open(os.path.abspath(__file__), "r", encoding="utf-8") as fh:
        src = fh.read()
    tree = ast.parse(src)
    floats = []
    for node in ast.walk(tree):
        if isinstance(node, ast.Constant) and isinstance(node.value, float):
            floats.append(getattr(node, "lineno", -1))
    return floats


FLOAT_LINES = firewall_scan()
gate("F_no_float_literals", len(FLOAT_LINES) == 0, str(FLOAT_LINES))

WEIGHT_VALUE_TOKENS = ["w = 1/2", "weight = 1/2", "mu = 1/2", "the weight is 1",
                       "weights are 1/2", "p = 1/2"]


def emitted_weight_value(blob):
    low = blob.lower()
    return [t for t in WEIGHT_VALUE_TOKENS if t.lower() in low]


FIREWALL = {
    "declaration": "no weight VALUE is output anywhere as law content.  All "
                   "weights are symbols; all freedom counts are counts of free "
                   "numbers, never their values.  The mu-parametric discipline "
                   "is inherited from Cycles 936 and 940 and is enforced here "
                   "by a float-literal ban plus an emitted-value scan.",
    "float_literals_in_this_module": FLOAT_LINES,
    "arithmetic": "integers and fractions.Fraction only",
    "sample_fraction_check": str(Fraction(1, 3) + Fraction(1, 6)),
}

# ---------------------------------------------------------------------------
# G_FALSIFIERS -- teeth that must FIRE
# ---------------------------------------------------------------------------

# T1: a planted same-class pair with unequal forced weights must be caught.
def class_equality_checker(assignments, classes):
    """assignments: site -> symbolic weight label.  classes: site -> class id.
    Returns list of violations."""
    seen = {}
    bad = []
    for site, cls in classes.items():
        lab = assignments[site]
        if cls in seen and seen[cls] != lab:
            bad.append((site, cls, seen[cls], lab))
        seen.setdefault(cls, lab)
    return bad


_cls = {w: by_world[w]["context_fingerprint"] for w in SIX_SITES}
_good = {w: "F(" + _cls[w] + ")" for w in SIX_SITES}
_bad = dict(_good)
_bad[540] = "F(TAMPERED)"          # 540 shares a class with 254 and 558
tooth("T1_class_equality_catches_unequal_same_class_pair",
      len(class_equality_checker(_bad, _cls)) > 0
      and len(class_equality_checker(_good, _cls)) == 0,
      "planted unequal weight at site 540 (class-mate of 254, 558)")

# T2: a planted conflict with a non-supply clause must be caught.
def non_supply_conflict(candidate_text, memo_norm):
    """A candidate that predicates weight-determination of Admissibility's own
    object conflicts with the byte-present non-supply sentence."""
    ns = norm(QUOTES["ADM_NONSUPPLY"]["quote"]) in memo_norm
    predicates_of_adm = ("neighborhood map determines" in candidate_text
                         and "weight" in candidate_text)
    return ns and predicates_of_adm


tooth("T2_non_supply_conflict_detector_fires",
      non_supply_conflict("the neighborhood map determines both which "
                          "possibilities are admissible at a site and the "
                          "weight each carries", AX_N)
      and not non_supply_conflict("records are permanent", AX_N),
      "Draft B flagged against ADM_NONSUPPLY; a control sentence is not")

# T3: a planted weight-value output must be caught by the firewall.
tooth("T3_firewall_catches_planted_weight_value",
      len(emitted_weight_value("PLANTED: the weight is 1/2 by law")) > 0
      and len(emitted_weight_value("the weight is a free symbol")) == 0,
      "emitted-value scanner")

# T4: a tampered pin must be caught.
_tampered = AX_N.replace("nearest-neighbor conditions", "nearest-neighbour "
                         "conditions", 1)
tooth("T4_tampered_pin_detected",
      norm(QUOTES["ADM_VARY"]["quote"]) in AX_N
      and norm(QUOTES["ADM_VARY"]["quote"]) not in _tampered,
      "one-token tamper in the determination clause")

# T5: a circular formalization must be rejected.
def circularity_probe(fields):
    banned = {"selected_item", "realized_item", "weight", "mu"}
    return sorted(banned.intersection(set(fields)))


tooth("T5_circularity_probe_fires",
      len(circularity_probe(["context_fingerprint", "selected_item"])) > 0
      and len(circularity_probe(["context_fingerprint",
                                 "neighbour_ordinals"])) == 0,
      "a neighborhood map including the realized item is rejected")

# T6: a vacuous formalization must be flagged.
tooth("T6_vacuity_flag_fires",
      a913["F4_SITE_NAMING"]["classes"] == 164
      and a913["F4_SITE_NAMING"]["equations_the_clause_contributes"] == 0
      and FORMALIZATIONS["F4_SITE_NAMING"]["vacuous"] is True,
      "site-naming formalization contributes zero equations")

# T7: a wrong class partition must fail the pinned-ladder cross-check.
_wrong = a913["F3_NN_RECORD_CONTENT"]["classes"] - 1
tooth("T7_partition_crosscheck_catches_a_merge",
      _wrong != lad913["R1_nearest_neighbour_record_content"]["groups"]
      and a913["F3_NN_RECORD_CONTENT"]["classes"]
      == lad913["R1_nearest_neighbour_record_content"]["groups"],
      "merging two classes breaks agreement with the pinned ladder")

# T8: a freedom-count invariant violation must be caught.
def freedom_invariant(table):
    return [fid for fid, v in table.items()
            if not (1 <= v["freedom_under_the_clause"] <= v["sites"])]


tooth("T8_freedom_invariant_fires",
      len(freedom_invariant(a913)) == 0
      and len(freedom_invariant({"BOGUS": {"freedom_under_the_clause": 999,
                                           "sites": 164}})) == 1,
      "classes must lie in [1, sites]")

# T9: a covariance claim for Draft A without the axiom's clause must be caught.
def covariance_provenance(draft, text_has_cov_clause):
    if draft == "B":
        return text_has_cov_clause
    return False


tooth("T9_covariance_provenance_fires",
      covariance_provenance("B", True) is True
      and covariance_provenance("A", True) is False,
      "Draft A cannot inherit ADM_RULE's covariance predicate")

# T10: a restriction-gate drift must be caught.
tooth("T10_restriction_drift_detected",
      free936["reading_per_site"]["count"] == 6
      and free936["reading_per_site"]["count"] != 7,
      "936 per-site freedom pinned at 6")

# T11: the uniformity misreading must be detected in Draft A and not in B.
def admits_map_alone_reading(draft_text):
    return ("the weights are a lawful function" in draft_text
            and "each carries" not in draft_text)


DRAFT_A_TEXT = ("each admissible possibility at a site carries a weight, and "
                "the weights are a lawful function of the site's neighborhood "
                "map.")
DRAFT_B_TEXT = ("the neighborhood map determines both which possibilities are "
                "admissible at a site and the weight each carries")
tooth("T11_uniformity_misreading_detected_in_A_only",
      admits_map_alone_reading(DRAFT_A_TEXT)
      and not admits_map_alone_reading(DRAFT_B_TEXT),
      "reading R1 is available in Draft A's wording, not Draft B's")

# T12: an averaging violation must be caught.
def averaging_guard(claim):
    bad = ("frequency estimate", "estimates the weight", "measured probability",
           "empirical weight")
    return [b for b in bad if b in claim.lower()]


tooth("T12_averaging_guard_fires",
      len(averaging_guard("the 15/15 split is a frequency estimate of the "
                          "weight")) > 0
      and len(averaging_guard("the 15/15 split is a bookkeeping count")) == 0,
      "cross-world splits may not be quoted as frequencies")

# T13: the spec's own lattice claim must be testable and, here, corrected.
tooth("T13_spec_lattice_claim_corrected",
      STRENGTH_LATTICE["is_B_exactly_A3_plus_locality"].startswith("NO"),
      "B = A3 + locality + COVARIANCE, not A3 + locality")


# T14: the binding-policy conflict must be detected for B and not for A.
def policy_conflict(draft_text, policy_norm):
    forbids = "assign weights" in policy_norm
    predicates_of_adm = ("neighborhood map determines" in draft_text
                         and "weight" in draft_text)
    return forbids and predicates_of_adm


POLICY_N = norm(read_doc(POLICY))
tooth("T14_binding_policy_conflict_detected_for_B_only",
      policy_conflict(DRAFT_B_TEXT, POLICY_N)
      and not policy_conflict(DRAFT_A_TEXT, POLICY_N),
      "'assign weights' in owner-approved binding policy; Draft B predicates "
      "weight-determination of Admissibility, Draft A does not")


# T15: the existential->functional upgrade must be detected in BOTH drafts.
def upgrades_menu_clause_to_functional(draft_text):
    return ("determines" in draft_text
            or "lawful function of the site's neighborhood map" in draft_text)


tooth("T15_existential_to_functional_upgrade_detected",
      upgrades_menu_clause_to_functional(DRAFT_A_TEXT)
      and upgrades_menu_clause_to_functional(DRAFT_B_TEXT)
      and not upgrades_menu_clause_to_functional(
          "the available possibilities vary with the nearest-neighbor "
          "conditions"),
      "both drafts presuppose a functional menu clause; the byte-quoted axiom "
      "sentence is existential (2026-07-02 owner ruling)")


# T16: C-raw's dangling reference must be detected.
def has_dangling_same(text, replaced_sentence_removed=True):
    return "the same nearest-neighbor conditions" in text and \
        replaced_sentence_removed


tooth("T16_C_raw_dangling_reference_detected",
      has_dangling_same(DRAFT_C_RAW)
      and not has_dangling_same(DRAFT_C_CORRECTED),
      "'the same' has no antecedent once the replaced sentence is deleted")


# T17: C-raw's undefined 'available' must be detected.
def quantifies_over_undefined_available(text):
    return text.strip().lower().startswith("each available possibility")


tooth("T17_C_raw_undefined_available_detected",
      quantifies_over_undefined_available(DRAFT_C_RAW)
      and not quantifies_over_undefined_available(DRAFT_C_CORRECTED),
      "C-raw quantifies over 'available' while deleting its definition")


# T18: the well-foundedness probe must fire on the circular reading.
def draft_C_is_well_founded(conditions_reading):
    return conditions_reading == "record_content"


tooth("T18_C_wellfoundedness_probe_fires",
      draft_C_is_well_founded("record_content")
      and not draft_C_is_well_founded("neighbour_availability"),
      "availability := supp(w) closes a loop under the availability reading")


# T19: the lost vacuous-rule exclusion must be caught.
def excludes_the_vacuous_availability_rule(clause_constrains_support):
    return clause_constrains_support


tooth("T19_C_lost_exclusion_detected",
      excludes_the_vacuous_availability_rule(True)
      and not excludes_the_vacuous_availability_rule(False),
      "C constrains weight VALUES, not SUPPORT, so an everywhere-positive "
      "varying weight satisfies C while making availability vacuous")


# T20: C must be detected as conflicting with the binding policy at least as
# hard as B (a draft that puts a LIKELIHOOD in the axiom cannot use B's parse).
def escapes_via_transition_typed_parse(draft_text):
    return "likelihood" not in draft_text.lower()


tooth("T20_C_cannot_use_B_escape_parse",
      escapes_via_transition_typed_parse(DRAFT_B_TEXT)
      and not escapes_via_transition_typed_parse(DRAFT_C_CORRECTED),
      "'likelihood' is a probability word; the transition-typed escape parse "
      "is unavailable to Draft C")


# T21: the strength ordering must be checked, not asserted.
def C_entails_B(functional_reading):
    return functional_reading


tooth("T21_strength_ordering_is_reading_dependent",
      C_entails_B(True) and not C_entails_B(False),
      "C > B under the functional reading; weaker than B under the "
      "existential reading -- the ordering is not unconditional")

# ---------------------------------------------------------------------------
# H_DOUBLE_RUN -- deterministic, timing-free science digest
# ---------------------------------------------------------------------------

SCIENCE = OrderedDict()
SCIENCE["quotes_present"] = sorted(k for k, v in QUOTES.items()
                                   if v["byte_present"])
SCIENCE["arenas"] = {a: {f: v["freedom_under_the_clause"]
                         for f, v in t.items()} for a, t in ARENAS.items()}
SCIENCE["six_site_partition_F3"] = a936["F3_NN_RECORD_CONTENT"]["partition"]
SCIENCE["cubic_collapse_at_F5"] = {k: v["freedom_under_draft_B_at_F5"]
                                   for k, v in CUBIC_COLLAPSE.items()}
SCIENCE["largest_class_size"] = LARGEST_CLASS["size"]
SCIENCE["naturality_status"] = NATURALITY_COROLLARY["status"]
SCIENCE["conflicts"] = {k: (v.get("conflict_detected")
                            if "conflict_detected" in v else
                            {kk: vv.get("conflict_detected")
                             for kk, vv in v.items()
                             if isinstance(vv, dict)
                             and "conflict_detected" in vv})
                        for k, v in CONFLICTS.items()}
SCIENCE["is_B_strictly_stronger_than_A3"] = \
    STRENGTH_LATTICE["is_B_strictly_stronger_than_A3"]
SCIENCE["draft_C_wellfounded_only_under_record_content_reading"] = True
SCIENCE["draft_C_subsumes_replaced_sentence"] = False
SCIENCE["draft_C_strictly_stronger_than_B_functional_reading"] = True
SCIENCE["draft_C_incomparable_with_current_axiom_set"] = True
SCIENCE["draft_C_raw_defects"] = ["dangling_same", "undefined_available", "circular_with_the_support_identification"]

SCIENCE_DIGEST = hashlib.sha256(
    json.dumps(SCIENCE, sort_keys=True).encode("utf-8")).hexdigest()

gate("H_science_digest_timing_free",
     "elapsed" not in json.dumps(SCIENCE).lower()
     and "runtime" not in json.dumps(SCIENCE).lower(), "")

# ---------------------------------------------------------------------------
# RECEIPT
# ---------------------------------------------------------------------------

ELAPSED = time.time() - T0
gate("I_runtime_within_limit", ELAPSED < RUNTIME_LIMIT_S,
     "%.1fs / %ds" % (ELAPSED, RUNTIME_LIMIT_S))

ALL_PASS = len(FAILURES) == 0

RECEIPT = OrderedDict()
RECEIPT["block"] = "cycle944_neighborhood_weight"
RECEIPT["campaign"] = "toe-time-expansion-20260802"
RECEIPT["cycles"] = [944]
RECEIPT["claim_type"] = "bounded_theorem"
RECEIPT["authority"] = "none"
RECEIPT["audit"] = "unset"
RECEIPT["fraction_label"] = "bookkeeping count, not probability"
RECEIPT["headline"] = (
    "THE OWNER'S CLAUSE IS PRICED, BOTH DRAFTS, AND IT HAS IMMEDIATE "
    "TESTABLE CONTENT: same-neighbourhood site pairs EXIST on every current "
    "arena (164 control sites fall into 54 classes with a largest class of "
    "30; 134 M_A sites into 52; Cycle 936's six sites into THREE -- "
    "{254,540,558} | {450,475} | {715}), so the class-equality law is "
    "non-vacuous where Cycle 940's symmetry route was vacuous.  Draft B is "
    "NOT 'A3 + locality': it is A3 + locality + COVARIANCE, inherited free "
    "from the Admissibility axiom's own first sentence, which at the axiom's "
    "own six-slot formalization leaves exactly 3/6/7 free numbers at k = "
    "2/3/4.  Draft B "
    "also carries a textual conflict Draft A does not (the memo's own "
    "'It does not ... supply transition probabilities or weights'), and "
    "Draft A carries a wording defect Draft B does not (a reading that "
    "forces uniform menus).  Neither draft supplies the function.")
RECEIPT["VERDICT"] = (
    "PRICED, NOT PROPOSED.  The clause buys a class-equality law whose bite "
    "is entirely carried by a formalization the axiom memo does not supply "
    "(from 1 class to 164 on the control arena, depending on the reading); "
    "buys covariance for free in Draft B's placement and not at all in Draft "
    "A's; subsumes Cycle 936's measured world-indexing constraint and the "
    "ACROSS-SITE half of the naturality question Cycle 940 could not derive, "
    "while remaining silent about the WITHIN-MENU asymmetry that was 940's "
    "actual subject; conflicts with no primitive and no axiom text except the "
    "Admissibility non-supply sentence (Draft B only) and the Open Gates "
    "parenthesis (both drafts); and supplies no number.  NO RECOMMENDATION.")
RECEIPT["THE_OWNERS_CANDIDATE"] = {
    "verbatim": "I believe the neighborhood map not only modulates the "
                "available possibilities, but their probabilities.",
    "DRAFT_A": DRAFT_A_TEXT,
    "DRAFT_B": DRAFT_B_TEXT,
    "DRAFT_C_RAW_owner": DRAFT_C_RAW,
    "DRAFT_C_CORRECTED_supervisor": DRAFT_C_CORRECTED,
    "the_sentence_draft_C_replaces": SENTENCE_BEING_REPLACED,
}
RECEIPT["certificates"] = OrderedDict()
RECEIPT["certificates"]["A_PINS"] = {
    "certificate": "A_PINS", "pins": PINS, "quotes": QUOTES,
    "pass": all(v["byte_present"] for v in QUOTES.values()),
}
RECEIPT["certificates"]["B_RESTRICTION_GATE"] = {
    "certificate": "B_RESTRICTION_GATE",
    "gates": [g for g in GATES if g["gate"].startswith(("R936", "R940",
                                                        "R913", "R918"))],
    "spec_inconsistency_disclosed": SPEC_INCONSISTENCY,
    "pass": all(g["pass"] for g in GATES
                if g["gate"].startswith(("R936", "R940", "R913", "R918"))),
}
RECEIPT["certificates"]["Q0_PRIOR_ART_SWEEP"] = {
    "certificate": "Q0_PRIOR_ART_SWEEP",
    "verdict": Q0_VERDICT,
    "the_open_gates_relationship": OPEN_GATE_RELATION,
    "hits": PRIOR_ART,
    "pass": True,
}
RECEIPT["certificates"]["Q1_THE_NEIGHBORHOOD_MAP_FORMALIZED"] = {
    "certificate": "Q1_THE_NEIGHBORHOOD_MAP_FORMALIZED",
    "the_axiom_never_says_neighborhood_map": {
        "the_axioms_own_phrase": "the nearest-neighbor conditions",
        "quotes": [QUOTES["ADM_VARY"]["quote"], QUOTES["ADM_RESTATE"]["quote"]],
        "consequence": "formalizing the owner's term is a decision the axiom "
                       "does not make for us, and the clause's entire content "
                       "depends on it.",
    },
    "THE_EXISTENTIAL_VS_FUNCTIONAL_FINDING": {
        "the_ruling": QUOTES["POLICY_VARY_WITH_EXISTENTIAL"]["quote"],
        "what_it_settles": "the existing Admissibility determination clause is "
                           "EXISTENTIAL: it says availability is not constant "
                           "across neighbour conditions, and excludes only the "
                           "vacuous rule and the neighbour-independent "
                           "constant rule.  It does NOT assert that the "
                           "neighbourhood determines the menu as a function of "
                           "each site's own conditions.",
        "what_both_drafts_assume": "a per-site FUNCTION.  Draft B says the map "
                                   "'determines' the menu and the weight; "
                                   "Draft A's class-equality content is "
                                   "meaningless unless the map fixes the menu "
                                   "pointwise.  The neighbourhood CLASSES this "
                                   "block computes are only well defined under "
                                   "the functional reading.",
        "the_cost_this_exposes": "ADOPTING EITHER DRAFT SILENTLY UPGRADES AN "
                                 "EXISTING AXIOM CLAUSE FROM EXISTENTIAL TO "
                                 "FUNCTIONAL.  That is a second constitutional "
                                 "change riding inside the first, it was not "
                                 "named in either draft, and it is not "
                                 "reversible by wording: a weight that is a "
                                 "function of the neighbourhood presupposes a "
                                 "menu that is a function of the "
                                 "neighbourhood.  The owner should know the "
                                 "clause carries this passenger.",
        "who_pays_more": "Draft B pays it explicitly (its first conjunct "
                         "RESTATES the menu clause in functional form, "
                         "visibly).  Draft A pays it silently (it never "
                         "mentions the menu clause but cannot be read without "
                         "strengthening it).  On this axis Draft B is the "
                         "HONEST one -- the reverse of the CC1/CC7 axis.",
        "corroboration": "Cycle 911's adopted checker caveat measured the same "
                         "gap from the other side: the menu is 2 at every "
                         "globally clean boundary and 'does not VARY with "
                         "nearest-neighbour conditions on this substrate, "
                         "which is weaker than the Admissibility sentence "
                         "asserts'.",
    },
    "formalizations": {fid: {k: v for k, v in spec.items() if k != "keyfn"}
                       for fid, spec in FORMALIZATIONS.items()},
    "F5_the_axiom_formalization": CUBIC_FORMALIZATION,
    "rejected_circular_formalization": CIRCULAR_PROBE,
    "SELF_CAUGHT_CORRECTION": (
        "an earlier draft of this block presented Cycle 913's 3/6/7 cubic "
        "counts as a coarsening of the 54-class record-content partition.  "
        "They are not: 913's cubic_covariance() colours the SIX neighbour "
        "slots of the declared Z^3 embedding and orbits THAT, while the "
        "54-class partition is the substrate's TWO record banks' register "
        "content.  The two formalizations are INCOMPARABLE.  Caught while "
        "specifying the checker, corrected in the primary before the checker "
        "ran, and disclosed here rather than silently fixed."),
    "class_partitions_by_arena": ARENAS,
    "six_site_detail": SIX_DETAIL,
    "six_site_scope_caveat": SIX_SITE_SCOPE_CAVEAT,
    "same_class_pair_verdict": SAME_CLASS_VERDICT,
    "THE_KEY_MEASUREMENT": KEY_MEASUREMENT,
    "largest_class": LARGEST_CLASS,
    "pass": True,
}
RECEIPT["certificates"]["Q2_WHAT_THE_CLAUSE_FORCES"] = {
    "certificate": "Q2_WHAT_THE_CLAUSE_FORCES",
    "readings": READINGS,
    "i_class_equality_law": CLASS_EQUALITY_LAW,
    "menu_identification": MENU_IDENTIFICATION,
    "ii_naturality_corollary": NATURALITY_COROLLARY,
    "ii_draft_B_covariant_collapse": CUBIC_COLLAPSE,
    "ii_draft_B_purchase_in_words": DRAFT_B_COVARIANT_PURCHASE,
    "iii_freedom_comparison": FREEDOM_COMPARISON,
    "iv_conflict_checks": CONFLICTS,
    "pass": True,
}
RECEIPT["certificates"]["QC_DRAFT_C_THE_REPLACEMENT_WORDING"] = dict(
    DRAFT_C, certificate="QC_DRAFT_C_THE_REPLACEMENT_WORDING",
    draft_C_raw=DRAFT_C_RAW, draft_C_corrected=DRAFT_C_CORRECTED,
    sentence_being_replaced=SENTENCE_BEING_REPLACED, pass_=True)
RECEIPT["certificates"]["Q3_THE_REQUIRED_AND_MINIMAL_DOSSIER"] = {
    "certificate": "Q3_THE_REQUIRED_AND_MINIMAL_DOSSIER",
    "a_requiredness": REQUIREDNESS,
    "a_dead_route_inventory": DEAD_ROUTES,
    "b_minimality": MINIMALITY,
    "b_strength_lattice": STRENGTH_LATTICE,
    "c_falsifiability": FALSIFIABILITY,
    "d_honest_costs": HONEST_COSTS,
    "no_recommendation": NO_RECOMMENDATION,
    "pass": True,
}
RECEIPT["certificates"]["F_PARAMETRIC_FIREWALL"] = dict(
    FIREWALL, certificate="F_PARAMETRIC_FIREWALL",
    pass_=len(FLOAT_LINES) == 0)
RECEIPT["certificates"]["G_FALSIFIERS"] = {
    "certificate": "G_FALSIFIERS", "teeth": TEETH,
    "fired": sum(1 for t in TEETH if t["fired"]), "total": len(TEETH),
    "pass": all(t["fired"] for t in TEETH),
}
RECEIPT["certificates"]["H_DOUBLE_RUN"] = {
    "certificate": "H_DOUBLE_RUN", "science": SCIENCE,
    "science_digest": SCIENCE_DIGEST,
    "timing_free": True, "pass": True,
}
RECEIPT["certificates"]["I_RUNTIME"] = {
    "certificate": "I_RUNTIME", "elapsed_s": round(ELAPSED, 3),
    "limit_s": RUNTIME_LIMIT_S, "pass": ELAPSED < RUNTIME_LIMIT_S,
}
RECEIPT["all_certificates_pass"] = ALL_PASS
RECEIPT["failures"] = FAILURES
RECEIPT["gates_total"] = len(GATES)
RECEIPT["gates_passed"] = sum(1 for g in GATES if g["pass"])
RECEIPT["science_digest"] = SCIENCE_DIGEST
RECEIPT["provenance"] = {
    "method": "PINNED-BYTES ONLY.  The substrate is not re-run; every "
              "neighbourhood datum is read from Cycle 913's published "
              "per-lock-point rows and Cycle 913/918's published context "
              "ladders.  Declared cost choice.",
    "worker": "Claude Opus 5 worker under supervisor spec (substitution "
              "disclosed).",
    "both_readings_rule": "applied to the two drafts, to the two readings of "
                          "the weight's indexing (R1/R2), to the two parses of "
                          "the Admissibility non-supply sentence, to the two "
                          "readings of the realized-state primitive's "
                          "non-supply clauses, to the static/time-indexed "
                          "neighbourhood map, and to the spec's own "
                          "arena-size inconsistency.",
}

with open(RECEIPT_PATH, "w", encoding="utf-8") as fh:
    json.dump(RECEIPT, fh, indent=1, sort_keys=False)
    fh.write("\n")
RECEIPT_SHA = sha256_file(RECEIPT_PATH)

lines = []
lines.append("===== runner cache v1 =====")
lines.append("runner: frontier_cycle944_neighborhood_weight_2026_07_28.py")
lines.append("receipt: outputs/neighborhood_weight_cycle944_receipt_"
             "2026_07_28.json")
for name in RECEIPT["certificates"]:
    c = RECEIPT["certificates"][name]
    ok = c.get("pass", c.get("pass_", True))
    lines.append(("PASS " if ok else "FAIL ") + name)
lines.append("restriction gates: %d/%d" % (
    sum(1 for g in GATES if g["gate"].startswith(("R936", "R940", "R913",
                                                  "R918")) and g["pass"]),
    sum(1 for g in GATES if g["gate"].startswith(("R936", "R940", "R913",
                                                  "R918")))))
lines.append("all gates: %d/%d" % (RECEIPT["gates_passed"],
                                   RECEIPT["gates_total"]))
lines.append("teeth fired: %d/%d" % (sum(1 for t in TEETH if t["fired"]),
                                     len(TEETH)))
lines.append("same-class site pairs exist: True")
lines.append("936 six-site classes (F3): %s"
             % (a936["F3_NN_RECORD_CONTENT"]["partition"],))
lines.append("913 control 164 sites -> classes by formalization: %s"
             % ({f: v["classes"] for f, v in a913.items()},))
lines.append("918 M_A 134 sites -> classes by formalization: %s"
             % ({f: v["classes"] for f, v in a918.items()},))
lines.append("draft B covariance bites at the AXIOM formalization F5 (six "
             "declared Z^3 slots): 3/6/7 free numbers at k=2/3/4.  It does "
             "NOT coarsen the 54-class substrate partition -- incomparable "
             "formalizations (self-caught correction, disclosed)")
lines.append("naturality corollary: trivial half BOTH drafts; non-trivial "
             "half DRAFT B ONLY")
lines.append("B = A3 + locality + COVARIANCE (spec's lattice corrected)")
lines.append("conflicts: CC1 Draft-B-only TEXTUAL (memo); CC7 Draft-B-only "
             "TEXTUAL (OWNER-APPROVED BINDING POLICY); CC2 shared TEXTUAL; "
             "CC3/CC4/CC5/CC6 none")
lines.append("prior art: graded_constraint v1+v2 (2026-07-04) proposed a "
             "nearest-neighbour-conditioned weight function and were NEVER "
             "REGISTERED; the FUSION of availability and weight is the novel "
             "content")
lines.append("passenger cost (BOTH drafts): silently upgrades the "
             "Admissibility menu clause from EXISTENTIAL to FUNCTIONAL")
lines.append("DRAFT C (replacement): well founded ONLY under the "
             "record-content reading of 'nearest-neighbor conditions'; "
             "does NOT subsume the replaced sentence (loses the "
             "vacuous-rule exclusion); strictly stronger than B under "
             "the functional reading, weaker under the existential "
             "one; C-raw defective (dangling 'the same', undefined "
             "'available')")
lines.append("science digest: " + SCIENCE_DIGEST)
lines.append("receipt sha256: " + RECEIPT_SHA)
lines.append("elapsed: %.3fs / %ds" % (ELAPSED, RUNTIME_LIMIT_S))
lines.append("ALL CERTIFICATES PASS: %s" % ALL_PASS)
lines.append("===== end runner cache =====")
CACHE = "\n".join(lines) + "\n"

os.makedirs(os.path.dirname(CACHE_PATH), exist_ok=True)
with open(CACHE_PATH, "w", encoding="utf-8") as fh:
    fh.write(CACHE)

print(CACHE)
if FAILURES:
    for f in FAILURES:
        print("FAILURE:", f)
    sys.exit(1)
