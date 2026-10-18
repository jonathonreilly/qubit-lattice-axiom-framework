# B21 check

Provenance: a fresh-context checker of the same model family. Its code is new: brackets computed directly on Fourier kernels, with no Euler operator, and its own √gR, DeWitt expansion and G2 bases (12 isotropic terms, and 648 general). Saved by the supervisor from the hand-back.

**Result:** `chk_b21.py` gives PASS=17 FAIL=0 (95 s). One expectation-bug log is kept: the matter coupling has a real extra freedom, R1·φ².

## Verdicts

- **(i) Confirmed, with a scope qualifier.** The Φ_ρ table was verified by substitution, including a_s → ρa_s.
  - The invariants are λ1K2/K1, K2/(4α), νK1/(4αλ1) and c0.
  - r = 1/3 (K1 = 3, K2 = 9) also closes.
  - **The no-go needs an ansatz that leaves every Φ_ρ-non-invariant normalisation free.** Fixing any of these breaks it and forces K1 = K2 (computed for the first two): a_s = 1, β = −1, λ1 = ν, a fixed nonpolynomial form, or a microscopic scale for h.
  - Lattice spacing, the background δ and the abelian lattice member do not break the freedom.
- **(ii) Confirmed**, by the A3, A7b and matter routes.
- **(iii) Confirmed.** kin1 = DeWitt/r, β = −1/r, K2/K1 = 1/r.
- **(iv) Confirmed and upgraded.** Uniqueness of G2 = ν∫P L_ξh also holds for the fully general 648-coefficient G2. The null dimensions are 129 for {G,G}, 145 for {C,G}, and 0 for both together.
- **(v) Confirmed.** All five premises are equivalent to r = 1. For (d) the coupling is (λ_s/λ1) × the unit stress, so a_s = 1/r.
- **(vi) Plausible.** HKT presuppose (a) and (b).

**Witness.** r = 2, r = 1 and r = 1/3 close in all six sectors. r = 2 with K2 := K1 fails {C,G} h-linear and {C,C} at P·h.

## Restatement for the notes

The common cone of matter and graviton is v² = K2/(4α), in lattice-coordinate units. K2 is the coefficient of [√gR]^(2), the TT term. It equals K1/(4α) only when r = 1. In the 09-24 / block-62 member K1 = K2 = K is supplied, so "K/(4α)" is correct there, with K read as the R2 (TT) coefficient.

**Open:** the h² sector (needs R3), degree 3, the lattice, multi-derivative G2, and the microscopic normalisation of h.
