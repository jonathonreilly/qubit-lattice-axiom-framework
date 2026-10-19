# Complete corrected argument: Covariant monomial constructions and spectral-square identities

This is inspectable mathematical source. The canonical claim is limited to: Complete stabilizer/displacement/gauge and constructive square arguments in the stated ansatz.

**Deferred continuation:** Terminal exclusions of additional microscopic letters or other nonmonomial families and the old antiunitary sufficiency claim. Complete arguments are retained below, but terminal negative conclusions are not promoted until the required residual-matched packet is supplied and reviewed. This does not make the exact identities uncertain. Historical verification statements below describe the original campaign, not a fresh capture or audit verdict.


# Corner-fermion covariant monomial shift letters are only the diagonal shift powers and their antipodal twins, and the settled momentum-shifting and antiunitary subclasses reduce to old words

**Date:** 2026-10-18
**Type:** bounded_theorem
**Status:** bounded support, unaudited.
- **Exact:**
  - Theorem 1, the classification of translation-invariant monomial letters (proof below; the two model sign facts are exact finite GF(2) computations);
  - the conjugation identities, the even-A reduction and the D± swap;
  - Theorem 4 (momentum-shifting letters) in the subclasses it lists: the Q statement for every Q, the D_Π reduction, the doubled-cell orbits and range-0 letters (exhaustive), the pure-permutation reduction and the a·R_L·b lemma;
  - Proposition 5 (antiunitary letters), given the palette proviso;
  - the exclusion of exp(π/4·A0), the E± identities, the relation W(k+Π) = (−1)^{n_R}W′(k) and its breaking by the witness E₊·S.
- **Numerical (sample statements):** the spectral Π-taste of E-words, and the breaking of the exact Π relation in every sampled reduced E-word.
- **By hand or worker-only, not rechecked:** the Q-multiplet paragraph (Theorem 4(c)) and the C8 worker's 20,000-word mixed-word sample.
- **Cited, not re-run:** the B26 and C8 screens, which are negative numerical searches, not no-go theorems.

Nothing is adopted. No physical identification is made.

**Provenance:** campaign blocks B26 and C8 of the scale-ladder campaign (2026-10-18).
- B26: drafted by a same-model-family worker; checked by a fresh-context same-family agent on its own from-scratch model build (`B26_check`, PASS = 47).
- C8: drafted by a same-model-family worker, who imported the B26 worker's model chain read-only (so not an independent build); checked by a fresh-context same-family agent (`C8_check`, PASS = 49), who reused the B26 checker's model build unchanged and wrote new code on it. The two checks therefore share one model build.
- Written up, with a consolidated self-contained runner, by the campaign supervisor's delegate, also same-family. The checks' corrections are applied here.
- Reviewed by a fresh-context same-family agent (`NOTE_B26C8_review`), whose scoped edits are applied here.

None of these is an independent human reviewer.

## Question

The campaign's step letters at the full-octahedral node are S, R_L and symmetric on-site unitaries (eight-node step note (`outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18_full_argument.md`)). Can the palette be enlarged by letters of other kinds?

- **B26:** other shift letters, i.e. translation-invariant monomial letters covariant up to a character.
- **C8:** letters outside that class: momentum-shifting letters (class 1), antiunitary letters (class 2) and non-permutation letters (class 3).

The question is what each class contains exactly, and whether it adds anything beyond the old words.

## Setting

- **Model.** The corner fermion of the companion notes: 12 corner modes c = {d, e} (d ⊥ e unit vectors) per site of Z³, with f_c = d + e.
  - **Hops.** On-site {a,b} ↔ {a,f}; links {a,b}@v ↔ {−a,b}@v + a.
  - **Flux.** square = plaquette = tube = π and triangle = 0, in a translation-invariant Z₂ gauge u.
  - **Lifts.** For each proper rotation R (24 of them), a gauge-dressed lift G_R|v,c⟩ = (−1)^{λ_R·v + τ_R(c)}|Rv, Rc⟩. Here (λ_R, τ_R) solves the projective-symmetry equations over GF(2), and is unique up to the global sign.
- **Operators.** Translation-invariant operators are block dicts a ↦ X_a with X|v,c⟩ = Σ_a |v+a⟩X_a|c⟩ and Bloch matrix X(k) = Σ_a X_a e^{ik·a}. Conjugation by G_R sends X_a to (−1)^{λ_R·a} U_R X_a U_Rᵀ, at displacement Ra.
- **Letters used.**
  - **S,** the diagonal shift {d,e}@v → ±{d,e}@v + f_c, with signs fixed by covariance. S^t for t ∈ Z.
  - **A0,** the on-site antipodal map {c} → ±{−c}, an A2 letter (real, A0² = −1).
  - **A_a = A0·S^a.**
  - **R_L = H_link/√2,** the link reflection (R_L² = 1).
  - **Rt := A0·R_L·A0⁻¹.**
  - **H_on** (on-site hopping) and **Λ** (chiral triangle operator), both k-independent.
  - **Symmetric on-site letters,** from the 6-dimensional commutant of the U_R. The Clifford palette PC (80 letters) consists of the projector sums P₀ + i^aP₁ + i^bP₂ over H_on eigenprojectors and P₀ + i^aP₁ + i^bP₂ + i^cP₃ over Λ eigenprojectors.
  - **E± = exp(±iπ/4·R_L) = (1 ± iR_L)/√2.**
  - **D_Q = e^{iQ·x}** for Q ∈ R³/2πZ³; D_Π with Π = π(1,1,1).
