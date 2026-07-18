# Koide Q-readout Probe 16 — Functional-Level Pivot, Sharpened Bounded Obstruction

**Date:** 2026-05-09
**Type:** bounded_theorem
**Scope:** review-loop source-note proposal — historical Probe 16 of the Koide
Frobenius-equipartition closure campaign (legacy alias: A1-condition).
It pivots from algebra-level closure
(Probes 1-14) to a **conditional Q-functional / Koide-readout probe**, under
the explicitly supplied and unretained hypothesis `λ_k = √m_k >= 0`, on the
nonzero-denominator domain `a != 0`. Under that hypothesis, the
Brannen Koide ratio `Q = Σm_k / (Σ√m_k)²` reduces to
`Q(a, |b|) = (a² + 2|b|²)/(3a²)` and is **U(1)_b-invariant by
construction** (depends only on `|b|²/a²`, not on `arg(b)`).
**Status:** source-note proposal for a **sharpened** bounded obstruction.
This conditional calculation does not derive P1, a charged-lepton carrier, or
a physical selector. The conditional Q expression is U(1)_b-invariant and can
therefore be written on the orbit coordinates `(a,|b|)`. This invariance does
not itself supply a quotient, Haar average, or physical readout. Even after a
stipulated Haar angular average, **the Frobenius-equipartition condition does
not follow**: an unconstrained continuous family of functional/weight choices
remains. This repair adds no premise and changes no premise registry.
**Authority role:** source-note proposal — audit verdict and
downstream status set only by the independent audit lane.
**Loop:** koide-a1-probe16-q-readout-functional-20260509
**Primary runner:** [`scripts/cl3_koide_a1_probe_q_readout_functional_2026_05_09_probe16.py`](../scripts/cl3_koide_a1_probe_q_readout_functional_2026_05_09_probe16.py)
**Cache:** [`logs/runner-cache/cl3_koide_a1_probe_q_readout_functional_2026_05_09_probe16.txt`](../logs/runner-cache/cl3_koide_a1_probe_q_readout_functional_2026_05_09_probe16.txt)

## Authority disclaimer

This is a source-note proposal. Pipeline-derived status is generated
only after the independent audit lane reviews the claim, dependency
chain, and runner. The claim type, scope, supplied/open premises, and
bounded-obstruction classification are author-proposed; the audit
lane has full authority to retag, narrow, or reject the proposal.

## Current naming and historical alias

The current framework baseline uses the named **Lattice**, **Qubit**,
**Admissibility**, and **Record** axioms. The historical phrase "framework
axiom A1" is obsolete. In this note, the legacy alias "A1-condition" refers
only to the Koide Frobenius-equipartition condition
`|b|²/a² = 1/2` (on `a != 0`) for the supplied abstract circulant
`H = aI + bC + b̄C²`; the explicit name is used for the live claim.

## Pivot motivation

All 14 prior probes attacked closure at the **algebra level** —
identifying an operator-level mechanism that fixes `(a, |b|)` such
that `|b|²/a² = 1/2`. Probe 13 (real-structure / antilinear
involution) and Probe 14 (retained-U(1) hunt) sharpened the missing
primitive to:

> "The canonical SO(2) phase quotient on the non-trivial doublet of
> A^{C_3} = the U(1)_b symmetry of the Brannen δ-readout."

This is a **continuous** symmetry, qualitatively different in kind
from any retained algebra symmetry. Probe 14 ruled out 9 retained
U(1) candidates; none projects to U(1)_b on the b-doublet.

Probe 13 §"Honest assessment" listed three options:

> 3. **Pivot to the SO(2)-quotient at the readout level (functional,
>    not algebraic).** The Brannen Q-functional IS U(1)_b-invariant
>    (Q depends only on `|b|²/a²`, not arg(b)). So the SO(2)-quotient
>    could be enforced AT THE Q-READOUT STEP, not at the algebra
>    level.

This probe takes that option. The hypothesis is: **at the Q-readout
level, the conditional Q formula is U(1)_b-invariant**. A separate Haar
angular average will be stipulated below as a projection; it is not derived as
the physical quotient. The question becomes: does the cited content force
`Q = 2/3` for the abstract spectral vector at the readout level?

