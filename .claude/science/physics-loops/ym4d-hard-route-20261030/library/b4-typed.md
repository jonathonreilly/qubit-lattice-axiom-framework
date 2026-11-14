# B4: typed potentials and zone uses
Provenance: Codex (GPT-6; requested effort max, runtime effort not exposed); checkout `6d367c519f0d145221b3786676c6c50a7354169f`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

## 1. What the outline supplies

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the constructions below.
SA denotes their pinned `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`.
The target is row 219. All arguments below are by hand.

- **Typed potential:** SA 5066–5082 introduces the inequality with “A suitable test is”.
  It requires the full tensor subtraction on the complex pairs used by the integral.
  This is a stated obligation, not a proved extension of the Euclidean case.
  SA 6486–6526 defines extraction through the background response and separately requires the counter-insertion normalization.
  SA (ER13), 6686–6742, proves the extraction bound with its inverse-square radius.
  SA (PW15)–(PW18), ending at 13834, proves the window estimate under its field, Hessian and cancellation hypotheses.
  SA (WF3)–(WF15), 15738–16355, then constructs the ordinary potential on independent outer-pair domains.
  We take these proved implications as cited inputs; they do not establish those hypotheses for a typed family.
- **One zone:** SA 5084–5106 introduces “The required axis estimate has the form”.
  SA 5163–5213 proves the reserve implication, including Cauchy differentiation.
  SA 5318–5344 proves the regular-zone Wilson contribution under curvature regularity at the actual substitutions.
  SA 5434–5464 states the remaining formation bound, including scalar anchors, copies and domain admission.
  SA 5466–5518 proves passage through a pinned cluster logarithm and a conditional copying recurrence.
  Thus the reserve and logarithm arguments are proved; their actual formation inputs remain obligations.
- **Joint tests:** B4, SA 4021–4023, requires “Joint marked derivatives and typed tensor counter-insertions”.
  SA 5215–5316 proves the joint reserve implication under an explicit capacity allocation.
  Its mixed bound uses the mass of the event containing all uses, not a product of separate survival probabilities.
  SA 5004–5015 also proves the marked-slot Cauchy implication.
  We cite these proofs without repeating them. Their common domains and majorants remain hypotheses.

These classifications also agree with SA 5111–5121, 6817–6823 and the ordinary-source construction at 22879–22918.
The latter does not prove the typed extension. The distinction is already explicit in SA 4006–4037.

## 2. Inputs and the first missing implication

Use SA's fluctuation index \(k\); its output is level \(k+1\).
Thus the induction level in `b4-induction.md` is \(k+1\).
Grant its entire premise package

\[
 \mathscr I_{k+1}:=\mathscr P+H_{<k+1}+BX^++UR+YA+LOC.
\]

Write \(\mathscr I\) for these premises at every level of the finite run.
This grants the repaired box package as a premise. It does not assert that row 221 has proved it.
The induction carries Euclidean members with their own scalar extractors.
It also carries defects and remainders with squared-radius costs.
Its conclusion is expressly the ordinary full-gas step (`b4-induction.md`, Result).
Neither its hypothesis nor its conclusion contains the full typed counter-insertion package or a large-field reserve theorem.

The first new input is **(TC)**: the prescribed tensor counter-insertions are linear, gauge-invariant, hereditary holomorphic families.
They must have the matching pointed affine jet, uniform member and Hessian bounds, and the origin's admitted complex cores.
These requirements must hold before any window restriction or bracket.
The ordinary identity (20) supplies this only for Euclidean members and their scalar tent action.

There is no additional demand for an identity on all independent-current pairs.
SA (WF4) constructs a critical inner pair even when the outer current is independent.
Outer and removed substitutions instead use (WF7)'s small differences and their own current assignments.
Thus a polynomial vanishing on the physical graph is not a counterexample to this window construction.
The missing step is admitting the prescribed typed counter-insertions into that construction.

Ordinary Cauchy differentiation cannot supply the missing tensor directions.
Indeed, \(g\cdot E(t)=E(t)\) implies \(g\cdot E'(0)=E'(0)\) for each lattice symmetry \(g\).
But the curvature polynomial
\(Q(F)=\langle F_{12},F_{12}\rangle-\langle F_{13},F_{13}\rangle\)
changes sign when coordinates 2 and 3 are exchanged. It is nonzero for real \(F_{12}\ne0,F_{13}=0\).
It is not a tangent to the Euclidean regular space.
Putting such a direction in the defect space gives the squared-radius cost, not the requested irrelevance cost.

## 3. The precise tensor reduction

Here is the extension that follows once (TC) holds. It does not assume isotropy of a typed direction.
Fix one direction \(E\), origin \(j\le k\), with \(g=\|E\|_{j,\kappa}\).
Retain gauge invariance, locality, companions and the core hypotheses used in Proposition W of `b2-extract.md`.
Let \(T_{j,z}(E)\) denote its full pointed affine Hessian, with the normalization used by its counter-insertions.
Write \(C_{j,z}[c]\) for the **prescribed** insertion; this notation does not choose a replacement.
The required part of (TC) is