- **Old words.** Products of S^p, R_L and symmetric on-site letters. The "old palette" adds Rt, which is −S·R_L·S⁻¹ (identity (I3) below).
- **Momenta.** k* = (π/2)(1, −1, 1) and −k*, the two O-fixed momenta (long-wavelength note (`docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`)).
- **Doublets.** D₊ = {H_on = 2, Λ = −2√2} and D₋ = {H_on = 2, Λ = +2√2}.
- **Covariance.** A letter X is O-covariant up to χ if G_g X G_g⁻¹ = χ(g)X for all 24 g.

## Theorem 1 (B26): the covariant monomial shift letters

**Statement.** Let X be a nonzero translation-invariant operator that is monomial: each column of the real-space matrix has exactly one nonzero entry. No bound is put on its displacement, and its coefficients may be any nonzero complex numbers. Suppose G_g X G_g⁻¹ = χ(g)X for all 24 proper rotations, with χ(g) ∈ C^×. Then:
- χ = A1 or χ = A2;
- if χ = A1, X = z·S^t for some z ∈ C^× and t ∈ Z;
- if χ = A2, X = z·A0·S^t for some z ∈ C^× and t ∈ Z.

Conversely, every z·S^t is A1 and every z·A0·S^t is A2. X is unitary iff |z| = 1.

**Model facts used (exact; runner 1.3–1.5).** For every corner c, let h_c be the nontrivial element of Stab_O(c).
- **(F-a)** λ_{h_c}·f_c is even.
- **(F-b)** τ_{h_c}(c) + τ_{h_c}(−c) is odd.

Both parities are gauge-invariant. Under a translation-invariant gauge change (−1)^{μ·v + ε(c)}, the lift of h becomes (λ_h + μ + R_hᵀμ, τ_h(c) + ε(c) + ε(R_h c)), up to the global sign. So λ_h·f_c changes by 2μ·f_c, because h fixes f_c, and τ_h(c) + τ_h(−c) changes by 2ε(c) + 2ε(−c) (plus 2 for a global sign flip), because h fixes c and −c. The runner confirms the parities on three random gauges. Every translation-invariant solution of the flux equations is gauge-equivalent to u (loop rank 22 = 36 − 14, runner 0.1), so (F-a) and (F-b) are properties of the model, not of the gauge.

**Proof.**
1. **The lifts compose up to a global sign.** Δ = G_g G_h G_gh⁻¹ is diagonal, of the form (−1)^{μ·v + ε(c)}. The PSG equations say that each lift maps every hopping term onto its rotated image with the correct sign. Δ covers the identity rotation, so it maps every hopping term to itself and preserves every edge sign, i.e. Δ takes the same value on the two ends of every edge. The hopping graph is connected: on-site edges connect the 12 corners, and links run along all three axes. So Δ is a constant ±1.

   Hence Ad(G) is a true representation, and χ(g)χ(h)X = χ(gh)X with X ≠ 0. So χ is a homomorphism O → C^×. The commutator subgroup of O is T = ker A2, of order 12 (runner 1.2), so χ ∈ {A1, A2}.
2. **One column fixes X.** Write X|0,c⟩ = z|a, i⟩ for one corner c. From G_g|0,c⟩ = (−1)^{τ_g(c)}|0, Rc⟩ and covariance,

   X|0, Rc⟩ = χ(g)⁻¹·z·(−1)^{τ_g(c) + λ_g·a + τ_g(i)}·|Ra, Ri⟩.

   O is transitive on the 12 corners, and X is translation-invariant, so this one column determines X.
3. **The stabiliser fixes the target.** Stab_O(c) = {1, h_c}, with h_c the C2′ rotation about f_c (runner 1.3). Taking g = h_c in step 2, the single nonzero entry of the column must be h_c-fixed: i ∈ {c, −c} and a ∈ Z·f_c. Indeed, h_c swaps d and e and negates the third axis, so its fixed corners are exactly c and −c, and its fixed lattice vectors are t·f_c, since f_c is primitive. Step 2 then also gives

   χ(h_c) = (−1)^{τ_h(c) + λ_h·a + τ_h(i)}.
4. **The character.** By (F-a), (−1)^{λ_h·t f_c} = 1 for every t.
   - If i = c, then χ(h_c) = +1. Since A2(h_c) = −1 (h_c is a transposition of two axes), χ = A1.
   - If i = −c, then by (F-b) χ(h_c) = −1, so χ = A2.
5. **Existence.** S^t has support c → c at displacement t·f_c. A0·S^t has support c → −c at the same displacement: A0 S^t maps c@0 to c@t f_c and then to −c@t f_c. Both are covariant with the stated characters (runner 1.8). By steps 2–4, X is z times one of them. ∎

