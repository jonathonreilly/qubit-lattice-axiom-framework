# Generations and mass ratios from the axioms (first-principles derivation)

**Date:** 2026-10-18. One agent (Opus 5.5), same family as the exercise; unrefereed. Scripts: `FP/scripts/s1_group.py`, `s2_checks.py`, `s3_menu.py`, `s4_tm1.py`; outputs `FP/out/s1–s4.out` (cap 0.4 GB, peak 68 MB).

## Target
(a) What the axioms imply about the number of fermion generations, their labels, and how lattice symmetry acts on them.
(b) What they imply about generation mass ratios: which structural facts follow, and which inputs cannot be avoided. Comparator: 9 charged masses spanning about 1e-6; |V_us|, |V_cb|, |V_ub| = 0.225, 0.042, 0.0037 (WALL.md).

## Premise Ledger
- **Lattice:** G = Z³ ⋊ O, with O the 24 proper rotations and no inversion (checked). Load-bearing throughout.
- **Admissibility:** one nearest-neighbour (NN) covariant rule. Its range is used in B4. Its "form and values" are not supplied, which is load-bearing for the inputs result.
- **Qubit:** used only in check (i), as a spin-½ internal space. *Convention:* the axioms do not say how rotations act on M₂(C); I take conjugation by SU(2).
- **Record:** not load-bearing.
- **Primitives.**
  - realized_state: a value that depends on the state is registered data.
  - scale_reference: units only.
  - kinetic_isotropy: unused.
- **Retained theorems:** none exist. Every one of the 5,759 ledger shards on origin/main is `unaudited` (5,383) or `meta` (376), and retained_pending_chain_count = 0 (scanned). So every step below starts from the axioms.
- **Named open dependencies (zero weight).**
  - **F1:** a fermion carrier. This is the staggered-Dirac/Grassmann gate listed outside the axioms.
  - **F2:** where generations are placed: either a *star* (the three lattice momenta X_i = πe_i, or M_i), or an *internal* label at Γ.
  - **F3:** each lepton sector keeps an exact residual subgroup of G. Used only for the prediction.
  - **Data imports:** PDG CKM; NuFIT-6.0/6.1 as quoted on main; JUNO 2025 as quoted on main.

## Minimal Mechanism
The eight period-2 lattice momenta {0,π}³ (the 2×2×2 cell), acted on by G. Everything else is representation theory on this set, or on a periodic lattice with L = 4.

## Derivation steps

**A1. The only native "3" is the number of axes.** Proved; checked in s1.
- Under O, Brillouin-zone orbits have sizes {1, 3, 6, 8, 12, 24}. Size 3 occurs only for X = (π,0,0) and M = (π,π,0).
- The corners split 1+3+3+1. The irreps of O have dimensions 1, 1, 2, 3, 3.
- On Z^d, the smallest nontrivial corner orbit has d elements (checked for d = 2…5).
- **Consequence:** N_gen = 3 is *available* as d = 3, never *forced*. No carrier (F1) exists, and singlet placements are equally admissible.

**A2. How the lattice acts on a star triplet.** Proved; checked.
- With scalar labels on the X triplet, the image of G is the 48 signed permutations B₃, and it acts irreducibly (commutant dimension 1).
  - Translations act by sign characters. **The generation label is a lattice-momentum parity.**
  - The axis half-turns V₄ act trivially.
  - T(1,1,1) acts as −1 on all three generations.
  - The det = +1 part is *exactly* O in its vector (T1) form. Its Klein subgroup is realised by the face-diagonal translations T(e_j+e_k).
  - So the effective flavour group is S₄(T1) × Z₂, made from translations and rotations together.
- With spin: Ind(χ_X ⊗ Res ρ) = Ind(χ_X) ⊗ ρ, so the generation factor is unchanged. Check (i): a group-averaged spin-½ NN carrier gives an exact 6-fold X multiplet.
- Internal placements:
  - T1 or T2 give the same image up to ±1.
  - The axis-permutation A1+E has image S₃ with V₄ acting trivially. This is the F-class of main's cubic-cell note.

**A3. Labels.**
- The canonical labels are the axes i = 1, 2, 3.
- The C₃ labels 1, ω, ω̄ are canonical: S₃ contains one Z₃, and the four body-diagonal C₃ of O are conjugate. Any transposition exchanges ω and ω̄.

