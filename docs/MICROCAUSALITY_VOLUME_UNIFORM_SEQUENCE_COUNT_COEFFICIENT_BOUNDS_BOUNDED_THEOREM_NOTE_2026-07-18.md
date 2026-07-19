---
claim_id: microcausality_volume_uniform_sequence_count_coefficient_bounds_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional bounded theorem for the supplied nearest-neighbor two-site bond Hamiltonian class on finite qubit-lattice regions (the axioms supply no dynamics): (W1) exact expansion of nested adjoints into ordered bond sequences; (W2) sequence-by-sequence death unless every next bond touches the current support, giving below-cone Taylor vanishing; (W3) N_0 = 1 and N_{k+1} <= 6(m+k)N_k, hence N_k <= product_{j=0}^{k-1}6(m+j), uniformly in region volume; (W4) ||[ad_H^k A,B]|| <= 2||A||||B||(2J)^k N_k, with an exact three-site reach-retreat-re-arrival witness showing that the inequality is one-sided; (W5) for finite d >= 0 and a region family with finite J_* = sup ||h_b||, a uniform Taylor-tail bound bar_a_d/(1-r_*) on the sufficient window r_* = 12J_*|t|(m+d)/(d+1) < 1. Generic all-time interaction-path theorems are not rederived here. Construction/control of the reconstructed many-body transfer Hamiltonian in a matching finite or quasilocal class, tail composition, the U-integrated slice, and the sharp-rate slice are outside this theorem; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.py
---

# Microcausality: Volume-Uniform Sequence-Count Coefficient Bounds And A Local Time Window

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; supplied nearest-neighbor two-site bond
Hamiltonians, finite tensor-product algebra, and the Heisenberg convention.
The axioms choose no dynamics.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.py`](../scripts/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.txt`](../logs/runner-cache/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.txt)

## Purpose And Placement

