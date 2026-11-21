# GEOH-O2: the actual charge ledger

Codex, 2026-11-08. Checkout `a3a238cc83b203e8eab77ce1f4a496e95462aca2`.
FINISH row 492. Research text, not an audit. No status is granted.

**Result:** stopping condition (c). The single supplier UO2 remains open after the three routes in §§5–7.
This file gives conditional ports and reserve comparisons, not a complete proof of GEOH-O2.

## 1. Target and prior work

This lane concerns GEOH-O2 only. The registry assigns it to GEOH.
`prior/geoh-o2.md` was absent. The whole of `prior/geoh.md` was read first.
Its O2 row and verdict item 2 identify the actual charge bound as the first hard step.
The rooted address count is already proved. It is not a new target.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Their large-field method follows Tadeusz Bałaban. The source keys are:

- **N:** [YM4_1400.tex, commit 2bc0658f91d2d03ba44e20bf695067e0a56a2ed9](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/2bc0658f91d2d03ba44e20bf695067e0a56a2ed9/YM4_1400.tex).
- **SA:** [YM4_sketch_500.tex, commit 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex).
- **I:** [complete account I, commit 31a47c543775](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex).

All arguments below are written arguments. Retrieval and text searches discharge nothing.
Only bounded source ranges are used. No numerical or enumeration result is used.

Write \(\lambda_j=\log\theta_j\) for N's weight and \(\ell_j=1+\log x_j\) for IN1's weight.
Write \(a=(j,Q)\) for a level-cell address. Its IN1 price is
\[
 w(a)=\ell_j(MR_j)^4.
\]
An occurrence means an address in one outer tree of the expanded island recursion.
It does not mean a later evaluation of that address.
IN1 (6) sums these occurrence prices to obtain \(v^\natural\).

Three different counts must remain separate:

1. Occurrences of a genealogy node in the island recursion.
2. Distinct stored coordinates and geometric read sites.
3. Charge incidences in the actual product and its estimates.

A bound on the first count does not bound the third.
A union of read sets forgets repeated incidences.

## 2. What is ported

The source steps below are due to Sussman and Alpoge, under their stated premises.
The final row records prior work in this repository.
“Proved there” describes the source argument. It grants no repository status.

| Step | Source and source standing | Premises retained here |
|---|---|---|
| Rooted address count \(D^{2(N-1)}\) | N 74615–74647; also SA 18673–18690. Proved there. | Actual connected address set; fixed root; degree \(D\le L^4+3^4+2\). |
| Finite-record entropy \(e^{bV^\circ}\) | N 74649–74669. Proved there conditionally. SA 18692–18701 sketches it. | Fixed local alphabets; bounded tests per site; polynomial stage choices; locally addressed seams and stored types. Every additional choice must be encoded. |
| Recursive node multiplicity | N 74250–74271. Proved there. | Cut at clearing nodes; retain each boundary as one outer leaf and one inner root. Keeping a drop-out does not copy its past. |
| Owned collar volume | N 74274–74300. Proved there conditionally. | Fixed-width collars of owned cells; count each paid incidence with its actual multiplicity. |
| Retained and restored load comparison | N 74302–74320. Conditional argument there. | Quiet/prepared boxes, the waiting window, comparable weights, and the stated retained-box lower count. Retained and action regions remain different. |
| Actual read-to-cell bound | N 78902–78937. Sketched supplier, not discharged there. | Simultaneous ownership for actual determining entries, action entries, retained nests, and bounded covering multiplicity. |
| Primitive history closure | N 4153–4181. Conditional. | Finite read ownership remains an explicit primitive premise at 4163–4171. |
| Live-region geometry and reader sums | I 85575–85700. Hypotheses, headed “Proof outstanding”. | In particular, strip ownership and probe incidence are not proved by that heading. I 166652–166659 still lists volume counts and live geometry as outstanding. |
| Outcome replay and current visible-label load | `sa-2.13.md:104–118,220–268`; checked as conditional in `pre-213.md:14–28`. | Fixed selectors, schedules and read-address ownership for the code; the stated set replacements for the visible load. The full analytic read family remains outside that load theorem. |

The first four rows do not supply the sixth row.
This is also the limit stated in `geoh.md:142–169` and `gates/geoh-gate.md`.
The separate live-strip obligation is `O-live-geometry`; this lane does not take it over.

## 3. Fix the source volume before assigning owners

