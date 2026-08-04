#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 915 -- comparator recovery (C1), the delta-memo lambda = 0.02 run (C2),
and the late-grid persistence probe (C3).

Successor to Cycle 914
(`scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py`), which reproduced
the committed d = 3 registration-bar measurement on the parent memo's
commissioned lambda set {0.05, 0.10, 0.20} over Jt in {0.0, ..., 1.2} and pinned
six cited-but-absent predecessor artifacts AS ABSENT.  This runner does three
things the 914 block explicitly left open.

C1  RECOVERY.  For each cited-but-absent predecessor: hunt the repository's git
    history read-only, disclose every command, and deliver either a FOUND
    provenance chain (added when/where, whether ever on a landed branch, why it
    is absent from the working tree, the recovered content's sha256, and its
    load-bearing claims) or exhaustive GENUINELY-ABSENT evidence.  The priority
    target is the d = 1 comparator note, because Cycle 914's own stdout labels
    the CHECK-05 comparison floor `d1-comparator-floor=0.20`.  Nothing is
    restored into the tree; the recovery is emitted as data plus a landing
    recommendation for the audit lane.

C2  THE DELTA-MEMO lambda = 0.02 RUN.  `docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md`
    Delta 1 commissions `lambda in {0.02, 0.05, 0.10, 0.20}`.  Cycle 914 ran the
    parent set only and recorded the omission as its LAMBDA-SET deviation.  This
    runner executes the frozen protocol at lambda = 0.02 on the certification
    subgrid: the three-condition certification per fragment per grid time, the
    first certified time (or its absence) by Jt <= 1, the disjoint-pair witness,
    C_ab on the subgrid, and the CHECK-gate outcomes.  The result either extends
    the certified window below lambda = 0.05 or brackets a LOWER boundary.

C3  THE LATE GRID.  The frozen certification subgrid T_C carries four late
    samples {1.5, 2.0, 5.0, 10.0} that Cycle 914 did not execute.  This runner
    executes the declared priority tier -- Jt in {1.5, 2.0} at BOTH certified
    lambdas {0.05, 0.10} -- and reports persistence or decay in the design's own
    semantics.  The remaining tier {5.0, 10.0} is NOT executed under the runtime
    cap and is disclosed as such.

Machinery.  The sector reduction, Chebyshev propagator, marginal reconstruction,
certification and commutator routines are AST-EXTRACTED from the Cycle 914
primary (whose exactness against full space was verified by the Cycle 914
independent checker) rather than reimplemented; the extraction is byte-pinned
and the extracted source's sha256 is reported.

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
from scipy.special import jv

T_START = time.time()

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = "| " + " | ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ============================================================== pins =========
# (path -> (sha256, git blob sha1)).  Hard-fail exit 2 on any mismatch.
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
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
        "4a863da1f3f255354839277271a3a69a5c205133"),
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py": (
        "fc7344a06503f9c159ea732cb6f622a23e61196e370914943ffd9a468fd592e4",
        "e0639e0b5d1ebdd995c4c7ec3255f8daeeb4fe0c"),
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl": (
        "9bf9282d477daf43635d29647ea0757fefb6105b755519c515539b3e28be3177",
        "6a3588d9a99efd6e704a1bff0127815995aa1fb4"),
}

# Comparator baselines the frozen memos cite but which are NOT in this tree.
# Pinned AS ABSENT exactly as Cycle 914 pinned them; C1 supplies the git-history
# provenance for each.  Present-in-tree is a hard failure (the pin is the claim).
CITED_ABSENT = [
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md",   # d=1 comparator note
    "docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md",
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md",
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md",
    "scripts/d3_registration_onset_pilot_2026_07_09.py",               # predecessor runner
    "scripts/d3_bar_location_measurement_2026_07_10.py",               # predecessor runner
]

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
WINDOW_NOTE = "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md"
C914_PRIMARY = "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
STREAM_002 = "logs/runner-cache/d3_bar_window_checkpoints/lam_0p02_observables.jsonl"

# ------------------------------------------------------ frozen protocol ------
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05                     # certification condition 1
EXCESS_MIN = 0.02                        # certification condition 3
INDEP_MAX = 0.02                         # certification condition 4 / C_ab gate
T0_ANCHOR_TOL = 1e-9                     # CHECK-01
DRIFT_MAX = 0.10                         # CHECK-02
PERSIST_N = 3                            # CHECK-03
DELTA_FACTOR_MAX = 1.5                   # CHECK-04
THETA_FLOOR = 0.20                       # CHECK-05 declared comparison floor
MACH_TOL = 1e-9
LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
X_CONTROL_MAX_JT = 1.0
CENTER = (0, 0, 0)

