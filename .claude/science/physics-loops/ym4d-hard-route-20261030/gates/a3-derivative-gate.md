# Gate of A3 derivative, queue row 89
Provenance: OpenAI Codex / GPT-6 (exact serving variant and configured effort are not exposed; queue requests xhigh); checkout `d5ee4fb43ed7c0fbc095f1ae3898631a178d750e`; Sussman–Alpoge outline `31a47c543775`; research text, not an audit, granting no status.

Credit throughout: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline's definitions, mechanisms and theorem statements; T. Balaban for the underlying averaging/background framework. The outline was fetched once to `/tmp/sa_ym4.tex`. Arguments below are by hand; imported hypotheses and unfinished repairs remain labelled. No numerical or symbolic run discharges a step. Source references without another filename are to `library/a3-derivative.md` at the pinned checkout. Only this report is an output.

`ADVANCE` means a checked conditional reduction, with any explicitly supplied repair below; it does not discharge P81 or P82. `CORRECT-NO-ADVANCE` means a valid reduction/observation that leaves its substantive input open. `WRONG` identifies an unsupported implication or false assertion in the submitted text, not a counterexample to Yang–Mills existence. Inherited dependencies are stated rather than counted again as separate defects.

## 6.1. Identification of the Landau pair

| Statement | Verdict | First failing step |
|---|---|---|
| Own-level node factors, (35), and triangular reduced datum | ADVANCE | None. The outer endpoint factor reads only interior rows of the immediately finer block. |
| Lemma 6.1 | ADVANCE | None. |
| Lemma 6.2 | ADVANCE with the repair below | “$m$ is a submersion because $\tilde q$ is” does not follow from (35). |
| Lemma 6.3 | ADVANCE, conditional on P81 and the stated scalar isomorphism | None. The neighbourhood may depend on the finite geometry. |
| Proposition 6.4 | ADVANCE with Lemma 6.2 repaired and a spanning forest | A single rooted spanning tree does not cover an allowed disconnected region. |

For (35), insert $v_j(z)=v_{j-1}(z)\mathsf v_{j-1}(z)$ at an outward endpoint. Its extra factor is a function of interior rows in $B(z)$; those rows are unchanged by the reduced-datum substitution. Thus its row transformation has identity diagonal and an off-diagonal part whose square is zero. Both its differential and its inverse exist on the prescribed chart. This justifies the kernel and transpose-range identities, including at a seam.

