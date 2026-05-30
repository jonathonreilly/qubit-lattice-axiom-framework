# Physics Loop — β=6 SU(3) Wilson Single-Plaquette Closure

## North-star goal

Derive, from framework primitives (no PDG / Monte-Carlo import), the
thermodynamic SU(3) Wilson single-plaquette expectation at the framework
coupling β=6:

```
<P>(β=6, L→∞) ≈ 0.5934      <P> := <(1/N_c) Re Tr U_p>,  N_c=3
```

This is the single most-cited open quantitative gate in the framework. It
feeds `u_0 = <P>^(1/4)` → `α_s(v) = α_bare/u_0²` → `α_s(M_Z) ≈ 0.1181`, and
via `α_LM` touches the v / y_t / m_t / m_H chain. Currently `<P>` is available
only as (i) an admitted comparison/reuse number and (ii) a numerical
Monte-Carlo finite-size-scaling extrapolation (`P_inf = 0.59400 ± 0.00037`).
Neither is an analytic from-primitives derivation.

## The doubly-walled lane-killer (do NOT re-attempt)

Per the attack-surface frontier map
(`docs/BETA6_PLAQUETTE_CLOSURE_ATTACK_SURFACE_FRONTIER_NOTE_2026-05-29.md`,
PR #2245), zero of five analytic routes survive adversarial pruning. The
single missing object is uniformly:

> **ρ_{p,q}(6)** — the boundary character measure / Perron eigenvector of the
> unmarked 3D spatial Wilson environment at β=6.

It is **doubly walled**:

1. **Algebraic underdetermination by local data.** Local character +
   intertwiner data + any 1-parameter ρ-family do NOT select ρ_{p,q}(6)
   (Theorem-3, `gauge_vacuum_plaquette_tensor_transfer_perron_solve_note`);
   the finite jet + analyticity + monotonicity do NOT force β_eff(6)
   (`gauge_vacuum_plaquette_framework_point_underdetermination_note`).
2. **Computational infeasibility of exact multi-link data.** Any exact
   evaluation of the unmarked 3D spatial Wilson environment at L_s≥3 is the
   treewidth-29-infeasible SU(3) tensor contraction (8^30 intermediate ~ 1e19
   GB, `su3_wigner_l3_treewidth_infeasible_2026-05-04`); naive Haar-MC is
   sign-problem-bound (`su3_wigner_l3_cube_haar_mc_negative_result_2026-05-04`).

No current route supplies new dynamical input escaping BOTH foreclosures.

## Finite-runway strategy

The lane has a **finite runway** before the treewidth wall. The runway is the
exact connected strong-coupling series of Δ(β) := P_full(β) − P_1plaq(β):

- Retained anchor: `Δ(β) = β⁵/472392 + O(β⁶)` (four closed cube shells,
  `gauge_vacuum_plaquette_mixed_cumulant_audit_note`, 4/18⁵).
- Each new exact coefficient d_n is one exact SU(3) Haar cluster computation.
  Cluster count grows ~ μⁿ (lattice-animal constant μ≈8); each non-closed
  cluster is a 3nj contraction whose cost rises with area. **β⁶ feasible; β⁷
  feasible if the cluster enumeration + contraction stays tractable;
  β⁷–β⁸ is the practical ceiling before the treewidth-29 wall.**
- The exact coefficients are the decisive inputs to the **landed resummation
  test harness** (`BETA6_RESUMMATION_ANSATZ_TEST_HARNESS_BOUNDED_NOTE_2026-05-30.md`,
  PR #2255): {d₅, d₆} activate the **tadpole/geometric** predictive verdict
  (predicts d₇); exact d₇ then **falsifies-or-supports** it. The d-log-Padé
  predictive verdict needs {d₅..d₈} (= β⁸, at/past the wall), so only its
  forward `<P>(6)` test is in-runway.

This loop does NOT claim β=6 closure. It advances the exact-coefficient
frontier by one or two orders, sharpens the obstruction, and runs the cheapest
decisive falsifier of the one not-yet-blocked analytic ansatz. A genuine
closure would still require either a Münster-style graphical strong-coupling
organizer, or a rank-aware contractor defeating the treewidth wall, plus an
independent proof that Δ(β) is real-analytic on (0,6] with a complex-pair
dominant singularity.

## Method (this loop's engine)

Exact connected-cumulant linked-cluster expansion:
`d_n = (1/n!) Σ'_{q1..qn} κ(X_p0; X_q1,…,X_qn)` (not all q_i=p_0), with each
exact SU(3) single-link Haar integral built as the invariant-tensor projector
(δ-caps + ε/det sector), validated against closed forms (int U Ū = δδ/3,
int UUU = εε/6, (2,2) U(3) Weingarten) and high-precision Haar Monte-Carlo.
Moments → connected cumulants via the set-partition Möbius formula; supports
enumerated on the proven "≥1 action face per p_0 edge + extras" scaffold with
a GF(3) link-balance pre-filter.

## Status authority

This loop's notes do not set or predict audit outcomes. All cited statuses are
read-offs from `docs/audit/data/audit_ledger.json`
(`rows[<claim_id>]['effective_status']`) on the stated dates. Framework PRs
land science/fixes only; never audit-lane data.
