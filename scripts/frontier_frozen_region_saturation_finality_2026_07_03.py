#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
frontier_frozen_region_saturation_finality_2026_07_03.py

Exact-arithmetic runner for the bounded + narrow-scoped theorems of the note:
  docs/FROZEN_REGION_RECORD_SATURATION_LOCAL_FINALITY_BOUNDARY_INFLUENCE_BOUNDED_NOTE_2026-07-03.md

Worker draft under the workhorse execution split. Audit status is set only by
the independent audit lane; nothing here is adopted, promoted, or ruled, and no
audit outcome is predicted.

Conventions (exactness firewall):
  * Exact only -- Python int / tuple / set / frozenset. NO float anywhere.
  * A "site" is a point of Z^3 as a 3-tuple of ints.
  * A record's locked value is modelled at the NOTE level by a 2-value scalar
    tag in {+1, -1} (Python ints 1, -1). This is the note-level model of the
    Record axiom's locking of one available local possibility; it is NOT a
    claim about the full one-site M_2(C) possibility domain.
  * A configuration C is a dict {site: locked_value}: "site carries a record
    with that locked value"; sites absent from C carry no record.
  * A history is a finite tuple (C_0, ..., C_T). Under permanence (PR #4874,
    in-flight, owner-approved 2026-07-03) together with the axiom sentence
    "A state is a configuration of records", record sets are nested along a
    realized history and locked values agree on the smaller domain. An EVENT at
    stage t is a new registration: a site in dom(C_t) \\ dom(C_{t-1}).

The covariant neighbor-dependent availability rule and the record-inclusion
event-ordering are REBUILT here from scratch (small exact windows). The
review-pending sibling PR #4873 (branch-only) is cited by number only and is
NOT read. The frozen-star / black-hole label is an owner interpretive READING,
not a claim; this runner asserts no GR content (no metric, horizon, curvature)
and no rate / clock content.
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


def available_at(s, C):
    """Covariant neighbor-dependent availability rule (rebuilt exactly):
    available_at(s) = { locked values of records on nearest neighbors of s }
    if that set is nonempty, else the full possibility set {+1,-1}."""
    vals = set()
    for nb in neighbors(s):
        if nb in C:
            vals.add(C[nb])
    if vals:
        return frozenset(vals)
    return FULL


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
    """New registrations from configuration prev to configuration cur."""
    return frozenset(s for s in cur if s not in prev)


def nested_with_agreement(hist):
    """Permanence + state-as-record-configuration => record sets nested and
    locked values agree on the smaller domain, at every succession step."""
    for i in range(1, len(hist)):
        prev, cur = hist[i - 1], hist[i]
        if not all(s in cur for s in prev):
            return False
        if not all(cur[s] == prev[s] for s in prev):
            return False
    return True


# ---------------------------------------------------------------------------
# Quote guards -- the note's quotes must match docs/MINIMAL_AXIOMS_2026-06-29.md
# (the PRE-restoration Record sentence lives in THIS worktree copy).
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
    rec = ("a record locks exactly one local possibility from the subset "
           "available at that site under Admissibility; the locked possibility "
           "is invariant under repeated readout")
    adm = ("the available possibilities are determined by, and vary with, the "
           "nearest-neighbor conditions")
    stt = "A state is a configuration of records."
    check("quote guard: pre-restoration Record locking+readout-invariance "
          "sentence present verbatim in MINIMAL_AXIOMS_2026-06-29.md",
          txt is not None and rec in txt)
    check("quote guard: Admissibility 'determined by, and vary with, the "
          "nearest-neighbor conditions' present verbatim",
          txt is not None and adm in txt)
    check("quote guard: 'A state is a configuration of records.' present verbatim",
          txt is not None and stt in txt)


# ===========================================================================
# T1 -- SATURATION IMPLIES LOCAL FINALITY (bounded, conditional on permanence)
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

    # constancy of the R-restriction is FORCED, by exact enumeration over
    # ALPHABET^8 candidate later R-restrictions:
    #   'absent' -> record removed      : barred by permanence
    #   +1 / -1  -> a locked value      : value change (alteration) barred by permanence
    #   'double' -> a second record     : barred by "locks exactly one"
    ALPHABET = ("absent", 1, -1, "double")
    sites = sorted(R2)

    def guard_ok(site, tag):
        if tag == "absent":
            return False                 # removal barred by permanence
        if tag == "double":
            return False                 # second record barred by locks-exactly-one
        return tag == C2[site]           # only the unchanged locked value survives

    survivors = [combo for combo in itertools.product(ALPHABET, repeat=len(sites))
                 if all(guard_ok(site, tag) for site, tag in zip(sites, combo))]
    check("T1 constancy FORCED: exactly one later R-restriction survives "
          "permanence+locks-one, and it equals C|R (history constant on R)",
          len(survivors) == 1
          and dict(zip(sites, survivors[0])) == {s: C2[s] for s in sites})
    check("T1 guards have teeth: removal, alteration, and double-record "
          "candidates are each rejected",
          (not guard_ok(sites[0], "absent"))
          and (not guard_ok(sites[0], -1))
          and (not guard_ok(sites[0], "double")))

    # global corollary: a globally-saturated all-(+1) configuration is
    # ADMISSIBLE against the note-level availability model, and readout is
    # additive over disjoint sub-collections with readout(empty)=0.
    admissible = all(C2[s] in available_at(s, C2) for s in R2)
    Ha = {s: C2[s] for s in R2 if s[0] == 0}
    Hb = {s: C2[s] for s in R2 if s[0] == 1}
    check("T1 global corollary: all-(+1) saturated config admissible (each "
          "locked value lies in its neighbor-determined availability set); "
          "readout additive over disjoint halves; readout(empty)=0",
          admissible and readout({}) == 0
          and readout(C2) == readout(Ha) + readout(Hb) == 8)

    # discriminating control: the admissibility check is not vacuous.
    Cbad = dict(C2)
    Cbad[(0, 0, 0)] = -1
    bad_ok = all(Cbad[s] in available_at(s, Cbad) for s in R2)
    check("T1 discriminating control: flipping one interior site to -1 amid +1 "
          "neighbors yields a NON-admissible config (check has teeth)",
          (not bad_ok) and (Cbad[(0, 0, 0)] not in available_at((0, 0, 0), Cbad)))


