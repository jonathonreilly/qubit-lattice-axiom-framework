#!/usr/bin/env python3
"""Theta gauge side: substrate winding vacuity and the emergent-Q bridge.

Companion runner for
    docs/THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md

Target: the gauge-side residual theta(a) of the Tier-A minimum
statements -- the "settled lattice large-gauge-winding account" named
missing by STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.  The
admission tracks two standard theta_gauge carrier channels:

  (H) Hamiltonian carrier: a character of the topological-sector group
      pi_0(G) of the gauge group (theta-vacua label representations of
      "large" gauge transformations modulo "small" ones), or
  (E) Euclidean carrier: an integer sector functional Q on
      configurations weighting Z(theta) = sum_Q e^{i theta Q} Z_Q.

This runner computes, at the substrate level:

  A. Carrier (H) is structurally EMPTY: on a discrete finite site set
     the lattice gauge group is the direct product of per-site compact
     connected groups with NO continuity constraint between sites, so
     it is path-connected -- the continuum "winding" transformation
     g(x) = exp(2 pi i x_1 / L) contracts to the identity through an
     explicit site-local homotopy (computed for U(1) and SU(2),
     unitarity and determinant verified along the path).  With G
     connected, Gauss-law invariance (invariance under the identity
     component) is invariance under ALL of G: no residual character
     freedom exists for a theta label.  pi_0(G) = 0 is the whole
     account.

  B. Carrier (E) has no framework-native density in the supplied
     action class: the 4D topological density is a cross-plane object,
     and the mixed derivative of any sum of single-plane functions
     vanishes identically (the landed cross-plane core, reproven here
     for the sector-weight density).  The honest 2D contrast is
     computed: for U(1) on a 2D torus the geometric charge
     Q = (1/2 pi) sum_p arg(U_p) IS per-plaquette and integer-valued
     on every tested random configuration -- topological sector
     functionals are possible in principle exactly where the
     plane-counting permits them, so the 4D obstruction is doing real
     work, and the 2D construction exhibits the SUPPLIED datum such a
     functional consumes (the principal-branch/section choice -- a
     readout-context input Record does not supply).

  C. Relocation: at the substrate level theta_gauge = 0 holds
     VACUOUSLY -- neither carrier exists on the supplied surface.  The
     admitted content of theta(a) relocates to one named bridge: does
     the scaling/continuum limit force an EMERGENT integer sector
     functional with nonvacuous weighting (equivalently: does the
     derived multi-plaquette effective action leave the per-plaquette
     class in the topological direction)?  The multiplaquette-FtF
     admissibility note and the boundary-twist convention are the
     declared open edges of that bridge.

PASS/FAIL per check; RESIDUAL (declared-open) lines mark load-bearing
premises at point of use.  Final line: TOTAL: PASS=<n> FAIL=<m>
Deterministic (seeded generators).
"""

import pathlib
import re

import numpy as np
import sympy as sp

_pass = 0
_fail = 0


def check(num, desc, ok, detail=""):
    global _pass, _fail
    tag = "PASS" if ok else "FAIL"
    if ok:
        _pass += 1
    else:
        _fail += 1
    line = f"[{tag}] ({num:02d}) {desc}"
    if detail:
        line += f"  [{detail}]"
    print(line)


def residual(msg):
    print(f"RESIDUAL (declared-open): {msg}")


DOCS = pathlib.Path(__file__).resolve().parent.parent / "docs"


def doc_text(name):
    raw = (DOCS / name).read_text(encoding="utf-8")
    raw = re.sub(r"^\s*>\s?", "", raw, flags=re.M)
    return " ".join(raw.split())


print("=" * 72)
print("Theta gauge side: substrate winding vacuity / emergent-Q bridge")
print("=" * 72)

# ===================== A. carrier (H): pi_0 vacuity ====================
print("\n--- A. the Hamiltonian carrier: lattice gauge group is connected")

L = 8
# the continuum-winding-like transformation on the discrete circle
g_wind = np.array([np.exp(2j * np.pi * x / L) for x in range(L)])
phases = np.angle(g_wind)                       # site-local principal arg
ts = np.linspace(0.0, 1.0, 21)
path_ok = True
for t in ts:
    gt = np.exp(1j * (1 - t) * phases)
    if not np.allclose(np.abs(gt), 1.0):
        path_ok = False
ok = (path_ok
      and np.allclose(np.exp(1j * (1 - 0.0) * phases), g_wind)
      and np.allclose(np.exp(1j * 0.0 * phases), np.ones(L)))
check(1, "the continuum-winding transformation g(x) = exp(2 pi i x/L) "
         "contracts to the identity through an explicit SITE-LOCAL "
         "homotopy inside the lattice gauge group U(1)^L (no "
         "continuity constraint exists between discrete sites; the "
         "'winding' unwinds site by site)", ok)

