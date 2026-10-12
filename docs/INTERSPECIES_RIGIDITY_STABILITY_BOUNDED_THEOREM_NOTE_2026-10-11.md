---
claim_id: interspecies_rigidity_stability_bounded_theorem_note_2026-10-11
runner: scripts/interspecies_rigidity_stability_2026_10_11.py
status: provisional
claim_scope: "Uniform quantitative homothety control under explicit six-anchor conditioning and normalized tangent or wedge defects; conditional integration and current consequences."
upstream_dependencies:
  - interspecies_collision_current_rigidity_bounded_theorem_note_2026-10-11
target_claim_type: bounded_theorem
artifact_role: theorem
target_claim_id: null
target_blocker_text: "Quantify the interspecies invariant step under approximate conservation."
source_of_blocker_text: companion_exact_theorem_open_extension
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
promotion_path: "Source-bound independent review and the independent audit path; separately prove physical tangent-defect and conditioning premises."
title: Quantitative labeled interspecies rigidity with conditioned anchors
date: 2026-10-11
claim_type: bounded_theorem
actual_current_surface_status: conditional-support
trace_class: direct_blocker_closure
reachability_to_target: partially_closes
independent_review: completed_for_frozen_S1_S31_source
bare_retained_allowed: false
---

**Type:** bounded_theorem


This note proves a uniform stability theorem for approximate cross-species
parallel secants in three dimensions. Six conditioned velocity anchors suffice;
the remaining label sets may be infinite, disconnected, nonmeasurable, or have
repeated and equal cross-species velocities. The estimate covers every label and
uses no same-species secant constraint. Its constant depends only on the velocity
diameter and two stated geometric conditioning parameters.

The hypothesis is a bound on tangent derivatives, or directly on gradient
secants. Small undifferentiated collision defects alone do not imply it. A
conditional integration and current corollary is proved below with its additional
regularity, symmetry, and path-length assumptions. No physical current law,
collision amplitude, measure, microscopic scattering process, or audit status is
derived here.

## 1. Frozen sources and exact extension

The complete source and independent review were read at these identities:

| Source | SHA256 | Role |
|---|---|---|
| [Exact theorem; frozen source identity below](INTERSPECIES_COLLISION_CURRENT_RIGIDITY_BOUNDED_THEOREM_NOTE_2026-10-11.md) | `ca44d1c852e6cd0437cf9e98913fb5fb106abb1b42567c68fb6bf3e9a60c80b8` | I7–I14 supply the exact geometric target; I15 and I20–I24 identify the integration/current interfaces |
| [Independent review](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/historical/INTERSPECIES_CURRENT_RIGIDITY_REVIEW.md.gz) | `78c3bc3c8f223b988713cb5bd5210c1a801e8cdc5f428ee648d6284c400d97d6` | Exact-scope review, including exceptional lines, equal labels, and supplied physical premises |

The linked exact publication preserves the mathematical source at the hash
above; the hash identifies that frozen source, not its new presentation.
The author also authored the exact source. This extension and its controls are
author evidence, not an independent re-review. The prior Lean packet is frozen;
its formalized exact finite geometry does not formalize the inequalities below.
No prior finite helper is imported into the new helper.

The exact note explicitly left quantitative stability open because noncoplanar
anchors can be ill-conditioned. The new issue is stronger than perturbing one
four-cycle: arbitrary labels can approach the two exceptional lines, and full
affine span by itself gives no quantitative separation of additional anchors.

A bounded local-ref search for quantitative interspecies/secant/bipartite rigidity
and conditioned anchors found only two unrelated protocol matches. Its exact
commands and output are in `interspecies_rigidity_stability/bounded_search.json`.
The searched local `origin/main` was
`a13caa4885f547c8d206265b031ba7649e539fd9`; the worktree HEAD was
`7faf6493528f4064d763a9cdede140d635ef4768`. No fetch, open-PR survey, or global
literature novelty claim is made. The theorem uses only the elementary Euclidean
estimates proved here and the fundamental theorem of calculus.

## 2. Quantified geometric theorem