The source definition is SA 17274, also N 61926 and 96520:
\[
 v(\omega)=\sum_j(\log x_j)s_j(\omega).                 \tag{1}
\]
Here \(s_j\) is the actual count of stored sites of level \(j\).
The operation fixes that count. It is not a freely chosen majorant.
SA 18087–18091 also records assigned collars and fixed coordinate multiplicities in its stored-site count.
These conventions must be retained when relating its different counts.
Reading a coordinate again does not create another integration variable; see `c1-repr.md:24–38`.
It can, however, create another charge in an estimate.

The tube in GEOH gives
\[
 \tfrac34\theta_j\le x_j\le\tfrac54\theta_j,\qquad \theta_j\ge X_0>e.
\]
Consequently
\[
 \lambda_j\le\ell_j\le3\lambda_j,\qquad
 0<\log x_j\le\ell_j.                                  \tag{2}
\]
Indeed, \(\log(4/3)<1\) proves the first lower bound.
The upper bound follows from \(\log(5/4)<1\) and \(\lambda_j>1\).
Thus N's and IN1's volumes differ by at most three, **on the same occurrences and scale sequence**.
This does not identify regions, stored slots, or two different choices of \(R_j\).

There is also an endpoint issue. N 73088–73099 has no independently generated level-zero region.
The first ordinary operation can still store bare, level-zero variables.
They must keep their actual level when assigned to the level-one node.
More generally, N 78905–78912 permits a one-step conversion costing \(L^4\).
It does not permit charging an old datum at an arbitrary later level.

For that one-step conversion, increase only the final floor so that \(X_0\ge\overline B\).
The frame increment bound gives
\[
 \theta_{j-1}\le\theta_j+\overline B\le2\theta_j,
 \quad
 \log x_{j-1}\le\log(\tfrac52\theta_j)<\lambda_j+1\le2\ell_j. \tag{3}
\]
Here \(e>5/2\), as follows from its first four series terms.
No early constant depends on this later floor.

Here is the exact reserve implication needed below.
Suppose an actual ownership map has the following properties.
It assigns each stored site of (1) to an occurrence \(a=(n,Q)\), with \(j=n\) or \(j=n-1\).
The map retains \(j\), the coordinate type, and every genuine coordinate multiplicity.
Project a level-\((n-1)\) site to its level-\(n\) block, recording the fine offset.
Assume that at each level-\(n\) site, the total assigned multiplicity is at most \(\mu L^4\).
The same bound includes native-level slots.
All assigned sites lie in the owner's collar of \(c_0\) layers of \(M\)-cubes.
The constants \(c_0,\mu\) must be uniform and chosen early.

For \(R_n\ge2c_0/(2^{1/4}-1)\), that collar has at most
\[
 (MR_n+2c_0M)^4\le2(MR_n)^4
\]
level-\(n\) sites. This is the ported collar estimate, N 74274–74300.
Equations (1)–(3) then give
\[
 v(\omega)\le4\mu L^4
       \sum_{a\text{ occurrence}}\ell_{n(a)}(MR_{n(a)})^4
     =4\mu L^4v^\natural(\omega).                       \tag{4}
\]
The sum already includes cut-boundary multiplicity. No extra factor of two is needed for cuts.
This proves the comparison **conditional on the actual assignment**.
It uses the specified \(v\), not \(\max(V_{\rm in},n^\sharp)\).
Neither (2) nor (4) supplies that assignment.

## 4. The single supplier to test

Call the missing supplier **UO2: uniform ownership of actual charge incidences**.
It makes the geometric supplier retained at N 78917–78923 precise for this lane's charge and code conventions.

Fix any finite admissible revised history, including every stopped-stage branch.
Use its actual kernel, test lists, retained coordinates, and determining and action entries.
Fix its selectors and schedules as in GEOH; do not replace them by more convenient ones.
Keep all five read lists of N 73147–73158 separate.

First split regions and masks into their elementary site, bond, and finite-stencil reads.
A carrier meeting several cells has several such incidences; it is not assigned whole to one cell.
An incidence records the operation, stage, object, actual level, coordinate type, and charge use.
Its uses include determining rows, action supports, prepared nests, seam factors, and source-reserve sites.
Local selector-output bits and test outcomes use the same ownership table for coding.
A repeated occurrence remains an incidence until an exact identity or an already supplied summation estimate removes its extra charge.
Recording one coordinate identifier is not such an identity.