# ------------------------------------------------- executed scope (C2/C3) ----
C2_LAMBDA = 0.02                                            # delta-memo Delta 1
C2_TIMES = [round(0.1 * i, 10) for i in range(13)]          # 0.0 .. 1.2
C2_DUP_T = 0.6            # requested twice in one propagation -> determinism gate
C3_LAMBDAS = (0.05, 0.10)                                   # the 914-certified pair
C3_TIMES = [1.5, 2.0]                                       # declared priority tier 1
C3_NOT_EXECUTED = [5.0, 10.0]                               # tier 2, not afforded
T_C_FROZEN = [round(0.1 * i, 10) for i in range(13)] + [1.5, 2.0, 5.0, 10.0]

DEVIATIONS = [
    "EXECUTED-SCOPE-C2: lambda = 0.02 executed on the frozen certification subgrid "
    "restricted to Jt in {0.0, ..., 1.2} (13 of the 17 T_C points).  The frozen main "
    "state grid Jt = 0:0.1:10 is NOT executed.  Identical restriction to Cycle 914's "
    "EXECUTED-GRID deviation, and for the same reason: the 900 s runtime cap against a "
    "frozen schedule that projects 7.1 h.  The deadline gate (Jt <= 1) and the "
    "three-consecutive-sample persistence gate both live entirely inside the executed "
    "window, so no CHECK-03 outcome depends on the omission.",

    "EXECUTED-SCOPE-C3: the frozen late certification samples are {1.5, 2.0, 5.0, 10.0}.  "
    "This run executes the declared priority tier {1.5, 2.0} at BOTH certified lambdas "
    "{0.05, 0.10}; {5.0, 10.0} are NOT executed at either lambda.  Reason: the Chebyshev "
    "degree scales with A * t_max (A = 54 + 27 lambda), so t_max = 10 costs M = 662 "
    "matrix-vector products per lambda against M = 169 for t_max = 2.0 -- roughly 491 s "
    "versus 125 s per lambda, which does not fit beside C2 under the 900 s cap.  The "
    "frozen memo classes all four late samples as recurrence diagnostics that 'do not "
    "rescue CHECK-03', so no gate consumes them.",

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
    "commutator routines are AST-extracted from the Cycle 914 primary rather than "
    "reimplemented.  This is deliberate: it makes C2/C3 a scope extension of a verified "
    "implementation rather than a second implementation with its own error surface.  The "
    "INDEPENDENT recomputation lives in the paired checker, which reimplements the "
    "certification arithmetic from the memos.",

    "C1-SEARCH-DISCLOSURE: the pickaxe searches that located the theta-floor provenance "
    "chain (`git log --all -S '<phrase>'`) cost minutes of wall clock over 36,832 "
    "commits and are NOT re-executed inside the runtime cap.  They are disclosed verbatim "
    "as the discovery route; this runner re-verifies their RESULT by cheap path-scoped "
    "commands (git log --all --diff-filter=A -- <path>, git rev-parse, git cat-file), and "
    "the paired checker re-derives the same chain by its own path-scoped route.",
]

# =========================================== Cycle 914 restriction constants ==
# Headline rows this block must reproduce value-for-value out of the 914 receipt.
C914_EXPECT = {
    "theta_star": {"0.05": 0.5007515272813331, "0.1": 0.5047307768675429, "0.2": None},
    "labels": {"0.05": "inside", "0.1": "inside", "0.2": None},
    "median": 0.502741152074438,
    "boundary_bracket": [0.1, 0.2],
    "event_jt": {"0.05": 0.6, "0.1": 0.7, "0.2": None},
    "lam020_opposite55_at_content_peak": 0.060394807359658895,
    "lam020_content_peak_jt": 0.7,
    "W_full_914": [0.05, 0.1],
    "verdict_parent": "BAR-NOT-PINNED",
    "verdict_delta": "BAR-DERIVED-EFFECTIVE",
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


def git(*args, check=True):
    """Read-only git.  Returns (cmd, rc, stdout).  Never mutates the tree."""
    cmd = ["git"] + list(args)
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True)
    if check and p.returncode not in (0, 1):
        die("git:%s rc=%d %s" % (" ".join(args)[:80], p.returncode, p.stderr[:120]))
    return {"cmd": "git " + " ".join(args), "rc": p.returncode, "out": p.stdout.rstrip("\n")}


