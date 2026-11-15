lead: anthropic/claude-opus-5-5/max mac-mini-toe-lane
# VC1-5U-odd: the vacuum of L5-U for odd m, pass 1

Written 2026-11-06 by a Claude Opus 5.5 headless lane on the Mac mini, as pass 1 under PR #10138's method: Claude drafts at length and runs to closure, Codex distils, a fresh session referees, then the part is frozen.

**What this file is.** An author-side long draft. It grants no status. It adopts no law, no reading and no definition. It changes no axiom and no working-set entry. `docs/MINIMAL_AXIOMS_2026-06-29.md` is unchanged. "Proved here" means: the argument is written out below and has not yet been distilled or refereed. No numerical check was run, and no step uses one.

**Source revisions read.**

| Ref | Commit |
|---|---|
| `claude/toe-assembly`, the commit the lane brief names | `22dfc60d8` |
| the same checkout at the time of writing (the lead added RCS1 files; none of the files below changed) | `bec8f2606` |

No other branch was read.

**Files read, by line, with the commit of their last change.** This folder: `VC1_5.md` (`bf95fc909`, frozen) lines 1-229 (all; Theorems 2.1, 2.2, 3.1, 5.1, 5.3, 5.5, 6.1, 7.1, VC1-5U-odd at 142-146, LW1-5U-Σc-odd at 148, R1-R4 at 162-221); `LW1_5.md` (`271c868a4`, frozen) lines 1-353 (all; section 2 lines 48-97, the law `L5-U` at 87-93, Theorem U at 136-138, section 6 lines 217-243 with Σ-U at 225-231 and Z-U at 233-235, B1-U at 259-269); `LZ1.md` (`b3f266672`, frozen) lines 1-209 (all; Theorems 3.1-3.3 at 57-77, RC1 at 163-184, RC2 at 186-192); `TOE_ASSEMBLY.md` (`7d2b20d29`) lines 71-91 (working set), 160-200 (sections 3.2-3.3, the four tests), 470-486 (VC1), 655-662 (section 10); `Y2W_DRAFT.md` (`92e03055c`) lines 1-40 and its FINISH (format only). `AGENTS.md` was read for routing.

**Owner guidance applied.** "just keep in mind our axioms may not be right, and we dont need to do some super hard core adversarial reads of them, we can specify if needed". The law `L5-U[m]`, the cell group and the readings E, P, F of `VC1_5.md` are read plainly. Nothing is specified or proposed for adoption.

**Working set used, by name.** PS-1c (cell covariance) and PS-6r (finite links), only through the frozen law `L5-U[m]` of `LW1_5.md` section 2. PS-7r only through its sentence "For the gauged law, the vacuum is the state VC1 builds from this sea". PS-3c, PS-3h5 and PS-4 appear only in one conditional remark (section 5).

**Frozen results used, by name.** `VC1_5.md`: definitions 1-5, Theorems 2.1, 2.2, 3.1(a), 5.1, 5.3, the path computation in the proof of Theorem 6.1, R1, R4. `LW1_5.md`: the law `L5-U`, Theorem U, Z-U, B1-U. `LZ1.md`: RC1(b), (c)(iii), only in a downstream remark. Each is quoted where it is used.

**Inputs from outside the working set.** Standard mathematics, used without a new proof: the spectral theorem for a representation of `C(K)` (`K` compact metrizable) by a projection-valued measure; the Riesz representation theorem; the Radon-Nikodym theorem and its chain rule; Schur orthogonality of characters of a compact group; highest-weight theory of `U(5)` (a highest-weight vector of weight `w` generates an irreducible module of highest weight `w`); `SU(5)` is perfect. Everything else is proved in the text. No citation is load-bearing.

**Literature (owner rule: searched before building).** Searched on 2026-11-06. "Abstract" means the arXiv abstract page was fetched; "text" means the relevant text was fetched and read.

| Work | ID | Fetched | Use here (context only) |
|---|---|---|---|
| Rokhsar, Kivelson, *Superconductivity and the quantum hard-core dimer gas*, PRL 61, 2376 (1988) | not on arXiv | bibliographic record only: **NOT VERIFIED** | origin of RK states |
| Moessner, Sondhi, *An RVB phase in the triangular lattice quantum dimer model* | cond-mat/0007378 | abstract | a gapped short-range RVB phase exists on the triangular lattice (2D, non-bipartite) |
| Hermele, Fisher, Balents, *Pyrochlore photons* | cond-mat/0305401 | abstract (search summary) | 3D U(1) Coulomb phase with a soluble RK point; physics expectation for section 6, attack A4 |
| Castelnovo, Chamon, Mudry, Pujol, *Generalized RK Hamiltonians and the stochastic matrix form* | cond-mat/0502068 | abstract | RK states as square roots of classical weights |
| Chandrasekharan, Wiese, *Quantum link models* | hep-lat/9609042 | abstract | the spin-1/2 U(1) quantum link model that section 3 finds inside `L5-U[m]` |
| Oshikawa, *Commensurability, excitation gap and topology* | cond-mat/9911137 | abstract | LSM filling: needs a gap |
| Hastings, *Lieb-Schultz-Mattis in higher dimensions* | cond-mat/0305505 | abstract | needs a gap |
| Nachtergaele, Sims, *A multi-dimensional LSM theorem* | math-ph/0608046 | abstract | needs a unique ground state |
| Ogata, Tasaki, *LSM type theorems without continuous symmetry* | 1808.08740 | abstract | needs a unique gapped ground state |
| Kobayashi, Shiozaki, Kikuchi, Ryu, *LSM with higher-form symmetry and quantum dimer models* | 1805.05367 | abstract | closest gauge-theory LSM analogue; concerns gapped trivial phases |
| Cheng, Zaletel, Barkeshli, Vishwanath, Bonderson, *Translational symmetry and microscopic constraints on SET phases* | 1511.02263 | abstract (search summary) | crystalline LSM; gapped phases |
| Po, Watanabe, Jian, Zaletel, *Lattice homotopy constraints on phases of quantum magnets* | 1703.06882 | abstract (search summary) | obstructs symmetric short-range-entangled states, not pure states |
| Fannes, Nachtergaele, Werner, *Finitely correlated states on quantum spin chains*, CMP 144, 443 (1992) | not on arXiv | bibliographic record only: **NOT VERIFIED** | purity of injective 1D states; not used |
| Perez-Garcia, Verstraete, Cirac, Wolf, *PEPS as unique ground states of local Hamiltonians* | 0707.2260 | abstract | injectivity gives finite-volume uniqueness; not used |
| Bencs, Hrušková, Tóth, *Factor-of-iid Schreier decorations of lattices in Euclidean spaces* | 2101.12577 | text: Theorem 1.2, Lemma 4.2, Corollary 4.3, proof of Theorem 1.2 (v2, pages 2, 15-17) | attack A3 |
| Bencs, Hrušková, Tóth, *Factor-of-iid balanced orientation of non-amenable graphs* | 2106.12530 | abstract | context for A3 |
| Chandgotia, Sheffield, Wolfram, *Large deviations for the 3D dimer model* | 2304.08468 | search summary only: **NOT VERIFIED** | 3D flow models lack a height function; context for A4 |

Findings. No source found treats purity of an infinite-volume RK state on a gauge-invariant algebra. Every LSM-type theorem found assumes a gap, a unique ground state, short-range entanglement or a split property. Reading P assumes none of these. So no published LSM theorem decides VC1-5U-odd. The equivalence of purity with a classical tail property (Theorem 4.2) is proved here natively. Bencs-Hrušková-Tóth Theorem 1.2 reads (spacing restored from the PDF text extraction): "For every d≥3, there is a finitary Aut(Λd □)-factor of iid which is a.s. a Schreier decoration of Λd □. Moreover, it has almost surely no infinite monochromatic paths." It is the strongest published input toward the classical lemma ICE-T below. It is not rebuilt here, and it does not state the tail property that ICE-T needs (attack A3).

---

## 0. The question, quoted

`VC1_5.md` line 23 fixes the conditions: "(i) stationarity under the tick `α`; (ii) local gauge invariance; (iii) invariance under all the stated cell lifts". Reading **P** "means purity of the restriction to `A^{gauge}`".

`VC1_5.md` line 142: "**VC1-5U-odd (open).** Does an odd-`m` state satisfy (i)–(iii) and P? Its filling must be an integer by Theorem 5.3."

`VC1_5.md` line 146, route 3: "**GAP:** finite-volume purity need not survive a weak-* limit; no proof of invariant-algebra purity is supplied. Symmetry and stationarity of the limit points hold (R4); purity on `A^{gauge}` is not shown."

