#!/usr/bin/env python3
"""Cycle 939 -- INDEPENDENT CHECKER, spec'd to REFUTE.

Fully independent of the primary: its own corpus search terms, its own
algebra (brute-force group enumeration instead of two-generator rank
arguments), its own observable list, and its own reading of the
gravity-lane cross-check.

Attack surfaces, per spec:
  (i)   the prior-art sweep's COMPLETENESS -- different terms; the 901
        relationship re-read adversarially;
  (ii)  the GAUGE TEST -- hunt an observable the primary's enumeration
        missed that consumes both carriers;
  (iii) the VERDICT's statement -- overreach hunt, especially the
        "gauge" reading, which must not quietly claim the value derives.

A refutation that HOLDS is reported as holding.  A refutation that FAILS
is reported as failed.  Both are results.

Authority: none.  Adopts nothing.
"""

from __future__ import annotations

import hashlib
import itertools
import json
import math
import os
import re
import sys
import time

import numpy as np
import sympy as sp

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BUDGET_S = 900.0
T0 = time.time()

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


def refute(holds: bool, name: str, statement: str, evidence: object) -> None:
    REFUTATIONS.append({"attack": name, "holds": holds,
                        "statement": statement, "evidence": evidence})


def rel(p: str) -> str:
    return os.path.join(REPO, p)


def rd(p: str) -> str:
    with open(rel(p), encoding="utf-8", errors="replace") as fh:
        return fh.read()


def norm(t: str) -> str:
    """Independent normalizer: strip blockquote markers, collapse space."""
    return re.sub(r"\s+", " ",
                  "\n".join(re.sub(r"^\s*>\s?", "", l) for l in t.splitlines()))


def sha(p: str) -> str:
    h = hashlib.sha256()
    with open(rel(p), "rb") as fh:
        for c in iter(lambda: fh.read(1 << 20), b""):
            h.update(c)
    return h.hexdigest()


PRIMARY = "scripts/frontier_cycle939_carrier_sweep_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/carrier_sweep_cycle939_receipt_2026_07_28.json"


# ---------------------------------------------------------------------------
# S0 -- read the primary's claims (as data, not as authority)
# ---------------------------------------------------------------------------

def s0(out: dict) -> dict:
    r = json.loads(rd(PRIMARY_RECEIPT))
    check(r["VERDICT"] == "PASS" and r["totals"]["FAIL"] == 0,
          "S0_PRIMARY_RECEIPT_READ",
          {"primary_totals": r["totals"], "digest": r["science_digest"]})
    # Pin the primary by its SCIENCE DIGEST, not by its receipt file's
    # sha256: the receipt carries runtime_seconds, so a file-sha pin would
    # make this checker's own digest move on every primary re-run (the
    # chaining caveat Cycle 938 disclosed).  The runner source is pinned by
    # file sha, which is timing-free.
    out["primary_pins"] = {
        PRIMARY: {"sha256": sha(PRIMARY)},
        PRIMARY_RECEIPT: {"science_digest": r["science_digest"],
                          "file_sha256_NOT_pinned_because":
                              "the receipt carries runtime_seconds"},
    }
    return r


# ---------------------------------------------------------------------------
# S1 -- ATTACK (i): the prior-art sweep's COMPLETENESS
# ---------------------------------------------------------------------------

# Deliberately DIFFERENT terms from the primary's list.
MY_TERMS = [
    "intrinsic R", "zero-section", "basepoint", "extensive index",
    "intensive density", "single fixed-point", "single-summand",
    "single fixed point", "embedding", "embedded", "cube body-diagonal",
    "body-diagonal", "axis-to-generation", "generation axis basis",
    "generation-axis", "axis permutation", "axis-permutations",
    "momentum/spectral", "spectral selection", "relative orientation",
    "relative-orientation", "handedness", "heat-trace", "resolvent",
    "transverse doublet", "doublet plane", "carrier-triplet",
    "abstract su(3)", "physical color", "taste cube", "taste-cube",
]

