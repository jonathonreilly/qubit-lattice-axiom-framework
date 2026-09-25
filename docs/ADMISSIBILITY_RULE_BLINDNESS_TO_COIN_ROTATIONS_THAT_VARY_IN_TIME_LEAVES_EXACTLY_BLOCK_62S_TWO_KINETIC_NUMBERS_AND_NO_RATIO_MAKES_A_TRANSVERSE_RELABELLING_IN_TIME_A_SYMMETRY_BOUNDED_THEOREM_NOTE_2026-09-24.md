---
claim_id: admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: Conditional constant-coefficient ultralocal quadratic kinetic forms for a supplied positive-orientation
  frame and the explicit quadratic (h,u) model. Independently imposed time-dependent rotation invariance leaves
  two metric kinetic coefficients. Exact isotropic-stretch coefficient, gradient and transverse variational identities,
  mode determinant and cube-symmetric coefficient classification. Nonzero momentum and nonzero transverse directions;
  alpha nonzero for the transverse obstruction and alpha positive for kinetic energy positive only for alpha>0.
  No nonlinear constraint closure, all-field impossibility, universal lattice dynamics or finite-wave-number common
  light cone is proved.
upstream_dependencies:
- admissibility_rule_a_ledger_linear_in_the_rates_every_clock_a_multiplier_the_ledger_a_wall_term_and_the_curvature_member_doubles_the_bending_bounded_theorem_note_2026-09-21
- admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
- admissibility_rule_bond_strains_and_plaquette_curls_a_field_energy_per_local_tick_that_does_not_see_the_coins_axes_is_the_curvature_member_bounded_theorem_note_2026-09-21
- admissibility_rule_in_the_curvature_member_the_clock_is_a_constraint_a_bodys_change_of_energy_acts_at_once_unless_formation_keeps_energy_local_bounded_theorem_note_2026-09-23
runner: scripts/admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_2026_09_24.py
---

# Blindness to coin rotations that vary in time leaves exactly block 62's two kinetic numbers, and no ratio makes a transverse relabelling in time a symmetry

**Date:** 2026-09-24
**Type:** bounded_theorem
**Status:** bounded-support (exact within blocks 60, 62 and 64 as landed; harvest block from a Grok-refereed probes attempt; nothing adopted or registered; unaudited)

This note works within blocks 60, 62, 64 and 101 as landed on main, with block 62's frame, symmetric member and kinetic family; it reports what blindness to coin rotations and to relabellings, both varying in time, fixes in the member's kinetic term and what it leaves supplied; block 112 (open) is placed, not used; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Within the explicitly supplied quadratic model, time-dependent coin-rotation invariance leaves two kinetic coefficients. Gradient relabelling invariance imposes beta=-alpha, while arbitrary time-dependent transverse relabellings fail for alpha!=0. These are additional invariance demands, not deductions from the axioms' lack of privileged possibilities or sites. The obstruction concerns only the displayed (h,u) model. It does not rule out other fields, constraints or changes to the action.

The isotropic-stretch coefficient is 12alpha+36beta. The two transverse trace-free modes have omega squared=K p squared/(4alpha); their long-wavelength speed equals1 when alpha=K/4 in the stipulated units. The invariance demands do not determine that ratio. The cube-symmetric calculation extends the kinetic ansatz to three constant coefficients, still only quadratic and ultralocal.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-24.
  - "No possibility is privileged. Possibilities are distinguished by the supplied algebraic structure alone." This does not itself grant invariance under arbitrary time-dependent rotations; that demand is separately imposed here.
  - "No site is privileged." Arbitrary time-dependent continuous relabelling invariance is separately imposed here.
  - "Admissibility is not a dynamics axiom." The memo does not "define a time metric". The frame, the member and its kinetic term are supplied clauses. Nothing is adopted.