`VC1_5.md` line 148: "**LW1-5U-Σc-odd (open).** Is there a pure, cell-symmetric all-site singlet for odd `m` with fluctuating end numbers?"

## 0.1 Outcome in one paragraph

**Open, reduced to one classical lemma, after three named attacks on that lemma.** Neither existence nor non-existence of an odd-`m` P-witness is proved. **Proved here:** (1) *Shadow theorem* (Theorem 2.2). If a state's restriction to `A^{gauge}` (or the state itself) is a factor state, the joint law of all matter numbers `N_x` and end numbers `p_{ℓ,z}` is trivial on the tail σ-algebra. This holds for every `m`, all constants and every plaquette class. (2) *Isotype* (Lemma 2.1). A P-witness carries one `U(5)` isotype, the same at every site. (3) *Ice reduction* (sections 3-4). For odd `m`, the empty-matter, highest-weight sector of `L5-U[m]` carries an exact copy of the spin-1/2 U(1) quantum link model on the cubic lattice. Every probability measure `ν` on 3-in-3-out arrow configurations that is quasi-invariant under finite modifications defines a stationary, gauge-invariant RK state `ω_ν`, for all constants of the base tick. It is cell symmetric when `ν` is, and pure on `A^{gauge}` exactly when `ν` is tail-trivial (Theorems 4.1, 4.2). (4) *Consequences* (section 5). The lemma **ICE-T** (a cell-invariant, tail-trivial, quasi-invariant measure on ice configurations) implies VC1-5U-odd for every odd `m`, at fillings 0 and 5. Conversely, a filling-0 or filling-5 P-witness of `L5-U[1]` or `L5-U[9]` yields a cell-invariant tail-trivial ice measure. The route-3 GAP of `VC1_5.md` is exactly the tail-triviality of the corresponding limit of uniform ice measures (Theorem 5.3). **Attacks on ICE-T** (section 6). A1, symmetric deterministic loop covers: refuted; every cell-invariant transition system has only bi-infinite paths (Proposition 6.2). A2, independent random transitions: fails at "every loop is finite". A3, the hierarchical factor of Bencs-Hrušková-Tóth: fails at "resampling a finite set of inputs changes finitely many arrows". **LW1-5U-Σc-odd** stays open; section 7 proves necessary conditions.

---

## 1. Definitions

Notation is that of `VC1_5.md` section 1: `A`, `A^{gauge}`, the gauge average `E`, the tick `α`, the lifts `β_g`, the cell group `G = 2Z^3 ⋊ O_{c0}`. On `L5-U[m]`: end numbers `p_{ℓ,z}`, matter numbers `N_x`, `Q_x = N_x + Σ_{ℓ∋x} p_{ℓ,x}`, Gauss generators `G^T_x`. `Γ_x(u)` is the local unitary that implements `u ∈ U(5)` at `x`; it is generated by the `G^T_x`. A **P-witness** is a state of `A` that satisfies (i)-(iii) and P. `Λ_n = [-n,n]^3 ∩ Z^3`.

**D1 (shadow).** `K_m` is the set of patterns `κ = ((n_x)_x, (p_{ℓ,z})_{ℓ,z})` with `n_x ∈ {0,…,5}`, `max(0,m-5) ≤ p_{ℓ,z} ≤ min(5,m)` and `p_{ℓ,x} + p_{ℓ,y} = m` on every link. It carries the product topology and is compact and metrizable. The **shadow** of a state `ω` is the Borel probability measure `κ_ω` on `K_m` with `∫ f dκ_ω = ω(f(N,p))` for every cylinder function `f`. Here `f(N,p)` is the joint functional calculus of finitely many commuting operators; the Riesz theorem gives `κ_ω`. For a finite site set `Λ`, `F^{out}_Λ` is the σ-algebra generated by `n_x` (`x ∉ Λ`) and by `p_{ℓ,z}` for links `ℓ` with no endpoint in `Λ`. The **tail** σ-algebra is `𝒯 = ∩_n F^{out}_{Λ_n}`. A measure is **tail-trivial** if every event in `𝒯` has measure 0 or 1.

**D2 (ice configurations).** An arrow configuration chooses one end of every link, its **high end**; the arrow points at it. `Ω_ice` is the set of arrow configurations with exactly three high ends among the six links at every site. It is closed in a product of two-point spaces, hence compact and metrizable. `G` acts geometrically: `g·c` has high end `g(h)` on `gℓ` when `c` has high end `h` on `ℓ`. Tail σ-algebra and tail-triviality are as in D1, with the arrows of links that have no endpoint in `Λ_n`.

**D3 (replacements).** Let `L` be a finite link set and `β, β'` arrow configurations on `L`. Put `D(β,β') = {c ∈ Ω_ice : c|_L = β, (β', c|_{L^c}) ∈ Ω_ice}` and `S_{β→β'}(c) = (β', c|_{L^c})`. Then `S_{β→β'}` is a bijection of the clopen set `D(β,β')` onto `D(β',β)` with inverse `S_{β'→β}`. These maps are the **replacements**; there are countably many. A Borel probability measure `ν` on `Ω_ice` is **quasi-invariant** if `ν(B) = 0 ⟺ ν(S(B)) = 0` for every replacement `S` and Borel `B ⊂ dom S`. It is **flip-invariant** if `ν(S(B)) = ν(B)`.

**D4 (the classical lemmas).**
- **ICE-T.** There is a `G`-invariant, quasi-invariant, tail-trivial Borel probability measure on `Ω_ice`.
- **ICE-T⁻.** The same without quasi-invariance.
- **ICE-U.** Some `G`-invariant, flip-invariant Borel probability measure on `Ω_ice` is tail-trivial.
- **ICE-QI.** ICE-T⁻ implies ICE-T.

ICE-U implies ICE-T, which implies ICE-T⁻. Flip-invariant measures are the Gibbs measures of the uniform specification on `Ω_ice`; this remark is not used.

**D5 (transition systems; section 6 only).** A transition system assigns to every site a partition of its six links into three pairs. Following pairs splits the link set into **loops**: closed trails and bi-infinite trails.

**Four-test check.** The four tests are those of `TOE_ASSEMBLY.md` section 3.2. These are mathematical definitions for this file, not readings of the law.

| Item | (1) fixes a target | (2) open-ended | (3) settles physics by premise | (4) unneeded structure or constant | Result |
|---|---|---|---|---|---|
| D1 shadow, tail | no: (i)-(iii) and P stay as in `VC1_5.md` | no: a fixed definition | no | no: a function of the law's own `N_x`, `p_{ℓ,z}` | pass |
| D2 arrows, `Ω_ice`, `G`-action | no | no | no | no: the `G`-action is the lift action on end numbers | pass |
| D3 replacements, quasi-invariance | no | no | no | no | pass |
| D4 ICE-T, ICE-T⁻, ICE-U, ICE-QI | no: each is a question, used only as an explicit hypothesis | no: fixed statements | no: nothing is assumed | no | pass |
| D5 transition systems | no | no | no | no | pass |

None is proposed for adoption.

## 2. Two facts about every P-witness

**Lemma 2.0 (support).** Let `B ∈ A^{gauge}` be local, with matter sites `S_B` and links `L_B`.
(a) `[Q_x, B] = 0` for every `x`, `[Σ_{x∈S_B} N_x, B] = 0`, and `B` is even.
(b) `B` commutes with every even local element of `A` whose matter sites avoid `S_B` and whose links avoid `L_B`; in particular with every such element of `A^{gauge}`.

*Proof.* (a) `Γ_x(e^{iθ}1) = e^{iθQ_x}` is the central `U(1)` of `U(5)_x`. Invariance gives `e^{iθQ_x} B e^{-iθQ_x} = B`; differentiate at `θ = 0` in the finite-dimensional local algebra. Let `V` be a finite site set containing `S_B` and both ends of every link of `L_B`. Then `Σ_{x∈V} Q_x = Σ_{x∈V} N_x + m|L_B| + R`, where `R` is a sum of end numbers of links outside `L_B` and commutes with `B`. So `[Σ_{x∈V} N_x, B] = 0`, and each `N_x` with `x ∉ S_B` commutes with `B`. Matter parity on `S_B` is `exp(iπ Σ_{x∈S_B} N_x)`, so `B` is even. This agrees with `LW1_5.md` Z-U, line 233: "A local operator with definite \(Q_x\) charges has total charge equal to its matter-number change, ... Thus no fermion-odd local operator is invariant under all \(U(5)_x\)." (b) `LW1_5.md` line 33: "Links commute with matter and are ordinary tensor factors." Even matter elements on disjoint site sets commute. ∎

