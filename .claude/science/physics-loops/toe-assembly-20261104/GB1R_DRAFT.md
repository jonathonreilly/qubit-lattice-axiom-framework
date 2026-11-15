lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1R: selected ground states through the register limit, pass 1

Written 2026-11-09 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). Lane: wall W1, leaf R of `GB1_TREE.md`.

**What this file is.** An author-side long draft. It grants no status. It adopts no law, no reading, no state prescription and no class. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means that the argument is written out below and has not yet been distilled or refereed. Every proof is a finite-dimensional linear-algebra argument, an estimate on a fixed finite tensor product of `ℓ²` spaces, or a standard measure-theoretic limit (dominated convergence, Fubini, Fourier inversion for Schwartz functions), written for Lean formalization. "[check]" marks one tiny scratch computation (section 8); a check guides and never proves.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `b5bf445d7a1ed97ccf38c5f329d4b6cff44c1ba0` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `1e0d3b58dcda7f83152b0bb51729260247454d65` |

Files read at those commits, by line. This folder (`.claude/science/physics-loops/toe-assembly-20261104/`): `prior/GB1R.md` (all 80 lines); `GB1_TREE.md` (all 793 lines; node R at 558-590, Lane brief 2 at 784-788, candidate table at 674-711); `LW2M_DRAFT.md` lines 1-60 (head, questions, outcome, setting); `LW2_DRAFT.md` lines 1-4, 57-59 (outcome), 270-328 (LW2-G, Theorems G1-G5); `GB1QL.md` lines 1-12 (status), 29-100 (definitions), 100-136 (Lemma 4.1), 137-160 (Proposition 4.2), 165-185 (Lemma 4.3, Remarks 4.4-4.6, R1), 209-230 (gates, Lemma 4.7, Theorem 4.8), and the grep hits for Corollaries 4.9-4.10; `GB1E.md` lines 1-40 and 186-224 (Theorems 8.1-8.3, hand-off); `GB1ISO.md` lines 7, 48-60 (Theorems 2.2-2.3), 135-137, 154-166 (section 6, Theorem 6.1); `GB1.md` lines 1-30 (status with Amendments 1-4) and 93-125 (section 4, Theorems 5.1-5.2); `GB1_GEN_OWNER_CHECK.md` lines 7, 15, 19-32, 77; `TOE_ASSEMBLY.md` lines 201-270 (sections 3.4-3.11) and 743-759 (section 11); `LIT_QLM.md` lines 1-8, 28-36, 74-90. On `origin/main`: `docs/FIXED_COUPLING_ROTOR_GROUND_CUTOFF_COMPACTNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md` lines 1-330 (owned argument 1 in full; the start of argument 2). The other `docs/` notes the digest names were not opened; they are listed in "Prior work used" with the digest's quotations, marked as such.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The family of Hamiltonians and the state prescription are read plainly from the R-SUM record and GB1's registers. Where a definition is needed that the sources do not fix (which ground state is "selected"), section 7 states it as a candidate and four-tests it. Nothing is adopted.

**Working set used, by name.** PS-6 and PS-6r (finite link registers), only through the specified register families of `GB1.md` Theorem 5.2 (U(1), integer `S`) and `GB1QL.md` section 1.2 (SU(2), `R_s`). The generator reading R-SUM of `TOE_ASSEMBLY.md` section 3.11, as recorded in `GB1_GEN_OWNER_CHECK.md` lines 25-32, applied to the four-tiling layer FP of `GB1ISO.md` section 6. No other axiom, law or decision is used. The results are family results for a supplied Hamiltonian; they say nothing about VC1, the tick, or a fixed law.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the spectral theorem in finite dimension and for one self-adjoint operator on a separable Hilbert space (used through spectral measures only), Stone's theorem, the Duhamel identity for bounded perturbations of a self-adjoint generator (Lemma D, proved), the Lieb-Robinson bound for bounded plaquette interactions with arbitrary on-site terms (Lemma LR, proved in finite dimension), compactness of tight sequences of density matrices (Lemma K, proved), a Perron-Frobenius lemma (Lemma PF, proved), Fourier inversion for Schwartz functions on `R`, Fubini, and dominated convergence. Literature is context only (section "Literature read") and never a proof step.

**[check].** `/tmp/toe-GB1R/check_gb1r.py`, output `/tmp/toe-GB1R/out.txt`, run with `python3 -I`; details and size in section 8.

---

## 0. The question, quoted

`GB1_TREE.md` line 562, node R: "**Statement.** For a fully specified family with the repaired magnetic interaction, prove local convergence of selected states and Euclidean correlators as \(s\to\infty\). Control volume dependence. State every allowed interchange of limits." Line 564: "**Status: OPEN.**" Line 568, imported hypotheses: "candidate family \(L[s]\); **C**; positive unwrapped \(\tau_E\); a fixed state prescription; **S**; the fixed-box semigroup theorem `GB1E.md`, Theorem 8.3."

Lines 572-582, the preferred route: "Use the zero-flux trial state and the representation-uniform plaquette norm. Seek a cell-orbit bound of the form \(\omega_s(E_\ell^2)\le C\frac{|\theta|}{\tau_E}\). This should give local electric-tail tightness. Combine it with finite-flux operator convergence. Pass the ground-state inequality \(\omega_s\!\left(A^*[H_s,A]\right)\ge0\) to a limit on a local core. Then establish convergence of Euclidean insertions." Line 584: "The first result may identify subsequential ground states. It must not claim uniqueness or VC1 membership."

Lines 786-788, Lane brief 2: "Use a specified cube-coupling Hamiltonian with positive electric energy. Prove a local electric-energy bound independent of volume and register size. Derive tail tightness. Pass the local ground-state inequality to a regular-link limit. Then treat bounded Euclidean insertions. Start with one \(U(1)\) plaquette. Extend to coupled cubes before \(SU(2)\). Claim subsequential states unless uniqueness is proved." "**Stopping rule:** a local convergence theorem; a counterexample to the proposed uniform bound; or one remaining lemma that fails **energy-tail control**, **local commutator convergence**, and **normalized Euclidean insertion control**."

The tree is a sketch by Codex gpt-6-astra and nobody had checked it. Its node-R statements used here were checked as follows. The proposed bound (line 574) is proved below in the form `Σ_i ω(E²_{ℓ_i}) ≤ 3b|θ|/τ_E` over the three link directions (Theorem E), for translation-invariant ground states; section 7.1 shows that the local ground-state inequality alone does not give it. The imported hypothesis "**C**" (an admissible finite-register cube-coupling *update*) is not used: the cube coupling here is a Hamiltonian, the R-SUM Hamiltonian of FP (Lemma 1.1), so node C's finite-depth question does not arise. The imported `GB1E.md` Theorem 8.3 is not used.

## 0.1 Outcome in one paragraph

**Proved: a local convergence theorem, the brief's first stopping point.** The specified cube-coupling Hamiltonian is the R-SUM Hamiltonian of FP, `H = τ_EΣ_ℓE²_ℓ + θΣ_pB_p` over all plaquettes, on GB1's integer-spin U(1) links and GB1QL's SU(2) family `R_s` (Lemma 1.1). The selected states are the translation-invariant physical ground states (candidate S-GS). **Rungs.** On one U(1) plaquette and on two coupled U(1) cubes the regular-link ground state is unique, and finite-register ground states converge to it with energy error `O(S^{−2})` (Theorem P, Lemma 3.1); on every finite SU(2) region the regular-link ground state is unique and the finite-register ground states converge to it (Theorem C). **Tori.** The zero-flux trial gives `Σ_iω(E²_{ℓ_i}) ≤ 3b|θ|/τ_E`, independent of volume and register size (Theorem E), hence tail tightness and trace-norm subsequential limits along any joint sequence of volumes and registers (Theorem L). The local ground-state inequality passes to the regular-link limit on a flux-bounded core (Theorem G). A Lieb-Robinson bound whose constants see only the plaquette norm (Lemma LR) gives the regular-link infinite-volume dynamics and convergence of all multi-time real-time correlators (Theorem D); the limit is a GNS ground state with `H_ω ≥ 0` (Theorem GS); and every normalized Euclidean insertion converges (Theorem EU). No gap, isolation or uniqueness is assumed on tori, and none is claimed there. **One counterexample:** at `θ = 0`, background-field states satisfy the local ground-state inequality with arbitrarily large `ω(E²)` (Proposition BF), so the bound comes from the finite-volume selection. **Not supplied:** uniqueness on tori, rates in volume, the tick or VC1, a Euclidean measure.

## Prior work used

Each item is used or extended below, with its path. "Ported" means rebuilt in this file with credit.

1. **The repository's rotor ground-cutoff theorem (main precursor, ported and extended).** `origin/main:docs/FIXED_COUPLING_ROTOR_GROUND_CUTOFF_COMPACTNESS_BOUNDED_THEOREM_NOTE_2026-09-15.md`, owned argument 1 (unaudited). Its line 76-79: "every sequence L_j->infinity, S_j->infinity has a subsequence converging in trace norm on each fixed finite region to a locally normal, physical, translation-invariant rotor ground state. The order or relative rates of these two limits need not be prescribed." Its sections 2-6 give the variational electric moment from an exact physical zero-flux trial (eqs. (2)-(4)), the gentle-projection compactness (eq. (5)), the ground-state inequality on a local core (eqs. (6)-(7); line 193: "no many-body spectral gap is used"), a same-state dynamics comparison (eq. (8)), and the spectral condition by Fourier test functions (section 6). That note treats a charged U(1) rotor model with the projection cutoff `P_S H P_S`. **What this file adds:** quantum-link coefficients that differ from one at every flux (U(1) spin-`S` links and the SU(2) `so(5)` family, not a projection); the full-plaquette R-SUM Hamiltonian of FP; a Lieb-Robinson bound whose constants see only the plaquette norm (Lemma LR), so that multi-time real-time correlators pass to the limit with no tightness of evolved vectors; normalized Euclidean insertions of any order (Theorem EU); and, on finite regions, uniqueness and convergence with rates (Theorems P and C). Theorems E, L, G and GS follow that note's structure.
2. **`GB1.md` Theorem 5.2 (U1-LS)**, line 113: the normalized U(1) quantum link with "normalized raising coefficient \(\kappa_+(m)=\sqrt{1-m(m+1)/[S(S+1)]}\)" and embedding "\(|m\rangle\mapsto|m\rangle\)". Used in Definition 1.2 and Lemma 1.3.
3. **`GB1QL.md`** (frozen): section 1.2 (the family `R_s`, `U_s`), Lemma 4.1(b) (`E² = k(k+2)/4` on `H_k`), Proposition 4.2(d) ("`‖U_s‖ ≤ 1` on `C² ⊗ R_s`", line 147), Lemma 4.3 (line 165, the low-flux bound `δ_s(M')`), the plaquette step of Lemma 4.7 (line 219: "`‖(B̃_p − B_p)v‖ ≤ 16δ_s(M'')‖v‖`"), the Markov and gentle-measurement steps in the proof of Corollary 4.9, and the density closure R2. Ported in Lemma 1.3 and Lemma K.
4. **`GB1ISO.md`** (frozen): Theorem 6.1 (line 161, "Every spatial plaquette occurs twice in their combined face sum"), used in Lemma 1.1; Theorem 2.2 (line 50, "\(k_t(g)>0\) for every \(t>0\)"), used in Lemma PF(b); the sign argument in the proof of Theorem 2.3 (line 60), ported in Lemma PF.
5. **`GB1E.md`** (frozen): Theorem 2.2 (line 52, \(k_t\) "is the convolution kernel of \(e^{-tE^2}\)"), used in Lemma PF(b). Theorem 8.3 (line 198, fixed box, thermal) is the fixed-box precursor of node R; it is not used.
6. **`GB1_GEN_OWNER_CHECK.md`** lines 25-32, the R-SUM record, used in Lemma 1.1.
7. **`LW2M_DRAFT.md`** (unfrozen pass-1 draft): FP as an ordered word fails cell covariance (its section 0.1). Lemma 1.1 uses the R-SUM *sum*, which has no ordering, so this failure does not touch it. **`LW2_DRAFT.md`** (unfrozen pass-1 draft): Theorem G3 (positivity of the fixed-step kernel at large `s`) is context; not used.
8. **Digest items not opened here** (quoted from `prior/GB1R.md`, not re-read, not used as proof steps): the charged finite-link local-dynamics note (`docs/CHARGED_FINITE_LINK_LOCAL_DYNAMICS_AND_PHASE_BRIDGE_BOUNDED_THEOREM_NOTE_2026-09-13.md`); the SU(3) electric-dominated gap note (`docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md`, "is not a joint-limit theorem"); the compact-rotor correlation and path notes (2026-09-16); the clock notes; the SU(3) Peter-Weyl local-observable and compression notes. All are unaudited per the digest.

