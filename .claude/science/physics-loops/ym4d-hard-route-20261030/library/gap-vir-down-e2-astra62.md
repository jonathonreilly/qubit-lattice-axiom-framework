# Repo search

**ON FILE (row 531, §11, rows 1617, 1623, 1626–1630).** Row 1632 at `5aab5b0d5`. The target-specific prior file is absent. The November 8 five-ref digest found a one-step centered-loop correlation in the soft-route work. I checked the positive multiplier in the soft-route file `MASS_GAP_LOCAL_BLOCK_ASTRA.md` §2 on PR 10114, the small-coupling Doob contraction in that file on PR 10133, and the simple finite-box vacuum in main's `research/mass-gap/library/gap-transfer.md`, Statement 4. These are estimates at one coupling. Main also has `research/mass-gap/library/gap-vir-sc.md`, Theorem U(ii), the slab derivative used below. Its Theorem B1 bounds how fast a normalized energy can fall. A fresh search of Markdown and TeX for VIR-down, the hidden adverse trace and the delay closure, outside this lane, returned no matches on main `8b11ae2bb95e` and PRs 10114, 10133, 10134, 10141 at `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, `a2f6a430e251`. [Lead's search](prior/repo-search-2026-11-08.md)

**ON FILE (outline index, rows 244–255).** Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, give the positive transfer and its partition-function trace in outline lines 2315–2335 at `31a47c543775`. Outline lines 588–599 and 31871–31882 distinguish polynomial decay from a spectral gap. CA-I lines 2703–2711 give the scope of Theorem 0, and lines 56342–56363 record bounds relative to baseline data. These passages contain no signed comparison between an excited state and the vacuum. [Outline index](sa-index/README.md) · [CA-I index](sa-index/ca-4.12-4.19/README.md)

**ON FILE (VIR-DOWN, check 1630 §§1, 3.3).** The registry lists the band estimate as open. The window depth is fixed before the cutoff. The cold-point requirement runs over every side from the hot side to the enlarged seed side, with the running budget (RB). Row 1628 (17), (19), (23) identifies the hidden block at each multiplier. Row 1629 (2.12)–(2.13) gives alternative sufficient tests. Row 1617 (2) already proves eventual positivity of all sufficiently high level slopes at fixed box and coupling. Its (6) controls omitted large electric spins in each eigenvector. Neither assertion settles the sign for a thermally occupied hidden vector on the band. [Eigenspace estimate](gap-vir-down-astra62.md) · [Delay test](gap-vir-down-twoside-astra62.md) · [Check 1630](gap-vir-down-twoside-check-opus.md)

The question pursued here is whether the Wilson slab gives an upper bound on the negative part of the vacuum-subtracted hidden slope. All estimates below concern the centre-neutral space. This note carries research text only.

**ON FILE (rows 1628–1630, notation and test).** Set $A=T/\lambda_0$ in frozen coordinates, let $F_r$ be its spectral projection at $r$, and let $E$ project onto the centered flowed-loop observations. The observed part of the delay closure in that eigenspace is $J_r=\operatorname{proj}(F_r\operatorname{ran}E)$. Its orthogonal complement there is $D_r=F_r-J_r$, with range $\operatorname{ran}F_r\cap\ker E$. Write $b_r=r^{-1}F_r A' F_r$ and $b_r^h=D_r b_r D_r$ acting on $D_r$. With $m=-\log r$ and the sums over $0<r<1$,
\[
 G(t)=\sum_r r^t\operatorname{rank}F_r,\qquad
 W_t=\sum_r m r^t\operatorname{rank}F_r,\qquad
 H_\kappa(t)=\sum_r r^t\operatorname{Tr}_{D_r}(\kappa m{\bf1}-b_r^h)_+ .
\]
At these multipliers $b_\psi$ below is the quadratic form of $b_r$. It is the log derivative of the normalized Rayleigh quotient with $\psi$ fixed. At a simple eigenvalue it equals $-\partial_\beta m$. At a crossing the estimates concern the entire compressed form.

## A lower bound for every hidden block at late bare coupling

**ON FILE (rows 667, 710, 1215, 1617–1618).** Write $N=n^3$, $d=3N$, $T=MCM$, $M=e^{-\beta V/2}$, where $0\le V\le 2d$. Here and below the spatial torus has $n\ge4$. The one-link multiplier in integer label $k=2j$ is $c_k=2e^{-\beta}I_{k+1}(\beta)/\beta$. Put $I(\beta)=c_0$. In electric normalization the vacuum eigenvalue is $\lambda_0/I(\beta)^d$. Row 1215 line 278 gives
\[
  0\le L:=\log\frac{I(\beta)^d}{\lambda_0}\le C_0 N\qquad(\beta\ge1)
  \tag{1}
\]
with an absolute $C_0$, which we fix once. Its trial confines each link to a cap of radius $\beta^{-1/2}$ around the identity. The spatial action costs $O(N)$ in the exponent and each normalized electric step has a fixed probability to stay in its cap. Positivity and the unique vacuum put the top of the unrestricted transfer in the neutral sector. The upper bound on $\lambda_0$ follows from $\|M\|\le1$ and $\|C\|=I(\beta)^d$. The same row already removes large endpoint actions and large jumps in the norm of the **unmarked** transfer. [Row 1215](gap-solve23-astra62.md) · [Check 1221](gap-solve23-check-opus.md)

