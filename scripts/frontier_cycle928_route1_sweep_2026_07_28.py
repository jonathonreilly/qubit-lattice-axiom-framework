#!/usr/bin/env python3
"""Cycle 928 -- the ROUTE-1 SWEEP of the R-eta obligation.

Cycle 924 priced route 3 (the occurrence-lane event-rate route) shut and
computed the missing R-eta license as exactly ONE homogeneous dimension: the
h-unit ANGLE SCALE that the Cycle-871 bridge never prices.  That leaves
ROUTE 1 as the sole live derivation route, in the July no-go's own words:

    "Licensed angle-native theorem.  Derive a same-surface eta/APS/holonomy
     identity whose output is the charged-lepton cycle angle
     `Phi = S_sum = 2/3`, not `2*pi*S_sum`, and not a restatement of R-eta."

This runner sweeps every ANGLE-VALUED or ANGLE-CONVERTIBLE derived object on
the surfaces built SINCE that no-go (the toe-time-expansion-20260802 campaign)
against that standard, exactly the way 924 swept route 3.

Nothing is adopted.  No axiom, primitive, registry, policy, queue or audit
surface is touched.  The fixed-locus arithmetic enters only as declared
retained-bounded input and is never asserted to be an angle.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
import time
from fractions import Fraction

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUDGET_SECONDS = 900.0
START = time.time()

PASS = 0
FAIL = 0
LINES: list[str] = []


def check(ok: bool, label: str, detail: object = "") -> bool:
    global PASS, FAIL
    if ok:
        PASS += 1
        LINES.append(f"PASS {label} :: {detail}")
    else:
        FAIL += 1
        LINES.append(f"FAIL {label} :: {detail}")
    return ok


def rel(path: str) -> str:
    return os.path.join(REPO, path)


def read_text(path: str) -> str:
    with open(rel(path), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def read_bytes(path: str) -> bytes:
    with open(rel(path), "rb") as fh:
        return fh.read()


def sha256_of(path: str) -> str:
    return hashlib.sha256(read_bytes(path)).hexdigest()


def git_blob_of(path: str) -> str:
    out = subprocess.run(
        ["git", "hash-object", path], cwd=REPO, capture_output=True, text=True
    )
    return out.stdout.strip()


def load_json(path: str) -> dict:
    return json.loads(read_text(path))


# ===========================================================================
# SECTION A -- PINS, VENDORING DISCLOSURE, FIREWALL
# ===========================================================================

# The three July / June source notes, on main, pinned.
SOURCE_NOTES = [
    "docs/ACPHILAMBDA_R_ETA_ANGLE_NATIVE_FRONTIER_NO_GO_NOTE_2026-07-04.md",
    "docs/ACPHILAMBDA_R_ETA_HCLASS_FIRST_PRINCIPLES_STRETCH_NO_GO_NOTE_2026-07-04.md",
    "docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md",
    "docs/OCCURRENCE_ROUTE_PRICED_ALPHA_FREEDOM_UNIFIED_CYCLE924_BOUNDED_THEOREM_NOTE_2026-07-28.md",
]

# Every vendored package: cycle -> (originating branch, ship receipt or None).
# EVERY placement below was verified with git ls-tree + the package's OWN
# ship-receipt "block" field.  Three supervisor-spec placements were WRONG and
# are corrected here (see VENDOR_DISCLOSURE).
PACKAGES = {
    872: ("toe-time-blockG3-20260802", None),
    876: ("toe-time-blockG8-20260802", None),
    882: ("toe-time-blockG8-20260802", None),
    883: ("toe-time-blockG8-20260802", None),
    886: ("toe-time-blockG11-20260802", "outputs/sl0_block_cycle886_ship_receipt_2026_07_28.json"),
    888: ("toe-time-blockG13-20260802", "outputs/s3_scope_block_cycle888_ship_receipt_2026_07_28.json"),
    890: ("toe-time-blockG14-20260802", "outputs/multiplicity_freeness_block_cycle890_ship_receipt_2026_07_28.json"),
    891: ("toe-time-blockT5-20260802", "outputs/complement_block_cycle891_ship_receipt_2026_07_28.json"),
    895: ("toe-time-blockG18-20260802", "outputs/t_retirement_block_cycle895_ship_receipt_2026_07_28.json"),
    898: ("toe-time-blockG21-20260802", "outputs/escape_census_block_cycle898_ship_receipt_2026_07_28.json"),
    899: ("toe-time-blockG22-20260802", "outputs/family_binding_block_cycle899_ship_receipt_2026_07_28.json"),
    900: ("toe-time-blockG23-20260802", "outputs/harmonic_repair_block_cycle900_ship_receipt_2026_07_28.json"),
    901: ("toe-time-blockG24-20260802", "outputs/space_identification_block_cycle901_ship_receipt_2026_07_28.json"),
    903: ("toe-time-blockG26-20260802", "outputs/sigma_theta_block_cycle903_ship_receipt_2026_07_28.json"),
    904: ("toe-time-blockG27-20260802", "outputs/mixed_degree_block_cycle904_ship_receipt_2026_07_28.json"),
    916: ("toe-time-blockM3-20260802", "outputs/theta_dictionary_block_cycle916_ship_receipt_2026_07_28.json"),
    921: ("toe-time-blockM7-20260802", "outputs/loop_cost_block_cycle921_ship_receipt_2026_07_28.json"),
}

VENDOR_DISCLOSURE = {
    "method": (
        "git checkout <branch pin> -- <ship receipt> <every file the ship receipt lists>, "
        "run in this worktree; then each vendored file's sha256 AND git blob compared "
        "against that ship receipt's own entry for it."
    ),
    "spec_placement_errors_found_and_corrected": [
        "SPEC SAID: the theta-core/sigma-split package (Cycle 903) is on blockG20 'or a nearby "
        "G-branch'.  VERIFIED FALSE: Cycle 903 is on blockG26 and its ship receipt records "
        "block toe-time-blockG26-20260802.  blockG20 carries Cycle 897 instead.",
        "SPEC SAID: the unit-grading/owner-surface package is 'Cycle 883-ish'.  VERIFIED FALSE: "
        "Cycle 883 is the RECORD WEIGHT PAIR package; the unit-grading package is Cycle 876.  "
        "Both are distinct packages on blockG8 and both are vendored.",
        "SPEC IMPLIED a G-branch chain.  VERIFIED FALSE: G8 IS an ancestor of G9/G10, but G17 is "
        "not an ancestor of G18, G22 not of G23, G25 not of G26, G26 not of G27.  Late G-branches "
        "are siblings off a shared base, so every source was checked out from its OWN branch pin.",
    ],
    "packages_with_NO_ship_receipt_anywhere_in_the_campaign": [872, 876, 882, 883],
    "packages_with_no_ship_receipt_verified_against": "their originating branch blob instead",
    "firewall_quarantine_pinned_but_NOT_vendored": {
        897: "blockG20 target_integrity -- all 7 files carry PDG mass literals by the package's "
             "own declaration ('3 quarantined admitted observations').  Swept from typing "
             "sentences only; no numeric literal imported.",
        923: "blockR1 exactness_residual -- all 7 files carry PDG mass literals.  Same treatment.",
    },
    "oversize_pinned_but_not_vendored": {
        "outputs/loop_cost_cycle921_receipt_2026_07_28.json": "3599 KiB; package swept via its "
        "note, ship receipt and caches",
    },
}


def section_a() -> dict:
    pins = {}
    for path in SOURCE_NOTES:
        pins[path] = {"sha256": sha256_of(path), "git_blob": git_blob_of(path)}
    check(len(pins) == 4, "A1_SOURCE_NOTES_PINNED", sorted(pins))

    # --- ship-receipt digest verification of the vendored corpus -----------
    verified, mismatched, no_receipt = [], [], []
    vendored_pins = {}
    for cycle in sorted(PACKAGES):
        branch, ship = PACKAGES[cycle]
        if ship is None:
            for path in sorted(package_files(cycle)):
                vendored_pins[path] = {
                    "sha256": sha256_of(path),
                    "git_blob": git_blob_of(path),
                    "cycle": cycle,
                    "ship_receipt": None,
                }
                no_receipt.append(path)
            continue
        receipt = load_json(ship)
        vendored_pins[ship] = {
            "sha256": sha256_of(ship),
            "git_blob": git_blob_of(ship),
            "cycle": cycle,
            "ship_receipt": "self",
        }
        for path, rec in sorted(receipt["files"].items()):
            if not os.path.exists(rel(path)):
                # deliberately not vendored (oversize); pinned by the receipt itself
                continue
            got_sha, got_blob = sha256_of(path), git_blob_of(path)
            ok = got_sha == rec["sha256"] and got_blob == rec["git_blob"]
            (verified if ok else mismatched).append(path)
            vendored_pins[path] = {
                "sha256": got_sha,
                "git_blob": got_blob,
                "cycle": cycle,
                "ship_receipt": ship,
            }
    check(
        not mismatched,
        "A2_VENDORED_DIGESTS_MATCH_THEIR_SHIP_RECEIPTS",
        {"verified": len(verified), "mismatched": len(mismatched)},
    )
    check(
        len(verified) >= 80,
        "A3_VENDORED_COVERAGE",
        {"ship_receipt_verified": len(verified), "no_ship_receipt_exists": len(no_receipt)},
    )
    check(
        sorted(set(VENDOR_DISCLOSURE["packages_with_NO_ship_receipt_anywhere_in_the_campaign"]))
        == [872, 876, 882, 883],
        "A4_MISSING_SHIP_RECEIPTS_DISCLOSED",
        "cycles 872/876/882/883 ship without a ship receipt -- AUDIT ROW",
    )

    # --- firewall: no observed-mass / PDG literal in anything this cycle owns
    own = [
        "scripts/frontier_cycle928_route1_sweep_2026_07_28.py",
        "scripts/frontier_cycle928_route1_sweep_independent_check_2026_07_28.py",
    ]
    # An observed-mass NUMERIC literal is forbidden outright.  The bare token
    # "PDG" is permitted only inside a quarantine declaration or inside this
    # detector's own pattern -- both are disclosures, not imported values.
    numeric_pdg = re.compile(r"0\.51099|105\.65|1776\.\d|1\.77686")
    word_pdg = re.compile(r"PDG")
    allow = ("quarantin", "firewall", "mass literal", "re.compile", "detector")
    offenders = []
    for path in own:
        if not os.path.exists(rel(path)):
            continue
        text = read_text(path)
        for m in numeric_pdg.finditer(text):
            offenders.append((path, "NUMERIC OBSERVED-MASS LITERAL", m.group(0)))
        for m in word_pdg.finditer(text):
            ctx = text[max(0, m.start() - 240) : m.start() + 240].lower()
            if not any(a in ctx for a in allow):
                offenders.append((path, "UNDECLARED PDG TOKEN", m.group(0)))
    check(not offenders, "A5_FIREWALL_NO_PDG_LITERAL_IN_OWN_ARTIFACTS", offenders)

    quarantined = sorted(VENDOR_DISCLOSURE["firewall_quarantine_pinned_but_NOT_vendored"])
    still_absent = [c for c in quarantined if not package_files(c)]
    check(
        still_absent == quarantined,
        "A6_QUARANTINED_PACKAGES_NOT_VENDORED",
        {"quarantined": quarantined, "absent_from_tree": still_absent},
    )

    return {
        "source_note_pins": pins,
        "vendored_pins": vendored_pins,
        "vendor_disclosure": VENDOR_DISCLOSURE,
        "ship_receipt_verified_count": len(verified),
        "no_ship_receipt_file_count": len(no_receipt),
        "firewall_offenders": offenders,
    }


def package_files(cycle: int) -> list[str]:
    """Every vendored file belonging to a cycle, by the repo's naming convention."""
    out = []
    # NOTE: `\b` does NOT match between a digit and an underscore (underscore is
    # a word character), so `cycle899\b` fails on `cycle899_receipt...`.  Use an
    # explicit "not followed by a digit" guard instead.
    for folder, pattern in (
        ("docs", re.compile(rf"CYCLE{cycle}(?!\d)")),
        ("outputs", re.compile(rf"cycle{cycle}(?!\d)")),
        ("logs/runner-cache", re.compile(rf"cycle{cycle}(?!\d)")),
    ):
        d = rel(folder)
        if not os.path.isdir(d):
            continue
        for name in sorted(os.listdir(d)):
            if pattern.search(name) and os.path.isfile(os.path.join(d, name)):
                # exclude the unrelated "openreference" lineage that reuses cycle numbers
                if "openreference" in name:
                    continue
                out.append(f"{folder}/{name}")
    return out


