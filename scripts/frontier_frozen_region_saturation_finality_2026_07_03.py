#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_frozen_region_saturation_finality_2026_07_03.py

Exact-arithmetic runner for the bounded + narrow-scoped theorems of the note:
  docs/FROZEN_REGION_RECORD_SATURATION_LOCAL_FINALITY_BOUNDARY_INFLUENCE_BOUNDED_NOTE_2026-07-03.md

Audit status is set only by the independent audit lane; nothing here is adopted,
promoted, or ruled, and no audit outcome is predicted.

Conventions (exactness firewall):
  * Exact only -- Python int / tuple / set / frozenset. NO float anywhere.
  * A "site" is a point of Z^3 as a 3-tuple of ints.
  * A record's locked value is modelled at the NOTE level by a 2-value scalar
    tag in {+1, -1} (Python ints 1, -1). This is the note-level model of the
    Record axiom's locking of one available local possibility; it is NOT a
    claim about the full one-site M_2(C) possibility domain.
  * A configuration C is a dict {site: locked_value}: "site carries a record
    with that locked value"; sites absent from C carry no record.
  * A history is a finite tuple (C_0, ..., C_T).

Layering of the derivations (this repair makes the halting content reading-free):
  * DOMAIN MONOTONICITY (permanence-derived, reading-free). Under permanence
    (LANDED on main, commit 50f0db6187; drafted as PR #4874, review-loop-closed;
    wording "records are permanent.") together with "A state is a configuration
    of records", record
    sets are nested along a realized history and locked values agree on the
    smaller domain, so the recorded-site domain grows monotonically:
    dom(C_{t-1}) subset of dom(C_t). A FIRST-REGISTRATION (dom-event) at stage t
    is a site in dom(C_t) \\ dom(C_{t-1}). Monotonicity is the primary lever for
    T2's halting and T4's finite-lattice bound; it needs no reading beyond
    permanence.
  * MODEL POSTULATE M1 (one-per-site content now GROUNDED on landed axiom text).
    Reading "A state is a configuration of records" plus the singular "a record
    locks exactly one admissible local possibility" phrasing, a state is a
    site-functional SET of records, each individuated as (site, value), with at
    most one record per site; a same-value re-registration is the SAME element (a
    non-event by identity, not by prohibition). M1's one-per-site content is
    GROUNDED on the LANDED axiom sentence "A site never carries more than one
    record." (commit 7950d9202c, PR #4879 "axioms: restore one record per site"),
    so the M1-load-bearing results no longer carry a reading residue. The Record
    readout clause quantifies over "any finite collection of pairwise-disjoint
    records", which contemplates non-disjoint (overlapping, same-site) records and
    merely withholds additivity from them; the landed one-per-site sentence fixes
    the site-functional individuation. M1 is load-bearing ONLY for T1's
    set-constancy 4^8 enumeration and T4's distinct-record pigeonhole tail. Event
    layering: a same-value re-registration is a non-event under BOTH the dom-based
    definition (no domain growth) and the M1 set definition (same element). M1's
    mathematical content is unchanged; only its grounding status moved from
    model-postulate-pending to grounded on landed axiom text.

