lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SGAPT: S-GAP at nonzero hop, pass 1

Written 2026-11-08 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen). Lane: wall W2, leaf S of `SMG1_TREE.md` (rank 1).

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" would mark a tiny scratch computation in `/tmp/toe-SGAPT/`; this pass ran none, so no statement below rests on a check. "Formal" marks a perturbative statement that is not proved.

**Source revisions read.**

| Ref | Commit |
|---|---|
| this checkout, branch `claude/toe-assembly` | `b5bf445d7` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `43a1fcc37` |
| `origin/docs/consolidate-chirality-doublers` (read with `git show` only) | file last changed `a1bced899` |

Files read in this folder, with the commit that last changed each: `prior/SGAPT.md` (`b5bf445d7`) lines 1-104 (all); `SMG1_TREE.md` (`a6291aad1`) lines 1-68 (head, tree), 253-368 (P4-P7), 584-632 (N9-N11), 634-660 (literature table), 735-816 (H, S), 817-830 (D, opening), 1124-1229 (specifications, ranking, Lane briefs 1-3); `SGAP.md` (`fb9508e83`) lines 1-155 (all, with Amendment 1); `SGAP0.md` (`fb9508e83`) lines 1-172 (all); `SMG15.md` (`8e8a7352d`) lines 1-219 (all); `SMG1.md` (`373e01725`) lines 49, 53, 57, 69, 132 (atom, by grep); `SMG1_OWNER_CHECK.md` (`777e071c3`) lines 17-21, 61-69, 138-150 (by grep); `TOE_ASSEMBLY.md` (`15d00adcf`) lines 169-180 (the four tests), 201-269 (sections 3.4-3.11), 739-759 (sections 10, 11). On `origin/main`: `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` (`4d0cd77bd`) lines 1-12, 230-240, 268-300; `docs/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md` (`1cb2a082b`) lines 17, 27, 51, 57-61; `docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` (`9a94662dc`) lines 9-14; `docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md` (`e92061999`) lines 12-15, 88-91. On the consolidation branch: `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 11, 2341.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The SGAP model is read plainly, as frozen. No axiom or law text is read adversarially, and none is proposed.

**Working set used, by name.** None directly. The model is the frozen SGAP ring model (`SGAP.md` Definitions 1-4). It inherits PS-5's five modes per site through `SMG15.md` Definition 1 (eight mirror Majoranas and one light mode). No owner reading is used: S-GAP is a finite-ring statement, separate from SMG1-GAP's GNS reading (`TOE_ASSEMBLY.md` line 261; `SGAP.md` line 22).

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: the spectral theorem and the variational principle in finite dimension; the Duhamel formula for `e^S H e^{-S}`; the fermionic Fock space and its momentum basis; elementary sums. Standard mathematics cited and not rebuilt, used in remarks only: the generalized Hölder inequality for traces (KMS bound). Published work enters only as credited context (section 2); no step below imports a published theorem.

---

## 0. The question, quoted

`SGAP.md` line 22, Definition 4: "**S-GAP** asks for `c₀,Δ>0` such that for every `τ>0`, `|t|,|ε|≤c₀τ`, allowed `L`, and `χ≠1`, `E_χ≥E_0+Δτ`." Line 21 fixes `H_ε=H_M+H_L+εH_4` on the half-filled Gauss space `H_{1/2}`, with `H_M=τΣ_x(W_x+14)`, `H_L=−tΣ_x hop_x`, `H_4=Σ_{x,a}T_{x,a}`, `T_{x,a}=iγ_{x,a}γ_{x+1,a}hop⁰_x`. Line 19: "`L∈4N`, `L≥8`", and "The electric coupling is zero".

`SGAP.md` line 5 (Amendment 1): "`SGAP0.md` ... proves S-GAP⁰, the t=0 case, with c₀=2·10⁻¹⁰ and Δ=7, uniform in the ring length". Same line: "Open by name: S-GAP at t≠0".

`SMG1_TREE.md` line 791, node S: "**Status:** OPEN." Line 797: "Cancel histories that do not detect the charged insertion. Bound the remaining charged histories with fermionic determinants retained." Line 815: "**Boundary.** This node covers a small square in \((t,\epsilon)\)."

Lane brief 1, lines 1192-1202: "Prove the stated S-GAP inequality for a nonzero neighbourhood in \((t,\epsilon)\), uniformly in allowed ring length. Preserve the canonical sector and every allowed nontrivial character." Then: "Normalize by the full moving-light partition function before taking absolute values. Seek an estimate tied to charged histories." The three attacks: "1. A charged polymer ratio with fermion determinants retained. 2. A defect-relative local Schrieffer–Wolff inequality. 3. A sector-aware localized charge-removal comparison." And: "Do not replace the full square by a weak-interaction wedge without naming the weaker theorem."

## 0.1 Outcome in one paragraph

**Open, after three named attacks.** S-GAP at `t≠0` is neither proved nor refuted. It stays open as the residual lemma **SGAPT-R** (section 5.4), the defect form of S-GAP. **Proved here, for every allowed `L`:** (A) a structure theorem (Theorem A): if some unitary that commutes with the global `S` action, `N` and the holonomy brings `H_ε` to `H_M+Σ_I V′_I+R`, with each `V′_I` supported on an arc `I` and commuting with the mirror-vacuum projector of `I`, then every charged level lies at least `14τ−d−2‖R‖` above `E_1`; here `d` measures how much the `V′_I` change in the presence of a mirror defect. The light sector's infrared behaviour plays no role. The case `U=1`, `R=0` contains the charged bound of `SMG15.md` Theorem 3. (B) A first-order dressing (Proposition B) gives `d≤16|ε|` and `‖R‖≤L|ε|(12|t|+144|ε|)/τ`. So `E_σ−E_1≥7τ` on rings of length `L≤(7τ−16|ε|)τ/(2|ε|(12|t|+144|ε|))`; this finite-ring bound is not S-GAP. (C) The convergent form of attack 2 meets resonances (Theorem C): on every arc of length `ℓ≥1+28τ/|t|`, the vacuum block and a pair block of the local unperturbed operator have eigenvalues within `π|t|/(ℓ+1)` of each other, and for a dense set of `t` in every `[−c₀τ,c₀τ]` some arc has an exact coincidence. (D) The absolute linked sums of attack 1 diverge (Theorem D): in the free half-filled light ring, the bond-bond connected correlation `C(x,s)` obeys `Σ_x C(x,s)=0` for every `s`, while `Σ_x∫_0^∞|C(x,s)|ds≥log(L/4+1)/(2π|t|)`. This is the Peierls `2k_F` logarithm. (E) A localized removal identity (Lemma E) extends `SGAP.md` Theorem 5 to every configuration-diagonal localizer. **What fails.** Attack 1 fails at the absolute linked sum (Theorem D). Attack 2 fails at the remainder: finite order leaves an extensive remainder (Proposition B), and the convergent version meets the resonances of Theorem C. Attack 3 fails at the localizer: a localizer that reads a bounded window cannot tell the charge from a neutral fluctuation with the same window content, whose removal costs `44τ` against a gain of `16τ` (exact energetics); the weight of such fluctuations is extensive only at a formal level. **Smallest sufficient sub-lemma found:** LOC (section 5.4), a flux bound for one family of localizers; with Lemma E it gives S-GAP with `Δ=16−Kc₀`. **Tree check.** The two "smallest rungs" of node S are already settled by elementary bounds and do not contain the difficulty (section 5.5). **Formal, not proved:** the square `|t|,|ε|≤c₀τ` contains, for every `c₀`, the line `|t|≈2ε²/(7τ)` where the second-order light chain is the isotropic XXZ chain; a proof that rests on infrared control of the light, as attack 1 does, would have to pass through that point. No counterexample was found, and none is expected.

## 1. Prior work used

Each item names what this file takes, and where it lives. All are frozen inputs; none is reopened.

| Prior result | Path | Use here |
|---|---|---|
| Model, notation, Definitions 1-6 | `SGAP.md` lines 19-24 | The setting of every statement below. |
| Theorem 1: symmetries; only the eight characters `Ŝ_+` occur on `H_{1/2}` | `SGAP.md` line 30 | Sector bookkeeping in section 3. |
| Theorem 2: at `ε=0`, `E_σ=E_L+16τ` for every `t` | `SGAP.md` line 36 | The anchor `Δ≤16`; the exact `ε=0` line. |
| Theorem 3: `YH_εY=H_ε+B` | `SGAP.md` lines 44-50 | The defect form SGAPT-R (section 5.4); Lemma E. |
| S-GAP is equivalent to `E_σ−E_1≥Δτ` for all seven `σ` | `SGAP.md` line 58 | Reduces the target to `E_σ−E_1`. |
| Theorem 4: parity chains at `t=0` | `SGAP.md` lines 64-70 | Context for section 5.6. |
| Theorem 5 (Lemma R), R-w, A4 | `SGAP.md` lines 105-121, 141 | Extended by Lemma E; A4 is the unlocalized form of attack 3. |
| A5: `λ_min(K+B)=λ_min(K)` on windows preserved by `Y` | `SGAP.md` line 147 | Excludes unrestricted windows from attack 3. |
| Theorems 2-9, S-GAP⁰; the cancellation "away from non-wall bonds" | `SGAP0.md` lines 38-156, 162 | The `t=0` endpoint; the mechanism attack 1 tries to extend. |
| Theorem 1: configuration projectors `P^χ`, rank one; degree-four mixing is off-diagonal | `SMG15.md` lines 32-34 | Section 3. |
| Theorem 2: Gauss reduction `J` | `SMG15.md` lines 36-40 | Section 3. |
| Theorem 3: charged levels cost `≥14τ−2δ` in the configuration-conserving family | `SMG15.md` lines 62-68 | Recovered as the case `U=1`, `R=0` of Theorem A. |
| Theorem 7: `PH_4Q(QH_MQ)⁻¹QH_4P=(2/(7τ))Σ_xΛ_x²P` | `SMG15.md` lines 136-144 | The formal light chain in section 5.6. |
| §8 routes 1-3 (extensive Schrieffer-Wolff remainder; absolute `|z|⁻²` light sum; two-dimensional on-site kernel) | `SMG15.md` lines 156-160 | Attacks 2 and 1 sharpen routes 1 and 2 into Proposition B, Theorem C and Theorem D. |
| Theorem 2.2: atom spectrum `−14` once, `0` eight times (odd), `2` seven times (even) | `SMG1.md` line 53 | The local gap `14τ` in Theorem A. |
| Node S, P5-P7, N11, Lane brief 1 | `SMG1_TREE.md` lines 765-815, 275-368, 610-632, 1190-1202 | Target, attacks, stopping rule. |
| Prior-work digest | `prior/SGAPT.md` | Map of the above. |
| Exact Feshbach operator whose bound "retains v's volume dependence" | `origin/main:docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 230-235 | Same obstruction as Proposition B, in a different model. |
| Sector-preserving coordinate argument "centered on its OWN vacuum energy", importing Yarotsky with "a unique vacuum and gap at least1" | `origin/main:docs/GAUGE_WILSON_FINITE_PW_UNIFORM_STATIC_SOURCE_ENERGY_BOUNDS_BOUNDED_THEOREM_NOTE_2026-09-07.md` lines 27, 57 | Its unique-vacuum hypothesis fails here: each site's light mode gives a two-dimensional on-site kernel. |
| Fermionic polymer norm "in an explicit high-mass, small-coupling region" | `origin/main:docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` lines 11-13 | Massive scope only; the light here is massless (Theorem D). |
| Atomic spectrum of the eight-Majorana Cayley form, `−14 (1), 0 (8, odd), +2 (7, even)` | consolidation branch, `docs/CHIRALITY_DOUBLERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` line 2341 | Agrees with `SMG1.md` Theorem 2.2. |

