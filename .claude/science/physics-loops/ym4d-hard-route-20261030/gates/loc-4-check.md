lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-05T05:31Z

# loc-4-check — queue row 235

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; checkout `1ad946eb7`; Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder ("SA L" numbers refer to it). One reading by one other model, not an audit; it grants no status. Every step was redone by hand. No computation enters any verdict.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for (R9)–(R12) and the bracket method (SA L5762–5861, L17904–17918). Codex wrote `library/loc-4.md`. Balaban for the background-localisation method.

## Verdicts

Sections 3–7 checked line by line by Claude, first failing step none. Each verdict is for an implication from the inputs that the note names.

| § | Statement | Verdict |
|---|---|---|
| 3 | Proposition O, geometry only: one first admission index, (a), (b) | ADVANCE |
| 4 | (1): Theorem A's inner curves lie in \(\mathcal U^H_j(X;\alpha_{0,j},\alpha_{1,j},\alpha_{0,j})\) at every Boolean corner, margin 1/5 | ADVANCE |
| 4 | (2): single-layer outer shifts \(P\dotplus\nu(\mathbf H_s,\mathsf j_s)\) lie in \(\mathcal U^H_j(X;a_0,a_1,a_0)\) for \(\lvert\nu\rvert<ca_0/b\) | ADVANCE |
| 4 | Hölder conversion; "(2) gives (R11)" if \(b\le Ce^{C\bar\kappa}L^{-(k-j)}\delta(\theta_k)\) | ADVANCE, conditional as stated |
| 5 | Scalar counterexample (3): one-move room does not iterate to (D4) | ADVANCE |
| 5 | Sufficiency of the budget (4) | ADVANCE |
| 6 | Corrected Lemma M: identity, read sets, vanishing, bound (5) | ADVANCE |
| 7 | Corrected Theorem W: exact (LOC) from (D1)–(D3), (SUP), splitting and (D4) at every move | ADVANCE |

No defect breaks a consumer. Five precisions are listed after the evidence; none changes a verdict.

## Evidence

**§3.** \(\operatorname{int}W_n\) increases with \(n\). Lemma S (passed in `gates/loc-3-check.md` §1) makes each \(W_n\) contain \(S\) in its interior or miss it there. \(S\subset\operatorname{int}\Omega_0=\operatorname{int}W_N\) by separation. So the first admission index exists, is unique, and is at least 1. (a): enlargements compose, so \(S\subset W_{n_S+1}\subset W_0^{+(n_S+1)\mu_W}\). (b): \(S\) misses \(\operatorname{int}W_{n_S}\), so it lies in \(\overline{W_{n_S}^c}\); distance to a set equals distance to its closure. The disclaimers are correct: no response lower bound, no refutation of (N2′), no joint history.

**§4 (1).** Inputs: `wf-c.md` Theorem A (checked by Codex, `b4-step.md` §0), Theorem I with the repairs of `gates/o1-decoupled-gate.md` §4.5, Lemma 5 and (A2-H) (ADVANCE in `gates/bx-fix-check.md`).
- (A1) puts every input clause at most 5/8 of its radius. Lemma E and the gauge ceiling \(e^{C_g\sup|B|}\le9/8\) give the coefficient \((9/8)^2(5/8)=405/512\). The envelope \(\bar a=\max(a,\alpha_0^{\rm input})\) does not change it, since (A1) bounds both radii by \((5/8)\alpha_{0,\ell}\).
- Age 0: \(405/512<4/5\), because \((4/5)\cdot512=409.6\).
- Age \(m\ge1\): the repaired floor gives \(\alpha_{0,\ell}/\alpha_{0,j}\le(1+m)^{1/2}\). With \(L\ge3\), \((1+m)^{1/2}L^{-2m}\le\sqrt2/9\), so the coefficient is below \(1/8\). Theorem A's unrepaired factor \(2(1+m)^{1/2}\) still gives about \(0.249<1/2\).
- Theorem I transfers the bound to every \(Z\subset X\), \(p\le j\), \(n\le p\) and both rules; the real factor is \(\mathbf1\).
- (H): for \(U=\mathbf1\), take \(g=\mathbf1\), \(A_r=0\), so \(A''=\mathcal H(B)\). Lemma 5 gives \([\nabla\mathcal H(B)]_{\alpha_H}\le C_{\mathcal H\mathrm H}\sup|B|\). With \(C_{\mathcal H}\to\max(C_{\mathcal H},C_{\mathcal H\mathrm H})\) in the potential ceiling, this is below \(\alpha_{1,j}/2\). The change costs only a larger \(C_\alpha\), chosen after \(M\) and before \(c_A\), so the order of constants survives.
- Theorem A covers all \(|s_\Delta|<e^{\bar\kappa}\), hence every Boolean corner.

