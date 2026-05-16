# Meron / Half-Instanton Action `4π²/g²` — External Narrow Theorem

**Date:** 2026-05-16
**Claim type:** positive_theorem
**Scope:** external 4D Euclidean SU(2) Yang-Mills meron (half-instanton)
finite classical action formula `S_meron = 4π²/g² = (1/2) S_inst`
(de Alfaro-Fubini-Furlan 1976; Callan-Dashen-Gross 1977-1979),
together with the published lattice realization on a 4D Z⁴ lattice
(Itou-Iritani 2014; González-Arroyo lineage on lattice fractional
instantons). Cited only as published gauge-theory context. No framework
substrate identification, hierarchy closure, scale ratio derivation, or
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

**Statement (external theorem):**

1. *Meron classical action.* Evaluated against the regularized
   Yang-Mills action `S[A]`, the meron configuration yields a finite
   classical action

   ```text
   S_meron = 4 π² / g²,
   ```

   as derived by de Alfaro-Fubini-Furlan (Phys. Lett. B **65** (1976)
   163) and used by Callan-Dashen-Gross (Phys. Rev. D **17** (1978)
   2717; Phys. Rev. D **19** (1979) 1826) in their meron-pair
   theory of confinement and hadronic structure.

2. *Half-action identity.* The meron action is exactly half the BPST
   instanton minimal action `S_inst = 8 π² / g²`:

   ```text
   S_meron  =  (1/2)  S_inst  =  4 π² / g².
   ```

   Equivalently, a widely-separated meron–anti-meron pair carries
   total action approaching `S_inst` from below; in the small-separation
   limit the pair coalesces into a single BPST instanton (CDG 1978).

3. *Fractional topological charge structure.* The meron carries
   fractional topological charge `Q_meron = 1/2`, in the sense that
   the topological charge integral

   ```text
   Q = (1 / (32 π²)) ∫ d^4x  Tr( F_μν *F^μν )
   ```

   accumulates a value `1/2` when integrated over half the relevant
   volume (a hemisphere of the `S^4` boundary, or equivalently the
   half-space `x_4 > 0` for a meron localized on the time axis).
   Two such half-units (a meron pair on opposite hemispheres) sum to
   integer `Q = 1`, recovering the BPST instanton integrality
   compatible with Atiyah-Singer.

4. *Lattice realization.* On a 4D Z⁴ Wilson lattice with link
   variables `U_x,μ ∈ SU(2)` and bare coupling `β = 4/g²`, Itou and
   Iritani (arXiv:1402.5984, 2014) demonstrate explicit fractional
   topological-charge configurations with charge `Q_lat = 1/2` and
   classical action approaching `4 π² / g²` in the continuum limit,
   building on the González-Arroyo lineage of lattice fractional
   instantons. The smoothing procedures used in the modern lattice
   gauge-theory literature (Wilson gradient flow; cooling) extract
   the meron action from a thermalized SU(2) configuration up to
   `O(a²)` lattice artifacts.

The action `S_meron = 4 π² / g²` is the canonical 4D SU(2) meron
classical action and is independent of the size parameter `ρ` (scale
invariance of the classical Yang-Mills action). The meron configuration
is singular at `x = 0` and at `x = ∞`; the finiteness of `S_meron` is
ensured by the logarithmic large-distance falloff of the gauge
potential combined with the standard short-distance regulator
(equivalently, gauge-fixing the meron core to a smooth interpolating
profile as in CDG).

## Boundary

This note records an external 4D Yang-Mills theorem and its standard
published lattice-gauge context. It does **not** claim:

- that the meron substrate or the CDG meron-pair configuration is
  identified with the framework's substrate (lattice cell, taste,
  blocking, plaquette family, or any project-specific structure);
- that the 4D SU(2) Wilson lattice on which the Itou-Iritani fractional
  instanton is realized is identified with any framework-specific
  lattice;
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
symbolic and `mpmath`-equivalent numerical surrogates where needed):

1. **T1**: symbolic meron action formula `S_meron = 4 π² / g²`
   reproduced as half of the BPST minimal action `8 π² / g²`.
2. **T2**: half-action identity `S_meron = (1/2) S_inst` verified
   symbolically.
3. **T3**: numerical `S_meron` at `g² ∈ {1/2, 1, 2}` evaluated as
   `4 π² / g²` ≈ `78.96`, `39.48`, `19.74` respectively.
4. **T4**: numerical `exp(-S_meron)` at the same `g²` values,
   exhibiting the canonical half-instanton suppression at intermediate
   coupling; at `g² = 1`, `4 π² ≈ 39.48` and `exp(-39.48) ≈ 7.6×10^{-18}`.
5. **T5**: fractional topological charge structure `Q_meron = 1/2`
   stated as an external theorem (the runner verifies the note text
   states `Q = 1/2` and the half-volume integration convention; the
   runner does **not** derive the fractional charge from first
   principles).
6. **T6**: meron has finite classical action despite carrying
   fractional topological charge — runner asserts that the note
   states the logarithmic large-distance asymptotic and the singular
   short-distance regulator that together render `S_meron` finite.
7. **T7**: lattice realization references — runner asserts that the
   note cites Itou-Iritani arXiv:1402.5984 (lattice meron) and the
   González-Arroyo lineage.
8. **T8**: source-note boundary — note declares `claim_type:
   positive_theorem`.
9. **T9**: boundary disclaimer — note does **not** claim framework
   substrate identification.
10. **T10**: boundary disclaimer — note does **not** claim
    `α_LM^16` closure or any hierarchy substitution (and does not
    claim `v/M_Pl = exp(-4π²/g²)`).

Expected runner result: `PASS=N`, `FAIL=0`.