## Phase 1 — Q-functional U(1)_b-invariance under an explicit P1 hypothesis

For this probe only, suppose the unsupplied physical hypothesis

```text
v_k = √m_k = λ_k >= 0,       a != 0
```

is imposed after choosing a circulant. The abstract theorem
[`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
proves the finite Fourier identities for a defined eigenvalue triple, but it
does not supply this P1 mass assignment or a physical carrier. Conditional on
the displayed probe hypothesis:

```text
v_k = √m_k = λ_k >= 0     (eigenvalues of H = aI + bC + b̄C² on hw=1), a != 0
```

so `λ_k = a + 2|b|cos(arg(b) + 2πk/3)`. Then:

```text
Σ √m_k    =  Σ λ_k     =  Tr(H)         =  3a
Σ m_k     =  Σ λ_k²    =  ‖H‖_F²        =  3a² + 6|b|²
Q         =  Σm_k/(Σ√m_k)²              =  (a² + 2|b|²)/(3a²)
```

Both numerator and denominator depend on `(a, |b|²)` only, hence:

```text
Q(a, b) = Q(a, |b|) ;     Q is U(1)_b-invariant on Herm_circ(3).
```

Equivalently: the **Brannen square-root mass carrier** `√m_k = V₀(1 +
c·cos(δ + 2πk/3))` (per [`KOIDE_Q_SO2_PHASE_ERASURE_SUPPORT_NOTE_2026-04-25.md`](KOIDE_Q_SO2_PHASE_ERASURE_SUPPORT_NOTE_2026-04-25.md))
is the same parameterization with `V₀ = a`, `c = 2|b|/a`, `δ = arg(b)`,
and `Q = (c² + 2)/6 = (a² + 2|b|²)/(3a²)`.

**Consequence**: `Q = 2/3 ⇔ a² = 2|b|² ⇔ |b|²/a² = 1/2 = A1`.

## Phase 2 — What a stipulated Haar angular average changes

The Q-functional is invariant. Separately, stipulate the normalized Haar
average over `arg(b)` as a projection of candidate functions on
`Herm_circ(3)`. On the resulting invariant `(a,|b|)` coordinates:

| Functional | U(1)_b-invariant? | Result after stipulated averaging |
|---|---|---|
| `Tr(H) = 3a` | ✓ | yes |
| `Tr(H²) = ‖H‖_F² = 3a² + 6|b|²` | ✓ | yes |
| `E_+(H) = ‖π_+(H)‖_F² = 3a²` | ✓ | yes |
| `E_⊥(H) = ‖π_⊥(H)‖_F² = 6|b|²` | ✓ | yes |
| `Tr(H³)` (carries `cos(3 arg b)`) | ✗ | erased after averaging |
| `det(H) = a³ - 3a|b|² + 2|b|³ cos(3 arg b)` | ✗ | erased after averaging |
| `log|det(H)|` (carries `cos(3 arg b)`) | ✗ | erased after averaging |

**Finding**: the phase-dependent **det-carrier law `log|det|`** is not
U(1)_b-invariant. The stipulated angular projection replaces it by an
invariant averaged candidate; this is a supplied projection, not evidence that
the physical framework eliminates the original carrier law.

The exact new content is limited to the conditional Q-invariance and the
computed behavior of several explicitly chosen projected functionals.

## Phase 3 — The remaining residue at the functional level

After the stipulated angular projection, multiple extremization functionals
remain on the `(a,|b|)` plane. We tested three representatives; weighted
block-log laws already form a continuous `mu/nu` family:

### Functional F1: Block-total Frobenius equipartition

```text
S_block(a, |b|) = log E_+ + log E_⊥ = log(3a²) + log(6|b|²)
                = log 3 + log 6 + 2 log a + 2 log |b|
```

Constraint: `E_+ + E_⊥ = 3a² + 6|b|² = const`.
Lagrange extremum: `1/E_+ = 1/E_⊥ → E_+ = E_⊥ → a² = 2|b|² → κ = 2 = A1`. ✓

This is the (1,1)-multiplicity-weighted Frobenius pairing identified
by the campaign synthesis as the missing primitive, realized
explicitly by the cited block-total Frobenius source proposal (see
[`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)).

### Functional F2: Angular-averaged log-det

