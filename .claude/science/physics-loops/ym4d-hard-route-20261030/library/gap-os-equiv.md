lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-11T09:30Z

Statements: IN PROGRESS (written section by section; this line is replaced at the end).

# Decay of correlations, the spectrum of H, and limits (queue row 668, `gap-os-equiv`)

Provenance: Claude Opus 5.5, high effort, Mac mini worker 2, checkout `5af49c4fc`, started 2026-11-10T21:30Z. Research text, not an audit; grants no status. One author run, no subagents, not checked by another model. No numeric run was made; every step is by hand. The task asked for the `lead:`/`lease_until:` lines first, so the status line is line 4.

## 0. Sources, coverage and credit

0.1. **Coverage check.** `library/open-core.md` (564 lines) has no hit for "mass gap", "spectral gap" or "semigroup". The FINISH rows on the gap are 655, 656, 661 (readings), 662 (`gap-skeleton`, a direction document), 667 (`gap-transfer`), 668 (this row) and 669 (`gap-skeleton-max`, a plan in progress). No other row proves the statements of this row. This file attacks no lemma of `open-core.md`.

0.2. **Repository sources read for this file.**

| Source | Part read | Use here |
|---|---|---|
| `library/prior/gap-prior.md` (Codex digest, row 655) | sections 1, 2, 3, 5 | 0.3 below |
| `library/gap-skeleton.md` (row 662) | sections 0, 1, 2 | names (G-ell), (G-inf); differences in Section 8 |
| `library/gap-transfer.md` (row 667, this worker's earlier item) | all | lattice instance of (2), (3); Lemma A3 there; Section 7 |
| `library/cl1.md` | Lemma 5 (lines 275-326) | statement (1) in the Schwinger-function instance |

0.3. **Prior repository results, and how this file uses them.**

- `ym/crossover-reduction`, result (L3), as reported by `gap-prior.md` section 2: "common exponential decay on a dense centered source algebra implies no spectral support below the common decay exponent, excludes additional zero-energy vacua". This is statement (3) below. The branch is not in this checkout (`git branch -r` lists no such branch), so its file was **not read** and its hypotheses could not be checked. Statement (3) is therefore proved here; the proof is eight lines and uses no spectral theorem.
- `physics-loop/cluster-mass-gap-adjoint-repair-20260529`, lemma (B), as reported by `gap-prior.md` section 2: in finite dimension, $\Delta_T>0$ gives a temporal connected correlator bounded by $\|A\|\|B\|e^{-n\Delta_T}$. This is the finite-dimensional case of statement (2). Branch file **not read**.
- `library/gap-transfer.md` (6b) and (7): statements (2) and (3) for the SU(2) Wilson transfer operator at fixed spacing, proved there from trace formulas. Section 9.6 of that file names this row as the general form.
- `library/cl1.md` Lemma 5: statement (1) for the Schwinger functional $\sigma$ of T0 (origin: SA HB1-HB7a, YM3_I IV-27-22, credited there to Sussman and Alpoge). Its proof of contraction (its eq. (18)) is the argument of 1.3 below. It defines $H$ through the spectral theorem for $T_1$. Section 1 below instead builds $H$ as a generator, so that no step of this file uses the spectral theorem.

0.4. **Literature, for credit only.** K. Osterwalder and R. Schrader, CMP 31 (1973) 83 and CMP 42 (1975) 281 (the reconstruction from reflection positivity): **not read**. J. Glimm and A. Jaffe, *Quantum Physics*, 2nd ed., Springer 1987, chapter 6 (the same, for measures): **not read**. E. Hille and K. Yosida (generators of contraction semigroups): **not read**. Sussman and Alpoge, with Claude and Codex as authors of their text, give the counterexample $d\mu(E)=Ee^{-E}dE$ (polynomial decay without a gap) at YM4_1400 lines 556-563, quoted in `gap-skeleton.md` section 1.1: **not read by this session**, quoted from that file. Every step below is proved here; nothing from these sources is a step.

0.5. **No spectral theorem.** Every statement below is proved with Hilbert-space arguments only: Cauchy-Schwarz, completion, Riemann integrals of continuous vector functions, and the definition of the spectrum. Where the row speaks of "the spectrum of $H$", Lemma E gives the translation into semigroup bounds by hand.

0.6. No numeric job was started, so the numeric lock and the memory check were not needed.

## S. Setting and properties

S.1. **Time set.** $\mathbb T$ is $\mathbb R$ (continuum) or $a\mathbb Z$ with $a>0$ (lattice). $\mathbb T_+=\mathbb T\cap[0,\infty)$ and $2\mathbb T_+=\{2t:t\in\mathbb T_+\}$.

S.2. **Data.** A *time-reflection datum* $\mathfrak D=(\mathcal V,b,\tau,1)$ consists of
- a complex vector space $\mathcal V$ (the observables at nonnegative time);
- a map $b:\mathcal V\times\mathcal V\to\mathbb C$, antilinear in the first and linear in the second slot (the reflected pairing, "$\langle\Theta\bar F\,G\rangle$");
- linear maps $\tau_t:\mathcal V\to\mathcal V$, $t\in\mathbb T_+$, with $\tau_0=\mathrm{id}$, $\tau_s\tau_t=\tau_{s+t}$ (translation forward in time);
- an element $1\in\mathcal V$ with $\tau_t1=1$ and $b(1,1)=1$.

The **truncated two-point function** is $u(F,G;t):=b(F,\tau_tG)-b(F,1)\,b(1,G)$.

S.3. **Properties.** Each statement below lists which of these it uses, and no others.
- **(P1) reflection positivity:** $b(F,F)\ge0$ for all $F\in\mathcal V$.
- **(P2) time symmetry:** $b(F,\tau_tG)=b(\tau_tF,G)$ for all $F,G$ and $t\in\mathbb T_+$.
- **(P3) time growth:** for each $F$ there are $C_F,k_F\ge0$ with $b(\tau_tF,\tau_tF)\le C_F(1+t)^{k_F}$ for all $t\in\mathbb T_+$.
- **(P4) time continuity** ($\mathbb T=\mathbb R$ only): $b(F,\tau_sF)\to b(F,F)$ as $s\downarrow0$, for each $F$.

S.4. **Instance (M): a measure.** Let $(\Phi,\Sigma,\mu)$ be a probability space: lattice fields, or distributions. Let $\alpha_t$ ($t\in\mathbb T$) be a group of bimeasurable bijections of $\Phi$ preserving $\mu$ (time translations), and $\theta$ a bimeasurable involution preserving $\mu$ (time mirror), with $\theta\alpha_t\theta=\alpha_{-t}$. For a measurable $F$ put $(\tau_tF)(\phi)=F(\alpha_{-t}\phi)$ and $(\Theta F)(\phi)=F(\theta\phi)$; then $\Theta\tau_t=\tau_{-t}\Theta$. Let $\Sigma_+\subset\Sigma$ be a sub-$\sigma$-algebra (fields at times $\ge0$) with $\tau_t L^2(\Sigma_+)\subset L^2(\Sigma_+)$ for $t\ge0$. Put $\mathcal V=L^2(\Phi,\Sigma_+,\mu)$, $b(F,G)=\mathbb E_\mu[\overline{\Theta F}\,G]$, $1$ the constant. Then:
- (P2) holds: by invariance of $\mu$ under $\alpha_t$, $b(\tau_tF,G)=\mathbb E[\overline{\tau_{-t}\Theta F}\,G]=\mathbb E[\overline{\Theta F}\,\tau_tG]$.
- (P3) holds with $C_F=\|F\|_2^2$, $k_F=0$: Cauchy-Schwarz and invariance give $|b(\tau_tF,\tau_tF)|\le\|\Theta\tau_tF\|_2\|\tau_tF\|_2=\|F\|_2^2$.
- (P4) holds if $\|\tau_sF-F\|_2\to0$ as $s\downarrow0$, since $|b(F,\tau_sF)-b(F,F)|\le\|F\|_2\|\tau_sF-F\|_2$.
- (P1) is the hypothesis "$\mu$ is reflection positive for $\theta$". For SU(2) Wilson measures on $a\mathbb Z^4$ it holds at site and link mirrors (`library/cl1.md` Lemma 3; `gap-transfer.md` section 1 for the torus with a finite time circle).
- $u(F,G;t)=\mathbb E[\overline{\Theta F}\,\tau_tG]-\mathbb E[\overline{\Theta F}]\,\mathbb E[G]$, the usual truncated function of the pair $(\overline{\Theta F},G)$ at time distance $t$.

S.5. **Instance (S): Schwinger functions.** $\mathcal V$ is the span of separated tuples supported in $\{x_4>0\}$ (with the empty tuple $1$), $b(F,G)=\sigma(\theta\bar F\cdot G)$, as in `library/cl1.md` (16). There (P1) is its Lemma 3, (P2) is translation invariance with $\theta\tau_t=\tau_{-t}\theta$, (P3) is its position-independent bound (4) (with $k_F=0$), and (P4) is its equations (6)-(7). So statement (1) in this instance is CL1 Lemma 5.

## A. Three general lemmas (proved here)

Throughout, $\mathcal K$ is a complex Hilbert space, $\langle\cdot,\cdot\rangle$ antilinear in the first slot.

**Lemma A1 (Hermitian form, Cauchy-Schwarz). Uses (P1) only.** For all $F,G\in\mathcal V$: $b(F,G)=\overline{b(G,F)}$ and $|b(F,G)|^2\le b(F,F)\,b(G,G)$.

Proof. A1.1. Put $q(F)=b(F,F)$, real by (P1). Expanding, $q(F+zG)=q(F)+z\,b(F,G)+\bar z\,b(G,F)+|z|^2q(G)$. Summing with weights $i^{-k}$ over $z=i^k$, $k=0,1,2,3$: $\sum_ki^{-k}q(F+i^kG)=4b(F,G)$, because $\sum_ki^{-k}=0$, $\sum_ki^{-k}i^k=4$, $\sum_ki^{-k}i^{-k}=\sum_k(-1)^k=0$.
A1.2. So $\overline{b(G,F)}=\frac14\sum_ki^{k}q(G+i^kF)$. Since $q(cX)=|c|^2q(X)$, $q(G+i^kF)=q(i^k(F+i^{-k}G))=q(F+i^{-k}G)$. Substituting $j=-k$ mod 4 gives $\overline{b(G,F)}=\frac14\sum_ji^{-j}q(F+i^jG)=b(F,G)$.
A1.3. By A1.1-A1.2, $0\le q(F+zG)=q(F)+2\operatorname{Re}(z\,b(F,G))+|z|^2q(G)$. If $q(G)=0$, take $z=-s\overline{b(F,G)}$, $s>0$: $0\le q(F)-2s|b(F,G)|^2$ for all $s$, so $b(F,G)=0$. If $q(G)>0$, take $z=-\overline{b(F,G)}/q(G)$: $0\le q(F)-|b(F,G)|^2/q(G)$. ∎

**Lemma A2 (log-convexity of a self-adjoint semigroup).** Let $T_t$ ($t\in\mathbb T_+$) be bounded self-adjoint operators on $\mathcal K$ with $T_0=1$, $T_sT_t=T_{s+t}$. Let $\psi\in\mathcal K$, $h\in\mathbb T_+$ with $h>0$, $\rho\ge0$, $C<\infty$, and suppose $\|T_{kh}\psi\|\le C\rho^k$ for infinitely many $k\in\mathbb N$. Then $\|T_h\psi\|\le\rho\|\psi\|$.

Proof. A2.1. Put $g_k=\|T_{kh}\psi\|^2$, $k\ge0$. For $k\ge1$, self-adjointness and the semigroup law give $g_k=\langle\psi,T_{2kh}\psi\rangle=\langle T_{(k-1)h}\psi,T_{(k+1)h}\psi\rangle$, so by Cauchy-Schwarz $g_k^2\le g_{k-1}g_{k+1}$.
A2.2. If $\psi=0$ or $g_1=0$ there is nothing to prove. Otherwise every $g_k>0$: if $j\ge2$ were the least index with $g_j=0$, then $g_{j-1}^2\le g_{j-2}g_j=0$, against minimality.
A2.3. Then $r_k=g_k/g_{k-1}$ satisfies $r_k\le r_{k+1}$ (divide A2.1 by $g_{k-1}g_k$). So $g_k=g_0r_1r_2\cdots r_k\ge g_0r_1^k$, and $r_1\le(g_k/g_0)^{1/k}\le(C^2\rho^{2k}/g_0)^{1/k}$ for the infinitely many $k$ of the hypothesis. The right side tends to $\rho^2$. So $g_1\le\rho^2g_0$. ∎

**Lemma A3 (facts on self-adjoint operators).** Definitions: an operator $A$ is a linear map from a subspace $D(A)\subset\mathcal K$ to $\mathcal K$. If $D(A)$ is dense, $D(A^*)$ is the set of $\chi$ for which some $\eta$ satisfies $\langle\chi,A\varphi\rangle=\langle\eta,\varphi\rangle$ for all $\varphi\in D(A)$, and $A^*\chi=\eta$ ($\eta$ is unique by density). $A$ is self-adjoint if $D(A^*)=D(A)$ and $A^*=A$. The resolvent set $\rho(A)$ is the set of $\lambda\in\mathbb C$ for which $A-\lambda:D(A)\to\mathcal K$ is bijective with a bounded inverse; $\operatorname{spec}(A)=\mathbb C\setminus\rho(A)$. "$A\ge c$" means $\langle\varphi,A\varphi\rangle\ge c\|\varphi\|^2$ for $\varphi\in D(A)$. Let $A$ be self-adjoint and $\mathcal K\ne\{0\}$.
(a) $A$ is closed: $\varphi_n\to\varphi$, $A\varphi_n\to y$ imply $\varphi\in D(A)$, $A\varphi=y$.
(b) If $\lambda\in\mathbb C$, $c>0$, $\|(A-\lambda)\varphi\|\ge c\|\varphi\|$ for all $\varphi\in D(A)$, and $\ker(A-\bar\lambda)=\{0\}$, then $\lambda\in\rho(A)$ and $\|(A-\lambda)^{-1}\|\le1/c$.
(c) If $\mu:=\inf\{\langle\varphi,A\varphi\rangle:\varphi\in D(A),\|\varphi\|=1\}>-\infty$, then $\mu\in\operatorname{spec}(A)$.
(d) If $A=B$ is bounded with $D(B)=\mathcal K$: $\|B\|=\sup_{\|\varphi\|=1}|\langle\varphi,B\varphi\rangle|$; and for $r\ge0$, $\operatorname{spec}(B)\subset[-r,r]$ if and only if $\|B\|\le r$. In particular $\operatorname{spec}(B)$ is a nonempty subset of $[-\|B\|,\|B\|]$.
(e) For $B$ as in (d) and a real polynomial $q$: $\|q(B)\|\le\sup_{x\in\operatorname{spec}(B)}|q(x)|$.
(f) If $A\ge0$, then $-1\in\rho(A)$; $R:=(A+1)^{-1}$ is bounded, self-adjoint, $\langle g,Rg\rangle\ge0$, $\|R\|\le1$; $\ker A=\ker(R-1)$; and for $\lambda\ne-1$: $\lambda\in\operatorname{spec}(A)$ if and only if $(1+\lambda)^{-1}\in\operatorname{spec}(R)$.

Proof. A3.1. (a): The set $\{(\chi,A^*\chi):\chi\in D(A^*)\}$ is closed in $\mathcal K\times\mathcal K$, since each condition $\langle\chi,A\varphi\rangle=\langle\eta,\varphi\rangle$ is closed in $(\chi,\eta)$. It is the graph of $A$.
A3.2. (b): The inequality gives injectivity. Range closed: if $(A-\lambda)\varphi_n\to y$, then $(\varphi_n)$ is Cauchy, $\varphi_n\to\varphi$, $A\varphi_n\to y+\lambda\varphi$, so by (a) $(A-\lambda)\varphi=y$. Range dense: if $y\perp(A-\lambda)D(A)$ then $\langle y,A\varphi\rangle=\langle\bar\lambda y,\varphi\rangle$ for all $\varphi\in D(A)$, so $y\in D(A^*)=D(A)$ with $Ay=\bar\lambda y$, hence $y=0$. So $A-\lambda$ is bijective; the inequality bounds the inverse by $1/c$.
A3.3. (c): $\mu$ is real. Suppose $\mu\in\rho(A)$, $S:=(A-\mu)^{-1}$. For $x=(A-\mu)\varphi$, $y=(A-\mu)\chi$: $\langle x,Sy\rangle=\langle(A-\mu)\varphi,\chi\rangle=\langle\varphi,(A-\mu)\chi\rangle=\langle Sx,y\rangle$ ($A$ symmetric, $\mu$ real), and $\langle x,Sx\rangle=\langle\varphi,(A-\mu)\varphi\rangle\ge0$. So $S$ is a bounded positive form and Cauchy-Schwarz $|\langle x,Sy\rangle|^2\le\langle x,Sx\rangle\langle y,Sy\rangle$ holds (A1.3 for the form $(x,y)\mapsto\langle x,Sy\rangle$). Take unit $\varphi_n\in D(A)$ with $\langle\varphi_n,(A-\mu)\varphi_n\rangle\to0$ and $y_n=(A-\mu)\varphi_n$, so $Sy_n=\varphi_n$. Then $1=|\langle\varphi_n,Sy_n\rangle|^2\le\langle\varphi_n,S\varphi_n\rangle\langle y_n,Sy_n\rangle\le\|S\|\langle\varphi_n,(A-\mu)\varphi_n\rangle\to0$. Contradiction.
A3.4. (d), first claim: let $s$ be the supremum. $s\le\|B\|$. For unit $x,y$ choose $|\omega|=1$ with $\langle x,B\omega y\rangle\ge0$ and put $y'=\omega y$. Since $\langle y',Bx\rangle=\overline{\langle x,By'\rangle}$: $4\operatorname{Re}\langle x,By'\rangle=\langle x+y',B(x+y')\rangle-\langle x-y',B(x-y')\rangle\le s(\|x+y'\|^2+\|x-y'\|^2)=4s$. So $|\langle x,By\rangle|\le s$; with $x=By/\|By\|$, $\|By\|\le s$.
A3.5. (d), second claim. If $\|B\|\le r$ and $\lambda\notin[-r,r]$: for real $\lambda$, $\|(B-\lambda)\varphi\|\ge(|\lambda|-\|B\|)\|\varphi\|$; for non-real $\lambda$, $\|(B-\lambda)\varphi\|\|\varphi\|\ge|\operatorname{Im}\langle\varphi,(B-\lambda)\varphi\rangle|=|\operatorname{Im}\lambda|\|\varphi\|^2$. The same bounds hold at $\bar\lambda$, so (b) gives $\lambda\in\rho(B)$. Conversely, if $\operatorname{spec}(B)\subset[-r,r]$: by (c) for $B$ and for $-B$ (note $\operatorname{spec}(-B)=-\operatorname{spec}(B)$), the infimum and the supremum of $\langle\varphi,B\varphi\rangle$ over unit $\varphi$ lie in $[-r,r]$, so $\|B\|\le r$ by A3.4. Nonempty: (c) puts the infimum in the spectrum.
A3.6. (e): $q(B)$ is bounded self-adjoint. Let $M=\sup_{\operatorname{spec}(B)}|q|$, finite by (d). Claim $\operatorname{spec}(q(B))\subset q(\operatorname{spec}(B))\subset[-M,M]$; then (d) gives $\|q(B)\|\le M$. If $q\equiv c$ is constant, $q(B)-\nu=(c-\nu)1$ is invertible for $\nu\ne c$, and $c\in q(\operatorname{spec}B)$ because $\operatorname{spec}B\ne\emptyset$. If $\deg q=k\ge1$ and $\nu\notin q(\operatorname{spec}B)$, write $q(x)-\nu=c\prod_{i=1}^k(x-z_i)$, $c\ne0$. No $z_i$ lies in $\operatorname{spec}B$, since $q(z_i)=\nu$. So $q(B)-\nu=c\prod_i(B-z_i)$ is a product of bijections with bounded inverses.
A3.7. (f): $\|(A+1)\varphi\|\|\varphi\|\ge\langle\varphi,(A+1)\varphi\rangle\ge\|\varphi\|^2$, and the same for $\bar\lambda=-1$, so (b) gives $-1\in\rho(A)$, $\|R\|\le1$. Self-adjointness and positivity of $R$: as for $S$ in A3.3, with $\mu=-1$. Kernel: $A\varphi=0$ iff $(A+1)\varphi=\varphi$ iff $\varphi=R\varphi$ (and then $\varphi\in RD=D(A)$). Correspondence: for $\varphi\in D(A)$, $(1-(1+\lambda)R)(A+1)\varphi=(A+1)\varphi-(1+\lambda)\varphi=(A-\lambda)\varphi$. Since $A+1:D(A)\to\mathcal K$ is a bijection with bounded inverse $R$, $A-\lambda$ is a bijection with bounded inverse iff $1-(1+\lambda)R$ is one; the inverses are related by $(A-\lambda)^{-1}=R(1-(1+\lambda)R)^{-1}$ and $(1-(1+\lambda)R)^{-1}=1+(1+\lambda)(A-\lambda)^{-1}$ (check: $(1-(1+\lambda)R)(1+(1+\lambda)(A-\lambda)^{-1})=1+(1+\lambda)[(A-\lambda)^{-1}-R-(1+\lambda)R(A-\lambda)^{-1}]$, and the bracket is $R[(A+1)-(A-\lambda)-(1+\lambda)](A-\lambda)^{-1}=0$; the other order is the same computation). Finally $1-(1+\lambda)R=(1+\lambda)((1+\lambda)^{-1}-R)$. ∎

