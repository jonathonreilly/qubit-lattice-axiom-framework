---
claim_id: admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_differ_iff_an_unrecorded_component_touches_two_recorded_sites_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the static law of a covariant nearest-neighbour rule with value-only covariance — the six-axis product rule phi in {p, q, r} (same, antipodal, orthogonal; positive) and the sphere rule exp(beta s.s') — on a finite set W of recorded sites with a finite set E of unrecorded sites adjacent to it, comparing the free-window reading R1 (the law is normalized over the recorded sites only) with the integrated-exterior reading R2 (every site's possibilities enter; records lock, unrecorded sites are summed) and the exterior-records reading R3 (the exterior records held): (Q1) mu_W^R2 is proportional to the W-bond product times a factor F_C(v_{partial C}) for each connected component C of E, and mu_W^R2 is the average of mu_W^R3(.|omega) over the exterior's law (proved; executed); (Q2) a component touching exactly one recorded site contributes a constant factor, by value covariance and the transitivity of the covariance group on the menu, so R1 = R2 whenever every component of E touches one recorded site (proved; executed symbolically for pendant paths and exactly on a plaquette with two pendant components); (Q3) a single unrecorded site touching two recorded sites contributes phi^2(v_x, v_y) = Z_1^2 P_0 + (p-q)^2 P_odd + (p+q-2r)^2 P_even, constant iff p = q = r; a path of k internal bonds contributes phi^{k+2}; in general a two-attachment factor is constant iff both of its nontrivial isotypic eigenvalues vanish; for the sphere rule the single-site factor is 4 pi sinh(beta|v_x+v_y|)/(beta|v_x+v_y|), strictly increasing in v_x . v_y (proved; executed); (Q4) exact witnesses: on the plaquette with one unrecorded site adjacent to two adjacent corners TV(R1, R2) = 78621/4563820 at (3,1,2), 675203620/64463986907 at (5,2,4), 221667/30063356 at (2,1,2); on the cube with its top face unrecorded TV = 9778807/1312253264 at (3,1,2); with two pendant components TV = 0 (executed); (Q5) the separating clause pair is recorded for the owner and not adopted; every result of this lane on tori is reading-independent, every window result stated uniformly in exterior records holds under R2 by averaging, and free-window statements are R1 by declaration (proved). No reading, rule or coupling is selected; exact arithmetic throughout."
upstream_dependencies:
  - minimal_axioms
  - possibility_covariance_soldered_vs_unsoldered_cl30_invariant_rules_and_haar_fair_coin_bounded_theorem_note_2026-09-14
  - admissibility_rule_formation_law_versus_static_law_finite_window_classification_bounded_theorem_note_2026-09-06
runner: scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py
---

# Unrecorded sites: the free-window and integrated-exterior readings of the static law differ exactly when an unrecorded component touches two recorded sites — an exact criterion, exact witnesses on the plaquette and the cube, and the separating clause recorded

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** bounded-support (exact; conditional on the named supplied readings; unaudited)

## Result up front

The campaign's meta note lists, as a hypothesis for investigation rather than
a reading, the claim that unrecorded sites carry no law-level state. Two
readings of the static law of a set of records are then on the table. Under
the free-window reading (R1), the law is the product of the rule's bond
weights over the recorded sites alone. Under the integrated-exterior reading
(R2), every site has its domain of possibilities, a record locks one of them,
and the possibilities of unrecorded sites are summed out. This note settles
when the two agree, exactly, for the lane's rules.