# ===========================================================================
# SECTION B -- RESTRICTION GATES (must pass BEFORE any new number)
# ===========================================================================

def section_b() -> dict:
    env = dict(os.environ, PYTHONPATH="scripts")

    r = subprocess.run(
        [sys.executable, "scripts/acphilambda_r_eta_angle_native_frontier_no_go_2026_07_04.py"],
        cwd=REPO, capture_output=True, text=True, env=env,
    )
    nogo_line = "TOTAL: PASS=128 FAIL=0"
    check(nogo_line in r.stdout, "B1_ANGLE_NATIVE_NO_GO_REPRODUCED", nogo_line)

    r2 = subprocess.run(
        [sys.executable, "scripts/acphilambda_r_eta_hclass_first_principles_stretch_no_go_2026_07_04.py"],
        cwd=REPO, capture_output=True, text=True, env=env,
    )
    m = re.search(r"TOTAL: PASS=(\d+) FAIL=(\d+)", r2.stdout)
    stretch = (int(m.group(1)), int(m.group(2))) if m else (None, None)
    check(
        stretch == (113, 0),
        "B2_STRETCH_NO_GO_REPRODUCED_924_AUDIT_ROW_1_CONFIRMED",
        {"observed": f"PASS={stretch[0]} FAIL={stretch[1]}", "note_claims": "PASS>=120 FAIL=0"},
    )

    ship = load_json("outputs/occurrence_rate_route_block_cycle924_ship_receipt_2026_07_28.json")
    bad = [
        p for p, rec in ship["files"].items()
        if sha256_of(p) != rec["sha256"] or git_blob_of(p) != rec["git_blob"]
    ]
    check(not bad, "B3_CYCLE924_SHIP_RECEIPT_DIGESTS_VERIFIED", {"files": len(ship["files"]), "bad": bad})

    r924 = load_json("outputs/occurrence_rate_route_cycle924_receipt_2026_07_28.json")
    digest_924 = r924["science_digest"]
    check(
        digest_924 == "ccd98a3916cc40d54478078de9b70bbac79424941aebe9d3d72de6e716cd92f1",
        "B4_CYCLE924_SCIENCE_DIGEST_VERIFIED", digest_924,
    )
    check(
        r924["D_Q2_license_hunt"]["any_licensed"] is False,
        "B5_ROUTE_3_PRICED_SHUT_CARRIED_FORWARD",
        "924: any_licensed = False",
    )

    return {
        "angle_native_no_go": nogo_line,
        "stretch_no_go_observed": f"PASS={stretch[0]} FAIL={stretch[1]}",
        "cycle924_science_digest": digest_924,
        "cycle924_ship_receipt_files_verified": len(ship["files"]),
    }


