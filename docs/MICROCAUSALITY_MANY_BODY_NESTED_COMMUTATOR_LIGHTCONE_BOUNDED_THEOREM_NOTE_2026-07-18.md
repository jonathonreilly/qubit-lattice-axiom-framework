---
claim_id: microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional nested-commutator support structure on the qubit lattice for a SUPPLIED nearest-neighbor bond Hamiltonian class on a finite region, with the tensor-product algebra and Heisenberg convention declared as supplied hypotheses (the axioms supply no dynamics and no Hamiltonian; nothing physical is selected): (L1) one-neighborhood support growth of the adjoint action, exactly; (T1) at finite graph distance, every Taylor coefficient of [A_X(t), B_Y] at t = 0 with order k < d(X,Y) vanishes identically, while observables in disconnected components commute for all times; an exact three-site noncommuting instance reaches the cone at k = d; (T2) an exact named commuting-chain exhibit where the cone is never reached at any order, so cone-saturation is Hamiltonian-dependent; (T3) a finite-volume factorial-tail bound with region-level constant c = 2 J M. This coarse bound does not supply a volume-uniform velocity or finite-speed propagation. The distinct support value is the exact reaching/stalling exhibit pair; stronger generic finite-range path-count bounds already exist in the repository. This note is relevant to, but does not close, the cited many-body transfer-H/quasilocal-composition task, the U-integrated slice, or the sharp-rate slice; no physical propagation speed, kinetic-isotropy content, or dynamics selection is claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/microcausality_many_body_nested_commutator_lightcone_2026_07_18.py
---

