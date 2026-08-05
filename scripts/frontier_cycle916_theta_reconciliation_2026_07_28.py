#!/usr/bin/env python3
"""Cycle 916 -- THE THETA RECONCILIATION (C1) + THE TIER-2 LATE SAMPLES (C2).

C1.  Three observables share the name `theta` across the registration lineage.
     This runner rebuilds all three from their own source bytes, makes each a
     computable observable on its own declared system, computes the exact
     conversions where they exist, and prices the bridge where they do not.

       A  the FROZEN d=3 protocol theta
          docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md (in tree, pinned)
          theta_A(t) = (1/6) sum_a [ (1 - Tr rho_{S,a}(t)^2) - (same
          trajectory's t=0 value) ] over the six center bonds; the subtrahend
          is EXACTLY zero for the verified product preparation, so A is the
          ABSOLUTE center-bond mixedness.

       B  the 2026-07-08 deposition-comparator theta
          docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md
          (never landed; recovered from git history)
          theta_B(t, bond) = (1 - Tr rho_bond(t)^2) - (1 - Tr rho_bond^GS ^2)
          PER BOND on the N=12 gauged staggered-Schwinger rotor comparator.
          EXCESS mixedness over an interacting-ground-state baseline.  This is
          where the `theta >= 0.2` floor is measured.

       C  the 2026-07-09/10 pilot theta
          docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md
          (never landed; recovered from git history)
          theta_C(t) = mean over the six center bonds of GROUND-STATE-
          SUBTRACTED (1 - purity) on the same d=3 cube as A.  EXCESS
          mixedness.  The freeze overturned this baseline.

C2.  The frozen protocol's tier-2 late samples (Jt = 5, 10) at the certified
     fields lambda = 0.05, 0.10: does anything RE-CERTIFY (open-boundary
     revival) or does the decay hold?

Deterministic, float64/complex128, no network, no tree writes.
Numerical machinery is AST-lifted from the Cycle 914 primary; the deposition
comparator's machinery is AST-lifted from its own recovered source bytes.
"""

import ast
import hashlib
import itertools
import json
import os
import re
import resource
import shutil
import subprocess
import sys
import tempfile
import time

import numpy as np
from scipy.special import jv

T_START = time.perf_counter()

BOUNDARY = [
    "Declared comparators only; no formation rule, threshold value, or axiom content is chosen.",
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis.",
    "Finite volume, finite time; persistence flags are finite-sample, never permanence.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# =============================================================== pins =========
# path -> (sha256, git blob sha1).  Present in tree; byte-exact; hard-fail.
PINS = {
    "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md": (
        "c3e0b9162170f5e87e486f9d34068114d1d56b2f80db5c57df7ff7536820a93e",
        "5dff1d8b1692099cd86b53959834b6bcb5865a71"),
    "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md": (
        "9373dd8a9c8275b2b86e075a84d0ebe8621d3e39f52895f0b9ef406ee3d082ad",
        "d5b36708949d06bf619b2452e8f2897468e51194"),
    "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md": (
        "74a0a4c0e40e78ec042824ba706389e53e8bde22443964388987557a1819552c",
        "5f056aa69d1cc06dbfa2dc9ed6804df40c7b39fe"),
    "docs/MINIMAL_AXIOMS_2026-06-29.md": (
        "fc4d60cce8154cec26be12a0735033de43a0e554e7be951ffc0399c0b9788697",
        "4a863da1f3f255354839277271a3a69a5c205133"),
    "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py": (
        "fc7344a06503f9c159ea732cb6f622a23e61196e370914943ffd9a468fd592e4",
        "e0639e0b5d1ebdd995c4c7ec3255f8daeeb4fe0c"),
    "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json": (
        "fba8a16ee811fa1729bc1cdb6988096193a7e14878e7a78380f4880120bf7223",
        "cabb1bef15221b5fca61ffc7c50f8ec18452893d"),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p05_observables.jsonl": (None, None),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p10_observables.jsonl": (None, None),
    "logs/runner-cache/d3_bar_window_checkpoints/committed_evidence_manifest.json": (None, None),
    "scripts/frontier_cycle915_comparator_recovery_2026_07_28.py": (None, None),
    "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json": (None, None),
    "scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py": (None, None),
}

C914_PRIMARY = "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py"
C914_RECEIPT = "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json"
C915_PRIMARY = "scripts/frontier_cycle915_comparator_recovery_2026_07_28.py"
C915_RECEIPT = "outputs/comparator_recovery_cycle915_receipt_2026_07_28.json"
PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"
LANDED_NOTE = "docs/D3_BAR_WINDOW_BOUNDED_NOTE_2026-07-11.md"
MANIFEST = "logs/runner-cache/d3_bar_window_checkpoints/committed_evidence_manifest.json"
STREAM = {0.05: "logs/runner-cache/d3_bar_window_checkpoints/lam_0p05_observables.jsonl",
          0.10: "logs/runner-cache/d3_bar_window_checkpoints/lam_0p10_observables.jsonl"}

# ------- artifacts consumed from git history (read-only), verified by digest --
# path -> (blob sha1, sha256, byte count, source-of-the-digest, role)
HISTORY = {
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md": (
        "7d5a3696a8a0df454151173b1968a74b05a5788c",
        "6424412e7c9e2455fe78ec610ec0873ea1e9977773709b0718c31113a1885a0a",
        9689, "cycle-915-receipt", "convention C: the pilot's theta"),
    "docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md": (
        "15ef586b1f18b4ed076ee64ea78ff5708f27ce2d",
        "b0a95a7cbff611ace567e06fd12092185aec7a8ba9fe136e38165d2dfe44f907",
        30700, "cycle-915-receipt", "convention C: the pilot's frozen protocol"),
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md": (
        "c63dd2fa17e1fae95e3df822e6706d95f128d5c0",
        "08a0716cc349b150f0ac84a16118154dc313eddc2ac8545bdf9766e5823c9393",
        10157, "cycle-915-receipt", "convention A: the route-C conclusion + the bad comparison"),
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md": (
        "dd247a8494f171d4dcaf9a532a09491202b1f512",
        "41b4f26af908a7b910fbb5683f9d50432f36328bced7cf107585f7f70771df04",
        5230, "cycle-915-receipt", "the d=1 note: reports NO theta, defers the comparison"),
    "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md": (
        "017353319be0167651d81fcae20505e284837f22",
        "3d7303ca4464f56e48c7f107b9d5cd6ef6d046a7a90a4fe13859affba3e42386",
        2796, "cycle-915-receipt", "convention B: where theta >= 0.2 is MEASURED"),
    "docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md": (
        "722d9c0f2c27c3d3f5211a98c394b79c20926f3e",
        "191c1ed76082d6e885cb6bc2063dbadd51c375149cd186b357094fd09974d38e",
        4802, "cycle-915-receipt", "convention B: the campaign's own restatement of the floor"),
    # --- NEW in Cycle 916: convention B's own machinery, recovered here -------
    "scripts/deposition_per_activity_kappa_2026_07_08.py": (
        "6eb8510116fd7958a7b4435a3477139f77a46d81",
        "477bdcdd697ed673c179af8815cdfb9d84c021d423b0c3e45f4aee904453f1da",
        29824, "cycle-916-measured", "convention B: the primary runner (recovered here)"),
    "logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt": (
        "8833e731251d799ecf5a6f43e833836377f0bbf7",
        "b09f2b11512eb552f57f2d9d7c5c145c35b64cedcf5920af58b4a65a541acf17",
        2968, "cycle-916-measured", "convention B: the committed runner cache (recovered here)"),
    "scripts/activity_energy_bound_witnesses_2026_07_08.py@edf69d3c": (
        "4415dd17c81fd2e8f519267f86cbb794034ca717",
        "0601e139f9e1b81a17ceac1ab6fe0807ca4ad6cb5ebde3b3c09307f1ea7d9370",
        None, "cycle-916-measured",
        "convention B: the ONLY blob of this path carrying the API B needs"),
}
B_WITNESS_PATH = "scripts/activity_energy_bound_witnesses_2026_07_08.py"
B_WITNESS_COMMIT = "edf69d3c70eb06ecbe5744c974bfefc6b1bbf1b0"
B_ENGINE_PATH = "scripts/gauged_schwinger_staggered_ed_engine_2026_07_08.py"
B_RUNNER_PATH = "scripts/deposition_per_activity_kappa_2026_07_08.py"
B_RUNNER_COMMIT = "8f75f76ca28b50748f2398f5339babf93c3fde19"
B_CACHE_PATH = "logs/runner-cache/deposition_per_activity_kappa_2026_07_08.txt"

# ====================================================== frozen constants ======
LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")
CENTER = (0, 0, 0)
LAMBDAS = (0.05, 0.10, 0.20)
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05
EXCESS_MIN = 0.02
INDEP_MAX = 0.02
DRIFT_MAX = 0.10
PERSIST_N = 3
THETA_FLOOR = 0.20
X_CONTROL_MAX_JT = 1.0
T_C_FROZEN = [round(0.1 * i, 10) for i in range(13)] + [1.5, 2.0, 5.0, 10.0]

# ------------------------------------------------- Cycle 916 execution scope --
# The frozen design's tier ordering is 1.5/2.0 (tier 1, executed by Cycle 915),
# then 5.0, then 10.0 (tier 2).  Cycle 916 executes tier 2 under a disclosed
# split: lambda = 0.05 at BOTH tier-2 times, lambda = 0.10 at Jt = 5.0.  The
# lambda = 0.10, Jt = 10.0 cell is NOT freshly executed here (budget); it is
# read from the pinned committed 2026-07-11 stream and labelled as such.
C2_SCOPE = {0.05: [0.0, 5.0, 10.0], 0.10: [0.0, 5.0]}
C2_NOT_EXECUTED = [(0.10, 10.0)]
TIER2_TIMES = (5.0, 10.0)

