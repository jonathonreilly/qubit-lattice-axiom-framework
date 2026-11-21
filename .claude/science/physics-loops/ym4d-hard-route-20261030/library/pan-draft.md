# (P-an): the analytic presentation of the step's non-Gaussian exponent — pass 1 (long draft)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), 2026-11-04, one session, written for the lead as pass 1 of the statement (P-an) on which AG1 (the rarity of old large-field regions) now rests, in our proof of T0. Research text. It is not an audit, it grants no status, and no other model has read it. Method: Claude drafts at length, Codex distils, a fresh session referees, then the part is frozen.

No step rests on a computation. Every argument is a one-variable Schwarz or Borel–Carathéodory estimate, an iterated Schwarz lemma on a polydisc, a Cauchy estimate, a parameter integral of a holomorphic integrand under a Borel majorant, a finite telescoping sum, a geometric series, or a count of cubes. Each is meant to be Lean-formalisable.

Credit. The architecture is that of Ethan Sussman and Levent Alpoge (with Claude and Codex as authors of their text): the histories, the large-field operation and what a patch retains, the carriage of kept forms, the island exponent Φ° + [−½q_X + V(X^~)], the sum over healed components and its Mayer expansion, the exempt hull length, the walk-parameter localisation and the hard-core polymer theorem (outline `ym4.tex`, "SA"); the reading of Balaban's step with the conditional fluctuation integral and the product window (complete account, "CA-II"); the s-parameter conditional Gaussian of the three-dimensional manuscript ("Y3"). Tadeusz Balaban's papers (CMP 109 (1987) 249; 116 (1988) 1; 119 (1988) 243; 122 (1989) 175, 355) are the source of the step, the windows, the operator 𝐂, the regions and the operation 𝐑. Jonathan Dimock's expositions (arXiv 1108.1335, 1212.5562, 1304.0705) are the readable versions. The Borel–Carathéodory and Schwarz lemmas are classical; the cluster-expansion criterion is Kotecký and Preiss (CMP 103 (1986) 491), in the form proved in SA L1270–1347.

Line references. **SA L** = `scratchpad/sa/ym4.tex`; **CA-II L** = `scratchpad/sa/ca_II.tex`; **Y3 L** = `scratchpad/sa/YM3_I.tex`; **TT L** = `library/ag1-tt-draft.md`; **IN1 L** = `library/in1-draft.md`; **ST1 L** = `library/st1-draft2.md`; **AS L** = `library/ym4-assembly.md`. I read every cited range in this session, in bounded ranges. Source text is paraphrased with line numbers; quotations are a few words.

Status words: **[proved]** = proved here by hand from the stated inputs; **[input: NAME, owner]** = a statement another submanuscript must supply, stated exactly; **[design]** = a choice of the construction; **[Outstanding]** = not proved.

---

## 0. Summary

**Result.** (P-an) is **proved**, as an implication from named inputs owned by NL1, ST1, LF1, IN1 and BG1 (Theorem P, §8). The part that no owner stated, (d), is proved (§7.6–7.7), by a route different from the one TT §3.3 sketched. Nothing of (P-an)'s own is left Outstanding. The constants: the decay rate in level-(i−1) lattice units is κ_P/M with κ_P := κ/(2c_g) fixed right after κ (c_g a geometric constant, (8.2)); C_π := e^{κ_P}; ρ := R_{i−1}(log θ_{i−1})^{−σ}/8 with q₁ := q − σ, σ := τ_B + 1. Under two exponent floors on q (8.3), two floors on κ̄, one floor on ST1's separation, and one ceiling on g, these constants do not depend on the level, the history, the volume or g.

**What P is (§3).** The step-i integrand, given the retained variables R, is 𝟏_𝒲e^{Φ}. Here Φ is Balaban's exponent (3.25) as CA-II L79979–80013 reads it, together with the dependence of the carried integral operations on the current background (SA L17558–17564). P is Φ minus the Gaussian part −½⟨y, Ay⟩ − ⟨𝐅, y⟩ and minus a constant. It is the sum, over a finite family 𝔉 of carried functions f, of f evaluated at the fluctuated field minus f at y = 0. The family has seven kinds: (W) Balaban's non-quadratic Wilson and Jacobian term and the coupling-profile difference; (S) the strip term; (Z) the δ-elimination factors; (E,R) the regular terms of every level; (B) the boundary terms of every origin, drop-out terms included; (K) the kept forms and kept Jacobians of standing operations, drop-outs included; (I) the exponents of standing islands. Healed components keep no factor (SA L17648). Their effect is in (R) and (B), through the Mayer expansion of SA (2d).

**The mechanism, in four steps.**
1. *Recentring (§5).* Each f, interpolated in walk parameters s, is holomorphic in the fluctuation on a polydisc of radius R_f ≥ R_{i−1} ~ (log θ_{i−1})^q. This radius is far larger than the tube radius r_out + ρ. If f is bounded two-sidedly, Schwarz's lemma bounds |f − f(0)| on the tube by (r_out + ρ)/R_f times its size. If only Re f is bounded above, Borel–Carathéodory gives the same, provided the value f(0) at the real centre is bounded below.
2. *Shells (§6).* Turn on the walk parameters shell by shell around the support of f. The n-th shell difference vanishes when any inner shell parameter vanishes. An iterated Schwarz lemma then gives the factor e^{−κ̄n}. This yields local pieces with exponential decay. It needs no Möbius sum over subsets, so large objects pay no entropy.
3. *Sizes (§7).* Every kind has a per-cube size that is at most polylogarithmic in θ. Objects attached to the live large-field region (islands, kept forms, drop-outs) sit at least ten level-i cells from Λ_i^{pre} (SA L17320–17325). Their influence is screened by e^{−cMŘ_i}. The age factor √(1 + age) of old objects is beaten by the ρ-separation of the layers.
4. *Assembly (§8).* The recentring factor 𝖺 = 4(r_out + ρ)/R_{i−1} → 0 times the polylogarithmic size is at most 1 under a ceiling on g. So C_π can be taken absolute.

**(d), the healed regions (§7.7).** SA's construction keeps no factor for a healed component (SA L17648). The sum over healed families is exponentiated by a Mayer expansion (SA L17968–17997). The mass of a component is defined with the supremum over complex pairs inside the integral (SA L17804; IN1 C.0). So the Kotecký–Preiss criterion holds uniformly on the complex domain of the exterior data. SA's polymer theorem (L1310–1326) then gives a holomorphic logarithm with a two-sided bound, and its terms are zero-free automatically (Theorem D1). For a factor that *is* kept, a standing island, the one-sided (I-8) gives a two-sided bound by Borel–Carathéodory once the centre value is bounded below (Lemma Q, Theorem D2). For a single integrated factor, if some construction kept one, Theorem D3 gives a zero-free polydisc with bounded logarithm. Its radius loses (log θ)^{2𝔭₀+9r}, not (log θ)^{5r} as TT L155 estimated: TT's Borel–Carathéodory step omitted the centre value, −Ψ ≈ ½q_X.

**Design point (§10).** The inner tests on Λ_i^{pre} read free bonds only. This is already SA's design: the approximate fluctuation test and the third test are "evaluated at the bonds of □^{~2} other than the pivot bonds" (SA L17317). This matches Balaban's product window (CA-II L80014–80053). No change to LF1 is needed. The point is compatible with ST1, because all y-dependence of carried activities enters through the fibre shift, where ST1's activities are holomorphic (ST1 L160).

**What changed against TT.** (i) (d) is not a zero-free-tube question for healed regions, since none is kept. It is a uniform-KP statement (Theorem D1). (ii) The Borel–Carathéodory loss includes ½q_X (Lemma Q). (iii) The literal exponential decay in d(b, b') needs the ten-cell gap: SA's class "asserts no decay across an exempt island" (SA L6196). (iv) q₁ = q − τ_B − 1, not q − 5r.

**First input on the path not yet stated by its owner in the form used:** (L), the walk-interpolated presentation of the step-i exponent on 𝕊 × 𝔻_{R_f} (§4.1). NL1(3)–(4) and ST1 Theorem 1 state it in substance for the actual source and the scalar λ, not for the free complex fluctuation as source. It is NL1's content, status [O] with NL1 through (D4). §13 lists the smaller new input statements.

**Line count**: at the end of the file.

---

## 1. The target and the setting

### 1.1 The statement

(P-an) (TT L441, L147). For every history h, level i and value of the retained variables R, the non-Gaussian exponent P of the step-i conditional law of the scaled fluctuation on the free bonds of Λ_i^{pre} is a finite sum Σ_XP_X. Each P_X is holomorphic on the tube 𝒯_ρ of radius ρ ≥ c_ρ(log θ_{i−1})^{q₁} about the window, real on real points, and depends only on the bonds of X. Moreover Σ_{X∋b,b'}sup_{𝒯_ρ}|P_X| ≤ C_πe^{−κd(b,b')}, with C_π independent of the level, the history, the volume and g.

Its use: TT Lemma 3.1 (TT L141–145, [proved] there) turns it into the clause (CL)(P), |∂_bP| ≤ p₁ and ‖P''‖_op ≤ p₂ ≤ a_−/4 on 𝒲. That clause is what Lemma 4.4 and Proposition 4.7 of TT need on the whole of Λ_i^{pre} (TT L158).

### 1.2 Notation

Fix h, a level i ≥ 1 and R. Write ℓ := log θ_{i−1}, g := g_{i−1} = θ_{i−1}^{−1/2}, and 𝔟 := 𝔟_{i−1} = A₁ℓ^{𝔭₀} (TT L13; IN1 L42–43; CA-II L79854). I is the set of free bonds of level i − 1 in Λ_i^{pre} (CA-II L80021–80030), E = (ℝ³)^I and E_ℂ its complexification. The coordinates are y_{b,a}, a = 1, 2, 3, in an orthonormal basis of su(2). The windows satisfy B(0, r_in) ⊂ K_b ⊂ B(0, r_out), with r_out = (5/4)c_N𝔟 (TT L120).