**UO2.** There are early integers \(c_0,\mu,J\), independent of depth, torus, cutoff and coupling floor, with these properties:

They may depend on the fixed early geometry and operation templates, but not on later choices of \(M\) or \(\kappa\).

1. Every actual incidence has an owning occurrence \((n,Q)\). Its complete finite geometric stencil lies in that owner's fixed collar.
2. Native-level reads keep level \(n\). The ordinary one-step inputs may have level \(n-1\), with their offset retained. Prepared data are never replaced by integrated-out fields.
3. After only justified grouping of repeated reads, each site of the owner collar receives at most \(\mu L^4\) charged slots and at most \(J\mu L^4\) discrete local slots.
4. The grouping preserves the actual kernel and the upper-integral majorant being used. It does not delete factors, replace action regions by retained regions, or add a new reserve definition.

Analytic sizes of the already formed local families are inputs to this geometric supplier.
UO2 must identify their actual owners. It cannot assume that those owners already have bounded multiplicity.
For absolutely summable carrier families, use their supplied rooted sum before assigning its per-site price.
This does not license replacing an unbounded number of unsummed charges by their set-theoretic union.

UO2 isolates the ownership part of GEOH-O2.
The entropy multiplication and the original-reserve comparison are its consumers.
Together with the fixed operation grammar, it supplies the missing hypotheses of the ported count and (4).

## 5. First route: follow the latest owner through each move

**Attempt.** Give each stored coordinate its creator, level, position, and role.
At a remade row, use the latest operation that owns that row.
At an inner island, descend into its retained record once.
Prove that each move preserves a fixed bound on incidences at that identifier.

Several parts of this induction are already supplied.
GEOH's mark rule makes the windows of nested standing marks disjoint.
Hence one position and one level have at most one active drop-out window.
This selects a remaking operation. It does not bound how often its output is used.

N 75934–75965 supplies a more precise stage statement.
The remaining inner graph uses rows wholly inside the prepared core.
The next face reads either retained level-\(j\) coordinates or the preceding chart's outgoing coordinates.
Reading through that inverse chart inserts no additional constraint.
A stop after the sharp test retains the nonpivots and translated density, including eliminated-pivot factors.
There is then no integrated collar normalizer.
These are conditional row assignments, using the full row-block separation and admitted real chart.
They are ported, not reproved here.

The candidate ledger is therefore:

| Actual object | Owner rule | What this establishes |
|---|---|---|
| Ordinary stored field or fluctuation coordinate | Its original ordinary-step slot; retain the actual level and any one-step offset. | A later read does not create another coordinate. |
| Removed, crossing, or inner stage row | The three-way row assignment of the actual collar chart. | The same constraint is not both solved and retained. |
| Remade determining entry | The unique active window at that position and level; read its retained or outgoing datum. | A unique candidate owner, not a bound on uses. |
| Visible action support | The original as-made node of that level. | Its visible subset is paid by the existing action-volume argument. |
| Prepared nest | Keep the selected \(Z''_j\) and its containing old hole separately. | Its membership does not replace the old action support. |
| Retained gauge seam | Keep the relative/ordinary prescription and actual background tag, N 73181–73194. | The tag specifies a function; it is not permission to erase it. |
| Carried form, elimination factor, and newly localized difference | Keep the birth identifier and the actual later read. | The bound on the number of paid incidences is still unproved. |

The last row prevents completion of the induction.
SA 17558–17564 states that changing the background produces differences of kept forms.
For one such form, write
\[
 F_s(A)=-\tfrac12\langle A,\Delta_s A\rangle,
 \qquad d_s(A)=F_s(A)-F_{s+1}(A).                       \tag{5}
\]
The next representation contains the new reading and the localized difference.
Both can read the same retained \(A\).
Uniqueness of \(A\)'s owner says nothing about the incidence contributed by \(d_s\).
An attempted incidence induction has the form
\[
 m_{s+1}(a)=m_s(a)+e_s(a)-r_s(a),                       \tag{6}
\]
where \(e_s\) counts new charged uses and \(r_s\) counts uses actually removed by an identity.
The row assignment bounds constraints. It supplies neither \(\sum_s e_s(a)\) nor the required removals \(r_s(a)\).
An unchanged carry requires no new charge.
The difference \(d_s\) is a new factor, so the carry rule alone does not remove it.

