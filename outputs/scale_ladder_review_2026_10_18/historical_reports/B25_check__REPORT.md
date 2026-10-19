# B25 check

Provenance: a fresh-context checker of the same model family. The model was rebuilt independently in `corelib.py` on `B7_check/chk_core.py`, importing no B2x library; B25's pickles were read only for word lists. Spectra match B25's model on 7 words. Saved by the supervisor from the hand-back.

**Totals: PASS=40 FAIL=0.** Several runs were killed or had bugs; all are logged.

## Verdicts

1. **Index lemma: confirmed and stronger.**
   - **Proof.**
     - Composition stays in G, and the ω bookkeeping closes for the antilinear kinds. The kinds form the Klein group.
     - Λ_ind/Λ_u embeds in (Z₂²)/H, giving index ≤ 4.
     - O acts trivially, because every word satisfies W(Rk + πRλ) = U_R W(k) U_Rᵀ with a k-independent U_R (verified for all 24 rotations), so Rt − t ∈ Λ_u.
     - Compositions were checked numerically.
   - **Lattices.** 13; 74 strictly nested pairs; 8 with trivial O action. On (π/64), 56 of 74 are good (29 of 42 down to π/4). All 8 trivial pairs and all 13 (Λ, Λ) pairs are bad.
   - **Every scale.** It holds at every scale, with exact rational witnesses: (a/2)e_z for (sc, bcc), and (b/2)(0,1,1) for (fcc, sc).
   - **Corrections:**
     - FINDINGS lacks the proof; add it.
     - Say "74 strictly nested; 8 strict admissible pairs plus 13 (Λ, Λ)".
     - "None of the 29 good pairs" should be 56 on the (π/8) range.
     - The quotient embeds in (Z₂²)/H.
2. **Letter rules: confirmed.** "Wᵀ is a palette word" is overstated: σ is not a palette letter. It holds for words without R_L; otherwise σ is inserted around each R_L. Nothing downstream depends on it.
3. **Census and Fourier: confirmed.**
   - An exact Fourier route (all twelve power sums, mod 48/64, finer than B25's detector) matches 19 of 19 stratified words on every attribute.
   - The FAIL word's 3-adic tastes are all U-type, so it is a (Λ, Λ) pair and bad.
   - B25's own p ≤ 3 Fourier check gives a superlattice, so it is a consistency check, not a characterisation.
   - **ALIGN2:** the cyclic mechanism explains only 8 of 28 words. The other 20 use a transpose-cyclic mechanism found by the checker (Gᵀ = ±G). All 28 are explained.
4. **Witnesses:** 4 of 4 reproduced by finite differences over 303 directions. The 64/136/60/28 split is confirmed, except that 8 of the 136 have 8-fold nodes.
5. **Scope: correct.** Conditions: pure translation tastes, U/T/I/K kinds, Λ_sp a lattice, and k-independent point-group unitaries (verified). Precisions:
   - the theorem classifies pairs; ruling out steps also needs pinning, which is observed (225/225), not proved;
   - antiunitary pinning is not counted, which only strengthens the necessary condition.