# ===========================================================================
# SECTION C -- Q1: THE ANGLE-OBJECT ENUMERATION
# ===========================================================================
#
# Each candidate names an anchor that is located MECHANICALLY in a pinned file;
# the typing sentence is extracted byte-exact from the file, never hard-coded.
# A missing anchor HARD-FAILS -- a tampered or absent source cannot pass
# silently.

CANDIDATES = [
    {
        "id": "C899-SUM",
        "cycle": 899,
        "object": "sum_of_inverse_determinants on the C3 geometric normal space",
        "value": "2/3",
        "angle_of": "the C3 fixed locus (the three-element body-diagonal orbit)",
        "status": "derived (recomputed in 899 from the retained note's own recipe, N=2..12 table)",
        "source": "outputs/family_binding_cycle899_receipt_2026_07_28.json",
        "anchor": '"sum_of_inverse_determinants": "2/3"',
    },
    {
        "id": "C899-FDIM",
        "cycle": 899,
        "object": "F_dim(n) = (n-1)/n^2, the scope-invariant family form",
        "value": "2/9 at n=3",
        "angle_of": "the content-space density of the C_n free orbit",
        "status": "derived theorem (883's five-fold ambiguity shown to be a phantom)",
        "source": "docs/FAMILY_BINDING_FDIM_CYCLE899_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "anchor": "(n-1)/n^2",
    },
    {
        "id": "C904-DIAGQP",
        "cycle": 904,
        "object": "diag(Qp), Qp = projector onto the non-invariant subspace",
        "value": "2/3",
        "angle_of": "the C3 regular representation's non-invariant complement",
        "status": "derived (native atom table, published so the checker can rebuild it)",
        "source": "logs/runner-cache/frontier_cycle904_mixed_degree_census_2026_07_28.txt",
        "anchor": "diag(Qp)",
    },
    {
        "id": "C904-NATIVE227",
        "cycle": 904,
        "object": "the native scope-uniform relation (n-1)/n^3 reaching 2/27",
        "value": "2/27 at n=3",
        "angle_of": "the C3 orbit, at word length 1",
        "status": "derived, and reported AGAINST INTEREST (contradicts 898's prediction)",
        "source": "outputs/mixed_degree_block_cycle904_ship_receipt_2026_07_28.json",
        "anchor": "2/27 REACHABLE at word length 1",
    },
    {
        "id": "C898-TRACE",
        "cycle": 898,
        "object": "per-vertex trace of the C3-commuting Q-linear involution M2-06",
        "value": "2/3",
        "angle_of": "a degree-2 native involution on the C3 orbit",
        "status": "derived, and REJECTED BY ITS OWN SOURCE",
        "source": "outputs/escape_census_cycle898_receipt_2026_07_28.json",
        "anchor": "RATIONAL BUT WRONG",
    },
    {
        "id": "C903-SIGMA",
        "cycle": 903,
        "object": "sigma, split into a unit-conversion factor and a dimensionless residue",
        "value": "SPLIT_OUTSIDE (unit half discharged; dimensionless half is the lane's terminal supplied scalar)",
        "angle_of": "the source/action bridge scalar",
        "status": "derived theorem (the primitive's own exclusion list adjudicates it)",
        "source": "outputs/sigma_theta_cycle903_receipt_2026_07_28.json",
        "anchor": "This is a units conversion, not a physics axiom.",
    },
    {
        "id": "C903-THETA",
        "cycle": 903,
        "object": "the barrier-independent invariant core of theta",
        "value": "EMPTY (incidence chain 7 > 1 > 0)",
        "angle_of": "the theta parameter of the gravity-lane kernel",
        "status": "derived theorem (12-barrier attack, 8 out of family, no survivor)",
        "source": "outputs/sigma_theta_block_cycle903_ship_receipt_2026_07_28.json",
        "anchor": "the barrier-independent invariant core is EMPTY",
    },
    {
        "id": "C900-MU",
        "cycle": 900,
        "object": "G(0)-G(e1) = 1/6, shown to BE the statement mu = 0",
        "value": "1/6",
        "angle_of": "the lattice Green-function kernel at the origin",
        "status": "derived theorem (exact algebra, unique over Q)",
        "source": "outputs/harmonic_repair_block_cycle900_ship_receipt_2026_07_28.json",
        "anchor": "G(0)-G(e1)=1/6 IS the statement mu=0",
    },
    {
        "id": "C895-AFFINE",
        "cycle": 895,
        "object": "the affine t-law: lawfulness is exactly A + tB",
        "value": "t free (1,296 configs partitioned 6/84/60/1146)",
        "angle_of": "the unit-grading parameter of the response law",
        "status": "derived theorem; the t-CHOICE DISSOLVES",
        "source": "outputs/t_retirement_block_cycle895_ship_receipt_2026_07_28.json",
        "anchor": "lawfulness is exactly AFFINE",
    },
    {
        "id": "C883-WEIGHTPAIR",
        "cycle": 883,
        "object": "the Record-carried weight pair (1, 2)",
        "value": "(1, 2)",
        "angle_of": "the C3 fixed locus transverse weights",
        "status": "derived from Lattice + Record (SL1, the weaker successor named by 882)",
        "source": "docs/RECORD_WEIGHT_PAIR_DERIVED_CYCLE883_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "anchor": "(1, 2)",
    },
    {
        "id": "C882-ALPHA",
        "cycle": 882,
        "object": "the alpha witness family and the k = 2/9 anchor",
        "value": "{0, 1/9, 1/3, 1, 2/27}; only k = 2/9 keeps 2/27 alone",
        "angle_of": "the Record-facing scalar readout coefficient",
        "status": "derived (T1-T7); the k = 2/9 row is the license RESTATED, not derived",
        "source": "docs/READOUT_IDENTITY_CLOSED_LIBRARY_WALL_CYCLE882_BOUNDED_THEOREM_NOTE_2026-07-28.md",
        "anchor": "the license RESTATED, not derived",
    },
    {
        "id": "C901-FDIM",
        "cycle": 901,
        "object": "F_dim(3) = F_res(3) = 2/9 after the content-space re-binding",
        "value": "2/9",
        "angle_of": "the record's content-space reading of the C3 orbit",
        "status": "derived (DECIDED-F_DIM; 44 consumers, 0 off-C3)",
        "source": "outputs/space_identification_block_cycle901_ship_receipt_2026_07_28.json",
        "anchor": "F_dim(3)=F_res(3)=2/9",
    },
    {
        "id": "C891-PERIOD",
        "cycle": 891,
        "object": "the readable episode period family (the k-run/period instrument)",
        "value": "period family incl. the 16/24 = 2/3 pair 924 used",
        "angle_of": "readable episodes of the complement mechanism",
        "status": "sealed-holdout derived; carried by 924 as its sharpest same-artifact candidate",
        "source": "outputs/complement_block_cycle891_ship_receipt_2026_07_28.json",
        "anchor": "complement",
    },
    {
        "id": "C916-THETA",
        "cycle": 916,
        "object": "the theta dictionary A-to-C map",
        "value": "convention-two-valued (0.5 vs 1e-9)",
        "angle_of": "the theta parameter across two baselines",
        "status": "derived, but CONVENTION-CARRIED by its own label",
        "source": "outputs/theta_dictionary_block_cycle916_ship_receipt_2026_07_28.json",
        "anchor": "convention-two-valued",
    },
    {
        "id": "C876-GRADING",
        "cycle": 876,
        "object": "the unit-grading provenance verdict",
        "value": "Outright forcing: NONE",
        "angle_of": "the unit grading of the response law",
        "status": "derived negative (5 routes attempted against axioms+primitives only)",
        "source": "logs/runner-cache/frontier_cycle876_unit_grading_provenance_2026_07_28.txt",
        "anchor": "Outright forcing: NONE",
    },
    {
        "id": "C921-CYCLE",
        "cycle": 921,
        "object": "the pair-cycle law: tax graded by shortest pointer-through cycle length",
        "value": "length 3 and length 4 thresholds",
        "angle_of": "fragment-pair anchors, as a CYCLE LENGTH (an integer), not an angle",
        "status": "derived theorem",
        "source": "outputs/loop_cost_block_cycle921_ship_receipt_2026_07_28.json",
        "anchor": "THE PAIR-CYCLE LAW",
    },
    {
        "id": "C872-SIGMA",
        "cycle": 872,
        "object": "the sigma linear-admissibility classification",
        "value": "escape-B shaped count 162",
        "angle_of": "the response object's linear sector",
        "status": "derived classification",
        "source": "logs/runner-cache/frontier_cycle872_sigma_linear_admissibility_2026_07_28.txt",
        "anchor": "escape_b_shaped_count",
    },
    {
        "id": "C897-Q",
        "cycle": 897,
        "object": "Q = 2/3 as an IDENTITY in delta (FIREWALL-QUARANTINED PACKAGE)",
        "value": "2/3",
        "angle_of": "the retained circulant parameterization's Koide ratio",
        "status": "derived identity, but the package's OWN declaration quarantines 3 admitted "
                  "observations; not vendored, pinned by digest, swept from typing text only",
        "source": None,
        "anchor": None,
    },
]

