# Hostile review of `c7/hard/gen/REPORT.md` (Lane B: generation count and chirality)

Nothing was run and no files were written. Every check below was done by hand. I read on `origin/main`:
- the corner-forcing note and its runner `scripts/probe_bz_corner_decomposition.py`;
- the Block 03 Kawamoto-Smit (KS) note and the Block 02 Grassmann note;
- `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` and `SITE_PHASE_CUBE_SHIFT_INTERTWINER_NOTE.md`;
- the 09-22 scalar-hop note and the 09-21 blind-walk note;
- the 09-03 taste-census note;
- `KOIDE_Z3_EQUIVARIANT_ANTICOMMUTING_NO_GO_NOTE_2026-05-16.md` §1–5.1;
- `FLAVOR_EMERGENT_CHIRALITY_NO_TRANSPORT_NOTE_2026-05-30.md` line 71.

## Verdicts

| Claim | Verdict |
|---|---|
| O1(b): plane-wave constraint, lemma, non-invariance | **HOLDS, with narrowed scope** (two sub-claims are wrong as stated; see below) |
| O1(b): the landed Step 3 uses non-symmetries | **HOLDS for the translations, in every gauge.** C₃ can be an exact symmetry in a suitable gauge |
| O1(c): characters (8,2,0,4,0); 2A₁+2T₁; A₁+T₁ per chirality; cocycle trivial | **HOLDS** (all 5 classes re-done by hand). The "3 is a vector" reading depends on the rotation centre |
| D1: forced NN coin Hamiltonian | **HOLDS, with narrowed scope** (needs S1 plus zero-flux translation invariance) |
| D2: nodes, handedness, frames | **HOLDS** |
| D3: Mackey argument | **HOLDS** as representation theory. At a = 0, extra symmetries merge the 3 with the 1 |
| S1: two modes per site | **GAP** for any reading as a derivation from the axioms. Defensible only as the program's existing supplied walker |
| D4: handedness I₃⊗σ₃ outside the no-go | **HOLDS, but inert.** It is the separate-factor case main already lists as open, and it says nothing about generation chirality |
| O4: no singlet-only NN mass | **HOLDS** for number-conserving terms. Pairing terms escape it under a tuning |
| D5: masses α−β and α+3β | **HOLDS, with narrowed scope.** "Lorentz-scalar" needs a = 0, which the landed 09-22 T4 already says |
| D6: mixing spectra | **HOLDS.** (i) omits singlet admixture. "Reduces O to C₃" is shown for on-site layer fields, not in general |
| D7: coin → KS ⊕ KS | **HOLDS** (Block 03 eq. (4) is this spin-diagonalisation identity) |

## 1. O1(b) and the landed corner-forcing note

**Re-derivation (EXACT).**
- Constraint. Take η_μ = (−1)^{ζ_μ·x}. The plaquette product is η_μ(x)η_ν(x+e_μ)η_μ(x+e_ν)η_ν(x) = (−1)^{(ζ_ν)_μ+(ζ_μ)_ν}. π flux requires (ζ_μ)_ν + (ζ_ν)_μ = 1, so at most one ζ_μ is zero.
- Action on corners. With H = −(i/2)Σ η_μ(∇⁺−∇⁻), we get H|k⟩ = Σ_μ sin k_μ |k+πζ_μ⟩. Corner A goes to A⊕ζ_μ with coefficient (−1)^{A_μ} sin q_μ.
- Lemma. b = e_c sends e_c to 0. b = e_a+e_c sends e_d to 111. b = 111 sends e_a to ē_a. So no nonzero b maps L₁ into itself.
- KS shifts are S_a = T_a·(−1)^{b^{(a)}·x}, with b^{(a)}_ν = (ζ_ν)_a. In the standard gauge this gives the usual (−1)^{x₂+x₃}, (−1)^{x₃}, 1. Confirmed.

