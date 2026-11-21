# HCM-TB: a top-level artificial boundary

Codex, 2026-11-08. FINISH row 524. Pinned checkout `9f5dc53301400b4c38c418dc8d2386f7445e73ed`.
Research text. Not an audit. Grants no status. No computer-assisted proof.
New calculations by Codex; not yet checked by another provider.
Companion check: [hcm-repair-check.md](../gates/hcm-repair-check.md).

Result: stopping condition (c). TB-BC, §4, remains open after three distinct routes.
The payment is conditional. This note does not refute HCM-TB or prove all its consumers compatible.

## 1. Scope and ports

The target is the renewed-rim payment in H-C-MARK, with IN1's price \(q_t\).
No `library/prior/hcm-tb.md` exists at this checkout.
The registry's H-C-MARK row has no owner. I found no existing HCM-TB proof there.
CR and DOM-FULL concern their original determining systems. They are not reopened here.
In particular, CA-I's outstanding outside-reblocking lemma is not assumed proved.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
The definitions, background results, geometry and energy certificate cited below are theirs.
Credit Tadeusz Bałaban for the constrained variational and localization methods.
Use the pinned **Y**, **SA** and **CA-I** source keys of [hcm-repair.md](hcm-repair.md), §1.
All line references below use those versions, not a later revision.

The SA index was searched before the source excerpts.
The relevant entries are chunks 05 (R4–R6), 09 (backgrounds and comparison),
10 (the bare boundary), and 11 (finite-box boundary forcing), with `obligations.md`.
The CA index supplies §4.12's determining sets and §4.13's outstanding localization input.

| Port | Source | Standing retained here |
|---|---|---|
| Boundary tower has a lower distance bound | CA-I 42985–43006 | Definition/hypothesis. It does not force descent at the outer boundary. |
| Constrained field has exact prescribed averages | CA-I 43098–43110 | Definition. It asserts no existence. |
| Local block-scale curvature and current estimates | CA-I 43113–43155 | Cited input, explicitly used there by statement. |
| Weighted datum-profile estimate | Y 12450–12515; SA 9678–9684 | Conditional on the regular construction and its local improvement. The absorption argument is supplied. |
| Joined-data and real comparison construction | Y 12962–13132, 13223–13427 | Uses the separated tower, including its bare outer collar. |
| Boundary force must enter the difference equation | SA 12226–12292, BGR28–BGR30 | Conditional inverse estimate. No free-boundary inverse is supplied by this argument. |
| Exact-cone energy certificate and payment implication | Y 71714–71844; `hcm-repair.md`, §3 | Already supplied. They are not re-derived here. |

## 2. What deleting the artificial rows does

Let \(X\) be an actual stage localization box. Its outer collar lies in ambient level \(m\).
Keep the erosion toward the old core. At the artificial exterior replace
\(\Theta_q=A_q\) by \(\Theta_q=X\) for \(q\le m\).
Take only the physical ambient rows there. Do not retain their lower face lifts.
Call the resulting determining partition \(\mathfrak B^{\rm TB}\).
Only complete blocks and rows with both endpoint blocks in \(X\) are included.
The inner mixed rows retain their original definitions and values.

For a field \(U^{\rm TB}\) in the prescribed constraint manifold,

\[
 M_{\mathfrak B^{\rm TB}}U^{\rm TB}=D.
 \tag{TB1}
\]

This equality is exact. It does not use a correction of approximate averages.
There is no condition on a deleted artificial lower row.
If the free-boundary problem has the cited regular solution, its rim scale is \(\ell_m\), and

\[
 |1-\partial U^{\rm TB}(p)|
 \le B_3\varepsilon_1\eta^2\ell_m^{-2}
 =B_3\varepsilon_1L^{-2m}.
 \tag{TB2}
\]

Here \(\eta=L^{-k}\) and \(\ell_m=L^{m-k}\), as in CA-I 42952–42954.
Every block meeting the full one-step enlargement of \(p\) must have level \(m\).
Merely assigning that level to its corner would not give (TB2).
The homogeneous outer collar supplies this condition for rim stencils clear of the inner seam.

