# B14 independent check: core claims confirmed, with caveats

Provenance: a fresh-context agent of the same model family. Files: `chk_e2_cone.py`, `chk_e5_obstruction.py`, logs, and `CHECK_NOTES.txt`. Saved by the supervisor from the hand-back.

## (1) E2 re-derived analytically: confirmed

- **The bracket.** {H_m(N),H_m(M)} = G_m[−cξ̃] exactly; the mass term cancels. Gravity gives G_g[(sK/4α)ξ̃]. So one total relabelling exists iff c = −sK/(4α), and sign(c) = −sign(sK/α) is convention-independent.
- **Caveat 1.** The "forced GR sign" holds given the supplied c > 0, α > 0, K > 0. With s = +1, closure gives c = −K/(4α): elliptic matter, the Euclidean HKT algebra.
- **The 09-24 sign, stronger form.** Block 101's Lagrangian linearises to N√g R − Nρ, so its Hamiltonian carries −K·R1. The 09-24 runner's +K·R1 is opposite to its own action and gives the Euclidean algebra. That is harmless for gravity alone, but inconsistent once matter is present.
- **Caveat 2.** One-endpoint bond timing gives a one-sided relabelling. "Endpoint mean required" holds only relative to the supplied symmetric G_m.

## (2) Own lattice test: confirmed

On L = 3 and 4, closure holds only at (s, c) = (+1, −κ) and (−1, +κ), with κ = K/(4α). Two species close iff c₁ = c₂.

## (3) E5 obstruction: confirmed and robust

No closure with matched timing (114 operators), free lapse placement (708) or longer range (804). A positive control that subtracts the obstruction monomial closes. The result is conditional on the supplied H_m and G_m discretisation.

## E6 note

E6 is reported selectively: at L = 6 and 8 the residual ratio exceeds 1. The absolute residual is roughly flat, so the falling ratio comes mainly from the growing base bracket. That fits an O(a²) artefact, but it rests on one configuration.

## (4) Attribution

- **Prior art:**
  - Teitelboim 1973 (common signature and light cone);
  - Kuchař 1974 and 1976;
  - Hojman–Kuchař–Teitelboim 1976;
  - Deser 1970 (universal coupling);
  - Düll–Schuller 2018;
  - lattice breaking of the algebra: Renteln–Smolin, Gambini–Pullin, Bahr–Dittrich.
- **New and narrow:**
  - the exact order-ε lattice realisation in the 09-24 discretisation;
  - the pairing of bond timing with G_m;
  - the explicit O(a²) obstruction monomial;
  - the 09-24 runner's sign mismatch with block 101.