def verify_pins():
    """Present pins: byte-exact.  Absent pins: must be absent.  Hard-fail exit 2."""
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
    absent = {}
    for path in CITED_ABSENT:
        present = os.path.exists(os.path.join(ROOT, path))
        if present:
            die("pin-absent:PRESENT %s (the absence pin is the claim)" % path)
        absent[path] = "absent"
    return out, absent


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


# =================================================== C1: the recovery ========
# Discovery route (disclosed; the expensive pickaxe searches are NOT re-run here
# -- see the C1-SEARCH-DISCLOSURE deviation).  Each artifact is re-verified by
# cheap path-scoped commands executed live below.
C1_TARGETS = [
    ("docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md",
     "d18851afa90adc22c160a1b413fe01c30a470abd", "PRIORITY: the d=1 comparator note"),
    ("docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md",
     "a68d73320540f952be9e92907bf0dde1ad8a22f6", "the d=3 pilot design scout"),
    ("docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md",
     "9a91be0d6ead36ce773b497ef5ce7486bc600b50", "the single-qubit pilot negative"),
    ("docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md",
     "44928e54bbbc2caae0c3f6ae1dae01fcc77a35ea", "the route-C pilot conclusion (PR #5144)"),
    ("scripts/d3_registration_onset_pilot_2026_07_09.py",
     "ce95a77e851be6e46851cf2e7f3a740b74e8b96a", "predecessor runner (pilot)"),
    ("scripts/d3_bar_location_measurement_2026_07_10.py",
     "6591b2360ea2ec0fed365110761e6b61cf1e1585", "predecessor runner (route C)"),
]

# The theta-floor provenance chain, discovered by pickaxe and re-verified here.
THETA_FLOOR_CHAIN = [
    ("docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md",
     "8f75f76ca28b50748f2398f5339babf93c3fde19",
     "record-deposition-rate block01 -- where theta >= 0.2 is MEASURED"),
    ("docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md",
     "ed5105ecf4e9e83ca9694e0222f9428aabc528cb",
     "record-deposition-rate block03 -- the campaign's own restatement of the floor"),
]

# Load-bearing extraction targets: (label, regex) applied to recovered bytes.
CLAIM_PATTERNS = {
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md": [
        ("bar_statement", r"The permanence bar \(R >= 2\) never fires[^\n]*\n(?:[^\n]*\n){0,2}"),
        ("theta_floor_deferral", r"the\s+quantitative bar location[\s\S]{0,260}?unmeasured here\."),
        ("verdict", r"TOTAL: ([A-Z\-]+), exit (\d)"),
        ("structural", r"Redundancy at permanence grade[\s\S]{0,200}?geometry\."),
    ],
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md": [
        ("theta_reading", r"Where the bar can be read[\s\S]{0,300}?margin\."),
        ("lam020_mechanism", r"C_55 = [\d\. /]+bits across\n?lambda = [\d\. /]+\."),
        ("verdict", r"the honest TOTAL is BAR-NOT-PINNED"),
        ("named_successor", r"Named successor[\s\S]{0,600}?window this run measured\."),
    ],
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md": [
        ("negative", r"\*\*No certified registration anywhere\.\*\*[\s\S]{0,420}?unavailable\."),
        ("below_window_flag", r"The BAR-BELOW-WINDOW flag[\s\S]{0,160}?no onset\."),
        ("theta_convention", r"theta\(t\) = mean over the six center bonds[^\n]*\n[^\n]*"),
    ],
    "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md": [
        ("floor_origin", r"the\n?registration cascade is transient-complete above the threshold floor\n?\(theta >= 0\.2\)[\s\S]{0,200}?a finding\)"),
        ("sparse_window", r"DEPOSITION-SPARSE WINDOW IS NON-EMPTY[\s\S]{0,160}?units\."),
        ("theta_definition", r"registration = upward\n?crossing of the EXCESS distinguishability[\s\S]{0,140}?threshold theta"),
    ],
    "docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md": [
        ("floor_restatement", r"Below a\s+threshold of about 0\.2[\s\S]{0,340}?free\s+function\."),
    ],
}


