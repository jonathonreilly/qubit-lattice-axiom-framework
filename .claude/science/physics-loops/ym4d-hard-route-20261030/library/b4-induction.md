# B4: joint induction over the steps
Provenance: Codex (GPT-6 family; exact serving variant and runtime effort not exposed; requested effort max); checkout `99bf6836b58cdf6bedc5d9ef3af23058ebd2311d`; Sussman–Alpoge `31a47c543775`. Research text, not an audit; no status granted.

## 1. Indices and scope

Credit Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the step construction.
SA means their pinned `YM4_sketch_500.tex`, fetched once to `/tmp/sa_ym4.tex`.
The local sources are the versions in the checkout above. Every argument here is by hand.

Call the step **level k** when its output is \(E^{(k)}\).
Its fluctuation scale is \(k-1\). Thus `b4-step.md` (19) is used with its k replaced by \(k-1\).
Every old regular member then has origin \(1\le i<k\).
This index shift is essential: the step never reads its own output as an old member.

Split Theorem TI into invariance of the step functional, \(\mathrm{TI}^{f}_k\), and of its formed total, \(\mathrm{TI}^{E}_k\).
The first can precede \((ID)_k\); the second cannot.
The induction carries the full member domains and bounds, not just an identity at the trivial field.
In particular, an earlier \((ID)_i\) must hold on all of \(\mathcal K_i\).

## 2. Constants are fixed before induction

Use `c4-order.md`'s table, with `um-envelope.md` §5 and `ti-2.md` §5 inserted in this order.

1. Fix margins, exponents, geometric ratios and counting rates; then odd \(L\), and the weak frame envelope.
   Fix A1–A3's bounds and response radii on their larger admissible classes.
   Use the repaired local-stencil floor \(2r_{\rm loc}\le(8L^2-9)M_1/2\) before the later cube sizes.
   The covariant nest rule has \(K=2\).
2. Retain the uniform matrix input of `um-envelope.md` (6)–(7), with constants fixed before \(M,\bar\kappa\).
   The adopted series supplies this conditionally: `inv-root.md` (17)–(20), `carrier-adopt.md` §6; here \(b_d=32\).
   Set the UM cost envelope to one. Choose \(\kappa,\lambda,\bar\kappa\) with
   \[
   \lambda_0+\sigma_0+\Theta/L<\lambda<
   \kappa/(2C_h^{\rm WF})-\epsilon_{\rm rate},\qquad
   \Theta=C_h^{\rm UM}\{1+2+c_\ell[(1+4\beta_s)\kappa+g_*]\},
   \]
   and \(\bar\kappa\ge\Theta+1,\lambda+2\), as well as c4-order's other rate floors.
   The earlier lower bound on \(L\) makes the interval nonempty.
3. Choose the parameter length, collars and \(M\), with \(\delta_0M\gg\bar\kappa\).
   Require \(H_0e^{b_d\bar\kappa-dM}\le\min(\epsilon_0/2,1/(6DM^4))\).
   This is possible: \(M^4e^{-dM}\le5!/(d^5M)\).
   Choose the tilt budgets and matrix radii as in `um-envelope.md` (2), so \(C_0^{\rm UM}\le1\).
4. Fix the box constants and charts. Then choose the test and core radii.
   For DOM, choose \(c,C_F\) before \(A_1/A_0\le c/(8C_F)\).
   Keep \(CM\alpha_0<\alpha_1\), \(\alpha_1^2\le C\alpha_0\), and SA 7569's cross-level radius ratios.
   Fix WF room, \(c_\nu\), formation constants and the uniform list budget next.
   The extra \(M^4\) pointing count enters these constants after \(M\); it does not change a decay exponent.
5. Choose one coupling floor last. It enforces all core ceilings,
   \(s_{k-1}(1+N_*)\ll1\), and the failed-test bound, uniformly in \(k\).
   Here \(\delta(t)\to0\), \(t\delta(t)^2\to\infty\), and
   \(s(t)=(A_1/C_0)(\log t)^{\mathfrak p_0-q}\to0\).
   Keep \(r\) before \(d_0\), and the weak frame constants before this floor.
   Returned flow constants never select it again.
   Compute \(b_k\) before selecting the next running weight; retain that same weak frame envelope.

Thus this order is conditional on uniform estimates, not on the induction conclusion.
Any repaired domain must supply its constants before the floor, in the same order.

## 3. Inputs and induction hypothesis

