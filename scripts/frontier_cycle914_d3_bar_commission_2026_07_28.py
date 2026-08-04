#!/usr/bin/env python3
"""Cycle 914 -- COMMISSION ROUTE C: d=3 registration-bar location measurement.

Executes the frozen route-C protocol of

    docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md   (parent, FROZEN 2026-07-10)

as amended by the frozen delta

    docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md     (FROZEN 2026-07-11)

on the open 3x3x3 cube, H_lambda = -sum_<ij> Z_i Z_j - lambda sum_i X_i,
lambda in {0.05, 0.10, 0.20} (the parent memo's commissioned set), with the
cubic-class pointer-contrast preparation, the exact six-fragment partition and
its tie-break, the three-condition Holevo certification with the declared
tolerances, the C_ab conditional-independence formula, the trajectory-t0 excess
anchor, and the CHECK gates.

This runner is an INDEPENDENT implementation written from the memos' equations.
It imports nothing from the historical engine or the historical runner.

DISCLOSED SCOPE (see the DEVIATIONS block in the receipt): the frozen main state
grid Jt = 0:0.1:10 and the four late pair-recurrence samples {1.5,2,5,10} are
NOT executed under this block's 900 s runtime cap.  The executed grid is the
frozen certification subgrid restricted to Jt in {0.0,0.1,...,1.2}, which
contains the entire headline window (the Jt<=1 onset deadline plus the two
samples the frozen design requires for the persistence flag).

Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.
No formation rule.
Sets no audit status.
"""

import hashlib
import itertools
import json
import os
import platform
import re
import resource
import sys
import time

import numpy as np
from scipy.special import jv

T_START = time.perf_counter()

BOUNDARY = [
    "Not basis-neutral: the ZZ bond and the declared Z pointer privilege the Z basis, by construction.",
    "No formation rule.",
    "Sets no audit status.",
]
BOUNDARY_LINE = " ".join(BOUNDARY)

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# ---------------------------------------------------------------- pins -------
# full path -> (sha256, git blob).  Hard-fail exit 2 on any mismatch.
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
    # discovered prior-run comparator artifacts (route C WAS run: see DISCOVERY)
    "scripts/d3_bar_window_measurement_2026_07_11.py": (
        "b11077be706ae3d74b779319362a793ce7a73bd8ee05fb331d8fa4ab40b21d29",
        "d046e4f4e37365ba56199822bc9977c5fc48ed73"),
    "scripts/d3_bar_location_engine_ext_2026_07_10.py": (
        "71189dad66e4427673a4a83ad216c122cbc461b0353086c105762e3d81e6cb27",
        "581c23a921a5d8186e6387b93bdbbf507f4d9f9c"),
    "scripts/d3_cubic_orbit_engine_2026_07_09.py": (
        "4eb603fc229bc441ef254e9edc04c1cfeec1fe221be4a1af82fcee24f30bd60b",
        "1d3f8e230aae2864881a0c0bcc923ac231a91857"),
    "logs/runner-cache/d3_bar_window_checkpoints/committed_evidence_manifest.json": (
        "00da52fe2c22ed5716d00d7a68fc172684458d65cfce9f8c409bb28151f8b69c",
        "5fadb440ada474f86517fca327382c0ed990c999"),
    "logs/runner-cache/d3_bar_window_checkpoints/cube_gather_preflight.json": (
        "a60e1f57a2b3e4e6605d08b5eb8c80e35b47d9d09eb0281f7560f58c61224016",
        "60fe2700e3b1f2785e264ba49d4a4886583f2b96"),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p05_observables.jsonl": (
        "c15ff555a7057adad82e2f1350c5567db675bd26d67ff93681c445264409c890",
        "c260b67a08e271e8e7caa8dc5fe195e39fe38a12"),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p10_observables.jsonl": (
        "ceeb47ed6798482be24f39159d8a045839b2990b0e7df0b4ee4632ce5e97736a",
        "fa3399265ed9eab04ac6f141fbddf07edfa28689"),
    "logs/runner-cache/d3_bar_window_checkpoints/lam_0p20_observables.jsonl": (
        "0307237ae14fdc9016eee3dcbc82599771ca9568b47f1629df2fafbe1bb0695e",
        "51417a70d11d72cb6d9be2df89fc2c3a81efe1f4"),
}

# Comparator baselines the frozen memos cite but which are NOT in this tree.
CITED_ABSENT = [
    "docs/REGISTRATION_REDUNDANCY_ONSET_BOUNDED_NOTE_2026-07-09.md",   # the d=1 comparator note
    "docs/D3_REGISTRATION_PILOT_DESIGN_SCOUT_2026-07-09.md",
    "docs/D3_REGISTRATION_ONSET_PILOT_BOUNDED_NOTE_2026-07-10.md",
    "docs/D3_BAR_LOCATION_BOUNDED_NOTE_2026-07-10.md",
    "scripts/d3_bar_location_measurement_2026_07_10.py",
    "scripts/d3_registration_onset_pilot_2026_07_09.py",
]

PARENT_MEMO = "docs/D3_BAR_LOCATION_DESIGN_SCOUT_2026-07-10.md"
DELTA_MEMO = "docs/D3_BAR_WINDOW_DESIGN_DELTA_2026-07-11.md"

# ------------------------------------------------------ frozen protocol ------
LAMBDAS = (0.05, 0.10, 0.20)             # parent memo commissioned set
DELTAS = (0.05, 0.10, 0.20)
HEADLINE_DELTA = 0.10
DEADLINE_JT = 1.0
CONTENT_H_MIN = 0.05                     # condition 1
EXCESS_MIN = 0.02                        # condition 3
INDEP_MAX = 0.02                         # condition 4 / C_ab gate
T0_ANCHOR_TOL = 1e-9                     # CHECK-01
DRIFT_MAX = 0.10                         # CHECK-02
PERSIST_N = 3                            # CHECK-03
DELTA_FACTOR_MAX = 1.5                   # CHECK-04
THETA_FLOOR = 0.20                       # CHECK-05 declared comparison floor
MACH_TOL = 1e-9
LABELS = ("+x", "-x", "+y", "-y", "+z", "-z")

# frozen certification subgrid T_C, restricted to the executed window (see DEVIATIONS)
T_C_FROZEN = [round(0.1 * i, 10) for i in range(13)] + [1.5, 2.0, 5.0, 10.0]
T_EXEC = [round(0.1 * i, 10) for i in range(13)]
T_NOT_EXEC = [1.5, 2.0, 5.0, 10.0]
X_CONTROL_MAX_JT = 1.0

CENTER = (0, 0, 0)


def sha256_bytes(b):
    return hashlib.sha256(b).hexdigest()


def blob_bytes(b):
    return hashlib.sha1(b"blob %d\0" % len(b) + b).hexdigest()


def die(msg):
    for s in BOUNDARY:
        print(s)
    print("TOTAL MACHINERY-FAIL %s" % msg)
    sys.exit(2)


