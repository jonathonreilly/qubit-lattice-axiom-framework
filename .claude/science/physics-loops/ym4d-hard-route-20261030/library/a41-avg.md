# A4.1: the actual changes of averaging

Codex, 2026-11-08. Repository pin `4ddbc7cecf481d1e77fe742303d7a7ade2fd4c22`.
FINISH row 510. Research text, not an audit. This note grants no status.
No computation supplies a proof. No independent check has occurred.

**Result: stopping alternative (c).** SC-HESS, stated in §4, remains open
after the three routes in §5. A4.1 is not proved here. No actual-history
counterexample is claimed. The existing uniform row and node estimates
are ported; they are not counted as new work.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors
of their text, for every source step below. Credit Tadeusz Balaban for
the averaging, gauge, constrained-inverse and multiscale methods.

## 1. Sources and work already done

The requested `prior/a41-avg.md` is absent at this pin.
The complete `prior/hstep.md` was read. Its A4.1 row leaves a general
comparison unowned. It does not leave the existing row estimates unproved.

Source abbreviations retain the pinned files and their line numbers:

* **Y:** `YM4_1400.tex`, commit `2bc0658f91d2d03ba44e20bf695067e0a56a2ed9`.
* **SA:** `YM4_sketch_500.tex`, commit `31a47c543775`.
* **I:** `theorem_0_complete_account_raw_I.tex`, commit `31a47c543775`.

The source copies are `/tmp/ym4_1400.tex`, `/tmp/sa_ym4.tex`, and
`/tmp/sa_ca_I.tex`. Only searches and bounded excerpts were used.
Navigation began with `sa-index/README.md`, neighbouring chunk rows,
and `obligations.md`. The 4.12–4.19 and complete-account indices supplied
the account references. The permitted Balaban paper directory is absent.
Balaban's formulas below are read through the account and existing ports.
No direct rereading of his papers is claimed.

The method uses Balaban's CMP 95 block and lift conventions, CMP 96
layer metric, CMP 99b constrained operators, and CMP 109 symmetric mean.
The precise ports are `out-pi.md` §§2.1, 2.4, 3.1 and I 831–848.
CMP 98 supplies their intervening relative-average identities.
These literature inputs are cited through those ports, with their
standing recorded below.

| Input | Source standing | What can be used |
|---|---|---|
| A4.1 | Y 2148–2156: required; 2169–2173: retained at general scope. SA 3898–3906 says the same. | No all-history averaging transfer follows from the catalogue. |
| Symmetric average and its contours | SA 7065–7073; I 831–855: definitions, with the CMP 109 construction cited. | The actual small-field map uses a mean of coordinate-order paths. |
| Plain and straightened averages | SA 7092–7116: definitions and comparison sketch. I 24239–24338: CMP 98 fundamental equality cited. | The coarse node factor must remain in the constraint identity. |
| Corner/mean comparison | SA 7406–7424 and 7798: sketched. | This compares linear rows after transporting their base sites. It is not a nonlinear fibre identification. |
| Finite recursion, node factor and row bounds | SA 11508–11610: written proof on its regular-pair class. | Depth-uniform bounds, conditional on complete local gauges. |
| Second constraint derivative | SA 11612–11639: written proof on the same class. | The two-leg moment and its current contraction are available. |
| Literal comb rows | `out-pi.md` §§2–4, especially Lemma 4.4: existing restricted proof. | Keep the corner grids, outward rows, physical measures and full reads. |
| Both contour prescriptions on supplied frames | `b98p5.md` §§2.1–2.5: existing proof, with its recorded Claude check. | Analytic bounds, node-factor bounds and fine densities for each map separately. Section 2.5 expressly denies equality of the curved maps. |
| PI/GW/GW1 inverses and words | `out-pi.md` §3.4; `walks-gw.md` theorem; `gw1.md` §§1–2, 7–9: existing restricted proofs. | Same literal rows and admitted fields. No new inverse proof is needed. |
| Determining-set averages | I 43013–43052, 43066–43084: cited inputs; mixed-level extension is a hypothesis. | A new target tower must meet those inputs. |
| Nonlinear mean/comb comparison | Y 16661–16865: written local reduction, with supplied comb inverse and admitted real reference. | It retains the linear error at a curved reference. It does not identify the completed physical form. |
| Node extension | Y 34390–34462: written proof in the proper reference class. | Bounded local extensions exist there. Rebuilding the bump argument would duplicate it. |
| Moving-slice saddle | Y 29049–29212: written conditional proof for the specified inner-action Lagrangian Hessian. | It is not a comparison of two averaging prescriptions or two boundary actions. |
| Physical continuation | Y 35771–35822: proved on the proper-background class. | The native critical branch has a uniform complex ball. |
| Physical Hessian and coarse readout | SA 11143–11254: written finite-dimensional identities on an admitted chart. | The current, constraint second derivative, outward datum and actual gauge function must match. |

