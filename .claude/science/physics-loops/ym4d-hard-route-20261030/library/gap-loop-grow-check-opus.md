# Check of `library/gap-loop-grow-astra.md` (Codex gpt-6-astra max, FINISH row 767)

- Checker: Claude Opus 5.5, one session, alone. Date: 2026-11-12.
- Source: `/Users/jonreilly/ym4d-lead/clone/.claude/science/physics-loops/ym4d-hard-route-20261030/library/gap-loop-grow-astra.md`, 672 lines, read in full.
- Cross-provider for the note itself (Codex author, Claude checker). Not independent of the
  inputs `gap-seed-sc.md` (Claude Fable 5.2) and `gap-seed-sc-check.md`, `gap-loop-pos-check-opus.md`
  (Claude Opus 5.5): where this check leans on them it is same-provider.
- Inputs read: `gap-loop-pos-astra.md` lines 60–519 (Sections 1–3 and the start of 4);
  `gap-loop-pos-check-opus.md` in full (286 lines); `gap-seed-sc.md` in full (257 lines);
  `gap-seed-sc-check.md` in full (118 lines); `gap-crux-fp.md` 3b.3 (lines 270–288);
  `gap-loop-eq-check.md` lines 64–100 (the Ward identity); for 4.2 only, the cited ranges
  `gap-crux-restate.md` 140–158, `gap-skeleton-max.md` 258–277, `gap-es1-opus-check.md` 56–85,
  and the outline `~/ym4d-lead/sa/YM4_sketch_500.tex` lines 26918–26934, 26978–27013.
- Method: by hand. No script, no numerics. No repository file edited. No git state changed.

## 1. Section 1

**1a. Formula (1). HOLDS.** It is the shift formula of `gap-loop-pos-astra.md` Section 1
(lines 77–80) with $w_a=p_A$, $w_{2a}=p_B$, $w^{\rm ins}_{\rm ev}=p^{\rm ins}_E$. That formula is
checked in `gap-loop-pos-check-opus.md` items 1–4. Re-derived: with $\hat Z=\int e^{s\sum x_p}$,
$\partial_s\log\hat Z(\text{cyl side }L,\text{time }t)=6L^3t\,w_L$, so per unit time
$\hat e'(L^3)=6L^3w_L$ and $\delta'=a(8\cdot6a^3w_a-6\cdot8a^3w_{2a})=48a^4(w_a-w_{2a})$;
$\partial_s\log\hat Z_0=6a^4w^{\rm ins}_{\rm ev}$ and $a\,\hat e'(a^3)=6a^4w_a$. Both vanish at
$s=0$. The integrals are $\delta\ge0$ and $\log(1+\epsilon)\ge0$; no pointwise sign is
asserted. The remark that one finite lattice cannot give cutoff uniformity is correct.

**1b. Scope reading of Theorem O. HOLDS AFTER CORRECTION (wording only).** Theorem O
(3.2) reads: for all $r\ge2$ and $I$ there is $J_r(I)>0$, independent of $a$. With
Corollary O-seed this gives, for fixed $r$ and $\beta$, failure for all $a$ above a threshold
depending on $r,\beta$. It does not give failure at each $a$. At $r=r(a)$ the bound is
$48a^4J_{r(a)}$ or $6a^4J_{r(a)}$; (3.8) has no uniform estimate of $\eta_n$. All correct.
This is not a correction of Theorem O: `gap-loop-pos-astra.md` lines 496–502 already state
the same quantifier.
Correction: "These statements cannot be strengthened by changing the order of the
quantifiers" claims an impossibility that is not proved. Nothing shows the reordered
statement (some $a_0$ for all $r$) is false. It only does not follow from Theorem O.
Read: "Theorem O does not yield these statements with the quantifiers reordered."

## 2. Section 2: Theorem A