They agree unless some connected set of unrecorded sites touches two
recorded sites. An unrecorded component attached to a single recorded site
contributes a factor that is constant, because the rule is invariant under
rotations of the values and the covariance group moves any value to any other;
a constant factor disappears in the normalization. An unrecorded site
attached to two recorded sites contributes the matrix square of the rule,
`φ²`, which is a constant matrix only when the rule is constant; a path of
unrecorded sites contributes a higher power, with the same conclusion; and the
general two-attachment factor is constant exactly when its two nontrivial
isotypic eigenvalues vanish. The differences are exact rationals on small
windows: on the plaquette with one unrecorded site adjacent to two adjacent
corners the two laws differ by `78621/4563820` in total variation at
`(3, 1, 2)`; on the cube with its top face unrecorded, by
`9778807/1312253264`; with pendant components only, by `0`.

Two models satisfying every axiom sentence used, differing on a named target:
the campaign's witness format. The separating clause pair — "a site without a
record contributes no factor to the law" against "every site's admissible
possibilities enter the law" — is recorded for the owner and not adopted.
For this lane the fork is harmless: results on tori have no exterior, and the
window results were stated uniformly in the exterior records, which covers
the integrated reading by averaging.

Exactly: Q1 (factorization and the average identity); Q2 (one attachment:
constant); Q3 (two attachments: `φ²`, `φ^{k+2}`, the eigenvalue criterion;
the sphere factor); Q4 (the witnesses); Q5 (the clause and the lane).
Executed with exact arithmetic: 20 checks, 13 mutations.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "the derivation campaign's seam 'record-process dynamics and unrecorded sites' (the meta note of 2026-09-13): 'the claim that unrecorded sites carry no law-level state is a hypothesis for investigation, not an adopted reading or a theorem'; the window convention of blocks 12, 17, 20 and 23"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "the hypothesis is now an exact fork: the free-window and integrated-exterior readings coincide iff every unrecorded component touches one recorded site; exact witnesses on the plaquette and the cube; the clause pair recorded for the owner. The lane's torus results are reading-independent and its window results cover the integrated reading by averaging. Consumers: the campaign's decision record; #8093's assembly (readings of Record)"
conditional_surface_status: "Q1-Q5 proved for the six-axis product rule with positive weights and for the sphere rule, on finite sets of recorded sites with finite unrecorded exteriors; the skeleton executed exactly (the spectral decomposition, the constancy criterion, pendant paths symbolically, three plaquette witnesses, the cube witness, the forest, the average identity, the sphere factors); conditional on the static reading of block 01 and on the two readings as declared; no reading adopted"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) is used through the sentences "Each site has a domain of local possibilities.", "No possibility is privileged.", "There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.", "For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.", "Records form.", "A site with no record cannot be read.", and "A state is a configuration of records.". Block 01 (`docs/ADMISSIBILITY_RULE_FORMATION_LAW_VERSUS_STATIC_LAW_FINITE_WINDOW_CLASSIFICATION_BOUNDED_THEOREM_NOTE_2026-09-06.md`, on `main`) supplies the static reading of a finite set of records: the normalized product of the rule's bond weights (its free-window form is R1 below). The landed possibility-covariance note (`docs/POSSIBILITY_COVARIANCE_SOLDERED_VS_UNSOLDERED_CL30_INVARIANT_RULES_AND_HAAR_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-14.md`, section "Empty-neighbourhood sphere laws") supplies the sphere as a possibility domain and the unsoldered reading. The campaign meta note (`docs/TOE_DERIVATION_CAMPAIGN_AXIOM_SUFFICIENCY_BY_UNDERDETERMINATION_WITNESSES_NOTE_2026-09-13.md`, on `main`) names the seam and the witness format. All proposed and unaudited.

