The harness blocked writing `c7/hard/chiral/REPORT.md` because subagents may not write report files, so the full report is below for you to save. It was written by derivation only against origin/main `0485dc0738`; nothing was run.

---

# REPORT.md: Lane C, a charged chiral fermion and the doubling obstruction

**Labels.**
- **EXACT**: a pen-and-paper proof given here.
- **CHECKED**: a finite hand enumeration.
- **ARGUED**: reasoning that has not been verified.
- **LIT**: an abstract or summary I fetched this session; it is never used as a premise.
- **[S]**: a supplied piece.

**Notes read on main:**
- the axioms memo;
- the hyperhoneycomb embedding note (#9168);
- the composite-sites exact-charge note (#9144);
- the covariant time-reversal-odd star-term note (the landed salvage of #9112);
- the Spin(10) atomic-gaps note (2026-09-14);
- the species-symmetry / sixteen-zero-modes note (2026-09-24);
- the chessboard record-background note;
- the no-per-site-chirality note;
- the registration-reinstates-chirality no-go.

## 1. The problem in framework terms

**What the axioms supply.**
- Z^3, with one M_2(C) per site, so each site space is finite-dimensional.
- One NN-covariant law-level distribution.
- Permanent records, at most one per site.
- No Hamiltonian, no fermion, no U(1) and no time.

**What is already on main.** Under the owner's 2026-09-02 ruling, sites compose by the tensor product and fermions are emergent.
- **Composite vertex (#9144).** The (σ, τ) composite vertex has an exact on-site SU(2), with S^z = −i c^x c^y/2.
- **Hyperhoneycomb comparator (#9168).** Its crossings carry opposite Berry fluxes.
- **Star-term note.** It gives one particle-hole pair of Weyl touchings.

**Target.** A supplied dynamics on finitely many qubits per site with two properties:
- an exact, quantized U(1) generator Q;
- an infrared set of left-handed Weyl charges {q_i} that is not symmetric under q → −q.

There are two grades:
- **(A) anomalous:** Σq³ ≠ 0 or Σq ≠ 0. A single charged Weyl fermion is the example.
- **(B) anomaly-free chiral:** for example the set (1, 5, −7, −8, 9). This is the grade a gauged U(1) such as hypercharge needs.

## 2. Obstructions, with exact scope

**The Nielsen-Ninomiya (N-N) hypotheses and their status under the axioms**

| | Hypothesis | Status under the axioms |
|---|---|---|
| H1 | Locality | Supplied by the NN rule |
| H2 | Translation invariance | Lattice axiom; records may break it |
| H3 | Closed system, Hermitian H, continuous time | Not axiom content; Record says records form, permanently |
| H4 | Symmetry on-site and compact | Not axiom content; no U(1) is supplied |
| H5 | Quadratic dynamics | Not axiom content |
| H6 | Finite-dimensional sites, no extra dimension | Qubit axiom (M_2(C)) and Lattice axiom (Z^3) |

**O1 (EXACT, standard): free fermions with an on-site U(1) are vectorlike.**
- Take a quadratic H that is translation-invariant and local, with an on-site U(1) of integer charges.
- [H, Q] = 0 means H hops only between orbitals of equal charge. Each charge sector is therefore its own Hermitian band problem.
- Within a sector, the Chern number on k_z-slices is periodic in k_z, so the node charges sum to zero.
- The content is vectorlike charge by charge, and the landed comparators obey this.

**O2 (ARGUED, standard anomaly matching).**
- An on-site compact U(1) on a tensor-product lattice can be coupled to a background lattice gauge field, so it is anomaly-free.
- Grade (A) is therefore excluded even with interactions. Grade (B) is not excluded.

**O3 (EXACT): static records are deletions.**
- A record acts as a product projection P. For fermion modes frozen in Fock states, P c P = 0, and P c_x† c_y P = 0 when x is recorded and y is not.
- So PHP is the problem on the unrecorded modes, with H1, H4 and H5 intact, and O1 applies to it.
- The landed Spin(10) note proves the interacting version for its slab (its §4). Freezing the mirror slots in the exact singlet "restores momentum-space doublers"; freezing a full layer leaves the partner.
- Records can carve a model, but the carved model is again a local lattice model on finite sites.

**O4 (EXACT): Majorana nodes give vectorlike content.**
- Take n flavour-blind Majorana copies, H = h(k) ⊗ 1_n (Yao-Lee has n = 3).
- Because c(−k) = c(k)†, the node at k0 and its image at −k0 are one set of modes: n complex Weyl fermions of a single chirality.
- An on-site symmetry G acts on them through a real orthogonal representation V. The content is V ⊗ C, whose generators are imaginary antisymmetric, so tr(T_a{T_b, T_c}) = 0.
- For S^z this gives charges ±1 at k0. "Weyl's U(1) is crystal momentum" is exactly this statement.

**O5 (EXACT, framework-specific): record sinks.** This answers (i) for the one thing Record does supply, irreversibility.
- **[S] setup.** Jumps are linear and finite-range, L_a = Σ_y [u_a(y−x) ψ_y + v_a(y−x) ψ_y†], each of definite charge. Each jump is identified with one record.
- **The escape exists at the operator level.**
  - Take the landed naive walk h = Σ_a σ_a sin k_a with jumps √γ (ψ_x − ψ_{x+e_j}).
  - Then H_eff = h − iγ Σ_j (1 − cos k_j). Damping is zero at k = 0 and 2γr at a corner with r components equal to π.
  - Only the chirality +1 node is long-lived: it is an anti-Hermitian Wilson term that keeps chirality and U(1).
  - This is the dynamical class of Bessho-Sato (LIT, arXiv:2006.04204).
- **Budget lemma (EXACT from the Record text).**
  - Each site carries at most one record, permanently. N sites can therefore host at most N jump-records ever.
  - A vacuum with jump-rate density ρ > 0 lasts at most about 1/ρ unless fresh carrier sites are supplied [S].
  - The half-filled sea above has ρ = γ Σ_j ⟨2(1 − cos k_j)⟩ > 0, so this escape is exactly what the budget forbids.
  - A stationary vacuum must therefore be dark.
- **Dark lemma (EXACT for two bands, h = σ·s(k)).**
  - Let the dark vacuum be a Slater state filling the lower band on some open set B around the light node.
  - Write φ = u_a*. On B, φ lies in the upper band line, so the trigonometric-polynomial identity ⟨φ, σ·s φ⟩² = |s|²|φ|⁴ holds on B.
  - By real analyticity it holds on all of T³. Equality in Cauchy-Schwarz then makes φ(k) an eigenvector of σ·s(k) everywhere.
  - Near any node, both eigenline maps have degree ±1 on small spheres, so φ vanishes on each such sphere. By continuity u_a(K) = 0 at every node K, and likewise v_a(K) = 0.
  - Damping is therefore O(|q|²) against energy O(|q|) at every node: each doubler stays a sharp infrared mode.
- **Scope.** Linear, finite-range or analytic jumps; a Gaussian dark state; two bands. The multiband case is ARGUED, and nonlinear jumps and correlated dark vacua are untouched.
- **Answer to (i).** Record supplies irreversibility (breaking H3). Its permanence and one-per-site clauses send a Gaussian sink back to doubling. It supplies no U(1).

**O6 (LIT): where not-on-site symmetries stand.**
- **Fidkowski-Xu** (arXiv:2306.10105, PRL 131, 196601). A chiral U(1) with an exponentially local charge cannot act on a single Weyl fermion when sites are finite-dimensional. Not-on-site alone is therefore not enough for grade (A).
- **Thorngren-Preskill-Fidkowski** (arXiv:2601.04304). Gaugeable chirality via "symmetry disentanglers" under anomaly cancellation.
  - The fetched text says their construction needs infinite-dimensional rotors. It also reports a finite-dimensional commuting-projector obstruction for their 2+1D SPT.
  - Rotors conflict with H6.

## 3. Candidate routes, ranked

**R1 (top): symmetric mass generation (SMG) of one cubic-invariant mirror.**
- **Supplies:**
  - complex species with charges [S];
  - the landed naive walk;
  - a staggered form-factor mass [S];
  - a cube-local multi-fermion interaction [S].
- **Violates:** H5 only. H4 stays on-site, so the U(1) remains gaugeable, and H6 holds. No axiom sentence conflicts, and interactions are no more imported than any supplied dynamics clause.
- **Would show:** grade (B).
- **Test:** §5A.
- **Risks (LIT):**
  - Golterman-Petcher-Rivas 1993 (DOI 10.1016/0550-3213(93)90049-U) found the Eichten-Preskill model "Dirac-like everywhere".
  - Golterman-Shamir (arXiv:2603.15985) argue that if the mirror zeros are "kinematical", the spectrum "must be vector-like".

**R2: two copies plus an exact pair of non-commuting U(1)s (Gioia-Thorngren type).**
- **Supplies:** two identical Majorana copies (Yao-Lee c^x, c^y, already on main) and one network translation T.
- **Construction (EXACT).** The quadratic operator ô_X = (i/4) cᵀXc commutes with H = 1 ⊗ A whenever [X, 1 ⊗ A] = 0.
  - Q_0 = ô_{ε ⊗ 1}, which is on-site.
  - Q_1 = ô_X with X = ε ⊗ (T + Tᵀ)/2 + τ^z ⊗ (T − Tᵀ)/2. X is real antisymmetric and commutes with H because [T, A] = 0.
  - The Bloch form is S_1(k) = τ^y cos(k·a) ± τ^z sin(k·a), so S_1² = 1: Q_1 is quantized, nearest-neighbour along a, and not on-site.
  - [S_0, S_1] ∝ sin(k·a) τ^x ≠ 0. At a node with sin(k0·a) ≠ 0 the two copies form a doublet of an infrared su(2).
- **What it gives and does not give.**
  - Each U(1) on its own acts vectorlike (charges ±1), consistent with Fidkowski-Xu.
  - The pair matches the Gioia-Thorngren doublet (LIT, arXiv:2503.07708): "two exact U(1) symmetries that gives rise to the global SU(2) anomaly", protecting gaplessness "even when crystalline translations are broken".
  - This replaces "crystal momentum" with an exact lattice symmetry. The anomalous structure is not on-site, so it cannot be gauged, and the result is grade A in the SU(2) sense, not grade B.
- **Violates:** H4. The axiom text is silent on symmetries, so there is no conflict.
- **Test:** §5B.

**R3: record sink (O5).**
- **Violates:** H3, and the form is licensed by Record.
- **Status:** blocked at the Gaussian level by the budget lemma together with the dark lemma. The remaining opening is nonlinear jumps with correlated dark vacua, which is the SMG problem again.

**R4: routes needing more than the axioms give.**
- **Rotor disentanglers:** H6 / Qubit axiom.
- **Domain walls:** they need an extra dimension. With a finite internal width, the problem is O1 with more orbitals (the Spin(10) note, §3–4).
- **Floquet:** a translation-invariant Gaussian finite-depth circuit has U(k) = Π e^{−ih_j(k)}, which is homotopic to 1, so W_3[U] = 0 (EXACT). Whether that forces zero net chirality is Bessho-Sato's content (ARGUED). A W_3 ≠ 0 walk is not a nearest-neighbour circuit.

## 4. Derivation for R1: the natural home for SMG

**Step 1 (EXACT): the doubled spectrum.**
- Per species, the landed naive walk h(k) = Σ_a σ_a sin k_a has nodes at K ∈ {0, π}³ with chirality (−1)^r, where r counts the π components.
- The counts are 1 (+), 3 (−), 3 (+), 1 (−), summing to 0.

**Step 2 (EXACT): a covariant reduction from 8 nodes to 2.**
- **[S] term.** Add m Σ_x ψ_x† ε(x) [fψ]_x, with:
  - ε = (−1)^{x+y+z};
  - f = Σ_{j<l} C_j C_l − 3;
  - (C_jψ)_x = (ψ_{x+e_j} + ψ_{x−e_j})/2.
- **Symmetries.**
  - f has only even displacements, so [ε, f] = 0 and the term is Hermitian.
  - It is invariant under site rotations. Odd translations send m → −m: this is the chessboard sign, which the landed chessboard note shows a record checkerboard supplies as a staggered term.
- **Spectrum.**
  - The term couples k to k + Π with strength m f(k), where f(k + Π) = f(k) and h(k + Π) = −h(k).
  - So [[h, mf], [mf, −h]]² = (|s|² + m²f²)·1, giving E = ±√(|s|² + m²f²).
- **Zeros.**
  - f(0) = f(Π) = 3 − 3 = 0, while f = −4 at r = 1 and r = 2.
  - Exactly two nodes survive: the light node at 0 (chirality +) and one cubic-invariant mirror at Π (chirality −).
  - Their mutual coupling is m f ≈ −m|q|², a Wilson-like, irrelevant term.
  - Without interactions this is one massless Dirac fermion per species, as O1 requires.

**Step 3 (EXACT): anomaly bookkeeping.**
- The mirror has the same charges and the opposite chirality.
- Every polynomial anomaly of the mirror is minus that of the light content.
- So the mirror is symmetric-gappable only if the light content is anomaly-free.

**Step 4 (EXACT arithmetic, plus LIT): content counts.**
- **Minimal size (LIT).** For U(1) alone, the minimal number of Weyl fermions is 5 (Costa-Dobrescu-Fox, arXiv:2001.11991). For U(1)² it is 6 and for U(1)³ it is 8.
- **An explicit set (EXACT).**
  - For (1, 5, −7, −8, 9): Σq = 0 and Σq³ = 1 + 125 − 343 − 512 + 729 = 0.
  - No ± pair appears, so the set is chiral.
- **Spin(10) alternative.** The 16 of Spin(10) gives 16 species × 2 coin components = 32 modes per site. That is the q = 32 of the landed Spin(10) atom.
- **Global anomalies for Spin × U(1):** I recall there are none beyond the perturbative ones, but I did not verify this (ARGUED).

**Step 5 (EXACT): the interaction a covariant rule could provide.**
- **Composite field.** Define Ψ_c = (1/8) Σ_{y ∈ c} ε(y) ψ(y) on each unit cube c.
- **Form factor.** |b(k)| = Π_j |sin(k_j/2)|:
  - it is 1 at Π;
  - it is about |q_x q_y q_z|/8 at the light node;
  - it is 0 at r = 1 and r = 2.
- So any interaction in Ψ acts at full strength on the mirror and reaches the light mode only through q³ factors.
- **Covariance.**
  - Ψ_c → −Ψ_c under odd translations, so even-degree terms are translation-invariant.
  - Cube sums are rotation-covariant.
  - Spin-singlet contraction makes the terms covariant under the coin SU(2).
- **Support.** The terms live on one cube, the same support class as the landed Kitaev and Bravyi-Kitaev cube constructions. How that classifies under the owner's through/across reading is a supplied judgment.

**Step 6 (CHECKED): reducing the flavour symmetry.**
- Species are ordered (1, 5, −7, −8, 9), and n is the species-number change. Four quartic monomials, each U(1)_Q-neutral and a coin singlet:

| Monomial | n | Charge check |
|---|---|---|
| (Ψ_1Ψ_1)(Ψ_5Ψ_{−7}) | (2,1,1,0,0) | 2 + 5 − 7 = 0 |
| (Ψ_{−7}Ψ_{−7})(Ψ_5Ψ_9) | (0,1,2,0,1) | 5 − 14 + 9 = 0 |
| (Ψ_{−8}Ψ_{−8})(Ψ_{−7}†Ψ_9) | (0,0,−1,2,1) | 7 − 16 + 9 = 0 |
| (Ψ_1Ψ_9)(Ψ_5†Ψ_5†) | (1,−2,0,0,1) | 1 + 9 − 10 = 0 |

- **Rank.** The rank is 4: the third vector is the one with a −8 entry, and the other three are independent by direct elimination.
- **Residual group.** The 4×4 minor deleting column 1 is −2, so the residual group is U(1)_Q × Z_2. That Z_2 is fermion parity, since the component sums of n are 4, 4, 2, 0, all even. Fermion parity is not inside U(1)_Q, because −8 is even while 1 is odd.
- **Consequence.** No extra continuous symmetry, and hence no extra anomaly, protects the mirror. The necessary symmetry condition for SMG is met.
- **Lorentz caveat.** The monomials are lattice-scale operators, and not all of them are Lorentz scalars.

**Step 7: what is shown and what is open.**
- **Shown (under the supplied species, charges, f and interaction).** The doubling problem reduces exactly to symmetrically gapping one cubic-invariant mirror copy of an anomaly-free set. All symmetry and anomaly preconditions are met, and the light mode is coupled through q² (quadratic) and q³ (interaction) factors only.
- **Open.**
  - Whether a symmetric gapped mirror phase exists at intermediate coupling without pairing the light mode to a mirror bound state (the GPR failure).
  - Whether the mirror zeros escape the Golterman-Shamir criterion.
- **Strong-coupling limit (ARGUED).** The overlap {Ψ_c, Ψ_{c′}†} = |c ∩ c′|/64 is nonzero. The U → ∞ limit is therefore a non-commuting projector problem, and the Spin(10) note's product-atom deletion identity does not transfer to it.

## 5. Cheapest decisive computation (spec, not run)

**A: decisive for R1's mechanism, as a 1+1D analog of the post-Step-2 situation.** In 1D the naive chain already has just two nodes, 0 and π.
- **Inputs.**
  - A ring of L sites with four complex species A, B, C, D, one component each.
  - Hopping (iη_s/2)(c†_{j+1}c_j − h.c.), with η = (−1, −1, +1, +1).
  - Charges t = (3, 4, 5, 0) and s = (−4, 3, 0, 5).
  - The light modes at k ≈ 0 are then left-movers with charges (3, 4) and right-movers with (5, 0): the 3450 set, with anomaly 9 + 16 = 25 + 0 (EXACT). The mirror sits at π.
  - Bond composite Φ_{s,j} = (ε_j/2)(c_{s,j} − c_{s,j+1}), with form factor |sin(k/2)|.
  - Interaction U Σ_j (O_{ℓ1} + O_{ℓ2} + h.c.), point-split over adjacent bonds, with gapping vectors ℓ1 = (1, −2, 1, 2) and ℓ2 = (2, 1, −2, 1).
  - EXACT checks on these vectors: ℓ·t = 0 and ℓ·s = 0; they are null for K = diag(±1, ±1, ∓1, ∓1), with ℓ1ᵀKℓ2 = 0. They leave U(1)_t × U(1)_s.
  - Method: DMRG with local dimension 16 and L from 64 to 128.
- **Measurements.**
  - The entanglement central charge c.
  - The single-particle gap at k ≈ 0 and at k ≈ π, from momentum-twisted excitations.
  - The anomalous correlator between the light fermion and its three-fermion mirror composite.

| Outcome | Meaning |
|---|---|
| c = 4 at U = 0 | control |
| c = 2, gap at π but not at 0, no light–composite pairing | the cube/bond-composite SMG works in the analog; next step is a small 3D cluster test |
| c = 4 at all U | the interaction is irrelevant |
| c < 2, or symmetry breaking, or long-range pairing | the GPR failure is inherited; charged chirality must come from R2-type exact symmetries or non-Gaussian dark vacua |

**B: cheap exact check for R2.**
- On the landed two-copy hyperhoneycomb comparator from #9168 (κ = 0.3), build Q_0 and Q_1 from a network translation a.
- Verify [H, Q_1] = 0 in rational arithmetic and that the spectrum of Q_1 is integer.
- At each located crossing, check sin(k0·a) ≠ 0 and that S_0 and S_1 generate su(2) on the copy doublet.
- Pass means the framework's charged Weyl pair carries an exact Gioia-Thorngren Witten-anomalous doublet.

---

**10-line summary**
1. [EXACT] Static records act as product projections (deletions), so the projected problem keeps every N-N hypothesis and doublers return (matching the landed Spin(10) §4).
2. [EXACT] Majorana-network nodes carry real-representation, vectorlike content under any on-site symmetry; "Weyl's U(1) is crystal momentum" is exactly this.
3. [EXACT] Record does break H3 (irreversibility), and an anti-Hermitian Wilson damping leaves one long-lived Weyl node. But one-record-per-site makes a non-dark vacuum unsustainable.
4. [EXACT] With a dark Gaussian vacuum and finite-range jumps, the damping vanishes at every Weyl node by analyticity plus the monopole argument, so the record-sink route returns to doubling.
5. [EXACT] Two copies give, besides the on-site U(1), a quantized nearest-neighbour not-on-site U(1) Q_1. The pair is non-commuting and the node becomes an anomalous SU(2) doublet (matches Gioia-Thorngren, LIT). It is not gaugeable.
6. [LIT] Fidkowski-Xu rule out a quantized exponentially-local chiral U(1) on a single Weyl. The disentangler route needs infinite-dimensional rotors, which conflicts with the Qubit axiom.
7. [EXACT] Top route, SMG: a covariant staggered form-factor mass reduces the naive walk's 8 nodes to one light node plus one cubic-invariant mirror at Π. The mirror's anomaly is minus the light's.
8. [EXACT/CHECKED] Minimal anomaly-free U(1) content is 5 Weyl (LIT); (1,5,−7,−8,9) verified. Four cube-local quartic monomials leave exactly U(1)_Q × Z₂^F.
9. [ARGUED] Open: whether the mirror gaps without pairing to the light mode (Golterman-Petcher-Rivas, Golterman-Shamir). The overlapping-cube strong-coupling limit escapes the landed deletion identity.
10. [SPEC] Decisive next run: 1+1D DMRG of the four-species naive 3450 chain with a π-mirror and bond-composite gapping terms; central charge 2 versus 4. Plus a cheap exact Q_1 commutator check on the #9168 comparator.

Sources: [arXiv:2006.04204](https://arxiv.org/abs/2006.04204), [arXiv:2306.10105](https://arxiv.org/abs/2306.10105), [arXiv:2503.07708](https://arxiv.org/abs/2503.07708), [arXiv:2601.04304](https://arxiv.org/abs/2601.04304), [arXiv:2603.15985](https://arxiv.org/abs/2603.15985), [arXiv:2001.11991](https://arxiv.org/pdf/2001.11991), [Golterman-Petcher-Rivas, OSTI](https://www.osti.gov/etdeweb/biblio/6331144), [arXiv:2409.12220](https://arxiv.org/abs/2409.12220), [arXiv:2512.22609](https://arxiv.org/abs/2512.22609), [arXiv:2604.06307](https://arxiv.org/abs/2604.06307), [arXiv:2601.14359](https://arxiv.org/abs/2601.14359)