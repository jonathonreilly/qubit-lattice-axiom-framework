# Emergent Lorentz is Radiatively Stable on the Discrete-Record-Tick (Z⁴ Hypercubic) Surface: B₄ Forbids the Marginal Velocity Anisotropy to All Orders — Bounded Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem (positive; single named premise = a non-retained finite-`a_τ` symmetric-tick realization premise of the `ξ=1` surface)
**Type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not set
or predict an audit outcome. The `bounded_theorem` label is a source-side
claim-boundary declaration, not an audit verdict.
**Primary runner:**
[`scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py`](../scripts/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.py)
**Cached runner output:**
[`logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt`](../logs/runner-cache/frontier_emergent_lorentz_radiative_stability_discrete_tick_2026_06_08.txt)

---

## Role

This note states **affirmatively** the positive horn of the emergent-Lorentz
velocity-RG analysis. Its companion no-go,
[`LORENTZ_VELOCITY_RG_COEFFICIENT_COMPUTED_NOTE_2026-06-08.md`](LORENTZ_VELOCITY_RG_COEFFICIENT_COMPUTED_NOTE_2026-06-08.md),
computed the one-loop velocity anisotropy as **one coefficient `δv(ξ)`** of the
spacetime anisotropy `ξ = a_s/a_τ`: the radiative Lorentz-violation **obstruction**
lives at the continuous-time horn `ξ → ∞`, and `δv = 0` by the **B₄ hypercubic**
symmetry at `ξ = 1`.