Inputs, as I read them. `gap-seed-sc.md` Theorem 1 (ii), (iii) and Theorem 2. Theorem 1 (iii)
gives $|\Phi(n;\beta)|\le0.16\,n^4(12800|\beta|)^{e(n)}$ for $|\beta|<1/12800$. Here
$2048/12800=0.16=4/25$. Theorem 2 gives $A_n=192n^3 4^{-4n}$ for $n\ge5$. Theorem A uses neither
the sign $\Phi\ge0$ nor its input (TM). I did not re-derive SC Lemmas 3.1–3.5 (row 694) or
Corollary 2.3. I did recheck the leading coefficient by a direct count. There are $12n^3$ tubes
on $n^4$, each with cumulant $4^{-4n}$. The torus $(2n)^4$ has no term of order $4n$. So
$16\cdot12n^3\,4^{-4n}=192n^3\,4^{-4n}$. This agrees with `gap-seed-sc-check.md` Section 1.

**2a. (2) and the set-up. HOLDS.** $n=2r+4\ge8\ge5$, so Theorem 2 applies, and $d=4n=e(n)$.

**2b. (6). HOLDS.** First, $\Phi_n$ in the hat normalization equals the seed-sc $\Phi(n;\cdot)$:
$16\cdot6n^4s-96n^4s=0$. Second, $\Phi_n(0)=0$ since $\hat Z(0)=1$. Third,
$\Phi_n'=16\cdot6n^4p_n-96n^4p_{2n}=96n^4f_n$. Fourth, $[s^d]\Phi_n=192n^3 4^{-d}$, and
$[s^k]\Phi_n=0$ for $k<d$ by Theorem 1 (ii). The bound $(4/25)n^4(12800|s|)^d$ is Theorem 1 (iii).

**2c. $R_*$ and (7). HOLDS.** $R_*=2^{-14}=1/16384<1/12800$. On $|s|=R_*$,
$|\Phi_n|\le0.16n^4(0.78125)^d\le n^4$. Cauchy gives $|[s^k]\Phi_n|\le n^4R_*^{-k}$.

**2d. (8). HOLDS.** With Lagrange nodes $j/M$, the numerator $\prod_{i\ne j}(x-i/M)$ has $M$
factors. Each has absolute coefficient sum $1+i/M\le2$, so the product has sum at most $2^M$.
The denominator is $|\prod_{i\ne j}(j-i)/M|=M^{-M}j!(M-j)!$. Summing over $j$,
$2^MM^M\sum_j1/(j!(M-j)!)=4^MM^M/M!$. Since $\log M!\ge M\log M-M+1$, this is at most
$(4e)^M/e<16^M$. Then $|[x^k]P|\le\max|P|\cdot\sum_j|[x^k]\ell_j|<16^M\max_{[0,1]}|P|$.

**2e. (9). HOLDS.** $t_*/R_*=2^{-6}$. The tail on $[0,1]$ is at most
$n^4\sum_{k>M}64^{-k}=n^4\,64^{-M}/63<n^4\,2^{-6M-5}$, since $63>32$.

**2f. (10). HOLDS.** $[x^d]P=192n^3\,4^{-d}2^{-20d}=192n^3\,2^{-22d}$, and $d\le M$. With $M=12d$:
$16^ME_n<n^4\,2^{-2M-5}=n^4\,2^{-24d-5}$. This is at most $96n^3\,2^{-22d}$ iff
$n\le3072\cdot2^{2d}$, which is true. Subtracting gives
$16^M\max|\Phi_n|>96n^3\,2^{-22d}$. Hence $\max_{[0,t_*]}|\Phi_n|>96n^3\,2^{-70d}=96n^3\,2^{-280n}$.

**2g. (3), Theorem A. HOLDS (given the seed-sc inputs).** For $s\le t_*$,
$|\Phi_n(s)|\le96n^4\int_0^{t_*}|f_n|$, so $\int_0^{t_*}|f_n|\ge2^{-280n}/n=j_r$. The witnesses
$\omega_n(s),\omega_{2n}(s)$ lie in $K_r(s)$ for every $s\ge0$ (Theorem O; pos-check item 23).
Both orders give $b(s)\ge|f_n(s)|\ge0$. So $\int_0^\beta b\ge\int_0^{t_*}b\ge j_r$ for $\beta\ge t_*$.
The step from $t_*$ to $\beta$ needs $b\ge0$, and $b\ge|f_n|$ gives it. Since $j_r$ does not depend
on $a$, $r$ may depend on $a$.