- *Cubes.* 𝒞 is the set of M-cubes of level i − 1, the fine localisation cubes of side M in level-(i − 1) units (SA L14294–14296). d_c is the sup-norm distance between cube indices, so *-adjacent cubes are at distance 1. For sets, d_c(Δ, X) := min_{Δ'∈X}d_c(Δ, Δ') and diam_cX := max d_c. N_n(X) := {Δ : d_c(Δ, X) ≤ n} and S_k(X) := {Δ : d_c(Δ, X) = k}. "Connected" means *-connected. Δ_b is the cube that contains the midpoint of b (fixed tie rule). A cube contains at most 4M⁴ bonds. The bonds of I "in" a cube set K are those b ∈ I with Δ_b ∈ K.
- *Volume sums.* At most (2n + 1)⁴ cubes have d_c(Δ, Δ') = n. So sup_ΔΣ_{Δ'}e^{−a d_c(Δ,Δ')} ≤ S(a) := Σ_{n≥0}(2n + 1)⁴e^{−an}, and S(a) ≤ 2 for a ≥ 6.
- *Polydiscs.* |ζ|_∞ := max_{b,a}|ζ_{b,a}| and 𝔻_r := {ζ ∈ E_ℂ : |ζ|_∞ < r}. The tube is 𝒯_ρ := {ζ : ∃y ∈ 𝒲, |ζ_{b,a} − y_{b,a}| < ρ ∀(b, a)} (TT L141). Since |y_{b,a}| ≤ |y_b| < r_out, we have 𝒯_ρ ⊂ 𝔻_{r_out+ρ}.
- *Walk parameters.* 𝕊 := {s ∈ ℂ^𝒞 : |s_Δ| < e^{κ̄}}, with SA's parameter radius R_s = e^{κ̄} (SA L17903–17906; `c4-order.md` row 9). For a cube set X, 𝕊_X := {s ∈ 𝕊 : s_Δ = 1 for Δ ∈ X}. supp s := {Δ : s_Δ ≠ 0}. For connected X, K_X(s) is the connected component of X ∪ supp s that contains X.
- *The step radius.* R := R_{i−1} := c_Rℓ^q. Here q is the radius exponent of IN1 L44, and c_R := C₁/(4C_𝐂C_H) with C₁ the radius coefficient (`c4-order.md` row 16), C_𝐂 Balaban's 𝐂-norm (TT L124) and C_H := C_{src}E_{κ̄}C_𝒜 the response constant of ST1's (S) at unit source (ST1 L181). So R is the scaled fluctuation radius α_{1,i−1}/g = C₁ℓ^q (IN1 L44), reduced by the reconstruction and response constants.
- *Recentring factor.* 𝖺 := 4(r_out + ρ)/R.
- *Gap and islands.* G := 10LŘ_i, the width in level-(i − 1) M-cubes of ten level-i cells (a level-i cell has side LMŘ_i in level-(i − 1) units). C₀ is the class constant: a standing island's hull lies in a cube of C₀ level-i cells (SA L17575; R2 (R3)).

---

## 2. What the sources say

### 2.1 Balaban's step, as CA-II reads it

- CA-II L79920–79938. After the expansion in A_k, the linearisation and removal of the δ-functions with 𝐂, and the scaling, the exponent is (3.15). It is the quadratic form −½⟨A, C*Δ^{(k)}CA⟩, Balaban's 𝐏^{(k)}, and a brace. The brace holds the differences of 𝐄 + 𝐑 + 𝐁 and of the coupling-profile Wilson term A((1/g²)(·) − 1/g², ·) between the background of the fluctuated field and U_{k+1}. CA-II names these "the six terms with which the Gaussian extraction deals".
- CA-II L79979–80013 (Balaban (3.25)). The conditional integral over A on Λ_{k+1} has exponent −½⟨A, C*ΔCA⟩ − ⟨A, C*ΔCA_k⟩, a term in A_k alone, 𝐏^{(k)}(g_k, (A_k, A)), the brace, and V^{(k)}(S_{k+1}, (A_k, A)). Here A_k is the stored field on Ω_{k+1} ∖ Λ_{k+1}.
- CA-II L79964–79968 (item (g)). On Λ_{k+1} only the small-field characteristic functions of (3.16) remain. Their product is χ^{(k)}(Λ_{k+1}).
- CA-II L80014–80053. The window is the product over the free bonds Λ^{(k)*}_{k+1} (pivot bonds removed) of norm balls of radius 𝔟_k in the scaled variable.

### 2.2 Sussman–Alpoge

- *Tests and regions* (SA L17317–17325). The approximate fluctuation test "is evaluated at the bonds of □^{~2} other than the pivot bonds", and the third test "at the same bonds" (L17317). Ω_t^c = Q_t'^{~2} ∪ P_t'^{~4} ∪ Ŷ^{~8}, Z^{[0]} = bx((Ω_t^c)^{~2} ∪ R_t'^{~}), and Z_t = Λ_t^c is the final Z^{[n]} (L17320–17325). Here Y is the live region.
- *The operation* (SA L17497–17546). Moves are positive kernels (L17499–17510). The strip substitution has a Jacobian that "contributes to the action as a boundary term" (L17526). The only variable integrated on Ω_{j+1} is A on Λ_{j+1}, conditionally on the stored A' (L17528–17531). 𝐓^{(j)} contains the factors z^{(j)} of the δ-elimination (L17534–17537).
- *Carriage* (SA L17558–17564). In a carried integral operation, the tests, gauge factors and δ-functions depend on no background. The kept forms Δ^{loc}_𝔨 and the factors z^{(j)} do: they are functions of a pair near 𝔨, evaluated at the current background. Each change of background produces differences that "localisation turns into boundary terms". A kept-form piece with carrier R has oscillation with respect to the pair at most Cp₀(g_j)²e^{−κd^♮_{j+1}(R)} (L17564).
- *What a patch retains* (SA L17642–17654). A healed component retains nothing once the sum over families has been exponentiated (L17648). An island retains χ^c_kχ_{k,Λ}χ(Λ^{pr})δ_{ax}𝐓'_k(X) as one block under its frame sum while it stands (L17648–17653). A drop-out retains the unreached one-step operations, bare integrals, the core and the failing factor; the terms produced so far "are added to the boundary terms" (L17654).
- *Proposition 2.4* (SA L17656–17662). The minimiser in a box exists, with |∂V_Λ − 𝟏| ≤ C(M)ε.
- *The island exponent* (SA L17822–17826). Φ_ω = Φ°_ω(ξ) + [−½q_X + V(X^~)](ξ; 𝐩). Here q_X = ‖φ^{1/2}D𝖧B‖² ≥ 0 is formed at a real background, |V(X^~)| ≤ C·#{stored sites}, and the full exponent is determined by the pair.
- *The mass* (SA L17804; IN1 L430). 𝖬(i, X) = |W₄|^{−1}Σ_ωe^{c𝗏(ω)}∫sup_{𝐩∈U^c_i}|e^{Φ_ω(ξ;𝐩)}|μ_ω(dξ). The supremum over complex pairs stands inside the integral.
- *(2d)* (SA L17841–18009). The identity at a real point of the tests (L17859–17869) has a nonnegative quadratic term ½‖φ^{1/2}D𝖧B‖² and a remainder 𝖱_X (estimate L17872–17889). Localisation of differences is by walk parameters with |s(Δ)| < e^{κ̄}: "setting a parameter to zero prevents a walk from crossing that cube", and the result is f(U^{old}) − f(U^{new}) = Σ_{Y⊃X}f_Y with |f_Y| ≤ 2𝖺b_fe^{−(κ̄−1)𝔪(X,Y)} (L17903–17920). Near a sharp test a term is analytic only in a switch (L17938–17947). The healed-family sum Σ_𝔛Π_C𝐓'_k(C)exp Σ_YV_𝔛(Y) is taken at fixed exterior data (L17968–17980). After the empty family is factored out, the Mayer expansion converges: log 𝖪 = Σ_Y(V_∅(Y) + 𝐑'_♯(Y)), with |𝐑'_♯(Y)| ≤ Ce^{−(1+c)p₀(g_k)}e^{−(1+β_s/2)κd^♮_k(𝒮';Y)}. The part with no standing object in its domain enters R^{(k)}, and the rest is a boundary term (L17982–17997).
- *Exempt hull* (SA L6191–6197). d^♮_{j,𝖧}(X) minimises M^{−1} times tree length "also over subfamilies 𝖥 ⊂ 𝖧 contained in X". The tree meets each cube outside ∪𝖥 and each member of 𝖥, without filling the members. 𝖧 is the family of standing islands, and the length "asserts no decay across an exempt island". (R23): |B_𝒮(j, X, o)| ≤ 𝖡e^{−κd^♮_j(𝒮;X)} (L6200–6202).
- *Class clause (vi)* (SA L19424). For an island, Φ_ω is Borel in ξ, analytic in 𝐩 and real at real pairs. "The bounds of mass … and of oscillation (2d) hold, the coupling in them being taken at the level at which the island was made." No explicit island oscillation bound is written at the cited places; §7.6 states and proves one.
- *Exponent conditions* (SA L19486–19493). Among them: q − 𝔭₀ > Cr, and q > C𝔭₀ "so that the product of an amplitude and an oscillation of degree 2𝔭₀ remains bounded". That is the recentring mechanism of §5.
- *Polymer theorem* (SA L1270–1347). Under Σ_{Y≁X}|z_Y|e^{a_Y} ≤ a_X, the connected series converges absolutely and e^{L(z)} = Z(z) ≠ 0. If the criterion holds throughout a complex activity domain with a uniform majorant, the series converges locally normally and gives the branch of log Z that vanishes at zero (L1310–1326).
- *Regular gas* (SA L14300–14420). Its potentials obey (UM1) and are holomorphic on declared complex fluctuation boxes. SA *assumes* (UM1) (L14304: "assume").

### 2.3 Y3 and our library

- Y3 L52576–52590. The three-dimensional conditional Gaussian puts s̄ = 1 on Z°^♯, s on the other big cubes of R and 0 outside R. Each coefficient or string is multiplied by the product of s̄ over its big-cube hull, and terms with zero product are omitted. This is the locality structure (L3) of §4.1 below.
- IN1 (I-5) (IN1 L70–78): the step and its error bounds on its box, analyticity and reality preserved. (I-8) (IN1 L90–94): Re Ψ_ω ≤ C_ΨV° on U^c_i. (I-12) (IN1 L112): layered support bounds. Class clauses (ii) and (vi) (IN1 L661, L666). Lemma D.1 (IN1 L673): θ_j/θ_n ≤ 1 + (n − j). Lemma D.3 (IN1 L687): the input bound N_⋆. Lemma D.5 (IN1 L701): the entry routes of 𝖡. Lemma C.11 (IN1 L622): real later arguments lie in the fixed set.
- ST1 Definition 3 (ST1 L160). P ∔ h = (U, A'', 𝐉 + K) with U real fixed. Carried activities are holomorphic on fixed-U fibres. ST1 (S) (ST1 L179–183): 𝔫(h_Y)(b) ≤ C_{src}E_{κ̄}C_𝒜δ_{src}e^{−μd(b,𝒮_v)}, in the weighted distance with ρ-separation of ST1 Definition 1 (ST1 L76). ST1 Theorem 1 (ST1 L40–62): carried compositions are holomorphic for s ∈ 𝔻(Y), |λ| < ϱ_X, with the localised bound (2).
- TT §3.3 (TT L139–158): Lemma 3.1 and the four terms (a)–(d).

---

## 3. P exactly

### 3.1 The conditional density

By TT (CL)(0d) (TT L118), conditionally on R the scaled fluctuation y ∈ E has density Z_R^{−1}𝟏_𝒲(y)e^{Φ(y)}. Here e^{Φ} collects every factor of the step-i integrand on {H_k = h} that depends on y and is not a window indicator. §10 shows that no other y-dependent indicator occurs. Reading Φ from Balaban's (3.25) (CA-II L79979–80013) and SA's carriage (SA L17558–17564):

  Φ(y) = −½⟨y, Ay⟩ − ⟨𝐅, y⟩ + Σ_{f∈𝔉}F_f(𝟏, y) + c(R),   (3.1)

with A := C*Δ^{(i−1)}C compressed to I (TT (CL)(A), from (I-1)), 𝐅 the rows on I of C*Δ^{(i−1)}CA_k (TT L131), and c(R) independent of y. The finite family 𝔉 has seven kinds. For each f, F_f(𝟏, y) is the f-term of the exponent at y: the physical evaluation, all walk parameters equal to 1 (§4.1).

- **(W) Wilson and Jacobian remainder.** Balaban's 𝐏^{(i−1)}(g, (A_k, y)) (CA-II L79920–79938, L79995). It collects the Wilson action at the background of the fluctuated field, the Haar density and the Jacobian of the linearised constraint, less the Gaussian part. The kind also holds the coupling-profile difference A(x(·) − x_{i−1}, U(·)) − A(x(·) − x_{i−1}, U_i) of the brace (CA-II L79920–79935). Its weight is O(1 + k − j) on shells (SA L17886–17888) and it is supported near the boundary of the flowing region (SA L17528–17529). Each f is the contribution of one plaquette or one block of the constraint, and lives in at most 2⁴ cubes.
- **(S) Strip.** V^{(i−1)}(S_i, (A_k, y)) (CA-II L79990–80003): the Jacobian of the strip substitution and the differences of strip quantities that depend on a shifted variable (SA L17526; the "terms of the strip" of SA L17541).
- **(Z) δ-elimination factors.** log z^{(j)}(c)(𝐩) for the coarse bonds c whose factor reads the current background (SA L17534–17537, L17558). This covers the step's own factors, the carried ones near Λ_i^{pre} and those kept by drop-outs (SA L17654; SA L17831 item (iv)).
- **(E, R) Regular terms of every level j ≤ i − 1.** E^{(j)}(X), R^{(j)}(X) at the background of the fluctuated field, minus their values at U_i (the brace of CA-II L79920–79935). This kind contains the healed-family terms 𝐑'_♯(Y) that entered R^{(k)} at a healing level k (SA L17996–17997; §7.7).
- **(B) Boundary terms of every origin** (SA L6185–6188: step, last layer of a regular family, a step remainder beside an island, a stage, exponentiation). This includes the terms produced by drop-outs (SA L17654), the healed-family terms with a standing object in their domain (SA L17997), the stage logarithms (SA L17949–17957), and the localised background differences of carried forms already converted to boundary terms (SA L17562).
- **(K) Kept forms of standing operations.** −½⟨A', Δ^{loc}_𝔨(𝐩)A'⟩ at the current pair, for components 𝔨 of live large-field regions and of drop-outs (SA L17553–17564, L17831 item (iv)), with the stored A' (in R) fixed.
- **(I) Standing islands.** Ψ_ω(ξ; 𝐩) := Φ_ω(ξ; 𝐩) − Φ°_ω(ξ) for each standing island, with its stored variables ξ, its frame r and its internal record ω (all in R) fixed (SA L17648–17653, L17822–17826; IN1 (I-8)).

**Healed components.** A component healed at an earlier level k retains nothing once the healed-family sum is exponentiated (SA L17648). So no kind "healed factor" appears in (3.1). The healed families enter only through the Mayer terms 𝐑'_♯, which (E, R) and (B) contain (SA L17996–17997). §7.7 proves the property (P-an) asks of them.

**Why the stored variables of standing objects are in R.** TT (CL)(0) defines R as all other variables of the level-(i − 1) state. A state is (h, ξ) with ξ the stored variables (SA L17499–17501). The frames r ∈ W₄ are draws (SA L17501–17503), and internal records are outcomes in h. So, given R, each standing block is a pointwise function of y. No integral over a standing object's variables is left inside the conditional law. This is why (I) is an exponent Ψ_ω and not a logarithm of an integral.

**Definition of P.**

  P(y) := Σ_{f∈𝔉}[F_f(𝟏, y) − f₀],  f₀ := F_f(𝟏, 0).   (3.2)