**Prior work the digest missed.** None that bears on S-GAP at `t≠0`. One relation the digest does not state: `SMG15.md` Theorem 3's charged bound is the special case of Theorem A below with `U=1` and `R=0` (section 4.1, Remark A.2).

## 2. Literature read

**Searches run (2026-11-08).** Web searches: Del Vecchio-Fröhlich-Pizzo-Rossi block-diagonalization with degenerate on-site ground states; rigorous mobile impurity in a Luttinger liquid with volume-uniform energy bounds; Henheik-Teufel-Wessel local stability; stability of a gapped sector beside gapless fermions and sector energies (extended search); Gentile-Mastropietro RG review; Datta-Fernández-Fröhlich quantum Pirogov-Sinai; rigorous RG for 1D fermions with a localized impurity; Brydges-Battle-Federbush cluster expansions with Gram bounds. The searches found no paper that proves a volume-uniform charged-sector energy bound for a gapped system coupled to a gapless one-dimensional Fermi sea. This is a report on these searches only, not a claim that no such paper exists.

**Fetched and checked (abstract page; full text where stated).** Short quotes are from the fetched pages.

| Work | Identifier | What was checked | Bearing here |
|---|---|---|---|
| J. Fröhlich, A. Pizzo, "Lie-Schwinger block-diagonalization and gapped quantum chains" | arXiv:1812.02457 (v2, 2019-02-27) | Abstract: on-site base Hamiltonian with a positive gap, short-range bounded interactions; the gap is "bounded from below by a positive constant uniformly in the length of the chain". The tree's locator "Theorem 3.5; hypotheses (1.4), (1.6), (1.7)" was **NOT VERIFIED**. | The convergent form of attack 2 (Theorem C). |
| S. Del Vecchio, J. Fröhlich, A. Pizzo, S. Rossi, "Local iterative block-diagonalization of gapped Hamiltonians: a new tool in singular perturbation theory" | arXiv:2007.07667, J. Math. Phys. 63, 073503 (2022) | Abstract, and section 1 of the ar5iv text (first 100k characters): the main theorem (section 1.2; its number was lost in the HTML) assumes on-site terms with ground state at `0` and a gap, interactions of norm at most `1`, and `|t|` below a threshold independent of size. Section 1 says the methods "can be extended to families of unperturbed operators with degenerate ground-state energies"; no condition for that case appears in the part read. | Same. The degenerate extension is not checked; Theorem C shows what fails for the degeneracy met here. |
| S. Del Vecchio, J. Fröhlich, A. Pizzo, "Block-diagonalization of infinite-volume lattice Hamiltonians with unbounded interactions" | arXiv:2108.13907 | Abstract only: gapped on-site operator plus small short-range perturbation; degenerate on-site case not stated. | Context. |
| S. Bravyi, M. Hastings, S. Michalakis, "Topological quantum order: stability under local perturbations" | arXiv:1001.0344, J. Math. Phys. 51, 093512 (2010) | Abstract: "sum of geometrically local commuting projectors on a D-dimensional lattice", with topological order conditions. | Requires a gapped unperturbed Hamiltonian; the light ring here is gapless. |
| S. Michalakis, J. Pytel, "Stability of Frustration-Free Hamiltonians" | arXiv:1109.1588, Commun. Math. Phys. 322, 277-302 (2013) | Abstract: "stability of the spectral gap for gapped, frustration-free Hamiltonians under general, quasi-local perturbations". The brief's "Michalakis-Zwolak" names this paper; that J. Pytel and J. P. Zwolak are one author is from memory, **NOT VERIFIED**. | Same requirement of a gap. |
| W. De Roeck, M. Salmhofer, "Persistence of exponential decay and spectral gaps for interacting fermions" | arXiv:1712.00977 (journal DOI 10.1007/s00220-018-3211-z) | Abstract: free system with a gapped ground state; "if the interaction is sufficiently weak, then the interacting system has a spectral gap as well". | Gapped free fermions only. |
| M. B. Hastings, "The Stability of Free Fermi Hamiltonians" | arXiv:1706.02270 | Abstract: "prove the stability of free fermion Hamiltonians which are gapped and local". | Same. |
| J. Henheik, S. Teufel, T. Wessel, "Local stability of ground states in locally gapped and weakly interacting quantum spin systems" | arXiv:2106.13780, Lett. Math. Phys. 112 (2022) | Abstract: "weakly interacting quantum spin systems with uniformly gapped on-site terms"; local perturbations change the ground state only locally, even when they close the gap. | The light mode has no on-site gap, so this does not apply; it is the closest "local perturbation" result found. |
| D. A. Yarotsky, "Quasi-particles in weak perturbations of non-interacting quantum lattice systems" | arXiv:math-ph/0411042 | Abstract: decoupled model with a non-degenerate gapped ground state. The tree's description of this identifier ("product-state stability", "Theorems 1-3") was not matched against the full text, **NOT VERIFIED**. | Imported by the main-branch static-source note with "a unique vacuum and gap at least1"; fails here for the same reason. |
| D. Abanin, W. De Roeck, W. W. Ho, F. Huveneers, "A Rigorous Theory of Many-Body Prethermalization for Periodically Driven and Closed Quantum Systems" | arXiv:1509.05386, Commun. Math. Phys. 354, 809-827 (2017) | Abstract: for well-separated scales, an effective conserved quantity persists for a time "(almost) exponential in U/J". | The finite-order remainder of Proposition B; quasi-conservation, not exact block form. |
| M. Salmhofer, C. Wieczerkowski, "Positivity and Convergence in Fermionic Quantum Field Theory" | arXiv:math-ph/9909002 | Abstract: convergence holds if the "propagator is summable and has a finite Gram constant". | Attack 1's single-scale route needs a summable light propagator; Theorem D shows the relevant sum diverges. |
| G. Benfatto, V. Mastropietro, "Universality relations in non-solvable quantum spin chains" | arXiv:0907.2837 (DOI 10.1007/s10955-010-9920-0) | Abstract: proves "exact relations between the critical exponents and the susceptibility" for weak short-range interactions. The tree's locator "Theorem 1.1; Eqs. (14)-(18)" was **NOT VERIFIED**. | Multiscale control of a weakly interacting light chain; would cover only a weak-interaction wedge (section 5.6). |
| G. Benfatto, V. Mastropietro, "Ward identities and Chiral anomaly in the Luttinger liquid" | arXiv:cond-mat/0409049, Commun. Math. Phys. 258, 609-655 (2005) | Abstract: "Luttinger liquid behavior characterized by non universal critical indices". | Same. |
| G. Antinucci, V. Mastropietro, M. Porta, "Universal edge transport in interacting Hall systems" | arXiv:1708.08517 (DOI 10.1007/s00220-018-3192-y) | Abstract: proofs by "exact renormalization group methods" and Ward identities. How the gapped bulk is integrated out was not checked in the full text, **NOT VERIFIED**. | The closest structural analogue found: a gapped sector beside interacting gapless one-dimensional fermions. |
| G. Gallavotti, "The Luttinger model: its role in the RG-theory of one dimensional many body Fermi systems" | arXiv:cond-mat/0008090, J. Stat. Phys. 103, 459-483 (2001) | Abstract only. | Context for the RG route. |
| N. Datta, R. Fernández, J. Fröhlich, "Low-temperature phase diagrams of quantum lattice systems. I." | mp_arc 95-228 (1995) | Abstract: classical systems in two or more dimensions with "a finite number of periodic ground states", small quantum perturbations, fermions allowed. | Context for the wedge in section 5.6; its stated dimension is not ours. |
| L. Fidkowski, A. Kitaev, "The effects of interactions on the topological classification of free fermion systems" | arXiv:0904.2197 (PRB 81, 134509) | Abstract: the invariant "becomes well defined only modulo 8". | The eight-Majorana atom's origin. |
| J. Wang, Y.-Z. You, "Symmetric Mass Generation" | arXiv:2204.14271, Symmetry 14, 1475 (2022) | Abstract: SMG is mass generation "without involving any symmetry breaking within an anomaly-free symmetry group". | Context. |
| D. Tong, "Comments on Symmetric Mass Generation in 2d and 4d" | arXiv:2104.03997 (JHEP 07 (2022) 001) | Abstract only. | Context. |

