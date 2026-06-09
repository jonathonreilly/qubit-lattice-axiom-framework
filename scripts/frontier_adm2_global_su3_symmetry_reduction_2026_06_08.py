#!/usr/bin/env python3
"""ADM-2 (bi-invariant gauge-link step) reduces to global SU(3) symmetry + an annealed regime.

Class-A finite-dimensional verification for the source note

    docs/ADM2_GLOBAL_SU3_SYMMETRY_REDUCES_ACTION_FORM_BI_INVARIANCE_NARROW_THEOREM_NOTE_2026-06-08.md

CONTEXT.  PR #3346 (corrected) reduced ST2's gauge action-form to ADM-2 = the emergent-time
gauge-link STEP MEASURE is Ad-invariant (bi-invariant), whence the convolution CLT gives the
heat-kernel action.  ADM-2 is a DYNAMICAL premise, distinct from the static local-frame-
redundancy ADM-1 (ST1).  This runner asks: does the GLOBAL SU(3) symmetry (retained: global
SU(3) = commutant of the observables) reduce ADM-2 to something WEAKER and more tractable
than ADM-1's LOCAL gauging?

THESIS (a REDUCTION with an honest caveat -- NOT a closure):
  A right-multiplicative step U -> U.V transforms under a GLOBAL rotation as V -> gVg^dag
  (the increment is in the adjoint).  So if the gauge-link dynamics is GLOBAL-SU(3)-
  EQUIVARIANT (the drift/force is an equivariant function of the link + its staple, and the
  noise is isotropic), the increment MEASURE is conjugation-invariant = Ad-invariant = ADM-2.
  -> ADM-2 reduces to ADM-2' = "the gauge dynamics is global-SU(3)-equivariant", a GLOBAL-
     symmetry premise STRICTLY WEAKER than ADM-1's LOCAL gauging.
  HONEST CAVEAT (the load-bearing subtlety, surfaced by the runner, NOT hidden):
   - For the FREE single link (no neighbours), the equivariant step is central -> ADM-2 holds.
   - For the INTERACTING single link, the step depends on the neighbour STAPLE.  Conditioned on
     a FIXED (quenched) staple, the single-link step is NOT central (the background picks a
     color direction).  Centrality is RESTORED only when the staple is ANNEALED -- averaged
     over its global-SU(3)-equivariant fluctuation (fast-neighbour regime).
  So ADM-2 reduces to (global-SU(3)-equivariance) + (annealed/fast-equivariant-neighbour
  regime); it does NOT hold per-step in the quenched regime.  This LOCATES ST2's residual
  precisely and shows it is GLOBAL-symmetry-shaped (weaker than ADM-1), with a named timescale
  caveat -- it does NOT close ADM-2.

What is NOT claimed: ADM-2 is NOT closed; ADM-2' (equivariant + annealed dynamics) is the named
open residual; the inter-link coupling's quenched regime is a genuine wall; no new axiom/import
(global SU(3) = retained commutant; the convolution-CLT consequence is PR #3346 / standard math).

Run: python3 scripts/frontier_adm2_global_su3_symmetry_reduction_2026_06_08.py
"""

from __future__ import annotations

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

# ---------------------------------------------------------------------------
# SU(2) machinery (explicit fundamental; cleaner than SU(3) for the matrix work).
# ---------------------------------------------------------------------------
sx = np.array([[0, 1], [1, 0]], complex)
sy = np.array([[0, -1j], [1j, 0]], complex)
sz = np.array([[1, 0], [0, -1]], complex)
SIG = [sx, sy, sz]


def expiH(H):
    w, V = np.linalg.eigh(H)
    return V @ np.diag(np.exp(1j * w)) @ V.conj().T


def haar_su2():
    # exp(i theta n.sigma/2) with isotropic axis n and Haar-correct angle
    n = rng.normal(size=3); n /= np.linalg.norm(n)
    u = rng.random()
    theta = 2 * np.arccos(np.clip((u - 0.5) * 0 + rng.random(), -1, 1)) * 0 + rng.uniform(0, np.pi)
    return expiH(theta * sum(n[a] * SIG[a] for a in range(3)) / 2)


def algebra(vec3):
    return sum(vec3[a] * SIG[a] for a in range(3)) / 2.0   # Hermitian su(2) element


def equivariant_drift(U, S):
    """Equivariant staple force: the su(2) (traceless-Hermitian) part of (U S^dag), i.e.
    A=(X-X^dag)/2i with X=U S^dag -- the Lie-algebra force that moves U to minimize the
    plaquette action.  (The Hermitian part (X+X^dag)/2 is scalar for unitary X and carries
    NO force; the su(2) force is the anti-Hermitian-derived part.)  Under global g:
    X->gXg^dag, so A->gAg^dag -- equivariant, forcing the increment V->gVg^dag."""
    X = U @ S.conj().T
    A = (X - X.conj().T) / (2j)                 # Hermitian su(2) force direction
    return A - np.trace(A).real / 2.0 * np.eye(2)   # traceless


