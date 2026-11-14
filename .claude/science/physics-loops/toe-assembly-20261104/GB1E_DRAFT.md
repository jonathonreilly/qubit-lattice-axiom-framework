lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# GB1E: the Euclidean lift (H-4D) of the lattice gauge bridge, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of part GB1E (wall W1) under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-GB1E/`; a check guides and never proves.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `9001dd7d8` |
| `origin/claude/ym4d-hard-route` (read with `git show` only, after `git fetch -q origin claude/ym4d-hard-route`) | `5082c9928` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd0` |

Files read, by line. This folder: `prior/GB1E.md` (all, 85 lines); `GB1.md` (all, 231 lines, with Amendments 1-2); `GB1QL.md` (all, 364 lines); `GB1QL_REFEREE.md` (all, 281 lines); `TOE_ASSEMBLY.md` lines 13-23 (axioms), 201-266 (sections 3.4-3.10), 431-454 (GA2, GB1), 596-620 (section 6), 722-736 (section 11); `GA2_Y2.md` (all, 178 lines); `GA2_Y2_DRAFT.md` lines 205-215 (T0-start[G], T0-rate); `SMG1.md` lines 3-9, 23, 29-31, 96, 108-110, 149 (by grep for "R-GEN", "Lemma F", "generator"); `Y2W_DRAFT.md` lines 1-40 (head format). YM branch, `.claude/science/physics-loops/ym4d-hard-route-20261030/`: `GOAL.md` lines 20-48; `library/t0-tree.md` lines 1-60 (and grep hits at 13, 35-36, 247, 254, 264, 391); `library/port/p8-positivity.md` lines 26-145 (B5, its proof, the reflection form). `origin/main`, `docs/`: `GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md` lines 1-132; `AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md` lines 40-80; `SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md` lines 38-56. The YM branch's `library/lg1.md` and `library/ro1-vs-ca.md` were not read; they are cited only through `prior/GB1E.md`, and marked so where used.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The test law `L5[SU(2), s]` and the owner's bounded R-GEN are read plainly. Where the lane needs a generator, it specifies one (R-SUM, R-IA, section 9.2) and four-tests it; nothing is adopted.

**Working set used, by name.** None as a premise. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. PS-6r enters only through `GB1QL.md`'s proposed rung test law `L5[SU(2), s]` (not a working-set law). The owner decision SMG1-GAP = R-GEN, bounded (`TOE_ASSEMBLY.md` §3.10, scope SMG1 only) is used only to report what it would give if its scope were widened (Proposition 3.2, Corollary 5.3). Results used, by name: `GB1QL.md` section 1, Lemma 4.1, R2, Lemma 4.7, Proposition 4.11, Lemma H; `GB1.md` Theorems 2.1 and 2.3; `SMG1.md` Lemma G0; the YM branch's port of B5 (`p8-positivity.md`).

**Scratch.** `/tmp/toe-GB1E/check_hk.py`: one-dimensional sums on 2001 angles; under one second and a few MB; started at 56 percent free memory. No matrix was built.

---

## 0. The question, quoted

**The lane's target (brief, 2026-11-07).** "decide whether the framework (through GB1QL's quantum-link family and a stated generator reading) supplies a probability measure on links of a 4D lattice, gauge invariant, reflection positive and in a stated action class, whose transfer matrix is `e^{-a_0 H}` for the Hamiltonian `H` that GB1QL approaches; give the exact relation between that measure and T0's isotropic Wilson SU(2) action (anisotropy, coupling trajectory, Haar links), and say which T0-start hypotheses (H-4D, H-GI, H-Haar, H-RP, H-class) are then delivered, approximately delivered, or fail, naming the first failing step."

**The start class.** `GA2_Y2_DRAFT.md` line 211, T0-start[G]: "every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`".

**Why (H-4D) comes first.** `GB1QL.md` line 328, Lemma H: "(H-GI), (H-RP), (H-Haar) and (H-class) are properties of one object, the measure `μ` that (H-4D) asks for. (H-G) fixes the group. So a hand-off that supplies no `μ` supplies none of the four properties, and the first input it lacks, after (H-G), is (H-4D)." Line 335 gives the reason: "Theorem 4.8 is a real-time statement for a unitary tick on Z³. `GB1.md` Theorem 2.1 (F1-F2): a unitary tick is not a positive transfer, and the tick does not fix a Hermitian logarithm."

**What the tick does not fix.** `GB1.md` line 45, Theorem 2.1: "Each defines `T_H=e^{-H}>0` with `T_H^i=U`. The tick alone does not select this logarithm or its imaginary-time correlators." Line 67 names the inputs: "E-1 is a quasi-energy lift, E-2 a relation of the chosen state to it, E-3 a small-angle/time-continuum family joined to a Euclidean limit, and E-4 isotropy (Y3)."

**The one generator reading the owner has chosen.** `TOE_ASSEMBLY.md` line 261, for SMG1 only: "fix the certified gate decomposition as part of the supplied data. Write `g=e^{-iX_g}`, with `X_g=X_g^*` and `‖X_g‖<π`. Set `H_U=Σ_gX_g`". Its scope line: "SMG1's rungs only, not every TOE gap."

**The consumer's wording.** `TOE_ASSEMBLY.md` line 613, Y1: "The framework's SU(2) link sector, with the update as transfer, has a Euclidean representation on `Z^3 x Z` (or on D4 events) with a local, gauge-invariant action `S_fw`, reflection positive in time."

**T0's measure.** YM branch, `library/port/p8-positivity.md` lines 44-48 (at `5082c9928`): "Here `G=SU(N_col)`, the trace has `tr 1=1`, `a_p(U)=1-Re tr U(∂p)`, `A(U)=Σ_p a_p(U)`, `dμ=Z_bare^{-1}e^{-x_0A(U)}dU`, `x_0>0`." Its reflection positivity (P8.1) is for planes `{x_μ = c}` with `c ∈ εZ` while sites lie in `ε(Z+1/2)^4`: planes that contain no site, that is, link reflections, in each of the four coordinate directions.

## 0.1 Outcome in one paragraph

**Decided, with the answer depending on one reading.** The tick fixes no logarithm (`GB1.md` Theorem 2.1), so a generator reading is needed. Under the candidate reading **R-SUM** (the Hamiltonian of the tick is the sum of its written layer exponents, `H = τ_E Σ_ℓ E²_ℓ + θ Σ_C B_C`) with `τ_E > 0`, the answer is yes for the target and yes-in-the-limit for the framework. On every finite periodic 4D box and for every `a_0 > 0` there is a probability measure `μ_ex` on `SU(2)`-valued links whose transfer matrix is exactly `e^{-a_0H}`; it is gauge invariant, has a bounded density with respect to product Haar measure, and is link-reflection positive in all four directions (Theorems 4.10, 6.3). Its class `𝒜_FK` is stated: total-variation limits of coarse-grained local lifts. The tick itself, continued to imaginary angles, is exactly the transfer matrix of a local measure `μ_loc` with heat-kernel temporal plaquettes and Wilson weights on the cube-face spatial plaquettes, up to one positive constant `λ` (the Euclidean step in ticks) that the tick does not fix (Theorems 4.5, 5.1). The framework supplies these only as `s → ∞`: its own band-limited lifts converge to `e^{-a_0H}` in trace norm (Theorem 8.4) but are signed measures at every fixed `s` for small `a_0` (Theorem 8.2), and no finite register has a gauge-covariant positive basis (Lemma 8.3). **Relation to T0.** Same group and Haar links. The heat kernel is never a Wilson weight (Lemma 7.2). Neither lift is invariant under exchanging time with a space axis (Theorem 7.3 for `μ_loc` at every parameter; Theorem 7.5 for `μ_ex` outside a discrete set of `θ`), and `μ_loc` breaks odd translations. `λ` sets the anisotropy (tree level `ξ_cl ~ (λ²|θ|τ_E)^{-1/2}`); the tick fixes the tree-level coupling (`g_cl² → 2(τ_E/|θ|)^{1/2}`); T0's coupling trajectory needs a family of laws. **Hand-off.** (H-4D), (H-GI), (H-Haar), (H-RP) are delivered: exactly for the target's lifts, approximately (as `s → ∞`) for the framework. **The first failing step is (H-class), at invariance under the exchange of time with a space axis**, provided `𝒜_{k_0}(g)` consists of hypercubic-invariant densities, as every class generated from T0's Wilson start does; the frozen `GA2_Y2.md` line 178 already lists anisotropy as a separate extension of T0. **Under the owner's bounded R-GEN**, if its scope were widened to GB1, the generator is bounded and the first failing step stays (H-4D), at the partition function (Theorem 5.2). Through the framework's own registers at fixed `s`, the first failing step is (H-4D), at positivity of the transfer kernel (Theorem 8.2).

## 1. Prior work used

Each item was used or extended; paths are relative to this folder unless marked.

- **`GB1QL.md`** (frozen). Section 1 (the link space `𝒦`, `H_k`, `E²`, the family `R_s`, `U_s`, the plaquette `X_p`, `B_p`, both ticks, the embedding `ι`): the setting of sections 3 and 8. Lemma 4.1 (harmonic calculus) and R2 (density of `⊕H_k`): used in Lemmas 4.1, 4.2 and 7.1. Lemma 4.7, plaquette step: the strong convergence in Theorem 8.4. Proposition 4.11(a): (H-G). Lemma H and the hand-off table (lines 328-343): extended by section 9, which supplies the measure Lemma H asks for and moves the first failure.
- **`GB1.md`** (frozen). Theorem 2.1 (F1-F2): the reason a reading is needed (section 3.2). Theorem 2.3 (F4, the Z₂ transfer identity "at real and imaginary angles"): extended to `SU(2)` with the heat-kernel temporal weight (Theorems 4.5 and 5.1). Line 31 (the cube-face parity description): Lemma 6.1 rebuilds it. Line 67 (E-1 to E-4) and line 209 ("the Wilson transfer is the tick at imaginary angles, which is not law data"): Theorem 5.1(c) makes the missing datum exact, one positive constant `λ`. Row H5: the coupling trajectory (section 7.3).
- **`GA2_Y2.md`** (frozen). Line 178 (the class is not pinned; "anisotropy and matching are separate extensions"): the (H-class) row. Line 176 ("a band-limited kernel is not automatically a positive probability density"): Theorem 8.2 shows that the framework's band-limited transfer kernels are in fact not positive in the Hamiltonian regime.
- **`GA2_Y2_DRAFT.md`** line 211 (T0-start[G]): the hypotheses tested.
- **`SMG1.md`** Lemma G0 (principal generator, line 29) and **`TOE_ASSEMBLY.md`** §3.10 (bounded R-GEN): Proposition 3.2 and Corollary 5.3.
- **YM branch**, `library/port/p8-positivity.md` (B5, ported there from Sussman–Alpoge CA-II `6.1:lem-reflection-positivity`): its crossing-kernel proof (P8.3)-(P8.6) is generalized to the class `𝒫` in Lemma 6.2. Its statement "the Wilson measure is invariant under every torus isometry preserving the bare lattice" is used in Theorem 7.3(c) and section 9.1. `GOAL.md` lines 20-48 (T0, T1) and `library/t0-tree.md` (the Wilson start of the T0 tree): section 7.3.
- **`origin/main`, `docs/AXIOM_FIRST_REFLECTION_POSITIVITY_WILSON_TEMPORAL_GAUGE_BRIDGE_NARROW_THEOREM_NOTE_2026-06-05.md`** (unaudited): "The character coefficients of `k_beta` are nonnegative" and "Products of these kernels over finitely many spatial links are positive semidefinite" (lines 54 and 59-60). Lemma 4.4 and Lemma 6.2 use the same mechanism for the heat kernel and the cube-face Wilson weight; credited, rebuilt.
- **`origin/main`, `docs/GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md`** (unaudited; one SU(3) cube): the anisotropic Wilson transfer tends to `e^{-tH}` strongly. Context for section 7.3, item 5; not used in a proof. Theorem 4.9 here is the heat-kernel analogue in trace norm, on a box, for `SU(2)`.
- **`origin/main`, `docs/SPATIAL_CUBIC_TIME_ANISOTROPY_GATE_NO_GO_2026-06-06.md`** (unaudited): "Spatial cubic symmetry allows `c_t != c_s`" (line 47). Theorems 7.3 and 7.5 are measure-level instances for the lifts.
- **YM branch `library/lg1.md` Theorem 13 and `library/ro1-vs-ca.md`**, through `prior/GB1E.md` only (not read here): the set of mirrors LG1 proves for the isotropic Wilson measure, and the anisotropic countermodels with axis RP and no O(4). Section 6.3 states which of these mirrors the lifts have.

**Prior work the digest missed.** `SMG1.md` Lemma G0 (needed to say what bounded R-GEN gives on a gate); `GB1.md` line 31 (the parity description of the cube-face set, on which the spatial reflection positivity rests); and `GB1QL.md` Lemma 4.7's plaquette step as the input for a Euclidean regulator limit (the digest names `GB1QL.md` only for its real-time rates).

**Failed attempts on file, and what is new here.** The digest's "literal tick-as-positive-transfer" failure (`GB1.md` line 45) is not repeated: the transfer matrices here are the tick's layers at imaginary angles (Theorem 5.1) or `e^{-a_0H}` under a stated reading, never the unitary tick. The digest's "slice covariance promoted to measure properties" failure (`GB1QL_REFEREE.md` line 100) is avoided: every property in section 9 is proved for a measure.

## 2. Literature read

Searched 2026-11-07 with WebSearch; arXiv abstract pages fetched with WebFetch. Nothing below is load-bearing: every step used later is rebuilt in sections 4-9. "NOT VERIFIED" means the text itself was not fetched; only its bibliographic record or a secondary description was seen.