**Two sub-claims are wrong as stated.**
1. "The plain translations T_a are not KS symmetries." In the standard gauge T₃ *is* a symmetry. The correct statement (EXACT) is that in any gauge, at most one plain translation is a symmetry. Proof: if T_a and T_b both were, every η would be independent of x_a and x_b, and the ab-plaquette product would be +1.
2. "Neither is the plain C₃." This is gauge-dependent and false in general. Take the cyclic gauge η₁ = (−1)^{x₂}, η₂ = (−1)^{x₃}, η₃ = (−1)^{x₁}:
   - it satisfies all three flux constraints;
   - it is invariant under x → (x₃, x₁, x₂);
   - so the plain C₃[111] is an exact KS symmetry there.

**A stronger replacement, independent of gauge (EXACT).** The π-flux constraint gives S_aS_b = −S_bS_a for a ≠ b. The true KS translations anticommute pairwise, so they have no joint characters. The "three distinct joint translation characters" therefore do not exist for any KS symmetry.

Separately, the Hamming labelling of KS zero modes depends on the gauge. Block 03 Remark R3 says "−η⁰ is the ε-gauge transform of η⁰ (same class; runner-verified), so the global-sign choice is gauge, not physics". The corner-forcing note's own check says ε acts as "n → n xor (1,1,1)". Together, the same physical modes are labelled hw = 1 in one representative and hw = 2 in the other.

The simplest counter is a dimension count. In a one-component carrier each corner holds one complex amplitude, so three corners give 3 dimensions, while three Weyl species need 6.

**What the landed note actually uses.** The runner's `translation_character` returns (−1)^{n_μ} (plain lattice translation), and `c3_111` is the bare index cycle with no gauge factor. These are plain lattice operators acting on corner plane-wave labels, not symmetries of the Block 03 operator. They are symmetries of the coin carrier (D7).

To be fair to the note: it never says these operators are KS symmetries, and it disclaims the species reading. So O1(b)(7), "It says nothing about KS species", attacks a claim the note does not make. The real defect is that the note attaches the corner algebra to the KS operator.

**A narrowing repair is warranted.** These are the exact landed sentences:
- Step 1: "By Block 03, the Kawamoto-Smit kinetic operator on Z³ APBC is diagonalized in momentum space at the BZ corners k_μ ∈ {0, π}."
  - This is false: H_KS maps k to k+πζ_μ.
  - Under APBC, the momenta (2m+1)π/L exclude 0 and π.
- Step 3: "The three lattice translations `T_x, T_y, T_z` act on the hw=1 triplet as … (distinct joint characters separating the three corners)."
  - These are plain translations, not KS symmetries. At least two fail in every gauge.
- Step 4: "If a quotient claims to preserve any exact retained operator, the observable-descent lemma forces its kernel to be invariant under that operator. In the present finite carrier, preserving the translation projectors forces…"
  - The projectors are not operators the KS carrier must preserve.
- Step 6: "There is no convention freedom in the Hamming-weight assignment to corners; it follows directly from the binary corner labeling under APBC."
  - This contradicts Block 03 R3, quoted above.
- Theorem 3: "The Kawamoto-Smit staggered-Dirac kinetic operator on Z³ APBC has 8 BZ corners that decompose UNIQUELY by Hamming weight…"

Suggested scope for the repair: the M₃(C) and no-proper-subspace statements hold for plain translations and the plain C₃ acting on corner plane-wave labels. They are not symmetry statements about the Block 03 operator, whose translations are magnetic and anticommuting, and whose Hamming labels depend on the representative of its gauge class.

The companion `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md` line 33 makes the stronger claim "the three `hw=1` sectors are exact observable sectors of the Hamiltonian". In the taste-cube form H(q) = sin q₁Z₁ + sin q₂X₁Z₂ + sin q₃X₁X₂Z₃, the X₁ factor changes Hamming weight. So that sentence is false for KS and needs the same narrowing.

## 2. O1(c): characters

I take (Wψ)(y) = g(y)ψ(R⁻¹y) and solve the link equations in the standard gauge:
- C₄z: g = (−1)^{y₁y₂};
- C₂z: g = 1;
- C₃: g = (−1)^{y₁y₂+y₁y₃};
- C₂′(110): g = (−1)^{y₁y₂}.

