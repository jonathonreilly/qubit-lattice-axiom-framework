# Fractional Instanton Dilute-Gas Hierarchy Mechanism — External Narrow Gate

**Date:** 2026-05-16
**Claim type:** open_gate
**Scope:** external 4D Euclidean SU(N) Yang-Mills fractional-instanton
charge structure `Q = k/N` and action `S_frac = (8π²/g²) |k/N|` on `T⁴`
with twisted boundary conditions ('t Hooft 1981; Anber-Poppitz
arXiv:1811.05882, arXiv:2107.07252; Cox-Pisarski arXiv:2310.16289;
Schäfer-Shuryak Rev. Mod. Phys. 70 (1998) 323), together with the
published dilute-gas approximation form used for fractional-instanton
ensembles. The dilute-gas/condensate part is recorded as an external
modeling target whose determinant, phase-space, coupling scale, and
validity regime remain load-bearing; it is **not** admitted here as a
standalone positive theorem. Cited only as published gauge-theory
context. No framework substrate identification, hierarchy closure,
scale ratio derivation, or `α_LM^16` substitution is claimed.
**Status authority:** independent audit lane only; pipeline-derived
status set by `compute_effective_status.py`.
**Runner:** [`scripts/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.py`](../scripts/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.py)
**Cache:** [`logs/runner-cache/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.txt`](../logs/runner-cache/frontier_fractional_instanton_dilute_gas_condensate_external_narrow.txt)

## Claim

Let `A_μ(x)` be a Euclidean SU(N) gauge connection on the 4-torus
`T⁴ = (R/L_1 Z) × (R/L_2 Z) × (R/L_3 Z) × (R/L_4 Z)` with twisted
boundary conditions

```text
A_μ(x + L_ν ê_ν) = Ω_ν(x) A_μ(x) Ω_ν(x)^{-1} - i Ω_ν(x) ∂_μ Ω_ν(x)^{-1}
```

where the transition functions `Ω_ν ∈ SU(N)` carry a non-trivial
't Hooft twist tensor `n_μν ∈ Z_N` (anti-symmetric, mod N) satisfying
the cocycle compatibility

```text
Ω_μ(x + L_ν ê_ν) Ω_ν(x) = e^{2π i n_μν / N} Ω_ν(x + L_μ ê_μ) Ω_μ(x).
```

The Euclidean Yang-Mills action is

```text
S[A] = (1 / (2 g²)) ∫_{T⁴} d^4x  Tr( F_μν F^μν )
```

and the topological charge

```text
Q = (1 / (32 π²)) ∫_{T⁴} d^4x  Tr( F_μν *F^μν ).
```

**Statement (external open gate):**

1. *Fractional topological charge.* On `T⁴` with a non-trivial 't Hooft
   twist `n_μν ∈ Z_N`, the topological charge takes fractional values

   ```text
   Q = k / N,    k ∈ Z,
   ```

   in units of the integer instanton charge. The minimum-action
   self-dual configuration in the sector `Q = k/N` is the
   't Hooft / González-Arroyo fractional instanton ('t Hooft Nucl.
   Phys. B **190** (1981) 455; González-Arroyo Nucl. Phys. B **153**
   (1979) 141; lineage continued in Anber-Poppitz arXiv:1811.05882,
   arXiv:2107.07252).

2. *Fractional instanton action.* The classical action of the
   self-dual minimum in the `Q = k/N` sector is

   ```text
   S_frac  =  (8 π² / g²) · |k / N|,
   ```

   reducing to the BPST minimal action `S_inst = 8 π² / g²` at integer
   charge `|k/N| = 1`. For the smallest fractional sector `k = 1`,
   `N` arbitrary,

   ```text
   S_frac(k=1, N)  =  (8 π² / g²) · (1 / N).
   ```

   This is the canonical fractional-instanton action used in the
   modern dilute-gas analysis (Anber-Poppitz arXiv:1811.05882,
   arXiv:2107.07252; Cox-Pisarski arXiv:2310.16289).

3. *Reduction to BPST and half-action scale at integer / half-integer charge.* At
   `N = 1` (no twist), the formula collapses to the BPST instanton
   `S_inst = 8 π² / g²`. At `N = 2`, `k = 1` (minimal `Z_2` twist),

   ```text
   S_frac(k=1, N=2)  =  4 π² / g²,
   ```

   matching the half-action scale recorded in the companion meron /
   fractional-instanton open-gate note. This is a numerical/algebraic
   cross-check of the scale only; it does not promote the singular
   unregularized meron to a finite-action theorem.