Let \(\mathscr P\) denote the inherited analytic package, with all its premises retained:
A1–A3, the contour representative (Id), kernel (K), the adopted operator series,
[QC], [RT], the repaired intrinsic Theorem U′, WF-c, Rule W and the Gaussian identities.
It also includes the torus floors, admissible radius ratios, weak frame bounds, bounded input lists,
and exact filing rules (N), (T), (F), (INS).
These are premises, not results of this induction.

The remaining inputs have the following precise scope.

- **\(BX^+\):** the repaired box package of Proposition W on every complex WF6 disc.
  It must include the Hessian comparison, preservation under substitution, and compatibility with WF-c and every window reader.
  At this commit, `bx-fix.md` ends at line 79.
  It defines the Hölder core (H) and names [PW-H]; it does not prove these requirements.
  DOM and ER7 presently concern the old cores.
  If (H) is used, \(BX^+\) must also establish their needed inclusions and uniform near-zero balls in that core.
  Restricting to real critical inputs alone cannot supply the complex product box.
- **UR, YA:** precisely the uniform Hessian moments and whole-core/young-age bounds in `b2-extract.md`:164–165.
  They must hold for each admitted regular direction and its own counterterm, on the declared domains.
- **LOC:** full read-support locality, including selection and admitted common formation families, through later steps and R stages.
  `loc.md` §§5–7 still retains (N1′)–(N3′). Equality of totals alone does not provide LOC.

Assume \(H_{<k}\): at every completed level \(i<k\), the ordinary map exists on its full product box.
Its full connected gas converges normally, its members have the stated uniform bounds and locality,
and \((ID)_i,\mathrm{TI}^{f}_i,\mathrm{TI}^{E}_i,(R14)_i,(20)_i\) hold on their stated domains.
Use the re-pointed member \(\bar E^{(i)}\) and its own extractor \(b_i=b[\bar E^{(i)}]\).
Carry admitted aged families and their defect budgets as well.
Assume the same input package for the next level; no conclusion at that level is included in \(\mathscr P\).

The base is \(k=1\): the regular list is empty and \(U_0(V)=V\).
There is no cancellation or old-potential estimate to assume at level zero.

## 4. Written order at level k

**1. Domains and the source map.**
Apply `dom.md` §§3–4 before using any gas identity.
Its pivot estimate gives the whole-support datum bound \(C_P\delta_{k-1}<r_B/2\).
A3 and the chosen ratio give
\[
 F_{k-1}(U_{k-1}(V))
 \le cL^{-2}e_k+C_F\delta_{k-1}<ce_{k-1}/2,
 \qquad e_i=\min(\varepsilon_{i-1},\varepsilon_i)\ (i\ge1),\quad e_0=\varepsilon_0.
\]
Changing units and applying A1 on nested fibres identifies every earlier read as
\(U_i(W_i)\), \(W_i\in\mathcal K_i\).
The core ratios in DOM (10)–(11) are bounded by
\(C(\log\Theta_{\rm floor})^{-(q-\mathfrak p_0)}(2/L)^{s-i}\).
One later floor makes them small at every depth.
This proves \((DOM)_k\) from \(\mathscr P\), with the extra core inclusions required by \(BX^+\).