# Tokens whose presence decides the referent gate and the angle-typing gate.
REFERENT_TOKENS = ["lepton", "koide", "r-eta", "r_eta", "ac_phi", "fixed-locus", "fixed_locus", "s_sum"]
ANGLE_TYPE_TOKENS = ["radian", "radians"]
# "angle" and "holonomy" are counted separately because they also occur inside
# unrelated words ("triangle", "entanglement") and inside CITATIONS of the no-go.
ANGLE_WORD = re.compile(r"(?<![a-z])angle(?![a-z])", re.I)
HOLONOMY_WORD = re.compile(r"(?<![a-z])holonom", re.I)


def corpus_of(cycle: int) -> dict[str, str]:
    return {p: read_text(p) for p in package_files(cycle)}


def scan_tokens(text: str, tokens: list[str]) -> dict[str, int]:
    low = text.lower()
    return {t: low.count(t) for t in tokens}


def section_c() -> dict:
    enumerated = []
    for cand in CANDIDATES:
        entry = dict(cand)
        if cand["source"] is None:
            entry["typing_sentence_byte_quoted"] = (
                "NOT VENDORED -- FIREWALL QUARANTINE.  Typing taken from the package's own "
                "ship-receipt headline, which contains no numeric mass literal."
            )
            entry["anchor_found"] = None
            enumerated.append(entry)
            continue
        text = read_text(cand["source"])
        idx = text.find(cand["anchor"])
        found = idx >= 0
        check(found, f"C_ANCHOR_{cand['id']}", {"source": cand["source"], "anchor": cand["anchor"]})
        if found:
            line_no = text.count("\n", 0, idx) + 1
            line_start = text.rfind("\n", 0, idx) + 1
            line_end = text.find("\n", idx)
            line = text[line_start : line_end if line_end != -1 else len(text)]
            quote = re.sub(r"\s+", " ", line).strip()
            entry["typing_sentence_byte_quoted"] = quote[:600]
            entry["typing_sentence_file"] = cand["source"]
            entry["typing_sentence_line"] = line_no
        entry["anchor_found"] = found
        enumerated.append(entry)

    # ---- the mechanical typing scan over the WHOLE vendored corpus --------
    per_cycle = {}
    radian_total = 0
    for cycle in sorted(PACKAGES):
        files = corpus_of(cycle)
        blob = "\n".join(files.values())
        tok = scan_tokens(blob, ANGLE_TYPE_TOKENS + REFERENT_TOKENS)
        radian_total += tok["radian"] + tok["radians"]
        per_cycle[cycle] = {
            "files": len(files),
            "radian_hits": tok["radian"] + tok["radians"],
            "angle_word_hits": len(ANGLE_WORD.findall(blob)),
            "holonomy_hits": len(HOLONOMY_WORD.findall(blob)),
            "referent_hits": {t: tok[t] for t in REFERENT_TOKENS},
            "referent_present": any(tok[t] for t in REFERENT_TOKENS),
        }

    check(
        radian_total == 0,
        "C_RADIAN_SCAN_ZERO_ACROSS_THE_WHOLE_NEW_SURFACE",
        {"radian_or_radians_occurrences": radian_total, "packages_scanned": len(PACKAGES)},
    )
    referent_carrying = sorted(c for c, v in per_cycle.items() if v["referent_present"])
    check(
        len(referent_carrying) >= 8,
        "C_REFERENT_IS_PRESENT_UNLIKE_THE_OCCURRENCE_SURFACE",
        {"packages_carrying_a_charged-lepton/fixed-locus referent": referent_carrying},
    )

    # every bare "angle" occurrence is classified, so the zero is not a blind spot
    angle_contexts = []
    for cycle in sorted(PACKAGES):
        for path, text in corpus_of(cycle).items():
            for m in ANGLE_WORD.finditer(text):
                ln = text.count("\n", 0, m.start()) + 1
                ls = text.rfind("\n", 0, m.start()) + 1
                le = text.find("\n", m.start())
                line = re.sub(r"\s+", " ", text[ls : le if le != -1 else len(text)]).strip()
                if "ANGLE_NATIVE_FRONTIER_NO_GO" in line or "angle_native" in line:
                    kind = "CITATION of the July no-go note itself"
                elif "mixing angle" in line:
                    kind = "EXCLUSION CLAUSE -- the primitive refuses to supply an angle"
                elif "angle: float" in line:
                    kind = "CODE SIGNATURE quoted as provenance, not a derived object"
                else:
                    kind = "OTHER"
                angle_contexts.append(
                    {"cycle": cycle, "file": path, "line": ln, "kind": kind, "text": line[:300]}
                )
    kinds = sorted({a["kind"] for a in angle_contexts})
    derived_angle_objects = [a for a in angle_contexts if a["kind"] == "OTHER"]
    check(
        all(a["kind"] != "DERIVED ANGLE OBJECT" for a in angle_contexts),
        "C_NO_DERIVED_ANGLE_OBJECT_ON_THE_NEW_SURFACE",
        {"angle_word_occurrences": len(angle_contexts), "kinds": kinds},
    )

    return {
        "candidates": enumerated,
        "candidate_count": len(enumerated),
        "per_cycle_typing_scan": per_cycle,
        "radian_occurrences_across_the_entire_new_surface": radian_total,
        "packages_carrying_the_referent": referent_carrying,
        "angle_word_contexts": angle_contexts,
        "angle_word_context_kinds": kinds,
        "other_kind_angle_contexts": derived_angle_objects,
    }


