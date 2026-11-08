# W1, W2 and W5: certificates and history matching

Codex, 2026-11-08. Checkout `362d9dd3694d54dbcaf51d8eeb7e778a9413fc47`.
Research text. Not an audit. Grants no status. No computation proves a step.

**Result.** The three source certificates are ported with their exact carriers.
W1 and W2 match IN1's maps on the adopted history-rule class.
W5 requires the stated restored-field, inset and carrying-action identities.
Application to every revised history still needs `GEOH-O1`, owned by `GEOH`.
This note stops at that existing assignment, under the no-duplicate instruction.
It does not claim an unconditional H-C or W6 theorem.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of
their text, for every source argument ported below. Credit Tadeusz Bałaban
for the averaging, constrained-background and large-field methods.

## 1. Sources and scope

**Y** means [YM4_1400.tex at `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex).
**SA** means [YM4_sketch_500.tex at `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
**I** means [complete account I at the latter pin](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).
Numbers after these letters are source lines.

The prior record `prior/w125-match.md` is absent. The whole
[H_step digest](prior/hstep.md) and [LFI digest](prior/lfi.md) were read.
Their W1, W2 and W5 ports are reused. The nonlinear averaging argument in
[sa-2.13-2.md, §6](sa-2.13-2.md) is also reused.
The registry gives H-C-AVERAGE, H-C-PLAQUETTE, H-C-FLUCTUATION and H-C-CUT
no separate owner at this pin. This note treats the assigned matching task.
It does not reopen H-C-MARK, H-C-KEPT, H-E or general domain admission.

The source search began with `sa-index/README.md`, neighboring chunk rows
and `obligations.md`. Relevant old-outline entries are SA 18210–18301,
18178–18186 and 18523–18535. The CA index locates the actual gauge region
at I 50188–50229 and 50251–50265. Bounded source excerpts were used.

### Premises before porting

Here **proved** describes the written source argument on its stated domain.
It does not mean independently checked or established for arbitrary histories.

| Premise | Source and standing | Exact role |
|---|---|---|
| Actual centered nonlinear average; positive linear flux and quadratic remainder | Y 4725–4779, 71619–71712: proved. Local version already rebuilt in `sa-2.13-2.md` §6. | Supplies H-C-AVERAGE on its actual four-block carrier. |
| Small-energy certificate on the complete backward cone | Y 71714–71842: proved. | Gives a depth-independent Wilson lower bound; also admits every intermediate mean. |
| Quantitative real orbit estimate for the specified separated test tower | Y 15241–15308: conditional induction. Its analytic premises are supplied by `bgc:proper-background`, Y 35634–35768. Proved on that specified geometry; cited here. | Small top curvature gives existence and passage. Totality alone supplies neither. |
| One-step rigidity, including crossing bonds | Y 3954 onward and 4538 give the statement and sketch. Y 10815–10871 supplies the finite reconstruction argument. Proved there; ported below. | Converts curvature, contour and coarse-row agreement into fine-bond agreement. |
| W1 and W2 contrapositives | Y 71845–71957: proved using the preceding inputs. | Supplies unweighted Wilson, respectively Wilson-plus-gauge, certificates. |
| Protected ordinary birth rows and original gauge factors | Y 71958–72093: proved for the stated update and quiet-window rules. | Transfers the same failed test to current, drop-out and inner-action reads. |
| Stopped action coefficient | Y 76758–76777: proved from the local freeze rule and drift bound. | Turns an unweighted certificate into a multiple of its birth coupling. |
| W5 preserved top rows, six-cell inset and separate carrying action | Y 72724–72737, 76865–76917: proved conditionally on the specified island construction. | Gives one fresh cut credit, outside the island's earlier mass. |
| Ordinary overlap allocation | Y 76811–76864, 76918–76937: proved under the stated carrier and floor rules. | Splits existing energy among events while keeping an integration share. |
| Complete W6 ledger | Y 76732–76754: hypothesis. | W1, W2 and W5 supply only their own event entries. |

I 4209–4246 cites Bałaban's ultraviolet theorem and large-field construction.
It is not a second proof of these three exact certificate matches.
The CA gauge-region formulas below are definitions imported from that construction.

## 2. W1: the nonlinear certificate on its actual carrier

This section ports Sussman–Alpoge, Y 4725–4779 and 71619–71892.
Use IN1's operator norm and \(a_p(U)=\tfrac12 f_U(p)^2\) for real \(U\).
All plaquettes in sums have one positive orientation.

For a coarse plaquette \(C\), let \(D(C)\) contain its four centered endpoint
blocks. Include every plaquette whose four corners lie there.
Include the plaquettes crossing the internal block faces.
This rectangle is IN1's \(Y(p')\), with its internal connecting bonds.
It contains every contour and straight segment used by the four actual averages.
Y 71619–71693 proves this without adding an exterior layer.