**PROVED (one-link electric derivative).** For every $\beta>0$ and every $k\ge0$,
\[
                    \partial_\beta\log c_k\ge-\frac{3}{2\beta}.              \tag{2}
\]
Use the positive integral for $I_{k+1}$ in row 1618, Lemma 1. Set $y=\beta(1-x)$ in that integral. With $K_k>0$ independent of $\beta$ and $p=k+1/2$, it gives
\[
  \beta^{3/2}c_k(\beta)
   =K_k\int_0^\infty e^{-y}y^p(2-y/\beta)_+^p\,dy.
\]
The integrand increases with $\beta$ for every $y>0$. The left side is differentiable and positive by the Bessel series, which proves (2). Products give the same lower bound multiplied by $d$ for the derivative of the log electric multiplier. [GL3–4, outline 2197–2243](sa-index/chunk-02.md) · [Row 1618](gap-vir-down-neon.md)

**PROVED (pointwise bound, including crossings).** For every unit vector $\psi$ in an eigenspace of $T$ of eigenvalue $\lambda=r\lambda_0>0$, write $m=-\log r$, $D_\psi=\langle\psi,T'\psi\rangle/\lambda$, and $D_0=D_\Omega$ at the vacuum. Then
\[
  b_\psi:=D_\psi-D_0\ \ge\ -\frac{m+L+3d/2+\beta D_0}{\beta}
    \ \ge\ -\frac{m+BN}{\beta},\qquad B=C_0+9/2,\quad \beta\ge1.          \tag{3}
\]
Indeed $w=C^{1/2}M\psi/\sqrt\lambda$ has norm one, and $C^{1/2}w=\sqrt\lambda\,M^{-1}\psi$. Therefore
\[
  \langle e^{\beta V}\rangle_\psi
       =\lambda^{-1}\langle w,Cw\rangle\le e^{m+L},\qquad
       \beta\langle V\rangle_\psi\le m+L.                                \tag{4}
\]
The last inequality is Jensen's inequality for the probability density $|\psi|^2$. Differentiating the two outer factors of $T$ gives $-\langle V\rangle_\psi$ in $D_\psi$. The middle factor gives the electric average in $w$ of the sum of the $d$ log derivatives (row 710 Theorem U(ii), row 1617). Equation (2) bounds it below by $-3d/(2\beta)$. Finally $D_0\le0$ because the derivative of the raw slab kernel inserts minus a nonnegative action between positive vacuum endpoints. This proves (3). The unitary identifying the Doob space with the Wilson space is frozen at the coupling in this calculation, as in row 1628. On an eigenspace, compression removes the commutator from a differentiable change of coordinates. The proof applies to every linear combination in that eigenspace. Compression to its hidden subspace $D_r$ therefore preserves (3).

**PROVED (price in the units of E2).** Write $G_D(t)=\sum_{r<1}r^t\dim D_r$ and $W_D(t)=\sum_{r<1}mr^t\dim D_r=hW_t$, always summing over $r>0$. If $H_\kappa(t)$ denotes the hidden adverse trace in check 1630, (3) gives
\[
 H_\kappa(t)\le(\kappa+\beta^{-1})W_D(t)+(BN/\beta)G_D(t).                \tag{5}
\]
At $G(t)\le c<1$, each $tm\ge a:=\log(1/c)$. Thus (23) of row 1628 allows $\rho=-(1+BNt/a)/\beta$. Together with the on-file bound one can use the better of the two. For fixed $c$ the volume term improves by a factor of order $\beta$ on the late window. It still grows with the cutoff. Even assuming E1 with fixed excess $\epsilon$, (5) leaves an uncontrolled term $BNG_D(t)/(\beta W_t)$.

