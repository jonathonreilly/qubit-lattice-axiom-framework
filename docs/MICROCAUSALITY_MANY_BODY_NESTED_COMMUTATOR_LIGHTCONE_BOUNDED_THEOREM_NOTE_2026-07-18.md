---
claim_id: microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional nested-commutator lightcone structure on the qubit lattice for a SUPPLIED finite-range bond Hamiltonian class on a finite region, with the tensor-product algebra and Heisenberg convention declared as supplied hypotheses (the axioms supply no dynamics and no Hamiltonian; nothing physical is selected): (L1) one-neighborhood support growth of the adjoint action, exactly; (T1) below-cone vanishing — every Taylor coefficient of [A_X(t), B_Y] at t = 0 with order k < d(X,Y) vanishes identically, so the commutator has a zero of order at least d(X,Y), with an exact three-site noncommuting instance reaching the cone at k = d; (T2) an exact commuting-chain exhibit where the cone is never reached at any order (the two bonds commute and the far bond commutes with the observable, so the nested adjoint chain collapses to the near bond alone), so cone-saturation is Hamiltonian-dependent; (T3) a finite-volume factorial-tail bound with region-level constants (M = the number of bonds in the finite region) and the exact tail domination — explicitly NOT a volume-uniform velocity statement and NOT finite-speed propagation. This is a conditional finite-range spin lemma relevant to, but not closing, the cited note's named many-body/quasilocal-composition open task, which remains open along with the U-integrated and sharp-rate slices; no physical propagation speed, kinetic-isotropy content, or dynamics selection is claimed."
upstream_dependencies:
  - minimal_axioms
  - gauged_log_transfer_quasilocality_combes_thomas_narrow_theorem_note_2026-06-13
runner: scripts/microcausality_many_body_nested_commutator_lightcone_2026_07_18.py
---

