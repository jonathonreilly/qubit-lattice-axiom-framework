# C5 R12-3 report: twisted lattice SUSY outside class 𝒮. Is there a doubler-free gauge multiplet, and does Groot Nibbelink–Pospelov protection remove the electron–photon split?

**Author.** Claude Opus 5.5 probe. Same family as the supervisor and every C5 worker. Unrefereed. 2026-10-12, 19:09Z to about 19:55Z. No repository file was edited.

**Scratch.** `S/` = `.../scratchpad/C5/R12-3/`. Scripts and outputs are in `S/scripts/`. Each runs in under 40 s with `OMP_NUM_THREADS=2`.
- `r123_bf_multiplet.{py,out}`: the BF (cochain) multiplet. Algebra, doubler scan, box photon, Chern numbers, twisted-helicity content, and the cubic-covariance mixing table.
- `r123_untwist_count.{py,out}`: an illustration of Theorem U (random SO(3)-covariant Nicolai Hessians).
- `r123_kd_check.{py,out}`: the Kähler–Dirac photino of the equivariant completion.
- `r123_partner_loop.{py,out}`, `r123_partner_conv.{py,out}`: the Q-fixed photino–selectron vertex, its Ward identity, and the transverse part of the one-loop electron speed.
- `r85_box_qed_copy.py`, `r101_pairing.py`: unmodified copies of the R8-5 and R10-1 helpers.

**Read.**
- `docs/MINIMAL_AXIOMS_2026-06-29.md`, in full (`AX`).
- `TESTS.md`:
  - the C5 method (`:2302-2320`);
  - R10 referee results and R11 worker readings (`:4268-4331`);
  - R12-3 (`:4373-4390`).
- R10-5: the report, `C5_R10-5_referee.md`, the verdict, and `scripts/C5/R10-5` (the partner-loop code was reused).
- R10-1: the report and verdict.
- R11 referee results, appended at `TESTS.md:4392` while this probe ran. R11-1 (a) is DERIVED: both statistics are necessary. That is consistent with this report and is not used.
- R8-5: the report (BQ law, vertex, Lemma C).
- O3: the report (Theorem 2, FS models).
- `TESTS.md:1172` (RC C1 Lemma R).

**Labels.**
- **proved**: complete under the stated hypotheses.
- **checked**: numerics here.
- **suggested**: argued, not proved.
- **reading**: an interpretation.
- **comparator**: literature. V = verified this session (abstract or search level); R = recalled, not verified.

---

## 0. In plain words

1. **The topological obstruction can be evaded, but only in one way.**
   - R10-5's photon doubling (Lemma PD) comes from the photon's helicity "charge" ±2 at q = 0. A doubler-free lattice photon multiplet needs massless partners carrying the opposite charge.
   - Neutral scalars mixed into the superpotential cannot supply it, however many there are: cubic covariance forbids their linear mixing with A (Lemma PD₁; proved and checked).
   - What can supply it: a neutral *vector* partner. The cheapest construction is a BF superpotential on the lattice's cochains, W = ⟨B, dA⟩ + ⟨τ, dB⟩, with B on plaquettes and τ on cubes.
     - Its square is exactly Maxwell plus massless B and τ.
     - The photon and photino are doubler-free, exactly relativistic inside R8-5's momentum box, and gauge invariant.
     - The total Chern number is 0.
     - This is proved and checked to 1e-15.
   - So the Chern obstruction does **not** extend to every twisted or mixed class.
2. **That multiplet's photino has the wrong spin.**
   - Under lattice rotations the BF photino carries helicities ±1, ±1, 0, 0. These are integer-spin fermions.
   - No internal symmetry can "untwist" them into spin-½ particles.
   - Theorem U (proved by counting, under stated hypotheses): **in Nicolai (SUSY quantum-mechanics) form on the gauge quotient, a doubler-free photon multiplet and an untwistable (spin-½) photino are incompatible.** This holds for any content of scalar and vector fields.
   - By the spin–statistics theorem (comparator), such a law cannot have a local, Lorentz-invariant continuum limit.