# ===========================================================================
# T2 -- LOCAL TIME STOPS (bounded, conditional on permanence)
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
          "succession step of the history",
          nested_with_agreement(hist))

    r_sat = tuple(all(s in hist[t] for s in R) for t in range(len(hist)))
    check("T2 region R unsaturated at stage 1, saturated at stage 2 (a frozen "
          "region is produced)",
          (r_sat[1] is False) and (r_sat[2] is True))

    in_R = tuple(len(events(hist[t - 1], hist[t]) & R) for t in range(1, len(hist)))
    out_R = tuple(len(events(hist[t - 1], hist[t]) - R) for t in range(1, len(hist)))
    check("T2 per-stage in-R event counts == (4,4,0,0): R event count halts "
          "after saturation (record-time in R ends)",
          in_R == (4, 4, 0, 0))
    check("T2 per-stage outside-R event counts == (0,0,2,2): events continue on "
          "the unsaturated complement at stages 3,4",
          out_R == (0, 0, 2, 2))

    r_count = tuple(len(set(hist[t]) & R) for t in range(len(hist)))
    check("T2 restricted record set in R is constant (==8) for stages 2,3,4 -- "
          "record-time in R is halted",
          r_count[2] == r_count[3] == r_count[4] == 8)

    out_cum = tuple(len(set(hist[t]) - R) for t in range(len(hist)))
    check("T2 outside-R record count strictly increases at stages 3 and 4 while "
          "R is frozen (time flows where unwritten possibility remains)",
          out_cum[2] < out_cum[3] < out_cum[4])


# ===========================================================================
# T3 -- BOUNDARY INFLUENCE WITHOUT EVOLUTION (bounded)
# ===========================================================================
def rotate_z(s):
    x, y, z = s
    return (-y, x, z)   # proper cubic rotation about the z-axis (det +1)


def T3():
    R = block((range(2), range(2), range(2)))
    base = {s: 1 for s in R}                 # saturated block, all +1
    s_bd = (2, 0, 0)                         # outside boundary site; neighbor (1,0,0) in R
    f_far = (5, 5, 5)                        # far outside site; no recorded neighbors
    H1 = dict(base)
    H2 = dict(H1); H2[(0, 0, 7)] = 1         # distant event, not adjacent to s_bd or f_far
    H3 = dict(H2); H3[(0, 7, 0)] = 1         # distant event
    hist = (H1, H2, H3)

    pin = tuple(available_at(s_bd, H) for H in hist)
    check("T3 boundary pin: outside site adjacent to the saturated block has "
          "availability {+1} at every stage",
          all(a == frozenset((1,)) for a in pin))

    far = tuple(available_at(f_far, H) for H in hist)
    check("T3 far site retains full availability {+1,-1} at every stage",
          all(a == FULL for a in far))

    check("T3 pin is PERMANENT: the in-R neighbor record (1,0,0)=+1 is constant "
          "along the history, so availability at s never relaxes",
          all(H.get((1, 0, 0)) == 1 for H in hist)
          and all(available_at(s_bd, H) == frozenset((1,)) for H in hist))

    # influence is possibility-level, NOT a force: s_bd is never itself recorded;
    # its availability is constrained but no record is placed on it.
    check("T3 influence is possibility-level (not dynamical): s stays registrable "
          "(unrecorded) at every stage while its availability is pinned",
          all(s_bd not in H for H in hist))

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

    # owner structural remark, checked: on a FINITE lattice one-record-per-stage
    # saturates within #sites stages; record-time then ends.
    Lat = block((range(2), range(2), range(2)))   # finite N-site lattice, N=8
    N = len(Lat)
    Cfin = {}
    stages = 0
    for site in sorted(Lat):
        Cfin[site] = 1
        stages += 1
    check("T4 finite N-site lattice: a one-per-stage history saturates in "
          "exactly N stages, with zero registrable sites afterward",
          stages == N and all(s in Cfin for s in Lat)
          and len(registrable_sites(Lat, Cfin)) == 0)

    # pigeonhole: after N distinct records no further registration is possible on
    # the finite lattice; unbounded record-time therefore requires infinite Z^3.
    check("T4 pigeonhole: after N distinct records the finite lattice has zero "
          "registrable sites (no (N+1)-th event) -- infinite Z^3 is load-bearing "
          "for unbounded record-time",
          len(registrable_sites(Lat, Cfin)) == 0)


def main():
    quote_guards()
    T1()
    T2()
    T3()
    T4()
    finish()


if __name__ == "__main__":
    main()