| Work | What was checked | What this file takes from it |
|---|---|---|
| M. Carena, H. Lamm, Y.-Y. Li, W. Liu, "Lattice Renormalization of Quantum Simulations", arXiv:2107.01166v2, Phys. Rev. D 104, 094519 | Abstract; ar5iv text of Sec. II-III. Eq. (9) splits the transfer matrix "symmetrically" as `T_V^{1/2} T_K T_V^{1/2}`; Eq. (18) defines `T(a_0) ≡ exp(−a_0 H(a, a_0))`, "it can be used to define a Hamiltonian"; Sec. II: with "a heat-kernel kinetic term (the Laplace-Beltrami operator)", "the higher order ω terms vanish and the mapping is exact"; Eq. (31): `δ_τ → iδ_t` turns the Euclidean transfer matrix into the Trotterized evolution. | Credit for the observation behind Theorem 4.5: the heat-kernel temporal weight makes the Euclidean transfer matrix an exact symmetric Trotter product, and the Trotterized tick is its analytic continuation. Theorems 4.5 and 5.1 prove this natively for the cube-face SU(2) model, with gauge projection, positivity and Haar density. |
| G. Kanwar, M. L. Wagman, "Real-time lattice gauge theory actions: unitarity, convergence, and path integral contour deformations", arXiv:2103.02602v3, Phys. Rev. D 104, 014513 | Abstract; ar5iv Sec. II.2 ("Although it is formally possible to construct a unitary time evolution operator for LGT through analytic continuation") and Sec. III.2 (the Kogut-Susskind kinetic term "can be recognized as the quadratic Casimir operator (up to a sign)"). The heat-kernel action's displayed formula was cut off in the fetched text. | Context for the real-time/Euclidean relation of section 5. Not used in a proof. |
| M. Carena, E. J. Gustafson, H. Lamm, Y.-Y. Li, W. Liu, "Gauge Theory Couplings on Anisotropic Lattices", arXiv:2208.10417v1, Phys. Rev. D 106, 114504 | Abstract only: perturbative bare-to-renormalized relations "at any anisotropy factor", for U(N) and SU(N). | Context for the anisotropy renormalization in section 7. Not used in a proof. |
| T. M. R. Byrnes, M. Loan, C. J. Hamer et al., "The Hamiltonian limit of (3+1)D SU(3) lattice gauge theory on anisotropic lattices", arXiv:hep-lat/0311014v1, Phys. Rev. D 69, 074509 | Abstract: results show "the universality between the Hamiltonian and Euclidean formulations of lattice gauge theory" (numerical). | Context only: universality between anisotropic and Hamiltonian forms is numerical evidence, not a theorem. |
| C. J. Hamer, M. Sheppeard, Z. Weihong, D. Schutte, "Universality for SU(2) Yang-Mills Theory in (2+1)D", arXiv:hep-th/9511179v1, Phys. Rev. D 54, 2395 | Abstract: "A striking demonstration of universality between the Hamiltonian and Euclidean formulations is obtained." | Same as above. |
| S. Chandrasekharan, U.-J. Wiese, "Quantum link models: A discrete approach to gauge theories", arXiv:hep-lat/9609042, Nucl. Phys. B 492 (1997) 455 | Abstract: link matrix elements are "non-commuting operators acting in a Hilbert space"; with "a fifth Euclidean dimension", dimensional reduction to four dimensions is argued from universality. | Credit for the `so(5)` link (already credited in `GB1QL.md`). Its Euclidean route adds a fifth dimension; this file does not use it (section 9). |
| A. Jaffe, "Reflection Positivity Then and Now", arXiv:1802.07880v1 | Abstract: a review, with "a new geometric approach and proof of the reflection positivity property". | Context for section 6. |
| M. Creutz, "Gauge fixing, the transfer matrix, and confinement on a lattice", Phys. Rev. D 15, 1128 (1977) | OSTI record 7118049, abstract: "Taking the timelike lattice spacing to zero, we extract the Kogut-Susskind Hamiltonian from the transfer matrix in the gauge A/sub 0/ = 0." Full text NOT VERIFIED. | Credit for the transfer-matrix method of Theorem 4.5 (temporal gauge, gauge projection). |
| M. Lüscher, "Construction of a selfadjoint, strictly positive transfer matrix for Euclidean lattice gauge theories", Commun. Math. Phys. 54, 283 (1977) | Bibliographic record and a first-page excerpt seen through search ("the operator e^(−aH)"; "we must make sure that T>0"). Full text NOT VERIFIED (Hamburg copy returned 403). | Credit for positivity of the Wilson transfer matrix; section 7 uses only the native statement. |
| K. Osterwalder, E. Seiler, "Gauge field theories on a lattice", Ann. Phys. 110, 440 (1978) | Bibliographic record only (Scilit, DOI 10.1016/0003-4916(78)90039-8). NOT VERIFIED. | Credit for link-reflection positivity of lattice gauge measures; Lemma 6.2 is rebuilt natively, following the route the YM branch ports in `p8-positivity.md`. |
| E. Seiler, *Gauge Theories as a Problem of Constructive Quantum Field Theory and Statistical Mechanics*, Lecture Notes in Physics 159 (1982) | Library records only. NOT VERIFIED. | Credit only. |
| J. Kogut, L. Susskind, "Hamiltonian formulation of Wilson's lattice gauge theories", Phys. Rev. D 11, 395 (1975) | Bibliographic record (DOI 10.1103/PhysRevD.11.395). NOT VERIFIED. | Credit for the Hamiltonian `H = (g²/2)ΣE² − (1/g²)ΣRe Tr U_p` form. |
| F. Karsch, "SU(N) gauge theory couplings on asymmetric lattices", Nucl. Phys. B 205, 285 (1982) | Bibliographic record only. NOT VERIFIED. | Credit for the one-loop anisotropy relations named in section 7. |
| P. Menotti, E. Onofri, "The action of SU(N) lattice gauge theory in terms of the heat kernel on the group manifold", Nucl. Phys. B 190, 288 (1981) | Bibliographic record and a secondary description (a one-plaquette action whose exponential solves the heat equation on the group). NOT VERIFIED. | Credit for the heat-kernel action used in Theorem 4.5. |
| E. Fradkin, L. Susskind, "Order and disorder in gauge systems and magnets", Phys. Rev. D 17, 2637 (1978) | Bibliographic record and abstract fragments (a limit "in which the time direction becomes continuous"). NOT VERIFIED. | Credit for the time-continuum limit of transfer matrices (the Z₂ case is `GB1.md` F4). |

**What the literature does not supply.** No fetched text states, for the Trotterized cube-face SU(2) tick of `GB1QL.md`, a Euclidean measure with all of: exact transfer matrix `e^{-a_0H}`, gauge invariance, Haar density, link-reflection positivity in all four directions. No fetched text compares such a measure with a finite quantum-link register at the level of a positive kernel. Universality between anisotropic and isotropic actions appears only as numerical evidence (hep-lat/0311014, hep-th/9511179) and one-loop perturbation theory (Karsch; arXiv:2208.10417).

## 3. The Hamiltonian GB1QL approaches

### 3.1 The slice space and the operators

All objects of this subsection are those of `GB1QL.md` section 1, on a finite box. `GB1QL.md` line 37: "`𝒦 = L²(S³, σ)` ... So `𝒦` is the Kogut-Susskind link space `L²(SU(2))`." Line 39: "`H_k` is the space of their restrictions to `S³`"; line 41: "`E² = k(k+2)/4 = j(j+1)` on `H_k`". Line 44 (R2): "`𝒦 = ⊕̂_k H_k`". Line 66: "`X_p = U_{ℓ_4}^* U_{ℓ_3}^* U_{ℓ_2} U_{ℓ_1}` ..., `B_p = tr X_p + (tr X_p)^*`, `B_C = Σ_{p ⊂ C} B_p`".

- **Box.** `Λ = (Z/NZ)³` with `N ≥ 4` even. `𝓛` is its set of oriented links `ℓ = (x, x+e_i)`. A **slice configuration** is `U ∈ SU(2)^𝓛`. The slice space is `𝒦_𝓛 = L²(SU(2)^𝓛, dU) = ⊗_ℓ 𝒦`, with `dU` the product of normalized Haar measures. Here `g(x) = x_4 + i x·σ` identifies `S³` with `SU(2)` (`GB1QL.md` line 37); I write `g` for both.
- **Gauge action.** For `h ∈ SU(2)^Λ` put `(h·U)_{(x,y)} = h_y^{-1} U_{(x,y)} h_x` and `(R(h)f)(U) = f(h·U)`. `R` is a unitary action (Haar is invariant). `P_0 = ∫ R(h) dh` is the orthogonal projection onto gauge-invariant functions.
- **Electric operator.** `A = Σ_ℓ E²_ℓ ≥ 0`. Its eigenspaces are `⊗_ℓ H_{k_ℓ}`, with eigenvalue `Σ_ℓ k_ℓ(k_ℓ+2)/4`, each of finite dimension. For `u > 0`, `Tr e^{-uA} = Θ(u)^{|𝓛|}` with `Θ(u) = Σ_{k≥0} (k+1)² e^{-uk(k+2)/4} < ∞`.
- **Cube-face set.** `CF` is the set of plaquettes that are faces of tiling cubes. `GB1.md` line 31: "Its plaquettes are exactly those whose two in-plane base parities agree: half the plaquettes in each plane." Lemma 6.1 rebuilds this and the reflection property used later.
- **Magnetic potential.** `V_θ = θ Σ_{C} B_C = θ Σ_{p∈CF} B_p`. On `𝒦_𝓛`, `B_p = 2 Tr X_p` is multiplication by a real smooth gauge-invariant function with values in `[-4, 4]` (`GB1QL.md` line 190: "`tr X_p` is multiplication by a real function, so `B_p = 2 tr X_p` on `𝒦`"). So `V_θ` is bounded, `‖V_θ‖ ≤ 4|θ| |CF|`.
- **Target Hamiltonian.** `H = τ_E A + V_θ` on `D(A)`, with the tick's angles `θ, τ_E ∈ R`.

**Lemma 3.1.** Let `τ_E > 0`.
(a) `H` is self-adjoint on `D(A)`, bounded below by `−‖V_θ‖`, and commutes with every `R(h)`.
(b) `H` has compact resolvent. Its eigenvalues `μ_1 ≤ μ_2 ≤ …` (with multiplicity) satisfy `μ_i ≥ τ_E α_i − ‖V_θ‖`, where `α_1 ≤ α_2 ≤ …` are those of `A`.
(c) For `u > 0`, `Tr e^{-uH} ≤ e^{u‖V_θ‖} Θ(uτ_E)^{|𝓛|} < ∞`.
(d) If `τ_E < 0`, `e^{-uH}` is unbounded for every `u > 0`. If `τ_E = 0`, `Tr(P_0 e^{-uH}) = ∞` for every `u > 0`.

*Proof.* (a) `V_θ` is bounded and symmetric, so `τ_E A + V_θ` is self-adjoint on `D(A)` (a bounded symmetric perturbation of a self-adjoint operator is self-adjoint on the same domain: `(H − z)^{-1}` exists for `|Im z| > ‖V_θ‖` by the Neumann series below). `E²` is a Casimir (`GB1QL.md` line 41), so `A` commutes with `R(h)`; `V_θ` is multiplication by a gauge-invariant function (`GB1QL.md` line 68: "its trace is invariant").
(b) For real `z < −‖V_θ‖`, `‖V_θ(τ_EA − z)^{-1}‖ ≤ ‖V_θ‖/|z| < 1`, so `(H − z)^{-1} = (τ_EA − z)^{-1}(1 + V_θ(τ_EA − z)^{-1})^{-1}`. The first factor is compact (`A` has finite-dimensional eigenspaces and eigenvalues tending to infinity), so the resolvent is compact. For a self-adjoint operator bounded below with compact resolvent, the min-max formula holds: `μ_i = min_{S} max_{x ∈ S, ‖x‖=1} ⟨x, Hx⟩` over `i`-dimensional subspaces `S ⊂ D(A)`. (Proof: expand `x` in an orthonormal eigenbasis; the span of the first `i` eigenvectors attains the minimum, and every `i`-dimensional `S` meets the closed span of the eigenvectors `i, i+1, …`.) Since `⟨x, Hx⟩ ≥ τ_E⟨x, Ax⟩ − ‖V_θ‖`, the same formula for `A` gives the bound.
(c) Sum `e^{-uμ_i} ≤ e^{u‖V_θ‖} e^{-uτ_Eα_i}` over `i`.
(d) If `τ_E < 0`, take unit `f ∈ H_k ⊗ (⊗_{ℓ'≠ℓ} H_0)`: `⟨f, Hf⟩ ≤ τ_E k(k+2)/4 + ‖V_θ‖ → −∞`, so `H` is unbounded below and `e^{-uH}` is unbounded. If `τ_E = 0`, `H = V_θ` is bounded and `e^{-uH} ≥ e^{-u‖V_θ‖}`. The gauge-invariant subspace `P_0𝒦_𝓛` is infinite-dimensional: for one plaquette `p`, the functions `(Tr X_p)^n`, `n ≥ 0`, are gauge invariant and linearly independent, since `Tr X_p` takes every value in `[−2, 2]`. So `Tr(P_0 e^{-uH}) ≥ e^{-u‖V_θ‖} dim P_0𝒦_𝓛 = ∞`. □

### 3.2 Two readings of "the Hamiltonian of the tick"

`GB1QL.md` line 70 fixes the target tick: "The **Kogut-Susskind tick** is `U_KS = W_B W_E` with `W_B = ∏_{C∈𝒞} g_C`, `g_C = e^{−iθ B_C}`, and `W_E = ∏_ℓ e^{−iτ_E E²_ℓ}`." The framework tick `U_{(s)}` is "the same formula with `U_s` and `R_s` in place of `U` and `𝒦`". The tick fixes no logarithm (`GB1.md` Theorem 2.1). Two readings supply one.

- **R-SUM (candidate, this file).** "The Hamiltonian of a tick written as an ordered product of layers `e^{-iτ_k K_k}`, with `K_k` the operators named in the law's data, is `Σ_k τ_k K_k`." For `U_KS` it gives `H = τ_E A + V_θ`. For `U_{(s)}` it gives `H_s = τ_E Σ_ℓ E²_ℓ + θ Σ_C B^s_C` on `R_s^{⊗𝓛}`.
- **Bounded R-GEN (owner, 2026-11-07, scope SMG1 only).** Read with its scope widened to GB1, it takes the principal generator `X_g` of each gate, `‖X_g‖ < π`.

**Proposition 3.2 (what bounded R-GEN gives).** Let `τ_E > 0`, `24|θ| < π`, and `τ_E/π` irrational. Put `w(x) = x − 2π⌊(x+π)/(2π)⌋ ∈ [−π, π)`.
(a) Every gate of `U_KS` and of `U_{(s)}` has a principal generator. For `U_KS` the sum is `H_wr = V_θ + Σ_ℓ w(τ_E E²_ℓ)`, a bounded operator with `‖H_wr‖ ≤ ‖V_θ‖ + π|𝓛|`.
(b) For `U_{(s)}` the sum equals R-SUM's `H_s` if and only if `τ_E s(s+2)/4 < π`.
(c) `H_wr` and `H` agree on vectors whose every link flux `k` has `τ_E k(k+2)/4 < π`, and differ on every `H_k`-component with `τ_E k(k+2)/4 ≥ π`. In particular `H_wr ≠ H`: one is bounded, the other is not.

*Proof.* `SMG1.md` line 29, Lemma G0: "A Hermitian `X` with `g = e^{−iX}` and `‖X‖ < π` exists if and only if `−1 ∉ spec g`. It is then unique." (a) `‖θB_C‖ ≤ 24|θ| < π` (`GB1QL.md` line 209: "`‖B_C‖ ≤ 24`"), so `X = θB_C` by uniqueness. The electric gate is `Σ_k e^{−iτ_E k(k+2)/4} Π_k` on each link. Its eigenvalue `−1` would need `τ_E k(k+2)/4 = (2m+1)π`, so `τ_E/π = 4(2m+1)/(k(k+2))` rational; hence there is no `−1`, and `X = Σ_k w(τ_E k(k+2)/4) Π_k`. The norm bound is termwise. On `R_s`, `‖θB^s_C‖ ≤ 24|θ|` too (`GB1QL.md` line 209: "`‖B̃_C‖ ≤ 24`"). (b) On `R_s` the flux is at most `s`, and the values `τ_E k(k+2)/4` increase in `k`. `w(x) = x` for `x ∈ [0, π)`, and `w(x) ≠ x` for `x ≥ π` because `w(x) < π`. (c) The same two facts, on each link. □

So bounded R-GEN never returns the Kogut–Susskind electric term: its generator is bounded, while `τ_E A` is not. On the framework side it agrees with R-SUM exactly while the register is small enough that no electric phase wraps.

### 3.3 Euclidean lifts

