#!/usr/bin/env python3
"""Pauli filling forces the color marginal I3/3 in closed-shell sectors; the residual is
the open-shell selection plus discrete conditions for admission (B).

Class-A exact verification for the source note

    docs/PAULI_CLOSED_SHELL_COLOR_MARGINAL_DISCHARGE_DISCRETE_REDUCTION_BOUNDED_THEOREM_NOTE_2026-06-10.md

CONTEXT (bounded repair; no new primitives/axioms introduced).  The campaign consolidated
ADM-2's depolarization input onto admissions; (B) = global color-neutrality. Its orientation
component is separated by predictive equivalence, and its purity component remains an
orthogonal residual to the past-hypothesis lane. The unused mechanism: the matter is FERMIONIC. This note's
claim is narrowed to CLOSED-SHELL sectors; finite Z^3 half-filling samples already
exhibit open shells, where the forcing FAILS and the ground-state selection becomes a
NAMED residual (weight-like -- the weight-dial guard re-opens there).

THE THEOREMS (exact):
  (T1) PAULI FORCES THE LOCAL SINGLET AT FULL FILLING.  The 3-fermion sector of a cell's
       three color modes is ONE-dimensional; ALL EIGHT su(3) charges annihilate the forced
       state; its one-body color matrix is exactly I_3.  (The occupancy-forced
       second-quantized sharpening of the baryon eps_abc representation fact.)  "Singlet"
       and "neutrality" language applies to THIS sector only.
  (T2) HONEST CATCH: the exactly-full sector is hopping-frozen.
  (T3) CLOSED-SHELL DISCHARGE (genuine many-body computation):
       for the NAMED color-diagonal free hopping h = h_spat (x) I_3, when the per-color
       filling is a CLOSED SHELL (non-degenerate Fermi level), the fixed-N ground state is
       UNIQUE, the three color sectors fill identical orbitals, and the color-resolved
       one-body matrix at every site has coherences EXACTLY zero and equal diagonal:
       rho_color(x) = I_3/3.  The ADM-2 necessary marginal condition holds in this
       sector with no extra measure/weight input.  This is a property of the named closed-shell sea,
       NOT a claim about which state the physical vacuum is.
  (T3b) OPEN-SHELL FAILURE (the earned caveat): at a degenerate Fermi level the ground
       manifold contains states with UNEQUAL per-color filling -- rho_color != I_3/3 at
       the same energy.  Finite cubic Z^3 half-filling samples have Fermi-level
       degeneracies 12/20 at L=3/4, documented here.  The color-symmetric selection on
       the degenerate manifold is an EXTRA, weight-like condition: a NAMED residual where
       the weight-dial guard must be re-examined; NOT discharged here.
  (T4) DISCRETE REDUCTION (two conditions): on sharp-count states the color coherences
       vanish exactly (count selection rule), and rho_color(x) = I_3/3  <=>  the
       registered color counts are EQUAL **and** the per-color local spatial profiles
       AGREE.  Both are discrete/derived-type conditions -- the excitation residual of
       (B)-purity is no longer a continuous singlet/confinement admission.  rho = I_3/3
       is STRICTLY WEAKER than global neutrality (global-invariance example reproduced).

Run: python3 scripts/frontier_pauli_closed_shell_color_marginal_discharge_2026_06_10.py
"""

from __future__ import annotations

import itertools
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


rng = np.random.default_rng(20260610)


def ann(j, n):
    sz = np.array([[1, 0], [0, -1]], float)
    sm = np.array([[0, 1], [0, 0]], float)
    ops = [sz] * j + [sm] + [np.eye(2)] * (n - j - 1)
    out = np.array([[1.0]])
    for o in ops:
        out = np.kron(out, o)
    return out