The physical datum read set does not grow in this definition.
The former face lift read these same top rows, Y 13058–13130.
Deleting its auxiliary rows introduces no exterior datum.
A selected minimizer on \(X\), if it exists uniquely in the chosen slice, therefore reads only \(X\).
Uniqueness and a common slice are needed for equality of outputs at equal inputs.

The gap changes. For \(q<m\), points of \(\Omega_{q+1}^{\rm TB}\) approach \(X^c\).
Their distance to \((\Omega_q^{\rm TB})^c\) has infimum zero in the closed-cell convention.
It cannot exceed the required positive \(\rho\xi_q\).
Thus Y 13019–13034's exterior separation check does **not** survive verbatim.
The interior gaps remain, but the old theorem on separated sequences cannot simply be applied.

## 3. The uses of that gap

I followed `mb:eroded-tower`, `mb:tower-gap`, `mb:restriction-identity`,
`mb:boundary-comparison` and `mb:real-collar-norm` in Y.
I also searched its bare-boundary, boundary-layer, \(W^c\), and face-lift passages.
This exposed uses beyond the face-lift list in the earlier note.

| Use | Source | Effect of HCM-TB |
|---|---|---|
| Alignment, separation and contained test carriers | Y 12985–13130 | Top blocks still align. Exterior separation must be replaced by a free-boundary theorem. Inner mixed tests retain their complete carriers. |
| Factorization of constraints under restriction | Y 12764–12838 | Internal coarse rows remain exact. A cut through a complete coarse carrier cannot use the old descent algorithm without checking that carrier. |
| Restriction preserves criticality | Y 12839–12866 | Free boundary variations can change omitted plaquettes. Equality of the retained averages no longer removes this boundary force. |
| Restricted-action current | Y 12876–12921; 13440–13464 | The old estimate is in bare units at the cut. It does not give a top-scale current bound. |
| Real collar alignment and response | Y 13223–13427 | The old source is a discrepancy of determining data. HCM-TB also changes the boundary variational problem. |
| Hereditary tower and gauge admission | SA 5663–5727; CA-I 49495–49546 | R4–R6 still apply on every required subdomain. Rim curvature alone does not prove them. |
| General gap certificate | Y 13910–13961 | Its exterior-gap entry is false for the changed tower. The unchanged interior entries remain usable. |
| Flat field-row decomposition | Y 27666–27729 | Its boundary removal uses \(Q_0v=v\). There is no such identity on a top-level collar. |
| Moving complex slice | Y 28836–28860 | Its boundary norm uses \(\ell=\eta\). Substituting \(\ell=\ell_m\) changes its estimate. |
| Slow cutoffs and commutators | Y 31397–31445 | A missing-neighbour graph-Laplacian term is first order at the boundary. The old scale cancellation is lost. |
| Joined strip current | Y 62926–62954 | The proof explicitly locates every changed-action bond in layer zero. The same bound cannot be assigned level \(m\). |
| Consecutive stages, ordinary reads and the final guard | Y 63864–63883, 64050–64107, 72243–72338 | Require a comparison on admitted common domains. Their thresholds are kept. |
| Localization across a new cut | CA-I 45115–45160 | The required coarse/fine compatibility is explicitly outstanding. That route cannot supply the changed-boundary comparison. |

The last three operator rows are not claims that their conclusions are false for a free boundary.
They identify where the published arguments need a different boundary estimate.
Ordinary test-cube localizations may keep their old descending towers.
That does not by itself compare them with the new stage background.

### What the two Bałaban papers actually give

CMP **102** (1985), 277–309, starts with separated domains, equation (1), pp.277–278.
Theorem 1 uses the spaces (2), (6), (8) and the mixed-data condition (7).
Its bounds (9)–(10) concern the stated enlarged cubes inside those domains.
The induction constructs a constrained trial by (11)–(14), then works in (19)–(21).
These are the method's inputs, not a theorem for arbitrary new boundary conditions.

CMP **109** (1987), 249–301, defines its local complex spaces in (1.11)–(1.16), pp.262–263.
Condition (iv) uses maximal domains satisfying the earlier separation conditions.
The tower bounds are on the two-layer inset.
Lemma 4, (3.53), p.280, retains those spaces and its hypotheses.
Its free-boundary replacement of \(H_j(\square_0)\) near (4.35), p.290,
is an interior linear-response comparison, with an exponential distance factor.
It is not a full-rim nonlinear theorem on the changed determining set.

