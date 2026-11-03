lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T11:12Z

# s210-fix: the reconstruction map with an admitted chart, and the repaired Theorem E

Queue row 203. Claude Opus 5.5, effort max, Mac mini worker. Pinned at commit 9e98c836e, branch `claude/ym4d-hard-route`.
Research-stage working state. One reading by one model. It is not an audit and grants no status.
Sources: Sussman-Alpoge `YM4_sketch_500.tex` at `31a47c543775` (fetched by URL; "SA L" = its line), credited to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text. Used here: the block map and its domain (L7071-7075), the double block and contour means (L7944-7990, (QC1)-(QC3), (QC7), (QC8)), the pivot (L8165-8175), the pivot chart (L7483-7487, L8259-8295), the step tests and Lemma 2.2 (L17317-17398), the strip (L17518), the operation R (L17585-17614), Theorem 6 (L9776-9783). Codex's `library/s210.md` (6)-(9); Claude's `library/s210-3.md`; Codex's check `gates/s210-3-check.md`.
Every step is a hand argument. No computation was run.

## 0. What this note repairs

The check found one root defect. Definitions 3.1-3.2 of `s210-3.md` say "pivots from the constraint", but SA's chart is only local (SA L7487, L8287-8295). So the reconstruction $\Phi_h$ was not defined at every coordinate, and nothing showed that its domain contains the supports. Theorem E (case 3), Corollary K and P's read closure failed through this. Two defects are independent of it: Lemma N's condition (N1) is too weak, and the code in P(c) omits the failure location inside $\mathbf R$.