**2h. (4), (5). HOLDS.** A separate-state certificate gives $\delta\le48a^4\int b$ and
$\log(1+\epsilon)\le6a^4\int b$. Its value is at least $48a^4j_r$, respectively $6a^4j_r$. It
cannot reach the tolerance when that value exceeds $10^{-7}$, respectively
$\log(1+10^{-7})$. These are (4) and (5). The condition $a\ge2r+3$ is inherited from O-seed and
makes the targets members of $K_r$.

**2i. Growth statements. HOLDS (one wording remark).**
$\log_2(a^4j_r)=4\log_2a-280(2r+4)-\log_2(2r+4)$. This tends to $+\infty$ if $r=o(\log a)$.
It also does so if $r\le c\log_2a$ with $4-560c>0$, that is $c<1/140$. "More explicitly"
should read "more generally": $r\le c\log_2a$ is a larger class than $o(\log a)$.

**2j. Size of the excluded range (remark, not a correction).** The note says "constants
deliberately loose" and claims no exclusion at a fixed size. Its claims are correct. The
reader should still see how far out the threshold lies. At $r=2$ ($n=8$), (4) needs
$4\log_2a>2240+3-5.58-23.25$, so $a>2^{553}\approx10^{166}$. Larger $r$ raises the threshold.
So Theorem A excludes no certificate at any lattice size a hand or machine calculation could
reach. As a quantitative supplier it is vacuous. Its content is the explicit uniformity in
$r$ that replaces the existence-defined $\eta_n$ of (3.8).

**2k. Scope and OPEN paragraphs. HOLDS.** It is a restriction on support only, with the witnesses
unchanged. There is no claim for box-scale $r(a)$ or at a fixed seed size. Correct.

**2l. U(1) compatibility. HOLDS; passes.** Theorem A is a lower bound on certificate width. It
proves no seed. T1 (`gap-crux-fp.md` 3b.3) can only refute a hypothesis that is said to imply
Seed. So T1–T3 cannot be violated here. The SU(2) coefficient is used, and no Abelian claim
is made.

**2m. Hidden (ES) or gap input. None.** Only finite-torus strong-coupling analyticity at
$|s|<1/12800$ and the exact witnesses enter.

## 3. Section 3

### 3.1 Charged one-point equations

**3a. (11). HOLDS.** I re-derived it here. Write $W=\tfrac12\operatorname{tr}X$ with $X=U_eA$, and
$x_p=\tfrac12\operatorname{tr}Y$ with $Y=U_eB_p$. The generators are $t_j=i\sigma_j$, and Pauli
completeness gives $\sum_j\operatorname{tr}(t_jX)\operatorname{tr}(t_jY)=\operatorname{tr}X\operatorname{tr}Y-2\operatorname{tr}(XY)$.
So $\Gamma_e(W,x_p)=Wx_p-\tfrac12\operatorname{tr}(XY)$. The SU(2) identity
$\operatorname{tr}X\operatorname{tr}Y=\operatorname{tr}XY+\operatorname{tr}XY^{-1}$ turns this into
$W(C\ominus p)-Wx_p$, with $W(C\ominus p)=\tfrac12\operatorname{tr}(AB_p^{-1})$. Then
$E[\Delta_eW+s\sum_p\sigma_p\Gamma_e(W,x_p)]=0$ and $\Delta_eW=-3W$ give (11). This agrees with
`gap-loop-eq-check.md` lines 66–86. The identity uses only Haar invariance at $e$ and the local
density $e^{s\sum\sigma_px_p}$. So it holds with twist signs and for winding $C$. The seam-dressing
sentence is harmless.

**3b. (12). HOLDS.** Take the cut to be the full slab of $\mu$-links from $x_\mu=t$ to $t+1$.
Multiplying these links by $-I$ preserves Haar measure, since $-I$ is central. A
$(\mu,\nu)$-plaquette with lower corner in the slab has two $\mu$-links of the slab, so its
trace is unchanged. No other plaquette meets the slab. So every $\sigma_px_p$ is invariant.
Each traversal of a slab link, in either direction, gives $-1$. So
$W(C)\mapsto(-1)^{q_\mu(C)}W(C)$, and $E_\sigma W(C)=0$ for $q\ne0$. This holds in all four
directions for each fixed twist on a finite torus. It passes to positive twist mixtures, and
to finite-time limits for loops of fixed time support.

