lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SGAP: Lemma S-GAP of SMG15 (wall W2), pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as a pass-1 lane of the TOE assembly, under the method of open PR #10138: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status, adopts no law, adopts no reading and changes no axiom or working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out in full below and has not yet been distilled or refereed. "[check]" marks a tiny scratch computation in `/tmp/toe-SGAP/` (under a minute, under 1 GB, started only with at least 50 percent free memory). A check guides and never proves. No step below is computer-assisted.

**Source revisions read.**

| Ref | Commit |
|---|---|
| branch `claude/toe-assembly` (this checkout) | `6e22793b6` |
| `origin/main` (read with `git show` only, after `git fetch -q origin main`) | `f5af11cd0` |

Files read at that commit, by line (last-change commit in brackets). This folder: `prior/SGAP.md` lines 1-92, all [`6e22793b6`]; `SMG15.md` lines 1-217, all [`373e01725`]; `SMG15_REFEREE.md` lines 1-90, 128-131, 144, 241-249, 288-292 [`7a7a141af`]; `SMG1.md` lines 1-153, all, with Amendment 1 (line 5) [`373e01725`]; `TOE_ASSEMBLY.md` lines 201-266 (sections 3.4-3.10) and 722-736 (section 11) [`47e819786`]; `SMG15_DRAFT.md` lines 37, 70-92 (its literature table), 282 [read by grep only]; `Y2W_DRAFT.md` lines 1-40, for the format only [`92e03055c`]. Long lines were read to their first 900-1800 characters.

`origin/main` at `f5af11cd0` (`git fetch -q origin main`; read with `git show` only; both notes last changed at or before `4d0cd77bd`): `docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md` lines 230-240, 254-258, 290-298; `docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md` lines 12-16, 87-91. They match the digest: "the bound retains v's volume dependence"; "At this order the induced term is a constant"; "a nonzero attractive density interaction", "not imported unchanged into the refined Spin(10) atom"; the KMS note "proves only scalar ODE consequences", and "Any future framework use must separately supply the BBF/Polchinski inequality". No step here uses them. The digest's other paths (the half-filled ring comparator `H`, the consolidated note `C`, the retained-Grassmann polymer note, PR #10135's gauge-gap note) concern other models or narrower scopes, as the digest reports; they were not read, and no step here rests on them.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The model of S-GAP is read plainly, exactly as `SMG15.md` line 150 writes it.

**Working set used, by name.** SMG1-GAP (bounded R-GEN, `TOE_ASSEMBLY.md` §3.10) only as the frame in which S-GAP's finite-ring sector statement is a candidate reading (R15-SPEC (S1), not adopted). GA1-P-NN (NN-a) is not used: S-GAP is a statement about one operator `H_ε`, not about a tick. PS-5 and PS-6r enter only through the rung-1 carrier of `SMG1.md`. No other entry is used. Nothing here is a verdict.

---

## 0. The question, quoted

`SMG15.md` line 148: "**S-GAP (open).** Do there exist `c₀,Δ>0` such that, for every `τ>0`, `|t|,|ε|≤c₀τ` and every allowed `L`, the `S`-charged spectrum of"

line 150: "`H_ε=τΣ_x(W_x+14)−tΣ_xhop_x+εΣ_{x,a}iγ_{x,a}γ_{x+1,a}hop⁰_x`"

line 152: "lies at least `Δτ` above its ground energy on `H_{1/2}`? This includes `t=0`. A unique ground state is a separate question."

"Allowed `L`" is `L∈4N`, `L≥8` (`SMG15.md` line 15). `SMG15_REFEREE.md` line 243 checks that the question is well posed: "`H_ε/τ` depends only on `t/τ` and `ε/τ`, so the quantifiers make sense." `SMG15.md` lines 154-158 list three attacks that failed, and `SMG15_REFEREE.md` line 290 carries S-GAP as "The stopping lemma". This lane is pass 1 on S-GAP itself.

## 0.1 Outcome in one paragraph

