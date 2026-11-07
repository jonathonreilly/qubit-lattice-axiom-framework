# SGAP0: the zero-hop charged gap

**Status.** In the finite-ring model and conditional on the frozen atom and Gauss reduction, the arguments below give (G1′), (HF-alt), and S-GAP⁰ for the stated constants. This is pass 2, not a referee or audit verdict. **GAP corrected:** the draft calls every contractible polymer at least two cells. Singletons are contractible polymers; their activities vanish. The proof below excludes these zero-activity polymers from the gas. S-GAP at nonzero hopping, (G1) inside the vacuum sector, and the downstream items listed in §7 remain open. The small-ring calculation is a reported check, not proof.

**Provenance.** Pass 1: Claude Opus 5.5, max, `SGAP0_DRAFT.md`. Pass 2: Codex `gpt-6.1-terra`, effort and session id: see run log. SHA-256: draft `71ee2dd593e9b067ea8333603f5c83641e286668f2234f4df723fef788dc93ca`; digest `77815dd273e0378093b01e3448ed974cbc5182a0f3c25e08f1854bfae3cd5435`; `SGAP.md` `be026f7cc7afcdfcb59c98473debee4ac7f9f600bea6ae92ff23d4fc845bdc91`; `SMG15.md` `b65cf2e1b52ff83b756e355b1293e54754da89be4bfa4db3bbd0502573b6a995`; `SMG1.md` `1e5a05a66d0b11016d18264351321165979d569cd84ad213e1dc4072cb021622`; `LW1.md` `78280bd620800eac671ddf6047d42e94c2ecf919d2f938909cc5595b168c09b9`; `TOE_ASSEMBLY.md` `0cdb4965d1df7fa279cad98c1be9bb5654043d01f677434df1e5f05f1ef32ee0`. Historical source revisions are those recorded in the draft; they were not refreshed with git. No scratch calculation was reproduced; `/tmp/toe-SGAP0` was unavailable.

## 1. Definitions inferred by the distiller

These definitions fix the scope and notation. They add no axiom or adopted physical reading.

1. Let `L∈4N`, `L≥8`, `τ>0`, `ε∈R`, `t=0`, and electric coupling zero. Use the atom, characters `Ŝ`, odd characters `ρ_a` (`a=1,…,8`), parity `m(χ)`, Gauss space, charge and light number of `SGAP.md` Definitions 1–6. In particular `ρ_a²=1`, `m(ρ_a)=−1`, and the `ρ_a` are distinct.
2. A pattern is `p∈{±1}^{Z_L}` with `∏p_x=1`. A bond `x=(x,x+1)` is a wall if `p_xp_{x+1}=−1`; `NW(p)` is the set of other bonds, and `walls(p)=L−|NW(p)|`. Write `p_alt` for either alternating pattern and `k(p)=#{x:p_x=−1}`. Both alternating patterns are allowed.
3. By `SGAP.md` Theorem 4, the block `K_p` is `𝓗⊗C²`, where `𝓗=⊗_x C^{16}` has basis `|χ⟩=⊗_x|χ_x⟩`, and the second factor is inert. On `𝓗`, `H_p=H_0+ε∑_{x,a}T^p_{x,a}`, with `H_0=τ∑_x e(χ_x)`, where `e(1)=0`, `e(χ)=14` for odd `χ` and `e(χ)=16` for nontrivial even `χ`. A move on bond `x` multiplies both endpoint characters by `ρ_a`. It is active exactly when `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`. Its matrix element has modulus one; `T^p_{x,a}` is Hermitian and acts on the two ordinary site factors, including at the wrap bond. The exact atom and reduction are in `SMG1.md` Theorem 2.2 and `SMG15.md` Theorem 2.
4. Set `n_x(χ_x)=(1−p_xm(χ_x))/2`, `N=∑n_x`, `q=∏χ_x`, and `ν=N−k(p)`. The product vacuum has `(q,ν)=(1,0)`. Let `𝒱_p` be the span of basis vectors with these labels, `e_p=min spec H_p`, and `E_p^⊥=min spec(H_p|𝒱_p^⊥)`. Let `E_σ` be the bottom of the charge-`σ`, half-filled block of the full Hamiltonian and `E_0=min_σ E_σ`.
5. **S-GAP⁰** asks for `c₀,Δ>0`, independent of `L,τ,ε`, such that `E_σ≥E_0+Δτ` for every allowed `L`, `τ>0`, `|ε|≤c₀τ` and `σ≠1`. It includes `ε=0` and is not a GNS or tick claim. **(G1′)** asks for a uniform positive gap above `e_p` for charged vectors of every `K_p`, at any light number. **(HF-alt)** asks for `e_{p_alt}−min_p e_p≤δτ` with a uniform `δ` smaller than the sector gap.
6. For the proof use slot length `d=1/(2τ)`, reference coupling `R=τ/120000`, `λ=|ε|/R`, `v=e^{-7}`, `u(r)=e^{4r/τ}−1`, `φ(r)=max(√u(r),v)`, `θ_r=2φ(r)` and `θ=θ_R`. Thus `θ≤0.01155`, `16θ≤0.1848`; for `|ε|≤10⁻⁸τ`, `θ_|ε|=2e^{-7}`.