**Failed attempts on file, respected.** The flux restriction cannot be dropped from operator comparisons (`GB1QL.md` Remark 4.6 and R1: error "at least `0.9θ²`, for every `s`"). Every comparison below is made on low flux inside a tight state, never uniformly on the register. The cutoff is not a reducing subspace of the regular-link Hamiltonian; as in item 1, the cutoff is removed on the test operator.

**Prior work the digest missed.** `GB1QL.md` Proposition 4.2(d), the contraction property that gives the representation-uniform plaquette norm the tree asks for (node R line 572); `GB1QL.md` Remark 4.4(ii) (line 175: "`R_s` is the space Tong et al. keep at `Λ = s`"), which places Tong et al.'s projected regulator and this family on the same space; `GB1ISO.md` Theorems 2.2-2.3 (strict heat-kernel positivity and the constant-sign argument), which give uniqueness on finite SU(2) regions here.

## Literature read

Searches run (2026-11-08/09, web search plus arXiv abstract pages): Tong-Albert-McClean-Preskill-Su truncation; Lieb-Robinson bounds with unbounded on-site terms; quantum-link convergence to Kogut-Susskind at large representation; Ciavarella truncation; Zohar-Burrello truncation; existence of infinite-volume ground states for Hamiltonian lattice gauge theory; weak-* limits of finite-volume ground states and the local ground-state condition. No source found in these searches proves convergence of quantum-link or truncated Kogut-Susskind *ground states* to a regular-link ground state in 3+1 dimensions uniformly in volume. That is a statement about these searches, not a novelty claim. Every item below is context; none is a proof step.

1. **Y. Tong, V. V. Albert, J. R. McClean, J. Preskill, Y. Su**, *Provably accurate simulation of gauge theories and bosonic systems*, arXiv:2110.06942 (v2, 2022-09-20), Quantum 6, 816 (2022). Abstract page fetched; PDF text read at the passages cited. Abstract: "if the initial state has low local quantum numbers, then an error at most $\epsilon$ can be achieved by choosing $\Lambda$ to scale polylogarithmically with $\epsilon^{-1}$". Appendix Theorem 5 (state truncation, eq. (9)); Theorem 6 (Hamiltonian truncation, eqs. (64)-(66)), which assumes "all projection operators Π(ν) λ commute with each other" and truncates by `Πall HΠall`. Theorem 12 (quantum-number tail of an eigenstate) assumes "|Ψ⟩ is an eigenstate of H corresponding to an eigenvalue ε with multiplicity 1, and that ε is separated from the rest of the spectrum of H by a spectral gap δ", and a finite mean absolute quantum number. **Relation.** Their regulator is a projection; here the U(1) and SU(2) links have coefficients below one at every flux. Their Theorem 12 needs a simple isolated eigenvalue; Theorems E-EU below use neither multiplicity one nor a gap, and give no polylogarithmic rate. `GB1QL.md` Remark 4.4(ii) records that both regulators live on the same space `R_s`.
2. **B. Nachtergaele, H. Raz, B. Schlein, R. Sims**, *Lieb-Robinson bounds for harmonic and anharmonic lattice systems*, arXiv:0712.3820, Commun. Math. Phys. 286 (2009) 1073-1098. Abstract page and section 2 fetched (ar5iv). Section 2 takes "a collection of local operators H^loc = {H_x} where each H_x is a self-adjoint operator" ("these operators H_x need not be bounded") and a bounded interaction Φ, with `H_Λ = Σ_{x∈Λ} H_x + Σ_{X⊂Λ} Φ(X)` (eq. (2.4)); Theorem 2.1, eqs. (2.6)-(2.8), bounds `‖[τ_t^Λ(A), B]‖` with constants built from `‖Φ‖_a` only. **Relation.** Lemma LR below is the finite-dimensional case for plaquette interactions, rebuilt; its key step (the decoupled dynamics contains every on-site term and so preserves the local algebra) is theirs.
3. **B. Nachtergaele, R. Sims**, *On the dynamics of lattice systems with unbounded on-site terms in the Hamiltonian*, arXiv:1410.8174. Abstract fetched: "We supply the mathematical arguments required to complete the proofs of two previously published results: Lieb-Robinson bounds for the dynamics of quantum lattice systems with unbounded on-site terms in the Hamiltonian and the existence of the thermodynamic limit of the dynamics of such systems." Context for Theorem D(c); the infinite-volume regular-link dynamics is built here from the uniform finite-register bounds instead.
4. **E. Zohar, M. Burrello**, *A formulation of lattice gauge theories for quantum simulations*, arXiv:1409.3085, Phys. Rev. D 91, 054506 (2015). Abstract page fetched: it rewrites "the Kogut-Susskind formulation of lattice gauge theories" with group-element and representation bases. A search snippet of the published abstract mentions "a consistent truncation of the Hilbert space for continuous groups"; the body was not read. NOT VERIFIED beyond the abstract page.
5. **A. N. Ciavarella, S. Hariprakash, J. C. Halimeh, C. W. Bauer**, *Truncation uncertainties for accurate quantum simulations of lattice gauge theories*, arXiv:2508.00061 (v4, 2026-09-04). Abstract fetched: "Generically, the truncation error falls off as a factorial of the field truncation." These are error estimates for dynamics, applied to the Schwinger model and pure U(1); the abstract states no theorem on ground states. Body NOT VERIFIED.
6. **S. Chandrasekharan, U.-J. Wiese**, *Quantum link models: a discrete approach to gauge theories*, arXiv:hep-lat/9609042, Nucl. Phys. B 492 (1997) 455-474. Abstract fetched: "the elements of the link matrices are represented by non-commuting operators acting in a Hilbert space." `GB1QL.md` section 1.2 identifies `R_s` with their SU(2) link in an `so(5)` representation.
7. **B. Schlittgen, U.-J. Wiese**, *Low-energy effective theories of quantum link and quantum spin models*, arXiv:hep-lat/0012014, Phys. Rev. D 63 (2001) 085007. Abstract fetched ("This D-theory regularization leads to the same continuum theories as the conventional approach"). `LIT_QLM.md` section 3 classifies its large-representation step as semiclassical, without uniform remainder bounds. Context only.
8. **O. Bratteli, D. W. Robinson**, *Operator Algebras and Quantum Statistical Mechanics 2*, the ground-state notion for C*-dynamical systems. A book; NOT VERIFIED (not fetched). The ground-state statements below are proved directly in the GNS form and do not rely on it.

## 1. The family made exact

### 1.1 Lattice, regions, plaquettes

Links of `Z³` are `ℓ = (x, x+e_i)`, `i ∈ {1,2,3}`. A plaquette `p` with base `y` in the `(i,j)`-plane, `i < j`, has links `ℓ_1 = (y, y+e_i)`, `ℓ_2 = (y+e_i, y+e_i+e_j)`, `ℓ_3 = (y+e_j, y+e_i+e_j)`, `ℓ_4 = (y, y+e_j)`, traversed `ℓ_1, ℓ_2` forward and `ℓ_3, ℓ_4` backward. A link lies in exactly 4 plaquettes. Two distinct plaquettes share at most one link, so a plaquette shares a link with exactly 12 others. A **region** is a finite set `Γ` of links; `P(Γ)` is the set of plaquettes with all four links in `Γ`; the vertices of `Γ` are the endpoints of its links. The torus `Λ_L = (Z/LZ)³`, `L ≥ 3`, has `3L³` links and `3L³` plaquettes, all four links of a plaquette distinct. For a finite link set `X` and `r ≥ 0` put `X_0 = X` and `X_{r+1} = X_r ∪ {links of plaquettes meeting X_r}`.

### 1.2 Links and registers

**Definition 1.2 (links).** `G ∈ {U(1), SU(2)}`; register label `s ∈ {1, 2, …} ∪ {∞}`, where `s = ∞` is the regular link.

*U(1).* `𝒦 = ℓ²(Z)`, `E|m⟩ = m|m⟩`, `U|m⟩ = |m+1⟩` (unitary). Flux of `|m⟩` is `|m|`. For an integer `S ≥ 1`, `R_S = span{|m⟩ : |m| ≤ S}` and `U_S|m⟩ = κ_S(m)|m+1⟩` for `−S ≤ m ≤ S`, with `κ_S(m) = √(1 − m(m+1)/(S(S+1)))`; note `κ_S(S) = 0` and `κ_S(−m−1) = κ_S(m)`. This is `S^+/√(S(S+1))`, the normalized link of `GB1.md` Theorem 5.2. `ι : R_S → 𝒦` is the inclusion and `Ũ_S = ιU_Sι^*` (zero on `R_S^⊥`). For a plaquette, `U_p = U_{ℓ_1}U_{ℓ_2}U_{ℓ_3}^*U_{ℓ_4}^*` and `B_p = U_p + U_p^*`; at finite `S` the same words in `Ũ_S` give `B̃^{(S)}_p`. Gauss generator at a vertex `x` of a region: `G_x = Σ_{ℓ ∋ x} ±E_ℓ` (plus for links leaving `x`, minus for links entering), gauge unitaries `V_x(α) = e^{iαG_x}`.

*SU(2).* `𝒦 = L²(S³, σ) ≅ L²(SU(2))`, `R_s = H_0 ⊕ ⋯ ⊕ H_s`, `E² = k(k+2)/4` on `H_k`, `U = Σ_μ x_μ ⊗ e_μ`, `U_s = Σ_μ P_μ ⊗ e_μ`, the gauge action, all as in `GB1QL.md` sections 1.1-1.2 and 1.5 item 3. Flux of `H_k` is `k`. `X_p = U_{ℓ_4}^*U_{ℓ_3}^*U_{ℓ_2}U_{ℓ_1}` (the corrected order of `GB1QL.md` section 1.3), `B_p = tr X_p + (tr X_p)^*`; `B̃^{(s)}_p` is the same word in `ιU_sι^*`.

For `s = ∞` put `B̃^{(∞)}_p = B_p`. Write `Π^ℓ_M` for the projection onto flux `≤ M` on link `ℓ`, `Π^X_M = ∏_{ℓ∈X}Π^ℓ_M`, and `e_G(k)` for the value of `E²` at flux `k`: `e_{U(1)}(k) = k²`, `e_{SU(2)}(k) = k(k+2)/4`. Both increase in `k`, so `E²_ℓ ≥ e_G(M+1)` on the range of `1 − Π^ℓ_M`.

### 1.3 The specified cube-coupling Hamiltonian

**Definition 1.4.** Fix `τ_E > 0` and `θ ∈ R`. For a region or torus `Γ` and a label `s`,
```
H_{Γ,s} = τ_E Σ_{ℓ∈Γ} E_ℓ² + θ Σ_{p∈P(Γ)} B̃^{(s)}_p .
```
For finite `s` it acts on `R_s^{⊗Γ}` (identified with `ι(R_s^{⊗Γ})`). For `s = ∞` it acts on `𝒦_Γ := 𝒦^{⊗Γ}` with domain `D(Σ_ℓ E²_ℓ)`; it is self-adjoint there, as a bounded perturbation of the nonnegative self-adjoint sum of commuting one-link operators. The **physical subspace** `ℋ^{phys}_{Γ,s}` is the joint fixed space of the gauge action at every vertex of `Γ`, using only links of `Γ` (open boundary for regions, periodic on tori). `H_{Γ,s}` commutes with the gauge action (Lemma 1.3(a)), so it preserves `ℋ^{phys}_{Γ,s}`. Write `e_{Γ,s}` for its lowest eigenvalue there, when it exists.

**Lemma 1.1 (the R-SUM Hamiltonian of FP).** Let `L` be even. The R-SUM Hamiltonian of the word made of the electric layer `∏_ℓ e^{−iτ_EE²_ℓ}` and the four FP layers `∏_{C∈𝒞+v} e^{−i(θ/2)B_C}`, `v ∈ {0,e_1,e_2,e_3}`, is `H_{Λ_L,s}`, for every `s`.

