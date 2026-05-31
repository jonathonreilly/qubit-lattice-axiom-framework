---
claim_id: z_n_spectral_asymmetry_physical_identification_note_2026-05-31
claim_type_author_hint: positive_theorem
status_authority: independent_audit_lane_only
direct_effective_status_change_allowed_from_this_note: false
---

# Physical-identification leg: L₃(1,2)=2/9 is the signed equivariant spectral asymmetry of the native generation operator H

**Date:** 2026-05-31
**Claim type:** positive identification theorem (finite / algebraic). Adds no
axiom and no import; introduces no new operator, substrate, or dynamics.
**Status authority:** independent audit lane only. This note does **not** set,
predict, or request any audit verdict, and does **not** itself promote the
supported note — any tier change is pipeline-derived after independent audit.
**Primary runner:**
`scripts/frontier_z_n_spectral_asymmetry_physical_identification.py`
with cache
`logs/runner-cache/frontier_z_n_spectral_asymmetry_physical_identification.txt`
(22/22 checks).

## Purpose

The retained_bounded note
[`AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md`](AXIOM_FIRST_Z_N_EQUIVARIANT_SPECTRAL_ASYMMETRY_NARROW_THEOREM_NOTE_2026-05-26.md)
proves the exact finite cyclotomic identity

```
L_N(a) = (1/N) sum_{k=1}^{N-1} prod_j 1/(zeta_N^{k a_j} − 1),     L_3(1,2) = 2/9,
```

and lists two honest residuals that bound it below `retained`:

1. it does **not** prove the continuum APS eta invariant on a real lens space;
2. the `C₃` dependency "supplies only bounded support for the weight pattern,
   **not a physical identification**" — i.e. it does not prove the abstract
   cyclotomic sum **is** the signed spectral asymmetry of a native framework
   operator.

This note supplies **residual (2) only** — the physical identification — and
explicitly **not** residual (1). It is promotion-support, not closure.

## The native operator