# ---------------------------------------------------- ground-state filter ----
FILTER_LO = -48.0          # damping-interval lower edge (below it: amplified)
FILTER_STEPS = 36          # Chebyshev filter degree (fixed; deterministic)
GLOBAL_MASK = np.uint32((1 << 26) - 1)

# ================================================ restriction-gate targets ====
# Cycle 915 tier-1 decay rows (value-for-value).
GATE_915_TIER1 = {
    (0.05, 1.5): {"theta": 0.05536841624921374, "r_ind": 0},
    (0.05, 2.0): {"theta": 0.49776829171140624, "r_ind": 0},
    (0.10, 1.5): {"theta": 0.07679935076390587, "r_ind": 0},
    (0.10, 2.0): {"theta": 0.5119308113644572, "r_ind": 0},
}
# Cycle 914 headline theta* (value-for-value, from the 914 receipt).  lambda=0.20
# never fires a headline event, so its theta* is null by construction.
GATE_914_THETA_STAR = {"0.05": 0.5007515272813331,
                       "0.1": 0.5047307768675429,
                       "0.2": None}
# Cycle 915 lambda = 0.02 headline row.
GATE_915_LAM002 = {"jt": 0.6, "theta": 0.5001041579430632, "r_ind": 6,
                   "max_pair": 0.0011326954132362564}
# The committed 2026-07-11 mixed-doublet per-bond baseline (landed evidence).
GATE_COMMITTED_GS = {0.05: 0.49999999613891866, 0.10: 0.4999999382019271}
# The recovered route-C note's own doublet diagnostic, to 4 decimals.
GATE_RECOVERED_CHI_GS = {0.05: 0.9997, 0.10: 0.9989, 0.20: 0.9963}
# Convention B's committed once-counts over THETAS = (.02,.05,.1,.2,.3,.4).
GATE_B_ONCE = {("0.6", "a"): [12, 8, 4, 0, 0, 0], ("0.6", "b"): [12, 8, 1, 0, 0, 0],
               ("1", "a"): [10, 6, 4, 1, 0, 0], ("1", "b"): [12, 8, 4, 0, 0, 0]}
GATE_B_GS_RANGE = (0.271746, 0.487698)

MACH_TOL = 1e-9


# ============================================================ utilities =======
def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def blob_sha1(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def die(msg):
    print("SETUP MACHINERY-FAIL %s %s" % (msg, BOUNDARY_LINE))
    print("TOTAL MACHINERY-FAIL %s" % BOUNDARY_LINE)
    sys.stdout.flush()
    sys.exit(2)


GIT_LOG = []


def git_bytes(*args):
    """Read-only git returning raw bytes.  Every command is disclosed."""
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True)
    GIT_LOG.append({"cmd": "git " + " ".join(args), "rc": p.returncode,
                    "out_bytes": len(p.stdout)})
    if p.returncode != 0:
        die("git:%s rc=%d" % (" ".join(args)[:90], p.returncode))
    return p.stdout


def git_text(*args, allow_fail=False):
    p = subprocess.run(["git"] + list(args), cwd=ROOT, capture_output=True, text=True)
    GIT_LOG.append({"cmd": "git " + " ".join(args), "rc": p.returncode,
                    "out": p.stdout.rstrip("\n")[:400]})
    if p.returncode not in (0, 1) and not allow_fail:
        die("git:%s rc=%d" % (" ".join(args)[:90], p.returncode))
    return p.stdout.rstrip("\n")


def json_default(o):
    """numpy scalars -> json; booleans must NOT be laundered into numbers."""
    if isinstance(o, (np.bool_, bool)):
        return bool(o)
    if isinstance(o, np.integer):
        return int(o)
    if isinstance(o, np.floating):
        return float(o)
    if isinstance(o, np.ndarray):
        return o.tolist()
    if isinstance(o, complex):
        return {"re": o.real, "im": o.imag}
    raise TypeError("unserialisable %r" % type(o))


def rss_gib():
    ru = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    return ru / (2.0 ** 30) if ru > 2 ** 32 else ru / (1024.0 ** 2)


def verify_pins():
    out = {}
    for path, (want_sha, want_blob) in PINS.items():
        fp = os.path.join(ROOT, path)
        if not os.path.isfile(fp):
            die("pin:missing %s" % path)
        b = open(fp, "rb").read()
        got_sha, got_blob = sha256_bytes(b), blob_sha1(b)
        if want_sha is not None and want_sha != got_sha:
            die("pin:sha256 %s want=%s got=%s" % (path, want_sha[:16], got_sha[:16]))
        if want_blob is not None and want_blob != got_blob:
            die("pin:blob %s want=%s got=%s" % (path, want_blob[:12], got_blob[:12]))
        out[path] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b),
                     "pinned_value_declared": want_sha is not None}
    return out


def recover_history():
    """Read every never-landed artifact out of git history, byte-verified.

    Nothing is written into the repository tree.  Digest mismatch is fatal.
    """
    rec = {}
    blobs = {}
    head = git_text("rev-parse", "HEAD")
    main_tip = git_text("rev-parse", "origin/main", allow_fail=True)
    for key, (blob, want_sha, want_bytes, source, role) in HISTORY.items():
        path = key.split("@")[0]
        in_tree = os.path.exists(os.path.join(ROOT, path))
        raw = git_bytes("cat-file", "blob", blob)
        got_sha = sha256_bytes(raw)
        got_blob = blob_sha1(raw)
        if got_sha != want_sha:
            die("history:sha256 %s want=%s got=%s" % (key, want_sha[:16], got_sha[:16]))
        if got_blob != blob:
            die("history:blob %s want=%s got=%s" % (key, blob[:12], got_blob[:12]))
        if want_bytes is not None and len(raw) != want_bytes:
            die("history:bytes %s want=%d got=%d" % (key, want_bytes, len(raw)))
        rec[key] = {
            "path": path, "git_blob": blob, "sha256": got_sha, "bytes": len(raw),
            "digest_source": source, "role": role,
            "present_in_tree_at_this_path": bool(in_tree),
            "verified": True,
        }
        blobs[key] = raw
    # the in-tree witnesses file is a DIFFERENT blob that lost B's API
    wt = os.path.join(ROOT, B_WITNESS_PATH)
    intree = open(wt, "rb").read()
    api = ("build_bond_trace_groups", "gauged_bond_activities", "gauged_local_arrays",
           "periodic_bond_distances", "reduced_density")
    hist = blobs["scripts/activity_energy_bound_witnesses_2026_07_08.py@edf69d3c"]
    rec["_witness_divergence"] = {
        "path": B_WITNESS_PATH,
        "in_tree_blob": blob_sha1(intree),
        "in_tree_sha256": sha256_bytes(intree),
        "history_blob": blob_sha1(hist),
        "api_present_in_tree": sorted(a for a in api
                                      if ("def %s" % a).encode() in intree),
        "api_present_in_history_blob": sorted(a for a in api
                                              if ("def %s" % a).encode() in hist),
        "finding": ("the in-tree file at this path no longer exposes the API the "
                    "deposition comparator imports; only the 2026-07-09 history "
                    "blob does, so convention B is executable ONLY from history"),
    }
    rec["_repo"] = {"head": head, "origin_main_tip": main_tip}
    return rec, blobs


# ================================================ AST extraction (Cycle 914) ==
EXTRACT_FUNCS = ["cube_sites", "proper_rotations", "parse_memo_fragments",
                 "tiebreak_fragments", "build_descriptor", "_bitperm_tables",
                 "chebyshev", "ent_bits", "conditional_blocks", "chi_holevo",
                 "ptrace_keep_one", "ptrace_split", "cond_mi", "purity", "r_ind",
                 "centered_frobenius_panel"]
EXTRACT_CLASSES = ["Sector"]
EXTRACT_ASSIGNS = ["CH"]


def extract_module(src_bytes, src_name, funcs, classes, assigns, extra_ns):
    """Lift named top-level definitions out of verified source bytes by AST."""
    tree = ast.parse(src_bytes.decode())
    keep, names = [], []
    for n in tree.body:
        if isinstance(n, ast.FunctionDef) and n.name in funcs:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.ClassDef) and n.name in classes:
            keep.append(n); names.append(n.name)
        elif isinstance(n, ast.Assign):
            tg = [x.id for x in n.targets if isinstance(x, ast.Name)]
            if tg and tg[0] in assigns:
                keep.append(n); names.append(tg[0])
    missing = ([f for f in funcs if f not in names] + [c for c in classes if c not in names]
               + [a for a in assigns if a not in names])
    if missing:
        die("ast:missing[%s] %s" % (src_name, ",".join(missing)))
    mod = ast.Module(body=keep, type_ignores=[])
    ast.fix_missing_locations(mod)
    extracted = "\n\n".join(ast.unparse(n) for n in keep)
    ns = dict(extra_ns)
    exec(compile(mod, src_name, "exec"), ns)
    return ns, {"names": sorted(names), "source_name": src_name,
                "source_sha256": sha256_bytes(src_bytes),
                "extracted_source_sha256": sha256_bytes(extracted.encode())}