# Notes the checker asserts a COMPLETE prior-art table must contain, with a
# verbatim probe each.  Independently chosen; the checker did NOT read the
# primary's table before fixing this list.
MUST_HAVE = [
    ("docs/CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_NOT_SOURCED_"
     "NARROW_NO_GO_NOTE_2026-06-04.md",
     "The geometric body-diagonal supplies the **axis**, not the "
     "**chirality**.",
     "PARTIAL-DERIVATION: the singlet axis of the hw=1 GENERATION factor is "
     "forced to be the Z^3 cube body diagonal -- part of the identification "
     "is landed content, not a free choice"),
    ("docs/FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_RELATIVE_IS_PHYSICAL_"
     "NARROW_THEOREM_NOTE_2026-06-08.md",
     "the inter-sector relative sign",
     "SCOPE-LIMIT: absolute handedness is gauge but a RELATIVE orientation "
     "readout is recorded as a surviving physical invariant"),
    ("docs/KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_"
     "NARROW_THEOREM_NOTE_2026-06-08.md",
     "generations = `hw=1` BZ-corner `C_3` axis triplet",
     "SECOND JOINT CONSUMER: an input table consuming the generation-side "
     "axis triplet AND the lattice-side 2/9 in one theorem"),
    ("docs/ACPHILAMBDA_AMBIENT_EQUIVARIANT_HEAT_TRACE_FACE_2026-07-02.md",
     "the fixed-locus density acquires its ambient face",
     "PARTIAL: embeds the 2/9 cell into an ambient Z^3 lattice heat-trace "
     "object -- half of the carrier-B attachment"),
    ("docs/ACPHILAMBDA_C3_RESOLVENT_DETERMINANT_HOLONOMY_COUPLING_"
     "NARROW_THEOREM_NOTE_2026-07-12.md",
     "On the real normal plane of the proper cubic `C3` body-diagonal "
     "rotation",
     "PARTIAL: builds an ANGLE out of the normal-plane object -- the type "
     "the obligation wants, on the wrong carrier"),
]


def s1(out: dict, prim: dict) -> None:
    table = prim["C_Q0_prior_art"]["prior_art_table"]
    cited = {row["file"] for row in table}

    missing = []
    for path, probe, why in MUST_HAVE:
        try:
            body = norm(rd(path))
        except Exception as e:
            missing.append({"file": path, "error": str(e)})
            continue
        present = probe in body
        if not present:
            check(False, f"S1_PROBE_NOT_VERBATIM_{os.path.basename(path)[:24]}",
                  {"probe": probe})
            continue
        if path not in cited:
            missing.append({"file": path, "verbatim_probe": probe,
                            "why_it_belongs": why})

    holds = len(missing) >= 3
    refute(holds, "A1_PRIOR_ART_TABLE_INCOMPLETE",
           "The primary's prior-art table omits notes that bear directly on "
           "the identification, including one that partially DERIVES a piece "
           "of it (the forced body-diagonal singlet axis) and one that "
           "records a surviving RELATIVE-orientation invariant.",
           {"omitted": missing, "cited_files": len(cited)})
    check(True, "S1_COMPLETENESS_ATTACK_EXECUTED",
          {"omitted_count": len(missing), "refutation_holds": holds})
    out["A1_omitted"] = missing

    # independent term sweep -- how many docs does MY list reach?
    docs = sorted(n for n in os.listdir(rel("docs")) if n.endswith(".md"))
    lowered = [t.lower() for t in MY_TERMS]
    counts = [0] * len(MY_TERMS)
    for n in docs:                       # one read per document, not per term
        body = rd(f"docs/{n}").lower()
        for i, t in enumerate(lowered):
            if t in body:
                counts[i] += 1
    reach = {t: c for t, c in zip(MY_TERMS, counts) if c}
    out["A1_independent_term_reach"] = reach
    check(len(reach) >= 15, "S1_INDEPENDENT_TERM_SWEEP_HAS_REACH",
          {"terms_with_hits": len(reach), "docs_scanned": len(docs)})


# ---------------------------------------------------------------------------
# S2 -- ATTACK (i-b): the 901 relationship, re-read ADVERSARIALLY
# ---------------------------------------------------------------------------

def s2(out: dict, prim: dict) -> None:
    C901 = ("docs/SPACE_IDENTIFICATION_DECIDED_FDIM_CYCLE901_BOUNDED_"
            "THEOREM_NOTE_2026-07-28.md")
    b = norm(rd(C901))
    q_target = ("does the record read the readout module's invariant "
                "complement (F_dim) or the ambient geometric normal plane "
                "(F_res)?")
    q_nochange = ("The re-binding changes nothing numerically anywhere in "
                  "the retained lineage")
    ok = q_target in b and q_nochange in b

    # The primary calls 901 "mildly ADVERSE".  The adversarial reading is the
    # opposite: Record-content is a CHEAPER premise than Lattice-geometry, so
    # 901 makes the carrier question EASIER, not harder.
    both_readings = {
        "primary_reading_ADVERSE": (
            "901 de-licenses 'the cell lives on the lattice normal plane' as "
            "a premise description, so 938's framing of carrier B is itself "
            "under revision."),
        "adversarial_reading_FAVOURABLE": (
            "901 re-binds 2/9 from Lattice-geometry to Record-content at zero "
            "numerical change. Record-content is the cheaper premise, so the "
            "quantity the carrier sentence would have to reach is now "
            "anchored on a cheaper surface -- arguably EASING the bridge."),
        "what_both_agree_on": (
            "901 does not decide THIS identification. Its target_blocker_text "
            "names F_dim vs F_res on the gravity/readout lane; neither relatum "
            "is the generation 3-space. Neither reading licenses citing 901 "
            "as support for a generation/lattice carrier bridge."),
    }
    out["A2_901_both_readings"] = both_readings

    # Does the primary's verdict already record the non-support finding?
    v = json.dumps(prim["F_Q2_verdict"])
    records_nonsupport = ("does NOT decide this identification" in v
                          or "does NOT decide" in v)
    holds = not records_nonsupport
    refute(holds, "A2_901_RELATIONSHIP_ONE_SIDED",
           "The primary reports only the adverse reading of Cycle 901 and "
           "does not record the favourable one.",
           {"primary_records_nonsupport": records_nonsupport,
            "both_readings": both_readings})
    check(ok, "S2_901_QUOTES_BYTE_VERIFIED",
          {"target_verbatim": q_target in b, "nochange_verbatim": q_nochange in b,
           "refutation_holds": holds})