For Lemma 6.1, differentiating the contour ratio gives $i[\chi(y)-\operatorname{Ad}(W_0(y,x))\chi(x)]$. Averaging gives $i(\chi-q\chi)$. Removing this factor leaves the next plain average gauged by $q\chi$. At zero all the accumulated factors equal one, so differentiation of their product is a sum; it telescopes to $i(\chi-Q'\chi)$. The iterated transported mean is exactly the pillar $Q'$ in SA 9634 and 7110–7112, not the comb average. There is no estimate proportional to the depth here.

**Repair of Lemma 6.2 (proved).** Given $h\in\ker K_A$, surjectivity of $K_A$, hence of $D\tilde q_A$, supplies a local curve $A(t)$ in the fixed $\tilde q$-fibre with $A'(0)=h$. This follows by splitting off any right-inverse coordinates and solving the finite-dimensional implicit equation. Put $v(t)=v[A(t)]$. Extend the node gauge

\[
g(t)(y)=v(0)(y)v(t)(y)^{-1}
\]

to the other sites with $g(0)=1$. By (35), $(e^{i\eta A(t)}U_0)^{g(t)}$ has exactly the constant plain datum $m(A)$. Its action equals $F(A(t))$, by gauge invariance. Criticality therefore gives $F'(A)h=0$. The annihilator identity gives $F'(A)=K_A^{\mathsf T}\omega$, uniquely because $K_A$ is onto. This avoids both the unsupported submersion inference and any unproved integrability of $\ker Dm_A$.

For Lemma 6.3, $Q'$ is onto: its pillars are disjoint and the coefficient of the top in each average is a nonzero scalar times the identity. On $\ker Q'$, $R\Delta=\Delta$, by the definition of $\operatorname{ran}R$. Injectivity follows from positivity of the real site Laplacian. A zero-energy site field is parallel on every active bond; every contour transport then carries its value exactly to the top, so $Q'\chi=\chi$ there. The extra small-error argument quoted in the note is unnecessary. This proves the finite-dimensional isomorphism used by the implicit-function theorem, without a uniform bound on its inverse.

For Proposition 6.4, near real zero the repaired multiplier equation, the slice equation, and the triangular datum identity give precisely (28). Continuity puts this pair inside the contraction's uniqueness ball after shrinking this *local* neighbourhood. The identity theorem extends $RD^{\mathsf T}a=0$ over the connected polydisc: successive one-variable identity theorems apply to the real open product neighbourhood. No uniform size of that neighbourhood is needed. Use **one rooted tree per connected component**, rooted at a top. The displayed transport recursion is holomorphic and determines the gauge there; its non-tree equations and all other top equations hold near real zero and therefore everywhere. The same argument proves uniqueness of holomorphic pairs normalized at zero. It claims neither a uniform bound on the bare-site gauge nor transversality away from zero.

## 7. The remaining critical-reference members

| Statement | Verdict | First failing step / limit |
|---|---|---|
| (38) | ADVANCE | None, after 6.1. Reference, slice and transpose pairings must remain fixed. |
| 7.1, $D^{\mathsf T}Dh$ | ADVANCE with the curl-convention expansion below | PX114 concerns the plaquette curl; identifying it with the forward curl without its correction skips a term. |
| 7.2, component Laplacian | ADVANCE | None for the forward-curl convention, on the stipulated interior stencil. |
| 7.3, current | ADVANCE | None on the action-current domain. |
| 7.4, Hölder | ADVANCE | None, conditional on precisely the weighted Hölder output assumed in P82. |
| 7.5, counting multiplier and top gauge | ADVANCE | None for these variables; the outline multiplier still needs M1. |
| Proposition 7.6, potential, second-order and top bounds | ADVANCE | None after the above repairs. |
| 7.6, asserted derivation of complex regularity of $\Phi$ | CORRECT-NO-ADVANCE as a P81 input | The unbounded complex bare-site gauge cannot be dropped from curvature/current value norms. |
| 7.7, higher coordinate derivatives | ADVANCE | None for BGR25–27; the tree rate is $m/q$, not a rate uniform in derivative order. |

The nonlinear estimates actually used are (11)–(12), not Section 5. Here is the density/mesh check. An entry of $K_a$ is bounded by $C\eta^4s^{-3}$ and its row sum by $Cs$ on a row of length $s$. A Cauchy circle of radius $c/(s\sup|h|)$ gives an entry derivative bounded by $C\eta^4s^{-3}s\sup|h|$; a second circle gives the product of two such factors. The fine transpose cancels exactly $\eta^4$, and the bounded overlap of actual row carriers leaves the force amplitude $s^{-3}$. Weights transfer by $e^{\theta D_L}$. Integrating these derivatives supplies the factors $r$ in (11). At an outward row the carrier scales differ by at most a fixed factor $L$; no sum over all layers occurs.

For (12), at a plaquette the cubic SU(2) trace has a factor $\sum_r X_r=\eta^2\mathfrak d a$: the trace of the symmetric cube of a traceless two-by-two matrix is zero. Varying its remaining term and summing by parts gives $a\nabla a$, $\eta(\nabla a)^2$, and curvature corrections bounded by $\kappa\eta\xi^{-2}a^2$. Terms of degree at least four give $a^3$. A difference of an already differentiated remainder costs at most $2/\eta$, cancelled by its displayed $\eta$. Consequently each force is bounded by $Cr^2\xi^{-3}$, and a local Cauchy circle gives $Cr\|h\|_{X,w}$. At the action boundary the crude $C\eta^{-1}|a|^2$ is allowed because that boundary is in layer zero, where $\xi=\eta$. Thus neither the transpose nor the Wilson remainder acquires a depth factor.

**Curl correction (proved).** Write $\mathfrak d=d+E$, where $d$ is the forward covariant curl used in 7.2. Expanding the four plaquette insertions gives, with $P=\partial U_0(p)$,

\[
E h(p)=\eta^{-1}(1-\operatorname{Ad}P)
 [\operatorname{Ad}U_\nu(x)h_\mu(x+\eta e_\nu)+h_\nu(x)]
\]

up to orientation, exactly the convention issue displayed at SA PX117. Hence every entry of $E$ is bounded by $C\kappa\eta\xi^{-2}$. The rows and columns have fixed finite support. The entries of $d$ are at most $C/\eta$, so $d^{\mathsf T}E+E^{\mathsf T}d+E^{\mathsf T}E$ maps $X_w$ to $F_w$ with norm $C\kappa$. No derivative bound on curvature is needed. PX114's remaining sixteen insertion terms have size $C|P-1|\eta^2$; division by the fine pairing $\eta^4$ gives the same $C\kappa\xi^{-2}$ coefficient bound. Any chart/current correction is $C\eta|J|$, again of this size. This supplies the claimed bound on $\Delta'$ in a single consistent forward-curl convention.

Now (38) gives
$d^{\mathsf T}dh=(DK_a[h])^{\mathsf T}\omega+K_a^{\mathsf T}\dot\omega-\Delta'h-N'_0(a)h$.
The four weighted bounds are respectively $C(\kappa+r)\|h\|_X$, $C\|\dot\omega\|_Y$, $C\kappa\|h\|_X$, and $Cr\|h\|_X$. This proves (39). Direct expansion of $d^{\mathsf T}d+DD^{\mathsf T}$ gives (40). Equal-direction shifts commute with their inverses. Each unequal-direction commutator has coefficient $\eta^{-2}(\operatorname{Ad}P-1)$ times a bounded transport. The slice sets $DRD^{\mathsf T}h=0$; the separately assumed $D(1-R)D^{\mathsf T}$ bound supplies the other divergence term. This is not a Laplacian estimate for a propagator.

For 7.3, differentiating $(\Xi_a^{\mathsf T})^{-1}F'(a)$ gives the two displayed terms. The derivative of $\Xi_a^{-1}$ is at most $C\eta|h|$ because its absolutely convergent series has arguments $\eta a$ in a fixed small ball. Multiplying by $K_a^{\mathsf T}\omega=O((\kappa+r)\xi^{-3})$, and using $\eta\le\xi$, proves the current bound. For 7.4, apply the assumed Hölder output directly to the two forcings in (33); do not infer Hölder regularity from a potential bound.

The product rule in 7.5 also differentiates all preceding/following block factors. Their product norms and inverse norms are bounded by
$\exp(C\sum_{n<j}|a_n|)\le\exp(Cr/(L-1))$,
using Section 4.1. The differentiated $n$th factor is at most $CL^n\eta\sup_{\mathrm{pillar}}|h|$. Since
$\sum_{n<j}L^n\eta\le\xi_j/(L-1)$,
this proves the top bound uniformly in depth. The pillar has bounded diameter in the original determining metric, including its adjacent-scale boundary stencils. This also proves the top-value estimate in 7.6 by integration along $tB$. Subtracting the reference current as in 7.6 proves its second-order estimate. The regularity of the representative $\Phi$ on the **complex** polydisc must remain part of P81: conjugating a plaquette by an uncontrolled complex $u(x)$ need not preserve its matrix norm. The real statement has no such problem.

For 7.7, choose each coordinate in turn as the initially differentiated coordinate, apply Cauchy with radius $c_*(1-\vartheta)r_B$, and take the minimum of the resulting exponentials. This yields $(q-1)![c_*(1-\vartheta)r_B]^{-(q-1)}e^{-m\max_i d(y,c_i)}$. The competing star has length at most $q\max_i d(y,c_i)$. These are precisely BGR25–27, with constants independent of the number of bonds, and with the stated loss in rate.

## 8. Reduction of the linear input

| Statement | Verdict | First failing step / limit |
|---|---|---|
| Lemma 8.1 | ADVANCE | None after retaining the original P81 regular-current/criticality input and the repaired $\Delta'$ estimate. |
| Lemma 8.2 | ADVANCE with the finite-colour argument below | One “unit colour phase” cannot align all matrix summands at once. Equivalence is up to a fixed colour factor. |
| Comparison with the comb inverse | CORRECT-NO-ADVANCE | Explicitly unproved operator comparisons remain unproved. |

There is no need to import the old P82 multiplier bound covertly. Lemma 6.2 at zero gives $J=K_0^{\mathsf T}\lambda_0$; $K_0$ is onto because the saddle inverse exists. Thus
$S^\circ(0,\lambda_0)=(-J,0)$,
so $\|\lambda_0\|_Y\le C^\circ\|J\|_F\le C^\circ C\kappa$.
Equation (11) consequently bounds $W_0$ by $C C^\circ\kappa$ as a map $X_w\to F_w$. The new remainder is bounded by $C\kappa r+Cr^2$, not solely $Cr^2$; its derivative is bounded by $C\kappa+Cr$. Choose $\kappa$ after $C^\circ$, then $r$, then $r_B$. The resulting contraction constant is at most $1/4$, and the differentiated inverse has norm at most $4/3$ for every allowed weight. Its Hölder estimate uses the assumed output bound on $S^{\circ-1}$ with the added force $-(\Delta'-W_0)h$. The scalar isomorphism needed in 6.3 was proved there; a corrected-current propagator identification is not needed.

For Lemma 8.2 the easy direction is
$w_i/w_j\le e^{\theta d(i,j)}$.
For the converse fix an output site and a unit output coordinate $e_a$, choose $w_j=e^{-\theta d(i,j)}$, and independently choose each input vector in the direction maximizing $e_a^*A_{ij}v_j$, with its complex phase removed. This gives the weighted sum of $\|A_{ij}^*e_a\|$. Sum over the fixed number of output colour coordinates and use $\|A_{ij}\|\le\sum_a\|A_{ij}^*e_a\|$. Insert the amplitudes and cell weights of (2) before doing this. It proves the claimed **row**-sum equivalence with a fixed dimensional constant, also for gradient output components. It does not prove the column half of BGR11. The set-distance weight in Section 10 is therefore legitimate under this precise, all-weights P82°.

## 9. Other paragraphs of Theorem 4

| Statement | Verdict | First failing step / limit |
|---|---|---|
| 9.1, reference with its actual current | CORRECT-NO-ADVANCE | The contraction is correct, but needs the inverse package on the entire specified complex regular-reference class, not only real critical references. |
| 9.1, independent-current pair | CORRECT-NO-ADVANCE | No operator is specified, so no such system or analyticity-in-pair theorem has been proved. |
| 9.2, identification of the derivative with the flat lift | ADVANCE | None. |
| 9.2, uniform periodisation estimate from mere strip holomorphy | WRONG as stated; conditional repair below | Strip holomorphy alone gives no depth-uniform bound on the symbol or its Fourier coefficients. |

For 9.1, the two differentiated nonlinear products give the same $C(\kappa+r)$ Lipschitz bound as before. The constant force $-J$ affects the size of the solution, not its datum derivative. The displayed augmented second-order equation follows without a slice condition, and (40), together with $D(1-R)D^{\mathsf T}$, gives the component Laplacian. Analyticity in the reference requires a holomorphic family of the actual $R,K_0,S^{\circ-1}$ with common domain and bounds. Real-critical P82° does not assert this extension. The independent-current paragraph is correctly left unspecified in 9.1, but Section 12's unqualified “Theorem 4 with all its members” cannot include it.

For 9.2, $DN(0,0)=0$ and $D\mathsf b(0)=1$, so differentiation of (29) gives exactly the flat saddle lift. **Repair (conditional, input still pending):** require that the actual infinite-lattice inverse symbol, with all intra-block species and scale amplitudes included, is analytic and uniformly bounded by $C$ on a fixed smaller strip. Shifting each Fourier contour by a fixed signed imaginary displacement gives $|K(n)|\le Ce^{-a|n|_1}$. For $|z|_\infty\le\ell_k/2$,

\[
\sum_{n\in\mathbb Z^4\setminus\{0\}}|K(z+n\ell_k)|
\le C'\exp(-a\ell_k/2).
\]

Indeed in every nonzero coordinate $|z_i+n_i\ell_k|\ge(|n_i|-1/2)\ell_k$, and the four geometric sums converge uniformly for the allowed positive lower bound on $\ell_k$. The absolutely convergent periodised inverse solves the periodic operator equation by translation invariance; uniqueness of the periodic saddle inverse identifies it with the torus kernel. This is a hand proof of the implication, not a proof of the uniform symbol input. The statement about constant gauge transformations addresses the scalar kernel only; the field saddle inverse/constraints, already assumed here, are also needed. An arbitrary family $c_kK$ has the same holomorphy strip and arbitrarily large constants, illustrating the omitted quantitative hypothesis.

## 10. Restriction, collars, and Theorem 6(c)

| Statement | Verdict | First failing step / limit |
|---|---|---|
| (G1) for the outline's actual joined sequence | CORRECT-NO-ADVANCE | Cutting a *tower configuration* at a depth (SA 9646, 9769) does not identify the *joined sequence* of SA 9783 with that cut. The note correctly leaves this pending. |
| Metric comparison and (R3) | ADVANCE conditional on the actual collared geometry and (G1) | None. The distance must be the original metric. |
| Lemma 10.1, weighted comparison implication | ADVANCE with the repairs/admission check below | No new analytic failure after 6–8 and 10.2–10.4; identification with the specified joined family remains conditional. |
| Lemma 10.2 | ADVANCE with the boundary/base-case repair below | Its induction base cites only the boundary strip, omitting the other constrained level-zero rows. Its last paragraph also overlooks the change of action current at the new boundary. |
| Lemma 10.3 | ADVANCE for the real fields of this section | None. Unitarity is essential to its product inequality. |
| Corollary 10.4 | ADVANCE on the stated single-layer collars | None in the error recursion; specify the order and support of the gauge construction as below. |

**Geometry.** Memberwise containment implies $\xi'(x)\le\xi(x)$ at each point. Comparing the path integrands, then taking infima, proves $d_{\mathbf B}\le d_{\mathbf B'}$; no comparison of the numbers of tops is involved. For any set $E$, the triangle inequality gives

\[
|d_{\mathbf B}(x,E)-d_{\mathbf B}(z,E)|
\le d_{\mathbf B}(x,z)\le d_{\mathbf B'}(x,z).
\]

Thus the exponential of either the boundary distance or the actual mismatch-set distance is an allowed weight. A collar point can be joined to the relevant part's complement through a bounded number of its outer cubes. That complement is contained in $W^c$ because $W$ is a meet of the parts. These cubes lie in original layer $j_a$, so their path cost is $O(\mu)$ in $d_{\mathbf B}$. It need not be $O(\mu)$ in the joined metric.

**What has not been checked about (G1).** SA 9646 specifies two types of erosion; SA 9783 describes agreement with the old sequence inside and a tower in the collar, with new row levels $q<j_a$. It does not supply a member-by-member gluing formula in these passages. The inequality (G1) is consistent with that description but is not proved by the citation to truncated tower configurations. A visible repair is to specify a compatible tower $T_q$ and set $\Omega'_q=\Omega_q\cap T_q$ (and intersect over parts). Intersections preserve the gap: distance to a union of complements is the minimum of the component distances. Aligned intersections preserve the level-block property. Containment is then immediate. **Still unproved:** that this precise meet has the prescribed old/new row assignment and is the actual localisation consumed in the outline. It would be a proposed replacement until that equality is checked.

Also retain eligibility for Theorem 6(a), not just the displayed (G1)–(G3). Those three conditions alone do not imply separation at higher levels: in an ambient constant torus sequence take $\Omega'_0=W$, $\Omega'_1=C=\Omega'_2$, where $C$ is a proper union of level-two blocks deep inside $W$. They satisfy the three conditions but the gap between members 1 and 2 is zero. This is a counterexample to that possible inference, **not** to separation of a correctly constructed tower. Lemma 10.1 explicitly invokes separatedness; the final pending list must retain its geometric verification for the actual family.

**Lemma 10.2, repaired proof.** At level zero, *every* bond in $W$ with no endpoint in $\Omega'_1$ is a determining row and is fixed, whether or not it is near the boundary. Bonds outside $W$ are fixed by extension. For $m>0$, a relevant bond with an endpoint in $\Omega'_m$ and none in $\Omega'_{m+1}$ is constrained directly. If neither endpoint is in $\Omega'_m$, its two level-$m$ blocks are disjoint from that member, by block alignment. All bonds in the one-step averaging carrier therefore fall under the previous induction statement. This proves equality of its $m$th averages. For an original row, (G1) ensures the required absence of endpoints in $\Omega'_{j+1}$, completing the constraint extension.

To compare actions, only a strip a few bare bonds wide is needed. Choose it strictly narrower than the gap in (G3). Every plaquette crossing the new boundary varies only on fixed bonds, so the difference of the two actions is exactly the difference of their inner-$W$ actions. This proves criticality.

For regularity, the curvature bound improves when the local scale is refined. At a bond with all its plaquettes in $W$, the current is unchanged and its new scale bound also improves. At the new action boundary, however, $J_W$ need not equal $J_{\Omega_0}$. Its new scale is $\eta$. Each surviving plaquette contributes at most $C\eta^{-3}|\partial U(p)-1|$ to the current in the fine pairing, so

\[
|J_W(b)|\le C\varepsilon_1\eta^{-1}
       \max_{p\ni b}\xi_p^{-2}
\le C\varepsilon_1\eta^{-3}.
\]

There are at most six plaquettes. This supplies regularity with a **fixed enlarged radius**, sufficient after decreasing the permitted $\varepsilon_1$. Mixed-scale datum tests use the finer average on the substituted bond; since all values come from the same $U$, composition makes each test an actual plaquette of an intermediate average. Equation (7) on the corresponding carriers bounds it by $C_L\varepsilon_1$. Apply P81 uniqueness only after these radius checks. No boundary Euler–Lagrange equation was silently imposed on a free boundary bond.

**Lemma 10.3, rebuilt.** Exchange adjacent coordinate steps to deform any two of the required paths with common endpoints. The number of exchanges is at most the square of their $O(L)$ lengths, and each exchange inserts one conjugated plaquette or its inverse. Unitarity and telescoping therefore bound the transport difference by $C_L\varpi$. All averaged contour transports in a block are within this amount of a fixed comb transport. The local mean estimate of Section 4.1 and the axial condition make that comb transport $1+O(C_L\varpi)$. Inserting one internal bond between two combs proves the internal-bond assertion. Doing the same with two crossings proves that all corridor bonds are within $C_L\varpi$ of one value $g$; $g$ itself need not be near one. Every straight segment in the average contains exactly one crossing and otherwise internal bonds, so it is $g+O(C_L\varpi)$; the central segment $W[c]$ has the same property. Thus each *closed ratio* $W_x$ is $1+O(C_L\varpi)$, and exponentiating its averaged logarithm shows $\mathcal M(W)(c)=g+O(C_L\varpi)$. This proves both claims without assuming a small corridor holonomy.

**Corollary 10.4, rebuilt.** Work downwards through $m=j-1,\ldots,0$. At step $m$, set the gauge equal to the current averaged contour transport on each level-$m$ site of a block and to one at its centre. Covariance puts that level into block axial gauge and leaves all higher averages unchanged. Define $G$ as the accumulated action of these successive gauges; with the convention $(U^g)^h=U^{hg}$ their final product is in the reverse order of application. This removes an order ambiguity in the displayed product in the note.

Use complete original level-$j$ blocks covering the collar row carriers. Such a block has no original node except its level-$j$ top. It lies wholly in layer $j$ by aligned nesting. Lower-level carriers stay within their two parent blocks. Set the gauge to one outside the blocks used; it then fixes **all** old nodes. Different parts can be treated on disjoint collar blocks by the prescribed separation of their boundaries. Gauge covariance preserves all real plaquette bounds during this process.

The one-step lift copies a coarse bond on a crossing and inserts one on an internal bond, so it is exactly 1-Lipschitz in the supremum matrix norm. Thus

\[
E_q\le C_L\varpi_q+E_{q+1},\qquad E_j=0.
\]

In (7), retain the actual initial curvature size $\varepsilon_1(\eta/\xi_j)^2$; use the fixed small potential bound $\kappa$ only to control the multiplicative product. This gives $\varpi_m\le C_L\varepsilon_1L^{2(m-j)}$. Hence
$E_q\le C_L\varepsilon_1\sum_{m=q}^{j-1}L^{2(m-j)}
\le C_L\varepsilon_1/(L^2-1)$.
There is no hidden $C_L^{j-q}$. The iterated copy/identity lift is exactly the stated lift of $V_j$. In a carrier meeting an original seam this geometric scaling would not follow; the single-layer hypothesis and complete parent blocks are doing essential work.

**Admission and Lemma 10.1.** Apply the restriction estimate and the alignment first. The aligned datum $\mathbf V^U$ is $C_L\varepsilon_1$-regular; its difference from $\mathbf V^J$ is a row logarithm $B_0$ of size $C_L\varepsilon_1$. Every datum test uses four rows and, at a seam, a finite one-step average, so its local Lipschitz estimate shows that $\mathbf V^J$ and every $e^{itB_0}\mathbf V^J$, $0\le t\le1$, are regular at $C_L\varepsilon_1$. Choose $\varepsilon_1$ below this regularity ceiling and $r_B/C_L$. P81 now legitimately supplies the joined reference and the whole interpolation. This also makes the original use of P81 at $U_*$ noncircular.

The weighted forcing is bounded by
$C e^{\theta(c_1\mu+D_L)}\varepsilon_1$:
the original-metric weight is bounded on collar rows by (R3), and the reduced datum only enlarges their carrier by $D_L$. Apply the all-weights saddle estimate and the $4/3$ inverse bound to this **single vector** forcing. Integrate along $tB_0$; apply (39) before integration for the third member. This proves (41) with constants independent of depth and the number of collar rows. The alignment gauge and the residual gauge are both one at old nodes, giving the asserted value of $w$ there. The former metric-ball counting and $L^2$ objections are indeed avoided.

## Consumer check: does Lemma 10.1 give (L)?

**Verdict: ADVANCE for a repaired conditional implication; CORRECT-NO-ADVANCE for the whole class in sa-2.8 §9.** Merely citing (41) and the scalar action inequality misses both a distance identification and an amplitude factor. No counterexample to (L) is claimed.

Use the actual mismatch set $\mathcal C_X$ from that section and redo the *same* proof of 10.1 with
$w(y)=e^{\theta d_{\mathbf D_p}(y,\mathcal C_X)}$.
This is admissible whenever the common joined problem satisfies (G1). Its datum forcing has norm at most $Ce^{\theta D_L}\varepsilon_1$, because the changed rows are supported in $\mathcal C_X$. This bypasses any unproved comparison between distance to $W^c$ and distance to $\mathcal C_X$. On the common level-$k$ plaquette stencil, in level-$k$ units, the repaired result is

\[
|f|+|\nabla f|\le E e^{-\theta D_p},\qquad
E=C_\mu\varepsilon_1,
\]

with a fixed, cutoff-independent upper bound on $E$. A fixed stencil enlargement changes the constant only.

Put the two plaquette holonomies in the common base-point gauge supplied by the real comparison. Expanding their four inserted exponentials gives a linear term $\eta_k^2\mathfrak d f$ and a remainder bounded by $C\eta_k^2|f|^2$; converting the curl adds at most $C\eta_k|f|\,|\partial U_*-1|$. The potential and gradient estimates therefore give
$\|G-H\|\le C\eta_k^2 E e^{-\theta D_p}$.
The two supplied curvature bounds and the real SU(2) squared-norm identity imply only

\[
|a_p(P_X)-a_p(P)|
\le C a_k E\,\eta_k^4 e^{-\theta D_p}.
\tag{L1}
\]

The second factor is **not yet** $a_k$. There are two repairs: prove a collar mismatch of size $O(a_k)$, or spend some distance decay. The latter works for the prescribed admitted real run. SA R19 (6020–6035) and 17334 give
$\min_{i\le k}x_i\ge x_k-c_5$ and
$\check R_k\ge[\log(\min_{i\le k}x_i)]^r$, $r\ge2$.
For a sufficiently small fixed coupling ceiling this yields
$\check R_k\ge c_R(\log x_k)^2$.
Writing $t=\log x_k$, the assumed $D_p\ge c_0M\check R_k$ gives

\[
E e^{-\theta D_p/2}
\le E e^{-(\theta c_0Mc_R/2)t^2}
\le e^{-t/2}t^q=a_k
\]

for all sufficiently large $t$. This last inequality is elementary: its logarithm has a negative quadratic term dominating the fixed constant, the linear term and $q\log t$. Its threshold depends only on the fixed construction constants. Inserting it in (L1) proves (L) with $m=\theta/2=\delta_0/16$. A fixed collar width $\mu$ is essential. Increasing it with the coupling would invalidate this absorption unless its prefactor were re-estimated.

**Still missing for the actual consumer:** identify the specified $P,P_X$ with this common restriction/joined problem, establish its memberwise geometry and separatedness, and verify that its complete mismatch set is exactly the set used in $D_p$, with no changed old row or seam datum outside it. P81/P82° and the admitted-frame hypotheses must hold for that problem and interpolation. The source itself says that the instance has not been checked. The scalar repair above closes no such all-history geometric/domain obligation.

## 12. Pending inputs and disposition

**Section 12's pending list is incomplete as a statement covering all of its advertised conclusions.** Its real-critical nonlinear reduction survives the repairs in this report. Its unqualified final claim covering all of Theorem 4, and its suggestion that the actual (L) consumer can proceed with only P81/P82°/(G1), are **WRONG** without the distinctions below.

The remaining issues, ranked by the conclusions they block, are:

1. **Actual localisation and consumer domain.** Keep the concrete joined-sequence construction, memberwise (G1), separatedness/admissibility, old-node/data matching, and identification of the sa-2.8 mismatch set pending. The meet construction above is a visible repair, not an established identification. The set-distance and missing-amplitude steps of the conditional (L) implication are repaired above.
2. **P82° in the real-critical problem.** Still pending: the all-weights saddle inverse in the actual $R,K_0$ conventions, gradient and Hölder outputs, and $D(1-R)D^{\mathsf T}$. The operator norm/row-sum equivalence must include the differentiated field outputs; potential-kernel row sums alone do not give gradient or Hölder estimates. The comb-to-pillar comparison remains unproved if that route is used. No corrected-current identification is needed.
3. **Extra linear domains for Section 9.** The real-critical input of item 2 does not cover the entire complex noncritical class of 9.1, nor does it specify the independent-current system (M2). Keep the holomorphic family and its uniform bounds explicit. For 9.2 keep the normalized infinite-lattice flat symbol/inverse and uniform smaller-strip bound explicit. These are additional clauses of a proposed P82 package, not consequences of Lemma 8.1 at a real critical reference.
4. **P81 at its actual strength.** It must supply the regular real critical orbit and uniqueness, the local gauges/current bounds used in Section 4 and the collar recursion, and the holomorphic $\Phi$ with its complex regularity and uniform chart radius. The latter regularity cannot be recovered from an uncontrolled complex bare-site gauge. Only the local gauge-fixing neighbourhood in 6.3 is allowed to be nonuniform.
5. **M1 is a statement-matching obligation.** The proved value bound is for the counting multiplier. If the outline chooses datum weights $\mu_c$, its value multiplier is $\mu_c^{-1}\lambda(c)$. For $\mu_c=\xi_c^4$ this inserts an unbounded $\xi_c^{-4}$ factor as the cutoff is removed. Thus choosing a convention is harmless only if the target is explicitly matched to it; the unconverted Theorem 4 value bound is not already proved. SA 11761–11770 requires the actual cell weights.
6. **Local proof repairs, supplied here.** The fibre-curve argument, spanning forest, curl correction, finite-colour row-sum argument, and restriction boundary/base-case checks repair the specific omitted steps without a new uniform nonlinear estimate. The higher-derivative rate loss and the order/support of the collar gauges must also be preserved.

**Research decision:** the Landau identification and real-critical response can advance as repaired conditional implications. Lemma 8.1 genuinely reduces the corrected inverse requirement. The collar comparison can advance under its concrete geometric/admission hypotheses. Do not mark the independent-current paragraph, the flat uniform input, the actual joined-family verification, or the whole (L) class as supplied by this gate. No result here discharges P81 or P82°, runs an audit, or grants status.

**Final checkpoint and source verification.** HEAD remains the provenance commit. The source note, consumer, GOAL and FINISH match that commit; the only repository change is this report. SHA-256: outline d7f77d4da3eb23038250c52468a341281d9ba86b4af21d3371d208a2537d4b6f; derivative note f37cbb7ef56cd51cc65298b95b9cfc193c14184e7e483336959956b3a36aa0b7; consumer 85315fb6910b0377e5827376ae6566c0605540223aef1e76b1566a5a494f9368. These hashes and Git checks are bookkeeping only. Next decision: preserve the repaired real-critical reduction, and obtain the explicit joined-family/consumer matching and the separately scoped linear inputs before claiming the advertised complete package. Section 5's unused second-variation argument was not certified.