- **The frame** (block 62 T1 as landed), restricted here to det E>0 and w>0. `E[j, a] = E^j_a`, with bond direction `j` and coin axis `a`. The inverse metric is `g⁻¹ = EEᵀ` and the metric is `g = E⁻ᵀE⁻¹`. The frame's rate per tick is `V = ĖE⁻¹/w`, where `w` is the local rate (block 60).
- **Invariants.** `I₁ = V_jk V^jk = tr(VᵀgVg⁻¹)`, `I₂ = V^j_k V^k_j = tr V²` and `I₃ = (V^j_j)²`.
  - **Premise:** the kinetic term is a constant-coefficient ultralocal quadratic form in `V` built with the metric alone, with no other tensors or derivatives, so it is `c₁I₁ + c₂I₂ + c₃I₃` times the weight-one density `w det e`.
  - `e = E⁻¹` is the co-frame (block 64), so `det e = √det g`.
  - A form of the cube's symmetry only is outside this premise. See N1.
- **The member** (block 62 T3 as landed). Strains `h = −(ε + εᵀ)` at first order around `E = 1 + ε`, with lattice symbols `p_j = 2 sin(k_j/2)`:
  - `R₁ = −(p·h·p − p² tr h)`;
  - `R₂ = −¼p²h_ijh_ij + ½|hp|² − ½(p·h·p)tr h + ¼p²(tr h)²`, the Fierz–Pauli form in block 62's words;
  - the Lagrangian `α ḣ_ijḣ_ij + β ḣ² + K(uR₁ + R₂)` with `w̄ = 1`, where `u` is the rates' multiplier and `K > 0` is block 60's member constant.
- **Relabellings.** `h → h + pξᵀ + ξpᵀ` leaves `R₁` and `R₂` unchanged for every `ξ` (block 62 T3). The *gradient* relabelling is `ξ ∥ p`; the two *transverse* ones have `p·ξ = 0`.
- **Mode equations** (block 62 T4 as landed): the Hessian in `(h₁₁, …, h₃₃, u)` of `X(α h_ijh_ij + β(tr h)²) + K(uR₁ + R₂)`. X=omega squared for harmonic time dependence exp(-i omega t); the displayed matrix is the mode equation after varying the quadratic action. Nonzero p is assumed for all directional iff statements.
- **Comparators, named only:**
  - the supermetric of DeWitt (`β = −α` is its value);
  - the uniqueness results of Hojman, Kuchař and Teitelboim for representations of the algebra of deformations of a slice;
  - the shift vector of the comparator's lapse-and-shift form.

## Theorem T1 — rotation blindness leaves exactly two kinetic numbers

*Statement.* Let `E(t)` be any positive-orientation invertible frame with w>0 and `R(t)` any rotation of the coin axes that varies with the site and the tick, so that `E → ERᵀ`.
- (a) `V` shifts by `E(ṘᵀR)E⁻¹/w`. Lowered, the shift `E⁻ᵀ(ṘᵀR)E⁻¹/w` is antisymmetric, and it ranges over every antisymmetric matrix as `R` varies.
- (b) `sym(gV) = −ġ/(2w)`.
- (c) Write `gV = S + A`, with `S` symmetric and `A` antisymmetric. Then `I₁ = |S|² + |A|²`, `I₂ = |S|² − |A|²` and `I₃ = (tr g⁻¹S)²`, where `|S|² = tr(g⁻¹Sg⁻¹S)` and `|A|² = −tr(g⁻¹Ag⁻¹A)`.
- (d) So `c₁I₁ + c₂I₂ + c₃I₃` is unchanged by every such rotation iff `c₁ = c₂`. The blind kinetic terms are exactly `(det e/w)[α tr(g⁻¹ġ g⁻¹ġ) + β(tr g⁻¹ġ)²]`, with `α = c₁/2` and `β = c₃/4`. At first order around the identity frame this is `(1/w)[α ḣ_ijḣ_ij + β ḣ²]`, block 62's rotation-invariant family.