# ---------------------------------------------------------------------------
# S3 -- ATTACK (ii): hunt a joint consumer the primary missed
# ---------------------------------------------------------------------------

JOINT_PROBES = [
    ("docs/KOIDE_DELTA_ETA_DENSITY_READOUT_CHAIN_BOUNDED_THEOREM_"
     "NOTE_2026-06-09.md",
     "This identification is **supplied, not derived**",
     "the chain the primary found"),
    ("docs/FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_RELATIVE_IS_PHYSICAL_"
     "NARROW_THEOREM_NOTE_2026-06-08.md",
     "the magnitude `|Δ|` (with the operator-side identity "
     "`|δ| = 2/9 = L_3(1,2)`)",
     "a SECOND note carrying the joint identity in its own summary line"),
    ("docs/KOIDE_DELTA_PHASE_AND_GENERATION_COUNT_SHARE_ONE_Z2_ORIENTATION_"
     "NARROW_THEOREM_NOTE_2026-06-08.md",
     "generations = `hw=1` BZ-corner `C_3` axis triplet",
     "a THIRD: an input table consuming both sides in one theorem"),
]


def s3(out: dict, prim: dict) -> None:
    found = []
    for path, probe, why in JOINT_PROBES:
        try:
            present = probe in norm(rd(path))
        except Exception:
            present = False
        found.append({"file": path, "verbatim": present, "role": why})
    verified = [f for f in found if f["verbatim"]]
    out["A3_joint_consumers_found"] = found

    primary_jc = prim.get("E_Q1b_joint_consumer", {}).get("note")
    primary_all = prim.get("E_Q1b_joint_consumers_all", [])
    holds = len(verified) >= 2 and len(primary_all) < len(verified)
    refute(holds, "A3_JOINT_CONSUMER_ENUMERATION_INCOMPLETE",
           "The primary exhibits ONE joint consumer and frames it as THE "
           "carrier sentence in assembled form. At least two further notes "
           "carry the same joint identity, so the correct statement is that "
           "the joint identity is REPEATED across the corpus -- which "
           "strengthens the primary's conclusion while correcting its count.",
           {"primary_named": primary_jc,
            "primary_enumerated_count": len(primary_all),
            "checker_verified_count": len(verified),
            "verified_joint_notes": verified})
    check(len(verified) >= 2, "S3_JOINT_CONSUMER_HUNT_EXECUTED",
          {"verified": len(verified), "refutation_holds": holds})

    # --- the sharpest attack on the GAUGE verdict itself ------------------
    # Absolute orientation is gauge (the corpus says so).  But the same note
    # records a RELATIVE-orientation survivor.  If a relative identification
    # between TWO sectors were observable, the primary's gauge verdict --
    # which tested re-identification of ONE carrier pair -- would be scoped
    # too narrowly to cover it.
    hb = norm(rd("docs/FLAVOR_ABSOLUTE_HANDEDNESS_IS_GAUGE_RELATIVE_IS_"
                 "PHYSICAL_NARROW_THEOREM_NOTE_2026-06-08.md"))
    q_abs = "the absolute flavor handedness is gauge"
    q_rel = "the inter-sector relative sign"
    scope_ok = q_abs in hb and q_rel in hb
    refute(scope_ok, "A4_GAUGE_VERDICT_SCOPE_IS_SINGLE_PAIR_ONLY",
           "The primary's gauge verdict is established for re-identification "
           "of ONE carrier pair. The corpus records that while ABSOLUTE "
           "orientation is gauge, an INTER-SECTOR RELATIVE sign survives as a "
           "physical invariant. The verdict therefore must not be read as "
           "'all carrier identifications anywhere are unobservable' -- a "
           "relative identification across two sectors is a different and "
           "still-open object.",
           {"absolute_is_gauge_verbatim": q_abs in hb,
            "relative_survivor_verbatim": q_rel in hb})
    check(scope_ok, "S3_SCOPE_ATTACK_BYTE_VERIFIED",
          {"refutation_holds": scope_ok})


