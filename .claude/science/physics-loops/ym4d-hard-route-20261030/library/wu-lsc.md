lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-08T16:58Z

# The last-scale constants: a proof of Lemma 6.3:lem-last-scale-constants of the complete account, with a normalization correction

Draft for the owner's review (queue row 352, `wu-lsc`). It is not sent anywhere. Research text: it grants no status and makes no public claim.

**Provenance.** Claude Opus 5.5 (max effort), Mac mini worker, checkout `26443a02d`. This is a write-up of checked texts. It adds no new mathematics. Its sources are: the proof `library/lsc.md` (Codex, two rounds, frozen 2026-11-05); its round-1 check `gates/lsc-gate.md` (Claude, smaller scope); the normalization check `gates/nrm-check.md` (Codex, checked line by line by Codex); and the round-2 check `gates/lsc2-gate.md` (Claude, first failing step none). The scope limits of §9 also come from `gates/lsc-uses-check.md` (Claude) and `gates/lsc-value.md` (Codex). The outward note `library/out-lsc.md` (Codex; checked for faithfulness by Claude in `gates/out-lsc-check.md`) went to the authors as their issue #16 on 2026-11-07. This draft keeps that note's marking of printed and added parts, and its correction F3 on the symbol $B_\sharp$. The presentation changes are listed in §9, item 8. **This write-up has not been checked by the other model.**

**Sources.** CA-I, CA-II, CA-III are `theorem_0_complete_account_raw_{I,II,III}.tex`; SA is `YM4_sketch_500.tex`. All are at commit `31a47c543775`, fetched by URL for this note. Numbers are TeX source lines. Status words are the ones the account declares, in its convention at CA-I 27–46: a statement with no status sentence "is proved in full", and "a statement proved from other named statements lists them … as its explicit hypotheses". Every passage quoted below was read in a bounded excerpt.

**Credit.** The lemma, its setting and notation, and the printed proofs of its parts (b)–(e) (CA-II 63369–63833) are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. So are the floor mechanism (CA-II 109918–109975; SA 23504–23527), the vacuum-energy theorem and density constants of CA-I 4.36, and the convention $e^{-E}Z$ (CA-II 140916–140926; SA 23405–23415, 23515–23527). **Tadeusz Bałaban** is credited for the renormalization-group construction the account uses: the real-background theorem (CMP 102, Theorem 1), the bounds of CMP 119, and the tree estimate CMP 116 (1.26). The proof of the parts the account leaves open was written by Codex (`library/lsc.md`): the offset argument for (a), the explicit constants on one coupling window, and the completion under the original floor of clause (iii-b). The normalization correction is Codex's (`gates/nrm-check.md`); a Claude check first raised the conflict (`gates/lsc-gate.md`). Claude checked the proof line by line.

## 1. The statement in their account, and its status there

**The label.** At CA-II 63365–63367 the account prints only a remark:

> \begin{remark}\label{6.3:lem-last-scale-constants}
> The statement of this lemma is not written out here; parts of its proof are printed below.

**What is printed.** Part (b), the admissible data and the last-scale coupling (CA-II 63369–63526), with the remark on what it relies on (63528–63565). Part (c), the per-ball bound across unit rescalings (63568–63689). Part (d), the local plaquette count (63691–63798). Part (e), bare couplings tending to zero (63800–63833). The corollary `6.3:cor-volume-free-constant` follows (63836–63899).

**What is not printed.** Part (a) is cited by the proof of (b): "Let $a:=K_J-K$, which lies in $\mathcal A$ by part (a)" (63371–63372). Part (d) cites "the inequality $K\le K_J$ … derived from hypotheses (I1), (I2) and (I3) of that lemma" (63700–63701). Neither part (a) nor (I1)–(I3) appears anywhere. The proof of (b) also takes the size of the last-scale constants from the correlation theorem, as a clause (63399–63410):
\[
E_+^\sharp+C_{\rm low}\le E_J(L,\mathfrak p,\varrho;g,m)
\qquad\text{(6.3:eq-last-scale-coupling-a)},
\]
with $E_J$ "a function of the displayed arguments only". The correlation theorem (CA-II 2791–2966) says only that $E_+^\sharp$ and $C_{\rm low}$ "are constants fixed in the treatment of the last lattice" (2949–2950). Its torus-bound proof takes the lower bound as hypothesis 8, "The floor for the unsourced integral at the level $K'$" (59677), and uses it at 59815–59819. So the open content of the lemma is: part (a), a proof of the floor, and constants $E_+^\sharp$, $C_{\rm low}$ whose sum obeys (6.3:eq-last-scale-coupling-a) at $m=m^J_{\mathbb T}(g)$.

**Status.** CA-III 110895–110899 lists the inputs of the per-ball volume-free bound and ends: "the uniformity of the last-scale constants in the torus exponent. The last of these is of status 'stated; proof incomplete'." CA-II 64603 says instead: "Statements of this book whose proofs are incomplete or outstanding: none." The two declarations conflict. We follow the first: it names this lemma, and the statement is in fact not written.

**Why it matters for their main theorem.** Clause (iii-b) of Theorem 0, the per-ball volume-free bound (CA-I 2610–2620), rests on it (CA-III 110895–110899). Clause (ii), the limits on each torus and on $\mathbb R^4$, appeals to it by statement (CA-II 68362–68365). Four places read it directly: CA-II 63531–63565 (`6.3:rem-exponent-statements`), 63907–63946 (the corollary and `6.3:rem-per-ball-reading`), 64157–64283 (the proof of `6.4:thm-per-ball-bound`), and 68362–68368.

**What this note proves.** Lemma 6.3 as those four uses read it (§3), as an implication from inputs the account states; §8 gives the status of each. On the way it corrects one application in CA-I: 4.33 (h4)(a) does not hold for the bare density of Definitions 1.1 and 1.5 (§2). The correction uses the account's own vacuum-normalized convention.

## 2. The normalization: what is wrong, and the correction

**2.1 The conflict.** Definition 1.1 sets "The *bare density* is $\rho_0(U):=\exp[-g_0^{-2}A(U)]$" (CA-I 477–481). Definition 1.5 sets $\rho_k=(\mathbf R\mathbf T)^k\rho_0$, "where $\rho_0$ is the bare density of Definition 1.1" (CA-I 924–933). In 4.33:thm-stability, $E_k[\mathcal S]$ is "the additive constant of the term $\tau_{\mathcal S}$" of $\rho_k$ (CA-I 157011), and hypothesis (h4)(a) reads (CA-I 157039–157041):
\[
-E_k[\mathcal S_\emptyset]=\mathfrak l_k-\mathfrak r_k,\qquad \mathfrak l_k\ge0,\qquad |\mathfrak r_k|\le C_{\mathfrak r}N_k .
\]
(h4) says "The vacuum-energy theorem applies". That theorem, 4.36:thm-never-large-exponent, defines its energies from an initial constant (`4.36:eq-label-energy-a`, CA-I 159153–159160):
\[
E:=\sum_{j=0}^{K-1}E^{(j)}(T,T),\qquad E_k[\mathcal S]:=E-\sum_{j=0}^{k-1}E^{(j)}(\Omega_{j+1},\Lambda_{j+1}),
\]
and its hypothesis (h1) asks for a density "with the energy constant (4.36:eq-label-energy-a)" (CA-I 159298–159300). Its part (a) (CA-I 159321–159336) gives $\mathfrak E_k:=E_k[\emptyset]=\sum_{j=k}^{K-1}E^{(j)}(T,T)=-\mathfrak l_k+\mathfrak r_k$ with $|\mathfrak r_k|\le C_{\mathfrak r}|T|_k$.