**§4 (2).** This is `wf-room.md` §3, (3.2), plus the Hölder clauses. I redid both. Lemma T (`a3-close.md` §2) is read as cited. It has not been checked by the other model: `gates/a3-close-meet-gate.md` excludes that section, as the note says.
- \(P\dotplus(\mathbf H,\mathsf j)=(U,A'\boxplus\mathbf H,\mathbf J+\mathsf j)\) (SA L5751–5759). So \(U\), its gauges and its towers do not change. (3.4)–(3.5) bound the field changes by \(C|\nu|b\). On \(|\nu|<R=da_0/b\) the fields meet radii \((2a_0,2a_1)\), using \(a_0\le a_1\).
- Lemma T at radii \((2a_0,2a_1)\) needs \(2a_0+2a_1\le c_T/2\), a small-radius choice. It gives \(K^\sharp(2a_0+4a_1^2)\le Aa_0\). The unit change to level \(p\) multiplies the bound by \(L^{-2(j-p)}\) and the clause radius by \(L^{-(j-p)}\), so the normalised bound only improves. \(\nu\mapsto A'\boxplus\nu\mathbf H_s\) is holomorphic and stays in Lemma T (a)'s ball.
- Schwarz's lemma on \(\ell(f(\nu)-f(0))\), \(\|\ell\|=1\), gives \((A+1/2)a_0|\nu|/R\). With \(c<d/[4(A+1/2)]\), each tower quantity stays below \(3a_0/4\). Each clause is fixed separately, so no sum over towers enters. The current: \(|\mathbf J+\nu\mathsf j_s|<a_0/2+ca_0<3a_0/4\) for \(c<1/4\).
- Hölder clause. In the witnessing gauge, \(\operatorname{Ad}(g^{-1})(A'\boxplus h)=A''\boxplus h''\), because bondwise BCH commutes with conjugation. On cubes of side \(C_{\rm box}LM\), \(\nabla(fg)=(\nabla f)(\tau g)+f\nabla g\) and \([g]_\alpha\le2\,{\rm diam}^{1-\alpha}\|\nabla g\|_\infty\). So \(C^{1,\alpha_H}\) is a Banach algebra with a constant that does not depend on the mesh. The remainder \(G_\eta(p,v)\) vanishes at \(p=0\). The \(C^{1,\alpha}\) size of \(A''\) is small: \(|A''|=|A'|\) and \(|\nabla A''|\le|\nabla_UA'|+C|A_r||A'|\). So \([\nabla A''_{\rm new}]_\alpha<a_1/2+Cca_0<3a_1/4\).
- Conversion: \(\nabla^{\mathbf U}h=\nabla h+K\,h(\cdot+\eta e_\mu)\), with \(K=i\operatorname{ad}(w)+O(\eta|w|^2)\) bounded in \(C^{\alpha_H}\), uniformly in \(\eta\). Straight transports over length \(s\le\xi_y\) differ from 1 by at most \(Cs\sup|w|\). With Lemma 0 and Proposition PH (ADVANCE in `gates/bx-fix-check.md`), the ordinary bound \(\epsilon\le C|\nu|B\|B'\|\) follows.
- (R11): \(\varrho=ca_0/b\ge(c/C)L^{k-j}a_{0,j}\delta(\theta_k)^{-1}e^{-C\bar\kappa}\), which is (R11) with \(c_F=c/C\), \(C_F=C\).

**§5.**
- Arithmetic: \(|z\pm\nu s/N|<1/2+2R/N<3/4\), since \(N>8R\). The physical path is \(0,1/N,0,\dots\), inside the half disc. At the corner with plus parameters 1 and minus parameters 0, the sum is \(N\cdot(1/N)=1\notin D\).
- No extension: \(G^2=1-z\) near 1 forces \(G(1)=0\) and \(2G(1)G'(1)=-1\).
- No cancellation: the displacement \((|I_+|-|I_-|)/N\) equals 1 only at that corner. Every other corner value lies in \([-1,1-1/N]\), where \(\sqrt{1-z}\) is holomorphic. So the bracket, as a function of a translation \(w\), is \(\pm\sqrt{-w}\) plus a holomorphic function.
- Relevance: the actual carriage evaluates such mixed corners. At move \(m+1\), a piece \(e_K\) of move \(m\) is read at \(Q_m(\mathbf1_{I\cup\mathcal A},1;Q_{m+1}(s,\nu;P))\), with Boolean corners at every earlier move. The example keeps this structure and replaces the response by a scalar shift. It is not a Yang–Mills counterexample, as the note says. It violates (4): the increments sum to \(2N\cdot2R/N=4R>1\).
- (4): telescoping gives \(\|\mathcal R_a(Q_m)\|<(1-\epsilon_a)r_a+\epsilon_ar_a\) for every prefix and every parameter choice.

**§6.**
- Identity: \(\sum_{K\subset\mathcal C}e_K=\sum_{I\subset\mathcal C}E(\mathbf1_{I\cup\mathcal A},1)(1-1)^{|\mathcal C\setminus I|}=E(\mathbf1,1)\). (D1) gives \(Q(\mathbf1,1;P)=P^{\rm old}\), up to the recorded node gauge that (D4) must carry.
- Vanishing: let \(\Delta\in K\) lie in a wall-component of \(K\cup\mathcal A\) that misses \(\mathcal A\). Then \(\Delta\) is not wall-adjacent to any \(\mathcal A\)-meeting component of \(I\cup\mathcal A\), for \(I\subset K\setminus\{\Delta\}\). So those components agree with and without \(\Delta\). Splitting keeps the response on them, and \(F\) reads only inside them (\(X^{+r}\subset\operatorname{int}\bigcup\mathcal A\), collars included). The terms cancel in pairs. With no datum on the \(\mathcal A\)-read components, \(E=0\) at every corner, so \(e_K=0\), including \(K=\varnothing\).
- Bound: \(E(s,0)=0\) because \(P\dotplus0=P\). \(|E|\le2M_F\) because \(\rho_XP\) is the \(\nu=0\) point of (D4). Schwarz's lemma gives \(|E(s,1)|\le2M_F/\varrho_F\). Then \(g(1)-g(0)=(2\pi i)^{-1}\oint g(z)\,dz/[z(z-1)]\) on \(|z|=R'\), with kernel at most \(1/[R'(R'-1)]\) on length \(2\pi R'\). Iterate over \(K\), with parameters fixed at 1 on \(\mathcal A\) and 0 on \(\mathcal C\setminus K\). This gives (5), with the \(\varrho_F^{-1}\) gain also for \(K=\varnothing\). This is SA L5856–5859, and SA L5860–5861 says the bracket bound "is proved once the response and inclusion hypotheses have been supplied".

**§7.** The induction is `loc-3.md` Theorem W with the missing premise of `gates/loc-3-check.md` §6 added. That check accepted the preservation steps "once the common local families and their evaluations exist". (D4) supplies the evaluations and Lemma M the local families. The carried pieces of the next move are the \(e_K\) and \(F\circ\rho_X\). Their domains are the sets where every corner argument lies in \(D_F\). So "(D4) at every move" is admission of every nested composition \(Q_m(c_m;Q_{m+1}(c_{m+1};\dots Q_M(s,\nu;P)))\), which is the all-history assertion that rows 236–248 attack. The window form of (b) is weaker than `loc-3.md`'s "inside \(Y\)". Moving the absorption of components to a separate bound is correct.

## Precisions (none changes a verdict)

1. **§5 heading.** It says (D4) "is necessary". The text proves that (D4) does not follow from one-move room. Only the Boolean-corner part of (D4) (\(\nu=1\), \(s\in\{0,1\}^{\mathcal P}\)) is necessary for the \(e_K\) to be defined. The complex room is what bound (5) uses. No consumer reads necessity.
2. **§6 hypotheses.** The list names (D4), splitting and (D2), but the identity uses (D1)'s physical identification. Add (D1); Theorem W already lists it.
3. **§5, order inside (4).** The telescoping needs each \(\mathcal R_a\) defined at every prefix. The clauses that define the charts (small logarithm branch, Lemma T (a)'s continuation ball) are globally defined functionals of the pair. Put them first in the budget; the dependent clauses are then defined. The note's sentence on chart room says this. Row 240 found that (R22) assigns no room to the (R5) continuation domain, which is consistent.
4. **§7, measures.** "Integrals over common measures preserve equality on equal traces" holds for measures that are local. A move's fluctuation measure depends on the background outside a piece's domain. So the step reads (D3)'s regional Gaussian decomposition (`library/regional-gauss.md`, row 233). The Result already lists regional existence as a further input.
5. **Scope.** In (1), Theorem A's complex parameter multiplies the window cutoff \(\zeta\). So (1) admits the box-first window curves, not an (R10) interpolation, and the note claims no more. In (3), the corner with only minus parameters on gives \(z=-1\), also outside \(D\). \(F\) extends there, so (3) is unaffected.

## What this means for the queue

- `loc-4.md` passes. Its corrections to `loc-3.md` stand: Proposition O is geometry only; Lemma M and Theorem W hold given (D4); one-move room does not give (D4); the budget (4) suffices.
- Rows 236, 240, 245, 247 and 248 build on (D4) and (4). Nothing here changes their statements.
- (LOC) stays open at (D4) for the actual carried compositions on every history and stage, and at regional Gaussian existence for (D3). §4 (2) also reads Lemma T, which is not yet checked by the other model.
- Kind: check of our own text. No candidate contribution to Sussman–Alpoge: the outline states (R10)'s inclusion as a hypothesis (SA L5813–5824) and proves the bracket under it (SA L5826–5861).