Declared objects.
- **Menus and rules.** The six-axis menu `M = {±e_1, ±e_2, ±e_3}` with the product rule `φ(v, v') = p` if `v = v'`, `q` if `v = −v'`, `r` otherwise (`p, q, r > 0`); the sphere `S²` with `φ(s, s') = e^{β s·s'}`, `β > 0`, and the uniform measure `dσ`. Both rules have **value-only covariance**: `φ(gv, gv') = φ(v, v')` for every `g` in the covariance group `G` (`O`, the 24 proper cube rotations, on `M`; `SO(3)` on `S²`), which acts transitively on the menu.
- **Sites.** A finite set `W` of recorded sites and a finite set `E` of unrecorded sites, with the nearest-neighbour graph of `Z³` restricted to `W ∪ E`; the connected components `C` of the graph induced on `E`; `∂C = {x ∈ W : x ~ a for some a ∈ C}` (the recorded sites `C` touches).
- **The three readings.** `μ_W^{(1)}(v) = Z_1^{−1} Π_{⟨xy⟩ ⊂ W} φ(v_x, v_y)` (R1, free window); `μ_{W∪E}(v, u) = Z^{−1} Π_{⟨ab⟩ ⊂ W∪E} φ` and `μ_W^{(2)}` its marginal on `W` (R2, integrated exterior); `μ_W^{(3)}(v | ω) = Z(ω)^{−1} Π_{⟨xy⟩⊂W} φ(v_x, v_y) Π_{x ∈ W, a ∈ E, x ~ a} φ(v_x, ω_a)` (R3, exterior records `ω` held; the object of blocks 17 and 23).
- **The effective factor.** `F_C(v_{∂C}) = Σ_{u ∈ M^C} Π_{⟨ab⟩ ⊂ C} φ(u_a, u_b) Π_{x ∈ ∂C, a ∈ C, x ~ a} φ(v_x, u_a)` (an integral against `dσ^C` on the sphere).
- **The spectral sectors of `φ` on `M`.** `P_0` the projector onto constants; `P_odd` onto odd functions (`f(−v) = −f(v)`, dimension `3`); `P_even` onto even functions with zero sum (dimension `2`); `Z_1 = p + q + 4r`.
- **Total variation.** `TV(μ, ν) = (1/2)Σ_v |μ(v) − ν(v)|`.

## Prior art and what is new

That integrating out a pendant subtree of a Markov random field leaves the marginal unchanged, and that a bridging subgraph induces an effective interaction, is classical (the marginalization of Gibbs fields; the Markov property). Blocks 15 and 16 treated *recorded* environments; block 01 declared the free-window static law; blocks 17 and 23 worked with exterior records held. What is new here: (i) the campaign's hypothesis about unrecorded sites turned into an exact fork with a graph criterion, for the lane's two rules, with the constancy of one-attachment factors proved from value covariance and transitivity rather than from a Markov property; (ii) the exact algebra of two-attachment factors on the six-axis menu (`φ²`, `φ^{k+2}`, the isotypic criterion) and the sphere's closed form; (iii) exact witnesses in the campaign's format, with the clause pair recorded; (iv) the audit of the lane's own window convention against the fork.

## Exact target and obligation graph

| Obligation | Statement | Route | Runner family |
|---|---|---|---|
| Q1 | factorization over components; R2 is the R3-average | the product form | D |
| Q2 | one attachment ⇒ constant factor; R1 = R2 for pendant exteriors | value covariance; transitivity | B, D |
| Q3 | two attachments: `φ²`, `φ^{k+2}`, the isotypic criterion; the sphere factor | the spectral decomposition; the sphere integral | B, C, E |
| Q4 | exact witnesses on the plaquette, the cube, the forest | enumeration | D |
| Q5 | the clause pair; the lane's convention | Q1–Q4 | — |

## Theorem Q1 — factorization and the average identity

**Statement.** `μ_W^{(2)}(v) = Z^{−1} Π_{⟨xy⟩ ⊂ W} φ(v_x, v_y) Π_C F_C(v_{∂C})`, the product over the connected components `C` of `E`; and `μ_W^{(2)} = Σ_ω μ_{W∪E}(u = ω) μ_W^{(3)}(· | ω)`, the sum over the exterior configurations weighted by their marginal law.

