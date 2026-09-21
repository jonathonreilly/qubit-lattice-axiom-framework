---
claim_id: admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_matched_pulls_and_a_kept_ledger_fix_the_clock_laws_second_order_bounded_theorem_note_2026-09-21
claim_type: bounded_theorem
claim_scope: "WITHIN supplied clauses, not adopted: block 53's local tick rates w_x = phi_x^2 = exp(u_x) (open PR #8568), block 54's amplitudes timed by them, with the hermitian generator H_w = phi H phi for any hermitian H (open PR #8570), AND THE PREMISE OF THIS NOTE: the rate field obeys a static law and the pair (field, amplitudes) keeps a ledger <H_w> + F[u] that does not change in time; several amplitudes enter through their densities (a product amplitude). None of this is in the axioms memo, which contains no amplitude dynamics, no time metric and no conserved energy. (T1) At fixed amplitude d<H_w>/du_x = e_x := Re chi_x^dagger (H_w chi)_x, and sum_x e_x = <H_w> (the amplitude's energy has weight one in the rates); along any motion d<H_w>/dt = sum_x e_x du_x/dt. (T2) (a) If the field's law is dF/du_x = -(e_x - mu), mu a constant and sum_x u_x fixed, the ledger is kept: the source is the amplitudes' ENERGY density with its mean removed. (b) If the law has another source s in place of e, the ledger changes at the rate sum_x (e_x - s_x) du_x/dt. (c) For a body at rest on block 54's reduced walk e_x = m w_x |chi_x|^2 exactly: the weak-field packet's density |psi|^2 is the energy density of a body at rest per unit rest energy and local rate; for a moving body e is the energy (5/4 per unit probability at wave vector pi/2 and rest energy 3/4), not the rest energy. (T3) For point bodies pulled at -E grad u (block 54) in one another's weak fields -gamma S G_0, G_0 the zero-mean potential of block 53's operator on a torus, pull on A plus pull on B = gamma (E_A S_B - E_B S_A) times the potential's difference across A; the pulls of a pair are equal and opposite at every separation iff S_A/E_A = S_B/E_B, and the pulls of any set of bodies sum to zero when S is proportional to E; with every body sourcing alike they do not. (T4) With no master clock the ledger has weight one under w -> t w. A nearest-neighbour bond energy of weight one is sum over bonds of sqrt(w_x w_y) f(u_x - u_y) with f even; f(0) = 0 lets uniform rates solve the empty-space law, and a site term c w_x is excluded by block 53's clause that a rate is determined by its neighbours' rates. Then sum_x d(ledger)/du_x = ledger, so with positive energies the ledger cannot be stationary in every u_x: the unit of rate is not a variable, mu is the ledger per site, and the source enters with its mean removed (the weak-field packet's projection). At weak field the law is block 53's operator: (u_x - average over the six neighbours) = -(gamma/6)(e_x - mu)/wbar for F = (2/gamma) sum over bonds (phi_x - phi_y)^2: the coupling gamma is a pure number and the source is the energy density counted in ambient ticks. The second order, which block 53 left free, is fixed: for every f the empty-space law agrees through second order in u with the averaging law for phi = sqrt(w) (block 53's power mean of order 1/2; u_x = delta^2/12 in the bump test), and f enters at the fourth order ((4 f_4 - f_2)/(576 f_2) delta^4). For the simplest f the law is phi_x = average of phi over the neighbours exactly. EXECUTED, NOT CLAIMED: two walkers on a ring sourcing the field that times them: with the energy density as the source the ledger changes by 1e-11 to 1e-9 and the two wave vectors' changes cancel to 3 parts in 10^5; with the probability density as the source the wave vectors' changes fail to cancel by one half (at rest) and the ledger moves by the amount T2(b) predicts, to three digits in four cases. COROLLARY (conditional on blocks 53 and 54 and on records being pulled as amplitudes are): block 53's one number is log kappa = -(gamma/6) x (the record's energy in ambient ticks), and a body of energy E draws every long-wavelength packet at gamma E wbar/(4 pi r^2). NOT claimed: that the pair keeps a ledger at all; that an amplitude which has formed no record sources anything (a question for the record reading, not settled here); the static form of the law or any delay; the number gamma; the function f beyond second order; lengths; any statistical statement; any gravitational statement; any adoption."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_2026_09_21.py
---

