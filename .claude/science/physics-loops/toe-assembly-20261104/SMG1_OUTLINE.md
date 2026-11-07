lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SMG1: wall W2 (chirality and the 16 by symmetric mass generation), assembly outline and rung 1, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini (`claude-opus-5-5`, max), as pass 1 of wall W2 under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** The assembly outline of wall W2 (`TOE_ASSEMBLY.md` section 11, line 718), in the form the YM branch uses for T0, and an attack on its first rung. It grants no status. It adopts no law, reading or definition. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation; a check guides and never proves.

**Source revisions read.**

| Ref | Commit | Read with |
|---|---|---|
| `claude/toe-assembly` (this checkout) | `1e078a90f` | working tree |
| `origin/claude/ym4d-hard-route` | `b9b7e0318` | `git show` |
| `origin/docs/consolidate-chirality-doublers` (PR #10131) | `a1bced899` | `git show` |
| `origin/claude/toe-cayley-mirror-gap-20261021` (#10078) | `d2b189516` | `git show` |
| `origin/main` | `f5af11cd0` | `git show` |

**Files read, by line.** This folder: `prior/SMG1.md` (all); `TOE_ASSEMBLY.md` lines 1-23, 71-94, 169-256 (sections 3.2-3.9), 388-476 (MT1, GA1, CH1, CG1), 586-610 (section 6), 708-726 (sections 10-11); `LW1_5.md` lines 1-120 (status, Amendments 1-3, definitions, both laws, C, C1, C2); `CH1.md` lines 1-130 (status, Amendments 1-6, inferred definitions, F1-F3, S1, C2, C3, CH1-C1, AM, S1-5, C2-5, Lemma V); `LIT_SMG.md` (all); `CG16S.md` lines 1-16, 116-140 (status, RC-W); `RCSP16.md` lines 7, 11, 86; `CH1_5U.md` lines 7, 9, 143-145, 155, 157; `CH1_5UQ.md` line 126; `GA2_Y2.md` lines 14, 24, 37-43; `RCS1.md` line 66; `LZ1.md` lines 50, 62; `MT1.md` line 29; `FL1.md` line 29; `VC1_5.md` lines 1-30 and the readings E, P, F (line 198 on); `Y2W_DRAFT.md` lines 1-40 (format only). YM branch: `.claude/science/physics-loops/ym4d-hard-route-20261030/library/ym4-assembly.md` lines 1-200 and `library/t0-tree.md` lines 1-30, as the model of an outline. PR #10131: `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` (below `C`) lines 11, 17, 19, 21, 519, 721, 1491, 1690, 2209-2211, 2221, 2231, 2237, 2249-2250, 2255, 2315-2319, 2334, 2341. #10078: its note `docs/THE_CAYLEY_COMPLETION_OF_THE_CHARGE_FOUR_TERM_HALVES_THE_GAPPING_COUPLING_OF_THE_EIGHT_MAJORANA_PROXY_CHAIN_BUT_BOTH_FORMS_PERSIST_AT_STRONG_COUPLING_BOUNDED_THEOREM_NOTE_2026-10-24.md` (all). Main: `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` (below `S`) lines 7, 14-16, 28, 97, 201, 235, 239; `docs/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md` lines 6, 10.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The working set is read plainly. Where a statement needs a meaning the texts do not fix, section 7 writes a candidate reading and four-tests it. Nothing is adopted.

**Working set used, by name.** PS-5 (five modes per site, `TOE_ASSEMBLY.md` line 205); PS-6 with PS-6r (finite link registers, line 183); PS-1 with PS-1c (cell covariance, line 180); GA1-P-NN, that is NN-a (line 235). PS-7r (line 184) is quoted once, for its small-step sentence. No other entry is used. The owner candidates R-CS^str (line 225) and ZM1-INV (line 252) are named in the target theorem as interfaces, not used as premises.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: finite abelian groups and their characters, traces of Clifford monomials, the complex Clifford algebra `Cl_8 ≅ M_16(C)`, linear codes over `F_2`. Literature: section 2, each item fetched on 2026-11-07, with its role. No citation is load-bearing for a proof step of rung 1.

**[check] runs.** Scripts `check_fk.py` and `check_chain.py` in `/tmp/toe-SMG1/scripts/`, outputs `out_fk.txt` and `out_chain.txt` in `/tmp/toe-SMG1/`; numpy 2.4.1, Python 3.12.8; each under 2 s and a few MB. They confirm, in floating point, the on-site spectrum of section 6.2, the identity of the printed Fidkowski-Kitaev term with Definition 6.1, and the two-site gap at a few hoppings. A third run was stopped after 120 s (a dense 4096-dimensional build); its results are not used. The second run of `check_chain.py` started when `memory_pressure` showed 44 percent free, below the 50 percent rule; it ran under a second. This is recorded here and not repeated.

## 0. Outcome in one paragraph

**Rung 1 is proved, in a stated reading; the outline is written.** The target theorem W2 is stated in standard mathematics (section 3): a cell-covariant NN-a tick on PS-5 sites with finite registers and an exact on-site group `G ⊋ G_SM`, a pure `G`-invariant ground state, and a scaling limit equal to one free left-handed Weyl 16 with no other field. The ladder (section 4) has atoms R0, eight Majorana chains R1, a new decoupling rung R1.5, a chiral 1+1D rung R2, two dimensions R3 and the 16 at R4. Of seven tricks (section 5), decoupling (a gapped mirror beside a gapless light sector, with no light partners) is the hardest; every prior repository attempt on file stops at it, and its simplest instance is R1.5. **Rung 1** (section 6), on five-mode sites with local fermion parity gauged: the Hamming stabilizer group `S ≅ Z₂⁴` forbids every quadratic mass, since each symmetric quadratic form has eigenspaces of dimension divisible by 16 on every ring (Theorem 6.4); Fidkowski-Kitaev's interaction, rebuilt as minus the sum of the fourteen weight-4 stabilizers, has spectrum −14 (1), 0 (8), +2 (7) with a unique `S`-fixed ground vector (Theorem 6.3, no computer); the zero-hop tick is NN-a, gauge invariant and symmetric, and its generator has a unique ground state, pure on the invariant algebra, with an explicit gap, in finite and infinite volume (Theorem 6.5); eight is least for sign-flip symmetries (Lemma 6.6). The tick itself has no spectral gap at its vacuum for any step (Proposition 6.7), so "gap" is read through the tick's generator (reading R-GEN; four-test verdict C, P, C, P in section 7; not adopted). With the chain hop, the gap persists on open segments by Fröhlich-Pizzo's Theorem 3.5, cited and not rebuilt [SP]. Open by name: R1-H, FLQ, R0-U5, R1.5-D, R2, R3-H, R3-D, W2.

## 1. Prior work used

The digest `prior/SMG1.md` was read first, in full. Every file it names that bears on W2 was read at the lines listed in the head. Paths: `T/` is this folder; `C` is the PR #10131 consolidation; `S` is the main SPIN10 note. Status words are the sources' own.

**Used or extended.**

| Prior result | Path | Use here |
|---|---|---|
| #10078: the Cayley 4-form on 8 Majoranas has spectrum −14 (1), 0 (8, odd), +2 (7, even), stabiliser `Spin(7)`; its supplied 1+1D proxy chain (4 complex modes per site, `SO(8)`-invariant hop) is gapped and flat in `L = 4..8` at `g ≥ 0.25` | `origin/claude/toe-cayley-mirror-gap-20261021:docs/THE_CAYLEY_COMPLETION_..._2026-10-24.md`, section A and table C; `C:2341` (logged) | Rung 1's on-site spectrum is re-proved natively in section 6.2 by a different route (the extended Hamming code), with credit. The proxy chain is rung 1's hopping chain; its numerics are a guide only. |
| Free updates are vector-like: F1-F3, F3a (net chirality at quasi-energy 0 equals that at π) | `T/CH1.md` lines 50-62 (frozen) | Target clause (W2.6) and the ladder's chirality step (section 5, trick D). |
| RC-W: a cell-covariant product of block layers has `W₃ = 0`; under NN-a and condition E a free 16 pairs with its mirror | `T/CG16S.md` lines 120, 140 (frozen, checked once) | Same use as F3. The digest cites line 140 only; RC-W itself is at line 120. |
| S1 and C2-5: odd local fields have odd charge on one-mode sites; triple products cannot be ten CAR modes | `T/CH1.md` lines 88, 126 (frozen) | Carrier constraints for rungs 2 and 4. |
| CH1-C1 (open): the 1D one-mode, finite-link `(1,7)`/`(5,5)` construction | `T/CH1.md` line 114 (frozen) | One admissible target content for rung 2. |
| The twisted family `R_u` is the 16 pulled back along a cover of `U(5)`; its mirror is anomaly-free (bordism cited); the mirror quartics are fixed by the gauged centre | `T/CH1_5U.md` lines 7, 9, 143-145 (frozen) | Rung 0 and rung 4 for `L5-U`. Its failed attacks 4 and 5 (lines 155, 157) are not repeated. |
| Four routes around the 16; Theorem SC; the live laws give no moving chiral 16 directly | `T/LW1_5.md` line 11, Amendment 3 (frozen) | Rung 4's carrier step. |
| No irreducible 16 and no Clifford cone from the straight-string witness | `T/RCSP16.md` lines 7, 11, 86 (frozen) | Same. |
| Every gauge-invariant element is matter-even | `T/RCS1.md` line 66, Theorem 4 (frozen) | Target clause (W2.4): on a gauged law the light fermions are charged sectors. |
| No finite register carries an invertible link covariant under a group with infinite image; finite images are allowed | `T/GA2_Y2.md` lines 37-43, Theorem 2.1 (N), Corollary 2.2 (frozen) | Rung 1 gauges a finite group, so its links are exact unitaries; rungs 2-4 inherit N. |
| Gauge averaging; purity on `𝔄^gauge` equals extremality among gauge-invariant states; readings E, P, F of a vacuum | `T/VC1_5.md` line 50 and lines 198-204 (frozen) | Theorem 6.5(3): the rung-1 state is pure on the invariant algebra. |
| Odd bands of D1 states are flat at nodes on both live laws | `T/LZ1.md` lines 50, 62, Theorems 2.1-2.2 (frozen) | Rung 4's carrier step. |
| Spin(10) atoms: a unique Spin(10)-singlet ground state with an exact atomic gap; the pair square on 32 modes, gap `19.0715 g` | `S:28`, `S:97` ("conditional-support", unaudited); `C:2316` (#9910, logged) | Rung 0 for the 16. Not re-proved here. |
| Strong-coupling atomic control keeps volume dependence | `S:235`, `S:239` | The reason rung 1's hopping step needs a volume-uniform stability theorem (section 5, trick B). |
| The 3450 cells: two-site cell 8-fold degenerate; three-site complete-graph cell unique with `Δ₀ = 0.134 g`; the neutral lattice `l₁, l₂` is K-null | `C:1491`, `C:1690`, `C:2334` (logged) | Rung 2's atom. |
| On one-mode chains with the staggered hop, the 3450 combination has non-integer spectra, so no circuit makes it an exact `U(1)` | `C:2318` (#9927, logged) | Rung 2's carrier constraint. The digest lists #9927 for rotors only. |
| The endpoint pairing normalisation `Q_QMC = Q_SIGN1/16`, and its stated non-conclusions | main, `docs/CHIRALITY_LOCAL_ENDPOINT_ALGEBRA_NOTE_2026-10-18.md` lines 6, 10 | Recorded for rung 4; not used. |
| The literature map: FK rebuild items (Clifford identities, excited energy, antiunitary action) and "A weak-hopping stability theorem" left to prove | `T/LIT_SMG.md` lines 200-202 | Section 6.2 rebuilds the first two by a different route; section 6.6 ports the stability theorem. |

**Failed attempts on file that bear on the ladder** (not repeated here): the tetrahedral FK term gaps both light copies (`C:2315`); a symmetric block mirror gap releases the light partners (`C:519`); a gapped far layer moves the mirror one layer in (`C:1491`, `S:201`); 3450 persistence beyond `L = 12` is not established (`C:2255`); π flow is forced and the far wall is chosen boundary data (`C:19`, `C:2237`); a Spin(10) flow does not import into `L5-U` (`T/CH1_5U.md` line 155); the overlap pullback gives a zero link matrix (`T/CH1_5U.md` line 157). Rung 1 below uses none of these routes.

**Missed by the digest, added here.** RC-W at `T/CG16S.md` line 120; Theorem N at `T/GA2_Y2.md` line 37; Theorem 4 at `T/RCS1.md` line 66; the VC1 purity equivalence at `T/VC1_5.md` line 50; the #9927 spectral obstruction at `C:2318`. The 2026 literature on exactly solvable 1+1D chiral lattice theories (section 2, items L13-L16) is not in the repository.

## 2. Literature read

All items were fetched on 2026-11-07 (arXiv abstract pages; INSPIRE records for papers not on arXiv). "Text" means the relevant text was fetched and the anchors were read in it. "Abstract" means only the abstract page was read; such an item is NOT VERIFIED beyond its abstract and is used as context only. No item is load-bearing for a proof step of rung 1. Rung 1's proofs (section 6) are written out here; the one imported step, 6.6, is marked `[SP]`.

| # | Work | Reference | Read | Anchor used | Role |
|---|---|---|---|---|---|
| L1 | Fidkowski, Kitaev, "The effects of interactions on the topological classification of free fermion systems" | arXiv:0904.2197v3; Phys. Rev. B 81, 134509 (2010) | text | Sec. II.1: Eq. (8) (the 14-term quartic `W`), Eqs. (9)-(10) (`c_{2j-1}=a_j+a_j^†`, `c_{2j}=-i(a_j-a_j^†)`), Eq. (11) (`W₁`, four terms); the sentence "Uniqueness follows from the fact that it is already a unique ground state of W₁". Sec. II.2: Eqs. (12)-(15), (19) (the path; partly numerical, Figs. 1-2) | Rung 0/1. Eq. (8) is re-proved natively in 6.2. The path of II.2 is not used. |
| L2 | Fidkowski, Kitaev, "Topological phases of fermions in one dimension" | arXiv:1008.4138v2; DOI 10.1103/PhysRevB.83.075103 | abstract | "the eight equivalence classes are distinct and exhaustive"; MPS methods | Context for the `Z₈`. |
| L3 | Seiberg, Shao, "Majorana chain and Ising model - (non-invertible) translations, anomalies, and emanant symmetries" | arXiv:2307.02534v3; SciPost Phys. 16, 064 (2024) | text (first 100k characters) | Eqs. (1.5), (3.5): `T: χ_ℓ ↦ χ_{ℓ+1}`; Eq. (3.20): `𝖦T = -T𝖦` for `L = 2N`; Eq. (1.17): lattice translation ≈ `(-1)^{F_L} e^{2πiP/L}` on low-lying states; "a lattice precursor of its mod 8 't Hooft anomaly" | Why one-site translation forbids the chain mass; context for "eight". |
| L4 | Hsieh, Halász, Grover, "All Majorana models with translation symmetry are supersymmetric" | arXiv:1604.08591v2; Phys. Rev. Lett. 117, 166802 (2016) | abstract | odd number of Majoranas per cell: "all states are at least doubly degenerate"; with antiperiodic boundary no unique gapped ground state in 1D | Rung 1.5 (light-sector protection). Interacting scope NOT VERIFIED. |
| L5 | Fröhlich, Pizzo, "Lie-Schwinger block-diagonalization and gapped quantum chains" | arXiv:1812.02457; Commun. Math. Phys. 375, 2039-2069 (2020) | text (first 100k characters) | Theorem 3.5 (stated in Sec. 1.2): on-site `H ≥ 0`, unique zero vector `Ω`, `H ≥ 1` on `Ω^⊥` ((1.2), (1.4)); `K_N(t)=Σ_iH_i + tΣ_{k≤k̄}Σ_iV_{I_{k;i}}`, open chain, `‖V_I‖ ≤ 1` ((1.5)-(1.7)); for `|t| < t₀`, unique ground state and gap `≥ 1/2` uniformly in `N`. The Kitaev-chain section 4 was not read. | Rung 1, step 6.6: `[SP]`. |
| L6 | Del Vecchio, Fröhlich, Pizzo, Rossi, "Local iterative block-diagonalization of gapped Hamiltonians: a new tool in singular perturbation theory" | arXiv:2007.07667v2; J. Math. Phys. 63, 073503 (2022) | abstract | "extended to higher-dimensional quantum lattice systems"; gap persists for small `|t|` | Rungs 3-4, stability assignment. |
| L7 | Yarotsky, "Ground states in relatively bounded quantum perturbations of classical lattice systems" | arXiv:math-ph/0412040; Commun. Math. Phys. 261, 799-819 (2006) | abstract | exponential decay of truncated correlations; analyticity of the ground state | Alternative to L5 in infinite volume. |
| L8 | Michalakis, Pytel, "Stability of frustration-free Hamiltonians" | arXiv:1109.1588v3; Commun. Math. Phys. 322, 277-302 (2013) | abstract | gap stable under quasi-local perturbations given local topological quantum order | Alternative stability route. |
| L9 | Bourne, Ogata, "The classification of symmetry protected topological phases of one-dimensional fermion systems" | arXiv:2006.15232v2; Forum Math. Sigma (DOI 10.1017/fms.2021.19) | abstract | an index for SPT phases of infinite fermionic chains | Context: a rigorous index framework for rung 1's phase. |
| L10 | BenTov, "Fermion masses without symmetry breaking in two spacetime dimensions" | arXiv:1412.0154v3; JHEP 1507 (2015) 034 | abstract | the SO(7) Kitaev-Fidkowski model; "the fermion propagator vanishes when p = 0" | Context for the propagator-zero question (L24). |
| L11 | Wang, You, "Symmetric Mass Generation" | arXiv:2204.14271; Symmetry 14, 1475 (2022) | abstract | review | Context. |
| L12 | Wang, Wen, "Non-Perturbative Regularization of 1+1D Anomaly-Free Chiral Fermions and Bosons" | arXiv:1307.7480v6; Phys. Rev. B 107, 014311 (2023) | abstract | "a topological non-perturbative proof of the equivalence between" anomaly cancellation and symmetric gapping rules (continuum); the 3-4-5-0 lattice proposal | Rung 2 target content and guide. |
| L13 | Thorngren, Preskill, Fidkowski, "Chiral Lattice Gauge Theories from Symmetry Disentanglers" | arXiv:2601.04304v2 | text (first 100k characters) | Sec. 1: a disentangler is "a constant-depth circuit of local unitaries that transforms the not-on-site symmetry action into an on-site one"; Eq. (19): needs `Σ q_V q_A = 0`; Sec. 3: rotors, "infinite-dimensional rotor degrees of freedom"; Sec. 2.4: the 3450 model is Gaussian and gapless (c = 2); Sec. 5: finite-dimensional commuting-projector SPTs are "sharply constrained" | Rung 2 guide. Its rotors are not finite registers (PS-6r). |
| L14 | Seifnashri, "Exactly Solvable 1+1d Chiral Lattice Gauge Theories" | arXiv:2601.14359v2 | abstract | modified Villain; an explicit quadratic Hamiltonian for the "34-50" theory | Rung 2 guide. Local dimension NOT VERIFIED. |
| L15 | Lu, Shao, "Fermionic Villain model with exact lattice chiral symmetries" | arXiv:2608.02728 | abstract | Villain bosons coupled to a Kitaev chain; SMG of 3450 "analytically demonstrated" via fermionic T-duality | Rung 2 guide. Rigour and local dimension NOT VERIFIED. |
| L16 | Zakharov, Ueda, Verstraete, Beenakker, "Symmetric mass generation of interacting chiral fermions on a one-dimensional lattice without fermion doubling" | arXiv:2606.24713v2; Phys. Rev. Research 8, 043009 (2026) | abstract | tangent fermions, "a nonlocal hopping"; DMRG gap for `K < 2/5` | Context. Nonlocal hop: not NN-a. |
| L17 | Zeng, Zhu, Wang, You, "Symmetric Mass Generation in the 1+1 Dimensional Chiral Fermion 3-4-5-0 Model" | arXiv:2202.12355v2; Phys. Rev. Lett. 128, 185301 (2022) | abstract | DMRG; six-fermion terms on the mirror edge of a thin strip; BKT transition | Rung 2 evidence (numerical). |
| L18 | Wang, Wen, "A Non-Perturbative Definition of the Standard Models" | arXiv:1809.11171v3; Phys. Rev. Research 2, 023356 (2020) | abstract (anchors via `LIT_SMG.md` section 2) | propose the 16 of Spin(10) on a 3+1D lattice, premised on "the existence of symmetric gapped boundary" | Rung 4 programme. Its gapped-boundary step is a premise there. |
| L19 | García-Etxebarria, Montero, "Dai-Freed anomalies in particle physics" | arXiv:1808.00009v3; DOI 10.1007/JHEP08(2019)003 | abstract | SM, SU(5), Spin(10) anomaly free; a `Z₄` assumed | Rung 4 anomaly ledger (used by `CH1_5U.md`). |
| L20 | Wan, Wang, "Beyond Standard Models and Grand Unifications: Anomalies, Topological Terms, and Dynamical Constraints via Cobordisms" | arXiv:1910.14668v4; JHEP 07 (2020) 062 | abstract | classification of invertible anomalies | Same. |
| L21 | Tong, "Comments on Symmetric Mass Generation in 2d and 4d" | arXiv:2104.03997v3; DOI 10.1007/JHEP07(2022)001 | abstract | SMG "using gauge dynamics in two and four dimensions" | Alternative mechanisms, rungs 2 and 4. |
| L22 | Razamat, Tong, "Gapped Chiral Fermions" | arXiv:2009.05037v3; Phys. Rev. X 11, 011063 (2021) | abstract | gapping one SM generation "without breaking electroweak symmetry" by extra dynamics | Same. |
| L23 | Eichten, Preskill, "Chiral Gauge Theories on the Lattice" | Nucl. Phys. B 268, 179-208 (1986), DOI 10.1016/0550-3213(86)90207-5 | INSPIRE abstract; text NOT VERIFIED | fermions in a complex representation on the lattice | Origin of the multi-fermion mirror route; context. |
| L24 | Golterman, Shamir, "Constraints on the symmetric mass generation paradigm for lattice chiral gauge theories" | arXiv:2505.20436v3 | abstract (anchors via `LIT_SMG.md` section 8) | "If these conditions are satisfied, the massless fermion spectrum must be vector-like"; SMG bound states are conjectured | Rung 4 constraint (section 5, trick C). |
| L25 | Kikukawa, "On the gauge invariant path-integral measure for the overlap Weyl fermions in 16 of SO(10)" | arXiv:1710.11618v5; PTEP (2019), DOI 10.1093/ptep/ptz115 | abstract | "There remains the issue of locality in the gauge-field dependence of the Weyl fermion measure" | Rung 4 alternative (Euclidean). |
| L26 | Ginsparg, Wilson, "A Remnant of Chiral Symmetry on the Lattice" | Phys. Rev. D 25, 2649 (1982) | INSPIRE abstract; text NOT VERIFIED | a block-spin chiral criterion avoiding doubling | Context. |
| L27 | Lüscher, "Exact chiral symmetry on the lattice and the Ginsparg-Wilson relation" | arXiv:hep-lat/9802011; Phys. Lett. B 428, 342-345 (1998) | abstract | the GW relation "implies an exact symmetry of the fermion action" | Context: the overlap route is Euclidean, not a tick. |
| L28 | Neuberger, "Exactly massless quarks on the lattice" | arXiv:hep-lat/9707022v3; Phys. Lett. B 417, 141-144 (1998) | abstract | overlap for vector-like theories, "no undesired doubling" | Context. |
| L29 | Nielsen, Ninomiya, "Absence of neutrinos on a lattice" I, II | Nucl. Phys. B 185, 20 (1981) (erratum B 195, 541); B 193, 173 (1981) | INSPIRE abstracts; texts NOT VERIFIED | equal numbers of left and right Weyl particles for a class of lattice theories | Ancestor of the framework's own F1-F3 and RC-W, which are what this file uses. |
| L30 | Fidkowski, Xu, "A no-go result for implementing chiral symmetries by locality-preserving unitaries in a 3 dimensional Hamiltonian lattice model of fermions" | arXiv:2306.10105v3; Phys. Rev. Lett. 131, 196601 (2023) | abstract | finite-dimensional on-site spaces: a Weyl `U(1)_A` is not a shallow circuit; `Z_{2N}` fails unless `N_f` is a multiple of `2N` | Rung 4 constraint on `G`. |
| L31 | Chatterjee, Pace, Shao, "Quantized axial charge of staggered fermions and the chiral anomaly" | arXiv:2409.12220v3; Phys. Rev. Lett. 134, 021601 (2025) | abstract | finite-dimensional 1+1D lattice: two integer charges flowing to vector and axial; the anomaly is matched by a non-abelian algebra | Rung 2 constraint. |
| L32 | Mastropietro, "Vanishing of the anomaly in lattice chiral gauge theory" | arXiv:2303.02790 (to appear in Ann. Henri Poincaré) | abstract | exact RG and decay bounds; infinite volume, weak coupling, massive non-compact `U(1)` | Rung 4 technology for the light sector. |
| L33 | You, He, Xu, Vishwanath, "Symmetric Fermion Mass Generation as Deconfined Quantum Criticality" | arXiv:1705.09313v2; Phys. Rev. X 8, 011026 (2018) | abstract | "a symmetric gapped phase can arise for multiples of eight Dirac fermions" | Rung 3 context. |
| L34 | Benfatto, Falco, Mastropietro, "Universal Luttinger Liquid Relations in the 1D Hubbard Model" | arXiv:1106.0356 | abstract | weak repulsive short-range interaction; non-perturbative RG and Ward identities; Borel summability | Rung 1.5 technology (assignment). |

The repository's own map `T/LIT_SMG.md` (2026-11-05) fetched L1, L11, L17-L22, L24, L25, L33 and others with exact anchors; it is prior work, credited, and its anchors are cited above only where marked.

**Search scope.** Fidkowski-Kitaev and the `Z₈`; Majorana translation anomalies; Wang-Wen in 1+1D and 3+1D; Tong and Razamat-Tong; the Dai-Freed and cobordism ledgers; Eichten-Preskill, Kikukawa, Ginsparg-Wilson, overlap, Nielsen-Ninomiya; rigorous gap stability (Yarotsky, Fröhlich-Pizzo, Del Vecchio et al., Michalakis-Pytel); rigorous lattice RG (Mastropietro); 2025-2026 exactly solvable 1+1D chiral lattice theories; Golterman-Shamir; Fidkowski-Xu; Chatterjee-Pace-Shao. **No fetched work gives a rigorous, finite-register, local lattice construction of a chiral 1+1D or 3+1D theory with its mirror gapped.** This is a search result, not an impossibility claim.

## 3. The target theorem in standard mathematics

The wall, quoted: `TOE_ASSEMBLY.md` line 718, "Target theorem: a local finite-register law on `Z^3`, NN-a, with exact on-site symmetry `G ⊇` the Standard Model group, whose light sector is one Weyl 16 of Spin(10) with every mirror and doubler gapped, by symmetric mass generation (SMG) rather than symmetry breaking." The definitions below make each term exact. Definitions D3 and D8 are readings; section 7 four-tests them as R-GEN and R-LIGHT.

### 3.1 Data

**D1 (carrier).** `Λ = Z³`. Site `x` carries `F_x = ΛC⁵`: five CAR modes `c_{x,j} = (γ_{x,2j−1} + iγ_{x,2j})/2`, Majoranas `γ_{x,1..10}`, parity `P_x` (PS-5, `TOE_ASSEMBLY.md` line 205; notation of `LW1_5.md` lines 36-41). Each nearest-neighbour link `ℓ` carries a finite-dimensional register `H_ℓ`, an ordinary tensor factor that commutes with matter (PS-6r, line 183; `LW1_5.md` line 44). `𝔄` is the quasi-local C*-algebra they generate, graded by matter parity.

**D2 (tick).** An automorphism `α` of `𝔄` in NN-a form (GA1-P-NN, `TOE_ASSEMBLY.md` line 235): a fixed finite number of layers; each layer a product of even unitaries `g` on disjoint edge triples `F_x ⊗ F_y ⊗ H_ℓ`; the whole product commutes with every local gauge generator of the law's gauge group `K` (possibly trivial) and with every cell lift of `𝒢 = 2Z³ ⋊ O_{c₀}` (PS-1c, line 180). Each gate comes with a Hermitian `X_g`, `‖X_g‖ < π`, and `g = e^{−iX_g}`. This is the "certified decomposition" of NN-a.

**D3 (generator; reading R-GEN).** `H_α = Σ_g X_g`, as a formal sum of local terms. Its derivation is `δ(A) = iΣ_g[X_g, A]` on local `A` (a finite sum). A state `ω` is a *ground state of the tick* if `ω(A*[H_α, A]) ≥ 0` for every local `A`. It has *gap* `Δ > 0` if, in its GNS representation, the positive generator `H_ω` with `H_ωΩ = 0` satisfies `spec(H_ω) ⊂ {0} ∪ [Δ, ∞)` and `ker H_ω = CΩ`.

**D4 (on-site symmetry).** A compact group `G`, continuous homomorphisms `u_x : G → U(F_x)` into even unitaries, compatible with the cell lifts, and a fixed action on the links. `γ_g = ⊗_x Ad u_x(g)` (with the link action). Require `α∘γ_g = γ_g∘α` for all `g`. Fix an injective homomorphism `ι : G_SM = (SU(3)×SU(2)×U(1))/Z₆ → G`.

**D5 (vacuum).** A state `ω` on `𝔄` that is `α`-invariant, `γ_g`-invariant for every `g ∈ G`, invariant under the cell group, pure, and a ground state of the tick (D3).

**D6 (light fields).** Odd quasi-local elements `ψ_{A,s}` (`A = 1..16`, spinor index `s = 1, 2`) with `γ_g(ψ_{A,s}) = Σ_B D(g)_{BA} ψ_{B,s}`, where `D` is a unitary representation of `G` and `D∘ι` is one Standard Model generation with `ν^c` (CG1, `TOE_ASSEMBLY.md` line 462). When every `K`-invariant element is even, as on both live laws (`RCS1.md` line 66, Theorem 4), the `ψ_{A,s}` are charged-sector fields in a fixed prescription; the owner candidate is R-CS^str (`TOE_ASSEMBLY.md` line 225, not adopted).

**D7 (free reference).** For `c > 0`, the left-handed Weyl two-point function of speed `c` is the distribution `S_c(x,t) = ∫ d³p (2π)^{−3} · ½(1 − p̂·σ⃗) · e^{i(p·x − c|p|t)}`, a `2×2` matrix with entries `S_c(x,t)_{ss'}`; `σ⃗` is the vector of Pauli matrices.

**D8 (scaling limit; reading R-LIGHT).** For `λ > 0` set `ψ^λ_{A,s}(x,t) = λ^{3/2} α^{⌊λt⌋}(τ_{[λx]} ψ_{A,s})`, where `τ_y` is the cell translation by the point `[λx]` of `2Z³` nearest to `λx`, and `t` is counted in ticks.

### 3.2 The statement

**Target Theorem W2.** There exist finite registers `H_ℓ`, a gauge group `K`, a compact group `G ⊇ ι(G_SM)`, a tick `α` as in D2 commuting with `γ_G`, quasi-local fields as in D6 and a state `ω` as in D5 such that:

- **(W2.1) Chiral content.** `Sym²(D)^G = 0`: no `G`-invariant quadratic (Majorana or Dirac) mass exists for the light fields.
- **(W2.2) No symmetry breaking.** `ω` is `G`-invariant and pure, so `ω(A) = 0` for every quasi-local `A` in a nontrivial irreducible `G`-isotypic component.
- **(W2.3) One Weyl 16.** There are `Z > 0` and `c > 0` with `lim_{λ→∞} ω(ψ^λ_{A,s}(x,t) ψ^λ_{B,s'}(0,0)*) = Z δ_{AB} S_c(x,t)_{ss'}` as distributions on `(x,t) ≠ (0,0)`.
- **(W2.4) Nothing else is light.** For every finite family of quasi-local operators, each rescaled by a power of `λ`, the scaling limit of the connected correlations exists and equals the corresponding correlation of a Wick polynomial in the free field of (W2.3). So no mirror, doubler or other massless field survives the limit. "Gapped" for mirrors and doublers means exactly this absence; no rate is part of W2.

(W2.1) forces `G ≠ ι(G_SM)`: under `G_SM` alone `ν^c` is a singlet and `ν^cν^c` is invariant. Both live laws meet (W2.1): for `L5-U` the `U(1)_N` charges `u, −3u, 5u` of `R_u` have no pair summing to zero (`LIT_SMG.md` section 2), and for `L5-O`, `Sym²(16) = 10 ⊕ 126`.

**Consequence already on file (not a premise).** By F1-F3 (`CH1.md` lines 50-62) and RC-W with its condition E (`CG16S.md` lines 120, 140), a quasi-free NN-a tick is vector-like in each preserved weight block at each quasi-energy whose nodes are Weyl points; light content at quasi-energy π makes the limits in (W2.3)-(W2.4) oscillate as `(−1)^{⌊λt⌋}`, so it is excluded too. So any tick meeting (W2.1)-(W2.4) is not quasi-free: the mirrors and doublers are gapped by interactions, which is what "SMG rather than symmetry breaking" means, given (W2.2).

**Variants.** W2[fin]: D1 with any finite site content in place of PS-5; this is the literature's form (L18). W2[L5-U]: the law is `L5-U` (`LW1_5.md` line 96), `K = U(5)`, and `D = f_u^*S⁺ = R_u`, the twisted family (`CH1_5U.md` line 7). W2[L5-O]: the law is `L5-O` (`LW1_5.md` line 89), `K = Spin(10)`. In both gauged variants D6's charged-sector clause applies, and odd bands of D1 states are flat at nodes (`LZ1.md` lines 50, 62), so the light fields cannot be odd bands of a D1 state.

### 3.3 What W2 does not contain

Gauging `G` and a massless gauge field (CH1-ii, `TOE_ASSEMBLY.md` line 447); reflection positivity; three families (W5); breaking to the Standard Model (W4); a common light cone for all species (W3); the identification of D8's scaling limit with the owner's zoom ZM1-INV (line 252), whose invariant-algebra map gives charged sectors "no zoom" (`TOE_ASSEMBLY.md` section 3.9, "What it changes"). These are interfaces, not parts of W2.

## 4. The ladder

Status words, as in the YM outline: **[P]** proved here, not yet distilled or refereed; **[SP]** proved in a named source, cited, not rebuilt; **[R]** a repository result, with the status its source gives; **[O]** open. Open inputs are written `⟦open: NAME⟧` inside the statement that needs them.

All rungs use D2's tick form, D3's generator reading (R-GEN, section 7), finite registers and NN-a. A "1D carrier" is the line `Z` of five-mode sites with links `(x, x+1)` and cell group `2Z ⋊ Z₂` (translations by 2, reflections about the centres of even bonds), the 1D form of PS-1c used by CH1-C1 (`CH1.md` line 114).

### R0. Atoms (0+1D)

**Statement R0[G, n].** Let `G` act on `ΛCⁿ` by even unitaries. (i) No nonzero `G`-invariant quadratic `i Σ_{ab} A_{ab} γ_aγ_b` exists. (ii) Some `G`-invariant even Hermitian `h` has a one-dimensional ground space, spanned by a `G`-invariant vector.

| Instance | Imports | Proof assignment | Status |
|---|---|---|---|
| R0-FK: `n = 4`, `G = S ≅ Z₂⁴` (Definition 6.1), `h = W` | none | New: the extended Hamming code argument, sections 6.2-6.4. Credit: Fidkowski-Kitaev L1 Eq. (8); #10078. | [P] |
| R0-16: the 16 with two spin components (32 modes), `G ⊇ Spin(10)` | — | Port #9910 (`C:2316`) and `S:28`; rebuild natively (for example by the characters of a finite subgroup, as section 6.2 does with `S`, or by a Casimir identity) | [R] logged; `S` "conditional-support" |
| R0-U5: a cell of `L5-U` carrying the mirror of `R_u` | `CH1_5U.md` Theorem 4.1 (the invariant quartics) | New. One site cannot carry it: the ten triple products are not ten CAR modes (`CH1.md` line 126), so the cell spans several sites. | [O] ⟦open: R0-U5⟧ |

### R1. Eight Majorana chains (1+1D), this file

**Statement R1.** On the 1D carrier, with modes 1-4 of each site as the 8 chains, global symmetry `S × Z` (Hamming sign flips and one-site translation of the generator) and gauge group `K = Z₂` (local fermion parity; in both live laws a local centre element acts on matter by `Ad P_x`, as section 3.6 of `TOE_ASSEMBLY.md` records from `LZ1.md` and `RCS1.md`): (a) every `S × Z`-symmetric quadratic form on a ring has all eigenspaces of dimension divisible by 16, and on `Z` its one-body spectrum contains 0; (b) the on-site term `W` has spectrum −14 (1, even), 0 (8, odd), +2 (7, even), and its ground vector spans the `S`-fixed vectors; (c) the zero-hop tick is NN-a, gauge invariant, `S`-symmetric and cell covariant, equals `e^{−iH}` exactly, and `H` has a unique ground state, pure on the invariant algebra, with gap `Δ₀ = min(14τ, τ₅, τ_E)`, in finite and infinite volume; (d) the intrinsic Floquet gap fails, so (c)'s gap is a generator statement; (e) with hopping `θ`, on open segments, the generator keeps a unique ground state and gap `≥ Δ₀/2` for `|θ| ≤ t₀Δ₀/4`.

**Imports.** R0-FK. Frozen: `VC1_5.md` line 50 (purity equivalence); `GA2_Y2.md` Corollary 2.2 (finite images allow exact links). Literature: Fröhlich-Pizzo L5, Theorem 3.5, for (e) only.

**Proof assignment.** (a)-(d): new, section 6. (e): the reduction to L5's hypotheses is new (Lemma 6.9); the stability theorem itself is ported from L5 and not rebuilt.

**Status.** (a)-(d) [P]; (e) [SP] ⟦open: R1-H, a native rebuild of L5 Theorem 3.5 for this chain, and its ring and infinite-volume forms⟧.

### R1.5. Decoupling (1+1D), a new rung

**Statement R1.5.** On the 1D carrier, keep R1 on modes 1-4 and let mode 5 be a light complex chain with the hop `θ_ℓ Σ_ℓ (i c†_{x,5} Z_ℓ c_{x+1,5} + h.c.)` at half filling. The symmetry is `S × U(1)₅ × Z` (`U(1)₅` the number of mode 5). Add any mixing terms `εH_mix` that are local, gauge invariant and symmetric. Then for `|θ|/τ` and `|ε|` small, the generator's ground states have a 1D scaling limit (D8 in one dimension, each field rescaled by its own power of `λ`) that is a `c = 1` Luttinger liquid carried by mode 5, and no other field survives the limit.

**Imports.** R1 including R1-H. Context for the light sector's protection by `U(1)₅` at filling `1/2` with one-site translation: Lieb-Schultz-Mattis-type statements, and Seiberg-Shao L3 and Hsieh-Halász-Grover L4 for Majorana translations. Benfatto-Falco-Mastropietro L34 for rigorous RG of 1D lattice fermions.

**Proof assignment.** New. Quadratic mixing `γ_{x,a}γ_{y,b}` with `a ≤ 8 < b` is forbidden by `S`: every `a ≤ 8` lies in the support of some `g ∈ S`, and `S` acts trivially on mode 5. So `H_mix` starts at quartic order: a light bilinear times an `S`-invariant mirror operator. Steps: integrate out the gapped mirror by a block-diagonalization relative to a gapless remainder (new; L5 needs a global gap); then control the induced marginal light couplings by a constructive 1D RG (to be ported from the programme of L34 after its theorems are read in full); then exclude a light-sector gap by the filling argument.

**Status.** [O] ⟦open: R1.5-D⟧.

### R2. A chiral 1+1D theory with its mirror gapped

**Statement R2.** On a 1D carrier (or a strip `Z × {1..w}` of five-mode sites), finite registers, an NN-a tick with exact on-site `U(1)_A × U(1)_B` (mode charges chosen per site), and a state as in D5, whose 1D scaling limit is a multi-component Luttinger theory whose `U(1)_A` currents have the levels of the 3-4-5-0 content (left movers of charges 3, 4; right movers 5, 0), or of CH1-C1's content (left `(1,7)`, right `(5,5)`), and no other field survives the limit. In 1+1D the light couplings are marginal, so the limit need not be free; the current levels are what the content fixes.

**Imports.** R1.5 (decoupling); the 3450 atom (`C:1690`-`C:1694`: the three-site complete-graph cell, `Δ₀ = (1 − √3/2)g`, with a cited Yarotsky bound "for the vector-like content only", and the remark that in the slab "the mirror relocates"; logged) and its neutral lattice (`C:2334`); frozen F3 in 1D (`CH1.md` line 58) and CH1-C1 (line 114); the spectral obstruction for one-mode staggered carriers (`C:2318`). Literature as guides: Wang-Wen L12 (gapping rules), Thorngren-Preskill-Fidkowski L13 (disentanglers; anomaly-free condition, its Eq. (19)), Seifnashri L14, Lu-Shao L15, Zeng et al. L17 (numerics), Chatterjee-Pace-Shao L31 (finite-dimensional constraint on an exact chiral anomaly; 3450 is anomaly free).

**Proof assignment.** Ported: the K-null gapping lattice (#10058) and the continuum gapping-rule algebra (L12). New: a finite-register carrier with exact on-site `U(1)` charges 3, 4, 5, 0 (L13-L15 use infinite-dimensional bosons, which PS-6r excludes); the mirror's strong-coupling atom with uniform gap (R1-H's method); decoupling (R1.5's method) with a chiral light sector.

**Status.** [O] ⟦open: R2⟧.

### R3. Dimension two (2+1D)

**Statement R3.** (a) On a plane `Z²` of five-mode sites, R1's statements (a)-(c) and (e) hold with `S`-symmetric flavour-diagonal hops, translation by one site in each direction, and the zero modes `Γ^a` at the momenta `{0, π}²`. (b) R1.5's decoupling holds with a light sector of 2D Majorana or Dirac cones whose protection is a lattice anomaly of translation.

**Imports.** R1, R1.5. Literature: Del Vecchio-Fröhlich-Pizzo-Rossi L6 or Yarotsky L7 for stability in `d = 2` (abstracts only); Hsieh-Halász-Grover L4 (2D arrays); You-He-Xu-Vishwanath L33 (context).

**Proof assignment.** (a): sections 6.2-6.5 carry over word for word except the stability step, ported from L6 or L7 after reading their theorems in full. (b): new.

**Status.** (a) [O] ⟦open: R3-H⟧; (b) [O] ⟦open: R3-D⟧.

### R4. The 16 (3+1D): Target Theorem W2

**Statement.** Section 3.2, in the variant W2[fin], W2[L5-U] or W2[L5-O].

**Imports.** R0-16 or R0-U5; R3 (stability and decoupling in higher dimension); frozen `CH1_5U.md` (the anomaly ledger, conditional on cited bordism), RC-W and F3a (chirality bookkeeping), `LZ1.md` Theorem 2.2 and `RCS1.md` Theorem 4 (the light fields are charged sectors on gauged live laws), `GA2_Y2.md` Theorem N (gauging continuous groups with finite registers). Literature: Wang-Wen L18 (programme), Golterman-Shamir L24 (the light-partner test), Fidkowski-Xu L30 (the on-site group must be anomaly free; the 16 has `N_f = 16`, a multiple of 4), Mastropietro L32 (RG technology for massless lattice fermions in 3+1D), Kikukawa L25 (Euclidean alternative).

**Proof assignment.** Ported: the anomaly ledger (`CH1_5U.md`; its bordism inputs L19-L20 stay [SS] until rebuilt). New: everything else, in the order of section 5.

**Status.** [O] ⟦open: W2⟧.

## 5. Hard steps, and the simplest rung for each trick

Seven tricks carry the ladder. Each row names the trick, the rung where it is hardest and why, and the simplest rung where it can be proved first.

| Trick | Content | Hardest at | Why it is hardest there | Simplest rung |
|---|---|---|---|---|
| A. Symmetric atom | every quadratic forbidden; a unique symmetric ground state on a site or cell | R0-U5 | On `L5-U` one site cannot carry the family (`CH1.md` line 126), so the atom is a multi-site cell whose sites are joined by gauge links; the 16's cell is 32 modes or more | R0-FK. **Done here** (6.2-6.4). |
| B. Stability | a uniform gap with hopping, from a product ground state | R4 | Three dimensions; the light sector is present; atomic control alone keeps the volume (`S:235`, `S:239`) | R1-H: 1D, nearest-neighbour, product state. Ported from L5 (6.6); native rebuild open. |
| C. Decoupling | mirror gapped, light sector gapless, no light partners | R2 and R4 | Every stability theorem read here (L5-L8) assumes a global gap; the light sector has none. The failed routes on file fail at this step: a symmetric block mirror gap releases the light partners (`C:519`); the tetrahedral FK term gaps both copies (`C:2315`); a gapped far layer moves the mirror in (`C:1491`, `S:201`). In 3+1D Golterman-Shamir (L24) adds the test that composite partners stay heavy. | R1.5: the light sector is non-chiral, protected by filling, and couples to the mirror only at quartic order because `S` forbids quadratic mixing. |
| D. Chirality on a tick | a chiral light sector although free NN-a ticks are vector-like | R4 | F3a forces equal chirality at 0 and π (`CH1.md` line 58), RC-W gives zero net chirality (`CG16S.md` line 120), the π flow is forced (`C:19`); the 16 must also pass L24 | R2 (abelian charges; known gapping rules L12; numerics L17). |
| E. Light fields on a gauged law | odd light fields when every gauge-invariant element is even | R4 on `L5-O`/`L5-U` | `RCS1.md` Theorem 4; odd bands of D1 states are flat (`LZ1.md` line 62); no local 16 on `L5-O`; four frozen routes (`LW1_5.md` Amendment 3) | R1.5 with `K = Z₂`: the light fermion of mode 5 is odd, so its correlations already need `Z_ℓ`-string dressing, the simplest charged-sector prescription. |
| F. Tick versus generator | gap and ground state of a Floquet tick | every rung with hopping | Proposition 6.7: even the zero-hop product tick has `1` in the spectrum of its GNS unitary on `Ω^⊥`, so "gap" has content only through a generator (R-GEN) or a new Floquet notion | R1. Proposition 6.7 is proved there. ⟦open: FLQ, the tick's own dynamics from the generator's gap⟧ |
| G. Gauging with finite registers | `G` gauged with PS-6r links | CH1-ii (after W2) | Theorem N (`GA2_Y2.md` line 37): no invertible covariant link for a group of infinite image | R1 for finite groups (exact links, Proposition 6.10); a 1+1D `U(1)` quantum-link version of R2 for continuous groups. |

**The hard step of each rung.**

- **R0:** trick A for the 16. Its cell is large, and on `L5-U` it spans sites.
- **R1:** trick B. The perturbation is extensive and the unperturbed term is interacting. Rung 1 is also the simplest place for it.
- **R1.5:** tricks C and E. Rung 1.5 is the simplest place for both.
- **R2:** trick D on top of C, with finite registers and exact on-site `U(1)` charges. The solvable 2026 constructions (L13-L15) use infinite-dimensional bosons, and one-mode staggered carriers have a spectral obstruction (`C:2318`).
- **R3:** tricks B and C in two dimensions. The 1D tools (L5, L34) do not apply. Four-fermion couplings are irrelevant in 2+1D, which helps C.
- **R4:** tricks C, D and E together, with A for the 16. Four-fermion couplings are irrelevant in 3+1D (L32's setting).

**Which step is the wall.** Trick C is the hardest in the ladder. No work read here proves a mirror gap next to a gapless chiral sector on a finite-register local lattice; every prior repository attempt on file stops there. This is a statement about what was found, not a no-go.

## 6. Rung 1 attacked

**Rung 1, as the lane brief states it.** "on a framework tick (one-mode or five-mode sites, NN-a, finite registers), eight Majorana chains in 1+1D with an exact symmetry that forbids every quadratic mass admit a symmetric, local, gauge-invariant update and state with a gap and a unique symmetric ground state; re-prove Fidkowski-Kitaev natively." Below it is proved on five-mode sites, in the generator reading R-GEN (section 7), for zero hop; the chain hop is added by a ported stability theorem (6.6). One-mode sites are not treated.

### 6.1 The carrier and the tick

**Carrier.** `Λ` is `Z`, a ring `Z_L` (`L ≥ 2`, sites `0..L−1`) or a segment `{1..N}`. Site `x` carries `F_x = ΛC⁵` with Majoranas `γ_{x,1..10}` (D1). Write `c_a = γ_{x,a}` for `a = 1..8` when the site is fixed: these are the **eight chains**. Mode 5 is `(γ_{x,9}, γ_{x,10})`, with number `n_{x,5}`. Each link `ℓ = (x, x+1)` carries `H_ℓ = C²` with Pauli operators `X_ℓ, Z_ℓ`.

**Gauge group.** `K = Z₂` at each site. The Gauss operator is `G_x = P_x ∏_{ℓ ∋ x} X_ℓ`; physical states have `G_x = 1`. In both live laws a local centre element acts on matter by `Ad P_x` (section 4, R1), so rung 1 gauges exactly that part.

**Definition 6.1 (the group `S` and the term `W`).** At one site put
`g₁ = −c₁c₂c₃c₄`, `g₂ = −c₅c₆c₇c₈`, `g₃ = −c₁c₂c₅c₆`, `g₄ = −c₁c₃c₅c₇`,
let `S = ⟨g₁, g₂, g₃, g₄⟩`, and let `W = −Σ_{g ∈ S, deg g = 4} g`, where `deg` is the number of Majorana factors. The global action of `g ∈ S` is `γ_g = ⊗_x Ad g_x`, with `g_x` the copy of `g` at site `x`; it fixes links and mode 5.

**Definition 6.1b (the rung-1 tick).** Fix `τ, τ₅, τ_E > 0` with `16τ + τ₅ < π`, `τ_E < π`, and `θ` with `4|θ| < π`. Local generators:
- `h^{FK}_x = τ(W_x + 14)` and `h⁵_x = τ₅ n_{x,5}` (on-site),
- `e_ℓ = τ_E(1 − X_ℓ)/2` (one link),
- `b_ℓ = (i/2) Σ_{a=1}^{8} γ_{x,a} Z_ℓ γ_{x+1,a}` for `ℓ = (x, x+1)` (an edge triple).

Layers: `L₁ = ∏_x e^{−i(h^{FK}_x + h⁵_x)}`, `L₂ = ∏_ℓ e^{−ie_ℓ}`, `L₃ = ∏_{x even} e^{−iθ b_{(x,x+1)}}`, `L₄ = ∏_{x odd} e^{−iθ b_{(x,x+1)}}`. The tick is `U = L₄L₃L₂L₁`. Its generator in the reading R-GEN is
`H(θ) = Σ_x (h^{FK}_x + h⁵_x) + Σ_ℓ e_ℓ + θ Σ_ℓ b_ℓ`, and `H₀ = H(0)`.
Replacing `Z_ℓ` by 1 and setting `τ = τ₅ = 0` gives the free tick of eight critical Majorana chains (LW1-5's free-tick convention, `LW1_5.md` inferred definition 4).

### 6.2 The Fidkowski-Kitaev atom, natively

The proof below replaces Fidkowski and Kitaev's route (L1, Sec. II.1, which shows uniqueness through `W₁` and leaves the `so(7)` check to a computer) by the extended Hamming code. It needs no computer.

**Lemma 6.2 (the structure of `S`).** For `u ⊆ {1..8}` write `c_u` for the ordered product of the `c_a`, `a ∈ u`, and identify `u` with its indicator vector in `F₂⁸`.

1. `c_u† = (−1)^{|u|(|u|−1)/2} c_u`, `c_u² = (−1)^{|u|(|u|−1)/2}`, and `c_u c_v = (−1)^{|u||v| − |u∩v|} c_v c_u`. In particular each `g_i` is a Hermitian involution and the `g_i` commute.
2. `n ↦ g₁^{n₁}g₂^{n₂}g₃^{n₃}g₄^{n₄}` is an isomorphism `F₂⁴ → S`. So `S` is abelian of order 16, and `−1 ∉ S`.
3. Every `g ∈ S` is `±c_u` with `u` in the code `C ⊂ F₂⁸` spanned by `u₁ = 11110000`, `u₂ = 00001111`, `u₃ = 11001100`, `u₄ = 10101010`; `g ↦ u` is an isomorphism `S → C`. `C` has one word of weight 0, fourteen of weight 4 and one of weight 8. `C = C^⊥`, and `C` has no word of weight 2.
4. `g₈ := g₁g₂ = c₁c₂⋯c₈ = P^{(4)}`, the parity of modes 1-4.
5. For `g = ±c_u ∈ S`: `g c_a g⁻¹ = (−1)^{u_a} c_a`.
6. `tr c_u = 0` on the 16-dimensional Fock space `V` of modes 1-4 whenever `u ≠ 0`.

*Proof.* (1) Reversing `k` factors costs `k(k−1)/2` transpositions; this gives the adjoint and the square. Moving each `c_b`, `b ∈ v`, through `c_u` costs `|u| − [b ∈ u]` signs. The four supports `{1234}, {5678}, {1256}, {1357}` meet pairwise in 0 or 2 points, so the `g_i` commute. (2) The `g_i` are commuting involutions, so the map is a surjective homomorphism. The support of a product is the sum in `F₂⁸` of the supports, and `u₁..u₄` are linearly independent. So `φ(n)` has empty support only for `n = 0`, where it is `+1`. (3) The sixteen sums of `u₁..u₄` are: `0`; `u₁, u₂, u₃, u₄` = `{1234}, {5678}, {1256}, {1357}`; `u₁+u₂ = {1..8}`; `u₁+u₃ = {3456}`, `u₁+u₄ = {2457}`, `u₂+u₃ = {1278}`, `u₂+u₄ = {1368}`, `u₃+u₄ = {2367}`; `u₁+u₂+u₃ = {3478}`, `u₁+u₂+u₄ = {2468}`, `u₁+u₃+u₄ = {1458}`, `u₂+u₃+u₄ = {2358}`; `u₁+u₂+u₃+u₄ = {1467}`. The weights are as stated. Any two words meet evenly (by (1), since `S` is abelian and all weights are even), so `C ⊆ C^⊥`; both have dimension 4. (4) `g₁g₂ = c₁⋯c₈`. With `a_j = (c_{2j−1} + ic_{2j})/2`, `n_j = (1 + ic_{2j−1}c_{2j})/2`, so `1 − 2n_j = −ic_{2j−1}c_{2j}` and `P^{(4)} = (−i)⁴c₁⋯c₈`. (5) Item (1) with `v = {a}` and `|u|` even. (6) Pick `a ∈ u`. Then `c_a c_u c_a⁻¹ = (−1)^{|u|−1}c_u = −c_u`, so `tr c_u = −tr c_u`. ∎

The fourteen weight-4 words of (3) are exactly the fourteen supports in Fidkowski-Kitaev's Eq. (8).

**Theorem 6.3 (the atom).** On `V`:

1. For each character `χ : S → {±1}`, `V_χ = {v : gv = χ(g)v for all g ∈ S}` is one-dimensional, and `V = ⊕_χ V_χ`.
2. `W` acts on `V_χ` as `−14` if `χ = 1`; as `2` if `χ ≠ 1` and `χ(g₈) = 1` (seven characters); as `0` if `χ(g₈) = −1` (eight characters).
3. `V₁ = Cψ` is the space of `S`-fixed vectors, and `ψ` is even. The odd sector is spanned by the orthonormal vectors `c_aψ`, `a = 1..8`.
4. No nonzero `S`-invariant quadratic `iΣ_{ab}A_{ab}c_ac_b` exists.
5. `W` equals Fidkowski-Kitaev's Eq. (8), with their Majoranas identified with `c_a` by their Eqs. (9)-(10), which agree with D1.

*Proof.* (1) `P_χ = (1/16)Σ_{g∈S} χ(g) g` is a family of orthogonal projections with `Σ_χ P_χ = 1` (character orthogonality). By Lemma 6.2(6), `tr P_χ = (1/16) tr 1 = 1`. (2) On `V_χ`, `W = −(Σ_{g∈S}χ(g) − χ(1) − χ(g₈)) = −16[χ = 1] + 1 + χ(g₈)`. The characters with `χ(g₈) = 1` form a subgroup of order 8. (3) `V₁` is the fixed space by definition, and `g₈ = P^{(4)}` acts on it as `+1`. By Lemma 6.2(5), `c_aψ ∈ V_{ρ_a}` with `ρ_a(±c_u) = (−1)^{u_a}`, and `ρ_a(g₈) = −1`. If `ρ_a = ρ_b` then `e_a + e_b ∈ C^⊥ = C`, which has no weight-2 word; so the eight `ρ_a` are distinct, and the unit vectors `c_aψ` lie in eight different lines. (4) `Ad g` multiplies `c_ac_b` (`a ≠ b`) by `(−1)^{u_a + u_b}`; invariance for all `g` needs `e_a + e_b ∈ C^⊥`, impossible. (5) By hand for three terms: `−g₁ = +c₁c₂c₃c₄`; `g₁g₃ = −c₃c₄c₅c₆`, so `−g₁g₃ = +c₃c₄c₅c₆`; `g₃g₄ = c₂c₃c₆c₇`, so `−g₃g₄ = −c₂c₃c₆c₇`. Each matches the sign in Eq. (8). [check] `check_fk.py` confirms all fourteen and the spectrum. Items (1)-(4) use only Definition 6.1, not this identification. ∎

So the printed spectrum of #10078 (−14 (1), 0 (8, odd), +2 (7, even)) and Fidkowski-Kitaev's statements that `W` "annihilates 8₋", has "eigenvalue −14" on their ground state and "eigenvalue 2 on the remaining vector multiplet 7" (L1, Sec. II.2) are re-proved, without the `so(7)` computation.

### 6.3 Every quadratic mass is forbidden

**Theorem 6.4 (free no-go).** Let `Λ = Z_L`, `L ≥ 2`. Let `Q = (i/4)Σ A_{xα,yβ} γ_{x,α}γ_{y,β} + const`, with `A` real antisymmetric and `α, β ∈ {1..10}`, be invariant under `γ_g` for every `g ∈ S` and under the one-site translation `τ₁` of the ring. Then:

1. `A_{xa,yβ} = 0` whenever `a ≤ 8` and `β ≠ a`.
2. The operators `Γ^a = Σ_{x∈Z_L} γ_{x,a}`, `a = 1..8`, commute with `Q`, and `{Γ^a, Γ^b} = 2Lδ_{ab}`.
3. Every eigenspace of `Q` on the Fock space `⊗_x ΛC⁵` has dimension divisible by 16. In particular no such `Q` has a unique ground state, on any ring.
4. On `Λ = Z`, if `A` is translation invariant with finite range, the one-body energy of each flavour `a ≤ 8` is `|2Σ_{r>0} A_{0a,ra} sin(kr)|`, which vanishes at `k = 0` and `k = π`. So every such `Q` is gapless.

*Proof.* (1) By Lemma 6.2(5), `γ_g` multiplies `γ_{x,α}γ_{y,β}` by `(−1)^{u_α + u_β}`, with `u₉ = u₁₀ = 0`. The quadratic monomials are linearly independent, so invariance holds term by term: `A_{xα,yβ} ≠ 0` forces `u_α = u_β` for every `u ∈ C`. For `α ≤ 8 < β` this fails, since every coordinate lies in `u₁` or `u₂`. For `α, β ≤ 8`, `α ≠ β`, it would put `e_α + e_β` in `C^⊥ = C`, which has no weight-2 word. (2) By (1), the flavour-`a` part is `(i/4)Σ_{x≠y} A^a_{xy} γ_{x,a}γ_{y,a}`, with `A^a_{x+1,y+1} = A^a_{xy}`. For `x ≠ y`, `[γ_{z,a}, γ_{x,a}γ_{y,a}] = 2δ_{zx}γ_{y,a} − 2δ_{zy}γ_{x,a}`. So `[Γ^a, Q] = (i/2)(Σ_y R^a_y γ_{y,a} − Σ_x R'^a_x γ_{x,a})` with column sums `R^a_y = Σ_x A^a_{xy}` and row sums `R'^a_x = Σ_y A^a_{xy}`. Translation invariance makes both equal to `Σ_r A^a_{0r}`, so the bracket vanishes. Terms in other flavours and in mode 5 are even in disjoint Majoranas and commute with `Γ^a`. The anticommutator is `Σ_{x,y}{γ_{x,a}, γ_{y,b}} = 2Lδ_{ab}`. (3) The `Γ^a/√L` obey the relations of eight anticommuting Hermitian involutions. The algebra they generate is a quotient of `Cl₈ ⊗ C ≅ M₁₆(C)`, which is simple, so it is `M₁₆(C)` itself. Each eigenspace of `Q` is invariant under it, hence a direct sum of copies of the only simple module `C¹⁶`. (`Cl₈ ⊗ C ≅ M₁₆(C)`: eight Jordan-Wigner Majoranas on four qubits generate all of `M₁₆(C)`, so the 256-dimensional abstract algebra maps onto `M₁₆(C)` and is isomorphic to it.) (4) For flavour `a`, `f(r) = A_{0a,ra}` satisfies `f(−r) = −f(r)`, and the one-body operator `iA` has symbol `iΣ_r f(r)e^{ikr} = −2Σ_{r>0} f(r) sin(kr)`, real and odd in `k`. ∎

**Why translation is needed.** The dimerised term `Σ_x (−1)^x (i/2)γ_{x,a}γ_{x+1,a}` is `S`-invariant, not `τ₁`-invariant, and gaps flavour `a`. Seiberg and Shao (L3, Eq. (1.17)) identify the Majorana translation at low energy with the chiral fermion parity `(−1)^{F_L}`, which is the continuum reason.

### 6.4 The tick at zero hop, and why eight

**Theorem 6.5 (rung 1 at zero hop).** Let `θ = 0` and `Δ₀ = min(14τ, τ₅, τ_E)`.

1. **Admissibility.** Every gate of `U` is supported in one site or one link, is even, commutes with every `G_y` and with every `γ_g`, `g ∈ S`. `U` commutes with the translations and with the reflection `r: x ↦ 1 − x`, `γ_{x,α} ↦ (−1)^x γ_{1−x,α}`, `X_ℓ, Z_ℓ ↦ X_{rℓ}, Z_{rℓ}` (on a ring take `L` even, so that `(−1)^x` is defined); these act transitively on sites. (For `θ ≠ 0` the same holds for translations by 2 and `r`, which maps even bonds to even bonds, and the sign `(−1)^x` makes `r(b_ℓ) = b_{rℓ}`.)
2. **Finite volume** (any ring or segment). `U = e^{−iH₀}`, the terms of `H₀` commute, and `H₀ ≥ Δ₀(1 − |Ψ⟩⟨Ψ|)`, `H₀Ψ = 0`, where `Ψ = ⊗_x(ψ_x ⊗ |0⟩_{x,5}) ⊗ ⊗_ℓ |+⟩_ℓ` and `X|+⟩ = |+⟩`. So `Ψ` is the unique ground state, with gap at least `Δ₀`. `Ψ` is gauge invariant (`G_xΨ = Ψ`), `S`-invariant, and invariant under translations and `r`.
3. **Infinite volume** (`Λ = Z`). The product state `ω₀` of the vectors above is the only state `ω` on `𝔄` with `ω(A*[H₀, A]) ≥ 0` for all local `A`. It is `α`-invariant, `γ_g`-invariant, gauge invariant and cell invariant. It is pure on `𝔄` and pure on the invariant algebra `𝔄^K`. Its GNS generator `H_{ω₀} ≥ 0` has `ker H_{ω₀} = CΩ` and `spec H_{ω₀} ⊂ {0} ∪ [Δ₀, ∞)`.

*Proof.* (1) On-site gates act in `F_x`, link gates in `H_ℓ`. `W_x` and `n_{x,5}` are even, and `G_y` acts on site `y` as `P_y`, which commutes with even elements, and on links by `X`, which commutes with `e_ℓ`. `W` is a sum of elements of the abelian group `S`, so `Ad g_x` fixes it; `S` acts trivially on mode 5 and links. Under `r` each term of `W_x` has four Majoranas of one site (sign `((−1)^x)⁴ = 1`); `n_{x,5}` has two; `P_x` has ten. For the hop, `r(b_{(x,x+1)}) = (i/2)Σ_a (−1)^{2x+1} γ_{1−x,a}Z γ_{−x,a} = b_{(−x,1−x)}`, and `−x` has the parity of `x`.
(2) `h^{FK}_x`, `h⁵_x` and `e_ℓ` act on different modes or factors and are even, so they commute, and `U = e^{−iH₀}`. Each is `≥ 0` and has a one-dimensional kernel on its own factor (modes 1-4, mode 5, or the link): `Cψ` for `h^{FK}_x`, whose next eigenvalue is `τ(0 + 14)` (Theorem 6.3); `|0⟩_5` for `h⁵_x`; `|+⟩` for `e_ℓ`. Each is at least its gap on the complement of its kernel. With `p_X` the kernel projections, `H₀ ≥ Δ₀Σ_X(1 − p_X) ≥ Δ₀(1 − ∏_X p_X)`, because for commuting projections the sum is at least 1 wherever the product is 0. `∏_X p_X = |Ψ⟩⟨Ψ|`. `G_xΨ = Ψ` because `ψ_x` is even, mode 5 is empty and `X|+⟩ = |+⟩`. `g_xψ_x = ψ_x` by Theorem 6.3(3). The reflection's sign at site `x` is implemented by `P_x`, which fixes the even vector there.
(3) Let `ω` satisfy the ground-state inequality. Take a term `t` with kernel vector `κ` and an eigenvector `e` with eigenvalue `λ_e > 0`, and put `A = |κ⟩⟨e|`, a local element on `t`'s factor. Every other term commutes with `A` (other factors, or other modes of the same site with an even term), so `[H₀, A] = [t, A] = −λ_e A`. Then `0 ≤ ω(A*[H₀, A]) = −λ_e ω(|e⟩⟨e|)`, so `ω(1 − p_X) = 0` for every term. By Cauchy-Schwarz `ω(B) = ω(p_R B p_R)` for `B` supported in a finite region `R`, where `p_R` is the product of the kernel projections of the terms in `R`, a rank-one projection onto the local product vector. So `ω = ω₀`. Conversely `ω₀(A*[H₀, A]) = ⟨AΨ, H₀AΨ⟩ ≥ 0` on a large enough region. Purity: if `ω₀ = λφ₁ + (1 − λ)φ₂`, then `φ_i(1 − p_X) = 0` for all `X`, and the same argument gives `φ_i = ω₀`. Purity on `𝔄^K` follows from `VC1_5.md` line 50 (frozen): for a gauge-invariant state, purity on the invariant algebra equals extremality among gauge-invariant states, and `ω₀` is extremal among all states. Invariance: `UΨ_R = Ψ_R` on each region, and part (2). The GNS space is spanned by vectors with finitely many excited factors; `H_{ω₀}` acts on them by sums of excitation energies, each at least `Δ₀`. ∎

**Lemma 6.6 (why eight, for sign-flip symmetries).** Let `ν = 2n` Majoranas `γ₁..γ_ν` act on `ΛCⁿ`. Let `U ⊆ F₂^ν` be a subspace of even-weight vectors, and let `D_u` (`u ∈ U`) be the automorphism `γ_a ↦ (−1)^{u_a}γ_a`, implemented by `c_u`. Suppose (i) no nonzero quadratic `iΣA_{ab}γ_aγ_b` is invariant under all `D_u`, and (ii) some `D_U`-invariant Hermitian operator has a unique ground vector. Then `ν ≥ 8`. For `ν = 8`, `U = C` (Lemma 6.2(3)) satisfies both, with `W` as the operator.

*Proof.* (ii) gives a pure invariant state: if `h` commutes with every `c_u` and has a unique ground vector `φ`, then each `c_uφ` is a ground vector, so `c_uφ ∈ Cφ`. If `u·v = 1` for some `u, v ∈ U`, then `c_uc_v = −c_vc_u` (Lemma 6.2(1)), and eigenvalues `λ, μ ≠ 0` would give `λμφ = −λμφ`. So `U ⊆ U^⊥`, and `k = dim U ≤ ν/2`. Define `s_a ∈ U*` by `s_a(u) = u_a`. Then `s_a = s_b` exactly when `e_a + e_b ∈ U^⊥`, which (i) forbids for `a ≠ b`. So the `ν` vectors `s_a` are distinct in `U* ≅ F₂^k`, `ν ≤ 2^k`, and self-orthogonality reads `Σ_a s_a s_aᵀ = 0` over `F₂`. For `ν = 2`: `k = 1`, `{s_a} = {0, 1}`, and the sum is `1`. For `ν = 4`: `k = 2`, `{s_a} = F₂²`, and the sum is the matrix with rows `(0,1)` and `(1,0)`. For `ν = 6`: `k = 3`, and `{s_a}` is `F₂³` minus two vectors `v ≠ w`. The sum over all of `F₂³` is 0 (each diagonal entry counts 4 vectors, each off-diagonal entry 2), so the remaining sum is `vvᵀ + wwᵀ`, whose diagonal is `v + w ≠ 0`. Each case contradicts. For `ν = 8` and `U = C`: (i) is Theorem 6.3(4), and (ii) is Theorem 6.3(2). ∎

So, within sign-flip symmetries, eight is the least number of Majoranas per site at which every quadratic is forbidden while a symmetric operator still has a unique ground state. For two, four or six, either a symmetric quadratic exists or no symmetric operator has a unique ground state. This is the class's form of Fidkowski-Kitaev's "eight"; it is not their `Z₈` theorem (L1, L2).

### 6.5 The tick itself has no spectral gap

Write `α(A) = U*AU` and let `U_ω` be the unitary on the GNS space of `ω₀` with `U_ω π(A)Ω = π(α(A))Ω`.

**Proposition 6.7 (no intrinsic Floquet gap).** In Theorem 6.5(3), for every `τ ∈ (0, π/16)`, `1` lies in the spectrum of `U_ω` restricted to `Ω^⊥ ∩ \overline{π(𝔄^K)Ω}`.

*Proof.* Pick a unit vector `e` in a seven-level line `V_χ` (`χ ≠ 1`, `χ(g₈) = 1`) and put `K_x = |e⟩⟨ψ|` at site `x`. `K_x` is even and supported on one site, so it lies in `𝔄^K`. For distinct sites `x₁..x_n`, `ξ_n = π(K_{x₁}⋯K_{x_n})Ω` is a unit vector orthogonal to `Ω`, and `U_ωξ_n = e^{16iτn}ξ_n`, since each excited site raises `H₀` by `τ(2 + 14)`. If `16τ/2π = p/q` is rational, `n = q` gives the eigenvalue 1. If it is irrational, the pigeonhole principle gives, for every `N`, some `n ≤ N` with `16τn` within `2π/N` of `2πZ`. The spectrum is closed. ∎

So "gap" for a tick has content only through a generator. Rung 1 therefore states its gap for the generator, as D3 and the reading R-GEN do. Whether the tick's own dynamics keeps `ω₀`'s neighbourhood stable for `θ ≠ 0`, beyond the generator statement, is ⟦open: FLQ⟧: for `θ ≠ 0`, find a stationary state of `α` that is pure on `𝔄^K`, cell invariant and `S`-invariant, and agrees with the ground state of `H(θ)` up to `O(θ)` on local observables.

### 6.6 The chain hop

**Lemma 6.9 (reduction to a spin chain).** On a segment `{1..N}`, order the matter Majoranas lexicographically in `(x, α)` and let `J` be the Jordan-Wigner unitary onto `⊗_{x=1}^{N} (C³² ⊗ C²)`, the `x`-th factor holding site `x` and link `(x, x+1)` (at `x = N` a dummy link carrying only its electric term `e_N`, which commutes with everything, has kernel `|+⟩` and gap `τ_E ≥ Δ₀`, so it changes neither uniqueness nor any gap below `Δ₀`). Then `J (H(θ) + e_N) J* = Δ₀(Σ_x H_x + t Σ_{x<N} V_{x,x+1})` with:
- `H_x = (h^{FK}_x + h⁵_x + e_{(x,x+1)})/Δ₀ ≥ 0`, with a unique zero vector and `H_x ≥ 1` on its orthogonal complement;
- `V_{x,x+1} = J b_{(x,x+1)} J*/4`, supported on factors `x, x+1`, with `‖V‖ ≤ 1`;
- `t = 4θ/Δ₀`.
Each hop gate `e^{−iθb_ℓ}` is even, gauge invariant and `S`-invariant.

*Proof.* Even operators supported on sites `x, x+1` map under `J` to operators on factors `x, x+1`: the Jordan-Wigner strings of two Majoranas cancel except between them in the order, which stays inside the two sites. The link qubits are ordinary factors. `H_x` is as in the proof of Theorem 6.5(2). The eight terms `(i/2)γ_{x,a}Zγ_{x+1,a}` commute (distinct Majoranas, one common `Z`) and have eigenvalues `±1/2`, so `‖b_ℓ‖ ≤ 4`. Gauge invariance: `G_x` changes the sign of `γ_{x,a}` (through `P_x`) and of `Z_ℓ` (through `X_ℓ`), so it fixes `b_ℓ`; likewise `G_{x+1}`. `γ_g` multiplies `γ_{x,a}γ_{x+1,a}` by `(−1)^{2u_a} = 1`. ∎

**Theorem 6.8 (rung 1 with hop) [SP].** Let `t₀` be the constant of Fröhlich-Pizzo's Theorem 3.5 (L5) for local dimension 64 and range 1. If `|θ| < t₀Δ₀/4`, then for every `N` the generator `H(θ)` on `{1..N}` has a unique ground state `Ψ_N(θ)` and gap at least `Δ₀/2`; `Ψ_N(θ)` is gauge invariant and `S`-invariant.

*Proof.* Lemma 6.9 puts `(H(θ) + e_N)/Δ₀` in L5's form ((1.2), (1.4)-(1.7)), and L5's Theorem 3.5 gives uniqueness and gap `≥ 1/2` for `|t| < t₀`, uniformly in `N`. This step is cited, not rebuilt. The dummy term `e_N` commutes with `H(θ)` and has gap `τ_E ≥ Δ₀`, so both conclusions hold for `H(θ)` itself. The `G_x` and the `γ_g` commute with `H(θ)` and have finitely many eigenvalues. A unique ground state is an eigenvector of each. While the gap stays open the ground-state projection is continuous in `θ` (a Riesz projection), so each eigenvalue is constant on the interval and equals its value `+1` (trivial character) at `θ = 0`. ∎

The ring and the infinite chain are not covered by L5's statement as read. They are ⟦open: R1-H⟧, together with a native rebuild of L5's Theorem 3.5. Yarotsky (L7) is a candidate source for the infinite chain; only its abstract was read.

### 6.7 Gauging all of `S`

**Proposition 6.10.** Replace `K = Z₂` by `K = S` at each site. Give each link the register `ℓ²(Ŝ) ≅ C¹⁶` with electric basis `|χ⟩`, `g ∈ S` acting at either end by `χ(g)`, Wilson shifts `M_{ρ,ℓ}|χ⟩ = |χρ⟩`, hop `b^S_ℓ = (i/2)Σ_a γ_{x,a} M_{ρ_a,ℓ} γ_{x+1,a}` (`ρ_a` as in Theorem 6.3(3)) and electric term `τ_E(1 − |1⟩⟨1|_ℓ)`. Then Theorem 6.5, Lemma 6.9 and Theorem 6.8 hold as stated, with local dimension `32 · 16` in Theorem 6.8. The links are exact unitaries; this is the finite-image case allowed by `GA2_Y2.md` Theorem 2.1 (N) and Corollary 2.2.

*Proof.* The Gauss operators are `G_x(g) = g_x χ_{ℓ₋}(g) χ_{ℓ₊}(g)`, diagonal on links. Under `G_x(g)`, `γ_{x,a}` changes by `ρ_a(g)`, and `M_{ρ_a,ℓ}` changes by `ρ_a(g)` because it shifts `χ_ℓ` by `ρ_a`; the product is fixed. The same holds at `x+1`. `W_x` commutes with `g_x`. The state with `ψ_x`, empty mode 5 and `|1⟩` on every link satisfies `G_x(g) = 1`. The rest of each proof is unchanged, with `‖b^S_ℓ‖ ≤ 4`. ∎

With `S` gauged, the symmetry that forbids every quadratic mass is itself the gauge group, as for the mirrors in W2.

### 6.8 Verdict on rung 1

**Proved here [P], in the reading R-GEN, on five-mode sites:**
1. The eight chains carry an exact on-site symmetry `S ≅ Z₂⁴` (with one-site translation) under which every quadratic mass is forbidden: every symmetric quadratic form has all eigenspaces of dimension divisible by 16 on every ring, and is gapless on `Z` (Theorem 6.4).
2. Fidkowski-Kitaev's on-site interaction, rebuilt as `W = −Σ_{deg g = 4} g` over the Hamming stabilizer group, has spectrum −14 (1), 0 (8, odd), +2 (7, even) and a unique `S`-fixed ground vector (Theorem 6.3).
3. The rung-1 tick is NN-a, gauge invariant (for `K = Z₂`, and for `K = S`), `S`-symmetric and cell covariant. At zero hop it equals `e^{−iH₀}`, and `H₀` has a unique ground state, gauge invariant, `S`-invariant, translation invariant and pure on the invariant algebra, with gap `min(14τ, τ₅, τ_E)`, in finite and infinite volume (Theorem 6.5, Proposition 6.10).
4. Eight is the least number of Majoranas per site at which sign-flip symmetries forbid every quadratic while a symmetric operator has a unique ground state (Lemma 6.6).
5. The tick has no intrinsic spectral gap (Proposition 6.7).

**Proved in a source [SP]:** with the chain hop, for `|θ| < t₀Δ₀/4`, on open segments, uniqueness, symmetry and gap `≥ Δ₀/2` (Theorem 6.8, through L5 and the native Lemma 6.9).

**Not treated:** one-mode sites; Fidkowski-Kitaev's 1D path (L1, Sec. II.2); the weak-coupling regime, where the gap of the free critical chains would have to open at small `τ/θ` (#10078's numerics suggest `g_c ∈ (0.125, 0.25]` in its normalisation).

Rung 1 closes at a proof, in the generator reading. The two named open statements it leaves, R1-H (native, ring, infinite chain) and FLQ (the tick's own dynamics), are statements, not failed lemmas.

## 7. Readings for the owner, four-tested

Nothing here is adopted. Each reading gets the four tests of `TOE_ASSEMBLY.md` section 3.2: it fails if it (1) states or fixes a part's target, (2) is open-ended, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. P = passes, C = passes on a stated condition, F = fails.

**R-GEN (the generator of a tick).** Text: "For a tick given with its certified NN-a decomposition into gates `g = e^{−iX_g}`, `X_g` Hermitian with `‖X_g‖ < π`, the tick's generator is `H_U = Σ_g X_g`. In SMG1's rungs and in W2, a ground state, a unique ground state and a gap of the tick mean those of `H_U`, as in D3."
- *Reason.* Proposition 6.7: the zero-hop rung-1 tick, the simplest gapped tick there is, has `1` in the spectrum of its GNS unitary on `Ω^⊥` for every step. A spectral gap of the tick itself is therefore never available. PS-7r already reads a tick at small step as `exp(−iεH)` (`TOE_ASSEMBLY.md` line 184).
- *Test 1: C.* It fixes the meaning of words in SMG1's own target, not another part's target. It must not be used to define VC1's vacuum; VC1 keeps its readings E, P and F (`VC1_5.md`).
- *Test 2: P.* The generator is fixed by the certified decomposition. Two decompositions of the same `U` can give different `H_U` (adding `2πP` to a gate's generator, for a projection `P` commuting with it, leaves the gate unchanged). So the reading refers to the law's specified gates, which NN-a already requires ("The factors certify a decomposition of the update").
- *Test 3: C.* It does not settle whether the tick's own dynamics keeps the generator's ground state; that stays FLQ (6.5). It passes while FLQ is kept open and no stationarity claim is drawn from it. An example shows why: for the tick `V L₂L₁ V*` with `V = L₄L₃` (the hop layers and their inverses), R-GEN's generator is `H₀`, because the hop generators cancel in the sum; but `Ψ` is not `α`-invariant for `θ ≠ 0` and generic `τ`, while the exact local generator `V H₀ V*` has the stationary ground state `VΨ`. This is why D5 asks for `α`-invariance separately. An alternative reading, "`U = e^{−iK}` for a finite-range `K` with small local terms, and the state is `K`'s gapped ground state", avoids the example but needs a norm bound as a new constant (test 4); it is recorded, not proposed.
- *Test 4: P.* It uses only the gates' generators, which the law specifies; the bound `‖X_g‖ < π` picks principal logarithms and adds no constant.

**R-LIGHT (D8 with W2.1-W2.4).** Text: the scaling-limit definition of "light sector is one Weyl 16, with every mirror and doubler gapped", as written in section 3.
- *Reason.* The owner's W2 sentence names a light sector; D6-D8 make "light" and "gapped" exact without choosing a vacuum or a gauge field.
- *Test 1: C.* It writes W2's own target exactly. It overlaps CH1's phrase "light spectrum at scales `>> a`" (`TOE_ASSEMBLY.md` line 447) and CH1's inferred definition IR (`CH1.md` section 1, item 8). It passes if adopted together with CH1's reading of "light", not separately.
- *Test 2: P.* Closed: the rescaling powers are existential per operator, and the free reference `S_c` is fixed.
- *Test 3: C.* Clause (W2.1) asks that no `G`-invariant mass exist for the light fields, which forces `G ⊋ G_SM` and makes `ν^c` light by symmetry. Whether `ν^c` is light is a physics question (for example, for neutrino masses). (W2.1) passes only if the owner intends a protected `ν^c`; otherwise (W2.1) should be dropped and the rest stands.
- *Test 4: P.* It uses the cell translations and the tick count already in the law; `Z` and `c` are existential.

**R1-LAW (the rung-1 model).** Text: Definitions 6.1 and 6.1b, as a rung model on five-mode sites, not a law of the framework.
- *Test 1: P.* It is a rung model; it fixes no part's target.
- *Test 2: P.* Its data are definite: `S`, `K = Z₂` (or `S`), the gates, and free constants `τ, τ₅, τ_E, θ`.
- *Test 3: P.* It settles nothing downstream; no live law changes.
- *Test 4: P.* Each piece is needed by its reasons: `S` is the stabilizer group of the Fidkowski-Kitaev vector; `K = Z₂` is the part of both live laws' gauge groups that the rung can keep; `τ₅` freezes the spectator mode, which uniqueness needs; `τ_E` fixes the link state, which uniqueness needs.

**Owner questions arising.** (Q1) Is R-GEN acceptable as the meaning of "gap" for SMG1's rungs? (Q2) Should W2 keep clause (W2.1), that is, should the whole 16 be light by symmetry? Neither is decided here.

## FINISH

**Proved (pass 1, not yet distilled or refereed).**
- The assembly outline of W2: the target theorem with every term defined (section 3), a ladder of six rungs with imports and proof assignments (section 4), and the hard step of each rung with the simplest rung for each of seven tricks (section 5).
- Rung 1, in the generator reading R-GEN, on five-mode sites with `K = Z₂` or `K = S`: Lemma 6.2 (the Hamming stabilizer group); Theorem 6.3 (Fidkowski-Kitaev's on-site spectrum −14 (1), 0 (8), +2 (7), unique `S`-fixed ground vector, re-proved without a computer); Theorem 6.4 (every `S × Z`-symmetric quadratic form has eigenspaces of dimension divisible by 16 on every ring and is gapless on `Z`); Theorem 6.5 (the zero-hop tick is NN-a, gauge invariant, symmetric and cell covariant, and its generator has a unique ground state, pure on the invariant algebra, with gap `min(14τ, τ₅, τ_E)`, in finite and infinite volume); Lemma 6.6 (eight is least for sign-flip symmetries); Proposition 6.7 (no intrinsic Floquet gap); Lemma 6.9 (the reduction of the hopping chain to Fröhlich-Pizzo's form); Proposition 6.10 (gauging all of `S` with exact links).
- With the chain hop, Theorem 6.8 holds on open segments for `|θ| < t₀Δ₀/4` by Fröhlich-Pizzo's Theorem 3.5 [SP]; the reduction and the symmetry conclusions are proved here.

**Counterexamples.**
- Proposition 6.7 refutes the intrinsic reading of "gap" for a tick (a spectral gap of the GNS unitary at the vacuum phase): it fails for the zero-hop rung-1 tick at every step `τ ∈ (0, π/16)`.
- Lemma 6.6 shows that no sign-flip symmetry on two, four or six Majoranas per site both forbids every quadratic and leaves a symmetric operator with a unique ground state.

**Open by name.** R1-H (a native rebuild of the stability step, and its ring and infinite-chain forms); FLQ (the tick's own dynamics for `θ ≠ 0`); R0-U5; R1.5-D; R2; R3-H; R3-D; W2. Owner questions Q1 (R-GEN) and Q2 (clause W2.1). No lemma here failed three attacks; rung 1 closed at a proof in the stated reading.

**What changes downstream.**
- **CH1-i and W2.** Rung 1 is done in the generator reading. The next lanes are R1.5 (decoupling, the simplest rung for the wall's hardest step) and a native rebuild of R1-H.
- **`LIT_SMG.md` lines 200-202.** Its rebuild items "the Clifford identities" and the "exact first excited energy" for the Fidkowski-Kitaev block are done (Theorem 6.3); the "antiunitary action" is not needed, since `S` replaces time reversal; its "weak-hopping stability theorem" is ported [SP], not rebuilt.
- **VC1, CH1, MT1.** Any part that speaks of a tick's gap meets Proposition 6.7. The owner question Q1 is theirs too; R-GEN is scoped to SMG1 until the owner decides.
- **CG1, MT1-ii, FL1, FAM1.** Unchanged. FAM1 still waits for rung 2.
- **Frozen parts.** None changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. No law, reading or working-set entry is adopted.