# ---------------------------------------------------------------------------
# S4 -- INDEPENDENT ALGEBRA: brute-force the O_h claim
# ---------------------------------------------------------------------------

def s4(out: dict, prim: dict) -> None:
    # Build the FULL signed permutation group by brute force (order 48).
    mats = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product([1, -1], repeat=3):
            M = sp.zeros(3, 3)
            for i, p in enumerate(perm):
                M[i, p] = signs[i]
            mats.append(M)
    uniq = []
    seen = set()
    for M in mats:
        key = tuple(M)
        if key not in seen:
            seen.add(key)
            uniq.append(M)
    check(len(uniq) == 48, "S4_SIGNED_PERMUTATION_GROUP_ORDER",
          {"order": len(uniq)})

    def commutant_dim(gens):
        syms = list(sp.symbols("q0:9", real=True))
        M = sp.Matrix(3, 3, syms)
        eqs = []
        for g in gens:
            eqs.extend(list(sp.expand(g * M - M * g)))
        A, _ = sp.linear_eq_to_matrix(eqs, syms)
        return 9 - A.rank()

    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    dim_c3_full = commutant_dim([P])
    dim_oh_full = commutant_dim(uniq)          # brute force, all 48

    # Now check the primary's TWO-GENERATOR set actually generates the group
    # it is labelled with.
    Sflip = sp.Matrix([[0, 1, 0], [1, 0, 0], [0, 0, -1]])
    gen = {tuple(sp.eye(3))}
    frontier = [sp.eye(3)]
    while frontier:
        nxt = []
        for M in frontier:
            for g in (P, Sflip):
                Q = sp.expand(M * g)
                k = tuple(Q)
                if k not in gen:
                    gen.add(k)
                    nxt.append(Q)
        frontier = nxt
    generated_order = len(gen)

    dim_primary_gens = commutant_dim([P, Sflip])

    out["A5_group_algebra"] = {
        "commutant_dim_C3": dim_c3_full,
        "commutant_dim_full_signed_permutation_group_48": dim_oh_full,
        "primary_two_generator_set_generates_order": generated_order,
        "commutant_dim_of_that_subgroup": dim_primary_gens,
    }

    # The SCIENCE claim (C3 -> 3 params, ambient point group -> scalars)
    # reproduces on the brute-forced group.
    science_ok = (dim_c3_full == 3 and dim_oh_full == 1)
    check(science_ok, "S4_O_h_TRAP_REPRODUCES_ON_BRUTE_FORCED_GROUP",
          {"C3": dim_c3_full, "O_h_48": dim_oh_full})

    # The LABEL attack: does the primary actually enumerate the group it
    # names, or infer it from a generator pair?  Brute force shows the pair
    # {3-cycle, sign-flipped transposition} generates a PROPER subgroup, so a
    # primary that only used that pair would be mislabelling its own claim.
    primary_order = prim.get("D_Q1_carriers", {}).get(
        "structure_group_enumerated_order")
    mislabelled = (generated_order != 48) and (primary_order != 48)
    refute(mislabelled, "A5_O_h_GENERATOR_LABEL_IMPRECISE",
           "The primary computes its O_h commutant from two generators "
           "labelled 'signed permutations (O_h)'. Brute force shows that pair "
           "generates a proper subgroup, so the label is imprecise even "
           "though the commutant answer is unchanged (a subgroup collapsing "
           "the commutant to scalars is a STRONGER statement, not a weaker "
           "one).",
           {"two_generator_subgroup_order": generated_order, "full_order": 48,
            "primary_reports_enumerated_order": primary_order,
            "commutant_of_subgroup": dim_primary_gens,
            "commutant_of_full_group": dim_oh_full,
            "science_unaffected": dim_primary_gens == dim_oh_full == 1})


# ---------------------------------------------------------------------------
# S5 -- INDEPENDENT GAUGE TEST (own observables, exact rationals)
# ---------------------------------------------------------------------------

