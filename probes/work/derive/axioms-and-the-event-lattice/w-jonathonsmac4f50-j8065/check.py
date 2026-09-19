#!/usr/bin/env python3
"""axioms-and-the-event-lattice, attempt a1 (w-jonathonsmac4f50-j8065): every quoted line of ATTEMPT.md exists verbatim at the cited path and
line of main at the pinned commit abb98a122eb7acefd37b10ae89dd33c500a9c353 (origin/main when read); the files read in full have the stated
lengths; the premise registry's canonical ids are the four read.

 Q1  the axiom memo: the Lattice, Admissibility, Record sentences and the Qualification, Relation-to-dynamics and Open-gates lines quoted
 Q2  the approved primitives (kinetic isotropy, realized state) and the premise registry's canonical_ids
 Q3  the policy's process lines (policy text carries no premise weight; the workflow for a proposed axiom; owner approval)
 Q4  the downstream time lane: single-clock (B-AXIS premise; slices {t} x Z^3), anomaly-forces-time (conditional 3+1; no step defines time via
     the anomaly), arrow (direction from record formation), append-only history order, block 01's formation order (the axioms supply no order)
 R1  lengths of the files read in full: memo 233, policy 818, kinetic-isotropy 99, scale-reference 57, realized-state 110, arrow 153 lines
"""
import json
import subprocess
import sys

PIN = "abb98a122eb7acefd37b10ae89dd33c500a9c353"
FAILS = []


def check(label, ok, detail):
    print(f"{'ok  ' if ok else 'FAIL'} {label}: {detail}")
    if not ok:
        FAILS.append(label)


def show(path):
    for ref in (PIN, "origin/main"):
        r = subprocess.run(["git", "show", f"{ref}:{path}"], capture_output=True, text=True)
        if r.returncode == 0:
            return r.stdout.split("\n"), ref
    return None, None


AX = "docs/MINIMAL_AXIOMS_2026-06-29.md"
POL = "docs/audit/AXIOM_MINIMALITY_POLICY.md"
KIN = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
RS = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SC = "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
CLK = "docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
ANO = "docs/ANOMALY_FORCES_TIME_THEOREM.md"
ARR = "docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md"
APP = "docs/PAST_HYPOTHESIS_EXISTENCE_REDUCTION_APPEND_ONLY_WELL_FOUNDEDNESS_BOUNDED_THEOREM_NOTE_2026-06-11.md"
B01 = "docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md"

QUOTES = {
    "Q1": [
        (AX, 37, "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor"),
        (AX, 38, "adjacency, standard translations, and proper cubic rotations about each site."),
        (AX, 40, "No site is privileged. Sites are distinguished by the supplied lattice"),
        (AX, 57, "There is one fixed nearest-neighbor admissibility rule, covariant under lattice"),
        (AX, 60, "For each site, the probability distribution over the possibilities is"),
        (AX, 61, "determined by, and varies with, the nearest-neighbor conditions."),
        (AX, 67, "distribution concerns which possibility a forming record locks, conditional"),
        (AX, 68, "on formation at that site; it does not supply the formation site, probability,"),
        (AX, 77, "Records form."),
        (AX, 79, "When present, a record locks exactly one admissible local possibility. A"),
        (AX, 80, "site never carries more than one record; records are permanent."),
        (AX, 82, "Only records are readable. A readout value is determined by record content"),
        (AX, 89, "primitive registration, before use as a premise. A choice not fixed by the"),
        (AX, 90, "supplied structure remains a named conditional or open dependency."),
        (AX, 92, "A state is a configuration of records."),
        (AX, 116, "Admissibility is not a dynamics axiom."),
        (AX, 122, "carrier, define a time metric, or provide a record-production process or"),
        (AX, 123, "physical persistence dynamics."),
        (AX, 183, "mechanisms, and the remaining formation rules (the distribution's form and"),
        (AX, 184, "values, at which site, and at what rate);"),
        (AX, 185, "- arrow, record-production dynamics, physical persistence dynamics, time metric,"),
    ],
    "Q2": [
        (KIN, 15, "The framework takes one structural graining fact: the emergent evolution tick is"),
        (KIN, 23, "equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are"),
        (KIN, 31, "is not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization"),
        (KIN, 32, "of time: the framework's time remains emergent and derived (the single-clock"),
        (KIN, 67, "- It does not re-axiomatize time. The emergent single-clock evolution remains"),
        (RS, 21, "The laws do not pick the state; the world does, among the states the laws"),
    ],
    "Q3": [
        (POL, 34, "- Citing policy text as a premise or interpretive authority — including"),
        (POL, 59, "If a physics-loop or science worker reaches \"we need an extra axiom to close"),
        (POL, 63, "2. Record the proposed axiom as an explicit science-level decision"),
        (POL, 76, "Review-loop, physics-loop, audit-loop, and audit-pipeline consumers must not"),
    ],
    "Q4": [
        (CLK, 21, "each lattice time slice `Σ_t = {t} × Z^3` is a"),
        (CLK, 30, "(S3′) **the axis"),
        (CLK, 31, "is a premise, not a derivation**"),
        (ANO, 13, "**Claim scope:** conditional 3+1 derivation."),
        (ANO, 23, "dimension count is exactly d_t = 1 and the spacetime signature is (3,1)."),
        (ANO, 25, "No step defines time"),
        (ANO, 26, "via the anomaly."),
        (ARR, 62, "derives the arrow's **direction** = \"away from the low-record boundary\"."),
        (APP, 30, "The history order throughout is **supplied by the record history**"),
        (B01, 139, "FORMATION law of a rule for a formation order `σ = (x_1, …, x_n)` under"),
        (B01, 141, "The axioms supply no order; every"),
    ],
}


