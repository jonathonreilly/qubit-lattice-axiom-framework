# The Antiperiodic-BC Axis Datum Is S₄-Transportable, and Native-on-Z³ Reduction: Single-Clock Axis Selection Has No Euclidean-Surface Supplier

**Date:** 2026-06-17
**Type:** narrow_theorem (computed S₄-transitivity of the axis datum) + axis-selection
route characterization (no-go-flavored)
**Claim type:** narrow_theorem

**Claim scope (narrow):** Two computed results plus one structural reduction, all on the
axis-label component of (B-AXIS.2) of
[`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md)
(audited_conditional). **(1)** On the even cubic-symmetric staggered block (equal even
extent per axis — the standard staggered-fermion even-extent condition; runner block [SCOPE]
exhibits the odd-extent falsifier), the per-axis
antiperiodic-boundary-condition Z₂ datum named as the minimal axis-selecting input by
[`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md)
is **itself transportable around all four axes**: the adjacent signed-permutation
exchanges `W_{a,a+1} = P_{a↔a+1} ∘ diag((-1)^{x_a x_{a+1}})` each preserve the periodic
staggered hop exactly **and** map the antiperiodic-axis-`a` configuration exactly onto the
antiperiodic-axis-`(a+1)` configuration (computed residuals `0`). These transpositions
generate `S₄` acting transitively on the four axes, so the antiperiodic-axis label is a
single 4-element orbit. **Consequence:** the Z₂ BC datum selects the evolution axis **only
relative to an already-privileged axis**; it is not by itself a non-transportable axis
supplier. **(2)** The discrete reality/sublattice-parity grading `ε(x)=(-1)^{Σ_μ x_μ}`
(`ε D ε = -D`) is **exactly W-invariant** (`W ε W^T = ε`), so the reality/CPT-type structure
is W-inert and carries no axis label. **(3)** Reduction: the only framing that dissolves the
axis-label question — time as the parameter of a one-parameter group/semigroup over the
**fixed** spatial Hilbert space `⊗_{x∈Z³} C²` (not a fourth lattice coordinate) — relocates
the residual to the already-named **emergent-dynamics open gate** of
[`MINIMAL_AXIOMS_2026-06-05.md`](MINIMAL_AXIOMS_2026-06-05.md) (the axioms supply no
dynamics); it does not derive the axis from retained content. **Conditional positive:** given
one privileged axis (equivalently, a supplied self-adjoint generator), the evolution
axis/clock is unique with no second commuting clock, per the retained Stone uniqueness.

This note makes **no** axis-selection derivation claim and proposes **no** status change for
any row. It records computed transport facts and a structural reduction.

**Status authority:** independent audit lane only. This source note does not set or predict
an audit outcome; audit verdict and effective status are set only by the independent audit
lane.
**Loop:** science-fix lane 2026-06-17 (B-AXIS follow-up; find-the-escape panel, two waves +
native-on-Z³ probe).
**Runner:**
[`scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py`](../scripts/single_clock_axis_datum_s4_transportable_check_2026_06_17.py)
(`TOTAL: PASS=22 FAIL=0`, deterministic, no RNG, runtime well under one minute).
**Authority role:** source-note proposal. If retained, this row supplies (a) the computed
S₄-transitivity of the antiperiodic-axis datum (sharpening the 2026-06-11 pin), and (b) the
characterization that the single-clock axis label has no non-transportable, non-circular
supplier on the Euclidean reconstruction surface and reduces, under the native framing, to
the emergent-dynamics open gate.

## 1. Context and the precise question

