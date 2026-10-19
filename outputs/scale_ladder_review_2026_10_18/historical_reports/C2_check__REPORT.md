# C2 check: does closure fix the seagull and the induced 1/G?

Provenance: a fresh-context checker of the same model family; not independent. Saved by the supervisor from the hand-back.

**Totals: PASS=13 FAIL=0.**

| Runner | Result |
|---|---|
| ck1_homogeneous_lemma | 4/0 |
| ck2_heatkernel | 4/0 |
| ck3_lattice | 4/0 |
| ck4_jordan_frame | 1/0 |

Two first-run checker bugs are logged (a normalisation bug and a sign bug). No criterion was changed between runs.

## Verdicts

1. **Continuum closure: confirmed.**
   - The homogeneous lemma holds in a stronger form: non-isotropic, 516 monomials, null space 0. Controls pass, and the "arbitrary N" quantifier is load-bearing.
   - **Scope:** uniqueness holds within the ≤ 2-derivative ansatz. With 4 derivatives, √g Ric²φ² is free (harmless at k²). But covariant dim-6 h-linear couplings such as R(∂φ)² are closure-compatible.
   - The Jordan-frame direction is derived exactly as a canonical point transformation, (ζ, cp, w, y1, y2) = (2sK, −4sK, 4s, 2s, −s). So ζ = 0 is a frame premise.
2. **Seagull and Sakharov coefficient: confirmed, with three corrections.**
   - The minimal seagull carries no ∂h, so its tadpole is Π(0).
   - a1 = (1/6 − ζ)R from the S⁴ spectrum. With Λ² := 1/s_min, 1/(16πG) = (1 − 6ζ)Λ²/(192π²). The convention-free form is (1/6 − ζ)⟨φ²⟩/2 for any Schwinger-type covariant regulator.
   - The flat-measure Hessian breaks Ward, already at k⁰.
   - **(a)** Covariant dim-6 scalar couplings (c6 a²/2)√g R(∂φ)² shift 1/(16πG) by −6c6(aΛ)² × the Sakharov value. They are allowed by closure and by Ward, and the shift is O(1) on a lattice.
   - **(b)** The fermion seagull has a k-dependent axial part, ω^(2) ~ h∂h, whose tadpole vanishes by parity (argued).
   - **(c)** G ≈ 1.54 a² (m → 0), 1.64 a² (m = 0.5), 1.88 a² (m = 1). The lattice c_EH values are −0.43 to +0.36 times this reference.
3. **Lattice: numerics confirmed; reframing needed.**
   - Position-space exact log det on 6⁴ matches C2's Π(K) to 1.9e−7. The Fierz–Pauli normalisation is confirmed, and the logged numbers are reproduced.
   - M1 − M2 is the bond placement tadpole (residual 3e−6), with EH projection +0.745 × the covariant reference.
   - **Reframing.** M1 equals M2 after re-identifying h → h + Q(h, h), with Q = O(a²∂h∂h). With a nonzero tadpole such a re-identification can add any hypercubic form to the k² symbol. So the Ward ratio and c_EH depend on the site-h identification; L3 and L6 hold only in that identification.
   - The physical conclusion survives either way. If a bare cosmological term cancels τ, the difference becomes a genuine O(Λ²) term in the action. If not, the off-shell coefficient is not invariant under field redefinitions.
4. **Framing.**
   - Closure at any order cannot fix 1/G. The robust witness is the dim-6 couplings: covariant, closure-compatible, Ward-respecting, and an O(1) shift.
   - An exact lattice Ward identity would fix at most the 8 non-covariant directions.
   - **What could fix 1/G:**
     - the complete microscopic lattice action;
     - spectral sum rules (Frolov–Fursaev–Zelnikov / Pauli–Villars boson–fermion cancellation);
     - a perfect-action / RG fixed-point principle, which depends on the blocking kernel.
   - **Prior art to add:** Dittrich 2008; Bahr–Dittrich 2009; Gambini–Pullin; Teitelboim 1973; Kuchař; EFT field-redefinition shifts; Jacobson.

## Edits applied to FINDINGS

- The ≤ 2-derivative scope.
- Dim-6 couplings as the main reason closure cannot fix 1/G.
- The site-h identification reframing.
- The fermion axial seagull.
- The mass range of the G estimate.
- The k⁰ break.
- B14 E5 cited.