def main():
    for tag, items in QUOTES.items():
        ok = True
        bad = []
        refs = set()
        for path, line, needle in items:
            lines, ref = show(path)
            refs.add(ref)
            if lines is None or line > len(lines) or needle not in lines[line - 1]:
                ok = False
                bad.append(f"{path}:{line}")
        check(tag, ok, f"{len(items)} quoted lines present verbatim at the cited path:line (ref {'/'.join(sorted(r[:10] for r in refs if r))})"
              + (f"; missing: {bad}" if bad else ""))
    # registry
    lines, ref = show("docs/audit/data/axiom_premise_nodes.json")
    reg = json.loads("\n".join(lines))
    ok = reg.get("canonical_ids") == ["minimal_axioms", "scale_reference_primitive", "kinetic_isotropy_primitive", "realized_state_primitive"]
    ok &= reg["nodes"]["minimal_axioms"]["current_path"] == AX
    check("Q2b", ok, f"docs/audit/data/axiom_premise_nodes.json canonical_ids = {reg.get('canonical_ids')} with minimal_axioms -> {AX}")
    # R1: lengths of the files read in full
    want = {AX: 233, POL: 818, KIN: 99, SC: 57, RS: 110, ARR: 153}
    got = {}
    ok = True
    for p, n in want.items():
        lines, _ = show(p)
        m = len(lines) - (1 if lines and lines[-1] == "" else 0)
        got[p.split("/")[-1]] = m
        ok &= m == n
    check("R1", ok, f"line counts of the files read in full: {got}")
    print("=" * 80)
    if FAILS:
        print(f"SUMMARY: ROUTE FAILS AT {FAILS[0]} ({FAILS})")
        return 0
    core = ("map of the axioms (main @ abb98a12) on the past of a record: sites are the points of Z^3 (Lattice L37) and a site never carries more "
            "than one record, permanently (Record L79-80); a forming record's distribution is fixed by the nearest-neighbor conditions (Admissibility "
            "L60-61, 'conditional on formation at that site', L67-68); the formation site, rate and order are not supplied (L68, L183-184; a choice "
            "not fixed remains a named conditional, L89-90); no time metric, arrow or record-production dynamics (L122-123, L185); the approved "
            "kinetic-isotropy primitive's Z^3 x Z_tau is a loop regulator with time 'emergent and derived' (L23, L31-32). Hence every one-record-per-site "
            "formation order on Z^3 (the backward 2+1 level order among them) is consistent, and every structure that forms a record at each tick of "
            "a site (the 3+1 event lattice with three-dimensional level planes, the symmetric light-cone past) is excluded as written by L37 + L80; "
            "admitting it needs a record-per-site-per-tick clause replacing L80's uniqueness and a supplied tick, an owner decision (policy L59-66, L76)")
    print("SUMMARY: PARTIAL " + core)
    print("HIT: " + core)
    return 0


if __name__ == "__main__":
    sys.exit(main())