**Definition 3.3 (transfer-kernel measure).** Fix `N_t ≥ 2` even. The **time-torus configuration space** is `Ω = SU(2)^{𝓛 × Z_{N_t}} × SU(2)^{Λ × Z_{N_t}}`: spatial links `U_{ℓ,t}` and temporal links `V_{x,t}` from `(x,t)` to `(x,t+1)`, with product Haar measure. Let `T` be a bounded operator on `𝒦_𝓛` with a measurable kernel `κ ≥ 0` (`(Tf)(U) = ∫ κ(U,U') f(U') dU'`). If
`0 < Z = ∫_Ω ∏_{t} κ(U_t, V_t·U_{t+1}) dU dV < ∞`,
the probability measure `μ_T = Z^{-1} ∏_t κ(U_t, V_t·U_{t+1}) dU dV` is the **Euclidean lift of `T`** with `N_t` slices. `T` is its **transfer matrix**. This is (H-4D) in its plain sense: a probability measure on `SU(2)`-valued links of the 4D periodic lattice `Λ × Z_{N_t}`, with a density with respect to product Haar measure.

**Lemma 3.4 (trace form).** Let `T` be as in Definition 3.3, commuting with every `R(h)`, with `κ` bounded. Then `Z = Tr(P_0 T^{N_t})`. For bounded measurable `F_1, …, F_{N_t}` on `SU(2)^𝓛`, acting by multiplication, `E_{μ_T}[∏_t F_t(U_t)] = Tr(F_1 TP_0 F_2 TP_0 ⋯ F_{N_t} TP_0)/Z`. If the `F_t` are gauge invariant, this is `Tr(P_0 F_1 T F_2 T ⋯ F_{N_t} T)/Z`.

*Proof.* Substituting `U' ↦ h·U'` (Haar invariant), `T R(h)` has kernel `κ(U, h^{-1}·U')`. So `TP_0` has the bounded kernel `κ_0(U,U') = ∫ κ(U, h·U') dh`. Integrating the `V_t` first (Fubini; all integrands are nonnegative or bounded), `Z = ∫ ∏_t κ_0(U_t, U_{t+1}) dU`. A bounded kernel on a probability space defines a Hilbert–Schmidt operator. The kernel of a product of two Hilbert–Schmidt operators is the integral of the kernels, and `Tr(BC) = ∫∫ B(x,y) C(y,x)` for Hilbert–Schmidt `B, C` (Parseval in `L²` of the product space). Apply these to the cyclic product of the `N_t ≥ 2` factors `F_t TP_0` (bounded kernels `F_t(U)κ_0(U,U')`). This gives the formula for the expectation, and with `F_t = 1` and `P_0T = TP_0`, `Z = Tr((TP_0)^{N_t}) = Tr(P_0T^{N_t})`. Gauge-invariant `F_t` commute with `P_0`, which gives the last form. □

## 4. The measure

### 4.1 The heat kernel on SU(2), rebuilt in GB1QL's harmonic calculus

**Lemma 4.1 (zonal kernels are characters).** For `k ≥ 0` let `φ_1, …, φ_{(k+1)²}` be an orthonormal basis of `H_k` and `Z_k(x,y) = Σ_a φ_a(x) \overline{φ_a(y)}`, the kernel of `Π_k`. Then:
(a) `Z_k` does not depend on the basis, and is real and symmetric.
(b) `Z_k(x,y) = z_k(xy^{-1})` (group product), for a real continuous class function `z_k`.
(c) `z_k(e) = (k+1)²` and `|z_k| ≤ (k+1)²`.
(d) `z_k = χ_{L_k}`, the character of the unitary representation `L_k(h)f(x) = f(h^{-1}x)` of `SU(2)` on `H_k`.

*Proof.* (a) `Z_k` is the kernel of the projection `Π_k`. `H_k` is closed under complex conjugation (the conjugate of a harmonic homogeneous polynomial is one, of the same degree), so a real orthonormal basis exists. (b) `GB1QL.md` line 37: "Left and right multiplication on `SU(2)` act on `x` by rotations", and line 91: "rotations preserve every `H_k`". Rotations act unitarily on `𝒦` (`σ` is invariant), so they carry orthonormal bases of `H_k` to orthonormal bases, and by (a) `Z_k(hx, hy) = Z_k(xh, yh) = Z_k(x,y)`. Put `z_k(g) = Z_k(g, e)`. Then `Z_k(x,y) = Z_k(xy^{-1}, e)`, and `z_k(hgh^{-1}) = Z_k(hg, h) = z_k(g)`. (c) `Z_k(x,x) = z_k(e)` is constant, and `∫ Z_k(x,x) dσ = Σ_a ‖φ_a‖² = dim H_k = (k+1)²` (`GB1QL.md` line 54: "`dim R_s = Σ_{k≤s}(k+1)²`"). Cauchy–Schwarz in `a` gives `|Z_k(x,y)|² ≤ Z_k(x,x) Z_k(y,y)`. (d) `L_k` is unitary since left translation is a rotation preserving `H_k`. `Tr L_k(h) = Σ_a ∫ \overline{φ_a(x)} φ_a(h^{-1}x) dσ(x) = ∫ Z_k(h^{-1}x, x) dσ(x) = z_k(h^{-1})`, and `z_k(h^{-1}) = Z_k(e, h) = Z_k(h, e) = z_k(h)` by symmetry. □

No Peter–Weyl theorem or Schur orthogonality is used: `L_k` need not be irreducible for what follows.

**Lemma 4.2 (heat kernel).** For `t > 0` put `k_t = Σ_{k≥0} e^{-tk(k+2)/4} z_k`.
(a) The series converges absolutely and uniformly. `k_t` is a real continuous class function, `k_t(g^{-1}) = k_t(g)`, `∫ k_t dσ = 1`, and `(e^{-tE²}f)(x) = ∫ k_t(xy^{-1}) f(y) dσ(y)` for `f ∈ 𝒦`.
(b) `k_t ≥ 0`, and `k_t > 0` on a neighbourhood of `e`.

*Proof.* (a) `|z_k| ≤ (k+1)²` and `Σ_k (k+1)² e^{-tk(k+2)/4} < ∞`. By R2 (`GB1QL.md` line 44) and Lemma 4.1(b) of `GB1QL.md`, `e^{-tE²} = Σ_k e^{-tk(k+2)/4} Π_k`, and `Π_k` has kernel `z_k(xy^{-1})`; uniform convergence lets the sum pass the integral. `∫ z_k dσ = (Π_k 1)(e) = δ_{k0}`. Symmetry of `Z_k` gives `k_t(g^{-1}) = k_t(g)`.
(b) *Step 1 (polynomials, maximum principle).* Let `f` be the restriction to `S³` of a real polynomial of degree `d`, with `f ≥ 0` on `S³`. By the induction in R2, `f ∈ ⊕_{k≤d} H_k`. So `u(t,x) = (e^{-tE²}f)(x) = Σ_{k≤d} e^{-tk(k+2)/4}(Π_kf)(x)` is a finite sum, smooth on `[0,∞) × S³`, with `u(0,·) = f`. On each `H_k`, `Σ_{μ<ν} L²_{μν} = k(k+2)` (`GB1QL.md` Lemma 4.1(b)) and `L_{μν} = −iD_{μν}`, so `∂_t u = −E²u = ¼ Σ_{μ<ν} D²_{μν} u`. Fix `ε > 0` and put `w = u + ε(1+t)`, so `w(0,·) ≥ ε`. Suppose `w ≤ 0` somewhere. By continuity and compactness, `t_* = inf{t : min_x w(t,x) ≤ 0}` is positive, and `w(t_*, x_*) = 0 = min_x w(t_*, x)` for some `x_*`. Then `w(t, x_*) > 0` for `t < t_*`, so `∂_t w(t_*, x_*) ≤ 0`. For the rotations `R_r = exp(r(𝔢_{μν} − 𝔢_{νμ}))` of `GB1QL.md` line 123, `(d/dr) f(R_r x) = −(D_{μν} f)(R_r x)`, so `D²_{μν}w(t_*, x_*) = (d²/dr²) w(t_*, R_r x_*)|_{r=0} ≥ 0`, because `r ↦ w(t_*, R_r x_*)` has a minimum at `0`. Hence `∂_t w(t_*, x_*) = ¼ Σ D²_{μν} w + ε ≥ ε > 0`, a contradiction. So `w > 0`; letting `ε → 0`, `u ≥ 0`.
*Step 2 (continuous `f ≥ 0`).* By Stone–Weierstrass (as in R2), real polynomials `p_n` converge uniformly to `√f`; then `p_n² ≥ 0` converge uniformly to `f`, and `|e^{-tE²}(p_n² − f)| ≤ ‖k_t‖_∞ ‖p_n² − f‖_∞`. So `e^{-tE²} f ≥ 0` pointwise.
*Step 3 (the kernel).* If `k_t(g_0) < 0`, continuity gives a neighbourhood `N` of `g_0` with `k_t < 0` on `N`. Take continuous `f ≥ 0`, supported in `N`, with `∫ f > 0`. Then `(e^{-tE²}f)(e) = ∫ k_t(y^{-1}) f(y) dσ = ∫ k_t(y) f(y) dσ < 0`, contradicting Step 2. Finally `k_t(e) = Σ_k (k+1)² e^{-tk(k+2)/4} > 0`, and `k_t` is continuous. □

`[check]` (`/tmp/toe-GB1E/check_hk.py`, floating point, under one second, a few MB; started at 56 percent free memory): on 2001 rotation angles `ψ ∈ (0, π)`, with `z_k(ψ) = (k+1) sin((k+1)ψ)/sin ψ` (Lemma 7.1) and the series truncated at `k = 400`, the minimum of `k_t` is `−6.4·10^{-12}` at `t = 0.05`, `−8.7·10^{-13}` at `t = 0.2` (roundoff near the antipode, where `k_t` is of order `e^{-π²/t}`), `8.8·10^{-3}` at `t = 1` and `0.80` at `t = 4`; `∫ k_t dσ = 1.000000` in all four cases. The same script checks the orthogonality `∫ z_j z_k dσ = δ_{jk}(k+1)²` for `j, k < 6` (error `7·10^{-10}`). A guide only.

### 4.2 Positive character weights

**Definition 4.3 (class `𝒫`).** A continuous class function `φ` on `SU(2)` is in `𝒫` if `φ = Σ_q a_q χ_{R_q}` with `a_q ≥ 0`, `R_q` finite-dimensional unitary representations of dimensions `d_q`, and `Σ_q a_q d_q^m < ∞` for every `m ≥ 1`.

**Lemma 4.4.** (i) `1 ∈ 𝒫`. (ii) For `β ≥ 0`, `e^{β Tr g} ∈ 𝒫`. (iii) For `t > 0`, `k_t ∈ 𝒫`.

*Proof.* (i) The trivial representation. (ii) `Tr g = χ_{C²}(g)` and `χ_R χ_{R'} = χ_{R⊗R'}`, so `e^{β Tr g} = Σ_q (β^q/q!) χ_{(C²)^{⊗q}}`, with `d_q = 2^q` and `Σ_q (β^q/q!) 2^{qm} = e^{β 2^m}`. This is the expansion (P8.3) of `p8-positivity.md` with `R = V` (for `SU(2)`, `Tr g` is real). (iii) Lemma 4.1(d) and 4.2(a): `a_k = e^{-tk(k+2)/4}`, `R_k = L_k`, `d_k = (k+1)²`, and `Σ_k e^{-tk(k+2)/4}(k+1)^{2m} < ∞`. □

### 4.3 The local lift

Fix `β_s ∈ R` and `t_E > 0`. On `Ω` (Definition 3.3) let the plaquette holonomies be: for a spatial plaquette `p` at slice `t`, `X_p(U_t)` (`GB1QL.md` line 66); for a spatial link `ℓ = (x,y)` at slice `t`, the temporal plaquette
`W_{ℓ,t} = V_{x,t}^{-1} U_{ℓ,t+1}^{-1} V_{y,t} U_{ℓ,t}`.
Under a 4D gauge transformation `h_{x,t}` with `U_{ℓ,t} ↦ h_{y,t} U_{ℓ,t} h_{x,t}^{-1}` and `V_{x,t} ↦ h_{x,t+1} V_{x,t} h_{x,t}^{-1}`, each holonomy is conjugated (`W_{ℓ,t} ↦ h_{x,t} W_{ℓ,t} h_{x,t}^{-1}`).

**The action class `𝒜_HK`.** The **local lift** `μ_loc[β_s, t_E]` has density with respect to product Haar measure
`ρ_loc = Z^{-1} ∏_t ∏_{p∈CF} e^{β_s Tr X_p(U_t)} ∏_{t} ∏_{ℓ} k_{t_E}(W_{ℓ,t})`.
Its plaquette weights are: `e^{β_s Tr}` on cube-face spatial plaquettes; `1` on the other spatial plaquettes; the heat kernel `k_{t_E}` on every temporal plaquette. This is a heat-kernel action in time (Menotti–Onofri; Drouffe; credited in section 2) with a cube-face Wilson action in space.

**Theorem 4.5 (local lift; the SU(2) form of `GB1.md` F4).** Put `H_B = Σ_C B_C`, `M = e^{(β_s/4)H_B}` (multiplication by a positive function) and
`T_loc = M e^{-t_E A} M`.
(a) `T_loc` is bounded, positive and injective, commutes with every `R(h)`, and has the bounded continuous kernel `κ(U,U') = M(U) ∏_ℓ k_{t_E}(U_ℓ U'^{-1}_ℓ) M(U') ≥ 0`.
(b) `ρ_loc = Z^{-1} ∏_t κ(U_t, V_t·U_{t+1})`. So `μ_loc` is the Euclidean lift of `T_loc` (Definition 3.3), `Z = Tr(P_0 T_loc^{N_t}) > 0`, and Lemma 3.4 holds.
(c) `ρ_loc` is invariant under every 4D gauge transformation.

*Proof.* (a) By Lemma 4.2, `e^{-t_EA} = ⊗_ℓ e^{-t_E E²_ℓ}` has kernel `∏_ℓ k_{t_E}(U_ℓ U'^{-1}_ℓ) ≥ 0`, bounded and continuous. It is positive and injective (eigenvalues `e^{-t_E α} > 0`). `M` is invertible and positive, so `T_loc = M e^{-t_EA} M` is positive and injective. `M` is gauge invariant (cube-face traces are, `GB1QL.md` line 68) and `A` commutes with `R(h)` (Lemma 3.1(a)). (b) `k_{t_E}` is a class function, so `k_{t_E}(W_{ℓ,t}) = k_{t_E}(U_{ℓ,t} V_{x,t}^{-1} U_{ℓ,t+1}^{-1} V_{y,t}) = k_{t_E}(U_{ℓ,t} ((V_t·U_{t+1})_ℓ)^{-1})`, with `(V·U)_{(x,y)} = V_y^{-1} U_{(x,y)} V_x` as in section 3.1. So `∏_ℓ k_{t_E}(W_{ℓ,t}) = ∏_ℓ k_{t_E}(U_{ℓ,t}(V_t·U_{t+1})_ℓ^{-1})`. Also `e^{β_s Σ_{p∈CF} Tr X_p(U)} = M(U)²` (because `B_p = 2Tr X_p`), and `M(V·U) = M(U)`. Writing `M(U_t)² = M(U_t) · M(V_{t-1}·U_t)` and regrouping around the cycle gives the product of `κ(U_t, V_t·U_{t+1})`. Lemma 3.4 applies (bounded kernel); `Z = Tr(P_0 T_loc^{N_t}) = Tr(P_0 T_loc^{N_t} P_0) > 0` because `T_loc^{N_t}` is positive and injective and `P_0 ≠ 0`. (c) Product Haar measure is invariant under the gauge transformation (left and right translations of each variable), every holonomy is conjugated, and every weight is a class function. □