The scalar flux coefficient is exactly IN1's \(W(C,p)\):

\[
 T_{C,p}=L^{-4}\#\{x\in B(y):p\in S_x(C)\},\qquad
 \sum_pT_{C,p}=L^2,\quad \sum_CT_{C,p}=L^{-2}.                 \tag{1}
\]

For each surface offset, a fixed fine plaquette determines its starting site.
There are \(L^2\) such offsets. This gives the column sum in dimension four.
The count uses periodic multiplicities where necessary.

Y's local comb and Taylor argument gives, on the actual regular branch,

\[
 F_C^+=\sum_pT_{C,p}O_{C,p}F_p+R_C,\qquad
 |R_C|\le C_L\sum_{p\subset D(C)}|F_p|^2,                  \tag{2}
\]

where \(F_p=-i\log\partial U(p)\) and each \(O_{C,p}\) is orthogonal.
The comb uses only internal plaquettes. Unitarity permits large open transports.
Thus no small global potential or trivial torus holonomy is assumed.
Converting small logarithms to group defects changes only the quadratic remainder.
The number of internal plaquettes is bounded for fixed \(L\). Hence

\[
 f_{\mathcal MU}(C)
 \le\sum_pW(C,p)f_U(p)+C_{\rm SO}\max_{p\subset D(C)}f_U(p)^2. \tag{3}
\]

Choose the curvature ceiling inside both regular-branch neighborhoods.
The total average in `c1-repr.md` §4 uses the same regular rule there.
Its other rules are unused. This identifies (3) with IN1 (15).
The local derivation is already in `sa-2.13-2.md` §6; it is not a new result here.

For top plaquettes \(S\) at level \(t\), define

\[
 \begin{split}
 D_j(C)&=\bigcup_{y\text{ corner of }C}B^{t-j}(y),\\
 \mathcal P_j(S)&=\bigcup_{C\in S}
   \{p\text{ at level }j:\text{ all corners of }p\text{ lie in }D_j(C)\},\\
 \mathcal N_0(S)&=\mathcal P_0(S).
 \end{split}                                                   \tag{4}
\]

These are sets, not lists charging one plaquette repeatedly.
Odd centered blocks subdivide exactly. Thus every one-step read of
\(\mathcal P_{j+1}(S)\) lies in \(\mathcal P_j(S)\).
This includes intermediate means and full double blocks.
Periodic projection preserves this inclusion; matrix entries retain their multiplicities.

Y 71744–71842 proves, for every real field on this complete carrier,

\[
 E_S(U):=\sum_{p\in\mathcal N_0(S)}a_p(U)
 \ge\min\left\{\frac14\sum_{C\in S}f_{\mathcal M^tU}(C)^2,
                         \frac12e_*\right\},\qquad e_*>0.       \tag{5}
\]

The constant is independent of depth and volume.
Its proof uses the norm bounds \(\|T\|_{2\to2}\le1\) and
\(\|T\|_{1\to1}\le L^{-2}<1\).
The quadratic remainders sum geometrically in the latter norm.
Small \(E_S\) therefore admits every intermediate regular branch.
Large \(E_S\) gives the second alternative directly.
There is no linearization of the failed configuration in (5).

For an ordinary test cube \(\square\), put \(D=\square^{\sim4}\).
Let \(S_t\) contain all level-\(t\) plaquettes internal to \(D\).
Use the specified separated \(M_1\)-tower of \(D\).
Its third enlargement lies in its top member.
The torus has at least \(6\rho\) top sites in each direction.
The regularity radius obeys

\[
 \varepsilon_1\le a_1,\qquad B_3\varepsilon_1\le
          \varepsilon_{\rm v}\le a_0.                          \tag{6}
\]

