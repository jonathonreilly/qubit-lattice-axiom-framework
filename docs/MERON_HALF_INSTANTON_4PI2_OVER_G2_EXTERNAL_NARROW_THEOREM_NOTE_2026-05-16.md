# Meron / Fractional-Instanton Half-Action `4π²/g²` — External Narrow Gate

**Date:** 2026-05-16
**Claim type:** open_gate
**Scope:** external 4D Euclidean SU(2) meron / fractional-instanton
context for the half-instanton action scale `4π²/g² = (1/2) S_inst`.
The note records the candidate scale only under explicit regulator,
meron-pair, half-volume, or twisted-boundary/fractional-instanton
conditions. It does **not** assert that the singular unregularized
single meron on `R^4` is a standalone finite-action theorem. Cited only
as published gauge-theory context. No framework substrate
identification, hierarchy closure, scale ratio derivation, or
`α_LM^16` substitution is claimed.
**Status authority:** independent audit lane only; pipeline-derived
status set by `compute_effective_status.py`.
**Runner:** [`scripts/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.py`](../scripts/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.txt`](../logs/runner-cache/frontier_meron_half_instanton_4pi2_over_g2_external_narrow.txt)

## Claim

Let `A_μ(x)` be a Euclidean SU(2) gauge connection on `R^4` with field
strength

```text
F_μν = ∂_μ A_ν - ∂_ν A_μ + i [A_μ, A_ν]
```

and Hodge dual

```text
(*F)_μν = (1/2) ε_μνρσ F^ρσ.
```

The Euclidean Yang-Mills action is

```text
S[A] = (1 / (4 g²)) ∫ d^4x  Tr( F_μν F^μν ).
```

The Callan-Dashen-Gross / de Alfaro-Fubini-Furlan meron solution on
`R^4` is the explicit singular SU(2) configuration

```text
A_μ^a(x) = (1 / g)  η^a_μν  ∂_ν  ln( x² / ρ² )
```

where `η^a_μν` is the standard 't Hooft symbol, `ρ` is a size
parameter, and `x² = δ_μν x^μ x^ν` is the Euclidean radius squared.

**Statement (external open gate):**

1. *Regularized meron / fractional-instanton action scale.* The
   singular de Alfaro-Fubini-Furlan / Callan-Dashen-Gross meron on
   `R^4` requires a regulator or paired/capped construction; without
   that boundary data the single-meron action is not being claimed here
   as a finite standalone theorem. In the regularized meron-pair,
   capped-core, half-volume, or fractional-instanton contexts cited
   below, the candidate half-instanton scale is

   ```text
   S_half = 4 π² / g²,
   ```

   with the regulator/boundary construction remaining load-bearing.
   This note therefore records an external target and source context,
   not a retained theorem-grade admission of a universal unregularized
   meron action.

2. *Half-action identity under the stated boundary data.* The
   half-instanton scale is algebraically half the BPST instanton
   minimal action `S_inst = 8 π² / g²`:

   ```text
   S_half  =  (1/2)  S_inst  =  4 π² / g².
   ```

   In a self-dual fractional-instanton setting this is the usual
   `S = (8π²/g²) |Q|` formula at `|Q| = 1/2`. In a meron setting, the
   regulator or pair construction is part of the claim boundary and is
   not supplied by the bare algebraic identity alone.

3. *Fractional topological charge structure.* Fractional charge
   `Q = 1/2` is admitted only in the cited half-volume, meron-pair, or
   twisted-boundary/fractional-instanton settings, not as an ordinary
   smooth compact SU(2) bundle charge. The topological charge integral

   ```text
   Q = (1 / (32 π²)) ∫ d^4x  Tr( F_μν *F^μν )
   ```

   can contribute a half-unit once the relevant boundary/twist/patching
   data are fixed. Two compatible half-units can sum to integer
   `Q = 1`, recovering the BPST instanton integrality compatible with
   Atiyah-Singer in the closed smooth setting.

4. *Lattice realization context.* On suitable 4D lattice/twisted-boundary
   setups, the cited lattice fractional-instanton literature studies
   fractional topological charge and half-instanton action scales. This
   note does not claim that every 4D `Z^4` Wilson lattice realizes such a
   sector, nor that the framework lattice is one of those sectors.

The load-bearing boundary is the regulator/twist/patching construction.
The singular meron configuration is not smooth at `x = 0` and has
infrared/large-distance boundary subtleties; this note does not turn
that singular object into a finite-action positive theorem.

## Boundary

This note records an external 4D Yang-Mills target/context and its
standard published lattice-gauge neighborhood. It does **not** claim:

- that the meron substrate or the CDG meron-pair configuration is
  identified with the framework's substrate (lattice cell, taste,
  blocking, plaquette family, or any project-specific structure);
- that the 4D SU(2) Wilson lattice on which the Itou-Iritani fractional
  instanton is realized is identified with any framework-specific
  lattice;
- that the singular unregularized single meron on `R^4` is a smooth
  finite-action theorem;
- that the regulator, cap, pair, twist, or continuum-limit hypotheses
  needed for a half-action statement have been derived inside the repo;
- closure of any framework substitution, hierarchy formula, scale
  ratio, or physical observable;
- closure of the `α_LM^16` substitution or any framework `α^N`
  hierarchy at integer `N`;
- closure of `v/M_Pl` or any other dimensional scale ratio (the
  hierarchy formula `v/M_Pl = exp(-4π²/g²)` is **not** claimed; the
  note records only the meron action as a standalone external
  theorem);
- any identification of `4π² ≈ 39.48` with `ln(M_Pl/v) ≈ 38.4` or any
  other framework scale separation;
- any numerical prediction or comparison with observation beyond the
  published gauge-theory context;
- any new framework axiom or repo-wide premise.

Any later framework use must separately identify the framework
substrate with the 4D SU(2) gauge background, identify a framework
observable with the meron sector, and verify the substrate-specific
bridge.

## External References

- V. de Alfaro, S. Fubini, G. Furlan,
  "A new classical solution of the Yang-Mills field equations",
  Phys. Lett. B **65** (1976) 163. (Meron solution.)
- C. G. Callan, R. F. Dashen, D. J. Gross,
  "Toward a theory of the strong interactions",
  Phys. Rev. D **17** (1978) 2717. (Meron-pair theory of confinement.)
- C. G. Callan, R. F. Dashen, D. J. Gross,
  "A theory of hadronic structure",
  Phys. Rev. D **19** (1979) 1826. (CDG meron / half-instanton.)
- D. Diakonov, "Instantons at work",
  Prog. Part. Nucl. Phys. **51** (2003) 173; arXiv:hep-ph/0212026.
  (Meron + instanton review.)
- Y. Itou, T. Iritani, "Fractional Instanton on Z⁴ Lattice",
  arXiv:1402.5984 (2014). (Lattice meron / fractional charge `Q=1/2`.)
- A. González-Arroyo and coauthors, long lineage on lattice instantons
  and fractional charges (e.g. Nucl. Phys. B **153** (1979) 141 on
  twisted boundary conditions; subsequent twisted-Eguchi-Kawai
  fractional-charge work).
- A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Y. S. Tyupkin,
  "Pseudoparticle Solutions of the Yang-Mills Equations",
  Phys. Lett. B **59** (1975) 85. (BPST instanton, `S_inst = 8 π²/g²`,
  cited for the half-action identity.)

## Verification

The paired runner checks (in exact Fraction arithmetic with SymPy `pi`
symbolic and numerical surrogates where needed):

1. **T1**: symbolic half-action scale `S_half = 4 π² / g²`
   reproduced as half of the BPST minimal action `8 π² / g²`.
2. **T2**: half-action identity `S_half = (1/2) S_inst` verified
   symbolically.
3. **T3**: numerical `S_half` at `g² ∈ {1/2, 1, 2}` evaluated as
   `4 π² / g²` ≈ `78.96`, `39.48`, `19.74` respectively.
4. **T4**: numerical `exp(-S_half)` at the same `g²` values,
   exhibiting the canonical half-instanton suppression at intermediate
   coupling; at `g² = 1`, `4 π² ≈ 39.48` and `exp(-39.48) ≈ 7.6×10^{-18}`.
5. **T5**: fractional topological charge structure `Q = 1/2` is stated
   only under boundary/twist/half-volume hypotheses (the runner does
   **not** derive the fractional charge from first principles).
6. **T6**: singular-meron boundary — runner asserts that the note
   explicitly refuses to treat the unregularized single meron as a
   finite-action theorem and records the regulator/twist/patching
   dependency.
7. **T7**: lattice realization references — runner asserts that the
   note cites Itou-Iritani arXiv:1402.5984 (lattice meron) and the
   González-Arroyo lineage.
8. **T8**: source-note boundary — note declares `claim_type: open_gate`.
9. **T9**: boundary disclaimer — note does **not** claim framework
   substrate identification.
10. **T10**: boundary disclaimer — note does **not** claim
    `α_LM^16` closure or any hierarchy substitution (and does not
    claim `v/M_Pl = exp(-4π²/g²)`).

Expected runner result: `PASS=N`, `FAIL=0`.

## Upstream authority

- [TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md](TOPOLOGICAL_INSTANTON_TEXTBOOK_INFRASTRUCTURE_IMPORT_NOTE_2026-05-17.md) — bounded named-import umbrella wrapper covering Luescher admissibility / gradient-flow lattice charge and twisted-`T^4` `'t Hooft / van Baal` fractional `Q = k / N` sectors. Provides the one-hop authority for the regulator / twist / patching construction yielding the `Q = 1/2`, `S = 4 pi^2 / g^2` meron half-action sector.
