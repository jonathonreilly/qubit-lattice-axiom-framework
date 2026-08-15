#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 915 -- the low-field certification run at lambda = 0.02 and the
late-time certification probe on the frozen finite d = 3 transverse-field
registration comparator.

Successor to the landed Cycle 914 comparator reproduction
(`scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py`, landed on
origin/main at 6277e4c6dfe77cf094b09a3529a69c1813773876), which reproduced the
committed d = 3 registration comparator streams on the parent memo's
commissioned lambda set {0.05, 0.10, 0.20} over Jt in {0.0, ..., 1.2}. Every
Cycle 914 byte consumed here is the LANDED byte. This runner executes two
finite scopes the landed Cycle 914 package explicitly left open.

LOW-FIELD CERTIFICATION RUN (historical alias: C2).  The frozen delta memo
    `docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md` commissions
    `lambda in {0.02, 0.05, 0.10, 0.20}`.  Landed Cycle 914 ran the parent set
    only and recorded the omission.  This runner executes the frozen protocol at
    lambda = 0.02 on the certification subgrid: the three-condition
    certification per fragment per sampled grid time, the first sampled
    certified time (or its absence) by Jt <= 1, the disjoint-pair witness, C_ab
    on the subgrid, and the CHECK-gate outcomes.  The lambda = 0.02 stream is
    ALREADY COMMITTED in this tree; this run is a REPRODUCTION of it on
    independent machinery, not a new measurement.

LATE-TIME CERTIFICATION PROBE (historical alias: C3).  The frozen certification
    subgrid carries four late samples {1.5, 2.0, 5.0, 10.0} that landed Cycle
    914 did not execute.  This runner executes Jt in {1.5, 2.0} at both sampled
    certified lambdas {0.05, 0.10} -- four rows in total -- and reports, for
    each row, whether the imported certification predicate holds AT THAT SAMPLE.
    Nothing is concluded about untested times, untested lambdas, or the
    behaviour of the certification predicate as a function.  {5.0, 10.0} are NOT
    executed under the runtime cap and are disclosed as such.

Machinery.  The sector reduction, Chebyshev propagator, marginal reconstruction,
certification and commutator routines are AST-EXTRACTED from the LANDED Cycle
914 primary (whose exactness against full space was verified by the Cycle 914
independent checker, and whose Chebyshev truncation bound is the corrected
operator-norm bound) rather than reimplemented; the extraction is byte-pinned
and the extracted source's sha256 is reported.

Claim scope.  Every number here is a finite, sampled, fixed-partition,
fixed-gate observation under the frozen protocol's imported cuts.  This runner
asserts no impossibility, no decay law, no functional non-tracking statement,
and no threshold test against the imported 0.20 theta convention.

Exit contract: exit 0 unless a pin, an internal machinery tolerance, the
determinism gate, or the falsifier probe fails; exit 2 on any of those.  The
certification outcomes are outcome-neutral and never move the exit code.

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
import sys
import time

import numpy as np
from scipy.special import jv

T_START = time.time()

# Declared execution budget for the audit-lane cache envelope.
AUDIT_TIMEOUT_SEC = 900

# Mutable repository inputs this runner reads as scientific evidence. Every one
# is landed on origin/main at the bytes pinned in PINS below. The runner's own
# source is not listed: it is hashed by the cache envelope itself.
AUDIT_INPUT_PATHS = (
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md",
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md",
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md",
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py",
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json",
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl",
)

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = "| " + " | ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================== pins =========
# (path -> (sha256, git blob sha1)).  Hard-fail exit 2 on any mismatch.
# EVERY pin below is the byte landed on origin/main at
# 6277e4c6dfe77cf094b09a3529a69c1813773876 (verified with `git cat-file`).  The
# Cycle 914 primary and receipt are the FIXED, landed forms; the pre-fix branch
# bytes this package originally carried are not consumed anywhere.
# The axiom memo is deliberately NOT pinned: it was context-only in the
# predecessor and is context-only here, its historical snapshot is superseded as
# the current package consumes no axiom-memo content.
PINS = {
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md": (
        "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
        "5dff1d8b1692099cd86b53959834b6bcb5865a71"),
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md": (
        "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
        "5f056aa69d1cc06dbfa2dc9ed6804df40c7b39fe"),
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md": (
        "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
        "d5b36708949d06bf619b2452e8f2897468e51194"),
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py": (
        "0cfab8fde089be2252f47a710d5822bc5a3458f6e15b37784855716979eb9dd4",
        "3d4c38794466d85047831efd099a9de313b5f343"),
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "2dddb1e145fb5854f1f303f8d417c4d8e62e84a64c1f8f3451bcf65ec2550e86",
        "15214b5f0b6e66855b41103da508f7a7bf09029f"),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl": (
        "9bf9282d477daf43635d29647ea0757fefb6105b755519c515539b3e28be3177",
        "6a3588d9a99efd6e704a1bff0127815995aa1fb4"),
}

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
C914_PRIMARY = "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
STREAM_002 = "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl"

# ------------------------------------------------------ frozen protocol ------
# EVERY constant in this block is an IMPORTED, DECLARED SCOPE INPUT stipulated by
# the two frozen memos pinned above.  None is derived, fitted, or measured in
# this package, and none is a framework primitive.  The per-constant role is
# recorded in PROTOCOL_INPUT_ROLES and emitted verbatim in the receipt.
DELTAS = (0.05, 0.10, 0.20)              # imported: tolerance cuts
HEADLINE_DELTA = 0.10                    # imported: which tolerance is headline
DEADLINE_JT = 1.0                        # imported: certification deadline
CONTENT_H_MIN = 0.05                     # imported: certification condition 1
EXCESS_MIN = 0.02                        # imported: certification condition 3
INDEP_MAX = 0.02                         # imported: condition 4 / C_ab gate
T0_ANCHOR_TOL = 1e-9                     # declared here: CHECK-01 numeric tol
DRIFT_MAX = 0.10                         # imported: CHECK-02 pointer drift cut
PERSIST_N = 3                            # imported: CHECK-03 persistence count
DELTA_FACTOR_MAX = 1.5                   # imported: CHECK-04 field factor cut
THETA_FLOOR = 0.20                       # IMPORTED COMPARATOR CONVENTION, UNVERIFIED
MACH_TOL = 1e-9                          # declared here: machinery tolerance
CHEBY_TAIL_MAX = 1e-12                   # declared here: truncation-bound gate
LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
X_CONTROL_MAX_JT = 1.0
CENTER = (0, 0, 0)

PROTOCOL_INPUT_ROLES = {
    "deltas": "imported declared scope input (frozen parent memo): the three "
              "tolerance cuts 0.05/0.10/0.20; not derived or fitted here",
    "headline_delta": "imported declared scope input: which tolerance the memo "
                      "designates as headline",
    "deadline_jt": "imported declared scope input: the Jt <= 1 certification "
                   "deadline",
    "content_excess_independence_gates": "imported declared scope inputs: the "
                                         "0.05 content, 0.02 excess and 0.02 "
                                         "conditional-independence cuts",
    "persistence_count": "imported declared scope input: three consecutive "
                         "sampled certifications",
    "drift_max": "imported declared scope input: the 0.10 pointer-drift cut",
    "field_factor_max": "imported declared scope input: the 1.5 cross-field "
                        "factor cut",
    "theta_floor": "IMPORTED COMPARATOR CONVENTION, UNVERIFIED.  The 0.20 value "
                   "is supplied to the frozen d = 3 protocol rather than derived "
                   "here. It is reported for disclosure only. This runner performs "
                   "NO threshold test against it and emits NO categorical "
                   "inside/outside label; any interpretation of that convention is "
                   "outside this finite-sample result.",
    "lambda_and_time_grids": "imported declared scope inputs (frozen delta memo "
                             "commissions the four lambdas; the frozen parent "
                             "memo fixes the certification subgrid); the "
                             "executed subset is disclosed in DEVIATIONS",
    "t0_anchor_tol_mach_tol_cheby_tail_max": "declared HERE as numerical "
                                             "tolerances of this run's own "
                                             "machinery gates; not physics",
}

