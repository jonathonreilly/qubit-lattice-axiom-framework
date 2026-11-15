lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# ZM1-I1[a]: the zoom with the owner's comparison class (p = 2), pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under the method of PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-ZM1I1A/`. A check guides and never proves. Nothing here is a verdict.

**Source revisions read.**

| Ref | Commit |
|---|---|
| branch `claude/toe-assembly`, checkout named in the lane brief | `31ef08a1e` |
| the same branch later in this session (adds `CG16B.md`, `CG16D.md` only; no file read here changed) | `59d3886d9` |

Files read, by line, in this folder (last-change commit; SHA-256 prefix): `prior/ZM1I1A.md` all (`a97593f4e`; `ecaf9d607feaff57`); `TOE_ASSEMBLY.md` lines 225-260, with section 3.8 at lines 239-246 (`36d5dd136`; `6fda41c203ac95b5`); `ZM1.md` lines 1-120 and 300-398, with Definition Z (lines 51-58), Definition G (lines 70-72), Theorems Z0, Z1 (statement and Step 1), Z3, Z3′, Z4, the precise ZM1-I1, Lemma R-GI and Attacks 1-3 (`36d5dd136`; `19bb781d7923b0a6`); `ZM1_OBS.md` lines 1-232 and 270-358, with sections 1-3, 5.1-5.3, Lemma ER, Lemma P1 and Proposition T (`36d5dd136`; `8d1e40accea00ef0`); `VC1_5.md` lines 1-241 (`727ad9884`; `b429d8d31d9719d8`); `VC1_5U_ODD.md` lines 1-16 (status) and 115-131 (Theorems 4.3, 5.1, 5.2) (`c4e7cfa88`; `b13e1055415b5a70`); `LW1_5.md` lines 60-104, 137, 333 (`727ad9884`; `bdd5159f8585030b`); `GA1_5.md` lines 1-32, 166-194 and the Proposition S-odd lines 316-339 (`913ef70a5`; `2ba3527fbb3819f7`); `GA15PHI.md` lines 1-12 (`913ef70a5`; `8822fabfa5893d58`); `LZ1I.md` lines 1-14, 29-102 (`7da1a4174`; `5208acb28cb3d64c`); `GA2_Y2.md` lines 37-69 (`727ad9884`; `57ced3f3b19c28f8`). Other branches: none was needed. The digest's paths on main and on the consolidation PRs are cited from the digest, with its quotes, and are not load-bearing here.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". Definitions Z and G and the owner's text ZM1-I1[a] are read plainly. The main result below says that, read plainly, they cannot all hold at once for `L ≥ 2`. Section 8 offers changes for the owner to consider. None is adopted.

**Working set used, by name.** PS-1c (locality and covariance of an update, through Definition Z), PS-5 (five modes per site) and PS-6r (finite link registers), through the two five-mode laws of `LW1_5.md` lines 87-100. PS-7r only through its sentence "the vacuum is the state VC1 builds". Owner decisions used as the statement of the problem: ZM1-I1[a] with `p = 2` (`TOE_ASSEMBLY.md` section 3.8) and GA1-P-NN = NN-a (section 3.7, only to name the admissible updates). Frozen results used by name: `ZM1.md` Definitions Z and G, Theorem Z4, Lemma R-GI; `ZM1_OBS.md` Theorems 1-3, Lemma ER; `VC1_5.md` Theorems 2.1, 4.2, 5.2, 5.5 and Proposition R2; `GA1_5.md` Theorem 6.3 and Proposition S-odd; `LZ1I.md` Theorems 6-8.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: a tracial state on a full matrix algebra is the normalized trace; the CAR algebra on finitely many modes is a full matrix algebra; a unital *-homomorphism preserves exponentials of self-adjoint elements; the variance of a hypergeometric count; the edge boundary of a finite set in `Z^3` has at least six edges. Literature is in section 2. No literature result is a step of any proof here.

**Scratch check.** `/tmp/toe-ZM1I1A/check.py`, output `out.txt` (under one second, a few MB, run after `memory_pressure` reported 55 percent free). It enumerates one link register and evaluates the trace covariances used in sections 4 and 5. It guides and never proves.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 243, the owner's text: "**ZM1-I1[a], the zoom's comparison class (owner 2026-11-06).** "The following specifies the comparison required in the open statement ZM1-I1[O]. It asserts no existence result. Retain the specified VC1 fine vacuum and the admissible fine updates of ZM1-I1. Retain \(L\ge2\), the Definition-Z map \(\Phi:\mathfrak A_1\to\mathfrak A\), (Z-a), (Z-b), (G1), (G2), and singleton embedding sets. Retain a coarse law \(\alpha_1\) of the stated form and an \(\alpha_1\)-invariant state \(\omega_1\). One coarse tick is \(L\) fine ticks. [...] Require \(|F_0^T-F_1^T|\le C_{R_0}(r^{-p}+tr^{-p-1})M(r,t)\), with \(p=2\). A zero envelope gives zero values on both sides. No separate one-point matching is imposed.""

`ZM1.md` line 363, the precise form that the owner's text retains: "Let `ω_0` be a vacuum that VC1 supplies for `L5-U[m]` (base tick, or with a plaquette class that GA1-P-5 supplies). There exist `L >= 2`, `p >= 1`, `C, κ_0 > 0`, a block map `Φ` of factor `L` (Definition Z) satisfying (Z-a), (Z-b) and (G1)–(G2) with `|S_X| = 1` for every coarse site `X`, a coarse law `α_1` of the `L5-U` form, and an `α_1`-invariant state `ω_1` of `A_1`, with the following property."

`ZM1.md` line 53, Definition Z: "A **block map of factor `L`** is a unital injective graded *-homomorphism `Phi : A_1 -> A` with:". Line 54: "(Z-a) *locality*: for `B in B_u`, `Phi(B)` is a norm limit of elements supported within distance `R` of the block `beta_u`, with error at most `C e^{-R/xi} ||B||` for constants `C, xi`".

`ZM1.md` lines 70-71, Definition G: "Let the coarse law be of the same type, with coarse Gauss generators `G^{(1),T}_u`. A block map `Phi` is **gauge covariant with embedding sets** `S_u` (nonempty, pairwise disjoint finite sets of fine sites) if: (G1) *Gauss law to Gauss law:* `Phi(G^{(1),T}_u) = sum_{x in S_u} G^T_x` for every coarse site `u` and every `T`".

`LW1_5.md` line 96, the `L5-U` Gauss generator: "\(\mathcal G_x^T=c_x^\dagger T c_x+\sum_{\ell\ni x}r_{\ell,x}^\dagger T r_{\ell,x}\)", line 100: "Here \(T\) is Hermitian, \(p_{\ell,x}=r_{\ell,x}^\dagger r_{\ell,x}\)". Line 94: "Each link carries \(\Lambda^m\mathbb C^{10}\), \(1\le m\le9\), with five rishon modes at each end."

The lane brief: decide ZM1-I1[a] with `p = 2`. Either construct the data for some vacuum and some admissible update, or prove that no such data exist for a named class, naming the step.

## 0.1 Outcome in one paragraph

**Counterexample: no such data exist, on either five-mode law, for every vacuum, every admissible update and every `L ≥ 2`.** The failing step is the block map itself, before any state or dynamics enters. **Theorem T (section 4).** Let `Φ` be a unital *-homomorphism from the coarse `L5-U[m_1]` algebra into the fine `L5-U[m]` algebra, with (G1) at `T = 1` and singleton sets `S_X = {x_X}`. Then the representatives of any two coarse neighbours are fine nearest neighbours. The reason is the trace. Every coarse local algebra is a full matrix algebra, so `Φ` preserves the normalized trace on it. Under the coarse trace the `U(1)` Gauss charges of two coarse neighbours are anticorrelated through their shared link, with covariance `−m_1(10−m_1)/36`. Under the fine trace the charges of two fine sites that share no link are independent. **Theorem T′.** With disjoint sets and (Z-a), the representative map is then a bijection of site sets that moves each site a bounded distance, which forces `L = 1`. **Theorem O (section 5).** The same holds on `L5-O[S_+]`, with the Cartan torus element of `Spin(10)` at angle `π/2` in place of the `U(1)` charge (trace covariance `−2^{−35}`). So ZM1-I1[a] has no data for any `p`; neither has any class ZM1-I1[O], nor the original ZM1-I1. Two strengthenings: on `L5-U`, (G1) with any finite sets forces `|S_X| = 1` (Proposition V); and (G1) for the `SU(5)` part alone gives the same no-go (Proposition Z5). **First tests (section 6).** Empty- or full-matter product vacua with the base tick (`VC1_5.md` Theorem 5.2 at `t = ±∞`, Theorem 5.5) are trivial for the criterion under any finite-range block map: every invariant truncated value vanishes beyond a finite range at every tick (Lemma DK, Proposition 6.0). The non-factor witness of `VC1_5.md` R2 is not trivial: it has a constant tail (Proposition R2′). The swap bands of `GA1_5.md` and the two-band vacua of `LZ1I.md` are not trivial: an exact band must be matched exactly. All of them fail at Theorem T′. **What the no-go does not touch (section 7).** Gauge covariance read at the level of automorphisms instead of generators, non-unital maps, measure-level maps and infinite link registers. Section 8 offers three changes of specification to the owner, four-tested. None is adopted. **New open statement:** G1-EQ (section 8.1).