```text
⟨det(H)²⟩_arg(b) = a⁶ - 6a⁴|b|² + 9a²|b|⁴ + 2|b|⁶
S_avgdet(a, |b|) = log ⟨det²⟩
```

Constraint: `E_+ + E_⊥ = const`.
The exact fixed-energy reduction, including both stationary points and the
endpoints, gives its global maximum at the boundary `|b| = 0`; the ratio
`κ=a²/|b|²` is undefined at that boundary (and diverges only as a
one-sided interior limit), so this point is **NOT** A1. ✗

### Functional F3: Standard log|det|² extremum on (a², |b|²)-plane (rank-weighted)

The `(1,2)` weighting is supplied here as a separate invariant rank-weighted
candidate. It is not derived by, or said to survive, a physical quotient:

```text
S_rank(a, |b|) = log a² + 2 log |b|²    (1:2 multiplicity from rank P_+ = 1, P_⊥ = 2)
```

Constraint: `E_+ + E_⊥ = const`.
Lagrange extremum: `1/a² · 2a = 2λ · 6a` and `2/|b|² · |b| = 2λ · 12|b|`
→ `E_+ = (1/3) E_total`, `E_⊥ = (2/3) E_total` → `κ = 1`, NOT A1. ✗

**Verdict on the tested functionals**: of F1, F2, and F3, only F1
(block-total Frobenius equal weight) lands at A1. F2 and F3 do not. No
exhaustive uniqueness claim over all invariant functionals is made.

## Phase 4 — The sharpened residue

The stipulated Haar projection removes angular dependence from the candidates
to which it is applied. The remaining issue is **the choice of extremization
functional** on the `(a,|b|)` plane; the cited content does not select a member
of the continuous functional/weight family.

The cited source-stack content currently provides:

- `KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM` — exact source-side
  algebra, current ledger status unaudited. It exhibits F1 with the `d = 3`
  one-trivial-plus-one-doublet pattern and the (1,1)
  multiplicity reading from Frobenius reciprocity.
- The MRU demotion note explicitly flags that the (1,1) weighting
  vs (1,2) weighting choice is **not pinned by cited source-stack content**;
  it is "minor and equivalent in scale to MRU-as-observable-principle".
- No cited matter-sector dynamics extremizes `log E_+ + log E_⊥`
  at the physical point (`V(m)` minimum is `m_V ≈ -0.433`, NOT
  the physical `m_* ≈ -1.161` per
  [`KOIDE_Z3_SCALAR_POTENTIAL_LEPTON_MASS_TOWER_NOTE_2026-04-19.md`](KOIDE_Z3_SCALAR_POTENTIAL_LEPTON_MASS_TOWER_NOTE_2026-04-19.md)
  §5).

**Sharpened residue at functional level**:

> "The physical extremization functional on the invariant `(a,|b|)`
> coordinates — selecting `F1 = log E_+ + log E_⊥` (block-total
> Frobenius, (1,1)-multiplicity weighting) over admissible competitors
> `F2 = log⟨det²⟩` (angular-averaged) and `F3 = log E_+ + 2 log E_⊥`
> (rank-weighted) — that lands the extremum at A1 (κ=2)."

This is a different framing of the still-open selection problem, not a claim
that the residual wall is strictly smaller:

- Probe 13/14 residue: "U(1)_b angular quotient on the b-doublet" — a
  **continuous** Lie-algebra-1 extension of retained discrete C_3.
- Probe 16 residue: "(1,1) multiplicity weighting selection on the
  invariant `(a,|b|)` plane" — an unconstrained continuous
  functional/weight choice, illustrated by three representatives.

The functional pivot exposes an invariant coordinate description, but it does
not retire the continuous choice of functional/weights and does not close A1.

## Phase 5 — Honest scope: does the polynomial cone identity propagate to closure?

The retained `KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM`
(positive_theorem) gives the polynomial identity:

```text
3(u² + v² + w²) = 2(u + v + w)²    (cone identity)
  ⇔  Q = 2/3
  ⇔  4(uv + uw + vw) - (u² + v² + w²) = 0
```

for any positive triple `(u, v, w) ∈ R³`. This is **purely polynomial**;
the (u, v, w) are abstract coordinates. The cited
`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE` extends the
identity to the C_3-Plancherel components: `Q = 2/3 ⇔ a₀² = 2|z|²`.