So the local lift supplies, for every `β_s ∈ R` and `t_E > 0`: a probability measure on `SU(2)`-valued links of the 4D periodic lattice `Λ × Z_{N_t}`, gauge invariant, with Haar reference measure and a bounded continuous density, whose transfer matrix is exactly `T_loc`. Its reflection positivity is section 6.

### 4.4 The exact lift of `e^{-a_0H}`

Throughout, `τ = τ_E > 0`, `W = V_θ`, `w = ‖W‖`, `H = τA + W`, and for `s > 0`
`Q_s = e^{-sτA} e^{-sW}`, `S_s = e^{-(s/2)W} e^{-sτA} e^{-(s/2)W}`.
`S_s` is `T_loc` at `(β_s, t_E) = (−2sθ, sτ)`, since `e^{(β_s/4)H_B} = e^{-(s/2)θH_B} = e^{-(s/2)W}`. Write `D_i` for the `6|𝓛|` operators `D_{μν,ℓ}` (`μ < ν`), so that `A = −¼ Σ_i D_i²` and `Σ_i ‖D_i z‖² = 4‖A^{1/2}z‖²`.

**Lemma 4.6 (tools).** (i) For a real smooth function `f` on `SU(2)^𝓛` and `z ∈ D(A)`: `fz ∈ D(A)` and `‖[A, f]z‖ ≤ c_f (‖z‖ + ‖Az‖)`, with `c_f = ½Σ_i‖D_i²f‖_∞ + 2(6|𝓛|)^{1/2} max_i‖D_if‖_∞`.
(ii) (Duhamel.) For `u ≥ 0` and `z ∈ 𝒦_𝓛`: `e^{-uH}z − e^{-uτA}z = −∫_0^u e^{-(u−r)τA} W e^{-rH} z dr`.
(iii) `‖e^{-uH}‖ ≤ e^{uw}`, `‖He^{-uH}‖ ≤ we^{uw} + (eu)^{-1}`, `‖Ae^{-uH}‖ ≤ τ^{-1}(2we^{uw} + (eu)^{-1})`, `‖Ae^{-uτA}‖ ≤ (euτ)^{-1}`, and `‖e^{-uH}‖_1 ≤ e^{uw} Θ(uτ)^{|𝓛|}`.

*Proof.* (i) On finite-flux vectors (smooth functions), `[D_i², f] = (D_i²f) + 2(D_if)D_i`, so `[A,f]z = −¼Σ_i[(D_i²f)z + 2(D_if)(D_iz)]`. Cauchy–Schwarz over `i` gives `Σ_i‖D_iz‖ ≤ (6|𝓛|)^{1/2}·2‖A^{1/2}z‖`, and `‖A^{1/2}z‖ ≤ ‖z‖ + ‖Az‖`. Finite-flux vectors form a core of `A`, and `A` is closed, so the bound and `fz ∈ D(A)` extend to `D(A)`. (ii) For `z ∈ D(A) = D(H)`, `r ↦ e^{-(u−r)τA}e^{-rH}z` is differentiable with derivative `e^{-(u−r)τA}(τA − H)e^{-rH}z = −e^{-(u−r)τA}We^{-rH}z`, because `e^{-rH}z ∈ D(A)` and `r ↦ e^{-rH}z` is `C¹` in the graph norm. Integrate from `0` to `u`; both sides are bounded in `z`, so the identity extends to all `z`. (iii) Spectral theorem with `H ≥ −w`: `|λ|e^{-uλ} ≤ we^{uw}` for `λ ∈ [−w, 0]` and `≤ (eu)^{-1}` for `λ ≥ 0`. Then `τ‖Az‖ ≤ ‖Hz‖ + w‖z‖`. The trace bound is Lemma 3.1(c). □

**Lemma 4.7 (one step).** For `0 < s ≤ 1` and `z ∈ D(A)`: `‖(Q_s − e^{-sH})z‖ + ‖(Q_s^* − e^{-sH})z‖ ≤ C_1 s² (‖z‖ + ‖Az‖)`, where `C_1` depends only on `τ`, `w` and the derivatives of `W` up to order two.

*Proof.* By Lemma 4.6(ii) and `e^{-sτA}(e^{-sW} − 1)z = −∫_0^s e^{-sτA}We^{-rW}z dr`,
`(Q_s − e^{-sH})z = ∫_0^s [e^{-(s−r)τA}W(e^{-rH} − e^{-rW})z + (e^{-(s−r)τA} − e^{-sτA})We^{-rW}z] dr`.
First term: `‖(e^{-rH} − e^{-rW})z‖ ≤ ‖(e^{-rH} − 1)z‖ + ‖(1 − e^{-rW})z‖ ≤ re^{rw}(‖Hz‖ + w‖z‖)`, and `‖Hz‖ ≤ τ‖Az‖ + w‖z‖`. Second term: `‖e^{-(s−r)τA}(1 − e^{-rτA})y‖ ≤ rτ‖Ay‖` with `y = f_r z`, `f_r = We^{-rW}`; by (i), `‖Ay‖ ≤ ‖f_r‖_∞‖Az‖ + c_{f_r}(‖z‖ + ‖Az‖)`, and `c_{f_r}` is bounded for `r ≤ 1`. Integrating over `r ∈ [0, s]` gives `O(s²)(‖z‖ + ‖Az‖)`. For `Q_s^* = e^{-sW}e^{-sτA}`:
`(Q_s^* − e^{-sH})z = ∫_0^s [(e^{-(s−r)τA} − 1)We^{-rH}z + W(e^{-rH} − e^{-sτA})z + (1 − e^{-rW})We^{-sτA}z] dr`,
and each bracket is `O(s)(‖z‖ + ‖Az‖)` by the same estimates, using `‖Ae^{-rH}z‖ ≤ τ^{-1}e^{rw}(‖Hz‖ + w‖z‖)`. □

**Lemma 4.8 (kernels and trace norms).** Let `0 < s ≤ 1` and `m ≥ 1`, and let `Y` be any product of `m` factors `Q_s`, or of `m` factors `Q_s^*`, or of `m` factors `S_s`.
(a) `Y` has a continuous kernel `y` with `0 ≤ y(U,U') ≤ e^{msw} ∏_ℓ k_{msτ}(U_ℓU'^{-1}_ℓ)`.
(b) If `m = m_1 + m_2` with `m_1 s, m_2 s ≥ u_0 > 0`, then `‖Y‖_1 ≤ e^{msw} Θ(2u_0τ)^{|𝓛|}`.

*Proof.* (a) `e^{-sτA}` has the continuous kernel `∏_ℓ k_{sτ}(U_ℓU'^{-1}_ℓ) ≥ 0` (Lemma 4.2), and each `e^{-cW}` (`0 < c ≤ s`) is multiplication by a function in `(0, e^{cw}]`. Kernels of products of such operators are iterated integrals of nonnegative functions, hence nonnegative and monotone in each factor. Replace each multiplier by its supremum and use `k_a * k_b = k_{a+b}` (from `e^{-aE²}e^{-bE²} = e^{-(a+b)E²}` and continuity of both sides). Continuity of `y` follows by dominated convergence. (b) `Y = Y_1Y_2` with `Y_i` products of `m_i` factors. `‖Y‖_1 ≤ ‖Y_1‖_2‖Y_2‖_2`, and by (a), `‖Y_i‖_2² = ∫∫ y_i² ≤ e^{2m_isw} ∫∫ ∏_ℓ k_{m_isτ}(U_ℓU'^{-1}_ℓ)² = e^{2m_isw} Tr e^{-2m_isτA} = e^{2m_isw}Θ(2m_isτ)^{|𝓛|}`, and `Θ` decreases. □

**Theorem 4.9 (Trotter limit in trace norm).** Let `a_0 > 0`, `n ≥ 8` with `s = a_0/n ≤ 1`. Then
`‖S_{a_0/n}^n − e^{-a_0H}‖_1 ≤ C (1 + log n)/n`,
with `C` depending only on the box, `θ`, `τ_E` and `a_0`.

*Proof.* Write `Q = Q_s`, `S = S_s`, `E = e^{-sH}`; `C` changes from line to line. *Step 1.* `S^n = e^{-(s/2)W} Q^{n−1} e^{-sτA} e^{-(s/2)W}`, so
`S^n − Q^n = (e^{-(s/2)W} − 1)Q^{n−1}e^{-sτA}e^{-(s/2)W} + Q^{n−1}e^{-sτA}(e^{-(s/2)W} − e^{-sW})`.
The differences of multipliers have norm at most `swe^{sw}`, and `‖Q^{n−1}‖_1 ≤ C` by Lemma 4.8(b) with `u_0 = a_0/4`. So `‖S^n − Q^n‖_1 ≤ Cs`. *Step 2.* `Q^n − E^n = Σ_{j=0}^{n−1} E^j(Q − E)Q^{n−1−j}`, and `‖E^j(Q−E)‖ = ‖(Q^* − E)E^j‖` because `E = E^*`.
- `j ≥ n/2`: `‖E^j(Q − E)Q^{n−1−j}‖_1 ≤ ‖E^{j/2}‖_1 ‖(Q^* − E)E^{j/2}‖ ‖Q^{n−1−j}‖`. Here `js/2 ≥ a_0/4`, so Lemma 4.6(iii) and Lemma 4.7 give `‖(Q^*−E)E^{j/2}‖ ≤ Cs²` and `‖E^{j/2}‖_1 ≤ C`. Each term is at most `Cs²`.
- `1 ≤ j < n/2`: `‖E^j(Q−E)Q^{n−1−j}‖_1 ≤ ‖(Q^*−E)E^j‖ ‖Q^{n−1−j}‖_1 ≤ C s²(1 + (js)^{-1})`, using `‖AE^j‖ ≤ C(1 + (js)^{-1})` and Lemma 4.8(b) with `u_0 = a_0/8` (valid for `n ≥ 8`).
- `j = 0`: with `m = ⌊(n−1)/2⌋`, `‖(Q − E)Q^{n−1}‖_1 ≤ ‖(Q−E)Q^m‖ ‖Q^{n−1−m}‖_1`. Since `Q^m = e^{-sτA}e^{-sW}Q^{m−1}`, `‖AQ^m‖ ≤ (esτ)^{-1}e^{msw}`, so Lemma 4.7 gives `‖(Q−E)Q^m‖ ≤ Cs`.
Summing: `‖Q^n − E^n‖_1 ≤ C(ns² + s Σ_{j<n/2} j^{-1} + s) ≤ C(1 + log n)/n`. *Step 3.* `E^n = e^{-a_0H}`. □

**Theorem 4.10 (the exact lift).** Let `τ_E > 0`, `θ ∈ R`, `a_0 > 0`, `N_t ≥ 2` even.
(a) `e^{-a_0H}` has a kernel `K` with `0 ≤ K(U,U') ≤ e^{a_0‖V_θ‖} ∏_ℓ k_{a_0τ_E}(U_ℓU'^{-1}_ℓ)` almost everywhere, and `K(h·U, h·U') = K(U,U')` almost everywhere for each `h`.
(b) The Euclidean lift `μ_ex` of `e^{-a_0H}` with `N_t` slices exists. `Z = Tr(P_0 e^{-N_ta_0H}) > 0`, Lemma 3.4 holds, and the law of `μ_ex` is invariant under every 4D gauge transformation.
(c) For odd `n`, let `μ^{(n)} = μ_loc[−2a_0θ/n, a_0τ_E/n]` with `nN_t` slices. Let `c_n` map a fine configuration to `((U_{nt})_t, (V^c_{x,t})_{x,t})` with `V^c_{x,t} = V_{x,nt+n−1} ⋯ V_{x,nt+1} V_{x,nt}`. Then `π_n = μ^{(n)} ∘ c_n^{-1}` is the Euclidean lift of `S_{a_0/n}^n`, and `‖π_n − μ_ex‖_{TV} → 0` as `n → ∞`.

*Proof.* (a) By Lemma 4.8(a) with `m = n`, `S_{a_0/n}^n` has a kernel `K_n` with `0 ≤ K_n ≤ e^{a_0w}∏_ℓ k_{a_0τ}`. Theorem 4.9 gives convergence in trace norm, hence in Hilbert–Schmidt norm, which is `L²` convergence of kernels; a subsequence converges almost everywhere, and the bounds pass to the limit. `R(h)e^{-a_0H}R(h)^{-1} = e^{-a_0H}` (Lemma 3.1(a)), and the kernel of `R(h)XR(h)^{-1}` is `x(h·U, h·U')`. (b) `K` is bounded and measurable, so Definition 3.3 and Lemma 3.4 apply; `Z > 0` because `e^{-N_ta_0H}` is positive and injective and `P_0 ≠ 0`. A 4D gauge transformation sends `(U_t, V_t·U_{t+1})` to `(h_t^{-1}·U_t, h_t^{-1}·(V_t·U_{t+1}))` (compute with `a·(b·U) = (ba)·U`), so by (a) the density is unchanged as an element of `L¹`; Haar measure is invariant. (c) By Theorem 4.5(b) the fine density is `∏_j κ_s(U_j, V_j·U_{j+1})`, `κ_s` the kernel of `S_s`, `s = a_0/n`. In the coarse step from `j_0 = nt` to `j_0 + n`, substitute `Ũ_j = (V_{j−1}⋯V_{j_0})·U_j` for `j_0 < j < j_0 + n` (sitewise products; Haar preserving). Gauge invariance of `κ_s` turns the factors of the step into `∏_j κ_s(Ũ_j, Ũ_{j+1})` with `Ũ_{j_0} = U_{j_0}` and `Ũ_{j_0+n} = V^c·U_{j_0+n}`. Integrating the `Ũ_j` gives `K_n(U_{j_0}, V^c·U_{j_0+n})`. The image of product Haar measure under `(V_{j_0}, …, V_{j_0+n−1}) ↦ V^c` is Haar measure, and the density depends on these variables only through `V^c`. So `π_n` has density `Z_n^{-1}∏_t K_n(U_t, V^c_t·U_{t+1})`. Finally, with `B = e^{a_0w} sup ∏_ℓ k_{a_0τ}`, `|∏_t K_n − ∏_t K| ≤ B^{N_t−1} Σ_t |K_n − K|(U_t, V_t·U_{t+1})`; integrating, `∫|∏K_n − ∏K| ≤ N_t B^{N_t−1}‖K_n − K‖_{L²} → 0`, so `Z_n → Z` and the normalized densities converge in `L¹`. □

**The action class of the exact lift.** `𝒜_FK` is the set of `μ_ex[θ, τ_E, a_0, N_t]`: the measures whose transfer matrix is exactly `e^{-a_0H}`, equivalently (Theorem 4.10(c)) the total-variation limits of coarse-grained local lifts along `(β_s, t_E) = (a_0/n)(−2θ, τ_E)`, `n` odd, `n → ∞`. This file neither claims nor excludes that their densities are finite products of plaquette weights.

## 5. The transfer matrix identity

### 5.1 The local transfer matrix is the tick at imaginary angles

For `z_B ∈ C` and `Re z_E ≥ 0` put `Φ(z_B, z_E) = e^{-(z_B/2)H_B} e^{-z_E A} e^{-(z_B/2)H_B}` on `𝒦_𝓛`. `H_B = Σ_C B_C` is a bounded multiplication operator and `e^{-z_EA}` is a contraction, so `Φ` is bounded, analytic in `(z_B, z_E)` for `Re z_E > 0`, and strongly continuous up to `Re z_E = 0`. All `B_p` are multiplication operators on `𝒦_𝓛`, so `W_B = ∏_C e^{-iθB_C} = e^{-iθH_B}`.