**Remarks.**
- No range or entry restriction is used. B26's restriction to entries in {±1, ±i} is unnecessary.
- By Frobenius reciprocity, each 12-dimensional support space (c → ±c at displacement t·f_c) carries exactly one of A1 and A2. The multiplicities are (1, 0) for c → c and (0, 1) for c → −c (runner 1.6).
- The class is narrow. It excludes R_L, a two-term sum, and every on-site letter except multiples of 1 and A0.

**Enumeration (runner 1.7; a different algorithm from the B26 check's orbit propagation).** Take every single-entry seed |a, i⟩⟨0, c_xy| with displacement a in the box [−R, R]³. Average it twistedly over O, (1/24)Σ_g χ(g) G_g E G_g⁻¹, for both characters, and keep the monomial results.

| Range R (sup norm) | Seeds | Monomial letters | Identified as |
|---|---|---|---|
| ≤ 1 | 324 | 6 | z S^t, z A0 S^t, \|t\| ≤ 1 |
| ≤ 2 | 1,500 | 10 | \|t\| ≤ 2 |
| ≤ 3 | 4,116 | 14 | \|t\| ≤ 3 |
| ≤ 4 (`--slow`) | 8,748 | 18 | \|t\| ≤ 4 |

The other averages vanish (the stabiliser sign is wrong) or are not monomial (the seed is not h_c-fixed). The B26 worker found the range ≤ 2 count with group averages, and the B26 check found all four counts by orbit propagation.

## Identities, the even-A reduction and the D± swap (exact)

**Identities** (runner 2.1–2.5, exact block-dict equalities with residual ≤ 2e−16):
- **(I1)** A0 S^p A0⁻¹ = S^{−p} (checked for p = 1, 2, 3). A0 S A0⁻¹ has support −c → −c at displacement f_c = −f_{−c}, so Theorem 1 already gives it as z·S⁻¹; the runner fixes z = 1.
- **(I2)** A0² = −1, in A0's real normalisation; (iA0)² = +1.
- **(I3)** A0 R_L A0⁻¹ = −S R_L S⁻¹. The alternatives −S⁻¹R_LS and +SR_LS⁻¹ fail, with residuals 0.71 and 1.41. With the definition of Rt, (I3) reads Rt = −S R_L S⁻¹.
- **(I4)** A0 Rt A0⁻¹ = +R_L. This follows from (I2), since A0² is a scalar.
- **(I5)** S⁻¹ Rt S = −R_L, a restatement of (I3).
- **(I6)** A0 H_on A0⁻¹ = H_on.
- **(I7)** A0 Λ A0⁻¹ = −Λ.

Also: Rt² = 1, Rt is Hermitian, and Rt ≠ ±R_L. A0 maps PC onto itself up to phases in {±1, ±i}, and maps the 6-dimensional symmetric on-site algebra into itself (runner 2.6).

**Even-A reduction.** In a word whose product of characters is A1, the A letters occur in even number, so they can be paired. For each pair, using (I2),

A_a·X·A_b = A0 S^a X A0⁻¹·A0²·S^b = −S^{−a}·X̃·S^b, with X̃ = A0 X A0⁻¹.

By (I1), (I3), (I4) and (I6), the dual X̃ of an A-free word X has the letters
- S^p → S^{−p};
- R_L → Rt = −S R_L S⁻¹;
- Rt → R_L;
- on-site o → A0 o A0⁻¹, again a symmetric on-site letter.

So **every even-A word equals z × a word in S^p, R_L and symmetric on-site letters**, with:
- z = ±1 if arbitrary symmetric on-site letters are allowed;
- z ∈ {±1, ±i} if the fills must stay normalised PC letters.

The reduced word's total S power is n_eff = Σ_p (−1)^{#A0 to the left}·p, with the A0 inside A_a counted to the left of its own S^a. The reduced word is often longer or reordered, and can contain S^{±3} (see the screen caveat below).

Runner 2.7 checks this on 300 random words with 2 or 4 A letters (600 with `--slow`); the maximum deviation is 7e−16, and the S power is checked against n_eff. Runner 2.8 checks the pair formula for all a, b ∈ −2…2.

**D± swap.** Every A_a maps D₊ onto D₋ and D₋ onto D₊ at both ±k*. The A1 letters S, R_L, Rt, H_on, Λ and symmetric on-site letters are scalars on each of D₊ and D₋ (runner 2.9). This is Schur's lemma for an A2 letter, since D₋ ≅ A2 ⊗ D₊.

By the per-letter speed lemma of the C11 speed-law note (`outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_generalised_speed_law_per_letter_additivity_2026_10_18_full_argument.md`), an A2 letter contributes only a label swap, so the A letters are no new velocity source. The k* speed of an even-A word is |n_eff|·√2/3.

## Theorem 4 (C8 class 1): momentum-shifting letters

**(a) Only Q ∈ {0, Π}, for every Q (exact).** Let X ≠ 0 satisfy T_v X T_v⁻¹ = e^{iQ·v}X for all v ∈ Z³, and G_g X G_g⁻¹ = χ(g)X for all g.
- From the form of the lifts, G_g T_w G_g⁻¹ = (−1)^{λ_g·w}·T_{R_g w}. The sign cancels in conjugation, so G_g X G_g⁻¹ has translation character R_gQ.
- Covariance then forces R_gQ ≡ Q mod 2π for all g.
- C4 about the z axis gives Q₁ ≡ −Q₂ and Q₂ ≡ Q₁, so 2Q₁ ≡ 0 and Q₂ ≡ Q₁. The same holds about the x axis. So Q = (q, q, q) with q ∈ {0, π}.

The runner scans the (π/8)Z³ and (π/12)Z³ grids and finds exactly 0 and Π (runner 3.1).

Every such X is D_Q·Y with Y translation-invariant. G_g D_Q G_g⁻¹ = D_{RQ} exactly; this is runner 3.2 for the 8 Q in π{0,1}³, whose O-orbits have sizes 1, 1, 3, 3. So D_Π is O-invariant, and Y has the same covariance as X. For monomial X, Theorem 1 then gives the **Q = Π letters z·D_Π·S^a and z·D_Π·A0·S^a**.

**(b) D_Π relations and the Π-taste (exact).**
- D_Π commutes with S, because f_c has even coordinate sum, so Π·f_c ∈ 2πZ.
- D_Π commutes with A0 and with every on-site letter.
- D_Π anticommutes with R_L and Rt, which hop by unit vectors.

(Runner 3.3, on the L = 4 torus.) Moving every D_Π to the left therefore costs a sign. A word in these letters and D_Π is ±D_Π^m × (word without D_Π), and it is translation-invariant iff m is even, since D_Π² = 1. So it is ± a word in the old letters and A0, and, when its character is A1, z times an old word by the even-A reduction.

In Bloch form, D_Π W D_Π = (−1)^{n_R}W reads W(k+Π) = (−1)^{n_R}W(k), with n_R the number of R_L and Rt letters (runner 3.4, 200 random words). Since k* + Π ≡ −k*, **this is the known Π-taste** of every old word (campaign blocks B18 and B20).

**(c) Q-multiplets (by hand, C8 worker; not rechecked).** A letter whose Q lies in a 3-element orbit is only D4-covariant, and there are infinitely many at every range. An O-covariant step needs the whole multiplet, i.e. a doubled-cell letter.

**(d) Doubled-cell letters (exact; Q ∈ π{0,1}³, monomial letters).** These are phased permutations commuting with the 2Z³ translations and O-covariant up to a character. Runner 3.5–3.7 works on the L = 4 torus with the 192 signed permutations of O × (2Z/4Z)³.
- **Orbits.** There are 6 mode orbits per doubled cell:
  - four of 12 modes with stabiliser {1, C2′}: sublattice 000, sublattice 111, and the corners perpendicular to the distinguished axis on the 100-type and 110-type sublattices;
  - two free orbits of 24 modes: the corners parallel to that axis.
- **Pieces.** The covariant pieces were found by orbit propagation.
  - A C2′ orbit goes to the same or the antipodal corner, and its stabiliser sign fixes the character.
  - A free orbit goes to any free-orbit mode, with either character.
  - At range ≤ 1 there are 6 pieces per C2′ orbit and 336 per free orbit. At range 0 there is one per character on each C2′ orbit (identity for A1, antipodal for A2), and 8 per character on each free orbit.
- **G0** is the set of range-0 doubled-cell letters: 2 characters × 8² free-orbit choices × 4⁶ ℤ₄ orbit phases = 524,288 letters. Exactly one perm part per character is sublattice-independent, and **exactly 8 letters are translation-invariant: z·1 and z·A0**, z ∈ {±1, ±i}.
- **Pure-permutation words (exact, any range, any cell).** A product of monomial letters is monomial and covariant. If it is translation-invariant, Theorem 1 makes it z·S^a or z·A0·S^a.

**(e) The a·R_L·b lemma (exact; runner 3.8).** For a, b ∈ G0, the translation-invariant products a·R_L·b are exactly z·{R_L, Rt, A0·R_L, R_L·A0}. Here z ∈ {±1, ±i} with ℤ₄ orbit phases, and z ∈ U(1) with U(1) orbit phases.
- **Support.** R_L has two nonzero entries per column, at the unit displacements along the two directions of the column's corner. Among all 128² = 16,384 pairs of perm parts, exactly 4 give a translation-invariant support, namely those with both perm parts sublattice-independent. The check found the same count with a different implementation.
- **Phases.** For each admissible pair, translation invariance is a linear system Ax ≡ C/2 mod 1 on the 12 orbit phases, x in units of 2π.
  - The Smith invariants of A are all 1 (rank 7), so the homogeneous solutions are Z¹² + ker_R(A).
  - Every real-kernel direction moves all entries of the word by one common phase.
  - So the U(1) solutions give one word per pair up to a scalar. The runner confirms this on random U(1) solutions.
  - Enumerating the ℤ₄ solutions (64 per pair) times global ℤ₄ phases gives exactly 16 words: R_L, A0·R_L, R_L·A0 and Rt, the last from A0·R_L·A0 = −Rt.

  It follows that every translation-invariant conjugate P·R_L·P⁻¹ with P ∈ G0 is ±R_L or ±Rt (C8 and its check, by Hermiticity; not re-run here).

**Not settled in class 1:**
- longer range-0 mixed words with two or more link letters (C8 sampled 20,000 words of the form M·g·M·g·M; 3 were translation-invariant with non-invariant G0 letters, all of old type; worker only, not rechecked);
- displaced (range ≥ 1) doubled-cell letters, the only class-1 route to k-dependent intertwiners;
- multiplets with Q outside π{0,1}³;
- non-monomial doubled-cell letters.

## Proposition 5 (C8 class 2): antiunitary letters

- **No quasi-energy.** An antiunitary U = V·K, with K complex conjugation in the real-space mode basis, has no quasi-energy. If Uψ = λψ, then U(e^{iθ}ψ) = e^{−2iθ}λ·(e^{iθ}ψ), so its eigenvalue phases can be rotated at will. Only U² = V·V* is a sensible step.
- **Reality of the letters.** S, R_L, Rt, A0 and all 48 dressed lift matrices are real (runner 4.1).
- **The square.** PC is closed under complex conjugation up to phases in {±1, ±i} (runner 4.2). Hence, **if V is a word in a conjugation-closed palette**, V* is the same word with conjugated slots (runner 4.3, 100 random words), and U² is an old-palette word up to a phase.
- **A necessary spectral constraint** is the pairing spec U²(−k) = conj spec U²(k) (runner 4.4). It holds because K(VV*)K = V*V = V⁻¹(VV*)V.
- At a momentum fixed by conjugation, det(V conjugate(V)) = |det V|² = 1, and its −1 eigenspace has even dimension: the antiunitary restriction there squares to −1. Thus conjugate spectral pairing alone is not sufficient (diag(−1,1,…,1) is a counterexample). The explicit square construction above is retained.
- **Proviso.** Antiunitary steps with V outside a conjugation-closed palette are open.

## Proposition 6 (C8 class 3): non-permutation letters

- **The form of a π/4 exponential.** For a unitary X, (1 + iX)/√2 is unitary iff X is Hermitian, i.e. X² = +1. For a real X with X² = −1, the unitary is exp(π/4·X) = (1 + X)/√2.
- **A0 and A_a (exact).** A_a² = −1, and G_g exp(θA_a) G_g⁻¹ = exp(χ(g)θA_a). So exp(π/4·A_a) is covariant up to a phase exactly for the 12 rotations of ker A2 = T: it is **only T-covariant** (runner 5.1, a = 0, 1, 2).
- **S^a** (a ≠ 0) is not an involution (runner 5.2).
- **On-site involutions.** exp(iπ/4(1 − 2P)) for every sum P of H_on or Λ eigenprojectors lies in PC up to a phase (runner 5.3). Other on-site involutions stay in the 6-dimensional on-site algebra, which is already a letter class.
- **E± = exp(±iπ/4·R_L) (exact; runner 5.4–5.7).**
  - E₊E₋ = 1, E₊² = iR_L and E₊R_L = iE₋, all from R_L² = 1.
  - E± is O-symmetric and translation-invariant, but not monomial: 3 nonzeros per column, with moduli 1/√2 and 1/2.
  - exp(±iπ/4·Rt) = S·E∓·S⁻¹ by (I3), so it is nothing new.
  - R_L(k+Π) = −R_L(k), so E±(k+Π) = E∓(k); also E(k)ᵀ = E(−k).
- **Broken exact Π relation (exact for the witness; sampled otherwise).** For an E-word, W(k+Π) = (−1)^{n_R}·W′(k), with W′ the word with E₊ ↔ E₋ swapped (exact). The relation W(k+Π) = ±W(k) of old words fails: for the witness E₊·S the residual is 1.0. It fails for every sampled reduced E-word (79/79 by default, 112/112 with `--slow`; runner 5.8), a sample count. In the sample it survives only in non-reduced words (22 of 112 by default, 45 of 126 with `--slow`), e.g. words whose E letters merge, E₊E₊ = iR_L. So −k* is no longer guaranteed to be a copy of k* at the operator level.
- **"Reduced"** here and below means the runner's local filter `hygienic()`: no cyclically adjacent pair that merges or cancels (E–E, E–R_L, R_L–E, R_L–R_L, Rt–Rt, S–S⁻¹, S⁻¹–S) and no adjacent slots. The filter was fixed after the first runs (see Criterion changes disclosed). It is local, not a full reduction: the E-free word E₊·S⁻¹·Rt·S·E₊·S = −i·S passes it (review probe). The sample counts are for the filter as written.
- **Surviving spectral Π-taste (numerical).** spec W(k+Π) = ω·spec W(k) with ω = ±1 holds in all sampled slot-free reduced E-words, i.e. words in S^{±1}, S², R_L, Rt and E± (80/80; 160/160 with `--slow`). It fails in all sampled reduced E-words with one or more generic symmetric on-site slots (0/80 kept; 0/160). The C8 check found 167/167 and 133/133. This is a sample statement. The check attributes the survival to the reality of every letter, but no proof is given here.
- **Scope of "new".** Among the π/4 exponentials examined (of A0, A_a, S^a, on-site involutions, R_L, Rt and D_Π), **E± is the only new letter**.
  - exp(iπ/4·D_Π) = F gives nothing (runner 5.11). F² = iD_Π, F·R_L = R_L·F⁻¹ and F·S = S·F, so words reduce to (old word)·F^m, which is translation-invariant only when F^m = ±1. F itself is not translation-invariant.
  - Conjugates g·E₊·g⁻¹ by old words g are already words.
  - No nontrivial symmetric on-site projector P gives a Hermitian involution R_L·P + (1 − P), since Hermiticity needs [R_L, P] = 0 (runner 5.13: the on-site commutant of R_L(k) is the scalars).
  - The C8 check found no further non-conjugate parameter-free involution, but its search was not exhaustive.
- **exp(iθR_L).** For θ ∈ (π/6)Z this is a further parameter-free O-symmetric letter, on the same footing as the π/6 on-site fills. For θ = π/6 it is not z·E₊ⁿ (1 and R_L are linearly independent), and it flips under k → k + Π (runner 5.10). **It was not screened.**
- **No velocity source.** E±, exp(iπ/6·R_L) and R_L are scalars on D₊ and D₋ at ±k*, with zero compressed derivative (runner 5.12). By the C11 lemma they contribute nothing to the k* speed.

## Screens (cited; negative numerical searches, not re-run, not no-go theorems)

Both screens use the campaign's single-node criterion (blocks B20 and B23):
- an exact 2-fold D± or 4-fold D₊ ⊕ D₋ level at k*;
- a sign test of r(k) on 8³ and then 16³ grids;
- for survivors, the nodes on (π/4)Z³ plus 40 Nelder–Mead starts, classified by degenerate perturbation theory.

The searches report what was tried and found nothing passing. They do not exclude other words, fills or lengths.

- **B26** (letters A_a with one or two Clifford slots).
  - **Family.** Words in S^{±1}, S^{±2}, R_L and Rt, of length ≤ 5. Classes are reduced modulo cyclic S cancellation and A0-duality, and kept only if they are not among the earlier B20/B23 skeletons and have n_S ≠ 0. This leaves 74 one-slot and 40 two-slot classes.
  - **Fills.** About 73k words.
  - **Result.** 88,998 (word, level) pairs: 86,599 fail the sign test, 2,399 survive it, and **0 pass**.
  - **Check.** The B26 check confirmed 40/40 sampled records.
  - **Coverage caveat (B26 check).** The family does not cover every even-A word of length ≤ 5. Some reduce to S^{±3}: A_2·S·o₁·A_0·o₂ = −S⁻³·õ₁·o₂ and A_1·S²·o₁·A_1·o₂ = −S⁻³·õ₁·S·o₂. A_0 letters can also make on-site slots adjacent, and products such as L·H are not in the palette screened.
- **C8** (E-words).
  - **Family.** Words in S^{±1}, S^{±2}, R_L, Rt and E±, with at least one E, n_S ≠ 0, length ≤ 5 and one or two Clifford slots. Reduced modulo cyclic rotation and complex conjugation, this leaves 348 one-slot and 84 two-slot classes.
  - **Fills.** 60,832 words.
  - **Result.** 69,660 levels: 69,021 fail the sign test, 639 survive it, and **0 pass**.
  - **Check.** The C8 check confirmed 38/38 sampled records. It corrected the −k* label of the 180 8-fold survivors to 89 with an exact linear-order flat direction and 91 genuinely anisotropic. The censuses of the closest cases are lower bounds; the check finds 59 defective nodes for E₊·S·L033.

## Scope

- **Theorem 1** covers translation-invariant monomial letters, exactly and at any range. It does not cover:
  - non-monomial letters, except the exponentials of Proposition 6;
  - O_h letters with inversion characters;
  - letters covariant under a subgroup only.
- **Theorem 4** settles (these are the "settled momentum-shifting subclasses" of the title):
  - single-Q letters, for every Q;
  - Q = Π monomial letters;
  - doubled-cell monomial letters for Q ∈ π{0,1}³ at the orbit and range-0 level;
  - pure-permutation words;
  - one link letter between two G0 letters.
- **Proposition 5** needs V in a conjugation-closed palette (the "settled antiunitary subclass" of the title).
- **Proposition 6** is scoped to the π/4 exponentials listed. The spectral Π-taste statement is numerical.
- **Not part of this note:**
  - B26's and C8's taste censuses (B24 lattices, B25 index lemma);
  - the B26 L1 sample;
  - the C8 remark that symmetric letters only rescale the k* speed, which the C11 lemma now proves for every C¹ letter at isolated 2-fold levels.
- No physical identification is made.

## Open

From the B26 and C8 reports and findings:
- S^{±3} and S^{±4} skeletons and adjacent-slot cases that even-A words generate at length ≤ 5 (screen coverage).
- O_h letters with inversion characters; letters covariant under subgroups only, including T-only steps with exp(π/4·A0), where D₊ and D₋ can mix.
- Non-monomial unitary letters of range ≥ 1 that combine S, A and link hops.
- Displaced (range ≥ 1) doubled-cell letters, and mixed words with them (k-dependent intertwiners).
- Longer range-0 mixed words with two or more link letters (sampled only).
- Momentum-shift multiplets with Q outside π{0,1}³ (larger cells); non-monomial doubled-cell letters.
- Non-conjugate O-symmetric Hermitian involutions beyond those probed; exponentials of on-site involutions in the M₂ block.
- Antiunitary steps with V outside a conjugation-closed palette.
- exp(iθR_L) at other rational angles (not screened).
- Words longer than 5, unsampled length-5 fills, π/6 fills on these skeletons, and G3/2 levels, in both screens.
- A proof, or a counterexample, for the spectral Π-taste of slot-free E-words.
- An independent check from a different model family, or a human reviewer.

## Premises

- **Axioms used.** Lattice Z³, unit translations, and cube rotations about sites (axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)).
- **Supplied.** The corner model, its flux pattern and gauge; the letter classes (monomial, momentum-shifting, doubled-cell, antiunitary, π/4 exponentials); the palettes PC and the symmetric on-site algebra.
- **Standard facts.**
  - Characters of O from its abelianisation.
  - Frobenius reciprocity.
  - Smith normal form over Z.
  - Schur's lemma.

