# L5-O, pass 1: the spinor and singlet questions of the Majorana five-mode law

Written 2026-11-05 by a Claude Opus 5.5 subagent, as pass 1 of the open items LW1-5-16 and LW1-5-Σ of `LW1_5_DRAFT.md`, with the SU(2) question for T0 (method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation (`check2.py` in `/private/tmp/claude-501/-Users-jonreilly-Projects-Physics--claude-worktrees-peaceful-yalow-de8f06/bd9fd3c1-9024-4004-87d2-e8917bcfe6a3/scratchpad/lw15o/`, under 100 MB, about 12 s); a check guides and never proves. Nothing here is a verdict. The sibling lane `LW1_5U_DRAFT.md` (the law `L5-U`) was not read and is not used.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `toe-assembly-local` (same commit as `origin/claude/toe-assembly`) | `e648fa3e0f` |
| `origin/claude/toe-why-five-modes-20261021` (#10014, closed) | `3d00c61f05` |
| `origin/claude/toe-composite-sixteen-20261021` (#10027, closed) | `fc76a41135` |

Files read at those commits, by line: `LW1_5_DRAFT.md` lines 1-510 (all); `TOE_ASSEMBLY.md` lines 125-144 (PS-5, PS-6, PS-7), 201-209 (section 3.4, D1), 342-417 (MT1, GA1, GA2, CH1, CG1), 464-476 (VC1), 528-549 (section 6, T0); `LW1.md` lines 26-50 (definitions, gauge-invariant states) and 176-179 (Lemma A1); the #10027 note `docs/SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md` (all 179 lines, by `git show`); the #10014 note `docs/FIVE_MODES_PER_SITE_ARE_THE_SMALLEST_ANOMALY_FREE_PROTECTED_SPIN2N_CONTENT_BOUNDED_THEOREM_NOTE_2026-10-22.md` lines 1-12, 34-42, 76-84, 158-176 (by `git show`); PR #10027's page (`gh pr view 10027`: title, state CLOSED; its body has an empty "Scope:" line, so the scope is quoted from the note's frontmatter).

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". PS-5, PS-6 and PS-6r are read plainly. Where the words allow more than one reading, each reading is named and treated, and nothing is adopted. Every choice considered carries the four-test check (section 5).

**Working set used, by name.** PS-5 (fallback text, D1), PS-6 and PS-6r (frames and registers), PS-1c (only through `L5-O`'s gates), PS-7 (only in section 3.5). Results used from `LW1_5_DRAFT.md`, cited by name there: Theorem C, Lemma C1, Theorem M, Lemma Q, Theorem G, Corollary R.1, Proposition Σ, Lemma Z, Proposition A, Lemma A1 (from `LW1.md`). PS-2, PS-3, PS-4 are not used.

---

## 0. The questions, quoted

`LW1_5_DRAFT.md` line 231 (Proposition Σ): "Suppose every link register is a representation on which `−1 ∈ Spin(20)` acts as one scalar `ε = ±1` ... Then at every site, `−1 ∈ Spin(10)` acts on the space of the site and its six link ends as the scalar `−1`. So no vector there is invariant under the local `Spin(10)`: the Gauss singlet sector is empty at every site."

Line 240 (Lemma Z(iii)): "every gauge-covariant local operator transforms under the gauge group by a true `SO(10)` representation, and if it is fermion odd, `−1_{10}` acts on it as `−1`: it is in the vector class (`10`, `120`, `126`, …). No local operator transforms as a spinor `16`."

Line 244: "Mixed-class registers (both classes in one register) admit operators that change a link's class; such operators can carry the spinor class. ... Whether that is a usable escape is open (**LW1-5-16**)."

Line 458: "**LW1-5-Σ (OPEN, owner/VC1).** Whether VC1 needs a pure Gauss-singlet vacuum. If yes, `L5-O` needs two register classes (choice c10), which fails test 4 today."

`TOE_ASSEMBLY.md` line 205 (D1's check): "Test 3: passes. It does not put in the 16; #10027 shows site-bilinear `Spin(10)` on five-mode sites gives "vector class, never the 16"." The #10014 conditions, its lines 163-164: "(a) the frame group is the full Spin(2N); (b) the content is one parity half, read as Weyl species".

#10027 claim_scope (in part): "every fermion-parity-odd excitation is in the vector class (10, 120, 126, ...), never a spinor 16."

## 0.1 Outcome in one paragraph

**The obstruction is about the matter field, not the states, and no finite register choice removes it.** Under every Spin(10) that acts on a five-mode site by Bogoliubov frames, the site algebra is the exterior algebra `Λ(10)` (Lemma F), and the implementer of `−1` on the site is the number `−1` (Lemma K0). So matter never carries a spinor-class charge relative to any state, under every register choice and every law with an exact Gauss law (Theorem K). Mixed-class registers do give local gauge-covariant operators in the spinor class: at two sites for `so(20)` registers, and, for a wider register in PS-6r's wording, a fermion-odd one with a half-spin representation at a single site (Proposition E). The law never makes them: every gate commutes with the local centre element, so a spinor-class Gauss charge is fixed in place for all time (Theorem P). It is a static probe, not a particle. So **LW1-5-16 is refuted** for what CG1 needs. CG1 needs the field reading (the 16 as the gauge class of the fermion-odd operators that create the light species); #10014's reading (b) is stated for states but used for fields, and on `L5-O` only the states half holds (section 2.6). One escape lies outside `L5-O`: a Spin(10) inside `G_full` that acts on `H_+` as the 16 and trivially on `H_−` (Proposition S′). Under it, odd site operators are 16s and `H_−` is a singlet space. Theorem M breaks it on `L5-O`; `L_full` keeps it. **LW1-5-Σ is answered in two parts.** A covariant end-pure register choice has pure Gauss singlets at every site only if the two tilings carry registers of opposite centre class (Theorem S3), and c10 (`S_+` and `C^{20}`) does have them (Theorem S1, with the Z4 criterion of Lemma S). A single reducible class `S_+ ⊕ C^{20}` only moves c10 into the initial state (Proposition S4). Both fail test 4 today. VC1's text asks for no singlet, and under LW1's reading of gauge invariance there are gauge-invariant states that are pure on the gauge-invariant algebra (Proposition S5). The price is named: one-class `L5-O` has a spinor-class Gauss charge at every site and no flux-free link state; whether GA2 survives that is the new open item **LW1-5-BG**. **SU(2):** every closed subgroup of `Spin(10)` is an exact gauge subgroup with its own Gauss law. For the Standard Model `SU(2)` (which does not contain `−1 ∈ Spin(10)`), Gauss singlets exist at every site (Proposition T). The lattice gauge theory is still `Spin(10)`, so GA2 on `L5-O` needs Yang-Mills for `Spin(10)`, a simple group outside T0's planned SU(2)-then-SU(N) path.

---

## 1. Setting: registers, centre elements, Bogoliubov actions

### 1.1 Registers in PS-6r's wording

`TOE_ASSEMBLY.md` line 183 (PS-6r): "Each link register is a finite quantum link: a finite-dimensional register on which the frame group of the site content acts, with the raising and lowering structure the Gauss law needs."

**Definition GR (register assignment).** Each link `ℓ = (x, y)` carries a finite-dimensional Hilbert space `R_ℓ` with two commuting unitary representations `ρ_{ℓ,x}`, `ρ_{ℓ,y}` of `Spin(10)`, one for each end, with Hermitian generators `L^{cd}_{ℓ,x}`, `L^{cd}_{ℓ,y}`. Links are ordinary tensor factors that commute with matter (`LW1.md` line 42). The Gauss generators are
\[
\mathcal G_x^{cd}=M_x^{cd}+\sum_{\ell\ni x}L^{cd}_{\ell,x}.
\]
A law is *Spin(10)-exact* if every gate commutes with every `𝒢_z^{cd}`. The `so(20)` registers of `LW1_5_DRAFT.md` Lemma Q are the case `ρ_{ℓ,x} = ρ∘(x-end embedding)`; for them and the hop (4.1), `L5-O` is Spin(10)-exact by Theorem G.

This reading is wider than `L5-O`'s item 2. It is used only to state how far each result reaches. Nothing here proposes a register.

### 1.2 Centre elements

Put
\[
\omega_x=\exp\Big(i\pi\sum_{j=1}^5\mathcal G_x^{2j-1,2j}\Big),\qquad z_x=\exp(2\pi i\,\mathcal G_x^{12}),\qquad \varepsilon_{\ell,x}=\exp(2\pi i L^{12}_{\ell,x}).
\]

**Lemma K0.**
(i) On the site Hilbert space, `exp(2πiM_x^{12}) = −1` and `exp(iπΣ_jM_x^{2j−1,2j}) = −iP_x`.
(ii) `z_x = −∏_{ℓ∋x} ε_{ℓ,x}`. Each `ε_{ℓ,x}` is a self-adjoint unitary on `R_ℓ` that commutes with `ρ_{ℓ,x}` and `ρ_{ℓ,y}`. `ω_x^2 = z_x` and `z_x^2 = 1`.
(iii) For `so(20)` registers, `ε_{ℓ,x} = ε_{ℓ,y} = ρ_ℓ(−1_{Spin(20)})`.
(iv) `Ad ω_x` acts on `𝒜_x` as the parity automorphism. `Ad z_x` acts on the whole matter algebra as the identity.

*Proof.* (i) The `M_x^{2j−1,2j} = n_{x,j} − 1/2` commute. `exp(iπ(n − 1/2)) = −i(−1)^n`, so the product is `(−i)^5(−1)^{N_x} = −iP_x`. And `exp(2πi(n_{x,1} − 1/2)) = −1`. (ii) The summands of `𝒢_x^{cd}` commute, so the exponential factorizes. `exp(2πiL^{12})` is `ρ_{ℓ,x}` of the element `−1` of `Spin(10)`, which is central, so `ε_{ℓ,x}` commutes with `ρ_{ℓ,x}`. It commutes with `ρ_{ℓ,y}` because the end actions commute. `ε^2 = ρ(1) = 1`. Then `z_x^2 = ∏ε^2 = 1`. Finally `ω_x^2 = ∏_j exp(2πi𝒢_x^{2j−1,2j})`, and each factor is the implementer of the same central element `−1` (a full turn in any coordinate plane; all planes are conjugate and conjugation fixes a central element), so `ω_x^2 = z_x^5 = z_x`. (iii) `LW1_5_DRAFT.md` line 233: "Each end factor is `ρ` of `exp(2πiT_{ij})`, which is `−1 ∈ Spin(20)` (the same element: a full turn in one coordinate plane)". (iv) By (i) the site factor of `ω_x` is `−iP_x`, and `Ad P_x` is the parity automorphism of `𝒜_x`. The site factor of `z_x` is the number `−1`. The link factors commute with all matter. Matter at other sites is untouched. ∎

**Centre classes.** For an operator `O` with `Ad ω_x(O) = i^k O`, call `k mod 4` its *class at `x`*. Class 0 and class 2 are the tensor classes (class 2 is #10027's "vector class": `10`, `120`, `126`); classes 1 and 3 are the spinor classes. `Ad z_x(O) = (−1)^kO`, so `O` is spinor class at `x` exactly when `Ad z_x(O) = −O`. For a representation space, the same words refer to the scalar by which `ω_x` acts. By Lemma K0(i) the site spaces have classes `H_+ ↦ 3` and `H_− ↦ 1`; the vector `C^{10}` has class 2; the trivial representation has class 0.

### 1.3 Every Bogoliubov Spin(10) kills −1

**Lemma B10.** Let `f: Spin(10) → O(10)` be a continuous homomorphism. Then `f(−1) = 1`.

*Proof.* If `f` is trivial, there is nothing to prove. Otherwise its kernel is a proper closed normal subgroup. Since `so(10)` is simple (cited; `LW1_5_DRAFT.md` cites simplicity of `so(20)` the same way), the kernel is discrete, and a discrete normal subgroup of a connected group is central. Central elements of `Spin(10)` map under the covering `Spin(10) → SO(10)` to central elements of `SO(10)`, which are `±I` (B2-5's commutant argument: a matrix commuting with all rotations is a scalar). So the centre lies in `{±1, ±ω}`, with `ω` a lift of `−I`. The element `ω` is central: `g ↦ gωg^{-1}ω^{-1}` is continuous, takes values in `{±1}`, and equals `1` at `g = 1`. The image of `f` is a connected subgroup of `SO(10)` of dimension 45, so it is `SO(10)`. If `f(−1) ≠ 1`, then `−1 = ω^2` is not in the kernel. A subgroup of `{1, ω, −1, −ω}` that contains `ω` or `−ω` contains `ω^2 = −1`. So the kernel is trivial, and `f` is an isomorphism `Spin(10) ≅ SO(10)`. That is false: `Spin(10)` has the four central elements `±1, ±ω`, and `SO(10)` has two. ∎

So, however a `Spin(10)` is made to act on a site by Bogoliubov frames (the only frames a faithful one-mode hop allows, Theorem M), its `−1` acts on the site algebra as the identity, and its implementer on the site is a number (Lemma G3 uniqueness: an implementer of the identity frame on `M_32(C)` is a scalar).

---

## 2. LW1-5-16: what the centre excludes, and what escapes

### 2.1 The matter field is the 10

**Lemma F (the site algebra is the exterior algebra of the 10).** The linear map `Â: Λ(C^{10}) → 𝒜_x`, `e_{a_1} ∧ ⋯ ∧ e_{a_k} ↦ γ_{x,a_1}⋯γ_{x,a_k}` (`a_1 < ⋯ < a_k`), is a bijection, and `Â∘Λ(R) = φ_R∘Â` for every `R ∈ O(10)`. So under the Bogoliubov frames `𝒜_x ≅ ⊕_kΛ^kC^{10}`. The fermion-odd part is `⊕_{k odd}Λ^k` (`10, 120, 252, 120, 10`), all of class 2. The even part is of class 0.

*Proof.* For `v_1, …, v_k ∈ span{γ_{x,a}}` put `A(v_1, …, v_k) = (k!)^{-1}Σ_π sgn(π) v_{π1}⋯v_{πk}`. It is multilinear and alternating, so `A = Â'∘∧` for a linear `Â'` on `Λ^k`. On distinct basis vectors the `γ`'s anticommute, so `A(γ_{a_1}, …, γ_{a_k}) = γ_{a_1}⋯γ_{a_k}`; hence `Â' = Â` on `Λ^k`. `Â` maps a basis to a basis (`LW1_5_DRAFT.md` Lemma C1's proof: the `2^{10}` ordered monomials are a basis of `M_32(C)`). By Lemma C1, `γ'_c = φ_R(γ_c)` pairwise anticommute, so `φ_R(γ_S) = γ'_{a_1}⋯γ'_{a_k} = A(Rγ_{a_1}, …, Rγ_{a_k}) = Â(Λ^kR\,e_S)`. `−I` acts on `Λ^k` as `(−1)^k`, and `Ad ω_x` acts on `𝒜_x` as `φ_{−I}` (Lemma K0(iv)), so the class is `2k mod 4` reduced to `{0, 2}` by parity of `k`. ∎

The states are different. `H_x = H_+ ⊕ H_−`, two 16-dimensional spaces of classes 3 and 1 (Lemma K0(i)). So the site's *states* are spinors and the site's *operators* are tensors. This is exactly what the centre argument uses: a space on which `−1` acts as one number has only tensor-class operators.

### 2.2 The centre theorem for every register

**Theorem K (centre and matter, any registers).** Take any register assignment (Definition GR) and any Spin(10)-exact law.
(K1) `Ad z_x` is the identity on the matter algebra. Every matter operator lies in a true `SO(10)` representation at every site, and fermion-odd matter operators are class 2 (Lemma F).
(K2) The site factor of `z_x` is the number `−1`. In every state, at every time, in finite or infinite volume, the matter at `x` carries the same spinor-class charge. No state differs from another by a spinor-class matter charge.
(K3) Every gate commutes with `z_x` and with `ω_x`. The spectral projections `Π_x^± = (1 ± z_x)/2` are constants of the motion: `ω∘α^n(Π_x^±) = ω(Π_x^±)` for every state `ω` and every `n`.
(K4) `Ad z_x(O) = −O` only if `O` has a nonzero block between the two eigenspaces of `ε_{ℓ,x}` for some link `ℓ ∋ x`. If every `ε_{ℓ,x}` is a number ("end-pure at `x`"), `Ad z_x` is the identity on the whole quasi-local algebra.
(K5) (Pairing.) If every register is link-pure (`ε_{ℓ,x}ε_{ℓ,y}` a number; true for every `so(20)` register by Lemma K0(iii)), every local operator that is an eigenvector of all `Ad z_x` is spinor class at an even number of sites.

*Proof.* (K1)-(K2): Lemma K0(i) and (iv), and Lemma F. (K3): a gate that commutes with the `𝒢_x^{cd}` commutes with their exponentials. So it commutes with `z_x` and `ω_x`, and so does the update `U`; then `α(Π_x^±) = U^*Π_x^±U = Π_x^±`. (K4): The site factor of `z_x` is a number. So `Ad z_x` is the product over the links at `x` of `Ad ε_{ℓ,x}`, each acting on one tensor factor. Write each link factor of `O` in 2×2 block form for `ε_{ℓ,x} = ±1`. `Ad ε_{ℓ,x}` is `+1` on diagonal blocks and `−1` on off-diagonal blocks. If no link factor has an off-diagonal block, `Ad z_x(O) = O`. If every `ε_{ℓ,x}` is a number, there are no off-diagonal blocks. (K5): Let `O` be supported on the matter of a finite set `S` of sites and on links with both ends in `S` (enlarge `S` if needed). Then
\[
\prod_{x\in S}z_x=(-1)^{|S|}\prod_{\ell\subset S}\varepsilon_{\ell,x}\varepsilon_{\ell,y}\prod_{\ell\in\partial S}\varepsilon_{\ell,\text{inner}} .
\]
The `z_x` commute (each pair shares at most one link, where the two end actions commute). The middle factors are numbers. The boundary factors act on links outside the support of `O`. So `Ad(∏_{x∈S}z_x)(O) = O`. For sites outside `S`, `Ad z_x(O) = O` by (K4)'s support argument. Hence `∏_x(−1)^{k_x} = 1`. ∎

(K1) and (K4) contain Lemma Z(i) and (iii) of `LW1_5_DRAFT.md` and extend them: (K1) needs no hypothesis on the registers; Lemma Z's "No local operator transforms as a spinor 16" holds exactly when the registers are end-pure (K4, and Proposition E below for the converse).

### 2.3 Mixed registers: spinor-class operators exist

**Proposition E (spinor-class link operators).**
(i) (`so(20)` register, mixed.) Let `R = S_+ ⊕ C^{20}`. Then `ε = ρ(−1_{Spin(20)}) = (−1) ⊕ (+1)`. For `s ∈ S_+` and `v ∈ C^{20}` the link operator `X = |v⟩⟨s|` on a link `ℓ = (x, y)` has `Ad z_x(X) = −X` and `Ad z_y(X) = −X`. `Ψ = γ_{x,a}X` is fermion odd with the same classes. These are local, gauge-covariant (each spans a finite-dimensional representation under the local gauge groups), and spinor class at two sites, as (K5) requires.
(ii) (Wider register, end-mixed at one end.) Let `H^x ≅ C^{32}` carry the spin representation of `Spin(10)_x` with Clifford generators `γ^x_b`, let `H^y ≅ C^{32}` likewise, and let `V ⊕ C` (dimension 11) carry the vector-plus-trivial representation of `Spin(10)_y` with the tensor operator `A_a = |a⟩⟨0| + |0⟩⟨a|`. Put `R = (H^x ⊗ (V ⊕ C)) ⊕ (H^x ⊗ H^y)` and `U^{ab} = γ^x_b ⊗ (A_a ⊕ γ^y_a)`. Then `U^{ab}` is Hermitian and is a `(10,10)` tensor operator, so the hop (4.1) with this `U` commutes with the Gauss law (the computation in the proof of Theorem G(i) uses only the tensor property). The link operator `X = 1_{H^x} ⊗ J`, with `J: C → H^y` an isometry onto a vector of `H^y_+` composed with the projection onto `C`, has `Ad z_x(X) = X` and `Ad z_y(X) = −X`. Its components under `Spin(10)_y` span `H^y_+`, a half-spin representation (a 16 or 16bar by convention; use `H^y_−` for the other). `γ_{y,a}X` is fermion odd and its components contain the other half-spin representation (`V ⊗ H_+ → H_−` by Clifford multiplication). So with this register there is a fermion-odd gauge-covariant local operator that carries a half-spin representation at one site and nothing elsewhere. Pairing fails, because this register is not link-pure.

*Proof.* (i) `ρ(−1_{Spin(20)})` is `−1` on the spinor representation `S_+` and `+1` on the vector `C^{20}` (a full turn acts as `+1` on vectors). By Lemma K0(iii), `ε_{ℓ,x} = ε_{ℓ,y} = ε`. `X` maps the `+1` eigenspace to the `−1` eigenspace, so both `Ad ε`'s negate it. `γ_{x,a}` has class 2 at `x`, so `Ψ` is still spinor class. (ii) `[L^{cd}_y, A_a] = i(δ_{da}A_c − δ_{ca}A_d)` on `V ⊕ C`, with `L^{cd}_y = i(E_{cd} − E_{dc})` on `V` and `0` on `C`; `[M^{cd}, γ_a] = i(δ_{da}γ_c − δ_{ca}γ_d)` is (1.1) of `LW1_5_DRAFT.md`. So `U^{ab}` obeys (Q2) of Lemma Q, which is all that Theorem G(i)'s computation uses. `ε_{ℓ,y}` is `+1` on `H^x ⊗ (V ⊕ C)` and `−1` on `H^x ⊗ H^y`, while `ε_{ℓ,x} = −1` on both. `X` maps the first summand to the second at the `y` end only. Under `Spin(10)_y`, `Ad` acts on `X` through `J`, and the span of the images of `J` under `Spin(10)_y` is the irreducible `H^y_+`. ∎

A covariant law would use `R ⊕ R^{swap}` on every link (section 3.3 explains why covariance needs the swap). That changes nothing above.

### 2.4 The law never makes or moves them

**Theorem P (spinor-class Gauss charges are static probes).** Take any register assignment and any Spin(10)-exact law. Let `ω` be a state with `ω(Π^-_x) = 1` ("a spinor-class Gauss charge at `x`").
(i) `ω∘α^n(Π^-_x) = 1` for every `n` (K3).
(ii) For every `A` in the algebra generated by the matter, the gates and the gauge-invariant operators, the state `ω_A = ω(A^*·A)/ω(A^*A)` (when defined) still has `ω_A(Π^-_x) = 1`. So neither matter nor the law screens the charge.
(iii) No vector in the range of `Π^-_x` is invariant under `Spin(10)_x`, because `z_x` is in that group and acts there as `−1`.
(iv) A spinor-class charge at `x` relative to a state `ω'` (that is, `ω(Π^-_x) ≠ ω'(Π^-_x)`) can be produced from `ω'` only by an operator outside the algebra of (ii), such as `X` of Proposition E.

*Proof.* (i) is (K3). (ii) `A` commutes with `z_x`: matter by (K1), gates by (K3), gauge-invariant operators by definition. So `ω_A(Π^-_x) = ω(A^*Π^-_xA)/ω(A^*A) = ω(Π^-_xA^*A)/ω(A^*A)`, and `ω(Π^-_x) = 1` makes `Π^-_x` act as the identity in the GNS space of `ω`, so this is `1`. (iii) is immediate. (iv) Every operator in the algebra of (ii) commutes with `Π^-_x`, so it cannot change `ω(Π^-_x)`. ∎

Compare a lattice gauge theory with a matter field in the 3. There, `z_x` is also conserved, and quarks still move: the matter part of the centre charge, `e^{2πiN_x/3}`, changes and the link ends compensate. Here the matter part is the number `−1` (K2). So the only way a site's spinor class could differ from a reference is through `Π^-_x` itself, and Theorem P fixes that for all time. In one-class `L5-O`, `Π^-_x = 1` at every site in every state: every site is such a "probe" site, and there is no reference without one.

**Answer to the probe question.** A spinor-class probe exists only as a fixed Gauss sector. Its composites with matter keep the spinor class at the probe's site (K1), are never gauge singlets there (P(iii)), and do not move (P(i)). A gauge-invariant composite with a charged probe that carries a moving 16 does not exist, for any finite register choice.

### 2.5 What escapes the centre argument

The argument uses three facts: the gauge group acts on matter through frames (automorphisms of `𝒜_x`); for `L5-O` the frames are Bogoliubov, so `−1` acts trivially (Lemma B10); and the gates commute with `z_x`. What escapes:

- **E1, states.** The site Fock space is `16 ⊕ 16bar` (classes 3, 1), and `S_+` register states are spinor class at both ends. These are not excitations: they are present at every site in every state (K2). #10027 line 165 says the same of #10014: "its Spin(10) "16 per family" counts site Fock states. Excitations above a fixed-site vacuum are tensors".
- **E2, fixed spinor-class Gauss sectors** on end-mixed registers (Proposition E, Theorem P). They are made only by operators outside the law and never move.
- **E3, a Spin(10) that is not Bogoliubov.** Proposition S′ below. It needs hops beyond one site mode, so it is outside `L5-O`.
- **E4, a changing site count**, #10027 line 128: "An excitation that adds or removes one five-mode site carries centre (-i)^{+-1}". This is outside the Lattice axiom and outside this draft.

#10027's second route, line 132 ("A deconfined spinon ... can carry z = +-i individually"), is excluded on `L5-O` in the sense of Theorem K: a gauge-charged spinon would need a spinor-class charge either in matter (K2 makes that a number) or in a Gauss sector (fixed by Theorem P). A spinon that carries no gauge charge but a projective charge of some other symmetry is outside Theorem K; it is not a 16 of the gauge group, so it does not meet CG1 either.

**Proposition S′ (a Spin(10) in `G_full` whose `−1` is the parity frame).** Let `S_+: Spin(10) → U(H_+)` be the site spin representation on the even half, and put `f(g) = Ad(S_+(g) ⊕ 1_{H_−})`.
(i) `f` is an injective homomorphism into the identity component of `G_full`, and `f(−1)` is the parity automorphism `Ad P_x ≠ id`.
(ii) Under `f`, the odd site operators `Hom(H_−, H_+) ≅ H_+ ⊗ C^{16}` are 16 copies of the 16 (spinor class), and every vector of `H_−` is invariant.
(iii) `f(Spin(10))` is not contained in the Bogoliubov frames. So every law with a faithful one-mode hop breaks it (Theorem M of `LW1_5_DRAFT.md`), and `L5-O` breaks it. `L_full` (Proposition A of `LW1_5_DRAFT.md`) keeps all of `G_full` exact, so `f(Spin(10))` is an exact gauge subgroup of `L_full`, with the restricted Gauss law.

*Proof.* (i) `S_+(g) ⊕ 1` is an even unitary, so `Ad` of it is a frame (Theorem C(i)). `S_+(−1) = −1` (Lemma K0(i)), so `f(−1) = Ad(−1 ⊕ 1) = Ad(−P_x) = Ad P_x`, which negates the odd elements. Injectivity: the kernel of `S_+` is a proper closed normal subgroup, hence central (simplicity), hence in `{±1, ±ω}`; by Lemma K0(i), `S_+(ω) = −i`, `S_+(−1) = −1` and `S_+(−ω) = i`, none of them `1`. If `Ad(S_+(g) ⊕ 1) = id`, then `S_+(g) ⊕ 1` is a scalar (Lemma G3), so `S_+(g) = 1`. (ii) `Ad(S_+(g) ⊕ 1)(|s⟩⟨t|) = S_+(g)|s⟩⟨t|` for `s ∈ H_+`, `t ∈ H_−`. (iii) If `f(Spin(10))` were Bogoliubov, Lemma C1 would give a homomorphism `Spin(10) → O(10)` with `f(−1) ≠ 1`, against Lemma B10. ∎

[check] `check2.py` (5): in the three-mode analogue (`Spin(6)`, site `C^8`), `Ad(−1 ⊕ 1)` negates every odd site generator.

This is #10126's third escape, quoted at `TOE_ASSEMBLY.md` line 417 ("a Spin(10) not generated by site bilinears"), made concrete inside the frames of PS-5 and PS-6. It is recorded, not proposed (section 5, choice c15). Under `f`, the five modes are not a covariant multiplet, and the choice of `1_{H_−}` (rather than another 16-dimensional tensor-class representation on `H_−`) has no PS reason.

### 2.6 Field or states: which reading CG1 needs

`TOE_ASSEMBLY.md` line 404 (CG1(a)): "The light chiral content of one family is the Standard Model one-generation multiplet ... equivalently the 16 of `Spin(10)` branched under `SU(3) x SU(2) x U(1)`". Line 389 (CH1(a)), which CG1 imports: "whose light spectrum at scales `>> a` is exactly the chiral content of CG1 (one Weyl 16, or the Standard Model multiplet, per family)". Line 344 (MT1(a)(3)): "per cell, carry enough modes for one family's chiral content (a 16 of `Spin(10)`, or the Standard Model multiplet)".

"Light spectrum", "content per family" and "modes" are words about excitations and the fields that create them. A site's Fock space is not an excitation: it is there at every site in every state (K2). So **CG1 needs the field reading**: the 16 (or the Standard Model multiplet) is the gauge representation carried by the fermion-odd operators, dressed by links if needed, that create the light species above the vacuum. On `L5-O`, for every finite register choice, those operators are tensor class (Theorem K, Lemma F), and spinor-class Gauss sectors are fixed (Theorem P). So CG1 read with "the 16 of `Spin(10)`" cannot be met on `L5-O`. CG1 read with "the Standard Model multiplet" is not excluded: `SU(5)` pieces of one family sit inside tensor-class representations of `Spin(10)` (`LW1_5_DRAFT.md` line 430: "the `120` contains a `10` of `SU(5)`"), so after breaking (EW1/VC1) the light content could be the Standard Model multiplet with tensor-class parents. Then "equivalently the 16" fails, and the right-handed completion (CG1-ii) is a separate question.

**#10014's reading (b).** Its line 38: "The 4D reading is that each state of S+ is one left-handed Weyl species. This is the Wilczek-Zee reading of Lambda(C^N), used by the merged ruleset; it is not derived here." That is a states reading. Its later steps treat `S+` as a field. Line 65: "A Majorana mass for a Weyl multiplet needs a *symmetric* invariant bilinear on S+." Line 79: "The element -1 in Spin(2N) acts as -1 on every S+ field and as +1 on every bilinear. It therefore equals (-1)^F". On `L5-O`, `−1` acts as the identity on every operator (K1), and the operator that acts as fermion parity is `ω`, not `−1` (Lemma K0(iv)). So the states half of (b) holds on `L5-O` (the site's even Fock space is the 16), and the field half, which its anomaly and mass steps use, fails for every register choice. #10014's conclusions about anomaly freedom and mass protection are field statements, and they do not transfer to `L5-O`'s excitations. Under `f` of Proposition S′, the field half would hold for the odd site operators (16 copies of the 16, `f(−1)` = parity), but `f` is not `L5-O`'s group. D1's check (`TOE_ASSEMBLY.md` line 205) cites only (a) and the vector-class result; this section adds that (a) without the field half of (b) does not give a 16 of excitations.

**Answer to item 1 (LW1-5-16).** Refuted for what CG1 needs. Proved: (1) for every finite register choice in PS-6r's wording and every Spin(10)-exact law with PS-5 sites, matter operators are tensor class, matter never carries a relative spinor charge, and spinor-class Gauss sectors are constants of the motion (Theorems K, P). (2) The centre argument excludes exactly: spinor class on any operator made from matter, gates or gauge-invariant operators; and, for end-pure registers, on any local operator. (3) What escapes: states (E1), fixed sectors made by non-law operators on end-mixed registers (E2, Proposition E; for `so(20)` registers they come in pairs, (K5)), a non-Bogoliubov Spin(10) outside `L5-O` (E3, Proposition S′), and a changing site count (E4). (4) The obstruction is about the field: the Majorana modes are the 10 and the site algebra is `Λ(10)`; the states are `16 ⊕ 16bar`.

---

## 3. LW1-5-Σ: Gauss singlets

### 3.1 The Z4 criterion

**Lemma S (when a product has a singlet).** Let `W` be a tensor product of factors, each one of `H_+`, `H_−` (the site half-spin spaces), `V = C^{10}`, or `C`, with `Spin(10)` acting diagonally. Give the factors the classes 3, 1, 2, 0. Then `W` has a nonzero `Spin(10)`-invariant vector if and only if the sum of the classes is `0 mod 4`.

*Proof.* Only if: `ω` acts on `W` as `i^{Σ classes}`, and an invariant vector is fixed by `ω`. If: four facts. (a) `H_+^* ≅ H_−`. The transposes `γ_a^T` are Hermitian and obey the same anticommutation relations. By Lemma C1's argument, `γ_S ↦ (γ_{a_1})^T⋯(γ_{a_k})^T` is an automorphism of `M_32(C)`; by Lemma G3 it is `Ad C` for an invertible `C`, so `Cγ_aC^{-1} = γ_a^T`. For `M = (i/2)γ_aγ_b` (`a ≠ b`), `CMC^{-1} = (i/2)γ_a^Tγ_b^T = (i/2)(γ_bγ_a)^T = −M^T`. So `B(u, v) = u^TCv` is a nondegenerate bilinear form with `B(Mu, v) + B(u, Mv) = 0`: it is `Spin(10)`-invariant. Next, `P_x^T = (−i)^5γ_{10}^T⋯γ_1^T = (−i)^5Cγ_{10}⋯γ_1C^{-1}`, and reversing ten anticommuting factors gives the sign `(−1)^{45} = −1`, so `P_x^TC = −CP_x` and `B(P_xu, P_xv) = −B(u, v)`. Hence `B(H_+, H_+) = 0`, and `B` pairs `H_+` with `H_−` nondegenerately. (b) Clifford multiplication `V ⊗ H_± → H_∓`, `w ⊗ u ↦ Σ_aw_aγ_au`, is equivariant (by (1.1)) and onto. By complete reducibility of unitary representations, `H_∓` is a summand of `V ⊗ H_±`. (c) `H_+ ⊗ H_+ ⊃ V` and `H_− ⊗ H_− ⊃ V`: `Hom(V, H_+ ⊗ H_+) ≅ Hom(V ⊗ H_+^*, H_+) = Hom(V ⊗ H_−, H_+) ∋` Clifford multiplication `≠ 0`. (d) `V ⊗ V ∋ Σ_ae_a ⊗ e_a`, and `H_+ ⊗ H_− ≅ H_+ ⊗ H_+^* = End(H_+) ∋ 1`. Now induct on the number of factors. Drop `C` factors. If `W` has a `V` and a spinor factor, replace `V ⊗ H_±` by its summand `H_∓` (class sum unchanged mod 4, by `2 + 3 ≡ 1`, `2 + 1 ≡ 3`). If only `V`'s remain, their number is even; pair them by (d). If only spinor factors remain, pair `H_+` with `H_−` by (d) while both occur; the rest are all `H_+` or all `H_−`, their number is `0 mod 4`, and (c) then (d) pair them. Each step replaces a sub-product by a summand, so an invariant of the smaller product is an invariant of `W`. ∎

[check] `check2.py` (2), the three-mode analogue `Spin(6)` (half-spin spaces of dimension 4, vector 6): invariants exist exactly for the words with class sum `0 mod 4` among ten words tested (`++++`: 1, `+++−`: 0, `++−−`: 2, `++v`: 1, `+−v`: 0, `+−`: 1, `++`: 0, `vv`: 1, `+v`: 0, `+++v−`: 3). (3), Cl(10): `B(H_+, H_+) = 0` and `B(H_+, H_−) ≠ 0`.

### 3.2 Singlets on a given register pattern

For an `so(20)` register `R` and a link `ℓ`, the components of `R` under `Spin(10)_x × Spin(10)_y` used here are:
- `S_+`: as a `Spin(20)` module it is the joint eigenspace of the two end parities `P^xP^y = σ` (fixed sign) in the Fock space of `Cl(20)`, so `S_+ = ⊕_p H^x_p ⊗ H^y_{pσ}`: both ends spinor class (classes 3 or 1 at each end).
- `C^{20} = (V ⊗ C) ⊕ (C ⊗ V)`: one end of class 2, the other of class 0.

**Theorem S1 (pure Gauss singlets on a pattern).** Give each link one of the registers `S_+` or `C^{20}` (any pattern, not necessarily covariant). Let `s(x)` be the number of `S_+` links at `x`.
(i) If `s(x)` is even for some `x`, no vector is invariant under `Spin(10)_x`.
(ii) If `s(x)` is odd for every `x` in a finite set `Λ`, there is a nonzero vector in the space of the sites of `Λ` and the links meeting `Λ` that is invariant under `Spin(10)_x` for every `x ∈ Λ`. On the whole lattice, the same construction gives a product vector state that is invariant under every local `Spin(10)_x`.

*Proof.* (i) `z_x = −(−1)^{s(x)}(+1)^{6−s(x)} = −1` (Lemma K0(ii), with `ε = −1` on `S_+` and `+1` on `C^{20}`). (ii) On each link choose one irreducible component: for `S_+` a parity `p`, giving `H^x_p ⊗ H^y_{pσ}`; for `C^{20}` one of its two summands. Then the space of `Λ` contains the tensor product, over `x ∈ Λ`, of `W_x = H_{x,q_x} ⊗ ⊗_{ℓ∋x}(\text{chosen end factor of } ℓ \text{ at } x)`, where `q_x` is a site parity still to be chosen. The class sum of `W_x` is `c(q_x) + Σ_{S_+ \text{ ends}}(\text{odd}) + Σ_{C^{20} \text{ ends}}(0 \text{ or } 2)`. With `s(x)` odd, the sum of the link ends is odd. So exactly one of `c(q_x) ∈ {3, 1}` makes the total `0 mod 4`. Choose that parity. Lemma S gives a nonzero invariant `T_x ∈ W_x`. Then `⊗_xT_x` is nonzero and invariant under every `Spin(10)_x`, `x ∈ Λ`, because `Spin(10)_x` acts only on the factor `W_x`. Each `T_x` has definite site parity, so on the lattice the product vector state is a well-defined even state of the CAR algebra tensored with the links. ∎

So the c10 pattern of `LW1_5_DRAFT.md` line 235 (`S_+` on even-tiling links, `C^{20}` on odd-tiling links, `s(x) = 3`) has a pure Gauss singlet at every site. The draft said "singlets can occur"; Theorem S1(ii) proves it.

### 3.3 Covariant patterns

**Lemma S2 (each link is reversed by a symmetry that fixes it; two link orbits).** In `𝒢 = 2Z^3 ⋊ O_{c_0}` (`LW1.md` line 33: "The group \(O\) consists of determinant-one signed coordinate permutations. Its action about \(c_0\) is \(x\mapsto Q(x-c_0)+c_0\)"):
(i) every link `(x, x + e_i)` is mapped to itself with its ends exchanged by some element of `𝒢`;
(ii) the even-tiling links form one orbit and the odd-tiling links form another.

*Proof.* (i) Take `i = 1`; the other directions follow by a cyclic coordinate permutation (determinant one). If `x_2 ≡ x_3 (mod 2)`, use `Q(y_1, y_2, y_3) = (−y_1, y_3, y_2)` (determinant `−1·(0 − 1) = 1`) and the translation `2t` with `t = (x_1, (x_2 − x_3)/2, (x_3 − x_2)/2)`. Then `y ↦ Q(y − c_0) + c_0 + 2t` sends `x` to `x + e_1` and `x + e_1` to `x`. If `x_2 ≢ x_3`, use `Q(y) = (−y_1, −y_3, −y_2)` (determinant one) and `t = (x_1, (x_2 + x_3 − 1)/2, (x_2 + x_3 − 1)/2)`. (ii) `LW1.md` line 201: "It sends even cube centres to even cube centres", so `𝒢` preserves the tiling of a link (Lemma A1: the tiling of `(x, x + e_i)` is fixed by `x_i mod 2`). Within direction 1 and the even tiling, the base points are `x_1` even and `(x_2, x_3)` arbitrary. `2Z^3` leaves the classes `(x_2, x_3) mod 2`, and the quarter turn `(y_1, y_2, y_3) ↦ (y_1, y_3, 1 − y_2)` about the `e_1` axis through `c_0` permutes them in a 4-cycle. Cyclic permutations join the directions. The odd tiling is the same. ∎

[check] `check2.py` (1): enumerating `O` (24 elements) and translations on a box: every link is fixed and reversed by some element, and there are two link orbits modulo `2Z^3`, one per tiling.

A covariant law maps the register of `ℓ` to that of `gℓ`, intertwining the end at `x` with the end at `gx`. By Lemma S2(i), each register is then isomorphic to itself with its two ends exchanged. So for end-pure registers the two ends of a link have the same class `ε_ℓ`, and by Lemma S2(ii) `ε_ℓ` depends only on the tiling: `ε_e` and `ε_o`.

**Theorem S3 (covariant end-pure registers).** For a covariant assignment of end-pure registers (any finite registers of Definition GR), `z_x = −ε_e^3ε_o^3` at every site. So a pure Gauss singlet needs `ε_eε_o = −1`: one tiling carries a spinor-class register and the other a tensor-class register. With the same register class on all links there is none. For `S_+` on one tiling and `C^{20}` on the other, singlets exist at every site (Theorem S1(ii)).

*Proof.* Lemma A1 as used in `LW1_5_DRAFT.md` line 235: "Each site has three links of each tiling". (In direction `i`, exactly one of `(x, x + e_i)` and `(x − e_i, x)` has an even base coordinate.) Then Lemma K0(ii). ∎

Proposition Σ is the case `ε_e = ε_o`. The reason is a parity count: the site is one spinor-class Clifford module, and an even number (six) of equal-class link ends cannot change the site's class.

### 3.4 A single reducible register class

**Proposition S4.** Let every link carry `R = S_+ ⊕ C^{20}` (one covariant class), with the hop (4.1) and the electric gate of `LW1_5_DRAFT.md` section 8.1.
(i) Every gate commutes with each `ε_ℓ = ρ_ℓ(−1_{Spin(20)})`. So the label `κ_ℓ ∈ {S, V}` of each link is a constant of the motion, and the law is the direct sum over patterns `κ` of the fixed-pattern laws of Theorem S1.
(ii) The patterns with a pure Gauss singlet at every site are those with `s(x)` odd at every `x`. The covariant ones among them are exactly the two c10 patterns (`S` on even links and `V` on odd links, or the reverse).
So this choice reproduces c10 as a sector and moves the choice of c10 into the initial state `ω_0`.

*Proof.* (i) `ρ(−1_{Spin(20)})` is central in the image of `Spin(20)`, so it commutes with every `U^{ab} = ρ(2T_{a,10+b})` and with `Γ^x_ℓ`, which is `ρ` of an element of `Spin(20)` (a product of ten unit vectors) up to a phase. (ii) Theorem S1; a pattern invariant under `𝒢` is constant on each tiling (Lemma S2(ii)); of the four constant patterns, only the two mixed ones have `s(x) = 3`. ∎

### 3.5 VC1 without a Gauss singlet

`TOE_ASSEMBLY.md` line 466 (VC1(a)): "Under `L` and PS-7, there is a translation- and rotation-invariant stationary state `omega_0` of the update (the vacuum) such that (1) it is stable ... (2) the matter of MT1 is its particle-hole excitations ...". It asks for a state, not a pure state and not a Gauss singlet. `LW1.md` line 47: "Gauge invariance of a state means invariance under these conjugations, not support in the sector \(\mathcal G_x=0\)."

**Proposition S5 (gauge-invariant states that are pure on observables).** In one-class `L5-O` (any end-pure registers), on a finite region with gauge group `K = ∏_{x}Spin(10)_x` over its interior sites, write the region's space as `⊕_λ V_λ ⊗ W_λ` (irreducible representations `V_λ` of `K` with multiplicity spaces `W_λ`). Then:
(i) the gauge-invariant operators are `⊕_λ 1_{V_λ} ⊗ End(W_λ)`;
(ii) for every `λ` and every unit `w ∈ W_λ`, the density matrix `d_λ^{-1}1_{V_λ} ⊗ |w⟩⟨w|` is gauge invariant in LW1's sense, and its restriction to the gauge-invariant operators is the pure vector state `w`;
(iii) every `λ` that occurs has every factor of spinor class (Proposition Σ), so `d_λ ≥ 2^{n}` for `n` interior sites; on the full algebra every gauge-invariant state is mixed at every site.

*Proof.* (i) Schur's lemma on the isotypic decomposition: an operator commuting with `K` preserves each isotypic block `V_λ ⊗ W_λ`, maps between blocks only for equal `λ`, and on a block it is `1 ⊗ B`. (ii) The density matrix commutes with `K`. On `⊕1 ⊗ End(W_λ)` it gives `B ↦ ⟨w, B_λw⟩`, a vector state of the full matrix algebra `End(W_λ)`, which is pure. (iii) An irreducible representation of `K` is a tensor product of irreducible representations of the factors. `z_x = −1` on the whole space, so no factor is trivial. A nontrivial irreducible representation of a connected group with no nontrivial one-dimensional representation (here `Spin(10)`, whose Lie algebra is simple) has dimension at least 2. A gauge-invariant density matrix is a mixture of the form in (ii) with `1_{V_λ}` factors, so it is mixed. ∎

So reading VC1 with LW1's notion of gauge invariance removes the need for a pure Gauss singlet. No structure is added, and the reading is LW1's own text. The mixedness is over gauge indices, which no gauge-invariant observable sees (S5(i)-(ii)).

**What it costs.** In one-class `L5-O` every site carries a spinor-class Gauss charge (`z_x = −1`), in every state. In lattice gauge theory language, that is a fixed external charge of spinor class at every site. Also:

**Remark (no flux-free link state).** On `S_+`, `ε_{ℓ,x} = −1`, so no vector of a link register is invariant under `Spin(10)_x`. On `C^{20} = (V ⊗ C) ⊕ (C ⊗ V)`, no vector is invariant under `Spin(10)_x × Spin(10)_y`. So in one-class `L5-O` with either register, no link has a state with zero flux at both ends. (Some `so(20)` registers have such a state; a register with a `(1, 1)` component is an example. None is proposed.)

Whether a lattice gauge theory with a spinor-class Gauss charge at every site and no flux-free link state has a long-distance limit that GA2 can compare with "continuum `G_i` Yang-Mills with the matter of CG1" (`TOE_ASSEMBLY.md` line 377) is open: **LW1-5-BG** (section 6).

**Answer to item 2 (LW1-5-Σ).** (a) A covariant register assignment with a pure Gauss singlet at every site exists: the two-tiling choice c10, proved in Theorem S1(ii), or the single reducible class `S_+ ⊕ C^{20}` in its c10 sector (Proposition S4). Theorem S3 shows that, among covariant end-pure assignments, only opposite classes on the two tilings work. None of these passes test 4 today, because no working-set text needs a pure singlet (section 5). (b) VC1 read with LW1 line 47 needs no singlet: Proposition S5 gives gauge-invariant states that are pure on the gauge-invariant algebra. That reading passes the four tests. It leaves LW1-5-BG.

---

## 4. SU(2) for T0

`TOE_ASSEMBLY.md` line 535 (what GA2 imports from T0): "Existence of the continuum SU(2) theory as an OS/Wightman theory (T0 proper); then SU(N), through the planned extension along the Sussman-Alpoge work." Line 377 (GA2): "Let `G = prod_i G_i` be the gauge group of GA1. For each simple factor `G_i` with negative one-loop beta coefficient, the framework's gauge sector ... agrees with continuum `G_i` Yang-Mills".

**Proposition T (SU(2) subgroups of `L5-O`).** Take `L5-O[R]` with any `so(20)` register.
(i) For every closed subgroup `K ⊂ Spin(10)` with Lie algebra `𝔨'`, the generators `𝒢_x^T = Σ_{c<d}T_{cd}𝒢_x^{cd}`, `T ∈ 𝔨'`, commute with every gate at every angle, and `e^{i𝒢_x^T}` implement `K` at `x`. So `K` is an exact gauge subgroup with its own Gauss law.
(ii) If `−1 ∈ K` and the registers are one end-pure class, there is no `K`-singlet at any site. Example: the `SU(2) = Spin(3)` that rotates `γ_{x,1}, γ_{x,2}, γ_{x,3}` contains `exp(2πiM^{12}) = −1`.
(iii) Let `SU(2)_W` be generated by `J_1 = (M^{12} − M^{34})/2`, `J_2 = (M^{13} + M^{24})/2`, `J_3 = (M^{14} − M^{23})/2` at each site (with the same combinations of the `L_{ℓ,x}` on the ends). On the site, `J_1 = (n_1 − n_2)/2`, `J_2 = (c_1^†c_2 + c_2^†c_1)/2`, and each `J_k` commutes with `n_1 + n_2`. So `SU(2)_W` is the `SU(2)` of the `U(2)` that acts on the modes `c_1, c_2`; up to conjugation it is the `SU(2)` of the Standard Model inside `SU(5) ⊂ Spin(10)`. Then `−1 ∉ SU(2)_W`, and in `L5-O[S_+]` there is a pure `SU(2)_W` Gauss singlet at every site.
(iv) The exact gauge group of `L5-O` stays `Spin(10)` (Corollary R.1). `SU(2)_W` invariance alone does not define the law's physical states, and the `SU(2)_W` part of the link variables is not a separate quantum link. So `L5-O` does not contain T0's pure `SU(2)` Yang-Mills as a sector. GA2's simple factor before breaking is `Spin(10)` itself.

*Proof.* (i) Theorem G(i): every `𝒢_x^{cd}` commutes with every gate; linear combinations and exponentials keep that. (ii) `−1 ∈ K` acts as `z_x = −1` (Proposition Σ). (iii) By (1.1), `M^{2j−1,2j} = n_j − 1/2`, and a direct expansion of `γ_1γ_3 + γ_2γ_4` and `γ_1γ_4 − γ_2γ_3` in the `c`'s gives number-conserving bilinears, so the `J_k` lie in `u(2)` of the modes 1, 2 and have no `n_1 + n_2` part. The three `J_k` close into `su(2)` and commute with the self-dual triple `(M^{12} + M^{34})/2, …`, the other factor of `so(4)` [check] `check2.py` (4), (4b). `exp(2πiJ_1)` acts on the site as `exp(iπ(n_1 − n_2)) = (−1)^{n_1+n_2}`, which is not a number. `J_1` has eigenvalues `±1/2` on the site, so the group is `SU(2)` (not `SO(3)`), and its only central element of order two is `exp(2πiJ_1)`. If `−1 ∈ Spin(10)` lay in `SU(2)_W`, it would be central there of order two, hence equal to `exp(2πiJ_1)`. But `−1` acts on the site as the number `−1`, and `exp(2πiJ_1)` does not. So `−1 ∉ SU(2)_W`. On the site, `Spin(4)` acts on the Fock space of modes 1 and 2 as the sum of its two half-spin spaces, one a doublet of `SU(2)_W` and one a singlet pair. So one parity half of modes 1, 2 is `SU(2)_W`-invariant. With the eight states of modes 3-5, that gives `2 × 8 = 16` invariant site vectors ([check] (4b): 16). The `x`-end of `S_+` is, as a `Spin(10)_x` module, copies of `H^x_±` (section 3.2), the same modules as the site, so it has `SU(2)_W`-invariant vectors at each end. Choose on each link a component `H^x_p ⊗ H^y_{pσ}` and in it a product of `SU(2)_W`-invariant vectors at the two ends; at each site take an invariant site vector. The product is invariant under every local `SU(2)_W`. (iv) Corollary R.1 of `LW1_5_DRAFT.md`. The `U^{ab}` with `a, b ≤ 4` generate an `so(8)` inside `so(20)` (by (Q3)), a `Spin(4)` quantum link, but the hop (4.1) also contains the other blocks, which mix the two sets of indices. ∎

**Answer to item 3.** Yes: `SU(2)_W ⊂ Spin(10)` is an exact gauge subgroup of `L5-O` with its own Gauss law, at every angle and for every register, and it has Gauss singlets at every site even with one register class. But it is a subgroup of an exact `Spin(10)`, not the gauge group of a sector. T0's pure `SU(2)` theory enters GA2 as the `SU(2)` factor only after `Spin(10)` breaks (EW1/VC1). Before breaking, GA2 needs Yang-Mills for `Spin(10)`. Line 535 names the planned path "SU(2) ... then SU(N)". `Spin(10)` is a simple group outside the `SU(N)` family, so that path does not reach it as stated. For `L5-U` the simple factor is `SU(5)` (`LW1_5_DRAFT.md` Theorem U), which is on that path.

---

## 5. Four-test check of every choice considered

Tests: (1) states or fixes a part's target; (2) open-ended; (3) settles a downstream question by premise; (4) adds structure its reasons do not need. Nothing below is adopted.

| Choice | (1) | (2) | (3) | (4) | Result |
|---|---|---|---|---|---|
| c10. `S_+` on even-tiling links, `C^{20}` on odd-tiling links | pass | pass | pass | fails: a tiling-dependent register class; its only reason is a pure singlet, which no working-set text needs (section 3.5) | recorded, not proposed |
| c12. One reducible class `S_+ ⊕ C^{20}` on all links | pass | pass | pass | fails: it adds a conserved class label on every link and leaves c10 to `ω_0` (Proposition S4); more structure than c10 | recorded, not proposed |
| c13. Registers outside `so(20)` (Definition GR, e.g. Proposition E(ii)) | fails if chosen to get a spinor-class operator (target) | fails unless given a named range: "any `(10,10)` tensor operator" is a family without a bound | pass | fails: end-asymmetric summands have no PS reason | recorded only to state the reach of Theorem K |
| c14. Fix the pattern `κ` in c12 to get a probe at chosen sites | fails: chosen for a spinor-class charge | pass | fails: puts a charge into `ω_0` by premise | fails | rejected |
| c15. Gauge group `f(Spin(10))` of Proposition S′ (law `L_full` broken to it, or a new hop keeping it) | fails: chosen because it gives the 16, not derived | conditional: `f` is one of several embeddings `(S_+, S')` with `S'` a 16-dimensional tensor-class representation on `H_−` | fails: it settles CG1's 16 by premise | fails: hops beyond one site mode, and the choice `S' = 1` | recorded, not proposed |
| R-VC1. Read VC1's state with `LW1.md` line 47's gauge invariance (Proposition S5) | pass | pass | conditional: it makes the spinor-class Gauss charge at every site a fact that GA2 must handle (LW1-5-BG) | pass: adds nothing; it is LW1's text | passes 1, 2, 4; 3 conditional, disclosed |
| R-CG1. Read CG1's "content" as the field reading (section 2.6) | pass | pass | conditional: it decides that `L5-O` cannot meet CG1's "16 of `Spin(10)`" clause | pass | passes 1, 2, 4; 3 conditional, disclosed |

R-CG1 is a reading of words already in CG1, CH1 and MT1 ("light spectrum", "content", "modes"). The states reading would let the site's Fock content count as a family, which no part's text describes as an excitation; it is named and not used.

---

## 6. Open statements and attacks

**LW1-5-16.** Answered (refuted for CG1's field reading) by Theorems K and P, with the escapes E1-E4 of section 2.5. Not open.

**LW1-5-Σ.** Answered in two parts (section 3, answer to item 2). The remaining physics is LW1-5-BG.

**LW1-5-BG (OPEN, GA2/VC1).** In one-class `L5-O` every site carries a spinor-class Gauss charge and no link has a flux-free state (Proposition S5(iii), Remark). Does the link sector still have a long-distance limit that GA2 can compare with continuum Yang-Mills with the matter of CG1?
- *Attack 1 (regroup the degrees of freedom).* Move the site's Clifford module into one link end, so that sites become neutral. This fails: `z_x = −1` is a statement about the whole space at `x` and does not depend on how it is split into factors. Any regrouping inside `x`'s space has the same `z_x`.
- *Attack 2 (screen by matter).* Bind matter to the site charge to make local singlets. This fails: matter operators commute with `z_x` (K1), so no matter state changes the class (Theorem P(ii)).
- *Attack 3 (strong coupling).* Compare with Kogut-Susskind strong coupling, whose ground state is flux-free on every link. This fails as a route here: `L5-O[S_+]` has no flux-free link state (Remark), and the plaquette class is open (GA1-P-5), so neither the strong-coupling ground state nor the small-field energy (GA1(a)(4)) can be written down yet.
A proof either way needs GA1-P-5.

**LW1-5-RQ (owner decision).** As in `LW1_5_DRAFT.md` section 8.3, with the evidence of this draft (FINISH).

**Inherited, unchanged.** LW1-5-X, LW1-5-T, GA1-P-5, LW1-U_f and LW1-U_sea on parity configurations, LW1-N.

---

## FINISH

**Proved here (pass 1, not refereed).**
- Lemma K0: the centre elements `ω_x`, `z_x` and their site factors (`−iP_x`, `−1`); for `so(20)` registers both ends of a link have the same `ε`.
- Lemma B10: every continuous homomorphism `Spin(10) → O(10)` kills `−1`. So any Bogoliubov action of `Spin(10)` on a site has `−1` acting trivially on the site algebra.
- Lemma F: under Bogoliubov frames the site algebra is `Λ(C^{10})`; fermion-odd site operators are class 2 (`10, 120, 252, 120, 10`).
- Theorem K: for every register assignment in PS-6r's wording and every Spin(10)-exact law, matter is tensor class, matter's spinor-class charge is a number in every state, the local centre projections are constants of the motion, Lemma Z's "no spinor-class local operator" holds exactly for end-pure registers, and for link-pure registers spinor classes come in pairs.
- Proposition E: mixed `so(20)` registers give spinor-class operators at two sites (bosonic and fermion odd); a wider end-mixed register gives a fermion-odd operator with a half-spin representation (a 16 or 16bar) at one site.
- Theorem P: spinor-class Gauss charges are static probes: never made, moved or screened by matter, by gates or by gauge-invariant operators; never singlets.
- Proposition S′: `f(g) = Ad(S_+(g) ⊕ 1)` embeds `Spin(10)` in `G_full` with `f(−1)` the parity frame; under it odd site operators are 16s and `H_−` is invariant; it is not Bogoliubov, so `L5-O` breaks it and `L_full` keeps it.
- Lemma S: the Z4 criterion for singlets in products of `H_+`, `H_−`, `C^{10}`, `C`.
- Theorem S1: on a fixed pattern of `S_+` and `C^{20}` links, pure Gauss singlets at every site exist exactly when every site has an odd number of `S_+` links; c10 has them.
- Lemma S2: every link is fixed and reversed by an element of `𝒢`; the two tilings are the two link orbits.
- Theorem S3: a covariant end-pure assignment has pure singlets only with opposite centre classes on the two tilings.
- Proposition S4: one reducible class `S_+ ⊕ C^{20}` conserves each link's class and reproduces c10 as a sector chosen by `ω_0`.
- Proposition S5: gauge-invariant states pure on the gauge-invariant algebra exist in one-class `L5-O`; on the full algebra every gauge-invariant state is mixed at every site.
- Proposition T: every closed subgroup of `Spin(10)` is an exact gauge subgroup with its own Gauss law; subgroups containing `−1` have no singlets with one register class; `SU(2)_W` does not contain `−1` and has singlets at every site.

**Counterexamples.**
- To Lemma Z(iii)'s last sentence without its hypothesis: Proposition E (mixed registers give local gauge-covariant spinor-class operators, fermion odd ones included).
- To pairing for registers outside `so(20)`: Proposition E(ii) (a half-spin representation at one site).
- To "a Spin(10) inside the frames of PS-5 and PS-6 always puts fermion-odd site operators in the vector class": Proposition S′ (`f(Spin(10)) ⊂ G_full`).
- To "the obstruction to singlets is about the register class alone": Theorem S3 (it is a parity count of spinor-class objects at a site; opposite classes on the two tilings remove it).

**Open, by name.** LW1-5-BG (three attacks recorded). Inherited and unchanged: LW1-5-X, LW1-5-T, GA1-P-5, LW1-U_f, LW1-U_sea, LW1-N. Owner decision: LW1-5-RQ.

**What this means for LW1-5-RQ.**
- `L5-O` keeps `Spin(10)` exact and meets #10014's condition (a). It does not escape either obstruction inside its own terms. The 16 is site content (states), never a field or a moving excitation, for every finite register choice (Theorems K, P). So on `L5-O`, CG1 can be met only through its "Standard Model multiplet" clause after breaking, with tensor-class parents, and #10014's field-level steps (anomaly, mass protection of the 16) do not apply to its excitations.
- The singlet obstruction is removable at the level of text: VC1 needs no pure singlet under LW1's own reading (Proposition S5). The physical price, a spinor-class Gauss charge at every site and no flux-free link, is LW1-5-BG and waits on GA1-P-5. Pure singlets need c10 or its c12 form, which fail test 4 today.
- GA2 on `L5-O` needs Yang-Mills for `Spin(10)` before breaking, which is outside the planned SU(2)-then-SU(N) path of `TOE_ASSEMBLY.md` line 535. `SU(2)_W` is exact with singlets, but only as a subgroup.
- The one escape from the centre found inside PS-5 and PS-6 is `f(Spin(10)) ⊂ G_full` (Proposition S′). It is not `L5-O` or `L5-U`. Choosing it because it gives the 16 fails test 1 (choice c15). If the owner wants the 16 as a field, the evidence points to a law with hops beyond one site mode, not to a register choice.
- This draft does not choose between `L5-O` and `L5-U`.

**Inputs from outside the working set.** `LW1_5_DRAFT.md` results named above (Theorem C, Lemmas C1 and Q, Theorems M, G, Corollary R.1, Propositions Σ and A, Lemma Z), and B5B's Lemma G3 (automorphisms of a full matrix algebra are inner; implementers unique up to a phase), as cited there. `LW1.md` Lemma A1, line 33 (the group `𝒢`), line 47 (gauge-invariant states), line 201. Standard mathematics, rebuilt in the text: alternating multilinear maps factor through `Λ^k`; Schur's lemma and isotypic decomposition; complete reducibility of unitary representations; the charge-conjugation matrix from the transpose automorphism; elementary facts on central elements of a connected double cover. Standard mathematics cited, not rebuilt: simplicity of `so(10)` (normal subgroups of `Spin(10)` are central or everything); integration of `so(10)` representations to `Spin(10)`. Literature context, never load-bearing: Kogut-Susskind Hamiltonian lattice gauge theory and its strong-coupling vacuum; quantum link models of `SO(N)` (Brower-Chandrasekharan-Wiese); the Wilczek-Zee construction of the 16 from `Λ(C^5)`; the Pati-Salam and Georgi-Glashow embeddings of `SU(2)_W` in `Spin(10)`.