*Proof.* The R-SUM record (`GB1_GEN_OWNER_CHECK.md` lines 25-27): "For GB1's specified layers \(e^{-i\tau_kK_k}\), set \(H=\sum_k\tau_kK_k\)." So `H = τ_E Σ_ℓ E²_ℓ + (θ/2) Σ_v Σ_{C∈𝒞+v} B̃^{(s)}_C` with `B̃_C = Σ_{p⊂C} B̃_p`. By `GB1ISO.md` Theorem 6.1, "Every spatial plaquette occurs twice in their combined face sum"; its proof is a parity count on plaquette bases and holds on an even torus. So the double sum is `2Σ_p B̃^{(s)}_p`. No commutation of plaquette operators is used, so this holds at finite `s`. □

The sum, unlike the ordered FP word, is invariant under all lattice translations and cubic symmetries; `LW2M_DRAFT.md`'s covariance failure concerns the word. Only translations are used below, and Theorems E-EU hold for every `L ≥ 3`.

**Lemma 1.3 (register facts).** For both groups and every `s`:

(a) `E²_ℓ` and `B̃^{(s)}_p` commute with the gauge action at every vertex.
(b) `‖B̃^{(s)}_p‖ ≤ b_G`, with `b_{U(1)} = 2`, `b_{SU(2)} = 4`.
(c) The zero-flux vector `Ω_0` (`⊗|0⟩`, resp. `⊗1`) is physical, `E²_ℓΩ_0 = 0`, and `⟨Ω_0, B̃^{(s)}_pΩ_0⟩ = 0`.
(d) If `v` has flux `≤ M` on the four links of `p` and `M ≤ s`, then `‖(B̃^{(s)}_p − B_p)v‖ ≤ η_G(s,M)‖v‖`, with `η_{U(1)}(S,M) = 8M(M+1)/(S(S+1))` and `η_{SU(2)}(s,M) = 32M(M+3)/(s(s+3))`.
(e) `B̃^{(s)}_p → B_p` strongly on `𝒦^{⊗p}` as `s → ∞`.
(f) `1 − Π^ℓ_M ≤ E²_ℓ / e_G(M+1)`.

