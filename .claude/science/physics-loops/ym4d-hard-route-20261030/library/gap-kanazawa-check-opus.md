# Check of library/gap-kanazawa-astra.md (FINISH row 801), by Claude Opus 5.5, line by line

Clone: `/Users/jonreilly/ym4d-lead/clone`. HEAD was `e9dd2626058e922b2ec1ac468317b1ca1e3f98c6`
at the start and `33a4d3b457825282502b78bdf6746dffa94557ff` at the end. `git diff --stat`
between them shows no change under the lane `library/`. Target last touched by
`f91f31f354`; sha256 prefix `e26e1c16f9a22d3d`; 734 lines, read in full.

Context read: `gap-tomboulis-read.md` §§2–2.4; `gap-tomboulis-check-opus.md` §§B–C;
`gap-means-max.md` §§4.1–4.6 (incl. (TM-tw) at 146–162); `gap-ext-astra.md` §§3.2–3.3, 4.2;
`gap-vortex-astra.md` §§4–7; `gap-trf-astra.md` 115–150 for (FQ) and (T2).
The SA outline was downloaded once at `31a47c543775` into its own new directory
(`scratchpad/sa-dl/pXrvgp/`). I read lines 1150–1356 only. Kanazawa v3 was **not**
downloaded. The §1 READ claims about his Theorems 1 and 3 are therefore not checked here.

Every verdict below is by hand. No numerical run was used, not even a GUIDE.

## 1. (K1)–(K8)

**(K2).** From (K1), Q_f = [Z_c^+(α)/Z_c(α)]·[Z_c(α)/Z_c(α_Λ)] = Q_c(α)e^{-D}.
So D = log Q_c(α) − log Q_f. Then R_f = 2Q_f − 1 = (1+R_c(α))e^{-D} − 1.
Also D = L_c(α_Λ) − L_c(α) = N∫_α^{α_Λ} p'_c, since L_c = N p_c. All three identities hold.

**(K3).** R_f ≥ R_c − ε ⟺ (1+R_c)e^{-D} ≥ 1+R_c−ε ⟺ e^{-D} ≥ 1 − ε/(1+R_c).
The right side is positive when ε < 1+R_c. Taking logs gives D ≤ −log(1 − ε/(1+R_c)). Holds.
*Scale.* If α_Λ ≥ α then D ≤ NC(α_Λ−α). If α_Λ < α then D ≤ 0. So D_+ ≤ NC(α_Λ−α)_+.
Put x = ε/(1+R_c). Then x ≥ ε/2, since R_c ≤ 1, and −log(1−x) ≥ x ≥ ε/2.
So (α_Λ−α)_+ ≤ ε/(2NC) gives (K3). The converse uses D ≥ Nc(α_Λ−α) when α_Λ > α.
The required scale is ε/N. Holds.

**(K4).** G = ∂log Z − ∂log Z^+ = −∂log(Z^+/Z) = −∂log Q. With row 797's
Φ = B^{-1}log Z_c, A = Φ', and A^+ = (Φ^+)', we get G = B(A − A^+).
The common bulk factor F̃_0 cancels between Z and Z^+. Holds.

**(K5).** At s = 0 the fine Wilson weight is constant. So Z_m = Z_{m+v} = 1 (Haar), R_f = 1, Q_f = 1.
At u = 0 we have f_0 = 1, so Q_c = 1. Integrating (K4) gives log Q_f(β) = −∫_0^β G_f and
log Q_c(α) = −∫_0^α G_c. Substituting into D = log Q_c(α) − log Q_f gives (K5). Holds.
Remark: this uses only the definition D := log Q_c(α) − log Q_f. It does not use (K1) or α_Λ.