## Relation to prior work

Bibliographic details are recalled from memory and were not re-verified for this note.

- **Projective symmetry groups** for gauge-dressed lattice symmetries: X.-G. Wen, Phys. Rev. B 65, 165113 (2002).
- **Fixed-point mechanism.** The argument for Theorem 4(a) is the one behind the pair-momentum statement Q ∈ {0, Π} of the eight-node step note (`outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18_full_argument.md`) (its T2).
- **Antiunitary time steps** without quasi-energy: standard. Only squares of antiunitary operators have a basis-independent spectrum.
- **New here, for this model:**
  - the exact classification of covariant monomial shift letters at any range, with the two sign facts;
  - the A0 identities and the even-A reduction;
  - the doubled-cell orbit structure and the a·R_L·b lemma;
  - the identification of E± as the only new π/4 exponential among those examined, and of its breaking of the exact Π relation.

  The group-theoretic tools are standard.

## Historical packet proposal (promotion deferred)

- **N1, routes not covered.** Listed under Open. The main ones are non-monomial letters of range ≥ 1, displaced doubled-cell letters, larger cells, O_h characters, and antiunitary V outside a conjugation-closed palette.
- **N2/N3, scope.**
  - Theorem 1 is quantified over all translation-invariant monomial letters, every displacement and every nonzero coefficient, under the 24 dressed rotations.
  - Theorem 4 is quantified over the subclasses it lists.
  - Proposition 6's "only new letter" is quantified over the seven exponential families listed, not over all non-monomial letters.
  - The screens are numerical negative searches with stated families and fills.
