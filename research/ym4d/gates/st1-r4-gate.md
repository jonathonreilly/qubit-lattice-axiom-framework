First failing step: none.

# Gate: `library/st1-r4.md` (ST1 round 4, Amendment CV), pass 3

Checked line by line by Claude (fresh session), Opus 5.5. This is one reading by another model. It is not an audit and grants no status. I did not write the text. I read `library/st1-r4.md` once, in full (1,684 lines). I compared it with `library/st1-r3.md` (diff by hunk) and `gates/st1-gate.md`. For `library/f-meas.md` I read §§1, 5, 6 and the Result, and diffed its body (lines 60–586) against `st1-r4.md` 926–1451. The two agree except for heading levels and one cross-reference ("§1" became "ST1 §2"). I checked imports against `p82.md` (lines 140, 220, 243) and `a1-balaban.md` §9.1 (2452–2546, especially 2492–2511). I read the cited source lines in SA (`ym4.tex`), CA-I (`ca_I.tex`) and Y3 (`YM3_I.tex`). No computation was used as a proof step.

## Round-3 fixes

All seven are in place. None is lost.
1. Line 135 records P82 as frozen, names M1 as the remaining matching item, and limits (15) to interior elements. See finding 1 for one dropped word.
2. Rows 2 and 9, and Lemma 10 at 675–677: the frame-increment bound may follow the amplitudes; \(C=3^{2r_R}\) after one \(\gamma\) ceiling.
3. Lemma 8 at 539 and 621–623: \(\bar a<\delta_B/(4C_QL)\) is chosen inside Lemma 8, before \(a_T\), and kept distinct from \(\widehat a\).
4. Lemma 10 (652) lists A1/F0/REG. F6 (905) lists RUN and (15).
5. Corollary 14′ (1587–1589) states the real-input scope and the admitted-complex-input scope. The "exactly the five hypotheses" wording is gone.
6. Line 1663 attributes \(q>p_0+2r_R\) to ST1 and states SA's own conditions.
7. Line 737: \(K_{\rm tw}=64e^{4\delta_T}K_T\).

## What I re-derived