# ------------------------------------------------- executed scope ------------
LOW_FIELD_LAMBDA = 0.02                                     # delta-memo lambda 1
LOW_FIELD_TIMES = [round(0.1 * i, 10) for i in range(13)]   # 0.0 .. 1.2
LOW_FIELD_DUP_T = 0.6     # requested twice in one propagation -> determinism gate
LATE_LAMBDAS = (0.05, 0.10)                     # the 914 sampled-certified pair
LATE_TIMES = [1.5, 2.0]                         # executed late samples
LATE_NOT_EXECUTED = [5.0, 10.0]                 # not afforded under the cap
T_C_FROZEN = [round(0.1 * i, 10) for i in range(13)] + [1.5, 2.0, 5.0, 10.0]

DEVIATIONS = [
    "EXECUTED-SCOPE-LOW-FIELD: lambda = 0.02 executed on the frozen certification subgrid "
    "restricted to Jt in {0.0, ..., 1.2} (13 of the 17 T_C points).  The frozen main "
    "state grid Jt = 0:0.1:10 is NOT executed.  Identical restriction to Cycle 914's "
    "EXECUTED-GRID deviation, and for the same reason: the 900 s runtime cap against a "
    "frozen schedule that projects 7.1 h.  The deadline gate (Jt <= 1) and the "
    "three-consecutive-sample persistence gate both live entirely inside the executed "
    "window, so no CHECK-03 outcome depends on the omission.",

    "EXECUTED-SCOPE-LATE-TIME: the frozen late certification samples are "
    "{1.5, 2.0, 5.0, 10.0}.  This run executes {1.5, 2.0} at both sampled certified "
    "lambdas {0.05, 0.10} -- four rows; {5.0, 10.0} are NOT executed at either lambda.  "
    "Reason: the Chebyshev degree scales with A * t_max (A = 54 + 27 lambda), so "
    "t_max = 10 costs M = 662 matrix-vector products per lambda against M = 169 for "
    "t_max = 2.0 -- roughly 491 s versus 125 s per lambda, which does not fit beside the "
    "low-field run under the 900 s cap.  Consequence for the claim: the four executed "
    "rows are the ENTIRE late-time evidence.  Nothing is asserted about Jt = 5, 10, "
    "about intermediate times, or about the certification predicate as a function of "
    "time; the honest reading of the four rows is 'not certified at these tested "
    "samples'.",

    "LAZY-Z-PAIRS: inherited from Cycle 914.  The frozen design evaluates the five pair "
    "classes at every T_C time; this run applies the design's own lazy rule (declared "
    "there for the X control) to Z as well, skipping pair evaluation at rows where fewer "
    "than two fragments pass the singleton gates at every delta.  Such rows cannot reach "
    "R_ind >= 2, so no first-hit time can change; skipped rows carry the reason "
    "'fewer-than-two-singleton-passes' and are never read as independence.",

    "GROUND-DOUBLET: inherited from Cycle 914.  The two-state invariant-sector Lanczos "
    "baseline is NOT executed under the runtime cap.  The frozen memo assigns the doublet "
    "a control-and-diagnostic-only role and FORBIDS it as a gate baseline, so no gate "
    "depends on it.  A repeated-observable stationary control anchored at its own first "
    "row is substituted and reported.",

    "DT-HALVING: inherited from Cycle 914.  This runner evaluates exp(-iHt) directly at "
    "each requested t by a single Chebyshev expansion of the sector Hamiltonian, so no dt "
    "exists to halve.  Substituted diagnostics: the rigorous Chebyshev truncation tail "
    "bound, state-norm conservation, and the duplicate-time propagation determinism gate.",

    "MACHINERY-REUSE: the sector reduction, propagator, marginal, certification and "
    "commutator routines are AST-extracted from the LANDED Cycle 914 primary rather than "
    "reimplemented.  This is deliberate: it makes the low-field and late-time runs a "
    "scope extension of a landed, verified implementation rather than a second "
    "implementation with its own error surface.  The INDEPENDENT recomputation lives in "
    "the paired checker, which reimplements the certification arithmetic from the memos.",

]

# =========================================== Cycle 914 restriction constants ==
# Rows this block must reproduce value-for-value out of the LANDED 914 receipt
# (origin/main 6277e4c6dfe77cf094b09a3529a69c1813773876).  These are byte-level
# restriction gates on landed content, not scientific targets of this run.
# The landed package issues NO delta-wiring completion verdict -- it records
# `delta_contract_discharged: false` -- so no such verdict is required or
# consumed here; the retired pre-fix verdict string is not referenced anywhere.
C914_EXPECT = {
    "theta_star": {"0.05": 0.5007515272813331, "0.1": 0.5047307768675429, "0.2": None},
    "labels": {"0.05": "above-unverified-imported-floor",
               "0.1": "above-unverified-imported-floor", "0.2": None},
    "median": 0.502741152074438,
    "boundary_bracket": [0.1, 0.2],
    "event_jt": {"0.05": 0.6, "0.1": 0.7, "0.2": None},
    "lam020_opposite55_at_content_peak": 0.060394807359658895,
    "lam020_content_peak_jt": 0.7,
    "W_sampled_914": [0.05, 0.1],
    "verdict_parent": "BAR-NOT-PINNED",
    "delta_contract_discharged": False,
}
# Committed 2026-07-11 lambda = 0.02 stream values (the reproduction target).
COMMITTED_002 = {
    "first_hit_jt_headline": 0.6,
    "theta_star_headline": 0.5001041579430463,
    "r_ind_headline": 6,
    "max_pair_at_hit": 0.0011326954132860711,
    "subset_headline": ["+x", "-x", "+y", "-y", "+z", "-z"],
}


# ============================================================ utilities ======
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def blob_sha1(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def die(msg):
    print("SETUP MACHINERY-FAIL %s %s" % (msg, BOUNDARY_LINE))
    print("TOTAL MACHINERY-FAIL %s" % BOUNDARY_LINE)
    sys.stdout.flush()
    sys.exit(2)


def verify_pins():
    """Verify every declared input byte exactly; hard-fail exit 2 on drift."""
    out = {}
    for path, (want_sha, want_blob) in PINS.items():
        fp = os.path.join(ROOT, path)
        if not os.path.isfile(fp):
            die("pin:missing %s" % path)
        b = open(fp, "rb").read()
        got_sha, got_blob = sha256_bytes(b), blob_sha1(b)
        if want_sha != got_sha:
            die("pin:sha256 %s want=%s got=%s" % (path, want_sha[:16], got_sha[:16]))
        if want_blob != got_blob:
            die("pin:blob %s want=%s got=%s" % (path, want_blob[:12], got_blob[:12]))
        out[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b)}
    return out


def rss_gib():
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return ru / (2.0 ** 30) if ru > 2 ** 32 else ru / (1024.0 ** 2)