The 2026-06-11 hostile re-scope of the single-clock evolution theorem withdrew the old
no-second-clock S3 and demoted evolution-axis selection to the declared premise (B-AXIS),
because the staggered-Dirac hop on the Euclidean block `Λ = (Z/Lτ) × (Z/Ls)³` is exactly
invariant under the conjugated exchange `W = P_{τ↔1} ∘ diag((-1)^{x_τ x_1})` (certificate
residual `0`; the plain swap without the sign field fails, so the certificate is non-trivial).
The governing boundary
[`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md)
(retained_no_go) states Stone uniqueness is transfer- and τ-relative; B-AXIS is its three
clauses N2 (the time step), N4 (axis/transfer-construction uniqueness — the **axis-label**
part is the target here), N5 (no independent commuting clock factor).

The route-pruning no-go (2026-06-11, currently unaudited — its computations are **recomputed
here**, not cited as authority) showed every W-transportable retained structure (OS/GNS,
record-durability, registration cone, anomaly chain) fails, and named the minimal escape: a
single per-axis Z₂ datum (antiperiodic-`τ`/periodic-space) breaks `W` exactly. A subsequent
note
[`SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md`](SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md)
(unaudited) pruned KMS/APBC as a supplier (the trace circle presupposes the τ axis).

**The question this note settles:** is that per-axis Z₂ datum a *non-transportable* axis
supplier, or is *which axis carries it* itself transportable — and is there any
Euclidean-surface enrichment (reality/CPT, gauge, tensor structure) that breaks `W`
non-transportably without presupposing the generator? And does the alternative "native"
framing (time off the 4-torus) derive the axis or relocate the admission?

## 2. Inputs (one hop, with exact licenses and fresh statuses)

| Input | Where used | License / status (origin/main, 2026-06-17) |
|---|---|---|
| The exchange certificate `W M W^T = M` (residual 0) and the declared (B-AXIS) | §1, runner [S] | [`AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03`](AXIOM_FIRST_SINGLE_CLOCK_CODIMENSION1_EVOLUTION_THEOREM_NOTE_2026-05-03.md) — bounded_theorem (audited_conditional); certificate **recomputed**, not cited blind |
| N2/N4/N5 reopening clauses; transfer-/τ-relativity | §1, §5 | [`SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06`](SINGLE_CLOCK_UNIQUENESS_SCOPE_BOUNDARY_2026-06-06.md) — **retained_no_go** |
| Stone finite-dim uniqueness (given positive `T`, fixed `τ`) | §5 conditional positive | [`SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10`](SINGLE_CLOCK_STONE_FINITE_DIM_UNIQUENESS_NARROW_THEOREM_NOTE_2026-05-10.md) — **retained** |
| The "sharpened pin" (per-axis Z₂ BC datum breaks `W`) | §3 (recomputed + sharpened) | [`SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11`](SINGLE_CLOCK_AXIS_SELECTION_FROM_RECORD_DURABILITY_NARROW_NO_GO_NOTE_2026-06-11.md) — **unaudited** (computation recomputed here; treated as a map, not authority) |
| KMS/APBC pruning (trace presupposes τ) | §4 | [`SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16`](SINGLE_CLOCK_KMS_APBC_AXIS_SUPPLIER_NO_GO_NOTE_2026-06-16.md) — **unaudited** |
| Axioms supply no dynamics; record-production dynamics is an open gate | §5 reduction | [`MINIMAL_AXIOMS_2026-06-05`](MINIMAL_AXIOMS_2026-06-05.md) — axiom memo |
| Post-record event order is axis-label-free; rates need a supplied τ | §5 | [`POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06`](POST_RECORD_CLOCK_RATE_INTERFACE_2026-06-06.md) — **retained_no_go** |
| Record formation not unconditionally forced; continuous generator may not embed | §5 | [`RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06`](RECORD_FORMATION_NOT_UNCONDITIONALLY_FORCED_BY_MINIMAL_AXIOMS_NARROW_NO_GO_NOTE_2026-06-06.md) (retained_no_go); [`RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06`](RECORD_MARKOV_GENERATOR_EMBEDDABILITY_BOUNDARY_2026-06-06.md) (retained_no_go) |
| Relativistic content rides a supplied continuum carrier | §5 | [`FREE_DIRAC_POINCARE_STONE_DIFFERENTIAL_GENERATOR_COINCIDENCE_COMMON_CORE_BOUNDED_THEOREM_NOTE_2026-06-08`](FREE_DIRAC_POINCARE_STONE_DIFFERENTIAL_GENERATOR_COINCIDENCE_COMMON_CORE_BOUNDED_THEOREM_NOTE_2026-06-08.md) — retained_bounded |

No fitted parameters, no observed values, no new axioms, no axiom-file edits, no imports.

## 3. The S₄-transitivity theorem (computed; runner blocks [S],[T],[REST],[SCOPE])

On the **even** cubic-symmetric block `L=(4,4,4,4)`, `m=0.3`, time-first staggered phases, with
the signed exchange `W_{a,b} = P_{a↔b} ∘ diag((-1)^{x_a x_b})` (even extent is required — the
periodic staggered η-phase closes consistently across the boundary wrap only for even extent;
block [SCOPE] exhibits the odd-extent falsifier, `‖W M W^T − M‖ = 6 ≠ 0` at `L=(3,3,3,3)`, and
the recompute reproduces the exact-zeros independently at `m=0.3, 1.7`, `L=(6,6,6,6)`, and under
an alternate equivalent staggered-phase convention):

- **[S]** `W_{0,1}` is orthogonal and preserves the periodic staggered hop exactly
  (`‖W M W^T − M‖ = 0`); the plain swap without the sign field fails (`‖P M P^T − P‖ ≈ 22.6 > 1`),
  so the certificate is non-trivial.
- **[T]** For each adjacent pair `(a,a+1) ∈ {(0,1),(1,2),(2,3)}`: `W_{a,a+1}` preserves the
  periodic hop (residual `0`) **and** maps the antiperiodic-axis-`a` operator exactly onto the
  antiperiodic-axis-`(a+1)` operator (`‖W M_ap(a) W^T − M_ap(a+1)‖ = 0`), with a strictly
  nonzero self-residual (`‖W M_ap(a) W^T − M_ap(a)‖ = 16 > 1`) confirming the BC is genuinely
  moved. The transpositions `(0,1),(1,2),(2,3)` generate `S₄`, which acts **transitively** on
  the four axes.
- **[REST]** Antiperiodic-axis-0 alone breaks the fixed `W_{0,1}` (the pin; nonzero residual);
  antiperiodic in **both** axes 0,1 restores `W_{0,1}` exactly (residual `0`).

**Theorem (computed).** The antiperiodic-axis label lies in a single transitive `S₄` orbit of
the staggered signed-permutation automorphism group. Hence supplying "one axis is antiperiodic"
fixes the evolution axis **only relative to an already-privileged axis**; the per-axis Z₂ BC
datum is not, by itself, a non-transportable axis supplier.

**Relation to the 2026-06-11 pin (narrowing observation, not a grade).** The route-pruning
no-go correctly computes that the Z₂ datum breaks a *fixed* `W`. Its summary language ("the
minimal axis-selecting input is … a single per-axis Z₂ datum") reads as if the datum *selects*
the axis. The computation above shows the datum's axis-choice is itself `S₄`-transportable, so
the selection is relative, not absolute. Aligning that note's language to its audited scope is
a candidate narrowing repair for the independent audit lane to weigh; this note authors no
grade and edits no other note.

## 4. Euclidean-surface enrichments do not break W non-transportably (runner block [R] + cited)

- **Reality / discrete grading (computed, [R]).** `W` is a real operator (commutes with
  `K`=complex conjugation). The sublattice-parity grading `ε(x)=(-1)^{Σ_μ x_μ}` satisfies
  `ε D ε = -D` and is **exactly W-invariant** (`W ε W^T = ε`, residual `0`): `W` permutes
  coordinates (leaving `Σ_μ x_μ` fixed) and its diagonal sign field commutes with the diagonal
  `ε`. So the reality/CPT-type grading is W-inert and carries no axis label. (Invariance fact
  about the grading operator only — not a chirality identification; no collision with the
  narrow chirality no-go, which forbids only the hybrid `γ_CL=Γ_χ`.)
- **KMS / thermal-trace antiperiodicity** is circular as a supplier: the trace `Tr e^{-βH} =
  Tr T^{Nτ}` presupposes the τ-transfer (so it presupposes the axis); APBC is a consumed
  finite-temperature convention, not derived (see the 2026-06-16 note).
- **Wilson temporal-gauge / plaquette** singles out an axis only through the labeled choice
  `U_0 = 1` (an axial-gauge choice transportable to `U_1 = 1`) and the choice of reflection
  plane; the plaquette action and the character/Bessel positivity coefficients are axis-blind.
- **QUANTUM tensor factor** `⊗_{x∈Z³} C²` does not stamp which three scaffold axes are
  spatial: both the τ-slice and an `x_1`-slice carry an equally-valid positive transfer, so the
  tensor-factor framing reduces to the (already-transportable) Osterwalder–Schrader
  reconstruction route.

No enrichment on the Euclidean reconstruction surface breaks `W`/`S₄` non-transportably
without presupposing the generator `H` (equivalently, the axis).

## 5. The native-on-Z³ reduction (the one framing that dissolves the axis — and what it costs)

If time is the parameter of a one-parameter unitary group / CPTP semigroup `U(t)` over the
**fixed** spatial Hilbert space `⊗_{x∈Z³} C²` — not a fourth lattice coordinate — then `W` and
the staggered `S₄` have no referent (a semigroup parameter is not a lattice axis; there is no
fourth `Z`-axis to permute), and the codimension-1 Cauchy slice is the spatial lattice itself
(`dim = 3`). The retained Stone uniqueness applies directly to any such `U(t)` on the fixed
finite-dimensional space, with **no** transfer-from-reflection construction. In this framing
the "which-of-four-axes" question has no object.

**But the generator is not axiom-supplied, so this reduces rather than derives.** The axioms
supply no dynamics (`MINIMAL_AXIOMS_2026-06-05`: Lattice/Quantum/Record each "does not supply a
dynamics"; record-production dynamics is an explicit open gate). The only retained generator
over the lattice is the RP/transfer reconstruction — which is the Euclidean 4-torus route that
carries `W`/`S₄`. A generator sourced from the record-production dynamics lands in the
open gate, where record formation is "not unconditionally forced" and a continuous one-parameter
generator may not even embed (the swap kernel has `det = -1`, no finite real generator). Even
granting an axis-free parameter, its **orientation** (past→future) reduces to the
already-admitted past-hypothesis and its **rate/metric** needs a supplied `τ`
(`POST_RECORD_CLOCK_RATE_INTERFACE`, retained_no_go). And the **relativistic** content
(dispersion, Lorentz, the Dirac connection) rides on the staggered two-step transfer / a
supplied continuum mass-shell carrier, so a strictly axis-free clock is non-relativistic.

**Net characterization (register-not-read).** The single-clock evolution-axis **label** is a
registered datum, not a pre-record operator to derive from the Euclidean surface. The native
framing genuinely dissolves the axis-among-four question and is a strictly **honester premise
shape** — it replaces a misleadingly-derivable-looking axis-label premise with a
transparently-named admission ("an emergent one-parameter dynamics over `Z³` is supplied") —
but it does **not** reduce the admission content: the residual is the emergent-dynamics open
gate (generator existence + a supplied `τ` + no second commuting clock), with orientation
already carried by the past-hypothesis. This is the same admission CLASS as the standing
register-not-read price; no primitive on the Euclidean surface fixes it.

**Conditional positive (retained).** Given one privileged axis — equivalently, a supplied
self-adjoint generator `H` (with the spectrum condition `H ≥ 0`) on `⊗_{x∈Z³} C²` — the
evolution group `U(t)=exp(-itH)` is unique and there is no independent commuting second clock,
by the retained Stone uniqueness. The axis-conditional single-clock theorem stands exactly as
its (B-AXIS) header declares; this note characterizes the premise, it does not discharge it.

## 6. No-go discipline (N1–N8) for the negative clause

- **N1 (alternative-route enumeration).** Axis-selector routes surveyed: action/RP exchange
  (W-invariant), OS/GNS reconstruction, record durability, registration cone, anomaly chain
  (all W-transportable per the recomputed 2026-06-11 certificates), KMS/APBC (circular, 2026-06-16),
  Cl(3) reality/CPT grading (W-inert, [R]), Wilson temporal-gauge (labeled choice), QUANTUM
  tensor factor (reduces to OS), dimension-selection (axiomatic off-surface, but the theorem
  lives on the 4-torus), native-on-Z³ (reduces to the emergent-dynamics open gate, §5).
- **N2 (wall-independence).** The S₄-transitivity is an exact computed fact about the staggered
  hop (runner [T]); it does not depend on any contested authority. The retained anchors
  (scope-boundary, Stone) are verified on origin/main.
- **N3 (hidden-wall scan).** No undisclosed dependence: the runner recomputes the W certificate
  and the pin from scratch; the unaudited sibling notes are used only as maps (recomputed), not
  as authorities.
- **N4 (residual matching).** The residual is named precisely: the emergent-dynamics admission
  (generator existence + τ + no-second-clock), with orientation = past-hypothesis. It is not a
  derivable Euclidean-surface operator.
- **N5 (rhetoric audit).** No "only/last route/exhausted/closes" language. The native framing is
  recorded as a live honester-premise reduction; the open gate is named, not closed; future
  positive suppliers (a non-transportable registration-direction theorem, or a native generator
  derivation) remain open paths. This note authors no audit grade.
- **N6 (partial-closure path).** The conditional positive (§5) is the retained partial closure:
  given one privileged axis / a supplied generator, uniqueness and no-second-clock hold. A future
  derivation of the generator from a conditional record-production layer would discharge the gate.
- **N7 (steelman).** Strongest pro-derivation case: "the antiperiodic-τ BC is the physical
  fermion thermal convention, so it is not free." Rebuttal (computed): which axis carries the
  antiperiodic BC is `S₄`-transportable ([T]); and the thermal convention presupposes the trace
  circle = the τ-transfer (circular, §4). The datum breaks a *fixed* W but is not a
  non-transportable supplier.
- **N8 (cross-cycle echo).** Consistent with the scope-boundary (retained_no_go), the
  route-pruning and KMS notes (unaudited), and the independent witness in `ANOMALY_FORCES_TIME`
  ("it does not derive d_t=1; it derives 'given Λ=Z_τ×Z³, exactly one U(t)'").

## 7. Boundary / honest-auditor read

This note does **not** derive the single-clock evolution axis, and does **not** change the
status of any row. Its load-bearing positive content is the computed S₄-transitivity of the
antiperiodic-axis datum (runner [T], residuals `0`) and the W-inertness of the reality grading
(runner [R]); these are exact finite-dimensional facts. The characterization in §4–§5 is a
reduction, not a theorem: it shows the axis label has no non-transportable, non-circular
supplier on the Euclidean reconstruction surface, and that the native-on-Z³ framing relocates
the residual to the already-named emergent-dynamics open gate (a strictly honester premise
shape, not fewer admissions). Whether the axis-conditional single-clock theorem should be read
with (B-AXIS.2) as a characterized register-not-read admission — and what that implies for its
effective status — is for the independent audit lane to decide.