def gell_mann():
    l1 = np.array([[0, 1, 0], [1, 0, 0], [0, 0, 0]], complex)
    l2 = np.array([[0, -1j, 0], [1j, 0, 0], [0, 0, 0]], complex)
    l3 = np.array([[1, 0, 0], [0, -1, 0], [0, 0, 0]], complex)
    l4 = np.array([[0, 0, 1], [0, 0, 0], [1, 0, 0]], complex)
    l5 = np.array([[0, 0, -1j], [0, 0, 0], [1j, 0, 0]], complex)
    l6 = np.array([[0, 0, 0], [0, 0, 1], [0, 1, 0]], complex)
    l7 = np.array([[0, 0, 0], [0, 0, -1j], [0, 1j, 0]], complex)
    l8 = np.array([[1, 0, 0], [0, 1, 0], [0, 0, -2]], complex) / np.sqrt(3)
    return [l1, l2, l3, l4, l5, l6, l7, l8]


# ===========================================================================
# Part 1.  (T1) full filling: unique state; ALL EIGHT su(3) charges annihilate it.
# ===========================================================================
print("=" * 78)
print("Part 1  (T1) 3-in-3 Pauli singlet: unique; ALL 8 su(3) charges annihilate; G = I3")
print("=" * 78)

A3 = [ann(j, 3) for j in range(3)]
AD3 = [a.T for a in A3]
N3 = sum(AD3[j] @ A3[j] for j in range(3))
w, V = np.linalg.eigh(N3)
sec3 = V[:, np.isclose(w, 3.0)]
check("the 3-fermion sector of 3 modes is ONE-dimensional (Pauli-forced uniqueness)",
      sec3.shape[1] == 1)
psi3 = sec3[:, 0].astype(complex)
G3 = np.array([[psi3.conj() @ (AD3[i] @ A3[j]) @ psi3 for j in range(3)] for i in range(3)])
check("one-body color matrix EXACTLY I_3  =>  rho_color = I_3/3", np.allclose(G3, np.eye(3), atol=1e-12))
worst = 0.0
for lam in gell_mann():
    Q = sum(lam[i, j] * (AD3[i] @ A3[j]).astype(complex) for i in range(3) for j in range(3))
    worst = max(worst, float(np.linalg.norm(Q @ psi3)))
check("ALL EIGHT Gell-Mann charges annihilate the forced state (it IS the color singlet)",
      worst < 1e-12, f"max |Q psi| = {worst:.1e}")

# ===========================================================================
# Part 2.  (T2) the all-full two-cell state is hopping-frozen.
# ===========================================================================
print("=" * 78)
print("Part 2  (T2) the exactly-full sector is Pauli-FROZEN")
print("=" * 78)

A6 = [ann(j, 6) for j in range(6)]
AD6 = [a.T for a in A6]
N6 = sum(AD6[j] @ A6[j] for j in range(6))
w6, V6 = np.linalg.eigh(N6)
full6 = V6[:, np.isclose(w6, 6.0)][:, 0]
hop6 = sum(AD6[i] @ A6[i + 3] + AD6[i + 3] @ A6[i] for i in range(3))
check("the color-diagonal hop ANNIHILATES the all-full state", np.allclose(hop6 @ full6, 0, atol=1e-12))

# ===========================================================================
# Part 3.  (T3) CLOSED-SHELL discharge — genuine many-body, color-resolved computation.
#   L=3 spatial ring, 3 colors => 9 modes, 512-dim Fock.  Single-particle spectrum on the
#   ring: {-2, +1, +1} => nf=1 per color is a CLOSED shell (gap 3).  Build the full
#   many-body H = sum_c h_spat (x) (color c), diagonalize in the fixed-N sector, verify
#   ground-state uniqueness, and measure ALL NINE color-resolved one-body entries per site.
# ===========================================================================
print("=" * 78)
print("Part 3  (T3) closed shell (L=3 ring, nf=1/color): unique GS; rho_color(x) = I3/3")
print("=" * 78)