**Credited from memory, NOT VERIFIED, never load-bearing.** G. Gentile, V. Mastropietro, Phys. Rep. 352 (2001) 273-437 (only its bibliographic record was seen); D. Brydges, P. Federbush, Commun. Math. Phys. 49 (1976); G. Battle, P. Federbush; K. Gawędzki, A. Kupiainen (Gross-Neveu); C. Kane, M. Fisher on a local impurity in a Luttinger liquid; R. Peierls and H. Fröhlich on the one-dimensional `2k_F` logarithm, which Theorem D rebuilds in the form needed here.

## 3. The model and the target, exact

**3.1 Configuration form (prior results, restated).** Fix the holonomy `w=±1`. Order all mirror modes before all light modes. By `SMG15.md` Theorems 1-2 and the proof of Theorem 3 (lines 32-40, 62-68), and `SGAP.md` Theorem 4 (lines 64-70), the holonomy-`w` part of `H_{1/2}` is

`H^{(w)}_{1/2} = 𝓜_+ ⊗ 𝓕`,

where `𝓕` is the light Fock space of `c_0,…,c_{L−1}` at `N=L/2`, and `𝓜_+` is spanned by the mirror configuration vectors `e_χ=⊗_x e_{χ_x}` with `∏_x χ_x∈Ŝ_+`. Here `e_{χ_x}` is a fixed unit vector in the rank-one character line `χ_x` of site `x`. Every even mirror operator acts as `M⊗1` and every even light operator as `1⊗ℓ`. All terms of `H_ε` are of these two kinds, or products of one of each:

- `H_M=Σ_χ τΣ_x e(χ_x)|e_χ⟩⟨e_χ|⊗1`, with `e(1)=0`, `e(ρ_a)=14`, `e(σ′)=16` for even `σ′≠1` (`SMG1.md` Theorem 2.2);
- `H_L=1⊗h^{(w)}`, `h^{(w)}=−tΣ_{x=0}^{L−2}(c_x†c_{x+1}+c_{x+1}†c_x)−tw(c_{L−1}†c_0+c_0†c_{L−1})`;
- `H_4=Σ_{x,a}M_{x,a}⊗Λ_x`, with `Λ_x=c_x†c_{x+1}+c_{x+1}†c_x` (indices mod `L`, no factor `w`), and `M_{x,a}=iγ_{x,a}γ_{x+1,a}` sending `e_χ` to `ω e_{χ^{x,a}}`, `|ω|=1`, where `χ^{x,a}` multiplies `χ_x` and `χ_{x+1}` by `ρ_a`.

The charge of `e_χ⊗φ` is `q(χ)=∏_xχ_x`. For `σ∈Ŝ_+`, the sector `H^{σ,(w)}_{1/2}=𝓜_σ⊗𝓕` uses the configurations with `q(χ)=σ`. Write `E_σ` for the bottom of `H_ε` on `⊕_w H^{σ,(w)}_{1/2}`.

**3.2 Notation used below.**

- `P^1_x` is the projector onto configurations with `χ_x=1` (an even mirror operator). For an arc `I⊂Z_L` (consecutive sites, possibly all of `Z_L`), `P^+_I=∏_{x∈I}P^1_x` and `Q_I=1−P^+_I`.
- `𝒩=Σ_x(1−P^1_x)` counts non-vacuum sites. Because every non-trivial character costs at least `14τ`, `H_M≥14τ𝒩`. On every charged sector, `𝒩≥1`, since `q(χ)≠1` forces some `χ_x≠1`.
- An operator is **supported on `I`** if it lies in the even part of the algebra generated by the matter modes (the eight `γ_{x,a}` and `c_x`) at the sites of `I`. Bond terms of `H_L` and `H_4` on the bond `{x,x+1}` are supported on that bond; for `x=L−1` the factor `w` is a number.
- The mirror vacuum is `e_vac=e_{(1,…,1)}`.

**3.3 The target in defect form.** By `SGAP.md` line 58, S-GAP holds if and only if there are `c₀,Δ>0` with `E_σ−E_1≥Δτ` for all seven `σ∈Ŝ_+∖{1}`, every allowed `L`, `τ>0`, and `|t|,|ε|≤c₀τ`. By `SGAP.md` Theorem 3, `E_σ` is the neutral bottom of `H_ε+B_σ`, with `B_σ=16τ(P^1_0−P^σ_0)−2εΣ_{c∈{a,b}}(T_{−1,c}+T_{0,c})`. So S-GAP says: the local operator `B_σ` raises the neutral bottom by at least `Δτ`. Section 5.4 states this as the residual lemma.

## 4. Results

### 4.1 Theorem A: a defect-relative block form gives a charged gap

**Lemma A.0 (vacuum compression).** Let `V` be supported on an arc `I`. Then there is a unique operator `ℓ` on the light modes of `I` with `P^+_IVP^+_I=(1⊗ℓ)P^+_I`. Moreover `‖ℓ‖≤‖V‖`; `ℓ` is self-adjoint if `V` is; `ℓ` commutes with `N` if `V` does.

*Proof.* Expand `V=Σ_α m_αℓ_α`, with `m_α` a monomial in the mirror Majoranas of `I` and `ℓ_α` a monomial in the light modes of `I`, of equal parity. `P^+_I` is the rank-one projector onto `vac_I=⊗_{x∈I}e_1` on the mirror of `I`, tensored with the identity elsewhere. It is even, so it commutes with every light operator. Hence `P^+_Im_αℓ_αP^+_I=(P^+_Im_αP^+_I)ℓ_α=⟨vac_I,m_αvac_I⟩P^+_Iℓ_α`. The vector `vac_I` is even, so the coefficient vanishes for odd `m_α`. Put `ℓ=Σ_α⟨vac_I,m_αvac_I⟩ℓ_α`, a sum over even terms. Since `P^+_I` and `ℓ` act on different tensor factors, `‖ℓ‖=‖(1⊗ℓ)P^+_I‖=‖P^+_IVP^+_I‖≤‖V‖`. Uniqueness, self-adjointness and the commutation with `N` follow from the same tensor-factor statement. `□`

**Definition.** For `V′_I` supported on `I` and commuting with `P^+_I`, write `ℓ_I` for its compression from Lemma A.0, and `δ_I=‖V′_I−1⊗ℓ_I‖` for its **defect sensitivity**. For a family `{V′_I}`, put `d=max_xΣ_{I∋x}δ_I`.

**Theorem A.** Fix `L`, `τ>0`, real `t,ε`. Let `U` be a unitary on `⊕_wH^{(w)}_{1/2}` that commutes with every `U_g`, `g∈S`, and with the holonomy. Suppose

`UH_εU* = H_M + Σ_{I∈𝓘}V′_I + R`,

where `𝓘` is a finite family of arcs, each `V′_I` is self-adjoint, supported on `I`, commutes with `N` and with `P^+_I`, and `R` is self-adjoint. Let `H_eff=Σ_Iℓ_I` and let `e_eff` be the least eigenvalue of `H_eff` on `𝓕` over both holonomies. If `d≤14τ`, then for every `σ∈Ŝ_+∖{1}`