**PROVED (finite-coupling check of the slope bound).** There is a direct min–max comparison that includes the vacuum penalty explicitly. Let $\widehat C_\beta=C_\beta/I(\beta)^d$, $\widehat\lambda_i(\beta)=\lambda_i(\beta)/I(\beta)^d$, and order the neutral eigenvalues with multiplicity. For $\beta_2=s\beta_1$ with $s\ge1$,
\[
 \widehat\lambda_i(\beta_2)\ \ge\ \widehat\lambda_i(\beta_1)^s,\qquad
 m_i(\beta_2)\ \le\ s m_i(\beta_1)+s L(\beta_1)-L(\beta_2).
 \tag{6}
\]
The normalized convolution increases in quadratic-form order. Its one-link multiplier $I_{k+1}/I_1$ is a product of the adjacent ratios $I_{q+1}/I_q$, each increasing by row 843, Lemma 3.1, as used in row 1617 (12). Hence at $\beta_2$ replacing $\widehat C_{\beta_2}$ by $\widehat C_{\beta_1}$ decreases the transfer in form order. Write $C_*=\widehat C_{\beta_1}$ for this paragraph only. The nonzero spectrum of the resulting transfer is that of $C_*^{1/2} e^{-\beta_2 V} C_*^{1/2}$, by exchanging the two factors of a singular-value product. In the span of the first $i+1$ eigenvectors of $C_*^{1/2} e^{-\beta_1 V} C_*^{1/2}$ take any unit $w$, and put $x=C_*^{1/2}w$. Then $0<\|x\|\le1$ and $\langle x,e^{-\beta_1 V}x\rangle\ge\widehat\lambda_i(\beta_1)$. Jensen applied to $z^s$ in the probability $|x|^2/\|x\|^2$ gives
\[
 \langle x,e^{-\beta_2 V}x\rangle
 \ge \|x\|^{2(1-s)}\langle x,e^{-\beta_1 V}x\rangle^s
 \ge\widehat\lambda_i(\beta_1)^s.
\]
Min–max and division by the vacuum give (6). For a simple level its right derivative gives $b_i\ge-m_i/\beta-L/\beta+L'$. Since $L'=d\,\partial_\beta\log I-D_0$ and $\partial_\beta\log I\ge-3/(2\beta)$, this recovers (3) through a finite comparison without differentiating an excited eigenvector. The quadratic-form proof of (3) handles any compression at a multiple level. The vacuum itself satisfies $sL(\beta_1)-L(\beta_2)\ge0$ by (6). Discarding this cost would change the inequality. [Bessel moment identity](gap-q8test-opus.md) · [Normalized electric increments](gap-vir-down-astra62.md)

## How much of E2 can come from large energies and large slab actions?

**ON FILE (rows 1143–1144, 1161–1162, 1215, 1619, 1626).** Row 1619's TRUNC and row 1626 (5)–(6) pay $\log(1+G(1))\le12\beta N$ to count high levels. Row 1618 §5.2 gives a smaller energy window if a bound at $t/2$ is supplied. Two older Wilson estimates allow an unconditional improvement here. In row 1143 §1, dropping all but the selected plaquette factors gives $Z^0\le I(\beta)^{3v-3}$ on an ordinary rectangular four-torus of volume $v$ with each side at least three. The selected plaquettes are independent Haar coordinates in the comb-tree parametrization. This is the inequality *before* the winding constraint is included. Row 1161 (19) at its counting parameter one gives $m_1\le C_1$ with an absolute $C_1$ for $\beta\ge1$ on all sufficiently large spatial tori here. [Selected plaquettes](gap-solve-astra62.md) · [Checked level count, S25](gap-solve9-check-opus.md) · [TRUNC](gap-vir-down-fable.md)

**PROVED (short-period entropy).** Use period three, where the selected-plaquette theorem applies directly. Positivity of the transfer and its commuting neutral projection gives $Z_+(3)\le Z^0(3)$. At $v=3N$, division by the cube of (1)'s vacuum lower bound gives
\[
 1+G(3)\le e^{3C_0N}I(\beta)^{-3}.
 \tag{7}
\]
In particular $\log(1+G(3))\le C_Z N$ throughout every sufficiently late fixed-depth window, with $C_Z=3C_0+1$. Indeed $I(\beta)\ge c_I\beta^{-3/2}$ for $\beta\ge1$ by integration over $0\le\theta\le\beta^{-1/2}$ in the one-link Haar density $2\sin^2\theta/\pi$. On this interval $\sin\theta\ge2\theta/\pi$ and $\beta(1-\cos\theta)\le1/2$, so one may take $c_I=8e^{-1/2}/(3\pi^3)$. By the calibrated growth and the fixed-depth width estimate, $\beta=O(\log n)$ uniformly on the window. Thus $3\log(1/I(\beta))\le N$ eventually. There are just three uncancelled powers of the Haar integral in (7).

**ON FILE (row 1161, paragraph following (19)).** At fixed period three the lower count gives $\log(1+G(3))\ge c_3 N$ for all sufficiently large boxes and $\beta\ge1$. Thus the order in $N$ of the entropy bound in (7) is attained on Wilson boxes. The lower count says nothing about the adverse part in (8). [Row 1161](gap-solve9-astra62.md)

