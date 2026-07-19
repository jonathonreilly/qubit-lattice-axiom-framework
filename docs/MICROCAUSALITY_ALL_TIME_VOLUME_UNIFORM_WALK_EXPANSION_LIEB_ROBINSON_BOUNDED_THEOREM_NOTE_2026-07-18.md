---
claim_id: microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional, self-contained nearest-neighbor specialization for a supplied Hermitian two-site bond Hamiltonian on finite qubit-lattice regions. For nonempty disjoint supports X,Y, with J=0 when the bond set is empty, the note proves by Duhamel iteration on the immediately previous bond that ||[tau_t(A),B]|| <= 2||A||||B||(n_X/10) sum_{k>=d}(20J|t|)^k/k!, together with factorial and exponentially reweighted tails. The constants are independent of region volume for fixed local inputs; a family statement requires a finite uniform J_*. This is an explicit loose-constant specialization, not a novelty or closure claim over generic interaction-path Lieb-Robinson theorems. It neither constructs or controls the reconstructed many-body transfer Hamiltonian nor composes quasilocal tails, integrates over U, derives a sharp rate, selects dynamics, or supplies a physical velocity."
upstream_dependencies:
  - minimal_axioms
  - microcausality_many_body_nested_commutator_lightcone_bounded_theorem_note_2026-07-18
  - microcausality_volume_uniform_sequence_count_coefficient_bounds_bounded_theorem_note_2026-07-18
runner: scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py
---

# Microcausality: All-Time Volume-Uniform Walk-Expansion Lieb-Robinson Bound