**B1. A symmetric realized state means degenerate generations.**
- Star, T1 and T2 triplets are exactly degenerate (Schur's lemma).
- A1+E gives at most 2 levels.
- This is main's and R3's ceiling, re-proved from the axioms.

**B2. No symmetry fixes any mass ratio.** Proved.
- Take any residual group H and a nondegenerate sector. In an H-adapted basis, the H-invariant operators include every diagonal operator, so every spectrum is allowed.
- Check: a C₃-invariant Hermitian matrix with the (e, μ, τ) spectrum exists.
- Symmetry can fix degeneracies, selection rules and eigenvectors. It never fixes eigenvalues.

**B3. The observed CKM leaves the common residual symmetry nothing to act on.** Proved; checked (iv).
- Masses are nondegenerate, so every irrep of H on V_L is one-dimensional.
- Distinct characters force both left rotations to be block-diagonal in the same way.
- A CKM with no zero entry then forces H to act on V_L by **a single character**, so H constrains nothing.
- Exhaustive menu (s3): of all exact-residual CKM patterns from B₃ or S₃, **0** lie within ×1.5 of the data.

**B4. What the nearest-neighbour range adds.** Proved; checked (ii) for a random 4×4 carrier with full anisotropy.
- Translation-invariant NN carrier: H(k) = A + Σ_j (T_j e^{ik_j} + h.c.). Then, as operators:
  - **H(X_i) + H(M_i) = H(Γ) + H(R)**
  - **H(X_i) − H(X_j) = 2[∂²_i H(Γ) − ∂²_j H(Γ)]**
- So star-placed generation splitting is *exactly* the axis anisotropy of the carrier's kinetic tensor. This holds for every NN rule and is the quantitative form of the "Lorentz cost".
- Translation breaking at period 2:
  - **Checked (iii):** an M₃ order couples {Γ, M₃}, {X₁, X₂}, {X₃, R} and {M₁, M₂} at the same time.
  - **Prior art (OBS-4, CLS-1):** a CKM that is not a permutation needs such an order.

**Unavoidable inputs (b).**
- F1 and F2.
- For each charged sector, all three masses in Planck units; for quarks, also the 4 CKM numbers. That is 13 numbers.
- By B2 and B3, none of them is fixed by symmetry. Each one is either a rule *value*, which Admissibility leaves unspecified, or *state data*, which realized_state registers.
- B4 ties the splittings to kinetic anisotropy but supplies no number.
- **No reduction below 13 was derived.**

## Novel Prediction: TM1 lepton mixing from bond-centred lattice symmetry
Under F2 (star triplet, or internal T1) and F3, I enumerated every exact residual pattern of B₃ (s3, s4):
- charged-lepton residuals: abelian subgroups with nondegenerate characters;
- neutrino residuals: Majorana Z₂ or Klein subgroups.

The fixed columns that can occur are exactly {(0,0,1), (0,½,½), (⅙,⅙,⅔), (¼,¼,½), (⅓,⅓,⅓)}. Every full pattern contains 0 or is trimaximal.

Fitted against the 3σ box (s12² from NuFIT-6.1 as quoted on main), **only (⅙,⅙,⅔) survives**, with deviation < 2e-3. Its nearest rivals:

| column | pattern | deviation |
|---|---|---|
| (⅓,⅓,⅓) | TM2 | 0.011 |
| (0,½,½) | θ₁₃ = 0 | 0.020 |
| (¼,¼,½) | | 0.032 |

The axis-permutation placement (S₃) allows only (0,½,½), so it is **excluded** for exact lepton residuals.

**Lattice realisation** (up to conjugation by G):
- **Charged leptons** keep C₃ about a body diagonal through a site.
- **Neutrinos** keep the **half-turn about the (110) face diagonal through the bond midpoint (0,0,½)**, that is C₂[110]∘T(e₃).
- The same half-turn through a site gives θ₁₃ = 0.
- The unit translation T(e₃) gives TM2, which is main's pattern and sits 3.6σ from JUNO (arXiv:2512.03809, as quoted on main).

**Predictions (TM1):**
- |U_e1|² = 2/3 and |U_μ1|² = |U_τ1|² = 1/6.
- **sin²θ₁₂ = 1 − 2/(3cos²θ₁₃) = 0.3182 ± 0.0002.** JUNO's first result is 0.3092 ± 0.0087, about 1σ away.
- cos δ = (1/6 − s₁₂²c₂₃² − c₁₂²s₂₃²s₁₃²)/(2s₁₂c₁₂s₂₃c₂₃s₁₃), giving:

| s₂₃² | cos δ | \|δ\| |
|---|---|---|
| 0.47 | −0.13 | 98° |
| 0.50 | 0 | 90° |
| 0.561 | 0.27 | 74° |

- The electron is the C₃-trivial character. A Brannen fit consistent with this needs δ_B = 2/9 + 2π/3, not 2/9.

**Novelty.** Main records that it "does not supply" TM1 (PMNS_TM2_COLUMN_SITE_BASIS…_2026-06-07, corrigendum of 2026-09-30). The S₄ group theory of TM1 is literature (Lam; Luhn and King), used here as a template and re-derived by enumeration. What is new: lattice translations supply the Klein subgroup, and TM1 is the unique survivor of the lattice's own menu.

**Kill conditions:**
- JUNO's final sin²θ₁₂ lies more than 3σ from 0.318 (expected σ ≈ 0.0015).
- δ breaks the sum rule at the measured θ₂₃.

## Weakest Link
- **F3.** Exact sector-wise residual symmetries are assumed, not derived. One realized state has to give charged leptons a C₃-symmetric order and neutrinos an order fixed by the bond-centred half-turn. Cross-sector operators must not spoil this; CLS-1 found that unprotected operators of this kind are generic.
- **Test artifact:** a lattice Landau model with the two orders and their one-loop cross-sector leakage, checking whether |U_e3| and the deviation from TM1 stay below about 1e-2.
- **Second weakest:** F2's scalar generation factor, which fails if the internal little-group rep is not the restriction of a global O-rep.

## Status
- (a) and B1–B4: **TESTED.** Exact checks; same family; unrefereed.
- Mass hierarchy: **BLOCKED** at the *values wall*. The axioms supply no rule values, and B2 shows symmetry cannot stand in for them.
- TM1 prediction: **PROPOSED.** It is conditional on F2 and F3, and is currently 1σ from JUNO.
