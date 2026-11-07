# SGAP: the charged gap in the chirality wall

**FINISH: FROZEN 2026-11-07 after pass 3 (SGAP_REFEREE.md); the referee's edits E1-E7 are applied.** Frozen means: the proved results below are not reopened; open statements are worked in their own files and enter by a dated amendment. The item enters `SMG15.md` as its Amendment 1. The lead (Claude Opus 5.5, laptop) checked that the edits are in the text; that is a text check, not a second referee. **Status.** S-GAP and its `t=0` case S-GAP⁰ remain **OPEN**. The results below are finite-ring statements conditional on the atom and Gauss reduction in `SMG1.md` and `SMG15.md`. Pass 3 done (SGAP_REFEREE.md); edits applied; ready to freeze. This is not an audit verdict. At `ε=0`, the charged gap is exactly `16τ`. For all `t,ε`, a local unitary transfers each charged block to the neutral block of a locally modified Hamiltonian. At `t=0`, conserved site parities reduce the problem to 16-level chains, but a comparison between sectors is still needed. The removal identity and an extensive odd-weight bound are proved below.

**Open statements to carry.** S-GAP⁰ (OPEN); S-GAP at `t≠0` (OPEN); (G1′) (unproved hypothesis, not adopted); (HF-alt) (unproved hypothesis, not adopted). Downstream, unchanged: R1.5-U, R1.5-D, R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D and W2/R4.

**GAPs.** A4 requires a bound `W_odd≤Kw` uniform in `L` and `ε`; by R-w it implies `w>0` when `|ε|<2τ`; the bound is not proved. A5 requires a strict local-window energy increase; that step is false. A6 requires a comparison across parity sectors; its per-sector half-filled gap assertion is false. (G1) and (HF′) below are unproved hypotheses. The statements about published stability and RG methods are context, not imported proof steps.

**Editing session provenance.** Codex `gpt-6.1-terra`, effort high, `codex-cli 0.165.0`; session id not visible.

**Provenance.** Pass 1: Claude Opus 5.5, max, `SGAP_DRAFT.md`. Pass 2: Codex `gpt-6.1-terra`; effort and session id: see run log. Source SHA-256: `SGAP_DRAFT.md` `c2715daa9826aed0d7074b6b25ba4cbcc0d9a2bb0295c5a582a69a796122dab8`; `prior/SGAP.md` `ec53242ca86df2b0d3e7216c945791c39a366e418fdda0dff0d857f91135d115`; `SMG15.md` `a192a685ed6b3d30c4a40e170e26cf90ec7a98873ebf1212aeff2bd741b9095c`; `SMG1.md` `1e5a05a66d0b11016d18264351321165979d569cd84ad213e1dc4072cb021622`; `CH1.md` `cdf1268c8a120d353f657bc211048e4f04f2ebe39704a76904ad77affc13564d`; `LW1.md` `78280bd620800eac671ddf6047d42e94c2ecf919d2f938909cc5595b168c09b9`; `TOE_ASSEMBLY.md` `5618fd1c8bd201b74d22911e0bd51916f6d8a47426592f2e2c9a108e93c58dca`. The source's historical revision claims were not refreshed with git. No pass-1 scratch result was reproduced; its recorded `/tmp/toe-SGAP` files were unavailable in this session.

## 1. Definitions inferred by the distiller

These definitions fix notation and the finite-ring reading. They add no axiom or adopted physical reading.