**PROVED (hidden high-energy tail).** Fix the trial rate $\kappa=\kappa_0>0$, the window depth, and $0<c<1$ before $K$. Take any point of its characteristic with $G(t)\le c$ on any of the box sides in check 1630. Then $n/512\le t\le C_t n$ for fixed $C_t$, since the bare width is bounded above at fixed depth (rows 1618 and 1630). Set
\[
 \Lambda=\frac{(C_Z+3)N}{t-3}\qquad(t>3).
\]
Let $H_{\kappa,\ge\Lambda}$ be the contribution of the hidden blocks with $m\ge\Lambda$. For all sufficiently late $K$, uniformly at those points,
\[
 0\le H_{\kappa,\ge\Lambda}\le e^{-N}W_t .                                \tag{8}
\]
By (3) each such block costs at most its dimension times $(\kappa+1/\beta)m+BN/\beta$ before thermal weighting. Both $e^{-(t-3)m}$ and $m e^{-(t-3)m}$ decrease for $m\ge\Lambda$ since $(t-3)\Lambda\ge1$. Sum the remaining weights at time three, including multiplicities, and use $W_t\ge m_1 e^{-tm_1}\ge (a/t)e^{-C_1t}$. This bounds the ratio in (8) by
\[
  \frac{t}{a}\big[(\kappa+1/\beta)\Lambda+BN/\beta\big]\,
           e^{C_1t+C_ZN-(t-3)\Lambda}.
\]
The log of the prefactor is $O(\log n)$ and $C_1t=O(n)$. The exponent from the last two terms is $-3N$, which proves (8). This retains energies up to $O(n^2)$ in lattice units, compared with $O(\beta n^2)$ from the period-one bound above. The retained range still contains all energies of order $1/t$.

**PROVED (the large-action part of the actual hidden mark).** In the raw one-step Wilson slab write $S$ for the sum of its temporal plaquette actions and half the spatial action of each boundary. Thus $0\le S\le4d$. In temporal gauge the kernel is $e^{-\beta S}$ before averaging over the boundary gauge. Put
\[
 F=C_0+\tfrac92\log2,\qquad R_\beta=2(F+4)N/\beta .
\]
In the matrix element defining each $D_\psi$, replace the mark $-S$ by $-S\,{\bf1}_{S\le R_\beta}$. Use the same replacement in $D_0$ and denote the resulting hidden compression by $b_r^{h,\mathrm{cut}}$. The transfer, its eigenspaces, the vacuum and the delay closure are all evaluated in the original Wilson law. This operation measures a truncated insertion at a point. It takes no derivative of the indicator.

For the omitted insertion the absolute raw kernel is bounded pointwise by
\[
  4d\,e^{-\beta R_\beta/2}e^{-(\beta/2)S}.
\]
Averaging gauge or centre images preserves this domination. For unit test vectors take absolute values at both ends and apply the norm bound for the positive-kernel transfer at $\beta/2$. Its top is the neutral vacuum by positivity and symmetry. Since $\lambda_0(\beta/2)\le I(\beta/2)^d$ and (2) at label zero gives $I(\beta/2)/I(\beta)\le2^{3/2}$, (1) gives $\lambda_0(\beta/2)/\lambda_0(\beta)\le e^{FN}$. The omitted operator divided by $\lambda_0(\beta)$ thus has norm at most $4d e^{-4N}$. For a hidden block and its vacuum subtraction this proves
\[
 \|b_r^h-b_r^{h,\mathrm{cut}}\|\le 4d e^{-4N}(e^m+1).
 \tag{9}
\]
The $e^m$ matters. An unmarked transfer-norm estimate by itself cannot be summed as a relative bound over all the excited states.

Let $H_{\kappa,<\Lambda}^{\mathrm{cut}}$ use the truncated insertion and only the blocks with $0<m<\Lambda$. On every cold point above, for all sufficiently late $K$,
\[
 \left|H_\kappa-H_{\kappa,<\Lambda}^{\mathrm{cut}}\right|
       \le 2e^{-N}W_t.                                                     \tag{10}
\]
On a block of dimension $j$, the positive-part trace equals $\sup_{0\le Y\le1}\operatorname{Tr}(YA)$ for a self-adjoint $A$. Perturbing $A$ by an operator of norm $\eta$ therefore changes the trace by at most $j\eta$, even at crossings. Summing (9) below $\Lambda$ costs at most $4d e^{-4N}(1+e^\Lambda)G(t)$. Coldness gives $G(t)\le tW_t/a$. Since $\Lambda/N=(C_Z+3)/(t-3)\to0$, the last cost is at most $e^{-N}W_t$ eventually. Adding (8) proves (10). The proof also applies with $\kappa=0$ at these same $t,\beta$. It uses the distribution of the **total** action of one slab. It allows arbitrary localized plaquette defects inside the retained set.