All four match the report. Using χ(R) = Σ g(Rs)(−1)^{|m|} over cell sites:
- C₄z: fixed sites have s₁ = s₂; (11s₃) gives (−1)(−1); total 4.
- C₂z: Σ(−1)^{s₁+s₂} = 0.
- C₃: sites 000 and 111 give 2.
- C₂′: 1 − 1 − 1 + 1 = 0.

So χ = (8,2,0,4,0) = 2A₁ + 2T₁ (CHECKED).

Per chirality the split must be 4+4. The only subset of {A₁, A₁, T₁, T₁} with dimension 4 is A₁+T₁, so that part follows.

**Cocycle trivial (EXACT).** W_RW_SW_{RS}⁻¹ is a sign field that commutes with H. Every NN link has nonzero hopping, so the sign field is constant, and its value at the fixed origin is 1.

**Caveat (ARGUED).** These are rotations about a site. Rotations about a cube centre differ from them by an anticommuting magnetic translation and may act projectively. So the "the 3 is spin-1" reading depends on the centre. What holds whatever the centre is 4 dimensions per chirality, i.e. N_f = 2. That is already on main: the taste census line 248 says "No generations from tastes". That note also marks 2A₁+2T₁ as unverified (line 167), and this hand check supplies it. The PR #7844 cross-reference cannot be checked on main.

## 3. D1–D3 and the admissibility of S1

**D1.** The invariant count is right:
- cos ⊗ 1 contains one A₁;
- sin ⊗ σ, i.e. T₁⊗T₁, contains one A₁;
- cos ⊗ σ, i.e. (A₁+E)⊗T₁ = 2T₁+T₂, contains none;
- sin ⊗ 1 and the on-site σ term contain none.

This assumes the two modes are a spin-½ doublet and the hopping is zero-flux and translation-invariant. A π-flux coin is equally NN-covariant up to gauge and is excluded by assumption.

**D2.** Confirmed: H_{e_a} = −σ_a(v q·σ)σ_a, handedness (−1)^{|n|}, node energies a₀+2a(3−2|n|).

**D3.**
- The stabiliser of πe₁ is the 8-element D₄.
- The lifts of C₄x and C₂y do not commute, so the 2-dimensional representation is irreducible.
- V₆ is induced from an irreducible representation, so it is irreducible. It is inequivalent to V₂ (different character orbit and dimension).
- Restricted to rotations, V₆ = E_{1/2}⊗(A₁+E) = E_{1/2}⊕G_{3/2}.
- Addition (EXACT): the irreducible little-group representation also pins each node to its corner.

**Hostile catch.** At a = 0 the even exchange maps of 09-22 T2 are exact unitary symmetries; for example V₀₁₁ = (−1)^{x₂+x₃}σ₁ commutes with H at a = 0. V₀₁₁ sends e₁ to 111 (and e₂ to e₃). So at a = 0 the left-handed triplet and singlet form one orbit, and the 3|1 split is not a property of the kinetic term.

**S1.** The axioms give one qubit, M₂(C), per site. Block 02 fixes a single-pair Grassmann per site with per-site Fock dimension 2, a retained input. A field with two fermion modes per site needs per-site dimension 4. The composites do not repair this:
- dimer pairings break O;
- a 2³ cell holds 8 modes, which is KS again with fourfold taste and a reach-2 hop;
- Kitaev partons need a Z₂ constraint, and the exactly solvable form freezes three of the four Majoranas.

The coin is defensible as the program's existing supplied walker: the 09-21 note says "amplitudes on the lattice with the qubit as their coin", and the 09-22 note says "not amplitude dynamics derived from the axioms". It is not fatal as a supplied model, but it rules out any reading of this result as derived from the axioms.

## 4. D4: separate-factor handedness