1. Let `L∈4N`, `L≥8`, and `x∈Z_L`. There are eight mirror Majoranas `γ_{x,a}`, `a=1,…,8`, and a light CAR mode `c_x`, with `n_x=c_x†c_x` and `N=Σ_x n_x`. Let `P_x` be total matter parity at `x`, `G_x=P_xX_{x−1}X_x`, `H_G=∩_x ker(G_x−1)`, and `H_{1/2}=H_G∩ker(N−L/2)`. Put `hop_x=c_x†Z_xc_{x+1}+c_{x+1}†Z_xc_x` and `hop⁰_x=c_x†c_{x+1}+c_{x+1}†c_x`. The electric coupling is zero; this is a restriction, not a derivation from the working set.
2. The atom `W`, the sign group `S≅Z₂⁴`, the characters `ρ_a`, and the projectors `P_x^χ` are those of `SMG1.md` §2 and `SMG15.md` §1 item 5 and §2. Each character line is one-dimensional. `W` has values `−14` on the trivial line, `0` on eight odd lines `ρ_a`, and `2` on the other seven even lines. Write `m(χ)=χ(g₁g₂)∈{±1}` and `Ŝ_+={χ:m(χ)=1}`. The eight `ρ_a` are distinct and odd. The global action is `U_g=∏_x g_x`.
3. For real `t,ε` and `τ>0`, set `T_{x,a}=iγ_{x,a}γ_{x+1,a}hop⁰_x`, `H_M=τΣ_x(W_x+14)`, `H_L=−tΣ_xhop_x`, `H_4=Σ_{x,a}T_{x,a}`, and `H_ε=H_M+H_L+εH_4`. Let `H^χ_{1/2}` be the `χ`-eigenspace of `U`, `E_χ` the bottom of `H_ε` there, with `E_χ=+∞` on an empty space, and `E_0=min_χ E_χ`. Neutral means `χ=1`; charged means `χ≠1`. Write `E_L=−2|t|/sin(π/L)`.
4. **S-GAP** asks for `c₀,Δ>0` such that for every `τ>0`, `|t|,|ε|≤c₀τ`, allowed `L`, and `χ≠1`, `E_χ≥E_0+Δτ`. **S-GAP⁰** is the same statement with `t=0`. Both include `ε=0`. These are finite-ring questions, not GNS or tick statements.
5. For `p∈{±1}^{Z_L}` with `∏_x p_x=1`, let `K_p={Φ∈H_G:P_xΦ=p_xΦ ∀x}`, `k(p)=#{x:p_x=−1}`, and `walls(p)=#{x:p_xp_{x+1}=−1}`. A fixed unit vector in the one-site character line `χ` is `e_χ`. A `p`-sector chain has local basis `|χ⟩_x=e_χ⊗|n_x(χ)⟩`, where `n_x(χ)=(1−p_xm(χ))/2`. In this basis `N=Σ_x n_x(χ_x)` and the charge is `∏_xχ_x`.
6. For a charged `σ`, let `O_x=Σ_{m(χ)=−1}P_x^χ`, `w=Σ_x‖P_x^σΨ‖²`, and `W_odd=Σ_x‖O_xΨ‖²`. The latter counts expected odd mirror lines; it is not a probability and can grow with `L`.

**Proposed readings, not adopted.** `SMG15.md` §1 proposes R15-SPEC under the owner-selected bounded R-GEN reading SMG1-GAP. Its referee's four tests are `C, P, P, C`: the finite-ring and canonical-sector bridge makes the fourth conditional. R-COR is also proposed, not adopted: its pass-1 checks were `C, P, C, P`, but after SMG1-GAP it fails test 3 as a reading of “gapped”; its correlation condition remains a diagnostic. The tick and GNS bridges remain separate. S-GAP⁰ is a named subcase, not a new reading; pass 1 reports its four checks as pass: it fixes no target, has closed quantifiers, settles no downstream question by premise, and adds no structure or constant. The ratio `ε²/(τ|t|)` is a proposed weak-interaction diagnostic only, undefined at `t=0`; it cannot replace the stated target.

## 2. Algebra and exact slice

**Theorem 1 (symmetries and charges; F1–F4, Lemma E).** Each `T_{x,a}` is a Hermitian contraction, preserves `N`, every `P_y`, all `G_y`, and the global `S` action. The Hamiltonian therefore preserves every `H^χ_{1/2}`. For fixed `t`, `E_χ(ε)=E_χ(−ε)`. Only `χ∈Ŝ_+` occur on `H_{1/2}`. There are eight such characters, and for each fixed `a`, `b↦ρ_aρ_b` bijects `{1,…,8}` with `Ŝ_+`.

