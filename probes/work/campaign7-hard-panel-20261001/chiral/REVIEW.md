# Hostile review of Lane C (chiral) REPORT.md

I checked everything by hand against origin/main `0485dc0738`. I ran no code and wrote no files.

**Sources I read:**
- the Spin(10) atomic-gaps note (2026-09-14);
- the chessboard record-background note (09-22);
- the composite-sites exact-charge note (#9144);
- the hyperhoneycomb note (#9168);
- the certified two-or-six touchings note (09-26);
- the star-term note;
- the species-symmetry note, which contains the walk symbol Σσ_a sin k_a.

I also fetched these abstracts this session: 2503.07708, 2603.15985, 2601.04304, 2306.10105, 2001.11991 and 2006.04204.

## Verdicts

| Claim | Verdict |
|---|---|
| O1 (free fermions with an on-site U(1) are vectorlike) | HOLDS |
| O2 | HOLDS (ARGUED, standard) |
| O3 (static records are deletions) | HOLDS WITH NARROWED SCOPE |
| O4 (Majorana nodes carry real-representation content) | HOLDS. It can be strengthened. |
| O5 budget lemma | HOLDS WITH NARROWED SCOPE |
| O5 dark lemma | HOLDS for its stated scope. It can be strengthened, and its relevance needs narrowing. |
| O6, Fidkowski-Xu paraphrase | WRONG paraphrase. Its use as a non-premise is unaffected. |
| R2 algebra: X, [X,1⊗A]=0, S_1²=1, non-commutation | HOLDS |
| R2 claim of an "exact lattice symmetry replacing crystal momentum" | GAP |
| Step 1 and Step 2 spectrum and f values | HOLDS |
| Step 2 "covariant", and its chessboard citation | HOLDS WITH NARROWED SCOPE (the citation overreaches) |
| Steps 3–4 | HOLDS. The Costa-Dobrescu-Fox counts 5, 6 and 8 are confirmed. |
| Step 5 form factor | HOLDS |
| Step 5/7: "light mode reached only through q³" and "coupled through q² and q³ factors only" | WRONG at the eigenmode level |
| Step 6 rank 4 and U(1)_Q × Z₂^F | HOLDS. It extends to the full U(5). |
| Step 7: "all symmetry and anomaly preconditions are met" | HOLDS WITH NARROWED SCOPE |
| §5A arithmetic | HOLDS. "Decisive" is overclaimed. |
| R4 Floquet, W₃ = 0 | HOLDS |

## 1. f, Hermiticity and the block square

All EXACT.

**Values of f.** In momentum space C_j acts as cos k_j, so f = e₂(cos k) − 3, where e₂ is the sum of pairwise products. Writing the cosine vector c at each corner weight r:

| Weight r | c | e₂ | f |
|---|---|---|---|
| 0 | (1,1,1) | 3 | 0 |
| 1 | (−1,1,1) | −1 | −4 |
| 2 | (−1,−1,1) | −1 | −4 |
| 3 | (−1,−1,−1) | 3 | 0 |

**Commutation and Hermiticity.**
- The displacements in f are ±e_j±e_l and 0, all of which preserve the parity of x+y+z. So [ε, f] = 0.
- ε and f are real symmetric and commute, so εf is Hermitian.
- f(k+Π) = f(k), because each product of two cosines flips sign twice.

**Fourier form.** The term is ψ†εfψ = Σ_k f(k) ψ†_{k+Π} ψ_k.

**Block square.** The mass mf is the identity in coin space, so it commutes with σ·s. Then [[σ·s, mf], [mf, −σ·s]]² = (|s|² + m²f²)·1.

**Small-q expansion.** f(q) ≈ −|q|², because each q_j² appears in two pairs.

**Survivors.** Exactly the pair (0, Π) survives, with chiralities + and −.

## 2. Cube composite

**Form factor (EXACT).** Put the cube's lowest corner at x and write y = x + δ with δ ∈ {0,1}³. Then Ψ_c = ε(x) Σ_k ψ_k e^{ik·x} Π_j (1 − e^{ik_j})/2, so |b| = Π_j |sin(k_j/2)|.

**Values.**
- At Π: 1.
- At the light node: ≈ |q_x q_y q_z|/8.
- At weights 1 and 2: 0.
- Nuance: b vanishes on every coordinate plane k_j = 0, not just at the node. The suppression is cubic-anisotropic.

**Error (EXACT).** The light *eigenmode* is not the bare chirality-+ field.
- In the (light u₊, mirror u₊) block at small q the matrix is [[|q|, −m|q|²], [−m|q|², −|q|]].
- The mass is coin-identity, so it couples light helicity + only to mirror helicity +, which sits at −|q|.
- The mixing angle is therefore ≈ m|q|/2.
- Ψ_c sees the mirror component at full strength, so the interaction couples to the light quasiparticle at **O(m|q|), not O(q³)**.
- Both orders vanish at q = 0, so the qualitative decoupling survives, but the stated order is wrong.
- Fix: use a form factor that vanishes faster. For example f², which has range up to four steps and still gives 0 at weights 0 and 3 and 16 at weights 1 and 2, gives mixing O(m|q|³).

## 3. Dark lemma

**The steps are correct (EXACT).**
- Finite-range jumps make φ a trigonometric polynomial. Exponential tails make it real-analytic.
- The squared identity is a trigonometric polynomial that vanishes on an open set, so it vanishes on all of T³.
- Equality in Cauchy-Schwarz gives an eigenvector of σ·s or zero. The squaring sensibly avoids √|s|², and the result does not fix which eigenline.
- The upper and lower eigenline bundles over a small sphere have Chern number ±1, so a continuous φ has a zero on each sphere. Continuity then gives φ(K) = 0.
- Wording fix: "vanishes on each sphere" should read "has a zero on each sphere".

**Hidden assumptions.**
1. The dark state is a Bloch-diagonal, translation-invariant Slater state. Degenerate-shell superpositions are excluded.
2. Jumps are linear, of definite charge, and parity-odd. A parity-odd jump needs a fermionic environment. A readable bosonic qubit record cannot carry fermion parity, so the class the lemma treats may not be the class that Record licenses.
3. The Hamiltonian part of the Lindbladian is the unchanged h.
4. B must be read as a punctured neighbourhood of the light node.

**Is "filled on an open set B" natural?** Yes. It is the minimal requirement for a Weyl vacuum at the light node.

**Strengthening (EXACT).** If the sea is filled in a punctured neighbourhood of every node, analyticity is not needed. The local degree argument with a continuous φ is enough, and a C¹ φ gives O(q²) damping.

**Multiband case.** The same local argument applied to P_mid φ, where P_mid projects onto the middle two bands and is smooth near the node, settles it EXACTLY under that hypothesis. The analytic continuation from B alone remains ARGUED for more than two bands.

**Near-dark caveat (ARGUED).**
- Near a linear node, lower(q) = upper(−q). Hence the vacuum's loss rate is ρ ≥ ∫_ball Γ(q) d³q/(2π)³ over the ball where φ is roughly constant, which has radius about 1/R for jump range R.
- So Γ ≲ C·R³·ρ: a sink can damp doublers for only about R³ e-folds within the record budget.
- The escape is therefore blocked by finite range combined with the budget, not by exact darkness alone.

## 4. R2

**The algebra checks out (all EXACT).**
- With ε = iτ^y, X = ε⊗S + τ^z⊗K, where S = (T+Tᵀ)/2 and K = (T−Tᵀ)/2.
- X is real and antisymmetric.
- [X, 1⊗A] = ε⊗[S,A] + τ^z⊗[K,A] = 0, given [T,A] = 0 and Tᵀ = T⁻¹.
- X² = −(S² − K²) − τ^x⊗[S,K] = −1. So Q₁ is a complex structure with spectrum in Z + N/2, the same offset as Q₀. The test spec's "spectrum of Q₁ is integer" needs that same shift.
- [ε⊗1, X] = −2τ^x⊗K, which is proportional to sin(k·a)τ^x.
- [ô_X, ô_Y] = i·ô_{[X,Y]}.
- The quote from Gioia-Thorngren is verbatim. Their abstract adds that the ultraviolet algebra is the Onsager algebra and that the model is a magnetic Weyl semimetal. The two-copy network is that structure in Majorana form, so R2 is their mechanism rather than a new one.

**Gaps.**

(a) **The bare Q₁ is unphysical.** The landed #9144 note proves P Q P = 0 for bare bilinears between distinct sites, and Q₁ is built from c^α_i c^β_{i+a}.
- The fix is to dress each bilinear with link strings u along a path.
- Even dressed, Q₁ commutes with H only in flux sectors with zero flux through every parallelogram spanned by a and a bond (ARGUED).
- So Q₁ is exact for the comparator in its fixed gauge sector, not for the spin model.

(b) **At quadratic level it does not replace crystal momentum (EXACT).**
- A perturbation that preserves Q₀ has the form 1⊗D₀ + ε⊗D₁.
- Preserving Q₁ as well requires [D₀, T] = 0, [D₁, S] = 0 and {D₁, K} = 0.
- The last two give D₁T = T⁻¹D₁. Then D₁(x,y) = D₁(x−a, y+a), which forces infinite range unless D₁ = 0.
- So local quadratic perturbations that preserve both U(1)s are exactly the flavour-blind, translation-invariant ones. Gioia-Thorngren's robustness when translations are broken is not shown for this construction.

(c) **R2 does not meet the §1 target.** Each U(1) acts vectorlike. "Grade A in the SU(2) sense" is a new grade and should be named as one.

(d) **Gauging logic.** The reason R2 cannot be gauged is that the infrared SU(2) is Witten-anomalous, not that it is not on-site.

(e) **Choice of translation (EXACT, from the landed certificate).**
- At J = 1, κ = 3/10, the landed certificate gives two nodes.
- κ² = 0.09 is below κ_c² = 3/20, so only family (i) exists: (x, 1−x, 0) and (1−x, x, 0).
- For a = n₁a₁ + n₂a₂ + n₃a₃, sin(k₀·a) = sin(2π(n₁−n₂)x). This is zero for a₃ and for a₁+a₂.
- a = a₁ works, because cos 2πx lies in (−1, 1).
- This gives one doublet, an odd count, as required.

## 5. Step 6

All EXACT.
- **Neutrality and rank.** Every monomial is neutral, and the rank is 4.
- **Minors.** Deleting column 1 gives −2 (I checked it). Deleting column 2 gives 10. Together these are consistent with (−1)^i M_i = 2q_i.
- **Component group.** The gcd of the maximal minors is 2·gcd(q) = 2, so the component group is Z₂.
- **Fermion parity.** π(1,1,1,1,1) gives row sums (4, 4, 2, 0)·π, all multiples of 2π. It is not in U(1)_Q, because −8 is even and 1 is odd.
- **Extension to U(5).** The charges are distinct, so the centralizer of U(1)_Q is the diagonal torus. A rank-1 non-abelian identity component would need weights symmetric under ±, and the chiral set is not. So the residual continuous symmetry is U(1)_Q inside all of U(5).
- **Not covered:**
  - cubic point-group and time-reversal/charge-conjugation symmetries, which generic complex couplings should be chosen to break;
  - the Lorentz caveat;
  - the global anomaly for Spin × U(1), which stays ARGUED.

## 6. Scope

**Spin(10) note.**
- §4 matches: "restores momentum-space doublers"; a full layer "still has the opposite-handed boundary partner"; q = 32.
- But "proves the interacting version" overstates it. §4 is a projection identity. §5 is a fixed-volume Feshbach bound for U > 2‖V‖, and the note says outright that it is not a proof about an intermediate interacting phase.
- Its frozen state (|0⟩+|F⟩)/√2 is not a Fock state, so the deletion identity is broader than O3's "Fock states".

**O3.**
- "Keeps every N-N hypothesis" fails for aperiodic record patterns, where H2 is lost. O1's slice-Chern proof needs periodicity; otherwise fall back on O2.
- Records of fluxes or links select a sector rather than delete modes.

**Chessboard note.**
- It supplies the configuration n_x and a scalar coupling c·n, and says "No formation or ordering of that configuration is derived".
- Its staggered term is the on-site (c/2)ε. That term gaps the (0, Π) pair as well.
- The εf form factor, which has face-diagonal (two-step) support, is a separate supplied term.

**Star-term note.** It reports a numerical particle-hole pair of *near*-touchings (energies about ∓0.0071), with no certified node count.

**Literature.**
- Fidkowski-Xu argue that U(1)_A cannot be implemented by shallow-depth circuits with finite on-site dimension. They do not say "exponentially local charge".
- The Thorngren-Preskill-Fidkowski abstract uses rotor models. Its commuting-projector obstruction is not in the abstract, and I did not verify it in the body.
- The report omits Gioia-Thorngren's single-Weyl model with a non-compact, not-on-site chiral symmetry.

**§5A.**
- The arithmetic holds:
  - ℓ·t = ℓ·s = 0 for both gapping vectors;
  - both vectors are K-null, and mutually K-orthogonal;
  - the gcd of the 2×2 minors is 1;
  - (−1)^F is (α, β) = (π, π).
- A 1+1D result cannot settle the 3+1D Golterman-Petcher-Rivas and Golterman-Shamir obstructions. I recall published 3450 DMRG work, but I have not verified that recollection. Call it a mechanism control, not "decisive".

**Brief compliance.** The word "only" is used repeatedly. The report is about 3000 words against a cap of 2500.

## Required corrections

1. Step 5/7: the light-mode exposure is O(m|q|) through quadratic mixing. Fix it with a higher-order form factor such as f², or restate it.
2. Step 2: drop "covariant reduction" and the chessboard attribution for εf. Name εf, with its face-diagonal range, as a separate [S] term.
3. R2:
   - add Wilson-line dressing;
   - restrict exactness to translation-invariant flux sectors;
   - state the quadratic-commutant result;
   - fix the gauging logic;
   - require n₁ ≠ n₂ in the choice of a.
4. O3: restrict to periodic records of states with definite parity. Narrow the Spin(10) citation to the projection identity plus the fixed-volume Feshbach bound.
5. Dark lemma:
   - add the translation-invariance and parity-odd caveats;
   - add the near-dark bound Γ ≲ R³ρ;
   - upgrade the multiband case when the sea is filled near every node;
   - fix the wording to "has a zero on".
6. Step 7: say "perturbative anomalies plus the U(5) flavour condition". Leave the global, lattice and time-reversal conditions open.
7. Correct the Fidkowski-Xu paraphrase. Downgrade the star-term citation to "numerical near-touchings".

## Bottom line

The overall verdict is correctly scoped: charged chirality reduces, under heavily supplied inputs, to symmetric mass generation of one cubic-invariant mirror, and that is not shown. The exact algebra is sound throughout: f, the block square, b(k), X, the residual group and the dark lemma. The report has one substantive error: the light mode couples to the interaction at O(q), not O(q³). It also overstates two things: R2 as an exact physical symmetry, and the landed chessboard and Spin(10) notes as support for Step 2 and O3.