Then Φ = −½⟨y, Ay⟩ − ⟨𝐅, y⟩ + P + const, which is TT's H = ½⟨y, Ay⟩ + ⟨𝐅, y⟩ − P up to a constant that cancels in Z_R. §6 writes P as the finite sum of localised pieces (6.3).

### 3.2 What is not in P

- Tests. The tests of step i on Λ_i^{pre} are the windows (§10). Every other test is a function of R (TT (CL)(0a); R2 (RS-c)). Passed approximate fluctuation tests and Balaban's axial-gauge characteristic function equal 1 on 𝒲 (R2 Theorem 5.4 item 10; CA-II L79886–79895).
- Gauge factors and δ-functions of carried operations depend on no background (SA L17558–17560). They are functions of R.
- Constants in y: they cancel in Z_R.

---
## 4. The inputs

### 4.1 The interpolated presentation (L)

**(L) Walk-interpolated presentation of the step-i exponent** [input: NL1(3)–(4) with ST1 Theorem 1 at the main step (ST1 hypothesis 6); owner NL1; reading flagged below]. For each f ∈ 𝔉 there are a nonempty connected cube set X_f ⊂ 𝒞, a radius R_f ≥ R, and a function F_f : 𝕊_{X_f} × 𝔻_{R_f} → ℂ with:

- (L1) F_f is holomorphic.
- (L2) F_f(𝟏, y) is the f-term of (3.1) at every y ∈ 𝒲.
- (L3) *Locality.* F_f(s, ζ) = F_f(s', ζ') whenever K_{X_f}(s) = K_{X_f}(s') =: K, s = s' on K, and ζ = ζ' on the bonds of I in K.
- (L4) *Reality.* F_f(s, ζ) is real when s and ζ are real.
- (L5) *No fluctuation, no response.* F_f(s, 0) = f₀ for every s ∈ 𝕊_{X_f}.
- (L6) *Bound.* Either (two-sided) |F_f| ≤ ½ω_f on 𝕊_{X_f} × 𝔻_{R_f}, or (one-sided) Re F_f ≤ f₀ + ω_f there. The number ω_f ≥ 0 is the *size* of f. Its *effective size* is ω_f^{eff} := ω_fR/R_f.

*Where (L) comes from.* SA's localisation of a carried term interpolates the term's argument by the response with a parameter s(Δ), |s(Δ)| < e^{κ̄}, for every cube a walk visits. Setting a parameter to zero stops walks through that cube. At s = 0 the term takes its new (unshifted) value (SA L17903–17916). Y3 does the same for the conditional Gaussian: each string is multiplied by the product of s̄ over its big-cube hull, and strings with zero product are omitted (Y3 L52579–52583). This is (L3). (L5) holds because the response to a zero fluctuation is zero, so the parameters have nothing to act on. (L4) holds because the response, the backgrounds and every carried function are real at real arguments (SA (2e), class clauses (ii), (vi); IN1 L661, L666). (L1) with R_f ≥ R is the statement that the step is holomorphic on its product box (NL1(3), AS L276) and that every carried composition stays in its domain (ST1 Theorem 1, ST1 L40–62; (D4)), with the free complex fluctuation ζ as the main-step source. The source of the main step lies in layers t − 2, t − 1 of the old sequence (ST1 Lemma SL(ii), ST1 L700–707). ST1 states holomorphy in (s, λ) for the actual source; (L1) is the same statement with δ_{src} replaced by C_𝐂g|ζ|_∞ for complex ζ.

*The reading flagged.* No owner has stated (L) with the free complex fluctuation, coordinate by coordinate, as the source. It is the form in which NL1's product-box holomorphy is used by the step's own cluster expansion (SA L14314–14315: potentials "holomorphic on their declared complex fluctuation boxes"). (P-an) asks no more of NL1 than the step itself does.

### 4.2 The sizes, kind by kind

Each is an input with its owner. §7 uses them.

- **(L-W)** [input: NL1(3), Balaban's 𝐏^{(k)} as read in CA-II L79919–79937]. For f ∈ 𝔉_W: R_f = R, |X_f| ≤ 2⁴, and ω_f ≤ C_W(M)·g·ℓ^{3q+r}. *Reason:* per plaquette, the non-quadratic remainder of x·a_p at a field of size ≤ C_HgR is ≤ Cx(gR)³ ≤ CgR³, since xg² ≤ 5/4 in the tube. The profile difference has weight O(1 + Ř) near Λ (SA L17886–17888) and oscillation ≤ C(1 + Ř)(ε + gR)gR ≤ CℓʳgR(p₀ + R).
- **(L-S), (L-Z)** [input: NL1(3), LF1(4); SA L17526, L17534–17537]. For f in the strip and δ-elimination kinds near Λ_i^{pre}: R_f = R, and sup_ΔΣ_{f:X_f∋Δ}ω_fe^{κ|X_f|} ≤ C_S + C_z. Both constants are fixed after M and before γ.
- **(L-reg)** [input: IN1 (I-5) and Lemma D.3 = SA L19509, NL1(3); reading]. For f in (E, R): R_f = R and N_{reg} := sup_ΔΣ_{f∈𝔉_{reg}:X_f∋Δ}ω_fe^{κ|X_f|} ≤ 2N_⋆. *Reading:* (D.3) is "everything that the small-field step requires of its input" (SA L19509), that is, the per-cube sizes of the regular terms as the step evaluates them, with forgetting and radius-ratio weights included (IN1 L687–693).
- **(L-B)** [input: (R23) = SA L6200–6202, with NL1(1)]. For f ∈ 𝔉_B with domain X, fix a minimising exempt tree T with family 𝖥 (SA L6191–6195), and take X_f := T ∪ ∪𝖥. This set is connected and contains X, and d^♮(𝒮; X_f) := d^♮(𝒮; X). Then R_f = R and ω_f ≤ 2𝖡e^{−κd^♮(𝒮;X_f)}. The same convention is used for (L-K). Moreover
  (N-B)  N_B^{ent} := sup_ΔΣ_{f∈𝔉_B:X_f∋Δ}e^{−(κ/2)d^♮(𝒮;X_f)} ≤ C_B^{ent}(M)ℓ^{τ_B},
  with τ_B an exponent fixed in the exponent row. (N-B) is the per-cube summability that the step's own polymer majorant B1 needs for its boundary terms (NL1(1), AS L274). Without islands it follows from (R23) when κ/2 exceeds the entropy of connected cube sets. Next to islands, the contracted geometry adds a polynomial factor in Ř: an island's boundary has O(L³Ř³) cubes, and distinct islands are Ř cubes apart. So τ_B ≤ 3r + 1 is the expected value.
- **(L-K)** [input: SA L17564, LF1(4)]. For f ∈ 𝔉_K: ω_f ≤ 2C_Kp₀(g_{j_f})²e^{−κd^♮(𝒮;X_f)}, with j_f the formation level, and the analogue N_K^{ent} ≤ C_K^{ent}(M)ℓ^{τ_B} of (N-B).
- **(L-I)** [input: IN1 (I-8) = LF1(4); SA L17822–17826]. For f ∈ 𝔉_I: Re F_f ≤ C_ΨV°(ω) on its domain, and f₀ = −½q_X(ξ; 𝐩(0)) + V(X^~)(ξ; 𝐩(0)) with |V(X^~)| ≤ C_VV°(ω).
- **(Q)** [input at later real pairs: LF1(4); proved at the main-step point in Lemma Q]. For real pairs 𝐩 in the island's fixed set and ξ on the support of its tests: q_X(ξ; 𝐩) ≤ C_Q(M)Ř_m⁴N_Xp₀(g_m)² + 2, with m the creation level and N_X the number of sites of X counted at their own levels.

### 4.3 Geometry and screening

- **(G-gap)** [SA L17320–17325; owner LF1(2)]. Every cube of Λ_i^{pre} is at d_c ≥ G = 10LŘ_i from the live region 𝒵_{i−1}. *Proof from the source:* Ω_i^c ⊃ Ŷ^{~8} and Λ_i^c = Z_i ⊃ Z^{[0]} ⊃ (Ω_i^c)^{~2} ⊃ Ŷ^{~10}, in level-i cells. A level-i cell is LŘ_i M-cubes of level i − 1 wide. Standing islands, live components and drop-outs lie in 𝒵_{i−1}.
- **(G-isl)** [SA L17575; R2 (R3); owner LF1(2)]. A standing island's level-(i − 1) hull lies in a cube of C₀ level-i cells. So its read set X^~ (hull plus one layer of M-cubes) has diam_c ≤ C₀LŘ_i + 2.
- **(G-sep)** [owner LF1(2)]. Distinct standing-island hulls are at d_c ≥ Ř_i. *Reason:* they are distinct components of Z_{i−1}. Components are separated by at least one level-(i − 1) cell, which is Ř_{i−1} ≥ Ř_i cubes wide (the boxing map bx repeats until no two boxes touch, SA L17325).
- **(S), (sep)** [ST1 L179–183 and ST1 Definition 1, ST1 L76]. The regional shift obeys 𝔫(h)(b) ≤ C_{src}E_{κ̄}C_𝒜δ_{src}e^{−μd_w(b,𝒮)}, where d_w is ST1's weighted distance (density l(x)^{−1}). Consecutive regions are ρ_{sep}-separated: dist_∞(Ω_{l+1}, Ω_l^c) ≥ ρ_{sep}ξ_l. We assume μρ_{sep} ≥ 2 [design: a floor on ρ_{sep} after μ, both fixed before κ in ST1's order, ST1 §4].

### 4.4 Healed families

- **(H-Mayer)** [input: LF1(5), ⟦LF-2.10⟧ open (AS L298); SA L17959–17997]. At a healing level k and fixed exterior data e in the complex domain 𝒟_{ext}, the healed-family sum divided by exp Σ_YV_∅(Y) equals Ξ(e) = Σ_ΓΠ_{γ∈Γ}z_γ(e). Γ runs over finite families of pairwise compatible polymers, compatible meaning disjoint supports. Each polymer γ contains at least one healed component. Each activity is an integral

  z_γ(e) = ∫Π_{C∈γ}μ_C(dξ_C)·e^{Σ_{C∈γ}Φ_C(ξ_C;𝐩_C(e,ξ))}·W_γ(e, ξ),

  with W_γ a finite product of factors (e^{δV_𝔛(Y)} − 1), holomorphic in e for fixed ξ, Borel in ξ, real at real (e, ξ). 𝒟_{ext} is the set of exterior data at which every pair 𝐩_C(e, ξ) lies in C's fixed set U^c_k(C^~, α_{0,k}, α_{1,k}) and every V_𝔛(Y) is in its domain.
- **(KP-h)** [input: LF1(5) with IN1 Theorem C.8; SA L17982–17989]. With ẑ_γ := ∫Π_Cμ_C(dξ_C)·sup_{e∈𝒟_{ext}}|e^{ΣΦ_C}W_γ| (an upper integral, majorised by a Borel function as in IN1 Theorem C.8 Step 1), there is a(·) ≥ 0 with Σ_{γ'≁γ}ẑ_{γ'}e^{a(γ')} ≤ a(γ), and a(γ) ≤ Ce^{−(1+c)p₀(g_k)}e^{−(1+β_s/2)κd^♮_k(𝒮';γ)} for the rooted sums. *Reason:* SA states that each nonempty polymer contains a healed component whose mass supplies e^{−(2−c)p₀(g_k)}, that the other local factors are prepaid by the mass, and that the connected expansion converges (SA L17982–17989). The mass is defined with the supremum over complex pairs *inside* the integral (SA L17804; IN1 L430). So the majorant ẑ_γ is the one that bound controls, uniformly in e ∈ 𝒟_{ext}.

---

## 5. Analytic lemmas

### 5.1 One variable

**Lemma 5.1 (Schwarz).** Let φ be holomorphic on {|t| < T} with φ(0) = 0 and |φ| ≤ B. Then |φ(t)| ≤ B|t|/T. [proved; classical]

*Proof.* ψ(t) := φ(t)/t extends holomorphically to t = 0. For |t| ≤ T' < T the maximum principle on {|t| ≤ T'} gives |ψ(t)| ≤ B/T'. Let T' ↑ T. ∎

**Lemma 5.2 (Borel–Carathéodory).** Let φ be holomorphic on {|t| < T} with φ(0) = 0 and Re φ ≤ A, A ≥ 0. Then |φ(t)| ≤ 2A|t|/(T − |t|) for |t| < T. [proved; classical]