def extract_914_machinery():
    src = open(os.path.join(ROOT, C914_PRIMARY), "rb").read()
    extra = {"np": np, "hashlib": hashlib, "itertools": itertools, "json": json,
             "re": re, "jv": jv, "sha256_bytes": sha256_bytes,
             "CENTER": CENTER, "LABELS": LABELS, "CONTENT_H_MIN": CONTENT_H_MIN,
             "EXCESS_MIN": EXCESS_MIN, "INDEP_MAX": INDEP_MAX}
    return extract_module(src, C914_PRIMARY, EXTRACT_FUNCS, EXTRACT_CLASSES,
                          EXTRACT_ASSIGNS, extra)


# ============================== C1(a): the three definitions from their bytes ==
DEFN_PATTERNS = {
    "A": (PARENT_MEMO,
          r"where `a` runs over the six center bonds and the subtrahend is the same "
          r"trajectory's `t=0` value[^\n]*"),
    "A2": (LANDED_NOTE,
           r"`theta = \(1/6\) sum_a \(1 - Tr\(rho_\{Sa\}\^2\) - baseline_a\)`[\s\S]{0,120}?observable\."),
    "B": ("docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md",
          r"registration = upward\n?crossing of the EXCESS distinguishability[\s\S]{0,180}?threshold theta"),
    "C": ("docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md",
          r"theta\(t\) = mean over the six center bonds of[^\n]*\n[^\n]*"),
    "C_freeze_reason": (PARENT_MEMO,
                        r"The worker draft anchored the excess gate[\s\S]{0,1400}?being repaired\.\)"),
    "A_baseline_rule": (PARENT_MEMO,
                        r"\*\*The stationary doublet is retained as control and diagnostic[\s\S]{0,180}?verified invariant sector\."),
    "floor_is_import": (LANDED_NOTE,
                        r"the theta observable and its `0\.20` declared comparison floor"),
}


def definitional_bytes(pin_texts, hist_texts):
    """Pull each definition VERBATIM out of the byte source that declares it."""
    out = {}
    for key, (path, pat) in DEFN_PATTERNS.items():
        txt = pin_texts.get(path) or hist_texts.get(path)
        if txt is None:
            die("defn:source-missing %s" % path)
        m = re.search(pat, txt)
        if m is None:
            die("defn:pattern-miss %s" % key)
        out[key] = {"source": path, "quote": " ".join(m.group(0).split())}
    return out


# ================================ C1(b): the d=3 ground doublet (own filter) ===
def ground_doublet(ns, sec, gflip, lam):
    """Chebyshev spectral filter -> the ferromagnetic ground doublet.

    The filter damps [FILTER_LO, +A] and amplifies everything below FILTER_LO.
    Started from the all-up product configuration (which is Z2-mixed), it
    converges to a SYMMETRY-BROKEN doublet member G+.  The global spin flip F
    (an exact symmetry of H) then gives the orthogonal member G- = F G+, and
    rho^(2) = (|G+><G+| + |G-><G-|)/2 is the frozen memo's basis-invariant
    doublet mixture -- independent of which member an eigensolver returns.
    """
    A = 54.0 + 27.0 * lam
    c = 0.5 * (A + FILTER_LO)
    h = 0.5 * (A - FILTER_LO)
    scratch = np.empty((sec.n, 2), dtype=np.complex128)

    def op(v, out):
        sec.matvec(v, lam, out, scratch)
        out -= c * v
        out /= h
        return out

    v0 = np.zeros((sec.n, 2), dtype=np.complex128)
    v0[0, 0] = 1.0                      # all 27 spins up (orbit 0, centre up)
    Tp = v0
    Tc = np.empty_like(v0)
    op(Tp, Tc)
    Tn = np.empty_like(v0)
    nmv = 1
    for _ in range(2, FILTER_STEPS + 1):
        op(Tc, Tn)
        Tn *= 2.0
        Tn -= Tp
        nmv += 1
        Tp, Tc, Tn = Tc, Tn, Tp
    g = Tc
    g /= np.sqrt(sec.norm2(g))
    Hg = np.empty_like(g)
    sec.matvec(g, lam, Hg, scratch)
    nmv += 1
    E = float((sec.sizes[:, None] * (g.conj() * Hg).real).sum())
    Hg -= E * g
    residual = float(np.sqrt(sec.norm2(Hg)))
    del Hg, scratch, Tn, Tp
    gm = g[gflip][:, ::-1].copy()        # global spin flip: the other member
    ov = complex((sec.sizes[:, None] * (g.conj() * gm)).sum())
    return {"state_plus": g, "state_minus": gm, "energy": E, "residual": residual,
            "matvecs": nmv, "overlap_abs": abs(ov), "filter_degree": FILTER_STEPS,
            "damp_interval": [FILTER_LO, A], "norm_minus": sec.norm2(gm)}


def bond_and_chi(ns, sec, OL, state):
    """(S, +x face) center-bond 4x4 marginal + the unnormalised Holevo blocks."""
    s0, s1, cross, p, herm = ns["conditional_blocks"](state, OL["opposite-55"][0], 5,
                                                      "Z", True)
    rho = np.zeros((64, 64), dtype=np.complex128)
    rho[:32, :32] = s0
    rho[32:, 32:] = s1
    rho[:32, 32:] = cross
    rho[32:, :32] = cross.conj().T
    T = rho.reshape(2, 2, 16, 2, 2, 16)
    bond = np.einsum("abicdi->abcd", T).reshape(4, 4)
    del rho
    w0, w1, wcross, pw, hermw = ns["conditional_blocks"](state, OL["opposite-44"][0], 4,
                                                         "Z", True)
    return {"bond": bond, "s0": s0, "s1": s1, "p": p, "herm": max(herm, hermw),
            "w0": w0, "w1": w1, "pw": pw}


# ================== C1(c): convention B rebuilt from its own recovered bytes ===
B_FUNCS = ["load_authorized_sources", "vectorize_trace_groups", "packed_local_amplitudes",
           "batched_bond_observables", "crossings_for_threshold", "all_crossings",
           "deterministic_ground_state", "ground_distinguishability",
           "stationary_control_is_exact"]
B_CLASSES = ["BondLayout"]
B_ASSIGNS = ["N_SITES", "MASS", "COUPLINGS", "W_MAX", "T_FINAL", "DT", "N_TIMES",
             "TIMES", "HALF_INDEX", "THETAS", "RESET_FRACTION", "FILL_LIMIT",
             "NUMERIC_TOL", "RNG_SEED"]


def run_convention_B(blobs, tmpdir):
    """Execute convention B's own observable on its own declared system.

    The two module dependencies are materialised OUTSIDE the repository, from
    byte-verified blobs (the witnesses module only exists with B's API in
    history).  No repository file is written.
    """
    import scipy.sparse as sp                       # noqa: F401  (B's namespace)
    import scipy.sparse.linalg as spla
    from dataclasses import dataclass               # noqa: F401
    wsrc = blobs["scripts/activity_energy_bound_witnesses_2026_07_08.py@edf69d3c"]
    open(os.path.join(tmpdir, os.path.basename(B_WITNESS_PATH)), "wb").write(wsrc)
    esrc = open(os.path.join(ROOT, B_ENGINE_PATH), "rb").read()
    open(os.path.join(tmpdir, os.path.basename(B_ENGINE_PATH)), "wb").write(esrc)
    sys.path.insert(0, tmpdir)
    try:
        rsrc = blobs[B_RUNNER_PATH]
        extra = {"np": np, "sp": sp, "spla": spla, "sys": sys, "time": time,
                 "importlib": __import__("importlib"), "dataclass": dataclass,
                 "Any": object, "__name__": "_c916_convention_B"}
        bns, bmeta = extract_module(rsrc, B_RUNNER_PATH, B_FUNCS, B_CLASSES,
                                    B_ASSIGNS, extra)
        engine, witnesses = bns["load_authorized_sources"]()
        basis = engine.Basis(n_sites=bns["N_SITES"], w_max=bns["W_MAX"],
                             charge_sector=0, rotor=True)
        groups = [witnesses.build_bond_trace_groups(basis, b)
                  for b in range(bns["N_SITES"])]
        layouts = [bns["vectorize_trace_groups"](g, basis.dim) for g in groups]
        occ, _ = witnesses.gauged_local_arrays(engine, basis, bns["MASS"],
                                               bns["COUPLINGS"][0])
        out = {"meta": bmeta, "system": {
            "model": "staggered gauged Schwinger, finite rotor links",
            "n_sites": int(bns["N_SITES"]), "mass": float(bns["MASS"]),
            "couplings": [float(g) for g in bns["COUPLINGS"]],
            "w_max": int(bns["W_MAX"]), "charge_sector": 0,
            "hilbert_dimension": int(basis.dim), "n_bonds": len(groups),
            "bond_convention": "periodic bond (x, x+1); imported BondTraceGroups",
            "times": "0 : %g : %g (%d samples)" % (bns["DT"], bns["T_FINAL"],
                                                   bns["N_TIMES"]),
            "kicks": "a: exp(+i 0.7 n_0) ; b: exp(+i 0.5 (n_0 + n_6))",
            "swept_thresholds": [float(x) for x in bns["THETAS"]],
        }, "cases": {}}
        gmin, gmax = float("inf"), float("-inf")
        for gi, g in enumerate(bns["COUPLINGS"]):
            H = engine.build_many_body_hamiltonian(
                basis, bns["MASS"], g, boundary_holonomy_shifts_w=True).tocsr()
            E0, gs, res = bns["deterministic_ground_state"](H, witnesses,
                                                            bns["RNG_SEED"] + gi)
            gd = bns["ground_distinguishability"](gs, groups, witnesses)
            gmin = min(gmin, float(gd.min()))
            gmax = max(gmax, float(gd.max()))
            ka = np.exp(1.0j * 0.7 * occ[0]) * gs
            kb = np.exp(1.0j * 0.5 * (occ[0] + occ[6])) * gs
            ev = spla.expm_multiply((-1.0j) * H, np.column_stack((ka, kb)),
                                    start=0.0, stop=bns["T_FINAL"],
                                    num=bns["N_TIMES"], endpoint=True,
                                    traceA=complex(-1.0j * np.sum(H.diagonal())))
            tag = ("0.6" if abs(g - 0.6) < 1e-12 else "1")
            for pi, prep in enumerate(("a", "b")):
                act, raw, ierr, ok = bns["batched_bond_observables"](
                    ev[:, :, pi], H, layouts)
                exc = raw - gd[None, :]
                once, _ = bns["all_crossings"](exc, rearm=False)
                out["cases"]["%s/%s" % (tag, prep)] = {
                    "coupling": float(g), "preparation": prep,
                    "ground_energy": E0, "ground_residual": res,
                    "gs_baseline_per_bond": [float(x) for x in gd],
                    "gs_baseline_min": float(gd.min()), "gs_baseline_max": float(gd.max()),
                    "raw_1_minus_purity_range": [float(raw.min()), float(raw.max())],
                    "excess_theta_range": [float(exc.min()), float(exc.max())],
                    "once_counts": [int(x) for x in once],
                    "observable_error": float(ierr), "proxy_range_ok": bool(ok),
                }
                del act, raw, exc
            del H, ev
        out["gs_baseline_range"] = [gmin, gmax]
        return out
    finally:
        if tmpdir in sys.path:
            sys.path.remove(tmpdir)