One possible repair is to charge each new difference elsewhere.
That requires its complete read set and the multiplicity of those new owners.
This is precisely the part of UO2 not supplied by the row induction.
Another repair is to group the differences before estimating them. Route three tests that repair.

**Route-one outcome.** Coordinate and constraint ownership survive the prefix, under the ported premises.
The proposed induction does not prove charge ownership for the complete kernel.
The first failed induction step is the passage from a unique remaking operation to a bounded number of its charged uses.

## 6. Second route: pack the collars and charge the visible label

**Attempt.** Cover actual reads by original cells, then use spatial overlap to bound all incidences.
This route does not follow the sequence of coordinate changes.
It tries to obtain the estimate from geometry alone.

There is a strong existing bound at one date.
The set replacements imply
\[
 \Omega_j^{\rm a}\subseteq\Omega_j^{\rm d},\qquad
 (\Omega_j^{\rm d})^c\subseteq Z_j^{\rm a}.              \tag{7}
\]
`sa-2.13.md:220–268` proves the resulting determining-bond and collared-action load bound.
N 78867–78901 gives the corresponding scalar-layer calculation.
They charge an unchanged lower layer one step upward, with its actual factor \(L^4\).
These proofs are ported. Repeating them would not settle UO2.

One can also count spatial overlap directly.
Raise the final floor until \(c_0M<MR_j\).
At a fixed level, a point belongs to collars of at most \(3^4\) partition cells.
In each coordinate, only its own interval and the two adjacent intervals can contribute.
Each original cell occurs at most twice after island cuts, by N 74250–74271.
Thus the multiplicity of **cell collars** is at most \(2\cdot3^4\).
This constant is early and uniform.

The desired multiplicity is different.
Let \(\mathscr E(a,z)\) contain the charged uses at site \(z\) assigned to occurrence \(a\).
The spatial calculation bounds
\[
 \sum_a\mathbf1_{\{z\in Q_a^+\}},
\]
whereas the incidence calculation needs to bound
\[
 \sum_a\sum_{e\in\mathscr E(a,z)}1.                    \tag{8}
\]
The first expression forgets \(e\). Even a single owner can have several uses.
A list of \(r\) reads of one site has union cardinality one and incidence cardinality \(r\).
This is a failure of the proposed inference, not an asserted admissible Yang–Mills history.
The missing bound on \(\mathscr E(a,z)\) cannot be inferred from spatial disjointness.

Reassigning all old reads to the current scale does not repair this argument.
On an interval without a size drop, a level-\(k\) cell contains \(L^{4(k-j)}\) level-\(j\) cells.
Their site counts are at their own levels.
A conversion by \(L^4\) is valid for one step, not for arbitrary \(k-j\).
Charging each old read directly to one current cell therefore requires a separate bound on its coarse multiplicity.
Charging it back to its original cell returns to (8).

Prepared and retained sets do not change this conclusion.
The prepared \(Z''_j\) can be covered by its original hole's cells.
The action support remains the restored support of the factor that was formed there.
N 74302–74320 compares their window volumes under its stated hypotheses.
It does not identify their read lists or their charge incidences.
Using the smaller retained set at an action place would lose actual factors.

**Route-two outcome.** Spatial packing and visible-label loads are controlled at their stated scopes.
The attempted extension fails at the projection from incidences to distinct spatial sites.
It leaves the same UO2 supplier open, without requiring a new live-strip proof.

## 7. Third route: cancel repeated readings before taking the bound

**Attempt.** Keep signed differences together. Telescope them before taking absolute values.
Then use the source recursion and the mass of each inner operation once.
This route seeks an identity of complete kernels, rather than an incidence injection or a packing bound.

On one unchanged coordinate space, (5) gives the exact identity
\[
 F_r+\sum_{s=0}^{r-1}(F_s-F_{s+1})=F_0.                \tag{9}
\]
Thus a rule that charged all these summands separately would waste a real cancellation.
The ownership question cannot be settled by counting textual occurrences of \(A\) alone.

The existing source gives two valid uses of this idea.
First, N 78490–78525 transfers one stored mass to later admitted reads by restricting its supremum.
It does not multiply that mass once per later date.
Second, SA 19190–19241 fixes the unsourced tests, measures, and background choices, and defines
\[
 \Psi_\omega=\Psi_\omega^{\rm new}
        +\sum_y\Psi_{\omega_y}(\xi_y;q_y(\xi)).          \tag{10}
\]
For a drop-out, the new completed-main-step term is absent.
Its carrying Wilson source stays in the carrying action.
SA 19320–19341 then proves the recursive estimate, conditional on the new-part estimate and its owned sites.
These are Sussman and Alpoge's proofs. They are ported here.