**The propagation question**: does an abstract spectral vector lie on the
cone, and—under the explicitly unretained P1 hypothesis—may it be identified
with `v = (√m_e, √m_μ, √m_τ)`?

- **At algebra level (Probes 1-14)**: the closure target is "derive
  `|b|²/a² = 1/2` from cited source-stack content". Result: those named
  probes did not supply the selector; no exhaustive no-go is inferred here.
- **At functional level (this probe)**: the closure target is "derive
  the (1,1)-multiplicity-weighting extremum convention from cited content".
  Result: the tested candidates do not select it; the functional-choice layer
  remains.

In **both** framings, the polynomial cone identity is the right
backbone but is **not load-bearing on closure**. It tells us that
"if `(a, |b|)` lies at A1, then `(λ_0, λ_1, λ_2)` lies on the cone
and Q = 2/3", but it does not tell us **why** the framework selects
A1.

## Setup

### Premises (A_min for probe 16)

| ID | Statement | Class |
|---|---|---|
| Qubit | `M_2(C)` / `Cl(3,0)` local algebraic presentation | framework context; see `MINIMAL_AXIOMS_2026-06-29.md`; not load-bearing in the finite circulant calculation |
| Lattice | `Z³` nearest-neighbour substrate | framework context; same source; not load-bearing in the finite circulant calculation |
| BZ | hw=1 BZ-corner triplet ≅ `ℂ³` with `C_3[111]` action | source dependency; see [`STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md`](STAGGERED_DIRAC_BZ_CORNER_FORCING_THEOREM_NOTE_2026-05-07.md) |
| 3GenObs | hw=1 carries `M_3(ℂ)` algebra; no proper exact quotient | source dependency; see [`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md) |
| Circulant | `C_3`-equivariant Hermitian on hw=1 is `aI + bC + b̄C²` | source dependency; see [`KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md`](KOIDE_CIRCULANT_CHARACTER_DERIVATION_NOTE_2026-04-18.md) R1 |
| BlockTotalFrob | `E_+ = 3a²`, `E_⊥ = 6|b|²` on `Herm_circ(3)` | source dependency; see [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md) |
| ConeAlg | Koide `Q = 2/3 ⟺ a₀² = 2\|z\|² ⟺ \|b\|²/a² = 1/2` | source dependency; see [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md) |
| ConePoly | Polynomial cone three-form equivalence | source dependency; see [`KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md) |
| P1 | `λ_k = √m_k` (P1 square-root identification) | unsupplied physical probe hypothesis; [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md) supplies only the abstract Fourier algebra and explicitly does not authorize P1 or a physical carrier |
| BrannenSO2 | `Q = (c²+2)/6` U(1)_b-invariant on Brannen carrier | source dependency; see [`KOIDE_Q_SO2_PHASE_ERASURE_SUPPORT_NOTE_2026-04-25.md`](KOIDE_Q_SO2_PHASE_ERASURE_SUPPORT_NOTE_2026-04-25.md) |
| Probe13 | Algebra-level residue: U(1)_b SO(2) phase quotient on b-doublet | source dependency; see [`KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md`](KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md) |
| Probe14 | No retained U(1) projects onto U(1)_b on b-doublet | source dependency; see [`KOIDE_A1_PROBE_RETAINED_U1_HUNT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe14.md`](KOIDE_A1_PROBE_RETAINED_U1_HUNT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe14.md) |

### Forbidden imports

- NO PDG observed mass values used as derivation input (per
  [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md))
- NO lattice MC empirical measurements
- NO fitted matching coefficients
- NO new premise, axiom, or registry entry added by this probe
- NO **import of empirical Koide match Q ≈ 2/3 as derivation input**
  (this would be the substep-4 AC narrowing rule violation; instead
  this probe operates entirely in the algebra-form `Q(a, |b|) =
  (a² + 2|b|²)/(3a²)` without instantiating numerical Q values)

## Theorem (Probe 16 sharpened functional-level bounded obstruction)

**Theorem.** Given the explicitly supplied cited `C_3`,
`M_3(ℂ)`, Hermitian-circulant, block-total, cone-equivalence, polynomial,
and Brannen-SO(2) source statements—and conditional on the separately
supplied, unretained P1 probe hypothesis:

