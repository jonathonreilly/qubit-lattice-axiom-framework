# The Absolute T-Odd Orientation Sign Is Convention: the Conjugation-Selector Class Is Empty (Carrier-Independent), and No Spectral / Symmetry-Equivariant Functional Is Orientation-Odd

**Date:** 2026-06-18
**Type:** narrow_no_go (selector-class emptiness + selector-completeness) + reduction map
**Claim type:** narrow_no_go
**Status authority:** independent audit lane only. This note sets/predicts no audit status,
**retires no Tier-A admission**, and edits no `docs/audit/data/*` file.

**Claim scope (narrow).** For the shared T-odd orientation `Z₂` — the realized sign of the
`Cl(3,1)` `e₄` volume form, equivalently `sign(Vandermonde Δ)` (Koide handedness), the
`θ` mass-side `arg det M ∈ {0,π}` orientation bit, and the EH/conformal-mode sign — three
results, all derived (runner 8/8), none asserted:

   **Imported premise (cited).** The two orientation branches are a **conjugate pair**: the
   opposite-orientation carrier is `σ H σ⁻¹` (the `K`-image), because the exact weld
   `e₄(e₁e₂e₃)e₄⁻¹ = −(e₁e₂e₃)` flips the spatial pseudoscalar = the orientation
   ([`GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION...`](GRAVITY_SIGN_IS_NOT_A_NEW_ADMISSION_REDUCES_TO_SHARED_ORIENTATION_DATUM_KCPT_CANNOT_SELECT_NARROW_THEOREM_NOTE_2026-06-18.md)).
   The random-`H` isospectrality below establishes the *carrier-independence* of the
   linear-algebra fact; the identification of the physical branch-map with conjugation is
   supplied by that weld. In this carrier `σ = e₄`-conjugation **= spatial parity `P`** (one
   operation), and `e₄² = −I`, so the `Z₂` is the conjugation *action* `σ(·)σ⁻¹` (involutive),
   not `e₄` itself.

1. **The conjugation-selector class is empty (carrier-independent).** For any Hermitian `H`
   and any conjugation `C` (unitary *or* anti-unitary), `spec(C H C⁻¹) = spec(H)`. So every
   symmetry-operation selector in the class **{K/CPT (anti-unitary), modular `J`, parity
   `P = σ`, chirality `Γ₅`}** leaves *every* spectral/energetic functional invariant — it
   cannot distinguish the two orientation branches. Verified machine-zero over 6 seeds and
   carrier sizes `n = 4,6,8,10,12`. **Consequence:** "run a bigger / interacting carrier to
   break the isospectrality" is a **provably dead falsifier**, and the absolute orientation
   label carries **no SPECTRAL/STATE gauge-invariant observable**. *(Topological action-offsets
   — the `θ`-term / Chern–Simons level — ARE `σ`-odd gauge-invariant observables, but they are
   non-spectral and are exactly the conceded `θ` gauge-side bridge, §5; they are not what is
   reclassified here.)*
2. **Selector characterization (scoped).** This adds to (1) exactly **one** fact. A selector
   must be `σ`-**odd** to separate the branches. (a) spectral functions `tr f(H)` are
   `σ`-even (a corollary of (1)); (b) `tr(sign(H)·O)` is `σ`-even iff `[O,σ]=0` (one-line
   cyclicity = the definition of `σ`-even). **New content (c):** a `σ`-odd functional needs an
   `O` that **anticommutes with `σ`** — a **`T`-odd** operator — whose one-point function
   *vanishes unless the state breaks `T`* (the external arrow); reading it from the label is
   circular. Positive control: such an `O` (`= e₁`) genuinely splits the branches
   (`±0.227`), so the dichotomy has teeth. Within the spectral + `σ`-equivariant class the
   orientation is a **`Z₂`-torsor with no canonical basepoint** — a registered boundary datum.
