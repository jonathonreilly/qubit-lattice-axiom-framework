"""Cycle 875: the B-AXIS second-leg discharge certificate (SUPPORT, not a theorem).

WHAT THIS IS.  The ANOMALY_FORCES_TIME theorem carries a declared premise
B-AXIS.  Cycle 864's certificate D_B_AXIS_CONTACT states the condition under
which that premise would stop being a premise, and splits it into two legs:
(i) the landed temporal laws restate in record-time, and (ii) the axis admits
no second record-clock.  Leg (i) is the 863-865 arc's evidence.  Leg (ii) was
declared UNTESTED there and handed to the scaled-bank construction.

This runner ASSEMBLES leg (ii): it quotes the premise and the two legs from
their pinned sources, formalizes leg (ii) as a decidable statement at a
declared scope, and classifies each leg-(ii) obligation as DISCHARGED_AT_SCOPE
or OPEN against re-derived witnesses.

WHAT THIS IS NOT.  This is an assembly certificate.  It does not promote
B-AXIS to derived and it does not claim leg (ii) is closed.  The premise
standing it emits is computed from the obligation table and is expected to
remain NOT_DISCHARGED while any obligation is OPEN.  The standing is NOT
compared against any desired value anywhere in this file: every integrity gate
tests reproducibility, quote fidelity, arithmetic identity or provenance, and
never tests for a preferred verdict.

EVIDENCE PROVENANCE.  The 863-866 artifacts were produced on sibling branches
(physics-loop/proof-grade-blockP24/P25-20260729, toe-time-blockF1-20260802) and
are NOT present in this branch's working tree.  Byte-exact copies are committed
under outputs/cycle875_pinned_evidence/ and every copy is verified here against
the declared git blob sha1 of the original object, which proves the copy is
byte-identical to the artifact at the named commit.  Nothing is trusted: the
blob sha1 is recomputed from the bytes on disk, not asked of git.

RE-DERIVATION POLICY.  Cheap witnesses are re-run: the Cycle-869 primary
(~9s) is executed as a subprocess and its stdout compared against the pinned
cache byte-for-byte.  Expensive witnesses (866 at 178s, 865 inside the arc)
are quoted from their sha-verified caches, and every headline number quoted is
independently RECOMPUTED from the payload it summarizes, so a mislabelled
headline is caught rather than repeated.

CERTIFICATES
  A_QUOTE_FIDELITY        the premise text and both legs are literal
                          substrings of their pinned sources, at recorded
                          byte offsets.
  B_FAMILY_DECLARATION    the declared candidate family is re-derived from
                          source (AST + payload), not asserted.
  C_LEG_II_FORMALIZATION  leg (ii) stated as a decidable predicate at the
                          declared scope, with its obligation decomposition.
  D_WITNESS_REDERIVATION  every quoted headline recomputed from its payload;
                          agreement recorded per witness.
  E_LIVE_REDERIVATION     the Cycle-869 primary re-run and diffed.
  F_DISCHARGE_MAP         per-obligation status with supporting artifact+sha.
  G_CONTROLS              shas, blobs, blocklist, determinism, budgets.
"""
from __future__ import annotations

import ast
from fractions import Fraction
from hashlib import sha1, sha256
from itertools import combinations
import json
from pathlib import Path
import re
import subprocess
import sys
import time


ROOT = Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC = 1400
STDOUT_LIMIT_BYTES = 150 * 1024

PREMISE_DOC = "docs/ANOMALY_FORCES_TIME_THEOREM.md"
PRIMARY_869 = "scripts/frontier_cycle869_clock_relation_2026_07_28.py"
CACHE_869 = "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt"
EV = "outputs/cycle875_pinned_evidence"
ARC_NOTE = f"{EV}/arc_note_863_865.md"
ARC_CHECK_CACHE = f"{EV}/cache_863_865_arc_check.txt"
CACHE_864 = f"{EV}/cache_864_laws_in_record_time.txt"
CACHE_865 = f"{EV}/cache_865_offset_law.txt"
SRC_ARC_CHECK = f"{EV}/src_863_865_arc_check.py"
CACHE_866 = f"{EV}/cache_866_scaled_banks.txt"
SRC_866 = f"{EV}/src_866_scaled_banks.py"

AUDIT_INPUT_PATHS = (
    "docs/ANOMALY_FORCES_TIME_THEOREM.md",
    "scripts/frontier_cycle869_clock_relation_2026_07_28.py",
    "logs/runner-cache/frontier_cycle869_clock_relation_2026_07_28.txt",
    "outputs/cycle875_pinned_evidence/arc_note_863_865.md",
    "outputs/cycle875_pinned_evidence/cache_863_865_arc_check.txt",
    "outputs/cycle875_pinned_evidence/cache_864_laws_in_record_time.txt",
    "outputs/cycle875_pinned_evidence/cache_865_offset_law.txt",
    "outputs/cycle875_pinned_evidence/cache_866_scaled_banks.txt",
    "outputs/cycle875_pinned_evidence/src_863_865_arc_check.py",
    "outputs/cycle875_pinned_evidence/src_866_scaled_banks.py",
)
DECLARED_INPUT_PATHS = AUDIT_INPUT_PATHS

EXPECTED_SHA256 = {
    PREMISE_DOC:
        "792e9c3d009c87529bd233ade9f191d76d9b1e1590e8073562644f0181a37b00",
    PRIMARY_869:
        "1406bf829b19bb8ff9765b4f3e23a499467db98a6753e0b7d07cd983fab2f493",
    CACHE_869:
        "ea19cd18c30c769453e2e15a9186449712ef8b99535234fde25b2073f1efa1fd",
    ARC_NOTE:
        "ce7274e92893f79064f99d4d246e2a25396f96f3ac2b2f97e0c110bdcc2af273",
    ARC_CHECK_CACHE:
        "75104f5d11749e378d447da4b930cd0456f60fe85e41b5c73c59657d9cae8a90",
    CACHE_864:
        "23adfab12899300445f00df870a89f19bb65903c1485b530631febd32fd3860f",
    CACHE_865:
        "c778ca722a80d7e45976ba5da1ab5c80cbce583b262c1a10c0e0fead8c85ef79",
    CACHE_866:
        "743e01f75fd7ccc0da42c3350273851ed44f2a97a850e08fc8ae8ff7de0c3ef4",
    SRC_ARC_CHECK:
        "d0c62a4388e90800e09d357757df0f3c32f47564c607c359c275c0674f42ed37",
    SRC_866:
        "c96160b54e746a44b7b259c4dbcfaf8fd03fe30787ec5c2ab9dd93ace3809cf1",
}