**Lemma 2.1 (one isotype).** For an irreducible representation `λ` of `U(5)`, with character `χ_λ` and dimension `d_λ`, put `P_λ(x) = d_λ ∫_{U(5)} \overline{χ_λ(u)} Γ_x(u) du` (normalized Haar measure).
(a) `P_λ(x)` is the projection onto the `λ`-isotypic part of `u ↦ Γ_x(u)`. Finitely many `λ` occur, and their `P_λ(x)` sum to 1.
(b) `P_λ(x)` is local, lies in `A^{gauge}` and commutes with every element of `A^{gauge}`.
(c) `β_g(P_λ(x)) = P_λ(gx)`.
(d) If `ω` satisfies P, exactly one `λ_x` has `ω(P_{λ_x}(x)) = 1`. If `ω` also satisfies (iii), `λ_x = λ` at every site, and `Q_x` is sharp at the number of boxes `|λ|`.

*Proof.* (a) Schur orthogonality: on an irreducible summand `ρ_η`, `∫ \overline{χ_λ(u)} ρ_η(u) du = δ_{λη}/d_λ`. The star of `x` (its matter and six links) is finite-dimensional. (b) `Γ_x(v) P_λ(x) Γ_x(v)^* = d_λ ∫ \overline{χ_λ(u)} Γ_x(vuv^{-1}) du = P_λ(x)`, because `χ_λ` is a class function and Haar measure is invariant. For `y ≠ x`, `Γ_y(v)` acts on other matter and on other link ends by even operators, so it commutes with `Γ_x(u)`. Every element of `A^{gauge}` commutes with each `Γ_x(u)`, hence with the integral. (c) `VC1_5.md` Theorem 2.2: "The U law has lifts with `c_{x,j}↦d_g(gx)c_{gx,j}` and `r^{ℓ,z}_j↦r^{gℓ,gz}_j` ... They commute with `α`, carry Gauss generators and end numbers to their images". So `β_g(G^T_x) = G^T_{gx}` and `β_g(Γ_x(u)) = Γ_{gx}(u)`. (d) `VC1_5.md` Theorem 3.1(a): "A self-adjoint central element `z` is sharp in every pure state `ψ` of `B`." Apply it on `B = A^{gauge}` to `z = P_λ(x)`; a projection sharp at `q` has `q = q^2`. The values sum to 1. Under (iii), `ω(P_λ(gx)) = ω(β_g(P_λ(x))) = ω(P_λ(x))`, and `G` is site-transitive (`VC1_5.md` Theorem 2.2). On the `λ`-isotypic part, `e^{iθQ_x} = Γ_x(e^{iθ}1)` acts as `e^{iθ|λ|}`. ∎

**Theorem 2.2 (shadow theorem).** Take `L5-U[m]` for any `m`, any constants and any plaquette class; the statement does not involve the tick. Let `ω` be a state of `A`. Suppose that `π_ω(A)''` is a factor, or that the GNS representation of `ω|A^{gauge}` generates a factor. Then the shadow `κ_ω` is tail-trivial.

*Proof.* Let `B` be `A` or `A^{gauge}` accordingly, and `(H, π, Ω)` the GNS triple of `ω|B`. Let `𝒟 ⊂ A^{gauge}` be the commutative C*-algebra generated by all `N_x` and `p_{ℓ,z}`. The map `f ↦ f(N,p)` on cylinder functions extends to an isometric *-isomorphism `C(K_m) → 𝒟`: every finite pattern allowed by the link constraints is a joint eigenvalue, so the operator norm equals the sup norm. The spectral theorem gives a projection-valued measure `P` on the Borel sets of `K_m` with `π(f(N,p)) = ∫ f dP` and values in `π(𝒟)''`. Both `⟨Ω, P(·)Ω⟩` and `κ_ω` represent `f ↦ ω(f(N,p))`, so they agree.

Let `𝒟_n` be generated by `N_x` (`x ∉ Λ_n`) and `p_{ℓ,z}` (`ℓ` with no endpoint in `Λ_n`). Let `pr_n` restrict a pattern to these coordinates, with image `K_n`. The spectral measure `P_n` of `π` on `𝒟_n ≅ C(K_n)` has values in `π(𝒟_n)''`. For each vector `ξ`, `⟨ξ, P_n(·)ξ⟩` and `⟨ξ, P(pr_n^{-1}(·))ξ⟩` represent the same functional on `C(K_n)`; so they agree, and polarization gives `P(pr_n^{-1}(B')) = P_n(B')`. Every event of `F^{out}_{Λ_n}` is some `pr_n^{-1}(B')`. Hence `P(T) ∈ π(𝒟_n)''` for every `T ∈ 𝒯` and every `n`.

Let `Y ∈ B` be local. For large `n`, `𝒟_n` consists of even elements whose support avoids that of `Y`, so `Y` commutes with `𝒟_n` (Lemma 2.0(b) when `B = A^{gauge}`; when `B = A`, `Y` may be odd but `𝒟_n` is even). Thus `π(Y) ∈ π(𝒟_n)' = (π(𝒟_n)'')'`, and `P(T)` commutes with `π(Y)`. Local elements are dense in `B` (for `A^{gauge}`, `VC1_5.md` Theorem 2.1: "Local invariant observables are dense in `A^{gauge}`"). So `P(T) ∈ π(B)'`. Also `P(T) ∈ π(𝒟)'' ⊂ π(B)''`. So `P(T)` is a central projection of a factor, `P(T) ∈ {0,1}`, and `κ_ω(T) = ⟨Ω, P(T)Ω⟩ ∈ {0,1}`. ∎

**Corollary 2.3 (P-witnesses).** Let `ω` satisfy (iii) and P on `L5-U[m]`. Then `κ_ω` is `G`-invariant and tail-trivial, and `κ_ω`-almost surely `n_x + Σ_{ℓ∋x} p_{ℓ,x} = q` at every site, with `q` the integer of `VC1_5.md` Theorem 5.3. Let `m = 1` and `ω(N_x) = 0` (or `ω(N_x) = 5`) at one site, hence, by (iii), at every site. Then, almost surely, `n ≡ 0` (or `n ≡ 5`) and the ends with `p = 1` are the high ends of an ice configuration. The image of `κ_ω` on `Ω_ice` is `G`-invariant and tail-trivial. Neither (i) nor (ii) is used.

*Proof.* P makes the GNS representation of `ω|A^{gauge}` irreducible, so it generates a factor; apply Theorem 2.2. The lifts carry `N_x` and `p_{ℓ,z}` to their images, so cylinder expectations are `G`-invariant. `VC1_5.md` Theorem 5.3: "Then `q_x∈Z` and `ω(N_x)=q_x-3m`. ... Every state pure on `A^{gauge}` is sharp in every `Q_x`". Sharpness gives `ω(Π[Q_x = q]) = 1`, which is the stated almost-sure identity. For `m = 1` every end number is 0 or 1 and each link has exactly one end with `p = 1`. `N_x ≥ 0` with mean 0 gives `n_x = 0` almost surely; then `q = 3`, so three ends at each site have `p = 1`. For full matter `n_x = 5`, `q = 8`, and again three. The arrow on `ℓ` is a function of `p_{ℓ,src}`, so tail events correspond. ∎

## 3. The odd-m ice sector

From here on `m` is odd and `a = (m-1)/2 ∈ {0,…,4}`. Put `w* = (6,…,6,3,0,…,0)`, with `a` entries 6. Write `H^j_x = G^{E_{jj}}_x = n_{x,j} + Σ_{ℓ∋x} r^{ℓ,x†}_j r^{ℓ,x}_j` and, for `j < k`, `E^{jk}_x = G^{E_{jk}}_x`.

**Arrow vectors.** For a link `ℓ = (x,y)` with source `x` and high end `h ∈ {x,y}`, put `p_h = a+1`, `p` of the other end `= a`, and

`|ℓ;h⟩ = r^{ℓ,x†}_1 ⋯ r^{ℓ,x†}_{p_x} r^{ℓ,y†}_1 ⋯ r^{ℓ,y†}_{p_y} |0⟩_ℓ ∈ Λ^m C^{10}`.

Flavours `1,…,p` are occupied at each end, and creators are ordered source end first, as in `VC1_5.md` R4. For a finite site set `V` and an arrow configuration `b` on a finite link set `L`, put `|b⟩_V = |vac⟩_V ⊗ ⊗_{ℓ∈L} |ℓ;b_ℓ⟩`, with empty matter on `V`. Links are tensor factors that commute with matter, so no sign depends on the order of links.

