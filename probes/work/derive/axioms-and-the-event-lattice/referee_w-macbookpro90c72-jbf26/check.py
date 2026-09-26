#!/usr/bin/env python3
"""Independent citation check for J:derive:axioms-and-the-event-lattice:a2.

Reads main by git show at PIN. Does not import the author's check.
The eight cited files are also required to match origin/main blob-for-blob.
"""
import json
import re
import subprocess

PIN = "b8d0017208a2c26f5938c618dc57f745293fe777"
AX = "docs/MINIMAL_AXIOMS_2026-06-29.md"
KI = "docs/KINETIC_ISOTROPY_PRIMITIVE_NOTE_2026-06-09.md"
RS = "docs/REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md"
SR = "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md"
PN = "docs/audit/data/axiom_premise_nodes.json"
SC = "docs/AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
AN = "docs/ANOMALY_FORCES_TIME_THEOREM.md"
AR = "docs/ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md"

QUOTES = [
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
    (PN, 5, '"minimal_axioms",'),
    (PN, 6, '"scale_reference_primitive",'),
    (PN, 7, '"kinetic_isotropy_primitive",'),
    (PN, 8, '"realized_state_primitive"'),
    (KI, 6, "**Date:** 2026-06-09"),
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
    (KI, 68, "derived; this primitive normalizes only the one graining ratio"),
    (RS, 21, "The laws do not pick the state; the world does, among the states the laws"),
    (RS, 22, "permit."),
    (RS, 30, "The past hypothesis is a separate, stronger input."),
    (RS, 35, "supplied by the physical history."),
    (RS, 64, "- It does not assert any special boundary condition on the realized history."),
    (SR, 19, "This is a units conversion, not a physics axiom."),
    (SC, 3, "**Date:** 2026-05-03 (hostile science-fix re-scope 2026-06-11;"),
    (SC, 7, "unit split 2026-06-17; see §0)"),
    (SC, 8, "**Type:** bounded_theorem"),
    (SC, 21, "Hilbert space; (S2′) each lattice time slice `Σ_t = {t} × Z^3` is a"),
    (SC, 22, "codimension-1 Cauchy surface: the equal-time local algebra is the"),
    (SC, 23, "mutually commuting tensor product of per-site one-qubit `M_2(C)` Pauli"),
    (SC, 30, "(S3′) **the axis"),
    (SC, 31, "is a premise, not a derivation**"),
    (SC, 38, '"exactly one clock" conclusion holds conditional on (B-AXIS)'),
    (AN, 1, "# Anomaly-Cancellation Consistency Bridge for 3+1 Spacetime"),
    (AN, 8, "**Type:** bounded_theorem"),
    (AN, 13, "**Claim scope:** conditional 3+1 derivation."),
    (AN, 20, "P-REC, and (f) the declared B-AXIS premise (one supplied blocked time"),
    (AN, 21, "step, one declared evolution axis/transfer construction, and no admitted"),
    (AN, 23, "dimension count is exactly d_t = 1 and the spacetime signature is (3,1)."),
    (AN, 24, "The lower bound (d_t odd, hence d_t >= 1) is computed; the upper bound"),
    (AN, 25, "(d_t <= 1) is local to the declared B-AXIS boundary. No step defines time"),
    (AN, 26, "via the anomaly."),
    (AR, 18, "`MINIMAL_AXIOMS_2026-06-29.md` lists the arrow, decoherence mechanisms, and"),
    (AR, 19, "record-production dynamics among the gates **outside** the four axioms"),
]

# Keyword hits in AX/KI/RS that are not themselves a quotation above.
CLASSIFIED = {
    (AX, 8): "status line naming the qubit-on-Z^3 memo",
    (AX, 114): "section heading Relation To Dynamics",
    (AX, 144): "continues L143: persistence dynamics needs a separate authority",
    (AX, 195): "history of separating the Z^3 lattice from realization gates",
    (AX, 199): "history of the date the formation sentence was appended; the sentence is L77",
    (KI, 17): "states the graining ratio c_t = c_s; no record structure",
    (KI, 25): "continues L23-24: one tick is one edge in form",
    (KI, 27): "the regulator's time-direction analogue of cubic adjacency",
    (KI, 29): "no dimensionless dynamical content",
    (KI, 34): "continues L32-33: the graining ratio of that emergent time",
    (KI, 39): "continues the list at L40 of inputs not used to derive c_t = c_s",
    (KI, 58): "restates the emergent time direction of the graining",
    (KI, 69): "no dimensionless dynamical quantity",
    (KI, 95): "dependency sentence: cubic adjacency paralleled in the time direction",
    (RS, 67): "pointer to the arrow note; a low-record boundary is a separate input",
    (RS, 95): "restates L30: the past hypothesis is not an entry of this primitive",
}

KEYS = re.compile(
    r"past|\btime|order|clock|tick|dynamic|formation|permanen|history|Z\^3|Z_tau|3\+1",
    re.I,
)
FILES = (AX, KI, RS, SR, PN, SC, AN, AR)
NF = 0
NP = 0


def rep(tag, ok, msg):
    global NF, NP
    NF += not ok
    NP += bool(ok)
    print(("PASS " if ok else "FAIL ") + tag + ": " + msg, flush=True)