**Proposed readings, not adopted.** `SMG15.md` §1 proposes R15-SPEC, with referee checks `C,P,P,C`; the finite-ring/canonical-sector bridge makes test 4 conditional. R-COR is proposed as a correlation diagnostic; its pass-1 checks were `C,P,C,P`, but `SGAP.md` records that after SMG1-GAP it fails test 3 as a reading of “gapped”. S-GAP⁰ is a named subcase, not a new reading; its recorded four checks pass. The diagnostic `ε²/(τ|t|)` is proposed only for nonzero `t` and is undefined here. Neither this note nor these proof devices adopt a reading.

## 2. Starting facts

**Theorem 1 (conserved labels and translation).** In every chain, `q` and `N` commute with `H_p`. Also `e_{−p_alt}=e_{p_alt}`.

*Proof.* A move multiplies `q` by `ρ_a²=1`. It flips both endpoint occupations. The active rule says those occupations differ, so their sum stays one. A cyclic shift of all matter modes and link registers is unitarily implemented on the finite algebra, preserves Gauss's law and the Hamiltonian, and sends `p_alt` to `−p_alt`. Hence the two blocks have equal spectra. `□`

The exact zero-coupling statement is already proved in `SGAP.md` Theorem 2: at `t=ε=0`, `E_1=0` and `E_σ=16τ` for each allowed nontrivial charge. The second-order coefficient below is already proved in `SMG15.md` Theorem 7 and `SGAP.md` Proposition 4.2: `−2ε² walls(p)/(7τ)`. The implication from a sector gap and filling comparison is already in `SGAP.md` Proposition 4.3 and its (G1′)/(HF-alt) closures.

## 3. Histories and polymer activities

Fix `p`, an integer `n_s≥4`, and `β=n_s d`. Divide the time circle into slots `I_k=[kd,(k+1)d)`, `k∈Z_{n_s}`. Cells `(x,k)` form the graph `Z_L×Z_{n_s}` with nearest-neighbour edges. Its degree is four.

A **history** consists of a starting character configuration, finitely many distinct ordered times and bond/flavour labels, all moves active, with the final configuration equal to the initial one. Its path is piecewise constant and periodic. Write `ω_i` for its move amplitudes and

`wt(h)=(-ε)^n (∏_i ω_i) exp[-∫_0^β H_0(χ(t))dt]`.

The history measure sums over initial configurations and labels and integrates the ordered times. Its **shadow** contains each cell in which a site is excited at some time and both endpoint cells of every jump in that slot. Outside the shadow the site is vacuum throughout the slot and no jump touches it. A **polymer** is a nonempty connected cell set. Polymers are incompatible when they meet or have adjacent cells; `N[γ]` is the set incompatible with `γ`, including itself. They are **contractible** if they miss a time slot, **winding** otherwise. Let `m(γ)` be the minimum number of cells in one time slice. The activity `w_p(γ)` is the integral of `wt(h)` over histories with exactly that shadow. `A_γ(r)` is the corresponding sum of absolute weights with `|ε|` replaced by `r` and all `|ω_i|` replaced by one. Write `w_p^{(2)}` for the two-jump contribution.

**Theorem 2 (Dyson expansion and factorization).** `Tr e^{-βH_p}` is the sum over compatible families of polymers of the product of their activities. Charge multiplies and `ν` adds over history components. Every contractible component has labels `(1,0)`. Thus a history with different labels has a winding component.

*Proof.* For matrices `A≥0`, `B`, the Dyson series follows by iterating `F'(s)=−e^{sA}Be^{-sA}F(s)` for `F(s)=e^{sA}e^{-s(A+B)}`. The `n`th term has norm at most `(β‖B‖)^n/n!`; hence the expansion is absolutely convergent. Applying it to `H_0` and `ε∑T` and taking the trace gives the history integral.