Suppose the paying field satisfies \(\mathcal M^tU=V_t\) on these complete top rows.
If \(E_{S_t}(U)<c\epsilon_t^2<e_*/2\), (5) gives
\(f_{V_t}<2\sqrt c\,\epsilon_t\) there.
The lifted datum is regular at radius \(3\sqrt c\,\epsilon_t\).
The cited real theorem gives the unique regular orbit and curvature
less than \(3B_3\sqrt c\,\epsilon_tL^{-2t}\) in bare units.
Choose \(3B_3\sqrt c<1\), then increase \(X_0\) to obtain (6).
The test passes. This also proves existence under the small-energy assumption.
Thus its total failure gives

\[
 E_{S_t}(U)\ge c_1\epsilon_t^2.                                \tag{7}
\]

Equivalently, the same real theorem contraposed gives a top plaquette
with \(f_{V_t}\ge c_{\rm lin}\epsilon_t\).
This is IN1's H-C-PLAQUETTE witness.
Its bare carrier is (4), not just a spanning sheet from (1).
The constant and smallness choices precede depth and history.

The weighted form needed by W6 is immediate on an owned share:

\[
 \inf_{p\in\mathcal N_0(S_t)}\upsilon(p)\ge c_v\theta_t
 \quad\Longrightarrow\quad
 A_{\mathcal N_0(S_t)}(\upsilon,U)\ge c_vc_1P_t^2.               \tag{8}
\]

This uses \(\theta_t\epsilon_t^2=P_t^2\).
It supplies the nonlinear alternative to Y's weighted row certificate
at 76786–76808. No unproved linear row bound replaces the nonlinear map.

## 3. W2: both cones and the actual gauge action

This section ports Sussman–Alpoge, Y 71893–71957 and 10815–10871.
Write \(k=t-1\). Keep \(S_t\) from §2.
For every tested nonpivot bond in \(\square^{\sim2}\), take its full endpoint double block.
Let \(S_k\) be all internal plaquettes of those double blocks.
Crossing plaquettes belong to \(S_k\).
Set

\[
 P_Q=\mathcal N_0(S_t)\cup\mathcal N_0(S_k),\qquad
 E_Q(U)=\sum_{p\in P_Q}a_p(U).                                  \tag{9}
\]

The second cone ends at level \(k\), not \(t\).
A common bare plaquette is counted once.
The required row identities are

\[
 \mathcal M^kU=V_k\ \text{on every bond of }S_k,\qquad
 \mathcal M V_k=V_t\ \text{on the corresponding complete top rows}. \tag{10}
\]

Keep the top rows of §2 as well.
Equality on the tested nonpivot bonds alone does not imply (10).

Let \(H_{yx}(V_k)\) be the actual contour mean at a noncentral block site.
Let \(\mathcal H_Q\) contain every such mean read by the comparisons.
Define

\[
 G_Q(V_k)=\sum_{(y,x)\in\mathcal H_Q}
          \left(1-\tfrac12\operatorname{Re}\operatorname{tr}H_{yx}(V_k)\right).
                                                                    \tag{11}
\]

Use precisely the factors retained by the soft axial gauge insertion.
For an undefined mean use zero in this energy sum.
Its actual gauge factor is then one, by the total convention.
Small \(E_Q\) will prove that each required mean is defined.
This convention therefore loses no step in the contrapositive.