- **N4, inputs.**
  - The sign facts are exact GF(2) computations.
  - The identities are exact equalities of real (or ±i) block matrices, residuals ≤ 2e−16.
  - The orbit, piece and G0 counts are exhaustive enumerations.
  - The a·R_L·b phases use integer Smith normal forms.
  - The spectral Π-taste is sampled.
- **N5, wording.**
  - "Monomial" means one nonzero entry per column of the real-space matrix.
  - "Old word" means a product of S^p, R_L and symmetric on-site letters, Rt included.
  - "Π-taste" means the relation W(k+Π) = ±W(k) (exact), or spec W(k+Π) = ±spec W(k) (spectral).
  - "New" means not z times a word in the old letters, a conjugate of E±, or an old exponential.
- **N6/N7, strongest objections.**
  - All agents are of one model family.
  - The two checks share one model build, and this runner copies it.
  - The class of Theorem 1 is narrow: it excludes R_L itself.
  - E± and exp(iθR_L) show that non-monomial symmetric letters exist, so "add nothing" is not claimed for class 3.
  - The screens cover a small part of the word space.
- **N8, earlier claims.** No repository note is changed. Campaign-internal statements corrected by the checks are listed below.

## Historical checking narrative (not fresh evidence)

Both checks are fresh-context agents of the same model family; neither is an independent human reviewer. Their code imports no repository code.