Each jump's endpoint cells lie in one shadow component. Restrict the path to one component and put the vacuum elsewhere. At the ends of each run of cells at a site, the adjacent outside cell is vacuum; hence the restricted path closes and uses precisely the jumps of that component. A move amplitude depends only on its two site factors, by the site-even factorization in `SGAP.md` Theorem 4, so amplitudes and the on-site energy weight factorize. Conversely, compatible component histories have disjoint, nonadjacent shadows; merging their jump sets gives one history. Coincident jump times form a null set, and the event-set measure is the product measure. This proves the partition-function identity. The labels compose because vacuum sites contribute `1` to `q` and `0` to `ν`. A contractible component is vacuum in a missing slot and has those labels there and hence at all times, by Theorem 1. `□`

**Theorem 3 (activity and counting bounds).** If `u(r)≤1`, then

`A_γ(r)≤16^{m(γ)}(2φ(r))^{|γ|}`.

Every closed history has an even number of jumps. A contractible history with nonempty shadow has at least two; with exactly two it is a vacuum pair at one wall, with one flavour and the second move undoing the first. Consequently, for contractible `γ` and `|ε|≤r`,

`|w_p(γ)|≤(|ε|/r)²(2φ(r))^{|γ|}`,  `|w_p(γ)−w_p^{(2)}(γ)|≤(|ε|/r)⁴(2φ(r))^{|γ|}`.

A singleton contractible polymer has zero activity. In a degree-four graph at most `16^{m−1}` connected `m`-cell sets contain a fixed cell.

*Proof.* Choose a time at a slice of minimal occupancy. At most `16^{m(γ)}` initial configurations occur. A jump in a bond-slot requires both endpoint cells in `γ`; there are at most `|γ|` such bond-slots. For a chosen set `J` of occupied bond-slots, summing its events and eight flavours costs `u(r)` per slot. Every untouched shadow cell is excited for its entire slot and costs at most `v`. At most `2|J|` cells are touched. Drop all other constraints and sum over `J`: the result is bounded by `16^{m(γ)}2^{|γ|}φ(r)^{|γ|}`.

Let `j_x` count jumps on bond `x`. Closure forces `j_{x−1}+j_x` even at each site, since each touch flips parity. Thus all `j_x` have the same parity; `L` is even, so their sum is even. A contractible history is vacuum in a missing slot. Zero jumps then gives empty shadow. With two jumps the first creates two odd characters from vacuum, hence is active only at a wall; closure forces the same bond and flavour for the second. The displayed bounds follow by extracting at least two or four powers of `|ε|/r`. Every jump touches two distinct cells, so a contractible singleton has no history. Finally, a connected `m`-cell set has a spanning tree and is the range of a depth-first walk of `2(m−1)` steps from the chosen cell. There are at most `4^{2(m−1)}=16^{m−1}` walks. `□`

**GAP in pass 1, corrected.** After its Lemma 4.4, the draft says every contractible *polymer* has at least two cells. A singleton is a counterexample to that set-theoretic statement. It has zero activity by Theorem 3. Below `𝒬` contains only contractible polymers with at least two cells. Removing the zero-activity singletons leaves every partition function unchanged and restores the lower limit `m=2` in all sums. Winding polymers have at least `n_s≥4` cells.

## 4. Finite polymer-gas estimates

For a finite set `Q` of polymers with a symmetric, reflexive incompatibility relation, put `Z(Q)=∑_{X⊂Q compatible}∏_{γ∈X}w(γ)`.

**Theorem 4 (Dobrushin induction).** Suppose nonnegative `μ(γ)` obey

`|w(γ)|∏_{γ'∈Q∩N[γ]}(1+μ(γ'))≤μ(γ)`.

For every `S⊂Q`, `Z(S)≠0`. For any polymer `γ`,

`|Z(S\N[γ])/Z(S)|≤∏_{γ'∈S∩N[γ]}(1+μ(γ'))`,

and the modulus of this ratio minus one is at most that product minus one. If `w_s` varies affinely on `[0,1]` with the same bound, then

`log|Z_1(Q)|−log|Z_0(Q)|=Re ∫_0^1∑_{γ∈Q}(w_1−w_0)(γ) Z_s(Q\N[γ])/Z_s(Q) ds`.