**3c. Parity of all terms. HOLDS.** $q(p)=0$ for a plaquette, so $W(C)x_p$ and $W(C\ominus p)$ carry
$q(C)$. The general statement is $E\prod_iW(C_i)=0$ unless $\sum_iq(C_i)=0$. So for odd $C$,
(11) reads $0=0$.

**3d. Restricted exclusion. HOLDS.** Ward rows preserve total charge. The linear system
therefore splits by charge sector, and zero charged unknowns extend any neutral solution.
A remark that strengthens the author's caution: setting all entries with nonzero total
charge to zero is also compatible with positivity. That is the twirl of any PSD moment matrix
over the $(\mathbb Z_2)^4$ flips, and the actual Wilson states already have those entries zero.
So charged data carry no information at all, linear or positive. The note claims only the
linear case, which is correct.

**3e. OPEN paragraph; $W(C)^2=(1+W(C^2))/2$. HOLDS.** $(\operatorname{tr}X)^2=\operatorname{tr}X^2+2$
in SU(2), so $(\tfrac12\operatorname{tr}X)^2=\tfrac12+\tfrac12W(C^2)$, and $C^2$ is neutral.

### 3.2 Normalization obstruction

**3f. (13). HOLDS.** Rescaling $I_\sigma$ by $c_\sigma>0$ leaves normalized moments and
homogeneous Ward rows unchanged, and scales within-sector Gram forms by $c_\sigma$. It changes
the mixture weights $q_k\propto Z_k$. This is trivially true and correctly labelled
"restricted".

**3g. (14) and the Haar anchor. HOLDS.** $Z_\sigma(0)=1$ for normalized Haar measure, and
$\partial_s\log Z_\sigma=E_\sigma H_\sigma$. Also $I_\sigma(e^{-sH_\sigma})=\int e^{sH}e^{-sH}\,dU=1$.
The series $\sum(-s)^kE_\sigma H^k/k!$ converges absolutely, since $|H|\le N_p$. Each $H^k$ is a
product of plaquette traces, so a full set of (multi-)loop moments fixes $Z_\sigma$. The anchor
gives $c_\sigma=1$. Under (14), $\partial_s\log c_\sigma=0$ and $c_\sigma(0)=1$, so $c_\sigma\equiv1$
(for $c$ differentiable in $s$). The conclusion "not an exclusion of full class B" is correct.

### 3.3 Theorem B

**3h. Existence. HOLDS.** $D_{e,j}$ generates $U_e\mapsto e^{\tau t_j}U_e$ and is divergence-free for
Haar. So $\int D(Fe^{sH})\,dU=0$, which is (15) for $\mu$.

**3i. Uniqueness. HOLDS.** Take $F_K=G\sum_{m\le K}(-sH)^m/m!$. These are polynomials. $F_K$ and
$DF_K$ converge uniformly to $e^{-sH}G$ and $D(e^{-sH}G)$, since $H$ and $DH$ are bounded. Then
$DF_K+sF_KDH\to e^{-sH}DG$, so $\nu(e^{-sH}DG)=0$. Set $\rho\propto e^{-sH}\nu$, a probability
measure since $e^{-sH}>0$. For $g(\tau)=\rho(G\circ L_{e^{\tau t_j}})$ one has
$g'(\tau)=\rho(D(G\circ L_{e^{\tau t_j}}))=0$, because $D$ commutes with translation along its own
subgroup and $G\circ L$ is a polynomial. The three subgroups generate SU(2). Stone–Weierstrass
extends invariance to $C(X)$. Averaging over product Haar translations gives
$\rho=\text{Haar}$, hence $\nu=\mu$. Remark: gauge invariance of $\nu$ is not used here, since
(15) for all non-invariant $F$ already fixes $\mu$. Gauge invariance enters only in the
loop-equation rewriting.

