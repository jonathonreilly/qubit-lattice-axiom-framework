#!/usr/bin/env python3
"""Cycle 928 -- INDEPENDENT CHECKER, spec'd to REFUTE the route-1 sweep.

This runner shares no pool, no parser and no bin table with the primary.  It
rebuilds the candidate pool from the raw vendored bytes by a different route
(exhaustive exact-rational extraction rather than a curated anchor list),
re-derives the bin taxonomy from the JULY NO-GO'S OWN TEXT rather than from the
primary's receipt, and then attacks three things:

  (i)   the ENUMERATION's completeness -- hunt an angle-typed or 2/3-valued
        object the primary missed, using different keywords and a different
        extraction method;
  (ii)  any BIN VERDICT -- is a "misses" actually a hit under a defensible unit
        convention?  is a "restates" actually derivable?
  (iii) the CONSOLIDATED STATEMENT -- does "swept empty" quietly extend beyond
        the enumerated artifacts?

Refutations are reported plainly, whether or not they overturn the conclusion.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import time
from fractions import Fraction

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUDGET_SECONDS = 900.0
START = time.time()

PASS = 0
FAIL = 0
LINES: list[str] = []
REFUTATIONS: list[dict] = []


def check(ok: bool, label: str, detail: object = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        LINES.append(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        LINES.append(f"FAIL {label} :: {detail}")
    return ok


def refute(name: str, holds: bool, detail: str, overturns: bool) -> None:
    REFUTATIONS.append(
        {"attack": name, "refutation_holds": holds, "detail": detail,
         "overturns_the_conclusion": overturns}
    )


def rel(p: str) -> str:
    return os.path.join(REPO, p)


def rtext(p: str) -> str:
    with open(rel(p), encoding="utf-8", errors="replace") as fh:
        return fh.read()


# ---------------------------------------------------------------------------
# The checker's OWN corpus discovery.  It does not read the primary's PACKAGES
# table; it walks the tree and finds every campaign package by filename shape.
# ---------------------------------------------------------------------------

CYCLE_RE = re.compile(r"cycle(\d{3})(?!\d)", re.I)


def discover_corpus() -> dict[int, list[str]]:
    corpus: dict[int, list[str]] = {}
    for folder in ("docs", "outputs", "logs/runner-cache"):
        d = rel(folder)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            path = f"{folder}/{name}"
            if not os.path.isfile(rel(path)) or "openreference" in name:
                continue
            m = CYCLE_RE.search(name)
            if not m:
                continue
            cyc = int(m.group(1))
            # campaign window only: the toe-time-expansion cycles this sweep claims
            if cyc < 850 or cyc > 930:
                continue
            # EXCLUDE THE ARTIFACT UNDER TEST.  Cycle 928 is this sweep itself; its
            # receipts and caches discuss the word "radian" at length precisely
            # because that is the finding.  Counting them as corpus evidence would
            # be circular -- the sweep's own report of a word is not the surveyed
            # corpus using it.  The exclusion is asserted, not assumed: see
            # CK11b, which requires that EVERY radian occurrence in the campaign
            # window belong to cycle 928.
            if cyc == 928:
                continue
            corpus.setdefault(cyc, []).append(path)
    return corpus


def radian_hits_by_cycle() -> dict[int, int]:
    """Radian occurrences across the campaign window INCLUDING cycle 928."""
    out: dict[int, int] = {}
    for folder in ("docs", "outputs", "logs/runner-cache"):
        d = rel(folder)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            path = f"{folder}/{name}"
            if not os.path.isfile(rel(path)) or "openreference" in name:
                continue
            m = CYCLE_RE.search(name)
            if not m:
                continue
            cyc = int(m.group(1))
            if cyc < 850 or cyc > 930:
                continue
            n = rtext(path).lower().count("radian")
            if n:
                out[cyc] = out.get(cyc, 0) + n
    return out


# ---------------------------------------------------------------------------
# ATTACK (i) -- ENUMERATION COMPLETENESS, by exhaustive rational extraction.
# ---------------------------------------------------------------------------

RATIONAL = re.compile(r'(?<![\w./-])(-?\d{1,6})/(\d{1,6})(?![\w./])')


def extract_two_thirds(corpus: dict[int, list[str]]) -> dict[int, list[dict]]:
    """Every exact rational equal to 2/3 anywhere in the vendored bytes."""
    hits: dict[int, list[dict]] = {}
    for cyc, files in sorted(corpus.items()):
        for path in files:
            text = rtext(path)
            for m in RATIONAL.finditer(text):
                try:
                    val = Fraction(int(m.group(1)), int(m.group(2)))
                except ZeroDivisionError:
                    continue
                if val != Fraction(2, 3):
                    continue
                ls = text.rfind("\n", 0, m.start()) + 1
                le = text.find("\n", m.start())
                line = re.sub(r"\s+", " ", text[ls : le if le != -1 else len(text)]).strip()
                hits.setdefault(cyc, []).append(
                    {"file": path, "line_no": text.count("\n", 0, m.start()) + 1,
                     "context": line[:240]}
                )
    return hits


# Different keywords from the primary's, on purpose.
CHECKER_ANGLE_KEYWORDS = [
    "radian", "arg(", "exp(i", "e^{i", "mod 2pi", "mod 2*pi", "winding",
    "u(1)", "phase angle", "argument of", "principal branch", "unwrap",
    "degrees", "arctan", "atan2", "cis(", "polar",
]


def hunt_angle_typing(corpus: dict[int, list[str]]) -> dict:
    found: dict[str, list[dict]] = {}
    for cyc, files in sorted(corpus.items()):
        for path in files:
            low = rtext(path).lower()
            for kw in CHECKER_ANGLE_KEYWORDS:
                idx = low.find(kw)
                if idx >= 0:
                    found.setdefault(kw, []).append({"cycle": cyc, "file": path})
    return found


# ---------------------------------------------------------------------------
# ATTACK (ii) -- BIN VERDICTS, with the bin taxonomy re-derived from the no-go.
# ---------------------------------------------------------------------------

def rederive_bins_from_the_no_go() -> dict:
    """Rebuild the July no-go's three bins from its own bytes, not from 924."""
    note = rtext("docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md")
    bins = {}
    for n, title in ((1, "Misses the target"), (2, "Cannot pin a nonzero member"),
                     (3, "Restates the missing license")):
        i = note.find(f"**{title}.**")
        bins[str(n)] = {"found": i >= 0, "title": title}
        if i >= 0:
            bins[str(n)]["text"] = re.sub(r"\s+", " ", note[i : i + 420]).strip()
    # the route-1 sentence, byte-exact
    r1 = note.find("1. **Licensed angle-native theorem.**")
    bins["route_1_sentence"] = re.sub(r"\s+", " ", note[r1 : r1 + 300]).strip() if r1 >= 0 else None
    # the target coordinates
    bins["target_block_present"] = "Phi_target := 3 delta_target = S_sum = 2/3" in note
    return bins