ER7 in `c1-repr.md` §8 uses no activity.
Its crude bound \(C\lambda^{-2}\) on the ball \(c_T/\lambda\) gives a quadratic error \(C\|A'\|^2\).
Thus its near-zero core consequence, ER8u, precedes cancellation and gas convergence.
Finally, `id-step.md` (1)–(4) gives \(B'(u)=a(u)=C_Vu-h_Vd(u)\)
and identifies the response and its current by A1/R9 uniqueness.
This is UM1's **[ID]**, not the logarithmic **(ID)**.

**2. Symmetry of the input and of the step functional.**
For \(i<k\) and either read background \(U\), Step 1 and \(H_{<k}\) give
\[
 \operatorname{Tot}E^{(i)}(\mathbf p_U)=\mathcal E^{(i)}(W_i)+c_i.
\]
For \(g\in\mathfrak G^{(k)}\subset\mathfrak G^{(i)}\), the right side is unchanged at \(gW_i\).
(INS) handles inserted invariant totals. Its origins are earlier: \(M\check R_j\le L^{k-j}\) excludes \(j\ge k\).
Kernel covariance and \(V=gV'\) therefore leave the positive real integral and its subtractions unchanged.
This proves \(\mathrm{TI}^{f}_k\) without \((ID)_k\).
This assertion concerns TI's invariant regular specialization, not an arbitrary spatial source array.
Keep \(H=\mathcal RH+D_H\) exactly; \(\|D_H\|\le2\|H\|\).
Only zero total permits dropping \(D_H\); otherwise its contribution stays in the allowed defect sector.

**3. Cancellation before restrictions, then the old-origin estimate.**
For each \(i<k\), use \((20)_i\) from \(H_{<k}\) before cutting its pointed sum.
Theorem P equates its affine Hessian with \(b_i\sum_{\mu<\nu}\langle F_{\mu\nu},F_{\mu\nu}\rangle\).
The unit tent has the same Hessian without \(b_i\). Absolute moments justify the subtraction.
With ER8u, \(BX^+\), UR and YA, Proposition W then gives, for
\(\sigma=L^{-(k-1-i)}\), the bound
\[
 Cg_i(\rho_i^2\sigma^{4+\alpha_H}+\rho_i^3\sigma^6)
\]
at each old base. The \(C_M\sigma^{-4}\) base count and one WF6 Cauchy estimate give
\[
 \|V_{k-1}^{\rm old}\|_\lambda\le Cs_{k-1}N_{k-1},\qquad
 N_{k-1}=\sum_{i<k}\omega_{k-i}g_i+
              \sum_i\rho_i^2(d_i+r_i)\le N_*,
 \quad \omega_n=C(1+n)^{3/2}L^{-\alpha_H(n-1)}.                 \tag{1}
\]
YA handles the youngest ages, including \(i=k-1\); defects and aged remainders need no (20).
The age series converges: its successive ratio tends to \(L^{-\alpha_H}<1\).
The separate defect/remainder list budget is retained; this age argument cannot bound it.
For site-frozen sources use \(\sup_z g_{i,z}\): each source is a Euclidean family with its own extractor.
Cancellation is applied to that family at its chosen base. No invariance of the whole array is used.

**4. Form and sum the full gas.**
Add (1), the intrinsic Theorem U′ and the finite-stencil pivot/Haar terms.
Their common UM1 budget is
\[
 a_k\le C\{\delta(t)+t^{-1/2}+|x/t-1|+s_{k-1}N_{k-1}\}.
                                                               \tag{2}
\]
The old action difference is independent of the Wilson coefficient \(x\).
The intrinsic and Gaussian bounds hold on their declared \(x/t\) disc.
Thus (2) uses the same complex core and parameter domains, not continuation from a real bound.
LOC supplies common full supports and heredity before grouping polymers.
Apply `b4-step.md` §10 to **all** types, with \(a=a_k\).
Its inequalities (15)–(17) give
\[
 |H_k(Z)|\le\tau_k e^{-\Lambda\ell(Z)},\qquad
 \tau_k=e^\Theta[2c_fL^4S_{\sigma_0}a_k/W_0+
                  n_b e^{-\gamma_{\rm tilt}t\delta(t)^2/2}].
\]
Put \(\mu=(1+4\beta_s)\kappa\) and \(w_Z=\sup|H_k(Z)|e^{\mu\ell(Z)}\).
The chosen rate reserve and small \(\tau_k\) give
\(\sum_{Z'\not\sim Z}w_{Z'}e^{\#Z'}\le\#Z/2\), as in §10.
The rooted recursion \(T_Z^{h+1}=\exp(\sum_{Z'\not\sim Z}w_{Z'}T_{Z'}^h)\),
\(T_Z^0=1\), stays below \(e^{\#Z}\): the preceding bound gives the induction step.
Monotone convergence bounds its full tree sum. Hence the connected series converges absolutely and normally.
Grouping connected components gives its exponential equal to the finite gas, including all older potentials.
This proves nonvanishing of that gas and a holomorphic output, with no label-count or depth loss.

The union bound (18) yields the ordinary map estimate
\[
 \|F_k\|_\mu\le C\{|1-x/t|+\delta(t)+s_{k-1}N_{k-1}
                               +e^{-ct\delta(t)^2}\}.           \tag{3}
\]
Here \(t^{-1/2}\le C\delta(t)\) at the chosen floor.
The potential depends linearly on each old family, including its linear extractor.
For a direction \(\dot S\), (1) allows a complex dial of radius
\(c/[s_{k-1}N_{k-1}(\dot S)]\) within the remaining potential budget.
Cauchy's formula applied to the uniformly bounded gas output gives
\(\|D_SF_k[\dot S]\|_\mu\le Cs_{k-1}N_{k-1}(\dot S)\).
Integrating this derivative along an admitted segment proves the ordinary Lipschitz bound.
For defects retain the exact split \(F(S_{\rm sym}+D)=F(S_{\rm sym})+
[F(S_{\rm sym}+D)-F(S_{\rm sym})]\).
The bracket is the defect output and obeys this bound. TI concerns the first term.
The fixed normalizer bound and (3) close the member bound \(E_0\) chosen before the run.

**5. Identification, now with the full list.**
The source identity from Step 1 and finite substitutions in `id-step.md` (7)–(8) give
\[
 \sum_YV(Y)=-T_3f_x+\log j_V+\Delta S,\qquad
 I_S=\sum_{\Gamma\ {\rm compatible}}\prod_{Z\in\Gamma}H_k(Z).
\]
Step 4 now permits the connected logarithm.
Adding the Gaussian normalizer proves \((ID)_k\), exactly as (9) there:
\(\operatorname{Tot}E^{(k)}(\mathbf p_{U_k(W)})=\mathcal E^{(k)}(W)+c_k\).
Its constant depends on fixed dimensions, normalizations and couplings, not on \(W\).
The logarithm agrees with the real branch by continuation from zero activities.

**6. Total symmetry, re-pointing and the new cancellation.**
At the invariant regular specialization, combine Steps 2 and 5 to obtain \(\mathrm{TI}^{E}_k\) on \(\mathcal K_k\).
Both sides are holomorphic in datum coordinates, so equality extends from a real open ball on each connected domain.
Lemma R's finite group average now preserves this regular total, its norm, locality and companion.
Adopt \(\bar E^{(k)}\) with \(b_k=b[\bar E^{(k)}]\).
The member bound, near-zero core and exponential background response give (D), (Mo), as in `b2-extract.md` §4.
Its gauge and affine-response inputs (C), (G), (AR) remain in \(\mathscr P\).
Theorem P and Corollary R14 then give \((R14)_k\) and \((20)_k\), before any window restriction.
This is the first use of \((ID)_k\) in cancellation.
It prepares the older-origin bound for the **next** step; it did not enter (1).
The base \(k=1\) follows by the same order with Step 3 empty. Thus \(H_{<k}\) extends to \(H_{\le k}\).

## 5. Circularity check

There is no same-level cycle in this written order:
\[
 (ID)_{i<k},(20)_{i<k}
 \ \longrightarrow\ (19)_{k-1}
 \ \longrightarrow\ {\rm gas}_k
 \ \longrightarrow\ (ID)_k
 \ \longrightarrow\ \mathrm{TI}^{E}_k
 \ \longrightarrow\ (20)_k .
\]
DOM and the source-response [ID] enter before these arrows.
The functional symmetry \(\mathrm{TI}^{f}_k\) uses only \((ID)_{i<k}\).
The two diagnostic lines are `ti-2.md`:167, which invokes current \((ID)\) for total symmetry,
and `id-step.md`:187, which requires full connected convergence before identification.
Using current total symmetry to establish that same gas would be circular.
The actual earlier-member read at `ti-2.md`:157 explicitly has \(i<j\), so it does not do this.

The old constants cycle has two opposing lines:
SA **19477**, \(\delta_0M\gg\bar\kappa\), and SA **14583**, \(\log(e^{\bar\kappa}-1)\ge\Theta\).
SA 14526–14528 and 14576 connect \(\Theta\) to the \(M\)-dependent Gaussian cost.
The early matrix constants and §2's cost envelope cut this cycle conditionally.
Without that uniform matrix input, mere reordering would not cut it.
No current-level B4 conclusion is used to establish that input.

## Result

**Proved here by hand, not independently checked:** the joint induction is ordered for the ordinary full-gas step.
For every level \(k\ge1\) of an admissible finite run, uniformly in its length and torus,
\[
 \boxed{\mathscr P+H_{<k}+BX^++UR+YA+LOC
 \ \Longrightarrow\
 B4^{\rm ordinary}_k,\ (1.6)_k,\ (ID)_k,\ \mathrm{TI}_k,\ (20)_k,}
\]
with \((19)_{k-1}\) proved on the way.
The subscripts denote output levels; the source's fluctuation index is one smaller.
The pending Hölder repair, UR, YA and LOC are not discharged.
In particular, the original broad-core BX is false; its repair cannot be silently substituted for it.

**Full B4 has further inputs.**
SA 4006–4037 also requires typed potential, zone and mixed estimates.
For that statement the implication above must additionally assume the actual complex potential test
(SA 5066–5082), the one-zone complex-mass test (SA 5084–5106), and their joint typed bounds.
They must hold on their own domains, with the prescribed counter-insertions and output survival weights.
Cauchy then differentiates those bounds on smaller discs; ordinary convergence supplies neither their domains nor their weights.
Thus the four named queue inputs close the ordinary induction conditionally, not the full finer B4 package.
No audit or scientific status follows.