*Proof.* Induct on `|S|`. Remove the members `γ_i` of `S∩N[γ]` one by one, writing `S_i=S_{i−1}\{γ_i}`. The deletion identity gives `Z(S_{i−1})=Z(S_i)(1+z_i)` with `z_i=w(γ_i)Z(S_i\N[γ_i])/Z(S_i)`. The induction and the hypothesis give `|z_i|≤μ(γ_i)/(1+μ(γ_i))<1`; the missing self-factor matters here. Products prove nonvanishing. Writing `(1+z_i)^{-1}=1+v_i` gives `|v_i|≤μ(γ_i)` and both ratio bounds. The deletion identity also gives `∂Z/∂w(γ)=Z(Q\N[γ])`; differentiate a continuous logarithm of the nonvanishing polynomial `Z_s` and take real parts. `□`

This is the finite induction credited in the draft to Dobrushin, via Fernández–Procacci, arXiv:math-ph/0605041, Eq. (2.13). The proof above is the input; no published theorem is imported.

**Theorem 5 (uniform gas bounds).** Let `|ε|≤R`, `𝒬` be all contractible polymers of size at least two, `μ(γ)=λ²(θe^{1/8})^{|γ|}`, `x=θ_|ε| e^{λ²/50}` and

`ζ=∑_{γ winding} A_γ(|ε|)e^{|γ|λ²/50}`.

Then for every polymer `γ`, `∑_{γ'∈𝒬∩N[γ]}μ(γ')≤|γ|λ²/50`; the hypothesis of Theorem 4 holds for any activities bounded by `λ²θ^{|γ|}`. Also

`ζ≤L(16x)^{n_s}/(1−32x)`,  `32x≤0.38`.

With `Z_c=Z(𝒬)` for the activities of `p` and `Z_p^⊥=Tr(Π_p^⊥e^{-βH_p})`,

`|Z_p−Z_c|≤|Z_c|(e^ζ−1)`,  `|Z_p^⊥|≤|Z_c|(e^ζ−1)`.

*Proof.* A polymer incompatible with `γ` meets `γ` or one of its neighbours, at most `5|γ|` cells. Put `y=16θe^{1/8}≤0.2095`. Theorem 3 bounds the sum of `μ` over polymers containing one cell by `(λ²/16)y²/(1−y)≤0.00347λ²`. Multiplication by five gives less than `λ²/50` per cell of `γ`. Thus `∏(1+μ)≤e^{|γ|λ²/50}≤e^{|γ|/8}`, which proves the criterion. Theorem 3 gives the required activity bound for both `p` and `p_alt`.

A winding polymer meets slot zero, has `|γ|≥n_s` and `m(γ)≤|γ|/n_s`. Theorem 3 and the count give the bound on `ζ`, using `16^{1/n_s}≤2`. Split each compatible family into winding and contractible members. Repeated application of Theorem 4 bounds the ratio after excluding all neighbours of the winding members by `∏_γ e^{|γ|λ²/50}`. Sum their absolute activities and drop compatibility to obtain `e^ζ−1`. For the projected trace, Theorem 2 makes the label constraint depend only on winding pieces and forces at least one; absolute integration gives the same bound. `□`

## 5. Sector gap

**Theorem 6 (Theorem A; (G1′)).** For `|ε|≤R`, every allowed `L` and every pattern `p`,

`E_p^⊥−e_p≥2τ[log(1/(16θ_|ε|))−λ²/50]≥3.3τ`.

For `|ε|≤10⁻⁸τ` the gap is at least `7τ`. Thus (G1′) holds with these respective constants, for every light number.

*Proof.* Fix `L` and let `n_s→∞`. Theorem 5 gives `ζ→0`; for `ζ≤0.1`, `Z_p^⊥/Z_p≤1.2ζ`. Since `Z_p^⊥≥e^{-βE_p^⊥}` and `Z_p≤16^L e^{-βe_p}`,

`e^{-β(E_p^⊥−e_p)}≤1.2·16^L L (16x)^{n_s}/(1−32x)`.

Take logarithms, divide by `β=n_s/(2τ)`, and take the limit. The first numerical bound follows from `16θ≤0.1848` and `λ²/50≤0.02`. For the second, `θ_|ε|=2e^{-7}` and `λ²≤1.44·10⁻⁶`, so the right side exceeds `7τ`. A charged vector lies in `𝒱_p^⊥`; the inert `C²` factor changes no energy. `□`

Every ground vector of `H_p` therefore lies in `𝒱_p`. This does not prove a gap or simplicity within `𝒱_p`. At `ε=0` the bound is below the exact `14τ` cost of leaving `𝒱_p`.