Let A and B be nonempty label sets, carrying vectors
\((x_a,P_a)\) and \((y_b,Q_b)\) in \(\mathbb R^3\). No assumption makes P or Q
a function of velocity. Let the diameter of the union of the velocity images be
at most \(D<\infty\). Fix A anchors \(x_1,x_2,x_3\) and B anchors
\(y_1,y_2,y_3\), retaining their labels and their P/Q values. Put

\[
 u=x_2-x_1,\quad v=y_2-y_1,\quad d=y_1-x_1,\quad M=[u\ v\ d],
 \quad L_X=x_1+\mathbb Ru,\quad L_Y=y_1+\mathbb Rv.
 \tag{S1}
\]

Assume, for some \(\sigma,h>0\),

\[
 |Mz|\ge\sigma|z|\quad(z\in\mathbb R^3),\qquad
 \operatorname{dist}(x_3,L_X)\ge h,\qquad
 \operatorname{dist}(y_3,L_Y)\ge h.
 \tag{S2}
\]

Thus the initial K2,2 is noncoplanar and each species has a conditioned
noncollinear triangle. In particular \(D\ge\sigma,h\). These finite conditions
are sufficient; full affine span of both entire images is not needed. Full
affine span supplies such choices with positive parameters, but gives no uniform
lower bound on those parameters over a family of images.

The **normalized-direction defect hypothesis** is, for every nonzero cross edge,

\[
 \operatorname{dist}\bigl(P_a-Q_b,\mathbb R(x_a-y_b)\bigr)\le\epsilon,
 \qquad \epsilon\ge0.
 \tag{S3}
\]

There is no equation at an equal-velocity pair. Equivalently,
\(|t\cdot(P_a-Q_b)|\le\epsilon\) for every unit vector t perpendicular to
\(x_a-y_b\), or
\(|(P_a-Q_b)\times(x_a-y_b)|\le\epsilon|x_a-y_b|\).

Define dimensionless constants

\[
 \begin{split}
 \rho&=D/\sigma\ge1,\qquad \tau=D/h\ge1,\qquad B_0=3+8\rho,\\
 T&=2\rho+2\tau(1+\rho),\\
 Z&=6\rho+8\rho^2,\qquad W=8\rho^3+6\rho^2+3\rho,\\
 R&=\max\{T(1+ZB_0),\ WB_0\},\qquad C=T(1+R).
 \end{split}\tag{S4}
\]

**Stability theorem.** Under S1–S3, set

\[
 \lambda=\frac{(P_1-Q_1)\cdot(x_1-y_1)}{|x_1-y_1|^2},\qquad
 b=P_1-\lambda x_1.
 \tag{S5}
\]

Then, uniformly over all labels,

\[
 |P_a-\lambda x_a-b|\le C\epsilon,\qquad
 |Q_b-\lambda y_b-b|\le C\epsilon,
 \qquad
 C\le5586\,(D/h)^2(D/\sigma)^5.
 \tag{S6}
\]

There is no smallness restriction on epsilon, no bound on P or Q, and no
cardinality dependence. The constant is deliberately conservative and is not
asserted optimal. A third A or B anchor may lie on the *opposite* anchor line;
those configurations are included. Equal cross velocities and duplicate labels
are included without a positive minimum relative speed.

## 3. Conditioning the initial four-cycle

For its four nonzero edges write the orthogonal decompositions

\[
 P_i-Q_j=\lambda_{ij}(x_i-y_j)+e_{ij},\qquad |e_{ij}|\le\epsilon,
 \quad i,j\in\{1,2\}.
 \tag{S7}
\]

The alternating sum telescopes. With

\[
 c=(\lambda_{22}-\lambda_{21},\ \lambda_{12}-\lambda_{22},
       -\lambda_{11}+\lambda_{21}-\lambda_{22}+\lambda_{12}),
\]

one obtains

\[
 Mc=-e_{11}+e_{21}-e_{22}+e_{12},\qquad |c|\le4\epsilon/\sigma.
 \tag{S8}
\]

