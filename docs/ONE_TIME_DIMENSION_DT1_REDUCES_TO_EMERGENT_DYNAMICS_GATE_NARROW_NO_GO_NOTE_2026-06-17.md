# One Time Dimension (d_t = 1) Reduces to the Emergent-Dynamics Gate; Multi-Time Is Kinematically Realizable

**Date:** 2026-06-17
**Type:** narrow_theorem (reduction + multi-time realizability witness) — no-go-flavored
**Claim type:** narrow_theorem

**Claim scope (narrow):** A characterization of where `d_t = 1` (exactly one emergent time
dimension) comes from, with a computed witness. **(1)** `d_t = 1` factors as
`[LOWER: d_t ∈ {1,3,5,…}]` ∩ `[UPPER: d_t ≤ 1]`; the lower bound is framework-internal
(anomaly bridge, conditional on declared premises), the upper bound is carried **entirely**
by the declared premise **B-AXIS.3 / N5** ("no independent commuting transfer factor as a
second physical clock"), an instance of the already-named **emergent-dynamics open gate**.
**(2)** Computed witness: a second independent commuting clock exists on the fixed spatial
Hilbert space `H = ⊗_{x∈Z³} C²`, so **multi-time (`d_t > 1`) is kinematically realizable** and
N5 is non-vacuous. **(3)** The only candidate upper-bound forcings (Tegmark well-posedness;
Record single-order; Clifford-within-odd) are external, circular, or symmetry-blind.
**Conclusion:** `d_t = 1` **reduces with no new admission** to the emergent-dynamics gate; it
is **not derivable** on the current surface. This note proposes **no** status change and edits
no other note. **Status authority: independent audit lane only.**

## 1. The question and the established bounds

The framework is `Z³` space (Lattice axiom; `d_s = 3` primitive) + **emergent** time (never a
fundamental `Z⁴`). The open atom: why `d_t = 1`?

- **Lower bound (framework-internal, conditional).** The anomaly-forces-time ABJ bridge
  ([`…ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE…`](ANOMALY_FORCES_TIME_ABJ_INCONSISTENCY_ACCEPTED_PREMISE_BRIDGE_BOUNDED_NOTE_2026-05-26.md),
  re-verified in [`…PREMISE_MANIFEST_RECHECK…`](ANOMALY_FORCES_TIME_BRIDGE_PREMISE_MANIFEST_RECHECK_NOTE_2026-06-17.md)):
  anomaly cancellation ⇒ Clifford `γ₅` ⇒ total `d = d_s + d_t` even ⇒ with `d_s = 3`,
  `d_t ∈ {1,3,5,…}`. Conditional on declared premises P-ABJ, P-HY, P-COMP, P-REC.
- **Upper bound (`d_t ≤ 1`).** Carried entirely by the declared premise **B-AXIS.3 = N5**
  of the single-clock theorem
  ([`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md),
  retained_no_go): "no independent commuting transfer factor is admitted as a second clock."
  Stone uniqueness ([`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS…`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md),
  retained) gives a **unique generator GIVEN one transfer** — it is transfer-relative and does
  **not** fix the *number* of independent generators.

So `d_t = 1 = [d_t ≥ 1 \text{ odd}] ∩ [d_t ≤ 1]`, and the cap is the dynamics gate, not a theorem.

## 2. Multi-time is kinematically realizable (runner `[MULTI-TIME]`, witness)

On `H = C² ⊗ C²` (two sites), the two commuting Hermitian generators `G₁ = σ_z ⊗ I`,
`G₂ = I ⊗ σ_z` give (all computed, residual 0):

- `[G₁, G₂] = 0` (commuting "clocks"); `span{G₁, G₂}` is rank 2 (a genuine *second* time
  direction, not collinear);
- `U(s,t) = exp(-i(sG₁ + tG₂))` is a true `R²` group homomorphism — a `d_t = 2` multi-time
  evolution;
- the off-diagonal element `U(1,0)` is **not** on any single-clock (sum-generator) orbit
  `exp(-ir(G₁+G₂))` (min gap `1.356 > 0.05` over a fine `r`-scan).

So a second independent commuting clock **exists** on the framework's fixed kinematics;
`{Quantum, Locality}` do not exclude `d_t > 1`. The **Record** axiom adds nothing: it is a
finitely-additive scalar readout over **unordered** finite pairwise-disjoint collections of
records (MINIMAL_AXIOMS_2026-06-05), carrying no order and no constraint on the *number* of
commuting generators. Hence `{Quantum, Locality, Record}` jointly do **not** exclude multi-time,
and B-AXIS.3 / N5 is a **non-vacuous, underived** premise.

## 3. The candidate upper-bound forcings fail (runner `[CLIFFORD-ODD]`, `[FORCING-STATUS]`)

- **Clifford-within-odd — symmetry-blind.** `γ₅` exists (anticommutes with all `γ_μ`) for
  `d_t = 1, 3, 5` alike (`d = 4, 6, 8`, all even; computed). The Clifford/anomaly argument
  yields only `d_t ∈ {odd ≥ 1}`; it does **not** single out `d_t = 1`.
- **Tegmark / ultrahyperbolic well-posedness — imported.** `d_t ≥ 2` makes the IVP ill-posed,
  *if one demands deterministic predictive evolution*. The axioms demand no such thing: Record
  is timeless and the realized-state primitive (REALIZED_STATE_PRIMITIVE_NOTE_2026-06-11) fixes
  the state **pointwise**, never requiring the present to predict the future. External/anthropic,
  not framework-internal (and flagged non-load-bearing in the parent theorem).
- **Record single-total-order — supplied, not derived.** The Record axiom is *unordered*; the
  single linear registration order is a *supplied* post-record layer (POST_RECORD_*; explicit
  firewall against a Record-derived arrow/order). It does not derive the dimensionality.
- **Stone / N5 — circular.** Stone gives uniqueness *given one* generator; invoking N5 to kill
  multi-time presupposes the single clock it would prove.

## 4. Result and distinction from the arrow admission

`d_t = 1` is **not** forced by `{Lattice, Quantum, Record}` and is **not** a new admission: it
**reduces with no new admission to the emergent-dynamics open gate**, specifically the
single-generator clause B-AXIS.3 / N5. The lower half (`d_t ≥ 1` odd) is framework-internal
(conditional on declared premises); the upper half (`d_t ≤ 1`) is the dynamics gate under a
different label.

This is **distinct from the arrow admission**: N5 governs **dimensionality** (how many
commuting time-generators), while the arrow governs the **direction** of one time. They are
separate; `d_t = 1` does not reduce to the arrow.

**Honest open atom (for any future forcing):** to derive `d_t = 1` one must add a
framework-internal reason that the emergent dynamics is **single-generator** (one-parameter) —
a registration-direction / one-clock ingredient — that excludes the kinematically-realizable
second commuting clock of §2 **without presupposing it**. No such route exists on the current
surface (every internal candidate is order/transport-invariant and cannot reduce the generator
count). The sharpest next artifact is a direct N5 no-go formalizing exactly that.

**Runner:** [`scripts/one_time_dimension_dt1_reduction_check_2026_06_17.py`](../scripts/one_time_dimension_dt1_reduction_check_2026_06_17.py)
(`TOTAL: PASS=9 FAIL=0`, deterministic, no RNG, < 1s). No fitted parameters, no observed
values, no new axioms, no axiom-file edits, no `docs/audit/data/*` edits. Sets no audit status.