**Lemma 3.1 (weight space).** Let `x ∈ V` and let `L` contain the six links at `x`. A vector `v` of (matter on `V`) ⊗ (links in `L`) satisfies `N_x v = 0` and `H^j_x v = w*_j v` for `j = 1,…,5` if and only if every occupation-basis vector in its expansion has empty matter at `x` and, at `x`, three ends with occupied flavour set `{1,…,a+1}` and three with `{1,…,a}`. Every such basis vector is annihilated by every `E^{jk}_x`, `j < k`.

*Proof.* `N_x` and `H^j_x` are diagonal in the occupation basis, so the equations hold exactly when they hold for each basis vector that occurs. With empty matter, `H^j_x` counts the ends at `x` whose set contains `j`. The value 6 for `j ≤ a` puts `1,…,a` in all six ends. The value 0 for `j > a+1` excludes those flavours. The value 3 for `j = a+1` puts `a+1` in exactly three ends. The converse is the same count. For `j < k`, the matter term of `E^{jk}_x` kills empty matter. An end term `r^{ℓ,x†}_j r^{ℓ,x}_k` needs `k` occupied and `j` empty; occupied sets here are initial segments, so `k` occupied forces `j` occupied. ∎

**Lemma 3.2 (invariant elements on arrow vectors).** Let `B ∈ A^{gauge}` be local, with matter sites `S_B` and links `L_B`, and let `V_B` be `S_B` together with both ends of every link of `L_B`. Let `L` be a finite link set containing every link with an endpoint in `V_B`, and `V ⊇ V_B` a finite site set. Let `b` be an arrow configuration on `L` with three high ends at every site of `V_B`. Then

`B|b⟩_V = Σ_{b'} k_B(b',b) |b'⟩_V`,

summed over arrow configurations `b'` on `L` that agree with `b` off `L_B` and have three high ends at every site of `V_B`. The coefficient `k_B(b',b) = ⟨b'|_V B |b⟩_V` depends only on `b|_{L_B}` and `b'|_{L_B}`.

*Proof.* `B` commutes with `Σ_{x∈S_B} N_x` (Lemma 2.0(a)), which vanishes on `|b⟩_V`; so it vanishes on `B|b⟩_V`. Each `N_x` is nonnegative, so every `N_x`, `x ∈ S_B`, vanishes there; for `x ∈ V ∖ S_B`, `N_x` commutes with `B`. `B` commutes with each `H^j_x`, `x ∈ V_B`, because `H^j_x` generates a one-parameter subgroup of `U(5)_x`. By Lemma 3.1, `|b⟩_V` has weight `w*` at each site of `V_B`, so `B|b⟩_V` has too. Lemma 3.1 at each site of `V_B` puts every occupation-basis vector of `B|b⟩_V` in the stated form at that site. `B` acts as the identity on links outside `L_B` and on matter outside `S_B`. Each link of `L_B` has both ends in `V_B`, so both of its ends have the form `{1,…,a}` or `{1,…,a+1}`; the constraint `p_x + p_y = m = 2a+1` makes exactly one end high. Each such basis vector is `±|b'⟩_V`; the sign enters the coefficient. Write `B = B_0 ⊗ 1` with `B_0` on (matter at `S_B`) ⊗ (links of `L_B`). Then `⟨b'|B|b⟩ = ⟨b'|_{L_B}, vac|B_0|b|_{L_B}, vac⟩ ∏_{ℓ∉L_B}⟨b'_ℓ|b_ℓ⟩`. ∎

**Lemma 3.3 (loop operators).** Let `C = (x_0, ℓ_0, x_1, ℓ_1, …, ℓ_{k-1}, x_k = x_0)` be a closed trail: `ℓ_i` joins `x_i` and `x_{i+1}`, the links are distinct, sites may repeat. Put (with `j_k = j_0`)

`O_C = Σ_{j_0,…,j_{k-1}=1}^{5} ∏_{i=0}^{k-1} r^{ℓ_i,x_i†}_{j_i} r^{ℓ_i,x_{i+1}}_{j_{i+1}}`.

Each factor is a number-preserving bilinear on one link, so it lies in that link's algebra, and factors on different links commute.
(a) `O_C ∈ A^{gauge}`.
(b) Let `b` be an arrow configuration on a link set containing `C`. If every `ℓ_i` has high end `x_{i+1}` in `b` ("`C` is directed in `b`"), then `O_C|b⟩ = σ_C |T_C b⟩`, where `T_C b` reverses the arrows of `C` and `σ_C ∈ {±1}` depends only on `C` and `m`. Otherwise `O_C|b⟩ = 0`.

*Proof.* (a) A gauge transformation `u` at `y` acts on the five rishon modes of each end at `y` by the second-quantized `u`: `r^†_j ↦ Σ_{j'} u_{j'j} r^†_{j'}` and `r_j ↦ Σ_{j'} \overline{u_{j'j}} r_{j'}`. Regroup `O_C` by visits; this uses only that operators on different links commute. The visit `i` to `x_i` contributes `Σ_{j_i} r^{ℓ_i,x_i†}_{j_i} r^{ℓ_{i-1},x_i}_{j_i}`, which unitarity of `u` leaves invariant. Other sites act trivially. (b) Fix one term. On link `ℓ_i` the annihilator acts first, on the original vector of that link. So the creator `r^{ℓ_i,x_i†}_{j_i}` meets an end whose set contains `{1,…,a}`, forcing `j_i ≥ a+1`. The annihilator `r^{ℓ_{i-1},x_i}_{j_i}` meets an end whose set lies in `{1,…,a+1}`, forcing `j_i ≤ a+1`. So only the term with every `j_i = a+1` survives. On `ℓ_i` it is nonzero exactly when the `x_{i+1}`-end contains `a+1` and the `x_i`-end lacks it, that is, when the high end is `x_{i+1}`. It then maps `|ℓ_i;x_{i+1}⟩` to `±|ℓ_i;x_i⟩`. That sign is fixed by the occupation pattern of the link, which depends only on `ℓ_i`, its orientation and `a`. ∎

**Lemma 3.4 (finite modifications).** Let `c, c' ∈ Ω_ice` differ exactly on a finite nonempty link set `D`. Orient each link of `D` toward its high end in `c`. Then every site has equal in- and out-degree in `D`, and `D` is a union of link-disjoint closed trails `C_1,…,C_r`, each directed in `c`. Their choice depends only on `c|_D`. Reversing them one after another stays in `Ω_ice` and ends at `c'`.

*Proof.* At a site `x`, let `d_in` (`d_out`) count the links of `D` at `x` whose high end in `c` is (is not) `x`. In `c'` all of them are reversed. Both configurations have three high ends at `x` and agree off `D`, so `d_in = d_out`. A finite digraph with equal in- and out-degrees is a union of link-disjoint directed closed trails: follow unused out-arcs from any arc; the walk can stop only at its start; remove the trail and repeat. Reversing a directed closed trail swaps one in-arc and one out-arc at each visit. So three high ends persist, and the other trails stay directed. After all reversals every link of `D` is reversed. ∎

By Lemmas 3.2-3.4, `A^{gauge}` acts on arrow vectors by kernels between ice configurations that differ on finitely many links, and the `O_C` act as signed reversals of directed closed trails. This is the gauge-invariant algebra of the spin-1/2 U(1) quantum link model (Chandrasekharan-Wiese, hep-lat/9609042) with `E_ℓ = p_{ℓ,src} - m/2 = ±1/2` and zero background charge. The identification is context only; the proofs use the lemmas.

## 4. RK states and their purity

Let `ν` be a quasi-invariant Borel probability measure on `Ω_ice`.

**Lemma 4.0 (replacement operators).** Let `S = S_{β→β'}: D → D'` be a replacement. Quasi-invariance makes `S_*(ν|_D)` and `ν|_{D'}` mutually absolutely continuous. Let `R_S = dS_*(ν|_D)/dν` on `D'`; it is positive and finite `ν`-a.e. on `D'`. Put `(V_Sψ)(c') = R_S(c')^{1/2} ψ(S^{-1}c')` on `D'` and `0` off `D'`. Then:
(V1) `V_S` is a partial isometry of `L^2(D)` onto `L^2(D')` and vanishes on `L^2(Ω_ice ∖ D)`;
(V2) `V_S^* = V_{S^{-1}}`;
(V3) on one link set `L`, `V_{S_{β'→β''}} V_{S_{β→β'}} = V_{S_{β→β''}} M_{1_{D(β,β')}}`;
(V4) if `L ⊂ L̃`, then `V_{S_{β→β'}} = Σ_γ V_{S_{(β,γ)→(β',γ)}}`, summed over arrow configurations `γ` on `L̃ ∖ L`.