Therefore CA-I 43122–43133 states a broader block-scale input than these excerpts alone establish.
One may use that input conditionally, exactly as CA-I does.
Its wording does not discharge the free-boundary extension requested in this task.

## 4. One supplier: TB-BC

**TB-BC is the top-boundary background and comparison lemma.**
It concerns only the actual boxed stages with the modified exterior of §2.
It does not ask for a smooth extension of arbitrary data through an old core.
Keep all unchanged stage hypotheses, physical constraints, independent currents,
creation domains, stopping stages and interior tower constructions.

Let \(v(\tau)\) be the defects of the actual determining tests.
Use their complete carriers and the original layer metric inside \(X\).
For sufficiently small \(\sup_\tau v(\tau)\), TB-BC asserts the following.

1. The free-boundary constrained problem has a regular critical orbit and the required local analytic slices.
   They satisfy (TB1), read only the declared data in \(X\), and agree at identical complete inputs.
2. The native weighted-profile estimate holds up to the top rim:
   \[
   |1-\partial U^{\rm TB}(p)|
   \le C\eta^2\ell(p)^{-2}
       \sup_\tau e^{-\delta d(p,\tau)}v(\tau).
   \tag{TB3}
   \]
   Here \(C,\delta\) do not depend on depth or history.
   Small datum tests must imply existence before (TB3) is used.
3. On the actual comparison reads inside \(X\), the old collar-response bounds remain valid,
   with fixed new constants, on the original common analytic domains.
   Include the comparison potential, its required derivatives, full-stencil currents and node gauges.
   Retain R4–R6, independent-current radii, gauge covariance and stopped creation domains.
   The difference equation must include the boundary variation of the truncated action.

Clause 3 does **not** bound the restricted-action current of an arbitrary ambient field at a cut.
That current can be large; the next calculation proves it.
At those cut bonds its contribution is a boundary force, not a small volume current.
Nor does clause 3 require a comparison-current bound on stencils excluded by the original consumer.
This avoids adding a stronger, false requirement to the repair.

This is the first missing supplier for HCM-TB.
The following three attempts all change the boundary; none keeps the four old bare data.

### Route A: apply the stated minimizer input and reuse datum response

CA-I 43128–43150, read as a hypothesis for its whole stated class,
would give the real orbit and (TB2).
The comparison step would then try to repeat Y 13298–13362.
The retained top data of the ambient restriction and of the new minimizer agree.
But the ambient restriction need not be critical for the new free-boundary action.
Its difference is therefore not a response to determining-data changes alone.

Here is the boundary calculation behind that failure.
Use top units, \(\eta=L^{-m}\), and \(T=\operatorname{diag}(1,-1)\).
On a rectangular lattice patch and its exterior take

\[
 U_1(x)=1,\qquad U_2(x)=e^{i\eta f x_1T},\qquad U_3=U_4=1,
 \quad 0<f\eta^2<\pi/2.
 \tag{TB4}
\]

Every 12-plaquette is \(e^{if\eta^2T}\).
The full-stencil first variation vanishes: the two parallel plaquette terms cancel.
The patch can sit inside a larger box with those exterior fine bonds fixed.
Thus the ambient criticality used in this calculation does not require a boundary equation on the smaller box.
At a flat left face of the restricted box, a tangential 2-bond has only one such term.
In the physical normalization of Y 62933–62947 its restricted current has magnitude

\[
 |J_X(b)|=\eta^{-3}\sin(f\eta^2)
 \ge {2f\over\pi\eta},
 \tag{TB5}
\]

up to the fixed trace normalization. The inequality uses \(\sin s\ge2s/\pi\).
It is a hand calculation, not a numerical limit.
Fine curvature remains at most \(f\eta^2\).
Thus even smooth curvature does not make this cut current \(O(f)\).
At a bare boundary the source weights it by \(\eta^3\); at a top boundary that cancellation is absent.

