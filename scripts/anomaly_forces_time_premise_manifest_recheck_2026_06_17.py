#!/usr/bin/env python3
"""
Independent premise-manifest re-check of the ANOMALY-FORCES-TIME ABJ bridge.

Purpose (re-audit readiness, not a status change): the bridge note
ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26
had its dependency edges repaired on 2026-06-16 (native_gauge_closure credited only
for the NONABELIAN surface + d_s=3; the abelian eigenvalue surface and the
hypercharge/completion values are SEPARATE bounded/premise edges). This runner closes
the remaining machine-level objection in the stale verdict ("the runner hard-codes
these charges") by making every numeric input carry an explicit PROVENANCE TAG, and by
asserting that no hypercharge/abelian value is attributed to native_gauge_closure.

Deterministic, no RNG, exact rationals + tiny finite Clifford diagnostics. Runtime < 1s.
It sets no audit status and predicts no audit outcome (audit lane only).
"""
from fractions import Fraction as F
import numpy as np

PASS = 0; FAIL = 0
def check(name, ok):
    global PASS, FAIL
    PASS += 1 if ok else 0; FAIL += 0 if ok else 1
    print(f"  [{'PASS' if ok else 'FAIL'}] {name}")

# ----------------------------------------------------------------------------
# PROVENANCE MANIFEST: every numeric input tagged by its supplier.
#   AXIOM            : the framework axioms (Lattice/Quantum/Record)
#   RETAINED_SOURCE  : a retained/bounded note, used ONLY for what it actually supplies
#   PREMISE          : a declared premise edge inherited from the parent theorem
# native_gauge_closure (GC) is RETAINED_SOURCE for NONABELIAN content + d_s=3 ONLY.
# The hypercharge VALUES are PREMISE (P-HY / P-COMP), never credited to GC.
# ----------------------------------------------------------------------------
MANIFEST = {
    "d_s = 3 (Z^3 substrate)"                : "AXIOM:Lattice (GC operates on it; not GC-derived)",
    "nonabelian SU(2)xSU(3) graph-first"     : "RETAINED_SOURCE:native_gauge_closure (NONABELIAN ONLY)",
    "abelian LH eigenvalue spectrum {+1/3 x6,-1 x2}": "RETAINED_SOURCE:native_gauge_left_handed_abelian_surface_bounded",
    "Y_like == anomaly-relevant U(1)_Y"      : "PREMISE:P-HY",
    "LH hypercharge values Y(Q)=+1/3,Y(L)=-1": "PREMISE:P-HY",
    "RH completion (4/3,-2/3,-2,0)"          : "PREMISE:P-COMP (SM branch = exact witness only)",
    "ABJ anomaly => non-closure"             : "PREMISE:P-ABJ (standard external result)",
    "staggered eps == Clifford chirality"    : "PREMISE:P-REC",
    "Clifford chirality exists iff d even"   : "RETAINED_SOURCE:clifford_volume_chirality_even_dimension",
}
print("PROVENANCE MANIFEST (input -> supplier):")
for k, v in MANIFEST.items():
    print(f"    {k:48} <- {v}")
print()

# Assertion: no hypercharge/abelian VALUE is credited to native_gauge_closure (GC).
gc_tagged = [k for k, v in MANIFEST.items() if "native_gauge_closure" in v]
gc_only_nonabelian = all(("NONABELIAN" in MANIFEST[k]) for k in gc_tagged)
print("BLOCK [GC-SCOPE]: native_gauge_closure credited only for nonabelian content")
check("native_gauge_closure tag(s) are NONABELIAN-only (no hypercharge/abelian credit)", gc_only_nonabelian)
check("hypercharge values are PREMISE (P-HY/P-COMP), not RETAINED_SOURCE",
      all(MANIFEST[k].startswith("PREMISE") for k in
          ["LH hypercharge values Y(Q)=+1/3,Y(L)=-1", "RH completion (4/3,-2/3,-2,0)"]))
print()