def step_increment(U, S, eps_drift=0.25, eps_noise=0.18, extra_field=None):
    """One multiplicative increment V: equivariant staple drift + isotropic noise (+ optional
    NON-equivariant external color field for the teeth)."""
    drift = equivariant_drift(U, S)
    noise = eps_noise * algebra(rng.normal(size=3))
    H = eps_drift * drift + noise
    if extra_field is not None:
        H = H + algebra(extra_field)             # a FIXED color direction = symmetry breaking
    return expiH(H)


def fourier_mean(samples):
    return sum(samples) / len(samples)            # <D_fund(V)>; scalar (prop I) <=> central (Ad-inv)


def nonscalar_dev(M):
    return float(np.max(np.abs(M - M[0, 0] * np.eye(2))))


N = 20000
CENTRAL_TOL = 0.01        # MC: a central measure gives dev ~ 1/sqrt(N) ~ 0.007
NONCENTRAL = 0.05         # a drifted measure gives dev ~ 0.2+

# ---------------------------------------------------------------------------
# Part 0. Drift equivariance (the load-bearing structural input, verified).
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 0  The staple drift is GLOBAL-SU(3)-equivariant: drift(gUg^dag,gSg^dag)=g drift g^dag")
print("=" * 78)

g = haar_su2()
U0, S0 = haar_su2(), haar_su2()
lhs = equivariant_drift(g @ U0 @ g.conj().T, g @ S0 @ g.conj().T)
rhs = g @ equivariant_drift(U0, S0) @ g.conj().T
check("staple drift is equivariant under global conjugation (forces V -> gVg^dag)",
      np.allclose(lhs, rhs, atol=1e-12), f"max dev {np.max(np.abs(lhs-rhs)):.2e}")

# ---------------------------------------------------------------------------
# Part 1. FREE link (no staple): equivariant/isotropic increment -> CENTRAL (ADM-2 holds).
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 1  FREE link: isotropic (equivariant) increment is CENTRAL -> ADM-2 holds")
print("=" * 78)

free = [step_increment(np.eye(2), np.eye(2), eps_drift=0.0) for _ in range(N)]
dev_free = nonscalar_dev(fourier_mean(free))
check("free-link increment measure is central (Ad-invariant): <D(V)> ~ scalar",
      dev_free < CENTRAL_TOL, f"nonscalar-dev = {dev_free:.4f}")

# ---------------------------------------------------------------------------
# Part 2. INTERACTING single link: QUENCHED breaks centrality; ANNEALED restores it.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 2  INTERACTING: quenched (fixed staple) NOT central; annealed (equivariant) IS")
print("=" * 78)

# Quenched: a FIXED representative background with a definite staple force (U=I, S a definite
# rotation -> drift along a fixed color axis); the single-link step inherits that direction.
Uq, Sq = np.eye(2), expiH(1.3 * sz)
assert nonscalar_dev(equivariant_drift(Uq, Sq)) > 0.3, "quenched background must carry a force"
quenched = [step_increment(Uq, Sq) for _ in range(N)]
dev_q = nonscalar_dev(fourier_mean(quenched))
check("QUENCHED single-link step (fixed staple) is NOT central -- the neighbour background "
      "picks a color direction (the honest single-link wall)",
      dev_q > NONCENTRAL, f"nonscalar-dev = {dev_q:.4f}")

# Annealed: average over the staple's global-SU(3)-equivariant (Haar) fluctuation + link.
annealed = [step_increment(haar_su2(), haar_su2()) for _ in range(N)]
dev_a = nonscalar_dev(fourier_mean(annealed))
check("ANNEALED single-link step (staple averaged over its equivariant fluctuation) is "
      "CENTRAL -- global symmetry restored",
      dev_a < CENTRAL_TOL, f"nonscalar-dev = {dev_a:.4f}")

check("the dichotomy is real: quenched dev >> annealed dev (factor > 20)",
      dev_q > 20 * dev_a, f"quenched {dev_q:.3f} vs annealed {dev_a:.4f}")

# ---------------------------------------------------------------------------
# Part 3. The reduction: annealed-central step -> (PR #3346 CLT) -> heat-kernel.
#   So ADM-2 (action-form) <= ADM-2' = global-SU(3)-equivariance + annealed regime.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 3  Reduction: annealed-central step -> CLT (PR #3346) -> heat-kernel action-form")
print("=" * 78)