# ================================================ AST extraction (Cycle 914) ==
EXTRACT_FUNCS = ["cube_sites", "proper_rotations", "parse_memo_fragments",
                 "tiebreak_fragments", "build_descriptor", "_bitperm_tables",
                 "chebyshev", "ent_bits", "conditional_blocks", "chi_holevo",
                 "ptrace_keep_one", "ptrace_split", "cond_mi", "purity", "r_ind",
                 "centered_frobenius_panel"]
EXTRACT_CLASSES = ["Sector"]
EXTRACT_ASSIGNS = ["CH"]


def extract_914_machinery():
    """Lift the verified Cycle 914 numerical machinery by AST.  No re-typing."""
    src_path = os.path.join(ROOT, C914_PRIMARY)
    src = open(src_path, "rb").read()
    tree = ast.parse(src.decode())
    keep, names = [], []
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name in EXTRACT_FUNCS:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.ClassDef) and n.name in EXTRACT_CLASSES:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.Assign):
            tg = [x.id for x in n.targets if isinstance(x, ast.Name)]
            if tg and tg[0] in EXTRACT_ASSIGNS:
                keep.append(n); names.append(tg[0])
    missing = ([f for f in EXTRACT_FUNCS if f not in names]
               + [c for c in EXTRACT_CLASSES if c not in names]
               + [a for a in EXTRACT_ASSIGNS if a not in names])
    if missing:
        die("ast:missing %s" % ",".join(missing))
    mod = ast.Module(body=keep, type_ignores=[])
    ast.fix_missing_locations(mod)
    extracted_src = "\n\n".join(ast.unparse(n) for n in keep)
    ns = {"np": np, "hashlib": hashlib, "itertools": itertools, "json": json,
          "re": re, "jv": jv, "sha256_bytes": sha256_bytes,
          # the frozen protocol constants the extracted routines close over
          "CENTER": CENTER, "LABELS": LABELS, "CONTENT_H_MIN": CONTENT_H_MIN,
          "EXCESS_MIN": EXCESS_MIN, "INDEP_MAX": INDEP_MAX}
    exec(compile(mod, src_path, "exec"), ns)
    return ns, {"names": sorted(names),
                "extracted_source_sha256": sha256_bytes(extracted_src.encode()),
                "source_file": C914_PRIMARY,
                "source_sha256": sha256_bytes(src)}


# =============================================== restriction gates (914) =====
def restriction_gates(receipt, ns):
    g = {}
    c05 = receipt["checks"]["CHECK-05"]
    ev = receipt["measurement"]["events"]

    g["theta_star_value_for_value"] = (c05["theta_star"] == C914_EXPECT["theta_star"])
    g["labels_value_for_value"] = (c05["labels"] == C914_EXPECT["labels"])
    g["median_value_for_value"] = (c05["median"] == C914_EXPECT["median"])
    g["boundary_bracket_value_for_value"] = (c05["boundary_bracket"] == C914_EXPECT["boundary_bracket"])

    jt = {}
    for lam in ("0.05", "0.1", "0.2"):
        h = ev[lam][str(HEADLINE_DELTA)]
        jt[lam] = None if h is None else h["jt"]
    g["event_jt_value_for_value"] = (jt == C914_EXPECT["event_jt"])
    g["event_jt_observed"] = jt

    rows020 = receipt["measurement"]["rows"]["0.2"]
    peak = next((r for r in rows020
                 if abs(r["jt"] - C914_EXPECT["lam020_content_peak_jt"]) < 1e-12), None)
    got = peak["pair_classes"]["opposite-55"] if peak and peak["pair_classes"] else None
    g["lam020_C55_value_for_value"] = (got == C914_EXPECT["lam020_opposite55_at_content_peak"])
    g["lam020_C55_observed"] = got
    g["lam020_C55_above_gate"] = bool(got is not None and got > INDEP_MAX)

    g["W_sampled_914"] = receipt["checks"]["CHECK-03-window-subset"]["W_full"]
    g["W_sampled_value_for_value"] = (g["W_sampled_914"] == C914_EXPECT["W_sampled_914"])
    # The landed parent issues one wiring verdict and explicitly records that the
    # delta contract is NOT discharged; both are gated here so that a tree whose
    # Cycle 914 bytes are not the landed ones cannot pass.
    g["verdicts_value_for_value"] = (
        receipt["verdict"]["parent_wiring"] == C914_EXPECT["verdict_parent"]
        and receipt["verdict"].get("delta_contract_discharged")
        is C914_EXPECT["delta_contract_discharged"]
        and "delta_wiring" not in receipt["verdict"])

    # CHECK-02 closed-form panel, spot-verified against an independent evaluation
    degrees = {"center": 6, "face": 5, "edge": 4, "corner": 3}
    spot = {}
    ok = True
    for lam_s, panel in receipt["measurement"]["centered_frobenius"].items():
        lam = float(lam_s)
        d = 2.0 ** 27
        den = np.sqrt(d) * np.sqrt(54.0 + 27.0 * lam * lam)
        for cls, deg in degrees.items():
            want = {"Z": 2.0 * lam / den,
                    "X": 2.0 * np.sqrt(deg) / den,
                    "Y": 2.0 * np.sqrt(deg + lam * lam) / den}
            got_p = panel[cls]
            for k in ("Z", "X", "Y"):
                if abs(got_p[k] - want[k]) > 1e-18:
                    ok = False
            spot["%s/%s" % (lam_s, cls)] = {"Z": want["Z"], "X": want["X"], "Y": want["Y"]}
    g["check02_panel_spot_verified"] = ok
    g["check02_panel_recomputed"] = spot
    # the panel's own physics content: max_Z < min_X at every commissioned lambda
    g["check02_ordering_holds"] = all(
        max(v["Z"] for v in panel.values()) < min(v["X"] for v in panel.values())
        for panel in receipt["measurement"]["centered_frobenius"].values())

    g["ok"] = all(bool(v) for k, v in g.items()
                  if k.endswith("value_for_value") or k in
                  ("check02_panel_spot_verified", "check02_ordering_holds"))
    return g


