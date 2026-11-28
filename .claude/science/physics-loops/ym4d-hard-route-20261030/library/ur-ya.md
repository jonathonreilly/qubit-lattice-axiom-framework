# UR and YA for the older-origin potential
Provenance: Codex (GPT-6 family; queue requests max effort; runtime variant and effort are not exposed); checkout `bb0761db4`; Sussman–Alpoge commit `31a47c543775`. Research text, not an audit; no status granted.

## 1. Scope and inputs

This note treats queue row 215 and Proposition W of `b2-extract.md`, Section 7. All arguments are by hand.
The target is uniformity in the old level j, the final level k, and volume. Fixed geometric constants may enter C.

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text.
Their outline supplies PH5a, PH20–PH21, and the large-domain and young-age argument at SA 15827–15835, 16034–16044.
The near-zero inclusion is ER8u, from ER7 in `c1-repr.md`, Section 8, with its named inputs.
We retain the actual core memberships supplied by the WF room estimates. This does not assert B4 or its identity.

## 2. The moment implication, with its missing input exposed

Use physical coordinates \(v=(A,J)\), where \(U=e^{i\eta_jA}\), and
\(\|v\|_{1,j}=\max(\|A\|_\infty,\|\nabla_jA\|_\infty,\|J\|_\infty)\).
The difference \(\nabla_j\) includes division by \(\eta_j\).

First, ER7 gives a ball of radius \(a_j=c\alpha_j\) in the core.
Indeed, on that ball,
\[
 |\partial e^{i\eta_j A}-1|
 \le C\eta_j^2(a_j+a_j^2).
\]
The linear term is the curl; every remaining term has at least two potentials.
Choose \(c\) so that \(CK_T(c+c^2)\alpha_j<\alpha_j/2\), using the fixed small ceiling on \(\alpha_j\).
Also choose \(c\alpha_j\) below the supplied potential and current radii.
The real factor is 1. ER7 now supplies all tower clauses, uniformly in j.
This is the ER8 argument at SA 6586–6633. It proves inclusion, not a response estimate.

Here is the additional input which PH5a needs:
\[
 \|h_j\delta_{x,\mu}^a\|_{1,j;X}
 \le C_R e^{-\delta\operatorname{dist}(x,X)},                 \tag{R}
\]
with \(C_R,\delta>0\) independent of j, for the **actual** response in PH4.
Assume (R) for this paragraph. Two-variable Cauchy on
\(\|s v+t w\|_{1,j;X}<a_j\) gives
\[
 |D^2G(X,0,z)[h_j\delta_x,h_j\delta_y]|
 \le Cg_j\alpha_j^{-2}e^{-\kappa d_j(X)}
 e^{-\delta(\operatorname{dist}(x,X)+\operatorname{dist}(y,X))}. \tag{1}
\]
Take the two circle radii \(a_j/(4\|v\|)\) and \(a_j/(4\|w\|)\).
This gives (1) without any factor counting bare coordinates.

Choose \(0<m<\delta/2\) with \(2mC_M<(\kappa-\kappa_D)/2\).
For \(z\in X\), \(|x-z|\le\operatorname{dist}(x,X)+\operatorname{diam}X+O(1)\).
Enclosing X in a coarse box shows
\[
 \sum_x e^{-(\delta-m)\operatorname{dist}(x,X)}
 \le C(1+\operatorname{diam}X)^4.
\]
To see the bound, the shell of integer width q has at most \(C(D+q)^4\) sites.
Sum its weight \(e^{-(\delta-m)q}\), and use \(D+q\le D(1+q)\), \(D\ge1\).
The two bond sums and the rooted count therefore give
\[
 C_m(z)\le Cg_j\alpha_j^{-2}
 \sum_{q\ge0}(q+1)^8
 e^{-(\kappa-\kappa_D-2mC_M)q}
 \le C'g_j\alpha_j^{-2}.                                  \tag{2}
\]
The series converges because \((q+1)^8e^{-\varepsilon q/2}\) has a finite maximum for every \(\varepsilon>0\).
Colour and orientation counts are fixed. The finite grid average costs at most \(M^4\).
All sums converge absolutely before any window restriction. Constant-colour invariance gives \(DG(X,0,z)=0\), so this is the composite Hessian.
Thus **ER8u plus (R) proves UR**. This rebuilds SA PH5a; it does not remove (R).

## 3. First failing input: (R) for the adopted representative

`b2-extract.md`, Section 4, fixes (Id): \(P_j\) uses the augmented contour-gauge branch \(u_{0,j}\).
Its derivative is \(R_{0,j}\) of `prefactor-loc.md`, Section 2, converted from link angles to physical potentials.
Lemma B there proves decay only at fixed depth. It was checked in `b-value.md`, Section 1.