`E_σ − E_1 ≥ 14τ − d − 2‖R‖`.

*Proof.* Step 1. `V′_I` and `1⊗ℓ_I` both commute with `P^+_I`, and `P^+_I(V′_I−ℓ_I)P^+_I=0` by Lemma A.0. So `V′_I−ℓ_I=Q_I(V′_I−ℓ_I)Q_I≥−δ_IQ_I`.

Step 2. For commuting projectors `p,q`: `1−pq=(1−p)+p(1−q)` and `p(1−q)≤1−q`. By induction, `Q_I≤Σ_{x∈I}(1−P^1_x)`.

Step 3. Steps 1-2 give `Σ_I(V′_I−ℓ_I)≥−Σ_x(Σ_{I∋x}δ_I)(1−P^1_x)≥−d𝒩`. With `H_M≥14τ𝒩` (section 3.2) and `R≥−‖R‖`:

`UH_εU* ≥ 1⊗H_eff + (14τ−d)𝒩 − ‖R‖`.

Step 4 (charged sector). `1⊗H_eff` and `𝒩` commute and preserve `𝓜_σ⊗𝓕`. There `𝒩≥1` and `H_eff≥e_eff`. Since `14τ−d≥0`, the right side of Step 3 is at least `e_eff+14τ−d−‖R‖` on `𝓜_σ⊗𝓕`, in both holonomies. `U` maps the `σ`-sector onto itself, so `E_σ≥e_eff+14τ−d−‖R‖`.

Step 5 (neutral sector). Choose a holonomy `w₀` and a unit `φ∈𝓕` with `H^{(w₀)}_effφ=e_effφ`. Put `Ψ₀=e_vac⊗φ`. It is neutral, half-filled and lies in every `Ran P^+_I`. Hence `V′_IΨ₀=P^+_IV′_IP^+_IΨ₀=ℓ_IΨ₀`, and `H_MΨ₀=0`. So `⟨Ψ₀,UH_εU*Ψ₀⟩=e_eff+⟨Ψ₀,RΨ₀⟩≤e_eff+‖R‖`. The unit vector `U*Ψ₀` is neutral and half-filled. The variational principle gives `E_1≤e_eff+‖R‖`.

Step 6. Subtract Step 5 from Step 4. `□`

**Remark A.1 (no infrared input).** `H_eff` may be gapless, and its ground state may be degenerate. The proof uses one operator inequality for the charged sectors and one trial vector for the neutral sector. Both see the same `H_eff`, so the light energy cancels exactly. No correlation of the light enters.

**Remark A.2 (`SMG15.md` Theorem 3 is the case `U=1`, `R=0`).** For `H_A` of `SMG15.md` §3, take `V′_x=K_x` on the bond `{x,x+1}`. `K_x` preserves configurations, so it commutes with `P^+_{\{x,x+1\}}`, and `ℓ_x=κ_x(1,1)`. Then `δ_x=max_{(χ,χ′)≠(1,1)}‖κ_x(χ,χ′)−κ_x(1,1)‖≤δ` (`SMG15.md` line 60: "The bond-norm difference is at most `δ`"), so `d≤2δ`. Theorem A gives `E_σ−E_1≥14τ−2δ`. This is the charged bound of `SMG15.md` Theorem 3 (line 66: "all globally `S`-charged levels cost at least `14τ−2δ`"). Theorem A extends it from configuration-preserving terms to terms that only preserve the local vacuum.

**Remark A.3 (the trivial instance for `H_ε`).** Take `U=1`. Split each `T_{x,a}` into the part that conserves the bond's mirror energy and the rest (section 4.2). The first part kills `P^+_{\{x,x+1\}}`-vectors and has range in `Q_{\{x,x+1\}}`, so it commutes with `P^+_{\{x,x+1\}}`. Put it, with `−t` times the bond's light hop, into `V′_x`, and the rest into `R`. Then `ℓ_x` is the light hop, `δ_x≤8|ε|`, `d≤16|ε|`, `‖R‖≤8|ε|L`, and `E_σ−E_1≥14τ−16|ε|−16|ε|L`. Only rings with `L<(14τ−16|ε|)/(16|ε|)` gain anything. Proposition B improves the remainder by one power of `(|t|+|ε|)/τ`.

### 4.2 Proposition B: first-order dressing, with an extensive remainder

**Energy bookkeeping of one move.** For a bond `b={x,x+1}` and a flavour `a`, let `Δ_{b,a}(χ)=e(χ_xρ_a)−e(χ_x)+e(χ_{x+1}ρ_a)−e(χ_{x+1})`. One site contributes `+14` (from `1`), `−14` (from `ρ_a`), `+2` (from `ρ_c`, `c≠a`) or `−2` (from an even `σ′≠1`). So `Δ_{b,a}∈{0,±4,±12,±16,±28}`. The move `χ↦χ^{b,a}` is an involution and `Δ_{b,a}(χ^{b,a})=−Δ_{b,a}(χ)`. Let `D^0_{b,a}` project onto the configurations with `Δ_{b,a}=0`, and let `K_{b,a}` be the configuration-diagonal operator with entry `1/Δ_{b,a}(χ)` where `Δ_{b,a}(χ)≠0` and `0` elsewhere. Then `‖K_{b,a}‖≤1/4`. Put `T^0_{b,a}=T_{b,a}D^0_{b,a}` and `T^≠_{b,a}=T_{b,a}(1−D^0_{b,a})`.

**Lemma B.1.** (i) `T^0_{b,a}` and `T^≠_{b,a}` are self-adjoint with norm at most `1`, and `T^0_{b,a}` commutes with `P^+_b`. (ii) `[H_M,T_{b,a}K_{b,a}]=τT^≠_{b,a}`. (iii) `(T_{b,a}K_{b,a})*=−T_{b,a}K_{b,a}`. (iv) All three operators commute with every `U_g`, with `N` and with the holonomy, and are supported on `b`.

*Proof.* `T_{b,a}e_χ⊗φ=ωe_{χ^{b,a}}⊗Λ_bφ` with `|ω|=1`, and `‖M_{b,a}‖=‖Λ_b‖=1`. Since `Δ(χ^{b,a})=−Δ(χ)`, `T_{b,a}` commutes with `D^0_{b,a}`, which gives (i)'s self-adjointness and norms. On `Ran P^+_b`, `Δ=28≠0`, so `T^0_{b,a}P^+_b=0`; taking adjoints, `P^+_bT^0_{b,a}=0`. (ii): `H_M` is diagonal and the move changes its value by `τΔ_{b,a}(χ)`, so `[H_M,T_{b,a}K_{b,a}](e_χ⊗φ)=τΔ(χ)Δ(χ)^{−1}T_{b,a}(e_χ⊗φ)` when `Δ(χ)≠0`, and `0` otherwise. (iii): `K_{b,a}T_{b,a}(e_χ⊗φ)=Δ(χ^{b,a})^{−1}T_{b,a}(e_χ⊗φ)=−T_{b,a}K_{b,a}(e_χ⊗φ)`, and `K_{b,a}` is real diagonal. (iv): both Majoranas of `M_{b,a}` take the same sign `ρ_a(g)` under `U_g` (`SGAP.md` Theorem 1); `U_g` and `K_{b,a}`, `D^0_{b,a}` are configuration-diagonal; `Λ_b` conserves `N` and has no link. `□`

**Proposition B.** For every allowed `L`, `τ>0`, real `t`, `|ε|≤7τ/8`, and every `σ∈Ŝ_+∖{1}`:

`E_σ − E_1 ≥ 14τ − 16|ε| − 2L|ε|(12|t|+144|ε|)/τ`.

In particular, if `|t|,|ε|≤c₀τ` and `L≤(7−16c₀)/(312c₀²)`, then `E_σ−E_1≥7τ`.

*Proof.* Put `S_b=(ε/τ)Σ_aT_{b,a}K_{b,a}` and `S=Σ_bS_b`. By Lemma B.1, `S*=−S`, `‖S_b‖≤(|ε|/τ)·8·(1/4)=2|ε|/τ`, `S_b` is supported on `b`, and `[H_M,S]=εT^≠` with `T^≠=Σ_{b,a}T^≠_{b,a}`. Write `H_ε=H_M+K_0+εT^≠` with `K_0=Σ_bk_b`, `k_b=−t·(\text{light hop of }b)+εΣ_aT^0_{b,a}`, so `‖k_b‖≤|t|+8|ε|`. The Duhamel formula `e^SXe^{−S}=X+∫_0^1e^{uS}[S,X]e^{−uS}du`, applied to `H_ε` and then to `−εT^≠=[S,H_M]` inside the integral, gives

`e^SH_εe^{−S} = H_M + K_0 + R_1`,  `R_1=∫_0^1e^{uS}([S,K_0]+u[S,εT^≠])e^{−uS}du`.

Even operators with disjoint supports commute, so `[S_b,k_{b′}]=0` unless `b′` meets `b`; three bonds meet each `b`. Hence `‖[S,K_0]‖≤3L·2·(2|ε|/τ)(|t|+8|ε|)` and `‖[S,εT^≠]‖≤3L·2·(2|ε|/τ)·8|ε|`. Since `e^{uS}` is unitary, `‖R_1‖≤12L|ε|(|t|+8|ε|)/τ+48Lε²/τ=L|ε|(12|t|+144|ε|)/τ`.

