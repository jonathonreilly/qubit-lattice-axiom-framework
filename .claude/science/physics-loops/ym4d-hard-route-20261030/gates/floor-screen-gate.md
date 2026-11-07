# Floor-screen gate — queue row 87
Provenance: OpenAI Codex, GPT-6 family (exact backend and actual effort not exposed; row 87 requests xhigh); checkout `460a6800be93d6288f1976b4ccb4d13bbb4ab0ba`; Sussman–Alpoge `31a47c543775`; T. Balaban, *The Variational Problem and Background Fields in Renormalization Group Method for Lattice Gauge Theories*, CMP **102** (1985), 277–309, Section F; research text, not an audit, grants no status.

| Statement | Verdict | First failure in the submitted argument |
|---|---|---|
| O | CORRECT-NO-ADVANCE | None for the full fixed joined datum; the subsequent assertion about all raw floor variables does not follow. |
| S | WRONG | Applying the step formula for \(\Omega_l^c\) at \(l=0\); positive levels also need the margin and seam identifications. |
| G | WRONG as written | (ii): the bare support of an outward row is not confined to width \(\xi_{j-1}\). The final bound is repaired below. |
| T | CORRECT-NO-ADVANCE | None under its stated flow hypotheses. |
| R | CORRECT-NO-ADVANCE, conditional | Step 3 inherits G(ii); after the repair, none. Its support and admission hypotheses remain inputs. |
| (OS-loc) | WRONG as an available estimate | The literal unpadded local datum is not what (160) reads; the weighted-tail replacement is also unproved. No refutation of the proposed inequality is claimed. |
| I | CORRECT-NO-ADVANCE, conditional | None. |

This checks row 83's proposed removal of the floor-screening reversal test (route-decisions position H). Credit for the outline and its constructions belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as the authors of their text. The outline was fetched once at the specified commit; the Balaban OCR stays outside the repository. All arguments below are hand arguments; file searches and transcription supply no mathematical discharge. Pending input theorems remain pending.

Verdicts distinguish a valid conditional lemma from a proof of its hypotheses or of the full screening claim. WRONG identifies a failed proof step or an unavailable asserted input; it does not turn an unproved support assertion into a proved counterexample.

## 1. Lemma O — CORRECT-NO-ADVANCE

**First failing step: none in the fixed-datum assertion.** Interpret the background as a partial map into regular critical **orbits**, with the full joined datum held fixed. Fix the sequence, its action domain, its constraint map, and all localization choices. Two assignments of other variables with the same full datum give the identical constraint set, the identical Wilson action, the identical stationarity equations and the identical regularity condition. Their sets of regular critical orbits therefore agree, including when that set is empty or is not a singleton. When it is a singleton, the backgrounds agree. A fixed axial representative also agrees; a representative chosen using an extra external gauge need not. This proves the assertion without assuming existence.

SA 9776–9783 requires one qualification: localization adds collar bonds carrying the lift of the old coarse datum. Independence holds after fixing **those values too**. It does not say that the localized background reads only the old bonds strictly inside the component.

The inference following the lemma is too broad. A bare field in the floor is not necessarily off the determining set: in a level-zero pillar its bare bonds are precisely determining bonds. The file's own Example 1 uses this fact. Changing such a bond changes the datum. Likewise a stored variable can enter through a reconstructed datum or collar lift. The valid statement is independence of changes that preserve the entire joined datum and the geometry. It proves neither that every raw floor variable preserves them nor that the remaining datum is regular. Thus Lemma O alone cannot retire the heavy-wall test.

## 2. Lemma S — WRONG as a completed support lemma

**First failing step:** the proof applies the step formula for \(\Omega_l^c\) to every \(l<m_b\). At \(l=0\) that formula is unavailable: SA 17317 instead defines \(\Omega_0=\Omega_1^{\sim}\). No level-zero plaquette test is shown to have passed by this argument. These are actual determining bonds and cannot be discarded using Lemma O.

Even restricted to positive, unmodified label levels, the proof stops before its conclusion:

1. A test with a bond in \(\Gamma_l\) is within one level-\(l\) spacing of \(\Omega_l\). The four-cell exclusion of \(P_l\) keeps it away from failed plaquette-test cubes. This does **not** establish that it was tested. The width and full support of the omitted margin of the older region are unspecified. The author assumes four cells; SA 6049–6074 explicitly leaves actual test neighborhoods to formation data. Eight cells minus an unspecified margin is no proved positive clearance.
2. For an ordinary plaquette of \(V_l\), a passed localized test and the converse averaging estimate of SA 9667 would give the claimed bound, conditional on that estimate. A seam test instead contains \(\mathcal M(V_{l-1})\) on its finer side (SA 9616). The argument has not identified these values with the averages of the localized field whose test passed. That requires the actual surviving delta constraints, including reconstructed pivot values (SA 17341). Smallness of \(V_l\) alone cannot imply smallness of this mixed product: take its coarse factors equal to 1 and one unconstrained fine-side factor equal to \(-1\). This is a counterexample to the omitted implication, **not** a claimed admissible history.

The last use of the converse averaging theorem is also explicitly unchecked in the source. A citation to it is a conditional input, not a hand discharge. The earlier-operation and newly lifted collar cases are expressly omitted; the drop-out evaluation fibre's imposed envelope does not prove the same envelope on every original support. SA 17709–17715 asserts the latter but does not supply the missing induction here.