*Proof.* Fix η > 0 and put A' := A + η > 0. Then Re φ < A' everywhere, so |2A' − φ| > |φ|, since |w|² − |2A' − w|² = 4A'(Re w − A') < 0. Hence χ := φ/(2A' − φ) is holomorphic on the disc, |χ| < 1 and χ(0) = 0. Lemma 5.1 gives |χ(t)| ≤ |t|/T. From φ = 2A'χ/(1 + χ) we get |φ| ≤ 2A'|χ|/(1 − |χ|) ≤ 2A'|t|/(T − |t|). Let η ↓ 0. ∎

### 5.2 Recentring on a polydisc

**Lemma 5.3 (recentring).** Let F be holomorphic on 𝔻_{R_f} ⊂ E_ℂ with F(0) =: f₀ real. Let 0 < r ≤ R_f/2.
(a) If |F| ≤ ½ω on 𝔻_{R_f}, then sup_{𝔻_r}|F − f₀| ≤ ωr/R_f.
(b) If Re F ≤ f₀ + ω on 𝔻_{R_f}, then sup_{𝔻_r}|F − f₀| ≤ 4ωr/R_f.
In both cases sup_{𝔻_r}|F − f₀| ≤ (4r/R)ω^{eff} whenever R_f ≥ R and ω^{eff} = ωR/R_f. [proved]

*Proof.* Fix ζ with 0 < |ζ|_∞ < r and put u := ζ/|ζ|_∞. Then tu ∈ 𝔻_{R_f} for |t| < R_f. Let φ(t) := F(tu) − f₀, so φ(0) = 0. (a) |φ| ≤ ω, and Lemma 5.1 at t = |ζ|_∞ gives |F(ζ) − f₀| ≤ ω|ζ|_∞/R_f. (b) Re φ ≤ ω, and Lemma 5.2 gives |φ(|ζ|_∞)| ≤ 2ω|ζ|_∞/(R_f − |ζ|_∞) ≤ 4ωr/R_f. ∎

### 5.3 An iterated Schwarz lemma

**Lemma 5.4.** Let D be holomorphic on the polydisc {t ∈ ℂ^m : |t_k| < T for all k}, with |D| ≤ B and D(t) = 0 whenever some t_k = 0. Then |D(t)| ≤ BΠ_k(|t_k|/T). In particular |D(1, …, 1)| ≤ BT^{−m} for T > 1. [proved]

*Proof.* Induction on m. For m = 1 this is Lemma 5.1. For m ≥ 2, fix t' = (t₂, …, t_m). The function t₁ ↦ D(t₁, t') vanishes at 0 and is bounded by B, so D(t) = t₁D̃(t) with D̃ holomorphic: the quotient is holomorphic in t₁ by Lemma 5.1's proof and jointly holomorphic by Cauchy's integral formula in t₁. As in Lemma 5.1, |D̃| ≤ B/T. D̃ vanishes whenever some t_k = 0 with k ≥ 2, since D does and t₁ ≠ 0 there; continuity covers t₁ = 0. Apply the induction hypothesis to t' ↦ D̃(t₁, t') with bound B/T. ∎

### 5.4 Parameter integrals

**Lemma 5.5.** Let (Ξ, μ) be a σ-finite measure space, 𝒪 ⊂ ℂ^n open, and u: Ξ × 𝒪 → ℂ such that u(ξ, ·) is holomorphic for every ξ, u(·, e) is measurable for every e, and |u(ξ, e)| ≤ m(ξ) for all e ∈ 𝒪, with m Borel and ∫m dμ < ∞. Then U(e) := ∫u(ξ, e)μ(dξ) is holomorphic on 𝒪. If u is real at real (ξ, e), so is U. [proved; standard]