## 6. Comparison of parity chains

**Theorem 7 (closed-history identity).** If a closed move sequence is active in two patterns and uses every bond an even number of times, its product of move amplitudes is the same in both chains. Consequently, if `p≠±p_alt`, then for a contractible polymer `γ` that sees no bond of `NW(p)`, `w_p(γ)=w_{p_alt}(γ)`. Here `γ` sees `b` when both endpoint cells of `b` occur in the same slot.

*Proof.* The Gauss reduction of `SMG15.md` Theorem 2 identifies the closed product with a Fock-space matrix element; choice of phases for the one-site character vectors cancels. Write `T_{x,a}=M_{x,a}Λ_x`, where `M=iγ_{x,a}γ_{x+1,a}` uses mirror modes and `Λ=hop_x⁰` uses light modes. These even operators commute across the two mode sets. A fixed mirror-line vector and a light occupation vector therefore factor the closed matrix element into a mirror part, independent of `p`, and a light part.

Every active light hop exchanges different occupations. In increasing-site Fock order its sign is `+1` on non-wrap bonds and `(-1)^{N−1}` on the wrap bond. `N` is conserved and the wrap bond occurs an even number of times, so the light product is `+1` in either pattern. This proves the first statement.

If `p≠±p_alt` and `γ` sees no non-wall bond of `p`, all its jumps are at walls in both patterns. The active rules and on-site energies agree there. The parity argument in Theorem 3 says all bond counts have the same parity; a non-wall bond is unused, so all counts are even. The first statement makes corresponding history weights equal. `□`

**Theorem 8 (Theorem B; (HF-alt)).** For `|ε|≤2·10⁻¹⁰τ` and every allowed `L` and `p`,

`e_p−e_{p_alt}≥|NW(p)| ε²/(6τ)`.

Thus `e_{p_alt}=min_p e_p` and (HF-alt) holds with `δ=0`. For nonzero `ε` the inequality is strict unless `p=±p_alt`.

*Proof.* The alternating patterns have equal energy by Theorem 1. Otherwise interpolate the contractible activities: `w_s=(1−s)w_p+sw_{p_alt}`, `0≤s≤1`, and put `Δw=w_{p_alt}−w_p`. Theorem 5 supplies one Dobrushin bound for every `s`. By Theorem 4,

`log|Z_1|−log|Z_0| ≥ ∑_γ Re Δw^{(2)}(γ) − ∑_γ|Δw−Δw^{(2)}|(γ) − ∑_γ|Δw(γ)|(e^{|γ|λ²/50}−1)`.

The two-jump histories are vacuum pairs. On a common wall their weights agree. For each non-wall `b` of `p`, the alternating chain has eight pair flavours. Each pair is specified by a start time `t` and an occupied arc length `s` around the time circle. Its weight is `ε²e^{-28τs}`. If `s<β−2d` its shadow misses a slot. Hence

`∑_γ Δw^{(2)}(γ) ≥ |NW(p)| β (2ε²/(7τ))(1−e^{-28τ(β−2d)})`.

For either error sum, Theorem 7 restricts `γ` to polymers seeing some `b∈NW(p)`. Anchor one such polymer at `(b,k)`; there are at most `|NW(p)|n_s` anchors. For each anchor Theorems 3 and 4 give

`∑_{γ∋(b,k)} |Δw−Δw^{(2)}| ≤ (λ⁴/8)(16θ)²/(1−16θ) ≤ 0.00524λ⁴`,

`∑_{γ∋(b,k)} |Δw|(e^{|γ|λ²/50}−1) ≤ (λ⁴/400)∑_{m≥2}m(16θe^{1/50})^m ≤ 0.00025λ⁴`.

The first estimate uses the factor two for the two chains. The second uses `e^z−1≤ze^z` and the degree-four count. Their sum is at most `λ⁴/180` per anchor.

Theorem 5 bounds the difference between `log Z_p` and `log|Z_0|`, and likewise for `p_alt`, by a quantity tending to zero as `n_s→∞` at fixed `L`. Divide the displayed inequality by `β` and use `−β^{-1}log Tr e^{-βH_p}→e_p`. Since `n_s/β=2τ`,

`e_p−e_{p_alt}≥|NW(p)|[2ε²/(7τ)−τλ⁴/90]`.

For `|ε|≤2·10⁻¹⁰τ`, `τλ⁴/90≤0.0922 ε²/τ`, and `2/7−0.0922≥1/6`. The two alternating patterns alone have no non-wall bonds. `□`