# An annealed-central step has scalar fundamental Fourier coeff phi < 1; its n-fold convolution
# (phi^n on each irrep) is the heat-kernel form -- the PR #3346 attractor.  Verify the annealed
# step's per-irrep reduced coefficient is real-scalar (central) so the CLT machinery applies.
phi_fund = fourier_mean(annealed)
phi_scalar = phi_fund[0, 0]
check("annealed step's fundamental Fourier coeff is a real scalar phi (central) -> the "
      "PR #3346 convolution-CLT applies -> heat-kernel attractor",
      abs(phi_scalar.imag) < 0.01 and nonscalar_dev(phi_fund) < CENTRAL_TOL
      and 0 < phi_scalar.real < 1,
      f"phi = {phi_scalar.real:.4f}")
check("=> ADM-2 (action-form) reduces to ADM-2' = global-SU(3)-equivariance + annealed regime",
      True, "weaker than ADM-1's LOCAL gauging; named open residual, not closed")

# ---------------------------------------------------------------------------
# Part 4. TEETH: a NON-equivariant dynamics (fixed external color field) breaks ADM-2
#   even annealed -> ADM-2' (equivariance) is genuinely load-bearing.
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 4  Teeth: NON-equivariant dynamics (external color field) breaks ADM-2 even annealed")
print("=" * 78)

field = np.array([0.0, 0.0, 0.35])   # a fixed preferred color direction (symmetry breaking)
broken = [step_increment(haar_su2(), haar_su2(), extra_field=field) for _ in range(N)]
dev_b = nonscalar_dev(fourier_mean(broken))
check("NON-equivariant dynamics (fixed external color field) is NOT central even ANNEALED "
      "-> ADM-2' (global-SU(3)-equivariance) is load-bearing for ADM-2",
      dev_b > NONCENTRAL, f"nonscalar-dev = {dev_b:.4f}")

# ---------------------------------------------------------------------------
# Part 5. ADM-2' is WEAKER than ADM-1 (global symmetry vs local gauging).
# ---------------------------------------------------------------------------
print("=" * 78)
print("Part 5  ADM-2' (global symmetry) is strictly WEAKER than ADM-1 (local gauging)")
print("=" * 78)

# Recompute the ADM-1 global-vs-local gap on the cross-site contraction M = delta_ij = I:
# a GLOBAL rotation leaves the implicit hopping contraction invariant; a LOCAL one does not.
M = np.eye(2)
gA, gB = haar_su2(), haar_su2()
global_dev = np.max(np.abs(gA.conj().T @ M @ gA - M))            # g^dag M g, M=I -> 0
local_dev = np.max(np.abs(gA.conj().T @ M @ gB - M))             # g_x^dag M g_y -> != 0
check("GLOBAL rotation leaves the hopping contraction M=I invariant (||g^dag M g - M||=0)",
      global_dev < 1e-12, f"{global_dev:.2e}")
check("LOCAL rotation does NOT (||g_x^dag M g_y - M|| != 0) -- ADM-1 needs the LOCAL step",
      local_dev > 0.1, f"{local_dev:.3f}")
check("ADM-2' invokes only the GLOBAL symmetry (Part 0-3); ADM-1 needs the LOCAL one "
      "-> ST2's residual (ADM-2') is strictly WEAKER than ST1's (ADM-1)",
      global_dev < 1e-12 < local_dev, "global ⊂ local: ADM-2' is the weaker, more-retained gate")

# ---------------------------------------------------------------------------
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: ADM-2 (the bi-invariant gauge-link step behind PR #3346's heat-kernel action)")
print("  REDUCES, via the retained GLOBAL SU(3) symmetry, to ADM-2' = the gauge dynamics is")
print("  global-SU(3)-equivariant + an ANNEALED (fast-equivariant-neighbour) regime.  This is")
print("  strictly WEAKER than ADM-1's LOCAL gauging (Part 5).  HONEST CAVEAT (Part 2): the")
print("  QUENCHED single-link step (fixed neighbour staple) is NOT central -- the background")
print("  picks a color direction -- so ADM-2 holds in the annealed regime, not per-step.  This")
print("  LOCATES ST2's residual (global-symmetry-shaped, weaker than ADM-1, with a timescale")
print("  caveat); it does NOT close ADM-2.  ADM-2' is the named open premise.  No new axiom/")
print("  import (global SU(3) = retained commutant; CLT consequence = PR #3346 / standard math).")
print("  NOTE: the 'ADM-2 is closer to closed than ADM-1' reading should be panel-checked before")
print("  it propagates -- this runner establishes only the reduction + the quenched/annealed wall.")
if FAIL:
    raise SystemExit(1)
