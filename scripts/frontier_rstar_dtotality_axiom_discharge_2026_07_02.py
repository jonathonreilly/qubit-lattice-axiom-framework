#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frontier runner: R* and D-totality discharge to landed axiom text (2026-07-02).

Bounded interpretive-premise discharge. This runner is exact-arithmetic
(Fraction/int/str only; NO floats) and stdlib-only. It exhibits, on small
finite witnesses, that two named interpretive premises used by review-pending
siblings are instances of already-landed axiom text:

  * R* (registrability reading, PR #4818 block03): clause 1 is the Record
    additivity sentence; clause 2 is an instance of
    "A readout value is determined by record content alone."
  * D-totality (PR #4820 block05): an instance of the law sentence
    "Its domain is a supplied condition, and at every state where the
    condition holds it gives exactly one answer."

It also models the two variants of block05's pointwise-escape T4 and the
motion-closure contrapositive restated from review-pending PR #4851.

This runner ADJUDICATES NOTHING. It sets no audit status, closes no wall, and
adds no axiom / policy / primitive / registry content. Blocks 03/05/16/17 and
PR #4851 are review-pending citations whose statuses belong to the independent
audit lane alone.

Check map (theorem -> checks), matching the note's [checks i-j] markers:
    Supplied surface (sentence guards)  : CHECK 01-06
    T1  R* -> Record text               : CHECK 07-09
    T2  D-totality -> law sentence       : CHECK 10-11
    T3(a) pointwise escape / motion      : CHECK 12-14
    T3(b) narrowed domain / supplier     : CHECK 15-16
    T4  ladder consequence (note greps)  : CHECK 17-21
    Metadata/dependency hygiene          : CHECK 22-24
"""

import os
import sys
from fractions import Fraction

# ---------------------------------------------------------------------------
# Harness
# ---------------------------------------------------------------------------
RESULTS = []  # list of (ok: bool, desc: str)


def check(ok, desc):
    RESULTS.append((bool(ok), desc))


def norm_ws(s):
    """Whitespace-normalize: collapse every whitespace run to one space, strip."""
    return " ".join(s.split())


def contains_norm(haystack, needle):
    """Whitespace-normalized substring containment (case-sensitive)."""
    return norm_ws(needle) in norm_ws(haystack)


REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
AXIOMS_PATH = os.path.join(REPO_ROOT, "docs", "MINIMAL_AXIOMS_2026-06-29.md")
NOTE_PATH = os.path.join(
    REPO_ROOT, "docs", "RSTAR_DTOTALITY_DISCHARGE_TO_AXIOM_TEXT_BOUNDED_NOTE_2026-07-02.md"
)


def read_text(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return fh.read()
    except OSError:
        return ""


AX = read_text(AXIOMS_PATH)
NOTE = read_text(NOTE_PATH)

# ===========================================================================
# Supplied surface: sentence guards on the landed axiom memo  [checks 1-6]
# ===========================================================================
NEEDLE_ADDITIVITY = (
    "For any finite collection of pairwise-disjoint records, scalar readout "
    "`I` is additive, with `I(empty)=0`."
)
NEEDLE_CONTENT_DET = "A readout value is determined by record content alone."
NEEDLE_LAW = (
    "A law privileges no states. Its domain is a supplied condition, and at "
    "every state where the condition holds it gives exactly one answer."
)
NEEDLE_LATTICE_DISTINCT = (
    "No site is privileged. Sites are distinguished by the supplied lattice "
    "structure alone."
)
NEEDLE_QUBIT_DISTINCT = (
    "No possibility is privileged. Possibilities are distinguished by the "
    "supplied algebraic structure alone."
)
NEEDLE_ABOUT_EACH_SITE = "about each site"

check(
    contains_norm(AX, NEEDLE_ADDITIVITY),
    "axiom memo carries the Record additivity sentence (R* clause 1 verbatim)",
)
check(
    contains_norm(AX, NEEDLE_CONTENT_DET),
    "axiom memo carries 'A readout value is determined by record content alone.'",
)
check(
    contains_norm(AX, NEEDLE_LAW),
    "axiom memo carries the full law sentence (domain + exactly-one-answer)",
)
check(
    contains_norm(AX, NEEDLE_LATTICE_DISTINCT),
    "axiom memo carries the Lattice distinction clause",
)
check(
    contains_norm(AX, NEEDLE_QUBIT_DISTINCT),
    "axiom memo carries the Qubit distinction clause",
)
check(
    contains_norm(AX, NEEDLE_ABOUT_EACH_SITE),
    "axiom memo carries 'about each site' (proper cubic rotations; motion group)",
)

# ===========================================================================
# T1: R* clause 2 is an instance of content-determination            [checks 7-9]
# ---------------------------------------------------------------------------
# Record content is a canonical, basis-free object (a site->possibility map keyed
# by intrinsic supplied site ids). An imported basis is an unsupplied auxiliary
# choice; its ORBIT is the choice set = a set of relabelings. A readout that
# varies over that orbit at FIXED record content is not determined by record
# content alone -> excluded by the content-determination sentence directly.
# ===========================================================================
CONTENT = (("s0", "up"), ("s1", "down"))  # fixed record content (canonical, basis-free)

# The imported-basis orbit: a set of labelings (index assignments to the records).
LABELINGS = [(0, 1), (1, 0)]  # orbit of the unsupplied auxiliary choice = choice set


def readout_basis_dependent(content, labeling):
    """Reads 'the possibility the imported basis lists first' -> basis-dependent."""
    placed = {labeling[i]: content[i][1] for i in range(len(content))}
    return placed[0]


def readout_content_only(content, labeling):
    """Additive record count: a function of record content alone (orbit-constant)."""
    return len(content)


def is_content_determined(readout, content, orbit):
    """Detector: determined by record content alone iff constant on the orbit of
    the unsupplied auxiliary choice."""
    values = {readout(content, L) for L in orbit}
    return len(values) == 1


check(
    not is_content_determined(readout_basis_dependent, CONTENT, LABELINGS),
    "T1: basis-dependent readout (varies at fixed content) flagged NOT content-determined",
)
check(
    is_content_determined(readout_content_only, CONTENT, LABELINGS),
    "T1: orbit-constant (record-content-only) readout passes content-determination",
)
check(
    len(set(LABELINGS)) >= 2
    and len({readout_basis_dependent(CONTENT, L) for L in LABELINGS}) >= 2,
    "T1: imported-basis orbit is a set of >=2 labelings inducing >=2 values (unsupplied choice, not record content)",
)

# ===========================================================================
# T2: D-totality is an instance of the law sentence                 [checks 10-11]
# ---------------------------------------------------------------------------
# A law-domain is the set of states satisfying a supplied condition. A rule
# undefined at a state where its supplied condition holds fails to give exactly
# one answer there -> it is not a law. Rule-domain totality is thus axiom text.
# ===========================================================================
DOMAIN_STATES = [0, 1, 2, 3]  # states where the supplied condition holds


def is_total_law(rule_dict, domain):
    """Exactly-one-answer at every state where the condition holds."""
    for s in domain:
        if s not in rule_dict:
            return False  # undefined in-domain -> not exactly one answer -> not a law
    return True


RULE_PARTIAL = {0: "a", 1: "b", 2: "c"}  # undefined at in-domain state 3
RULE_TOTAL = {0: "a", 1: "b", 2: "c", 3: "d"}

check(
    not is_total_law(RULE_PARTIAL, DOMAIN_STATES),
    "T2: partial rule (undefined at an in-domain state) fails exactly-one-answer totality",
)
check(
    is_total_law(RULE_TOTAL, DOMAIN_STATES),
    "T2: total rule passes exactly-one-answer totality on its supplied domain",
)

# ===========================================================================
# T3(a): pointwise escape closes via motion-closure                 [checks 12-14]
# ---------------------------------------------------------------------------
# Miniature of the retirement runner (PR #4851): a 2x2x2 wraparound lattice.
# Sites are tuples; translations act by site permutation (mod-2). Records are
# site->possibility maps transported by the group. The contrapositive: a
# condition whose extension is not motion-closed draws, in extension, a
# distinction among motion-related structure-isomorphic states carried by
# neither record content nor supplied structure -- barred by the two distinction
# clauses. A generic one-record singleton domain is not motion-closed; the
# empty-configuration singleton IS (the honest exception). Pointwise EVALUATION
# of a motion-closed rule at the realized state is distinct from a singleton
# domain: evaluation is not a domain.
# ===========================================================================
TRANSLATIONS = [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]  # (Z/2)^3


def translate_site(site, t):
    return tuple((site[i] + t[i]) % 2 for i in range(3))


def translate_config(config, t):
    """Transport a record configuration (frozenset of (site, possibility))."""
    return frozenset((translate_site(site, t), poss) for (site, poss) in config)


def motion_closed(domain):
    """domain: set of configs. Closed iff every translate of every member stays in."""
    for config in domain:
        for t in TRANSLATIONS:
            if translate_config(config, t) not in domain:
                return False
    return True


def orbit(config):
    return frozenset(translate_config(config, t) for t in TRANSLATIONS)


EMPTY = frozenset()  # the empty configuration (motion-invariant)
S0 = frozenset({((0, 0, 0), "a")})  # a generic (non-motion-invariant) one-record state

check(
    not motion_closed(frozenset({S0})),
    "T3(a): singleton domain at a generic one-record state is NOT motion-closed",
)
check(
    motion_closed(frozenset({EMPTY})),
    "T3(a): empty-configuration singleton IS motion-closed (the honest exception)",
)

UNIFORM_CONFIG = frozenset(((s, "p") for s in [(a, b, c) for a in (0, 1) for b in (0, 1) for c in (0, 1)]))
UNIFORM_RULE = {UNIFORM_CONFIG: "ctx"}
check(
    motion_closed({UNIFORM_CONFIG})
    and not all(state in UNIFORM_RULE for state in [UNIFORM_CONFIG, frozenset()]),
    "T3(a): uniform-configuration singleton is motion-closed (lawful narrow domain) yet no full-surface supplier",
)

ORBIT_S0 = orbit(S0)  # the motion-closed law domain (all 8 one-record 'a' states)


def rule_R(config):
    """A motion-closed rule: record count. Single-valued at every state."""
    return len(config)


eval_distinct_from_domain = (
    motion_closed(ORBIT_S0)  # the lawful domain is motion-closed
    and (S0 in ORBIT_S0)  # the realized state is a member (an evaluation point)
    and (rule_R(S0) == 1)  # pointwise evaluation yields exactly one value
    and (not motion_closed(frozenset({S0})))  # yet the singleton {s0} is not a lawful domain
)
check(
    eval_distinct_from_domain,
    "T3(a): pointwise evaluation of a motion-closed rule at s0 is distinct from a singleton domain (evaluation is not a domain)",
)

# ===========================================================================
# T3(b): narrowed 'Y nondegenerate' domain vs full-surface supplier [checks 15-16]
# ---------------------------------------------------------------------------
# The law-admissible surface: delta = k*pi/6, k = 0..11, stored EXACTLY as
# Fraction multiples of pi (no floats). Degeneracy loci: delta = m*pi/3, i.e.
# k even. The S3-class fine-partition rule is total on the nondegenerate
# (record-content) narrowed domain, but is silent at the loci -- so it cannot
# serve as a context supplier for the FULL law-admissible surface.
# ===========================================================================
SURFACE = [Fraction(k, 6) for k in range(12)]  # angle in units of pi (exact)


def is_degenerate(angle_over_pi):
    """delta is an integer multiple of pi/3 iff angle*3 is an integer."""
    return (angle_over_pi * 3).denominator == 1


NONDEGEN = [a for a in SURFACE if not is_degenerate(a)]  # narrowed domain (Y nondegenerate)


def s3_rule(angle_over_pi):
    """S3-class fine partition: a single verdict where recoverable, else silent."""
    if is_degenerate(angle_over_pi):
        return None
    return "fine-partition"


def total_on(rule, domain):
    return all(rule(a) is not None for a in domain)


def is_full_surface_supplier(rule, surface):
    return all(rule(a) is not None for a in surface)


check(
    total_on(s3_rule, NONDEGEN) and len(NONDEGEN) == 6,
    "T3(b): S3-class rule is total on the narrowed 'Y nondegenerate' domain",
)
check(
    (not is_full_surface_supplier(s3_rule, SURFACE))
    and any(s3_rule(a) is None for a in SURFACE),
    "T3(b): S3-class rule fails full-surface supplier -- a law-admissible locus gets no context verdict",
)

# ===========================================================================
# T4: ladder consequence -- boundary greps on the note              [checks 17-20]
# ---------------------------------------------------------------------------
# Flag, do not close. The note must firewall its own scope.
# ===========================================================================
check(contains_norm(NOTE, "adjudicates nothing"), "note asserts it adjudicates nothing")
check(contains_norm(NOTE, "no wall is closed"), "note asserts no wall is closed")
check(contains_norm(NOTE, "review-pending"), "note flags siblings as review-pending citations")
check(
    contains_norm(NOTE, "evaluation is not a domain"),
    "note states 'evaluation is not a domain'",
)
check(
    "**Type:** bounded_theorem" in NOTE and "**Claim type:** bounded_theorem" in NOTE,
    "metadata: note declares canonical bounded_theorem type fields",
)
check(
    "**Audit boundary:** independent audit lane only" in NOTE
    and "**Status authority:**" not in NOTE
    and "**Actual current surface status:**" not in NOTE,
    "metadata: note uses audit boundary, not legacy status-authority/status-surface wording",
)
check(
    "(MINIMAL_AXIOMS_2026-06-29.md)" in NOTE
    and "(REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11.md)" in NOTE
    and "Review-pending sibling details are listed as PR numbers only and are not dependency links." in NOTE,
    "dependency hygiene: landed premise surfaces are linked and review-pending siblings are not dependency links",
)

# ---------------------------------------------------------------------------
# Report
# ---------------------------------------------------------------------------
def main():
    fails = 0
    for i, (ok, desc) in enumerate(RESULTS, 1):
        status = "PASS" if ok else "FAIL"
        if not ok:
            fails += 1
        print(f"CHECK {i:02d}: {status} — {desc}")
    passes = len(RESULTS) - fails
    print(f"TOTAL: PASS={passes} FAIL={fails}")
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