**Theorem 5.1 (one free constant).** (a) The Kogut–Susskind tick is unitarily equivalent to its symmetric form: `U_KS = e^{-i(θ/2)H_B} Φ(iθ, iτ_E) e^{i(θ/2)H_B}`.
(b) For `λ > 0`, `Φ(λθ, λτ_E) = Φ(−iλ·iθ, −iλ·iτ_E)` is the transfer matrix `T_loc` of the local lift `μ_loc[β_s, t_E]` with `β_s = −2λθ` and `t_E = λτ_E`, provided `τ_E > 0`.
(c) Conversely, a local lift `μ_loc[β_s, t_E]` arises in (b) from the ticks with `(θ, τ_E) = λ^{-1}(−β_s/2, t_E)`, `λ > 0`, and only from these. The tick fixes the ray of `(β_s, t_E)`; the point `λ` on the ray is not fixed by the tick.
(d) `Φ(a_0θ/n, a_0τ_E/n)^n → e^{-a_0H}` in trace norm as `n → ∞`, with `H` the R-SUM Hamiltonian (Theorem 4.9).

*Proof.* (a) `W_BW_E = e^{-iθH_B}e^{-iτ_EA} = e^{-i(θ/2)H_B}(e^{-i(θ/2)H_B}e^{-iτ_EA}e^{-i(θ/2)H_B})e^{i(θ/2)H_B}`. (b) `e^{-(λθ/2)H_B} = e^{(β_s/4)H_B} = M` with `β_s = −2λθ`, and `e^{-λτ_EA} = e^{-t_EA}`; compare Theorem 4.5. (c) Solve `β_s = −2λθ`, `t_E = λτ_E`. (d) `Φ(sθ, sτ_E) = S_s`. □

So the SU(2) Euclidean partner of the tick is exact and local, up to one positive number `λ`: the Euclidean time step in units of one tick. This is the precise SU(2) form of `GB1.md` line 209 ("the Wilson transfer is the tick at imaginary angles, which is not law data"): the missing law datum is exactly `λ`. Its effect is the anisotropy (section 7). Carena, Lamm, Li and Liu (arXiv:2107.01166, Eq. (31): `δ_τ → iδ_t`) make the same observation for Trotterized evolution; the heat-kernel temporal weight is what makes it exact (their Sec. II).

**What the tick does not give.** The transfer matrix of the local lift is `e^{-λH^{(λ)}}` with `H^{(λ)} = −λ^{-1} log T_loc`, defined because `T_loc` is positive and injective (Theorem 4.5(a)). This file does not claim `H^{(λ)} = H` at any `λ`; `A` and `H_B` do not commute (`[A, H_B]1 = AH_B = 3H_B ≠ 0`, because each `Tr X_p` lies in `H_1` on each of its four links). The exact `e^{-a_0H}` is reached only through (d) and Theorem 4.10. Lüscher (CMP 54, 283; NOT VERIFIED beyond the first page) defines the Hamiltonian of the Wilson action by the same logarithm.

### 5.2 Bounded generators have no Euclidean lift

**Theorem 5.2.** Let `H'` be a bounded self-adjoint operator on `𝒦_𝓛` commuting with every `R(h)`. For every `a_0 > 0` and even `N_t ≥ 2`, `e^{-a_0H'}` has no Euclidean lift: if `κ ≥ 0` is a measurable kernel of `e^{-a_0H'}`, then `∫_Ω ∏_t κ(U_t, V_t·U_{t+1}) dU dV = ∞`.

*Proof.* As in Lemma 3.4, `X = e^{-a_0H'}P_0` has the nonnegative kernel `κ_0(U,U') = ∫ κ(U, h·U') dh`, and `Z = ∫ ∏_t κ_0(U_t, U_{t+1}) dU`. Let `x` be the kernel of `X^{N_t/2}`, the iterated integral of `κ_0` (well defined in `[0, ∞]` by Tonelli). `X^{N_t/2}` is self-adjoint, so `x(U,U') = x(U',U)` almost everywhere, and `Z = ∫∫ x(U,U') x(U',U) = ∫∫ x²`. If `Z < ∞`, `x ∈ L²`, so `X^{N_t/2}` is Hilbert–Schmidt and `Tr X^{N_t} = ‖X^{N_t/2}‖_2² < ∞`. But `X^{N_t} = e^{-N_ta_0H'}P_0 ≥ e^{-N_ta_0‖H'‖} P_0`, and `P_0` has infinite rank (Lemma 3.1(d)). So `Tr X^{N_t} = ∞`, a contradiction. □

**Corollary 5.3 (what each reading gives for (H-4D)).** On every box:
1. Under R-SUM with `τ_E > 0`: the Euclidean lift of `e^{-a_0H}` exists for every `a_0 > 0` and even `N_t` (Theorem 4.10).
2. Under R-SUM with `τ_E = 0`: `H = V_θ` is bounded, and there is no lift (Theorem 5.2). With `τ_E < 0`: `e^{-a_0H}` is unbounded (Lemma 3.1(d)), and there is no lift with a bounded transfer matrix.
3. Under bounded R-GEN, under the hypotheses of Proposition 3.2: the Kogut–Susskind tick's generator `H_wr` is bounded, so it has no Euclidean lift for any `a_0 > 0` (Theorem 5.2). The first failing step is the finiteness of the partition function. The same holds for the limit of the framework's bounded R-GEN generators as `s → ∞` at fixed `τ_E > 0`, since that limit, on every fixed flux bound, is `H_wr` (Proposition 3.2(b)–(c)).

*Proof.* Items 1-2 are cited. Item 3: `H_wr` is bounded and gauge invariant (each `w(τ_EE²_ℓ)` is a function of a Casimir). □

So the answer to (H-4D) depends on the generator reading. The owner's bounded R-GEN, if its scope were widened from SMG1 to GB1, would make (H-4D) fail for the Kogut–Susskind target. R-SUM makes it hold. Section 9 four-tests both.

## 6. Gauge invariance, Haar reference, reflection positivity

**Gauge invariance and Haar reference** are proved: Theorem 4.5(a),(c) for the local lift and Theorem 4.10(a),(b) for the exact lift. Both have a bounded density with respect to product Haar measure on all spatial and temporal links.

### 6.1 The cube-face set under reflections

**Lemma 6.1.** Let `B = {x ∈ Λ : x_1 ≡ x_2 ≡ x_3 mod 2}` and let the tiling cubes be the unit cubes with base point in `B`.
(a) Every link lies in exactly one tiling cube.
(b) The faces of tiling cubes are exactly the plaquettes in a plane `(i,j)` whose base point has `x_i ≡ x_j mod 2`; each lies in exactly one tiling cube. So these cubes realize the set `CF` quoted from `GB1.md` line 31.
(c) For `i ∈ {1,2,3}` and `c ∈ Z + ½`, the reflection `x_i ↦ 2c − x_i` maps `CF` onto `CF`.
(d) For `c ∈ Z`, it maps the `CF` plaquettes of the planes `(i,j)`, `j ≠ i`, onto the non-`CF` plaquettes of those planes.

*Proof.* (a) A link in direction `1` at base `y` lies in the cubes with base `(y_1, y_2 − a, y_3 − b)`, `a, b ∈ {0,1}`. Exactly one of them is in `B`: `a ≡ y_2 − y_1` and `b ≡ y_3 − y_1` mod 2. Other directions alike. (b) A `(1,2)`-face of the cube at `x ∈ B` has base `(x_1, x_2, x_3)` or `(x_1, x_2, x_3 + 1)`, with `x_1 ≡ x_2`. Conversely a `(1,2)`-plaquette at base `y` with `y_1 ≡ y_2` is a face of the cube at `(y_1, y_2, y_3 − b)` exactly when `y_3 − b ≡ y_1`, one value of `b`. Other planes alike. (c) Take `i = 1`, `c = m + ½`. A plaquette in plane `(1,j)` with base coordinate `x_1` occupies `[x_1, x_1+1]` in direction 1; its image occupies `[2m − x_1, 2m + 1 − x_1]`, base `2m − x_1 ≡ x_1`. Plaquettes in plane `(2,3)` keep their in-plane base. (d) For `c = m`, the image base is `2m − x_1 − 1 ≢ x_1`. □

Only the parity description of `CF` is used below. The tiling with the other parity convention gives the same conclusions (c)–(d) with "agree" replaced by "disagree".

### 6.2 Link-reflection positivity for positive character weights

The following is the Osterwalder–Seiler link-reflection argument as the YM branch ports it from Sussman–Alpoge (CA-II `6.1:lem-reflection-positivity`; `p8-positivity.md` lines 26-130 at `5082c9928`; the remark on reducible representations is line 81). There it is stated for the Wilson weight. The proof uses only (P8.3) "positive character coefficients" and the matrix identity (P8.4), and the port notes: "Reducible unitary representations work in the source's factorization exactly as irreducible ones do." It is rebuilt here for the class `𝒫`.

**Setting.** `Γ = (Z/N_1Z) × ⋯ × (Z/N_4Z)`, all `N_μ` even. Each positively oriented bond `b` carries `U_b ∈ SU(2)`; `dU` is product Haar measure. Each plaquette `p` carries a bounded measurable class function `φ_p ≥ 0` of its holonomy `W_p`. In `SU(2)`, `g^{-1}` is conjugate to `g`, so every class function satisfies `φ(g^{-1}) = φ(g)` (and characters are real); the choice of base point and orientation of `W_p` does not matter. Fix a direction `μ` and `c ∈ Z + ½`. The reflection `ϑ` fixes the planes `{x_μ = c}` and `{x_μ = c + N_μ/2}` (which contain no site), and `Γ` minus these planes has two open halves `Γ_±`. Bonds are in `Γ_+`, in `Γ_−`, or crossing. As in (P8.1), `(ϑ·U)_b = U_{ϑb}`, or `U_{ϑb}^{-1}` if `ϑ` reverses the orientation of `b`.

**Lemma 6.2 (link-reflection positivity).** Assume `φ_{ϑp} = φ_p` for every plaquette, `φ_p ∈ 𝒫` for every plaquette containing a crossing bond, and `Z = ∫ ∏_p φ_p(W_p) dU > 0`. Let `μ = Z^{-1}∏_pφ_p(W_p)dU`. Then for every bounded measurable `F` of the bonds in `Γ_+`: `⟨F(ϑ·U)⟩_μ = ⟨F(U)⟩_μ` and `⟨\overline{F(ϑ·U)} F(U)⟩_μ ≥ 0`.

*Proof.* `ϑ` permutes bonds (inverting some variables), preserves product Haar measure and permutes plaquettes; with `φ_{ϑp} = φ_p` this gives the first claim. Split the plaquettes into `P_+`, `P_−` (all bonds in `Γ_±`) and `P_×` (containing crossing bonds). `ϑ` exchanges `P_+` and `P_−` and maps `P_×` to itself, so `∏_{p∈P_−}φ_p(W_p(U)) = G(ϑ·U_−)` with `G(U_+) = ∏_{p∈P_+}φ_p(W_p(U_+))`. A crossing plaquette in plane `(μ,ν)` at one plane has crossing bonds `ℓ_x`, `ℓ_{x'}` (`x' = x + e_ν`), oriented from `Γ_−` to `Γ_+`, and tangential bonds `b^± = ϑb^∓` in `Γ_±`; its holonomy is `W = U(ℓ_x)U(b^+)U(ℓ_{x'})^{-1}U(b^−)^{-1}` up to conjugation and inversion. Expand `φ_p(W) = Σ_q a_q χ_{R_q}(W)` and, for a unitary representation `R`,
`χ_R(σ_1σ_2σ_3^{-1}σ_4^{-1}) = Σ_{i,j,k,l} R_{ij}(σ_1) R_{jk}(σ_2) \overline{R_{lk}(σ_3)} \overline{R_{il}(σ_4)}` (P8.4).
In every crossing plaquette that contains `ℓ_x`, the factor of `σ = U(ℓ_x)` carries one index joined to a `Γ_−` factor (`i` or `l`) and one joined to a `Γ_+` factor (`j` or `k`). By Haar invariance replace `σ` by `σ'σ''^{-1}` with `σ', σ''` independent and Haar distributed. Then `R(σ)_{ij} = Σ_m R(σ')_{im}\overline{R(σ'')_{jm}}` and `\overline{R(σ)_{lk}} = Σ_{m'} \overline{R(σ')_{lm'}} R(σ'')_{km'}`. So `σ'` carries exactly the `Γ_−` indices and `σ''` exactly the `Γ_+` indices, in the same pattern. Integrating `σ'` gives a function `u_x(i,l; m,m')`; integrating `σ''` gives `\overline{u_x(j,k; m,m')}` (P8.5). Collect the labels `α = (q(·), m(·), m'(·))`, the weights `c_α = ∏ a_q ≥ 0` and
`G_α(U_+) = Σ_{j,k} ∏_x \overline{u_x(j,k)} ∏ R^{q}_{jk}(U(b^+))`.
Since `(ϑ·U)_{b^+} = U(b^−)`, the `Γ_−` side is `\overline{G_α(ϑ·U_−)}`, and
`∫ ∏_{crossing} dU(ℓ) ∏_{p∈P_×} φ_p(W_p) = Σ_α c_α G_α(U_+) \overline{G_α(ϑ·U_−)}` (P8.6).
Each index sum per plaquette has at most `d_q^4` terms and `|R_{ij}| ≤ 1`, so `Σ_q a_q d_q^k < ∞` (Definition 4.3) gives absolute convergence of every expansion and justifies every exchange of sums and integrals, as in `p8-positivity.md` (convergence paragraph after (P8.3)). The two planes have disjoint crossing bonds and plaquettes, so their expansions multiply. Hence, after `U_− ↦ ϑ·U_−` (Haar preserving),
`Z⟨\overline{F(ϑ·U)}F(U)⟩_μ = Σ_α c_α |∫ F(U_+) G_α(U_+) G(U_+) dU_+|² ≥ 0`. □

### 6.3 Reflection positivity of the lifts