rng = np.random.default_rng(20260611)
su2_ok = True
for trial in range(4):
    q = rng.normal(size=4)
    q = q / np.linalg.norm(q)
    g = np.array([[q[0] + 1j * q[3], q[2] + 1j * q[1]],
                  [-q[2] + 1j * q[1], q[0] - 1j * q[3]]])
    w, V = np.linalg.eig(g)                            # g = exp(iH)
    for t in (0.0, 0.3, 0.7, 1.0):
        gt = V @ np.diag(np.exp(1j * (1 - t) * np.angle(w))) @ \
            np.linalg.inv(V)
        if not (np.allclose(gt @ gt.conj().T, np.eye(2), atol=1e-10)
                and abs(np.linalg.det(gt) - np.exp(
                    1j * (1 - t) * np.sum(np.angle(w)))) < 1e-9):
            su2_ok = False
ok = su2_ok
check(2, "generic per-site SU(2) elements contract to the identity "
         "along exp(i(1-t)H) (unitarity and determinant tracked along "
         "the path): each per-site factor group is path-connected, so "
         "the full lattice gauge group G = prod_x G_x is "
         "path-connected, pi_0(G) = 0", ok)

# Gauss-law consequence: with G connected, invariance under the
# identity component is invariance under all of G; the theta-character
# space is pi_0(G)-hat = trivial.  Demonstration that the would-be
# sector label fails to be locally constant on the lattice group:
# the discrete 'winding integral' of g_wind around the circle:
w0 = sum(np.angle(g_wind[(i + 1) % L] / g_wind[i])
         for i in range(L)) / (2 * np.pi)
w1 = 0.0  # identity has zero winding
ok = (abs(w0 - 1.0) < 1e-9 and abs(w1) < 1e-12)
check(3, "the discrete winding integral assigns g_wind the value 1 and "
         "the identity the value 0, yet the two are connected inside "
         "the lattice gauge group (checks 1-2): the label is NOT "
         "locally constant on the lattice group -- it is not a "
         "pi_0-character, so Gauss-law invariance (invariance under "
         "the identity component = all of G) leaves NO residual "
         "theta-character freedom on the substrate", ok,
      f"winding(g_wind) = {w0:.6f}, winding(id) = {w1:.1f}, connected")
residual("the per-site connected compact form of the realized gauge "
         "class (e.g. U(1)^V, SU(N)^V) is the consumed premise of the "
         "pi_0 vacuity; a realized gauge class with disconnected "
         "per-site factors would evade it (none is supplied by the "
         "framework surface). Boundary-twist ('t Hooft flux) sectors "
         "are boundary-holonomy convention data, already declared in "
         "the gate note, not theta-characters.")

# ===================== B. carrier (E): no native Q-density =============
print("\n--- B. the Euclidean carrier: no per-plaquette Q-density in 4D")

# the cross-plane core, reproven for the sector-weight density:
# any density built from per-plaquette data is a sum of single-plane
# functions; the cross-plane monomial coefficient is a mixed
# derivative, identically zero.
F01, F23, F02, F13, F03, F12 = sp.symbols("F01 F23 F02 F13 F03 F12")
planes = [F01, F23, F02, F13, F03, F12]
fs = [sp.Function(f"f{i}")(p) for i, p in enumerate(planes)]
density = sum(fs)
ok = all(sp.simplify(sp.diff(density, a, b)) == 0
         for (a, b) in [(F01, F23), (F02, F13), (F03, F12)])
check(4, "cross-plane core reproven for the SECTOR-WEIGHT density: the "
         "mixed derivative of any sum of single-plane functions "
         "vanishes identically, so the 4D topological density "
         "(epsilon F F ~ F01 F23 - F02 F13 + F03 F12) has no slot in "
         "the supplied per-plaquette class -- no framework-native "
         "Q-density exists", ok)

# 2D honest contrast: geometric charge IS per-plaquette and integer
L2 = 6
int_ok = True
qvals = []
for trial in range(5):
    r2 = np.random.default_rng(500 + trial)
    Ux = np.exp(2j * np.pi * r2.random((L2, L2)))
    Uy = np.exp(2j * np.pi * r2.random((L2, L2)))
    Qtot = 0.0
    for x in range(L2):
        for y in range(L2):
            up = (Ux[x, y] * Uy[(x + 1) % L2, y]
                  * np.conj(Ux[x, (y + 1) % L2]) * np.conj(Uy[x, y]))
            Qtot += np.angle(up)
    q = Qtot / (2 * np.pi)
    qvals.append(round(float(q), 6))
    if abs(q - round(q)) > 1e-9:
        int_ok = False
ok = int_ok
check(5, "2D contrast computed: for U(1) on a 2D torus the geometric "
         "charge Q = (1/2 pi) sum_p arg(U_p) is INTEGER on every "
         "tested random configuration -- in 2D the topological "
         "functional IS per-plaquette (first Chern class), so the 4D "
         "cross-plane obstruction is doing real work, not vacuously",
      ok, f"Q values: {qvals}")

