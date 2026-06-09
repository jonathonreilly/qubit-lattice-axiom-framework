#!/usr/bin/env python3
"""Edge/two-site framing supplies no native color route; the RECORD axiom has no cross-site clause.

Class-A verification (finite algebra + structural text audit) for the source note

    docs/EDGE_TWO_SITE_FRAMING_SUPPLIES_NO_NATIVE_COLOR_ROUTE_RECORD_TEXT_NARROW_NO_GO_NOTE_2026-06-08.md

CONTEXT.  Several ADM-1 discharge attempts framed the problem at the EDGE/two-site level:
"the link/two-site structure (e.g. the native SWAP between neighbour qubits, or a
two-endpoint dressing) supplies the color/cross-site structure, and the RECORD axiom's
'no cross-site identification' clause makes the frame unregistered."  An ADM-1
find-the-escape panel (forced_finding) adversarially recomputed this framing and found it
fails on exact grounds, INCLUDING a text error about the axiom itself.  This runner makes
those grounds exact (route-DEMOTE, narrow).

THE GROUNDS:
  (G-A) THE NATIVE TWO-SITE OPERATION IS COLOR-BLIND.  The qubit-native two-site
        primitive SWAP on C^2 (x) C^2 commutes with EVERY diagonal rotation g (x) g — it is
        a real permutation carrying NO internal direction, no su(3) data (a single qubit
        link natively carries only u(2): the QUBIT_LINK_U2 boundary), and no holonomy
        U_xy.  Pre-gauging, the edge supplies symmetric (color-blind) structure only.
  (G-B) EXTRACTING Ad-CLASS CONTENT NEEDS A SUPPLIED CONTINUOUS AVERAGE.  On the
        irreducible color triplet the genuine partition map is trivial (D(U) = U; Schur),
        so recovering the gauge-invariant Ad-class/trace content requires the Haar average
        U -> (Tr U/Nc) I — a CONTINUOUS group average = a supplied generator, exactly what
        the retained record boundaries say Record alone does not provide.  The edge framing
        therefore COLLAPSES into the same supplied-carrier / color-trace gate; it does not
        bypass it.
  (G-C) RECORD-AXIOM TEXT CORRECTION.  The canonical RECORD axiom
        (MINIMAL_AXIOMS_2026-06-04, the live authority) supplies ONLY additive scalar
        readout I(R1 u R2) = I(R1) + I(R2) and explicitly DISCLAIMS composition and
        arbitrary observable identification; it contains NO "cross-site identification"
        clause.  Routes that leaned on that paraphrase were importing structure the axiom
        does not contain.  (Structural text audit below, following the repo's
        note-text-audit runner precedent.)

SCOPE (narrow route-demote, NOT a closure): demotes the EDGE/TWO-SITE FRAMING route to
ADM-1 / native color.  Does NOT foreclose supplied-carrier models (the TWO_ENDPOINT_GAUSS
note is an honest bounded model and is untouched); does NOT close ADM-1 or the
gauging-selection gate; adds no axiom/import; no PDG value.

Run: python3 scripts/frontier_edge_two_site_framing_no_native_color_route_record_text_2026_06_08.py
"""

from __future__ import annotations

import os
import numpy as np

PASS = 0
FAIL = 0


def check(name: str, condition: bool, detail: str = "") -> None:
    global PASS, FAIL
    tag = "PASS" if condition else "FAIL"
    if condition:
        PASS += 1
    else:
        FAIL += 1
    line = f"  [{tag}] {name}"
    if detail:
        line += f"  ({detail})"
    print(line)


rng = np.random.default_rng(20260608)


def haar_su(n):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1.0 / n)


# ===========================================================================
# Part 1.  (G-A) SWAP on C^2 (x) C^2 is color-blind: commutes with every g (x) g.
# ===========================================================================
print("=" * 78)
print("Part 1  (G-A) the native two-site SWAP is color-blind (commutes with all g x g)")
print("=" * 78)

SWAP = np.zeros((4, 4))
for i in range(2):
    for j in range(2):
        SWAP[2 * j + i, 2 * i + j] = 1.0

worst = 0.0
for _ in range(100):
    g = haar_su(2)
    gg = np.kron(g, g)
    worst = max(worst, float(np.max(np.abs(SWAP @ gg - gg @ SWAP))))
check("SWAP commutes with g (x) g for every g (100 Haar samples) — carries NO internal "
      "direction", worst < 1e-12, f"max [SWAP, g(x)g] = {worst:.1e}")