**(K6).** I take dμ_m ∝ e^{sH_m}. With v represented by the sheet Σ, η_{m+v,p} = −η_{m,p} on Σ.
So H_{m+v} = H_m − 2Y and R = ⟨W⟩_m with W = e^{-2sY}.
*First form.* ∂log Z^+ = (⟨H_m⟩_m + R⟨H_{m+v}⟩_{m+v})/(1+R). Subtracting this from ⟨H_m⟩_m
gives R(⟨H_m⟩_m − ⟨H_{m+v}⟩_{m+v})/(1+R). This is the factor R/(1+R).
*Second form.* R' = ⟨∂_sW⟩ + ⟨WH_m⟩ − ⟨W⟩⟨H_m⟩ = −2⟨YW⟩ + Cov_m(W,H_m).
So G = −R'/(1+R) = (2⟨WY⟩ − Cov_m(W,H_m))/(1+R).
*Consistency.* ⟨H_{m+v}⟩_{m+v} = ⟨(H_m−2Y)W⟩_m/R. So R⟨H_m⟩ − R⟨H_{m+v}⟩_{m+v} = 2⟨YW⟩ − Cov(W,H_m).
The two forms agree. The covariance is with the whole H_m, which is extensive.
A constant shift −sN_f multiplies Z_m and Z_{m+v} alike and cancels from R and from G. Holds.

**(K7).** Fix α and differentiate L_c(α_Λ(β)) = L_c(α) + log Q_c(α) − log Q_f(β).
This gives N p'_c(α_Λ) α_Λ' = G_f(β), which is (K7) when L'_c > 0.
*Offset.* At β = 0, Q_f = 1. So L_c(α_Λ(0)) = log Z_c(α) + log Q_c(α) = log Z_c^+(α).
Since Q_c ≤ 1 and L_c is increasing on J, α_Λ(0) ≤ α. Its size is at most
H_c(α)/(Nc_*) ≤ 2e^{-ℓ²}/c_*, by (K21). It vanishes only if R_c(α) = 1. Holds.

**(K8).** 1 − R_f = 2 − (1+R_c)e^{-D}.
For D ≥ 0 this equals δ_c + (1+R_c)(1−e^{-D}) ≤ δ_c + 2D.
For D < 0 we have e^{-D} > 1, so R_f > R_c and 1 − R_f < δ_c. Holds.
*Budget.* δ_c ≤ e_a/4 and D_+ ≤ e_a/8 give 1 − R_f ≤ e_a/2.
So Q_F ≤ e_a/4 ≤ 1/384 < 1/192.
Also 8Q_F ≤ 2e_a ≤ K(a)η_*^{a/2}/2 ≤ K(a)√S_ev, using S_ev ≥ η_*^a.
This matches (FQ) as stated in `gap-trf-astra.md:121–141`. Holds.
*Minor correction (wording).* The (V) sentence requires "their sum is at most 1/2".
The condition used is δ_c + 2D_+ ≤ 1/2. Then −log(1−x) ≤ 2x for x ≤ 1/2 gives F_f ≤ 2(δ_c+2D_+).

**Verdict, item 1: HOLDS** (one wording fix in the (V) clause of (K8)).

## 2. (K9)–(K10)

**(K9).** (TM-tw), `gap-means-max.md:148`, gives T_m ≥ 0, trace class, commuting with the flips,
and Z^{e+m} = Tr(T_m^t C^e) for spatial m in frame 1. Linearity gives
Z^+ = (Z_m + Z_{m+v})/2 = Tr(T_m^t(1+C_v)/2).
In a joint eigenbasis, Tr(T^tC_v) = Σλ_i^t c_i with c_i = ±1 and λ_i ≥ 0. So Z_{m+v} ≤ Z_m.
The integrand is positive, so Z_{m+v} > 0. Hence R ∈ (0,1] and Q ∈ (1/2,1].
I checked the required pairs. In frame 1, m_2 = k_34 = 0 leaves m ∈ ⟨k_23, k_24⟩, which is spatial.
Both v_13 and v_14 contain direction 1, so they are temporal. One frame suffices. Holds.