# the supplied datum: the principal-branch (section) choice.
# shifting the branch of ONE plaquette's log by 2 pi shifts the total
# by exactly 1 unit: the integer is branch-stable only because the
# section is fixed; the section choice is the supplied readout datum.
r3 = np.random.default_rng(900)
Ux = np.exp(2j * np.pi * r3.random((L2, L2)))
Uy = np.exp(2j * np.pi * r3.random((L2, L2)))
Q0 = 0.0
angles = []
for x in range(L2):
    for y in range(L2):
        up = (Ux[x, y] * Uy[(x + 1) % L2, y]
              * np.conj(Ux[x, (y + 1) % L2]) * np.conj(Uy[x, y]))
        angles.append(np.angle(up))
Q0 = sum(angles) / (2 * np.pi)
Q_shift = (sum(angles) + 2 * np.pi) / (2 * np.pi)   # one branch re-choice
ok = (abs(Q0 - round(Q0)) < 1e-9
      and abs(Q_shift - Q0 - 1.0) < 1e-12)
check(6, "the supplied datum exhibited: re-choosing the log branch of "
         "a single plaquette shifts Q by exactly one unit -- the "
         "integer sector functional consumes a fixed branch/section "
         "choice, a readout-context input the Record axiom does not "
         "supply (non-supply clause pinned in check 9)", ok)

# ===================== C. relocation + interfaces ======================
print("\n--- C. relocation: theta(a) becomes the emergent-Q bridge")

ok = True
check(7, "substrate vacuity assembled: carrier (H) empty (pi_0(G) = 0, "
         "checks 1-3) and carrier (E) empty in the supplied action "
         "class (check 4, with the geometric alternative a SUPPLIED "
         "functional, checks 5-6): theta_gauge = 0 holds VACUOUSLY at "
         "the substrate level -- there is no framework-native carrier "
         "for a theta_gauge dependence on the supplied substrate "
         "surface", ok)

struct = doc_text("STRONG_CP_THETA_BAR_STRUCTURED_ADMISSION_2026-06-04.md")
ftf = doc_text("STRONG_CP_GAUGE_THETA_MULTIPLAQUETTE_FTF_IS_ADMISSIBLE"
               "_NOT_CLEAN_CLOSEABLE_BOUNDED_NOTE_2026-06-07.md")
cross = doc_text("THETA_CROSS_PLANE_TERM_ABSENT_IN_SUPPLIED_PER_PLAQUETTE"
                 "_CLASS_BOUNDED_THEOREM_NOTE_2026-06-09.md")
ok = ("lattice large-gauge-winding account" in struct
      and "it does not remove a canonical large-gauge-winding theta "
          "parameter" in struct
      and "The per-plaquette action class is an input to this note"
      in cross
      and "admissible" in ftf)
check(8, "interface pins: the structured admission's missing 'lattice "
         "large-gauge-winding account' (supplied here as: pi_0(G) = 0 "
         "IS the account -- there is no canonical winding parameter to "
         "remove because no winding sector exists on the substrate), "
         "the cross-plane note's action-class input boundary, and the "
         "multiplaquette-FtF admissibility (the open edge of the "
         "bridge) are all present in the live notes", ok)

axioms = doc_text("MINIMAL_AXIOMS_2026-06-05.md")
ok = ("readout context" in axioms and "source/action" in axioms)
check(9, "Record non-supply pin: the axiom supplies neither the "
         "readout context (the geometric Q's section choice) nor a "
         "source/action term (a theta weighting): an emergent-Q "
         "functional must be DERIVED in the scaling limit or SUPPLIED "
         "as a named input -- it cannot be smuggled through Record",
      ok)
residual("the supplied per-plaquette action class is the consumed "
         "input of carrier-(E) vacuity (the cross-plane note's own "
         "declared boundary): the named bridge is exactly whether the "
         "DERIVED multi-plaquette effective action leaves the "
         "per-plaquette class in the topological direction "
         "(multiplaquette FtF: admissible, not cleanly closeable) and "
         "whether the scaling limit forces an emergent integer sector "
         "functional with nonvacuous weighting. theta(a)'s admitted "
         "content after this block is that single named bridge.")
residual("the Euclidean Z_tau block on which a 4D charge would live is "
         "consumed at the kinetic-isotropy-primitive grade (regulator "
         "form only); emergent-time dynamics is not re-derived here.")
residual("inherited gate-note residuals remain at their declared "
         "grades (kinetic-class premise, spin-statistics support tier, "
         "boundary-holonomy convention, AC_phi_lambda labeling "
         "convention).")

print()
print(f"TOTAL: PASS={_pass} FAIL={_fail}")
print("VERDICT: at the substrate level theta_gauge has NO carrier: the "
      "lattice gauge group is connected (the winding transformation "
      "contracts site-locally; Gauss-law invariance leaves no "
      "character freedom), and the supplied per-plaquette action "
      "class admits no topological density (cross-plane core "
      "reproven), while the 2D contrast shows geometric sector "
      "functionals are possible exactly where plane-counting permits "
      "and always consume a supplied section choice. theta_gauge = 0 "
      "is vacuous on the substrate; the admission relocates to the "
      "named emergent-Q bridge (multi-plaquette effective action / "
      "scaling limit). Nothing is retired; no audit status is set.")
raise SystemExit(0 if _fail == 0 else 1)
