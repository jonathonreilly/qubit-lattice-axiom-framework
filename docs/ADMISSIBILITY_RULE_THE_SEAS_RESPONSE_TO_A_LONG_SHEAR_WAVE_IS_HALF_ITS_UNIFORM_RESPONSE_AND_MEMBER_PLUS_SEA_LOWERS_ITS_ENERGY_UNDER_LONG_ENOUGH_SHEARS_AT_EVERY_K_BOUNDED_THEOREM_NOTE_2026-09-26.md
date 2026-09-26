---
claim_id: admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_and_member_plus_sea_lowers_its_energy_under_long_enough_shears_at_every_k_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's framed walk as landed (H = 1/2 sum_j {E^j(x).sigma, S_j}, symbol s_j = sin k_j, massless) with its filled negative band, block 62's member F_2 = -K wbar (u R_1 + R_2) with K > 0, and the sea's energy counted in the static energy (as block 147 does when the member sees the half-filled sea), at second order in a static frame wave E = 1 + eps cos(q.x), eps symmetric, with second-order perturbation theory for the filled sea supplied: (T1) the sea's energy per site is E2(q) = -<F(k, q)> with F = [|w|^2 (ab + s.s') - 2 (s.w)(s'.w)]/(ab(a + b)), s = s(k), s' = s(k + q), a = |s|, b = |s'|, w = eps (s + s')/4; 0 <= F <= ||eps||_F^2 (a + b)/4 uniformly, so E2 is continuous at q = 0 with limit half the uniform frame's second-order energy E_unif(eps) = -<|s x eps s|^2/(2|s|^3)>; (T2) E_unif(eps) < 0 for every symmetric eps not a multiple of the identity; (T3) on transverse traceless waves (tr h = 0, h p = 0) R_1 = 0 and the member's energy is K wbar (p^2/4) tr(h^2) = O(K |q|^2), so for every K > 0 member plus sea has negative static second-order energy under every long enough transverse traceless shear wave; (T4, the supervisor's extension, unrefereed) the same holds with block 139's staggered mass mu > 0: the mass anticommutes with every framed walk, so the sea is gapped by 2 mu, its response is continuous with the same half-uniform limit, and the massive uniform form -<(|s x eps s|^2 + mu^2 |eps s|^2)/(2 R^3)>, R^2 = |s|^2 + mu^2, is negative for every nonzero symmetric eps. The q^2 part of the sea's response is not decided. A harvest of probe #9299 (Claude Opus 5.5, the supervisor's family), confirmed by an other-family referee (#9332, Grok). Nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
  - admissibility_rule_angles_are_the_tilt_of_the_coins_frame_with_them_two_disturbances_travel_at_one_direction_free_speed_and_the_price_is_a_conserved_stress_bounded_theorem_note_2026-09-21
  - admissibility_rule_the_members_zero_mode_tests_the_zero_of_energy_if_the_member_sees_the_half_filled_sea_a_closed_lattice_bounces_or_cannot_move_bounded_theorem_note_2026-09-25
  - admissibility_rule_the_books_admit_one_rest_energy_the_staggered_mass_keeps_them_exactly_so_massive_content_meets_the_member_iff_alpha_equals_k_over_four_bounded_theorem_note_2026-09-25
runner: scripts/admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_2026_09_26.py
---

# The sea's response to a long shear wave is half its uniform response, and member plus sea lowers its energy under long enough shears at every K

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact within block 62's framed walk and member, with the sea's energy counted and second-order perturbation theory for the filled sea supplied; a harvest of probe #9299, confirmed by an other-family referee in #9332; nothing adopted or registered; unaudited)