*Proof.* `iγ_{x,a}γ_{x+1,a}` is a Hermitian unitary and `hop⁰_x` is a Hermitian contraction. They are even operators on disjoint mode sets, so commute. Each endpoint of `T` contains two odd operators, proving site-parity and Gauss invariance; it conserves light number. Both Majoranas acquire the same `ρ_a(g)` under `U_g`. The remaining terms preserve these symmetries by `SMG15.md` §2–3. Put `R=∏_{x even}(g₁g₂)_x`. Mirror parity reverses one Majorana on each bond and fixes the other terms, so `RH_εR*=H_{−ε}` within each charge block.

`P_x=(g₁g₂)_x(−1)^{n_x}` and Gauss's law gives `∏P_x=1`. Since `N=L/2` is even, `U_{g₁g₂}=1`. The map `χ↦χ(g₁g₂)` is onto because each `ρ_a` maps to `−1`; its kernel has eight elements. The eight distinct odd `ρ_a` exhaust its other coset. Multiplication by `ρ_a` gives the bijection. `□`

**Theorem 2 (Proposition Z).** At `ε=0`, for every real `t`, `E_1=E_L` and `E_σ=E_L+16τ` for all nontrivial `σ∈Ŝ_+`. Thus the largest possible S-GAP constant on this slice is `16`.

*Proof.* `H_M` is diagonal in mirror configurations, and the reduced light operator is the same in each compatible configuration (`SMG15.md`, Theorems 1–3). Its half-filled minimum over the two holonomies is `E_L`. A neutral all-trivial configuration attains it. A nontrivial even total charge requires either one nontrivial even site, costing `16τ`, or at least two nontrivial sites, costing at least `28τ`. A configuration with exactly one `σ` site attains `16τ` and is compatible with Gauss's law and half filling. `SMG15.md` Theorem 3 assumes `t₀≠0`; at `t=0`, `H_ε=H_M` on this slice, so `E_1=0` and `E_σ=16τ` directly. `□`

The configuration-conserving family and its `14τ−2δ` bound are already proved in `SMG15.md` Theorem 3; they do not cover the off-diagonal `H_4`. The atom and character shift are already proved in `SMG1.md` Theorem 2.2 and `SMG15.md` Theorem 1. The latter's Theorem 2 already proves the Gauss reduction used below.

## 3. Local charge shift

**Theorem 3 (Theorem A).** Fix `σ∈Ŝ_+\{1}`, a site `x₀`, and `a≠b` with `σ=ρ_aρ_b`. Let `Y=iγ_{x₀,a}γ_{x₀,b}` and

`B=16τ(P^1_{x₀}−P^σ_{x₀})−2ε Σ_{c∈{a,b}}(T_{x₀−1,c}+T_{x₀,c})`.

Then `Y` is a Hermitian unitary preserving `H_{1/2}`, sends charge `χ` to `χσ`, and `YH_εY=H_ε+B`. Consequently the `σ` block of `H_ε` is unitarily equivalent to the neutral block of `H_ε+B`.

*Proof.* CAR gives `Y*=Y`, `Y²=1`. The even on-site mirror operator commutes with `N`, site parities, Gauss operators, light and link operators; it transforms by `σ`. The character shift sends a local `χ` line to `χσ`. The atomic eigenvalue differences are `+16` at `χ=1`, `−16` at `χ=σ`, and zero elsewhere, including all odd lines. Conjugation by `Y` reverses precisely `γ_{x₀,a}` and `γ_{x₀,b}` and hence the four displayed bond terms. This gives the operator identity and the block equivalence. `□`

**Corollary 3.1 (A1).** For unit neutral and `σ` ground vectors `Ω,Ψ`, respectively,