## 1. Prior work used

Each item names the result, its path and what this file does with it. "Ported" means quoted and used as proved there. "Extended" means a new statement here that contains the old one or sharpens it.

| Prior result | Path | Use here |
|---|---|---|
| Definitions Z and G, (Z-a), (G1), (G2) | `ZM1.md` lines 51-58, 70-72 | The hypotheses of Theorems T, T′, O. Read plainly; section 3. |
| Theorem Z4: "`D_u >= n_0 \|S_u\| + 1`" | `ZM1.md` line 311 | Extended on `L5-U` by Proposition V: (G1) with any finite sets forces `\|S_X\| = 1`. Z4 is the nearest earlier constraint on embedding sets. |
| Theorems Z3, Z3′ and Attacks 1-2 on ZM1-I1 | `ZM1.md` lines 319-361, 382-384 | Not used. They fail at the coarse matter field. Theorem T fails earlier, at the coarse link and Gauss sector, for every field. Section 7.5 compares. |
| The example `Ψ = W c_{x_u} W^*` | `ZM1.md` line 359 | Consistent with Theorem T: it is one field, not a block map of the whole coarse algebra. |
| Lemma R-GI and its consequence | `ZM1.md` lines 370-376 | Not needed for the no-go. Quoted in section 8.1: its proof uses (G1) only through a conjugation step that (G1-eq) keeps. |
| Theorem 1 (a unital homomorphism "preserves exponentials of self-adjoint elements") | `ZM1_OBS.md` line 56 | Ported. Used in Theorem O and Proposition Z5. |
| Theorems 2-3 (diagonal gauge projection; `Φ(𝔄₁^G)⊆𝔄^G`) | `ZM1_OBS.md` lines 60-70 | Ported in section 6 and in the reading G1-EQ (section 8.1). |
| Lemma ER and its consequence (exact asymptotic matching of every nonzero invariant tail) | `ZM1_OBS.md` lines 284-292 | Ported in section 6 to classify the first tests. |
| Lemma P1 (the existential exponent is `p = 1`) | `ZM1_OBS.md` lines 300-304 | Theorem T′ does not depend on `p`. |
| VC1 witnesses: Theorems 4.2, 5.2, 5.5, Proposition R2, the R4 ice limits; Amendment 1 (ICE-T) | `VC1_5.md` lines 80-140, 196-240; `VC1_5U_ODD.md` via `VC1_5.md` line 7 | The vacua tested in section 6. |
| Theorem 6.1 (R): on empty matter, `L5-U` invariant dynamics reduce to link dynamics | `GA1_5.md` lines 150-158 | Ported and extended in section 6 (Lemma DK): with the base tick the reduced dynamics is one product of single-link unitaries, so every invariant truncated value vanishes beyond a finite range. |
| Theorem 6.3 and Proposition S-odd (the neutral swap band) | `GA1_5.md` lines 166-182, 316-339 | Section 6.2. |
| Theorems 6-8 (two exact neutral bands of different speeds) | `LZ1I.md` lines 76-102 | Section 6.2. |
| Theorem 2.1 (N) and Corollary 2.2: "A finite register with a nontrivial infinitesimal link representation has no invertible covariant link" | `GA2_Y2.md` lines 37-41 | The closest relative of Theorem T. Both come from the finiteness of the registers (PS-6r). N is about one link operator. T is about the trace of the whole embedded algebra. Neither implies the other; section 7.5. |

**From the digest `prior/ZM1I1A.md`, with its paths and quotes.**
- The level-matched polar map of #9928 is "an isometry in a 2+1D Z_3 toy" (`G:287,295,311,11` in the digest's shorthand). An isometry gives a non-unital map, so it lies outside Definition Z and outside Theorem T. Section 7.3 says why non-unital maps escape.
- The dyadic even refinement on main supplies "support-preserving even embeddings" of a free chain with no gauge field. Theorem T needs a Gauss law with a shared link, so it says nothing there.
- The constrained-fiber series on main is measure-level (action-space). It lies outside Definition Z ("This excludes measure-level (Euclidean) block maps", `ZM1.md` line 65). Theorem T does not touch it.
- The finite-region Peter–Weyl approximation on main works with group-valued links before truncation, which have no normalized trace. Section 7.4 explains why such links escape Theorem T.
- The digest's failed attempts (minimal coupling, coherent links, conserved projections, momentum support, vacuum matching, raw contraction, exact flow compatibility, finite diagnostics) are not repeated. Theorem T is a new step: it uses the trace of the coarse algebra, which none of them uses.

**Prior work the digest missed.** `GA1_5.md` Theorem 6.1 (R), the empty-matter reduction, bears directly on this lane's first tests; section 6 ports it. The digest records no trace argument and no adjacency constraint on representative sites in the searched material. Within this folder, `ZM1.md` Theorem Z4 is the nearest constraint on embedding sets.

## 2. Literature read

Searched on 2026-11-07: operator-algebraic renormalisation and refinement maps for lattice gauge theory; quantum-cellular-automaton and fermionic-automaton renormalisation; entanglement renormalisation of gauge and topological models; quantum link models and D-theory; rigorous block-spin RG (Balaban, Dimock, Gawedzki–Kupiainen, Brydges–Federbush); decay of truncated correlations; and, in an extended search, "Gauss-law preserving coarse graining of quantum link models with finite link spaces". The last search found no paper that states a block map of a quantum link model with an exact Gauss embedding, and no trace obstruction. That is a search result, not a proof of absence. No item below is a step of any proof here. Each is credited and placed relative to Theorem T.

| Work | arXiv / reference | What was fetched and read | Bearing |
|---|---|---|---|
| A. Brothier, A. Stottmeister, "Operator-algebraic construction of gauge theories and Jones' actions of Thompson's groups" | arXiv:1901.04940; CMP 376 (2020) 841-891 | Abstract page and the ar5iv text: Section 2.1, eq. (2.1) "R(b)=Ad(u)(b⊗id)"; Lemma 2.1, eq. (2.2) "R(Σ a_g λ_g) = Σ (a_g∘μ_G) λ_{g,e}"; Props. 2.6, 2.9-2.12 on the gauge action "γ_t(s)(λ_g) = λ_{sgs⁻¹}" and its compatibility with refinement. The refinement maps are unital injective *-embeddings (introduction; Section 1.4.2 "injective *-morphism R"). The level-`t` algebra is `𝒞(G_t)⋊G_{t,d}⊂B(L²(G_t))` (Prop. 2.9). | The nearest published analogue of a Definition-Z map with a gauge field: a coarse link function is evaluated on the product of the fine link variables. It is gauge equivariant as an action of automorphisms. Section 7.2 computes, from eq. (2.2) alone, that for a finite abelian `G` the coarse gauge rotation at the far end of a link is carried to a fine operator at the near end, so the generator identity (G1) does not hold there, while equivariance does. For infinite compact `G` the link space `L²(G)` is infinite-dimensional and has no normalized trace, so Theorem T's first step has no analogue. |
| A. Brothier, A. Stottmeister, "Canonical quantization of 1+1-dimensional Yang-Mills theory: an operator-algebraic approach" | arXiv:1907.05549 | Abstract page only. | Context: the same refinement framework applied to YM in 1+1 dimensions. Not used. |
| A. Stottmeister, V. Morinelli, G. Morsella, Y. Tanimoto, "Operator-algebraic renormalization and wavelets" | arXiv:2002.01442; PRL 127, 230601 (2021) | Abstract page. | Context: an RG step fixed by a wavelet scaling equation, for free fields with no gauge field. Its maps are quasi-free, like `ZM1.md` Z1-Z2. Theorem T needs a Gauss law and does not apply. |
| T. J. Osborne, A. Stottmeister, "Conformal field theory from lattice fermions" | arXiv:2107.13834; CMP (2022) | Abstract page. | Context: the same framework for lattice fermions; no gauge field. Not used. |
| L. S. Trezzini, A. Bisio, P. Perinotti, "Renormalisation of Quantum Cellular Automata" | arXiv:2407.12652; Quantum 9, 1756 (2025) | Abstract page: tiles of neighbouring cells, a selected subspace per tile, several steps equal one step of a new automaton; a necessary and sufficient condition. | Context: a subspace (non-unital) notion of zoom. It lies outside Definition Z's unital maps; section 7.3. |
| L. S. Trezzini, A. Pizzamiglio, A. Bisio, P. Perinotti, "Renormalisation of Fermionic Cellular Automata" | arXiv:2511.23398 | Abstract page. Its Theorem 1, cited by `ZM1.md` Attack 3, was not re-read here: **NOT VERIFIED** in this lane. | The fermionic version of the previous row; the same remark. |
| O. Duranthon, G. Di Molfetta, "Coarse-grained quantum cellular automata" | arXiv:2011.04287; PRA 103, 032224 (2021) | Abstract page (paraphrase): space-time cells, projection onto cell borders ("signals"), coarse dynamics, a Dirac limit. | Context: projection-based coarse-graining with no gauge field. As far as the abstract shows, it is not a unital homomorphism of the kind in Definition Z. |
| M. Aguado, G. Vidal, "Entanglement renormalization and topological order" | arXiv:0712.0348; PRL 100, 070404 (2008) | Abstract page: an exact MERA for the toric code, a fixed point of the entanglement-renormalization flow, quantum doubles. | An exact RG for a lattice gauge model with finite link spaces (the toric code is a `Z_2` lattice gauge theory). Its steps are MERA isometries, which are not unital homomorphisms; so it lies outside Definition Z and is consistent with Theorem T; section 7.3. |
| S. Chandrasekharan, U.-J. Wiese, "Quantum link models: a discrete approach to gauge theories" | hep-lat/9609042; NPB 492 (1997) 455-474 | Abstract page. | Context: quantum link models reach a continuum limit by dimensional reduction from an extra dimension (D-theory; hep-lat/9709120 and hep-lat/0012014 seen in search results only, **NOT VERIFIED**), not by a homomorphic block map. Consistent with Theorem T. |
| J. Dimock, "The renormalization group according to Balaban — I. Small fields" | arXiv:1108.1335 (parts II, III: arXiv:1212.5562, 1304.0705, abstracts not fetched, **NOT VERIFIED**) | Abstract page of part I. | Context: the rigorous block-spin RG is measure-level (block averages of integration variables). It lies outside Definition Z (`ZM1.md` line 65). Not used. |
| T. Balaban, lattice gauge RG series (CMP, 1980s); K. Gawędzki, A. Kupiainen, block-spin RG (CMP, Ann. Phys., 1980s); D. Brydges, P. Federbush, cluster and Mayer expansions (JMP 1978) | not on arXiv | **NOT VERIFIED**: not fetched. | Named because the brief asks for them. All are measure-level. Nothing here depends on them. |
| M. B. Hastings, T. Koma, "Spectral gap and exponential decay of correlations" | math-ph/0507008; CMP 265 (2006) 781-804 | Abstract page. | Context for Lemma ER's tails: a gap gives exponentially decaying truncated correlations. Not used: the tails in section 6 are computed exactly. |
| B. Nachtergaele, R. Sims, "Lieb-Robinson bounds and the exponential clustering theorem" | math-ph/0506030; CMP 265 (2006) 119-130 | Abstract page. | Same as the previous row. Not used. |