3. **The twisted N = 2 route is closed in its natural class.** Its photino (the "odd-signature" operator) carries Chern +2, so with a conserved fermion number it has doublers (Lemma PD₂; proved and checked).
4. **What survives is twisted N = 4.**
   - Completing BF equivariantly, with a complex scalar σ and a site fermion η, gives a full Kähler–Dirac photino. Its Chern number is 0, it is untwistable, and K² = Δ, so it is doubler-free (checked).
   - Its content is the abelian N = 4 multiplet: the photon plus 6 massless neutral scalars. This is consistent with Catterall's lattice N = 4 (comparator V).
   - It is **not built here** with charged matter, its equivariant Hamiltonian is not written, and its 6 massless scalars couple to the electron at strength e.
5. **Groot Nibbelink–Pospelov (GNP) protection cannot operate on Z³ × ℝ.**
   - GNP needs momentum in the supersymmetry algebra. Every lattice supercharge here squares to H alone.
   - Rescaling the gauge multiplet's superpotential keeps Q exact and the Ward identity intact, and changes c_γ/c_e freely. So **no lattice supercharge relates the electron and photon speeds** (Theorem L; proved for the Nicolai class).
   - An additive momentum in the algebra is excluded by Lemma R (suggested).
   - Computed:
     - the photon's one-loop matter loops cancel (R10-1 Theorem P, matched);
     - the photon loop leaves the electron at −17.96 / −10.66 (refereed);
     - the transverse part of the Q-fixed partner loop adds about −9 to −11 per e²/16π², with an IR mass dependence. That signals the computation is incomplete: the dressing terms are not computed.
   - No vanishing of c_e − c_γ was found, and none is protected.
6. **Against the FIXED readings: INCONCLUSIVE** (worker reading).
   - **No PASS.** No law meets all of: exact Q, Ward identity, doubler-free photon, and one-loop c_e − c_γ = 0.
   - **No FAIL for the whole class.** The Chern obstruction is evaded by the BF and Kähler–Dirac constructions.
   - **Bounded no-gos offered to the referee:** PD₁ (Nicolai with scalar mixing), PD₂ (twisted N = 2 with a conserved ghost number), Theorem U, and Theorem L.

---

## 1. Hypotheses and classes (stated before any title)

- **H-lat.** Z³ × ℝ, continuous time. Translation invariance and the *proper* cubic group O (`AX:37-41`).
  - Symbols are C¹, periodic and translation invariant.
  - The photon symbol is either the cochain symbol D_j = e^{iq_j} − 1 or R8-5's box symbol D_j = i d(q_j)e^{iq_j/2}, with d = ρq + (1 − ρ)2 sin(q/2) and plateau (c₁, c₂) = (1, 2).
  - The matter is R10-5's Theorem Q multiplet (8-component Clifford-flat fermion plus 8 real bosons, M² = E²), complexified per Lemma J (onsite-charge version): 16 + 16 per site.