**3j. Loop-equation form. HOLDS.** For gauge-invariant $\nu$, $\nu(Q)=\nu(\operatorname{avg}_gQ)$.
The average is a gauge-invariant polynomial. Tree gauge reduces it to a conjugation-invariant
polynomial in the based holonomies $V_i=c_i+iv_i\cdot\sigma$. By the first fundamental theorem
for SO(3), this is a polynomial in the $c_i$, $v_i\cdot v_j$ and $(v_i\times v_j)\cdot v_k$.
The averaging sketch with $(u,v,u\times v)$ is adequate: sphere and circle moments are
pairings divided by $d(d+2)\cdots$, and $\epsilon\epsilon$ reduces to $\delta$s. I checked the two
displayed traces from $(a\cdot\sigma)(b\cdot\sigma)=a\cdot b+i(a\times b)\cdot\sigma$. They give
$W(V_iV_j)=c_ic_j-v_i\cdot v_j$ and the printed triple formula, with $+(v_i\times v_j)\cdot v_k$.
So every generator is a polynomial in Wilson loops.
Scope: "equivalently written" means the averaged scalar equations
$\nu(\operatorname{avg}Q_F)=0$. These are linear equations in loop moments. They are not
in general the Makeenko–Migdal form for a gauge-invariant test. The note's scope paragraph
says this ("completeness of a particular list ... is not asserted").

**3k. Finite selection. HOLDS.** The gauge-invariant probability measures form a weak-* compact
set. Each equation cuts out a closed set, and their intersection is $\{\mu\}$. $B_\eta$ is
compact and disjoint from $\{\mu\}$, so finitely many failure sets cover it. The list depends on
the graph, $s$, $f$ and $\eta$, as stated.

**3l. Scope and consequence. HOLDS (one remark).** It is correct that on a fixed finite graph
there is only one measure with the full volume-labelled Ward data, and that this is not an
estimate of (1). Remark: Theorem B is stated for one fixed twist $\sigma$. The even state $E$ is a
mixture over twists. Theorem B fixes each sector's normalized law, but not the weights
$q_k(s)$. Those need the 3.2 anchor, or a cross-sector constraint. The cylinders A and B are
outside Theorem B, as the note says.

**3m. U(1) test (Section 3). HOLDS; passes.** For U(1) with the same period, the $m=1$ case of
`gap-loop-eq-check.md` lines 91–95 gives $E\,W=(s/2)\sum\sigma_pE[W(C\ominus p)-W(C\oplus p)]$.
With $\cos A\cos B$ product rule this is (11) with $1$ in place of $3$. Parity, normalization
and compactness carry over: $-1\in U(1)$, Stone–Weierstrass, and the Abelian invariants are
loop characters. Determinacy holds for U(1) at every coupling. By T1/T3, determinacy alone
cannot imply the seed at any U(1) coupling where the U(1) seed fails. The note phrases this
conditionally and does not need the RECALLED (F8). No Abelian seed is produced.

**3n. Hidden (ES) or gap input. None.** The cylinder limit for fixed-time-support loops uses
only the simple top eigenvalue of the transfer operator on a finite spatial box, which is
Perron–Frobenius. It needs no gap uniform in $a$.

## 4. Section 4

### 4.1 Theorem C

**4a. Theorem C. HOLDS.** $\omega_n\otimes\omega_{2n}$ and $\omega_{2n}\otimes\omega_n$ are actual
probability measures. So moment and localizing matrices on the product algebra are PSD.
Take a Ward row in copy 1 with a product test $F=\sum_iF^{(1)}_iG^{(2)}_i$. It equals
$\sum_iE_1[DF_i+sF_iDH]\,E_2[G_i]=0$. For the componentwise reflection, take tests in
$\operatorname{span}\{A_i\otimes B_k\}$ with $A_i,B_k$ positive-half polynomials. The Gram form is
$G^1\otimes G^2$ (Kronecker), which is PSD. On a list of paired tests $A_a\otimes B_a$ it is the
Hadamard product, PSD by Schur. Restriction to a subspace keeps it PSD. One-sided reflection
($\Theta_1\otimes\mathrm{id}$) would also pass. The marginal differences are $\pm f_n$, so
$b\ge|f_n|$, and Theorem O and (3) survive. The extension to finitely many copies is correct.