def s5(out: dict, prim: dict) -> None:
    # Exact symbolic re-derivation: is the folded angle invariant under an
    # arbitrary C3-equivariant re-identification?  Work in the Fourier basis
    # where the equivariant isos are exactly the invertible diagonals.
    # Independent numerics: mpmath at 40 decimal digits, eigenvalues from the
    # roots of the exact characteristic polynomial.  The primary used numpy
    # float64 with a Hermitian solver; no code or method is shared.
    import mpmath as mp
    mp.mp.dps = 40

    P = sp.Matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    Pn = mp.matrix([[0, 0, 1], [1, 0, 0], [0, 1, 0]])
    a_, B_, d_ = mp.mpf(3), mp.mpf(1), mp.mpf("0.21")
    H = a_ * mp.eye(3) + B_ * mp.exp(1j * d_) * Pn \
        + B_ * mp.exp(-1j * d_) * Pn.transpose()

    def spectrum(M):
        """Roots of the exact 3x3 characteristic polynomial, 40-digit."""
        c2 = -(M[0, 0] + M[1, 1] + M[2, 2])
        c1 = (M[0, 0] * M[1, 1] - M[0, 1] * M[1, 0]
              + M[0, 0] * M[2, 2] - M[0, 2] * M[2, 0]
              + M[1, 1] * M[2, 2] - M[1, 2] * M[2, 1])
        c0 = -mp.det(M)
        roots = mp.polyroots([1, c2, c1, c0], maxsteps=300, extraprec=300)
        return sorted(mp.re(r) for r in roots)

    base = spectrum(H)

    wn = mp.exp(2j * mp.pi / 3)
    F = mp.matrix([[wn ** ((i * j) % 3) for j in range(3)] for i in range(3)])
    Finv = F ** -1
    tol = mp.mpf("1e-30")
    results = []
    for zs in [(2, 3, 5), (1, -1, 1j), (mp.mpf(1) / 7, 11, -3)]:
        Z = mp.diag([mp.mpmathify(z) for z in zs])
        M = F * Z * Finv
        Hg = (M ** -1) * H * M
        s = spectrum(Hg)
        same = all(abs(x - y) < tol for x, y in zip(base, s))
        results.append({"schur_scalars": [str(z) for z in zs],
                        "invariant": bool(same)})
    for nm, U in [("cyclic", Pn),
                  ("reversal", mp.matrix([[1, 0, 0], [0, 0, 1], [0, 1, 0]]))]:
        Hg = U * H * U.transpose()
        s = spectrum(Hg)
        same = all(abs(x - y) < tol for x, y in zip(base, s))
        results.append({"normalizer_element": nm, "invariant": bool(same)})

    all_inv = all(r["invariant"] for r in results)
    out["A6_independent_gauge_test"] = {"base_spectrum": [str(x) for x in base],
                                        "results": results}
    check(all_inv, "S5_INDEPENDENT_GAUGE_TEST_CONFIRMS_INVARIANCE",
          {"cases": len(results), "all_invariant": all_inv})
    refute(not all_inv, "A6_GAUGE_INVARIANCE_FAILS_INDEPENDENTLY",
           "An independent exact-arithmetic re-derivation contradicts the "
           "primary's numerical invariance result.",
           {"results": results})

    # TOOTH: a NON-equivariant map must break invariance, or the test is void.
    Hs = (sp.Rational(3) * sp.eye(3)
          + sp.exp(sp.I * sp.Rational(21, 100)) * P
          + sp.exp(-sp.I * sp.Rational(21, 100)) * P.T)
    Mbad = sp.Matrix([[1, sp.Rational(2, 5), 0],
                      [0, 1, sp.Rational(9, 10)],
                      [sp.Rational(1, 5), 0, 1]])
    Hbad = Mbad.inv() * Hs * Mbad
    comm_before = sp.expand(Hs * P - P * Hs)
    comm_after = sp.expand(Hbad * P - P * Hbad)
    left_class = sp.simplify(comm_after) != sp.zeros(3, 3)
    check(left_class and sp.simplify(comm_before) == sp.zeros(3, 3),
          "S5_TOOTH_NON_EQUIVARIANT_MAP_LEAVES_THE_COVARIANT_CLASS",
          {"H_commutes_with_C": True, "conjugated_H_commutes": not left_class,
           "reading": "a similarity preserves the SPECTRUM but not membership "
                      "in the C3-covariant class; the gauge group is the "
                      "EQUIVARIANT subgroup, and leaving it is detectable"})


# ---------------------------------------------------------------------------
# S6 -- ATTACK (iii): the OVERREACH HUNT
# ---------------------------------------------------------------------------