Now apply Theorem A with `U=e^S` (it commutes with every `U_g` and the holonomy by Lemma B.1(iv)), `V′_b=k_b` and `R=R_1`. By Lemma B.1(i), `k_b` commutes with `P^+_b`, and its compression is `ℓ_b=−t·(\text{light hop of }b)`, because `P^+_bT^0_{b,a}P^+_b=0`. So `δ_b=‖εΣ_aT^0_{b,a}‖≤8|ε|`, `d≤16|ε|≤14τ`, and `H_eff=h^{(w)}`, the free light ring. Theorem A gives the bound. For the last claim, `2L|ε|(12|t|+144|ε|)/τ≤312Lc₀²τ≤(7−16c₀)τ`. `□`

**Remark B.2 (what the remainder contains).** The leading part of `R_1` is `[S,H_L]`. Its terms at the bond `b` create a mirror pair on `b` from the vacuum, with an amplitude of order `ε t/τ`, while a light particle hops on a neighbouring bond. Acting on `Ψ₀=e_vac⊗φ`, terms at bonds far apart produce orthogonal vectors (different pair positions). So `‖R_1Ψ₀‖` grows like `√L` whenever one bond's term is nonzero on `Ψ₀`. This is a formal reading of the leading term, not a proved lower bound on `‖R_1‖`. It shows why no finite-order local dressing can make the `L`-dependence of Theorem A's `2‖R‖` disappear: the vacuum fluctuations are removed only to a finite order, and what is left acts at every bond. This is route 1 of `SMG15.md` §8 (line 158), now with explicit constants.

### 4.3 Theorem C: resonances in a local block step

A convergent local Schrieffer-Wolff (Lie-Schwinger) scheme removes, arc by arc, the part of the effective interaction that maps `Ran P^+_I` into `Ran Q_I`. On an arc `I` it solves `[G_I,X]=−(Q_IYP^+_I+P^+_IYQ_I)` for an operator `G_I` supported on `I` that commutes with `P^+_I`. The light hops inside `I` commute with `P^+_I`, so they belong to such a `G_I`. This section takes the smallest such choice and shows what it meets.

Let `I` be an arc of `ℓ` sites, `2≤ℓ≤L−1`, and

`G_I = Σ_{x∈I}τ(W_x+14) − tΣ_{b⊂I}(\text{light hop of }b)`.

If `I` contains the wrap bond, the factor `w` on it is removed by the gauge change `c_y↦−c_y` for the sites of `I` after that bond; spectra are unchanged. Let `n=⌊ℓ/2⌋`. Let `𝓗_+` be the mirror vacuum of `I` with `n` light particles on `I`, and `𝓗_pair` the configuration `(ρ_a,ρ_a,1,…,1)` on `I` (pair on the first bond of `I`, which `T_{b,a}` creates from the vacuum) with `n` light particles on `I`. Let `ε_k=−2t cos(πk/(ℓ+1))`, `k=1,…,ℓ`, and `E_A=Σ_{k∈A}ε_k` for `A⊂{1,…,ℓ}`.

**Theorem C.** Let `t≠0`, `τ>0`.

(i) `spec(G_I|𝓗_+)={E_A:|A|=n}` and `spec(G_I|𝓗_pair)={28τ+E_B:|B|=n}`.

(ii) Put `E_min=min_{|A|=n}E_A` and `E_max=max_{|A|=n}E_A`. Every point of `[E_min,E_max]` lies within `π|t|/(ℓ+1)` of some `E_A`, and `E_max−E_min≥|t|(ℓ−1)`.

(iii) If `ℓ≥1+28τ/|t|`, some `λ∈spec(G_I|𝓗_+)` and `μ∈spec(G_I|𝓗_pair)` satisfy `|λ−μ|≤π|t|/(ℓ+1)`. So the inverse of `X↦[G_I,X]` on operators `𝓗_+→𝓗_pair`, where it exists, has norm at least `(ℓ+1)/(π|t|)`.

(iv) For every `c₀>0`, the set of `t∈[−c₀τ,c₀τ]` at which some `ℓ` gives `spec(G_I|𝓗_+)∩spec(G_I|𝓗_pair)≠∅` is dense in `[−c₀τ,c₀τ]`. At such `t`, `[G_I,X]=Y` has no solution `X:𝓗_+→𝓗_pair` when `Y` has a nonzero matrix element between the two coinciding eigenvectors.

*Proof.* (i) `G_I` preserves the mirror configuration of `I`. On `𝓗_+` the atoms contribute `0`; on `𝓗_pair` they contribute `14τ+14τ`. The light part is the open hopping chain on `ℓ` sites. Its one-particle eigenvectors `j↦sin(πkj/(ℓ+1))` have eigenvalues `ε_k`. Its `n`-particle eigenvectors are the Slater determinants, with energies `E_A`.

(ii) Take `t>0`; for `t<0` reverse the labels. Then `ε_1<ε_2<…<ε_ℓ`. Starting from `A_0={1,…,n}`, raise the largest element of the set by one level until it reaches `ℓ`, then the next one until it reaches `ℓ−1`, and so on, ending at `{ℓ−n+1,…,ℓ}`. Each step changes the energy by `ε_{k+1}−ε_k=2t(cos(πk/(ℓ+1))−cos(π(k+1)/(ℓ+1)))∈(0,2πt/(ℓ+1)]`, since `|cos α−cos β|≤|α−β|`. The energies run from `E_min` to `E_max` with steps at most `2πt/(ℓ+1)`, which proves the first claim. For the width, `ε_{ℓ+1−k}=−ε_k` gives `E_max−E_min=4tΣ_{k=1}^n cos(πk/(ℓ+1))`. On `[0,1/2]`, `cos(πu)≥1−2u` (the chord of a concave function), and `k/(ℓ+1)≤1/2`. So the sum is at least `n−n(n+1)/(ℓ+1)`, which equals `ℓ²/(4(ℓ+1))` for even `ℓ` and `(ℓ−1)/4` for odd `ℓ`; both are at least `(ℓ−1)/4`.

(iii) Take `μ=28τ+E_min`. If `28τ≤|t|(ℓ−1)`, then `μ∈[E_min,E_max]`, and (ii) gives `λ`. For eigenvectors `u∈𝓗_+` (eigenvalue `λ`) and `v∈𝓗_pair` (eigenvalue `μ`), `[G_I,|v⟩⟨u|]=(μ−λ)|v⟩⟨u|`.

(iv) Coincidence means `28τ=E_A−E_B=t·g(A,B)` with `g(A,B)=2Σ_{k∈B}c_k−2Σ_{k∈A}c_k`, `c_k=cos(πk/(ℓ+1))`. By (ii) for `t>0`, the numbers `g(A_j,A_0)` along the chain run from `0` to at least `ℓ−1` with steps at most `2π/(ℓ+1)`. Given `0<a<b≤c₀τ`, pick `ℓ` with `2π/(ℓ+1)<28τ/a−28τ/b` and `ℓ−1≥28τ/a`. Then some chain value `g` lies in `(28τ/b,28τ/a)`, and `t=28τ/g∈(a,b)` gives a coincidence. Negative `t` is the mirror image. At a coincidence, `⟨v,[G_I,X]u⟩=(μ−λ)⟨v,Xu⟩=0` for every `X`. `□`

**Remark C.1 (what this does to attack 2).** The coincidences are real. On an arc of length `ℓ≳28τ/|t|`, the light band of the arc can absorb the `28τ` of a mirror pair. In a ground state such processes are only virtual. But an exact block form on the whole space, as Theorem A asks, must also hold on states where the arc's light is excited; there the pair and the light excitations resonate. The rigorous lower bound (iii) grows only linearly in `ℓ`; alone it would not stop a scheme whose interactions decay exponentially in `ℓ`. What stops the scheme is (iv): no lower bound on the distance between the two spectra holds on an open set of `t`. One can instead leave the light hops out of `G_I`. Then each step is solvable with denominators at least `4τ` (Lemma B.1), but commutators with the light hops reappear in the next order, as `[S,H_L]` did in Proposition B. Iterating raises the light degree of the terms. That this iteration is only asymptotic, with remainders that are small but act at every bond, is the prethermal picture of Abanin-De Roeck-Ho-Huveneers (arXiv:1509.05386); it is not proved here.

### 4.4 Theorem D: absolute linked sums of the light diverge

Take the free light ring `h=h^{(−1)}`, `t≠0`, `L∈4N`, `L≥8`. Extend the modes by `c_{x+L}=−c_x`. Then `h=−tΣ_{x∈Z_L}(c_x†c_{x+1}+c_{x+1}†c_x)`. Define the translation-covariant bond operators `Λ̃_x=c_x†c_{x+1}+c_{x+1}†c_x`, `x∈Z_L`. So `Λ̃_x=Λ_x` for `x≤L−2` and `Λ̃_{L−1}=−Λ_{L−1}`. By `SMG15.md` Theorem 3, the half-filled ground state `Φ₀` of `h` is unique, with energy `E_L`. For `s≥0` put