*Proof.*
- (a) `ṘᵀR` is antisymmetric because `RᵀR = 1`. `V′ = (ĖRᵀ + EṘᵀ)RE⁻¹/w = V + E(ṘᵀR)E⁻¹/w`. With `g = E⁻ᵀE⁻¹`, `g·E(ṘᵀR)E⁻¹ = E⁻ᵀ(ṘᵀR)E⁻¹`, which is antisymmetric. It is onto the antisymmetric matrices because `E` is invertible.
- (b) `ġ = −g(ĖEᵀ + EĖᵀ)g` and `Eᵀg = E⁻¹`, so `gĖE⁻¹ + (gĖE⁻¹)ᵀ = −ġ`.
- (c) The cross terms vanish, by transposition and cyclicity of the trace: the trace of a symmetric matrix times an antisymmetric one is zero. `tr(g⁻¹A) = 0`.
- (d) A rotation changes only `A`, so the form changes by `(c₁ − c₂)(|A′|² − |A|²)`. Take `A = 0` and any nonzero shift. Then substitute (b).

∎

*Checked (B1).* A generic rational frame `E = [[2,1,0],[½,3,1],[0,−1,2]]`, with nine symbolic rates and three symbolic rotation rates:
- `I₁ + I₂` and `I₃` are unchanged, and `I₁ − I₂` is not;
- `sym(gV) = −ġ/(2w)`;
- the lowered shift is antisymmetric.

## Theorem T2 — the isotropic stretch

*Statement.* For `h = 2λδ` the kinetic term is `(12α + 36β) λ̇²/w`, block 60 T5's `c_k`. The coefficient increases with `β`, so for `α > 0`:
- it is negative (an algebraic sign condition only; actual evolution additionally needs the supplied rate constraint and contents assumptions) iff `β < −α/3`;
- it is `−24α` at `β = −α`, inside that region;
- it is `−6K` at `(α, β) = (K/4, −K/4)`, block 60 T5's comparator value.

*Proof.* `ḣ_ijḣ_ij = 12λ̇²` and `(tr ḣ)² = 36λ̇²`. ∎

*Checked (C1).* The coefficient, its root `β = −α/3`, and the two values.

## Theorem T3 — no ratio makes a transverse relabelling in time a symmetry

*Statement.* Let `ζ(t)` be any function of the tick.
- (a) **Transverse.** Let p!=0 and choose any nonzero xi-hat perpendicular to p. The runner uses (p2,-p1,0), which is nonzero when p1 or p2 is nonzero; the proof applies also to the other axis directions. The relabelling `h → h + (pξ̂ᵀ + ξ̂pᵀ)ζ` leaves `R₁` and `R₂` unchanged. It changes the Lagrangian by exactly `4αζ̇ ξ̂·ḣ·p + 2αp²|ξ̂|²ζ̇²`, with no `β`.
  - The variational derivative of this change in `ζ` is `−4α(ξ̂·ḧ·p + p²|ξ̂|²ζ̈)`, which is not zero.
  - So the change is not a total derivative, and for no `(α, β)` with `α ≠ 0` is the relabelling a symmetry.
  - The multiplier `u` cannot absorb it: `u` multiplies `R₁`, which the relabelling leaves unchanged. Only h and u occur in this model. On a pure transverse configuration R1=0, so any regular multiplier shift contributes zero while the kinetic change need not vanish; thus u cannot cancel the obstruction.
