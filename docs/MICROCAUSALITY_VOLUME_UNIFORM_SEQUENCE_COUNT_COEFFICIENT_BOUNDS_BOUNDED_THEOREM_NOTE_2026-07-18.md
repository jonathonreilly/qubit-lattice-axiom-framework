---
claim_id: microcausality_volume_uniform_sequence_count_coefficient_bounds_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional strengthening of the sibling lightcone lemma on the same supplied finite-range class (axioms supply no dynamics; same declared algebra and Heisenberg convention): (W1) the exact multinomial expansion of the nested adjoint into bond sequences; (W2) the dead-sequence lemma — a sequence contributes only if each bond touches the support accumulated so far — recovering below-cone vanishing sequence-by-sequence; (W3) the accumulated-support sequence count N_k bounded by the conservative local product 6^k·m(m+1)···(m+k−1) with m the site count of the observable's support (a touching bond adds at most one new site — a review-lens strengthening adopted with its recurrence N_{k+1} ≤ 6(m+k)N_k proven by unique-prefix extension) — independent of the region size at fixed local data; (W4) volume-uniform per-coefficient bounds ||[ad_H^k A, B]|| ≤ 2||A||||B||(2J)^k N_k, gated at k = 2 with exact norms, plus an exact k = 3 parity exhibit where every sequence's commutator with the chosen probe vanishes although the cone was reached at k = 2 — coefficient bounds are upper bounds, probe- and order-dependent; (W5) a commutator bound uniform over region families at fixed J_* = sup over the family of the bond norms, m, observable norms, and coordination, on the certified sufficient window |t| < (d+1)/(12·J_*·(m+d)), via the recurrence, term-ratio, and geometric-tail chain, with the zero-coefficient, t = 0, and J = 0 cases handled separately and every inequality gated. The all-time volume-uniform Lieb-Robinson constant (the integral-equation walk reorganization) and the sharp rate remain open exactly as the sibling names them; nothing physical is selected."
upstream_dependencies:
  - minimal_axioms
  - microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.py
---

# Microcausality: Volume-Uniform Sequence-Count Coefficient Bounds And The Local Time Window

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; same supplied class, algebra, and
Heisenberg convention as the sibling note; the axioms choose no dynamics.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.py`](../scripts/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.txt`](../logs/runner-cache/microcausality_volume_uniform_sequence_count_coefficient_bounds_2026_07_18.txt)

## Purpose