**The uniform physical norm estimate (R) is false for this representative.**
Here is a hand example. Put \(s=L^j\), \(\eta=s^{-1}\), and choose a colour matrix \(|T|=1\).
Set the coarse field \(B_1=T\), \(B_\mu=0\) for \(\mu\ne1\).
Define a fine link-angle field v by
\[
 v_1(b)=
 \begin{cases}
 T,&b\text{ crosses a face between adjacent level-j blocks},\\
 0,&\text{otherwise},
 \end{cases}
 \qquad v_\mu=0\quad(\mu\ne1).                              \tag{3}
\]
Only faces normal to direction 1 occur in (3).
Parallel 1-bonds on every plaquette have equal values, so \(dv=0\).
Every contour inside a smaller block misses these faces.
Each coarse path across a final block crosses exactly one face.
Induction over the averages therefore gives
\[
 Q_{0,j}v=B,\qquad \tau_rQ_{0,r}v=0\quad(0\le r<j).
\]
Thus \((v,0)\) solves the augmented saddle equations in `prefactor-loc.md`, Section 2.
Their fixed-depth uniqueness gives \(R_{0,j}B=v\).
Equivalently, \(e^{itv}\) has zero Wilson action and zero contour gauge terms, with the prescribed coarse datum.

In the physical chart the response is \(H_jB=\eta^{-1}v\). Hence, at a crossing and its neighbour,
\[
 |H_jB|=\eta^{-1},\qquad |\nabla_jH_jB|=\eta^{-2}.           \tag{4}
\]
If (R) held, summing it over the constant coarse source would bound these values independently of j.
Indeed, for a fixed-size coarse domain X the sum
\(\sum_x e^{-\delta\operatorname{dist}(x,X)}\) is uniformly finite.
To use only compact data, truncate B and pass to the limit at fixed j using Lemma B's exponential decay.
Equation (4) contradicts the resulting uniform bound as \(j\to\infty\).

The checked A3 bound concerns a different response: \(H_j^{\rm L}=D\mathcal H_j(0)\), in Landau gauge.
`flat-port.md` (9.9) and `a3-derivative.md` (34), (39), Section 7.3 give
\[
 |H_j^{\rm L}\delta_x|+|\nabla_jH_j^{\rm L}\delta_x|
 +|D^*D H_j^{\rm L}\delta_x|
 \le Ce^{-\delta\operatorname{dist}(x,X)}\quad\text{on }X,   \tag{5}
\]
on the uniform level-j lattice. All output scales there are 1.
The checks are `gates/flat-port-gate.md` and `gates/a3-derivative-gate.md`, Section 7.
No bare-bond counting measure enters (5).

One cannot substitute (5) into (1) without a gauge identity for G's Hessian.
For the constant datum above, the smooth response is constant T.
The gradient converting it to (3) varies inside each final block.
It is not a block-constant gauge direction.
The checked class inputs used in `b2-extract.md` supply only the block-constant subgroup;
see `carrier-adopt.md`, Lemma L(c) and its following limitation.
They do not prove
\[
 D^2G(X,0,z)[(d\chi,0),w]=0
\]
for these intra-block gradients.

This refutes the proposed uniform-response input, **not UR itself**.
A proof of that extra Ward identity, or a direct bound for the actual contracted Hessian, could still prove UR.
Full local gauge invariance would supply the identity by differentiation, since \(DG(X,0,z)=0\).
It is a stronger premise than the checked subgroup invariance; we do not add it here.

## 4. The whole-core bounds and the own tent

The following bounds do not need a small datum ball.
Core membership gives \(|G(X,P,z)|\le g_j e^{-\kappa d_j(X)}\), hence
\[
 |G(X,P,z)-G(X,0,z)|\le2g_j e^{-\kappa d_j(X)}.              \tag{6}
\]
Here 0 denotes the pair \((1,0)\). This holds on the whole WF disc whenever the stated core membership holds.

For a complex plaquette holonomy \(W\in SL(2,\mathbb C)\),
\[
 A_p(W)=1-\tfrac12\operatorname{tr}W
       =\tfrac12\det(W-1),\qquad |A_p(W)|\le C|W-1|^2.
\]
The core curvature bound is \(|W-1|\le C\alpha_j\eta_j^2\).
For each plaquette orientation the midpoint tent satisfies
\(\eta_j^4\sum_p h_z(p)=1\).
Indeed, with \(\eta_j=1/s\), its one-dimensional sums are
\[
 s^{-1}\left[1+2\sum_{r=1}^{s-1}(1-r/s)\right]=1,
 \qquad
 2s^{-1}\sum_{r=0}^{s-1}(1-(r+\tfrac12)/s)=1.
\]
Multiply the four factors, with two half-shifts. Summing the six orientations proves
\[
 |A_{j,z}(P)|\le C\alpha_j^2                              \tag{7}
\]
on the whole core, uniformly in j. This is SA's whole-core assertion at 13570–13577, proved directly.

