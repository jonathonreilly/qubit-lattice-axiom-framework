---
claim_id: microcausality_all_time_volume_uniform_walk_expansion_lieb_robinson_bounded_theorem_note_2026-07-18
claim_type: bounded_theorem
claim_scope: "Bridge-conditional closure of the family's named open task on the same supplied finite-range class (axioms supply no dynamics; same declared algebra and Heisenberg convention as the siblings, Hermitian bond terms, plus the declared finite-matrix ODE context stated in Hypotheses), under the standing hypothesis X ∩ Y = ∅ (d ≥ 1, with the necessity of the exclusion gated by an exact d = 0 counterexample): (G1) the algebraic kernel of the Duhamel step — Jacobi rearrangement, conjugation-commutator distribution, the boundary reduction [H, O] = [H_∂supp(O), O], and the self-term drop [h, h] = 0 — each identity gated symbolically or at exact instances as marked; (G2) the directed-time norm-transport lemma ||f(t)|| ≤ ||f(0)|| + ∫_0^t ||R|| (t ≥ 0) for f' = i[H̃(t), f] + R(t), with the intertwiner and unitarity computations gated symbolically, the variation-of-constants identity gated end-to-end at an exact rational-spectrum instance, the finite-sum triangle inequality rebuilt and gated, and negative times obtained by the gated H → −H symmetry, never by |t| substitution; (G3) the one-step Duhamel inequality ||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| Σ_{b∩X≠∅} ∫_0^t ||[τ_s(h_b), B]|| ds (t ≥ 0), gated on an exact stationary-bond instance with even-in-t norm; (G4) the iteration into bond-adjacency walks — the derivation re-run per bond with the self term dropped BEFORE the Jacobi step, so each next bond is adjacent to the PREVIOUS bond, not the accumulated support — with the depth-2 assembly identity and the vanishing remainder gated; (G5) the exact walk combinatorics on Z^3: bonds per site = 6, bond-adjacency degree = 10 (enumerated, box-stable), walks of length k from X counted by n_X·10^(k−1) (all six start bonds checked), and the reach lemma with a sharp d = 3 instance; (G6) the all-time volume-uniform Lieb-Robinson bound ||[τ_t(A), B]|| ≤ 2||A||||B||(n_X/10) Σ_{k≥d} (20J|t|)^k/k! ≤ 2||A||||B||(n_X/10)((20J|t|)^d/d!)e^{20J|t|}, constants free of |Λ|, with the tail lemma re-derived, the term-ratio monotone-decrease statement kept separate from exponential decay, the μ-reweighted exponential tail bound Σ_{k≥d} x^k/k! ≤ e^{−μd + xe^μ} (a review-lens contribution, adopted and gated) giving the μ = 1 velocity-type readout 20eJ, and an explicit large-d smallness certificate gated in exact integer arithmetic; (G7) strict-extension exhibits against both siblings' certificates (block01's constant is region-level 2J·|E(Λ)|; block02's window at the instance is 1/12, while this bound is finite at every t — broader time domain, no within-window smallness claim). Neither 20J (walk-series activity scale) nor 20eJ is claimed sharp; the sharp rate, the U-integrated statement, and the fermionic transfer bridge remain open; nothing physical is selected."
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
**Scope:** bridge-conditional; same supplied class, algebra, and
Heisenberg convention as the siblings, plus the declared finite-matrix
ODE context in Hypotheses; the axioms choose no dynamics.
**Audit-status authority:** independent audit lane only. This note sets no
audit verdict and predicts none.
**Primitive status:** no primitive is approved, registered, edited, or
enlarged here.
**Primary runner:**
[`scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py`](../scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py)
**Runner cache:**
[`logs/runner-cache/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.txt`](../logs/runner-cache/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.txt)

## Purpose