The omitted terms can also change under a variation with zero retained top average.
Work in the commuting subgroup and in one boundary top block.
Change the physical 2-potential by \(t h(x_1)T\), independently of the tangent coordinates.
Give \(h\) value \(1\) on the first fine site layer, \(-1\) on the next, and zero elsewhere.
Then \(\sum h=0\) in that top block.
The plain level-\(m\) 2-average has increment proportional to this sum, hence zero.
The other row increments vanish: their contour contributions average the centered tangent displacement to zero.
For commuting fields in the small logarithm chart this calculation is exact for the nonlinear average.
It is the actual centered-average linear formula of SA 7773–7781, with no noncommutative remainder.
All retained top rows are therefore fixed.

The 12-action derivative sums \(\eta\sin(f\eta^2)[h(x_1+\eta)-h(x_1)]\).
It telescopes to \(-\eta\sin(f\eta^2)\) for each tangent plaquette column.
It is nonzero. This exhibits the missing boundary term in the restriction argument.
The example diagnoses that argument; it is not a counterexample to a new free minimizer.

**Route A fails at the criticality premise of the old datum-response identity.**
A fixed-gauge free-boundary comparison must retain the surface force in (TB5).

### Route B: reflect the box and use the periodic theorem

Reflection is a serious alternative for the real problem.
Reflect the box and its old interior layers across each outer face.
Copy tangential top rows and put identity on rows normal to a reflection face.
Those rows have identity coarse plaquette holonomy across the face.
The homogeneous outer collar separates the reflected old cores.
All copied data still read only the original box.

If a regular periodic solution can be chosen in the reflection slice,
its restriction has the desired real rim scale.
For a reflection-symmetric field with identity crossing links, crossing fine plaquettes are identity.
The periodic action is \(2^4\) times the box action.
Reflecting a constraint-preserving box variation would then prove free-boundary criticality.
This is a possible reduction of real existence, not an application of the old restriction identity.
The averaging covariance used here is Sussman–Alpoge's SA 7049–7064, 7773;
Bałaban CMP 109, (0.5)–(0.9), supplies the symmetric-mean method.

