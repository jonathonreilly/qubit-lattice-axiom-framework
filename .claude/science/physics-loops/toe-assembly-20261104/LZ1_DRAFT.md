lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# LZ1 with MT1-S: a common light cone for all species, pass 1

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of part LZ1 (with MT1-S) under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status. It adopts no law, reading, definition or specification. It changes no axiom and no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means that the argument is written out in full below; it is not yet distilled or refereed. A "[check]" is a tiny scratch computation in `/tmp/toe-lz1/`; it guides and never proves.

**Lane.** Claude Opus 5.5 (model id `claude-opus-5-5`), max reasoning effort, headless lane `mac-mini-toe-lane`. No subagents. One numeric check, run after `memory_pressure` showed 66 percent free.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local checkout, branch `claude/toe-assembly` (sparse), as given in the lane brief | `dfe1706ec0d6572406e9e1e326b8524216589229` |

No other branch was read.

**Files read, by line, at that commit.** All in `.claude/science/physics-loops/toe-assembly-20261104/`. `TOE_ASSEMBLY.md` lines 1-220 (axioms, target, working set, sections 3.1-3.5) and 300-368 (ST1, LZ1, BR1, MT1). `MT1.md` lines 1-140 (all). `MT1_REFEREE.md` lines 1-341 (all). `LW1.md` lines 1-250 (status, amendments, definitions, A1-B5), 320-400 (B10, B11, C1, B12), 401 (E1) and 474-512 (open statements). `LW1_5.md` lines 1-140 (status, definitions, the two laws, C-U), 160-260 (centre, singlets, filling, carry-over, B1-U) and 295-352. `CH1_5UQ.md` lines 1-100 (definitions, Theorems 2.1-3.3) and 218-226 (RC7). `TM1.md` lines 100-148 (Lemma 15, section 5). For format only: `Y2W_DRAFT.md` lines 1-45 and its section headers. SHA-256, first 16 hex digits: `TOE_ASSEMBLY.md` 8027d9d44eb5fcaf; `MT1.md` c8263124f7df9bea (the text the MT1 referee read); `MT1_REFEREE.md` 51acc331b9709faa; `LW1.md` 78280bd620800eac; `LW1_5.md` 7afb7ee2a52d91cd; `CH1_5UQ.md` 674c2ef458aac936; `TM1.md` 24e183db90eb5ab9.

**Working-set entries used, by name.** PS-1 read by PS-1c, only through the cell lifts of the two laws. PS-5 (five fermion modes per site). PS-6 and PS-6r, only through the link registers of `L5-U` and `L5-O[S_+]`. PS-7 and PS-7r, only in Corollary Z.3, to state a tension. The owner decision LW1-5-RQ (both laws live). Not used: PS-2, PS-3 and its refinements, PS-4, PS-11, PS-Ar.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and the working set are read plainly. Where a reading is needed, it is named and four-tested, and nothing is adopted.

**Results from other parts.** Rebuilt in this file, with credit: the centre elements and matter parity (F1-F4, from `MT1.md` Theorem 6 and `CH1_5UQ.md` RC7); the frozen projector (Corollary Z.2(b), from `CH1_5UQ.md` Theorem 3.1); the free-node classification (Lemma M.0, from the referee closure `MT1_REFEREE.md` C4); the filling count (Corollary Z.3, from `LW1_5.md` F-U); the even-translation lifts (section 1.1, from `LW1.md` A2). Quoted from frozen or about-to-freeze parts without rebuilding, each named where used: `MT1.md` Theorem 4 (input of Lemma M.0), `LW1_5.md` B1-U (the lifted cell group, input of Corollary Z.3), `LW1_5.md` H and Corollary SC.1 (Corollary Z.4 and Remark Z.5), and, outside any proof, `LW1.md` B12, `MT1.md` Theorems 7 and 10.

## Literature record

**Searches run (2026-11-06).** WebSearch, standard mode: (1) Chadha-Nielsen, Lorentz invariance as a low-energy phenomenon, RG convergence of speeds; (2) Anber-Donoghue, universal limiting speed; (3) Collins-Perez-Sudarsky-Urrutia-Vucetich, fine-tuning; (4) Isobe-Nagaosa, QED in solids, flow of light and electron speeds; (5) Bisio-D'Ariano-Perinotti, QCA theory of light; (6) Levin-Wen, emergent photons and electrons, speeds; (7) Polchinski 2011 comment; (8) anisotropic lattice QCD, separate quark and gauge anisotropy tuning; (9) Hilbert space fragmentation in lattice gauge theories; (10) charged sectors, Gauss law and dressing. No published theorem was found that a lattice symmetry forces one common speed across species. Every source found says the opposite: speeds of different multiplets are independent dimension-four parameters, made equal only by tuning, by a protecting symmetry (supersymmetry is the one example named), or by renormalization-group running that is logarithmic at weak coupling.

**Works used, with what was fetched.** None is load-bearing. Every result below is proved in this file.

| Work | arXiv | Fetched | Exact statement used |
|---|---|---|---|
| Anber, Donoghue, "The emergence of a universal limiting speed", Phys. Rev. D 83, 105027 (2011) | 1102.0789 | abstract page; PDF text of v2 | Eqs. (18)-(19): Yukawa beta functions, "c_b = c_f is an IR attractive line". Eqs. (51)-(54): relative speed difference η with β(η) = b g²η/(4π²c³) and a logarithmically running coupling. Page 2: "In the absence of any form of interactions between particles, their speeds are expected to be frozen as we run down to the IR." Abstract: "The differences normally vanish only logarithmically". |
| Collins, Perez, Sudarsky, Urrutia, Vucetich, Phys. Rev. Lett. 93, 191301 (2004) | gr-qc/0403053 | abstract page; PDF text of v4 | Abstract: Lorentz violation "at the percent level ... unless the bare parameters of the theory are unnaturally strongly fine-tuned". Page 2: "If the microscopic theory violates Lorentz invariance at the Planck scale, then generically we also get Lorentz violation at low energies without any suppression by powers of E/E_P"; "different fields have different values of c". |
| Polchinski, comment on arXiv:1106.1417 (2011) | 1106.6346 | PDF text of v2 | Page 2: "the spatial gradient terms for each of the 19 gauge multiplets. These lead to different 'speeds of light' for the different multiplets"; "a Lorentzian lattice with equal time and space steps has no such enhanced symmetry". Page 3: "Supersymmetry is the one known example [6, 7], in which both the space and time derivative kinetic terms arise from a single superfield." |
| Bisio, D'Ariano, Perinotti, "Quantum cellular automaton theory of light", Ann. Phys. 368, 177 (2016) | 1407.6928 | abstract page; PDF text of v1 | Eq. (7): Weyl automata A_k = exp[−i n_k·σ]. Eq. (9): n_k ≈ k/√3 at small k. Eq. (43): the composite photon has ω(k) = 2\|n_{k/2}\|. So the photon, built from two Weyl fermions, has the Weyl leading speed. |
| Bednik, Pujolàs, Sibiryakov, JHEP 11 (2013) 064 | 1305.0011 | abstract page only | Deviations from relativistic behaviour "power-law suppressed by the ratio of the infrared and ultraviolet scales", in strongly coupled holographic examples. |
| Iengo, Russo, Serone, JHEP 0911:020 (2009) | 0906.3477 | abstract page only | "Lorentz symmetry is not recovered at low energies with the accuracy needed to withstand basic experimental constraints", unless the Lorentz-breaking terms, "including δc², are unnaturally fine-tuned". |
| Coleman, Glashow, Phys. Rev. D 59, 116008 (1999) | hep-ph/9812418 | abstract page only | Perturbations "define the energy-momentum eigenstates and their maximal attainable velocities in the high-energy limit". The body was not fetched; any species-by-species detail is NOT VERIFIED. |
| Morrin, Ó Cais, Peardon, Ryan, Skullerud, Phys. Rev. D 74, 014505 (2006) | hep-lat/0604021 | abstract page only | "A method for nonperturbative renormalisation of the parameters in the anisotropic gauge and quark actions is presented." |
| Kijowski, Rudolph, Śliwa, Ann. Henri Poincaré 4, 1137 (2003) | hep-th/0203214 | abstract page only | Observables are "gauge-invariant elements satisfying the Gauss law"; irreducible representations are "labeled by the value of the total electric charge". |
| Horan, Lavelle, McMullan, Pramana 51, 317 (1998) | hep-th/9810089 | abstract page only | "a method to construct charged particles" (dressed charges). |
| Ciavarella, Bauer, Halimeh (2025) | 2502.03533 | abstract page only | Kogut-Susskind lattice gauge theories "give rise to Hilbert space fragmentation". A relative of the frozen stars of Corollary Z.2. |
| Chadha, Nielsen, "Lorentz invariance as a low-energy phenomenon", Nucl. Phys. B 217, 125 (1983) | none | library record only | NOT VERIFIED. Credited as the origin of the idea that speeds converge under the renormalization group, from secondary descriptions only. |
| Liberati, "Tests of Lorentz invariance: a 2013 update" | 1304.5795 | search snippet only | NOT VERIFIED. |