*Proof.* (V1) `∫_{D'} R_S |ψ∘S^{-1}|^2 dν = ∫_D |ψ|^2 dν`; the inverse image of `φ` is `(R_S^{-1/2}φ)∘S`. (V2) Change variables with `R_{S^{-1}}` and use the chain rule `R_{S^{-1}} = (R_S∘S)^{-1}` a.e. on `D`. (V3) `S_{β'→β''}∘S_{β→β'}` is defined exactly on `D(β,β') ∩ D(β,β'')` and agrees there with `S_{β→β''}`; the chain rule multiplies the two derivatives. (V4) `D(β,β')` is the disjoint union of the `D((β,γ),(β',γ))`, on which the maps and their derivatives agree. ∎

**Definition of `Θ`.** For local `B ∈ A^{gauge}`, let `V_B` be as in Lemma 3.2, `L` the set of links with an endpoint in `V_B`, and `k_B(β',β)` the coefficient of Lemma 3.2 for arrow configurations `β, β'` on `L` with three high ends at every site of `V_B`; otherwise `k_B(β',β) = 0`. Put

`Θ(B) = Σ_{β,β'} k_B(β',β) V_{S_{β→β'}}` (a finite sum).

By (V4) and the locality of `k_B`, enlarging `L` does not change `Θ(B)`.

**Theorem 4.1 (RK states).** Let `m` be odd and `ν` quasi-invariant.
(a) `Θ` extends uniquely to a unital *-representation of `A^{gauge}` on `L^2(ν)`.
(b) `ω̂_ν(B) = ⟨1, Θ(B)1⟩` is a state of `A^{gauge}`. `ω_ν = ω̂_ν∘E` is a gauge-invariant state of `A` with `ω_ν|A^{gauge} = ω̂_ν`. So `ω_ν` satisfies (ii).
(c) For all angles `0 ≤ μ < 2ε < π` and every real `τ_E`, `ω_ν` satisfies (i) for the base tick.
(d) If `ν` is `G`-invariant, `ω_ν` satisfies (iii).
(e) `ω_ν(N_x) = 0`; `Q_x` is sharp at `3m`; the isotype of Lemma 2.1 is `w*` at every site; the shadow of `ω_ν` is the image of `ν` under `c ↦ (n ≡ 0, p = a+1 at high ends, p = a at the others)`.
(f) The same holds with fully occupied matter in place of `|vac⟩`: then `N_x = 5`, `Q_x = 5+3m`, and the isotype is `w* + (1,1,1,1,1)`.

*Proof.* (a) For a finite region `R`, `A^{gauge} ∩ A_R` is a finite-dimensional C*-algebra, and the union over `R` is dense in `A^{gauge}` (`VC1_5.md` Theorem 2.1). It suffices that `Θ` is linear, unital, *-preserving and multiplicative on this union; it is then contractive on each `A^{gauge} ∩ A_R` and extends. Linearity is clear. `Θ(1) = Σ_β M_{1_{[c|_L = β]}} = 1`. `k_{B^*}(β,β') = \overline{k_B(β',β)}`, and (V2) gives `Θ(B^*) = Θ(B)^*`. For a product, take one `L` containing every link with an endpoint in `V = V_B ∪ V_{B'}`. By (V3),

`Θ(B)Θ(B') = Σ_{β,β''} Σ_{β'} k_B(β'',β') k_{B'}(β',β) V_{S_{β→β''}} M_{1_{D(β,β')}}`.

At `c ∈ D(β,β'')`, the indicator `1_{D(β,β')}(c)` equals 1 exactly when `β'` has three high ends at every site of `V`. Indeed `k_{B'}(β',β) = 0` unless `β' = β` off `L_{B'}`, sites outside `V` meet no link of `L_{B'}`, and all links at sites of `V` lie in `L`. By Lemma 3.2 applied to `B'` and then to `B`, the inner sum over admissible `β'` is `⟨β''|BB'|β⟩ = k_{BB'}(β'',β)`. So `Θ(B)Θ(B') = Θ(BB')`.
(b) `ω̂_ν(B^*B) = ‖Θ(B)1‖^2 ≥ 0` and `ω̂_ν(1) = 1`. `VC1_5.md` Theorem 2.1: "Restriction gives an affine bijection from gauge-invariant states on `A` to states on `A^{gauge}`, with inverse `φ↦φ∘E`."
(c) `LW1_5.md` line 78: "Cube gates in a layer have disjoint matter and links. Infinite products mean local automorphisms as in LW1 E1." So for local `B` there is a finite product `W` of gates with `α(B) = W^*BW`. Theorem U of `LW1_5.md`, line 136: "every \(\mathcal G_x^T\) commutes with every hop and electric gate". So every gate commutes with every `Γ_x(u)` and lies in `A^{gauge}`. A cube gate is `exp(-ia_eH_C)` or `exp(ia_oH_C)`, with `H_C` a sum of hops on the edges of `C`. Every term of `h^U_ℓ = Σ_{jk} c^†_{y,j}U^{jk}_ℓ c_{x,k} + h.c.` ends with a matter annihilator at a site of `C`. So `H_C|b⟩_V = 0` when `V` contains the sites of `C`, the gate fixes `|b⟩_V`, and `Θ` of it is 1. The electric gate `exp(-iτ_E(p_{ℓ,src} - m/2)^2)` multiplies every `|b⟩_V` by `e^{-iτ_E/4}`, since `|p_{ℓ,src} - m/2| = 1/2`. Hence `Θ(W)` is a phase and `Θ(α(B)) = Θ(W)^*Θ(B)Θ(W) = Θ(B)`. So `ω̂_ν∘α = ω̂_ν`. `VC1_5.md` Theorem 2.1: "The map `E` commutes with `α` and the cell lifts." So `ω_ν∘α = ω̂_ν∘α∘E = ω_ν`. No property of `ν` or of the angles was used.
(d) On a finite region the lift `β_g` is implemented by `W_g = W^{mat}_g ⊗ W^{link}_g`. Here `W^{link}_g` second-quantizes `r^{ℓ,z}_j ↦ r^{gℓ,gz}_j` on each link (`LW1_5.md` B1-U). `W^{mat}_g` implements `c_{x,j} ↦ d_g(gx)c_{gx,j}` as a relabelling followed by parities `exp(iπN_x)`, so it fixes the matter vacuum. Inside each end, `W^{link}_g` keeps the flavour order. If `g` reverses `ℓ`, the two blocks of creators change order, at the cost `(-1)^{p_xp_y} = (-1)^{a(a+1)} = +1`; `VC1_5.md` R4(c) writes this sign as `(-1)^{(m^2-1)/4}`, and `(m^2-1)/4 = a(a+1)` is even. So `W_g|b⟩_V = |g·b⟩_{gV}` and `k_{β_g(B)}(g·β', g·β) = k_B(β',β)`. Put `(U_gψ)(c) = ψ(g^{-1}·c)`. `G`-invariance of `ν` makes `U_g` unitary with `U_g1 = 1`, and gives `U_gV_SU_g^* = V_{gSg^{-1}}` with `gS_{β→β'}g^{-1} = S_{g·β→g·β'}`. Hence `Θ(β_g(B)) = U_gΘ(B)U_g^*` and `ω̂_ν∘β_g = ω̂_ν`. Since `E` commutes with `β_g`, `ω_ν∘β_g = ω_ν`.
(e) `N_x|b⟩_V = 0` and `Q_x|b⟩_V = 3m|b⟩_V`, so `Θ(N_x) = 0` and `Θ((Q_x - 3m)^2) = 0`. By Lemma 3.1, `|b⟩_V` is a highest-weight vector of weight `w*` for `U(5)_x`, so it lies in the `w*`-isotypic part; hence `Θ(P_{w*}(x)) = 1`. `Θ(f(N,p))` is multiplication by `f(0, p(c))`.
(f) With full matter, every hop term contains a matter creator at a site of `C`, so cube gates again act as the identity. Lemma 2.0(a) keeps the matter on `S_B` full, because its total is maximal and conserved. In Lemma 3.1 full matter adds 1 to every flavour count and its raising terms vanish; the rest is unchanged. ∎

**Theorem 4.2 (purity equals tail-triviality).** Let `m` be odd and `ν` quasi-invariant. Then `ω̂_ν` is pure on `A^{gauge}` if and only if `ν` is tail-trivial. In that case `ω_ν` satisfies P and, by R1, F. The same holds for the full-matter twin.

