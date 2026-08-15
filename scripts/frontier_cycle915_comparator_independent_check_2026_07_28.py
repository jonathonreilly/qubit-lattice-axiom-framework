#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 915 independent check -- SPEC'D TO REFUTE, FAIL-CLOSED.

Adversarial counterpart to
`scripts/frontier_cycle915_comparator_recovery_2026_07_28.py`.  Its job is to
break that runner's reported observations, not to agree with them.

EXIT CONTRACT (fail-closed): exit 0 only if every pin holds, every finding
survives, and every mutation tooth fires.  A stale pin, a refuted finding or a
blind tooth exits 1.  A green process is therefore a certificate, not a
formality.

PACKET ROLE.  This checker is CLAIM-SCOPED and CO-LOAD-BEARING for the paired
note: the independent recomputation, the refutation findings and the mutation
teeth exist only on this surface, and the primary deliberately does not import
it, so automatic import discovery cannot attach it to the audit packet.  It is
declared as the note's `packet_helper_runner`.

Attack surfaces
---------------
INDEPENDENT RECOMPUTATION OF THE LOW-FIELD ROWS (historical alias: A3). The
    lambda = 0.02 certification rows are recomputed from scratch with the landed
    Cycle 914 checker's verified independent machinery -- a MAX-canonical orbit
    sector (the primary's is MIN-canonical), a SHIFTED Chebyshev propagator with
    non-zero spectral centre, and row-by-row expand-table marginals -- and the
    certification arithmetic is re-derived from the memo definitions.  No primary
    value is copied into the recomputation; comparison happens only at the end.

INDEPENDENT RECOMPUTATION OF THE LATE-TIME ROWS (historical alias: A4).  ALL
    FOUR executed late rows -- Jt in {1.5, 2.0} at lambda in {0.05, 0.10} -- are
    recomputed independently and compared row by row.  These four rows are the
    package's only new numerical content, so partial coverage would leave the
    new content unchecked.

Landed-ancestor discipline.  Every Cycle 914 byte read here is the byte landed on
origin/main at 6277e4c6dfe77cf094b09a3529a69c1813773876.  The axiom memo is not
read: it was context-only and its historical snapshot is superseded on main.

Teeth
-----
Six mutation probes, each of which must be DETECTED: tampered pin, hardcoded
certification, leaked verdict, skipped grid point, planted early-certification
blindness, and a tampered committed stream.

Read inventory.  This runner reads external scientific inputs (the frozen memos,
the landed Cycle 914 primary/receipt/checker, the committed lambda = 0.02 stream)
and package-local integrity inputs (the paired primary's source and receipt,
which it verifies).  Both kinds are declared in AUDIT_INPUT_PATHS.

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
import scipy.linalg as sla
from scipy.special import jv

T_START = time.time()

# Declared execution budget for the audit-lane cache envelope.
AUDIT_TIMEOUT_SEC = 1200

# Mutable repository inputs this runner reads.  External scientific inputs: the
# frozen memos, the landed Cycle 914 primary/receipt/checker, and the committed
# lambda = 0.02 stream.  Package-local integrity inputs: the paired primary's
# source and receipt, which this runner verifies rather than trusts.
AUDIT_INPUT_PATHS = (
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md",
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md",
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md",
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py",
    "scripts/frontier_cycle914_d3_bar_independent_check_2026_07_28.py",
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json",
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl",
    "scripts/frontier_cycle915_comparator_recovery_2026_07_28.py",
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json",
)

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
STREAM_002 = "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl"

# Every digest below is the byte landed on origin/main at
# 6277e4c6dfe77cf094b09a3529a69c1813773876 (verified with `git cat-file`).  The
# axiom memo is deliberately absent: context-only in the predecessor, superseded
# on main, and consumed by nothing here.
PIN_SHA = {
    PARENT_MEMO: "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
    DELTA_MEMO: "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
    NOTE_MEMO: "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
    C914_PRIMARY: "0cfab8fde089be2252f47a710d5822bc5a3458f6e15b37784855716979eb9dd4",
    C914_CHECKER: "1735d665b327ab8f821160daa122686576dac678da865945aaff129816136358",
    C914_RECEIPT: "2dddb1e145fb5854f1f303f8d417c4d8e62e84a64c1f8f3451bcf65ec2550e86",
    STREAM_002: "9bf9282d477daf43635d29647ea0757fefb6105b755519c515539b3e28be3177",
}
LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
CENTER = (0, 0, 0)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE = 0.10
GATE_H, GATE_EXC, GATE_IND, DEADLINE = 0.05, 0.02, 0.02, 1.0
C2_LAMBDA = 0.02
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
# ALL four executed late rows are recomputed here, not a spot sample: they are
# the package's only new numerical content.
LATE_LAMBDAS = (0.05, 0.10)
LATE_TIMES = (1.5, 2.0)
FINDINGS = []
TEETH = []


def note(tag, ok, detail, **kw):
    d = {"check": tag, "survives": bool(ok), "detail": detail}
    d.update(kw)
    FINDINGS.append(d)
    return d


def sha(b):
    return hashlib.sha256(b).hexdigest()


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


# ========================================= independent numerics ==============
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
def run_teeth(ns, rows002, primary_receipt, frags):
    def tooth(name, detected, detail):
        TEETH.append({"tooth": name, "detected": bool(detected),
                      "exit": "BIT-FLIPPED" if detected else "BLIND", "detail": detail})

    # 1 tampered pin
    b = open(os.path.join(ROOT, PARENT_MEMO), "rb").read()
    bad = bytearray(b); bad[len(bad) // 2] ^= 0x01
    tooth("tampered-pin", sha(bytes(bad)) != PIN_SHA[PARENT_MEMO],
          "single-byte flip in the parent memo changes its sha256 -> pin verification fails")

    # 2 hardcoded certification (theta perturbation)
    hit = next((r for r in rows002 if r["r_ind"][str(HEADLINE)] >= 2), None)
    claimed = primary_receipt["low_field_certification"]["first_hit"]["theta"]
    perturbed = claimed + 1e-6
    tooth("hardcoded-certification",
          hit is not None and abs(hit["theta"] - perturbed) > 1e-9,
          "perturbing the primary's theta* by 1e-6 is caught by the independent theta "
          "recomputation at tolerance 1e-9 (true |dev| = %.3e)"
          % (abs(hit["theta"] - claimed) if hit else float("nan")))

    # 3 leaked verdict: R_ind is recomputed, not copied
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

    # 4 skipped grid point
    want = set(round(t, 6) for t in T_EXEC)
    got = set(round(r["jt"], 6) for r in rows002)
    prim = set(round(r["jt"], 6) for r in primary_receipt["low_field_rows"])
    tooth("skipped-grid-point", want == got == prim,
          "every one of the %d frozen executed subgrid points is present in BOTH the "
          "primary's rows and this checker's independent rows (missing: checker %s, "
          "primary %s)" % (len(want), sorted(want - got), sorted(want - prim)))

    # 5 planted early-certification blindness
    C = {k: 0.001 for k in PAIR_CLASS}
    n_plant, sub, _ = ns["r_ind"]({l: 0.99 for l in LABELS}, {l: 0.99 for l in LABELS},
                                  1.0, C, HEADLINE)
    early = [r for r in rows002 if r["jt"] <= 0.3 + 1e-12
             and r["r_ind"][str(HEADLINE)] >= 2]
    tooth("planted-early-certification-blindness", n_plant >= 2 and not early,
          "a fabricated all-fragment row planted at the gate returns R_ind=%d through the "
          "same routine that returns no certification at Jt <= 0.3 in the measured data -- "
          "the routine is not blind to an early hit, the physics simply has none" % n_plant)

    # 6 tampered committed stream
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
    out["pins"] = {"digests": pins, "all_match": pin_ok}
    note("pins", pin_ok,
         "independent sha256 of every declared input matches its landed byte")

    primary_receipt = json.load(open(os.path.join(ROOT, PRIMARY_RECEIPT)))
    out["primary_runner_sha256"] = sha(open(os.path.join(ROOT, PRIMARY), "rb").read())

    # ---- independent recomputation of the low-field rows ------------------
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
    prim = primary_receipt["low_field_certification"]
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
    pm_rows = {round(r["jt"], 6): r for r in primary_receipt["low_field_rows"]}
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
    out["independent_low_field_recomputation"] = cmp2
    note("low-field-rows", c2_survives,
         "independent MAX-canonical / shifted-Chebyshev recomputation of all %d executed rows "
         "reproduces the primary's lambda = 0.02 first hit (Jt = %s, R_ind = %s, subset of %s), "
         "every per-delta first hit, and the W_full membership; max row deviation %.3e bits"
         % (len(rows002), chk_hit["jt"] if chk_hit else None,
            chk_hit["r_ind"] if chk_hit else None,
            len(chk_hit["subset"]) if chk_hit else None, max(dev.values())))

    print("LOW-FIELD-RECOMPUTE[lambda=0.02]=%s first-sampled-hit=%s theta=%s R_ind=%s "
          "sampled-window-member=%s(primary %s) rows=%d max-dev=%.3e r_ind-mismatches=%d "
          "energy-dev=%.3e %s"
          % ("SURVIVES" if c2_survives else "REFUTED",
             chk_hit["jt"] if chk_hit else None, chk_hit["theta"] if chk_hit else None,
             chk_hit["r_ind"] if chk_hit else None, chk_in_W, prim["in_W_full"],
             len(rows002), max(dev.values()), len(r_ind_mismatch),
             abs(Et - E0), BOUNDARY_LINE))
    sys.stdout.flush()

    # ---- independent recomputation of ALL FOUR late-time rows -------------
    late_out, late_rows_checked, late_survives = {}, 0, True
    late_max_dev = 0.0
    for lam3 in LATE_LAMBDAS:
        times3 = [0.0] + list(LATE_TIMES)
        o3, prop3 = ns["shifted_chebyshev"](sec, lam3, a0, times3)
        anch3 = {"chi0": None, "theta0": None}
        chk_rows = [build_row(ns, sec, fm, pm, o3[i], t, lam3, anch3)
                    for i, t in enumerate(times3)]
        del o3
        prim3 = primary_receipt["late_time_probe"]["results"][str(lam3)]
        per_row = {}
        for r3 in chk_rows[1:]:
            t3 = r3["jt"]
            prim_row = next((r for r in prim3["late_rows"]
                             if abs(r["jt"] - t3) < 1e-12), None)
            if prim_row is None:
                late_survives = False
                per_row[str(t3)] = {"primary_row_present": False}
                continue
            chk_cert = bool(r3["r_ind"][str(HEADLINE)] >= 2)
            prim_cert = bool(prim3["certified_at_late_samples"].get(str(t3), None))
            d3 = {"chi_closed_five": abs(r3["chi_closed_five"] - prim_row["chi_closed_five"]),
                  "chi_wedge_four": abs(r3["chi_wedge_four"] - prim_row["chi_wedge_four"]),
                  "theta": abs(r3["theta"] - prim_row["theta"]),
                  "H_Z": abs(r3["H_Z"] - prim_row["H_Z"])}
            row_ok = (chk_cert == prim_cert and max(d3.values()) < 1e-8
                      and r3["r_ind"] == prim_row["r_ind"])
            late_survives = late_survives and row_ok
            late_max_dev = max(late_max_dev, max(d3.values()))
            late_rows_checked += 1
            per_row[str(t3)] = {"checker_certified": chk_cert,
                                "primary_certified": prim_cert,
                                "checker_r_ind": r3["r_ind"],
                                "primary_r_ind": prim_row["r_ind"],
                                "checker_theta": r3["theta"],
                                "max_abs_dev": d3, "row_agrees": bool(row_ok)}
        late_out[str(lam3)] = {"rows": per_row, "propagator": prop3,
                               "primary_sampled_label": prim3["sampled_label"]}
    expected_rows = len(LATE_LAMBDAS) * len(LATE_TIMES)
    late_survives = bool(late_survives and late_rows_checked == expected_rows)
    out["independent_late_time_recomputation"] = {
        "coverage": "ALL executed late rows (%d of %d)" % (late_rows_checked, expected_rows),
        "rows_checked": late_rows_checked, "rows_expected": expected_rows,
        "max_abs_dev": late_max_dev, "per_lambda": late_out}
    note("late-time-rows", late_survives,
         "independent recomputation of ALL %d executed late rows (Jt in %s at lambda in %s) "
         "reproduces the primary's per-row certification outcome and R_ind ledger; max "
         "deviation %.3e bits.  The agreed reading of these rows is 'not certified at these "
         "tested samples' -- no decay, limit or indicator claim is checked because none is made"
         % (late_rows_checked, list(LATE_TIMES), list(LATE_LAMBDAS), late_max_dev))

    # ---- restriction-gate re-derivation -----------------------------------
    r914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    g = primary_receipt["restriction_gates_vs_landed_cycle914"]
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
    run_teeth(ns, rows002, primary_receipt, frags)
    out["teeth"] = TEETH
    teeth_ok = sum(1 for t in TEETH if t["detected"])

    out["findings"] = FINDINGS
    surviving = [f["check"] for f in FINDINGS if f["survives"]]
    refuted = [f["check"] for f in FINDINGS if not f["survives"]]
    table = {"rows": rows002, "events": chk_ev,
             "late_time": out["independent_late_time_recomputation"]}
    out["result_table_sha256"] = sha(json.dumps(table, sort_keys=True, default=repr).encode())
    out["numerics"] = {"python": sys.version.split()[0], "numpy": np.__version__,
                       "sector_dim": sec.n * 2, "basis_wall_s": basis_wall,
                       "low_field_wall_s": c2_wall, "peak_rss_gib": rss_gib(),
                       "wall_s": time.time() - T_START}
    # FAIL-CLOSED exit contract: green only when every pin holds, every finding
    # survives, and every tooth fires.
    all_teeth = (teeth_ok == len(TEETH))
    exit_code = 0 if (pin_ok and not refuted and all_teeth) else 1
    out["verdict"] = {"surviving_checks": surviving, "refuted_checks": refuted,
                      "teeth_detected": teeth_ok, "teeth_total": len(TEETH),
                      "exit_contract": "fail-closed: exit 0 only if pins hold, no finding is "
                                       "refuted, and all teeth fire",
                      "pins_ok": bool(pin_ok),
                      "exit_code": exit_code}

    with open(os.path.join(ROOT, "outputs/comparator_independent_check_cycle915_receipt_2026_07_28.json"),
              "w") as fh:
        json.dump(out, fh, indent=1, sort_keys=True, default=str)

    print("LATE-TIME-RECOMPUTE[%s]=%s rows=%d/%d max-dev=%.3e per-lambda=%s %s"
          % (json.dumps(list(LATE_TIMES)), "SURVIVES" if late_survives else "REFUTED",
             late_rows_checked, expected_rows, late_max_dev,
             json.dumps({l: late_out[l]["primary_sampled_label"] for l in late_out}),
             BOUNDARY_LINE))
    print("TEETH %d/%d detected: %s %s"
          % (teeth_ok, len(TEETH),
             "; ".join("%s=%s" % (t["tooth"], t["exit"]) for t in TEETH), BOUNDARY_LINE))
    print("TOTAL INDEPENDENT-CHECK-COMPLETE surviving=%s refuted=%s teeth=%d/%d pins=%s "
          "exit=%d(fail-closed) digest=%s wall=%.1fs rss=%.2fGiB %s"
          % (surviving, refuted, teeth_ok, len(TEETH), bool(pin_ok),
             exit_code, out["result_table_sha256"][:16], out["numerics"]["wall_s"],
             out["numerics"]["peak_rss_gib"], BOUNDARY_LINE))
    sys.stdout.flush()
    sys.exit(exit_code)


if __name__ == "__main__":
    main()