Standard results used are rebuilt in the text, not cited: the uniqueness of the tracial state on a full matrix algebra (Lemma T1; for UHF algebras this is classical, credited to J. Glimm, 1960, **NOT VERIFIED**, not used); the CAR algebra of `n` modes is `M_{2^n}` (Jordan–Wigner, rebuilt in Lemma T1).

## 3. Definitions in force

### 3.1 The fine algebra

Fix `L5-U[m]`, `1 ≤ m ≤ 9`. Sites are `Z^3`; links join nearest neighbours. At each site `x` there are five matter modes `c_{x,j}` (CAR). Each link `ℓ = (x, y)` carries ten rishon modes, five at each end, restricted to total number `m`; its algebra is `End(Λ^m C^{10})`, a full matrix algebra of dimension `d_m^2`, `d_m = C(10, m)`. The quasi-local algebra `𝔄` is the norm closure of the finite-region algebras `𝔄(Λ)`. Link factors commute with matter and with one another (`VC1_5.md` §1, item 1). Write `N_x = Σ_j c^†_{x,j} c_{x,j}`, `p_{ℓ,x} = r^†_{ℓ,x} r_{ℓ,x}`, and

\[
 Q_x := \mathcal G^{1}_x = N_x + \sum_{\ell\ni x} p_{\ell,x},
\]

the Gauss generator at `T = 1` (`LW1_5.md` line 96). Two sites are **fine neighbours** if a link joins them. `Q_x` lies in the algebra of the **star** of `x`: its matter and its six links. The stars of `x` and `y` share a factor exactly when `x = y` or `x, y` are fine neighbours.

### 3.2 The coarse lattice

As in `ZM1.md` §1.1: the coarse cell `u ∈ Z^3` is the block `β_u` of the `L^3` fine cells `{Lu + c'}`, that is `(2L)^3` fine sites; it has 8 coarse sites `(u, r)`, `r ∈ {0,1}^3`. The coarse sites form a copy of `Z^3` (`(u, r) ↦ 2u + r`) with nearest-neighbour coarse links. Every coarse site has exactly six coarse neighbours. (`ZM1.md` §3.1 uses another indexing for Z0, with one coarse site per block of side `2L`; Theorem T′ holds for it too, with the same proof.)

### 3.3 One reading needed: "a coarse law of the `L5-U` form"

**Reading R-form (candidate; not adopted).** The coarse algebra `𝔄_1` is the `L5-U[m_1]` algebra of §3.1 on the coarse lattice of §3.2, for some `m_1 ∈ {1, …, 9}` not required to equal `m`. Its Gauss generators `G^{(1),T}_X` have the formula of `LW1_5.md` line 96. Its update `α_1` is any `L5-U` law there, with any constants and any plaquette class.

*Four tests.* (1) It states no target: it names an algebra, not a property of `α_1` or `ω_1`. Pass. (2) It is closed: the algebra is fixed up to the single integer `m_1`. Pass. (3) It settles no downstream physics by premise: it is the plain sense of Definition G's own words, "Let the coarse law be of the same type". Pass. (4) It adds no structure: it allows any `m_1` and any constants, so it is weaker than reading `m_1 = m`. Pass.

The no-go below does not depend on the choices that the reading leaves free. It holds for every `m_1`, for every `α_1`, and also if each coarse site carries extra finite gauge-neutral factors (Remark T.3).

### 3.4 The normalized trace

For a finite region `Λ`, `𝔄(Λ)` is a full matrix algebra (Lemma T1). Its normalized trace is `τ_Λ = Tr/dim`. These are compatible under inclusion, so they define a state `τ` of `𝔄`, the **tracial state**. In the occupation basis — matter occupation patterns times, on each link, the `d_m` subsets `S ⊂ {1, …, 10}` with `|S| = m` — every number operator and end number is diagonal, and `τ` of a diagonal operator is the uniform average of its diagonal over the product of these finite configuration sets. So, under `τ`, the matter occupations and the link configurations are independent random variables, matter occupations uniform on `{0, 1}`, each link configuration uniform on its `d_m` subsets. The same holds for `𝔄_1` and its tracial state `τ_1`.

## 4. The no-go on L5-U: trace rigidity of the Gauss embedding

Throughout this section `Φ : 𝔄_1 → 𝔄` is a unital *-homomorphism, `𝔄` is `L5-U[m]` and `𝔄_1` is `L5-U[m_1]` on the coarse lattice (§3). Injectivity and grading are never used.

### 4.1 The trace is transferred

**Lemma T1 (trace transfer).** (a) For every finite set of coarse sites, the algebra `𝔄_1(Λ_1)` of their matter and of the coarse links among them is *-isomorphic to a full matrix algebra `M_n`. (b) A tracial state of `M_n` equals `Tr/n`. (c) `τ(Φ(A)) = τ_1(A)` for every `A ∈ 𝔄_1`.

*Proof.* (a) Order the `k` matter modes of `Λ_1`. The Jordan–Wigner map `c_j ↦ σ^z ⊗ … ⊗ σ^z ⊗ σ^- ⊗ 1 ⊗ … ⊗ 1` (with `σ^-` in slot `j`) respects the CAR. Its image contains every `σ^-_j`: by induction on `j`, since `σ^z_i = 1 − 2(σ^-_i)^†σ^-_i`. These generate every matrix unit of `(C^2)^{⊗k}`, so the CAR algebra of `k` modes maps onto `M_{2^k}`. The CAR algebra is spanned by the `4^k` ordered monomials, so its dimension is at most `4^k`, and a surjection onto the `4^k`-dimensional `M_{2^k}` is injective. The link factors are full matrix algebras that commute with matter and with each other; so `𝔄_1(Λ_1) ≅ M_{2^k} ⊗ M_{d_{m_1}} ⊗ … ⊗ M_{d_{m_1}} = M_n`. (b) Let `φ` be a tracial state and `E_{ij}` the matrix units. For `i ≠ j`, `φ(E_{ij}) = φ(E_{ii}E_{ij}) = φ(E_{ij}E_{ii}) = 0`. For all `i, j`, `φ(E_{ii}) = φ(E_{ij}E_{ji}) = φ(E_{ji}E_{ij}) = φ(E_{jj})`. The `n` diagonal values sum to `φ(1) = 1`. (c) `A ↦ τ(Φ(A))` is positive and unital. It is tracial: `τ(Φ(AB)) = τ(Φ(A)Φ(B)) = τ(Φ(B)Φ(A)) = τ(Φ(BA))`, because `τ` is tracial on each `𝔄(Λ)` and hence, by continuity, on `𝔄`. By (a) and (b) it equals `τ_1` on every `𝔄_1(Λ_1)`. These are dense and both functionals are continuous. □

