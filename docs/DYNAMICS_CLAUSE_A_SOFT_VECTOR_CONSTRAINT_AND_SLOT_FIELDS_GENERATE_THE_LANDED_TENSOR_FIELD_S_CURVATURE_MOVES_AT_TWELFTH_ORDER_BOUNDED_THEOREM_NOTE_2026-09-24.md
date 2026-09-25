---
claim_id: dynamics_clause_a_soft_vector_constraint_and_slot_fields_generate_the_landed_tensor_field_s_curvature_moves_at_twelfth_order_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Supplied tensor stencil, U sum(Gv)^2 and unit slot shifts. A named planar displacement has exact order-twelve coefficient 111150053/31850496 from 2304 monotone partial states. Radius-two coefficient- and anchor-restricted searches are not box-free minimum theorems. Kernel translation makes formal unbounded-slot diagonal shifts state independent; other off-diagonal terms and convergence remain open. Named twenty-slot qubit moves, twelve sampled fourth-order backgrounds, a selected cosine Hessian with omega squared=2Jg lambda, and an L=3 modular incidence calculation are retained. No complete leading Hamiltonian or physical phase is claimed.
upstream_dependencies:
- minimal_axioms
runner: scripts/dynamics_clause_soft_tensor_constraint_generates_curvature_moves_2026_09_24.py
---

# Soft tensor constraints: explicit transition amplitudes and bounded diagnostics

**Type:** bounded_theorem

**Date:** 2026-09-24
**Status:** conditional-support; supplied-model mathematics, unaudited.

## Supplied model and scope

Use the canonical slots and vector stencil of the
[landed tensor parent](LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md).
The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not select this law.
The energy and perturbation are

    H0=U sum_rows (Gv)_row²,   V=-h sum_slots (X_s+X_s†),   U>0,

where v is the integer change from a zero-charge configuration and X_s
raises one slot by one. Each squared vector row is supported on one
link-site neighbourhood. The rotor model has unbounded integer slots.
For a two-level slot only its allowed raising or lowering direction acts.
Here h is the one-step matrix element; a spin field h_spin sigma_x/2
instead gives h=h_spin/2.

## Named planar displacement and its exact amplitude

The displacement delta in the ab plane has -2 on E_aa(c),E_bb(c),
+1 on E_aa(c±e_b),E_bb(c±e_a), and -1,+1,+1,-1 on the four ab faces
based at c,c-e_a,c-e_b,c-e_a-e_b. Direct substitution gives G delta=0.
Its L1 norm is twelve. Any twelve-step path from zero to this delta
must be monotone in every slot, with two coordinates taking 0,1,2 and
eight taking 0,1. There are 3² 2^8=2304 partial states and
12!/(2!2!)=119750400 ordered paths.

Only the two endpoints have zero syndrome. Exact rational recursion over
the partial states sums every intermediate denominator |Gv|² and gives

    A=111150053/31850496,
    <delta|H_eff|0> = -A h^12/U^11 at its first possible order.

The sign follows from twelve factors -h and eleven negative resolvents.
No subtraction involving an earlier visit to the degenerate sector
contributes to these minimal paths. This proves the coefficient of this
NAMED displacement, not that it is the globally first off-diagonal move.
The same recursion for a four-edge U(1) ring gives 5/2, or 5/32 with
(h_spin/2)^4. At equal one-step h the ratio is (A/(5/2))(h/U)^8.

Floating-point diagonalization of the 2304-state path box at h/U=.1,.15,.2
is a numerical diagnostic of the coefficient. Its tiny splittings and
extrapolation are not an exact finite-h or convergence proof. Every
minimal twelve-step path lies inside the box, which is why the exact
rational coefficient is unaffected by that truncation.

## What the searches establish

The radius-two box is [-2,2]^3 coarse cells, with every touching row imposed.
The L1 minimizer splits each coefficient into nonnegative positive and
negative parts bounded by four and restricts the selected anchor to +1 or +2.
The enumeration permits entries 0,±1,±2, the same positive anchor and L1≤12.
It finds six diagonal-anchor and four face-anchor planar patterns.
Completeness is asserted only when the final solver call reports infeasibility;
a timeout or enumeration cap fails the check. These are solver-reported
finite restricted results, not exact global integer certificates.

A separate radius-two unit-entry problem with anchor +1 reports support
twenty. The explicit planar twenty-slot pattern is printed in the primary;
the returned spatial patterns and that planar pattern have no zero-energy
proper monotone partial state. Their numerical path sums are approximately
0.926 and 510.6. These certify named order-twenty transitions.
No radius-three execution or box-free enumeration is present here.
Historical global minimum and orbit-completeness claims are deferred on
the preserved PR head.