`C(x,s)=⟨Φ₀,Λ̃_x e^{−s(h−E_L)}Λ̃_0Φ₀⟩−⟨Φ₀,Λ̃_xΦ₀⟩⟨Φ₀,Λ̃_0Φ₀⟩`.

**Theorem D.** (i) `Σ_{x∈Z_L}C(x,s)=0` for every `s≥0`. (ii) `Σ_{x∈Z_L}(−1)^xC(x,s)≥0` for every `s≥0`, and

`∫_0^∞Σ_{x∈Z_L}(−1)^xC(x,s)ds ≥ log(L/4+1)/(2π|t|)`.

(iii) Hence `Σ_{x∈Z_L}∫_0^∞|C(x,s)|ds ≥ log(L/4+1)/(2π|t|)`.

*Proof.* Let `K=(2π/L)(Z+1/2)` mod `2π` and `c_x=L^{−1/2}Σ_{k∈K}e^{ikx}c_k`; this respects `c_{x+L}=−c_x`. Then `h=Σ_kε_kc_k†c_k` with `ε_k=−2t cos k`. Take `t>0`. Since `L∈4N`, no `k∈K` has `cos k=0`, and the set `O={k∈K: cos k>0}` has `L/2` elements. So `Φ₀=∏_{k∈O}c_k†|0⟩` up to phase. A direct substitution gives

`Λ̃_x=(1/L)Σ_{q,k∈K}(e^{ik}+e^{−iq})e^{i(k−q)x}c_q†c_k`.

For `k∈O`, `q∉O`, the vectors `c_q†c_kΦ₀` are orthonormal eigenvectors of `h` with eigenvalues `E_L+ε_q−ε_k`; all other `c_q†c_kΦ₀` vanish or equal `Φ₀` (when `q=k∈O`). The `Φ₀`-component of `Λ̃_xΦ₀` is `⟨Λ̃_x⟩Φ₀`. Hence

`C(x,s)=(1/L²)Σ_{k∈O,q∉O}|e^{ik}+e^{−iq}|²e^{−i(k−q)x}e^{−s(ε_q−ε_k)}`.

Since `k−q∈(2π/L)Z`, `Σ_xe^{−i(k−q)x}=L` if `k=q` and `0` otherwise. Here `k≠q`, which proves (i). For (ii), `Σ_x(−1)^xe^{−i(k−q)x}=L` if `q=k−π` and `0` otherwise. For `k∈O`, `q=k−π` has `cos q=−cos k<0`, so `q∉O`; then `|e^{ik}+e^{−iq}|²=|e^{ik}−e^{−ik}|²=4sin²k` and `ε_q−ε_k=4t cos k>0`. So

`Σ_x(−1)^xC(x,s)=(1/L)Σ_{k∈O}4sin²k·e^{−4ts cos k}≥0`,  `∫_0^∞Σ_x(−1)^xC(x,s)ds=(1/(tL))Σ_{k∈O}sin²k/cos k`.

By `k↦−k`, the last sum is twice the sum over `k∈O`, `k>0`. For those `k`, `u=π/2−k=2πm/L` with `m∈{1/2,3/2,…,L/4−1/2}`, and `sin²k/cos k=cos²u/sin u`. Keep only `u≤π/4`, that is `m≤L/8`; there `cos²u≥1/2` and `sin u≤u`, so `cos²u/sin u≥L/(4πm)`. At least `L/8` half-integers `m=i+1/2` satisfy `m≤L/8`, and `Σ_{i=0}^{M−1}1/(i+1/2)=2Σ_{i=0}^{M−1}1/(2i+1)≥log(2M+1)`, because `1/(2i+1)≥∫_i^{i+1}dx/(2x+1)`. With `M≥L/8` this is at least `log(L/4+1)`. So `Σ_{k∈O}sin²k/cos k≥2(L/(4π))log(L/4+1)`, which gives (ii). For `t<0`, `O={cos k<0}`; the same pairing `q=k−π` and the substitution `k↦k−π` give the same bound with `|t|`. (iii) follows from `Σ_x|C(x,s)|≥|Σ_x(−1)^xC(x,s)|` and Tonelli. `□`

**Remark D.1 (the insertions of short vacuum pairs).** A vacuum pair created and removed on the bond `x` within a time of order `1/τ` carries the light insertion `Λ_x(s₁)Λ_x(s₂)≈Λ_x²=n_x+n_{x+1}−2n_xn_{x+1}`. Wick ordering in `Φ₀`, where `⟨n_x⟩=1/2` and `G₁=⟨c_x†c_{x+1}⟩=(1/L)Σ_{k∈O}cos k` is real, gives `Λ_x²=const+2G₁:Λ_x:−2:n_xn_{x+1}:` (the density terms cancel at half filling). So the link between two such pairs contains `4G₁²C(x,s)`, with `G₁→1/π`. The quartic part is not estimated here.

**Remark D.2 (what this does to attack 1).** Any polymer or cluster bound that takes absolute values of the light connected correlations between two mirror polymers before summing over the second polymer's position meets the sum in (iii). That sum grows like `log L`, so no `L`-uniform Kotecký-Preiss or Dobrushin condition (`SGAP0.md` Theorem 4) holds after absolute values. The uniform part cancels exactly by (i). The staggered (`2k_F=π`) part does not cancel: by (ii) even its signed time integral grows like `log L`. This is the Peierls instability of the half-filled chain. It sharpens route 2 of `SMG15.md` §8 (line 159), which named a possible `|z|⁻²` contribution without computing it, and it matches the convergence condition of Salmhofer-Wieczerkowski (arXiv:math-ph/9909002), a summable propagator, which the massless light chain violates.

### 4.5 Lemma E: localized charge removal

Write a vector of the `σ`-sector as `Ψ=Σ_ξe_ξ⊗ψ_ξ`, `ψ_ξ∈𝓕` (one holonomy; the other is treated the same way). A **localizer at `y`** is a real configuration-diagonal operator `χ_y` (a function `ξ↦χ_y(ξ)`, acting as `χ_y⊗1`) with `χ_y(ξ)=0` unless `ξ_y=σ`. For a family `χ=(χ_y)_y` put `w_χ=Σ_y‖χ_yΨ‖²` and define its **flux**

`Φ(χ)=Σ_yΣ_{x,a}Σ_ξ(χ_y(ξ^{x,a})−χ_y(ξ))²‖ψ_{ξ^{x,a}}‖‖ψ_ξ‖`.

**Lemma E.** Let `σ∈Ŝ_+∖{1}` and let `Ψ` be a normalized vector with `H_εΨ=E_σΨ`. For every family of localizers with `w_χ>0`,

`E_σ − E_1 ≥ 16τ − |ε|Φ(χ)/(2w_χ)`.

*Proof.* Fix `y`. Choose `a≠b` with `σ=ρ_aρ_b` and put `Y_y=iγ_{y,a}γ_{y,b}`. By `SGAP.md` Theorem 3, `Y_yχ_yΨ` is neutral and half-filled, has norm `‖χ_yΨ‖`, and `⟨Y_yχ_yΨ,H_εY_yχ_yΨ⟩=⟨χ_yΨ,(H_ε+B_y)χ_yΨ⟩`. Since `χ_y=P^σ_yχ_y=χ_yP^σ_y`, only `P^σ_yB_yP^σ_y` enters. Its atomic part is `−16τP^σ_y`. Its bond part vanishes, because each bond term of `B_y` changes the character at `y`. So the variational principle gives `E_1‖χ_yΨ‖²≤⟨χ_yΨ,H_εχ_yΨ⟩−16τ‖χ_yΨ‖²`. For real diagonal `χ`, `χHχ=(χ²H+Hχ²)/2+[χ,[H,χ]]/2`; with `H_εΨ=E_σΨ` this gives `⟨χ_yΨ,H_εχ_yΨ⟩=E_σ‖χ_yΨ‖²+⟨Ψ,[χ_y,[H_ε,χ_y]]Ψ⟩/2`. Only `εH_4` fails to commute with `χ_y`. A matrix element of `[χ,[V,χ]]` between configurations `ξ′,ξ` equals `−(χ(ξ′)−χ(ξ))²V_{ξ′ξ}`, and `|⟨ψ_{ξ^{x,a}},Λ_xψ_ξ⟩|≤‖ψ_{ξ^{x,a}}‖‖ψ_ξ‖`. So `|⟨Ψ,[χ_y,[εH_4,χ_y]]Ψ⟩|` is at most `|ε|` times the `y`-term of `Φ(χ)`. Sum over `y`. `□`

With `χ_y=P^σ_y` this is `SGAP.md` Theorem 5 (Lemma R) in a different arrangement; there the flux counts every move into or out of a `σ` line, including the `σ` lines of neutral fluctuations far from the charge, which is the failure recorded as A4 (`SGAP.md` line 141).