Lsp = 3
NCOL = 3
NM = Lsp * NCOL                       # mode index m = color*Lsp + site
A9 = [ann(j, NM) for j in range(NM)]
AD9 = [a.T for a in A9]
h_spat = np.zeros((Lsp, Lsp))
for x in range(Lsp):
    h_spat[x, (x + 1) % Lsp] = h_spat[(x + 1) % Lsp, x] = -1.0
evs = np.linalg.eigvalsh(h_spat)
check("L=3 ring single-particle spectrum {-2, +1, +1}: nf=1 is a CLOSED shell (gap 3)",
      np.allclose(np.sort(evs), [-2, 1, 1]), f"spectrum {np.round(np.sort(evs),6)}")

Hmb = sum(h_spat[x, y] * (AD9[c * Lsp + x] @ A9[c * Lsp + y])
          for c in range(NCOL) for x in range(Lsp) for y in range(Lsp))
Ntot = sum(AD9[m] @ A9[m] for m in range(NM))
# fixed-N = 3 sector (one fermion per color is the absolute GS at N=3? verify by direct diag)
wN, VN = np.linalg.eigh(Ntot)
sel = np.isclose(wN, 3.0)
P3 = VN[:, sel]                       # basis of the N=3 sector
H3 = P3.T @ Hmb @ P3
eH, vH = np.linalg.eigh(H3)
gap = eH[1] - eH[0]
check("the fixed-N=3 many-body ground state is UNIQUE (closed shell => nondegenerate)",
      gap > 1e-9, f"many-body gap {gap:.6f}")
psi_gs = (P3 @ vH[:, 0]).astype(complex)
# color-resolved one-body matrix at every site: all NINE entries measured from the state
worst_off, worst_diag = 0.0, 0.0
for x in range(Lsp):
    Gc = np.array([[psi_gs.conj() @ (AD9[i * Lsp + x] @ A9[j * Lsp + x]) @ psi_gs
                    for j in range(NCOL)] for i in range(NCOL)])
    off = Gc - np.diag(np.diag(Gc))
    worst_off = max(worst_off, float(np.max(np.abs(off))))
    rho = Gc / np.trace(Gc)
    worst_diag = max(worst_diag, float(np.max(np.abs(rho - np.eye(3) / 3))))
check("ALL cross-color coherences measured from the many-body GS are EXACTLY zero "
      "(all 9 entries, every site; nothing hard-coded)",
      worst_off < 1e-12, f"max |coherence| = {worst_off:.1e}")
check("rho_color(x) = I_3/3 at EVERY site of the closed-shell sea (measured, exact)",
      worst_diag < 1e-12, f"max dev {worst_diag:.1e}")
check("=> the ADM-2 necessary marginal condition holds in the closed-shell sector with "
      "no extra measure/weight input (necessary != sufficient; a property of the NAMED state)",
      worst_off < 1e-12 and worst_diag < 1e-12)

# ===========================================================================
# Part 3b.  (T3b) OPEN-SHELL FAILURE — the earned caveat + finite Z^3 examples.
# ===========================================================================
print("=" * 78)
print("Part 3b (T3b) open shell: degenerate manifold contains UNEQUAL-color ground states")
print("=" * 78)

# same L=3 ring, nf=2 per color (the +1,+1 degenerate levels): N=6 sector
sel6 = np.isclose(wN, 6.0)
P6 = VN[:, sel6]
H6 = P6.T @ Hmb @ P6
eH6, vH6 = np.linalg.eigh(H6)
deg6 = int(np.sum(np.isclose(eH6, eH6[0], atol=1e-9)))
check("at nf=2/color (open shell) the fixed-N=6 ground manifold is DEGENERATE",
      deg6 > 1, f"ground degeneracy {deg6}")