# Microcausality: A Many-Body Nested-Commutator Lightcone For The Supplied Finite-Range Class

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; the Hamiltonian class is supplied, exactly
as in the cited microcausality notes; the axioms choose no dynamics.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here; the kinetic-isotropy primitive is not used.
**Primary runner:**
[`scripts/microcausality_many_body_nested_commutator_lightcone_2026_07_18.py`](../scripts/microcausality_many_body_nested_commutator_lightcone_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_many_body_nested_commutator_lightcone_2026_07_18.txt`](../logs/runner-cache/microcausality_many_body_nested_commutator_lightcone_2026_07_18.txt)

## Purpose

The landed gauged quasilocality note
[`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md)
states: "The `U`-integrated, many-body, and sharp-rate problems are
separate open tasks, not walls claimed here." The one-particle bridge
surface
[`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
works on one-particle blocks and free bilinear sectors. This note supplies a
conditional finite-range spin lemma relevant to that many-body task
without closing it: for a supplied finite-range bond Hamiltonian on a
finite qubit-lattice region, commutators of separated observables have a
zero of order at least the graph distance, with a finite-volume
factorial-tail bound above the cone. The named many-body/quasilocal-
composition task, the `U`-integrated slice, and the sharp-rate slice all
remain open exactly as named there — this block does not construct the
many-body transfer Hamiltonian nor place it in the finite-range class.

## The Supplied Class

Let `Λ ⊂ Z^3` be finite and
`H = Σ_b h_b` a supplied Hamiltonian whose terms `h_b` are Hermitian and
supported on nearest-neighbor bonds `b` of `Λ`, with finite bond norms.
The axiom memo's own boundary is the honesty needle here: "Admissibility
is not a dynamics axiom." and "It does not
choose a Hamiltonian or transfer operator". Everything below is a theorem
about the supplied class, of the same conditional shape as the cited
microcausality notes; no dynamics is selected and no physical propagation
speed is claimed.

Two further supplied hypotheses are declared (not axiom consequences):
the observable algebra is the finite tensor product `⊗_{x∈Λ} M_2(C)`
with operators supported on tensor slots, and time evolution is the
Heisenberg convention `A(t) = e^{itH} A e^{−itH}`, under which the `k`-th
Taylor coefficient of `A(t)` at `t = 0` is `(i)^k/k! · ad_H^k A`. For an
operator `A` with support `supp A ⊆ Λ`, write `N^k(supp A)` for the
`k`-fold nearest-neighbor graph neighborhood and `d(X, Y)` for the graph
distance between supports.

## Results

**L1 (one-neighborhood support growth, exact).** For every bond `b` not
touching `supp A`, `[h_b, A] = 0` (the factors act on disjoint tensor
slots), so

> `supp(ad_H A) ⊆ N^1(supp A)`, and by iteration
> `supp(ad_H^k A) ⊆ N^k(supp A)`.

This is finite operator algebra on the supplied class; the runner gates
the disjoint-slot commutation and the one-step support containment on
exact three-site instances.

**T1 (below-cone Taylor vanishing, exact).** The `k`-th Taylor
coefficient of `[A_X(t), B_Y]` at `t = 0` is `(i)^k/k! · [ad_H^k A, B]`.
By L1, `supp(ad_H^k A) ⊆ N^k(X)`, and for `k < d(X, Y)` that neighborhood
is disjoint from `Y`, so the coefficient vanishes identically:

> every coefficient with `k < d(X, Y)` vanishes — `[A_X(t), B_Y]` has a
> zero of order **at least** `d(X, Y)` at `t = 0` (arrival exactly at
> `d` holds for the named noncommuting instance below, not in general;
> see T2).

Exact instance (gated, 8-by-8): on the three-site chain with
`H = X_1 X_2 + Z_2 Z_3`, `A = Z_1`, `B = X_3` (`d = 2`): the `k = 0` and
`k = 1` commutators are exactly zero and the `k = 2` commutator is
nonzero — the cone is reached at `k = d`.

**T2 (the cone need not be reached: commuting exhibit, exact, all
orders).** For the commuting chain `H = X_1 X_2 + X_2 X_3` with
`A = Z_1`: since `[h_{12}, h_{23}] = 0` and `[h_{23}, A] = 0`, the nested
adjoint chain collapses to the near bond alone,
`ad_H^k A = ad_{h_{12}}^k A` for every `k`, so the support never leaves
`{1, 2}` and no site-3 probe is ever reached, at any order (the runner
gates the displayed orders `k = 2, 3` for both site-3 probes; the
collapse identity carries the all-order statement). So T1's vanishing is
a one-sided bound: below-cone coefficients always vanish, while
cone-saturation depends on the supplied Hamiltonian. No genericity claim
is made in either direction.

**T3 (finite-volume factorial-tail bound).** With `J = max_b ||h_b||`
and `M = |E(Λ)|` the number of bonds of the finite region, iterating the
commutator norm inequality `||[P, Q]|| ≤ 2||P||·||Q||` — itself rebuilt
here rather than cited: `||PQ − QP|| ≤ ||PQ|| + ||QP|| ≤ 2||P||·||Q||`
by the triangle inequality and submultiplicativity of the operator norm,
with the runner gating the squared-norm chain on an exact instance —
over the bond sum
gives `||ad_H^k A|| ≤ (2 J M)^k ||A||` and hence, for `d = d(X, Y)`,

> `||[A_X(t), B_Y]|| ≤ 2 ||A|| ||B|| Σ_{k ≥ d} (c |t|)^k / k!
>  ≤ 2 ||A|| ||B|| · ((c |t|)^d / d!) · e^{c |t|}`,

with `c = 2 J M`, using the exact tail domination
`Σ_{k ≥ d} x^k/k! ≤ (x^d/d!)·e^x` (from `d!/k! ≤ 1/(k−d)!`, equivalent
to `binomial(k, d) ≥ 1`, gated formally). The constant is a
region-level bookkeeping bound: it grows with the region, so this is
explicitly **not** a volume-uniform velocity and **not** a finite-speed
propagation statement; a genuine volume-uniform Lieb-Robinson constant
would need the interaction-path argument, which together with the
sharp-rate problem remains open exactly as the cited note names it.

## No-Go Discipline Gate

T2 is the block's bounded negative (cone non-saturation for a named
Hamiltonian), answered:

- **N1 route inventory:** (1) perturb the commuting chain's couplings —
  any all-`X` bond chain has commuting site factors and stalls
  identically; ATTEMPTED in structure (the stall is algebraic, not
  fine-tuned); (2) change the probe `B` — the `k`-step operator stays
  supported on `N^1`, so every site-3 probe commutes; ATTEMPTED via the
  support gate; (3) longer times — the collapse identity `ad_H^k A = ad_{h_12}^k A`
  carries the stall to every order (the runner gates `k ≤ 3`);
  (4) different observables `A` — `Z_1` is the exhibited case; other
  choices are named untested; (5) non-commuting bonds — that is T1's
  generic instance, not a rescue of the stall.
- **N2 wall independence:** one exhibit wall (non-saturation); T1's
  vanishing is a positive statement, not a second wall.
- **N3 hidden-wall scan:** finiteness of the region, Hermiticity and
  finite bond norms, and the nearest-neighbor range are the supplied
  class, stated; the Taylor-coefficient identification
  (`∂_t^k` at `t = 0` giving nested commutators) is the standard exact
  identity on finite matrices, note-carried.
- **N4 residual matching and dependency roles:** the Combes-Thomas note
  supplies the named open-task sentence (the block's target) and the
  conditional shape; `minimal_axioms` supplies the no-dynamics boundary
  needle; the one-particle bridge note is contrast context, cited in
  prose only.
- **N5 rhetoric audit:** "lightcone" here means exactly the below-cone
  Taylor vanishing plus the series bound for the supplied class; no
  physical causality, continuum, `U`-integrated, or sharp-rate claim; no
  genericity claim for saturation.
- **N6 partial-closure scan:** the `U`-integrated and sharp-rate slices
  remain open exactly as the cited note names them; nothing here
  forecloses either.
- **N7 steelman:** "Lieb-Robinson bounds are textbook." Reply: stated as
  such — the note's content is the exact placement on this framework's
  supplied class with runner-gated instances, the honest commuting-stall
  exhibit pair, and the closure of the many-body slice the lane itself
  named open; the comparator literature is not imported as proof.
- **N8 cross-cycle echo:** no prior cycle in this lane is cited; the
  exhibit-pair shape (named reaching instance plus named stalling
  instance) is used in place of any genericity claim.

## Non-Claims

- Does **not** select, derive, or prefer any Hamiltonian; the axioms
  supply no dynamics, and the supplied-class shape matches the cited
  microcausality notes.
- Does **not** claim a physical propagation speed, kinetic-isotropy
  content, continuum limits, `U`-integrated statements, or sharp rates.
- Does **not** claim cone-saturation for generic Hamiltonians.
- Does **not** set an audit verdict; independent audit remains required.

## Verification

The primary runner checks the listed reductions and witnesses and nothing
more (sympy, exact arithmetic, single process, three-site 8-by-8
instances): disjoint-slot bond commutation; one-step support containment;
the T1 instance (`k = 0, 1` zero, `k = 2` nonzero at `d = 2`); the T2
commuting exhibit (`k = 2, 3` zero); the factorial tail-domination
inequality in formal form; a commutator norm-bound instance; and needle
checks pinning the cited note's open-task sentence, the axiom memo's
no-dynamics sentences, and this note's claim identifier and labels.
Mutation checks (one load-bearing mutation per check family, reverted)
are recorded in the review history and PR body.

Measured runner total after final verification:
`TOTAL: PASS=17 FAIL=0`.
