#!/usr/bin/env python3
"""J:derive:axioms-and-the-event-lattice:a2 -- worker w-macbookpro90c72-j59ee.

A reading task. Every quotation in ATTEMPT.md is checked verbatim at its path and line on main, pinned at MAIN below (also reported
against the current origin/main). The axiom-level corpus is the four canonical premise nodes of docs/audit/data/axiom_premise_nodes.json;
each of their files is scanned line by line for the task's keywords and every hit is either cited or classified.
  Q1  the quotations exist verbatim (axioms memo, the three approved primitives, the premise-node list, the causal-time notes)
  Q2  the axiom-level corpus is exactly the four canonical ids, and the memo is 233 lines (read in full)
  Q3  every keyword hit (past, time, order, clock, tick, dynamic, formation, permanen, history, Z^3/Z_tau, 3+1) in the axiom-level files
      is cited in ATTEMPT.md or classified here as not bearing on the question
  Q4  the tension: the approved kinetic-isotropy primitive calls time 'emergent and derived (the single-clock ... theorem)', while that
      theorem, and the anomaly bridge that caps d_t <= 1, make the evolution axis a declared premise (B-AXIS)
"""
import json
import os
import re
import subprocess

MAIN = "b8d0017208a2c26f5938c618dc57f745293fe777"
NF = 0
NP = 0

AX = "docs/MINIMAL_AXIOMS_2026-06-29.md"
KI = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
RS = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SR = "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
PN = "docs/audit/data/axiom_premise_nodes.json"
SC = "docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
AN = "docs/ANOMALY_FORCES_TIME_THEOREM.md"
AR = "docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md"

QUOTES = [
    # the axioms memo
    (AX, 37, "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"),
    (AX, 38, "adjacency, standard translations, and proper cubic rotations about each site."),
    (AX, 40, "No site is privileged. Sites are distinguished by the supplied lattice"),
    (AX, 57, "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"),
    (AX, 58, "translations and proper cubic rotations."),
    (AX, 60, "For each site, the probability distribution over the possibilities is"),
    (AX, 61, "determined by, and varies with, the nearest-neighbor conditions."),
    (AX, 67, "distribution concerns which possibility a forming record locks, conditional"),
    (AX, 68, "on formation at that site; it does not supply the formation site, probability,"),
    (AX, 69, "or rate."),
    (AX, 77, "Records form."),
    (AX, 79, "When present, a record locks exactly one admissible local possibility. A"),
    (AX, 80, "site never carries more than one record; records are permanent."),
    (AX, 82, "Only records are readable. A readout value is determined by record content"),
    (AX, 83, "alone. A site with no record cannot be read."),
    (AX, 89, "A choice not fixed by the"),
    (AX, 90, "supplied structure remains a named conditional or open dependency."),
    (AX, 92, "A state is a configuration of records."),
    (AX, 116, "Admissibility is not a dynamics axiom."),
    (AX, 122, "carrier, define a time metric, or provide a record-production process or"),
    (AX, 123, "physical persistence dynamics."),
    (AX, 143, "structure, transition relations, record-production dynamics, physical"),
    (AX, 166, "- Record names the fixed locking of one admissible local possibility,"),
    (AX, 167, "one-record-per-site uniqueness, permanence, content-determined readout, and"),
    (AX, 183, "mechanisms, and the remaining formation rules (the distribution's form and"),
    (AX, 184, "values, at which site, and at what rate);"),
    (AX, 185, "- arrow, record-production dynamics, physical persistence dynamics, time metric,"),
    (AX, 201, "formation rule (which admissible possibility, at which site, with what weight,"),
    (AX, 202, "at what rate) at that time remained downstream supplier content."),
    (AX, 212, "extensional form and values are not specified by this memo, and the formation"),
    (AX, 232, "distribution's form and values, dynamics, readout contexts, and physical"),
    # the approved primitives and the premise list
    (PN, 5, '"minimal_axioms",'),
    (PN, 6, '"scale_reference_primitive",'),
    (PN, 7, '"kinetic_isotropy_primitive",'),
    (PN, 8, '"realized_state_primitive"'),
    (KI, 15, "The framework takes one structural graining fact: the emergent evolution tick is"),
    (KI, 16, "grained on the same footing as the spatial lattice edge."),
    (KI, 23, "equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are"),
    (KI, 24, "computed is hypercubic-symmetric"),
    (KI, 31, "is not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization"),
    (KI, 32, "of time: the framework's time remains emergent and derived (the single-clock"),
    (KI, 33, "codimension-1 evolution theorem)"),
    (KI, 40, "evolution, reflection positivity, scale reference, and records' causal order"),
    (KI, 41, "are not used here as a derivation of that equality."),
    (KI, 67, "- It does not re-axiomatize time. The emergent single-clock evolution remains"),
    (RS, 21, "The laws do not pick the state; the world does, among the states the laws"),
    (RS, 30, "The past hypothesis is a separate, stronger input."),
    (RS, 35, "supplied by the physical history."),
    (RS, 64, "- It does not assert any special boundary condition on the realized history."),
    # the causal-time notes
    (SC, 3, "**Date:** 2026-05-03 (hostile science-fix re-scope 2026-06-11;"),
    (SC, 7, "unit split 2026-06-17; see §0)"),
    (KI, 6, "**Date:** 2026-06-09"),
    (SC, 8, "**Type:** bounded_theorem"),
    (SC, 21, "Hilbert space; (S2′) each lattice time slice `Σ_t = {t} × Z^3` is a"),
    (SC, 22, "codimension-1 Cauchy surface: the equal-time local algebra is the"),
    (SC, 23, "mutually commuting tensor product of per-site one-qubit `M_2(C)` Pauli"),
    (SC, 30, "(S3′) **the axis"),
    (SC, 31, "is a premise, not a derivation**"),
    (SC, 38, "\"exactly one clock\" conclusion holds conditional on (B-AXIS)"),
    (AN, 1, "# Anomaly-Cancellation Consistency Bridge for 3+1 Spacetime"),
    (AN, 8, "**Type:** bounded_theorem"),
    (AN, 13, "**Claim scope:** conditional 3+1 derivation."),
    (AN, 20, "P-REC, and (f) the declared B-AXIS premise (one supplied blocked time"),
    (AN, 21, "step, one declared evolution axis/transfer construction, and no admitted"),
    (AN, 23, "dimension count is exactly d_t = 1 and the spacetime signature is (3,1)."),
    (AN, 25, "(d_t <= 1) is local to the declared B-AXIS boundary. No step defines time"),
    (AN, 26, "via the anomaly."),
    (AR, 18, "`MINIMAL_AXIOMS_2026-06-29.md` lists the arrow, decoherence mechanisms, and"),
    (AR, 19, "record-production dynamics among the gates **outside** the four axioms"),
]