The covariant neighbor-dependent availability rule and the record-inclusion
event-ordering are REBUILT here from scratch (small exact windows). PR #4882 is
context only and is not load-bearing. The frozen-star / black-hole label is an
owner interpretive READING, not a claim; this runner asserts no GR content (no
metric, horizon, curvature) and no rate / clock content.
"""

import itertools
import os
import re
import sys

# ---------------------------------------------------------------------------
# check harness -- "CHECK NN: PASS/FAIL -- desc", TOTAL line, nonzero exit on FAIL
# ---------------------------------------------------------------------------
_RESULTS = []


def check(desc, ok):
    n = len(_RESULTS) + 1
    _RESULTS.append(bool(ok))
    print("CHECK %02d: %s -- %s" % (n, "PASS" if ok else "FAIL", desc))


def finish():
    passed = sum(1 for r in _RESULTS if r)
    total = len(_RESULTS)
    print("TOTAL: PASS=%d FAIL=%d" % (passed, total - passed))
    sys.exit(0 if passed == total else 1)


# ---------------------------------------------------------------------------
# exact lattice + model primitives
# ---------------------------------------------------------------------------
UNIT = ((1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1))
FULL = frozenset((1, -1))  # note-level 2-value possibility set {+1,-1}


def add(s, v):
    return (s[0] + v[0], s[1] + v[1], s[2] + v[2])


def neighbors(s):
    return tuple(add(s, u) for u in UNIT)


def neighbor_values(s, C):
    """Recorded-neighbor value set V(s) = { C[nb] : nb a neighbor of s, nb in C }.
    Under permanence this set is monotonically nondecreasing along a history."""
    return frozenset(C[nb] for nb in neighbors(s) if nb in C)


def available_at(s, C):
    """Covariant neighbor-dependent availability rule (rebuilt exactly):
    available_at(s) = V(s) = { locked values of records on nearest neighbors of
    s } if that set is nonempty, else the full possibility set {+1,-1}."""
    v = neighbor_values(s, C)
    return v if v else FULL


def registrable_sites(R, C):
    """Sites of region R carrying no record (a new registration could occur)."""
    return frozenset(s for s in R if s not in C)


def readout(C):
    """Scalar readout modelled as the exact integer sum of locked values;
    additive over disjoint record collections, readout(empty)=0."""
    total = 0
    for v in C.values():
        total += v
    return total


def block(ranges):
    """Cartesian-product block of Z^3 as a frozenset of sites."""
    xs, ys, zs = ranges
    return frozenset((x, y, z) for x in xs for y in ys for z in zs)


def events(prev, cur):
    """First-registrations (dom-events) from configuration prev to cur:
    dom(cur) \\ dom(prev). A same-value re-registration is NOT an event."""
    return frozenset(s for s in cur if s not in prev)


def nested_with_agreement(hist):
    """Permanence + state-as-record-configuration => record sets nested and
    locked values agree on the smaller domain, at every succession step; hence
    the recorded-site domain is monotone (dom(prev) subset of dom(cur))."""
    for i in range(1, len(hist)):
        prev, cur = hist[i - 1], hist[i]
        if not all(s in cur for s in prev):
            return False
        if not all(cur[s] == prev[s] for s in prev):
            return False
    return True


# ---------------------------------------------------------------------------
# Quote guards -- the note's quotes must match docs/MINIMAL_AXIOMS_2026-06-29.md.
# Five live guards: Record locking (with one-per-site + permanence),
# Admissibility, state-as-configuration (M1 basis), Lattice, and Record
# readout-additivity. Qubit is cited but carries no quote. The Record locking
# guard keys to the CURRENT landed Record section: "When present, a record locks
# exactly one admissible local possibility. A site never carries more than one
# record; records are permanent." The one-per-site sentence "A site never carries
# more than one record." landed at commit 7950d9202c (PR #4879 "axioms: restore
# one record per site"); permanence ("records are permanent.") landed earlier at
# commit 50f0db6187 (PR #4874). The transitional either-or that survived the
# landing race is retired; this guards the current text alone and fails on any
# further change to the Record locking paragraph.
# ---------------------------------------------------------------------------
def axioms_normalized():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, os.pardir, "docs", "MINIMAL_AXIOMS_2026-06-29.md")
    with open(path, "r", encoding="utf-8") as fh:
        return re.sub(r"\s+", " ", fh.read())


def quote_guards():
    try:
        txt = axioms_normalized()
    except Exception:
        txt = None
    rec = ("When present, a record locks exactly one admissible local "
           "possibility. A site never carries more than one record; records "
           "are permanent.")   # CURRENT landed Record section (7950d9202c + 50f0db6187)
    adm = ("the available possibilities are determined by, and vary with, the "
           "nearest-neighbor conditions")
    stt = "A state is a configuration of records."
    lat = ("Physical sites are the points of the cubic lattice `Z^3`, with "
           "nearest-neighbor adjacency, standard translations, and proper cubic "
           "rotations about each site.")
    rda = ("For any finite collection of pairwise-disjoint records, scalar "
           "readout `I` is additive, with `I(empty)=0`.")
    # LIVE guard on the current landed Record section. The one-per-site sentence
    # "A site never carries more than one record." landed at commit 7950d9202c
    # (PR #4879); permanence ("records are permanent.") landed at 50f0db6187
    # (PR #4874); readout-invariance survives as a derived lemma. The transitional
    # either-or is retired -- this guards the current text alone.
    check("quote guard: current Record section 'When present, a record locks "
          "exactly one admissible local possibility. A site never carries more "
          "than one record; records are permanent.' present verbatim -- landed "
          "one-per-site (commit 7950d9202c, PR #4879) and permanence (commit "
          "50f0db6187) are authoritative",
          txt is not None and rec in txt)
    check("quote guard: Admissibility 'determined by, and vary with, the "
          "nearest-neighbor conditions' present verbatim",
          txt is not None and adm in txt)
    check("quote guard: 'A state is a configuration of records.' present "
          "verbatim (named basis for model postulate M1)",
          txt is not None and stt in txt)
    check("quote guard: Lattice 'Physical sites are the points of the cubic "
          "lattice Z^3 ... proper cubic rotations about each site.' present "
          "verbatim (guards the load-bearing infinite-lattice sentence)",
          txt is not None and lat in txt)
    check("quote guard: Record readout 'For any finite collection of "
          "pairwise-disjoint records, scalar readout I is additive, with "
          "I(empty)=0.' present verbatim (guards the pairwise-disjoint clause)",
          txt is not None and rda in txt)


# ===========================================================================
# T1 -- SATURATION IMPLIES LOCAL FINALITY (bounded; permanence LANDED 50f0db6187,
#       set-constancy grounded on landed one-per-site M1, commit 7950d9202c)
# ===========================================================================
def T1():
    # exact saturated windows: one record per site, all locked +1
    R2 = block((range(2), range(2), range(2)))   # 2x2x2 = 8 sites
    R3 = block((range(3), range(3), range(3)))   # 3x3x3 = 27 sites
    C2 = {s: 1 for s in R2}
    C3 = {s: 1 for s in R3}

    check("T1 2x2x2 window record-saturated (|R|=8) => zero registrable sites in R",
          len(R2) == 8 and len(registrable_sites(R2, C2)) == 0)
    check("T1 3x3x3 window record-saturated (|R|=27) => zero registrable sites in R",
          len(R3) == 27 and len(registrable_sites(R3, C3)) == 0)

    # PRIMARY (dom-based, reading-free): permanence => domain monotone, so once R
    # is saturated R subset of dom(C_t) at every later stage and NO first-
    # registration (dom-event) can occur in R again. No per-site uniqueness.
    fin_hist = (dict(C2),
                {**C2, (2, 0, 0): 1},
                {**C2, (2, 0, 0): 1, (2, 1, 0): 1})
    R_in_dom = all(all(s in H for s in R2) for H in fin_hist)
    dom_events_in_R = tuple(len(events(fin_hist[i - 1], fin_hist[i]) & R2)
                            for i in range(1, len(fin_hist)))
    check("T1 dom-based finality (reading-free, primary): R saturated => R subset "
          "of dom(C_t) at every later stage (domain monotone under permanence), "
          "so zero first-registrations in R thereafter -- no per-site uniqueness",
          R_in_dom and dom_events_in_R == (0, 0))

    # STRONGER (model-relative, uses M1): the record SET on R is FORCED constant.
    # The candidate alphabet is a MODEL-RELATIVE device --
    #   'absent' -> record removed        : barred by permanence
    #   +1 / -1  -> a locked value        : value change (alteration) barred by permanence
    #   'double' -> a second, DISTINCT record : inexpressible inside the partial-map
    #               model and only multi-valued outside it; barred by M1
    #               (site-functional set, at most one record per site).
    ALPHABET = ("absent", 1, -1, "double")
    sites = sorted(R2)

    def guard_ok(site, tag):
        if tag == "absent":
            return False                 # removal barred by permanence
        if tag == "double":
            return False                 # second record barred by M1 (site-functional set)
        return tag == C2[site]           # only the unchanged locked value survives

    survivors = [combo for combo in itertools.product(ALPHABET, repeat=len(sites))
                 if all(guard_ok(site, tag) for site, tag in zip(sites, combo))]
    check("T1 M1 set-constancy (model-relative): over the 4^8 model-relative "
          "candidate R-restrictions, exactly one survives permanence (no removal/"
          "alteration) + M1 (no second record), and it equals C|R -- the record "
          "set on R is constant",
          len(survivors) == 1
          and dict(zip(sites, survivors[0])) == {s: C2[s] for s in sites})
    check("T1 guards have teeth: removal (permanence), alteration (permanence), "
          "and second-record 'double' (M1) candidates are each rejected",
          (not guard_ok(sites[0], "absent"))
          and (not guard_ok(sites[0], -1))
          and (not guard_ok(sites[0], "double")))

    # global corollary (RULE-DEPENDENT, within the note-level model): the all-(+1)
    # saturated config is admissible against the EXHIBITED availability rule, and
    # readout is additive over disjoint sub-collections with readout(empty)=0.
    admissible = all(C2[s] in available_at(s, C2) for s in R2)
    Ha = {s: C2[s] for s in R2 if s[0] == 0}
    Hb = {s: C2[s] for s in R2 if s[0] == 1}
    check("T1 global corollary (rule-dependent): all-(+1) saturated config "
          "admissible under the exhibited rule (each locked value lies in its "
          "neighbor-determined availability set); readout additive over disjoint "
          "halves; readout(empty)=0",
          admissible and readout({}) == 0
          and readout(C2) == readout(Ha) + readout(Hb) == 8)

    # discriminating control (RULE-DEPENDENT): flipping one CORNER site (the 2x2x2
    # block has no interior site) to -1 amid +1 neighbors yields NON-admissible
    # under the exhibited rule. A different covariant rule could reverse both
    # this and the all-(+1) verdict above (rule-dependence residue, T1 corollary).
    Cbad = dict(C2)
    Cbad[(0, 0, 0)] = -1
    bad_ok = all(Cbad[s] in available_at(s, Cbad) for s in R2)
    check("T1 discriminating control (rule-dependent): flipping one CORNER site "
          "(0,0,0) to -1 amid +1 neighbors yields a NON-admissible config under "
          "the exhibited rule (check has teeth)",
          (not bad_ok) and (Cbad[(0, 0, 0)] not in available_at((0, 0, 0), Cbad)))


# ===========================================================================
# T2 -- LOCAL RECORD-TIME STOPS (bounded; permanence LANDED 50f0db6187)
#   Primary derivation is dom-based (reading-free): saturation => the region is
#   inside the monotone domain forever => in-region first-registrations halt.
# ===========================================================================
def T2():
    R = block((range(2), range(2), range(2)))          # region, 8 sites
    C0 = {}
    C1 = {(0, y, z): 1 for y in range(2) for z in range(2)}      # 4 R-events (x=0)
    C2 = dict(C1)
    C2.update({(1, y, z): 1 for y in range(2) for z in range(2)})  # +4 R-events => R saturated
    C3 = dict(C2)
    C3.update({(2, 0, 0): 1, (2, 0, 1): 1})            # 2 outside events
    C4 = dict(C3)
    C4.update({(2, 1, 0): 1, (3, 0, 0): 1})            # 2 outside events
    hist = (C0, C1, C2, C3, C4)

    check("T2 permanence: record sets nested and locked values agree at every "
          "succession step (recorded-site domain monotone, dom(prev) subset dom(cur))",
          nested_with_agreement(hist))

    r_sat = tuple(all(s in hist[t] for s in R) for t in range(len(hist)))
    check("T2 region R unsaturated at stage 1, saturated at stage 2 (a frozen "
          "region is produced)",
          (r_sat[1] is False) and (r_sat[2] is True))

    # dom-based halting (reading-free): in-R first-registration (dom-event) count
    # goes to zero once R is inside the monotone domain; outside events continue.
    in_R = tuple(len(events(hist[t - 1], hist[t]) & R) for t in range(1, len(hist)))
    out_R = tuple(len(events(hist[t - 1], hist[t]) - R) for t in range(1, len(hist)))
    check("T2 in-R first-registration counts == (4,4,0,0): the dom-event count in "
          "R halts after saturation (local record-time in R ends) -- reading-free",
          in_R == (4, 4, 0, 0))
    check("T2 outside-R first-registration counts == (0,0,2,2): events continue "
          "on the unsaturated complement at stages 3,4",
          out_R == (0, 0, 2, 2))

    r_count = tuple(len(set(hist[t]) & R) for t in range(len(hist)))
    check("T2 recorded-site count in R is constant (==8) for stages 2,3,4 -- "
          "record-time in R is halted",
          r_count[2] == r_count[3] == r_count[4] == 8)

    out_cum = tuple(len(set(hist[t]) - R) for t in range(len(hist)))
    check("T2 outside-R record count strictly increases at stages 3 and 4 while "
          "R is frozen (time flows where unwritten possibility remains)",
          out_cum[2] < out_cum[3] < out_cum[4])

    # event-definition layering (explicit): a same-value re-registration is a
    # NON-EVENT under BOTH definitions -- zero domain growth (dom-based) and the
    # same (site,value) element (M1 set).
    C2_re = dict(hist[2]); C2_re[(0, 0, 0)] = 1        # re-register an existing +1
    dom_growth = len(events(hist[2], C2_re))
    m1_same = (frozenset((s, hist[2][s]) for s in hist[2])
               == frozenset((s, C2_re[s]) for s in C2_re))
    check("T2 event-definition layering: a same-value re-registration at an "
          "already-recorded site is a NON-EVENT under both definitions -- zero "
          "domain growth (dom-based) and the same (site,value) element (M1)",
          dom_growth == 0 and m1_same)


# ===========================================================================
# T3 -- BOUNDARY INFLUENCE WITHOUT EVOLUTION (bounded)
#   General content: MONOTONE CONTAINMENT (the region value stays available at a
#   neighbor forever). Full SINGLETON pinning holds exactly for CAVITY sites.
# ===========================================================================
def rotate_z(s):
    x, y, z = s
    return (-y, x, z)   # proper cubic rotation about the z-axis (det +1)


def T3():
    R = block((range(2), range(2), range(2)))
    base = {s: 1 for s in R}                 # saturated block, all +1
    s_bd = (2, 0, 0)                         # outside boundary site; neighbor (1,0,0) in R
    f_far = (5, 5, 5)                         # far outside site; no recorded neighbors
    G1 = dict(base)
    G2 = dict(G1); G2[(0, 0, 7)] = 1          # distant event, not adjacent to s_bd or f_far
    G3 = dict(G2); G3[(0, 7, 0)] = 1          # distant event
    ghist = (G1, G2, G3)

    # general content: MONOTONE CONTAINMENT. V(s_bd) is monotonically
    # nondecreasing under permanence; the region value +1 is available forever.
    Vseq = tuple(neighbor_values(s_bd, H) for H in ghist)
    mono = all(Vseq[i - 1] <= Vseq[i] for i in range(1, len(Vseq)))
    contains_region_value = all(1 in available_at(s_bd, H) for H in ghist)
    check("T3 monotone containment (general, within the note-level model): the "
          "recorded-neighbor value set at a boundary site is monotonically "
          "nondecreasing under permanence, and the region value +1 stays "
          "available at every stage (once available it never leaves)",
          mono and contains_region_value and Vseq[0] == frozenset((1,)))

    # seat-1 RELAXATION counterexample: a later ADMISSIBLE -1 record on a
    # DIFFERENT neighbor of s_bd relaxes availability {+1} -> {+1,-1}. The
    # singleton pin is NOT permanent for a boundary site; only containment is.
    diff_nb = (3, 0, 0)                       # neighbor of s_bd, distinct from in-R (1,0,0)
    before = dict(base)
    minus_admissible = (-1) in available_at(diff_nb, before)   # neighbors unrecorded => FULL
    after = dict(before); after[diff_nb] = -1
    relaxed = available_at(s_bd, after)
    check("T3 relaxation counterexample (exact): an admissible -1 on a DIFFERENT "
          "neighbor (3,0,0) relaxes availability at the boundary site from {+1} "
          "to {+1,-1} -- the singleton pin is NOT permanent; +1 stays available "
          "(monotone containment survives the relaxation)",
          available_at(s_bd, before) == frozenset((1,))
          and minus_admissible
          and relaxed == FULL
          and (1 in relaxed)
          and diff_nb in neighbors(s_bd) and diff_nb != (1, 0, 0))

    # CAVITY singleton pinning (exact): a cavity site -- all six neighbors inside
    # the saturated region -- is pinned to {+1} FOREVER, regardless of any outside
    # events. Shell = 3x3x3 minus its center; cavity c = the (unrecorded) center.
    shell = block((range(3), range(3), range(3))) - frozenset({(1, 1, 1)})
    cav_base = {s: 1 for s in shell}          # 26-site saturated shell, all +1
    c = (1, 1, 1)
    all_nb_in_shell = all(nb in shell for nb in neighbors(c))
    K1 = dict(cav_base)
    K2 = dict(K1); K2[(9, 0, 0)] = -1         # admissible far -1 (its neighbors unrecorded)
    K3 = dict(K2); K3[(0, 0, 9)] = 1          # further outside event
    khist = (K1, K2, K3)
    cav_pin = tuple(available_at(c, H) for H in khist)
    far_minus_admissible = (-1) in available_at((9, 0, 0), K1)
    check("T3 cavity singleton pinning (exact, within the note-level model): a "
          "cavity site with all six neighbors inside the saturated shell has "
          "availability {+1} at every stage regardless of arbitrary outside "
          "events (incl. an admissible far -1) -- full singleton for cavity sites",
          all_nb_in_shell and (c not in shell) and len(shell) == 26
          and far_minus_admissible
          and all(a == frozenset((1,)) for a in cav_pin))

    far = tuple(available_at(f_far, H) for H in ghist)
    check("T3 far site (no recorded neighbors) retains full availability {+1,-1} "
          "at every stage",
          all(a == FULL for a in far))

    # influence is possibility-level, NOT a force: the boundary and cavity sites
    # are never themselves recorded; availability is constrained, no record placed.
    check("T3 influence is possibility-level (not dynamical): the boundary site "
          "and the cavity site stay registrable (unrecorded) at every stage while "
          "their availability is constrained -- no record placed, no evolution",
          all(s_bd not in H for H in ghist) and all(c not in H for H in khist))

    # covariance of the rule under lattice translations and proper cubic rotations
    probes = [(2, 0, 0), (1, 1, 1), (0, 0, 0), (3, 3, 3), (5, 5, 5)]
    v = (3, -2, 4)
    Cv = {add(s, v): val for s, val in base.items()}
    trans_ok = all(available_at(add(p, v), Cv) == available_at(p, base) for p in probes)
    check("T3 availability rule is covariant under lattice translation "
          "(available_at(s+v; C+v) == available_at(s; C))",
          trans_ok)

    Cr = {rotate_z(s): val for s, val in base.items()}
    rot_ok = all(available_at(rotate_z(p), Cr) == available_at(p, base) for p in probes)
    check("T3 availability rule is covariant under a proper cubic rotation "
          "(available_at(Rs; RC) == available_at(s; C))",
          rot_ok)


# ===========================================================================
# T4 -- GLOBAL SATURATION UNREACHABLE AT FINITE STAGE (narrow, scoped)
#   Scope: realized histories with finite initial record support and finitely
#   many registrations per step.
# ===========================================================================
def window(k):
    rng = range(-k, k + 1)
    return block((rng, rng, rng))   # (2k+1)^3 cube centered at origin


def T4():
    # finite initial support + finite per-step batches => recorded set finite
    init = frozenset({(0, 0, 0)})
    batches = (
        frozenset({(1, 0, 0), (2, 0, 0)}),
        frozenset({(3, 0, 0), (4, 0, 0), (5, 0, 0)}),
        frozenset({(6, 0, 0)}),
        frozenset({(7, 0, 0), (8, 0, 0), (9, 0, 0), (10, 0, 0)}),
    )
    recorded = set(init)
    sizes = [len(recorded)]
    for b in batches:
        recorded |= b
        sizes.append(len(recorded))
    check("T4 finite initial support + finite per-step batches => recorded set "
          "size is a finite integer at every stage (sizes == [1,3,6,7,11])",
          all(isinstance(n, int) for n in sizes) and sizes == [1, 3, 6, 7, 11])

    # finite unions of finite sets are finite (integer-level counting law)
    fsets = [frozenset(range(3)), frozenset(range(2, 5)), frozenset({10, 11})]
    U = set()
    tot = 0
    for fs in fsets:
        U |= fs
        tot += len(fs)
    check("T4 finite union of finite sets is finite: |union| is an integer and "
          "<= sum of sizes (7 <= 8)",
          isinstance(len(U), int) and len(U) == 7 and len(U) <= tot)

    # Z^3 minus a finite recorded set stays infinite: unrecorded count in the
    # (2k+1)^3 window grows without bound while recorded set is fixed finite.
    uncounts = []
    for k in (1, 2, 3):
        W = window(k)
        rec_in = sum(1 for s in W if s in recorded)
        uncounts.append(len(W) - rec_in)
    check("T4 unrecorded-site count in (2k+1)^3 window strictly increases for "
          "k=1,2,3 (%s): infinitely many unrecorded sites remain" % (tuple(uncounts),),
          uncounts[0] < uncounts[1] < uncounts[2]
          and uncounts == [27 - 2, 125 - 3, 343 - 4])

    # explicit unrecorded witness at this finite stage => not globally saturated
    M = max(max(abs(c) for c in s) for s in recorded)
    witness = (M + 1, 0, 0)
    check("T4 explicit unrecorded site (M+1,0,0) outside the bounding window at "
          "a finite stage => global saturation NOT reached at any finite stage",
          witness not in recorded)

    # finite lattice
    Lat = block((range(2), range(2), range(2)))   # finite N-site lattice, N=8
    N = len(Lat)

    # PRIMARY (dom-based, reading-free): a saturating history has exactly N
    # first-registrations, and every attempted (N+1)-th registration on the
    # saturated lattice yields zero domain growth (a forced non-event). No M1.
    domhist = [dict()]
    accd = {}
    for site in sorted(Lat):
        accd[site] = 1
        domhist.append(dict(accd))
    domev = tuple(len(events(domhist[i - 1], domhist[i])) for i in range(1, len(domhist)))
    extend_growth = tuple(len(events(accd, {**accd, site: 1})) for site in sorted(Lat))
    check("T4 dom-based finite bound (reading-free): a saturating history on the "
          "N-site lattice has exactly N first-registrations (dom-events == (1,)*8, "
          "sum == N == 8); every attempted (N+1)-th registration yields zero "
          "domain growth -- at most N first-registrations, no M1 needed",
          domev == tuple([1] * N) and sum(domev) == N and N == 8
          and extend_growth == tuple([0] * N))

    # owner structural remark, checked: on a FINITE lattice one-record-per-stage
    # saturates within #sites stages; record-time then ends.
    Cfin = {}
    stages = 0
    for site in sorted(Lat):
        Cfin[site] = 1
        stages += 1
    check("T4 finite N-site lattice: a one-per-stage history saturates in "
          "exactly N stages, with zero registrable sites afterward",
          stages == N and all(s in Cfin for s in Lat)
          and len(registrable_sites(Lat, Cfin)) == 0)

    # STRONGER (model-relative, uses M1): distinct-record pigeonhole tail. Under
    # M1's site-functional (site,value) individuation the saturated lattice holds
    # exactly N distinct record elements and a same-value re-registration adds
    # none, so no (N+1)-th DISTINCT record exists. M1-load-bearing.
    elements = frozenset((s, Cfin[s]) for s in Cfin)
    after_reg = elements | frozenset((s, 1) for s in sorted(Lat))
    check("T4 M1 pigeonhole tail (model-relative, M1-load-bearing): the saturated "
          "N-site lattice carries exactly N distinct (site,value) records; "
          "re-registration adds no element (M1 same-element identity), so no "
          "(N+1)-th distinct record exists -- infinite Z^3 is load-bearing",
          len(elements) == N and after_reg == elements and len(after_reg) == N)


def main():
    quote_guards()
    T1()
    T2()
    T3()
    T4()
    finish()


if __name__ == "__main__":
    main()
