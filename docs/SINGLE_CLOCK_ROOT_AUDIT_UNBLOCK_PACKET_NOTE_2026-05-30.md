# Single-Clock Root Audit-Unblock Packet

**Date:** 2026-05-30
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This note is an
audit-unblock packet; it does not set or predict an audit verdict.
**Primary runner:**
[`scripts/frontier_single_clock_root_audit_unblock_packet.py`](../scripts/frontier_single_clock_root_audit_unblock_packet.py)
**Generated output:**
[`outputs/single_clock_root_audit_unblock_packet_2026-05-30.json`](../outputs/single_clock_root_audit_unblock_packet_2026-05-30.json)

## Purpose

This packet narrows the root dependencies of the single-clock
codimension-1 theorem to the exact scope needed by the 3+1
anomaly-forces-time parent route.

The parent route does **not** need a full continuum Wightman package,
cluster decomposition, observed Lorentzian spacetime, or an independent
mass-gap theorem. It needs only the following finite-lattice statement:

```text
qubit tensor locality on Z^3
+ physical 3+1 action surface with one reflection-positive temporal
  transfer axis and finite-range Hamiltonian
=> one Hamiltonian clock and one codimension-1 Cauchy slice.
```

This packet therefore separates stale broad roots from the genuinely
load-bearing root that remains.

## Dependency Narrowing

For the `d_t = 1` use in the anomaly-forces-time route, the active
single-clock proof needs:

1. **Equal-time local algebra.** A1+A2 supply one qubit algebra at each
   `Z^3` site and the tensor product over a spatial slice. Operators on
   distinct sites commute as tensor factors. This is already carried by the
   retained qubit/`Cl(3)` narrow algebra surface.
2. **One temporal transfer axis.** The physical action must supply a
   reflection-positive transfer matrix in exactly one direction. This is the
   real remaining root and is part of the staggered/Wilson action realization
   surface.
3. **Finite-range Hamiltonian.** Once the action supplies the local
   nearest-neighbor Hamiltonian, the finite-block Lieb-Robinson estimate is
   standard finite-range operator algebra.
4. **Positive transfer spectral calculus.** Once a positive Hermitian
   transfer matrix `T` exists, the ground-state-subtracted Hamiltonian
   `H = -log(T / ||T||) / a_tau` is self-adjoint and non-negative by ordinary
   finite-dimensional functional calculus.

The following older broad roots are therefore not independent blockers for
the time-count use case:

| Older root | Current audit status | Single-clock role after narrowing |
|---|---:|---|
| `AXIOM_FIRST_SPECTRUM_CONDITION_THEOREM_NOTE_2026-04-29.md` | unaudited | Not an independent root. The needed lattice spectrum condition follows from positive transfer-matrix functional calculus once temporal RP is supplied. |
| `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md` | unaudited | Not load-bearing for excluding `d_t > 1`. Clustering is useful for continuum QFT behavior, but the time-count intersection only needs one clock plus codimension-1 data. |
| `AXIOM_FIRST_MICROCAUSALITY_LIEB_ROBINSON_THEOREM_NOTE_2026-05-01.md` | unaudited | The continuum microcausality corollary is not load-bearing. The needed finite-lattice pieces are tensor-factor equal-time locality and finite-range Lieb-Robinson support. |
| `EMERGENT_LORENTZ_INVARIANCE_NOTE.md` / Lorentz-kernel notes | conditional / unaudited | Not load-bearing for the time-count proof. They are continuum/metric refinements after the single-clock lattice statement. |

The broad reflection-positivity parent is also too wide for the present use.
The actual load-bearing root is narrower:

```text
physical 3+1 staggered/Wilson action
=> one reflection-positive temporal transfer matrix
=> one Hamiltonian clock.
```

This remains tied to the staggered-Dirac/action realization gate. This packet
does not pretend to close that action gate.

## Finite Calculus Lemma

Let `T` be a positive Hermitian transfer matrix on a finite physical Hilbert
space. Let `M = ||T||_op`. On the support of `T`, define

```text
H := -log(T / M) / a_tau.
```

Then:

- `H` is self-adjoint;
- `H >= 0`;
- `exp(-a_tau H) = T / M`;
- the top eigenvector of `T` has energy `0`;
- any non-top eigenvalue of `T` gives a positive excitation energy.

This is finite-dimensional spectral calculus, not a separate physical
postulate. It is the only spectrum-condition content needed by the
single-clock lattice proof.

## Finite-Range Locality Lemma

Let the finite-block Hamiltonian be a sum of uniformly bounded local terms,

```text
H = sum_z h_z,
support(h_z) subset B_r(z),
||h_z|| <= J.
```

Then for operators `A_x`, `B_y` supported at sites `x` and `y`,

```text
|| [exp(iHt) A_x exp(-iHt), B_y] ||
  <= 2 ||A_x|| ||B_y|| exp(-d(x,y) + v_LR |t|)
```

with `v_LR = 2 e r J` in the standard coarse lattice estimate.
The equal-time case is stronger: if `x != y`, the commutator vanishes
exactly because the two operators live on different tensor factors.

This is the only microcausality/Lieb-Robinson content needed by the
single-clock lattice proof.

## What Remains After This Packet

This packet reduces the non-ABJ single-clock audit blockers to:

1. audit of this narrowed dependency packet;
2. audit of the single-clock theorem on the narrowed scope;
3. closure/audit of the physical 3+1 action surface that supplies the
   unique temporal transfer axis and finite-range Hamiltonian.

It does **not** close:

- the staggered-Dirac/action realization gate;
- full Wilson+staggered reflection positivity;
- the physical matter/hypercharge surface;
- the parent anomaly-forces-time theorem before independent audit.

## Audit Handoff

```yaml
proposed_claim_type: bounded_theorem
actual_current_surface_status: root-audit-unblock packet
target_claim_id: axiom_first_single_clock_codimension1_evolution_theorem_note_2026-05-03
trace_class: direct_dependency_narrowing
old_broad_roots_not_independent_blockers:
  - axiom_first_spectrum_condition_theorem_note_2026-04-29
  - axiom_first_cluster_decomposition_theorem_note_2026-04-29
  - axiom_first_microcausality_lieb_robinson_theorem_note_2026-05-01
  - emergent_lorentz_invariance_note
remaining_real_root:
  - physical 3+1 staggered/Wilson action temporal transfer-axis theorem
action_gate_still_open: true
audit_required_before_effective_status_change: true
```

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_single_clock_root_audit_unblock_packet.py
```

Expected:

```text
TOTAL: PASS=<N> FAIL=0
VERDICT: single-clock root audit unblock packet passes; old broad roots are
not independent blockers for the time-count use case, and the remaining root is the action/temporal-transfer axis.
```