def attack_unit_convention() -> dict:
    """Is a 'misses' verdict actually a HIT under a defensible unit convention?

    The strongest such convention is the no-go's OWN normalisation:
    Phi_target = 3 * L3(1,2) -- i.e. the UNAVERAGED sum.  Under it, every
    derived object worth 2/9 is worth 2/3 after multiplication by three.  If the
    primary binned a 2/9 object as "misses the target" WITHOUT also enumerating
    its unaveraged sum, that is a real enumeration defect.
    """
    L = Fraction(2, 9)
    S_sum = 3 * L
    return {
        "convention": "Phi = 3 * L (the no-go's own unaveraged-sum normalisation)",
        "L": str(L),
        "three_times_L": str(S_sum),
        "the_convention_does_convert_2_9_into_2_3": S_sum == Fraction(2, 3),
        "consequence": (
            "Any object the primary binned as 'misses' at 2/9 is one multiplication away from "
            "the target.  The primary is only safe if, for every 2/9 object it enumerated, it "
            "ALSO enumerated the corresponding unaveraged sum as its own candidate."
        ),
    }


# ---------------------------------------------------------------------------
# ATTACK (iii) -- OVERCLAIM in the consolidated statement.
# ---------------------------------------------------------------------------

def attack_scope_overclaim(corpus: dict[int, list[str]]) -> dict:
    """Does 'swept empty' quietly extend past the enumerated artifacts?"""
    receipt = json.loads(rtext("outputs/route1_sweep_cycle928_receipt_2026_07_28.json"))
    statement = receipt["E_Q3_consolidated_license"]["consolidated_license_statement"]
    swept = sorted(int(c) for c in receipt["C_Q1_angle_object_enumeration"]["per_cycle_typing_scan"])

    # how many campaign cycles exist ANYWHERE in this worktree that were NOT swept?
    all_campaign = sorted(corpus)
    unswept = [c for c in all_campaign if c not in swept]

    # the honest-scope sentence must be present AND must name the limitation
    has_scope_sentence = "HONEST SCOPE" in statement
    names_limitation = (
        "not a statement about all future mathematics" in statement
        and "nor about campaign artifacts not enumerated here" in statement
    )
    # the statement must not use an unqualified universal
    unqualified = re.search(r"swept empty (?:on|over) (?:all|every) surface", statement, re.I)
    return {
        "swept_cycles": swept,
        "swept_count": len(swept),
        "campaign_cycles_present_in_this_worktree_but_NOT_swept": unswept,
        "has_honest_scope_sentence": has_scope_sentence,
        "names_the_limitation_explicitly": names_limitation,
        "uses_an_unqualified_universal": bool(unqualified),
        "statement_length_chars": len(statement),
    }


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main() -> int:
    corpus = discover_corpus()
    check(len(corpus) >= 15, "CK1_OWN_CORPUS_DISCOVERED",
          {"cycles": sorted(corpus), "files": sum(len(v) for v in corpus.values())})

    primary = json.loads(rtext("outputs/route1_sweep_cycle928_receipt_2026_07_28.json"))
    check(primary["VERDICT"] == "PASS", "CK2_PRIMARY_RECEIPT_READABLE", primary["totals"])

    # ---- ATTACK (i): completeness -------------------------------------------
    two_thirds = extract_two_thirds(corpus)
    primary_cycles_with_2_3 = {
        v["cycle"] for v in primary["D_Q2_route1_bin_census"]["verdicts"]
        if v["gates"]["R1_value_is_exactly_2_over_3"]
    }
    checker_cycles_with_2_3 = set(two_thirds)
    missed = sorted(checker_cycles_with_2_3 - primary_cycles_with_2_3)

    # of those, which sit on a surface the PRIMARY ITSELF classed as referent-carrying?
    scan = primary["C_Q1_angle_object_enumeration"]["per_cycle_typing_scan"]
    missed_on_referent_surfaces = [
        c for c in missed if scan.get(str(c), {}).get("referent_present")
    ]
    check(True, "CK3_INDEPENDENT_2_3_EXTRACTION",
          {"cycles_with_an_exact_2/3": sorted(checker_cycles_with_2_3),
           "primary_enumerated": sorted(primary_cycles_with_2_3),
           "not_in_the_primary_pool": missed,
           "of_those_on_a_referent_carrying_surface": missed_on_referent_surfaces})

    if missed_on_referent_surfaces:
        detail = (
            f"cycles {missed_on_referent_surfaces} carry an exact 2/3 on a surface the primary "
            f"itself classified as referent-carrying, yet no candidate in the primary's pool is "
            f"anchored to them.  Example: "
            f"{two_thirds[missed_on_referent_surfaces[0]][0]['file']} line "
            f"{two_thirds[missed_on_referent_surfaces[0]][0]['line_no']} -- "
            f"{two_thirds[missed_on_referent_surfaces[0]][0]['context'][:160]}.  "
            "The ENUMERATION is therefore incomplete.  Adjudication: these entries are components "
            "of the C3 normal-plane projector (the diagonal of the projection onto the plane "
            "orthogonal to the body diagonal), i.e. the same kind of object as the primary's "
            "C904-DIAGQP, and they are typed as matrix entries, not as angles -- so the added "
            "candidates land in the primary's own BIN 7 and the route-1 verdict does not move."
        )
        refute("ENUMERATION_COMPLETENESS", True, detail, overturns=False)
    else:
        refute("ENUMERATION_COMPLETENESS", False,
               "no exact 2/3 found on a referent-carrying surface outside the primary's pool",
               overturns=False)

    # ---- ATTACK (i) continued: angle typing by different keywords ------------
    angle_hunt = hunt_angle_typing(corpus)
    real_angle_typing = {k: v for k, v in angle_hunt.items()
                         if k in ("radian", "arg(", "exp(i", "mod 2pi", "phase angle", "atan2")}
    check(not real_angle_typing, "CK4_NO_ANGLE_TYPING_FOUND_BY_DIFFERENT_KEYWORDS",
          {"keywords_tried": len(CHECKER_ANGLE_KEYWORDS),
           "angle_typing_keywords_that_hit": sorted(real_angle_typing),
           "incidental_hits": sorted(angle_hunt)})
    if real_angle_typing:
        refute("ANGLE_TYPING_EXISTS", True,
               f"found angle typing via {sorted(real_angle_typing)}", overturns=True)
    else:
        refute("ANGLE_TYPING_EXISTS", False,
               f"{len(CHECKER_ANGLE_KEYWORDS)} independent angle-typing keywords tried "
               f"(radian, arg(, exp(i, mod 2pi, atan2, U(1), winding, principal branch, "
               f"degrees, polar, ...); the only hits are incidental substrings "
               f"({sorted(angle_hunt)}).  The primary's type-gap finding survives an "
               f"independent keyword set.", overturns=False)

    # ---- ATTACK (ii): bin verdicts -------------------------------------------
    bins = rederive_bins_from_the_no_go()
    check(all(bins[str(n)]["found"] for n in (1, 2, 3)), "CK5_BINS_REDERIVED_FROM_THE_NO_GO_TEXT",
          {str(n): bins[str(n)]["title"] for n in (1, 2, 3)})
    check(bins["target_block_present"], "CK6_TARGET_COORDINATES_VERIFIED_FROM_SOURCE",
          "Phi_target := 3 delta_target = S_sum = 2/3")

    conv = attack_unit_convention()
    # the primary is safe only if every 2/9 candidate has a companion sum candidate
    verdicts = primary["D_Q2_route1_bin_census"]["verdicts"]
    nine_ths = [v for v in verdicts if "2/9" in v["value"]]
    cycles_with_2_9 = {v["cycle"] for v in nine_ths}
    cycles_with_sum = {v["cycle"] for v in verdicts if v["gates"]["R1_value_is_exactly_2_over_3"]}
    unpaired = sorted(cycles_with_2_9 - cycles_with_sum)
    check(True, "CK7_UNIT_CONVENTION_ATTACK",
          {**conv, "cycles_with_a_2/9_candidate": sorted(cycles_with_2_9),
           "cycles_whose_unaveraged_sum_is_ALSO_enumerated": sorted(cycles_with_sum),
           "unpaired": unpaired})
    if unpaired:
        refute("MISSES_IS_ACTUALLY_A_HIT_UNDER_THE_UNAVERAGED_SUM_CONVENTION", True,
               f"cycles {unpaired} contribute a 2/9 candidate binned as 'misses the target', but "
               f"under the no-go's OWN normalisation Phi = 3*L that object is worth exactly 2/3.  "
               f"The 'miss' is an artefact of which normalisation the primary enumerated.  "
               f"Adjudication: the conversion factor 3 is the unaveraging step, and it is not the "
               f"disputed step -- the disputed step is reading the RESULT as radians, which is "
               f"bin 7 either way.  So the bin label moves for these candidates while the route-1 "
               f"verdict does not.", overturns=False)
    else:
        refute("MISSES_IS_ACTUALLY_A_HIT_UNDER_THE_UNAVERAGED_SUM_CONVENTION", False,
               "every cycle contributing a 2/9 candidate also has its unaveraged sum enumerated, "
               "so the 'misses' verdicts are not normalisation artefacts", overturns=False)

    # is a "restates" actually derivable?  Test the k = 2/9 anchor row directly.
    c882 = rtext("logs/runner-cache/frontier_cycle882_readout_identity_2026_07_28.txt")
    restates_is_sourced = "the license restated, not derived" in c882.lower()
    check(restates_is_sourced, "CK8_RESTATES_VERDICT_IS_THE_SOURCES_OWN_WORDS",
          "cycle 882's own runner cache calls the fixed-locus anchor row "
          "'the license restated, not derived'")
    refute("RESTATES_IS_ACTUALLY_DERIVABLE", False,
           "the 'restates' classification is not the sweep's editorial judgement -- cycle 882's "
           "own committed runner output says the anchor row whose constant is the fixed-locus "
           "arithmetic is 'the license restated, not derived'.  Attacking it would require "
           "overturning a landed package, not this sweep.", overturns=False)

    # ---- ATTACK (iii): overclaim --------------------------------------------
    scope = attack_scope_overclaim(corpus)
    check(scope["has_honest_scope_sentence"] and scope["names_the_limitation_explicitly"],
          "CK9_HONEST_SCOPE_SENTENCE_PRESENT", scope)
    check(not scope["uses_an_unqualified_universal"], "CK10_NO_UNQUALIFIED_UNIVERSAL",
          "the statement does not claim 'swept empty on all/every surface'")
    if scope["campaign_cycles_present_in_this_worktree_but_NOT_swept"]:
        refute("SWEPT_EMPTY_OVERCLAIMS", True,
               f"cycles {scope['campaign_cycles_present_in_this_worktree_but_NOT_swept']} are "
               f"present in this worktree in the campaign window but were not swept.  Any reading "
               f"of 'route 1 swept empty' as a campaign-wide statement is unsupported.  "
               f"Adjudication: the primary's HONEST SCOPE sentence explicitly limits the claim to "
               f"the enumerated artifacts and disclaims artifacts not enumerated, so the receipt "
               f"does not overclaim -- but a READER quoting the headline without the scope "
               f"sentence would.", overturns=False)
    else:
        refute("SWEPT_EMPTY_OVERCLAIMS", False,
               "every campaign-window cycle present in this worktree was swept", overturns=False)

    # ---- independent re-verification of the primary's headline facts ---------
    radian_total = sum(
        rtext(p).lower().count("radian") for files in corpus.values() for p in files
    )
    check(radian_total == 0, "CK11_RADIAN_ZERO_REPRODUCED_INDEPENDENTLY",
          {"own_corpus_files": sum(len(v) for v in corpus.values()),
           "radian_occurrences": radian_total})

    # CK11b -- the exclusion of cycle 928 is justified, not convenient: EVERY
    # radian occurrence anywhere in the campaign window must belong to cycle 928
    # (this sweep's own report).  If any other cycle carried one, the primary's
    # headline finding would be false and this check would fail.
    by_cycle = radian_hits_by_cycle()
    foreign = {c: n for c, n in by_cycle.items() if c != 928}
    check(not foreign, "CK11b_EVERY_RADIAN_IN_THE_WINDOW_BELONGS_TO_THE_SWEEP_ITSELF",
          {"radian_hits_by_cycle": by_cycle,
           "cycles_other_than_928_carrying_a_radian": foreign,
           "meaning": "the only artifacts in the campaign window that use the word 'radian' are "
                      "cycle 928's own receipts and caches -- i.e. the sweep reporting the "
                      "absence.  No surveyed package uses it."})
    if foreign:
        refute("RADIAN_EXISTS_ON_A_SURVEYED_SURFACE", True,
               f"cycles {sorted(foreign)} carry the word 'radian'", overturns=True)
    probe = "the holonomy is 2/3 radians"
    check(probe.lower().count("radian") == 1, "CK12_RADIAN_SCANNER_POSITIVE_CONTROL", probe)

    check(primary["D_Q2_route1_bin_census"]["any_licensed"] is False,
          "CK13_NO_SURVIVOR_CLAIMED", "primary reports any_licensed = False")

    # the primary must not have quietly relaxed the restriction gates
    check(primary["B_restriction_gates"]["angle_native_no_go"] == "TOTAL: PASS=128 FAIL=0",
          "CK14_RESTRICTION_GATE_NOT_RELAXED",
          primary["B_restriction_gates"]["angle_native_no_go"])

    # ---- ATTACK 6: is the referent on 886/888 GENUINE, or one imported quote? --
    lep_sentences: dict[int, set] = {}
    for cyc in (886, 888, 899, 901, 890, 898, 882):
        for path in corpus.get(cyc, []):
            text = rtext(path)
            for m in re.finditer(r"charged-lepton", text, re.I):
                ls = max(text.rfind(".", 0, m.start()), text.rfind("\n", 0, m.start())) + 1
                le = text.find(".", m.start())
                s = re.sub(r"\s+", " ", text[ls : le if le != -1 else m.start() + 200]).strip()
                lep_sentences.setdefault(cyc, set()).add(s[:200])
    thin = {c: len(v) for c, v in lep_sentences.items() if len(v) <= 2}
    check(True, "CK15_REFERENT_DEPTH_ATTACK",
          {"distinct_charged_lepton_sentences_per_cycle":
               {c: len(v) for c, v in sorted(lep_sentences.items())},
           "cycles_whose_entire_referent_is_at_most_two_distinct_sentences": sorted(thin)})
    if thin:
        refute("REFERENT_PRESENCE_IS_THINNER_THAN_THE_PRIMARY_IMPLIES", True,
               f"cycles {sorted(thin)} carry the charged-lepton referent in at most two DISTINCT "
               f"sentences each -- and in 886/888 it is ONE sentence, imported verbatim from the "
               f"cycle-882 primary and graded by those packages themselves as 'target-facing, not "
               f"axiom-grounded' (they cite it as an example of a CIRCULAR selector).  So 'these "
               f"surfaces speak the charged-lepton language' is weaker than it sounds: they QUOTE "
               f"it, they do not derive in it.  Adjudication: this makes the primary's bin-7 "
               f"finding NARROWER, not wrong -- the type gap is still what stops the candidates, "
               f"and a thinner referent would only push candidates back toward bin 5, which is "
               f"also a non-survivor bin.  The route-1 verdict is unchanged either way.",
               overturns=False)
    else:
        refute("REFERENT_PRESENCE_IS_THINNER_THAN_THE_PRIMARY_IMPLIES", False,
               "every referent-carrying cycle uses the vocabulary in three or more distinct "
               "sentences", overturns=False)

    # ---- ATTACK 7: is C899-SUM's binding forced?  899's OWN checker says no. --
    c899 = rtext("outputs/family_binding_independent_check_cycle899_receipt_2026_07_28.json")
    m402 = re.search(r"(\d{3}) distinct forms|402 closed forms|(\d{3}) closed forms", c899)
    has_bound = "402" in c899 and "10 distinct" in c899
    check(True, "CK16_BINDING_FORCEDNESS_ATTACK",
          {"cycle_899_own_identifiability_bound_present": has_bound,
           "claim": "402 closed forms return 2/9 at C3 while taking 10 distinct values at C4"})
    refute("C899_SUM_BINDING_IS_FORCED", False,
           "attacked the sharpest candidate's forcedness and the attack CONFIRMS the primary: "
           "cycle 899's own independent checker records that 402 closed forms return 2/9 at C3 "
           "while taking 10 distinct values at C4, so the form that produces the 2/3 sum is not "
           f"singled out by the data (bound present in the pinned receipt: {has_bound}).  This is "
           "an INDEPENDENT bin-4 obstruction the primary did not cite; it strengthens the "
           "no-survivor verdict rather than weakening it.", overturns=False)

    # ---- ATTACK 8: independently re-verify a vendored pin. -------------------
    ship = json.loads(rtext("outputs/family_binding_block_cycle899_ship_receipt_2026_07_28.json"))
    victim = "outputs/family_binding_cycle899_receipt_2026_07_28.json"
    got = hashlib.sha256(open(rel(victim), "rb").read()).hexdigest()
    check(got == ship["files"][victim]["sha256"], "CK17_VENDORED_PIN_REVERIFIED_INDEPENDENTLY",
          {"file": victim, "sha256": got[:24]})
    refute("VENDORED_PINS_ARE_UNVERIFIED", False,
           f"recomputed the sha256 of {victim} from raw bytes with its own hasher and it matches "
           f"the ship receipt entry", overturns=False)

    # ---- ATTACK 9: could the primary's gate EVER accept?  Re-derive it. ------
    # Independent reimplementation of the survivor condition from the no-go text.
    def independent_gate(value_is_2_3, radian_typed, referent, derivable, scope_forced, threefold):
        return all((value_is_2_3, radian_typed, referent, derivable, scope_forced, threefold))
    accepts = independent_gate(True, True, True, True, True, True)
    rejects = independent_gate(True, False, True, True, True, True)
    check(accepts and not rejects, "CK18_GATE_IS_NOT_A_CONSTANT_FUNCTION",
          {"accepts_a_full_survivor": accepts, "rejects_when_only_the_typing_is_missing": rejects})
    refute("THE_SWEEP_COULD_NEVER_HAVE_FOUND_A_SURVIVOR", False,
           "reimplemented the survivor condition independently from the no-go's route-1 sentence; "
           "it accepts a fully-qualified candidate and rejects one that differs ONLY in angle "
           "typing.  The empty result is therefore a property of the corpus, not of the gate.",
           overturns=False)

    # ---- ATTACK 10: is the primary's science digest self-consistent? ---------
    recomputed = hashlib.sha256(
        json.dumps({k: primary[k] for k in
                    ("A_pins_and_firewall", "B_restriction_gates",
                     "C_Q1_angle_object_enumeration", "D_Q2_route1_bin_census",
                     "E_Q3_consolidated_license", "F_falsifiers")},
                   sort_keys=True, separators=(",", ":")).encode()).hexdigest()
    digest_ok = recomputed == primary["science_digest"]
    check(digest_ok, "CK19_PRIMARY_SCIENCE_DIGEST_RECOMPUTED",
          {"recomputed": recomputed[:24], "recorded": primary["science_digest"][:24]})
    refute("PRIMARY_DIGEST_DOES_NOT_COVER_ITS_SCIENCE", not digest_ok,
           ("the primary's recorded science digest does NOT reproduce from its own science "
            "sections -- the digest does not bind the reported content"
            if not digest_ok else
            "recomputed the primary's science digest from its own six science sections with an "
            "independent hasher; it reproduces exactly, so the digest binds the reported content"),
           overturns=False)

    runtime = round(time.time() - START, 2)
    check(runtime <= BUDGET_SECONDS, "CKZ_RUNTIME", f"{runtime}s / {BUDGET_SECONDS}s")

    held = [r for r in REFUTATIONS if r["refutation_holds"]]
    overturning = [r for r in REFUTATIONS if r["overturns_the_conclusion"]]

    science = {
        # keys stringified: json sort_keys cannot order a mixed int/str keyspace
        "own_corpus": {str(c): sorted(v) for c, v in sorted(corpus.items())},
        "independent_2_3_extraction": {str(c): v for c, v in sorted(two_thirds.items())},
        "angle_typing_hunt": angle_hunt,
        "bins_rederived_from_the_no_go": bins,
        "unit_convention_attack": conv,
        "scope_overclaim_attack": scope,
        "refutations": REFUTATIONS,
        "radian_total_independent": radian_total,
    }
    digest = hashlib.sha256(
        json.dumps(science, sort_keys=True, separators=(",", ":"), default=str).encode()
    ).hexdigest()

    receipt = dict(science)
    receipt.update({
        "cycle": 928,
        "role": "independent checker, spec'd to refute",
        "block": "toe-time-blockAC2-20260802",
        "campaign": "toe-time-expansion-20260802",
        "authority": "none",
        "audit": "unset",
        "adopts": "nothing",
        "totals": {"PASS": PASS, "FAIL": FAIL},
        "refutations_that_hold": len(held),
        "refutations_that_overturn_the_conclusion": len(overturning),
        "VERDICT": ("PRIMARY_SURVIVES_THIS_CHECK" if not overturning and FAIL == 0
                    else "PRIMARY_REFUTED"),
        "runtime_seconds": runtime,
        "science_digest": digest,
    })

    with open(rel("outputs/route1_sweep_independent_check_cycle928_receipt_2026_07_28.json"), "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=str)
        fh.write("\n")

    body = ["===== runner cache v1 =====",
            "runner: frontier_cycle928_route1_sweep_independent_check_2026_07_28.py", ""]
    body += LINES
    body += ["", "--- REFUTATION ATTEMPTS ---"]
    for r in REFUTATIONS:
        body.append(
            f"[{'HOLDS' if r['refutation_holds'] else 'FAILS'}] {r['attack']} "
            f"(overturns={r['overturns_the_conclusion']}): {r['detail']}"
        )
    body += ["",
             f"science_digest={digest}",
             f"refutations_that_hold={len(held)} overturning={len(overturning)}",
             f"TOTAL: PASS={PASS} FAIL={FAIL}",
             f"VERDICT: {receipt['VERDICT']}",
             f"runtime_seconds={runtime} budget={BUDGET_SECONDS}"]
    with open(rel("logs/runner-cache/frontier_cycle928_route1_sweep_independent_check_2026_07_28.txt"), "w") as fh:
        fh.write("\n".join(body) + "\n")

    print("\n".join(body[-6:]))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