`max_Ψ(−⟨Ψ,BΨ⟩) ≤ E_σ−E_1 ≤ min_Ω⟨Ω,BΩ⟩ ≤ 16τ+8|ε|`.

*Proof.* Apply the variational principle to `H_ε+B` in the neutral block at `Ω`, and to `H_ε` there at `YΨ`. The identity `YBY=−B` gives the lower bound. Each of the four bond terms is a contraction and `‖P^1−P^σ‖=1`. `□`

For a **single** charged block, Theorem 3 expresses its energy relative to `E_1`, not automatically to `E_0`. S-GAP is equivalent to a uniform positive lower bound on `E_σ−E_1` for **all seven** nontrivial even characters: such a bound gives S-GAP because `E_1≥E_0`; conversely, S-GAP makes every charged `E_σ` exceed `E_0`, so the minimum `E_0` is attained at `χ=1` and `E_1=E_0`. If S-GAP holds, `Δ≤16+8c₀`, and the `ε=0` slice sharpens this to `Δ≤16`. A translation eigenvector in a charged ground space obeys `⟨P^σ_{x₀}−P^1_{x₀}⟩=(⟨Σ_xP_x^σ⟩−⟨Σ_xP_x^1⟩)/L`; the lower variational bound need not be positive.

Pass 1 reports a sparse open two-site, no-link `1024×1024` check of the conjugation identity and sector spectra, with zero floating-point discrepancy and a sample gap `15.997382` at `τ=1,t=0.3,ε=0.05`. It also reports a dense first run exceeding its 1 GB cap. These are reported checks, not proof or checks of the ring quantifiers; the files were unavailable here.

## 4. Conserved parity sectors at `t=0`

**Theorem 4 (Theorem C and Corollary C1).** At `t=0`, `H_ε` commutes with every `P_x` and every link operator. The Gauss space is `⊕_{∏p=1}K_p`, with `2^{L−1}` sectors, and

`K_p ≅ (⊗_x C^{16})⊗C²`,  `H_ε|K_p=H_p⊗1`,

where `H_p=τΣ_x(W(χ_x)+14)+εΣ_{x,a}T^p_{x,a}`. On the local basis of Definition 5, `T^p_{x,a}` connects `|χ_x,χ_{x+1}⟩` to `|χ_xρ_a,χ_{x+1}ρ_a⟩` with matrix element of modulus one exactly when `m(χ_x)m(χ_{x+1})=−p_xp_{x+1}`; otherwise it annihilates that basis vector. The `C²` factor is inert. Each chain has a unique product on-site zero vector `|1⟩^{⊗L}`, an on-site gap `14τ`, and terms of norm at most `|ε|` per flavour and bond. This vector is neutral, has `N=k(p)`, and a bond term acts on it exactly at a wall.

*Proof.* The atomic term and `T` preserve all site parities; at `t=0` neither uses links. The Gauss reduction `J:F_even⊗C²→H_G` maps all parity-preserving matter operators to themselves tensored with `1`. At fixed `p_x`, each of the 16 mirror lines determines one light occupation, giving the stated basis. Products of site-even operators act on the corresponding ordinary tensor factors, including the wrap bond. Each `T` is a sum of products of site-even operators `γc` or `γc†`; it changes each endpoint's character by `ρ_a` and exchanges light occupancy. Its amplitude has modulus one by CAR and one-dimensionality of the character lines. The exchange is possible exactly when the two occupations differ, which is the displayed condition. The remaining assertions follow from the atom values and `m(1)=1`. `□`

The unsplit reference's multi-dimensional on-site kernel in the Fröhlich–Pizzo attack in `SMG15.md` is absent inside a fixed `p` chain; the inert `C²` is a global multiplicity. Also, the free moving light chain responsible for the cited `|z|⁻²` tails is absent at `t=0` inside these sectors. These observations do not verify every hypothesis of a stability theorem or the comparison between sectors.

