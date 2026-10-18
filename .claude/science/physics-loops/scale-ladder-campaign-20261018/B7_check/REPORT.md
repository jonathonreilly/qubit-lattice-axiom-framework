# B7 independent check: confirmed with corrections

Provenance: a fresh-context agent of the same model family. It rebuilt everything without the repo model: its own GF(2) gauge solve, and a brute-force PSG over all 2^15 (λ,τ) per O_h element. Scripts: `chk_*.py` and logs. Saved by the supervisor from the hand-back.

## Verdicts

- **(a) Anticommutation: confirmed, wording to fix.**
  - The C2 lifts anticommute **globally** on the one-particle space.
  - k* matters only because it is fixed by both affine maps.
  - With only D2, all 8 points (±π/2)³ are forced even.
- **(b) Odd filling forced gapless: confirmed.**
- **(c) Even-filling insulators: confirmed.**
  - ν=2: certified gap ≥ 0.737.
  - ν=1 with C2x only: certified gap ≥ 0.717.
  - Site irreps: [2,2,4,4] under O and [4,4,4] under O_h.
- **(d) Twisted odd-L torus: confirmed, exact.**
  - The condition Rθ + πL·Rλ ≡ θ reduces, for odd L, to the affine fixed-point condition.
  - With θ = ±k* all 24 rotations are symmetries for L=1, 3, 5; with θ = 0 only 3 of 24 are.
  - (−1)^N commutation holds exactly on Fock space.
  - The LSM conclusion is correctly labelled conditional.
- **(e) Doubled-cell pair state: confirmed for the class "O_h about site 0 plus even translations".**
  - It is a product of on-site states, so an atomic SRE state at ν=1.
  - Caveat: this is NOT the A2-staggered-mass group, which contains odd translation × w1-odd rotations. There a free cube-centre doublet exists at ν=1. Name the class explicitly.
- **(f) Prior art: partly misattributed.**
  - Watanabe–Po–Vishwanath–Zaletel, PNAS 112, 14551 (2015) assumes time-reversal symmetry, so it is a method precedent only.
  - The interacting precedents are Po–Watanabe–Jian–Zaletel (arXiv:1703.06882) and Else–Thorngren (arXiv:1907.08204). Both are stated for spin or bosonic systems, so the fermionic (−1)^N version is an adaptation.
  - Block-state counting is due to Song–Huang–Fu–Hermele and Huang–Song–Huang–Hermele (2017).
  - The free-fermion statement is textbook double-group theory.

## Not re-checked

The runner-point node filling, the Wyckoff table, and the ν = 4–10 gaps.