### 4.2 Two covariances

Write `Cov_τ(A, B) = τ(AB) − τ(A)τ(B)` and `Var_τ(A) = Cov_τ(A, A)`.

**Lemma T2 (fine independence).** If `x ≠ y` are not fine neighbours, `Cov_τ(Q_x, Q_y) = 0`. If `x, y` are fine neighbours, `Cov_τ(Q_x, Q_y) = −m(10−m)/36`. Also `Var_τ(Q_x) = 5/4 + m(10−m)/6`.

*Proof.* By §3.4, `Q_x` is the random variable `N_x + Σ_{ℓ∋x} p_{ℓ,x}` on a product probability space. If `x, y` are not fine neighbours, the stars of `x` and `y` are disjoint (§3.1), so `Q_x` and `Q_y` are functions of disjoint sets of independent coordinates. If they are neighbours, the only shared coordinate is the link `ℓ = (x, y)`; covariance is bilinear and independent terms drop out, so the covariance is `Cov(p_{ℓ,x}, p_{ℓ,y})`, computed in Lemma T3. The variance is the sum of the variances of the seven independent summands: `5 · 1/4` for matter and `6 Var(p)`. □

**Lemma T3 (hypergeometric end number).** Let `S` be uniform among the `m`-subsets of `{1, …, 10}` and `A` a fixed 5-subset. Put `p = |S ∩ A|` and `p' = m − p`. Then `Var(p) = m(10−m)/36` and `Cov(p, p') = −m(10−m)/36`. Both are nonzero for `1 ≤ m ≤ 9`.

*Proof.* Write `p = Σ_{i∈A} 1_i` with `1_i = 1[i ∈ S]`. Then `E 1_i = m/10` and, for `i ≠ i'`, `E 1_i 1_{i'} = m(m−1)/90`. So `Var(p) = 5 (m/10)(1 − m/10) + 20 (m(m−1)/90 − m^2/100) = m(10−m)/20 − m(10−m)/45 = m(10−m)/36`. Then `Cov(p, m − p) = −Var(p)`. □

[check] `out.txt`, first block: exact enumeration of the `C(10, m)` subsets gives `Cov(p_X, p_Y) = −m(10−m)/36` for `m = 1, …, 9`.

**Corollary T3′ (coarse anticorrelation).** For coarse neighbours `X, Y`, `Cov_{τ_1}(Q^{(1)}_X, Q^{(1)}_Y) = −m_1(10−m_1)/36 < 0`.

*Proof.* Lemma T2 on the coarse lattice, which has the same local structure, with `m_1` for `m`. □

### 4.3 Adjacency, then no block map

**Theorem T (adjacency of representatives).** Suppose `Φ(G^{(1),1}_X) = G^1_{x_X}` for every coarse site `X`, that is, (G1) at `T = 1` with `S_X = {x_X}`. Then for every coarse link `(X, Y)`, the sites `x_X` and `x_Y` are fine neighbours. Moreover `m(10−m) = m_1(10−m_1)`.

*Proof.* `G^1 = Q`. By Lemma T1(c), `τ(Q_{x_X} Q_{x_Y}) = τ(Φ(Q^{(1)}_X Q^{(1)}_Y)) = τ_1(Q^{(1)}_X Q^{(1)}_Y)`, and `τ(Q_{x_X}) = τ_1(Q^{(1)}_X)`, `τ(Q_{x_Y}) = τ_1(Q^{(1)}_Y)`. So `Cov_τ(Q_{x_X}, Q_{x_Y}) = −m_1(10−m_1)/36 < 0` by Corollary T3′. If `x_X = x_Y`, the left side is a variance, which is not negative. If `x_X ≠ x_Y` are not fine neighbours, the left side is `0` by Lemma T2. Both are contradictions, so they are fine neighbours, and Lemma T2 then gives `−m(10−m)/36` on the left. □

**Lemma T5 (bounded displacement).** Suppose (G1) at `T = 1` with singleton sets, and (Z-a) with constants `C, ξ` for the coarse site and link algebras, each assigned to the block of its coarse cell or of an adjacent coarse cell. Then there is `R_*`, depending on `C, ξ, L`, with `dist(x_X, β_{u(X)}) ≤ R_*` for every coarse site `X = (u(X), r)`.

*Proof.* `Q^{(1)}_X` is a sum of seven terms, `N_X` and six end numbers, each of norm at most `5` and each in an algebra assigned to a block within fine distance `4L` of `β_{u(X)}`. By (Z-a), for every `R` there is `Y_R` supported in the set `Γ_R` of sites within `R + 4L` of `β_{u(X)}` (with the links among them) such that `‖Q_{x_X} − Y_R‖ ≤ 35 C e^{−R/ξ}`. Suppose the star of `x_X` shares no factor with `Γ_R`. Let `σ_±` be two occupation configurations that agree off the star of `x_X`; on the star, `σ_+` fills the matter of `x_X` and gives each of its six ends the end number `min(5, m)`, and `σ_-` empties the matter and gives each end `max(0, m−5)`. Their basis-vector states `ψ_±` are states of `𝔄`: the expectation of a CAR monomial in a basis vector is nonzero only if each mode occurs in a pair `c^†c` or `cc^†`; it then equals a sign independent of the configuration times a product of occupations of the modes involved. So `ψ_+(Y) = ψ_-(Y)` for every `Y ∈ 𝔄(Γ_R)`. But `ψ_+(Q_{x_X}) − ψ_-(Q_{x_X}) = 5 + 6(min(5,m) − max(0,m−5)) ≥ 11`. Hence `11 ≤ |ψ_+(Q_{x_X} − Y_R)| + |ψ_-(Q_{x_X} − Y_R)| ≤ 2 · 35 C e^{−R/ξ}`. Fix `R` with `70 C e^{−R/ξ} < 11`. Then the star of `x_X` meets `Γ_R`, so `dist(x_X, β_{u(X)}) ≤ R + 4L + 1 =: R_*`. □

**Theorem T′ (no block map for `L ≥ 2`).** Suppose (G1) at `T = 1` with pairwise disjoint singleton sets, and (Z-a) as in Lemma T5. Then `L = 1`.

*Proof.* Let `ρ(X) = x_X`. Disjointness makes `ρ` injective. By Theorem T, `ρ` maps the six coarse neighbours of `X` to six distinct fine neighbours of `ρ(X)`. A fine site has exactly six fine neighbours, so `ρ` maps the coarse neighbourhood of `X` onto the fine neighbourhood of `ρ(X)`. Hence the image of `ρ` contains every fine neighbour of each of its points. The fine lattice is connected, so `ρ` is onto: it is a bijection from coarse sites to fine sites. Now count. Let `B_N` be the union of the blocks `β_u`, `u ∈ {0, …, N−1}^3`; it has `(2LN)^3` fine sites. Each is `ρ(X)` for exactly one `X = (u, r)`, and Lemma T5 puts it within `R_*` of `β_u`. Then each coordinate of `u` lies in `[−c, N − 1 + c]` with `c = ⌈R_*/(2L)⌉ + 1`. There are at most `8(N + 2c)^3` such `X`. So `8L^3N^3 ≤ 8(N + 2c)^3` for every `N ≥ 1`, that is `L ≤ 1 + 2c/N`. Let `N → ∞`: `L ≤ 1`. □

**Corollary T″ (ZM1-I1[a] has no data on `L5-U`).** For every `m ∈ {1, …, 9}`, every vacuum, every fine update, every coarse law of the `L5-U` form (reading R-form), every coarse state and every `L ≥ 2`: no map satisfies Definition Z with (Z-a) together with (G1) on singleton embedding sets. So the existential statement ZM1-I1[a] with `p = 2` is false. So are ZM1-I1[a] with any `p`, ZM1-I1[O] for each class `O` of `ZM1_OBS.md` §5, and the original ZM1-I1 of `ZM1.md` line 363.

**Named failing step.** "`Φ(G^{(1),1}_X) = G^1_{x_X}`" — (G1) at `T = 1` — at a coarse link whose two representatives are not fine neighbours. Theorem T′ shows that (Z-a) and `L ≥ 2` force such a link to exist.

**Remark T.3 (what is not used).** (Z-b), (G2), injectivity, the grading, the coarse dynamics `α_1`, the states `ω_0, ω_1`, the comparison class and `p` are not used. The value of `m_1` is not used beyond `1 ≤ m_1 ≤ 9`. Extra finite gauge-neutral factors at coarse sites change nothing: they are independent coordinates under `τ_1` and do not enter `Q^{(1)}_X`. With the indexing of `ZM1.md` §3.1 (one coarse site per block of side `2L`), the count in Theorem T′ gives `8L^3 ≤ 1`, a contradiction for every `L ≥ 1`.