- **Class 𝒩 (Nicolai / SUSY-QM on the gauge quotient).**
  - Real bosonic coordinates x with one complex fermion per coordinate. Q = Σψ†(p − i∂W), with W real and gauge invariant.
  - Physical states are the basic forms: Gauss law G|ψ⟩ = 0 and the horizontal condition ι_v|ψ⟩ = 0 (Witten's SUSY-QM on X/G; comparator R).
  - The fermion one-particle operator is the Hessian C restricted to the physical subspace.
  - 𝒮 (R10-5) ⊂ 𝒩 is the case with A only.
- **Class 𝒩_{0,1}.** Class 𝒩 with the massless sector's fields in ℓ = 0 or ℓ = 1 of the emergent SO(3), and the massless sector's C linear in q near 0, nonsingular for q ≠ 0 small. That is, the massless sector is relativistic with no extra zero modes at q → 0.
- **Class 𝒯₂ (twisted N = 2, Hamiltonian).** A conserved fermion number U(1) (ghost number) commuting with H. The photino one-particle operator near q = 0 is the odd-signature operator on (η ∈ Ω⁰, ψ ∈ Ω¹), i.e. Floer's extended Hessian (comparator R). C¹ translation-invariant symbol.
- **Untwisting (H-tw).** The physical rotation is the lattice (twisted) rotation composed with an internal SU(2)_R commuting with H, and physical photinos have spin ½ (no physical helicity ≥ 3/2). This is the standard reading of twisted lattice SUSY (comparator R).
- **Excluded, not addressed:**
  - Euclidean lattices: Sugino, Catterall's A4*, DKKN links. These are set B, where hypercubic or A4* time–space symmetry, not SUSY, acts on the cone (F2).
  - Compact links.
  - Non-C¹ symbols.
  - Light-cone supercharges with a non-additive P̃.
  - Two loops.
  - The quotient-metric and horizontal-dressing O(e²) terms in the electron self-energy (§3.6).
  - Nonabelian gauge groups.

## 2. Prior art (each counted once)

- **R10-5** (CWC, FAIL bounded to 𝒮; `TESTS.md:4303-4310`; `C5_R10-5_report.md:162-179`).
  - Lemma PD: C₁ = ±iε·q with Chern ±2 forces transverse zeros.
  - Theorem Q; Lemma J (onsite-charge version).
  - §3.4: in 𝒮, C → λC keeps Q exact (`C5_R10-5_report.md:188`).
  - The referee confirms that GNP assumes the full supercharge-and-translation algebra (`C5_R10-5_referee.md:34`).
- **R10-1** (CWC): Theorem P, the photon cancellation; the electron residual is −17.96 / −10.66 at N = 224 (`C5_R10-1_referee_verdict.md:7-9`).
- **R8-5** (CWC): the BQ vertex and Ward identity (`C5_R8-5_report.md:133-140`); Lemma C and Theorem B.
- **O3** (CWC): Theorem 2 (nilpotent Q ⇒ E₀ = 0 under Q-preserving deformations); P-site prices.
- **RC C1 Lemma R** (CWC): the C¹ invariants of normal collisions are λE + b·k + c (`TESTS.md:1172`).
- **Comparators.**
  - Groot Nibbelink–Pospelov, hep-ph/0404271 (V, abstract): in the supersymmetric SM, LV operators have dimension ≥ 5. The algebra assumption is from the R10-5 referee.
  - Kaplan–Katz–Ünsal, hep-lat/0206019 (V, abstract): spatial-lattice SUSY, including N = 4 SYM in 3+1.
  - Catterall, hep-lat/0503036 (V, search-level summary): N = 4 SYM on A4*, local, gauge invariant, doubler-free, with one exact nilpotent scalar Q. The fermions form a Kähler–Dirac field, from the Marcus twist.
  - Sugino, hep-lat/0311021 (V, search level): hypercubic, Euclidean, Q nilpotent up to gauge transformations.
  - D'Adda–Kanamori–Kawamoto–Nagata link approach (V that it exists and that critiques exist; content R).
  - Berruto–Diamantini–Sodano, hep-th/0004203 (V via the R10-5 referee).
  - Spin–statistics (Pauli 1940; Weinberg's massless-field theorem) (R).
  - Marcus / Kapustin–Witten twist with complexified connection A + iφ and Morse function Im CS (R).
  - Becher–Joos Kähler–Dirac lattice fermions (R).
- **Repo:** `YT_CLASS_3_SUSY_2HDM_ANALYSIS_NOTE_2026-04-18.md:470-535` (no SUSY retained), as cited in R10-5.

## 3. Results

### 3.1 Lemma PD₁: neutral scalar mixing cannot cure the doubling. Proved; checked

- **Claim.** In class 𝒩 with A plus any number of neutral fields in the irreps A₁, A₂, E or T₂ of O, with any masses and any C¹ mixing in W, the photon has extra transverse zeros on T³. The one exception is massless scalars whose quadratic block is degenerate on a sphere (a non-generic edge case).
- **Proof.**
  1. **Linear mixing.** Transverse linear A–field mixing needs an O-invariant tensor in T₁(q) ⊗ Γ ⊗ T₁ that is antisymmetric in (A-index, q). Its dimension is 0 for A₁, A₂, E and T₂, and 1 only for T₁ (checked by solving the covariance and transversality equations, `r123_bf_multiplet.out` (6)).
  2. **Scalar self-blocks.** Their linear terms vanish too, since T₁ ⊗ Γ ⊗ Γ′ ∌ A₁ for Γ, Γ′ ∈ {A₁, A₂, E}.
  3. **The non-photon block.** Near q = 0 it is either constant (massive: a trivial bundle) or even in q (massless: c₁ = 0, because the bundle is pulled back from RP², and H²(RP²; ℤ) = ℤ₂ maps to 0 in H²(S²; ℤ)). The O(q²) mixing does not close the O(|q|) photon gap.
  4. **Contradiction.** So c₁(P₊) on a small sphere is the photon's ±2 + 0. R10-5's punctured-torus argument (refereed) then applies. ∎
- **T₂ fields** can mix among themselves through a curl and are then "vector-type". They are not scalar mixing.
- **Scope.** This covers R10-5's named escape "A–scalar mixing" when the partners are scalars. It does not cover vector partners (§3.2).

### 3.2 The BF multiplet: a doubler-free Nicolai photon. Proved; checked

- **The law (gauge part).** A ∈ Ω¹ (links), B ∈ Ω² (plaquettes), τ ∈ Ω³ (cubes), all non-compact:

  W = ⟨B, dA⟩ + ⟨τ, dB⟩,  C = [[0, d₁†, 0], [d₁, 0, d₂†], [0, d₂, 0]].

- **Gauge invariance.** W depends on A only through F = dA, so C(d₀λ, 0, 0) = 0. Checked to 5e-16.
- **Maxwell emerges.** The boson potential is ½|∂W|² = ½|F|² + ½⟨B, ΔB⟩ + ½⟨τ, Δτ⟩. The cross term ⟨dA, d†τ⟩ vanishes because d² = 0. Symbol identity checked to 4e-15.
  - This is the BDS cure, a Maxwell term, but obtained *inside* the gradient form. The R10-5 referee's remark that "adding Maxwell breaks Q" (`C5_R10-5_referee.md:26`) does not apply, because the Hessian is enlarged rather than modified.
- **Spectrum.** C² = Δ·P_phys exactly, with Δ = Σ|D_j|². So the photon, photino, B and τ all have ω² = Δ, with zeros only at q = 0.
  - Doubler scan, N = 16 and 24, cochain and box: the minimum nonzero |eig| sits at the grid point nearest 0 and equals √Δ there.
  - Control: the class-𝒮 curl iε·sin q has transverse zeros at (π,0,0), (π,π,0) and (π,π,π).
- **Box photon.** Inside the photon plateau, eig C = ±|q| (three times each) and 0 (gauge), to 1e-12 (`r123_bf_multiplet.out` (2)). Per-axis box symbols commute, so d² = 0 survives (proved).
- **Chern bookkeeping** (`r123_bf_multiplet.out` (4), Fukui–Hatsugai on |q| = 0.05):

| operator | rank P₊ | c₁ |
|---|---|---|
| class-𝒮 lattice curl (R10-5 control) | 1 | +2.0000 |
| continuum curl iε·q | 1 | +2.0000 |
| continuum odd signature (σ, A): twisted N = 2 photino | 2 | +2.0000 |
| BF continuum / cochain lattice / box lattice | 3 | 0.0000 / 0.0000 / 0.0000 |
| Kähler–Dirac Ω⁰…³ (cochain) | 4 | 0.0000 |

- **Why the BF Chern number is 0 (proved).** C is odd under (−1)^deg, i.e. chiral. The positive eigenbundle is then the graph of a unitary from the even bundle (B) to the odd bundle, so it is isomorphic to a trivial bundle.
- **Exact supercharge (proved, standard).** Coupling to matter: W_tot = W + ½⟨φ, M_Aφ⟩, with M_A the Peierls-dressed Clifford M, real symmetric for every A.
  - Q = d_W = e^{−W}de^{W} on forms on X is nilpotent for any W.
  - The gauge vector fields v_λ are isometries with v_λ(W) = 0. Cartan's formula gives {Q, ι_v} = L_v, which is the Gauss generator G including fermions, and [Q, G] = 0.
  - So Q preserves basic forms and is exact on the physical space.
- **Ward identity.** The Q-fixed photino–electron–selectron vertex is V_j = eJ[h_j(−p) − h_j(−k_s)]/(−D̄_j). It obeys Σ_j D̄_jV_j = −eJ[h(−p) − h(−k_s)] (checked to 5e-16 over 400 random momenta, cochain and box). The electron vertex is R8-5's.
- **Caveat on locality (proved, short computation).** The *local* ambient Hamiltonian ½{Q, Q†_flat} does not preserve the horizontal constraint:
  - {Q†, ι_v} = −iΣ_{a,b}(∂_a v_b)ψ_aψ_b ∝ eλ Σ J_{ab}ψ_{φ,a}ψ_{φ,b} ≠ 0, because ∂_φ v_φ = eλJ is antisymmetric and nonzero.
  - So the honest Hamiltonian lives on X/G with the quotient metric g = flat − e²(Jφ)(Δ + e²|φ|²)⁻¹(Jφ)ᵀ. That metric is non-local, Coulomb-like, and enters at O(e²).
  - Reading: its local completion is the Cartan (equivariant) model, which adds σ and η (§3.5).

### 3.3 Theorem U: in class 𝒩, doubler-freeness and spin-½ photinos are incompatible. Proved under H-tw and 𝒩_{0,1}; checked

- **Claim.** Take a photon multiplet in 𝒩_{0,1} with n_V vector fields (n_G ≥ 1 of them gauge, the photon included) and n_S massless scalars. Its massless sector cannot be simultaneously:
  - (i) nonsingular near q = 0, i.e. no extra zero modes; and
  - (ii) untwistable to spin-½ photinos (H-tw).
- **Proof.**
  1. **The general linear form.** SO(3) covariance, reality and Hermiticity give C₁ = a ⊗ iε·q (a real symmetric) on the vectors, scalar–vector terms K q_j (longitudinal only), and no scalar–scalar terms.
     - Gauge invariance kills K on the gauge longitudinals.
     - The vector–vector linear term (ε) annihilates longitudinals.
  2. **Nonsingularity.** The helicity-0 block is [[0, |q|K], [|q|Kᵀ, 0]] between the n_S scalars and the n_V − n_G physical longitudinals. It is nonsingular only if n_S = n_V − n_G.
  3. **The helicity count.** The twisted-helicity multiset of all one-particle fermion states at momentum q is {+1 × n_V, −1 × n_V, 0 × (n_V − n_G + n_S)}. Particles come from the positive band; antiparticles are holes, which keep the missing state's helicity.
  4. **Untwisting.** Under H-tw, every SU(2)_R multiplet must be a doublet with adjacent twisted helicities (h, h − 1). Spin-3/2 multiplets would need |h_tw| = 2. So #0 = #(±1), i.e. n_V − n_G + n_S = 2n_V.
  5. **Contradiction.** Steps 2 and 4 together force n_G = 0. ∎
- **Checked** (`r123_untwist_count.out`, random a and K): every nonsingular content has n_S = n_V − n_G and is not pairable; every content with n_S > n_V − n_G has exact zero modes.
  - BF (n_V, n_G, n_S) = (2, 1, 1): helicities {±1, ±1, 0, 0}; c₁ = 0; not untwistable (`r123_bf_multiplet.out` (5): positive band {−1, 0, +1}).
- **Consequence (suggested; comparator R).** The BF photino is a set of integer-twisted-spin fermions with causal local anticommutators and positive energy. By spin–statistics no such local field theory is Lorentz-covariant, so the BF law's continuum limit is not Lorentz invariant.
  - The IR mass dependence in §3.6 is *consistent* with this but does not establish it (see §3.6).
- **Meaning.** In SUSY-QM (Nicolai) form, R10-5's Chern obstruction trades for a spin obstruction. The escape needs fermions not one-per-quotient-coordinate: an equivariant η paired with the longitudinal photino.

### 3.4 Lemma PD₂: the twisted N = 2 photino has doublers. Proved; checked

- **Claim.** In 𝒯₂ the photino's positive band near q = 0 carries c₁ = ±2 (checked: +2.0000 for the continuum odd-signature operator). This is two Weyl fermions of the same chirality under the conserved ghost number.
  - With a C¹ symbol gapped on T³ ∖ {0}, R10-5's punctured-torus argument applies verbatim to the fermion operator. So extra zeros are forced: the Nielsen–Ninomiya form of Lemma PD. ∎
- **Escapes (named):**
  - break the ghost-number U(1), i.e. a Majorana photino; but twisted Q has ghost number +1, so this leaves 𝒯₂;
  - add opposite-chirality partners. This is N = 2 vector plus adjoint hyper = N = 4 (§3.5).
- **Scope.** That the Hamiltonian twisted N = 2 photino operator near 0 is the odd-signature operator is the comparator (Floer/Witten), recalled. The helicity content {+1, 0} and {0, −1} (`r123_bf_multiplet.out` (5)) matches the N = 2 twist: (½)_spin ⊗ (½)_R.

### 3.5 What survives: the Kähler–Dirac (twisted N = 4) photon multiplet. Checked for the free photino; the law is not built

- **The photino.** The Cartan-model completion of BF adds σ (complex, on sites) and η ∈ Ω⁰. Its photino is the full Kähler–Dirac operator K = d + d† on Ω⁰…³ (8 complex per site):
  - K² = Δ·1₈ to 4e-15 (cochain and box), so it is doubler-free;
  - chiral, so c₁ = 0;
  - twisted helicities {+1, 0, 0, −1} per band, so untwistable as 2 × (½ ⊗ ½_R) (`r123_kd_check.out`; `r123_bf_multiplet.out` (4)–(5)).
- **Bosons.** A_T (2) + B (3) + τ (1) + σ (2) = 8. These are the photon plus 6 neutral massless scalars, the abelian N = 4 content.
  - Reading: this is the Marcus/KW-twisted N = 4 multiplet, in which B ≅ the 1-form scalar φ and W = Im CS(A + iφ) is BF at the abelian level (comparator R).
  - It agrees with Catterall's Kähler–Dirac N = 4 lattice construction (comparator V), but in Hamiltonian Z³ × ℝ form.
- **Not done:**
  - the equivariant Hamiltonian (Q² = H + G(σ));
  - the coupling to charged hypermultiplets, which breaks N = 4 to N = 2 (the N = 4 photino is already Chern-neutral, so the hypers need not cancel any photino charge);
  - the proof that one twisted Q survives with matter on Z³ × ℝ.

  All open.

### 3.6 Part (c): c_e − c_γ

- **Theorem L (no supercharge relation between c_e and c_γ). Proved in 𝒩; suggested for equivariant/twisted classes.**
  - In 𝒩, replace W_gauge → λW_gauge. Q stays exact (any W). Gauge invariance and the Ward identity are unchanged (W_gauge is still gauge invariant, and the matter vertex does not involve W_gauge). The tree speeds become c_γ = λ, c_e = 1.
  - So c_γ − c_e is not constrained by Q, at tree level or at any loop order.
  - In twisted classes the gauge action is Q-exact (comparator R), so an anisotropic Q(δΛ_gauge) does the same. Suggested.
- **Why GNP has no lattice counterpart (suggested).**
  - GNP's dimension-5 bound uses {Q_α, Q̄_β̇} = 2σ^μP_μ: one P^μ shared by every superfield (`C5_R10-5_referee.md:34`).
  - On an interacting Z³ × ℝ law with umklapp (forced by R8-5 Theorem B: the photon couples to every charged mode), an additive conserved one-body P̃ in {Q, Q†} must be a C¹ collision invariant. By Lemma R (`TESTS.md:1172`) that is λE + b·k + c, and periodicity forces b = 0.
  - So {Q, Q†} ∝ H + cN, with no momentum, and no species-universal metric is enforced.
  - The step "superalgebra element ⇒ additive one-body collision invariant" is assumed, not proved.
- **What is computed, at one loop, in the BF + matter law (matched masses).**
  - **δc_γ.**
    - The matter loops cancel: R10-1 Theorem P with the J-doubled content (1 Dirac(4) : 2 complex scalars).
    - The one-loop A–B mixing through the selectron loop vanishes: tr[(1 ⊗ J)(Clifford ⊗ J)] = 0. Checked at trace level; this matters because B is degenerate with the photon.
    - The photon has no photino coupling at this order.
    - So δc_γ = 0 (checked within these pieces).
  - **δc_e, photon loop:** −17.96 (Wilson) and −10.66 (box) (refereed R10-1).
  - **δc_e, Q-fixed photino–selectron loop, transverse part only** (coupling e, no free y; `r123_partner_loop.out`, `r123_partner_conv.out`):

| curves | m = 0.1 (N = 48 / 64 / 96) | m = 0.05 (N = 64 / 80 / 96) | m = 0.025 (N = 96) |
|---|---|---|---|
| Wilson electron / cochain photino | −8.88 / −9.01 / −9.08 | −9.88 / −10.13 / −10.27 | −10.88 (under-resolved) |
| box b₁ = 0.8 electron / box photino | −9.56 / −9.69 / −9.76 | −10.56 / −10.81 / −10.96 | −11.56 (under-resolved) |

  - **Reading of the table.**
    - The partner piece has the same sign as the photon loop.
    - It grows by about 1.3 per halving of m, roughly −2 ln(1/m). That is an IR, in-box non-covariance of the *transverse piece*.
    - In Coulomb-gauge QED the transverse photon alone is also non-covariant, and the instantaneous Coulomb term restores covariance. Here the analogue is the horizontal (fermionic-Gauss) dressing plus the O(e²) quotient-metric terms of §3.2. These are not computed.
  - **So no physical one-loop c_e − c_γ is claimed for the Q-exact law.**
    - The sum of computed pieces, about −27 to −29 per e²/16π², is not a result.
    - What is established: nothing in the construction forces cancellation (Theorem L), and every computed piece is negative.

### 3.7 Per-site content and prices (named, not adopted)

- **P-site.**
  - **BF gauge multiplet:** 7 real non-compact CCR coordinates per site (A: 3, of which 1 is gauge; B: 3; τ: 1), plus 7 complex CAR modes, of which 6 are physical after the horizontal constraint.
  - **Equivariant (N = 4) version:** add 2 real CCR (σ) and 1 CAR (η): 8 physical CCR and 8 CAR.
  - **Charged matter:** 16 real CCR plus 16 CAR (Lemma J, onsite charge).
  - All of this sits against the Qubit fibre M₂(ℂ) (`AX:43-53`): graded composition and infinite-dimensional bosons on links, plaquettes and cubes (O3 Prop. 3).
- **P-dyn.** H = {Q, Q†} on basic forms is not supplied by Admissibility (`AX:116-130`).
  - The local form needs the equivariant completion.
  - The basic-form form needs a non-local O(e²) quotient metric.
- **P-spin (BF).** Integer-twisted-spin photinos (Theorem U). No Lorentz-invariant local continuum (suggested, via spin–statistics).
- **P-neutral.**
  - BF: 4 massless neutral bosons. B couples to curl j at O(e), a magnetic-dipole-strength long-range coupling (reading).
  - N = 4: 6 massless neutral scalars with O(e) Yukawas to the electron. Fifth-force and equivalence-principle bounds exclude these unless they are massive (comparator R). Masses break SUSY softly, which brings back O3/R10-1 residuals.
- **P-match.** A selectron degenerate with the electron (R10-5; comparator R excludes it).
- **P-noP.** No momentum in the lattice superalgebra (Theorem L), so c_e − c_γ is unprotected. R8-5's tuned relative-speed counterterm (about 1 part in 1e16–1e17) stays the price.

## 4. Against the FIXED readings (`TESTS.md:4387-4390`)

**Worker reading: INCONCLUSIVE.** Same family; the referee is required for the bounded no-gos below.

- **PASS: not met.** The registered conditions, in turn:
  - Exact supercharge and Ward identity, with a doubler-free photon: **met by the BF law** (§3.2). But its Hamiltonian is either non-local (quotient metric) or needs the unbuilt equivariant completion. Its photino violates the untwisting condition (Theorem U).
  - One-loop c_e − c_γ vanishing, or dimension-5-suppressed, for every edge shape: **not shown**, and not protected (Theorem L; no momentum in the algebra). The computed pieces are all negative. The full Q-exact one-loop value is not computed (dressing terms).
  - The N = 4 candidate (§3.5) is not built with charged matter.
- **FAIL ("a refereed no-go extending R10-5's Chern obstruction to the twisted or orbifold class"): not met for the class.** The obstruction is evaded by a vector partner: BF in Nicolai form, and Kähler–Dirac in equivariant form. Both give c₁ = 0 and are doubler-free (proved; checked).
  - **Bounded extensions offered to the referee:**
    - **PD₁:** Nicolai class with any neutral scalar mixing (A₁/A₂/E/T₂): doublers forced.
    - **PD₂:** twisted N = 2 with conserved ghost number: doublers forced (photino-side Nielsen–Ninomiya).
    - **Theorem U:** in 𝒩_{0,1}, doubler-free ⇒ not untwistable.
    - **Theorem L:** no lattice supercharge in 𝒩 relates c_e and c_γ.
  - If the referee reads R12-3's FAIL as satisfiable on the named escape "twisted N = 2 equivariant constructions with the scalar a", then PD₂ meets FAIL bounded to 𝒯₂. I flag this rather than choose it.
- **The record, if confirmed.**

  > "The lattice photon multiplet's Chern charge can be cancelled only by vector partners (BF/Kähler–Dirac, i.e. N = 4 content). In Nicolai form that costs integer-spin photinos (Theorem U); twisted N = 2 keeps the doublers (PD₂); the equivariant N = 4 route is open but not built. No lattice supercharge relates c_e and c_γ (no momentum in the algebra), so GNP protection does not transfer to Z³ × ℝ. The electron–photon split remains unremoved and unprotected."

## 5. Strong-word check

- **"Exact":**
  - d² = 0 and C² = Δ·P_phys (symbol identities, checked to 4e-15);
  - Q² = 0 on basic forms (Cartan/Witten, standard);
  - the Ward identity of the Q-fixed vertex (algebraic, checked to 5e-16);
  - box ω = |q| inside the plateau (checked to 1e-12).
- **"Doubler-free":** zeros only at q = 0, because C² = Δ and Δ > 0 off 0 (cochain and box). The grid scans illustrate this; the proof is the identity.
- **"Proved":**
  - PD₁ (representation theory plus R10-5's topology; the even-map step holds generically);
  - BF's c₁ = 0 (chirality);
  - Theorem U (counting, under H-tw and 𝒩_{0,1});
  - PD₂ (topology, given the comparator's near-0 form);
  - Theorem L in 𝒩.
- **"Suggested":**
  - the spin–statistics consequence;
  - Theorem L outside 𝒩;
  - the no-P argument via Lemma R;
  - "the N = 4 candidate is the cheapest that survives".
- **"Checked":** every table number. The partner-loop code is validated only internally: the Ward identity, the projector check, and reuse of R10-5's referee-confirmed RS structure. The m = 0.025 rows are under-resolved.
- **Not claimed:**
  - any physical value of c_e − c_γ for a Q-exact law;
  - anything about Euclidean (set B) twisted lattices;
  - the nonabelian case;
  - two loops.

## 6. For the referee

1. **PD₁:** the O-irrep table (`r123_bf_multiplet.py` part 6), and the even-block c₁ = 0 step via RP².
2. **BF:** check C·gauge = 0, C² = Δ·P_phys and c₁ = 0, and whether the chiral-graph argument is complete. Also whether the locality caveat ({Q†, ι_v} ≠ 0) is computed correctly.
3. **Theorem U:** the general SO(3) linear form; the hole-helicity convention; the doublet-pairing criterion (#0 = #±1); and whether H-tw is the right reading of "untwistable".
4. **PD₂:** whether the Hamiltonian twisted N = 2 photino operator is the odd-signature operator with conserved ghost number.
5. **Theorem L and the Lemma R step.**
6. **The partner loop:** vertex convention, and whether the IR log can be cancelled by the dressing terms.

**Downloads:** none. Web lookups were abstract or search level only: hep-ph/0404271, hep-lat/0206019, a search for Catterall hep-lat/0503036, and a search for Sugino and DKKN.