**PROVED (a full-spectrum check on the action cutoff).** The cut removes Wilson configurations of positive slab measure at late cutoffs. Taking every lower link equal to the identity and every upper link equal to the negative identity gives $S=2d$. Taking both slices at the identity gives $S=0$. Since $R_\beta/N\to0$, continuity and positivity of the raw Haar density give open sets on opposite sides of the cut. One can also estimate the omission before discarding any eigenvalue. Write $H_\kappa^{\rm cut}$ for the same truncated mark summed over the full excited spectrum. The trace variation bound used in (10), applied to (9), gives
\[
 |H_\kappa-H_\kappa^{\rm cut}|
 \le 4d e^{-4N}\big[G(t-1)+G(t)\big]\le e^{-3N}W_t                         \tag{10a}
\]
eventually. Indeed, Hölder on the positive excited multipliers gives $G(t-1)/G(t)\le[G(3)/G(t)]^{1/(t-3)}$ for $t>4$. Equation (7) and $G(t)\ge e^{-C_1t}$ bound the logarithm of this ratio by $(C_ZN+C_1t)/(t-3)=o(N)$. Now use $G(t)\le tW_t/a$. This also proves absolute summability after the replacement. Here no information on the sign or the observation of any retained level was used.

An independent way to bound the high-energy part of the truncated trace avoids (3). Dominate its raw marked kernel by $R_\beta$ times the unmarked kernel. Then $\|b_r^{h,\mathrm{cut}}\|\le R_\beta(e^m+1)$. Sum $\kappa m+R_\beta(e^m+1)$ over $m\ge\Lambda$ with the thermal weights and divide by $W_t$. Using the time-three sum, this is bounded by
\[
 \frac{t}{a}\big(\kappa\Lambda+2R_\beta\big)
       \exp\!\big(C_1t+C_ZN-(t-4)\Lambda\big).
\]
Here $m e^{-(t-3)m}$ is decreasing on the discarded range, and the $e^m$ in the mark costs one time step. The exponent is $-3N+\Lambda+C_1t$ with $\Lambda+C_1t=o(N)$. The prefactor grows at most polynomially. Consequently this high-energy cost is at most $e^{-2N}W_t$ before division, eventually. Adding (10a) checks (10) by cutting the mark first and without bounding any individual untruncated slope.

**PROVED (what (10) removes from the E1 budget).** Under E1 the observed contribution to row 1628 (19), after its duration cost, is at least $\kappa W_D+\epsilon W_t$. By the scalar inequality $(\kappa m-x)_+\le\kappa m+(-x)_+$ in each hidden block, it suffices to control $H_0$. At large $K$, the excluded high energies and the discarded part of the insertion together change this zero-speed cost by at most $2e^{-N}W_t$. For example, $H_{0,<\Lambda}^{\mathrm{cut}}\le(\epsilon/2)W_t$ would leave a strictly positive margin eventually. There is no estimate here of that last inequality. The quantitative content is the error (10) in units of the actual thermal energy, irrespective of how small $W_t$ is. The low-energy inequality with its margin merely identifies what still has to be paid.

## A regime where the hidden sign can be decided

**PROVED (all excited neutral levels on cold, strong-coupling Wilson boxes).** For $0<\beta\le1/(16d)$, at every $n\ge4$,
\[
             b_r^h\succeq (2\beta)^{-1}{\bf1}_{D_r}
             \quad\hbox{for all }0<r<1,\qquad G(t)<1/2\quad(t\ge1).
 \tag{11}
\]
In fact the bound holds on the entire excited eigenspace. This supplies the sign simultaneously for the low and high levels on a specified range of Wilson boxes. In particular $H_0=0$. Row 1610 line 141 argued that every level falls at strong coupling. Row 710 Proposition EL treats the purely electric model and its Theorem B1 bounds the rate of a fall. Row 1626 (11) concerns the full thermal derivative as $\beta\downarrow0$ at fixed size. Equation (11) proves the proposed sign for the full Wilson transfer on the displayed range. [Row 1610](gap-direction7-fable.md) · [Row 710](gap-vir-sc.md)

To prove the sign use the dual transfer $\widehat B=\widehat C^{1/2}M^2\widehat C^{1/2}$ from the proof of (6). Its top eigenvalue $\widehat\lambda_0$ is at least $\langle1,\widehat B1\rangle=\int e^{-\beta V}\ge e^{-2\beta d}\ge7/8$. Let $\Pi$ project onto the constant Haar function. The GL3–4 multiplier formula and row 710, Lemma J(c), bound every nonzero-label multiplier of $\widehat C$ by $q=\beta/4$ on this range. Indeed the one-link ratio to label zero is a product of $I_{j+1}/I_j\le\beta/(2(j+1))$ for $j\ge1$, and a nonconstant product has at least one such factor. Thus $\widehat B\preceq\widehat C\preceq\Pi+q(1-\Pi)$. If $w_0$ is the unit top vector of $\widehat B$ and $p_0=|\langle1,w_0\rangle|^2$, then $7/8\le p_0+q(1-p_0)$. With $q\le1/4$ this gives $p_0\ge5/6$.