**(K10).** f_u ≥ 1 − 4u > 0 for u < 1/4. Its character coefficients are c_0 = 1 and c_{1/2} = 2u ≥ 0.
f_u is real and central, so the convolution ψ ↦ ∫f_u(UV^{-1})ψ(V)dV is self-adjoint.
By Schur it acts on the spin-j coefficient space by c_j/d_j ≥ 0. So it is PSD.
In temporal gauge each temporal plaquette gives f_u(U_ℓ(t)U_ℓ(t+1)^{-1}). Their tensor product is PSD.
The spatial factor M = Π f_u(η_pU_p) > 0 includes the magnetic signs. Then T = PM^{1/2}KM^{1/2}P ≥ 0.
The temporal twist v sits on one time seam. There it acts as the centre flip of the direction-3
(or 4) links on one slice. That flip leaves every spatial plaquette weight invariant:
a plaquette contains 0 or 2 flipped links. It also commutes with K, since K is central-covariant.
So C_v commutes with T. The periodic residual gauge integral gives the trace on gauge-invariant
states. This yields (K9) for the coarse box. The note does not identify (K10) with a block
Wilson action, and that is correct. Holds.

**Verdict, item 2: HOLDS.**

## 3. Coarse lemma (K11)–(K16)

**SA input, checked against outline 1150–1356.** The criterion is
Σ_{Y≁X}|z_Y|e^{a_Y} ≤ a_X, with self-incompatibility. The conclusion bounds the absolute
unrooted connected series by Σ_X|z_X|e^{a_X}, by rooting at the first vertex.
On a domain with a uniform majorant it gives the holomorphic branch of log Z that is 0 at 0.
The note quotes this correctly.

**(K12) and hard core.** Expand Π_p(1 + 2uχ(η_pU_p)) over subsets S. Split S into
link-connected components. Distinct components share no link, so the Haar integral factorizes.
Families of pairwise disjoint, non-adjacent polymers correspond bijectively to subsets S.
So Z_η is the hard-core polymer partition function, with incompatibility meaning "share a
plaquette or a link". Holds.

**Degree and count.** A plaquette has 4 links. In 4D each link lies in 6 plaquettes.
Two distinct plaquettes share at most one link. So the degree is exactly 4·5 = 20, for sides ≥ 3.
A DFS walk of a spanning tree has 2(k−1) steps along graph edges, each with ≤ 20 choices.
Its visited set is the k-set. So the count is ≤ 20^{2(k−1)} = 400^{k−1} ≤ 441^k.
The bound is valid but loose. Holds.

**|z_X|.** |2χ_{1/2}| ≤ 4 and Haar is a probability, so |z_X| ≤ (4|u|)^{|X|}. Holds.

**(K13) and the criterion.** 441·4e²·r = 1/84, so Σ_{X∋p}|z_X|e^{2|X|} ≤ Σ_k 84^{-k} = 1/83.
Use the weighted activities z̃_X = z_Xe^{|X|} and a_X = |X|.
Y ≁ X forces Y to meet the closed neighbourhood of X, which has ≤ 21|X| plaquettes.
So Σ_{Y≁X}|z̃_Y|e^{|Y|} ≤ 21|X|/83 < |X|. Holds.

**(K14).** The SA bound gives Σ|φ|/n!·Π|z̃_{X_i}| ≤ Σ_X|z_X|e^{2|X|} ≤ Σ_pΣ_{X∋p} ≤ N/83 ≤ N. Holds.
*Analyticity.* The margin 21/83 < 1 persists for |u| ≤ r(1+δ) with small δ > 0.
So log Z_η is holomorphic near the closed disc. Better still, z_X(u) = u^{|X|}z_X(1),
so |z_X(r)|e^{|X|} = |z_X(re)|. Then (K14) is an absolute bound at radius re.
It gives |N b_k| ≤ N(re)^{-k} directly. This is stronger than (K15)'s r^{-k}. Holds.

**Mod-2 cycles.** Flip an odd-incidence link U_ℓ → −U_ℓ. Haar is invariant and
χ_{1/2}(−g) = −χ_{1/2}(g), so the integral equals its negative and vanishes.
η_p = ±1 is central, so z_X(η) = (Πη_p)z_X(1). Holds.