3. **Modular / KMS circularity (closes the Bisognano–Wichmann escape).** The modular
   conjugation `J` is an anti-unitary involution; the modular Hamiltonian of a Gibbs state is
   `K_mod = βH + const` (verified `‖K_mod − βH‖/‖βH‖ ~ 1e-16`), and `H → −H` flips
   `K_mod → −K_mod` (`β → −β`). Modular flow acquires a direction **only after** `sign(H≥0)`
   is chosen — which **is** the arrow input. So the modular/PCT route presupposes the
   orientation; it does not select it.

**What this reclassifies, and what it does NOT.** The **absolute** orientation sign is
**reclassified as sign/convention** (the `Y0`/`g0` vacuous-convention class) for the
spectral/state sector — it adds **no** admission. This is the **shared K-real orientation
piece** of both Tier-A admissions: the `θ` mass-side `{0,π}` pin (discharged at the bilinear
level by [`THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE`](THETA_MASS_SIDE_EPSILON_HERMITICITY_REALITY_BRIDGE_DISCHARGE_BOUNDED_THEOREM_NOTE_2026-06-11.md),
conditional on the K-real reading) and the `AC_φλ` `δ=0` orientation bit (the first of the two
bits of sub-admission (i); the orientation pin, **not** the `det_C`-vs-`det_R` value `r`). It
does **not retire either admission** — and the *one* `σ`-odd observable that survives the no-go
(§4, the topological `θ`-term / Chern–Simons level) **is** the `θ` gauge-side bridge that stays
open, which is *why* reclassifying the K-real sign is consistent: `θ` keeps its
**emergent-Q gauge-side bridge**
([`THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE`](THETA_GAUGE_SUBSTRATE_NO_WINDING_CARRIER_EMERGENT_Q_BRIDGE_BOUNDED_THEOREM_NOTE_2026-06-11.md)),
and `AC_φλ` keeps the **`det_C`-vs-`det_R` value `r`** (the `r=1` vs `r=1/2` magnitude wall),
the **Type-B radian-readout law** ([`KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY`](KOIDE_A1_RADIAN_BRIDGE_IRREDUCIBILITY_AUDIT_NOTE_2026-04-24.md)),
and the **species bridge**. The orientation result touches the *sign*, never the *magnitude*.

## 1. The selector class is empty (B1)