**Proposition 4.1 (C2: per-sector comparison is false).** At `t=ε=0`, choose `p_x=(−1)^x` and change `p_0,p_2` to `−1`. In `K_p∩H_{1/2}`, both the neutral and every even charged minimum equal `28τ`, while `E_0=0`.

*Proof.* Here `k(p)=L/2+2` and `∏p_x=1`. The identity `N=k(p)+Σ_{x:m(χ_x)=−1}p_x` shows half filling requires at least two odd sites, costing at least `28τ`. Put `ρ_a` at 0 and `ρ_b` at 2 and trivial characters elsewhere. This reaches the bound and has charge `ρ_aρ_b`. Take `a=b` for neutral and use Theorem 1 for any even charge. The all-trivial state in an alternating sector gives global energy zero. `□`

**Proposition 4.2 (C3: second order).** Let `P` project in `K_p` onto `|1⟩^{⊗L}⊗C²` and `Q=1−P`. Then

`PH_4P=0`,  `PH_4Q(QH_MQ)⁻¹QH_4P=(2/(7τ)) walls(p) P`.

The formal second-order correction is `−2ε² walls(p)/(7τ)`, minimized by the two alternating patterns, both half filled. All other patterns have at most `L−2` walls. Higher orders are not bounded here.

*Proof.* This is the already-proved `SMG15.md` Theorem 7 restricted to `K_p`: `hop⁰_x²=n_x+n_{x+1}−2n_xn_{x+1}` is the wall indicator on the product vector. A ring has an even number of walls and reaches `L` only for alternating signs. `□`

**Proposition 4.3 (C5: sufficient hypotheses).** Suppose `t=0` and there are `c₀,Δ_G>0`, `δ≥0` such that for every allowed `L`, `τ>0`, and `|ε|≤c₀τ`:

- **(G1)** each `H_p` has a nondegenerate ground eigenvalue `e_p`, with every other eigenvalue at least `e_p+Δ_Gτ`;
- **(HF′)** `E_0−E_*≤δτ`, where `E_*=min spec(H_ε|H_G)` without fixing `N`.

Then every charged energy satisfies `E_σ≥E_0+(Δ_G−δ)τ`. If `δ<Δ_G`, S-GAP⁰ follows.

*Proof.* At `ε=0`, each chain ground vector is the neutral product. For a fixed endpoint `ε`, (G1) holds along the segment from 0 to `ε`. Its isolated rank-one ground projector varies continuously, while its `S` character takes values in a finite set. The character therefore stays trivial. Every charged vector is orthogonal to it and costs at least `e_p+Δ_Gτ`. Theorem 4 gives `E_*=min_p e_p`; apply (HF′). `□`

**Weaker sector hypothesis (referee closure, SGAP_REFEREE.md).** At `t=0`, let **(G1′)** assert that there are `c₀,Δ_G>0` such that for every allowed `L`, `τ>0`, `|ε|≤c₀τ` and every `p`, every `S`-charged vector of `K_p`, of any `N`, has energy at least `e_p+Δ_Gτ`. (G1) implies (G1′) by the ground-state continuity argument above. Together (G1′) and (HF′) give `E_σ≥min_p e_p+Δ_Gτ=E_*+Δ_Gτ≥E_0+(Δ_G−δ)τ`, since `H_ε` is block diagonal in `p`. (G1′) is unproved and not adopted.

**Alternating-sector comparison (referee closure, SGAP_REFEREE.md).** Let `p_alt` be alternating and let **(HF-alt)** be `e_{p_alt}−min_p e_p≤δτ`. Under (G1), the simple ground projector of `H_{p_alt}(s)` is continuous from `s=0` to `ε`. Since `N` and `U_g` commute with the chain Hamiltonian, their ground-state values are continuous and discrete; at `s=0` they are `L/2` and `1`. The ground vector therefore remains half filled and neutral, so `E_0≤e_{p_alt}` and (HF-alt) implies (HF′). (HF-alt) is unproved and not adopted; Proposition 4.2 suggests `δ=0` at second order, without a higher-order bound.