This note works within block 62 as landed on main (the framed walk, its filled sea and the member's second-order energy) and counts the sea's energy in the static energy, as block 147 (landed) does when the member sees the half-filled sea; it reports the sea's response to a long shear wave and what the member's energy does against it; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 155 (held as an open PR) showed that the walker sea's energy falls under every uniform shear at fixed volume, where the member's energy is zero. It left long shear waves open: there the member has an energy, of order `K q²`. This note is a harvest of a probe result that another model family has confirmed. It closes that case.

- **T1: the sea's response is continuous at long wavelength.**
  - Under a static frame wave `E = 1 + ε cos(q·x)`, the filled sea's second-order energy per site is `E2(q) = −⟨F(k, q)⟩`. `F` is an explicit interband sum.
  - It obeys `0 ≤ F ≤ ‖ε‖_F²(a + b)/4`, uniformly in `k` and `q`.
  - So `E2(q)` tends, as `q → 0`, to half the uniform frame's second-order energy, `½E_unif(ε)`, with `E_unif(ε) = −⟨|s × εs|²/(2|s|³)⟩`.
- **T2: the uniform response is negative for every shear.** `E_unif(ε) < 0` for every symmetric `ε` that is not a multiple of the identity. No lattice constant is needed.
- **T3: the member does not hold long shear waves.**
  - On transverse traceless waves, block 62's `R₁` vanishes, and the member's energy is `K w̄ (p²/4) tr(h²)`, of order `K|q|²`.
  - The sea gives a negative amount that does not shrink as `q → 0`.
  - So for every `K > 0`, member plus sea has negative static second-order energy under every long enough transverse traceless shear wave.
- **T4: the massive sea too** (the supervisor's extension, unrefereed). With block 139's staggered mass `μ > 0`, the conclusion is the same.
  - The mass anticommutes with every framed walk, so the sea is gapped by `2μ`.
  - The massive uniform response `−⟨(|s × εs|² + μ²|εs|²)/(2R³)⟩`, with `R² = |s|² + μ²`, is negative for every nonzero strain, dilations included.

In plain terms: if the walkers' filled sea counts as energy, then a gentle, long-wavelength shear of the lattice lowers the total energy, however stiff the member is. The member's resistance to a wave vanishes as the wave gets longer, and the sea's gain does not.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The walk, the frame, the sea and the member are supplied clauses. Nothing is adopted.
- **Block 62 (landed on main).** Quoted by the runner (A3).
  - The generator `H = ½ Σ_j {E^j(x)·σ, S_j}`, with `S_j = (T_j − T_j†)/(2i)` and symbol `s_j = sin k_j`.
  - `h = −(ε + εᵀ)`.
  - The member `F_2 = −K w̄ (u R_1 + R_2)`, with `R₁ = p² tr h − pᵀhp` and `R₂` as landed, in `p_j = 2 sin(q_j/2)`.
  - `R₁` and `R₂` are unchanged by relabellings (T3(b)).
- **Block 139 (landed on main)**, for T4. The staggered rest energy is `H + mε`, with `ε(x) = (−1)^{x₁+x₂+x₃}`, and it anticommutes with the walk, so `(H + mε)² = H² + m²` (quoted, A4). Here the mass is written `μ`.
- **The sea.** Every negative-energy state of the walk is filled: the massless walk in T1–T3, and the walk with block 139's staggered mass in T4.
  - Its energy is counted in the static energy. This is the reading block 147 (landed) calls the member seeing the half-filled sea.
  - Under the other reading, the sea's frame-dependent energy is subtracted, and nothing here is driven.
- **Second-order perturbation theory for the filled sea** (Rayleigh–Schrödinger theory for a Slater determinant) is supplied. Only interband transitions enter; intraband ones are blocked by occupation (Pauli).
- **The static reading.** "Lowers its energy" means the static second-order energy. No dynamics is claimed.
- **Block 155** (open PR #9289, not landed) is placement only. Its explicit uniform form at `μ = 0`, `−(3A/8)Σh_ii² − (B/4)Σ_{i<j}h_ij²` with `A, B > 0`, agrees with T2 and is not used.
- **Names.** The identity `|s|²|v|² − (s·v)² = |s × v|²` is Lagrange's. The limit uses Lebesgue's dominated limit theorem.

## Domain qualifications

- The strain `ε` is symmetric, and `K > 0`. The rate `w̄` is the mean rate (1 at rest).
- In T1–T3 the walk is massless. The eight zeros of `s(k)` form a null set, and the bound of T1 holds through them. In T4 the mass `μ > 0` gaps the sea.
- T3 concerns transverse traceless amplitudes: `tr h = 0` and `hp = 0` at the wave's own symbol `p`. The statement is for every direction of `q`.
- Everything is at second order in the amplitude and static. The `q²` part of the sea's response is not decided here.
- These are conditional statements within supplied clauses, not a physical gravitational identification.

## Theorem T1 — the sea's response is continuous at long wavelength

*Statement.*
- For `E = 1 + ε cos(q·x)`, the filled sea's second-order energy per site is `E2(q) = −⟨F(k, q)⟩`. Here
  - `F = [|w|²(ab + s·s′) − 2(s·w)(s′·w)]/(ab(a + b))`;
  - `s = s(k)`, `s′ = s(k + q)`, `a = |s|`, `b = |s′|`;
  - `w = ε(s + s′)/4`.
- `0 ≤ F ≤ ‖ε‖_F²(a + b)/4 ≤ (√3/2)‖ε‖_F²`.
- `lim_{q→0} E2(q) = ½E_unif(ε)`, where `E_unif(ε) = −⟨(|s|²|εs|² − (s·εs)²)/(2|s|³)⟩` is the second-order energy of the filled band under the uniform frame `1 + ε`.

*Proof.*
1. **The vertex (B1).** `S_j` is diagonal in `k` with symbol `sin k_j`, and `cos(q·x)` moves `k` by `±q` with weight `½`. So `⟨k + q|V|k⟩ = σ·w`, with `w = ε(s + s′)/4`.
2. **The two-level element (B2).** `|⟨+, n′|σ·w|−, n⟩|² = [|w|²(1 + n·n′) − 2(n·w)(n′·w)]/2` for unit vectors `n = s/a` and `n′ = s′/b`.
3. **The filled sea.**
   - At second order, the filled band's energy changes by minus the sum of the squared interband elements over the gaps `a + b`.
   - The `±q` transitions give equal averages, under `k → −k`.
   - This gives `E2 = −⟨F⟩`.
4. **The bound.**
   - `F ≥ 0`, because its numerator is `2ab` times a squared element.
   - `s·s′ ≤ ab` and `|(s·w)(s′·w)| ≤ ab|w|²`, so the numerator is at most `4ab|w|²`.
   - `|w| ≤ ‖ε‖_F(a + b)/4`, and `a, b ≤ √3`.
   - The runner checks the bound exactly at 400 configurations with rational `a` and `b` (B5).
5. **The limit.**
   - Away from the eight zeros of `s`, `b → a` as `q → 0`, and `F(k, q) → F(k, 0) = (a²|εs|² − (s·εs)²)/(4a³)` (B3).
   - The uniform frame moves `−|(1 + ε)s|` at second order by `−2F(k, 0)` (B4).
   - `F` is bounded and the zone has finite measure, so the dominated limit theorem gives `E2(q) → −⟨F(k, 0)⟩ = ½E_unif(ε)`. The `½` is the mean of `cos²`.
   - `E2` is a quadratic form in `ε` whose entries each have this limit. So the limit is uniform on `‖ε‖_F = 1`. ∎

## Theorem T2 — the uniform response is negative for every shear

*Statement.* `E_unif(ε) < 0` for every symmetric `ε` that is not a multiple of the identity. So on traceless strains `E_unif` is negative definite: `E_unif(ε) ≤ −c‖ε‖_F²` with `c > 0`.

*Proof.*
- `|s|²|εs|² − (s·εs)² = |s × εs|² ≥ 0` (C1).
- The polynomial `|s × εs|²` in `s` vanishes identically only when `ε` is a multiple of the identity (C2). So otherwise it is positive on an open dense set of `s`.
- The map `k ↦ s(k)` has nonzero Jacobian `(cos(π/4))³` at `(π/4, π/4, π/4)`, so it is open there (C2). Hence the integrand `|s × εs|²/(2|s|³)` is positive on a set of `k` of positive measure, and the average is positive.
- An explicit case: at `s = (1, 1, 0)`, `ε = diag(1, −1, 0)` has gap 4 (C3).
- On traceless strains no nonzero `ε` is a multiple of the identity. The unit sphere is compact, so the form's maximum there is negative. ∎

## Theorem T3 — the member does not hold long shear waves

*Statement.*
- On a transverse traceless amplitude (`tr h = 0`, `hp = 0`):
  - `R₁ = 0`, so block 62's lapse constraint holds with `u = 0`;
  - `R₂ = −(p²/4) tr(h²)`;
  - the member's static energy per mode is `K w̄ (p²/4) tr(h²)`, with `|p| ≤ |q|`.
- Hence for every `K > 0` there is `q₀ > 0` such that, for `0 < |q| < q₀` in any direction and every nonzero transverse traceless amplitude, member plus sea has negative static second-order energy.
- The scale is `q₀² ∼ |E_unif|/(K w̄)`.

*Proof.*
- `R₂` is homogeneous of degree 2 in `p`, and `R₁`, `R₂` are unchanged by relabellings (D1).
- On transverse traceless `h`, the forms reduce as stated. This is checked for `p` along an axis, and at `p = (1, 2, 2)` with an exact transverse basis (D2).
- With `ε = −h/2`, the sea's part tends to `½E_unif(−h/2) ≤ −(c/8)‖h‖_F²`, uniformly in the direction of `h` (T1, T2). The member's part is at most a fixed multiple of `K w̄ |q|²‖h‖_F²`, whatever the normalization of the wave's two components at `±q`. ∎

## Theorem T4 — the massive sea too

*Statement* (the supervisor's extension, unrefereed). With block 139's staggered mass `μ > 0`:
- `με` anticommutes with the framed walk `½Σ_j{E^j(x)·σ, S_j}` for every frame field. So `(H + με)² = H² + μ²`, and the filled band lies at least `2μ` below the empty one.
- The sea's static second-order response to the wave is continuous in `q`, and tends to `½E_unif^μ(ε)`, where `E_unif^μ(ε) = −⟨(R²|εs|² − (s·εs)²)/(2R³)⟩` and `R² = |s|² + μ²`.
- `R²|εs|² − (s·εs)² = |s × εs|² + μ²|εs|²`. So `E_unif^μ(ε) < 0` for every nonzero symmetric `ε`, dilations included.
- Hence T3's conclusion holds for the massive sea: for every `K > 0`, member plus massive sea has negative static second-order energy under every long enough transverse traceless shear wave.

*Proof.*
- **The gap.** A hop joins sites of opposite parity, so `ε` anticommutes with every hop term, whatever the frame (E2; block 139 T3 for the uniform walk).
- **The limit.** Write the second-order energy with band projections: `−Tr[P₊(k ± q) V_± P₋(k) V_±†]/(R(k ± q) + R(k))`, summed over `k` and the two components `±q`. The denominators are at least `2μ`, and the projections onto the two levels `±R` are continuous. As `q → 0`, each component's vertex tends to half the uniform vertex at `k`. So `E2(q)` tends to `2 · ¼` of the uniform second-order energy, `½E_unif^μ(ε)`.
- **The uniform form.** The second-order coefficient of `−(|(1 + ε)s|² + μ²)^{1/2}` is `−(R²|εs|² − (s·εs)²)/(2R³)`, with the stated split (E1). For nonzero `ε`, `|εs|² > 0` on a set of positive measure, so the average is negative.
- **The member.** T3's bound does not involve the sea. ∎

## What this settles and what it does not

- **Settled.** With the sea's energy counted, the flat frame with the filled sea is not a minimum of the static second-order energy at any `K > 0`, for the massless sea and (T4, unrefereed) the massive one. Long transverse traceless shear waves lower it, and the member's energy only grows as `q²`. This answers block 155's open case of long-wavelength shears.
- **For landed block 147.** This is another consequence of the reading in which the member sees the half-filled sea. The owner's reading question is not decided here.
- **Not settled.**
  - The `q²` part of the sea's response, and whether it is relabelling-invariant. The probe evaluates it in floating point only (`0.0022838` and `0.0039358` for two relabelling modes). An exact enclosure needs about thirty one-dimensional integrals.
  - Dynamics.
  - The sea under one record per site.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 155 (open PR #9289): long-wavelength shears (q != 0) left open; block 147 as landed: which zero of energy the member sees"
source_of_blocker_text: probes task J:derive:the-seas-long-wavelength-shear-response-exactly
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "the q^2 part of the sea's response exactly; an other-family check of T4; the sea under one record per site"
conditional_surface_status: "static, second order; the massless walk (T1-T3) and block 139's staggered mass (T4); the sea's energy counted; second-order perturbation theory for the filled sea supplied"
hypothetical_axiom_status: "the walk, the frame, the sea, the member and the reading are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks.**
  - Block 62 (landed): the walk and the member.
  - Block 147 (landed): the reading in which the member sees the half-filled sea.
  - Block 155 (open PR #9289): the uniform shear, at fixed volume and at every size. It left long waves open.
- **Probes.**
  - #9198, worker `w-macbookpro9927a-j5403`, Claude Opus 5.5: the formula for the static response and floating-point `q²` values.
  - #9299, worker `w-jonathonsmac4f50-j9cf0`, Claude Opus 5.5, the supervisor's own model family, found T1–T3 exactly. It also reduced the `q²` part to one-dimensional integrals of Bessel type, evaluated in floating point only.
  - #9332, worker `w-macbookpro90c72-j7aa2`, `grok-4.6`, another model family, refereed it with its own checker: "HIT: confirmed - member plus sea is unstable to every long enough shear wave, at every `K > 0`." It did not rebuild the floating-point coefficients.
- **In the literature.** The second-order energy of a filled band under a static perturbation is standard perturbation theory (Rayleigh–Schrödinger, for a Slater determinant). The identity in T2 is Lagrange's. The limit is Lebesgue's dominated limit theorem. All are imports at definition level.
- **New here.**
  - The harvest.
  - An exact check of the bound in place of the probe's high-precision evaluation.
  - The uniformity of the limit in the strain, which T3 needs for every direction.
  - The exact transverse check at a non-axial wave vector.
  - T4, the massive sea: the gap from the staggered mass for every frame, and the massive uniform form. This is the supervisor's and has no other-family check.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: the member plus the counted sea under long shear waves. The obligations are:
- (O1) the premises (A3);
- (O2) the sea's response and its limit (B1–B5);
- (O3) the sign (C1–C3);
- (O4) the member's energy on transverse traceless waves (D1–D2);
- (O5) the massive sea (A4, E1–E2).

## No-Go Discipline Gate

The note's negative sentences:
- no `K > 0` makes the flat frame with the counted sea a minimum of the static second-order energy;
- the member's energy does not hold long transverse traceless shear waves.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *The sea's response vanishes as `q → 0`.* It does not: it tends to half the uniform response (T1). ATTEMPTED.
2. *Some shear leaves the sea's energy unchanged.* Only a multiple of the identity does (T2). ATTEMPTED.
3. *The multiplier `u` rescues the member.* `R₁ = 0` on transverse traceless waves, so `u` does not enter (D2). ATTEMPTED.
4. *A relabelling moves the wave out of the transverse traceless class.* `R₁` and `R₂` are relabelling-invariant (D1), and the sea's limit is taken at the given strain. ATTEMPTED.

Scope left open:
- dynamics;
- the `q²` part;
- the other reading of block 147, under which nothing is driven.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- Second-order perturbation theory for the filled sea, the counted reading and the static reading are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| block 62 (landed) | the walk, `h`, the member's forms | yes (quoted, A3) |
| block 147 (landed) | the counted reading | yes (as a declared premise) |
| block 139 (landed) | the staggered mass (T4) | yes (quoted, A4) |
| block 155 (open PR #9289) | the uniform shear; the open long-wave case | placement |
| probe #9299 and referee #9332 | the result and its confirmation | yes (re-derived, rerun exactly) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the sea's long-wave response is half its uniform response, negative for every shear; the member does not hold long transverse traceless waves" | executed: the vertex and the two-level element | executed: `F(k, 0)`, the uniform term, the bound at 400 exact configurations | executed: the gap polynomial; the member on transverse traceless waves at two wave vectors | executed: homogeneity and relabelling invariance; the massive uniform form; the staggered mass's anticommutation | not executed: the `q²` part; one record per site; T4's limit is argued, not computed at finite `q` |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "Block 155 already had this."
  - *Reply:* Block 155 treated uniform strains, where the member has no energy.
  - For waves the member costs `K q²`. Whether that holds long waves was open, and it does not.
- *Objection:* "A large `K` stabilizes."
  - *Reply:* Only down to `q₀ ∼ (|E_unif|/K)^{1/2}`. Longer waves still lower the energy.

### N8 — Cross-cycle echo
- Block 147: a closed lattice bounces or cannot move if the member sees the sea.
- Block 155: the counted sea forces a closed lattice to shear.
- This note: long shear waves lower the energy at every `K`.

## Falsifiers

- A non-scalar symmetric `ε` with `E_unif(ε) ≥ 0`.
- A `K > 0` and a transverse traceless amplitude for which member plus sea has nonnegative static second-order energy at all small `|q|`.

## Boundaries and non-claims

- Static and second order; the massless walk, and block 139's staggered mass in T4; the sea's energy counted.
- The walk, the frame, the sea and the member are supplied.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62, 139 and 147 (landed), restated and quoted. Block 155 (open PR) placed.
- Named standard imports, at definition level:
  - second-order perturbation theory for a Slater determinant (Rayleigh–Schrödinger);
  - Lagrange's identity;
  - Lebesgue's dominated limit theorem;
  - polynomial identity and open-map arguments;
  - exact symbolic and rational arithmetic.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.**
  - Probe #9299 (Claude Opus 5.5) was refereed by #9332 (`grok-4.6`, another family).
  - The supervisor wrote a new exact runner. It ports the attempt's exact parts, makes the bound check exact, and leaves out the floating-point `q²` evaluation.
  - T4 (v2, 2026-09-26) is the supervisor's extension to the massive sea. It has no other-family check.
- **Before writing.** Origin was re-fetched. Blocks 62 and 147 were read as landed. Block 155 was read on its PR branch. The own prior-art check covered memory, open PRs and main. It found block 155's open case and no earlier treatment of long waves.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_the_seas_response_to_a_long_shear_wave_is_half_its_uniform_response_2026_09_26.py
```

Expected: `TOTAL: PASS=21 FAIL=0`.