*Proof.* *GNS.* For a cylinder set `[β] = {c : c|_L = β}`, the product `Π_β` of end-number projections `Π[p_{ℓ,h} = a+1]` (`h` the high end of `β` on `ℓ`) lies in `A^{gauge}`; `LW1_5.md` Theorem U: "End numbers commute with the Gauss generators." `Π_β|b⟩_V = [b|_L = β]|b⟩_V`, so `Θ(Π_β) = M_{1_{[β]}}`. Hence `Θ(A^{gauge})1` contains every cylinder simple function. Cylinder sets form an algebra that generates the Borel σ-algebra, so these functions are dense in `L^2(ν)`. Thus `(L^2(ν), Θ, 1)` is the GNS triple of `ω̂_ν`, and `ω̂_ν` is pure exactly when `Θ(A^{gauge})' = C1`.

*Maximal abelian.* Let `T` commute with every `M_{1_{[β]}}`. Then `T` commutes with `M_f` for every `f ∈ C(Ω_ice)`, by norm limits. Put `h = T1`. For continuous `f`, `Tf = TM_f1 = M_fT1 = fh`, so `‖fh‖_2 ≤ ‖T‖‖f‖_2`. Cylinder sets are clopen, and indicators of cylinder sets approximate `1_B` in `L^2(ν)` for any Borel `B`; a subsequence converges a.e. So `∫_B|h|^2dν ≤ ‖T‖^2ν(B)` for all `B`, and `|h| ≤ ‖T‖` a.e. Then `T = M_h` on the dense set `C(Ω_ice)`, hence everywhere.

*Invariance.* Let `M_h` commute with `Θ(A^{gauge})`. For a closed trail `C`, Lemma 3.3 gives `k_{O_C}(β',β) = σ_C` when `β` is directed on `C` and `β' = T_Cβ`, and 0 otherwise. By (V4), `Θ(O_C) = σ_C V_{S_C}`, where `S_C` reverses `C` on the links of `C`. Apply `M_hV_{S_C} = V_{S_C}M_h` to `1_{dom S_C}`: `h R^{1/2} = R^{1/2}(h∘S_C^{-1})` a.e. on `ran S_C`, and `R > 0` there. So `h∘S_C = h` a.e. on `dom S_C`. Let `S = S_{β→β'}` be any replacement and `D_0 = {ℓ : β_ℓ ≠ β'_ℓ}`. By Lemma 3.4, on all of `dom S`, `S` is the composition of the reversals of one fixed list of trails determined by `β|_{D_0}`; every intermediate configuration lies in the domain of the next reversal. Quasi-invariance carries null sets to null sets along the chain. So `h∘S = h` a.e. on `dom S`.

*Tail.* Fix a finite link set `L`. Let `N` be the union, over the finitely many replacements `S` on `L`, of `{c ∈ dom S : h(Sc) ≠ h(c)}` and of its images under replacements; it is null. Off `N`, `h` is constant on the finite fibre `Φ(c) = {(β, c|_{L^c}) ∈ Ω_ice}`, since each point of the fibre is `S(c)` for some replacement with `c ∈ dom S`. The fibre average `H(c) = |Φ(c)|^{-1}Σ_{c''∈Φ(c)}h(c'')` is a measurable function of the arrows off `L`, and `H = h` off `N`. Let `L_n` be the links with an endpoint in `Λ_n`. This gives versions `h_n = h` a.e., each a function of the arrows off `L_n`. For every `k`, `h̃ = limsup_n Re h_n` is a function of the arrows off `L_k`, because the `h_n` with `n ≥ k` are; so it is `𝒯`-measurable, and it equals `Re h` a.e. The same holds for `Im h`. Tail-triviality makes `h` a.e. constant. So `Θ(A^{gauge})' = C1`.

*Converse.* If `ω̂_ν` is pure, `ω_ν` satisfies P. Theorem 2.2 makes its shadow tail-trivial. By Theorem 4.1(e) the shadow is the image of `ν` under an injective map that carries arrows of links off `L_n` to end numbers of links with no endpoint in `Λ_n`; so `ν` is tail-trivial. R1 of `VC1_5.md`: "If `ω|A^{gauge}` is pure, then `π_ω(A)''` is a factor." ∎

**Remark 4.3 (stationarity is free in this sector).** Theorem 4.1(c) uses no property of `ν`. So for odd `m`, at fillings 0 and 5 in the arrow sector, the base tick adds nothing to (ii), (iii) and P. The question there is kinematic.

**Remark 4.4 (plaquette layers).** A plaquette gate class (GA1-P-5, open law data) would act on arrow vectors by trail reversals. Theorem 4.1(c) can then fail. Every statement in sections 4-5 concerns the base tick, as in `VC1_5.md`.

## 5. Consequences for VC1-5U-odd

**Theorem 5.1 (ICE-T suffices).** Suppose ICE-T holds, with measure `ν`. Then for every odd `m ∈ {1,3,5,7,9}`, all angles `0 ≤ μ < 2ε < π` and every real `τ_E`, the base tick of `L5-U[m]` has two P-witnesses: `ω_ν`, with filling 0, `Q_x` sharp at `3m` and isotype `w*`; and its full-matter twin, with filling 5, `Q_x` sharp at `5+3m` and isotype `w* + (1,1,1,1,1)`. Both are factor states. They are distinct.

*Proof.* Theorems 4.1 and 4.2. `N_x` separates them. ∎

The fillings are integers, as `VC1_5.md` Theorem 5.3 requires.

**Theorem 5.2 (ICE-T⁻ is necessary at the edges).** Let `m ∈ {1, 9}`. If `L5-U[m]`, for some constants and any plaquette class, has a state with (iii), P and filling 0 or 5, then ICE-T⁻ holds. Neither (i) nor (ii) is needed.

*Proof.* For `m = 1` this is Corollary 2.3. For `m = 9` the end numbers are 4 or 5 and each link has one end of each. Filling 0 gives `q = 27 = 6·4 + 3`, so three ends at each site have `p = 5`; filling 5 gives `q = 32` and the same count. Repeat the proof of Corollary 2.3 with "high end" meaning `p = 5`. ∎

For other odd `m` at filling 0 or 5, the same proof gives a `G`-invariant, tail-trivial measure on divergence-free flows `E_ℓ = p_{ℓ,src} - m/2 ∈ Z + 1/2` with `|E_ℓ| ≤ min(m, 10-m)/2`. At fillings 1-4 the shadow may carry charges, and no reduction is made here.

**Theorem 5.3 (the route-3 GAP, restated exactly).** Let `ω` be a local weak-* limit point of the states `ω_L` of `VC1_5.md` R4 along a subsequence, and let `ν` be its arrow law on `Ω_ice`. Then `ν` is `G`-invariant and flip-invariant, `ω|A^{gauge} = ω̂_ν`, and `ω∘E` is pure on `A^{gauge}` if and only if `ν` is tail-trivial. If `ν` is not tail-trivial, `ω|A^{gauge}` is not even a factor state.

*Proof.* R4 defines `𝒞_L` as the ice assignments of the even box `Λ_L` with, among other conditions, "the net flux through each coordinate plane is zero. (Orient each link from its low end to its high end; the flux through a plane normal to `e_j` is the signed number of links crossing it.)", and `Ψ_L` as the equal-amplitude sum of the `|c⟩`, `c ∈ 𝒞_L`.

*Step 1.* Fix a local `B ∈ A^{gauge}` and take `L` large. Lemma 3.2 is local, so it holds in the box. For `c ∈ 𝒞_L`, `B|c⟩ = Σ_{c'} k_B(c',c)|c'⟩`, where each `c'` is an ice assignment of the box differing from `c` only on `L_B`. By Lemma 3.4, also local, `c'` arises from `c` by reversing directed closed trails inside a ball that does not wrap the box. Each such trail lifts to a closed trail of `Z^3`, which crosses each coordinate plane equally often in both directions. So no plane flux changes, and `c' ∈ 𝒞_L`.

*Step 2.* So `ω_L(B) = |𝒞_L|^{-1}Σ_{c,c'∈𝒞_L}⟨c'|B|c⟩ = ∫F_B dν_L`, with `ν_L` uniform on `𝒞_L` and `F_B(c) = Σ_{β'} k_B(β', c|_L)[(β', c|_{L^c}) has three high ends at every site]` a cylinder function, the same in the box and on `Z^3` once `L` is large. By Step 1, every replacement on a link set inside such a ball maps `D(β,β') ∩ 𝒞_L` bijectively onto `D(β',β) ∩ 𝒞_L`, so `ν_L(S(B')) = ν_L(B')` for cylinder sets `B' ⊂ dom S`.