**Corollary 4.4 (C6).** At `t=0`, every eigenvalue on each `H^χ_{1/2}` has even multiplicity. In particular the half-filled ground vector is not unique at zero electric coupling.

*Proof.* In Theorem 4, `H_ε`, `N`, and `U_g` all act trivially on the `C²` factor. `□`

## 5. Charge removal and odd weight

**Theorem 5 (Lemma R).** For a normalized `σ`-ground vector `Ψ`, choose `a,b` as in Theorem 3 and write `Y_y=iγ_{y,a}γ_{y,b}`, `D_y=Y_yP_y^σ`, `H_4^{(y)}=Σ_{c=1}^{8}(T_{y−1,c}+T_{y,c})`. Then `D_yΨ` is neutral, `‖D_yΨ‖=‖P_y^σΨ‖`, and

`⟨D_yΨ,H_εD_yΨ⟩=(E_σ−16τ)‖P_y^σΨ‖²−ε⟨P_y^σΨ,H_4^{(y)}Ψ⟩`.

Consequently

`(E_σ−E_1−16τ)w ≥ −|ε|X`,  `X=Σ_y|⟨P_y^σΨ,H_4^{(y)}Ψ⟩| ≤ 4√2 √(w W_odd)`.

*Proof.* Theorem 3 gives the charge and norm assertions. In `P_y^σ(H_ε+B_y)P_y^σ`, the local atomic part of `B_y` is `−16τP_y^σ` and its bond part vanishes because each bond changes the character at `y`. `H_M,H_L` commute with `P_y^σ`, and `P^σ_yH_ε(1−P^σ_y)=εP^σ_yH_4^{(y)}`; the eigenvalue equation yields the displayed identity. The neutral variational bound and a sum over `y` give the first inequality. For each bond and flavour, only the input line `σρ_c` contributes to the matrix element into `σ`. These eight distinct lines exhaust the odd lines. Two Cauchy–Schwarz inequalities and the two incident bonds give `2√8 √(w W_odd)`. `□`

Thus, when `w>0`, `E_σ−E_1≥16τ−4√2|ε|√(W_odd/w)`. The draft's sufficiency claim omits the `w>0` step; referee closure R-w supplies it for `|ε|<2τ`. If `w=0`, the summed inequality alone is `0≥0` and gives no gap; a charged configuration can have no local `σ` line, for example two even nontrivial characters whose product is `σ`.

**R-w (referee closure, SGAP_REFEREE.md).** Let `|ε|<2τ`, any `t`, and `Ψ` be a normalized `σ`-ground vector, `σ≠1`. If `W_odd=0`, then `w>0`.

*Proof.* At `ε=0`, Theorem 2's minimizers have exactly one `σ` site, so `w=1`. Let `ε≠0`. `H_M` and `H_L` preserve mirror configurations; each `T_{x,a}` reverses mirror parity at `x` and `x+1`. If `W_odd=0`, `Ψ` lies in all-even configurations and `H_4Ψ` lies in configurations with two odd sites. Projecting `H_εΨ=E_σΨ` onto those gives `H_4Ψ=0`, so `(H_M+H_L)Ψ=E_σΨ`. If also `w=0`, every configuration in `Ψ` has charge `σ` and no `σ` line, hence at least two nontrivial even lines, so `E_σ≥E_L+32τ`. The neutral trial vector with all lines trivial and the light ground state in the best holonomy has `⟨H_4⟩=0`, so `E_1≤E_L`. Corollary 3.1 gives `E_σ≤E_1+16τ+8|ε|<E_L+32τ`, a contradiction. `□`

**Sufficiency (referee closure, SGAP_REFEREE.md).** Suppose `K≥0`, `0<c₀<2`, `4√2c₀√K<16`, and for every allowed `L`, `τ>0`, `|t|,|ε|≤c₀τ` and `σ≠1` some normalized `σ`-ground vector has `W_odd≤Kw`, with `K` independent of `L` and `ε`. Then S-GAP holds with `Δ=16−4√2c₀√K`. Indeed, the bound and R-w imply `w>0`, and Theorem 5 gives `E_σ−E_1≥Δτ`; the equivalence after Corollary 3.1 gives S-GAP.