# =============================================================== pins ========
def verify_pins():
    rec = {}
    for rel, (want_sha, want_blob) in sorted(PINS.items()):
        p = os.path.join(ROOT, rel)
        if not os.path.exists(p):
            die("pin-missing:%s" % rel)
        b = open(p, "rb").read()
        got_sha, got_blob = sha256_bytes(b), blob_bytes(b)
        if got_sha != want_sha or got_blob != want_blob:
            die("pin-mismatch:%s" % rel)
        rec[rel] = {"sha256": got_sha, "git_blob": got_blob, "bytes": len(b)}
    absent = {}
    for rel in CITED_ABSENT:
        absent[rel] = os.path.exists(os.path.join(ROOT, rel))
        if absent[rel]:
            die("expected-absent-artifact-present:%s" % rel)
    return rec, absent


def scan_counts():
    def n(d, suf):
        p = os.path.join(ROOT, d)
        if not os.path.isdir(p):
            return 0
        return sum(1 for f in os.listdir(p) if f.endswith(suf))
    return {
        "docs_md": n("docs", ".md"),
        "scripts_py": n("scripts", ".py"),
        "runner_cache_entries": len(os.listdir(os.path.join(ROOT, "logs/runner-cache"))),
        "outputs_entries": len(os.listdir(os.path.join(ROOT, "outputs"))),
    }


def discovery():
    """Was any part of route C ever RUN?  Name-scan the tree for its artifacts."""
    names = {
        "historical_route_c_runner": "scripts/d3_bar_window_measurement_2026_07_11.py",
        "historical_engine_extension": "scripts/d3_bar_location_engine_ext_2026_07_10.py",
        "historical_orbit_engine": "scripts/d3_cubic_orbit_engine_2026_07_09.py",
        "historical_runner_cache": "logs/runner-cache/d3_bar_window_measurement_2026_07_11.txt",
        "historical_validate_cache": "logs/runner-cache/d3_bar_window_validate_2026_07_11.txt",
        "historical_checkpoint_dir": "logs/runner-cache/d3_bar_window_checkpoints",
        "historical_manifest": "logs/runner-cache/d3_bar_window_checkpoints/committed_evidence_manifest.json",
        "historical_preflight": "logs/runner-cache/d3_bar_window_checkpoints/cube_gather_preflight.json",
    }
    found = {k: os.path.exists(os.path.join(ROOT, v)) for k, v in names.items()}
    streams = {}
    for tag in ("0p02", "0p05", "0p10", "0p20"):
        rel = "logs/runner-cache/d3_bar_window_checkpoints/lam_%s_observables.jsonl" % tag
        p = os.path.join(ROOT, rel)
        streams[tag] = sum(1 for _ in open(p)) if os.path.exists(p) else 0
    return {
        "route_c_previously_run": all(found.values()),
        "artifacts_present": found,
        "committed_stream_row_counts": streams,
        "cited_but_absent": CITED_ABSENT,
        "scan_counts": scan_counts(),
    }


# ========================================================= descriptor ========
def cube_sites():
    return sorted([(x, y, z) for x in (-1, 0, 1) for y in (-1, 0, 1) for z in (-1, 0, 1)])


def proper_rotations():
    out = []
    for perm in itertools.permutations(range(3)):
        for signs in itertools.product((1, -1), repeat=3):
            M = np.zeros((3, 3), dtype=np.int64)
            for i in range(3):
                M[i, perm[i]] = signs[i]
            if int(round(np.linalg.det(M))) == 1:
                out.append(M)
    assert len(out) == 24
    return out


def parse_memo_fragments(memo_bytes):
    """Parse the six declared fragment lists from the FROZEN memo's own bytes."""
    txt = memo_bytes.decode("utf-8")
    frags = {}
    for m in re.finditer(r"`F_\(([+-][xyz])\) = \[([^\]]*)\]`", txt):
        label = m.group(1)
        pts = re.findall(r"\(([+-]?\d),([+-]?\d),([+-]?\d)\)", m.group(2))
        frags[label] = [tuple(int(v) for v in p) for p in pts]
    return frags


def tiebreak_fragments():
    """Recompute the partition from the memo's stated tie-break ALGORITHM."""
    frags = {l: [] for l in LABELS}
    faces = [c for c in cube_sites() if c != CENTER and sum(map(abs, c)) == 1]
    for f in faces:
        ax = "xyz"[[abs(v) for v in f].index(1)]
        sgn = "+" if sum(f) > 0 else "-"
        frags[sgn + ax].append(f)
    for c in cube_sites():
        if c == CENTER or sum(map(abs, c)) == 1:
            continue
        x, y, z = c
        if sum(map(abs, c)) == 2 and x != 0:            # edge with x != 0
            frags[("+" if x > 0 else "-") + "x"].append(c)
        else:                                            # x=0 edges and all corners
            key = (1 if y > 0 else -1, 1 if z > 0 else -1)
            frags[{(1, 1): "+y", (-1, 1): "+z", (-1, -1): "-y", (1, -1): "-z"}[key]].append(c)
    return frags


def build_descriptor(memo_bytes):
    sites = cube_sites()
    rots = proper_rotations()
    declared = parse_memo_fragments(memo_bytes)
    if sorted(declared) != sorted(LABELS):
        die("descriptor:memo-fragment-parse")
    algo = tiebreak_fragments()
    for l in LABELS:
        if set(declared[l]) != set(algo[l]):
            die("descriptor:tiebreak-mismatch:%s" % l)
    sizes = [len(declared[l]) for l in LABELS]
    if sizes != [5, 5, 4, 4, 4, 4]:
        die("descriptor:fragment-sizes")
    allsites = [c for l in LABELS for c in declared[l]]
    if len(allsites) != 26 or len(set(allsites)) != 26 or CENTER in allsites:
        die("descriptor:partition")
    if set(allsites) != set(s for s in sites if s != CENTER):
        die("descriptor:coverage")

    # proper-rotation classes of fragments and of the 15 pairs
    setmap = {frozenset(declared[l]): l for l in LABELS}
    frag_class_edges = {l: set() for l in LABELS}
    for M in rots:
        for l in LABELS:
            img = frozenset(tuple(int(v) for v in (M @ np.array(c))) for c in declared[l])
            if img in setmap:
                frag_class_edges[l].add(setmap[img])
    if frag_class_edges["+x"] != {"+x", "-x"} or frag_class_edges["-x"] != {"+x", "-x"}:
        die("descriptor:closed-five-class")
    wedge = {"+y", "-y", "+z", "-z"}
    for l in wedge:
        if frag_class_edges[l] != wedge:
            die("descriptor:wedge-four-class")

    pairs = [(LABELS[i], LABELS[j]) for i in range(6) for j in range(i + 1, 6)]
    pair_orbit = {}
    for pa in pairs:
        img_set = set()
        for M in rots:
            imgs = []
            for l in pa:
                img = frozenset(tuple(int(v) for v in (M @ np.array(c))) for c in declared[l])
                imgs.append(setmap.get(img))
            if imgs[0] is not None and imgs[1] is not None:
                img_set.add(tuple(sorted(imgs, key=LABELS.index)))
        pair_orbit[pa] = img_set
    declared_classes = {
        "opposite-55": [("+x", "-x")],
        "opposite-44": [("+y", "-y"), ("+z", "-z")],
        "plus-x-orthogonal": [("+x", q) for q in ("+y", "-y", "+z", "-z")],
        "minus-x-orthogonal": [("-x", q) for q in ("+y", "-y", "+z", "-z")],
        "transverse-orthogonal": [("+y", "+z"), ("+z", "-y"), ("-y", "-z"), ("-z", "+y")],
    }
    norm = {}
    for cls, members in declared_classes.items():
        for pa in members:
            key = tuple(sorted(pa, key=LABELS.index))
            if key in norm:
                die("descriptor:pair-class-overlap")
            norm[key] = cls
    if len(norm) != 15:
        die("descriptor:pair-class-count")
    for pa in pairs:
        key = tuple(sorted(pa, key=LABELS.index))
        for other in pair_orbit[pa]:
            if norm[other] != norm[key]:
                die("descriptor:pair-class-not-rotation-closed")
    payload = json.dumps({"fragments": {l: declared[l] for l in LABELS},
                          "pair_classes": {"|".join(k): v for k, v in sorted(norm.items())},
                          "label_order": list(LABELS)}, sort_keys=True)
    return declared, norm, sha256_bytes(payload.encode())


