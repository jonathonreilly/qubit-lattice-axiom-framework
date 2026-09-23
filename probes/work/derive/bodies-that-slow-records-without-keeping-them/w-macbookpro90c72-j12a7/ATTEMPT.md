# Attraction without growth: bodies that slow records without keeping them

Attempt 3 of 4. Worker `w-macbookpro90c72-j12a7`, model `claude-opus-5-5`. Script: `check.py` in this directory; it prints 7 checks, then a `SUMMARY` line and a `HIT` line.

**Provenance.**
- At claim time the tool printed the first sentence of attempt a2 (`w-jonathonsmac4f50-j40e2`, claude-opus-5, not refereed). I formed the plan below first, and read a2's `ATTEMPT.md` afterwards (section 3).
- **Overlap.** My unit `recapture-share-of-a-body-in-balance:a1` (issue #8765) used block 48's hitting probability and a directed-walk sweep. The sweep here is written afresh for classes of slowed records.
- **Sources.**
  - Block 48 (PR #8558): the streaming rule; the hitting probability `h` (T3a); the shells (T3b); the force (T3c) and its coefficient (T3e).
  - Block 49 (PR #8559): attraction is tied to growth.
  - Block 51 (PR #8563): the wind is not isotropic.
  - Block 52 (PR #8564): the biased-walk clause.

## 1. Statement attempted

**Setting.**
- **Records.** A record has content `v = m s`, with `s` a unit vector and `m ∈ (0, 1]`. It steps to `x + sign(s_k) e_k` at rate `m|s_k|/√3`. Its step frequencies are `w_k = |s_k|/|s|₁`, independent of `m`.
- **Slowing site.** It lets a record pass and replaces its content by `κv`.
- **Independent records.** No exchange and no scattering, except in (d).
- **Content law.** `ρ f(m, s)`, with `f(m, s) = f(m, −s)`. For (b), magnitude and direction are independent, `f = p(m) f_dir(s)`.

**(a) One slowing site at the origin.** At every site `x`, for content `m s`:
- unslowed records have density `ρ f (1 − h(x, s))`;
- slowed records have content `κ m s` and density `ρ f h(x, s)/κ`;
- here `h` is block 48's hitting probability: `n!/∏|x_k|! · ∏ w_k^{|x_k|}` on the closed octant of `s`, `n = |x|₁`, and zero elsewhere;
- at the origin itself every record present is slowed, with density `ρf/κ`.

Three consequences follow:
- the number flux is unchanged;
- the momentum density is unchanged;
- the density rises by `ρ f h (1/κ − 1)`. Every shell `|x|₁ = n` carries the whole slowed flux (`Σ_shell h = 1`), so the excess per shell, `ρf(1/κ − 1)`, is the same at every distance.

**(b) Two slowing sites, `κ₁` at the origin and `κ₂` at `x`.** Per tick, site 2 takes momentum

    (1 − κ₂) (ρ/√3) Σ f m² |s|₁ s [1 − (1 − κ₁) h(x, s)].

- The isotropic part, the `1`, cancels.
- The push is `(1 − κ₁)(1 − κ₂) ⟨m²⟩ F₄₈(x)`, with `F₄₈(x) = −(ρ/√3) ∫ f_dir |s|₁ s h(x, s)`. That is block 48's collisionless force, `−(ρ/(4π√3)) m(x) |r̂|₁² r̂/r² (1 + O(1/r))` (block 48 T3e). It points towards site 1.
- The force on site 1 is exactly the opposite: action equals reaction.
- Neither body grows: a slowing site keeps no record.

**(c) The price.**
- *Run-down per site.* A slowing site removes magnitude from the gas at `(1 − κ)(ρ/√3)⟨m²|s|₁⟩` per tick.
- *Per record.* A record crossing slowing sites of density `n_b` has, after `N` steps, `m = m₀κ^{K}` with `K ~ Bin(N, n_b)`. In mean field, `m(t) = m₀/(1 + (1 − κ) n_b |s|₁ m₀ t/√3)`.
- *Scalings.* The pull goes as `(1 − κ)²`. The run-down rate goes as `(1 − κ)`. The impulse a pair can exchange over the gas's whole life goes as `(1 − κ)/n_b`.
- *The inequality.* If the gas keeps half its magnitude for `T` ticks, then

      pull per pair ≤ 3⟨m²⟩|F₄₈| / (n_b ⟨|s|₁ m⟩ T)² = 4⟨m²⟩|F₄₈| / (3 n_b² ⟨m⟩² T²)

  for the uniform sphere.

**(d) Healing.** With re-draws at rate `γ`, a slowed record keeps its slowed content to shell `n` with probability `h q^n`, where `q = κa/(κa + γ)` and `a = m|s|₁`. The slowed beam is gone within about `κa/γ` steps, shorter than the unslowed mean free path `a/γ`. Beyond that length:
- the slowing site sources no conserved quantity: the number flux is unchanged and the net momentum taken is zero;
- so no `1/r²` shadow force survives. This last point is argued, not proved.

**(e) What it adds, and whether it survives.** The mechanism adds:
- a menu with magnitudes;
- a slowing clause.

It lives in the collisionless regime, with block 48's anisotropic coefficient `m(x)|r̂|₁²`, and it does not survive collisions (d). Under block 52's biased walk the directed-walk structure is lost; see S10.

## 2. Steps

Each step is marked PROVED (argument given in full), CHECKED (verified by `check.py`, check named in brackets) or ASSUMED.

**S1 — PROVED. Part (a).** Fix a content `m s`, and write `a_k = m|s_k|/√3` and `A = Σ a_k`.

*Unslowed records.* The stationary equations are:
- at `x ≠ 0`: `A n_u(x) = Σ_k a_k n_u(x − σ_k e_k)`;
- at the origin: `n_u(0) = 0`, because an arriving record is slowed at once;
- far upstream: `n_u → ρf`.

*Slowed records.* They step at rates `κa_k`:
- at `x ≠ 0`: `κA n_s(x) = Σ_k κ a_k n_s(x − σ_k e_k)`;
- at the origin: `κA n_s(0) = Σ_k a_k n_u(−σ_k e_k) = Aρf`, since the upstream neighbours have `h = 0`.

*Solution.* `h` satisfies `h(0) = 1` and `h(x) = Σ w_k h(x − σ_k e_k)` elsewhere. So `n_u = ρf(1 − h)` and `n_s = ρf h/κ` solve the equations. The solution is unique among bounded fields that vanish in the perturbation far upstream. This is block 48 T3a's argument: the difference of two solutions is its own average over the walk run backwards.

*Consequences.*
- Number flux: `A n_u + κA n_s = Aρf`.
- Momentum density: `n_u m s + n_s κ m s = ρf m s`.

**S2 — CHECKED [A1, A2].** Exact Fractions, by a sweep along each direction's octant on `[−4, 4]³`.
- The data: 54 rational directions (the signed permutations of `(1,0,0)`, `(3/5,4/5,0)` and `(2/3,2/3,1/3)`), two magnitudes `m = 1, 1/2`, and `κ = 1/3`.
- The equations are directed, so the block solution equals the infinite-lattice one.
- Every class flux equals the closed form at every site, and the flux and the momentum density are unchanged.
- The slowed flux through every shell `n ≤ 4` is exactly 1.

**S3 — PROVED. Part (b).** Records reaching `x` come from upstream sites, so the arrival rates at `x` do not depend on site 2 itself. A directed walk visits `x` at most once and the origin at most once.
- *Arrivals at `x`.* Unslowed records arrive at `Aρf(1 − h(x, s))`, with content `m s`. Records slowed at the origin arrive at `κA · ρf h/κ = Aρf h(x, s)`, with content `κ₁ m s`.
- *Momentum taken.* Site 2 takes `(1 − κ₂)` of each arriving content. That gives the formula in (b).
- *Isotropic part.* `Σ f m²|s|₁ s = 0`, because `f(m, s) = f(m, −s)`.
- *Magnitudes.* With `f = p f_dir` the magnitudes enter only through `Σ p m² = ⟨m²⟩`.
- *Action and reaction.* The same argument at the origin gives `h(−x, s) = h(x, −s)`. So `F₁ = −F₂` exactly, for every `κ₁` and `κ₂`.
- *No growth.* A slowing site keeps no record, so the capture rate is zero, and block 49's law (the wind is tied to growth) assigns these bodies no wind.

**S4 — CHECKED [B1, B2].** Both sites are solved jointly, including records slowed by both. Three configurations:
- `x = (2,0,0)` with `κ = (1/3, 1/2)`;
- `x = (2,1,1)` with `κ = (1/3, 1/2)`;
- `x = (1,2,0)` with `κ = (3/4, 1/5)`.

In each:
- the momentum taken equals the closed form and equals `(1 − κ₁)(1 − κ₂)⟨m²⟩F₄₈`;
- `F₁ = −F₂`;
- the push points towards site 1;
- a lone site takes zero;
- the two-magnitude force equals `⟨m²⟩ = 5/8` times the unit-magnitude force;
- at each site arrivals equal departures.

For example, at `(2,1,1)`: `F = (−1/675, −8/6075, −8/6075)/√3`.

**S5 — cited.** The asymptotics of `F₄₈` are block 48 T3(e); they are not re-derived here.

**S6 — PROVED, given one ASSUMED model. Part (c).**
- *ASSUMED: placement.* The slowing sites are placed independently with density `n_b`.
- *Per step.* A directed walk visits distinct sites, so the number of slowing sites met in `N` steps is `Bin(N, n_b)`. Hence `E m = m₀(1 − (1 − κ)n_b)^N` and `E m² = m₀²(1 − (1 − κ²)n_b)^N`.
- *Continuous time, mean field.* `dm/dt = −(1 − κ) n_b |s|₁ m²/√3`, so `m(t) = m₀/(1 + ct)` with `c = (1 − κ)n_b|s|₁m₀/√3`.
- *Impulse.* The pull on a pair is `(1 − κ)²⟨m²⟩(t)|F₄₈|`. Integrating it gives `(1 − κ)² m₀²/c ∝ (1 − κ)/n_b`.
- *The inequality.* Half the magnitude kept at `T` means `cT ≤ 1`, i.e. `(1 − κ) ≤ √3/(n_b|s|₁m₀T)`. That gives the pull bound in (c).
- *A2's cancellation.* For bodies whose momentum accumulates the push, the displacement gained while the gas lasts goes as `F₀τ²/M ∝ (1 − κ)²/((1 − κ)n_b)² = n_b^{−2}`. So `κ` cancels, as a2 found by a different route.

**S7 — CHECKED [C1, C2].** The binomial identities hold exactly at `N = 7`, `n_b = 1/5`, `κ = 1/3`. Sympy verifies the ODE solution, the impulse `m₀/c`, the linear dependence on `(1 − κ)`, and the solution of the inequality.

**S8 — PROVED, then ARGUED. Part (d).**
- *PROVED.* With an independent re-draw clock of rate `γ`, each step of a slowed record is a race between the hop (rate `κa`) and the re-draw. So the slowed record reaches shell `n` still carrying its slowed content with probability `h(x, s) q^n`. The anisotropic shadow force is carried only by records whose content still remembers the passage. A re-drawn content is independent of its history.
- *ARGUED.* The re-drawn records carry no direction towards the origin, and the slowing site changes neither the number current nor the net momentum. So conserved-density fields have no monopole source, and no `1/r²` force survives beyond a few slowed mean free paths.
- *Not solved.* The pair re-draw on the momentum class loses the slowed record's memory at its first collision as well, but its conserved-momentum bookkeeping is not solved here.

**S9 — CHECKED [D1].** At `κ = 1/3`, `a = 3/2`, `γ = 1/10`: `q = 5/6`, and `q^n = 0.833, 0.402, 0.162, 0.026` at `n = 1, 5, 10, 20`. The slowed decay length is 5 steps, against 15 for unslowed records.

**S10 — Part (e).**
- **Additions.** Contents with magnitude `m < 1` (blocks 44–52 use unit contents), and a slowing site as a new kind of body. Neither is in the axioms.
- **Block 51.** The force lives where there is no scattering, so it keeps block 48's anisotropic coefficient `m(x)|r̂|₁²`. Block 51's collisional corrections belong to the regime where (d) says the shadow has healed.
- **Block 52.** Streaming becomes a bias on a symmetric walk, and paths are no longer directed. `h` is then replaced by the biased walk's Green function, and the `1/κ` density law fails: slowing reduces the drift but not the symmetric hops. Not computed.

## 3. Relation to a2, and where the route stops

**a2 and this attempt.** a2 assembled the pair force by rescaling block 48's factor and did not solve the transport. Here the transport of both sites is solved exactly, including records slowed by both, and the `⟨m²⟩` weight, the direction of the push and action equals reaction all come out of that computation. I agree with a2 on:
- (a);
- (b);
- `κ` cancelling in the displacement (S6).

In addition I give:
- the exact per-step run-down law;
- the impulse `∝ (1 − κ)/n_b`;
- an explicit inequality on the pull;
- the exact unscattered fraction for (d).

**Where it stops.**
- Screening beyond the healing length is argued, not proved.
- The momentum-class pair re-draw is not solved.
- Block 52's biased walk is not computed.
- The body's law of motion, which (c)'s displacement remark needs, is borrowed from block 48's clause (momentum accumulates, velocity `P/(√3M)`).

## 4. What would finish it

1. Solve (d) with block 51's pair re-draw at small density, to first order in `γ`, and show that the far field has no monopole.
2. Compute block 52's version: the Green function of the biased walk with a slowing site that multiplies the bias.
3. Integrate the two-body trajectory in a running-down gas, which turns S6's scaling into a bound.