The birth gauge region is specified, not chosen to fit the estimate.
CA-I 50192–50211 places it outside \(P_t'^{\sim1}\cup\widehat Y^{\sim5}\).
The \(Q_t\)-tests occur one coarse-cell layer inside that region.
CA-I 50251–50265 gives the same one-layer margin for \(Q_1\).
Since \(M\ge L^2M_2\), the third test enlargement remains in that margin.
It contains the block centers and the means in \(\mathcal H_Q\).
These are the contour factors inserted in [c1-repr.md, §4](c1-repr.md).

Suppose

\[
 E_Q(U)+G_Q(V_k)<c_Q\delta_k^2<e_*/2.                            \tag{12}
\]

Apply (5) separately to the two sets, using their common upper bound \(E_Q\).
Their plaquette defects are less than \(2\sqrt{c_Q}\delta_k\).
The tower theorem applies with \(\varepsilon_1=3\sqrt{c_Q}\delta_k\).
Keep (6), and impose \(B_3\varepsilon_1\le L^2c_2^{\rm elem}\).
It gives the background \(W_0=\mathcal M^kU_{t,\square}(V_t)\).
Its double-block curvature is at most \(2B_3\varepsilon_1L^{-2}\).
Both fields therefore have their actual contour means.

The third enlargement contains only the top nodes in these blocks.
Lower-row nodes lie near the tower boundary, outside this enlargement.
Thus a residual gauge fixing the block centers can put \(W_0\) in block axial gauge.
All its required contour means then equal one.
This is the representative used by the actual approximate test.
Its top average is \(V_t\), by the determining constraint and the lift identity.
Equation (10) gives exactly the same average for \(V_k\).

For completeness, the source's reconstruction estimate is

\[
 \begin{split}
 |V_k(b)-W_0(b)|
 \le{}&|\mathcal M V_k(c)-\mathcal M W_0(c)|
       +d_T(b_-)+d_T(b_+)\\
 &+C_L\{\varpi(V_k)+\varpi(W_0)\}.
 \end{split}                                                    \tag{13}
\]

Omit the coarse-row term for an internal bond.
Here \(\varpi\) is the maximum curvature on the full double block.
The contour differences are \(d_T(x)=|H_{yx}(V_k)-1|\).
Y 10815–10871 obtains (13) by replacing means with comb transports.
Internal bonds form comparison loops.
Crossing bonds compare to their coarse average through the full double block.
All multipliers are unitary. This explains both the carrier and the coefficient one.

The first term in (13) vanishes.
By (11), \(d_T(x)\le\sqrt{2G_Q}\).
Hence (13) is at most \(C_L'\sqrt{c_Q}\delta_k\).
Choose \(c_Q\) so that \(C_L'\sqrt{c_Q}<2\).
Every tested nonpivot bond then passes the \(2\delta_k\) threshold.
All existence conditions were established before this conclusion.
Total failure consequently implies

\[
 E_Q(U)+G_Q(V_k)\ge c_Q\delta_k^2.                              \tag{14}
\]

This is the H-C-FLUCTUATION certificate.
The Wilson coefficient must be comparable to \(\theta_k\) on \(P_Q\).
The gauge coefficient is its original \(\theta_k\).
Thus an allocated fraction \(\lambda>0\) gives

\[
 \lambda\left[A_{P_Q}(\upsilon,U)+\theta_kG_Q(V_k)\right]
 \ge c_3\lambda\theta_k\delta_k^2
 =c_3\lambda(A_1/A_0)^2P_k^2
 \ge c_4\lambda P_t^2.                                        \tag{15}
\]

IN1 (1) bounds neighboring frame differences.
For a sufficiently high \(X_0\), \(\theta_k/\theta_t\) and \(P_k/P_t\)
have fixed positive upper and lower bounds.
This justifies the last comparison and the use of the stopped coefficient.
The constants may depend on the fixed threshold amplitudes.

The gauge normalizers remain attached to their original factors.
Equation (15) spends an exponent share; it does not renormalize the measure.
It uses no stored Gaussian coercivity.
A Wilson-only payment would fail to control a gauge change fixing the coarse centers.

## 4. Which history reads preserve W1 and W2

This is the protected-row argument of Sussman–Alpoge, Y 71958–72093.
Its local counterparts are C1 §§2,4–6 and GEOH's Inputs R and P.
The following argument quantifies over records satisfying those adopted rules.

Let \(\mathfrak c\) be the level-\(t\) cell containing the failed test cube.
The two-layer \(Q_t'\) and four-layer \(P_t'\) buffers give

\[
 \mathfrak c^\sim\subset\Omega_t^c\cap D_{\rm birth}.            \tag{16}
\]

For \(t>1\), the birth margin also puts it inside \(\Lambda_{t-1}\).
It avoids older live components and marks.
Alignment and \(M\ge L^2M_2\) put \(\square^{\sim4}\) inside this neighborhood.
The full blocks of (4) remain inside it at every finer level.
The \(Q_t\) double blocks lie in the third enlargement.
Their second cone therefore lies in the same neighborhood.
No paying plaquette crosses the boundary of the available field.

At birth, C1 retains the field and constraint on \(\Omega_t^c\).
It retains the failed indicator and the gauge factors.
For \(t=1\), use the stored bare field on bonds with both endpoints in
\(\Omega_1^c\). This covers (16).

Consider any later operation at level \(m\) containing this birth.
Write \(h=m-N_m\).
The quiet-window rule gives \(t\le h\).
A drop-out remakes only entries of levels strictly greater than \(h\).
Its integrations use field levels at least \(h\).
Thus \(V_{t-1}\), its contour factors and its step-\(t\) constraints survive.
Both determining entries \(\Omega_{t-1}\) and \(\Omega_t\) remain unchanged.
Induction repeats this statement through every containing drop-out.

There are three resulting reads.

| Read | Why it has the exact certificate data |
|---|---|
| Current real background | Its defining constraints reproduce the protected \(V_{t-1}\) rows. Retained one-step constraints give \(V_t\). |
| Compatible drop-out fibre | IN1's fibre imposes those rows and recorded test values at every real evaluation. Its excluded failure is the new root's test. The old birth failure remains. |
| Completed operation's inner Wilson field | On the old core, the localized inner determining set equals the prepared set. New increments have no endpoint there. The protected datum remains \(V^{\rm in}\). |

For the third read, use the adapted constrained representative.
A Landau representative need not literally have the fixed coarse datum.
Gauge adaptation leaves every Wilson plaquette action unchanged.
It does not change the stored gauge factors in (11).
The representative choice belongs to the read, not to a new draw of those variables.
Y 72061–72090 makes this distinction explicit.

The real inner Wilson factor depends on stored variables alone.
A complex exterior supremum does not replace it with a complex Wilson field.
For a drop-out, (7) and (14) hold pointwise throughout the compatible real fibre.
No interchange of a supremum and an integral is used.

If an island or healing absorbs the birth, this outer record stops reading its old payment.
Its earlier history is then inside the absorbed operation.
The protected-row proof does not charge it a second time.
It also supplies no witness for a later operation's own failed test.

These statements verify the carrier and value identities on the adopted rule class.
They do not establish that every revised operation belongs to that class.
That existing realization obligation is stated precisely in §7.

## 5. W5: the cut island's last test

This section ports Sussman–Alpoge, Y 72724–72737 and 76865–76917.
Let \(Y\) be a still-standing second-class island born at level \(m\).
Write \(V_m^{\rm fr}\) for its restored field.
The failed density test is a test of this field.
It is not a test of the earlier prepared inverse field.

The birth determining datum contains every top bond meeting \(Y\).
After island creation, subsequent operations carry those entries through level \(m\).
An eligible containing window starts above \(m\), by the mark quarantine rule.
Thus every compatible real paying field \(\widehat U\) satisfies

\[
          \mathcal M^m\widehat U=V_m^{\rm fr}
          \quad\hbox{on the full final test carrier}.           \tag{17}
\]

These are the island's post-creation entries.
They are not the pre-healing lower entries, which its creation replaced.
An island supplies no later remake levels.
Its retained constraint uses the restored top datum.

Take a failed density cube \(C\) in the six-cell inset.
Its regularity test reads four test layers.
Completing the averaging blocks costs at most one further level-\(m\) unit.
The parameter floor gives

\[
             4M_2R_m+1<MR_m.                                 \tag{18}
\]

For IN1's \(L\ge27\), \(M\ge L^2M_2\) and \(R_m\ge1\),
the inequality follows from \((L^2-4)M_2R_m>1\).
Thus the complete four-block cones remain inside \(Y\).
The inset requirement concerns the whole read, including its blocks.
An assertion only about the test cube's center would not suffice.

Apply the same separated-tower criterion as in §2 on this interior carrier.
Choose \(\zeta>0\) with \(B_3\zeta<1\).
Increase the floor so that

\[
 \zeta\epsilon_m\le a_1,\qquad
 B_3\zeta\epsilon_m\le\varepsilon_{\rm v}\le a_0,\qquad
 \zeta^2\epsilon_m^2\le2e_* .                                 \tag{19}
\]

If all its top plaquettes have defect less than \(\zeta\epsilon_m\),
the regular orbit exists and passes the inset test.
Failure therefore supplies a top plaquette of at least that size.
Use (17) and (5) on its full cone:

\[
 \sum_{p\in P_Y}a_p(\widehat U)\ge c_5'\epsilon_m^2,
                      \qquad P_Y\subset Y.                    \tag{20}
\]

At birth the carrying action has weight \(x_m\) there.
A standing second-class island remains in that level's action region.
The old-core taper is one on \(P_Y\).
The stopped-weight comparison therefore gives

\[
 A_{P_Y}^{\rm carry}(\upsilon,\widehat U)
          \ge c_{\rm cut}\theta_m\epsilon_m^2
          =c_{\rm cut}P_m^2.                                  \tag{21}
\]

Here \(c_5'\) is a certificate constant, unrelated to IN1's frame constant \(c_5\).

The two actions have different arguments and different owners.

| Action factor | Field and use |
|---|---|
| Inner prepared action in the stored operation | The prepared inverse field, built from its old inner variables. SA 17642–17646 displays \(A(x''_m\phi_{\rm c},U''(e^{ig_mB},V''))\). Its earlier certificates pay the inner mass. |
| Carrying action used in (21) | The real field \(\widehat U\), whose protected top rows are \(V_m^{\rm fr}\). It pays the final density failure in the enclosing history. |

SA 17648–17654 retains the island's complementary density test with its operation.
Y 72724–72737 identifies the restored top field and reserves this event for the outer genealogy.
Y 76906–76917 explicitly distinguishes the two action factors.
One cannot charge (21) to the prepared action merely because both carriers lie in \(Y\).
Nor does the fact that the inner mass is at most one supply a new credit.

The analogous drop-out convention is Y 74099–74104.
Its own root failure is excluded from its earlier mass.
A containing operation may charge it only after supplying the whole paying carrier.
This convention does not prove a fresh witness for every other kind of root failure.

Let the outer cut count this island as \(b\le N_{\rm cut}\) artificial creation cells.
Take \(c_G\le c_{\rm cut}/(2N_{\rm cut})\).
Increase \(X_0\) until \(P_m\ge1/c_{\rm cut}\).
Then IN1's required allocation holds:

\[
        b\,c_GP_m^2+\frac12P_m
                         \le c_{\rm cut}P_m^2.                 \tag{22}
\]

If the mark convention uses \(P_m\), require \(P_m\ge2/c_{\rm cut}\) instead.
Both credits spend the same fresh witness after splitting it once.
No inner mass or previously spent creation gain enters (22).

The local C1 retention formula identifies the failed density factor.
It does not, by itself, specify the six-cell inset or prove the action-profile identity.
Those are explicit premises of this match to Y's island operation.
Replacing an unspecified margin by six cells would be a change of construction.
No such change is made here.

## 6. Exactly what reaches W6

This is the allocation of Sussman–Alpoge, Y 76758–76777 and 76811–76937.
The retained coefficient of a birth at \(t\) uses indices no later than
\(t+C_RR_t\). Its profile is a convex combination of those weights.
For every index \(s\) in that profile, IN1 (1) gives
\(\theta_s\ge\theta_t-C_6R_t-c_5\).
IN1 (3) gives \(x_s\ge3\theta_s/4\).
Consequently

\[
       \upsilon(p)\ge\tfrac34(\theta_t-C_6R_t-c_5).
\]

Since \(R_t=O((\log\theta_t)^r)\), choose a uniform floor with
\(C_6R_t+c_5\le\theta_t/3\). This gives \(\upsilon(p)\ge\theta_t/2\).
The local freeze rule is essential.
An arbitrarily later running coefficient would not have this lower bound.

At one birth level, each selected witness lies within two cells of its owning cell.
The source's ordinary allocation has multiplicity at most \(D=5^4\).
Divide the energy by \(D\), and retain a fixed positive integration fraction.
Distinct untouched pieces have disjoint paying shares.
A later mark spends Wilson energy outside its old floor.
The protected birth cones lie inside that floor.
The gauge factors remain assigned to their original level and contour.
These rules prevent the ordinary certificates from spending later-window factors.

The resulting W6 contributions are:

| Witness | Available energy before shared allocation | W6 contribution after allocation |
|---|---|---|
| W1 | Wilson action on \(\mathcal N_0(S_t)\), at least \(c\theta_t\epsilon_t^2\). | A creation gain \(c_GP_t^2\). No gauge or stored Gaussian energy is required. |
| W2 | Wilson action on the union of both cones, plus the original \(\theta_{t-1}G_Q\). | A creation gain \(c_GP_t^2\), using the fixed neighboring-threshold comparison. Both payers are necessary. |
| W5 | Carrying fresh-field Wilson action on \(P_Y\subset Y\), at least \(c_{\rm cut}P_m^2\). | The at most \(N_{\rm cut}\) artificial creation gains and the cut mark in (22). The island's earlier mass is untouched. |

The source ledger is

\[
 A(\upsilon,U)+\sum_j\theta_jG_j(\xi)+\beta_1\sum_j|A_j|^2
                 \ge\sum_e\Gamma_e,\qquad
 \Gamma_e=c_{\rm w}\theta_{t(e)}a_e^2.                          \tag{23}
\]

Equations (8), (15) and (21) supply only the indicated entries of this sum.
W1 uses \(a_e=\epsilon_t\). W2 starts with \(\delta_{t-1}\) and its original gauge coefficient.
Equation (15) converts that payment to the creation level \(t\).
W5 uses \(\epsilon_m\) once, before the allocation (22).
They consume no Gaussian coordinate reserve.
They do not prove that the other events fit within the remaining shares.
In particular, they neither settle W4 nor identify every kept positive form.
The reserve \(\beta>0\) needed by the reference integral remains a separate W6/H-E requirement.
For drop-outs these inequalities must hold at every compatible real evaluation.
They are not estimates of an integral at a selected background.

## 7. Actual-history stopping point

The rule-level proof is complete with the stated source premises.
The unrestricted assertion about our revised histories is not proved.
The missing first input is already registered:

**GEOH-O1, witness specialization.** Every revised history presented to H-C
must obey the adopted class, selector and fate rules on these complete reads.
In particular, an ordinary birth in a containing level-\(m\) operation has
\(t\le m-N_m\). A standing island below that operation has \(s<m-N_m\).
Remakes start strictly above the floor.
The resulting protected rows, indicators and contour slots are the ones retained by C1.

[geoh.md](geoh.md), Definition 2 and its realization paragraph, expressly retains this input.
[cp-triage.md](cp-triage.md), §3, identifies the same residual.
[open-registry.md](open-registry.md) assigns GEOH-O1 to GEOH.
This is not a new unowned witness lemma.
The separate full read-ownership match is GEOH-O2; W6's full allocation also remains open.

Three existing facts must not be mistaken for this realization input.
C1 proves exact positive kernels, but does not choose their complete class selectors.
GEOH proves geometry for records satisfying its Inputs R and P and its class rule.
Y proves the protected-read argument for its stated construction.
None of these statements alone identifies every revised record with that construction.
The CA's open-endpoint quarantine cannot substitute for the adopted closed-endpoint rule;
GEOH already records that distinction.

For W5 the outstanding instantiation must also locate the actual six-cell final test
and its carrying action slot, as specified in §5.
An unnamed inset or an unlabelled Wilson factor does not meet the certificate.
The source's detailed proof does not supply that identity for a different operation.

The task forbids attacking a target already owned elsewhere.
Accordingly, this note stops at GEOH-O1 without reopening its proof lane.
No three-route exhaustion or actual-history counterexample is claimed.
The output is a port and an exact conditional match, with the owned residual exposed.
It grants no scientific status.

| Item | Result in this note | Remaining qualification |
|---|---|---|
| H-C-AVERAGE | Actual four-block coefficient and nonlinear remainder matched to IN1 (15). | Regular-branch ceiling stated in §2; no independent check claimed. |
| W1 / H-C-PLAQUETTE | Total-test certificate and complete cone ported; protected-row match proved on the adopted rule class. | Actual realization of that class. |
| W2 / H-C-FLUCTUATION | Two cones, crossing plaquettes, actual contours and coarse rows matched on that class. | Actual realization and retention of exactly those factors. |
| W5 / H-C-CUT | Interior certificate and fresh-action allocation ported with explicit top-row and inset conditions. | Actual final-test placement and action-slot identification. |
| W6 | The three supplied event entries and their payer types are explicit. | Full ownership, W4, kept coercivity and integration reserve remain open. |

**First open input:** GEOH-O1's actual-history realization, owned by GEOH.
Do not open a duplicate W125 realization lane.