The native generation operator on the `hw=1` triplet
([`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md))
is the `C₃` circulant

```
H = a I + b C + b̄ C²        on ℂ³,   C the cyclic shift (C³ = I),
```

the Hermitian lift `H = iD` of the retained-bounded real anti-Hermitian
staggered Dirac operator
([`CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md`](CPT_EXACT_REAL_ANTI_HERMITIAN_D_NARROW_THEOREM_NOTE_2026-05-10.md))
whose Koide reduction is
[`KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md`](KOIDE_CIRCULANT_Q_TWO_THIRDS_ALGEBRAIC_NARROW_THEOREM_NOTE_2026-05-10.md).
The `C₃` body-diagonal character pattern `(1, ω, ω²)` is the retained-bounded
circulant surface
[`NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md`](NEW_PARITY_IS_CIRCULANT_PHASE_NARROW_THEOREM_NOTE_2026-05-23.md).

## The identification

Because `[H, C] = 0`, the generation operator and the `C₃` symmetry share an
eigenbasis. H's spectrum splits canonically:

- the **C-fixed singlet** `v₀ = (1,1,1)/√3` (`C v₀ = v₀`, trivial character,
  weight `0`) — the generation-uniform scale direction;
- the **doublet** `v₁, v₂` carrying the two **non-trivial** `C`-characters
  `ω¹, ω²`.

**(i) The transverse weights are H's doublet characters — not an abstract
choice.** The weight tuple `(a₁, a₂)` in `L_N` is recovered from H itself: the
two non-singlet eigenmodes of `H` carry `C`-eigenvalues `ω¹` and `ω²`, so the
weight tuple is exactly `(1, 2)` (runner §B). The singlet is the trivial
character (weight `0`); the doublet is the `(1,2)` sector. The abstract repeated
patterns `(1,1)`, `(2,2)` — which evaluate to `1/9`, not `2/9` — are **not** H's
doublet, because H's two doublet characters are **distinct** (`{1,2}`, not
repeated). So `2/9` rather than `1/9` is selected by H's distinct-character
doublet (runner §D).

**(ii) The cyclotomic factor is a resolvent of the generation symmetry on H's
doublet.** Since `C^k` acts on the doublet eigenmode of character `ω^{a_j}` as
the scalar `ω^{k a_j}`, the factor `1/(ω^{k a_j} − 1)` is exactly the eigenvalue
of the resolvent `(C^k − I)⁻¹` on that mode. Hence

```
L_3(1,2) = (1/N) sum_{k=1}^{N-1} det[ (C^k − I)⁻¹ | doublet of H ] = 2/9,
```

computed two independent ways — the note's cyclotomic formula and the
H-intrinsic resolvent determinant — and shown **equal** (runner §C, with the
symbolic identity `(ω−1)(ω²−1) = 3` in `ℤ[ω]`). `L₃(1,2)` is therefore a
spectral functional of the generation symmetry `C` **restricted to H's
doublet**, not an abstract character sum.

**(iii) The doublet is H's signed / spectral-flow sector.** The signed content
is intrinsic to H: at `θ = arg(b) = 0` the singlet eigenvalue `a + 2|b|` stays
positive for all `r = |b|²/a²`, while the **doublet eigenvalues cross zero at
`r = 1`** (the spectral-flow point) — positive for `r<1`, negative for `r>1`
(runner §E). The finite equivariant spectral asymmetry of H,

```
eta_C(H) = sum_{λ_k ≠ 0} sign(λ_k) · tr(C | ker(H − λ_k))  ∈  ℤ[ω],
```

(the well-defined object of the supported note's Statement 1) is `0` for `r<1`
(`1 + ω + ω² = 0`) and **jumps to `2`** for `r>1` (`1 − (ω + ω²) = 2`) — the jump
carried entirely by the doublet. So the doublet **is** H's signed
spectral-asymmetry sector, and the "asymmetry channel" value `r = 1` is exactly
its zero-crossing. `L₃(1,2) = 2/9` is the finite equivariant eta / Lefschetz
weight of that sector.

This is the constructive content asserted (not proved) by the parallel sibling
`KOIDE_READOUT_CHANNEL_MAP_NOTE_2026-05-31` (PR sibling), which maps the
asymmetry channel to "the eigenvalue signs / spectral flow" of the same `H`;
here that mapping is proved from H's eigenstructure.

## What this removes, and what it does not

**Removes residual (2).** Every ingredient of `L₃(1,2)` is now tied to the
native operator H: the weights `(1,2)` are H's doublet `C`-characters, the
singlet/doublet split is H's `C`-fixed-locus / orthogonal-complement split, the
factor `1/(ω^{k a_j}−1)` is `(C^k − I)⁻¹` on H's doublet, and the signed
structure is H's doublet zero-crossing at `r=1`. The weight sum is the signed
equivariant spectral asymmetry of the native generation operator — not merely
"bounded support for a weight pattern."

**Does NOT address residual (1).** No continuum APS eta invariant on a real lens
space is proved or computed. The identification here is **finite /
algebraic** — the equivariant character of the finite group `⟨C⟩ ≅ Z₃` acting on
the finite-dimensional triplet. The continuum Atiyah–Patodi–Singer fixed-point
bridge (lens-space eta, a framework Dirac operator on a curved background)
remains an open import; this note does not retire it. The Atiyah–Bott /
Donnelly Lefschetz language is **external context** for why the finite
resolvent-determinant is the right sidecar object, exactly as in the supported
note.

## Non-circularity

`r = |b|²/a²` is the free scan variable; `r = 1` (the asymmetry value) and `2/9`
emerge only as outputs (runner §F). `L₃(1,2)` is computed independently via the
cyclotomic formula and the H-intrinsic resolvent determinant and the two are
shown equal — the identification is a proven equality, not an assumed labelling.

## Promotion handoff

This note requests independent audit of the **physical-identification leg**
above. If the audit lane accepts that residual (2) is discharged — the finite
cyclotomic weight sum **is** the signed equivariant spectral asymmetry of the
native generation operator H — then the only residual remaining on
`axiom_first_z_n_equivariant_spectral_asymmetry` is the continuum APS bridge
(residual 1). Whether that justifies a tier change of the supported note is
**audit-decided**; this note neither sets nor requests it, and edits no audit
row.

## Anchors (live-ledger tiers, verified origin/main 2026-05-31)

retained / retained_bounded:
`axiom_first_z_n_equivariant_spectral_asymmetry` (retained_bounded, the supported
note), `koide_circulant_q_two_thirds_algebraic` (retained),
`cpt_exact_real_anti_hermitian_d` (retained_bounded),
`new_parity_is_circulant_phase` (retained_bounded),
`three_generation_hw1_distinct_translation_characters` (retained),
`three_generation_observable_theorem` (retained).