**Proof.** A bond of `W ∪ E` lies within `W`, within a single component of `E` (two adjacent unrecorded sites are in the same component), or between `W` and a component. Summing `Π φ` over `u ∈ M^E = Π_C M^C` therefore factorizes into the `W`-bond product times `Π_C F_C`, and `F_C` depends on `v` only through `v_{∂C}`. The average identity is the definition of the conditional law: `μ_{W∪E}(v, ω) = μ_{W∪E}(ω) μ_W^{(3)}(v | ω)`, since the conditional density of `v` given `u = ω` is the `W`-bond product times the `W–E` factors with `u = ω`, normalized. ∎ (Executed on the plaquette with one unrecorded site: D4.)

## Theorem Q2 — one attachment gives a constant factor

**Statement.** If `∂C = {b}` (the component touches exactly one recorded site, through any number of bonds), then `F_C(v_b)` does not depend on `v_b`. Consequently `μ_W^{(2)} = μ_W^{(1)}` whenever every component of `E` touches exactly one recorded site.

**Proof.** For `g ∈ G`, `F_C(g v_b) = Σ_u Π_{⟨ab⟩⊂C} φ(u_a, u_b) Π_{a ~ b} φ(g v_b, u_a)`. Substitute `u_a = g u'_a` for every `a ∈ C` (a bijection of `M^C`; on the sphere the invariant measure `dσ^C` is preserved): by value-only covariance every factor returns to `φ(u'_a, u'_{a'})` or `φ(v_b, u'_a)`, so `F_C(g v_b) = F_C(v_b)`. `G` is transitive on the menu, so `F_C` is constant. A constant factor cancels between numerator and normalization in Q1. ∎ (Executed: the factor of a pendant path of two and of three unrecorded sites, symbolically in `p, q, r`, is the same polynomial for all six values of `v_b`; the plaquette with two pendant components has `TV(R1, R2) = 0` exactly at `(2, 1, 2)`: B4, D3.)