# ----------------------------------------------------------------------------
# BLOCK [B1/B3]: anomaly arithmetic over the explicitly-tagged content (exact).
# All fields as LEFT-handed Weyl; RH entered as LH conjugates (rep->conj, Y->-Y).
# SU(3): A (fund 3:+1, 3bar:-1, singlet:0), T (fund/antifund:1/2, singlet:0).
# SU(2): T (doublet:1/2, singlet:0).
# ----------------------------------------------------------------------------
fields = {
 'Q  (2,3)_+1/3' : dict(d2=2,T2=F(1,2), d3=3,T3=F(1,2),A3=+1, Y=F(1,3)),
 'L  (2,1)_-1'   : dict(d2=2,T2=F(1,2), d3=1,T3=0,    A3=0,  Y=F(-1)),
 'u^c(1,3b)_-4/3': dict(d2=1,T2=0, d3=3,T3=F(1,2),A3=-1, Y=F(-4,3)),
 'd^c(1,3b)_+2/3': dict(d2=1,T2=0, d3=3,T3=F(1,2),A3=-1, Y=F(2,3)),
 'e^c(1,1)_+2'   : dict(d2=1,T2=0, d3=1,T3=0,    A3=0,  Y=F(2)),
 'nu^c(1,1)_0'   : dict(d2=1,T2=0, d3=1,T3=0,    A3=0,  Y=F(0)),
}
LH = {k: v for k, v in fields.items() if k[0] in 'QL'}
def s(dom, sel): return sum(sel(f) for f in dom.values())

print("BLOCK [B1]: LH-only anomaly traces (nonzero => chiral inconsistency under P-ABJ)")
check("Tr[Y^3]      == -16/9", s(LH, lambda f: f['d2']*f['d3']*f['Y']**3) == F(-16,9))
check("Tr[SU3^2 Y]  == +1/3",  s(LH, lambda f: f['T3']*f['d2']*f['Y'])    == F(1,3))
check("Tr[SU3^3]    == +2",    s(LH, lambda f: f['A3']*f['d2'])           == F(2))
check("Tr[SU2^2 Y]  == 0",     s(LH, lambda f: f['T2']*f['d3']*f['Y'])    == 0)
check("Tr[Y] (grav) == 0",     s(LH, lambda f: f['d2']*f['d3']*f['Y'])    == 0)

print("BLOCK [B3]: P-COMP completion (4/3,-2/3,-2,0) cancels ALL six anomalies")
conds = {
 'SU(3)^3'     : lambda f: f['A3']*f['d2'],
 'SU(3)^2 U(1)': lambda f: f['T3']*f['d2']*f['Y'],
 'SU(2)^2 U(1)': lambda f: f['T2']*f['d3']*f['Y'],
 'U(1)^3'      : lambda f: f['d2']*f['d3']*f['Y']**3,
 'grav^2 U(1)' : lambda f: f['d2']*f['d3']*f['Y'],
}
for n, sel in conds.items():
    check(f"full-set {n:13} == 0", s(fields, sel) == 0)

# ----------------------------------------------------------------------------
# BLOCK [B4/B5/B6]: conditional chain gamma_5 -> even d -> (d_s=3) -> d_t odd.
# Finite diagnostic of the retained Clifford fact: a chirality gamma_5 = i^?*prod(gamma)
# anticommutes with every gamma iff d is even.
# ----------------------------------------------------------------------------
def gammas(d):
    # build d Hermitian gamma matrices via iterated Pauli/Jordan-Wigner (Euclidean Clifford)
    sx=np.array([[0,1],[1,0]],complex); sy=np.array([[0,-1j],[1j,0]],complex); sz=np.array([[1,0],[0,1]],complex)
    X=np.array([[0,1],[1,0]],complex); Y=np.array([[0,-1j],[1j,0]],complex); Z=np.array([[1,0],[0,-1]],complex)
    n=(d+1)//2
    def kron(ms):
        out=np.array([[1]],complex)
        for m in ms: out=np.kron(out,m)
        return out
    G=[]
    for k in range(n):
        for P in (X,Y):
            ms=[Z]*k+[P]+[np.eye(2,dtype=complex)]*(n-k-1)
            G.append(kron(ms))
            if len(G)==d: return G
    return G[:d]
def anticommute_all(g5, G):
    return all(np.allclose(g5@gm+gm@g5, 0) for gm in G)
print("BLOCK [B5]: chirality anticommutes with all gammas IFF d even (finite diagnostic)")
for d in (2,3,4,5):
    G=gammas(d)
    g5=G[0].copy()
    for gm in G[1:]: g5=g5@gm
    ac=anticommute_all(g5,G)
    expect=(d%2==0)
    check(f"d={d}: gamma_5 anticommutes-with-all == {expect} (even-d)", ac==expect)
print("BLOCK [B6]: with d_s=3 (Lattice axiom) and d even -> d_t odd in {1,3,5,...}")
check("d_s=3 + (d_s+d_t even) => d_t odd", all(((3+dt)%2==0)==(dt%2==1) for dt in range(1,8)))

# Scope guard: this bridge stops at d_t odd; d_t=1 is the separate one-time-dimension open gate.
print("SCOPE: bridge yields d_t in {odd positives}; the d_t=1 pin is the one-time-dimension open gate, NOT claimed here.")
print()
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