**B26 check** (`.claude/science/physics-loops/scale-ladder-campaign-20261018/B26_check/ (unavailable historical pointer; not a proof premise)`: REPORT.md, chk_*.py and logs; PASS = 47, FAIL = 0). It used a from-scratch model build (`mymodel.py`) with its own GF(2) flux and lift solver, built S and A0 by orbit propagation, and read B26 pickles only as data.
- **Confirmed:** the classification (enumeration to range ≤ 4), the identities, the even-A reduction, the D± swap, the k* speed with the sign-flipped n_eff, and the screen spot check.
- **Corrections applied here:**
  1. the two sign facts in the proof;
  2. the projective-sign wording;
  3. the real normalisation of A0²;
  4. the Rt identities;
  5. the reduction prefactor z;
  6. the norm convention;
  7. the screen coverage;
  8. the open items.

**C8 check** (`.../C8_check/`: REPORT.md, chk_*.py and logs; PASS = 49, FAIL = 0). It reused the B26 checker's `mymodel.py` unchanged, with new code, and imported nothing from C8 or its model chain.
- **Confirmed:**
  - the D_Q structure for every Q;
  - the D_Π relations;
  - the doubled-cell orbits and pieces (independent propagation);
  - G0;
  - the a·R_L·b lemma (exhaustive support, U(1) phases by Smith normal form);
  - class 2 with the palette proviso;
  - the exp(π/4·A0) exclusion;
  - the E± identities;
  - the screen spot check.
