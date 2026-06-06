# Axiom-First Spectrum Condition (Lattice Analogue) on Cl(3) ⊗ Z^3

**Date:** 2026-04-29 (citation-graph repair: 2026-05-02; 2026-05-30
staggered-only-sector rescope: repoint the load-bearing transfer-matrix
positivity input from the full reflection-positivity umbrella row to the
in-repo-derived per-config two-step transfer-positivity sector, and
decouple (SC4) from the asserted-gap cluster-decomposition import;
2026-06-06 blocked-time normalization repair: align `H` and `m_gap` with
the two-step object `T := T_hat^2`, so the physical time spacing is
`2 a_tau`).
**Status:** support — source note on the minimal axiom surface; runner passing;
audit-pending. (SC1)–(SC3) are stated **conditional on the
staggered-only per-config two-step transfer positivity sector** named
below; (SC4) is rescoped to a **conditional** temporal-decay corollary on
a supplied gap. No promotion is claimed; the independent audit lane owns
any verdict.
**Loop:** `axiom-first-foundations-block02`
**Cycle:** 1 (Route R7)
**Runner:** `scripts/axiom_first_spectrum_condition_check.py`
**Log:** `outputs/axiom_first_spectrum_condition_check_2026-04-29.txt`

## Cited authorities (one hop)

The load-bearing input to (SC1)–(SC3) is a **positive Hermitian transfer
matrix `T` on a finite physical Hilbert space `H_phys`** on the
staggered-only surface. As of the 2026-05-30 rescope this input is taken
from the in-repo-derived **two-step blocked transfer-positivity sector**,
not from the full `U`-integrated interacting reflection-positivity claim.
The one-hop source authorities are:

- [`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md)
  — the in-repo first-principles derivation that the **free** (`U = 1`)
  two-step blocked transfer matrix `T_hat^2` is positive Hermitian
  (`T_hat^2 = B^dag B`, `H_hat = -log(T_hat^2)/(2 a_τ) ≥ 0`), anchored to
  the exact free staggered dispersion. This supplies the `T` positive-
  Hermitian input of Step 1 on the free surface.
- [`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)
  — extends the same two-step positivity from `U = 1` to a **fixed,
  arbitrary `SU(3)` (and `U(1)`) spatial background in temporal gauge,
  config-by-config**: `T_hat^2[U]` positive Hermitian,
  `H_hat[U] = -log(T_hat^2[U])/(2 a_τ) ≥ 0`. This carries the `T`
  positive-Hermitian input of Step 1 from the free to the fixed-background
  staggered surface. Its downstream P2 residual is not used here.
- [`AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`](AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md)
  — the in-repo blocked-time normalization bridge: the staggered two-step
  block `T_hat^2` advances two lattice time steps, so the physical
  Hamiltonian and transfer gap use `-(1/(2 a_τ)) log(T_hat^2 / M_T)`;
  the old `1/a_τ` normalization would double the Hamiltonian and gap.
- [`STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`](STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md)
  — the positive determinant weight `det(M_KS + m·I) ≥ m^n > 0`
  config-by-config on every `SU(3)` background, supplying the positive
  fermion measure of the staggered surface.
- [`REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`](REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md)
  — the abstract finite Cauchy–Schwarz / symmetric-involution norm-square
  identity supplying the gauge/bosonic-half factor.

These are the same four authorities the reflection-positivity row itself
names as the established factors of its staggered-only sector; this note
cites them directly rather than through the umbrella row so that (SC1)–
(SC3) do not load-bear on the umbrella's still-open `U`-integrated full
interacting `SU(3)` closure.

**Context see-also (not load-bearing here; plain text so the citation
graph does not record an upstream edge).** The full reflection-positivity
umbrella row `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md`
collects the staggered-only sector above together with a `U`-integrated
full interacting `SU(3)` reduction target that remains `unaudited`. This
note no longer imports that umbrella's `U`-integrated claim: Step 1 needs
only "`T` positive Hermitian on the finite `H_phys`", which the four
sector authorities above supply for the free and fixed-background
staggered surfaces. Consumers that previously read this row as backed by
the umbrella's full interacting claim should note the narrowed surface.