# ==================================================== the measurement row =====
def observable_row(ns, sec, OL, frags, pair_class, a, t, lam, chi0, one0, bond0, mach):
    """One full certification row.  Structure follows the Cycle 914 primary."""
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

    raw_bond = 1.0 - purity(bond5)
    if chi0 is None:
        chi0 = {"closed-five": chi5, "wedge-four": chi4}
        one0 = dict(one_chi)
        bond0 = raw_bond
        mach["t0_anchor"] = max(mach["t0_anchor"], abs(chi5), abs(chi4),
                                max(abs(v) for v in one_chi.values()), abs(raw_bond))

    chi_by_label = {l: (chi5 if l in ("+x", "-x") else chi4) for l in LABELS}
    exc_by_label = {l: chi_by_label[l] - (chi0["closed-five"] if l in ("+x", "-x")
                                          else chi0["wedge-four"]) for l in LABELS}
    row.update({
        "H_Z": H, "p_z": p, "chi_closed_five": chi5, "chi_wedge_four": chi4,
        "excess_closed_five": chi5 - chi0["closed-five"],
        "excess_wedge_four": chi4 - chi0["wedge-four"],
        "one_site_chi": one_chi,
        "raw_bond_one_minus_purity": raw_bond,
        "theta": raw_bond - bond0,                       # convention A
        "pointer_tv_drift": abs(p[0] - 0.5),
        "removed_pointer_coherence": coh,
        "symmetry_max": sym, "state_norm_err": abs(n2 - 1.0),
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
    return row, chi0, one0, bond0


def tier2_verdict(rows):
    """RE-CERTIFIES iff any tier-2 row reaches R_ind >= 2 at any tolerance."""
    hits = [{"lam": r["lam"], "jt": r["jt"], "delta": d, "r_ind": r["r_ind"][str(d)]}
            for r in rows for d in DELTAS
            if r["jt"] >= 1.2 and r["r_ind"][str(d)] >= 2]
    return ("RE-CERTIFIES" if hits else "DECAY-HOLDS"), hits


# ====================================================== falsifier probes ======
def falsifier_probe(ns):
    r_ind = ns["r_ind"]
    idx = {l: i for i, l in enumerate(LABELS)}
    C = {tuple(sorted(pa, key=idx.get)): 0.001
         for pa in itertools.combinations(LABELS, 2)}
    chi = {l: 0.98 for l in LABELS}
    exc = {l: 0.98 for l in LABELS}
    n_plant, sub_plant, _ = r_ind(chi, exc, 1.0, C, HEADLINE_DELTA)
    n_corr, _, _ = r_ind(chi, exc, 1.0, {k: 0.5 for k in C}, HEADLINE_DELTA)
    n_low, _, _ = r_ind({l: 0.5 for l in LABELS}, {l: 0.5 for l in LABELS},
                        1.0, C, HEADLINE_DELTA)
    n_noexc, _, _ = r_ind(chi, {l: 0.0 for l in LABELS}, 1.0, C, HEADLINE_DELTA)
    # a PLANTED re-certifying LATE row must flip the C2 verdict
    planted = [{"lam": 0.05, "jt": 10.0, "r_ind": {"0.05": 0, "0.1": 4, "0.2": 4}}]
    v_planted, hits = tier2_verdict(planted)
    clean = [{"lam": 0.05, "jt": 10.0, "r_ind": {"0.05": 0, "0.1": 0, "0.2": 0}}]
    v_clean, _ = tier2_verdict(clean)
    return {
        "planted_certification_detected": bool(n_plant >= 2), "planted_r_ind": n_plant,
        "planted_subset": sub_plant,
        "correlated_pairs_rejected": bool(n_corr < 2),
        "below_content_rejected": bool(n_low < 2),
        "zero_excess_rejected": bool(n_noexc < 2),
        "planted_late_revival_flips_verdict": bool(v_planted == "RE-CERTIFIES"),
        "planted_late_hits": hits,
        "clean_late_row_holds_decay": bool(v_clean == "DECAY-HOLDS"),
        "ok": bool(n_plant >= 2 and n_corr < 2 and n_low < 2 and n_noexc < 2
                   and v_planted == "RE-CERTIFIES" and v_clean == "DECAY-HOLDS"),
        "meaning": ("the certification gate fires on a planted row and refuses three "
                    "near misses, and the C2 verdict function flips to RE-CERTIFIES "
                    "on a planted late revival: a real revival could not be missed"),
    }


# ============================================================== main =========
def main():
    pins = verify_pins()
    hist, blobs = recover_history()
    pin_texts = {p: open(os.path.join(ROOT, p), "rb").read().decode("utf-8", "replace")
                 for p in (PARENT_MEMO, DELTA_MEMO, LANDED_NOTE)}
    hist_texts = {k.split("@")[0]: v.decode("utf-8", "replace")
                  for k, v in blobs.items() if k.endswith(".md")}
    defs = definitional_bytes(pin_texts, hist_texts)

    print("SETUP cycle=916 pins=%d history-artifacts=%d git-cmds=%d head=%s %s"
          % (len(pins), len([k for k in hist if not k.startswith("_")]), len(GIT_LOG),
             hist["_repo"]["head"][:10], BOUNDARY_LINE))
    sys.stdout.flush()

    # ------------------------------------------------------- convention B ----
    t_b = time.perf_counter()
    tmpdir = tempfile.mkdtemp(prefix="c916_convB_")
    try:
        B = run_convention_B(blobs, tmpdir)
    finally:
        shutil.rmtree(tmpdir, ignore_errors=True)
    b_wall = time.perf_counter() - t_b
    b_cache = blobs[B_CACHE_PATH].decode()
    b_gate = {"once_counts_value_for_value": True, "per_case": {}}
    for key, want in GATE_B_ONCE.items():
        got = B["cases"]["%s/%s" % key]["once_counts"]
        ok = (got == want)
        b_gate["per_case"]["%s/%s" % key] = {"want": want, "got": got, "ok": ok}
        b_gate["once_counts_value_for_value"] &= ok
    b_gate["gs_range_want"] = list(GATE_B_GS_RANGE)
    b_gate["gs_range_got"] = B["gs_baseline_range"]
    b_gate["gs_range_ok"] = bool(
        abs(B["gs_baseline_range"][0] - GATE_B_GS_RANGE[0]) < 1e-6
        and abs(B["gs_baseline_range"][1] - GATE_B_GS_RANGE[1]) < 1e-6)
    b_gate["cache_line_present"] = bool("GS-d-range=[0.271746,0.487698]" in b_cache)
    if not (b_gate["once_counts_value_for_value"] and b_gate["gs_range_ok"]):
        die("restriction-gate:convention-B %s" % json.dumps(b_gate)[:300])

    # the floor's own resolution: 0.2 is a SWEPT GRID POINT, not a fitted value
    fill_at = {}
    for key in ("0.6/a", "1/a"):
        cs = B["cases"][key]
        fill_at[key] = {"once_counts": cs["once_counts"]}
    floor_bracket = {
        "swept_grid": B["system"]["swept_thresholds"],
        "declared_floor": 0.2,
        "grid_neighbour_below": 0.1,
        "true_crossing_bracketed_in": "(0.1, 0.2]",
        "reading": ("the 0.20 floor is the smallest SWEPT threshold at which the "
                    "committed fill translation falls under the campaign-6 wake "
                    "bound 0.3; the adjacent grid point 0.1 gives fill 0.333, so "
                    "the floor is grid-resolution-limited, not a measured crossing"),
    }
    print("C1-B[deposition comparator, recovered+executed] dim=%d bonds=%d "
          "gs-baseline=[%.6f,%.6f] once-counts-reproduced=%s cache-gate=%s wall=%.1fs %s"
          % (B["system"]["hilbert_dimension"], B["system"]["n_bonds"],
             B["gs_baseline_range"][0], B["gs_baseline_range"][1],
             b_gate["once_counts_value_for_value"], b_gate["cache_line_present"],
             b_wall, BOUNDARY_LINE))
    sys.stdout.flush()

    # ------------------------------------------------- d=3 machinery + gates --
    ns, ast_meta = extract_914_machinery()
    receipt914 = json.load(open(os.path.join(ROOT, C914_RECEIPT)))
    receipt915 = json.load(open(os.path.join(ROOT, C915_RECEIPT)))

    gates = {}
    ts = receipt914["checks"]["CHECK-05"]["theta_star"]
    gates["c914_theta_star_value_for_value"] = all(
        (ts[k] is None and v is None) or (ts[k] is not None and v is not None
                                          and abs(float(ts[k]) - v) < 1e-15)
        for k, v in GATE_914_THETA_STAR.items())
    gates["c914_theta_star"] = {k: ts[k] for k in ts}
    t1 = {}
    ok1 = True
    for lam in ("0.05", "0.1"):
        for r in receipt915["C3_late_grid"]["results"][lam]["late_rows"]:
            key = (float(lam), float(r["jt"]))
            want = GATE_915_TIER1.get(key)
            if want is None:
                continue
            hit = (r["theta"] == want["theta"]
                   and all(v == want["r_ind"] for v in r["r_ind"].values()))
            t1["%g@%g" % key] = {"theta": r["theta"], "want": want["theta"], "ok": bool(hit)}
            ok1 &= hit
    gates["c915_tier1_decay_value_for_value"] = bool(ok1)
    gates["c915_tier1_rows"] = t1
    h2 = receipt915["C2_lambda_002"]["first_hit"]
    gates["c915_lam002_value_for_value"] = bool(
        h2["jt"] == GATE_915_LAM002["jt"] and h2["theta"] == GATE_915_LAM002["theta"]
        and h2["r_ind"] == GATE_915_LAM002["r_ind"]
        and abs(h2["max_pair"] - GATE_915_LAM002["max_pair"]) < 1e-15)
    gates["c915_lam002_row"] = {"jt": h2["jt"], "theta": h2["theta"],
                                "r_ind": h2["r_ind"], "max_pair": h2["max_pair"]}
    gates["c915_theta_revival_figures"] = {
        "0.05@2.0": GATE_915_TIER1[(0.05, 2.0)]["theta"],
        "0.10@2.0": GATE_915_TIER1[(0.10, 2.0)]["theta"]}
    gates["convention_B"] = b_gate
    if not (gates["c914_theta_star_value_for_value"]
            and gates["c915_tier1_decay_value_for_value"]
            and gates["c915_lam002_value_for_value"]):
        die("restriction-gate:d3 %s" % json.dumps(
            {k: v for k, v in gates.items() if k.endswith("value_for_value")}))

    # ------------------------- the committed 2026-07-11 streams (landed rows) --
    committed = {}
    for lam, path in STREAM.items():
        rows = [json.loads(l) for l in open(os.path.join(ROOT, path))]
        gs = sorted({b["gs_doublet_one_minus_purity"] for r in rows
                     for b in r["center_bonds"]})
        committed[lam] = {
            "rows": len(rows), "jt_min": min(r["jt"] for r in rows),
            "jt_max": max(r["jt"] for r in rows),
            "gs_doublet_one_minus_purity_distinct": gs,
            "by_jt": {round(r["jt"], 6): {"theta": r["theta"], "r_ind": r["r_ind"]}
                      for r in rows},
        }
        if len(gs) != 1 or abs(gs[0] - GATE_COMMITTED_GS[lam]) > 1e-15:
            die("committed-stream:gs-baseline lam=%g got=%r" % (lam, gs))
    gates["committed_gs_baseline_value_for_value"] = True
    gates["committed_gs_baseline"] = {str(k): v["gs_doublet_one_minus_purity_distinct"][0]
                                      for k, v in committed.items()}
    # THE FINDING that reframes C2: the landed grid already reaches Jt = 10
    committed_tier2 = {}
    for lam in committed:
        for t in TIER2_TIMES:
            r = committed[lam]["by_jt"].get(round(t, 6))
            if r is not None:
                committed_tier2["%g@%g" % (lam, t)] = {
                    "theta_A": r["theta"], "r_ind": r["r_ind"],
                    "theta_C_mixed": r["theta"] - GATE_COMMITTED_GS[lam]}

    print("C1-STREAMS committed 2026-07-11 grid covers Jt=%.1f..%.1f at both certified "
          "lambdas; tier-2 cells ALREADY LANDED: %s %s"
          % (committed[0.05]["jt_min"], committed[0.05]["jt_max"],
             {k: v["r_ind"] for k, v in committed_tier2.items()}, BOUNDARY_LINE))
    sys.stdout.flush()

    # ---------------------------------------------------------- d=3 basis ----
    t_basis = time.perf_counter()
    sec = ns["Sector"]()
    basis_wall = time.perf_counter() - t_basis
    if sec.n * 2 != 5605504:
        die("basis:orbit-count %d" % (sec.n * 2))
    if sec.checksum != receipt914["numerics"]["basis_checksum"]:
        die("basis:checksum-drift %s" % sec.checksum[:16])
    gates["basis_checksum_matches_914"] = True

    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read()
    frags, pair_class, desc_sum = ns["build_descriptor"](memo)
    if desc_sum != receipt914["protocol"]["fragment_descriptor_checksum"]:
        die("descriptor:drift %s" % desc_sum[:16])
    gates["fragment_descriptor_matches_914"] = True

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
    gflip = sec.orbit_of[sec.reps ^ GLOBAL_MASK].copy()      # global spin flip
    del sec.orbit_of

    a0 = sec.prep(None, None, None)
    if abs(sec.norm2(a0) - 1.0) > 1e-12:
        die("prep:norm")

    mach = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0, "entropy_bound": 0.0,
            "symmetry": 0.0, "t0_anchor": 0.0, "cheby_tail": 0.0}

    # ============================================ C1(b): the A <-> C offset ===
    t_gs = time.perf_counter()
    offsets = {}
    for lam in (0.05, 0.10):
        d = ground_doublet(ns, sec, gflip, lam)
        gp = bond_and_chi(ns, sec, OL, d["state_plus"])
        gm = bond_and_chi(ns, sec, OL, d["state_minus"])
        purity = ns["purity"]
        bond_mixed = 0.5 * (gp["bond"] + gm["bond"])
        delta_broken = 1.0 - purity(gp["bond"])
        delta_broken_m = 1.0 - purity(gm["bond"])
        delta_mixed = 1.0 - purity(bond_mixed)
        chi5 = ns["chi_holevo"](gp["s0"] + gm["s0"], gp["s1"] + gm["s1"],
                                [gp["p"][0] + gm["p"][0], gp["p"][1] + gm["p"][1]])
        chi4 = ns["chi_holevo"](gp["w0"] + gm["w0"], gp["w1"] + gm["w1"],
                                [gp["pw"][0] + gm["pw"][0], gp["pw"][1] + gm["pw"][1]])
        chi5b = ns["chi_holevo"](gp["s0"], gp["s1"], gp["p"])
        offsets[lam] = {
            "energy": d["energy"], "residual": d["residual"], "matvecs": d["matvecs"],
            "filter_degree": d["filter_degree"], "damp_interval": d["damp_interval"],
            "member_overlap_abs": d["overlap_abs"], "norm_flipped_member": d["norm_minus"],
            "delta_gs_mixed_doublet": delta_mixed,
            "delta_gs_broken_member_plus": delta_broken,
            "delta_gs_broken_member_minus": delta_broken_m,
            "member_dependence_of_the_offset": abs(delta_mixed - delta_broken),
            "chi_gs2_closed_five_bits": chi5[0], "chi_gs2_wedge_four_bits": chi4[0],
            "chi_gs_broken_member_closed_five_bits": chi5b[0],
            "committed_gs_baseline": GATE_COMMITTED_GS[lam],
            "abs_dev_vs_committed": abs(delta_mixed - GATE_COMMITTED_GS[lam]),
            "hermiticity": max(gp["herm"], gm["herm"]),
        }
        mach["hermiticity"] = max(mach["hermiticity"], offsets[lam]["hermiticity"])
        del d, gp, gm, bond_mixed
    gs_wall = time.perf_counter() - t_gs

    gates["computed_gs_matches_committed"] = all(
        offsets[l]["abs_dev_vs_committed"] < 1e-6 for l in offsets)
    gates["recovered_chi_gs_value_for_value"] = all(
        abs(round(offsets[l]["chi_gs2_closed_five_bits"], 4)
            - GATE_RECOVERED_CHI_GS[l]) < 5e-5 for l in offsets)
    gates["recovered_chi_gs"] = {str(l): offsets[l]["chi_gs2_closed_five_bits"]
                                 for l in offsets}

    print("C1-OFFSET %s %s"
          % ({"lam=%g" % l: {"Delta_GS(mixed doublet)": "%.12f" % offsets[l]["delta_gs_mixed_doublet"],
                             "Delta_GS(symmetry-broken member)": "%.12f" % offsets[l]["delta_gs_broken_member_plus"],
                             "member-dependence": "%.6f" % offsets[l]["member_dependence_of_the_offset"],
                             "chi_GS2(bits)": "%.6f" % offsets[l]["chi_gs2_closed_five_bits"],
                             "E0": "%.12f" % offsets[l]["energy"],
                             "resid": "%.2e" % offsets[l]["residual"],
                             "|<G+|G->|": "%.2e" % offsets[l]["member_overlap_abs"],
                             "dev-vs-committed": "%.2e" % offsets[l]["abs_dev_vs_committed"]}
              for l in (0.05, 0.10)}, BOUNDARY_LINE))
    sys.stdout.flush()

    # --------------- offset Jt-independence over the whole committed grid -----
    jt_dependence = {}
    for lam in committed:
        dev = 0.0
        vals = []
        for jt, r in sorted(committed[lam]["by_jt"].items()):
            a_val = r["theta"]
            c_val = a_val - GATE_COMMITTED_GS[lam]
            vals.append((jt, a_val, c_val))
            dev = max(dev, abs((a_val - c_val) - GATE_COMMITTED_GS[lam]))
        jt_dependence[str(lam)] = {
            "samples": len(vals), "jt_span": [vals[0][0], vals[-1][0]],
            "max_abs_deviation_of_the_offset_from_constant": dev,
            "offset_is_jt_independent": bool(dev < 1e-15),
            "theta_A_range": [min(v[1] for v in vals), max(v[1] for v in vals)],
            "theta_C_mixed_range": [min(v[2] for v in vals), max(v[2] for v in vals)],
        }

    # ================================================ C2: the tier-2 samples ==
    t_c2 = time.perf_counter()
    c2 = {}
    all_late = []
    for lam in (0.05, 0.10):
        times = C2_SCOPE[lam]
        outs, prop = ns["chebyshev"](sec, lam, a0, times)
        mach["cheby_tail"] = max(mach["cheby_tail"], prop["tail_bound"])
        rows, chi0, one0, bond0 = [], None, None, None
        for it, t in enumerate(times):
            row, chi0, one0, bond0 = observable_row(
                ns, sec, OL, frags, pair_class, outs[it], t, lam, chi0, one0, bond0, mach)
            rows.append(row)
        del outs
        late = [r for r in rows if r["jt"] >= 1.2]
        all_late.extend(late)
        cmpd = {}
        for r in late:
            ref = committed[lam]["by_jt"].get(round(r["jt"], 6))
            if ref is not None:
                cmpd["%g" % r["jt"]] = {
                    "fresh_theta": r["theta"], "committed_theta": ref["theta"],
                    "abs_dev": abs(r["theta"] - ref["theta"]),
                    "fresh_r_ind": r["r_ind"], "committed_r_ind": ref["r_ind"],
                    "r_ind_agrees": all(int(ref["r_ind"]["%.2f" % d]) == r["r_ind"][str(d)]
                                        for d in DELTAS if "%.2f" % d in ref["r_ind"]),
                }
        c2[str(lam)] = {
            "executed_times": times, "t0_anchor_bond": bond0,
            "propagator": {"half_width": prop["half_width"], "degree": prop["degree"],
                           "matvecs": prop["matvecs"], "tail_bound": prop["tail_bound"]},
            "rows": [{k: r[k] for k in ("jt", "theta", "raw_bond_one_minus_purity",
                                        "r_ind", "r_raw", "chi_closed_five",
                                        "chi_wedge_four", "excess_closed_five",
                                        "excess_wedge_four", "H_Z", "pair_classes",
                                        "pair_reason", "singleton_passes",
                                        "certifying_subsets", "pointer_tv_drift",
                                        "Q_quiet", "X_face", "state_norm_err")}
                     for r in rows],
            "theta_C_mixed": {"%g" % r["jt"]: r["theta"] - offsets[lam]["delta_gs_mixed_doublet"]
                              for r in late},
            "theta_C_broken": {"%g" % r["jt"]: r["theta"] - offsets[lam]["delta_gs_broken_member_plus"]
                               for r in late},
            "vs_committed": cmpd,
        }
        print("C2[lambda=%.2f] %s | reproduction-vs-committed: %s %s"
              % (lam,
                 "; ".join("Jt=%.1f theta_A=%.12f R_ind=%s pairs=%s"
                           % (r["jt"], r["theta"], r["r_ind"],
                              r["pair_reason"] or "evaluated") for r in late),
                 {k: "dev=%.2e r_ind_agrees=%s" % (v["abs_dev"], v["r_ind_agrees"])
                  for k, v in cmpd.items()}, BOUNDARY_LINE))
        sys.stdout.flush()
    c2_wall = time.perf_counter() - t_c2

    verdict_c2, hits = tier2_verdict(all_late)
    repro_ok = all(v["r_ind_agrees"] and v["abs_dev"] < 1e-9
                   for lam in c2 for v in c2[lam]["vs_committed"].values())

    # ------------------------------- the 915 theta prediction, tested ---------
    pred_band = 0.05
    pred_rows = []
    for r in all_late:
        pred_rows.append({"lam": r["lam"], "jt": r["jt"], "theta": r["theta"],
                          "abs_dev_from_0.50": abs(r["theta"] - 0.50),
                          "within_band": bool(abs(r["theta"] - 0.50) <= pred_band),
                          "r_ind_zero": all(v == 0 for v in r["r_ind"].values())})
    for key, v in committed_tier2.items():
        if key not in ["%g@%g" % (r["lam"], r["jt"]) for r in all_late]:
            pred_rows.append({"lam": float(key.split("@")[0]), "jt": float(key.split("@")[1]),
                              "theta": v["theta_A"], "source": "committed-2026-07-11",
                              "abs_dev_from_0.50": abs(v["theta_A"] - 0.50),
                              "within_band": bool(abs(v["theta_A"] - 0.50) <= pred_band),
                              "r_ind_zero": all(int(x) == 0 for x in v["r_ind"].values())})
    n_in = sum(1 for r in pred_rows if r["within_band"])
    prediction = {
        "prediction_under_test": ("Cycle 915: at the deep-late samples theta stays near "
                                  "0.50 while R_ind stays 0"),
        "band": pred_band, "rows": pred_rows,
        "r_ind_zero_everywhere": all(r["r_ind_zero"] for r in pred_rows),
        "theta_within_band": "%d/%d" % (n_in, len(pred_rows)),
        "verdict": ("CONFIRMED" if n_in == len(pred_rows) else
                    ("REFUTED" if n_in == 0 else "PARTIALLY-REFUTED")),
        "reading": ("the R_ind half of the prediction holds at every tier-2 sample; the "
                    "theta half fails at Jt = 10, where theta climbs well above 0.50 -- "
                    "theta is not pinned near 0.50, it keeps drifting upward while "
                    "nothing certifies"),
        "post_specified": ("the band was fixed by this runner AFTER the committed "
                           "2026-07-11 rows had been read; this test is post-specified "
                           "descriptive support, not a blind prediction test"),
    }

    print("C2-VERDICT %s (tier-2 hits=%d) | fresh-vs-committed reproduction ok=%s | "
          "theta-prediction=%s theta-in-band=%s R_ind=0 everywhere=%s %s"
          % (verdict_c2, len(hits), repro_ok, prediction["verdict"],
             prediction["theta_within_band"], prediction["r_ind_zero_everywhere"],
             BOUNDARY_LINE))
    sys.stdout.flush()

    # =================================== C1(c): THE RECONCILIATION DICTIONARY ==
    d05 = offsets[0.05]
    d10 = offsets[0.10]
    theta_star = GATE_914_THETA_STAR
    check05 = {
        "the_row_as_landed": ("914/915 CHECK-05 compares theta* ~ 0.50 against a floor "
                              "0.20 and labels every fired event `inside` the sparse "
                              "window with more than a factor of two of margin"),
        "why_it_is_void_as_stated": (
            "theta* is an A-value (ABSOLUTE center-bond mixedness on the open 3^3 "
            "transverse-field Ising cube); 0.20 is a B-threshold (EXCESS bond mixedness "
            "over an interacting-ground-state baseline on the N=12 gauged staggered-"
            "Schwinger rotor comparator). Different systems, different baseline kinds, "
            "no declared map. The comparison is a category error, not a close call."),
        "nearest_same_shape_comparison": (
            "the only A-side quantity with B's baseline SHAPE (excess over the "
            "interacting ground state) is C. On the d=3 cube, C = A - Delta_GS exactly, "
            "with Delta_GS independent of Jt."),
        "X_under_the_mixed_doublet_convention": {
            "lambda=0.05": theta_star["0.05"] - d05["delta_gs_mixed_doublet"],
            "lambda=0.10": theta_star["0.1"] - d10["delta_gs_mixed_doublet"],
            "vs_floor": "BELOW the 0.20 floor by three orders of magnitude",
        },
        "X_under_a_symmetry_broken_member": {
            "lambda=0.05": theta_star["0.05"] - d05["delta_gs_broken_member_plus"],
            "lambda=0.10": theta_star["0.1"] - d10["delta_gs_broken_member_plus"],
            "vs_floor": "ABOVE the 0.20 floor",
        },
        "X_is_not_a_number": (
            "the two doublet conventions move theta* by ~0.5 -- more than twice the "
            "entire floor being compared against -- and they land on OPPOSITE sides of "
            "it. X is a two-valued function of a convention nothing in the lineage "
            "fixes, so the corrected reading of CHECK-05 is: the row reports no "
            "comparison at all, and the 0.20 label must be dropped, not re-signed."),
        "what_survives": (
            "theta* ~ 0.50 remains a correctly measured A-value of this comparator, and "
            "its lambda/delta insensitivity survives; only its comparison to 0.20 dies."),
    }
    bridge = {
        "verdict": "NO CONVERSION WITHOUT A BRIDGE PREMISE",
        "why": ("A and B are functions on disjoint state spaces (2^27 qubit "
                "configurations on an open 3^3 cube vs a %d-dimensional charge-zero "
                "gauged rotor sector at N=12) with no declared correspondence between "
                "their bonds, their fields (lambda vs g), their preparations (global "
                "product quench vs two strictly local unitary kicks on an interacting "
                "ground state) or their time units. Any map between them is a CHOICE."
                % B["system"]["hilbert_dimension"]),
        "required_content": [
            "B1 SYSTEM MAP: an identification of the two comparators' bond sets and "
            "their reduced 4-dimensional bond states (6 center bonds of a 27-qubit cube "
            "vs 12 periodic bonds of an N=12 gauged rotor chain), with the induced "
            "identification of lambda with g and of Jt with the deposition comparator's "
            "time unit.",
            "B2 BASELINE-KIND IDENTIFICATION: a rule saying which subtrahend the shared "
            "name `theta` denotes -- the trajectory's own t=0 value (A) or the "
            "interacting ground state's value (B, C). This is not a normalisation "
            "choice: on the d=3 cube the two differ by Delta_GS = %.6f, i.e. by more "
            "than twice the floor." % d05["delta_gs_mixed_doublet"],
            "B3 DOUBLET-CONVENTION FIX: if the baseline is the interacting ground state, "
            "a rule picking the ground state when it is degenerate. On the d=3 cube the "
            "ground doublet is split by ~1e-13 and the two natural conventions (the "
            "basis-invariant mixture vs a symmetry-broken member) give baselines %.6f "
            "and %.6f. The deposition comparator does not face this (its ground state "
            "is non-degenerate), so a bridge cannot inherit a convention from B."
            % (d05["delta_gs_mixed_doublet"], d05["delta_gs_broken_member_plus"]),
            "B4 COMPARATOR-INDEPENDENT NORMALISATION: a lemma that bond 1-purity is "
            "comparable across comparators at all. The landed 2026-07-11 note states "
            "the opposite in its own words: no reviewed theorem maps this value to a "
            "comparator-independent normalisation.",
            "B5 GRID CLOSURE: the 0.20 floor is a swept-grid value, not a measured "
            "crossing; the true crossing is bracketed only in (0.1, 0.2]. A bridge "
            "importing '0.20' imports the grid, not a threshold.",
        ],
        "price": ("five premises, of which B2/B3 are not merely unsupplied but "
                  "MEASURABLY OUTCOME-DECIDING here (they move the compared quantity by "
                  "~0.5 against a 0.20 floor), and B4 is explicitly disclaimed by the "
                  "landed note itself. Nothing cheaper than a new joint comparator with "
                  "both systems' observables measured under one declared convention "
                  "will discharge them."),
        "cheapest_honest_repair": ("stop citing 0.20 in the d=3 lane. Report theta* as an "
                                   "A-value with no floor attached, exactly as the "
                                   "landed 2026-07-11 note's import inventory already "
                                   "labels it (a `declared comparison floor`)."),
    }

    dictionary = {
        "definitions": {
            "A": {
                "name": "frozen d=3 protocol theta",
                "declared_in": PARENT_MEMO,
                "verbatim": defs["A"]["quote"],
                "restated_in": {LANDED_NOTE: defs["A2"]["quote"]},
                "system": "open 3x3x3 qubit cube, H = -J sum_<ij> Z_i Z_j - lambda J sum_i X_i",
                "preparation": "class-uniform product: centre + 6 faces in +X, 20 quiet sites in +Z",
                "observable": "(1/6) sum over the six centre bonds of [1 - Tr rho_{S,a}^2] "
                              "minus the SAME TRAJECTORY's t=0 value",
                "baseline_kind": "trajectory t=0 (verified exactly zero for a product prep)",
                "aggregation": "mean over six centre bonds (all equal by proper-cubic symmetry)",
                "is_therefore": "ABSOLUTE centre-bond mixedness",
                "measured_t0_subtrahend": {str(l): c2[str(l)]["t0_anchor_bond"] for l in (0.05, 0.10)},
                "computable_here": True,
            },
            "B": {
                "name": "deposition-comparator theta (2026-07-08 block01)",
                "declared_in": "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md",
                "verbatim": defs["B"]["quote"],
                "system": B["system"],
                "observable": "per bond: [1 - Tr rho_bond(t)^2] - [1 - Tr (rho_bond^GS)^2]",
                "baseline_kind": "interacting ground state, per bond (non-degenerate here)",
                "aggregation": "NONE -- thresholded bond by bond, one registration per site",
                "is_therefore": "EXCESS bond mixedness",
                "measured_baseline_range": B["gs_baseline_range"],
                "the_floor": floor_bracket,
                "recoverability": (
                    "FULLY RECOVERABLE AND RE-EXECUTABLE. The note, its runner, its "
                    "committed cache and the engine module it imports are all in git "
                    "history; the runner's crossing counts reproduce value-for-value. "
                    "One caveat: the witnesses module at its in-tree path no longer "
                    "carries the API B imports, so B runs only against the 2026-07-09 "
                    "history blob."),
                "computable_here": True,
            },
            "C": {
                "name": "pilot theta (2026-07-09/10)",
                "declared_in": "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md",
                "verbatim": defs["C"]["quote"],
                "system": "the SAME open 3x3x3 cube as A, but preparation = uniform "
                          "product with Bloch vector (1,1,1)/sqrt(3) on all 27 sites",
                "observable": "mean over the six centre bonds of ground-state-subtracted "
                              "(1 - purity)",
                "baseline_kind": "interacting ground state (QUASI-DEGENERATE DOUBLET here)",
                "aggregation": "mean over six centre bonds",
                "is_therefore": "EXCESS centre-bond mixedness",
                "computable_here": True,
                "ill_posedness": (
                    "C is not a single observable: its baseline is only defined once a "
                    "member of the ground doublet is chosen, and the two natural choices "
                    "differ by %.6f (lambda=0.05) / %.6f (lambda=0.10)."
                    % (d05["member_dependence_of_the_offset"],
                       d10["member_dependence_of_the_offset"])),
            },
        },
        "conversions": {
            "A_to_C": {
                "exists": True,
                "map": "theta_C(t) = theta_A(t) - Delta_GS(lambda)",
                "exactness": "EXACT and Jt-INDEPENDENT: both are affine functions of the "
                             "same 1 - purity(rho_bond(t)); the two baselines are both "
                             "constants in t, so their difference is a pure offset",
                "offsets": {str(l): {
                    "Delta_GS_mixed_doublet": offsets[l]["delta_gs_mixed_doublet"],
                    "Delta_GS_symmetry_broken_member": offsets[l]["delta_gs_broken_member_plus"],
                    "member_dependence": offsets[l]["member_dependence_of_the_offset"],
                } for l in (0.05, 0.10)},
                "jt_independence_measured": jt_dependence,
                "caveat": ("the map is exact but NOT single-valued: Delta_GS depends on "
                           "the doublet convention, and the dependence (~0.5) dwarfs the "
                           "quantity being converted"),
            },
            "A_to_B": bridge,
            "C_to_B": {
                "exists": False,
                "note": ("C and B share a baseline KIND (interacting ground state) but "
                         "nothing else: different systems, different bond sets, "
                         "different aggregation (C averages six bonds; B thresholds each "
                         "bond separately). Sharing the baseline kind removes only "
                         "bridge item B2, leaving B1, B3, B4, B5 outstanding."),
            },
        },
        "why_the_freeze_overturned_C": {
            "memo_reason_verbatim": defs["C_freeze_reason"]["quote"],
            "memo_rule_verbatim": defs["A_baseline_rule"]["quote"],
            "reproduced_as_a_measured_artifact": {
                "chi_GS2_closed_five_bits": {str(l): offsets[l]["chi_gs2_closed_five_bits"]
                                             for l in (0.05, 0.10)},
                "chi_GS2_wedge_four_bits": {str(l): offsets[l]["chi_gs2_wedge_four_bits"]
                                            for l in (0.05, 0.10)},
                "ceiling_H_Z_bits": 1.0,
                "excess_gate_would_demand_bits": {
                    str(l): offsets[l]["chi_gs2_closed_five_bits"] + EXCESS_MIN
                    for l in (0.05, 0.10)},
                "verdict": ("CONFIRMED: chi_GS^(2) saturates the pointer entropy, so a "
                            "chi - chi_GS >= 0.02 bit gate would demand chi >= %.4f bit "
                            "against a hard ceiling of 1 bit -- the negative would be "
                            "provable before any evolution ran, exactly as the freeze "
                            "memo argued."
                            % (offsets[0.05]["chi_gs2_closed_five_bits"] + EXCESS_MIN)),
                "the_pilot_escaped_only_by_the_ambiguity": {
                    "chi_GS_symmetry_broken_member_bits": {
                        str(l): offsets[l]["chi_gs_broken_member_closed_five_bits"]
                        for l in (0.05, 0.10)},
                    "reading": ("a symmetry-broken doublet member has a small chi_GS, "
                                "which is why the pilot's eigensolver produced a usable "
                                "gate; the mixture -- the only convention that does not "
                                "depend on eigensolver orientation -- does not."),
                },
                "matched_against_recovered_note": {
                    "recovered_values": GATE_RECOVERED_CHI_GS,
                    "reproduced": gates["recovered_chi_gs_value_for_value"],
                },
            },
        },
        "note_ledger": {
            PARENT_MEMO: {"reports": "A", "status": "in tree, frozen protocol memo"},
            DELTA_MEMO: {"reports": "A", "status": "in tree, frozen protocol delta"},
            LANDED_NOTE: {"reports": "A",
                          "status": "in tree, landed; already labels 0.20 a DECLARED "
                                    "comparison floor in its import inventory",
                          "floor_label_verbatim": defs["floor_is_import"]["quote"]},
            "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md": {
                "reports": "A", "status": "never landed, recovered",
                "carries_the_bad_comparison": True,
                "correction": ("its sentence `Every fired event is inside the sparse "
                               "window (theta* >= 0.2) with more than a factor of two of "
                               "margin` is an A-vs-B comparison and does not hold; see "
                               "the corrected CHECK-05 reading")},
            "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md": {
                "reports": "C", "status": "never landed, recovered"},
            "docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md": {
                "reports": "C", "status": "never landed, recovered (pilot protocol)"},
            "docs/DEPOSITION_PER_ACTIVITY_KAPPA_BOUNDED_NOTE_2026-07-08.md": {
                "reports": "B", "status": "never landed, recovered; the floor's origin"},
            "docs/DEPOSITION_CONSTANT_CONSTRAINT_MAP_2026-07-08.md": {
                "reports": "B", "status": "never landed, recovered; restates the floor"},
            "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md": {
                "reports": "NONE",
                "status": "never landed, recovered; the d=1 note reports no theta of its "
                          "own and explicitly DEFERS the theta* comparison to a d >= 2 "
                          "comparator"},
            C914_PRIMARY: {"reports": "A",
                           "status": "in tree; its stdout labels the floor "
                                     "`d1-comparator-floor`, which Cycle 915 already "
                                     "identified as a misattribution -- the floor is B's"},
            C915_PRIMARY: {"reports": "A", "status": "in tree"},
        },
        "one_line": ("A is absolute bond mixedness on the d=3 cube; B and C are excess "
                     "over an interacting ground state, B on a different comparator "
                     "entirely and C on a ground state that is not unique. A<->C is an "
                     "exact but convention-valued offset; A<->B needs a five-premise "
                     "bridge that nothing in the lineage supplies."),
    }

    print("C1-DICTIONARY conventions=3 A<->C=EXACT-OFFSET(Delta_GS=%.9f/%.9f, "
          "member-dependence=%.6f/%.6f) A<->B=%s bridge-premises=%d | CHECK-05 "
          "corrected: theta*(lambda=0.05)=%.12f is an A-value and 0.20 is a "
          "B-threshold; the same-shape (excess) value is X=%.6e under the mixed "
          "doublet or X=%.6f under a symmetry-broken member -- opposite sides of "
          "the floor %s"
          % (d05["delta_gs_mixed_doublet"], d10["delta_gs_mixed_doublet"],
             d05["member_dependence_of_the_offset"],
             d10["member_dependence_of_the_offset"], bridge["verdict"],
             len(bridge["required_content"]), theta_star["0.05"],
             check05["X_under_the_mixed_doublet_convention"]["lambda=0.05"],
             check05["X_under_a_symmetry_broken_member"]["lambda=0.05"], BOUNDARY_LINE))
    sys.stdout.flush()

    fals = falsifier_probe(ns)
    if not fals["ok"]:
        die("falsifier-visibility %s" % json.dumps(fals)[:300])

    mach_ok = (mach["norm"] < MACH_TOL and mach["hermiticity"] < MACH_TOL
               and abs(mach["negativity"]) < MACH_TOL and mach["entropy_bound"] < MACH_TOL
               and mach["symmetry"] < MACH_TOL and mach["t0_anchor"] < MACH_TOL
               and mach["cheby_tail"] < MACH_TOL)

    wall = time.perf_counter() - T_START
    receipt = {
        "schema": "frontier-cycle916-theta-reconciliation-v1",
        "cycle": 916, "date": "2026-07-28",
        "runner": "scripts/frontier_cycle916_theta_reconciliation_2026_07_28.py",
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "history_artifacts": hist,
        "git_commands": GIT_LOG,
        "ast_extraction": ast_meta,
        "C1_definitions_verbatim": defs,
        "C1_convention_B": B,
        "C1_offsets": {str(k): v for k, v in offsets.items()},
        "C1_offset_jt_independence": jt_dependence,
        "C1_reconciliation_dictionary": dictionary,
        "C1_corrected_check05": check05,
        "C2_scope": {"executed": {str(k): v for k, v in C2_SCOPE.items()},
                     "not_freshly_executed": [list(x) for x in C2_NOT_EXECUTED],
                     "disclosure": ("the lambda=0.10, Jt=10 cell was not freshly "
                                    "propagated here (Chebyshev budget); it is reported "
                                    "from the pinned committed 2026-07-11 stream and "
                                    "labelled as such"),
                     "frozen_grid": T_C_FROZEN},
        "C2_results": c2,
        "C2_verdict": {"verdict": verdict_c2, "tier2_hits": hits,
                       "fresh_vs_committed_reproduction_ok": bool(repro_ok),
                       "committed_tier2_rows": committed_tier2,
                       "reading": (
                           "no tier-2 sample certifies at any tolerance, at either "
                           "certified field, freshly or in the landed stream. There is "
                           "no open-boundary revival: certification in this comparator "
                           "is a transient window that opens at Jt = 0.6/0.7 and closes "
                           "for good. The d=3 bar's decay is monotone in the sense that "
                           "matters -- it never comes back.")},
        "C2_theta_prediction": prediction,
        "committed_streams": {str(k): {kk: vv for kk, vv in v.items() if kk != "by_jt"}
                              for k, v in committed.items()},
        "restriction_gates": gates,
        "falsifier_visibility": fals,
        "numerics": {"python": sys.version.split()[0], "numpy": np.__version__,
                     "route": ("exact proper-cubic invariant-sector reduction (orbit "
                               "basis, machinery AST-lifted from the Cycle 914 primary) "
                               "+ Chebyshev expansion of exp(-iHt); ground doublet by a "
                               "Chebyshev spectral filter plus the exact global-spin-flip "
                               "symmetry; convention B by exact sparse ED, machinery "
                               "AST-lifted from its own recovered source bytes"),
                     "sector_dimension": sec.n * 2, "basis_checksum": sec.checksum,
                     "fragment_descriptor_checksum": desc_sum,
                     "machinery": mach, "machinery_ok": bool(mach_ok),
                     "basis_wall_s": basis_wall, "layout_wall_s": ol_wall,
                     "ground_doublet_wall_s": gs_wall, "c2_wall_s": c2_wall,
                     "convention_b_wall_s": b_wall, "wall_s": wall,
                     "peak_rss_gib": rss_gib()},
        "deviations": [
            {"id": "C2-SCOPE-SPLIT",
             "what": "tier 2 executed as lambda=0.05 at Jt in {5,10} plus lambda=0.10 at "
                     "Jt=5; the lambda=0.10 Jt=10 cell is read from committed evidence",
             "why": "one Chebyshev pass to Jt=10 costs ~650 matvecs on a 5.6M-orbit "
                    "sector; both lambdas at both times does not fit the 900 s budget"},
            {"id": "TIER-2-ALREADY-LANDED",
             "what": "the committed 2026-07-11 streams already carry Jt = 5 and 10 rows "
                     "at both certified lambdas, so C2 is an independent REPRODUCTION, "
                     "not a first measurement",
             "why": "Cycle 914/915 called tier 2 unexecuted, which was true of THOSE "
                    "runners but not of the landed evidence they pin"},
            {"id": "B-EXECUTED-FROM-HISTORY",
             "what": "convention B's two module dependencies are materialised in a "
                     "temporary directory OUTSIDE the repository from byte-verified "
                     "blobs; no repository file is written",
             "why": "the witnesses module at its in-tree path lost the API B imports"},
            {"id": "POST-SPECIFIED-PREDICTION-BAND",
             "what": "the |theta - 0.50| <= 0.05 band for the Cycle 915 theta prediction "
                     "was fixed after the committed rows were read",
             "why": "the committed rows are pinned evidence and had to be read to build "
                    "the restriction gates; the test is labelled post-specified"},
        ],
        "verdict": {
            "C1": "RECONCILED",
            "C2": verdict_c2,
            "total": "THETA-RECONCILED/%s" % verdict_c2,
        },
    }
    outp = os.path.join(ROOT, "outputs/theta_reconciliation_cycle916_receipt_2026_07_28.json")
    blob = json.dumps(receipt, indent=1, sort_keys=True, default=json_default)
    open(outp, "w").write(blob + "\n")

    print("GATES %s %s"
          % ({k: v for k, v in gates.items()
              if isinstance(v, bool)}, BOUNDARY_LINE))
    print("FALSIFIER planted-cert=%s planted-late-revival-flips-verdict=%s "
          "near-misses-rejected=%s %s"
          % (fals["planted_certification_detected"],
             fals["planted_late_revival_flips_verdict"],
             fals["correlated_pairs_rejected"] and fals["below_content_rejected"]
             and fals["zero_excess_rejected"], BOUNDARY_LINE))
    print("MACHINERY %s ok=%s rss=%.2fGiB %s"
          % ({k: "%.3g" % v for k, v in sorted(mach.items())}, mach_ok, rss_gib(),
             BOUNDARY_LINE))
    for s in BOUNDARY:
        print("BOUNDARY  %s" % s)
    print("TOTAL THETA-RECONCILED/%s conventions=3 A<->C=exact-offset A<->B=no-conversion"
          "(bridge=%d premises) tier2=%s reproduction=%s wall=%.1fs receipt=%s %s"
          % (verdict_c2, len(bridge["required_content"]), verdict_c2, repro_ok, wall,
             sha256_bytes(blob.encode())[:16], BOUNDARY_LINE))
    sys.stdout.flush()
    return 0


if __name__ == "__main__":
    sys.exit(main())