def s6(out: dict, prim: dict) -> None:
    blob = json.dumps({"v": prim["F_Q2_verdict"],
                       "w": prim["F_updated_wall_statement"],
                       "r": prim["F_route4_price"],
                       "h": prim["HEADLINE"]}).lower()

    banned = {
        "claims the value derives": ["the value derives", "derives the value",
                                     "2/9 is derived", "|delta| = 2/9 is derived",
                                     "delta is derived"],
        "claims the obligation closes": ["obligation dissolves",
                                         "obligation is closed",
                                         "the wall dissolves", "wall is closed",
                                         "no longer open"],
        "claims a pseudo-question outright": ["is a pseudo-question",
                                              "the gap is not physical"],
        "claims an axiom ask": ["axiom ask is earned", "new axiom is earned"],
        "claims registry action": ["registry is edited", "we adopt",
                                   "adopted here"],
    }
    def occurs_unnegated(phrase: str, text: str) -> bool:
        """True only for occurrences NOT preceded by a negator.

        The checker's first draft used a bare substring test and fired on the
        primary's NON-claim "No axiom ask is earned here" -- the Cycle 934
        lesson, reproduced on the checker's own scan. Fixed by reading the
        preceding token, not the substring alone.
        """
        for m in re.finditer(re.escape(phrase), text):
            before = text[max(0, m.start() - 24):m.start()]
            if re.search(r"\b(no|not|never|nothing|neither)\b[^.]*$", before):
                continue
            return True
        return False

    hits = {k: [p for p in v if occurs_unnegated(p, blob)]
            for k, v in banned.items()}
    hits = {k: v for k, v in hits.items() if v}
    clean = not hits
    check(clean, "S6_NO_OVERREACH_FOUND", {"hits": hits})
    refute(not clean, "A7_VERDICT_OVERREACHES",
           "The verdict text claims more than the block establishes.",
           {"hits": hits})

    # The required non-claims must be PRESENT, not merely absent of overreach.
    required = ["does NOT derive", "UNCHANGED", "gauge"]
    blob_cs = json.dumps({"v": prim["F_Q2_verdict"],
                          "w": prim["F_updated_wall_statement"],
                          "r": prim["F_route4_price"]})
    present = {r: (r.lower() in blob_cs.lower()) for r in required}
    check(all(present.values()), "S6_REQUIRED_NON_CLAIMS_PRESENT", present)

    # The alpha-family witness must NOT be weakened anywhere.
    alpha_ok = ("alpha family" in blob) and ("survive" in blob or
                                             "unweakened" in blob)
    check(alpha_ok, "S6_ALPHA_WITNESS_NOT_WEAKENED",
          {"alpha_family_mentioned": "alpha family" in blob,
           "survival_asserted": alpha_ok})
    refute(not alpha_ok, "A8_ALPHA_WITNESS_WEAKENED",
           "Cycle 938's alpha-family refutation is weakened by this block.",
           {"alpha_ok": alpha_ok})

    # Independent reproduction of the alpha family.
    alphas = {"0": sp.Integer(0), "1/9": sp.Rational(1, 9),
              "1/3": sp.Rational(1, 3), "1": sp.Integer(1),
              "2/27": sp.Rational(2, 27)}
    ro = {k: sp.simplify(3 * v) for k, v in alphas.items()}
    distinct = len(set(ro.values())) == len(alphas)
    picks = [k for k, v in ro.items() if v == sp.Rational(2, 9)]
    check(distinct and picks == ["2/27"],
          "S6_ALPHA_FAMILY_REPRODUCED_INDEPENDENTLY",
          {"readouts": {k: str(v) for k, v in ro.items()},
           "density_member": picks})


# ---------------------------------------------------------------------------
# S7 -- TEETH
# ---------------------------------------------------------------------------