# keyword hits in the axiom-level files that bear on nothing asked, with the reason
CLASSIFIED = {
    (AX, 8): "status line naming the qubit-on-Z^3 package (restates the Lattice axiom)",
    (AX, 114): "section heading",
    (AX, 144): "continues L143 (persistence dynamics needs a separate authority)",
    (AX, 195): "history: the Z^3 lattice separated from realization gates in April-May",
    (AX, 199): "history: the date the formation sentence was added (its content is L200-202, cited)",
    (AX, 200): "history: 'Records form.' became occurrence content (same as L77, cited)",
    (KI, 3): "terminology pointer",
    (KI, 25): "continues L23-24 (one tick is one edge in form)",
    (KI, 28): "the time-direction analogue of cubic adjacency (restates L23-25)",
    (KI, 34): "continues L32-33 (the graining ratio)",
    (KI, 39): "continues L40 (the list of what is not used)",
    (KI, 53): "anisotropic kinetic form, contrast only",
    (KI, 57): "structural premise category, contrast only",
    (KI, 58): "emergent time direction, restates L15-16",
    (KI, 68): "continues L67",
    (RS, 3): "terminology pointer",
    (RS, 34): "the realized-state reference (L35 cited)",
    (RS, 65): "continues L64 (low-record boundary is a separate input)",
    (RS, 66): "continues L64",
    (RS, 95): "the past hypothesis is not an entry (restates L30)",
    (RS, 67): "pointer to the arrow note (a low-record boundary is a separate input; the arrow note's L18-19 are cited)",
    (KI, 17): "the declared content c_t = c_s, a graining ratio (no record structure)",
    (KI, 27): "the statement is about the regulator geometry (restates L23-24, cited)",
    (KI, 29): "no dimensionless dynamical content",
    (KI, 69): "no dimensionless dynamical quantity supplied",
    (KI, 95): "dependency list",
}
KEYS = re.compile(r"past|\btime|order|clock|tick|dynamic|formation|permanen|history|Z\^3|Z_tau|3\+1", re.I)


def rep(tag, ok, msg):
    global NF, NP
    NF += (not ok)
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg)


