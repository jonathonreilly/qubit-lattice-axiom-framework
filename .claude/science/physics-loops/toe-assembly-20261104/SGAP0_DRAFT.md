lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane

# SGAP0: the zero-hop charged gap S-GAP⁰ by a native expansion in each parity sector, pass 1

Written 2026-11-07 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 of lane SGAP0 (wall W2) under the method of open PR #10138. Claude drafts at length and runs to closure; Codex distils; a fresh session referees; then the part is frozen.

**What this file is.** An author-side long draft. It grants no status. It adopts no law, reading or definition. It changes no axiom and no working-set entry; `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means the argument is written out in full below; it has not yet been distilled or refereed. Every proof is by hand. No step is computer-assisted. "[check]" marks a tiny scratch computation in `/tmp/toe-SGAP0/`; a check guides and never proves. Nothing here is a verdict.

**Source revisions read.** Branch `claude/toe-assembly` at commit `fa803749e`. Files in this folder, with the last commit that touches each:

| File | Last commit | Lines read |
|---|---|---|
| `prior/SGAP0.md` | `fa803749e` | all |
| `SGAP.md` (frozen) | `8e8a7352d` | 1-153 (all) |
| `SGAP_REFEREE.md` | `51ce28531` | 1-272 (all) |
| `SMG15.md` (frozen) | `8e8a7352d` | 1-8, 13-22, 28-34, 130-162 |
| `SMG1.md` (frozen) | `373e01725` | lines 7, 49, 53, 69, 118, 132, 149 (grep hits) |
| `TOE_ASSEMBLY.md` | `dd158e6a2` | 201-270 (sections 3.4-3.11), 726-740 (section 11) |
| `Y2W_DRAFT.md` | `92e03055c` | 1-40, for the format only |

No other branch was read. The digest's main-branch items (the clock note, the SU(3) Yarotsky note, the ring comparator, the Spin(10) note) were checked by the SGAP referee at `origin/main` `f5af11cd0` (`SGAP_REFEREE.md` section 4.5). This file uses none of them in a proof, so they were not re-read.

**Working set used, by name.** None directly. The model is the frozen `t=0`, zero-electric-coupling ring of `SGAP.md` Definitions 1-6. It enters through the atom of `SMG1.md` Theorem 2.2 and the Gauss reduction of `SMG15.md` Theorem 2, as `SGAP.md` Theorem 4 packages them. Through those, PS-5 and PS-6r enter as in `SGAP.md`. The owner frame is SMG1-GAP (bounded R-GEN, `TOE_ASSEMBLY.md` 3.10). S-GAP⁰ is a finite-ring spectral statement; it neither uses nor contradicts that frame.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The model of `SGAP.md` is read plainly. No reading is proposed below, so no four-test check is needed; section 6 says why.

---

## 0. The question, quoted

`SGAP.md` line 20 (Definition 4): "**S-GAP** asks for `c₀,Δ>0` such that for every `τ>0`, `|t|,|ε|≤c₀τ`, allowed `L`, and `χ≠1`, `E_χ≥E_0+Δτ`. **S-GAP⁰** is the same statement with `t=0`. Both include `ε=0`. These are finite-ring questions, not GNS or tick statements."

`SGAP.md` line 93 (referee closure): "At `t=0`, let **(G1′)** assert that there are `c₀,Δ_G>0` such that for every allowed `L`, `τ>0`, `|ε|≤c₀τ` and every `p`, every `S`-charged vector of `K_p`, of any `N`, has energy at least `e_p+Δ_Gτ`." The same line: "Together (G1′) and (HF′) give `E_σ≥min_p e_p+Δ_Gτ=E_*+Δ_Gτ≥E_0+(Δ_G−δ)τ`".

`SGAP.md` line 95: "Let `p_alt` be alternating and let **(HF-alt)** be `e_{p_alt}−min_p e_p≤δτ`."

`SGAP.md` line 147 (A6): "A convergent sector expansion with controlled `p`-local energy terms and a classical comparison is a proposed route, not a proved necessity or an attempted construction."

The lane's target: prove (G1′) and (HF-alt) at `t=0` for small `ε`, by a native expansion in each sector, with explicit constants uniform in `L`; hence S-GAP⁰. Or give a counterexample, or a lemma that fails three named attacks distinct from A1-A6.

## 0.1 Outcome in one paragraph

**Proved: S-GAP⁰, with `c₀ = 2·10⁻¹⁰` and `Δ = 7`.** The constants are explicit and far from optimal. They do not depend on `L`, `τ` or the sign of `ε`. The proof is a space-time polymer expansion inside each parity chain `H_p`. Imaginary time is cut into slots of length `1/(2τ)`. A history of the Dyson series has a shadow of space-time cells, and its weight factorizes over shadow components (Lemma 4.2). Every component carries a weight bounded per cell (Lemma 4.3). A Dobrushin-type inductive lemma, rebuilt in full (Lemma 4.5), controls the gas of components that do not wind around the time circle. Two results follow. **Theorem A (this is (G1′), strengthened).** For `|ε| ≤ τ/120000`, every `p` and every allowed `L`, every vector of `K_p` whose charge or light number differs from the chain vacuum's has energy at least `e_p + 3.3τ`; for `|ε| ≤ 10⁻⁸τ` the bound is `e_p + 7τ`. A charged vector forces a component that winds in time, and each winding slot costs a fixed factor. **Theorem B (this is (HF-alt) with `δ = 0`, made strict).** For `|ε| ≤ 2·10⁻¹⁰τ`, `e_p ≥ e_{p_alt} + (L − walls(p)) ε²/(6τ)` for every `p`. The proof interpolates the activities of the two chains. Their activities agree on every component that sees no non-wall bond of `p` (Lemma 5.1, an exact Fock-space identity). At each non-wall bond the alternating chain gains the vacuum pair, worth `2ε²/(7τ)` per unit time; everything else there is `O(ε⁴)`. **Corollary C.** The two theorems give S-GAP⁰ through `SGAP.md` Proposition 4.3's route, with no continuity argument. They also show `E_0 = e_{p_alt}`. No counterexample arises. S-GAP at `t ≠ 0` stays open: there the parity sectors mix and the free light chain is gapless, and nothing here touches that.

## 1. Setup: the t = 0 parity chains

Everything in this section is ported from the frozen `SGAP.md` (Definitions 1-6, Theorems 1 and 4), with its notation. Fix an allowed `L` (`L∈4N`, `L≥8`), `τ>0`, real `ε`, and `t=0`.

**1.1 The chain.** Fix `p∈{±1}^{Z_L}` with `∏_xp_x=1`. `SGAP.md` Theorem 4: "`K_p ≅ (⊗_x C^{16})⊗C²`, `H_ε|K_p=H_p⊗1`". Write `𝓗=⊗_{x∈Z_L}C^{16}` with orthonormal basis `|χ⟩=⊗_x|χ_x⟩`, `χ∈Ŝ^{Z_L}`, where `Ŝ` is the 16-element character group. Then `H_p=H_0+εV`:

- `H_0=τΣ_x e(χ_x)`, diagonal, with `e(1)=0`, `e(χ)=14` for the eight odd `χ` (`m(χ)=−1`) and `e(χ)=16` for the seven even `χ≠1`. These are `W+14` on the three line types (`SGAP.md` Definition 2).
- `V=Σ_{x∈Z_L}Σ_{a=1}^{8}T_{x,a}`. "Bond `x`" is the pair `(x,x+1)`. `SGAP.md` Theorem 4: "`T^p_{x,a}` connects `|χ_x,χ_{x+1}⟩` to `|χ_xρ_a,χ_{x+1}ρ_a⟩` with matrix element of modulus one exactly when `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`; otherwise it annihilates that basis vector." Call that condition **active**. Each `T_{x,a}` is Hermitian (`SGAP.md` Theorem 1). The move flips both `m` values, so the target of an active move is active for the same bond and flavour. Write `ω` for the modulus-one matrix element of a move.

A bond `x` is a **wall** of `p` if `p_xp_{x+1}=−1`, and a **non-wall** otherwise. Write `NW(p)` for the set of non-wall bonds, so `walls(p)=L−|NW(p)|`. The alternating pattern `p_alt` has `NW=∅`. At a wall a move is active on pairs of lines of equal parity; at a non-wall, on pairs of opposite parity.

**1.2 Conserved labels.** Put `n_x(χ)=(1−p_xm(χ))/2` (`SGAP.md` Definition 5), `N(χ)=Σ_xn_x(χ_x)`, and the charge `q(χ)=∏_xχ_x∈Ŝ`. The vacuum `|𝟙⟩=|1⟩^{⊗L}` has `q=1` and `N=k(p)` (`SGAP.md` Theorem 4). Put `ν(χ)=N(χ)−k(p)=Σ_x[n_x(χ_x)−n_x(1)]`. Vacuum sites contribute `1` to `q` and `0` to `ν`.

*Fact 1.1.* An active move preserves `q` and `ν`. *Proof.* `ρ_a²=1` gives `q`. The move replaces `n_x,n_{x+1}` by `1−n_x,1−n_{x+1}`. The active condition reads `p_xm(χ_x)≠p_{x+1}m(χ_{x+1})`, that is `n_x≠n_{x+1}`, so `n_x+n_{x+1}=1` is unchanged. `□`

So `H_p` commutes with the diagonal operators `q` and `N`. Let `𝒱_p=span{|χ⟩: q(χ)=1, ν(χ)=0}` and `𝒱_p^⊥` its orthogonal complement in `𝓗`. Both are invariant. Put

`e_p = min spec H_p`,  `E^⊥_p = min spec(H_p|𝒱_p^⊥)`.

**1.3 Link to S-GAP⁰.** By Theorem 4 of `SGAP.md`, `H_ε` is block diagonal over `p`, the `C²` factor is inert, and the charge and `N` of a vector of `K_p` are `q` and `N` above. Hence `E_χ=min_p min spec(H_p` on `q=χ`, `N=L/2)`, and `E_0=min_χE_χ`. (G1′) is the statement `min spec(H_p` on `q≠1) ≥ e_p+Δ_Gτ`; since `{q≠1}⊂𝒱_p^⊥`, the bound `E^⊥_p≥e_p+Δ_Gτ` implies it.

*Fact 1.2 (translation).* `e_{−p_alt}=e_{p_alt}`. *Proof.* The cyclic shift `γ_{x,a}↦γ_{x+1,a}`, `c_x↦c_{x+1}`, link `x`↦link `x+1` is an automorphism of the finite algebra of modes and links. That algebra is a full matrix algebra, so the shift is implemented by a unitary `U_T`. At `t=0`, `H_ε=τΣ_x(W_x+14)+εΣ_{x,a}iγ_{x,a}γ_{x+1,a}hop⁰_x` is a sum of one term per site and per bond, and the shift maps each term to the next, the wrap bond included. It maps `G_x` to `G_{x+1}` and `P_x` to `P_{x+1}`. So `U_T` commutes with `H_ε`, preserves `H_G`, and maps `K_p` onto `K_{p′}` with `p′_x=p_{x−1}`. It maps `p_alt` to `−p_alt`. `□`

**1.4 Standing constants.** Throughout: the slot length `δ=1/(2τ)`; the reference coupling `R=τ/120000`; `λ=|ε|/R`; `v=e^{−14τδ}=e^{−7}`; for `r≥0`, `u(r)=e^{8rδ}−1=e^{4r/τ}−1` and `φ(r)=max(√u(r), v)`; `ϑ_ε=2φ(|ε|)` and `ϑ=2φ(R)`. Numerically `u(R)=e^{1/30000}−1≤3.334·10⁻⁵`, so `√u(R)≤5.775·10⁻³`, `v≤9.12·10⁻⁴`, and

`ϑ ≤ 0.01155`,  `16ϑ ≤ 0.1848`.

For `|ε|≤R`: `λ≤1` and `ϑ_ε≤ϑ`. For `|ε|≤10⁻⁸τ`: `√u(|ε|)≤2.0·10⁻⁴<v`, so `ϑ_ε=2e^{−7}`.

## 2. Literature read

Searches were run on 2026-11-07 (WebSearch, standard mode) for: Yarotsky's weak-perturbation papers; Fernández-Procacci on abstract polymer models; Datta-Fernández-Fröhlich-Rey-Bellet; Borgs-Kotecký-Ueltschi; Kennedy-Tasaki 1992; Del Vecchio-Fröhlich-Pizzo-Rossi; space-time cluster expansions with the Kotecký-Preiss criterion for gaps. Pages fetched with WebFetch are marked "fetched". The fetch tool paraphrases; quotes below are the short phrases it returned. **No citation is load-bearing.** Every step used below is proved in this file.

| # | Work | Status here | What was checked |
|---|---|---|---|
| L1 | R. Fernández, A. Procacci, *Cluster expansion for abstract polymer models. New bounds from an old approach*, arXiv:math-ph/0605041 (published version DOI 10.1007/s00220-007-0279-2, as the arXiv page lists it; volume and pages NOT VERIFIED) | fetched (abstract, ar5iv text) | eq. (2.2), the polymer partition function; eq. (2.12), the Kotecký-Preiss condition `ρ_{γ₀} exp[Σ_{γ≁γ₀} μ_γ] ≤ μ_{γ₀}`; eq. (2.13), the Dobrushin condition `ρ_{γ₀} ∏_{γ≁γ₀}(1+μ_γ) ≤ μ_{γ₀}`, with the note that the product "include[s] γ₀, which is always incompatible with itself" |
| L2 | R. Kotecký, D. Preiss, *Cluster expansion for abstract polymer models*, CMP 103 (1986) 491-498 | **NOT VERIFIED** (Project Euclid page returned empty) | only its criterion as printed in L1 (2.12) |
| L3 | R. L. Dobrushin, *Estimates of semiinvariants for the Ising model at low temperatures*, AMS Transl. (2) 177 (1996) 59-81 | **NOT VERIFIED** (not online) | only its condition as printed in L1 (2.13); Lemma 4.5 below is the inductive argument credited to it, rebuilt |
| L4 | D. Ueltschi, *Cluster expansions and correlation functions*, arXiv:math-ph/0304003, Moscow Math. J. 4 (2004) 511-522 | fetched (abstract) | a cluster expansion for discrete and continuous systems whose condition is "an extension of the neat Kotecky-Preiss criterion" |
| L5 | C. Borgs, R. Kotecký, D. Ueltschi, *Low temperature phase diagrams for quantum perturbations of classical spin systems*, CMP 181 (1996) 409-446; mp_arc 95-233 | fetched (mp_arc abstract only; the PDF did not convert) | maps a `d`-dimensional quantum system with `H = H⁽⁰⁾ + λV`, `H⁽⁰⁾` diagonal, onto a classical contour system in `d+1` dimensions. Its contour definitions and bounds are **NOT VERIFIED** |
| L6 | D. A. Yarotsky, *Ground states in relatively bounded quantum perturbations of classical lattice systems*, arXiv:math-ph/0412040, CMP 261 (2006) 799-819 | fetched (abstract) | spectral gap, exponential decay of truncated correlations and analyticity of the ground state for such perturbations |
| L7 | D. A. Yarotsky, *Uniqueness of the ground state in weak perturbations of non-interacting gapped quantum lattice systems*, J. Stat. Phys. 118 (2005) 119-144 | **NOT VERIFIED** (no arXiv copy found) | known here only through L8's abstract |
| L8 | J. Henheik, S. Teufel, T. Wessel, *Local stability of ground states in locally gapped and weakly interacting quantum spin systems*, arXiv:2106.13780, LMP 112 (2022) | fetched (abstract) | its results are "technically corollaries to a theorem of Yarotsky" (L7) |
| L9 | D. A. Yarotsky, *Quasi-particles in weak perturbations of non-interacting quantum lattice systems*, arXiv:math-ph/0411042 | fetched (abstract) | "a general weak perturbation of a non-interacting quantum lattice system with a non-degenerate gapped ground state" |
| L10 | J. Fröhlich, A. Pizzo, *Lie-Schwinger block-diagonalization and gapped quantum chains*, arXiv:1812.02457 (v2, 2019) | fetched (abstract) | chain-length-uniform gap for small short-range perturbations of an on-site gapped Hamiltonian, by "local Lie-Schwinger conjugations" |
| L11 | S. Del Vecchio, J. Fröhlich, A. Pizzo, S. Rossi, arXiv:1908.07450 (DOI 10.1007/s00220-020-03878-y) | fetched (abstract) | the same conclusion for interactions form-bounded by the on-site terms |
| L12 | S. Del Vecchio, J. Fröhlich, A. Pizzo, S. Rossi, *Local iterative block-diagonalization of gapped Hamiltonians*, arXiv:2007.07667, J. Math. Phys. 63, 073503 (2022) | search snippet only, **NOT VERIFIED** | |
| L13 | S. Michalakis, J. Pytel, *Stability of frustration-free Hamiltonians*, arXiv:1109.1588, CMP 322 (2013) 277-302 | fetched (abstract) | stability of the gap of frustration-free Hamiltonians under quasi-local perturbations, given "Local Topological Quantum Order" |
| L14 | T. Kennedy, H. Tasaki, CMP 147 (1992) 431-484 | search only; its perturbative content **NOT VERIFIED** | |
| L15 | N. Datta, R. Fernández, J. Fröhlich, L. Rey-Bellet, Helv. Phys. Acta 69 (1996); mp_arc 96-226 | search only, **NOT VERIFIED** | |

**How this file uses them.** L5, L6 and L7 treat quantum perturbations of a classical (diagonal) Hamiltonian with a unique ground configuration through a space-time expansion; L10-L13 reach chain-length-uniform gaps by other methods. Each `H_p` falls into their setting: on-site gap `14τ`, unique product vacuum, nearest-neighbour terms of norm at most `8|ε|`. None of them was checked for periodic chains with a twisted charge sector, and none compares ground energies of different chains. So this file rebuilds a space-time expansion from scratch (section 4), in a form with a finite polymer set and slots of fixed length. The cross-sector comparison (Theorem B) is new here as far as the fetched abstracts show; that is a report on the works read, not a claim about the literature as a whole. Lemma 4.5 is Dobrushin's inductive argument (L3 through L1 (2.13)), proved in full below.

## 3. Prior work used

| Prior result | Path | Use here |
|---|---|---|
| Prior-work digest | `prior/SGAP0.md` | routes on file, failed attempts, the missed-input pointer to a native sector expansion |
| Definitions 1-6; Theorem 1 (symmetries, `E_χ(ε)=E_χ(−ε)`, Hermitian `T`); Theorem 2 (exact `ε=0` gap `16τ`) | `SGAP.md` lines 13-36 | section 1; consistency check of Theorem A at `ε=0` |
| Theorem 4 (`t=0` split into `2^{L−1}` chains, the 16-level basis, the active rule, `H_ε|K_p=H_p⊗1`) | `SGAP.md` lines 62-68 | the whole model of sections 1, 4, 5 |
| Proposition 4.2 (second order, `2/(7τ)` per wall) | `SGAP.md` lines 76-82; `SMG15.md` Theorem 7 | the value of the pair term in Theorem B, recomputed in the space-time form |
| Proposition 4.3 and the referee closures (G1′), (HF-alt) | `SGAP.md` lines 84-95; `SGAP_REFEREE.md` §3.3 | the target statements; Corollary C follows the same route |
| Corollary 4.4 (even multiplicity at `t=0`) | `SGAP.md` line 97 | scope remark in section 6 |
| A4, A5, A6 and the routes on file | `SGAP.md` lines 139-149; `SMG15.md` §8; `SGAP_REFEREE.md` §5 | section 6 names the new step and why it avoids each failing step |
| Fermionic factorization `T_{x,a}=−i(γ_{x,a}c_x†)(γ_{x+1,a}c_{x+1})+i(γ_{x,a}c_x)(γ_{x+1,a}c_{x+1}†)` (N26) | `SGAP_REFEREE.md` line 99 | Lemma 5.1 uses the equivalent product form `T_{x,a}=(iγ_{x,a}γ_{x+1,a})·hop⁰_x` of `SGAP.md` Definition 3 |
| Atom (`−14` once, `0` eight times odd, `2` seven times even) | `SMG1.md` Theorem 2.2, line 53 | through the on-site energies `0, 14τ, 16τ` |
| Gauss reduction `J: F_even⊗C²→H_G` | `SMG15.md` Theorem 2 | through Theorem 4 of `SGAP.md`, and in Lemma 5.1 (matrix elements in `H_G` equal those in `F_even`) |

**Extended here.** (G1′) is proved in the stronger form "every vector off the vacuum's `(q,ν)` sector" (Theorem A). (HF-alt) is proved with `δ=0` and a quantitative strict margin (Theorem B). `SGAP.md` Proposition 4.3's conclusion then holds unconditionally on the stated range.

**Prior work the digest missed.** None that bears on the proof. The digest's main-branch items were not needed: the clock note's reflection method (`E:351`) would need a reflection structure for the parity chains, and the route below does not use one.

## 4. A space-time polymer representation of each chain

Fix `p`, an integer `n_s≥4`, and `β=n_sδ=n_s/(2τ)`. Write `Z_p(β)=Tr_𝓗 e^{−βH_p}`.

### 4.1 Dyson series

**Lemma 4.1 (Dyson).** Let `A,B` be complex `d×d` matrices with `A` Hermitian and `A≥0`, and `β≥0`. Then

`e^{−β(A+B)} = Σ_{n≥0} (−1)^n ∫_{0<t_1<⋯<t_n<β} e^{−(β−t_n)A} B e^{−(t_n−t_{n−1})A} B ⋯ B e^{−t_1A} dt_1⋯dt_n`,

and the `n`-th term has norm at most `(β‖B‖)^n/n!`.

*Proof.* Put `F(s)=e^{sA}e^{−s(A+B)}` and `B(s)=e^{sA}Be^{−sA}`. Then `F(0)=1` and `F′(s)=−B(s)F(s)`, so `F(s)=1−∫_0^sB(s_1)F(s_1)ds_1`. Substituting this identity into itself `n` times gives `F(β)` as the sum of the terms `k<n` of the series, written with `B(s_1)⋯B(s_k)` over `β>s_1>⋯>s_k>0`, plus a remainder. The remainder is an integral of `B(s_1)⋯B(s_n)F(s_n)` over a simplex of volume `β^n/n!`; its norm is at most `(β sup_s‖B(s)‖)^n sup_s‖F(s)‖/n!`, which tends to `0`. Multiply by `e^{−βA}` on the left: `e^{−βA}B(s_1)⋯B(s_k)=e^{−(β−s_1)A}Be^{−(s_1−s_2)A}B⋯Be^{−s_kA}`. Rename `t_i=s_{k+1−i}`. Since `A≥0`, every `e^{−sA}` with `s≥0` has norm at most `1`, which gives the term bound. `□`

Apply Lemma 4.1 with `A=H_0≥0` and `B=εV`, take the trace in the basis `|χ⟩`, and expand `V=Σ_{x,a}T_{x,a}`. Each `T_{x,a}` sends a basis vector to `ω` times a basis vector, or to `0`. So each term of the expansion is indexed by a starting configuration and a sequence of moves, and is either `0` or a single product.

**Definition 4.1 (history).** A *history* `h` is: an integer `n≥0`; a configuration `χ⁰`; times `0<t_1<⋯<t_n<β`; labels `(x_i,a_i)`. With `χ^i=(χ^{i−1})^{x_i,a_i}` (both `χ_{x_i}` and `χ_{x_i+1}` multiplied by `ρ_{a_i}`), each move `i` must be active on `χ^{i−1}`, and `χ^n=χ⁰`. Its *path* is `χ(t)=χ^i` for `t∈[t_i,t_{i+1})` (`t_0=0`, `t_{n+1}=β`), extended `β`-periodically. Its *weight* is

`wt(h) = (−ε)^n ∏_{i=1}^n ω_i · exp(−∫_0^β H_0(χ(t)) dt)`.

Write `∫dh` for `Σ_nΣ_{χ⁰}Σ_{labels}∫_{0<t_1<⋯<t_n<β}dt`. Lemma 4.1 gives, with absolute convergence,

`Z_p(β) = ∫ wt(h) dh`.  (4.1)

Equivalently, a history is `χ⁰` together with a finite set of labelled jump events `(t,x,a)` with distinct times. Listing the set in increasing time gives the ordered tuple, so `∫dh` is Lebesgue measure on such sets, `n` events at a time, with no factor `1/n!`. Merging two event sets with disjoint times is a bijection onto event sets, and it carries the product of the two measures to the measure of the merged set. This is the only measure fact used below.

### 4.2 Cells, shadows and polymers

**Cells.** Slots are `I_k=[kδ,(k+1)δ)`, `k∈Z_{n_s}`. A *cell* is `(x,k)∈𝒞=Z_L×Z_{n_s}`. Two cells are adjacent if they differ by one step in `x` at equal `k`, or by one step in `k` at equal `x`. Since `L≥8` and `n_s≥4`, every cell has exactly four neighbours.

**Shadow.** For a history `h`, `Sh(h)` is the set of cells `(x,k)` such that `χ_x(t)≠1` for some `t∈I_k`, together with the two cells `(x_i,k),(x_i+1,k)` of every jump `i` with `t_i∈I_k`.

(F1) If `(x,k)∉Sh(h)`, then `χ_x(t)=1` for all `t∈I_k`, and no jump in slot `k` touches `x`.

**Polymers.** A *polymer* is a nonempty connected set of cells; `𝒫` is the set of polymers. `γ≁γ′` (incompatible) means `γ∪γ′` is connected, that is, the two sets meet or contain adjacent cells. `N[γ]={γ′∈𝒫: γ′≁γ}`; it contains `γ`. A family is *compatible* if its members are pairwise compatible. Let `π(γ)={k: (x,k)∈γ for some x}`. A polymer is *winding* if `π(γ)=Z_{n_s}`, and *contractible* otherwise; `𝒫=𝒫^c⊔𝒫^w`. Put `m(γ)=min_k|γ∩(Z_L×{k})|`; `m(γ)=0` for contractible `γ`. The activity of `γ` is

`w(γ) = ∫_{Sh(h)=γ} wt(h) dh`.

For `Q⊂𝒫`, `Z(Q)=Σ_{X⊂Q compatible}∏_{γ∈X}w(γ)`, with `1` for the empty family.

**Lemma 4.2 (factorization).**
(a) Let `h` be a history and `Γ_1,…,Γ_m` the connected components of `Sh(h)`. They form a compatible family of polymers. There are unique histories `h_1,…,h_m` with `Sh(h_j)=Γ_j`, whose jump sets partition the jump set of `h`, with `wt(h)=∏_jwt(h_j)`.
(b) Conversely, for a compatible family `Γ_1,…,Γ_m` and histories `h_j` with `Sh(h_j)=Γ_j` and pairwise distinct jump times, there is exactly one history `h` whose pieces in (a) are the `h_j`.
(c) `Z_p(β)=Z(𝒫)`.
(d) `q` and `ν` are constant along a path. The `(q,ν)` of `h` is the product of the pieces' `q` and the sum of their `ν`. A piece with contractible shadow has `(q,ν)=(1,0)`.

*Proof.* (a) A jump's two cells are adjacent and lie in `Sh(h)`, so each jump lies in exactly one component. Let `h_j` have the jumps of `h` that lie in `Γ_j`, and the path `χ^{(j)}_x(t)=χ_x(t)` if `(x,k(t))∈Γ_j`, and `1` otherwise, where `k(t)` is the slot of `t`. Fix a site `x`. The slots `k` with `(x,k)∈Γ_j` form runs of consecutive slots. If `(x,k)∈Γ_j` and `(x,k−1)∉Γ_j`, then `(x,k−1)∉Sh(h)`, since adjacency would put it in `Γ_j`; by (F1), `χ_x≡1` on `I_{k−1}`. The same holds after the last slot of a run. Hence `χ^{(j)}_x` is piecewise constant, equals `1` at both ends of each run, and changes only at jumps of `h` that touch `x` inside the run; these are jumps of `h_j`. At each jump of `h_j`, both sites carry the values of `h` just before and just after the jump, also when the jump time is a slot boundary (the earlier slot is then either in `Γ_j` or vacuum at that site). So every move of `h_j` is active and has the same `ω`; `ω` depends only on the two site states, because `T_{x,a}` acts on the tensor factor `C^{16}_x⊗C^{16}_{x+1}` (`SGAP_REFEREE.md` N26). The path closes because `h` closes. `Sh(h_j)⊂Γ_j` by construction. Conversely a cell of `Γ_j` lies in `Sh(h)` through an excited time, where `h_j` is excited too, or through a jump, which belongs to `h_j`. The jump factors split among the pieces. The integral `∫H_0` is a sum over sites and slots; vacuum contributes `0`, and each excited pair `(x,t)` lies in exactly one `Γ_j`. So `wt(h)=∏_jwt(h_j)`. Each `h_j` is fixed by `h` and `Γ_j`, so the pieces are unique.
(b) Define the path to be `χ^{(j)}` on the cells of `Γ_j` and `1` elsewhere, and take the union of the jumps. Each move uses two sites inside one `Γ_j`, where the path agrees with `h_j`; so it is active, and the path closes. The shadow is `⋃_jΓ_j`. The `Γ_j` are pairwise disjoint and non-adjacent, so they are exactly its components, and (a) returns the `h_j`.
(c) By (a) and (b), `h↦(h_1,…,h_m)` is a bijection, outside the null set of coinciding jump times, from histories with shadow components `{Γ_1,…,Γ_m}` onto tuples of histories with shadows `Γ_j`. It is measure preserving: the starting configuration of `h` is the superposition of those of the pieces, and the jump measure of a merged event set is the product measure (section 4.1). Weights multiply. Summing over all compatible families gives `Z(𝒫)`, and (4.1) gives `Z_p(β)`.
(d) Constancy is Fact 1.1. At a time `t`, each non-vacuum site `x` lies in the cell `(x,k(t))` of exactly one `Γ_j`, where `h` agrees with `h_j`; vacuum sites contribute trivially. So `q` multiplies and `ν` adds over pieces. If `Γ_j` is contractible, pick `k∉π(Γ_j)`; by (F1) applied to `h_j`, every site is vacuum on `I_k`, so `(q,ν)(h_j)=(1,0)` there, hence always. `□`

**Corollary 4.2′.** If `(q,ν)(χ⁰)≠(1,0)`, some piece of `h` is winding. *Proof.* Lemma 4.2(d). `□`

### 4.3 Activity bounds

Since `|ω|=1`, `w(γ)=Σ_{n≥0}(−ε)^n c_n(γ)` with `c_n(γ)=∫_{Sh(h)=γ, n jumps}∏ω_i e^{−∫H_0}dh`, and `|c_n(γ)|≤C_n(γ)=∫_{Sh(h)=γ, n jumps}e^{−∫H_0}dh`. Put `A_γ(r)=Σ_nC_n(γ)r^n` for `r≥0`, and `w^{(2)}(γ)=ε²c_2(γ)`.

**Lemma 4.3.**
(i) If `u(r)≤1`, then `A_γ(r)≤16^{m(γ)}(2φ(r))^{|γ|}`.
(ii) `C_n(γ)=0` for odd `n`. If `γ` is contractible, `C_0(γ)=0`, and every history with shadow `γ` and exactly two jumps is a *vacuum pair*: two moves at one bond `b` with one flavour, the second undoing the first, and `b` is a wall.
(iii) If `γ` is contractible and `|ε|≤r` with `u(r)≤1`: `|w(γ)|≤(|ε|/r)²(2φ(r))^{|γ|}` and `|w(γ)−w^{(2)}(γ)|≤(|ε|/r)⁴(2φ(r))^{|γ|}`.
(iv) If `u(|ε|)≤1`: `|w(γ)|≤A_γ(|ε|)≤16^{m(γ)}ϑ_ε^{|γ|}`.

*Proof.* (i) *Reference time.* Pick `k*` with `|γ∩(Z_L×{k*})|=m(γ)` and put `t*=k*δ`. A history is fixed by its configuration at `t*` and its event set: apply the moves in cyclic order from `t*`. For a history with shadow `γ`, (F1) makes every site outside `γ`'s slice at `k*` vacuum at `t*`. So at most `16^{m(γ)}` configurations at `t*` occur. *Where jumps sit.* An event at bond `x` in slot `k` puts `(x,k)` and `(x+1,k)` in the shadow, so `(x,k)` lies in `BS(γ)={(x,k): (x,k),(x+1,k)∈γ}`. In each slot, a set `A⊂Z_L` contains both ends of at most `|A|` bonds, so `|BS(γ)|≤|γ|`. *Energy.* Let `J⊂BS(γ)` be the bond-slots that hold at least one event. Call a cell *touched* if it is one of the two cells of an element of `J`. If `(x,k)∈γ` is untouched, no jump in slot `k` touches `x`, so `χ_x` is constant on `I_k`; as `(x,k)` is in the shadow, `χ_x≠1` on all of `I_k`, and `e(χ_x)≥14` gives a factor at most `e^{−14τδ}=v` in `e^{−∫H_0}`. Touched cells give a factor at most `1`, since `H_0≥0`. *Sum.* Drop every other constraint. For a fixed `J`, each bond-slot in `J` carries `n≥1` events with times in `I_k` (ordered volume `δ^n/n!`), `8^n` flavour choices and weight `r` per event; this sums to `e^{8rδ}−1=u(r)`. So

`A_γ(r) ≤ 16^{m(γ)} Σ_{J⊂BS(γ)} u(r)^{|J|} v^{|γ|−#touched(J)}`.

At most `2|J|` cells are touched and `u(r)≤1`, so `u^{|J|}≤(√u)^{#touched(J)}` and each term is at most `φ(r)^{|γ|}`. There are at most `2^{|BS(γ)|}≤2^{|γ|}` sets `J`. This gives (i).
(ii) Let `j_y` be the number of jumps at bond `y` in a closed history. Site `y` is touched `j_{y−1}+j_y` times. Each touch multiplies `χ_y` by an odd character and so reverses `m(χ_y)`. The path closes, so `j_{y−1}+j_y` is even for every `y`. Hence all `j_y` have one parity, and `n=Σ_yj_y` is even because `L` is even. Now let `γ` be contractible and pick `k∉π(γ)`; by (F1) the path is the vacuum on `I_k`. If `n=0`, the path is constant, hence the vacuum, and the shadow is empty, which contradicts `γ≠∅`. If `n=2`, start at a time in `I_k`. The first move acts on the vacuum at some bond `b` with some flavour `a`; it is active only if `1=m(1)m(1)=−p_bp_{b+1}`, so `b` is a wall. It puts `ρ_a` at `b` and `b+1`. The second move must restore the vacuum; a move at bond `b′` changes exactly sites `b′,b′+1`, so `b′=b` and its flavour is `a`.
(iii) By (ii), `A_γ(|ε|)=Σ_{n≥2, even}C_n|ε|^n≤(|ε|/r)²A_γ(r)`, and `|w−w^{(2)}|≤Σ_{n≥4}C_n|ε|^n≤(|ε|/r)⁴A_γ(r)`. Apply (i) with `m(γ)=0`.
(iv) `|w(γ)|≤Σ_n|c_n||ε|^n≤A_γ(|ε|)`, then (i) with `r=|ε|`. `□`

### 4.4 Counting polymers

**Lemma 4.4.** In a graph whose vertices have degree at most `4`, at most `16^{m−1}` connected sets of `m` vertices contain a given vertex `c`. Hence for `0≤y` with `16y<1` and `m_0≥1`:

`Σ_{γ∋c, |γ|≥m_0} y^{|γ|} ≤ (1/16) Σ_{m≥m_0}(16y)^m = (16y)^{m_0}/(16(1−16y))`.

*Proof.* A connected set `S∋c` with `|S|=m` has a spanning tree. A depth-first walk around that tree from `c` back to `c` crosses each tree edge twice, so it has length `2(m−1)`, and its vertex set is `S`. So `S` is determined by a walk of length `2(m−1)` from `c`. There are at most `4^{2(m−1)}=16^{m−1}` such walks. The sum follows. `□`

Every contractible polymer has at least two cells (Lemma 4.3(ii): it has a jump, and a jump has two cells). Every winding polymer has at least `n_s` cells and meets slot `0`.

### 4.5 Dobrushin's inductive lemma

**Lemma 4.5 (after Dobrushin [L3], in the form of [L1] eq. (2.13)).** Let `𝒬̂` be a set with a symmetric relation `≁` such that `γ≁γ` for all `γ`, and write `N[γ]={γ′: γ′≁γ}`. Let `𝒬⊂𝒬̂` be finite, `w: 𝒬→C`, and `μ: 𝒬→[0,∞)` with

(D) `|w(γ)| ∏_{γ′∈𝒬∩N[γ]} (1+μ(γ′)) ≤ μ(γ)` for every `γ∈𝒬`.

For `Q⊂𝒬` let `Z(Q)=Σ_{X⊂Q compatible}∏_{γ∈X}w(γ)`. Then for every `Q⊂𝒬` and every `γ∈𝒬̂`:
(a) `Z(Q)≠0`;
(b) `Z(Q)=Z(Q∖N[γ])·∏_{i=1}^k(1+z_i)`, where `γ_1,…,γ_k` lists `Q∩N[γ]` in any order and `|z_i|≤μ(γ_i)/(1+μ(γ_i))`;
(c) `|Z(Q∖N[γ])/Z(Q)| ≤ ∏_{γ′∈Q∩N[γ]}(1+μ(γ′))` and `|Z(Q∖N[γ])/Z(Q)−1| ≤ ∏_{γ′∈Q∩N[γ]}(1+μ(γ′))−1`.

*Proof.* Induction on `|Q|`. For `Q=∅` all three hold, with `k=0` and both sides equal to `1`. Let `|Q|≥1` and assume (a)-(c) for every proper subset of `Q` and every element of `𝒬̂`. Fix `γ∈𝒬̂` and list `Q∩N[γ]={γ_1,…,γ_k}`. Put `Q_0=Q` and `Q_i=Q_{i−1}∖{γ_i}`, so `Q_k=Q∖N[γ]`. A compatible family in `Q_{i−1}` either avoids `γ_i`, or contains `γ_i` together with a compatible family in `Q_{i−1}∖N[γ_i]=Q_i∖N[γ_i]`. So

`Z(Q_{i−1}) = Z(Q_i) + w(γ_i) Z(Q_i∖N[γ_i])`.

Each `Q_i` with `i≥1` is a proper subset of `Q`. By (a) and (c) for `Q_i` and `γ_i`, `Z(Q_i)≠0` and `|Z(Q_i∖N[γ_i])/Z(Q_i)|≤∏_{γ′∈Q_i∩N[γ_i]}(1+μ(γ′))`. Since `γ_i∉Q_i`, that product omits the factor `1+μ(γ_i)`. So `z_i=w(γ_i)Z(Q_i∖N[γ_i])/Z(Q_i)` satisfies, by (D) divided by `1+μ(γ_i)`,

`|z_i| ≤ μ(γ_i)/(1+μ(γ_i)) < 1`,

and `Z(Q_{i−1})=Z(Q_i)(1+z_i)`. Multiplying over `i` gives (b). If `k≥1`, `Q_k` is a proper subset, so `Z(Q_k)≠0`, and (b) gives `Z(Q)≠0`. If `k=0` for the given `γ`, repeat the argument with any `γ_0∈Q`, for which `k≥1`; this gives (a). For (c): `1/(1+z_i)=1+v_i` with `|v_i|≤|z_i|/(1−|z_i|)≤μ(γ_i)`. Hence `|∏(1+v_i)|≤∏(1+μ(γ_i))` and `|∏(1+v_i)−1|≤∏(1+|v_i|)−1≤∏(1+μ(γ_i))−1`. `□`

**Corollary 4.6 (logarithmic derivative).** `Z(Q)` is affine in each `w(γ)`, `γ∈Q`, with `∂Z(Q)/∂w(γ)=Z(Q∖N[γ])`. Let `s↦w_s` (`s∈[0,1]`) be affine, with (D) for every `s` and one fixed `μ`. Then `s↦Z_s(Q)` is a polynomial with no zero on `[0,1]`. A continuous logarithm `ℓ(s)` of it exists, and

`ℓ(1)−ℓ(0) = ∫_0^1 Σ_{γ∈Q} (w_1(γ)−w_0(γ)) · Z_s(Q∖N[γ])/Z_s(Q) ds`,  `Re(ℓ(1)−ℓ(0)) = log|Z_1(Q)|−log|Z_0(Q)|`.

*Proof.* The deletion identity of the proof above, with `i` replaced by any `γ∈Q`, shows `Z(Q)=Z(Q∖{γ})+w(γ)Z(Q∖N[γ])`, where neither term depends on `w(γ)`. A nonvanishing continuous function on an interval has a continuous logarithm, `ℓ′=Z_s′/Z_s`, and the chain rule gives the integrand. `□`

## 5. Results

### 5.1 Closed histories have the same amplitude in every chain

**Lemma 5.1 (Fock-space identity).** Let `h` be a closed move sequence (a start `χ⁰` and moves `(x_i,a_i)`, `i=1,…,n`, returning to `χ⁰`) in which every bond is used an even number of times. If `h` is active in the chains of two patterns `p` and `p′`, then its amplitude `∏_iω_i` is the same in both chains.

*Proof.* By `SGAP.md` Theorem 4 and `SMG15.md` Theorem 2, the chain vector `|χ⟩` of `K_p` is, up to a phase and the inert `C²` factor, the Fock vector `Φ_p(χ)∈F_even` with mirror line `χ_x` and light occupation `n^p_x(χ_x)=(1−p_xm(χ_x))/2` at each site; matter operators that preserve every site parity have the same matrix elements in `H_G` as in `F_even`. Phases cancel in a closed product, so `∏_iω_i=⟨Φ_p(χ⁰)|T_{x_n,a_n}⋯T_{x_1,a_1}|Φ_p(χ⁰)⟩`. By `SGAP.md` Definition 3, `T_{x,a}=M_{x,a}Λ_x` with `M_{x,a}=iγ_{x,a}γ_{x+1,a}` (even, mirror modes only) and `Λ_x=hop⁰_x` (even, light modes only). Even operators on disjoint sets of modes commute. So `T_{x_n,a_n}⋯T_{x_1,a_1}=MΛ` with `M=M_{x_n,a_n}⋯M_{x_1,a_1}` and `Λ=Λ_{x_n}⋯Λ_{x_1}`. Write `Φ_p(χ)=A_χB_n|0⟩`, where `A_χ` is a fixed polynomial in mirror modes that produces the mirror lines (it does not depend on `p`), `B_n=∏_{x=0}^{L−1}(c_x†)^{n_x}` in increasing `x`, and `n=n^p(χ)`. Then

`⟨Φ|MΛ|Φ⟩ = ⟨0|B_n†(A_χ†MA_χ)ΛB_n|0⟩ = ⟨0|(A_χ†MA_χ)(B_n†ΛB_n)|0⟩`,

because `Λ` is even and commutes with `A_χ`, and `A_χ†MA_χ` is even and commutes with `B_n†`. The vector `B_n†ΛB_n|0⟩` is `κ|0⟩` plus vectors with some light mode occupied, where `κ=⟨n|Λ|n⟩`. The even mirror operator `A_χ†MA_χ` commutes with every light number operator, so it keeps the second part orthogonal to `|0⟩`. Hence `∏_iω_i=⟨0|A_χ†MA_χ|0⟩·⟨n|Λ|n⟩`. The first factor does not depend on `p`. For the second, activity of move `i` means the occupations at `x_i` and `x_i+1` differ (proof of Fact 1.1). On such an occupation vector, `hop⁰_x` swaps the two occupations with sign `+1` if `x≠L−1`: no occupied mode lies between `c_x` and `c_{x+1}` in the order of `B_n`. For the wrap bond `x=L−1` the sign is `(−1)^{N−1}`, the parity of the other occupied modes. So `⟨n|Λ|n⟩=(−1)^{(N−1)j_{L−1}}`, where `j_{L−1}` is the number of moves at the wrap bond. It equals `1` because `j_{L−1}` is even. `□`

**Corollary 5.1′ (local identity of activities).** Let `p≠±p_alt`, so `NW(p)≠∅`. Say `γ∈𝒫^c` *sees* bond `b` if `(b,k),(b+1,k)∈γ` for some `k`. If `γ` sees no bond of `NW(p)`, then `w_p(γ)=w_{p_alt}(γ)`.

*Proof.* Every jump of a history with shadow `γ` sits at a bond that `γ` sees (proof of Lemma 4.3(i)), hence at a wall of both `p` and `p_alt`. At a wall the active rule is `m(χ_x)m(χ_{x+1})=+1` in both chains. So both chains have the same histories with shadow `γ`, and `H_0` is the same. Each such history uses no bond of `NW(p)`, so some bond count is `0`; by the parity argument of Lemma 4.3(ii) all bond counts are even. Lemma 5.1 gives equal amplitudes, hence equal weights and equal activities. `□`

### 5.2 The gas of contractible polymers

Let `|ε|≤R`, so `λ=|ε|/R≤1`. For `γ∈𝒫^c` put `μ(γ)=λ²(ϑe^{1/8})^{|γ|}`. Put `y=16ϑe^{1/8}≤0.2095`, `x_ε=ϑ_εe^{λ²/50}`, and

`ζ = Σ_{γ∈𝒫^w} A_γ(|ε|) e^{|γ|λ²/50}`.

Write `Z^⊥_p(β)=Tr(Π^⊥e^{−βH_p})`, where `Π^⊥` projects onto `𝒱_p^⊥`.

**Lemma 5.2.** For every pattern `p`, allowed `L` and `n_s≥4`:
(a) Every activity vector `w` on `𝒫^c` with `|w(γ)|≤λ²ϑ^{|γ|}` satisfies (D) on `𝒬=𝒫^c` with this `μ`. This holds for `w_p` and `w_{p_alt}`.
(b) For every `γ∈𝒫`: `Σ_{γ′∈𝒫^c∩N[γ]} μ(γ′) ≤ |γ|λ²/50`.
(c) `ζ ≤ L(16x_ε)^{n_s}/(1−32x_ε)`, and `32x_ε≤0.38`.
(d) `|Z_p(β)−Z(𝒫^c)| ≤ |Z(𝒫^c)|(e^ζ−1)` and `|Z^⊥_p(β)| ≤ |Z(𝒫^c)|(e^ζ−1)`, with `Z(𝒫^c)` built from `w_p`.

*Proof.* (b) `γ′≁γ` means that `γ′` meets `γ` or a neighbour of `γ`; at most `5|γ|` cells qualify. Every contractible polymer has at least two cells. By Lemma 4.4 with `m_0=2`, for each cell `c`, `Σ_{γ′∈𝒫^c, γ′∋c}μ(γ′)≤(λ²/16)y²/(1−y)≤0.00347λ²`. Multiply by `5|γ|`: `0.0174|γ|λ²≤|γ|λ²/50`.
(a) Using `1+μ≤e^μ` and (b): `|w(γ)|∏_{γ′∈𝒫^c∩N[γ]}(1+μ(γ′))≤λ²ϑ^{|γ|}e^{|γ|λ²/50}≤λ²ϑ^{|γ|}e^{|γ|/8}=μ(γ)`. For `w_p`, Lemma 4.3(iii) with `r=R` gives `|w_p(γ)|≤λ²ϑ^{|γ|}`; the same for `p_alt`.
(c) A winding polymer meets slot `0`, has `|γ|≥n_s` cells, and has `m(γ)≤|γ|/n_s`, since its `n_s` slices partition it. Lemma 4.3(iv) gives `A_γ(|ε|)e^{|γ|λ²/50}≤(16^{1/n_s}x_ε)^{|γ|}`. Sum over the `L` cells of slot `0` and use Lemma 4.4: `ζ≤L·(1/16)Σ_{m≥n_s}(16^{1+1/n_s}x_ε)^m=L(16x_ε)^{n_s}/(1−16^{1+1/n_s}x_ε)`, and `16^{1/n_s}≤2`. Numerically `32x_ε≤32·0.01155·e^{1/50}≤0.38`.
(d) By Lemma 4.2, `Z_p(β)` is the sum over compatible families. Split a family into its winding members `W` and its contractible members, which form a compatible family inside `𝒫^c∖N[W]`, where `N[W]=⋃_{γ∈W}N[γ]`. So `Z_p(β)=Σ_W∏_{γ∈W}w(γ)·Z(𝒫^c∖N[W])`, the sum over compatible `W⊂𝒫^w`. The term `W=∅` is `Z(𝒫^c)`. For `W={γ_1,…,γ_r}`, apply Lemma 4.5(c) `r` times, with `𝒬=𝒫^c` and `𝒬̂=𝒫`, removing `N[γ_1]`, then `N[γ_2]`, and so on; by (b), `|Z(𝒫^c∖N[W])|≤|Z(𝒫^c)|∏_{j}e^{|γ_j|λ²/50}`. With `|w(γ)|≤A_γ(|ε|)`,
`|Z_p(β)−Z(𝒫^c)| ≤ |Z(𝒫^c)| Σ_{∅≠W⊂𝒫^w}∏_{γ∈W}A_γ(|ε|)e^{|γ|λ²/50} ≤ |Z(𝒫^c)|(e^ζ−1)`.
For `Z^⊥_p`: `Π^⊥` is diagonal in the basis and commutes with `H_p`, so `Z^⊥_p(β)` is the integral of `wt(h)` over histories with `(q,ν)(χ⁰)≠(1,0)`. By Lemma 4.2(d) the condition involves only the winding pieces, and by Corollary 4.2′ it forces `W≠∅`. For fixed `W`, the integral over the pieces with shadows in `W` under that condition has modulus at most `∏_{γ∈W}A_γ(|ε|)`. The same estimate follows. `□`

### 5.3 Theorem A: the gap off the vacuum sector, (G1′)

**Theorem A.** Let `τ>0`, `|ε|≤R=τ/120000`, `L` allowed, and `p` any pattern. Then

`E^⊥_p − e_p ≥ 2τ [ ln(1/(16ϑ_ε)) − λ²/50 ]`.

In particular `E^⊥_p−e_p≥3.3τ` for all `|ε|≤R`, and `E^⊥_p−e_p≥7τ` for `|ε|≤10⁻⁸τ`. The bound does not depend on `L` or `p`.

*Proof.* Take `n_s≥4` and `β=n_s/(2τ)`. By Lemma 5.2(c), `ζ→0` as `n_s→∞`; take `n_s` so large that `ζ≤1/10`. Lemma 5.2(d) gives `Z_p(β)≥|Z(𝒫^c)|(2−e^ζ)≥0.89|Z(𝒫^c)|` and `Z^⊥_p(β)≤|Z(𝒫^c)|(e^ζ−1)≤1.06ζ|Z(𝒫^c)|`. So `Z^⊥_p/Z_p≤1.2ζ`. The trace of `Π^⊥e^{−βH_p}` is at least its largest eigenvalue, so `Z^⊥_p(β)≥e^{−βE^⊥_p}`; and `Z_p(β)≤16^Le^{−βe_p}`. Hence

`e^{−β(E^⊥_p−e_p)} ≤ 16^L · 1.2ζ ≤ 16^L · 1.2L (16x_ε)^{n_s}/(1−32x_ε)`.

Take logarithms and divide by `β=n_s/(2τ)`: `E^⊥_p−e_p ≥ 2τ ln(1/(16x_ε)) − (2τ/n_s)ln(1.2·16^L L/(1−32x_ε))`. Let `n_s→∞` at fixed `L`. With `x_ε=ϑ_εe^{λ²/50}` this is the displayed bound. Numerically: for `|ε|≤R`, `16ϑ_ε≤0.1848` and `λ²/50≤0.02`, giving `2(1.688−0.02)τ≥3.3τ`. For `|ε|≤10⁻⁸τ`, `ϑ_ε=2e^{−7}` (section 1.4) and `λ²≤1.5·10⁻⁶`, giving `2(7−ln 32−3·10⁻⁸)τ≥7.06τ`. `□`

**Corollary A′ ((G1′), proved).** At `t=0`, (G1′) holds with `c₀=1/120000` and `Δ_G=3.3`, and with `Δ_G=7` for `c₀=10⁻⁸`. *Proof.* An `S`-charged vector of `K_p≅𝓗⊗C²` lies in `𝒱_p^⊥⊗C²`, and `H_ε|K_p=H_p⊗1` (section 1.3). `□`

Theorem A says more than (G1′). Every vector of `K_p` with light number `N≠k(p)` also lies at least `3.3τ` above `e_p`. So every ground vector of `H_p` has `q=1` and `N=k(p)`. Theorem A says nothing about the spectrum inside `𝒱_p`; in particular it does not claim that `e_p` is a simple eigenvalue. As a consistency check, at `ε=0` it gives `7.07τ`, below the exact value `14τ` (every vector of `𝒱_p^⊥` has an excited site, and odd sites cost `14τ`).

### 5.4 Theorem B: the alternating chain is lowest, (HF-alt)

**Theorem B.** Let `τ>0`, `|ε|≤2·10⁻¹⁰τ`, and `L` allowed. For every pattern `p`,

`e_p − e_{p_alt} ≥ (L − walls(p)) · ε²/(6τ)`.

In particular `e_{p_alt}=min_pe_p`, so (HF-alt) holds with `δ=0`; and `e_p>e_{p_alt}` for every `p≠±p_alt` when `ε≠0`.

*Proof.* If `p=±p_alt` the right side is `0` and Fact 1.2 gives equality. Let `NW(p)≠∅`. Take `n_s≥4` and `β=n_s/(2τ)`. Both chains act on `𝓗`, with the same `H_0`, the same cells and the same polymers; Lemma 4.3 applies to each. Let `w_0=w_p` and `w_1=w_{p_alt}` on `𝒫^c`, `w_s=(1−s)w_0+sw_1`, `Δw=w_1−w_0`, and `Z_s=Z(𝒫^c)` built from `w_s`. Since `|w_s(γ)|≤max(|w_0(γ)|,|w_1(γ)|)≤λ²ϑ^{|γ|}`, Lemma 5.2(a) gives (D) for every `s` with one `μ`. Corollary 4.6 gives

`log|Z_1| − log|Z_0| = Re ∫_0^1 Σ_{γ∈𝒫^c} Δw(γ) R_s(γ) ds`,  `R_s(γ)=Z_s(𝒫^c∖N[γ])/Z_s(𝒫^c)`.

By Lemma 4.5(c) and Lemma 5.2(b), `|R_s(γ)−1|≤e^{|γ|λ²/50}−1`. Hence

`log|Z_1|−log|Z_0| ≥ Σ_γ Re Δw^{(2)}(γ) − Σ_γ|Δw(γ)−Δw^{(2)}(γ)| − Σ_γ|Δw(γ)|(e^{|γ|λ²/50}−1)`,  (5.1)

where `Δw^{(2)}=w_1^{(2)}−w_0^{(2)}`.

*Main term.* By Lemma 4.3(ii), the two-jump histories with contractible shadow are vacuum pairs at walls. A pair at a wall of both chains has the same weight in both (Lemma 5.1, or directly: both moves have the same two site states). So `Σ_γΔw^{(2)}(γ)` is the total weight of contractible vacuum pairs of the alternating chain at the bonds `b∈NW(p)`. Such a pair, with flavour `a`, is fixed by an arc of the time circle: a start `t∈[0,β)` and a length `s∈(0,β)`, the pair being present on the arc. The two jump times are `t` and `t+s` mod `β`; each unordered pair of times gives two arcs, told apart by `χ⁰`, so the measure is `dt ds`. The weight is `(−ε)²⟨𝟙|T_{b,a}|χ′⟩⟨χ′|T_{b,a}|𝟙⟩e^{−28τs}=ε²e^{−28τs}`: `T_{b,a}` is Hermitian, the move is active on the vacuum at a wall of `p_alt`, and the pair costs `2·14τ`. If `s<β−2δ`, the arc meets at most `n_s−1` slots, so the shadow is contractible. All pair weights are positive. Hence

`Σ_γΔw^{(2)}(γ) ≥ |NW(p)| · 8ε² · β∫_0^{β−2δ}e^{−28τs}ds = |NW(p)| · (2ε²/(7τ)) · β · (1−e^{−28τ(β−2δ)})`.

This is `SGAP.md` Proposition 4.2's `2ε²/(7τ)` per wall, recovered per unit time.

*Error terms.* By Corollary 5.1′, `Δw(γ)≠0` only if `γ` sees some `b∈NW(p)`; choose an anchor cell `(b,k)∈γ` with `(b+1,k)∈γ`. There are `|NW(p)|·n_s` possible anchors. Fix one, `c`. By Lemma 4.3(iii) with `r=R`, `|Δw−Δw^{(2)}|≤2λ⁴ϑ^{|γ|}` and `|Δw|≤2λ²ϑ^{|γ|}`. By Lemma 4.4 with `m_0=2` and `e^z−1≤ze^z`:

`Σ_{γ∋c}2λ⁴ϑ^{|γ|} ≤ (λ⁴/8)(16ϑ)²/(1−16ϑ) ≤ 0.00524λ⁴`,

`Σ_{γ∋c}2λ²ϑ^{|γ|}(e^{|γ|λ²/50}−1) ≤ (λ⁴/25)(1/16)Σ_{m≥2}m(16ϑe^{1/50})^m ≤ 0.00025λ⁴`,

using `16ϑ≤0.1848`, `16ϑe^{1/50}≤0.1886` and `Σ_{m≥2}my^m=y²(2−y)/(1−y)²`. The two error sums in (5.1) are therefore at most `|NW(p)|·n_s·λ⁴/180`.

*Limit.* By Lemma 5.2(d) for each chain, `Z_p(β)` lies between `|Z_0|(2−e^ζ)` and `|Z_0|e^ζ`, and likewise `Z_{p_alt}(β)` with `|Z_1|`. For `ζ≤1/10` both logarithms differ by at most `2ζ`. Also `e_p=−lim_{β→∞}β^{−1}log Z_p(β)`, because `e^{−βe_p}≤Z_p(β)≤16^Le^{−βe_p}`. Divide (5.1) by `β`, use `n_s/β=2τ`, and let `n_s→∞` (`ζ→0` by Lemma 5.2(c)):

`e_p − e_{p_alt} ≥ |NW(p)| · [ 2ε²/(7τ) − τλ⁴/90 ]`.

With `λ=1.2·10⁵|ε|/τ`, `τλ⁴/90=2.304·10^{18}(ε/τ)²·ε²/τ≤0.0922ε²/τ` when `|ε|≤2·10⁻¹⁰τ`. Since `2/7−0.0922≥1/6`, the theorem follows. `□`

### 5.5 Corollary C: S-GAP⁰

**Corollary C (S-GAP⁰).** Put `c₀=2·10⁻¹⁰` and `Δ=7`. For every `τ>0`, every real `ε` with `|ε|≤c₀τ`, every allowed `L` and every `σ∈Ŝ∖{1}`,

`E_σ ≥ E_0 + 7τ`.

Moreover `E_0=E_1=e_{p_alt}`. This is `SGAP.md` Definition 4 with `t=0`, including `ε=0`.

*Proof.* Since `c₀τ≤10⁻⁸τ≤R`, Theorem A holds with the bound `7τ`, and Theorem B holds. By Theorem A every ground vector of `H_{p_alt}` lies in `𝒱_{p_alt}`: `q=1` and `N=k(p_alt)=L/2`. Through `K_{p_alt}≅𝓗⊗C²` it gives a neutral half-filled vector of energy `e_{p_alt}`, so `E_0≤E_1≤e_{p_alt}`. Every `E_χ` is a minimum over subspaces of the blocks `K_p`, so `E_χ≥min_pe_p=e_{p_alt}` by Theorem B; hence `E_0=E_1=e_{p_alt}`. For `σ≠1`, a vector with charge `σ` has `q≠1` and lies in `𝒱_p^⊥⊗C²` inside its block (section 1.3). So `E_σ≥min_pE^⊥_p≥min_p(e_p+7τ)≥e_{p_alt}+7τ=E_0+7τ`. `□`

The route is `SGAP.md` Proposition 4.3 with (G1′) and (HF-alt) in the place of hypotheses. The continuity argument of the referee closure is not needed: Theorem A puts the ground space of `H_{p_alt}` in the neutral, half-filled sector directly. The constants are crude. The exact `ε=0` value is `Δ=16` (`SGAP.md` Theorem 2). The loss to `7` comes from the bound `e(χ)≥14` per excited cell; the tiny `c₀` comes from the per-cell factor `√u(R)` of Lemma 4.3 against the `O(ε²)` pair term in Theorem B. Neither is optimized here.

**Remark C.1 (where the half-filled ground space sits).** For `|ε|≤c₀τ` and `ε≠0`, Theorem B gives `e_p>e_{p_alt}` for `p≠±p_alt`. So every vector of `H_{1/2}` with energy `E_0` lies in `K_{p_alt}⊕K_{−p_alt}`: its site parities alternate. With `SGAP.md` Corollary 4.4 (every level has even multiplicity at `t=0`), this describes the degeneracy at `t=0`; it says nothing about `t≠0`.

## 6. Scope, the attacks on file, and readings

**6.1 The new step against the failures on file.** `SGAP.md` and `SMG15.md` name these failed attacks: A1 (`SGAP.md` Corollary 3.1, a two-sided bound with no sign), A4 (charge removal), A5 (shifted window), A6 (parity sectors), and `SMG15.md` §8 routes 1-3. A grep of `SGAP_DRAFT.md` (`b21cbe0fc`) finds no attacks labelled A2 or A3; this file relates its step to the named ones.

- *A6 failed* at the comparison across sectors: "The elementary estimates are extensive" (`SGAP.md` line 147). **New step:** compare two chains by interpolating their polymer activities (Corollary 4.6). Lemma 5.1 and Corollary 5.1′ make the two activity vectors equal on every polymer that sees no non-wall bond. So the extensive parts cancel exactly, and the difference is a sum of local terms at the non-wall bonds.
- *Route 1, local Schrieffer-Wolff,* failed because "bounding the total remainder by the sum of local norms gives a bound growing with `L`" (`SMG15.md` line 158). No operator remainder is bounded in norm here. Lemma 4.5 bounds ratios of partition functions, and each ratio error is local to one polymer.
- *Route 2, absolute light-linked polymers,* failed through a possible `|z|⁻²` tail of two free light propagators (`SMG15.md` line 159). At `t=0` no light mode hops (`SGAP.md` line 70: "absent at `t=0`"). Every untouched cell of a polymer here pays `e^{−7}` (Lemma 4.3), so the sums converge absolutely.
- *Route 3, Fröhlich-Pizzo on the unsplit reference,* failed because the on-site kernel was two-dimensional (`SMG15.md` line 160). Each `H_p` has a one-dimensional on-site kernel (`SGAP.md` Theorem 4). No published stability theorem is imported; Lemmas 4.1-4.5 are proved here.
- A1, A4 and A5 are not used. In particular `W_odd≤Kw` stays unproved; at `t=0` it is no longer needed.

**6.2 What is not proved here.**
- S-GAP at `t≠0`. Theorem 4 of `SGAP.md` fails there, because `hop_x` changes `P_x`. The light chain is then gapless, and every untouched-cell factor of Lemma 4.3 that came from the on-site gap is lost for light excitations. Nothing here bears on that case.
- (G1) of `SGAP.md` Proposition 4.3, a simple ground eigenvalue of `H_p` with a gap inside `𝒱_p`. It is not needed. At `t=0`, uniqueness on `H_{1/2}` fails anyway (`SGAP.md` Corollary 4.4).
- Good constants. The check in section 7 suggests that Theorem B's conclusion holds at `ε=0.2τ` on a small ring; the proof gives `2·10⁻¹⁰τ`.
- Infinite-volume, GNS or tick statements. S-GAP⁰ is a finite-ring statement (`SGAP.md` line 20); so are Theorems A and B.

**6.3 Readings and the four tests.** This file proposes no reading, specification or definition. Theorems A and B and Corollary C are statements about the frozen finite-ring model of `SGAP.md`. S-GAP⁰ itself was four-tested when it was named (`SGAP.md` line 24). The slot length `δ` and the reference coupling `R` are proof devices. They are not law data, and no statement depends on them except through the explicit numbers. So the four-test check has nothing to act on. Nothing is adopted.

**6.4 Lean-formalizability.** Every step is finite-dimensional linear algebra, a finite sum, an integral over a simplex or a box, or an induction on a finite set. The analytic inputs are: the derivative of a matrix exponential (Lemma 4.1); Fubini and the product structure of Lebesgue measure on event sets (Lemma 4.2(c)); a continuous logarithm of a nonvanishing polynomial on `[0,1]` (Corollary 4.6). No step is computer-assisted. The numerical constants are elementary bounds on `e^x`, `ln` and geometric sums.

## 7. [check] A small ring

**What was run.** Script `/tmp/toe-SGAP0/check2.py`, output `/tmp/toe-SGAP0/out2.txt`. Ring `L=4`, which is **not** an allowed `L`; the check only guides. `τ=1`, `ε∈{0.05, 0.2}`. One site carries five CAR modes in a 32-dimensional Fock space. The generators of `S` are the Majorana products on the supports of `SMG1.md` Lemma 2.1, in increasing order, and `W=−Σ` over the fourteen weight-four group elements. Character lines are joint eigenvectors of the generators. Each `H_p` is assembled in the site-parity basis of `SGAP.md` Theorem 4 from the factorization N26 (`SGAP_REFEREE.md` line 99), by index arithmetic. The space has dimension `16⁴=65536`. Lowest eigenvalues come from sparse `eigsh` on symmetry blocks. Floating point only. Run time 5.8 s; peak resident memory 408 MB; `memory_pressure` showed 57% free before the run.

**Output.** `W` has eigenvalues `−14, 0, 2` with multiplicities `1, 8, 7` per light state, as `SMG1.md` Theorem 2.2 states. Hermiticity error at most `9·10⁻¹⁷`.

| `ε/τ` | `p` | `NW(p)` | `e_p−e_{p_alt}` | `(2ε²/7τ)·NW` | `E^⊥_p−e_p` |
|---|---|---|---|---|---|
| 0.05 | `(+,−,+,−)` | 0 | 0 | 0 | 14.0013 |
| 0.05 | `(+,+,−,−)` | 2 | 1.4286·10⁻³ | 1.4286·10⁻³ | 13.9496 |
| 0.05 | `(+,+,+,+)` | 4 | 2.8574·10⁻³ | 2.8571·10⁻³ | 13.8979 |
| 0.2 | `(+,−,+,−)` | 0 | 0 | 0 | 14.0200 |
| 0.2 | `(+,+,−,−)` | 2 | 2.2855·10⁻² | 2.2857·10⁻² | 13.7953 |
| 0.2 | `(+,+,+,+)` | 4 | 4.5775·10⁻² | 4.5714·10⁻² | 13.5679 |

The pattern `(−,−,+,+)` repeats the `(+,+,−,−)` row. In every row the minimum over the vacuum sector `(q,N)=(1,k(p))` equals `e_p`, since the last column is positive.

**Reading.** The alternating chain is lowest, and the excess matches `2ε²/(7τ)` per non-wall bond to four digits at `ε=0.05τ`; at `ε=0.2τ` the fourth-order part is visible but small. The gap off the vacuum sector is close to `14τ`. This agrees with Theorems A and B and suggests their constants are very pessimistic. It proves nothing, and `L=4` lies outside S-GAP⁰'s quantifiers.

**A breach to record.** A first design (`/tmp/toe-SGAP0/check_sgap0.py`, dense diagonalization of symmetry blocks) was stopped by its 100 s alarm after reaching 1.77 GB resident memory. That is above the 1 GB cap and the one-minute limit. Its memory was not sized before the run. No output of that run is used. The second design above stayed within both limits.

---

## FINISH

**Proved (by hand in this file; no computer-assisted step; not yet distilled or refereed).** All for the frozen `t=0`, zero-electric-coupling ring of `SGAP.md`, conditional on the atom of `SMG1.md` and the Gauss reduction of `SMG15.md`, as `SGAP.md` is.
- Lemma 4.1 (Dyson series); Lemma 4.2 (each history factorizes over the components of its space-time shadow; a history off the vacuum's `(q,ν)` sector has a winding component); Lemma 4.3 (per-cell activity bound, even jump counts, two-jump contractible histories are vacuum pairs at walls); Lemma 4.4 (polymer count `16^{m−1}`); Lemma 4.5 (Dobrushin's inductive lemma, rebuilt) and Corollary 4.6.
- Lemma 5.1: a closed move sequence that uses every bond an even number of times has the same amplitude in every chain where it is active. Corollary 5.1′: the activities of `H_p` and `H_{p_alt}` agree on every contractible polymer that sees no non-wall bond of `p`.
- **Theorem A.** For `|ε|≤τ/120000`, every allowed `L` and every `p`: `E^⊥_p−e_p≥2τ[ln(1/(16ϑ_ε))−λ²/50]≥3.3τ`, and `≥7τ` for `|ε|≤10⁻⁸τ`. Hence (G1′), in the stronger form that every vector off the vacuum's `(q,N)` sector is gapped.
- **Theorem B.** For `|ε|≤2·10⁻¹⁰τ`: `e_p−e_{p_alt}≥(L−walls(p))ε²/(6τ)` for every `p`. Hence (HF-alt) with `δ=0`.
- **Corollary C (S-GAP⁰).** For every `τ>0`, `|ε|≤2·10⁻¹⁰τ`, allowed `L` and `σ≠1`: `E_σ≥E_0+7τ`; also `E_0=E_1=e_{p_alt}`. Remark C.1: for `0<|ε|≤2·10⁻¹⁰τ` every half-filled ground vector lies in `K_{p_alt}⊕K_{−p_alt}`.

**Counterexamples.** None. No counterexample to S-GAP or S-GAP⁰ is known.

**Open by name.**
- S-GAP at `t≠0` (OPEN, unchanged). The method here needs every excitation to be gapped; a hopping light mode is not.
- (G1) inside the vacuum sector `𝒱_p` (a simple ground eigenvalue of `H_p` with a gap): not proved, and not needed for S-GAP⁰.
- Constants. The proof gives `c₀=2·10⁻¹⁰` and `Δ=7`; the exact `ε=0` value is `16`, and the `[check]` suggests the conclusions hold much further out. Sharper constants are an open refinement, not a gap in the proof.
- A4's bound `W_odd≤Kw` (unproved; at `t=0` no longer needed).
- Downstream, unchanged: R1.5-U, R1.5-D, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4.

**What changes downstream.**
- If the distiller and referee confirm it, S-GAP⁰ moves from OPEN to proved on `|ε|≤2·10⁻¹⁰τ`. It would enter `SGAP.md` by a dated amendment. (G1′) and (HF-alt) then stop being hypotheses at `t=0` on that range; `SGAP.md` Proposition 4.3's conclusion holds unconditionally there.
- `SMG15.md` R1.5-D: the `t=0` charged-gap subcase is settled on that range. Generic decoupling at `t≠0` is unchanged.
- The method (a space-time polymer gas with fixed slots, Dobrushin's lemma, and interpolation of activities across sectors) is available to later rungs only where all excitations are gapped. It does not touch a gapless light sector.
- No axiom, law, frozen part, reading or working-set entry changes. Nothing is adopted. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged.