Write $E_{\rm vac}$ for this $E$. The bare density of Definitions 1.1 and 1.5 starts from the constant $0$, not $E_{\rm vac}$. So the constant of its never-large term is $E^{\rm bare}_k[\mathcal S_\emptyset]=E_k[\mathcal S_\emptyset]-E_{\rm vac}$, and
\[
-E^{\rm bare}_k[\mathcal S_\emptyset]=E_{\rm vac}+\mathfrak l_k-\mathfrak r_k. \tag{2.1}
\]
The term $E_{\rm vac}$ is the one (h4)(a) omits for the bare density.

**2.2 The omission changes the conclusion.** Two arguments show it. The first uses the account's one-step inputs; the second uses none.

*(i) One step.* At $SU(2)$, $d=4$, the one-step energy of the never-large pair is (`4.36:eq-never-large-exponent-2`, `-3`, CA-I 159416–159428)
\[
E^{(j)}(T,T)=-\tfrac92(L^4-1)\log x_j\,|T|_{j+1}+r_j,\qquad |r_j|\le D_0|T|_{j+1},\quad D_0:=(L^4-1)c^\sharp_G+K_*(E_0+1).
\]
At $k=1$ the bare constant is $E^{\rm bare}_1[\mathcal S_\emptyset]=-E^{(0)}(T,T)\ge[\tfrac92(L^4-1)\log x_0-D_0]\,|T|_1$. The bare reading of (h4)(a) gives $E^{\rm bare}_1[\mathcal S_\emptyset]=-\mathfrak l_1+\mathfrak r_1\le C_{\mathfrak r}|T|_1$. The constants $D_0$, $C_{\mathfrak r}$ depend only on $L$, $N$, $\mathfrak p$, while $x_0=g_0^{-2}$ is unbounded on $0<g_0\le g_-(g)$. So the two cannot both hold once $\log x_0>(D_0+C_{\mathfrak r})/[\tfrac92(L^4-1)]$.

*(ii) The bare floor is false.* Read for the bare density, 4.33 (i-b)(1) and (i-c), with the ball integration of §5, would give $Z(0)=\int\rho_0\,dU\ge e^{-C^*_{\rm low}(g)N^4}$ at fixed $g$, for every $g_0$ in Case A. The following exact bound contradicts this.

**Proposition 2.2 (axial-gauge bound).** On the periodic lattice of integer side $T\ge3$, with $a(W)=1-\operatorname{Re}\operatorname{tr}W$, $\operatorname{tr}\mathbb 1=1$, and normalized Haar measure,
\[
\log\int e^{-x_0A(U)}\,dU\ \le\ -\tfrac92(1-T^{-1})T^4\log x_0+3(1-T^{-1})T^4\log C_H,\qquad C_H=(\pi/2)^{5/2}. \tag{2.2}
\]

*Proof.* Write sites as $(y,t)$, $y\in(\mathbb Z/T)^3$, $0\le t<T$. Put $h(y,0)=1$ and $h(y,t+1)=h(y,t)U_4(y,t)$ for $t\le T-2$. Change the temporal variables of each $y$, one after another, to $h(y,1),\dots,h(y,T-1)$ and $P(y):=h(y,T-1)U_4(y,T-1)$. Then, at fixed temporal variables, change each spatial bond to $W_i(y,t):=h(y,t)U_i(y,t)h(y+e_i,t)^{-1}$. Each change is a left or right multiplication by an element already fixed, so it preserves product Haar probability measure. The action is gauge invariant. In the new variables the $(i,4)$ plaquette at $(y,t)$, $t\le T-2$, has holonomy $W_i(y,t)W_i(y,t+1)^{-1}$. Every $a(\cdot)\ge0$ (CA-I 456–460), so dropping all spatial plaquettes and all temporal plaquettes at $t=T-1$ does not decrease the integrand. The remaining integrand does not depend on $h$ or $P$, whose integrals are one. For each of the $3T^3$ pairs $(i,y)$ there remains a chain $\int\prod_{t<T}dW_t\prod_{t\le T-2}e^{-x_0a(W_tW_{t+1}^{-1})}$. Integrate $W_0,W_1,\dots,W_{T-2}$ in turn: by invariance each gives $c(x_0):=\int e^{-x_0a(W)}dW$, and the last integral is one. Hence the left side of (2.2) is at most $3T^3(T-1)\log c(x_0)$.
For $W$ with eigenvalues $e^{\pm i\theta}$, $a(W)=1-\cos\theta=2\sin^2(\theta/2)\ge2\theta^2/\pi^2$ on $[0,\pi]$, by concavity of sine on $[0,\pi/2]$. Normalized Haar measure has density $\tfrac2\pi\sin^2\theta\,d\theta$ in $\theta\in[0,\pi]$, and $\sin^2\theta\le\theta^2$. So
$c(x)\le\tfrac2\pi\int_0^\infty\theta^2e^{-2x\theta^2/\pi^2}d\theta=C_Hx^{-3/2}$, using $\int_0^\infty u^2e^{-u^2}du=\sqrt\pi/4$ (integration by parts from $\int_{\mathbb R}e^{-u^2}du=\sqrt\pi$). Insert this. $\square$

In Case A with $K'\ge1$ the bare side is $T=L^{K'}N\ge LN$, so (2.2) gives $\log Z(0)\le-L^4N^4[\tfrac94\log x_0-3\log C_H]$ once $\tfrac32\log x_0>\log C_H$. At fixed $g$, $C^*_{\rm low}(g)$ is a fixed number, while $x_0\to\infty$ and $K'\to\infty$ as $g_0\downarrow0$ (part (a) and $K\to\infty$). So the bare floor fails for all small $g_0$. A version uniform in $K'\ge1$ is in `gates/nrm-check.md`, (12)–(14).

**2.3 The correction.** Put
\[
\widehat\rho_0:=e^{-x_0A-E_{\rm vac}},\qquad \widehat\rho_k:=e^{-E_{\rm vac}}\rho_k,\qquad \widehat Z(w):=e^{-E_{\rm vac}}Z(w), \tag{2.3}
\]
with $Z(w)$ the bare partition function of Chapter 6 (`6.3:not-joint-cumulants`). Every exact operation of the recursion commutes with multiplication by the positive number $e^{-E_{\rm vac}}$. The block push-forward is linear. The creating step is an exact finite decomposition of unity (h11). On a component, $\mathbf R$ replaces $\tau$ by $m_\tau\mathfrak s$, with $m_{c\tau}=c\,m_\tau$ and $\mathfrak s$ a probability law (h8). The integral identities (h7), (h9), (h10) are linear. Hence $\widehat\rho_k=(\mathbf R\mathbf T)^k\widehat\rho_0$; the constant of its never-large term is $E_k[\mathcal S_\emptyset]=\mathfrak E_k$ of 4.36; (h4)(a) holds for $\widehat\rho_k$ by 4.36 (a); and (i-c) reads $\int\widehat\rho_k\,dV_k=\widehat Z(0)$ for $k\le K$. The proof of 4.33 (i-b)(1) (CA-I 157114–157129) then applies unchanged and gives
\[
\chi_k\,e^{-x_kA(U_k)-E_-N_k}\,dV_k\ \le\ \widehat\rho_k\,dV_k,\qquad E_-=C_E+C_{\mathfrak r}, \tag{2.4}
\]
with $C_E=E_1^\sharp(1-L^{-\beta_T})^{-1}+1$ of (h2). This is also 4.36:cor-density-constants (1) (CA-I 159530–159537, proof 159571–159593), whose proof feeds only $\mathfrak E_k\le C_{\mathfrak r}|T|_k$ into the lower-bound lemma. In bare variables, (2.4) carries the factor $e^{E_{\rm vac}}$ on its left side.