# Cross-branch provenance.  local evidence path -> (commit, original path,
# git blob sha1 of the original object).  The blob sha1 is recomputed from the
# committed bytes; agreement proves byte-identity with the named commit's blob.
PINNED_PROVENANCE = {
    ARC_NOTE: (
        "fd94927ca125764b0eb37eaf47b47763e145ef15",
        "docs/TIME_FROM_RECORDS_ARC_CYCLES863_865_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "88869e97ba2caa00b1331c1503aa6d57c0200074",
    ),
    ARC_CHECK_CACHE: (
        "fd94927ca125764b0eb37eaf47b47763e145ef15",
        "logs/runner-cache/frontier_cycle863_865_arc_independent_check_2026_07_28.txt",
        "6c471a1f3c1c560a95007458a6058ef16020962e",
    ),
    CACHE_864: (
        "fd94927ca125764b0eb37eaf47b47763e145ef15",
        "logs/runner-cache/frontier_cycle864_laws_in_record_time_2026_07_28.txt",
        "c4111a30a66888e51367412411089c9d0b0d86bf",
    ),
    CACHE_865: (
        "fd94927ca125764b0eb37eaf47b47763e145ef15",
        "logs/runner-cache/frontier_cycle865_offset_law_2026_07_28.txt",
        "13814e58dbce06cb4614c058ec7661d85ef760cf",
    ),
    SRC_ARC_CHECK: (
        "fd94927ca125764b0eb37eaf47b47763e145ef15",
        "scripts/frontier_cycle863_865_arc_independent_check_2026_07_28.py",
        "90ec71f825df20d36ed0c431189c174884f93e23",
    ),
    CACHE_866: (
        "a64676cf7795377074975c5686b5e83f686f6ab3",
        "logs/runner-cache/frontier_cycle866_scaled_banks_2026_07_28.txt",
        "4506f4c7090ad24469bc5b9516802900f5eac183",
    ),
    SRC_866: (
        "7ad5231f6160d5513ca0c502b79413bdd689ab8e",
        "scripts/frontier_cycle866_scaled_banks_2026_07_28.py",
        "34f2fc8c8ef22dab7e46f2f6164640301a19674c",
    ),
}

# Pinned sources are EVIDENCE, never code.  They are read as bytes/AST only.
BLOCKLISTED_MODULES = (
    "frontier_cycle863_865_arc_independent_check_2026_07_28",
    "frontier_cycle866_scaled_banks_2026_07_28",
    "frontier_cycle869_clock_relation_2026_07_28",
)

STATIONS = 19

# ---------------------------------------------------------------- the quotes
# Each entry: (label, source path, the literal text that must appear verbatim).
QUOTES = (
    (
        "B_AXIS_PREMISE_ROW",
        PREMISE_DOC,
        "**Declared premise:** one supplied blocked time step, one declared "
        "evolution axis/transfer construction, and no admitted independent "
        "commuting transfer factor as a second clock. This gives the local "
        "conditional cap `d_t <= 1` used here.",
    ),
    (
        "B_AXIS_NONCIRCULARITY",
        PREMISE_DOC,
        "No\n   anomaly trace, no chirality argument, and no content of this "
        "note\n   enters that supplied axis premise.",
    ),
    (
        "LEG_STATEMENT_864D",
        CACHE_864,
        "B-AXIS discharges (premise -> derived) iff the evolution axis is "
        "CONSTITUTED by the record order: (i) the landed temporal laws restate "
        "in record-time coordinates (certificates A/B here), and (ii) the axis "
        "admits no second record-clock (the single-clock content) \\u2014 "
        "condition (ii) is untested here and remains the open leg",
    ),
    (
        "LEG_OWNERSHIP_864D",
        CACHE_864,
        "A and B are the (i)-leg evidence; C scopes the gauge remainder; the "
        "(ii)-leg needs the scaled-bank construction",
    ),
    (
        "LEG_STATEMENT_ARC_NOTE",
        ARC_NOTE,
        "the ANOMALY_FORCES_TIME theorem's\n  B-AXIS premise discharges iff "
        "(i) the laws restate in record-time\n  — the (i)-leg evidence is "
        "this arc — and (ii) no second record\n  clock exists — "
        "untested, owned by the scaled-bank construction.",
    ),
    (
        "ARC_NEGATIVE_DISCIPLINE",
        ARC_NOTE,
        "the intrinsic-predictor exhaustion is\nat the declared 29+28 family",
    ),
    (
        "F_CLOSURE_869",
        CACHE_869,
        "a negative priced to F and its caps, not a claim about all "
        "conceivable transformations.",
    ),
    (
        "WHAT_A_NEGATIVE_COSTS_869",
        CACHE_869,
        "It does not exclude transformations outside F, nor relations that "
        "only appear beyond tick 8192.",
    ),
)

# ------------------------------------------------- the leg-(ii) formalization
LEG_II_FORMAL = (
    "LEG (ii), DECIDABLE FORM AT DECLARED SCOPE.  Fix a substrate scope S (a "
    "bank count B and a census of keys/worlds), a declared candidate family C "
    "of record-native constructions, and the declared relation family F with "
    "its caps.  Say a member c of C DEFINES A SECOND GLOBAL TIME on S when all "
    "three hold: (a) RECORD-NATIVE -- c is computable from the record stream "
    "alone, with no scheduler-valued or otherwise gauge input; (b) GLOBAL -- c "
    "assigns a tick to every key of the census of S, not to a sub-population; "
    "(c) INDEPENDENT -- c is not carried onto the record-time clock by any "
    "exact member of F, i.e. c is not that clock re-zeroed, re-lagged by whole "
    "orbits, or otherwise F-equivalent to it.  Then LEG_II(S, C, F) := 'no "
    "member of C defines a second global time on S'.  Because C, F and S are "
    "finite and declared, LEG_II(S, C, F) is decidable by exhaustion, and that "
    "exhaustion is exactly what the pinned artifacts ran."
)
LEG_II_PRICE = (
    "LEG_II is a statement ABOUT C, F and S.  It is not the leg (ii) of the "
    "864-D condition, which quantifies over all record structures at all "
    "scales.  The gap between them is the family-closure caveat and the scope "
    "caveat, both carried as OPEN obligations below.  No accumulation of "
    "DISCHARGED_AT_SCOPE rows closes either."
)

STATUS_VALUES = ("DISCHARGED_AT_SCOPE", "OPEN", "PERMANENTLY_OPEN")


def compact(value) -> str:
    return json.dumps(value, sort_keys=True, separators=(",", ":"))


def digest(value) -> str:
    return sha256(compact(value).encode()).hexdigest()[:16]