Since \(\lambda_{21}-\lambda_{11}=c_3-c_2\) and
\(\lambda_{12}-\lambda_{11}=c_1+c_3\), both absolute differences are at
most \(8\epsilon/\sigma\). Define residuals at every label by

\[
 r_a=P_a-\lambda x_a-b,\qquad s_b=Q_b-\lambda y_b-b.
 \tag{S9}
\]

Then \(r_1=0\), \(s_1=-e_{11}\), and S7 implies

\[
 |r_2|\le(2+8\rho)\epsilon,\qquad
 |s_2|\le(1+8\rho)\epsilon.
 \tag{S10}
\]

Thus all four anchor residuals are at most \(A_0\epsilon\), where
\(A_0=2+8\rho\) and \(B_0=1+A_0\). Subtracting the homothety preserves S3
and every wedge defect, since its cross-edge difference is parallel to that edge.

## 4. Two propagation estimates without short-edge division

Suppose two opposite anchor residuals, at velocities \(z_1,z_2\), are at most
\(\eta\). Put \(q=z_2-z_1\), assume \(|q|\ge\sigma\), and let r be the
residual at an arbitrary label of velocity x. For \(E=\epsilon+\eta\), S3 gives

\[
 |r\times(x-z_i)|\le D E\quad(i=1,2),\qquad
 |r\times q|\le2D E.
 \tag{S11}
\]

If an edge vanishes, its wedge is zero identically, so no missing equal-edge
equation has been used. Write \(r=\alpha\widehat q+e\), with
\(e\perp q\). Then

\[
 |e|\le2\rho E.
 \tag{S12}
\]

If \(\ell_x=\operatorname{dist}(x,z_1+\mathbb Rq)>0\), the first wedge in
S11 also gives

\[
 |r|\le\left[2\rho+\frac D{\ell_x}(1+2\rho)\right]E.
 \tag{S13}
\]

Indeed, \(|\widehat q\times(x-z_1)|=\ell_x\), so
\(|\alpha|\ell_x\le D E+D|e|\). In particular, if
\(\ell_x\ge\sigma/4\), the right side is at most \(ZE\).

If a third known opposite anchor at \(z_3\) also has residual at most eta and
\(\operatorname{dist}(z_3,z_1+\mathbb Rq)\ge h\), subtracting its wedge
from the first gives \(|r\times(z_3-z_1)|\le2DE\). Consequently

\[
 |\alpha|h\le2DE+D|e|,
 \qquad |r|\le T E.
 \tag{S14}
\]

This triangle estimate is uniform even on its sides, at its vertices, and at
velocities arbitrarily near any anchor. It is an estimate from two independent
anchor *differences*, not an inverse of the angle of each arbitrary cross pair.

## 5. The exceptional-line estimate and completion

Apply S12 to the original opposite anchor pairs, with
\(E=B_0\epsilon\). All A residuals are within \(p=2\rho E\) of
\(\mathbb RV\), and all B residuals within p of \(\mathbb RU\), where
\(U=u/|u|\), \(V=v/|v|\). There are two cases for the selected B anchor y3.

**Case 1: \(\operatorname{dist}(y_3,L_X)\ge\sigma/4\).**
S13 gives \(|s_3|\le ZE\). Since \(ZE\ge A_0\epsilon\), all three B
anchor residuals have this bound. Their triangle and S14 give

\[
 |r_a|\le T(\epsilon+ZE)=T(1+ZB_0)\epsilon\quad\hbox{for all A labels}.
 \tag{S15}
\]

**Case 2: \(\operatorname{dist}(y_3,L_X)<\sigma/4\).**
For A velocities with \(\operatorname{dist}(x,L_Y)\ge\sigma/4\), S13 already
gives \(|r|\le ZE\). It remains to handle the entire tube
\(\operatorname{dist}(x,L_Y)<\sigma/4\), including the line itself.

Choose a unit normal n to \(\operatorname{span}(u,v)\), with \(n\cdot d>0\).
S2 implies

\[
 n\cdot d=\operatorname{dist}(d,\operatorname{span}(u,v))\ge\sigma.
 \tag{S16}
\]