The sibling
[`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md)
proves below-cone Taylor vanishing, an all-time disconnected-component result,
and a deliberately coarse finite-volume factorial-tail bound. It also records
that stronger generic finite-range interaction-path bounds already exist on
repository source surfaces. This note supplies a narrower self-contained
Taylor-level lemma for the nearest-neighbor two-site bond subclass: expand into
ordered bond sequences, discard dead sequences, count the survivors using only
local support data, and sum a geometric majorant on an explicit local window.

The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
memo supplies only the honesty boundary that Admissibility is not a dynamics
axiom and chooses no Hamiltonian or transfer operator. The Hamiltonian below is
supplied. This theorem neither rederives the existing generic all-time
interaction-path result nor places the reconstructed many-body transfer
Hamiltonian in its hypotheses. The live physical bridge residual is that
placement/control problem together with quasilocal tail composition; the
`U`-integrated and sharp-rate slices are also separate.

## Supplied Class And Notation

Let `Lambda` be a finite region of `Z^3`, not necessarily connected. Let

> `H = sum_{b in E(Lambda)} h_b`

be a supplied Hermitian Hamiltonian with each `h_b` supported on one
nearest-neighbor two-site bond and `J = max_b ||h_b||` (take `J = 0` when the
bond set is empty). The observable algebra is the finite tensor product of
one-site `M_2(C)` factors, and
`A(t) = exp(itH) A exp(-itH)`. Let `A` be supported on a nonempty set `X` of
`m >= 1` sites and let `B` be supported on `Y`. Distances are graph distances
in the induced nearest-neighbor graph. Thus `d = d(X,Y)` is a finite integer
`d >= 0` when the supports lie in one component and `d = infinity` otherwise.

For an ordered sequence `(b_k,...,b_1)`, write

> `T(b_k,...,b_1) = ad_{h_{b_k}} ... ad_{h_{b_1}} A`.

Let `N_k` be the number of length-`k` sequences for which `T` is nonzero, and
define the empty-sequence count `N_0 = 1`. Define the local product majorant

> `bar_N_0 = 1`, and
> `bar_N_k = product_{j=0}^{k-1} 6(m+j)` for `k >= 1`.

For a family of regions, volume-uniformity below additionally assumes the
finite bound

> `J_* = sup_{Lambda,b} ||h_b^(Lambda)|| < infinity`.

This family hypothesis is not implied by finiteness of each individual region.

## Results

**W1 (ordered sequence expansion, exact).** Linearity of the commutator gives

> `ad_H^k A = sum_{(b_k,...,b_1) in E(Lambda)^k}
> ad_{h_{b_k}} ... ad_{h_{b_1}} A`.

Every ordered word occurs once. This is a finite algebraic identity, not a
commutative multinomial collection.

**W2 (dead-sequence lemma and below-cone vanishing, exact).** If the innermost
bond misses `X`, its commutator with `A` is zero. At any later stage, a bond
that misses the current operator support also gives zero. Hence every nonzero
sequence begins on `X` and each subsequent bond touches the support produced
by its prefix. Each such nearest-neighbor two-site bond can add at most one new
site. A length-`k` sequence therefore cannot reach `Y` when finite `k < d`, so

> `[ad_H^k A,B] = 0` for every finite `k < d`.

When `d = infinity`, the sibling's all-time disconnected-component theorem
applies; no factorial or local-window formula involving infinity is used.

**W3 (local sequence-count majorant).** A set of `s` sites in `Z^3` has `6s`
site-edge incidences. An internal bond is counted twice and a boundary bond
once, so the number of distinct nearest-neighbor bonds touching the set is at
most `6s`; restricting to a finite region only removes bonds.

Partition the surviving length-`k+1` sequences by their unique length-`k`
prefix. A surviving prefix has accumulated at most `m+k` sites, and its
extension fiber contains at most `6(m+k)` touching bonds. The prefix map is
generally many-to-one; the fiber bound, not injectivity, proves

> `N_{k+1} <= 6(m+k) N_k`.

With `N_0 = 1`, induction gives

> `N_k <= bar_N_k = product_{j=0}^{k-1} 6(m+j)`.

The right-hand side depends on `m`, the coordination number, and `k`, but not
on the region volume.

**W4 (volume-uniform coefficient bound; one-sided).** Iterating
`||[P,Q]|| <= 2||P||||Q||` along each sequence gives

> `||T(b_k,...,b_1)|| <= (2J)^k ||A||`.

The final commutator with `B`, followed by the triangle inequality, gives

> `||[ad_H^k A,B]|| <= 2||A||||B||(2J)^k N_k`
> `                         <= 2||A||||B||(2J)^k bar_N_k`.

This is volume-uniform at each fixed order for fixed local data. It is only an
upper bound. On the three-site chain
`H = X_1X_2 + Z_2Z_3`, `A = Z_1`, the cone reaches site 3 at order 2: the
`X_3` and `Y_3` probes register while `Z_3` is silent. At order 3, every
ordered sequence term separately commutes with the full site-3 probe algebra;
the far-site component is absent term-by-term, rather than canceled between
words. At order 4, `X_3` and `Y_3` register again while `Z_3` remains silent.
This exact reach-retreat-re-arrival witness makes no statement about other
Hamiltonians or all Taylor orders.

**W5 (family-uniform bound on a certified local time window).** Assume first
that `d` is a finite integer `d >= 0`, `J_* > 0`, and both observable norms are
nonzero. For an individual region define

> `a_k = 2||A||||B||(2J)^k N_k |t|^k/k!`,

and define the region-independent majorant

> `bar_a_k = 2||A||||B||(2J_*)^k bar_N_k |t|^k/k!`.

Then `a_k <= bar_a_k`. The exact product recurrence for `bar_N_k` gives

> `bar_a_{k+1}/bar_a_k = 12J_*|t|(m+k)/(k+1)`

whenever the ratio is defined. Moreover

> `(m+k)/(k+1) - (m+k+1)/(k+2)
>  = (m-1)/((k+1)(k+2)) >= 0`,

so the ratio is nonincreasing for `m >= 1`. Set

> `r_* = 12J_*|t|(m+d)/(d+1)`.

If `r_* < 1`, equivalently

> `|t| < (d+1)/(12J_*(m+d))`,

then W2 and geometric domination give the explicitly local bound

> `||[A_X(t),B_Y]|| <= sum_{k>=d} a_k`
> `                         <= sum_{k>=d} bar_a_k`
> `                         <= bar_a_d/(1-r_*)`.

All quantities on the final right-hand side are fixed by `m`, `d`, `J_*`, the
observable norms, the coordination number, and `t`; the region volume does not
appear.

The boundary cases require no division by a vanishing term. If `N_d = 0`, the
W3 recurrence forces every later `N_k` to vanish. If either observable norm is
zero, the commutator is zero. If `t = 0` or `J_* = 0`, the static commutator
bound is immediate: it is zero for `d > 0` and at most `2||A||||B|| = bar_a_0`
for `d = 0`. For `d = 0`, the definition `N_0 = bar_N_0 = 1` supplies the
first Taylor term. For `d = infinity`, use the sibling's exact all-time
disconnected-component result instead.

## No-Go Discipline Gate

**Status: PASS.** The narrowest honest classification is
`bounded-with-corrected-wall-count`. W1-W5 are a local Taylor corollary on a
supplied nearest-neighbor two-site bond class. The generic all-time
interaction-path theorem is not an open wall and is not claimed as new here.

**N1 — alternative attacks and routes.**

| Route | Disposition | Test and result |
|---|---|---|
| Change the order-3 far-site probe across the one-site Pauli basis | ATTEMPTED | `X_3`, `Y_3`, and `Z_3` are all silent. |
| Inspect each order-3 bond word rather than the summed adjoint | ATTEMPTED | Every word commutes with the far-site algebra; the retreat is term-by-term. |
| Advance one order | ATTEMPTED | Order 4 re-arrives against `X_3` and `Y_3`, defeating any all-order stall reading. |
| Reorganize the expansion by Duhamel/Gronwall interaction paths | NOT YET ATTEMPTED HERE | Existing repository source surfaces already carry stronger generic bounds, so this is not counted as an open wall. |
| Derive the physical Hamiltonian from the minimal axioms | RULED OUT BY PRIOR | The approved axiom memo supplies no Hamiltonian, transfer operator, or dynamics. |
| Construct/control the reconstructed many-body transfer Hamiltonian and compose its quasilocal tails | NOT YET ATTEMPTED | This is the actual physical bridge residual. |
| Perform the `U`-integrated and sharp-rate steps | NOT YET ATTEMPTED | These are separate downstream tasks. |

**N2 — premise and residual independence.** The theorem premises are `P1`, a
finite tensor-product algebra/region; `P2`, a supplied nearest-neighbor
two-site bond family together with finite `J_*`; and `P3`, the Heisenberg
convention generated by that supplied Hamiltonian.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| `P1/P2` | no | no | yes |
| `P1/P3` | no | no | yes |
| `P2/P3` | no | no | yes |

For physical reuse, the remaining residuals are `R1`, transfer-H
placement/control and quasilocal tail composition; `R2`, `U` integration; and
`R3`, a sharp rate.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| `R1/R2` | no | no | yes |
| `R1/R3` | no | no | yes |
| `R2/R3` | no | no | yes |

The generic all-time path-count theorem is not included in the residual table.

**N3 — hidden-condition scan.** The load-bearing conditions are explicit:
finite `d` for W5, `N_0 = 1`, nonempty `X` and `m >= 1`, finite family
supremum `J_*`, separate zero-norm/zero-time/zero-coupling cases, a supplied
nearest-neighbor two-site bond decomposition, finite tensor-product algebra,
and the Heisenberg convention. The direct minimal-axiom link records only the
no-dynamics boundary. No generic finite-range or multi-site constant is hidden
inside the number `6`.

**N4 — residual matching.**

| Witness | Witness residual | Residual used here | Match? |
|---|---|---|---|
| Current sibling note | Generic finite-range path-count bounds already exist; reconstructed transfer-H placement/control and tail composition remain | W1-W5 do not close the transfer-H placement/composition problem | yes |
| Minimal-axiom memo | No Hamiltonian, transfer operator, or dynamics is supplied by Admissibility | Prevents reading the supplied `H` as axiom-derived | yes |
| Direct Pauli calculation | Exact order-3 retreat for the named instance | Exact order-3 retreat only | yes |

**N5 — rhetoric by resolution.** Sequence-by-sequence, the order-3 retreat is
exact. Probe-by-probe, `X_3` and `Z_3` generate the full far-site algebra and
`Y_3` is also checked. Order-by-order, only the displayed orders 2-4 support
the reach-retreat-re-arrival wording. Hamiltonian-by-Hamiltonian, one Pauli
chain supplies the witness and no generic saturation claim is made.
Family-wide, W5 is conditional on finite `J_*` and the displayed local window.

**N6 — partial closure.** The sibling records prior generic path-count,
support-thickening, and free-bilinear quasilocal source surfaces. Those results
retire any claim that generic interaction-path counting is globally open. They
do not construct the reconstructed many-body transfer Hamiltonian, prove that
it lies in a matching finite or quasilocal interaction class, or compose its
tails through the `U`-integrated step. No new axiom or convention is requested.

**N7 — hostile steelman.** A hostile reviewer can correctly say that W1-W5
are a deliberately weaker local-Taylor corollary of generic finite-range
Lieb-Robinson machinery, and that finite examples cannot prove the universal
counting lemma. That defeats novelty, theorem-by-computation, and
globally-open-route readings. It does not defeat the note-carried fiber-count
proof or the resulting local window under the explicit nearest-neighbor and
finite-`J_*` hypotheses.

**N8 — cross-cycle echo.** The sibling's source inventory finds the earlier
microcausality path-count, spatial-cluster Lieb-Robinson, and free-bilinear
quasilocal surfaces. Their successful mechanism is local or exponentially
weighted interaction-path counting. This theorem uses the same local
combinatorial mechanism only for its displayed Taylor majorant, acknowledges
the stronger generic results, and leaves only the distinct transfer-H
placement/composition, `U`-integration, and sharp-rate residuals.

## Non-Claims

- Does **not** select, derive, or prefer a Hamiltonian; the axioms supply no
  dynamics.
- Does **not** cover generic finite-range or multi-site interactions with the
  displayed constant `6`.
- Does **not** claim a physical propagation speed, a new generic all-time
  Lieb-Robinson theorem, a continuum limit, kinetic isotropy, `U` integration,
  or a sharp rate.
- Does **not** claim coefficient nonvanishing at or above the graph-distance
  order.
- Does **not** set an audit verdict; independent audit remains required.

## Verification

The primary runner checks exact finite-matrix witnesses and independent
symbolic/numeric instances of the formulas it implements: ordered sequence
expansion at orders 2 and 3; inner- and later-miss death; below-cone vanishing;
the `6s` incidence count; `N_0`, the product majorant, and its recurrence;
actual sequence counts; the W4 coefficient bound using both the actual count
and the product majorant; the complete order-2 through order-4 probe table;
the W5 ratio, monotonicity, window constant, geometric tail, family-finiteness
condition, and boundary cases. The universal fiber-count and family-uniform
arguments remain note-carried analytic steps rather than claims of exhaustive
computation. The runner reads no mutable source notes, so its SHA-pinned cache
depends only on the runner source and installed exact-arithmetic library.

Measured runner total after final verification:
`TOTAL: PASS=23 FAIL=0`.