The proposed repair is to apply (9) to the **whole** changing operation, thereby supplying those owned sites.
It works across a substitution only if the full density is pulled back, including its Jacobian and seam factors.
The actual operation also marginalizes variables.
For example, N 75915–75932 leaves the integral
\[
 I_W(s)=\int F(\Psi_W(s,a))J_W(s,a)\,da.               \tag{11}
\]
The outgoing variable \(s\) does not determine \(a\).
There is no inverse substitution on the outgoing space with which to telescope all earlier densities.
Keeping \(a\) in the history restores the exact joint kernel.
It also restores every factor reading \(a\), whose charge still needs an owner.

Exact equality after that marginalization cannot substitute for the needed bound before marginalization.
Here is the elementary obstruction to that inference.
Give \(\xi\in\{-1,1\}\) probability \(1/2\), and let \(-1\le p\le1\).
The positive kernel \(K(\xi,p)=1+\xi p\) satisfies
\[
 \tfrac12\sum_{\xi=\pm1}K(\xi,p)=1,
 \qquad
 \tfrac12\sum_{\xi=\pm1}\sup_p K(\xi,p)=2.             \tag{12}
\]
Thus a mass-preserving kernel identity does not identify its inside-integral supremum with the outgoing constant.
This is a counterexample to the attempted inference only.
It is not a Yang–Mills history and is not a counterexample to UO2.

N 78848–78861 supplies the correct composition inequality under a common Borel majorant and admitted reads.
That majorant uses the actual additive volume.
It does not prove that repeated charges fit that volume; using it for this purpose would assume UO2.
Similarly, the carrier criterion at N 77136–77157 starts with already owned site sets.
It bounds the sum of their prices, not their multiplicity in the actual history.

To finish this route, one must identify the grouped factors **before** the supremum and give their charged slots.
One must include the stopped branches of (11), the relative seam factors, and the restored action supports.
Neither the source recursion nor exact measure preservation supplies that grouping.
No analytic source estimate belonging to another registry row is attempted here.

**Route-three outcome.** Pure re-evaluation and the stated source recursion avoid an ancestor factor.
Extending that conclusion to the actual charged kernel fails at the marginalization step (11).
The missing pre-supremum grouping and slot assignment are the same UO2 supplier.

## 8. The discrete record and its conditional price

The replay construction in `sa-2.13.md:104–118` already gives the correct method.
Its use here must retain the revised operation's selectors and seam prescriptions.
The following specifies what its letters must record; it does not assume a bound on their number.

| Part of the record | Data kept | Reconstruction rule |
|---|---|---|
| Geometry | Active level-cell addresses; cut-island roots; selected prepared masks and any other discrete selector outputs. | Reconstruct components in fixed address order. Carry an inner record by its root reference. |
| Ordinary tests | Pass, fail, or unread for each actual test object and type. | Use total tests, including failures where a required object does not exist. |
| Collar/rim rounds | Outcomes at the objects selected by the fixed round rule. | Replay the rule from \(Z^{[0]}\). Its current state determines the next objects and round number. No permutation is summed. |
| Preparation | Completed-stage count, first failed-test type and its outcome locations. | Earlier completed tests passed. Later tests are unread. Keep the actual stopped prefix. |
| Retained coordinates | Native level, slot type, incoming/outgoing row mask and creation identifier. | Carry unchanged slots by identifier. Resolve new slots through the specified chart recipe. |
| Seams | Relative or ordinary prescription, retained/pivot/nonpivot role, and the operation's actual background recipe. | Reconstruct the gauge factor and its arguments together. A solved constraint is not also retained. |
| Frames | The actual frame at each frame slot. | Keep its own factor \(|W_4|^{-1}\), also inside retained islands. |

Selectors whose outputs are not determined by the preceding discrete data must have their outputs recorded.
Calling such a selector “fixed” does not remove those outputs from the code.
Continuous fields and reference draws remain integration variables.
A background recipe is fixed by the operation and its recorded branch; its value is not a discrete letter.
An additional freely chosen recipe would require an additional code and price.