To verify this, minimize \(|d-au-bv|\), and use S2 on the coefficient vector
\((-a,-b,1)\), whose norm is at least one. The two tube conditions therefore
give \(n\cdot(x-y_3)\ge\sigma/2\). This particular cross edge cannot vanish.

Write \(r=\alpha V+e\), \(s_3=\beta U+f\), where \(|e|,|f|\le p\).
S3 on this one edge supplies

\[
 r-s_3=\gamma(x-y_3)+e_*,\qquad |e_*|\le\epsilon.
\]

Taking the n component gives \(|\gamma|\le2(2p+\epsilon)/\sigma\), hence

\[
 |\alpha V-\beta U|\le(2\rho+1)(2p+\epsilon).
 \tag{S17}
\]

S2 also implies
\(|\alpha V-\beta U|\ge(\sigma/D)\sqrt{\alpha^2+\beta^2}\): apply it
to \((-\beta/|u|,\alpha/|v|,0)\), and use \(|u|,|v|\le D\).
Since \(\epsilon\le E\), it follows that

\[
 |r|\le p+\rho(2\rho+1)(2p+\epsilon)
       \le(8\rho^3+6\rho^2+3\rho)E=WE.
 \tag{S18}
\]

For \(\rho\ge1\), \(W\ge Z\), so S18 covers every A label in Case 2.
Combining the two cases gives \(|r_a|\le R\epsilon\) for every A label.
Apply S14 to the A triangle \((x_1,x_2,x_3)\), now all known within
\(R\epsilon\). Every B residual is at most \(T(1+R)\epsilon=C\epsilon\).
Since \(T\ge1\), this also bounds the A residuals. This proves S6.

The proof never imposes an equation at equal velocities. It works separately
for every repeated label, so two P values at one velocity must differ by at
most \(2C\epsilon\); the analogous assertion holds across species too.

For the simpler constant in S6, use
\(T\le6\tau\rho\), \(B_0\le11\rho\), \(Z\le14\rho^2\),
\(W\le17\rho^3\). Then \(R\le930\tau\rho^4\) and
\(C\le6\tau\rho(1+930\tau\rho^4)\le5586\tau^2\rho^5\).

## 6. Unnormalized wedge errors and velocity scaling

Suppose S3 is replaced by the uniform, **unnormalized** condition

\[
 |(P_a-Q_b)\times(x_a-y_b)|\le\omega\quad\hbox{for every pair}.
 \tag{S19}
\]

At equal velocities this is vacuous. It does not imply S3 with epsilon=omega:
for a relative velocity of length ell, the perpendicular error is wedge/ell.
Nevertheless, the conditioned-anchor theorem has the following direct variant,
with no minimum speed required over all labels:

\[
 \max\left\{\sup_a|P_a-\lambda x_a-b|,
 \sup_b|Q_b-\lambda y_b-b|\right\}\le\frac{2C}{\sigma}\,\omega,
 \tag{S20}
\]

where lambda and b are still S5. To prove it, rerun Sections 3–5 with
\(\epsilon_*=2\omega/\sigma\). Every original anchor cross edge has length
at least sigma: its coefficient vector in M is respectively
\((0,0,-1),(1,0,-1),(0,-1,-1),(1,-1,-1)\). Thus its projection error is at
most \(\omega/\sigma\le\epsilon_*\), as required in Section 3. All uses of
arbitrary edges in Sections 4–5 before S17 are only wedge estimates; S19 gives
\(\omega\le D\epsilon_*\), which is exactly their needed bound. The sole
further normalized projection is the tube-to-tube edge in Case 2, whose length
is at least \(\sigma/2\), so its error is at most epsilon*. This verifies every
use of S3 in the proof and proves S20. Directly replacing epsilon by omega,
without this dimensional factor, would be wrong.

Here sigma, h, and D have velocity units; epsilon has P units, and omega has
P-times-velocity units. C is dimensionless. Translating all velocities changes
only the representation of b. Uniformly rescaling all velocities by a positive
factor leaves rho, tau, and the S6 P-error unchanged, while lambda scales
inversely. The S20 prefactor scales inversely with velocity, as it must.