- **Corrections applied here:**
  1. the scope of "only new letter", with exp(iθR_L) and generated conjugates;
  2. the Π-taste wording (spectral survival for slot-free words);
  3. the class-1 scope;
  4. the class-2 proviso;
  5. the −k* flat/anisotropic split;
  6. the open items.
- **Not rechecked by the C8 check:** the 20,000-word mixed sample and the Q-multiplet paragraph.

**Runner provenance.**
- **What is copied.** The runner copies the B26 checker's model build, as already ported into the C11 runner. The doubled-cell orbit and piece code and the a·R_L·b phase method (Smith normal form plus ℤ₄ enumeration) follow the C8 check's.
- **What differs in implementation.**
  - The classification enumeration uses twisted group averaging of single-entry seeds instead of the check's orbit propagation.
  - The identities are exact block-dict equalities rather than random-k Bloch comparisons.
  - The a·R_L·b support count is vectorised index arithmetic.
  - The D_Π relations use sparse real-space operators.

  This is implementation-level difference, not independence of reasoning.
- **Criterion changes disclosed.**
  - **First default run: TOTAL PASS = 50, FAIL = 1.** Check 5.8 pre-declared that every sampled E-word breaks W(k+Π) = ±W(k); 52 of 63 did. The 11 exceptions were unreduced words whose E letters merge (e.g. E₊E₊ = iR_L). After seeing this, the claim was restricted to reduced words, and both counts are now reported.
  - **First `--slow` run: TOTAL PASS = 51, FAIL = 1.** Check 5.9 found one generic-slot word keeping the spectral Π-taste: E₊·Rt·Rt·E₋·o·S, which reduces to the E-free word o·S because Rt² = 1. After seeing this, the reduced-word filter was extended to exclude cancelling R_L·R_L, Rt·Rt and S·S⁻¹ pairs.
  - **The next default run, after that filter change, failed 5.8's floor of 50 reduced words** (declared before the run; 49 were drawn). The sample was enlarged from 200 to 300 words (400 with `--slow`).