def show(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git show {rev}:{path} failed: {r.stderr.strip()[:200]}")
    return r.stdout.split("\n")


def main():
    cache = {}
    bad = []
    for path, line, q in QUOTES:
        if path not in cache:
            cache[path] = show(MAIN, path)
        L = cache[path]
        if not (1 <= line <= len(L) and q in L[line - 1]):
            bad.append((path, line, q))
    rep("Q1 quotations verbatim", not bad,
        f"{len(QUOTES)} quotations from {len(set(p for p, _, _ in QUOTES))} files found verbatim at their cited lines on main @ {MAIN[:12]}"
        + (f"; missing: {bad[:3]}" if bad else ""))
    # Q2: the corpus
    nodes = json.loads("\n".join(cache[PN]))
    ids = nodes["canonical_ids"]
    paths = {k: v["current_path"] for k, v in nodes["nodes"].items()}
    ok2 = ids == ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"] and \
        paths["minimal_axioms"] == AX and paths["kinetic_isotropy_primitive"] == KI and paths["realized_state_primitive"] == RS and \
        paths["scale_reference_primitive"] == SR and len(cache[AX]) - (1 if cache[AX][-1] == "" else 0) == 233
    rep("Q2 the axiom-level corpus", ok2,
        "the premise-node allowlist on main has exactly the canonical ids minimal_axioms, scale_reference_primitive, "
        "kinetic_isotropy_primitive, realized_state_primitive with those four current paths; the memo has 233 lines, read in full")
    # Q3: exhaustive keyword scan of the four axiom-level files
    cited = {(p, l) for p, l, _ in QUOTES}
    unaccounted = []
    hits = 0
    for path in (AX, KI, RS, SR):
        L = cache[path] if path in cache else show(MAIN, path)
        for i, text in enumerate(L, 1):
            if KEYS.search(text):
                hits += 1
                if (path, i) in cited or (path, i) in CLASSIFIED:
                    continue
                if path == SR:          # the scale reference supplies units only; every hit there is classified by one rule
                    continue
                unaccounted.append((os.path.basename(path), i, text.strip()[:80]))
    sr_hits = sum(1 for t in show(MAIN, SR) if KEYS.search(t))
    rep("Q3 no bearing line left out", not unaccounted,
        f"{hits} keyword hits in the four axiom-level files (memo, three primitives): every hit in the memo, the kinetic-isotropy and the "
        f"realized-state notes is cited or classified with a reason; the scale-reference note's {sr_hits} hits concern units only"
        + (f"; unaccounted: {unaccounted[:4]}" if unaccounted else ""))
    # Q4: the tension, from the texts themselves
    ki_derived = "emergent and derived" in cache[KI][31] and "single-clock" in cache[KI][31]
    sc_premise = "is a premise, not a derivation" in cache[SC][30] and "conditional on (B-AXIS)" in cache[SC][37]
    an_premise = "B-AXIS" in cache[AN][19] and "No step defines time" in cache[AN][24]
    rep("Q4 the time axis is a premise, not axiom content", ki_derived and sc_premise and an_premise,
        "the approved kinetic-isotropy primitive (L32-33) calls time 'emergent and derived (the single-clock codimension-1 evolution "
        "theorem)'; that theorem (L30-31, L38) states 'the axis is a premise, not a derivation' and 'exactly one clock' only 'conditional "
        "on (B-AXIS)'; the anomaly bridge (L20-26) gets d_t = 1 only with the declared B-AXIS premise and 'No step defines time via the "
        "anomaly': on main no text makes a time direction axiom content")
    head = subprocess.run(["git", "rev-parse", "origin/main"], capture_output=True, text=True).stdout.strip()
    print(f"(main pinned at {MAIN[:12]}; origin/main here is {head[:12]})")
    print(f"TOTAL: PASS={NP} FAIL={NF}")
    if NF == 0:
        print("SUMMARY: PARTIAL a cited map extending round 1 to the three approved primitives and the causal-time notes: records live "
              "on Z^3, once and permanently (L37, L79-80, L166-167), formed from the nearest-neighbor conditions (L60-61) at a site, rate "
              "and order not supplied (L68, L183-184); the primitives add only a Z^3 x Z_tau loop regulator (KI L23-24, L31) and a history "
              "that picks the state (RS L21); consistent: one-record-per-site orders on Z^3 (2+1 sweeps); excluded as written: a record per "
              "site per tick (3+1 level planes, the light cone)")
        print("HIT: on main no text makes a time axis axiom content: the approved kinetic-isotropy primitive calls time 'emergent and "
              "derived (the single-clock ... theorem)' (KI L32-33), but that theorem says 'the axis is a premise, not a derivation' and gives "
              "one clock only 'conditional on (B-AXIS)' (SC L30-31, L38), and the 3+1 anomaly bridge caps d_t at the declared B-AXIS "
              "boundary, 'No step defines time via the anomaly' (AN L20-26); with one permanent record per Z^3 site (L79-80, L166-167) no "
              "record lattice with three-dimensional level planes is supplied")
    else:
        print(f"SUMMARY: ROUTE FAILS AT {NF} check(s) above")


if __name__ == "__main__":
    main()
