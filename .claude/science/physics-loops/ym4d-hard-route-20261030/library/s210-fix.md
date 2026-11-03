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