These are source classifications, not new proof certificates.
The row and node-factor estimates will be ported, not rederived.

## 2. Consumer census

There are three different operations. They must not be called one change.

| Consumer | Actual operation | Boundary retained here |
|---|---|---|
| PI → GW → GW1 | The same CMP 98/99b comb rows, with physical transposes and current corrections. | No averaging-scheme substitution occurs. GW1's switched families do not preserve arbitrary inverse identities. |
| DR-LIFT | Transport of a full response system with matching complete reads, coefficients, rows and branches; `dr.md` 93, 142–166, 594. | LIFT is supplied. Its owner is DR. |
| LAYER-RC | Apply the target determining-set average to the returned field; `layered-a3.md` 149–198, 1324–1341. | This changes the tower. It does not assert equality of two backgrounds. RC's owner is PR1/PR-lay. |
| M3 | Carry already supplied gauge or labelled-word intertwiners; `m3.md` §4.4 and §8. | It constructs no new scheme comparison or global covering identity. |
| Plain → straightened | Insert the node gauge for one fixed contour prescription. | An exact identity exists. Deleting its node factor changes the constraint. |
| Symmetric → comb | Use the early Balaban operator package for the symmetric hard constraint. | This is the remaining comparison. SA 7108 and 7424 identify its intended use. |

The registry and FINISH searches found no other owner of the last comparison.
This lane does not reopen DR-LIFT, LAYER-RC, PI-ADMIT, or B98-P5.
In particular, a proof about admitted comb rows is not an application theorem
for every symmetric hard-constraint history.

## 3. What the existing comparison actually transfers

This section ports Sussman and Alpoge's Y 16661–16865, with Balaban's
raw-row normalization. It is not a new proof of their comparison.
Raw rows have counting pairing. Fine fields have pairing weight
`eta^4`. Per-length rows instead have weight `xi_c^4`.
Changing pairing requires the corresponding diagonal length factors.

At a supplied real reference, let `Q_c` denote the comb derivative.
Let `q_m(A)` be the actual straightened mean logarithm.
Let `T` transport the coarse base sites. Their formulas are

\[
 T^{-1}q_m(A)=Q_cA+C(A),\qquad C(0)=0,\qquad C'(0)=E.
 \tag{1}
\]

The term `E` is generally nonzero. Their `H_c` satisfies `Q_c H_c=I`.
On the supplied ball, `C'(A)H_c` has norm at most `1/2`.
Thus their right inverse is