**Homology and the factor 2.** Write η = (−1)^ω with δω = 0. Then Π_{p∈X}η_p = (−1)^{⟨ω,X⟩}.
This depends only on [ω] and on the mod-2 class [X]. It equals 1 on boundaries, since ⟨ω,∂c⟩ = ⟨δω,c⟩ = 0.
The Ursell factor φ depends only on the incompatibility graph, not on η.
So a cluster term changes with η only if some X_i has [X_i] ≠ 0.
*Size.* Let π_{μν}: T⁴ → T²_{μν} be the cellular projection. It sends μν-plaquettes to plaquettes
and the others to lower cells. π_*X is a mod-2 2-cycle of T². Since T² has no 3-cells,
Z_2(T²) = {0, [T²]}. A nonzero μν coordinate forces π_*X = all L_μL_ν plaquettes,
each with an odd number of preimages. So |X| ≥ L_μL_ν ≥ ℓ². Such a cluster has total size ≥ ℓ².
For each such term, |T(η) − T(η')| ≤ 2|T| ≤ 2e^{-ℓ²}|T|e^{Σ|X_i|}. Summing with (K14) gives
|log Z_η − log Z_η'| ≤ 2Ne^{-ℓ²} for 0 ≤ u ≤ r. Both the sign argument and the factor 2 hold.

**(K15), c⁶ coefficient.** Only cycle polymers have nonzero activity. Their size is ≥ 6.
At size 6, only elementary cube boundaries occur. The slicing proof in
`gap-tomboulis-check-opus.md` B3 shows this; wrapping cycles need ≥ 64 plaquettes.
Each cube has weight (2u)^6·d^{8−12} = 64u⁶/16 = 4u⁶. There are C(4,3)V = 4V cubes.
δω = 0 gives product 1 on each cube. Clusters of two or more polymers have size ≥ 12.
So log Z_η = 16Vu⁶ + O(u⁷), and p_η = (16V/6V)u⁶ + … = (8/3)u⁶ + Σ_{k≥7}. Holds.
*Cauchy.* |log Z| ≤ N on |u| = r gives |b_k| ≤ r^{-k}. Holds.

**(K16).** p' − 16u⁵ = Σ_{k≥7} k b_k u^{k−1}. Its modulus is ≤ (u⁶/r⁷)Σ_{j≥0}(j+7)(u/r)^j.
For x = u/r ≤ 1/2: Σ(j+7)x^j = x/(1−x)² + 7/(1−x) = 2 + 14 = 16. Holds.
*Constants.* With α = r⁷/8, J ⊂ [r⁷/16, 3r⁷/16] ⊂ [0, r⁷/2] ⊂ [0, r/2], since r < 1.
16u⁶/r⁷ ≤ 8u⁵ ⟺ u ≤ r⁷/2. So 8u⁵ ≤ p' ≤ 24u⁵ on J.
This gives c_* = 8(α/2)⁵ and C_* = 24(3α/2)⁵. J ⊂ [0,r] also gives the second bound of (K11) there.
J ⊂ (0,1/4) keeps (K10) positive. Holds.

**Verdict, item 3: HOLDS.**

## 4. (K17)–(K18)

**(K17).** Q_f ∈ (1/2,1] holds by (K9) for the fine Wilson pair in frame 1.
Q_c(α) ∈ (1/2,1] holds by (K9)–(K10) on the coarse box, which carries the same classes.
So D := log Q_c(α) − log Q_f lies strictly inside (−log 2, log 2).
On J, L_c' = Np'_c ≥ Nc_*. Hence L_c(3α/2) − L_c(α) ≥ Nc_*α/2 > log 2 > D.
Likewise L_c(α) − L_c(α/2) > log 2 > −D.
By the IVT and strict monotonicity there is exactly one α_Λ ∈ J with L_c(α_Λ) = L_c(α) + D.
Exponentiating gives Z_c(α_Λ) = Z_c^+(α)/Q_f, which is (K1).
Also |α_Λ − α| ≤ |D|/(Nc_*) ≤ log 2/(Nc_*). Holds.
*Uniformity.* The proof uses only |D| < log 2 and (K11), and (K11) holds for every closed cocycle.
So it is uniform in β ≥ 0 and in spatial m. Holds.
*Analyticity.* Q_f(β) is real-analytic and positive: it is a finite compact integral of an entire
integrand. L_c is real-analytic on J, the log of a positive polynomial, with L_c' ≠ 0.
The analytic inverse function theorem applies. Holds.
Uniqueness is claimed only in J, which is all that is needed.

**Dyadic specialization.** For k ≥ n+3, ℓ = 2^{k−n} ≥ 8, so the sides are ≥ 8.
N = 6a²cd/16^n → ∞, so Nc_*α/2 > log 2 holds for large k.
The cohomology labels transfer: same coordinate pair, closed dual stack. Holds.

**(K18).** Apply (K11) with η = m+v and η' = m at u = α ≤ r, with ℓ² = a²/4^n.
This gives 0 ≤ F_c = −log R_c ≤ 2Ne^{-a²/4^n}, with the lower bound from R_c ≤ 1.
Then 1 − R_c ≤ F_c. Holds.
N ≤ 24a⁴/16^n is polynomial. With fixed n the exponent is quadratic in a, so the endpoint is
area-small. The note correctly states that nothing bounds D as k grows.

**Verdict, item 4: HOLDS.**

## 5. (K19)–(K20)

**(K19).** Suppose both twists are temporal in a frame, as e_m and e_v.
Then Z^+ = Tr(T_0^t C^{e_m}(1+C^{e_v})/2). On the flip character χ the multiplier is
(−1)^{χ·e_m}(1+(−1)^{χ·e_v})/2. It equals −1 when χ·e_v = 0 and χ·e_m = 1.
Projecting the e_v parity leaves the e_m parity. Holds.

**(K20).** Take m = v_24 (k_24 = m_3 in frame 1, with m_2 = 0) and v = v_13. This is a required pair.
In time 2, v_24 contains the time direction, so it is the insertion C_4.
v_13 does not contain direction 2, so it is a spatial background.
So Z_m = Tr(T_0^tC_4) and Z_{m+v} = Tr(T_{v13}^tC_4), and the seam operator is C_4(T_0^t+T_{v13}^t)/2.
Both T's commute with C_4. On the C_4 = −1 subspace the form is −⟨ψ,(T_0^t+T_{v13}^t)ψ⟩/2 ≤ 0.
*Strictness.* For β > 0 the Wilson character coefficients are positive multiples of
Bessel functions I_{2j+1}(β) > 0. So K is injective and PSD.
M^{1/2} is bounded below, with the magnetic signs included. So T = PM^{1/2}KM^{1/2}P is
positive definite on gauge-invariant states, and so is T^t.
*Nonemptiness.* The direction-4 Polyakov trace is gauge invariant and nonzero.
In frame 2 it uses spatial links only. It changes sign under C_4.
So the subspace is nonzero and the form is strictly negative there. Holds.
The note claims only this transfer-crossing form. It explicitly does not deny other reflection
set-ups. The scope is right. (K17) works in frame 1 and needs no second frame. This is correct.

**Verdict, item 5: HOLDS.**

## 6. (K21), encode-any-q, the rescaling test, (K24), (K25), 2I

**(K21).** D(u) = log Q_c(u) − log Q_f = H_f − H_c(u). Q_c ≤ 1 gives H_c ≥ 0.
Q_c = (1+R_c)/2 ≥ R_c gives H_c ≤ F_c ≤ 2Ne^{-ℓ²} on J ⊂ [0,r].
Hence |D(u) − H_f| ≤ 2Ne^{-ℓ²}, and ∂_αD = ∂_α log Q_c = −G_c. Holds.

**Encode any q.** Replace Q_f by q ∈ [1/2,1]. Then D = log Q_c(α) − log q, with |D| < log 2
(equality needs Q_c = 1 and q = 1/2, and Nc_*α/2 > log 2 is strict anyway).
The proof of (K17) goes through unchanged. Holds.

**Rescaling test.** Multiply every twisted-sector integrand by e^{−Mβ}.
Normalized conditional laws, and hence every commutator contraction, are unchanged.
R_f becomes e^{−Mβ}R_f ∈ (0,1]. The integrated response ∫_0^βG = −log Q_f becomes
−log[(1+e^{−Mβ}R_f)/2] → log 2 as M → ∞, for fixed β > 0.
The note says the modified family is not Wilson. The test is logical only. Holds.
(Notation: M here is unrelated to the M of (LC) in §4.2.)

**(K23).** This differentiates a finite positive integral; dν_k is the marginal law of ξ. Holds.

**(K24).** R_f > 64θ ⟺ (1+R_c)e^{−D} > 1+64θ ⟺ D < log((1+R_c)/(1+64θ)).
The generic bound is D ≤ log Q_c + log 2 = log(1+R_c). It exceeds the (K24) threshold, so it
gives no margin. Holds. The note's circularity remark agrees with `gap-ext-astra.md` §3.3.

**(K25).** For irreducible ρ of a compact group (including counting measure on a finite group):
∫ρ(A)Xρ(A)^*dA = (trX/d)I. Then ∫ρ([A,B]) = d^{-1}∫χ(B)ρ(B)^*dB = d^{-2}I,
by orthogonality of matrix coefficients. Holds.
*2I contains i, j.* The vertices (0,±1,±φ), (±1,±φ,0), (±φ,0,±1) form a regular icosahedron.
The half-turn about the x-axis sends (x,y,z) to (x,−y,−z). It maps each of the three families
to itself; the y- and z-axis half-turns do the same. So they lie in the rotation group A5.
Their SU(2) lifts are ±i, ±j, ±k. Then [i,j] = ij(−i)(−j) = (ij)² = k² = −1,
independent of the lift signs. Holds.
*Irreducibility.* i acts with the distinct eigenvalues ±i. jij^{-1} = −i, so j swaps the two eigenlines.
No line is invariant. Holds.
*Odd dimension ≥ 2.* A 1-dim ρ has ρ(−1) = ρ([i,j]) = 1. So centre-odd irreducibles have d ≥ 2
and eigenvalue d^{-2} ≤ 1/4. The defining rep attains 1/4. So the norm is exactly 1/4. Holds.
*Minorization.* (8) uses only the oscillation ≤ 24β of the exponent relative to product Haar.
It transfers verbatim to the finite group, and so does (9). Holds.
*(LC) failure.* For M > π/(2Δ_G), 1 − tr/2 ≤ π/(2M) < Δ_G forces A_M = B_M = I.
Then [A_M,B_M]^M = I ≠ −I. In U(1) all commutators are 1. Holds.

**Verdict, item 6: HOLDS.**

## 7. (K-RESP) and its implication of (FQ)

**Form.** The fine integrand is (K6)'s second form, so the bracket is D by (K5). Holds.

**Implication.** Assume (K-RESP), so D_+ ≤ e_a/8.
(K18) gives δ_c ≤ 2Ne^{-a²/4^n}, with N ≤ 24a⁴/16^n. We need e_a/4 to dominate this.
e_a/4 is the minimum of 1/384 and K(a)η_*^{a/2}/16. K(a) ≥ C_1 > 0, and η_*^{a/2} decays only
linearly in the exponent. With n fixed the quadratic exponent wins.
So δ_c ≤ e_a/4 for all large dyadic a. Then (K8) and the §1 budget give (FQ) for every
c,d ∈ {a,2a}, β ∈ I, m_2 = 0 and i = 3,4. These are exactly the quantifiers of (FQ) in
`gap-trf-astra.md:121–128`. Holds.
*Minor correction (constant).* (FQ) and (T2) ask K(a) ≤ C_1a^{p_1}. The note sets
K(a) = C_1(1+a)^{p_1}. This satisfies the requirement only after C_1 ↦ 2^{p_1}C_1, for a ≥ 1.
Rename the constant, or write K(a) = C_1a^{p_1}.
The dyadic-only caveat is stated correctly.

**Observation (clarifies scope; not an error).** The implication does not use (K17) or α_Λ.
It uses only D := log Q_c(α) − log Q_f (so (K5) and (K8) are identities) and (K18).
The fine integral in (K-RESP) equals H_f = −log((1+R_f)/2) exactly.
So (K-RESP) ⟺ H_f ≤ H_c(α) + e_a/8, and 0 ≤ H_c(α) ≤ 2Ne^{-ℓ²}.
In other words, (K-RESP) is an (FQ)-strength bound on the fine ratio, up to an area-small
additive term. It is not a reduction of (FQ) to a weaker statement. The note's §6 text at
683–686 says this in substance. It could say it in one sentence.

**Verdict, item 7: HOLDS AFTER CORRECTION** (K(a) constant; see above).

## 8. Is the summary judgement right?

Yes. By (K21), D = H_f − H_c(α) with 0 ≤ H_c ≤ 2Ne^{-ℓ²}.
So |D| (or D_+) ≤ ε forces H_f ≤ ε + 2Ne^{-ℓ²}. Conversely H_f ≤ ε gives D ≤ ε.
For H_f small, H_f = (1−R_f)/2 + O((1−R_f)²).
Hence an exponentially small mismatch is equivalent, up to the coarse error, to an exponentially
small fine positive-average deficit. The encode-any-q statement shows that the scalar
construction carries no information about Q_f. The observation in §7 shows the coarse apparatus
is logically idle in (K-RESP) ⇒ (FQ). The representation relocates the crux; it does not shrink it.

What the note does add is correct and modest:
- the exact signed formula (K5)–(K6) with the R/(1+R) factor and the whole-action covariance;
- a background-uniform inverse (K17) with a trapping interval, covering the crossed pairs in one frame;
- an area-small coarse endpoint (K18);
- a checked seam obstruction (K20);
- a correct demonstration that the 2I group passes the commutator-contraction test.

## Verdict table

| Item | Verdict |
|---|---|
| 1. (K1)–(K8): (K2), (K3) and ε/N scale, (K4), (K5), (K6), (K7) and offset, (K8) and budget | HOLDS (wording: in the (V) clause, "their sum" must mean δ_c+2D_+ ≤ 1/2) |
| 2. (K9) range (1/2,1] in frame 1; (K10) coarse transfer positivity | HOLDS |
| 3. (K11)–(K16): polymer gas, degree 20, 441^k, (4u)^{|X|}, (K13)/(K14), homology ≥ ℓ², factor 2, 8/3, Cauchy, constants | HOLDS (441^k loose: 400^{k−1}; Cauchy bound improvable to (re)^{−k}) |
| 4. (K17)–(K18): inverse, uniformity, analyticity, dyadic, endpoint | HOLDS |
| 5. (K19)–(K20): seam multiplier and strict negativity on C_4 = −1 | HOLDS |
| 6. (K21), encode-any-q, rescaling test, (K23), (K24), (K25), 2I ∋ i,j with [i,j] = −1, irreducibility | HOLDS |
| 7. (K-RESP) ⇒ dyadic (FQ) via (K8), (K18) | HOLDS AFTER CORRECTION (K(a) = C_1(1+a)^{p_1} vs required ≤ C_1a^{p_1}: rename constant) |
| 8. Summary judgement: relocation, not shrinkage | HOLDS |
| §1 READ claims on Kanazawa Theorems 1, 3 | NOT CHECKED (PDF not downloaded) |

No item FAILS.

RESULT: HOLDS AFTER CORRECTION — every hand step in (K1)–(K25) and (K-RESP) checks; the only corrections are a constant rename (K(a)=C_1(1+a)^{p_1} must be absorbed into C_1a^{p_1} for (FQ)) and the wording of the (V) clause of (K8), and the summary is right that the representation relocates the crux, since (K-RESP) is equivalent, up to the area-small coarse term 2Ne^{-ℓ²}, to an (FQ)-strength bound on the fine deficit H_f.