For every unit excited vector $w=C^{1/2}M\psi/\sqrt\lambda$ one has $w\perp w_0$ by the dual eigen-equation. Since the projection of $1$ onto $w_0^\perp$ has squared norm $1-p_0$, the probability of a nonzero electric label in $w$ is at least $p_0$. Thus $\mathbb E_w\sum_e k_e\ge5/6$. The positive Bessel series gives $\beta\,\partial_\beta\log c_k=k+\beta I_{k+2}/I_{k+1}-\beta\ge k-\beta$. Row 710's action formula and $D_0\le0$ now yield
\[
 \beta b_\psi \ge 5/6-\beta(d+2d)\ge 5/6-3/16>1/2.
\]
This argument is uniform in the choice of vector inside a degenerate level. For coldness, $I(\beta)=\int e^{-\beta a(g)}dg\ge e^{-\beta}$ by Jensen, since the Haar mean of $a(g)=1-\tfrac12\operatorname{tr}g$ is one. It follows that $\lambda_0\ge e^{-3\beta d}$. The unprojected positive trace satisfies $\operatorname{Tr} M C M\le\operatorname{Tr}C=1$, the last equality being the integral of the diagonal of the smooth convolution kernel. Consequently $G(t)\le G(1)\le e^{3/16}-1\le3/13<1/2$. The bound $\beta\le1/(16d)$ shrinks as $n$ grows. The calibrated window instead has $\beta_K\to\infty$.

**PROVED (a check on the loss of this sign argument).** Replacing $7/8$ by the actual $\widehat\lambda_0$ would give $p_0\ge(\widehat\lambda_0-q)/(1-q)$ with $q=I_2/I_1$, since this is the largest one-link multiplier off the constants. The Bessel ratio tends to one as $\beta\to\infty$ by concentration of the one-link tilted Haar probability at the identity. Row 1145 (19) gives $\widehat\lambda_0\le e^{-c_2 N}$ for $\beta\ge1$ in its stated range of sufficiently large boxes. Hence even that refinement gives a negative lower bound for $p_0$ on the late boxes. This diagnoses precisely where the finite-volume sign proof loses its content. It does not exhibit a rising Wilson level. [Vacuum normalization, row 1145](gap-solve2-astra62.md) · [Strong-coupling thermal comparison, row 1626](gap-vir-down-dom-astra62.md)

## A bound on both signs at low energy from the vacuum pressure

**ON FILE (row 1623).** Convexity of a Wilson log partition function alone gives no sign for its vacuum-subtracted response. The estimate below uses the complex slab kernel as well as the vacuum pressure. [Prior literature search](prior/gap-vir-down-lit-luna.md)

**PROVED (a local bound at fixed coupling).** On one spatial box put $p(x)=\log\lambda_0(x)$ for the raw Wilson transfer at real coupling $x$. Write $I_K=[\beta_K,\beta_{K+r}]$ and enlarge it by one at both ends to $I_K^+$. Here $r$ in the endpoints denotes the fixed window depth. For $x\in I_K$ and $\beta_K\ge2$, define
\[
 \mathcal M(x)=\sup_{0<s\le1}\frac{p'(x+s)-p'(x-s)}{2s}.
\]
For every eigenvalue multiplier $r$ with $0<m=-\log r\le1$,
\[
 \frac{\|b_r^h(x)\|}{m}\ \le\
 C\left(1+\sqrt{\mathcal M(x)/m}\right),\qquad C=2+2\sinh 2.               \tag{12}
\]
The pressure is convex. Indeed the positive kernel permits taking the vacuum Rayleigh supremum over nonnegative unit vectors. For each such vector the raw Rayleigh quotient is a positive Laplace integral in $x$, whose logarithm is convex by Hölder. Taking the supremum preserves convexity. The simple finite-box vacuum of the analytic transfer gives a real analytic $p$ on the positive real axis. Alternatively, the local analytic eigenprojection follows by expanding the resolvent on a circle separating the simple top eigenvalue from the rest. Thus $\mathcal M$ is finite on this compact interval for each box.