The sibling note
[`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md)
proved below-cone vanishing and a factorial-tail bound whose constant
`c = 2J·|E(Λ)|` is region-level, stating: "a genuine volume-uniform
Lieb-Robinson constant would need the interaction-path argument". This
note supplies the exact Taylor-level part of that argument: expanding the
nested adjoint into bond sequences and counting only those that survive
the dead-sequence lemma replaces the region-level bond count with local
data (the observable's support size and the lattice's local bond counts),
giving volume-uniform per-coefficient bounds at every order and a
volume-uniform commutator bound on an exact local time window. What it
does not supply — stated plainly — is the all-time volume-uniform
constant: that needs the integral-equation reorganization into
walks adjacent to the previous bond, which, together with the sharp rate,
remains open exactly as the sibling names it.

## Results

On the sibling's supplied surface (finite region `Λ ⊂ Z^3`, supplied
nearest-neighbor bond Hamiltonian `H = Σ_b h_b`, `J = max_b ||h_b||`,
observable `A` supported on `X` with `m = |X|` sites, probe `B` on `Y`,
`d = d(X, Y)`):

**W1 (multinomial sequence expansion, exact).** Nested adjoints expand
into bond sequences:

> `ad_H^k A = Σ_{(b_k, ..., b_1)} ad_{h_{b_k}} ··· ad_{h_{b_1}} A`,

a finite algebraic identity (gated at `k = 2, 3` on the three-site
chain by summing all `2^k` sequences exactly).

**W2 (dead-sequence lemma, exact).** A sequence contributes zero unless
its innermost bond touches `X` and each later bond touches the support
accumulated by the earlier bonds (the sibling's L1, applied per step;
gated: inner-miss and later-miss sequences vanish exactly, on three- and
four-site instances). Surviving sequences grow the support by at most one
bond per step, so no sequence of length `k < d` reaches `Y` — recovering
the sibling's below-cone vanishing sequence-by-sequence.

**W3 (accumulated-support count, local and exact).** The number `N_k` of
surviving sequences obeys

> `N_k ≤ Π_{j=0}^{k−1} 6·(m + j)`, via the recurrence
> `N_{k+1} ≤ 6·(m + k)·N_k`
>
> (unique-prefix extension: every surviving length-`(k+1)` sequence is a
> surviving length-`k` prefix extended by one bond touching the
> accumulated support of at most `m + k` sites; the map to prefixes is
> injective),

since a support of `s` sites on `Z^3` meets at most `6s` bonds and a
bond required to touch the accumulated support adds at most **one** new
site (a review-lens strengthening adopted here). Every factor is fixed by `m`, the coordination number `6`, and the
sequence length; the region size `|Λ|` appears nowhere — this replaces
the sibling's `M = |E(Λ)|`. Uniformity over a family of regions is at
fixed `J_* = sup_{Λ, b} ||h_b^{(Λ)}||`, `m`, observable norms, and
coordination — the supplied class fixes finite norms per region, so the
family-level `J_*` is a named hypothesis, not a consequence. (Gated: the
bond-count enumeration `≤ 6s` on exact small site sets; the product
values; the recurrence instance on the chain; and the actual
surviving-sequence counts below the bound.)

**W4 (volume-uniform per-coefficient bounds; upper bounds only).**
Iterating `||[P, Q]|| ≤ 2||P||·||Q||` (rebuilt in the sibling) along each
sequence and summing,

> `||[ad_H^k A, B]|| ≤ 2 ||A|| ||B|| (2J)^k N_k`,

with `N_k` as in W3 — volume-uniform at every order. Gated at `k = 2`
with exact norms on the three-site chain. The bound is an upper bound
and not an equality in a strong, exact sense — the chain exhibits an
order-parity breathing, gated exactly: the cone is reached at `k = 2`
(the `X_3` and `Y_3` probes register; `Z_3` is silent at the gated
orders `k = 2, 4`, the arriving factor being itself `Z_3`); at `k = 3` the entire site-3 component
cancels — every one of the eight sequences separately commutes with both
`X_3` and `Z_3`, hence with the full site-3 algebra they generate, a
complete support retreat; and at `k = 4` the commutator
re-arrives against `X_3` while `Z_3` stays silent. Coefficient
nonvanishing is probe- and order-dependent; only the bound is claimed.

**W5 (volume-uniform bound on an exact local time window).** Writing the
commutator's absolutely convergent Taylor series (finite matrices) and
bounding term `k` by `a_k = 2||A||||B|| (2J)^k N_k |t|^k / k!`: whenever
`a_k > 0`, the recurrence `N_{k+1} ≤ 6(m + k) N_k` gives

> `a_{k+1}/a_k ≤ 12 J |t| · (m + k)/(k + 1)`,

and `(m + k)/(k + 1)` is nonincreasing in `k` for every `m ≥ 1` (the
runner gates `(m + k)(k + 2) ≥ (m + k + 1)(k + 1)`, which reduces
exactly to `m ≥ 1`). The degenerate cases are handled separately: if
some `a_k = 0` then all later counts vanish and the tail is a finite
sum; at `t = 0` or `J = 0` the commutator bound is immediate. Hence for
`r := 12 J |t| (m + d)/(d + 1) < 1` — the certified sufficient window
`|t| < (d + 1) / (12 J (m + d))`, with `J` read as the family-level
`J_*` when comparing regions — the tail is dominated geometrically:

> `||[A_X(t), B_Y]|| ≤ a_d / (1 − r)`,

with `a_d` built from `m`, `J`, `d`, and the observable norms.
Uniform over region families at fixed `J_*`, `m`, observable norms, and
coordination, on the stated certified window; the window is fixed by the
same inventory. Beyond the window, the sibling's
region-level bound still applies; the all-time volume-uniform constant
remains open as named.

## No-Go Discipline Gate

W2's dead-sequence statement and the W4 parity exhibit are the bounded
negatives, answered:

- **N1 route inventory.** Against the parity exhibit: (1) change the
  probe at `k = 3` — every sequence commutes with both `X_3` and `Z_3`,
  hence with the whole site-3 algebra; no probe registers; ATTEMPTED and
  gated; (2) go one order higher — `k = 4` re-arrives against `X_3` and
  `Y_3`-type probes while `Z_3` stays silent; ATTEMPTED and gated; (3)
  orders beyond `k = 4` — named untested; the claim is only that bounds
  are not equalities at the gated orders; (4) change the Hamiltonian —
  the sibling's commuting chain stalls at every order by its collapse
  identity; a different mechanism, exhibited there; (5) longer-range or
  multi-site supplied terms — outside the nearest-neighbor bond class,
  named untested.
- **N2 wall independence:** the dead-sequence lemma is structural; the
  parity exhibit is an instance statement; neither implies the other.
- **N3 hidden-wall scan:** the `6s` bond count and the `+2` support
  growth are the nearest-neighbor class's exact local combinatorics,
  gated; the absolute-convergence step is the finite-matrix entire-series
  fact, note-carried as in the sibling; the `m ≥ 2` absorption is stated
  where used.
- **N4 residual matching and dependency roles:** the sibling supplies
  the class, L1, the norm inequality (rebuilt there), and the named open
  task this note partially takes; `minimal_axioms` supplies the
  no-dynamics boundary needle only.
- **N5 rhetoric audit:** "volume-uniform" is claimed for per-coefficient
  bounds at every order and for the commutator bound on the stated exact
  window only; the all-time statement is named open, not softened.
- **N6 partial-closure scan:** the walk-reorganization route and the
  sharp rate remain open; nothing here forecloses them.
- **N7 steelman:** "the window makes it useless." Reply: the window is
  local and exact, the per-coefficient bounds are unconditional in `t`,
  and the sibling's region-level bound covers all `t` — the pair of
  bounds brackets exactly what the open walk argument would unify.
- **N8 cross-cycle echo:** the sibling's exhibit-pair discipline is
  repeated (bound gated at a reaching instance; non-equality gated at an
  exact vanishing instance).

## Non-Claims

- Does **not** supply the all-time volume-uniform Lieb-Robinson
  constant, the walk reorganization, the sharp rate, the U-integrated
  statement, or any physical velocity; does **not** alter the sibling's
  scope.
- Does **not** claim coefficient nonvanishing at or above the cone
  (probe- and order-dependent, exhibited).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains required.

## Verification

The primary runner checks the listed identities and witnesses and
nothing more (sympy, exact arithmetic, single process; three- and
four-site instances, 8x8 and 16x16): the multinomial expansion at
`k = 2, 3` by full sequence enumeration; the dead-sequence gates
(inner-miss, later-miss); the sequence-by-sequence below-cone recovery;
the `6s` bond-count enumeration on exact site sets and the product-form
count values; the `k = 2` coefficient-bound norm computation; the
`k = 3` parity exhibit (all eight sequences vanish against the probe,
both the sum and each term); the term-ratio and monotonicity
inequalities in formal form; the geometric-tail closed form and an exact
window instance; and needle checks pinning the sibling's named-open
sentence, the axiom memo's no-dynamics sentence, and this note's claim
identifier and labels. Mutation checks (one load-bearing mutation per
check family, reverted) are recorded in the review history and PR body.

Measured runner total after final verification:
`TOTAL: PASS=19 FAIL=0`.
