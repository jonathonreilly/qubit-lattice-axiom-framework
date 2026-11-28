# HCM repair: smooth data on the renewed rim

Check: [Claude's HCM-SC check](../gates/hcm-repair-check.md), FINISH row 520; repairs and HCM-TB follow-up, row 524.

Codex, 2026-11-08. Pinned checkout `1e8cc3962ccbae7cc8d07f162da22e5a01b3a31f`.
Research text. Not an audit. Grants no status. No computer-assisted proof.

Result, corrected after the check: HCM-SC remains open after two genuine routes.
The old Route 1 keeps the obstructing bare data, so it does not count as a repair attempt.
Deleting artificial lower rows gives the distinct HCM-TB route in [hcm-tb.md](hcm-tb.md).
That follow-up stops at TB-BC after three new routes; it does not claim the payment is proved.
The required payment follows conditionally, but the repaired stage and all its consumers are not proved compatible.

## 1. Scope and source premises

The original note is FINISH row 503. Row 524 repairs it at pinned commit `9f5dc5330`.
There is no `library/prior/hcm-repair.md` at this checkout.
The H-C-MARK registry row is open and has no other owner.
The target is the proposed construction change in `gates/hc-mark-check.md`, finding 10.
The earlier fresh-payment counterexample is already in `hc-mark.md` and `prior/lfi.md`.
It is not a counterexample to a smooth replacement.
Finding 9's claims about probabilities are not used here.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Every source result below is theirs, with its stated hypotheses.
Credit Tadeusz Bałaban for the constrained minimizer and large-field methods.

Source keys:

- **Y**: [expanded outline, commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex).
- **SA**: [outline, commit `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
- **I**: [complete account I, commit `31a47c543775`](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).

Line numbers refer to those pinned files. The local SA indices supplied the initial source ranges.
The repository entry point names `docs/ai_methodology/SCIENCE_WORKFLOW.md`, which is absent here.
The task's GOAL and FINISH instructions govern this narrow research note.

“Proved there” means a written source argument, with its hypotheses retained.
“Cited” means that the account invokes Bałaban; it is not a new proof here.

| Premise | Source standing | Exact scope |
|---|---|---|
| Face lift has exact nonlinear averages | Proved there: Y 7223–7246, 13058–13101 | Internal transports are identity; each averaging line crosses one coarse face. |
| Joined collar tests inherit coarse curvature | Proved there: Y 13103–13130 | The defect is not multiplied by the square of the fine mesh. |
| Regular expansion requires bare-scale curvature | Input: Y 61905 | Threshold is proportional to \(\varepsilon_m L^{-2m}\). |
| Interior screening before a stage | Proved there: Y 72243–72323 | The bound uses the joined local level. It excludes the problematic joining collar. |
| Top data of that collar lie outside the old floor | Proved there: Y 72268–72281 | This concerns the original face-lift read set. A new interpolation needs its own read-set check. |
| Constrained minimizer has exact prescribed averages and local-scale bounds | Cited: I 43100–43155 | Bałaban CMP 102b, with localization from CMP 109. The block-scale form is used by statement. |
| Stage domains include simple and hereditary tower conditions | Definition/input: SA 5663–5727, R4–R6 | Real and complex fields, independent currents, every allowed subdomain, both erosion assignments. |
| Bałaban's component class uses size and waiting conditions | Proved source comparison: I 55379–55420 | It does not supply an analytic test for the changed collar. |

The account's minimizer estimate is

\[
 |\partial U(\mathfrak B,D)(p)-1|
 <B_3\epsilon_1\eta^2\ell_{\mathfrak B}(p)^{-2}.
 \tag{1}
\]

Thus a homogeneous top-scale determining set gives the desired mesh factor.
A joined set with bare determining bonds does not give it by (1) alone.
The distinction is geometric, not a choice of the coupling floor.

## 2. The test being changed

The proposed change concerns the **prospective regularity guard of the preparatory R-stage**.
It does not concern the ordinary Gaussian rim test.
Y 63864–63883 gives the stage thresholds and their relation to Bałaban CMP 122a (1.24).
Y 72324–72338 identifies the final-stage member at issue:

\[
 |\partial U^{\rm pr}_{m,X}(p)-1|
 <a_{\rm s}\epsilon_m\eta_m^2,
 \qquad a_{\rm s}=3(1-\beta_{\rm s}/2),\qquad \eta_m=L^{-m}.
 \tag{2}
\]

Here \(p\) is a bare plaquette in the tested part of \(X\cap\Omega_m\).
Some such plaquettes have four artificial determining bonds at the localization boundary.
Those bonds currently receive the face lift of \(V_m\).

The proposed guard keeps (2), including its units.
It replaces the artificial collar datum used to construct \(U^{\rm pr}_{m,X}\).
If lower artificial rows remain, it must use one fine interpolation and its actual successive averages there.
It may instead delete those rows and change the artificial boundary tower, as HCM-TB proposes.
Changing bare values while silently keeping incompatible intermediate values is not a definition of that datum.
Physical retained rows and their delta functions still have their original values.
New artificial rows are auxiliary boundary data, not replacements for the retained physical variables.

The same rule must be used whenever consecutive stages compare this localized background.
Otherwise their common-data response argument loses its premise; see Y 63864–63883 and 64073–64074.
The initial one-step face lift and the terminal density-test lift need not be changed.
They serve different constructions.

Calling a plaquette a level-\(m\) plaquette does not smooth its holonomy.
Replacing (2) by a bound in joined-level units would weaken Y 61905 and SA R4, lines 5672–5685.
That is a different change, and is not used here.

Bałaban's geometric R-class, described at I 55379–55392, does not prove this new guard admissible.
Nor does the absence of this guard from that description permit its deletion from the port.
The account invokes the stage theorem separately at I 54985–55024.
Its local holomorphy conclusion explicitly retains the stage hypotheses.

## 3. The payment, conditional on the repaired bound

This section identifies what a successful interpolation must supply.
It uses the existing ordinary certificate, not a new averaging proof.

Let \(E_{m,X}\) be the top rows read by the interpolation and the rim comparison.
Include every plaquette needed by their datum tests.
Let

\[
 D_{m,X}=\max_{P\ \mathrm{read}}|1-\partial V_m(P)|.
\]

All four-block bare carriers must avoid the old floor.
They must use the actual top averages of the compatible evaluation field.
Assume, for these complete reads, that small \(D_{m,X}\) gives existence and

\[
 |1-\partial U^{\rm pr}_{m,X}(p)|
 \le \eta_m^2\bigl(C_{\rm s}D_{m,X}+b_{m,X}\bigr),
 \qquad b_{m,X}\le a_{\rm s}\epsilon_m/4
 \tag{3}
\]

on **every** plaquette in the changed rim guard.
The term \(b_{m,X}\) includes the old-core response and all seam errors.
An estimate only on the prescribed bonds does not establish (3) on adjacent free plaquettes.
Likewise, an estimate conditional on prior existence does not handle an undefined orbit.

Choose \(d=a_{\rm s}/(4C_{\rm s})\).
If \(D_{m,X}<d\epsilon_m\), (3) gives a bound below half the threshold in (2).
Thus a failed guard, including undefinedness under the existence premise, implies

\[
 |1-\partial V_m(P)|\ge d\epsilon_m
 \quad\hbox{for some read plaquette }P.
 \tag{4}
\]

The exact-cone certificate is proved in Y 71745–71844, with its carriers defined at Y 71714–71744.
For this singleton \(P\), it gives

\[
 E_{\mathcal N_0(P)}(U)
 \ge \min\{d^2\epsilon_m^2/4,e_*/2\}.
 \tag{5}
\]

At a sufficiently weak coupling, \(d^2\epsilon_m^2/4\le e_*/2\).
Hence a retained carrying coefficient at least \(c_w\theta_m\) gives
\(c_wd^2P_m^2/4\), since \(\theta_m\epsilon_m^2=P_m^2\).
This is exactly the certificate used for the distinct island event at Y 76887–76917.
The island event itself is not being substituted for the rim event.

One must still allocate this energy once.
Y 76813–76864 proves the old mark-halo allocation for its stated carriers.
A changed interpolation must fit those carriers, or prove the corresponding enlarged-carrier allocation.
That halo adds only two level-\(m\) unit-cube layers, by Y 76817–76820.
The check raises the possibility that the rim lies beyond that halo; a larger-carrier allocation would then be an input.
The size comparison alone does not establish this: Y 63760–63771 identifies the localization box \(X\) with the component.
The \(O(M)\) final integration box is the different box \(\Lambda^{\rm pr}\), Y 63825–63836.
See [hcm-tb.md](hcm-tb.md), §5. Complete carriers inside \(X=C(u)\) fit the original halo.
Any carrier extending beyond \(C(u)^+\) still needs the larger allocation, with floor exclusion and bounded overlap.
Merely placing its output bond outside the floor does not place its full input there.
After a fixed overlap division and an integration reserve, write the available share as \(c_*P_m^2\).
The constants \(c_w,c_*\) are inputs from the retained action and ownership rules.

For the consumer, write \(r_t=\widehat r_t\) in IN1's notation:

\[
 r_t=4c_1M^4R_t^5+\kappa_1,\qquad
 T_t=C_TR_t,\qquad q_t=C_{\rm cnt}T_tr_t.
 \tag{6}
\]

The genealogy inequality is IN1 (31), lines 484–506.
Its reserve argument at lines 508–529 accepts \(q_t\) for each renewed mark.
This substitution was already proved in `hc-mark.md`, §2.
There is no need to require a new payment of \(P_t/2\).

For completeness, put \(x=\log\theta_t\ge1\).
Since \(R_t\le Lx^r\),

\[
 q_t\le Kx^{6r},\qquad
 K=C_{\rm cnt}C_T(4c_1M^4L^6+\kappa_1L).
\]

In the normalization \(P_t=x^{p_0}\), it suffices to choose
\(x^{2p_0-6r}\ge K/c_*\).
Any fixed normalization factor in \(P_t\) is absorbed into \(c_*\).
IN1 assumes \(p_0>6r\), so this choice is available after all price constants.
It gives \(c_*P_t^2\ge q_t\), uniformly in the absolute level and cutoff.
This proves the payment implication from (3), the read-set conditions, and ownership.
It does not prove those premises for a new collar.

## 4. The first supplier: HCM-SC

**HCM-SC means an exact local smooth collar insertion. It is sufficient, not necessary.**
It is a statement about replacing artificial determining data.
It is not the global same-system extension called LOC-flat in `dom.md`, Lemma 12.
That extension and general later-domain admission remain with the DOM-FULL registry row.

Fix one actual stage geometry and its old physical common rows.
The repair may change the artificial tower and delete its lower artificial rows.
The conditions below apply only to artificial rows that remain.
On the source collar, common rows have its top level; see Y 13116–13120.
No freedom to overwrite old physical finer rows is assumed.
Let \(\mathcal P_{\rm rim}\) contain every rim plaquette stencil touched by the replacement.
Include stencils crossing the interface with the unchanged part.
Take all averaging carriers in the source's fixed frames.

The supplier must choose a field-independent top read set \(E_{m,X}\).
Its complete four-block carriers must lie in the available mark halo outside the old floor.
A larger halo is allowed only with a supplied bounded-overlap and floor-exclusion proof.
Its size and shape are recorded in the new local read sets.

For all real top data with \(D_{m,X}\le d_0\), it must construct a fine connection
\(\mathscr I_{m,X}(V_m)\) on those padded collar stencils, with these properties:

1. Its level-\(m\) averages equal \(V_m\) on every common top row.
   Every retained lower artificial row is its actual iterated average; deleted rows impose no condition.
   Its mixed tests use those same averages on their complete carriers.
   It agrees with every old common row encountered by the replacement.
2. It satisfies
   \[
   \sup_{p\in\mathcal P_{\rm rim}}
        |1-\partial\mathscr I_{m,X}(V_m)(p)|
          \le C_{\rm s}D_{m,X}\eta_m^2.                 \tag{7}
   \]
   The constants \(d_0>0,C_{\rm s}<\infty\) are independent of depth, volume and history.
3. It reads only the declared top data and fixed geometry.
   Identical complete local inputs produce identical outputs in the specified frames.
   Gauge covariance uses the induced gauges on all intermediate rows.
   It has compatible holomorphic continuations on the admitted local datum charts.
   Their radii and physical-norm bounds are uniform in depth.
4. Under the supplied hypotheses of the unchanged parts of the stage, this insertion gives (3).
   It includes existence when \(D_{m,X}<d\epsilon_m\).
   The resulting critical field, with its independent current, belongs to every R4–R6 domain read by that stage.
   The assertion holds at each permitted stopping stage, on the terms' original creation domains.
   The collar-response and gauge comparisons used below retain their stated bounds with fixed new constants.
   All new input carriers are included in those comparisons.

Even the real, curvature part of this statement is not supplied by the cited minimizer theorem on the existing joined set.
The source proves exact averages and smoothness separately on other geometries.
It does not identify them with this replacement while retaining its read set.

HCM-SC is the local analytic supplier for the mark argument.
It has no history sum, Wilson coefficient, payment or entropy in its conclusion.
Its fourth clause is essential: SA R4–R6 cannot be inferred from (7).
R4 also needs controlled local gauges, complex potentials and independent currents.
R5–R6 quantify over every admitted subdomain, erosion and tower truncation.
The source explicitly retains these application conditions at I 49495–49546.

## 5. The old obstruction and two routes to HCM-SC

### Old Route 1: the unchanged-boundary obstruction, not a repair route

This route keeps the joined determining set and applies Bałaban's constrained minimizer there.
It preserves the original exact constraints and locality.
It does not repair the rim.

The four bonds of the plaquette in Y 72324–72338 are prescribed individually.
Minimization cannot change their product.
For a nonzero top defect \(a\), that bare defect remains \(a\).
Equation (7) would require \(a\le C_{\rm s}aL^{-2m}\).
For \(L^{2m}>C_{\rm s}\), this is false.

This is a reuse of their face-lift obstruction, not another history construction.
The account's bound (1) agrees with it: the local determining scale there is bare.
Changing the minimizing functional without changing these four constraints cannot help.

This proves why the data must change. It is not one of the three routes required by stopping condition (c).

### Route 2: minimize at the top scale, then patch the collar

A homogeneous determining set at level \(m\) removes Route 1's obstruction.
On admitted complete top data, I 43100–43155 gives exact averages and

\[
 |1-\partial S_m(V)(p)|<B_3D\eta_m^2.
 \tag{8}
\]

This is a cited Bałaban input, not a proof of HCM-SC.
The homogeneous problem requires its full prescribed datum.
An arbitrary extension across the old core can read the floor or fail its smallness hypothesis.
Taking a global minimizer and then restricting its output does not remove those input reads.
Exponential response bounds, such as Y 7668–7728, do not make those reads identically zero.

The natural local attempt is to use padded top-scale problems and join their outputs.
The padding must put the **whole** tested rim inside their smooth region.
The joined output must then preserve all common coarse rows.
A bare-bond splice does not preserve the curvature bound, even for compatible flat inputs.

There is a better conditional candidate than such a splice.
On an admitted padded auxiliary tower, put every target rim stencil in its top member.
Prescribe the top datum there and use the source's usual face data only at the auxiliary outer boundary.
The minimizer then gives (8) on the target rim.
Defining its intermediate artificial rows by its own averages ensures exact composition.
This ports the same mechanism used for interior density tests at Y 98117–98146.
It does not put the **original stage minimizer** in that auxiliary top member.
Their determining sets, constraint variations and local scales differ.
Identifying the two minimizers, or transporting their domains, is an additional step.

Here is a hand check of that failed splice.
Work in level-\(m\) units, with \(\eta=L^{-m}\le1/4\), in a commuting SU(2) subgroup.
Let \(T=\operatorname{diag}(1,-1)\), and choose \(0<a<1/4\).
Set

\[
 \phi(x)=a\sin(2\pi x_1),\qquad g(x)=e^{i\phi(x)T}.
\]

The fields \(S_0=1\) and
\(S_1(x,\mu)=g(x)^{-1}g(x+\eta e_\mu)\) are flat.
At every top site, \(g=1\).
Gauge covariance of the actual average gives \(\mathcal M^m S_0=\mathcal M^m S_1=1\).
This uses the endpoint covariance proved in SA 8090–8104.
Their top data agree exactly.

Join their potentials by a cutoff \(\chi(x_2)\) which changes from zero to one across one fine edge:

\[
 W_1(x)=\exp\{i\chi(x_2)[\phi(x+\eta e_1)-\phi(x)]T\},
 \qquad W_\mu(x)=1\quad(\mu\ne1).
 \tag{9}
\]

On the crossing 12-plaquette at \(x_1=0\), its angle has magnitude
\(a\sin(2\pi\eta)\ge4a\eta\).
The inequality follows from concavity of sine on \([0,\pi/2]\).
Since the angle is below \(\pi\), its matrix defect is at least \(8a\eta/\pi\).
Thus this splice is not flat, although its input top curvature is zero.
It violates (7), whose right side is zero in this example.
It also has the wrong mesh order for any bound \(Ca\eta^2\).

Interpolating the gauge itself repairs this particular flat example.
It does not establish the curved, exact-average gluing rule.
Using a top-scale transition width avoids this specific mesh loss.
It then requires a padded collar, coherent gauge transitions, and an exact correction of all affected averages.
None of those corrections follows from (8).
The smooth output of a local minimizer is not automatically the output of neighboring local problems on their overlap.

Even a single padded auxiliary tower leaves this insertion problem.
The supplied collar comparison gives the plaquette factor \(L^{-2\lambda^W(p)}\), at Y 13390–13412.
At a bare joined row this is one.
A distance bound independent of \(m\) cannot turn it into \(L^{-2m}\).
For example, \(Ce^{-cM R_m}\le L^{-2m}\) fails for large \(m\) at fixed top coupling and fixed \(R_m\).
A new argument could exploit additional layer crossings or a homogeneous relative estimate.
It must prove that estimate on the actual stencils, including free crossing plaquettes and tower reads.
The source's inset comparison does not assert it there.

The required new argument is specific to the replacement collar.
I have not reopened DOM's different global extension problem.
The CMP 109/116 small-field theorem is also conditional here; see I 4136–4159 and 4191–4208.

**Failed step:** localizing and gluing the homogeneous smooth solution while preserving the exact collar constraints and read sets.

### Route 3: use the explicit smooth linear lift, then correct the mean

There is already a useful smooth lift in the outline.
SA 8852–8946 proves an exact right inverse of the flat plain average.
SA 8985–9037 proves its supremum and curl estimates.
With \(N=L^m\), it gives

\[
 P^{[m]}w=A,\qquad
 \|dw\|_\infty\le16N^{-2}\|d_NA\|_\infty.
 \tag{10}
\]

This result is ported. It is not derived again here.
Its scope is linear flat data; SA 9049–9055 explicitly retains the nonlinear and domain comparisons.

The exact correction uses the inverse of

\[
 \mathcal A_N=\prod_{\lambda=1}^4
 [a_0I+a_1(T_\lambda+T_\lambda^{-1})],\quad
 a_0=\frac34+\frac1{4N^2},\quad
 a_1=\frac{1-N^{-2}}8.
 \tag{11}
\]

For \(N>1\), this is not a finite-range inverse.
Here is an elementary support check.
Restrict to arrays constant in three directions.
The other three factors act as one, since \(a_0+2a_1=1\).
If a finitely supported sequence \(z\) solved
\([a_0I+a_1(T+T^{-1})]z=\delta_0\), let its first and last nonzero indices be \(l,r\).
The output has nonzero entries \(a_1z_l\) at \(l-1\) and \(a_1z_r\) at \(r+1\).
Both would have to be at zero.
That requires \(l=1\) and \(r=-1\), a contradiction.
The same argument excludes a uniformly bounded-range inverse on arbitrarily large tori.

The subsequent interpolation does not remove the tail in general.
Take a coarse 1-form with only its second component nonzero, equal to \(\delta_0\) in the first coordinate.
Make it constant in the other coordinates.
Its inverse coefficient is the sequence \(z\) above.
If the first difference of \(z\) had finite support, \(z\) would be constant on each tail.
The homogeneous equation there, with \(a_0+2a_1=1\), forces both constants to vanish.
That would make \(z\) finitely supported, which was just excluded.
The interpolation identity \(dI_1=I_2d_N\) is proved in SA 8791–8851.
At fine plaquettes based at coarse nodes, its 12-component samples this difference times \(N^{-2}\).
It therefore has a tail too.
The plain-average correction is a gradient and cannot change this curl.
Thus the particular exact lift (10) is not a local collar rule.

Truncation restores finite dependence but loses exact averaging.
In one direction put \(B=(a_1/a_0)(T+T^{-1})\).
The truncated inverse \(a_0^{-1}\sum_{j=0}^{J}(-B)^j\) leaves the exact residual
\((-1)^JB^{J+1}\).
Its coefficients are nonzero on suitable data for every finite \(J\).
Smallness of that residual is not an equality in a delta constraint.

The available finite pivot chart does correct averages exactly.
Its own coefficient is \(L^{-3}I_3\), proved at SA 8165–8199.
It is not a smooth distributed correction.
At the identity, a commuting one-pivot change of angle \(\sigma\) changes its coarse log by \(L^{-3}\sigma\).
This equality is exact on the small abelian arc: the contour terms contain no pivot, and exactly \(L\) paths read it.
A neighboring bare plaquette with no other changed edge acquires angle \(\sigma\).
Hence correcting a bare-to-level-one row error \(r\) can create curvature of order \(L^3r\).

To retain (7) at a bare rim, this correction would need

\[
 |r|\le C D_{m,X}L^{-2m-3}.                         \tag{12}
\]

A bound on this row error only by \(CD_{m,X}^2\) would not suffice.
Neither would a fixed truncation error times \(D_{m,X}\).
No identification of a top-row residual with this bottom-row residual is asserted.
Transporting residuals through all levels with the needed scale factors is itself required.
At fixed positive \(D_{m,X}\), (12) becomes arbitrarily stronger as the absolute level increases.
A coupling floor is chosen before that level.
Increasing the truncation range with \(m\) also loses the fixed local read footprint.
The component's top-scale size can stay fixed while \(m\) increases.

One could instead seek an exact **smooth distributed** nonlinear correction.
That correction, with the needed support and seam compatibility, is precisely the missing part of HCM-SC.
The pivot example does not show that every such correction fails.

**Failed step:** upgrading the known linear smooth lift to a local nonlinear exact section without concentrating curvature.

### HCM-TB: retain the top level at the artificial boundary

CA-I 43000–43004 gives a lower bound on the boundary tower, not a forced descent there.
Keep the ambient level-\(m\) rows at the outer join and retain the erosion toward the old core.
Delete the artificial lower rows. Use the constrained minimizer on this changed determining set.
Its top averages are exact constraints. There is then no collar face lift to smooth.
The claimed rim scale is \(\ell_{\mathfrak B}=\ell_m\), so (1) has the desired factor \(L^{-2m}\).
Applying that theorem at a free outer boundary, and preserving its consumers, still needs proof.
This route is pursued in [hcm-tb.md](hcm-tb.md); a padded localized layer reduces to the same question.

## 6. Consumers of the face lift

I searched Y and I for `face.?lift`, and followed the named collar-comparison labels in Y.
The literal face-lift phrase has no match in I.
That is not evidence that I has no relevant constraints; its semantic interfaces appear in the last rows below.

The narrow proposed change is confined to the artificial collar of an R-stage background.
A global replacement of the face lift would change the independent constructions listed here too.
“Unchanged” below means that their definitions retain the old lift.
It is not a proof of any new evaluation in their domains.

| Consumer and source lines | Effect of the proposed change |
|---|---|
| Initial exact field, first-step chart, uniqueness, response, gauge covariance and common complex charts: Y 7223–7264, 7309–7332, 7507–7527, 7668–7742, 8013–8041, 8380–8401 | Unchanged. These are fixed one-step constructions. Their estimates do not prove depth-uniform rim insertion. |
| Joined collar data and mixed tests: Y 13058–13130 | Changed at the R-stage use. Exact top means alone do not identify every mixed row. HCM-SC(1) must supply the whole averaging diagram. |
| Datum descent and its two radii: Y 14977–15012 | The original descent is unchanged. It only asserts an approximate seam average in general. It cannot supply exact repaired seam constraints by identification. |
| Correction of regular trials and fixed-step face-lift corollary: Y 34888–34900, 35166–35249 | Unchanged. The former requires a regular fine trial; the latter explicitly excludes iterated face lifts as uniform trials. |
| Real collar alignment and response: Y 13315–13414 | Needs a new alignment and admitted comparison for the inserted datum. Its existing curvature factor uses the joined level. |
| Product descent in the common old frame: Y 37276–37307 | Its original comparison lift remains available. Replacing the actual collar requires new discrepancy bounds and coherent intermediate frames. The displayed matrix identity alone supplies neither. |
| Ordinary strip localization and shifts: Y 62432–62510 | The ordinary localization remains unchanged. Comparisons involving a repaired stage require its new domain and complete-carrier bounds. |
| Canonical holomorphic collar target and covariance: Y 62717–62805 | Its original target reads one top bond and two full blocks. A changed target needs its own gauge law, holomorphy and declared carrier. Curvature control is insufficient. |
| Strip/density comparison and prefinal/final inset read: Y 63182–63214, 64050–64087 | Exact top-row preservation keeps the ordinary test-cube datum identical. Comparing the repaired stage with that datum still needs HCM-SC(4). |
| Prefinal exterior datum tests: Y 64088–64107 | The old tests reduce to identity or lifted top holonomy. With HCM-TB they become actual top-row tests. Existence and subsequent comparison on the changed tower still need proof. |
| Stage curvature estimate at the artificial join: Y 71368–71382 | The old face lift transfers the top datum bound. HCM-TB deletes those artificial tests; its full free-boundary curvature estimate must replace their use. |
| Inset positive evaluations and prospective global orbit: Y 64568–64617, 65536–65573 | These distinguish the interior seam from the outer face lift. Their inset and unchanged-global-row arguments do not cover the new full rim. |
| Literal final regularity guard: Y 72324–72338 | This is the changed test of §2. Its numerical threshold stays fixed. |
| Terminal product-ball and action bound: Y 98111–98163 | Unchanged. Its tested plaquettes already lie inside the top member. It is a useful model for the auxiliary tower, not a full-rim stage theorem. |
| Linearized localized read: Y 102096–102126 | The ordinary localization is unchanged. A changed caller needs the new comparison before its derivative can be taken. |
| Common-exterior precision comparison: Y 103250–103290 | It needs identical complete local inputs and a common joined background. Nonlocal completion of the rim datum would invalidate that premise. |
| Lower/upper localized readout comparison and datum ball: Y 104134–104225 | The original localizations remain. Any repaired-stage use must retain the ancestor frames, logarithmic chart bounds and exponential collar estimate. |
| Cutoff comparison on a test-cube tower: Y 134088–134131 | Unchanged by the collar-only modification. Its lifted test-radius datum is an independent localization, like Y 98111–98163. |
| Exact constraint manifold: I 43100–43155 | The minimizer solves its prescribed constraint problem. It does not prove equivalence between two different determining systems. |
| Tower localization: I 45115–45160 | The proposed outside-reblocking route requires compatibility between coarse constraints crossing the cut and finer constraints in the smaller tower. It is explicitly unproved there. A changed caller must supply its corresponding comparison. |
| Real gauges and stopped-stage spaces: I 49495–49546; SA 17433–17447 | Each term keeps its creation domain, and stopped stages retain their actual determining sequence. New collar data need admission there; the old action sequence cannot be silently changed. |
| Preparatory boundary theorem: I 54985–55024 | The theorem assumes the stage theorem and its analytic spaces. Its locality conclusion cannot be applied before verifying the changed reads. |
| Bałaban's R-class and retained factors: I 55379–55420 | The geometric class and old stored factors do not prove this analytic insertion or provide another energy copy. |

The simple partition identity survives any specified Borel replacement guard:
\(\widetilde\chi+(1-\widetilde\chi)=1\).
That identity proves neither the positive expansion nor a gain on the negative branch.
No full consumer-preservation claim is made here.

## 7. Result and status

**The original claim of stopping condition (c) is withdrawn. Only two genuine repair routes were tried.**
The old Route 1 preserves the very boundary data that HCM-SC proposes to replace.
Route 2 supplies a smooth auxiliary field but not its insertion into the original stage and all its domains.
Route 3 supplies a smooth linear inverse but not a local nonlinear correction with the required curvature scale.

The splice and pivot examples refute those recipes, not every smooth repair.
There is no new counterexample to H-C-MARK in this note.
The source's old face-lift counterexample does not refute a correctly inserted smooth collar either.

The next supplier may prove the insertion clause or delete the artificial lower rows by HCM-TB.
It must control free rim stencils as well as the four-bond determining plaquettes.
A homogeneous minimizer estimate alone would leave the same unproved step.

| Claim | Status | Scope or source |
|---|---|---|
| Exact face-lift averages and old collar identities | Ported from Y 7223–7246, 13058–13130 | Proved there; no fine smoothness asserted. |
| Old full-rim obstruction | Ported from Y 72324–72338; `hc-mark.md` | Already known; not a counterexample to the proposed smooth replacement. |
| Homogeneous constrained minimizer and its mesh factor | Input, cited at I 43100–43155 | Bałaban's stated block-scale theorem on its own admitted determining set. |
| Auxiliary-tower interpolation on its admitted top inset | Proved here as a conditional application of that input | §5, Route 2; exact averages, not original-stage domain transport. |
| Stage domain and stopped-space requirements | Ported definitions/inputs: SA 5663–5727, 17433–17447; I 49495–49546 | No new R4–R6 admission proof. |
| Exact-cone Wilson certificate | Ported from Y 71714–71844 | Proved there; complete carriers and actual physical averages required. |
| Mark ownership and carrying action | Input; source argument at Y 76813–76864 and IN1 H-C | Must be matched to any changed read footprint. |
| Bound (3) implies an ordinary witness and payment \(q_m\) | Proved here, §3 | Conditional on existence, complete reads and retained ownership. |
| Unchanged bare face constraints cannot smooth their plaquette | Proved here from the ported identity, Route 1 | Defeats fixed-boundary minimization. |
| Direct potential splice can create curvature from flat, equal-top-data fields | Proved here, (9) | Does not exclude coherent gauge gluing. |
| Exact smooth flat linear lift | Ported from SA 8852–8946, 8985–9037 | Proved there; nonlinear and domain scope excluded at SA 9049–9055. |
| Its convolution correction has no finite-range inverse | Proved here, (11) | Support argument, independent of any numerical calculation. |
| A one-pivot correction need not preserve bare-scale smoothness | Proved here using SA 8165–8199 | Exact commuting calculation; a distributed correction remains possible. |
| All changed consumers retain their bounds | Input — not established | Specific dependencies are listed in §6. |
| **First open input: the changed-boundary supplier in HCM-TB** | **Input — see [hcm-tb.md](hcm-tb.md)** | **HCM-SC is a sufficient alternative, open after two genuine routes. H-C-MARK is not proved here.** |