*Step 3.* Along the subsequence, `ν([β]) = ω(Π_β) = lim ν_L([β])` defines `ν`, and `ω(B) = ∫F_B dν`. The identity `ν(S(B')) = ν(B')` passes to the limit for cylinder sets and then to all Borel sets in the clopen `dom S`. R4(d): "every local weak-* limit point `ω` of `(ω_L)` satisfies (i) and (iii)"; so `ν` is `G`-invariant.

*Step 4.* With `R_S ≡ 1`, `Θ(B)1 = Σ_{β,β'}k_B(β',β)1_{D(β',β)}`, so `ω̂_ν(B) = Σ k_B(β',β)ν(D(β',β))`. Also `∫F_B dν = Σ k_B(β',β)ν(D(β,β'))`. Flip-invariance gives `ν(D(β',β)) = ν(D(β,β'))`. So `ω|A^{gauge} = ω̂_ν = (ω∘E)|A^{gauge}`. Theorem 4.2 and Theorem 2.2 finish the proof. ∎

So the GAP of route 3 is exactly ICE-U for the limit `ν`. Symmetry and stationarity come free (R4, Theorem 4.1); only tail-triviality is missing.

**Remark 5.4 (records, conditional).** `VC1_5.md` Corollary 5.6 states: "Under PS-3c, PS-4, proposed PS-3h5 and the joint Born identification, with the witness as the initial state, these empty and full matter witnesses form records of value 0 and 5 respectively at all sites at tick 1." Its proof uses only that site numbers are sharp and equal at every tick. Theorem 4.1(c),(e) give this for `ω_ν` and its twin. So, under the same readings and ICE-T, they form records of values 0 and 5. This is not used.

**Remark 5.5 (LZ1 bookkeeping).** `LZ1.md` RC1(c)(iii): "On `L5-U[m]`, the conclusion of (ii) holds for every locally gauge-invariant, stationary, cell-invariant state in which some `𝒢^T_x` with traceless `T` has `ω((𝒢^T_x)²)>0`." In `ω_ν` the isotype `w*` is not a character. Summing `ω((𝒢^{T_a}_x)^2)` over an orthonormal basis `T_a` of `su(5)` gives the quadratic Casimir of `V_{w*}`, which is positive. So some traceless generator has positive second moment, and `ω_ν` lies in that class.

## 6. The lemma ICE-T and three attacks

ICE-T asks for a `G`-invariant, quasi-invariant, tail-trivial probability measure on 3-in-3-out arrow configurations of `Z^3`. By Theorem 5.1 it would settle VC1-5U-odd positively. Each attack below aims at it.

**Lemma 6.1 (resampling criterion).** Let `ξ = (ξ_i)_{i∈I}` be independent random variables on a countable set `I`, and `Y = F(ξ)` a measurable map into `Ω_ice`. Suppose that for every finite `J ⊂ I` the following holds: if `ξ'` agrees with `ξ` off `J` and `ξ'|_J` is an independent copy of `ξ|_J`, then `Y(ξ)` and `Y(ξ')` differ on finitely many links almost surely. Then the law of `Y` is tail-trivial.

*Proof.* Let `T` be a tail event. Two configurations that differ on finitely many links lie both in `T` or both outside it, since `T` is determined by the arrows off `L_n` for every `n`. So `1_T(Y(ξ)) = 1_T(Y(ξ'))` a.s. `Y(ξ')` is a function of `(ξ'|_J, ξ|_{I∖J})`, which is independent of `ξ|_J`. Hence `P(Y ∈ T | ξ|_J) = P(Y(ξ') ∈ T | ξ|_J) = P(Y ∈ T)` a.s. So `{Y ∈ T}` is independent of `σ(ξ|_J)` for every finite `J`, hence of `σ(ξ)`, which contains it. Then `P(Y ∈ T) = P(Y ∈ T)^2`. ∎

**Attack A1: symmetric deterministic loop covers. Refuted.**

**Proposition 6.2.** (a) Every `G`-invariant transition system pairs, at each site, each even-cube link with an odd-cube link, in one of the patterns `{a_i, b_{i+k}}` of `VC1_5.md` Theorem 6.1. All its loops are bi-infinite trails. (b) Orient each loop of such a system by an independent fair coin. The resulting measure on `Ω_ice` is `G`-invariant and not tail-trivial.

*Proof.* (a) `VC1_5.md` Theorem 2.2: "a site stabilizer is cyclic of order 3 and cycles the three even-cube edges and the three odd-cube edges separately." A `G`-invariant system has a stabilizer-invariant pairing at every site. Let the generator act by `a_i ↦ a_{i+1}`, `b_i ↦ b_{i+1}`. A pairing of the six links has at most one pair inside `{a_1,a_2,a_3}`, and the 3-cycle moves every 2-subset of a 3-set; so an invariant pairing has no such pair, and likewise none inside `{b_i}`. So the pairs are `{a_i, b_{σ(i)}}` with `σ` commuting with the 3-cycle, that is, `σ(i) = i + k`. Following pairs is the walk computed in the proof of `VC1_5.md` Theorem 6.1: "Either `k=0` everywhere, giving straight lines, or the two sublattices alternate between `1` and `2`." In the second case, "The last entry and incoming link are the translates of the initial entry and incoming link by `T=(2,2,-2)` or `(2,-2,2)`. Since `T∈2Z^3`, the component repeats indefinitely. Site transitivity and the site stabilizer take this component to every other component, so all are bi-infinite paths." The system is `G`-invariant, so the walk repeats with drift `T ≠ 0` and never closes. (b) `G` permutes the loops and preserves the product of fair coins. Fix a loop `γ`. Almost surely its arrows all point forward or all backward along `γ`. The event "`c` points forward along `γ` on all but finitely many links of `γ`" is a tail event, since `γ` has infinitely many links off every `L_n`. It has probability `1/2`. ∎

The failing step is "every loop is finite". It is false for every `G`-invariant system. This is the transition-system form of the path case of `VC1_5.md` Theorem 6.1.

**Attack A2: independent random transitions. Fails at loop finiteness.** Let each site choose its pairing independently, from a law on the 15 pairings that is invariant under its stabilizer, transported to all sites by `G`, with full support. Give every link an independent fair arrow `d_ℓ` and an independent uniform label. Orient each finite loop along `d_{ℓ*}`, where `ℓ*` is its link of largest label. Proved here: the law is `G`-invariant, because the rule commutes with `G`. Given the pairings, loop orientations are independent and fair. If every loop is finite almost surely, the arrow law is tail-trivial: resampling the inputs on a finite set changes only the loops through that set, before and after, which are finitely many finite loops; Lemma 6.1 applies. **Failing step: "every loop is finite almost surely."** Following pairs is a walk in a random environment that is reused on every return. In three dimensions nothing here shows that it closes. A stabilizer-invariant law concentrated near one pairing concentrates near the patterns of Proposition 6.2, whose loops are infinite. Quasi-invariance of this law is also not checked.

**Attack A3: the hierarchical factor of Bencs-Hrušková-Tóth. Fails at finite change.** arXiv:2101.12577 Theorem 1.2 reads (spacing restored from the PDF text extraction): "For every d≥3, there is a finitary Aut(Λd □)-factor of iid which is a.s. a Schreier decoration of Λd □. Moreover, it has almost surely no infinite monochromatic paths." The same page states: "Every Schreier decoration gives a balanced orientation by forgetting the colours." A balanced orientation of `Z^3` is a point of `Ω_ice`. `G` acts on `Z^3` by graph automorphisms, so the law is `G`-invariant. The proof ends: "let each monochromatic cycle randomly choose one of the two strong orientations for itself." Tail-triviality would follow from Lemma 6.1 if resampling finitely many inputs changed finitely many arrows. The paper proves a finitary coding: each output is a.s. determined by the inputs in a finite random ball. It does not state the finite-change property. Its hierarchy uses independent maximal `r_i`-discrete sets (proof of Lemma 4.2: "Generating Ci independently of each other using the above construction") and the toasts of its reference [16, Theorem 5.5], which the text does not reproduce. A resampled input can change `C_i` near itself for every `i`. **Failing step: "finite change under finite resampling" for this hierarchy.** It is not decided here, and the construction is not rebuilt here. Quasi-invariance is also not addressed.

