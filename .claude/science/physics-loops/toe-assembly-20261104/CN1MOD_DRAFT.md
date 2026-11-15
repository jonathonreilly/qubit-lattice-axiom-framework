lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CN1MOD: the speed difference under one massive U(1) field, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as a pass-1 lane of the TOE assembly (wall W3, the smallest sub-lemma of R1-MOD in `CN1.md`). Method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-CN1MOD/`. A check guides and never proves.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `9137b3783` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd0` |
| `origin/docs/consolidate-gauge-matter-registers` (same way) | `7086189d1` |
| `origin/docs/consolidate-lorentz-dispersion` (same way) | `586d7c81d` |

Files read, by line. This folder: `prior/CN1MOD.md` 1-79 (all); `CN1.md` 1-197 (all); `CN1_REFEREE.md` 1-130, 160, 166, 204, 214, 220, 236-395; `CN1_OUTLINE.md` 280-300 (the R1-D proof, Lemma R1-MOD, attacks 1-4, R1″-MOD); `LZ1.md` 1-33 (status, Amendments 1-4); `LZ1I.md` 1-24 and 178-224 (Theorems 11-12, A1-A4, open items); `ZM1INV.md` 1-40 and 146-185; `TOE_ASSEMBLY.md` 201-266 (sections 3.4-3.10) and 722-736 (section 11); `GA15PHI.md` line 5; `GB1.md` lines 5, 7, 15; `Y2W_DRAFT.md` 1-30 (format; its line 30 also quotes `LW1_5_DRAFT.md` Theorem U, which section 5 uses). `origin/main`: `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` (the "Peierls note") lines 5-9, 38-50, 265-282, 498-517; `docs/WILSON_STAGGERED_RETAINED_GRASSMANN_TWO_LAYER_KP_POLYMER_NORM_BOUNDED_THEOREM_NOTE_2026-07-12.md` (the "K note") lines 11-13, 21-23, 85-88. `origin/docs/consolidate-gauge-matter-registers`: `docs/GAUGE_MATTER_REGISTERS_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 11 and 1189-1193 (the #9943 row). `origin/docs/consolidate-lorentz-dispersion`: `docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 81 and 110-114 (the #9913 entry). The other notes the digest names (the quartet note Q, the Weyl note W, the exchange-matrix note, the Hall note) were not opened; this file uses them only through the digest's quotes and states no result that depends on them.

**Working set used, by name.** None as a premise. The model of section 3 is a supplied lattice model, not a framework law; section 5 says why no law realises it yet. The owner decision ZM1-INV is quoted only where section 5 compares the model with the framework.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The axioms and working-set entries are read plainly. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Inputs from outside the repository.** Standard mathematics, rebuilt in the text: the Cauchy estimate for holomorphic functions (in one variable and along a segment in a complex Banach space), Taylor's formula with remainder, Fubini's theorem in polar coordinates, elementary inequalities for sums and products, the Clifford relations of Euclidean gamma matrices, and moments of the uniform measure on the unit sphere of `R^4`. One imported physics input, exactly as `CN1.md` imports it: the one-loop coefficients of (OL), ported from the Peierls note (conditional-support, unaudited). Literature is in section 2; no citation is a proof step.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 730, wall W3: "Target theorem: under the owner's zoom (ZM1-INV), species that interact through a common gauge field have speed differences that flow to zero. [...] Ladder: rung 1, two species coupled to one U(1) field in a solvable or perturbative-with-bounds model; rung 2, the framework's own gauge layer; rung 3, every species. First rung to work: rung 1."

`CN1.md` line 52, R1-MOD: "**R1-MOD** asks for an exact scale integration in a lattice regularization whose interpolated coefficients obey (OL+ρ) with the §5 bounds uniformly at all scales, with (Sm) at the starting scale and `f + f₁₂ ≤ Ke^{−βℓ}`." `CN1.md` line 58: "R1″ gives the photon a mass and has `N=log(Λ/m_γ)` marginal scales. R1″-MOD asks for bounds uniform in `N`; its finite-scale consequence also requires uniform initial data, smallness and constants in Theorem 3."

`CN1_OUTLINE.md` line 300: "**R1″-MOD:** R1-MOD for M1 with a photon mass `m_γ`, on the `N = log(Λ/m_γ)` scales above `m_γ`, with `K` and `β` independent of `N`. If R1″-MOD holds, Theorem R1-C(a)-(c) applied on `[0, N]` bounds the speed spread at the scale `m_γ` by `C(1+N)^{−γ′}`, uniformly as `m_γ → 0`. Attacks 1-3 meet the same steps there; attack 2's kernel becomes massive, which removes the long-range tail but keeps the marginal coupling across `N` scales."

The lane brief states the target: for two (or n) lattice Dirac species with different bare speeds coupled to one massive U(1) field (mass `m > 0`, small coupling), in a model whose RG can be controlled, prove that the speed difference contracts scale by scale with constants uniform in the number of scales down to the scale `1/m`; or give a counterexample; or give a lemma on which three named attacks, distinct from those on file, fail.

The attacks on file (`CN1.md` line 177; `CN1_REFEREE.md` item 59, which cites the same paragraph as line 162 of an earlier commit). (1) Port the all-orders renormalised expansion of Giuliani–Mastropietro–Porta; fails at the sum over orders. (2) Integrate the Gaussian photon exactly, then run a convergent fermionic expansion; fails at scale-summability of the massless kernel. (3) Ward identities with exchange symmetry; fails at the size estimate. (4) Large `N`; the `1/N` series is not known to converge.

**What this file does, in one paragraph.** Section 3 fixes a lattice model M″ and states R1″-MOD for it in a discrete form. Section 4 proves the following. Theorem 1: per-scale bounds of a stated form give scale-by-scale contraction of the speed difference with constants independent of `N`. Lemma 2 and Theorem 3: exchange symmetry plus a size bound on a complex neighbourhood give the Lipschitz form that attack 3 lacked; so R1″-MOD reduces to one size bound, called UB″. Proposition 4: UB″ cannot hold on a full complex disc of the bare coupling, uniformly in `N`; Proposition 5: it can be posed on a disc tangent to the imaginary axis. Corollary 4″ sharpens Proposition 4 and needs no import. Three new attacks on UB″ then fail at named steps; the first fails at Corollary 4″, which is proved.

## 1. Prior work used

Paths are relative to this folder unless a branch is named. "Status" is the status the source gives itself.

| Prior result | Path and lines | Status there | Use here |
|---|---|---|---|
| The one-loop flow (OL), with `P,R,S` | `CN1.md` lines 65-72 | frozen; coefficients ported from the Peierls note, conditional | Section 3.3, Theorem 3 |
| Theorem 1 (R1-A, global alignment) and its box argument | `CN1.md` lines 78-93 | frozen | Lemma 3a extends the box step to discrete scales |
| Theorem 2 (R1-B, pair exponent `2q²/W`) | `CN1.md` lines 95-100 | frozen | The exponent of Theorem 1 is its discrete form |
| Class `𝓡`, (R-i)-(R-iii), and the sentence "symmetry alone does not give the bound" | `CN1.md` lines 109-117 | frozen | Lemma 2 supplies the missing bound from a complex size bound |
| Theorem 3 (R1-C) and its window proof | `CN1.md` lines 119-129 | frozen | Theorem 1 is a discrete, finite-`N` analogue for the pair |
| Referee closure: convergence for integrable forcing | `CN1.md` line 133 | frozen; referee closure, unrefereed | Not used; cited for scope |
| Proposition 4 (R1-D) and closures R1-D-a, R1-D-b | `CN1.md` lines 135-141 | frozen | Section 3.4: why the difference line of M″ has no source |
| R1, R1-MOD, R1″-MOD, attacks 1-4 | `CN1.md` lines 52, 58, 177; `CN1_OUTLINE.md` lines 291-300 | frozen; outline is pass 1 | The target; distinctness of the new attacks |
| Item 36: exchange symmetry plus a Lipschitz bound gives (R-iii) | `CN1_REFEREE.md` line 204 | referee closure | Lemma 2 replaces the assumed Lipschitz bound by a size bound |
| Item 59: ruling on attacks 1-3 | `CN1_REFEREE.md` line 250 | referee | Standard for a failed attack |
| Theorems 11-12 (integrated drag; marginal rate is not a power) | `LZ1I.md` lines 180-190 | frozen | Theorem 1's rate is a power of `N`, not of `L^N`, as Theorem 12 says it must be |
| Exact polymer norm for the retained gauge–Grassmann logarithm, one step, high mass | K note, `origin/main` lines 11-13, 21-23, 85-88 | conditional, unaudited (digest) | Attack C: a one-step norm exists in a massive regime; the note "does not prove an invariant RG neighborhood" |
| One-loop lattice matching, each remainder "integrates to a finite O(rho_0) value", "Higher-loop control remains open", decaying forcing | Peierls note, `origin/main` lines 265-282, 498-517 | "conditional-support" (line 7) | Section 3.3: the lattice drag correction decays; it enters Theorem 1 as the `e^{−βk}` term |
| #9943: massive (Stueckelberg) photon in a supplied Gaussian, large-register, small-step tick model; exact dressed-hop Ward identity | `origin/docs/consolidate-gauge-matter-registers`, consolidation note line 1191 | "logged"; "author statements for review" (line 11) | Section 5: the nearest framework-side carrier of M″ |
| #9913: one-loop tick velocity logs cancel at matched tree cones; "kappa is a finite lattice constant" | `origin/docs/consolidate-lorentz-dispersion`, consolidation note lines 81, 112 | author-side | Section 3.4: finite matching is initial data, not a source |

**Prior work the digest missed, added here.** (a) `CN1_REFEREE.md` item 36 (line 204) proves the Lipschitz-to-(R-iii) step that Lemma 2 below builds on; the digest quotes only `CN1.md` line 117. (b) The digest's consumer note says that a fixed-mass construction alone "would not meet that handoff" (`prior/CN1MOD.md`, Consumers, citing `CN1.md` line 58). The literature has exactly such fixed-mass constructions in 3+1 dimensions: Mastropietro, arXiv:2001.00183, takes the photon mass `M_a = a^{−1}M` at the cutoff scale (section 2). Proposition 4 shows why they cannot be extended verbatim to `N` scales. (c) A `grep -rl "tangent\|Borel"` over this folder returns only files of other parts (the CH1, LW1, SMG1, VC1 and RCS1 families: chirality, the law, symmetric mass generation, the vacuum, charged sectors). No repository work on the analyticity domain of the bare coupling was found.

## 2. Literature read

Searches run on 2026-11-07 (WebSearch, standard mode): lattice massless fermions with massive vector bosons in `d=4`; Giuliani–Mastropietro–Porta lattice QED for graphene; Balaban–O'Carroll–Schor fermions in an external gauge field; Bauerschmidt–Brydges–Slade renormalisation group and the 4-dimensional weakly self-avoiding walk; Feldman–Magnen–Rivasseau–Sénéor infrared `Φ⁴_4`; Gawędzki–Kupiainen massless lattice `φ⁴_4`; Mastropietro "Emergent Adler-Bardeen theorem"; a general search for a constructive four-dimensional lattice QED. Each work below was fetched at the page named. "Fetched text" means the fetch tool returned the page and I quote from its extraction. Nothing here is a proof step.

| Work | Page fetched | What it says (quoted from the fetched text) | Use here |
|---|---|---|---|
| V. Mastropietro, "Emergent Adler-Bardeen theorem", arXiv:2001.00183, JHEP 03 (2020) 095 | ar5iv HTML | Photon covariance (eq. 15) `v_{μ,ν}(x)=δ_{μ,ν}∫dk χ(k)e^{ikx}/(k²+M_a²)`; "M_a = M in d=1 and M_a = a^{-1}M in d=3 is a regularizing mass"; (before eq. 16) "For a non-perturbative analysis we find convenient to integrate out the boson field getting a purely fermionic theory"; the theorem holds "For small λ"; conclusions: "It would be interesting to establish a similar property removing the mass regularization of photons." | The `N = O(1)` precedent in 3+1 dimensions; attack A |
| S. Fabbri, V. Mastropietro, B. Renzi, "Non-perturbative renormalization for lattice massive QED₂: the ultraviolet problem", arXiv:2602.03705 (3 Feb 2026) | arXiv abstract | Lattice massive QED₂ with a Wilson term, fermion mass `m`, vector mass `M`, `m ≪ M ≪ a^{−1}`; expansions converge for `|e| ≤ e_0` with `e_0` independent of `a` and `m`; the bosons are integrated out | A full-disc bound uniform in the number of scales, in 1+1 dimensions; scope of Proposition 4 |
| V. Mastropietro, "Nonperturbative renormalization of the lattice Sommerfield vector model", arXiv:2203.07652 (Phys. Rev. D 105, 114502, per the DOI on the page) | arXiv abstract | 2D massive vector field and light fermion; "we prove that there is no infinite field renormalization"; convergent expansions uniform in lattice spacing and volume | Same as above |
| A. Giuliani, V. Mastropietro, M. Porta, "Lattice quantum electrodynamics for graphene", arXiv:1107.4741, Ann. Phys. 327 (2012) 461-511 | arXiv abstract | Exact RG; "a renormalized expansion that is finite at all orders"; the Fermi velocity increases to the speed of light; "Lorentz invariance spontaneously emerges in the infrared." | Source of attack 1 on file |
| A. Giuliani, V. Mastropietro, M. Porta, "Anomaly non-renormalization in interacting Weyl semimetals", arXiv:1907.00682 (accepted in CMP, per the page) | arXiv abstract | Interacting 3D lattice Weyl models; result "at a non-perturbative level". The abstract does not state the interaction class. | 3+1 lattice fermions are controlled non-perturbatively for the interactions treated there; which class is NOT VERIFIED |
| R. Bauerschmidt, D. Brydges, G. Slade, "Introduction to a renormalisation group method", arXiv:1907.05474, LNM 2242 (2019) | arXiv abstract | RG map, perturbation theory, norms and "stability analysis" for the 4-dimensional hierarchical `\|φ\|⁴` model; Euclidean nearest-neighbour setting outlined; supersymmetry and the 4-dimensional weakly self-avoiding walk | Template of attack C |
| R. Bauerschmidt, D. Brydges, G. Slade, "Logarithmic correction for the susceptibility of the 4-dimensional weakly self-avoiding walk: a renormalisation group analysis", arXiv:1403.7422, CMP 337 (2015) 817-877 | arXiv abstract | The susceptibility "has a logarithmic correction to mean-field scaling behaviour as the critical point is approached"; supersymmetric field theory; rigorous RG | Precedent: a 4D marginally irrelevant boson–fermion (supersymmetric) system controlled at all scales |
| T. Balaban, M. O'Carroll, R. Schor, "Properties of block renormalization group operators for Euclidean Fermions in an external gauge field", J. Math. Phys. 32 (1991) 3199-3208, DOI 10.1063/1.529479 | Rutgers repository record | "The basis is laid for a block renormalization analysis of spinor electrodynamics in d=2,3 dimensions in a lattice approximation."; the operators, in a regular external gauge field, are "uniformly bounded analytic functions of complex-valued gauge fields" | Attack B |
| J. Dimock, "Quantum electrodynamics on the 3-torus I.- First step", arXiv:math-ph/0210020 | ar5iv HTML, first 100,000 characters | On the four-dimensional model: "To date this has not been possible and success is not likely anytime soon."; it "lacks ultraviolet asymptotic freedom, the flow of the effective coupling constants away zero"; "The present work will not directly generalize to (QED)4." | Attack B; the direction of the obstruction (section 4.7) |
| M. Anber, J. Donoghue, "The emergence of a universal limiting speed", arXiv:1102.0789, Phys. Rev. D 83, 105027 (2011) | arXiv abstract | Interactions drive different limiting speeds to a common one at low energy; differences usually shrink only logarithmically, so limits need an "exponentially large energy trajectory" | Context for the rate in Theorem 1 |

**NOT VERIFIED (not fetched, or fetched empty).** K. Gawędzki, A. Kupiainen, "Massless lattice `φ⁴_4` theory: rigorous control of a renormalizable asymptotically free model", CMP 99 (1985) 197-252: the Project Euclid page returned no text; title, journal and pages are from search snippets only. J. Feldman, J. Magnen, V. Rivasseau, R. Sénéor, "Construction and Borel summability of infrared `Φ⁴_4` by a phase space expansion", CMP 109 (1987) 437-480: same; a snippet attributes Borel summability in `λ` to its Theorem 1.3. Bauerschmidt–Brydges–Slade, "A renormalisation group method. III" and "V" (arXiv:1403.7252, 1403.7256): titles from search results only. Balaban–O'Carroll–Schor, CMP 122 (1989) 233-247: search snippet only. Brydges–Fröhlich–Seiler and Brydges–Dimock–Hurd, named in the lane brief "on massive lattice QED": not fetched; I could not check that description. Feldman–Knörrer–Trubowitz (fermionic functional integrals): not fetched. Chadha–Nielsen, Nucl. Phys. B 217 (1983) 125: not fetched, as in `CN1.md`. None of these is used below except as a named precedent.

**What the search found and did not find.** In 3+1 dimensions, the fetched non-perturbative results with lattice fermions and a massive vector field put the vector mass at the cutoff scale (arXiv:2001.00183), so the number of marginal scales is bounded. The bounds uniform in the cutoffs that were found are in 1+1 dimensions (arXiv:2602.03705, 2203.07652). Dimock (math-ph/0210020) states that a non-perturbative construction of the four-dimensional model "has not been possible"; his reason concerns the ultraviolet limit. No construction of 3+1-dimensional lattice fermions coupled to a vector field with bounds uniform in the number of marginal scales was found. This is a search result, not a literature-wide claim.

## 3. The model M″ and the lemma

### 3.1 The model

This is a supplied lattice model for rung 1. It is not a framework law (section 5).

*Lattice and fields.* Euclidean lattice `Λ_T = (Z/TZ)^4`, spacing one in all four directions, points `x = (x_0, x_1, x_2, x_3)`; `x_0` is Euclidean time. Bounds below are required to be independent of `T`. Species `a = 1, …, n`, `n ≥ 2`. Each species has a Grassmann field `ψ_a(x), ψ̄_a(x) ∈ C^4`, a charge `q_a ∈ Z∖{0}`, a bare speed `v_a > 0` and a bare mass counterterm `μ_a ∈ R`. The photon is a real field `A_μ(x)`, `μ = 0,…,3`, on the link `(x, x+μ̂)`. Euclidean gamma matrices are Hermitian with `{γ_μ, γ_ν} = 2δ_{μν}`.

*Fermion action (Wilson, `r = 1`, Peierls coupling).* With `w_{a,0} = 1`, `w_{a,j} = v_a` (`j = 1,2,3`) and `U_{a,μ}(x) = exp(i e q_a A_μ(x))`,
\[
S_F=\sum_a\sum_x\Big\{\mu_a\bar\psi_a\psi_a(x)+\sum_\mu w_{a,\mu}\Big[\bar\psi_a\psi_a(x)-\tfrac12\bar\psi_a(x)(1-\gamma_\mu)U_{a,\mu}(x)\psi_a(x+\hat\mu)-\tfrac12\bar\psi_a(x+\hat\mu)(1+\gamma_\mu)U_{a,\mu}(x)^*\psi_a(x)\Big]\Big\}.
\]
At `A = 0` its kernel in momentum space is `D_a(p) = μ_a + Σ_μ w_{a,μ}[(1 − cos p_μ) + iγ_μ sin p_μ]`. The doublers have masses of order one; the counterterms `μ_a` are chosen so that the light fermions stay massless (two relevant parameters for `n = 2`).

*Photon (Feynman–Stueckelberg covariance, speed one, mass `m`).* `A` is the centred Gaussian field with covariance
\[
C_{\mu\nu}(x-y)=\delta_{\mu\nu}\int_{[-\pi,\pi]^4}\frac{d^4k}{(2\pi)^4}\,\frac{e^{ik\cdot(x-y)}}{\hat k^2+m^2},\qquad \hat k^2=\sum_\mu\big(2\sin\tfrac{k_\mu}{2}\big)^2 .
\]
This is the lattice form of the covariance in arXiv:2001.00183 eq. (15), with a small regularising mass `m` in place of `a^{−1}M`. The weight is `dμ_C(A)\,e^{−S_F}\,dψ\,dψ̄`. The bare coupling is `G_0 := e^2`; the bare photon speed is one (a choice of time unit).

*Symmetries used.* (i) `S_F` is invariant under `ψ_a(x) → e^{ieq_aχ(x)}ψ_a(x)`, `ψ̄_a(x) → e^{−ieq_aχ(x)}ψ̄_a(x)`, `A_μ(x) → A_μ(x) + χ(x+μ̂) − χ(x)`; the Gaussian weight is not (gauge fixing and mass). (ii) Charge conjugation `A → −A` with the usual map of `ψ, ψ̄`, so expectations of conjugation-even observables depend on `e` through `G_0 = e^2`. (iii) Translations, the cubic group on space with its spin lift, time reflection. (iv) **Exchange.** If `q_a = q_b`, the swap `σ_{ab}: ψ_a ↔ ψ_b` maps the model with data `(v_a, v_b, μ_a, μ_b)` to the model with `(v_b, v_a, μ_b, μ_a)`. It is a symmetry exactly when those data agree.

*Scales.* Fix an integer `L ≥ 2`, `h = log L`, and put `N := ⌊log_L(1/m)⌋`, the number of scales above the photon mass.

### 3.2 Exact scale integration and its coordinates

An *exact scale integration* of M″ is a sequence of effective weights `S_0 = S`, `S_1, …, S_N`, each obtained from the previous one by integrating the fluctuation fields of one scale exactly and rescaling by `L`. The scheme (block averaging, momentum slicing, finite-range decomposition) is left to the attack. Its *state* at scale `k` is a point `X_k` of a complex Banach space `𝔛_k` with the following coordinates: the speeds `v_a(k)` (ratio of the spatial to the temporal coefficient of the local fermion kinetic term of species `a`), the photon speed `c(k)` and coupling `G(k) = G_k` (from the local quadratic photon term, normalised as in `CN1.md` Lemma 7), the remaining relevant and marginal coordinates, and an irrelevant remainder. The exchange `σ = σ_{12}` acts on `𝔛_k` as a linear isometric involution that swaps `v_1(k), v_2(k)` and fixes `c(k), G(k)`. The *per-step map* is `R_k: X_k ↦ X_{k+1}`.

Use an `ℓ^1`-type norm in which the speed block contributes `|v_1| + |v_2|`. Then for the pair `Δ_k := v_1(k) − v_2(k)`,
\[
\|X_k-\sigma X_k\| = 2|\Delta_k| + E_k ,\tag{3.1}
\]
where `E_k ≥ 0` is the norm of the exchange-odd part of all other coordinates (including the difference of the mass coordinates and the odd part of the irrelevant remainder).

### 3.3 The one-loop drag on the pair

From (OL) with `q_1 = q_2 = q`, the one-loop speed increment per step is `h G_k q² F(v_a(k), c(k))` with `F(v,c) = P(v,c)(c − v)`. Write `s = v/c`. A direct computation from the displayed `P` gives
\[
F(v,c)=\frac{(4s^2+3s+1)(1-s)}{6\pi^2(1+s)^2},\qquad \frac{dF}{ds}=-\frac{4s^2(s+3)}{6\pi^2(1+s)^3}<0\quad(s>0).\tag{3.2}
\]
*Proof of (3.2).* `4v²+3vc+c² = c²(4s²+3s+1)`, `c − v = c(1−s)`, `c(v+c)² = c³(1+s)²`; so `F = f(s)/(6π²(1+s)²)` with `f(s) = (4s²+3s+1)(1−s) = −4s³+s²+2s+1`. Then `f′(s)(1+s)² − 2f(s)(1+s) = (1+s)[(−12s²+2s+2)(1+s) − 2(−4s³+s²+2s+1)] = (1+s)(−4s³−12s²) = −4s²(s+3)(1+s)`, and divide by `6π²(1+s)^4`. □

So `F(v_1,c) − F(v_2,c) = −Λ_k Δ_k` with `Λ_k = c^{−1}∫_0^1 |F′(s_2 + t(s_1−s_2))| dt`. On any compact box `B′ ⊂ (0,∞)` of speeds, `Λ_k ∈ [Λ_min, Λ_max]` with `Λ_min > 0`. At consensus `Λ = P(c,c) = 1/(3π²c)`, as in `CN1_REFEREE.md` item 7. The drag is positive at every positive speed ratio, not only near consensus.

### 3.4 Why the pair line has no source

With `q_1 = q_2` and exchange-covariant counterterms, the only exchange-odd data of M″ are `v_1 − v_2` and what it generates. So the difference line has no forcing term independent of the odd data: if `X_k = σX_k` then `X_{k+1} = σX_{k+1}` and `Δ_{k+1} = 0`. A persistent source of the kind in `CN1.md` Proposition 4 (R1-D) would need an odd datum that the model does not have. Lattice and photon-mass corrections to the drag enter only as odd functions of the state, so Lemma 2 below turns them into Lipschitz terms. The #9913 finite matching (`LORENTZ_DISPERSION_CONSOLIDATED…` line 112, "kappa is a finite lattice constant") is of this kind: it changes the initial data, not the flow's fixed point.

### 3.5 The lemma, in discrete form, and its smallest sub-lemma

**R1″-MOD[d] (proposed precise form of `CN1.md` R1″-MOD for M″; four tests in section 6).** For `n = 2`, `q_1 = q_2 = 1`: there are `L ≥ 2`, `G_* > 0`, a compact set `B ⊂ (0,∞)` of bare speeds and constants `C, γ > 0`, all independent of `N`, such that for every `m ∈ (0, L^{−2}]`, every `G_0 ∈ (0, G_*]` and bare speeds in `B`, suitable counterterms give an exact scale integration with
\[
|\Delta_k|\le C\,(1+G_0 k)^{-\gamma}\,|\Delta_0|\quad (0\le k\le N),
\]
and, for some `c > 0` and `κ ≥ 1` with `δ_k := |Δ_k| + κE_k` (`E_k` as in (3.1)), strict contraction `δ_{k+1} ≤ (1 − cG_k)δ_k` at every scale `k` in a window `k_β ≤ k < N − k_β`; `c, κ, k_β` independent of `N`.

**UB″ (the size bound; the smallest sub-lemma found).** For `n = 2`, `q_1 = q_2 = 1`, there are constants `K, β, r, b_± > 0`, `θ ∈ [0,1)`, `k_m ∈ N`, a box `B′`, and `G_* > 0`, all independent of `N`, such that for `G_0 ∈ (0, G_*]` some exact scale integration of M″ satisfies, for `0 ≤ k < N`:

- (U0) *initial odd data:* `E_0 ≤ K|Δ_0|`;
- (U1) *exchange covariance:* `R_k ∘ σ = σ ∘ R_k`;
- (U2) *speed lines:* on the open `r`-neighbourhood `U_k` in `𝔛_k` of the segment `[σX_k, X_k]`, the function `ρ^{(k)}(Y) := [R_k(Y)]_{v_1} − v_1(Y) − hG(Y)F(v_1(Y), c(Y))` is holomorphic, and `|ρ^{(k)}| ≤ Kη_k` on `U_k` for `k < N − k_m`, `|ρ^{(k)}| ≤ KG_k` on `U_k` for `k ≥ N − k_m`, with `η_k := G_k² + G_k e^{−βk} + G_k e^{−β(N−k)}`; here `[·]_{v_1}` is the `v_1`-coordinate;
- (U3) *odd remainder:* `E_{k+1} ≤ θE_k + KG_k²|Δ_k|`;
- (U4) *coupling:* `1/G_k + b_− ≤ 1/G_{k+1} ≤ 1/G_k + b_+`;
- (U5) *box:* `v_1(k), v_2(k), c(k) ∈ B′`.

The term `G_k e^{−βk}` carries the lattice correction to the drag (the Peierls note's remainders "integrates to a finite O(rho_0) value", line 269). The term `G_k e^{−β(N−k)}` carries the photon-mass correction `O((mL^k)²) ≤ O(L^{−2(N−k)})` at scales above `1/m` (`mL^N ≤ 1` by the choice of `N`), so `β ≤ 2h` suffices there. The last `k_m` scales near `1/m` get only a crude bound; the Peierls note says of exactly this situation that "a new mass threshold is a different problem" (line 516). Theorem 3 shows UB″ implies R1″-MOD[d]. No separate Lipschitz or vanishing-at-equal-speeds hypothesis is needed for the pair: Lemma 2 derives it.

## 4. Results

### 4.1 Theorem 1: per-scale bounds give contraction uniform in N

**Theorem 1 (discrete pair contraction).** Fix `λ, K, β, b_−, b_+ > 0`, `θ ∈ [0,1)` and `k_m ∈ N`. Let `N > k_m`. Let `G_k > 0`, `Δ_k ∈ R` and `E_k ≥ 0` (`0 ≤ k ≤ N`) satisfy, with `η_k := G_k² + G_k e^{−βk} + G_k e^{−β(N−k)}`:

- (a) `1/G_k + b_− ≤ 1/G_{k+1} ≤ 1/G_k + b_+` for `0 ≤ k < N`;
- (b) `|Δ_{k+1}| ≤ (1 − λG_k + Kη_k)|Δ_k| + E_k` for `0 ≤ k < N − k_m`;
- (b′) `|Δ_{k+1}| ≤ (1 + KG_k)|Δ_k| + E_k` for `N − k_m ≤ k < N`;
- (c) `E_{k+1} ≤ θE_k + KG_k²|Δ_k|` for `0 ≤ k < N`.

Put `κ := 2/(1−θ)`, `K′ := K(1+κ)` and `δ_k := |Δ_k| + κE_k`. If `G_0 ≤ 1` and `λG_0 ≤ (1−θ)/2`, then
\[
\delta_N\le C\,(1+b_+G_0N)^{-\lambda/b_+}\,\delta_0,\qquad
C=(1+b_+G_0k_m)^{\lambda/b_+}\exp\!\Big[K'\Big(G_0^2+\frac{G_0}{b_-}+\frac{2G_0}{1-e^{-\beta}}+k_mG_0\Big)\Big].
\]
`C` does not depend on `N`. Moreover, if also `K′G_0 ≤ λ/4`, let `k_β` be the least integer with `K′e^{−βk_β} ≤ λ/4`. Then `δ_{k+1} ≤ (1 − λG_k/4)δ_k` for every `k` with `k_β ≤ k < N − max(k_β, k_m)`: the pair contracts strictly at every scale of that window, and the window's end margins do not depend on `N`.

*Proof.* Step 1 (one step, `k < N − k_m`). By (b) and (c),
`δ_{k+1} ≤ (1 − λG_k + Kη_k + κKG_k²)|Δ_k| + (1 + κθ)E_k`.
Since `λG_k ≤ λG_0 ≤ (1−θ)/2` (by (a), `G_k ≤ G_0`), `κ(1 − θ − λG_k) ≥ κ(1−θ)/2 = 1`, that is `1 + κθ ≤ κ(1 − λG_k)`. Also `κKG_k² ≤ κKη_k`. Hence `δ_{k+1} ≤ (1 − λG_k + K′η_k)|Δ_k| + (1 − λG_k)κE_k ≤ (1 − λG_k + K′η_k)δ_k`. The factor is positive because `λG_k < 1`.

Step 2 (one step, `k ≥ N − k_m`). By (b′) and (c), `δ_{k+1} ≤ (1 + KG_k + κKG_k²)|Δ_k| + (1 + κθ)E_k`. Since `1 + κθ ≤ κ` and `G_k ≤ 1`, `δ_{k+1} ≤ (1 + K′G_k)δ_k`.

Step 3 (product). With `1 + x ≤ e^x`,
`δ_N ≤ δ_0 exp[−λ Σ_{k<N−k_m} G_k + K′ Σ_{k<N} η_k + K′k_mG_0]`.
By (a), `1/G_k ≤ 1/G_0 + b_+k`, so `G_k ≥ G_0/(1 + b_+G_0k)`. This is decreasing in `k`, so the left Riemann sum dominates the integral: `Σ_{k=0}^{N′−1} G_k ≥ ∫_0^{N′} G_0(1 + b_+G_0s)^{−1}ds = b_+^{−1} log(1 + b_+G_0N′)`, with `N′ = N − k_m`. By (a) again, `G_k ≤ G_0/(1 + b_−G_0k)`, so `Σ_k G_k² ≤ G_0² + ∫_0^∞ G_0²(1 + b_−G_0s)^{−2}ds = G_0² + G_0/b_−`. Also `Σ_k G_ke^{−βk} ≤ G_0/(1−e^{−β})` and `Σ_{k<N} G_ke^{−β(N−k)} ≤ G_0Σ_{j≥1}e^{−βj} ≤ G_0/(1−e^{−β})`. Finally `(1 + x(N−k_m))(1 + xk_m) ≥ 1 + xN` for `x ≥ 0`, so `(1 + b_+G_0N′)^{−λ/b_+} ≤ (1 + b_+G_0k_m)^{λ/b_+}(1 + b_+G_0N)^{−λ/b_+}`. Combine.

Step 4 (window). For `k_β ≤ k < N − k_β`, `η_k ≤ G_k(G_0 + e^{−βk} + e^{−β(N−k)}) ≤ G_k(G_0 + 2e^{−βk_β})`, so `K′η_k ≤ G_k(λ/4 + λ/2)` and Step 1 gives `δ_{k+1} ≤ (1 − λG_k/4)δ_k`. □

**Remarks.** (1) The exponent `λ/b_+` is the discrete form of `CN1.md` Theorem 2's `q²P∞/(WS∞)`. In Theorem 3 below, `λ = hΛ_min` and `b_+ ≈ hW·max S`; on a box shrinking to consensus the ratio tends to `2q²/W`. (2) The rate is a power of `N = log_L(1/m)`, not of `L^N`. This is what `LZ1I.md` Theorem 12 (line 188) says a marginal drag must give: "a nonzero difference is not `O((a_lat|k|)^p)` for any `p>0`". (3) Only upper bounds on `|Δ|` and `E` are used. No lower bound on the drag beyond `λG_k` and no sign of `Δ` enters. (4) Below the photon mass (`k > N`) nothing is claimed. With a massive photon the drag switches off there, and the difference is expected to freeze at its scale-`N` value. Theorem 1 bounds that value.

### 4.2 Lemma 2 and Theorem 3: UB″ implies R1″-MOD[d]

**Lemma 2 (an exchange-odd difference is Lipschitz once it is bounded on a complex neighbourhood).** Let `𝔛` be a complex Banach space, `σ` a linear involution of `𝔛`, `X ∈ 𝔛` and `r > 0`. Let `ρ` be holomorphic on the open `r`-neighbourhood `U` of the segment `[σX, X]`, with `|ρ| ≤ M` on `U`. Then
\[
|\rho(X)-\rho(\sigma X)|\le \frac{M}{r}\,\|X-\sigma X\|.
\]

*Proof.* Put `Y_t = σX + t(X − σX)`, `t ∈ [0,1]`, and `g(t) = ρ(Y_t)`. Then `g′(t) = Dρ(Y_t)[X − σX]`. Fix `t` and a unit vector `u`. The function `φ(ζ) = ρ(Y_t + ζu)` is holomorphic on `|ζ| < r`, because `Y_t + ζu ∈ U`, and `|φ| ≤ M` there. Cauchy's formula on the circle `|ζ| = r′ < r` gives `|φ′(0)| ≤ M/r′`; let `r′ → r`. So `‖Dρ(Y_t)‖ ≤ M/r`, and the mean value inequality gives `|g(1) − g(0)| ≤ (M/r)‖X − σX‖`. □

This is the step that `CN1.md` line 117 records as missing: "Exchange symmetry together with a uniform `O(G²)` Lipschitz bound in the two exchanged speed coordinates gives the homogeneous difference form; symmetry alone does not give the bound." Lemma 2 says what does give it: a size bound `O(G²)` on a complex neighbourhood of fixed radius. A constructive RG produces exactly such bounds, because its expansions are convergent and hence analytic in the coordinates. So the Lipschitz half of attack 3's failing step is settled. The size half is UB″ (U2).

**Lemma 3a (discrete box).** Take all `n` species and the photon with the per-step maps
`v_a(k+1) = v_a(k) + hG_kq_a²P(v_a,c)(c − v_a) + ρ_a(k)`, `c(k+1) = c(k) + hG_kΣ_b n_bq_b²R(v_b,c)(v_b − c) + ρ_0(k)`
(right sides at scale `k`), with `|ρ_a(k)|, |ρ_0(k)| ≤ K(G_k²D_k + φ_k)`, `Σ_kφ_k ≤ Φ`, and Theorem 1 (a). Let `m_0, M_0` be the least and largest initial speed, `D_0 = M_0 − m_0`, `B′ = [m_0/2, M_0 + m_0/2]`, `p̄ = max_{B′×B′} max(max_a q_a²P, Σ_b n_bq_b²R)` and `D̄ = e^{2K(G_0²+G_0/b_−)}(D_0 + 2KΦ)`. If `hG_0p̄ ≤ 1` and `K[(G_0² + G_0/b_−)D̄ + Φ] ≤ m_0/2`, then every speed stays in `B′` at every scale, for every `N`.

*Proof.* Induction on `k`; assume all speeds lie in `B′` at scales `0, …, k`. With `τ_a = hG_kq_a²P(v_a,c) ∈ [0,1]` the one-loop move of `v_a` is `(1−τ_a)v_a + τ_ac`. With `τ′_b = hG_kn_bq_b²R(v_b,c) ≥ 0`, `Στ′_b ≤ 1`, the move of `c` is `(1 − Στ′_b)c + Στ′_bv_b`. Both are convex combinations of current speeds, so the one-loop step maps `[m_k, M_k]` into itself. Hence `M_{k+1} ≤ M_k + K(G_k²D_k + φ_k)`, `m_{k+1} ≥ m_k − K(G_k²D_k + φ_k)`, and `D_{j+1} ≤ (1 + 2KG_j²)D_j + 2Kφ_j`. The discrete Grönwall bound gives `D_j ≤ ∏(1 + 2KG_i²)(D_0 + 2KΦ) ≤ D̄`, using `ΣG_i² ≤ G_0² + G_0/b_−` from Theorem 1's proof. Summing, `M_{k+1} ≤ M_0 + K[(G_0² + G_0/b_−)D̄ + Φ] ≤ M_0 + m_0/2` and `m_{k+1} ≥ m_0/2`. □

This is the discrete form of the box step in `CN1.md` Theorem 3. Its hypothesis on `ρ_a, ρ_0` is the discrete (R-i): the remainders vanish at consensus up to summable forcing. That vanishing is not an exchange symmetry. It reflects Lorentz invariance at consensus up to lattice terms, and it stays part of the size estimate. Lemma 3a shows that (U5) costs nothing beyond (R-i) and smallness.

**Theorem 3 (UB″ implies R1″-MOD[d]).** Assume UB″ with its constants. Let `Λ_min, Λ_max` be the bounds of section 3.3 on `B′`, `λ := hΛ_min`, `K_1 := max(K, 2K/r)`, and let `G_*` satisfy `G_* ≤ 1`, `hG_*Λ_max ≤ 1`, `λG_* ≤ (1−θ)/2` and `3KG_* ≤ r`. Then for `G_0 ∈ (0, G_*]` and every `N`, with `κ = 2/(1−θ)`,
\[
|\Delta_k|\le C\,(1+K)\kappa\,(1+b_+G_0k)^{-\lambda/b_+}\,|\Delta_0|\qquad(0\le k\le N),
\]
where `C` is the constant of Theorem 1 with `K_1` in place of `K`. If also `K_1(1+κ)G_0 ≤ λ/4`, the pair contracts strictly at every scale of the window of Theorem 1. All constants are independent of `N`.

*Proof.* By (U1), `σX_{k+1} = R_k(σX_k)`. The `v_1`-coordinate of `σX_{k+1}` is `v_2(k+1)`. By (U2) at the point `σX_k ∈ U_k`, whose `v_1`-, `c`- and `G`-coordinates are `v_2(k), c(k), G_k`, that coordinate equals `v_2(k) + hG_kF(v_2(k), c(k)) + ρ^{(k)}(σX_k)`. Subtracting from (U2) at `X_k` and using section 3.3,
\[
\Delta_{k+1}=(1-hG_k\Lambda_k)\,\Delta_k+\big[\rho^{(k)}(X_k)-\rho^{(k)}(\sigma X_k)\big].
\]
By (U5), `Λ_k ∈ [Λ_min, Λ_max]`, so `0 ≤ 1 − hG_kΛ_k ≤ 1 − λG_k`. By Lemma 2 and (3.1) the bracket is at most `(M_k/r)(2|Δ_k| + E_k)`, with `M_k = Kη_k` for `k < N − k_m` and `M_k = KG_k` otherwise. Since `η_k ≤ 3G_k` and `3KG_0 ≤ r`, `M_k/r ≤ 1`. So (b) and (b′) of Theorem 1 hold with `K_1`, and (c) is (U3), (a) is (U4). Theorem 1 and its proof, run up to any `k ≤ N`, give `|Δ_k| ≤ δ_k ≤ C(1 + b_+G_0k)^{−λ/b_+}δ_0` for `k ≤ N − k_m` and, through the last `k_m` steps, with the same `C`. Finally `δ_0 = |Δ_0| + κE_0 ≤ (1 + κK)|Δ_0| ≤ (1+K)κ|Δ_0|` by (U0), as `κ ≥ 2`. □

**What Theorem 3 removes and what it leaves.** It removes the interpolation in `CN1.md`'s R1-MOD (the RG is discrete and Theorem 1 is discrete). It removes the separate Lipschitz hypothesis (R-iii), by Lemma 2. It removes the forcing on the pair line, by section 3.4. It leaves one estimate, UB″ (U2)-(U5): an analytic size bound per scale, uniform in `N`. The next sections ask where that bound can hold and try three ways to prove it.

### 4.3 Proposition 4: no disc of the bare coupling works for all N

**Proposition 4 (Cauchy obstruction).** Let `r, B, α > 0` and `β ≥ 0`. Suppose `F` is holomorphic on `{|z| < r}`, `|F| ≤ B` there, and `|F′(0)| ≥ αN − β` for an integer `N`. Then `N ≤ (B/r + β)/α`.

*Proof.* Cauchy's estimate on the circle `|z| = r′ < r` gives `|F′(0)| ≤ B/r′`; let `r′ → r`. So `αN − β ≤ B/r`. □

**Corollary 4′ (for M″; conditional on the one-loop input of `CN1.md`).** Fix bare speeds `v_1 ≠ v_2` in `B`, and fix an exact scale integration whose coordinates are holomorphic in `G_0` near `0` for each `N` (as any convergent expansion gives). Assume the first-order input: at `G_0 = 0` the speeds do not flow (`Δ_N(0) = Δ_0`), and the first `G_0`-derivative of the scale-`N` speed of species `a` is `Σ_{k<N} h F(v_a, 1)(1 + ε_k^a)` with `Σ_k |ε_k^a| ≤ c_1`, `c_1` independent of `N`. (This is the one-loop drag of (OL) per scale, with the photon speed one at zeroth order, plus lattice corrections and photon-mass corrections that are summable over scales, as in section 3.5.) Then there are no `r, B > 0` such that, for every `N`, `G_0 ↦ Δ_N(G_0)` is holomorphic on `|G_0| < r` with `|Δ_N| ≤ B|Δ_0|`.

*Proof.* Put `F_N = Δ_N/Δ_0` and `Λ_0 := −(F(v_1,1) − F(v_2,1))/Δ_0 > 0` (section 3.3). The input gives `F_N′(0) = −hΛ_0N + e_N` with `|e_N| ≤ h(|F(v_1,1)| + |F(v_2,1)|)c_1/|Δ_0|`, which is independent of `N`. Proposition 4 with `α = hΛ_0` bounds `N`. □

The same argument works with the coupling instead of the speeds. If `1/G_N = 1/G_0 + Σ_{k<N} b_k + O(G_0)` with `Σ_{k<N} b_k ≥ bN − c` (the one-loop vacuum polarisation of (OL), `S > 0`), then the second Taylor coefficient of `G_N` is `−Σb_k`, and Cauchy's estimate for the second derivative gives the same contradiction.

**Corollary 4″ (no import needed).** Let `r, B > 0`. Suppose that for every `N` the scale-`N` coupling coordinate `G_N(z)`, as a function of the bare coupling `z = G_0`, is holomorphic on `|z| < r`, with `|G_N| ≤ B`, `G_N(0) = 0` and `G_N′(0) = 1` (at zeroth order the photon kinetic term is not renormalised, so the coupling coordinate is `G_0(1 + O(G_0))`). Then `G_N(x) ≥ x/2` for every `N` and every real `x ∈ [0, r²/(8B)]`. Hence (U4) of UB″, which gives `G_N(x) ≤ x/(1 + b_−xN)` for `x ∈ (0, G_*]`, fails at `x = min(G_*, r²/(8B))` for `N > 1/(b_−x)`. In the same way, if `Δ_N(z)/Δ_0` is holomorphic on `|z| < r`, bounded by `B` and equal to `1` at `z = 0` (no flow at zero coupling), then `Δ_N(x)/Δ_0 ≥ 1/2` for `x ∈ [0, r/(4B)]` and every `N`, which contradicts the decay `|Δ_N| ≤ C(1+G_0N)^{−γ}|Δ_0|` of R1″-MOD[d] for large `N`.

*Proof.* For `|z| ≤ r/2` the disc of radius `r/2` around `z` lies in `|z| < r`, so Cauchy's estimates give `|G_N″(z)| ≤ 2B/(r/2)² = 8B/r²` and `|F′(z)| ≤ 2B/r` for `F = Δ_N/Δ_0`. Taylor's formula with remainder on `[0, x]`: `G_N(x) ≥ x − (8B/r²)x²/2 = x − 4Bx²/r² ≥ x/2` when `x ≤ r²/(8B)`, and `F(x) ≥ 1 − 2Bx/r ≥ 1/2` when `x ≤ r/(4B)`. Both ranges lie in `[0, r/2]`, because Cauchy's estimate with `G_N′(0) = 1` gives `B ≥ r`, and `F(0) = 1` gives `B ≥ 1`. (For real `x` the values are real: the coordinates are real for real bare data.) □

So UB″, or the decay R1″-MOD[d] asserts, is incompatible with bounds on a disc of the bare coupling whose radius does not depend on `N`. This uses no one-loop coefficient: the decay itself is the obstruction.

**What Corollaries 4′ and 4″ say and do not say.** It does not touch R1″-MOD[d], which concerns real `G_0 > 0`. It does say that no proof can establish UB″ (or any bound on the scale-`N` speeds) by analytic bounds on a fixed complex disc around `G_0 = 0` with radius independent of `N`. On the real axis the expected answer `(1 + bG_0N)^{−γ}` (Theorem 1) continues to a function with a branch point at `G_0 = −1/(bN)`, which enters every fixed disc as `N` grows. Corollary 4′ needs a Taylor coefficient that grows linearly in the number of scales; in M″ the one-loop drag and the one-loop vacuum polarisation supply such growth, as marginal effects of 3+1 dimensions. Corollary 4″ needs only the decay itself. Whether the 1+1-dimensional quantities of arXiv:2602.03705 avoid such growth is not examined here.

### 4.4 Proposition 5: a disc tangent to the imaginary axis works

**Proposition 5 (tangent domain).** Let `b > 0`, `K ≥ 0`, `C := K + 2(b+K)²` and `r_0 := min{1, b/(2C), 1/(4(b+K))}`. Let complex numbers `G_k` satisfy `G_{k+1} = G_k − bG_k² + R_k` with `|R_k| ≤ K|G_k|³` whenever `|G_k| ≤ r_0`.

- (i) If `Re(1/G_0) ≥ 1/r_0`, then `Re(1/G_k) ≥ 1/r_0 + bk/2` and `|G_k| ≤ (1/r_0 + bk/2)^{−1}` for every `k ≥ 0`.
- (ii) If the `G_k` are real and `G_0 = −t` with `0 < t ≤ r_0`, then `|G_k| > r_0` for some `k ≤ 2/(bt) + 1`.

The set `{G ≠ 0 : Re(1/G) ≥ 1/r_0}` is the closed disc `|G − r_0/2| ≤ r_0/2` without the point `0`: it is tangent to the imaginary axis at `0` and contains `(0, r_0]`.

*Proof.* Write `w_k = 1/G_k` and `u = bG_k − R_k/G_k`. If `|G_k| ≤ r_0`, then `|u| ≤ (b + K)|G_k| ≤ 1/4`, and `1/(1−u) = 1 + u + u²/(1−u)` with `|u²/(1−u)| ≤ 2|u|²`. Since `G_{k+1} = G_k(1 − u)`,
\[
w_{k+1}=w_k+b-\frac{R_k}{G_k^2}+\frac{u^2}{(1-u)G_k},\qquad |w_{k+1}-w_k-b|\le \big(K+2(b+K)^2\big)|G_k|=C|G_k|\le \tfrac b2 .
\]
(i) Induction: if `Re w_k ≥ 1/r_0 + bk/2`, then `|G_k| ≤ 1/Re w_k ≤ r_0`, so `Re w_{k+1} ≥ Re w_k + b/2`. (ii) Let `k_1 = ⌈2/(bt)⌉` and suppose `|G_j| ≤ r_0` for all `j ≤ k_1`. Then the `w_j` are real, `|w_j| ≥ 1/r_0`, and `w_{j+1} − w_j ∈ [b/2, 3b/2]`. So `w_{k_1} ≥ −1/t + bk_1/2 ≥ 0`, hence `w_{k_1} ≥ 1/r_0`, while `w_0 = −1/t ≤ −1/r_0`. A step of length at most `3b/2 < 2/r_0` (as `r_0 ≤ 1/(4(b+K))`) cannot jump over the gap `(−1/r_0, 1/r_0)`, so some `w_j` lies in it: a contradiction. So some `j ≤ k_1 ≤ 2/(bt) + 1` has `|G_j| > r_0`. □

**Use.** Part (ii) is Corollary 4′ for the coupling line alone: a negative bare coupling of size `t` runs out of the small-coupling region after about `2/(bt)` scales, so a bound on a disc of radius `t` cannot hold past that many scales. Part (i) shows that the running coupling itself causes no trouble on the tangent disc, uniformly in `k`. So the domain on which UB″ can be posed, with `N`-independent constants, is a tangent disc in the bare coupling (or, equivalently, a fixed disc in the running couplings `G_k`), not a full disc around `0`. A proof of UB″ must therefore organise its expansion around the running coupling. The renormalised expansions of the literature do this order by order (arXiv:1107.4741: "finite at all orders"), and attack 1 on file stops at summing them.

### 4.5 Lemma 6: the one-loop local quartic photon term has no sign at leading order

A scale decomposition that is not gauge covariant generates local photon terms that gauge invariance forbids: `A_μA_μ`-type masses (relevant) and `A⁴`-type terms (marginal). Attack C below needs the sign of the quartic ones. Lemma 6 computes their continuum one-loop part.

**Lemma 6.** Let `v > 0`, write `p_v = (p_0, vp_1, vp_2, vp_3)` and, for real `A ∈ R^4`, `Ã = (A_0, vA_1, vA_2, vA_3)`. Let `𝒩: R^4 → [0,∞)` be continuous, positively homogeneous of degree one and positive off `0`, and let `ψ: (0,∞) → R` be measurable with `∫_0^∞ |ψ(t)| dt/t < ∞`. Then
\[
\int_{\mathbb R^4} d^4p\;\psi(\mathcal N(p))\,\frac{\operatorname{tr}\big[(\not p_v\,\tilde{\not A})^4\big]}{(p_v^2)^4}=0 .
\]
For a constant field `A`, a fermion of speed `v` with the Ward-consistent vertex `γ_0A_0 + vγ·A` and propagator `χ(p)(i\not p_v)^{−1}` gives a one-loop quartic term proportional to this integral with `ψ = χ^4`. A scale slice gives the same form with `ψ` the difference of two such functions. So the continuum one-loop contribution to the local quartic photon coupling vanishes at every scale, for every speed and every regulator that depends on `p` through one homogeneous norm.

*Proof.* (1) Clifford identity. For vectors `p, a` put `X = \not p\not a`. From `\not a\not p = 2(p·a) − \not p\not a` we get `X² = 2(p·a)X − p²a²`, hence `X⁴ = [8(p·a)³ − 4(p·a)p²a²]X + p⁴a⁴ − 4(p·a)²p²a²`. With `tr X = 4p·a` and `tr 1 = 4`,
\[
\operatorname{tr}X^4 = 32(p\cdot a)^4-32(p\cdot a)^2p^2a^2+4p^4a^4 .
\]
(2) Moments on `S³`. Let `g` be a standard Gaussian vector in `R^4` and `g = Rω` with `R = |g|`; then `R` and `ω` are independent and `ω` is uniform on `S³`. `E g_1² = 1 = E R² · E ω_1²` with `E R² = 4`, so `E ω_1² = 1/4`. `E g_1⁴ = 3 = E R⁴ · E ω_1⁴` with `E R⁴ = 4·3 + 12·1 = 24`, so `E ω_1⁴ = 1/8`. By rotation invariance the same holds for `ω·e` for any unit `e`.
(3) Substitute `p′ = p_v` (Jacobian `v^{−3}`); `𝒩(p) = 𝒩′(p′)` with `𝒩′(p′) = 𝒩(p′_0, p′_1/v, p′_2/v, p′_3/v)`, again homogeneous of degree one and positive. In polar coordinates `p′ = ρω`, the integrand is `ψ(ρ𝒩′(ω))ρ^{−4}T(ω)` with `T(ω) = tr[(\not ω\tilde{\not A})⁴] = 32(ω·Ã)⁴ − 32(ω·Ã)²|Ã|² + 4|Ã|⁴`, a bounded function. With `d⁴p′ = ρ³dρ\,dω` and `t = ρ𝒩′(ω)`,
\[
\int = v^{-3}\Big(\int_0^\infty\psi(t)\,\frac{dt}{t}\Big)\int_{S^3}T(\omega)\,d\omega ,
\]
by Fubini, which applies since the double integral of the absolute value is at most `v^{−3}·68|Ã|⁴·|S³|·∫|ψ|dt/t`. By (2), `∫_{S³}T dω = |S³||Ã|⁴(32/8 − 32/4 + 4) = 0`. □

[check] `/tmp/toe-CN1MOD/check_box.py`: the trace identity holds with relative error `2·10^{−14}` at 200 random points; Monte Carlo averages of the angular integrand at `v ∈ {0.6, 1, 1.7}` and three field directions are zero within two standard errors. Floating point, a few seconds; it guides and does not prove.

**Consequence used below.** The cubic group and charge conjugation allow several quartic photon forms, for instance `Σ_μ A_μ⁴` and `(A·A)²`, and they allow indefinite combinations: `Q(A) = Σ_μA_μ⁴ − ½(A·A)²` is `+½` at `A = e_1` and `−¼` at `A = ½(1,1,1,1)`. Lemma 6 removes the continuum one-loop contribution at every scale. So the sign of the generated local quartic photon coupling is set by lattice corrections at the first scales, by the Peierls seagulls, and by two and more loops. No symmetry of M″ fixes it.

### 4.6 Three new attacks on UB″

The attacks on file are listed in section 0. Each attack below states its plan, what it reached, and the first step it could not pass. The standard is that of `CN1_REFEREE.md` item 59: an attack counts as failed when its first failing step is named. Here attack A's failing step is a theorem; attacks B and C name their step and state the partial results reached before it.

**Attack A: analytic bounds in the bare coupling on a disc, uniform in `N`.**

*Plan.* Integrate the massive photon exactly, as arXiv:2001.00183 does before its eq. (16) ("we find convenient to integrate out the boson field getting a purely fermionic theory"). Run a convergent fermionic multiscale expansion with Gram-type determinant bounds. Prove analyticity in `G_0` on `|G_0| < r` with `r` independent of `N`, as the 1+1-dimensional result arXiv:2602.03705 states for its cutoffs (its abstract, as fetched, says that `e_0` depends neither on the lattice spacing nor on the fermion mass; this is a paraphrase, not a quotation). Read UB″ (U2)-(U4) off the expansion, and get the Lipschitz part from Lemma 2.

*Reached.* Theorem 3: if the bounds held on such a disc, R1″-MOD[d] would follow. Also, in this plan the photon kernel is integrated once and never renormalised, so its normalisation, which is `G`, is the bare one at every scale: in 3+1 dimensions every local four-fermion term has scaling dimension six, so the fermionic localisation at scale `k` contains no term that could carry a running `G_k`. The expansion is therefore an expansion in `G_0`.

*Fails at.* Corollary 4″ (proved, no import): bounds on a disc of the bare coupling with radius independent of `N` contradict the decay of the coupling in (U4) and the decay of the pair in R1″-MOD[d]. Corollary 4′ and Proposition 5(ii) give the same conclusion from the one-loop coefficients. The failure does not depend on the decay of the photon kernel or on the photon mass.

*Distinct from the file.* Attack 2 on file has the same first move but stops at "scale-summability of the kernel". Attack A stops at the domain of analyticity, and that stop is a theorem. It also settles attack 2 for the massive case: without kernel renormalisation that plan yields bare-coupling bounds, which Corollary 4″ excludes. The repair it points to is to run `G_k`, that is, to keep the photon (or a running kernel) in the RG. Attacks B and C do that.

**Attack B: gauge-covariant block-spin RG with background-field fermions (Balaban; Balaban–O'Carroll–Schor; Dimock's QED₃ as the template).**

*Plan.* Keep the photon as a field. Average it gauge-covariantly over blocks, so that every effective action is gauge invariant. Then the Ward identities hold exactly at every scale; no photon mass and no quartic photon term is generated; the only marginal photon coordinate is the `F²` coefficient, that is, the running `G_k`, which Proposition 5 keeps on the tangent domain. At each scale integrate the fermions in the background of the photon not yet integrated, using the block-RG fermion operators of Balaban–O'Carroll–Schor (J. Math. Phys. 32 (1991) 3199). Split each scale into small-field and large-field regions for the photon, as Balaban does and as Dimock's QED₃ (arXiv:math-ph/0210020) does in `d = 3`.

*Reached.* (i) The stated obstruction to QED₄ does not apply to UB″. Dimock gives as the reason that the four-dimensional model "lacks ultraviolet asymptotic freedom, the flow of the effective coupling constants away zero". That concerns a continuum limit at fixed renormalised coupling. In M″ the bare coupling is fixed at the lattice scale and the RG runs toward the infrared, where the coupling decreases (Proposition 5(i)). (ii) The photon part is free and abelian, so its block minimisers and background-field propagators are linear objects. (iii) With exact gauge covariance the coordinates of Lemma 2 can be gauge-invariant ones, and (U1) holds because the block averaging treats both species alike.

*Fails at.* **B1**: the scale-`k` fermion operators (fluctuation covariance and block minimisers in a background gauge field) must be analytic and uniformly bounded in complex backgrounds, with exponentially decaying kernels, uniformly in `k ≤ N`, for every background in the small-field set of a marginal coupling in 3+1 dimensions. Balaban–O'Carroll–Schor give these properties "in a regular external gauge field" and frame the programme for "spinor electrodynamics in d=2,3"; Dimock writes that his `d = 3` work "will not directly generalize to (QED)4". I tried the direct route: in each block, put the background in axial gauge and expand the fermion block operators in a Neumann series around the free ones. Inside one block the series converges when `|e_k F|` is small. Between blocks, the axial gauges differ by gauge transformations that are not small. Absorbing them needs the gauge-covariant averaging, and the 3+1 analysis of that averaging is B1. This lane does not prove B1 and found no source for it. The step after B1 would be **B2**, a decoupling of the fermion integral across large-field regions, where the background is not regular.

*Distinct from the file.* No attack on file keeps the photon as a field with a non-perturbative treatment of its fluctuations.

**Attack C: finite-range RG with polynomial localisation, not gauge covariant (the Bauerschmidt–Brydges–Slade scheme).**

*Plan.* Decompose the photon covariance into finite-range pieces, `C = Σ_k Γ_k` (the BBS book, arXiv:1907.05474, introduces finite-range decomposition), and the fermion covariance by scale. Carry coordinates `(V_k, K_k)`: `V_k` a local polynomial of scaling dimension at most four in `A, ψ, ψ̄`, `K_k` an irrelevant polymer remainder. Use norms that are analytic in the boson field with a Gaussian regulator, as in BBS, and Grassmann norms for the fermions. Track the relevant terms: the two fermion masses are fixed by the counterterms `μ_a`; the photon mass terms `A_0²` and `Σ_iA_i²` that the non-covariant slicing generates at intermediate scales must cancel in the full model, because `S_F` is gauge invariant, and the scheme has to show this scale by scale. Keep the marginal couplings on the tangent domain of Proposition 5. The BBS analysis of the 4-dimensional weakly self-avoiding walk (arXiv:1403.7422) is the precedent for a 4D marginally irrelevant boson–fermion system controlled at all scales.

*Reached.* The list of marginal coordinates: per species the two kinetic coefficients and two vertex charges (temporal and spatial), the photon quadratic coefficients, and the local quartic photon couplings allowed by the cubic group and charge conjugation. Lemma 6: the continuum one-loop contribution to every quartic photon coupling vanishes at every scale.

*Fails at.* **C1, stability.** Norms of BBS type bound `e^{−V_k}` on a complex neighbourhood of the real boson fields, weighted by a Gaussian regulator. This needs the quartic part of `V_k` to be non-negative in every field direction. In the `|φ|⁴` model the quartic term is the interaction itself and carries a coupling of fixed sign. M″ has no bare quartic photon term; the generated one has the sign of lattice, seagull and higher-loop contributions (Lemma 6), and the symmetries allow indefinite forms (section 4.5). If it is negative along a direction, `|e^{−V_k(A)}|` grows like `e^{c|A|⁴}` along it, and no Gaussian regulator bounds it. Moving the quartic term into `K_k` does not help: it is marginal, so `K_k` would no longer contract. The two repairs that suggest themselves are a gauge-covariant decomposition, which is attack B, and localisation in gauge-invariant variables for the compact (Peierls) coupling, which, as far as this lane can see, again needs the background-field fermion bounds of B1.

*Distinct from the file and from B.* It keeps the photon as a field (unlike attacks 1-4) and gives up gauge covariance (unlike B); it stops at the sign of a generated coupling, not at fermion operator bounds.

### 4.7 The attacks on file, after this file

- *Attack 2* (Gaussian photon integration plus a convergent fermionic expansion). With a photon mass the kernel's long-range tail is gone, as the outline expected. As planned, without renormalising the kernel, the attack gives bare-coupling bounds, and Corollary 4″ shows these cannot be uniform in `N` if R1″-MOD[d] is true. Its failure for R1″-MOD is now proved, with no import.
- *Attack 3* (Ward identities and exchange symmetry). Its failing step had two halves: the Lipschitz form and the size. Lemma 2 settles the Lipschitz half: exchange symmetry plus a size bound on a complex neighbourhood gives (R-iii). The size half is UB″ (U2).
- *Attacks 1 and 4* are unchanged. Proposition 5 says where attack 1's renormalised expansion has to live if its orders are ever summed: on a fixed disc in the running couplings, which is a tangent disc in the bare one.

## 5. Which framework law realises M″

None does yet. M″ is a supplied Euclidean lattice model. The live laws (`L_cube`, `L5-U[m]`, `L5-O[S_+]`) differ from it at five named points, and each point is an open item already on file.

1. **The photon.** M″ has a non-compact Gaussian photon with a cone of speed one. The laws carry finite link registers; for `L5-U` the register is "ten complex rishon modes [...] restricted to a sector of fixed total rishon number `m`" (`LW1_5_DRAFT.md` line 254, Theorem U, as quoted in `Y2W_DRAFT.md` line 30). The only flux-carrying band constructed so far "is an exact one-way band in a chosen stationary state, not an identified photon or a Clifford cone" (`GA15PHI.md` line 5). Open items: H-PHOTON and GA1-5-Φ as a cone (`CN1.md` line 58).
2. **The link sector as a named lattice gauge theory.** Using Balaban-type or BBS-type results on a law needs the gauge-invariant link sector to equal a named U(1) lattice gauge theory, with a Gaussian (large-register) limit. That is wall W1. `GB1.md` line 15 lists "GB1-U1 and GB1-SU2 beyond the proved sectors" as open; its Amendment 1 (line 7) refutes the finite abelian rungs as ZM1-INV readouts and says "The U(1) quantum-link rung is untouched".
3. **The photon mass.** No law has a photon mass term or a mechanism that gives one, and the TOE target needs a massless photon. In M″ the mass is only a regulator. Its framework counterpart would be a finite zoom depth or a finite box. R1″-MOD[d] with constants independent of `N` is the statement that this regulator can be removed. The nearest framework-side carrier with a mass is #9943: a supplied Gaussian, large-register photon with a Stueckelberg mass on the cube tick in its small-step limit ("Supplied model, finite diagnostic: small-step limit, flat cell, Gaussian registers, supplied gauge fixing and photon mass", consolidation note line 1191; status "logged").
4. **Euclidean integral versus tick.** M″'s RG acts on a Euclidean functional integral. The laws are unitary ticks. Transferring UB″ to a law needs a transfer-matrix identification of the tick with a reflection-positive Euclidean weight; that is part of R2-a (H-TICK) and of ST1. None was found in the files read for this lane.
5. **What the speeds are.** M″'s speeds are coefficients of effective actions, that is, gauge-fixed charged two-point data. ZM1-INV maps only invariant algebras ("Impose no map on charged fields or Gauss generators", `TOE_ASSEMBLY.md` line 252). `CN1.md` line 161 (GAP 6.2) already says such a coefficient "has no supplied identification with a ZM1-INV observable; R1-OBS or another bridge is needed".

So M″ realises rung 1 of W3 as a supplied model, as `TOE_ASSEMBLY.md` line 730 allows ("two species coupled to one U(1) field in a solvable or perturbative-with-bounds model"). Rung 2 needs items 1-5. Nothing in this file selects a law or a reading.

## 6. Smuggle checks

This file proposes four things; none is adopted. The four tests ask whether a proposal (1) states or fixes a part's target, (2) is open-ended so that a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. P is pass, C conditional, F fail.

| Proposal | 1 | 2 | 3 | 4 | Reason |
|---|---|---|---|---|---|
| M″ as the supplied rung-1 model for R1″ (section 3.1) | P | P | P | C | (1) It is a test model; W3's ladder asks for one ("a solvable or perturbative-with-bounds model", `TOE_ASSEMBLY.md` line 730) and it fixes no framework target. (2) The action, covariance and parameters are fully listed. (3) It decides nothing about the framework's photon or matter (section 5). (4) Conditional: the Wilson term costs two fermion-mass counterterms that a node-protected lattice Dirac operator would not need; the photon mass is the regulator R1″ itself asks for; the Feynman–Stueckelberg covariance is a gauge choice that adds no physical constant. |
| R1″-MOD[d] as the precise form of `CN1.md`'s R1″-MOD for M″ (section 3.5) | P | P | P | P | (1) It restates CN1's own R1″-MOD; the window clause is the lane's "contracts scale by scale". (2) Closed. (3) It concerns a supplied model only. (4) It replaces the interpolation of R1-MOD by the discrete steps an RG actually has, and adds no constant. |
| UB″ as the sub-lemma a proof must supply (section 3.5) | P | P | P | P | (1) It is a sufficient condition (Theorem 3), not a target. (2) Closed list (U0)-(U5). (3) Nothing downstream is assumed. (4) Each item is used once in Theorem 3: (U0) for `δ_0`, (U1)-(U2) for Lemma 2, (U3) for `E_k`, (U4) for the rate, (U5) for `Λ_min`; each term of `η_k` has its own source (one-loop remainder, lattice, photon mass). |
| TD: pose UB″ on a tangent disc of the bare coupling, equivalently on a fixed disc of the running couplings (section 4.4) | P | P | P | P | (1) It fixes no target. (2) Closed. (3) It is a statement about domains of analyticity, not physics. (4) Corollary 4″ shows a full disc is impossible and Proposition 5 shows the tangent disc is invariant; nothing more is added. |

The owner guidance ("we can specify if needed") is met by these specifications: each is a precise form of an item already on file, not a new axiom.

## FINISH

**Proved here (author-side; not yet distilled or refereed).**
- Formula (3.2): the one-loop drag `F(v,c) = P(v,c)(c − v)` of (OL) is strictly decreasing in `v/c` at every positive ratio, so the pair drag `Λ_k` is positive on every box of positive speeds.
- Theorem 1: per-scale bounds of the stated form give `|Δ_N| + κE_N ≤ C(1 + b_+G_0N)^{−λ/b_+}(|Δ_0| + κE_0)` with `C` independent of `N`, and strict contraction at every scale of a window whose margins do not depend on `N`.
- Lemma 2: an exchange-odd difference is Lipschitz, with constant `M/r`, once the remainder is bounded by `M` on a complex `r`-neighbourhood. This settles the Lipschitz half of attack 3's failing step.
- Lemma 3a: the discrete box, from the discrete (R-i) and smallness.
- Theorem 3: UB″ implies R1″-MOD[d], with constants independent of `N`.
- Proposition 4 and Corollaries 4′ (conditional on the one-loop coefficients `CN1.md` imports) and 4″ (no import): no bound on a disc of the bare coupling with radius independent of `N` is compatible with the decay that UB″ and R1″-MOD[d] assert.
- Proposition 5: on a disc tangent to the imaginary axis the coupling recursion stays small for all scales; a negative bare coupling `−t` leaves the small region within `2/(bt) + 1` scales.
- Lemma 6: the continuum one-loop zero-momentum quartic photon term vanishes, for every speed and every regulator that depends on one homogeneous norm.

**Counterexamples.**
- Corollary 4″ refutes the statement "UB″ holds with bounds analytic on a disc of the bare coupling whose radius does not depend on `N`". This refutes a proof strategy (attack A, and attack 2 on file in its massive form), not R1″-MOD.
- No counterexample to R1″-MOD[d] was found. Section 3.4 shows that M″ has no exchange-odd datum that could act as a persistent source of the R1-D kind.

**Open by name.**
- **UB″**, equivalently (by Theorem 3) **R1″-MOD[d]** for M″. Three new attacks failed, by name: **A**, analytic bounds in the bare coupling uniform in `N` (fails at Corollary 4″, proved); **B**, gauge-covariant block-spin RG with background-field fermions (fails at **B1**, the 3+1-dimensional, `N`-uniform analyticity and decay of the fermion block operators on the small-field set); **C**, finite-range RG with polynomial localisation (fails at **C1**, stability without a sign for the generated quartic photon couplings).
- **B2** (fermionic decoupling across large-field regions); the lattice sign of the quartic photon coupling in attack C.
- The discrete spread theorem for `n` species with unequal charges (only equal-charge pairs are treated here; `CN1.md` Theorem 3 covers continuous flow time).
- Inherited, unchanged: R1-MOD, R1′, R1-OBS, CN1-T, CN1-T(r), R2 (R2-a/H-TICK, R2-b/H-TRANSFER, R2-c), R3, R-P, H-PHOTON, H-THR, H-FIN; GB1-U1; GA1-5-Φ as a cone; VC1; ZM1-I1[INV].

**What changes downstream.**
- *CN1.* R1″-MOD reduces to UB″ (Theorem 3). (R-iii) needs no separate Lipschitz hypothesis (Lemma 2). Any proof has to expand in running couplings, on a tangent domain of the bare coupling (Corollary 4″, Proposition 5). Attack 2's failure for the massive case is now a theorem. A possible amendment line, for the lead and the owner to judge: "R1″-MOD reduces to UB″ (`CN1MOD` Theorem 3); attacks A, B, C failed at Corollary 4″, B1, C1." Proposed, not adopted.
- *LZ1.* Nothing new. The rate in Theorem 1 is a power of `N = log_L(1/m)`, as `LZ1I.md` Theorem 12 requires of a marginal drag; R-P still needs another mechanism.
- *GA1, GB1, ST1.* M″ becomes rung 2 only with the five inputs of section 5 (a photon with a cone, GB1-U1 with a Gaussian limit, removal of the mass regulator, a transfer-matrix identification of the tick, and an invariant meaning for the speeds).
- *Owner.* Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