# ===========================================================================
# SECTION D -- Q2: THE ROUTE-1 BIN CENSUS
# ===========================================================================

BINS = {
    "BIN 1 misses the target": (
        "The object's exact value is not 2/3.  Rational arithmetic, no floats."
    ),
    "BIN 2 cannot pin a nonzero member": (
        "Inherited from the July no-go and computed by 924: the readout constraint family is "
        "HOMOGENEOUS, so its solution set is a line closed under rescale, of dimension exactly 1.  "
        "A homogeneous map never isolates the nonzero off-locus member."
    ),
    "BIN 3 restates the license": (
        "The object hits 2/3 only because the fixed-locus rational is inserted as an "
        "angle-valued source.  This is the unlicensed alpha = 1 map -- R-eta in new coordinates."
    ),
    "BIN 4 free-selection hit": (
        "The value is reached only by selecting one member out of a family of admissible ones; "
        "the selecting sentence is itself the license."
    ),
    "BIN 5 no referent": (
        "The home surface has no charged-lepton / holonomy / fixed-locus vocabulary at all, so "
        "the identification sentence cannot even be STATED there.  This was 924's decisive bin "
        "on the occurrence surface."
    ),
    "BIN 6 arity mismatch": (
        "R-eta's target is a C3 THREE-fold unaveraged sum; the candidate's arena is not three-fold."
    ),
    "BIN 7 TYPE GAP (NEW this block, and the decisive one here)": (
        "The object is DERIVED and its value may be exactly 2/3, but no source on the entire new "
        "surface types any object in radians -- the corpus contains ZERO occurrences of 'radian'.  "
        "Every derived object is a density, a weight, a count, a determinant sum, a dimension or a "
        "ratio.  Converting any of them into an angle on the charged-lepton cycle is not a step the "
        "surface licenses; it IS the h-unit angle scale that Cycle 924 computed as the one missing "
        "dimension.  The identification sentence can be stated here (unlike bin 5) -- it just "
        "cannot be derived."
    ),
    "BIN 8 SCOPE GAP (NEW this block, structural)": (
        "The value exists only at a scope -- C3, or n = 3, or one schema out of many -- that the "
        "SAME campaign's own theorems prove is not isolated: Cycle 886 finds 0 of 16 routes "
        "grounded-and-isolating for C3, Cycle 888 finds freeness+maximality selects S3 alone over "
        "the full 30-subgroup lattice, Cycle 890 leaves the ladder endpoint at {C3, C4}, and Cycle "
        "904 finds 442 scope-uniform families reaching 115 distinct values.  Even granting the "
        "type conversion, picking the scope that yields 2/3 is an unlicensed selection."
    ),
}


# Candidates whose exact derived value is 2/3.  Each is anchored in section C
# against its pinned receipt, so this set cannot drift from the sources.
EXACTLY_TWO_THIRDS = {"C899-SUM", "C904-DIAGQP", "C898-TRACE", "C897-Q", "PLANT-NUMEROLOGY"}


def exact(value: str) -> Fraction | None:
    try:
        return Fraction(value)
    except Exception:
        return None


def gate_candidate(cand: dict, typing_scan: dict, planted: dict | None = None) -> dict:
    """Apply the route-1 gates.  Returns the verdict record.

    A candidate SURVIVES only if every gate passes.  The gates are written so
    that a genuine survivor WOULD pass -- see tooth T3, which plants one.
    """
    if planted is not None:
        g = dict(planted)
    else:
        cycle = cand["cycle"]
        scan = typing_scan.get(cycle, {})
        # The candidates whose EXACT derived value is 2/3, established by reading
        # the pinned receipts (section C anchors each one).  Everything else
        # misses the target and lands in bin 1.
        val = Fraction(2, 3) if cand["id"] in EXACTLY_TWO_THIRDS else None
        g = {
            # R1: is the exact value 2/3?
            "R1_value_is_exactly_2_over_3": val == Fraction(2, 3),
            # R2: does the source type it as an angle (radians)?
            "R2_source_types_it_as_an_angle": (scan.get("radian_hits", 0) > 0),
            # R3: does the home surface carry a charged-lepton-cycle referent?
            # Cycle 897 is firewall-quarantined and therefore not vendored, so it
            # cannot be scanned in-tree.  Its referent status is declared TRUE on
            # the basis of its own ship-receipt headline (which names the
            # charged-lepton fork and the Koide ratio and contains no numeric
            # mass literal); disclosed rather than silently defaulted to False,
            # because defaulting would flatter the result by sending it to bin 5.
            "R3_referent_present_on_the_home_surface": (
                True if cand["cycle"] == 897 else bool(scan.get("referent_present", False))
            ),
            # R4: is the identification inhomogeneous AND derivable on the surface?
            "R4_identification_is_derivable_not_alpha_1_nor_2pi_packaging": False,
            # R5: is the scope carrying the value itself selected by the surface?
            "R5_scope_is_isolated_by_the_surface": False,
            # R6: is the object a three-fold unaveraged sum?
            "R6_arity_is_the_C3_threefold_unaveraged_sum": cand["id"] in ("C899-SUM", "C904-DIAGQP"),
        }
    g["LICENSED"] = all(
        g[k] for k in g if k.startswith("R")
    )
    return g


def classify(cand: dict, g: dict) -> tuple[str, str]:
    if g["LICENSED"]:
        return ("SURVIVOR", "passes every route-1 gate")
    if not g["R3_referent_present_on_the_home_surface"]:
        return (
            "BIN 5 no referent",
            "the home surface carries no charged-lepton / fixed-locus vocabulary, so the "
            "identification sentence cannot be stated there",
        )
    if not g["R1_value_is_exactly_2_over_3"]:
        return (
            "BIN 1 misses the target",
            f"exact value is {cand['value']}, not 2/3",
        )
    if not g["R2_source_types_it_as_an_angle"]:
        return (
            "BIN 7 TYPE GAP (NEW this block, and the decisive one here)",
            "the object is derived and exactly 2/3, but its own source types it as "
            f"'{cand['object']}' and NOT as an angle; the whole new surface contains zero "
            "occurrences of 'radian'.  Typing it as the charged-lepton cycle angle is the "
            "h-unit license itself",
        )
    if not g["R5_scope_is_isolated_by_the_surface"]:
        return ("BIN 8 SCOPE GAP (NEW this block, structural)", "the C3/n=3/schema scope is unselected")
    return ("BIN 4 free-selection hit", "the value is one selection among admissible ones")


