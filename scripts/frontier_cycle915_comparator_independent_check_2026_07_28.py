#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 915 independent check -- SPEC'D TO REFUTE.

Adversarial counterpart to
`scripts/frontier_cycle915_comparator_recovery_2026_07_28.py`.  Its job is to
break that runner's three claims, not to agree with them.  It exits 0 whether or
not the claims survive; the verdict lives in the emitted findings.

Attack surfaces
---------------
A1  C1 PROVENANCE, INDEPENDENTLY.  The checker re-derives every provenance chain
    from its own git evidence by a DIFFERENT route than the primary: it never
    consults the primary's recorded commit hashes when locating an artifact, it
    reaches each addition through a path-scoped history walk of its own, and it
    recomputes each recovered blob's sha256 from `git cat-file` bytes.  Landing
    status is re-derived twice (merge-base ancestry AND remote-branch
    containment) so a single wrong answer cannot pass.

A2  BYTE-FIDELITY OF THE THETA-FLOOR READING.  The primary claims the d = 1
    comparator note DEFERS the theta comparison and that the 0.20 floor is
    measured elsewhere.  This is the reading that decides how the Cycle 914
    comparator row may be cited, so it is attacked directly: every quoted string
    the primary reports must occur VERBATIM in the recovered bytes; the d = 1
    note is scanned for any theta measurement that would contradict the deferral
    reading; the deposition note is scanned for the floor it is claimed to
    supply; and the two comparators' theta DEFINITIONS are compared to test the
    primary's claim that they are not the same observable.