# ==================================================== the measurement ========
def observable_row(ns, sec, OL, frags, pair_class, a, t, lam, chi0, one0, bond0,
                   x_chi0, mach, do_x_control):
    """One certification row.  Structure follows the Cycle 914 primary exactly."""
    shell_of = {1: "face", 2: "edge", 3: "corner"}
    Fpx, Fpy = frags["+x"], frags["+y"]
    conditional_blocks = ns["conditional_blocks"]
    chi_holevo = ns["chi_holevo"]
    ptrace_keep_one = ns["ptrace_keep_one"]
    cond_mi = ns["cond_mi"]
    purity = ns["purity"]
    r_ind = ns["r_ind"]

    n2 = sec.norm2(a)
    mach["norm"] = max(mach["norm"], abs(n2 - 1.0))
    row = {"jt": t, "lam": lam}

    s0, s1, cross, p, herm = conditional_blocks(a, OL["opposite-55"][0], 5, "Z", True)
    mach["hermiticity"] = max(mach["hermiticity"], herm)
    chi5, neg5 = chi_holevo(s0, s1, p)
    H = -sum(q * np.log2(q) for q in p if q > 0)
    rho_joint = np.zeros((64, 64), dtype=np.complex128)
    rho_joint[:32, :32] = s0
    rho_joint[32:, 32:] = s1
    rho_joint[:32, 32:] = cross
    rho_joint[32:, :32] = cross.conj().T
    T = rho_joint.reshape(2, 2, 16, 2, 2, 16)
    bond5 = np.einsum("abicdi->abcd", T).reshape(4, 4)
    coh = float(np.abs(cross).max())
    one5 = {}
    for j, site in enumerate(Fpx):
        r0 = ptrace_keep_one(s0, 5, j)
        r1 = ptrace_keep_one(s1, 5, j)
        c1, _ = chi_holevo(r0, r1, p)
        one5.setdefault(shell_of[sum(map(abs, site))], []).append((c1, r0 + r1))
    del s0, s1, cross, rho_joint

    w0, w1, wcross, pw, hermw = conditional_blocks(a, OL["opposite-44"][0], 4, "Z", True)
    mach["hermiticity"] = max(mach["hermiticity"], hermw)
    chi4, neg4 = chi_holevo(w0, w1, pw)
    rj = np.zeros((32, 32), dtype=np.complex128)
    rj[:16, :16] = w0
    rj[16:, 16:] = w1
    rj[:16, 16:] = wcross
    rj[16:, :16] = wcross.conj().T
    T = rj.reshape(2, 2, 8, 2, 2, 8)
    bond4 = np.einsum("abicdi->abcd", T).reshape(4, 4)
    one4 = {}
    for j, site in enumerate(Fpy):
        r0 = ptrace_keep_one(w0, 4, j)
        r1 = ptrace_keep_one(w1, 4, j)
        c1, _ = chi_holevo(r0, r1, pw)
        one4.setdefault(shell_of[sum(map(abs, site))], []).append((c1, r0 + r1))
    del w0, w1, wcross, rj

    mach["negativity"] = max(mach["negativity"], abs(min(neg5, neg4)))
    for c in (chi5, chi4):
        mach["entropy_bound"] = max(mach["entropy_bound"], max(0.0, c - H, -c))
    sym = 0.0
    for cls in ("face", "edge"):
        allv = [x[0] for x in one5.get(cls, [])] + [x[0] for x in one4.get(cls, [])]
        if len(allv) > 1:
            sym = max(sym, max(allv) - min(allv))
    cor = [x[0] for x in one4.get("corner", [])]
    if len(cor) > 1:
        sym = max(sym, max(cor) - min(cor))
    sym = max(sym, abs(np.abs(bond5 - bond4)).max())
    sym = max(sym, abs(p[0] - pw[0]))
    mach["symmetry"] = max(mach["symmetry"], sym)

    one_chi = {c: float(np.mean([x[0] for x in (one5.get(c) or one4.get(c))]))
               for c in ("face", "edge", "corner")}
    one_rho = {}
    for c in ("face", "edge", "corner"):
        src = one5.get(c) or one4.get(c)
        one_rho[c] = sum(x[1] for x in src) / len(src)

    first = chi0 is None
    if first:
        chi0 = {"closed-five": chi5, "wedge-four": chi4}
        one0 = dict(one_chi)
        bond0 = 1.0 - purity(bond5)
        mach["t0_anchor"] = max(mach["t0_anchor"], abs(chi5), abs(chi4),
                                max(abs(v) for v in one_chi.values()))

    chi_by_label = {l: (chi5 if l in ("+x", "-x") else chi4) for l in LABELS}
    exc_by_label = {l: chi_by_label[l] - (chi0["closed-five"] if l in ("+x", "-x")
                                          else chi0["wedge-four"]) for l in LABELS}
    row.update({
        "H_Z": H, "p_z": p, "chi_closed_five": chi5, "chi_wedge_four": chi4,
        "excess_closed_five": chi5 - chi0["closed-five"],
        "excess_wedge_four": chi4 - chi0["wedge-four"],
        "one_site_chi": one_chi,
        "one_site_excess": {c: one_chi[c] - one0[c] for c in one_chi},
        "capacity_gain": {"closed-five": chi5 - max(x[0] for v in one5.values() for x in v),
                          "wedge-four": chi4 - max(x[0] for v in one4.values() for x in v)},
        "theta": (1.0 - purity(bond5)) - bond0,
        "pointer_tv_drift": abs(p[0] - 0.5),
        "removed_pointer_coherence": coh,
        "symmetry_max": sym,
        "state_norm_err": abs(n2 - 1.0),
        "sum_delta_chi": 2.0 * (chi5 - chi0["closed-five"]) + 4.0 * (chi4 - chi0["wedge-four"]),
    })
    bl = {}
    for c in ("face", "edge", "corner"):
        r = one_rho[c]
        bl[c] = [float(2 * r[0, 1].real), float(-2 * r[0, 1].imag),
                 float((r[0, 0] - r[1, 1]).real)]
    row["bloch"] = bl
    row["Q_quiet"] = 1.0 - (bl["edge"][2] + bl["corner"][2]) / 2.0
    row["X_face"] = bl["face"][0]

    need_pairs = any(
        len([l for l in LABELS
             if H >= CONTENT_H_MIN and chi_by_label[l] >= (1.0 - d) * H
             and exc_by_label[l] >= EXCESS_MIN]) >= 2 for d in DELTAS)
    C, classes = {}, {}
    if need_pairs:
        for cls, (ol, ka, kb) in OL.items():
            q0, q1, _, pq, hq = conditional_blocks(a, ol, ka + kb, "Z", False)
            mach["hermiticity"] = max(mach["hermiticity"], hq)
            classes[cls] = cond_mi(q0, q1, pq, ka, kb)
            del q0, q1
        for (la, lb), cls in pair_class.items():
            C[(la, lb)] = classes[cls]
    row["pair_classes"] = classes if need_pairs else None
    row["pair_reason"] = None if need_pairs else "fewer-than-two-singleton-passes"

    rr, subs, singles = {}, {}, {}
    for d in DELTAS:
        n, sub, sg = r_ind(chi_by_label, exc_by_label, H, C, d)
        rr[str(d)] = n
        subs[str(d)] = sub
        singles[str(d)] = sg
    row["r_ind"] = rr
    row["certifying_subsets"] = subs
    row["singleton_passes"] = singles
    row["r_raw"] = {k: len(v) for k, v in singles.items()}

    if do_x_control and t <= X_CONTROL_MAX_JT + 1e-12:
        x0, x1, _, px, _ = conditional_blocks(a, OL["opposite-55"][0], 5, "X", False)
        chi5x, _ = chi_holevo(x0, x1, px)
        del x0, x1
        y0, y1, _, py, _ = conditional_blocks(a, OL["opposite-44"][0], 4, "X", False)
        chi4x, _ = chi_holevo(y0, y1, py)
        del y0, y1
        tot = px[0] + px[1]
        Hx = -sum((q / tot) * np.log2(q / tot) for q in px if q / tot > 1e-15)
        if x_chi0 is None:
            x_chi0 = (chi5x, chi4x)
        xchi = {l: (chi5x if l in ("+x", "-x") else chi4x) for l in LABELS}
        xexc = {l: xchi[l] - (x_chi0[0] if l in ("+x", "-x") else x_chi0[1]) for l in LABELS}
        xr = {}
        for d in DELTAS:
            xr[str(d)] = len([l for l in LABELS
                              if Hx >= CONTENT_H_MIN and xchi[l] >= (1.0 - d) * Hx
                              and xexc[l] >= EXCESS_MIN])
        row["x_control"] = {
            "H_X": Hx, "p_x": px, "chi": [chi5x, chi4x],
            "singleton_passes": xr,
            "r_ind_ge2_possible": bool(any(v >= 2 for v in xr.values())),
            "pair_reason": None if any(v >= 2 for v in xr.values())
                           else "fewer-than-two-X-singletons-pass"}
    return row, chi0, one0, bond0, x_chi0