# Action and reaction: the rate field's source is the amplitudes' energy density; matched pulls and a kept ledger fix the second order of the clock law

**Date:** 2026-09-21
**Type:** bounded_theorem
**Status:** bounded-support (exact statements within supplied clauses and one supplied premise — that the pair of rate field and amplitudes keeps a ledger; nothing adopted or registered; unaudited)

This note works within supplied clauses for local tick rates and for amplitudes timed by them; it reports what the rate field's source must be if the pair keeps a ledger and every pull is matched; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 53 (open PR #8568): with no master clock, a local tick rate obeys the lattice averaging equation, and records enter as additive sources with one free number `κ`. Block 54 (open PR #8570): an amplitude whose phase is timed by the local clock is pulled towards slow clocks with a force equal to its energy times the gradient, exactly. The weak-field packet on `main` supplies a third thing: the *source*, read off the amplitude as `ρ = |ψ|²`. This note asks what the source has to be.

**The premise (supplied).** The rate field obeys a static law, and the books balance: the amplitudes' energy plus an energy of the field does not change in time.

1. **The ledger identity.** Change the rate at one site and the amplitude's energy changes by the energy it has at that site: `d⟨H_w⟩/du_x = e_x`, and the `e_x` add up to the whole energy (T1).
2. **What the source must be.** The books balance when the field's law is `dF/du_x = −(e_x − μ)`: the source is the **energy density**, with its mean removed. With any other source `s` the ledger moves at the rate `Σ_x (e_x − s_x) du_x/dt` (T2). For a body at rest the energy density is `m w |χ|²`: the packet's `|ψ|²` times the rest energy and the local rate. For a moving body it is the energy, not the rest energy.
3. **Every pull matched.** Block 54 made the pull on a body proportional to its energy. Two bodies then pull each other equally and oppositely at every separation iff each sources in proportion to its energy, one constant for all. If every body sourced alike — a count — a heavy and a light body left alone would push themselves along (T3).
4. **No master clock, again.** The ledger must keep its form when the unit of rate is changed, so the field's own energy has weight one: bond energies `√(w_x w_y) f(u_x − u_y)`. Two consequences. The unit of rate cannot be one of the variables — if it were, the total would have to vanish — so the source enters with its mean removed: the packet's projection, from the ledger this time. And the second order of the clock law, which block 53 left free, is fixed: through second order every such law is the *averaging law for `√w`*. The function `f` enters only at the fourth order; the coupling `γ` is a pure number (T4).
5. **Executed.** Two walkers on a ring sourcing the field that times them. With the energy density as the source the ledger holds to `10⁻¹¹` and the two wave vectors' changes cancel to 3 parts in 10⁵. With the probability density as the source the changes fail to cancel by one half, and the ledger moves by exactly the amount item 2 predicts.