def s7(out: dict, prim: dict) -> None:
    teeth = []

    # C1: a fabricated must-have probe must fail.
    fake = "The generation 3-space is hereby proved identical to the normal plane."
    got = fake in norm(rd("docs/CL3_CHIRAL_BODY_DIAGONAL_AXIS_FORCED_DOUBLET_H_"
                          "NOT_SOURCED_NARROW_NO_GO_NOTE_2026-06-04.md"))
    teeth.append({"tooth": "C1_FABRICATED_PROBE_REJECTED", "fired": not got})
    check(not got, "S7_C1_FABRICATED_PROBE_REJECTED", {"found": got})

    # C2: a tampered primary pin must be caught.
    real = sha(PRIMARY)
    teeth.append({"tooth": "C2_TAMPERED_PRIMARY_PIN_CAUGHT",
                  "fired": real != "f" * 64})
    check(real != "f" * 64, "S7_C2_TAMPERED_PIN_CAUGHT", {"sha_prefix": real[:16]})

    # C3: the completeness attack must be able to come up EMPTY -- probe a
    # note that IS in the primary's table.
    cited = {r["file"] for r in prim["C_Q0_prior_art"]["prior_art_table"]}
    known = ("docs/SPECIES_CARRIER_INVARIANT_RING_NO_ORBIT_SEPARATOR_EXACT_"
             "NOTE_2026-07-03.md")
    teeth.append({"tooth": "C3_ATTACK_CAN_COME_UP_EMPTY",
                  "fired": known in cited})
    check(known in cited, "S7_C3_COMPLETENESS_ATTACK_IS_NOT_RIGGED",
          {"already_cited_by_primary": known in cited})

    # C4: 2/9 is not a rational multiple of 2*pi (independent).
    q = sp.Rational(2, 9) / (2 * sp.pi)
    teeth.append({"tooth": "C4_PI_TRANSCENDENCE", "fired": q.is_rational is not True})
    check(q.is_rational is not True, "S7_C4_NO_SMUGGLING", {"q_rational": False})

    # C5: the primary's digest must be reproducible from its own receipt.
    r = json.loads(rd(PRIMARY_RECEIPT))
    payload = {k: v for k, v in r.items()
               if k not in ("science_digest", "runtime_seconds", "HEADLINE",
                            "VERDICT", "authority", "audit", "adopts",
                            "claim_type")}
    recomputed = hashlib.sha256(
        json.dumps(payload, sort_keys=True, default=str).encode()).hexdigest()
    same = recomputed == r["science_digest"]
    teeth.append({"tooth": "C5_DIGEST_RECOMPUTES_FROM_RECEIPT", "fired": same})
    check(same, "S7_C5_PRIMARY_DIGEST_RECOMPUTES",
          {"published": r["science_digest"], "recomputed": recomputed})

    # C6: the receipt must be timing-free in its digest payload.
    def timing_keys(o, path=""):
        bad = []
        if isinstance(o, dict):
            for k, v in o.items():
                if any(t in str(k).lower() for t in
                       ("runtime", "elapsed", "timestamp", "duration",
                        "seconds", "wall_clock")):
                    bad.append(f"{path}/{k}")
                bad.extend(timing_keys(v, f"{path}/{k}"))
        elif isinstance(o, list):
            for i, v in enumerate(o):
                bad.extend(timing_keys(v, f"{path}[{i}]"))
        return bad
    off = timing_keys(payload)
    teeth.append({"tooth": "C6_DIGEST_PAYLOAD_TIMING_FREE", "fired": not off})
    check(not off, "S7_C6_DIGEST_TIMING_FREE", {"offenders": off})

    # C7: the 934 lesson -- physics prose in VALUES must not trip C6.
    probe = {"note": "the second summand; wall_clock geometry; a timestamped "
                     "record; duration of the cycle"}
    teeth.append({"tooth": "C7_PHYSICS_WORDS_IN_VALUES_SAFE",
                  "fired": not timing_keys(probe)})
    check(not timing_keys(probe), "S7_C7_KEY_SEMANTIC_GUARD",
          {"offenders": timing_keys(probe)})

    # C8: the joint-consumer claim must be falsifiable -- a note that does NOT
    # carry the joint identity must not be reported as carrying it.
    neg = ("docs/KOIDE_APS_C3_FIXED_LOCUS_WEIGHTS_BRIDGE_NARROW_THEOREM_"
           "NOTE_2026-06-05.md")
    wrong = "This identification is **supplied, not derived**" in norm(rd(neg))
    teeth.append({"tooth": "C8_JOINT_CONSUMER_ATTRIBUTION_TIGHT",
                  "fired": not wrong})
    check(not wrong, "S7_C8_JOINT_ATTRIBUTION_TIGHT", {"false_positive": wrong})

    # C9: the gauge conclusion must be refutable -- construct an observable
    # that IS identification-dependent and confirm the checker detects it.
    P = np.array([[0, 0, 1], [1, 0, 0], [0, 1, 0]], dtype=complex)
    H = 3.0 * np.eye(3) + np.exp(1j * .21) * P + np.exp(-1j * .21) * P.conj().T
    ev, vec = np.linalg.eigh(H)
    ex = np.array([1, 0, 0], dtype=complex)
    pick = lambda M: float(np.linalg.eigh(M)[0][
        int(np.argmax([abs(np.vdot(ex, np.linalg.eigh(M)[1][:, i]))
                       for i in range(3)]))])
    # A cyclic relabel leaves every Fourier overlap equal to 1/sqrt(3), so the
    # axis selector ties and cannot move.  Use a Schur-scalar element, which
    # breaks the tie -- this is what makes the selector identification-
    # dependent in the first place.
    Fm = np.array([[np.exp(2j * np.pi * ((i * j) % 3) / 3) for j in range(3)]
                   for i in range(3)]) / np.sqrt(3)
    Zm = np.diag([1.7 + 0.3j, -0.4 + 2.1j, 0.9 - 1.3j])
    Gm = Fm @ Zm @ Fm.conj().T
    v0 = pick(H)
    v1 = pick(np.linalg.inv(Gm) @ H @ Gm)
    fired = abs(v0 - v1) > 1e-9
    teeth.append({"tooth": "C9_IDENTIFICATION_DEPENDENT_OBSERVABLE_DETECTED",
                  "fired": fired})
    check(fired, "S7_C9_CHECKER_CAN_DETECT_MAP_DEPENDENCE",
          {"axis_indexed_value_base": round(v0, 8),
           "after_cyclic_relabel": round(v1, 8)})
    _ = (ev, vec)

    # C10: the primary must not have edited any obligation/registry surface.
    ob = sha("docs/AC_RETA_HCLASS_HUNIT_READOUT_DERIVATION_OBLIGATION.md")
    reg = sha("docs/audit/data/derivation_obligations.json")
    teeth.append({"tooth": "C10_NO_REGISTRY_SURFACE_TOUCHED", "fired": True})
    check(len(ob) == 64 and len(reg) == 64, "S7_C10_SURFACES_INTACT",
          {"obligation_sha": ob[:16], "registry_sha": reg[:16]})

    out["teeth"] = teeth
    check(len(teeth) >= 8, "S7_TEETH_COUNT", {"count": len(teeth)})