```
(a) Conditional Q-functional U(1)_b-invariance (exact abstract algebra).
    Under P1, Q(a, b) = (a² + 2|b|²)/(3a²) depends only on (a, |b|),
    not arg(b). This is conditional on the unretained P1 hypothesis and does
    not supply a physical quotient or readout.

(b) Det-carrier behavior under a stipulated Haar angular average.
    log|det(H)| carries the U(1)_b-non-invariant cos(3 arg b) term.
    Under the explicitly supplied angular average over arg(b) ∈ [0, 2π),
    ⟨det(H)⟩ = a(a² - 3|b|²) and ⟨det²⟩ = a^6 - 6a^4|b|² + 9a²|b|^4
    + 2|b|^6. The angular-averaged det-carrier extremum lands at the
    boundary |b|=0, where κ is undefined, NOT at A1.

(c) Block-total Frobenius equipartition is one exact extremum candidate
    at functional level (not a physical selector or closure).
    log E_+ + log E_⊥ at fixed E_+ + E_⊥ = const has its
    Lagrange extremum exactly at E_+ = E_⊥ ⇔ a² = 2|b|² ⇔ A1.
    F1 lands at A1.

(d) Functional-choice ambiguity persists at functional level.
    Multiple invariant functionals on the `(a,|b|)` plane are possible:
    - F1 = log E_+ + log E_⊥ (block-total Frobenius, (1,1)-mult)
      → extremum at A1 (κ=2).
    - F2 = log⟨det²⟩ (angular-averaged squared determinant)
      → extremum at |b|=0 boundary, where κ is undefined, NOT A1.
    - F3 = log E_+ + 2 log E_⊥ (rank-weighted, (1,2)-mult)
      → extremum at κ=1, NOT A1.
    More generally the weighted block-log family varies continuously with
    `mu/nu`; no cited extremization principle pins F1 over that family.

Therefore the supplied angular projection removes phase dependence from the
projected candidates, but **does not derive the Koide
Frobenius-equipartition condition**. The residue is
an unconstrained continuous functional/weight choice on `(a,|b|)`, together
with the still-unretained physical carrier/readout hypothesis.

No new premise, axiom, or registry entry is proposed by this probe.
```

**Proof.** (a) Direct algebraic computation of Q under P1 (runner
Sections 2-3). (b) Direct symbolic computation of det(H) showing the
`cos(3 arg b)` dependence (runner Sections 4.1-4.4). (c) Explicit
Lagrange extremum on F1 (runner Sections 5.1-5.4). (d) Explicit
Lagrange/numerical extrema on F2 and F3 with verification that they
land away from A1 (runner Sections 5.5-5.8). ∎

## Phase 6 — Honest assessment

### Does the functional-level pivot actually work?

**As an exact conditional calculation, but not as a closure.** The Q formula
respects U(1)_b under the unretained P1 hypothesis. Applying a Haar angular
average to other candidates is an explicitly supplied projection, not a
framework-derived physical quotient.

But it does **not close A1**. The substantive question — "what
forces `Q = 2/3`?" — moves from "what fixes `(a, |b|)` such that
`|b|²/a² = 1/2` at algebra level" to "what selects the (1,1)-
multiplicity extremum convention F1 over the continuous family of possible
weights/functionals on invariant coordinates". The substantive content of
the residue is not eliminated.

### Did the retained Koide-cone polynomial identity propagate cleanly to closure?

**No.** The polynomial identity (`KOIDE_CONE_THREE_FORM_EQUIVALENCE`)
provides the **algebraic backbone** linking `Q = 2/3` to `|b|²/a² =
1/2` to the cone equation `3(u² + v² + w²) = 2(u + v + w)²`, but
all three forms are algebraically equivalent on the supplied domain. The
question of whether an abstract spectral vector may be physically identified
with a charged-lepton √m-vector and
**lies on** the cone is not closed by the polynomial identity alone;
that would require an independent forcing principle that selects A1
over the continuum of off-cone (a, |b|) pairs.