| Defect (check section) | Repair | Here |
|---|---|---|
| Defs 3.1-3.2: no chart (3) | Lemma G: on the support, the constraint has exactly one pivot solution in all of SU(2). Defs 3.1'-3.2' then define $\Phi_h$ at every coordinate. | §1, §2 |
| Theorem E cases 3, 6, 7 and (E) (4) | Lemma C: one common chart indicator, implied by the tests in both histories and by the fill. Theorem E'. | §3, §4 |
| Corollary K (5) | follows from Theorem E' (d) | §5 |
| Lemma N, label-local family (5) | stopping nests (N1'); Lemma N' | §6 |
| $F=\log J$ (5) | hypothesis (N3'): ${\rm Lip}(\theta)\sup_n\|H^{(n)}\|<1/2$ | §6 |
| P(c) (6) | a failure-location symbol; at most $\mathsf N_j+6$ values | §7 |
| P read closure (6) | chart reads lie inside test reads | §7 |

Unchanged from `s210-3.md` (checked by Codex): Proposition D, P(a)-(b), rules (L1)-(L4) as definitions, and Lemma N's telescoping and $C^1$ estimate under their hypotheses.

## 1. Lemma G: the pivot constraint has one solution on the support

**Metric.** For $U\in{\rm SU}(2)$ with $U\ne-\mathbf 1$, let $\ell(U)$ be the Hermitian traceless $A$ with $\|A\|<\pi$ and $e^{iA}=U$. Put $d(U,V)=\|\ell(UV^{-1})\|$ (and $d=\pi$ at $UV^{-1}=-\mathbf 1$), and $a(U)=d(U,\mathbf 1)$. On traceless Hermitian $2\times2$ matrices the operator norm is the Euclidean norm of $\mathbb R^3$. So $d$ is the geodesic distance of the bi-invariant metric for which SU(2) is the unit 3-sphere. It is invariant under left and right translation and under inversion.

- (F-a) $d(e^{iA},e^{iB})\le\|A-B\|$ for all $A,B$.
- (F-b) On a geodesic segment where $a\le\theta_*<\pi$, $\ell$ is Lipschitz with constant $\theta_*/\sin\theta_*$. For $\theta_*\le1$ this is at most $1+\theta_*^2/5$.

*Proof.* $A\mapsto e^{iA}$ is the Riemannian exponential map at $\mathbf 1$. On the unit sphere its differential at $A$ has singular values $1$ (radial) and $|\sin\|A\||/\|A\|$ (twice). All are at most $1$, which gives (F-a) by integration along $s\mapsto(1-s)A+sB$. The inverse has singular values $1$ and $\theta/\sin\theta$, which gives (F-b). For $\theta\le1$, $\sin\theta\ge\theta-\theta^3/6$, so $\theta/\sin\theta\le(1-\theta^2/6)^{-1}\le1+\theta^2/5$. $\square$

**The block map (SA L7071-7075, L7944-7990).** Take $L\ge3$ odd, $h=(L-1)/2$, a coarse bond $c=(y,y')$ with $y'=y+Le_\mu$, and its double block $D_c=B(y)\cup B(y')$ with an embedded rectangular lift. A configuration on $D_c$ gives an element of SU(2) to each bond with both end points in $D_c$. The pivot is $b_0=(y+he_\mu,\,y+(h+1)e_\mu)$ (SA L8169). It is the only coarse pivot among these bonds, since a coarse pivot crosses between two adjacent blocks. For $x\in B(y)$ put $x'=x+Le_\mu$. Call $x$ *axial* if its coordinates transverse to $\mu$ equal those of $y$; there are $L$ axial sites. Write $T=U[c]$, the straight transport from $y$ to $y'$. For non-axial $x$ write $X_x=U(y,x)U([x,x'])U(x',y')$, with SA's contour means, and $X_{x,\Gamma,\Gamma'}=U(\Gamma)U([x,x'])U(\Gamma')^{-1}$ for $\Gamma\in\mathcal G(y,x)$, $\Gamma'\in\mathcal G(y',x')$. SA's map has three rules:

- on ${\rm Dom}(c)=\{\varpi_c(U)<c_DL^{-2}\}$, $\varpi_c=\sup_{p\subset D_c}\|\partial U(p)-\mathbf 1\|$: $\ \mathcal M(U)(c)=\exp\big(iL^{-4}\sum_{x\in B(y)}\ell(X_xT^{-1})\big)T$;
- off ${\rm Dom}(c)$, if no $X_{x,\Gamma,\Gamma'}T^{-1}$ equals $-\mathbf 1$: the same with $\ell(X_xT^{-1})$ replaced by the mean over $(\Gamma,\Gamma')$ of $\ell(X_{x,\Gamma,\Gamma'}T^{-1})$;
- otherwise $\mathcal M(U)(c)=T$.

On ${\rm Dom}(c)$ SA uses the local analytic logarithm. Below it is applied only where $a(X_xT^{-1})\le1/2$, and there it equals $\ell$.

**Step 0 (the pivot enters only through $T$).** For axial $x$, $\mathcal G(y,x)$ and $\mathcal G(y',x')$ contain only the straight path. So $U(y,x)U([x,x'])U(x',y')$ is the straight transport from $y$ to $y'$, which is $T$, and the axial terms are $\ell(\mathbf 1)=0$ in all rules. For non-axial $x$, the paths in $\mathcal G(y,x)$ stay in $B(y)$, those in $\mathcal G(y',x')$ stay in $B(y')$, and $[x,x']$ is off the axis. The two end points of $b_0$ lie in different blocks, so none of these paths contains $b_0$. Thus $X_x$ and $X_{x,\Gamma,\Gamma'}$ do not depend on $U(b_0)$, and $T=PU(b_0)Q$, where $P$ and $Q$ are the straight transports from $y$ to the start of $b_0$ and from its end to $y'$. The map $U(b_0)\mapsto T$ is a bijection of SU(2). There are $L^4-L$ non-axial sites, so the weights $L^{-4}$ of the non-axial terms add up to $1-L^{-3}$. Hence, in the first two rules,
$$\mathcal M(U)(c)=e^{im(T)}T,\qquad m(T)=L^{-4}\sum_{x\ \text{non-axial}}\ell_x(T),\tag{G0}$$
where $\ell_x(T)$ is $\ell(X_xT^{-1})$ or the mean over $(\Gamma,\Gamma')$ of $\ell(X_{x,\Gamma,\Gamma'}T^{-1})$. Every $\|\ell_x\|<\pi$, so $\|m(T)\|<(1-L^{-3})\pi$.

**Lemma G (pivot uniqueness).** Let $R$ and $V$ be configurations on $D_c$. Suppose:

- (G1) $\varpi_c(R)\le\varpi$;
- (G2) $d(V(b),R(b))\le\eta$ at every bond $b\ne b_0$ of $D_c$;
- (G3) the target is $u=\mathcal M(R)(c)$;
- (G4) with $\varepsilon_1=C_8L\varpi+\eta$ and $\sigma=9L\varepsilon_1$: $\ \sigma\le c_1L^{-6}$, where $c_1=\min\{1/8,\,c_D/16\}$.

Here $C_8$ is the constant of SA's comb gauge (QC8). Let $V_g$ be $V$ with the value $g$ at $b_0$. Then:

- (i) $\mathcal M(V_g)(c)=u$ has exactly one solution $g\in{\rm SU}(2)$;
- (ii) at it, $V_g\in{\rm Dom}(c)$, and $g$ is the fixed point of the contraction $\Psi$ of Step 4, so it is a continuous function of $(V|_{D_c\setminus b_0},u)$;
- (iii) $d(g,R(b_0))\le C L^4\eta$, with $C$ universal.

*Proof.* **Step 1 (gauge).** SA (QC8) gives a gauge $s$ on $D_c$, built from combs of $R$, with $a(R^s(b))\le C_8L\varpi$ at every bond. All three rules are gauge covariant (SA L7073): each $X_{x,\Gamma,\Gamma'}T^{-1}$ is a loop based at $y$ and is conjugated by $s(y)$, and $\ell(sYs^{-1})=s\ell(Y)s^{-1}$. ${\rm Dom}(c)$ and the condition of the third rule are gauge invariant, and (G2) is preserved. So assume $s=\mathbf 1$. Then every bond of $R$, and every bond $b\ne b_0$ of $V$, is within $\varepsilon_1$ of $\mathbf 1$.

**Step 2 (sizes).** A path product of at most $5L$ bonds other than $b_0$ is within $5L\varepsilon_1$ of $\mathbf 1$, by the triangle inequality and invariance. A contour mean of path products of length at most $2L$ is within $4L\varepsilon_1$ of $\mathbf 1$ (SA (QC7): the mean of elements within $t$ of $\mathbf 1$ lies within $2t$). So every $X_x$ and every $X_{x,\Gamma,\Gamma'}$, for $V$ and for $R$, is within $\sigma$ of $\mathbf 1$. Also $a(P),a(Q)\le L\varepsilon_1\le\sigma$, and $a(R[c])\le L\varepsilon_1$. Since $R\in{\rm Dom}(c)$, (G0) gives $\|m_R\|\le\max_xa(X^R_xR[c]^{-1})\le2\sigma$. Hence $a(u)\le3\sigma$.

**Step 3 (every solution has $a(T)\le5L^3\sigma$).** Write $T=e^{iZ}$, $\theta=\|Z\|=a(T)$.

(a) $\theta\le\pi/2$. Each $XT^{-1}$ has $a\le\theta+\sigma<\pi$, so the third rule does not apply. On the geodesic from $XT^{-1}$ to $T^{-1}$ (length $d(X,\mathbf 1)\le\sigma$) we have $a\le\pi/2+\sigma$, so (F-b) gives $\|\ell(XT^{-1})+Z\|\le2\sigma$. If $V_g\in{\rm Dom}(c)$, the plaquettes at $b_0$ are below $c_DL^{-2}$, so $\theta\le\frac\pi2c_DL^{-2}+2\sigma$ and every $a(X_xT^{-1})\le1/2$; there SA's logarithm is $\ell$. In both remaining rules, $\|m(T)+(1-L^{-3})Z\|\le2\sigma$. Since $e^{-i(1-L^{-3})Z}e^{iZ}=e^{iL^{-3}Z}$, right invariance and (F-a) give $d(\mathcal M(V_g)(c),e^{iL^{-3}Z})\le2\sigma$. If $\mathcal M(V_g)(c)=u$, then $L^{-3}\theta=a(e^{iL^{-3}Z})\le2\sigma+a(u)\le5\sigma$.

(b) $\theta>\pi/2$. Take a plaquette $p\subset D_c$ through $b_0$, transverse direction $\nu$; its other three bonds are not pivots. Then $a(\partial V_g(p))\ge a(g)-3\varepsilon_1\ge\theta-2L\varepsilon_1-3\varepsilon_1\ge1$, so $\|\partial V_g(p)-\mathbf 1\|\ge2\sin\frac12>c_DL^{-2}$, and $V_g\notin{\rm Dom}(c)$. Under the third rule $\mathcal M=T$ and $a(T)>\pi/2>a(u)$, so there is no solution. Under the second rule, $\mathcal M=u$ means $e^{im}=uT^{-1}$, so $\theta-3\sigma\le a(uT^{-1})\le\|m\|<(1-L^{-3})\pi$. Then every point of the geodesics from $XT^{-1}$ to $T^{-1}$ has $a\le(1-L^{-3})\pi+4\sigma\le(1-\tfrac12L^{-3})\pi$, because $4\sigma\le\frac12L^{-6}$. On that set $\theta/\sin\theta\le\pi/\sin(\frac\pi2L^{-3})\le\pi L^3$, using $\sin x\ge2x/\pi$. So $\|m+(1-L^{-3})Z\|\le\pi L^3\sigma$, and as in (a), $L^{-3}\theta\le\pi L^3\sigma+3\sigma\le4L^3\sigma$ (for $L\ge3$). With $\theta>\pi/2$ this gives $\sigma>\frac\pi8L^{-6}$, against (G4). So there is no solution.

**Step 4 (existence and uniqueness).** Put $\rho=8L^3\sigma\le L^{-3}$ and $\mathcal B=\{T:a(T)\le\rho\}$. For $T\in\mathcal B$: $a(g)\le\rho+\sigma$; a plaquette through $b_0$ has $a\le\rho+2\sigma\le9c_1L^{-3}<c_DL^{-2}$; other plaquettes have $a\le4\varepsilon_1$. So $V_g\in{\rm Dom}(c)$, the first rule holds on $\mathcal B$, and every $a(X_xT^{-1})\le\rho+\sigma\le1/2$. Define $\Psi(T)=e^{-im(T)}u$. Its fixed points in $\mathcal B$ are the solutions in $\mathcal B$.

- $\Psi(\mathcal B)\subset\mathcal B$: $a(\Psi(T))\le\|m(T)\|+a(u)\le(1-L^{-3})(\rho+\sigma)+3\sigma\le\rho-L^{-3}\rho+4\sigma=\rho-4\sigma$.
- Contraction: by (F-a), $d(\Psi(T_1),\Psi(T_2))\le\|m(T_1)-m(T_2)\|$. The geodesic from $X_xT_1^{-1}$ to $X_xT_2^{-1}$ stays in the convex ball $a\le\rho+\sigma<\pi/2$, and has length $d(T_1,T_2)$. By (F-b) the constant is at most $(1-L^{-3})(1+(\rho+\sigma)^2/5)\le1-\tfrac34L^{-3}$, since $(\rho+\sigma)^2\le\frac{81}{64}L^{-6}$.

Banach's theorem gives one fixed point in $\mathcal B$. By Step 3 every solution lies in $\{a(T)\le5L^3\sigma\}\subset\mathcal B$. This proves (i). The family $\Psi$ depends continuously on $(V|_{D_c\setminus b_0},u)$ and contracts uniformly, so the fixed point is continuous; this proves (ii).

**Step 5 (iii).** $R$ satisfies the same hypotheses with the same target, and $R[c]\in\mathcal B$ solves it. So $R(b_0)$ is the solution for $R$. Two uniform contractions with constant $1-\frac34L^{-3}$ have fixed points at distance at most $\frac43L^3\sup_{\mathcal B}d(\Psi_V,\Psi_R)\le\frac43L^3\sup_{\mathcal B}\|m_V-m_R\|$. By (F-b), $\|m_V-m_R\|\le2\max_xd(X^V_x,X^R_x)$. Path products differ by at most $5L\eta$, and the contour mean is Lipschitz with a universal constant on these small balls (differentiate the contraction (QC7) of SA). So $d(T_V,T_R)\le CL^4\eta$, and $d(g,R(b_0))\le d(T_V,T_R)+d(P_V,P_R)+d(Q_V,Q_R)\le CL^4\eta$. $\square$

**Remarks.** (1) Lemma G uses SA's crude rules at L7073 in Step 3(b). Under another Borel extension of $\mathcal M$ off ${\rm Dom}(c)$, a far solution can exist; then a branch rule would have to be supplied. (2) Lemma G is what SA's sentence "the averaging constraint transports smallness" (L17346) needs at pivot bonds. By (iii), on the support the pivot fluctuation is at most $CL^4$ times the nonpivot one. SA's Lemma 2.2 (a) then needs $C(L)A_1/A_0$ small, which SA's order of constants allows ($A_1/A_0$ after $L$); this is not checked here. (3) The fixed point is SA's chart value of (QC24): both are the unique small solution.

## 2. Coordinates and the reconstruction at every coordinate

Fix a history $h$ and a step $t=k+1$ of it. A bond *of* a region is a bond with both end points in it. A test cube has side $M_2\check R_t\le L^{-2}M\check R_t$, so it is at most $L^{-2}$ of a level-$t$ cell (SA L17336). We read $\square^{\sim2}$ in SA L17317 as $\square$ with two layers of test cubes.

**(L0) Pivot-resolved coarse bonds (supplied convention).** A coarse bond $c$ of level $t$ is *pivot-resolved* at step $t$ if both blocks of $D_c$ lie in $\Omega_t(h)$. Their set is $\mathcal C_t(h)$. At every other coarse bond the delta function is read as the definition $V_t(c):=\mathcal M(V_k)(c)$, as SA L18038 reads it on stored regions. When $c$ crosses $\partial\Omega_t$, its pivot is not a bond of $\Omega_t$, and it is a raw coordinate. This corrects case 7 of `s210-3.md`, which said that a surviving delta function fixes a pivot. It defines a coarse field.

**(G-e) Edge of $\Omega_t$.** Every nonpivot bond of $\Omega_t$ within half a level-$t$ cell of $\Omega_t^c$ is a zone-F strip bond.

*Proof.* $Z_t\supset(\Omega_t^c)^{\sim2}$ (SA L17317), so $\Lambda_t\subset\Omega_t^{\sim-2}$. A test of threshold at most $\delta_k$ is a third test, a collar test or a rim test. Third tests are made on cubes $\square\subset\Omega_t^{\sim-1}$ and read $\square^{\sim2}$. Collar bonds lie within $\varpi_T\le M$ level-$k$ units of $\Lambda_t$, and rim cells touch $\Lambda_t$. So every bond that such a test reads lies within $2L^{-2}$ cell of $\Omega_t^{\sim-1}$, or within one cell of $\Lambda_t$. Both sets stay at least $(1-2L^{-2})$ cell from $\Omega_t^c$. A bond within half a cell of $\Omega_t^c$ is therefore read by no such test. It is not in $\Lambda_t$, so it is a strip bond, and (L2) puts it in zone F. $\square$

**Definition 3.1' (formula coordinates at step $t$, with ranges).**

- (F1) The raw stored fields of SA L18038: fine fields on the stored regions, where coarse fields are defined by averaging. Range SU(2); Haar measure.
- (F2) $A(b)\in B_\pi=\{A:\|A\|<\pi\}$ at each nonpivot bond $b$ of $\Omega_t$ that lies in $\Lambda_t$ or in zone K. Measure $dA$. The Haar density $\sigma_{\rm H}(A)$ is a density.
- (F3) $W'(b)\in{\rm SU}(2)$ at each strip bond of zone C or F. Haar measure.
- (F4) $V_t(c)\in{\rm SU}(2)$ at each coarse bond $c$ of $\Omega_t$. Haar measure.

There are no other coordinates. The pivot values of $\mathcal C_t(h)$ are not coordinates.

**Definition 3.2' (reconstruction).** Fix exterior data in $G^h_t$ (Section 4). Put $\eta_*=\tfrac52\delta_k$. The map $\Phi_h$ sends $\xi$ to raw fields as follows.

- On (F1) and (F4) it is the identity. At a coarse bond $c\notin\mathcal C_t(h)$ that meets $\Omega_t$, $V_t(c):=\mathcal M(V_k)(c)$; by (G-e) this reads (F1) values and zone-F values $W'V^{\rm loc}$ only.
- (F2): $V_k(b)=e^{iA(b)}V^{\rm bg}_{k,h}(b)$.
- (F3): $V_k(b)=T_{H_h(b)}(W'(b))$, as in `s210.md` (6).
- The pivot of $c\in\mathcal C_t(h)$: on $\Sigma^h_c=\{\xi:\ d(V_k(b),V^{\rm bg}_{k,h}(b))\le\eta_*$ at every bond $b\ne b_0(c)$ of $D_c\}$, $V_k(b_0(c))$ is the solution of Lemma G with $R=V^{\rm bg}_{k,h}|_{D_c}$ and $u=V_t(c)$. Off $\Sigma^h_c$, $V_k(b_0(c)):=\mathbf 1$.

The *chart of $h$ at step $t$* is $\Sigma^h_t=\bigcap_{c\in\mathcal C_t(h)}\Sigma^h_c$. Define $\Phi_{h^-}$ and $\Sigma^{h^-}_t$ in the same way. Lemma G applies on $\Sigma^h_c$ by (EX') and (S) of Section 4. So $\Phi_h$ is defined at every coordinate value, and it is Borel: (F2) and (F3) are smooth, $\Sigma^h_c$ is closed, and the pivot is continuous on it (Lemma G (ii)).

**The common chart.** Let $\Sigma^0_t$ be the set of $\xi$ with $\|A(b)\|<\delta_k$ at every (F2) bond and $r(W'(b))<2.3\,\delta_k$ at every (F3) bond, among the nonpivot bonds of the $D_c$, $c\in\mathcal C_t$. It is a condition on the coordinates alone. Where $h$ and $h^-$ have the same coordinate types, it is the same set for both.

## 3. Lemma C: the chart contains every supported branch and the fill

**Lemma C.** Assume (EX'), (M) and (S) of Section 4 at step $t$ for $h$. Let $P^h$ be the indicator product of $h$ after the drops of case 2, as a function of $\xi$ through $\Phi_h$.

- (a) $P^h\le\mathbf 1_{\Sigma^0_t}$ on every branch, that is, for every outcome of every test.
- (b) On $G^h_t$, $\Sigma^0_t\subset\Sigma^h_t$.
- (c) On $G^h_t$, $\Phi_h$ is injective on $\Sigma^h_t$. Its image contains every raw configuration of the support of $P^h$, except the Haar-null set where $V_k(V^{\rm bg})^{-1}=-\mathbf 1$ at an (F2) bond. So the raw integral of an integrand supported there equals its formula integral over $\Sigma^h_t$, with the change-of-variables density.
- (d) The same holds for $h^-$ under (EX'), (M) and (S) for $h^-$. This includes the fill at the places of $\mathfrak c$.

Hence $\mathbf 1_{\Sigma^0_t}$, $\mathbf 1_{\Sigma^h_t}$ and $\mathbf 1_{\Sigma^{h^-}_t}$ can be put into the two products, or taken out, without changing them.

*Proof.* (a) Let $b$ be a nonpivot bond of $D_c$, $c\in\mathcal C_t$; so $b$ is a bond of $\Omega_t$. There are three cases.

- $b\in\Lambda_t$. Then $b$ lies in a cube of $\Omega_t^{\sim-1}$ outside $R_t$, because $\Lambda_t\subset\Omega_t^{\sim-2}$ and $Z_t\supset R_t'^{\sim}$ (SA L17317). Its third test passed, so $\|A(b)\|<\delta_k$.
- $b$ in zone K. A passed test of threshold at most $\delta_k$ reads $b$, so $\|A(b)\|<\delta_k$.
- $b$ in zone C or F. A strip bond in $\Omega_t^{\sim-1}\setminus R_t$ lies in a cube whose third test passed, so it is in zone K. Hence $b\in S_t=(\Omega_t\setminus\Omega_t^{\sim-1})\cup R_t$, and $b$ lies in a test cube of $S_t$, since $S_t$ is a union of cells and failed cubes. The approximate test $\chi'_k$ of that cube survives (SA Lemma 2.2 (b)) and reads $b$. It passed, because $\Omega_t^c\supset Q_t'^{\sim2}$. In zone C, `s210.md` (8) and (M) turn it into $\|W'(b)V^{\rm loc}(b)Q(b)^{-1}-\mathbf 1\|<2\delta_k$. In zone F the two tested matrices are equal. With $\|V^{\rm loc}Q^{-1}-\mathbf 1\|<\delta_k/6$ from (M), and $r(X)\le1.01\|X-\mathbf 1\|$ for $\|X-\mathbf 1\|\le1/10$, we get $r(W'(b))<2.02\,\delta_k+0.17\,\delta_k<2.3\,\delta_k$.

Only passed tests of the record are used, and every history passes these. So (a) holds on every branch.

(b) On $G^h_t$, (M) gives $\|H_h\|<\delta_k/6$. At an (F2) bond, $d(V_k(b),V^{\rm bg}(b))=\|A(b)\|<\delta_k$. At an (F3) bond, $T_H(W')(V^{\rm bg})^{-1}=F_H(W')=W'e^{-i\theta(W')H}$, so the distance is $r(F_H(W'))\le r(W')+\|H\|<2.3\,\delta_k+\delta_k/6<\eta_*$.

(c) The nonpivot raw values determine $\xi$: $A=\ell(V_k(V^{\rm bg})^{-1})$, and $W'=T_H^{-1}(V_k)$ because $T_H$ is a diffeomorphism (`s210.md` 5.1). The pivots are functions of these values, so $\Phi_h$ is injective. Let $V$ be a raw configuration of the support, off the null set. It satisfies $V_t(c)=\mathcal M(V_k)(c)$ at every $c\in\mathcal C_t$. Its coordinates obey the bounds in (a), because the tests of (a) read no pivot (SA L17317). So $\xi\in\Sigma^0_t\subset\Sigma^h_t$. By Lemma G (i) each pivot of $V$ is the unique solution, so $V=\Phi_h(\xi)$. For the change of variables at one coarse bond: for targets $u'$ near $u$, $\Psi_{u'}$ is still a contraction of $\mathcal B$ (Step 4 of Lemma G, with $3\sigma$ replaced by $a(u')$). So the inverse of $T\mapsto e^{im(T)}T$ is Lipschitz near $u$, and the smooth map $g\mapsto\mathcal M(V_g)(c)$ has invertible differential at the solution. The pivot equations of different coarse bonds involve different pivots (SA L8172), so these changes of variables combine. The density is SA's coarea density (L7483-7487); it is a density, and nothing below uses its form.

(d) $h^-$ is a history, and (a)-(c) used only its own record, (EX'), (M) and (S). At the places of $\mathfrak c$, $h^-$ carries the never-large record (L4). Every bond there at level $k$ lies in $\Lambda_t(h^-)$, so the first case of (a) applies. $\square$

## 4. Theorem E': (10) on the supports, with the chart admitted

**Inputs.** (SUP), (L2.2), (LAD), (CAR) and (M) are as in `s210-3.md` Section 3. (EX) is strengthened, and one smallness is added.

- (EX') (EX), and also: at every $c\in\mathcal C_t(h)$ the background obeys its constraint, $\mathcal M(V^{\rm bg}_{k,h})(c)=V_t(c)$ (it is the constrained minimiser of SA (1b)); and $\varpi_c(V^{\rm bg}_{k,h})\le\varpi_*$ on each $D_c$ (SA L17257 bounds the background plaquettes).
- (S) $\sigma_*=9L(C_8L\varpi_*+\eta_*)\le c_1L^{-6}$. With $\varpi_*\le C\varepsilon_k$ and $\delta_k<\varepsilon_k$, this asks $\varepsilon_k\le c(L)$. That is a smallness of $\gamma$, which SA's order permits ($\gamma_0$ after $L$ and the one-step constants of $\mathcal M$, SA L9916).

$G^h_t$ is the set where (EX') and (M) hold at step $t$ for the label of $h$, and $G^h=\bigcap_tG^h_t$. Rules: (L0)-(L4).

**Theorem E'.** Under these inputs, let $m$ be a move of a retained cluster $\mathfrak r$ at step $t$, and $o$ an outcome of $m$. Then there is one set $D_{m,o}$ of formula coordinates with properties (a)-(c) of `s210-3.md` Theorem E, read with Definitions 3.1'-3.2', and also:

- (d) $P^h$ and $P^{h^-}$ vanish off the common chart $\Sigma^0_t$. On $G^h_t\cap G^{h^-}_t$, $\Sigma^0_t\subset\Sigma^h_t\cap\Sigma^{h^-}_t$. On each chart the formula integral equals the raw integral (Lemma C).

Hence (10) holds for every retained move and outcome, and the factorisation (E) of `s210-3.md` holds as an identity of functions of $\xi$.

*Proof.* The proof of `s210-3.md` Section 4 stands, with the following changes.

1. *Case 1, one addition.* A raw test can read $V_t(c)$ at a coarse bond $c\notin\mathcal C_t$ that meets $\Omega_t$. There $V_t(c)=\mathcal M(V_k)(c)$ reads (F1) values and zone-F values $W'V^{\rm loc}$ on $D_c$ (G-e). $V^{\rm loc}$ is the same function of the coordinates in $h$ and $h^-$ (case 4). So the set $D_{m,o}$ is the same.
2. *Case 2.* (L2.2) (a) uses the pivot value on the small branch (SA L17346). On the support of the remaining factors, Lemma C (a)-(c) and Lemma G (i) show that every pivot is the unique solution. So (L2.2) applies as SA states it, and the drops are exact in both histories.
3. *Case 3.* $\Phi_h$ is now defined at every coordinate. The test reads nonpivot bonds only (SA L17317), so its value at $\Phi_h(\xi)$ does not depend on the pivot values or on the convention off the chart. As before, on $G^h_t$, $D_{m,o}=\{\|A(b)\|<a_b\ \forall b\}$ or its complement.
4. *Case 6, one more object.* The pivot reconstruction exists on $\Sigma^h_t$ (Lemma G). Off $\Sigma^h_t$, both products vanish (Lemma C (a), (b)). So this failure is the same in both histories.
5. *Case 7, replaced.* A pivot value enters three things. (i) Densities: the elimination Jacobian, the Haar density and the action. Theorem E' says nothing about them. (ii) The domain: Lemma C shows that it is implied by the tests in each history, and the common indicator $\mathbf 1_{\Sigma^0_t}$ is a function of the coordinates. (iii) The old tests of case 2, which both histories drop. No retained support reads a pivot value.
6. *(b), chart reads.* $\Sigma^0_t$ reads the nonpivot coordinates of the $D_c$. Lemma C (a) reads each of them with a test within one test cube. So the chart adds no read outside the reads of the tests, and its reach $2L$ is less than one cell.
7. *(E).* As before, $P^h=\tilde P^h$ on $G^h$ by (a), and both vanish off $G^h$ by (LAD). The replaced factors are the coordinate forms of the same tests (cases 3-4), so they carry the bounds of Lemma C (a). Thus $\tilde P^h\le\mathbf 1_{\Sigma^0_t}$ as well, and (LAD) needs nothing new. Multiplying by $\mathbf 1_{\Sigma^0_t}$ changes neither product. (d) is Lemma C. $\square$

**What Theorem E' does not show.** As before, it says nothing about densities. It rests on the cited inputs; (LAD) is still an assumption about support control after replacement (check, Section 4).

## 5. Corollary K': (5) for supports and reference measures

**Corollary K'.** Assume the inputs of Theorem E'. Use the coordinates of Definition 3.1', and keep every density out of the kernel. Then each retained move has the same kernel in $h$ and $h^-$: the same support, reference measure and draw normalisers.

*Proof.* Supports: by Theorem E' (a) they agree on $G^h_t\cap G^{h^-}_t$, and off it both vanish by (LAD). By Theorem E' (d) both lie in the common chart $\Sigma^0_t$, on which $\Phi_h$ and $\Phi_{h^-}$ are both admitted parametrisations (Lemma C (c)). So the chart boundary cuts neither support. This was the failing step of the check. Reference measures: fixed products, Haar on (F1), (F3), (F4) and $dA$ on $B_\pi$ for (F2). The Haar density $\sigma_{\rm H}(A)$ and the pivot elimination density are densities. None of these reads a label. Normalisers: as in `s210-3.md` (gauge factor $\int\mathfrak G_k(V^u)du=1$, frames $|W_4|^{-1}$, and the reference law and denominator of a retained $\mathbf R$ formed from the component's own data, case 5). $\square$

So the Lemma of `s210.md` Section 3 applies to the support-and-reference layer. Proposition D (checked by Codex) still shows that the density half of (5) is false; it is carried by the gas interaction.

## 6. Lemma N': exact local pieces from a stopping nest

**Stopping regions.** A label $\ell$ is the record of a history up to step $t$. For a union $S$ of cells, $S^+$ adds one layer of cells at every level. Two labels *agree on* $S$ if they record the same regions and outcomes in every cell of $S$. A *stopping region* is a map $\ell\mapsto W(\ell)$ such that $W(\ell')=W(\ell)$ whenever $\ell'$ agrees with $\ell$ on $W(\ell)^+$. Example: let $W_0(\ell)$ be the component of $\Lambda_t^c\cap\Lambda_k$ that contains $b$. If $\ell'$ agrees with $\ell$ on $W_0(\ell)^+$, then in $\ell'$ the cells of $W_0(\ell)$ lie in $\Lambda_t^c\cap\Lambda_k$ and the cells touching it do not. So $W_0(\ell')=W_0(\ell)$. The check's example, a $W_1$ chosen by a label bit in $W_2\setminus W_1$, is not a stopping region.

**Lemma N'.** Fix a strip bond $b$ of level $k$ at step $t$, with exterior data on the support. Let $W_0\subset W_1\subset\dots\subset W_N$ be stopping regions such that:

- (N1') $W_0$ is the component above, $W_N$ is the torus, each $W_n(\ell)$ is a $\mu$-collared region of SA Theorem 6 (c) whose localised problem exists on the support, and $W_{n+1}(\ell)\subset W_n(\ell)^{+\mu_W}$ (at most $\mu_W$ layers of cells per step);
- (N2') $\|\ell(V^{(n+1)}(b)V^{(n)}(b)^{-1})\|\le\varepsilon_Ne^{-\delta_Nn}$, where $V^{(n)}(b)$ is the level-$k$ average of $U^\circ_{W_n}$ at $b$, in block axial gauge;
- (N3') ${\rm Lip}(\theta)\,h_*<1/2$, where $h_*=2\varepsilon_N/(1-e^{-\delta_N})$.

Put $H^{(n)}=\ell(V^{(n)}(b)V^{\rm loc}(b)^{-1})$. Then $H^{(0)}=0$, $H^{(N)}=H$, and $\|H^{(n)}\|\le h_*$ for every $n$. Let $F(H')=\log J_{H'}(W'(b))$ at fixed $W'(b)$. Then $F(H^{(n)})$ is defined for every $n$, $F(0)=0$, and
$$
F(H)=\sum_{n<N}t_n,\qquad t_n=F(H^{(n+1)})-F(H^{(n)}),\qquad |t_n|\le4\,{\rm Lip}(\theta)\,\varepsilon_Ne^{-\delta_Nn}.
$$
Each $t_n$ is a function of the label on $W_{n+1}^+$, of the (F1) and (F4) coordinates in $W_{n+1}$, and of $W'(b)$. If $W_{n+1}(\ell^h)^+$ meets no place of $\mathfrak c$, then $t^h_n=t^{h^-}_n$.

*Proof.* *Sizes.* $V^{(0)}=V^{\rm loc}$ and $U^\circ_{\rm torus}$ is the true background, so $H^{(0)}=0$ and $H^{(N)}=H$. By (N2') and invariance, $d(V^{(n+1)}V^{{\rm loc}\,-1},V^{(n)}V^{{\rm loc}\,-1})\le\varepsilon_Ne^{-\delta_Nn}$. Suppose $\|H^{(n)}\|\le\sum_{j<n}2\varepsilon_Ne^{-\delta_Nj}\le h_*$. Then $\|H^{(n+1)}\|=a(V^{(n+1)}V^{{\rm loc}\,-1})\le h_*+\varepsilon_N<1$, with no use of the claim for $n+1$. Both points lie in the convex ball $a\le1$, so (F-b) gives $\|H^{(n+1)}-H^{(n)}\|\le(1/\sin1)\,\varepsilon_Ne^{-\delta_Nn}\le2\varepsilon_Ne^{-\delta_Nn}$. This closes the induction.

*The function $F$.* $J_{H'}(W')=1-X_{H'}\theta(W')$, and $X_{H'}\theta(W')=d\theta_{W'}(H')$ is linear in $H'$ with $|d\theta_{W'}(H')|\le{\rm Lip}(\theta)\|H'\|$. On the ball $\|H'\|\le h_*$, (N3') gives $J\ge1-{\rm Lip}(\theta)h_*>1/2$. There $F$ is smooth, $F(0)=0$, and $\|dF\|=\|d\theta_{W'}\|/J\le2\,{\rm Lip}(\theta)$. The segment from $H^{(n)}$ to $H^{(n+1)}$ stays in the ball. The mean value theorem gives the bound on $t_n$, and the sum telescopes. (N3') also makes each strip map $F_{H^{(n)}}$ a diffeomorphism (`s210.md` 5.1).

*Locality.* $U^\circ_W$ reads only the joined sequence and the joined datum of $W$ (SA L9783): the label on $W$, the (F1) data and $V_t$ in $W$, and lifts of $V_{j_a}$ on collar bonds inside $W$. Strip coordinates are not part of the datum (`s210-3.md` (R2)). The two regions $W_n,W_{n+1}$ are fixed by the label on $W_{n+1}^+$. So $t_n$ reads what the statement says. Now let $W_{n+1}(\ell^h)^+$ meet no place of $\mathfrak c$. Then $\ell^h$ and $\ell^{h^-}$ agree on $W_{n+1}(\ell^h)^+$, so $W_{n+1}(\ell^{h^-})=W_{n+1}(\ell^h)$. Also $W_n(\ell^h)^+\subset W_{n+1}(\ell^h)^+$, so $W_n(\ell^{h^-})=W_n(\ell^h)$. In $W_{n+1}$ the coordinate types are the same, and the (F1), (F4) coordinates are shared variables; $W'(b)$ is a coordinate of $\mathfrak r$. So $U^\circ_{W_n}$ and $U^\circ_{W_{n+1}}$ are the same in both histories, and $t^h_n=t^{h^-}_n$. $\square$

**Consequence.** By (N1'), $W_{n+1}^+\subset W_0^{+((n+1)\mu_W+1)}$. So a piece whose $W_{n+1}^+$ meets $\mathfrak c$ has $n\ge(d(W_0,\mathfrak c)-1)/\mu_W-1$, in cells. These pieces go into the interaction $V_{\mathfrak X}(W_{n+1})$. Each depends on $\mathfrak X$ only through the components that meet $W_{n+1}^+$, and each is bounded by $4\,{\rm Lip}(\theta)\varepsilon_Ne^{-\delta_Nn}$. The decay is in $d(W_0,\mathfrak c)$, where $W_0$ is the strip component of $\mathfrak r$. `s210-3.md` wrote $d(b,\mathfrak c)$; that needs a bounded $W_0$. The same argument applies to any density of the step that is a $C^1$ function of the true background at finitely many bonds near $b$, under the analogue of (N3').

**Status of the hypotheses.** (N1') asks for a stopping nest of $\mu$-collared regions. Its existence is not proved here. The collar condition of SA Theorem 6 (c) (each collar in one layer of the sequence) forces the nest to follow the label, and the repo's Definition A localisation is a candidate. (N2') is SA Theorem 6 (c) for the nested pair $(W_n,W_{n+1})$. SA states it up to a gauge $w$. The block axial representative is canonical (SA Theorem 6 (b)), but the transfer of the bound to it is not proved here. (N3') is the condition the check named. A cut-off that rises over $[\frac43\delta,\frac53\delta]$ can be chosen with ${\rm Lip}(\theta)\le4/\delta_k$. Then (N3') holds if $h_*<\delta_k/8$. SA's strip bound $|H|\le C\varepsilon_ke^{-\check R_k}$ (L17518) suggests that $\varepsilon_N$ carries the factor $e^{-\check R_k}$, but (N3') is not derived here.

## 7. Proposition P, repaired

**P(c).** In one class component $X$, the outcome of the operation $\mathbf R$ of level $j$ has a fate and, for a drop-out, a failure location (SA L17585-17614). The values are:

- healed; island (only the last test $\chi_j$ fails);
- drop-out at the tests before stage $n+1$, one value for each $0\le n<\mathsf N_j$;
- drop-out at the extension test (2);
- drop-out at the test on $B$ (factor $1-\chi_B$);
- drop-out at the last-shell test (factor $\chi_B(1-\chi_{\rm last})$);
- drop-out because a reference normaliser is not in $(0,\infty)$ (SA L17499 says this does not occur on the supports; it is counted anyway).

Each stage is a decomposition of unity component by component (SA L17410), so a stage gives one value. There are at most $\mathsf N_j+6$ values. The location fixes the factor that the record carries, so the code decodes injectively; this was the check's failing step. The frame $r\in W_4$ is recorded with weight $|W_4|^{-1}$, and these weights add up to $1$. So the frame-weighted number of $\mathbf R$-records of one component is at most $\mathsf N_j+6\le e^{(M\check R_j)^4}$: put $x=M\check R_j\ge2$; then $\mathsf N_j=\check R_j\le x$ and $x+6\le x^4\le e^{x^4}$. This replaces $\mathsf N_j+3$ in the proof of `s210-3.md`. The rest of that proof, and $b=8c_TL^4\log2+1$, are unchanged.

**The read closure.** The first sentence of Proposition P now has a proof. Theorem E' (b) bounds the reach of every retained support read by one cell. The chart reads lie inside the test reads (Theorem E', item 6). The pivot reconstruction reads $D_c$, and this matters only for densities. The fill reads what the never-large tests at the places of $\mathfrak c$ read (Lemma C (d)), within one cell. So every support read of a move of $\mathfrak c$, and every read of its fill in $h^-$, lies in $\widehat A(\mathfrak c)$. With P(a) and P(b) (checked by Codex) and P(c) above, (3) holds for the support layer with $J=81$, and `s210.md` (4) applies.

## 8. Where it stops

The repairs leave the stop of `s210-3.md` Section 7 in place. The first input that fails is still (LOC): every formed term and every correction $V_{\mathfrak X}(Y)$ must be label-local through later steps and $\mathbf R$ stages (SA L17541-17558, L17964). Lemma N' gives the formation step of the strip densities, under (N1')-(N3'). After (LOC), the mass bound (8.1) and the order of rates (item 3 there) are still open. (Act) of `sa-2.13.md` and hypothesis 3 there wait on (LOC).

## Result

- **Proved by Claude, not yet checked by the other model.**
  - Lemma G: on a double block whose nonpivot bonds are near a regular background, SA's averaging constraint has exactly one pivot solution in all of SU(2). It lies in ${\rm Dom}(c)$ and depends continuously on the data, with an explicit condition $9L(C_8L\varpi+\eta)\le c_1L^{-6}$. Step 3 (b) uses SA's crude rules off ${\rm Dom}(c)$ (L7073).
  - Definitions 3.1'-3.2' with (L0) and (G-e): the reconstruction $\Phi_h$ is defined at every coordinate, with the chart $\Sigma^h_t$ and the common chart $\Sigma^0_t$.
  - Lemma C: both histories' products, on every branch and on the fill, vanish off $\Sigma^0_t$; $\Sigma^0_t$ lies in both charts; raw and formula integrals agree there.
  - Theorem E' and Corollary K', as implications from (SUP), (L2.2), (EX'), (M), (S), (LAD), (CAR) and rules (L0)-(L4). They repair the check's failing steps: case 3, the undefined pivot (case 6), case 7, (E), and K's "the supports agree".
  - Lemma N' under (N1')-(N3'): the stopping nest repairs the label-local family, and (N3') repairs the $\log J$ example.
  - P(c) with a failure-location symbol ($b$ unchanged), and P's read closure.
- **Open.** (LOC) is still the first input that fails. Also open: the existence of a stopping nest (N1'); the common-gauge comparison (N2'); (N3') against SA's constants; the cited inputs, including (LAD) as an assumption; the mass bound (8.1); and the order of rates.
- **Note for the lead (FINISH, How we work, item 6).** SA's prescription "$V_k$ is given the value that solves ... the averaging constraint" (L17344, L17521) and its Lemma 2.2 (a) assume that this solution is unique and small. SA's chart (QC24) is only local. Lemma G proves uniqueness on the support from SA's own block map. This is a proof of a step that the outline assumes, not an error in it. It needs the other model's check before any use outside this repository.
