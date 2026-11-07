lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CG1-16-S: a site-count change around the 16 (route 1), pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of the TOE assembly (part CG1, item CG1-16-S, route 1 of #10027) under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. Every rule below is a candidate for the owner. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. One scratch computation was run, marked `[check]` in section 4.3: `/tmp/toe-CG16S/check_F.py` (numpy, floating point, 2.4 s, 27 MB peak), started after `memory_pressure` reported 55 percent free (two earlier readings were 44 percent, below the threshold). A check guides; it proves nothing. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local `claude/toe-assembly` (this checkout, HEAD) | `15bc39079b` |
| `origin/main` | `f5af11cd01` |
| `origin/docs/consolidate-gauge-matter-registers` (#10027 note and the consolidation) | `7086189d10` |
| `origin/claude/toe-site-count-matter-20261021` (#10038 source branch) | `5adea19dc2` |
| `origin/claude/scale-ladder-lane-theorems-20261018` (B3 note last changed `8f65d826b`) | `89d8e59561` |

Other branches were read only with `git fetch -q origin <branch>` and `git show origin/<branch>:<path>`. Files read, by line.
- This folder: `prior/CG16S.md` 1-81 (all); `TOE_ASSEMBLY.md` 14-23, 120-135 (PS-5, PS-6), 195-260 (sections 3.4-3.8), 378-393 (MT1), 436-456 (CG1); `LW1_5.md` 1-215 (status, definitions, both laws, C-C2, M, Q, G, R, U, S′, alternative A, F and K, mixed registers, the one-ended construction, Theorem SC, SC.1, Σ, the reducible-register correction, S1-S4); `LW1.md` 36-60 (definitions) and 401-404 (Theorem E1); `TM1.md` 1-60; `LZ1.md` 1-66; `ZM1.md` 5, 18, 49-72 (Definition Z, (G1), (G2)), 311-325 (Theorems Z4, Z3); `RCS1.md` 8, 12, 64 (Theorem 4).
- Branch `docs/consolidate-gauge-matter-registers`: `docs/SPIN10_MOTT_SITES_CARRY_NO_COMPOSITE_SIXTEEN_THE_CENTRE_FIXES_EVERY_FERMION_TO_THE_VECTOR_CLASS_BOUNDED_THEOREM_NOTE_2026-10-22.md` 1-179 (all; the routes are lines 126-140 at this commit); `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` 1-12, 1130-1145 (line 1139 is the #10027-routes entry), 1190-1205 (line 1202 is #10038, line 1204 is #10045).
- Branch `claude/toe-site-count-matter-20261021`: `docs/A_SITE_COUNT_CHANGE_BY_ONE_CARRIES_THE_SPIN10_SPINOR_SO_UNDER_THE_ODD_SITE_RULE_EVERY_FERMION_IS_A_MOBILE_SITE_DEFECT_WHILE_ITS_CONES_STAY_VECTOR_LIKE_BOUNDED_THEOREM_NOTE_2026-10-22.md` 1-224 (all).
- `origin/main`: `docs/CANDIDATE_LAWS.md` 20-34; `docs/CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md` 1-69 (all); `docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md` 1-40.
- Branch `claude/scale-ladder-lane-theorems-20261018`: `.claude/science/physics-loops/scale-ladder-campaign-20261018/B3_formation_coding_radius/DRAFT_NOTE.md` 50-53 and 231-233, found by grep for "hole" and "remov".

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The Lattice axiom is read plainly. The site-count rules of section 3 are written as specifications, four-tested, and left to the owner.

**Working set used, by name.** PS-5 (five modes per site), PS-6 and PS-6r (local frames, finite link registers), PS-1c (cell covariance under `𝒢 = 2Z³ ⋊ O_{c₀}`), GA1-P-NN = NN-a (owner, 2026-11-06), PS-7r (only its sentence that the gauged vacuum is VC1's), the Record axiom (section 5 only), and the proposed, unadopted PS-3g and PS-3h5 (section 5 only). Results used, by name: `LW1.md` E1; `LW1_5.md` C2, F and K, the mixed-register paragraph, Theorem SC; `LZ1.md` section 1 (centre implementers, D1 states, bands) and Theorems 2.1-2.2; `RCS1.md` Theorem 4; `ZM1.md` Definition Z, (G1) and Theorem Z4; `TM1.md` Definitions 3-6 and Theorems 3-5. From the consolidation, as supplied-model results: #10027 part B and #10038 parts A, B, D, E. Each is quoted where used.

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the spectral theorem in finite dimension, Schur's lemma, Stokes' theorem on manifolds with boundary, the homotopy formula for closed forms, Chern-Weil for projector bundles over a closed surface, unique factorization in `C[z₁^{±1}, z₂^{±1}]`. Published work is used as a guide and credited in section 1; no step rests on a citation.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 453, CG1(e): "the spinor 16 rather than the vector 10 (#10027; the #10126 synthesis lists three escapes: "a site-count change, deconfined spinons outside the finite-site theorem, or a Spin(10) not generated by site bilinears")."

#10027, route 1 (note lines 128-131): "Site count is not fixed. An excitation that adds or removes one five-mode site carries centre (-i)^{+-1}, which is spinor class. [...] A "moving site/vacancy" 16 needs the Z^3 / permanent-site axiom to bend (records creating or removing sites; compare the scale-ladder "removed sites" lane). UNTESTED."

The consolidation, line 1139: "Route 1 is tested in #10038 (logged), which bends the Lattice axiom: a site-count change is spinor class for either content parity, so spinor bosons occur; a fermionic 16 also needs the supplied odd-site rule, and the defect cones stay vector-like." Line 1202 (#10038, part D): "An invariant staggered on-point energy gaps them all, so the cones are vector-like (16_L + 16_R)."

The lane brief gives three targets.
1. State the minimal site-count rule as a law in LW1 form (covariant, local, finite registers, NN-a), four-test it, and compare it with the repository's removed-site work.
2. Prove or refute that its defect band is chiral. Either some admissible law gives a single light Weyl 16 without its mirror, or the cones stay vector-like for every law of the class. Name the step.
3. Say what the rule costs TM1, LZ1 and ZM1.

**The lattice axiom, as quoted in `TOE_ASSEMBLY.md` line 16.** "Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site." **PS-5, line 205.** "Each site has the possibilities of five fermion modes; its full algebra is `Cl(10)`, presented as `M_32(C)`."

## 0.1 Outcome in one paragraph

**Proved, with two counterexamples; no part stops at an open lemma.** (1) In LW1 form a changing site count is a point register `V_x = C|∅⟩ ⊕ ΛC⁵` (Lemma 3.1). Whether this bends the Lattice axiom or PS-5's `M_32(C)` is a reading (Observation 3.1). The minimal rule **SC-min** passes tests 1-3 and is conditional on test 4. The odd-site rule **SC-odd**, which a fermionic 16 needs (Proposition 3.6(a), Corollary 3.3), fails tests 1 and 3. Sites move only on end-mixed link registers: on end-pure registers, including `L5-O`'s `S_+`, every occupation is conserved (Proposition 3.4); Proposition 3.5 gives a register that moves them, dragging a string of links. None of the repository's removed-site work (CL-2's graph holes, the split cascade, the scale-ladder holes, record vacancies) supplies a mobile site defect. (2) **The defect band is not chiral.** In the class itself (gauge links, NN-a; for the Spin(10) frame under SC-odd with link-pure registers), every odd defect band in every D1 state is flat (Theorem 4.2, extending `LZ1.md` Theorems 2.1-2.2). The site moves, but its centre pattern does not. So a D1 vacuum has no light Weyl 16, chiral or not. In the free reading (global Spin(10), #10038's setting), the one-site walk over the empty lattice is a finite-depth circuit, so its three-dimensional winding vanishes (Theorem H). A Nielsen-Ninomiya theorem for a tick (Theorem F, a native proof of the class-A case of Bessho-Sato Eq. (15)) turns zero winding into zero net chirality at quasienergy 0. So for every law of the free reading, the light 16 nodes of the one-site walk pair with their mirrors (Theorem 4.5). The step: a finite-depth circuit is null-homotopic, and parity with Schur's lemma puts the whole 16 in one block. **Counterexamples:** under SC-min a gauge-invariant local fermion exists, a 16-16bar singlet pair (Proposition 4.2.3), so `RCS1.md` Theorem 4 and `LZ1.md`'s centre identity need SC-odd for site-count laws; and with gauge links a single site can be created gauge-invariantly (Proposition 3.6(c)), so #10038 A7's `dn ≡ 0 mod 4` holds only without links. (3) **Costs.** TM1: its Theorems 1-5 carry over (Proposition 5.2), but records and moving sites conflict: under L-point a recorded point's occupation is frozen (Proposition 5.3), so in a vacuum where every point records (TM1's case (E)) a local defect never leaves a bounded region (Corollary 5.3.1); and L-site needs site names the law does not have. LZ1: no gain in D1 vacua; a broken identity under SC-min; defect patterns join LZ1-SC's static class. ZM1: (G1) forces all four centre classes at a coarse site (Proposition 5.4), and under SC-min the ZM1-I1[a] class contains gauge-invariant fermions.

## 1. Literature

Searched 2026-11-06 with WebSearch (standard and extended) for: Floquet Nielsen-Ninomiya theorems; Weyl quantum cellular automata and fermion doubling; unpaired Weyl points and three-dimensional winding numbers; index theory of quantum walks; symmetric matrix-product unitaries; flat Chern bands with strictly local hopping; reversible graph dynamics with vertex creation; lattice definitions of the Spin(10) 16. Each arXiv abstract page below was fetched; the fetch tool returns short quotations only. No citation carries a proof step.

| Work | Fetched | What it says, by number | Use here |
|---|---|---|---|
| T. Bessho, M. Sato, arXiv:2006.04204, PRL 127, 196404 (2021) | abstract and ar5iv text | Theorem 2, Eq. (8): `w₃ = Σ_{Im E>0} Ch = −Σ_{Im E<0} Ch` for non-Hermitian `H`; Eq. (9): "w₃ = −(1/24π²)∫ tr[H⁻¹dH]³"; Eq. (12): "H(k) = iU_F(k)"; Theorem 3′, Eq. (15): `n = Σ_{ε_α=μ} ν^μ_α`, where "α labels the Fermi surfaces defined by ϵ=μ" | Theorem F (section 4.3) is a native proof of the class-A, three-dimensional case of Eq. (15) at `μ = 0` for isolated nodes |
| X.-Q. Sun, M. Xiao, T. Bzdušek, S.-C. Zhang, S. Fan, arXiv:1806.09296, PRL 121, 196401 (2018) | abstract | "there is an equal number of right-handed and left-handed Weyl points in 3D Floquet lattice"; in the adiabatic limit a low-energy subspace can carry one-handed points, with imbalance "twice the winding number of the Floquet operator" of that subspace | Remark 4.3.3: the imbalance sits in a subspace that no exact symmetry protects; Theorem H shows why the full operator has `W₃ = 0` |
| S. Higashikawa, M. Nakagawa, M. Ueda, arXiv:1806.06868, PRL 123, 066403 (2019) | abstract | a single Weyl fermion "is prohibited in static lattice systems by the Nielsen-Ninomiya theorem"; it is realized by a "topologically nontrivial Floquet unitary operator" | Theorem H: such an operator is not a finite-depth circuit of local gates, so LW1 form excludes it |
| G. M. D'Ariano, P. Perinotti, arXiv:1306.1934, PRA 90, 062106 (2014) | abstract | the Dirac equation emerges from the large-scale dynamics of a unitary, local, homogeneous, isotropic quantum cellular automaton | context only; its explicit automaton is not used |
| D. Bakircioglu, P. Arnault, P. Arrighi, arXiv:2505.07900 (v3, 17 Jan 2026) | abstract | they "demonstrate the existence of FD issues in QCAs"; a covering-map fix "does not break the chiral symmetry of the massless scheme" | context; the fix is not examined here |
| D. Gross, V. Nesme, H. Vogts, R. F. Werner, arXiv:0910.3675, CMP 310, 419-454 (2012) | abstract | an integer index for one-dimensional walks; trivial index exactly when the walk is realized by partitioned unitaries; shifts are the prototypes of nontrivial index | the one-dimensional analogue of Lemma W (section 4.6) |
| Z. Gong, C. Sünderhauf, N. Schuch, J. I. Cirac, arXiv:1812.09183, PRL 124, 100402 (2020) | abstract | matrix-product unitaries with on-site symmetries are "completely classified by the (chiral) index and the cohomology class of the symmetry group"; symmetry-protected indices "quantify the imbalance in the transport associated to each group element" | motivates Proposition 4.6.1: a symmetric walk built from non-symmetric gates can carry per-sector indices |
| L. Chen, T. Mazaheri, A. Seidel, X. Tang, arXiv:1311.4956, J. Phys. A 47, 152001 (2014) | abstract | exact flatness, nonzero Chern number and strictly local hopping are "not possible to simultaneously satisfy all three"; one band by "a rather elementary proof", several by K-theory | Lemma U (section 4.6) is a native argument of the same kind |
| J. Dubail, N. Read, arXiv:1307.7726, PRB 92, 205307 (2015) | abstract | "sets of compactly-supported Wannier-type functions do not exist for band structures in this class" | same as above |
| P. Arrighi, A. Durbec, A. Emmanuel, arXiv:1805.10330 (v4, 10 Jul 2026) | abstract | earlier formalisms answered negatively ("nodes cannot be destroyed without jeopardising bijectivity"); reversible local creation and destruction is possible in three relaxed, equivalent settings | section 3.1: in the operator-algebra law form a site is created by changing a point register, so the named-vertex obstruction does not arise |
| P. Arrighi, S. Martiel, S. Perdrix, arXiv:1502.04368 | abstract | reversibility added to causal graph dynamics | the vertex-preservation theorem in its title is NOT VERIFIED (not on the abstract page) |
| J. Wang, X.-G. Wen, arXiv:1809.11171, PRR 2, 023356 (2020) | abstract | Spin(10) chiral fermion theories with 16-dimensional Weyl spinors "can be defined on a 3+1D lattice, and subsequently dynamically gauged"; the argument rests on cobordism classification and on "the existence of symmetric gapped boundary for the trivial symmetric invertible topological orders" | a lattice model with supplied 16-component fields and interactions, not a site-count law; not tested here |

**NOT VERIFIED (not fetched; named only as context).** H. B. Nielsen, M. Ninomiya, Nucl. Phys. B185, 20 (1981), B193, 173 (1981), Phys. Lett. B105, 219 (1981). D. Friedan, Commun. Math. Phys. 85, 481-490 (1982) (title and venue confirmed by search only). A. A. Suslin (1977) on `SL_n` over polynomial rings; R. G. Swan (1978) on projective modules over Laurent polynomial rings; H. Bass, A. Heller, R. G. Swan (1964); M. F. Atiyah, R. Bott, Acta Math. 112 (1964); A. Pressley, G. Segal, *Loop Groups* (1986). Section 4.6 names the last five only as published routes to the open Lemma W.

## 2. Prior work used

Paths: **G** = `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` on `origin/docs/consolidate-gauge-matter-registers`; **N27** = the #10027 note on the same branch; **N38** = the #10038 note on `origin/claude/toe-site-count-matter-20261021`; **T** = this folder.

| Prior result | Path, line | Status at source | How used |
|---|---|---|---|
| #10027 B: on a fixed site set, `exp(2πi M_01) = (-1)^{n_sites}` and `z = (-1)^F (-i)^{n_sites}` | N27 69-73 | supplied model, exact | ported and rebuilt with a vacancy state in Lemma 3.2 |
| #10038 A2-A4: `z = (-1)^F (-i)^{N_s}`; a defect is spinor class iff `dn` is odd; under the odd-site rule `z = i^{N_s}` and `(-1)^F = (-1)^{N_s}` | N38 62-71 | logged, supplied model | rebuilt in Lemma 3.2 and Corollary 3.3 |
| #10038 A5: "The odd rule is therefore the one parity choice that makes the defect spinors fermions. This is a reason for the choice, not a fitted value." | N38 72-74 | logged | test 1 of SC-odd (section 3.4) |
| #10038 A6: the invariant one-mode hop "never stays in the odd-odd sector" | N38 75-77 | logged | cost of SC-odd (section 3.4) |
| #10038 A7/C0: covariant creation needs `dn = 0 mod 4` | N38 78-84 | logged | extended: with gauge links, Proposition 3.6 |
| #10038 B1-B3: the whole-content transfer is local, Spin(10)-covariant, fermionic; only `Z₂` link phases are covariant | N38 86-93 | logged | the transfer gate of section 3.3 |
| #10038 D1-D2: polarized-background defect band; a staggered energy gaps all cones, "16_L + 16_R" | N38 112-118 | logged, finite toy | extended to a theorem for every symmetric free defect walk (Theorem 4.5) |
| #10038 E1: whole-cube splits add 56 sites per even cube, centre-neutral | N38 123-127 | logged | section 3.5 comparison |
| #10038's record sentence: "a record must travel with its site's content. Whether "permanent" survives a moving site is OPEN." | N38 181 | logged | section 5.1 |
| #10027 and #10038 routes and narrowing | G 1139, G 1202 | author consolidation, "author statements for review" (G 11) | section 0 |
| `LW1_5.md` C2 (fixed site algebras), F and K, mixed registers, Theorem SC | T/LW1_5.md 108-119, 171-202 | FROZEN | Lemma 3.2, Proposition 3.6, section 4.2 |
| `LW1_5.md` alternative A: "PS-6 alone does not select `SO(10)` or `U(5)`" | T/LW1_5.md 161-167 | FROZEN | section 3.4, test 4 |
| `LZ1.md` section 1 (centre implementers `c_z`, D1 states, bands) and Theorems 2.1-2.2 (pinned patterns, flat nodes) | T/LZ1.md 32-64 | FROZEN | Theorem 4.2 extends both to site-count laws |
| `RCS1.md` Theorem 4: "Every `A∈𝔄^G` is matter-even." | T/RCS1.md 64 | FROZEN | Proposition 4.2.3 shows it fails for one site-count register |
| `ZM1.md` Definition Z, (G1), Theorem Z4 | T/ZM1.md 49-72, 311 | FROZEN | section 5.3 |
| `TM1.md` Definitions 3-6, Theorems 3-5 | T/TM1.md 22-60 | FROZEN | section 5.1 |
| `LW1.md` E1 (quasi-local update, finite-depth layers) | T/LW1.md 401 | FROZEN | Lemma 4.4.1 |

**Prior work the digest missed.**
- `origin/main:docs/CANDIDATE_LAWS.md` line 25, the record-removal clause CL-2: "When a record forms, its qubit leaves the flow: the network is permanently short that site's share." Its companion `docs/CANDIDATE_LAW_CL2_A_RECORDS_QUBIT_LEAVES_THE_FLOW_EVIDENCE_BOUNDED_THEOREM_NOTE_2026-10-18.md` treats removed sites as graph holes: "For the separate graph-hole problem, delete the hole vertices and edges incident on them." This is the repository's removed-site rule. Section 3.5 compares it.
- `origin/main:docs/FAST_VACANCY_MOTION_AFTER_FORMATION_BOUNDED_THEOREM_NOTE_2026-09-24.md`: there a vacancy is a site with no record ("its only vacancy at B site 3"); the site count is fixed. #10038 line 215 already set these notes aside.
- Scale-ladder campaign, B3 draft note, lines 52 and 232 (branch `claude/scale-ladder-lane-theorems-20261018`): "hole-emitting rules, where the hole is an output symbol that later neighbours may read or ignore"; "Conditioning on hole-free completion turns rejection rules into static pair measures". A hole there is a formation output, not a missing site. No scale-ladder file on that branch removes or creates sites; the grep for "remov" found none.
- `LZ1.md` Theorems 2.1-2.2 bear directly on route 1. The digest lists `RCS1.md` Theorem 4 but not these two.

**Failed attempts on file, not repeated.** Promoting the Fock 16 to a cone multiplet (G 827); Mott composites on fixed sites (G 1036, G 1079); site-count motion as the whole chiral solution (G 1202: "An invariant staggered on-point energy gaps them all"). Section 4 does not rerun the last one. It proves why it fails for every symmetric free walk and asks what remains.

## 3. Target (1): the minimal site-count rule in LW1 form

### 3.1 Sites that may be absent are point registers

A law in LW1 form acts on one fixed quasi-local algebra (`LW1.md` line 52: "The quasi-local algebra `𝔄` is the norm completion of the finite matter-and-link algebras"). Its tick is an automorphism of that algebra (E1). The algebra cannot gain or lose tensor factors in time. So a changing set of sites must be written on a fixed index set.

**Definition 3.1 (point register).** For `x ∈ Z³` put `V_x = C|∅⟩_x ⊕ F_x`, where `F_x = ΛC⁵` is the five-mode Fock space of PS-5. The empty state `|∅⟩_x` is even. The occupation of `x` is `o_x = 1 − |∅⟩⟨∅|_x`. The grading of `V_x` is `P_x = |∅⟩⟨∅|_x + (−1)^{N_x} o_x`. Matter operators of distinct points graded-commute. The odd variant is `V_x^− = C|∅⟩_x ⊕ Λ^{odd}C⁵`, of dimension 17. A site frame acts on `F_x` as in `LW1_5.md` section 3 and fixes `|∅⟩_x`. The Spin(10) generators are `M_x^{ab} = o_x (i/2)γ_{x,a}γ_{x,b} o_x`. They vanish on `|∅⟩`.

**Lemma 3.1 (encoding).** For a finite set `Λ`, the space of configurations "a subset `S ⊆ Λ` of present sites, each with content in `F`" is `⊕_{S⊆Λ} ⊗̂_{x∈S} F_x`. It is canonically isomorphic, as a graded space with its site-frame actions, to `⊗̂_{x∈Λ} V_x`.

*Proof.* Expand `⊗̂_{x∈Λ}(C|∅⟩_x ⊕ F_x)` by distributivity. The summand indexed by `S` is `⊗̂_{x∈S}F_x ⊗ ⊗_{x∉S}|∅⟩_x`. The empty factors are even, so they add no signs. Frames act factorwise on both sides. ∎

So "sites created or removed" with at most one site per point is a law on point registers. Interstitials (two sites at one point) need a larger register; the minimal rule omits them. Arrighi, Durbec and Emmanuel (arXiv:1805.10330) record that, for reversible graph dynamics with named vertices, "nodes cannot be destroyed without jeopardising bijectivity". In Lemma 3.1's form a point keeps its name and only its state changes. Unitarity then forces only this: a gate that empties a point must move the content to other factors in its support.

**Observation 3.1 (where the bend sits).** Lemma 3.1 gives one mathematics under two readings. Reading R-site: "a physical site is an occupied point"; then the Lattice axiom is bent. Reading R-point: "every point is a site with possibilities `|∅⟩ ⊕ ΛC⁵`"; then the Lattice axiom holds and PS-5's sentence "its full algebra is `Cl(10)`, presented as `M_32(C)`" is bent, since `End(V_x) = M_33(C)`. Which text bends is a reading for the owner. Nothing below depends on it.

### 3.2 Centre algebra with empty points

**Lemma 3.2.** On `V_x` put `ω_x^{mat} = exp(iπ Σ_{j=1}^5 M_x^{2j−1,2j})` and `z_x^{mat} = exp(2πi M_x^{12})`.
(a) `z_x^{mat} = (−1)^{o_x}`.
(b) `ω_x^{mat} = |∅⟩⟨∅|_x − i(−1)^{N_x} o_x`.
(c) For finite `Λ`, `∏_{x∈Λ} ω_x^{mat} = (−i)^{N_s(Λ)}(−1)^{F(Λ)}`, with `N_s(Λ) = Σ_{x∈Λ} o_x` and `F(Λ) = Σ_{x∈Λ} N_x`.
(d) Let `A` be a matter operator supported in `Λ` that changes `N_s(Λ)` by `Δn` and has parity `θ(A) = ±1`. Then `Ad(∏_{x∈Λ} ω_x^{mat})(A) = (−i)^{Δn} θ(A) A`.
(e) On `V_x^−`: `ω_x^{mat} = |∅⟩⟨∅|_x + i o_x`, `z_x^{mat} = (−1)^{o_x} = (−1)^{N_x}`, and every homogeneous matter operator has `θ(A) = (−1)^{Δn}`.

*Proof.* On `F_x`, `M^{2j−1,2j} = n_j − 1/2` (`LW1_5.md` section 1). So `exp(iπ(n_j − 1/2)) = −i(−1)^{n_j}` and the product over five modes is `(−i)⁵(−1)^{N} = −i(−1)^N`. Also `exp(2πi(n_1 − 1/2)) = −1`. On `|∅⟩` every generator is zero, so both exponentials are 1. This gives (a) and (b). For (c), the factors commute and act pointwise; multiply. For (d), `A` maps the eigenspace of `(N_s(Λ), (−1)^{F(Λ)})` with values `(n, ε)` into the one with `(n + Δn, θε)`. So conjugation by (c) multiplies `A` by `(−i)^{Δn}θ`. For (e), `N_x` is odd on `Λ^{odd}`, so `(−1)^{N_x} = −1 = (−1)^{o_x}` there and `+1` on `|∅⟩`. Hence `θ(A) = (−1)^{Δn}`. ∎

**Corollary 3.3 (route 1, rebuilt).** Call a homogeneous matter operator *spinor class at `x`* if `Ad ω_x^{mat}` has eigenvalue `±i` on it, and *tensor class* if `±1`.
(i) An operator that fills or empties one point is spinor class there, for either content parity. So spinor-class bosons occur under `V_x` (#10038 A3).
(ii) Under `V_x^−`, the element `−1 ∈ Spin(10)` acts on every point as local fermion parity. An operator is odd exactly when it changes the site count by an odd number. A filled point is the 16-dimensional `Λ^{odd}`, and an emptied one carries the conjugate class (#10038 A4).

*Proof.* (i) `Ad ω_x^{mat}(|s⟩⟨∅|_x) = −i(−1)^{N_s}|s⟩⟨∅|_x` by Lemma 3.2(b). (ii) Lemma 3.2(e). ∎

### 3.3 The candidate rules

Both texts below are proposals for the owner. Neither is adopted.

> **SC-min.** "Each point of `Z³` holds at most one site. The register of a point is an even empty state together with the five-mode Fock space of PS-5; every site frame fixes the empty state. The law is in LW1 form on these registers: GA1-P-NN with `F_x` replaced by `V_x`, covariance under `𝒢 = 2Z³ ⋊ O_{c₀}`, gauge invariance of the complete update, and finite link registers on which the frame group acts at each end."

> **SC-odd.** "As SC-min, and a present site holds an odd number of fermions: the register is `C|∅⟩ ⊕ Λ^{odd}C⁵`."

The LW1-form clauses are the existing ones. A gate is a unitary on `V_x ⊗̂ V_y ⊗ H_ℓ`, even, acting as the identity elsewhere; a layer is a locally finite product of such gates on disjoint triples; the update has finitely many layers; it commutes with each gauge transformation `exp(i𝒢_x^T)`, `𝒢_x^T = o_x(matter generator)o_x + Σ_{ℓ∋x}(end generator)`, and with each cell lift.

**Proposition 3.4 (end-pure registers freeze the sites).** Take a Spin(10)-type law under SC-min or SC-odd. Suppose every link register is end-pure: the lift of `−1 ∈ Spin(10)` at each end acts on it as a scalar. Then every `o_x` is conserved by every gauge-invariant gate. No site moves, appears or disappears. This covers the specified register `S_+` of `L5-O`.

*Proof.* Put `z_x = exp(2πi𝒢_x^{12})`. As in `LW1_5.md` Theorem SC(a), `z_x` is a product of commuting unitaries: the matter factor `z_x^{mat} = (−1)^{o_x}` (Lemma 3.2(a)) and the six end factors `ε_{ℓ,x}`. Each gate commutes with `𝒢_x^{12}`, hence with `z_x`. End-purity makes each `ε_{ℓ,x}` a scalar `±1`. So `(−1)^{o_x}` is a scalar multiple of `z_x` and commutes with every gate. Since `o_x ∈ {0, 1}`, `o_x = (1 − (−1)^{o_x})/2` commutes too. For `S_+`: `LW1_5.md` S1-S4 decomposes it into endpoint factors ("`S_+` into paired half-spin factors"), so at each end every summand is a half-spin module, on which `−1` acts as `−1`; and Σ lists it among the end-pure registers ("This includes one uniform irreducible `S_+` or vector register"). ∎

**Proposition 3.5 (a register that moves sites).** Let `R_ℓ = C|r₀⟩ ⊕ (S_+ ⊗ S_+^*) ⊕ (S_− ⊗ S_−^*)`, where `F = ΛC⁵ = S_+ ⊕ S_−` is the 32-dimensional Clifford module, `Spin(10)_x` acts on the factors `S_σ`, `Spin(10)_y` acts on the factors `S_σ^*`, and both act trivially on `|r₀⟩`. Fix orthonormal bases `B_±` of `S_±` and write `e_s` for the same vectors in the link factor `F`. For `σ = ±` put
`T_ℓ^σ = (1/4) Σ_{s∈B_σ} Σ_{s′∈B_σ} (|∅⟩⟨s|)_x ⊗̂ (|s′⟩⟨∅|)_y ⊗ |e_s ⊗ e_{s′}^*⟩⟨r₀|`,
and `h_ℓ = Σ_σ (T_ℓ^σ + T_ℓ^{σ†})` (under SC-odd keep only `σ = −` and the summand `S_− ⊗ S_−^*`). Then `h_ℓ` is even and commutes with every gauge generator at `x` and at `y`. Each `T_ℓ^σ` is an isometry from `S_σ ⊗ |∅⟩_y ⊗ |r₀⟩` into `|∅⟩_x ⊗ S_σ ⊗ (S_σ ⊗ S_σ^*)`, and `exp(−i(π/2)h_ℓ)` empties `x`, fills `y` and moves the link off `|r₀⟩`.

*Proof.* Each term moves content of one parity from `x` to `y`, so it preserves total fermion parity: `h_ℓ` is even. Under `u ∈ Spin(10)_x`, which preserves `S_σ`, `(|∅⟩⟨s|)_x ↦ Σ_t \bar u_{ts}(|∅⟩⟨t|)_x` and `e_s ↦ Σ_t u_{ts}e_t`. Unitarity, `Σ_s \bar u_{ts}u_{t′s} = δ_{tt′}`, makes the contraction over `s` invariant. The contraction over `s′` is invariant under `Spin(10)_y` in the same way, with `S_σ^*` carrying the contragredient action. Other points and links are untouched. Differentiating gives commutation with the generators. Isometry: `T_ℓ^σ` sends `|s⟩_x|∅⟩_y|r₀⟩` to `(1/4)Σ_{s′}|∅⟩_x|s′⟩_y|e_s ⊗ e_{s′}^*⟩`, of norm `(1/4)·16^{1/2} = 1`, and distinct `s` give orthogonal images. So `T^σ` is a partial isometry, `h_ℓ` acts on each two-dimensional span `{v, T^σ v}` as `σ_x`, and the stated gate exchanges them up to the phase `−i`. ∎

The link of Proposition 3.5 is end-mixed: at `x` the lift of `−1` is `+1` on `|r₀⟩` and `−1` on `S_σ ⊗ S_σ^*`. A moved site leaves a string of such links behind it, back to the emptied point. This is the Gauss law of a Spin(10)-charged object. The string carries the spinor class that `z_x` conservation demands.

**Proposition 3.6 (how many sites a gate may add).**
(a) Under SC-odd every even operator changes `N_s` by an even number. So site-count parity equals fermion parity, and every law in the class conserves it.
(b) An even matter operator that commutes with `∏_{x∈Λ} ω_x^{mat}` has `Δn ≡ 0 mod 4`. This holds for every even matter operator invariant under a global Spin(10) (#10038 A7/C0, rebuilt).
(c) Under SC-min, with a link register `R = C|r₀⟩ ⊕ F` on which `Spin(10)_x` acts on `F` and `Spin(10)_y` trivially, the operator `Σ_{s∈B_+} (|s⟩⟨∅|)_x ⊗ |r₀⟩⟨e_s|` is even, gauge invariant, and has `Δn = +1`.

*Proof.* (a) Lemma 3.2(e): `θ(A) = (−1)^{Δn}`, and `θ = +1`. (b) Lemma 3.2(d) gives the factor `(−i)^{Δn}θ = (−i)^{Δn}`, which must be 1. The element `∏ω_x^{mat}` is the image of a global Spin(10) element, so global invariance implies commutation. (c) The matter factor is even since `B_+ ⊂ S_+`. The contraction over `s` is invariant under `Spin(10)_x` as in Proposition 3.5; nothing else acts. ∎

### 3.4 Four tests

Test 1 fails a text that states or fixes a part's target. Test 2 fails an open-ended text. Test 3 fails a text that settles a downstream physics question by premise. Test 4 fails a text that adds structure or constants its own reasons do not need. P = pass, C = conditional, F = fail.

| Rule | 1 | 2 | 3 | 4 | Reasons |
|---|---|---|---|---|---|
| SC-min | P | P | P | C | 1: it names no species, group or chirality; Corollary 3.3(i) shows it gives spinor-class bosons as readily as fermions, so it is not tuned to the 16. 2: the register and the law form are fixed; the link register is as open as PS-6r already is, and no more. 3: it settles no downstream question; whether any defect propagates is section 4's question. 4: the empty state is exactly what a changing site count needs; but by Proposition 3.4 the rule does nothing on end-pure registers, so it works only with an end-mixed register such as Proposition 3.5's, which its reason (motion) does need. |
| SC-odd | F | P | F | C | 1: its stated reason is the target. #10038 A5: "The odd rule is therefore the one parity choice that makes the defect spinors fermions." 3: by Corollary 3.3(ii) every fermion is then a site defect; this settles MT1(a)(1)'s statistics and CG1(e)'s "16 rather than 10" for defects by premise, and by #10038 A6 it removes the one-mode hop that LW1-5's laws use. 4: it removes the even half of `ΛC⁵`, against PS-5's `M_32(C)`. |

The verdicts are proposals. The owner decides.

**What SC-min alone gives.** By Corollary 3.3(i), a filled or emptied point is spinor class for either content parity. By Proposition 3.6(a)-(b), SC-min does not tie fermion parity to site count. So SC-min does not make the defect a fermionic 16. The tie needs SC-odd, which fails tests 1 and 3. This is the precise form of the consolidation's sentence at G 1139: "a fermionic 16 also needs the supplied odd-site rule".

**The `L5-U` frame.** Under `U(5)` frames the empty state `|∅⟩` and the empty site `|0⟩ ∈ Λ⁰` carry the same representation (the trivial one, charge 0). So `|∅⟩⟨0|_x + h.c.` is a frame-invariant even gate: a site with no fermions can appear or vanish with no link change. Under `U(5)` the site count is not a gauge charge, and the 16 is not a frame multiplet. `Λ^{odd}C⁵ = Λ¹ ⊕ Λ³ ⊕ Λ⁵` carries the `SU(5)` types `5`, `10bar`, `1` at `N = 1, 3, 5`; these are three gauge representations, not one. The rest of this file therefore treats the Spin(10) frame of `L5-O`, where route 1 is posed.

### 3.5 Comparison with the removed-site work in the repository

| Work | What is removed or added | Does a defect move? | Relation to SC-min |
|---|---|---|---|
| CL-2, `origin/main:docs/CANDIDATE_LAWS.md` line 25: "When a record forms, its qubit leaves the flow: the network is permanently short that site's share." Evidence note (2026-10-18): "delete the hole vertices and edges incident on them." | a recorded site leaves the dynamics, permanently | no: holes only accumulate | A CL-2 hole is a frozen point, not an empty one. Its record is permanent. Any centre class it carries is static: holes never move, so they form no band. CL-2 never creates sites. |
| #10038 E1 and the register's split ("adding 7 sites per parent site", "56 per even cube") | sites added in whole cubes | not by itself | `Δn = 56 ≡ 0 mod 4`, so `i^{56} = 1` under SC-odd: growth is centre-neutral and makes no net 16 (Proposition 3.6(b) is the general form). |
| Scale-ladder B3 note, lines 52, 232: "hole-emitting rules, where the hole is an output symbol"; "Conditioning on hole-free completion" | nothing: a hole is a formation output | no | no site-count change; a hole is a record symbol. |
| Main, 2026-09-24 vacancy notes ("its only vacancy at B site 3") | nothing: a vacancy is a site with no record | yes, as a record vacancy | fixed site count; #10038 line 215 already set them aside. |

None of these supplies a mobile site defect. SC-min with Proposition 3.5's register is, as far as the search found, the repository's first site-count rule in LW1 form with gauge-invariant motion.

## 4. Target (2): is the defect band chiral?

### 4.1 Two settings

**(G), the class itself.** Site-count laws of section 3.3 with link registers, gauge invariant as a whole (NN-a). Bands are read as in `LZ1.md` section 1 (reading R-loc): a band is `(d, F, V)` with an isometry `F: L²(T³; C^d) → H` intertwining translations and the tick, in the GNS space of a **D1 state** ("stationary, even-translation invariant and invariant under each `Ad c_z`. Local gauge invariance implies the last property", `LZ1.md` line 40).

**(F), the free reading.** Matter-only laws on point registers, with no link registers: a finite product of nearest-neighbour layers of even gates on `V_x ⊗̂ V_y`, covariant under `𝒢`, whose complete update commutes with a global Spin(10) acting on `F_x` and fixing `|∅⟩`. Gates need not commute with Spin(10). #10038's model is in this class (its B2: "The transfer is local (one bond) and Spin(10)-covariant"). This reading is auxiliary, like `LW1_5.md`'s free tick ("an auxiliary c-number replacement of link operators").

### 4.2 Setting (G): every odd defect band is flat

`LZ1.md` section 1 defines local centre implementers `c_z` and uses one identity (line 38): "On a local operator `A`, the product of their adjoint actions over a finite set containing all matter sites and both ends of all links in its support equals matter parity `θ`". With empty points this identity changes (Lemma 3.2(d)). The repair below needs SC-odd for the Spin(10) frame.

Call a link register **link-pure** if the product of the two end lifts of `−1 ∈ Spin(10)`, and the product of the two end factors of `ω`, act on it as scalars. Every irreducible `Spin(20)` register is link-pure. The product of the two end factors of `ω` is the lift of `−I_20`, and `LW1_5.md` line 208 says of it: "the lift is central in `Spin(20)`, so Schur's lemma makes it a scalar". The product of the two end lifts of `−1` is the image of `(−1, −1)` under `Spin(10) × Spin(10) → Spin(20)`, which is the identity. Proposition 3.5's register is link-pure: on `|r₀⟩` both end factors are 1, and on `S_σ ⊗ S_σ^*` the two end factors of `−1` and of `ω` are inverse to each other (the `y`-end acts by the contragredient).

**Theorem 4.2 (flat defect bands).** Take a site-count law in setting (G) of one of these two kinds.
(a) Spin(10) frame, SC-odd, link-pure registers. Put `c_z = ω_z = exp(iπ Σ_j 𝒢_z^{2j−1,2j})`.
(b) `U(5)` frame (SC-min or SC-odd), link operators that preserve each link's total rishon number. Put `c_z = exp(iπQ_z)`, `Q_z = N_z + Σ_{ℓ∋z} p_{ℓ,z}`.
Then in every D1 state, with respect to these `c_z`:
(i) the GNS space is the orthogonal sum of joint eigenspaces `H(κ)` of the implementers `U_z`, over finitely supported patterns `κ: Z³ → μ₄` (case (a)) or `κ: Z³ → {±1}` (case (b));
(ii) the odd sector lies in the sum `H_nt` over nontrivial patterns, and on `H_nt` the tick is momentum independent, `H_nt ≅ L²(T³; K)`, `T_β = M_β`, `Ũ = 1 ⊗ W`;
(iii) every band in `H_nt` is identically 1 near any node. In particular every odd defect band, including any band of the 16, is flat.

*Proof.* Case (b) first. On `V_x`, `N_x = 0` on `|∅⟩`, so the matter factor of `c_z` is `(−1)^{N_z}`. Each allowed link operator preserves the link's total rishon number `p_{ℓ,x} + p_{ℓ,y}`, so the product of its two end factors acts on it trivially. Hence `LZ1.md`'s identity at line 38 holds verbatim: the product of `Ad c_z` over a large finite set is `θ`. The proofs of `LZ1.md` Theorems 2.1 and 2.2 use only that identity, the commutation of `c_z` with every gate (gauge invariance of the gates' product, `LW1.md` E1), covariance, and D1. They apply unchanged.

Case (a). (1) *The implementers.* `ω_z` is the matter factor `ω_z^{mat}` (Lemma 3.2(e): `|∅⟩⟨∅| + i o_z`) times six commuting end factors. Two `ω`'s share at most one link and act there through commuting end actions, so they commute. The update commutes with every `𝒢_z^{ab}`, hence with `ω_z`. `ω_z^4` acts trivially by conjugation: on matter `ω_z^{mat}` has eigenvalues in `{1, i}`, and each end factor is the image of a central element of order dividing 4. Covariance is as in `LZ1.md`. A D1 state gives commuting implementers `U_z` with `U_z^4 = 1`, fixing `Ω`, commuting with `Ũ`, and translated by `T_β`.
(2) *Patterns of local operators.* For local `A` and finite `Λ` containing its matter support and both ends of its links, put `A_κ = 4^{−|Λ|} Σ_{n∈(Z₄)^Λ} ∏_{z∈Λ} κ_z^{−n_z} Ad(∏_{z∈Λ} ω_z^{n_z})(A)` for `κ ∈ μ₄^Λ`. Then `Σ_κ A_κ = A`, and `Ad ω_z(A_κ) = κ_z A_κ` for `z ∈ Λ` (character orthogonality on `(Z₄)^Λ`). For `z ∉ Λ`, `ω_z` acts trivially on `A`: it has no matter there and its end factors act on links outside `A`'s support.
(3) *Odd components are nontrivial.* Write `A_κ` as a sum of parts homogeneous in the site-count change `Δn`. On such a part, `Ad(∏_{z∈Λ} ω_z)` is `i^{Δn}` on the matter factor (Lemma 3.2(c), (e): `∏ω^{mat} = i^{N_s}`) times 1 on links, by link-purity. So `∏_{z∈Λ} κ_z = i^{Δn}`. If the part is odd, `Δn` is odd (Lemma 3.2(e)), so `∏κ_z ∈ {±i}` and `κ` is nontrivial. If `κ` is trivial, `i^{Δn} = 1`, so `Δn ≡ 0 mod 4` and the part is even.
(4) *The rest.* Steps (1)-(3) replace `LZ1.md` section 1's identity and its use in Theorem 2.1. The remaining steps of Theorems 2.1 and 2.2 are unchanged: apply `A ↦ A_κ` to `Ω` and use cyclicity for (i); a finite nonempty subset of `Z³` has no nonzero translation stabilizer, which gives `L²(T³; K)` and `Ũ = 1 ⊗ W` for (ii); the countable point spectrum of `W` and the `C¹` argument give (iii). ∎

**What the step is.** The site moves, but the centre pattern `κ` cannot: each `ω_z` is conserved and local, and SC-odd makes every odd operator carry a nontrivial pattern, because `θ = (−1)^{Δn}` and the pattern product is `i^{Δn}`. Proposition 3.5 shows the mechanism: the moving site drags a string of end-mixed links, and `ω` at each point is unchanged. So route 1 does not escape `LZ1.md` Theorem 2.2. In a D1 vacuum there is no light Weyl 16 to be chiral or vector-like. A propagating 16 would have to be a dressed charged sector (R-CS^str of `TOE_ASSEMBLY.md` section 3.6), which is `RCS1.md`'s open question MT1-S[R-CS^str], not this lane's.

**Proposition 4.2.3 (SC-odd is needed in case (a)).** Under SC-min with a Spin(10) frame, take the register `R′_ℓ = C|r₀⟩ ⊕ (S_+ ⊗ S_−)`, with `Spin(10)_x` on `S_+` and `Spin(10)_y` on `S_−`. Put
`A = Σ_{s∈B_+} Σ_{s′∈B_−} (|s⟩⟨∅|)_x ⊗̂ (|s′⟩⟨∅|)_y ⊗ |r₀⟩⟨e_s ⊗ e_{s′}|`.
Then `A ≠ 0` is local, gauge invariant and fermion odd. So `RCS1.md` Theorem 4 ("Every `A∈𝔄^G` is matter-even") fails for this site-count law, and so does the identity of `LZ1.md` line 38.

*Proof.* The matter factor creates an even site at `x` and an odd site at `y`, so `A` is odd. At `x`, `(|s⟩⟨∅|)_x` transforms like `e_s` and `⟨e_s|` like its dual; the contraction over `s ∈ B_+` is invariant, since `Spin(10)` preserves `S_+`. The same holds at `y` over `B_−`. Link-purity: both end lifts of `−1` are `+1` on `|r₀⟩` and `−1` on `S_+ ⊗ S_−`, so their product is 1. The end factors of `ω` are `1·1` on `|r₀⟩` and `(−i)(+i) = 1` on `S_+ ⊗ S_−` (Lemma 3.2(b): `ω` is `−i` on `S_+` and `+i` on `S_−`), so their product is 1 as well. ∎

`A` creates a Spin(10)-singlet pair, a 16 and a 16bar site joined by a link. It is a gauge-invariant local fermion, but a singlet. Whether such composites propagate is not decided here; they are not the 16 of CG1.

### 4.3 A Nielsen-Ninomiya theorem for a tick, at quasienergy 0

This section is about one smooth map `V: T³ → U(d)`, the Bloch form of a translation-covariant walk. The tick convention is `V = e^{−iH}` locally, so an eigenvalue `e^{−iE}` has quasienergy `E`. Put `Z₀ = {K : 1 ∈ spec V(K)}`, the quasienergy-0 set, and
`ω₃ = (1/24π²) tr(g^{−1}dg)³` on `U(d)`, `W₃[V] = ∫_{T³} V^*ω₃`.

**Definition 4.3 (Weyl point at quasienergy 0).** `K₀ ∈ Z₀` with `dim ker(V(K₀) − 1) = 2`. Near `K₀` take `H(K) = i log V(K)` with a branch cut that avoids `spec V(K₀)`, so `H` is smooth. Let `Q(K)` be its rank-2 spectral projector for eigenvalues near 0. In a smooth orthonormal frame of `ran Q`, `QHQ = a(K)·1 + b(K)·σ`, with `a(K₀) = 0`, `b(K₀) = 0`. Require `N = (∂b_j/∂K_i)(K₀)` invertible and the cone not over-tilted: `|∇a(K₀)·n̂| < |Nn̂|` for every unit vector `n̂`. Put `χ(K₀) = sign det N`, the chirality.

**Theorem F.** Let `V: T³ → U(d)` be smooth and `Z₀` finite.
(i) For each `K₀ ∈ Z₀` the limit `ind(K₀) = −lim_{ε→0} ∫_{∂B_ε(K₀)} V^*β` exists, with `β` the 2-form of Step 2 below, and `Σ_{K₀∈Z₀} ind(K₀) = W₃[V]`.
(ii) At a Weyl point, `ind(K₀) = −χ(K₀)`. So if `Z₀` consists of Weyl points, `Σ_{K₀∈Z₀} χ(K₀) = −W₃[V]`.
(iii) The same holds at any quasienergy `μ`, with `Z_μ` and `e^{iμ}V` in place of `Z₀` and `V`; `W₃[e^{iμ}V] = W₃[V]`.

*Proof.* **Step 1 (`ω₃` is closed).** Put `θ = g^{−1}dg`; then `dθ = −θ∧θ`. So `d tr θ³ = tr(dθ θθ − θ dθ θ + θθ dθ) = −tr θ⁴`. Moving one 1-form past a 3-form under the trace gives a sign `−1`, so `tr θ⁴ = −tr θ⁴ = 0`.

**Step 2 (the open set `C = {U : 1 ∉ spec U}` and its primitive `β`).** For `U ∈ C` put `L(U) = (1/2πi)∮_Γ ℓ(λ)(λ − U)^{−1}dλ`, where `ℓ(λ) = −i log λ` with `arg λ ∈ (0, 2π)` is holomorphic off `[0, ∞)`, and `Γ` encircles `spec U` inside `C∖[0, ∞)`. The same `Γ` serves near each `U`, so `L` is smooth on `C`. `L(U)` is Hermitian with spectrum in `(0, 2π)`, and `U = e^{iL(U)}`. Put `Φ(t, U) = e^{itL(U)}` on `[0,1] × C`. Write `Φ^*ω₃ = dt∧α_t + γ_t`. Closedness gives `∂_tγ_t = dα_t`. Integrate: `γ₁ − γ₀ = dβ` with `β = ∫₀¹ α_t dt`. Since `Φ(1, ·) = id` and `Φ(0, ·) = 1` is constant, `ω₃|_C = dβ`.

**Step 3 (Stokes).** `V(K) ∈ C` off `Z₀`. Remove balls `B_ε(K₀)`, `K₀ ∈ Z₀`. Since `V^*ω₃` is smooth on `T³`, `W₃[V] = lim_{ε→0} ∫_{T³∖∪B_ε} d(V^*β) = −lim Σ_{K₀} ∫_{∂B_ε(K₀)} V^*β`, with `∂B_ε` oriented as the boundary of `B_ε`. The limits exist separately: for `ε′ < ε`, the two sphere integrals differ by `∫_{B_ε∖B_{ε′}} V^*ω₃`, which tends to 0 because the integrand is bounded. This proves (i).

**Step 4 (a Weyl point).** (4a) On `K = K₀ + εn̂`, `a = ε∇a(K₀)·n̂ + O(ε²)` and `|b| = ε|Nn̂| + O(ε²)`, uniformly in `n̂`. The tilt condition and compactness of the sphere give `c > 0` with `|Nn̂| − |∇a·n̂| ≥ c`. So for small `ε` the doublet eigenvalues `λ_± = a ± |b|` satisfy `λ_+ > 0 > λ_−`, and the other eigenvalues of `H` stay away from 0. (Isolation alone already excludes `|∇a·n̂| > |Nn̂|` in any direction: `a` is odd and `|b|` even to first order, so the pair would pass from both positive to both negative along the sphere and meet 0.) (4b) The eigenvalue `e^{−iλ_+}` has argument `2π − λ_+` in `(0, 2π)`, and `e^{−iλ_−} = e^{i|λ_−|}` has argument `|λ_−|`. So `L(V(K)) = (2π − λ_+)P_+(K) + |λ_−|P_−(K) + L_rest(K)`, with `P_±` the doublet eigenprojectors and `L_rest` acting on `ran(1 − Q(K))`. (4c) On `K = K₀ + εn̂`, `n̂ ∈ S²`, as `ε → 0` and uniformly with first derivatives in `n̂`: `λ_± → 0`, `L_rest(K) → L_rest(K₀)`, and in the frame `P_+(K) → Π(n̂) = (1 + b̂·σ)/2` with `b̂ = Nn̂/|Nn̂|`. Hence `Φ(t, V(K₀ + εn̂)) → Ψ(t, n̂) = [1 + (e^{2πit} − 1)Π(n̂)] e^{itL_rest(K₀)}` in `C¹([0,1] × S²)`. (4d) Since `∫_{∂B_ε}V^*β = ∫_{[0,1]×S²} (Φ∘(id × V(K₀ + ε·)))^*ω₃` and the integrand is a polynomial in first derivatives, the limit is `∫_{[0,1]×S²} Ψ^*ω₃`. (4e) `Ψ` is block diagonal for `ran Q(K₀) ⊕ ran Q(K₀)^⊥`, and the 3-form of a block sum is the sum of the blocks' 3-forms. The second block depends on `t` only, so its 3-form vanishes. (4f) For `g = 1 + (λ − 1)P`, `λ = e^{2πit}`, `P = Π(n̂)`: `g^{−1} = 1 + (λ̄ − 1)P` and `g^{−1}dg = λ̄dλ P + A`, `A = (λ − 1)dP + |λ − 1|² PdP`. Only terms with one `dλ` survive. By cyclicity of the trace, `tr(g^{−1}dg)³ = 3 λ̄dλ ∧ tr(PAA)`. From `P²= P`: `PdP P = 0` and `PdP PdP = 0`. So `PA = (λ − 1 + |λ − 1|²)PdP = (1 − λ̄)PdP` and `PAA = (1 − λ̄)(λ − 1)PdPdP = −|1 − λ|² PdPdP`. Hence `tr(g^{−1}dg)³ = −3|1 − λ|² λ̄dλ ∧ tr(PdPdP)`. With `∫₀¹ |1 − e^{2πit}|² 2πi dt = 4πi`, `∫ Ψ^*ω₃ = (1/24π²)(−12πi) ∫_{S²} tr(ΠdΠdΠ) = −c₁(Π)`, where `c₁(Π) = (i/2π)∫_{S²} tr(ΠdΠdΠ)`. (4g) For `P = (1 + m·σ)/2` on the unit sphere of `m`, `tr(PdPdP) = (i/4)ε_{jkl} m_l dm_j∧dm_k = (i/2) dA`, so `∫ = 2πi` and `c₁ = −1`. The map `n̂ ↦ b̂` has degree `sign det N = χ`. So `c₁(Π) = −χ`, the limit in (4d) is `χ`, and `ind(K₀) = −χ`. This proves (ii).

**Step 5.** For (iii), `e^{iμ}` is a constant scalar, so `(e^{iμ}V)^{−1}d(e^{iμ}V) = V^{−1}dV`. ∎

[check] `check_F.py` (grid `28³`, central finite differences) evaluated two maps `T³ → SU(2)`. For `V(k) = e^{ik₁σ_x}e^{ik₂σ_y}e^{ik₃σ_z}` it found `W₃ = 0.0000` and eight quasienergy-0 nodes: `χ = −1` at `(0,0,0)`, `(0,π,π)`, `(π,0,π)`, `(π,π,0)` and `χ = +1` at `(π/2,π/2,π/2)`, `(π/2,3π/2,3π/2)`, `(3π/2,π/2,3π/2)`, `(3π/2,3π/2,π/2)`; so `Σχ = 0`. For the unit-quaternion map `h/|h|`, `h = (sin k₁, sin k₂, sin k₃, 2 − Σ_j cos k_j)`, which has no finite range, it found `W₃ = −1.0000` and seven nodes with `Σχ = +1`. Both agree with `Σχ = −W₃`, including the sign and the normalization `1/24π²`.

**Remark 4.3.1 (relation to published work).** Theorem F is the class-A, three-dimensional case of Bessho and Sato's Eq. (15) (arXiv:2006.04204), here for isolated nodes, proved natively. It differs from a per-band count. For any one band, the Berry monopole charges of all its nodes sum to zero, which is how Sun et al. (arXiv:1806.09296) count "an equal number of right-handed and left-handed Weyl points in 3D Floquet lattice". Theorem F counts the light species at one quasienergy, in the local ordering there.

**Remark 4.3.2 (the Floquet loophole).** Theorem F allows a single Weyl point at quasienergy 0 when `W₃[V] = ±1`. The static theorem has no such room, since a static band structure has `W₃ = 0`. So the question for LW1-form laws is whether their walks can have `W₃ ≠ 0`. Section 4.4 answers it for the one-site sector.

### 4.4 Setting (F): the one-site walk is a finite-depth circuit

Take a law in setting (F). Let `Ω_∅ = ⊗_x |∅⟩_x` be the empty background, `ω_∅` its product state, and `E₁(S)` the span of states on a finite set `S` with exactly one occupied point.

**Condition (E).** Each gate `g`, with support `{x, y}`, maps `C|∅∅⟩` and `E₁({x, y})` into themselves. Write `g|∅∅⟩ = λ_g|∅∅⟩`.

Under SC-odd, (E) reduces to `g|∅∅⟩ ∈ C|∅∅⟩`: one-site states are odd, two-site states are even, and gates are even. In words, (E) says that the empty lattice is a vacuum of the law and that sites move rather than appear in pairs from nothing.

**Lemma 4.4.1 (the one-site walk).** Under (E), `ω_∅` is invariant under the tick, and the GNS one-site space `H₁ ≅ ℓ²(Z³) ⊗ F` (`F = F_x` or `Λ^{odd}C⁵`) is invariant under the implementing unitary `Ũ` with `ŨΩ = Ω`. On `H₁`, `Ũ` is the walk
`V = ∏_{layers} ∏_{g in layer} u_g`, with `u_g = λ_g^{−1} g` on `E₁(supp g)` and `u_g = 1` on one-site states outside `supp g`.
`V` commutes with the even translations and has finite range, so its Bloch form `V(K)` on the cell torus `T³` is a trigonometric polynomial in `K`, with values in `U(8 dim F)`.

*Proof.* Each gate fixes `Ω_∅` up to the phase `λ_g`, so `ω_∅` is invariant under each gate's automorphism and under `α`. The GNS vector `π(|v⟩⟨∅|_x)Ω` is the one-site state `v` at `x`. A gate acts on it by `g` if `x ∈ supp g`, and otherwise multiplies it by `λ_g`, which cancels against the normalization `ŨΩ = Ω`. Gates of one layer have disjoint supports, so their product acts on `H₁` as the direct sum of the `u_g`, which converges strongly. Covariance under the cell lifts gives commutation with `τ_β`, `β ∈ 2Z³`; finitely many layers of nearest-neighbour gates give finite range. ∎

**Theorem H (the one-site walk winds trivially).** (a) `W₃[V] = 0`. (b) If every gate commutes with a compact group `G` that fixes `|∅⟩`, then for the isotypic decomposition `V = ⊕_ρ 1_ρ ⊗ V_ρ`, `W₃[V_ρ] = 0` for each `ρ`. (c) If only the complete update commutes with `G`, then `Σ_ρ (dim ρ) W₃[V_ρ] = 0`.

*Proof.* (a) By the spectral theorem write `u_g = e^{iA_g}` with `A_g = Σ_j θ_j P_j` Hermitian, `P_j` the spectral projectors of `u_g`. Choose `A_g` on one gate per cell-group orbit and transport it by the lifts; covariance makes `u_g` commute with its stabilizer, and so does `A_g`, a spectral function of `u_g`. Put `u_g(t) = e^{itA_g}` and `V(t) = ∏_{layers}∏_g u_g(t)`. Each `V(t)` is a covariant finite-range walk, `V(0) = 1`, `V(1) = V`, and `V(t, K)` is smooth on `[0,1] × T³`. Since `ω₃` is closed (Theorem F, Step 1), Stokes on `[0,1] × T³` gives `W₃[V(1)] − W₃[V(0)] = ∫_{[0,1]×T³} d(V^*ω₃) = 0`. And `W₃[1] = 0`. (b) If `g` commutes with `G`, so do its spectral projectors, hence `A_g` and every `u_g(t)`. So `V(t)` commutes with `G`, each `V_ρ(t)` is a smooth homotopy from `1` to `V_ρ`, and (a)'s argument applies to `V_ρ`. (c) `tr(V^{−1}dV)³ = Σ_ρ (dim ρ) tr(V_ρ^{−1}dV_ρ)³`; integrate and use (a). ∎

**Remark 4.4.2.** Higashikawa, Nakagawa and Ueda (arXiv:1806.06868) realize a single Weyl fermion through a "topologically nontrivial Floquet unitary operator". Theorem H shows that no one-site walk of an LW1-form law is of that kind. The proof uses only that the update is a finite product of local unitaries, and each local unitary lies in a connected group. The adiabatic one-handed bands of Sun et al. (arXiv:1806.09296) sit in a subspace that no exact symmetry separates; Theorem H(c) allows such sectors only when a symmetry sector of the same parity can compensate.

### 4.5 The 16 is vector-like in setting (F)

**Theorem 4.5.** Take a law in setting (F) under SC-min or SC-odd, with condition (E), and the global Spin(10). Let `V_σ` be the one-site walk restricted to content parity `σ` (`σ = −` only, under SC-odd). Then:
(i) `V_σ = 1_{S_σ} ⊗ W_σ` for a finite-range covariant walk `W_σ`, and `W₃[W_σ] = 0`;
(ii) if the quasienergy-0 set of `W_σ` is finite and consists of Weyl points, then `Σ χ = 0` over them: the 16 (and the 16bar) has as many left-handed as right-handed light nodes;
(iii) the same holds at every quasienergy `μ`.
No law of setting (F) gives a single light Weyl 16 without its mirror in the one-site sector over the empty lattice. No condition on the individual gates is needed beyond NN-a's evenness.

*Proof.* Gates are even. A one-site state has the parity of its content, so each `u_g` preserves the parity sectors of `E₁`. Hence `V_σ = ∏ u_g|_σ` is itself a finite product of local unitaries, and Theorem H(a) gives `W₃[V_σ] = 0`. The complete update commutes with the global Spin(10), which preserves `S_σ`; so `V_σ` commutes with Spin(10) on `S_σ ⊗ ℓ²(Z³)`. `S_σ` is irreducible, so by Schur's lemma `V_σ = 1_{S_σ} ⊗ W_σ`, and `W_σ` has finite range. Then `W₃[V_σ] = 16·W₃[W_σ]`, so `W₃[W_σ] = 0`. Theorem F(ii) gives (ii); Theorem F(iii) gives (iii). ∎

**The step, named.** The one-site walk of each content parity is a finite-depth circuit, hence null-homotopic (Theorem H). Parity and Schur's lemma put the whole 16 in one isotypic block, so the block's winding vanishes. Theorem F turns zero winding into zero net chirality at quasienergy 0. This is a Nielsen-Ninomiya theorem for defect bands. #10038 D2 is the special case of one supplied band, where "An invariant staggered on-point energy gaps them all".

**Scope of Theorem 4.5.** It covers sites moving over the empty lattice, at any interaction strength among the gates, because the one-site sector is exact. It does not cover a defect over a filled, entangled background, such as #10038's "exchange singlet vacuum": there the one-defect sector is not invariant under the gates. In the class itself, setting (G), Theorem 4.2 covers every D1 state, filled or not. A one-site fibre with two inequivalent irreducible types of the same parity (as for `U(5)` frames: `Λ¹`, `Λ³`, `Λ⁵`) would get only the weighted identity of Theorem H(c) when gates mix them; this file does not treat that case (section 3.3 keeps to the Spin(10) frame).

## 5. Target (3): what the rule costs TM1, LZ1, ZM1

### 5.1 TM1

**Lemma 5.1 (actual values on point registers).** Under the proposed PS-3g ("The actual value of a site is a joint value of the site observables that every exact frame at that site leaves unchanged"), with the Spin(10) frame: on `V_x` the actual value is one of `∅`, `+`, `−` (empty, even content, odd content); on `V_x^−` it is the occupation `o_x`.

*Proof.* As a Spin(10) module, `V_x = C ⊕ S_+ ⊕ S_−`, three pairwise inequivalent irreducibles (trivial, and the two half-spin modules, which `LW1_5.md` C2 separates by `P`). By Schur's lemma the fixed algebra is spanned by the three projectors. On `V_x^−` there are two summands, so the fixed algebra is `span{|∅⟩⟨∅|, o_x}`. ∎

So under SC-odd the actual configuration is the site configuration itself. PS-3h5 would need restating for point registers; that is a reading for the owner.

**Proposition 5.2 (TM1's proved results carry over).** `TM1.md` Theorems 1-5 hold verbatim for site-count laws with `a_x` the value of Lemma 5.1.

*Proof.* `TM1.md` Definition 3 asks for "a finite-spectrum self-adjoint even site observable `a_x`, with `β_g(a_x)=a_{gx}`". The projectors of Lemma 5.1 are even, have finite spectrum, and are covariant, since every lift fixes `|∅⟩` up to a phase and maps `S_±` to `S_±`. The proofs of Theorems 1-5 use only these properties, the disagreement projectors `D_xy`, stationarity, and transitivity of the cell group (`TM1.md` lines 41-63). ∎

**The cost: records against moving sites.** The Record axiom says: "When present, a record locks exactly one admissible local possibility. A site never carries more than one record; records are permanent." With moving sites it has two readings.

- **L-point.** A record at `x` fixes the actual value of the point `x` at every later half-tick.
- **L-site.** A record rides with its site (#10038 line 181: "a record must travel with its site's content").

**Proposition 5.3 (L-point blocks motion).** Let `ω′` be any state and take a history measure with the Born marginals of `ω′∘α^n` that respects L-point. If `x` records the value `v` at tick `t`, then `ω′∘α^n(Π_x(v)) = 1` for every `n ≥ t`.

*Proof.* Under L-point, `ξ_{2n}(x) = v` almost surely for `n ≥ t`. The Born marginal gives `ω′∘α^n(Π_x(v)) = P(ξ_{2n}(x) = v) = 1`. ∎

So under L-point a defect can never put or take occupation weight at a recorded point.

**Corollary 5.3.1 (a recorded vacuum confines a defect).** Let `ω` be stationary and in `TM1.md`'s case (E), where "every site records at tick 1" (Theorem 4). Let `ω′ = ω(O^*·O)/ω(O^*O)` for a local `O`. If the tick-1 witness test `α(D)`, `D = D_{xy} + D_{xz}`, of a point `x` commutes with `O`, then `x` records at tick 1 in `ω′` as it does in `ω`. Hence, under L-point, every point outside a bounded neighbourhood of `supp O` has sharp, constant occupation from tick 1 on. A history that respects L-point never lets the defect's occupation weight reach those points.

*Proof.* Stationarity and case (E) give `ω(α(D)) = 0` for a witness pair. Since `α(D)` is even and commutes with `O`, `ω(O^*α(D)O) = ω(O^*O α(D))`. Cauchy-Schwarz gives `|ω(O^*O α(D))|² ≤ ω((O^*O)²) ω(α(D)²)`, and `ω(α(D)²) ≤ ‖D‖ ω(α(D)) = 0` because `α(D) ≥ 0`. So `ω′(α(D)) = 0`. One tick has finite range, so the commutation holds outside a bounded neighbourhood of `supp O`. Proposition 5.3 applies at each such point. ∎

So, if VC1's vacuum lies in case (E), L-point leaves a site defect no band: it stays in a bounded region in every history that respects the records, and a law that moves its weight further has no such history. Under L-site the record needs a site to ride on. Lemma 3.1's encoding has no site names: two sites with equal content are not told apart, and a transfer is a swap. So L-site needs a name register at each point, which neither SC-min nor SC-odd supplies. Either way, route 1 adds a constraint to the open TM1-i: where records may form in a law whose sites move. Which reading holds is the owner's to decide.

### 5.2 LZ1

- **No gain in D1 vacua.** Theorem 4.2 extends `LZ1.md` Theorems 2.1-2.2 to site-count laws (Spin(10) frame with SC-odd and link-pure registers; `U(5)` frame in general). `LZ1.md` Corollary 2.3 then holds for them too: under R-loc, every odd light species of a D1 state is flat. Route 1 gives LZ1's fermion clause no propagating odd species in a D1 vacuum.
- **A broken identity under SC-min.** Proposition 4.2.3 breaks the identity at `LZ1.md` line 38 for an admissible register. LZ1's pattern argument must then be re-proved register by register, and `RCS1.md` Theorem 4 needs the hypothesis "SC-odd and link-pure" (or the specified registers) for site-count laws.
- **Static class.** In a D1 state the centre pattern of a defect is tick-fixed (Theorem 4.2(ii)). It belongs to the static class that owner decision LZ1-SC separates ("Tick-fixed weight is recorded as a separate static class, which LZ1 does not constrain").
- **Setting (F).** Theorem 4.5 pairs the light 16 nodes. LZ1-i's common-cone question then applies to Dirac pairs, as for any other vector-like species.

### 5.3 ZM1

**Proposition 5.4 (blocks carry all four centre classes).** Under SC-odd with a Spin(10) frame, let a block map `Φ` satisfy (G1) of `ZM1.md` Definition Z ("`Φ(G^{(1),T}_u) = sum_{x in S_u} G^T_x` for every coarse site `u` and every `T`"), with `|S_u| ≥ 3`. Then the coarse `ω_u^{(1)}` has every element of `μ₄`, up to one common phase, in its spectrum. So the coarse law cannot be of class SC-odd with end-pure coarse links.

*Proof.* `Φ` is a unital `*`-homomorphism, so it commutes with exponentials: `Φ(ω_u^{(1)}) = ∏_{x∈S_u} ω_x`. Pick a link configuration on which the end factors of the block's boundary links have fixed eigenvalues; links inside the block contribute a scalar by link-purity. On that configuration the matter factor is `i^{N_s(S_u)}` (Lemma 3.2(e)), and `N_s(S_u)` takes every value `0, …, |S_u|`, so `i^{N_s}` takes all four values. A unital `*`-homomorphism can only shrink spectra (`spec Φ(a) ⊆ spec a`, since `Φ` maps inverses to inverses), so `ω_u^{(1)}` has all four classes up to one phase. An SC-odd coarse register has matter classes `{1, i}` only, and end-pure coarse links multiply them by a scalar: two values. ∎

Since Proposition 3.4 already forces end-mixed links for any law whose sites move, Proposition 5.4 is a consistency condition rather than an obstruction: the zoom of a moving-site law has end-mixed coarse links too.

- **The comparison class of ZM1-I1[a].** The owner's text takes "all norm-at-most-one `A,B∈𝔄_1^G`". Under SC-odd with link-pure registers, `𝔄^G` stays matter-even: step (3) of Theorem 4.2's proof gives an odd local operator a nontrivial pattern, so some local centre moves it. Under SC-min, Proposition 4.2.3 puts odd elements in `𝔄^G`. The coarse law must then match the two-point tails of gauge-invariant fermions as well (`ZM1_OBS.md` Lemma ER, as cited in `TOE_ASSEMBLY.md` section 3.8: it "forces the coarse law to match the correlation length and amplitude of every nonzero invariant tail").

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma 3.1: sites that may be absent, at most one per point, are exactly point registers `V_x = C|∅⟩ ⊕ ΛC⁵`. Observation 3.1: the bend reads as Lattice (R-site) or as PS-5 (R-point).
- Lemma 3.2 and Corollary 3.3: with empty points, `z_x^{mat} = (−1)^{o_x}`, `∏ω^{mat} = (−i)^{N_s}(−1)^F`, and an operator's centre phase is `(−i)^{Δn}θ`; under SC-odd, `−1 ∈ Spin(10)` is local fermion parity (#10027 B and #10038 A2-A4, rebuilt).
- Proposition 3.4: on end-pure link registers, including `L5-O`'s `S_+`, every occupation `o_x` is conserved by every gauge-invariant gate.
- Proposition 3.5: the register `C|r₀⟩ ⊕ (S_+ ⊗ S_+^*) ⊕ (S_− ⊗ S_−^*)` carries an even, gauge-invariant, link-pure gate that moves a whole site.
- Proposition 3.6: under SC-odd site-count parity is fermion parity; globally invariant even operators have `Δn ≡ 0 mod 4`; with a link, `Δn = 1` is gauge invariant.
- The four-test table of section 3.4: SC-min P P P C; SC-odd F P F C.
- Theorem 4.2: in every D1 state of a site-count law (Spin(10) frame with SC-odd and link-pure registers, or `U(5)` frame), the GNS space splits into finitely supported centre patterns, the odd sector lies in nontrivial patterns, the tick there is momentum independent, and every odd band is flat near its nodes.
- Theorem F: for smooth `V: T³ → U(d)` with finite quasienergy-0 set, `Σ ind = W₃[V]`; at Weyl points `ind = −χ`, so `Σχ = −W₃[V]`; the same at every quasienergy.
- Lemma 4.4.1 and Theorem H: the one-site walk over the empty lattice is a finite product of local unitaries, so `W₃ = 0`; per isotypic block if gates commute with `G`; weighted by dimension otherwise.
- Theorem 4.5: in setting (F), for every law under SC-min or SC-odd with condition (E), `V_σ = 1_{S_σ} ⊗ W_σ` and `W₃[W_σ] = 0`, so the light 16 (and 16bar) nodes have zero net chirality at every quasienergy.
- Lemma 5.1, Propositions 5.2-5.4, Corollary 5.3.1: the actual values on point registers; TM1 Theorems 1-5 carry over; under L-point a recorded point's Born occupation is frozen, and in a case-(E) vacuum a local defect stays in a bounded region; under (G1) a coarse site carries all four centre classes.

**Counterexamples.**
- Proposition 4.2.3: under SC-min with a Spin(10) frame and the link-pure register `C|r₀⟩ ⊕ (S_+ ⊗ S_−)`, a nonzero local gauge-invariant odd operator exists. So "Every `A∈𝔄^G` is matter-even" (`RCS1.md` Theorem 4) and the identity at `LZ1.md` line 38 fail for site-count laws without SC-odd.
- Proposition 3.6(c): with a gauge link, a single site is created gauge-invariantly, so #10038 A7's "covariant site creation needs dn = 0 mod 4" does not extend to gauged laws.

**Open, by name.** Nothing in this lane stops at a three-attack lemma. Inherited and unchanged: MT1-S[R-CS^str] (`RCS1.md`), which is now where any propagating 16 of route 1 would have to live; VC1, including whether its vacuum is a D1 state. For the owner: adoption of SC-min or SC-odd, if either; the reading R-site or R-point (Observation 3.1); the reading L-point or L-site of the Record axiom (section 5.1); a point-register form of PS-3h5. Not decided and not needed for the targets: whether the singlet composites of Proposition 4.2.3 propagate.

**What changes downstream.**
- **CG1(e), route 1.** A site-count change does not by itself give a light chiral 16. In D1 vacua of the class there is no propagating 16 band at all (Theorem 4.2); in the free reading the 16 bands are vector-like for every law (Theorem 4.5). #10038 D2's numerical finding is now a theorem for every symmetric free one-site walk. Route 1 leads to the same place as charged matter generally: a dressed charged sector (R-CS^str).
- **PS-6r and GA1-P-5.** Moving sites need end-mixed registers (Proposition 3.4). `L5-O`'s `S_+` alone freezes them.
- **RCS1 and LZ1.** For site-count laws, Theorem 4 of RCS1 and Theorems 2.1-2.2 of LZ1 hold under SC-odd with link-pure registers (Theorem 4.2) and fail under SC-min for some registers (Proposition 4.2.3).
- **TM1.** If a site-count rule is ever adopted, the Record axiom needs a reading for moving sites (L-point or L-site) before TM1-i can be posed on that law.
- **ZM1.** A block map with (G1) for a moving-site SC-odd law needs coarse sites with all four centre classes (Proposition 5.4); under SC-min the ZM1-I1[a] comparison class contains gauge-invariant fermions.
- **Literature.** Bessho-Sato's Floquet theorem (arXiv:2006.04204, Eq. (15)) and the Higashikawa-Nakagawa-Ueda and Sun et al. Floquet Weyl constructions (arXiv:1806.06868, arXiv:1806.09296) are the published loophole; Theorem H closes it for the one-site walks of LW1-form laws.