## Scope

**In scope (load-bearing).** On the **staggered-only** action surface
`S = S_G[U] + bar(chi)(M_KS[U] + m·I) chi`, `m > 0`, the two-step blocked
transfer matrix `T := T_hat^2` is positive Hermitian on a finite physical
Hilbert space `H_phys := H_phys^(2)` — established in-repo for the free
(`U = 1`) case and for fixed, arbitrary `SU(3)`/`U(1)` spatial backgrounds
in temporal gauge, config-by-config, by the four sector authorities above.
This note records the lattice analogue of the **spectrum condition** for
that `T`: the reconstructed Hamiltonian `H := -(1/(2 a_τ)) log(T/M_T)` on
`H_phys` is self-adjoint and bounded below. After this note, any package
lane that relies on "the Hamiltonian is positive after vacuum subtraction"
can cite this axiom-first lattice statement on the staggered-only surface
of the minimal axiom setup instead of treating the spectrum condition as a continuum
import — **with the conditional scope stated here**.

**Out of scope (not claimed by this note).**

- The full staggered **+ Wilson** plaquette extension: the determinant /
  transfer-positivity inputs are claimed only on the staggered-only
  surface, matching the sector authorities. The Wilson subsurface is not
  asserted.
- The `U`-integrated full interacting `SU(3)` reflection positivity as an
  unconditional theorem: the sector authorities supply per-config
  fixed-background positivity plus the two named factor notes; the
  `U`-integrated closure is a reduction target of the umbrella row and
  stays out of this note's load-bearing surface.
- Unconditional spatial cluster decomposition (see (SC4) below): this note
  does not import it. (SC4) is rescoped to a conditional temporal-decay
  corollary on a supplied gap.

## Minimal-axiom objects in use

The transfer matrix `T := T_hat^2` and finite physical Hilbert space
`H_phys := H_phys^(2)` are the two-step blocked objects of the staggered-
only sector authorities (free `U = 1` derivation plus its fixed-background
extension). They are finite-dimensional by construction (a free quadratic
fermion Fock space at fixed gauge background), so all spectral statements
below are elementary finite-dimensional linear algebra on a bounded
positive Hermitian `T`. Because `T` is the two-step object `T_hat^2`, its
physical time interval is the blocked interval `a_blk := 2 a_τ`; all energy
and gap rates below use this blocked interval.

The time-spacing convention is not an added axiom. It is inherited from
the blocked object itself: `T_hat^2` is one period-two block and advances
two single lattice time steps. Therefore the Hamiltonian reconstructed
from `T := T_hat^2` is normalized by `2 a_τ`, not by `a_τ`. The companion
bridge note and runner prove that the old `1/a_τ` normalization gives
exactly twice the same vacuum-subtracted Hamiltonian and mass gap.

## Statement

Let `T := T_hat^2` be the two-step blocked staggered-only transfer matrix
on the finite physical Hilbert space `H_phys`, positive Hermitian by the
sector authorities (free `U = 1` and fixed-background `SU(3)`/`U(1)`
config-by-config). Let `M_T := ‖T‖_{op}` be its operator norm and
`a_blk := 2 a_τ` its blocked temporal spacing. Then on the staggered-only
surface of the minimal axiom setup:

**(SC1) Self-adjointness.** `H := -(1/(2 a_τ)) log(T / M_T)` is a
self-adjoint operator on `H_phys`. *(Unconditional given `T` positive
Hermitian.)*

**(SC2) Boundedness below.** `H ≥ 0` on `H_phys`. The ground state
energy is `E_0 := 0`, and all excited-state energies satisfy
`E_n ≥ 0`. *(Unconditional given `T` positive Hermitian.)*