The retained polynomial cone three-form equivalence is purely
polynomial algebra over abstract `(u, v, w) ∈ R³`. It does **not**
identify `(u, v, w)` with charged-lepton √m amplitudes (per the note's
own `## What this does NOT claim` section). Identifying `(u, v, w) =
(√m_e, √m_μ, √m_τ)` and forcing the cone is precisely the A1
open selector condition this campaign is trying to derive.

### What specifically blocks the functional-level approach?

The block is the **functional-choice convention**. On invariant `(a,|b|)`
coordinates there is a continuous family of possible functionals/weights;
three tested representatives are:

1. **F1** (block-total Frobenius, (1,1)-multiplicity): lands at A1.
2. **F2** (angular-averaged det): lands at boundary, NOT A1.
3. **F3** (rank-weighted, (1,2)-multiplicity): lands at κ=1, NOT A1.

The cited `KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM` is a source
proposal with current ledger status unaudited, and the canonicality of F1 is
not established; this is exactly
what the campaign synthesis flagged as the missing primitive.

The cited `KOIDE_MRU_DEMOTION_NOTE` explicitly says the (1,1) vs
(1,2) choice is "minor and equivalent in scale to MRU-as-observable-
principle" but **not derivable from cited source-stack content alone**. This
probe verifies that the same kind of choice persists at the functional
level, in modified form — the (1,1)-multiplicity vs angular-averaged-
det convention.

### Critical circularity check

**Does this probe smuggle in the empirical Q ≈ 2/3 match?**

No. The probe operates entirely on the algebraic Q-functional `Q(a,
|b|) = (a² + 2|b|²)/(3a²)` without instantiating numerical PDG mass
values. The runner verifies:

- F1 extremum at `a² = 2|b|²` (algebraic, no PDG input).
- F2, F3 extrema at boundaries / `κ = 1` respectively (algebraic).

The cited PDG numerical realization (`PDG E_+/E_⊥ ≈ 1.000018` per
the block-total Frobenius theorem §5.2) is an **audit-comparator
observation only**, never load-bearing on the in-scope content. It
appears in the block-total source note for falsification
purposes but is not used here as a derivation input.

This satisfies the substep-4 AC narrowing rule.

## Convention-robustness check

- **Scale-invariance** of `|b|²/a²` is preserved under `H → cH`. ✓
- **Basis change** `C → C^{-1} = C²` preserves C_3-action and isotype
  structure. ✓
- **U(1)_b-invariance** of the conditional Q expression is
  convention-independent once the unretained P1 probe hypothesis is supplied. ✓

The invariant coordinates `(a,|b|)` are exact. Neither a physical quotient nor
the physical extremization functional on those coordinates is pinned by the
cited content.

## Attack-vector enumeration

This is the sixteenth attack vector in the campaign:

| # | Attack vector | Outcome |
|---|---|---|
| 16 | Q-functional / Koide-readout level pivot | conditional invariant formula plus supplied Haar projection; continuous functional/weight choice and physical readout remain open |

This refines the residue from Probe 13/14:

- **Probe 13/14 residue**: U(1)_b angular quotient on b-doublet
  (continuous Lie-algebra-1 extension).
- **Probe 16 residue**: continuous functional/weight choice on the
  `(a,|b|)` plane, illustrated by block-total Frobenius,
  angular-averaged determinant, and rank-weighted representatives.

The calculation sharpens the exact behavior of named candidates but does not
turn the continuous selection problem into a discrete one, and A1 is not
closed.

## Status block

### Author proposes (audit lane decides):

- `claim_type`: `bounded_theorem` (sharpened obstruction; no closure)
- audit-derived effective status: set only by the independent audit lane after review
- `open_conditions`: `["Koide Frobenius-equipartition:
  |b|²/a² = 1/2 on a != 0"]` — the unresolved condition, with the Probe 16
  sharpening:
  "the physical extremization functional on invariant `(a,|b|)` coordinates
   — block-total Frobenius (1,1)-multiplicity over
   angular-averaged det or rank-weighted competitors — that lands the
   extremum at A1 (κ=2)"

**No new premise or registry entry is added by this probe.**

### What this probe DOES

1. Verifies that under the explicitly supplied, unretained P1 probe
   hypothesis `λ_k = √m_k`, the
   Brannen Koide ratio `Q(a, b) = (a² + 2|b|²)/(3a²)` is U(1)_b-
   invariant by construction.
