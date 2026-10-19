> Live supporting mathematical source with scope corrections. Historical run tables and numerical values below are submitted evidence, not a fresh capture or independent validation. The cross-rung primary does not execute these campaign producers. Exact displayed algebra retains its stated hypotheses. Terminal exclusions beyond the explicitly active constructive results remain deferred scientific proposals; their full arguments are preserved here for inspection and are not adopted by historical verdict labels.

# B21 findings: do the degree-2 brackets force K1 = K2?



Three harness bug logs are kept (run1, run2, run3).

**Answer: no. No bracket at any degree can, within an ansatz that leaves every Φ_ρ-non-invariant normalisation free (check scope qualifier).** Fixing any one of a_s = 1, β = −1, λ1 = ν, or a nonpolynomial single-K form breaks the freedom and forces K1 = K2. The brackets force the invariant relation λ1·K2 = ν·K1. K1 = K2 follows only with the normalisation premise h = g − δ.

## Setup

- **Constraint.** C(N) = ∫N[kin0 + kin1 − K1R1 − K2R2], with R_n = [√gR]^(n).
  - kin0 = (trP² + b(trP)²)/(4α).
  - kin1 is the general isotropic, parity-even, ultralocal h-linear kinetic metric (k1..k4).
- **Relabelling.** G = λ1G1 + G2, with G2 a general 12-term one-derivative P-linear h-linear term.
- **Lapse rule.** N′ = s1ξ·∂N + s2N∂·ξ.
- **Closure targets.** {C,C} = c0 G[ζ] with ζ = (δ + βh + β′trhδ)(N∂M − M∂N); {G,G} = νG[[ξ,η]].

## Which bracket forces what

| Step | Bracket | Result |
|---|---|---|
| A1 | {G,G} at order P | Fixes part of G2; 4 directions stay free |
| A4 | {G,G} at order P·h | λ1 free |
| A2 | {C,G} h-linear | s1 = −λ1K2/K1, s2 = 0, with a 3-dimensional null family |
| A3 | A1 + A2 together | G2 = ν∫P L_ξh uniquely, null directions removed; ν = λ1K2/K1. The check confirms this also for the fully general 648-coefficient G2 |
| A5 | {C,C} at order P | DeWitt trace b = −½; c0 = K1/(4αλ1) |
| A6 | {C,G} degree 2, P² | kin1 = DeWitt about rδ, with r = λ1/ν. s2 is a density-weight convention |
| A7 | {C,C} at order P·h | β = −1/r, β′ = 0 |
| A7b–c | {C,C} at order P·h alone | Second and third routes to λ1K2 = νK1, and β = −K2/K1 |
| A7d | with β = −1 imposed | K2 = K1 and λ1 = ν |
| A8 | joint solution | One-parameter family in r: K2/K1 = 1/r, β = −1/r, kin1 = DeWitt/r |
| W1–W3 | second code path | r = 2 with K1 = 3, K2 = 3/2 closes everywhere; r = 2 with K2 = K1 fails; r = 1 with K1 = K2 closes |

## Why no bracket can force K1 = K2

- **The map.** Φ_ρ: (h, P) → (ρh, P/ρ) is canonical, so it preserves every bracket. It sends λ1 → λ1/ρ, K1 → ρK1, K2 → ρ²K2, α → ρ²α, kin1 → kin1/ρ and β → ρβ.
- **Invariant content.** λ1K2/K1 = ν, equivalently s1 = −ν. Three independent routes give it: A3, A7b/c, and matter via B19.
- **Physical reading.** The cone v² = K2/(4α) = νK1/(4αλ1), the graviton cone, is canonically invariant. "K1/(4α)" is meaningful only once h's normalisation is fixed.
- **Equivalent premises.** Given closure these are all the same statement:
  - (a) λ1 = ν;
  - (b) structure function δ − h (β = −1);
  - (c) DeWitt on δ + h;
  - (d) unit matter coupling;
  - (e) block 62's single K on R1 and R2.

  The member supplies (e). This is HKT's "geometrodynamics regained" specialised; HKT presuppose (a) and (b).
- **Extra matter freedom (check).** The covariant non-minimal coupling R1·φ² is free. It does not change a_s, s1 or the cone.

## Premises and open items

- **Premises:** continuum, flat background, degree ≤ 2, isotropic parity-even ansätze; ultralocal kin1; Fierz–Pauli-form potential; one constraint with no ∂N terms; a field-independent lapse rule.
- **Not computed:** the h² sector, which needs [√gR]^(3) (prediction K3 = K2²/K1); degree 3; the lattice; the non-isotropic G2 in the degree-2 sectors (the h-linear uniqueness is settled by the check). The canonical-rescaling argument applies only while every normalization moved by that rescaling remains free; a fixed microscopic normalization changes the premise.

## Prior art (from memory)

- Teitelboim 1973; Kuchař 1974; HKT 1976; Isham–Kuchař 1985.
- Barbour–Foster–Ó Murchadha 2002; Anderson–Barbour 2002.
- Gomes–Shyam 2016; Giulini's reviews; Deser 1970; Hořava 2009.
- LQG deformed algebras, which relax (b).