**4b. Theorem C scope. HOLDS.** It excludes only product-compatible constraints, not
gluing identities, boundary laws or cross-moment conditions. Correct.

### 4.2 Prior work

**4c. Citations. HOLDS.** I read every cited range.
- `gap-crux-restate.md` 145–156 (Way 2) gives $N_{\rm seam}=192n^3-96n^2$ and the Jensen bound
  $\Phi\le\beta(192n^3-96n^2)(1-\bar a_n)$. My recount: $4$ directions $\times2$ cuts $\times3$
  planes $\times8a^3=192a^3$, less $6$ pairs $\times4\times4a^2=96a^2$ counted twice.
- `gap-skeleton-max.md` 260–275 is Lemma 4, the doubling identities with Rényi-2 entropies.
- `gap-es1-opus-check.md` 58–83 is the sector-purity identity (1).
- Outline 26980–27011 is the chessboard bound with $\operatorname{Tr}Y^q\le(\operatorname{Tr}Y)^q$
  for $Y\ge0$. It then uses stability on $T_*$, the floor and the vacuum densities. Outline
  26920–26932 keeps the face-energy, floor, common-coupling/normalizer and nonwrapping
  hypotheses.
The note's description is accurate, and it claims no new exclusion here.

### 4.3 The conditional joint certificate

**4d. (16). HOLDS.** With exact marginals, $E_\pi X=p_A$ and $E_\pi Y=p_B$. Then
$|p_A-p_B|\le\sqrt{E(X-Y)^2}$, and integrating against $48a^4$, respectively $6a^4$, gives (16).
For E, the signed plaquette is a random variable under the positive twist mixture, so the same
step applies.

**4e. Framing of (16) and the OPEN coupling item. HOLDS AFTER CORRECTION.**
Here $X,Y$ are scalar, with the anchor and orientation randomness inside the law. Hence
$\inf_\pi E_\pi(X-Y)^2=W_2(\lambda_A,\lambda_B)^2$, where $\lambda_A,\lambda_B$ are the two
one-plaquette laws. The comonotone (quantile) coupling attains it. It lifts to a coupling of
the full states by the gluing lemma, so the "correct global marginals" requirement costs
nothing. Three consequences:
- The best value of (16) is $48a^4\int W_2(\lambda_A,\lambda_B)$. That is a functional of the
  two *separate* marginal laws. The sentence "a joint certificate using a cross moment, not
  two separate plaquette intervals" is literally true. But optimizing over couplings removes
  the joint content.
- $W_2\ge|p_A-p_B|$ pointwise. So (16) is never sharper than the exact integrand. Condition (17)
  implies the pointwise bounds $|p_A-p_B|\le10^{-7}/(48\beta a^4)$ and
  $|p^{\rm ins}_E-p_A|\le\log(1+10^{-7})/(6\beta a^4)$ on $[0,\beta]$. These are a no-cancellation
  form of the ES integrands, so (17) is at least as strong as (ES) itself. This is stated
  openly as a hypothesis, not assumed quietly. The note's "sufficient, not necessary"
  is correct.
- The witnesses obstruct a separate local bound on $W_2$ just as before:
  $W_2(\lambda_{\omega_n},\lambda_{\omega_{2n}})\ge|f_n|$.
Correction to the OPEN sentence (lines 592–594 and 653–654): "Construct a genuine coupling"
should read: "Bound $W_2$ between the actual one-plaquette laws (or between laws of a larger
local observable) by global information that the Theorem O witnesses violate." A coupling
with the correct marginals and minimal cost always exists. Joint structure helps only as a
proof device for one chosen coupling, never as a weaker hypothesis.

**4f. (17). HOLDS.** If $D\le(\tau/(48\beta a^4))^2$ on $[0,\beta]$, then $48a^4\int_0^\beta\sqrt D\le\tau$.
The same holds for EA.