2. Verifies that the phase-dependent **det-carrier law** is not
   U(1)_b-invariant and computes what a stipulated Haar angular projection
   does to its squared form.
3. Verifies that the block-total Frobenius equipartition F1 = log E_+
   + log E_⊥ has its Lagrange extremum at A1 (κ=2) on the (a, |b|)-
   plane.
4. Verifies that admissible competitors F2 (angular-averaged det)
   and F3 (rank-weighted) land **away** from A1.
5. Localizes the residual selection to a continuous family of invariant
   functional/weight choices, without deriving a physical quotient.

### What this probe DOES NOT do

1. Does NOT close the A1-condition.
2. Does NOT add any new axiom, premise, or registry entry.
3. Does NOT modify any cited source statement (BZ, 3GenObs, Circulant,
   BlockTotalFrob, ConeAlg, ConePoly, BrannenSO2, Probe13, or Probe14),
   and does not promote P1 into a retained premise.
4. Does NOT promote any downstream theorem; the block-total Frobenius row's
   current ledger status remains unaudited.
5. Does NOT load-bear PDG values into a derivation step.
6. Does NOT modify the audit-honest options enumerated by the
   eleven-probe campaign synthesis (supply/derive/pivot).

## Strategic options remaining

This probe **does not select** an option. Three options remain after
16 probes:

1. **Continue derivation hunt**. The residue is now precisely
   characterized at functional level: a continuous functional/weight
   selection problem. A future probe might find a derivation of
   F1 canonicality from cited source-stack content (e.g., max-entropy
   principle on isotypic decomposition, Gibbs-state argument, or a
   variational principle internal to retained `Cl(3)` structure).

2. **Supply the (1,1)-multiplicity functional convention**. A future
   premise could state: "the physical extremization
   functional on invariant `(a,|b|)` coordinates is the
   block-total Frobenius (1,1)-multiplicity-weighted log-law." Under
   such a premise, the Koide Frobenius-equipartition condition follows
   immediately. This note does not supply that premise.

3. **Pivot to other bridge work**. The Koide Frobenius-equipartition
   condition is one named target among multiple open bridge gaps. The audit lane and
   the user may classify A1 as a parameter/readout target and
   prioritize independent bridge work over A1-closure attempts.

## Honest note on the polynomial identity

The retained `KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM` is
positive_theorem and provides the polynomial backbone:

- `(F_orbit)`: `4(uv + uw + vw) - (u² + v² + w²) = 0`
- `(F_ratio)`: `(u² + v² + w²)/(u + v + w)² = 2/3`
- `(F_cyclic)`: `2 r₀² = r₁² + r₂²` (in cyclic basis)

These are equivalent for any abstract (u, v, w). The probe verifies
that under the supplied, unretained P1 probe hypothesis
(`v_k = √m_k = λ_k >= 0`, `a != 0`, and `λ_k = a +`
2|b|cos(arg(b) + 2πk/3)), the (F_ratio) form gives `Q = (a² +
2|b|²)/(3a²)`. The polynomial identity is
correctly applied; it does not, by itself, force A1.

The functional-level pivot's contribution is to make conditional
U(1)_b-invariance manifest and to compute three named candidates after a
supplied Haar projection. It does not clear the physical quotient/readout
wall; the continuous functional/weight choice also remains.

## Cross-references

### Foundational baseline

- Minimal axioms: `MINIMAL_AXIOMS_2026-06-29.md`
- Substep-4 AC narrowing: [`STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md`](STAGGERED_DIRAC_SUBSTEP4_AC_NARROW_BOUNDED_NOTE_2026-05-07_substep4ac.md)

### Retained polynomial Koide-cone identities

- Three-form equivalence: [`KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md`](KOIDE_CONE_THREE_FORM_EQUIVALENCE_NARROW_THEOREM_NOTE_2026-05-02.md)
- Completing-root narrow: [`KOIDE_CONE_COMPLETING_ROOT_NARROW_THEOREM_NOTE_2026-05-02.md`](KOIDE_CONE_COMPLETING_ROOT_NARROW_THEOREM_NOTE_2026-05-02.md)
- Algebraic equivalence: [`CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md`](CHARGED_LEPTON_KOIDE_CONE_ALGEBRAIC_EQUIVALENCE_NOTE.md)