\[
 H_A=H_c(1+C'(A)H_c)^{-1}T^{-1},\qquad q_m'(A)H_A=I.
 \tag{2}
\]

Y 16764–16819 also bounds the physical transpose and multiplier.
It uses both kernel sums and the bounded overlap of adjacent-height rows.
These estimates have no depth factor.

The underlying summation is already proved in `b98p5.md` §§2.3–2.5
and SA 11550–11610. For a row of length `xi=L^j eta`, put
`t_s=L^(s-j)`. The repeated raw errors have size `C epsilon t_s`, and

\[
 \sum_{s<j}t_s<\frac1{L-1},\qquad
 \prod_{s<j}(1+C\epsilon t_s)
       \le \exp\!\left(\frac{C\epsilon}{L-1}\right).
 \tag{3}
\]

The same summation bounds the node product and its condition number.
Multiplying a fixed estimate greater than one at every level would lose
this fact. Such a loss would be a defective estimate, not a counterexample.

The exact node identity is

\[
 M^j(e^{i\eta A}U)
      =(e^{ia_j}M^j(U))^{v_j[A]},\qquad
 v_{s+1}=v_s|_{s+1}\,u_s.
 \tag{4}
\]

It is SA 11540–11548, also I 24314–24338's cited fundamental equality.
The contour prescription must agree in all four places: the mean,
straightening, gauge average, and axial condition. Y 3712 states this.
Equation (4) is not an identity between the mean and comb prescriptions.

Y 34390–34462 supplies the regular node extension in its own reference
class. The rough tower-axial gauge of Y 3991–4005 is a different map.
It can jump across blocks. Its supremum bound does not imply a first
difference bound. No new node-extension lemma is needed on the supplied
proper class.

The physical second jet is also already known. Write `b(B)` for the
actual reduced datum, `omega` for its multiplier, and `W_1` for the
matched row covariance. Sussman and Alpoge prove

\[
 K_L=\Delta_U^W-\langle\omega,D^2q(0)\rangle,
 \qquad
 D^2\mathcal A_{\rm eff}
 =Db^T(W_1^{-1}-a)Db+\langle\omega,D^2b\rangle.
 \tag{5}
\]

These are SA 11143–11179. On outward rows, `b` includes the lower
endpoint factor, SA 11189–11202. The next curved fibre adds its own
multiplier and the derivatives of the actual gauge function,
SA 11204–11254. None may be removed by renaming `Q`.

## 4. The remaining supplier: SC-HESS

The first unresolved comparison concerns the **completed physical form**.
It is not a new inverse estimate for the comb family.
Y 23838–23847 makes this distinction explicit. Its physical constrained
Hessian does not identify a separately defined independent-current extension.

Here is a precise sufficient supplier for the perturbative transfer route.
Call it **SC-HESS**. Its domain is an actual mean-to-comb use whose common
reference, complete reads, action, independent rows and complex ball have
already been admitted. Admission is not part of this lemma.

Keep the actual masks, pivots, seam factors and gauge function of that use.
Use physical pairings. Let `chi_m` be its prescribed mean-scheme fibre
chart in fine per-length coordinates, with `chi_m(0)=0`, after removing
residual gauge directions. Define

\[
 \mathcal E_m
   =D^2\{S(e^{i\eta\chi_m(z)}U)+\mathrm{GF}_m(z)\}_{z=0}.
 \tag{6}
\]

Here `S` is the action actually consumed, including its boundary convention.
Let `E_c^J` be the corresponding specified comb current precision on its
gauge-fixed fibre, and let `G_c^J=(E_c^J)^{-1}` be the supplied inverse.
This notation does not assert that the comb precision is already (6).
For GW1 its unreduced inverse is the one in `gw1.md` (2), (27).
Its restriction and its current completion must be the required ones.

Use the actual node and slice coordinate changes to identify the two
tangent fibres. Denote their map from comb to mean coordinates by `T_f`.
The field-row part is fixed by (1); the gauge-row part must use the
prescribed node extension. No new physical gauge function may be chosen.
Match the flat reference forms first, with fixed allowed constants.
If that match is absent, this supplier cannot be invoked.
Verifying this identification for the actual chart is part of the missing
comparison. The field-row map (12) alone is not a claimed `T_f`.

**SC-HESS.** Verify that this `T_f` and its inverse have uniform energy
and weighted readout bounds, with complete carriers. Form the actual defect

\[
 \mathcal R=T_f^T\mathcal E_m T_f-E_c^J.
 \tag{7}
\]

Prove that it has a complete-carrier analytic expansion satisfying

\[
 \begin{split}
 |\langle u,\mathcal Ru\rangle|
     &\le\tfrac12 c_c\|u\|_{X_c}^2
                       &&\text{at real physical pairs},\\
 \|G_c^J\mathcal R\|_{\mathscr A}
     &\le\tfrac12
                       &&\text{on the prescribed complex ball}.
 \end{split}                                                    \tag{8}
\]

Here `c_c` is the supplied comb fibre gap. The norm `X_c` is its energy
norm. The algebra `mathscr A` is GW1 §3.1's normalized cell majorant
algebra, including reversed physical contractions, the allowed first
derivative/Hölder readouts, and a positive spare tree exponential.
The identity is adjoined when summing the inverse series.
All constants and the needed fixed shrink precede depth, volume and history.
The rows, node derivatives and current in (7) must belong to the same
physical chart. A bound for a separately chosen quadratic completion
does not prove (8).

Equations (6), (7) and (9) are unswitched identities. For independent-current
pairs, the target extension must first be specified and matched.
Switches are assigned to the completed words. No inverse identity at
nontrivial switches is asserted.

This is a sufficient perturbative lemma, not a claim that every valid
intertwiner must be a small perturbation. It addresses a second jet on
already admitted fibres. It asserts neither A1's orbit theorem nor
admission of a later history. Those existing tasks keep their owners.

The consequence for the inverse is elementary. If (7)–(8) hold, then

\[
 \mathcal E_m^{-1}
   =T_f\sum_{n\ge0}(-G_c^J\mathcal R)^nG_c^J T_f^T.
 \tag{9}
\]

Indeed `(E_c^J+R)=E_c^J(I+G_c^J R)`. The geometric series inverts
the last factor. Congruence by `T_f` gives (9).
The real part of (8) preserves half the comb gap before the fixed
coordinate loss. The algebra part gives the existing physical column
powers and decay after fixed junction costs. It costs no factor per level.
This explains why the unresolved task is (7)–(8), not another inverse sum.

The complete saddle still matters for A3's multiplier response.
Y 23849–23915 already proves that block-inverse formula.
It explicitly retains the bounds on the lift and the products involving
the Hessian. A field inverse alone is not the whole response theorem.

## 5. Three routes to SC-HESS

### Route 1: telescope the actual contours and node factors

Use Balaban's contour comparison before taking inverses. Equations
(1)–(4) already control its accumulation. At a real reference the frozen
base transport is orthogonal. At complex references its physical bilinear
transpose is its inverse, since the trace pairing is conjugation invariant.
Its operator norm still needs the supplied condition-number bound.
Thus frozen conjugation can be removed from a row penalty.

The attempted next step was to use that conjugation for the full Hessian.
It fails because the coarse node factor depends on the field.
For a nonlinear coordinate change `Psi`, the exact chain rule is

\[
 D^2(S\circ\Psi)[u,v]
  =\langle D\Psi u,S''D\Psi v\rangle
                         +\langle S',D^2\Psi[u,v]\rangle.
 \tag{10}
\]

Constrained criticality does not give `S'=0` in the ambient field space.
It gives the multiplier equation in (5). Hence the last term survives.
At an outward row it also produces the datum term in (5).

This is not only a possible bookkeeping term. Y 4034 supplies a seam
example with one bare bond `eta A=t H` and node factor

\[
 u(z)=\exp\!\left(it\frac{L^4-1}{8L^4}H\right)\ne1.
 \tag{11}
\]

We port that example; it is not a new counterexample.
Replacing the reduced datum by the plain datum discards a real factor.
The later bounded node extension repairs regularity of a gauge lift.
It does not identify the two full quadratic completions in (7).
This route proves the existing row bounds and stops at the last term
of (10) with the actual current and gauge function.

### Route 2: repair the constraints with the comb right inverse

This route works at the tangent level. Freeze the reference and use
one consistent row normalization. Then `T^{-1}Q_m=Q_c+E`.
Suppose the supplied row and lift bounds give
`||H_c E||_{X -> X}<=kappa<1`. Define

\[
 T_0=(I+H_cE)^{-1}.
 \tag{12}
\]

Since `Q_c H_c=I`, multiplication gives

\[
 (Q_c+E)T_0=Q_c,\qquad Q_mT_0=TQ_c.
 \tag{13}
\]

Thus `T_0` maps the two field-constraint kernels bijectively.
Its norm is at most `(1-kappa)^{-1}`; its inverse norm is at most
`1+kappa`. Weighted versions use the same complete-carrier products.
No depth enters. Gauge constraints still have to be included.
Y 29049–29103 gives the combined-constraint method for its own family;
it does not identify different nonlinear physical completions.

The attempted next step was to transfer criticality and the Hessian
from (13). That inference fails. At a mean-scheme critical field,
write the physical stationarity equation in the same row pairing:

\[
 J=Q_m^T\omega
    =Q_c^T T^T\omega+E^T T^T\omega.
 \tag{14}
\]

There is no premise making the last term vanish.
For `a in ker Q_c`, the uncorrected comb-fibre derivative is
`<T^T omega,Ea>`. Thus the same fine field need not be critical for
the comb constraint. Calling `J` an independent current permits an
auxiliary operator; it does not prove that operator is (6).

The second-derivative row bound, SA 11612–11639, does bound an individual
contraction with a supplied small multiplier. That part is already done.
It does not select the physical multiplier, datum second jet or gauge
completion after the switch. Y 23838–23847 expressly retains that match.
Using (9) before proving it would assume SC-HESS.
This route therefore supplies (13), but not (7)–(8).

### Route 3: use the native mean-scheme variational theorem

This avoids a scheme comparison inside the native problem.
Port Y 29144–29212 and 35771–35822: the specified proper inner-action
problem has its physical saddle and uniform continuation.
Its node extension is already supplied by Y 34390–34462.
These results are useful. They are not missing lemmas to rebuild.

The attempted substitution into the stated PI/GW/GW1 consumers changes
the boundary problem. PI uses touching field bonds and the compressed
whole-action Hessian. The native theorem uses its inner action.
`pi-admit.md` §7 already proves their difference at a flat slab boundary:

\[
 \langle A,(\Delta_W-\Delta_{\rm in})A\rangle
                       =\eta^{-2}\|A\|_2^2>0
 \tag{15}
\]

for its specified single tangent bond. The missing incident plaquette
produces (15). It persists when curvature and twist are zero.
It cannot be charged to a curvature-small change of averaging.

This is an existing operator-identification obstruction, not an actual
history with a depth-growing averaging loss. The boundary-entry problem
belongs to PI-ADMIT. Actual chart/step branch matching belongs to
HMA-BRANCH. We stop this route at those owners, as instructed.
Replacing the action, trimming its boundary, or choosing an exterior
extension would change the consumer and would need a separate proof.

The three routes are different: contour algebra, tangent constraint repair,
and a native variational replacement. None proves SC-HESS on the requested
actual uses. They do not show that SC-HESS, or A4.1, is false.

## 6. Closure record

The retained general hypothesis in Y is not evidence of a missing proof
for every local ingredient. Its newer local comparison, node extension,
physical Hessian identities and native inverse must be reused.
Conversely, those separate results do not identify the actual two
completed forms at a consumer. That is where this lane stops.

SC-HESS is a supplier within this A4.1 attempt, not a new registry row.
It does not take ownership of PI-ADMIT, DR-LIFT, LAYER-RC, B99-W,
HMA-BRANCH, or stored-factor formation. Route 3 stopped when it reached
their boundary. The only repository output is this file.
The checkout advanced during this session. The cited repository inputs
were compared with `4ddbc7cec` and remain unchanged at their cited paths.

| Item | Result | Scope or remaining input |
|---|---|---|
| Uniform nonlinear row comparison | Ported, already written | Y 16661–16865; admitted common chart. |
| Node product and bounded regular extension | Ported, already written | SA 11540–11610; Y 34390–34462; supplied reference class. |
| Field-constraint intertwiner (12)–(13) | Elementary conditional consequence | Supplied row error and bounded right inverse; gauge rows and physical second jet still required. |
| Inverse transfer (9) | Conditional algebraic consequence | Requires the actual SC-HESS defect and its two bounds. |
| Contour/gauge route | Does not close SC-HESS | The variable node factor contributes the current and datum second jets. |
| Tangent repair route | Does not close SC-HESS | The residual in (14) prevents an automatic physical-current identification. |
| Native variational route | Stops at an owned comparison | PI-ADMIT's boundary operator mismatch; HMA-BRANCH's actual branch match. |
| A4.1 on every actual history | **Open** | No full transfer and no actual-history counterexample obtained. |

**First open input:** SC-HESS, equations (6)–(8), for the prescribed
mean/comb comparison on already admitted, matched physical reads.
It must include both coarse node factors and the actual current and gauge
second derivatives. The separate all-history admission obligations remain
with their existing owners.
