# B18 check: taste symmetry and isotropic doublers

Provenance: a fresh-context checker of the same model family. All code is its own, built from the scale-ladder runner's construction code (`chk_model.py`), not from b18lib, walklib or diraclib. Saved by the supervisor from the hand-back.

**Totals: PASS=31, FAIL=1.** The FAIL is the checker's own zero-chirality test, which fails because the word has nodal lines (chk5c, confirmed by chk5d). First-run errors were the checker's own.

## Verdicts

1. **S theorem: holds, and is extended.**
   - V_ac = 0 unless f_c = Mᵀf_a, for any continuous (even measurable) V.
   - Mᵀ must permute the 12 face diagonals, so M ∈ O_h, and θ ∈ (π/2)Z³.
   - Exactly 96 of 3072 (M, θ) are allowed: the PSG lifts × the Q-taste. All send k* to ±k*.
   - This covers all GL(3,Z) maps, real θ, antiunitary maps and E → −E. Lattice translations are absorbed.
   - **Scope note:** S is 12 families of 1D chains, with corner-dependent line symmetries diag((−1)^{n_c·x}). These lie outside the uniform-taste theorem and are not symmetries of the eight-node step. Say "no uniform (translation-covariant) taste".
2. **Normaliser obstruction: holds.**
   - |Stab| is 24 at k* and 8 at the doubler.
   - Forced isotropy holds for M ∈ O_h. For general GL(3,Z) the forced cone is isotropic only in a pulled-back metric, which fails B17 anyway.
3. **The eight-node step has no taste: holds, with the proof completed.**
   - Exact perturbation theory confirms:
     - v* = 0.4714045 isotropic at ±k*;
     - doublers (0.2467203, 0.5837466, 0.5837466), ratio 1 − 1/√3;
     - an identical node set at −π/2.
   - **Added:** four more Weyl doublets at the doubler momenta, at E = ±1.144936 and ±1.996657, with speeds (0.12336, 0.06168, 0.06168) and |det| 0.000469. None matches v*³.
   - Unitarity forces |det M| = 1.
   - **Exhaustive test:** of 48 × 8 × 2 maps with E → ±E + φ, 192 pass, and every one sends k* to ±k*. The smallest mismatch is 0.384 rad.
   - The Q-taste is an on-site V with w = −1, and every B1 step has it.
4. **c3: holds for all α and both w.** Conjugating by the axis C2s preserves the corner planes, so α cancels. The commutant at k* is blocks 6 + 6. Limited to H_link-type V.
5. **S² family and B1 table: numbers confirmed, with corrections.**
   - (a) **X-point isotropy is an exact taste:** V W(k) V⁻¹ = W(k + (π/2)e_x).
   - (b) **Census corrected.** At E = π one cell has:
     - O-fixed point + 3 X points: isotropic, flux +1;
     - 4 points (π/4)(±1,±1,±1): isotropic, flux −1;
     - 12 points (π/4)(1,1,0): uniaxial (2.4943, 1.5813, 1.5813), flux +1;
     - 12 points (π/4)(1,0,0): uniaxial, flux −1.

     Net chirality is 0, and is argued forced (zero 3-winding for products of a diagonal shift, reflections and constants). Remove "anomalous Floquet".
   - (c) **"None clean" is weak evidence**, since X crossings can be harmless taste copies. The best word, S2.L202.S2.L020, has exact nodal lines at E = 0 and 12 uniaxial nodes. B17 failure is established only for the censused words.
6. **Prior art.** Add:
   - Bedaque–Buchoff–Tiburzi–Walker-Loud 2008;
   - Kluberg-Stern–Morel–Napoly–Petersson 1983; van den Doel–Smit 1983;
   - Bessho–Sato 2021;
   - Wen 2002 and Essin–Hermele 2013 (PSG).
