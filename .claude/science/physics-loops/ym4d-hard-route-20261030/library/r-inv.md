# Invariance of inserted remainder totals
Provenance: Codex (GPT-6 family; exact serving variant and runtime effort not exposed; requested effort max); checkout `408191a7667374b8b510d7b694eed8c7e9958e9f`; Sussman–Alpoge `31a47c543775`; research text, not an audit; no status granted.

## 1. Question and sources

This note addresses row 239 and defect D1 of `gates/b4-ind-check.md`.
It concerns the invariant regular specialization, including constant scalar sources.
Nonconstant source arrays retain the separate problem D2.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline construction.
SA denotes their pinned `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`.
SA 7581 requires invariant remainder totals.
It says: “Both symmetries are part of the definition of ‘renormalised’.”
This passage supplies a requirement, not a propagation proof.
SA 16057–16067 gives defects the weight \(\rho_j^2\), without geometric age decay.
Balaban, CMP 119 (1988), p. 260, (2.32)–(2.33), states the same partition-preserving covariance.
That passage defers its construction proof.
The existing search, `lit-large-field.md` §1, records no healing operation in the YM3 or QED3 manuscripts.

Write \(T_H(\mathbf P)=\sum_X H(X,\mathbf P)\).
For the insertion group \(G=\mathfrak G^{(m+1)}\), (INS) gives
\[
 T_{D_H}(\mathbf P)
 =T_H(\mathbf P)-|G|^{-1}\sum_{g\in G}T_H(g^{-1}\mathbf P).
 \tag{1}
\]
Reindexing \(X\) proves (1).
Thus invariant totals suffice to remove every insertion defect exactly.
Small individual norms do not suffice.

## 2. Transport the formation data

Write an isometry as \(a(x)=Ox+t\), with \(O\in W_4\).
Carry grids, histories, stored fields, independent currents, and frames.
In particular, carry \(r\) to \(Or\).
Naturality means covariance with these data carried.
Invariance requires the fixed formation data to survive this transport.

The adopted rules (N), (T), and (F) have this property.
Their proofs are in `ti-cov.md` §3 and `ti-2.md` §1.
Rule (N) selects the unique smallest collared box on the carried face grid.
Rule (T) orders sites in the carried frame.
Rule (F) gives equal weights to all smallest containing polymers.
Isometries preserve each defining criterion.

The insertion age removes the remaining grid dependence.
Let H have origin j and enter at m+1.
By `ti-2.md`, Lemma 3, every grid side in level-j units is an L-power at most \(M\check R_j\).
The insertion condition gives
\[
 s\mid L^{m+1-j}\qquad\text{for every such grid side }s.
 \tag{2}
\]
Thus insertion translations preserve all formation grids.
Signed permutations preserve their centred cubes.
This includes older test grids, not only the last grid.
The bound \(\check R_i\le L^{j-i}\check R_j\) follows from the weak coupling frame and its fixed floor.
It requires no defect budget.

## 3. The strip substitution under bond reversal

The strip map is natural as a change of integration coordinates.
A simple inversion of its new variable would give the wrong matrix order.
Fix the exterior data of one bond, as in `s210.md` §5.1.
Write
\[
 B=e^{iH}L,\qquad T_{H,L}(W)=Wq(W)L,
 \qquad q(W)=e^{i(1-\theta(W))H}.
\]
Here \(\theta\) depends only on the SU(2) distance from the identity.
The reversed backgrounds have \(\bar L=L^{-1}\) and \(\bar H=-L^{-1}HL\).
Define the reversed coordinate by
\[
 \iota_{H,L}(W)=L^{-1}q(W)^{-1}W^{-1}q(W)L.
\]
Conjugation and inversion preserve the distance.
Hence \(\theta(\iota_{H,L}W)=\theta(W)\), and multiplication gives
\[
 T_{\bar H,\bar L}(\iota_{H,L}W)=T_{H,L}(W)^{-1}.
 \tag{3}
\]
This coordinate map preserves Haar measure.
Indeed, write \(W=\cos u\,I+i\sin u\,n\cdot\sigma\).
Haar measure is proportional to \(\sin^2u\,du\,d\Omega(n)\).
At fixed u, the map sends n through an orthogonal transformation.
Its dependence on u leaves this product measure unchanged.
The two exceptional central elements have measure zero.
Applying (3) twice also gives its inverse.

Let \(J_{H,L}\) be the positive Haar Jacobian of T.
Equation (3) and invariance of Haar measure imply
\[
 J_{\bar H,\bar L}(\iota_{H,L}W)=J_{H,L}(W).
 \tag{4}
\]
Thus the full substituted density transforms correctly, including its Jacobian.
At \(\theta=0\), this is inversion conjugated by B.
At \(\theta=1\), it is inversion conjugated by L.
These are precisely the unshifted and fully shifted charts.