- (b) **Gradient** (block 112 T2's field part, re-checked). The relabelling `h → h + ppᵀζ` with `u → u − (2α/K)ζ̈` changes the Lagrangian by exactly `−2α d(ζ̇R₁)/dt + (α + β)(2p² tr ḣ ζ̇ + p⁴ζ̇²)`. That is a total derivative iff `β = −α`.

*Proof.*
- (a) `tr(δḣ) = 2p·ξ̂ζ̇ = 0`, so the `β` term does not change. `tr(ḣδḣ) = 2ζ̇ ξ̂·ḣ·p` and `tr(δḣ²) = 2p²|ξ̂|²ζ̇²`. A total derivative has zero variational derivative.
- (b) Expand. `R₁` and `R₂` are unchanged, and the shift of `u` adds `−2αζ̈R₁`.

∎

*Checked (D1).* Both changes are computed with `h`, `u` and `ζ` as symbolic functions of the tick at symbolic `p`, together with the variational derivative.

*Reading.* This is an off-shell identity at quadratic order. It proves neither nonlinear constraint closure nor the impossibility of other fields or modified constraints. Under this action alone, transverse solutions can drift; positivity requires alpha>0.

## Theorem T4 — quadratic modes and long-wavelength speed

*Statement.*
- (a) Block 62's `7×7` mode determinant, with `K` explicit, is `−32K²X³α²(α + β)(p²)²(Kp² − 4αX)²`.
- (b) `M(ppᵀ, 2αX/K) = 2(α + β)Xp²(δ, 0)`. So the gradient direction, with the rates' multiplier, is null at every `X` iff `β = −α`.
- (c) For alpha!=0 and nonzero transverse xi, the transverse direction `n_t = (pξ̂ᵀ + ξ̂pᵀ, u = 0)` is annihilated at `X = 0`, and `n_tᵀMn_t = 4αXp²|ξ̂|²`. So it is not null at `X ≠ 0`: its evolution is `ζ̈ = 0`, a uniform drift with kinetic energy `2αp²|ξ̂|²ζ̇²`.
- (d) The travelling pair has `X = Kp²/(4α)` (block 62 T4), which for alpha>0 has long-wavelength speed sqrt(K/(4alpha)). Matching speed1 requires alpha=K/4; the lattice symbol still gives finite-wave-number anisotropy. Neither T1 nor T3 involves `K`, so the two blindness demands leave `α/K` free.

*Proof.* (a) Rotate nonzero p to (r,0,0). The symmetric-tensor coordinate transformation has determinant1, so the Hessian determinant is unchanged. In these coordinates R1=r^2(h22+h33) and R2=r^2(h22*h33-h23^2)/2; direct block factorization gives the stated expression. This is an algebraic rotation of the symbol, not a rotation symmetry of the discrete lattice. (b) and (c) By multiplication, using T3. (d) The transverse trace-free subspace h11=h12=h13=0,h22=-h33 gives two kinetic coefficients proportional to alpha and restoring coefficients proportional to K p^2/4, including at beta=-alpha where the full determinant vanishes identically. T1's condition `c₁ = c₂` and T3's `β = −α` do not contain `K`. ∎

*Checked (E1).*
- The determinant at `p = (1, 2, 2)` and `(2/5, 1/3, −3/7)`.
- The gradient image, each entry zero or carrying `α + β`, and zero at `β = −α`.
- The transverse direction at `X = 0`, and its quadratic value.
- The light-cone condition.

## Theorem T5 — without the metric premise, the gradient relabelling forces isotropy and the ratio

*Statement.* Replace the metric-built premise by block 62's cube family, `M₁Σ_j ḣ_jj² + M₂Σ_{i<j} ḣ_iiḣ_jj + M₃Σ_{i<j} ḣ_ij²`. This is the general quadratic form in `ḣ` with the cube's symmetry: the trace, the traceless diagonal and the off-diagonal part each carry one number.
- (a) The gradient relabelling in time, `h → h + ppᵀζ` with `u → u + (c/K)ζ̈`, is a symmetry up to a total derivative iff `(M₁, M₂, M₃) = (0, c, −c)`.
  - That is the rotation-invariant member (`M₃ = 2M₁ − M₂`) at `β = −α`, with `α = −c/2`.
  - For `α > 0` the shift is T3's, `−(2α/K)ζ̈`.
- (b) A transverse relabelling in time, `ξ = p × a` for any constant `a`, is a symmetry iff `(M₁, M₂, M₃) = (M, 2M, 0)`. That is the pure trace term `M(tr ḣ)²`. It has `α = 0`, so the transverse trace-free kinetic term is absent. An identically zero determinant alone does not classify the remaining degenerate dynamics.
- (c) Both together hold only for the zero kinetic term.

*Proof.*
- (a) The change of the Lagrangian is `ζ̇·ℓ(ḣ) + q(p)ζ̇² + cζ̈R₁`. Since `ζ̇ℓ(ḣ) = d(ζ̇ℓ(h))/dt − ζ̈ℓ(h)`, the change is a total derivative iff `ℓ = cR₁` and `q = 0`.
  - `ℓ(ḣ) = 2M₁Σ_i p_i²ḣ_ii + M₂Σ_i ḣ_iiΣ_{j≠i}p_j² + 2M₃Σ_{i<j}p_ip_jḣ_ij`.
  - `R₁ = Σ_i h_iiΣ_{j≠i}p_j² − 2Σ_{i<j}p_ip_jh_ij`.
  - So `M₁ = 0`, `M₂ = c` and `M₃ = −c`. Then `q = M₁Σp_j⁴ + (M₂ + M₃)Σ_{i<j}p_i²p_j² = 0`.
- (b) The multiplier does not couple, because `R₁` and `R₂` are unchanged. The `ζ̇²` coefficient must vanish for every `p` and every `ξ ⊥ p`. At `p = e₁`, `ξ = e₂` it is `M₃`. At `p = (1, 1, 0)`, `ξ = (1, −1, 0)` it is `8M₁ − 4M₂`. With `M₃ = 0` and `M₂ = 2M₁` the term is `M₁(tr ḣ)²`, and `tr δḣ = 2p·ξζ̇ = 0`.

∎

*Checked (D2).* Every variational derivative of each change is reduced to its coefficients in the fields' derivatives, `p` and `a`, and the linear systems are solved exactly.

*Reading.*
- Block 62 T4(c) showed that a cube-only kinetic term can make the speed depend on direction.
- The gradient part of relabelling blindness in time rules that out by itself, with no premise about the metric, and lands on `β = −α`.
- So T1's premise is needed only for the count of two when the relabelling demand is dropped.
- Within this three-coefficient family, transverse invariance removes the transverse trace-free kinetic term.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 62 as landed: the kinetic family (1/wbar)[alpha hdot_ij hdot_ij + beta hdot^2] is declared, not derived; zero-frequency directions can admit secular motion unless constraints or identifications remove them; alpha = K/4 is not forced"
source_of_blocker_text: block 62 as landed
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "a field that couples to the transverse relabellings (bond rates of block 59, the twist of block 65) or a proof that the clauses cannot supply one; beyond second order, block 112's closure; a clause sharing one light cone between walker and field"
conditional_surface_status: "T1 exact for every frame under the metric-built premise; T2-T5 exact at second order in the strains at every lattice wave vector; T5 within block 62's cube family"
hypothetical_axiom_status: "the frame, the member and its kinetic term are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 60 T5: `c_k` and uniform motion of a closed lattice.
  - Block 62: the frame, the member, the kinetic family (declared), the determinant, the warning about secular motion, and `α = K/4` not forced.
  - Block 64: a rotation-blindness calculation within its supplied six-term continuum ansatz and truncation orders.
  - Block 101: the clock is a constraint, and `α + β = 0` is special.
- **Opened, not landed.** Block 112 (PR #9152): at beta=-alpha a bounded placement calculation is available; general nonlinear constraint closure is not established here. Its T2 already used this probes attempt's gradient part (#8734). That part is only re-checked here, as the contrast to T3(a).
- **The probes attempt.** `the-kinetic-term-under-the-two-blindness-demands` a1 (Claude Opus 5.5, issue #8734) found T1–T4 and the transverse cost. A Grok referee confirmed it (#8981).
- **In the literature.**
  - DeWitt's supermetric and its value `β = −α`.
  - The uniqueness of the comparator's constraint algebra (Hojman, Kuchař, Teitelboim).
  - The comparator's shift vector, which absorbs relabellings in time.
  - The Fierz–Pauli form.

  All reference only.
- **New here:**
  - T1 as the derivation of block 62's declared family, exact for every frame;
  - T2's placement of `β = −α` inside block 60 T5's region;
  - T3(a) and T4(c): the transverse relabellings are real drifts at every ratio, the precise form of block 62's warning, and a third-column item;
  - T4(d): the blindness demands do not touch `α/K`;
  - T5, the supervisor's own addition (same model family as the attempt's author; not refereed by another family): in block 62's cube family the gradient relabelling demand alone forces the rotation-invariant member at `β = −α`;
  - an independent exact runner.

## Exact target and obligation graph

Target: what the two blindness demands, extended from tick to tick, fix in block 62's kinetic term. The obligations are:
- (O1) the rotation demand (T1);
- (O2) the placement of the closing ratio against block 60 (T2);
- (O3) the relabelling demand, transverse and gradient (T3);
- (O4) the mode-level form and what stays free (T4);
- (O5) the cube family, without the metric premise (T5).

T1–T5 discharge them. Open beyond them: a field for the transverse relabellings, and orders beyond the second.

## No-Go Discipline Gate

The note's negative sentences:
- no `(α, β)` with `α ≠ 0` makes a transverse relabelling varying in time a symmetry of block 62's member, within the explicit (h,u) action;
- the blindness demands do not fix `α/K`.

### N1 — Routes by which the sentence could fail or mislead
1. *A field outside the clauses.* A vector field that couples to the transverse relabellings would absorb them, as the comparator's shift does. Candidates the attempt names: block 59's bond rates and block 65's twist. Neither is examined here, and the obstruction here concerns only the explicit (h,u) action.
2. *Kinetic terms outside the premise.* T5 treats block 62's cube family, the general form in `ḣ` with the cube's symmetry. Terms with `u̇`, higher derivatives, and forms in the frame's rate beyond first order with the cube's symmetry alone are not treated.
3. *Beyond second order.* T3 and T4 are at second order in the strains. Nonlinear closure remains outside this calculation; the related open placement is not evidence of it.
4. *Other transverse directions.* `ξ̂ = (p₂, −p₁, 0)` is one transverse direction. The two-dimensional transverse plane behaves the same way, because the change is `2αp²|ξ|²ζ̇²` plus a linear term for every `ξ ⊥ p`. The runner executes one direction per wave vector, at symbolic `p`.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
None beyond the supplied frame, member and kinetic premise.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility privileged; no site privileged; no dynamics or time metric in the axioms | yes |
| blocks 60, 62, 64 (landed) | `c_k`; frame, member, modes, kinetic family; rotation blindness | yes (restated) |
| block 101 (landed) | `α + β = 0` special | no (placement) |
| block 112 (open, PR #9152) | bounded placement calculation; the gradient part | no (placement; re-checked) |
| probes (#8734; Grok-refereed #8981) | T1–T4 first derived | yes (re-derived) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "in the supplied constant-coefficient ultralocal quadratic metric family, rotation invariance leaves two kinetic coefficients; for alpha!=0 arbitrary time-dependent transverse relabelling fails" | executed: the antisymmetric shift for a generic rational frame with symbolic rates | executed: the invariants before and after the rotation; `sym(gV) = −ġ/(2w)` | executed: the `7×7` determinant at two rational `p`; the gradient image; the transverse quadratic value | executed: both relabellings with the fields as symbolic functions of the tick; the variational derivative; the cube family's symmetry conditions solved exactly | second order in the strains (T1 for every frame); `α/K`, `K` and the kinetic term's existence declared |

### N6 — Partial-closure paths and primitive scan
`kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form of the repository. Block 62 left open whether it bears on `α = K/4`; that is still undecided here, and the primitive is not used. `scale_reference_primitive` and `realized_state_primitive` are not used. Nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "The transverse drift is harmless: nothing measures it."
  - *Reply:* Within the clauses it carries kinetic energy `2αp²|ξ|²ζ̇²`. A motion that nothing measures but that carries energy is exactly what the relabelling demand rules out.
  - Either the demand is dropped for transverse relabellings in time, or a field is supplied. Records alone do not decide which.

### N8 — Cross-cycle echo
- Block 64 treated a restricted field-energy ansatz under rotation blindness. T1 derives the kinetic term's form from the same blindness in time.
- Blocks 101 and 112 met `β = −α` from the constraint side. T3(b) meets it from the relabelling side.
- T3(a) is the part the lane had not stated.

## Falsifiers

- A metric-built quadratic form with `c₁ ≠ c₂` that is unchanged by every rotation varying in time.
- A ratio `(α, β)` with `α ≠ 0` at which the transverse change is a total derivative.
- A regular u shift cancelling the transverse kinetic variation on R1=0 within this explicit action.
- A mode at nonzero `X` along a transverse relabelling.
- A term of the cube family other than `(0, c, −c)` for which the gradient relabelling in time is a symmetry.

## Boundaries and non-claims

- The frame, the member and the kinetic term are supplied; the metric-built premise is declared.
- The three-coefficient cube kinetic family is treated in T5. Higher orders, derivative kinetic forms and additional fields are not classified.
- `α/K` and `K` are not derived.
- The comparator is named, not adopted. No gravitational claim is made.

## Imports

- [Supplied source, block 62](ADMISSIBILITY_RULE_ANGLES_ARE_THE_TILT_OF_THE_COINS_FRAME_WITH_THEM_TWO_DISTURBANCES_TRAVEL_AT_ONE_DIRECTION_FREE_SPEED_AND_THE_PRICE_IS_A_CONSERVED_STRESS_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 64](ADMISSIBILITY_RULE_BOND_STRAINS_AND_PLAQUETTE_CURLS_A_FIELD_ENERGY_PER_LOCAL_TICK_THAT_DOES_NOT_SEE_THE_COINS_AXES_IS_THE_CURVATURE_MEMBER_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 60](ADMISSIBILITY_RULE_A_LEDGER_LINEAR_IN_THE_RATES_EVERY_CLOCK_A_MULTIPLIER_THE_LEDGER_A_WALL_TERM_AND_THE_CURVATURE_MEMBER_DOUBLES_THE_BENDING_BOUNDED_THEOREM_NOTE_2026-09-21.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.
- [Supplied source, block 101](ADMISSIBILITY_RULE_IN_THE_CURVATURE_MEMBER_THE_CLOCK_IS_A_CONSTRAINT_A_BODYS_CHANGE_OF_ENERGY_ACTS_AT_ONCE_UNLESS_FORMATION_KEEPS_ENERGY_LOCAL_BOUNDED_THEOREM_NOTE_2026-09-23.md): only the current scoped mathematical statement is used; no premise adoption or retained grade is inferred.

- `minimal_axioms`. Blocks 60, 62, 64 and 101, restated or placed. Block 112, placed only.
- The probes attempt, refereed by another model family.
- Named standard imports, at definition level:
  - the decomposition of a matrix into symmetric and antisymmetric parts;
  - the trace's cyclicity;
  - the variational derivative (the Euler–Lagrange expression) and the fact that total derivatives have none;
  - determinants;
  - exact symbolic arithmetic.

## Review record

- **Who and when.** Supervisor-run block, the seventy-second since the source-link direction opened; 2026-09-24.
- **Provenance.**
  - The probes attempt by Claude Opus 5.5 derived the results (#8734). A Grok referee confirmed them (#8981).
  - The supervisor re-checked them with its own runner. It added:
    - the variational-derivative test;
    - the gradient image's factor;
    - the transverse direction's quadratic value;
    - the reading against block 62's warning;
    - T5, the cube family without the metric premise. T5 is the supervisor's own derivation, same model family as the attempt's author, and has not been refereed by another family.
- **Before writing.**
  - Main was re-fetched, and blocks 60, 62, 64 and 101 were read as landed.
  - The own-prior-art check found that block 112 (open) had already used the gradient part of #8734. This note was rescoped to the parts block 112 does not state.
- **Independence.** Mutation census: four mutations in families B–E, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_blindness_to_coin_rotations_that_vary_in_time_leaves_exactly_block_62s_two_kinetic_numbers_and_no_ratio_makes_a_transverse_relabelling_in_time_a_symmetry_2026_09_24.py
```

Expected: `TOTAL: PASS=12 FAIL=0`.