**Date:** 2026-07-18
**Type:** bounded_theorem
**Claim type:** bounded_theorem
**Scope:** bridge-conditional; a self-contained nearest-neighbor specialization
on the supplied class and finite-matrix analysis context below. It is not a
novelty claim over generic interaction-path theorems. The axioms choose no
dynamics.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py`](../scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.txt)

## Purpose And Placement

The first sibling,
[`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md),
proves below-cone Taylor vanishing, disconnected-component locality, and a
deliberately coarse finite-volume factorial tail. The second,
[`MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md),
gives local Taylor-coefficient bounds and an explicit local time window. It
also records that stronger generic finite-range interaction-path bounds
already exist on repository source surfaces.

This note therefore claims no generic-path novelty or global open-task
closure. Its narrower purpose is to give a self-contained nearest-neighbor
specialization with one explicit, loose constant. The reorganization happens
at the Duhamel level: differentiating `[τ_t(A), B]`, reducing `[H, A]` to
bonds touching `supp(A)`, and applying Jacobi term-by-term produces an
inhomogeneity involving the evolved **bond** `[τ_s(h_b), B]`. Repeating the
same reduction for that bond makes each next bond adjacent to the immediately
**previous bond**, not the accumulated support. On `Z^3` the resulting bond
graph has degree `10`, so geometric walk counts divided by factorials converge
for every `t`, independently of the region volume for fixed local inputs.

The
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md)
memo is imported only for its explicit boundary that Admissibility supplies no
Hamiltonian, transfer operator, time metric, or physical persistence dynamics.
It supplies neither the Hamiltonian below nor a physical clock. Both are
outside the axiom content.

## Hypotheses (all supplied, none derived)

Let `Λ ⊂ Z^3` be finite, not necessarily connected, with induced
nearest-neighbor bond set `E(Λ)`. Let

> `H = Σ_{b∈E(Λ)} h_b`

be supplied, with every `h_b` Hermitian and supported on the two sites of `b`.
Define `J = max_b ||h_b||`, with the convention **`J = 0` when
`E(Λ) = ∅`**. Hermiticity is load-bearing because the transport generator
`H̃(t)` below must be self-adjoint.

Let `A` and `B` be supported on **nonempty** sets `X,Y ⊆ Λ`. A zero operator
may be assigned any nonempty support containing it. Assume
**`X ∩ Y = ∅`, equivalently `d ≥ 1`**, where `d = d_{Z^3}(X,Y)` is the
ambient cubic-lattice graph distance. This ambient distance is no greater
than the induced finite-region distance and is therefore conservative in the
reach lemma. Define

> `n_X = #{b ∈ E(Λ) : b ∩ X ≠ ∅} ≤ 6|X|`

and use the supplied Heisenberg convention
`τ_t(A) = e^{itH} A e^{−itH}`. The `d = 0` case is excluded because the
displayed prefactor need not dominate the initial overlapping-support
commutator. If `E(Λ)=∅`, or if no interaction component meets both supports,
the evolution is static across the separation and the commutator is zero.

For a family of finite regions, the phrase *volume-uniform* additionally
requires a finite `J_* = sup_{Λ,b} ||h_b^{(Λ)}||`, together with uniform
control of the displayed local inputs (`||A||`, `||B||`, and `n_X`, or a
fixed support-size bound). Finiteness of every individual region does not
imply this family hypothesis.

Declared finite-matrix analysis context (supplied, with the algebraic
identities below proved in the note and sampled by the runner): (i) existence,
unitarity, and termwise differentiability
of `e^{itH}`, giving `d/dt τ_t(A) = i[H, τ_t(A)]` (the siblings'
entire-series fact); (ii) existence of the time-ordered propagator
`V(t)` with `V'(t) = i H̃(t) V(t)`, `V(0) = 1`, for the continuous
bounded self-adjoint generator `H̃(t)` below (a finite-dimensional
linear ODE); (iii) continuity of `s ↦ ||[τ_s(h_b), B]||` and the Riemann
limit passage extending the finite-sum triangle inequality to integrals
(the finite-sum inequality itself is rebuilt in G2; only the
limit passage is supplied). No literature statement is load-bearing: the
Lieb-Robinson/Nachtergaele-Sims line is a **comparator class only**; the
proof below is self-contained and imports no literature theorem as a proof
step.

## Results

**G1 (algebraic kernel of the Duhamel step, exact).** Four identities,
each checked:

1. Jacobi rearrangement `[[P, Q], R] = [P, [Q, R]] − [Q, [P, R]]`
   (symbolic zero on generic matrix symbols).
2. Conjugation distributes over commutators,
   `M [P, Q] M^{−1} = [M P M^{−1}, M Q M^{−1}]` (symbolic zero), hence
   `τ_t([h_b, A]) = [τ_t(h_b), τ_t(A)]`.
3. Boundary reduction: `[H, O] = [H_{∂Z}, O]` for `O` supported on `Z`,
   with `H_{∂Z} = Σ_{b∩Z≠∅} h_b` — a bond missing `Z` acts on
   complementary tensor factors and commutes exactly (the first
   sibling's L1a mechanism, rechecked here on the three-site chain).
4. Self-term drop: `[h_b, h_b] = 0`, so for `O = h_b` the reduction
   sum runs over the **other** bonds touching `b` only.

Combining 1-4 with the supplied derivative fact, `f(t) := [τ_t(A), B]`
satisfies the inhomogeneous commutator flow

> `f'(t) = i[H̃(t), f(t)] − i Σ_{b∩X≠∅} [τ_t(A), [τ_t(h_b), B]]`,
> `H̃(t) := Σ_{b∩X≠∅} τ_t(h_b)`,

because `f'(t) = i[τ_t([H, A]), B] = i Σ_{b∩X≠∅} [[τ_t(h_b), τ_t(A)], B]`
by (2)-(3), and each summand rearranges by (1) with `P = τ_t(h_b)`,
`Q = τ_t(A)`, `R = B`.

**G2 (norm-transport lemma; identities checked, finite-sum triangle
rebuilt).** Let `f' = i[H̃(t), f] + R(t)` with `H̃(t)` self-adjoint,
and let `V` solve `V' = iH̃V`, `V(0) = 1`. Writing `W := V^†` (so
`W' = −iWH̃`, valid since `H̃^† = H̃`):

- *Unitarity is preserved:* `d/dt(WV) = W'V + WV' = −iWH̃V + iWH̃V = 0`
  (checked symbolically), so `V(t)` stays unitary.
- *Intertwiner:* `d/dt(W f V) = W' f V + W f' V + W f V' = W R V`
  (checked symbolically — the commutator part cancels exactly).
- Integrating **for `t ≥ 0`**, `W(t) f(t) V(t) = f(0) + ∫_0^t W R V ds`.
  Unitary invariance of the operator norm (checked at a rational
  orthogonal instance: conjugation preserves the spectrum of `M^†M`)
  and the triangle inequality for integrals give

  > `||f(t)|| ≤ ||f(0)|| + ∫_0^{t} ||R(s)|| ds`  (`t ≥ 0`).

  Negative times are **not** obtained by substituting `|t|` into this
  display (that would integrate `R` over the wrong side of `0`);
  they are obtained by the `H → −H` symmetry: `τ_{−t}^{H} = τ_{t}^{−H}`
  exactly (checked), the supplied class is invariant under `H → −H` with
  the same `J`, bonds, and walks, so every bound proved below for
  `t ≥ 0` holds verbatim for `−H` and therefore yields the `|t|` form
  of the final theorem. The `G3` instance additionally exhibits the
  symmetry concretely: its commutator norm is even in `t` (checked).

  The triangle inequality for integrals is used in its rebuilt finite
  form: for matrices, `||M_1 + M_2 + M_3|| ≤ ||M_1|| + ||M_2|| +
  ||M_3||` by iterated two-term subadditivity (checked at an exact
  instance with a strict-inequality witness); applying it to Riemann
  sums of the continuous integrand and passing to the limit (supplied
  context (iii)) yields `||∫ M|| ≤ ∫ ||M||`.
- The variation-of-constants identity behind this — `g(t) =
  V(t)(g(0) + ∫_0^t V^† R V ds)V(t)^†` solves `g' = i[H̃, g] + R` — is
  additionally checked end-to-end at an exact instance with rational
  spectrum and polynomial inhomogeneity.

**G3 (one-step Duhamel inequality).** Applying G2 to the flow in G1 and
bounding the inhomogeneity by `||[τ_t(A), [τ_t(h_b), B]]|| ≤ 2||A|| ·
||[τ_t(h_b), B]||` (unitary invariance `||τ_t(A)|| = ||A||` plus the
commutator norm bound `||[P, Q]|| ≤ 2||P||·||Q||`, rebuilt in the first
sibling and rechecked here):

> `||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| Σ_{b∩X≠∅} ∫_0^{t}
> ||[τ_s(h_b), B]|| ds`  (`t ≥ 0`; negative `t` via the checked
> `H → −H` symmetry of G2, giving the `|t|` forms below).

Checked on an exact stationary-bond instance: `Λ` two sites, `H = h =
J·X_1X_2`, `A = Z_1`, `B = Z_2`. There `[H, h] = 0` so `τ_s(h) = h`
exactly (checked), the right side is `4J|t|` exactly, and the left side is
`2|sin(2Jt)|` by the checked conjugation closed form
`e^{iθX_1X_2} Z_1 e^{−iθX_1X_2} = cos(2θ)Z_1 + sin(2θ)Y_1X_2`; the
inequality reduces to `|sin x| ≤ |x|` (elementary: `cos ≤ 1`
integrated; checked at exact instances `x = 1/2, 1, 3`).

**G4 (iteration = walk expansion).** The iteration does **not** reuse
G3's display verbatim with `A → h_b` (that display's sum includes the
bond itself). Instead the derivation is re-run for `f_b(s) :=
[τ_s(h_b), B]`, dropping the self term **before** the Jacobi step:
`[H, h_b] = Σ_{b'∩b≠∅, b'≠b} [h_{b'}, h_b]` by G1.3 **and** G1.4
(`[h_b, h_b] = 0`, checked with the reduced instance
`[H, h_12] = [h_23, h_12]`), so the flow is

> `f_b'(s) = i[H̃_b(s), f_b(s)] − i Σ_{b'∩b≠∅, b'≠b}
> [τ_s(h_b), [τ_s(h_{b'}), B]]`,
> `H̃_b(s) := Σ_{b'∩b≠∅, b'≠b} τ_s(h_{b'})`,

and G2 applies to it exactly as before. The new sum therefore runs over
bonds `b'` adjacent to `b` (`b' ∩ b ≠ ∅`, `b' ≠ b`) — the **previous
bond only**, not the accumulated support. No self-drop is used at the
first step, where `A` is generic and the sum over all `n_X` touching
bonds stands. Unrolling to depth `K` and
bounding every leftover integrand by the a priori bound
`||[τ_s(h_{b'}), B]|| ≤ 2J||B||` (G3's commutator bound plus
`||τ_s(h)|| = ||h||`):

> `||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| Σ_{k=1}^{K} (2J)^{k−1}
> Σ_{w∈𝒲_k} ||[h_{b_k}, B]|| · |t|^k/k! + ρ_K`,

where `𝒲_k` is the set of walks `w = (b_1, …, b_k)` with `b_1 ∩ X ≠ ∅`,
`b_{j+1} ∩ b_j ≠ ∅`, `b_{j+1} ≠ b_j`, the iterated integrals
`∫_0^{|t|}∫_0^{s_1}···ds = |t|^k/k!` are exact (checked at `k = 3`), and

> `ρ_K ≤ 2||A|| (2J)^K |𝒲_{K+1}| · 2J||B|| · |t|^{K+1}/(K+1)! → 0`

as `K → ∞` for every fixed `t` (geometric-over-factorial; ratio checked).
The depth-2 assembly is additionally checked as an exact algebraic
identity, and the monotonicity step (integrating a pointwise-smaller
polynomial majorant) is checked on an exact instance. By G1.3, the base
term `||[h_{b_k}, B]||` vanishes unless `b_k ∩ Y ≠ ∅` and is otherwise
`≤ 2J||B||`; and `||[A, B]|| = 0` since `d ≥ 1` gives disjoint supports.

**G5 (exact walk combinatorics on `Z^3`).** All enumerated exactly:

- Bonds incident to one site: exactly `6`, so `n_X ≤ 6|X|`.
- Bond-adjacency degree: every bond of `Z^3` has exactly `10` adjacent
  bonds (`6 + 6 − 2`), enumerated and box-stable (two box sizes).
- Walk counts: `|𝒲_k| ≤ n_X · 10^{k−1}` — first bond at most `n_X`
  choices, each later bond at most `10`. Exact instances: for
  single-site `X`, `|𝒲_2| = 60 = 6·10` exactly, and each start bond
  admits exactly `100 = 10^2` length-3 continuations (a length-`k` walk
  has `k − 1` adjacency steps).
- Reach lemma: the sites of `b_j` lie within `Z^3`-distance `j` of `X`
  (induction: `b_1` touches `X`; each next bond shares a site with the
  previous one), so a walk with `b_k ∩ Y ≠ ∅` needs `k ≥ d`. Sharp at
  the checked `d = 3` instance: no walk of length `≤ 2` touches `Y`, and
  a length-3 walk does. Walks in `E(Λ)` are walks in `E(Z^3)` and the
  `Z^3` distance lower-bounds the induced distance, so both the count
  and the reach constraint transfer conservatively to every `Λ`.

**G6 (theorem: all-time volume-uniform Lieb-Robinson bound).** Under
the standing hypothesis `X ∩ Y = ∅` (`d ≥ 1`), feeding
G5 into G4 and using the coefficient identity `(2J)^k · n_X · 10^{k−1}
= (n_X/10)(20J)^k` (checked symbolically):

> `||[τ_t(A), B]|| ≤ 2||A|| ||B|| (n_X/10) Σ_{k≥d} (20J|t|)^k / k!`
> `≤ 2||A|| ||B|| (n_X/10) · ((20J|t|)^d / d!) · e^{20J|t|}`,

for all `t` and every finite `Λ`, with constants depending only on
`||A||`, `||B||`, `n_X ≤ 6|X|`, `J`, and `d` — **not** on `|Λ|`. For a
family, replacing `J` by a finite uniform `J_*` and uniformly controlling
the other displayed local inputs gives the corresponding family-uniform
bound; no such uniform `J_*` is inferred from finite-volume hypotheses. The
tail lemma `Σ_{k≥d} x^k/k! ≤ (x^d/d!)e^x` is re-derived from
`d!/k! ≤ 1/(k−d)!` (binomial `≥ 1`; the first sibling's mechanism,
rechecked with an exact partial-sum instance). Cone readout, stated at two strengths with `x := 20J|t|` (the
**walk-series activity scale** — deliberately not called a velocity):

- *Monotone decrease:* once `d > x` the successive-term ratio
  `x/(d+1) < 1` (checked), so the majorant decreases as `d` grows. This
  alone is **not** an exponential-decay statement — at `d` slightly
  above `x` the majorant is still enormous.
- *Exponential form:* reweighting
  the tail termwise by `x^k/k! = e^{−μk}(xe^μ)^k/k!` (identity checked
  symbolically) and using `e^{−μk} ≤ e^{−μd}` for `k ≥ d` (reduces to
  the exponent comparison `μk ≥ μd`, checked symbolically, plus
  monotonicity of `exp` — declared context, checked at exact instances)
  gives, for every `μ > 0`,

  > `Σ_{k≥d} x^k/k! ≤ e^{−μd + x e^μ}`,

  so the bound decays exponentially in `d` at fixed `t`, with the
  `μ = 1` readout: decay `e^{−d}` once `d > e·x`, i.e. a
  Lieb-Robinson-type velocity bound `v ≤ 20eJ` in site units. An
  explicit large-`d` smallness certificate is also checked in exact
  integer arithmetic (`e < 3`, so at `J = 1`, `t = 10`, `d = 800` the
  tail factor obeys `3^200 · 200^800/800! < 10^{−40}`).

Neither `20J` nor `20eJ` is claimed sharp.

**G7 (placement relative to the sibling certificates and live residuals).**
The comparison is descriptive, not a novelty or priority claim:

- Block01's displayed factorial-tail constant is region-level,
  `c = 2J|E(Λ)|`; G6 gives an explicit nearest-neighbor specialization whose
  constant is free of `|E(Λ)|` for fixed local inputs.
- Block02 retains a sharper Taylor-coefficient statement and a certified
  local window that this note does not reproduce. G6 instead gives one loose
  all-time function-level majorant. No ordering between the two numerical
  bounds is claimed inside block02's window.
- Stronger generic finite-range interaction-path theorems already exist on
  repository source surfaces. This note is only a self-contained specialization
  with transparent constants. The live physical residual is construction and
  control of the reconstructed many-body transfer Hamiltonian in a matching
  finite or quasilocal class, followed by quasilocal-tail composition. The
  `U`-integrated and sharp-rate steps remain separate.

## No-Go Discipline Gate

**Status: PASS.** The narrow classification is
`bounded-with-corrected-wall-count`: G1-G7 prove a specialization for a
supplied nearest-neighbor bond Hamiltonian. Generic interaction-path counting
is not an open wall. Physical reuse still requires the distinct residuals
listed in N2.

**N1 — alternative attacks and routes.**

| Route | Marker | Current-cycle result and source status |
|---|---|---|
| Invoke a generic interaction-path Lieb-Robinson theorem and treat G6 as new generic closure | ATTEMPTED | Direct comparison in this cycle shows that such a theorem would defeat novelty, not the narrower self-contained specialization proved in G1-G7. The [sequence-count sibling](MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md) is contextual corroboration only: its tracked status is `bounded_theorem / unaudited / unaudited`, so it is not used as retained authority. |
| Derive the supplied Hamiltonian or physical clock from Admissibility | RULED OUT BY PRIOR | [`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) explicitly supplies neither a Hamiltonian/transfer operator nor a time metric or physical persistence dynamics. Its tracked status is `meta / unaudited / meta`, and it is the registered axiom-source authority for this limited negative boundary. |
| Use the earlier finite-range bridge as automatic placement of the exact reconstructed many-body `H` | ATTEMPTED | Source-scope inspection in this cycle finds that [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md) makes quasilocal reuse conditional rather than placing this exact many-body `H`. Its tracked status is `bounded_theorem / unaudited / unaudited`; the inspection tests this route but does not promote the source to retained authority. |
| Use the spatial-cluster path theorem to bypass transfer-H construction/control | ATTEMPTED | Source-scope inspection in this cycle finds that [`SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md`](SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md) assumes a local Hamiltonian satisfying its range, norm, and degree conditions; it does not construct the reconstructed many-body transfer Hamiltonian. Its tracked status is `bounded_theorem / unaudited / unaudited`, so only its stated hypothesis mismatch is used here. |
| Promote the free-bilinear quasilocal closure to the interacting many-body sector | ATTEMPTED | Source-scope inspection in this cycle finds that [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md) restricts its exact-log kernel and quasilocal LR composition to the free bilinear sector. Its tracked status is `bounded_theorem / unaudited / unaudited`; the sector mismatch is tested without treating that source as retained authority. |
| Read the all-time supplied-`H` bound as already `U`-integrated or sharp | ATTEMPTED | Direct inspection of G1-G7 in this cycle finds neither a `U` integral nor an optimization theorem. [`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md) is non-authoritative context with tracked status `bounded_theorem / unaudited / unaudited`; it is not needed for the self-contained result. |

**N2 — premise and residual independence.** The theorem premises are `P1`,
finite tensor-product algebra with nonempty disjoint supports; `P2`, a supplied
Hermitian nearest-neighbor two-site bond decomposition; and `P3`, the supplied
Heisenberg convention plus finite-matrix ODE context. `J` is the norm maximum
derived from `P2`, with the empty-set convention `J=0`; it is not counted as an
independent premise.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| `P1/P2` | no | no | yes |
| `P1/P3` | no | no | yes |
| `P2/P3` | no | no | yes |

For physical reuse the residuals are `R1`, construction and placement/control
of the reconstructed many-body transfer Hamiltonian in a matching interaction
class; `R2`, composition of its quasilocal tails with an LR estimate; `R3`,
the `U`-integrated statement; and `R4`, a sharp-rate theorem.

| Pair | First closes second? | Second closes first? | Independent? |
|---|---|---|---|
| `R1/R2` | no | no | yes |
| `R1/R3` | no | no | yes |
| `R1/R4` | no | no | yes |
| `R2/R3` | no | no | yes |
| `R2/R4` | no | no | yes |
| `R3/R4` | no | no | yes |

The generic interaction-path theorem is excluded from this residual table
because current repository sources already contain that mechanism.

**N3 — hidden-condition scan.** A phrase-by-phrase reread found the following
potential hiding places; each is classified here rather than left implicit.

| Phrase or close variant | Classification |
|---|---|
| “supplied class” / “declared finite-matrix context” | Explicit theorem conditions `P1-P3`, not axiom consequences. |
| “by the boundary reduction” / “by Jacobi” | Proved algebraic steps G1-G4, not external imports. |
| “comparator class only” | Non-load-bearing context; no literature theorem is used in the proof. |
| “volume-uniform” | Individual-region constants omit `|Λ|`; a family reading separately requires finite `J_*` and uniform local inputs. |
| empty bond set, disconnected interaction components, or zero operators | `J=0` on an empty bond set; disconnected evolution is static across supports; zero operators may be assigned nonempty supports. |
| support distance | `X` and `Y` are explicitly nonempty and disjoint, so ambient `Z^3` distance is defined and `d≥1`. |

The searches for “we assume,” “by construction,” “as is standard,” “the
framework provides,” “bridge context,” “background,” “naturally,”
“obviously,” “standard QFT,” “registered,” and “canonical” reveal no further
load-bearing premise. Finite-matrix exponential/ODE existence and the Riemann
limit passage are stated explicitly in Hypotheses.

**N4 — residual matching and dependency roles.**

| Witness | Witness residual | Role or residual used here | Match? |
|---|---|---|---|
| [Current sequence-count sibling, Purpose and N4-N8](MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md) | Generic path results exist; transfer-H placement/control plus tail composition remain | G6 is only a specialization; `R1-R2` remain | yes |
| [Minimal axioms, downstream-boundary section](MINIMAL_AXIOMS_2026-06-29.md) | No Hamiltonian, transfer operator, clock, or dynamics supplied | Prevents reading `P2-P3` as axiom-derived | yes |
| [Finite-range bridge, F5](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md) | Strict finite-range exact-log carrier fails; quasilocal reuse is conditional | `R1-R2` | yes |
| [Spatial-cluster LR note, honest scope and Lemma C](SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md) | Generic path counting under supplied local-interaction hypotheses | Prior generic mechanism; no novelty claim | yes |
| [Free-bilinear quasilocal bridge, B3](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md) | Free-bilinear exact-log sector only | Interacting many-body `R1-R2` | no — excluded as a witness of many-body closure; retained only as a partial-closure example in N6/N8 |
| [Gauged Combes-Thomas note, no-go boundary](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md) | Fixed-background single-particle quasilocality; many-body, `U`, and sharp-rate tasks separate | `R1`, `R3`, `R4` remain distinct | yes |

**N5 — rhetoric by resolution.**

| Resolution | What is actually established |
|---|---|
| per bond | `||h_b||≤J`; the recursion drops the self bond and moves only to a bond adjacent to the immediately previous bond. |
| per site/support | At most six initial bonds per site and ten later neighbors; the bound carries `n_X≤6|X|`. |
| per finite volume | G6 holds for every finite `Λ`, including boundary-truncated and disconnected regions, with no `|Λ|` in the constant. |
| family of volumes | Uniform only with finite `J_*` and uniform control of the displayed local inputs; individual finiteness is insufficient. |
| supplied interaction class | Nearest-neighbor Hermitian two-site bond terms in finite tensor-product algebras only; no generic multi-site constant is hidden in `10`. |
| physical transfer reuse | Not established: `R1-R3` remain, and `20J`/`20eJ` are not physical speeds. |

Thus “all-time volume-uniform” has only the per-volume/family-conditional
meaning above. It does not mean axiom-derived dynamics, universal interaction
class, physical propagation, or a sharp velocity.

**N6 — primitive, convention, reframe, and partial-closure scan.** The
[`axiom_premise_nodes.json`](audit/data/axiom_premise_nodes.json) registry and
[`premise_decision_history.json`](audit/data/premise_decision_history.json)
contain no Hamiltonian or dynamics primitive that chain-satisfies `P2-P3` or
`R1`. The approved kinetic-isotropy primitive supplies only a structural
kinetic-form ratio, not dynamics or a transfer Hamiltonian. The
[`CONTROLLED_VOCABULARY.md`](repo/CONTROLLED_VOCABULARY.md) and convention
history contain no labeling-only reframe that constructs a physical generator;
therefore this residual is not misclassified as “new axiom required.” No new
axiom is requested.

Prior partial closures are material and are listed explicitly without treating
their source-authored statements as retained authority:

- [`MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md)
  — status `bounded_theorem / unaudited / unaudited`; its stated generic
  path-counting comparison would close only the generic-mechanism part, not
  transfer-H construction or the physical reuse residuals.
- [`MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md`](MICROCAUSALITY_FINITE_RANGE_H_AND_VLR_BRIDGE_THEOREM_NOTE_2026-05-09.md)
  — status `bounded_theorem / unaudited / unaudited`; its stated finite-range
  bridge and quasilocal reframe would partially narrow `R1-R2` if independently
  validated.
- [`SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md`](SPATIAL_CLUSTER_DECOMPOSITION_LIEB_ROBINSON_REAL_NOTE_2026-05-19.md)
  — status `bounded_theorem / unaudited / unaudited`; its stated generic
  interaction-graph path counting would close only the generic-mechanism part,
  not transfer-H construction.
- [`FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md`](FREE_BILINEAR_QUASILOCAL_LR_BRIDGE_THEOREM_NOTE_2026-06-10.md)
  — status `bounded_theorem / unaudited / unaudited`; its stated free-bilinear
  composition would close quasilocal LR composition only in that restricted
  sector.
- [`GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md`](GAUGED_LOG_TRANSFER_QUASILOCALITY_COMBES_THOMAS_NARROW_THEOREM_NOTE_2026-06-13.md)
  — status `bounded_theorem / unaudited / unaudited`; its stated
  fixed-background single-particle quasilocality would close only that carrier.

These unaudited surfaces identify partial-closure paths but do not supply
retained closure. The present G1-G7 proof independently removes generic
nearest-neighbor path counting from this note's wall set; none of the cited
restricted carriers is silently upgraded to the reconstructed interacting
many-body Hamiltonian.

**N7 — hostile steelman.** A hostile reviewer can correctly argue that the
generic Duhamel/interaction-path theorem already exists in repository source,
so G1-G7 are a looser nearest-neighbor corollary rather than a new theorem of
the field; a finite matrix runner also cannot prove the universal recursion.
That argument defeats novelty, global closure, and theorem-by-computation
readings. It does not defeat the note-carried algebraic proof under `P1-P3`.
Accordingly the artifact is retained only as a self-contained explicit-constant
specialization, and the runner is described as sampled corroboration rather
than proof replacement.

**N8 — cross-cycle echo.** A repo-wide scan, including prior microcausality
notes and physics-loop no-go ledgers, found three directly similar wall shapes:

| Earlier wall | Later disposition and mechanism | Application here |
|---|---|---|
| Generic all-time finite-range path counting was treated as absent on early local certificates | Retired by self-contained interaction-graph/Duhamel path counting in the spatial-cluster and related sources | Generic counting is not claimed open or new here. |
| Exact reconstructed `H` was assumed strictly finite range | Falsified on the bilinear sector and reframed to quasilocal tails in the finite-range bridge | The same quasilocal reframe narrows `R1-R2`; it does not remove the need to control the many-body carrier. |
| Transfer-H/LR composition was open in the free exact-log sector | Retired there by an explicit exponentially decaying kernel and weighted path sum | This is the strongest candidate mechanism for `R1-R2`, but the free-sector kernel authority does not extend automatically to interacting many-body dynamics. |

The convention and premise histories show examples of walls retired by
ratification or reframe, but none turns an unspecified physical Hamiltonian
into a supplied generator. The applicable reframe—finite range to
quasilocality—is therefore carried forward rather than dismissed.

## Non-Claims

- Does **not** claim the scale `20J` or the readout `20eJ` is sharp,
  and does **not** supply transfer-H construction/control, quasilocal-tail
  composition, the `U`-integrated statement, or any physical velocity.
- Does **not** cover `d = 0` (overlapping supports) — excluded by
  hypothesis, with an exact counterexample showing why the displayed
  prefactor cannot simply be extended to that case.
- Does **not** claim numerical smallness inside the cone, nor that this
  bound is numerically smaller than block02's inside its window.
- Does **not** replace block02's per-coefficient bounds (they are
  coefficient-level statements this note does not reproduce).
- Does **not** claim novelty or priority over existing generic
  interaction-path Lieb-Robinson theorems.
- Does **not** assert family-uniformity without finite `J_*` and uniform local
  inputs.
- Does **not** select dynamics; the linked minimal-axiom memo supplies none.
- Does **not** set an audit verdict; independent audit remains required.

## Verification

Primary runner:
[`scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py`](../scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py)
— sympy-exact and enumeration-exact throughout. Checks are of two
honestly distinguished kinds: **symbolic identity checks** (Jacobi,
conjugation, intertwiner, unitarity, coefficient assembly, μ-reweighting,
and the remainder ratio) and **exact finite-instance checks**
(variation-of-constants, triangle inequality, stationary-bond dynamics,
walk enumeration, boundary cases, tail arithmetic, and a three-site
two-step reach coefficient).

The three-site recursion check independently compares the derivative of
`[τ_t(h_12),B]` at `t=0` with the previous-bond Jacobi flow. One reproducible
mutation then adds the forbidden self bond to the inhomogeneous sum while
leaving the reduced homogeneous generator unchanged; the mutated identity is
nonzero and is rejected. This is a single named mutation, not a mutation
battery. The runner also checks the exact first-zero/second-nonzero finite-chain
Taylor coefficients against the displayed `k=2` walk majorant and checks the
empty-bond/disconnected static boundary.

These checks corroborate specific proof steps; they do not prove the universal
Duhamel recursion or replace the note-carried derivation. The runner has no
mutable note inputs or prose-presence checks, so its committed cache depends
only on the runner source and exact deterministic output. It prints one
`PASS`/`FAIL` line per check and a final total.