### 4.4 Two strengthenings

**Proposition V (on `L5-U`, (G1) forces singletons).** Suppose `Φ(G^{(1),1}_X) = Σ_{x∈S_X} G^1_x` for nonempty finite sets `S_X`. Then `|S_X| = 1` for every `X`. This sharpens `ZM1.md` Theorem Z4, which bounds `|S_u|` by the content.

*Proof.* Put `S = S_X`, `I(S)` = number of links with both ends in `S`, and `∂S` = number of links with exactly one end in `S`; so `|∂S| = 6|S| − 2I(S)`. On a link with both ends in `S` the two end numbers sum to the constant `m`. So `Σ_{x∈S} Q_x = Σ_{x∈S} N_x + m I(S) + Σ_{ℓ∈∂S} p_{ℓ, end in S}`, a constant plus independent summands, and `Var_τ = 5|S|/4 + v|∂S|` with `v = m(10−m)/36`. Lemma T1 gives `Var_τ(Σ_{x∈S}Q_x) = Var_{τ_1}(Q^{(1)}_X) = 5/4 + 6v_1`, `v_1 = m_1(10−m_1)/36`. Multiply by 36 and put `k = m(10−m)`, `k_1 = m_1(10−m_1)`, both in `{9, 16, 21, 24, 25}`:
\[
 45(|S|-1) = 6k_1 - k\,|\partial S| .
\]
Every nonempty finite `S ⊂ Z^3` has `|∂S| ≥ 6`: for each of the six directions `±e_i`, a site of `S` that maximizes the coordinate along that direction has its link in that direction leaving `S`. So the right side is at most `150 − 54 = 96`, and `|S| ≤ 3`. The lattice graph is bipartite, so three sites span at most two links: for `|S| = 3`, `|∂S| ≥ 14` and the right side is at most `150 − 126 = 24 < 90`. For `|S| = 2`, `|∂S| ∈ {10, 12}` is even, so the right side `6k_1 − k|∂S|` is even, while the left side is `45`, which is odd. So `|S| = 1`. □

[check] `out.txt`, last block: no solution with `|S| ∈ {2, 3, 4}` for the listed boundary sizes.

**Proposition Z5 (the `SU(5)` part suffices).** Suppose (G1) is required only for traceless `T`, with singleton sets. Theorems T and T′ still hold.

*Proof.* Let `ζ = e^{2πi/5}` and `H = (2π/5) diag(1, 1, 1, 1, −4)`, traceless. On a five-mode Fock space, `exp(i c^†Hc)` is the second quantization of `e^{iH} = ζ·1`, so it acts on the `N`-particle sector as `ζ^N`. Hence `u_x := exp(i G^H_x) = ζ^{N_x} ∏_{ℓ∋x} ζ^{p_{ℓ,x}}`, and likewise `u^{(1)}_X`. A unital *-homomorphism preserves exponentials of self-adjoint elements (`ZM1_OBS.md` Theorem 1), so `Φ(u^{(1)}_X) = u_{x_X}`. All factors are diagonal, so §3.4 applies. Put `μ = E ζ^{N} = (1+ζ)^5/32` and `κ = E ζ^{p}` for the end number `p` of Lemma T3 (at either end; `p` and `m_1 − p` have the same law). For coarse neighbours, independence and `p_{ℓ,X} + p_{ℓ,Y} = m_1` give
\[
 \tau_1(u^{(1)}_Xu^{(1)}_Y)-\tau_1(u^{(1)}_X)\tau_1(u^{(1)}_Y)=\mu^2\kappa^{10}\big(\zeta^{m_1}-\kappa^2\big).
\]
Here `μ ≠ 0` since `1 + ζ ≠ 0`. `|κ| < 1`: `κ` is a positive-weight average of `ζ^a` over at least two consecutive values of `a`, which give distinct points of the unit circle. So `ζ^{m_1} ≠ κ^2`. `κ ≠ 0`: for `m_1 ≤ 2` the points `ζ^a`, `a ≤ m_1`, lie in an open half-plane; for `m_1 = 3, 4, 5` the real part of `C(10,m_1) κ` is `10 + 50cos72° + 50cos144° + 10cos216° < 0`, `5 + 50cos72° + 100cos144° + 50cos216° + 5cos288° < 0`, and `2 + 50cos72° + 200cos144° < 0`; for `m_1 ≥ 6`, `|κ_{m_1}| = |κ_{10−m_1}|` by the substitution `a ↦ 5 − a`. So the coarse covariance is nonzero. For fine sites that are not neighbours the fine covariance of `u_x, u_y` is `0` by independence. The rest is the proof of Theorems T and T′. □

[check] `out.txt`, third block: `|κ| ∈ [0.57, 0.81]` and `|coarse covariance| ∈ [0.35, 0.67]` (before the factor `μ^2κ^{10}`) for `m_1 = 1, …, 9`.

## 5. The no-go on L5-O[S_+]

The lane brief admits `L5-O` ("on L5-U[m] (or L5-O)"). `ZM1_OBS.md` §5 says the O analogue of ZM1-I1 "is a separate proposed comparison". Read it with the same Definitions Z and G, coarse law of the `L5-O[S_+]` form, and the Gauss generators of `LW1_5.md` line 89: "\(\mathcal G_x^{cd}=M_x^{cd}+\sum_{\ell\ni x}L^{cd}_{\ell,x}\)". The group is `Spin(10)`, which has no `U(1)` factor, so Lemma T3's covariance is not available. The linear covariance of the Cartan generators across an `S_+` link is `0`: the mean of `N` over the even values and over the odd values of a five-mode factor is `40/16 = 5/2` in both cases, so the shared parity carries no linear correlation. A group element replaces it.

### 5.1 The factors and a torus element

At a site, the ten matter Majoranas `γ_{x,a}` form a factor with Fock space `C^{32}`. A link carries twenty Majoranas, ten at each end (`η^y_a`, `η^x_b`, `LW1_5.md` line 87), restricted to the 512-dimensional half-spin space `S_+` of `Spin(20)`. On any ten Majoranas `γ_1, …, γ_{10}` put `c_j = (γ_{2j−1} + iγ_{2j})/2` and `n_j = c^†_j c_j`. Then `γ_{2j−1}γ_{2j} = −i(2n_j − 1)`, so

\[
 \tfrac i2\,\gamma_{2j-1}\gamma_{2j}=n_j-\tfrac12 .
\]

`M^{cd}` and `L^{cd}` have this form (`T_{ij}=iη_iη_j/2`, `LW1_5.md` line 87; `M^{12}−M^{34}=n_1−n_2`, line 333). So `K_x := Σ_{j=1}^5 \mathcal G^{2j−1,2j}_x` acts on each of the seven factors of the star of `x` as `N − 5/2`, `N` the number of that factor's five complex modes. The two ends of an `S_+` link have equal parity of their numbers `N_x, N_y` (`VC1_5.md` §2: "`S_+` is the even total-rishon-parity sector"). The opposite convention changes only the sign of the covariance below.

Put `g_x = exp(i(π/2)K_x)`, a local gauge unitary. It is diagonal in the occupation basis and acts on each factor as `e^{i(π/2)(N − 5/2)}`. Let `χ_e = Σ_{N even} C(5,N) e^{i(π/2)(N−5/2)}` and `χ_o` the same sum over odd `N`. With `e^{−i5π/4}` factored out, `Σ_{N even} C(5,N) i^N = 1 − 10 + 5 = −4` and `Σ_{N odd} C(5,N) i^N = 5i − 10i + i = −4i`. So `χ_e = −4e^{−i5π/4}`, `χ_o = −4i e^{−i5π/4}`, `χ_e + χ_o = 4√2`, and `(χ_e − χ_o)^2 = −32`.

**Lemma O1 (traces of `g`).** Under the tracial state: on the matter factor, `τ(g) = (χ_e + χ_o)/32 = 2^{−5/2}`; on an `S_+` link with `g` at one end only, `τ(g ⊗ 1) = 16(χ_e + χ_o)/512 = 2^{−5/2}`; with `g` at both ends, `τ(g ⊗ g) = (χ_e^2 + χ_o^2)/512`, so
\[
 \tau(g\otimes g)-\tau(g\otimes1)\,\tau(1\otimes g)=\frac{(\chi_e-\chi_o)^2}{1024}=-\frac1{32}.
\]

*Proof.* The `S_+` basis is the set of pairs of occupation patterns at the two ends with equal parity of `N_x, N_y`: `2 · 16 · 16 = 512` pairs. Sum the diagonal over them. □

[check] `out.txt`, second block: enumeration of the 512 basis states gives covariance `−0.03125` and `τ(g) = 0.17678 = 2^{−5/2}`.

### 5.2 The theorem

**Theorem O (adjacency on `L5-O[S_+]`).** Let `Φ` be a unital *-homomorphism from the coarse `L5-O[S_+]` algebra into the fine one, with `Φ(\mathcal G^{(1),2j−1,2j}_X) = \mathcal G^{2j−1,2j}_{x_X}` for `j = 1, …, 5` and every coarse site `X` (part of (G1) with singleton sets). Then representatives of coarse neighbours are fine neighbours. With pairwise disjoint sets and (Z-a), `L = 1`.