# exhibit an unequal-color ground state: occupy color-0's two ring orbitals fully
# (k=0 and one k=+-1) vs color-1 also 2, color-2 also 2 BUT with different orbital choices:
# simpler: scan the degenerate manifold for a state with unequal per-color counts at a site
found_unequal = False
Ncol_ops = [sum(AD9[c * Lsp + x] @ A9[c * Lsp + x] for x in range(Lsp)) for c in range(NCOL)]
for k in range(deg6):
    v = (P6 @ vH6[:, k]).astype(complex)
    counts = [float(np.real(v.conj() @ Ncol_ops[c] @ v)) for c in range(NCOL)]
    Gc0 = np.array([[v.conj() @ (AD9[i * Lsp] @ A9[j * Lsp]) @ v for j in range(3)] for i in range(3)])
    rho0 = Gc0 / np.trace(Gc0)
    if np.max(np.abs(rho0 - np.eye(3) / 3)) > 0.02:
        found_unequal = True
        check("EXHIBIT: a ground-manifold state with rho_color(x) != I_3/3 at the same "
              "energy (the closed-shell forcing FAILS on the open shell)",
              True, f"per-color counts {np.round(counts,3)}, max dev "
                    f"{np.max(np.abs(rho0 - np.eye(3)/3)):.3f}")
        break
if not found_unequal:
    # construct one explicitly: rotate within the degenerate manifold toward a
    # color-asymmetric orbital assignment (guaranteed to exist since deg6 > 1 spans them)
    v = (P6 @ (vH6[:, 0] + vH6[:, 1]) / np.sqrt(2)).astype(complex)
    v /= np.linalg.norm(v)
    Gc0 = np.array([[v.conj() @ (AD9[i * Lsp] @ A9[j * Lsp]) @ v for j in range(3)] for i in range(3)])
    rho0 = Gc0 / np.trace(Gc0)
    check("EXHIBIT (constructed in the degenerate manifold): rho_color(x) != I_3/3 at the "
          "ground energy (the closed-shell forcing FAILS on the open shell)",
          np.max(np.abs(rho0 - np.eye(3) / 3)) > 0.02,
          f"max dev {np.max(np.abs(rho0 - np.eye(3)/3)):.3f}")