The tent also has a uniform **unmultiplied** Hessian moment.
At the flat field, its Hessian kills every fine gradient, by full gauge invariance and \(DA_{j,z}(1)=0\).
The contour representative and the Landau representative are gauge related, by the background construction and the Landau pair identity.
Differentiating that gauge transformation at 1 adds a fine gradient, whose curl is zero.
Thus its kernel equals
\[
 K^A_z(x,y)=\sum_p\eta_j^4h_z(p)
 \langle d_{\eta_j}H_j^{\rm L}\delta_x(p),
         d_{\eta_j}H_j^{\rm L}\delta_y(p)\rangle.
\]
Here \(d_\eta H=\eta^{-1}\sum_{b\in\partial p}H(b)\).
The first-difference member of (5) bounds each factor by \(Ce^{-\delta|x-z|}\) on the tent, after a fixed constant enlargement.
Quadrature bounds the kernel by \(Ce^{-\delta(|x-z|+|y-z|)}\).
For any \(m<\delta\), its weighted bond sum is finite uniformly in j.
This proves the mechanism at SA 13323–13345 for the action. It does not prove the same gradient identity for G.

For the **multiplied** own tent one still needs
\[
 |b_j(G)|\le Cg_j\alpha_j^{-2}.                            \tag{8}
\]
UR would imply (8): the extractor is the second displacement moment of \(K_z\).
If \(r=|x-z|+|y-z|\), its polynomial weight is at most \(C(1+r)^2\le C_m e^{mr}\).
Apply (2), then the prescribed bulk reindexing. Thus (7) would give \(|b_jA_{j,z}|\le Cg_j\).
Without UR or another proof of (8), the proved bound is only \(C|b_j|\alpha_j^2\).

## 5. Large domains and young ages

**Assume (8) in this section.** File the own tent once, on a fixed domain containing its support, as in WF13a.
Its diameter and tree length are fixed in level-j units. Absorb \(e^{\kappa d_j(X)}\) for that one domain into C.
Equation (7) then gives the same domain weight as (6). No separate extractor is assigned to each original domain.

Put \(D_X=2+\operatorname{diam}_jX\), \(\sigma=L^{-(k-j)}\), and \(\rho=\max(1,\alpha_k/\alpha_j)\).
For \(T_X=\rho\sigma^2D_X\ge1\), (6)–(8) bound the vacuum-subtracted member and its filed tent by
\[
 Cg_j(1+T_X^2)e^{-\kappa d_j(X)}
 \le 2Cg_j\rho^3\sigma^6D_X^3e^{-\kappa d_j(X)}.             \tag{9}
\]
The optional affine quadratic value of the tent obeys this bound too:
its exact normalization gives \(C|b_j||F|^2\le Cg_j\rho^2\sigma^4\le Cg_jT_X^2\).
The rooted count sums \(D_X^3e^{-\kappa d_j(X)}\), since \(\kappa>\kappa_D\).
Thus large domains contribute at most \(Cg_j\rho^3\sigma^6\), the second term of WF8.
Changing the small-domain threshold to a fixed \(t_0<1\) only changes C in (9).

For young ages write \(n=k-j\). The supplied axial datum estimate and radius comparison give
\[
 \|B\|_\infty/r_{B,j}\le C_0\rho L^{-n},\qquad
 \rho^2\le C_a(1+n).
\]
Induction gives \(1+n\le2^n\). Hence
\(C_0\rho L^{-n}\le C_0\sqrt{C_a}(\sqrt2/L)^n\).
Choose an integer N with \(C_0\sqrt{C_a}(\sqrt2/L)^N<1/2\).
It exists because \(L\ge3\). Every failure of the half-datum-ball condition has \(n<N\).
This choice depends on fixed constants only.

At those ages retain the actual core membership, and use (6)–(8) directly.
After the domain sum their bound is \(Cg_j\).
Since \(\rho\ge1\) and \(\sigma\ge L^{-N}\),
\[
 Cg_j\le CL^{(4+\alpha_H)N}g_j
       [\rho^2\sigma^{4+\alpha_H}+\rho^3\sigma^6].           \tag{10}
\]
This proves the young-age part of YA, conditional on (8), without an increasing number of exceptions.
Equations (9)–(10) are the hand argument behind SA 15827–15835 and 16034–16044.

## Result

Proved here by Codex, not yet checked by the other model:

- ER8u and a uniform response in the **same Hessian** imply UR, by (1)–(2).
- The whole-core bounds for G and the unmultiplied own tent are (6)–(7).
  The tent's Hessian moments are uniform because its Hessian kills all fine gradients.
- Given the coefficient bound (8), large domains and all young ages satisfy YA, by (9)–(10).

**First failing input:** (R), equivalently SA ER12, for the contour-gauge response fixed by (Id) in `b2-extract.md`.
The explicit flat field (3) disproves its uniform physical norm bound.
The checked Landau estimate cannot replace it without an additional Hessian gauge identity for G.
Thus UR for the actual member, and YA for its multiplied counterterm, remain open here.
This is not a counterexample to UR, YA, or (19). No status changes follow.