def git_blob(payload: bytes) -> str:
    return sha1(b"blob %d\0" % len(payload) + payload).hexdigest()


def literal_assignment(tree, name):
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    try:
                        return ast.literal_eval(node.value)
                    except ValueError:
                        return None
    return None


def tuple_element_prefixes(tree, name):
    """Leading literal chunk of every element of a tuple assignment.

    FAMILY's entries interpolate declared caps, so the tuple is not a
    literal.  Its member codes still live in the first plain-string chunk of
    each entry, which is what this reads -- from the AST, never from a
    restatement of the family in this file.
    """
    for node in ast.walk(tree):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    if not isinstance(node.value, (ast.Tuple, ast.List)):
                        return None
                    out = []
                    for element in node.value.elts:
                        if isinstance(element, ast.Constant):
                            out.append(element.value)
                        elif isinstance(element, ast.JoinedStr) and element.values:
                            head = element.values[0]
                            out.append(head.value
                                       if isinstance(head, ast.Constant) else "")
                        else:
                            out.append("")
                    return tuple(out)
    return None


def cache_stdout(text: str) -> str:
    """The stdout section of a runner-cache v1 file."""
    head = "----- stdout -----\n"
    tail = "\n----- stderr -----"
    start = text.index(head) + len(head)
    end = text.index(tail, start)
    return text[start:end]


def cache_field(text: str, key: str):
    """Parse `<KEY> <json>` or `CERTIFICATE <KEY> PASS <json>` from a cache."""
    for line in cache_stdout(text).splitlines():
        for prefix in (f"CERTIFICATE {key} PASS ", f"CERTIFICATE {key} FAIL ",
                       f"{key} ", f"PASS {key} :: ", f"FAIL {key} :: "):
            if line.startswith(prefix):
                return json.loads(line[len(prefix):])
    return None


# ================================================================ certificates
def a_quote_fidelity(payloads):
    rows = []
    for label, path, text in QUOTES:
        raw = payloads[path].decode()
        offset = raw.find(text)
        rows.append({
            "label": label,
            "source": path,
            "found": offset >= 0,
            "byte_offset": offset,
            "quote_sha256": sha256(text.encode()).hexdigest()[:16],
            "quote_chars": len(text),
        })
    result = {
        "certificate": "A_QUOTE_FIDELITY",
        "quotes": tuple(rows),
        "all_located": all(row["found"] for row in rows),
        "policy": (
            "Every quoted string must occur VERBATIM in the sha-verified bytes "
            "of its pinned source.  A quote that has been paraphrased, "
            "re-wrapped or re-encoded fails here."
        ),
    }
    result["pass"] = result["all_located"]
    return result


def b_family_declaration(payloads):
    """Re-derive the declared candidate family from source, never assert it."""
    arc_src = ast.parse(payloads[SRC_ARC_CHECK], filename=SRC_ARC_CHECK)
    src866 = ast.parse(payloads[SRC_866], filename=SRC_866)
    src869 = ast.parse(payloads[PRIMARY_869], filename=PRIMARY_869)

    # --- 865 predictor family: singles from the cache payload, pairs from the
    # literal pair_pool in the checker source (C(8,2)).
    hunt = cache_field(payloads[ARC_CHECK_CACHE].decode(),
                       "THE_INTRINSIC_PREDICTOR_HUNT")
    singles_from_payload = len(hunt["expanded_candidates"])
    pair_pool = None
    for node in ast.walk(arc_src):
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == "pair_pool":
                    pair_pool = ast.literal_eval(node.value)
    pairs_from_source = (len(list(combinations(pair_pool, 2)))
                         if pair_pool else None)
    f865 = {
        "scope": "B=2 (two-bank), the 863-865 arc census",
        "singles_claimed": hunt["expanded_candidate_count"],
        "singles_recounted_from_payload": singles_from_payload,
        "singles_agree": (hunt["expanded_candidate_count"]
                          == singles_from_payload),
        "pairs_claimed": hunt["pair_candidates_tested_if_needed"],
        "pair_pool_size_from_source": len(pair_pool) if pair_pool else None,
        "pairs_recomputed_C_n_2": pairs_from_source,
        "pairs_agree": (hunt["pair_candidates_tested_if_needed"]
                        == pairs_from_source),
        "scheduler_excluded_as_not_record_native": (
            hunt["scheduler_gap_is_record_native"] is False),
        "verdict": hunt["verdict"],
    }

    # --- 866 sync-cadence structures: bank counts and the probe declared in
    # the primary's own literals.
    bank_counts = literal_assignment(src866, "BANK_COUNTS")
    c866 = json.loads(payloads[CACHE_866].decode()
                      .split("CERTIFICATE B3_RESULTS PASS ")[1].splitlines()[0])
    c866_b4 = json.loads(payloads[CACHE_866].decode()
                         .split("CERTIFICATE B4_RESULTS PASS ")[1]
                         .splitlines()[0])
    f866 = {
        "scope": f"B in {list(bank_counts)} (scaled-bank construction)",
        "bank_counts_from_source": list(bank_counts),
        "horizon_from_source": literal_assignment(src866, "HORIZON"),
        "store_cap_from_source": literal_assignment(src866, "STORE_CAP"),
        "events_from_source": list(literal_assignment(src866, "EVENTS_USED")),
        "structures": [
            "ALLSYNC_CADENCE: the all-bank synchronization cadence "
            "(B_DERIVED_CLOCK_AT_SCALE)",
            "PAIR_CADENCES: disjoint bank-pair sync sequences "
            "(C_SECOND_CLOCK_TEST)",
            "BIRTH_DATUM_PATTERN: the record-native per-world origin "
            "candidate (D_BIRTH_DATUM_INTRINSIC)",
        ],
        "pair_count_B3": len(c866["second_clock"]["pair_dominant_gaps"]),
        "pair_count_B4": len(c866_b4["second_clock"]["pair_dominant_gaps"]),
        "granularity": (
            "866's pair-cadence comparison is at TOP-3 DOMINANT-GAP "
            "granularity.  It is a cadence-signature probe, not a relation-"
            "family search: it cannot certify that two cadences are the same "
            "clock, only that their dominant-gap signatures differ or agree."
        ),
    }

    # --- 869 clock-dictionary family F and its caps, from the primary's AST.
    family = tuple_element_prefixes(src869, "FAMILY")
    members = tuple(entry.split()[0] for entry in family if entry.split())
    f869 = {
        "scope": f"B={literal_assignment(src869, 'FIXTURE_BANKS')} "
                 f"(stations={literal_assignment(src869, 'STATIONS')})",
        "F_members": list(members),
        "F_size": len(members),
        "horizon_chunks": literal_assignment(src869, "HORIZON_CHUNKS"),
        "evidence_floor": literal_assignment(src869, "EVIDENCE_FLOOR"),
        "min_lag_overlap": literal_assignment(src869, "MIN_LAG_OVERLAP"),
        "across_key_rep_cap": literal_assignment(src869, "ACROSS_KEY_REP_CAP"),
        "windowed_offset_anchors": literal_assignment(
            src869, "WINDOWED_OFFSET_ANCHORS"),
        "closure_declared": literal_assignment(src869, "FAMILY_CLOSURE"),
    }

    result = {
        "certificate": "B_FAMILY_DECLARATION",
        "candidate_family_865_predictors": f865,
        "candidate_family_866_sync_cadences": f866,
        "relation_family_869_clock_dictionary": f869,
        "note": (
            "C = (865 predictor family) U (866 sync-cadence structures) U "
            "(869 clock corpus); F = the 869 relation family.  Every element "
            "above is read out of a sha-verified source or payload; none is "
            "restated from the campaign brief."
        ),
    }
    result["pass"] = bool(
        f865["singles_agree"] and f865["pairs_agree"]
        and f865["scheduler_excluded_as_not_record_native"]
        and bank_counts and f866["pair_count_B3"] == 3
        and f866["pair_count_B4"] == 6
        and f869["F_size"] == 7 and f869["closure_declared"]
    )
    return result


