#!/usr/bin/env python3
"""Independent referee for axioms-and-the-event-lattice attempt a1.

Every cited sentence is read from the pinned main commit, not from the
working tree and not from the author's script.
"""

import json
import subprocess

PIN = "abb98a122eb7acefd37b10ae89dd33c500a9c353"
FAILS = []

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

QUOTES = [
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
    (AX, 89, "primitive registration, before use as a premise. A choice not fixed by the"),
    (AX, 90, "supplied structure remains a named conditional or open dependency."),
    (AX, 92, "A state is a configuration of records."),
    (AX, 116, "Admissibility is not a dynamics axiom."),
    (AX, 122, "carrier, define a time metric, or provide a record-production process or"),
    (AX, 123, "physical persistence dynamics."),
    (AX, 183, "mechanisms, and the remaining formation rules (the distribution's form and"),
    (AX, 184, "values, at which site, and at what rate);"),
    (AX, 185, "- arrow, record-production dynamics, physical persistence dynamics, time metric,"),
    (KIN, 15, "The framework takes one structural graining fact: the emergent evolution tick is"),
    (KIN, 23, "equivalently the Euclidean regulator block `Z^3 x Z_tau` on which loops are"),
    (KIN, 31, "is not a fourth spatial dimension, not a new dynamics, and not a re-axiomatization"),
    (KIN, 32, "of time: the framework's time remains emergent and derived (the single-clock"),
    (KIN, 67, "- It does not re-axiomatize time. The emergent single-clock evolution remains"),
    (RS, 21, "The laws do not pick the state; the world does, among the states the laws"),
    (POL, 34, "- Citing policy text as a premise or interpretive authority — including"),
    (POL, 59, "If a physics-loop or science worker reaches \"we need an extra axiom to close"),
    (POL, 63, "2. Record the proposed axiom as an explicit science-level decision"),
    (POL, 76, "Review-loop, physics-loop, audit-loop, and audit-pipeline consumers must not"),
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
]

LENGTHS = {
    AX: 233,
    POL: 818,
    KIN: 99,
    SC: 57,
    RS: 110,
    ARR: 153,
    CLK: 714,
    ANO: 470,
    APP: 122,
}


def require(cond, msg):
    print(("ok: " if cond else "FAIL: ") + msg)
    if not cond:
        FAILS.append(msg)


def blob(path):
    r = subprocess.run(["git", "show", f"{PIN}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return r.stdout.split("\n")


def main():
    cache = {}
    for path, line, needle in QUOTES:
        if path not in cache:
            cache[path] = blob(path)
        lines = cache[path]
        ok = lines is not None and 1 <= line <= len(lines) and needle in lines[line - 1]
        require(ok, f"{path}:{line} contains the cited sentence")
    for path, n in LENGTHS.items():
        lines = cache.get(path) or blob(path)
        # git show keeps a trailing empty split from the final newline
        count = len(lines) - (1 if lines and lines[-1] == "" else 0)
        require(count == n, f"{path} has {count} lines at {PIN[:12]} (attempt says {n})")
    reg_lines = blob("docs/audit/data/axiom_premise_nodes.json")
    reg = json.loads("\n".join(reg_lines))
    ids = reg.get("canonical_ids")
    require(ids == [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ], f"canonical premise ids are {ids}")
    # The exclusion in S2 is the permanence sentence, already checked at AX:80.
    ax = cache[AX]
    require("never carries more than one record" in ax[79],
            "one record per site is the sentence that excludes a second record at the same site")
    print("TOTAL FAIL =", len(FAILS))
    if FAILS:
        print("SUMMARY: fails at a citation - " + "; ".join(FAILS[:6]))
        return 1
    print(
        "HIT: confirmed - at main abb98a12 the axiom text places sites at the points of Z^3 and "
        "says a site never carries more than one record. Every one-record-per-site formation "
        "order, including the level order x1+x2+x3, is a named conditional. A structure that "
        "writes a new record at the same site on a later tick contradicts that sentence. "
        "Z^3 x Z_tau in the kinetic-isotropy note is a loop regulator, not a lattice of record sites."
    )
    print(
        "SUMMARY: confirmed - the citation map matches the pinned commit. The text does not "
        "choose among one-record orders, and it excludes per-tick records at one site."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