The account already uses this convention. CA-II 140880–140886 defines a bare $Z_m$ ("no normalising constant is included"). CA-II 140916–140926 writes $\widetilde Z_m(v)=e^{-E_m-\mathcal E_m(v)}Z_m(v)$ with $E_m=\sum_{j<K}E^{(j)}_{\rm vac}(\mathbb T_m,\mathbb T_m)$, and calls $\exp[-x_0A(U)-E_m]$ "the density $\rho_0$ of Definition 1.5". CA-I 929 points to the bare formula instead; the two passages disagree literally. The volume-transfer proof keeps the factor: $Z_m(0)\ge\exp[E_m-C_{\rm low}(2L^m)^4]$ (CA-II 141703–141707). The outline proves its floor for $e^{-E}Z(0)$ (SA 23515–23527). The sourced density of the correlation theorem admits any constant $E$ "independent of $U$ and of $z$" (CA-II 730–739).

So the correction is: read 4.33 (h4)(a), (i-b)(1) and (i-c) for $\widehat\rho_k$, or carry $e^{E_{\rm vac}}$ on the bare side. It changes no probability expectation and no cumulant (CA-II 63067–63068). It is not a new physical assumption.

## 3. The lemma, as its consumers read it

There is no source sentence to quote. The statement below is a reconstruction: each conclusion is the one their printed proof says it shows, or the one a consumer reads. For (b) the printed proof announces (CA-II 63412–63420): "We show that $b\ge0$, that the correlation theorem applies with data $(g,m_J,N_T,x_0)$, that its bare lattice is that of Lemma 6.3 under the dilation $y\mapsto y/(2L^{m_1})$, that its last lattice $T^{(K')}$ is the block lattice at depth $b$ below the cutoff, with $N=2L^{m_1+b}$ sites per side, that the domain … is contained in $\mathbb D$, that $S^T_{n;K,m_1}=S^{K_J}_n$, and that (6.3:eq-last-scale-coupling-b) and (6.3:eq-last-scale-coupling-c) below hold, where neither $x^*(g)$ nor $E_*$ contains $K$, $g_0$, $m_1$, $a$ or positions."