## 1. Statement (1): Hilbert space, semigroup, Hamiltonian, vacuum

**Statement (1).** Let $\mathfrak D=(\mathcal V,b,\tau,1)$ be a datum (S.2).
(1a) *Uses (P1).* $\mathcal N=\{F:b(F,F)=0\}$ is a subspace and equals $\{F:b(G,F)=0\ \forall G\}$. $\langle[F],[G]\rangle:=b(F,G)$ is a well-defined inner product on $\mathcal V/\mathcal N$. Let $\mathcal H$ be the completion and $[F]$ the class of $F$. The vacuum $\Omega:=[1]$ has $\|\Omega\|=1$, and $\langle\Omega,[G]\rangle=b(1,G)$.
(1b) *Uses (P1), (P2), (P3).* For $t\in\mathbb T_+$, $\|[\tau_tF]\|\le\|[F]\|$, so $\tau_t\mathcal N\subset\mathcal N$ and $[F]\mapsto[\tau_tF]$ extends to a bounded operator $T_t$ on $\mathcal H$. Each $T_t$ is self-adjoint with $\|T_t\|\le1$; $T_0=1$, $T_sT_t=T_{s+t}$, $T_t\Omega=\Omega$, $T_{2t}=T_t^*T_t\ge0$, and $\langle[F],T_t[G]\rangle=b(F,\tau_tG)$. With $Q:=1-|\Omega\rangle\langle\Omega|$: $QT_t=T_tQ$ and
$$u(F,G;t)=\langle Q[F],T_tQ[G]\rangle,\qquad u(F,F;0)=\|Q[F]\|^2=b(F,F)-|b(1,F)|^2 .$$
(1c) *Uses (P1)-(P4), $\mathbb T=\mathbb R$.* $t\mapsto T_t\psi$ is continuous on $[0,\infty)$ for each $\psi$. Define $D(H)$ as the set of $\psi$ for which $\lim_{h\downarrow0}h^{-1}(\psi-T_h\psi)$ exists, and $H\psi$ as the limit. Then: $H$ is self-adjoint and $H\ge0$; $H\Omega=0$; $T_tD(H)\subset D(H)$ with $HT_t\varphi=T_tH\varphi$ and $\frac{d}{dt}T_t\varphi=-HT_t\varphi$ for $\varphi\in D(H)$; $\ker H=\{\psi:T_t\psi=\psi\ \forall t\ge0\}$; and $(T_t)$ is the only family of operators with $\|S_t\|\le1$, $S_0=1$, $S_sS_t=S_{s+t}$, $t\mapsto S_t\psi$ continuous, whose generator (defined in the same way) is $H$. We write $T_t=e^{-tH}$.
(1d) *Lattice, $\mathbb T=a\mathbb Z$, uses (P1)-(P3).* $T:=T_a$ is a self-adjoint contraction with $T_{na}=T^n$ and $T^2\ge0$. No Hamiltonian is defined here; the gap is stated for $T$ (Lemma E, E3). If $T\ge0$ and $\ker T=0$, then $-a^{-1}\log T$ is defined by functional calculus; this file does not use it.