## Diagonal energies and missing effective terms

For unbounded slots, translation by any kernel vector commutes with both
H0 and V. It maps any zero-charge basis configuration to any other one
in that sector. In a symmetry-respecting formal perturbative expansion,
all diagonal matrix elements therefore agree: only a state-independent
diagonal shift is generated. This does not establish convergence or rule
out other off-diagonal kernel translations. In particular, the complete
leading effective Hamiltonian is not inferred from a bounded search.

For two-level slots the available shift directions depend on the starting
configuration, so that translation argument fails. The runner samples
twelve balanced configurations on a 6³ torus where the displayed planar
twenty-slot move acts, and explicitly checks Gx=Gx'=0. In those samples
the fourth-order difference matches

    Delta E4=(201/960) Delta N_A h^4/U^3,

where N_A counts rows whose two diagonal slots differ. Some sampled
differences vanish. This is a sampled formula, not a theorem for every
balanced background or evidence that most configurations are split.
The original general claim and unprovided larger enumeration remain deferred.

## Selected cosine comparator and the factor of two

Study separately the selected sum -g sum_p(T_p+T_p†) with g>0,
T_p=exp(i delta_p dot q), plus a supplied J sum_s E_s²/2, J>0.
Expanding -2g cos(delta_p dot q) gives +g(delta_p dot q)².
If V(k) has the three planar rows, the potential Hessian is 2g V†V.
Thus on the vector-gauge quotient,

    omega² = 2 J g lambda(k),

where lambda is an eigenvalue of V†V restricted to ker G(k).
The factor two is essential with this definition of g.
All rows are O(|k|²), so the frequencies are O(|k|²).
At generic directions the selected three branches are quadratic; on
coordinate planes one vanishes. Finite momentum samples are diagnostics,
not a proof of positivity away from every possible exceptional momentum.
Additional generated curvature terms may change the soft branch.

Imposing S q=0 reduces the sampled configuration count to two, but
the supplied E² term does not preserve the scalar stabilizer.
This restricted count is not a dynamically invariant two-mode theory.
The parent's stronger cubic bound assumes both gauge symmetries, lifted
compact characters, fixed canonical structure and moment summability.
No general obstruction to nonlinear, singular or collective linear modes
is claimed.

## Modulo-two incidence

On the stated L=3 torus, restricting to face slots gives four slots per
row and four rows per slot. These are the dual cubic lattice's plaquette
and link incidences. Exact GF(2) elimination gives a 29-dimensional
face kernel and rank 26 for the six-face cube patterns, leaving three
winding classes. A planar integer piece reduced modulo two has eight
nonzero slots and zero syndrome. This is an incidence/code calculation,
not a demonstration of a selected topological phase.

## Evidence and negative-claim discipline

The [primary](../scripts/dynamics_clause_soft_tensor_constraint_generates_curvature_moves_2026_09_24.py)
and [receipt](../logs/runner-cache/dynamics_clause_soft_tensor_constraint_generates_curvature_moves_2026_09_24.txt)
retain the finite searches, exact path coefficient, numerical diagnostics,
SAT backgrounds and modular ranks. Current review does not apply an audit
verdict. No supplied Hamiltonian, slot type, state or gravitational reading
is adopted.

### N1
Examined routes are integer planar transitions, restricted integer/unit
searches, unbounded-slot translations, sampled two-level backgrounds and
modular face moves.

### N2
The absence of intermediate zero syndromes for a named path box does not
exclude all smaller moves on the full lattice. The two claims are distinct.

### N3
The tensor stencil, soft energy, slot shifts, couplings and optional electric
energy are imports. Native law selection and state preparation remain open.

### N4
The actual landed tensor parent supplies the stencil and compact-bound
hypotheses. Unprovided box-free or high-precision historical checks are
preserved as deferred work, not evidence of the retained claims.

### N5
Five resolutions are explicit: bound the optimizer domain; certify the
named transition by exact recursion; use translation symmetry only for
formal diagonal equality; narrow the qubit formula to twelve backgrounds;
correct the cosine Hessian factor two. Runner stdout records each one.

### N6
Global minimal order, a complete effective Hamiltonian, a uniform
perturbative limit, all-background qubit formulas and a controlled phase
remain deferred and recoverable from the original branch.

### N7
Other kernel moves can coexist with the planar moves. Finite modular
aliases and nonlinear mechanisms can evade the regular-character class.
Neither is silently excluded by the bounded computations.

### N8
The tensor complex and continuum comparisons have prior art in the parent.
These transition calculations do not establish gravitons, reciprocal
matter coupling, physical sources or a native quantum-gravity model.