**A fourth remark: the uniform measure (ICE-U).** The natural candidate is an R4 limit (Theorem 5.3). Hermele-Fisher-Balents (cond-mat/0305401, abstract) describe the analogous 3D Coulomb phase and its soluble RK point by Gaussian QED. One expects power-law arrow correlations there. Tail-triviality would follow from a decay estimate for the influence of boundary conditions under the uniform specification on `Ω_ice`. No such estimate is proved here. Three-dimensional flow models have no height function (Chandgotia-Sheffield-Wolfram, 2304.08468, NOT VERIFIED). The physics expectation is not used.

## 7. LW1-5U-Σc-odd

**Proposition 7.1.** Let `m` be odd and `ψ` a pure state of `A` invariant under every local gauge automorphism and every cell lift.
(a) `ψ` satisfies (ii), (iii) and P.
(b) There is one integer `k` with `ψ(Γ_x(u)) = det(u)^k` for all `x` and `u`. The isotype is the character `det^k`, `Q_x` is sharp at `5k`, and the filling is `5k - 3m`: it is 2, 1, 0 or 5, 4, 3 for `m = 1, 3, 5, 7, 9`.
(c) The shadow `κ_ψ` is `G`-invariant and tail-trivial.
(d) For `m = 5`, `N_x` is sharp at 0 or at 5, and `κ_ψ`-almost surely the flow `E_ℓ = p_{ℓ,src} - 5/2` is divergence-free.
(e) No RK state `ω_ν` of section 4 is of this kind.

*Proof.* (a) A pure state is extreme among all states, hence among gauge-invariant ones. `VC1_5.md` Theorem 2.1: "For a gauge-invariant state, P is equivalent to extremality among all gauge-invariant states." (b) In the irreducible GNS representation, `ψ∘Ad Γ_x(u) = ψ` means that `π(Γ_x(u))Ω` defines the same state as `Ω`. The map `π(A)Ω ↦ π(A)π(Γ_x(u))Ω` is then isometric and commutes with `π(A)`, so it is a scalar; hence `π(Γ_x(u))Ω = χ(u)Ω` with `χ` a continuous character of `U(5)`. `SU(5)` is perfect and `U(5)/SU(5) ≅ U(1)` via `det`, so `χ = det^k`. Then `ψ(P_λ(x)) = d_λ∫\overline{χ_λ}det^k du` is 1 for `λ = det^k` and 0 otherwise. `ψ(e^{iθQ_x}) = e^{5ikθ}` for all `θ`, so `Q_x` is sharp at `5k`. Lemma 2.1(c) and site transitivity make `k` constant. `VC1_5.md` Theorem 5.3 gives filling `5k - 3m ∈ [0,5]`; the listed values are the multiples of 5 in `[3m, 3m+5]`, minus `3m`. They agree with Σ-U's list in `LW1_5.md`, line 227: "n_m=2,4,1,3,0\text{ or }5,2,4,1,3." (entries for `m = 1, …, 9`). (c) Corollary 2.3. (d) `VC1_5.md` Theorem 5.1: "both mean end numbers are `m/2`". For `q = 15`, `N_x = 15 - Σ_{ℓ∋x}p_{ℓ,x} ≥ 0` almost surely and the mean of the sum is 15; so the sum is 15 a.s., `N_x = 0`, and the divergence of `E` at `x` is `Σ_{ℓ∋x}p_{ℓ,x} - 15 = 0`. For `q = 20` the same argument gives `N_x = 5`. (e) `w*` has unequal entries, so it is not a character. ∎

So a Σc-odd state lives in the `SU(5)`-singlet sector. For `m = 5` its shadow is a cell-invariant, tail-trivial measure on divergence-free half-integer flows; for `m ∈ {1,3,7,9}` the matter may fluctuate. In the singlet sector the multiplicity of the singlet per local flow pattern exceeds one in general, so section 4's construction does not transfer. **LW1-5U-Σc-odd stays open.** Its classical part, a cell-invariant tail-trivial flow measure, is implied by ICE-T for `m = 5`: an ice configuration is such a flow.

## 8. What was checked

No numerical check was run; no step uses one. Every quoted line was copied from the file named, at the commit given in the head. The literature claims rest on the fetched pages listed in the head; items marked NOT VERIFIED carry no weight. The standard theorems named in the head (spectral theorem, Riesz, Radon-Nikodym with its chain rule, Schur orthogonality, highest-weight theory of `U(5)` in Theorem 4.1(e)) are not reproved.

---

## FINISH

**Proved here (pass 1, not distilled or refereed).**
- Lemma 2.0: local gauge-invariant elements conserve the matter number of their support, are even, and commute when supports are disjoint.
- Lemma 2.1: a P-witness has one `U(5)` isotype `λ`, the same at every site, with `Q_x` sharp at `|λ|`.
- Theorem 2.2 (shadow theorem): if `ω` or `ω|A^{gauge}` is a factor state, the joint law of all `N_x` and `p_{ℓ,z}` is tail-trivial. Any `m`, any constants, any plaquette class.
- Corollary 2.3: the shadow of a P-witness is cell-invariant, tail-trivial and obeys the sharp Gauss law; for `m = 1` at filling 0 or 5 it is an ice measure.
- Lemmas 3.1-3.4: for odd `m`, the empty-matter, highest-weight sector carries the spin-1/2 U(1) quantum link algebra; loop operators reverse directed closed trails; finite modifications are trail reversals.
- Theorem 4.1: every quasi-invariant measure `ν` on `Ω_ice` gives a gauge-invariant state `ω_ν`, stationary for all constants of the base tick, cell-invariant when `ν` is, with filling 0, `Q_x = 3m` and isotype `w*`; and a full-matter twin with filling 5.
- Theorem 4.2: `ω_ν` is pure on `A^{gauge}` if and only if `ν` is tail-trivial.
- Theorem 5.1: ICE-T implies VC1-5U-odd for every odd `m`, all constants, at fillings 0 and 5.
- Theorem 5.2: for `m ∈ {1,9}`, a state with (iii), P and filling 0 or 5 implies ICE-T⁻.
- Theorem 5.3: the route-3 GAP of `VC1_5.md` holds for an R4 limit point exactly when its arrow law is tail-trivial; otherwise that limit is not even a factor state on `A^{gauge}`.
- Lemma 6.1 (resampling criterion for tail-triviality) and Proposition 6.2 (attack A1).
- Proposition 7.1: necessary conditions for LW1-5U-Σc-odd.

**Counterexamples.** Proposition 6.2: no measure built from a cell-invariant deterministic transition system with independent loop orientations is tail-trivial; every loop of such a system is a bi-infinite trail. No frozen claim is contradicted.

**Open by name.**
- **VC1-5U-odd.** Open. It follows from ICE-T (Theorem 5.1). At `m ∈ {1,9}` and fillings 0 or 5 it implies ICE-T⁻ (Theorem 5.2). Fillings 1-4 are not reduced.
- **ICE-T.** Open after three named attacks: A1 (refuted at "every loop is finite", Proposition 6.2); A2 (fails at "every loop of an independent random transition system is finite"); A3 (fails at "resampling finitely many inputs of the Bencs-Hrušková-Tóth hierarchy changes finitely many arrows").
- **ICE-U** for the R4 limits: the route-3 GAP, now stated exactly (Theorem 5.3). The uniform-measure remark of section 6 fails at a three-dimensional decay-of-influence estimate.
- **ICE-QI**: whether ICE-T⁻ implies ICE-T.
- **LW1-5U-Σc-odd.** Open; Proposition 7.1 gives necessary conditions.
- Unchanged: P-existence with a plaquette class on both laws; the PS-7r sea continuation of VC1; VC1-i; TM1-i; LW1-5U-PS7 (owner); LW1-5-BG; LW1-5-X; GA1-P-5; LW1-5-RQ (owner).

**What changes downstream.**
- VC1 on `L5-U` for odd `m`, fillings 0 and 5: in the highest-weight arrow sector, purity is equivalent to a classical tail property, and the base tick costs nothing (Remark 4.3, Theorem 4.2). Existence follows from ICE-T; at `m ∈ {1,9}` it requires ICE-T⁻. Other isotypes at `m ∈ {3,5,7}` are not treated.
- Every future P-witness on `L5-U`, for any `m`, constants or plaquette class, must have one isotype and a tail-trivial, cell-invariant shadow (Lemma 2.1, Corollary 2.3). This is a test for any candidate vacuum, including a continuation of the PS-7r sea.
- LZ1: under ICE-T, `ω_ν` lies in the class of RC1(c)(iii) (Remark 5.5).
- TM1, conditional on PS-3c, PS-4, proposed PS-3h5 and the joint Born identification: under ICE-T, `ω_ν` and its twin form records of values 0 and 5 (Remark 5.4).
- No law, reading, axiom or working-set entry changes. Both laws stay live. Nothing is adopted.