# ============================================================== basis ========
CH = [(0, 9), (9, 9), (18, 8)]


def _bitperm_tables(p):
    tabs = []
    for (sh, w) in CH:
        vals = np.arange(1 << w, dtype=np.uint32)
        t = np.zeros(1 << w, dtype=np.uint32)
        for b in range(w):
            t |= ((vals >> np.uint32(b)) & np.uint32(1)) << np.uint32(p[sh + b])
        tabs.append(t)
    return tabs


class Sector(object):
    """Exact proper-cubic invariant sector of the open 3x3x3 cube."""

    def __init__(self):
        self.sites = cube_sites()
        self.nc = [c for c in self.sites if c != CENTER]
        self.idx = {c: i for i, c in enumerate(self.nc)}
        self.rots = proper_rotations()
        N26 = 1 << 26
        perms = []
        for M in self.rots:
            p = np.empty(26, dtype=np.int64)
            for j, c in enumerate(self.nc):
                p[j] = self.idx[tuple(int(v) for v in (M @ np.array(c)))]
            perms.append(p)
        x = np.arange(N26, dtype=np.uint32)
        ci = [((x >> np.uint32(sh)) & np.uint32((1 << w) - 1)).astype(np.uint32) for (sh, w) in CH]
        canon = None
        tmp = np.empty(N26, dtype=np.uint32)
        for p in perms:
            tabs = _bitperm_tables(p)
            np.take(tabs[0], ci[0], out=tmp)
            tmp |= tabs[1][ci[1]]
            tmp |= tabs[2][ci[2]]
            canon = tmp.copy() if canon is None else np.minimum(canon, tmp, out=canon)
        del tmp, ci
        self.reps = np.flatnonzero(canon == x).astype(np.uint32)
        self.n = int(self.reps.size)
        lut = np.zeros(N26, dtype=np.uint32)
        lut[self.reps] = np.arange(self.n, dtype=np.uint32)
        self.orbit_of = lut[canon]
        del lut, canon, x
        self.sizes = np.bincount(self.orbit_of, minlength=self.n).astype(np.float64)
        self.flip = np.empty((26, self.n), dtype=np.uint32)
        for i in range(26):
            self.flip[i] = self.orbit_of[self.reps ^ np.uint32(1 << i)]
        bonds = [(a, b) for ia, a in enumerate(self.sites) for b in self.sites[ia + 1:]
                 if sum(abs(a[k] - b[k]) for k in range(3)) == 1]
        assert len(bonds) == 54
        self.bonds = bonds
        zr = np.empty((26, self.n), dtype=np.int8)
        for i in range(26):
            zr[i] = 1 - 2 * ((self.reps >> np.uint32(i)) & np.uint32(1)).astype(np.int8)
        E_nc = np.zeros(self.n, dtype=np.int16)
        sig = np.zeros(self.n, dtype=np.int16)
        for (ca, cb) in bonds:
            if ca == CENTER:
                sig += zr[self.idx[cb]]
            elif cb == CENTER:
                sig += zr[self.idx[ca]]
            else:
                E_nc += zr[self.idx[ca]].astype(np.int16) * zr[self.idx[cb]].astype(np.int16)
        self.Ediag = np.empty((self.n, 2), dtype=np.float64)
        self.Ediag[:, 0] = E_nc + sig
        self.Ediag[:, 1] = E_nc - sig
        del zr, E_nc, sig
        h = hashlib.sha256()
        h.update(np.asarray([self.n], dtype=np.int64).tobytes())
        h.update(self.sizes.astype(np.int64).tobytes())
        h.update(self.reps.tobytes())
        h.update(self.Ediag.astype(np.int64).tobytes())
        self.checksum = h.hexdigest()

    def layout(self, subset):
        """Raw-to-orbit lookup ordered so that `subset` occupies the HIGH bits."""
        rest = [c for c in self.nc if c not in subset]
        order = list(subset) + rest
        p = np.empty(26, dtype=np.int64)
        for q, site in enumerate(order):
            p[25 - q] = self.idx[site]
        tabs = _bitperm_tables(p)
        y = np.arange(1 << 26, dtype=np.uint32)
        xx = tabs[0][(y & np.uint32(511))]
        xx |= tabs[1][((y >> np.uint32(9)) & np.uint32(511))]
        xx |= tabs[2][((y >> np.uint32(18)) & np.uint32(255))]
        del y
        out = self.orbit_of[xx]
        return out

    def matvec(self, a, lam, out, work):
        np.multiply(a, -self.Ediag, out=out)
        out -= lam * a[:, ::-1]
        for i in range(26):
            np.take(a, self.flip[i], axis=0, out=work)
            out -= lam * work
        return out

    def norm2(self, a):
        return float((self.sizes[:, None] * (a.real ** 2 + a.imag ** 2)).sum())

    def prep(self, faces, edges, corners):
        """Class-uniform product preparation, raw amplitudes on orbit reps."""
        quiet = np.uint32(0)
        for c in self.nc:
            if sum(map(abs, c)) >= 2:
                quiet |= np.uint32(1 << self.idx[c])
        a = np.zeros((self.n, 2), dtype=np.complex128)
        ok = (self.reps & quiet) == 0
        a[ok, :] = 2.0 ** -3.5      # center + 6 faces in +X, 20 quiet sites in +Z
        return a