**Proposition 5.1 (R2).** Let `t=0`, `0<ε≤τ`, and `σ∈Ŝ_+\{1}`. Define `g(ε)=[2ε²/(7τ)]/[1+ε²/(98τ²)]`. Then

`E_σ(ε)≤16τ−(L/2−1)g(ε)`.

There is a differentiability point `ε′∈(0,ε]` such that every normalized `σ`-ground vector at `ε′` obeys `W_odd≥Lε²/(200704τ²)`.

*Proof.* Use the alternating `p` sector. Put `|σ⟩,|1⟩` at sites 0,1 as two single-site factors. On each other pair `(2j,2j+1)` use the normalized vector proportional to `|1,1⟩−κΣ_cω_c|ρ_c,ρ_c⟩`, with `κ=ε/(28τ)` and `ω_c=⟨ρ_c,ρ_c|T^p_{2j,c}|1,1⟩`. Each `|ω_c|=1`. The pair has fixed light number one and neutral charge. Its energy is

`(8κ²·28τ−16εκ)/(1+8κ²)=−g(ε)`.

Every bond between blocks, and every bond at sites `0` and `1`, has zero expectation because it changes one character in each of two factors, leaving their supports. The trial state is half filled and has charge `σ`, proving the upper bound.

The finite-dimensional lowest eigenvalue `E_σ(s)` is concave in `s` and differentiable except at finitely many points. By Theorem 2, `E_σ(0)=16τ`. The secant bound and `L/2−1≥L/4` give a differentiability point with `E_σ′(ε′)≤−Lε/(28τ)`; use `g(ε)/ε≥ε/(7τ)`. At such a point every ground vector has `⟨H_4⟩=E_σ′(ε′)`. Since `T_{y,c}` flips odd/even mirror parity at `y`, `|⟨T_{y,c}⟩|≤2‖O_yΨ‖`. Summing gives `|⟨H_4⟩|≤16√(LW_odd)`, hence the stated constant. `□`

## 6. Open statements and failed steps

**S-GAP⁰ (OPEN).** The target in Definition 4 remains open. In Theorem 4's notation it is equivalent, for a positive uniform `Δ`, to the charged minimum over all `p` and `N=L/2` being at least `Δτ` above the corresponding neutral minimum: if this holds, the neutral minimum is the full ground energy. S-GAP at `t≠0` also remains open.

**A4 — removal: GAP.** The missing step is `W_odd≤Kw` uniformly in `L` and `ε`. Proposition 5.1 shows that at some `ε′`, `W_odd` grows at least linearly in `L`; the desired bound would therefore require an extensive lower bound on `w` at those parameters. The removal identity does not supply it. This does not disprove that bound. Its Cauchy–Schwarz estimate counts odd fluctuations far from the selected charged line; a suitable localization or correlation estimate is missing. The same identity applies at nonzero `t`.

**Conditional obstruction (referee closure, SGAP_REFEREE.md).** If `w≤w_max` at the parameters `ε′_L` of Proposition 5.1, with `w_max` independent of `L`, then no `L`-uniform `K` exists: Proposition 5.1 gives `W_odd/w≥Lε²/(200704 w_max τ²)`, which is unbounded in `L`.

**Referee heuristic (SGAP_REFEREE.md), not a proof.** If `w` grows with `L`, `σ` lines created in neutral pairs far from the charged line can cause the growth. For such a line, the variational step may discard about `32τ` per line while protecting `16τ`; this suggests restricting the sum to the charged line's neighbourhood, requiring a localization estimate.