**Theorem 6.3.** Let `N ≥ 4` and `N_t ≥ 2` be even.
(a) For every `β_s ∈ R` and `t_E > 0`, the local lift `μ_loc[β_s, t_E]` is link-reflection positive (Lemma 6.2's two conclusions) for the temporal reflections through `t ∈ Z + ½` and for the spatial reflections through `x_i ∈ Z + ½`, `i = 1, 2, 3`.
(b) For every `θ ∈ R`, `τ_E > 0`, `a_0 > 0`, the exact lift `μ_ex` has the same property.
(c) For a spatial reflection `ϑ_s` through a plane `x_i = c ∈ Z` (a site mirror): the local lift is not `ϑ_s`-invariant when `β_s ≠ 0`, and the exact lift's transfer matrix does not commute with `ϑ_s` when `θ ≠ 0`.

*Proof.* (a) *Temporal.* The crossing plaquettes are the temporal plaquettes `W_{ℓ,t_0}` at the plane; their weight `k_{t_E} ∈ 𝒫` (Lemma 4.4(iii)). Spatial plaquettes lie in slices and never cross. The reflection maps slices to slices and temporal plaquettes to temporal plaquettes, so the assignment is invariant. Lemma 6.2 applies for every `β_s`. *Spatial, `β_s ≥ 0`.* Crossing plaquettes are spatial plaquettes in planes `(i,j)` (weight `e^{β_s Tr} ∈ 𝒫` on `CF`, `1 ∈ 𝒫` off `CF`) and temporal plaquettes of crossing spatial bonds (`k_{t_E} ∈ 𝒫`). Lemma 6.1(c) gives invariance of the assignment. *Spatial, `β_s < 0`.* Take `i = 1` (others by permuting coordinates). Put `σ_{x,1} = (−1)^{x_2+x_3}`, `σ_{x,2} = (−1)^{x_3}`, `σ_{x,3} = 1` on spatial bonds; `N` is even, so this is well defined. Every spatial plaquette has `∏_{b∈∂p}σ_b = −1`: in plane `(1,2)` the product is `(−1)^{(x_2+x_3)+(x_2+1+x_3)}`, in `(1,3)` it is `(−1)^{(x_2+x_3)+(x_2+x_3+1)}`, in `(2,3)` it is `(−1)^{x_3 + (x_3+1)}`. `σ` does not depend on `x_1`, so `σ_{ϑb} = σ_b` for every reflection in direction 1. Let `Ψ` multiply each `U_{b,t}` by `σ_b` (all `t`; `−1` is central). `Ψ` preserves Haar measure, flips `Tr X_p` on every spatial plaquette, fixes every temporal plaquette (`σ_b² = 1`), and commutes with `ϑ`. So `Ψ_*μ_loc[β_s, t_E] = μ_loc[−β_s, t_E]`, and for `F` of the `Γ_+` bonds, `F∘Ψ^{-1}` is again a function of the `Γ_+` bonds; positivity for `−β_s > 0` gives positivity for `β_s`.
(b) Take `n` odd and `π_n` as in Theorem 4.10(c), with fine parameters `(β_s, t_E) = (−2a_0θ/n, a_0τ_E/n)`. *Spatial reflections* act slicewise and on temporal links sitewise; they commute with `c_n`, and `F∘c_n` is a function of fine `Γ_+` bonds when `F` is a function of coarse `Γ_+` variables (a coarse temporal link at `x ∈ Γ_+` is a product of fine temporal links at `x`). *The temporal reflection* through the coarse plane between slices `t_0` and `t_0+1` corresponds to the fine reflection through `nt_0 + n/2 ∈ Z + ½` (here `n` odd is used). It maps fine slice `nt` to `n(2t_0 + 1 − t)`, and the fine temporal links of coarse step `t` to those of step `2t_0 − t`, in reversed order and inverted; so `V^c ↦ (V^c)^{-1}`, which is the coarse reflection, and the coarse halves pull back into the fine halves. So each `π_n` satisfies both conclusions of Lemma 6.2. Both are of the form `E[G] ≥ 0` or `E[G_1] = E[G_2]` for bounded measurable `G`, and `|E_{π_n}[G] − E_{μ_ex}[G]| ≤ ‖G‖_∞ ‖π_n − μ_ex‖_{TV} → 0`.
(c) Distinct plaquettes give linearly independent functions `Tr X_p`: `Tr X_p` lies in `⊗_{ℓ∈p} H_1 ⊗ ⊗_{ℓ∉p} H_0` (each link entry is linear in `x`, hence in `H_1`), and these subspaces are orthogonal for distinct link sets. By Lemma 6.1(d), `ϑ_s` maps the `CF` plaquettes of the planes `(i,j)`, `j ≠ i`, onto the non-`CF` ones, and fixes the rest of `CF` setwise. So `Σ_{p∈CF} Tr X_p ∘ ϑ_s − Σ_{p∈CF} Tr X_p` is a nonzero function, orthogonal to constants. For the local lift, the two continuous densities differ by the factor `exp(β_s ×` that function`)` on every slice, so the measures differ when `β_s ≠ 0`. For the exact lift, let `R f = f∘ϑ_s`; `RAR^{-1} = A`. If `R e^{-a_0H} R^{-1} = e^{-a_0H}`, taking logarithms of these positive injective operators gives `R V_θ R^{-1} = V_θ`, which is false when `θ ≠ 0`. □

This is the reflection positivity of (P8.1), which `GA2_Y2_DRAFT.md`'s T0-start asks for, in all four directions. It is not the larger set of mirrors that the YM branch's LG1 Theorem 13 proves for the isotropic Wilson measure ("all coordinate site, coordinate bond and diagonal lattice mirrors", `library/lg1.md` line 431 per `prior/GB1E.md`): spatial site mirrors fail by (c), and the time–space exchange is not a symmetry (Theorems 7.3 and 7.5).

## 7. The action class and the relation to T0's isotropic Wilson action

### 7.1 Class functions on SU(2)

A class function depends only on the rotation angle `ψ ∈ [0, π]`, where `g` has eigenvalues `e^{±iψ}`; then `Tr g = 2 cos ψ = 2x_4`.

**Lemma 7.1.** (a) For bounded class functions, `∫ f dσ = (2/π)∫_0^π f(ψ) sin²ψ dψ`.
(b) `z_k(ψ) = (k+1) sin((k+1)ψ)/sin ψ`.
(c) A bounded class function `φ` acts by convolution `(C_φf)(x) = ∫ φ(xy^{-1})f(y) dσ(y)` on `H_k` as the scalar `c_k(φ) = (k+1)^{-2}∫ φ z_k dσ`.
(d) For `b ≠ 0`, `c_k(e^{b Tr}) = I_{k+1}(2b)/b`, with `I_n(x) = Σ_{j≥0} (x/2)^{n+2j}/(j!(n+j)!)`. In particular `|c_k(e^{bTr})| ≥ |b|^k/(k+1)!`. For `b = 0`, `c_k = δ_{k0}`.

*Proof.* (a) Spherical coordinates `x = (sin ψ ω, cos ψ)`, `ω ∈ S²`, have volume element `sin²ψ dψ dω` on `S³`; normalize. (b) Two elements of `SU(2)` with the same trace are conjugate in `SU(2)` (diagonalize by a unitary and rescale its determinant), so the class function `z_k(g(x)) = Z_k(x, e)` is `P(x_4)` on `S³`. It is the restriction of a harmonic polynomial `F` homogeneous of degree `k`; then `F(x) = r^kP(x_4/r)`. `F|_{S³}` depends only on `x_4`, so it is invariant under `x_1 ↦ −x_1`, and so is the homogeneous `F`; hence `P(u) = F(√(1−u²), 0, 0, u)` is a polynomial of degree `≤ k`. With `u = x_4/r`: `|∇u|² = (1−u²)/r²`, `Δu = −3u/r²`, `x·∇u = 0`, `Δr^k = k(k+2)r^{k−2}`, so `ΔF = r^{k−2}[(1−u²)P'' − 3uP' + k(k+2)P]`. Comparing coefficients of `u^j`: `(j+2)(j+1)p_{j+2} = [j(j+2) − k(k+2)]p_j`. In the parity class opposite to `k`, the top coefficient `p_{j_0}` (`j_0 < k`) must vanish; the class of `k` is fixed by `p_k`. So the polynomial solutions form a line. `U_k(cos ψ) = sin((k+1)ψ)/sin ψ` is a polynomial of degree `k` in `cos ψ` (`U_{k+1} = 2uU_k − U_{k−1}`) and solves it: for `y(ψ) = P(cos ψ)`, `y'' + 2cot ψ y' = (1−u²)P'' − 3uP'`, and `(y sin ψ)'' = −(k+1)² y sin ψ` gives `y'' + 2cot ψ y' = −k(k+2)y`. Normalize by `z_k(e) = (k+1)²` and `U_k(1) = k+1`. (c) By Lemma 4.1, `∫ z_jz_k dσ = (Π_jΠ_k`'s kernel at `(e,e)) = δ_{jk}(k+1)²`. By (a) and (b), class functions in `L²(σ)` correspond to `f(ψ)sin ψ ∈ L²([0,π], dψ)`, which the sine system `sin((k+1)ψ)` spans; so `z_k/(k+1)` is an orthonormal basis of the class functions. `C_{z_k} = Π_k` (its kernel), so `C_φ = Σ_k c_k(φ) Π_k`. (d) By (a), (b): `c_k = (1/(π(k+1)))∫_0^π e^{2b cos ψ}(cos kψ − cos(k+2)ψ) dψ`. Expanding `e^{2b cos ψ}` and using `(1/π)∫_0^π cos^mψ cos nψ dψ = 2^{-m} C(m, (m−n)/2)` for `m ≥ n`, `m ≡ n` (mod 2), and `0` otherwise, gives `(1/π)∫_0^π e^{x cos ψ} cos nψ dψ = I_n(x)`. The series identity `I_k − I_{k+2} = (2(k+1)/x) I_{k+1}` (compare coefficients of `(x/2)^{k+2j}`: `1/(j!(k+j)!) − 1/((j−1)!(k+j+1)!) = (k+1)/(j!(k+j+1)!)`) gives `c_k = I_{k+1}(2b)/b`. For `x > 0` all terms of `I_n(x)` are positive, and `I_n(−x) = (−1)^n I_n(x)`; keep the term `j = 0`. □

`[check]` (`check_hk.py`): `∫ e^{2b cos ψ} z_k dσ/(k+1)² = I_{k+1}(2b)/b` to `10^{-11}` for `b = 0.5, 2`, `k ≤ 5`.

### 7.2 Exact differences from the isotropic Wilson measure

**Lemma 7.2 (the heat kernel is never a Wilson weight).** For `t > 0` there are no `a, b ∈ R` with `k_t(g) = e^{a + b Tr g}` on a neighbourhood of `e`.

*Proof.* Both sides are real-analytic functions of `ψ ∈ R` (for `k_t`: by Lemma 7.1(b), `z_k(ψ) = (k+1)U_k(cos ψ)` with `U_k(cos ψ) = Σ_{j=0}^k e^{i(k−2j)ψ}`, so `|U_k(cos ψ)| ≤ (k+1)e^{k|Im ψ|}`, and `e^{-tk(k+2)/4}` makes the series converge uniformly on every strip `|Im ψ| ≤ c`). Equality near `ψ = 0` gives equality everywhere, so `c_k(k_t) = e^a c_k(e^{bTr})` for all `k`. `c_k(k_t) = e^{-tk(k+2)/4} > 0` for all `k`, so `b ≠ 0` (Lemma 7.1(d)), and then `e^{-tk(k+2)/4} ≥ e^a|b|^k/(k+1)!` for all `k`. This fails for large `k`, since `log((k+1)!) ≤ (k+1)log(k+1)` grows more slowly than `tk²/4`. □

**Theorem 7.3 (the lifts are not isotropic Wilson).** Let `N_t = N` (so that exchanging the time axis with a space axis is a symmetry of the lattice `Γ`).
(a) For all `β_s ∈ R`, `t_E > 0`: let `ς` exchange the time axis and the spatial axis `1` (temporal links go to direction-1 links). Then `ς_*μ_loc[β_s, t_E] ≠ μ_loc[β_s, t_E]`.
(b) If `β_s ≠ 0`, `μ_loc[β_s, t_E]` is not invariant under the translation by `e_i`, `i = 1, 2, 3`.
(c) For no parameters is `μ_loc[β_s, t_E]` equal to T0's Wilson measure `Z^{-1}e^{-x_0A_W(U)}dU` (all plaquettes, `A_W = Σ_p(1 − ½Re Tr U_p)`) on `Γ`, for any `x_0 ≥ 0`.

*Proof.* (a) The density `ρ` is continuous and positive near the identity configuration `𝟙` (Lemma 4.2(b)). If `ς_*μ = μ` then `ρ∘ς = ρ` everywhere. Let `𝟙_b(ε)` equal `𝟙` except `U_b = e^{εX}`, `X ∈ su(2)` nonzero, rotation angle `ψ = ψ(ε) → 0`. Plaquettes through `b` have holonomy conjugate to `e^{±εX}`; the others have holonomy `e`. So `log ρ(𝟙_b(ε)) − log ρ(𝟙) = Σ_{p∋b} g_p(ψ)`, where `g_W(ψ) = 2β_s(cos ψ − 1)` on `CF`, `0` on other spatial plaquettes, and `g_K(ψ) = log k_{t_E}(ψ) − log k_{t_E}(0)` on temporal ones. A direction-1 spatial bond lies in exactly two `CF` plaquettes (two faces of its unique tiling cube, Lemma 6.1(a),(b)), two other spatial plaquettes, and two temporal ones: the sum is `2g_W + 2g_K`. A temporal link `V_{x,t}` lies in the six temporal plaquettes of the spatial links at `x`: the sum is `6g_K`. `ς` maps one kind of bond to the other and `𝟙_b(ε)` to `𝟙_{ςb}(±ε)`, so `2g_W + 2g_K = 6g_K`, i.e. `k_{t_E}(ψ) = k_{t_E}(0)e^{β_s(cos ψ − 1)}` for small `ψ`, against Lemma 7.2.
(b) Translation by `e_1` changes the parity of `x_1`, so it maps the `CF` plaquettes of planes `(1,2)` and `(1,3)` onto non-`CF` ones; conclude as in the proof of Theorem 6.3(c).
(c) T0's Wilson measure is invariant under `ς` (P8: "the Wilson measure is invariant under every torus isometry preserving the bare lattice"). By (a), `μ_loc` is not. □

**Theorem 7.5 (the exact lift is not isotropic either).** Let `N_t = N`, `τ_E > 0`, `a_0 > 0`. The set of `θ ∈ R` for which `ς_*μ_ex = μ_ex` is a discrete subset of `R ∖ {0}` (possibly empty).

*Proof.* *At `θ = 0`*, `e^{-a_0H} = e^{-a_0τ_EA} = T_loc` at `(β_s, t_E) = (0, a_0τ_E)`, so `μ_ex = μ_loc[0, a_0τ_E]`, which is not `ς`-invariant (Theorem 7.3(a)). *An invariant.* Let `p, p'` be `(1,2)`-plaquettes in one slice whose bases differ by `e_1`, with `p ∈ CF` and `p' ∉ CF`. If `ς_*μ_ex = μ_ex`, then `E[Tr X_q]` for a `(1,2)`-plaquette `q` equals the expectation of the temporal plaquette `ς q`, which does not depend on the time coordinate (time-translation invariance of `μ_ex`), that is, on the `x_1`-coordinate of `q`. So `Δ(θ) := E_{μ_ex}[Tr X_p] − E_{μ_ex}[Tr X_{p'}] = 0`. By Lemma 3.4, `E[Tr X_q] = Tr(P_0 Tr X_q e^{-βH})/Tr(P_0e^{-βH})` with `β = N_ta_0`. *Analyticity.* Iterating Lemma 4.6(ii) gives `e^{-β(τ_EA + θH_B)} = Σ_m (−θ)^m I_m` with `I_m = ∫_{0<u_1<⋯<u_m<β} e^{-(β−u_m)τ_EA}H_B ⋯ H_B e^{-u_1τ_EA} du`. In each term the largest gap is at least `β/(m+1)`, so `‖I_m‖_1 ≤ ‖H_B‖^m (β^m/m!) Θ(βτ_E/(m+1))^{|𝓛|}`, and `Θ(u) ≤ C(1 + u^{-3/2})`. The series converges in trace norm for every `θ`, so `Δ` is real-analytic on `R`. *Derivative at `0`.* The flux sectors `⊗_ℓH_{k_ℓ}` are preserved by `A` and `P_0`, and multiplication by `Tr X_q` changes the flux by `±1` on each link of `q` and nowhere else (`GB1QL.md` Lemma 4.1(a)). So `Tr(P_0 Tr X_q · Y)` vanishes for every `Y` built from `A`, `P_0` and `Tr X_r` with `r ≠ q` used at most once. Hence `Δ(0) = 0` and
`Δ'(0) = −(2/Z_0) ∫_0^β ‖e^{-uτ_EA/2} (Tr X_p) P_0 e^{-(β−u)τ_EA/2}‖_2² du < 0`,
where only the term `r = p` of `H_B = Σ_{r∈CF} 2Tr X_r` survives (and none for `p' ∉ CF`). So `Δ` is not identically zero, its zeros are discrete, and `0` is one of them. □

Section 9.1 records the consequence for (H-class).

### 7.3 Small-field stiffness, anisotropy, coupling trajectory, Haar links

**Proposition 7.4 (stiffness at the identity).** As `ψ → 0`:
`log e^{β_s Tr g} = 2β_s − β_sψ² + O(ψ⁴)`, `log k_t(ψ) = log k_t(0) − c_tψ² + O(ψ⁴)` with `c_t = (2/3)⟨E²⟩_t`,
where `⟨E²⟩_t = Σ_k (k+1)² (k(k+2)/4) e^{-tk(k+2)/4} / Σ_k (k+1)² e^{-tk(k+2)/4}`. `c_t` is strictly decreasing in `t`, `c_t → ∞` as `t → 0`, `c_t → 0` as `t → ∞`, and `t c_t → 1` as `t → 0`. T0's weight `e^{x_0 Re tr W} = e^{(x_0/2)Tr W}` has stiffness `x_0/2` on every plaquette.

*Proof.* `sin((k+1)ψ)/sin ψ = (k+1)(1 − k(k+2)ψ²/6 + O(ψ⁴))`, uniformly summable against `e^{-tk(k+2)/4}`. `d⟨E²⟩_t/dt = −Var_t(E²) < 0`. As `t → ∞` the weight concentrates on `k = 0`. As `t → 0`, Riemann sums with `y = k√t/2` give `⟨E²⟩_t ~ (1/t)∫y⁴e^{-y²}dy / ∫y²e^{-y²}dy = 3/(2t)`. □

**The relation, stated exactly.** Take the Kogut–Susskind sign `θ < 0 < τ_E` and Euclidean step `λ` (Theorem 5.1): `β_s = 2λ|θ|`, `t_E = λτ_E`.
1. **Haar links.** Identical: both measures have product normalized Haar reference measure on all links of `Γ`, gauge group `SU(2)`.
2. **Plaquettes and weights.** T0: weight `e^{(x_0/2)Tr}` on every plaquette. Lift: `k_{t_E}` on temporal plaquettes, `e^{β_s Tr}` on `CF` spatial plaquettes, `1` on the other half of the spatial plaquettes. By Lemma 7.2 and Theorem 7.3 the two never coincide.
3. **Anisotropy.** In small-field (tree-level) form, a lattice field from a smooth connection with spatial spacing `a` and temporal spacing `a_0` has plaquette angles proportional to `a·a_0|F_{i0}|` and `a²|F_{ij}|`, with one common constant. Averaging the spatial stiffness over `CF` (half of each spatial plane) gives `β_s/2`. Requiring the leading quadratic form to be a multiple of `g^{-2}∫|F|²`, calibrated so that T0's measure has `ξ = 1` and `g² = 4/x_0`, gives the tree-level dictionary `ξ_cl² = (a/a_0)² = 2c_{t_E}/β_s` and `g_cl⁴ = 8/(c_{t_E} β_s)`. On the tick's ray, using `tc_t → 1`: `ξ_cl ~ (λ²|θ|τ_E)^{-1/2}` and `g_cl² → 2(τ_E/|θ|)^{1/2}` as `λ → 0`. So `λ` moves the anisotropy, and the tick fixes the tree-level coupling. The tree-level isotropic point `ξ_cl = 1` is the unique `λ_iso` with `c_{λτ_E} = λ|θ|` (left side decreasing from `∞` to `0`, right side increasing from `0`); there the lift has stiffness `β_s/2` on temporal plaquettes and `β_s` on `CF` plaquettes, the `CF`-average of T0's stiffness `x_0/2` at `x_0 = β_s`. This dictionary is the classical (tree-level) continuum limit, not a theorem about quantum anisotropy; one-loop renormalization of `ξ` is Karsch's computation (NOT VERIFIED; arXiv:2208.10417 gives such relations at any anisotropy).
4. **Coupling trajectory.** One law has fixed `(θ, τ_E)`, so one tree-level coupling. Varying `λ` changes anisotropy, not coupling. T0's trajectory is a sequence of isotropic Wilson measures with `x_0 → ∞` (T1: "along a coupling trajectory the proof chooses", `GOAL.md` line 26 at `5082c9928`). Following it would need a family of laws with `τ_E/|θ| → 0`, which `GB1.md` row H5 already names: "Needs a family of laws, or the requests T0-start[G] and T0-rate". GB1QL's own family is in `s` at fixed angles, which changes the register, not the coupling.
5. **Transfer matrices.** T0's isotropic measure has the positive transfer matrix `e^{(x_0/4)Σ_{sp}Tr} C_{x_0} e^{(x_0/4)Σ_{sp}Tr}` (all spatial plaquettes; `C_{x_0}` the Wilson temporal convolution, with multipliers `c_k(e^{(x_0/2)Tr})/c_0 = I_{k+1}(x_0)/I_1(x_0)` by Lemma 7.1(d)). The local lift has `Φ(λθ, λτ_E)` (multipliers `e^{-t_Ek(k+2)/4}`); the exact lift has `e^{-a_0H}`. The repository's main-branch note `GAUGE_WILSON_FULL_CUBE_COMPACT_INTERACTING_HAMILTONIAN_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-07.md` (unaudited; one SU(3) cube) proves that the anisotropic Wilson transfer `F(h) = M_h C_{a/h}^{⊗12} M_h` satisfies `F(t/n)^n → e^{-tH}` strongly, with `H = −(3/(2a))Δ + V`: anisotropic Wilson measures approach the same kind of Hamiltonian as the anisotropy grows. It is context here, not used in a proof.

## 8. What the framework itself supplies

Sections 4-7 lift the target, Trotterized Kogut–Susskind `SU(2)`. This section asks what the framework's own registers `R_s` give. Notation from `GB1QL.md` section 1.4: `ι : R_s → 𝒦` is the inclusion and `ι_𝓛 = ⊗_ℓ ι`; then `ι_𝓛ι_𝓛^* = Π_s := ⊗_ℓ Π_{≤s}`, which commutes with `A` and with every `R(h)`. `d_s = dim R_s = (s+1)(s+2)(2s+3)/6`.

### 8.1 At fixed `s`: signed measures

**Lemma 8.1.** Let `D_s(x,y) = Σ_{k≤s} Z_k(x,y)`, the kernel of `Π_{≤s}`. Then `D_s(x,x) = d_s`, and for `s ≥ 1`, `m_s := −min D_s > 0`.

*Proof.* `D_s(x,x) = Σ_{k≤s}(k+1)²` (Lemma 4.1(c)). Put `f(y) = D_s(e, y)`, real and continuous. `∫ f dσ = (Π_{≤s}1)(e) = 1`. `y_4 ∈ H_1 ⊂ R_s`, so `∫ f(y) y_4 dσ(y) = (Π_{≤s} y_4)(e) = 1` (`e = e_4`). Hence `∫ f(y)(1 − y_4) dσ = 0`. If `f ≥ 0`, then `f(1 − y_4) = 0` almost everywhere; `1 − y_4 > 0` off the null set `{e}`, so `f = 0` almost everywhere and `∫ f = 0 ≠ 1`. □

`[check]` (`check_hk.py`): `min D_s = −3, −2.333, −10, −6.034, −21` for `s = 1, …, 5` (`D_1 = 1 + 4cos ψ` exactly).

**Theorem 8.2 (the framework's own lift is signed in the Hamiltonian regime).** Let `s ≥ 1` and let `X` be any operator on `R_s^{⊗𝓛}` with `‖X − 1‖ < m_s/d_s`. Then the continuous kernel `κ_X` of `ι_𝓛Xι_𝓛^*` is negative on a nonempty open set. Consequently:
(a) For every Hermitian `H_s` on `R_s^{⊗𝓛}` (every generator reading) and every `0 < a_0 < log(1 + m_s/d_s)/‖H_s‖`, no measure with Haar density has transfer matrix `ι_𝓛e^{-a_0H_s}ι_𝓛^*` (Definition 3.3 needs `κ ≥ 0` almost everywhere).
(b) For R-SUM's `H_s` with `θ = 0`, the same holds for `0 < a_0τ_E < 4 log(1 + m_s/d_s)/(s(s+2))`, a bound independent of the box.

*Proof.* Let `(φ_a)` be an orthonormal basis of `R_s^{⊗𝓛} ⊂ 𝒦_𝓛` made of products. Then `κ_X(U,U') = Σ_{a,b} φ_a(U) X_{ab} \overline{φ_b(U')}`, and `κ_1(U,U') = ∏_ℓ D_s(U_ℓ, U'_ℓ)`. With `φ(U) = (φ_a(U))_a`, `‖φ(U)‖² = κ_1(U,U) = d_s^{|𝓛|}`, so `|κ_X − κ_1| ≤ ‖X − 1‖ d_s^{|𝓛|}`. Choose `y_0` with `D_s(e, y_0) = −m_s`, `U = 𝟙` and `U'` equal to `𝟙` except `U'_{ℓ_0} = y_0`: `κ_1(U,U') = −m_s d_s^{|𝓛|−1}`, so `κ_X(U,U') ≤ d_s^{|𝓛|−1}(−m_s + ‖X−1‖d_s) < 0`. Continuity gives an open set. Kernels of one operator agree almost everywhere. (a) `‖e^{-a_0H_s} − 1‖ ≤ e^{a_0‖H_s‖} − 1`. (b) With `θ = 0`, `ι_𝓛e^{-a_0H_s}ι_𝓛^*` is the tensor product over links of the band-limited heat operator, whose kernel is the product of one-link kernels. Apply the first part to one link (`‖e^{-a_0τ_EE²}|_{R_s} − 1‖ ≤ a_0τ_E s(s+2)/4`) and evaluate the other factors at `(e, e)`, where they are positive. □

`[check]` (`check_hk.py`): the one-link band-limited heat kernel `Σ_{k≤s} e^{-tk(k+2)/4} z_k` has minimum `−2.97, −2.71, −1.75` at `t = 0.01, 0.1, 0.5` for `s = 1`, and `−21.2, −1.35, −5.5·10^{-5}` for `s = 8`; it is positive at `t = 2` for `s ≤ 8`. So the theorem's threshold is not sharp, and positivity can return at large `a_0τ_E`; this file claims nothing there.

**Lemma 8.3 (no gauge-covariant positive basis on a finite register).** Let `V` be finite-dimensional with an orthonormal basis `(e_i)`, and let a connected topological group `G` act by a continuous unitary representation `π` such that each `π(g)` maps the cone `{Σ c_ie_i : c_i ≥ 0}` into itself. Then `π` is trivial.

*Proof.* The columns of `π(g)` are orthonormal vectors with nonnegative entries, so they have disjoint supports; `dim V` such columns force each to have one nonzero entry, equal to `1` by unitarity. So `π(g)` is a permutation matrix. `g ↦ π(g)` is continuous into a finite discrete set and `G` is connected, so `π(g) = π(1) = 1`. □

The gauge action on `R_s^{⊗𝓛}` (rotations of `S³` on each link, `GB1QL.md` line 91) is nontrivial for `s ≥ 1`. So a probability-measure representation of a framework transfer matrix in a basis of the framework's own register (a Feynman–Kac representation with "classical configurations") cannot carry the `SU(2)` gauge action. The group-valued variables of `𝒦` keep the gauge action, but at fixed `s` they lose positivity (Theorem 8.2). These are two faces of one fact: an exactly gauge-invariant Euclidean measure on group-valued links needs the infinite register `𝒦`.

### 8.2 As `s → ∞`: trace-norm convergence to the exact lift

**Theorem 8.4 (the Euclidean regulator limit).** Let `τ_E > 0`, `θ ∈ R`, `a_0 > 0`, the box fixed, and `H_s = τ_E Σ_ℓ E²_ℓ + θ Σ_C B^s_C` on `R_s^{⊗𝓛}` (R-SUM). Then `‖ι_𝓛 e^{-a_0H_s} ι_𝓛^* − e^{-a_0H}‖_1 → 0` as `s → ∞`. Consequently, for even `N_t` and bounded measurable slice functions `F_1, …, F_{N_t}`, the framework's Euclidean correlators converge to those of the probability measure `μ_ex` (Theorem 4.10):
`Tr(∏_t (ι^*F_tι e^{-a_0H_s} P_0)) / Tr(P_0 e^{-N_ta_0H_s}) → E_{μ_ex}[∏_t F_t(U_t)]`,
with `P_0` restricted to `R_s^{⊗𝓛}` on the left.

*Proof.* Put `Ṽ_s = ι_𝓛(θΣ_C B^s_C)ι_𝓛^*` and `H̃_s = τ_EA + Ṽ_s`. `Ṽ_s` maps into `ran Π_s`, vanishes on its complement, and `‖Ṽ_s‖ ≤ 24|θ| |𝒞| =: w'`. `A` preserves `ran Π_s`, so `ι_𝓛e^{-a_0H_s}ι_𝓛^* = e^{-a_0H̃_s}Π_s =: X_s`. Put `X = e^{-a_0H}`.
*Step 1 (strong convergence).* `GB1QL.md` Lemma 4.7, plaquette step: "`‖(B̃_C − B_C)v‖ ≤ 96δ_s(M'')‖v‖`" for `v` of flux at most `M''` on the cube; with `‖B̃_C‖, ‖B_C‖ ≤ 24` and density of finite-flux vectors, `Ṽ_s → V_θ` strongly. Duhamel, `e^{-a_0H}z − e^{-a_0H̃_s}z = ∫_0^{a_0} e^{-(a_0−r)H̃_s}(Ṽ_s − V_θ)e^{-rH}z dr`, with integrand bounded by `2w'e^{a_0w'}‖z‖`, and dominated convergence give `e^{-a_0H̃_s} → e^{-a_0H}` strongly; and `Π_s → 1` strongly.
*Step 2 (eigenvalues).* Let `μ_i^s` be the eigenvalues of `H_s` and `μ_i` those of `H`, increasing with multiplicity. *Upper:* let `E_i` be spanned by the first `i` eigenvectors of `H`. For large `s`, `Π_sE_i` has dimension `i`, and on its unit sphere the Rayleigh quotient of `H̃_s` converges uniformly to that of `H` on `E_i` (finite dimension; `⟨Π_sy, AΠ_sy⟩ = ⟨y, AΠ_sy⟩ → ⟨y, Ay⟩`), whose maximum is `μ_i`. Min-max on `ran Π_s` gives `limsup μ_i^s ≤ μ_i`. *Lower:* take orthonormal eigenvectors `x_1^s, …, x_i^s` for `μ_1^s, …, μ_i^s`. Their `A`-forms are bounded by `(μ_i + 1 + w')/τ_E` for large `s`; `A` has compact resolvent, so along a subsequence realizing `liminf μ_i^s` they converge in `𝒦_𝓛` to orthonormal `y_1, …, y_i`. For a unit `y` in their span, `⟨y, Ay⟩ ≤ liminf` of the forms (lower semicontinuity of a closed form) and `⟨y^s, Ṽ_sy^s⟩ → ⟨y, V_θy⟩`, so `⟨y, Hy⟩ ≤ liminf μ_i^s`; min-max gives `μ_i ≤ liminf μ_i^s`. *Domination:* `μ_i^s ≥ τ_E α_i − w'`, because `A` restricted to `ran Π_s` has `i`-th eigenvalue at least `α_i`. By dominated convergence and Lemma 3.1(c), `Tr X_s = Σ_i e^{-a_0μ_i^s} → Σ_i e^{-a_0μ_i} = Tr X`.
*Step 3 (trace norm).* Let `P` be a finite-rank projection with `Tr(X(1−P)) < ε`. Then `Tr(X_s(1−P)) = Tr X_s − Tr(X_sP) → Tr(X(1−P))`. For `Y ≥ 0`, `‖(1−P)Y‖_1 ≤ ‖(1−P)Y^{1/2}‖_2 ‖Y^{1/2}‖_2 = (Tr((1−P)Y) Tr Y)^{1/2}`. Splitting `X_s − X` by `P` and `1 − P`, and using `‖P(X_s − X)P‖_1 → 0` (finite rank, weak convergence), `limsup ‖X_s − X‖_1 ≤ 4(2ε · 2Tr X)^{1/2}`. Let `ε → 0`.
*Correlators.* `ι^*F_tι` embedded is `Π_sF_tΠ_s`, and `P_0` commutes with `Π_s`. The numerator is `Tr(∏_t(Π_sF_tΠ_s X_sP_0))`; each `X_s` converges in trace norm and the bounded factors `Π_sF_tΠ_s → F_t` strongly (also their adjoints), so it converges to `Tr(∏_t(F_tXP_0))`. The same with `F_t = 1` for the denominator, which tends to `Z > 0`. Lemma 3.4 identifies the limit. □

So, under R-SUM, the framework supplies (H-4D) **approximately**, in this order of limits: fixed box, fixed `a_0` and `N_t`, then `s → ∞`. Its approximants are signed (Theorem 8.2 at small `a_0`) and converge in trace norm to the transfer matrix of a genuine probability measure, `μ_ex`. This is the Euclidean counterpart of `GB1QL.md` Theorem 4.8. Unlike Theorem 4.8, it is not uniform in the volume: imaginary-time evolution has no light cone, and the trace norms are extensive. Under bounded R-GEN the limit generator is `H_wr`, which has no lift (Corollary 5.3, item 3).

`μ_ex` is, by Lemma 3.4, the Gibbs state of `H` at inverse temperature `N_ta_0` on the gauge-invariant sector. Whether the framework's state is the ground state of `H` (the limit `N_t → ∞`) is `GB1.md`'s E-2; nothing here supplies it.

## 9. The hand-off, hypothesis by hypothesis

### 9.1 The table

T0-start[SU(2)] (`GA2_Y2_DRAFT.md` line 211): "every gauge-invariant, reflection-positive probability measure `μ` on `G`-valued links of `a_{k_0}Z^4`, with Haar reference measure and density in `𝒜_{k_0}(g)` for some `g ≤ g_*`". Three objects are candidates for `μ`: the local lift `μ_loc` (Theorem 4.5; the tick at imaginary angles, Theorem 5.1), the exact lift `μ_ex` (Theorem 4.10; transfer matrix exactly `e^{-a_0H}`), and the framework's own lift through `ι` at fixed `s` (section 8). "Delivered" means proved here or in a frozen item; "approximately" means in a stated order of limits. All statements are on finite periodic boxes `(Z/NZ)³ × Z/N_tZ`, `N ≥ 4` and `N_t ≥ 2` even, as T0-start's "every torus side" asks.

| Hypothesis | `μ_loc[β_s, t_E]` (`t_E > 0`) | `μ_ex` under R-SUM (`τ_E > 0`) | framework at fixed `s` / as `s → ∞` | under bounded R-GEN |
|---|---|---|---|---|
| (H-G) `SU(2)`, local | delivered in the test law (`GB1QL.md` Proposition 4.11(a)) | same | same | same |
| (H-4D) probability measure on links of a 4D lattice | **delivered**, every `β_s ∈ R` (Theorem 4.5) | **delivered**, every `a_0 > 0`, `θ ∈ R` (Theorem 4.10) | **fails** at fixed `s` for `0 < a_0 < log(1 + m_s/d_s)/‖H_s‖`, every generator reading: the kernel is negative on an open set (Theorem 8.2). **Approximately delivered** as `s → ∞` at fixed box, `a_0`, `N_t`, under R-SUM (Theorem 8.4) | **fails** for the Kogut–Susskind generator and the `s → ∞` limit: partition function infinite (Theorem 5.2, Corollary 5.3) |
| (H-GI) `μ` gauge invariant | delivered (Theorem 4.5(c)) | delivered (Theorem 4.10(b)) | the approximants are gauge invariant signed measures | no `μ` |
| (H-Haar) Haar reference, density | delivered, bounded continuous density | delivered, bounded density | signed density at fixed `s` | no `μ` |
| (H-RP) reflection positivity | delivered: link reflections in all four directions (P8.1 form), all `β_s` (Theorem 6.3(a)) | delivered, all `θ` (Theorem 6.3(b)) | limit inherits it (Theorem 8.4 and 6.3(b)) | no `μ` |
| (H-class) density in `𝒜_{k_0}(g)`, `g ≤ g_*` | **fails** if the class consists of hypercubic-invariant densities: not invariant under exchanging time with a space axis, at every `(β_s, t_E)` (Theorem 7.3(a)); not invariant under odd translations if `β_s ≠ 0` (7.3(b)); never T0's Wilson measure (7.3(c)) | **fails** on the same condition for every `θ` outside a discrete subset of `R ∖ {0}`: not invariant under exchanging time with a space axis (Theorem 7.5); on that discrete set, not decided here | as for `μ_ex` | no `μ` |
| Uniformity in `a`, `L`; T0-rate | not hypotheses on `μ`; not delivered | same | same | same |

**About (H-class).** `𝒜_{k_0}(g)` is not pinned in the TOE files: `GA2_Y2.md` line 178, "the class and topology must be pinned before the claims are testable". Two fixed facts decide the row conditionally. First, T0's Wilson measure and every image of it under a hypercubic-covariant block map are hypercubic invariant (P8: "the Wilson measure is invariant under every torus isometry preserving the bare lattice"). Second, the frozen interface already lists the extension this file would need: "T0 is stated for Wilson SU(2); SU(5), SO(10), matter, anisotropy and matching are separate extensions" (`GA2_Y2.md` line 178). The tree-level coupling `g_cl² = 2(τ_E/|θ|)^{1/2}` is small only by a choice of angles, as `GB1QL.md` line 339 already says.

**The first failing step.**
- Through GB1QL's family with R-SUM (`τ_E > 0`): the target's lifts deliver (H-4D), (H-GI), (H-Haar) and (H-RP) exactly; the framework delivers them in the limit `s → ∞`. The first failing step is **(H-class), at invariance under the exchange of the time axis with a space axis**. Its root is Lemma 7.2: the Euclidean partner of the electric layer is the heat kernel, never a Wilson weight; and the tick fixes the anisotropy only up to the free step `λ` (Theorem 5.1(c)). Cube-face spatial structure breaks odd translations as well.
- At fixed `s`, through the framework's own registers: the first failing step is **(H-4D), at positivity of the transfer kernel**, for `a_0` below the threshold of Theorem 8.2.
- Through bounded R-GEN: the first failing step is **(H-4D), at finiteness of the partition function** (Theorem 5.2).

This replaces the hand-off's "(H-4D) first" (`GB1QL.md` line 343) by a reading-dependent answer: R-SUM moves the first failure to (H-class); bounded R-GEN keeps it at (H-4D).

### 9.2 Readings for the owner, four-tested

The four tests (`LW1_5_DRAFT.md` line 328, as quoted in `GB1QL.md` line 349): "(1) states or fixes a part's target; (2) open-ended; (3) settles a downstream physics question by premise; (4) adds structure or constants its own reasons do not need." A reading fails a test when the condition holds. P = pass, C = conditional, F = fail. Nothing is adopted.

| Reading | Text | Tests | Reasons |
|---|---|---|---|
| **R-SUM** (candidate) | "For GB1, the Hamiltonian of a tick written as an ordered product of layers `e^{-iτ_kK_k}`, with `K_k` the operators named in the law's data, is `Σ_k τ_kK_k`." | 1 P, 2 P, 3 C, 4 C | (1) It fixes no part's target: under it GB1E's properties are proved (Theorems 4.10, 6.3, 7.3), not assumed. (2) Closed: it applies to layered ticks written in named operators. (3) It fixes E-1 (which logarithm) by the law's notation; by `GB1.md` Theorem 2.1 that choice fixes every imaginary-time correlator. It settles neither the state (E-2) nor isotropy (Y3). (4) It reads the written value of `τ_E`, which the tick fixes only modulo `8π` (`4E²` has integer spectrum), and the lift needs `τ_E > 0`, a sign the tick does not fix. |
| Bounded R-GEN, scope widened to GB1 (the owner's SMG1 text) | `TOE_ASSEMBLY.md` line 261, unchanged, applied to GB1's ticks. | as recorded for SMG1: C P C C | Recorded for completeness. Under it (H-4D) fails for the Kogut–Susskind target and for the `s → ∞` limit (Corollary 5.3, item 3). Widening its scope is an owner decision; this file only reports the consequence. |
| **R-IA** (candidate) | "The Euclidean partner of a layered tick at Euclidean step `λ > 0` is the symmetric product of its layers with every angle multiplied by `−iλ`." | 1 P, 2 C, 3 C, 4 C | (1) It names no target. (2) `λ` is left open: one free positive constant per law (Theorem 5.1(c)). (3) It defines the Euclidean side (E-1 and E-3 at once) instead of deriving it. (4) It adds `λ`, which the tick does not fix; it needs `τ_E > 0`. Under it, `μ_loc` delivers (H-4D), (H-GI), (H-Haar), (H-RP) at every `λ` (Theorems 4.5, 6.3). |
| R-ISO (recorded, not proposed) | "Choose `λ = λ_iso`, the tree-level isotropic step (Proposition 7.4)." | 1 F, 2 P, 3 F, 4 C | (1) It fixes `λ` by T0's isotropy, the hand-off's target. (3) It settles Y3 at tree level by premise; Theorem 7.3(a) shows the measure is still not isotropic. |

## FINISH

**Proved** (pass 1; not yet distilled or refereed).
- Lemma 3.1 and Proposition 3.2: the R-SUM Hamiltonian `H` on a box (self-adjoint, compact resolvent, `Tr e^{-uH} < ∞` for `τ_E > 0`); what bounded R-GEN gives (`H_wr`, bounded).
- Lemmas 4.1-4.2: zonal kernels of `H_k` are characters of unitary representations; the `SU(2)` heat kernel is a nonnegative class function (maximum principle in `GB1QL.md`'s harmonic calculus). Lemma 4.4: Wilson weights (`β ≥ 0`) and heat kernels have positive character expansions.
- Theorem 4.5: the local lift `μ_loc[β_s, t_E]` (heat-kernel time, cube-face Wilson space) is a gauge-invariant probability measure with bounded continuous Haar density and exact transfer matrix `T_loc`.
- Theorem 4.9: `‖S_{a_0/n}^n − e^{-a_0H}‖_1 ≤ C(1 + log n)/n` (Trotter in trace norm). Theorem 4.10: the exact lift `μ_ex` of `e^{-a_0H}` exists, with the stated properties, and is the total-variation limit of coarse-grained local lifts.
- Theorem 5.1: the local transfer matrix is the symmetric tick at imaginary angles, up to one free positive constant `λ`. Theorem 5.2 and Corollary 5.3: a bounded gauge-invariant generator has no Euclidean lift (infinite partition function); what each reading gives for (H-4D).
- Lemma 6.1 (cube-face set under reflections); Lemma 6.2 (link-reflection positivity for positive character weights; port of the YM branch's B5); Theorem 6.3: both lifts are link-reflection positive in all four directions, for all `β_s` and all `θ` (the wrong sign via a centre change of variables); spatial site mirrors fail.
- Lemma 7.1 (zonal formula, multipliers, Wilson multipliers `I_{k+1}(2b)/b`); Lemma 7.2 (the heat kernel is never a Wilson weight); Theorem 7.3 (`μ_loc` is never invariant under time–space exchange, never under odd translations if `β_s ≠ 0`, never T0's Wilson measure); Proposition 7.4 (small-field stiffness; the unique tree-level isotropic step `λ_iso`); Theorem 7.5 (`μ_ex` is not time–space exchange invariant for `θ` outside a discrete subset of `R ∖ {0}`).
- Lemma 8.1, Theorem 8.2, Lemma 8.3: at fixed `s` the framework's band-limited transfer kernels are negative on an open set whenever `‖X − 1‖ < m_s/d_s` (every generator reading, small `a_0`; box-uniform at `θ = 0`); no finite register carries a gauge-covariant positive basis. Theorem 8.4: under R-SUM, `‖ι e^{-a_0H_s} ι^* − e^{-a_0H}‖_1 → 0` as `s → ∞`, and the framework's Euclidean correlators converge to those of `μ_ex`.

**Counterexamples.**
- To "the framework at fixed `s` supplies a probability measure through its own registers": Theorem 8.2, for `a_0` below the stated threshold, for every generator reading.
- To (H-4D) under bounded R-GEN widened to GB1: Theorem 5.2 with Proposition 3.2.
- To "the Euclidean lift is T0's isotropic Wilson measure at some coupling and step": Lemma 7.2 and Theorem 7.3.

**Open by name.**
- GB1E-ς: time–space exchange invariance of `μ_ex` for `θ` in the discrete zero set of `Δ` (Theorem 7.5), `θ ≠ 0`.
- (H-class) as a decision needs `𝒜_{k_0}(g)` pinned (`GA2_Y2.md` line 178); carried, not new.
- T0-start for anisotropic, cube-face starts (the extension `GA2_Y2.md` line 178 already names), or isotropy restoration from such starts (Y3); E-2 (the framework's state versus the ground state of `H`); VC1; T0-rate. Carried.
- A volume-uniform form of Theorem 8.4. Not attempted; Theorem 8.4 is per box.

**What changes downstream.**
- GB1 and GB1QL hand-off: Lemma H's "(H-4D) first" becomes reading-dependent. Under R-SUM (or R-IA for the local lift), the measure Lemma H asks for exists, with (H-GI), (H-Haar), (H-RP) proved, and the first failing step moves to (H-class), at time–space exchange invariance. Under bounded R-GEN widened to GB1, it stays at (H-4D). **Owner question:** which generator reading GB1 uses (section 9.2: R-SUM 1 P, 2 P, 3 C, 4 C; R-IA 1 P, 2 C, 3 C, 4 C; bounded R-GEN as recorded for SMG1).
- Y1 (`TOE_ASSEMBLY.md` line 613): for the `SU(2)` test-law target, `μ_loc` is a Euclidean representation on `Z³ × Z` with a local, gauge-invariant action, reflection positive in time (and in space), exact for the tick at imaginary angles, with one free constant `λ`. The framework's own registers give it only as `s → ∞`.
- Y3 and GA2: the lifts are anisotropic and cube-face. O(4) needs either isotropy restoration from such a start or T0-start extended to it; T0's isotropic start is not reached by choosing `λ` (Theorem 7.3(a) holds at every `λ`, including `λ_iso`).
- `GA2_Y2.md` line 176 (band-limited kernels): answered in the Hamiltonian regime: the framework's band-limited transfer kernels are not positive (Theorem 8.2).
- ST1 route B (reflection positivity of a Euclidean tick transfer): available for the `SU(2)` test-law target under R-IA (Theorems 5.1, 6.3(a)).