### Abstract Fourier identity and open P1 identification

- Abstract Hermitian-circulant Fourier invariant (no mass/P1/carrier
  authority):
  [`KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_SPECTRUM_OPERATOR_BRIDGE_THEOREM_NOTE_2026-04-19.md)
- Block-total Frobenius (source proposal; current ledger unaudited): [`KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md`](KOIDE_KAPPA_BLOCK_TOTAL_FROBENIUS_MEASURE_THEOREM_NOTE_2026-04-19.md)
- MRU demotion (functional-choice convention status): [`KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md`](KOIDE_MRU_DEMOTION_NOTE_2026-04-20.md)

### Brannen-carrier U(1)_b-erasure context

- Brannen Q SO(2) phase erasure: [`KOIDE_Q_SO2_PHASE_ERASURE_SUPPORT_NOTE_2026-04-25.md`](KOIDE_Q_SO2_PHASE_ERASURE_SUPPORT_NOTE_2026-04-25.md)
- Q readout quotient (context only): [`KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md`](KOIDE_Q_READOUT_FACTORIZATION_THEOREM_2026-04-22.md)
- Brannen phase reduction: [`KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md`](KOIDE_BRANNEN_PHASE_REDUCTION_THEOREM_NOTE_2026-04-20.md)

The Q-readout note proves kernel invariance only for the definitionally selected
class `S_L={Phi composed with L}`. Locality, bosonic/even parity, species
resolution, first-live rhetoric, and `C_3` covariance have not been shown to
classify all selectors into `S_L`; `S_z(u,v,w,z)=z` is a `C_3`-invariant,
kernel-sensitive counterexample. The row supplies no Brannen carrier, physical
charged-lepton selector, `Q` functional, normalization, mass spectrum, source
law, comparator, or delta bridge.

### Sister Koide-A1 probes

- Probe 13 (real-structure / antilinear involution): [`KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md`](KOIDE_A1_PROBE_REAL_STRUCTURE_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe13.md) — sharpened residue: U(1)_b angular quotient
- Probe 14 (retained-U(1) hunt) — see [`KOIDE_A1_PROBE_RETAINED_U1_HUNT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe14.md`](KOIDE_A1_PROBE_RETAINED_U1_HUNT_BOUNDED_OBSTRUCTION_NOTE_2026-05-09_probe14.md)

### Eleven-probe campaign baseline

- Synthesis (campaign terminal state, pre-Probe 12): [`KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md`](KOIDE_A1_11_PROBE_CAMPAIGN_BOUNDED_ADMISSION_META_NOTE_2026-05-08.md)

## Validation

```bash
python3 scripts/cl3_koide_a1_probe_q_readout_functional_2026_05_09_probe16.py
```

Expected: `SCORECARD ALGEBRA_PASS=13 ALGEBRA_FAIL=0 CONDITIONAL_PASS=19
CONDITIONAL_FAIL=0`, followed by `=== TOTAL: PASS=32, FAIL=0 ===`.

The runner verifies:

1. Supplied finite-algebra inputs (Section 1): C unitary, order 3, eigenvalues
   `{1, ω, ω̄}`; H = aI + bC + b̄C² is Hermitian and circulant.
2. Conditional algebra after explicitly supplying the unretained P1 probe
   hypothesis `λ_k = √m_k` (Section 2); the abstract Fourier theorem does not
   supply that hypothesis.
3. Q-functional under P1: Q(a, b) = (a² + 2|b|²)/(3a²) is U(1)_b-
   invariant (Section 3).
4. Det carrier carries cos(3 arg b) and is NOT U(1)_b-invariant
   (Section 4).
5. Block-total Frobenius F1 extremum at A1 (Section 5.1).
6. Angular-averaged det F2 extremum at boundary, NOT A1 (Section 5.2).
7. Rank-weighted F3 extremum at κ=1, NOT A1 (Section 5.3).
8. Functional-choice ambiguity verified explicitly (Section 6).
9. No PDG numerical input is load-bearing (Section 7).
10. Polynomial cone identity applied correctly under P1 (Section 8).
11. Convention-robustness checks (Section 9).
12. Verdict: SHARPENED bounded obstruction; no premise or registry change
    (Section 10).