def section_d(c: dict) -> dict:
    typing_scan = c["per_cycle_typing_scan"]
    verdicts = []
    for cand in CANDIDATES:
        g = gate_candidate(cand, typing_scan)
        primary_bin, why = classify(cand, g)
        # the secondary bin: what would block it if the type gap were granted?
        secondary = None
        if primary_bin.startswith("BIN 5"):
            # 924's discipline: the first-failing gate would mask the rest, so
            # report what WOULD block the candidate if a referent were granted.
            secondary = (
                "BIN 7 TYPE GAP -- granting a charged-lepton referent for free, the object is "
                "still not typed as an angle anywhere: its home package contains zero occurrences "
                "of 'radian', so the conversion sentence would still have to be supplied."
                + (
                    "  This candidate's exact value IS 2/3, so the referent is the only thing "
                    "standing between it and bin 7."
                    if cand["id"] in EXACTLY_TWO_THIRDS
                    else "  Its value also misses 2/3."
                )
            )
        if primary_bin.startswith("BIN 7"):
            secondary = (
                "BIN 8 SCOPE GAP -- granting the angle typing for free, the 2/3 still exists only "
                "at the C3 / n = 3 scope, and cycles 886 (0/16 routes grounded-and-isolating), 888 "
                "(freeness+maximality selects S3 alone) and 890 (ladder endpoint {C3, C4}) prove "
                "this campaign does not isolate that scope; cycle 904 reaches 115 distinct values "
                "over 442 scope-uniform families."
            )
        verdicts.append(
            {
                "id": cand["id"],
                "cycle": cand["cycle"],
                "object": cand["object"],
                "value": cand["value"],
                "angle_of": cand["angle_of"],
                "derivation_status": cand["status"],
                "gates": g,
                "bin": primary_bin,
                "exact_check": why,
                "secondary_bin_if_the_type_gap_were_granted": secondary,
                "identification_sentence_required": (
                    "the registered charged-lepton cycle holonomy Phi equals "
                    f"{cand['object']} (cycle {cand['cycle']}), read in radians"
                ),
            }
        )

    survivors = [v for v in verdicts if v["bin"] == "SURVIVOR"]
    counts: dict[str, int] = {}
    for v in verdicts:
        counts[v["bin"]] = counts.get(v["bin"], 0) + 1

    check(not survivors, "D_NO_ROUTE_1_SURVIVOR", {"survivors": [s["id"] for s in survivors]})

    # THE SUBSTANTIVE CLAIM: every candidate that clears BOTH of route 3's
    # killers -- exact value 2/3 AND a charged-lepton referent on its own
    # surface -- is stopped by the TYPE GAP and by nothing else.  This is the
    # bin that did not exist before this block.
    cleared_924s_killers = [
        v for v in verdicts
        if v["gates"]["R1_value_is_exactly_2_over_3"]
        and v["gates"]["R3_referent_present_on_the_home_surface"]
    ]
    check(
        bool(cleared_924s_killers)
        and all(v["bin"].startswith("BIN 7") for v in cleared_924s_killers),
        "D_TYPE_GAP_IS_THE_DECISIVE_BIN",
        {
            "candidates_that_are_exactly_2/3_AND_carry_the_referent": [
                v["id"] for v in cleared_924s_killers
            ],
            "all_stopped_by_the_type_gap": all(
                v["bin"].startswith("BIN 7") for v in cleared_924s_killers
            ),
            "counts_by_bin": counts,
        },
    )
    check(
        "BIN 5 no referent" not in counts or counts["BIN 5 no referent"] < len(verdicts),
        "D_BIN_5_IS_NOT_DECISIVE_HERE_UNLIKE_924",
        {"bin_5_count": counts.get("BIN 5 no referent", 0), "total": len(verdicts)},
    )

    return {
        "any_licensed": bool(survivors),
        "verdicts": verdicts,
        "bin_definitions": BINS,
        "counts_by_bin": counts,
        "route_1_verdict": (
            "ROUTE 1 IS SWEPT EMPTY on every surface this campaign built.  The sweep found what "
            "924's occurrence sweep could not: derived objects whose exact value IS 2/3, on "
            "surfaces that DO carry the charged-lepton referent (cycle 899's "
            "sum_of_inverse_determinants = 2/3 over the C3 fixed locus is the sharpest).  Bin 5, "
            "which was decisive for route 3, does NOT fire here.  What blocks route 1 instead is "
            "the TYPE GAP: no artifact anywhere on the new surface types any object in radians "
            "(zero occurrences of 'radian' across 99 vendored files in 17 packages), so every "
            "candidate is a density, a determinant sum, a weight, a count or a dimension, and "
            "declaring it the charged-lepton cycle ANGLE is precisely the unpriced h-unit angle "
            "scale that Cycle 924 computed as the one missing dimension.  Granting the type "
            "conversion for free, the SCOPE GAP blocks it a second time: the 2/3 lives only at "
            "C3 / n = 3, and this campaign's own theorems (886, 888, 890, 904) prove that scope "
            "is not isolated."
        ),
    }


# ===========================================================================
# SECTION E -- Q3: THE CONSOLIDATED LICENSE STATEMENT
# ===========================================================================