4. *Dilute-gas free-energy structure.* In the dilute-gas approximation,
   the partition function of the `Q = k/N` fractional-instanton
   ensemble factorizes as a sum over independent localized
   configurations only in the regime where the approximation is valid.
   The contribution of a single fractional
   instanton to the partition function takes the schematic form

   ```text
   Z_1(k, N)  ~  V · ∫ dρ  D(ρ; g, μ)  exp( - S_frac(k, N) ),
   ```

   where `V` is the 4-volume, `D(ρ; g, μ)` is the one-loop zero-mode +
   determinant density at renormalization point `μ` (Schäfer-Shuryak
   Rev. Mod. Phys. **70** (1998) 323; 't Hooft Phys. Rev. D **14**
   (1976) 3432). Summing the dilute-gas series yields a free-energy
   density

   ```text
   F_DG  =  - V · n_eff · exp( - S_frac ) · (one-loop determinant),
   ```

   with `n_eff` a combinatorial / orientation factor whose value is
   model- and regime-dependent. In the same schematic approximation,
   the corresponding vacuum-energy-density scale is often written as

   ```text
   ε_vac  ~  - exp( - S_frac ) · M^4,
   ```

   per fractional sector, with `M` a dimensionful scale set by the
   determinant and running-coupling context. This note does not derive
   `n_eff`, `M`, or the integration measure.

5. *Condensate/gas-density criterion as an open target.* A common
   heuristic for when fractional-instanton effects can become dense is
   that the per-sector Boltzmann factor is not exponentially small
   relative to the available determinant and phase-space factors,
   schematically

   ```text
   exp( - S_frac )  ~  O(1)
   ```

   on the relevant scale. This is not a theorem-grade condensate
   formation claim inside this repo: the determinant, density of states,
   coupling scale, finite-volume/temperature limits, and convergence of
   the expansion must be supplied by a future audited bridge.

6. *Canonical numerical values.* At canonical bare coupling `g² = 1`
   the action evaluates as

   ```text
   N = 2, k = 1:  S_frac = 4 π² ≈ 39.48,   exp(-S_frac) ≈ 7.16 × 10⁻¹⁸,
   N = 3, k = 1:  S_frac = 8 π² / 3 ≈ 26.32,  exp(-S_frac) ≈ 3.7 × 10⁻¹²,
   N = 4, k = 1:  S_frac = 2 π² ≈ 19.74,   exp(-S_frac) ≈ 2.7 × 10⁻⁹.
   ```

   These are raw action Boltzmann factors for the stated external
   normalization; they are not framework numerical predictions and do
   not by themselves establish condensate formation.

7. *Twisted boundary condition requirement.* The fractional charge
   `Q = k/N` requires the underlying 4-manifold to admit a non-trivial
   `Z_N` center twist. On `R^4` (no twist) the topological charge is
   integer-valued (Atiyah-Singer index theorem). The fractional sector
   `Q = k/N` is intrinsic to the twisted-`T⁴` setting and to the
   center-symmetry-respecting boundary conditions used by 't Hooft
   1981, González-Arroyo 1979, Anber-Poppitz 2018-2021, and the modern
   Cox-Pisarski 2023 dilute-gas analysis.

The action formula and schematic dilute-gas expression are external
inputs/targets for later bridge work. This note does not assert that
the dilute-gas expansion converges, that a condensate forms, or that
the determinant/phase-space factors produce a framework hierarchy.

## Boundary

This note records an external 4D Yang-Mills action formula and its
standard published lattice / dilute-gas neighborhood. It does **not**
claim:

- that the fractional instanton substrate or the twisted-`T⁴` setting
  is identified with the framework's substrate (lattice cell, taste,
  blocking, plaquette family, `Z⁴` Wilson surface, or any
  project-specific structure);
- that the 4D SU(N) `T⁴`-with-`Z_N`-twist setting is identified with
  any framework-specific lattice or substrate;
- closure of any framework substitution, hierarchy formula, scale
  ratio, or physical observable;
- theorem-grade closure of dilute-gas convergence, condensate
  formation, one-loop determinant normalization, phase-space density,
  or running-coupling scale choice;
- closure of the `α_LM^16` substitution or any framework `α^N`
  hierarchy at integer `N`;
- closure of `v/M_Pl` or any other dimensional scale ratio (the
  hierarchy formula `v/M_Pl = exp(-S_frac)` is **not** claimed; the
  note records only the fractional-instanton action and a schematic
  dilute-gas target as external context);
- any identification of the published `S_frac` Boltzmann factor with a
  framework hierarchy ratio;