def show(rev, path):
    r = subprocess.run(["git", "show", f"{rev}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(f"git show {rev}:{path} failed: {r.stderr.strip()[:200]}")
    return r.stdout.split("\n")


def blob(rev, path):
    r = subprocess.run(["git", "rev-parse", f"{rev}:{path}"], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip()[:200])
    return r.stdout.strip()


def main():
    origin = subprocess.run(
        ["git", "rev-parse", "origin/main"], capture_output=True, text=True
    ).stdout.strip()
    same = all(blob(PIN, p) == blob(origin, p) for p in FILES)
    rep(
        "Q0 pin matches origin/main",
        same,
        f"eight cited files are the same blobs at {PIN[:12]} and origin/main {origin[:12]}",
    )
    cache = {p: show(PIN, p) for p in FILES}
    bad = []
    for path, line, quote in QUOTES:
        lines = cache[path]
        if not (1 <= line <= len(lines) and quote in lines[line - 1]):
            bad.append((path, line, quote[:60]))
    rep(
        "Q1 quotations",
        not bad,
        f"{len(QUOTES)} substrings sit on the cited lines at {PIN[:12]}"
        + (f"; missing {bad[:3]}" if bad else ""),
    )
    nodes = json.loads("\n".join(cache[PN]))
    ids = nodes["canonical_ids"]
    paths = {k: v["current_path"] for k, v in nodes["nodes"].items()}
    ax_n = len(cache[AX]) - (1 if cache[AX][-1] == "" else 0)
    ok_ids = ids == [
        "minimal_axioms",
        "scale_reference_primitive",
        "kinetic_isotropy_primitive",
        "realized_state_primitive",
    ]
    ok_paths = (
        paths["minimal_axioms"] == AX
        and paths["scale_reference_primitive"] == SR
        and paths["kinetic_isotropy_primitive"] == KI
        and paths["realized_state_primitive"] == RS
        and ax_n == 233
    )
    rep(
        "Q2 premise corpus",
        ok_ids and ok_paths,
        "canonical ids are the four premises, paths match, memo is 233 lines",
    )
    cited = {(p, n) for p, n, _ in QUOTES}
    unaccounted = []
    hits = 0
    for path in (AX, KI, RS, SR):
        for i, text in enumerate(cache[path], 1):
            if not KEYS.search(text):
                continue
            hits += 1
            if path == SR or (path, i) in cited or (path, i) in CLASSIFIED:
                continue
            unaccounted.append((path.split("/")[-1], i, text.strip()[:70]))
    sr_hits = sum(1 for t in cache[SR] if KEYS.search(t))
    rep(
        "Q3 keyword scan",
        not unaccounted and sr_hits == 0 and hits == 39,
        f"{hits} keyword hits in the four premise files; scale-reference contributes {sr_hits}; "
        "every memo, kinetic-isotropy, and realized-state hit is quoted or classified"
        + (f"; unaccounted {unaccounted[:4]}" if unaccounted else ""),
    )
    ki = cache[KI]
    sc = cache[SC]
    an = cache[AN]
    tension = (
        "emergent and derived" in ki[31]
        and "single-clock" in ki[31]
        and "remains" in ki[66]
        and "derived" in ki[67]
        and "is a premise, not a derivation" in sc[30]
        and "conditional on (B-AXIS)" in sc[37]
        and "B-AXIS" in an[19]
        and "d_t >= 1" in an[23]
        and "No step defines time" in an[24]
        and "via the anomaly." in an[25]
    )
    rep(
        "Q4 time axis is a declared premise",
        tension,
        "KI L32-33 and L67-68 call the single-clock evolution emergent and derived; "
        "SC L31 and L38 make the axis a premise and one clock conditional on B-AXIS; "
        "AN L24-26 computes d_t >= 1 and caps d_t <= 1 at B-AXIS, and no step defines time via the anomaly",
    )
    one_record = (
        "never carries more than one record" in cache[AX][79]
        and "records are permanent" in cache[AX][79]
        and "Z^3" in cache[AX][36]
        and "not a fourth spatial dimension" in ki[30]
    )
    rep(
        "Q5 one record on Z^3",
        one_record,
        "AX L37 sites are Z^3; AX L80 one permanent record per site; "
        "KI L31 the regulator block is not a fourth spatial dimension",
    )
    print(f"TOTAL: PASS={NP} FAIL={NF}", flush=True)
    if NF == 0:
        print(
            "SUMMARY: PARTIAL cited map at main "
            f"{PIN[:12]} (eight files match origin/main {origin[:12]}): "
            "one permanent record per Z^3 site; formation site, rate, and order are not supplied; "
            "Z^3 x Z_tau is a loop regulator; a time axis enters as the declared premise B-AXIS, not as axiom content. "
            "A record per site per tick is excluded. A simultaneous subset of Z^3 may be three-dimensional; "
            "that is one formation, not a later record at the same site.",
            flush=True,
        )
        print(
            "HIT: confirmed - on main no axiom-level text makes a time axis axiom content. "
            "The kinetic-isotropy primitive calls time emergent and derived by the single-clock theorem "
            "(KI L32-33, L67-68), while that theorem says the axis is a premise, not a derivation, "
            "and one clock holds only conditional on B-AXIS (SC L30-31, L38). "
            "The anomaly bridge gives d_t = 1 only with the declared B-AXIS premise and says no step defines time "
            "via the anomaly (AN L20-26). One permanent record per Z^3 site (AX L37, L79-80, L166-167) "
            "excludes a record lattice that writes the same site again on a later tick.",
            flush=True,
        )
    else:
        print(f"SUMMARY: fails at {NF} check(s) above", flush=True)


if __name__ == "__main__":
    main()