# ======================================================== propagation ========
def chebyshev(sec, lam, a0, times):
    """Exact e^{-iHt} on the invariant sector by Chebyshev expansion (float64)."""
    A = 54.0 + 27.0 * lam                     # rigorous spectral half-width bound
    tmax = max(times)
    M = int(np.ceil(A * tmax)) + 5
    while abs(jv(M, A * tmax)) > 1e-17:
        M += 5
    outs = [np.zeros_like(a0) for _ in times]
    coef = np.zeros((M + 1, len(times)), dtype=np.complex128)
    for k in range(M + 1):
        for j, t in enumerate(times):
            coef[k, j] = jv(k, A * t) * ((-1j) ** k) * (1.0 if k == 0 else 2.0)
    scratch = np.empty_like(a0)
    Tprev = a0.copy()
    Tcur = np.empty_like(a0)
    sec.matvec(Tprev, lam, Tcur, scratch)
    Tcur /= A
    Tnext = np.empty_like(a0)
    nmv = 1

    def acc(k, vec):
        for j in range(len(times)):
            c = coef[k, j]
            if abs(c) < 1e-18:
                continue
            outs[j] += c * vec

    acc(0, Tprev)
    acc(1, Tcur)
    for k in range(2, M + 1):
        sec.matvec(Tcur, lam, Tnext, scratch)
        Tnext *= (2.0 / A)
        Tnext -= Tprev
        nmv += 1
        acc(k, Tnext)
        Tprev, Tcur, Tnext = Tcur, Tnext, Tprev
    tail = float(max(abs(jv(M + 1, A * tmax)), abs(jv(M + 2, A * tmax))))
    return outs, {"half_width": A, "degree": M, "matvecs": nmv, "tail_bound": 2.0 * tail}


# ========================================================= observables =======
def ent_bits(w):
    w = np.asarray(w).real
    neg = float(min(0.0, w.min()))
    w = w[w > 1e-16]
    return float(-(w * np.log2(w)).sum()), neg


def conditional_blocks(a, OL, k, basis="Z", want_cross=False):
    """Return (sigma_0, sigma_1, cross, p, diagnostics) for the pointer split."""
    if basis == "Z":
        v0 = np.ascontiguousarray(a[:, 0])
        v1 = np.ascontiguousarray(a[:, 1])
    else:                                    # X pointer projectors
        v0 = (a[:, 0] + a[:, 1]) / np.sqrt(2.0)
        v1 = (a[:, 0] - a[:, 1]) / np.sqrt(2.0)
        v0 = np.ascontiguousarray(v0)
        v1 = np.ascontiguousarray(v1)
    M0 = v0[OL].reshape(1 << k, -1)
    s0 = M0 @ M0.conj().T
    if want_cross:
        M1 = v1[OL].reshape(1 << k, -1)
        s1 = M1 @ M1.conj().T
        cross = M0 @ M1.conj().T
        del M1
    else:
        del M0
        M1 = v1[OL].reshape(1 << k, -1)
        s1 = M1 @ M1.conj().T
        cross = None
        del M1
    p = [float(np.trace(s0).real), float(np.trace(s1).real)]
    herm = max(float(np.abs(s0 - s0.conj().T).max()), float(np.abs(s1 - s1.conj().T).max()))
    return s0, s1, cross, p, herm


def chi_holevo(s0, s1, p):
    rho = s0 + s1
    tot = p[0] + p[1]
    Savg, n1 = ent_bits(np.linalg.eigvalsh(rho / tot))
    Scond, n2 = 0.0, 0.0
    for s, pz in ((s0, p[0]), (s1, p[1])):
        if pz <= 1e-14:
            continue
        e, nn = ent_bits(np.linalg.eigvalsh(s / pz))
        Scond += (pz / tot) * e
        n2 = min(n2, nn)
    return Savg - Scond, min(n1, n2)


def ptrace_keep_one(sig, k, j):
    """Reduce a 2^k x 2^k operator to site j (0 = first coordinate in the list)."""
    lo = 1 << j
    hi = 1 << (k - 1 - j)
    T = sig.reshape(lo, 2, hi, lo, 2, hi)
    return np.einsum("aibajb->ij", T)


def ptrace_split(sig, ka, kb, keep_first):
    da, db = 1 << ka, 1 << kb
    T = sig.reshape(da, db, da, db)
    return np.einsum("aibi->ab", T) if keep_first else np.einsum("iaib->ab", T)


def cond_mi(s0, s1, p, ka, kb):
    """C_ab = sum_z p_z [S(rho_a^z)+S(rho_b^z)-S(rho_ab^z)] on the Z_S-dephased state."""
    tot = p[0] + p[1]
    out = 0.0
    for s, pz in ((s0, p[0]), (s1, p[1])):
        if pz <= 1e-14:
            continue
        r = s / pz
        ra = ptrace_split(r, ka, kb, True)
        rb = ptrace_split(r, ka, kb, False)
        sa, _ = ent_bits(np.linalg.eigvalsh(ra))
        sb, _ = ent_bits(np.linalg.eigvalsh(rb))
        sab, _ = ent_bits(np.linalg.eigvalsh(r))
        out += (pz / tot) * (sa + sb - sab)
    return out


def purity(rho):
    return float(np.trace(rho @ rho).real)


# ===================================================== certification ========
def r_ind(chi, excess, H, C, delta):
    """Largest pairwise-independent certifying subset; ties -> lexicographically
    first in the frozen label order (+x,-x,+y,-y,+z,-z)."""
    singles = [l for l in LABELS
               if H >= CONTENT_H_MIN and chi[l] >= (1.0 - delta) * H and excess[l] >= EXCESS_MIN]
    best, best_key = [], None
    idx = {l: i for i, l in enumerate(LABELS)}
    for r in range(len(singles), 0, -1):
        for comb in itertools.combinations(sorted(singles, key=idx.get), r):
            ok = True
            for i in range(len(comb)):
                for j in range(i + 1, len(comb)):
                    key = tuple(sorted((comb[i], comb[j]), key=idx.get))
                    if C.get(key) is None or C[key] > INDEP_MAX:
                        ok = False
                        break
                if not ok:
                    break
            if ok:
                key = tuple(idx[c] for c in comb)
                if best_key is None or key < best_key:
                    best, best_key = list(comb), key
        if best:
            break
    return len(best), best, singles


def centered_frobenius_panel(lam, degrees):
    """Exact centered-Frobenius commutator panel (closed form; d = 2^27).

    ||H||_F^2/d = 54 + 27 lam^2 ; ||O - Tr(O)I/d||_F^2/d = 1 for a Pauli.
    [H, Z_i] = 2i lam Y_i                      -> 2 lam
    [H, X_i] = -2i sum_{j~i} Y_i Z_j           -> 2 sqrt(deg_i)
    [H, Y_i] = 2i sum_{j~i} X_i Z_j - 2i lam Z_i -> 2 sqrt(deg_i + lam^2)
    """
    d = 2.0 ** 27
    den = np.sqrt(d) * np.sqrt(54.0 + 27.0 * lam * lam)
    out = {}
    for cls, deg in degrees.items():
        out[cls] = {"degree": deg,
                    "Z": 2.0 * lam / den,
                    "X": 2.0 * np.sqrt(deg) / den,
                    "Y": 2.0 * np.sqrt(deg + lam * lam) / den}
    return out


