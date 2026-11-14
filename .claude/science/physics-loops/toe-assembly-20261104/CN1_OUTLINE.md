lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# CN1: a common light cone by interaction (wall W3), assembly outline and rung 1, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method (Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen).

**What this file is.** The assembly outline for wall W3 (`TOE_ASSEMBLY.md` §11), in the Sussman–Alpoge form, and an author-side attack on its first rung. It grants no status. It adopts no law, no reading and no axiom change. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "Ported" means: proved in a named prior file; that file's status is stated where it is used. "[check]" marks a tiny scratch computation in `/tmp/toe-CN1/`; a check guides and never proves. Every proof below is pen-and-paper mathematics (real analysis of ordinary differential equations, linear algebra, elementary calculus) and can be formalised in Lean. No proof uses a computer.

**Source revisions read.**

| Ref | Commit |
|---|---|
| local branch `claude/toe-assembly` (this checkout) | `1e078a90f` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd0` |
| `origin/claude/ym4d-hard-route` (read with `git show` only) | `fe6f69a33` |
| `origin/docs/consolidate-lorentz-dispersion` (read with `git show` only) | `586d7c81d` |

Files read at those commits, by line. This folder: `prior/CN1.md` lines 1-79 (all); `TOE_ASSEMBLY.md` lines 201-256 (§3.4-3.9), 296-369 (ZM1, TM1, ST1, LZ1), 712-726 (§11); `LZ1I.md` lines 1-224 (all); `LZ1.md` lines 1-46 (status, amendments, §1 definitions), 50, 62-66 (Theorems 2.1-2.2, Corollary 2.3), 165; `LW1.md` lines 14-72 (amendments, free data, §1 definitions, the law `L_cube`); `ZM1I1A.md` lines 1-48; `ZM1.md` lines 372-378 (Lemma R-GI); `GA15PHI.md` lines 1-12 (status); `Y2W_DRAFT.md` lines 1-40 (format only). `origin/main`: `docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` (the "Peierls note") lines 1-60, 149-180, 405-520; `docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md` lines 15-24, 66-78; `docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` lines 18-30; `docs/VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md` lines 22-28, 86-95; `docs/LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md` lines 22-26, 42-48. `origin/docs/consolidate-lorentz-dispersion`: `docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 79-134 (the #9913 entry). YM branch, `.claude/science/physics-loops/ym4d-hard-route-20261030/library/ym4-assembly.md` lines 1-60 and its section list, `library/t0-tree.md` lines 1-30 and its section list, as the model of an outline.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The laws and readings on file are read plainly. Section 7 records readings that CN1 needs; none is adopted.

**Working set used, by name.** PS-1 (one update axis; the tick) and the owner's NN-a (`TOE_ASSEMBLY.md` line 235), through the admissible-update class of `LZ1I.md` §1. PS-5 and PS-6r only through the laws `L5-U[m]`, `L5-O[S_+]` and `L_cube` as named objects. The owner decisions LZ1-SC (line 229), ZM1-I1[a] with `p=2` (line 243) and ZM1-INV (line 252), quoted where used. The working candidate R-CS^str (line 225), named and not used as a premise. Frozen results used, by name: `LZ1.md` Theorems 2.1-2.2 and Corollary 2.3; `ZM1.md` Lemma R-GI; `LZ1I.md` Theorems 7-9, 10′, 11, 12 and RC-Z; `GA15PHI.md` status line (no identified photon).

**Inputs from outside the working set.** Standard mathematics, rebuilt in the text: existence and uniqueness for locally Lipschitz ordinary differential equations; the Dini-derivative monotonicity lemma; comparison (barrier) arguments for scalar differential inequalities; Grönwall's inequality. Two one-loop coefficient functions of continuum quantum electrodynamics with unequal speeds are ported from the Peierls note on `origin/main` (status there: conditional-support, unaudited), and one is re-derived here from the Lorentz-invariant vacuum-polarisation coefficient by a change of coordinates (Lemma V). That Lorentz-invariant coefficient, `d(1/e²)/dℓ = 1/(6π²)` per Dirac fermion, is the textbook one-loop result; it is imported, not rebuilt, and it fixes only the numerical exponent of Theorem R1-B, never the convergence. Literature is listed in §1 with arXiv numbers and equation numbers; none of it is load-bearing.

---

## 0. The question, quoted

`TOE_ASSEMBLY.md` line 720, wall W3: "**W3. A common light cone, CN1** (feeds LZ1, ST1, GR). Target theorem: under the owner's zoom (ZM1-INV), species that interact through a common gauge field have speed differences that flow to zero. Programme: Chadha–Nielsen's "Lorentz invariance as a low-energy phenomenon" and its successors. The frozen counterexample LZ1-i (two free neutral species keep different Clifford speeds) is the free rung's answer; interactions are the escape. Ladder: rung 1, two species coupled to one U(1) field in a solvable or perturbative-with-bounds model; rung 2, the framework's own gauge layer; rung 3, every species. First rung to work: rung 1."

`TOE_ASSEMBLY.md` line 356, LZ1(a): "there are `c > 0` and `p >= 2` such that, for every light species (fermions, gauge bosons, graviton), the low-momentum dispersion is `E = c|k|(1 + O((a|k|)^p))` with the same `c`; ... [**open input LZ1-i**: a mechanism that fixes one common `c` across species]".

`TOE_ASSEMBLY.md` line 252, the zoom (owner, 2026-11-07): "Replace the full-algebra map by a unital injective *-homomorphism \(\Phi:\mathfrak A_1^G\longrightarrow\mathfrak A^G\). ... Impose no map on charged fields or Gauss generators."

The lane brief's rung-1 target: two species of different bare speed coupled to one U(1) gauge field, in a model where the flow of the speed difference can be controlled with explicit bounds; prove that the difference shrinks under the zoom at a stated rate, or give a counterexample; and say which hypothesis of Chadha–Nielsen fails on a framework tick.

## 0.1 Outcome in one paragraph

**Target.** CN1-T (§2) states W3 in standard mathematics: along a ZM1-INV zoom, the threshold sets of all invariant light observables collapse to one cone, `lim_{κ→0} limsup_k Δ_k(κ) = 0`, for a vacuum with a photon band (T1) whose other light species carry Gauss charge (T2). The ladder (§3) runs R0 (free and decoupled, frozen), R1 (one U(1), two charged species), R2 (the framework's U(1) layer), R3 (every species), with a side rung R-P for LZ1's power rate. **Rung 1, proved at the level of flows:** the `n`-species one-loop flow with unequal speeds converges globally for any positive coefficients (Theorem R1-A); for two species of equal charge the difference decays as `(C + o(1))ℓ^{−2q²/W}`, exponent `1` for two unit-charge Dirac species (Theorem R1-B); the rate survives every exchange-symmetric `O(G²)` remainder and integrable forcing (Theorem R1-C). **Counterexample:** a persistent source of the drag's own order fixes a permanent offset (Proposition R1-D). **Open:** that a real lattice model of rung 1 has a flow in the remainder class (R1-MOD); three attacks fail at named steps (sum over orders; scale-summability of the massless photon kernel; size estimate from Ward identities). **On a framework tick** the failing hypothesis of Chadha–Nielsen is H1: the speed of a charged two-point function is not an observable there (Lemma 6.1, `LZ1.md` Theorem 2.2, ZM1-INV), so CN1 reads speeds from thresholds of invariant spectral measures. The rate is a power of the zoom level, not of the scale, so LZ1's `p ≥ 2` needs more than this mechanism.

## 1. Literature

Fetched 2026-11-07 with WebSearch and WebFetch (arXiv abstract pages, ar5iv full text, INSPIRE records). The fetch tool limits verbatim quotation; where it paraphrased, this file says "summary" and quotes only short phrases. Nothing in this section is load-bearing.

**1.1 The programme.**
- **[CN] S. Chadha, H. B. Nielsen**, "Lorentz invariance as a low-energy phenomenon", Nucl. Phys. B 217 (1983) 125-144, DOI 10.1016/0550-3213(83)90081-0. No arXiv number. Fetched: the INSPIRE record only. Abstract (summary): symmetries seen in nature are to be "regarded as infrared attractive fixed points"; a non-covariant model of electrodynamics is studied by its β-functions; it mimics Lorentz invariance better as the energy scale decreases. **The paper's text is NOT VERIFIED** (not fetched). No equation or hypothesis of [CN] is quoted from the paper. The hypotheses H1-H7 of §6 are the mechanism as restated by [KLP], [IN], [AD] and the Peierls note, which were read.
- **[NN78] H. B. Nielsen, M. Ninomiya**, "β-function in a non-covariant Yang-Mills theory", Nucl. Phys. B 141 (1978) 153-177, DOI 10.1016/0550-3213(78)90341-3. Fetched: INSPIRE record. Abstract (summary): lowest order in the coupling and in the deviation from covariance; Lorentz invariance becomes more accurate at smaller mass scales; the relative deviation falls as `α_S^{-7/11}`. Text NOT VERIFIED.
- **[NN81]** Nielsen-Ninomiya fermion-doubling theorem (Nucl. Phys. B 185 (1981) 20): not fetched, NOT VERIFIED, not used.
- **[KLP] V. A. Kostelecký, C. D. Lane, A. G. M. Pickering**, "One-loop renormalization of Lorentz-violating electrodynamics", Phys. Rev. D 65 (2002) 056006, arXiv:hep-th/0111123. Read on ar5iv: the β-functions displayed after Eq. (27) (the page drops that display's number): "(βc)μν = q²/(6π²)(cμν + cνμ − (kF)μαν^α)" and `(β_{k_F})_{κλμν} = q²/(6π²)[(k_F)_{κλμν} − ½η_{μκ}(c_{νλ}+c_{λν}) + ½η_{νκ}(c_{μλ}+c_{λμ}) + ½η_{μλ}(c_{νκ}+c_{κν}) − ½η_{νλ}(c_{μκ}+c_{κμ})]`; the running solution Eq. (34), with `Q(μ) = 1 − (q₀²/6π²) ln(μ/μ₀)` and the factor `1 − Q^{-3}`. §5.2 below contracts these to one relative coefficient.
- **[IN] H. Isobe, N. Nagaosa**, "Theory of a quantum critical phenomenon in a topological insulator: (3+1)-dimensional quantum electrodynamics in solids", Phys. Rev. B 86 (2012) 165127, arXiv:1205.2427. Read on ar5iv: Eqs. (9)-(11) are the one-loop flows of the electron speed `v`, the photon speed `c` and the coupling `e²/ε`; Eq. (12) the coupling `α = e²/(εc²v)`; Eq. (14) the solution; Eqs. (15a), (15b) two crossover scales. Quoted: "the speed of electron v and that of photon c approach to the same value c∞ = (c₀²v₀)^(1/3) in the infrared (IR) limit". The electron equation carries the factor `1 + 2x + x² − 4x³ = (1 − x)(4x² + 3x + 1)`, `x = v/c`, the same factor as the Peierls note. The overall powers of `c` in the rendered equations were not compared with ours.
- **[AD] M. M. Anber, J. F. Donoghue**, "The emergence of a universal limiting speed", Phys. Rev. D 83 (2011) 105027, arXiv:1102.0789. Abstract: "The differences normally vanish only logarithmically". Read on ar5iv: Eq. (54), `β(η) = (b g²/4π²c³) η + O(η²)` for `η = c_b/c_f − 1`; Eq. (57), `η(μ) = η*[g²(μ)/g²(μ*)]^{2b/5}`; §VIII, a power-law model in which the number of active species grows as a power of the scale (Eqs. (58), (63)-(65)).
- **[IRS] R. Iengo, J. G. Russo, M. Serone**, "Renormalization group in Lifshitz-type theories", JHEP 0911 (2009) 020, arXiv:0906.3477. Abstract: "A logarithmic running of c² persists also at low-energies, if δc² ≠ 0 in the UV"; Lorentz symmetry needs the breaking terms "unnaturally fine-tuned".

**1.2 Fixed points with power-law approach.**
- **[RJH] B. Roy, V. Juričić, I. F. Herbut**, "Emergent Lorentz symmetry near fermionic quantum critical points in two and three dimensions", JHEP 04 (2016) 018, arXiv:1510.07650. Abstract: "all three velocities ultimately flow to a common terminal velocity", "non-universal and different from the original velocity of light" (one-loop ε-expansion).
- **[VTF] O. Vafek, Z. Tešanović, M. Franz**, "Relativity restored: Dirac anisotropy in QED₃", Phys. Rev. Lett. 89 (2002) 157003, arXiv:cond-mat/0203047. Abstract: anisotropic QED₃ "renormalizes to an isotropic limit" (leading order in `1/N`).
- **[BPS] G. Bednik, O. Pujolàs, S. Sibiryakov**, "Emergent Lorentz invariance from strong dynamics: holographic examples", JHEP 11 (2013) 064, arXiv:1305.0011. Abstract: deviations are "power-law suppressed" "by the ratio of the infrared and ultraviolet scales". **[KS] I. Kharuk, S. Sibiryakov**, arXiv:1505.04130 (chiral fermions; abstract only, no rate stated there).

**1.3 Rigorous renormalised dispersion.**
- **[GMP12] A. Giuliani, V. Mastropietro, M. Porta**, "Lattice quantum electrodynamics for graphene", Ann. Phys. 327 (2012) 461-511, arXiv:1107.4741. Abstract: "We show that the Fermi velocity increases up to the speed of light"; the renormalised expansion is "finite at all orders". Fermions live in 2+1 dimensions, the photon in 3+1.
- **[GMP10]** same authors, "Anomalous behavior in an effective model of graphene with Coulomb interactions", Ann. Henri Poincaré 11 (2010) 1409-1452, arXiv:1001.5347: series in running couplings with explicit bounds "at all orders". **[P11] M. Porta**, thesis, arXiv:1105.1368: "the effective Fermi velocity flows to the speed of light", "at all orders in renormalized perturbation theory".
- This lane's searches found no convergent (beyond all orders) construction of the infrared flow of 3+1-dimensional QED with massless charged fermions, with or without unequal speeds. That is a search result, not a claim about the literature as a whole.

**1.4 Naturalness, gauge charges, link models.**
- **[CPSUV] J. Collins, A. Perez, D. Sudarsky, L. Urrutia, H. Vucetich**, "Lorentz invariance and quantum gravity: an additional fine-tuning problem?", Phys. Rev. Lett. 93 (2004) 191301, arXiv:gr-qc/0403053. Abstract: a Planck-scale preferred frame with known interactions "gives rise to Lorentz violation at the percent level" unless bare parameters are "unnaturally strongly fine-tuned".
- **[Pol] J. Polchinski**, arXiv:1106.6346, Class. Quantum Grav. 29 (2012) 088001. Abstract: "the only known exceptions are based on supersymmetry".
- **[Bu] D. Buchholz**, "Gauss' law and the infraparticle problem", Phys. Lett. B 174 (1986) 331-334 (INSPIRE). Abstract (summary): a state with a charge measurable by Gauss' law is not an eigenstate of the mass operator.
- **[HFB] M. Hermele, M. P. A. Fisher, L. Balents**, "Pyrochlore photons", Phys. Rev. B 69 (2004) 064404, arXiv:cond-mat/0305401: an emergent photon, "a gapless, linearly dispersing" mode, with "gapped S^z = 1/2 spinons carrying the U(1)" charge.
- **[PMML] S. D. Pace, S. C. Morampudi, R. Moessner, C. R. Laumann**, "The emergent fine structure constant of quantum spin ice is large", Phys. Rev. Lett. 127 (2021) 117205, arXiv:2009.04499: the constant is "more than an order of magnitude greater than α_QED".

**1.5 What the literature gives CN1.** (a) The mechanism is established at one loop and at all orders in renormalised perturbation theory [KLP, IN, AD, GMP12]. (b) For an infrared-free U(1) the approach is logarithmic [AD, IN, KLP]. A power-law approach appears with an interacting fixed point [RJH, VTF], strong dynamics [BPS], or a growing number of species [AD §VIII]. (c) No convergent construction for 3+1 dimensions was found. (d) Finite offsets are natural at the size of the coupling unless a symmetry protects them [CPSUV, Pol]; #9913 finds such an offset on a framework-type tick (§6, H7). (e) Gauss-law charges have no sharp mass shell [Bu]; in link-model U(1) phases the charges are gapped [HFB] and the coupling need not be small [PMML].

## 2. The target theorem (CN1-T)

Open inputs are written inside statements as ⟦open: NAME⟧, as in the YM outline. Each name is owned by the part listed in the FINISH block.

### 2.1 Framework objects, by file and line

- **Algebra and gauge group.** The quasi-local algebra `𝔄` of matter and link registers and the local gauge transformations `e^{itG_x}`: `LW1.md` lines 45-60 (`L_cube`); for the five-mode laws, `ZM1I1A.md` §1 item 1 and `LW1_5.md`. `𝔄^G` is the subalgebra fixed by every local gauge transformation.
- **Update.** An *admissible update* is the base tick `U₀ = W_E M_o M_e` with finitely many appended gauge-invariant layers, implementable under NN-a: `LZ1I.md` line 19 ("Call such an update *admissible* here"); NN-a is `TOE_ASSEMBLY.md` line 235. `α(A) = U*AU`.
- **States.** A *D1 state* is stationary, invariant under the translations `τ_β` by `2β`, `β ∈ Z³`, and under the local centre actions: `LZ1.md` line 40 and `LZ1I.md` line 21. Its GNS data are `(H, π, Ω)`, the tick implementer `Ũ`, the translation implementers `T_β`, and `H_phys = closure(π(𝔄^G)Ω)` (`LZ1.md` §1).
- **Bands.** `LZ1I.md` line 23: "A band `(d,F,V)` consists of an isometry `F:L²(T³;C^d)→H` and continuous `V:T³→U(d)` with `T_βF=F e^{iK·β}` and `ŨF=FM_V`. A node has `V(K₀)=1` and `V` is `C¹` nearby. Set `h=i log V` and `N_i=∂_i h(K₀)`. It propagates if some `N_i≠0`; it has a Clifford cone of speed `v>0` if `{N_i,N_j}=2v²δ_ij`." Under LZ1-SC (`TOE_ASSEMBLY.md` line 229) the dispersion clause counts only band images in `ker(Ũ−1)^⊥`.
- **Photon band.** A band in `H_phys` is *flux-carrying* under the proposed R-Φ (`GA1_5.md` line 61) "if its image is orthogonal to `closure π(𝒩)Ω`". A *photon band* below means a flux-carrying band with a Clifford cone. None is constructed: `GA15PHI.md` line 5 calls its band "an exact one-way band in a chosen stationary state, not an identified photon or a Clifford cone".
- **Charged species.** `LZ1.md` line 62, Theorem 2.2: "every odd light species in the proposed sense is flat there, with `N_j=0`". So a charged fermion has no band reading under R-loc. Its prescription is the working candidate R-CS^str (`TOE_ASSEMBLY.md` line 225), not adopted.
- **Zoom.** A *zoom trajectory* is a sequence of R-form tick systems `(𝔄_k, α_k, ω_k)`, `k ≥ 0`, with `(𝔄_0, α_0, ω_0)` the fine data, and maps `Φ_k : 𝔄_{k+1}^G → 𝔄_k^G` as in ZM1-INV (`TOE_ASSEMBLY.md` line 252): unital, injective, *-homomorphic, cell covariant, exponentially local, with block factor `L ≥ 2` and one coarse tick equal to `L` ticks of the level below. Consecutive levels meet the class-(a) comparison with `p = 2` (line 243).

### 2.2 Speed functionals (proposed reading CN1-OBS; four-tested in §7)

Fix a level `k`, write `(α, ω)` for `(α_k, ω_k)`, and let `A ∈ 𝔄^G` be local. Put `ξ_A = π(A)Ω − ω(A)Ω`. Let `μ_A` be the joint spectral measure of the commuting unitaries `(Ũ, T)` in `ξ_A`, a finite measure on `(λ, K) ∈ (−π, π] × T³`. Fix `0 < κ ≤ 1` and the window `W(κ) = {(λ, K) : |λ| ≤ κ, 0 < |K| ≤ κ}`. Call `A` *light at `κ`* if `μ_A(W(κ)) > 0`.

- **Threshold set.** The singular support `ss(μ_A)` is the complement of the largest open set on which `μ_A` has a `C^∞` density with respect to Lebesgue measure. Put `E_A(κ) = closure{ |λ|/|K| : (λ, K) ∈ ss(μ_A) ∩ W(κ) }`.
- **Cone mismatch.** Let `S_k(κ)` be the union of `E_A(κ)` over the light `A` in a named family `𝔉_k` (§2.3). If `S_k(κ)` is nonempty and bounded away from `0`, put `Δ_k(κ) = (sup S_k(κ) − inf S_k(κ)) / inf S_k(κ)`.

Three facts fix the meaning. (i) A band with a Clifford cone of speed `v` has spectral measure on the graph `λ = ±v|K| + O(|K|²)`, a Lebesgue-null set; so `E_A(κ) ⊂ [v − Cκ, v + Cκ]` for `A` creating it. (ii) A free massless species of speed `v_a` gives its invariant bilinears a pair continuum with density supported in `|λ| ≥ v_a|K| + O(|K|²)` and not smooth across that edge; so its threshold set lies within `Cκ` of `v_a`. (iii) For two decoupled species of speeds `v₁ < v₂`, `Δ_k(κ) ≥ (v₂ − v₁)/v₁ − Cκ`. The support of `μ_A` alone would not do: interactions fill the region above the slowest cone, so a faster species hides inside it. Its threshold stays visible as a point of non-smoothness. A common light cone means every threshold of every invariant light observable sits on one cone.

### 2.3 Statement

**Target Theorem CN1-T.** Let `L` be `L5-U[m]`, `L5-O[S_+]` or `L_cube`, with an admissible update that contains a magnetic (plaquette) layer ⟦open: plaquette class, `LW1.md` line 30; GA1-P-5⟧, and let `ω` be the VC1 vacuum ⟦open: VC1⟧. Let `(𝔄_k, α_k, ω_k, Φ_k)` be a ZM1-INV zoom trajectory meeting class (a) with `p = 2` at every step ⟦open: ZM1-I1[INV]⟧. Assume:
- (T1) *Coulomb phase.* For every `k` the light sector of `ω_k` contains a photon band with speed `c_k > 0` ⟦open: GA1-5-Φ as a Clifford cone⟧.
- (T2) *Charged light matter.* Every light band or light continuum of `ω_k` that is not made of photons alone is generated, through invariant local observables, by species that carry nonzero Gauss charge in the R-CS^str sense ⟦open: R-CS, MT1-S[R-CS]⟧. Pair continua of charged species are allowed. A light neutral bound state would be a neutral species and is excluded: its photon couplings are multipoles, which are irrelevant, and in the two-sector flow of `LZ1I.md` Theorem 11 an irrelevant coupling gives a convergent drag integral, hence no alignment.

Let `𝔉_k` be the invariant local observables of `𝔄_k^G` that are light at `κ`. Then
\[
\lim_{κ→0}\ \limsup_{k→∞}\ Δ_k(κ) = 0 .
\]
**Rate form CN1-T(r).** There are `C, γ > 0` with `Δ_k(κ₀) ≤ C(1 + k)^{−γ} + Cκ₀` for a fixed window `κ₀`.

### 2.4 What CN1-T leaves out, and why

- *Neutral species.* (T2) excludes them. They are not a gap of the outline: `LZ1I.md` Theorem 9 (line 117) proves that a universal common-speed claim over its class is false; its two neutral bands keep speeds `sin θ₁/√3 ≠ sin θ₂/√3`. Rung 3 treats the neutral case as a separate statement.
- *The power rate.* LZ1(a) asks `E = c|k|(1 + O((a|k|)^p))`, `p ≥ 2`. In zoom levels that is `Δ_k = O(L^{−pk})`. CN1-T(r) asks only `(1+k)^{−γ}`. Theorem R1-B below shows the U(1) mechanism gives exactly a power of `k`, so LZ1's rate needs a further input (§4, hard step H-RATE).
- *Finite matching.* CN1-T is a statement about limits. It says nothing about the size of `Δ_k` at the level where the charged matter becomes massive; #9913's finite offset (§6, H7) lives there.
- *The graviton.* GR2 owns the tensor modes; CN1-T does not name them.

## 3. The ladder

Status words: **[F]** frozen in this folder; **[Pt]** ported from a named prior file, with that file's status; **[P]** proved here, not yet checked; **[O]** open. Each rung names its imports and which steps are ported and which are new.

### R0. Free and decoupled species keep their speeds [F]

**Statement.** Let a D1 state carry two bands in `H_phys ∩ ker(Ũ−1)^⊥` with Clifford speeds `v₁ ≠ v₂`, and let a zoom with `M` fine ticks per coarse tick and `L′` fine cells per coarse cell meet the band comparison of `LZ1I.md` Theorem 10′. Then the coarse system carries the speeds `(M/L′)v₁ ≠ (M/L′)v₂`. With `c_t = c_s` graining, `M = L′ = L`, so `Δ_k(κ) ≥ |v₁ − v₂|/min(v₁,v₂) − Cκ` at every level.
**Imports.** `LZ1I.md` Theorems 7-9, 10′ and RC-Z (frozen; RC-Z and 10′ are referee closures, unrefereed). **Assignment.** All ported. Nothing new. This is the free rung's answer: without a connecting interaction, the zoom keeps the split.

### R1. One U(1), two charged species, one-loop flow with bounds [P] + [O]

**Model M1.** Continuum QED in 3+1 dimensions with `n` massless Dirac species `a` (multiplicity `n_a > 0` in Dirac units, charge `q_a ≠ 0`, speed `v_a > 0`), one photon with Lagrangian `½(εE² − μ^{-1}B²)` and speed `c = (εμ)^{-1/2}`, coupling `G = e²/ε`, Wilsonian scale `ℓ = log(Λ/scale)`. Its one-loop flow (OL) is stated in §5.1.
**Statements.**
- **R1-A** (global convergence) [P]: for all positive data, (OL) has a unique global solution; the speeds stay in their initial hull; the spread `D(ℓ)` obeys `D(ℓ) ≤ C(1+ℓ)^{−γ}` with explicit `γ > 0`; all speeds converge to one `c_∞ > 0`.
- **R1-B** (sharp rate, equal charges) [P]: if `q₁ = q₂ = q` and `v₁(0) ≠ v₂(0)`, then `v₁ − v₂ = (C + o(1)) ℓ^{−2q²/W}` with `C ≠ 0`, `W = Σ_b n_b q_b²`. Two unit-charge Dirac species: exponent `1`.
- **R1-C** (robustness) [P]: R1-A and R1-B persist for flows in the remainder class `𝓡` of §5.4 (exchange-symmetric `O(G²)` remainders; forcing integrable against `(1+ℓ)^{2q²/W}`). A persistent marginal forcing destroys convergence.
- **R1-MOD** (the model has such a flow) [O]: the lattice-regularised M1 has a multiscale sequence of effective actions whose quadratic coefficients `(v_a(k), c(k), G(k))` solve (OL) up to a remainder in `𝓡`. Failed attacks in §5.6.
- **R1-OBS** (the flow variables are the thresholds) [P at zero coupling in the continuum, Proposition R1-OBS₀; O beyond]: in M1 at scale `k`, `S_k(κ)` lies within `C(κ + G_k)` of `{v_a(k)} ∪ {c(k)}` and meets each of them within the same distance. At zero coupling this is fact (ii) of §2.2.

**Conclusion of the rung.** R1-A, R1-B, R1-C, R1-MOD and R1-OBS give CN1-T(r) for M1 with `γ = 2q²/W` (equal charges).
**Imports.** The one-loop coefficient functions `P` (fermion) and `R, S` (photon, coupling), ported from the Peierls note on `origin/main` (conditional-support, unaudited) and cross-checked against [IN] Eq. (9) and [KLP]; `R` and `S` are re-derived in Lemma V. The textbook Lorentz-invariant vacuum-polarisation coefficient. `LZ1I.md` Theorems 11 and 12 (frozen). **Assignment.** R1-A, R1-B, R1-C: new here (ordinary differential equations). Coefficients: ported. R1-MOD, R1-OBS: new statements, open.

### R2. The framework's own U(1) layer [O]

**Statement.** Let the law be `L_cube`, or the `U(1)` centre of `U(5)` in `L5-U[m]`, with an admissible update that contains a plaquette layer. Let `ω` be a D1 state in which the light sector contains a photon band of speed `c₀` (T1) and one massless charged species of node speed `v₀` in the R-CS^str sense (T2). Let `(α_k, ω_k, Φ_k)` be a ZM1-INV zoom trajectory with class (a), `p = 2`. Then the coarse constants `(v_k, c_k, G_k)` solve (OL) with `ℓ = k log L` up to a remainder in `𝓡`, and `Δ_k(κ) ≤ C(1+k)^{−γ} + Cκ`.
**Imports.** ⟦open: GA1-5-Φ as a Clifford cone⟧ (`GA15PHI.md` has a flux band, not a cone); ⟦open: R-CS⟧; ⟦open: ZM1-I1[INV]⟧; ⟦open: Y2-W⟧ (a small coupling at some scale); ⟦open: VC1⟧. Frozen: `LZ1.md` Theorem 2.2 (why the charged species needs R-CS^str); `ZM1.md` Lemma R-GI; `LZ1I.md` Theorem 10′ and RC-Z.
**New steps.** (R2-a) *Tick loops*: the one-loop logarithms of a tick (Floquet propagators) have the continuum coefficients `P, R, S`, because the logarithm comes from the node region; #9913's check C2 ("the Coulomb part runs with the continuum velocity log 2/(3 pi)") is numerical support, not proof. (R2-b) *Threshold transfer*: extend RC-Z and Theorem 10′ from isolated branches to the edges of continua, so that class (a) carries `S_k(κ)` across a zoom step. (R2-c) *Lattice forcing*: cell-scale terms enter (OL) as a forcing that decays like `L^{−βk}`, `β > 0`; this places them in `𝓡`. The finite offset at the starting level (#9913) is an initial condition, not a forcing.

### R3. Every species [O]

**Statement.** CN1-T in full for the VC1 vacuum of a live law: all light species carrying gauge charge, abelian and non-abelian, with the photon of the unbroken `U(1)`.
**Imports.** R2; GA2 (the non-abelian continuum sector); BK1 (breaking, W4); CH1 (a gauged chiral light sector); [NN78]-type non-abelian drag, re-proved on a tick. Neutral species stay outside (T2); `LZ1I.md` Theorem 9 forces that restriction or another one.
**New steps.** Non-abelian drag on a tick; the end of the flow at confinement or breaking, where gauge bosons and quarks leave the light sector (`LZ1I.md` Theorem 11 then freezes what is left); the photon of the unbroken group after W4.

### R-P. A power rate (side rung, for LZ1, not CN1-T) [O]

**Statement.** A model in which `Δ_k ≤ C L^{−βk}`, `β > 0`. In the literature this needs an interacting infrared fixed point at which relative-speed operators are irrelevant ([RJH], ε-expansion; [VTF], `1/N`), strong dynamics ([BPS]), or a growing number of active species ([AD] §VIII). By R1-B and `LZ1I.md` Theorem 12, the infrared-free U(1) of R1 does not give it.

## 4. Hard steps, and where each is proved first

Each rung has one step that carries most of the risk. For each: the step, why it is the hardest, and the simplest rung on which the trick can be proved first.

**R0.** No hard step. All results are frozen.

**R1. H-CONV (the content of R1-MOD).** *Step:* a non-perturbative bound, uniform over infinitely many infrared scales, showing that the multiscale flow of the speeds of M1 equals (OL) up to a remainder in `𝓡`. *Why hardest:* (a) the coupling decays only like `1/ℓ`, so per-scale errors do not sum geometrically; they sum only because the remainder is `O(G²)` and `∫G² dℓ < ∞`; (b) the remainder must vanish at equal speeds, which is a structural property (exchange symmetry and Lorentz invariance of the consensus point), not a size estimate; (c) the photon is massless; integrating it out leaves a long-range current-current kernel that is marginal; (d) the known rigorous results stop at all orders of renormalised perturbation theory ([GMP12], [GMP10], [P11]). *Simplest rung for the trick:* **R1′**, the reduced QED of [GMP12] (fermions in a plane, photon in space). There the velocity flow to `c`, lattice Ward identities and all-order bounds exist; the missing step is the sum over orders. A second, simpler home is **R1″**: M1 with a photon mass `m_γ`, so that only `N = log(Λ/m_γ)` scales carry a marginal coupling. The trick there is a remainder bound uniform in `N`; R1-C then gives the spread at the scale `m_γ`, uniformly as `m_γ → 0`.

**R1. H-THR (the content of R1-OBS).** *Step:* identify the flow variables with thresholds of invariant spectral measures beyond one loop. *Why hard:* Gauss-law charges have no sharp mass shell ([Bu]); soft photons change threshold exponents; the threshold location runs with `|K|`. *Simplest rung:* the free theory (fact (ii) of §2.2), then the one-loop current correlator of M1, which is an explicit two-species bubble plus photon mixing.

**R2. H-PHOTON.** *Step:* a photon band with a Clifford cone on a framework tick (T1). *Why hardest:* the frozen constructions give a one-way flux band and neutral modes, not a cone (`GA15PHI.md` line 5); the plaquette class is open law data (`LW1.md` line 30); finite link registers need not give a small coupling (Y2-W; in a spin-ice U(1) phase the emergent fine structure constant is large [PMML] and the charges are gapped [HFB]). *Simplest rung:* `L_cube` at large link spin `S`, where the link register approaches the noncompact Peierls carrier of the main note, whose photon is Gaussian. Prove a Clifford photon band there first, then lower `S`.

**R2. H-TRANSFER (R2-b).** *Step:* carry threshold sets across one zoom step under class (a). *Why hard:* RC-Z assumes a finite branch decomposition (its hypothesis (Z3)); continua have none. *Simplest rung:* free massless species on the cube tick in a quasi-free state. Pair continua are then explicit convolutions of the B10 dispersion `1 − cos w = sin²θ(1 − χ(K))`, and their edges can be compared directly.

**R2. H-TICK (R2-a)** is moderate: the logarithm of a one-loop tick integral comes from the node region, where the tick propagator is the continuum one up to `O(|K|²)`. Its simplest rung is the one-loop fermion speed log on the cube tick with a Gaussian photon.

**R3. H-NA.** *Step:* non-abelian drag, and the end of the flow at confinement or breaking. *Why hardest:* the coupling grows in the infrared, so the drag strengthens and perturbation theory ends; then gauge bosons and quarks leave the light sector, and `LZ1I.md` Theorem 11 freezes whatever offset remains among the light remnants. *Simplest rung:* the one-loop non-abelian drag ([NN78] is the classical computation, text NOT VERIFIED here) on the asymptotically free side, where `g → 0` in the ultraviolet.

**R3 and LZ1. H-FIN.** *Step:* the size of the speed offsets at the level where species become massive. CN1-T, a statement about limits, does not see it; LZ1's observational bounds do. *Simplest rung:* the one-loop finite offset of #9913 on a tick, proved analytically (sign and non-vanishing) instead of numerically.

**R-P. H-RATE.** *Step:* a power rate. *Simplest rung:* [VTF]'s QED₃ at large `N`, where the relative-speed exponent is computed at leading order in `1/N`.

## 5. Rung 1, attacked

Outcome of this section: R1-A, R1-B and R1-C are proved. A persistent marginal forcing is a counterexample to convergence (Proposition R1-D). R1-MOD is open; three distinct attacks fail at named steps (§5.6). R1-OBS is open beyond zero coupling.

### 5.1 The one-loop flow (OL)

Variables: speeds `v_a > 0` (`a = 1,…,n`), photon speed `c > 0`, coupling `G = e²/ε > 0`; `′ = d/dℓ`. Data: `n_a > 0`, `q_a ≠ 0`, `W = Σ_b n_b q_b²`.
\[
\text{(OL)}\qquad
\begin{aligned}
v_a' &= G\,q_a^2\,P(v_a,c)\,(c-v_a),\\
c' &= G\sum_b n_b q_b^2\,R(v_b,c)\,(v_b-c),\\
G' &= -G^2\sum_b n_b q_b^2\,S(v_b),
\end{aligned}
\qquad
P=\frac{4v^2+3vc+c^2}{6\pi^2 c\,(v+c)^2},\quad
R=\frac{v+c}{12\pi^2 c\,v},\quad
S=\frac{1}{6\pi^2 v}.
\]

*Source of the first line (ported).* The Peierls note on `origin/main`, line 174-176, for one Dirac cone pair of charge `e` with gauge action `½∫[Σ E_i² + c² Σ F_ij²]` (its line 47-49, so `ε = 1` and `G = e²`): "dv/dell = v(A_s-A_t) = e^2(c-v)(4v^2+3vc+c^2)/[6 pi^2 c(v+c)^2]". At one loop the self-energy of species `a` sees only its own vertex and the photon propagator, which is proportional to `1/ε`; so `e²` becomes `q_a² G`. The note derives the formula from explicit Feynman-parameter integrals `I_3`, `I_5` (its lines 160-170) and shows gauge independence of the logarithm (its lines 234-255). Its status is conditional-support, unaudited. [IN] Eq. (9) carries the same factor `(1 − x)(4x² + 3x + 1)`.

**Lemma V (photon and coupling lines).** For a Dirac fermion of speed `v` and charge `qe`, the coefficient of `ℓ` in the one-loop photon Lagrangian is `(q²e²/6π²)·½(E²/v − vB²)`. Hence the second and third lines of (OL) hold.

*Proof.* (a) *Input.* For a relativistic fermion of speed one the coefficient is `(q²e²/6π²)·½(E² − B²)`. This is the textbook one-loop vacuum polarisation, `d(1/e²)/dℓ = 1/(6π²)` for the action `−F²/(4e²)`; it is imported. (b) *Rescaling.* Put `y = x/v`. The operator `iγ⁰(∂_t − iqeA_0) + ivγ^j(∂_{x_j} − iqeA_j)` equals `iγ⁰(∂_t − iqeA_0) + iγ^j(∂_{y_j} − iqeÃ_j)` with `Ã_j = vA_j`; the one-form `A_0dt + A_jdx^j` is unchanged. In `(t, y)` the fermion has speed one. Its logarithmic term per unit `dt d³y` is `(q²e²/6π²)·½(Ẽ² − B̃²)`, with `Ẽ = vE` and `B̃ = ∇_y × Ã = v²B`. Since `d³y = v^{−3}d³x`, the term per unit `dt d³x` is `(q²e²/6π²)·½(v²E² − v⁴B²)v^{−3}`, which is the claim. The coefficient of a logarithm does not depend on the regulator; finite parts do, and they are not used. (c) *Flow.* Adding the terms of all species to `½(εE² − μ^{−1}B²)` gives `ε′ = Σ_b n_bq_b²e²/(6π²v_b)` and `(μ^{−1})′ = Σ_b n_bq_b²e²v_b/(6π²)`. With `c² = 1/(εμ)` and `μ = 1/(εc²)`,
\[
\frac{d\log c}{d\ell}=\tfrac12\Big(\mu\,(\mu^{-1})'-\frac{\varepsilon'}{\varepsilon}\Big)=\frac{G}{12\pi^2}\sum_b n_bq_b^2\Big(\frac{v_b}{c^2}-\frac1{v_b}\Big)=G\sum_b n_bq_b^2\,\frac{(v_b+c)(v_b-c)}{12\pi^2c^2v_b},
\]
which is the second line after multiplying by `c`. The vertex charge `e` does not run (Ward identity), so `G′ = −(e²/ε²)ε′`, the third line. □

### 5.2 Consistency of (OL) with the sources

- **(C1) Shared speed.** If all `v_a = v`, put `r = v/c`, `g = G/c`, `N = W`. Then (OL) gives `dr/dℓ = −g(r−1)H_N(r)/(12π²)`, `dg/dℓ = −Ng²(r + 1/r)/(12π²)`, `d log c/dℓ = Ng(r² − 1)/(12π²r)`, with `H_N(r) = 2(4r²+3r+1)/(r+1)² + N(r+1)`. These are the Peierls note's equations, lines 476-480, term by term. (Check: `dg/dℓ = G′/c − Gc′/c² = −(G²N/(12π²c³v))(2c² + v² − c²)`.)
- **(C2) Linearisation.** At `v_a = c = c_∞` put `v_a = c_∞(1+f_a)`, `c = c_∞(1+h)`, `κ = G/(6π²c_∞)`. Since `P(c,c) = 1/(3π²c)`, `R(c,c) = 1/(6π²c)` and `S(c) = 1/(6π²c)`: `f_a′ = 2q_a²κ(h − f_a)`, `h′ = κΣ_b n_bq_b²(f_b − h)`, `κ′ = −Wκ²`, up to quadratic terms. This is the Peierls note's linearised multi-cone flow, lines 427-431.
- **(C3) [KLP].** For one species, contract [KLP]'s β-functions with `k̃_{μν} = (k_F)_{μαν}{}^α`. For symmetric traceless `c_{μν}`, the photon display contracts to `μ dk̃/dμ = (q²/6π²)(k̃ − 2c)` (the four `c`-terms give `−η tr c − (c + c^T)`), and `μ d(2c)/dμ = (q²/3π²)(2c − k̃)`. So the relative coefficient `r = 2c − k̃` obeys `μ dr/dμ = (q²/2π²) r`, a decay exponent `3` against `μ d q²/dμ = q⁴/(6π²)`. In (C2) with `n = 1`, `W = 1`, the matter–photon mode has eigenvalue `2 + 1 = 3` and exponent `3/W = 3`. They agree, and [KLP] Eq. (34) carries the factor `Q^{−3}`.
- **(C4) [IN].** For one species, (OL) gives `d log(c²v)/dℓ = G v(c − v)²/(6π²c²(c+v)²) ≥ 0`, which is second order in `c − v`. So `c²v` is constant to first order, as in [IN]'s limit `c_∞ = (c₀²v₀)^{1/3}`.
- **[check]** `/tmp/toe-CN1/check_r1.py`, output `out.txt` (scipy LSODA, `rtol 1e-11`, `ℓ` up to `10⁹`, under one second): two unit-charge species from `(v₁, v₂, c, G) = (0.6, 1.4, 1, 2)`: fitted exponent of `|v₁ − v₂|` against `1+ℓ` is `−1.0000`; with a third unit-charge spectator, `−0.6667`; the spread `max − min` is nonincreasing at every output step; one species: `c²v` moves from `0.7` to `0.7028`. A check guides and never proves.

### 5.3 Theorem R1-A (global convergence) [P]

**Setting.** Let `P, R : (0,∞)² → (0,∞)` and `S : (0,∞) → (0,∞)` be any locally Lipschitz functions (the one-loop ones are examples). Take positive initial data `v_a(0), c(0), G(0) = G₀`. Put `m(ℓ) = min{v₁,…,v_n, c}`, `M(ℓ) = max{v₁,…,v_n, c}`, `D = M − m`, `B = [m(0), M(0)]`, and
\[
p_-=\min_a q_a^2\cdot\min_{B^2}P,\qquad R_+=\sum_b n_bq_b^2\cdot\max_{B^2}R,\qquad S_\pm=\sum_b n_bq_b^2\cdot\max_B S\ \text{resp.}\ \min_B S .
\]

**Theorem R1-A.** (OL) has a unique solution on `[0, ∞)`, and:
1. `m` is nondecreasing and `M` is nonincreasing; every speed stays in `B`.
2. `G₀/(1 + G₀S₊ℓ) ≤ G(ℓ) ≤ G₀/(1 + G₀S₋ℓ)`.
3. With `τ(ℓ) = ∫₀^ℓ G`, `s₀ = 1/(4R₊)` and `η = (1 − e^{−p₋s₀})/4`: `D(ℓ) ≤ (1−η)^{−1}D(0)e^{−|log(1−η)|τ(ℓ)/s₀} ≤ (1−η)^{−1}D(0)(1 + G₀S₊ℓ)^{−γ}`, with `γ = |log(1−η)|/(s₀S₊) > 0`.
4. All speeds converge to one limit `c_∞ ∈ B`.

For the one-loop functions, on `B`: `P ≥ 1/(6π²M(0))` because `4v² + 3vc + c² ≥ (v+c)²`; `R ≤ 1/(6π²m(0))` because `(v+c)/(cv) = 1/v + 1/c`; and `1/(6π²M(0)) ≤ S ≤ 1/(6π²m(0))`. So every constant above is explicit.

*Proof.* **Local solution.** The vector field is locally Lipschitz on the open set `(0,∞)^{n+2}`, so a unique maximal solution exists on some `[0, ℓ*)`.

**Item 1.** *Dini lemma:* if `f₁,…,f_N` are `C¹` and `F = max_i f_i`, then `D⁺F(ℓ) = limsup_{h↓0}(F(ℓ+h) − F(ℓ))/h ≤ max_{i∈I(ℓ)} f_i′(ℓ)`, where `I(ℓ)` is the set of indices with `f_i(ℓ) = F(ℓ)`. Indeed the indices outside `I(ℓ)` stay below `F(ℓ) − δ` for small `h` by continuity, so `F(ℓ+h) = max_{i∈I(ℓ)} f_i(ℓ+h)` for small `h`, and the difference quotients converge. Apply it to `M`. If `v_a = M`, then `v_a′ = Gq_a²P·(c − M) ≤ 0`. If `c = M`, then `c′ = GΣ_b n_bq_b²R·(v_b − M) ≤ 0`. So `D⁺M ≤ 0` everywhere. A continuous function with `D⁺ ≤ 0` everywhere is nonincreasing: if `M(b) > M(a)` for `a < b`, the function `M(ℓ) − ε(ℓ − a)` with `0 < ε < (M(b) − M(a))/(b − a)` takes a larger value at `b` than at `a`; at the last point `ℓ₀ ∈ [a, b)` where it is at most its value at `a`, its upper Dini derivative is at least `0`, which forces `D⁺M(ℓ₀) ≥ ε > 0`. The same argument gives `m` nondecreasing.

**Item 2.** `G > 0` on `[0, ℓ*)`: the solution with `G(ℓ₁) = 0` is `G ≡ 0`, which is excluded by uniqueness. So `(1/G)′ = Σ_b n_bq_b²S(v_b) ∈ [S₋, S₊]` by item 1. Integrate.

**Global existence.** If `ℓ* < ∞`, the solution stays in the compact set `B^{n+1} × [G₀/(1 + G₀S₊ℓ*), G₀]` inside the open domain, which contradicts maximality. So `ℓ* = ∞`, and by item 2, `τ(ℓ) → ∞`.

**Item 3.** Use `τ` as the variable: `dv_a/dτ = q_a²P(c − v_a)`, `dc/dτ = Σ_b n_bq_b²R(v_b − c)`. Fix `τ₀` and write `M̄, m̄, D̄` for `M, m, D` at `τ₀`. *Case 1:* `c(τ₀) ≤ (M̄ + m̄)/2`. For `τ ≥ τ₀`, `|v_b − c| ≤ D(τ) ≤ D̄`, so `|dc/dτ| ≤ R₊D̄`. Hence on `[τ₀, τ₀ + s₀]`, `c(τ) ≤ (M̄ + m̄)/2 + D̄/4 = M̄ − D̄/4 =: K`. *Barrier:* if `v_a(τ₁) ≤ K` for some `τ₁` in this window, then `v_a ≤ K` on `[τ₁, τ₀ + s₀]`. Otherwise take `τ₂ > τ₁` with `v_a(τ₂) > K` and `τ₃ = sup{τ ∈ [τ₁, τ₂] : v_a(τ) ≤ K}`; on `(τ₃, τ₂]`, `v_a > K ≥ c`, so `dv_a/dτ < 0`, and `v_a(τ₂) < v_a(τ₃) = K`, a contradiction. *Decay above the barrier:* while `v_a > K`, `d(v_a − K)/dτ = q_a²P(c − v_a) ≤ q_a²P(K − v_a) ≤ −p₋(v_a − K)`, so `v_a(τ) − K ≤ (D̄/4)e^{−p₋(τ−τ₀)}`. In both cases `v_a(τ₀ + s₀) ≤ M̄ − ηD̄`. Also `c(τ₀ + s₀) ≤ K ≤ M̄ − ηD̄`, since `η ≤ 1/4`. So `M(τ₀ + s₀) ≤ M̄ − ηD̄`, while `m(τ₀ + s₀) ≥ m̄` by item 1. Thus `D(τ₀ + s₀) ≤ (1 − η)D̄`. *Case 2:* `c(τ₀) ≥ (M̄ + m̄)/2`. The same argument with the lower barrier `m̄ + D̄/4` raises `m` by `ηD̄`. Iterating, `D(τ) ≤ (1−η)^{⌊τ/s₀⌋}D(0)`. Item 2 gives `τ(ℓ) ≥ S₊^{−1} log(1 + G₀S₊ℓ)`, and the second bound follows.

**Item 4.** `M` is nonincreasing and bounded below; `m` is nondecreasing and bounded above; `M − m → 0`. So both converge to one `c_∞`, and every speed lies between them. □

*Remark.* R1-A uses only positivity and local Lipschitz continuity of `P, R, S`. It does not depend on the numerical values of the ported coefficients or on the imported textbook coefficient. Neither do Theorem R1-C(a) and Proposition R1-D below.

### 5.4 Theorem R1-B (the rate, equal charges) [P]

**Theorem R1-B.** Assume R1-A's setting, with `P ∈ C²` and `S ∈ C¹` near the diagonal of `B²` (true for the one-loop functions), and `q₁ = q₂ = q` (the multiplicities `n₁, n₂` may differ). Put `Δ = v₁ − v₂`, `P_∞ = P(c_∞, c_∞)`, `S_∞ = S(c_∞)`. If `Δ(0) ≠ 0`, then `Δ(ℓ) ≠ 0` for all `ℓ`, and
\[
|\Delta(\ell)|=(C+o(1))\,(1+\ell)^{-q^2P_\infty/(S_\infty W)},\qquad C>0 .
\]
For the one-loop functions `P_∞ = 1/(3π²c_∞)` and `S_∞ = 1/(6π²c_∞)`, so the exponent is `2q²/W`. Two unit-charge Dirac species and nothing else: `|v₁ − v₂| ≍ ℓ^{−1}`.

*Proof.* Put `F(v, c) = P(v, c)(c − v)`. Then `Δ′ = Gq²(F(v₁,c) − F(v₂,c)) = −Gq²Λ(ℓ)Δ`, with `Λ(ℓ) = −∫₀¹ ∂_vF(v₂ + θΔ, c) dθ`. The equation is linear in `Δ` with continuous coefficient, so `Δ(ℓ) = Δ(0)exp(−q²∫₀^ℓ GΛ)`, which never vanishes. Since `∂_vF(v,c) = ∂_vP(v,c)(c − v) − P(v,c)` equals `−P(c,c)` at `v = c`, and `|v_a − c_∞|, |c − c_∞| ≤ D` (because `c_∞ ∈ [m(ℓ), M(ℓ)]`), there is `L₁` with `|Λ(ℓ) − P_∞| ≤ L₁D(ℓ)`. By R1-A, `GD ≤ C(1+ℓ)^{−1−γ}`, so `∫₀^∞ G|Λ − P_∞| < ∞`.

Next, `1/G(ℓ) = 1/G₀ + ∫₀^ℓ s`, with `s = Σ_b n_bq_b²S(v_b)` and `|s − WS_∞| ≤ WL₂D`. Put `γ″ = min(γ, 1/2)`. Then `1/G(ℓ) = WS_∞ℓ + E(ℓ)` with `|E(ℓ)| ≤ C(1+ℓ)^{1−γ″}`. Hence `|G(ℓ) − 1/(WS_∞(1+ℓ))| ≤ C(1+ℓ)^{−1−γ″}` for large `ℓ`, and `∫₀^ℓ G = (WS_∞)^{−1}log(1+ℓ) + C₁ + o(1)`. Combining,
\[
\log|\Delta(\ell)|=\log|\Delta(0)|-\frac{q^2P_\infty}{WS_\infty}\log(1+\ell)-C_2+o(1). \qquad\square
\]

*Remarks.* (1) More charged species slow the alignment of a given pair: `W` grows, the coupling falls faster, and the exponent `2q²/W` falls. (2) The species difference is the slowest mode near consensus. In (C2) the matter–photon mode has eigenvalue `2q² + W` and exponent `(2q² + W)/W`, larger than `2q²/W`. For unequal charges the slowest exponent is `λ_min/W`, with `λ_min` the least nonzero eigenvalue of the weighted star matrix of (C2) (Peierls note, lines 437-457, linear level; this file does not prove the nonlinear version). (3) In zoom levels, `ℓ = k log L`. So R1-B gives CN1-T(r) for the truncated flow with `γ = 2q²/W`, and `|Δ_k|` is not `O(L^{−βk})` for any `β > 0`; this is `LZ1I.md` Theorem 12 ("a nonzero difference is not `O((a_lat|k|)^p)` for any `p>0`", line 188) in the present setting.

### 5.5 Theorem R1-C (robustness) and Proposition R1-D (a counterexample) [P]

A real multiscale flow differs from (OL) by higher loops and by cell-scale terms. Write the perturbed flow (OL+ρ): add `ρ_a` to the `v_a` line, `ρ₀` to the `c` line and `ρ_G` to the `G` line, with `ρ` continuous in `ℓ` and locally Lipschitz in the state.

**The class `𝓡(K, f, f₁₂)`.**
- (R-i) `|ρ_a|, |ρ₀| ≤ KG²D + f(ℓ)`, with `f ≥ 0` continuous and `∫₀^∞ f < ∞`.
- (R-ii) `|ρ_G| ≤ KG³`.
- (R-iii) For the pair `1, 2` with `q₁ = q₂ = q`: `ρ₁ − ρ₂ = −G²ϑΔ + g₁₂`, with `|ϑ| ≤ K` and `|g₁₂(ℓ)| ≤ f₁₂(ℓ)`, `∫₀^∞ f₁₂(ℓ)(1+ℓ)^{2q²/W}dℓ < ∞`.

(R-iii) holds with `g₁₂ = 0` whenever the remainder is symmetric under exchanging the two species, `ρ₁(v₁,v₂,·) = ρ₂(v₂,v₁,·)`, and has Lipschitz constant at most `KG²/2` in the speeds: then `|ρ₁ − ρ₂| ≤ KG²|Δ|`. Terms of two loops and beyond are `O(G²)`. Cell-scale terms that break the exchange symmetry go into `g₁₂`.

**Theorem R1-C.** Let `B′ = [m(0)/2, 2M(0)]`, `S′ = W/(12π²M(0))`, `a = 4KG₀/S′`, `F = ∫₀^∞ f`, and assume the smallness condition
\[
\text{(Sm)}\qquad KG_0\le S'/2,\qquad \tfrac{a}{2}\,e^{a}\,\big(D(0)+2F\big)+F\le \tfrac12 m(0).
\]
(a) If `f ≡ 0`, or `f(ℓ) ≤ Ke^{−βℓ}` with `β > 0`, the solution of (OL+ρ) exists on `[0, ∞)`, stays in `B′`, and `D(ℓ) ≤ C(1+ℓ)^{−γ′}` for some `C, γ′ > 0`; all speeds converge to one limit.
(b) If in addition (R-iii) holds with `g₁₂ = 0`, Theorem R1-B holds with the same exponent `q²P_∞/(S_∞W)`; only `C` changes.
(c) If (R-iii) holds with `g₁₂ ≠ 0`, then `(1+ℓ)^{q²P_∞/(S_∞W)}Δ(ℓ)` converges to a finite limit `C_eff`, which may be zero. So `|Δ(ℓ)| ≤ C(1+ℓ)^{−q²P_∞/(S_∞W)}`.

*Proof.* (a) *Box.* As long as the speeds lie in `B′`, `Σ_bn_bq_b²S ≥ S′`, so `(1/G)′ ≥ S′ − KG ≥ S′/2` and `G ≤ G₀/(1 + G₀S′ℓ/2)`; hence `∫₀^∞G² ≤ 2G₀/S′`. The Dini lemma of R1-A gives `D⁺M ≤ KG²D + f` and `D₊m ≥ −KG²D − f`, so `D⁺D ≤ 2KG²D + 2f`. Grönwall gives `D(ℓ) ≤ e^{2K∫G²}(D(0) + 2F) ≤ e^{a}(D(0) + 2F)`, since `K∫G² ≤ a/2`. Then `M(ℓ) − M(0) ≤ ∫(KG²D + f) ≤ (a/2)e^{a}(D(0) + 2F) + F ≤ m(0)/2` by (Sm), and likewise `m(0) − m(ℓ) ≤ m(0)/2`. So the speeds stay in `[m(0)/2, M(0) + m(0)/2] ⊂ B′`; continuity closes the bootstrap, and global existence follows as in R1-A. *Contraction.* In `τ`-time the homogeneous part of the perturbation is at most `KGD`. Repeat item 3 of R1-A with the constants `p′₋, R′₊` of `B′`: the photon moves at most `(R′₊ + KG(τ₀))D̄` per unit `τ`, and above the barrier `d(v_a − K)/dτ ≤ −p′₋(v_a − K) + KG(τ₀)D̄`. Over one window the forcing adds at most `ε = 2∫ f dℓ` over the corresponding `ℓ`-interval. This gives `D(τ₀ + s₀′) ≤ (1 − η′ + C′KG(τ₀))D̄ + ε`. Since `G → 0`, the factor is at most `1 − η′/2` after some `τ₁`. If `f ≡ 0`, then `D ≤ Ce^{−cτ}`. If `f ≤ Ke^{−βℓ}`, the `j`-th window starts at `ℓ_j ≥ e^{c″j} − 1` (because `τ(ℓ) ≤ C log(1+ℓ)` by item 2 of R1-A), so `ε_j ≤ (2K/β)e^{−βℓ_j}` decays faster than any geometric sequence, and the recursion `D_{j+1} ≤ (1 − η′/2)D_j + ε_j` again gives `D_j ≤ C(1 − η′/2)^{j}`. In both cases `τ(ℓ) ≥ c′log(1+ℓ)` turns this into a power of `1+ℓ`. (b) Now `Δ′ = −G(q²Λ + Gϑ)Δ`, so `Δ(ℓ) = Δ(0)exp(−∫₀^ℓ G(q²Λ + Gϑ))` with `∫G²|ϑ| ≤ K∫G² < ∞`. Also `(1/G)′ = s + O(KG)`, and `∫₀^ℓ G = O(log(2+ℓ))`, so the error term `E(ℓ)` of R1-B's proof keeps its bound up to a logarithm, which is still `O((1+ℓ)^{1−γ″/2})`. The rest of R1-B's proof is unchanged. (c) Let `Ψ(ℓ) = exp(−∫₀^ℓ G(q²Λ + Gϑ))`; by (b), `Ψ(ℓ) = (C_Ψ + o(1))(1+ℓ)^{−q²P_∞/(S_∞W)}` with `C_Ψ > 0`. Variation of constants gives `Δ(ℓ) = Ψ(ℓ)[Δ(0) + ∫₀^ℓ Ψ(s)^{−1}g₁₂(s)ds]`, and `|Ψ^{−1}g₁₂| ≤ C(1+s)^{q²P_∞/(S_∞W)}f₁₂(s)` is integrable. Parts (b) and (c) use from (a) only the bound `D ≤ C(1+ℓ)^{−γ′}`, which holds in both cases of (a). □

Item (c) extends the Peierls note's "Decaying lattice forcing and finite matching" (lines 505-517): "The lattice correction changes the finite matching constant but does not shift the massless truncated flow's asymptotic fixed metric by a constant."

**Proposition R1-D (a persistent marginal source defeats the drag).** Let `Δ` solve `Δ′ = −Gq²Λ(ℓ)Δ + σG(ℓ)`, with `σ ≠ 0` constant, `Λ` continuous with `Λ(ℓ) → P_∞ > 0`, and `G > 0` with `∫₀^∞ G = ∞`. Then `Δ(ℓ) → σ/(q²P_∞) ≠ 0`.

*Proof.* In `τ`-time, `y = Δ − σ/(q²P_∞)` solves `dy/dτ = −q²Λy + σ(1 − Λ/P_∞)`. Given `ε > 0`, choose `τ₁` with `|Λ − P_∞| ≤ ε` and `Λ ≥ P_∞/2` for `τ ≥ τ₁`. Then `|y(τ)| ≤ |y(τ₁)|e^{−q²P_∞(τ−τ₁)/2} + 2|σ|ε/(q²P_∞²)`. Let `τ → ∞`, then `ε → 0`. □

So (R-iii) cannot be weakened to "the remainder is `O(G)`". A source of the drag's own order that does not vanish at equal speeds fixes a permanent offset. On a tick such a source would be a marginal Lorentz-violating term generated at every scale, not only at the starting scale. R2-c (§3) must show that cell-scale terms decay instead. This is the finite-matching problem of [CPSUV] and #9913 in flow form.

### 5.6 R1-MOD: three attacks, each fails at a named step [O]

**Lemma R1-MOD (statement).** There are a lattice regularisation of M1 (spatial lattice `Z³`, continuous time or a tick), a block factor `L ≥ 2`, a coupling `G₀ > 0` and a sequence of effective actions `S_k`, `k ≥ 0`, each obtained from the previous by exact integration over one scale, whose quadratic coefficients `(v_a(k), c(k), G(k))` interpolate a solution of (OL+ρ) with `ρ ∈ 𝓡(K, f, f₁₂)`, `f(ℓ) + f₁₂(ℓ) ≤ Ke^{−βℓ}`, `β > 0`, for every `k`.

With R1-MOD, Theorems R1-A to R1-C give the rate of R1 for the model, not only for its truncation.

- **Attack 1: port the all-orders expansion of [GMP12].** *Plan:* write the effective couplings as series in the running couplings, with the order-`N` coefficient bounded at every scale, as [GMP12] does for reduced QED ("finite at all orders"), and read (OL+ρ) off the second-order terms. *Fails at:* the sum over `N`. A remainder estimate of class `𝓡` needs a bound summable in `N`; [GMP12], [GMP10] and [P11] state bounds order by order. Their fermions also live in a plane; M1's fermions live in space, which changes the integrals but not the obstruction.
- **Attack 2: integrate the photon exactly, then run a convergent fermionic expansion.** *Plan:* the noncompact photon is Gaussian; integrating it gives a fermion model with the current-current kernel `j·D·j`; Grassmann (determinant) bounds make fermionic tree expansions converge when the quartic kernel is summable scale by scale. *Fails at:* scale-summability of the kernel. `D` is massless, and its piece at photon scale `h` couples fermion clusters at any finer scale with only the marginal power counting, with no extra decay in the scale gap. This lane does not have an argument that restores the gap. The rigorous treatments of such kernels ([GMP10]) stop at all orders.
- **Attack 3: symmetry and Ward identities instead of size bounds.** *Plan:* use the lattice Ward identity (current conservation) and the exchange symmetry `1 ↔ 2` to show that the remainder vanishes at equal speeds and is `O(G²)`. *Fails at:* the size estimate. Ward identities tie vertex to wave-function renormalisation component by component (temporal with temporal, spatial with spatial); they fix the running of the charge and leave the ratio of spatial to temporal coefficients free. The exchange symmetry gives the vanishing at `Δ = 0` (the structure of (R-iii)) but no bound. This agrees with #9913's exact item: "no symmetry fixes the ratio of two species' dressed speeds" (the heading at line 81 of the consolidation note; quoted in `TOE_ASSEMBLY.md` line 363).
- **Attack 4 (for the record): large `N`.** At `N = ∞` with `e²N` fixed, the fermion self-energy is `O(1/N)`, so the species keep their speeds at leading order; the drag appears at order `1/N`, and the `1/N` series is not known to converge.

**Smallest exact sub-lemma.** **R1″-MOD:** R1-MOD for M1 with a photon mass `m_γ`, on the `N = log(Λ/m_γ)` scales above `m_γ`, with `K` and `β` independent of `N`. If R1″-MOD holds, Theorem R1-C(a)-(c) applied on `[0, N]` bounds the speed spread at the scale `m_γ` by `C(1+N)^{−γ′}`, uniformly as `m_γ → 0`. Attacks 1-3 meet the same steps there; attack 2's kernel becomes massive, which removes the long-range tail but keeps the marginal coupling across `N` scales.

### 5.7 R1-OBS: proved at zero coupling; beyond, the same three attacks fail

**Proposition R1-OBS₀ (free species).** In the continuum, let `j⁰` be the charge density of a free massless Dirac field of speed `v`. Then the spectral density of `j⁰` in the vacuum is `ρ(λ, K) = C_v|K|² θ(λ − v|K|)` with a constant `C_v > 0`, and its threshold set is `E_{j⁰}(κ) = {v}` for every `κ`.

*Proof.* For `v = 1`, Lorentz covariance and current conservation give `ρ^{μν}(q) = (q^μq^ν − q²g^{μν})ρ₁(q²)`, and for a massless free field `ρ₁(q²) = C₁θ(q²)θ(q⁰)` with a constant `C₁ > 0`, because `ρ₁` is dimensionless and the only scale is `q²`. At `μ = ν = 0`, `q⁰q⁰ − q²g⁰⁰ = |K|²`, so `ρ⁰⁰ = C₁|K|²θ(λ − |K|)`. For speed `v`, the change of variables `y = x/v` of Lemma V maps the field to the speed-one field and `(λ, K)` to `(λ, vK)`, up to positive constants from the Jacobian and the normalisation of `j⁰`. The density is smooth (a polynomial) on `λ > v|K|`, zero on `λ < v|K|`, and jumps by `C_v|K|² ≠ 0` across `λ = v|K|`, `K ≠ 0`. So its singular support in `W(κ)` is the cone `λ = v|K|`, and `E_{j⁰}(κ) = {v}`. □

Beyond zero coupling, R1-OBS asks that the thresholds of invariant spectral measures sit at the running flow variables. Each attack of §5.6 applies and fails at the same step: attack 1 gives the current correlator order by order, and the sum over orders is missing; attack 2 needs the same scale-summability of the photon kernel; attack 3 gives transversality of the current correlator (a Ward identity) but no threshold location. On a tick, R1-OBS₀ itself is open; its simplest rung is the free cube tick (hard step H-TRANSFER, §4).

## 6. Which Chadha-Nielsen hypothesis fails on a framework tick

The text of [CN] was not fetched (§1.1). The hypotheses below are the mechanism as the read sources state it: [KLP] (β-functions of the coefficients of `ψ̄γ^μ∂^νψ` and of the photon tensor), [IN] (flows of the electron velocity, the photon speed and the coupling), [AD] (self-energies and RG), and the Peierls note ("The characteristic speeds used below are the spatial/temporal coefficients of the renormalized local one-loop two-point action", its lines 40-41).

**Lemma 6.1 (charged two-point functions carry no speed).** Let `ω` be invariant under conjugation by `e^{iθG_x}` for every site `x` and `θ ∈ R`, where `G_x` is the local Gauss generator (`LW1.md` line 56 for `L_cube`; `Q_x` in `ZM1I1A.md` §1 for `L5-U`). Let the tick commute with every `e^{iθG_x}` (`LW1.md` Theorem B4, line 241, for the base tick; appended layers are gauge invariant by admissibility). Let `ψ_x`, `ψ_y` be local operators with `[G_x, ψ_x] = −ψ_x`, `[G_z, ψ_x] = 0` for `z ≠ x`, and likewise at `y ≠ x`. Then `ω(ψ_x^* α^n(ψ_y)) = 0` for every `n ∈ Z`.

*Proof.* Put `U = e^{iθG_x}`. Then `Uψ_xU^* = e^{−iθ}ψ_x`, `Uψ_yU^* = ψ_y`, and `Uα^n(ψ_y)U^* = α^n(ψ_y)` because `U` commutes with the tick. Invariance gives `ω(ψ_x^*α^n(ψ_y)) = e^{iθ}ω(ψ_x^*α^n(ψ_y))` for all `θ`. □

This is the argument of `ZM1.md` Lemma R-GI (line 372) at the fine level; credit there. So a charged two-point function in a gauge-invariant state is supported on `x = y` at all times. It has no spatial dependence, hence no dispersion and no speed.

| | Hypothesis of the mechanism | On a framework tick | Evidence |
|---|---|---|---|
| H1 | The flowing objects are the speed coefficients of the charged fields' two-point function (gauge-fixed propagator) | **Fails** | Lemma 6.1; `LZ1.md` Theorem 2.2 (line 62): "every odd light species in the proposed sense is flat there, with `N_j=0`"; ZM1-INV (`TOE_ASSEMBLY.md` line 252): "Impose no map on charged fields or Gauss generators" |
| H2 | Continuous time; an energy scale `μ` | Holds after translation for `L = 2` | Scale = zoom level, `ℓ = k log L`; light = the window `W(κ)`. `LZ1I.md` Theorem 10′(e): a zoom with `M` ticks folds far branches into zero branches only if `Mw_j(2πn/L′) ∈ 2πZ`; "If `M≤2` this never happens"; for `M ≥ 3` it happens at finitely many angles ("`E_{4,4}` is not empty") |
| H3 | A massless photon on every scale (Coulomb phase) | Open | `GA15PHI.md` line 5: "not an identified photon or a Clifford cone"; `LW1.md` line 30: "The plaquette class and its constants are unspecified" |
| H4 | Massless charged matter on every scale, so that the drag integral diverges | Open | `LZ1I.md` Theorem 11 (line 180): "The difference tends to zero exactly when it starts at zero or the integral diverges"; MT1-S[R-CS] and R-CS open; in spin-ice U(1) phases the charges are gapped [HFB] |
| H5 | Every species carries the gauge charge | Fails for neutral bands | `LZ1I.md` Theorems 7-9: two neutral bands, speeds `sin θ_j/√3`, "exactly decoupled in the tick" (line 194) |
| H6 | A small coupling, so that one loop dominates | Open | Y2-W open (`GA2_Y2_DRAFT.md` line 195, via `Y2W_DRAFT.md` line 26); link-model couplings need not be small [PMML] |
| H7 | No marginal Lorentz-violating source at consensus (a Lorentz-invariant regulator) | Open; it carries a proved obstruction | The tick breaks Lorentz symmetry at the cell scale. Proposition R1-D: a persistent source of the drag's order fixes a permanent offset. #9913 (consolidation note, line 122): "kappa is nonzero, O(1) and negative (electron slower than the photon)"; and line 132: "The flow from the cell scale to the electron mass suppresses the offset only by a factor 0.88" |

**Answer.** On a framework tick the hypothesis that fails is H1. In every locally gauge-invariant state the charged two-point function is on-site (Lemma 6.1), and in the band reading the charged species is flat (`LZ1.md` Theorem 2.2); the zoom carries no charged data (ZM1-INV). So the variable that Chadha–Nielsen-type flows move is not an observable of the framework's zoom. CN1 replaces it by thresholds of invariant spectral measures (CN1-OBS, §2.2), and needs the bridge R1-OBS (open) to identify the two. H5 fails for neutral species, which CN1-T excludes by (T2). H3, H4, H6 and H7 are open inputs on the framework. H2 holds after translation for `L = 2`.

**The rate is a separate mismatch, not a failed hypothesis.** The U(1) mechanism gives `|Δ_k| ≍ k^{−2q²/W}` (Theorem R1-B). LZ1(a)'s power `p ≥ 2` needs `O(L^{−pk})`; by `LZ1I.md` Theorem 12, "a nonzero difference is not `O((a_lat|k|)^p)` for any `p>0`".

## 7. Readings for the owner (four-tested, none adopted)

The four tests: a proposal fails if it (1) states or fixes a part's target, (2) is open-ended so a part can add to it, (3) settles a downstream physics question by premise, or (4) adds structure or constants its own reasons do not need. P = pass, C = conditional, F = fail. Nothing below is adopted; only the owner adopts.

| Reading | Text | 1 | 2 | 3 | 4 | Use in this file |
|---|---|---|---|---|---|---|
| **CN1-OBS** | Speeds of a level-`k` system are read from the threshold sets `E_A(κ)` of invariant local observables (§2.2): singular supports of the joint spectral measure of `(Ũ, T)` in the window `W(κ) = {|λ| ≤ κ, 0 < |K| ≤ κ}`; the cone mismatch is `Δ_k(κ)`. | P | P | P | C | The quantity in which CN1-T is stated. |
| **R-PH** | A *photon band* is a flux-carrying band in the R-Φ sense (`GA1_5.md` line 61) with a Clifford cone (`LZ1I.md` line 23). | P | P | P | P | Hypothesis (T1) of CN1-T. |
| **R-SCALE** | The zoom level `k` is the flow time `ℓ = k log L`, with one coarse tick equal to `L` ticks (ZM1-I1[a]). | P | P | P | P | Comparing (OL) with a zoom (R2). |
| **R-THR** | The speed of a charged species is the threshold speed of its own invariant current `j_a`. | P | C | C | P | Recorded, not used. |
| **(T2) as a reading of LZ1** | LZ1's common-cone clause covers only species with Gauss charge. | F | P | F | P | Not proposed. (T2) is used only as a hypothesis inside CN1-T. |

**Reasons.**
- *CN1-OBS.* Test 1: it defines the quantity; it does not say that `Δ_k → 0`, and it names no speed or species. Test 2: closed; one number `κ`, a fixed notion of singular support, a fixed family (all invariant local observables light at `κ`). Test 3: invariant observables are forced by ZM1-INV ("Impose no map on charged fields"); the reading decides neither R-CS, nor LZ1's rate, nor ST1. Test 4: conditional; the window constant `κ₀` of CN1-T(r) is a constant of the rate statement only, and the limit form removes it. Why singular supports and not supports: interactions fill the region above the slowest cone, so a faster species is invisible in the support and visible only as a threshold (§2.2, fact (iii)).
- *R-PH.* It adds the cone condition to the existing R-Φ. It fixes no target of GA1-5-Φ (whose frozen band is one-way and is not called a photon) and settles nothing downstream.
- *R-SCALE.* It is the identification that `LZ1I.md` Theorem 10′ already uses (`M = L′ = L` keeps speeds unchanged under `c_t = c_s` graining).
- *R-THR.* Test 2 is conditional: it needs a separately conserved number for each species, which a law need not supply. Test 3 is conditional: it defines a charged speed without R-CS, and must agree with R-CS^str wherever both are defined. R1-OBS (open) would make it a theorem in M1; that is better than a reading.
- *(T2) as a reading.* It fails test 1 (it states the mechanism's scope as the target's scope) and test 3 (it removes neutral species by premise), as `LZ1I.md` §6 found for S-CONN ("fail: states the desired mechanism"; "fail: decides neutral-sector coupling by premise"). As a hypothesis of a theorem it restricts nothing in the law.

## 8. Prior work used

Each prior result used or extended here, with its path and how it is used. `main:` means `origin/main` at `f5af11cd0`; `T/` means this folder.

| Prior result | Path | Status there | Use here |
|---|---|---|---|
| One-loop fermion speed log, `dv/dℓ = e²(c−v)(4v²+3vc+c²)/[6π²c(v+c)²]`, with its gauge-independence argument | `main:docs/SPATIAL_LATTICE_GAUGE_FERMION_LOGARITHMS_AND_METRIC_ATTRACTION_LIMITS_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 149-176, 234-255 | conditional-support, unaudited | Ported as `P` in (OL) |
| Nonlinear isotropic truncated flow for one shared fermion speed; convergence and exponent `(N+2)/N` | same note, lines 474-503 | same | Consistency (C1); **extended** by R1-A (distinct speeds, `n` species, global) and R1-B (the inter-species exponent `2q²/W`) |
| Linearised multi-cone flow, weighted star graph, exponents `λ_j/W` | same note, lines 405-473 | same | Consistency (C2); R1-B remark (2) |
| Decaying lattice forcing changes only the finite matching constant | same note, lines 505-517 | same | **Extended** by R1-C(c) to the nonlinear two-species flow |
| "Higher-loop control remains open" | same note, line 503 | same | Made exact as the class `𝓡` (R1-C) and the open Lemma R1-MOD (§5.6) |
| Exchange-matrix attraction, `d(v_F − v_B)/dl = −(a+b)(v_F − v_B)` for constant positive drag | `main:docs/EMERGENT_LORENTZ_VELOCITY_RG_EXCHANGE_MATRIX_EXACT_SUPPORT_NOTE_2026-06-18.md` lines 66-78 | bounded theorem, unaudited | **Extended** by R1-A to state-dependent coefficients, `n` species and a running coupling |
| Theorems 11 (drag dichotomy) and 12 (marginal rate) | `T/LZ1I.md` lines 180-190 | frozen | H4; R1-B remark (3); §6 rate mismatch |
| Theorems 7-9 (two neutral bands, different speeds; necessary restriction) | `T/LZ1I.md` lines 80-119 | frozen | R0; H5; (T2) |
| Theorem 10′ and RC-Z (zoom transfer of band speeds; folded branches for `M ≥ 3`) | `T/LZ1I.md` lines 121-178 | frozen (referee closures, unrefereed) | R0; R2 imports; H2 |
| Theorem 2.2 and Corollary 2.3 (odd bands flat) | `T/LZ1.md` lines 62-66 | frozen | H1 |
| Lemma R-GI (charged two-point functions vanish off-site) | `T/ZM1.md` line 372 | frozen | Lemma 6.1 is its argument at the fine level |
| GA1-5-Φ: a flux band, "not an identified photon or a Clifford cone" | `T/GA15PHI.md` line 5 | frozen | (T1), H3, hard step H-PHOTON |
| #9913: no tick symmetry fixes the electron cone to the photon cone; finite one-loop offset; continuum Coulomb log on a tick | `origin/docs/consolidate-lorentz-dispersion:docs/LORENTZ_DISPERSION_CONSOLIDATED_BOUNDED_THEOREM_NOTE_2026-10-30.md` lines 81-134 | author statements for review | H7; R2-a support; attack 3 |
| ZM1-INV, ZM1-I1[a] with `p = 2`, LZ1-SC, NN-a, R-CS^str (owner decisions and working candidate) | `T/TOE_ASSEMBLY.md` lines 225-256 | owner decisions; R-CS^str not adopted | §2 objects; (T2) names R-CS^str as an open input |

**Prior work the digest `prior/CN1.md` missed, now added.**
- `T/GA15PHI.md` (frozen 2026-11-07): the only frozen flux-carrying band is one-way and has no Clifford cone. It bears directly on H3 and on hypothesis (T1).
- `T/ZM1.md` Lemma R-GI as a statement about charged two-point functions, which gives H1's failure on a tick (Lemma 6.1). The digest cites ZM1-INV's text but not this lemma.
- `T/LZ1I.md` Theorem 10′(e): a zoom with `M ≥ 3` ticks per coarse tick can fold far branches into zero branches at finitely many angles. It bears on H2 (what counts as light on a tick).

**Further digest items, read at the cited lines.**
- `main:docs/EMERGENT_LORENTZ_INTERACTING_VELOCITY_RG_ATTRACTOR_NOTE_2026-06-06.md` lines 18-30: "once the specified one-loop packet is supplied, the speed-difference mode is IR-attractive"; status "conditional-support / open gate". R1-A proves the nonlinear, many-species form of that consequence for the one-loop packet of (OL).
- `main:docs/VELOCITY_RG_GAUGE_SEAGULL_TRANSVERSE_VACUUM_POLARIZATION_2026-06-22.md` lines 86-90: "The precise net coefficient needs a gauge-invariant fermion-velocity prescription: the bare self-energy `Z` is gauge-dependent (Feynman vs Landau differ)". At one loop in the continuum, the Peierls note's longitudinal argument (its lines 234-255) gives gauge independence of the speed logarithm. CN1-OBS with R1-OBS is this file's proposal for the prescription beyond one loop and on a tick.
- `main:docs/LORENTZ_NATURALNESS_GAP_QUANTIFIED_OBSTRUCTION_NOTE_2026-06-06.md` lines 42-48: "Under those supplied inputs, the answer is no, by 4 to 16 orders of magnitude"; this is the [CPSUV] problem in the repository's terms, and it belongs to H-FIN and H7.

**Digest items not opened here (only the digest's summary was read), with the reason.** The Hall-response notes (`main:docs/NATIVE_WEYL_GAUGE_HALL_AND_CONE_FLOW_BOUNDED_THEOREM_NOTE_2026-09-13.md` and the mixed-quartet note) concern Weyl carriers with separated nodes; M1 has Dirac species and no Hall term, and R2 must check the photon action on the framework (H-PHOTON). The B4 two-surface note is a symmetry route (A1 of `LZ1I.md`), not a drag route. The supplied matched free cone is a finite-matching statement (H-FIN). The gravity notes belong to R3 and GR. The Wilson/staggered proxy note and the finite-torus WTI note are recorded by the digest as withdrawn or unable to supply physical drag coefficients; R1 does not use them.

## FINISH

**Proved here (pass 1; not yet distilled or refereed).**
- Lemma V: the photon and coupling lines of the one-loop flow with unequal speeds, from the Lorentz-invariant vacuum-polarisation coefficient by the change of coordinates `y = x/v`.
- Theorem R1-A: for any positive, locally Lipschitz coefficient functions, the `n`-species one-loop flow (OL) exists for all `ℓ ≥ 0`, keeps every speed in its initial hull, contracts the spread as `D(ℓ) ≤ C(1+ℓ)^{−γ}` with explicit `γ > 0`, and sends all speeds to one limit.
- Theorem R1-B: for two species of equal charge `q`, `|v₁ − v₂| = (C + o(1))(1+ℓ)^{−2q²/W}`, `C > 0`; for two unit-charge Dirac species alone the exponent is `1`. In zoom levels, `|Δ_k| ≍ k^{−2q²/W}`.
- Theorem R1-C: R1-A and R1-B survive every remainder in the class `𝓡` (exchange-symmetric `O(G²)` terms, integrable forcing); integrable forcing changes only the constant.
- Proposition R1-OBS₀: a free continuum species of speed `v` has threshold set `{v}` for its charge density.
- Lemma 6.1: in a gauge-invariant state, charged two-point functions are on-site at all times, so they carry no speed (the fine-level form of `ZM1.md` Lemma R-GI).
- Consistency (C1)-(C4): (OL) reduces to the Peierls note's shared-speed and linearised flows and agrees with [KLP]'s β-functions and [IN]'s near-invariant `c²v`.

**Counterexamples.**
- Proposition R1-D: a persistent source `σG`, `σ ≠ 0`, in the difference equation gives `v₁ − v₂ → σ/(q²P_∞) ≠ 0`. The remainder class of R1-C cannot be widened to all `O(G)` terms.
- Ported, frozen (R0): the two neutral bands of `LZ1I.md` keep different speeds through every zoom that meets Theorem 10′.

**Open by name.**
- **R1-MOD** (the model has a flow in `𝓡`): three distinct attacks failed. Attack 1 (port [GMP12]'s all-orders expansion) fails at the sum over orders. Attack 2 (integrate the Gaussian photon, then a convergent fermionic expansion) fails at scale-summability of the massless photon kernel. Attack 3 (Ward identities and exchange symmetry) fails at the size estimate. Attack 4 (large `N`) is recorded. Smallest sub-lemma: **R1″-MOD** (photon mass `m_γ`, bounds uniform in the number of scales).
- **R1-OBS** beyond zero coupling: the same three attacks fail at the same steps.
- **R2**, with new steps R2-a (tick loops), R2-b (threshold transfer, H-TRANSFER), R2-c (cell-scale forcing decays), and inputs GA1-5-Φ as a Clifford cone (H-PHOTON), R-CS, ZM1-I1[INV], Y2-W, VC1.
- **R3** (every species; H-NA), **H-FIN** (finite matching), **R-P** (a power rate; H-RATE).
- **CN1-T** and **CN1-T(r)** themselves.

**Which hypothesis of Chadha–Nielsen fails on a framework tick.** H1: the flow variable of the mechanism is the speed of a charged field's two-point function, and on a tick in a gauge-invariant state that function is on-site (Lemma 6.1), the charged band is flat (`LZ1.md` Theorem 2.2), and the zoom carries no charged data (ZM1-INV). H5 fails for neutral species (`LZ1I.md`). H3, H4, H6 and H7 are open on the framework; H2 holds after translation for `L = 2`.

**What changes downstream.**
- *LZ1.* LZ1-i gets a definite target for charged species, CN1-T. The U(1) mechanism gives a power of the zoom level, `k^{−2q²/W}`, never `L^{−pk}`; so LZ1(a)'s `p ≥ 2` needs R-P or a protecting symmetry, and the cell-scale offset (#9913) is a separate matching input (H-FIN).
- *ZM1.* Class (a) must carry threshold sets of continua across a zoom step (R2-b). RC-Z covers isolated branches only.
- *GA1.* CN1 needs a photon band with a Clifford cone (T1). The frozen flux band of `GA15PHI.md` is not one. This is W3's first framework priority.
- *MT1-S and R-CS.* (T2) and R1-OBS need the charged sector. Lemma 6.1 shows that a charged speed must come from invariant composites or from the R-CS^str dressing, not from a charged two-point function.
- *ST1 and GA2.* The threshold sets of CN1-OBS are an invariant form of the spectrum condition and of a common cone; ST1's route B and GA2's anisotropy removal can use them.
- *GR2.* CN1-T does not cover the graviton.
- *Owner.* Four readings are recorded with their four-test results (CN1-OBS, R-PH, R-SCALE, R-THR). Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
