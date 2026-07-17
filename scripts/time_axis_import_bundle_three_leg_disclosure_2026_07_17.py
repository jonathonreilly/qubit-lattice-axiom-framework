#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
time_axis_import_bundle_three_leg_disclosure_2026_07_17.py

Paired runner for

  TIME_AXIS_IMPORT_BUNDLE_THREE_LEG_DISCLOSURE_BOUNDED_NOTE_2026-07-17.md

The note discloses at least three supplied legs consumed by the phrase
"the Z^4 operator block with OS time" (equivalently "Z^3 + tick"):

  leg A -- axis existence / compactification: the representation-faithfulness
           bridge; BOTH sub-legs (realized-history origin, periodic
           compactification) are named OPEN by the time-axis bounded note;
  leg B -- axis label: the axis-label clause of B-AXIS.2; narrow no-go on
           derivability from the current retained surface (that note's own
           scope), with a computed sufficient supplier shape (one per-axis
           Z_2 BC-asymmetry datum, or a declared registration-direction
           bridge);
  leg C -- axis rate / spacing: B-AXIS.1a/1b, supplied, walled by the
           count-not-rate firewalls.

Blocks:
  [L2-W]         leg-B computed witnesses re-run from scratch (numpy; explicit
                 even block (4,4,2,2), antisymmetrized KS hop matrix,
                 time-first phases): exact exchange invariance under periodic
                 BCs, plain-swap falsifier, BC-asymmetry breaking + exact
                 symmetric-BC restoration, kernel-dimension discriminator.
  [REC]          record-layer facts consuming none of legs A-C (exact
                 arithmetic in this block: int/tuple/set/frozenset/dict only):
                 finite replay of index nesting on an eight-history family,
                 existential spatial-nesting failure witnesses, uniqueness on
                 both generic witnesses with named degenerate fixtures and a
                 D0 boundary fixture on which uniqueness persists.
  [SOURCE_GATES] a load-bearing anchor fragment of every consumed clause is
                 literally present (whitespace-normalized substring) in its
                 on-main source file AND in the disclosure note.
  [NOTE_HYGIENE] lexical guards on the note itself (section presence, phrase
                 absence, decimal placement).

All printed numerics are platform-stable (bound booleans, exact discrete
values, integers); no raw noise digits are printed. Deterministic, no RNG.