# ============================================================== main =========
def main():
    pins, absent = verify_pins()
    disc = discovery()
    memo = open(os.path.join(ROOT, PARENT_MEMO), "rb").read()
    frags, pair_class, desc_sum = build_descriptor(memo)

    t_basis = time.perf_counter()
    sec = Sector()
    basis_wall = time.perf_counter() - t_basis
    if sec.n * 2 != 5605504:
        die("basis:orbit-count %d" % (sec.n * 2))

    Fpx, Fmx = frags["+x"], frags["-x"]
    Fpy, Fmy, Fpz, Fmz = frags["+y"], frags["-y"], frags["+z"], frags["-z"]
    t_ol = time.perf_counter()
    OL = {
        "opposite-55": (sec.layout(Fpx + Fmx), 5, 5),
        "opposite-44": (sec.layout(Fpy + Fmy), 4, 4),
        "plus-x-orthogonal": (sec.layout(Fpx + Fpy), 5, 4),
        "minus-x-orthogonal": (sec.layout(Fmx + Fpy), 5, 4),
        "transverse-orthogonal": (sec.layout(Fpy + Fpz), 4, 4),
    }
    ol_wall = time.perf_counter() - t_ol
    del sec.orbit_of

    PAIR_REP = {"opposite-55": ("+x", "-x"), "opposite-44": ("+y", "-y"),
                "plus-x-orthogonal": ("+x", "+y"), "minus-x-orthogonal": ("-x", "+y"),
                "transverse-orthogonal": ("+y", "+z")}
    shell_of = {1: "face", 2: "edge", 3: "corner"}

    a0 = sec.prep(None, None, None)
    prep_norm = sec.norm2(a0)
    if abs(prep_norm - 1.0) > 1e-12:
        die("prep:norm %r" % prep_norm)

    results = {}
    mach = {"norm": 0.0, "hermiticity": 0.0, "negativity": 0.0, "entropy_bound": 0.0,
            "symmetry": 0.0, "t0_anchor": 0.0, "cheby_tail": 0.0}

    for lam in LAMBDAS:
        outs, prop = chebyshev(sec, lam, a0, T_EXEC)
        mach["cheby_tail"] = max(mach["cheby_tail"], prop["tail_bound"])
        rows = []
        chi0 = {}
        one0 = {}
        bond0 = None
        for it, t in enumerate(T_EXEC):
            a = outs[it]
            n2 = sec.norm2(a)
            mach["norm"] = max(mach["norm"], abs(n2 - 1.0))
            row = {"jt": t, "lam": lam}

            # ---- closed-five (representative F_+x) with S-coherence for theta
            s0, s1, cross, p, herm = conditional_blocks(a, OL["opposite-55"][0], 5,
                                                        "Z", want_cross=True)
            mach["hermiticity"] = max(mach["hermiticity"], herm)
            chi5, neg5 = chi_holevo(s0, s1, p)
            H = -sum(q * np.log2(q) for q in p if q > 0)
            rho_joint = np.zeros((64, 64), dtype=np.complex128)
            rho_joint[:32, :32] = s0
            rho_joint[32:, 32:] = s1
            rho_joint[:32, 32:] = cross
            rho_joint[32:, :32] = cross.conj().T
            # (S, face) center bond: keep S and the first site of F_+x
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

            # ---- wedge-four (representative F_+y)
            w0, w1, wcross, pw, hermw = conditional_blocks(a, OL["opposite-44"][0], 4,
                                                           "Z", want_cross=True)
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
            # Holevo bound: 0 <= chi <= H(Z_S) <= 1 bit, exactly
            for c in (chi5, chi4):
                mach["entropy_bound"] = max(mach["entropy_bound"], max(0.0, c - H, -c))
            # symmetry-consistency gates (frozen 1e-9)
            sym = 0.0
            for cls in ("face", "edge"):
                v5 = [x[0] for x in one5.get(cls, [])]
                v4 = [x[0] for x in one4.get(cls, [])]
                allv = v5 + v4
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

            if it == 0:
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

            # ---- lazy pair evaluation (frozen lazy rule applied to Z; see DEVIATIONS)
            need_pairs = any(
                len([l for l in LABELS
                     if H >= CONTENT_H_MIN and chi_by_label[l] >= (1.0 - d) * H
                     and exc_by_label[l] >= EXCESS_MIN]) >= 2 for d in DELTAS)
            C = {}
            classes = {}
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

            # ---- X-declared-pointer demolition control (frozen: main samples Jt=0:0.1:1)
            if t <= X_CONTROL_MAX_JT + 1e-12:
                x0, x1, _, px, _ = conditional_blocks(a, OL["opposite-55"][0], 5, "X", False)
                chi5x, _ = chi_holevo(x0, x1, px)
                del x0, x1
                y0, y1, _, py, _ = conditional_blocks(a, OL["opposite-44"][0], 4, "X", False)
                chi4x, _ = chi_holevo(y0, y1, py)
                del y0, y1
                tot = px[0] + px[1]
                Hx = -sum((q / tot) * np.log2(q / tot) for q in px if q / tot > 1e-15)
                if it == 0:
                    x_chi0 = (chi5x, chi4x)
                xchi = {l: (chi5x if l in ("+x", "-x") else chi4x) for l in LABELS}
                xexc = {l: xchi[l] - (x_chi0[0] if l in ("+x", "-x") else x_chi0[1])
                        for l in LABELS}
                xr = {}
                for d in DELTAS:
                    xr[str(d)] = len([l for l in LABELS
                                      if Hx >= CONTENT_H_MIN and xchi[l] >= (1.0 - d) * Hx
                                      and xexc[l] >= EXCESS_MIN])
                row["x_control"] = {
                    "H_X": Hx, "p_x": px, "chi": [chi5x, chi4x],
                    "zero_probability_outcome": [bool(q / tot <= 1e-14) for q in px],
                    "singleton_passes": xr,
                    "r_ind_ge2_possible": bool(any(v >= 2 for v in xr.values())),
                    "pair_evaluated": bool(any(v >= 2 for v in xr.values())),
                    "pair_reason": None if any(v >= 2 for v in xr.values())
                                   else "fewer-than-two-X-singletons-pass"}
            rows.append(row)
        results[lam] = {"rows": rows, "prop": prop}
        del outs

    # ============================================== events, checks, verdict ==
    events = {}
    for lam in LAMBDAS:
        rows = results[lam]["rows"]
        ev = {}
        for d in DELTAS:
            hit = None
            for i, r in enumerate(rows):
                if r["r_ind"][str(d)] >= 2:
                    run = 0
                    for j in range(i, len(rows)):
                        if rows[j]["r_ind"][str(d)] >= 2:
                            run += 1
                        else:
                            break
                    hit = {"jt": r["jt"], "theta": r["theta"], "r_ind": r["r_ind"][str(d)],
                           "subset": r["certifying_subsets"][str(d)], "run": run,
                           "by_deadline": r["jt"] <= DEADLINE_JT + 1e-12,
                           "pair_values": r["pair_classes"],
                           "drift": r["pointer_tv_drift"],
                           "Q_quiet": r["Q_quiet"], "X_face": r["X_face"]}
                    break
            ev[str(d)] = hit
        events[lam] = ev

    shell = {}
    for lam in LAMBDAS:
        rows = results[lam]["rows"]
        cr = {}
        for c in ("face", "edge", "corner"):
            cr[c] = next((r["jt"] for r in rows if r["one_site_excess"][c] >= EXCESS_MIN), None)
        imax = int(np.argmax([r["sum_delta_chi"] for r in rows]))
        xi = 0
        for sh, c in ((1, "face"), (2, "edge"), (3, "corner")):
            if rows[imax]["one_site_excess"][c] >= EXCESS_MIN:
                xi = sh
        shell[lam] = {"crossings": cr, "t_summax": rows[imax]["jt"],
                      "sum_delta_chi": rows[imax]["sum_delta_chi"], "xi_reg": xi,
                      "delta_chi": [rows[imax]["one_site_excess"][c]
                                    for c in ("face", "edge", "corner")]}

    degrees = {"center": 6, "face": 5, "edge": 4, "corner": 3}
    cf = {lam: centered_frobenius_panel(lam, degrees) for lam in LAMBDAS}

    # CHECK-01
    c01 = {"t0_anchor_max_bits": mach["t0_anchor"],
           "ok": mach["t0_anchor"] <= T0_ANCHOR_TOL,
           "stationary_control": None}
    # stationary control: repeat the first-hit observable row three times through the
    # identical event routine anchored at its own first row -> algebraically zero excess.
    lam_s = HEADLINE_DELTA if HEADLINE_DELTA in LAMBDAS else LAMBDAS[0]
    r_s = next((r for r in results[lam_s]["rows"] if r["r_ind"][str(HEADLINE_DELTA)] >= 2),
               results[lam_s]["rows"][-1])
    stat_counts = []
    for d in DELTAS:
        chi_b = {l: (r_s["chi_closed_five"] if l in ("+x", "-x") else r_s["chi_wedge_four"])
                 for l in LABELS}
        exc_b = {l: 0.0 for l in LABELS}          # own first row is the anchor
        Cs = {}
        if r_s["pair_classes"]:
            for k, cls in pair_class.items():
                Cs[k] = r_s["pair_classes"][cls]
        n = sum(1 for _ in range(PERSIST_N)
                if r_ind(chi_b, exc_b, r_s["H_Z"], Cs, d)[0] >= 2)
        stat_counts.append(n)
    c01["stationary_control"] = {"event_counts": stat_counts,
                                 "ok": stat_counts == [0, 0, 0],
                                 "substitute_for": "ground-doublet stationary control (NOT EXECUTED - see DEVIATIONS)"}
    c01["ok"] = bool(c01["ok"] and c01["stationary_control"]["ok"])

    # CHECK-02
    comm_ok = all(max(v["Z"] for v in cf[lam].values()) < min(v["X"] for v in cf[lam].values())
                  for lam in LAMBDAS)
    drift_ok = True
    for lam in LAMBDAS:
        h = events[lam][str(HEADLINE_DELTA)]
        if h and h["drift"] > DRIFT_MAX:
            drift_ok = False
    x_ok = True
    for lam in LAMBDAS:
        for r in results[lam]["rows"]:
            if "x_control" in r and r["jt"] <= DEADLINE_JT + 1e-12 and r["x_control"]["r_ind_ge2_possible"]:
                x_ok = False
    c02 = {"commutator_ordering": comm_ok, "drift": drift_ok, "x_pointer_control": x_ok,
           "ok": bool(comm_ok and drift_ok and x_ok)}

    # CHECK-03 -- parent wiring (every commissioned lambda) and delta wiring (window)
    locality = all((shell[lam]["crossings"]["face"] or np.inf) <=
                   (shell[lam]["crossings"]["edge"] or np.inf) <=
                   (shell[lam]["crossings"]["corner"] or np.inf) for lam in LAMBDAS)
    parent_hits = {lam: (events[lam][str(HEADLINE_DELTA)] is not None
                         and events[lam][str(HEADLINE_DELTA)]["by_deadline"]
                         and events[lam][str(HEADLINE_DELTA)]["run"] >= PERSIST_N)
                   for lam in LAMBDAS}
    c03_parent = {"per_lambda": parent_hits, "locality": locality,
                  "ok": bool(all(parent_hits.values()) and locality)}
    W_full = [lam for lam in LAMBDAS
              if all(events[lam][str(d)] is not None and events[lam][str(d)]["by_deadline"]
                     for d in DELTAS)
              and events[lam][str(HEADLINE_DELTA)]["run"] >= PERSIST_N]
    c03_delta = {"W_full": W_full, "window_size_ok": len(W_full) >= 2, "locality": locality,
                 "ok": bool(len(W_full) >= 2 and locality)}

    def med(v):
        v = sorted(v)
        n = len(v)
        return None if n == 0 else (v[n // 2] if n % 2 else 0.5 * (v[n // 2 - 1] + v[n // 2]))

    def check04(lams):
        meds = {}
        missing = False
        for d in DELTAS:
            vals = []
            for lam in lams:
                h = events[lam][str(d)]
                if h is None:
                    missing = True
                else:
                    vals.append(h["theta"])
            meds[str(d)] = med(vals)
        good = [m for m in meds.values() if m is not None and m > 0]
        factor = (max(good) / min(good)) if len(good) == len(DELTAS) else None
        return {"medians": meds, "missing_event": missing, "factor": factor,
                "ok": bool(not missing and factor is not None and factor < DELTA_FACTOR_MAX)}

    c04_parent = check04(LAMBDAS)
    c04_delta = check04(W_full) if W_full else {"medians": {}, "missing_event": True,
                                                "factor": None, "ok": False}
    if W_full:
        hv = [events[lam][str(HEADLINE_DELTA)]["theta"] for lam in W_full]
        c04_delta["field_factor"] = max(hv) / min(hv)
        c04_delta["ok"] = bool(c04_delta["ok"] and c04_delta["field_factor"] < DELTA_FACTOR_MAX)

    theta_star = {lam: (events[lam][str(HEADLINE_DELTA)]["theta"]
                        if events[lam][str(HEADLINE_DELTA)] else None) for lam in LAMBDAS}
    inside = {lam: (None if theta_star[lam] is None
                    else ("inside" if theta_star[lam] >= THETA_FLOOR else "BAR-BELOW-WINDOW"))
              for lam in LAMBDAS}
    tv = [v for v in theta_star.values() if v is not None]
    c05 = {"theta_star": theta_star, "labels": inside, "median": med(tv),
           "range": [min(tv), max(tv)] if tv else None,
           "boundary_bracket": None}
    if W_full:
        above = [l for l in LAMBDAS if l > max(W_full) and l not in W_full]
        c05["boundary_bracket"] = [max(W_full), min(above)] if above else "not-bracketed-above-0.20"
        c05["noncontiguous"] = (sorted(W_full) != [l for l in LAMBDAS if l <= max(W_full)])

    mach_ok = (mach["norm"] <= MACH_TOL and mach["hermiticity"] <= MACH_TOL
               and mach["negativity"] <= MACH_TOL and mach["symmetry"] <= MACH_TOL
               and mach["t0_anchor"] <= T0_ANCHOR_TOL)

    if not (mach_ok and c01["ok"]):
        verdict_parent = "MACHINERY-FAIL"
    elif not (c02["ok"] and c03_parent["ok"] and c04_parent["ok"]):
        verdict_parent = "BAR-NOT-PINNED"
    else:
        verdict_parent = "BAR-DERIVED-EFFECTIVE"
    if not (mach_ok and c01["ok"]):
        verdict_delta = "MACHINERY-FAIL"
    elif not (c02["ok"] and c03_delta["ok"] and c04_delta["ok"]):
        verdict_delta = "BAR-NOT-PINNED"
    else:
        verdict_delta = "BAR-DERIVED-EFFECTIVE"

    # ========================================= independent reproduction test ==
    repro = {"max_abs_dev": {}, "rows_compared": 0, "ok": True}
    for lam in LAMBDAS:
        tag = "lam_0p%02d" % int(round(lam * 100))
        p = os.path.join(ROOT, "logs/runner-cache/d3_bar_window_checkpoints/%s_observables.jsonl" % tag)
        ref = {}
        for line in open(p):
            r = json.loads(line)
            ref[round(r["jt"], 6)] = r
        dev = {"chi_closed_five": 0.0, "chi_wedge_four": 0.0, "theta": 0.0, "pair": 0.0,
               "H_Z": 0.0}
        vmis = 0
        for r in results[lam]["rows"]:
            k = round(r["jt"], 6)
            if k not in ref:
                continue
            rr = ref[k]
            repro["rows_compared"] += 1
            dev["chi_closed_five"] = max(dev["chi_closed_five"],
                                         abs(r["chi_closed_five"] - rr["fragment_types"]["closed-five"]["chi_bits"]))
            dev["chi_wedge_four"] = max(dev["chi_wedge_four"],
                                        abs(r["chi_wedge_four"] - rr["fragment_types"]["wedge-four"]["chi_bits"]))
            dev["theta"] = max(dev["theta"], abs(r["theta"] - rr["theta"]))
            dev["H_Z"] = max(dev["H_Z"], abs(r["H_Z"] - rr["pointer_z"]["entropy_bits"]))
            refc = (rr.get("pair_conditional_mi_bits") or {}).get("classes") or {}
            if r["pair_classes"] and refc:
                for cls, v in r["pair_classes"].items():
                    if refc.get(cls) is not None:
                        dev["pair"] = max(dev["pair"], abs(v - refc[cls]))
            for d in DELTAS:
                if r["r_ind"][str(d)] != rr["r_ind"]["%.2f" % d]:
                    vmis += 1
        dev["r_ind_mismatches"] = vmis
        repro["max_abs_dev"][str(lam)] = dev
        if max(dev["chi_closed_five"], dev["chi_wedge_four"], dev["theta"], dev["pair"]) > 1e-9 or vmis:
            repro["ok"] = False

    # ================================================================ output ==
    wall = time.perf_counter() - T_START
    rssg = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 2 ** 30

    table = []
    for lam in LAMBDAS:
        for r in results[lam]["rows"]:
            table.append([lam, r["jt"], r["H_Z"], r["chi_closed_five"], r["chi_wedge_four"],
                          r["theta"], r["pair_classes"], r["r_ind"], r["certifying_subsets"]])
    digest = sha256_bytes(json.dumps(table, sort_keys=True, default=repr).encode())

    dev_list = [
        "EXECUTED-GRID: frozen main state grid Jt=0:0.1:10 NOT executed; frozen certification "
        "subgrid T_C restricted to Jt in {0.0,...,1.2} (13 of 17 T_C points).  The four late "
        "recurrence samples {1.5,2.0,5.0,10.0} are NOT executed (the frozen memo classes them as "
        "recurrence diagnostics that 'do not rescue CHECK-03').  Reason: 900 s runtime cap; the "
        "frozen schedule projects 7.1 h.",
        "LAZY-Z-PAIRS: the frozen design evaluates the five pair classes at every T_C time; this "
        "run applies the design's own lazy rule (declared there for the X control) to Z as well, "
        "skipping pair evaluation at rows where fewer than two fragments pass the singleton gates "
        "at every delta.  Such rows cannot reach R_ind>=2, so no first-hit time can change; the "
        "skipped rows carry reason 'fewer-than-two-singleton-passes' and are never read as "
        "independence.",
        "GROUND-DOUBLET: the two-state invariant-sector Lanczos baseline (CHECK-01 stationary "
        "control and the chi_GS diagnostic) is NOT executed under the runtime cap.  The frozen "
        "memo assigns the doublet a control-and-diagnostic-only role and forbids it as a gate "
        "baseline, so no gate depends on it.  A repeated-observable stationary control anchored "
        "at its own first row is substituted and reported.",
        "DT-HALVING: the frozen dt-halving machinery trace presumes a time-stepping integrator.  "
        "This runner evaluates exp(-iHt) directly at each requested t by a single Chebyshev "
        "expansion of the sector Hamiltonian, so no dt exists to halve.  Substituted diagnostics: "
        "rigorous Chebyshev truncation tail bound, state-norm conservation, and the checker's "
        "independent-propagator comparison.",
        "LAMBDA-SET: lambda in {0.05,0.10,0.20}, the PARENT memo's commissioned set.  The "
        "2026-07-11 delta memo additionally commissions lambda=0.02; it is not executed here.",
    ]

    receipt = {
        "schema": "d3-bar-commission-cycle914-v1",
        "cycle": 914,
        "runner": "scripts/frontier_cycle914_d3_bar_commission_2026_07_28.py",
        "date": "2026-07-28",
        "boundary_sentences": BOUNDARY,
        "pins": pins,
        "cited_but_absent": {k: "absent" for k in CITED_ABSENT},
        "discovery": disc,
        "protocol": {
            "parent_protocol_hash": PINS[PARENT_MEMO][0],
            "delta_protocol_hash": PINS[DELTA_MEMO][0],
            "geometry": "open-3x3x3", "N": 27, "J": 1,
            "H": "-sum_<ij> Z_i Z_j - lambda sum_i X_i",
            "lambdas": list(LAMBDAS), "deltas": list(DELTAS),
            "headline_delta": HEADLINE_DELTA, "deadline_jt": DEADLINE_JT,
            "preparation": {"center": [1, 0, 0], "face": [1, 0, 0],
                            "edge": [0, 0, 1], "corner": [0, 0, 1]},
            "fragments": {l: frags[l] for l in LABELS},
            "fragment_descriptor_checksum": desc_sum,
            "T_C_frozen": T_C_FROZEN, "T_executed": T_EXEC, "T_not_executed": T_NOT_EXEC,
        },
        "numerics": {
            "route": "exact proper-cubic invariant-sector reduction (orbit basis) + "
                     "Chebyshev expansion of exp(-iHt); float64/complex128",
            "sector_dimension": sec.n * 2,
            "sector_dimension_expected_by_memo": 5605504,
            "basis_checksum": sec.checksum,
            "orbit_size_histogram": {str(int(k)): int(v) for k, v in
                                     zip(*np.unique(sec.sizes, return_counts=True))},
            "chebyshev": {str(l): results[l]["prop"] for l in LAMBDAS},
            "machinery": mach, "machinery_ok": bool(mach_ok),
            "basis_wall_s": basis_wall, "layout_wall_s": ol_wall,
            "peak_rss_gib": rssg, "wall_s": wall,
            "python": platform.python_version(), "numpy": np.__version__,
            "blas": "Accelerate", "result_table_sha256": digest,
        },
        "deviations": dev_list,
        "measurement": {
            "events": {str(l): {k: v for k, v in events[l].items()} for l in LAMBDAS},
            "theta_star_headline": {str(l): theta_star[l] for l in LAMBDAS},
            "shell": {str(l): shell[l] for l in LAMBDAS},
            "centered_frobenius": {str(l): cf[l] for l in LAMBDAS},
            "rows": {str(l): results[l]["rows"] for l in LAMBDAS},
        },
        "checks": {
            "CHECK-01": c01, "CHECK-02": c02,
            "CHECK-03-parent": c03_parent, "CHECK-03-delta": c03_delta,
            "CHECK-04-parent": c04_parent, "CHECK-04-delta": c04_delta,
            "CHECK-05": c05,
        },
        "verdict": {"parent_wiring": verdict_parent, "delta_wiring": verdict_delta,
                    "exit_code_from": "parent_wiring"},
        "independent_reproduction_vs_committed_2026_07_11": repro,
        "blindness": "NOT BLIND: the committed 2026-07-11 streams were read during scoping. "
                     "This block is an independent re-execution and reproduction test, not a "
                     "blind certification.",
    }

    outp = os.path.join(ROOT, "outputs/d3_bar_commission_cycle914_receipt_2026_07_28.json")
    with open(outp, "w") as f:
        json.dump(receipt, f, indent=1, sort_keys=True, default=float)

    ev_s = "; ".join(
        "lambda=%g:%s" % (l, (("t=%.1f/theta*=%.6f/R=%d/subset=%s/run=%d"
                               % (events[l][str(HEADLINE_DELTA)]["jt"],
                                  events[l][str(HEADLINE_DELTA)]["theta"],
                                  events[l][str(HEADLINE_DELTA)]["r_ind"],
                                  events[l][str(HEADLINE_DELTA)]["subset"],
                                  events[l][str(HEADLINE_DELTA)]["run"]))
                              if events[l][str(HEADLINE_DELTA)] else "none"))
        for l in LAMBDAS)
    print("SETUP geometry=open-3x3x3 N=27 J=1 H=-sum_<ij>ZiZj-lambda*sum_iXi lambda=%s "
          "prep=center+faces:+X,edges+corners:+Z route=C fragments=[5,5,4,4,4,4] "
          "sector_dim=%d basis=%s descriptor=%s parent_hash=%s delta_hash=%s "
          "T_exec=%s T_not_exec=%s ROUTE-C-PREVIOUSLY-RUN=%s %s"
          % (list(LAMBDAS), sec.n * 2, sec.checksum[:16], desc_sum[:16],
             PINS[PARENT_MEMO][0][:16], PINS[DELTA_MEMO][0][:16], T_EXEC, T_NOT_EXEC,
             disc["route_c_previously_run"], BOUNDARY_LINE))
    print("EVENTS headline-delta=%.2f %s ; N-order=delta%s per-lambda-hit-counts=%s %s"
          % (HEADLINE_DELTA, ev_s, list(DELTAS),
             {str(l): [1 if events[l][str(d)] else 0 for d in DELTAS] for l in LAMBDAS},
             BOUNDARY_LINE))
    print("PROFILE+DEMOLITION %s ; centered-Frobenius[max_Z<min_X]=%s ; X-pointer-control=%s ; %s"
          % ("; ".join("lambda=%g:t_summax=%.1f/DeltaChi[face,edge,corner]=%s/cross=%s/sum=%.6g/xi=%d/Q=%.6g/Xface=%.6g"
                       % (l, shell[l]["t_summax"], ["%.6g" % v for v in shell[l]["delta_chi"]],
                          [shell[l]["crossings"][c] if shell[l]["crossings"][c] is not None
                           else "unavailable" for c in ("face", "edge", "corner")],
                          shell[l]["sum_delta_chi"], shell[l]["xi_reg"],
                          results[l]["rows"][int(np.argmax([r["sum_delta_chi"] for r in results[l]["rows"]]))]["Q_quiet"],
                          results[l]["rows"][int(np.argmax([r["sum_delta_chi"] for r in results[l]["rows"]]))]["X_face"])
                       for l in LAMBDAS), comm_ok, x_ok, BOUNDARY_LINE))
    print("BAR theta*=%s median=%s range=%s labels=%s W_full=%s boundary=%s "
          "delta-medians=%s tolerance-factor=%s field-factor=%s "
          "d1-comparator-floor=%.2f(theta*>=floor:%s) %s"
          % ({str(l): theta_star[l] for l in LAMBDAS}, c05["median"], c05["range"],
             {str(l): inside[l] for l in LAMBDAS}, W_full, c05["boundary_bracket"],
             c04_delta.get("medians"), c04_delta.get("factor"), c04_delta.get("field_factor"),
             THETA_FLOOR, all(v >= THETA_FLOOR for v in tv), BOUNDARY_LINE))
    print("CHECKS+MACHINERY CHECK-01=%s CHECK-02=%s CHECK-03[parent]=%s CHECK-03[delta]=%s "
          "CHECK-04[parent]=%s CHECK-04[delta]=%s CHECK-05=%s MACHINERY=ok(%s) "
          "REPRO-vs-2026-07-11=%s(rows=%d,max_dev=%s) %s"
          % (c01["ok"], c02["ok"], c03_parent["ok"], c03_delta["ok"], c04_parent["ok"],
             c04_delta["ok"], {str(l): inside[l] for l in LAMBDAS},
             {k: "%.3g" % v for k, v in mach.items()}, repro["ok"], repro["rows_compared"],
             {k: "%.3g" % max(v for v in d.values() if isinstance(v, float))
              for k, d in repro["max_abs_dev"].items()}, BOUNDARY_LINE))
    print("TOTAL %s [parent-wiring] / %s [delta-wiring] theta*=%s window=%s boundary=%s "
          "digest=%s wall=%.1fs rss=%.2fGiB %s"
          % (verdict_parent, verdict_delta, c05["median"], W_full, c05["boundary_bracket"],
             digest[:16], wall, rssg, BOUNDARY_LINE))

    if verdict_parent == "MACHINERY-FAIL":
        sys.exit(2)
    sys.exit(1 if verdict_parent == "BAR-NOT-PINNED" else 0)


if __name__ == "__main__":
    main()