The no-go's claim_scope: "the subspace of Hermitian operators on R^3 commuting with the cyclic shift R intersects the subspace of Hermitian operators anti-commuting with `Γ_χ = (2/3) J − I` only at H = 0." Its §4 adds that the structure with "`γ_CL = I ⊗ σ_3`, and `Γ_χ` as a SEPARATE grading on the `R³` factor is NOT addressed".

So D4 is out of scope of the no-go. That is correct but uninformative: N7 of the same note already names it as the steelman, and the no-transport note's line 71 shows the grading is "**INERT**" on generations.

What is genuinely new is concrete: the e_a ↔ ē_a pairing is the unique S₃-equivariant one (the 3-point S₃-set has no automorphisms), and it matches the ε pairing.

## 5. O4, D5, D6

**O4 (EXACT).** The Hermiticity condition and the algebra (B_a = B, α = −B, hence zero) are right. A sharper version: with O-symmetric NN terms, G = α₀ + ib Σcos k_μ. Then the triplet mass is √(α₀²+b²) and the singlet mass is √(α₀²+9b²), so at NN range the singlet is at most 3 times heavier than the triplet.

Scope gap: pairing escapes O4. The NN, O-symmetric s-wave pairing Δ(k) = D(−1+Σcos k) vanishes exactly at πe_a and gaps the other five corners (values 2D, −2D, −4D). That leaves three left-handed Weyl nodes, but only by a one-parameter tuning, without U(1), and with nothing protecting them.

**D5.** Confirmed:
- ε·F is Hermitian because F(k+Q) = F(k);
- triplet mass α−β, singlet mass α+3β;
- the even-translation characters (−,+,−), (−,−,+), (+,−,−) are shared within each pair.

But for a ≠ 0 the paired nodes are offset by 4a, which acts as an axial energy offset. The 09-22 T4 already says these "are corner energies, not a derived collection of rest masses". So the Lorentz-scalar reading needs a = 0, and there (section 3) the 3|1 split comes from the supplied β term alone. Reach 2 also goes beyond the NN rule and is a further supply.

**D6.**
- (i) I re-derived M = mI − 2b L·S, using σ_bσ_a = −(L_c)_{ba}σ_c. Eigenvalues: m−b for J = 3/2 (4 states) and m+2b for J = 1/2 (2 states). Confirmed. However, c = a also couples e_a to 000, so the singlet admixture caveat applies here as in (ii).
- (ii) σ_bσ_dσ_a = iε_{bda}, the circulant mI + iλ(P−Pᵀ), and the spectrum m, m±√3λ are all confirmed.
- "Needs a background that breaks even translations" is EXACT by the character argument.
- "Reduces O to C₃" is EXACT within on-site layer fields, since (A₁+E)⊗T₁ contains no A₁. It is ARGUED in general.

## Bottom line

**On the narrowing repair.** It is warranted and should target Step 1, Steps 3–4, Step 6 and Theorem 3 "UNIQUELY", plus line 33 of `THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md`. The firmest grounds are two facts:
- the true KS translations anticommute, so no joint characters exist in any gauge;
- Block 03 R3 makes the Hamming labels depend on the gauge representative.

**On "three generations".** This is a genuine group-theory result, but it is conditional and not a derivation from the axioms. It shows that a spin-½ coin walker with zero-flux NN hopping has, per handedness, a Mackey-protected irreducible triplet ⊗ spin. The 3 is the number of weight-1 corners, which equals d. This is the naive-fermion doubler count, reread as copies labelled by crystal momentum.

The result rests on these supplied pieces:
1. two amplitudes per site (the coin), which conflicts with Block 02 if read as a fermion field;
2. zero-flux NN hopping;
3. either a ≠ 0 (3|1 split, but no Lorentz-scalar masses) or a = 0 plus a reach-2 β term with a supplied hierarchy;
4. backgrounds that break translations, for mixing.

The result is vector-like, so G4 (charged chirality) is untouched. On the one-mode-per-site carrier that Blocks 02 and 03 actually fix, the count is N_f = 2 and there is no triplet.