def first_hit(rows, delta):
    for i, r in enumerate(rows):
        if r["r_ind"][str(delta)] >= 2:
            run = 0
            for j in range(i, len(rows)):
                if rows[j]["r_ind"][str(delta)] >= 2:
                    run += 1
                else:
                    break
            return {"jt": r["jt"], "theta": r["theta"], "r_ind": r["r_ind"][str(delta)],
                    "subset": r["certifying_subsets"][str(delta)], "run": run,
                    "by_deadline": r["jt"] <= DEADLINE_JT + 1e-12,
                    "pair_values": r["pair_classes"], "drift": r["pointer_tv_drift"],
                    "Q_quiet": r["Q_quiet"], "X_face": r["X_face"],
                    "max_pair": (max(r["pair_classes"].values()) if r["pair_classes"] else None)}
    return None


# ====================================================== falsifier probe ======
def falsifier_probe(ns):
    """Falsifier visibility: a PLANTED early certification at lambda = 0.02 must be
    detected by the same gate machinery that produced the measured rows.  The probe
    proves the gate is outcome-sensitive, not that the physics certified early."""
    r_ind = ns["r_ind"]
    H = 1.0
    # a fabricated Jt = 0.1 row: content above the headline gate, pairs below the
    # independence gate.  If the machinery were blind to early rows, this returns < 2.
    chi = {l: 0.98 for l in LABELS}
    exc = {l: 0.98 for l in LABELS}
    C = {}
    idx = {l: i for i, l in enumerate(LABELS)}
    for a, b in itertools.combinations(LABELS, 2):
        C[tuple(sorted((a, b), key=idx.get))] = 0.001
    n_plant, sub_plant, _ = r_ind(chi, exc, H, C, HEADLINE_DELTA)
    # and a control: same content, pairs ABOVE the independence gate -> must NOT certify
    C_bad = {k: 0.5 for k in C}
    n_corr, _, singles_corr = r_ind(chi, exc, H, C_bad, HEADLINE_DELTA)
    # and a below-content control -> must not certify
    chi_low = {l: 0.5 for l in LABELS}
    n_low, _, _ = r_ind(chi_low, {l: 0.5 for l in LABELS}, H, C, HEADLINE_DELTA)
    # and a no-excess control -> must not certify (excess gate binding)
    n_noexc, _, _ = r_ind(chi, {l: 0.0 for l in LABELS}, H, C, HEADLINE_DELTA)
    return {
        "planted_early_certification_detected": bool(n_plant >= 2),
        "planted_r_ind": n_plant, "planted_subset": sub_plant,
        "correlated_pairs_rejected": bool(n_corr < 2),
        "correlated_r_ind": n_corr, "correlated_raw_singletons": len(singles_corr),
        "below_content_rejected": bool(n_low < 2), "below_content_r_ind": n_low,
        "zero_excess_rejected": bool(n_noexc < 2), "zero_excess_r_ind": n_noexc,
        "ok": bool(n_plant >= 2 and n_corr < 2 and n_low < 2 and n_noexc < 2),
        "meaning": "the gate machinery fires on a planted early row and refuses three "
                   "distinct near-miss rows, so a genuine early certification at "
                   "lambda = 0.02 could not have been missed by construction",
    }