Both siblings name the same open task. The first,
[`MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_MANY_BODY_NESTED_COMMUTATOR_LIGHTCONE_BOUNDED_THEOREM_NOTE_2026-07-18.md),
proved below-cone Taylor vanishing and an all-time bound whose constant
`c = 2J·|E(Λ)|` is region-level. The second,
[`MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md`](MICROCAUSALITY_VOLUME_UNIFORM_SEQUENCE_COUNT_COEFFICIENT_BOUNDS_BOUNDED_THEOREM_NOTE_2026-07-18.md),
made the constants local but only on a finite time window, and stated
why: at the Taylor-coefficient level the count is genuinely
accumulated-support — "the pair of bounds brackets exactly what the open
walk argument would unify". This note supplies that walk argument. The
reorganization happens at the Duhamel level, not the coefficient level:
differentiating `[τ_t(A), B]`, reducing `[H, A]` to the bonds touching
`supp(A)`, and applying the Jacobi identity term-by-term produces an
inhomogeneous commutator flow whose inhomogeneity involves the evolved
**bond** `[τ_s(h_b), B]` — a fixed two-site object — rather than the
growing operator. Iterating on the bond replaces accumulated-support
sequences by walks on the bond-adjacency graph, each next bond adjacent
to the **previous bond** only. On `Z^3` that graph has degree exactly
`10`, so the walk count is geometric, and geometric-over-factorial
converges for every `t`, volume-uniformly. The result is the family's
all-time volume-uniform Lieb-Robinson bound with rate constant `20J` —
explicitly **not** claimed sharp.

## Hypotheses (all supplied, none derived)

Same supplied surface as the siblings: a finite region `Λ ⊂ Z^3` with
its induced nearest-neighbor bond set `E(Λ)`; a supplied bond
Hamiltonian `H = Σ_{b∈E(Λ)} h_b` with each `h_b` Hermitian (the first
sibling's declaration, load-bearing here: it makes the generator
`H̃(t)` below self-adjoint, which G2 requires) and `J = max_b ||h_b||`; observables
`A` supported on `X ⊆ Λ` and `B` supported on `Y ⊆ Λ` with
**`X ∩ Y = ∅`, equivalently `d ≥ 1` — required throughout** (the `d = 0`
overlapping case is excluded by hypothesis, and the runner exhibits why
the exclusion is necessary: at `d = 0` the bound's right side can fall
below `||[A, B]||` itself); `d = d(X, Y)`
the `Z^3` graph distance (a lower bound for the `Λ`-induced distance,
hence conservative in the reach lemma); `n_X = #{b ∈ E(Λ) : b ∩ X ≠ ∅}
≤ 6·|X|`; the Heisenberg convention `τ_t(A) = e^{itH} A e^{−itH}`. The
axioms supply no dynamics (needled); `H` is a supplied object of the
declared class, so every statement is bridge-conditional exactly as in
the siblings.

Declared finite-matrix analysis context (supplied, with every algebraic
identity gated): (i) existence, unitarity, and termwise differentiability
of `e^{itH}`, giving `d/dt τ_t(A) = i[H, τ_t(A)]` (the siblings'
entire-series fact); (ii) existence of the time-ordered propagator
`V(t)` with `V'(t) = i H̃(t) V(t)`, `V(0) = 1`, for the continuous
bounded self-adjoint generator `H̃(t)` below (a finite-dimensional
linear ODE); (iii) continuity of `s ↦ ||[τ_s(h_b), B]||` and the Riemann
limit passage extending the finite-sum triangle inequality to integrals
(the finite-sum inequality itself is rebuilt and gated in G2; only the
limit passage is supplied). No literature statement is load-bearing: the
Lieb-Robinson/Nachtergaele-Sims line is a **comparator class only**; the
proof below is self-contained and every load-bearing identity is gated.

## Results

**G1 (algebraic kernel of the Duhamel step, exact).** Four identities,
each gated:

1. Jacobi rearrangement `[[P, Q], R] = [P, [Q, R]] − [Q, [P, R]]`
   (symbolic zero on generic matrix symbols).
2. Conjugation distributes over commutators,
   `M [P, Q] M^{−1} = [M P M^{−1}, M Q M^{−1}]` (symbolic zero), hence
   `τ_t([h_b, A]) = [τ_t(h_b), τ_t(A)]`.
3. Boundary reduction: `[H, O] = [H_{∂Z}, O]` for `O` supported on `Z`,
   with `H_{∂Z} = Σ_{b∩Z≠∅} h_b` — a bond missing `Z` acts on
   complementary tensor factors and commutes exactly (the first
   sibling's L1a mechanism, re-gated here on the three-site chain).
4. Self-term drop: `[h_b, h_b] = 0`, so for `O = h_b` the reduction
   sum runs over the **other** bonds touching `b` only.

Combining 1-4 with the supplied derivative fact, `f(t) := [τ_t(A), B]`
satisfies the inhomogeneous commutator flow

> `f'(t) = i[H̃(t), f(t)] − i Σ_{b∩X≠∅} [τ_t(A), [τ_t(h_b), B]]`,
> `H̃(t) := Σ_{b∩X≠∅} τ_t(h_b)`,

because `f'(t) = i[τ_t([H, A]), B] = i Σ_{b∩X≠∅} [[τ_t(h_b), τ_t(A)], B]`
by (2)-(3), and each summand rearranges by (1) with `P = τ_t(h_b)`,
`Q = τ_t(A)`, `R = B`.

**G2 (norm-transport lemma; identities gated, finite-sum triangle
rebuilt).** Let `f' = i[H̃(t), f] + R(t)` with `H̃(t)` self-adjoint,
and let `V` solve `V' = iH̃V`, `V(0) = 1`. Writing `W := V^†` (so
`W' = −iWH̃`, valid since `H̃^† = H̃`):

- *Unitarity is preserved:* `d/dt(WV) = W'V + WV' = −iWH̃V + iWH̃V = 0`
  (gated symbolically), so `V(t)` stays unitary.
- *Intertwiner:* `d/dt(W f V) = W' f V + W f' V + W f V' = W R V`
  (gated symbolically — the commutator part cancels exactly).
- Integrating **for `t ≥ 0`**, `W(t) f(t) V(t) = f(0) + ∫_0^t W R V ds`.
  Unitary invariance of the operator norm (gated at a rational
  orthogonal instance: conjugation preserves the spectrum of `M^†M`)
  and the triangle inequality for integrals give

  > `||f(t)|| ≤ ||f(0)|| + ∫_0^{t} ||R(s)|| ds`  (`t ≥ 0`).

  Negative times are **not** obtained by substituting `|t|` into this
  display (that would integrate `R` over the wrong side of `0`);
  they are obtained by the `H → −H` symmetry: `τ_{−t}^{H} = τ_{t}^{−H}`
  exactly (gated), the supplied class is invariant under `H → −H` with
  the same `J`, bonds, and walks, so every bound proved below for
  `t ≥ 0` holds verbatim for `−H` and therefore yields the `|t|` form
  of the final theorem. The `G3` instance additionally exhibits the
  symmetry concretely: its commutator norm is even in `t` (gated).

  The triangle inequality for integrals is used in its rebuilt finite
  form: for matrices, `||M_1 + M_2 + M_3|| ≤ ||M_1|| + ||M_2|| +
  ||M_3||` by iterated two-term subadditivity (gated at an exact
  instance with a strict-inequality witness); applying it to Riemann
  sums of the continuous integrand and passing to the limit (supplied
  context (iii)) yields `||∫ M|| ≤ ∫ ||M||`.
- The variation-of-constants identity behind this — `g(t) =
  V(t)(g(0) + ∫_0^t V^† R V ds)V(t)^†` solves `g' = i[H̃, g] + R` — is
  additionally gated end-to-end at an exact instance with rational
  spectrum and polynomial inhomogeneity.

**G3 (one-step Duhamel inequality).** Applying G2 to the flow in G1 and
bounding the inhomogeneity by `||[τ_t(A), [τ_t(h_b), B]]|| ≤ 2||A|| ·
||[τ_t(h_b), B]||` (unitary invariance `||τ_t(A)|| = ||A||` plus the
commutator norm bound `||[P, Q]|| ≤ 2||P||·||Q||`, rebuilt in the first
sibling and re-gated here):

> `||[τ_t(A), B]|| ≤ ||[A, B]|| + 2||A|| Σ_{b∩X≠∅} ∫_0^{t}
> ||[τ_s(h_b), B]|| ds`  (`t ≥ 0`; negative `t` via the gated
> `H → −H` symmetry of G2, giving the `|t|` forms below).

Gated on an exact stationary-bond instance: `Λ` two sites, `H = h =
J·X_1X_2`, `A = Z_1`, `B = Z_2`. There `[H, h] = 0` so `τ_s(h) = h`
exactly (gated), the right side is `4J|t|` exactly, and the left side is
`2|sin(2Jt)|` by the gated conjugation closed form
`e^{iθX_1X_2} Z_1 e^{−iθX_1X_2} = cos(2θ)Z_1 + sin(2θ)Y_1X_2`; the
inequality reduces to `|sin x| ≤ |x|` (elementary: `cos ≤ 1`
integrated; gated at exact instances `x = 1/2, 1, 3`).

**G4 (iteration = walk expansion).** The iteration does **not** reuse
G3's display verbatim with `A → h_b` (that display's sum includes the
bond itself). Instead the derivation is re-run for `f_b(s) :=
[τ_s(h_b), B]`, dropping the self term **before** the Jacobi step:
`[H, h_b] = Σ_{b'∩b≠∅, b'≠b} [h_{b'}, h_b]` by G1.3 **and** G1.4
(`[h_b, h_b] = 0`, gated with the reduced instance
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
`∫_0^{|t|}∫_0^{s_1}···ds = |t|^k/k!` are exact (gated at `k = 3`), and

> `ρ_K ≤ 2||A|| (2J)^K |𝒲_{K+1}| · 2J||B|| · |t|^{K+1}/(K+1)! → 0`

as `K → ∞` for every fixed `t` (geometric-over-factorial; ratio gated).
The depth-2 assembly is additionally gated as an exact algebraic
identity, and the monotonicity step (integrating a pointwise-smaller
polynomial majorant) is gated on an exact instance. By G1.3, the base
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
  the gated `d = 3` instance: no walk of length `≤ 2` touches `Y`, and
  a length-3 walk does. Walks in `E(Λ)` are walks in `E(Z^3)` and the
  `Z^3` distance lower-bounds the induced distance, so both the count
  and the reach constraint transfer conservatively to every `Λ`.

**G6 (theorem: all-time volume-uniform Lieb-Robinson bound).** Under
the standing hypothesis `X ∩ Y = ∅` (`d ≥ 1`), feeding
G5 into G4 and using the coefficient identity `(2J)^k · n_X · 10^{k−1}
= (n_X/10)(20J)^k` (gated symbolically):

> `||[τ_t(A), B]|| ≤ 2||A|| ||B|| (n_X/10) Σ_{k≥d} (20J|t|)^k / k!`
> `≤ 2||A|| ||B|| (n_X/10) · ((20J|t|)^d / d!) · e^{20J|t|}`,

for all `t` and every finite `Λ`, with constants depending only on
`||A||`, `||B||`, `n_X ≤ 6|X|`, `J`, and `d` — **not** on `|Λ|`. The
tail lemma `Σ_{k≥d} x^k/k! ≤ (x^d/d!)e^x` is re-derived from
`d!/k! ≤ 1/(k−d)!` (binomial `≥ 1`; the first sibling's mechanism,
re-gated with an exact partial-sum instance). Cone readout, stated at two strengths with `x := 20J|t|` (the
**walk-series activity scale** — deliberately not called a velocity):

- *Monotone decrease:* once `d > x` the successive-term ratio
  `x/(d+1) < 1` (gated), so the majorant decreases as `d` grows. This
  alone is **not** an exponential-decay statement — at `d` slightly
  above `x` the majorant is still enormous.
- *Exponential form (review-lens contribution, adopted):* reweighting
  the tail termwise by `x^k/k! = e^{−μk}(xe^μ)^k/k!` (identity gated
  symbolically) and using `e^{−μk} ≤ e^{−μd}` for `k ≥ d` (reduces to
  the exponent comparison `μk ≥ μd`, gated symbolically, plus
  monotonicity of `exp` — declared context, gated at exact instances)
  gives, for every `μ > 0`,

  > `Σ_{k≥d} x^k/k! ≤ e^{−μd + x e^μ}`,

  so the bound decays exponentially in `d` at fixed `t`, with the
  `μ = 1` readout: decay `e^{−d}` once `d > e·x`, i.e. a
  Lieb-Robinson-type velocity bound `v ≤ 20eJ` in site units. An
  explicit large-`d` smallness certificate is also gated in exact
  integer arithmetic (`e < 3`, so at `J = 1`, `t = 10`, `d = 800` the
  tail factor obeys `3^200 · 200^800/800! < 10^{−40}`).

Neither `20J` nor `20eJ` is claimed sharp.

**G7 (strict-extension exhibits against the siblings' certificates,
exact).** Neither sibling is contradicted; both certificates are
strictly extended, and both facts are gated:

- Block01's all-time constant is region-level — its note says the
  constant `c = 2J·|E(Λ)|` grows with the region (needled); G6's
  constant is free of `|E(Λ)|`.
- Block02's certified window at the instance `J_* = 1`, `m = 1`,
  `d = 6` is `|t| < 7/84 = 1/12` (value gated), while G6 is finite at
  `t = 10` — and nontrivially small there for suitable `d` (the G6
  large-`d` certificate above). Block02's per-coefficient bounds remain
  the coefficient-level statement this note does not reproduce; this
  note's bound is the broader **time-domain** function-level statement
  (no claim is made that it is numerically smaller inside block02's
  window).

## No-Go Discipline Gate

- **N1 route inventory.** Against "the walk expansion might still be
  volume-dependent": (1) the propagator `V(t)` involves all of `H` —
  ATTEMPTED: it enters only through unitary invariance of the norm,
  which is volume-blind; gated via the intertwiner identity; (2) the
  walk count might secretly depend on `Λ` — ATTEMPTED: walks in `E(Λ)`
  inject into walks in `E(Z^3)` and the count is gated on `Z^3`; (3)
  the base terms might reintroduce `|E(Λ)|` — ATTEMPTED: each base term
  is a single bond against `B`, bounded by `2J||B||`, with the
  `Y`-touching constraint gated; (4) the remainder might diverge —
  ATTEMPTED: geometric-over-factorial, gated symbolically past the
  threshold and at an instance; (5) degenerate cases — ATTEMPTED:
  `d = 0` is excluded by hypothesis and the runner gates an exact
  counterexample showing the exclusion is necessary (at `d = 0` the
  right side can fall below `||[A, B]||`); at `J = 0` every `h_b = 0`,
  so `τ_t = id` and `[A, B] = 0` by disjoint supports while the bound's
  right side is also `0` — consistent, covered by the disjointness
  gate; negative `t` — ATTEMPTED: handled by the gated `H → −H`
  symmetry, never by substituting `|t|` into the directed-time lemma.
- **N2 hypothesis independence.** The supplied hypotheses are
  independent in the standard sense: bond-locality (used in G1.3),
  Hermiticity of `h_b` (used only through `H̃(t)^† = H̃(t)` in G2),
  the norm bound `J` (used only in G4's majorization), and `d ≥ 1`
  (used only to kill `||[A, B]||` and set the series start) enter at
  disjoint proof steps; dropping any one breaks exactly the step named,
  as the runner's mutation battery exhibits gate-by-gate. The Duhamel
  mechanism (this note) and block02's coefficient mechanism are
  different expansions of the same object; neither implies the other —
  the walk reorganization happens **before** taking coefficients (the
  `k`-th walk term is not the `k`-th Taylor coefficient).
- **N3 hidden-wall scan.** The load-bearing conditions are all
  declared in Hypotheses: `d ≥ 1` (explicit, with the necessity
  exhibit), Hermitian bond terms, exponential calculus (siblings'
  declared class), time-ordered propagator existence (finite linear
  ODE), and the Riemann limit passage. Each is named where used; every
  load-bearing algebraic identity is gated; instance-level gates are
  described as instances (Verification). The `sin x ≤ x` step in the
  G3 instance gate is elementary and gated at exact instances.
- **N4 dependency roles, per citation.**
  - Block01 (sibling): supplies the class declaration (Hermitian bond
    terms, `J`), the L1a disjoint-factor mechanism (re-gated at G1c),
    the commutator norm bound (rebuilt there, re-gated at G3b), and
    the tail-domination mechanism (re-derived at G6b). Residual: none —
    each supplied fact is re-gated here.
  - Block02 (sibling): supplies the naming of this task (needled at N3
    of the runner) and the window certificate compared in G7 (value
    re-gated). Residual: none load-bearing.
  - `minimal_axioms`: supplies the no-dynamics boundary needle only.
  - Lieb-Robinson/Nachtergaele-Sims literature line: comparator class
    only — no cited statement is load-bearing; the recursion is
    rebuilt from gated identities in G1-G4.
- **N5 rhetoric audit.** "All-time volume-uniform" is claimed for the
  stated bound on the stated class; `20J` is named an activity scale,
  not a velocity; the velocity-type readout is the `μ`-bound's `20eJ`,
  stated with "not claimed sharp"; no physical velocity, propagation,
  or dynamics-selection claim is made.
- **N6 partial-closure scan.** Closed here: the walk reorganization —
  the family's named open task — at the Hamiltonian level. Still open,
  named: the sharp rate (optimizing `20J`/`20eJ`), the
  `U`-integrated/tick-level statement, and the fermionic transfer
  bridge. Nothing here forecloses them.
- **N7 steelman (strongest counterarguments found in review, answered
  in text).** (a) "The theorem fails at `d = 0`" — correct as an attack
  on an unhypothesized statement; the hypothesis `d ≥ 1` is now
  explicit and the runner gates the exact `d = 0` counterexample as an
  exclusion-necessity exhibit. (b) "The norm-transport display is false
  for `t < 0`" — correct against a naive `|t|` substitution; the lemma
  is directed-time and negative times go through the gated `H → −H`
  symmetry. (c) "The term-ratio argument is not exponential decay" —
  correct; the exponential statement is the separate `μ`-reweighted
  bound, adopted from the review lens and gated. (d) "The bound is
  astronomically large at `20J|t| ≫ d`" — inside the cone no decay is
  claimed; `2||A||||B||` is already the trivial bound there; the
  content is volume-uniformity at every `t` plus the outside-cone
  decay, both gated.
- **N8 prior-wall echo.** Searched the family and the cited CT note
  for prior walls this note might silently cross: block01's "explicitly
  NOT a volume-uniform velocity statement" wall is the one this note
  crosses **openly** — that wall was a scope marker on its own
  region-level constant, not a no-go, and its note names the
  interaction-path argument as the intended route (needled at G7a).
  The CT note's `U`-integrated and sharp-rate walls are untouched and
  remain open. No landed no-go forbids this bound; the family's
  exhibit-pair discipline (bound gated at a reaching instance,
  non-equality exhibited elsewhere) is repeated via G3's stationary
  bond and block02's parity exhibits.

**Status: PASS** (all eight items answered above; the three review
blockers and the cone-rate major are repaired in text and gated).

## Non-Claims

- Does **not** claim the scale `20J` or the readout `20eJ` is sharp,
  and does **not** supply the `U`-integrated statement, the fermionic
  transfer bridge, or any physical velocity.
- Does **not** cover `d = 0` (overlapping supports) — excluded by
  hypothesis, with the necessity of the exclusion gated.
- Does **not** claim numerical smallness inside the cone, nor that this
  bound is numerically smaller than block02's inside its window.
- Does **not** replace block02's per-coefficient bounds (they are
  coefficient-level statements this note does not reproduce).
- Does **not** select dynamics; the axioms supply none (needled).
- Does **not** set an audit verdict; independent audit remains required.

## Verification

Primary runner:
[`scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py`](../scripts/microcausality_all_time_volume_uniform_walk_expansion_2026_07_18.py)
— sympy-exact and enumeration-exact throughout. Gates are of two
honestly-distinguished kinds: **symbolic identity gates** (Jacobi,
conjugation, intertwiner, unitarity, coefficient assembly, μ-reweighting
identity, remainder-ratio threshold — proved for the displayed symbols)
and **exact instance gates** (variation-of-constants at a rational
spectrum, triangle-inequality witness, stationary-bond closed forms,
walk enumerations, tail and certificate arithmetic — exact at the named
instances, supporting the written proof text rather than replacing it).
The runner prints one `PASS`/`FAIL` line per gate and a final total; the
cached transcript is committed at the path in the header at landing
time.