Fix a unit vector $\psi$ in an excited eigenspace at $x$. For $0<s\le1$, let $\ell$ be the real affine function interpolating $p$ at $x-s,x+s$, extended to complex arguments. Let $\delta=\ell(x)-p(x)$. The chord slope lies between the two endpoint derivatives, so $|\ell'-p'(x)|\le2s\mathcal M(x)$. Integrating twice gives
\[
 0\le\delta=\tfrac12\int_{-s}^s (s-|y|)\,p''(x+y)\,dy
             \le s^2\mathcal M(x).
\]
The function $f(z)=e^{-\ell(z)}\langle\psi,T_z\psi\rangle$ is holomorphic, with the inner product linear in the second slot. On $|z-x|\le s$, the absolute raw kernel at $z$ equals the kernel at $\operatorname{Re}z$ before gauge averaging. Integration against $|\psi|$ at both ends bounds the absolute matrix element by $\lambda_0(\operatorname{Re}z)$. Convexity gives $|f|\le1$ there. At its centre $q=f(x)=e^{-m-\delta}\in(0,1)$. The holomorphic function $(f-q)/(1-qf)$ has modulus at most one on the disk and vanishes at the centre. Applying the maximum modulus principle after division by $z-x$ gives $s|f'(x)|\le1-q^2$. Dividing by $q$ now gives
\[
 |D_\psi-p'(x)|\le 2s\mathcal M(x)+\frac{2\sinh(m+\delta)}{s}.              \tag{13}
\]
Choose $s=\min(1,\sqrt{m/\mathcal M(x)})$, taking $s=1$ when $\mathcal M=0$. Then $\delta\le m$, $s\mathcal M\le\sqrt{m\mathcal M}$ and $\sinh(2m)\le m\sinh 2$. This proves (12) for every quadratic form value in the eigenspace, and hence for the hidden compression, including multiple levels. It bounds the response of a nearly maximal Rayleigh quotient using only the real vacuum pressure near the coupling.

**PROVED (size of the low-energy bound along the window).** Put $H_{0,\le1}=\sum_{0<m\le1}r^t\operatorname{Tr}_{D_r}(-b_r^h)_+$. On the cold part of the characteristic, $tm\ge a$ and $t\le C_t n$. Equation (12) gives $H_{0,\le1}/W_t\le C(1+\sqrt{C_t n\,\mathcal M/a})$. In particular its upper integral over the cold part obeys
\[
 \int_{I_K\ \mathrm{cold}}^{*}\!\frac{H_{0,\le1}}{W_t}\,dx
 \ \le\ C\!\left(|I_K|+
       2\sqrt{\frac{3 C_t n |I_K|\, B N}{a(\beta_K-1)}}\right).           \tag{14}
\]
For the proof put $d\mu=p''(x)\,dx$ on $I_K^+$. At the vacuum, (2) and (4) give $-BN/x\le p'(x)\le0$ for $x\ge1$. Hence $\mu(I_K^+)\le BN/(\beta_K-1)$. For each $y>0$ the length of $\{x\in I_K:\mathcal M(x)>y\}$ is at most $\min(|I_K|,3\mu(I_K^+)/y)$. To see this, cover a compact subset by finitely many open centred intervals with average density above $y$. Select the longest remaining interval successively, removing those that intersect it. The triples of the disjoint selected intervals cover the original compact subset. The sum of their lengths is at most $\mu(I_K^+)/y$. The superlevel set is measurable by continuity of the fixed-radius averages, and inner regularity gives the claim. Integrating the length bound at $y=z^2$ over $z>0$ yields $\int_{I_K}\sqrt{\mathcal M}\,dx\le2\sqrt{3|I_K|\mu(I_K^+)}$. This proves (14) even if one only uses a measurable majorant for the hidden spaces. Its cost is $O(1+n^2/\sqrt{\beta_K-1})$ at fixed window depth. This grows with $n$ and leaves the running budget of check 1630 open.

## What distinguishes the comparison laws

**ON FILE (rows 1618 Theorem 2, 1622, 1626–1628).** The free transverse photon has coupling-independent vacuum-normalized oscillator energies. In compact Gaussian $U(1)$ with zero monopoles, zero spatial magnetic flux and the three half-turn projections, the joint energies are $E_{\rm ph}+e_Q$, with $e_Q=|Q|^2/(2\beta n)$ and $Q\in(2\mathbb Z)^3$. The Gaussian rescaling is unitary. In that representation the log-multiplier derivative on a product state is $e_Q/\beta$. Within an energy eigenspace the rescaling commutator vanishes. Contractible flowed loops and all their delays are invariant under flat shifts, so their observed part is in $Q=0$. Row 1628 (22) already excludes a positive observed rate in both models. Row 1618 also gives failure of the seed in the compact Gaussian comparison at the prescribed aspect for $\beta\ge1$. [Compact transfer](gap-vir-down-neon.md) · [Observation check, §1.8](gap-vir-down-dom-astra62-check-opus.md) · [Delay comparison](gap-vir-down-twoside-astra62.md)