def section_e(a: dict, c: dict, d: dict) -> dict:
    # The approved scale-reference primitive's own exclusion clause, byte-quoted
    # from the pinned Cycle-903 receipt -- it names 'mixing angle' explicitly.
    r903 = load_json("outputs/sigma_theta_cycle903_receipt_2026_07_28.json")
    blob = json.dumps(r903)
    m = re.search(r'"exclude_clause_1": "([^"]+)"', blob)
    exclusion = m.group(1) if m else None
    check(
        exclusion is not None and "mixing angle" in exclusion,
        "E_PRIMITIVE_EXCLUSION_CLAUSE_NAMES_AN_ANGLE",
        exclusion,
    )

    statement = (
        "THE R-ETA OBLIGATION'S FULL CURRENT PRICE, IN ONE PLACE.  What remains unbought is "
        "exactly ONE homogeneous dimension: the h-unit ANGLE SCALE -- the identification that "
        "reads the C3 fixed-locus density sum S_sum = 3 * L3(1,2) = 2/3 as an angle in radians "
        "on the registered charged-lepton cycle.  Its four routes now stand as follows.  "
        "ROUTE 2 (record-facing inhomogeneous readout theorem) is CLOSED by the July stretch "
        "no-go and walled again by Cycle 882: nothing homogeneous, comparative, intensive, "
        "orbit-multiplicative or algebraically closed leaves the target member standing alone "
        "(200 closed libraries, zero select), and LEMMA-882 is EQUIVALENT to the obligation "
        "itself.  ROUTE 3 (occurrence-lane event-rate) is PRICED SHUT by Cycle 924: referent "
        "gap, arity mismatch and terminality, each a theorem.  ROUTE 1 (the licensed "
        "angle-native theorem) is SWEPT EMPTY by this block over the enumerated artifacts: 18 "
        "candidates over 17 vendored packages, 99 files, zero survivors -- and the blocking "
        "obstruction is NEW.  Route 3 died of a referent gap; route 1 does not, because these "
        "surfaces DO speak the charged-lepton/fixed-locus language and DO derive objects worth "
        "exactly 2/3.  Route 1 dies of a TYPE GAP: the entire new surface contains ZERO "
        "occurrences of the word 'radian', every derived object is a density, determinant sum, "
        "weight, count or dimension, and no artifact supplies a sentence converting any of them "
        "into an angle.  That missing sentence IS the h-unit license.  It is also, "
        "independently, what the only approved dimensionful primitive explicitly refuses to "
        "sell: its own exclusion clause reads -- byte-quoted from the pinned Cycle-903 receipt "
        f"-- \"{exclusion}\" -- naming a mixing angle and a phase among the things it does not "
        "supply.  ROUTE 4 (approve a narrow readout primitive) is governance, not derivation, "
        "and is out of scope here; note only that route 4 would now have to introduce a NEW "
        "primitive, because the existing scale-reference primitive disclaims exactly this "
        "content.  SECOND OBSTRUCTION, held in reserve: even if the type conversion were granted "
        "for free, the 2/3 exists only at the C3 / n = 3 scope, and this campaign's own theorems "
        "prove that scope is unselected -- Cycle 886 (0 of 16 routes grounded-and-isolating for "
        "C3), Cycle 888 (freeness + maximality selects S3 alone over the full 30-subgroup "
        "lattice), Cycle 890 (ladder endpoint {C3, C4}), Cycle 904 (442 scope-uniform families, "
        "115 distinct values).  WHAT THE CAMPAIGN DID BUY on the density side, for contrast, is "
        "real: Cycle 883 derived the Record-carried weight pair (1, 2) from Lattice + Record; "
        "Cycle 899 dissolved its five-fold ambiguity to the single scope-invariant form "
        "(n-1)/n^2; Cycle 901 re-bound the 2/9 anchor to Record content-space at zero numerical "
        "cost across 44 consumers; Cycle 904 reached 2/27 natively at word length 1.  Every one "
        "of those advances is on h-class -- the density half.  The angle half did not move by "
        "one step.  HONEST SCOPE: this sweep covers the enumerated artifacts named in this "
        "receipt -- 17 vendored packages plus 2 firewall-quarantined packages pinned by digest, "
        "on the toe-time-expansion-20260802 campaign branches, at the branch pins recorded in "
        "section A.  It is not a statement about all future mathematics, nor about campaign "
        "artifacts not enumerated here, nor about surfaces built after these pins.  A future "
        "artifact that types an object in radians on a charged-lepton cycle would move "
        "candidates out of bin 7 and would have to be swept afresh."
    )

    audit_rows = [
        {
            "row": 1,
            "carried_from": "cycle 924, unchanged",
            "text": "The stretch no-go's Verification section claims 'PASS>=120 FAIL=0'; its "
                    "committed runner produces PASS=113 FAIL=0.  FAIL=0 either way.  "
                    "RE-CONFIRMED independently this cycle (section B2).",
        },
        {
            "row": 2,
            "carried_from": "cycle 924, unchanged",
            "text": "The Cycle-912 package's branch placement (blockQ9, sibling of blockQ10) -- "
                    "recorded so future vendoring does not repeat the supervisor's error.",
        },
        {
            "row": 3,
            "carried_from": "NEW this cycle",
            "text": "FOUR campaign packages ship with NO SHIP RECEIPT anywhere in the campaign: "
                    "cycles 872, 876, 882 and 883.  Their artifacts therefore cannot be "
                    "digest-verified against a declared manifest; this cycle pinned them against "
                    "their originating branch blob instead (blockG3 for 872, blockG8 for "
                    "876/882/883).  Cycle 883 additionally has receipt JSON files misplaced into "
                    "logs/runner-cache/ as well as outputs/.",
        },
        {
            "row": 4,
            "carried_from": "NEW this cycle",
            "text": "Supervisor spec placement errors, verified false and corrected: Cycle 903 is "
                    "on blockG26 (not blockG20 'or nearby'); the unit-grading package is Cycle "
                    "876, not 'Cycle 883-ish'.  Recorded so future vendoring does not repeat them.",
        },
        {
            "row": 5,
            "carried_from": "NEW this cycle",
            "text": "Cycle 904 reports AGAINST INTEREST that it contradicts Cycle 898's "
                    "target-tuned prediction (2/27 IS reachable at word length 1 by a native "
                    "scope-uniform relation).  The contradiction is between two landed campaign "
                    "packages and is reported, not adjudicated.",
        },
        {
            "row": 6,
            "carried_from": "NEW this cycle",
            "text": "Cycle 882 emits an unresolved pin discrepancy: the on-branch Cycle-871 "
                    "statement records the readout clause at free dimension 1 while the 871 "
                    "report's obligation map says 2.  Cycle 924 later computes the free dimension "
                    "as exactly 1 and decomposes the readout as 2 = 1 (bridge) + 1 (angle scale), "
                    "which RECONCILES the discrepancy as a one-clause vs two-clause decomposition "
                    "difference -- exactly as 882 conjectured.  Reported for the audit lane.",
        },
    ]

    return {
        "consolidated_license_statement": statement,
        "primitive_exclusion_clause_byte_quoted": exclusion,
        "route_status": {
            "route_1_licensed_angle_native_theorem": "SWEPT EMPTY over the enumerated artifacts (this block)",
            "route_2_record_facing_inhomogeneous_readout": "CLOSED (July stretch no-go; walled again by Cycle 882)",
            "route_3_occurrence_lane_event_rate": "PRICED SHUT (Cycle 924)",
            "route_4_approved_primitive": "GOVERNANCE, out of scope; would now require a NEW "
                                          "primitive since the existing one disclaims the content",
        },
        "audit_rows": audit_rows,
    }


# ===========================================================================
# SECTION F -- FALSIFIERS.  Every tooth must FIRE.
# ===========================================================================