def c1_recover():
    """Per-artifact provenance chain from git history.  Read-only; nothing restored."""
    main_tip = git("rev-parse", "origin/main")["out"]
    head = git("rev-parse", "HEAD")["out"]
    n_refs = len(git("for-each-ref", "--format=%(refname)")["out"].splitlines())
    n_commits = git("rev-list", "--all", "--count")["out"]
    out = {"repo": {"origin_main_tip": main_tip, "head": head,
                    "refs_searched": n_refs, "commits_reachable": int(n_commits or 0)},
           "artifacts": {}, "theta_floor_chain": {}, "commands": []}

    def record(d):
        out["commands"].append(d)
        return d

    def one(path, add_commit_hint, role):
        rec = {"role": role, "verdict": None, "commands": []}

        c = record(git("cat-file", "-e", "HEAD:%s" % path, check=False))
        rec["commands"].append(c["cmd"])
        rec["in_tree_at_head"] = (c["rc"] == 0)

        c = record(git("log", "--all", "--diff-filter=A",
                       "--format=%H %ci %s", "--", path))
        rec["commands"].append(c["cmd"])
        adds = [l for l in c["out"].splitlines() if l.strip()]
        rec["add_commits"] = adds

        c = record(git("log", "--all", "--diff-filter=D", "--format=%H %ci %s", "--", path))
        rec["commands"].append(c["cmd"])
        rec["delete_commits"] = [l for l in c["out"].splitlines() if l.strip()]

        c = record(git("log", "--all", "--diff-filter=R", "--find-renames",
                       "--format=%H %ci %s", "--", path))
        rec["commands"].append(c["cmd"])
        rec["rename_commits"] = [l for l in c["out"].splitlines() if l.strip()]

        if not adds:
            rec["verdict"] = "GENUINELY-ABSENT"
            rec["absence_evidence"] = {
                "refs_searched": n_refs, "commits_reachable": int(n_commits or 0),
                "add_commits": 0, "note": "no addition of this exact path anywhere in --all"}
            return rec

        commit = adds[0].split()[0]
        if add_commit_hint and not any(l.startswith(add_commit_hint[:12]) for l in adds):
            rec["hint_mismatch"] = "expected %s among adds" % add_commit_hint[:12]
        # provenance
        c = record(git("merge-base", "--is-ancestor", commit, "origin/main", check=False))
        rec["commands"].append(c["cmd"])
        rec["ancestor_of_origin_main"] = (c["rc"] == 0)

        c = record(git("merge-base", "--is-ancestor", commit, "HEAD", check=False))
        rec["commands"].append(c["cmd"])
        rec["ancestor_of_head"] = (c["rc"] == 0)

        c = record(git("branch", "-a", "--contains", commit))
        rec["commands"].append(c["cmd"])
        branches = sorted(x.strip().lstrip("* ").strip() for x in c["out"].splitlines() if x.strip())
        rec["branches_containing"] = branches

        c = record(git("log", "-1", "--format=%H%n%an%n%ci%n%s", commit))
        rec["commands"].append(c["cmd"])
        meta = c["out"].splitlines()
        rec["add_commit"] = {"sha": meta[0], "author": meta[1] if len(meta) > 1 else None,
                             "date": meta[2] if len(meta) > 2 else None,
                             "subject": meta[3] if len(meta) > 3 else None}

        # recovered content (read-only)
        c = record(git("rev-parse", "%s:%s" % (commit, path)))
        rec["commands"].append(c["cmd"])
        blob = c["out"].strip()
        p = subprocess.run(["git", "cat-file", "blob", blob], cwd=ROOT, capture_output=True)
        rec["commands"].append("git cat-file blob %s" % blob[:12])
        body = p.stdout
        rec["recovered"] = {"blob": blob, "bytes": len(body), "sha256": sha256_bytes(body)}

        # distinct blob variants across history
        c = record(git("log", "--all", "--format=%H", "--", path))
        rec["commands"].append(c["cmd"])
        variants = set()
        for cc in c["out"].splitlines():
            r = git("rev-parse", "%s:%s" % (cc.strip(), path), check=False)
            if r["rc"] == 0:
                variants.add(r["out"].strip())
        rec["distinct_blob_variants"] = sorted(variants)

        # landing verdict
        if rec["ancestor_of_origin_main"]:
            why = "landed-then-removed" if rec["delete_commits"] else "on-main-unexpectedly"
        elif rec["delete_commits"]:
            why = "never-landed-and-deleted-on-its-own-branch"
        else:
            why = "never-landed"
        rec["absent_from_main_because"] = why
        rec["verdict"] = "FOUND"

        # load-bearing claims
        txt = body.decode("utf-8", "replace")
        claims = {}
        for label, pat in CLAIM_PATTERNS.get(path, []):
            m = re.search(pat, txt)
            claims[label] = m.group(0).strip() if m else None
        rec["load_bearing_claims"] = claims
        return rec

    for path, hint, role in C1_TARGETS:
        out["artifacts"][path] = one(path, hint, role)
    for path, hint, role in THETA_FLOOR_CHAIN:
        out["theta_floor_chain"][path] = one(path, hint, role)
    return out