Conjugation preserves the spectrum: for unitary `U`, `U H U⁻¹` is similar to `H`; for
anti-unitary `K` (complex conjugation, possibly dressed by a unitary), `K H K⁻¹ = U H^T U†`,
and `H^T` is isospectral to Hermitian `H`. Every member of the orientation-selector class is
such a conjugation: `P = σ` (the `e₄` flip), `Γ₅` (unitary), and `K/CPT`, modular `J`
(anti-unitary). Given the **imported premise** that the opposite branch *is* the `σ`-conjugate
(the `e₄` weld, above), no spectral/energetic functional — energy, free energy, partition
function, any `tr f(H)` — separates a branch from its image. The runner confirms machine-zero
`max|dE|` over seeds and over `n = 4..12`: the random-`H` result is **carrier-independent**, so
enlarging or interacting the carrier cannot help the *linear-algebra* fact (the standing "maybe
a richer carrier breaks it" hope is foreclosed). What the runner does *not* itself prove is the
premise — that the physical branch-map is a conjugation — which is supplied by the cited weld.

## 2. Selector characterization: §1 + one new fact (B3)

This section adds to §1 exactly **one** thing. To *select* a branch a functional `F` must be
`σ`-odd (`F(σH) = −F(H)`). (a) spectral functionals `tr f(H)` are `σ`-even (a *corollary* of
§1's isospectrality); (b) `tr(sign(H)·O)` is `σ`-even iff `[O,σ]=0` (one-line cyclicity — the
*definition* of `σ`-even, same engine as §1). **New content (c):** a `σ`-odd functional needs
an `O` that **anticommutes** with `σ` — a `T`-**odd** operator — whose one-point function
*vanishes unless the state breaks `T`* (the external arrow); otherwise reading it amounts to
reading the orientation label, which is circular. The positive control confirms the dichotomy
has teeth: a `σ`-odd `O` (`= e₁`) genuinely splits the branches (`±0.227`). **Scope:** this is
a characterization over the named functional classes (spectral + `σ`-equivariant traces) on the
minimal carrier, *not* a universal impossibility proof (see §4 for the observable that escapes
it). It is the honest form of "within these classes the orientation is a torsor with no
canonical basepoint." (NB `σ = P` here, so the "commutant" framing is not an independent
survey; B3's content is just §1 plus the (c) characterization.)

## 3. Modular flow is circular for this datum (B4)

The one structure with a genuine direction — the KMS/modular flow — gets that direction from
the spectrum condition `H ≥ 0`. The runner builds the Gibbs state and recovers `K_mod = βH`,
and shows `H → −H` flips the modular generator. So Bisognano–Wichmann / Tomita–Takesaki cannot
*derive* the orientation: `sign(H)` is its **input**. (This is the rigorous form of the
gravity-sign note's "modular-PCT route is independently blocked"; it is a distinct,
conformal-scale/positivity mechanism from the K/CPT involution of §1.)

## 4. The observable that escapes the no-go (the third horn) (B5)

The no-go above covers only **spectral / state** functionals. One gauge-invariant `σ`-odd
observable is **non-spectral** and escapes: a **topological action-offset** — the 2+1
Chern–Simons level (computed: a QWZ Chern number `+1` for `m∈(0,2)`, `−1` for `m∈(−2,0)`, `0`
for `|m|>2`; it flips with the mass-sign branch and is a Berry invariant, not any `tr f(H)`),
whose 3+1 analog is the `θ`-term coefficient `arg det M ∈ {0,π}`. So the selector dichotomy has
**three horns**, not two: **circular** (reads the label) | **external** (Past Hypothesis /
`T`-breaking state) | **topological action-offset**. Crucially, that topological observable **is
exactly the `θ` gauge-side bridge** this note keeps open — so its existence does *not* reopen
what is reclassified (the K-real spectral sign); it is *why* the reclassification is consistent.

## 5. Reduction map (no admission added or retired)

- **Absolute orientation sign** → **convention** (`Y0`/`g0` class) for the spectral/state
  sector. No SPECTRAL/STATE gauge-invariant content (§1); no admissible `σ`-odd spectral
  selector (§2); modular flow circular (§3). The one `σ`-odd observable that survives is
  non-spectral and is the open `θ` gauge-bridge (§4).
- **Observable content** → the **relative arrow**, a **universal-floor Past Hypothesis** (a
  boundary state-selection, *not* a Tier-A admission, *not* a principle, *not* a status-bounding
  dependency; pinned by [`ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL`](ARROW_FROM_RECORD_FORMATION_PAST_HYPOTHESIS_RESIDUAL_NOTE_2026-06-05.md)).
  This is **separate** and **not** discharged here.
- **Shared K-real piece of both Tier-A admissions** → **reclassified as a sign/convention** (the
  `θ` mass-side `{0,π}` pin and the `AC_φλ` `δ=0` orientation bit). The `genuine_admitted_input_count`
  is **unchanged at 2**; `θ`'s emergent-Q gauge bridge (= the §5 escaping observable) and
  `AC_φλ`'s `r`-value / radian law / species bridge remain open. Any registry change is the
  audit lane's, not this note's.

**Runner:**
[`scripts/frontier_orientation_sign_conjugation_selector_class_empty_2026_06_18.py`](../scripts/frontier_orientation_sign_conjugation_selector_class_empty_2026_06_18.py)
(10/10; deterministic, matrices `≤12×12` + a 2D `24×24` Berry-flux grid (no 4D-BZ quadrature),
single process — memory-safe). No fitted parameters, no observed values, no axiom-file edits, no
`docs/audit/data/*` edits, no audit status. The isospectrality, KMS, and Chern-number facts are
universal; the framework's specific realization (the cited `e₄` weld) is what makes them the
orientation-sign atom shared by gravity, flavor, and `θ`.