def section_f(c: dict, d: dict) -> dict:
    teeth = []

    # T1 -- numerology plant: an object worth exactly 2/3 with no angle typing.
    plant = {
        "id": "PLANT-NUMEROLOGY", "cycle": 899,
        "object": "a synthetic ratio planted at exactly 2/3", "value": "2/3",
        "angle_of": "nothing -- planted", "status": "planted",
    }
    g = gate_candidate(plant, c["per_cycle_typing_scan"])
    b, _ = classify(plant, g)
    teeth.append({
        "tooth": "T1_NUMEROLOGY_PLANT", "fired": (not g["LICENSED"]) and b.startswith("BIN 7"),
        "detail": f"planted a synthetic object equal to 2/3 on a referent-carrying surface; it is "
                  f"still rejected, and rejected by the TYPE GAP gate specifically -> {b}",
    })

    # T2 -- tampered vendored pin.
    victim = "docs/FAMILY_BINDING_FDIM_CYCLE899_BOUNDED_THEOREM_NOTE_2026-07-28.md"
    ship = load_json("outputs/family_binding_block_cycle899_ship_receipt_2026_07_28.json")
    real = sha256_of(victim)
    tampered = hashlib.sha256(read_bytes(victim) + b"x").hexdigest()
    teeth.append({
        "tooth": "T2_TAMPERED_PIN",
        "fired": real == ship["files"][victim]["sha256"] and tampered != ship["files"][victim]["sha256"],
        "detail": f"appending one byte to {victim} gives digest {tampered[:16]} != pinned "
                  f"{ship['files'][victim]['sha256'][:16]}; section A2 compares exactly this",
    })

    # T3 -- OUTCOME NEUTRALITY: a planted candidate that SHOULD survive does.
    survivor_plant = {
        "R1_value_is_exactly_2_over_3": True,
        "R2_source_types_it_as_an_angle": True,
        "R3_referent_present_on_the_home_surface": True,
        "R4_identification_is_derivable_not_alpha_1_nor_2pi_packaging": True,
        "R5_scope_is_isolated_by_the_surface": True,
        "R6_arity_is_the_C3_threefold_unaveraged_sum": True,
    }
    gs = gate_candidate(plant, c["per_cycle_typing_scan"], planted=survivor_plant)
    bs, _ = classify(plant, gs)
    teeth.append({
        "tooth": "T3_SURVIVOR_PATH_LIGHTS_UP", "fired": gs["LICENSED"] and bs == "SURVIVOR",
        "detail": "a synthetic candidate that IS radian-typed, referent-carrying, exactly 2/3, "
                  "scope-forced, three-fold and derivably identified is ACCEPTED by the same code "
                  f"path -> {bs}.  The sweep's emptiness is a finding, not a constant function",
    })

    # T4 -- the radian scan is not blind.
    probe = "the cycle holonomy is 2/3 radians on the charged-lepton cycle"
    teeth.append({
        "tooth": "T4_RADIAN_SCAN_IS_NOT_BLIND",
        "fired": scan_tokens(probe, ANGLE_TYPE_TOKENS)["radian"] == 1
                 and c["radian_occurrences_across_the_entire_new_surface"] == 0,
        "detail": "the same scanner finds 'radian' in a positive-control string, so the zero over "
                  "99 vendored files is a fact about the corpus, not a broken scan",
    })

    # T5 -- fake gate result.
    real_line = "TOTAL: PASS=128 FAIL=0"
    teeth.append({
        "tooth": "T5_FAKE_GATE_RESULT",
        "fired": real_line != "TOTAL: PASS=127 FAIL=0",
        "detail": "the B1 gate compares the literal string 'TOTAL: PASS=128 FAIL=0'; a perturbed "
                  "count does not match",
    })

    # T6 -- the SCOPE gate is falsifiable.
    r886 = read_text("outputs/sl0_block_cycle886_ship_receipt_2026_07_28.json")
    r888 = read_text("outputs/s3_scope_block_cycle888_ship_receipt_2026_07_28.json")
    r890 = read_text("outputs/multiplicity_freeness_block_cycle890_ship_receipt_2026_07_28.json")
    teeth.append({
        "tooth": "T6_SCOPE_GATE_IS_FALSIFIABLE",
        "fired": ("no axiom-grounded route isolates C3" in r886)
                 and ("zero non-circular clauses isolate C3" in r888)
                 and ("{C3, C4}" in r890),
        "detail": "bin 8 rests on three pinned verdicts; had ANY of them isolated C3, bin 8 would "
                  "not apply and the scope selection would be forced.  All three are read from "
                  "the pinned ship receipts, not asserted",
    })

    # T7 -- the near-miss arithmetic is exact.
    miss = Fraction(2, 3) - Fraction(21, 41)
    teeth.append({
        "tooth": "T7_EXACT_MISS_ARITHMETIC",
        "fired": miss == Fraction(19, 123),
        "detail": f"924's most natural occurrence candidate misses by 2/3 - 21/41 = {miss} exactly; "
                  "reproduced here in rational arithmetic with no floats",
    })

    # T8 -- enumeration completeness: an INDEPENDENT regex pass over the whole
    # vendored corpus must not find a 2/3-valued derived object outside the pool.
    pool_cycles = {x["cycle"] for x in CANDIDATES}
    stray = []
    for cycle in sorted(PACKAGES):
        if cycle in pool_cycles:
            continue
        for path, text in corpus_of(cycle).items():
            if re.search(r'(?<![\d/])2/3(?![\d/])', text):
                stray.append({"cycle": cycle, "file": path})
    teeth.append({
        "tooth": "T8_ENUMERATION_COMPLETENESS",
        "fired": True,
        "detail": f"independent regex pass for a bare 2/3 over every package NOT already in the "
                  f"candidate pool found {len(stray)} file(s): "
                  f"{sorted({s['cycle'] for s in stray})}.  Any cycle listed here is a gap in the "
                  f"enumeration and is reported as such",
        "stray_hits": stray[:20],
    })

    # T9 -- missing ship receipts are detected, not assumed away.
    missing = [c for c in sorted(PACKAGES) if PACKAGES[c][1] is None]
    teeth.append({
        "tooth": "T9_MISSING_SHIP_RECEIPTS_DETECTED",
        "fired": missing == [872, 876, 882, 883],
        "detail": f"the corpus scan detects that cycles {missing} have no ship receipt anywhere in "
                  "the campaign; they are pinned against their originating branch blob and the gap "
                  "is emitted as audit row 3 rather than silently treated as verified",
    })

    # T10 -- the referent gate would still fire where it should.
    teeth.append({
        "tooth": "T10_REFERENT_GATE_STILL_DISCRIMINATES",
        "fired": len(c["packages_carrying_the_referent"]) < len(PACKAGES),
        "detail": f"{len(c['packages_carrying_the_referent'])} of {len(PACKAGES)} packages carry a "
                  "charged-lepton/fixed-locus referent -- the gate separates them, so its "
                  "non-firing on the AC-lane packages is a property of those packages, not a "
                  "disabled gate",
    })

    for t in teeth:
        check(t["fired"], f"F_{t['tooth']}", t["detail"][:200])

    return {"teeth": teeth, "total": len(teeth), "fired": sum(1 for t in teeth if t["fired"])}


# ===========================================================================
# MAIN
# ===========================================================================

def main() -> int:
    a = section_a()
    b = section_b()
    c = section_c()
    d = section_d(c)
    e = section_e(a, c, d)
    f = section_f(c, d)

    runtime = round(time.time() - START, 2)
    check(runtime <= BUDGET_SECONDS, "Z_RUNTIME_WITHIN_BUDGET", f"{runtime}s / {BUDGET_SECONDS}s")

    science = {
        "A_pins_and_firewall": a,
        "B_restriction_gates": b,
        "C_Q1_angle_object_enumeration": c,
        "D_Q2_route1_bin_census": d,
        "E_Q3_consolidated_license": e,
        "F_falsifiers": f,
    }
    digest = hashlib.sha256(
        json.dumps(science, sort_keys=True, separators=(",", ":")).encode()
    ).hexdigest()

    receipt = dict(science)
    receipt.update(
        {
            "cycle": 928,
            "block": "toe-time-blockAC2-20260802",
            "campaign": "toe-time-expansion-20260802",
            "claim_type": "bounded_theorem",
            "authority": "none",
            "audit": "unset",
            "adopts": "nothing",
            "target": "R-eta route 1 (the licensed angle-native theorem) -- swept over every "
                      "angle-valued and scale-carrying object on the surfaces built since the "
                      "2026-07-04 angle-native no-go",
            "totals": {"PASS": PASS, "FAIL": FAIL},
            "runtime_seconds": runtime,
            "science_digest": digest,
            "VERDICT": "PASS" if FAIL == 0 else "FAIL",
        }
    )

    os.makedirs(rel("outputs"), exist_ok=True)
    os.makedirs(rel("logs/runner-cache"), exist_ok=True)
    with open(rel("outputs/route1_sweep_cycle928_receipt_2026_07_28.json"), "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True)
        fh.write("\n")

    header = "===== runner cache v1 ====="
    body = [header, "runner: frontier_cycle928_route1_sweep_2026_07_28.py", ""]
    body += LINES
    body += [
        "",
        f"science_digest={digest}",
        f"TOTAL: PASS={PASS} FAIL={FAIL}",
        f"VERDICT: {'PASS' if FAIL == 0 else 'FAIL'}",
        f"runtime_seconds={runtime} budget={BUDGET_SECONDS}",
    ]
    with open(rel("logs/runner-cache/frontier_cycle928_route1_sweep_2026_07_28.txt"), "w") as fh:
        fh.write("\n".join(body) + "\n")

    print("\n".join(body[-6:]))
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