**4g. (18). HOLDS.** In 4D, each link lies in 6 plaquettes. So the four links of $p$ touch
$4\cdot5+1=21\le24$ distinct plaquettes. Given the exterior, the log-density of these links
relative to $\mathrm{Haar}^4$ is $s\sum\sigma x$ over those plaquettes. Its oscillation is at most
$2s\cdot24=48s$, so the normalized density $\rho$ lies in $[e^{-48s},e^{48s}]$. Under $\mathrm{Haar}^4$,
$U_p$ is Haar, with $E\,c=0$ and $E\,c^2=1/4$ ($S^3$ coordinate). Then
$|E_sx|\le\max|\rho-1|\le e^{48s}-1=d_s$, and $E_sx^2\ge\tfrac14e^{-48s}\ge\tfrac14-d_s$. The bounds
are uniform in the exterior, so they pass to cylinder limits and twist mixtures.

**4h. (19) and the product failure. HOLDS.** $48\cdot2^{-10}=3/64$. Then
$d_s\le(3/64)/(1-3/64)=3/61<1/16$, and $\operatorname{Var}\ge\tfrac14-d_s-d_s^2>47/256>1/8$.
Independence gives $D=\operatorname{Var}X+\operatorname{Var}Y+(EX-EY)^2\ge1/4$.
$\int_0^{2^{-10}}\tfrac12=2^{-11}$, and $6a^4/2048\approx2.9\times10^{-3}a^4>10^{-7}>\log(1+10^{-7})$.
Remark: this uses the single-random-plaquette $X$ of the note's definition. A spatially
averaged $X$ at the fixed time would have a smaller variance. That case is not covered, and
4e makes it moot.

**4i. (20), deterministic tiling. HOLDS.** $p$ and $p+ae_i$ are distinct and link-disjoint on the
$2a$-periodic box for $a\ge2$. Setting one non-shared link of $p$ to $-I$ gives traces $-1$ and $1$.
An open neighbourhood has positive Haar mass, and the Wilson density is positive. For the
cylinder, the conditional density on the 8 links is bounded below uniformly in the exterior.
Reflection copying: choose a link of $p$ not in $\theta p$ (the far spatial link), and the
same argument applies. The note correctly says (20) does not refute RP inequalities.

**4j. U(1) test (Section 4). HOLDS; passes.** (16) uses no group identity. Under T1, its
quantitative hypothesis (17) must fail wherever the U(1) seed fails, and the note states this
correctly. For U(1), $E\cos^2=1/2$, so (18)–(19) still give $D$ bounded below. Strict positivity
rules out copying. No Abelian seed is produced.

**4k. Hidden (ES) or gap input. None quietly.** (17) is an explicit hypothesis at least as
strong as a pointwise (ES), as 4e shows. (18)–(20) use only bounded local densities.

## Verdict table