**(SC3) Energy gap (conditional on non-degeneracy).** If `T` has a
non-degenerate top eigenvalue `M_T` with next eigenvalue `λ_1 < M_T`, then
the mass gap `m_gap := E_1 - E_0 = -(1/(2 a_τ)) log(λ_1 / M_T) > 0`. On a
finite carrier the free staggered `T_hat^2` has a non-degenerate vacuum
(the runner exhibits `m_gap > 0` on the tested finite surface), but
non-degeneracy is **not** asserted as a closed-form property of every
canonical configuration; where it fails, `m_gap ≥ 0` with equality
permitted.

**(SC4) Conditional temporal-decay corollary (no unconditional cluster
decomposition imported).** *Given* the transfer-matrix gap `Δ_T := m_gap
> 0` of (SC3), the finite-block temporal transfer-matrix bridge note
[`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md)
gives exponential decay of **temporal**
ground-state connected correlators at rate `Δ_T = m_gap`, with an explicit
finite-temperature excited-state-population correction. This note does
**not** assert unconditional spatial cluster decomposition: that requires a
separate spatial cluster-decomposition theorem and an
independently derived gap, neither of which is claimed here. (SC4) is
therefore a corollary conditioned on (SC3)'s gap input, not an import of an
unconditional clustering theorem.

## Proof

### Step 1 — `T` is positive Hermitian (cited from the staggered-only sector authorities)

By the in-repo free-case derivation
([`AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`](AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md))
and its fixed-background extension
([`RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`](RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md)),
the two-step blocked transfer matrix `T := T_hat^2` is positive Hermitian
on the finite `H_phys`: `T_hat^2 = B^dag B` with `B = exp(-a_τ H_hat)` and
`H_hat ≥ 0`, so `spec(T) ⊆ (0, M_T]` with `M_T = ‖T‖_{op} < ∞`. (Because
`H_hat ≥ 0` the spectrum is strictly positive; the vacuum eigenvalue is
`M_T` and there is no nontrivial kernel on this finite Fock space, so
`H_phys^× = H_phys`.) The positive determinant weight and gauge-half
norm-square factors that complete the staggered-only `U`-integrated
inequality are the two named factor notes; they are not
re-derived here.

### Step 2 — Functional calculus gives `log(T / M_T)`

Because `spec(T) ⊆ (0, M_T]` (Step 1), `T / M_T` is a positive Hermitian
operator with spectrum `(0, 1]`. The (finite-dimensional) functional
calculus defines `log(T / M_T)` as a self-adjoint operator with spectrum
`(-∞, 0]` (since `log` is real on positive reals and `log(1) = 0`).

Because `T` is the two-step block `T_hat^2`, the physical block spacing is
`2 a_τ` by the blocked-time normalization bridge. Hence
`H := -(1/(2 a_τ)) log(T / M_T)` is self-adjoint on `H_phys` with
spectrum `[0, +∞)`. (No kernel-extension is needed: `T` has no nontrivial
kernel on this finite Fock space, so `H_phys^× = H_phys`.) This proves
(SC1) and (SC2) unconditionally given the Step-1 positivity input.

### Step 3 — Ground state and gap (conditional on non-degeneracy)

The top eigenvalue of `T / M_T` is `1`, achieved by the vacuum
`|0⟩_phys`. Then `H |0⟩_phys = 0`, so `E_0 = 0`.

If the top eigenvalue `M_T` is non-degenerate, the next eigenvalue
`λ_1 < M_T`, and

```text
    m_gap   =   E_1 - E_0   =   -(1/(2 a_τ)) log(λ_1 / M_T)   >   0.    (1)
```

Non-degeneracy holds on the tested finite carrier (the runner exhibits
`m_gap > 0`), but is **not** asserted as a closed-form property of every
canonical configuration; this is the conditional content of (SC3). Where
the top eigenvalue is degenerate, (1) gives `m_gap = 0`.

### Step 4 — Conditional temporal-decay corollary (no unconditional cluster import)

This step is a corollary *conditioned on* the gap `Δ_T := m_gap > 0` of
Step 3, not an import of an unconditional cluster-decomposition theorem.
Given `Δ_T > 0`, the finite-block temporal transfer-matrix bridge
([`CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`](CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md))
bounds the temporal connected correlator
`|⟨A(τ) B(0)⟩_c| ≤ C e^{-Δ_T τ}` on the ground state, where `τ` is measured
in the same physical blocked-time units as `a_blk`, with an explicit
finite-temperature excited-state-population correction; the decay length is
`1 / m_gap`.

What this step does **not** do: it does not establish unconditional
spatial cluster decomposition, and it does not supply a first-principles
derivation of `Δ_T > 0` for the full canonical staggered + Wilson `Cl(3) ⊗
Z^3` Hamiltonian. Those remain open and require a separate
spatial cluster-decomposition theorem plus an independently derived gap.
Within those limits, the conditional corollary recovers the temporal
ground-state correlation-length structure on the staggered-only
surface. ∎

## Hypothesis set used

The staggered-only surface of the minimal axiom setup via the four sector authorities
named in "Cited authorities". No imports from the forbidden list. The
load-bearing input is "`T := T_hat^2` positive Hermitian on a finite
`H_phys`"; everything downstream of it ((SC1), (SC2), and (SC3) under the
stated non-degeneracy condition) is elementary finite-dimensional spectral
theory on a bounded positive Hermitian operator, with the generator
normalized by the two-step blocked spacing `a_blk := 2 a_τ`. (SC4) additionally
conditions on the temporal bridge note and on the
gap `Δ_T > 0` of (SC3).

## Corollaries

C1. *Hamiltonian is self-adjoint and bounded below.* On the staggered-only
surface of the minimal axiom setup the ground-state-subtracted `H` on `H_phys` has only
non-negative eigenvalues. This is the lattice analogue of the Wightman
positive-energy axiom, conditional on the Step-1 transfer-positivity
input.

C2. *Mass-gap is the spectral-gap of `T`.* When the top eigenvalue is
non-degenerate (SC3), any package row that quotes a mass-gap value or
scaling can be related to the operator spectrum of the staggered-only
two-step transfer matrix via (1), using the two-step blocked time interval
`a_blk = 2 a_τ`.

C3. *Conditional temporal-clustering corollary.* Given the gap of (SC3),
the temporal bridge note + this note give exponential temporal
ground-state connected-correlator decay at rate `m_gap`. This is the
conditional temporal half of a lattice Wightman-axiom-pair; the
unconditional spatial cluster-decomposition half is **not** supplied here
(it needs a separate spatial cluster-decomposition theorem and
an independently derived gap).

## Honest status

**Source note; conditional scope.** (SC1)–(SC2) are proved on the
staggered-only surface of the minimal axiom setup given the Step-1 transfer-positivity
input from the four sector authorities; they are elementary finite-dimensional spectral theory
downstream of that input. (SC3) is conditional on a non-degenerate top
eigenvalue (exhibited on the finite carrier, not asserted in closed form
for every configuration). (SC4) is a corollary conditioned on (SC3)'s gap
and on the temporal bridge note; it is **not** an
unconditional cluster-decomposition import. The runner exhibits the
spectrum of `T`, the corresponding `H` spectrum, the gap, and confirms the
ground state has `E_0 = 0` after subtraction, on the free-staggered finite
surface. This note does not set or predict an audit outcome; the
independent audit lane owns any verdict.

**What changed in the 2026-05-30 rescope (and why it improves audit
readiness).** This rescope moves the load-bearing transfer-positivity
input from the broad umbrella row to the narrower in-repo two-step sector
(free + fixed-background, plus the two named factor notes), and (SC4) no
longer imports the full cluster-decomposition companion. It is rescoped to
a conditional temporal-decay corollary on the temporal bridge note. The
remaining open items are recorded
honestly above (Wilson extension, `U`-integrated full interacting closure,
unconditional spatial clustering, closed-form non-degeneracy / first-
principles gap).

**What changed in the 2026-06-06 blocked-time repair.** The theorem now
uses the same time spacing as its load-bearing transfer object:
`T := T_hat^2` advances two lattice time steps, so `H` and `m_gap` use
`1/(2 a_τ)`. The primary runner now constructs the two-step object
`T = exp(-2 a_τ H_lat)`, reconstructs `H` with `1/(2 a_τ)`, and checks
that the old `1/a_τ` normalization is exactly `2H`.

## Citations

- Minimal axiom setup: `docs/MINIMAL_AXIOMS_2026-04-11.md`
- staggered-only two-step transfer-positivity sector (load-bearing,
  markdown-linked under "Cited authorities"):
  `AXIOM_FIRST_RP_TWO_STEP_TRANSFER_MATRIX_POSITIVITY_NOTE_2026-05-28.md`,
  `RP_P2_GAUGE_EXTENSION_AND_REALIZATION_RESIDUAL_NOTE_2026-05-28.md`,
  `STAGGERED_ONLY_DET_POSITIVITY_CASE_A_NOTE_2026-05-17.md`,
  `REFLECTION_POSITIVITY_GAUGE_HALF_CAUCHY_SCHWARZ_NARROW_THEOREM_NOTE_2026-05-10.md`
- blocked-time normalization bridge for the `T_hat^2` factor of two:
  `AXIOM_FIRST_SPECTRUM_CONDITION_BLOCKED_TIME_NORMALIZATION_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`
- conditional temporal-decay bridge for (SC4) (markdown-linked in (SC4)):
  `CLUSTER_DECOMPOSITION_MASS_GAP_BRIDGE_THEOREM_NOTE_2026-05-09.md`
- context see-also (not load-bearing; plain text):
  `AXIOM_FIRST_REFLECTION_POSITIVITY_THEOREM_NOTE_2026-04-29.md` (umbrella
  row collecting the sector authorities plus the still-open `U`-integrated
  reduction target),
  `AXIOM_FIRST_CLUSTER_DECOMPOSITION_THEOREM_NOTE_2026-04-29.md` (full
  cluster-decomposition companion; not imported after the (SC4) rescope)

## Audit dependency repair links

This graph-bookkeeping section records explicit dependency notes so the
audit citation graph reflects the rescoped surface. It does not promote
this note or change the audited claim scope.

- The four staggered-only sector authorities and the (SC4) temporal bridge
  note are the load-bearing one-hop dependencies and are written as
  markdown links above so the citation-graph builder records them as
  upstream edges.
- The blocked-time normalization bridge is now a load-bearing one-hop
  dependency for the factor `1/(2 a_τ)` in `H` and `m_gap`. The primary
  runner and the companion bridge runner are both linked/cached:
  [`scripts/axiom_first_spectrum_condition_check.py`](../scripts/axiom_first_spectrum_condition_check.py),
  [`outputs/axiom_first_spectrum_condition_check_2026-04-29.txt`](../outputs/axiom_first_spectrum_condition_check_2026-04-29.txt),
  [`logs/runner-cache/axiom_first_spectrum_condition_check.txt`](../logs/runner-cache/axiom_first_spectrum_condition_check.txt),
  [`scripts/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.py`](../scripts/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.py),
  [`logs/runner-cache/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.txt`](../logs/runner-cache/audit_companion_spectrum_condition_blocked_time_normalization_2026_06_05.txt).
- `axiom_first_reflection_positivity_theorem_note_2026-04-29` and
  `axiom_first_cluster_decomposition_theorem_note_2026-04-29` are
  **context see-also only** after this rescope (backticked plain text, so
  the citation-graph builder does not parse them as upstream load-bearing
  edges): the umbrella row's `U`-integrated full interacting `SU(3)` claim
  and the full cluster-decomposition theorem are no longer premises of
  (SC1)–(SC4) as rescoped here.