# ============================================================== main =========
def main():
    pins = verify_pins()

    print("SETUP cycle=915 pins=%d durable-input-closure=origin/main %s"
          % (len(pins), BOUNDARY_LINE))
    sys.stdout.flush()

    # -------------------------------------------------- machinery + gates ---
    ns, ast_meta = extract_914_machinery()
    receipt914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    gates = restriction_gates(receipt914, ns)
    if not gates["ok"]:
        die("restriction-gate %s" % json.dumps({k: v for k, v in gates.items()
                                                if k.endswith("value_for_value")}))

    t_b = time.perf_counter()
    sec = ns["Sector"]()
    basis_wall = time.perf_counter() - t_b
    if sec.n * 2 != 5605504:
        die("basis:orbit-count %d" % (sec.n * 2))
    if sec.checksum != receipt914["numerics"]["basis_checksum"]:
        die("basis:checksum-drift %s" % sec.checksum[:16])

    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read()
    # The landed descriptor builder returns the count of PARTITION-PRESERVING
    # proper rotations alongside the partition.  That count is the narrowed
    # orbit-equivalence scope landed with Cycle 914: the declared partition is
    # NOT closed under the full 24-element proper cubic group, and no such
    # closure is claimed or used here.
    frags, pair_class, desc_sum, n_part_rots = ns["build_descriptor"](memo)
    if desc_sum != receipt914["protocol"]["fragment_descriptor_checksum"]:
        die("descriptor:drift %s" % desc_sum[:16])

    t_ol = time.perf_counter()
    Fpx, Fmx = frags["+x"], frags["-x"]
    Fpy, Fmy, Fpz = frags["+y"], frags["-y"], frags["+z"]
    OL = {
        "opposite-55": (sec.layout(Fpx + Fmx), 5, 5),
        "opposite-44": (sec.layout(Fpy + Fmy), 4, 4),
        "plus-x-orthogonal": (sec.layout(Fpx + Fpy), 5, 4),
        "minus-x-orthogonal": (sec.layout(Fmx + Fpy), 5, 4),
        "transverse-orthogonal": (sec.layout(Fpy + Fpz), 4, 4),
    }
    ol_wall = time.perf_counter() - t_ol
    del sec.orbit_of

    a0 = sec.prep(None, None, None)
    if abs(sec.norm2(a0) - 1.0) > 1e-12:
        die("prep:norm")

    mach = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0, "entropy_bound": 0.0,
            "symmetry": 0.0, "t0_anchor": 0.0, "cheby_tail": 0.0}

    # ================================== low-field certification run ========
    t_c2 = time.perf_counter()
    times2 = list(LOW_FIELD_TIMES) + [LOW_FIELD_DUP_T]        # duplicate -> determinism gate
    outs, prop2 = ns["chebyshev"](sec, LOW_FIELD_LAMBDA, a0, times2)
    mach["cheby_tail"] = max(mach["cheby_tail"], prop2["tail_bound"])
    dup_i = times2.index(LOW_FIELD_DUP_T)              # first occurrence
    dup_state_bitwise_equal = bool(np.array_equal(
        outs[dup_i].view(np.uint8), outs[-1].view(np.uint8)))

    rows2, chi0, one0, bond0, x_chi0 = [], None, None, None, None
    for it, t in enumerate(LOW_FIELD_TIMES):
        row, chi0, one0, bond0, x_chi0 = observable_row(
            ns, sec, OL, frags, pair_class, outs[it], t, LOW_FIELD_LAMBDA,
            chi0, one0, bond0, x_chi0, mach, True)
        rows2.append(row)
    # observable-pipeline determinism: recompute the duplicated time from the
    # duplicate state and require bitwise-equal scalars
    dup_row, _, _, _, _ = observable_row(
        ns, sec, OL, frags, pair_class, outs[-1], LOW_FIELD_DUP_T, LOW_FIELD_LAMBDA,
        chi0, one0, bond0, x_chi0, mach, False)
    ref_row = rows2[LOW_FIELD_TIMES.index(LOW_FIELD_DUP_T)]
    dup_keys = ["chi_closed_five", "chi_wedge_four", "theta", "H_Z", "sum_delta_chi"]
    dup_obs_equal = all(dup_row[k] == ref_row[k] for k in dup_keys)
    dup_pair_equal = (dup_row["pair_classes"] == ref_row["pair_classes"])
    del outs
    c2_wall = time.perf_counter() - t_c2

    ev2 = {str(d): first_hit(rows2, d) for d in DELTAS}
    h2 = ev2[str(HEADLINE_DELTA)]

    # --- membership in the delta memo's own sampled-window language ---
    all_deltas_hit_by_deadline = all(
        ev2[str(d)] is not None and ev2[str(d)]["by_deadline"] for d in DELTAS)
    headline_persists = bool(h2 is not None and h2["run"] >= PERSIST_N)
    lam002_in_W_full = bool(all_deltas_hit_by_deadline and headline_persists)

    per_delta2 = {str(d): (None if ev2[str(d)] is None else
                           {"jt": ev2[str(d)]["jt"], "by_deadline": ev2[str(d)]["by_deadline"],
                            "r_ind": ev2[str(d)]["r_ind"], "run": ev2[str(d)]["run"],
                            "theta": ev2[str(d)]["theta"]}) for d in DELTAS}

    # --- reproduction of the committed 2026-07-11 lambda = 0.02 stream ---
    committed = [json.loads(l) for l in open(os.path.join(ROOT, STREAM_002))]
    cmap = {round(float(r["jt"]), 6): r for r in committed}
    dev = {"theta": 0.0, "chi_closed_five": 0.0, "chi_wedge_four": 0.0,
           "H_Z": 0.0, "pair_opposite_55": 0.0}
    n_cmp = 0
    r_ind_agree = True
    for r in rows2:
        c = cmap.get(round(r["jt"], 6))
        if c is None:
            continue
        n_cmp += 1
        dev["theta"] = max(dev["theta"], abs(r["theta"] - c["theta"]))
        ft = c["fragment_types"]
        cf = ft["closed-five"].get("chi_bits")
        wf = ft["wedge-four"].get("chi_bits")
        if cf is not None:
            dev["chi_closed_five"] = max(dev["chi_closed_five"], abs(r["chi_closed_five"] - cf))
        if wf is not None:
            dev["chi_wedge_four"] = max(dev["chi_wedge_four"], abs(r["chi_wedge_four"] - wf))
        dev["H_Z"] = max(dev["H_Z"], abs(r["H_Z"] - c["pointer_z"]["entropy_bits"]))
        pc = c.get("pair_conditional_mi_bits") or {}
        if r["pair_classes"] and pc.get("classes"):
            dev["pair_opposite_55"] = max(
                dev["pair_opposite_55"],
                abs(r["pair_classes"]["opposite-55"] - pc["classes"]["opposite-55"]))
        for d in DELTAS:
            key = "%.2f" % d
            if key in c["r_ind"] and c["r_ind"][key] != r["r_ind"][str(d)]:
                r_ind_agree = False
    repro = {"rows_compared": n_cmp, "max_abs_dev": dev, "r_ind_agrees": r_ind_agree,
             "ok": bool(n_cmp > 0 and r_ind_agree and max(dev.values()) < 1e-8),
             "committed_targets": COMMITTED_002,
             "measured_first_hit_jt": None if h2 is None else h2["jt"],
             "measured_theta_star": None if h2 is None else h2["theta"],
             "measured_r_ind": None if h2 is None else h2["r_ind"],
             "measured_max_pair": None if h2 is None else h2["max_pair"]}

    print("LOW-FIELD[lambda=0.02] first-sampled-hit=%s theta*=%s R_ind=%s subset=%s run=%s "
          "max-pair=%s per-delta=%s sampled-window-member=%s repro-vs-committed=%s(rows=%d,dev=%s) %s"
          % (None if h2 is None else h2["jt"], None if h2 is None else h2["theta"],
             None if h2 is None else h2["r_ind"], None if h2 is None else h2["subset"],
             None if h2 is None else h2["run"], None if h2 is None else h2["max_pair"],
             per_delta2, lam002_in_W_full, repro["ok"], repro["rows_compared"],
             {k: "%.3g" % v for k, v in dev.items()}, BOUNDARY_LINE))
    sys.stdout.flush()

    # ====================================== late-time certification probe ====
    t_c3 = time.perf_counter()
    c3 = {}
    for lam in LATE_LAMBDAS:
        times3 = [0.0] + list(LATE_TIMES)
        o3, prop3 = ns["chebyshev"](sec, lam, a0, times3)
        mach["cheby_tail"] = max(mach["cheby_tail"], prop3["tail_bound"])
        rows3, c0, o0, b0, xc0 = [], None, None, None, None
        for it, t in enumerate(times3):
            row, c0, o0, b0, xc0 = observable_row(
                ns, sec, OL, frags, pair_class, o3[it], t, lam,
                c0, o0, b0, xc0, mach, False)
            rows3.append(row)
        del o3
        late = [r for r in rows3 if r["jt"] > 1.2]
        c3[str(lam)] = {
            "executed_times": times3,
            "propagator": {"degree": prop3["degree"], "matvecs": prop3["matvecs"],
                           "tail_bound": prop3["tail_bound"]},
            "late_rows": [{"jt": r["jt"], "r_ind": r["r_ind"], "theta": r["theta"],
                           "chi_closed_five": r["chi_closed_five"],
                           "chi_wedge_four": r["chi_wedge_four"],
                           "excess_closed_five": r["excess_closed_five"],
                           "H_Z": r["H_Z"], "pair_classes": r["pair_classes"],
                           "pair_reason": r["pair_reason"],
                           "singleton_passes": r["singleton_passes"],
                           "r_raw": r["r_raw"], "Q_quiet": r["Q_quiet"],
                           "X_face": r["X_face"], "drift": r["pointer_tv_drift"]}
                          for r in late],
            "certified_at_late_samples": {
                str(r["jt"]): bool(r["r_ind"][str(HEADLINE_DELTA)] >= 2) for r in late},
        }
        cert = c3[str(lam)]["certified_at_late_samples"]
        # Sampled labels ONLY.  Each label describes the executed rows and
        # nothing else: no decay law, no limit, no statement about untested
        # times or lambdas is expressed or implied by these strings.
        c3[str(lam)]["sampled_label"] = (
            "CERTIFIED-AT-ALL-TESTED-SAMPLES" if all(cert.values()) else
            "NOT-CERTIFIED-AT-ANY-TESTED-SAMPLE" if not any(cert.values())
            else "MIXED-ACROSS-TESTED-SAMPLES")
        c3[str(lam)]["sampled_label_meaning"] = (
            "a statement about the %d executed row(s) at this lambda only; the "
            "untested times {5.0, 10.0} and every unsampled time are outside it"
            % len(cert))
        c3[str(lam)]["early_first_hit_jt_from_914"] = C914_EXPECT["event_jt"][
            "0.05" if lam == 0.05 else "0.1"]
    c3_wall = time.perf_counter() - t_c3
    c3_scope = {"executed_times": list(LATE_TIMES), "executed_lambdas": list(LATE_LAMBDAS),
                "not_executed_times": list(LATE_NOT_EXECUTED),
                "executed_row_count": len(LATE_TIMES) * len(LATE_LAMBDAS),
                "reading": "the four executed rows support exactly one sentence: the "
                           "imported certification predicate does not hold at these "
                           "tested samples.  No decay, no limit, no monotonicity and no "
                           "statement about theta as an indicator follows from them.",
                "design_semantics": "the frozen memo classes all four late certification "
                                    "samples as recurrence diagnostics that do not rescue "
                                    "CHECK-03; these labels are finite-sample flags"}

    print("LATE-TIME[executed=%s] %s %s"
          % (json.dumps(c3_scope["executed_times"]),
             "; ".join("lambda=%s:%s(%s)" % (l, c3[l]["sampled_label"],
                                             json.dumps(c3[l]["certified_at_late_samples"]))
                       for l in c3),
             BOUNDARY_LINE))
    sys.stdout.flush()

    # ============================================== checks on the new data ==
    fal = falsifier_probe(ns)

    c01 = {"t0_anchor_max_bits": mach["t0_anchor"],
           "ok": mach["t0_anchor"] <= T0_ANCHOR_TOL}
    # stationary control (substitute; see DEVIATIONS): a repeated observable row
    # anchored at its own first row has algebraically zero excess -> zero events
    r_s = next((r for r in rows2 if r["r_ind"][str(HEADLINE_DELTA)] >= 2), rows2[-1])
    stat = []
    for d in DELTAS:
        chi_b = {l: (r_s["chi_closed_five"] if l in ("+x", "-x") else r_s["chi_wedge_four"])
                 for l in LABELS}
        Cs = {}
        if r_s["pair_classes"]:
            for k, cls in pair_class.items():
                Cs[k] = r_s["pair_classes"][cls]
        stat.append(sum(1 for _ in range(PERSIST_N)
                        if ns["r_ind"](chi_b, {l: 0.0 for l in LABELS},
                                       r_s["H_Z"], Cs, d)[0] >= 2))
    c01["stationary_control"] = {"event_counts": stat, "ok": stat == [0, 0, 0]}
    c01["ok"] = bool(c01["ok"] and c01["stationary_control"]["ok"])

    degrees = {"center": 6, "face": 5, "edge": 4, "corner": 3}
    cf002 = ns["centered_frobenius_panel"](LOW_FIELD_LAMBDA, degrees)
    comm_ok = max(v["Z"] for v in cf002.values()) < min(v["X"] for v in cf002.values())
    drift_ok = bool(h2 is None or h2["drift"] <= DRIFT_MAX)
    x_ok = all(not r["x_control"]["r_ind_ge2_possible"]
               for r in rows2 if "x_control" in r and r["jt"] <= DEADLINE_JT + 1e-12)
    c02 = {"commutator_ordering": bool(comm_ok), "drift": drift_ok,
           "x_pointer_control": bool(x_ok), "panel": cf002,
           "ok": bool(comm_ok and drift_ok and x_ok)}

    cr = {}
    for c in ("face", "edge", "corner"):
        cr[c] = next((r["jt"] for r in rows2 if r["one_site_excess"][c] >= EXCESS_MIN), None)
    inf = float("inf")
    order = [cr[c] if cr[c] is not None else inf for c in ("face", "edge", "corner")]
    locality_ok = order[0] <= order[1] <= order[2]
    c03 = {"lam002_first_hit_by_deadline": bool(h2 is not None and h2["by_deadline"]),
           "lam002_persistence_samples": None if h2 is None else h2["run"],
           "lam002_persists": headline_persists,
           "shell_crossings": cr, "locality": bool(locality_ok),
           "ok": bool(h2 is not None and h2["by_deadline"] and headline_persists and locality_ok)}

    # CHECK-03/04/05 with lambda = 0.02 folded into the 914 sampled window
    W_full = sorted(set(C914_EXPECT["W_sampled_914"]) | ({LOW_FIELD_LAMBDA} if lam002_in_W_full else set()))
    theta_star_all = dict(C914_EXPECT["theta_star"])
    if h2 is not None:
        theta_star_all["0.02"] = h2["theta"]
    tv = [v for k, v in theta_star_all.items() if v is not None and float(k) in W_full]
    field_factor = (max(tv) / min(tv)) if tv and min(tv) > 0 else None
    commissioned = [0.02, 0.05, 0.10, 0.20]
    certified = [l for l in commissioned if l in W_full]
    non_cert_above = [l for l in commissioned if l not in W_full and certified and l > max(certified)]
    bracket_above = [max(certified), min(non_cert_above)] if certified and non_cert_above else None
    non_cert_below = [l for l in commissioned if l not in W_full and certified and l < min(certified)]
    bracket_below = [max(non_cert_below), min(certified)] if certified and non_cert_below else None
    contiguous = certified == [l for l in commissioned
                               if min(certified) <= l <= max(certified)] if certified else False
    # NO categorical inside/outside label is emitted against the imported 0.20
    # convention. The numbers and the import's type are published, but that
    # convention is not used as a threshold in this finite-sample result.
    c05 = {"theta_star": theta_star_all, "W_full": W_full,
           "boundary_bracket_above": bracket_above,
           "boundary_bracket_below": bracket_below,
           "noncontiguous_window": (not contiguous),
           "imported_theta_convention_value": THETA_FLOOR,
           "imported_theta_convention_type": "unverified_imported_comparator_convention",
           "threshold_test_performed": False,
           "categorical_labels_emitted": False,
           "why_no_labels": "the 0.20 value is an unverified imported comparator convention. "
                            "This package reports theta values but does not use that convention "
                            "as a threshold, so it performs no threshold test and assigns no "
                            "inside/outside label. Any physical interpretation or baseline "
                            "reconciliation remains outside this finite-sample result",
           "theta_convention_role": "disclosure only; not used as a threshold",
           "field_factor": field_factor,
           "field_stability_ok": bool(field_factor is not None and field_factor < DELTA_FACTOR_MAX),
           "window_size_ok": bool(len(W_full) >= 2),
           "theta_floor_citation": "the landed Cycle 914 row types 0.20 as an unverified "
                                   "imported comparator convention; this package preserves that "
                                   "typing and performs no threshold test"}

    c2_outcome = ("SAMPLED-WINDOW-INCLUDES-0.02" if lam002_in_W_full
                  else "SAMPLED-WINDOW-EXCLUDES-0.02")
    c2_summary = {
        "outcome": c2_outcome,
        "lambda": LOW_FIELD_LAMBDA,
        "in_W_full": lam002_in_W_full,
        "first_hit": h2,
        "per_delta_first_hits": per_delta2,
        "all_deltas_by_deadline": all_deltas_hit_by_deadline,
        "headline_persists_3_samples": headline_persists,
        "W_full_after": W_full,
        "boundary_bracket_above": bracket_above,
        "boundary_bracket_below": bracket_below,
        "reading": ("at lambda = 0.02, on the sampled subgrid and under the imported cuts, the "
                    "certification predicate first holds by Jt <= 1 at every commissioned "
                    "tolerance and persists for the required number of consecutive samples, "
                    "reproducing the ALREADY-COMMITTED 2026-07-11 lambda = 0.02 stream.  This is "
                    "a reproduction of landed bounded support at one more field value, not a new "
                    "boundary result: nothing is claimed at unsampled fields or unsampled times"
                    if lam002_in_W_full else
                    "at lambda = 0.02 the sampled rows fail at least one clause of the imported "
                    "membership predicate; the sampled bracket is reported and nothing is claimed "
                    "at unsampled fields or unsampled times"),
    }

    # The Chebyshev truncation bound is a DECLARED ERROR BOUND of this run and
    # is gated with the rest of the machinery, not excluded from it.
    machinery_ok = all(v <= (CHEBY_TAIL_MAX if k == "cheby_tail" else MACH_TOL)
                       for k, v in mach.items())

    # ------------------------------------------------------------ digest ---
    table = {
        "low_field_rows": [{k: r[k] for k in sorted(r) if k not in ("bloch", "x_control")}
                           for r in rows2],
        "low_field_events": ev2,
        "late_time": c3,
        "check05": c05,
    }
    digest = sha256_bytes(json.dumps(table, sort_keys=True, default=repr).encode())

    wall = time.time() - T_START
    rssg = rss_gib()

    receipt = {
        "schema": "frontier-cycle915-comparator-recovery-v1",
        "cycle": 915,
        "date": "2026-07-28",
        "runner": "scripts/frontier_cycle915_comparator_recovery_2026_07_28.py",
        "boundary_sentences": BOUNDARY,
        "deviations": DEVIATIONS,
        "pins": pins,
        "ast_extraction": ast_meta,
        "restriction_gates_vs_landed_cycle914": gates,
        "protocol_input_roles": PROTOCOL_INPUT_ROLES,
        "low_field_certification": c2_summary,
        "low_field_rows": rows2,
        "low_field_reproduction_vs_committed_2026_07_11": repro,
        "late_time_probe": {"scope": c3_scope, "results": c3},
        "checks": {"CHECK-01": c01, "CHECK-02": c02, "CHECK-03": c03, "CHECK-05": c05},
        "falsifier_visibility": fal,
        "determinism": {"duplicate_time_requested": LOW_FIELD_DUP_T,
                        "propagated_state_bitwise_equal": dup_state_bitwise_equal,
                        "observable_scalars_bitwise_equal": bool(dup_obs_equal),
                        "pair_classes_bitwise_equal": bool(dup_pair_equal),
                        "ok": bool(dup_state_bitwise_equal and dup_obs_equal and dup_pair_equal)},
        "protocol": {"H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i", "J": 1, "N": 27,
                     "geometry": "open-3x3x3", "deltas": list(DELTAS),
                     "headline_delta": HEADLINE_DELTA, "deadline_jt": DEADLINE_JT,
                     "T_C_frozen": T_C_FROZEN,
                     "delta_memo_lambdas": [0.02, 0.05, 0.10, 0.20],
                     "delta_protocol_hash": PINS[DELTA_MEMO][0],
                     "parent_protocol_hash": PINS[PARENT_MEMO][0],
                     "fragment_descriptor_checksum": desc_sum,
                     "partition_preserving_proper_rotations": n_part_rots,
                     "pair_class_equivalence": "orbit equivalence under the "
                         "partition-preserving proper rotations only (%d of 24); the "
                         "declared partition is NOT closed under the full proper cubic "
                         "group and no such closure is claimed" % n_part_rots,
                     "theta_convention_import": {
                         "value": THETA_FLOOR,
                         "type": "unverified_imported_comparator_convention",
                         "role": "disclosure only; no threshold test is performed against it",
                         "interpretation_status": "outside this finite-sample result"}},
        "numerics": {"python": sys.version.split()[0], "numpy": np.__version__,
                     "route": "exact proper-cubic invariant-sector reduction (orbit basis) "
                              "+ Chebyshev expansion of exp(-iHt); float64/complex128 "
                              "(machinery AST-extracted from the LANDED Cycle 914 primary, "
                              "including its corrected operator-norm truncation bound)",
                     "sector_dimension": sec.n * 2, "basis_checksum": sec.checksum,
                     "basis_wall_s": basis_wall, "layout_wall_s": ol_wall,
                     "low_field_wall_s": c2_wall,
                     "late_time_wall_s": c3_wall,
                     "chebyshev": {"low_field": prop2},
                     "cheby_tail_bound_gate": CHEBY_TAIL_MAX,
                     "machinery": mach, "machinery_ok": bool(machinery_ok),
                     "peak_rss_gib": rssg, "wall_s": wall,
                     "result_table_sha256": digest},
        "verdict": None,
    }
    sampled_result = ("MACHINERY-FAIL" if not (machinery_ok and c01["ok"]
                                               and receipt["determinism"]["ok"] and fal["ok"])
                      else "LOW-FIELD-CERTIFIED" if lam002_in_W_full
                      else "LOW-FIELD-NOT-CERTIFIED")
    receipt["verdict"] = {"low_field_sampled_result": sampled_result,
                          "low_field_outcome": c2_outcome,
                          "late_time_sampled_labels": {l: c3[l]["sampled_label"] for l in c3},
                          "note": "outcome-neutral wiring: the low-field run lands certified-or-"
                                  "not and the late-time rows land certified-or-not AT THE TESTED "
                                  "SAMPLES; neither is a machinery condition and neither states "
                                  "anything about untested samples"}

    out_path = os.path.join(ROOT, "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json")
    with open(out_path, "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=str)

    print("GATES landed-914-restrictions=%s theta*=%s labels=%s bracket=%s "
          "sampled-window[914]=%s C55[lam=0.20,Jt=0.7]=%s panel-spot=%s ordering=%s %s"
          % (gates["ok"], json.dumps(receipt914["checks"]["CHECK-05"]["theta_star"]),
             json.dumps(receipt914["checks"]["CHECK-05"]["labels"]),
             gates["boundary_bracket_value_for_value"], gates["W_sampled_914"],
             gates["lam020_C55_observed"], gates["check02_panel_spot_verified"],
             gates["check02_ordering_holds"], BOUNDARY_LINE))
    print("CHECKS+MACHINERY CHECK-01=%s CHECK-02=%s CHECK-03[lam=0.02]=%s "
          "CHECK-05[window=%s bracket-above=%s bracket-below=%s field-factor=%s "
          "threshold-test-performed=False]=%s falsifier=%s determinism=%s "
          "MACHINERY=ok(%s, cheby-tail-gate=%.0e) %s"
          % (c01["ok"], c02["ok"], c03["ok"], W_full, bracket_above, bracket_below,
             None if field_factor is None else "%.9f" % field_factor,
             c05["window_size_ok"], fal["ok"], receipt["determinism"]["ok"],
             {k: "%.3g" % v for k, v in mach.items()}, CHEBY_TAIL_MAX, BOUNDARY_LINE))

    # ---- resolution certificate: what this run resolves, at what granularity --
    print("RESOLUTION-CERTIFICATE (granularity of every statement this run makes) %s"
          % BOUNDARY_LINE)
    print("per_element: each of the six declared fragments is evaluated separately at "
          "every executed grid time against the three imported certification conditions, "
          "and the certifying subset is recorded fragment by fragment.")
    print("per_site: single-site Holevo values and their excesses are resolved for the "
          "face, edge and corner site classes inside each fragment, giving the "
          "shell-resolved crossing order reported in CHECK-03.")
    print("per_mode: checked and not executed -- the frozen comparator declares one "
          "pointer observable (Z) with an X control basis and no normal-mode "
          "decomposition, so no per-mode resolution is defined and none is claimed.")
    print("per_block: the five declared fragment-pair classes are resolved as blocks "
          "through the conditional-mutual-information gate at every row where two or "
          "more fragments clear the singleton gates; skipped rows carry their reason.")
    print("lattice_wide: checked and not executed -- every number here is a finite, "
          "sampled, fixed-partition observation on the open 3x3x3 cube at the executed "
          "grid; no lattice-wide, continuum, all-times or limiting statement is made.")

    print("TOTAL %s low-field=%s(lambda=0.02 %s) late-time=%s theta*[0.02]=%s "
          "sampled-window=%s digest=%s wall=%.1fs rss=%.2fGiB %s"
          % (sampled_result, c2_outcome,
             "in the sampled window" if lam002_in_W_full else "not in the sampled window",
             json.dumps({l: c3[l]["sampled_label"] for l in c3}),
             None if h2 is None else h2["theta"], W_full,
             digest[:16], wall, rssg, BOUNDARY_LINE))
    sys.stdout.flush()
    sys.exit(0 if sampled_result != "MACHINERY-FAIL" else 2)


if __name__ == "__main__":
    main()