**Proposition E.2 (window localizers are fooled; exact part).** Fix `r≥0`. Let `χ_y` depend only on the configuration in the window `W_y=[y−r,y+r]` and equal `1` on the window content "`σ` at `y`, vacuum elsewhere in `W_y`". Let `ξ_f` be any configuration that has `ρ_a` at `y−r−1`, `σ=ρ_aρ_b` at `y`, `ρ_b` at `y+r+1`, and vacuum elsewhere on `[y−r−1,y+r+1]`. Then (i) `χ_y(ξ_f)=1`; (ii) the three named sites have product character `1`, so they form a neutral group; (iii) their atomic energy is `14τ+16τ+14τ=44τ`, and removing the `σ` at `y` leaves `28τ`. So the removal at `y` releases `16τ` from a group that costs `44τ`; the neutral trial vector it produces still carries the `28τ` group.

*Proof.* (i): the window content of `ξ_f` is the named one. (ii): `ρ_a·ρ_aρ_b·ρ_b=1`. (iii): `SMG1.md` Theorem 2.2. `□`

**Formal estimate (not proved).** Such a group is produced from the vacuum by `2r+2` moves (one pair on each side of `y`, each end moved `r` steps outward), each with an energy denominator between `14τ` and `44τ`. Formally its amplitude is of order `(ε/(Cτ))^{2r+2}` per site, so the total weight of fooled windows in `Ψ` is of order `L(ε/(Cτ))^{4r+4}`. For a fooled window, the localized vector `χ_yΨ` sits on a virtual group, so its contribution to the flux is of order `(44τ/|ε|)` times its weight. Lemma E then loses about `44τ` times (fooled weight)/(true weight), which grows without bound as `L→∞` at fixed `r`. A window that grows with `L` makes `χ_y` read far-away configurations; then far-away moves change `χ_y` and enter the flux. This dilemma is where attack 3 stops (section 5.3).

## 5. The three named attacks

Each attack aims at the residual lemma SGAPT-R (section 5.4), the defect form of S-GAP at `t≠0`. Each is recorded with its route, its failed estimate and the parameter domain of the failure, as Lane brief 1 asks (line 1202).

### 5.1 Attack 1: a charged polymer ratio with fermion determinants retained

**Route.** Expand `e^{−βH_ε}` in `εH_4`, keeping `H_M+H_L` exact. The light factor of a mirror history `h` is the time-ordered free expectation `⟨T∏_iΛ_{x_i}(s_i)⟩_L`, after division by `Z_L=Tr e^{−βh}`, the full moving-light partition function. So `Z_χ/Z_L=Σ_{h:q(h)=χ}w_M(h)⟨T∏_{i∈h}Λ_{x_i}(s_i)⟩_L`. The normalized light factor of any history has modulus at most `1` (the generalized Hölder inequality for traces, cited and not rebuilt; this is used in remarks only). As in `SGAP0.md` Theorem 2, a charged history has a charged winding component. The plan, from `SMG1_TREE.md` line 797, is to cancel the neutral histories that do not detect the charge and to bound the rest.

**Where it differs from P7.** In `SGAP0.md` the activities factorize over shadow components (Theorem 2 there), because at `t=0` the light is slaved to the mirror. Here the light factor of a union of components is not the product of their light factors. Its truncated (connected) parts link components that are far apart in space-time. Cancelling the neutral histories therefore needs a Dobrushin or Kotecký-Preiss condition for a linked gas, in which a link carries a truncated light correlation.

**Failed estimate.** The condition needs `Σ_{γ′}|link(γ,γ′)|μ(γ′)≤C|γ|` with `C` independent of `L`. For two short vacuum pairs, the link contains `4G₁²C(x,s)` (Remark D.1). Theorem D(iii) shows that the sum of `|C(x,s)|` over the position `(x,s)` of the second pair is at least `log(L/4+1)/(2π|t|)`. So, after absolute values, the left side grows at least like `log L` times the pair activities, of order `(ε/τ)²` each; the quartic remainder of Remark D.1 is not estimated. The uniform part cancels exactly (Theorem D(i)); the staggered part does not, even with signs (Theorem D(ii)).

**Domain of the failure.** Every `t≠0`, `ε≠0` and allowed `L`: the growth in `L` in Theorem D does not disappear as `t,ε→0`. A repair would have to keep the sign structure of the staggered light response at all scales, which is a multiscale (renormalization group) treatment of the light chain. Section 5.6 records why such a treatment, as far as found, does not cover the full square.

### 5.2 Attack 2: a defect-relative local Schrieffer-Wolff inequality

**Route.** Theorem A turns any defect-relative block form `UH_εU*=H_M+Σ_IV′_I+R` into the bound `E_σ−E_1≥14τ−d−2‖R‖`, with no infrared input. The attack seeks `U` with `d` small and `‖R‖` bounded uniformly in `L`.

**What it gives.** At first order, Proposition B gives `d≤16|ε|` and `‖R‖≤L|ε|(12|t|+144|ε|)/τ`, hence `E_σ−E_1≥7τ` on rings with `L≤(7−16c₀)/(312c₀²)`. It is an explicit charged gap at `tε≠0` that holds only on finite rings.

**Failed estimate.** `‖R‖≤rτ` with `r` independent of `L`. At finite order the remainder acts at every bond (Remark B.2; formal at higher order), so `‖R‖` grows with `L`. A convergent arc-by-arc scheme that keeps the light hops in the local operator meets the resonances of Theorem C: on every arc of length `ℓ≥1+28τ/|t|` the vacuum block and the pair block come within `π|t|/(ℓ+1)` of each other, and for a dense set of `t` they coincide exactly, so the step has no solution unless a matrix element vanishes. A scheme that leaves the light hops out of the local operator avoids these resonances in each step but regenerates commutators with the light hops at the next order (Remark C.1).

**Domain of the failure.** Finite order: every `tε≠0` and every `L`, with the explicit range of Proposition B. Convergent form: every `t≠0` with rings of length `L≥2+28τ/|t|`, and exact coincidences on a dense set of `t` in every `[−c₀τ,c₀τ]`. At `t=0` the resonance of Theorem C does not occur, because the arc operator then has the vacuum block at `0` and every other block at `14τ` or more. The finite-order remainder of Proposition B is still proportional to `L` there.

### 5.3 Attack 3: a sector-aware localized charge-removal comparison

**Route.** Lemma E compares each charged ground vector with neutral vectors in the true neutral sector (as N11 of the tree asks, line 620: "Retain the global sector constraint in the comparison"). It removes the charge where a localizer says it is. S-GAP follows once one family of localizers has `w_χ≥1/2` and flux `Φ(χ)≤K`, uniformly in `L` (Lemma LOC, section 5.4).

**Failed estimate.** `Φ(χ)≤K` uniformly in `L`. For `χ_y=P^σ_y` this is A4's bound, which `SGAP.md` line 141 leaves unproved. A localizer that reads a window of fixed radius `r` cannot tell the charge from a neutral group `(ρ_a, vacuum^r, σ, vacuum^r, ρ_b)` with the same window content (Proposition E.2, exact). Removing the `σ` of such a group releases `16τ` from a group that costs `44τ`, so each fooled window adds a large positive term to the flux. Formally, fooled windows have total weight of order `L(ε/(Cτ))^{4r+4}` (not proved), which beats a bounded true weight as `L→∞`. A localizer whose window grows with `L` is changed by moves far from `y`, and those moves enter the flux; no bound on their total was found.

**Domain of the failure.** Every `ε≠0`, any `t`, including `t=0`. The failure does not involve the light; it is the same failure as A4 at `t=0`, where `SGAP0.md` succeeded by polymers instead.

### 5.4 The residual lemma and the smallest sufficient sub-lemma

**Residual lemma SGAPT-R (open; attacks 1-3 failed).** There are `c₀,Δ>0` such that for every allowed `L`, every `τ>0`, every `t` with `0<|t|≤c₀τ`, every `|ε|≤c₀τ` and every `σ∈Ŝ_+∖{1}`, the bottom of `H_ε+B_σ` on the neutral half-filled sector exceeds the bottom of `H_ε` there by at least `Δτ`.

By `SGAP.md` Theorem 3 and line 58, SGAPT-R is S-GAP restricted to `t≠0`. Together with S-GAP⁰ (`SGAP0.md` Theorem 9) it gives S-GAP, with the smaller of the two `c₀` and the smaller `Δ`. It restates the frozen target; it adds no structure.

**Smallest sufficient sub-lemma found, LOC.** There are `c₀>0` and `K<∞` such that for every allowed `L`, `τ>0`, `|t|,|ε|≤c₀τ` and `σ≠1`, some normalized `σ`-ground vector `Ψ` and some family of localizers with `0≤χ_y≤1` (section 4.5) satisfy `w_χ≥1/2` and `Φ(χ)≤K`.

By Lemma E, LOC gives `E_σ−E_1≥16τ−|ε|K≥(16−c₀K)τ`, hence S-GAP with `Δ=16−c₀K` once `c₀<16/K`. LOC concerns one ground vector and one family of diagonal operators. It needs no light correlation and no operator identity on the whole space. For `χ_y=P^σ_y` it is A4's open bound (`SGAP.md` line 141). For every window localizer it fails at a formal level (Proposition E.2). An adaptive localizer, one that reads as far as needed to pair neutral groups and is still changed by few far-away moves, is the open construction.