## 4. The moves before the frame sum

The stage tests commute with transported isometries.
Here are the required ingredients, including failed outcomes.

The block average uses every coordinate order.
An isometry therefore permutes its contours and commutes with the average.
The constrained Wilson action and its regularity class are transported together.
A1 uniqueness then transports the critical orbit.
The contour slice (Id) is also preserved.
Its unique representative therefore transports exactly, as in `ti-2.md`, Lemma 1.
The same argument applies to a localized determining set with its boundary data carried.
The tower assignment also transports, by (A7) of `assign-adopt.md`.
It does not replace that slice by a fixed comb tree.

For real B, reversing \(V=e^{iA}B\) replaces A by \(-\operatorname{Ad}(B^{-1})A\).
This preserves its norm and Lebesgue measure.
Plaquette norms, logarithm domains, and contour conditions are consequently transported.
Every stage threshold in SA 17585–17626 depends only on levels, couplings, and shell membership.
Changing the threshold to \(\delta'_j\) changes none of these identities.
The existence test for a regular box extension is preserved by transporting that extension.
Its converse follows by the inverse isometry.
Undefined objects remain undefined because the defining problems are transported bijectively.
Thus complementary tests also commute; see SA 17346.

Hulls, collars, connected components, and bounding boxes commute with isometries.
The repeated boxing and collar/rim rounds therefore commute at every iteration.
The stopping round is the same.
Eligibility for a stage uses size, quietness, joining, and quarantine only.
Each property is preserved, including its full history window.
Rule (N) transports the subsequent nest.

For (L0), the two-block membership test and the pivot constraint are transported.
Uniqueness transports the supported pivot solution.
The value outside its chart is the identity, which is preserved.
For (L1), use the localized background argument above.
For (L2), the transported record gives the same K, C, or F zone.
Equations (3)–(4) transport the actual substituted density in each zone.
For (L3), retaining or dropping an identically-one factor gives the same supported density.
For (L4), transport the erased component and fill its image with the same never-large record.
These are the rules of `s210-fix.md` §2 and `s210-3.md` §3.

The Gaussian operations commute as well.
Differentiating the transported action and constraint transports their Hessians and currents.
Products, inverses, restrictions, and Schur complements preserve this identity.
The adopted carrier series has fixed scalar coefficients and transported carriers.
Its retention rule uses intersection, connectedness, and distance only.
Thus it transports the kept form and the rejected total separately.
This uses the algebra checked in `ti-cov.md` §3, not a new coercivity estimate.

## 5. Frames and the healing gauge

SA 17585 forms “every object” after the stages in its summand's frame.
This includes the reference law, its denominator, both trees, both tests, and the subsequent healing construction.
The passage sketches the covariance mechanism.
SA 17664–17671 supplies the healing formula but does not prove its spatial covariance.

We spell out the frame prescription for its auxiliary choices.
Let c be the core site chosen by rule (T).
Set \(f_{c,r}(y)=c+ry\).
Form the local gauges and partition of unity in these coordinates, using one fixed rule for each normalized geometry.
Then carry them back by \(f_{c,r}\).
This is formation in a frame, not an additional average of gauge transformations.
It preserves every existing estimate because coordinate transport is an isometry.
Existence and analyticity of the local gauges remain the inherited analytic input.

Under \(a(x)=Ox+t\), rule (T) gives \(c'=ac\), \(r'=Or\), and
\[
 f_{c',r'}^{-1}a=f_{c,r}^{-1}.
 \tag{5}
\]
The normalized problem and its prescribed choices are therefore identical.
In particular,
\[
 \chi_{ay}^{aX,Or}(ax)=\chi_y^{X,r}(x),\qquad
 \widehat u_{ay}^{aX,Or}[a\mathbf P](ax)
 =\widehat u_y^{X,r}[\mathbf P](x).
\]
Consequently the quaternion sum in SA 17667 has the same matrix value at corresponding sites.
Its determinant and its square root branch agree.
The normalized healing gauge \(u^{\rm g}\) therefore transports exactly.
This argument needs no gauge invariance of a healed member.

The trees, tree constraints, last-shell test, and reference numerator transport by the same coordinate rule.
Changing raw integration variables transports the reference denominator too.
Hence each normalized reference law transports.
The frame rule includes the cutoffs and all drop-outs after tree fixing.
Those summands must keep their own frame, as SA 17585 and 17654 require.
Earlier drop-outs have no frame dependence, by §4.
Reindexing \(r\mapsto Or\) now transports the complete component operation.

## 6. The remainder total

Let \(\mathcal D\) collect the formation data.
Sections 2–5 prove covariance of each complete move, with its outcome transported.
Composing the moves gives
\[
 a_*\Pi_{\mathcal D}^{o}(\sigma,\cdot)
 =\Pi_{a\mathcal D}^{ao}(a\sigma,\cdot).
 \tag{6}
\]
For tests this follows from their indicators.
For draws and integrations it follows by the changes of variables above.
Unused variables are carried unchanged.
Thus induction on the finite move sequence transports every history, including inner islands.
This proves covariance of the histories themselves, rather than using mass preservation to infer it.

Erasing a healed cluster commutes with a.
Two clusters touch exactly when their images touch.
The bijection of SA 17451 therefore transports the hard-core families and their internal histories.
The completed action of SA 17959–17980 transports too.
It uses the erased history and exact differences of earlier terms.
Exact localization preserves these complete differences.
All pieces are retained in this statement.

Consequently the healed gas and its empty-family action satisfy
\[
 \mathsf K_{a\mathcal D}(a\mathbf P)=\mathsf K_{\mathcal D}(\mathbf P),
 \qquad
 V_{\emptyset,a\mathcal D}(a\mathbf P)=V_{\emptyset,\mathcal D}(\mathbf P).
 \tag{7}
\]
Introduce a scalar dial on every healed activity.
After removing the empty family, the gas equals one when that dial is zero.
Its formal logarithm is then uniquely fixed.
Transport bijects every connected graph, including its coefficient and symmetry factor.
Thus (7) gives covariance of the logarithm coefficient by coefficient.
On a normally convergent domain it gives covariance of the actual logarithm.
This step does not assume a defect estimate.

At the never-large output label, no standing object occurs.
SA 17982–17997 identifies the complete nonempty logarithm with the healed contribution to \(T_{R^{(k)}}\).
There is no boundary part to subtract at this label.
Its total therefore transports by (7).
The regular inputs are the re-pointed Euclidean families of `b4-induction.md`, Step 6.
Their group averages commute with transport by reindexing the conjugate group.
Vacuum subtraction and the scalar Wilson counterterms also commute.
The other contribution is the young-remainder interpolation in SA 17534–17548.
Its endpoints, differences, integrals, and logarithms all commute with transport.
It therefore transports whenever the earlier remainder totals do.
The initial remainder list is empty.
Induction over production levels proves
\[
 T_{H,a\mathcal D}(a\mathbf P)=T_{H,\mathcal D}(\mathbf P)
 \tag{NAT}
\]
for every remainder that (INS) later inserts.

These identities concern the admitted construction and keep its analytic premises.
For independent currents, transport \(\mathbf J\) along with \(\mathbf U\) in every operator and substitution.
The preceding algebra applies on the real slice of that pair domain.
Holomorphy extends it to each common connected complex domain containing that slice.
This uses a real open set of pair coordinates, not only pairs satisfying \(\mathbf J=J(\mathbf U)\).
For physical step reads, (DOM) supplies the earlier covariance classes.
No claim of admission follows merely from this transport identity.

## 7. The defect budget

Fix any insertion and \(a\in\mathfrak G^{(m+1)}\).
Equation (2) fixes all its formation grids.
The frame sum removes the carried-frame change.
Constant scalar sources and the scalar coupling sequence are also fixed.
Thus (NAT) gives
\[
 T_H(a\mathbf P)=T_H(\mathbf P).
 \tag{R-inv}
\]
Equation (1) now gives \(T_{D_H}=0\) at every admitted read.
Vacuum subtraction preserves this equality.

Delete these zero totals before forming the next list action.
Start with the empty defect list and use the same reduced action presentation at each step.
Then the induction bracket is exactly
\[
 \beta_k=F_k(S_{\rm sym}+0)-F_k(S_{\rm sym})=0.
\]
There is no new insertion defect.
Induction gives the input-free defect budget
\[
 d_k=0,\qquad N_k(D)=\sum_{j<k}\rho_{j,k}^{\,2}d_j=0
 \quad\text{for every }k\text{ and every finite run length }K.
 \tag{8}
\]
This is exact, so no summation of the factors \(s_k\) is needed.
It concerns complete list totals.
Restricted domain sums still require their prescribed boundary pieces.
The invariant aged remainders retain their separate size budget.

## Result

**Proof of the spatial naturality step sketched by SA, for the admitted construction.**
With (N), (T), (F), and SA's full frame prescription, (NAT) implies (R-inv).
The prescription includes the transported healing choices of §5.
Thus every (INS) defect has zero total, and the constant-source defect budget is exactly zero.
Repair (c) is unnecessary for these defects.
The proof is by hand and is not independently checked.

**First input still open:** admission of the carried compositions, (D4) in `loc-4.md` §5.
It includes the healing gauges, stored arguments, and logarithm charts at every stage, with complex room.
The symmetry proof does not supply this analytic input or full B4.
Nonconstant-source closure remains D2 of `b4-ind-check.md`.