The full consumer needs more than this real symmetric slice.
Its analytic domains have independent complex potentials and currents on the original box.
Their naive reflected extension need not obey the physical gradient bound.
Already at \(U=1\), take a constant normal potential
\(A'_1=aT\), with \(0<|a|<a_1/4\), and other components zero.
Its intrinsic gradient inside the box is zero.
Odd reflection sets its value on a crossing normal bond to zero and changes its sign beyond the face.
One adjacent physical difference is therefore

\[
 \eta^{-1}|aT-0|=|a|/\eta.
 \tag{TB6}
\]

This leaves the original \(a_1\)-ball for arbitrarily fine mesh.
The failure concerns the specified splitting and frame, not gauge-invariant curvature.
A gauge correction could fix this pure-gradient example.
It would still have to preserve the actual coarse rows, the common frame,
the independent current, and every required continued tower throughout the original domains.
For a top collar, a natural correction integrates the normal connection inward from the top-node plane.
It can fix the top nodes and hence preserve their averaged rows.
Products of at most \(C/\eta\) factors of size \(1+O(\eta a_1)\) cost at most \(e^{Ca_1}\).
Thus the product length alone does not cause a mesh loss.
But this construction supplies no hereditary test on a reflected subdomain crossing the mirror.
Such a domain folds onto overlapping pieces; it is not one original subdomain with its original tower.
Reapplying the generic minimizer estimate costs its constant \(B_3\).
An original strict bound by \(a_0\) has no guaranteed margin for \(B_3a_0\).
The same issue applies to the fixed independent-current and continuation radii.
No quantified inclusion for these original domains has been proved by this correction.
Projecting to symmetric data alone proves no such inclusion either.

**Route B fails at transport of the actual analytic domains through the reflection construction.**
It does not refute reflection as a method, or the real top-rim estimate.

### Route C: keep the boundary force and apply the bulk inverse

Use the correct equation, following SA BGR28:

\[
 \mathcal S_X\,\Delta\Psi=f_{\rm rows}+f_{\partial X}.
 \tag{TB7}
\]

Here \(\mathcal S_X\) is the actual free-boundary constrained saddle operator.
The force includes the removed plaquettes, constraint-row differences and gauge restoration.
In top units, (TB5) gives \(\|f_{\partial X}\|_\infty\asymp f/\eta\).
Even granting a uniform inverse in the old volume-force norm, BGR29 gives only

\[
 C f\eta^{-1}e^{-c d(x,\partial X)}.
 \tag{TB8}
\]

At a rim read the distance is bounded. The mesh loss remains.
It also remains at a fixed physical inset as \(m\) increases.
A larger coupling floor cannot depend on that absolute depth.

The force must instead be treated as a surface force, with its actual cancellations.
For example, if \(K_X(x,z)\) is the potential-from-current kernel with physical volume pairing,
a layer force \(\tau(z)/\eta\) contributes
\(\eta^3\sum_{z\in\partial_\eta X}K_X(x,z)\tau(z)\).
The missing linear conclusion, in a top-scale patch, has the form

\[
 \|\mathcal S_X^{-1}(f_{\rm rows}+f_{\partial X})\|_{\rm reads}
       \le C\varepsilon
 \tag{TB9}
\]

for forces produced by the original admitted inputs of size \(\varepsilon\).
The read norm includes the needed first derivatives and the original interior higher readouts.
It must have the corresponding decay away from the changed boundary.
This is not an estimate for arbitrary unrelated surface forces.
One possible argument subtracts a local constant from \(\tau\) and uses a Hölder bound on the remainder.
That would require a uniform trace Hölder estimate on the actual common complex domains.
The simple-domain hypothesis bounds a first difference of the potential, not a Hölder seminorm of that difference.
Adding that hypothesis would shrink the consumers' domains. It is not done here.
The alternative is to retain the coupled row, gauge and volume terms and prove their cancellation in (TB9).
The volume-row bound in BGR29 supplies neither argument.
The free-boundary interior comparison near CMP 109 (4.35) does not state (TB9).
The source's all-bare models, SA 10505, instead avoid this nonbare boundary problem.
Their fine-Dirichlet counterexamples concern another boundary condition; they do not disprove (TB9).

For nonlinear comparison, the inverse must also control the averaged Jacobian along the actual common segment.
SA 12285–12292 explicitly retains that requirement.
An arbitrary average of invertible operators need not be invertible.
No admitted segment or conormal inverse on that segment has been constructed here.

**Route C fails at the uniform surface-force inverse and its nonlinear continuation.**
This route retains the correct force. It differs from Route A's attempted zero-force identification.

## 5. The old core and the two boxes

There are two distinct boxes in the source.
The eligible component is \(X=G_m\), Y 63684–63771.
It has between 21 and 100 level-\(m\) cells along a side.
Those cells have side \(M\check R_m\), not side one.
The prepared integration box \(\Lambda^{\rm pr}\) inside \(X\) has side at most \(88M\),
Y 63825–63836. The latter is the small final box mentioned at Y 63866.
The stage backgrounds in that same passage remain localized in \(X\).

Consequently the \(O(M)\) assertion does not identify the outer localization rim with \(\partial\Lambda^{\rm pr}\).
At the outer rim of the original \(X\), Y 72280–72306 supplies the old-carrier separation
used in its conditional estimate. The proposed top boundary changes the local output scale there.
It does not justify the estimate's free-boundary analytic input.

Even in the compressed \(O(M)\) box, a fixed Euclidean distance is not the required argument.
Here is the conditional shell calculation, retaining the source geometry.
Put

\[
 R=\check R_{k_0+1}=L^{m-k_0-1},\qquad N=m-k_0-2=\log_LR-1.
 \tag{TB10}
\]

These are the exact scale relation of Y 63774–63782 and the late shells of Y 63800–63828.
The boxes are nested and concentric in this compressed range.
Their successive widths are \(w_i-w_{i+1}=ML^{i+1}\).
A path from the older inner carriers to the outer side crosses each intervening shell.
In the original weighted metric each full crossing costs at least \(c_0M/M_1\).
The fixed \(c_0>0\) allows for adjacent-level ratios and the fixed carrier insets.
Dropping a fixed number of incomplete end shells changes only the constant below.
Thus the compressed-shell distance is at least
\((c_0M/M_1)(\log_LR-C_0)\).

Port the old-datum bound \(C\check R_m^2\varepsilon_m\) from Y 72284–72294.
The running-minimum scales are nonincreasing, so \(\check R_m\le R\).
**If TB-BC supplies the native weighted profile on these reads**, that contribution is at most

\[
 b_{m,X}\le C_M\varepsilon_m R^{,2-\alpha},
 \qquad \alpha={\delta c_0M\over M_1\log L}.
 \tag{TB11}
\]

Indeed, multiply \(CR^2\varepsilon_m\) by the exponential of the preceding distance.
The discarded end shells give a fixed factor in \(C_M\).
Choose the geometric width so \(\alpha>2\), after the fixed response rate.
Then choose the coupling ceiling so
\(C_M R^{2-\alpha}\le a_s/4\).
The depth relation makes \(R\) uniformly large at weak coupling; CA-I 42907–42947.
This order gives \(b_{m,X}\le a_s\varepsilon_m/4\).
It uses the number of crossed levels, not an erroneous claim that the small box has width \(M\check R_m\).
It proves the scalar absorption conditional on the native profile and the stated crossed-shell read geometry.
It does not establish that profile at the new free boundary, or a margin for every changed analytic read.

### Ownership

The check correctly records that \(C(u)^+\) adds only two level-\(m\) unit-cube layers.
Y 76813–76864 allocates those halos, conditionally on the retained action containing their shares.
However, the source defines a node by its component, \(u=(m,C(u))\), Y 74219–74233.
For the boxed stage above, \(C(u)=X\).
The small final integration box is not a different definition of \(C(u)\).
Thus the sizes alone do not show that this stage's rim lies outside the mark halo.
Complete top block carriers inside \(X\) already lie inside \(C(u)^+\).

This resolves the box-size inference, not every ownership premise.
Any replacement requiring carriers beyond \(C(u)^+\) needs a larger-carrier allocation.
That allocation is an input, with floor exclusion and bounded overlap, before it can pay.
No padding or exterior read has been silently added to HCM-TB here.
The retained coefficient and the source's action-share hypotheses also remain inputs.

## 6. Consumers of the lift

Only the preparatory stage's artificial outer boundary is changed.
The ordinary test-cube towers and the original fixed-step lifts keep their definitions.
“Unchanged” below describes that definition choice. It grants no analytic admission for a new caller.

| Consumer | Source | Result of this round |
|---|---|---|
| Initial exact lift, uniqueness, response, covariance and complex charts | Y 7223–7264, 7309–7332, 7507–7527, 7668–7742, 8013–8041, 8380–8401 | Unchanged fixed-step constructions. |
| Joined datum and mixed tests | Y 13058–13130 | Deleted artificial rows have no tests. Physical top constraints remain exact by (TB1). Free-boundary existence is open. |
| Real collar comparison | Y 13315–13414 | TB-BC is needed. Route A explains why identical top data alone do not suffice. |
| Datum descent | Y 14977–15012 | Original descent unchanged. It supplies no exact identification across the new free cut. |
| Regular trial correction and fixed-step lift | Y 34888–34900, 35166–35249 | Unchanged. Neither supplies a depth-uniform top-boundary chart. |
| Product descent in the common old frame | Y 37276–37307 | Algebra unchanged; the new comparison and its frame still require TB-BC. |
| Strip localization, shift and holomorphic collar target | Y 62432–62510, 62717–62805, 62926–62954 | Original localizations retained. Changed-stage evaluations need common-domain admission; the boundary-current issue cannot be discarded. |
| Strip/density and final inset comparison | Y 63182–63214, 64050–64087 | Identical physical top rows identify the ordinary test datum. Comparing its orbit with the new stage orbit still requires TB-BC. |
| **Prefinal exterior tests** | **Y 64088–64107** | **The old identity/lift alternatives become actual top-row tests at the changed boundary. Subsequent comparison is open.** |
| Positive inset and prospective global orbit | Y 64568–64617, 65536–65573 | Their original restrictions do not establish the full changed rim. |
| **Stage curvature at the artificial join** | **Y 71368–71382** | **The old transferred datum bound persists on retained top tests. Its free-boundary curvature consequence is (TB3), still open.** |
| Literal final guard | Y 72324–72338 | Its threshold is unchanged. The four-bare-bond counterexample no longer applies to the deleted rows. |
| Terminal product ball and action | Y 98111–98163 | Unchanged independent tower; its tested region already lies in the top member. |
| Linearized localized read | Y 102096–102126 | The original read remains. Differentiation at a changed caller needs the common complex comparison first. |
| Common exterior precision | Y 103250–103290 | Equality of declared inputs is retained by the definition. Its admitted analytic comparison is not yet proved. |
| Lower/upper localized readouts | Y 104134–104225 | Original towers retained; changed-stage use still needs the common frame, datum ball and collar estimate. |
| **Cutoff comparison** | **Y 134088–134131** | **Unchanged ordinary test-cube tower. Its test-radius admission is not a full-rim stage theorem.** |
| **Tower localization** | **CA-I 45115–45160** | **Outstanding source route, including crossing-constraint compatibility. It is not a supplied proof of TB-BC.** |
| Real gauges, stopped spaces and preparatory terms | CA-I 49495–49546, 54985–55024; SA 17433–17447 | Original creation domains and locality in the term's support remain mandatory. TB-BC has not been proved on them. |

Thus no assertion that all consumers remain valid is made.
The changed consumers are listed explicitly; curvature and exact averaging would not settle them alone.
Padding moves the same free-boundary issue outward or enlarges the input region.
It supplies no fourth route independent of TB-BC.

## 7. Payment and stopping point

If TB-BC supplies (TB3), the appropriate old-core bound, and the complete read set,
then it gives (3) of `hcm-repair.md` on every tested rim plaquette.
Its small-data existence clause covers undefinedness as a failed test.
Section 3 of that note then supplies an actual top plaquette witness and its exact-cone certificate.
With the retained action share and ownership, the gain is \(c_*P_t^2\).

The consumed price is

\[
 q_t=C_{\rm cnt}C_T R_t(4c_1M^4R_t^5+\kappa_1),
 \tag{TB12}
\]

from IN1 (31), with its reserve calculation at lines 500–529.
It is \(O((\log\theta_t)^{6r})\).
Since \(P_t=A_0(\log\theta_t)^{p_0}\) and \(p_0>6r\),
the final coupling ceiling makes \(c_*P_t^2\ge q_t\).
This is the already checked payment implication. No extra requirement of \(P_t/2\) is imposed.
It remains conditional on TB-BC and the existing carrying-action and ownership inputs.

**Result: stopping condition (c). TB-BC remains open after Routes A, B and C.**
Route A fails at restriction criticality. Route B fails to transport the original analytic domains.
Route C retains the boundary force but lacks its uniform constrained response on those domains.
These are three attempts at the changed boundary, not the old four-fixed-bonds obstruction.
The calculations refute the indicated shortcuts. They do not refute HCM-TB itself.
No proof of the H-C-MARK payment for the modified construction is claimed.

| Claim | Status | Scope |
|---|---|---|
| Repairs requested by the check | Done in `hcm-repair.md` | Route count, optional deletion, missing consumers, R4 and ownership question. |
| Top constraints and declared data footprint | Exact construction identities | Conditional on a selected solution; they do not assert existence. |
| Mesh factor at a top rim | Conditional port, CA-I 43142–43149 | Needs the free-boundary regular theorem on the changed set. |
| Old bare-collar arguments survive unchanged | False | Exterior gap and zero boundary-force premise fail. |
| Boundary current calculation (TB5) and zero-average variation | Proved here | Diagnose the failed restriction argument; no counterexample to HCM-TB. |
| Naive reflection preserves the given analytic splitting | False by (TB6) | A corrected domain transfer remains possible and unproved. |
| Compressed old-core absorption | Conditional implication (TB11) | Requires the native profile on the specified crossed-shell reads. |
| Mark halo versus final integration box | Source distinction resolved | \(X=C(u)\) differs from \(\Lambda^{\rm pr}\); any genuinely larger carrier still needs allocation. |
| Rim estimate implies \(q_t\) | Existing conditional proof preserved | Needs existence, full reads, old-core control and action ownership. |
| Every changed consumer is admitted | Open | Curvature alone does not supply the common analytic domains. |
| **First open input: TB-BC, §4** | **Open after three distinct routes** | **Free-boundary regular background and its comparison on the original stage domains.** |