- any numerical prediction or comparison with observation beyond the
  published gauge-theory context;
- any new framework axiom or repo-wide premise.

Any later framework use must separately identify the framework
substrate with the 4D SU(N) twisted-`T⁴` gauge background, identify a
framework observable with the fractional-instanton sector, derive the
determinant/phase-space/coupling-scale data, and verify the
substrate-specific bridge.

## External References

- G. 't Hooft, "A property of electric and magnetic flux in
  nonabelian gauge theories", Nucl. Phys. B **153** (1979) 141 (twisted
  boundary conditions; see also `n_μν` framework).
- G. 't Hooft, "Topology of the gauge condition and new confinement
  phases in non-abelian gauge theories", Nucl. Phys. B **190** (1981)
  455. (Fractional `Q = k/N` and early condensate analysis.)
- G. 't Hooft, "Computation of the quantum effects due to a
  four-dimensional pseudoparticle", Phys. Rev. D **14** (1976) 3432.
  (One-loop dilute-gas determinant.)
- A. González-Arroyo, "Yang-Mills fields on the four-dimensional
  torus", Nucl. Phys. B **153** (1979) 141, and subsequent lineage.
  (Fractional instantons on `T⁴` with twist.)
- M. M. Anber, E. Poppitz, "Two-flavor adjoint QCD, Z_2_N anomalies,
  and generalized symmetries", arXiv:1811.05882 (2018). (Fractional
  θ-vacua + fractional-instanton dilute gas in the modern setting.)
- M. M. Anber, E. Poppitz, "Anomaly and gauging of symmetries in
  4D",  arXiv:2107.07252 (2021). (Fractional instanton + center
  vortex.)
- P. Cox, R. D. Pisarski, "An effective theory of fractional
  instantons", arXiv:2310.16289 (2023). (Modern dilute-gas analysis.)
- T. Schäfer, E. V. Shuryak, "Instantons in QCD",
  Rev. Mod. Phys. **70** (1998) 323. (Instanton liquid review;
  dilute-gas determinant.)
- A. A. Belavin, A. M. Polyakov, A. S. Schwartz, Y. S. Tyupkin,
  "Pseudoparticle Solutions of the Yang-Mills Equations",
  Phys. Lett. B **59** (1975) 85. (BPST instanton, cited for the
  `N=1` collapse.)
- Y. Itou, T. Iritani, "Fractional Instanton on Z⁴ Lattice",
  arXiv:1402.5984 (2014). (Lattice realization of fractional charges,
  cross-check with the meron `N=2` reduction.)

## Verification

The paired runner checks (in exact Fraction arithmetic with SymPy `pi`
symbolic and `mpmath`-equivalent numerical surrogates where needed):

1. **T1**: symbolic fractional topological charge `Q = k/N` and action
   formula `S_frac = (8 π² / g²) |k/N|` reproduced.
2. **T2**: half-action cross-check — at `N = 2`, `k = 1`,
   `S_frac = 4 π² / g²`, matching the companion open-gate half-action
   scale without promoting a standalone meron theorem.
3. **T3**: numerical `S_frac` at canonical `g² = 1` for several `N`:
   `SU(2): 4 π²`, `SU(3): 8 π² / 3`, `SU(4): 2 π²`.
4. **T4**: dilute-gas free-energy structural form recorded —
   `F_DG = -V · n_eff · exp(-S_frac) · (1-loop det)` (symbolic only;
   no numerical claim on `n_eff` or `D(ρ; g, μ)`).
5. **T5**: open condensate/gas-density criterion recorded —
   `exp(-S_frac) ~ O(1)` is tagged as heuristic/model-regime language,
   with determinant/phase-space/coupling-scale data left open.
6. **T6**: at SU(3), `g² = 1`, `k = 1`,
   `S_frac = 8 π² / 3 ≈ 26.32`, `exp(-S_frac) ≈ 3.7 × 10⁻¹²` (canonical
   numerical Boltzmann factor).
7. **T7**: twisted boundary condition requirement recorded —
   `T⁴` with non-trivial `Z_N` center twist `n_μν` is needed for the
   fractional `Q = k/N` sector to exist.
8. **T8**: source-note boundary — note declares `claim_type: open_gate`.
9. **T9**: boundary disclaimer — note does **not** claim framework
   substrate identification.
10. **T10**: boundary disclaimer — note does **not** claim
    `α_LM^16` closure or any hierarchy substitution (and does not
    claim `v/M_Pl = exp(-S_frac)`).

Expected runner result: `PASS=N`, `FAIL=0`.