*Remark.* The soldered reading acts on sites and values jointly; the argument uses only invariance of `φ` under value rotations, which the lane's rules have (the pair relation same/antipodal/orthogonal, and `s·s'`, are invariant).

## Theorem Q3 — two attachments

**Statement.** (a) *Spectral decomposition.* On functions on `M`, `φ = Z_1 P_0 + (p − q) P_odd + (p + q − 2r) P_even`. (b) *One unrecorded site.* If `C = {a}` and `∂C = {x, y}`, then `F_C(v_x, v_y) = (φ²)(v_x, v_y) = Z_1² P_0 + (p−q)² P_odd + (p+q−2r)² P_even`, which is a constant matrix if and only if `p = q = r`; explicitly `φ²_{same} − φ²_{orth} = (p−r)² + (q−r)²` and `φ²_{anti} − φ²_{orth} = 2(p−r)(q−r)`. (c) *A path.* If `C` is a path of `k` internal bonds whose end sites attach to `x` and `y` respectively, `F_C = φ^{k+2}`, constant iff `p = q = r`. (d) *In general.* For `∂C = {x, y}`, `F_C` is `G`-covariant, hence `F_C = λ_0 P_0 + λ_odd P_odd + λ_even P_even` as a matrix in `(v_x, v_y)`, and it is constant iff `λ_odd = λ_even = 0`; when `x` and `y` attach to distinct sites `a ≠ b` of `C` through single bonds, `F_C = φ T φ` with `T(u_a, u_b)` the weight of `C` with `u_a, u_b` held, itself `G`-covariant with sectors `τ_0, τ_odd, τ_even`, so `λ_odd = (p−q)² τ_odd` and `λ_even = (p+q−2r)² τ_even`. (e) *The sphere.* For `C = {a}`, `∂C = {x, y}`: `F_C = 4π sinh(β|v_x + v_y|)/(β|v_x + v_y|)` with `|v_x + v_y|² = 2 + 2 v_x·v_y`, strictly increasing in `v_x·v_y`; for `∂C = {b}` it is `4π sinh β/β`.

**Proof.** (a) For `f` on `M`, `(φf)(v) = p f(v) + q f(−v) + r Σ_{v' ⊥ v} f(v')`. If `f` is odd, `Σ_{v'⊥v} f(v') = 0` (the four orthogonal values come in antipodal pairs), so `φf = (p − q)f`. If `f` is even with zero sum, `Σ_{v'⊥v} f(v') = Σ_{all} f − f(v) − f(−v) = −2f(v)`, so `φf = (p + q − 2r)f`. Constants are eigenvectors with `Z_1`. The three sectors span all functions (dimensions `1 + 3 + 2`). (b) `F_C(v_x, v_y) = Σ_u φ(v_x, u)φ(u, v_y) = (φ²)(v_x, v_y)` since `φ` is symmetric; squaring the decomposition gives the sectors; a matrix `λ_0 P_0 + λ_odd P_odd + λ_even P_even` is constant (a multiple of `P_0`) iff `λ_odd = λ_even = 0`, i.e. `(p−q)² = 0 = (p+q−2r)²`, i.e. `p = q = r`; the entry differences follow by expanding `φ²` (executed). (c) The factor is the matrix product of `k + 2` copies of `φ`, with eigenvalues the `(k+2)`-th powers. (d) `F_C(gv_x, gv_y) = F_C(v_x, v_y)` by the substitution of Q2, so `F_C` commutes with the action of `G`; the commutant of a representation decomposing into three inequivalent irreducibles (the trivial, the odd three-dimensional and the even two-dimensional sectors, inequivalent by their dimensions and the trivial one's character) is spanned by the three projectors; the rest is (b)'s argument with `T` in place of the middle factor. (e) `∫ e^{β u·w} dσ(u) = 4π sinh(β|w|)/(β|w|)` for `w ≠ 0` (polar coordinates about `w`; `2π∫_{−1}^{1} e^{β|w|t} dt`), applied to `w = v_x + v_y` and to `w = v_b`; `sinh z/z` is strictly increasing on `z > 0` because `(sinh z/z)' = (z cosh z − sinh z)/z²` and `z cosh z − sinh z = Σ_{n≥1} 2n z^{2n+1}/(2n+1)! > 0`. ∎

Executed: the three eigenvalues with explicit eigenvectors, the entry differences and the constancy criterion (B1–B2); the path powers for `k ≤ 3` (B3); the sphere factors and the series positivity (C1–C2); two single-site components attached to the same pair of recorded sites (the two unrecorded corners of a plaquette), whose combined factor is the entrywise square of `φ²` and is nonconstant unless `p = q = r` (E1).

## Theorem Q4 — the witnesses

**Statement.** Exact values of `TV(μ_W^{(1)}, μ_W^{(2)})`: (a) `W` a plaquette, `E` one site adjacent to two adjacent corners: `78621/4563820` at `(3, 1, 2)`, `675203620/64463986907` at `(5, 2, 4)`, `221667/30063356` at `(2, 1, 2)`; (b) `W` the bottom face of the unit cube, `E` its top face (a four-cycle touching all four recorded sites): `9778807/1312253264` at `(3, 1, 2)`; (c) `W` a plaquette, `E` a pendant path of two sites off one corner and a pendant site off the opposite corner: `0` at `(2, 1, 2)`.

**Proof.** Enumeration of `M^{W∪E}` with integer weights and exact rational normalization; (c) is Q2. ∎ (D1–D3.)

## Corollary Q5 — the clause pair and the lane's convention