**S-GAP is neither proved nor refuted. The stopping lemma is its `t=0` case, S-GAP⁰, on which three new attacks fail at named steps.** Proved here, every step written out: (1) *Lemma E, Proposition Z.* On `H_{1/2}` the only nontrivial charges are the seven of `Ŝ_+` (even mirror parity), and at `ε=0` the charged gap is exactly `16τ` for every `t` and `L`. So S-GAP holds at `ε=0` with `Δ=16`, the best constant there. (2) *Theorem A (charge shift), for every `t` and `ε`.* An on-site Majorana bilinear `Y` maps the `σ`-charged block of `H_ε` unitarily onto the neutral block of `H_ε+B`, where `B` is a local operator at one site and its two bonds. Corollary A1: `max_Ψ(−⟨Ψ,BΨ⟩)≤E_σ−E_1≤min_Ω⟨Ω,BΩ⟩≤16τ+8|ε|`. So S-GAP says that one local operator raises the neutral ground energy by `Δτ`; the extensive energies cancel identically. (3) *Theorem C (`t=0`).* Every site parity is conserved, the light occupation is a function of the mirror line, and `H_ε` splits into `2^{L−1}` chains of 16-level sites, each with a one-dimensional on-site kernel and on-site gap `14τ`. So at `t=0` the failing steps of two attacks on file (Fröhlich-Pizzo's (1.4); the `|z|⁻²` light tails) do not occur. Proposition C2: the per-sector form of S-GAP is false at `ε=0`. Proposition C5: a uniform gap in each sector (G1) plus "half filling costs at most `δτ` against the best filling" (HF') implies S-GAP⁰. Remark C6: at `t=0` every level on `H_{1/2}` has even multiplicity. (4) *Lemma R* (removing the charge, exact, every `t`) and *Proposition R2* (at `t=0` the odd weight of a charged ground vector is at least `Lε²/(200704τ²)`). **Failed attacks on S-GAP⁰**, distinct from the three on file: A4, removal (fails at bounding the odd weight by the `σ`-weight; R2 makes the odd weight extensive); A5, charge shift with a window bound (fails at `λ(K+B)>λ(K)`, which is false: the two are equal); A6, sector splitting with a per-sector gap (fails at the comparison across sectors, which needs (HF')). **S-GAP at `t≠0`** stays open; A4 and A5 fail there the same way.

## 1. Prior work used

Every row is a frozen result, used as stated there. Nothing here re-proves it, except where a row says so.

| Prior result | Path | Use here |
|---|---|---|
| Code `C`, group `S≅Z₂⁴`, `g₁g₂=c₁⋯c₈=P^(4)` (the mirror parity), the sign rule `g c_a g⁻¹=(−1)^{u_a}c_a` | `SMG1.md` Lemma 2.1 (line 47) | Lemma E; the sign symmetry in section 3 |
| Atom: each of the sixteen characters occurs once; `W` is `−14` on the trivial line, `0` on the eight odd lines, `2` on the seven other even lines; `ψ` even and `S`-fixed | `SMG1.md` Theorem 2.2 (line 49) | Every result; it fixes the numbers 14 and 16 |
| Lemma M: degree-four mixing is a same-flavour mirror pair times a number-conserving light pair | `SMG1.md` line 137 | Only to say that `H_4` is the general degree-four form, as `SMG15.md` does |
| Theorem 1: rank-one configuration projectors `P^χ_x`; shift rule `γ_{x,a}P^χ_x=P^{χρ_a}_xγ_{x,a}`; the eight `ρ_a` are distinct and label the odd lines; the global action `U_g` | `SMG15.md` line 30 | Lemma E, Theorem A, Theorem C |
| Theorem 2: Gauss reduction `J:F_even⊗C²→H_G`; `∏_xP_x=1` on `H_G`; parity-preserving matter operators map to themselves tensored with `1` | `SMG15.md` lines 34-42 | Lemma E, Theorem C |
| Theorem 3, proof: with mirror modes ordered first, every even light operator acts as `1⊗ℓ` on each mirror configuration; the free half-filled minimum `E₀=−2|t₀|/sin(π/L)` | `SMG15.md` lines 62, 70 | Proposition Z |
| Theorem 7: `PH_4P=0` and the coefficient `2/(7τ)`, with `Λ_x²=n_x+n_{x+1}−2n_xn_{x+1}` | `SMG15.md` lines 136-140 | Remark C3 (second order on each sector) |
| The three failed attacks on S-GAP and their failing steps | `SMG15.md` lines 154-158; `SMG15_REFEREE.md` §2.9 (lines 241-249) | Section 5: the attacks here are distinct from them. Section 4.3 says where two of their failing steps disappear at `t=0` |
| The `t=0` remark: on `N=L/2` the second-order operator is minimized by the two alternating configurations | `SMG15.md` line 152; `SMG15_REFEREE.md` line 243 | Remark C3 extends it: at `t=0` the occupation pattern is conserved exactly, not only at second order |
| SMG1-GAP (bounded R-GEN), R15-SPEC (S1), not adopted | `TOE_ASSEMBLY.md` line 261; `SMG15.md` line 24 | Frame only |

**Missed by the digest.** None that bears on S-GAP. The digest (`prior/SGAP.md`) lists every file above. Its "Missed inputs" (lines 72-82) are taken up as follows: the configuration criterion and the `t=0` quantifier (sections 4.1-4.3); the induced interaction (Remark C3); finite-ring versus GNS statements (S-GAP is read on finite rings, as `SMG15.md` line 148 states it).

## 2. Literature read

All items were searched on 2026-11-07 with WebSearch; "fetched" means the arXiv abstract page was fetched with WebFetch that day. The fetch tool limits verbatim quotes, so quotes are short. No item carries a proof step here. Everything used below is proved in this file.

| # | Work | Fetched | What it says (quoted or close paraphrase) | Use here |
|---|---|---|---|---|
| L1 | J. Fröhlich, A. Pizzo, "Lie-Schwinger block-diagonalization and gapped quantum chains", arXiv:1812.02457 (v2, 2019-02-27) | abstract | "We study quantum chains whose Hamiltonians are perturbations by bounded interactions of short range"; the unperturbed part couples no sites and has "a strictly positive energy gap"; the gap stays bounded below uniformly in the length for small coupling. Theorem 3.5 and hypotheses (1.4), (1.6), (1.7) as quoted in `SMG1_REFEREE.md` §2.5, not re-read | Context for Theorem C's remark (the on-site kernel becomes one-dimensional at `t=0`) |
| L2 | S. Del Vecchio, J. Fröhlich, A. Pizzo, S. Rossi, "Local iterative block-diagonalization of gapped Hamiltonians: a new tool in singular perturbation theory", arXiv:2007.07667, J. Math. Phys. 63, 073503 (2022) | abstract | the unperturbed operator is a "gapped operator, consisting of a sum of on-site terms"; the method shows "the spectral gap above the ground-state energy of such Hamiltonians persists"; the chain case is the earlier arXiv:1908.07450 (seen in search results only, NOT VERIFIED) | Context |
| L3 | D. A. Yarotsky, "Ground states in relatively bounded quantum perturbations of classical lattice systems", arXiv:math-ph/0412040, Commun. Math. Phys. 261, 799-819 (2006) | abstract | "existence of the spectral gap, exponential decay of truncated correlations, analyticity of the ground state" for relatively bounded quantum perturbations of classical models | Context for attack A6 (the cluster-expansion step it would need) |
| L4 | T. Kennedy, H. Tasaki, "Hidden symmetry breaking and the Haldane phase in S=1 quantum spin chains", Commun. Math. Phys. 147, 431-484 (1992) | **NOT VERIFIED** (search snippet only; no arXiv version found) | perturbation theory for "diagonally dominant" Hamiltonians, per the snippet | Credit only |
| L5 | W. De Roeck, M. Salmhofer, "Persistence of exponential decay and spectral gaps for interacting fermions", arXiv:1712.00977, Commun. Math. Phys. 365, 773-796 (2019) per the search result | abstract | weakly interacting lattice fermions whose free system "is assumed to have a ground state separated by a gap"; the gap persists, uniformly in the lattice size | Context: its hypothesis excludes the gapless light chain |
| L6 | M. B. Hastings, "The Stability of Free Fermi Hamiltonians", arXiv:1706.02270 | abstract | "we prove the stability of free fermion Hamiltonians which are gapped and local" | Context, as L5 |
| L7 | S. Bravyi, M. Hastings, S. Michalakis, "Topological quantum order: stability under local perturbations", arXiv:1001.0344, J. Math. Phys. 51, 093512 (2010) | abstract | Hamiltonians of local commuting projectors; a small perturbation leaves low-lying bands separated by a constant gap; proof by "discrete Hamiltonian flow equations", relative boundedness and Lieb-Robinson bounds | Context |
| L8 | S. Michalakis, J. Pytel, "Stability of Frustration-Free Hamiltonians", arXiv:1109.1588, Commun. Math. Phys. 322, 277-302 (2013). The brief calls it Michalakis-Zwolak; the abstract page lists the authors as Michalakis and Pytel | abstract | "We prove stability of the spectral gap for gapped, frustration-free Hamiltonians under general, quasi-local perturbations"; condition "Local Topological Quantum Order" | Context |
| L9 | G. Benfatto, V. Mastropietro, "Ward identities and chiral anomaly in the Luttinger liquid", arXiv:cond-mat/0409049, Commun. Math. Phys. 258, 609-655 (2005) | abstract | interacting 1D systems "verify an hidden approximate Gauge invariance"; correlations "show a Luttinger liquid behavior characterized by non universal critical indices" | Context for the marginal light coupling (section 5, attack A6) |
| L10 | G. Benfatto, V. Mastropietro, "Ward identities and vanishing of the Beta function for d=1 interacting Fermi systems", J. Stat. Phys. 115, 143-184 (2004) | **NOT VERIFIED** (search snippet only; arXiv ID not found) | the snippet: a simplified proof of the asymptotic vanishing of the Beta function | Credit only |
| L11 | G. Benfatto, V. Mastropietro, "Universality relations in non-solvable quantum spin chains", arXiv:0907.2837 | not re-fetched; `SMG15_DRAFT.md` line 87 reports its ar5iv text (Eq. (1), Theorem 1.1) | XXZ-type chains with a small extra interaction | Context, as on file |
| L12 | A. Giuliani, V. Mastropietro, M. Porta, "Absence of interaction corrections in graphene conductivity", arXiv:1010.4461, Phys. Rev. B 83, 195401 (2011) | abstract | interaction corrections to the conductivity vanish, "rigorously established" | Credit for the constructive-RG-with-Ward-identities programme only |
| L13 | G. Benfatto, G. Gallavotti (Fermi-surface RG, J. Stat. Phys. 1990); D. Brydges, T. Kennedy (Mayer expansions, J. Stat. Phys. 1987); D. Brydges, H.-T. Yau (Commun. Math. Phys. 1990); R. Kotecký, D. Preiss (Commun. Math. Phys. 1986) | **NOT VERIFIED** (no arXiv versions; not fetched) | named from the lane brief and from memory | Credit only; no statement from them is used |

**Search for the exact object.** A search for a rigorous ground-energy bound for a mobile impurity in a Luttinger liquid found none. The closest hit, arXiv:1308.6260 (abstract seen in search results only, NOT VERIFIED), bounds the infinite-time momentum of an impurity in a free Fermi gas, not its energy gap. A search for Mastropietro's work on an impurity in a Luttinger liquid found no rigorous paper on that problem. So no fetched work states a uniform energy gap for a gapped excitation coupled to a gapless one-dimensional chain. Every fetched stability theorem (L1-L3, L5-L8) assumes a gapped unperturbed system. This is the obstacle `SMG15.md` line 158 records for L1. Section 4.3 shows that at `t=0` the obstacle disappears inside each sector of conserved site parities.

## 3. The model made exact

The carrier and all symbols are those of `SMG15.md` §1 (lines 15-20). Write

`H_M:=τΣ_x(W_x+14)`, `H_L:=−tΣ_xhop_x`, `T_{x,c}:=iγ_{x,c}γ_{x+1,c}hop⁰_x` (`c=1,…,8`), `H_4:=Σ_{x,c}T_{x,c}`,

so that `H_ε=H_M+H_L+εH_4` is the operator of `SMG15.md` line 150, on `H_{1/2}`. `U_g=∏_xg_x` is the global action of `g∈S`. For a character `χ∈Ŝ` put `H^χ_{1/2}:={Φ∈H_{1/2}: U_gΦ=χ(g)Φ for all g}`, `E_χ:=min spec(H_ε|H^χ_{1/2})` (`+∞` if the space is `0`), and `E_0:=min spec(H_ε|H_{1/2})=min_χE_χ`. "Neutral" means `χ=1`; "charged" means `χ≠1`.

**S-GAP, restated.** There are `c₀,Δ>0` such that `E_χ≥E_0+Δτ` for every `χ≠1`, every `τ>0`, every `|t|,|ε|≤c₀τ` and every `L∈4N`, `L≥8`.

**Facts F1-F4 (proved here).**

(F1) *`T_{x,c}` is Hermitian and `‖T_{x,c}‖≤1`.* `iγ_{x,c}γ_{x+1,c}` is Hermitian and squares to `1`. `hop⁰_x` is Hermitian; on its two modes its eigenvalues are `−1,0,0,1`. The two factors are even operators on disjoint sets of modes, so they commute. A product of two commuting Hermitian contractions is a Hermitian contraction.

(F2) *`T_{x,c}` is even at every site.* At site `x` it contains `γ_{x,c}` and one of `c_x,c_x†`; at `x+1` likewise; elsewhere nothing. So it commutes with every site parity `P_y` and, having no link factor, with every `G_y`. It commutes with `N`. Under `U_g` both Majoranas pick up `ρ_c(g)`, so `U_gT_{x,c}U_g*=T_{x,c}`. `H_M` and `H_L` also commute with `U_g`, `N` and every `G_y` (`SMG15.md` line 58). So `H_ε` preserves `H_{1/2}` and each `H^χ_{1/2}`. `U` is a unitary representation of the finite abelian group `S`, so `H_{1/2}=⊕_χH^χ_{1/2}` orthogonally.

(F3) *Light operators act the same way in every mirror configuration.* This is the `1⊗ℓ` fact in the proof of `SMG15.md` Theorem 3 (line 70), with Theorem 2's reduction: under `J`, `H_L` is `1_mirror` tensored with the twisted free light hop. Its minimum over the half-filled light space and both holonomies is `E_L:=−2|t|/sin(π/L)` (`SMG15.md` line 62 with `t₀=t`; `E_L=0` at `t=0`).

(F4) *Sign symmetry: `E_χ(ε)=E_χ(−ε)`.* Put `R:=∏_{x even}(g₁g₂)_x`. By `SMG1.md` Lemma 2.1, `(g₁g₂)_x` is the mirror parity of site `x`. It anticommutes with `γ_{x,c}`, `c≤8`, and commutes with everything else at other sites, with light modes, links, `W_y`, `G_y`, `N` and `U_g` (`S` is abelian). On the ring of even length every bond has exactly one even endpoint. So `RT_{x,c}R*=−T_{x,c}` for every bond and `RH_εR*=H_{−ε}`, sector by sector.

## 4. Results

### 4.1 Which charges occur, and the exact gap at `ε=0`

Let `Ŝ_+:={χ∈Ŝ: χ(g₁g₂)=1}`.

**Lemma E (charges on `H_{1/2}` are even).** On `H_{1/2}`, `U_{g₁g₂}=1`. Hence `H^χ_{1/2}=0` unless `χ∈Ŝ_+`. `Ŝ_+` has eight elements: `1` and seven charged ones. Every odd character `ρ_a` lies outside `Ŝ_+`. For each fixed `a`, the map `b↦ρ_aρ_b` is a bijection from `{1,…,8}` onto `Ŝ_+`, with `a↦1`. So every charged `σ∈Ŝ_+` is `ρ_aρ_b` for some `b≠a`.

*Proof.* The site parity is `P_x=(g₁g₂)_x(−1)^{n_x}`: by `SMG1.md` Lemma 2.1, `g₁g₂=c₁⋯c₈=P^(4)=∏_{j≤4}(−ic_{2j−1}c_{2j})`, and `−iγ_{2j−1}γ_{2j}=1−2n_j` for each mirror mode. `SMG15.md` Theorem 2 gives `∏_xP_x=1` on `H_G`. So `U_{g₁g₂}(−1)^N=1` on `H_G`. On `H_{1/2}`, `N=L/2` is even because `4|L`. So `U_{g₁g₂}=1` there. Next, `χ↦χ(g₁g₂)` is a homomorphism onto `{±1}` (it is onto: `ρ_a(g₁g₂)=−1`, since `g₁g₂` has full support). So `Ŝ_+` has index two, and its complement has eight elements. The eight `ρ_a` are distinct (`SMG15.md` Theorem 1) and lie in the complement, so they fill it. Multiplication by `ρ_a` maps the complement bijectively onto `Ŝ_+`, and `ρ_aρ_a=1`. □

**Proposition Z (`ε=0`, every `t`).** At `ε=0`, for every `τ>0`, real `t` and `L∈4N`: `E_1=E_L`, and `E_σ=E_L+16τ` for every charged `σ∈Ŝ_+`. So S-GAP holds at `ε=0` with `Δ=16`, for all `t`, and `16` is the largest constant possible there.

*Proof.* At `ε=0`, `H_ε=H_M+H_L`. The configuration projectors `P^{χ⃗}` commute with it (`SMG15.md` Theorem 1). On configuration `χ⃗`, `H_M=τm(χ⃗)` with `m(χ⃗):=Σ_x(W(χ_x)+14)`; by `SMG1.md` Theorem 2.2, a site contributes `0` if `χ_x=1`, `14` if `χ_x` is odd, and `16` if `χ_x` is even and nontrivial. By (F3) every eigenvalue in configuration `χ⃗` is at least `E_L+τm(χ⃗)`. `U_g` acts on configuration `χ⃗` by `∏_xχ_x(g)` (`SMG15.md` Theorem 1). So a vector in `H^σ_{1/2}`, `σ≠1`, lies in configurations with `∏_xχ_x=σ≠1`. Such a configuration has at least one nontrivial site. If it has exactly one, that site carries `σ`, which is even and nontrivial: `m=16`. If it has two or more, `m≥28`. So `E_σ≥E_L+16τ`. For equality, take `χ_y=σ` at one site `y` and `χ_x=1` elsewhere. All mirror lines are even, so Gauss's law leaves the whole half-filled light space with both holonomies (`SMG15.md` line 70), and the free light minimum `E_L` is attained. The same argument with all `χ_x=1` gives `E_1=E_L`. □

`SMG15.md` Theorem 3 gives `14τ−2δ` for its family; on `H_{1/2}` Lemma E raises the `ε=0` value to `16τ`, because a single odd site cannot carry a charge there.

### 4.2 The charge-shift identity (every `t`, every `ε`)

**Theorem A (charge shift).** Fix a site `x₀` and a charged `σ∈Ŝ_+`. By Lemma E choose `a≠b` with `ρ_aρ_b=σ`, and put `Y:=iγ_{x₀,a}γ_{x₀,b}`. Then:

(i) `Y` is a Hermitian unitary. It commutes with `N`, every `P_x`, every `G_x`, and every light and link operator. `U_gYU_g*=σ(g)Y`. So `Y` maps `H^χ_{1/2}` onto `H^{χσ}_{1/2}` for every `χ`.

(ii) `YH_εY=H_ε+B`, where `B:=16τ(P^1_{x₀}−P^σ_{x₀})−2εΣ_{c∈{a,b}}(T_{x₀−1,c}+T_{x₀,c})`.

(iii) `H_ε|H^σ_{1/2}` and `(H_ε+B)|H^1_{1/2}` are unitarily equivalent. In particular `E_σ=min spec((H_ε+B)|H^1_{1/2})`.

*Proof.* (i) `Y*=−iγ_bγ_a=Y` and `Y²=−γ_aγ_bγ_aγ_b=γ_a²γ_b²=1`. `Y` is even and lives on site `x₀`, so it commutes with `P_x`, with `G_x` (no link factor), with `N` (it touches no light mode), and with every operator on other modes. By `SMG1.md` Lemma 2.1, `gγ_cg⁻¹=ρ_c(g)γ_c`, so `U_gYU_g*=ρ_a(g)ρ_b(g)Y=σ(g)Y`. Hence `U_gYΦ=σ(g)χ(g)YΦ` for `Φ∈H^χ_{1/2}`. Since `Y²=1` the map is onto.

(ii) `Y` commutes with `H_L`, with every `W_x`, `x≠x₀`, and with every `T_{x,c}` not touching `x₀`. At `x₀`: by the shift rule (`SMG15.md` Theorem 1), `Y` maps the line of `χ` to the line of `χσ`. So `YW_{x₀}Y=Σ_χW(χσ)P^χ_{x₀}`. By `SMG1.md` Theorem 2.2, `W(χσ)−W(χ)` is `2−(−14)=16` for `χ=1`, `−16` for `χ=σ`, `0−0` for odd `χ` (then `χσ` is odd), and `2−2` for even `χ∉{1,σ}`. So `τYW_{x₀}Y=τW_{x₀}+16τ(P^1_{x₀}−P^σ_{x₀})`. Next, `Yγ_{x₀,c}Y=−γ_{x₀,c}` if `c∈{a,b}` and `+γ_{x₀,c}` otherwise (count anticommutations). `T_{x₀−1,c}` and `T_{x₀,c}` contain `γ_{x₀,c}` once, times operators that commute with `Y`. So exactly the four terms with `c∈{a,b}` change sign, which gives the bond part of `B`.

(iii) For `Φ∈H^σ_{1/2}`, `YH_εΦ=(H_ε+B)YΦ` by (ii), and `Y:H^σ_{1/2}→H^1_{1/2}` is unitary by (i). □

`[check]` (`/tmp/toe-SGAP/check_sgap_sparse.py`, output `out_sparse.txt`; 0.7 s, peak footprint 130 MB, sparse `1024×1024`, run with 52 percent free memory). On an open two-site chain without links, with `τ=1`, `t=0.3`, `ε=0.2`, `a=1`, `b=2`: `‖YHY−(H+B)‖=0` and `‖YW_0Y−W_0−16(P^1_0−P^σ_0)‖=0` exactly in floating point; the `σ`-sector and the neutral sector at light number one both have dimension 32, and their spectra agree to `0`. The gap `E_σ−E_1` is `16.000000` at `ε=0` (`t=0.3` and `t=0`) and `15.997382` at `t=0.3`, `ε=0.05`. **Cap breach, reported.** A first, dense version of the same script (`check_sgap.py`) peaked at 1.10 GB footprint (1.22 GB resident) for 9 s, above the 1 GB cap. It printed the same numbers. It was replaced by the sparse version above and not run again.

**Corollary A1 (two-sided bound, exact).** Let `Ω` range over unit neutral ground vectors (`H_εΩ=E_1Ω`, `Ω∈H^1_{1/2}`) and `Ψ` over unit `σ`-ground vectors. Then

`max_Ψ(−⟨Ψ,BΨ⟩) ≤ E_σ−E_1 ≤ min_Ω⟨Ω,BΩ⟩ ≤ 16τ+8|ε|`.

*Proof.* `f(s):=min spec((H_ε+sB)|H^1_{1/2})` is a minimum of affine functions of `s`, hence concave, with `f(0)=E_1` and `f(1)=E_σ` (Theorem A). Concavity gives `f'_−(1)≤f(1)−f(0)≤f'_+(0)`. In finite dimension, `f'_+(0)=min⟨Ω,BΩ⟩` over unit minimizers at `s=0`, and `f'_−(1)=max⟨Φ,BΦ⟩` over unit minimizers `Φ` at `s=1`. These are `Φ=YΨ`. From `Y(H_ε+B)Y=H_ε` and (ii), `YBY=−B`, so `⟨YΨ,BYΨ⟩=−⟨Ψ,BΨ⟩`. Last, `P^1_{x₀}−P^σ_{x₀}` has spectrum in `{−1,0,1}` and each `T` has norm at most `1` (F1). □

So S-GAP is the statement that one fixed local operator `B`, of norm at most `16τ+8|ε|` and supported on `x₀` and its two bonds, raises the ground energy of the neutral sector by at least `Δτ`. The extensive parts of `E_σ` and `E_1` cancel identically. If S-GAP holds, then `E_0=E_1` and `Δ≤16+8c₀`. The lower bound of Corollary A1 is useful only for a `σ`-ground vector concentrated near `x₀`. `H_ε` commutes with one-site translation, which preserves `H^σ_{1/2}`, so the `σ`-ground space contains a translation eigenvector `Ψ`. For it, `⟨P^σ_{x₀}⟩_Ψ−⟨P^1_{x₀}⟩_Ψ=(⟨𝒩_σ⟩_Ψ−⟨𝒩_1⟩_Ψ)/L` with `𝒩_χ:=Σ_xP^χ_x`, and this is near `−1` whenever `⟨𝒩_1⟩_Ψ` is near `L`; then the bound from that `Ψ` is near `−16τ`. Section 5 (attack A5) returns to this.

### 4.3 The case `t=0`: conserved site parities and mirror-only chains

For `p∈{±1}^{Z_L}` with `∏_xp_x=1` put `K_p:={Φ∈H_G: P_xΦ=p_xΦ for all x}`, `k(p):=#{x: p_x=−1}`, and call the bond `(x,x+1)` a wall of `p` if `p_xp_{x+1}=−1`. For `χ∈Ŝ` let `m(χ):=χ(g₁g₂)`, the parity of the mirror line `χ` (`+1` exactly on `Ŝ_+`). Fix a unit vector `e_χ` in each line.

**Theorem C (`t=0`).** Let `t=0`.

(i) `H_ε` commutes with every `P_x` and with every link operator.

(ii) `H_G=⊕_pK_p`, and each `K_p` is invariant under `H_ε`, `U_g` and `N`. There is a unitary `K_p≅(⊗_{x∈Z_L}C^{16})⊗C²` under which the basis vector `|χ⟩_x` of the `x`-th factor is `e_χ` at site `x` with light occupation `n_x(χ):=(1−p_xm(χ))/2`, and `H_ε|K_p=H_p⊗1`, where

`H_p=τΣ_x(W(χ_x)+14)+εΣ_{x,c}T^p_{x,c}`.

Here `T^p_{x,c}` acts on factors `x,x+1`; its matrix element between `|χ_x,χ_{x+1}⟩` and `|χ_xρ_c,χ_{x+1}ρ_c⟩` has modulus one when `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`, and all its other matrix elements vanish. On `K_p`, `N=Σ_x(1−p_xm(χ_x))/2` and `U_g=∏_xχ_x(g)` are diagonal.

(iii) In `K_p` the on-site term `τ(W(χ_x)+14)` has the single zero vector `|1⟩_x` and is at least `14τ` on its complement. The zero vector `|1⟩^{⊗L}` of `H_M|K_p` (tensored with `C²`) is neutral and has `N=k(p)`. On it, `T^p_{x,c}` acts exactly on the walls of `p`.

*Proof.* (i) `H_M` is even and on-site. `T_{x,c}` commutes with every `P_y` by (F2). At `t=0` no term contains a link operator.

(ii) The `P_x` are commuting involutions; `K_p` are their joint eigenspaces, and `∏_xP_x=1` on `H_G` (`SMG15.md` Theorem 2) forces `∏p_x=1`. By that theorem, `J*P_xJ=P_x⊗1`, and every matter operator that preserves all site parities maps to itself tensored with `1`; `H_M`, `T_{x,c}`, `U_g` and `N` are such operators. So `K_p≅F_p⊗C²`, with `F_p` the matter vectors with site parities `p`. At one site, the vectors of parity `p_x` are (even mirror)`⊗`(light `n` with `(−1)^n=p_x`) plus (odd mirror)`⊗`(light `n` with `(−1)^n=−p_x`). The eight even and eight odd lines are one-dimensional (`SMG1.md` Theorem 2.2), so `{e_χ⊗|n_x(χ)⟩}` is a basis of 16 vectors. For the tensor form, let `C^χ_x` be the polynomial in the creation operators of site `x`, of parity `p_x`, with `C^χ_x|vac⟩=e_χ⊗|n_x(χ)⟩`; it exists and is unique, because a creation polynomial is determined by its action on the empty site. Map `⊗_x|χ_x⟩` to `C^{χ_0}_0C^{χ_1}_1⋯C^{χ_{L−1}}_{L−1}|vac⟩`. This sends an orthonormal basis to an orthonormal basis. An operator `A` that is even and lives on site `x` commutes with every `C^χ_y`, `y≠x`, and maps the parity-`p_x` vectors of site `x` (the span of the `e_χ⊗|n_x(χ)⟩`) to themselves. Normal-order `AC^{χ}_x`: its part without annihilators acts on the empty site as `AC^χ_x` does, so it equals `Σ_{χ'}⟨χ'|A|χ⟩C^{χ'}_x`; the rest, `R`, has an annihilator at `x` on the right of each term, so `R` kills the vector `∏_{y>x}C_y|vac⟩`, whose site `x` is empty. So `A` acts on factor `x` alone, with its one-site matrix, and no signs appear. Now reorder: `T_{x,c}=i[(γ_{x,c}c_x)(γ_{x+1,c}c_{x+1}†)−(γ_{x,c}c_x†)(γ_{x+1,c}c_{x+1})]`, a sum of products of site-even operators (one transposition gives the minus sign, two give the plus sign). `γ_{x,c}c_x†` maps `e_χ⊗|0⟩` to a unit multiple of `e_{χρ_c}⊗|1⟩` (shift rule; `γ_{x,c}` is unitary and the lines are one-dimensional) and kills `e_χ⊗|1⟩`; `γ_{x,c}c_x` does the reverse. Since `m(χρ_c)=−m(χ)`, the slaved occupation flips with the line, so these maps act inside `F_p`. Hence `T_{x,c}|χ_x,χ_{x+1}⟩` is a unit multiple of `|χ_xρ_c,χ_{x+1}ρ_c⟩` when `n_x(χ_x)≠n_{x+1}(χ_{x+1})`, and `0` otherwise. The condition `n_x≠n_{x+1}` reads `p_xm(χ_x)≠p_{x+1}m(χ_{x+1})`, that is `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`. `H_ε` does not act on the `C²` factor (the holonomy label). The formulas for `N` and `U_g` follow from the basis.

(iii) The on-site values are `SMG1.md` Theorem 2.2's: `0` on the trivial line, `14` on odd lines, `16` on the other even lines. On `|1⟩^{⊗L}`, `m=+1` everywhere, `n_x=(1−p_x)/2`, and the condition in (ii) reads `p_xp_{x+1}=−1`. □

**Corollary C1 (the failing steps on file, at `t=0`).** Inside each `K_p` the on-site kernel is one-dimensional, with gap `14τ` (iii). So the failing step of attack 3 on file, Fröhlich-Pizzo's (1.4) with the four-dimensional kernel `ψ⊗{|0⟩,|1⟩}⊗{|+⟩,|−⟩}` (`SMG15_REFEREE.md` line 247), does not occur at `t=0` inside a sector: the light occupation and the link are fixed by `p`, up to the global label on which `H_ε` does not act. The light field has no dynamics at `t=0`: its occupation is a function of the mirror line. So the failing step of attack 2 on file, the `|z|⁻²` tails of free light correlations (`SMG15_REFEREE.md` line 246), has no source at `t=0`. Each `H_p` is a chain of 16-level sites with one on-site matrix, independent of `x` and `p`, and nearest-neighbour terms of norm at most `|ε|` each (F1). This is the class of L1-L3, whose theorems are cited here and not used.

**Proposition C2 (the per-sector form fails).** Let `L∈4N`, `L≥8`, `τ>0`, `t=ε=0`. Let `p` be the alternating pattern `p_x=(−1)^x` with `p_0` and `p_2` changed to `−1`. Then `∏p_x=1`, `k(p)=L/2+2`, and on `K_p∩H_{1/2}` the lowest neutral level and the lowest `σ`-level, for every charged `σ∈Ŝ_+`, are both `28τ`. Meanwhile `E_0=0`.

*Proof.* `∏_x(−1)^x=(−1)^{L/2}=1`, and two sign changes keep the product. On `K_p`, `N=k(p)+Σ_{x:m(χ_x)=−1}p_x` by (ii). So `N=L/2` needs `Σ_{odd sites}p_x=−2`, hence at least two odd sites. At `ε=t=0` the energy is `τΣ_x(W(χ_x)+14)≥28τ`. Equality holds for `χ_0=ρ_a`, `χ_2=ρ_b`, trivial elsewhere: two odd sites with `p=−1`, so `N=L/2`, with charge `ρ_aρ_b`. Taking `b=a` gives a neutral vector; taking `b` with `ρ_aρ_b=σ` (Lemma E) gives a `σ`-vector. `E_0=0` is Proposition Z with `E_L=0`. □

So no proof of S-GAP at `t=0` can treat each `K_p` alone: in some sectors the charged and neutral half-filled levels coincide, and only their height above levels in other sectors (here `28τ` above `E_0`) separates them from the ground energy.

**Remark C3 (second order on each sector, exact identity).** On `K_p`, let `P` project onto `|1⟩^{⊗L}⊗C²` and `Q=1−P`. Then `PH_4P=0` and `PH_4Q(QH_MQ)⁻¹QH_4P=(2/(7τ))·walls(p)·P`. This is `SMG15.md` Theorem 7, case I, read on `K_p`: there `Λ_x²=n_x+n_{x+1}−2n_xn_{x+1}`, which on `|1⟩^{⊗L}` is `1` exactly on the walls. The formal second-order energy `−(2ε²/(7τ))walls(p)` is lowest for the two alternating patterns (`walls=L`, `k=L/2`); every other `p` has at most `L−2` walls, since the number of walls on a ring is even. `SMG15.md` line 152 says the second-order operator is minimized by the two alternating occupations. Theorem C adds that at `t=0` the pattern `p` is conserved exactly, at every order. Higher orders are not bounded here.

**Proposition C5 (an exact sufficient pair, `t=0`).** Let `t=0` and `E_*:=min spec(H_ε|H_G)`, the ground energy over all particle numbers. Suppose, for some `c₀>0`, `Δ_G>0`, `δ≥0` and all `|ε|≤c₀τ`, `L∈4N`, `L≥8`:

(G1) for every `p`, `H_p` has a nondegenerate lowest eigenvalue `e_p`, and every other eigenvalue of `H_p` is at least `e_p+Δ_Gτ`;

(HF') `E_0−E_*≤δτ`.

Then `E_σ≥E_0+(Δ_G−δ)τ` for every charged `σ`. So (G1) and (HF') with `δ<Δ_G` give S-GAP⁰ with `Δ=Δ_G−δ`.

*Proof.* The lowest vector of `H_p` is `|1⟩^{⊗L}` at `ε=0` (Theorem C (iii)), which is neutral. `U_g` commutes with `H_p`, so a nondegenerate lowest vector has one character. Along `s↦H_p(s)`, with `s` running from `0` to the given `ε`, the lowest eigenvalue stays isolated by (G1), so its spectral projection is continuous in `s`; its character, a continuous function of `s` with values in a finite set, stays trivial. So every charged vector of `K_p` is orthogonal to the lowest vector, and its energy is at least `e_p+Δ_Gτ`. Since `min_pe_p=E_*` (Theorem C (ii)), `E_σ≥E_*+Δ_Gτ≥E_0+(Δ_G−δ)τ`. □

(G1) is of the type L1-L3 state for chains with a one-dimensional on-site kernel; it is not rebuilt here. (HF') says the half-filling constraint costs at most `δτ` against the best filling. At second order (Remark C3) the best `p` are the two alternating patterns, which are half filled, so formally `E_0=E_*`; nothing beyond second order is proved here.

**Remark C6 (even multiplicities at `t=0`).** At `t=0`, `H_ε|K_p=H_p⊗1_{C²}` (Theorem C (ii)), where `C²` carries the holonomy label of `SMG15.md` Theorem 2. `U_g` and `N` act on `F_p` only, so they act trivially on `C²`. So every eigenvalue of `H_ε` on each `H^χ_{1/2}` has even multiplicity. S-GAP sets uniqueness aside (`SMG15.md` line 152); this shows that at `t=0` (with `τ_E=0`, as in all of `SMG15.md`) the ground vector of `H_{1/2}` is never unique, so R15-SPEC's (S3) needs `t≠0` there. `SMG1.md` Theorem 4.1 uses `τ_E>0` for its uniqueness for the same reason.

### 4.4 Removing the charge from the charged ground vector

**Lemma R (removal identity, every `t`).** Let `σ∈Ŝ_+` be charged, choose `a,b` as in Theorem A, and let `Ψ` be a unit vector with `Ψ∈H^σ_{1/2}`, `H_εΨ=E_σΨ`. For each site `y` put `D_y:=Y_yP^σ_y`, `Y_y:=iγ_{y,a}γ_{y,b}`, and `H_4^{(y)}:=Σ_c(T_{y−1,c}+T_{y,c})`. Then `D_yΨ∈H^1_{1/2}`, `‖D_yΨ‖=‖P^σ_yΨ‖`, and

`⟨D_yΨ,H_εD_yΨ⟩=(E_σ−16τ)‖P^σ_yΨ‖²−ε⟨P^σ_yΨ,H_4^{(y)}Ψ⟩`.

Hence, with `w:=Σ_y‖P^σ_yΨ‖²` and `W_odd:=Σ_y‖O_yΨ‖²`, where `O_y` projects onto the odd lines at `y`:

`(E_σ−E_1−16τ)w ≥ −|ε|X`, `X:=Σ_y|⟨P^σ_yΨ,H_4^{(y)}Ψ⟩| ≤ 4√2·√(w·W_odd)`.

*Proof.* `Y_y` maps line `σ` to line `1` and preserves `H_{1/2}` (Theorem A (i)), so `D_yΨ` is neutral; `D_y*D_y=P^σ_y`. By Theorem A at `x₀=y`, `D_y*H_εD_y=P^σ_y(H_ε+B_y)P^σ_y`. Here `P^σ_yB_yP^σ_y=−16τP^σ_y`: `P^σ_yP^1_y=0`, and each `T` on a bond at `y` changes the line at `y` by some `ρ_c≠1`, so `P^σ_yTP^σ_y=0`. `H_M` and `H_L` commute with `P^σ_y`, so `P^σ_yH_ε(1−P^σ_y)=εP^σ_yH_4^{(y)}`. Therefore `⟨Ψ,P^σ_yH_εP^σ_yΨ⟩=E_σ‖P^σ_yΨ‖²−ε⟨P^σ_yΨ,H_4^{(y)}Ψ⟩`, which gives the identity. Since `D_yΨ` is neutral, its energy is at least `E_1‖P^σ_yΨ‖²`; summing over `y` gives the inequality. For the bound on `X`: a term `T_{b,c}` on a bond at `y` maps line `σρ_c` at `y` to line `σ`, so `⟨P^σ_yΨ,T_{b,c}Ψ⟩=⟨P^σ_yΨ,T_{b,c}P^{σρ_c}_yΨ⟩`, of modulus at most `‖P^σ_yΨ‖‖P^{σρ_c}_yΨ‖`. As `c` runs over `1,…,8`, `σρ_c` runs over the eight odd characters (Lemma E). Two bonds touch `y`. So `X≤2Σ_yΣ_c‖P^σ_yΨ‖‖P^{σρ_c}_yΨ‖≤2√8·Σ_y‖P^σ_yΨ‖‖O_yΨ‖≤4√2√(wW_odd)`, by Cauchy-Schwarz twice. □

So `E_σ−E_1≥16τ−4√2|ε|√(W_odd/w)` whenever `w>0`. This is exact and holds for every `t`. It proves S-GAP for any family of charged ground vectors with `W_odd≤Kw`, `K` independent of `L`, once `4√2c₀√K<16`.

**Proposition R2 (the odd weight is extensive, `t=0`).** Let `t=0`, `0<ε≤τ`, `L∈4N`, `L≥8`, and `σ∈Ŝ_+` charged. Then `E_σ(ε)≤16τ−(L/2−1)g(ε)` with `g(ε):=(2ε²/(7τ))/(1+ε²/(98τ²))`. There is `ε'∈(0,ε]` at which `E_σ` is differentiable, and every unit `σ`-ground vector `Ψ` at `ε'` has `W_odd(Ψ)≥Lε²/(200704τ²)`.

*Proof.* Work in `K_p` for `p_x=(−1)^x` (Theorem C); here every bond is a wall. Take the product vector with `|σ⟩` at site `0`, `|1⟩` at site `1`, and on each bond `(2j,2j+1)`, `1≤j≤L/2−1`, the unit vector `φ_j∝|1,1⟩−κΣ_cω_c|ρ_c,ρ_c⟩`, `κ:=ε/(28τ)`, `ω_c:=⟨ρ_c,ρ_c|T^p_{2j,c}|1,1⟩` (modulus one, Theorem C (ii)). Its charge is `σ∏(ρ_c)²=σ`. On each block the pair `(ρ_c,ρ_c)` moves the light particle within the bond, so `N=k(p)=L/2`. Each block contributes `[8κ²·28τ−16εκ]/(1+8κ²)=−g(ε)`: the numerator is `(2/7−4/7)ε²/τ`, and `T^p_{2j,c'}`, `c'≠c`, sends `|ρ_c,ρ_c⟩` outside the support of `φ_j`. Every bond between blocks, and every bond at sites `0` and `1`, changes the line at one site of each of two different factors by some `ρ_c≠1`; the result is orthogonal to the product vector, whose blocks carry equal lines on their two sites, so these expectations vanish. Site `0` costs `16τ`. This gives the first claim. `E_σ(ε)` is the lowest eigenvalue of an analytic Hermitian family, so it is concave (a minimum of affine functions) and differentiable except at finitely many points of `[0,ε]`; it is even (F4), and `E_σ(0)=16τ` (Proposition Z with `E_L=0`). A concave function's derivative does not increase, and its average over `[0,ε]` is `(E_σ(ε)−E_σ(0))/ε`; so there is a differentiability point `ε'∈(0,ε]` with `E_σ'(ε')≤−(L/2−1)g(ε)/ε≤−(L/4)(ε/(7τ))`, using `g(ε)/ε≥ε/(7τ)` for `ε≤τ` and `L/2−1≥L/4`. At a differentiability point every unit ground vector has `⟨Ψ,H_4Ψ⟩=E_σ'(ε')` (one-sided derivatives of a lowest eigenvalue are the extreme values of `⟨H_4⟩` on the ground space). Each `T_{y,c}` flips the mirror parity at `y`, so `T_{y,c}=O_yT_{y,c}(1−O_y)+(1−O_y)T_{y,c}O_y` and `|⟨Ψ,T_{y,c}Ψ⟩|≤2‖O_yΨ‖`. Summing over `8L` terms, `|⟨Ψ,H_4Ψ⟩|≤16Σ_y‖O_yΨ‖≤16√(L·W_odd)`. So `W_odd≥(Lε/(28τ))²/(256L)=Lε²/(200704τ²)`. □

## 5. Attacks on what stays open

**The stopping lemma, S-GAP⁰ (open).** S-GAP at `t=0`: there are `c₀,Δ>0` such that `E_σ≥E_0+Δτ` for every charged `σ`, every `τ>0`, every `|ε|≤c₀τ` and every `L∈4N`, `L≥8`, with `t=0`. By Theorem C it is a statement about the `2^{L−1}` chains `H_p`:

`min_p min spec(H_p | σ-charged, N=L/2) ≥ min_p min spec(H_p | neutral, N=L/2) + Δτ`.

S-GAP⁰ is the case `t=0` of S-GAP, which `SMG15.md` line 152 includes. A counterexample to S-GAP⁰ refutes S-GAP. Proposition Z proves it at `ε=0` with `Δ=16`. Three attacks on it fail, each at a named step. None of them is one of the three on file (local Schrieffer-Wolff, absolute polymer expansion with a free light field, Fröhlich-Pizzo; `SMG15.md` lines 156-158).

**Attack A4: remove the charge from the charged ground vector (Lemma R).** *Plan.* Lemma R is exact. It proves S-GAP⁰, and S-GAP, as soon as `W_odd≤Kw` with `K` independent of `L` and `4√2c₀√K<16`. *Failing step: the bound `W_odd≤Kw`.* Proposition R2 proves that `W_odd` is at least `Lε²/(200704τ²)` for every charged ground vector at some `ε'∈(0,ε]`. So the step needs `w≥Lε²/(200704Kτ²)`: an extensive number of `σ`-lines in the charged ground vector. The ingredients of Lemma R (the eigen-equation, Theorem A, Cauchy-Schwarz) give no lower bound on `w` that grows with `L`. The loss sits in the Cauchy-Schwarz step: it pairs the `σ`-weight at `y` with all odd weight at `y`. In the product vector of Proposition R2's proof, the odd weight sits in pair fluctuations on every block, almost all of them far from the `σ`-line, and Cauchy-Schwarz cannot tell that weight from odd weight next to the `σ`-line. Separating the two needs a statement about how the charged ground vector is built near its `σ`-line: a cluster property. Lemma R does not supply it. The attack uses `t=0` only in Proposition R2, so it fails the same way for S-GAP.

**Attack A5: shift the charge to a fixed site and split off a window (Theorem A with an Anderson bound).** *Plan.* By Theorem A, `E_σ=min spec((H_ε+B)|H^1_{1/2})` with `B` local at `x₀`. Let `Λ` be a window containing `x₀` and its two bonds, `K` the sum of the terms of `H_ε` that touch `Λ`, and `H_out:=H_ε−K`. Then `E_σ≥λ(H_out)+λ(K+B)`, where `λ` is a lowest eigenvalue on a space that contains `H^1_{1/2}`, and likewise `E_1≥λ(H_out)+λ(K)`. The hope is that `λ(K+B)` exceeds `λ(K)` by order `τ`, with the surface difference `E_1−λ(H_out)−λ(K)` controlled separately. *Failing step: `λ(K+B)>λ(K)`. It is false: `λ(K+B)=λ(K)` exactly.* `Y` commutes with `H_out`, and `Y(H_ε+B)Y=H_ε` (from `YBY=−B`). So `Y(K+B)Y=K`, and the two windows have the same spectrum. The Anderson bound for `E_σ` is then the same number as the Anderson bound for `E_1`, so the method gives at most `E_σ−E_1≥λ(H_out)+λ(K)−E_1≤0`. The reason is structural: in the shifted frame, line `σ` at `x₀` costs nothing, and only the global neutrality of `H^1_{1/2}` forces a second defect. A window does not see a global constraint. Restricting the window to its own neutral part is not allowed: a neutral vector may carry `σ` inside the window and `σ` outside it. The attack holds for every `t` and fails the same way.

**Attack A6: split by conserved site parities, then use a gap in each sector (Theorem C).** *Plan.* At `t=0` each `H_p` is a chain of 16-level sites with a one-dimensional on-site kernel, an on-site gap `14τ`, and nearest-neighbour terms of norm at most `|ε|` each (Corollary C1). The obstacles of attacks 2 and 3 on file are absent there. A uniform gap above the ground vector of each `H_p`, of the kind L1-L3 state (cited here, not rebuilt), would then bound the charged levels in each sector. *Failing step: the comparison across sectors.* Proposition C2 proves the per-sector statement false: in some sector the lowest neutral and charged half-filled levels coincide. So the levels of an unbalanced sector (`k(p)≠L/2`) must be compared with `E_0`, which lives in another sector. Given (G1), Proposition C5 shows that (HF') suffices for this comparison. Two bounds are available. Lower: for every unit vector of `K_p`, `⟨H_p⟩≥14τW_odd−16|ε|√(L·W_odd)≥−(32/7)(ε²/τ)L`, because `H_M≥14τΣ_yO_y` and `|⟨H_4⟩|≤16√(L·W_odd)` (proof of Proposition R2). Upper: `E_0≤E_1≤−(L/2)g(ε)`, from the product vector of Proposition R2 with all `L/2` bonds `(2j,2j+1)` paired and no `σ`-line. These differ by an amount of order `(ε²/τ)L`. The needed comparison is of order `τ`, between energies of order `(ε²/τ)L` whose formal leading terms differ only by `(2ε²/(7τ))(L−walls(p))` (Remark C3). So the step needs each sector's ground energy written as a sum of `p`-local terms with summable tails, to precision `o(1)` in `L`, and then a comparison of the resulting classical energies of `p`: the methods of L1-L4, not rebuilt here. The attack is specific to `t=0`: for `t≠0`, `hop_x` does not commute with `P_x` (the `[check]` gives `‖[H,P_x]‖=0.6` at `t=0.3`, against `0` at `t=0`).

**What is not attempted.** A native convergent expansion in each `K_p`, with `p`-local sector energies and a Peierls-type bound for the classical energy of `p`, is the route the failing step of A6 points to. Corollary C1 shows that neither failing step on file blocks it at `t=0`. This file does not write it and claims nothing about it.

**S-GAP at `t≠0`.** It stays open, with the three failed attacks on file and A4, A5 above. At `t≠0` the light chain moves, the sectors of Theorem C mix, and the formal second-order light operator is the induced density interaction of `SMG15.md` Theorem 7, with the ratio `ε²/(τ|t|)` of `SMG15.md` line 142. Theorem A recasts S-GAP, for every `t`, as the rise of the neutral ground energy caused by one local operator `B`. A constructive renormalisation group of the Benfatto-Mastropietro type (L9-L11) would have to control that rise in a gapless chain with a marginal coupling. In the shifted frame the rise comes with a mobile defect that neutrality forces, the effect A5 isolates. No fetched work (section 2) controls such an energy.

---

## FINISH

**Readings and the four tests.** No reading, specification or definition is proposed. S-GAP⁰ is the `t=0` case of S-GAP as `SMG15.md` line 148 states it. (G1) and (HF') are hypotheses of a proved implication, not proposals. `Ŝ_+`, `K_p`, walls, `w` and `W_odd` are notation. For the record, S-GAP⁰ as a named sub-lemma passes the four tests: (1) it fixes no part's target, being a case of an existing open statement; (2) its quantifiers are closed; (3) it settles no downstream question by premise; (4) it adds no structure or constant.

**Proved.**
- Lemma E: on `H_{1/2}`, `U_{g₁g₂}=1`; the occurring charges are the eight characters of `Ŝ_+`; each charged one is `ρ_aρ_b`.
- Proposition Z: at `ε=0`, for every `t`, `τ` and `L∈4N`: `E_1=E_L` and `E_σ=E_L+16τ` for every charged `σ`.
- Theorem A (charge shift), every `t`, `ε`: `YH_εY=H_ε+B`, `B=16τ(P^1_{x₀}−P^σ_{x₀})−2εΣ_{c∈{a,b}}(T_{x₀−1,c}+T_{x₀,c})`; the `σ`-block of `H_ε` is unitarily equivalent to the neutral block of `H_ε+B`. Corollary A1: the two-sided bound with upper end `16τ+8|ε|`.
- Theorem C (`t=0`): conserved site parities; `H_ε|K_p=H_p⊗1`, a chain of 16-level sites with one-dimensional on-site kernel and gap `14τ`, bond terms of modulus-one matrix elements exactly where `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`. Corollary C1. Remark C3 (second order equals `−(2ε²/(7τ))walls(p)`). Proposition C5 ((G1) and (HF') imply S-GAP⁰ with `Δ=Δ_G−δ`). Remark C6 (even multiplicities at `t=0`).
- Lemma R (removal identity) and Proposition R2 (`W_odd≥Lε²/(200704τ²)` at some `ε'∈(0,ε]`, `t=0`).
- Facts F1-F4, including the sign symmetry `E_χ(ε)=E_χ(−ε)`.

**Counterexamples.** Proposition C2 refutes the per-sector form of S-GAP at `t=ε=0` (a sector with `k(p)=L/2+2` in which the lowest neutral and charged half-filled levels are both `28τ`). It is not a counterexample to S-GAP. The identity `λ(K+B)=λ(K)` refutes the step attack A5 needs. No counterexample to S-GAP or S-GAP⁰ is known.

**Open by name.**
- **S-GAP⁰** (S-GAP at `t=0`), the stopping lemma. Three attacks failed: A4, charge removal (at `W_odd≤Kw`); A5, charge shift with a window bound (at `λ(K+B)>λ(K)`, false); A6, sector splitting with a per-sector gap (at the comparison across sectors, which needs (HF') given (G1)). The route the failing step of A6 points to, a native convergent expansion in each sector with `p`-local energies and a Peierls-type bound for the classical energy of `p`, is not attempted.
- **S-GAP at `t≠0`**: open, with the three attacks on file (`SMG15.md` lines 156-158) and A4, A5.

**What changes downstream.**
- `SMG15.md` (R1.5): on `H_{1/2}`, S-GAP's best constant at `ε=0` is `16`, not `14`. S-GAP is equivalent to the statement that the local operator `B` of Theorem A raises the neutral ground energy by `Δτ`. Its `t=0` case is a problem about gapped 16-level chains plus a comparison across sectors (Theorem C, Proposition C5). A `t=0` lane can target (G1) natively and (HF'). A `t≠0` lane with a constructive renormalisation group must control the energy cost of `B` in the gapless chain.
- R1.5-U: at `t=0` (with `τ_E=0`) every level of `H_ε` on `H_{1/2}` has even multiplicity (Remark C6), so uniqueness needs `t≠0` or `τ_E>0`.
- SMG1's later rungs (R2, R3): Theorem A's proof uses only one-dimensional character lines, a charge reachable by an even on-site unitary, and terms that touch a site through single Majoranas. A rung with these features gets the same reduction of a charged gap to the energy cost of one local operator. This is a remark, not a theorem about those rungs.
- No frozen part changes. No axiom, law or working-set entry changes. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.

**Scratch.** `/tmp/toe-SGAP/check_sgap_sparse.py` and `out_sparse.txt` (within the cap); `check_sgap.py` (dense, one run over the 1 GB cap, reported in section 4.2).