def c1_theta_floor_verdict(rec):
    """Decide how the 0.20 comparison floor may be cited, from recovered bytes."""
    d1 = rec["artifacts"]["docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md"]
    dep = rec["theta_floor_chain"].get(
        "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md", {})
    d1c = d1.get("load_bearing_claims") or {}
    depc = dep.get("load_bearing_claims") or {}

    deferral = d1c.get("theta_floor_deferral")
    d1_defers = bool(deferral and "unmeasured here" in deferral and "DEFERRED" in deferral)
    dep_measures = bool(depc.get("floor_origin") and "theta >= 0.2" in depc["floor_origin"])

    # what the in-tree window note itself says about the floor's status
    wtxt = open(os.path.join(ROOT, WINDOW_NOTE), "rb").read().decode()
    declared_import = "the theta observable and its `0.20` declared comparison floor" in wtxt
    import_header = "supplied inputs rather than derived conclusions" in wtxt

    # what the 914 primary calls it
    ptxt = open(os.path.join(ROOT, C914_PRIMARY), "rb").read().decode()
    c914_label = "d1-comparator-floor" in ptxt

    if d1_defers and dep_measures:
        origin = "record-deposition-rate comparator (2026-07-08 block01), NOT the d=1 registration note"
        kind = "MEASURED-IN-A-DIFFERENT-COMPARATOR-THEN-IMPORTED-AS-A-DECLARED-FLOOR"
    elif dep_measures:
        origin = "record-deposition-rate comparator (2026-07-08 block01)"
        kind = "MEASURED-ELSEWHERE"
    elif d1_defers:
        origin = "unlocated; the d=1 note explicitly defers the comparison"
        kind = "DECLARED-WITHOUT-LOCATED-SOURCE"
    else:
        origin = "unresolved"
        kind = "UNRESOLVED"

    return {
        "question": "does theta >= 0.20 come from a d=1 measurement, a convention, or a design choice?",
        "answer_kind": kind,
        "origin": origin,
        "d1_note_defers_the_comparison": d1_defers,
        "d1_note_deferral_quote": deferral,
        "deposition_note_measures_the_floor": dep_measures,
        "deposition_note_quote": depc.get("floor_origin"),
        "deposition_theta_definition_quote": depc.get("theta_definition"),
        "d3_theta_definition": "theta(t) = (1/6) sum_a ([1 - Tr rho_(S,a)(t)^2] - [same trajectory's t=0 value]); "
                               "the d=3 subtrahend is EXACTLY ZERO for the verified product preparation",
        "observables_are_not_the_same": True,
        "observables_note": "the deposition-comparator theta subtracts a per-bond interacting-ground-state "
                            "baseline of 0.27-0.49; the d=3 theta subtracts the trajectory's own t=0 value, "
                            "which the frozen memo verifies to be zero.  The two thetas share a NAME and a "
                            "1-purity core but not a baseline convention, so 0.20 is not a like-for-like "
                            "threshold on the d=3 observable.",
        "in_tree_window_note_calls_it_declared_import": bool(declared_import and import_header),
        "cycle914_stdout_label": "d1-comparator-floor" if c914_label else None,
        "cycle914_label_is_a_misattribution": bool(c914_label and d1_defers),
        "citation_rule_for_the_914_comparator_row":
            "The 914 CHECK-05 row may be cited ONLY as 'theta* compared against a 0.20 floor DECLARED by the "
            "frozen d=3 protocol and imported from the 2026-07-08 record-deposition-rate comparator'.  It may "
            "NOT be cited as a d=1-derived floor: the d=1 registration note measures no theta and explicitly "
            "defers the comparison to a d >= 2 comparator.  Because the two comparators anchor theta on "
            "different baselines, the 'inside / more than a factor of two of margin' reading is a "
            "cross-comparator numeric comparison, not a threshold test.",
    }