At fixed recipes, frames and continuous arguments, replay these rows in chronological order.
At each move, its input record and the recorded outcomes determine the next discrete state.
If a selector needs more data, its recorded output gives that state instead.
Induction over the finite list of moves therefore reconstructs the discrete history.
This proves finite reconstruction, not the uniform slot bound.

If UO2 holds, the ported finite-record estimate applies.
For example, let \(K\ge2\) bound the local alphabet after finite types are bundled.
Let component headers have at most \(3K_f(R_n+1)^p\) possibilities, as in GEOH's interface.
With \(J\) as in UO2, its collar count gives the sufficient early price
\[
 \begin{split}
 c_R&=\log(2^{r+1}L)+r,\\
 b_{\rm code}
   &=\log2+2J\mu L^4\log K+\log(3K_f)+pc_R.            \tag{13}
 \end{split}
\]
This is GEOH (6), using its proved \(\log(R_n+1)\le c_R\ell_n\), with the actual slot budget inserted.
N 74649–74669 supplies the same conditional multiplication argument.
Normalized frames introduce no additional non-frame entropy.
Selectors, schedules, alphabets, header powers and UO2 constants must all precede \(\kappa\).
Only the stated floors on \(M,R_n,X_0\) may be enlarged later.

The unresolved issue is not the multiplication in (13).
It is the uniform number and ownership of the actual recorded slots and charged reads.

## 9. Result

**Stopping condition (c).** UO2 remains open after three distinct routes:
temporal owner induction, spatial collar packing, and cancellation of complete kernels.
Their failed steps are (6), (8), and the marginalization (11), respectively.
They do not prove UO2 false or show that no fourth route can work.
No actual history breaking the requested bound has been established.

The strongest additional conclusion is the precise reserve implication (4), using the original source volume.
The requested actual entropy and reserve bounds remain conditional on UO2.
The existing geometry, count, row-prefix and mass-transfer results have been ported at their stated scopes.
No claim here closes GEOH-O2 or changes another registry row.

The next mathematical task is exact: supply the charge-slot table through one ordinary move and every stopped-stage branch.
For each newly formed factor, identify its complete read and either a fresh owner or its exact pre-supremum cancellation.
Prove that this table preserves UO2's incidence bound.
Recounting nodes, distinct sites, or normalized frames will not supply this step.

## Status table

| Claim | Standing | Scope or first open input |
|---|---|---|
| Rooted address count | Ported from N 74615–74647; SA 18673–18690 | Connected actual address set and fixed degree. |
| Recursive node multiplicity | Ported from N 74250–74271 | Nodes, not repeated charges. |
| Fixed-width collar volume | Ported from N 74274–74300 | An actual owner map is required. |
| Stage-prefix row assignment | Ported from N 75934–75965 | Full row-block separation and admitted actual chart. |
| Later reuse of one stored mass | Ported from N 78490–78525 | Actual read coverage; unchanged factor and admissible weight. |
| Current visible-label load | Ported from `sa-2.13.md:220–268`; compare N 78867–78901 | Does not count all formed analytic reads. |
| Source-recursion estimate | Ported from SA 19190–19241, 19320–19341 | Actual new-part bound and owned sites remain inputs. |
| Weight comparison (2) and one-step comparison (3) | Proved here | IN1 tube, frame drift and common scale sequence. |
| Spatial collar overlap \(\le2\cdot3^4\) | Proved here, using the ported node multiplicity | Counts cell collars, not all charged uses. |
| Telescoping (9) and the marginalization obstruction (12) | Proved here | Fixed-coordinate identity and an inference counterexample; neither proves or refutes UO2. |
| Reserve implication \(v\le4\mu L^4v^\natural\) | Proved here, conditional | Original \(v\) of SA 17274; actual assignment in UO2. |
| Finite discrete reconstruction | Proved here by replay; method ported from `sa-2.13.md:104–118` | All discrete selector outputs and seam types recorded; no uniform size conclusion. |
| Exponential non-frame count with (13) | Ported conditional count: N 74649–74669; GEOH (6) | UO2 and the finite operation grammar. |
| Revised operation rules, fixed selectors, chart and analytic estimates | Input | Consumed only at their stated scope; other registry lanes are not taken over. |
| **UO2: uniform ownership of actual charge incidences** | **Input; first open input** | **Not proved by any of the three routes in §§5–7. GEOH-O2 remains open.** |