**Closest repo results.** `CH1_5UQ.md` Theorem 2.2 and RC7 (charged two-point functions vanish at separation; credit to that item's draft, distiller and referee) are the closest to Theorem P; Theorem P upgrades them from correlators to a statement about every band. `MT1_REFEREE.md` C4 is the base of Theorem M. `LW1_5.md` F-U (integer filling on periodic boxes) is the base of Corollary Z.3. The assembly quotes #9913: "no symmetry fixes the ratio of two species' dressed speeds" (`TOE_ASSEMBLY.md` line 327); that PR was not read here.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 320, LZ1(a): "For the law `L` and its zoom, there are `c > 0` and `p >= 2` such that, for every light species (fermions, gauge bosons, graviton), the low-momentum dispersion is `E = c|k|(1 + O((a|k|)^p))` with the same `c`; the leading Lorentz-violating operator of each sector has mass dimension at least `4 + p`, with its coefficient computed at one loop or better [**open input LZ1-i**: a mechanism that fixes one common `c` across species]; ...".

`TOE_ASSEMBLY.md` line 332, LZ1(e): "LZ1-i (#9913 shows symmetry alone does not fix it; a dynamical attractor is needed ...)".

`MT1.md` line 134: "**MT1-S (open).** On either five-mode law, in the VC1 vacuum, the light fermion-odd excitations have a node whose leading generator satisfies ER's Clifford one-cone condition."

`MT1_REFEREE.md` line 301: "neither the working set nor `MT1.md` defines "the leading generator of the light fermion-odd excitations" of an interacting state. On L5-O the gauge dressing of those excitations also needs a specification (C7)."

`TOE_ASSEMBLY.md` line 214 (LW1-5-RQ): "The owner chose: **keep both live.**"

## 0.1 Outcome

**MT1-S is false in the vacuum's own representation, on both laws.** Read there (reading R-loc, the plain reading of "in the VC1 vacuum"), every fermion-odd band of every locally gauge-invariant, cell-invariant, stationary state is flat (Theorem P). Its leading generator is zero, so ER's Clifford condition, which needs `v > 0`, fails. The reason is Gauss's law: the local centre gauge transformations commute with the tick, so every odd excitation made by a local operator leaves a charge pattern that never moves. The same theorem kills the fermion clause of LZ1's first statement in that reading: no fermion is a propagating light species of the vacuum representation. Both statements need a charged-sector prescription, named here R-CS. CH1 already carries the same owner question.

**Under R-CS, MT1-S reduces to one representation statement.** On `L5-U` at `μ = 0 = τ_E`, a light charged band whose node fibre carries the free node representation once has one isotropic cone (Theorem M, built on `MT1_REFEREE.md` C4). Multiplicity one is needed: two copies admit two cones of any two speeds (Example S.3).

**Symmetry cannot give LZ1 its common speed.** Speeds are invariants of symmetry orbits of bands, and the symmetries impose no relation between orbits (section 4: Lemma S.1, Proposition S.2). No symmetry of a PS-1 law mixes time and space. No symmetry of the vacuum representation maps a propagating boson band into the odd sector (Proposition S.4), so the supersymmetry route is closed there.

**LZ1 forces the vacuum to be sharp on conserved local operators.** Read spectrally (R-SC), LZ1 forbids zero-energy states at small nonzero momentum, so the vacuum must be dispersion-free on every conserved local gauge-invariant operator (Theorem Z). On `L5-U` this applies to the Gauss charges `Q_x`. With site-transitive invariance it forces integer filling, so PS-7's half filling fails (Corollary Z.3). So LZ1 read spectrally, PS-7, and a site-transitive vacuum whose Gauss-charge correlations decay exponentially cannot all hold on `L5-U` (Corollary Z.3′).

**Also proved.** The dressed `L5-O[S_+]` tick has an antiunitary symmetry `Θ_O` for all constants (Proposition O); the MT1 referee listed "no antiunitary symmetry of the dressed tick is known" as a failing step on `L5-O`.

**Open.** LZ1-i, one speed for all propagating light species (all bosonic under R-loc), after three named attacks (section 7). Four candidate closing conditions are four-tested; none passes all four (section 6). The kill attempt, two propagating light bands with different speeds in an admissible interacting law, failed at a named step; it is a failed search, not a no-go.

---

## 1. The question made exact

### 1.1 Laws and the facts used

The laws are `L5-U[m]`, `1 ≤ m ≤ 9`, and `L5-O[S_+]`, as stated in `LW1_5.md` section 2, and `L_cube` (`LW1.md` section 1) where noted. A *gauge-invariant update of the same form* is the base tick `U_0 = W_E M_o M_e` followed by finitely many layers of finite-support gates, each gate commuting with every local gauge transformation and each layer covariant under the cell translations `τ_β` below. This class contains every plaquette class that GA1-P-5 may supply, since GA1-P-5 asks for a covariant gauge-invariant class. Its tick automorphism is `α(A) = U*AU` on local `A`, extended as in `LW1.md` E1.

Cell vectors are `β ∈ Z³`. The lift of the translation by `2β` is `τ_β`. `LW1.md` line 209 (A2): "Even translations preserve its phases exactly." Indeed an even translation maps each tiling to itself, and the edge signs `η_i(x) = (−1)^{Σ_{j<i} x_j}` depend only on parities of coordinates. So `τ_β` moves every generator at `z` to the same generator at `z + 2β`, and `τ_β∘α = α∘τ_β` for both base ticks (`LW1_5.md` B1-U and A2-5 carry this to five modes) and, by the covariance of the added layers, for every gauge-invariant update of the same form.

**Centre elements.** One local unitary `c_z` per site:
- `L5-U`: `c_z = e^{iπQ_z}`, with `Q_z = N_z + Σ_{ℓ∋z} p_{ℓ,z}` (matter number at `z` plus the rishon numbers of the six `z`-ends);
- `L5-O[S_+]`: `c_z = ω_z := ∏_{j=1}^{5} exp(iπ 𝒢^{2j−1,2j}_z)`, the lift of `−1_{10}` at `z`;
- `L_cube`: `c_z = e^{iπ𝒢_z}`.

These are the centre elements named in `MT1_REFEREE.md` edit E7. The following facts are rebuilt here.

**F1 (action on generators).** `Ad c_z` multiplies by `−1` every matter mode at `z` and every link generator at a `z`-end of a link at `z`: the rishons `r^{ℓ,z}_k` for `L5-U`, the Majoranas `η^{ℓ,z}_a` for `L5-O`. It fixes every other generator.

*Proof.* `L5-U`: `e^{iπQ_z} = (−1)^{Q_z}` is a function of number operators, hence even. It anticommutes with each mode that `Q_z` counts and commutes with every other mode. `L5-O`: `[M^{12}, γ_1] = −iγ_2` and `[M^{12}, γ_2] = iγ_1` (`LW1_5.md` section 1 gives `[M^{ab},γ_c] = i(δ_{bc}γ_a − δ_{ac}γ_b)`), so `e^{iθM^{12}}γ_1e^{−iθM^{12}} = γ_1 cos θ + γ_2 sin θ`. At `θ = π` the pair goes to minus itself. `𝒢^{cd}_z = M^{cd}_z + Σ_ℓ L^{cd}_{ℓ,z}` rotates the matter Majoranas at `z` and each `z`-end set of link Majoranas in the same way (`LW1_5.md` Q and G). The product over the five planes negates all ten matter Majoranas at `z` and all ten `z`-end Majoranas of each link at `z`. The generators at other sites and other ends commute with `ω_z`. `L_cube`: `𝒢_z = n_z + Σ_{out} E_ℓ − Σ_{in} E_ℓ` has integer spectrum (`CH1_5UQ.md` RC7, instance (2)), `[E_ℓ, J_ℓ] = J_ℓ`, so `Ad e^{iπ𝒢_z}` negates `c_z` and the operators `J_ℓ, J_ℓ^†` of the six links at `z`, and fixes every `E_ℓ`. For `L_cube`, read "link generator at a `z`-end" in F1-F4 as "`J_ℓ` or `J_ℓ^†` of a link at `z`"; each link operator then gets one sign from each end. ∎

**F2 (gauge invariance).** Every gate of a gauge-invariant update commutes with every `c_z`, so `Ad c_z∘α = α∘Ad c_z`.

*Proof.* `c_z` is a local gauge transformation. For the base gates directly: an `L5-U` hop term `c†_{y,j} r^y_j r^{x†}_k c_{x,k}` contains exactly two generators at each of its ends `x` and `y` (matter and rishon), so by F1 it is fixed by `Ad c_x` and `Ad c_y`. An `L_cube` hop `c_y^† J_ℓ c_x` likewise gets two signs from each end. An `L5-O` hop term `γ_{y,a} η^y_a η^x_b γ_{x,b}` (`U^{ab} = 2T_{a,10+b} = iη^y_aη^x_b`, `LW1_5.md` line 80) is fixed in the same way. `L5-U`'s `W_E` is diagonal in end numbers. `L5-O`'s `Γ^x = i^5 η^x_1⋯η^x_{10}` has ten generators at one end. ∎

**F3.** The `c_z` are even and commute pairwise; `(Ad c_z)²` is the identity; `τ_β∘Ad c_z = Ad c_{z+2β}∘τ_β`. All follow from F1 and the form of `τ_β`.

**F4 (matter parity; `MT1.md` Theorem 6, `CH1_5UQ.md` RC7).** Let `A` be local and let `Λ` be finite and contain every matter site of `A` and both ends of every link of `A`. Then `θ(A) = Ad(∏_{z∈Λ} c_z)(A)`.

*Proof.* By F1 the product negates each matter generator in `Λ` once and each generator of a link of `A` twice. A link operator of `L5-U` preserves the link's total rishon number, so each of its terms has an even number of rishon factors; a link operator of `L5-O[S_+]` is an even product of Majoranas. So link factors are fixed and matter is acted on by `θ`. ∎

### 1.2 States and their representations

**D1 (states used).** A state `ω` of the quasi-local algebra `𝔄` is a *D1 state* if it is stationary (`ω∘α = ω`), cell-invariant (`ω∘τ_β = ω` for all `β`) and centre-invariant (`ω∘Ad c_z = ω` for all `z`). Every locally gauge-invariant state is centre-invariant. Local gauge invariance means "invariance of a state under conjugations, not a prescribed zero-charge Gauss sector" (`LW1.md` line 124).

Let `(H, π, Ω)` be the GNS triple. As in `CH1_5UQ.md` line 26, define `Ũπ(A)Ω = π(α(A))Ω`, and likewise `T_βπ(A)Ω = π(τ_β(A))Ω` and `U_zπ(A)Ω = π(Ad c_z(A))Ω`. Each map is an automorphism preserving `ω`, so each is isometric on `π(𝔄)Ω` with dense range, and extends to a unitary. They fix `Ω` and satisfy

\[
\tilde U T_\beta = T_\beta\tilde U,\quad \tilde U U_z = U_z\tilde U,\quad T_\beta U_z T_\beta^{-1} = U_{z+2\beta},\quad U_zU_{z'} = U_{z'}U_z,\quad U_z^2 = 1 .
\]

`H` is separable: the local operators with rational coefficients in finite matrix units are dense in `𝔄`. By F4, `ω∘θ = ω` on local operators, so fermion parity has a unitary `U_θ` fixing `Ω`. Put `H_odd = {v : U_θ v = −v}`, the closure of `π(𝔄_odd)Ω`, and `H_even` likewise. Put `H_phys` for the closure of `π(𝔄^G)Ω`, where `𝔄^G` is the gauge-invariant quasi-local algebra.

### 1.3 Bands, nodes and cone speeds

Write `K ∈ T³ = (−π, π]³` for cell momentum. On `L²(T³; X)`, `M_β` multiplies by `e^{iK·β}`, and `M_V` multiplies by a matrix function `V(K)`.

**D2 (band).** A band of `ω` is a triple `(d, F, V)`: `d ≥ 1`; `F : L²(T³; C^d) → H` an isometry; `V : T³ → U(d)` continuous; with `T_β F = F M_β` for all `β` and `Ũ F = F M_V`. Its image `B = F(L²)` is closed and invariant under `Ũ` and every `T_β`.

**D3 (node, leading generator, cone speed).** A node is a point `K_0` with `V(K_0) = 1` near which `V` is `C¹`. Near `K_0` put `h(K) = i log V(K)` (principal logarithm, analytic on unitaries near `1`). The leading generator is the Hermitian triple `N_j = ∂h/∂K_j (K_0)`, `j = 1, 2, 3`. The band has *one isotropic cone of speed `v > 0`* when `{N_i, N_j} = 2v²δ_{ij}`; this is ER's Clifford condition (`MT1.md` line 32). The band *propagates* at `K_0` when some `N_j ≠ 0`. It is *flat* at `K_0` when `V ≡ 1` on a neighbourhood of `K_0`.

**D4 (light species).** A light species of `ω` is a band with a node whose image lies in `H_even` (bosonic) or in `H_odd` (fermionic). Its speeds at the node are the moduli of the nonzero eigenvalues of `Σ_j n_jN_j` over unit vectors `n`. A set of light species *shares one cone* when each has one isotropic cone and all have the same `v`.

**D5 (symmetries and orbits).** A symmetry of `(law, ω)` is a unitary or antiunitary `S` on `H` with `SΩ = Ω`, `SŨS^{-1} = Ũ` and `ST_βS^{-1} = T_{Qβ}` for a signed permutation matrix `Q` depending on `S`. For a group `𝒮` of symmetries, two bands lie in one orbit when some `S ∈ 𝒮` maps one image onto the other. The definition requires `S` to commute with `Ũ`. For an ordered PS-1 update that is forced: `LW1.md` line 391 (B12): "A symmetry of an ordered PS-1 update that maps each time slice to a time slice cannot move the time root off its line."

### 1.4 Three readings, named and not adopted

- **R-loc.** MT1-S and LZ1's first statement are read in the GNS representation of the vacuum `ω`, with D2-D4. This is the plain reading of "in the VC1 vacuum" (`MT1.md` line 134).
- **R-CS.** A charged-sector prescription: a rule that gives, for the vacuum `ω`, the representations or the gauge-invariant pair constructions in which charged fermions are described. This file names R-CS and proposes none. It is the owner question already open in CH1: "the charged-correlator prescription of IR (an owner question)" (`CH1_5UQ.md` line 13).
- **R-SC.** LZ1's first statement read spectrally on the physical sector: if `ω` satisfies it, there is `δ > 0` such that no nonzero `Ũ`-fixed vector of `H_phys` has `T`-spectral measure carried by `{0 < |K| < δ}`. Such a vector is an excitation of zero energy at low nonzero momentum; a light species containing it has `E = 0 ≠ c|k|`. The global variant **R-SC\*** asks that every `Ũ`-fixed vector of `H_phys` be `T`-invariant.

The four tests for D2-D5 and for these readings are in section 6.

---

## 2. Theorem P: charges made by local operators never move

### 2.1 Patterns

A *pattern* is a map `κ : Z³ → {±1}` with finitely many values `−1`. Write `D(κ) = {z : κ(z) = −1}`, `1` for the trivial pattern, and `(τ_β κ)(z) = κ(z − 2β)`. Put `H(κ) = {v ∈ H : U_z v = κ(z) v for all z}`.

**Lemma P.1 (patterns of a local operator).** Let `A` be local and `Λ` as in F4. For `ε ∈ {±1}^Λ` put
\[
A_\varepsilon = 2^{-|\Lambda|}\sum_{S\subseteq\Lambda}\Big(\prod_{z\in S}\varepsilon_z\Big)\,\mathrm{Ad}\Big(\prod_{z\in S}c_z\Big)(A).
\]
Then `A = Σ_ε A_ε`; `Ad c_z(A_ε) = ε_z A_ε` for `z ∈ Λ`; `Ad c_z(A_ε) = A_ε` for `z ∉ Λ`. If `A` is fermion odd, every nonzero `A_ε` has `∏_{z∈Λ} ε_z = −1`, so its pattern is nontrivial.

*Proof.* By F3 the maps `Ad c_z`, `z ∈ Λ`, are commuting involutive automorphisms: a representation of `(Z_2)^Λ` on `𝔄`. `A_ε` is the projection onto the character `ε`. The identity `Σ_ε ∏_{z∈S} ε_z = 2^{|Λ|}` if `S = ∅` and `0` otherwise gives `A = Σ_ε A_ε`. Replacing `S` by its symmetric difference with `{z}` gives `Ad c_z(A_ε) = ε_z A_ε`. For `z ∉ Λ`, `c_z` acts on matter at `z` and on `z`-ends; no link of `A` has an end at `z`, since `Λ` contains both ends of every link of `A`. `c_z` is even, so it commutes with `A_ε`. If `A` is odd, so is `A_ε`, because `θ` commutes with each `Ad c_z`. F4 gives `−A_ε = θ(A_ε) = (∏_z ε_z) A_ε`. ∎

**Lemma P.2 (pattern decomposition).** `H` is the orthogonal sum of the `H(κ)` over all patterns. Each `H(κ)` is `Ũ`-invariant and `T_β H(κ) = H(τ_β κ)`. The odd sector lies in `H_nt := ⊕_{κ ≠ 1} H(κ)`.

*Proof.* Each `U_z` is a self-adjoint unitary, so its `±1` eigenspaces are orthogonal; two different patterns differ at some `z`, so `H(κ) ⊥ H(κ')`. For local `A`, Lemma P.1 and `U_zΩ = Ω` give `π(A_ε)Ω ∈ H(κ_ε)`, with `κ_ε = ε` on `Λ` and `1` off `Λ`. So `π(A)Ω` is a finite sum of vectors in the `H(κ)`. Local operators are dense in `𝔄` and `Ω` is cyclic, so the closed sum is `H`. `Ũ` commutes with every `U_z`. For `v ∈ H(κ)`, `U_z T_β v = T_β U_{z−2β} v = κ(z − 2β) T_β v`. For odd local `A`, every component has a nontrivial pattern by Lemma P.1; `H_nt` is closed, so it contains `H_odd`. ∎

**Lemma P.3 (free orbits).** If `κ ≠ 1` and `β ≠ 0`, then `τ_β κ ≠ κ`.

*Proof.* `τ_β κ = κ` means `D(κ) + 2β = D(κ)`, hence also `D(κ) − 2β = D(κ)`. `D(κ)` is finite and nonempty; let `z` be its lexicographically largest element. Both `z + 2β` and `z − 2β` lie in `D(κ)`, and one of them is lexicographically larger than `z` unless `β = 0`. ∎

### 2.2 The flat structure of the charged part

**Proposition P.4.** Choose one pattern `κ_O` in each orbit `O` of nontrivial patterns under the cell translations. Put `𝒦 = ⊕_O H(κ_O)` and `W = Ũ|_𝒦`. Then there is a unitary `Φ : L²(T³; 𝒦) → H_nt` with
\[
\Phi^{-1} T_\beta \Phi = M_\beta,\qquad \Phi^{-1}\tilde U\Phi = 1\otimes W\quad(\text{multiplication by the constant } W).
\]

*Proof.* By Lemmas P.2 and P.3, `H_nt = ⊕_O ⊕_β T_β H(κ_O)`, an orthogonal sum in which `T_β` maps `H(κ_O)` unitarily onto `H(τ_β κ_O)` and the pairs `(O, β)` label distinct patterns. So `(u_β)_β ↦ Σ_β T_β u_β` is unitary from `ℓ²(Z³; 𝒦)` onto `H_nt`. Compose with the Fourier map `f(K) = Σ_β u_β e^{iK·β}` (Plancherel). A shift `u_β ↦ u_{β−β'}` becomes `M_{β'}`. `Ũ Σ_β T_β u_β = Σ_β T_β Ũ u_β`, and `Ũ` preserves `𝒦`. ∎

**Lemma P.5 (bands in `H_nt` are flat at nodes).** Let `(d, F, V)` be a band with image in `H_nt`, let `K_0` be a node, and let `V` be `C¹` on a connected open `𝒰 ∋ K_0`. Then `V ≡ 1` on `𝒰`. Its leading generator is zero.

*Proof.* (a) *Decomposition.* `G = Φ^{-1}F` is an isometry with `G M_β = M_β G`. Let `e_i` also denote the constant function with value `e_i`, and put `g_i = G(e_i) ∈ L²(T³; 𝒦)`. For trigonometric polynomials `p`, `G(p e_i) = p g_i`. Isometry and polarization give `∫ \bar q r ⟨g_i, g_j⟩ dK = δ_{ij} ∫ \bar q r dK` for all trigonometric polynomials `q, r`. The products `\bar q r` include all trigonometric polynomials (take `q = 1`), so every Fourier coefficient of the integrable function `⟨g_i(K), g_j(K)⟩ − δ_{ij}` vanishes, and it is zero almost everywhere. Define `F̃(K) e_i = g_i(K)`: an isometry `C^d → 𝒦` for almost every `K`. Then `G f = F̃(·) f(·)` for trigonometric-polynomial `f`, and for all `f` by continuity.

(b) *Intertwining.* `ŨF = F M_V` gives `(1 ⊗ W) G = G M_V`. Applied to `e_i`: `W F̃(K) = F̃(K) V(K)` for almost every `K`. So `F̃(K) C^d` is a `d`-dimensional `W`-invariant subspace on which `W` is unitarily equivalent to `V(K)`.

(c) *Countable spectrum.* A unitary on a finite-dimensional invariant subspace is diagonalizable with eigenvalues of `W`. The eigenvalue set `σ` of `W` is countable, since eigenvectors for distinct eigenvalues are orthogonal in the separable `𝒦`. So, for almost every `K`, all eigenvalues of `V(K)` lie in `σ`, and for each `k` the numbers `Re tr V(K)^k` and `Im tr V(K)^k` lie in a countable set.

(d) *A `C¹` function that takes countably many values almost everywhere is constant.* Let `f` be real and `C¹` on the connected open `𝒰`, with `f(K) ∈ C` for almost every `K` and `C` countable. Suppose `∇f(K_1) ≠ 0`. Some partial derivative, say `∂_1 f`, is nonzero at `K_1`, hence on a small closed box `Q ⊂ 𝒰` around `K_1`. On each segment of `Q` parallel to the first axis, `f` is strictly monotone, so it takes each value of `C` at most once; the set of points of the segment where `f ∈ C` is countable and has length zero. `f^{-1}(C)` is a countable union of closed sets, hence measurable, and Fubini's theorem gives it measure zero in `Q`. That contradicts `f ∈ C` almost everywhere on `Q`. So `∇f ≡ 0` on `𝒰` and `f` is constant.

(e) By (c) and (d), `tr V(K)^k` is constant on `𝒰` for `k = 1, …, d`. Newton's identities give the characteristic polynomial from these traces, so the spectrum of `V(K)` is constant on `𝒰`. At `K_0` it is `{1}`. A unitary whose spectrum is `{1}` is the identity. So `V ≡ 1` on `𝒰`, `h ≡ 0` and `N_j = 0`. ∎

### 2.3 The theorem and what it decides

**Theorem P (pinned charges).** Let the update be any gauge-invariant update of `L5-U[m]`, `L5-O[S_+]` or `L_cube` form, with any constants, and let `ω` be a D1 state. Then:
1. `H = H(1) ⊕ H_nt`; on `H_nt` the cell translations act by multiplication and the tick by a constant, as in Proposition P.4.
2. Every band with image in `H_nt` is flat at each node, on the connected neighbourhood where it is `C¹`.
3. Every fermionic light species of `ω` is flat at its node; its leading generator is zero.
4. Every vector of `H(1)` is fermion even.

*Proof.* Items 1-3 are Lemma P.2, Proposition P.4 and Lemma P.5, with `H_odd ⊂ H_nt`. For item 4: for local `A` with trivial pattern, F4 gives `U_θ π(A)Ω = π(θ(A))Ω = ∏_{z∈Λ} U_z π(A)Ω = π(A)Ω`. Every vector of `H(1)` is a limit of such vectors (project the vectors `π(A)Ω` onto `H(1)` using Lemma P.2). ∎

**What item 3 means.** A local odd operator creates a matter excitation together with a change of Gauss charge at its sites. The tick moves the matter, but the Gauss pattern stays where it was made, because each `U_z` commutes with `Ũ`; the matter stays tied to it by flux. So the charge pattern labels a conserved position, and cell momentum only sees that label. This is the band form of `CH1_5UQ.md` Theorem 2.2 and RC7, whose two-point statement it contains: for local odd `ψ` and disjoint translates, `⟨π(τ_βψ)Ω, Ũ^n π(τ_{β'}ψ)Ω⟩ = 0` for every `n`, because the pattern components of the two vectors lie in different `H(κ)`. It agrees with the standard fact that charged states are not made from a gauge-invariant vacuum by local operations (Kijowski, Rudolph and Śliwa, arXiv:hep-th/0203214; Horan, Lavelle and McMullan, arXiv:hep-th/9810089; not load-bearing).

**Corollary P.6 (MT1-S under R-loc is false).** Let `ω` be any VC1 vacuum of either law that is a D1 state; every locally gauge-invariant one is. Then no fermionic light species of `ω` propagates. Read in `ω`'s representation, MT1-S asserts a fermion-odd node whose leading generator satisfies `{N_i, N_j} = 2v²δ_{ij}` with `v > 0`; Theorem P gives `N_j = 0`. So MT1-S is false under R-loc, on both laws, for every value of the constants and every plaquette class. The same holds for MT1(a)(2) read with ER for "local excitations" (`TOE_ASSEMBLY.md` line 354), because ER assigns a spin only under the Clifford condition.

**Corollary P.7 (LZ1's fermions under R-loc).** Under R-loc, the light species of LZ1's list that are fermions are flat. So LZ1's first statement, with `c > 0` for "fermions", is false under R-loc for every vacuum that is a D1 state, unless the vacuum has no fermionic light species at all; in that case the fermion clause is empty. Either way the fermion clause needs R-CS.

**What survives.** Two places can still show propagating charged fermions. (i) Gauge-invariant pair operators: a matter mode at `x`, a string of link operators, and a matter mode at `y`. Such an operator has trivial pattern, so its vectors lie in `H(1)` and may propagate; the single-fermion dispersion is then read from the two-fermion states, as an edge of a continuum or through a bound state. (ii) Charged superselection sectors: representations other than the vacuum's, with the flux taken to infinity. Both are instances of R-CS. Theorem P says nothing against either.

---

## 3. Theorem Z: LZ1 forces the vacuum to be sharp on conserved local operators

### 3.1 Conserved local operators give zero-energy states

**Lemma Z.1.** Let `ω` be stationary and cell-invariant, and let `Y` be local with `α(Y) = Y`. Put `Y' = Y − ω(Y)`, `v_β = π(τ_β(Y'))Ω` and `C(β) = ⟨v_0, v_β⟩ = ω(Y'^* τ_β(Y'))`. Let `E` be the joint spectral measure of `T_{e_1}, T_{e_2}, T_{e_3}` on `T³`, so that `T_β = ∫ e^{iK·β} dE(K)`, and let `μ(·) = ⟨v_0, E(·) v_0⟩`. Then `Ũ v_β = v_β`, `T_β v_0 = v_β`, `C(β) = ∫ e^{iK·β} dμ(K)` and `μ(T³) = C(0) = ω(Y'^*Y')`.
- (a) If `C(β) → 0` as `|β| → ∞` and `C(0) > 0`, then `E(T³ \ {0}) v_0` is a nonzero `Ũ`-fixed vector orthogonal to every `T`-invariant vector.
- (b) If `|C(β)| ≤ A e^{−κ|β|}` for some `A, κ > 0` and `C(0) > 0`, then for every `δ > 0` the vector `E({0 < |K| < δ}) v_0` is nonzero and `Ũ`-fixed.

*Proof.* Cell covariance of the tick gives `α(τ_β(Y)) = τ_β(α(Y)) = τ_β(Y)`, so `Ũ v_β = v_β`; and `T_β v_0 = v_β` by definition. The formula for `C` is the spectral theorem for the commuting unitaries `T_{e_j}`. `Ũ` commutes with every `T_β`, hence with every spectral projection `E(Δ)`, so each `E(Δ) v_0` is `Ũ`-fixed. (a) The range of `E({0})` is the set of `T`-invariant vectors. If `μ(T³ \ {0}) = 0`, then `μ = C(0)δ_0` and `C(β) = C(0)` for all `β`, contrary to `C(β) → 0`. (b) Exponential decay makes `c(K) = (2π)^{−3} Σ_β C(β) e^{−iK·β}` converge uniformly on a complex strip around `T³`, so `c` is real-analytic. `μ` and `c(K)dK` have the same Fourier coefficients, so `μ = c(K) dK`, with `c ≥ 0` and `∫ c = C(0) > 0`. A real-analytic function on the connected `T³` that vanishes on a nonempty open set vanishes everywhere. So `∫_{0<|K|<δ} c > 0`. ∎

**Theorem Z.** Let `ω` be stationary and cell-invariant, and let `Y ∈ 𝔄^G` be local with `α(Y) = Y`.
- (i) If `ω` satisfies R-SC\* and `ω(Y'^*τ_β(Y')) → 0`, then `ω(Y^*Y) = |ω(Y)|²`.
- (ii) If `ω` satisfies R-SC and `ω(Y'^*τ_β(Y'))` decays exponentially in `|β|`, then `ω(Y^*Y) = |ω(Y)|²`.

*Proof.* `τ_β` maps `𝔄^G` onto itself, so `H_phys` is invariant under every `T_β` and `T_β^*`, and the spectral projections `E(Δ)` preserve `H_phys`. `v_0 ∈ H_phys`. If `C(0) > 0`, Lemma Z.1 gives a vector in `H_phys` that R-SC\* (case i) or R-SC (case ii) forbids. So `C(0) = ω(Y'^*Y') = ω(Y^*Y) − |ω(Y)|² = 0`. ∎

In words: under R-SC, every conserved local gauge-invariant operator is dispersion-free in the vacuum, and `π(Y)Ω = ω(Y)Ω`.

### 3.2 `L5-U`: Gauss charges and frozen stars

**Corollary Z.2.** (a) For every gauge-invariant update of `L5-U` form, `Q_x ∈ 𝔄^G` and `α(Q_x) = Q_x`. (b) For the base tick of `L5-U[m]`, any `m`, `ε`, `μ`, `τ_E`, the frozen projector `P_x` defined below lies in `𝔄^G`, satisfies `α(P_x) = P_x`, and is neither `0` nor `1`. So a vacuum as in Theorem Z has every `Q_x` sharp and `ω(P_x) ∈ {0, 1}` for every `x`.

*Proof.* (a) `Q_x` is the generator `𝒢^T_x` of `LW1_5.md` line 87 with `T = 1`, the central `U(1)` of `U(5)_x`. It commutes with every gauge generator, so it is gauge invariant. Each gate commutes with `e^{itQ_x}` for all real `t`; on the finite-dimensional local space this gives `[gate, Q_x] = 0`.

(b) This rebuilds `CH1_5UQ.md` Theorem 3.1 (credit to that item's draft, distiller and referee). On the unconstrained Fock space of matter and rishons put, for each link `ℓ` at `x`, `φ_{ℓ,x} = Σ_k r^{ℓ,x†}_k c_{x,k}`. Put `K_x = Σ_{ℓ∋x}(φ^*_{ℓ,x}φ_{ℓ,x} + φ_{ℓ,x}φ^*_{ℓ,x})`, `F_x = ker K_x`, and let `P_x` project onto `F_x`.
- Each term of `K_x` is positive and preserves `N_x` and every end number `p_{ℓ,x}`. So `P_x` commutes with the link-number constraints and restricts to an operator of the law. `F_x` is the common kernel of all `φ_{ℓ,x}` and `φ^*_{ℓ,x}`, since `⟨v, K_x v⟩ = Σ_ℓ (‖φ_{ℓ,x} v‖² + ‖φ^*_{ℓ,x} v‖²)`.
- `U(5)_x` acts on `c_x` and on each `r^{ℓ,x}` by the same matrix (`𝒢^T_x = c_x^† T c_x + Σ_ℓ r^†_{ℓ,x} T r_{ℓ,x}`), so each `φ_{ℓ,x}` is invariant, and so are `K_x` and `P_x`. Gauge transformations at other sites act on other modes.
- For `ℓ = (x, y)`: `h_ℓ = φ^*_{ℓ,y}φ_{ℓ,x} + φ^*_{ℓ,x}φ_{ℓ,y}`, because `φ^*_{ℓ,y}φ_{ℓ,x} = Σ_{jk} c^†_{y,j} r^y_j r^{x†}_k c_{x,k}` is the first term of `h^U_ℓ` (`LW1_5.md` line 87) and the second is its adjoint.
- `[φ_{ℓ,x}, φ^*_{ℓ,y}] = 0`. Indeed `r^{x†}_k c_{x,k} c^†_{y,j} r^y_j = −r^{x†}_k c^†_{y,j} c_{x,k} r^y_j = −c^†_{y,j} r^{x†}_k r^y_j c_{x,k} = c^†_{y,j} r^y_j r^{x†}_k c_{x,k}`. The steps use: matter modes at different sites anticommute; matter commutes with rishons; the distinct rishon modes `r^{x}_k` and `r^{y}_j` of one link anticommute. Taking adjoints, `[φ_{ℓ,y}, φ^*_{ℓ,x}] = 0`.
- For `v ∈ F_x`: `h_ℓ v = φ^*_{ℓ,y}(φ_{ℓ,x} v) + φ_{ℓ,y}(φ^*_{ℓ,x} v) = 0`. So `h_ℓ P_x = 0`, and `P_x h_ℓ = (h_ℓ P_x)^* = 0`. The same holds when `x` is the target of `ℓ`.
- Split each cube generator as `H_C = H_C^x + H_C^{rest}`, the links of `C` at `x` and the others. `H_C^x P_x = P_x H_C^x = 0`. `H_C^{rest}` is even and acts on other matter and other registers, so it commutes with `P_x`. Hence `[e^{−iaH_C}, P_x] = 0`. `W_E` is diagonal in end numbers, which commute with `P_x`. So the base tick commutes with `P_x`, and `α(P_x) = P_x`.
- `F_x ≠ 0`: with `a = max(0, m − 5)`, the occupation vector with matter set `A` at `x` and set `A` at every `x`-end, `|A| = a`, is killed by every `φ_{ℓ,x}` and `φ^*_{ℓ,x}` (each move lands on an occupied mode); the `y`-ends then hold `m − a ≤ 5` rishons. `F_x ≠` everything: take matter `{1}` at `x` and, at one `x`-end, a set of size `a ≤ 4` inside `{2, …, 5}`; then `φ_{ℓ,x}` moves flavour `1` into an empty mode and gives a nonzero vector.

A projector is dispersion-free exactly when `ω(P_x) ∈ {0, 1}`. ∎

**Corollary Z.3 (integer filling).** Let `ω` be a state of a gauge-invariant update of `L5-U[m]` form in which every `Q_x` is dispersion-free. Suppose `ω` is invariant under the lifted cell group `𝒢 = 2Z³ ⋊ O_{c_0}`. Then `ω(N_x) = q − 3m` for one integer `q` and all `x`; in particular `ω(N_x) ≠ 5/2`. If `ω` is only cell-invariant, then `Σ_{x∈C_0} ω(N_x) = Σ_{x∈C_0} q_x − 24m` with integers `q_x`, where `C_0 = {0,1}³`.

*Proof.* Dispersion-free means `π(Q_x)Ω = q_x Ω`, and `q_x` lies in the integer spectrum of `Q_x`. `LW1_5.md` line 259 (B1-U): "The base `L5-U` tick is covariant under the cell group `𝒢 = 2Z³ ⋊ O_{c_0}`, whose action is transitive on sites", and its lifts "send `𝒢_x^T, N_x, Q_x, p_{ℓ,z}` to their geometric counterparts". So `𝒢`-invariance makes `q_x = q` for all `x`. Sum `ω(Q_x) = ω(N_x) + Σ_{ℓ∋x} ω(p_{ℓ,x})` over `x ∈ C_0`. Fix a direction `i`. The end numbers at `x` of the links `(x, x+e_i)` and `(x−e_i, x)` contribute `ω(p_{(x,x+e_i),x}) + ω(p_{(x−e_i,x),x})`. By cell invariance, `ω(p_{(x−e_i,x),x}) = ω(p_{(x',x'+e_i),x'+e_i})` with `x' ∈ C_0` congruent to `x − e_i` mod `2Z³`, and `x ↦ x'` is a bijection of `C_0`. So the direction-`i` part of the sum is `Σ_{x'∈C_0}(ω(p_{(x',x'+e_i),x'}) + ω(p_{(x',x'+e_i),x'+e_i})) = 8m`, because the two ends of a link hold `m` rishons. Over three directions this is `24m`. So `Σ_{x∈C_0} ω(N_x) = Σ_{x∈C_0} q_x − 24m`; with `q_x = q` and `ω(N_x)` constant by site transitivity, `ω(N_x) = q − 3m`. ∎

This extends `LW1_5.md` F-U from periodic boxes to infinite volume, and from "sharp" as a hypothesis to "sharp" as a consequence of R-SC.

**Corollary Z.3′ (the half-filled site-transitive vacuum has static zero modes).** Let `ω` be a stationary state of a gauge-invariant update of `L5-U[m]` form, with any constants and any plaquette class. Suppose `ω` is `𝒢`-invariant, half filled (`ω(N_x) = 5/2`), and its Gauss-charge correlations `ω((Q_x − ω(Q_x)) τ_β(Q_x − ω(Q_x)))` decay exponentially in `|β|`. Then for every `δ > 0`, `H_phys` contains a nonzero `Ũ`-fixed vector whose cell momentum lies in `{0 < |K| < δ}`. So `ω` violates R-SC, and LZ1's first statement, read by R-SC, fails in `ω`.

*Proof.* By Corollary Z.3, `Q_x` is not dispersion-free in `ω`. Apply Lemma Z.1(b) to `Y = Q_x ∈ 𝔄^G` (Corollary Z.2(a)). ∎

This is a counterexample to LZ1's first statement on `L5-U`, on the stated class of candidate vacua. The excitations it finds are fluctuations of a conserved Gauss charge: neutral, static and of zero energy at every small nonzero momentum. Whether VC1's vacuum lies in this class is VC1's question. PS-7 asks for half filling; PS-1c asks the update, not the vacuum, to be site transitive. So the escape routes are: a vacuum that breaks `𝒢` to a subgroup that is not transitive on sites, with background charges `q_x` summing to `20 + 24m` per cell; a vacuum without exponential clustering of `Q_x`; or a reading of LZ1 other than R-SC.

### 3.3 `L5-O[S_+]`

**Corollary Z.4.** For every gauge-invariant update of `L5-O[S_+]` form, the star Casimir `C_x = Σ_{c<d} (𝒢^{cd}_x)²` lies in `𝔄^G` and is conserved. A vacuum as in Theorem Z is dispersion-free on every `C_x`. No filling constraint follows. `LW1_5.md` line 213 (H): "Every state invariant under all local `Spin(10)` transformations has `ω(n_{x,j}) = 1/2` for each mode", so locally gauge-invariant `L5-O` states are half filled automatically, and Corollary Z.3 has no `L5-O` analogue.

*Proof.* `C_x` is the Casimir of `Spin(10)_x`, invariant under it and under the other sites' groups, which act on other modes. Each gate commutes with every `𝒢^{cd}_x`: the hop contains the contraction `Σ_b η^x_b γ_{x,b}`, which is invariant under the simultaneous rotation of `γ_{x,·}` and `η^x_·` that `𝒢^{cd}_x` generates (`LW1_5.md` Q and G), and `Γ^x` is the product of all ten `x`-end Majoranas, invariant under `SO(10)`. ∎

**Remark Z.5 (outside the physical sector).** The Gauss generators `𝒢^{cd}_x` are conserved and local, but not gauge invariant. On `L5-O[S_+]` no state is dispersion-free on all of them. `LW1_5.md` line 193 (Corollary SC.1): "With one end-pure class on all links, every `z_x` is the scalar `−1`". So the star space has no `Spin(10)_x` singlet, and `C_x ≥ c_* > 0` as an operator, where `c_*` is the least Casimir value on the nontrivial irreducible summands of the finite-dimensional star space. If every `𝒢^{cd}_x` were dispersion-free, then `π(𝒢^{cd}_x)Ω = g^{cd}Ω`; so `π([𝒢^{ab}_x, 𝒢^{cd}_x])Ω = 0`; since `so(10) = [so(10), so(10)]`, every `π(𝒢^{ef}_x)Ω = 0`, and `ω(C_x) = 0`, a contradiction. Lemma Z.1(a), applied to a `𝒢^{cd}_x` of positive variance, then gives, in every clustering cell-invariant stationary state, `Ũ`-fixed vectors at nonzero momentum. When `ω` is locally gauge invariant these vectors lie in the adjoint part of the GNS space, orthogonal to `H_phys`. So on `L5-O[S_+]` the spectral reading can be posed on `H_phys` only. This is the static background charge of `LW1_5.md` LW1-5-BG seen in the GNS space.

---

## 4. What the laws' symmetries can and cannot do (Lemma S.1 to Proposition S.4)

**Lemma S.1 (symmetries preserve speeds).** Let `S` be a symmetry (D5) with matrix `Q`, and `(d, F, V)` a band. If `S` is unitary, put `(Rf)(K) = f(Q^{-1}K)`. Then `(d, S F R^{-1}, V∘Q^{-1})` is a band with image `S(B)`. A node `K_0` goes to `QK_0`, and the leading generator goes to `N'_j = Σ_i Q_{ji} N_i`. If `S` is antiunitary, `(d, S F C R'^{-1}, V')` is a band with image `S(B)`, where `C` is complex conjugation of components, `(R'f)(K) = f(−Q^{-1}K)` and `V'(K) = \overline{V(−Q^{-1}K)}`. In both cases the set of speeds and the Clifford condition, with its `v`, are preserved.

*Proof.* Unitary case. `K·Q^{-1}β = (QK)·β` because `Q` is orthogonal, so `R M_{Q^{-1}β} R^{-1} = M_β` and `R M_V R^{-1} = M_{V∘Q^{-1}}`. Then `T_β S F R^{-1} = S T_{Q^{-1}β} F R^{-1} = S F M_{Q^{-1}β} R^{-1} = (S F R^{-1}) M_β`, and `Ũ S F R^{-1} = S F M_V R^{-1} = (S F R^{-1}) M_{V∘Q^{-1}}`. Differentiating `h(Q^{-1}K)` at `QK_0` gives `N'_j = Σ_i Q_{ji} N_i`. For a unit vector `n`, `Σ_j n_j N'_j = Σ_i (Q^T n)_i N_i`, so the speeds in direction `n` are those of `N` in direction `Q^T n`; `{N'_i, N'_j} = Σ_{kl} Q_{ik}Q_{jl}{N_k, N_l} = 2v²δ_{ij}`. Antiunitary case: the same with `C M_β C = M_{−β}` and complex conjugation of `V`; eigenvalue moduli are unchanged. ∎

**Proposition S.2 (orbits are independent).** Let `𝒩` be a group acting on a finite-dimensional space `E = ⊕_{i=1}^{r} E_i` by unitary and antiunitary operators `ρ(g)`, each preserving every `E_i`, with signed permutation matrices `Q_g`. Call a Hermitian triple `N` on `E` covariant if `ρ(g) N_j ρ(g)^{-1} = Σ_i (Q_g)_{ij} N_i` for unitary `g` and the antiunitary analogue otherwise. If `N = ⊕_i N^{(i)}` is covariant and block diagonal, then `⊕_i λ_i N^{(i)}` is covariant for all real `λ_i`.

*Proof.* The conditions are real-linear in `N` and act block by block, because each `ρ(g)` preserves each `E_i` and the `λ_i` are real. ∎

So the symmetries impose no relation between the speeds of bands that no symmetry exchanges, and they fix no speed: Lemma S.1 moves speeds only by rotating directions. No symmetry can relate a spatial scale to a time scale: every symmetry commutes with `Ũ` (D5), as `LW1.md` B12 forces for an ordered PS-1 update, and acts on momenta by a signed permutation. This is the lattice form of Polchinski's remark (arXiv:1106.6346, page 2) that "a Lorentzian lattice with equal time and space steps has no such enhanced symmetry".

**Example S.3 (two cones under every node symmetry; `L5-U`, `μ = 0 = τ_E`).** Use the node forms of `MT1_REFEREE.md` C4 and its Remark on `H_0 = C^8 ⊗ C^5`: rotations `ρ̂(Q) ⊗ 1`, inversion `ρ̂_I ⊗ 1` (`ρ̂_I = A_1A_2A_3`), the antiunitary `(D_r K) ⊗ K_5`, `σ̂(0) ⊗ 1 = cχ_G ⊗ 1`, and `1 ⊗ U(5)`. Take two copies, `E = H_0 ⊗ C²`, with every symmetry acting as the identity on `C²` (and the antiunitary as complex conjugation there). For every real symmetric `2 × 2` matrix `M`, the triple `N_j = G_j ⊗ 1_5 ⊗ M` satisfies all of these conditions. Its speeds are `|m_1|` and `|m_2|`, the moduli of the eigenvalues of `M` (in the units where `{G_i, G_j} = 2δ_{ij}`). So two light species with the same quantum numbers can carry two cones of any two speeds without breaking any node symmetry.

*Proof.* Each condition holds for `G_j ⊗ 1_5`: by the converse part of Lemma M.0 (section 5.1), transported by `U` as in the proof of Theorem M, and because `G_j ⊗ 1_5` commutes with `1 ⊗ U(5)`. `M` is fixed by the identity and by complex conjugation, since it is real. `N_j² = 1 ⊗ 1 ⊗ M²` and `{N_i, N_j} = 2δ_{ij} 1 ⊗ 1 ⊗ M²` give the speeds. ∎

**Proposition S.4 (no symmetry joins a propagating band to the charged part).** Let `ω` be a D1 state, `S` a symmetry and `B` a band of `ω` that propagates at a node. Then `S(B) ⊄ H_nt`. In particular no symmetry of the vacuum representation maps a propagating bosonic light species into the fermion-odd sector.

*Proof.* By Lemma S.1, `S(B)` is the image of a band with the same nonzero speeds at the image node, where it is `C¹`. If `S(B) ⊂ H_nt`, Lemma P.5 makes it flat there. ∎

**What section 4 decides.** Symmetry cannot supply LZ1-i on either law. The speeds of different orbits are independent (S.2, S.3); no speed is fixed (S.1); and under R-loc, the fermion-boson relation that supersymmetry provides in the continuum (Polchinski, page 3: "Supersymmetry is the one known example [6, 7], in which both the space and time derivative kinetic terms arise from a single superfield") is excluded inside the vacuum representation (S.4). This agrees with #9913 as the assembly quotes it.

---

## 5. MT1-S under a charged-sector prescription, and a new symmetry of `L5-O`

### 5.1 Theorem M: multiplicity one gives one cone

**Lemma M.0 (`MT1_REFEREE.md` C4, rebuilt; credit to the MT1 referee).** Use `MT1.md` lines 19-24 and Theorem 4 (line 60): `A_j` and `Γ_j = iZ_jA_j` (`j = 1, 2, 3`) are Hermitian involutions that anticommute pairwise; their 64 ordered monomials `Γ^S A^R` (`S, R ⊆ {1, 2, 3}`) form a basis of `M_8(C)`; `A_j` and `Z_j` are real in the residue basis; and "`ρ̂(Q)A_jρ̂(Q)*=A_{π(j)}` and `ρ̂(Q)Γ_jρ̂(Q)*=s_jΓ_{π(j)}`", where `Qe_j = s_je_{π(j)}`. Put `χ = −iΓ_1Γ_2Γ_3`, `D_r = Z_1Z_2Z_3` and `ρ̂_I = A_1A_2A_3` (the inversion lift, `MT1.md` line 118). Let `M_1, M_2, M_3` be Hermitian `8 × 8` matrices with
- (R) `ρ̂(Q) M_j ρ̂(Q)^* = Σ_i Q_{ij} M_i` for every `Q ∈ O`;
- (I) `ρ̂_I M_j ρ̂_I^{-1} = −M_j`;
- (Θ) `D_r \overline{M_j} D_r = M_j`;
- (σ′) `M_j χ = χ M_j`.

Then `M_j = aΓ_j` for one real `a`. Conversely `aΓ_j` satisfies all four.

*Proof.* Each condition acts on the basis `Γ^S A^R` coefficient by coefficient. `χ` commutes with each `Γ_k` and anticommutes with each `A_k`: conjugation by `χ` gives the factor `(−1)^{|R|}`. `ρ̂_I` commutes with each `A_k` and anticommutes with each `Γ_k`: factor `(−1)^{|S|}`. `Z_j` anticommutes with `A_j` and commutes with `A_k`, `k ≠ j` (the matching `A_k` does not change `r_j`); so `Z_j` anticommutes with `Γ_j` and commutes with `Γ_k`, `k ≠ j`, and `D_r` anticommutes with every `A_k` and `Γ_k`. `A_k` and `Z_k` are real, so `\overline{Γ_k} = −Γ_k`. Hence `X ↦ D_r \overline{X} D_r` sends `c Γ^S A^R` to `\bar c (−1)^{|R|} Γ^S A^R`. For the face half-turn about `e_1`, `Q = diag(1, −1, −1)`, Theorem 4 gives `Γ_1 ↦ Γ_1`, `Γ_{2,3} ↦ −Γ_{2,3}` and fixes every `A_k`: factor `(−1)^{|S ∩ {2,3}|}`; the half-turns about `e_2`, `e_3` give `(−1)^{|S∩{1,3}|}`, `(−1)^{|S∩{1,2}|}`.

(σ′) keeps only even `|R|`, and (I) only odd `|S|`. (R) for the three half-turns sends `M_1` to `M_1`, `−M_1`, `−M_1`, so `|S ∩ {2,3}|` is even and `|S ∩ {1,3}|`, `|S ∩ {1,2}|` are odd; with `|S|` odd only `S = {1}` remains. Likewise for `M_2` and `M_3`. So `M_1 = Γ_1(a + b_{12}A_1A_2 + b_{13}A_1A_3 + b_{23}A_2A_3)`. For the three-fold turn `C`, `e_1 → e_2 → e_3 → e_1`, (R) gives `M_2 = ρ̂(C)M_1ρ̂(C)^* = Γ_2(a + b_{12}A_2A_3 − b_{13}A_1A_2 + b_{23}A_3A_1)`. For the quarter-turn `C_4`, `e_1 → e_2`, `e_2 → −e_1`, `e_3 → e_3`, (R) gives `M_2 = ρ̂(C_4)M_1ρ̂(C_4)^* = Γ_2(a − b_{12}A_1A_2 + b_{13}A_2A_3 − b_{23}A_3A_1)`. Comparing coefficients: `b_{12} = b_{13} =: b` and `b_{23} = 0`, so `M_1 = Γ_1(a + bA_1(A_2 + A_3))`. `Γ_1` is Hermitian and `Γ_1A_1A_k` (`k ≠ 1`) is anti-Hermitian, since `Γ_1` commutes with `A_1A_k`; so `a` is real and `b` is imaginary. (Θ) maps the coefficient `b` (where `|R| = 2`) to `\bar b`, so `b` is real; hence `b = 0`. So `M_1 = aΓ_1`, and (R) for `C` gives `M_2`, `M_3`. Conversely, `Σ_i Q_{ij}Γ_i = s_jΓ_{π(j)} = ρ̂(Q)Γ_jρ̂(Q)^*`; `ρ̂_I` anticommutes with `Γ_j`; `D_r\overline{Γ_j}D_r = D_r(−Γ_j)D_r = Γ_j`; and `χ` commutes with `Γ_j`. ∎

**Theorem M (`L5-U`, `μ = 0 = τ_E`).** Let `E` be a finite-dimensional Hilbert space with unitaries `r(Q)` (`Q ∈ O`), `r(I)`, `s`, an antiunitary `t`, and a unitary representation `w` of `U(5)`. Suppose a unitary `T : E → H_0 = C^8 ⊗ C^5` carries them, up to phases, to the free node forms of Example S.3: `T r(Q) T^{-1} = λ_Q ρ̂(Q) ⊗ 1`, `T r(I) T^{-1} = λ_I ρ̂_I ⊗ 1`, `T s T^{-1} = λ_s cχ_G ⊗ 1`, `T t T^{-1} = λ_t (D_r K) ⊗ K_5`, `T w(u) T^{-1} = 1 ⊗ u`. Let `N_j` be Hermitian on `E` with `r(Q) N_j r(Q)^{-1} = Σ_i Q_{ij} N_i`, `r(I) N_j r(I)^{-1} = −N_j`, `t N_j t^{-1} = N_j`, `s N_j = N_j s` and `w(u) N_j = N_j w(u)`. Then `T N_j T^{-1} = a G_j ⊗ 1_5` for one real `a`. If `a ≠ 0`, `N` satisfies ER's Clifford condition with `v = |a|`: one isotropic cone.

*Proof.* Phases cancel under conjugation, also for antiunitaries. Put `U = e^{iεR_e/2}` and `M_j = U^* T N_j T^{-1} U`, so that `G_j = UΓ_jU^*`. `U` commutes with every `ρ̂(Q)` and with `ρ̂_I`, which both preserve `R_e = Σ_jA_j/√3`. `U` commutes with `D_rK`, because `R_e` is real and `D_rR_eD_r = −R_e`, so `D_r\overline{U}D_r = U`. And `U^*χ_GU = χ`. Commuting with `1 ⊗ U(5)` makes `M_j = M'_j ⊗ 1_5`, since the commutant of `U(5)` on `C^5` is the scalars; then the antiunitary condition reads `D_r\overline{M'_j}D_r = M'_j`. So `M'_j` satisfies (R), (I), (Θ) and (σ′) of Lemma M.0, which gives `M'_j = aΓ_j` with `a` real, and `T N_j T^{-1} = aG_j ⊗ 1_5`. Finally `{G_i, G_j} = 2δ_{ij}`. ∎

**Sharpness.** Each hypothesis is needed. Multiplicity one: Example S.3. The symmetry `σ`, which needs `μ = 0 = τ_E`: `MT1.md` Theorem 10's `uZ^G_j` term satisfies the other conditions and splits the cone. Inversion and the antiunitary: the two other witnesses of `MT1_REFEREE.md` C4 (cited for sharpness only; nothing below uses them).

**Scope.** By Theorem P, Theorem M never applies to a fermionic band of the own representation of a vacuum that is a D1 state: those bands are flat. It applies to bands of a charged-sector representation chosen by R-CS, if that representation carries the four symmetries in the stated forms, and to the auxiliary free node, where it is C4 itself. So, under R-CS, MT1-S on `L5-U` at `μ = 0 = τ_E` is equivalent to one statement: the light charged band's node fibre carries the free node representation once.

### 5.2 Proposition O: an antiunitary symmetry of the dressed `L5-O[S_+]` tick

**Proposition O.** There is an antilinear `*`-automorphism `Θ_O` of the quasi-local algebra of `L5-O[S_+]` with
\[
\Theta_O(\gamma_{x,a}) = -(-1)^{x_1+x_2+x_3}\,\gamma_{x,a},\qquad \Theta_O(\eta_i\eta_j) = \eta_i\eta_j
\]
for every site, colour and link register. For every `ε`, `μ`, `τ_E`: `Θ_O(h_ℓ) = −h_ℓ` on every link, `Θ_O(Γ^x_ℓ) = −Γ^x_ℓ`, `Θ_O` fixes every cube gate, the electric layer and `U_0`, and `Θ_O∘α = α∘Θ_O`.

*Proof.* (1) *Matter.* The matter algebra is the complexification of the real `C*`-algebra generated by the self-adjoint Majoranas `γ_{x,a}`. Conjugating coefficients with respect to this real form is an antilinear `*`-automorphism that fixes every `γ_{x,a}`. Compose it with the automorphism `γ_{x,a} ↦ −(−1)^{x_1+x_2+x_3} γ_{x,a}`, which preserves the Clifford relations.

(2) *One link.* Realize `Cl(20)` on `(C²)^{⊗10}` by Jordan-Wigner: `γ_{2k−1} = Z^{⊗(k−1)} ⊗ X ⊗ 1`, `γ_{2k} = Z^{⊗(k−1)} ⊗ Y ⊗ 1`, `k = 1, …, 10`. Complex conjugation `K` in the product basis fixes `X` and `Z` and negates `Y`, so `Kγ_{2k−1}K = γ_{2k−1}` and `Kγ_{2k}K = −γ_{2k}`. Put `M = γ_1γ_3⋯γ_{19}`, a real unitary. Each `γ_{2k−1}` anticommutes with the nine other factors of `M` and commutes with itself, so `Mγ_{2k−1}M^{-1} = −γ_{2k−1}`; each `γ_{2k}` anticommutes with all ten, so `Mγ_{2k}M^{-1} = γ_{2k}`. Hence the antiunitary `J = MK` satisfies `Jγ_iJ^{-1} = −γ_i` for every `i`, so `J(γ_iγ_j)J^{-1} = γ_iγ_j`. The chirality `Γ = −γ_1⋯γ_{20}` (`LW1_5.md` line 199: "Their product is `η_1⋯η_20 = −Γ`") has a real coefficient and twenty factors, so `JΓJ^{-1} = Γ` and `J` preserves `S_+`. Also `J² = M\overline{M} = M² = (−1)^{45} = −1`. So `A ↦ JAJ^{-1}` is an antilinear `*`-automorphism of `End(S_+)` fixing every `η_iη_j`. [check: `/tmp/toe-lz1/scripts/check_J.py` builds this `J` on the 1024-dimensional module and confirms `Jγ_iJ^{-1} = −γ_i`, `[J, Γ] = 0`, `J² = −1`, `J(γ_iγ_j)J^{-1} = γ_iγ_j` for all 190 pairs, and `JΓ^xJ^{-1} = −Γ^x`; 38 s, 634 MB.]

(3) *Whole algebra.* On each finite region the algebra is the tensor product of the matter part and the link registers (links commute with matter). A pair of antilinear maps defines an antilinear map of the algebraic tensor product, `a ⊗ b ↦ θ_m(a) ⊗ θ_ℓ(b)`, because `(a, b) ↦ θ_m(a) ⊗ θ_ℓ(b)` is antilinear in each slot. It is a `*`-automorphism on each finite region, isometric there, and compatible with inclusions, so it extends to the quasi-local algebra.

(4) *The tick.* `U^{ab} = iη^y_aη^x_b` goes to `−iη^y_aη^x_b = −U^{ab}`. With `s(x) = −(−1)^{x_1+x_2+x_3}`, `h_ℓ = (i/2)Σ_{ab} γ_{y,a}U^{ab}γ_{x,b}` goes to `(−i/2)Σ_{ab} s(y)γ_{y,a}(−U^{ab})s(x)γ_{x,b} = s(x)s(y) h_ℓ = −h_ℓ`, since neighbours have opposite parity. `H_C` has real coefficients, so `Θ_O(H_C) = −H_C`, and `Θ_O(e^{−iaH_C}) = Σ_n (ia)^n(−H_C)^n/n! = e^{−iaH_C}` for real `a`. `Γ^x = i^5 η^x_1⋯η^x_{10}` is `i^5` times a product of five fixed pairs, so `Θ_O(Γ^x) = (−i)^5 η^x_1⋯η^x_{10} = −Γ^x`, and `Θ_O(e^{−iτ_EΓ^x}) = e^{iτ_E(−Γ^x)} = e^{−iτ_EΓ^x}`. So `Θ_O(U_0) = U_0`, and `Θ_O(α(A)) = Θ_O(U_0)^*Θ_O(A)Θ_O(U_0) = α(Θ_O(A))`. ∎

**Remark O.1.** `MT1_REFEREE.md` line 297 lists, for `L5-O`, the failing step "no antiunitary symmetry of the dressed tick is known (C6 does not apply)". Proposition O removes it, for every value of `τ_E`. It does not by itself give condition (Θ) of Lemma M.0 at the free `O` node. Composed with the centre transformation `∏_{x even} c_x`, `Θ_O` fixes every matter Majorana, so on the number-conserving free `O` walk it acts as the antilinear map `c_{x,j} ↦ c_{x,j}^†`, a particle-hole conjugation, not as a one-body antiunitary of the particle band. Whether some product of `Θ_O` with exact symmetries acts on a charged `L5-O` band as condition (Θ) depends on R-CS and on the lift ambiguity of `MT1_REFEREE.md` C7; this file does not settle it.

---

## 6. Four-test checks

A reading, specification or definition fails if it (1) states or fixes a part's target, (2) is open-ended so that a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants that its own reasons do not need. Nothing below is adopted.

### 6.1 The definitions and readings this file uses

| Item | (1) | (2) | (3) | (4) | Note |
|---|---|---|---|---|---|
| D2-D4 (band, node, leading generator, light species) | pass | pass | conditional | pass | "One cone" is tested, not asserted. Finite fibres and `C¹` at the node exclude infraparticle-type spectra: a massless charged particle in a Coulomb phase has no band. So D2-D4 cannot see such a species, and that is where R-CS is needed. |
| D5 (symmetry) | pass | pass | pass | pass | Commuting with `Ũ` is what `LW1.md` B12 forces for an ordered update. |
| R-loc (the vacuum's own representation) | pass | pass | pass | pass | The plain reading of "in the VC1 vacuum". Theorem P decides MT1-S under it as a consequence, not by premise. |
| R-CS (charged-sector prescription) | n/a | n/a | n/a | n/a | Named only. Theorem P constrains any proposal: it cannot be the vacuum representation itself. The owner question is shared with CH1. |
| R-SC, R-SC\* (spectral readings of LZ1) | conditional | pass | pass | pass | Each is a consequence of LZ1's first statement under the reading "every low-energy excitation of the vacuum lies in some light species". Used only as a hypothesis of necessary conditions (Theorem Z), never to prove LZ1. |

The clustering hypotheses of Theorem Z and Corollary Z.3′ are stated in each statement; they are hypotheses of theorems, not proposed premises.

### 6.2 Candidate conditions that would close LZ1-i

The lane brief asks for the condition that would close LZ1's common speed. Four candidates were written down and tested. Section 4 rules out a closure by the laws' symmetries.

**LZ1-C1 (equal-speed tuning).** "The law's free constants are chosen so that every light species of the vacuum has the same speed."
- (1) fail: it fixes LZ1's target. (2) pass. (3) fail: it settles LZ1(a)'s common speed by premise. (4) pass: it removes freedom; it adds none.
- This is the condition that would close the common-speed clause. The literature found does the same: anisotropic lattice QCD renormalizes "the parameters in the anisotropic gauge and quark actions" separately (Morrin et al., arXiv:hep-lat/0604021), and Collins et al. (arXiv:gr-qc/0403053) and Iengo, Russo and Serone (arXiv:0906.3477) find fine tuning necessary. Adopted, it would make the common speed an input of the law choice, not a derived result.

**LZ1-C2 (a protecting fermionic symmetry).** "The update has a symmetry mapping each light fermion species onto a light boson species."
- (1) pass: it states a symmetry. (2) pass once the symmetry is written. (3) fail: it predicts a boson partner with equal quantum numbers for each light fermion, which settles T5's content by premise. (4) fail: it adds a whole symmetry structure.
- Under R-loc, Proposition S.4 excludes it outright. Polchinski (arXiv:1106.6346, page 3) names supersymmetry as the one known example of this kind and notes that its breaking reintroduces the problem.

**LZ1-C3 (single source).** "Every light species of the vacuum other than the fermion multiplet is a threshold composite of it."
- (1) pass: it states a structure, not the speed. (2) conditional: "threshold composite" needs a definition of continuum edges in an interacting Floquet law. (3) fail: it settles GA1's and GA2's question whether gauge bosons are link modes or composites, and GR2's for the graviton. (4) pass.
- Bisio, D'Ariano and Perinotti (arXiv:1407.6928, eq. (43), `ω(k) = 2|n_{k/2}|`) show the mechanism in a free model: a photon built from two Weyl fermions inherits their leading speed. Under R-loc the source multiplet is flat (Theorem P), so C3 must be posed under R-CS.

**LZ1-C4 (infrared attractor).** "Under ZM1's zoom, every dimension-four speed difference among light species is irrelevant at the infrared fixed point."
- (1) fail: it restates the common speed in renormalization-group language. (2) pass. (3) fail. (4) pass.
- Even granted, it does not give LZ1(a) as worded. At weak coupling the speeds approach each other only logarithmically (Anber and Donoghue, arXiv:1102.0789, eqs. (51)-(54)), which contradicts `E = c|k|(1 + O((a|k|)^p))` with `p ≥ 2`. A power-law approach is found only in strongly coupled examples (Bednik, Pujolàs and Sibiryakov, arXiv:1305.0011). These are literature statements, not proved here.

**Verdict.** No candidate passes all four tests. LZ1-C1 closes the common-speed clause and fails tests 1 and 3. The owner may still choose it; the common speed would then be a law choice.

---

## 7. What stays open, and the attacks that failed

**Lemma 7.1 (the bare gauge sector of `L5-U` does not propagate).** For the base tick of `L5-U[m]` (and of `L_cube`), the subspace with no matter fermions is invariant, and the tick acts on it as `W_E`, a product of single-link unitaries diagonal in the end numbers (in the electric values, for `L_cube`).

*Proof.* Each term of `h_ℓ` ends, on the right, with a matter annihilator: `c^†_{y,j}U^{jk}c_{x,k}` and its adjoint `c^†_{x,k}U^{jk†}c_{y,j}`. So `h_ℓ` kills every vector with no matter, every cube gate `e^{−iaH_C}` acts on such vectors as the identity, and `U_0 = W_E M_o M_e` acts as `W_E`. ∎

So on the base `L5-U` and `L_cube` ticks the link registers change only when matter hops. A light gauge boson, if the vacuum has one, is a collective mode of a vacuum with matter; it has no free-level counterpart. The Majorana hop of `L5-O` creates pairs from the empty matter state, so Lemma 7.1 has no `L5-O` analogue.

### 7.1 LZ1-i, open after three named attacks

**LZ1-i (as reduced here).** In the VC1 vacuum of either law, all propagating light species share one speed. By Theorem P they are all bosonic under R-loc; charged fermions enter only under R-CS.

- **Attack A1 (symmetry)** fails at Proposition S.2: the symmetries impose no relation between different orbits and fix no speed. Example S.3 gives explicit two-cone witnesses that respect every node symmetry of `L5-U` at `μ = 0 = τ_E`. Proposition S.4 closes the fermion-boson version inside the vacuum representation.
- **Attack A2 (continuity from the free node)** fails at Theorem P. The auxiliary free walk's light species form the fermionic node multiplet, with one cone of speed `v = sin ε/√3` in cell units per tick (`MT1.md` Theorem 7, `MT1_REFEREE.md` C4). In the representation of every D1 state of the interacting law, fermionic bands are flat, so no free light species continues as a propagating one. Bosonic light species have no free-level counterpart (Lemma 7.1).
- **Attack A3 (renormalization-group attractor)** fails at "a controlled flow exists": ZM1-i is open. Granted a flow, it fails at "the approach is a power law" for weakly coupled infrared sectors (section 6.2, LZ1-C4; literature, not proved here).

**Kill attempt K (two propagating light species with different speeds, exactly).** It failed at "an exactly solvable sector with a propagating light band exists". Tried: (K1) frozen stars are static (Corollary Z.2(b)); (K2) one-particle sectors over the empty-matter state, with blocking link configurations, keep their Gauss pattern pinned (Theorem P), and the moving matter drags a flux string, so the configurations form a graph of strings, not a lattice; (K3) sectors in which some flavours are locked at every star reduce to a smaller quantum link model of the same form, still interacting. Exactly free sectors appear only after the c-number replacement of links, which is not the interacting law (`LW1_5.md` inferred definition 4). This is a failed search, not a no-go. The counterexample to LZ1's first statement that does exist is Corollary Z.3′: static neutral zero modes in every half-filled, site-transitive, exponentially clustering `L5-U` state.

### 7.2 MT1-S

Under R-loc, MT1-S is false (Corollary P.6). Under R-CS, on `L5-U` at `μ = 0 = τ_E`, it is equivalent to the multiplicity-one statement of Theorem M, which is open. On `L5-O`, two steps remain beyond R-CS: the lift ambiguity of `MT1_REFEREE.md` C7, and whether some symmetry acts on a charged band as condition (Θ) of Lemma M.0 (Remark O.1).

---

## FINISH

**Proved** (written out in full above; pass 1, not distilled or refereed).
- Facts F1-F4: the action of the local centre elements on generators, their commutation with every gauge-invariant gate, and fermion parity as a product of centre elements, for `L5-U`, `L5-O[S_+]` and `L_cube` (rebuilt from `MT1.md` Theorem 6 and `CH1_5UQ.md` RC7).
- Theorem P (with Lemmas P.1-P.3, Proposition P.4, Lemma P.5): for any gauge-invariant update of either law, any constants and any plaquette class, and any stationary, cell-invariant, centre-invariant state, the charged part of the GNS space is `L²(T³; 𝒦)` with a momentum-independent tick; every band there, and so every fermionic light species, is flat at its nodes.
- Corollaries P.6 and P.7: MT1-S and the fermion clause of LZ1's first statement fail in the vacuum's own representation.
- Lemma Z.1 and Theorem Z: under R-SC (or R-SC\*) and a clustering hypothesis, the vacuum is dispersion-free on every conserved local gauge-invariant operator.
- Corollary Z.2: on `L5-U`, `Q_x` is conserved and gauge invariant for every gauge-invariant update; the frozen projector `P_x` is conserved, gauge invariant, and neither `0` nor `1` for the base tick (rebuilt from `CH1_5UQ.md` Theorem 3.1).
- Corollary Z.3: a Gauss-sharp, site-transitive `L5-U` state has integer filling `q − 3m` (`LW1_5.md` F-U at infinite volume).
- Corollary Z.3′: every half-filled, site-transitive, stationary `L5-U` state with exponentially decaying Gauss-charge correlations has neutral zero-energy states at arbitrarily small nonzero momentum.
- Corollary Z.4 and Remark Z.5: on `L5-O[S_+]` the star Casimirs must be sharp under R-SC; no state is dispersion-free on all local Gauss generators, so R-SC can be posed on the physical sector only.
- Lemma S.1, Proposition S.2, Example S.3, Proposition S.4: symmetries preserve speeds, impose no relation between orbits, admit two cones of any two speeds on two copies of the free node representation, and cannot map a propagating band into the charged part.
- Theorem M: on `L5-U` at `μ = 0 = τ_E`, a band whose node fibre carries the free node representation once, with its four symmetries and `U(5)`, has one isotropic cone; each hypothesis is needed.
- Proposition O: an antilinear automorphism `Θ_O` fixes the dressed `L5-O[S_+]` tick for every `ε`, `μ`, `τ_E` ([check] on the link part).
- Lemma 7.1: the empty-matter sector of the base `L5-U` and `L_cube` ticks evolves by `W_E` alone.

**Counterexamples.**
- To MT1-S read in the vacuum's own representation (R-loc): every VC1 vacuum of either law that is a D1 state (Corollary P.6).
- To LZ1's first statement read by R-SC, on `L5-U`: every half-filled, site-transitive, stationary state with exponentially decaying Gauss-charge correlations, for all constants and every plaquette class (Corollary Z.3′).
- To "the laws' symmetries force one cone across species": two copies of the free node representation with `N_j = G_j ⊗ 1_5 ⊗ M` (Example S.3).
- To "a symmetry of the vacuum representation can relate a propagating boson band to a fermion band": Proposition S.4.

**Open by name.**
- **LZ1-i** (all propagating light species of the VC1 vacuum share one speed). Three attacks failed: A1 symmetry at Proposition S.2; A2 continuity from the free node at Theorem P; A3 renormalization-group attractor at "a controlled flow exists" (ZM1-i). The kill attempt K failed at "an exactly solvable sector with a propagating light band exists".
- **MT1-S[R-CS]**: on `L5-U` at `μ = 0 = τ_E`, equivalent to the multiplicity-one hypothesis of Theorem M. On `L5-O`, also the lift ambiguity of C7 and the node form of `Θ_O` (Remark O.1).
- **R-CS**, the charged-sector prescription: an owner question, shared with CH1's charged-correlator prescription.
- No candidate closing condition passes the four tests (section 6.2). LZ1-C1 (equal-speed tuning) would close the common-speed clause and fails tests 1 and 3.

**What changes downstream.**
- MT1: MT1-S is false under its plain reading R-loc; it needs restating under R-CS. MT1(a)(2) read with ER is false for local excitations. On `L5-O`, attack A1 loses the step "no antiunitary symmetry of the dressed tick is known" (Proposition O).
- LZ1 (`TOE_ASSEMBLY.md` lines 318-332): the fermion clause of LZ1(a) needs R-CS. LZ1-i cannot come from the laws' symmetries. With `p ≥ 2`, LZ1(a) is not delivered by a weakly coupled attractor (literature). Under R-SC, LZ1 requires the VC1 vacuum to be sharp on every conserved local gauge-invariant operator.
- VC1 and PS-7 on `L5-U`: a half-filled, site-transitive, exponentially clustering vacuum violates R-SC. So the `L5-U` vacuum must break site transitivity (with background charges summing to `20 + 24m` per cell), or lose exponential clustering of the Gauss charges, or LZ1 must be read otherwise. This sharpens LW1-5U-PS7. `L5-O` has no such tension: its locally gauge-invariant states are half filled (`LW1_5.md` H).
- CH1: its charged-correlator prescription is now needed by MT1-S and by LZ1 as well.
- GA1-P-5: the frozen stars belong to the base tick; a plaquette class may lift them. If it does not, R-SC requires `ω(P_x) ∈ {0, 1}`.
- No working-set entry, axiom, law or reading changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