*Proof.* U is continuous by dominated convergence. Fix a closed polydisc P ⊂ 𝒪 and a coordinate direction. On each complex line in P the contour integral of u(ξ, ·) over a triangle vanishes (Goursat). By Fubini, which applies since |u| ≤ m, so does that of U. Morera's theorem in each variable and Hartogs' theorem (or Osgood's lemma, since U is continuous) give joint holomorphy. ∎

---

## 6. The shell decomposition

Fix f ∈ 𝔉 with data (X_f, R_f, F_f, ω_f) as in (L). Let r ≤ R_f/2 and o_f(r) := sup{|F_f(s, ζ) − f₀| : s ∈ 𝕊_{X_f}, |ζ|_∞ ≤ r}. By (L5), F_f(s, ·) has value f₀ at 0 for every s, and by (L4) f₀ is real. Lemma 5.3, applied to F_f(s, ·) for each fixed s, gives

  o_f(r) ≤ (4r/R)ω_f^{eff}.   (6.1)

For n ≥ 0 let s^{(n)} ∈ 𝕊_{X_f} be the indicator of N_n(X_f) (so s^{(0)} = 𝟏_{X_f}), and define

  g_{−1}^f(ζ) := F_f(s^{(0)}, ζ) − f₀,  g_n^f(ζ) := F_f(s^{(n+1)}, ζ) − F_f(s^{(n)}, ζ) (n ≥ 0).

**Proposition 6.1 (shells).** [proved from (L)]
(a) F_f(𝟏, ζ) − f₀ = Σ_{n≥−1}g_n^f(ζ). Only finitely many terms are nonzero.
(b) g_n^f is holomorphic on 𝔻_{R_f} and real on real points.
(c) g_n^f depends only on the coordinates of the bonds of I in N_{n+1}(X_f), with N_0 := X_f for n = −1. It vanishes identically if there is no such bond.
(d) On 𝔻_r: |g_{−1}^f| ≤ o_f(r), and |g_n^f| ≤ 2o_f(r)e^{−κ̄n} for n ≥ 0.

*Proof.* (a) The torus is finite, so s^{(n)} = 𝟏 for n ≥ n₀, the d_c-diameter of the torus. The sum telescopes to F_f(s^{(n₀)}, ζ) − f₀ = F_f(𝟏, ζ) − f₀. (b) From (L1) and (L4), since s^{(n)} is real. (c) Distance to X_f changes by at most 1 between *-adjacent cubes, and X_f is connected, so N_n(X_f) is connected. Hence K_{X_f}(s^{(n)}) = N_n(X_f). By (L3), F_f(s^{(n)}, ζ) depends only on ζ on the bonds of I in N_n(X_f) ⊂ N_{n+1}(X_f). If no bond of I lies in N_{n+1}(X_f), then g_n^f is constant in ζ, and by (L5) the constant is f₀ − f₀ = 0.
(d) The bound on g_{−1}^f is the definition of o_f(r). Let n ≥ 0. For t ∈ ℂ^n and u ∈ ℂ, let σ(t, u) ∈ 𝕊_{X_f} be 1 on X_f, t_k on S_k(X_f) for 1 ≤ k ≤ n, u on S_{n+1}(X_f), and 0 beyond. Put D(t) := F_f(σ(t, 1), ζ) − F_f(σ(t, 0), ζ) for |t_k| < e^{κ̄}. Then D(1, …, 1) = g_n^f(ζ). D is holomorphic by (L1), and |D| ≤ 2o_f(r) on 𝔻_r because each term differs from f₀ by at most o_f(r). Suppose t_k = 0 for some k ≤ n. Every chain of adjacent cubes from X_f to S_{n+1}(X_f) passes through S_k(X_f), where σ vanishes. So K_{X_f}(σ(t, u)) ⊂ N_{k−1}(X_f) for both u = 0 and u = 1. The two parameter vectors coincide on that set, so by (L3) D(t) = 0. Lemma 5.4 with T = e^{κ̄} gives |g_n^f(ζ)| ≤ 2o_f(r)e^{−κ̄n}. ∎

Write X_{f,n} := {b ∈ I : Δ_b ∈ N_{n+1}(X_f)} (and X_{f,−1} := {b ∈ I : Δ_b ∈ X_f}). Then

  P = Σ_{f∈𝔉}Σ_{n≥−1}g_n^f = Σ_XP_X,  P_X := Σ_{(f,n): X_{f,n}=X}g_n^f.   (6.3)

This is a finite sum, by (a) and the finiteness of 𝔉. Each P_X is holomorphic on 𝔻_R ⊃ 𝒯_ρ, real on real points, and depends only on the bonds of X.

*Why shells and not subsets.* SA's own localisation (SA L17913–17916) and the Möbius form f = Σ_{Y⊃X}f_Y run over all sets Y ⊃ X_f. For an X_f with many boundary cubes, the number of such Y with |Y ∖ X_f| = n is about (81|X_f|)ⁿ/n!. The total is then e^{c|X_f|} with c ≈ 81(D + 1)²e^{−(κ̄−2)}. That is harmless for a class polymer, whose size carries e^{−κ|X_f|}. It is not harmless for a standing island, whose size is about Ř⁴ cubes and whose bound carries no such weight. The shells give the same decay with no entropy factor, since each shell is a single parameter (Proposition 6.1(d)).

---
## 7. Sizes, kind by kind

§8 needs a single per-cube quantity. For a cube Δ put

  N^♮(Δ) := Σ_{f∈𝔉}ω_f^{eff}exp(κ_P·diam_cX_f − (κ̄/2)·d_c(Δ, X_f)),  N^♮ := sup_{Δ∈Λ_i^{pre}}N^♮(Δ),   (7.1)

with κ_P from (8.2). This section bounds N^♮ by a sum over the kinds. Write 𝔉° := 𝔉_W ∪ 𝔉_S ∪ 𝔉_Z ∪ 𝔉_{reg} for the kinds with ordinary decay.

### 7.1 Kinds with ordinary decay: (W), (S), (Z), (E, R)

**Lemma 7.1.** Σ_{f∈𝔉°}ω_f^{eff}e^{κ_Pdiam_cX_f − (κ̄/2)d_c(Δ,X_f)} ≤ S(κ̄/2)·(N_W + C_S + C_z + 2N_⋆), where N_W := sup_ΔΣ_{f∈𝔉_W:X_f∋Δ}ω_fe^{κ|X_f|} ≤ 4⁶M⁴e^{16κ}C_W(M)gℓ^{3q+r}. [proved from (L-W), (L-S), (L-Z), (L-reg)]

*Proof.* For f ∈ 𝔉°, R_f = R, so ω^{eff} = ω. X_f is connected, so diam_cX_f ≤ |X_f| − 1, and κ_P ≤ κ gives e^{κ_Pdiam_cX_f} ≤ e^{κ|X_f|}. Also e^{−(κ̄/2)d_c(Δ,X_f)} ≤ Σ_{Δ''∈X_f}e^{−(κ̄/2)d_c(Δ,Δ'')}. Exchanging the sums, the left side is at most Σ_{Δ''}e^{−(κ̄/2)d_c(Δ,Δ'')}Σ_{f∈𝔉°:X_f∋Δ''}ω_fe^{κ|X_f|}. The inner sum is at most the sum of the four per-cube constants, by the inputs. The outer sum is at most S(κ̄/2). For N_W: a cube meets at most 6·(2M)⁴ plaquettes, each f ∈ 𝔉_W has |X_f| ≤ 2⁴, and ω_f ≤ C_W(M)gℓ^{3q+r} by (L-W). ∎

### 7.2 Boundary terms, including those beside islands and those from drop-outs

**Lemma 7.2 (geometry of exempt domains).** Let T be a set of cubes outside the islands and 𝖥 a family of standing-island hulls, such that the graph whose vertices are T and the members of 𝖥, with adjacency as edges, is connected (SA L6191–6195). Put X := T ∪ ∪𝖥 and |T| = d^♮ + 1. Assume Ř_i ≥ 3. Then [proved from (G-isl), (G-sep), (G-gap)]:
(a) diam_cX ≤ (2 + 2C₀L)|T| + (C₀LŘ_i + 4)·𝟏{𝖥 ≠ ∅};
(b) if 𝖥 ≠ ∅, then for every cube Δ of Λ_i^{pre}: G ≤ d_c(Δ, X) + 1 + (2 + 2C₀L)|T|.

*Proof.* (a) Two cubes of X are joined by a path in the tree graph. Walking it costs one step per tree cube and at most diam(H) + 2 ≤ C₀LŘ_i + 4 per member H on the path, by (G-isl). Distinct members are at d_c ≥ Ř_i by (G-sep). Between two consecutive members, a simple path in the tree graph therefore uses at least Ř_i − 1 tree cubes. So the number k of members on the path satisfies (k − 1)(Ř_i − 1) ≤ |T|. The length is at most |T| + k(C₀LŘ_i + 4) ≤ |T| + (1 + |T|/(Ř_i − 1))(C₀LŘ_i + 4). Since (C₀LŘ_i + 4)/(Ř_i − 1) ≤ 1.5C₀L + 2 ≤ 2C₀L + 1 for Ř_i ≥ 3 and C₀L ≥ 2 (L ≥ 27), this is at most (2 + 2C₀L)|T| + C₀LŘ_i + 4. (b) Let H ∈ 𝖥 and let x ∈ X be the cube nearest Δ. By (G-gap), G ≤ d_c(Δ, H) ≤ d_c(Δ, x) + 1 + (length of a tree-graph path from x to H, excluding H). That path costs at most (2 + 2C₀L)|T| by the count in (a). ∎

**Lemma 7.3.** Put c_g := (2 + 2C₀L)(1 + C₀/10) and κ_P := κ/(2c_g) (8.2). If κ̄ ≥ 4κ_PC₀, then
Σ_{f∈𝔉_B}ω_f^{eff}e^{κ_Pdiam_cX_f − (κ̄/2)d_c(Δ,X_f)} ≤ 2𝖡e^{κ}S(κ̄/4)N_B^{ent} ≤ 2𝖡e^{κ}S(κ̄/4)C_B^{ent}(M)ℓ^{τ_B}. [proved from (L-B), (N-B), Lemma 7.2]

*Proof.* Let f ∈ 𝔉_B with domain X_f, exempt tree T and family 𝖥. Write d := d_c(Δ, X_f). If 𝖥 = ∅, Lemma 7.2(a) gives κ_Pdiam ≤ (κ/2)|T|. If 𝖥 ≠ ∅, (a) and (b) give

  diam_cX_f ≤ (2 + 2C₀L)|T| + (C₀/10)G + 4 ≤ (2 + 2C₀L)|T| + (C₀/10)(d + 1 + (2 + 2C₀L)|T|) + 4 = c_g|T| + (C₀/10)d + C₀/10 + 4.

In both cases κ_Pdiam_cX_f ≤ (κ/2)|T| + (κ_PC₀/10)d + κ_P(C₀/10 + 4), and κ_P(C₀/10 + 4) ≤ κ/2 because (C₀/10 + 4)/(1 + C₀/10) ≤ 4 and 2 + 2C₀L ≥ 4. Since κ_PC₀/10 ≤ κ̄/4, we get e^{κ_Pdiam − (κ̄/2)d} ≤ e^{κ/2}e^{(κ/2)(d^♮+1)}e^{−(κ̄/4)d}. By (L-B), ω_f^{eff} ≤ 2𝖡e^{−κd^♮}. So the summand is at most 2𝖡e^{κ}e^{−(κ/2)d^♮(𝒮;X_f)}e^{−(κ̄/4)d_c(Δ,X_f)}. Sum as in Lemma 7.1, with e^{−(κ̄/4)d_c(Δ,X_f)} ≤ Σ_{Δ''∈X_f}e^{−(κ̄/4)d_c(Δ,Δ'')}, and use (N-B). ∎

Drop-out terms are covered here. The terms a drop-out has produced up to its failure "are added to the boundary terms" (SA L17654), so they are elements of 𝔉_B with origin "stage" or "step" (SA L6185–6188) and obey (R23). The factors a drop-out keeps, its kept forms and Jacobians at the current background (SA L17831 item (iv)), are elements of 𝔉_K and 𝔉_Z (§7.3). Its tests and its failing factor 1 − χ depend on no background (SA L17558–17560) and are functions of R.

### 7.3 Objects attached to the live region: screening

These are the kinds (K) and (I), together with the (Z)-factors carried by standing operations. Each such f is formed at some level m ≤ i − 1, on a domain whose bonds lie in layers j ≤ m of the label of its formation. It is read at the current background on a set X_f inside the read sets of the live region 𝒵_{i−1}. So, by (G-gap), d_c(Δ, X_f) ≥ G − 2 for every cube Δ of Λ_i^{pre}.

**Lemma 7.4 (screening).** Assume (S) and (sep) with μρ_{sep} ≥ 2, and the frame bound θ_j/θ_{i−1} ≤ 1 + (i − 1 − j) (IN1 Lemma D.1). Let f be attached to the live region, formed at level m, with domain radii α_{1,j} on the layer of level j (room fraction c_{room} ∈ (0, 1]). Define R_f as the largest radius such that, for |ζ|_∞ < R_f and s ∈ 𝕊_{X_f}, the regional shift caused by the source ζ stays within half the room at every bond that f reads. Then

  R/R_f ≤ C_{scr}·(ℓ/ℓ_m)^q·e^{−5μLMŘ_i},  C_{scr} := 2^{q−1}/c_{room}.

[proved from (S), (sep), (G-gap), IN1 Lemma D.1; (S) applied with δ_{src} = C_𝐂g|ζ|_∞]

*Proof.* Let b be a bond that f reads, in a layer of level j ≤ m. By (S), the shift at b from the source ζ is at most C_{src}E_{κ̄}C_𝒜C_𝐂g|ζ|_∞e^{−μd_w(b,𝒮)}. Here 𝒮 ⊂ Λ_i^{pre}'s rows (ST1 Lemma SL(ii)). The factor E_{κ̄} covers complex s (ST1 L183). The weighted distance from 𝒮 to b is at least the larger of two quantities. First, the gap: (G-gap) gives at least 10LMŘ_i level-(i − 1) units, and passing through layers of lower level only increases d_w, since its density is l(x)^{−1}. Second, the layers crossed: the path descends from layer i − 1 to layer j, and each crossing of a band Ω_l ∖ Ω_{l+1} of width at least ρ_{sep}ξ_l adds at least ρ_{sep}, by (sep). So d_w ≥ ½(10LMŘ_i + ρ_{sep}(i − 1 − j)). The room at b is c_{room}α_{1,j}. Requiring the shift to be at most half the room for all such b gives

  R/R_f ≤ max_b 2C_{src}E_{κ̄}C_𝒜C_𝐂gR·e^{−μd_w}/(c_{room}α_{1,j}).

Now gR/α_{1,j} = (gR/α_{1,i−1})(α_{1,i−1}/α_{1,j}). Here gR/α_{1,i−1} = c_R/C₁ by §1.2, and α_{1,i−1}/α_{1,j} = (g/g_j)(ℓ/ℓ_j)^q ≤ (1 + (i − 1 − j))^{1/2}(ℓ/ℓ_j)^q by IN1 L44 and Lemma D.1. With A := i − 1 − j, (1 + A)^{1/2}e^{−(μ/2)ρ_{sep}A} ≤ (1 + A)^{1/2}e^{−A} ≤ 1. Finally θ_j ≥ θ_m − c₅ (the frame (F), IN1 L49), so ℓ_j ≥ ℓ_m − 1 ≥ ℓ_m/2 and (ℓ/ℓ_j)^q ≤ 2^q(ℓ/ℓ_m)^q. Collect the factors and use c_R = C₁/(4C_𝐂C_H) with C_H := C_{src}E_{κ̄}C_𝒜 (§1.2): R/R_f ≤ (2C_HC_𝐂c_R/(c_{room}C₁))·2^q(ℓ/ℓ_m)^qe^{−5μLMŘ_i} = C_{scr}(ℓ/ℓ_m)^qe^{−5μLMŘ_i}. ∎

*Why the age does not hurt.* An object formed long ago has domain radii α_{1,j} at its own, weaker coupling. These are smaller than the current α_{1,i−1} by up to √(1 + age) (Lemma D.1). The object sits in layers of its own age. Between it and Λ_i^{pre} the label descends through one ρ_{sep}-separated band per level of age, and (S) charges e^{−μρ_{sep}} per band. So the screening beats the age factor. Without (sep), an old island could be pushed out of its domain by the step's complex fluctuation. §12, route F5, records this.

### 7.4 Kept forms

**Lemma 7.5.** Σ_{f∈𝔉_K}ω_f^{eff}e^{κ_Pdiam_cX_f − (κ̄/2)d_c(Δ,X_f)} ≤ 2^{q+2}C_KC_{scr}A₀²e^{κ}S(κ̄/4)C_K^{ent}(M)ℓ^{2𝔭₀+τ_B}e^{−5μLMŘ_i}. [proved from (L-K), Lemma 7.4, and the argument of Lemma 7.3]

*Proof.* By (L-K) and Lemma 7.4, ω_f^{eff} ≤ 2C_KA₀²ℓ_m^{2𝔭₀}e^{−κd^♮}·C_{scr}(ℓ/ℓ_m)^qe^{−5μLMŘ_i}. Since q ≥ 2𝔭₀ and ℓ_m ≥ ℓ − 1, we have ℓ_m^{2𝔭₀}(ℓ/ℓ_m)^q ≤ 2^qℓ^{2𝔭₀}. The geometric part is that of Lemma 7.3, with N_K^{ent} in place of N_B^{ent}. ∎

### 7.5 Standing islands: Borel–Carathéodory, the centre value, Lemma Q

**Lemma Q (the quadratic part of an island exponent).** Let X be a component that has passed the tests of 𝐑 at level m, and ξ a point on the support of its tests. At the real point of the main step (SA L17859), [proved from SA L17859–17869, LF1(4) and (BX)]

  q_X ≤ C_Q(M)Ř_m⁴N_Xp₀(g_m)² + 2.

At other real pairs of the fixed set U^c_m it holds as the input (Q) (§4.2).

Here (BX) [input: BG1(1) Lipschitz with SA Proposition 2.4, L17656–17662] is the following. On the support, every plaquette p ⊂ supp φ_X of U_{m,X}(e^{ig_mB}V_Λ) has |∂U_p − 𝟏| ≤ C_{bx}(M)ε_m. Every plaquette of U'' in supp(1 − φ_c) on the shell of level j has |∂U''_p − 𝟏| ≤ C_{bx}(M)Ř_j²ε_j, in level-j units. *Reason:* |∂V_Λ − 𝟏| ≤ C(M)ε (SA L17656), the test |B| < δ'_m/g_m (SA L17642) and δ'_m ≤ ε_m, the Lipschitz bound of the background map (BG1(1)), and the layered support bounds (IN1 (I-12), L112).

*Proof.* The identity of SA L17859–17869, at a real point of the tests, reads

  −x_mA(φ_X, U_{m,X}(e^{ig_mB}V_Λ)) − A(x''_m(·), U'') + x_mA(φ_X, U₀) = −A(x_m(·), Ū) − A(x''_mφ_c, U'') − ½q_X + 𝖱_X.

Solve for ½q_X. The Wilson action is linear in its weight, A(w, U) = Σ_pw(p)a_p(U), with a_p ≥ 0. At a real point every weight is nonnegative: x_m > 0, φ ∈ [0, 1], and x''_m ≥ 0 on the shells (SA L17640). So −x_mA(φ_X, U₀) ≤ 0 and −A(x_m(·), Ū) ≤ 0. Also A(x''_m(·), U'') − A(x''_mφ_c, U'') = A(x''_m(1 − φ_c), U''). Hence

  ½q_X ≤ x_mA(φ_X, U_{m,X}(e^{ig_mB}V_Λ)) + A(x''_m(1 − φ_c), U'') + |𝖱_X|.

For SU(2), a_p = f_p²/2 with f_p = |∂U_p − 𝟏| (IN1 L37). By (BX), each plaquette of the first action contributes at most x_mC_{bx}²ε_m²/2 = (x_m/θ_m)C_{bx}²p₀(g_m)²/2 ≤ C_{bx}²p₀(g_m)². On the shell of level j, x''_m = x_m + O(1 + m − j) (SA L17640) and 1 + m − j ≤ 2Ř_m (the window has N_m + 1 = Ř_m + 1 levels). With θ_j ≥ θ_m − c₅, each plaquette contributes at most C_{bx}²Ř_j⁴p₀(g_j)²·(x_m + 2Ř_m)/θ_j ≤ 2C_{bx}²Ř_m⁴p₀(g_j)². Since θ_j ≤ θ_m + B̄(m − j) ≤ 2θ_m for γ small, ℓ_j ≤ ℓ_m + 1 and p₀(g_j) ≤ 2p₀(g_m). The number of plaquettes is at most 6N_X. Finally |𝖱_X| ≤ Cg_m^{1/2} ≤ 1 (LF1(4), AS L297: "a remainder ≤ Cg_k^{1/2}"). Collect: ½q_X ≤ 6N_X(C_{bx}²p₀(g_m)² + 8C_{bx}²Ř_m⁴p₀(g_m)²) + 1, so the claim holds with C_Q(M) := 108C_{bx}(M)². ∎

The site count, from the class rule (SA L17575): X ∩ Z_j lies in a cube of O(1) level-j cells for each of the N_m + 1 levels of the window, and a level-j cell has (MŘ_j)⁴ sites. So N_X ≤ C_{cls}M⁴Ř_m⁵, and V°(ω) ≤ N_X.

**Theorem D2 (the two-sided island bound).** Let f ∈ 𝔉_I be the exponent of a standing island X formed at level m. Then f is of one-sided type (L6), with [proved from (L-I), (Q), Lemma 5.3(b)]

  ω_f = C_ΨV° − f₀ ≤ (C_Ψ + C_V)V° + ½q_X ≤ C_I(M)ℓ_m^{τ_I},  τ_I := 2𝔭₀ + 9r,

and for every s ∈ 𝕊_{X_f} and |ζ|_∞ ≤ r ≤ R_f/2:

  |F_f(s, ζ) − f₀| ≤ 4(r/R_f)ω_f ≤ (4r/R)·C_I(M)C_{scr}2^qℓ^{τ_I}e^{−5μLMŘ_i}.

Here C_I(M) := (C_Ψ + C_V + C_QA₀²)C_{cls}M⁴L⁹ + 1.

*Proof.* F_f(s, ζ) = Ψ_ω(ξ; 𝐩(s, ζ)), and 𝐩(s, ζ) ∈ U^c_m for |ζ|_∞ < R_f by the definition of R_f (Lemma 7.4). (I-8) gives Re F_f ≤ C_ΨV°. By (L5), F_f(s, 0) = f₀ = Ψ_ω(ξ; 𝐩₀) for every s, where 𝐩₀ is the current real pair. It lies in U^c_m by IN1 Lemma C.11. So f₀ = −½q_X + V ≥ −½q_X − C_VV°, and f₀ is real (SA L17822–17826; class clause (vi)). Lemma 5.3(b) applied to ζ ↦ F_f(s, ζ) gives the first inequality. For the size: V° ≤ N_X ≤ C_{cls}M⁴Ř_m⁵, Ř_m ≤ Lℓ_m^r, and Lemma Q (or (Q)) gives ½q_X ≤ C_Q(M)Ř_m⁴N_Xp₀(g_m)² + 1. Since p₀(g_m) = A₀ℓ_m^{𝔭₀}, ω_f ≤ C_I(M)ℓ_m^{2𝔭₀+9r}. The last inequality is Lemma 7.4 together with ℓ_m^{τ_I}(ℓ/ℓ_m)^q ≤ 2^qℓ^{τ_I} for q ≥ τ_I. ∎

This is the oscillation bound that SA's class clause (vi) refers to (SA L19424) without writing it.

**Lemma 7.6.** If κ_P ≤ κ̄/(4C₀), then Σ_{f∈𝔉_I}ω_f^{eff}e^{κ_Pdiam_cX_f − (κ̄/2)d_c(Δ,X_f)} ≤ e^{κ̄}S(κ̄/4)·2^qC_{scr}C_I(M)ℓ^{τ_I}e^{−5μLMŘ_i}. [proved from Theorem D2, (G-isl), (G-gap), (G-sep)]

*Proof.* By (G-isl), diam_cX_f ≤ C₀LŘ_i + 2. By (G-gap), d := d_c(Δ, X_f) ≥ G − 2 = 10LŘ_i − 2, so LŘ_i ≤ (d + 2)/10. With κ_P ≤ κ̄/(4C₀): κ_P(C₀LŘ_i + 2) ≤ (κ̄/4)LŘ_i + κ̄/(2C₀) ≤ (κ̄/40)(d + 2) + κ̄/2. Hence κ_Pdiam − (κ̄/2)d ≤ −(κ̄/4)d + κ̄, and e^{κ_Pdiam − (κ̄/2)d} ≤ e^{κ̄}e^{−(κ̄/4)d}. Distinct islands have disjoint read sets by (G-sep), so each cube lies in at most one X_f. Sum with S(κ̄/4) and Theorem D2 (ω^{eff} = ω_fR/R_f). ∎

### 7.6 Healed regions: the Mayer expansion on the complex domain

**Theorem D1 (healed families have holomorphic two-sided logarithms).** Assume (H-Mayer) and (KP-h) at a healing level k. [proved from (H-Mayer), (KP-h), IN1 Theorem C.8 Step 1, Lemma 5.5 and SA L1310–1326]
(a) Each activity z_γ is holomorphic on 𝒟_{ext} and real at real exterior data.
(b) Ξ(e) ≠ 0 on 𝒟_{ext}. log Ξ, the branch that vanishes when all activities vanish, is holomorphic on 𝒟_{ext} and real at real e.
(c) log Ξ = Σ_Y𝐑'_♯(Y), where 𝐑'_♯(Y) is the sum of the connected cluster terms whose union of supports is Y. Each 𝐑'_♯(Y) is holomorphic on 𝒟_{ext}, real at real e, depends on e only through the data that the polymers of its clusters read, and satisfies the two-sided bound Σ_{Y∋x}sup_{𝒟_{ext}}|𝐑'_♯(Y)| ≤ Σ_{γ∋x}ẑ_γe^{a(γ)}.
(d) So the healed-region contributions to the step-i exponent are two-sided bounded holomorphic functions of the exterior data. No zero-free tube for an individual factor is needed, because none is kept (SA L17648).

*Proof.* (a) By (H-Mayer), z_γ(e) = ∫u_γ(ξ, e)μ_γ(dξ) with u_γ(·, e) Borel, u_γ(ξ, ·) holomorphic on 𝒟_{ext}, and real at real (ξ, e): Φ_C(ξ; ·) is analytic in the pair and real at real pairs (class clause (vi), SA L19424), the pair map e ↦ 𝐩_C(e, ξ) is holomorphic and real, and W_γ is as stated. By (KP-h) and IN1 Theorem C.8 Step 1 there is a Borel majorant m_γ ≥ sup_e|u_γ(·, e)| with ∫m_γ ≤ ẑ_γ + η_γ < ∞. Lemma 5.5 gives (a). (b) (KP-h) is the criterion of SA L1272–1276 for the activities z_γ(e), with the majorant ẑ_γ independent of e ∈ 𝒟_{ext}. SA's theorem (SA L1310–1326) gives absolute convergence of the connected series, e^{L} = Ξ ≠ 0, and, since the criterion holds throughout the complex domain with a uniform majorant, local normal convergence and the branch of log Ξ vanishing at zero. Each term of the connected series is a polynomial in the activities, hence holomorphic by (a), and real at real e. Locally normal convergence preserves holomorphy (Weierstrass). (c) Group the absolutely convergent series by the union of supports. The rooted bound is SA L1314–1320: the sum over clusters containing a given root, weighted by |φ^T|Π|z|, is at most e^{a(γ)}. Summing over roots γ ∋ x gives the bound. (d) By SA L17996–17997, 𝐑'_♯(Y) enters R^{(k)} when no standing object meets its domain, and is a boundary term otherwise. ∎

*Consequence for (P-an).* After the healing level, the 𝐑'_♯ are carried terms of kinds (E, R) and (B). Their two-sided bound holds on 𝒟_{ext}, which is the domain on which (L) at later steps must evaluate them. By (KP-h) the bound is Ce^{−(1+c)p₀(g_k)}e^{−(1+β_s/2)κd^♮}. This is below the class bounds of R^{(k)} and B^{(k)}, since e^{−(1+c)p₀(g_k)} ≤ g_k^{κ₀} for γ small. So (L-reg) and (L-B) include them with no new constant.

**Theorem D3 (a single integrated factor, if one were kept).** Suppose a construction kept, for a passed component X, the integrated factor M_X(𝐩) := |W₄|^{−1}Σ_ω∫e^{Φ_ω(ξ;𝐩)}μ_ω(dξ) as a function of a pair 𝐩, holomorphic on a polydisc 𝔻(𝐩₀, R_X) about a real 𝐩₀ inside U^c_m. Suppose M_X(𝐩₀) > 0, and put Γ_X := sup_ξ(C_ΨV°(ω) − Ψ_ω(ξ; 𝐩₀)) over the support. Then on 𝔻(𝐩₀, R_X/(8Γ_X + 2)), M_X has no zero and |log M_X(𝐩) − log M_X(𝐩₀)| ≤ 0.52, with Γ_X ≤ C_I(M)ℓ_m^{τ_I}. [proved from (I-8), (Q), Lemma 5.2, Lemma 5.5]

*Proof.* Fix 𝐩 with |𝐩 − 𝐩₀| ≤ R_X/(8Γ_X + 2) =: tR_X, and ξ on the support. The function τ ↦ Ψ_ω(ξ; 𝐩₀ + τ(𝐩 − 𝐩₀)/t) − Ψ_ω(ξ; 𝐩₀), for |τ| < 1, vanishes at 0 and has real part at most Γ_X, by (I-8). Lemma 5.2 at τ = t gives |Ψ_ω(ξ; 𝐩) − Ψ_ω(ξ; 𝐩₀)| ≤ 2Γ_Xt/(1 − t) ≤ 1/3. Since Φ° does not depend on the pair, e^{Φ_ω(ξ;𝐩)} = e^{Φ_ω(ξ;𝐩₀)}e^{δ(ξ)} with |δ| ≤ 1/3. At the real pair 𝐩₀, e^{Φ_ω(ξ;𝐩₀)} > 0, so ν₀ := e^{Φ_ω(ξ;𝐩₀)}μ_ω(dξ)/(|W₄|M_X(𝐩₀)), summed over ω, is a probability measure. Then M_X(𝐩)/M_X(𝐩₀) = ν₀(e^δ), and |ν₀(e^δ) − 1| ≤ e^{1/3} − 1 < 0.4. So M_X(𝐩) ≠ 0, the principal logarithm of the ratio is holomorphic (Lemma 5.5 for M_X; composition with Log on {|w − 1| < 0.4}), and |Log| ≤ −log 0.6 < 0.52. The bound on Γ_X is that of ω_f in Theorem D2. ∎

*Comparison with TT §3.3(d).* TT L155 proposes Borel–Carathéodory "into a two-sided bound of order C_ΨV°|ζ − y|/ρ". The correct form is (2|ζ − y|/(ρ − |ζ − y|))·(C_ΨV° − Ψ(y)). The centre value −Ψ(y) = ½q_X − V is of order p₀²N_X by Lemma Q, not O(V°). So the radius loses Γ_X ~ ℓ^{2𝔭₀+9r}, not V° ~ ℓ^{5r}, and TT's q₁ = q − 5r must become q₁ ≤ q − 2𝔭₀ − 9r on that route. Theorem D3 is TT's route with this correction. The construction does not need it, since healed factors are not kept (Theorem D1) and island exponents are screened (Lemma 7.6).

---
## 8. The theorem

### 8.1 Statement

Put

  σ := τ_B + 1,  q₁ := q − σ,  ρ := Rℓ^{−σ}/8 = c_ρℓ^{q₁} with c_ρ := c_R/8,   (8.1)
  c_g := (2 + 2C₀L)(1 + C₀/10),  κ_P := κ/(2c_g).   (8.2)

**Theorem P ((P-an)).** Assume the inputs of §4: (L); (L-W), (L-S), (L-Z), (L-reg), (L-B) with (N-B), (L-K), (L-I), (Q) and (BX); (G-gap), (G-isl), (G-sep), (S) and (sep); (H-Mayer) and (KP-h). Assume the exponent floors

  q ≥ 2𝔭₀ + 9r  and  q > 𝔭₀ + τ_B + 1,   (8.3)

the floors κ̄ ≥ 24 and κ̄ ≥ 4C₀κ_P, and μρ_{sep} ≥ 2. Then there is a ceiling X_P on g (8.5) such that, for every history h, level i with x_{i−1} ≥ X_P, and value of R, the following holds. The exponent P of (3.2) is the finite sum Σ_XP_X of (6.3). Each P_X is holomorphic on 𝔻_R ⊃ 𝒯_ρ, real on real points, and depends only on the bonds of X. For all b, b' ∈ I,

  Σ_{X∋b,b'}sup_{𝒯_ρ}|P_X| ≤ e^{−κ_Pd_c(Δ_b,Δ_{b'})} ≤ e^{κ_P}e^{−(κ_P/M)d(b,b')},   (8.4)

where d is the sup-norm distance between bond midpoints in level-(i − 1) units. So (P-an) holds with q₁ = q − τ_B − 1 > 𝔭₀, c_ρ = c_R/8, C_π = e^{κ_P}, and decay rate κ_P/M. [proved from the inputs listed]

### 8.2 Proof

*Step 1: structure.* (6.3) and Proposition 6.1(a)–(c) give the finite sum, holomorphy on 𝔻_{R_f} ⊃ 𝔻_R, reality and locality. 𝒯_ρ ⊂ 𝔻_{r_out+ρ} ⊂ 𝔻_R, since r_out + ρ < R (§1.2 and Step 2).

*Step 2: the recentring factor.* Put r := r_out + ρ. Since r_out = (5/4)c_NA₁ℓ^{𝔭₀} and R = c_Rℓ^q with q > 𝔭₀, and ρ = Rℓ^{−σ}/8, we have r ≤ R/4 ≤ R_f/2 once ℓ ≥ ℓ₁ := (20c_NA₁/c_R)^{1/(q−𝔭₀)} + 1. By (6.1), o_f(r) ≤ 𝖺ω_f^{eff} with 𝖺 = 4r/R ≤ 5c_NA₁ℓ^{𝔭₀−q}/c_R + ℓ^{−σ}/2. By (8.3), q − 𝔭₀ > σ, so 𝖺 ≤ ℓ^{−σ} for ℓ ≥ ℓ₂ := (10c_NA₁/c_R)^{1/(q−𝔭₀−σ)} + ℓ₁.

*Step 3: one function, two bonds.* Fix f, b, b', and put d_b := d_c(Δ_b, X_f), d_{b'} := d_c(Δ_{b'}, X_f), m_f := max(d_b, d_{b'}). By Proposition 6.1(c), b, b' ∈ X_{f,n} requires n + 1 ≥ m_f, or n = −1 and m_f = 0. If m_f = 0, Proposition 6.1(d) bounds the sum over n of sup_{𝔻_r}|g_n^f| by o_f(r)(1 + 2/(1 − e^{−κ̄})) ≤ 4o_f(r). If m_f ≥ 1, it is at most Σ_{n≥m_f−1}2o_f(r)e^{−κ̄n} ≤ 4e^{κ̄}o_f(r)e^{−κ̄m_f}. In both cases the contribution of f to Σ_{X∋b,b'}sup_{𝒯_ρ}|P_X| is at most 4e^{κ̄}𝖺ω_f^{eff}e^{−κ̄m_f}.

