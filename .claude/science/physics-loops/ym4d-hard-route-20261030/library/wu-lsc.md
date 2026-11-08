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

**What this note proves.** Lemma 6.3 as those four uses read it (§3), as an implication from inputs that the account states and declares proved (§8). On the way it corrects one application in CA-I: 4.33 (h4)(a) does not hold for the bare density of Definitions 1.1 and 1.5 (§2). The correction uses the account's own vacuum-normalized convention.

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
At $k=1$ the bare constant is $E^{\rm bare}_1[\mathcal S_\emptyset]=-E^{(0)}(T,T)\ge[\tfrac92(L^4-1)\log x_0-D_0]\,|T|_1$. The bare reading of (h4)(a) gives $E^{\rm bare}_1[\mathcal S_\emptyset]=-\mathfrak l_1+\mathfrak r_1\le C_{\mathfrak r}|T|_1$. The constants $D_0$, $C_{\mathfrak r}$ depend only on $L$, $N$, $\mathfrak p$, while $x_0=g_0^{-2}$ is unbounded on $0<g_0\le g_-(g)$. So the two fail together once $\log x_0>(D_0+C_{\mathfrak r})/[\tfrac92(L^4-1)]$.

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