An IR momentum limit does not by itself imply ill-conditioning: the velocity
image of a conical dispersion may retain a fixed angular span. If anchors
instead approach one angular cone on a unit sphere, a normal curvature scale
can collapse faster than their diameter. For an explicit family, take
\(0<t\le1\), \(s=2t/(1+t^2)\), \(a=2t^2/(1+t^2)\), and

\[
 \begin{array}{lll}
 x_1=(0,0,1),&x_2=(s,0,1-a),&x_3=(0,-s,1-a),\\
 y_1=(0,s,1-a),&y_2=(-s,0,1-a),&y_3=x_1.
 \end{array}\tag{S21}
\]

All six velocities have unit norm. One may choose \(D=2s\), \(h=s/2\), and
\(\sigma=a/2\). Indeed the two triangle heights are at least s and
\(s/\sqrt2\), while

\[
 \|M^{-1}\|_F^2=\frac3{2s^2}+\frac3{4a^2}
                  \le\frac9{4a^2}<\frac4{a^2}.
\]

The inverse norm bound proves the displayed sigma. Thus rho=4/t and tau=4;
our conservative C grows at most as \(t^{-5}\) in this family. This is a bound
for this theorem and this angular anchor choice, not an optimal conditioning
exponent or a universal physical IR scaling law.

## 7. Why four-cycle conditioning and qualitative span are insufficient

Here is a continuous labeled-family witness with fixed D and sigma. Let
\(0<\delta\le1\), and use the connected compact velocity sets

\[
 \begin{split}
 X={}&[0,e_1]\cup[0,e_2]\cup\{e_2+t e_3:0\le t\le2\},\\
 Y_\delta={}&\{e_2+t e_3:0\le t\le1\}
 \cup\{e_2+s\delta e_1:0\le s\le1\}
 \cup\{e_2+s\delta e_2:0\le s\le1\}.
 \end{split}\tag{S22}
\]

Both images have full affine span. Their union has diameter at most three.
The fixed four-cycle \(x_1=0,x_2=e_1,y_1=e_2,y_2=e_2+e_3\) has sigma=1.
Set Q=0 on Y, P=0 on the first two segments of X, and
\(P(e_2+t e_3)=(t-1)_+e_3\) on its last segment. These are continuous and
agree on the intersections. All defects vanish unless \(t>1\) and y lies
on one of the short transverse arms. There the normalized defect is

\[
 \frac{(t-1)s\delta}{\sqrt{t^2+s^2\delta^2}}
 \le\frac\delta2.
 \tag{S23}
\]

Yet every homothety has uniform error at least 1/6. If its error is eta,
the values at 0 and e1 give \(|\lambda|\le2\eta\). The values at e2 and
\(e_2+2e_3\) give \(|1-2\lambda|\le2\eta\). Therefore
\(1\le2\eta+4\eta\). This remains an exact counterexample as delta tends
to zero: connectedness, full affine spans, bounded diameter, and a uniformly
noncoplanar initial four-cycle do not give a family-uniform constant without
further conditioning. The B triangle height is of order delta; S2 measures
precisely a missing separation. No necessity or optimality of our particular
six-anchor condition is claimed.

## 8. Integration and the derivative premise

Let \(E_s,F_s\in C^1(O_s)\) on connected open momentum domains, and apply the
theorem to the momentum labels with \(x,y=\nabla E_s\) and
\(P,Q=\nabla F_s\). Assume their velocities satisfy S1–S2 and their gradients
satisfy S3. With \(\delta_g=C\epsilon\), the conclusion is

\[
 |\nabla(F_s-\lambda E_s-b\cdot k)|\le\delta_g.
 \tag{S24}
\]

Fix a base point \(k_s\) and set \(c_s=F_s(k_s)-\lambda E_s(k_s)-b\cdot k_s\).
For the intrinsic path distance in \(O_s\), integration along piecewise C1
paths gives

\[
 |F_s(k)-\lambda E_s(k)-b\cdot k-c_s|
 \le\delta_g\,d_{O_s}(k_s,k).
 \tag{S25}
\]