This runner is a source-note artifact. It does not set or predict an audit
outcome; the independent audit lane is the only authority for effective
status.
"""
from __future__ import annotations

import itertools
import os
import re

import numpy as np

PASS = 0
FAIL = 0
TOL = 1e-11

NOTE_NAME = "TIME_AXIS_IMPORT_BUNDLE_THREE_LEG_DISCLOSURE_BOUNDED_NOTE_2026-07-17.md"
TIME_AXIS_NOTE = "TIME_AXIS_IS_THE_HISTORY_INDEX_RECORD_MONOTONE_DIRECTION_BOUNDED_NOTE_2026-07-03.md"
SINGLE_CLOCK_NOTE = "SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md"
AXIOM_FIRST_NOTE = "AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md"
AXIOMS_FILE = "MINIMAL_AXIOMS_2026-06-29.md"


def record(tag: str, label: str, passed: bool, detail: str = "") -> None:
    global PASS, FAIL
    if passed:
        PASS += 1
    else:
        FAIL += 1
    status = "PASS" if passed else "FAIL"
    print(f"  [{status}][{tag}] {label}" + (f"  -- {detail}" if detail else ""))


def opnorm(A: np.ndarray) -> float:
    return float(np.linalg.norm(A, ord=2))


def read_doc(name: str) -> str:
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "docs", name)
    with open(path, encoding="utf-8") as fh:
        return fh.read()


def normws(s: str) -> str:
    # markdown blockquote markers are formatting, not content -- but only
    # OUTSIDE code fences: strip a leading '>' (with optional indent) from
    # each non-fenced line before whitespace-normalizing, so a quote wrapped
    # across blockquote lines still matches its source while fenced content
    # (e.g. a literal YAML block) is left byte-intact.
    parts = re.split(r"(```.*?```)", s, flags=re.S)
    cleaned = []
    for i, part in enumerate(parts):
        if i % 2 == 0:
            part = re.sub(r"(?m)^[ \t]*>[ \t]?", "", part)
        cleaned.append(part)
    return " ".join("".join(cleaned).split())


def contains_norm(haystack: str, needle: str) -> bool:
    return normws(needle) in normws(haystack)


# ---------------------------------------------------------------------
# leg-B surface: antisymmetrized KS hop matrix, time-first phases
# eta_0 = 1, eta_mu(x) = (-1)^(x_0+...+x_{mu-1}); per-axis BC flags
# (same construction as the single-clock runner; re-built from scratch)
# ---------------------------------------------------------------------


def build_surface(Ls, mass: float = 0.3, apbc=()):
    sites = list(itertools.product(*[range(l) for l in Ls]))
    idx = {s: i for i, s in enumerate(sites)}
    N = len(sites)

    def eta(mu, x):
        return (-1) ** sum(x[:mu])

    M = np.zeros((N, N))
    sectors = []
    for mu in range(4):
        Mmu = np.zeros((N, N))
        for x in sites:
            y = list(x)
            y[mu] = (y[mu] + 1) % Ls[mu]
            bc = -1.0 if (mu in apbc and x[mu] == Ls[mu] - 1) else 1.0
            Mmu[idx[x], idx[tuple(y)]] += bc * eta(mu, x)
            Mmu[idx[tuple(y)], idx[x]] -= bc * eta(mu, x)
        sectors.append(Mmu)
        M += Mmu
    M += mass * np.eye(N)
    return M, sectors, sites, idx


def exchange_W(Ls, sites, idx):
    N = len(sites)
    P = np.zeros((N, N))
    S = np.zeros((N, N))
    for x in sites:
        P[idx[(x[1], x[0], x[2], x[3])], idx[x]] = 1.0
        S[idx[x], idx[x]] = (-1.0) ** (x[0] * x[1])
    return P @ S, P


def block_L2_W():
    print()
    print("-" * 72)
    print("[L2-W] LEG B WITNESSES (re-run from scratch on the explicit block)")
    print("-" * 72)
    Ls = (4, 4, 2, 2)
    mass = 0.3
    M, _, sites, idx = build_surface(Ls, mass)
    N = len(sites)
    W, P = exchange_W(Ls, sites, idx)

    r_orth = opnorm(W @ W.T - np.eye(N))
    record("C", "W = P_{tau<->1} diag((-1)^{x_tau x_1}) is orthogonal",
           r_orth <= TOL,
           f"N = {N} sites; bound resid <= 1e-11: {r_orth <= TOL}")

    r_inv = opnorm(W @ M @ W.T - M)
    record("C", "exact exchange invariance under periodic BCs: W M_KS W^T = M_KS",
           r_inv <= TOL, f"bound resid <= 1e-11: {r_inv <= TOL}")

    naive = opnorm(P @ M @ P.T - M)
    record("D", "falsifier: the plain axis swap WITHOUT the sign field fails, "
           "with residual equal to 4*sqrt(2) on this block",
           abs(naive - 4.0 * np.sqrt(2.0)) <= TOL,
           f"resid = {naive:.4f}; |resid - 4*sqrt(2)| <= 1e-11: "
           f"{abs(naive - 4.0 * np.sqrt(2.0)) <= TOL}")

    M_ap, _, _, _ = build_surface(Ls, mass, apbc=(0,))
    r_ap = opnorm(W @ M_ap @ W.T - M_ap)
    record("C", "antiperiodic-tau / periodic-space BCs break the exchange exactly, "
           "with residual equal to 2*sqrt(2) on this block",
           abs(r_ap - 2.0 * np.sqrt(2.0)) <= TOL,
           f"resid = {r_ap:.6f}; |resid - 2*sqrt(2)| <= 1e-11: True")

    M_both, _, _, _ = build_surface(Ls, mass, apbc=(0, 1))
    r_both = opnorm(W @ M_both @ W.T - M_both)
    record("C", "falsification leg: antiperiodic in BOTH tau and x_1 restores the "
           "exact exchange symmetry -- the selecting datum is the BC ASYMMETRY",
           r_both <= TOL, f"bound resid <= 1e-11: {r_both <= TOL}")

    _, sec_ap, _, _ = build_surface(Ls, 0.0, apbc=(0,))
    kt = int(np.sum(np.abs(np.linalg.eigvals(sec_ap[0])) < 1e-9))
    k1 = int(np.sum(np.abs(np.linalg.eigvals(sec_ap[1])) < 1e-9))
    record("C", "relabeling-invariant kernel discriminator: temporal(apbc) kernel "
           "dimension 0, x_1(pbc) kernel dimension 32",
           kt == 0 and k1 == 32, f"dim ker: temporal(apbc) = {kt}, x_1(pbc) = {k1}")


# ---------------------------------------------------------------------
# [REC] record-layer content licensed WITHOUT import (exact arithmetic)
# ---------------------------------------------------------------------
# A configuration is a dict: site (3-tuple of ints) -> record value (int).
# rec() reads record content as a frozenset of (site, value) pairs.


def rec(cfg):
    return frozenset(cfg.items())


def subset(a, b):
    return a <= b


def comparable(a, b):
    return (a <= b) or (b <= a)


def incomparable(a, b):
    return not comparable(a, b)


def make_stack(history):
    S = {}
    for t, cfg in enumerate(history):
        for site, val in cfg.items():
            S[site + (t,)] = val
    return S


def slice_time(stack, t):
    out = {}
    for key, val in stack.items():
        if key[3] == t:
            out[key[:3]] = val
    return out


def reconstruct(stack, T):
    return tuple(slice_time(stack, t) for t in range(T + 1))


def index_axis_values(stack):
    return frozenset(key[3] for key in stack)


def spatial_recset_identified(history, axis, a):
    out = set()
    for t, cfg in enumerate(history):
        for site, val in cfg.items():
            if site[axis] == a:
                reduced = tuple(site[i] for i in range(3) if i != axis)
                out.add((reduced + (t,), val))
    return frozenset(out)


def monotone_directions(history):
    out = set()
    T = len(history) - 1
    if all(subset(rec(history[t]), rec(history[t + 1])) for t in range(T)):
        out.add("index")
    for axis, name in ((0, "x1"), (1, "x2"), (2, "x3")):
        a0 = spatial_recset_identified(history, axis, 0)
        a1 = spatial_recset_identified(history, axis, 1)
        if comparable(a0, a1):
            out.add(name)
    return frozenset(out)


WINDOW = frozenset((a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1))
HISTORY = ({(0, 0, 0): 1},
           {(0, 0, 0): 1, (1, 1, 1): 1},
           {(0, 0, 0): 1, (1, 1, 1): 1, (0, 1, 0): 1, (1, 0, 1): 1})
HISTORY_B = ({(1, 1, 1): 1},
             {(1, 1, 1): 1, (0, 0, 0): 1},
             {(1, 1, 1): 1, (0, 0, 0): 1, (1, 0, 0): 1, (0, 1, 1): 1})
SINGLE = ({}, {(0, 0, 0): 1})
UNIFORM_BURST = ({}, {(0, 0, 0): 1, (1, 0, 0): 1})
TRANS_INVARIANT = ({},
                   {(0, 0, 0): 1, (1, 0, 0): 1},
                   {(0, 0, 0): 1, (1, 0, 0): 1, (0, 1, 0): 1, (1, 1, 0): 1})
FACE_CONFINED = ({},
                 {(0, 0, 0): 1},
                 {(0, 0, 0): 1, (0, 1, 0): 1, (0, 0, 1): 1})
C_FULL = {s: 1 for s in WINDOW}
STATIC = (C_FULL, C_FULL, C_FULL)
C_ASYM = {(0, 0, 1): 1, (0, 1, 0): 1, (1, 0, 0): 1}
STATIC_ASYM = (C_ASYM, C_ASYM, C_ASYM)
ALL_HISTORIES = (HISTORY, HISTORY_B, SINGLE, UNIFORM_BURST,
                 TRANS_INVARIANT, FACE_CONFINED, STATIC, STATIC_ASYM)


def block_REC():
    print()
    print("-" * 72)
    print("[REC] RECORD-LAYER FACTS CONSUMING NONE OF LEGS A-C (exact arithmetic)")
    print("-" * 72)

    stack = make_stack(HISTORY)
    T = len(HISTORY) - 1
    ok = all(stack.get(site + (t,)) == val
             for t, cfg in enumerate(HISTORY) for site, val in cfg.items())
    ok = ok and all(HISTORY[key[3]].get(key[:3]) == val for key, val in stack.items())
    ok = ok and reconstruct(stack, T) == HISTORY
    ok = ok and index_axis_values(stack) == frozenset(range(T + 1))
    record("A", "stacked representation exact: S[(x,t)] = h_t at x, no phantom "
           "cells, full round-trip, 4th-axis coordinate set = {0..T}", ok)

    record("A", "(i) UNIVERSAL: the history index nests for EVERY realized history "
           "in the eight-history family (incl. all degeneracy members)",
           all("index" in monotone_directions(h) for h in ALL_HISTORIES),
           "finite replay of the source proposition on this witness family, "
           "grounded on the landed permanence sentence (records are permanent)")

    record("A", "generic witness is event-bearing: at least one strict record "
           "inclusion step",
           any(rec(HISTORY[t]) < rec(HISTORY[t + 1]) for t in range(T)))

    for axis, name in ((0, "x1"), (1, "x2"), (2, "x3")):
        a0 = spatial_recset_identified(HISTORY, axis, 0)
        a1 = spatial_recset_identified(HISTORY, axis, 1)
        record("A", f"(ii) EXISTENTIAL: generic witness -- {name} translation-"
               "identified opposite slices incomparable (spatial nesting fails)",
               incomparable(a0, a1))

    b0 = spatial_recset_identified(HISTORY_B, 1, 0)
    b1 = spatial_recset_identified(HISTORY_B, 1, 1)
    record("A", "(ii) symmetry-related second witness (window-automorphism image of "
           "the generic witness): x2 slices incomparable while its index still nests",
           incomparable(b0, b1) and "index" in monotone_directions(HISTORY_B))

    record("A", "(iii) uniqueness on the generic witness: the history index is the "
           "UNIQUE record-monotone direction",
           monotone_directions(HISTORY) == frozenset({"index"}))

    record("A", "(iii) degeneracy D1 single-record: NOT unique (empty opposite "
           "slices comparable by convention)",
           monotone_directions(SINGLE) > frozenset({"index"}))

    u0 = spatial_recset_identified(UNIFORM_BURST, 0, 0)
    u1 = spatial_recset_identified(UNIFORM_BURST, 0, 1)
    record("A", "(iii) degeneracy D1 uniform-burst: NOT unique (x1 slices "
           "translation-identified EQUAL)",
           monotone_directions(UNIFORM_BURST) > frozenset({"index"}) and u0 == u1)

    t0 = spatial_recset_identified(TRANS_INVARIANT, 0, 0)
    t1 = spatial_recset_identified(TRANS_INVARIANT, 0, 1)
    record("A", "(iii) degeneracy D1 translation-invariant growth: NOT unique "
           "(x1 slices EQUAL at every step)",
           monotone_directions(TRANS_INVARIANT) > frozenset({"index"}) and t0 == t1)

    fc1 = spatial_recset_identified(FACE_CONFINED, 0, 1)
    record("A", "(iii) degeneracy D1 face-confined: NOT unique (records confined "
           "to the x1=0 face; x1=1 slice empty)",
           monotone_directions(FACE_CONFINED) > frozenset({"index"})
           and fc1 == frozenset())

    record("A", "(iii) degeneracy D0 static (event-free): every stack direction "
           "trivially monotone (marking non-unique)",
           monotone_directions(STATIC) == frozenset({"index", "x1", "x2", "x3"}))

    record("A", "(iii) uniqueness on the second symmetry-related witness",
           monotone_directions(HISTORY_B) == frozenset({"index"}))

    record("A", "(iii) boundary fact: a spatially translation-inequivalent STATIC "
           "history retains index-uniqueness -- D0 membership does not force "
           "non-uniqueness (non-uniqueness is exhibited on fixtures, not "
           "characterized)",
           monotone_directions(STATIC_ASYM) == frozenset({"index"}))


# ---------------------------------------------------------------------
# [SOURCE_GATES] anchor fragments of consumed clauses present in source
# AND in the note
# ---------------------------------------------------------------------

GATES = (
    ("leg A header", TIME_AXIS_NOTE,
     "The representation bridge is OPEN; this note does not close B-AXIS."),
    ("leg A both sub-legs", TIME_AXIS_NOTE,
     "Both legs — realized-history origin and periodic compactification — "
     "are named OPEN. Not proved here."),
    ("leg C firewall", TIME_AXIS_NOTE,
     "No time metric, clock rate, blocked step, or spacing is derived; "
     "B-AXIS.1a/1b stay as supplied, walled by the count-not-rate firewalls "
     "(unaudited post-reset)."),
    ("leg B narrow no-go", SINGLE_CLOCK_NOTE,
     "so the axis-label component of B-AXIS.2 (= scope-boundary N4) is not "
     "derivable from the current retained surface."),
    ("leg B pin datum", SINGLE_CLOCK_NOTE,
     "one per-axis Z_2 boundary-condition asymmetry datum "
     "(antiperiodic-tau/periodic-space) breaks the exchange exactly"),
    ("leg B record-shaped supplier", SINGLE_CLOCK_NOTE,
     "a declared registration-direction bridge is the record-shaped equivalent."),
    ("B-AXIS.1 clause", AXIOM_FIRST_NOTE,
     "(B-AXIS.1) one supplied blocked time step `2a_τ` (= N2), now split"),
    ("B-AXIS.2 clause", AXIOM_FIRST_NOTE,
     "(B-AXIS.2) one declared evolution axis carrying one RP/transfer construction"),
    ("B-AXIS.3 clause", AXIOM_FIRST_NOTE,
     "(B-AXIS.3) no independent commuting transfer factor is admitted as a "
     "second physical clock (= N5)."),
    ("Record permanence sentence", AXIOMS_FILE,
     "When present, a record locks exactly one admissible local possibility. "
     "A site never carries more than one record; records are permanent."),
)


def block_SOURCE_GATES():
    print()
    print("-" * 72)
    print("[SOURCE_GATES] anchor fragments of consumed clauses present in source "
          "AND in the note")
    print("-" * 72)
    note = read_doc(NOTE_NAME)
    cache = {}
    for label, src_name, needle in GATES:
        if src_name not in cache:
            cache[src_name] = read_doc(src_name)
        in_src = contains_norm(cache[src_name], needle)
        in_note = contains_norm(note, needle)
        record("B", f"gate ({label}): anchor fragment present in `{src_name}` AND "
               "in the disclosure note", in_src and in_note,
               f"in source: {in_src}, in note: {in_note}")


# ---------------------------------------------------------------------
# [NOTE_HYGIENE] structural guards on the note itself
# ---------------------------------------------------------------------


def strip_code(text: str) -> str:
    out = re.sub(r"```.*?```", "", text, flags=re.S)
    out = re.sub(r"`[^`]*`", "", out)
    return out


def block_NOTE_HYGIENE():
    print()
    print("-" * 72)
    print("[NOTE_HYGIENE] structural guards on the note")
    print("-" * 72)
    note = read_doc(NOTE_NAME)

    record("D", "type/claim-strength/status-authority lines present (audit lane is "
           "the sole status authority)",
           "**Type:**" in note and "**Claim strength:**" in note
           and "**Status authority:**" in note
           and "does not set or predict an audit outcome" in note)

    required = ("## Purpose", "## Supplied objects", "## Declared symbols",
                "## Bounded consequence", "## Honest auditor read", "## Non-claims",
                "## Relation to prior notes", "## Load-bearing dependencies",
                "## Runner verification map")
    missing = [s for s in required if s not in note]
    record("D", "required sections present",
           not missing, f"missing: {missing or 'none'}")

    banned = ("only route", "last route", "exhaust", "closes the",
              "route is closed", "no further route", "the axis is hereby derived",
              "bijection", "minimal supplier")
    hits = [b for b in banned if b in note.lower()]
    record("D", "pinned closing/derivation phrases absent",
           not hits, f"hits: {hits or 'none'}")

    stripped = strip_code(note)
    dec = re.search(r"\d\.\d", stripped)
    record("D", "no prose decimals outside code fences/backticks",
           dec is None, f"first hit: {dec.group(0) if dec else 'none'}")


# ---------------------------------------------------------------------
# main
# ---------------------------------------------------------------------


def main() -> None:
    print("=" * 72)
    print("TIME-AXIS IMPORT BUNDLE: THREE-LEG DISCLOSURE RUNNER (2026-07-17)")
    print("=" * 72)
    print()
    print("Discloses at least three supplied legs consumed by 'the Z^4 operator")
    print("block with OS time': leg A (axis existence/compactification, OPEN),")
    print("leg B (axis label, sufficient supplier shape computed), leg C")
    print("(rate/spacing, supplied). Re-runs the computable witnesses and gates")
    print("a load-bearing anchor fragment of every consumed clause.")

    block_L2_W()
    block_REC()
    block_SOURCE_GATES()
    block_NOTE_HYGIENE()

    print()
    print("=" * 72)
    print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
    print("=" * 72)
    if FAIL:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