*Proof.* Lemma T1 holds verbatim: the coarse matter factor is a CAR algebra of five modes and each link algebra is `End(S_+) = M_{512}`. Since `Φ` preserves exponentials of self-adjoint elements (`ZM1_OBS.md` Theorem 1), `Φ(g^{(1)}_X) = g_{x_X}`. For coarse neighbours `X, Y`, all factors are independent under `τ_1` except the shared link, so by Lemma O1
\[
 \tau_1(g^{(1)}_Xg^{(1)}_Y)-\tau_1(g^{(1)}_X)\tau_1(g^{(1)}_Y)=(2^{-5/2})^{12}\cdot\Big(-\frac1{32}\Big)=-2^{-35}\neq0 ,
\]
the twelve factors being the matter and the five unshared links at each of `X` and `Y`. Under `τ`, `g_x` and `g_y` are independent when `x ≠ y` are not fine neighbours, so their covariance is `0`, a contradiction. If `x_X = x_Y = x`, this element gives none: `g_x^2` acts on the matter factor as `−i(−1)^N`, of trace `0`, so the fine value is `τ(g_x^2) − τ(g_x)^2 = −(2^{−5/2})^{14} = −2^{−35}`, equal to the coarse value. That case is excluded by the disjointness of the embedding sets, which Definition G requires. The rest is the proof of Theorem T. For Theorem T′, Lemma T5 holds with `\mathcal G^{12}_x` in place of `Q_x`: its spectrum on the star runs from `−7/2` to `7/2`, both ends attained by occupation configurations with each link in `S_+` (adjust the parity of a link with a mode of its far end, which lies in the star), so the bound `‖\mathcal G^{12}_x − Y‖ ≥ 7/2` replaces `11/2`. □

**Corollary O″.** The `L5-O[S_+]` analogue of ZM1-I1[a], read with Definitions Z and G, has no data for any vacuum (including the witnesses `ω_0`, `ω_F`, `τ` of `VC1_5.md` Theorems 4.1-4.2), any update and any `L ≥ 2`. Named failing step: (G1) on the Cartan generators at a coarse link whose representatives are not fine neighbours.

### 5.3 The common mechanism

**Theorem G (general form).** Let a law have finite-dimensional link registers, a compact local gauge group acting on the star of each site by local unitaries, and a coarse law of the same type. Suppose there are local gauge unitaries `g = exp(i θ·\mathcal G)`, `h = exp(i θ'·\mathcal G)` whose traces on every unshared factor of a star are nonzero, and whose action on one link register is **trace-correlated**: `τ_ℓ(g_X h_Y) ≠ τ_ℓ(g_X) τ_ℓ(h_Y)`. Then any unital *-homomorphism with (G1) on disjoint singleton sets sends coarse neighbours to fine neighbours, and with (Z-a) it has `L = 1`.

*Proof.* Lemma T1, preservation of exponentials, and the independence argument of Theorems T and O. □

If the end actions are trace-uncorrelated for all `g, h`, the character of the link register factorizes, `χ(g, h) = χ(g, 1)χ(1, h)/dim`. Theorem G does not apply to such registers. The registers of `L5-U`, `L5-O[S_+]` and `L_cube` are trace-correlated: for `L_cube` the electric field enters the Gauss law at the two ends with opposite signs, so the covariance is `−Var(E) = −S(S+1)/3 < 0` for spin `S ≥ 1/2`.

## 6. First tests: which vacua are trivial for the criterion

Theorem T′ removes every first test at the block-map stage. The brief still asks which exactly solvable cases are trivial for the criterion. This section answers it for a hypothetical block map, so that the answer stays useful under any changed specification of section 8 that keeps class (a).

**Definition (dark pair; used only in this section).** A state and update `(ω, α)` of a five-mode law are **dark** if, for all gauge-invariant local `X, Y` with disjoint supports and all `n ≥ 0`, `ω(X α^n(Y)) = ω(X)ω(Y)`.

**Proposition 6.0 (dark pairs are trivial for the criterion).** Let `Φ` be a block map with (G1)-(G2) on singleton sets that is of finite range (each `Φ(B)`, `B` in a coarse site or link algebra, is supported within fine distance `r_Φ` of its block). Let `(ω_0, α)` and `(ω_1, α_1)` be dark. Then class (a)'s bound holds for every `p` with `C_{R_0} = 2(2R_0 + 2⌈r_Φ/L⌉ + 3)^p`.

*Proof.* `Φ(𝔄_1^G) ⊆ 𝔄^G` (`ZM1_OBS.md` Theorem 3). Let `r_* = 2R_0 + 2⌈r_Φ/L⌉ + 3`. For `|β|_∞ ≥ r_*` the supports of `Φ(A)` and `Φ(τ_βB)` are disjoint, and the coarse supports of `A` and `τ_βB` are disjoint, so both truncated values vanish at every tick. For `1 ≤ r < r_*`, `|F_0^T − F_1^T| ≤ 2M(r,t) ≤ C_{R_0} r^{−p} M(r,t)`, because `M(r,t)` dominates both values at `β`. □

With only the exponential tails that (Z-a) allows, dark pairs are not trivial: a nonzero fine value against a zero coarse value at every larger separation violates the bound, by Lemma ER. So triviality needs finite range, which (Z-a) permits.

### 6.1 Empty-matter vacua with the base tick are dark

**Lemma DK (dark kinematics; extends `GA1_5.md` Theorem 6.1).** On `L5-U[m]`, take the base tick `U_0 = W_E M_o M_e` with any `ε, μ, τ_E` and no plaquette layer. Let `ψ` be an even product state over sites and links with empty matter at every site (or full matter at every site), whose link states commute with the electric factors, and put `ω = ψ∘E`. Then `ω(X α^n(Y)) = ψ(X γ^n(Y))` for invariant local `X, Y`, where `γ = Ad(W_E^*)` is a product of single-link automorphisms. Hence `(ω, α)` is dark.

*Proof.* `GA1_5.md` Theorem 6.1 (R) states the reduction for D1 states with `ω(N_x) = 0` and update `W_B W_E` composed with the matter layers; with no plaquette layer `W_B = 1`. Its proof, quoted: "Every number-conserving matter hop annihilates empty matter, so the matter cube unitaries and their adjoints act as identity on `P₀`. The link layers preserve `P₀`." And: "Summing the local `U(1)` Gauss-charge commutators shows `∑d_x=0`". So on a finite region containing all supports, an invariant `X` commutes with the projection `P_0` onto empty matter, `ρ_ψ = P_0ρ_ψP_0`, and `U_0P_0 = W_EP_0`, `P_0U_0^* = P_0W_E^*`. Then
\[
 \operatorname{tr}(\rho_\psi XU_0^{*n}YU_0^{n})=\operatorname{tr}(U_0^{n}\rho_\psi XU_0^{*n}\,Y)=\operatorname{tr}(W_E^{n}\rho_\psi XW_E^{*n}\,Y)=\psi(X\,\gamma^n(Y)).
\]
For full matter the same holds with the projection onto full matter: a hop `c^†_y U c_x` and its adjoint vanish there because `c^†` kills a full mode. `W_E` is a product of commuting one-link unitaries, so `γ^n(Y)` has the support of `Y`. For disjoint supports, the even product state factorizes: `ψ(Xγ^n(Y)) = ψ(X)ψ(γ^n(Y)) = ψ(X)ψ(Y)`, since `ψ` commutes with the electric factors. On invariant elements `ω = ψ`. □

So the following VC1 vacua give dark pairs with the base tick, and are **trivial for the criterion**: `VC1_5.md` Theorem 5.2 at `t = ±∞` (empty or full matter, normalized link traces; reading E, every `m`); Theorem 5.5 (even `m`, locked end numbers `(k, k)`, empty or full matter; reading P). The coarse law has dark pairs of the same kind (Lemma DK on the coarse lattice). For these vacua the whole content of ZM1-I1[a] would be the block map, and Theorem T′ says there is none.

### 6.2 Vacua that are not trivial

**Proposition R2′ (the non-factor E-witness has a constant tail).** In `VC1_5.md` Proposition R2, `ω = 2^{−3}Σ_s ψ_s`. Let `P = Π[p_{ℓ,src} = a]` on a link `ℓ` along `e_1`, a gauge-invariant projection, and `β` a translation along `e_1`. Then `F^T(P, τ_βP; t) = 1/4` for every separation and every tick.