**Proof.**
1.1. (1a): by Lemma A1, $F\in\mathcal N$ iff $b(G,F)=0$ for all $G$ (one direction is A1.3, the other takes $G=F$). This set is a subspace. If $F-F',G-G'\in\mathcal N$ then $b(F,G)=b(F',G')$, so the form is well defined; it is Hermitian (A1.2), positive, and definite on the quotient. $\|\Omega\|^2=b(1,1)=1$.
1.2. (1b), the contraction. Fix $F$ and put $a(t)=\|[\tau_tF]\|=b(\tau_tF,\tau_tF)^{1/2}$ (real by (P1)). (P2) with $G=\tau_tF$ gives $b(\tau_tF,\tau_tF)=b(F,\tau_{2t}F)$. Lemma A1 gives $a(t)^2\le a(0)a(2t)$.
1.3. If $a(0)=0$ then $a(t)=0$. Otherwise iterate 1.2 $r$ times: $a(t)\le a(0)^{1-2^{-r}}a(2^rt)^{2^{-r}}$. By (P3), $a(2^rt)^{2^{-r}}\le\big(C_F(1+2^rt)^{k_F}\big)^{2^{-r-1}}$, whose logarithm $2^{-r-1}(\log C_F+k_F\log(1+2^rt))$ tends to $0$ (if $C_F=0$, $a(2^rt)=0$ and then $a(t)=0$). Letting $r\to\infty$: $a(t)\le a(0)$. This is the argument of `cl1.md` (18).
1.4. So $\tau_t\mathcal N\subset\mathcal N$ and $[F]\mapsto[\tau_tF]$ is a well-defined linear contraction on the dense subspace $\mathcal V/\mathcal N$; it extends uniquely to $T_t$ with $\|T_t\|\le1$. $\langle[F],T_t[G]\rangle=b(F,\tau_tG)=b(\tau_tF,G)=\langle T_t[F],[G]\rangle$ by (P2); both sides are continuous in each argument, so $T_t$ is self-adjoint. The semigroup law, $T_0=1$ and $T_t\Omega=\Omega$ hold on classes and pass to the closure. $T_{2t}=T_tT_t=T_t^*T_t$.
1.5. $Q$ and $T_t$: $T_tQ\psi=T_t\psi-\langle\Omega,\psi\rangle\Omega$ and $QT_t\psi=T_t\psi-\langle\Omega,T_t\psi\rangle\Omega=T_t\psi-\langle T_t\Omega,\psi\rangle\Omega$, equal. Then $\langle Q[F],T_tQ[G]\rangle=\langle[F],T_tQ[G]\rangle=\langle[F],T_t[G]\rangle-\langle\Omega,[G]\rangle\langle[F],\Omega\rangle=b(F,\tau_tG)-b(1,G)\,b(F,1)$, using $Q^2=Q=Q^*$ and $\langle[F],\Omega\rangle=b(F,1)$.
1.6. (1c), continuity. $\|T_s[F]-[F]\|^2=b(F,\tau_{2s}F)-2\operatorname{Re}b(F,\tau_sF)+b(F,F)\to0$ as $s\downarrow0$ by (P4) (first term by 1.2). For $\psi\in\mathcal H$ and $\varepsilon>0$ pick $[F]$ with $\|\psi-[F]\|<\varepsilon$; then $\|T_s\psi-\psi\|\le2\varepsilon+\|T_s[F]-[F]\|$. So $T_s\psi\to\psi$. At $t>0$: $\|T_{t+h}\psi-T_t\psi\|\le\|T_h\psi-\psi\|$ and, for $0<h\le t$, $\|T_{t-h}\psi-T_t\psi\|=\|T_{t-h}(\psi-T_h\psi)\|\le\|\psi-T_h\psi\|$.
1.7. Generator calculus. Let $\varphi\in D(H)$, $t\ge0$. $h^{-1}(T_t\varphi-T_hT_t\varphi)=T_th^{-1}(\varphi-T_h\varphi)\to T_tH\varphi$, so $T_t\varphi\in D(H)$, $HT_t\varphi=T_tH\varphi$. The right difference quotient $h^{-1}(T_{t+h}\varphi-T_t\varphi)=-T_th^{-1}(\varphi-T_h\varphi)\to-T_tH\varphi$. For $t>0$ the left one is $-T_{t-h}h^{-1}(\varphi-T_h\varphi)=-T_{t-h}H\varphi-T_{t-h}[h^{-1}(\varphi-T_h\varphi)-H\varphi]$; the first term tends to $-T_tH\varphi$ by 1.6 and the second has norm at most $\|h^{-1}(\varphi-T_h\varphi)-H\varphi\|\to0$. So $\frac d{dt}T_t\varphi=-T_tH\varphi$, continuous in $t$.
1.8. The resolvent. For $\psi\in\mathcal H$, $s\mapsto e^{-s}T_s\psi$ is continuous with norm $\le e^{-s}\|\psi\|$. Its Riemann integrals over $[0,N]$ exist (uniform continuity on $[0,N]$, completeness) and converge as $N\to\infty$ (the tails have norm $\le e^{-N}\|\psi\|$). Put $R\psi=\int_0^\infty e^{-s}T_s\psi\,ds$. $R$ is linear, $\|R\|\le1$, and $\langle\chi,R\psi\rangle=\int_0^\infty e^{-s}\langle\chi,T_s\psi\rangle ds$ (the inner product passes through Riemann sums and limits). Hence $R$ is self-adjoint ($\langle\chi,T_s\psi\rangle=\langle T_s\chi,\psi\rangle$). Two vectors with the same inner products with every $\chi$ are equal; this is how the identities below are checked.
1.9. $R\psi\in D(H)$ and $HR\psi=\psi-R\psi$. Substituting $u=s+h$ in the scalar integrals: $T_hR\psi=e^h\int_h^\infty e^{-u}T_u\psi\,du$. So $h^{-1}(R\psi-T_hR\psi)=h^{-1}\int_0^he^{-u}T_u\psi\,du-h^{-1}(e^h-1)\int_h^\infty e^{-u}T_u\psi\,du$. The first term tends to $\psi$, since its distance to $\psi$ is at most $\sup_{0\le u\le h}\|e^{-u}T_u\psi-\psi\|$. The second tends to $R\psi$.
1.10. $RH\varphi=\varphi-R\varphi$ for $\varphi\in D(H)$. For $\chi\in\mathcal H$ the function $g(s)=\langle\chi,T_s\varphi\rangle$ is $C^1$ with $g'(s)=-\langle\chi,T_sH\varphi\rangle$ (1.7). Integration by parts on $[0,N]$ gives $\int_0^Ne^{-s}g'=e^{-N}g(N)-g(0)+\int_0^Ne^{-s}g$. As $N\to\infty$ ($|g|\le\|\chi\|\|\varphi\|$): $-\langle\chi,RH\varphi\rangle=-\langle\chi,\varphi\rangle+\langle\chi,R\varphi\rangle$.
1.11. By 1.9-1.10, $1+H:D(H)\to\mathcal H$ is a bijection with inverse $R$, and $D(H)=R\mathcal H$. $D(H)$ is dense: if $\chi\perp R\mathcal H$ then $\langle R\chi,\psi\rangle=\langle\chi,R\psi\rangle=0$ for all $\psi$, so $R\chi=0$ and $\chi=(1+H)R\chi=0$.
1.12. Self-adjoint. Symmetric: for $\chi,\varphi\in D(H)$, $\langle\chi,H\varphi\rangle=\lim\langle\chi,h^{-1}(\varphi-T_h\varphi)\rangle=\lim\langle h^{-1}(\chi-T_h\chi),\varphi\rangle=\langle H\chi,\varphi\rangle$. So $D(H)\subset D(H^*)$ and $H^*=H$ there. If $\chi\in D(H^*)$ with $\langle\chi,H\varphi\rangle=\langle\eta,\varphi\rangle$ for all $\varphi\in D(H)$, then $\langle\chi,(1+H)\varphi\rangle=\langle\chi+\eta,\varphi\rangle$; with $\varphi=R\psi$ this reads $\langle\chi,\psi\rangle=\langle R(\chi+\eta),\psi\rangle$ for all $\psi$. So $\chi=R(\chi+\eta)\in D(H)$, and $H\chi=(\chi+\eta)-\chi=\eta$.
1.13. $H\ge0$: $\langle\varphi,H\varphi\rangle=\lim h^{-1}(\|\varphi\|^2-\langle\varphi,T_h\varphi\rangle)\ge0$ since $\|T_h\|\le1$. $H\Omega=0$ since $T_h\Omega=\Omega$. Kernel: if $T_t\psi=\psi$ for all $t$, then $\psi\in D(H)$ and $H\psi=0$. If $H\psi=0$, then $\frac d{dt}T_t\psi=-T_tH\psi=0$, so for every $\chi$ the scalar $\langle\chi,T_t\psi\rangle$ is constant (mean value theorem on real and imaginary parts) and $T_t\psi=\psi$.
1.14. Uniqueness. Let $(S_t)$ be as in (1c) with generator $H$. By 1.7 applied to $S$, $S_s\varphi\in D(H)$ and $\frac d{ds}S_s\varphi=-HS_s\varphi$ for $\varphi\in D(H)$. Fix $t>0$ and put $w(s)=T_{t-s}S_s\varphi$, $0\le s\le t$. For $0<s<t$ and small $h$ of either sign, $h^{-1}(w(s+h)-w(s))=T_{t-s-h}\,h^{-1}(S_{s+h}\varphi-S_s\varphi)+h^{-1}(T_{t-s-h}-T_{t-s})S_s\varphi$. The first term tends to $-T_{t-s}HS_s\varphi$ (the operators $T_r$ are uniformly bounded and strongly continuous, and the vectors converge). The second tends to $+T_{t-s}HS_s\varphi$ by 1.7 at the point $t-s$ with $S_s\varphi\in D(H)$. So $w'=0$ on $(0,t)$; $w$ is continuous on $[0,t]$; hence $w(0)=w(t)$, i.e. $T_t\varphi=S_t\varphi$. By density of $D(H)$ and boundedness, $T_t=S_t$.
1.15. (1d): 1.1-1.5 hold for $\mathbb T=a\mathbb Z$ unchanged; $T_{na}=T^n$ by the semigroup law and $T^2=T^*T\ge0$. For the SU(2) Wilson transfer operator, $\mathsf T_P=\hat S^*\hat S\ge0$ (`gap-transfer.md` step 3.3, as used in its 6.1). ∎