The framework **does** derive temporal structure — the **single-clock codimension-1
evolution theorem**
([`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md),
live-ledger **unaudited**, on retained RP-temporal-bridge / spectrum / cluster / Cl(3)
/ arrow inputs) derives a **unique single-clock unitary evolution**. But its **physical
output is continuous Stone time** `U(t) = exp(−itH)` on the spatial `Z³` slice (Step 1:
the analytic continuation of the transfer `T^n`), which is the **continuous-time
(`ξ → ∞`) obstruction surface**; and the **retained no-go**
[`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
shows `T` fixes only the product `a_τ·H`, not `a_τ`. So the velocity anisotropy `δv` is
the **same coefficient `δv(ξ)`** read at two surfaces: the **derived** continuous-time
surface (`ξ → ∞`, the computed obstruction) and the **`ξ = 1`** surface this note treats.

**Premise (the single bound — a realization premise, not delivered by the derived-time
chain).** Physical time at the UV scale is the **discrete record-tick** with **finite
`a_τ`** and the **symmetric central-difference (staggered) tick**, so spacetime is the
**Z⁴ hypercubic causal graph** (spatial `Z³` × temporal `Z_τ`, matched no-diagonal
adjacency; the symmetric-staggered `ξ = 1` surface). This premise is **not** delivered
by the single-clock chain — which uses the **forward** transfer `T = e^{−Ha_τ}`
(B₄-breaking at `ξ = 1`) and leaves `a_τ` removable — and the only retained authority
for the isotropic SO(4)/B₄ form proves it **only at `a → 0`** (the `ξ → ∞` surface). So
it is a **separate realization premise, currently non-retained** (the finite-`a_τ`
symmetric tick, plus the `audited_renaming` record-tick = physical-time identification),
**not** "no bound." The companion boundary note
[`TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md`](TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md)
maps this in full. This note proves the **positive** side (the B₄ selection rule on the
`ξ = 1` surface) as a bounded theorem, conditional on that premise.

**Theorem (verified-grade, bridge-independent).** On that surface the marginal
dim-4 velocity-anisotropy operator (`c_t ≠ c_s`) is forbidden by B₄ **to all orders
and rep-blindly**, so **emergent Lorentz invariance is radiatively stable**: the only
Lorentz-violating residual is the **Planck-suppressed dimension-6** cubic operator,
`|δE²/E²| ≈ (1/3)(E/M_Pl)² ≈ 2×10⁻³⁹` at 1 GeV — far below every SME/UHECR/GRB/clock
comparator bound. Runner: **12 PASS / 0 FAIL**.

## The theorem

### (1) B₄ forbids the marginal dim-4 velocity anisotropy
The diagonal quadratic kinetic form `c_t p_t² + c_s |p_s|²` has, under spatial `O_h`
alone, a **2-dimensional** invariant space (`c_t` and `c_s` independently free — the
marginal anisotropy `c_t − c_s` is *allowed*); under the **4D hypercubic group B₄**
it has a **1-dimensional** invariant space (`c_t = c_s` *forced*) — the `t↔s` axis
swap relates the temporal and spatial coefficients (runner Part 1; consistent with
the retained
[`SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)).
So the marginal LV operator is **not in the B₄-invariant ring**.

### (2) All-orders, rep-blind selection rule ⇒ `δv = 0`
On the Z⁴ hypercubic action the `t↔s` axis swap is an exact B₄ symmetry — a **finite
relabeling** of a B₄-invariant measure, propagator, and vertices — so the temporal
and spatial self-energy coefficients are equal: `Σ_t = Σ_s` to **machine zero** at
every resolution (runner Part 2). This is a **selection rule, not a one-loop
cancellation**: the marginal dim-4 anisotropy is not B₄-invariant (1), so it is
forbidden at **every loop order**, and power counting forbids regenerating it from
the dim-6 residual. It is **rep-blind**: the loop factorizes as
`g² C₂(rep) × [spacetime integral]`, and the spacetime difference is the machine zero
above, so `δv(rep) = C₂(rep) × 0 = 0` for **every** gauge representation — hence the
**species-to-species difference** (the actual LV observable)
`(C₂ᵢ − C₂ⱼ) × 0 = 0` vanishes too.

### (3) The framework's actual fermion supplies the isotropy
Form-equality (the full isotropic Z⁴ action) is **not** a special tuning: **any**
hypercubic-symmetric action gives `δv = 0` (naive `r = 0`, Wilson `r_t = r_s`, both to
machine zero; only a deliberate `r_t ≠ r_s` breaks it, runner Part 3). The framework's
canonical free-staggered action — isotropic `η_μ`, the same `sin(p_μ)` in all four
directions, `c₄ = −1/3` in all four
([`LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md`](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md))
— **is** isotropic, so the theorem applies to the actual fermion (modulo the
symmetric-staggered, central-difference realization rider).

### (4) The residual Lorentz violation is harmless
With the marginal dim-4 operator forbidden (1), the leading surviving LV is the
B₄-allowed **dimension-6** operator: `E² = k² − (a²/3)Σ_i k_i⁴` (the retained
[`EMERGENT_LORENTZ_INVARIANCE_NOTE.md`](EMERGENT_LORENTZ_INVARIANCE_NOTE.md) result,
now over all four directions). With `a = 1/M_Pl`, `|δE²/E²| ≈ (1/3)(E/M_Pl)² ≈
2×10⁻³⁹` at 1 GeV — below every comparator bound (`10⁻¹²` quark/gluon … `10⁻²⁷`
nucleon) by `≫ 15` orders. This is the framework's **positive** Lorentz fingerprint:
emergent Lorentz holds to dim-6, and any LV detected at the `(E/M_Pl)²` level would
carry the unique cubic-harmonic `ℓ = 4` angular signature of the cubic lattice.

## Verdict

**Positive, bounded on a non-retained tick-realization premise.** On the discrete-
record-tick (Z⁴ hypercubic, finite-`a_τ`, symmetric-tick) surface, B₄ forbids the
marginal velocity anisotropy to all orders and rep-blindly, so emergent Lorentz is
**radiatively stable** — **no naturalness problem** on this surface, the only Lorentz
violation the Planck-suppressed dim-6 operator (`~2×10⁻³⁹` at 1 GeV). The naturalness
lever is therefore **one named realization premise** of the single `δv(ξ)` coefficient:
the framework **derives** time (single-clock theorem, unaudited) but as **continuous
Stone time** (the `ξ → ∞` obstruction surface); the `ξ = 1` surface this theorem treats
needs a **separate, non-retained** premise — a finite physical `a_τ` (over the
removable regulator) **plus** the symmetric central-difference tick (over the forward
transfer the chain uses; the SO(4) isotropy authority is `a → 0`-only) — which the
derived-time chain does **not** supply and partly contradicts. **Both horns of `δv(ξ)`
remain live.** The companion boundary note maps the open seams.

## What this note does NOT claim

- It does **not** claim emergent Lorentz is protected **unconditionally / "no
  bound."** The result rests on a **finite-`a_τ` symmetric-tick realization premise** of
  the `ξ = 1` surface, which the framework's derived-time chain does **not** supply
  (its physical output is continuous Stone time, the obstruction surface) and partly
  contradicts (the forward transfer; `a_τ` removable; SO(4) isotropy `a → 0`-only).
- It does **not** claim that premise is **derived** or **retained** — time *is* derived
  (single-clock theorem, unaudited), but as continuous Stone time, **not** as this
  finite-`a_τ` symmetric tick; the audit lane is the only status authority.
- It does **not** close the naturalness lever or contradict the companion obstruction
  note — it is the **positive horn** of the same one coefficient `δv(ξ)`; the
  obstruction is the continuous-time (`ξ → ∞`) horn.
- It does **not** depend on the absolute clock **rate** (the retained
  [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
  prunes only rate-**from-counts**; this theorem uses the dimensionless conformal
  class / B₄ graph symmetry, and the supplied scale primitive sets the absolute
  scale): the B₄ selection rule is a property of the lattice **geometry**, not the
  metric rate.
- It carries the **realization rider**: it holds for the canonical symmetric-staggered
  (central-difference) tick, not a generic forward/Wilson transfer step.
- **No** new axiom, primitive, repo vocabulary, or class tag; **no** PDG-fit /
  `g_bare` derivation input. Literature (Collins et al *PRL* 93 (2004) 191301;
  Kostelecký–Russell SME tables) is comparator only. It sets **no** audit status.

## Reprove-and-cite ledger

- **Reproven here** (runner, from lattice/group primitives): the `O_h` (2-dim) vs B₄
  (1-dim) invariant count of the diagonal kinetic form; the Z⁴ `Σ_t = Σ_s`
  machine-zero (all resolutions), its rep-blindness (species difference = 0), and the
  selection-rule (all-orders) structure; the isotropic-action universality (only a
  deliberate `r_t ≠ r_s` breaks it); the dim-6 dispersion `a²/3` and the
  `(E/M_Pl)² ≈ 2×10⁻³⁹` residual at 1 GeV.
- **Cited** (comparator/scope only, never a derivation input):
  Collins–Perez–Sudarsky–Urrutia–Vucetich *PRL* **93** (2004) 191301 (the marginal
  regeneration the B₄ surface forbids); Kostelecký–Russell SME data tables (LV
  comparator bounds).

## Audit dependency repair links

This section records explicit dependency links for the audit citation graph. It does
not promote this note or change any audited claim scope.

- [TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md](TEMPORAL_STRUCTURE_DERIVATION_BOUNDARY_BOUNDED_NOTE_2026-06-08.md)
- [AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
- [SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
- [LORENTZ_VELOCITY_RG_COEFFICIENT_COMPUTED_NOTE_2026-06-08.md](LORENTZ_VELOCITY_RG_COEFFICIENT_COMPUTED_NOTE_2026-06-08.md)
- [SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md](SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md)
- [EMERGENT_LORENTZ_INVARIANCE_NOTE.md](EMERGENT_LORENTZ_INVARIANCE_NOTE.md)
- [LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md](LORENTZ_BOOST_FREE_STAGGERED_FERMION_2POINT_SO4_NARROW_THEOREM_NOTE_2026-05-29.md)
- [LATTICE_NN_LIGHT_CONE_NOTE.md](LATTICE_NN_LIGHT_CONE_NOTE.md)
- [POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md)
- [DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md](DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md)
- [MINIMAL_AXIOMS_2026-06-05.md](MINIMAL_AXIOMS_2026-06-05.md)

### Source-note boundary

**Hypothesis set:** (1) the three axioms + the approved scale primitive `a⁻¹ = M_Pl`;
(2) **the single admitted premise** — physical UV time is the discrete record-tick, so
spacetime is the Z⁴ hypercubic causal graph (the `ξ = 1` surface); (3) the framework's
canonical isotropic staggered action; (4) standard one-loop / all-orders lattice
selection-rule reasoning (B₄ group theory + the verified Z⁴ self-energy control);
(5) SME/UHECR/GRB/clock bounds as comparators. The result is positive and **bounded on
premise (2)**; the realization rider (the canonical symmetric-staggered tick) is
named.

**Forbidden-imports check:** no new axiom, primitive, repo vocabulary, or class tag;
only standard terms (hypercubic group, invariant ring, selection rule, self-energy,
staggered fermion, dimension-6 operator). No fitted/PDG/lattice-MC value consumed as a
derivation input; the LV bounds are comparators.

**No-promotion statement:** this note does **not** promote, demote, or set the audit
status of the companion obstruction note, the emergent-Lorentz notes, the
free-staggered SO(4) note, the reachability/clock-rate notes, or any upstream row. The
independent audit lane is the only status authority.