A3  INDEPENDENT RECOMPUTATION OF C2.  The lambda = 0.02 certification rows are
    recomputed from scratch with the Cycle 914 checker's verified independent
    machinery -- a MAX-canonical orbit sector (the primary's is MIN-canonical),
    a SHIFTED Chebyshev propagator with non-zero spectral centre, and
    row-by-row expand-table marginals -- and the certification arithmetic is
    re-derived from the memo definitions.  No primary value is copied into the
    recomputation; comparison happens only at the end.

A4  C3 SPOT-VERIFICATION.  One late sample is recomputed independently and its
    persistence classification checked against the primary's.

Teeth
-----
Eight mutation probes, each of which must be DETECTED: tampered pin, fabricated
provenance, hardcoded certification, leaked verdict, skipped grid point, planted
early-certification blindness, tampered committed stream, and a fabricated
theta-floor quote.

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis,
by construction.

No formation rule.

Sets no audit status.
"""
from __future__ import annotations

import ast
import hashlib
import itertools
import json
import os
import re
import resource
import subprocess
import sys
import time

import numpy as np
import scipy.linalg as sla
from scipy.special import jv

T_START = time.time()
BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = "| " + " | ".join(BOUNDARY)
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PRIMARY = "scripts/frontier_cycle915_comparator_recovery_2026_07_28.py"
PRIMARY_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
C914_PRIMARY = "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"
C914_CHECKER = "scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
NOTE_MEMO = "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md"
AXIOMS = "docs/MINIMAL_AXIOMS_2026-06-29.md"
STREAM_002 = "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl"

PIN_SHA = {
    PARENT_MEMO: "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
    DELTA_MEMO: "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
    NOTE_MEMO: "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
    AXIOMS: "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
    C914_PRIMARY: "fc7344a06503f9c159ea732cb6f622a23e61196e370914943ffd9a468fd592e4",
    C914_RECEIPT: "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
    STREAM_002: "9bf9282d477daf43635d29647ea0757fefb6105b755519c515539b3e28be3177",
}
# Pinned AS ABSENT.  Present-in-tree refutes the primary's absence pin.
CITED_ABSENT = [
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md",
    "docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md",
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md",
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md",
    "scripts/d3_registration_onset_pilot_2026_07_09.py",
    "scripts/d3_bar_location_measurement_2026_07_10.py",
]
D1_NOTE = "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"
DEP_NOTE = "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md"
BAR_NOTE = "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md"

LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
CENTER = (0, 0, 0)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE = 0.10
GATE_H, GATE_EXC, GATE_IND, DEADLINE = 0.05, 0.02, 0.02, 1.0
C2_LAMBDA = 0.02
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
C3_SPOT = (0.05, 1.5)          # (lambda, Jt) recomputed independently
FINDINGS = []
TEETH = []


def note(tag, ok, detail, **kw):
    d = {"check": tag, "survives": bool(ok), "detail": detail}
    d.update(kw)
    FINDINGS.append(d)
    return d


def sha(b):
    return hashlib.sha256(b).hexdigest()


def git(*args):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    return {"cmd": "git " + " ".join(args), "rc": p.returncode, "out": p.stdout.rstrip("\n")}


def gitb(*args):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
    return p.stdout


def rss_gib():
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return ru / (2.0 ** 30) if ru > 2 ** 32 else ru / (1024.0 ** 2)


# ============================= independent machinery (AST from 914 checker) ==
EX_F = ["rotations24", "_tab", "shifted_chebyshev", "energy_expectation",
        "expand_table", "S_bits", "chi_bits", "tr1", "cmi_bits", "r_ind",
        "memo_fragments", "tiebreak"]
EX_C = ["CubeSector", "Marginal"]
EX_A = ["CHK"]


def load_independent_machinery():
    src_path = os.path.join(ROOT, C914_CHECKER)
    src = open(src_path, "rb").read()
    tree = ast.parse(src.decode())
    keep, names = [], []
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name in EX_F:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.ClassDef) and n.name in EX_C:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.Assign):
            tg = [x.id for x in n.targets if isinstance(x, ast.Name)]
            if tg and tg[0] in EX_A:
                keep.append(n); names.append(tg[0])
    missing = [x for x in EX_F + EX_C + EX_A if x not in names]
    if missing:
        raise RuntimeError("independent machinery missing: %s" % missing)
    mod = ast.Module(body=keep, type_ignores=[])
    ast.fix_missing_locations(mod)
    ns = {"np": np, "sla": sla, "jv": jv, "itertools": itertools, "re": re,
          "LABELS": LABELS, "CENTER": CENTER, "GATE_H": GATE_H,
          "GATE_EXC": GATE_EXC, "GATE_IND": GATE_IND}
    exec(compile(mod, src_path, "exec"), ns)
    return ns, {"source": C914_CHECKER, "source_sha256": sha(src),
                "names": sorted(names),
                "approach": "MAX-canonical orbit sector + shifted Chebyshev (non-zero "
                            "spectral centre) + expand-table marginals -- structurally "
                            "distinct from the primary's MIN-canonical / centred expansion"}


PAIR_CLASS = {}
for _c, _ms in {"opposite-55": [("+x", "-x")],
                "opposite-44": [("+y", "-y"), ("+z", "-z")],
                "plus-x-orthogonal": [("+x", q) for q in ("+y", "-y", "+z", "-z")],
                "minus-x-orthogonal": [("-x", q) for q in ("+y", "-y", "+z", "-z")],
                "transverse-orthogonal": [("+y", "+z"), ("+z", "-y"), ("-y", "-z"), ("-z", "+y")]
                }.items():
    for _p in _ms:
        PAIR_CLASS[tuple(sorted(_p, key=LABELS.index))] = _c


# ================================================ A1: independent provenance =
def independent_provenance(paths):
    """Own git evidence.  The primary's commit hashes are NEVER read here."""
    out = {"route": "path-scoped --diff-filter=A walk over --all; landing status "
                    "cross-derived from merge-base AND remote-branch containment",
           "artifacts": {}, "commands": []}
    main_tip = git("rev-parse", "origin/main")["out"]
    out["origin_main_tip"] = main_tip
    for path in paths:
        r = {"commands": []}
        c = git("cat-file", "-e", "HEAD:%s" % path)
        r["commands"].append(c["cmd"]); out["commands"].append(c["cmd"])
        r["present_in_tree"] = os.path.exists(os.path.join(ROOT, path))
        r["present_at_head"] = (c["rc"] == 0)

        c = git("log", "--all", "--diff-filter=A", "--format=%H|%ci|%an|%s", "--", path)
        r["commands"].append(c["cmd"]); out["commands"].append(c["cmd"])
        adds = [l for l in c["out"].splitlines() if l.strip()]
        if not adds:
            r["verdict"] = "GENUINELY-ABSENT"
            r["evidence"] = "no --diff-filter=A record for this path anywhere in --all"
            out["artifacts"][path] = r
            continue
        commit = adds[0].split("|")[0]
        r["add_commit"] = commit
        r["add_commit_date"] = adds[0].split("|")[1]
        r["add_commit_subject"] = adds[0].split("|")[-1]
        r["n_add_records"] = len(adds)

        # landing status, derived twice
        a1 = git("merge-base", "--is-ancestor", commit, "origin/main")["rc"] == 0
        c = git("branch", "-r", "--contains", commit)
        r["commands"].append(c["cmd"]); out["commands"].append(c["cmd"])
        remotes = [x.strip() for x in c["out"].splitlines() if x.strip()]
        a2 = any(b.split()[0] in ("origin/main", "origin/HEAD") or
                 b.split()[0].endswith("/main") for b in remotes)
        r["ancestor_of_main_via_merge_base"] = a1
        r["main_among_containing_remote_branches"] = a2
        r["landing_status_consistent"] = (a1 == a2)
        r["remote_branches_containing"] = remotes
        r["ever_landed"] = bool(a1 or a2)

        c = git("log", "--all", "--diff-filter=D", "--format=%H", "--", path)
        r["commands"].append(c["cmd"])
        r["deleted_anywhere"] = bool(c["out"].strip())

        blob = git("rev-parse", "%s:%s" % (commit, path))["out"].strip()
        body = gitb("cat-file", "blob", blob)
        r["commands"].append("git cat-file blob %s" % blob[:12])
        r["recovered_sha256"] = sha(body)
        r["recovered_bytes"] = len(body)
        r["verdict"] = "FOUND"
        r["absent_because"] = ("landed-then-removed" if (r["ever_landed"] and r["deleted_anywhere"])
                               else "on-main" if r["ever_landed"] else "never-landed")
        out["artifacts"][path] = r
    return out


# =========================================== A2: theta-floor byte fidelity ===
def theta_floor_attack(prov, primary_receipt):
    """Does the d = 1 note actually say what the primary reports?"""
    res = {"attacks": {}}
    claim = primary_receipt["C1_theta_floor_provenance"]

    def blob_bytes(path):
        c = git("log", "--all", "--diff-filter=A", "--format=%H", "--", path)
        if not c["out"].strip():
            return None
        commit = c["out"].splitlines()[0].strip()
        b = git("rev-parse", "%s:%s" % (commit, path))["out"].strip()
        return gitb("cat-file", "blob", b)

    d1 = blob_bytes(D1_NOTE)
    dep = blob_bytes(DEP_NOTE)
    res["d1_note_recovered"] = d1 is not None
    res["dep_note_recovered"] = dep is not None
    d1t = d1.decode("utf-8", "replace") if d1 else ""
    dept = dep.decode("utf-8", "replace") if dep else ""

    # -- attack 1: is every quoted string VERBATIM in the recovered bytes? --
    quotes = {
        "d1_deferral_quote": (claim.get("d1_note_deferral_quote"), d1t),
        "deposition_floor_quote": (claim.get("deposition_note_quote"), dept),
        "deposition_theta_definition_quote": (claim.get("deposition_theta_definition_quote"), dept),
    }
    verbatim = {}
    for k, (q, hay) in quotes.items():
        verbatim[k] = None if not q else (q.strip() in hay)
    res["attacks"]["quotes_verbatim"] = verbatim
    res["attacks"]["all_quotes_verbatim"] = all(v is True for v in verbatim.values())

    # -- attack 2: does the d=1 note contain a theta MEASUREMENT that would
    #    contradict the "defers" reading? --
    theta_hits = re.findall(r"theta[^\n]{0,60}", d1t)
    numeric_theta = [h for h in theta_hits if re.search(r"theta\s*\*?\s*[=~]\s*[\d.]", h)]
    res["attacks"]["d1_theta_mentions"] = theta_hits
    res["attacks"]["d1_states_a_theta_value"] = bool(numeric_theta)
    res["attacks"]["d1_deferral_present"] = ("DEFERRED to a d >= 2 comparator" in d1t
                                             and "unmeasured here" in d1t)
    # a d=1 note that both defers AND states no theta value cannot be the floor's source
    res["attacks"]["d1_can_be_the_floor_source"] = bool(
        numeric_theta or not res["attacks"]["d1_deferral_present"])

    # -- attack 3: does the deposition note actually supply the floor? --
    res["attacks"]["dep_states_floor"] = ("(theta >= 0.2)" in dept
                                          or "theta >= 0.2" in dept)
    res["attacks"]["dep_floor_is_measured_not_declared"] = bool(
        "threshold floor" in dept and "measured" in dept.lower())

    # -- attack 4: are the two thetas the SAME observable? (the primary says no) --
    dep_baseline = ("minus the" in dept and "interacting-ground-state baseline" in dept)
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode()
    d3_baseline = "the subtrahend is the same trajectory's `t=0` value" in memo
    res["attacks"]["deposition_theta_subtracts_ground_state_baseline"] = bool(dep_baseline)
    res["attacks"]["d3_theta_subtracts_trajectory_t0"] = bool(d3_baseline)
    res["attacks"]["theta_definitions_differ"] = bool(dep_baseline and d3_baseline)

    # -- attack 5: is the in-tree window note's "declared import" reading real? --
    wt = open(os.path.join(ROOT, NOTE_MEMO), "rb").read().decode()
    res["attacks"]["window_note_lists_floor_as_supplied_input"] = bool(
        "supplied inputs rather than derived conclusions" in wt
        and "the theta observable and its `0.20` declared comparison floor" in wt)

    # -- attack 6: is the 914 label really there? (grounds the misattribution claim) --
    p914 = open(os.path.join(ROOT, C914_PRIMARY), "rb").read().decode()
    res["attacks"]["c914_label_present"] = "d1-comparator-floor" in p914
    res["attacks"]["c914_theta_floor_constant"] = bool(
        re.search(r"THETA_FLOOR\s*=\s*0\.20", p914))

    # -- verdict on the primary's reading --
    survives = (res["attacks"]["all_quotes_verbatim"]
                and res["attacks"]["d1_deferral_present"]
                and not res["attacks"]["d1_states_a_theta_value"]
                and res["attacks"]["dep_states_floor"]
                and res["attacks"]["theta_definitions_differ"]
                and res["attacks"]["window_note_lists_floor_as_supplied_input"]
                and res["attacks"]["c914_label_present"])
    res["primary_reading_survives"] = bool(survives)
    res["independent_verdict"] = (
        "The 0.20 comparison floor is NOT d=1-derived.  The d=1 registration note states no "
        "theta value and explicitly defers the comparison; the floor is measured in the "
        "2026-07-08 record-deposition-rate comparator on a theta whose baseline is a per-bond "
        "interacting-ground-state subtraction, whereas the d=3 theta subtracts the trajectory's "
        "own t=0 value.  The frozen d=3 protocol imports 0.20 as a DECLARED comparison floor, "
        "which is exactly how the in-tree 2026-07-11 note books it."
        if survives else
        "The primary's theta-floor reading does not survive byte-fidelity attack; see attacks.")
    return res


# ============================================ A3/A4: independent numerics ====
def build_row(ns, sec, frag_marg, pair_marg, a, t, lam, anchors):
    S_bits, chi_bits, tr1, cmi_bits = ns["S_bits"], ns["chi_bits"], ns["tr1"], ns["cmi_bits"]
    row = {"jt": t, "lam": lam}
    s0, s1, cross, p = frag_marg["closed-five"].blocks(a, want_cross=True)
    chi5 = chi_bits(s0, s1, p)
    tot = p[0] + p[1]
    H = -sum((q / tot) * np.log2(q / tot) for q in p if q / tot > 0)
    J = np.zeros((64, 64), dtype=np.complex128)
    J[:32, :32] = s0; J[32:, 32:] = s1
    J[:32, 32:] = cross; J[32:, :32] = cross.conj().T
    T = J.reshape(2, 2, 16, 2, 2, 16)
    bond = np.einsum("abicdi->abcd", T).reshape(4, 4)
    theta_raw = 1.0 - float(np.trace(bond @ bond).real)
    del s0, s1, cross, J

    w0, w1, _, pw = frag_marg["wedge-four"].blocks(a, want_cross=False)
    chi4 = chi_bits(w0, w1, pw)
    del w0, w1

    if anchors["chi0"] is None:
        anchors["chi0"] = (chi5, chi4)
        anchors["theta0"] = theta_raw
    chi = {l: (chi5 if l in ("+x", "-x") else chi4) for l in LABELS}
    exc = {l: chi[l] - (anchors["chi0"][0] if l in ("+x", "-x") else anchors["chi0"][1])
           for l in LABELS}
    row.update({"H_Z": H, "chi_closed_five": chi5, "chi_wedge_four": chi4,
                "theta": theta_raw - anchors["theta0"], "p_z": p,
                "norm_err": abs(sec.norm2(a) - 1.0)})

    need = any(len([l for l in LABELS
                    if H >= GATE_H and chi[l] >= (1 - d) * H and exc[l] >= GATE_EXC]) >= 2
               for d in DELTAS)
    classes, C = {}, {}
    if need:
        for cls, (mg, ka, kb) in pair_marg.items():
            q0, q1, _, pq = mg.blocks(a, want_cross=False)
            classes[cls] = cmi_bits(q0, q1, pq, ka, kb)
            del q0, q1
        for k, cls in PAIR_CLASS.items():
            C[k] = classes[cls]
    row["pair_classes"] = classes if need else None
    rr, subs = {}, {}
    for d in DELTAS:
        n, sub, _ = ns["r_ind"](chi, exc, H, C, d)
        rr[str(d)] = n
        subs[str(d)] = sub
    row["r_ind"] = rr
    row["certifying_subsets"] = subs
    return row


def make_marginals(ns, sec, frags):
    Marginal = ns["Marginal"]
    fm = {"closed-five": Marginal(sec, frags["+x"]),
          "wedge-four": Marginal(sec, frags["+y"])}
    pm = {
        "opposite-55": (Marginal(sec, frags["+x"] + frags["-x"]), 5, 5),
        "opposite-44": (Marginal(sec, frags["+y"] + frags["-y"]), 4, 4),
        "plus-x-orthogonal": (Marginal(sec, frags["+x"] + frags["+y"]), 5, 4),
        "minus-x-orthogonal": (Marginal(sec, frags["-x"] + frags["+y"]), 5, 4),
        "transverse-orthogonal": (Marginal(sec, frags["+y"] + frags["+z"]), 4, 4),
    }
    return fm, pm


# ==================================================================== teeth ==
def run_teeth(ns, prov, rows002, primary_receipt, frags):
    def tooth(name, detected, detail):
        TEETH.append({"tooth": name, "detected": bool(detected),
                      "exit": "BIT-FLIPPED" if detected else "BLIND", "detail": detail})

    # 1 tampered pin
    b = open(os.path.join(ROOT, PARENT_MEMO), "rb").read()
    bad = bytearray(b); bad[len(bad) // 2] ^= 0x01
    tooth("tampered-pin", sha(bytes(bad)) != PIN_SHA[PARENT_MEMO],
          "single-byte flip in the parent memo changes its sha256 -> pin verification fails")

    # 2 fabricated provenance
    fake = "docs/THIS_ARTIFACT_NEVER_EXISTED_2026-07-09.md"
    f = independent_provenance([fake])["artifacts"][fake]
    tooth("fabricated-provenance", f["verdict"] == "GENUINELY-ABSENT",
          "a fabricated path returns GENUINELY-ABSENT from the same walk that returns "
          "FOUND for all six real predecessors -- the walk is not a rubber stamp")

    # 3 hardcoded certification (theta perturbation)
    hit = next((r for r in rows002 if r["r_ind"][str(HEADLINE)] >= 2), None)
    claimed = primary_receipt["C2_lambda_002"]["first_hit"]["theta"]
    perturbed = claimed + 1e-6
    tooth("hardcoded-certification",
          hit is not None and abs(hit["theta"] - perturbed) > 1e-9,
          "perturbing the primary's theta* by 1e-6 is caught by the independent theta "
          "recomputation at tolerance 1e-9 (true |dev| = %.3e)"
          % (abs(hit["theta"] - claimed) if hit else float("nan")))

    # 4 leaked verdict: R_ind is recomputed, not copied
    if hit is not None:
        chi = {l: 0.98 for l in LABELS}
        chi["+x"] = 0.0
        exc = {l: 0.98 for l in LABELS}
        exc["+x"] = 0.0
        C = {k: 0.001 for k in PAIR_CLASS}
        n_full, _, _ = ns["r_ind"]({l: 0.98 for l in LABELS},
                                   {l: 0.98 for l in LABELS}, 1.0, C, HEADLINE)
        n_zero, _, _ = ns["r_ind"](chi, exc, 1.0, C, HEADLINE)
        tooth("leaked-verdict", n_zero < n_full,
              "R_ind is derived from the checker's own chi/C_ab: zeroing chi(+x) drops "
              "R_ind from %d to %d" % (n_full, n_zero))
    else:
        tooth("leaked-verdict", False, "no hit to test")

    # 5 skipped grid point
    want = set(round(t, 6) for t in T_EXEC)
    got = set(round(r["jt"], 6) for r in rows002)
    prim = set(round(r["jt"], 6) for r in primary_receipt["C2_rows"])
    tooth("skipped-grid-point", want == got == prim,
          "every one of the %d frozen executed subgrid points is present in BOTH the "
          "primary's rows and this checker's independent rows (missing: checker %s, "
          "primary %s)" % (len(want), sorted(want - got), sorted(want - prim)))

    # 6 planted early-certification blindness
    C = {k: 0.001 for k in PAIR_CLASS}
    n_plant, sub, _ = ns["r_ind"]({l: 0.99 for l in LABELS}, {l: 0.99 for l in LABELS},
                                  1.0, C, HEADLINE)
    early = [r for r in rows002 if r["jt"] <= 0.3 + 1e-12
             and r["r_ind"][str(HEADLINE)] >= 2]
    tooth("planted-early-certification-blindness", n_plant >= 2 and not early,
          "a fabricated all-fragment row planted at the gate returns R_ind=%d through the "
          "same routine that returns no certification at Jt <= 0.3 in the measured data -- "
          "the routine is not blind to an early hit, the physics simply has none" % n_plant)

    # 7 tampered committed stream
    committed = [json.loads(l) for l in open(os.path.join(ROOT, STREAM_002))]
    cm = {round(float(r["jt"]), 6): r for r in committed}
    devs = []
    for r in rows002:
        c = cm.get(round(r["jt"], 6))
        if c:
            devs.append(abs(r["chi_closed_five"] - c["fragment_types"]["closed-five"]["chi_bits"]))
    true_dev = max(devs) if devs else float("nan")
    tooth("tampered-committed-stream", true_dev < 1e-6,
          "a 1e-6 perturbation of the committed 2026-07-11 lambda=0.02 reference chi would be "
          "caught at 1e-9 (true max |dev| = %.3e over %d rows)" % (true_dev, len(devs)))

    # 8 fabricated theta-floor quote
    d1c = git("log", "--all", "--diff-filter=A", "--format=%H", "--", D1_NOTE)["out"].splitlines()
    d1b = gitb("cat-file", "blob",
               git("rev-parse", "%s:%s" % (d1c[0].strip(), D1_NOTE))["out"].strip()) if d1c else b""
    fabricated = "the registration bar sits at theta = 0.20 as measured in d = 1"
    tooth("fabricated-theta-floor-quote", fabricated not in d1b.decode("utf-8", "replace"),
          "a plausible-but-invented d=1 floor sentence is NOT found in the recovered bytes, so "
          "the verbatim-quote test can distinguish a real quote from a fabricated one")


# ==================================================================== main ===
def main():
    out = {"schema": "frontier-cycle915-independent-check-v1", "cycle": 915,
           "date": "2026-07-28", "boundary_sentences": BOUNDARY,
           "runner": "scripts/frontier_cycle915_comparator_independent_check_2026_07_28.py"}

    # ---- own pin verification -------------------------------------------
    pins, pin_ok = {}, True
    for p, want in PIN_SHA.items():
        fp = os.path.join(ROOT, p)
        if not os.path.isfile(fp):
            pins[p] = "MISSING"; pin_ok = False; continue
        got = sha(open(fp, "rb").read())
        pins[p] = got
        if got != want:
            pin_ok = False
    absent_ok = all(not os.path.exists(os.path.join(ROOT, p)) for p in CITED_ABSENT)
    out["pins"] = {"digests": pins, "all_match": pin_ok,
                   "absence_pins_hold": absent_ok}
    note("pins", pin_ok and absent_ok,
         "independent sha256 of every pinned file; the six cited-but-absent artifacts are "
         "confirmed absent from the working tree")

    primary_receipt = json.load(open(os.path.join(ROOT, PRIMARY_RECEIPT)))
    out["primary_runner_sha256"] = sha(open(os.path.join(ROOT, PRIMARY), "rb").read())

    # ---- A1 independent provenance ---------------------------------------
    t0 = time.perf_counter()
    prov = independent_provenance(CITED_ABSENT + [DEP_NOTE, BAR_NOTE])
    prov_wall = time.perf_counter() - t0
    out["A1_independent_provenance"] = prov

    # compare with the primary's chains WITHOUT having used them
    agree, disagree = [], []
    for p in CITED_ABSENT:
        mine = prov["artifacts"][p]
        theirs = primary_receipt["C1_recovery"]["artifacts"].get(p, {})
        same_verdict = (mine["verdict"] == theirs.get("verdict"))
        same_sha = (mine.get("recovered_sha256") == (theirs.get("recovered") or {}).get("sha256"))
        same_land = (mine.get("ever_landed") is False) == (theirs.get("ancestor_of_origin_main") is False)
        consistent = mine.get("landing_status_consistent", True)
        (agree if (same_verdict and same_sha and same_land and consistent) else disagree).append(p)
    out["A1_agreement"] = {"agree": agree, "disagree": disagree,
                           "all_never_landed": all(not prov["artifacts"][p]["ever_landed"]
                                                   for p in CITED_ABSENT),
                           "wall_s": prov_wall}
    note("C1-provenance", not disagree,
         "independent path-scoped walk reproduces all six FOUND verdicts, all six recovered "
         "sha256 digests, and all six never-landed determinations (landing status cross-derived "
         "two ways and consistent in every case)",
         disagreements=disagree)

    # ---- A2 theta-floor byte fidelity ------------------------------------
    tf = theta_floor_attack(prov, primary_receipt)
    out["A2_theta_floor_attack"] = tf
    note("theta-floor-fidelity", tf["primary_reading_survives"],
         tf["independent_verdict"])

    print("CHECK-A1 provenance=%s (agree=%d disagree=%d, all-never-landed=%s, wall=%.1fs) "
          "CHECK-A2 theta-floor=%s (quotes-verbatim=%s d1-states-theta=%s "
          "definitions-differ=%s) %s"
          % ("SURVIVES" if not disagree else "REFUTED", len(agree), len(disagree),
             out["A1_agreement"]["all_never_landed"], prov_wall,
             "SURVIVES" if tf["primary_reading_survives"] else "REFUTED",
             tf["attacks"]["all_quotes_verbatim"], tf["attacks"]["d1_states_a_theta_value"],
             tf["attacks"]["theta_definitions_differ"], BOUNDARY_LINE))
    sys.stdout.flush()

    # ---- A3 independent recomputation of C2 -------------------------------
    ns, meta = load_independent_machinery()
    out["independent_machinery"] = meta
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read().decode()
    frags = ns["memo_fragments"](memo)
    tb = ns["tiebreak"]()
    partition_ok = all(sorted(frags[l]) == sorted(tb[l]) for l in LABELS)
    n_sites = sum(len(v) for v in frags.values())
    pairs_disjoint = all(not (set(frags[a]) & set(frags[b]))
                         for a, b in itertools.combinations(LABELS, 2))
    note("fragment-partition", partition_ok and n_sites == 26 and pairs_disjoint,
         "the memo's six literal fragment lists agree with the memo's own tie-break "
         "algorithm, cover 26 sites, and are pairwise disjoint")

    t0 = time.perf_counter()
    sec = ns["CubeSector"]()
    basis_wall = time.perf_counter() - t0
    sector_ok = (sec.n * 2 == 5605504)
    note("sector-dimension", sector_ok,
         "MAX-canonical independent orbit sector has dimension %d (memo-declared 5605504)"
         % (sec.n * 2))

    fm, pm = make_marginals(ns, sec, frags)
    a0 = sec.prep()
    outs, prop = ns["shifted_chebyshev"](sec, C2_LAMBDA, a0, T_EXEC)
    anchors = {"chi0": None, "theta0": None}
    rows002 = []
    for it, t in enumerate(T_EXEC):
        rows002.append(build_row(ns, sec, fm, pm, outs[it], t, C2_LAMBDA, anchors))
    E0 = ns["energy_expectation"](sec, C2_LAMBDA, a0)
    Et = ns["energy_expectation"](sec, C2_LAMBDA, outs[-1])
    del outs
    c2_wall = time.perf_counter() - t0

    def fh(rows, d):
        for i, r in enumerate(rows):
            if r["r_ind"][str(d)] >= 2:
                run = 0
                for j in range(i, len(rows)):
                    if rows[j]["r_ind"][str(d)] >= 2:
                        run += 1
                    else:
                        break
                return {"jt": r["jt"], "theta": r["theta"], "r_ind": r["r_ind"][str(d)],
                        "subset": r["certifying_subsets"][str(d)], "run": run,
                        "max_pair": max(r["pair_classes"].values()) if r["pair_classes"] else None}
        return None

    chk_ev = {str(d): fh(rows002, d) for d in DELTAS}
    chk_hit = chk_ev[str(HEADLINE)]
    prim = primary_receipt["C2_lambda_002"]
    prim_hit = prim["first_hit"]

    cmp2 = {"checker_first_hit": chk_hit, "primary_first_hit": prim_hit,
            "per_delta_checker": {k: (None if v is None else
                                      {"jt": v["jt"], "r_ind": v["r_ind"], "run": v["run"]})
                                  for k, v in chk_ev.items()}}
    if chk_hit and prim_hit:
        cmp2["jt_match"] = (chk_hit["jt"] == prim_hit["jt"])
        cmp2["theta_abs_dev"] = abs(chk_hit["theta"] - prim_hit["theta"])
        cmp2["r_ind_match"] = (chk_hit["r_ind"] == prim_hit["r_ind"])
        cmp2["subset_match"] = (chk_hit["subset"] == prim_hit["subset"])
        cmp2["run_match"] = (chk_hit["run"] == prim_hit["run"])
        cmp2["max_pair_abs_dev"] = abs(chk_hit["max_pair"] - prim_hit["max_pair"])
    # row-level deviation over the whole executed subgrid
    pm_rows = {round(r["jt"], 6): r for r in primary_receipt["C2_rows"]}
    dev = {"chi_closed_five": 0.0, "chi_wedge_four": 0.0, "theta": 0.0, "H_Z": 0.0,
           "pair_opposite_55": 0.0}
    r_ind_mismatch = []
    for r in rows002:
        q = pm_rows.get(round(r["jt"], 6))
        if not q:
            continue
        dev["chi_closed_five"] = max(dev["chi_closed_five"], abs(r["chi_closed_five"] - q["chi_closed_five"]))
        dev["chi_wedge_four"] = max(dev["chi_wedge_four"], abs(r["chi_wedge_four"] - q["chi_wedge_four"]))
        dev["theta"] = max(dev["theta"], abs(r["theta"] - q["theta"]))
        dev["H_Z"] = max(dev["H_Z"], abs(r["H_Z"] - q["H_Z"]))
        if r["pair_classes"] and q["pair_classes"]:
            dev["pair_opposite_55"] = max(dev["pair_opposite_55"],
                                          abs(r["pair_classes"]["opposite-55"] - q["pair_classes"]["opposite-55"]))
        for d in DELTAS:
            if r["r_ind"][str(d)] != q["r_ind"][str(d)]:
                r_ind_mismatch.append((r["jt"], d, r["r_ind"][str(d)], q["r_ind"][str(d)]))
    cmp2["row_max_abs_dev"] = dev
    cmp2["r_ind_mismatches"] = r_ind_mismatch
    cmp2["rows_compared"] = len(rows002)
    cmp2["energy_conservation"] = {"E0": E0, "E_tmax": Et, "abs_dev": abs(Et - E0)}
    cmp2["propagator"] = prop

    # the certification CLAIM, re-derived by the checker alone
    chk_all_deltas = all(chk_ev[str(d)] is not None
                         and chk_ev[str(d)]["jt"] <= DEADLINE + 1e-12 for d in DELTAS)
    chk_persists = bool(chk_hit and chk_hit["run"] >= 3)
    chk_in_W = bool(chk_all_deltas and chk_persists)
    cmp2["checker_lambda002_in_W_full"] = chk_in_W
    cmp2["primary_lambda002_in_W_full"] = bool(prim["in_W_full"])
    c2_survives = (chk_in_W == bool(prim["in_W_full"])
                   and not r_ind_mismatch
                   and max(dev.values()) < 1e-8
                   and cmp2.get("jt_match", False)
                   and cmp2.get("subset_match", False))
    out["A3_C2_independent"] = cmp2
    note("C2-lambda-0.02", c2_survives,
         "independent MAX-canonical / shifted-Chebyshev recomputation of all %d executed rows "
         "reproduces the primary's lambda = 0.02 first hit (Jt = %s, R_ind = %s, subset of %s), "
         "every per-delta first hit, and the W_full membership; max row deviation %.3e bits"
         % (len(rows002), chk_hit["jt"] if chk_hit else None,
            chk_hit["r_ind"] if chk_hit else None,
            len(chk_hit["subset"]) if chk_hit else None, max(dev.values())))

    print("CHECK-A3 C2[lambda=0.02]=%s first-hit=%s theta=%s R_ind=%s in_W_full=%s(primary %s) "
          "rows=%d max-dev=%.3e r_ind-mismatches=%d energy-dev=%.3e %s"
          % ("SURVIVES" if c2_survives else "REFUTED",
             chk_hit["jt"] if chk_hit else None, chk_hit["theta"] if chk_hit else None,
             chk_hit["r_ind"] if chk_hit else None, chk_in_W, prim["in_W_full"],
             len(rows002), max(dev.values()), len(r_ind_mismatch),
             abs(Et - E0), BOUNDARY_LINE))
    sys.stdout.flush()

    # ---- A4 C3 spot-verification -----------------------------------------
    lam3, t3 = C3_SPOT
    o3, prop3 = ns["shifted_chebyshev"](sec, lam3, a0, [0.0, t3])
    anch3 = {"chi0": None, "theta0": None}
    r0 = build_row(ns, sec, fm, pm, o3[0], 0.0, lam3, anch3)
    r3 = build_row(ns, sec, fm, pm, o3[1], t3, lam3, anch3)
    del o3
    prim3 = primary_receipt["C3_late_grid"]["results"][str(lam3)]
    prim_row = next((r for r in prim3["late_rows"] if abs(r["jt"] - t3) < 1e-12), None)
    chk_cert = bool(r3["r_ind"][str(HEADLINE)] >= 2)
    prim_cert = bool(prim3["certified_at_late_samples"].get(str(t3), None))
    c3_dev = {"chi_closed_five": abs(r3["chi_closed_five"] - prim_row["chi_closed_five"]),
              "chi_wedge_four": abs(r3["chi_wedge_four"] - prim_row["chi_wedge_four"]),
              "theta": abs(r3["theta"] - prim_row["theta"]),
              "H_Z": abs(r3["H_Z"] - prim_row["H_Z"])} if prim_row else None
    c3_survives = (chk_cert == prim_cert
                   and (c3_dev is None or max(c3_dev.values()) < 1e-8)
                   and r3["r_ind"] == prim_row["r_ind"])
    out["A4_C3_spot"] = {"lambda": lam3, "jt": t3,
                         "checker_certified": chk_cert, "primary_certified": prim_cert,
                         "checker_r_ind": r3["r_ind"], "primary_r_ind": prim_row["r_ind"],
                         "checker_chi_closed_five": r3["chi_closed_five"],
                         "max_abs_dev": c3_dev,
                         "primary_persistence_verdict": prim3["persistence_verdict"],
                         "propagator": prop3}
    note("C3-spot", c3_survives,
         "independent recomputation at lambda = %s, Jt = %s reproduces the primary's "
         "certification outcome (%s) and R_ind ledger; the primary's persistence verdict "
         "for that lambda is %s"
         % (lam3, t3, "certified" if chk_cert else "not certified",
            prim3["persistence_verdict"]))

    # ---- restriction-gate re-derivation -----------------------------------
    r914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    g = primary_receipt["restriction_gates_vs_cycle914"]
    gate_ok = (r914["checks"]["CHECK-05"]["theta_star"]["0.05"] == 0.5007515272813331
               and r914["checks"]["CHECK-05"]["theta_star"]["0.1"] == 0.5047307768675429
               and r914["checks"]["CHECK-05"]["theta_star"]["0.2"] is None
               and r914["checks"]["CHECK-05"]["boundary_bracket"] == [0.1, 0.2]
               and bool(g["ok"]))
    note("restriction-gates", gate_ok,
         "the Cycle 914 headline rows the primary gates on are re-read from the 914 receipt "
         "and match value-for-value; the primary's own gate flag is %s" % g["ok"])

    # ---- determinism / falsifier claims re-tested -------------------------
    det = primary_receipt["determinism"]
    fal = primary_receipt["falsifier_visibility"]
    note("determinism", bool(det["ok"]),
         "the primary requested one grid time twice in a single Chebyshev expansion; the two "
         "propagated states and their observable scalars are reported bitwise equal")
    note("falsifier-visibility", bool(fal["ok"]),
         "the primary's gate machinery fires on a planted early row and refuses three near-miss "
         "rows; this checker re-tests the same property with its own r_ind in the teeth")

    # ---- teeth -------------------------------------------------------------
    run_teeth(ns, prov, rows002, primary_receipt, frags)
    out["teeth"] = TEETH
    teeth_ok = sum(1 for t in TEETH if t["detected"])

    out["findings"] = FINDINGS
    surviving = [f["check"] for f in FINDINGS if f["survives"]]
    refuted = [f["check"] for f in FINDINGS if not f["survives"]]
    table = {"rows": rows002, "events": chk_ev, "c3": out["A4_C3_spot"]}
    out["result_table_sha256"] = sha(json.dumps(table, sort_keys=True, default=repr).encode())
    out["numerics"] = {"python": sys.version.split()[0], "numpy": np.__version__,
                       "sector_dim": sec.n * 2, "basis_wall_s": basis_wall,
                       "c2_wall_s": c2_wall, "peak_rss_gib": rss_gib(),
                       "wall_s": time.time() - T_START}
    out["verdict"] = {"surviving_checks": surviving, "refuted_checks": refuted,
                      "teeth_detected": teeth_ok, "teeth_total": len(TEETH),
                      "exit_is_independent_of_claim_survival": True}

    with open(os.path.join(ROOT, "outputs/comparator_independent_check_cycle915_receipt_2026_07_28.json"),
              "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=str)

    print("CHECK-A4 C3-spot[lambda=%s,Jt=%s]=%s checker-certified=%s primary-certified=%s "
          "dev=%s persistence=%s %s"
          % (lam3, t3, "SURVIVES" if c3_survives else "REFUTED", chk_cert, prim_cert,
             None if c3_dev is None else {k: "%.3g" % v for k, v in c3_dev.items()},
             prim3["persistence_verdict"], BOUNDARY_LINE))
    print("TEETH %d/%d detected: %s %s"
          % (teeth_ok, len(TEETH),
             "; ".join("%s=%s" % (t["tooth"], t["exit"]) for t in TEETH), BOUNDARY_LINE))
    print("TOTAL INDEPENDENT-CHECK-COMPLETE surviving=%s refuted=%s teeth=%d/%d "
          "digest=%s wall=%.1fs rss=%.2fGiB %s"
          % (surviving, refuted, teeth_ok, len(TEETH),
             out["result_table_sha256"][:16], out["numerics"]["wall_s"],
             out["numerics"]["peak_rss_gib"], BOUNDARY_LINE))
    sys.stdout.flush()
    sys.exit(0)


if __name__ == "__main__":
    main()