**A5 — local window: GAP, with counterexample to the needed strict inequality.** Let `Λ` contain `x₀` and its incident bonds, write `H_ε=H_out+K`, with `H_out` supported away from `x₀`, and take unrestricted window eigenvalues on a space preserved by `Y`. Then `YH_outY=H_out` and `YKY=K+B`; since `YBY=−B`, `Y(K+B)Y=K`. Thus `K+B` and `K` are unitarily equivalent, and `λ_min(K+B)=λ_min(K)` exactly, for every `t,ε` and every window space preserved by `Y` (referee closure, SGAP_REFEREE.md). A neutral global vector can carry charge `σ` both inside and outside the window, so one cannot simply impose window neutrality. The failure holds for every `t`; it does not refute S-GAP.

**A6 — parity-sector stability: GAP.** A per-sector half-filled charged-versus-neutral gap is false by Proposition 4.1. Even a proof of (G1) must compare the best charged half-filled sector with the global half-filled minimum; (HF′) suffices by Proposition 4.3 but is open. The elementary estimates are extensive: `H_p≥14τW_odd−16|ε|√(LW_odd)≥−(32/7)(ε²/τ)L` in expectation, while the neutral paired trial state gives `E_0≤−(L/2)g(ε)`. They do not yield the needed `O(τ)` comparison. A convergent sector expansion with controlled `p`-local energy terms and a classical comparison is a proposed route, not a proved necessity or an attempted construction.

**Prior failed routes.** `SMG15.md` §8 identifies local Schrieffer–Wolff with an extensive remainder bound; absolute light-linked polymers with a possible logarithmically divergent absolute `|z|⁻²` contribution, without excluding cancellations; and the cited Fröhlich–Pizzo application with a degenerate unsplit on-site reference. The fixed-volume Feshbach estimate and Gaussian-replacement failure for a different atom are recorded in `prior/SGAP.md`; neither supplies this uniform gap. For nonzero `t`, parity sectors mix and the leading formal light term is the density interaction already proved as an atomic resolvent identity in `SMG15.md` Theorem 7. A constructive RG treatment would still need a justified bridge to this charged-energy difference.

**Other open items by name.** R1.5-U (generic uniqueness and absence of translation breaking), R1.5-D (controlled decoupling and light scaling), R15-GNS, P3, Q-R15, the tick/generator state comparison, W2-LIGHT, R1-H, FLQ, R2, R3-H, R3-D, and W2/R4 remain open as specified in `SMG15.md` and `CH1.md`. Corollary 4.4 rules out R15-SPEC's finite-ring uniqueness S3 at `t=0` for this zero-electric-coupling model; it does not settle generic uniqueness for other parameters. Neither the finite-ring result nor the proposed reading establishes the higher-dimensional chirality target.

**Prior sources and limits.** `prior/SGAP.md` records the earlier exact-family, twist, circuit and second-order results in `SMG15.md`; their stated scopes remain unchanged. It also reports a distinct half-filled ring comparator at `ref/main/docs/ADMISSIBILITY_RULE_THE_HARD_CORE_SEA_ON_A_RING_IS_ONE_TWISTED_BAND_HALF_FILLED_WITH_HALF_THE_FREE_SEAS_VOLUME_TERM_AND_CLOCK_STIFFNESS_BOUNDED_THEOREM_NOTE_2026-09-24.md` and distinct atom–bath calculations at `ref/main/docs/SPIN10_SYMMETRIC_ATOMIC_GAPS_MIRROR_BOUNDARY_PROJECTION_AND_CURRENT_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-14.md`. Those are digest reports, not independently checked here, and do not transfer their conclusions to `H_ε`. The KMS scalar-ODE result at `ref/main/docs/KMS_FERMIONIC_BRYDGES_MAJORANT_EXTERNAL_NARROW_THEOREM_NOTE_2026-05-11.md` does not by itself supply the required fermionic inequality. Pass 1's literature search and citations are recorded in `SGAP_DRAFT.md` §2; its cited abstracts were not independently re-fetched here. In particular no claim of an exhaustive literature absence follows from its search. No axiom, law, frozen source or working-set entry changes.