*Remark (formal; guidance only).* Arc products `π_{[u,v]}(ξ)=∏_{u≤z≤v}ξ_z` see the difference that a window cannot. Inside the fooling group of Proposition E.2, the arc products that start at `y−r−1` take the values `ρ_a`, then `ρ_b`, then `1`; none of them equals `σ`. Across the true charge, the arc product changes from `1` to `σ` and stays `σ`. A localizer that asks for "arc product `1` on long arcs to the left of `y`, and `σ` on long arcs that cross `y`" is not fooled by such groups. It is fooled by neutral `σ`-`σ` pairs at separation `r`, whose formal amplitude carries `r` factors of a `σ` hop, each of order `ε²/τ²`. Whether such a localizer has bounded flux needs a priori bounds on extended neutral groups in the charged ground state; none is proved here. The other sufficient condition met here is Theorem A's block form with `d` and `‖R‖` bounded uniformly; Theorem C shows that its natural convergent construction meets resonances.

**Four tests.** This file proposes no reading, specification or law text. SGAPT-R restates the frozen target. LOC, the block form of Theorem A, `d`, `δ_I`, `w_χ` and `Φ(χ)` are mathematical notation for sufficient conditions; none is offered for adoption, so none is four-tested as a candidate.

### 5.5 Check of the tree's node S

The tree says of itself "nobody has checked it" (line 1). Checked here against the frozen files: P5 matches `SMG15.md` Theorem 3 (lines 62-66); P6 matches `SMG15.md` Theorem 7 (lines 136-140); P7 matches `SGAP0.md` Theorem 9 (lines 150-152), with `c₀=2·10⁻¹⁰` and `Δ=7`; node S's statement (lines 769-789) matches `SGAP.md` Definition 4. The literature locators of LFP ("Theorem 3.5"), LRG1 ("Theorem 1.1") and LSW (arXiv:1105.0675) were not checked against full texts (**NOT VERIFIED**). For LY, the fetched abstract of arXiv:math-ph/0411042 concerns quasi-particles; the tree's description "Product-state stability and thermodynamic ground-state construction" was not matched (**NOT VERIFIED**).

**The two "smallest rungs" do not contain the difficulty.**

- Line 803, "One charged winding history with arbitrary free light propagation": the normalized light factor of any history has modulus at most `1` (Hölder for traces, cited). The rung reduces to a sum of positive mirror weights, which contains no light. The difficulty sits in the neutral histories of the denominator and their light links (Theorem D).
- Line 811, "A two-bond charged cluster coupled to an arbitrarily long free light chain": replace `εH_4` by its terms on two bonds, of norm at most `16|ε|`. At `ε=0` the charged gap is exactly `16τ` for every `L` (`SGAP.md` Theorem 2). Weyl's inequality in each sector then gives `E_σ−E_1≥16τ−32|ε|` for every `L`. The difficulty is that `H_4` acts on all `L` bonds at once.

### 5.6 The square and the light's infrared (formal; not proved)

`SMG15.md` Theorem 7 gives the formal second-order light operator `−tΣ_x hop_x−(4ε²/(7τ))N+(4ε²/(7τ))Σ_xn_xn_{x+1}` (line 140). By Jordan-Wigner this is an XXZ chain with anisotropy `Δ_XXZ=2ε²/(7τ|t|)` at fixed `N`. That the XXZ chain is gapless for `|Δ_XXZ|≤1` and gapped for `Δ_XXZ>1` is credited from memory (**NOT VERIFIED**). For every `c₀>0`, the point `ε=c₀τ/2`, `t=c₀²τ/14` lies in the square and has `Δ_XXZ=1`. So the square contains, at the formal level, the point where the light chain changes from a Luttinger liquid to a charge-density wave; Theorem D's staggered logarithm is the signature of that competition.

Consequences, all formal. A multiscale treatment of the light, of the kind checked in section 2 for weak interactions (Benfatto-Mastropietro), would aim at a weak-interaction wedge, here named **S-GAP-LL**: `ε²≤κτ|t|`. A two-scale contour treatment around the charge-density wave, after `SGAP0.md`, would aim at **S-GAP-CDW**: `|t|≤κε²/τ`. Neither is proved or proposed here, and neither reaches the strip around `|t|=2ε²/(7τ)` by the results checked. Theorem A and Lemma E need no infrared control of the light; they are the routes found that could cover the whole square, and each stops at the step recorded in sections 5.2-5.3.

## FINISH

**Proved (pass 1; author-side, not distilled or refereed).**

- Lemma A.0: the vacuum compression `ℓ` of an operator supported on an arc exists, is unique, and has `‖ℓ‖≤‖V‖`.
- Theorem A: a symmetric unitary with `UH_εU*=H_M+Σ_IV′_I+R`, each `V′_I` supported on an arc and commuting with that arc's mirror-vacuum projector, gives `E_σ−E_1≥14τ−d−2‖R‖` for every `σ≠1` and every `L`, with no infrared input. Remark A.2: this contains the charged bound of `SMG15.md` Theorem 3.
- Lemma B.1 and Proposition B: `E_σ−E_1≥14τ−16|ε|−2L|ε|(12|t|+144|ε|)/τ` for all `L`, `t`, `|ε|≤7τ/8`. So `E_σ−E_1≥7τ` on rings with `L≤(7−16c₀)/(312c₀²)` when `|t|,|ε|≤c₀τ`. This is a finite-ring result, not S-GAP.
- Theorem C (i)-(iv): on arcs of length `ℓ≥1+28τ/|t|`, the vacuum and pair blocks of the arc operator `G_I` have eigenvalues within `π|t|/(ℓ+1)`; exact coincidences occur for a dense set of `t` in every `[−c₀τ,c₀τ]`.
- Theorem D: in the free half-filled light ring, `Σ_xC(x,s)=0`, `Σ_x(−1)^xC(x,s)≥0`, and `Σ_x∫_0^∞|C(x,s)|ds≥∫_0^∞Σ_x(−1)^xC(x,s)ds≥log(L/4+1)/(2π|t|)`.
- Lemma E: `E_σ−E_1≥16τ−|ε|Φ(χ)/(2w_χ)` for every family of localizers; Proposition E.2: the exact part of the fooling of window localizers.
- Section 5.5: the tree's two-bond rung holds with `E_σ−E_1≥16τ−32|ε|` for every `L`; its one-history rung reduces to a mirror-only sum, using the cited Hölder inequality for traces.

**Counterexamples.** None to S-GAP, SGAPT-R or LOC, and none expected. Refuted estimates: the `L`-uniform absolute linked-sum bound that attack 1 needs (Theorem D); uniform spectral separation in the arc step of attack 2's convergent form (Theorem C).

**Open by name.**

- **SGAPT-R**, S-GAP at `t≠0` in defect form. Attacks failed: (1) charged polymer ratio with fermion determinants retained, at the absolute linked sum (Theorem D; every `tε≠0`, every `L`); (2) defect-relative local Schrieffer-Wolff inequality, at the remainder (Proposition B; finite order) and at the arc step (Theorem C; convergent form, `t≠0`); (3) sector-aware localized charge removal, at the localizer (Proposition E.2; every `ε≠0`).
- **LOC**, the smallest sufficient sub-lemma found (section 5.4).
- Formal statements not proved: the growth of finite-order remainders at higher order (Remark B.2); the extensive weight of fooled windows (section 4.5); the XXZ reading of the light and its isotropic point inside the square (section 5.6).
- Named weaker theorems, not worked and not proposed: **S-GAP-LL** (`ε²≤κτ|t|`) and **S-GAP-CDW** (`|t|≤κε²/τ`).

**What changes downstream.**

- Node S stays OPEN, and `SGAP.md`'s "S-GAP at `t≠0`" stays open, now with three named failed attacks, the residual lemma SGAPT-R and the sub-lemma LOC. Nothing is adopted; no frozen file, axiom, law or working-set entry changes.
- Node D asks for "a positive charged mirror gap in the same model" in its weak-interaction wedge (`SMG1_TREE.md` lines 821-831). That is S-GAP-LL, not the full square. A multiscale route could aim at D and S-GAP-LL together.
- Theorem A is a criterion that other rungs (D, R2, R3) can reuse: a defect-relative block form with a bounded remainder gives a charged gap whatever the light's infrared behaviour.
- Theorem D is special to one spatial dimension. By power counting (formal, not proved), a massless Dirac bath in `2+1` or `3+1` dimensions has bilinear links decaying like `|z|⁻⁴` or `|z|⁻⁶`, which are absolutely summable over space-time. So, at this formal level, the obstruction to attack 1 found here does not arise for node R3's smallest rung or for node M.
- Proposition B gives an explicit charged gap at `tε≠0`, on finite rings only. It supplies no uniform statement to R15-SPEC's S1, to D or to R2.
- Downstream items listed as open in `SGAP0.md` line 164 are unchanged.