\[
 T_{j,z}(C_{j,z}[c])=c,\qquad
 \|C_{j,z}[T_{j,z}(E)]\|_{j,\kappa}\le Cg,\qquad
 \|K_{E-C[T(E)]}\|_{\rm moments}\le Cg\alpha_j^{-2}.       \tag{1}
\]

The bounds include the whole core, young ages and both representatives used by the box comparison.
Extraction alone gives \(\|T_{j,z}(E)\|\le Cg\alpha_j^{-2}\), by SA (ER13).
It does not give the first identity in (1), nor a bound for a prescribed insertion.

Subtract the vacuum and \(C[T(E)]\) from the full pointed sum at \(z\), obtaining \(H_z\).
Linearity of \(T_{j,z}\) and (1) give \(T_{j,z}(H_z)=0\).
Constant colour invariance gives \(DH_z(0)=0\).
Indeed, each coordinate's linear functional annihilates every commutator; commutators span \(\mathfrak{su}(2)\).
Apply the cited (PW15) estimate to each domain of this subtracted family.
Its only leading term is the affine Hessian. The complete sum of these terms vanishes by (1).
Absolute Hessian moments permit this sum before restricting to the window.
The omitted domains retain the exponential tail in (PW17).
Thus, writing \(\sigma=L^{-(k-j)}\), \(\rho=\max(1,\alpha_k/\alpha_j)\), the bound at one base is

\[
 Cg\{\rho^2\sigma^{4+\alpha_H}+\rho^3\sigma^6
                  +(1+\rho^2\sigma^4)e^{-c/\sigma}\}.       \tag{2}
\]

This application uses the actual complex inner pair (WF4), not an identity theorem from real backgrounds.
There are at most \(C_M\sigma^{-4}\) bases in a window.
For any fixed integer \(m>4+\alpha_H\), \(e^{-c/\sigma}\le m!c^{-m}\sigma^m\), by the exponential series.
Together with \(\rho\ge1\), this absorbs the tail into the first term of the window bound.
The other two terms are bounded by \(2Cg\rho^3\sigma^{\alpha_H}\).
The finitely many young ages use (1)'s whole-core bound, as in Proposition W.

All these bounds hold on the same \(\nu\)-disc, \(|\nu|<c_\nu/s_k\), with \(s_k=\delta_k/\alpha_k\).
Cauchy at zero contributes \(s_k/c_\nu\).
Apply the existing outer/removed estimates (WF7) and the common-root brackets (WF13).
Their rate losses were fixed in \(\mathscr I_{k+1}\); no new exponent or label count is used.
Since \(\rho^3\le C(1+k-j)^{3/2}\), this proves

\[
 \|\dot V_{k,j}[E]\|_{\rm pot}
 \le Cs_k\omega_{k+1-j}g,\qquad
 \omega_{a+1}=C(1+a)^{3/2}L^{-\alpha_Ha}.                 \tag{3}
\]

The norm ranges over the admitted local complex cores, the tested real fluctuation box,
and all independent fine parameters \(|s_\Delta|<e^{\bar\kappa}\).
It uses SA 5073–5078's quadratic fluctuation majorant.
Thus (3) is the potential test with \(\varkappa_k=s_k\), **conditional on (TC)**.
Defects and remainders retain \(Cs_k\rho_j^2\|E\|\); a Wilson-weight direction retains its marginal cost.
They acquire no \(\omega\) from this proof.

For finitely many admitted directions, linearity gives the joint potential bound
\(\|\sum_r z_r\dot V_r\|_{\rm pot}\le C\sum_r|z_r|q_r\), where \(q_r\) is its appropriate cost above.
On \(\sum_r|z_r|q_r<b\), choose fixed \(b\) inside the unused B1 budget.
Then `b4-step.md` Section 10 applies with the sum of the type budgets.
This gives a common holomorphic gas bound without a factor counting the directions.
It proves no history survival factor.

## 4. Zone and joint inputs are separate

