# C6 check: rung 0 to rung 1 (the corner model)

Provenance: a fresh-context checker of the same model family. Its code is new: geometry, a galois GF(2) solver, a BFS PSG and Bloch sums. Saved by the supervisor from the hand-back.

**Totals: 23 PASS, 0 FAIL** (chk_A 13, chk_B 6, chk_C 4).

**Verdict.** The headline holds: no map is derived, and the clauses are supplied. A1, A4 and the ν = 1 energetics reproduce. The registration lemma is correct once restated, and it does not need finitarity. Three statements were overstated.

## Verdicts

1. **Clause list: confirmed**, with file and line citations.
   - Corner-code note: line 4, lines 24 and 40–47.
   - Long-wavelength note: lines 59–70, 81 and 109.
   - Scale-ladder note: lines 122, 128 and 474.
   - Add two clauses: the supplied U(1)-twisted rotation realization W, and the supplied hopping family.
2. **A1: confirmed.**
   - L = 3: rank + 3 = 649 = E − V + 1; only the 8 patterns with square = plaquette are solvable.
   - L = 4: all 16 are solvable.
3. **A2: confirmed and strengthened.**
   - Sign flips act transitively on consistent configurations, so every one is the bare sector of some convention.
   - The PSG exists for all 16 uniform patterns, so symmetry cannot select the flux.
   - The "canonical BK" observation is weak: it is L = 3 only, with a non-covariant labelling.
4. **A3: confirmed.**
5. **A4: confirmed** by a different PSG method. C4⁴ = −1 ⇔ square = π, Tx and Ty commute ⇔ square = plaquette, and the targets give {1011, 1111}. The fixed momenta are gauge-dependent in form.
6. **"π through every face": confirmed,** for t1 = −1 with the real background (λ = 0). Call it gauge-invariant in the standard convention, not "convention-free". With the chiral term the triangle phase is π + 3 arctan λ.
7. **ν = 1 energetics: confirmed** to 5e−5.
   - 1111 ranks 15/16 (+1.854) at t2 = 0.2, and 16/16 (+1.514) at t2 = 1.
   - With the chiral term, 1011 ranks 6/16.
   - The 0000 vs 0010 order at t2 = 0.2 is unresolved.
   - **Correction:** "descent goes to near flux-free" is inaccurate. Squares and triangles go to about 0, but plaquette (~0.5) and tube (~0.3) remain.
8. **Dimension bound: correct as a density bound** (12 qubits per coarse site).
   - Index m ≥ 12 holds only for registered embeddings. The smallest O-invariant index ≥ 12 is 16.
   - **"No fine-translation-covariant encoding exists" is NOT proved:** fractional-translation encodings, like a TI chain blocked by 12, are not excluded. That is an open route.
9. **Registration lemma: correct, and strengthened.**
   - **Setting:** ω iid on Z³, and X = Φ(ω) any measurable equivariant factor; finitarity is not needed.
   - **Claim 1:** no a.s. measurable o: Ω → Z³/Λ with o∘T^v = o − v, for any index m ≥ 2.
   - **Claim 2:** none into R³/Λ′ either, by weak mixing, so there are no Bragg peaks off 2πZ³.
   - **Hypotheses are load-bearing:** an empty start and a translation-covariant rule. B3's Definition 1 allows a periodic deterministic B or a y-dependent rule, and each registers trivially (controls in chk_C).
   - **Not excluded:** polycrystals, defective registration, amorphous packings, fractional-translation encodings, emergent quasiparticles.
   - The quantum version (TI finite-depth circuits from TI product states) is confirmed.
10. **"Formation cannot produce the coarse rung at all": overstated.** Restrict it to covariant rules from an empty start. The radius-0 writing of the flux background presupposes a y-dependent, hence registering, rule.
11. **The c6_C illustration** is fine as an illustration. "Most block-favouring" is unjustified, and ≤ 0.16 is a finite-size number consistent with zero.