**Theorem 9 (Corollary C; S-GAP⁰).** For `c₀=2·10⁻¹⁰`, `Δ=7`, every `τ>0`, `|ε|≤c₀τ`, allowed `L` and nontrivial `σ`,

`E_σ≥E_0+7τ`,  `E_0=E_1=e_{p_alt}`.

For `ε≠0` in this range every half-filled ground vector lies in `K_{p_alt}⊕K_{−p_alt}`.

*Proof.* Theorem 6 puts every ground vector of `H_{p_alt}` in the neutral vacuum-label sector. As `k(p_alt)=L/2`, it gives a neutral half-filled ground vector at energy `e_{p_alt}`. Theorem 8 says no block has lower energy; hence `E_0=E_1=e_{p_alt}`. Every charged vector belongs to the complement of `𝒱_p` in its block, so Theorem 6 gives `E_σ≥min_p e_p+7τ`. The final assertion follows from the strict part of Theorem 8. `□`

This proves a finite-ring subcase of the chirality target, conditional on the supplied model and prior results. It does not establish the 3+1-dimensional target in `TOE_ASSEMBLY.md`. `SGAP.md` Corollary 4.4 already proves even multiplicity at `t=0`; the above does not determine the full degeneracy.

## 7. Scope, checks, and open items

The new comparison cancels activities away from non-wall bonds before estimating errors. It addresses A6's extensive comparison, rather than using its false per-sector half-filled claim. The ratio estimates also avoid the global remainder norm in `SMG15.md` §8 route 1. Route 2's moving-light tail is absent at `t=0`; route 3's two-dimensional unsplit on-site kernel is absent after fixing `p`. These observations do not prove the corresponding nonzero-hopping results. A1, A4 and A5 are not used; A5's strict window assertion is false as recorded in `SGAP.md`.

**Open by name.** S-GAP at `t≠0`; (G1), a simple ground eigenvalue and a gap within `𝒱_p`; sharper constants; A4's uniform `W_odd≤Kw`; R1.5-U, R1.5-D beyond this zero-hop charged-gap subcase, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4. Infinite-volume, GNS and tick statements are not established. The finite-ring bounds do not establish the light-sector replacement or a physical axiom. The inferred definitions are mathematical notation, not proposed physical readings.

**Arithmetic check.** A local floating-point evaluation gives the neighbour coefficient `0.0173232<1/50`, the two per-anchor error coefficients `0.00523368` and `0.000244314` with sum below `1/180`, and the general gap coefficient `3.33746>3.3`. This checks numerical margins only.

**Recorded check, not reproduced.** Pass 1 reports sparse floating-point diagonalization at `L=4`, outside the allowed domain, with `τ=1` and `ε=0.05,0.2`. It reports alternating sectors lowest, energy excesses close to `2ε²|NW|/(7τ)`, and gaps off `𝒱_p` between `13.5679τ` and `14.0200τ`. It reports Hermiticity error at most `9·10⁻¹⁷`. This neither proves the uniform claim nor checks an allowed ring. Its first dense design was stopped after exceeding the stated 1 GB and one-minute limits; its output was not used. Its second reported run stayed within them. The scripts and outputs were unavailable here.

**Prior and literature scope.** `prior/SGAP0.md` records the already-proved exact slice, reduction, second-order term and conditional implications cited above. It also identifies the distinct three-state-clock reflection comparison in `ref/main/docs/THREE_STATE_CLOCK_ENDPOINT_REFLECTION_SECTOR_ENERGY_AND_GROUND_DEFECT_BOUND_BOUNDED_THEOREM_NOTE_2026-09-15.md`, the conditional SU(3) gap application in `ref/main/docs/GAUGE_WILSON_ELECTRIC_DOMINATED_VOLUME_UNIFORM_GAP_BOUNDED_THEOREM_NOTE_2026-09-07.md`, and the different free-ring comparator in `ref/main/docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md`. Their hypotheses do not by themselves establish this comparison. The digest reports these main-branch items unaudited; they were not independently re-read here.

Pass 1 records a literature search in `SGAP0_DRAFT.md` §2, including Fernández–Procacci, Dobrushin, Kotecký–Preiss, Borgs–Kotecký–Ueltschi, Yarotsky and Fröhlich–Pizzo. The draft reports several abstract-only checks and marks other sources unverified. It did not check their periodic twisted-sector hypotheses or an applicable cross-sector comparison. No external theorem is used as a load-bearing input here, and no literature-wide novelty claim follows.