**Visible repair (conditional; support construction still unproved).** State the formation margin and require the *entire* test neighborhood to fit between it and \(\Omega_l\). For each positive-level seam, exhibit the surviving constraint \(\mathcal M(V_{l-1})(b)=V_l(b)\) on each substituted bond; then the mixed plaquette equals the tested coarse plaquette and the converse bound applies. At level zero supply the passed approximate tests **including pivot reconstruction** on every bond of a plaquette. If those give \(\|V_0(b)-W(b)\|\le h\), where \(W\) has plaquettes bounded by \(u\), telescoping four unitary factors gives \(\|\partial V_0(p)-1\|\le u+4h\). With \(u\le C\varepsilon_1/L^2\), \(h\le C(A_1/A_0)\varepsilon_0\), and the stated threshold comparison this is \(C'\varepsilon_0\). Check the analogous identities after every earlier operation and for every collar lift. Until that is done, retain (D-F) as an explicit hypothesis; do not call (SUP) proved. This repair identifies the needed estimates but does not assert that the unspecified formation data satisfy them.

## 3. Lemma T — CORRECT-NO-ADVANCE

**First failing step: none under its displayed flow and threshold hypotheses.** Put \(s=2r+p_0\) and \(h(x)=x^{-1/2}(\log x)^s\). Then \(h'/h=(s/\log x-1/2)/x\), so \(h\) decreases for \(x\ge e^{2s}\). Rounding to the next power of \(L\) gives
\[
 R_l^2\varepsilon_l\le L^2A_0h(x_l)
 \le L^2A_0h(x_m-C_{\rm fl})\le2L^2A_0h(x_m).
\]
The last inequality follows, for \(x_m\ge2C_{\rm fl}\), from the square-root ratio being at most \(\sqrt2\) and the logarithmic ratio being at most one. The running minimum is at least \(x_m-C_{\rm fl}\), so
\[
 R_m^2\varepsilon_m\ge A_0x_m^{-1/2}
 [\log(x_m-C_{\rm fl})]^{2r}(\log x_m)^{p_0}
 \ge\tfrac12 A_0h(x_m)
\]
after increasing the fixed lower bound on \(x_m\). For an explicit choice for this last step, set \(q=2^{-1/(2r)}\), require \(x_m\ge2C_{\rm fl}\) and \(\log x_m\ge\log2/(1-q)\). Then \(\log(x_m-C_{\rm fl})\ge q\log x_m\). Division proves the stated \(4L^2\) bound, uniformly in \(l,m\). Empty floors cause no exception.

The application must keep the frame variable distinct from the action coupling. SA 6016–6047 gives the lower flow bound directly for \(\theta\), with \(\varepsilon_j=A_0\theta_j^{-1/2}(\log\theta_j)^{p_0}\) and \(R_j=R(\min_{i\le j}\theta_i)\). Thus the lemma applies verbatim with \(x\) renamed \(\theta\); no new flow conjecture is needed. If \(\varsigma\) uses the actual \(x_m\), the tube (R20) supplies a fixed comparison, not equality. For sufficiently small tube ratio, \(\theta_m/2\le x_m\le3\theta_m/2\), so the two inverse square roots and their fixed logarithmic powers are comparable. This preserves the decay-to-zero comparisons below, with changed constants. Identifying the two sequences silently would not be valid.

## 4. Lemma G — WRONG as written; the distance bound has a hand repair

**First failing step: (ii), the claimed support width \(\xi_{j-1}\).** An outward level-\(j\) row reads a double block of level \(j\), including \(B^j(c_-)\) on the finer side; it does not read just a block of diameter \(\xi_{j-1}\). SA 7430 states this explicitly. For a flat face halfway between two consecutive level-\(j\) tops, the outside top of an outward bond is already \(\xi_j/2\) from the face, greater than \(\xi_{j-1}\) for \(L>2\). This is an allowed aligned face and disproves that intermediate assertion.

Here is the repair, keeping the final constant 4. Use the full coarse plaquette and its underlying centered blocks. Their support is within \(3\xi_j\) of \(\Omega_j^S\), and any point of the geometric test loop is within \(3\xi_j\) of any point of that support. Indeed the four coarse corners span one spacing in two coordinate directions, the blocks add at most half a spacing on either side, and the finer-side one-step averages stay in the same coarse blocks. The constant 3 safely covers the endpoints and the bare-lattice rounding. Fix the allowed large gap so \(\rho>3L\), and take \(MR_{m_b}>3\).

* (i) survives: two closed grid cells which do not touch have indices differing by at least two in one coordinate. Consequently \(\operatorname{dist}_\infty(F,\Omega_{m_b})\ge s\), with \(s=MR_{m_b}\xi_{m_b}\).
* For \(j\ge m_b+1\), the full support lies in \(\Omega_{j-1}^S\): its distance from \(\Omega_j^S\) is at most \(3\xi_j<\rho\xi_{j-1}\). By (S1b) and nesting, that set lies in \(\Omega_{m_b}\). For \(j=m_b\), its distance from \(\Omega_{m_b}\) is at most \(3\xi_{m_b}<s\). Neither kind of test meets \(F\). Hence a floor test has \(l\le m_b-1\).
* Pick a support point in \(F\). The preceding support-diameter estimate puts every point of \(\tau\) at physical distance at least \(s-3\xi_l\) from \(\Omega_{m_b}\). A path from \(x\in\Omega_{m_b}\) to \(\tau\), after its last exit, must traverse at least \(s-4\xi_{m_b-1}\) outside that set; the extra spacing accommodates a discrete exit bond.
* By (S1b), throughout this final segment inside \(X\) the stage's local scale is at most \(\xi_{m_b-1}\). Outside \(X\), any part of \(\widetilde X\setminus X\) lies in \(\Omega_{m_b}\) and therefore cannot occur on the segment; outside \(\widetilde X\) the weight is \(\eta^{-1}\ge\xi_{m_b-1}^{-1}\). Every path, including paths taking shortcuts through coarser layers before their last exit, therefore costs at least
\[
 (s-4\xi_{m_b-1})/\xi_{m_b-1}=LMR_{m_b}-4.
\]
Taking the infimum proves the repaired G. This is conditional on **all** of (S1b), including the localization collar being inside \(\Omega_{m_b}\); separation alone does not imply it. The proof does not establish (S1) for the actual stage construction.

## 5. Theorem R — CORRECT-NO-ADVANCE as a conditional theorem

**First failing dependency in the submitted proof:** Step 3 invokes G's erroneous support argument. Section 4 above repairs it. With that repair and the standing flow hypotheses of T, no further step fails. This does not supply (D-F) on supports, (D-far) from the energy, or admission of the actual stage geometry. Plaquettes in the conclusion must, of course, belong to the domain of the localized background as well as to \(\Omega_{m_b}\).

1. Set \(A_F=4L^2C_FR_m^2\varepsilon_m\) and \(e_1=\max\{\varsigma,A_F\}\). D-far, D-F and T bound **every actual test of the joined datum** by \(e_1\). In the theorem's single-flow notation, both entries are \(e^{-\ell_m/2}\) times fixed powers of \(\ell_m\), since \(R_m\le L\ell_m^r\); hence \(e_1\to0\). The frame/action version follows by the tube comparison in §3. Require the admitted geometry and the inputs' torus floor separately; a smaller coupling does not establish these. Choose the coupling ceiling so \(e_1\le\bar\varepsilon\) and \(C_1e_1\le a_P\), with the necessary chart bounds.
2. A1-S now gives a nonempty single regular critical orbit at radius \(C_1e_1\). A3-P applies to that orbit. This is where existence is obtained; a local profile bound by itself supplies no existence.
3. Split the profile maximum into \(\mathcal T_{\rm far}\) and \(\mathcal T_F\). The first part is at most \(\varsigma\). For each test in the second part, the repaired G and T give
\[
 e^{-\delta_Pd_S(x,\tau)}v(\tau)
 \le A_Fe^{-\delta_P(LMR_{m_b}-4)}
 \le e^{4\delta_P}A_Fe^{-L\delta_PMR_m}.
\]
The last inequality uses \(R_{m_b}\ge R_m\), which follows directly because a running minimum, its logarithm and upward rounding to powers of \(L\) are non-increasing with the index. Maximizing proves R(b).
4. The flow bound implies \(\log\min_{i\le m}x_i\ge\ell_m/2\) at a sufficiently small coupling. Divide the second entry of R(b) by \(\varsigma=C_vg_m\ell_m^{p_1-4r}\). The quotient is at most
\[
 \frac{4L^4C_FA_0e^{4\delta_P}}{C_v}
 \ell_m^{6r+p_0-p_1}
 e^{-L\delta_PM2^{-r}\ell_m^r}\longrightarrow0.
\]
For a hand justification, for any fixed exponent \(a\) choose an integer \(n>a/r\); the inequality \(e^{ct^r/2}\ge(ct^r/2)^n/n!\) makes \(t^ae^{-ct^r}\to0\). Lowering the ceiling proves R(c), uniformly in depth.

**Exact interface with `a3-profile.md` (30)–(31).** Use its no-inward-bond, real, already admitted localized problem, including its pending P81/P82 ports. Set its mismatch set equal to the **set of actual tests** \(\mathcal T_F\), not to the geometric floor \(F\). Its metric is precisely \(d_S=d_{\mathbf B}\) of SA 9602. For a plaquette let \(d(p,\mathcal T_F)\) be the minimum over its corners and the tests. Since every corner is in \(\Omega_{m_b}\), G gives the same lower bound for this minimum. Use \(\delta_P=\delta\) supplied by the profile, or a smaller rate. Equation (30) gives R's maximum with the same profile constant; (31) alone is written as a sum and gives that maximum after enlarging the constant by a factor two.

No propagator rate is imported. The coefficient \(L\delta_P\) in the exponent of \(MR_m\) comes from the proved distance \(LMR_m-4\); the exponent per unit of \(d_S\) remains \(\delta_P\). The outline's pre-existing symbol \(\delta_0\) cannot simply be identified with this new number. If a single rate is needed elsewhere, choose it no larger than both the available propagator rate and \(L\delta_P\), and choose rate-dependent geometry subsequently. Thus (31) has the needed profile content, **conditionally**, but supplies neither the support/admission hypotheses nor a previously fixed larger rate. It also says nothing of this strength throughout the waiting collar immediately adjacent to the floor.

## 6. (OS-loc) — WRONG as an available estimate; the proposed inequality remains unproved

The file honestly labels this proposal unproved. The verdict means it cannot discharge the one-step input; it is **not** a counterexample to the inequality. Here is the line-by-line comparison with Balaban, using \(\delta_B\) for his propagator rate to avoid identifying it with the profile rate.

* **(160).** In the gauge centered at \(y\), the actual mixed datum on \(\square_k'{}^{(k-1)}\cup\square_k''{}^{(k)}\) gives
  \( |B(c)|\le(8d^2L^2+4L^2|c_--y|)\varepsilon_1\).
  The first term comes from reconstructing the finer block; the second from accumulating plaquettes along the axial paths. This reads the plaquette tests of (7), including its mixed seam tests, on the construction's **padded** cube. A local supremum can replace \(\varepsilon_1\) only if it covers every such test and its reconstruction blocks. Section F's (144) constructs additional cubes and a padding of \(2R_1M_1\xi_j\); (160) is not stated just on the central cube of side \(2R_1M_1\xi_j\).
* **(161).** Split the flat-kernel sum for \(HB\) into the rows controlled by (160) and the artificial outer rows. The latter carry averages of \(U\), bounded globally by \(18d^2L^3M\varepsilon_0\) from (152)–(155). Split the kernel exponential into two equal factors; the distance of those rows yields \(e^{-\delta_BR_1M_1/2}\). The remaining weighted row sum has terms proportional to \(e^{-\delta_Bd(y_1,y_2)/2}(d(y_1,y_2)+1)(L^{j_2}\eta)^{-1}\). Dropping this scale factor would change the estimate.
* **(162)–(164).** Balaban defines \(B_3\) as four times the prefactor of that uniform row sum. Its summability is a cited flat-propagator input, not proved by the OCR. Choose \(R_1M_1\) so \(B_3e^{-\delta_BR_1M_1/2}\le1/2\). Then the four coordinate norms of \(HB\) are at most
  \(\frac14 M_A\max\{B_3\varepsilon_1,\varepsilon_0/2\}\), with \(M_A=1\) on the central pillar. The factor \(1/4\) is fixed by the ratio of (161)'s prefactor to (162), resolving the garbled fraction in (164).
* **(165).** Insert \(A=A_1+HB-HD(A_1+HB)\) and the critical equation (158). The two nonlinear contributions give, on the central pillar,
  \[
  \mathcal N(A)\le\tfrac14\max\{B_3\varepsilon_1,\varepsilon_0/2\}
       +K_Q\varepsilon_0^2,\qquad
  K_Q=B_0(C_4+4C_2)(36dL^2B_1R_1M_1)^2.
  \]
  For the larger-cube case the quadratic factor is \((M'\varepsilon_0)^2\), where \(M'=M/(R_1M_1)\). The floor-screen text omits \((R_1M_1)^2\) when describing this term. It can be absorbed into a fixed \(C_Q\) after geometry is fixed; it cannot simply be deleted.
* **(166)–(167).** Choose \(a_5\) so \(K_Qa_5\le1/8\), along with the earlier chart bounds. For \(M'=M_A=1\), the coordinate bound becomes \(\frac14H+\varepsilon_0/8\le H/2\), where \(H=\max\{B_3\varepsilon_1,\varepsilon_0/2\}\). The last inequality uses \(H\ge\varepsilon_0/2\). The subsequent group-field conversion (168), bounded by \(e'+86d(e')^2<2e'\), gives the global halving \(r_U\le H\). Thus (167) alone is a coordinate estimate; curvature and current require this additional conversion. Leaving the quadratic remainder unabsorbed is legitimate with a larger fixed \(C_Q\) which includes that conversion.

**First unsupported identification with the displayed (OS-loc):** replacing the datum bound by the literal \(a(y)\) defined on the unpadded `box(y)`. Specify a read box containing all the tests in (160), including the finer reconstruction blocks. A fixed enlargement is sufficient geometrically, but must be made in the definition. Its weighted diameter is a fixed \(D=C_LR_1M_1\); the printed \(8R_1M_1\) has not been justified for this enlarged read box.

**The substantive remaining failure:** the step \(\varepsilon_0\mapsto Tf\) in the far contribution is absent from Balaban. From \(r_U\le f\), a point on an axial reconstruction path is controlled by \(f(z)\le e^{\kappa d_S(y,z)}Tf(y)\). To sum this against the row's kernel requires a bound relating **that path point's** distance to the row endpoint's distance. Triangle inequality supplies no such bound for a prescribed comb. A fine slab can make a comb enter a region of very large metric weight while a path between its endpoints goes around the slab in coarser layers. The weighted distance to an interior point of the slab can then exceed the endpoints' distance by an arbitrarily large amount. Separation of successive layers does not make every comb a near-geodesic.

**Visible repair (unproved port).** Define \(a^+(y)\) on the complete padded read box. Prove, in local gauges and the actual no-inward-bond/inner-action convention, a weighted row estimate for the far **reduced angular datum**. Choose \(\kappa\) smaller than the available kernel rate, retain a summable exponential after the weight is inserted, and choose the auxiliary collar so the resulting tail coefficient is at most \(1/2\). Bound the nonlinear and group-conversion terms by the full \(C_Q\varepsilon_0^2\). This would give the corrected (OS-loc) with \(a^+\). Neither a local gauge-existence lemma alone nor (160)–(167) proves the needed weighted row estimate. The pending P81/P82 route in `a3-profile.md` is an alternative conditional route; it is not an already completed port of this displayed formula.

## 7. Lemma I — CORRECT-NO-ADVANCE

**First failing step: none.** This is a valid purely scalar implication from (OS-loc). Put \(Q=C_Q\varepsilon_0^2\). Its two provisos give \(B_3\sup a+Q\le\varepsilon_0\) and \(Q\le\varepsilon_0/2\). Thus, if \(r_U\le f_n\le\varepsilon_0\), (OS-loc) gives \(r_U\le f_{n+1}\), while
\[
 f_{n+1}\le\max\{B_3\sup a,\varepsilon_0/2\}+Q\le\varepsilon_0.
\]
This proves admissibility at every iteration starting from \(f_0=\varepsilon_0\).

For nonnegative functions, \(T\) is monotone and positively homogeneous, preserves binary maxima, fixes nonnegative constants, and satisfies \(T(u+c)\le Tu+c\). Triangle inequality gives \(T^2u\le Tu\); choosing the intermediate point to be the initial point gives the reverse inequality, so \(T^2=T\). Also \(u\le Tu\).

Set \(A=B_3a+2Q\). At \(n=0\), \(f_0\le\max\{TA,\varepsilon_0+2Q\}\). If \(f_n\le\max\{TA,2^{-n}\varepsilon_0+2Q\}\), the preceding identities give
\[
 f_{n+1}\le\max\{B_3a+Q,\tfrac12TA+Q,
                   2^{-n-1}\varepsilon_0+2Q\}
 \le\max\{TA,2^{-n-1}\varepsilon_0+2Q\}.
\]
Here \(B_3a+Q\le A\le TA\) and \(TA\ge2Q\) justify both absorptions. Letting \(n\to\infty\), without needing convergence of \(f_n\), gives
\(r_U\le TA\le B_3Ta+2Q\), exactly the claimed result.

There is also a shorter check: use the allowed choice \(f=r_U\) directly, apply \(T\), and put \(z=Tr_U\). Then \(z\le\max\{B_3Ta,z/2\}+Q\), whence \(z\le\max\{B_3Ta+Q,2Q\}\le B_3Ta+2Q\). Thus the provisos are sufficient for the printed iteration but unnecessary for this direct consequence. Neither proof establishes (OS-loc).

## 8. Section 5's consumer and the consequence for row 83

The global quadratic remainder is not itself an obstruction to **screening**. Conditional on the repaired (OS-loc), take \(\varepsilon_0=(C_1+2B_3)e_1\). For small coupling, \(B_3\sup a^+\le\varepsilon_0/2\) and \(C_Q\varepsilon_0^2\le\varepsilon_0/2\); Lemma I applies. Split the tests in each read box before taking either maximum. Exterior tests contribute at most \(\varsigma\), even in a box also containing a floor test. If a read box at \(y'\) contains a floor test, its diameter bound and G give \(d_S(y,y')\ge LMR_{m_b}-4-D\). Therefore
\[
 r_U(y)\le B_3\max\{\varsigma,
       e^{\kappa(4+D)}A_Fe^{-L\kappa MR_m}\}
       +2C_Q\varepsilon_0^2.
\]
The tail is absorbed as in R. Without even assuming which entry of \(e_1\) dominates,
\[
 \varepsilon_0^2/\varsigma
 \le C\{\varsigma+g_m\ell_m^{8r+2p_0-p_1}\}\longrightarrow0.
\]
Thus a corrected Corollary R' follows conditionally, with \(D\) replacing the unsupported printed diameter. This residual quadratic estimate is not the homogeneous full A3 profile, but it suffices for this consumer.

The defects that affect the route, ranked by consequence, are: **(1)** S does not establish the support envelope needed for (D-F); **(2)** Balaban's local calculation has not been ported to (OS-loc)'s weighted tail and actual read sets; **(3)** G's support width is false, though its final distance estimate has the repair above; **(4)** O's valid fixed-datum assertion is overextended to raw floor variables. The frame/coupling distinction and rate choice are explicit interface requirements, handled above, not additional claimed closures.

The surviving result is conditional screening for an admitted stage with controlled **actual joined datum**. Row 83 has not established that every support has such a datum, and its proposed dismissal of the heavy-wall reversal test does not follow. No counterexample to the complete supported screening statement has been proved here; no unconditional screening or rarity result is obtained.