*Proof.* Each `ψ_s` is gauge invariant ("so `ψ_s` is gauge invariant", `VC1_5.md` line 200) and satisfies Lemma DK's hypotheses: empty matter, and link densities that are functions of `p_{ℓ,src}`, hence commute with `W_E`. `P` and `τ_βP` are functions of end numbers, so `γ` fixes them. By Lemma DK and the product property, `ψ_s(P α^n(τ_βP)) = ψ_s(P γ^n(τ_βP)) = ψ_s(P)ψ_s(τ_βP)` for `β ≠ 0`. Here `ψ_s(P) = ψ_s(τ_βP) = 1` if `s_1 = +1` and `0` otherwise ("In each `ψ_s` every `P_i` is sharp, at `1` if `s_1 = +1` and at `0` if `s_1 = −1`", `VC1_5.md` line 202). Four of the eight `s` have `s_1 = +1`. So `ω(P α^n(τ_βP)) = 1/2` and `ω(P) = ω(τ_βP) = 1/2`, and `F^T = 1/2 − 1/4`. □

So `M(r, t) ≥ 1/4` for all `r`, and Lemma ER (power form with `η = 0`) asks the coarse side for the same constant tail with the same amplitude `1/4`, at every tick. Not trivial.

**The swap band (`GA1_5.md` Theorem 6.3, Proposition S-odd).** The D1 state is a product over stars with empty matter, and the update adds the swap layer. The band is `V(K) = e^{−iK·(1,1,1)}` (`GA1_5.md` line 168), an exact glider: "swap conjugation moves `A_v` to `A_{a_e(a_o(v))}`. At `v=2b`, this is `2b−2(1,1,1)`" (line 178). The vectors `u_b = π(A_{2b})Ω` are orthonormal (same line). So the truncated value of `A_0^*` and `τ_βA_0` at tick `t` is `1` at one `β` with `|β|_∞ = t` and `0` at every other `β`. If the image of a block map contains an element with a nonzero component along `u_0`, the envelope `M(r, t)` is nonzero for `r ≤ t`, and at `r = t` the bound asks the coarse value at that `β` to equal the fine one up to `2C_{R_0}t^{−2}` times the envelope: an exact coarse glider, one coarse cell per coarse tick. Not trivial. The same holds for the conjugated band of `GA15PHI.md`.

**The two-band vacua (`LZ1I.md` Theorems 6-8).** `ω_Σ` and its cell average `ω̄` carry "two bands with the fibres `V₁,V₂`" of different Clifford speeds (line 99). `ZM1_OBS.md` Theorems 8′ and 9′ then ask the coarse law to reproduce both branch phases to `O(|θ|^{p+1})` and their weights. Not trivial; this is the content `LZ1I.md` names LZ1-i[ZM1a].

**Not decided here, and not needed.** The odd-`m` ice states (`VC1_5.md` R4; `VC1_5U_ODD.md` Theorems 4.3 and 5.1: "If ICE-T holds, every odd `m∈{1,3,5,7,9}` and every allowed choice of base-tick constants has two distinct P-witnesses, of filling 0 and 5"): Lemma DK's reduction applies (empty or full matter), so the invariant dynamics is the electric layer, but the link state is not a product state; the tails are the correlations of the ice measure, which this file does not compute. Theorem 5.2 at finite `t`, and the `L5-O` witnesses `ω_0`, `ω_F`, `τ`: the matter hops act on excitations (`GA1_5.md` line 192: "the Majorana hop can create pairs"), and their tails are not computed here.

All of these fail at Theorem T′ (on `L5-U`) or Theorem O (on `L5-O`).

## 7. What the no-go uses, and what escapes it

### 7.1 The hypotheses, one by one

| Hypothesis | Where used | Without it |
|---|---|---|
| `Φ(1) = 1` and `Φ` a *-homomorphism | Lemma T1(c): `τ∘Φ` is a tracial state, hence `τ_1` | Section 7.3. |
| Finite link registers (PS-6r) | Lemma T1(a): local algebras are full matrix algebras with a normalized trace | Section 7.4. |
| (G1) as an identity of generators, at `T = 1` (U), the centre of `SU(5)` (U, Proposition Z5) or the Cartan torus (O) | Theorems T, O, Proposition Z5 | Section 7.2. |
| A coarse law of the same type: coarse neighbours share a trace-correlated link | Corollary T3′, Lemma O1 | A coarse system whose links are trace-uncorrelated is not a gauge law of the five-mode type (Theorem G, last paragraph). |
| Disjoint embedding sets | injectivity of `ρ` in Theorem T′; the case `x_X = x_Y` in Theorem O | Definition G requires disjointness. |
| (Z-a) | Lemma T5: bounded displacement | Without locality, `ρ` can be any graph isomorphism of `Z^3`, and the "zoom" is a relabelling of the fine law with `L` only a name. |
| `L ≥ 2` | the count in Theorem T′ | `L = 1` and `Φ = id` satisfy everything. |

Not used: (Z-b), (G2), injectivity, the grading, `α`, `α_1`, `ω_0`, `ω_1`, the comparison class and `p`.

### 7.2 Gauge equivariance in place of the generator identity

Read (G1) at the level of automorphisms:

\[
 \text{(G1-eq)}\qquad \Phi\circ\operatorname{Ad}\big(e^{i\theta\mathcal G^{(1),T}_X}\big)=\operatorname{Ad}\big(e^{i\theta\mathcal G^{T}_{x_X}}\big)\circ\Phi\quad\text{for all }X,\ T,\ \theta .
\]

(G1) implies (G1-eq). Under (G1-eq) only, `e^{−iθ\mathcal G^T_{x_X}}Φ(e^{iθ\mathcal G^{(1),T}_X})` lies in the relative commutant `Φ(𝔄_1)' ∩ 𝔄`, and need not be `1`. Lemma T1 still holds, but the fine element whose trace is transferred is `Φ(Q^{(1)}_X)`, which may differ from `Q_{x_X}` by an element of the relative commutant. Theorem T's comparison then has no fine side to compare with. So Theorem T does not apply. This lane does not decide whether a map with (G1-eq) exists; it is the open statement G1-EQ of section 8.1.

The published refinement maps for lattice gauge fields are equivariant in this sense. In Brothier–Stottmeister (arXiv:1901.04940), Lemma 2.1, eq. (2.2): "R(Σ a_g λ_g) = Σ (a_g∘μ_G) λ_{g,e}". So `R(λ_g) = λ_g ⊗ 1`. The following is this lane's computation from eq. (2.2), not a statement of that paper. Take `G` finite and abelian, so that `L^2(G)` is finite-dimensional and the link algebra is a full matrix algebra. Right translation is `(ρ_bξ)(h) = ξ(hb) = ξ(bh) = (λ_{b^{−1}}ξ)(h)`, so `R(ρ_b) = λ_{b^{−1}} ⊗ 1`: the coarse gauge rotation at the far end of the coarse link goes to an operator on the near fine link. The fine gauge rotation at the far end is `1 ⊗ ρ_b`. The two implement the same automorphism of the image: for `f` a function on `G`, both send `f(g_1g_2)` to `f(g_1g_2b)`, and both commute with `λ_g ⊗ 1`. So `R` satisfies (G1-eq) at the far end, and it does not satisfy the generator identity there. This is what the argument of Theorem G predicts: on the refined chain the two ends of the coarse link are not neighbours, and for finite `G` the generator identity would contradict the trace (for abelian `G`, `λ_aρ_a = 1` on one link, so the two end rotations are perfectly trace-correlated).

### 7.3 Non-unital maps

The exact RG maps found in the literature for finite-register gauge and topological models are isometries or subspace selections: the toric-code MERA (Aguado–Vidal, arXiv:0712.0348), the tile-and-subspace renormalisation of automata (arXiv:2407.12652, arXiv:2511.23398), and the level-matched polar map of #9928 in the digest. An isometry `V` gives `A ↦ VAV^*`, with `Φ(1) = VV^* ≠ 1`. The natural Gauss condition is then an intertwining, `VG^{(1)}_X = G_{x_X}V`. In finite volume `Tr(VAV^*) = Tr(A)`, so traces are still transferred, but the relevant fine functional is the compressed trace `Tr(P · P)`, `P = VV^*`. It need not factorize across fine sites, because `P` can correlate them. So Lemma T2 has no analogue, and Theorem T does not apply. These maps lie outside Definition Z, which asks for a unital homomorphism.

### 7.4 Infinite registers and measure-level maps

With group-valued links (`L^2(G)`, `G` infinite compact), the link algebra has no normalized trace and Lemma T1 fails. This is the setting of Brothier–Stottmeister's refinement (`𝒞(G_t)⋊G_{t,d}⊂B(L²(G_t))`, Prop. 2.9) and of the Peter–Weyl approximation note in the digest. The argument of Theorem G does not use that the coarse register equals the fine one: it applies to every finite coarse register, of any size, whose two ends are trace-correlated. Measure-level block maps (Balaban's RG; Dimock's exposition, arXiv:1108.1335; the constrained-fiber series in the digest) average integration variables, not operators, and lie outside Definition Z (`ZM1.md` line 65).

### 7.5 Relation to earlier obstructions