**Statement.** (a) The two readings are two models satisfying every axiom sentence quoted under Premises and differing on the named target (the law on `W`) by the exact amounts of Q4; their separating clause pair, recorded for the owner and not adopted, is: (R1) "The static law of a configuration of records is normalized over the recorded sites alone; a site without a record contributes no factor." against (R2) "Every site's admissible possibilities enter the static law; a record locks one of them, and the possibilities of a site without a record are summed." Neither is derived from the quoted sentences: "Each site has a domain of local possibilities" applies to every site, "A state is a configuration of records" names the records alone, and "A site with no record cannot be read" concerns readout, not the law. (b) For this lane: results proved on tori (blocks 19–23) involve no exterior and are reading-independent; results proved uniformly in the exterior records (blocks 17 and 23) hold under R2 by Q1's average identity; results declared on free windows (blocks 01, 05, 12) are R1 statements; and R1 = R2 for every window whose unrecorded surroundings are pendant components (Q2).

**Proof.** (a) is Q1–Q4 with the sentences quoted; (b) is Q1(second part) and Q2 applied to the cited blocks' objects. ∎

*Not claimed.* Which reading the axioms intend; any global (infinite-exterior) form of R2 beyond the finite `E` declared; anything about the formation reading, where the recorded set grows and the fork takes a different form (block 15's environments are R3 objects).

## No-Go Discipline Gate

The negative sentence is Q4 with Q3: the two readings are not the same law on any window whose unrecorded surroundings contain a component touching two recorded sites, for every non-constant rule. Escapes named: the constant rule `p = q = r` (where every factor is constant); pendant exteriors (Q2); the formation reading (not treated).

### N1 — Routes by which the negative could fail
1. *The one-attachment argument also kills two-attachment factors* — closed: it uses transitivity on a single value; with two values the orbit of the pair is not a single point, and `φ²` is nonconstant (B2).
2. *A cancellation between components* — closed: the factors multiply and each is a function of its own `∂C` (Q1).
3. *The plaquette witness is a degenerate triple* — closed: three triples executed, including `(3,1,2)` where `p + q = 2r` kills the even sector but not the odd one (D1).
4. *The cube's four-cycle exterior might contribute a constant* — closed: `TV > 0` exactly (D2).
5. *The constant rule; pendant exteriors; the formation reading* — escapes, named above.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
No hidden dependence: the inputs are the axioms' sentences, block 01's static reading, the parent note's sphere law, and the meta note's seam.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the seven sentences under Premises | yes (premise) |
| block 01 (`main`) | the static reading; R1 | yes (premise, proposed) |
| the possibility-covariance note (`main`) | the sphere domain and reading | yes for Q3(e) (premise, proposed) |
| the campaign meta note (`main`) | the seam and the witness format | framing only |
| blocks 15–17, 19–23 (open PRs) | the lane's window convention audited in Q5(b) | Q5(b) only (evidence addresses) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "R1 ≠ R2 iff an unrecorded component touches two recorded sites" | executed: the spectral decomposition with eigenvectors; `φ²`'s entry differences; the path powers; the sphere integrals and the series | executed: pendant paths of two and three sites symbolically for all six values | executed: the two unrecorded corners' entrywise square of `φ²` | executed: the plaquette at three triples, the cube, the forest, the average identity | proved for every finite `W`, `E` and every non-constant rule of the two families (Q1–Q3); the readings' intent not claimed |

### N6 — Partial-closure paths and primitive scan
The registered primitives supply no reading of Record; none is a wall.

### N7 — Steelman
Hostile reviewer: "This is the Markov property of Gibbs fields; pendant subtrees marginalize trivially and bridges do not." Reply: the campaign asked whether the hypothesis 'unrecorded sites carry no law-level state' has content, and the answer is an exact graph criterion with witnesses in the campaign's format plus the audit of the lane's own convention; the one-attachment constancy here comes from value covariance and transitivity, which also covers exteriors that are cycles attached at one site. Conceded: nothing here says which reading the axioms mean.

### N8 — Cross-cycle echo
Block 15's criterion (sequential equals joint iff no site records an inside neighbour with a second) and block 16's flip lemma are the recorded-environment relatives of this fork; block 17's boundary conditions and block 23's exterior records are R3 objects; the tori of blocks 19–22 are reading-free.

## Falsifiers
- An eigenvector of `φ` outside the three sectors, or an eigenvalue other than `Z_1`, `p − q`, `p + q − 2r` (B1); an entry difference of `φ²` other than `(p−r)² + (q−r)²` or `2(p−r)(q−r)`, or a constant `φ²` at some `(p, q, r)` with `p, q, r` not all equal (B2); a path power with a nontrivial eigenvalue other than `(p−q)^{k+2}`, `(p+q−2r)^{k+2}` (B3); a pendant path whose factor depends on `v_b` (B4).
- A sphere factor other than `4π sinh β/β` (one attachment) or `4π sinh(β|w|)/(β|w|)` (two), or a nonpositive coefficient in `z cosh z − sinh z` (C1–C2).
- A plaquette, cube or forest value other than those of Q4, or a failure of the average identity (D1–D4); the two unrecorded corners' combined factor constant at a non-constant rule (E1).

## Boundaries and non-claims
This note proves, for the six-axis product rule and the sphere rule, that the free-window and integrated-exterior readings of the static law on a finite set of records coincide if and only if every unrecorded component touches one recorded site, with exact witnesses and the separating clause pair recorded; it does not say which reading the axioms intend, does not treat infinite unrecorded exteriors beyond finite sets, does not treat the formation reading, does not select a reading, rule or coupling as physical, and adopts no clause. No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision. No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Imports
- `minimal_axioms`: the sentences quoted under Premises.
- Block 01 and the possibility-covariance note (both on `main`): the static reading and the sphere law; proposed, unaudited. The campaign meta note (on `main`): the seam and the format. PRs #8149–#8151, #8153–#8157 (open) referenced in Q5(b) as evidence addresses only.
- Re-proved at scope: Q1 (the product form), Q2 (value covariance and transitivity), Q3 (the spectral decomposition; the commutant of three inequivalent irreducibles; the sphere integral; the series), Q4 (enumeration).
- Named standard imports at definition level (never as authority for physics): that the commutant of a representation decomposing into pairwise inequivalent irreducible representations is spanned by the isotypic projectors (Schur); the polar-coordinate evaluation of the sphere integral.
- Reference only (named, not used): the Markov property of Gibbs fields.

## Review record
Supervisor-run block (owner directive: don't stop; assess the next lane at each conclusion; no subagents). The lane assessment before this block found the queue down to hard or incremental items and the other lanes owned by the owner's live integration or by other workers; the campaign meta note's untouched seam on unrecorded sites was taken. The control (`specs/supervisor_control_block24_unrecorded_sites.py`) computed the eigenvalues, the `φ²` differences, the pendant and bridging path factors, the three plaquette witnesses, the cube witness, the sphere factors and the forest before the contract (a first draft with a `3×3` window plus pendants was infeasible at `6^{12}` configurations and was replaced by the plaquette); the lens pass is in `GOAL_block24.md`; the primary seat wrote Q1–Q5 and the runner; the refuting pass (`CHECKER_block24_findings.md`) recomputed the plaquette and cube witnesses by floating-point tensor contraction, tested one-attachment constancy on random pendant components and two-attachment nonconstancy on random bridging components at random positive weights through the isotypic eigenvalues, and checked the sphere factor by quadrature.

## Verification

```bash
python3 scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py
python3 scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py --list-mutations
python3 scripts/admissibility_rule_unrecorded_sites_free_window_versus_integrated_exterior_readings_2026_09_15.py --mutation claim_reading_selected_injected
```

Families: A authority and inputs; B the spectral decomposition, the constancy criterion, the path powers, the pendant paths; C the sphere factors; D the witnesses and the average identity; E the two-corner component; F fences, forbidden phrases, the floating-point self-scan, the placement of the classical names; G the resolution lines. Each of the 13 declared mutations fails in exactly one family. Expected final line: `TOTAL: PASS=20 FAIL=0`.
