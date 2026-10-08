---
claim_id: record_activation_criticality_and_conditioned_planar_models_bounded_theorem_note_2026-10-08
claim_type: bounded_theorem
claim_scope: "For the declared independent exponential activation process on Z^3, the formed-site law at each fixed time is exactly Bernoulli site percolation; the accepted formalized critical-percolation theorem therefore gives almost surely finite formed-site clusters at its critical activation time. Separately, exact finite conditional dictionaries identify balanced cubic-ice layers with uniform six-vertex ice, a content-free planar record gas with square Ising, and a four-content occupied plane with symmetric Ashkin-Teller. The six-vertex GFF consequence has an explicit paper premise. No unrestricted cubic phase, content-cluster criticality, native dynamics or physical identification is inferred."
runner: scripts/record_activation_criticality_and_conditioned_planar_models_2026_10_08.py
upstream_dependencies:
  - minimal_axioms
  - supplied_record_laws_and_common_order_kernels_bounded_theorem_note_2026-09-15
  - uniform_ice_static_photon_stiffens_in_a_background_flux_and_saturation_leaves_square_ice_bounded_theorem_note_2026-09-23
  - square_ice_is_gaussian_at_long_wavelength_and_a_zone_boundary_excess_makes_the_sum_rule_miss_bounded_theorem_note_2026-09-24
  - admissibility_rule_the_record_gas_does_make_the_chessboard_when_a_recorded_bond_costs_a_factor_below_nine_over_62500_and_the_two_framed_states_differ_at_every_site_bounded_theorem_note_2026-09-24
---

# Record activation criticality and conditional planar models

**Type:** bounded_theorem. **Current status:** conditional-support; selective source review is recorded in the branch packet, and formal audit is unset.

```yaml
actual_current_surface_status: conditional-support
conditional_surface_status: conditional-support
trace_class: upstream_support
artifact_role: theorem
reachability_to_target: supports
audit_required_before_effective_retained: true
bare_retained_allowed: false
hypothetical_axiom_status: null
admitted_observation_status: null
```

The question is which standard probability laws occur exactly inside already supplied record models. Independent activation gives an exact critical-percolation consequence. Specified planar conditions give three useful statistical-mechanics comparisons with explicit weights, sectors and limits. These are separate models: no equality between their dynamics or equilibrium laws is assumed.

All clocks, activities, pair weights, initial conditions and restrictions below are supplied mathematical data. The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) do not choose them or identify their time and observables with physical readouts. External mathematical support does not change that premise boundary.

## 1. Sources, imports and prior work

Internal source baseline is `ed04ee2736b5bddb4e9064966505e3c3dfe003de`. All external OpenAI sources below are pinned to `adc7f1241b42e322a6451854ab7e4b4c146bf78a`.