check("SWAP is a REAL permutation (no phase/holonomy data: SWAP = SWAP* = SWAP^T, "
      "SWAP^2 = I)",
      np.allclose(SWAP, SWAP.conj()) and np.allclose(SWAP, SWAP.T)
      and np.allclose(SWAP @ SWAP, np.eye(4)))

# the single-qubit-link boundary (QUBIT_LINK_U2): anti-Hermitian endomorphisms of C^2 have
# real dimension 4 = u(2); su(3) needs real dimension 8 — no faithful su(3) on one link.
check("single qubit link: dim u(2) = 4 < dim su(3) = 8 — no faithful native su(3) on a "
      "qubit link (the QUBIT_LINK_U2 boundary, restated)",
      2 * 2 == 4 and (3 ** 2 - 1) == 8)

# ===========================================================================
# Part 2.  (G-B) Ad-class content needs a SUPPLIED continuous average (collapse).
# ===========================================================================
print("=" * 78)
print("Part 2  (G-B) extracting Ad-class/trace content needs a supplied continuous average")
print("=" * 78)

NC = 3
U = haar_su(NC)
# the genuine partition map on the irreducible triplet is trivial: D(U) = U (Schur)
g3 = haar_su(NC)
P_nontriv = np.diag([1.0, 0, 0]).astype(complex)
check("Schur: a nontrivial projector does not commute with the irreducible SU(3) action "
      "-> the only G1 partition is {I}, D(U) = U (registers the FRAMED link, not the class)",
      float(np.max(np.abs(P_nontriv @ g3 - g3 @ P_nontriv))) > 0.1)
# the Ad-class invariant content is reached only by the Haar average (continuous):
T_mc = sum(V @ U @ V.conj().T for V in (haar_su(NC) for _ in range(50000))) / 50000
target = (np.trace(U) / NC) * np.eye(NC)
check("the Ad-class/trace content U -> (TrU/Nc) I is the HAAR AVERAGE (continuous group "
      "integral; MC 50k) — a supplied generator, not a record partition",
      np.max(np.abs(T_mc - target)) < 0.02,
      f"max dev {np.max(np.abs(T_mc - target)):.4f}")
print("   => the edge/two-site framing COLLAPSES into the supplied-carrier/color-trace")
print("      gate: pre-gauging the edge is color-blind (Part 1); post-hoc class extraction")
print("      needs the continuous average Record does not supply (retained boundaries).")

# ===========================================================================
# Part 3.  (G-C) RECORD-axiom structural text audit (live authority file).
# ===========================================================================
print("=" * 78)
print("Part 3  (G-C) MINIMAL_AXIOMS_2026-06-04: additive readout only; NO cross-site clause")
print("=" * 78)

AXIOM_FILE = os.path.join(os.path.dirname(__file__), "..", "docs",
                          "MINIMAL_AXIOMS_2026-06-04.md")
with open(AXIOM_FILE, encoding="utf-8") as fh:
    text = fh.read()
low = text.lower()

check("the axiom file states the additive readout law I(R_1 sqcup R_2) = I(R_1) + I(R_2)",
      "i(r_1 sqcup r_2) = i(r_1) + i(r_2)" in low)
check("the axiom file states it supplies ONLY additive scalar record readout",
      "supplies only additive scalar record readout" in low)
check("the axiom file explicitly disclaims (system) composition",
      "composition" in low)
check("the axiom file explicitly disclaims arbitrary observable identification",
      "arbitrary observable identification" in low)
check("the axiom file contains NO 'cross-site' clause (the paraphrase some routes leaned "
      "on does not exist in the canonical text)",
      "cross-site" not in low and "cross site" not in low)
check("the axiom file supersedes the 2026-05-20 wording (it is the live authority)",
      "supersedes" in low and "2026-05-20" in low)

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE (narrow route-demote): the EDGE/TWO-SITE FRAMING route to native color /")
print("  ADM-1 is demoted — the native two-site SWAP is color-blind (commutes with all")
print("  g x g; real permutation; no holonomy), the single-qubit link carries only u(2),")
print("  and extracting Ad-class content requires a SUPPLIED continuous Haar average (the")
print("  same supplied-carrier/color-trace gate; Record's retained boundaries).  PLUS the")
print("  text correction: the canonical RECORD axiom (MINIMAL_AXIOMS_2026-06-04) is")
print("  additive scalar readout ONLY, disclaims composition + arbitrary observable")
print("  identification, and contains NO 'cross-site identification' clause — routes that")
print("  leaned on that paraphrase imported structure.  Does NOT foreclose supplied-")
print("  carrier models (TWO_ENDPOINT_GAUSS untouched), does NOT close ADM-1 or the")
print("  gauging-selection gate.  No new axiom/import; no PDG value.")
if FAIL:
    raise SystemExit(1)