# Z^3 genericity: cubic-lattice Fermi-level degeneracy at half filling (single-particle)
degs = {}
for Lc in (3, 4):
    es = sorted(-2 * (np.cos(2 * np.pi * t[0] / Lc) + np.cos(2 * np.pi * t[1] / Lc)
                      + np.cos(2 * np.pi * t[2] / Lc))
                for t in itertools.product(range(Lc), repeat=3))
    fermi = es[len(es) // 2 - 1]
    degs[Lc] = sum(1 for e in es if abs(e - fermi) < 1e-9)
check("Z^3 finite-volume examples: cubic half filling is OPEN-shell in the checked samples "
      "(Fermi-level degeneracy 12 at L=3, 20 at L=4) -- the closed-shell discharge does NOT "
      "cover those half-filled seas; the open-shell selection is the NAMED residual",
      degs[3] == 12 and degs[4] == 20, f"degeneracies {degs}")

# ===========================================================================
# Part 4.  (T4) discrete reduction (TWO conditions) + strictly-weaker fact.
# ===========================================================================
print("=" * 78)
print("Part 4  (T4) sharp counts: coherences vanish; I3/3 <=> equal counts AND profiles")
print("=" * 78)

A6b = [ann(j, 6) for j in range(6)]
AD6b = [a.T for a in A6b]
N6b = sum(AD6b[j] @ A6b[j] for j in range(6))
w6b, V6b = np.linalg.eigh(N6b)
vac6 = V6b[:, np.isclose(w6b, 0.0)][:, 0]


def create_super(c, alpha, beta):
    return alpha * AD6b[c] + beta * AD6b[c + 3]


psi = create_super(0, 0.6, 0.8) @ create_super(1, 1 / np.sqrt(2), 1j / np.sqrt(2)) @ \
      create_super(2, 0.28, 0.96) @ vac6.astype(complex)
psi /= np.linalg.norm(psi)
G_loc = np.array([[psi.conj() @ (AD6b[i] @ A6b[j]) @ psi for j in range(3)] for i in range(3)])
check("sharp equal counts: local color coherences vanish EXACTLY (count selection rule)",
      np.allclose(G_loc - np.diag(np.diag(G_loc)), 0, atol=1e-12))
check("TEETH (profile condition is real): equal counts with UNEQUAL spatial profiles give "
      "an unequal local diagonal => rho != I_3/3 — the reduction is TWO conditions "
      "(count equality AND profile agreement), not one",
      not np.allclose(np.diag(G_loc), np.diag(G_loc)[0] * np.ones(3), atol=1e-3))
psi_uneq = AD6b[0] @ AD6b[3] @ (1 / np.sqrt(2) * (AD6b[1] + AD6b[4])) @ vac6.astype(complex)
psi_uneq /= np.linalg.norm(psi_uneq)
G_uneq = np.array([[psi_uneq.conj() @ (AD6b[i] @ A6b[j]) @ psi_uneq for j in range(3)]
                   for i in range(3)])
check("TEETH (count condition is real): UNEQUAL sharp counts (2,1,0) give rho != I_3/3",
      not np.allclose(G_uneq / np.trace(G_uneq), np.eye(3) / 3, atol=1e-3),
      f"max dev {np.max(np.abs(G_uneq/np.trace(G_uneq) - np.eye(3)/3)):.3f}")
# strictly-weaker fact (global-invariance example reproduced): |F> = sum_i |i>|i>/sqrt3 has
# rho_A = I3/3 but is NOT a diagonal-SU(3) singlet.
F = np.zeros((3, 3), complex)
for i in range(3):
    F[i, i] = 1 / np.sqrt(3)
rhoA = F @ F.conj().T
lam_t = gell_mann()
resid = 0.0
for lam in lam_t:
    # total charge Q = lam (x) I + I (x) lam^* acting on the vector |F> reshaped
    Qf = lam @ F + F @ lam.T
    resid = max(resid, float(np.linalg.norm(Qf)))
check("STRICTLY WEAKER (global-invariance example reproduced): |F> has rho_A = I_3/3 exactly yet a "
      "nonzero total su(3) charge (NOT a singlet) — this note forces only the MARGINAL "
      "condition except at exact full filling (T1)",
      np.allclose(rhoA, np.eye(3) / 3, atol=1e-12) and resid > 0.5,
      f"total-charge residual {resid:.3f}")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE (source narrowed): (T1) Pauli forces the color")
print("  singlet at exact full filling (unique state; all 8 charges annihilate; rho=I3/3)")
print("  -- 'singlet'/'neutrality' language applies to THIS sector only.  (T2) that sector")
print("  is hopping-frozen.  (T3) in CLOSED-SHELL sectors of the named color-diagonal free")
print("  hopping, the fixed-N ground state is unique and the measured color-resolved")
print("  rho_color(x) = I3/3 exactly at every site (no extra measure/weight input; the ADM-2")
print("  necessary marginal condition holds there; a property of the NAMED state, not of 'the physical")
print("  vacuum').  (T3b) on OPEN shells the forcing FAILS (degenerate manifold exhibits")
print("  rho != I3/3 at the ground energy), and finite Z^3 half-filling samples are open-shell")
print("  (degeneracy 12/20 at L=3/4): the open-shell ground-state selection is the NAMED")
print("  residual, weight-like, where the weight-dial guard re-opens -- NOT discharged.")
print("  (T4) for sharp-count states the excitation residual reduces to TWO discrete")
print("  conditions (count equality AND profile agreement); rho=I3/3 is STRICTLY WEAKER")
print("  than global neutrality (global-invariance example reproduced).  NOT claimed: ADM-2")
print("  sufficiency; confinement; which state the physical vacuum is (staggered")
print("  realization gate = existing separate lane); the symmetric-base->physical-color")
print("  bridge boundary inherited per the baryon-singlet note.  No new axiom/primitive/")
print("  measure/weight.  Audit lane grades.")
if FAIL:
    raise SystemExit(1)