Here \(k\) denotes the final output level, as in SA's zone test, and \(0<q_a<1\) is fixed.
Use precisely SA 4942–4964's load \(p_n(\delta)\), including marginal amplitudes, increments and still-filed remainders.
For a use \(z=(n,k')\), freeze the tests, measures, evaluation maps and affected histories.
SA 5150–5158 specifies its actual insertion:

\[
 L_{\omega,z}[\delta]
   =\sum_{e\in\mathcal E(\omega,z)}
       \epsilon_e\,\delta F_e(\kappa_{\omega,e})
     +\delta c_\omega.                                   \tag{4}
\]

Each \(e\) includes its prescribed counter-insertions and unit change.
The scalar term \(\delta c_\omega\) must remain.
If the evaluation maps vary, their derivatives must also be included.

The first zone input absent from \(\mathscr I\) is an affected-history mass bound with unspent reserve.
Even granting that bound, one still needs the formation estimate

\[
 |L_{\omega,z}[\delta]|
 \le p_n(\delta)\left(C_V V_\omega+
                         \sum_b a_{\omega,z,b}S_{\omega,b}\right),       \tag{5}
\]

uniformly on the actual external-pair domain.
Here \(V_\omega\ge0\) is a stored-volume charge and \(S_{\omega,b}\ge0\) are available action pieces.
For one use require \(0\le a_{\omega,z,b}\le1\).
The required mass majorant includes \(\exp(c_VV_\omega+c_S\sum_bS_{\omega,b})\), with fixed positive reserves.
Require it for the affected activities, summably after their pinned cluster factors and spatial weights are included.
For histories of age \(a=(k-n-1)_+\), that norm must be at most \(C\epsilon_kq_a^a\).
On drop-outs, its supremum uses the compatible evaluation fibres, as SA 22896–22918 specifies.

Under these inputs, SA's proved reserve and pinned-logarithm lemmas give

\[
 \sup_{|\lambda|p_n(\delta)<r}
       \|R_{k;n,k'}(\lambda)\|_{k,\kappa}
       \le C\epsilon_kq_a^a,\qquad
 r<\min\{c_V/(2C_V),c_S/2\}.                             \tag{6}
\]

Rooting each affected connected cluster at one affected activity gives the same bound for its subseries.
Subtracting its value at zero costs at most a factor two.
This is a citation of their conditional proof, not a new proof of (5) or its mass input.
For nonlinear formed phases, the corresponding bound must hold throughout this disc, not just at zero.
An unintegrated boundary term uses its actual majorant instead of \(\epsilon_kq_a^a\).
The survival factor never divides the input load.

LOC bounds read supports. It does not bound the sum of evaluated copies in (4), or their scalar anchors.
The ordinary B1 majorant bounds the regular gas. It supplies neither the mass input nor (5).
SA 5403–5432 already gives an exact counterexample to replacing the formation bound by ordinary analyticity and carrier oscillation.
We cite it; it is not a counterexample to the Wilson operation.
SA 5346–5401 also proves why an unrestricted bare zone can require action reserve.
The available action must be identified after the other payments.

Joint bounds further require the capacity allocation of SA 5215–5316:
\(\sum_z V_{\omega,z}\le V_\omega\) and \(\sum_z a_{\omega,z,b}\le1\).
For several directions at one use the domain is
\(\sum_i|\lambda_{z,i}|p_{z,i}<r\).
These capacities prevent many uses from spending the same reserve.
They are not consequences of separate axis estimates.
Their actual-history verification is also absent from \(\mathscr I\).

For precision, suppose the common marked connected output is bounded by \(B_A\) on this joint domain
and on Section 3's potential ball \(\sum_r|t_r|q_r<b\).
At a point in both half-sized domains, let \(m=|\alpha|+|\beta|\ge1\).
Cauchy circles of radii \(b/(2m q_r)\) and \(r/(2m p_{z,i})\) remain inside these domains.
Their product Cauchy formula gives

\[
 \|D_t^\alpha D_\lambda^\beta R_A\|
 \le \alpha!\beta!\,B_A
       (2m/b)^{|\alpha|}(2m/r)^{|\beta|}
       \prod_r q_r^{\alpha_r}\prod_{z,i}p_{z,i}^{\beta_{z,i}}.           \tag{7}
\]

A zero cost means independence in that direction and gives a zero derivative.
Thus the derivative step needs no additional level or position constant.
But \(B_A\) must already bound the histories and connected clusters containing the marked uses.
It is not the product of separate survival bounds.
Formula (7) spells out the cited Cauchy implication; it does not establish its joint hypothesis.

## Result

- **Typed potential and its joint potential ball:** Section 3 proves a step the outline leaves as an obligation,
  conditional on the additional typed counter-insertion package (TC). It is not a proof from the stated induction inputs alone.
- **One-zone test:** the reserve, regular Wilson channel and logarithm implications are proved in the outline and cited here.
  No line-by-line check of those proofs was performed. The actual mass and formation inputs remain unproved here.
- **Zone and mixed derivatives:** the outline proves the conditional capacity/Cauchy argument; (7) records its smaller-domain bound.
  This is an application of that proof, not a new closure of the joint typed estimate.
- **First missing input:** (TC), specifically (1) for the prescribed full tensor insertions on their actual cores.
  The ordinary Euclidean induction cannot provide it by differentiation.
  Even with (TC), the history reserve, formed-copy bound (5), and common capacity allocation remain separate inputs.

Full B4 is therefore **not proved from \(\mathscr I\)**.
This note supplies a conditional tensor reduction, not a correction of the outline and not a counterexample to its Yang–Mills step.
The new reduction has not been checked by another model. No status is granted.