| Input | Exact use here | Support and coverage |
|---|---|---|
| [E213: CriticalZ3 production theorem](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/CriticalZ3/Main.lean#L99-L110) | Almost surely every nearest-neighbor site cluster on ℤ³ is finite under `siteLaw siteCritical` | Accepted external Lean-verified mathematical support. The site component is exactly the scope used. |
| [E213 threshold bound](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/OAI/Probability/CriticalZ3/Subunit.lean#L247-L250) | `siteCritical < 1`, so the critical activation time is finite | Production dependency `OAI.CriticalZ3.siteCritical_lt_one`. |
| [E225: balanced six-vertex GFF paper](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026/The-Gaussian-free-field-limit-of-the-balanced-six-vertex-model-with-variance-multiplier-1-over-arcsin-c-over-2-September-23-2026.pdf), Theorem 1.1, pp. 2–4 | The GFF consequence in §4, at `c=1` and the paper's iterated balanced-torus state | Explicit paper premise. No Lean coverage for this GFF theorem is claimed. The finite dictionary is proved here. |
| [E218: bulk Ising paper](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/Conformal-universality-of-bulk-Ising-correlations-under-weak-interactions-September-23-2026/paper.pdf), §1, p. 2 | Supplies the stated conventional square-Ising benchmark `Kc=(1/2)log(1+√2)` | No weak-interaction universality or interface theorem is imported here; the gas dictionary is elementary. |
| [E233: critical Ashkin–Teller currents paper](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/preprints/The-joint-scaling-limit-of-critical-Ashkin-Teller-currents-September-25-2026/main.pdf), §2.1–2.2, pp. 4–6 | Identifies the external parameter line `J>0`, `U≤J`, `sinh(2J)=e^(-2U)` | Only the parameter dictionary is used. Its joint primal/dual current scaling theorem is not imported. |

E213 is the declaration `OAI.CriticalZ3.critical_no_infinite`, with site specialization `OAI.CriticalZ3.site_critical_no_infinite`. The official [formalization manifest](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/formalization.yaml#L1082-L1084) and [comparator configuration](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CriticalZ3.json) select `OAI.Probability.CriticalZ3.Main`. The [comparator definitions](https://github.com/openai/math/blob/adc7f1241b42e322a6451854ab7e4b4c146bf78a/lean/ComparatorChallenges/CriticalZ3.lean#L7-L58) use `Fin 3 → ℤ`, product Bernoulli site bits, nearest-neighbor paths whose vertices are open, and the site critical infimum. Its `sorry` is the challenge placeholder, not the production proof. We use the accepted production result; repeating its build or proof review is not a gate to this bridge. No new local Lean build is claimed.

Prior work fixes the contribution of this note:

- The [supplied record-law construction](SUPPLIED_RECORD_LAWS_AND_COMMON_ORDER_KERNELS_BOUNDED_THEOREM_NOTE_2026-09-15.md), lines 91–126 at the baseline, already has independent exponential activation, content-copy marks and finite decreasing ancestor graphs. Section 2 extracts its exact formed-site pushforward and applies E213.
- The [saturated ice-layer note](UNIFORM_ICE_STATIC_PHOTON_STIFFENS_IN_A_BACKGROUND_FLUX_AND_SATURATION_LEAVES_SQUARE_ICE_BOUNDED_THEOREM_NOTE_2026-09-23.md), §“Exact saturated-sector identity”, already reduces saturated cubic layers to independent uniform square ice. The [square-ice comparison note](SQUARE_ICE_IS_GAUSSIAN_AT_LONG_WAVELENGTH_AND_A_ZONE_BOUNDARY_EXCESS_MAKES_THE_SUM_RULE_MISS_BOUNDED_THEOREM_NOTE_2026-09-24.md) retains finite two-point comparisons, explicitly without a Gaussian-law limit. Sections 3–4 supply the arrow/sector/limit match needed for E225.
- The [record-gas note](ADMISSIBILITY_RULE_THE_RECORD_GAS_DOES_MAKE_THE_CHESSBOARD_WHEN_A_RECORDED_BOND_COSTS_A_FACTOR_BELOW_NINE_OVER_62500_AND_THE_TWO_FRAMED_STATES_DIFFER_AT_EVERY_SITE_BOUNDED_THEOREM_NOTE_2026-09-24.md), §“Premises and declared objects” and T1, already defines the six-content gas and its unlike-bond identity. Sections 5–6 specialize it to planar controls. Lattice-gas/Ising and four-state/Ashkin–Teller transformations are standard algebra; no novelty of those transformations is asserted.

## 2. Independent activation gives critical site percolation

### Declared process

At every `x∈ℤ³`, start blank and supply independent `T_x∼Exp(λ)`, with fixed `λ>0`. Supply independent fair innovation bits, uniform parent-selection marks, and copy marks of parameter `a∈[0,1)`, all independent of the times. At `T_x`, the site records once and permanently. If there are no already formed neighbors it uses its innovation bit. Otherwise it chooses a formed nearest neighbor uniformly and copies that content with probability `a`, using its innovation otherwise. The content is `0` or `I` in `M₂(ℂ)`. In particular, content selection never cancels or delays activation.

This defines the infinite process without a first global event. The independent continuous times have no ties almost surely, also after a countable union over pairs. A strictly decreasing activation-time path of length `n` is self-avoiding. From a fixed site there are at most `6·5^(n−1)` such candidate paths, each decreasing with probability `1/(n+1)!`. The probability of a decreasing path of length `n` therefore tends to zero. Almost surely every site's decreasing ancestor graph has finite depth and, by local finiteness, finitely many vertices. A countable intersection gives this simultaneously at all sites. Evaluate the contents on these finite ancestor graphs. The conditional chance of content `I`, given `m>0` formed neighbors containing `k` copies of `I`, is `(1−a)/2+ak/m`; for `m=0` it is `1/2`. Both contents remain supported for `a<1`. The existing pair `a=1/4,3/4` is included; `a=0` is the constant-content-kernel boundary member.

Define `η_x(t)=1{T_x≤t}` for each deterministic `t≥0`. Define the cluster `C_x(t)` to be empty when `η_x(t)=0`; otherwise it is the set reached from `x` by nearest-neighbor paths all of whose vertices have flag one. This matches the open-endpoint convention in E213.

### Theorem A: exact flag law and critical-time conclusion

For every `λ>0`, `a∈[0,1)` and fixed `t≥0`, the law of `(η_x(t))_x` is precisely independent Bernoulli site percolation with parameter

`q(t)=1−exp(−λt)`.

Let `p_c` be the site critical infimum in E213. Then

`t_c = −log(1−p_c)/λ`

is finite and positive, and almost surely **every formed-site cluster is finite at `t=t_c`**. This statement does not assert that the formed sites disappear: their density parameter is `p_c`.

**Proof.** For any finite `F⊂ℤ³` and pattern `b∈{0,1}^F`, independence of the times gives

`P(η|F=b)=∏_{x∈F} q(t)^{b_x}(1−q(t))^{1−b_x}`.

Finite cylinders generate the countable product sigma algebra, so this determines exactly the product Bernoulli law used in E213. Copy marks do not enter this calculation. At `t_c`, `q(t_c)=p_c`; the pushforward of the accepted E213 site theorem proves the simultaneous all-site assertion.

For completeness, `p_c≥1/5>0`: at `p<1/5`, the chance of an open self-avoiding length-`n` path from zero is at most `6·5^(n−1)p^(n+1)→0`. An infinite cluster in this locally finite graph would contain such paths at every length. The production bound `p_c<1` gives finiteness of `t_c`. The continuous increasing map `q:[0,∞)→[0,1)` also takes the infimum of positive origin-percolation parameters to the corresponding activation-time infimum. To check this last statement, use the usual common-uniform-bit monotone coupling: for any `p>p_c`, the definition of infimum provides a percolating parameter below `p`, and monotonicity gives positive origin probability at `p`. ∎

At `t=0` all sites are blank. Every site is eventually formed almost surely, but this does not imply an infinite cluster at the fixed critical time. Correlated contents are not independent site colors. A law with failed formations, feedback-dependent activation rates, dependent clocks, or completion conditioning needs its own pushforward calculation; Theorem A has not supplied one for it.

### Corollary A: a static record-gas boundary member

The gas defined in §5 has, at `g=1` and `p=q=r>0`, occupation weight `ζ^N`. On every finite set its partition function is `(1+ζ)^V`, independently of the fixed exterior occupation because there are no bond factors. Its infinite-volume flag law is therefore the product Bernoulli law of density `ζ/(1+ζ)`. E213 gives finite clusters almost surely at

`ζ_c=p_c/(1−p_c)`.

For `t>0`, this static product law and the dynamic flag law agree when `ζ=exp(λt)−1`. It is an equality of fixed-time occupation laws; no equality of content laws or dynamics follows.

## 3. Conditioned cubic ice and the balanced six-vertex sector

Let `M,L≥4` be even integers and use the square torus `T_{M,L}`. A cubic-ice layer has binary horizontal-link occupations and two prescribed vertical-link bits `v_x,w_x` at each vertex. Impose `v_x+w_x=1` pointwise and give equal weight to every horizontal assignment obeying the cubic rule of exactly three occupied incident links. This is a finite conditional layer law. In the previously studied saturated vertical sectors the complementary condition already holds, and holding all vertical layers leaves horizontal layers independent.

### Theorem B: finite measure and sector equivalence

Every allowed horizontal configuration has exactly two occupied links incident to each vertex. Put `ε(x,y)=(-1)^(x+y)`. Orient each occupied edge from even to odd and each unoccupied edge from odd to even. This gives a weight-preserving bijection to six-vertex arrows of weights `a=b=c=1`.

For a horizontal edge starting at `(x,y)` and pointing in the positive coordinate direction, let `τ_x(x,y)` be `+1` for a right arrow and `−1` for a left arrow. Then

`τ_x(x,y)=ε(x,y)(2n_x(x,y)−1)`.

Thus the balanced six-vertex condition on every vertical cut, `Σ_y τ_x(x,y)=0`, is exactly the occupation condition

`Σ_y (-1)^y(2n_x(x,y)−1)=0`.

**Proof.** Removing the one occupied vertical link leaves degree two among the four horizontal links. At an even vertex the two occupied links point out and the others in; at an odd vertex the directions reverse. Conversely, the arrow direction determines each occupation and the two-in/two-out condition gives degree two. All weights are one. The displayed sign identity proves the cut relation. Summing arrow divergence over a column gives conservation of the cut flux, so a single balanced cut enforces every one. Conditioning either uniform measure on this corresponding nonempty sector preserves the bijection. Nonemptiness follows, for example, by occupying every edge in one coordinate direction and none in the other; the alternating cut sum vanishes for even `L`. ∎

The parity restriction is essential for this dictionary. On an odd-period torus `ε` is not a well-defined bipartition. Independent row counts give 242 versus 276 in the balanced occupation/arrow models on `3×4`, and 2600 versus 3520 on `3×6`; these are adverse controls, not a claim about another possible odd-torus mapping. On `4×4`, the all-sector occupation count is 2970, agreeing with the existing saturated-layer result, while the balanced count is 1682. The sector restriction is therefore explicit model content. No condition on the other torus winding is imposed.

## 4. The paper-premised GFF consequence

**Additional premise E225.** Accept Theorem 1.1 of the pinned balanced six-vertex paper for its stated model, normalization and limits. It asserts existence of the balanced-torus local limit as `M→∞` first and then even `L→∞`, for each fixed `0<c≤2`, and the GFF limit of its unit-jump height.

Under E225, Theorem B identifies the corresponding iterated even-`M`, even-`L` limit of our balanced conditional layer with the paper's `c=1` plane law. Indeed, every finite law agrees under the local arrow map, and existence of the full first limit in E225 makes its even subsequence agree. The second limit is already through even widths. This argument does not exchange the limits or assert sector equivalence for the all-sector law.

Give the face on the left of an arrow height one more than the face on its right. On the plane the ice rule makes height increments path independent, so `h` is defined modulo constants. Put `h_δ(x)=h(x/δ)` using the paper's face convention. For any finite collection of smooth compactly supported tests `f_i` with integral zero, E225 then gives

`(∫ h_δ f_i)_i ⇒ centered Gaussian with covariance (6/π)∬ G(x,y) f_i(x)f_j(y) dx dy`,

where `G(x,y)=−(1/(2π))log|x−y|`. The multiplier is `1/arcsin(1/2)=6/π`; the height jumps have magnitude one, so no extra factor from the occupation bits is inserted.

This consequence is explicitly conditional on a named paper theorem. It is packaged now without claiming a Lean proof of the GFF theorem. The all-size finite dictionary is proved independently in §3. The unrestricted cubic marginal, a three-dimensional Perron layer state, and a quantum ring ground state have not been identified with these conditioned balanced planar laws.

## 5. A content-free planar gas is square Ising

### Declared gas

On a finite cubic graph a site is empty or carries one of the six contents `±e_1,±e_2,±e_3`. With positive `p,q,r`, the pair weight `ω(s,s')` is `p` for equal contents, `q` for opposites and `r` for orthogonal contents. Define

`M(s,s')=6ω(s,s')/(p+q+4r)`.

For an occupied set with `N` vertices and `B` occupied-occupied bonds, put

`Q=E_uniform[∏_occupied bonds M(s_x,s_y)]`,  `weight=ζ^N g^B Q`,

with `ζ,g>0`; the contents in this expectation are independently uniform before weighting. This restates the supplied gas. When `p=q=r`, `M=1` and `Q=1` on every occupied graph.

Take a planar `M×L` torus with even `M,L≥4`, embedded in a slab with two held neighboring layers. At each planar site hold the lower/upper occupations complementary, so exactly one is occupied. Keep `p=q=r`. Terms involving only held sites are constants. Every occupied plane site then contributes precisely one vertical occupied bond. The conditional planar law is

`weight_plane=(ζg)^N g^{B_plane}`.

### Theorem C: exact zero-field dictionary

At `ζ=g^(−3)` and for every `g>0`, set

`σ_x=ε_x(2n_x−1)`,  `K=−(1/4)log g`.

The occupation law is carried bijectively to the periodic zero-field nearest-neighbor Ising law `weight∝exp(KΣ_<xy> σ_xσ_y)` on the same square torus. It is ferromagnetic for `0<g<1`; `g=1` gives independent fair occupations.

**Proof.** The effective activity is `g^(−2)`. Every planar vertex has degree four, the number of bonds is `2V`, and `ε_x ε_y=−1` on a bond. Expanding the products gives

`Σ_<xy> σ_xσ_y = −2V+8N−4B_plane`,

or `4(B_plane−2N)=−2V−Σ σ_xσ_y`. Consequently

`g^(B_plane−2N)=g^(−V/2) exp[−(log g)/4 · Σ σ_xσ_y]`.

The first factor is configuration independent. The inverse occupation map is `n_x=(1+ε_xσ_x)/2`. ∎

The conventional square-Ising critical benchmark `Kc=(1/2)log(1+√2)` corresponds exactly to `g_c=exp(−4Kc)=3−2√2`. This identifies the benchmark inside the conditioned planar family. No critical point of the full cubic gas is thereby identified. A domain/interface theorem would require its own compatible boundary law. Summing general six-content interactions gives a graph-dependent `Q`, so no small finite-range Ising perturbation is assumed here.

## 6. Four planar contents give symmetric Ashkin–Teller weights

Condition a plane fully occupied, all immediate off-plane neighbors vacant, and each plane content to lie in `{+e_1,−e_1,+e_2,−e_2}`. The plane may be a finite square torus as above. The occupation factors and the constant normalization of `M` are now configuration independent; the content law has weight `∏_bonds ω(s_x,s_y)`.

Encode `+e_1=(+,+)`, `−e_1=(−,−)`, `+e_2=(+,−)`, `−e_2=(−,+)`, with components `σ,τ`.

### Theorem D: exact pair-weight and parameter dictionary

For all positive `p,q,r`, define

`J=(1/4)log(p/q)`,  `U=(1/4)log(pq/r²)`,  `C=(pqr²)^(1/4)`.

Then on every bond

`ω = C exp[J(σσ'+ττ')+U σσ'ττ']`.

Hence the normalized conditional law is exactly the symmetric Ashkin–Teller pair law. The external E233 parameter conditions are equivalent to

`p>q`,  `q≤r`,  `p−q=2r`.

**Proof.** Equal states give `(σσ',ττ')=(1,1)` and weight `Ce^(2J+U)=p`; opposites give `(-1,-1)` and weight `Ce^(−2J+U)=q`; orthogonal contents give opposite signs and weight `Ce^(−U)=r`. These three cases exhaust the bonds and prove the all-graph identity. Positivity makes all logarithms and normalizations legitimate. Furthermore

`sinh(2J)=(p−q)/(2√(pq))`,  `e^(−2U)=r/√(pq)`,  `U−J=(1/2)log(q/r)`.

The stated equivalence follows. ∎

The current gas example `(p,q,r)=(3,1,2)` is off that parameter line. `(3,1,1)` maps to its endpoint `J=U=(log 3)/4`, and `(5,1,2)` maps to an interior point. This is a parameter-line comparison, not a new proof of Ashkin–Teller criticality. E233's joint current theorem additionally specifies a primal/dual spin-edge coupling with wired/free boundaries. The ordinary pair-weight identity above does not create that joint law, and no current/cluster scaling conclusion is claimed for it.

## 7. Executed checks, review boundary and formalization follow-up

The [standalone primary runner](../scripts/record_activation_criticality_and_conditioned_planar_models_2026_10_08.py) reads no scientific files and uses only standard-library integer and rational arithmetic. Its [canonical cache](../logs/runner-cache/record_activation_criticality_and_conditioned_planar_models_2026_10_08.txt) is saved through the repository's `runner_cache` envelope.

The scientific checks cover the tensor-law forward equations, projection through content kernels, a state-dependent-rate adverse control, static gas product factorization, separate occupation/arrow row counts and parity/sector controls, the planar gas identity on all 65,536 `4×4` configurations, and all 16 Ashkin–Teller bond assignments at four positive parameter triples. Fourth powers remove logs and roots in the latter check. These finite checks support the independently stated proofs; they neither estimate `p_c` nor certify a thermodynamic limit.

Reproduce from the repository root:

```bash
python3 scripts/record_activation_criticality_and_conditioned_planar_models_2026_10_08.py
```

The successful source-bound run prints `TOTAL: PASS=22 FAIL=0`. The number counts grouped checks, not independent proofs. No new framework axiom, physical parameter choice, audit verdict or empirical prediction is supplied.

Concrete Lean targets for the later audit are:

1. Prove that the coordinate threshold map on independent exponential times pushes the product measure to `OAI.CriticalZ3.siteLaw (1−exp(−λt))`; map the open-endpoint cluster definition and apply `site_critical_no_infinite` at `t_c`. Formalize the static activity/product-law corollary by the same interface.
2. Construct the finite equivalence between degree-two occupations and divergence-free arrows on even square tori, then prove preservation of counting measure and the balanced cut condition. Transport local weak limits through this fixed local map; keep E225 as a separate theorem premise until its stated support changes.
3. Prove the degree-four bipartite edge-sum identity and equality of normalized planar gas/Ising weights, including the complementary held-layer factor.
4. Prove the four-state/two-spin equivalence and positive real pair-weight identities, with the exact translation of E233's parameter conditions.

These are audit follow-ups for the new bridges, not pre-PR gates. The current note provides ordinary proofs and exact finite checks. Independent source review remains separate from formal retained status. Physical law selection, removal of conditioning, unrestricted cubic phase questions and the absent Ashkin–Teller current coupling remain open where named; the proven conditional statements do not depend on solving them.