*Step 4: decay in d(b, b').* Choose x, x' ∈ X_f nearest Δ_b, Δ_{b'}. Then d_c(Δ_b, Δ_{b'}) ≤ d_b + diam_cX_f + d_{b'} ≤ 2m_f + diam_cX_f. Since κ_P ≤ κ/2 ≤ κ̄/4,

  κ̄m_f ≥ (κ̄/2)d_b + (κ̄/2)m_f ≥ (κ̄/2)d_b + κ_P(d_c(Δ_b, Δ_{b'}) − diam_cX_f).

So the contribution of f is at most 4e^{κ̄}𝖺·ω_f^{eff}e^{κ_Pdiam_cX_f − (κ̄/2)d_c(Δ_b,X_f)}·e^{−κ_Pd_c(Δ_b,Δ_{b'})}.

*Step 5: sum over f.* Summing over f ∈ 𝔉 gives Σ_{X∋b,b'}sup_{𝒯_ρ}|P_X| ≤ 4e^{κ̄}𝖺N^♮(Δ_b)e^{−κ_Pd_c(Δ_b,Δ_{b'})}, with N^♮ of (7.1). By Lemmas 7.1, 7.3, 7.5 and 7.6, with S(κ̄/2), S(κ̄/4) ≤ 2:

  N^♮ ≤ 2(N_W + C_S + C_z + 2N_⋆) + 4𝖡e^{κ}C_B^{ent}(M)ℓ^{τ_B} + 2^{q+3}C_KC_{scr}A₀²e^{κ}C_K^{ent}(M)ℓ^{2𝔭₀+τ_B}e^{−5μLMŘ_i} + 2^{q+1}e^{κ̄}C_{scr}C_I(M)ℓ^{τ_I}e^{−5μLMŘ_i}.

N_W ≤ 4⁶M⁴e^{16κ}C_W(M)gℓ^{3q+r} → 0 as ℓ → ∞, because g = θ^{−1/2} = e^{−ℓ/2}. The running-minimum rule gives Ř_i ≥ (log min_{j≤i}θ_j)^r ≥ (ℓ − 1)^r, since θ_j ≥ θ_i − c₅ ≥ θ_{i−1} − B̄ − c₅ (frame (F)). With r ≥ 2, ℓ^{c}e^{−5μLM(ℓ−1)^r} → 0 for every fixed c. So there is ℓ₃ such that for ℓ ≥ ℓ₃ the first, third and fourth parts other than N_⋆, C_S, C_z total at most 2, and

  N^♮ ≤ C_Nℓ^{τ_B},  C_N := 2(C_S + C_z + 2N_⋆) + 4𝖡e^{κ}C_B^{ent}(M) + 2.

*Step 6: the ceiling.* With 𝖺 ≤ ℓ^{−σ} and σ = τ_B + 1, we get 4e^{κ̄}𝖺N^♮ ≤ 4e^{κ̄}C_Nℓ^{−1}. Define

  X_P := (5/4)exp(max{ℓ₁, ℓ₂, ℓ₃, 4e^{κ̄}C_N}),   (8.5)

that is, X_P = (5/4)e^{ℓ_∗} with ℓ_∗ := max{ℓ₁, ℓ₂, ℓ₃, 4e^{κ̄}C_N}. In the tube |x − θ| ≤ θ/4 one has θ_{i−1} ≥ (4/5)x_{i−1}, so x_{i−1} ≥ X_P implies ℓ ≥ ℓ_∗. Then 4e^{κ̄}𝖺N^♮ ≤ 1, which gives the first inequality of (8.4). Like every condition of the form sup_{x≥γ^{−2}}h(x) ≤ c with h → 0, it is a ceiling on γ (SA L19485, IN1 L334).

*Step 7: lattice units.* Cubes have side M, so d(b, b') ≤ M(d_c(Δ_b, Δ_{b'}) + 1). This is the second inequality of (8.4). ∎

### 8.3 Remarks

*What (8.4) does not use.* It does not use a lower bound on any normaliser, a zero-free property of any individual factor, or decay across standing islands. Decay across islands is not available: SA L6196 says the class "asserts no decay across an exempt island". (8.4) holds even so, because no bond of I is within G of an island (G-gap), and κ̄ ≫ κ pays the island's diameter (Lemmas 7.3, 7.6).

*The derivative form, without the gap.* Suppose only the bounds on ∂_bP and P'' were wanted, and (G-gap) were dropped. Proposition 6.1(d) and Cauchy estimates give |∂_bF_f| ≤ (o_f/ρ)e^{−κ̄d_b} and ‖∂_b∂_{b'}F_f‖ ≤ (6o_f/ρ²)e^{−κ̄m_f}, by Lemma 5.4 applied to the derivative with shells up to m_f. The Schur sums are then bounded by 𝖺/ρ² times Σ_fω_f^{eff}|X_f|e^{−(κ̄/2)d_c(Δ,X_f)}. This needs only a linear weight |X_f| and no decay across objects. So (CL)(P) has a second, more robust proof. §11 records it.

---

## 9. Uniformity and the order of constants

**Uniformity.** Every bound in Theorem P is a supremum over cubes of a local sum. Its constants are listed below. None depends on the history h, the level i, the torus or the cutoff. The only dependence on g is through ℓ = log θ_{i−1}, and it is removed by the ceiling X_P. Every bound holds for every value of R. So C_π = e^{κ_P} is independent of the level, the history, the volume and g, as (P-an) requires.

**The IN1 constraint.** Every constant that a choice before κ reads must be fixed before κ, be independent of M and κ̄, and contain M only as a lower bound (IN1 L310–336, `c4-order.md`). The constants of this draft, in order:

| Constant | Where | Fixed at | Depends on | Before κ? M, κ̄? |
|---|---|---|---|---|
| D = 80, S(·) | §1.2 | absolute | dimension 4 | yes; independent |
| exponents σ = τ_B + 1, q₁ = q − σ, τ_I = 2𝔭₀ + 9r; floors (8.3) on q | §8.1 | row 2 (r → 𝔭₀ → 𝔭₁ → q) | r, 𝔭₀, τ_B | yes; independent. (8.3) is a floor on q after 𝔭₀, r (row 2 already requires q > C𝔭₀, q − 𝔭₀ > Cr) |
| C₀ | (G-isl) | geometry of the class rule (SA L17575) | the O(1) of single boxes | yes; independent |
| c_g = (2 + 2C₀L)(1 + C₀/10) | (8.2) | with L (row 3) | C₀, L | yes; independent |
| κ_P = κ/(2c_g) | (8.2) | determined right after κ (row 8′) | κ, c_g | read by nothing before κ; independent of M, κ̄ |
| C_π = e^{κ_P} | Thm P | determined after κ | κ_P | independent of M, κ̄ |
| floors κ̄ ≥ 24, κ̄ ≥ 4C₀κ_P | Thm P | row 9 (κ̄ up, after κ) | κ_P, C₀ | floors on κ̄; admissible (SA already has κ̄ ≫ Lκ, SA L19477) |
| μ, ρ_{sep}; μρ_{sep} ≥ 2 | (S), (sep) | ST1's rate (row 5); separation ρ = R₁M₁ (row 6) | ST1 | before κ (ST1 L62, L982); μρ_{sep} ≥ 2 is a floor on ρ_{sep} at row 6 [design] |
| c_{room}, C_{scr} = 2^{q−1}/c_{room} | Lemma 7.4 | ST1's room fraction; exponents | q | before κ; independent |
| c_R = C₁/(4C_𝐂C_H), c_ρ = c_R/8 | §1.2, (8.1) | after the radii (row 16, after M) and E_{κ̄} (after κ̄) | C₁, C_𝐂, C_{src}, E_{κ̄}, C_𝒜 | **no**: after M and κ̄. Read only by R, ρ, 𝖺, so only by ceilings on g |
| C_W(M), C_S, C_z, C_K, C_{bx}(M), C_Q(M), C_I(M), C_{cls}, C_B^{ent}(M), C_K^{ent}(M) | §4.2, §7 | with NL1/LF1's constants, after M, before γ | M, L, A₀ | **no**: they depend on M. Read only by N^♮, hence only by X_P |
| 𝖡, N_⋆ | (L-B), (L-reg) | rows 17, 21 (after M, before γ) | IN1 | read only by X_P |
| decay rate in lattice units κ_P/M | (8.4) | determined after M | κ_P, M | enters TT Lemma 3.1 only through S_d(κ_P/M) ≤ 4M⁴e^{κ_P}S(κ_P), hence only p₂, a ceiling on g (as TT L359 allowed for C_π) |
| X_P | (8.5) | last (rows 21–22) | everything above | a ceiling on g |

*No cycle.* No constant chosen before γ reads c_R, c_ρ, any of the M-dependent constants, κ_P/M or X_P. The constants chosen before κ that this draft introduces (D, the exponents, C₀, c_g, c_{room}, C_{scr}) depend on nothing chosen at or after κ. κ_P and C_π are determined by κ and read by nothing chosen before γ. This is the pattern of R2's C_q (R2 L712) and of TT's c_T, C_π (TT L363).

---

## 10. The design point, and its compatibility with LF1 and ST1

**(DP) Free-bond tests on Λ_i^{pre}** [design; already SA's]. Every test of step i that reads the fluctuation on Λ_i^{pre} is the indicator of a norm ball, or an intersection of norm balls, in the variable of a *single free bond*. No other factor of the step-i integrand that depends on y is an indicator.

*Sources.* Balaban's window is the product over free bonds Λ^{(k)*}_{k+1} (pivot bonds removed) of norm balls (CA-II L80021–80053; Balaban CMP 109 (2.9), CMP 119 (3.16)–(3.20) as read there). SA's approximate fluctuation test "is evaluated at the bonds of □^{~2} other than the pivot bonds", and the third test "at the same bonds" (SA L17317). So (DP) holds in SA's construction as written. TT §3.2 (TT L129) asked LF1 to change its construction if it tested pivot bonds. It does not, so no change is needed.

*Why it matters.* A test of 𝒜 at a pivot bond is a constraint through the nonlinear readout ϱ_b (TT (CL)(ℓ)), and its set need not be convex (TT L129). Here it matters a second time. P must be holomorphic on a polydisc about the window. A pivot-bond test would put an indicator of a non-convex, y-dependent set into e^{Φ}, and no tube would be possible.

*Compatibility with LF1.* Here is every test LF1 makes at step i or later, with what it reads:
- The plaquette tests χ_t(□) read V_t, a function of R (SA L17317).
- The approximate fluctuation test reads free bonds of Λ, and equals 1 on 𝒲 where it passed (R2 Theorem 5.4 item 10).
- The third test reads free bonds of Λ. These are the windows, at the thresholds θ_cδ near ∂Λ and δ inside (SA L17354), smoothed by (SM) with uniforms in R (R2 §5.1).
- The collar test reads stored bonds within ϖ_T of Λ, and the rim test reads cells of Z_t (SA L17356–17357). Both read R.
- The stage tests at δ'_j, the test on B, the last-shell test and χ_{k,Λ}, χ(Λ^{pr}) read the variables of class components inside Z (SA L17585–17653). These are R.
- The decompositions (3.3) and (3.16) of Balaban are the approximate fluctuation test and the windows (CA-II L79879–79886, L79939–79962).
- Tests carried by standing operations depend on no background (SA L17558–17560). They are functions of R.
So LF1 is compatible with (DP) as constructed, and (CL)(0a) (TT L114) holds for tests.

*Compatibility with ST1.* ST1 defines domains and admission. It makes no test. Two points need checking.
- (i) ST1's carried activities are holomorphic on fixed-U fibres and only Borel in the real factor U (ST1 Definition 3, ST1 L160). In the step-i conditional law, the real factor of every pair is the new background, a function of R. The fluctuation enters only through the fibre shift h(ζ) of the main-step substitution P ∔ h (ST1 L160; source in layers t − 2, t − 1 by ST1 Lemma SL(ii), ST1 L700–707). So all y-dependence lies where ST1's activities are holomorphic, which is what (L1) uses.
- (ii) Near a sharp test, SA claims analyticity only in a switch μ_b, not in the stored field (SA L17938–17947). The sharp tests at step i are the windows on Λ_i^{pre}, which read y, not a stored field. A carried term formed before step i has no switch on y, because y did not exist as a variable when it was formed. Terms formed at step i are formed after y is integrated.
So (DP) imposes nothing on ST1 beyond (L). One requirement on ST1 is recorded: ST1 Theorem 1 must be read at the main step with the free complex fluctuation as source, and (S) must hold for complex sources of sup norm < R (§4.1).

*Pivot bonds in the readout.* (DP) concerns tests only. The pivot variables are reconstructed from the free ones by 𝐂 (CA-II L79925; TT (CL)(ℓ)) and by the pivot chart (ST1 Lemma FC). That reconstruction is holomorphic and enters P through (W). This is consistent with (DP).

---

## 11. Consequences for AG1, and corrections to TT

### 11.1 (CL)(P)

TT Lemma 3.1 (TT L141–145) with π_X := sup_{𝒯_ρ}|P_X| and Theorem P gives, for y ∈ 𝒲, in cube form,

  |∂_bP(y)| ≤ √3/ρ,  ‖∂_b∂_{b'}P(y)‖ ≤ 6e^{−κ_Pd_c(Δ_b,Δ_{b'})}/ρ²,  ‖P''(y)‖_op ≤ 24M⁴S(κ_P)/ρ².   (11.1)

So (CL)(P) holds with p₁ := √3/ρ_{i−1} and p₂ := 24M⁴S(κ_P)/ρ_{i−1}², with ρ_{i−1} = c_ρ(log θ_{i−1})^{q₁}. Since P is holomorphic on 𝔻_R ⊃ 𝒲 ∪ (−𝒲), the neighbourhood 𝒩 := 𝔻_R ∩ E is symmetric, as (CL)(P) requires. TT's ceiling list (TT L365–370) is updated: p₂ ≤ a_−/4 reads 24M⁴S(κ_P) ≤ (a_−/4)c_ρ²ℓ^{2q₁}, and (M) uses p₁ = √3/(c_ρℓ^{q₁}). Both are ceilings on g after M.

*The second proof (§8.3).* Without (G-gap), Proposition 6.1(d), Lemma 5.4 and Cauchy estimates give |∂_bP| ≤ (𝖺/ρ)Σ_fω_f^{eff}e^{−κ̄d_c(Δ_b,X_f)} and Σ_{b'}‖∂_b∂_{b'}P‖ ≤ (24M⁴𝖺/ρ²)S(κ̄/2)Σ_fω_f^{eff}|X_f|e^{−(κ̄/2)d_c(Δ_b,X_f)}. These need per-cube sums with the weight |X_f| only. I record this because it makes AG1 independent of the exact island geometry. The literal (P-an) uses (G-gap).

### 11.2 Corrections to TT §3.3

1. TT L155 treats (d) as a zero-free-tube question for a positive healed factor M_X. SA keeps no factor for a healed component (SA L17648). The healed families are exponentiated by a Mayer expansion (SA L17968–17997). Their logarithm is holomorphic and two-sided bounded by KP on the complex exterior domain (Theorem D1). The one-sided (I-8) suffices for this, since a modulus needs only Re Φ.
2. TT L155's Borel–Carathéodory step omits the centre value. The correct loss is Γ_X = C_ΨV° − Ψ(centre) ≤ C_I(M)ℓ^{2𝔭₀+9r} (Lemma Q, Theorem D3), not V° ~ ℓ^{5r}. So "q₁ = q − 5r" is not correct on that route. In Theorem P the island term is screened (Lemma 7.6), and q₁ = q − τ_B − 1.
3. TT L147 allows C_π to depend on M. Theorem P gives C_π = e^{κ_P}, independent of M and κ̄. The M-dependence is in the decay rate κ_P/M (lattice units) and in the ceiling X_P.
4. TT L149 says "only ρ → ∞ is used; no margin of the tube over the window is needed". Theorem P uses more: the ratio 𝖺 = 4(r_out + ρ)/R → 0. That ratio is what makes C_π uniform, and it is the mechanism SA names at L19491 ("the product of an amplitude and an oscillation of degree 2𝔭₀ remains bounded").
5. TT L129's conditional change to LF1 (pivot-bond tests) is not needed (§10).

---

## 12. Routes that fail, and why (recorded; each was met and replaced)

- **F1. A zero-free tube for an integrated factor from the ratio sup|M_X|/M_X(𝐩₀).** Hölder gives sup_{𝔻}|M_X|/M_X(𝐩₀) ≤ e^{Γ}. Lemma 5.1 applied to M_X/M_X(𝐩₀) − 1 then gives a zero-free polydisc of radius only about R_Xe^{−Γ}, with Γ ~ ℓ^{2𝔭₀+9r}M⁴. That is smaller than any power of ℓ. Exact reason: the ratio route is exponential in the exponent's oscillation, and Borel–Carathéodory is linear in it. Replaced by Theorem D3.
- **F2. Borel–Carathéodory from the upper bound alone (TT L155).** It is false as stated. For example Ψ = N·h(𝐩) with Re h ≤ 0 and h(𝐩₀) = −1 has Re Ψ ≤ 0 but oscillation of order N. Exact reason: the bound is (2r/(R − r))(A − Ψ(centre)), and −Ψ(centre) = ½q_X − V is not O(V°). Replaced by Lemma Q, which bounds q_X through SA's (2d) identity.
- **F3. Möbius localisation f = Σ_{Y⊃X_f}f_Y for large objects.** The pieces carry e^{−(κ̄−2)|Y∖X_f|}. The number of Y ⊃ X_f with |Y ∖ X_f| = n is up to (C|X_f|)ⁿ/n!, so the total is exp(Ce^{−κ̄}|X_f|). For an island with |X_f| ≈ C₀⁴L⁴Ř⁴ this beats any polylogarithmic gain. Exact reason: the subsets attach anywhere along a large boundary, and an island's size carries no weight e^{−κ|X_f|}. Replaced by the shells of §6.
- **F4. Exponential decay in d(b, b') from the class bounds alone.** SA's (R23) uses the exempt hull length, which "asserts no decay across an exempt island" (SA L6196). A family obeying (R23) can couple two bonds on opposite sides of an island with size 𝖡e^{−2κ}. Then (8.4) fails by e^{κ_PC₀LŘ}, which is unbounded in g. Exact reason: the class bound is per term and exempt. Replaced by (G-gap), the ten-cell margin of Λ_i^{pre} around the live region (SA L17320–17325), with κ̄ ≫ κ.
- **F5. Old objects at their own radii.** An object formed at level m is holomorphic only where the pair stays within radii α_{1,j}, j ≤ m. These are smaller than α_{1,i−1} by up to √(1 + age) (IN1 Lemma D.1). With the gap alone, the screening e^{−μ·10LMŘ_i} is fixed in terms of the current level while the age is unbounded, so admission fails for ages above about e^{20μLMŘ_i}. Exact reason: the gap does not grow with the age. Replaced by the ρ_{sep}-separation of the layers: the weighted distance grows by ρ_{sep} per level of age (Lemma 7.4).

No statement of (P-an)'s own remains after these replacements.

---

## 13. Status

### 13.1 Statements of this draft

| Statement | Where | Status |
|---|---|---|
| Definition of P, (3.1)–(3.2), the seven kinds | §3 | [design/reading] of CA-II L79919–80013 and SA L17497–17654 |
| Lemma 5.1 (Schwarz) | §5.1 | [proved] |
| Lemma 5.2 (Borel–Carathéodory) | §5.1 | [proved] |
| Lemma 5.3 (recentring) | §5.2 | [proved] |
| Lemma 5.4 (iterated Schwarz) | §5.3 | [proved] |
| Lemma 5.5 (parameter integrals) | §5.4 | [proved] |
| Proposition 6.1 (shells) | §6 | [proved] from (L) |
| Lemma 7.1 (ordinary kinds) | §7.1 | [proved] from (L-W), (L-S), (L-Z), (L-reg) |
| Lemma 7.2 (exempt geometry) | §7.2 | [proved] from (G-isl), (G-sep), (G-gap) |
| Lemma 7.3 (boundary terms, drop-out terms) | §7.2 | [proved] from (L-B), (N-B) |
| Lemma 7.4 (screening) | §7.3 | [proved] from (S), (sep), (G-gap), IN1 Lemma D.1 |
| Lemma 7.5 (kept forms) | §7.4 | [proved] from (L-K), Lemma 7.4 |
| Lemma Q (centre value) | §7.5 | [proved] at the main-step point from SA L17859–17869, LF1(4), (BX); at later real pairs = input (Q) |
| Theorem D2 (two-sided island bound) | §7.5 | [proved] from (L-I), (Q), Lemmas 5.3, 7.4 |
| Lemma 7.6 (islands) | §7.5 | [proved] |
| Theorem D1 (healed families) | §7.6 | [proved] from (H-Mayer), (KP-h), SA L1310–1326 |
| Theorem D3 (a kept integrated factor) | §7.6 | [proved] from (I-8), (Q) |
| Theorem P = (P-an) | §8 | [proved] from the inputs of §4 |
| (CL)(P), (11.1) | §11.1 | [proved] from Theorem P and TT Lemma 3.1 |
| (DP) and its compatibility | §10 | [design], already SA's (SA L17317); checked against LF1 and ST1 |
| Corrections to TT §3.3 | §11.2 | [proved] (items 1–2 by Theorems D1, D3 and route F2) |

### 13.2 Inputs, with owners

| Input | Owner | Status as recorded | Stated by the owner in this form? |
|---|---|---|---|
| **(L)** interpolated presentation on 𝕊 × 𝔻_{R_f} | NL1(3)–(4), ST1 Thm 1 (hyp. 6) | NL1 [O] through (D4) (AS L288); ST1 Thm 1 [proved as implication] | **No: stated for the actual source and scalar λ, not the free complex fluctuation. First on the path.** |
| (L-W) size of 𝐏^{(k)} and the profile term | NL1(3) | Balaban; CA-II reading | no explicit bound found |
| (L-S), (L-Z) strip and δ-elimination | NL1(3), LF1(4) | SA L17526, L17534–17537 | sizes not stated |
| (L-reg) = (D.3) as the step evaluates | IN1, NL1(3) | IN1 Lemma D.3 [P] | yes, as SA L19509's sentence; reading flagged |
| (L-B) = (R23), (N-B) | NL1(1), IN1 class | (R23) stated (SA L6200); (N-B) is B1's per-cube sum | (N-B) with exponent τ_B: not stated |
| (L-K) kept-form oscillation | LF1(4) | SA L17564 | yes (SA L17564), with exempt d^♮ |
| (L-I) = (I-8) | LF1(4) | [C] conditional (`gates/sa-2.8-terms-gate.md`) | yes |
| (Q) at later real pairs; (BX) | LF1(4), BG1(1) | Lemma Q at the main-step point | no |
| (G-gap), (G-isl), (G-sep) | LF1(2) | SA L17320–17325, L17575; GEO [C] under supplied rules | (G-sep) not stated as such |
| (S), (sep), μρ_{sep} ≥ 2 | ST1 | ST1 (S) [hypothesis 4 of Thm 1, proved at every transition by Thm 2]; (sep) Def 1 | μρ_{sep} ≥ 2 new [design] |
| (H-Mayer) | LF1(5) | ⟦LF-2.10⟧ open (AS L298); `s210.md` Result: (5) unproved | stated by SA L17968–17997, not proved |
| (KP-h), uniform on 𝒟_{ext} | LF1(5), IN1 C.8 | SA L17982–17989 states convergence | the uniform-in-complex-e form is new here (it follows from the mass definition) |

### 13.3 The first remaining statement on (P-an)'s path

(P-an) has no Outstanding statement of its own. The first input on its path not yet stated by its owner in the form used is **(L)**:

> For every f ∈ 𝔉 there are a connected X_f, a radius R_f ≥ R = c_R(log θ_{i−1})^q and F_f : 𝕊_{X_f} × 𝔻_{R_f} → ℂ, holomorphic, with F_f(𝟏, ·) the f-term of the step-i exponent on 𝒲, depending only on (s, ζ) restricted to K_{X_f}(s), real at real arguments, equal to F_f(𝟏, 0) at ζ = 0 for every s, and bounded as in (L6).

It is NL1's product-box holomorphy (NL1(3)) together with ST1's admission at the main step (ST1 Theorem 1), with the free complex fluctuation as the source. It is what the step's own cluster expansion already requires of NL1 (SA L14314–14315). It is not attacked here, because it is the main content of NL1 and (D4), not a part of (P-an). After it come, in path order, (BX) and (Q) at later real pairs, (N-B) with its exponent, and (H-Mayer) (⟦LF-2.10⟧).

### 13.4 Checks this draft needs

- One check, by another model, of §5–§8: Lemmas 5.1–5.5, Proposition 6.1, Lemmas 7.1–7.6, Lemma Q, Theorems D1–D3 and P. They are self-contained complex analysis and counting.
- A check of §3 and §4: that (3.1) lists every y-dependent factor of the step-i integrand, and that each input is the owner's statement read correctly. In particular (L) at the main step, and the identification of the kept forms, z-factors and island blocks as the only background-dependent parts of carried operations (SA L17558–17564).
- ST1 to confirm (S) for complex sources of sup norm < R, and the floor μρ_{sep} ≥ 2.

*RAM and method.* No computation was run. Every source was read in bounded ranges, cited above.

End of pass 1 (P-an).

This file has 566 lines.