## Historical execution record (not a fresh capture)

```bash
python3 scripts/corner_fermion_symmetric_shift_letter_classification_2026_10_18.py
python3 scripts/corner_fermion_symmetric_shift_letter_classification_2026_10_18.py --slow
```

- **Default:** `TOTAL: PASS=51 FAIL=0`, about 15 s on 2 threads. Seeded with `numpy.random.default_rng(20261018)`.
- **With `--slow`:** `TOTAL: PASS=52 FAIL=0`, about 20 s. It adds the range ≤ 4 enumeration and enlarges the samples.

Runner sections:
- 0: model build;
- 1: Theorem 1;
- 2: identities and the even-A reduction;
- 3: class 1;
- 4: class 2;
- 5: class 3.

Campaign scripts, all ending with FAIL = 0:
- `.claude/science/physics-loops/scale-ladder-campaign-20261018/B26_new_shift_letters/ (unavailable historical pointer; not a proof premise)` (PASS = 53);
- `.../B26_check/` (PASS = 47);
- `.../C8_beyond_permutation_letters/` (PASS = 55);
- `.../C8_check/` (PASS = 49).

## Load-bearing sources

- Long-wavelength note (O-fixed momenta ±k*, doublets D±) (`docs/CORNER_FERMION_LONG_WAVELENGTH_THEORY_IS_ONE_ISOTROPIC_SPIN_HALF_DOUBLET_AND_ONE_QUBIT_BLOCK_EMBEDDING_BOUNDED_THEOREM_NOTE_2026-10-17.md`)
- Eight-node step note (letters S, R_L, H_on, Λ; gauge-dressed lifts) (`outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_doubler_gapping_selection_rule_and_weyl_dipole_2026_10_18_full_argument.md`)
- C11 speed-law note (per-letter coefficients; A2 letters only swap labels; functions of R_L have zero coefficient) (`outputs/scale_ladder_continuations_review_2026_10_18/corner_fermion_generalised_speed_law_per_letter_additivity_2026_10_18_full_argument.md`); load-bearing only for the no-velocity-source corollaries
- Context, not a dependency: campaign blocks B18, B20, B23, B26 and C8. Their packs are campaign history, not repository sources.
- Axioms (`docs/MINIMAL_AXIOMS_2026-06-29.md`)