- **CV construction (1152–1157).** The descent \(u(x)=u(z)(\mathcal M^nU)(z,x)\), with \(u=I\) at nodes, gives \((\mathcal M^nU^u)(z,x)=I\) by two-sided covariance of the Federbush mean. Level-\(n\) averages read \(u\) only at level-\(n\) grid sites, so the top-down solve is triangular and assigns each value once. This matches `a1-balaban.md` 2492–2511 ("either the comb or the actual mean") and SA 9669–9676.
- **Item 4 (Lemma 8, 583–589).** At a mean-axial \(U_0\) the reference mean is \(I\), while single paths need not be \(I\). The reference paths are close to each other, since their difference is enclosed curvature of order \(L^2\varpi\). So Lemma 3's contraction, which is uniform in \(N\le24\), applies on a smaller ball. By (23), a level-\(n\) bond changes by at most \(2\xi_n\sup|H|\). A path has at most \(2(L-1)\) bonds, and the conjugating prefixes are real unitary. Thus each factor changes by at most \(C_{\rm av}(L)\cdot4(L-1)\xi_n\sup|H|\). The sum over \(n<q\) is below \(C\xi_q\sup|H|\). This gives \(\exp(C\xi_q\sup|H|)\), with no fixed factor raised to the pillar depth. The recursion has the right gauge orientation for \(W_B^{u_B}=\Phi_V(B)\).
- **Item 5.** \((U^u)^w=U^{wu}\) holds under (1), so the composed gauge is \(wu_B\). Tops stay fixed.
- **Items 1–3.** Lemma 5's proof uses the CV representative. The auxiliary tree gauge (278) is labelled auxiliary. LEV is unchanged in substance.
- **FM1–FM3.** \(\sigma_H=1/(2\pi^2)\) is correct. In FM2, \(\sigma_H^{|E|}/\sigma_H^{|C|}=\sigma_H^N\). The \((u,v)\mapsto t\) determinant is \(\prod_c\det J_c^{-1}\), because each equation reads only its own pivot. The \(s(Q(v_c))\) denominator is right. FM3 follows at \(v=0\). The independence argument for the kernel is sound. (FM3n) correctly separates a kernel from a law.
- **FM4–FM6.** FM5's free-row Haar invariance gives \(s(g^2Q(B'))\). The pivot factors stay in \(\Pi_V\). FM6 matches CA-I 81735–81756: the full logarithm is \(g_jCB-h\tilde D(g_jCB)=\Psi_V(\mathsf C_VgB)\).
- **Theorem FM, (FMd), (FMg).** \(DΨ-I=-h_VDd\) is supported on pivot rows. Each \(d(c)\) depends on \(t_F\) and \(t_{p(c)}\) only, so the pivot block is block-diagonal. This gives the trace-log sum. Adding and subtracting the two quadratic forms is an exact identity. \(E_{\rm ch}=N\log(\sigma_Hg^3)\) matches SA 7487 (one \(\sigma_H(0)\) per non-pivot bond).
- **FM7.** By SA QC15 (8185–8189), a free internal bond on the line from \(y\) towards the pivot has coefficient at least \(L^{-4}>0\) in \((K_I\iota u)(c)\). So the pivot angle is nonzero on an open set, where \((\sin r/r)^2<1\). The strict difference follows.
- **FC3.** Since \(\ker DM_-\subset\ker DM_+\), \(U_+\) is also critical for its own \(M_-\) datum. M\(_+\) nodes are M\(_-\) nodes, so residual M\(_-\) gauges are residual for M\(_+\). The derivative along the in-fibre curve vanishes.
- **FC4.** A noncentre site with all incident bonds internal needs \(L\ge5\). The Hessian identity follows by differentiating \(d\mathcal S(\xi)=0\) in fibre coordinates.
- **FC5.** \(V^u(y,x)=I\). Retained rows avoid new nonnodes. Each soft term is at its minimum zero. Under CV, \(V(y,x)=(\mathcal M^jU_+)(y,x)=I\), so \(V_{\rm ax}=V\).
- **FC6.** I checked the comb bonds for order (4,3,2,1), the mean \(e^{iF_p/2}\) of \(\{I,e^{iF_p}\}\), \(V_{\rm ax}(e)=e^{iF_p/2}\) and (FC6b). The \(\tan\alpha\) quadratic centre and (FC6c) are correct.
- **FC0–FC2.** \(u(m)=0\). FC1's two-way inclusion uses \(9\delta'/8<r_u\), \(C_{\rm ch}L^4\cdot9\delta'/8+\delta'/8<r_{\rm sol}/4\) and \(r_{\rm sol}/4+h<r_{\rm sol}/2\). FC2 is FM5 with \(V'=V^\sharp\). The FC-test example \(\int_{-b}^b\mathbf 1_{|z+x|<b}dz=2b-|x|\) is correct.
- **FC7.** The harmonic measure of the arc at \(\zeta=i\) is \((4/\pi)\arctan(1/R)\). The coordinates stay below \(3r_{\rm hol}/4\). If \(\alpha\le1/2\) and \(H_{\mathbb R}\le M_*\), the bound is \(\sqrt{M_*C_F}e^{-aR_\sharp/2}\). The \(\gamma\) limit follows from \(r>1\).
- **FC8.** \(2\delta'+\delta'/8+\delta'/16=35\delta'/16<9\delta'/4\).
- **FC9.** With \(d_0=3/4\): \(r_-=7/16\), \(r_+=13/16\), the image lies in \(T^\sharp_b\) since \(14b/16<b\), and the Jacobian bound is \(e^{2/(16^2d_0^2)}\). These agree with Y3 52091–52134 at \(d_*=3/4\), \(\varepsilon_{\mathbf m}=1/16\). The fixed-endpoint homotopy is correct.
- **(FCr).** \(\|\beta-(Z-m)\|\le C_\ell|Z|\|\eta\|\le2C_\ell b\|\eta\|\) on \(T^\sharp_{2b}\). The quadratic-difference bound \(Cs_1Nb^2\|\eta\|\) follows.

## Outstanding items and constants

- **FM-match** enters only through Theorem 14 hypothesis 5 and Corollary 14′. **FC-mean-match** and **FC-test** enter only there and in Theorem FC's statement of its premise. **FC6-history** is used nowhere. **CI** enters only as hypothesis 4 and in (77). None is used silently.
- **Constants rule.** CV's \(C_{\rm av},C_u,C'_u\) and ST-test\(^{\rm hol}\)'s \(r_{\rm hol},M_*\) are in row 2, before \(\kappa\). The new smallness conditions are \(\gamma\) ceilings in row 10, after the amplitudes: FC1, FC8, \(R>1\), \(\alpha\le1/2\) (which needs \(\|Y\|\le C_Qr_1(i)\), with \(C_1\) from row 9) and the FC7 limit. The contour fractions are absolute. No constant fixed before \(\kappa\) reads \(b_f\), \(C_0\), \(C_1\), \(A_0\) or \(A_1\).

## Source readings

Each reads as stated.
- SA 7178–7181: the block axial gauge uses contour means, imposed softly "at those pairs \((y,x)\) for which the mean \(V(y,x)\) is defined (no factor is inserted at the other pairs)".
- SA 7481–7487: local coarea with \(\operatorname{Tr}\log(1-\mathsf h\partial\tilde D)+\sum_b\log\sigma_H\) over all bonds. \(\sigma_H(0)\) per non-pivot bond is absorbed. It is a local identity.
- SA 9667–9676: the mean gauge is a second gauge of the same kind, related to the comb one by \(\mathcal G^{\rm res}\). Theorems 3 and 5 concern the comb representative; \(V^{\rm bg}_k\) uses the mean.
- CA-I 54290–54310: the \((A_j,B_j)\) integrals with \(z^{(j)},\chi^{(j)},\chi'^{(j)},\mathbb P^{(j)}\). \(\mathfrak K^{(n)}\) is the increment of \(A^{(n)}+g_j^{-2}A\) between \(\mathbb U^{\rm sh}\) and \((U^{(n+1)}_k,A_j=0)\). This matches FM-match at 1097–1098.
- CA-I 81735–81756, 81829: the collar logarithm, \(B'_j=g_jB_j\), the full logarithm with \(h\tilde D\), and \(CB=B\) on independent bonds.
- Y3 46302–46386: integrated coarea with pivot factors \(\sigma_1(|B'(b_0(c))|^2)\), non-pivot Haar factors and Borel \(\Upsilon\) via Tonelli.
- Y3 52091–52134: the bump deformation. "The failed-test bonds are left fixed, so a bounded Borel factor in those variables is allowed." Reading "only" as in line 1653 is fair, since Cauchy needs holomorphy in the moved variables.
- Also checked: SA 8170–8232 (QC15–QC19), SA 17369–17396 (Lemma 2.2, "the new tests imply the old"), and CA-I 74312–74321 (integration bonds and rim).

## Findings (none fatal)

**1. Line 135 (P82° status). Repairable wording.** Round-3 fix 1 asked for "P82° holds conditionally". Line 135 now says "P82° is now proved and frozen". Theorem P82 assumes I1–I8 (`p82.md` 220), with A1/F0 as I6, and \(\varepsilon_P\) depends on A1's auxiliary length unless that length is at its floor (`p82.md` 153). No step is affected: Theorem 14 hypothesis 1 assumes P82°–M1 and A1/F0/REG, and \(\rho_0\) (row 3) precedes \(\kappa\). Repair: write "proved, conditional on I1–I8 (including A1/F0), and frozen".

**2. Lines 1179–1180 (Lemma CV item 5) with line 129. Repairable, one sentence.** Item 5 applies (15) at the mean-axial base and says it is "assumed at arbitrary admitted real regular bases". §2 calls P82° proved, and `p82.md` 220 proves it at "its real axial A1 representative" \(U^\circ\). The transfer holds. The two representatives differ by a real residual gauge \(w\) (SA 9676; `a1-balaban.md` 2501). All P82 operators and norms are covariant under real gauge changes (`p82.md` 243). Every member of (15) is invariant under unitary \(\operatorname{Ad}w\). Tops are unchanged because \(w=I\) at nodes. Repair: state this covariance transfer in item 5.

**3. Line 1449 (Outstanding F-contour). Repairable notation.** "\(\theta_m=0\)" is not defined in the folded text (it is also undefined in `f-meas.md` 583). It collides with RUN's frame parameter \(\theta_m\ge\gamma^{-2}\). \(m_r\) and \(\epsilon_m\) refer to F5, whose radius is \(b_j=9\delta'_j/(8g_j)\), while FC7 uses \(b=\delta'/g\). Since \(b/16<b_j/16\), \(\epsilon_m=1/16\) is valid. Repair: define the parameter or delete it, and say which radius \(\epsilon_m\) refers to.

**4. Line 1166 (Lemma CV item 3). Not a failure.** "It now pins the selected contour convention too" overstates. LEV preserves \(T_{\mathbf U}(a)\) at level \(q-1\) of pinnable levelled tops. That value is \(I\) only when the real factor is CV-selected. Nothing downstream uses more than preservation. Repair: say "preserves the CV-selected contour values at those cells".

**5. Lines 1216–1228 (FC5) and 1329–1334 (FC-test). Not a failure.** SA's block-axial factor (7181) also carries the indicator \(\mathbf 1\{|V(y,x)-\mathbf 1|<\varepsilon_k\}\). It is a Borel factor in moved variables. FC-test's general wording covers it ("every remaining moved-variable factor"), so it is not used silently. Naming it would make the FC-test obligation concrete.

## Verdict

Amendment CV is ported correctly at every round-3 comb use (41, 128, 276–277, 339, 345, 581, 1064). The construction of the representative, the composition order \(wu_B\), and the uniform mean-Lipschitz conjugator bound check. The conjugator bound replaces the factor-two claim without a per-level loss, so (52), (49), CORE and the budgets keep their form. The folded F-results check as written: Theorem FM with pivot Haar factors, FM7, FC1–FC9, FC3–FC5 and Theorem FC. They are a faithful copy of `f-meas.md`. FM-match, FC-mean-match, FC-test, FC6-history and CI are named and not used silently. The constants respect the stated order. All seven round-3 fixes remain. Findings 1–3 are wording and notation repairs. Theorem 14 and Corollary 14′ hold as stated, conditional on their imports and the named Outstanding items.

Checked line by line by Claude (fresh session).
