# Emergent Lorentz is Radiatively Stable on the Discrete-Record-Tick (Z⁴ Hypercubic) Surface: B₄ Forbids the Marginal Velocity Anisotropy to All Orders — Bounded Theorem

**Date:** 2026-06-08
**Claim type:** bounded_theorem (positive; single named premise = the discrete-tick admission)
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

Because the framework's **temporal structure is not in its axioms** —
`{Lattice (spatial Z³), Quantum, Record}` carries no time (Record is a *timeless*
noun; the Lattice axiom "does not supply a dynamics … causal cone"; time is an
**admitted dynamics gate**, the framework's own
[`DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md`](DIRAC_LORENTZ_DIAGNOSTIC_BOUNDARIES_FROM_REJECTED_REPAIRS_NOTE_2026-06-07.md))
— the velocity anisotropy `δv` is **unavoidably conditional on a temporal
admission**. It is `0` on the discrete-record-tick admission and the computed
obstruction on the continuous-time admission. This note proves the **positive**
side as a bounded theorem.

**Premise (the single bound).** Physical time at the UV scale is the **discrete
record-tick**, so spacetime is the **Z⁴ hypercubic causal graph** — the spatial `Z³`
lattice times a temporal `Z_τ` with matched **nearest-neighbor / no-diagonal**
adjacency (the LATTICE-axiom no-diagonal clause + the retained finite-graph
reachability
[`LATTICE_NN_LIGHT_CONE_NOTE.md`](LATTICE_NN_LIGHT_CONE_NOTE.md), read as the
symmetric-staggered `ξ = 1` surface). This premise is a **dynamics-gate admission —
the owner's foundational choice**, equal in status to the complementary
continuous-time admission; it is **not derived** and the result is **not "no
bound."**

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

**Positive, bounded on the discrete-tick admission.** On the discrete-record-tick
(Z⁴ hypercubic) surface, B₄ forbids the marginal velocity anisotropy to all orders
and rep-blindly, so emergent Lorentz is **radiatively stable** — there is **no
naturalness problem** on this surface, and the only Lorentz violation is the
Planck-suppressed dim-6 operator (`~2×10⁻³⁹` at 1 GeV). The naturalness lever is
therefore not a no-go to overturn but a **single foundational admission**: adopting
the discrete record-tick as physical UV time yields this positive theorem;
the complementary continuous-time admission yields the companion computed obstruction.

## What this note does NOT claim

- It does **not** claim emergent Lorentz is protected **unconditionally / "no
  bound."** The result rests on the **discrete-tick admission**, a dynamics gate equal
  in status to the continuous-time admission; the temporal structure is **not** in the
  axioms, so `δv` cannot be unconditional.
- It does **not** claim the discrete-tick premise is **derived** or **retained**; it
  is the owner's foundational choice, and the audit lane is the only status authority.
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
