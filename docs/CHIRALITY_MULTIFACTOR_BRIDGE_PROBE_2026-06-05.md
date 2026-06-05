# Chirality Multi-Factor Bridge Probe — native Cl(3) joint grading does not transport onto the generation factor

**Date:** 2026-06-05
**Type:** meta
**Claim type:** meta
**Status:** negative-route probe record (PT-C wall, native variant). Source-note
proposal; pipeline-derived status set only after independent audit review. No
theorem promotion, no new axiom, no import.
**Runner:** [`scripts/chirality_multifactor_bridge_probe_2026_06_05.py`](../scripts/chirality_multifactor_bridge_probe_2026_06_05.py) (SCORECARD 15/15 PASS)
**Cached output:** [`logs/runner-cache/chirality_multifactor_bridge_probe_2026_06_05.txt`](../logs/runner-cache/chirality_multifactor_bridge_probe_2026_06_05.txt)

## Question

`r = |b|²/a² = 1/2` (Koide `Q=2/3`) needs a Hermitian grading `Γ_χ = (2/3)J − I`
that **anticommutes** with the mass operator on the **generation** `R³` factor
(retained `koide_anticommuting_operator_derivation`). The retained_bounded no-go
`koide_z3_equivariant_anticommuting_no_go` blocks this only for `C₃`-equivariant
operators on a single `R³`, and its **§4 escape-hatch (II)** explicitly leaves
open the multi-factor case where the chiral grading lives in a tensor factor
**distinct** from where `Γ_χ` acts.

A prior test (PT-C / `flavor_emergent_chirality_no_transport_note_2026-05-30`,
audited_conditional) closed escape-hatch (II) for the **spacetime / Connes-Lott**
grading `γ_CL = I₃ ⊗ σ₃`: that grading is **inert** on the generation factor
(`{G ⊗ σ₁, I₃ ⊗ σ₃} = 0` for *every* `G`), so it imposes zero constraint on the
generation operator.

**This probe asks the genuinely distinct question PT-C did not:** A2 supplies each
site the algebra `Cl(3,0) ≅ M₂(C)` with a **native** chirality source — the Cl(3)
volume element / even-odd grading — distinct from any imported spacetime `γ₅`. The
generations are the `hw=1` BZ-corner orbit, a lattice structure. Does a
**multi-factor operator on `(on-site Cl(3) qubit) ⊗ (generation R³)`**, with the
chiral grading built from the **native on-site Cl(3) grading coupled to the
generation index through the staggered/lattice geometry** (where `taste-C₃ =
generation-C₃` is locked), induce a genuine **off-block generation grading** after
the physical `hw=1` species reduction — or collapse to the on-block requirement
(`Q=1`), as PT-C found for the spacetime `γ_CL`?

## Verdict

**COLLAPSES-TO-ON-BLOCK (PT-C wall) — native Cl(3) variant.** The native on-site
Cl(3) source does **not** transport across the tensor factor onto the generation
triplet. There is **no off-block generation grading and no `Q=2/3`**. The collapse
happens through two independent mechanisms, and the strongest available adversary
(off-diagonal corner coupling) also collapses.

This is a **negative result** that **sharpens** PT-C: escape-hatch (II) is now
closed for the framework's *native* chirality source, not only the imported
spacetime one. It is a route-pruning, **not** a global no-go — see the residuals.

## What the runner establishes (15/15 exact checks)

**[1] The native Cl(3) grading is a central scalar — there is no on-site grading to
transport.** The volume element `ω = γ₁γ₂γ₃ = σ₁σ₂σ₃ = i·I₂` is **central** at odd
`n=3` (retained `clifford_volume_chirality_even_dimension`). No on-site bivector
anticommutes with all three generators — each `σ_jσ_k` misses `σ_j` and `σ_k`'s
third partner (consistent with retained_no_go `no_per_site_chirality_theorem`). So
the only candidate on-site gradings are the generators `σ_a` themselves (each a
*partial* grading), not the Cl(3) chirality `ω`.

**[2] The lattice coupling is real and exact.** The axis rotation `U(123)`
(`σ₁→σ₂→σ₃`) restricted to `hw=1` equals the generation cyclic shift `R`
(`taste-C₃ = generation-C₃`, the staggered lock). And the staggered free-Dirac
symbol `sin(k_μ)=0` at every corner momentum `k_μ∈{0,π}`, so `hw=1` is a **kinetic
zero-locus**: no chiral grading is supplied by the kinetic Dirac there (context:
2026-06-04 `corner_fermion_determinant`, `staggered_taste_is_qubit`, both
`unaudited`).

