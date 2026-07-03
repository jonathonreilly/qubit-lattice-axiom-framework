#!/usr/bin/env python3
"""ST1 and ST2 sit at the SAME wall: one undelivered continuous-time gauge-link dynamics.

Class-A finite-dimensional verification for the source note

    docs/ST1_ST2_SAME_WALL_GAUGE_DYNAMICS_RESIDUAL_CONVERGENCE_NARROW_THEOREM_NOTE_2026-06-08.md

HONEST CAPSTONE of the ADM-1/ADM-2 investigation (corrects this session's over-reaches).
A red-team panel refuted the claim that ST2's ADM-2 is "discharged / ahead of ST1's ADM-1".
This runner records what genuinely survives and the corrected structural finding.

THE ONE GENUINE BRICK (survives, exact, anchored on the retained global SU(3) commutant):
  the color-equivariance of the gauge-link force is FREE -- given ANY internal-symmetric
  coupling, the force F(U,M)=su(3)-part(U M^dag) satisfies F(gUg^dag,gMg^dag)=g F g^dag.

WHAT DOES NOT SURVIVE (the over-reaches, each demonstrated false here):
  (X1) "equivariance discharges ADM-2' (the gauge dynamics is equivariant)": equivariance is
       VACUOUS as a delivery of dynamics -- the identity holds for the gradient force, its
       NEGATION (reversed arrow), a non-gradient commutator flow, AND F=0 (no dynamics). So it
       selects/signs/rates NO generator.
  (X2) "ADM-2' is strictly WEAKER than ADM-1 (global subset local)": a CATEGORY ERROR. Global
       equivariance is automatic for any internal-symmetric coupling; the LOCAL covariance a
       gauge dynamics needs is bi-fundamental (g_x != g_y), which the force does NOT satisfy by
       a global adjoint. A static symmetry constraint (ADM-1) is not rankable vs dynamical
       generator premises toward closure.
  (X3) "annealed centrality supplies the CLT premise": the ensemble twirl over global g gives
       first-moment centrality (Schur depolarizing -- automatic from the retained global
       symmetry), NOT a central per-step KERNEL; the interacting per-step is non-central and
       the increments are CORRELATED, so the #3346 i.i.d.-central CLT is not supplied.

THE CORRECTED STRUCTURAL FINDING (the value):
  ST2's action-form residual = (equivariance: free) + R1 (a continuous-time action-gradient
  gauge-link generator: unadmitted import candidate; the Lattice + Quantum + Record baseline
  does not supply it -- retained record_classical_semigroup_boundary + retained_no_go
  record_markov_generator_embeddability_boundary) + R2 (mixing/ergodicity giving
  i.i.d.-central steps: OPEN) + (H_cov-as-connection: currently conditional on ADM-1's
  local-frame-redundancy premise, PR #3332).  R1, R2, and ADM-1 collapse in this route map
  to ONE undelivered package: continuous-time gauge-link / color-einselection dynamics
  (generator + rate + local transporter reading + mixing regime).
  => ST1 and ST2 sit at the SAME wall in the current residual map.  ST2 RELOCATED/RELABELED
     ADM-1's open input; it did NOT weaken it.

No new axiom, primitive, or import is added.

Run: python3 scripts/frontier_st1_st2_same_wall_gauge_dynamics_residual_2026_06_08.py
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
NC = 3


def haar_su(n=NC):
    A = rng.normal(size=(n, n)) + 1j * rng.normal(size=(n, n))
    Q, R = np.linalg.qr(A)
    Q = Q @ np.diag(np.exp(1j * np.angle(np.diag(R))))
    return Q / np.linalg.det(Q) ** (1.0 / n)


def su_force(X, n=NC):
    A = (X - X.conj().T) / (2j)
    return A - np.trace(A).real / n * np.eye(n)


def nonscalar_dev(M):
    return float(np.max(np.abs(M - M[0, 0] * np.eye(M.shape[0]))))


def rand_M():
    return rng.normal(size=(NC, NC)) + 1j * rng.normal(size=(NC, NC))


# ===========================================================================
# Part 1.  THE BRICK (survives): the gauge-link force is global-SU(3)-EQUIVARIANT.
#   Anchored on the RETAINED global SU(3) commutant (graph_first_su3, cl3_color_automorphism).
# ===========================================================================
print("=" * 78)
print("Part 1  The genuine brick: color-equivariance of the gauge force is FREE")
print("=" * 78)


def grad_force(U, M):
    return su_force(U @ M.conj().T)


worst = 0.0
for _ in range(200):
    U, M, g = haar_su(), rand_M(), haar_su()
    worst = max(worst, float(np.max(np.abs(
        grad_force(g @ U @ g.conj().T, g @ M @ g.conj().T) - g @ grad_force(U, M) @ g.conj().T))))
check("gauge force F(U,M)=su(3)-part(U M^dag) is global-SU(3)-equivariant (200 cfgs)",
      worst < 1e-10, f"max dev {worst:.1e} -- free, given the retained global SU(3) commutant")

# ===========================================================================
# Part 2.  (X1) Equivariance is VACUOUS as a delivery of dynamics.
#   The SAME identity holds for: gradient F, -F (reversed arrow), a commutator flow, and F=0.
# ===========================================================================
print("=" * 78)
print("Part 2  (X1) Equivariance delivers NO dynamics: holds for grad, -grad, commutator, and 0")
print("=" * 78)


def neg_force(U, M):
    return -su_force(U @ M.conj().T)


def commutator_flow(U, M):
    return su_force(U @ M.conj().T - M.conj().T @ U)   # a different (non-gradient) equivariant flow


def zero_force(U, M):
    return np.zeros((NC, NC), dtype=complex)


for label, F in [("gradient force", grad_force), ("NEGATED force (reversed arrow)", neg_force),
                 ("non-gradient commutator flow", commutator_flow), ("F=0 (NO dynamics)", zero_force)]:
    w = 0.0
    for _ in range(50):
        U, M, g = haar_su(), rand_M(), haar_su()
        w = max(w, float(np.max(np.abs(F(g @ U @ g.conj().T, g @ M @ g.conj().T) - g @ F(U, M) @ g.conj().T))))
    check(f"equivariance identity holds for '{label}'", w < 1e-10, f"dev {w:.1e}")
print("   => equivariance is VACUOUS: selects/signs/rates NO generator (holds even for F=0) ->")
print("      does NOT discharge ADM-2' (needs an actual gauge-link dynamics package = R1).")

# ===========================================================================
# Part 3.  (X2) global != local: the force is NOT locally covariant (category error).
# ===========================================================================
print("=" * 78)
print("Part 3  (X2) global equivariance != local covariance: NOT rankable vs ADM-1")
print("=" * 78)

U, M = haar_su(), rand_M()
gx, gy = haar_su(), haar_su()
# local connection law: U -> gx U gy^dag, matter bilinear M -> gy M gx^dag
F_local = grad_force(gx @ U @ gy.conj().T, gy @ M @ gx.conj().T)
dev_gx = float(np.max(np.abs(F_local - gx @ grad_force(U, M) @ gx.conj().T)))
dev_gy = float(np.max(np.abs(F_local - gy @ grad_force(U, M) @ gy.conj().T)))
check("under a LOCAL law (g_x != g_y) the force is NOT a global adjoint g F g^dag "
      "(bi-fundamental) -- global equivariance is far weaker than local covariance",
      dev_gx > 0.3 and dev_gy > 0.3, f"dev vs g_x-conj {dev_gx:.2f}, vs g_y-conj {dev_gy:.2f}")
print("   => ranking ADM-1 (static symmetry) vs R1/R2 (dynamical premises) toward closure is a")
print("      CATEGORY ERROR (the session's repeated over-reach).")

# ===========================================================================
# Part 4.  (X3) ensemble twirl != i.i.d.-central CLT premise.
# ===========================================================================
print("=" * 78)
print("Part 4  (X3) annealed = Schur twirl (first moment), NOT a central per-step kernel")
print("=" * 78)

# A FIXED maximally-anisotropic step direction (a quenched per-step):
D = su_force(haar_su())                      # a fixed su(3) drift direction
eps = 0.3
def step_at(g):                              # one increment in the globally-rotated frame
    from scipy.linalg import expm
    return expm(1j * eps * (g @ D @ g.conj().T))
# Ensemble twirl over fresh global g -> first-moment central (Schur):
twirl = sum(step_at(haar_su()) for _ in range(4000)) / 4000
check("ensemble twirl over global g -> first-moment CENTRAL (Schur depolarizing) -- automatic "
      "from the retained global SU(3) symmetry",
      nonscalar_dev(twirl) < 0.02, f"twirl nonscalar-dev {nonscalar_dev(twirl):.3f}")
# But a FIXED per-step kernel is NON-central, and a co-evolving walk has CORRELATED increments:
fixed_step = step_at(np.eye(NC))
check("a FIXED per-step kernel is NON-central (the interacting per-step the CLT actually sees)",
      nonscalar_dev(fixed_step) > 0.1, f"per-step nonscalar-dev {nonscalar_dev(fixed_step):.3f}")
# correlated increments: a slowly-rotating background gives high lag-1 autocorrelation
bg = [np.eye(NC)]
for _ in range(400):
    from scipy.linalg import expm
    bg.append(expm(1j * 0.05 * su_force(rand_M())) @ bg[-1])   # slow drift => correlation
dirs = np.array([np.real(np.trace((b @ D @ b.conj().T) @ D)) for b in bg])
dirs = (dirs - dirs.mean())
autocorr1 = float(np.dot(dirs[:-1], dirs[1:]) / np.dot(dirs, dirs))
check("co-evolving background gives strongly CORRELATED increments (lag-1 autocorr >> 0) -- the "
      "#3346 i.i.d.-central CLT is NOT supplied (needs mixing/ergodicity = R2, open)",
      autocorr1 > 0.5, f"lag-1 autocorr {autocorr1:.2f}")

# ===========================================================================
# Part 5.  THE CONVERGED RESIDUAL: R1 + R2 + ADM-1 = ONE undelivered input.
# ===========================================================================
print("=" * 78)
print("Part 5  ST1 and ST2 sit at the SAME wall: one continuous-time gauge-link dynamics")
print("=" * 78)

print("   SURVIVES (free): color-equivariance of the gauge force (Part 1).")
print("   ST2 residual = (equivariance: free) + R1 (continuous-time action-gradient generator")
print("     on U: unadmitted import candidate; the Lattice + Quantum + Record baseline does")
print("     not supply it) + R2 (mixing/ergodicity -> i.i.d.-central steps: OPEN) +")
print("     (H_cov-as-connection: currently conditional on ADM-1, PR #3332).")
print("   R1, R2 and ADM-1 collapse in this route map to ONE undelivered package: continuous-")
print("     time gauge-link / color-einselection dynamics (generator + rate + local transporter")
print("     reading + mixing regime).  => ST1 and ST2 sit at the SAME wall.")
print("   ST2 RELOCATED/RELABELED ADM-1's open input; it did NOT weaken it.")
print("   (corrected finding: ST1 == ST2 wall; ST2 NOT ahead; only the equivariance brick is free.)")

# ===========================================================================
print("=" * 78)
print(f"TOTAL: PASS={PASS} FAIL={FAIL}")
print("=" * 78)
print("SCOPE: HONEST CAPSTONE of the ADM-1/ADM-2 investigation.  The ONE genuine brick: the")
print("  gauge force's color-equivariance is FREE (retained global SU(3) commutant).  It does")
print("  NOT discharge ADM-2' (equivariance is vacuous as dynamics -- holds even for F=0), is")
print("  NOT rankable vs ADM-1 (global != local, a category error), and the 'annealed' demo is")
print("  a Schur twirl, NOT the i.i.d.-central CLT premise (per-step non-central, increments")
print("  correlated).  CORRECTED FINDING: ST2's residual (R1 generator + R2 mixing) and ST1's")
print("  ADM-1 collapse in this route map to ONE undelivered continuous-time gauge-link/color-")
print("  einselection dynamics package -- ST1 and ST2 sit at the SAME wall here. No new axiom,")
print("  primitive, or import is added.")
if FAIL:
    raise SystemExit(1)