# Finite-Volume Nested-Commutator Support And Cone Exhibits For A Supplied Bond Hamiltonian

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bounded support theorem on a supplied Hamiltonian class; the
axioms choose no dynamics, and no physical causal closure is claimed.
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
`docs/GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`
states: "The `U`-integrated, many-body, and sharp-rate problems are
separate open tasks, not walls claimed here." The earlier microcausality
bridge note
`docs/MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
also contains a stronger general finite-range interaction-path estimate,
while
`docs/SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md`
contains the same support-thickening mechanism and a path-count
Lieb-Robinson theorem. Those are prior bounded source surfaces, cited here
as non-load-bearing repo placement rather than proof inputs. This note's
distinct support value is narrower: an explicit three-site pair in which
one supplied Hamiltonian reaches the graph-distance order and another
stalls at every order, plus a deliberately coarse finite-volume tail bound.
It supplies a
conditional finite-range spin lemma relevant to that many-body task
without closing it: for a supplied finite-range bond Hamiltonian on a
finite qubit-lattice region, commutators of separated observables have a
zero of order at least the graph distance, with a finite-volume
factorial-tail bound above the cone. The named many-body/quasilocal-
composition task, the `U`-integrated slice, and the sharp-rate slice all
remain open exactly as named there — this block does not construct the
many-body transfer Hamiltonian nor place it in the finite-range class.

## The Supplied Class

Let `Λ ⊂ Z^3` be finite, not necessarily connected, and let
`H = Σ_{b∈E(Λ)} h_b` be a supplied Hamiltonian whose terms `h_b` are
Hermitian and supported on nearest-neighbor bonds `b` of `Λ`, with finite
bond norms; absent bonds may be represented by `h_b = 0`.
The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
boundary is the honesty needle here: "Admissibility
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
operator `A` with support `supp A ⊆ Λ`, let
`N(S)=S∪{y∈Λ : y is a nearest neighbor of some x∈S}`, set `N^0(S)=S`,
and define `N^k` by iteration. Distances use this induced nearest-neighbor
graph on `Λ`; `d(X,Y)` is the distance between nonempty supports and is
`∞` when they lie in different connected components.

## Results

**L1 (one-neighborhood support growth, exact).** For every bond `b` not
touching `supp A`, `[h_b, A] = 0` (the factors act on disjoint tensor
slots), so

> `supp(ad_H A) ⊆ N^1(supp A)`, and by iteration
> `supp(ad_H^k A) ⊆ N^k(supp A)`.

This is finite operator algebra on the supplied class; the runner gates
the disjoint-slot commutation and the one-step support containment on
exact three-site instances.

**T1 (below-cone Taylor vanishing, exact).** Let `A` and `B` be supported
in nonempty sets `X` and `Y`. The `k`-th Taylor
coefficient of `[A_X(t), B_Y]` at `t = 0` is `(i)^k/k! · [ad_H^k A, B]`.
When `d(X,Y)<∞`, L1 gives `supp(ad_H^k A) ⊆ N^k(X)`, and for
`k < d(X, Y)` that neighborhood is disjoint from `Y`, so the coefficient
vanishes identically:

> every coefficient with `k < d(X, Y)` vanishes — `[A_X(t), B_Y]` has a
> zero of order **at least** `d(X, Y)` at `t = 0` (arrival exactly at
> `d` holds for the named noncommuting instance below, not in general;
> see T2).

If `d(X,Y)=∞`, the same support argument makes every Taylor coefficient
zero. Finite-dimensional Heisenberg evolution is entire in `t`, so
`[A_X(t),B_Y]=0` for every `t`: disconnected components are the exact
all-time case, and no factorial involving `∞` is used.

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
gates both site-3 generators at `k = 2, 3` and the full-H/near-bond
equality through `k = 8`; the collapse identity carries the all-order
statement). So T1's vanishing is
a one-sided bound: below-cone coefficients always vanish, while
cone-saturation depends on the supplied Hamiltonian. No genericity claim
is made in either direction.

**T3 (finite-volume factorial-tail bound).** Let `d(X,Y)<∞`. With
`J = max_b ||h_b||` (and `J=0` when `E(Λ)` is empty) and
`M = |E(Λ)|` the number of bonds of the finite region, iterating the
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
to `binomial(k, d) ≥ 1`; the proof is note-carried and the runner checks a
finite exact integer grid). The displayed constant is a region-level
bookkeeping bound and can grow with the region. It therefore supplies no
volume-uniform velocity or finite-speed statement. Stronger finite-range
interaction-path bounds under bounded local overlap already appear in the
two repo-placement notes named above. The open residual relevant here is
instead to construct or control the reconstructed many-body transfer
Hamiltonian in a matching finite/quasilocal interaction class and prove the
tail-composition step; this note does neither.

## No-Go Discipline Gate

**Status: PASS.** The semantic negative is deliberately narrow: T2 proves
non-saturation only for the displayed `H=X_1X_2+X_2X_3`, `A=Z_1`, and
site-3 probe algebra. The applicable assertion classes are
`bounded_with_named_walls` and `derived_no_go_boundary`; no generic no-go
for finite-range dynamics is asserted.

**N1 — five alternative attacks.** Each route attacks the named exhibit,
not a broader Hamiltonian family.

| Route | Disposition | Test and result |
|---|---|---|
| The two bonds might fail to commute | ATTEMPTED | Exact Pauli multiplication and runner gate T2d give `[X_1X_2,X_2X_3]=0`. |
| The far-bond derivation might re-enter at a later nested order | ATTEMPTED | Since `[ad_{h12},ad_{h23}]=ad_{[h12,h23]}=0` and `ad_{h23}A=0`, every word containing `ad_{h23}` annihilates `A`; hence `ad_H^kA=ad_{h12}^kA`. |
| Resumming all Taylor orders might reach site 3 even if low orders do not | ATTEMPTED | The preceding equality holds for every `k`, and the finite-matrix Taylor series is entire, so the resummed evolution remains in the `{1,2}` algebra. |
| A different site-3 probe might detect hidden support | ATTEMPTED | Commutation with the generating probes `X_3` and `Z_3`, together with support in `{1,2}`, covers the full one-site algebra `M_2(C)`; the runner checks both generators through order 8 and the algebraic collapse is all-order. |
| The test machinery might report stalling for every two-bond chain | ATTEMPTED | The noncommuting comparator `X_1X_2+Z_2Z_3` reaches site 3 at order 2, so the same exact-matrix machinery distinguishes reach from stall. |

**N2 — supplied-condition independence.** The named conditions are:
`W1`, a finite tensor-product algebra on a finite region; `W2`, a supplied
nearest-neighbor Hermitian bond decomposition with finite norms; `W3`, the
Heisenberg convention generated by that supplied `H`; and `W4`, the absent
physical bridge placing the reconstructed many-body transfer Hamiltonian in
a finite/quasilocal interaction class. No pair collapses automatically:

| Pair | Closing first closes second? | Closing second closes first? | Independent? |
|---|---|---|---|
| W1 / W2 | no | no | yes |
| W1 / W3 | no | no | yes |
| W1 / W4 | no | no | yes |
| W2 / W3 | no | no | yes |
| W2 / W4 | no | no | yes |
| W3 / W4 | no | no | yes |

`W1`-`W3` bound this operator theorem. `W4` bounds only its physical reuse;
it is not needed to prove L1-T3.

**N3 — hidden-condition phrase scan.** "Supplied" names `W1`-`W3`
explicitly. "Background" occurs only in the title/scope of the cited
fixed-background note and is non-load-bearing here. "Approved" and
"registered" occur only in the primitive-status disclaimer and add no
premise. "By iteration" in L1 is the displayed induction, not a hidden
condition. The finite-matrix Taylor identity follows directly by repeated
differentiation of `e^{itH}Ae^{-itH}` under the stated convention; no
"standard QFT" or framework-supplied dynamics step is used.

**N4 — residual matching.** No prior negative result is used to prove T2;
its evidence is the direct algebra above. The contextual witnesses match
only the boundaries assigned to them:

| Witness | Witness residual | Residual used here | Match? |
|---|---|---|---|
| `GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md:277-278,315-317` | `U`-integrated, many-body transfer-H/LR-composition, and sharp-rate tasks remain separate | names the downstream task this supplied-class lemma does not close | yes |
| `MINIMAL_AXIOMS_2026-06-29.md:105-109` | Admissibility supplies no Hamiltonian, transfer operator, or dynamics | prevents reading the supplied `H` as axiom-derived | yes |
| T2 and the primary runner | exact named commuting-chain stall | T2's exact named commuting-chain stall | yes |
| Existing finite-range LR notes | generic path-count support theorem | repo placement only, not a witness for T2 | not used |

**N5 — rhetoric at each resolution.** At the named three-site
Hamiltonian/observable resolution, all-order non-saturation is proved. At
the resolution of other observables, other bond algebras, generic
finite-range Hamiltonians, the reconstructed transfer Hamiltonian, and a
continuum causal theory, it is not claimed. "Cone" means only graph-distance
Taylor support. The displayed `c=2JM` estimate is region-dependent and does
not itself supply a uniform velocity; that statement does not claim that no
stronger uniform estimate exists.

**N6 — partial-closure and primitive scan.** The current primitive registry
contains no dynamics or Hamiltonian premise, so no approved primitive closes
`W4`, and no new axiom is requested. Existing partial closures are material:

- `MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`
  already carries a stronger path-count theorem for supplied finite-range
  support families and a free hopping application;
- `SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md`
  independently carries support thickening and finite-range chain counting;
- `FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md` closes a
  free-bilinear quasilocal composition under its stated kernel hypothesis.

Those routes narrow `W4`; none constructs the full reconstructed many-body
transfer Hamiltonian or proves its `U`-integrated quasilocal composition.

**N7 — hostile steelman.** A hostile reviewer can say that the stall is an
artifact of choosing one commuting Pauli chain: change the second bond to
`Z_2Z_3` and the cone is reached, while stronger general finite-range
Lieb-Robinson theorems already exist in this repo. That defeats any generic
non-saturation, novelty, or many-body-closure reading. It does not defeat the
actual existential boundary—the named commuting example really does stall at
all orders—so the claim is kept at that narrow exhibit level and the stronger
prior work is acknowledged.

**N8 — cross-cycle echo.** The repo search found the three prior surfaces
listed in N6, the live conformal-causal source-packet finding in
`docs/repo/ACTIVE_REVIEW_QUEUE.md`, and
`docs/work_history/repo/review_feedback/QUBIT_SYMMETRY_EXCHANGE_LAW_REDUCTION_PROBE_NOTE_2026-07-14.md:70-75`,
which already records second-order reach on a three-site chain. Their
successful mechanism is local interaction-path counting (or exponentially
weighted path counting), not a new primitive. The same mechanism can
strengthen the coarse `2JM` estimate for a supplied class and has already
done so; it does not retire the separate transfer-H placement/composition
residual. No earlier wall was treated as foreclosing this exact named stall
exhibit.

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
commuting exhibit and full-H/near-bond equality through `k = 8`; the
disconnected-component instance through `k = 8`; factorial domination on
the exact grid `0 ≤ d ≤ 8`, `d ≤ k ≤ 16`; a commutator norm-bound instance;
and the rebuilt norm-inequality chain. The universal support, all-order
collapse, factorial, and source-boundary arguments remain note-carried
analytic steps rather than claims of exhaustive computation. The runner
does not read mutable source notes, so its SHA-pinned cache depends only on
the runner source and installed exact-arithmetic library.

Measured runner total after final verification:
`TOTAL: PASS=16 FAIL=0`.