**[3] The joint grading is block-diagonal in generation.** Building the joint
grading `Γ_J = Σ_μ g_μ ⊗ Π_μ` (native on-site bivector `g_μ` coupled to the corner
projector `Π_μ`), its physical reduction to `(qubit)⊗(gen)` is **block-diagonal in
generation**: every off-diagonal entry links *different qubit states at the same
generation corner*, never different generations. Its partial trace over the qubit —
the pure generation operator — is **exactly zero**.

**[4] Inert lemma (the structural core, PT-C reproven natively).** For any
`D = A ⊗ X` (on-site `A`, generation `X`) and grading `Γ = γ_q ⊗ Γ_g`:

```
   tr_qubit{D, Γ}  =  tr(A·γ_q) · {X, Γ_g}.
```

The **species reduction integrates the on-site spinor uniformly** ⟹ effective
`A = I₂` ⟹ the prefactor `tr(I₂·γ_q) = 0` for every traceless on-site grading
(all `σ`'s and bivectors). So the joint anticommutation imposes **zero constraint**
on the generation factor (verified end-to-end with the circulant generation mass
`M = aI + bC + b̄C²`; `b/a` left free, never set to `1/√2`).

**Contrapositive (why this is a genuine wall, not an artifact of `A=I₂`):** a
**nonzero** induced generation grading requires `tr(A·γ_q) ≠ 0`, i.e. the Dirac
must **entangle** the on-site and generation indices — collapsing the two factors
into one combined index. But then the grading is no longer a *separate* generation
grading: it is `Γ_χ` itself read through the entangling lock, and the constraint
reduces back to `{M, Γ_χ}=0` on `R³`, which the retained no-go closes (forcing a
`C₃`-breaking import). The multi-factor structure buys nothing.

**[4b] Strongest adversary also collapses.** A joint grading **off-diagonal in the
corner index**, built from the corner double-shift `S_μS_ν` whose `hw=1` projection
is `J−I` (the *genuine* off-block generation coupling,
`flavor_native_double_shift_corner_coupling`, retained_bounded), still reduces to a
**zero** generation constraint after the qubit/species trace. The inert wall holds
whether the corner coupling is diagonal or off-diagonal.

**[5] Discriminator vs the Hamming no-go.** The Cl(3) **volume-element** variant
lands as a **scalar on the `hw=1` orbit**: `ω` is site-local (`ω = iI` on every
corner) ⟹ `ω|hw1 = i·I₃`. Like the Hamming spatial parity `ε=(−1)^{hw}` (which is
`−I₃` on `hw=1`, S₃-uniform), it commutes with `R` and does **not** anticommute
with `Γ_χ` — it cannot grade the generation orbit. So the native Cl(3) volume
route does **not evade** the established d=3+1 Hamming no-go; it **reduces to it**
(a `REDUCES-TO-HAMMING-NO-GO` collapse), for a *distinct* reason — odd-dimension
**centrality** rather than S₃-invariance — but with the *same* consequence.

**[6] Q sanity.** The only operator that *does* break `C₃` and anticommute with
`Γ_χ` has spectrum `{−λ, 0, +λ}` (signature `(1,2)` forces a zero): singular-value
`Q = 1/2` (not `2/3`), signed/Brannen `Q` divergent (trace 0). So even the
escaping branch does not reach `Q=2/3` — consistent with PT-C's V3.

## Why this is NOT a global no-go (honest residuals)

This probe prunes **one** filling of escape-hatch (II): the native on-site Cl(3)
grading coupled through the staggered lattice. It does **not** close:

- The **separate-factor Connes-Lott** route with an *independent* `H_L ⊕ H_R`
  doubling factor (not the on-site Cl(3) qubit) — still open (named open in the
  2026-06-04 `staggered_taste_is_qubit` synthesis table).
- The **equivariant-η / Z_N spectral-asymmetry** operator-realization bridge
  (retained_bounded `axiom_first_z_n_equivariant_spectral_asymmetry`, `L₃(1,2)=2/9`),
  which lives in the `C₃`-breaking sector the no-go cannot see — PT-C's named next
  path; untouched here.
- The **η-phase mass-weighting** residual riding the open staggered-Dirac gate.

The single unsupplied import remains the **`C₃`-orbit-splitting chiral grading on
`R³_gen`** — shared across the Koide `Q=2/3` and generation-identification gates.
This probe confirms the native on-site Cl(3) source is **not** that import; it does
not assert no construction can supply it.

## What this claims / does NOT claim

- **Claims:** the native Cl(3) on-site grading (volume element `ω` central scalar;
  generators `σ_a` traceless) is **inert** on the generation factor after the
  physical `hw=1` species reduction, whether coupled diagonally or off-diagonally
  in the corner index; the volume-element variant reduces to the Hamming
  scalar-collapse. Escape-hatch (II) is closed for the *native* source, as PT-C
  closed it for the *spacetime* source.
- **Does NOT claim:** a universal no-go on `r=1/2`; that the separate-factor or
  η-phase routes fail; that `Q=2/3` is empirically wrong (the masses fit it at the
  admitted physical point); any new axiom, import, or theorem promotion.

## Inputs and forbidden-imports check

- No PDG / measured / fitted values consumed. `b/a` is a free symbol and is **never**
  set to `1/√2`. Literature (Kawamoto–Smit staggered tastes) is comparator-only; the
  taste matrices and their algebra are the framework's on-site Cl(3) qubit.
- Retained dependencies (statuses verified on `origin/main` ledger 2026-06-05):
  `clifford_volume_chirality_even_dimension` (retained), `no_per_site_chirality`
  (retained_no_go), `koide_anticommuting_operator_derivation` (retained),
  `koide_z3_equivariant_anticommuting_no_go` (retained_bounded),
  `three_generation_hw1_distinct_translation_characters` (retained),
  `parity_violation_does_not_reach_generation_triplet` (retained_bounded),
  `flavor_native_double_shift_corner_coupling` (retained_bounded).
- Context-only (not load-bearing-retained): `flavor_emergent_chirality_no_transport`
  (audited_conditional — PT-C), `staggered_taste_is_qubit` / `corner_fermion_determinant`
  / `cl3_taste_generation` (unaudited).

## Cross-references

- [`KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md`](KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md)
  — §4 escape-hatch (II) this probe addresses (native variant).
- [`FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md`](FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md)
  — PT-C: escape-hatch (II) closed for the spacetime `γ_CL`; this probe extends to the native Cl(3) source.
- [`CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md`](CLIFFORD_VOLUME_CHIRALITY_EVEN_DIMENSION_NARROW_THEOREM_NOTE_2026-05-10.md)
  — `ω` central at odd `n` (the [1] core).
- [`NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md`](NO_PER_SITE_CHIRALITY_THEOREM_NOTE_2026-05-02.md)
  — no per-site `γ₅` in `M₂(C)`.
- [`STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md`](STAGGERED_TASTE_IS_THE_QUBIT_NO_SEPARATE_KOIDE_MULTIPLICITY_NARROW_OBSTRUCTION_NOTE_2026-06-04.md)
  — taste = qubit; the separate-factor route stays open (context).
- [`FLAVOR_NATIVE_DOUBLE_SHIFT_CORNER_COUPLING_NOTE_2026-05-30.md`](FLAVOR_NATIVE_DOUBLE_SHIFT_CORNER_COUPLING_NOTE_2026-05-30.md)
  — the `J−I` double-shift used in the [4b] adversary.

```yaml
claim_type_author_hint: meta
claim_scope: |
  Negative-route probe of escape-hatch (II) of the Z3-equivariant Koide no-go,
  specialized to the framework's NATIVE on-site Cl(3,0) chirality source coupled to
  the generation hw=1 orbit through the staggered lattice (taste-C3 = generation-C3).
  Result: the native joint grading is INERT on the generation factor after the hw=1
  species reduction -- block-diagonal in generation with zero qubit-partial-trace
  (diagonal and off-diagonal corner couplings both collapse); the volume-element
  variant reduces to a scalar on the orbit (the Hamming no-go). No off-block
  generation grading, no Q=2/3. Inert lemma: tr_qubit{A(x)X, gamma_q(x)Gamma_g} =
  tr(A gamma_q){X,Gamma_g}; species-uniform trace kills it (tr gamma_q = 0). This
  closes escape-hatch (II) for the native source as PT-C closed it for the spacetime
  source; it does NOT close the separate-factor Connes-Lott or equivariant-eta routes.
upstream_dependencies:
  - clifford_volume_chirality_even_dimension_narrow_theorem_note_2026-05-10
  - no_per_site_chirality_theorem_note_2026-05-02
  - koide_anticommuting_operator_derivation_theorem_note_2026-05-10
  - koide_z3_equivariant_anticommuting_no_go_note_2026-05-16
  - three_generation_hw1_distinct_translation_characters_narrow_theorem_note_2026-05-10
  - parity_violation_does_not_reach_generation_triplet_narrow_theorem_note_2026-05-23
  - flavor_native_double_shift_corner_coupling_note_2026-05-30
admitted_context_inputs:
  - standard Clifford-algebra structure (Lawson-Michelsohn); comparator-only staggered-taste literature
```