**Notation** (all from CA-II §6.3). The fixed data, in their order (`6.3:not-standing-parameters`, 62824–62860): $d=4$, $G=SU(2)$ with $\operatorname{tr}\mathbb 1=1$; $L$ odd, $L\ge L_0$; $\mathfrak p$ (containing $M=L^{m'}$ and the radius exponent $r$); $\gamma$; $\gamma_H<1$; the source radius $\varrho>0$. The flow letters $\lambda=c_0/2$, $b_+=3\lambda+2c_2$, $c_5=2c_2$, $\lambda^\sharp$, $B^\sharp$ and $g_-(g)=(g^{-2}+B^\sharp)^{-1/2}$. The floors $m_{\mathbb T}$, $N_{\mathbb T}(g,m)$ and $m^J_{\mathbb T}(g)$ (`6.3:def-block-exponent-floor`), and $\mathcal A$, $a^\natural$, $\mathcal B(g)$, $\ell(n,R)$ (`6.3:def-one-sided-floors`). The indices $K=K(g_0,g)$ and $K_J$ (`6.3:def-first-passage`), $X=g^{-2}$, $x_0=g_0^{-2}$, and $m_J:=m^J_{\mathbb T}(g)$. The classes $\mathfrak S(n,R)$, $\mathfrak S(n,R,d)$ (`6.3:def-source-classes`), the norm $\|f\|_\sharp=\max\{\|f\|_\infty,40M\operatorname{Lip}f\}$, and $S^T_n=S^T_{n;K,m_1}$, the joint cumulants under the Wilson measure (`6.3:not-joint-cumulants`). *Case A* means $K_J\ge m_J$; *Case B* means $K_J<m_J$.

**Inputs.** Their status in the account is in §8.

- (I) Clause (0) of Theorem 0 (`4.19:prop-clause-zero`) with `4.2:lem-first-passage`: $K$ is defined, $x_k>X$ for $k\le K$, and $K(g_0,g)\to\infty$ as $g_0\downarrow0$.
- (II) The standing identification $b_{k+1}(0)=\beta_{k+1}$ of `6.3:def-first-passage` (CA-II 63072–63081).
- (III) The correlation theorem `5.1:thm-correlation-theorem` with its admitted inputs, and hypotheses 1–7 and 9 of its torus-bound proof (CA-II 59649–59680). Hypothesis 8, the floor, is **not** assumed; §5 proves it.
- (IV) Hypotheses (h1)–(h3) and (h7)–(h11) of `4.33:thm-stability` at every level $k\le K$ (CA-I 157030–157078), and `4.36:thm-never-large-exponent` and `4.36:cor-density-constants` with their hypotheses (CA-I 159272–159600).
- (V) Bałaban's real-background theorem in the form 4.31 (e) (CA-I 154052–154058), and the first assertion of `4.31:lem-window-characteristic` (CA-I 155039–155078).
- (VI) At zero source, the sourced format of Chapter 5 has the one-step energies $E^{(j)}$ of CA-I. The account makes this identification at CA-II 140916–140926; it is not proved there or here.

**Normalization.** In the sourced density $\rho^w_0=\exp[-A(x_0-w,U)-E]$ of the correlation theorem (`5.1:eq-torus-floor-b`, CA-II 730–739), take
\[
E:=E_{\rm vac}=\sum_{j<K}E^{(j)}(T,T),\qquad K=K(g_0,g), \tag{3.1}
\]
as the account does at CA-II 140918–140924. Then the correlation theorem's partition function is $Z^J=e^{-E_{\rm vac}}Z=\widehat Z$ of (2.3), and the normalized partition function of its torus-bound proof is $\widetilde Z=e^{-\mathcal E}\widehat Z$, with $\mathcal E(0)=0$ (CA-II 59718–59719).

**Lemma 6.3 (reconstructed).** Assume (I)–(VI) and (3.1). Let $0<g\le\min\{\gamma_H,\gamma_J(L,\mathfrak p,\varrho),\gamma_D(L,\mathfrak p,\gamma)\}$, so that the coupling floor `6.3:eq-one-sided-floors-a` holds. Let $m_1\ge m_{\mathbb T}(g_-(g))$ and $0<g_0\le g_-(g)$.

- **(a) Bounded offset.** $K\le K_J$. In Case A, $a:=K_J-K\in\mathcal A$.
- **(b) Admissible data and last-scale constants.** In Case A put $K'=K_J-m_J$, $N_T=2L^{m_1-a}$, $b=m_J-a$, $N=N_TL^{m_J}$. Then every assertion of the announcement quoted above holds; in particular $K'=K-b$, $N=2L^{m_1+b}$ and $X<x_{K'}\le x^*(g)$ (`6.3:eq-last-scale-coupling-b`, CA-II 63501). Moreover
\[
\widetilde Z(0)=\widehat Z(0)\ge e^{-C^*_{\rm low}(g)N^4},\qquad |\widetilde Z(w)|\le e^{C^*_+(g,\varrho)N^4}\ \text{ on }\mathbb D, \tag{3.2}
\]
with $C^*_{\rm low}$ of (5.5) and $C^*_+$ of (6.4). So (`6.3:eq-last-scale-coupling-c`) holds with $E_+^\sharp:=C^*_+$, $C_{\rm low}:=C^*_{\rm low}$ and
\[
E_*(L,\mathfrak p,g,\varrho):=C^*_+(g,\varrho)+C^*_{\rm low}(g)<\infty . \tag{3.3}
\]
$C^*_{\rm low}$, $C^*_+$ and $E_*$ each do not depend on $K$, $g_0$, $m_1$, $a$, $N_T$, $N$ or positions. The number $E_{\rm vac}$ is not bounded, and nothing below needs a bound on it.
- **(c) Change of units** (printed, CA-II 63568–63689). If also $L^{m_1}\ge L^{m_J}\ell(n,R)$ (`6.3:eq-one-sided-floors-c`), then in Case A, for $n\ge2$, $R,d>0$ and $\vec f\in\mathfrak S(n,R,d)$,
$|S^T_n(\vec f)|\le C^*_n(d;R)\prod_i\|f_i\|_\sharp$ with $C^*_n(d;R)=\max_{b'\in\mathcal B(g)}\Phi_{n,dL^{b'},RL^{b'}}(E_*)$ (`6.3:eq-unit-rescalings-a`, `-b`). It is a function of $(L,\mathfrak p,g,\varrho;n,d,R)$ alone and non-increasing in $d$.
- **(d) Remaining cutoffs** (printed, CA-II 63691–63798). In Case B, for $n\ge1$, $R>0$ and $\vec f\in\mathfrak S(n,R)$, $|S^T_n(\vec f)|\le C^B_n\prod_i\|f_i\|_\infty$ with $C^B_n=c_n[12(2R+3)^4]^nL^{4nm_J}$, $c_n=\sum_{\pi\in{\rm Part}(n)}(|\pi|-1)!$.
- **(e) Limits** (printed, CA-II 63800–63833). At fixed $(g,m_1)$, a sequence $g_0^{(i)}\downarrow0$ is in Case A for all but finitely many $i$. It has a subsequence with constant $a$, hence constant $N_T$, $N$, $b$, along which the limit clauses of the correlation theorem apply. The bounds of (b)–(d) hold along the whole sequence.
- **(f) The original floor of (iii-b)** (added). For $n\ge2$, $R,d>0$ and every $m_1$ with $m_1\ge m_{\mathbb T}(g_-(g))$ and $L^{m_1}\ge\ell(n,R)$, which is the floor of CA-I 2610–2620, $|S^T_n(\vec f)|\le C^\infty_n(d;R)\prod_i\|f_i\|_\sharp$ for $\vec f\in\mathfrak S(n,R,d)$. Here $C^\infty_n$ of (7.3) does not depend on $K$, $g_0$, $m_1$ or positions, and is non-increasing in $d$.

**Order of choice.** First $L,\mathfrak p,\gamma,\gamma_H,\varrho$ and every construction constant, as in the account (CA-I 1331–1685; CA-II 2412–2438, 2858–2867). Then $g$, which fixes $m_J$, $x^*(g)$, $\mathcal B(g)$ and the constants (3.2)–(3.3); $\mathcal A$ was fixed before $g$. Then $(n,R,d)$. Then $m_1$, $g_0$ and the positions vary. Uniformity is in the torus exponent $m_1$, at the fixed omitted-step exponent $m_J(g)$. Nothing is claimed for an omitted-step exponent that varies on its own.

## 4. Proof of (a), and of the identification in (b)

**(a), added.** By (I), $x_j>X$ for every $j\le K$. By (II) the run of the correlation theorem has the same numbers $x_j$. $K_J$ is the largest $k$ with $x_j>X$ for all $j\le k$, so $K\le K_J$.

Now let Case A hold, so that $m=m_J$ is an admissible block exponent and the correlation theorem applies. Its flow bound (`6.3:eq-data-families-4`, CA-II 63174–63177) holds for $0\le i<j\le K_J$. If $a=0$, then $a\in\mathcal A$. If $a\ge1$, take $i=K$, $j=K_J$. The definition of $K$ gives $x_K\le X+B^\sharp$, and the definition of $K_J$ gives $x_{K_J}>X$. Hence
\[
\lambda a-2c_2\ \le\ x_K-x_{K_J}\ <\ (X+B^\sharp)-X=B^\sharp ,
\]
so $\lambda a<B^\sharp+c_5$ and $a\in\mathcal A$ (`6.3:eq-one-sided-floors-1`). No sign of a single increment is used. $\square$

Why only Case A: the correlation theorem asserts its flow bounds for data with an admissible block exponent $m$, $m^J_{\mathbb T}(g)\le m\le K_J$ (CA-II 2869–2873). In Case B there is none. Every use of $a\in\mathcal A$ is in Case A: part (b), and part (e) after finitely many terms. Part (d) uses only $K\le K_J$ (CA-II 63700–63701), and part (e) needs only $a_i\ge0$ to get $K^{(i)}_J\ge K_i\to\infty$.

**The identification in (b): their printed proof.** CA-II 63422–63507 proves, in Case A, every assertion of the announcement except the bound on the constants. We use it as printed. In outline: the floors give $m_1-a\ge0$ and $b=m_J-a\ge0$, so $N_T=2L^{m_1-a}$ is an integer $\ge1$, and $L^{K_J}N_T=2L^{m_1+K}$ (`6.3:eq-last-scale-coupling-2`). So the dilation $y\mapsto y/(2L^{m_1})$ maps the bare lattice of spacing $L^{-K}$ on $\mathbb T_{m_1}$ onto the correlation theorem's bare lattice. The spacing of $T^{(k)}$ becomes $L^{k-K}$, so $T^{(K')}$ is the block lattice at level $K-b$, with $N=2L^{m_1+b}$ sites per side. For $\tilde f(y)=f(2L^{m_1}y)$ one has $\|\tilde f\|^J_\sharp=\max\{\|f\|_\infty,40ML^{-b}\operatorname{Lip}f\}\le\|f\|_\sharp$. Linearity of $A(c,U)$ in the weight gives $\rho^w_0=e^{-E}\exp[-x_0A(U)+\sum_iz_i\mathcal O(f_i)]$, so $Z=e^EZ^J$ and $S^T_{n;K,m_1}=S^{K_J}_n$. Finally (`6.3:eq-last-scale-coupling-1`) with $i=K'$, $j=K_J$ gives
\[
X<x_{K'}\le x^*(g):=X+b_++\max\{0,\,3\lambda m_J+2c_2\} \tag{4.1}
\]
(CA-II 63492–63501). The right side is a function of $(L,\mathfrak p,g)$.

With $E=E_{\rm vac}$ of (3.1), their identity $Z=e^EZ^J$ reads $Z^J=\widehat Z$. It identifies the probability laws and the cumulants. It does not equate $Z^J$ with the unshifted Chapter 1 integral $Z$; that equation is exactly the step §2 shows to fail.

## 5. Proof of (b): the normalized floor

Work in Case A at the last lattice $T^{(K')}$. Put $\mathsf V:=N^4$, its number of sites; $x:=x_{K'}\in(X,x^*]$ by (4.1); and $\eta:=L^{-K'}$, the fine spacing in level-$K'$ units. Let $a_1$ and $B_3\ge1$ be the constants of 4.31 (e), and $\varepsilon(x)=A_0x^{-1/2}(\log x)^{p_0}$, $p_0\ge0$, the small-field threshold (CA-I 153606–153610). All three are fixed before $g$ and do not depend on the torus. Define, after $g$,
\[
\varepsilon_*(g):=A_0(x^*)^{-1/2}(\log X)^{p_0},\qquad
s_*(g):=\min\Bigl\{\tfrac12,\ \tfrac{a_1}8,\ \tfrac{\varepsilon_*}{8B_3},\ \tfrac1{8B_3\sqrt{x^*}}\Bigr\}>0. \tag{5.1}
\]
Since $X>1$, $x\le x^*$ and $p_0\ge0$, we have $\varepsilon(x)\ge\varepsilon_*$.

**Step 1: the small-field ball.** Let $\mathcal B$ be the set of block fields $V$ on $T^{(K')}$ with $\|V(b)-1\|<s_*$ (operator norm, as in CA-I 153575–153583) on each of its $4\mathsf V$ bonds. For a plaquette, $V_1V_2V_3V_4-1=\sum_j V_1\cdots V_{j-1}(V_j-1)$, multiplication by a unitary preserves the operator norm, and $\|V^{-1}-1\|=\|V-1\|$. So $\|V(\partial p)-1\|<4s_*$ on $\mathcal B$. Now $4s_*\le a_1/2$ and $4B_3s_*\le\varepsilon_*/2\le\varepsilon(x)/2$. So 4.31 (e) with $\varepsilon_1=4s_*$, and the first assertion of `4.31:lem-window-characteristic` with $w=4s_*$, give on $\mathcal B$
\[
\chi_{K'}=1,\qquad \|U_{K'}(V)(\partial p)-1\|<4B_3s_*\eta^2\ \text{ for every fine plaquette }p. \tag{5.2}
\]
If $K'=0$, then $U_0=V$, $\eta=1$, there is no $\chi$, and (5.2) holds since $B_3\ge1$. (If the datum is read in the convention of CA-I 155092–155095, replace $a_1$ by $a_1/Q_0$ and $B_3$ by $Q_0B_3$, $Q_0:=\max\{1,C_Q\}$, in (5.1).)

**Step 2: the action.** For $W\in SU(2)$ with eigenvalues $e^{\pm i\theta}$ and $\operatorname{tr}\mathbb 1=1$, $1-\operatorname{Re}\operatorname{tr}W=1-\cos\theta=\tfrac12\|W-1\|^2$. Below $T^{(K')}$ there are exactly $6\mathsf V\eta^{-4}$ fine plaquettes. So on $\mathcal B$, by (5.2) and $s_*^2\le(64B_3^2x^*)^{-1}$,
\[
A(U_{K'}(V))\le6\mathsf V\eta^{-4}\cdot\tfrac12(4B_3s_*\eta^2)^2=48B_3^2s_*^2\,\mathsf V,\qquad
x\,A(U_{K'}(V))\le\tfrac{48x}{64x^*}\mathsf V\le\tfrac34\mathsf V. \tag{5.3}
\]
The powers $\eta^{-4}$ and $\eta^4$ cancel. The curvature bound for the minimizing background, (5.2), is what allows it.

**Step 3: Haar mass of a ball** (the outline's calculation, SA 23504–23513). For $0<s\le1$, normalized Haar measure gives $\{W:\|W-1\|<s\}$ mass at least $c_Hs^3$, $c_H=8/(3\pi^3)$. Indeed write $W=\cos\theta\,\mathbb 1+i\sin\theta\,n\cdot\sigma$; then $\|W-1\|=2\sin(\theta/2)\le\theta$, and Haar measure is $(2\pi^2)^{-1}\sin^2\theta\,d\theta\,d\Omega(n)$. So the set $\{0\le\theta<s\}$ lies in the ball. On $[0,1]$, $\sin\theta\ge2\theta/\pi$ by concavity of sine on $[0,\pi/2]$. Integrating over $\theta<s$ and over $S^2$ (area $4\pi$) gives $\frac{2}{\pi}\cdot\frac{4}{\pi^2}\cdot\frac{s^3}{3}=c_Hs^3$.

**Step 4: integration.** By positivity of the terms and (2.4) at $k=K'$, then (5.2), (5.3), Step 3 with $s=s_*\le\tfrac12$, and independence of the $4\mathsf V$ bond measures,
\[
\widetilde Z(0)=\widehat Z(0)=\int\widehat\rho_{K'}\,dV_{K'}\ \ge\int_{\mathcal B}e^{-xA(U_{K'}(V))-E_-\mathsf V}\,dV_{K'}\ \ge\ e^{-(E_-+3/4)\mathsf V}\bigl(c_Hs_*^3\bigr)^{4\mathsf V}=e^{-C^*_{\rm low}(g)\mathsf V}, \tag{5.4}
\]
\[
C^*_{\rm low}(g):=E_-+\tfrac34+4\log(c_H^{-1})+12\log(s_*(g)^{-1}). \tag{5.5}
\]
The first equality is $\mathcal E(0)=0$. The second is (i-c) for $\widehat\rho$ (§2.3), and also the correlation theorem's mass identity $\int\rho^0_{K'}\,dV_{K'}=Z^J(0)$ (CA-II 2933–2935) with $Z^J=\widehat Z$; no pointwise identification of the two runs' densities is needed. If $K'=0$, use $\widehat\rho_0=e^{-x_0A-E_{\rm vac}}$ and $-E_{\rm vac}=-\mathfrak E_0=\mathfrak l_0-\mathfrak r_0\ge-C_{\mathfrak r}\mathsf V$ (4.36 (a)); the same calculation applies.

$C^*_{\rm low}$ depends only on $E_-,c_H,a_1,B_3,A_0,p_0,X$ and $x^*(g)$. So it is free of $K$, $g_0$, $m_1$, $a$, $N_T$, $N$ and positions. In bare variables (5.4) reads $Z(0)\ge\exp[E_{\rm vac}-C^*_{\rm low}(g)N^4]$. This is the form of `gates/nrm-check.md` (21), of the outline's (OH6) (SA 23515–23527), and of CA-II 141703–141707.

**The single-coupling form.** The account reads $C_{\rm low}$ "at the bound … for $x_{K'}$" (CA-II 63221–63225, 63543–63547). Put $s(x):=\min\{\tfrac12,\tfrac{a_1}8,\tfrac{\varepsilon(x)}{8B_3},\tfrac1{8B_3\sqrt x}\}$ and $C_{\rm low}(x):=E_-+\tfrac34+4\log c_H^{-1}+12\log s(x)^{-1}$. The same proof, with $s(x_{K'})$ in place of $s_*$, gives $\widetilde Z(0)\ge e^{-C_{\rm low}(x_{K'})N^4}$. On $X<x\le x^*$ each entry of $s(x)$ is at least the matching entry of $s_*$, so $C_{\rm low}(x)\le C^*_{\rm low}(g)$.

## 6. Proof of (b): the upper bound in the same normalization, and $E_*$

The torus-bound proof (`5.12:prf-torus-bound-proof`, CA-II 59645–59813) proves $|\widetilde Z(z)|\le e^{E_+^\sharp N^4}$ on $\mathbb D$ (`5.12:eq-torus-bound-proof-7`) from its hypotheses 1–7 and 9. The floor, hypothesis 8, enters only afterwards (59815–59821). Two things must be checked: that this bound holds with $E=E_{\rm vac}$, and how $E_+^\sharp$ depends on the last coupling.

**The normalization enters with coefficient one.** The exponent of the sourced induction format contains $-E^w_k$ (`5.2:eq-induction-format-3`, CA-II 25040–25043), and clause (f) gives $E^w_k=E-\sum_j\sum_{X\subset\Lambda_j}e^{(j)}(X;w)-(\text{the $z$-free logarithms})$ (CA-II 25233–25238). So the choice $E=E_{\rm vac}$ multiplies every history measure by $e^{-E_{\rm vac}}$ and leaves $e_j(X;w)$ and $\mathcal E(w)$ unchanged. After $\mathcal E$ is subtracted, the source-free constant of a history $h$ at level $k$ is, by (VI), the energy of 4.36:
\[
E_k[h]=E_{\rm vac}-\sum_{j<k}E^{(j)}(\Omega_{j+1},\Lambda_{j+1}).
\]
The missing source shares are the extra history costs of CA-II 59727–59730. In particular, the source-free residual of the never-large history is $\mathfrak E_k$ of 4.36 (a), not the bare constant of (2.1).

**The label bound.** `4.36:cor-density-constants` (2) (CA-I 159538–159550) bounds this energy for every label:
\[
-E_k[\mathcal S]\le C_\Gamma(g_k)|T|_k+\sum_{j=1}^k\bigl(C_{\log}\log x_{j-1}+C^{\rm lab}_{\rm loc}\bigr)|Z^+_j|_j,\qquad C_\Gamma(g_k)=\tfrac92(\log x_k+\bar B\gamma^2)+C_{\mathfrak r}, \tag{6.1}
\]
at $N=2$. The first term uses the whole current volume $|T|_k=\mathsf V$ at $k=K'$. The sum is a large-field charge. Like the lower-zone terms, the missing source shares and the live arrested piles, it is paid inside the history sum by the retained hypotheses 5–7 and 9 (CA-II 59727–59740, 59766–59799).

**The extra top-zone member.** The per-zone-cell value bound with the volume ceiling gives at most $2^{-4}(C_\sharp O(1)+1)\log x_j$ per zone cell (`5.12:eq-torus-bound-proof-5`, CA-II 59759–59763). Below $K'$ it joins the logarithmic charges already paid. In the top zone $j=K'$ it is extensive, and it is the member $2^{-4}(C_\sharp O(1)+1)\mathsf T_{K'}$, $\mathsf T_{K'}=\log x_{K'}$ (59772–59780). The comparison constant $C_\sharp$ is bounded by the number $\bar C_\sharp$, which is chosen before the coupling ceiling (`5.2:def-comparison-constant`, CA-II 7992–8073; order of choice, 2427).

**Assembly.** Fix the constants of the retained estimates, all chosen before $g$: $C^J_{\rm maj}$, the source-budget form of the nonlogarithmic majorant constant; $c_{\rm gas}$, the exponent of the live-gas and history-label sum after the charges are paid; and $c_{\rm top}:=2^{-4}(\bar C_\sharp C_{\rm zone}+1)$, with the fixed geometric counting factor in $C_{\rm zone}$. Then the modulus integration and gas sum of CA-II 59801–59813, applied to each normalized history at level $K'$, give
\[
|\widetilde Z(z)|\le e^{(A_J+B_J\log x_{K'})\mathsf V}\ \text{ on }\mathbb D,\qquad
A_J:=\tfrac92\bar B\gamma^2+C_{\mathfrak r}+C^J_{\rm maj}+c_{\rm gas},\qquad B_J:=\tfrac92+c_{\rm top}. \tag{6.2}
\]
None of $A_J$, $B_J$ contains $N_T$, $K$, $K'$, the number of levels or positions. Since $B_J>0$ and $x_{K'}\le x^*(g)$ by (4.1),
\[
|\widetilde Z(z)|\le e^{C^*_+(g,\varrho)N^4}\ \text{ on }\mathbb D,\qquad C^*_+(g,\varrho):=A_J+B_J\log x^*(g). \tag{6.3}
\]
$C^*_+$ depends on $\varrho$ through the source budget. In bare variables (6.3) reads $|e^{-\mathcal E(z)}Z(z)|\le e^{E_{\rm vac}+C^*_+N^4}$. The factor $e^{E_{\rm vac}}$ must stay: multiplying a weaker bare bound, such as $Z(0)\le1$, by $e^{-E_{\rm vac}}$ would not give (6.3).

This is a port of the account's sourced estimates, at the standing of hypotheses 1–7 and 9 and of (VI). It does not derive a complex-source majorant from the source-free bound alone. It adds two things: the normalization is explicit, and the dependence on $x_{K'}$ is displayed.

A remark on the account's wording. CA-II 63227–63228 and 63407–63410 say that $E_+^\sharp$ reads $(g,m)$ only through the top-zone member. But Bałaban's constants $E_\pm$ "depend on $g_k$" (CA-II 59769–59770), and (6.1) has the leading member $\tfrac92\log x_k$. The single *additional* member is the top-zone one. All logarithmic members together are bounded by $B_J\log x_{K'}$, as in (6.2). The consumers read only this upper bound, not a unique split of the exponent.

**The constant $E_*$.** By (5.5) and (6.3),
\[
\boxed{\;E_*(L,\mathfrak p,g,\varrho)=A_J+B_J\log x^*(g)+E_-+\tfrac34+4\log(c_H^{-1})+12\log(s_*(g)^{-1})\;} \tag{6.4}
\]
satisfies (`6.3:eq-last-scale-coupling-c`). It is built from construction constants fixed before $g$, from $X=g^{-2}$, and from $x^*(g)$ and $s_*(g)$, which are functions of $(L,\mathfrak p,g)$. So it does not contain $K$, $g_0$, $m_1$, $a$, $N_T$, $N$ or positions. This proves (3.2), (3.3) and part (b). $\square$

## 7. Parts (c)–(e), the cancellation of $E_{\rm vac}$, and the original floor

**7.1 Parts (c), (d), (e): their printed proofs.** Each applies as printed, with $E_*$ of (6.4) in (`6.3:eq-last-scale-coupling-c`) and with (a) as stated in §3.

- (c) (CA-II 63568–63689) reads part (iii) of `6.4:thm-per-ball-bound` on $T^{(K')}$ with $(R,d)$ replaced by $(RL^b,dL^b)$, in the form $C^\infty_n=\Phi_{n,d,R}(E_+^\sharp+C_{\rm low})$. The floor (`6.3:eq-one-sided-floors-c`) gives $\ell(n,RL^b)\le L^b\ell(n,R)\le L^{m_1}$ for every $b\in\mathcal B(g)$. $\Phi$ is non-decreasing in $t$, so $t\le E_*$ and a maximum over the finite set $\mathcal B(g)$ give $C^*_n$. There is no circle: the proof of 6.4 keeps $E_+^\sharp+C_{\rm low}$ as a number throughout, and invokes this lemma only in its last paragraph on constants (CA-II 64271–64273).
- (d) (CA-II 63691–63798) uses only $K\le K_J$ from (a), then a local plaquette count, $\#\{p:x(p)\in\operatorname{supp}f_i\}\le6(2R+3)^4L^{4K}\le6(2R+3)^4L^{4m_J}$, and the moment–cumulant formula. It needs no torus floor and no partition-function bound.
- (e) (CA-II 63800–63833): $K_J^{(i)}=K_i+a_i\ge K_i\to\infty$ by (I), so Case A holds for all but finitely many $i$. There $a_i\in\mathcal A$, a finite set, so some value repeats infinitely often. Along that subsequence $N_T$, $N$ and $b$ are constant, which are the fixed-data hypotheses of the correlation theorem's limit clauses. The bounds of (b)–(d) do not depend on $a_i$, so they hold along the whole sequence.

**7.2 Where $E_{\rm vac}$ cancels.** Put $A:=C^*_+$, $B:=C^*_{\rm low}$, $\mathsf V=N^4$. In bare variables, (6.3) and (5.4) read
\[
|e^{-\mathcal E(w)}Z(w)|\le e^{E_{\rm vac}+A\mathsf V},\qquad Z(0)\ge e^{E_{\rm vac}-B\mathsf V},\qquad
\Bigl|e^{-\mathcal E(w)}\frac{Z(w)}{Z(0)}\Bigr|=\frac{|\widetilde Z(w)|}{\widetilde Z(0)}\le e^{(A+B)\mathsf V}. \tag{7.1}
\]
The same $E_{\rm vac}$ stands in both bounds because numerator and denominator are on one torus, at one cutoff, in one run. Equivalently, the bare exponents $A+E_{\rm vac}/\mathsf V$ and $B-E_{\rm vac}/\mathsf V$ have the uniform sum $A+B\le E_*$. The four direct uses (gates/lsc2-gate.md, item 3):

| Use | What it reads | Effect |
|---|---|---|
| CA-II 63531–63565 | the upper bound with its top-zone member, and the floor with $C_{\rm low}$ read through $x_{K'}$ | these are (6.2)–(6.3) and §5 (single-coupling form); $Z=e^EZ^J$ (63486) is used only for cumulants |
| CA-II 63907–63946 | $E_+^\sharp+C_{\rm low}\le E_*$, then a maximum over $b$ | the cancellation (7.1) happens inside each run, before the maximum |
| CA-II 64157–64183, 64246–64283 | (S) and (F) at a periodized weight and at zero source, on one torus; then the $|\mathcal C|$-th root; also $C_{\rm low}$ alone "bounded above by a quantity free of $m$" (64271–64273) | (7.1) before the root leaves $(A+B)N^4/|\mathcal C|=(A+B)\ell^4$ and no $E_{\rm vac}/|\mathcal C|$; $C^*_{\rm low}$ is uniform by itself |
| CA-II 68362–68368 | a dependency statement for clause (ii) | clause (ii) uses probability expectations and cumulants (66418–66477), which the scalar does not change |

**7.3 The original floor of (iii-b): proof of (f), added.** Part (c) uses the stronger floor (`6.3:eq-one-sided-floors-c`). Clause (iii-b) asks only $m_1\ge m_{\mathbb T}(g_-(g))$ and $L^{m_1}\ge\ell(n,R)$ (CA-I 2610–2620). The torus exponents between the two floors form a finite set, and the torus bound covers them. Put
\[
J:=\max\{m_{\mathbb T}(g_-(g)),\ m_J+\log_L\ell(n,R)\},\qquad N_{\max}:=2L^{J+m_J},\qquad \Delta:=d/(2L^J). \tag{7.2}
\]
For $m_1\ge J$, (c) applies in Case A and (d) in Case B. Let $m_1<J$ and Case A. Then $N=2L^{m_1+b}\le N_{\max}$, the separation on the side-one torus is $d/(2L^{m_1})\ge\Delta$, and $\|\tilde f\|^J_\sharp\le\|f\|_\sharp$ (§4). Clause (iv) of the correlation theorem (CA-II 2937–2959), with $\mathsf Q\le e^{E_*N^4}\le e^{E_*N_{\max}^4}$ by (b), and its decreasing majorant $C_{UV}(\mathsf d)\le C\mathsf d^{-4}(1+\log^+\mathsf d^{-1})$, gives $|S^T_n(\vec f)|\le C^{\rm bd}_n(d;R)\prod_i\|f_i\|_\sharp$ with
\[
C^{\rm bd}_n(d;R):=\Bigl[C\Delta^{-4}(1+\log^+\Delta^{-1})+\log2\cdot\bigl(2e^{E_*N_{\max}^4}+2\bigr)^n\Bigr]\Bigl(\frac n\varrho\Bigr)^n .
\]
Since $\|f\|_\infty\le\|f\|_\sharp$, part (f) holds with
\[
C^\infty_n(d;R):=\max\bigl\{C^*_n(d;R),\ C^B_n,\ C^{\rm bd}_n(d;R)\bigr\}. \tag{7.3}
\]
Each entry is free of $K$, $g_0$, $m_1$ and positions and non-increasing in $d$, so the maximum is too. If no separated tuple fits on a small torus, there is nothing to bound. This uses (b) and the torus bound, not (iii-b) itself. Under the floor of (c), $\max\{C^*_n,C^B_n\}$ suffices, which is the constant of `6.3:cor-volume-free-constant`. $\square$

## 8. Inputs, with their status in their account

"No status sentence" means proved in full in the account's convention (CA-I 27–46), as an implication from the hypotheses the statement lists.

| Input | Where | Status in their account |
|---|---|---|
| (I) clause (0); first passage | `4.19:prop-clause-zero` (CA-I 56419); `4.2:lem-first-passage` (CA-I 3636) | no status sentence |
| (II) $b_{k+1}(0)=\beta_{k+1}$ | `6.3:def-first-passage` (CA-II 63073–63075) | "we assume, as a standing hypothesis" |
| (III) correlation theorem, flow bounds, mass identity, torus bound (iv) | `5.1:thm-correlation-theorem` (CA-II 2791–2966) | no status sentence; its admitted inputs include "the statement on the window data of the blocks at the preparatory site … whose proof is outstanding" (2808–2812) |
| (III) hypotheses 1–7, 9 of the torus-bound proof | `5.12:prf-torus-bound-proof` (CA-II 59649–59680) | statements of Chapter 5, named there as hypotheses |
| (IV) representation and integral identities, (h1)–(h3), (h7)–(h11) | `4.33:thm-stability` (CA-I 157028–157078) | no status sentence; (h1) rests on `4.20:thm-representation` and Bałaban's majorants CMP 122 (1.73), (1.79) |
| (IV) vacuum energies and density constants | `4.36:thm-never-large-exponent` (CA-I 159272), `4.36:cor-density-constants` (CA-I 159511) | no status sentence; hypotheses include CMP 109 (1.18) and CMP 119 (2.31), cited by statement |
| (V) real background fields | 4.31 (e) = Bałaban CMP 102, Theorem 1, (7)–(10) (CA-I 154052–154058) | published theorem, cited by statement |
| (V) small-field functions equal one | `4.31:lem-window-characteristic` (CA-I 155039) | no status sentence; first assertion read off from 4.31 (e) |
| (VI) zero-source energies of Chapter 5 = $E^{(j)}$ of CA-I | used at CA-II 140916–140926 | identification made, not proved |
| per-ball bound, used by (c) | `6.4:thm-per-ball-bound` (CA-II 63964) | no status sentence; an implication from the correlation theorem, CMP 116 (1.26) cited by statement, reflection positivity (proved) and this lemma (CA-III 110895–110899) |
| $SU(2)$ Haar facts; moment–cumulant formula; axial gauge | §2, §5; `6.3:eq-plaquette-count-1` (CA-II 63766) | elementary, proved in full here or there |

## 9. Scope limits carried from the checks

1. **An implication.** The lemma holds at the standing of (I)–(VI). It proves none of them. In particular the outstanding window-data statement of the correlation theorem (CA-II 2808–2812), the eight retained sourced hypotheses, the representation and vacuum-energy hypotheses, Bałaban's real-background theorem and identification (VI) stay open where the account leaves them (`gates/lsc2-gate.md`, verdict). So clause (iii-b) is no longer blocked by this lemma, but it is not unconditional.
2. **What is uniform.** Uniformity is in the torus exponent $m_1$, at the fixed omitted-step exponent $m_J(g)$. $E_{\rm vac}$ is not bounded; it is about $-\tfrac92\log x_0$ per bare site, and it cancels only inside one run on one torus (7.1). The lemma proves $b\in\mathcal B(g)\subset[0,m_J(g)]$, not that $b$ is independent of $K$ (`gates/lsc-uses-check.md`, F1).
3. **Case B.** There no admissible data of the correlation theorem exist (`gates/lsc-uses-check.md`, F2). Only (d) holds there, and it gives no partition-function bound. For the same reason this note states $a\in\mathcal A$ in Case A only (§4); every use is in Case A.
4. **Other uses of the lemma.** The four uses of §7.2 are checked (`gates/lsc2-gate.md`). `gates/lsc-uses-check.md` finds four more covered after stated ceilings (U1, U3–U5): `6.1:not-units-sources` (a), `6.4:rem-unit-conversion`, `6.4:rem-complex-sources` (Case A), and the paragraph after `6.2:prop-cell-covariance`. `6.4:rem-small-cutoffs` (U10) is an alternative route; its claim that no separate small-cutoff treatment is needed is not supported, since Case B needs (d). `8.22:not-partition-sources-cells` and `9.98` read the two bounds in unit-lattice volume $(2L^m)^4$ with levels $j\le K$. This lemma gives them only in last-lattice volume $L^{4b}(2L^m)^4$, in Case A. The unit-site clause $\mathsf B\le C_{\mathsf B}(1+\log g^{-2})$ (CA-II 140932–140933) is not supplied. Across two tori $E_{\rm vac}$ does not cancel; the residue is the vacuum-density difference (`8.22:lem-vacuum-energy-density`), an input outside this lemma. The ceiling Lemma M and the Case B transfer repair in `gates/lsc-uses-check.md` are Claude's, not checked by the other model, and not part of this note.
5. **The correction elsewhere.** Other passages read the bare floor and need the same normalized reading (`gates/nrm-check.md` §6): 4.31 (d) and the fixed-depth limits, where a positive bare limit $Z_K\ge z_*>0$ is false by (2.2) (CA-I 156531–156656, 156782–156834); `8.8:lem-stability-exponent`; and the global quotients of 8.12 and 8.18. This note does not check them.
6. **Not claimed.** No factorial growth, clustering, $O(4)$ or higher-point rotation result; no statement for $SU(N)$, $N\ge3$; no unconditional stability theorem.
7. **Already theirs** (`gates/lsc-value.md` §3). The identification, transport, local count and subsequence arguments of (b)–(e), the floor mechanism, the Haar calculation and the normalized vacuum remainder are the account's. The additions are the offset argument for (a), the explicit constants on one coupling window ((5.1), (5.5), (6.2)–(6.4)), the normalization reconciliation of §2, and the completion (f).
8. **Presentation changes against `library/lsc.md`.** The second clause of (a) is stated in Case A (§4). The constant in (6.1) is the account's $\bar B$ of 4.36; `lsc.md` uses a larger $B_{\rm vac}$, which also works. The slope is written $B^\sharp$, as in CA-II §6.3; CA-I writes the clause-(0) slope as $B_\sharp$ (CA-I 641–667), the same letter as the constant of CA-I 157049 (`gates/out-lsc-check.md`, F3). Proposition 2.2 is `gates/nrm-check.md` §3. The bare floor's failure is shown at fixed $g$; the version uniform in $K'$ is nrm-check (12)–(14). No other change.

## Result

**Proof** (write-up of checked texts; this write-up itself is not checked by the other model).

- Lemma 6.3:lem-last-scale-constants (CA-II 63365, statement unwritten there; "stated; proof incomplete" at CA-III 110895–110899) holds as reconstructed in §3, parts (a)–(f), as an implication from inputs (I)–(VI), in the vacuum-normalized convention (3.1). At $m=m_J(g)$: $e^{-E_{\rm vac}}Z(0)\ge e^{-C^*_{\rm low}(g)N^4}$, $|e^{-E_{\rm vac}-\mathcal E(w)}Z(w)|\le e^{C^*_+(g,\varrho)N^4}$, and $C^*_++C^*_{\rm low}\le E_*$ of (6.4). Each constant is uniform in $K$, $g_0$, $m_1$, $a$, $N_T$ and positions. $E_{\rm vac}$ cancels exactly at the four direct uses. (f) gives the per-ball constant under the original floor of clause (iii-b).
- **Correction to their text.** 4.33 (h4)(a) (CA-I 157039–157041) does not hold for the bare density of Definitions 1.1 and 1.5 (CA-I 477–481, 924–933): the bare identity is $-E^{\rm bare}_k[\mathcal S_\emptyset]=E_{\rm vac}+\mathfrak l_k-\mathfrak r_k$, and the bare floor is false (Proposition 2.2). In the account's own convention $\widehat Z=e^{-E_{\rm vac}}Z$ (CA-II 140916–140926; SA 23515–23527) the lower member and floor hold, and no probability or cumulant changes. This correction went to the authors as issue #16 on 2026-11-07 (`library/out-lsc.md`).
- **Open.** The upstream inputs (I)–(VI) at their standing in the account; the unit-lattice reading of 8.22 and 9.98; the cross-torus vacuum-density bound; the same correction at 4.31 (d), 8.8, 8.12 and 8.18.