| # | Statement (lines) | Verdict |
|---|---|---|
| 1 | (1), shift formulas $48a^4$, $6a^4$; integrals $\ge0$ (64–78) | HOLDS |
| 2 | Scope reading of Theorem O's quantifiers (80–86) | HOLDS AFTER CORRECTION: "cannot be strengthened" → "Theorem O does not yield the reordered statements"; restates pos-astra 496–502, not a correction of it |
| 3 | (2): $n=2r+4$, $d=4n$, $t_*=2^{-20}$, $j_r$ (97–102) | HOLDS |
| 4 | (6): $\Phi_n'=96n^4f_n$, order $d$, coefficient $192n^3 4^{-d}$, bound $(4/25)n^4(12800\lvert s\rvert)^d$ (140–149) | HOLDS given `gap-seed-sc.md` Thm 1 (ii), (iii), Thm 2 (same-provider checked); (TM) not used |
| 5 | $R_*=2^{-14}$, $\lvert\Phi_n\rvert\le n^4$, (7) (149–155) | HOLDS |
| 6 | (8) Lagrange bound $16^M$ (157–170) | HOLDS |
| 7 | (9) tail $<n^4 2^{-6M-5}$ (172–179) | HOLDS |
| 8 | (10) $\max\lvert\Phi_n\rvert\ge96n^3 2^{-280n}$ (181–196) | HOLDS |
| 9 | Theorem A, (3) (105–111, 198–201) | HOLDS |
| 10 | (4), (5) (113–124) | HOLDS |
| 11 | $r=o(\log a)$ and $r\le c\log_2a$, $c<1/140$ (126–129, 203–208) | HOLDS ("more explicitly" → "more generally") |
| 12 | Theorem A scope and OPEN (210–220) | HOLDS; remark: at $r=2$ the excluded range is $a>2^{553}$, so no physically reachable size is excluded |
| 13 | Theorem A U(1) compatibility (222–227) | HOLDS; passes |
| 14 | (11) twisted one-link Ward equation (233–245) | HOLDS (re-derived) |
| 15 | (12) and total-parity conservation (247–262) | HOLDS |
| 16 | Restricted exclusion of charged one-point rows (264–269) | HOLDS (also true with positivity, by twirling) |
| 17 | Neutral odd-odd data; $W(C)^2=(1+W(C^2))/2$ (271–277) | HOLDS |
| 18 | (13) normalization witnesses (279–297) | HOLDS |
| 19 | (14), Haar anchor, $c_\sigma\equiv1$ (299–315) | HOLDS |
| 20 | Theorem B existence and uniqueness (323–358) | HOLDS (gauge invariance not needed for uniqueness) |
| 21 | Theorem B loop-equation rewriting, SO(3) invariants, trace formulas (360–401) | HOLDS (averaged equations, not Makeenko–Migdal form; the note says so) |
| 22 | Theorem B finite selection (335–337, 403–414) | HOLDS |
| 23 | Theorem B scope and consequence (416–431) | HOLDS; remark: fixed twist only, mixture weights of E need 3.2's anchor |
| 24 | Section 3 U(1) test (433–441) | HOLDS; passes |
| 25 | Theorem C (447–469) | HOLDS |
| 26 | Theorem C scope (471–476) | HOLDS |
| 27 | 4.2 prior-work citations and seam count (478–496) | HOLDS (all ranges read) |
| 28 | (16) (500–517) | HOLDS |
| 29 | "Joint certificate" framing; OPEN "construct a genuine coupling" (517–518, 592–594, 653–654) | HOLDS AFTER CORRECTION: the optimal coupling gives $D=W_2(\lambda_A,\lambda_B)^2$, a two-marginal quantity; it always exists; the open item is smallness of $W_2$, which the witnesses obstruct locally ($W_2\ge\lvert f_n\rvert$) |
| 30 | (17) sufficient bounds (519–531) | HOLDS; implies a pointwise (ES)-integrand bound, so not weaker than (ES) |
| 31 | (18) (533–550) | HOLDS (21 plaquettes, 24 is a valid bound) |
| 32 | (19) and the product-coupling failure (552–569) | HOLDS (for the single-plaquette $X$ defined) |
| 33 | (20) deterministic tiling and reflection copying (571–590) | HOLDS |
| 34 | Section 4 U(1) test (600–606) | HOLDS; passes |
| 35 | Any step quietly assuming (ES) or a gap | None found; (17) is an explicit hypothesis at least as strong as pointwise (ES) |

RESULT: Sections 1–4 of gap-loop-grow-astra.md check line by line (Codex gpt-6-astra max author; Claude Opus 5.5 checker). Formula (1), Theorem A with every constant in (2)–(10) and the exclusions (4)–(5), the twisted Ward equation (11), parity (12), the normalization witnesses and Haar anchor, Theorem B (uniqueness, loop form, finite selection), Theorem C, (16)–(20), and all three U(1) tests HOLD. There are two corrections, neither breaking a theorem: (i) the quantifier remark claims an impossibility it does not prove; (ii) with scalar $X$, $\inf_\pi D=W_2(\lambda_A,\lambda_B)^2$, so the joint route depends only on the two marginals, (17) implies a pointwise (ES) bound, and the OPEN item is smallness of $W_2$, not existence of a coupling. Theorem A excludes nothing below $a\approx2^{553}$. No step assumes (ES) or a gap, and no ES certificate or mass gap is proved.