def c_leg_ii_formalization():
    result = {
        "certificate": "C_LEG_II_FORMALIZATION",
        "statement": LEG_II_FORMAL,
        "price": LEG_II_PRICE,
        "decidability": (
            "finite declared C, finite declared F, finite declared census S; "
            "each membership test is an exact search over a declared "
            "parameter range, so LEG_II(S,C,F) is decided by exhaustion"
        ),
        "conjuncts": ["RECORD_NATIVE", "GLOBAL", "INDEPENDENT_OF_F"],
        "claim_type": "SUPPORT",
        "not_a_theorem": (
            "This cycle binds landed results to a named premise.  It derives "
            "no new physical content and promotes no premise."
        ),
    }
    result["pass"] = bool(
        len(result["conjuncts"]) == 3
        and "decidable by exhaustion" in LEG_II_FORMAL
        and result["claim_type"] == "SUPPORT"
    )
    return result


def d_witness_rederivation(payloads):
    """Recompute every quoted headline from the payload it summarizes."""
    c869 = payloads[CACHE_869].decode()
    pair_of_pairs = cache_field(c869, "D_WITHIN_KEY_PAIR_OF_PAIRS")
    bank_clocks = cache_field(c869, "E_WITHIN_KEY_BANK_CLOCKS")
    across = cache_field(c869, "F_ACROSS_KEYS")
    verdict = cache_field(c869, "G_RELATION_VERDICT")

    checks = []

    def note(name, claimed, recomputed, how):
        checks.append({
            "witness": name, "claimed": claimed, "recomputed": recomputed,
            "agree": claimed == recomputed, "how": how,
        })

    # W1 866 pair-cadence signature distinctness, recomputed from the payload.
    # The birth-datum nativity values are RECORDED, not gated: a True there
    # would change the obligation status downstream, never fail this check.
    c866_text = payloads[CACHE_866].decode()
    birth_native_by_B = {}
    for B in (3, 4):
        payload = json.loads(
            c866_text.split(f"CERTIFICATE B{B}_RESULTS PASS ")[1].splitlines()[0]
        )
        gaps = payload["second_clock"]["pair_dominant_gaps"]
        recomputed = len({compact(v) for v in gaps.values()})
        note(f"866_B{B}_distinct_pair_cadence_signatures",
             payload["second_clock"]["distinct_pair_cadence_signatures"],
             recomputed,
             "count distinct top-3 dominant-gap signatures over the pair map")
        birth_native_by_B[str(B)] = {
            "native_pattern_functional":
                payload["birth_datum"]["native_pattern_functional"],
            "gauge_e1_functional": payload["birth_datum"]["gauge_e1_functional"],
            "first_allsync_equals_e2":
                payload["derived_clock"]["first_allsync_equals_e2"],
            "allsync_on_tick_fraction":
                payload["derived_clock"]["allsync_on_tick_fraction"],
        }

    # W2 869 within-key bookkeeping identities.
    for name, cert, families in (("pair_clocks", pair_of_pairs, 3),
                                 ("bank_clocks", bank_clocks, 3)):
        split = cert["evidence_split"]
        note(f"869_{name}_comparable_equals_split_total",
             cert["comparable_pairs_of_clocks"], sum(split.values()),
             "comparable pairs must equal the sum of the evidence split")
        substantive = sum(v for k, v in split.items()
                          if not k.startswith("THIN"))
        note(f"869_{name}_substantive_equals_nonthin",
             cert["substantive_pairs_of_clocks"], substantive,
             "substantive pairs must equal the non-THIN evidence rows")
        note(f"869_{name}_verdicts_cover_the_corpus",
             sum(cert["verdicts"].values()), 304 * families,
             "verdict counts must cover every key x clock-pair slot")

    # W3 the single within-key non-identity dictionary, and its commensurability.
    hist = pair_of_pairs["witness_parameter_histogram"]
    nonidentity = {k: v for k, v in hist.items()
                   if k.startswith(("F1:", "F2", "F3:"))
                   and not k.endswith(("c=0", "L=0,d=0"))}
    note("869_pair_clocks_nonidentity_full_dictionaries",
         pair_of_pairs["substantive_nonidentity_full_dictionaries"],
         sum(nonidentity.values()),
         "count full-dictionary witnesses whose parameters move the ticks")
    lags = [int(k.split("d=")[1]) for k in nonidentity]
    note("869_nonidentity_lags_are_whole_orbits",
         True, all(abs(d) % STATIONS == 0 for d in lags),
         f"every tick-moving witness offset divisible by stations={STATIONS}")
    orbit_counts = {str(d): str(Fraction(abs(d), STATIONS)) for d in lags}

    # W4 across-key: recompute the headline totals over the FULL corpus.
    full_edges = full_nonzero = full_outside = full_f3 = 0
    per_family = {}
    for fam in ("bank_clocks", "pair_clocks"):
        for label, payload in across[fam].items():
            edges = payload["F1_edges_to_class_representative"]
            outside = payload["sounding_keys"] - payload["keys_in_nontrivial_F1_class"]
            per_family[f"{fam}:{label}"] = {
                "F1_edges": edges,
                "F1_edges_nonzero_offset": payload["F1_edges_with_nonzero_offset"],
                "F1_edges_zero_offset": payload[
                    "F1_edges_with_zero_offset_identical_cadences"],
                "keys_outside_any_nontrivial_F1_class": outside,
                "F3_factor_edges": payload["F3_factor_edges_between_distinct_words"],
            }
            full_edges += edges
            full_nonzero += payload["F1_edges_with_nonzero_offset"]
            full_outside += outside
            full_f3 += payload["F3_factor_edges_between_distinct_words"]
    pair_edges = sum(v["F1_edges"] for k, v in per_family.items()
                     if k.startswith("pair_clocks"))
    pair_outside = sum(v["keys_outside_any_nontrivial_F1_class"]
                       for k, v in per_family.items()
                       if k.startswith("pair_clocks"))
    note("869_headline_across_key_F1_edges_is_pair_clocks_only",
         verdict["across_key_F1_edges"], pair_edges,
         "the G-certificate headline recomputed over PAIR clocks alone")
    note("869_headline_keys_outside_is_pair_clocks_only",
         verdict["across_key_keys_outside_any_nontrivial_F1_class"],
         pair_outside,
         "the G-certificate outside-count recomputed over PAIR clocks alone")
    note("869_full_corpus_every_F1_edge_carries_nonzero_offset",
         full_edges, full_nonzero,
         "over bank AND pair clocks, F1 edge count vs nonzero-offset count")

    # W5 period commensurability, recomputed from the period census.
    periods = verdict["nondegenerate_periods_in_corpus"]
    note("869_every_nondegenerate_period_is_whole_orbits",
         verdict["every_nondegenerate_period_is_whole_orbits"],
         all(row["period_ticks"] % STATIONS == 0 for row in periods),
         f"every corpus period divisible by stations={STATIONS}")
    note("869_period_orbit_counts",
         [row["orbits"] for row in periods],
         [str(row["period_ticks"] // STATIONS) for row in periods],
         "orbit counts recomputed as period_ticks / stations")

    # W6 865 hunt outcome.  RECORDED, not gated, for the same reason as W1:
    # a selected predictor would change O2's status, not fail this check.
    hunt = cache_field(payloads[ARC_CHECK_CACHE].decode(),
                       "THE_INTRINSIC_PREDICTOR_HUNT")
    hunt_outcome = {
        "verdict": hunt["verdict"],
        "selected_predictor": hunt["selected_predictor"],
        "nonvacuous_intrinsic_singles": len(hunt["nonvacuous_intrinsic_singles"]),
        "nonvacuous_intrinsic_pairs": len(hunt["nonvacuous_intrinsic_pairs"]),
        "scheduler_gap_is_record_native": hunt["scheduler_gap_is_record_native"],
    }

    findings = []
    if not next(c for c in checks
                if c["witness"].endswith("F1_edges_is_pair_clocks_only"))["agree"]:
        findings.append("869 across-key headline scope not reproduced")
    findings.append(
        f"SCOPE FINDING: the 869 G-certificate headline "
        f"'across_key_F1_edges={verdict['across_key_F1_edges']}' and "
        f"'keys outside any nontrivial F1 class="
        f"{verdict['across_key_keys_outside_any_nontrivial_F1_class']}' are "
        f"PAIR-CLOCK figures.  Over the full across-key corpus (bank AND pair "
        f"clocks) the totals are {full_edges} F1 edges, {full_nonzero} of them "
        f"with nonzero offset, and {full_outside} keys outside any nontrivial "
        f"F1 class.  The kind of the conclusion is unchanged -- every single "
        f"across-key F1 edge moves the origin -- but the uncovered residue is "
        f"{Fraction(full_outside, verdict['across_key_keys_outside_any_nontrivial_F1_class'])}"
        f"x the headline figure, and obligation O7 is priced to the larger one."
    )
    findings.append(
        f"NON-TRANSLATION RESIDUE: {full_f3} across-key F3 factor edges relate "
        f"distinct gap words by index lag plus offset.  These are relations, "
        f"so they unify rather than split clocks, but they are NOT pure time "
        f"translations, so 'CROSS_KEY_TIME_TRANSLATION_DICTIONARY' describes "
        f"the F1 layer only."
    )

    result = {
        "certificate": "D_WITNESS_REDERIVATION",
        "checks": tuple(checks),
        "agreements": sum(1 for c in checks if c["agree"]),
        "disagreements": tuple(c["witness"] for c in checks if not c["agree"]),
        "across_key_per_family": per_family,
        "across_key_full_corpus": {
            "F1_edges": full_edges, "F1_edges_nonzero_offset": full_nonzero,
            "keys_outside_any_nontrivial_F1_class": full_outside,
            "F3_factor_edges": full_f3,
        },
        "nonidentity_witness_orbit_counts": orbit_counts,
        "birth_datum_by_B_866": birth_native_by_B,
        "intrinsic_hunt_outcome_865": hunt_outcome,
        "findings": findings,
    }
    # Gate: every recomputation must EXECUTE and agree.  A disagreement is a
    # real defect in a quoted number and must stop the certificate.
    result["pass"] = bool(checks) and not result["disagreements"]
    return result


TIMING_FIELD = re.compile(
    r'"(runtime_seconds|elapsed_seconds|runtime|elapsed)":\s*-?[0-9]+(\.[0-9]+)?'
)
# A runner that reports its own stdout size cannot reproduce that number once
# a wall-clock number of a different string length is embedded in it.  This
# field is masked ONLY when its drift is exactly accounted for by the timing
# drift (see length_delta_fully_explained below), never unconditionally.
SELFSIZE_FIELD = re.compile(r'"(stdout_bytes)":\s*[0-9]+')


def mask_timing(text: str) -> str:
    return TIMING_FIELD.sub(lambda m: f'"{m.group(1)}":TIMING', text)


def mask_selfsize(text: str) -> str:
    return SELFSIZE_FIELD.sub(lambda m: f'"{m.group(1)}":SELFSIZE', text)


def mask_all(text: str) -> str:
    return mask_selfsize(mask_timing(text))


def e_live_rederivation(payloads):
    """Re-run the cheap Cycle-869 primary and diff against its pinned cache.

    Wall-clock fields cannot reproduce, so they are MASKED -- and the mask is
    then audited: every raw differing line must become equal under the timing
    mask alone.  A substantive drift therefore cannot hide behind the mask.
    """
    started = time.monotonic()
    proc = subprocess.run(
        [sys.executable, str(ROOT / PRIMARY_869)],
        capture_output=True, cwd=str(ROOT), timeout=600,
    )
    elapsed = round(time.monotonic() - started, 3)
    live = proc.stdout.decode()
    pinned = cache_stdout(payloads[CACHE_869].decode())
    live_lines, pinned_lines = live.splitlines(), pinned.splitlines()
    differing = [i for i, (a, b) in enumerate(zip(live_lines, pinned_lines))
                 if a != b]
    explained = [i for i in differing
                 if mask_all(live_lines[i]) == mask_all(pinned_lines[i])]

    # Exact accounting for the two masked fields.  The whole raw length drift
    # must be attributable to the wall-clock strings, and the runner's own
    # stdout_bytes claim must have drifted by exactly that same amount.
    live_t = TIMING_FIELD.findall(live)
    pinned_t = TIMING_FIELD.findall(pinned)
    timing_len_delta = None
    if len(live_t) == len(pinned_t):
        timing_len_delta = sum(
            len(a.group(0)) - len(b.group(0))
            for a, b in zip(TIMING_FIELD.finditer(live),
                            TIMING_FIELD.finditer(pinned))
        )
    raw_len_delta = len(live) - len(pinned)
    live_size = [int(m.group(0).split(":")[1])
                 for m in SELFSIZE_FIELD.finditer(live)]
    pinned_size = [int(m.group(0).split(":")[1])
                   for m in SELFSIZE_FIELD.finditer(pinned)]
    selfsize_delta = ([a - b for a, b in zip(live_size, pinned_size)]
                      if len(live_size) == len(pinned_size) else None)
    result = {
        "certificate": "E_LIVE_REDERIVATION",
        "reran": PRIMARY_869,
        "exit_code": proc.returncode,
        "elapsed_seconds": elapsed,
        "live_stdout_sha256": sha256(live.encode()).hexdigest(),
        "pinned_stdout_sha256": sha256(pinned.encode()).hexdigest(),
        "live_masked_sha256": sha256(mask_all(live).encode()).hexdigest(),
        "pinned_masked_sha256": sha256(mask_all(pinned).encode()).hexdigest(),
        "byte_identical_raw": live == pinned,
        "line_counts_equal": len(live_lines) == len(pinned_lines),
        "masked_identical": mask_all(live) == mask_all(pinned),
        "raw_differing_lines": differing,
        "differing_lines_explained_by_mask": explained,
        "unexplained_differing_lines": [i for i in differing
                                        if i not in explained],
        "timing_field_counts_equal": len(live_t) == len(pinned_t),
        "timing_length_delta": timing_len_delta,
        "raw_length_delta": raw_len_delta,
        "length_delta_fully_explained": timing_len_delta == raw_len_delta,
        "selfsize_delta": selfsize_delta,
        "selfsize_delta_matches_raw": (
            selfsize_delta is not None
            and all(d == raw_len_delta for d in selfsize_delta)),
        "mask_patterns": [TIMING_FIELD.pattern, SELFSIZE_FIELD.pattern],
        "policy": (
            "Cheap evidence is re-derived, not quoted.  The 869 primary is "
            "executed as a subprocess (never imported: it is blocklisted) and "
            "its stdout compared with the committed cache under two declared "
            "masks: wall-clock fields, and the runner's own stdout_bytes "
            "self-report.  Both masks are audited rather than trusted -- the "
            "whole raw length drift must be accounted for by the wall-clock "
            "strings, and stdout_bytes must have drifted by exactly that "
            "amount.  Any substantive change breaks masked equality."
        ),
    }
    result["pass"] = bool(
        proc.returncode == 0
        and result["line_counts_equal"]
        and result["masked_identical"]
        and not result["unexplained_differing_lines"]
        and result["timing_field_counts_equal"]
        and result["length_delta_fully_explained"]
        and result["selfsize_delta_matches_raw"]
    )
    return result


def f_discharge_map(family, witnesses):
    """The obligation table.  Statuses are assigned from the witness rows."""
    w = {c["witness"]: c for c in witnesses["checks"]}
    full = witnesses["across_key_full_corpus"]
    birth = witnesses["birth_datum_by_B_866"]
    hunt = witnesses["intrinsic_hunt_outcome_865"]
    f865 = family["candidate_family_865_predictors"]
    f866 = family["candidate_family_866_sync_cadences"]
    f869 = family["relation_family_869_clock_dictionary"]

    def ok(*names):
        return all(w[n]["agree"] for n in names)

    no_native_birth_datum = not any(
        row["native_pattern_functional"] for row in birth.values())

    obligations = [
        {
            "id": "O1_RECORD_NATIVITY_FILTER",
            "obligation": "conjunct (a): scheduler-valued and other gauge "
                          "structures are disqualified as rival record clocks",
            "status": ("DISCHARGED_AT_SCOPE"
                       if hunt["scheduler_gap_is_record_native"] is False
                       and no_native_birth_datum else "OPEN"),
            "scope": "B=2, B=3, B=4",
            "artifact": [ARC_CHECK_CACHE, CACHE_866],
            "evidence": "865 scheduler_gap_is_record_native=false; 866 "
                        "native_pattern_functional=false at B=3 and B=4",
        },
        {
            "id": "O2_NO_RECORD_NATIVE_RIVAL_PREDICTOR",
            "obligation": "no record-native predictor in the declared 865 "
                          "family reconstructs the per-world time origin, so "
                          "no such predictor defines a rival global clock",
            "status": ("DISCHARGED_AT_SCOPE"
                       if hunt["verdict"]
                       == "INTRINSIC_HUNT_EXHAUSTED_AT_DECLARED_FAMILY"
                       and hunt["selected_predictor"] is None else "OPEN"),
            "scope": f"B=2, family = {f865['singles_claimed']} singles + "
                     f"{f865['pairs_claimed']} pairs",
            "artifact": [ARC_CHECK_CACHE],
            "evidence": f865["verdict"],
        },
        {
            "id": "O3_NO_WITHIN_KEY_RIVAL_BANK_CLOCK",
            "obligation": "no single-bank clock is promoted to a rival global "
                          "time by the declared relation family",
            "status": ("DISCHARGED_AT_SCOPE"
                       if ok("869_bank_clocks_comparable_equals_split_total",
                             "869_bank_clocks_substantive_equals_nonthin",
                             "869_bank_clocks_verdicts_cover_the_corpus")
                       else "OPEN"),
            "scope": f869["scope"] + ", 831 substantive pairs of bank clocks",
            "artifact": [CACHE_869],
            "evidence": "0 substantive non-identity full dictionaries; the "
                        "single relation is F1 with c=0 (identical cadences)",
        },
        {
            "id": "O4_NO_WITHIN_KEY_RIVAL_PAIR_CLOCK",
            "obligation": "no pair clock is promoted to a rival global time; "
                          "the one tick-moving dictionary is a whole-orbit lag",
            "status": ("DISCHARGED_AT_SCOPE"
                       if ok("869_pair_clocks_nonidentity_full_dictionaries",
                             "869_nonidentity_lags_are_whole_orbits")
                       else "OPEN"),
            "scope": f869["scope"] + ", 480 substantive pairs of pair clocks",
            "artifact": [CACHE_869],
            "evidence": "1 of 480 substantive pairs carries a tick-moving full "
                        "dictionary; its witness is F3 with L=0, d=-1121 = "
                        "-59 whole 19-station orbits, i.e. commensurate",
        },
        {
            "id": "O5_PERIOD_COMMENSURABILITY",
            "obligation": "conjunct (c) at the rate level: no clock in the "
                          "corpus runs at a period incommensurate with the "
                          "station cycle, so none defines an independent rate",
            "status": ("DISCHARGED_AT_SCOPE"
                       if ok("869_every_nondegenerate_period_is_whole_orbits",
                             "869_period_orbit_counts")
                       else "OPEN"),
            "scope": f869["scope"],
            "artifact": [CACHE_869],
            "evidence": "corpus periods {19, 114, 1444} ticks = {1, 6, 76} "
                        "whole orbits of the 19-station cycle",
        },
        {
            "id": "O6_CROSS_KEY_ONE_TIME_UP_TO_ORIGIN",
            "obligation": "across keys, every clock the family relates is the "
                          "same clock re-zeroed, not a second time",
            "status": ("DISCHARGED_AT_SCOPE"
                       if ok("869_full_corpus_every_F1_edge_carries_nonzero"
                             "_offset")
                       else "OPEN"),
            "scope": f869["scope"] + ", the F1-covered across-key component",
            "artifact": [CACHE_869],
            "evidence": f"{full['F1_edges']}/{full['F1_edges']} across-key F1 "
                        f"edges carry a nonzero offset over the full corpus "
                        f"(bank and pair clocks); zero zero-offset edges",
        },
        {
            "id": "O7_CROSS_KEY_UNCOVERED_KEYS",
            "obligation": "the keys that fall outside every nontrivial F1 "
                          "class are not shown to share the one time",
            "status": "OPEN",
            "scope": f869["scope"],
            "artifact": [CACHE_869],
            "evidence": f"{full['keys_outside_any_nontrivial_F1_class']} keys "
                        f"outside any nontrivial F1 class over the full "
                        f"across-key corpus (the G-certificate headline "
                        f"reports 92, which is the pair-clock figure alone)",
        },
        {
            "id": "O8_UNRELATED_SUBSTANTIVE_PAIR_RESIDUE",
            "obligation": "substantive clock pairs that the family refuses to "
                          "relate are not shown to be one clock re-zeroed; "
                          "F's refusal is not identity",
            "status": "OPEN",
            "scope": f869["scope"],
            "artifact": [CACHE_869],
            "evidence": "429 of 480 substantive pair-clock comparisons and 830 "
                        "of 831 substantive bank-clock comparisons return "
                        "NO_RELATION_IN_F.  Under conjunct (c) these are "
                        "exactly the unresolved rival candidates: the negative "
                        "says F found no dictionary, not that none exists",
        },
        {
            "id": "O9_B4_RELATION_FAMILY_UNRUN",
            "obligation": "run the relation-family exhaustion at B=4 (and "
                          "beyond), where only a cadence-signature probe ran",
            "status": "OPEN",
            "scope": "B=4",
            "artifact": [CACHE_866, PRIMARY_869],
            "evidence": f"869 ran at {f869['scope']} only.  866 did run at "
                        f"B=4, but its C_SECOND_CLOCK_TEST compares TOP-3 "
                        f"DOMINANT-GAP signatures and found "
                        f"{f866['pair_count_B4']} distinct signatures over "
                        f"{f866['pair_count_B4']} bank pairs (and 3 over 3 at "
                        f"B=3), which measures signature distinctness, not "
                        f"clock identity.  No member of F was searched at B=4",
        },
        {
            "id": "O10_FAMILY_CLOSURE",
            "obligation": "extend every negative beyond its declared family "
                          "and caps",
            "status": "PERMANENTLY_OPEN",
            "scope": "all",
            "artifact": [PRIMARY_869, ARC_NOTE],
            "evidence": "865's exhaustion is priced to 29 singles + 28 pairs; "
                        "869's NO_RELATION_IN_F is priced to F = "
                        + ", ".join(f869["F_members"])
                        + f" at horizon {f869['horizon_chunks']}; 866's probe "
                          "is priced to top-3 gap granularity.  No finite "
                          "family can discharge this obligation, so it is "
                          "carried permanently and no count of discharged "
                          "rows retires it",
        },
        {
            "id": "O11_SUBSTRATE_TO_B_AXIS_TRANSFER",
            "obligation": "establish that the record-clock corpus measured "
                          "here IS the surface B-AXIS quantifies over",
            "status": "OPEN",
            "scope": "the bridge itself",
            "artifact": [PREMISE_DOC],
            "evidence": "B-AXIS speaks of 'no admitted independent commuting "
                        "transfer factor as a second clock' on the emergent "
                        "spacetime.  Every artifact assembled here measures "
                        "clocks on the Cycle-719 two-rail controller "
                        "substrate.  No pinned artifact identifies the two "
                        "surfaces, so even a fully closed LEG_II would not "
                        "reach the premise without this bridge",
        },
        {
            "id": "O12_LEG_I_CO_DEPENDENCE",
            "obligation": "leg (i) is a conjunct of the same 864-D condition "
                          "and is not re-derived by this cycle",
            "status": "OPEN",
            "scope": "leg (i)",
            "artifact": [CACHE_864, ARC_NOTE],
            "evidence": "864 certificates A/B supply the (i)-leg evidence with "
                        "verdict_A=MOMENT_LAW_TRANSFORMS and verdict_B=MIXED.  "
                        "This cycle quotes that standing and does not improve "
                        "it; leg (ii) alone never discharges the premise",
        },
    ]
    for row in obligations:
        row["artifact_sha256"] = {p: EXPECTED_SHA256[p] for p in row["artifact"]}
        row["artifact_provenance"] = {
            p: {"commit": PINNED_PROVENANCE[p][0],
                "original_path": PINNED_PROVENANCE[p][1],
                "git_blob": PINNED_PROVENANCE[p][2]}
            for p in row["artifact"] if p in PINNED_PROVENANCE
        }

    tally = {status: sum(1 for r in obligations if r["status"] == status)
             for status in STATUS_VALUES}
    open_rows = tuple(r["id"] for r in obligations if r["status"] != "DISCHARGED_AT_SCOPE")
    standing = ("B_AXIS_SECOND_LEG_DISCHARGED_AT_DECLARED_SCOPE"
                if not open_rows else
                "B_AXIS_NOT_DISCHARGED__SECOND_LEG_PARTIAL_AT_SCOPE")
    result = {
        "certificate": "F_DISCHARGE_MAP",
        "obligations": tuple(obligations),
        "tally": tally,
        "open_obligations": open_rows,
        "premise_standing": standing,
        "premise_standing_is_computed": (
            "standing is derived from the obligation table above; this file "
            "contains no comparison of the standing against a target value"
        ),
        "reading": (
            "The landed results close the record-nativity filter, the 865 "
            "predictor family, the within-key bank and pair clock families, "
            "period commensurability, and the across-key origin question on "
            "its covered component -- all at B=2/B=3 scope.  They leave open "
            "the uncovered across-key keys, the unrelated substantive pair "
            "residue, the entire B=4 relation-family run, family closure, the "
            "substrate-to-B-AXIS bridge, and leg (i)'s own standing.  B-AXIS "
            "remains a declared premise."
        ),
    }
    result["pass"] = bool(
        all(r["status"] in STATUS_VALUES for r in obligations)
        and all(r["artifact"] and r["evidence"] for r in obligations)
        and sum(tally.values()) == len(obligations)
        and standing.startswith("B_AXIS_")
    )
    return result


def g_controls(payloads, started):
    rows = []
    for path in AUDIT_INPUT_PATHS:
        raw = payloads[path]
        row = {
            "path": path,
            "exists": (ROOT / path).is_file(),
            "worktree_relative": not Path(path).is_absolute(),
            "sha256": sha256(raw).hexdigest(),
            "git_blob": git_blob(raw),
            "access": ("PINNED_EVIDENCE_BYTES_AST_ONLY" if path in PINNED_PROVENANCE
                       else "WORKTREE_TEXT_ONLY"),
        }
        expected = EXPECTED_SHA256.get(path, "")
        row["sha256_exact"] = (row["sha256"] == expected) if expected else None
        if path in PINNED_PROVENANCE:
            commit, original, blob = PINNED_PROVENANCE[path]
            row["pinned_commit"] = commit
            row["pinned_original_path"] = original
            row["git_blob_matches_pin"] = row["git_blob"] == blob
        rows.append(row)

    # Determinism: the whole evidence-derived payload rebuilt and re-digested.
    family = b_family_declaration(payloads)
    once = digest([a_quote_fidelity(payloads), family,
                   d_witness_rederivation(payloads)])
    twice = digest([a_quote_fidelity(payloads), b_family_declaration(payloads),
                    d_witness_rederivation(payloads)])
    runtime = round(time.monotonic() - started, 3)
    result = {
        "certificate": "G_CONTROLS",
        "inputs": tuple(rows),
        "declared_input_paths_are_literal": DECLARED_INPUT_PATHS == AUDIT_INPUT_PATHS,
        "blocklisted_modules": list(BLOCKLISTED_MODULES),
        "blocklist_violations": [name for name in BLOCKLISTED_MODULES
                                 if name in sys.modules],
        "determinism": {"digest": once, "repeat_digests_equal": once == twice},
        "runtime_seconds": runtime,
        "runtime_budget_seconds": AUDIT_TIMEOUT_SEC,
        "runtime_under_budget": runtime < AUDIT_TIMEOUT_SEC,
        "pinned_evidence_all_match": all(
            row.get("git_blob_matches_pin", True) for row in rows),
    }
    result["pass"] = bool(
        all(row["exists"] and row["worktree_relative"] for row in rows)
        and all(row["sha256_exact"] in (True, None) for row in rows)
        and result["pinned_evidence_all_match"]
        and result["declared_input_paths_are_literal"]
        and not result["blocklist_violations"]
        and result["determinism"]["repeat_digests_equal"]
        and result["runtime_under_budget"]
    )
    return result


def main() -> int:
    started = time.monotonic()
    payloads = {path: (ROOT / path).read_bytes() for path in AUDIT_INPUT_PATHS}

    quotes = a_quote_fidelity(payloads)
    family = b_family_declaration(payloads)
    formal = c_leg_ii_formalization()
    witnesses = d_witness_rederivation(payloads)
    live = e_live_rederivation(payloads)
    dmap = f_discharge_map(family, witnesses)
    controls = g_controls(payloads, started)

    certs = {
        "A_QUOTE_FIDELITY": quotes, "B_FAMILY_DECLARATION": family,
        "C_LEG_II_FORMALIZATION": formal, "D_WITNESS_REDERIVATION": witnesses,
        "E_LIVE_REDERIVATION": live, "F_DISCHARGE_MAP": dmap,
        "G_CONTROLS": controls,
    }
    checks = {name: bool(cert["pass"]) for name, cert in certs.items()}
    summary = {
        "cycle": 875,
        "claim_type": "SUPPORT",
        "checks": checks,
        "premise_standing": dmap["premise_standing"],
        "tally": dmap["tally"],
        "open_obligations": dmap["open_obligations"],
        "findings": witnesses["findings"],
        "runtime_seconds": controls["runtime_seconds"],
        "pass": all(checks.values()),
    }

    lines = ["CYCLE875_BAXIS_SECOND_LEG_CERTIFICATE",
             "CLAIM_TYPE SUPPORT_ASSEMBLY_NOT_A_THEOREM",
             "NO_PREMISE_IS_PROMOTED_BY_THIS_CYCLE"]
    for name in ("A_QUOTE_FIDELITY", "B_FAMILY_DECLARATION",
                 "C_LEG_II_FORMALIZATION", "D_WITNESS_REDERIVATION",
                 "E_LIVE_REDERIVATION", "F_DISCHARGE_MAP", "G_CONTROLS"):
        lines.append(f"CERTIFICATE {name} "
                     + ("PASS " if checks[name] else "FAIL ")
                     + compact(certs[name]))
    lines.append("SUMMARY_JSON " + compact(summary))
    lines.append("CYCLE875_BAXIS_SECOND_LEG_CERTIFICATE_"
                 + ("PASS" if summary["pass"] else "HONEST_FAIL"))
    out = "\n".join(lines) + "\n"
    if len(out.encode()) >= STDOUT_LIMIT_BYTES:
        raise AssertionError(("stdout limit", len(out.encode())))

    receipt = ROOT / ("outputs/cycle875_baxis_second_leg_certificate"
                      "_2026_07_28.json")
    receipt.write_text(json.dumps(
        {"summary": summary, "certificates": certs,
         "leg_ii_formalization": LEG_II_FORMAL,
         "leg_ii_price": LEG_II_PRICE},
        indent=1, sort_keys=True, default=list) + "\n")

    sys.stdout.write(out)
    return 0 if summary["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