def c1_landing_recommendation(rec):
    """Emitted as DATA for the audit lane.  This runner restores nothing."""
    items = []
    for path, r in list(rec["artifacts"].items()) + list(rec["theta_floor_chain"].items()):
        if r.get("verdict") != "FOUND":
            continue
        items.append({
            "path": path,
            "recover_from": "%s:%s" % (r["add_commit"]["sha"], path),
            "blob": r["recovered"]["blob"],
            "sha256": r["recovered"]["sha256"],
            "bytes": r["recovered"]["bytes"],
            "single_blob_variant": len(r["distinct_blob_variants"]) == 1,
            "never_landed": not r["ancestor_of_origin_main"],
            "priority": "HIGH" if "REGISTRATION_REDUNDANCY_ONSET" in path
                        or "D3_BAR_LOCATION_BOUNDED" in path else "NORMAL",
        })
    return {
        "action": "RECOMMENDATION-ONLY (this runner restored nothing; no tree write occurred)",
        "addressed_to": "the audit lane",
        "finding": "every cited-but-absent predecessor exists in git history on physics-loop "
                   "branches and none is an ancestor of origin/main; the 2026-07-19 landing "
                   "commits carried the d3-bar-window artifacts onto main but not the "
                   "predecessor campaign notes or their runners",
        "items": items,
    }


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

    g["W_full_914"] = receipt["checks"]["CHECK-03-delta"]["W_full"]
    g["W_full_value_for_value"] = (g["W_full_914"] == C914_EXPECT["W_full_914"])
    g["verdicts_value_for_value"] = (
        receipt["verdict"]["parent_wiring"] == C914_EXPECT["verdict_parent"]
        and receipt["verdict"]["delta_wiring"] == C914_EXPECT["verdict_delta"])

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
    pins, absent = verify_pins()

    # ---------------------------------------------------------------- C1 ----
    t_c1 = time.perf_counter()
    rec = c1_recover()
    floor = c1_theta_floor_verdict(rec)
    landing = c1_landing_recommendation(rec)
    c1_wall = time.perf_counter() - t_c1

    n_found = sum(1 for r in rec["artifacts"].values() if r["verdict"] == "FOUND")
    n_absent = sum(1 for r in rec["artifacts"].values() if r["verdict"] == "GENUINELY-ABSENT")

    print("SETUP cycle=915 pins=%d absent-pins=%d C1[found=%d genuinely-absent=%d "
          "refs=%d commits=%d wall=%.1fs] %s"
          % (len(pins), len(absent), n_found, n_absent,
             rec["repo"]["refs_searched"], rec["repo"]["commits_reachable"],
             c1_wall, BOUNDARY_LINE))
    sys.stdout.flush()

    print("RECOVERY %s | theta-floor: %s origin=%s | d1-note-defers=%s "
          "deposition-note-measures=%s | 914-label-misattribution=%s %s"
          % ("; ".join("%s=%s%s" % (os.path.basename(p), r["verdict"],
                                    "" if r["verdict"] != "FOUND"
                                    else "(%s,%s)" % (r["absent_from_main_because"],
                                                      r["recovered"]["sha256"][:12]))
                       for p, r in rec["artifacts"].items()),
             floor["answer_kind"], floor["origin"],
             floor["d1_note_defers_the_comparison"],
             floor["deposition_note_measures_the_floor"],
             floor["cycle914_label_is_a_misattribution"], BOUNDARY_LINE))
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
    frags, pair_class, desc_sum = ns["build_descriptor"](memo)
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

    # ================================================================ C2 ====
    t_c2 = time.perf_counter()
    times2 = list(C2_TIMES) + [C2_DUP_T]        # duplicate -> determinism gate
    outs, prop2 = ns["chebyshev"](sec, C2_LAMBDA, a0, times2)
    mach["cheby_tail"] = max(mach["cheby_tail"], prop2["tail_bound"])
    dup_i = times2.index(C2_DUP_T)              # first occurrence
    dup_state_bitwise_equal = bool(np.array_equal(
        outs[dup_i].view(np.uint8), outs[-1].view(np.uint8)))

    rows2, chi0, one0, bond0, x_chi0 = [], None, None, None, None
    for it, t in enumerate(C2_TIMES):
        row, chi0, one0, bond0, x_chi0 = observable_row(
            ns, sec, OL, frags, pair_class, outs[it], t, C2_LAMBDA,
            chi0, one0, bond0, x_chi0, mach, True)
        rows2.append(row)
    # observable-pipeline determinism: recompute the duplicated time from the
    # duplicate state and require bitwise-equal scalars
    dup_row, _, _, _, _ = observable_row(
        ns, sec, OL, frags, pair_class, outs[-1], C2_DUP_T, C2_LAMBDA,
        chi0, one0, bond0, x_chi0, mach, False)
    ref_row = rows2[C2_TIMES.index(C2_DUP_T)]
    dup_keys = ["chi_closed_five", "chi_wedge_four", "theta", "H_Z", "sum_delta_chi"]
    dup_obs_equal = all(dup_row[k] == ref_row[k] for k in dup_keys)
    dup_pair_equal = (dup_row["pair_classes"] == ref_row["pair_classes"])
    del outs
    c2_wall = time.perf_counter() - t_c2

    ev2 = {str(d): first_hit(rows2, d) for d in DELTAS}
    h2 = ev2[str(HEADLINE_DELTA)]

    # --- C2 verdict in the delta memo's own W_full language ---
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

    print("C2[lambda=0.02] first-hit=%s theta*=%s R_ind=%s subset=%s run=%s "
          "max-pair=%s per-delta=%s W_full-member=%s repro-vs-committed=%s(rows=%d,dev=%s) %s"
          % (None if h2 is None else h2["jt"], None if h2 is None else h2["theta"],
             None if h2 is None else h2["r_ind"], None if h2 is None else h2["subset"],
             None if h2 is None else h2["run"], None if h2 is None else h2["max_pair"],
             per_delta2, lam002_in_W_full, repro["ok"], repro["rows_compared"],
             {k: "%.3g" % v for k, v in dev.items()}, BOUNDARY_LINE))
    sys.stdout.flush()

    # ================================================================ C3 ====
    t_c3 = time.perf_counter()
    c3 = {}
    for lam in C3_LAMBDAS:
        times3 = [0.0] + list(C3_TIMES)
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
        c3[str(lam)]["persistence_verdict"] = (
            "PERSISTS" if all(cert.values()) else
            "DECAYS" if not any(cert.values()) else "MIXED")
        c3[str(lam)]["early_first_hit_jt_from_914"] = C914_EXPECT["event_jt"][
            "0.05" if lam == 0.05 else "0.1"]
    c3_wall = time.perf_counter() - t_c3
    c3_scope = {"executed_times": list(C3_TIMES), "executed_lambdas": list(C3_LAMBDAS),
                "not_executed_times": list(C3_NOT_EXECUTED),
                "priority_order_declared": "1.5 and 2.0 at both lambdas first, then 5.0, then 10.0",
                "tier_executed": 1,
                "design_semantics": "the frozen memo classes all four late T_C samples as "
                                    "recurrence diagnostics that do not rescue CHECK-03; "
                                    "persistence here is the finite-sample flag, never permanence"}

    print("C3[late-grid] scope=%s %s %s"
          % (json.dumps(c3_scope["executed_times"]),
             "; ".join("lambda=%s:%s(%s)" % (l, c3[l]["persistence_verdict"],
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
    cf002 = ns["centered_frobenius_panel"](C2_LAMBDA, degrees)
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

    # CHECK-03/04/05 with lambda = 0.02 folded into the 914 window
    W_full = sorted(set(C914_EXPECT["W_full_914"]) | ({C2_LAMBDA} if lam002_in_W_full else set()))
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
    c05 = {"theta_star": theta_star_all, "W_full": W_full,
           "boundary_bracket_above": bracket_above,
           "boundary_bracket_below": bracket_below,
           "noncontiguous_window": (not contiguous),
           "labels": {k: (None if v is None else
                          ("inside" if v >= THETA_FLOOR else "BAR-BELOW-WINDOW"))
                      for k, v in theta_star_all.items()},
           "field_factor": field_factor,
           "field_stability_ok": bool(field_factor is not None and field_factor < DELTA_FACTOR_MAX),
           "window_size_ok": bool(len(W_full) >= 2),
           "theta_floor_citation": floor["citation_rule_for_the_914_comparator_row"]}

    c2_outcome = ("WINDOW-EXTENDS-BELOW-0.05" if lam002_in_W_full
                  else "LOWER-BOUNDARY-BRACKETED")
    c2_summary = {
        "outcome": c2_outcome,
        "lambda": C2_LAMBDA,
        "in_W_full": lam002_in_W_full,
        "first_hit": h2,
        "per_delta_first_hits": per_delta2,
        "all_deltas_by_deadline": all_deltas_hit_by_deadline,
        "headline_persists_3_samples": headline_persists,
        "W_full_after": W_full,
        "boundary_bracket_above": bracket_above,
        "boundary_bracket_below": bracket_below,
        "reading": ("lambda = 0.02 certifies at every commissioned tolerance by Jt <= 1 with a "
                    "persistent headline event, so the certified window extends BELOW the 914 "
                    "measurement's lowest certified field" if lam002_in_W_full else
                    "lambda = 0.02 fails at least one W_full clause, so the certified window is "
                    "bounded BELOW as well as above and the boundary bracket below is reported"),
    }

    machinery_ok = all(v <= MACH_TOL for k, v in mach.items() if k != "cheby_tail")

    # ------------------------------------------------------------ digest ---
    table = {
        "c2_rows": [{k: r[k] for k in sorted(r) if k not in ("bloch", "x_control")}
                    for r in rows2],
        "c2_events": ev2,
        "c3": c3,
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
        "cited_but_absent_pinned_as_absent": absent,
        "ast_extraction": ast_meta,
        "restriction_gates_vs_cycle914": gates,
        "C1_recovery": rec,
        "C1_theta_floor_provenance": floor,
        "C1_landing_recommendation": landing,
        "C2_lambda_002": c2_summary,
        "C2_rows": rows2,
        "C2_reproduction_vs_committed_2026_07_11": repro,
        "C3_late_grid": {"scope": c3_scope, "results": c3},
        "checks": {"CHECK-01": c01, "CHECK-02": c02, "CHECK-03": c03, "CHECK-05": c05},
        "falsifier_visibility": fal,
        "determinism": {"duplicate_time_requested": C2_DUP_T,
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
                     "theta_floor": THETA_FLOOR},
        "numerics": {"python": sys.version.split()[0], "numpy": np.__version__,
                     "route": "exact proper-cubic invariant-sector reduction (orbit basis) "
                              "+ Chebyshev expansion of exp(-iHt); float64/complex128 "
                              "(machinery AST-extracted from the Cycle 914 primary)",
                     "sector_dimension": sec.n * 2, "basis_checksum": sec.checksum,
                     "basis_wall_s": basis_wall, "layout_wall_s": ol_wall,
                     "c1_wall_s": c1_wall, "c2_wall_s": c2_wall, "c3_wall_s": c3_wall,
                     "chebyshev": {"c2": prop2},
                     "machinery": mach, "machinery_ok": bool(machinery_ok),
                     "peak_rss_gib": rssg, "wall_s": wall,
                     "result_table_sha256": digest},
        "verdict": None,
    }
    verdict = ("MACHINERY-FAIL" if not (machinery_ok and c01["ok"]
                                        and receipt["determinism"]["ok"] and fal["ok"])
               else "C2-CERTIFIED" if lam002_in_W_full else "C2-NOT-CERTIFIED")
    receipt["verdict"] = {"block": verdict, "c2_outcome": c2_outcome,
                          "c3_persistence": {l: c3[l]["persistence_verdict"] for l in c3},
                          "note": "outcome-neutral wiring: C2 lands certified-or-not and C3 "
                                  "lands persist-or-decay; neither is a machinery condition"}

    out_path = os.path.join(ROOT, "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json")
    with open(out_path, "w") as fh:
        json.dump(receipt, fh, indent=1, sort_keys=True, default=str)

    print("GATES 914-restrictions=%s theta*=%s labels=%s bracket=%s W_full[914]=%s "
          "C55[lam=0.20,Jt=0.7]=%s panel-spot=%s ordering=%s %s"
          % (gates["ok"], json.dumps(receipt914["checks"]["CHECK-05"]["theta_star"]),
             json.dumps(receipt914["checks"]["CHECK-05"]["labels"]),
             gates["boundary_bracket_value_for_value"], gates["W_full_914"],
             gates["lam020_C55_observed"], gates["check02_panel_spot_verified"],
             gates["check02_ordering_holds"], BOUNDARY_LINE))
    print("CHECKS+MACHINERY CHECK-01=%s CHECK-02=%s CHECK-03[lam=0.02]=%s "
          "CHECK-05[window=%s bracket-above=%s bracket-below=%s field-factor=%s]=%s "
          "falsifier=%s determinism=%s MACHINERY=ok(%s) %s"
          % (c01["ok"], c02["ok"], c03["ok"], W_full, bracket_above, bracket_below,
             None if field_factor is None else "%.9f" % field_factor,
             c05["window_size_ok"], fal["ok"], receipt["determinism"]["ok"],
             {k: "%.3g" % v for k, v in mach.items()}, BOUNDARY_LINE))
    print("TOTAL %s C2=%s(lambda=0.02 %s) C3=%s theta*[0.02]=%s window=%s "
          "digest=%s wall=%.1fs rss=%.2fGiB %s"
          % (verdict, c2_outcome, "in W_full" if lam002_in_W_full else "not in W_full",
             json.dumps({l: c3[l]["persistence_verdict"] for l in c3}),
             None if h2 is None else h2["theta"], W_full,
             digest[:16], wall, rssg, BOUNDARY_LINE))
    sys.stdout.flush()
    sys.exit(0 if verdict != "MACHINERY-FAIL" else 2)


if __name__ == "__main__":
    main()