**PROVED (exactly hidden zero slopes).** Let $q_E$ be the rank of the finite loop-cell observation at one box. At one nonzero lattice momentum take the two transverse oscillator polarizations of the same frequency $\omega>0$. Distributing $j$ quanta over these two modes, with zero occupation in the rest and $Q=0$ in the compact case, gives $j+1$ independent vectors at energy $j\omega$. Choose $j>q_E$. The restriction of $E$ to their span has a nonzero kernel. A unit vector in that kernel belongs to $D_r$ at $r=e^{-j\omega}$, including when other charges share the eigenvalue. The whole $Q=0$ product subspace in this eigenspace is annihilated by $b_r$ by the preceding spectrum and commutator identity. The resulting hidden slope is exactly zero in both comparisons. In the pure photon $H_\kappa=\kappa W_D$. In the compact model all compressions of the diagonal slopes $e_Q/\beta$ are positive semidefinite, so $H_0=0$ and $H_\kappa\le\kappa W_D$. The sign requested in E2 therefore holds even in the seedless compact model. E1 fails in both because its observed trace is zero while $W_t>0$.

**PROVED (the same small-coupling sign in two interacting comparisons).** In four-dimensional Wilson $U(1)$ the Fourier expansion of $e^{\beta(z+z^{-1})/2}$ on the unit circle gives $c_k=e^{-\beta}I_{|k|}(\beta)$. The positive Bessel series gives $I_{j+1}/I_j\le\beta/(2(j+1))$ also at $j=0$. Thus the off-constant normalized multiplier is at most $\beta/2\le1/4$ on the range of (11), and $\beta\,\partial_\beta\log c_k\ge |k|-\beta$ by the same derivative identity. The spatial bound, spatial Haar trial and diagonal trace used in (11) apply verbatim, since $1-\cos\theta\in[0,2]$ has Haar mean one. This proves (11) there. In five-dimensional Wilson $SU(2)$ write $d_5=4n^4$ for the links and $p_5=6n^4$ for the spatial plaquettes. For $\beta\le1/(16p_5)$ the vacuum trial gives $\widehat\lambda_0\ge e^{-2\beta p_5}\ge7/8$, the electric bound is the same as in (11), and $\beta b_\psi\ge5/6-\beta(d_5+2p_5)>1/2$. The trace bound and $\lambda_0\ge e^{-\beta(d_5+2p_5)}$ again give $G(t)<1/2$ for $t\ge1$. These tests concern interacting Wilson actions at small bare coupling. For the weakly coupled interacting compact Wilson $U(1)$ law the Gaussian product spectrum is unavailable here, and its hidden sign is undetermined by these arguments.

**ARGUED (scope of the law dependence, Lemma ALG).** The strict Wilson conclusion (11) fails in both Gaussian models on the hidden oscillator vectors just constructed. Its Wilson proof needs a vacuum concentrated in the constant electric representation and a gain $k/\beta$ from differentiating the nonconstant small-coupling Wilson multiplier. A photon oscillator has zero normalized derivative after Gaussian rescaling, and in the compact model the independent constant holonomy can only add $e_Q/\beta$, which vanishes at $Q=0$. This distinction reads the transfer law. The flat-shift symmetry by itself identifies the observed charge sector and supplies no slope sign. No failure of the desired non-strict E2 sign is involved. For five-dimensional $SU(2)$ the very same one-link integral gives (2). The conjugation (4), the raw positive-kernel domination in (9) and the chord estimate (13) also work there, with $4n^4$ spatial links and $6n^4$ spatial plaquettes. The four-dimensional count in (7) sets an entropy cost, with no lower bound on a signed response. I have no step that fails for typical weakly coupled five-dimensional $SU(2)$ fields. The results give no four-dimensional selective sufficient condition. [Lemma ALG, row 1553](gap-mech-direction4-fable.md)

**ON FILE (non-equivalence, row 1628, mode interchange).** Row 1628 exhibits positive transfers with identical purity and opposite answers to its observed test. This separates that test from spectral purity in its comparison class. A converse restricted to the calibrated Wilson trajectory is open. Equations (8)–(10) here estimate the magnitude of specific omitted terms using the Wilson law. Replacing the full inequality by the inequality on the retained terms alone provides no further progress toward its sign.

**RESULT — (d), first component of E2.**
**PROVED** by hand on the calibrated cold window that levels above $(C_Z+3)n^3/(t-3)$ and slab marks above $2(F+4)n^3/\beta$ can together change the hidden adverse trace by at most $2e^{-n^3}W_t$, (7)–(10). The mark alone costs at most $e^{-3n^3}W_t$ at full spectrum, (10a).
**PROVED** the all-level slope floor (3)–(6), the low-energy pressure bounds (12)–(14), and the strict hidden sign on cold Wilson boxes with $0<\beta\le1/(48n^3)$, (11).
**PROVED** exact hidden zero slopes in both Gaussian comparisons and the small-coupling sign also for interacting four-dimensional Wilson $U(1)$ and five-dimensional Wilson $SU(2)$. The non-strict E2 sign holds in both Gaussian models.
The sign and size relative to the E1 margin of the retained Wilson response on the calibrated window remain open. No rising hidden Wilson level on that window, seed proof or disproof, or mass gap follows. These hand proofs have no independent review.