- `ZM1.md` Theorems Z3, Z3′ (linear coarse fermions vanish off the representative site) and Attacks 1-2 fail at the coarse matter field. Theorem T fails at the coarse Gauss law, whatever the fields are. Z3′ is not implied by T: Z3′ is a statement about one field under (G1)-(G2), and T shows that no full map has (G1); the field statement stays meaningful under (G1-eq).
- `GA2_Y2.md` Theorem 2.1 (N) forbids an invertible covariant link operator on a finite register. Theorem T forbids a trace-preserving Gauss embedding with distant representatives. N is about one operator; T is about the trace of an embedded algebra. Neither implies the other. Both come from PS-6r's finite registers, and both disappear for group-valued links.
- `ZM1.md` Theorem Z4 bounds the content by `|S_u|`. Proposition V forces `|S_u| = 1` on `L5-U`, whatever the content.

## 8. Readings offered to the owner (four-tested, none adopted)

Theorem T′ shows that the owner's text, read with Definitions Z and G, has no instance on either five-mode law. The owner said "we can specify if needed". Three changes are offered. Each is a candidate. None is adopted. Each keeps class (a), `p = 2` and the rest of the owner's text.

### 8.1 R-G1EQ: gauge equivariance at representative sites

**Text.** Replace (G1) by (G1-eq) of section 7.2: `Φ∘Ad(e^{iθ\mathcal G^{(1),T}_X}) = Ad(e^{iθ\mathcal G^T_{x_X}})∘Φ` for every coarse site `X`, every `T` and every real `θ`. Keep (G2), singleton disjoint sets, (Z-a), (Z-b), unital injective graded homomorphisms and a coarse law of the same type.

*Four tests.* (1) It states no target: it is a closed condition on `Φ`. Pass. (2) It is closed. Pass. (3) Downstream physics: the conclusions of `ZM1_OBS.md` Theorems 2-3 and `ZM1.md` Lemma R-GI follow from one consequence of (G1), the step "conjugation by `e^{iθ G^1_x}` acts on `Φ(A_1)` as `Φ` of the coarse gauge transformation at `X`" (`ZM1.md` line 372), which (G1-eq) states directly. So class (a)'s data stay gauge-invariant and their selection rules survive. But coarse and fine Gauss charges are no longer identified, so any statement about charged sectors (R-CS, MT1-S) would need its own link between the two. Class (a) uses none. Conditional. (4) It removes structure: it is implied by (G1). Pass. **P P C P.**

*What it leaves.* **G1-EQ (open statement).** On `L5-U[m]` (or `L5-O[S_+]`), for some `L ≥ 2`, is there a unital *-homomorphism `Φ` from a coarse algebra of the same type with (Z-a), (Z-b), (G1-eq), (G2) and disjoint singleton sets? Theorem T does not decide it (section 7.2). Brothier–Stottmeister's maps satisfy the analogue of (G1-eq) for group-valued links. Whether a finite-register analogue exists is not known to this lane.

### 8.2 R-ISO: isometric zooms on a selected subspace

**Text.** Replace "unital injective graded *-homomorphism" by "an isometric embedding of the coarse system onto a specified subspace of the fine system, with each coarse Gauss generator intertwined with the fine generator at its representative site". This is the subspace notion of `ZM1.md` Attack 3 and of arXiv:2407.12652 and arXiv:2511.23398.

*Four tests.* (1) It states no target, provided the subspace is fixed by its own rule and not chosen to make the comparison hold. Conditional. (2) It is closed only once that rule is stated. Conditional. (3) If the subspace is the vacuum or a low-energy sector, it settles by premise that this sector closes under the dynamics, which is part of what the zoom is meant to show. Conditional. (4) It adds a projection and an intertwining condition. Conditional. **C C C C.** Its closedness also meets the unproved classification of `ZM1.md` GAP Attack 3.

### 8.3 R-MEAS: measure-level block maps

**Text.** Read the zoom of ZM1-I1[a] as a measure-level block map of a Euclidean form of the law, comparing the same class-(a) data, as in `ZM1.md` line 65 ("Those stay open under Y1 and ZM1-G").

*Four tests.* (1) Pass. (2) Conditional: it needs a Euclidean form of the law (Y1, open). (3) Conditional: a Euclidean form with positive weights needs reflection positivity for the chosen update (ST1). (4) Conditional: it adds the Euclidean structure. **P C C C.** It is the setting of Balaban's RG and of the YM branch.

### 8.4 Changes that do not help (not offered)

- Dropping (Z-a): the proof of Theorem T′ then gives a bijection of site sets, and the map is a relabelling of the fine law with `L` only a name.
- (G1) for the `SU(5)` part only: Proposition Z5.
- Embedding sets of other sizes on `L5-U`: Proposition V.
- Any finite coarse register, fixed or growing, whose coarse neighbours share a trace-correlated link: Theorem G.

## FINISH

**Proved** (pass 1, unrefereed; every proof is written out above and uses no computation).
- Lemma T1: a unital *-homomorphism from the coarse algebra preserves the normalized trace. Lemma T2: under the fine trace, the `U(1)` Gauss charges of two sites that are not fine neighbours are independent. Lemma T3 and Corollary T3′: under the coarse trace, the charges of coarse neighbours have covariance `−m_1(10−m_1)/36`.
- Theorem T: on `L5-U`, (G1) at `T = 1` with singleton sets forces the representatives of coarse neighbours to be fine neighbours, and `m(10−m) = m_1(10−m_1)`.
- Lemma T5 and Theorem T′: with disjoint sets and (Z-a), the representative map is a bijection of site sets with bounded displacement, so `L = 1`.
- Corollary T″: on `L5-U[m]`, every `m`, no block map with (Z-a) and (G1) on singleton sets exists for `L ≥ 2`.
- Proposition V: on `L5-U`, (G1) with any finite sets forces `|S_X| = 1`. Proposition Z5: (G1) for traceless `T` alone gives Theorems T and T′.
- Lemma O1, Theorem O, Corollary O″: the same on `L5-O[S_+]`, through the Cartan torus element `exp(i(π/2)Σ_j \mathcal G^{2j−1,2j})`, coarse covariance `−2^{−35}`.
- Theorem G: the general form for finite registers with trace-correlated links (covers `L_cube`).
- Proposition 6.0 and Lemma DK (extending `GA1_5.md` Theorem 6.1): empty- or full-matter product vacua with the base tick are dark, hence trivial for class (a) under any finite-range block map. Proposition R2′: the non-factor E-witness of `VC1_5.md` R2 has the constant invariant tail `1/4`.

**Counterexamples.**
- **ZM1-I1[a] with `p = 2` is false as specified**, on `L5-U[m]` for every `m ∈ {1, …, 9}` and on `L5-O[S_+]`. For every VC1 vacuum, every admissible fine update (base tick, any GA1-P-5 member, any NN-a update), every coarse law of the same type, every coarse state and every `L ≥ 2`, no block map with (Z-a), (G1) and singleton disjoint sets exists. The same holds for every `p`, for ZM1-I1[O] in each class of `ZM1_OBS.md` §5, and for the original ZM1-I1 (`ZM1.md` line 363).
- **Named failing step:** (G1) at `T = 1`, "`Φ(G^{(1),1}_X) = G^1_{x_X}`", at a coarse link whose two representatives are not fine neighbours (on `L5-O`: (G1) on the five Cartan generators). Theorem T′ shows that (Z-a) and `L ≥ 2` force such a link.

**Open by name.**
- **G1-EQ** (section 8.1): existence of a block map with (G1-eq) in place of (G1), for some `L ≥ 2`, on either law.
- The owner's choice, if any, among R-G1EQ (P P C P), R-ISO (C C C C) and R-MEAS (P C C C), or another change.
- Inherited items are unchanged; none was worked here.

**What changes downstream.**
- `ZM1.md`: Definitions Z and G, read together with "a coarse law of the same type", have no instance with `L ≥ 2` on either five-mode law. ZM1-I1 is false as stated in every class. No frozen proof of `ZM1.md` changes: Z0's coarse system is not of the same type, and Z1-Z2 have no Gauss law. A dated amendment is for the lead.
- `ZM1_OBS.md`: the class-(a) specification, Lemma ER and Theorems 1-12 stand. The existence statements ZM1-I1[O] are false as stated on both laws.
- `TOE_ASSEMBLY.md` §3.8: the owner's text has no instance. The cause is (G1) with (Z-a), not the class or `p = 2`. Section 8 lists changes for the owner.
- Consumers of ZM1(a)1 through class (a): GA2's operator-side interface, LZ1-i[ZM1a] (`LZ1I.md`), the YM branch's H-BLOCK interface and ZM1-G. No homomorphic zoom of the specified kind exists to supply them. Under R-G1EQ the question becomes G1-EQ. Under R-MEAS it moves to Y1 and ZM1-G.
- First tests, for any change that keeps class (a) and finite-range maps: the dark vacua (`VC1_5.md` Theorem 5.2 at `t = ±∞`, Theorem 5.5) put the whole content in the block map; the R2 witness, the swap bands and the `LZ1I.md` vacua ask for exact matching of nonzero tails.
- Not changed: `docs/MINIMAL_AXIOMS_2026-06-29.md`, the working set, and every frozen part.