Connected open domains supply finite paths to each fixed point. A uniform
global error requires a supplied finite intrinsic radius; a convex domain
permits its Euclidean radius. This geometric dependence is not removed by
stating only that the domain is connected and bounded.

The S3 premise has a direct tangent interpretation. At a regular AB pair, a
unit tangent t to the energy shell is perpendicular to the relative velocity.
S3 says that the derivative of the charge sum along every such t is at most
epsilon in absolute value. It follows from a *uniform Lipschitz defect on
shells*, but not from a uniform value defect without a scale or regularity bound.

For example, on balls containing 0 and e2, take
\(E_A=E_B=|k|^2/2\), \(F_A=\nu\sin(mk_1)\), and \(F_B=0\). Every AB
collision has charge defect at most \(2\nu\), whereas at the regular pair
\((0,e_2)\) the gradient difference is \(\nu m e_1\), perpendicular to the
relative velocity \(-e_2\). Its S3 defect is \(\nu m\), arbitrarily large.
The velocities here have full span on fixed bounded domains. This excludes
the unqualified value-defect-to-derivative step, without contradicting S6.

A separately supplied scale/regularity bridge can work. Suppose every unit
shell tangent is realized by a C2 curve \(\gamma(s)\) for \(0\le s\le\ell\),
with \(\gamma'(0)=t\), and its charge sum g obeys
\(|g(s)-g(0)|\le\nu\), \(|g''(s)|\le H\). Taylor's integral remainder gives,
for each \(0<r\le\ell\),

\[
 |g'(0)|\le\nu/r+Hr/2.
 \tag{S26}
\]

Uniform versions of these premises yield S3 with that epsilon. If
\(0<\sqrt{2\nu/H}\le\ell\), the bound is \(\sqrt{2\nu H}\).
The uniform curve length and g'' bound, including shell curvature effects,
must themselves be proved; neither follows from an arbitrarily small value
defect or a qualitative implicit-function theorem near vanishing relative speed.

## 9. A conditional approximate current corollary

This section assumes more than S24 for a generic charge. Suppose
\(E_s\in C^1(O_s)\), \(E_s^2\in C^2(O_s)\), and the *specified* vector charge
is \(J_s=\nabla(E_s^2/2)=E_s\nabla E_s\). Assume S1–S2 for its velocities and
S3 for each scalar charge \((J_s)_i\), with P/Q equal to the corresponding
rows of \(DJ_s\), all with the same epsilon. These are derivative-of-current
assumptions, not consequences of approximate energy conservation.

Apply S6 separately to the three rows. It gives common \(a\in\mathbb R^3\)
and \(B\in\mathbb R^{3\times3}\) such that

\[
 DJ_s(k)=a\,v_s(k)^T+B+\mathcal E_s(k),\qquad
 |(\mathcal E_s)_{i\bullet}|\le\delta_g=C\epsilon.
 \tag{S27}
\]

The exact symmetry of DJ_s implies, after subtracting at the A anchor
velocities x1 and xj, for j=2,3,
\(|a\times(x_j-x_1)|\le4\sqrt3\,\delta_g\): each of the three skew-entry
differences is at most \(4\delta_g\). Decompose a along u as in Section 4
and use the height of x3. This gives

\[
 |a|\le4\sqrt3\,\delta_g
 \left[\frac1\sigma+\frac{1+D/\sigma}{h}\right]
 =\frac{2\sqrt3 T\delta_g}{D}.
 \tag{S28}
\]

Put \(B_*=B+a x_1^T\) and \(S=(B_*+B_*^T)/2\). At the A anchor x1,
S27 and symmetry give \(\|B_*-S\|_F\le\sqrt3\delta_g\). Therefore this
*one common symmetric matrix* satisfies, throughout both species domains,

\[
 \|DJ_s-S\|_F\le |a|D+2\sqrt3\delta_g
 \le\eta_J:=2\sqrt3(T+1)\delta_g.
 \tag{S29}
\]

No derivative of an unknown error is taken. In particular, merely integrating
a generic charge estimate and then differentiating its small value error would
not justify S28–S29.

For any base point and any path of length L from it to k, integration yields
species constants c_s,e_s such that

\[
 |J_s(k)-Sk-c_s|\le\eta_J L,\qquad
 |E_s(k)^2-k^TSk-2c_s\cdot k-e_s|\le\eta_J L^2.
 \tag{S30}
\]

The second bound follows by integrating the first residual *along the same
path*: after arclength r its norm is at most eta_J r, whose integral is
eta_J L²/2 for the potential E²/2. The constants are chosen by the exact value
and gradient at the base point. Infima over path lengths are allowed.

If, in addition, each scalar E_s and each O_s are invariant under the 24 proper
cubic rotations, then DJ_s transforms by conjugation. Average S29 over the group.
The symmetric matrix average is \(\beta I\), with the common real
\(\beta=\operatorname{tr}S/3\), and
\(\|DJ_s-\beta I\|_F\le\eta_J\). Half-turns remove off-diagonal entries and
quarter-turns equate the diagonals, which proves the asserted group average.
If O_s has intrinsic diameter at most L_s, then

\[
 |J_s(k)-\beta k|\le\eta_J L_s,\qquad
 |E_s(k)^2-\beta|k|^2-e_s|\le2\eta_J L_s^2.
 \tag{S31}
\]

For the first bound, average the differences between
\(J_s(k)-\beta k\) and its values at the rotated orbit of a fixed base point.
Each difference is at most eta_J L_s; the orbit values average to zero by
vector covariance and the zero cubic-group average. Integrate its gradient
\(2(J_s-\beta k)\) for the second bound. This argument does not assume that
the origin belongs to the regular domain.

These are conditional approximation estimates with all dimensional scales
displayed. They fix neither the sign of beta nor a lower bound on its magnitude.
No native observable identification, physical collision law, or infrared
error rate is supplied by the current corollary.

## 10. Proof obligations, alternate routes, and controls

The universal geometric proof is Sections 3–5; S20 and the later corollaries
check their additional premises explicitly. No compactness argument, omitted
exceptional set, generic-position assertion for arbitrary labels, or empirical
matrix rank substitutes for those steps.

The first attempted propagation route divided by the angle from each arbitrary
x to the opposite anchor line. Its bound is S13 and diverges on that line;
it cannot prove the target uniform estimate. The normal-plane tube argument
S16–S18 supplies the missing step. A direct finite inverse of the complete
bipartite constraint matrix is another route for finitely many labels, but
its singular value would otherwise hide the geometric conditioning and does
not alone prove the uniform theorem for arbitrary sets. It is used only as a
separate finite control. Inferring tangent derivatives from bounded charge
values fails by the explicit high-frequency example.

The [new helper](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/evidence/interspecies_rigidity_stability/stability_controls.py.gz) uses
SymPy exact rational/symbolic arithmetic. It imports no prior helper and uses no
floating approximations. Its different finite formulation builds the complete
cross-wedge constraint matrix, deletes equal edges, and derives exact dual
coefficients expressing every residual in S9 in terms of independent constraint
rows. If the maximum dual-row l1 norm is L, each wedge component is at most
D epsilon, so each residual vector is at most 2 D L epsilon. This proves a
finite-fixture bound by a different algebraic route; it is not the proof for
arbitrary sets and not an independent reviewer.

| Exact finite fixture | Constraint rank / unknowns | Equal edges omitted | Dual bound coefficient | S4 coefficient |
|---|---:|---:|---:|---:|
| Both exceptional lines and repeated labels | 26 / 30 | 3 | 36 | 2187930 |
| Third B anchor away from the A line | 26 / 30 | 3 | 93 | 2187930 |
| Equal cross velocities at the third triangle anchors | 26 / 30 | 4 | 84 | 2187930 |
| Nonorthogonal affine transform of the first fixture | 26 / 30 | 3 | 26897/105 | 320848031154846/343 |

The complete rational dual matrices are saved as `certificate_*.json` beside the
baseline snapshot. Other exact checks cover the cycle signs and orthogonal
projection normalization; nonnegative-polynomial certificates for all constant
comparisons when rho,tau>=1; the thin-image defect identity and a dual functional
proving its 1/6 error lower bound; velocity dilation of the wedge and residual
matrices; the unit-sphere cone's heights/inverse norm; and the cubic average,
high-frequency derivative, and potential integration factor. The continuum
inequality signs and their stated parameter intervals are proved in the text,
not inferred by a floating sample.

The first baseline completed with exit 0 in 0.406 seconds under a declared
120-second timeout, using Python 3.13.5 and SymPy 1.14.0. Its full output and
exact invocation are in [controls.log](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/evidence/interspecies_rigidity_stability/runs/baseline01/controls.log.gz)
and [execution.json](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/evidence/interspecies_rigidity_stability/runs/baseline01/execution.json).
There was no failed baseline development run.

Four actual source-mutant processes were also run. They reverse a cycle
coefficient, remove the projection denominator, remove extra-anchor height from
the bound, or remove the wedge inverse-scale factor. Each exits 1 at its intended
mathematical assertion; none fails from parsing, imports, or timeout. The height
and wedge mutations are rejected by explicit adverse data and a 1/6 lower bound,
not merely by comparison with copied expected constants. Exact source edits,
identities, commands, and complete tracebacks are preserved in the
[mutation manifest](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/evidence/interspecies_rigidity_stability/mutation_manifest.json) and
its four `mutants/` directories. These are selected discriminators, not
exhaustive mutation coverage.

The [receipt](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/evidence/interspecies_rigidity_stability/receipt.json) binds the final note,
helper, snapshots, rational certificates, complete logs, and source guards.
The frozen source notes, their receipts, and all recorded Lean artifacts were
rehashed unchanged. This task edited no repository or editable prompt files.
The source-bound independent stability review is recorded in the milestone
delivery packet; the exact source's earlier review does not certify this new
proof, and the old Lean compilation does not verify these inequalities.

The bounded geometric stability obligation is discharged under S1–S3, with
S20 as its direct wedge variant. The next application obligation is to produce
the actual uniform tangent-defect bound and geometrically conditioned anchors
at the desired scale. For integrated/current conclusions, the additional
regularity, intrinsic path lengths, current identification, and individual
species symmetry must also be supplied or proved. No result here upgrades an
almost-everywhere value defect to uniform derivative control or supplies a
microscopic conservation selection rule.

## 11. Completed source-bound review and publication controls

The complete independent review of S1–S31 is preserved at
`evidence/INTERSPECIES_RIGIDITY_STABILITY_REVIEW.md.gz` in this milestone,
SHA-256 `6fc511af23a82defd672c9c2c2febd7aa542604a9fbac25fd9e1438119504eee`.
Its receipt is `interspecies_rigidity_stability_review/receipt.json`,
SHA-256 `84be0fc8b21555b5000d99c8cf7cb91a1ffa7638f565a040039674da4b6b3cb9`.
The reviewer reconstructed every argument before inspecting author controls,
used a separate exact smooth-current example on a domain excluding the origin,
and requested no mathematical repair. It does not supply the physical premises.
Root read the complete source, review, helpers and raw outputs and verified
the final source bindings. The earlier pending-review source remains unchanged.

The publication primary preserves the entire executable mathematical helper
body. Its new metadata binds this note and the exact companion; generated
finite dual certificates use a temporary directory. The original full
certificates remain in the historical evidence. Its summary counts nine
finite control families, not proof obligations. Six actual whole-primary
mutations test the cycle sign, projection denominator, anchor-height cost,
wedge scale, potential factor two and cubic average. Their full sources and
logs are preserved separately from the four original author mutations.

The [delivery record](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/aeee46fa0e2879038eec1b8ee8a1e173ac77518e/.claude/science/physics-loops/toe-interspecies-rigidity-20261011/DELIVERY_CHECKS.md)
and exact publication map bind final canonical and repository checks. All
Sections 2–9, including S1–S31, retain the frozen source's mathematical bytes.
The scoped Lean packet covers exact finite geometry only; no Lean certificate
of the stability inequalities is claimed. No audit verdict is applied.