## E. Lemma E: the gap as a semigroup bound and as a spectral statement

Fix a datum with (P1)-(P3), its $\mathcal H,\Omega,T_t,Q$ from (1), and $m>0$. Define:
- **(V)** $\{\psi\in\mathcal H:T_t\psi=\psi\ \forall t\in\mathbb T_+\}=\mathbb C\Omega$ (the vacuum is the only invariant vector);
- **(G$_m$)** $\|T_t\psi\|\le e^{-mt}\|\psi\|$ for all $\psi\in\Omega^\perp$ and $t\in\mathbb T_+$ (semigroup form of the gap).

For $\mathbb T=\mathbb R$ with (P4), let $H'$ be $H$ restricted to $D(H')=D(H)\cap\Omega^\perp$, an operator on the Hilbert space $\Omega^\perp$.

**Lemma E.**
(E1) (G$_m$) implies (V).
(E2) $\mathbb T=\mathbb R$, (P4). $H'$ is self-adjoint on $\Omega^\perp$, and the following are equivalent: (i) (G$_m$); (ii) $\langle\varphi,H\varphi\rangle\ge m\|\varphi\|^2$ for $\varphi\in D(H')$; (iii) $\operatorname{spec}(H')\subset[m,\infty)$; (iv) (V) and $\operatorname{spec}(H)\subset\{0\}\cup[m,\infty)$. Form (iv) is the hypothesis of row item (2).
(E3) $\mathbb T=a\mathbb Z$, $T=T_a$. (G$_m$) $\iff$ $\|T|_{\Omega^\perp}\|\le e^{-ma}$ $\iff$ $\operatorname{spec}(T|_{\Omega^\perp})\subset[-e^{-ma},e^{-ma}]$.

**Proof.**
E.1. $T_t\Omega^\perp\subset\Omega^\perp$ by 1.5. If $T_t\psi=\psi$ for all $t$, then $Q\psi$ is invariant and in $\Omega^\perp$, so $\|Q\psi\|\le e^{-mt}\|Q\psi\|$ for $t>0$ in $\mathbb T_+$, so $Q\psi=0$. This is (E1).
E.2. $H'$ maps into $\Omega^\perp$: $\langle\Omega,H\varphi\rangle=\langle H\Omega,\varphi\rangle=0$. Since $\Omega\in D(H)$, $QD(H)\subset D(H)$, so $D(H)=\mathbb C\Omega\oplus D(H')$ and $D(H')=QD(H)$ is dense in $\Omega^\perp$. $H'$ is symmetric. If $\chi,\eta\in\Omega^\perp$ and $\langle\chi,H'\varphi\rangle=\langle\eta,\varphi\rangle$ for $\varphi\in D(H')$, then for $\varphi=c\Omega+\varphi'\in D(H)$: $\langle\chi,H\varphi\rangle=\langle\chi,H'\varphi'\rangle=\langle\eta,\varphi'\rangle=\langle\eta,\varphi\rangle$. So $\chi\in D(H)\cap\Omega^\perp$ with $H\chi=\eta$. Hence $H'$ is self-adjoint.
E.3. (i)$\Rightarrow$(ii). For $\varphi\in D(H')$: $\langle\varphi,T_h\varphi\rangle=\|T_{h/2}\varphi\|^2\le e^{-mh}\|\varphi\|^2$, so $\langle\varphi,H\varphi\rangle=\lim_{h\downarrow0}h^{-1}(\|\varphi\|^2-\langle\varphi,T_h\varphi\rangle)\ge\lim h^{-1}(1-e^{-mh})\|\varphi\|^2=m\|\varphi\|^2$.
E.4. (ii)$\Rightarrow$(iii). For real $\lambda<m$: $\|(H'-\lambda)\varphi\|\|\varphi\|\ge\langle\varphi,(H'-\lambda)\varphi\rangle\ge(m-\lambda)\|\varphi\|^2$. For non-real $\lambda$: $\|(H'-\lambda)\varphi\|\|\varphi\|\ge|\operatorname{Im}\langle\varphi,(H'-\lambda)\varphi\rangle|=|\operatorname{Im}\lambda|\|\varphi\|^2$. Both bounds hold at $\bar\lambda$ too, so Lemma A3(b) on $\Omega^\perp$ gives $\lambda\in\rho(H')$.
E.5. (iii)$\Rightarrow$(ii). $H'\ge0$ (1.13). If $\Omega^\perp=\{0\}$ there is nothing to prove. Otherwise by A3(c) the infimum $\mu$ of $\langle\varphi,H'\varphi\rangle$ over unit $\varphi\in D(H')$ lies in $\operatorname{spec}(H')\subset[m,\infty)$.
E.6. (ii)$\Rightarrow$(i). Let $\varphi\in D(H')$ and $f(t)=\|T_t\varphi\|^2$. By 1.7, $T_t\varphi\in D(H)\cap\Omega^\perp$ and $\frac d{dt}T_t\varphi=-HT_t\varphi$. Expanding $\langle w(t+h),w(t+h)\rangle-\langle w(t),w(t)\rangle$ for $w(t)=T_t\varphi$ gives $f'(t)=-2\langle T_t\varphi,HT_t\varphi\rangle\le-2mf(t)$. So $(e^{2mt}f)'\le0$ and $f(t)\le e^{-2mt}f(0)$ (mean value theorem). Both sides of $\|T_t\psi\|\le e^{-mt}\|\psi\|$ are continuous in $\psi$, and $D(H')$ is dense in $\Omega^\perp$ (E.2).
E.7. (iii)$\Rightarrow$(iv). If $T_t\psi=\psi$ for all $t$, then $H\psi=0$ (1.13), $HQ\psi=0$, so $Q\psi\in\ker H'=\{0\}$ ($0\in\rho(H')$ as $m>0$): (V). For $\lambda\notin\{0\}\cup[m,\infty)$, $H-\lambda$ acts as $-\lambda$ on $\mathbb C\Omega$ and as $H'-\lambda$ on $D(H')$; the map $\psi\mapsto-\lambda^{-1}\langle\Omega,\psi\rangle\Omega+(H'-\lambda)^{-1}Q\psi$ is a bounded two-sided inverse.
E.8. (iv)$\Rightarrow$(iii); this excludes a non-eigenvalue spectral point of $H'$ at $0$. Let $R=(H+1)^{-1}$ (A3(f)) and $\alpha=(1+m)^{-1}<1$. Claim: $\operatorname{spec}(R)\subset[0,\alpha]\cup\{1\}$. By A3(d), $\operatorname{spec}(R)\subset[-1,1]$. For $\lambda\in\operatorname{spec}(R)$, $\lambda\ne0$, A3(f) gives $\lambda^{-1}-1\in\operatorname{spec}(H)\subset\{0\}\cup[m,\infty)$; so $\lambda=1$ or $0<\lambda\le\alpha$ (a negative $\lambda$ would give $\lambda^{-1}-1<-1$).
E.9. For $k,j\ge0$, A3(e) with $q(x)=x^k-x^{k+j}$ gives $\|R^k-R^{k+j}\|\le\sup_{[0,\alpha]\cup\{1\}}|x^k(1-x^j)|\le\alpha^k$. So $R^k$ converges in norm to a bounded self-adjoint $P$ with $P^2=\lim R^{2k}=P$ and $RP=\lim R^{k+1}=P$. Likewise $\|R-R^{k+1}\|\le\sup_{[0,\alpha]\cup\{1\}}|x(1-x^k)|\le\alpha$, so $\|R(1-P)\|\le\alpha$.
E.10. $RP=P$ gives $P\mathcal H\subset\ker(R-1)=\ker H$ (A3(f)), and $\ker H$ is the set of invariant vectors (1.13), which is $\mathbb C\Omega$ by (V). $R\Omega=\Omega$ because $(H+1)\Omega=\Omega$, so $P\Omega=\Omega$. Hence $P=|\Omega\rangle\langle\Omega|$ and $1-P=Q$.
E.11. $R$ maps $\Omega^\perp$ into $D(H')$, and $R':=R|_{\Omega^\perp}$ inverts $H'+1$ on $\Omega^\perp$. By E.9-E.10, $\|R'\|\le\alpha$, so $\operatorname{spec}(R')\subset[-\alpha,\alpha]$ (A3(d)). $H'\ge0$ gives $\operatorname{spec}(H')\subset[0,\infty)$ (E.4 with $m=0$). For $\lambda\in\operatorname{spec}(H')$, A3(f) applied to $H'$ gives $(1+\lambda)^{-1}\in\operatorname{spec}(R')$, so $(1+\lambda)^{-1}\le\alpha$, i.e. $\lambda\ge m$.
E.12. (E3): (G$_m$) at $t=a$ is the norm bound. Conversely $\Omega^\perp$ is $T$-invariant, so $\|T^n\psi\|\le\|T|_{\Omega^\perp}\|^n\|\psi\|$. The last equivalence is A3(d) for the bounded self-adjoint $T|_{\Omega^\perp}$. ∎

## 2. Statement (2): a gap gives exponential decay

**Statement (2).** *Uses (P1), (P2), (P3) and (G$_m$).* For $\mathbb T=\mathbb R$ with (P4), (G$_m$) may be replaced by the row's hypothesis "(V) and $\operatorname{spec}(H)\subset\{0\}\cup[m,\infty)$" (Lemma E2, (iv)$\Rightarrow$(i)); for $\mathbb T=a\mathbb Z$, by $\operatorname{spec}(T|_{\Omega^\perp})\subset[-e^{-ma},e^{-ma}]$ (E3).
(2a) For all $F,G\in\mathcal V$ and $t\in\mathbb T_+$:
$$|u(F,G;t)|\le e^{-mt}\,\|Q[F]\|\,\|Q[G]\|\le e^{-mt}\,b(F,F)^{1/2}\,b(G,G)^{1/2},\qquad\|Q[F]\|^2=u(F,F;0)=b(F,F)-|b(1,F)|^2 .$$
(2b) (*monotonicity*) For each $F$, $t\mapsto e^{mt}u(F,F;t)$ is nonnegative and nonincreasing on $2\mathbb T_+$ (on all of $\mathbb R_+$ if $\mathbb T=\mathbb R$).
(2c) Instance (M). Put $\Sigma_-=\{\theta(E):E\in\Sigma_+\}$. For $A\in L^2(\Sigma_-)$, $B\in L^2(\Sigma_+)$, $t\in\mathbb T_+$:
$$\big|\mathbb E[A\,\tau_tB]-\mathbb E[A]\,\mathbb E[B]\big|\le e^{-mt}\,\sigma_A\sigma_B\le e^{-mt}\|A\|_2\|B\|_2,\qquad\sigma_A^2=\mathbb E|A|^2-|\mathbb E A|^2 .$$
By invariance of $\mu$ the same holds for $\tau_sA$ and $\tau_{s+t}B$, any $s\in\mathbb T$: observables separated by a time slab of width $t$.

**Proof.**
2.1. (2a): By 1.5, $u(F,G;t)=\langle Q[F],T_tQ[G]\rangle$. $Q[G]\in\Omega^\perp$, so $\|T_tQ[G]\|\le e^{-mt}\|Q[G]\|$, and Cauchy-Schwarz gives the first bound. $\|Q[F]\|\le\|[F]\|=b(F,F)^{1/2}$.
2.2. (2b): for $\sigma\le\sigma'$ in $\mathbb T_+$, $u(F,F;2\sigma)=\|T_\sigma Q[F]\|^2$ and $u(F,F;2\sigma')=\|T_{\sigma'-\sigma}T_\sigma Q[F]\|^2\le e^{-2m(\sigma'-\sigma)}u(F,F;2\sigma)$, because $T_\sigma Q[F]\in\Omega^\perp$.
2.3. (2c): $F:=\overline{\Theta A}$ is $\Sigma_+$-measurable (for a Borel set $U$, $F^{-1}(\bar U)=\theta^{-1}(A^{-1}(U))$ and $A^{-1}(U)=\theta(E)$ with $E\in\Sigma_+$, $\theta$ an involution) and $\|F\|_2=\|A\|_2$ ($\theta$ preserves $\mu$). $\overline{\Theta F}=A$. So $b(F,\tau_tB)=\mathbb E[A\tau_tB]$, $b(F,1)=\mathbb E[A]$, $b(1,B)=\mathbb E[B]$, and (2a) gives the bound with $\|Q[F]\|\|Q[B]\|$. Finally $\|Q[F]\|^2=\mathbb E[A\,\overline{\Theta A}]-|\mathbb E A|^2\le\mathbb E|A|^2-|\mathbb EA|^2$ by Cauchy-Schwarz and $\|\Theta A\|_2=\|A\|_2$; likewise $\|Q[B]\|^2\le\sigma_B^2$. ∎

**Remark 2.4.** The constant is $\|Q[F]\|\|Q[G]\|$: no growth, clustering or rotation property enters. In the lattice compact case this is `gap-transfer.md` (6b) and the finite-dimensional lemma (B) of `cluster-mass-gap-adjoint-repair` (0.3).