**Where the three blocks leave the packet.** Its operator and projection (block 53), its test response (block 54) and its source (this note, for bodies at rest) follow from three supplied clauses: no master clock; phases timed by local clocks; the books balance. One pure number, `γ`, is left, and block 53's `κ` becomes `log κ = −(γ/6) ×` (the record's energy in ambient ticks) if records are pulled as amplitudes are. What the note does not settle is whether an amplitude that has formed no record sources anything at all; that is a question for the record reading.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 54 (PR #8570), next_trace_action: 'the amplitude as a source: whether action and reaction (a conserved energy for the pair of rate field and amplitude) forces the amplitude's energy density, not its probability density, to source the rate field'; weak-field packet on main: the source rho = |psi|^2 is supplied"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "whether an unrecorded amplitude can be a source under the record reading, or only records with log kappa = -(gamma/6) E; a delay of the field (the static law acts at a distance); the ray limit of the clocked walk as a theorem; the number gamma; a clause for lengths"
conditional_surface_status: "T1 exact for every amplitude, hermitian generator and positive rate field; T2 exact given a static law and a ledger of the stated form; T3 exact for point bodies in the weak field of block 53's operator on a torus, with block 54's force law; T4 exact for nearest-neighbour bond energies of weight one; the coupled motion is executed only"
hypothetical_axiom_status: "blocks 53 and 54's clauses; a static field law; a kept ledger of the form <H_w> + F[u]; amplitudes entering through their densities; hypotheses only"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Premises and declared objects

The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`, read in full on 2026-09-21 together with `docs/repo/DEFERRED_DECISIONS.md`) contains no amplitude dynamics, no time metric and no conserved energy; it is used through the Lattice axiom and through those absences. Blocks 53 and 54 (open PRs #8568, #8570) supply the rate field and the clocked amplitude; both are supplied clauses.

- **Rates.** `w_x = φ_x² = exp(u_x) > 0`.
- **Amplitudes.** `χ` with the plain norm, `i dχ/dt = H_w χ`, `H_w = φHφ` (every bond carries `φ_x φ_y`), `H` any hermitian generator; for several walkers a product amplitude, each factor timed by the same field.
- **Energy density.** `e_x = Re χ_x†(H_w χ)_x`, summed over the two components and over the walkers.
- **Field law.** Static: `u` is determined at each time by the amplitudes. **Ledger.** `⟨H_w⟩ + F[u]`, `F` a differentiable function of the rates.
- **Point bodies** (T3). A body at `x_A` with energy `E_A` and source strength `S_A`; its weak field is `−γ S_A G_0(· − x_A)`, `G_0` the zero-mean solution of `u_x −` (average of the six neighbours) `= δ_x −` mean on a torus; the pull on it is `−E_A` times the central difference of the others' fields (block 54's force law).
- **Bump test** (T4). Two opposite neighbours at `u = ±δ`, the other four at `0`; the law's answer for `u_x`.

That the derivative of an energy with respect to a parameter is the expectation of the derivative is the theorem of Hellmann and Feynman; a field determined at each time by the densities of the amplitudes it acts on is a mean field in the sense of Hartree. The equality of action and reaction is Newton's third law, and that a source proportional to something other than the pulled quantity breaks it is the classical argument for the equality of active and passive mass. The degree-one identity is Euler's. In the continuum the content of T4 is Einstein's second static theory of 1912: requiring action and reaction to balance, he replaced `Δc = kcσ` by `cΔc − ½(∇c)² = kc²σ`, which is `Δ√c = (k/2)√c σ` — the square root of the local speed obeys the linear equation, and the field's own energy is among its sources. None is used as authority.

## Prior art and what is new

Every ingredient is classical, and the continuum form of the main result is Einstein's of 1912, reached by the same argument. What is new is its place in the framework's vocabulary and on the lattice: (i) the weak-field packet's supplied source `ρ = |ψ|²` is identified as the rest-body form of a quantity — the energy density `e_x`, the derivative of the clocked energy with respect to the local rate — that is fixed once block 54's clause is granted and the books are required to balance; (ii) the same requirement, combined with block 53's premise that only ratios of rates mean anything, removes a freedom block 53 recorded (the second order of the clock law) and gives the packet's zero-mode projection a second derivation; (iii) the statements are exact lattice identities with an exact rate for the failure of any other source, and the coupled motion is executed. It is a conditional derivation of a supplied piece, not a gravitational claim.

## Exact target and obligation graph

Target: what the rate field's source must be. Obligations: (O1) how the amplitudes' energy depends on the rates; (O2) the law that keeps the ledger, and what any other law does to it; (O3) matched pulls; (O4) what block 53's premise does to the ledger; (O5) an executed check of the coupled motion. T1–T4 discharge O1–O4; O5 is executed and not claimed.

## Theorem T1 — the ledger identity

*Statement.* For every amplitude, hermitian `H` and positive rate field, `∂⟨χ|H_w|χ⟩/∂u_x = e_x` at fixed `χ`, and `Σ_x e_x = ⟨H_w⟩`. If `u` changes in time and `i dχ/dt = H_w χ`, then `d⟨H_w⟩/dt = Σ_x e_x du_x/dt`.

*Proof.* `⟨H_w⟩ = Σ_{x,y} φ_x φ_y χ_x†H_{xy}χ_y` is a quadratic form in `φ`, and `∂/∂u_x = (φ_x/2)∂/∂φ_x`: `∂⟨H_w⟩/∂u_x = ½[χ_x†(H_wχ)_x + (H_wχ)_x†χ_x] = e_x`. Summing over `x` counts every term of the quadratic form twice with the factor one half. The amplitude's own motion contributes `i⟨[H_w, H_w]⟩ = 0`. ∎

## Theorem T2 — the law that keeps the ledger

*Statement.* Let `Σ_x u_x` be held fixed (the unit of rate; see T4). (a) If at every time `∂F/∂u_x = −(e_x − μ)` for all `x`, with `μ` independent of `x`, then `⟨H_w⟩ + F` is constant. (b) If instead `∂F/∂u_x = −(s_x − μ)` for some other source `s`, then `d(⟨H_w⟩ + F)/dt = Σ_x (e_x − s_x) du_x/dt`. (c) On block 54's reduced walk `H = mσ_1 + σ_3 D`, an amplitude with a real envelope and the rest-energy content has `e_x = m w_x |χ_x|²` at every site; a plane wave of wave vector `π/2` with `m = 3/4` has `e_x = (5/4)|χ_x|²`.

*Proof.* `d(⟨H_w⟩ + F)/dt = Σ_x (e_x + ∂F/∂u_x) du_x/dt` by T1, and `Σ_x du_x/dt = 0` removes `μ`. (c) For the content `(1, 1)` one has `(1,1)σ_3(1,1)ᵀ = 0`, so with a real envelope the hopping terms contribute nothing to the real part and the rest term gives `m φ_x² |χ_x|²`; for the plane wave `H_wχ = (5/4)χ`. ∎

The source is the derivative of the clocked energy with respect to the local rate. It is not a separate choice: once block 54's clause says how a rate field acts on an amplitude, the requirement that the books balance says how the amplitude acts on the rate field. For a slow body `e = m w |χ|²`, and the packet's source is recovered with the rest energy as its constant; a moving body sources its energy, and a walker with no rest energy at all still sources.

## Theorem T3 — every pull matched

*Statement.* For two point bodies, (pull on `A` from `B`'s field) + (pull on `B` from `A`'s field) `= γ (E_A S_B − E_B S_A) ∇_c G_0(x_A − x_B)`, `∇_c` the central difference. The two pulls are equal and opposite at every separation iff `S_A/E_A = S_B/E_B`. For any set of bodies with `S = cE` the pulls sum to zero; with every `S` equal they do not in general.

*Proof.* The pull on `A` is `−E_A ∇_c(−γ S_B G_0)(x_A − x_B) = γ E_A S_B ∇_c G_0(x_A − x_B)`, and the pull on `B` is `γ E_B S_A ∇_c G_0(x_B − x_A)`. `G_0` is even because the operator commutes with inversion, so its central difference is odd. `∇_c G_0` does not vanish identically, which gives the iff for a pair; for a set with `S = cE` the pair terms cancel two by two. ∎

Executed exactly on the `4×4×4` torus with energies `2, 5, 3/2`: total pull zero for `S ∝ E`, and non-zero for a count. Matched pulls presume that nothing else carries momentum; a fixed arrangement of sources may of course pull a test body without being pulled back.

## Theorem T4 — no master clock: the ledger has weight one

*Statement.* Let the ledger keep its form under `w → tw` for every `t > 0` (block 53's premise; `⟨H_w⟩` has weight one by T1). (a) A nearest-neighbour bond energy of weight one is `Σ_bonds √(w_x w_y) f(u_x − u_y)` with `f` even. Uniform rates solve the empty-space law iff `f(0) = 0`. A site term `c w_x`, also of weight one, makes the empty-space law at a site involve the multiplier `μ`, a global quantity, and is excluded by block 53's clause that a rate is determined by its neighbours' rates. (b) `Σ_x ∂(⟨H_w⟩ + F)/∂u_x = ⟨H_w⟩ + F`. With `⟨H_w⟩ > 0` and `F ≥ 0` the ledger is therefore not stationary in every `u_x`: the unit of rate is not a variable; stationarity under variations with `Σ_x δu_x = 0` gives the law of T2 with `μ = (⟨H_w⟩ + F)/N`, so that the source enters as `e_x − μ`. (c) For `F = (2/γ) Σ_bonds (φ_x − φ_y)²` the weak-field law is `u_x −` (average of `u` over the six neighbours) `= −(γ/6)(e_x − μ)/w̄`, `w̄` the ambient rate: block 53's operator, a coupling that is a pure number, and a source counted in ambient ticks. (d) For every even `f` with `f(0) = 0 < f''(0)` the empty-space law gives, in the bump test, `u_x = δ²/12 + ((4f_4 − f_2)/(576 f_2)) δ⁴ + …` (`f_2 = f''(0)`, `f_4 = f''''(0)`): the second order is that of the averaging law for `φ = √w`, block 53's power mean of order `1/2`, whatever `f`. For `F` of (c) the empty-space law is `φ_x =` average of `φ` exactly.

*Proof.* (a) A symmetric function of `(w_x, w_y)` homogeneous of degree one is `√(w_x w_y)` times an even function of `log(w_x/w_y)`. At uniform rates `∂F/∂u_x = 3w f(0)`. (b) The degree-one identity for weight one (both terms are homogeneous of degree two in `φ`), applied to both terms. If every `∂/∂u_x` of the ledger vanished, the ledger would vanish; it is positive. (c) `∂F/∂u_x = (2/γ) φ_x Σ_y (φ_x − φ_y)`, and `φ = √w̄ (1 + (u − ū)/2 + …)`. (d) `∂/∂u_x [√(w_x w_y) f(d)] = √(w_x w_y) [f(d)/2 + f'(d)]` with `d = u_x − u_y`; dividing the law by `√w_x` and expanding, `Σ_y e^{−d_y/2}[f_2 d_y + (f_2/4) d_y² + O(d³)] = f_2 Σ_y [d_y − d_y²/4] + O(d³) = 0`, in which `f_2` cancels and `f_4` has not yet appeared; in the bump test `Σ_y d_y = 6u_x` and `Σ_y d_y² = 2δ² + O(δ⁴)`. The power mean of order `p` gives `pδ²/6`. For (c)'s `F`, `φ_x Σ_y (φ_x − φ_y) = 0`. ∎

The argument of (b) can be run the other way. If the unit of rate *were* varied the ledger would have to vanish, the field's energy would have to be negative to cancel the amplitudes', and then like energies would raise the rates around them and repel. Pulls towards energy, a positive field energy and a unit of rate that is not a variable go together.

## Corollary (conditional on blocks 53 and 54 and on records being pulled as amplitudes are)

Block 53 lets a record enter as `u_x −` average `= log κ`. If a record is pulled by the field as block 54's amplitudes are, in proportion to its energy `E`, then T3 requires it to source in the same proportion, and by T4(c) `log κ = −(γ/6) E/w̄`: block 53's free number is the record's energy in ambient ticks times the universal `γ/6`, and `κ < 1`. Far from a body of energy `E`, `u ≈ −γ(E/w̄)/(4πr)`, and by block 54 every long-wavelength packet falls towards it at `γ E w̄/(4πr²)`.

## Executed (supervisor control; floating point; evidence, not proof)

`specs/supervisor_control_block55_two_walkers.py` — two walkers on a ring of 1500 sites (block 54's reduced walk; widths 30; positions 500 and 1000), the weak-field law `2u_z − u_{z+1} − u_{z−1} = −Γ(s_z −` mean`)`, `Γ = 0.002`, `T = 300`; three sources: the energy density; the probability density (every walker sources alike); the rest form `w(m_A|χ^A|² + m_B|χ^B|²)`. Wave vectors are read from `⟨T⟩`; by block 54 each changes at `−E du/dz`, so the two changes cancel iff the pulls are matched.

| source | change of wave vectors `A`, `B` | their sum, as a fraction of the larger | ledger moved by | T2(b) predicts |
|---|---|---|---|---|
| *both at rest, rest energies 0.3 and 0.6* | | | | |
| energy | `+0.016307`, `−0.016307` | `1.6×10⁻⁵` | `−1.0×10⁻¹¹` | `0` |
| probability | `+0.013009`, `−0.025988` | `0.50` | `+1.37×10⁻⁵` | `+1.37×10⁻⁵` |
| rest form | `+0.016290`, `−0.016306` | `9.8×10⁻⁴` | `−2.94×10⁻⁶` | `−2.94×10⁻⁶` |
| *`A` moving at wave vector 0.4 (rest energy 0.3), `B` at rest (0.6)* | | | | |
| energy | `+0.035570`, `−0.035571` | `2.6×10⁻⁵` | `−1.4×10⁻⁹` | `0` |
| probability | `+0.030389`, `−0.035474` | `0.14` | `−3.94×10⁻³` | `−3.94×10⁻³` |
| rest form | `+0.037362`, `−0.022093` | `0.41` | `+4.57×10⁻⁴` | `+4.57×10⁻⁴` |

With the probability density as the source the heavier body is pulled twice as hard as the lighter and pulls no harder. The rest form is the energy density of bodies at rest and works for them; once a body moves it misses the energy of motion and fails by two fifths. The fields reach `u ≈ −0.13`, so these runs are not deep in the weak-field regime; the ledger's behaviour does not depend on that.

## Correspondence with the weak-field packet (of form; no gravitational claim)

| supplied in the packet on `main` | within the three supplied clauses |
|---|---|
| operator `−Δ_lat`, from a posited quadratic action | block 53: forced by nearest-neighbour determination, covariance and scale covariance; here again as the weak-field form of any weight-one ledger (T4c) |
| zero mode projected out, `P_0 ρ` | block 53: the unit of rate is unobservable; here: the unit of rate is not a variable of the ledger (T4b) |
| source `ρ = |ψ|²` | the energy density `e_x`; for a body at rest `m w |χ|²` (T2c); for a moving body its energy |
| test response `S = L(1 − φ)`, `F = +m∇φ` | block 54: `φ = −u`, `m` the body's energy |
| coupling and units | one pure number `γ`; block 53's `κ = exp(−(γ/6)E/w̄)` |

## No-Go Discipline Gate

The note's negative sentences: a source other than the energy density does not keep the ledger and does not match the pulls; the unit of rate cannot be a variable of the ledger; a site term is excluded; the second order of the clock law is not free.

### N1 — Routes by which the sentences could fail
1. *No ledger.* If the pair keeps no ledger, nothing here constrains the source. The axioms do not contain one; it is this note's premise.
2. *A ledger of another form.* An energy that is not the sum of `⟨H_w⟩` and a function of the rates — for instance one in which the field's energy depends on the amplitude as well — is a different coupling and is not covered.
3. *A field with its own motion.* With a delay the ledger gains a term for the field's motion; T1 is unchanged, so the static part of the law keeps the energy density as its source. Not worked.
4. *Sources that are records.* If only records source (block 53) and they form by a rule this note does not have, there is no ledger of this kind; T3 then applies to records as bodies and gives the Corollary. Whether an amplitude that has formed no record sources anything is not settled here.
5. *Bodies that are not points, strong fields.* T3 uses point bodies, weak fields and block 54's force law, exact for uniform gradients and executed otherwise.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
The coupling is a mean field: amplitudes enter through densities, and several walkers through a product amplitude. The law is static. `F` is a function of the rates alone, of nearest-neighbour bonds in T4. T4(b) uses `F ≥ 0` and `⟨H_w⟩ > 0`. The rest-body statement T2(c) is made on block 54's reduced walk, where motion across the line plays the part of a rest energy; one walker has none (block 54).

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | the lattice; the absence of amplitude dynamics, of a time metric and of a conserved energy | yes (premise; the absences motivate the clauses and do not prove them) |
| block 53 (open PR #8568) | the rate field, its operator, scale covariance, the record clause with `κ` | yes (restated; T4 and the Corollary are conditional on it) |
| block 54 (open PR #8570) | the clocked generator `φHφ`; the force law; the reduced walk | yes (restated; T1–T3 are conditional on it) |
| weak-field packet (`main`) | the supplied source the correspondence is drawn with | target, not premise |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "`e_x = d⟨H_w⟩/du_x`, summing to `⟨H_w⟩`; the ledger's rate with any source; matched pulls iff `S ∝ E`; weight one, the unit of rate not a variable, second order fixed" | executed: the energy density at 27 sites and its derivative at nine | executed: a body at rest at every site of a ring with a rational rate field; a moving body on a ring of four | executed: the bump test for two weight-one energies as exact power series through the fourth order | executed: three bodies on the `4×4×4` torus with exact potentials; the pair identity for three choices of strengths | T1 for every amplitude, generator and rate field; T2 for every static law and ledger of the stated form; T3 for point bodies in weak fields on any torus; T4 for every nearest-neighbour bond energy of weight one; the ledger itself, the static law, `γ` and `f` not derived |

### N6 — Partial-closure paths and primitive scan
The registered primitives do not supply a ledger or a source: `scale_reference_primitive` converts units and fixes no pure number; `kinetic_isotropy_primitive` grants `c_t = c_s` of a kinetic form; `realized_state_primitive` grants evaluation at a supplied state and no density. Nothing is proposed for registration.

### N7 — Steelman
Hostile reviewer: "A conserved energy is an import; the axioms have none." Reply: yes, and it is declared as this note's premise. What the note shows is that once it is granted the source is no longer a separate choice, that the packet's `|ψ|²` is its rest-body form, and that block 53's premise then removes a freedom block 53 had recorded. Second objection: "A field sourced by an amplitude that has formed no record contradicts 'only records are readable'." Reply: the note does not settle that and says so; T3 and the Corollary are the form the result takes if only records source. Third objection: "This is a known static theory." Reply: in the continuum, yes, and it is named; the lattice statements, the exact failure rate of other sources, and the link to block 53's free second order are what is added.

### N8 — Cross-cycle echo
Block 41 made the record count the only local additive invariant density of the record layer; blocks 45 to 49 found that a capture picture's pull is tied to growth and its push to gross capture, so that action and reaction there are not symmetric in the bodies' masses. Block 53 left `κ` and the second order free; block 54 made the pull proportional to energy. Here the two free items of block 53 are tied to one pure number and one function at fourth order, and the symmetry between pulling and being pulled is what does it.

## Falsifiers

- An amplitude, generator and rate field with `∂⟨H_w⟩/∂u_x ≠ Re χ_x†(H_wχ)_x`, or with densities that do not sum to `⟨H_w⟩`.
- A static law with a source other than the energy density under which `⟨H_w⟩ + F` is kept for all motions; a motion under a source `s` whose ledger does not move at the rate `Σ(e − s)du/dt`.
- Two point bodies with `S_A/E_A ≠ S_B/E_B` whose pulls cancel at every separation.
- A nearest-neighbour bond energy of weight one, even with `f(0) = 0 < f''(0)`, whose bump test does not give `δ²/12` at second order.

## Boundaries and non-claims

That the pair keeps a ledger is a premise; the axioms contain no conserved energy. The coupling is a mean field and the law is static: nothing is said about how the field follows a change of its sources. Whether an amplitude that has formed no record sources anything is not settled; a rule for where records form would be needed to relate a source carried by records to one carried by the amplitude, and none is used. `γ` is not derived, and neither is `f` beyond the second order. T3 is a statement about point bodies in weak fields. One walker has no rest energy; T2(c)'s body at rest lives on the reduced walk. Lengths are not addressed. The correspondence with the weak-field packet is one of form. No gravitational statement is made and nothing is adopted.

## Imports
- `minimal_axioms`: the Lattice axiom and the memo's silence on amplitude dynamics, the time metric and a conserved energy. Blocks 53 and 54 (PRs #8568, #8570, open): restated. The weak-field packet on `main`: the target of the correspondence.
- Named standard imports at definition level: differentiation of a quadratic form; the degree-one identity for homogeneous functions; evenness of the potential of an operator that commutes with inversion; power series.
- Reference only: Hellmann and Feynman; Hartree; Newton; Euler; Einstein (1912).

## Review record
Supervisor-run block, the third of the source-link direction, on the owner's instruction "ok lets work the source link into the amplitude layer". Lens pass, in writing, by the supervisor (the campaign's no-subagent rule). A foundations lens: a conserved energy is not in the axioms and is declared as the premise; a source carried by an unrecorded amplitude is in tension with "only records are readable" — the note does not settle it and gives the form the result takes if only records source; no statistical statement is used or compared. A rigour lens: T2 is stated as a sufficient law plus an exact rate for any other source, in place of an "iff" over all motions that would need the reachable directions of `du/dt` to span; the "iff" of T3 is for a pair and rests on the potential's central difference not vanishing identically; a site term of weight one is scale covariant, so it is excluded by block 53's locality clause and not by scale covariance, and the note says which. A comparator lens: the continuum form is a known static theory of 1912, reached by the same argument; named under the Premises and Prior art. A strategy lens: the packet's three supplied pieces now follow from three supplied clauses with one pure number left. Refuting pass (`specs/supervisor_control_block55_refuter.py`, machinery disjoint from the runner's): W1 the ledger identity with symbolic rates and amplitude; W2 the bump test for a general weight-one bond energy, symbolically (`δ²/12`, and `(4f_4 − f_2)/(576f_2)` at fourth order; equal to the power mean iff `p = 1/2`); W3 ten bodies on a `16³` torus (`2×10⁻¹⁶` against `4×10⁻²`); W4 the weight-one identity by finite differences, and its failure for a field energy quadratic in `u`; W5 two walkers with dense exponentials (ledger `−4×10⁻¹²`; `−2.388×10⁻⁴` against the predicted `−2.388×10⁻⁴`). All pass. Findings folded from the control: the first "rest" source left out the local rate and missed the balance by 8 per cent in a run whose own field reaches `u ≈ −0.1` — the runner's E1 has the factor `w`, and the control now does; the first prediction of the ledger's rate averaged amplitudes at the midpoint of a step and was off by a factor of two in the case where the ledger moves least — replaced by the trapezoid rule on the integrand; momentum balance was first read from displacements, which differ by the factor `w²` at the two bodies, and is now read from the wave vectors. Mutation census: 10 mutations, each failing in its own family only. Author checks only; no independent review has taken place.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_action_and_reaction_the_rate_fields_source_is_the_amplitudes_energy_density_2026_09_21.py
```

Expected: `TOTAL: PASS=18 FAIL=0`.