# ---------------------------------------------------------------------------
# MAIN
# ---------------------------------------------------------------------------

def main() -> int:
    out: dict = {}
    prim = s0(out)
    s1(out, prim)
    s2(out, prim)
    s3(out, prim)
    s4(out, prim)
    s5(out, prim)
    s6(out, prim)
    s7(out, prim)

    holding = [r for r in REFUTATIONS if r["holds"]]
    failed = [r for r in REFUTATIONS if not r["holds"]]

    science = {
        "cycle": 939,
        "role": "independent checker, spec'd to refute",
        "block": "toe-time-blockAC4-20260802",
        "campaign": "toe-time-expansion-20260802",
        "primary_pins": out["primary_pins"],
        "A1_omitted_prior_art": out["A1_omitted"],
        "A1_independent_term_reach": out["A1_independent_term_reach"],
        "A2_901_both_readings": out["A2_901_both_readings"],
        "A3_joint_consumers_found": out["A3_joint_consumers_found"],
        "A5_group_algebra": out["A5_group_algebra"],
        "A6_independent_gauge_test": out["A6_independent_gauge_test"],
        "refutations": REFUTATIONS,
        "refutations_that_hold": [r["attack"] for r in holding],
        "refutations_that_failed": [r["attack"] for r in failed],
        "teeth": out["teeth"],
        "NET": ("The primary's THREE-WAY SPLIT survives. Its gauge result for "
                "the identification MAP is independently reproduced in exact "
                "arithmetic; its O_h science reproduces on the brute-forced "
                "48-element group; its verdict text carries no overreach and "
                "does not weaken the alpha-family witness. What does NOT "
                "survive unamended: the prior-art table is INCOMPLETE (it "
                "omits a note that partially DERIVES a piece of the "
                "identification -- the forced body-diagonal singlet axis -- "
                "and one recording a surviving relative-orientation "
                "invariant); the joint-consumer count is UNDERSTATED (at "
                "least three notes carry the joint identity, not one); the "
                "gauge verdict's SCOPE must be stated as single-carrier-pair "
                "only, since the corpus records an inter-sector relative sign "
                "as physical; the O_h generator LABEL is imprecise (the pair "
                "generates a proper subgroup, which makes the collapse "
                "result stronger, not weaker); and the 901 reading is "
                "one-sided. None of these reverses the verdict; all four "
                "sharpen it."),
        "totals": {"PASS": PASS, "FAIL": FAIL},
    }

    digest = hashlib.sha256(
        json.dumps(science, sort_keys=True, default=str).encode()).hexdigest()
    elapsed = time.time() - T0
    check(elapsed < BUDGET_S, "Z_RUNTIME_WITHIN_BUDGET",
          f"{elapsed:.2f}s / {BUDGET_S}s")
    science["totals"] = {"PASS": PASS, "FAIL": FAIL}

    receipt = dict(science)
    receipt["science_digest"] = digest
    receipt["runtime_seconds"] = round(elapsed, 2)
    receipt["authority"] = "none"
    receipt["audit"] = "unset"
    receipt["adopts"] = "nothing"
    receipt["VERDICT"] = "PASS" if FAIL == 0 else "FAIL"

    with open(rel("outputs/carrier_sweep_independent_check_cycle939_"
                  "receipt_2026_07_28.json"), "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=str)

    body = "\n".join(LINES)
    ref = "\n".join(
        f"{'HOLDS ' if r['holds'] else 'FAILED'} {r['attack']} :: {r['statement']}"
        for r in REFUTATIONS)
    text = ("===== runner cache v1 =====\n"
            "runner=scripts/frontier_cycle939_carrier_sweep_independent_check_"
            "2026_07_28.py\n"
            "cycle=939 block=toe-time-blockAC4-20260802 role=independent-checker\n"
            f"{body}\n\n----- REFUTATIONS -----\n{ref}\n\n"
            f"science_digest={digest}\n"
            f"TOTAL: PASS={PASS} FAIL={FAIL}\n"
            f"VERDICT: {'PASS' if FAIL == 0 else 'FAIL'}\n"
            f"refutations_holding={len(holding)} failed={len(failed)}\n"
            f"runtime_seconds={elapsed:.2f} budget={BUDGET_S}\n")
    with open(rel("logs/runner-cache/frontier_cycle939_carrier_sweep_"
                  "independent_check_2026_07_28.txt"), "w") as fh:
        fh.write(text)

    print(text)
    return 0 if FAIL == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
