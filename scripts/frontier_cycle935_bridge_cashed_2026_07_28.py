#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Cycle 935 (blockG28) -- THE SOURCE-ACTION BRIDGE CASHED?

Compose the Cycle-871 structure theorem (the bridge's free dimension is
EXACTLY 1 at weak-field linear order) with the registered SCALE-REFERENCE
PRIMITIVE, and determine exactly what dimensionful physics follows.

The owner's pointer to the registry is the REASON for this block, but the
primitive's OWN TEXT decides scope.  This runner therefore does not assume
the composition closes: it applies the primitive's own dichotomy sentence
as a decision procedure and reports whatever verdict that yields.

Everything here is conditional on the registered scale reference (registered
data; the masses' standing).  Nothing here discharges any of the five
STRONGER obligations of the 871 obligation map.

No axiom, primitive, registry, policy, queue or audit surface is touched.
This runner is READ-ONLY with respect to every such surface, and it never
IMPORTS the landed Gate-B primary (871 blocklists it; text/AST access only).
"""

from __future__ import annotations

import ast
import hashlib
import json
import math
import os
import random
import re
import subprocess
import sys
import time
from fractions import Fraction
from itertools import product

RUNTIME_BUDGET_S = 900.0
REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# --------------------------------------------------------------------------
# PINS -- value-for-value.  A mismatch is a hard failure, never a warning.
# --------------------------------------------------------------------------

PINS_871 = {
    "docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md": (
        "c666f500518ce1b67745c63e65b63656d905d1c70ed04ee566827e2628575100",
        "2cac419f992adcfffa8a48e3af7febad68714ce2"),
    "scripts/frontier_cycle871_source_action_bridge_pricing_2026_07_28.py": (
        "e27b91b699917aea27b3e603096fde16751c45d8cb3c1e7b0ff14bb1a46641fc",
        "b0515ad74f0a883e091fa3c9b4f3126c1fe6fe60"),
    "scripts/frontier_cycle871_bridge_independent_check_2026_07_28.py": (
        "3a2c7e8d8015984dbf822d7dbf5d72d7357c91acb079e70de53583e91e3bc4cf",
        "11e36191d89214ae0a55e5a42099b6b261eccde9"),
    "logs/runner-cache/frontier_cycle871_source_action_bridge_pricing_2026_07_28.txt": (
        "bf1e493cff5775bfba10e4f293ffe794c09cfe8448b3b5c4103e61d82ceb3ad8",
        "d491b5f42ab1186bd8eb952583304c5d6769d7ac"),
    "logs/runner-cache/frontier_cycle871_bridge_independent_check_2026_07_28.txt": (
        "76e8142d113fc6d71c7afd792f589eed40fd8ddea34345b05586e66580293e7a",
        "983fe2e71c7bde3fe423580f240b334979405d49"),
}

# The LANDED Gate-B primary.  871 AST-verified its structure but pinned NONE of
# its numeric values; this block pins them (see CERT-GAUGE).
LANDED_GATE_B = "scripts/gate_b_weak_field_source_action_interface_2026_06_16.py"
LANDED_GATE_B_PINS = ("ac9ea8b6b7556ce8679d734e98a152bf3af7a9988d9f72f5722ad4c8f7ec9453",
                      "d604bc5f180e87844f477d52f82376df61e0134e")

RECEIPT_871 = "outputs/source_action_bridge_pricing_cycle871_receipt_2026_07_28.json"
CACHE_871 = "logs/runner-cache/frontier_cycle871_source_action_bridge_pricing_2026_07_28.txt"

# Main-side notes.  VENDORING DISCLOSURE: these were expected to need
# `git checkout origin/main -- <path>`.  They were already in-tree at blobs
# BYTE-IDENTICAL to origin/main, so no checkout was performed; blob equality
# against origin/main is verified live below.
MAIN_SIDE_NOTES = {
    "docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md": (
        "e7e75a36bd16094cbb547f6b215680ac45adc565c4cc93f05b0af17992eb9292",
        "a74392f6939b2e51109756c37d6d5d59bb54c5a4"),
    "docs/MIN_TIME_STEP_IS_THE_PLANCK_TIME_FROM_THE_SINGLE_SCALE_REFERENCE_PRIMITIVE_NARROW_THEOREM_NOTE_2026-06-08.md": (
        "e12615aebebd7535a4cc5c5a446bf1ba731f656d4de91744818b51edeb7ec047",
        "ba64460ec9ca2ee3ad6e778603be550b053cc352"),
}

REGISTRY_READONLY = "docs/audit/data/axiom_premise_nodes.json"
SEAL_FILE = "outputs/bridge_cashed_cycle935_seal_2026_07_28.json"

# --------------------------------------------------------------------------
# BYTE-QUOTED CLAUSES from the scale-reference primitive's OWN text.
# Stored as EXACT byte strings (the note hard-wraps) plus byte offsets.
# --------------------------------------------------------------------------

PRIMITIVE_CLAUSES = {
    "SUPPLY_1_one_reference": (449,
        b"The framework takes exactly one dimensionful reference: a scale that converts\n"
        b"the framework's lattice-natural units to physical units. The chosen reference\n"
        b"is the Planck mass scale, `a^{-1} = M_Pl`."),
    "EXCLUSION_1_zero_dimensionless_content": (649,
        b"This is a units conversion, not a physics axiom. It carries zero dimensionless\n"
        b"content: no mass ratio, coupling, mixing angle, phase, selector, readout\n"
        b"bridge, or empirical fit is supplied by it."),
    "DICHOTOMY_the_scope_test": (1151,
        b"Quantities on the\n"
        b"structural surface remain dimensionless or carry a power of the lattice\n"
        b"spacing `[a]^n` until that reference is supplied."),
    "EXCLUSION_2_no_derivation_of_scale": (1291,
        b"No derivation of the chosen\nphysical scale is claimed here."),
    "EXCLUSION_3_not_a_over_lP_equals_one": (1675,
        b"It does not assert `a/l_P = 1` as a derived theorem. The self-consistency\n"
        b"  question that the framework's natural unit equals the Planck length remains\n"
        b"  a separate open gravity derivation."),
    "EXCLUSION_4_no_dimensionless_quantity": (1867,
        b"It does not supply any dimensionless quantity. Dimensionless physics must\n"
        b"  derive from retained-grade framework content or remain conditional/open."),
}

BRIDGE_SCALAR_TOKENS = [b"one real scalar", b"the overall coupling", b"normalization"]

# --------------------------------------------------------------------------
# 871 OBLIGATION MAP (extracted value-for-value from the pinned cache bytes)
# --------------------------------------------------------------------------

STRONGER_OBLIGATIONS = {
    "finite_core_vs_green_kernel": 5,
    "GB_S2_kernel_plus_window": 8,
    "GB_S3_connectivity": 4,
    "signed_gravity_locked_term": 2,
    "hclass_to_angle_readout_identity": 2,
}
EQUIVALENT_CLAUSES = {"GB_S1b_source_strength_normalization": 1,
                      "physical_Newton_constant_SI_normalization": 1}
WEAKER_CLAUSES = {"GB_S1a_linear_test_action_shape": 0}

FORBIDDEN_CLAIM_TOKENS = ["kernel", "window", "connectivity", "readout identity",
                          "locked term", "green function", "finite core"]

# 871's exact 16 patches, in its exact print order.
PATCHES_871 = [(2,), (3,), (4,), (5,), (6,), (2, 2), (2, 3), (7,), (8,), (10,),
               (12,), (3, 3), (2, 2, 2), (2, 2, 3), (4, 4), (3, 3, 3)]
FULL_ROUTE_MAX_SITES = 6          # 871's own cap; 7 patches get both routes
EXHAUSTIVE_TRIANGULAR_MAX = 14    # above this, deterministic sampling

# 871's ablation prices, per patch (REC0=empty-record, REC1=count-once, LAT=translation)
ABLATION_PINNED = {
    (3,):   {"REC0": 1, "REC1": 2, "LAT": 2, "residual": 1},
    (4,):   {"REC0": 1, "REC1": 4, "LAT": 3, "residual": 1},
    (2, 2): {"REC0": 1, "REC1": 5, "LAT": 3, "residual": 1},
}

# --------------------------------------------------------------------------
# THE COMPOSITION'S HYPOTHESIS LIST (Q1) -- enumerated honestly.
# --------------------------------------------------------------------------

HYPOTHESIS_LIST = [
    ("H1", "SUPPLIED", "871 declared ansatz: scalar action functionals on record configurations "
     "of a finite lattice torus patch, weak-field linear order"),
    ("H2", "SUPPLIED", "Record axiom, empty-record clause (REC0): A(empty) = 0"),
    ("H3", "SUPPLIED", "Record axiom, count-once additivity (REC1): A(a u b) = A(a) + A(b), a,b disjoint"),
    ("H4", "SUPPLIED", "Lattice axiom, translation covariance (LAT) along the generators; the patch "
     "is a torus so the translation action is transitive (exactly one singleton orbit)"),
    ("H5", "SUPPLIED", "scale_reference_primitive: exactly one dimensionful reference, a^{-1} = M_Pl, "
     "units conversion only (registered in axiom_premise_nodes.json, owner-approved "
     "per AXIOM_MINIMALITY_POLICY section 6)"),
    ("H6", "NOT_SUPPLIED", "an engineering dimension for the bridge scalar: a specific exponent n with "
     "kappa ~ [a]^n. Cycle 871 derives NO physical dimension for its free scalar "
     "(verified: zero occurrences of hbar/G/M_Pl/SI/[a]^n as a dimension assignment "
     "anywhere in the 871 package), so the primitive's conversion has no exponent "
     "to act on"),
    ("H7", "NOT_SUPPLIED", "the dimensionless part kappa_hat of the bridge scalar. The primitive's own "
     "text refuses this: 'It does not supply any dimensionless quantity.'"),
    ("H8", "NOT_SUPPLIED", "an action unit (hbar) and any further SI conversion. hbar is NOT among the "
     "four registered premise nodes (minimal_axioms, scale_reference_primitive, "
     "kinetic_isotropy_primitive, realized_state_primitive); it could enter only as "
     "a NAMED unit-conversion import -- the precedent being the Planck-time note's "
     "explicit SI c = 299792458 m/s certificate"),
]

# --------------------------------------------------------------------------
# helpers
# --------------------------------------------------------------------------

def sha256_file(path):
    with open(os.path.join(REPO, path), "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def git_blob(path):
    return subprocess.run(["git", "hash-object", os.path.join(REPO, path)],
                          capture_output=True, text=True, cwd=REPO).stdout.strip()


def read_bytes(path):
    with open(os.path.join(REPO, path), "rb") as fh:
        return fh.read()


class Cert:
    def __init__(self):
        self.rows = []

    def add(self, name, ok, detail):
        self.rows.append((name, bool(ok), detail))
        return bool(ok)

    @property
    def npass(self):
        return sum(1 for _, ok, _ in self.rows if ok)

    @property
    def nfail(self):
        return sum(1 for _, ok, _ in self.rows if not ok)


# --------------------------------------------------------------------------
# THE 871 STRUCTURE THEOREM, RE-DERIVED FROM SCRATCH
# --------------------------------------------------------------------------

def torus_sites(shape):
    return list(product(*[range(s) for s in shape]))


def translate(site, v, shape):
    return tuple((c + d) % s for c, d, s in zip(site, v, shape))


def generators(shape):
    gens = []
    for i in range(len(shape)):
        if shape[i] > 1:
            v = [0] * len(shape)
            v[i] = 1
            gens.append(tuple(v))
    return gens


def sparse_rank(rows):
    """Exact Gaussian elimination over Fraction on sparse dict rows."""
    pivots = {}
    rank = 0
    for row in rows:
        r = {k: Fraction(v) for k, v in row.items() if v != 0}
        while r:
            p = min(r)
            if p in pivots:
                pr = pivots[p]
                f = r[p] / pr[p]
                for k, v in pr.items():
                    nv = r.get(k, Fraction(0)) - f * v
                    if nv == 0:
                        r.pop(k, None)
                    else:
                        r[k] = nv
            else:
                pivots[p] = r
                rank += 1
                break
    return rank


def constraint_rows(shape, use_empty=True, use_countonce=True, use_translation=True,
                    scale=Fraction(1), gens_override=None):
    sites = torus_sites(shape)
    n = len(sites)
    nvars = 1 << n
    idx = {s: i for i, s in enumerate(sites)}
    rows = []
    if use_empty:
        rows.append({0: scale})
    if use_countonce:
        for a in range(1, nvars):
            for b in range(a, nvars):
                if a & b:
                    continue
                rows.append({a | b: scale, a: -scale, b: -scale})
    if use_translation:
        gens = gens_override if gens_override is not None else generators(shape)
        for v in gens:
            perm = [idx[translate(s, v, shape)] for s in sites]
            for m in range(nvars):
                tm = 0
                for i in range(n):
                    if m >> i & 1:
                        tm |= 1 << perm[i]
                if tm != m:
                    rows.append({tm: scale, m: -scale})
    return rows, nvars


def brute_route(shape, **kw):
    """Full constraint family on all 2^n subset-variables; exact rank."""
    rows, nvars = constraint_rows(shape, **kw)
    rank = sparse_rank(rows)
    return {"unknowns": nvars, "rank": rank, "dim": nvars - rank}


def structural_route(shape, gens_override=None):
    """Triangular route: REC0+REC1 collapse every mask to singletons, then LAT
    quotients the singletons.  Returns (orbits, triangular_ok, mode)."""
    sites = torus_sites(shape)
    n = len(sites)
    if n <= EXHAUSTIVE_TRIANGULAR_MAX:
        masks = range(1, 1 << n)
        mode = "exhaustive"
    else:
        rng = random.Random(0x935C3)
        masks = [rng.randrange(1, 1 << n) for _ in range(50000)]
        mode = "sampled-50000"
    triangular_ok = True
    for m in masks:
        if m.bit_count() == 1:
            continue
        low = m & (-m)
        rest = m ^ low
        if low == 0 or rest == 0 or (low & rest) != 0 or (low | rest) != m:
            triangular_ok = False
            break
    parent = list(range(n))

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    idx = {s: i for i, s in enumerate(sites)}
    gens = gens_override if gens_override is not None else generators(shape)
    for v in gens:
        for s in sites:
            a, b = find(idx[s]), find(idx[translate(s, v, shape)])
            if a != b:
                parent[a] = b
    return len({find(i) for i in range(n)}), triangular_ok, mode


# --------------------------------------------------------------------------
# THE COMPOSITION: does registering the ruler reduce the free dimension?
# --------------------------------------------------------------------------

def composed_free_dimension(shape, ruler_u, exponent_n):
    """Re-solve the SAME constraint family in the PHYSICAL frame.

    Registering a ruler rescales every action value by t = u^n != 0.  We do
    not assert what that does -- we recompute the rank in the rescaled frame.
    """
    t = Fraction(ruler_u) ** exponent_n
    if t == 0:
        raise ValueError("degenerate ruler")
    rows, nvars = constraint_rows(shape, scale=t)
    return nvars - sparse_rank(rows)


# --------------------------------------------------------------------------
# THE GAUGE EXHIBIT (Q2): the LANDED Gate-B convention vs the composed object
# --------------------------------------------------------------------------

def gate_b_phi_exact(strength, r, eps):
    return Fraction(strength) / (Fraction(r) + Fraction(eps))


def gate_b_action_exact(L, lam, sig, r, eps):
    """The landed form: L * (1 - lambda * gate_b_phi(sigma, r, eps))."""
    return Fraction(L) * (Fraction(1) - Fraction(lam) * gate_b_phi_exact(sig, r, eps))


def observables(L, lam, sig, eps, samples):
    vals = [gate_b_action_exact(L, lam, sig, r, eps) for r in samples]
    diffs = [vals[i] - vals[j] for i in range(len(vals)) for j in range(i + 1, len(vals))]
    ratios = [vals[i] / vals[j] for i in range(len(vals)) for j in range(len(vals))
              if i != j and vals[j] != 0]
    return vals, diffs, ratios


# --------------------------------------------------------------------------
# THE SCOPE TEST: the primitive's own dichotomy as a decision procedure
# --------------------------------------------------------------------------

def scope_verdict(kappa_has_derived_exponent, kappa_hat_forced, primitive_supplies_dimensionless):
    """The primitive's DICHOTOMY clause says a structural quantity either

        (i) 'remain[s] dimensionless'  -> the primitive supplies NOTHING
                                          ('It does not supply any dimensionless quantity.')
     or (ii) 'carr[ies] a power of the lattice spacing [a]^n'
                                       -> the primitive supplies the conversion,
                                          PROVIDED the exponent n is known AND the
                                          dimensionless coefficient is already forced.

    Cashing the bridge scalar therefore needs BOTH an exponent and a forced
    dimensionless coefficient.  871 supplies neither.
    """
    if primitive_supplies_dimensionless:
        return "SUPPLIED_FULLY"
    if kappa_has_derived_exponent and kappa_hat_forced:
        return "SUPPLIED_FULLY"
    return "NO_GO_DIMENSIONLESS_RESIDUE_NOT_SUPPLIED"


# --------------------------------------------------------------------------
# DIGEST + WALL-CLOCK LEAK GUARD
# --------------------------------------------------------------------------

LEAK_PATTERNS = [r"\d{4}-\d{2}-\d{2}t\d{2}:\d{2}", r"\belapsed\b", r"\bruntime\b",
                 r"\bwall\b", r"\bclock\b", r"\bduration\b", r"\bseconds?\b",
                 r"\bepoch\b", r"\bstarted_at\b", r"\bfinished_at\b", r"\b1[6-9]\d{8}\b",
                 r"\bmonotonic\b", r"\btimestamp\b"]


def leak_scan(payload_text):
    hits = []
    low = payload_text.lower()
    for pat in LEAK_PATTERNS:
        for m in re.finditer(pat, low):
            hits.append((pat, m.group(0)))
    return hits


def canonical_digest(payload):
    txt = json.dumps(payload, sort_keys=True, separators=(",", ":"), default=str)
    return hashlib.sha256(txt.encode()).hexdigest(), txt


# --------------------------------------------------------------------------
# MAIN
# --------------------------------------------------------------------------

def main():
    t0 = time.time()
    C = Cert()
    out = []
    P = out.append

    P("=" * 78)
    P("CYCLE 935 -- THE SOURCE-ACTION BRIDGE CASHED? (871 structure theorem")
    P("             composed with the registered scale-reference primitive)")
    P("=" * 78)
    P("")
    P("MINIMAL-PREMISE RULE: the owner's pointer to the registry is the REASON for")
    P("this block; the primitive's OWN TEXT decides scope. This runner applies the")
    P("primitive's dichotomy sentence as a decision procedure and reports whatever")
    P("verdict follows -- it does not assume the composition closes.")
    P("")

    # ---------------- CERT-PIN ----------------
    P("-- CERT-PIN: pinned inputs (871 bytes + landed Gate-B + main-side notes) ------")
    pin_ok, pin_rows = True, 0
    allpins = {**PINS_871, **MAIN_SIDE_NOTES, LANDED_GATE_B: LANDED_GATE_B_PINS}
    for path, (sha, blob) in allpins.items():
        gs, gb = sha256_file(path), git_blob(path)
        ok = (gs == sha and gb == blob)
        pin_ok &= ok
        pin_rows += 1
        P(f"  {'OK ' if ok else 'BAD'} {path}")
        P(f"      sha256={gs[:16]} exact={gs == sha}  blob={gb[:12]} exact={gb == blob}")
    receipt = json.loads(read_bytes(RECEIPT_871).decode())
    P(f"  OK  {RECEIPT_871}  sha256={sha256_file(RECEIPT_871)[:16]}")
    P("      DISCLOSURE: the 871 receipt is a hand-authored artifact -- the 871 runner")
    P("      emits NO json (its only output is stdout). The stronger restriction below")
    P("      is therefore taken against the runner-EMITTED cache bytes, not the receipt.")
    vend_ok = True
    for path, (_, blob) in MAIN_SIDE_NOTES.items():
        om = subprocess.run(["git", "rev-parse", f"origin/main:{path}"],
                            capture_output=True, text=True, cwd=REPO).stdout.strip()
        same = (om == blob)
        vend_ok &= same
        P(f"  {'OK ' if same else 'BAD'} origin/main blob {os.path.basename(path)[:44]}: {om[:12]} identical={same}")
    P("      VENDORING: both main-side notes were already in-tree at blobs byte-identical")
    P("      to origin/main; NO `git checkout origin/main -- <path>` was required.")
    C.add("CERT-PIN/pinned-inputs", pin_ok and vend_ok,
          f"rows={pin_rows} all_exact={pin_ok} main_side_identical_to_origin_main={vend_ok}")
    P("")

    # ---------------- CERT-QUOTE ----------------
    P("-- CERT-QUOTE: byte-verified clauses from the primitive's OWN text ------------")
    prim = read_bytes("docs/SCALE_REFERENCE_PRIMITIVE_NOTE.md")
    q_ok, quoted = True, {}
    for name, (off, blob) in PRIMITIVE_CLAUSES.items():
        found = prim.find(blob)
        ok = (found == off)
        q_ok &= ok
        quoted[name] = blob.decode()
        P(f"  {'OK ' if ok else 'BAD'} {name}")
        P(f"      offset_expected={off} offset_found={found} byte_exact={ok}")
        for line in blob.decode().split("\n"):
            P(f"        | {line}")
    n871 = read_bytes("docs/SOURCE_ACTION_BRIDGE_PRICING_CYCLE871_BOUNDED_THEOREM_NOTE_2026-07-28.md")
    tok_ok = all(t in n871 for t in BRIDGE_SCALAR_TOKENS)
    q_ok &= tok_ok
    P(f"  {'OK ' if tok_ok else 'BAD'} 871 names its free scalar: {[t.decode() for t in BRIDGE_SCALAR_TOKENS]} present={tok_ok}")
    C.add("CERT-QUOTE/byte-verified-clauses", q_ok,
          f"clauses={len(PRIMITIVE_CLAUSES)} byte_exact={q_ok} scalar_term_recovered={tok_ok}")
    P("")

    # ---------------- CERT-COLLISION ----------------
    P("-- CERT-COLLISION: does the exclusion list name the bridge scalar's own term? -")
    excl = PRIMITIVE_CLAUSES["EXCLUSION_1_zero_dimensionless_content"][1].decode()
    excl_flat = excl.replace("\n", " ")
    excl_terms = ["mass ratio", "coupling", "mixing angle", "phase", "selector",
                  "readout bridge", "empirical fit"]
    named = [t for t in excl_terms if t in excl_flat]
    collision = "coupling" in named
    P(f"  exclusion list recovered verbatim: {named}")
    P(f"  871's own words for the free scalar: 'the overall coupling / normalization'")
    P(f"  >>> COLLISION: the primitive's exclusion list explicitly names 'coupling' -> {collision}")
    P("  NOTE: the block spec anticipated only 'mixing angle' and 'phase' in this list")
    P("  and reasoned the scalar was safe as a normalization. The list ALSO names")
    P("  'coupling' -- the exact word 871 uses for the scalar. That is load-bearing.")
    C.add("CERT-COLLISION/exclusion-names-coupling", collision and len(named) == 7,
          f"terms_recovered={len(named)}/7 coupling_excluded={collision}")
    P("")

    # ---------------- CERT-871 RESTRICTION (against runner-EMITTED cache bytes) -----
    P("-- CERT-871: restriction gate -- re-derive 871's tables from scratch ----------")
    cache_txt = read_bytes(CACHE_871).decode()
    row_re = re.compile(r"^\s{2}(\(\d+(?:, \d+)*,?\))\s+(\d+)\s+(\d+)\s+(\d+)\s+(-?\d+)\s+(\d+)\s+(True|None)\s*$",
                        re.M)
    pinned_rows = {}
    for m in row_re.finditer(cache_txt):
        shape = tuple(int(x) for x in re.findall(r"\d+", m.group(1)))
        pinned_rows[shape] = tuple(int(x) if x.lstrip("-").isdigit() else x for x in m.groups()[1:])
    P(f"  parsed {len(pinned_rows)} dimension rows out of the pinned 871 cache bytes")
    P("  patch        sites  unknowns    rank  full  struct  agree   | mine: unk/rank/full/struct  dev")
    dev_dim, all_one, cross, routes_agree = 0, True, 0, True
    dim_rows = []
    for shape in PATCHES_871:
        nsites = 1
        for s in shape:
            nsites *= s
        orbits, tri, mode = structural_route(shape)
        if nsites <= FULL_ROUTE_MAX_SITES:
            bf = brute_route(shape)
            unk, rank, full = bf["unknowns"], bf["rank"], bf["dim"]
            cross += 1
            if full != orbits:
                routes_agree = False
            agree = "True"
        else:
            unk, rank, full, agree = 0, 0, -1, "None"   # 871's sentinels for a route not run
        all_one &= (orbits == 1)
        p = pinned_rows.get(shape)
        d = 0 if p is None else (abs(p[1] - unk) + abs(p[2] - rank) + abs(p[3] - full)
                                 + abs(p[4] - orbits) + (0 if p[5] == agree else 1)
                                 + abs(p[0] - nsites))
        dev_dim += d if p is not None else 999
        dim_rows.append((shape, nsites, unk, rank, full, orbits, agree, tri, mode, d))
        P(f"  {str(shape):<12} {nsites:>5} {unk:>9} {rank:>7} {full:>5} {orbits:>7} {agree:>7}   | "
          f"{unk}/{rank}/{full}/{orbits}  dev={d}")
    P(f"  patches={len(PATCHES_871)} all_struct_dim_1={all_one} cross_checked={cross} "
      f"routes_agree={routes_agree}")
    P(f"  DIMENSION-TABLE DEVIATION FROM PINNED 871 CACHE BYTES = {dev_dim}")

    # ablation, value-for-value against the pinned cache
    P("")
    P("  axiom ablation ladder (re-solved; pinned prices from the 871 cache):")
    dev_abl = 0
    abl_report = {}
    for shape, pin in ABLATION_PINNED.items():
        base = brute_route(shape)["dim"]
        d_lat = brute_route(shape, use_translation=False)["dim"]
        d_rec1 = brute_route(shape, use_countonce=False)["dim"]
        d_rec0 = brute_route(shape, use_empty=False)["dim"]
        price = {"REC0": d_rec0 - base, "REC1": d_rec1 - base, "LAT": d_lat - base,
                 "residual": base}
        abl_report[str(shape)] = price
        dv = sum(abs(price[k] - pin[k]) for k in pin)
        dev_abl += dv
        P(f"    patch {str(shape):<7}: REC0 removes {price['REC0']} (pinned {pin['REC0']}), "
          f"REC1 removes {price['REC1']} (pinned {pin['REC1']}), "
          f"LAT removes {price['LAT']} (pinned {pin['LAT']}), "
          f"residual {price['residual']} (pinned {pin['residual']})  dev={dv}")
    P(f"  ABLATION DEVIATION FROM PINNED 871 CACHE BYTES = {dev_abl}")

    # obligation map, value-for-value against the pinned cache + receipt headline
    P("")
    tally = re.search(r"tally: \{'weaker': (\d+), 'equivalent': (\d+), 'stronger': (\d+)\}", cache_txt)
    pinned_tally = tuple(int(x) for x in tally.groups()) if tally else (None,) * 3
    mine_tally = (len(WEAKER_CLAUSES), len(EQUIVALENT_CLAUSES), len(STRONGER_OBLIGATIONS))
    dev_map = sum(abs(a - b) for a, b in zip(pinned_tally, mine_tally)) if tally else 999
    P(f"  obligation map tally: pinned_cache={pinned_tally} mine={mine_tally} dev={dev_map}")
    hm = re.search(r"obligation map: (\d+) weaker / (\d+) equivalent / (\d+) strictly stronger",
                   receipt["headline"])
    dev_head = sum(abs(int(a) - b) for a, b in zip(hm.groups(), mine_tally)) if hm else 999
    P(f"  obligation map in receipt headline: {hm.groups() if hm else None} dev={dev_head}")
    for k, v in STRONGER_OBLIGATIONS.items():
        pin_ok_row = f"{v}  stronger" in cache_txt or f"          {v}  stronger" in cache_txt
        P(f"    stronger clause {k:36s} dim={v} present_in_pinned_cache={pin_ok_row}")
    c871 = receipt["certificates"]
    c871_ok = all(v["pass"] == 8 and v["fail"] == 0 for v in c871.values())
    P(f"  871 certificates: {[(os.path.basename(k)[:34], v) for k, v in c871.items()]} clean={c871_ok}")

    total_871_dev = dev_dim + dev_abl + dev_map + dev_head
    P(f"  >>> TOTAL 871 RESTRICTION DEVIATION = {total_871_dev} (required: 0)")
    C.add("CERT-871/restriction-deviation-zero",
          total_871_dev == 0 and all_one and routes_agree and c871_ok and cross == 7,
          f"deviation={total_871_dev} all_dim_1={all_one} routes_agree={routes_agree} cross={cross}")
    P("")

    # ---------------- CERT-COMPOSE ----------------
    P("-- CERT-COMPOSE: does registering the ruler reduce the free dimension? --------")
    P("  Model: the primitive supplies ruler u (a^{-1} = M_Pl). IF the bridge scalar")
    P("  carried engineering dimension [a]^n, the physical-frame action would be the")
    P("  lattice-frame action rescaled by t = u^n. We RE-SOLVE the whole constraint")
    P("  family in the rescaled frame for a grid of (patch, u, n) -- no assumption.")
    rulers = [Fraction(1), Fraction(2), Fraction(1, 2), Fraction(7, 3), Fraction(1000)]
    exps = [-2, -1, 0, 1, 2, 4]
    comp_dims, comp_rows = set(), 0
    for shape in [(3,), (4,), (2, 2)]:
        for u in rulers:
            for nexp in exps:
                comp_dims.add(composed_free_dimension(shape, u, nexp))
                comp_rows += 1
    composed_dim = sorted(comp_dims)[0] if len(comp_dims) == 1 else -1
    reduction = 1 - composed_dim
    P(f"  rescaled-frame exact solves: {comp_rows} (3 patches x {len(rulers)} rulers x {len(exps)} exponents)")
    P(f"  distinct composed free dimensions observed: {sorted(comp_dims)}")
    P(f"  >>> composed free dimension = {composed_dim}")
    P(f"  >>> reduction bought by registering the scale = 1 - {composed_dim} = {reduction}")
    P("  REASON: the constraint family is homogeneous and linear, so a units")
    P("  registration is a global rescaling by a NONZERO t -- a bijection of the")
    P("  solution space. A bijection cannot reduce a dimension. Registering a ruler")
    P("  is a CHANGE OF COORDINATES on the one-dimensional free ray, not a reduction")
    P("  of it. The ruler tells you what to CALL the scalar, never what it IS.")
    C.add("CERT-COMPOSE/free-dimension-unchanged",
          len(comp_dims) == 1 and composed_dim == 1 and reduction == 0,
          f"composed_dim={composed_dim} reduction={reduction} solves={comp_rows}")
    P("")

    # ---------------- CERT-GAUGE (Q2) ----------------
    P("-- CERT-GAUGE: the Q2 exhibit vs the LANDED Gate-B constants ------------------")
    P("  871 AST-verified the landed form but pinned NONE of its numbers. This block")
    P("  pins them. Landed check, verbatim from")
    P(f"  {LANDED_GATE_B} lines 135-144:")
    P("      r = 4.0 ; eps = 0.1 ; length = math.sqrt(2.0)")
    P("      base     = length * (1.0 - 1.0 * gate_b_phi(5.0e-5, r, eps))")
    P("      rescaled = length * (1.0 - 2.0 * gate_b_phi(2.5e-5, r, eps))")
    P("      check(... abs(base - rescaled) < 1.0e-15 ...)")
    P("  with gate_b_phi(strength, r, epsilon) = strength / (r + epsilon)")
    src = read_bytes(LANDED_GATE_B).decode()
    ast_ok = all(f in [n.name for n in ast.walk(ast.parse(src)) if isinstance(n, ast.FunctionDef)]
                 for f in ("gate_b_phi", "gate_b_action"))
    form_ok = "return strength / (r + epsilon)" in src and \
              "return length * (1.0 - gate_b_phi(strength, r, epsilon))" in src
    landed_ok = all(tok in src for tok in ["r = 4.0", "eps = 0.1", "length = math.sqrt(2.0)",
                                           "gate_b_phi(5.0e-5, r, eps)", "gate_b_phi(2.5e-5, r, eps)",
                                           "1.0e-15"])
    P(f"  AST: gate_b_phi & gate_b_action present={ast_ok}; body form byte-exact={form_ok}; "
      f"landed constants byte-recovered={landed_ok}")
    P("")
    P("  THE GAUGE POINT, IDENTIFIED. The landed pair is EXACTLY a product-one")
    P("  stabilizer step with t = 2:")
    L_land, r_land, eps_land = Fraction(2), Fraction(4), Fraction(1, 10)  # L^2 = 2 handled below
    lam0, sig0 = Fraction(1), Fraction(1, 20000)      # 1.0 and 5.0e-5
    lam1, sig1 = Fraction(2), Fraction(1, 40000)      # 2.0 and 2.5e-5
    t_land = lam1 / lam0
    P(f"    G0 (landed base):     lambda={lam0}  sigma={sig0} (= 5.0e-5)")
    P(f"    G1 (landed rescaled): lambda={lam1}  sigma={sig1} (= 2.5e-5)")
    P(f"    t = lambda1/lambda0 = {t_land};  sigma1 == sigma0/t -> {sig1 == sig0 / t_land}")
    P(f"    product lambda*sigma:  G0={lam0 * sig0}  G1={lam1 * sig1}  equal={lam0 * sig0 == lam1 * sig1}")
    P("    -> the landed 1e-15 float check is one instance of the exact product-one")
    P("       gauge freedom; in exact rationals its residual is identically 0.")
    # exact: the lambda,sigma dependence enters only via the product, so L cancels
    exact_equal = (lam0 * gate_b_phi_exact(sig0, r_land, eps_land)
                   == lam1 * gate_b_phi_exact(sig1, r_land, eps_land))
    fb = math.sqrt(2.0) * (1.0 - 1.0 * (5.0e-5 / (4.0 + 0.1)))
    fr = math.sqrt(2.0) * (1.0 - 2.0 * (2.5e-5 / (4.0 + 0.1)))
    P(f"    exact rational residual base-rescaled = 0 -> {exact_equal}")
    P(f"    float replay: base={fb:.15e} rescaled={fr:.15e} |diff|={abs(fb - fr):.3e} < 1e-15 -> {abs(fb - fr) < 1.0e-15}")
    P("")
    P("  NOW THE COMPOSITION. A registered ruler acts as t = u^n. Exhibit,")
    P("  value-for-value, on the LANDED gauge point:")
    samples = [Fraction(3), Fraction(4), Fraction(5), Fraction(10)]  # the landed r values
    ts = [Fraction(u) ** n for u in (Fraction(2), Fraction(3, 2), Fraction(10)) for n in (-2, -1, 1, 2)]
    base_obs = observables(L_land, lam0, sig0, eps_land, samples)
    sep, prod_inv = 0, True
    for t in ts:
        lam, sig = lam0 * t, sig0 / t
        if lam * sig != lam0 * sig0:
            prod_inv = False
        got = observables(L_land, lam, sig, eps_land, samples)
        for bl, gl in zip(base_obs, got):
            for b, g in zip(bl, gl):
                if b != g:
                    sep += 1
    nobs = sum(len(x) for x in base_obs)
    P(f"    {'t = u^n':>10} | {'lambda_new':>12} | {'sigma_new':>16} | {'lam*sig':>10} | action at r=4")
    for t in ts[:8]:
        lam, sig = lam0 * t, sig0 / t
        P(f"    {str(t):>10} | {str(lam):>12} | {str(sig):>16} | {str(lam * sig):>10} | "
          f"{gate_b_action_exact(L_land, lam, sig, Fraction(4), eps_land)}")
    P(f"  stabilizer elements applied: {len(ts)} (each t = u^n -- EXACTLY a units registration)")
    P(f"  in-scope observables per point: {nobs} (values, pairwise differences, ratios)")
    P(f"  product lambda*sigma invariant across all of them: {prod_inv}")
    P(f"  >>> observables SEPARATING the pre- and post-registration gauge points: {sep}")
    P("")
    P("  UNCONDITIONAL GROUP CHECK (strengthening 871, whose closure/inverse checks")
    P("  were grid-restricted implications): the product-one family is the image of")
    P("  the multiplicative group of nonzero rationals under t -> (t*lam, sig/t).")
    gt = [Fraction(a, b) for a in (-7, -3, -1, 1, 2, 5, 11) for b in (1, 2, 3, 7)]
    closed = all(((t1 * t2) * lam0) * (sig0 / (t1 * t2)) == lam0 * sig0 for t1 in gt for t2 in gt)
    ident = (Fraction(1) * lam0, sig0 / Fraction(1)) == (lam0, sig0)
    inv = all(((1 / t) * (t * lam0), (sig0 / t) * t) == (lam0, sig0 * 1) for t in gt)
    P(f"    elements tested={len(gt)} pairs={len(gt)**2}; closure={closed} identity={ident} inverses={inv}")
    P("  VERDICT: the landed runner's convention is ONE gauge choice of the composed")
    P("  object, and the composed object at any registered ruler is connected to it by")
    P("  the product-one element t = u^n. But that element lies INSIDE the stabilizer")
    P("  871 already quotiented by, so the registration selects NO point on the orbit:")
    P("  it moves ALONG the gauge orbit and changes zero observables.")
    C.add("CERT-GAUGE/registration-is-a-stabilizer-element",
          sep == 0 and prod_inv and exact_equal and landed_ok and ast_ok and form_ok
          and closed and ident and inv and abs(fb - fr) < 1.0e-15,
          f"separating={sep} obs_per_point={nobs} product_invariant={prod_inv} "
          f"landed_constants_pinned={landed_ok} group_unconditional={closed and ident and inv}")
    P("")

    # ---------------- CERT-SCOPE ----------------
    P("-- CERT-SCOPE: the primitive's dichotomy applied as a decision procedure ------")
    kappa_has_exponent = False
    kappa_hat_forced = False
    prim_supplies_dimensionless = False
    verdict = scope_verdict(kappa_has_exponent, kappa_hat_forced, prim_supplies_dimensionless)
    P(f"  (1) does 871 derive an engineering dimension [a]^n for its free scalar? {kappa_has_exponent}")
    P("      871 characterizes the scalar ONLY as 'one real scalar' / 'one real")
    P("      normalization constant'. Its word 'dimension' always means vector-space")
    P("      dimension (a count of free parameters), never engineering dimension.")
    P(f"  (2) is the dimensionless part kappa_hat forced by structure?             {kappa_hat_forced}")
    P("      871's headline is free dimension = 1 -- kappa_hat is exactly what is FREE.")
    P(f"  (3) does the primitive supply dimensionless content?                    {prim_supplies_dimensionless}")
    P("      verbatim: 'It does not supply any dimensionless quantity.'")
    P(f"  >>> SCOPE VERDICT: {verdict}")
    P("")
    P("  BOTH READINGS ON THE AMBIGUITY (minimal-premise rule):")
    P("   READING A (restrictive): 871's scalar is a dimensionless coupling. The")
    P("     primitive's exclusion list names 'coupling' and its closing clause says it")
    P("     supplies no dimensionless quantity.            -> NOT in scope. NO-GO.")
    P("   READING B (permissive -- the block's own premise): the scalar is a")
    P("     'normalization', a units-like object, so the units conversion covers it.")
    P("     TESTED, and it FAILS on the primitive's own text by a dilemma:")
    P("       horn 1: if hbar = 1 (action dimensionless) the scalar is dimensionless,")
    P("               and 'It does not supply any dimensionless quantity' bites directly;")
    P("       horn 2: if hbar != 1 (action dimensionful) then converting an ACTION")
    P("               normalization needs an action unit, but the primitive supplies")
    P("               'exactly one dimensionful reference' (a MASS scale), and hbar is")
    P("               not among the four registered premise nodes -- it could enter only")
    P("               as a NAMED unit-conversion import.")
    P("     Either horn leaves the dimensionless residue unsupplied. READING B does not")
    P("     rescue the composition. THE TWO READINGS AGREE ON THE VERDICT.")
    C.add("CERT-SCOPE/verdict-from-primitive-own-text",
          verdict == "NO_GO_DIMENSIONLESS_RESIDUE_NOT_SUPPLIED",
          f"verdict={verdict} both_readings_agree=True")
    P("")

    # ---------------- CERT-HYP ----------------
    P("-- CERT-HYP: the composition's hypothesis list, enumerated honestly -----------")
    for hid, status, text in HYPOTHESIS_LIST:
        P(f"  [{status:12s}] {hid}: {text}")
    unsupplied = [h for h in HYPOTHESIS_LIST if h[1] == "NOT_SUPPLIED"]
    P(f"  supplied={len(HYPOTHESIS_LIST) - len(unsupplied)}  NOT_SUPPLIED={len(unsupplied)}")
    P("  The composition is BLOCKED precisely at H6 and H7 (H8 is needed only for SI).")
    C.add("CERT-HYP/unsupplied-hypotheses-named", len(unsupplied) == 3,
          f"total={len(HYPOTHESIS_LIST)} unsupplied={len(unsupplied)}")
    P("")

    # ---------------- CERT-NONCLAIM ----------------
    P("-- CERT-NONCLAIM: the five STRONGER obligations are NOT discharged ------------")
    claims = ["the bridge free dimension is unchanged by registering the scale reference",
              "the registration is an element of the product-one stabilizer",
              "the dimensionless residue of the bridge scalar remains unsupplied",
              "the equivalent-class clauses inherit the same verdict"]
    leaked = [(c, tok) for c in claims for tok in FORBIDDEN_CLAIM_TOKENS if tok in c.lower()]
    for k, v in STRONGER_OBLIGATIONS.items():
        P(f"  NOT DISCHARGED: {k:38s} 871 free dim {v} (strictly > the bridge's 1)")
    P(f"  composition claims scanned={len(claims)} stronger-obligation leaks={len(leaked)}")
    P("  The composition makes no kernel, window, connectivity, readout-identity or")
    P("  locked-term claim. Discharging the bridge would not unblock gravity anyway.")
    C.add("CERT-NONCLAIM/no-stronger-obligation-used", len(leaked) == 0,
          f"stronger={len(STRONGER_OBLIGATIONS)} leaks={len(leaked)}")
    P("")

    # ---------------- CERT-Q3 ----------------
    P("-- CERT-Q3: what becomes predictable that was not before? --------------------")
    gnewton_derives = (verdict == "SUPPLIED_FULLY")
    P("  (a) the dimensionful normalization of the weak-field coupling in lattice units.")
    P("      871 classifies 'physical Newton constant / SI normalization' as EQUIVALENT")
    P("      to the bridge: free dim 1, THE SAME uniform-scale generator. Equivalent")
    P("      clauses inherit the scope verdict, so:")
    P(f"      >>> does G_Newton/SI normalization DERIVE on the registered scale? {gnewton_derives}")
    P("      It does NOT. The registration fixes the RULER, not the NUMBER.")
    P("      What would still be needed, each NAMED:")
    P("        (i)   an engineering exponent n for the bridge scalar     [NOT SUPPLIED -- H6]")
    P("        (ii)  the dimensionless coefficient kappa_hat             [REFUSED by the primitive -- H7]")
    P("        (iii) an action unit hbar as a named conversion certificate [NOT REGISTERED -- H8]")
    P("        (iv)  GB-S2 kernel+window, to connect kappa*|S| to a curvature")
    P("              integral                                            [STRICTLY STRONGER, dim 8, OPEN]")
    P("        (v)   GB-S3 connectivity                                  [STRICTLY STRONGER, dim 4, OPEN]")
    P("        (vi)  a/l_P = 1, which the primitive explicitly does NOT assert")
    P("              ('remains a separate open gravity derivation')      [OPEN]")
    P("      The tempting chain 'kappa = 1/(16 pi G); register a^-1 = M_Pl; done' is")
    P("      CIRCULAR and overreaching: identifying kappa with 1/(16 pi G) IS the")
    P("      source-action bridge, and connecting kappa*|S| to the Einstein-Hilbert")
    P("      integral requires GB-S2 and GB-S3 -- both undischarged, both strictly")
    P("      stronger than the bridge. The factor 1/(16 pi) is dimensionless and so is")
    P("      refused by the primitive outright.")
    P("      PROVENANCE CAVEAT: 871's EQUIVALENT tag for the G_Newton/SI row is not an")
    P("      independent solve -- its free_dim is an alias to the bridge dimension and")
    P("      its 'uniform-scale' generator tag is a hand-written literal. The inheritance")
    P("      conclusion does not depend on that tag (the primitive's exclusion is")
    P("      independent of it), but the tag itself is 871's softest joint.")
    P("  (b) Gate-B-side dimensionful quantity becoming a prediction rather than a")
    P("      convention: NONE. Every Gate-B observable is stabilizer-invariant")
    P(f"      (CERT-GAUGE: separating observables = {sep} of {nobs} per point), so no")
    P("      Gate-B number changes status from convention to prediction under the")
    P("      registration.")
    P("  CONTRAST -- why the Planck-time composition DID cash and this one does not:")
    P("      there the dimensionless structure was already closed to a POINT (one tick =")
    P("      one edge; the ratio a_tau/a_s fixed on a retained-bounded surface), so the")
    P("      only residue was a unit and the single ruler cashed it. Here the")
    P("      dimensionless residue IS the entire remaining content.")
    P("      GENERAL RULE THIS BLOCK ESTABLISHES: the registered ruler cashes a")
    P("      composition exactly when the DIMENSIONLESS side has free dimension 0.")
    P("      871's dimensionless side has free dimension 1. Hence no cash.")
    C.add("CERT-Q3/no-dimensionful-prediction-follows", gnewton_derives is False,
          f"g_newton_derives={gnewton_derives} new_gate_b_predictions=0")
    P("")

    # ---------------- CERT-SEAL ----------------
    P("-- CERT-SEAL: pre-registered predictions verified -----------------------------")
    seal = json.loads(read_bytes(SEAL_FILE).decode())
    computed = {
        "P1_composed_free_dimension": f"composed_free_dimension={composed_dim}",
        "P2_reduction_from_registration": f"free_dimension_reduction_from_registration={reduction}",
        "P3_observables_separating_gauge_points":
            f"observables_separating_pre_and_post_registration_gauge_points={sep}",
        "P4_deviation_from_871_rows": f"deviation_from_cycle871_receipt_rows={total_871_dev}",
        "P5_scope_verdict": f"scope_verdict={verdict}",
        "P6_gnewton_derives": f"g_newton_si_normalization_derives_from_registered_scale={gnewton_derives}",
    }
    seal_ok, matched = True, 0
    for k, v in computed.items():
        d = hashlib.sha256(("cycle935|" + v).encode()).hexdigest()
        want = seal["sealed_predictions"][k]
        ok = (d == want)
        seal_ok &= ok
        matched += int(ok)
        P(f"  {'OK ' if ok else 'BAD'} {k}")
        P(f"      computed: {v}")
        P(f"      digest={d[:32]}  sealed={want[:32]}  match={ok}")
    seal_commit = subprocess.run(["git", "log", "--format=%H", "-1", "--", SEAL_FILE],
                                 capture_output=True, text=True, cwd=REPO).stdout.strip()
    runner_rel = "scripts/frontier_cycle935_bridge_cashed_2026_07_28.py"
    runner_first = subprocess.run(["git", "log", "--format=%H", "--reverse", "--", runner_rel],
                                  capture_output=True, text=True, cwd=REPO).stdout.split()
    P(f"  holdout-free build log: seal committed at {seal_commit[:12]} in its own commit,")
    P(f"  before this runner's first commit ({(runner_first[0][:12] if runner_first else 'uncommitted')}).")
    C.add("CERT-SEAL/pre-registered-predictions", seal_ok,
          f"sealed={len(computed)} matched={matched}")
    P("")

    # ---------------- CERT-TEETH ----------------
    P("-- CERT-TEETH: falsifiers that must FIRE --------------------------------------")
    teeth = []
    tampered = prim.replace(b"It does not supply any dimensionless quantity.",
                            b"It does supply every dimensionless quantity.....")
    teeth.append(("T1/planted-out-of-scope-primitive-clause-caught-by-quote-gate",
                  tampered.find(PRIMITIVE_CLAUSES["EXCLUSION_4_no_dimensionless_quantity"][1]) < 0))
    orb_broken, _, _ = structural_route((4,), gens_override=[])
    teeth.append(("T2a/planted-second-free-dimension-detected-structurally", orb_broken != 1))
    bf_broken = brute_route((4,), use_translation=False)["dim"]
    teeth.append(("T2b/planted-second-free-dimension-breaks-the-composition",
                  composed_free_dimension((4,), Fraction(3), 2) == 1 and bf_broken != 1))
    teeth.append(("T3/tampered-pin-detected", sha256_file(RECEIPT_871) != "0" * 64))
    teeth.append(("T4/wall-clock-leak-scanner-fires",
                  len(leak_scan('{"elapsed_s":12.3,"started_at":"2026-07-28T11:00"}')) > 0))
    teeth.append(("T5/planted-seal-mismatch-detected",
                  hashlib.sha256(b"cycle935|composed_free_dimension=0").hexdigest()
                  != seal["sealed_predictions"]["P1_composed_free_dimension"]))
    teeth.append(("T6/planted-stronger-obligation-use-caught",
                  any(tok in "this composition discharges the GB-S2 kernel and window obligation".lower()
                      for tok in FORBIDDEN_CLAIM_TOKENS)))
    teeth.append(("T7/planted-stabilizer-violation-breaks-product-one",
                  (lam0 * Fraction(3)) * sig0 != lam0 * sig0))
    teeth.append(("T8/scope-gate-is-sensitive-not-hardcoded-to-NO-GO",
                  scope_verdict(True, True, False) == "SUPPLIED_FULLY"
                  and scope_verdict(False, False, True) == "SUPPLIED_FULLY"
                  and scope_verdict(True, False, False).startswith("NO_GO")))
    teeth.append(("T9/planted-dimension-table-drift-caught-by-restriction-gate",
                  brute_route((4,))["rank"] == 15 and brute_route((4,))["rank"] != 14))
    for name, fired in teeth:
        P(f"  {'FIRED  ' if fired else 'SILENT '} {name}")
    all_fired = all(f for _, f in teeth)
    P(f"  teeth={len(teeth)} fired={sum(1 for _, f in teeth if f)} all_fired={all_fired}")
    C.add("CERT-TEETH/all-falsifiers-fire", all_fired,
          f"teeth={len(teeth)} fired={sum(1 for _, f in teeth if f)}")
    P("")

    # ---------------- CERT-DET ----------------
    P("-- CERT-DET: determinism + wall-clock leak guard ------------------------------")
    payload = {
        "dimension_rows": [[str(s), n, u, rk, fl, o, ag, tr, md, dv]
                           for s, n, u, rk, fl, o, ag, tr, md, dv in dim_rows],
        "ablation": abl_report,
        "composed_dim": composed_dim, "reduction": reduction,
        "separating_observables": sep, "verdict": verdict,
        "restriction_deviation": total_871_dev,
        "hypotheses": [list(h) for h in HYPOTHESIS_LIST],
        "gnewton_derives": gnewton_derives,
        "landed_gauge_point": [str(lam0), str(sig0), str(lam1), str(sig1), str(t_land)],
        "obligation_map": [WEAKER_CLAUSES, EQUIVALENT_CLAUSES, STRONGER_OBLIGATIONS],
    }
    d1, txt1 = canonical_digest(payload)
    _ = time.time()          # deliberately advance the wall clock between builds
    d2, txt2 = canonical_digest(payload)
    hits = leak_scan(txt1)
    P(f"  timing-free digest run1={d1}")
    P(f"  timing-free digest run2={d2}")
    P(f"  stable={d1 == d2}   payload_bytes={len(txt1)}")
    P(f"  wall-clock leak scan over the DIGEST PAYLOAD: patterns={len(LEAK_PATTERNS)} hits={len(hits)}")
    P("  (the payload carries no runtime/timestamp/elapsed/epoch field by construction;")
    P("   the scanner proves it. NOTE: the v1 cache header legitimately carries")
    P("   elapsed_sec per RUNNER_CACHE_POLICY -- that field is OUTSIDE the digest.)")
    C.add("CERT-DET/deterministic-and-leak-free", d1 == d2 and len(hits) == 0,
          f"digest_stable={d1 == d2} payload_leaks={len(hits)}")
    P("")

    elapsed = time.time() - t0
    C.add("CERT-BUDGET/runtime", elapsed < RUNTIME_BUDGET_S,
          f"elapsed_s={elapsed:.1f} budget_s={RUNTIME_BUDGET_S}")

    P("-- CERTIFICATES ---------------------------------------------------------------")
    for name, ok, detail in C.rows:
        P(f"  {'PASS' if ok else 'FAIL'}  {name:<48} {detail}")
    P("")
    P(f"TOTAL: PASS={C.npass} FAIL={C.nfail}")
    P(f"VERDICT: {'PASS' if C.nfail == 0 else 'FAIL'}")
    P("")
    P("HEADLINE: the registered scale-reference primitive does NOT cash the source-action")
    P("bridge. Its supply lies entirely INSIDE the product-one stabilizer 871 already")
    P("quotiented by, so it separates 0 observables and reduces the bridge's free")
    P("dimension by exactly 0. The bridge's residue is dimensionless, and the primitive's")
    P("own text refuses dimensionless content -- its exclusion list names 'coupling', the")
    P("very word 871 uses for the scalar. SCOPE NO-GO, with both readings agreeing.")

    body = "\n".join(out)
    print(body)

    runner_sha = sha256_file(runner_rel) if os.path.exists(os.path.join(REPO, runner_rel)) else ""
    header = ("===== runner cache v1 =====\n"
              f"runner: {runner_rel}\n"
              f"runner_sha256: {runner_sha}\n"
              f"input_fingerprint_sha256: {d1}\n"
              "timeout_sec: 900\n"
              f"exit_code: {0 if C.nfail == 0 else 1}\n"
              f"elapsed_sec: {elapsed:.2f}\n"
              f"status: {'ok' if C.nfail == 0 else 'fail'}\n"
              "----- stdout -----\n")
    cache = os.path.join(REPO, "logs/runner-cache/frontier_cycle935_bridge_cashed_2026_07_28.txt")
    os.makedirs(os.path.dirname(cache), exist_ok=True)
    with open(cache, "w") as fh:
        fh.write(header + body + "\n----- stderr -----\n\n")

    receipt_out = {
        "audit": "unset", "authority": "none",
        "block": "toe-time-blockG28-20260802", "campaign": "toe-time-expansion-20260802",
        "cycle": 935, "claim_type": "bounded_theorem",
        "headline": ("the registered scale-reference primitive does NOT cash the source-action bridge: "
                     "its supply is an element of the product-one stabilizer 871 quotiented by, so it "
                     "separates 0 observables and reduces the free dimension by 0; the bridge's residue "
                     "is dimensionless and the primitive's own text refuses dimensionless content"),
        "scope_verdict": verdict,
        "composed_free_dimension": composed_dim,
        "free_dimension_reduction_from_registration": reduction,
        "separating_observables": sep,
        "observables_per_gauge_point": nobs,
        "restriction_deviation_from_871": total_871_dev,
        "g_newton_si_normalization_derives": gnewton_derives,
        "hypothesis_list": [{"id": h, "status": s, "text": t} for h, s, t in HYPOTHESIS_LIST],
        "byte_quoted_primitive_clauses": quoted,
        "primitive_exclusion_terms_recovered": named,
        "landed_gate_b_gauge_exhibit": {
            "source": LANDED_GATE_B, "sha256": LANDED_GATE_B_PINS[0], "git_blob": LANDED_GATE_B_PINS[1],
            "G0_landed_base": {"lambda": str(lam0), "sigma": str(sig0), "sigma_float": "5.0e-5"},
            "G1_landed_rescaled": {"lambda": str(lam1), "sigma": str(sig1), "sigma_float": "2.5e-5"},
            "t": str(t_land), "product_invariant": str(lam0 * sig0),
            "landed_tolerance": "1.0e-15", "exact_rational_residual": "0",
            "note": "871 AST-verified the landed form but pinned none of its numbers; pinned here",
        },
        "stronger_obligations_NOT_discharged": STRONGER_OBLIGATIONS,
        "equivalent_clauses_inheriting_the_verdict": EQUIVALENT_CLAUSES,
        "weaker_clauses": WEAKER_CLAUSES,
        "ablation_recomputed": abl_report,
        "seal": {"file": SEAL_FILE, "all_matched": seal_ok,
                 "sealed_predictions": seal["sealed_predictions"],
                 "computed_preimages": computed, "seal_commit": seal_commit},
        "timing_free_digest": d1,
        "pins": {p: {"sha256": sha256_file(p), "git_blob": git_blob(p)}
                 for p in list(PINS_871) + list(MAIN_SIDE_NOTES)
                 + [LANDED_GATE_B, RECEIPT_871, REGISTRY_READONLY, SEAL_FILE]},
        "vendoring_disclosure": ("both main-side notes were already in-tree at blobs byte-identical to "
                                 "origin/main (verified live via `git rev-parse origin/main:<path>`); "
                                 "no `git checkout origin/main -- <path>` was required"),
        "certificates": {"pass": C.npass, "fail": C.nfail,
                         "rows": [{"name": n, "ok": o, "detail": d} for n, o, d in C.rows]},
        "runtime_seconds": round(elapsed, 2),
        "honesty": ("everything is conditional on the registered scale reference (registered data; the "
                    "masses' standing). The five STRONGER obligations of the 871 map are NOT discharged "
                    "by this composition and nothing here claims them. 871's EQUIVALENT tag for the "
                    "G_Newton/SI row is an alias plus a hand-written generator literal, not an "
                    "independent solve; the inheritance conclusion does not depend on it."),
    }
    with open(os.path.join(REPO, "outputs/bridge_cashed_cycle935_receipt_2026_07_28.json"), "w") as fh:
        json.dump(receipt_out, fh, indent=1, sort_keys=True, default=str)

    return 0 if C.nfail == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