*Proof.* (a) U(1): `V_x(α)UV_x(α)^* = e^{±iα}U` with the sign of the link's orientation at `x`, and `Ũ_S` raises flux by one exactly as `U` does, so the same holds for `Ũ_S`; in `U_p` the phases at each vertex cancel (at `y`: `ℓ_1` forward, `ℓ_4` backward, both leaving `y`; similarly at the other three corners). SU(2): `GB1QL.md` section 1.5 item 3 and the corrected order of section 1.3. (b) U(1): `κ_S ≤ 1`, so `‖Ũ_S‖ ≤ 1`, `‖U_p‖ ≤ 1`. SU(2): `‖U_s‖ ≤ 1` (`GB1QL.md` Proposition 4.2(d)) and `‖U‖ = 1`, so `‖X_p‖ ≤ 1`; for an operator matrix `M` on `C² ⊗ 𝒦'`, `tr M = Σ_a (u_a^* ⊗ 1)M(u_a ⊗ 1)` has norm `≤ 2‖M‖`. (c) U(1): `U_pΩ_0` has fluxes `(1,1,−1,−1)`. SU(2): each entry of `U_s` or `U_s^*` is a combination of the `P_μ`, and `P_μ` maps `H_0` into `H_1` (`P_μ = x^+_μY_s + Y_sx^-_μ`, `x^-_μ H_0 = 0`); so every term of `tr X^s_pΩ_0` lies in `H_1` on all four links. The constant function is invariant under rotations, so `Ω_0` is physical. (d) U(1): for `|m| ≤ M ≤ S`, `(Ũ_S − U)|m⟩ = (κ_S(m) − 1)|m+1⟩` and `(Ũ_S − U)^*|m⟩ = (κ_S(m−1) − 1)|m−1⟩`; since `0 ≤ κ ≤ 1`, `1 − κ_S(m) ≤ 1 − κ_S(m)² = m(m+1)/(S(S+1)) ≤ M(M+1)/(S(S+1))`, and the same for `m−1`. The operators are diagonal-to-shifted, so `‖(Ũ_S − U)v‖ ≤ (M(M+1)/(S(S+1)))‖v‖` for `v` of flux `≤ M` on that link. Telescope as in `GB1QL.md` Lemma 4.7: `Ũ_p − U_p = Σ_i F_1⋯F_{i−1}(F̃_i − F_i)F̃_{i+1}⋯F̃_4`; the factors right of position `i` act on other links and keep the flux of `ℓ_i`; all factors have norm `≤ 1`. This gives `4M(M+1)/(S(S+1))` for `U_p` and the same for `U_p^*`. SU(2): `GB1QL.md` Lemma 4.3 with `δ_s(M') = 2M'(M'+3)/(s(s+3))` (defined at its line 163) and the plaquette step of Lemma 4.7 (line 219: "`‖(B̃_p − B_p)v‖ ≤ 16δ_s(M'')‖v‖`"). (e) By (d), `(B̃^{(s)}_p − B_p)v → 0` for every finite-flux `v`. Finite-flux vectors are dense (U(1): finite sequences; SU(2): `GB1QL.md` closure R2, then tensor products). With the uniform bound (b) this gives strong convergence on all of `𝒦^{⊗p}`. (f) On flux `> M`, `E² ≥ e_G(M+1)`; both sides are functions of the same commuting operators. □

### 1.4 The selected states, local algebras and the core

**Definition 1.5 (candidate state prescription; four-tested in section 7).** For finite `s` and `L ≥ 3`, `𝔊_{L,s}` is the set of states `A ↦ Tr(ρA)` on `B(R_s^{⊗Λ_L})` with `ρ` a density matrix supported in the lowest eigenspace of `H_{Λ_L,s}` on `ℋ^{phys}_{Λ_L,s}` and invariant under all translations of `Λ_L`. The ground-space average `Tr(P_{L,s}·)/Tr P_{L,s}` lies in `𝔊_{L,s}` (translations commute with `H_{Λ_L,s}` and the Gauss law, hence with the ground projection `P_{L,s}`), so `𝔊_{L,s} ≠ ∅`.

For a finite link set `X ⊂ Z³` write `𝒦_X = 𝒦^{⊗X}` and identify `B(𝒦_X)` with `B(𝒦_X) ⊗ 1 ⊂ B(𝒦_Y)` for `X ⊂ Y`. `𝔄` is the C*-inductive limit of the `B(𝒦_X)`. `B(𝒦_X)^G` is the set of operators commuting with the restriction to `X` of the gauge action at every vertex; `𝔄^G` is the closure of their union. For `L` larger than `2 diam X + 4`, `X` is identified with its image in `Λ_L`, and a state `ω` of the torus register gives the density matrix `ρ^X_ω = ι_X(Tr_{Λ_L∖X}ρ)ι_X^*` on `𝒦_X`.

**The core.** `𝒟 = ∪_{X,M} 𝒟^M_X`, `𝒟^M_X = {A ∈ B(𝒦_X)^G : A = Π^X_MAΠ^X_M}`. It is a `*`-algebra: if `A = PAP`, `B = P'BP'` with cutoffs `M, M'` on `X, X'`, then `Q = Π^{X∪X'}_{max(M,M')}` satisfies `QAB = AB = ABQ`, because on links of `X'∖X` the projection commutes with `A` and is absorbed by `P'`, and symmetrically. For `A ∈ 𝒟^M_X`, `M ≤ s`, the operator `A` maps `ι(R_s^{⊗Γ})` into itself and its compression `ι^*Aι` is a register operator. For `A ∈ 𝒟^M_X` put `X^+ = X_1` and
```
[H^{(s)}, A] := τ_E Σ_{ℓ∈X} [E²_ℓ, A] + θ Σ_{p ∩ X ≠ ∅} [B̃^{(s)}_p, A]  ∈ B(𝒦_{X^+}),
```
a finite sum; `‖[E²_ℓ, A]‖ ≤ 2e_G(M)‖A‖` since `E²_ℓΠ^ℓ_M` is bounded by `max_{k≤M} e(k)`. On a region or torus containing `X^+`, this is the commutator of `A` with `H_{Γ,s}`, because every other term commutes with `A`.

## 2. One U(1) plaquette

The section is written for a U(1) region `Γ` that satisfies (Gen) below; one plaquette is the first case, two coupled cubes the second (section 3).

**Flux picture.** On a U(1) region `Γ`, `ℋ^{phys}_{Γ,∞} = ℓ²(𝒵(Γ))`, where `𝒵(Γ)` is the set of integer flows `c ∈ Z^Γ` with zero divergence at every vertex (out-flux minus in-flux, links of `Γ` only). `Q(c) = Σ_ℓ c_ℓ²` is the electric operator `Σ_ℓ E²_ℓ`. For `p ∈ P(Γ)` let `∂p ∈ 𝒵(Γ)` be `+1` on `ℓ_1, ℓ_2` and `−1` on `ℓ_3, ℓ_4`. Then `U_p|c⟩ = |c+∂p⟩` and `Ũ_{S,p}|c⟩ = κ_p(c)|c+∂p⟩` with `κ_p(c) = κ_S(c_{ℓ_1})κ_S(c_{ℓ_2})κ_S(c_{ℓ_3}−1)κ_S(c_{ℓ_4}−1) ∈ [0,1]` (zero if `c` or `c+∂p` leaves the cutoff). The physical register space is `ℓ²` of `{c ∈ 𝒵(Γ) : max_ℓ|c_ℓ| ≤ S}`.

**(Gen)** Every `c ∈ 𝒵(Γ)` is an integer combination of the `∂p`, `p ∈ P(Γ)`.

**Sign change.** Let `σ_ℓ ∈ {±1}` be the field of `GB1ISO.md` line 137 (`σ_{x,1} = (−1)^{x_2+x_3}`, `σ_{x,2} = (−1)^{x_3}`, `σ_{x,3} = 1`); its product over the four links of every plaquette is `−1` (a direct check in each of the three planes). `W = ∏_{ℓ∈Γ, σ_ℓ=−1} e^{iπE_ℓ}` is diagonal in flux, so it commutes with the Gauss law and with `E²`, and `WU_ℓW^* = σ_ℓU_ℓ`, `WŨ_{S,ℓ}W^* = σ_ℓŨ_{S,ℓ}`. Hence `WB̃^{(s)}_pW^* = −B̃^{(s)}_p` for every `p` and `s`, and `H_{Γ,s}(θ)` is unitarily equivalent to `H_{Γ,s}(−θ)` by the same `W`. So we may take `θ ≤ 0`.

**Lemma PF (Perron-Frobenius for a discrete Schrödinger operator; the sign argument is that of `GB1ISO.md` Theorem 2.3).** Let `𝒞` be countable, `q : 𝒞 → [0,∞)` with finite sublevel sets, `τ > 0`, and `A` a bounded self-adjoint operator on `ℓ²(𝒞)` with real entries, `A_{cc} = 0`, `A_{cc'} ≤ 0` for `c ≠ c'`, whose graph `{c ~ c' : A_{cc'} ≠ 0}` is connected. Then `H = τq + A` (self-adjoint on `D(q)`) has compact resolvent, a simple lowest eigenvalue with an eigenvector that is strictly positive at every `c`, and a gap `δ > 0` above it.

*Proof.* `(τq + λ)^{-1}` is compact (diagonal entries tend to zero), and for `λ > ‖A‖`, `(H + λ)^{-1} = (τq + λ)^{-1}(1 + A(τq+λ)^{-1})^{-1}` is compact. So the spectrum is discrete; the lowest eigenvalue `e` has a finite-dimensional eigenspace, equal to the set of minimizers of the form `h(v) = τΣ_c q(c)|v_c|² + ⟨v, Av⟩` on unit vectors of the form domain, and `δ > 0` is the distance to the next eigenvalue. `H` commutes with complex conjugation, so the eigenspace is spanned by real vectors. For real `v`, `Σ_{c≠c'}A_{cc'}|v_c||v_{c'}| ≤ Σ_{c≠c'}A_{cc'}v_cv_{c'}`, so `h(|v|) ≤ h(v)`, and `|v|` is a minimizer, hence an eigenvector. If `|v|_c = 0`, the eigen-equation at `c` reads `0 = Σ_{c'}A_{cc'}|v|_{c'}`, a sum of nonpositive terms, so `|v|` vanishes at every neighbour of `c`; by connectivity `|v| = 0`. So a nonzero real eigenvector `v` has `|v| > 0` everywhere. Then `v_± = (|v| ± v)/2` are eigenvectors or zero, nonnegative, with disjoint supports; a nonzero one is strictly positive everywhere, so one of them is zero and `v = ±|v|`. Two orthogonal real eigenvectors cannot both have a strict constant sign. So the eigenvalue is simple. □

**Lemma P1 (comparison on the cutoff space).** For every unit `v` supported on `{max_ℓ|c_ℓ| ≤ S}` and every `p`,
```
|⟨v, (B̃^{(S)}_p − B_p)v⟩| ≤ (6⟨v,Qv⟩ + 16)/S² .
```
*Proof.* Only pairs `c, c' = c+∂p` both inside the cutoff contribute, so `⟨v,(Ũ_{S,p} − U_p)v⟩ = Σ_c (κ_p(c) − 1)\bar v_{c'}v_c`. Each of the four factors of `κ_p(c)` is `κ_S(m)` for a step `m → m+1` on one link, and `1 − κ_S(m) ≤ 1 − κ_S(m)² = m(m+1)/(S(S+1)) ≤ max(m², (m+1)²)/(S(S+1))`. Since `1 − ∏_iκ_i ≤ Σ_i(1−κ_i)` for `κ_i ∈ [0,1]`, `1 − κ_p(c) ≤ (Q(c) + Q(c'))/(S(S+1))`. Use `2|v_c||v_{c'}| ≤ |v_c|² + |v_{c'}|²` and `Q(c') ≤ 2Q(c) + 8`, `Q(c) ≤ 2Q(c') + 8` (as `(a±1)² ≤ 2a² + 2` on each of four links): `|⟨v,(Ũ_{S,p} − U_p)v⟩| ≤ (3⟨Q⟩_v + 8)/(S(S+1))`. The `U_p^*` term is the complex conjugate of this one, so `|⟨v,(B̃^{(S)}_p − B_p)v⟩| ≤ 2(3⟨Q⟩_v + 8)/(S(S+1)) ≤ (6⟨Q⟩_v + 16)/S²`. □

**Theorem P (U(1) regions with (Gen); one plaquette).** Let `Γ` satisfy (Gen), `n_p = |P(Γ)|`, `J = 2|θ|n_p`, `τ_E > 0`.

(a) `H_{Γ,∞}` on `ℋ^{phys}` has a simple lowest eigenvalue `e_∞` with unit eigenvector `φ_∞`, and a gap `δ_Γ > 0`.
(b) For every integer `S ≥ 1` and every unit ground vector `φ_S` of `H_{Γ,S}` on the physical register space, with energy `e_S`: `e_S, e_∞ ∈ [−J, 0]`, and both `⟨Q⟩_{φ_S}` and `⟨Q⟩_{φ_∞}` are at most `J/τ_E`.
(c) If `(S+1)² ≥ 3J/τ_E`, then with `C_1 = 20J²/τ_E + 8J`,
```
|e_S − e_∞| ≤ C_1/S² ,    1 − |⟨φ_∞, ιφ_S⟩|² ≤ 2C_1/(δ_Γ S²) .
```
(d) For `S² > 4C_1/δ_Γ` the ground state of `H_{Γ,S}` is simple, and with phases fixed by `⟨φ_∞, ιφ_S⟩ ≥ 0`, `‖ιφ_S − φ_∞‖ ≤ 2(C_1/δ_Γ)^{1/2}/S`.

*Proof.* (a) At `θ = 0`: `H = τ_EQ`, ground state `|0⟩`, gap at least `4τ_E` (a nonzero flow has `|c_ℓ| ≥ 1` on a cycle of at least four links). For `θ ≠ 0`, take `θ < 0` by the sign change. Apply Lemma PF with `𝒞 = 𝒵(Γ)`, `q = Q` (finite sublevel sets), `A = θΣ_p(T_p + T_p^*)`, `T_p|c⟩ = |c+∂p⟩`: its entries are `θ` times nonnegative integers, its diagonal vanishes because `∂p ≠ 0`, and by (Gen) every `c` is joined to `0` by steps `±∂p`. (b) `|0⟩` is physical and `⟨0|B_p|0⟩ = 0` (Lemma 1.3(c)), so `e ≤ 0`; `H ≥ −|θ|Σ_p‖B_p‖ ≥ −J`. For a ground vector, `τ_E⟨Q⟩ = e − θ⟨ΣB_p⟩ ≤ J`. (c) Also `τ_EQφ = (e − θΣB_p)φ` gives `⟨Q²⟩_φ ≤ (2J/τ_E)²`. *Lower bound:* `ιφ_S` is a physical unit vector of finite flux, so by Lemma P1, `e_∞ ≤ ⟨ιφ_S, H_{Γ,∞}ιφ_S⟩ ≤ e_S + |θ|n_p(6J/τ_E + 16)/S² = e_S + J(3J/τ_E + 8)/S²`. *Upper bound:* let `Π` project onto the cutoff (it commutes with the Gauss law). Off the cutoff `Q ≥ (S+1)²`, so `t_0 = ‖(1−Π)φ_∞‖² ≤ 4J²/(τ_E²(S+1)⁴)` and `t_1 = ⟨(1−Π)φ_∞, Q(1−Π)φ_∞⟩ ≤ 4J²/(τ_E²(S+1)²)`; the hypothesis gives `t_0 ≤ 1/2`. Since `(H_∞ − e_∞)φ_∞ = 0`, `⟨Πφ_∞, (H_∞ − e_∞)Πφ_∞⟩ = ⟨(1−Π)φ_∞, (H_∞ − e_∞)(1−Π)φ_∞⟩ ≤ τ_Et_1 + 2Jt_0`. With `ψ = Πφ_∞/‖Πφ_∞‖`, `⟨Q⟩_ψ ≤ 2J/τ_E`, and Lemma P1, `e_S ≤ ⟨ψ, H_{Γ,S}ψ⟩ ≤ e_∞ + 2(τ_Et_1 + 2Jt_0) + J(6J/τ_E + 8)/S²`. Now `2τ_Et_1 ≤ 8J²/(τ_E(S+1)²)` and, using `(S+1)² ≥ 3J/τ_E`, `4Jt_0 ≤ 16J³/(τ_E²(S+1)⁴) ≤ 6J²/(τ_E(S+1)²)`. So `e_S − e_∞ ≤ C_1/S²`, and `e_∞ − e_S ≤ C_1/S²` from the lower bound. *Vectors:* `⟨ιφ_S, (H_∞ − e_∞)ιφ_S⟩ ≤ (e_S − e_∞) + J(3J/τ_E+8)/S² ≤ 2C_1/S²`, while by (a) and the spectral theorem `H_∞ − e_∞ ≥ δ_Γ(1 − |φ_∞⟩⟨φ_∞|)` on `ℋ^{phys}`. (d) Two orthonormal ground vectors would both have `|⟨φ_∞,·⟩|² > 1/2`, which is impossible. With the stated phase, `‖ιφ_S − φ_∞‖² = 2 − 2⟨φ_∞,ιφ_S⟩ ≤ 2(1 − ⟨φ_∞,ιφ_S⟩²)`. □

**One plaquette.** `Γ = {ℓ_1,…,ℓ_4}`, `𝒵(Γ) = Z∂p` (the Gauss law at the four corners forces `c = n∂p`), so (Gen) holds, `n_p = 1`, `Q(n∂p) = 4n²`, `J = 2|θ|`. In the basis `|n⟩ = |n∂p⟩`,
```
H_{p,∞} = 4τ_E n² + θ(T + T^*) on ℓ²(Z),      H_{p,S} = 4τ_E n² + θ Σ_{n=−S}^{S−1} κ_S(n)⁴ (|n+1⟩⟨n| + |n⟩⟨n+1|) on ℓ²{−S,…,S},
```
using `κ_S(−n−1) = κ_S(n)`. Theorem P gives: the unique regular-link plaquette ground state `φ_∞`; `⟨n²⟩ ≤ |θ|/(2τ_E)` in every ground state, for every `S`; `|e_S − e_∞| ≤ (80θ²/τ_E + 16|θ|)/S²` once `(S+1)² ≥ 6|θ|/τ_E`; and `‖ιφ_S − φ_∞‖ = O(1/S)`. `H_{p,∞}` is the Fourier transform of the rotor operator `−4τ_E∂_φ² + 2θcos φ` on `L²(S¹)`; nothing below uses that form. The `[check]` of section 8 tests these rates.

## 3. Coupled cubes, and finite SU(2) regions

**The region.** `Γ_2` is the union of the two unit cubes `[0,1]³` and `[1,2]×[0,1]²`, which share the face `{1}×[0,1]²`. Vertices `(a,b,c)`, `a ∈ {0,1,2}`, `b,c ∈ {0,1}` (12). Links: 8 in direction 1, `((a,b,c),(a+1,b,c))`, `a ∈ {0,1}`; 6 in direction 2, `((a,0,c),(a,1,c))`; 6 in direction 3, `((a,b,0),(a,b,1))` (20 in all). `P(Γ_2)` has 11 plaquettes: four `(1,2)`-plaquettes with base `(a,0,c)`, `a ∈ {0,1}`; four `(1,3)`-plaquettes with base `(a,b,0)`, `a ∈ {0,1}`; three `(2,3)`-plaquettes with base `(a,0,0)`, `a ∈ {0,1,2}`. The two cubes lie in different FP tilings (`[0,1]³ ∈ 𝒞`, `[1,2]×[0,1]² ∈ 𝒞+e_1`), and they share four links. In GB1's cube-face model no two tiling cubes share a link (`GB1QL.md` section 1.3), so this coupling is exactly what FP adds. Under Lemma 1.1 the shared face and all other faces enter `H_{Γ_2,s}` with the same coefficient `θ`.

**Lemma 3.1 ((Gen) for two coupled cubes).** Every `c ∈ 𝒵(Γ_2)` is an integer combination of the eleven `∂p`.

*Proof.* Call the four direction-2 and direction-3 links with first coordinate `a` the slice `a`; slice `a` is the boundary 4-cycle of the `(2,3)`-plaquette at `a`. *Step 1.* For the direction-2 link `ℓ = ((a,0,c'),(a,1,c'))` of slice `a ∈ {0,1}`, the `(1,2)`-plaquette `p` with base `(a,0,c')` has `ℓ` as its `ℓ_4`, so `∂p = −1` on `ℓ`; its other links are two direction-1 links and a link of slice `a+1`. Replacing `c` by `c + c_ℓ∂p` makes the value on `ℓ` zero and changes no other link of slice `a`. The same holds for the direction-3 links of slice `a` with the `(1,3)`-plaquettes of base `(a,b,0)`. Clear slice 0, then slice 1; clearing slice 1 does not touch slice 0. The result `c'` differs from `c` by an integer combination of plaquette boundaries, lies in `𝒵(Γ_2)`, and is supported on direction-1 links and slice 2. *Step 2.* At a vertex `(0,b,c'')` only one link of `c'`'s support remains, the direction-1 link to `(1,b,c'')`; zero divergence makes it zero. At `(1,b,c'')` the two direction-1 links remain and the first is zero, so the second is zero. So `c'` lives on the slice-2 4-cycle, and zero divergence on a 4-cycle makes it `n` times the boundary of the `(2,3)`-plaquette at `a = 2`. □

So Theorem P applies to `Γ_2` with `n_p = 11`, `J = 22|θ|`: the regular-link ground state on two coupled cubes is unique with a gap `δ_{Γ_2} > 0`; every finite-`S` ground state has `⟨Σ_ℓE²_ℓ⟩ ≤ 22|θ|/τ_E`; `|e_S − e_∞| ≤ (9680θ²/τ_E + 176|θ|)/S²` once `(S+1)² ≥ 66|θ|/τ_E`; and `‖ιφ_S − φ_∞‖ = O(δ_{Γ_2}^{-1/2}/S)`. The proof of Lemma 3.1 works for any straight column of cubes.

**Proposition 3.2 (SU(2): one regular-link ground state on every finite region).** For every finite region `Γ`, `τ_E > 0` and `θ ∈ R`, the lowest eigenvalue of `H_{Γ,∞}` on `ℋ^{phys}_{Γ,∞}` is simple, and `H_{Γ,∞}` has compact resolvent there.

*Proof.* *Compact resolvent.* `L²(SU(2)^Γ)` is the orthogonal sum of the finite-dimensional spaces `⊗_ℓH_{k_ℓ}`, on which `Σ_ℓE²_ℓ = Σ_ℓ k_ℓ(k_ℓ+2)/4`; each value occurs for finitely many tuples. So `Σ_ℓE²_ℓ` has compact resolvent, and the bounded perturbation `θΣ_pB_p` keeps it (as in Lemma PF). *Positivity improving.* `e^{−tτ_EE²}` is convolution with `k_{tτ_E}` (`GB1E.md` Theorem 2.2), and `k_{tτ_E} > 0` everywhere (`GB1ISO.md` Theorem 2.2: "\(k_t(g)>0\) for every \(t>0\) and \(g\in SU(2)\)"). So `e^{−tH_E}`, `H_E = τ_EΣ_ℓE²_ℓ`, maps every nonnegative nonzero function to a function that is positive everywhere. `V = θΣ_pB_p` is multiplication by the real bounded function `θΣ_p 2tr X_p` (the trace of an `SU(2)` matrix is real). Put `W = ‖V‖_∞ − V ≥ 0`. The Dyson series `e^{−t(H_E − W)} = Σ_{n≥0}D_n(t)`, `D_0(t) = e^{−tH_E}`, `D_n(t) = ∫_0^t e^{−(t−u)H_E}WD_{n−1}(u)du`, converges in norm (`‖D_n(t)‖ ≤ (t‖W‖)^n/n!`) and is the iterated Duhamel formula for the bounded perturbation `−W`. Every `D_n(t)` preserves positivity and `D_0(t)` improves it; so `e^{−tH_{Γ,∞}} = e^{−t‖V‖_∞}e^{−t(H_E − W)}` improves positivity. *Perron-Frobenius on the physical space.* Gauge-invariant functions form a closed subspace stable under `f ↦ |f|`, `f ↦ f̄` and `e^{−tH}`. The lowest eigenvalue `e` of `H|_{phys}` gives the top eigenvalue `λ = e^{−te}` of the positive compact operator `T = e^{−tH}|_{phys}`, and its eigenspace is spanned by real functions. For a real eigenvector `f`, `|Tf| ≤ T|f|` pointwise, so `⟨|f|, T|f|⟩ ≥ |⟨f, Tf⟩| = λ‖f‖²`; hence `|f|` is a top eigenvector and `|f| = λ^{-1}T|f| > 0` almost everywhere. As in Lemma PF, `f = ±|f|`, and two orthogonal real eigenvectors cannot both have a strict constant sign. □

**Theorem C (finite regions, both groups).** Let `Γ` be a finite region: for U(1) assume (Gen); for SU(2) no assumption. Let `s_j → ∞` and let `φ_j` be any unit ground vectors of `H_{Γ,s_j}` on the physical register spaces, with energies `e_{s_j}`. Then `e_{s_j} → e_∞`, `|⟨φ_∞, ιφ_j⟩| → 1`, and `‖ι|φ_j⟩⟨φ_j|ι^* − |φ_∞⟩⟨φ_∞|‖_1 → 0`. For U(1) the rates of Theorem P hold.

*Proof.* Put `J = b_G|θ|n_p`. *Upper limit.* `Π_j = Π^Γ_{s_j}` commutes with the Gauss law and `Π_jφ_∞ → φ_∞`. With `ψ_j = Π_jφ_∞/‖Π_jφ_∞‖`, `⟨ψ_j, τ_EΣE²ψ_j⟩ ≤ τ_E⟨φ_∞,ΣE²φ_∞⟩/‖Π_jφ_∞‖²`, and `⟨ψ_j, B̃^{(s_j)}_pψ_j⟩ → ⟨φ_∞, B_pφ_∞⟩` by Lemma 1.3(b),(e). So `limsup e_{s_j} ≤ e_∞`. *Compactness.* As in Theorem P(b), `⟨φ_j, ΣE²φ_j⟩ ≤ J/τ_E`, so `‖(1 − Π^Γ_M)ιφ_j‖² ≤ |Γ|J/(τ_Ee_G(M+1))` by Lemma 1.3(f). `Π^Γ_M` has finite rank, so every subsequence has a further subsequence with `ιφ_j → φ` in norm, `‖φ‖ = 1`, `φ` physical. *Lower semicontinuity.* For each `M`, `⟨φ, ΣE²Π^Γ_Mφ⟩ = lim_j⟨ιφ_j, ΣE²Π^Γ_Mιφ_j⟩ ≤ liminf_j⟨φ_j,ΣE²φ_j⟩` (a bounded operator, below `ΣE²`); let `M → ∞`. Also `⟨ιφ_j, B̃^{(s_j)}_pιφ_j⟩ → ⟨φ, B_pφ⟩`. So `⟨φ, H_{Γ,∞}φ⟩ ≤ liminf e_{s_j} ≤ e_∞`: `φ` minimizes the form, so it is a ground vector, `φ = cφ_∞` with `|c| = 1` (Theorem P(a) or Proposition 3.2), and `e_{s_j} → e_∞` along the subsequence. Every subsequence has such a further subsequence, so the whole sequence converges. For unit vectors, `‖|u⟩⟨u| − |w⟩⟨w|‖_1 ≤ 2 min_{|c|=1}‖u − cw‖`. □

This settles the brief's first two rungs on finite regions: one U(1) plaquette and two coupled U(1) cubes, with uniqueness and rates; and every finite SU(2) region, with uniqueness and no rate. The torus is next.

## 4. The torus: electric bound, tightness and local limits (U(1) and SU(2))

From here on both groups are treated at once, on tori `Λ_L`, with `b = b_G` (Lemma 1.3(b)).

**Theorem E (electric bound, independent of volume and register size).** Let `L ≥ 3`, `1 ≤ s < ∞`, `τ_E > 0`, `θ ∈ R`, and `ω ∈ 𝔊_{L,s}`. For `i ∈ {1,2,3}` all links `ℓ` in direction `i` have the same `ω(E²_ℓ) =: e_i`, and
```
e_1 + e_2 + e_3 ≤ 3b|θ|/τ_E ,   so   ω(E²_ℓ) ≤ K_E := 3b|θ|/τ_E  for every link ℓ .
```
*Proof.* `ω` is translation invariant, so `ω(E²_ℓ)` depends only on the direction. `ω = Tr(ρ·)` with `ρ` supported in the ground space, so `ω(H_{Λ_L,s}) = e_{Λ_L,s}`. The zero-flux vector is physical and has energy `0` (Lemma 1.3(c)), so `e_{Λ_L,s} ≤ 0`. Hence `τ_E L³(e_1+e_2+e_3) = τ_EΣ_ℓω(E²_ℓ) = e_{Λ_L,s} − θΣ_pω(B̃^{(s)}_p) ≤ |θ| b · 3L³`. □

This is the tree's proposed bound (`GB1_TREE.md` line 574, "\(\omega_s(E_\ell^2)\le C\frac{|\theta|}{\tau_E}\)") with `C = 3b`, for translation-invariant ground states; it is the torus version of the rotor note's eq. (3). For the ground-space average, which is also invariant under the cubic symmetries of `H_{Λ_L,s}`, the same count gives `ω(E²_ℓ) ≤ b|θ|/τ_E`; this is not used. Section 7.1 shows that the bound is a property of the finite-volume selection: the local ground-state inequality alone does not imply it.

**Lemma T (tail tightness).** For `ω ∈ 𝔊_{L,s}`, a finite link set `X`, and `M ≥ 0`: `ω(1 − Π^X_M) ≤ |X| K_E / e_G(M+1)`.

*Proof.* The `Π^ℓ_M` commute, so `1 − ∏_{ℓ∈X}Π^ℓ_M ≤ Σ_{ℓ∈X}(1 − Π^ℓ_M)`; apply Lemma 1.3(f) and Theorem E. □

**Lemma GM (gentle projection; port of `GB1QL.md` Corollary 4.9's proof and the rotor note's eq. (5)).** For a density matrix `ρ` and a projection `Π`, `‖ρ − ΠρΠ‖_1 ≤ 2(Tr ρ(1−Π))^{1/2}`.

*Proof.* For a unit vector `ψ`, `|ψ⟩⟨ψ| − |Πψ⟩⟨Πψ| = |(1−Π)ψ⟩⟨ψ| + |Πψ⟩⟨(1−Π)ψ|`, of trace norm at most `2‖(1−Π)ψ‖`. Write `ρ = Σλ_i|ψ_i⟩⟨ψ_i|` and use `Σλ_i‖(1−Π)ψ_i‖ ≤ (Σλ_i‖(1−Π)ψ_i‖²)^{1/2}`. □

**Lemma K (compactness of tight density matrices).** Let `𝒦'` be a Hilbert space with finite-rank projections `Π_1 ≤ Π_2 ≤ ⋯`. If density matrices `ρ_j` satisfy `sup_j Tr ρ_j(1 − Π_M) ≤ ε(M)` with `ε(M) → 0`, a subsequence converges in trace norm to a density matrix `ρ`, and `Tr ρ(1 − Π_M) ≤ ε(M)`.

*Proof.* Each `Π_Mρ_jΠ_M` lies in a bounded subset of the finite-dimensional space `B(Π_M𝒦')`. A diagonal extraction makes `Π_Mρ_jΠ_M` converge for every `M`. By Lemma GM, `‖ρ_j − ρ_k‖_1 ≤ 4ε(M)^{1/2} + ‖Π_M(ρ_j − ρ_k)Π_M‖_1`, so the subsequence is Cauchy in the trace class, which is complete. Positivity, trace one and the tail bound pass to trace-norm limits. □

**Theorem L (subsequential local limits; any relative rate).** Let `L_j → ∞` and `s_j → ∞` with no relation imposed, and `ω_j ∈ 𝔊_{L_j,s_j}`. There is a subsequence and density matrices `ρ^X` on `𝒦_X`, one for each finite link set `X ⊂ Z³`, with `‖ρ^X_{ω_j} − ρ^X‖_1 → 0` for every `X`. They are consistent, `Tr_{X∖Y}ρ^X = ρ^Y`, so `ω(A) = Tr(ρ^XA)` for `A ∈ B(𝒦_X)` defines a locally normal state `ω` of `𝔄`. Moreover:

(a) `ω` is invariant under the translations of `Z³`;
(b) if all links at a vertex `x` lie in `X`, then `V_x(h)ρ^X = ρ^X` for every gauge element `h`; for every vertex `x`, `ρ^X` commutes with the restriction of `V_x(h)` to `X`;
(c) `Σ_i sup_M ω(E²_{ℓ_i}Π^{ℓ_i}_M) ≤ 3b|θ|/τ_E`, with `ℓ_i` any link in direction `i`;
(d) `ω(1 − Π^X_M) ≤ |X|K_E/e_G(M+1)`.

*Proof.* The finite subsets of the links of `Z³` form a countable family. For each `X`, Lemmas T and K apply to `(ρ^X_{ω_j})_j` with `Π_M = Π^X_M` (finite rank on `𝒦_X`); a diagonal extraction gives convergence for all `X`. Partial traces are trace-norm contractions, so consistency passes to the limit. (a) For fixed `X` and `a ∈ Z³`, once `X` and `X+a` embed in `Λ_{L_j}`, translation invariance of `ω_j` gives `ρ^{X+a}_{ω_j} = T_aρ^X_{ω_j}T_a^*`. (b) `ρ_j` is supported in the physical space, so `V_x(h)ρ_j = ρ_j`; taking the partial trace over the complement of `X` gives the first claim when `V_x(h)` acts inside `X`. In general `V_x(h) = V' ⊗ V''` (inside and outside `X`), and `Tr_{X^c}` of `V'⊗V''ρ_jV'^*⊗V''^*` is `V'ρ^X_{ω_j}V'^*`. (c) For each `M`, `ω(E²_ℓΠ^ℓ_M) = lim_j ω_j(E²_ℓΠ^ℓ_M) ≤ liminf_j ω_j(E²_ℓ)`; sum over the three directions and use Theorem E. (d) Lemma K's tail bound. □

**The order of limits.** (i) *Joint*, with any relative rate: Theorem L. (ii) *Volume first.* For fixed `s`, the same proof (now with a fixed finite register) gives limit points `ω_s` as `L → ∞`, with (a)-(d). As `s → ∞`, the `ω_s` again satisfy Lemma T uniformly, so they have limit points `ω`. Each such `ω` is also a joint limit point: with `d(ω, ω') = Σ_n 2^{−n}‖ρ^{X_n}_ω − ρ^{X_n}_{ω'}‖_1` for an increasing exhausting sequence of boxes `X_n`, choose for each `s` an `L_s` with `d(ω_{L_s,s}, ω_s) < 1/s`. So everything below applies to iterated limits. (iii) *Register first.* At fixed `L`, the s-limit points of `𝔊_{L,s}` are translation-invariant states supported in the ground space of the regular-link torus Hamiltonian `H_{Λ_L,∞}`: this is the proof of Theorem C without its uniqueness step (the upper limit, compactness from `Σ_ℓ⟨E²_ℓ⟩ ≤ 3L³K_E`, and lower semicontinuity), since `Σ_ℓE²_ℓ` has finite-dimensional eigenspaces on the torus too. Theorem E holds for these states with the same proof, and the proofs of sections 5-6 go through with `s_j = ∞` allowed (finite-register estimates pass to fixed-`L` strong limits as in the proof of Theorem D(a)). No claim is made that the three orders, or two subsequences, give the same state.

## 5. Selected ground states through the register limit

Throughout, `ω` and the subsequence `(ω_j)` are as in Theorem L, and `H_j = H_{Λ_{L_j},s_j}`, `e_j` its physical ground energy, `ρ_j` the density matrix of `ω_j`.

### 5.1 The local ground-state inequality

**Lemma TS.** If `ρ_j → ρ` in trace norm, `Y_j → Y` strongly, and `sup_j‖Y_j‖ < ∞`, then `Tr(ρ_jY_j) → Tr(ρY)`.

*Proof.* `|Tr(ρ_jY_j) − Tr(ρY)| ≤ ‖ρ_j − ρ‖_1 sup‖Y_j‖ + |Tr(ρ(Y_j − Y))|`. With `ρ = Σλ_i|u_i⟩⟨u_i|`, `Tr(ρ(Y_j − Y)) = Σλ_i⟨u_i,(Y_j−Y)u_i⟩`; each term tends to zero and is bounded by `2λ_i sup‖Y_j‖ + 2λ_i‖Y‖`; dominated convergence. □

**Theorem G (ground-state inequality in the regular-link limit).** For every `A ∈ 𝒟`,
```
ω( A^* [H^{(∞)}, A] ) ≥ 0 ,
```
with the local commutator of section 1.4. No spectral gap, uniqueness or isolation is used.

*Proof.* Let `A ∈ 𝒟^M_X`. For `j` large, `s_j ≥ M` and `X^+` embeds in `Λ_{L_j}`. Then `A` preserves the register and `a_j = ι^*Aι` is a gauge-invariant register operator, so it maps the physical register space into itself. For a ground vector `ψ` in the support of `ρ_j`, `H_jψ = e_jψ` gives `⟨ψ, a_j^*[H_j, a_j]ψ⟩ = ⟨a_jψ, (H_j − e_j)a_jψ⟩ ≥ 0`; summing, `ω_j(a_j^*[H_j,a_j]) ≥ 0`. All terms of `H_j` other than those listed in section 1.4 commute with `a_j`. On the register, `ι` intertwines `E²_ℓ`, `A` and `B̃^{(s_j)}_p` with `E²_ℓ`, `a_j` and `B^{(s_j)}_p`, and `ρ_j` lives on the register. So `ω_j(a_j^*[H_j,a_j]) = Tr(ρ^{X^+}_{ω_j}Y_j)` with `Y_j = A^*[H^{(s_j)},A]`. By Lemma 1.3(e), `Y_j → Y = A^*[H^{(∞)},A]` strongly, and `‖Y_j‖ ≤ 2τ_E|X|e_G(M)‖A‖² + 8|θ|b|X|‖A‖²`. Lemma TS and Theorem L give `Tr(ρ^{X^+}_{ω_j}Y_j) → ω(Y)`. □

This is the rotor note's eq. (7) for the quantum-link families and the full-plaquette Hamiltonian. The cutoff is removed on the test operator `A`; the state is never projected.

### 5.2 Locality uniform in the register, and real-time correlators

**Lemma LR (Lieb-Robinson for plaquette interactions; finite-dimensional case of `arXiv:0712.3820` section 2, rebuilt).** Let `Λ` be a finite link set (region or torus) with finite-dimensional link spaces `𝒦'_ℓ`, and `H_Y = Σ_{ℓ∈Y}h_ℓ + Σ_{p∈P(Y)}Φ_p` for `Y ⊂ Λ`, with `h_ℓ` self-adjoint on `𝒦'_ℓ` and `Φ_p` self-adjoint on the links of `p`, `‖Φ_p‖ ≤ J`. Put `τ^Y_t(A) = e^{itH_Y}Ae^{−itH_Y}`. Let `A` act on `X ⊂ Y`.

(LR1) If `B` acts on a link set `Z`, then `‖[τ^Y_t(A), B]‖ ≤ 2‖A‖‖B‖ Σ_{n≥0} (2J|t|)^n/n! · N_n`, where `N_0 = 1` if `X ∩ Z ≠ ∅` and `0` otherwise, and for `n ≥ 1`, `N_n` counts chains `p_1, …, p_n` in `P(Y)` with `p_1` meeting `X` and not inside `X`, `p_{k+1} ≠ p_k` sharing a link with `p_k`, and `p_n` meeting `Z`. Always `N_n ≤ 4|X|·12^{n−1}`.

(LR2) If `X_R ⊂ Y ⊂ Λ`, then `‖τ^Λ_t(A) − τ^Y_t(A)‖ ≤ ε_R(t)|X|‖A‖`, with
```
ε_R(t) = (32/3) J|t| (24J|t|)^R e^{24J|t|} / R! .
```
The constants involve only `J` and the lattice: not the `h_ℓ`, not `dim 𝒦'_ℓ`, not `Λ`.

*Proof.* (LR1) Let `V = Σ_{p∈∂X}Φ_p`, `∂X = {p ∈ P(Y) : p meets X, p ⊄ X}`, and `H' = H_Y − V`. `H'` is a sum of a part on the links of `X` and a commuting part on `Y∖X`; it contains **every** on-site term, so `τ'_t = e^{itH'}·e^{−itH'}` maps `B(𝒦'_X)` onto itself isometrically. For `A ∈ B(𝒦'_X)` put `Z_t = τ'_{−t}(A)` and `f(t) = [τ^Y_t(Z_t), B]`. Then `d/dt τ^Y_t(Z_t) = τ^Y_t(i[H_Y − H', Z_t]) = iΣ_{p∈∂X}τ^Y_t([Φ_p, Z_t])`. By the Jacobi identity, `[τ^Y_t([Φ_p,Z_t]), B] = [τ^Y_t(Φ_p), f(t)] − [τ^Y_t(Z_t), [τ^Y_t(Φ_p), B]]`. So `f' = i[Ṽ(t), f] + r(t)` with `Ṽ(t) = Σ_{p∈∂X}τ^Y_t(Φ_p)` self-adjoint and `‖r(t)‖ ≤ 2‖A‖Σ_{p∈∂X}‖[τ^Y_t(Φ_p),B]‖`. With `W' = iṼW`, `W(0) = 1` (unitary), `(W^*fW)' = W^*rW`, so `‖f(t)‖ ≤ ‖[A,B]‖ + ∫_0^{|t|}‖r‖`. Since `τ'_{−t}` is a bijection of the unit ball of `B(𝒦'_X)`, `C(X,t) := sup_{‖A‖≤1, A∈B(𝒦'_X)}‖[τ^Y_t(A),B]‖` obeys `C(X,t) ≤ C(X,0) + 2JΣ_{p∈∂X}∫_0^{|t|}C(p,u)du`, with `C(W,0) ≤ 2‖B‖` if `W` meets `Z` and `0` otherwise. Iterate; `|∂X| ≤ 4|X|` and a plaquette shares a link with 12 others, so the `N`-th remainder is at most `2‖B‖(2J|t|)^N 4|X|12^{N−1}/N! → 0`. (LR2) Duhamel in finite dimension: `τ^Λ_t(A) − τ^Y_t(A) = i∫_0^tτ^Λ_u([H_Λ − H_Y, τ^Y_{t−u}(A)])du`. On-site terms outside `Y` and plaquettes disjoint from `Y` commute with `B(𝒦'_Y)`, so only `p ∈ P(Λ)` meeting `Y` with `p ⊄ Y` remain. Such `p` misses `X_{R−1}` (otherwise `p ⊂ X_R ⊂ Y`). A chain in `P(Y)` starting at `X` has `p_k ⊂ X_k`, so it needs `n ≥ R` plaquettes to share a link with `p`. By (LR1) with `B = Φ_p`, and since each `p_n` shares a link with at most 16 plaquettes `p`, `Σ_p‖[Φ_p, τ^Y_v(A)]‖ ≤ 2J‖A‖Σ_{n≥R}(2J|v|)^n 64|X|12^{n−1}/n!`. Integrate over `v` and use `Σ_{n≥R}x^n/n! ≤ x^Re^x/R!`. □

For the register Hamiltonians, `h_ℓ = τ_EE²_ℓ` and `Φ_p = θB^{(s)}_p`, so `J = b|θ|`, uniformly in `s`, `τ_E` and `L`.

**Lemma D (Duhamel for bounded perturbations).** Let `K` be self-adjoint and `V_1, V_2` bounded self-adjoint. For all `t` and all vectors `φ`,
`e^{it(K+V_1)}φ − e^{it(K+V_2)}φ = i∫_0^t e^{i(t−u)(K+V_1)}(V_1 − V_2)e^{iu(K+V_2)}φ du`.
Consequently, on a finite region `Y` with regular links, `e^{itH_{Y,s}} → e^{itH_{Y,∞}}` strongly as `s → ∞` (with `H_{Y,s} = τ_EΣE² + θΣ_{p∈P(Y)}B̃^{(s)}_p` on `𝒦_Y`), uniformly for `|t| ≤ T`; and if `A_s → A` *-strongly with `sup‖A_s‖ < ∞`, then `e^{itH_{Y,s}}A_se^{−itH_{Y,s}} → τ^{Y,∞}_t(A)` *-strongly.

*Proof.* `K + V_k` is self-adjoint on `D(K)`. For `φ ∈ D(K)`, `u ↦ e^{i(t−u)(K+V_1)}e^{iu(K+V_2)}φ` is differentiable with derivative `−ie^{i(t−u)(K+V_1)}(V_1 − V_2)e^{iu(K+V_2)}φ` (product rule: the right factor stays in `D(K)` and is differentiable; the left factor is a uniformly bounded, strongly continuous family, differentiable on `D(K)`). Integrate from `0` to `t`; both sides are bounded in `φ`, so the identity extends from the dense `D(K)`. For the consequence, take `V_1 = θΣB̃^{(s)}_p`, `V_2 = θΣB_p`: `‖(e^{itH_{Y,s}} − e^{itH_{Y,∞}})φ‖ ≤ ∫_0^{|t|}‖θΣ_p(B̃^{(s)}_p − B_p)e^{iuH_{Y,∞}}φ‖du`, which tends to zero by Lemma 1.3(e) and dominated convergence; the bound increases with `|t|`. Products of uniformly bounded strongly convergent families converge strongly; apply this to the adjoints too. □

**Theorem D (real-time correlators and the regular-link dynamics).** 

(a) For every finite `X` and bounded `A ∈ B(𝒦_X)`, `τ_t(A) := lim_{R→∞} τ^{X_R,∞}_t(A)` exists in norm, with `‖τ_t(A) − τ^{X_R,∞}_t(A)‖ ≤ ε_R(t)|X|‖A‖` and `J = b|θ|`. `τ` extends to a one-parameter group of *-automorphisms of `𝔄` that preserves `𝔄^G`.
(b) Let `A_1, …, A_n ∈ B(𝒦_X)` with `A_k = Π^X_MA_kΠ^X_M`, and `t_1, …, t_n ∈ R`. With `τ^{(j)}` the Heisenberg dynamics of `H_j` applied to `ι^*A_kι`,
`lim_j ω_j(τ^{(j)}_{t_1}(A_1) ⋯ τ^{(j)}_{t_n}(A_n)) = ω(τ_{t_1}(A_1) ⋯ τ_{t_n}(A_n))`.
(c) `ω ∘ τ_t = ω` on `𝔄`.
(d) For `A ∈ 𝒟^M_X`, `‖τ_t(A) − τ_{t'}(A)‖ ≤ c_A|t − t'|` with `c_A = 2τ_E|X|e_G(M)‖A‖ + 8b|θ||X|‖A‖`.

*Proof.* (a) Let `R' > R`, and `P_s` the register projection on `𝒦_{X_{R'}}`; it commutes with `H_{X_{R'},s}` and `H_{X_R,s}`. Put `A_s = Π^X_sAΠ^X_s`. Then `P_s(τ^{X_{R'},s}_t(A_s) − τ^{X_R,s}_t(A_s))P_s` is `ι(·)ι^*` of the corresponding difference of register dynamics, whose norm is at most `ε_R(t)|X|‖A‖` by (LR2) (with `Λ = X_{R'}`). As `s → ∞` it converges strongly to `τ^{X_{R'},∞}_t(A) − τ^{X_R,∞}_t(A)` (Lemma D, `P_s → 1`, `A_s → A` *-strongly), and the norm is lower semicontinuous under strong limits. So `(τ^{X_R,∞}_t(A))_R` is Cauchy, with the stated rate. Each `τ^{X_R,∞}_t` is a *-automorphism of `B(𝒦_{X_R})` that commutes with the restricted gauge action at every vertex (`E²` and `B_p`, `p ⊂ X_R`, do); so `τ_t` is an isometric *-homomorphism on local elements, preserving gauge invariance, and extends to `𝔄`. Group law: for `r < R`, `‖τ^{X_R}_t(τ^{X_R}_{t'}(A)) − τ_t(τ_{t'}(A))‖ ≤ 2ε_r(t')|X|‖A‖ + ε_{R−r}(t)|X_r|‖A‖`, by comparing through `τ^{X_r}_{t'}(A)` (supported in `X_r`, and `X_R ⊃ (X_r)_{R−r}`); let `R → ∞`, then `r → ∞`. `τ_{−t}` inverts `τ_t`. (b) For `j` large, `s_j ≥ M`, `X_R` embeds in `Λ_{L_j}`, and by (LR2) on the torus each `τ^{(j)}_{t_k}(ι^*A_kι)` is within `ε_R(t_k)|X|‖A_k‖` of the register dynamics of `H_{X_R,s_j}`. On the register that is `τ^{X_R,s_j}_{t_k}(A_k)`, which converges *-strongly to `τ^{X_R,∞}_{t_k}(A_k)` (Lemma D). By Lemma TS and Theorem L, `ω_j(∏_kτ^{X_R,s_j}_{t_k}(A_k)) → ω(∏_kτ^{X_R,∞}_{t_k}(A_k))`, which is within `Σ_kε_R(t_k)|X|∏_l‖A_l‖` of `ω(∏_kτ_{t_k}(A_k))` by (a). So the `limsup_j` of the error is at most `2Σ_kε_R(t_k)|X|∏_l‖A_l‖`, for every `R`. (c) `ρ_j` commutes with `H_j`, so `ω_j ∘ τ^{(j)}_t = ω_j`; (b) gives `ω(τ_t(A)) = ω(A)` for `A = Π^X_MAΠ^X_M`. For general `A ∈ B(𝒦_X)`, `A_M = Π^X_MAΠ^X_M → A` strongly, `ω(τ^{X_R,∞}_t(A_M)) → ω(τ^{X_R,∞}_t(A))` by Lemma TS, and (a) is uniform in `M`. (d) On a finite register region, `d/dt τ_t(a) = τ_t(i[H,a])` and `‖[H_{Y,s},a]‖ ≤ c_A` for `a = ι^*Aι` (at most `4|X|` plaquettes meet `X`). Pass to `s = ∞` by Lemma D and lower semicontinuity, then to `R → ∞` by (a). □

Theorem D(b) needs no tightness of time-evolved vectors: Lemma LR localizes each factor uniformly in `s`, and the product of local factors is then tested against the convergent local density matrix. This replaces the polarization step of the rotor note's section 6.

### 5.3 The limit is a ground state of the regular-link dynamics

**Theorem GS.** Let `(π, ℋ_ω, Ω)` be the GNS representation of `ω` restricted to `𝔄^G`. There is a unique strongly continuous unitary group `U_t = e^{itH_ω}` on `ℋ_ω` with `U_tπ(A)Ω = π(τ_t(A))Ω`, and
```
H_ω ≥ 0 ,   H_ωΩ = 0 .
```
So `ω` is a ground state of the regular-link dynamics `τ` in the GNS sense. For `A ∈ 𝒟`, `π(A)Ω` lies in the form domain of `H_ω` and `⟨π(A)Ω, H_ωπ(A)Ω⟩ = ω(A^*[H^{(∞)},A])` is the quantity of Theorem G.

*Proof.* *Density.* For `B ∈ B(𝒦_X)^G`, `B_M = Π^X_MBΠ^X_M ∈ 𝒟` (the flux projections commute with the gauge action), and `‖π(B − B_M)Ω‖² = Tr(ρ^X(B−B_M)^*(B−B_M)) = Σλ_i‖(B−B_M)u_i‖² → 0` by dominated convergence. So `π(𝒟)Ω` is dense in `ℋ_ω`. *The group.* `ω∘τ_t = ω` (Theorem D(c)) makes `π(A)Ω ↦ π(τ_t(A))Ω` isometric and well defined; it extends to unitaries with `U_tU_{t'} = U_{t+t'}` and `U_tπ(B)U_t^* = π(τ_t(B))`. By Theorem D(d), `t ↦ U_tπ(A)Ω` is Lipschitz for `A ∈ 𝒟`; with density and `‖U_t‖ = 1`, `U` is strongly continuous. Stone's theorem gives `H_ω`, and `U_tΩ = Ω` gives `H_ωΩ = 0`. *Positivity.* Fix `A ∈ 𝒟^M_X` and let `μ_A` be the spectral measure of `H_ω` in the vector `π(A)Ω`, so `F(t) := ∫e^{itλ}dμ_A(λ) = ⟨π(A)Ω, U_tπ(A)Ω⟩ = ω(A^*τ_t(A))`. For `j` large, with `a = ι^*Aι` and `ρ_j = Σ_iλ_i|ψ_i⟩⟨ψ_i|` (ground vectors), `F_j(t) := ω_j(a^*τ^{(j)}_t(a)) = Σ_iλ_i⟨aψ_i, e^{it(H_j − e_j)}aψ_i⟩ = ∫e^{itλ}dμ_j(λ)`, where `μ_j` is a positive measure of mass `≤ ‖A‖²` supported in `[0,∞)`: `aψ_i` is physical and `H_j − e_j ≥ 0` there. Theorem D(b) with `n = 2` gives `F_j(t) → F(t)` for every `t`, and `|F_j| ≤ ‖A‖²`. Let `f ≥ 0` be smooth with compact support in `(−∞, 0)` and `f̂(t) = ∫f(λ)e^{−itλ}dλ`, a Schwartz function. Fourier inversion and Fubini give, for every finite positive measure `μ`, `∫f dμ = (2π)^{−1}∫f̂(t)(∫e^{itλ}dμ(λ))dt`. Hence `∫f dμ_A = (2π)^{−1}∫f̂F = lim_j(2π)^{−1}∫f̂F_j = lim_j∫f dμ_j = 0` by dominated convergence. Such `f` increase to the indicator of `(−∞,0)`, so `μ_A((−∞,0)) = 0`. The spectral projection `1_{(−∞,0)}(H_ω)` therefore vanishes on the dense set `π(𝒟)Ω`, hence is zero. *The form identity.* For `A ∈ 𝒟`, `‖τ_t(A) − A − t·i[H^{(∞)},A]‖ ≤ c'_At²` with `c'_A` from Theorem D(d) applied to the core element `[H^{(∞)},A]` (finite-register region bounds, then the two limits); so `π(A)Ω ∈ D(H_ω)` with `H_ωπ(A)Ω = π([H^{(∞)},A])Ω`, and the identity follows. □

This is the spectral form of the ground-state condition, proved as in the rotor note's section 6, here through Theorem D(b) for the quantum-link families.

## 6. Bounded Euclidean insertions

**Theorem EU (normalized Euclidean correlators).** Let `A_1, …, A_n ∈ 𝒟` and `u_1, …, u_{n−1} ≥ 0`. For `j` large put `a_k = ι^*A_kι` and
```
G_j(u) = ω_j( a_1 e^{−u_1(H_j − e_j)} a_2 e^{−u_2(H_j − e_j)} ⋯ e^{−u_{n−1}(H_j − e_j)} a_n ) .
```
Then `|G_j(u)| ≤ ∏_k‖A_k‖`, and
```
lim_j G_j(u) = G(u) := ⟨π(A_1^*)Ω, e^{−u_1H_ω} π(A_2) e^{−u_2H_ω} ⋯ e^{−u_{n−1}H_ω} π(A_n)Ω⟩ .
```
The insertions are normalized by the ground energy, so each `e^{−u(H_j−e_j)}` is a contraction on the physical space; the limit uses the same positive generator `H_ω` as Theorem GS.

*Proof.* Products of elements of `𝒟` lie in `𝒟` (section 1.4), so factors with `u_k = 0` can be merged; assume every `u_k > 0`. Fix a smooth `χ` with `χ = 1` on `[−1/2, ∞)` and `χ = 0` on `(−∞, −1]`, and put `g_k(λ) = e^{−u_kλ}χ(λ)`, a Schwartz function equal to `e^{−u_kλ}` on `[0,∞)`. For a self-adjoint `K` and vectors `v, w`, Fourier inversion and Fubini give `⟨v, g(K)w⟩ = (2π)^{−1}∫ĝ(t)⟨v, e^{itK}w⟩dt` for every Schwartz `g`. The gauge-invariant `a_k` keep vectors in the physical space, where `H_j − e_j ≥ 0`; so `g_k(H_j − e_j) = e^{−u_k(H_j−e_j)}` there. Applying the formula once per factor (Fubini on `R^{n−1}`, the integrand bounded by `∏_k|ĝ_k(t_k)|∏_k‖A_k‖`):
```
G_j(u) = (2π)^{1−n} ∫_{R^{n−1}} ∏_k ĝ_k(t_k) · F_j(t) dt,
F_j(t) = ω_j( a_1 e^{it_1(H_j−e_j)} a_2 ⋯ e^{it_{n−1}(H_j−e_j)} a_n ) = ω_j( a_1 τ^{(j)}_{T_1}(a_2) τ^{(j)}_{T_2}(a_3) ⋯ τ^{(j)}_{T_{n−1}}(a_n) ),
```
with `T_k = t_1 + ⋯ + t_k`; the second form uses `e^{iTH_j}ψ = e^{iTe_j}ψ` for ground vectors. By Theorem D(b), `F_j(t) → F(t) := ω(A_1τ_{T_1}(A_2)⋯τ_{T_{n−1}}(A_n))` for every `t`, with `|F_j| ≤ ∏‖A_k‖`. Dominated convergence gives `G_j(u) → (2π)^{1−n}∫∏ĝ_k(t_k)F(t)dt`. In the GNS space, `F(t) = ⟨π(A_1^*)Ω, U_{t_1}π(A_2)U_{t_2}⋯π(A_n)Ω⟩` (use `U_tπ(B)U_t^* = π(τ_t(B))` and `U_tΩ = Ω`). The same Fourier formula with `K = H_ω`, and `g_k(H_ω) = e^{−u_kH_ω}` because `H_ω ≥ 0` (Theorem GS), identify the limit with `G(u)`. The bound `|G_j| ≤ ∏‖A_k‖` holds because each `a_k` has norm `≤ ‖A_k‖` and each insertion is a contraction on the physical space. □

**Properties of the limit functions.** (i) *Euclidean reflection positivity in time:* for `B_1, …, B_m ∈ 𝒟`, `u_b ≥ 0` and `c ∈ C^m`, `Σ_{a,b}\bar c_ac_b⟨π(B_a)Ω, e^{−(u_a+u_b)H_ω}π(B_b)Ω⟩ = ‖Σ_bc_be^{−u_bH_ω}π(B_b)Ω‖² ≥ 0`. (ii) *Time-translation structure:* `G` depends only on the gaps `u_k`, and `u ↦ G(u)` is continuous on `[0,∞)^{n−1}` and analytic in each `u_k > 0` (spectral calculus of `H_ω ≥ 0`). (iii) *Uniformity:* `|G| ≤ ∏‖A_k‖`, for all volumes and registers. These are the structures that an Osterwalder-Schrader reconstruction returns; here they are obtained directly from the Hamiltonian side. Whether `G` comes from a gauge-invariant Euclidean *measure* on group variables is node H's question (`GB1_TREE.md` line 610, "One normalized four-dimensional gauge-invariant measure"), and is not addressed here.

**What the limit does not give.** It does not identify `ω` with the VC1 state, with a tick-invariant state, or with a state of a fixed register (the family quantifier stays: `GB1_TREE.md` line 102, "needs an owner-approved change of quantifiers before it establishes the root for one fixed law"). It gives no rate in volume or register at fixed observable, and no uniqueness on the torus: different subsequences, and different choices `ω_j ∈ 𝔊`, may give different limits.

## 7. Candidate readings and the four tests

### 7.1 The electric bound comes from the selection, not from the local inequality

**Proposition BF (background-field local ground states).** Take U(1), regular links on `Z³`, `θ = 0`, `τ_E > 0`. For `n ∈ Z` let `c^{(n)}` be the flow equal to `n` on every direction-1 link and `0` elsewhere, and `ω_n` the product state `⊗_ℓ|c^{(n)}_ℓ⟩⟨c^{(n)}_ℓ|` on `𝔄`. Then `ω_n` is locally normal, translation invariant and satisfies the Gauss law at every vertex; `ω_n(A^*[H^{(∞)}, A]) ≥ 0` for every `A ∈ 𝒟`; and `ω_n(E²_ℓ) = n²` on direction-1 links.

*Proof.* `c^{(n)}` has zero divergence (at each vertex one direction-1 link enters with `n` and one leaves with `n`). Let `A ∈ 𝒟^M_X`, and let `Y ⊃ X` be a finite box containing the star of every vertex that touches `X`. Put `φ = ⊗_{ℓ∈Y}|c^{(n)}_ℓ⟩`. At each vertex `x` touching `X`, `V_x(α)` restricted to `Y` fixes `φ` and commutes with `A`, so it fixes `Aφ = Σ_c a_c|c⟩`, where `c` differs from `c^{(n)}` only on `X`. Hence `a_c ≠ 0` only if `δ = c − c^{(n)}` has zero divergence at every vertex, that is, `δ` is a finitely supported integer flow with zero divergence. With `Q_X = Σ_{ℓ∈X}E²_ℓ` and `θ = 0`, `ω_n(A^*[H^{(∞)},A]) = τ_E Σ_c|a_c|²(Q_X(c) − Q_X(c^{(n)})) = τ_E Σ_c|a_c|²(2nΣ_{ℓ∈X, dir 1}δ_ℓ + Σ_ℓδ_ℓ²)`. For each `a ∈ Z`, summing the divergence of `δ` over the half-space `{x_1 ≤ a}` gives zero; interior links cancel, so the total of `δ` on the direction-1 links crossing the plane `x_1 = a + 1/2` is zero. Summing over `a`, `Σ_{dir 1}δ_ℓ = 0`. So the expression is `τ_EΣ_c|a_c|²Σ_ℓδ_ℓ² ≥ 0`. □

At `θ = 0`, Theorem E gives `ω(E²_ℓ) ≤ 0` for every selected limit, which excludes `ω_n`, `n ≠ 0`. So no proof of a bound like Theorem E can use only the local ground-state inequality: it must use the finite-volume minimization, as Theorem E does through the zero-flux trial on the torus. This answers the first named attack ("energy-tail control") in the direction the brief needs: tail control is available for the selected states, and only for a selection that sees the global energy.

### 7.2 Four tests

The tests (`GB1_TREE.md` lines 680-683): (1) does the specification state or fix a part's target; (2) is it open-ended; (3) does it settle a downstream question by premise; (4) does it add structure its own reasons do not need. P = concern absent, F = fails, C = a condition the owner must decide. Nothing below is adopted.

| Candidate | Exact text | 1 | 2 | 3 | 4 | Condition before use |
|---|---|---|---|---|---|---|
| **H-FP** (the cube-coupling Hamiltonian of node R) | "For node R, the family is `H_{Λ_L,s} = τ_EΣ_ℓE²_ℓ + θΣ_pB̃^{(s)}_p` with all plaquettes, on the registers of `GB1.md` Theorem 5.2 (U(1), integer `S`) or `GB1QL.md` section 1.2 (SU(2)), with `τ_E > 0` and `θ` fixed across the family." | P | P | C | P | It is R-SUM applied to FP (Lemma 1.1), so it inherits R-SUM's condition (`GB1_GEN_OWNER_CHECK.md` line 77: "**C.** Supplies the energy reading and Euclidean correlations"). It does not supply node C's finite-depth tick: `LW2M_DRAFT.md` shows the FP word is not cell covariant. |
| **S-GS** (the state prescription of Definition 1.5) | "For node R, the selected states at finite `L, s` are the translation-invariant states supported in the physical ground space of `H_{Λ_L,s}`; the canonical member is the ground-space average." | P | P | C | P | It fixes no target and is closed (determined by `H` and the translations); the ground-space average is the zero-temperature limit of the physical Gibbs states. Test 3 is C because selecting Hamiltonian ground states, rather than states of the tick, is node V's question; the theorems here use S-GS only as a hypothesis and settle nothing about VC1. Test 4: translation averaging uses a symmetry `H` already has; no constant is added. |

The tree's row "Unspecified 'large register' … C F P C" (`GB1_TREE.md` line 698) is repaired by H-FP's fixed register families. Using a family result for the root still needs the owner's change of quantifiers (line 102); none is proposed here.

## 8. Checks

**[check]** `/tmp/toe-GB1R/check_gb1r.py`, run with `python3 -I` at 55 percent free memory; 15 s, peak memory footprint 287 MB; output `/tmp/toe-GB1R/out.txt`. Floating point, `τ_E = 1`, `θ < 0`. The largest object is a sparse `141217 × 141217` matrix (two coupled cubes at cutoff 2, about 3·10⁶ nonzeros), handled by `eigsh` for one eigenvalue; dense diagonalization only up to dimension 399. The regular-link reference uses a projection cutoff, not `S → ∞`. Guidance only; nothing here proves anything.

| Region, `θ` | `S` | `e_S − e_ref` | `S²|e_S − e_ref|` | `1 − |⟨φ_ref, φ_S⟩|²` | `⟨ΣE²⟩` (bound `2|θ|n_p`) |
|---|---|---|---|---|---|
| plaquette, `−0.5` | 8 / 32 / 64 | `4.76e-5` / `3.38e-6` / `8.60e-7` | 0.0030 / 0.0035 / 0.0035 | `< 1e-4` | `4⟨n²⟩ = 0.116` (1.0) |
| plaquette, `−2.0` | 8 / 32 / 64 | `5.51e-3` / `3.92e-4` / `9.99e-5` | 0.352 / 0.402 / 0.409 | `S²(1−ov²)` 0.0008 / 0.0001 / `< 1e-4` | 0.935 (4.0) |
| two plaquettes, `−2.0` | 4 / 8 / 16 | `5.87e-2` / `1.78e-2` / `4.83e-3` | 0.939 / 1.138 / 1.237 | `4.9e-4` / `4.3e-5` / `3.1e-6` | 1.878 (8.0) |
| two cubes, `−0.3` | 1 / 2 | `1.11e-2` / `4.14e-3` | 0.011 / 0.017 | `1.2e-3` / `6.4e-5` | 0.476 (6.6) |

The plaquette references use cutoff 80, the two-plaquette references cutoff 30, the two-cube reference only cutoff 2 (so its rows test the bound, not the rate). Readings: `S²|e_S − e_∞|` levels off far below `C_1` (28 and 352 for the plaquette), consistent with the `O(S^{−2})` energy rate of Theorem P; the overlap defect falls faster than the `O(S^{−2})` that Theorem P(c) guarantees (it is near `S^{−4}` here), so the vector bound is not sharp; every ground state obeys the electric bound with a wide margin.

## FINISH

**Stopping point reached: a local convergence theorem** (the first stopping point of Lane brief 2, `GB1_TREE.md` line 788), for the specified family H-FP with the state prescription S-GS, both candidates and not adopted (section 7.2). Pass 1; not distilled, not refereed.

**Proved here.**
1. Lemma 1.1: the R-SUM Hamiltonian of the FP word is the full-plaquette Hamiltonian `H_{Λ_L,s}`, at every register size; no commutation is needed.
2. Theorem P (U(1) regions with (Gen)): a unique regular-link ground state with a gap; `⟨ΣE²⟩ ≤ 2|θ|n_p/τ_E` in every ground state at every `S`; `|e_S − e_∞| ≤ C_1/S²`; `1 − |⟨φ_∞,ιφ_S⟩|² ≤ 2C_1/(δ_ΓS²)`; simple finite-`S` ground state for large `S`. It covers one plaquette and, by Lemma 3.1, two coupled cubes.
3. Proposition 3.2 and Theorem C: on every finite SU(2) region the regular-link ground state is unique, and every sequence of finite-register ground states converges to it in norm (no rate).
4. Theorem E: on tori, every translation-invariant physical ground state obeys `e_1 + e_2 + e_3 ≤ 3b|θ|/τ_E` (`b = 2` for U(1), `4` for SU(2)), uniformly in volume and register size; Lemma T gives tail tightness.
5. Theorem L: along any sequence `L_j, s_j → ∞`, with any relative rate, the local density matrices have trace-norm convergent subsequences; the limit is locally normal, translation invariant and satisfies the Gauss law. Volume-first and register-first orders are covered (section 4).
6. Theorem G: the limit satisfies `ω(A^*[H^{(∞)},A]) ≥ 0` on the flux-bounded gauge-invariant core, with no gap.
7. Lemma LR: a Lieb-Robinson bound whose constants see only `b|θ|`, uniformly in the register and the electric coupling. Theorem D: the regular-link infinite-volume dynamics exists as a group of automorphisms of `𝔄`, every multi-time real-time correlator of flux-bounded local operators converges, and the limit is invariant.
8. Theorem GS: the limit is a ground state in the GNS sense, `H_ω ≥ 0`.
9. Theorem EU: every normalized Euclidean correlator `ω_j(a_1e^{−u_1(H_j−e_j)}a_2⋯a_n)` converges to `⟨π(A_1^*)Ω, e^{−u_1H_ω}π(A_2)⋯π(A_n)Ω⟩`, bounded by `∏‖A_k‖`, reflection positive in Euclidean time.

**Counterexamples.** Proposition BF: at `θ = 0`, background-field product states satisfy the local ground-state inequality with `ω(E²_ℓ) = n²`. So the local inequality alone does not give the electric bound; the bound is a property of the finite-volume selection. This refutes no proposed statement of the tree; it fixes where the bound comes from.

**Open by name.** GB1R-UNIQ: whether the torus limit is independent of the subsequence and of the choice in `𝔊`. GB1R-RATE: a volume-uniform rate at fixed local observable. GB1R-V: whether S-GS's state is the state of any tick or of VC1 (node V). Node C's finite-depth realisation of FP is untouched.

**What changes downstream.**
- Node R: its first deliverable exists for the family H-FP under S-GS, on both rungs U(1) and SU(2), subsequential on tori, unique with rates on the finite U(1) regions of the brief, unique on finite SU(2) regions.
- Node H can take the limit functions of Theorem EU as Euclidean correlations of one selected state, with a positive generator and time-reflection positivity. They are Hamiltonian correlations, not a Euclidean measure on group variables; H's measure, action-class and isotropy obligations stand.
- Node V: S-GS is a candidate prescription (P P C P), to be put to the owner only with V's tick question.
- RATE, GA2 and T0: nothing supplied; the family quantifier stays (`GB1_TREE.md` line 102).
- R-SUM: Lemma 1.1 shows that under R-SUM the cube coupling FP needs no ordering, so `LW2M_DRAFT.md`'s covariance failure of the FP word does not reach the Hamiltonian branch; it stays a failure of the tick.
