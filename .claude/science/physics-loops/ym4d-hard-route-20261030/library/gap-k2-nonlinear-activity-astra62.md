# Repo search

**Source check (proved as a search record).** FINISH row 1492, checkout `e523295691e7`. The target-specific prior file is absent. I searched Markdown and TeX on `origin/main` at `8b11ae2bb95e` and PR refs `pr/10114`, `pr/10133`, `pr/10134`, `pr/10141` at `f76f6c649cff`, `89faef229ff6`, `1e70c7211a2c`, `c73ad7b177d9`. The search for the nonlinear Cartan/stripe centre, the two gap-k2 precursor names, the joint hot denominator and normalized activities at the nonlinear centre returned no hits. Method searches included rooted KP, Kotecký–Preiss, mixed majorant, common local reference, mixed hot/cold, pinned Gaussian singleton, 384-contour and K2-STEP. A further five-ref search for a two-site gauge, coarse dipole, hybrid phase/rate/coercivity, cold complement and principal-chart pin returned no lines. The broad KP search was capped.

- Main’s `research/mass-gap/library/gap-sc-box.md` §0 identifies the abstract finite-gas KP theorem and treats a separate strong-coupling box. On PRs 10114 and 10133, `ym4d-proof/RD4.md` 448–460 obtains the connected log bound (L7) given overlap-component factorization with common local references and a mixed majorant. Its review and `checks/mixsmall_hole_analysis.md` retain both hypotheses. The November 8 digest §9 records the same restriction on using marginal prices. [Prior search](prior/repo-search-2026-11-08.md)
- Main’s `docs/GAUGE_WILSON_SPATIAL_LOOP_AREA_SUPPRESSION_BOUNDED_THEOREM_NOTE_2026-09-07.md` 69–71 uses the implication from the KP row to a pinned sum at most $e^{a_{\rm root}}$. Main’s `docs/WILSON_STAGGERED_CONSTRAINED_FIBER_TWO_LAYER_KP_COMPLEX_SOURCE_POLYMER_BOUNDED_THEOREM_NOTE_2026-07-12.md` (2.10) uses $c|Y|$ for a two-layer gas on its complex domain. Both supply combinatorial comparisons for other activities.
- In this checkout, row 1480 (2), (3), (9), (10) gives the integrated fine-block singleton, its exact vacuum and curvature extraction, the Gaussian-centre violation at fixed angle, and the common denominator. Row 1490 (5)–(7) gives the Hessian, unique local minimum and cancellation of the earlier fluctuation-scale quartic. Its first follow-up asks for this full-domain test. Row 1488 A4 and A8 checked the earlier normalization and Gaussian-centre violation. Registry entries H-SF and H-LF cover the general formation estimate and exact Borel operations. The registry search found no assignment for this nonlinear-centre side-two test. [Row 1480](gap-k2-integrated-activity-astra62.md) · [Row 1490](gap-k2-nonlinear-pin-astra62.md) · [Row 1488](gap-k2-activity-interface-check-opus.md) · [Registry](open-registry.md)

## Result for row 1492

**Proved.** On the coarse $4^4$ torus, at $a=1$, $t=1/8$, the normalized cold singleton specified in row 1490 (7) exceeds even its field-weighted rooted budget. Equation (4) gives a positive exponential rate, and the last finite-coupling estimate gives the explicit witness $x=10^{40\cdot37{,}632}$. The trial field changes the potentials at just two coarse sites. This refutes the fixed-angle extrapolation of the previously proved fluctuation-scale cancellation.

**Proved for a fresh stripe-Hessian Gaussian.** Equation (1) gives the exact marked integral and (2) its joint posterior normalization. At $x=100$, $t=0$, the positive cold complement of row 1490's box by itself exceeds $1-12\cdot10^{-21}$. For the unsplit cold mark that weight cancels at the flat field. Equation (8) gives an all-domain lower bound on every mixed phase for a smaller, explicit volume-independent source interval. The common rooted bound for the *unsplit* marks of the fresh Gaussian remains open on the whole requested interval.

## Plan saved at creation

1. Read the target-specific prior record, GOAL and the requested FINISH rules. Check the repository refs, outline index and registry for prior results and ownership.
2. Recover the finite-volume integral, block coordinates, amplitudes, marked numerators and common denominator from rows 1480 and 1490. Identify the first estimate that remains open.
3. Test the normalized activities on the stated integration domain. Seek either a common rooted Kotecký–Preiss bound or one explicit violation. Record the status and arithmetic basis of each step.
4. Verify the result against the source definitions and record the next two research rows and their decisive outcomes.

## What the published result supplies

**Source check (proved as a statement of scope).** In Sussman and Alpoge, with Claude and Codex, outline 1271–1279 specifies the rooted inequality. At 1368–1373 its application starts “after verifying” that inequality and requires a separate large-field label estimate. QC1–QC3 at 7945–7987 use odd blocks and relative logarithms. The formation hypotheses are explicit at 16350–16355. CA-II 3521–3556 bounds the resummed $|\Phi(X)|$ by $E^*e^{-\kappa d(X)}$ for potentials satisfying the stated Bałaban bounds on its cutoff domain. CA-I 4023–4045 labels the related unmarked-increment proof incomplete. CA-III 1055–1067 quotes constants depending on $d,L$ and uniform in the shell sequence. The local report of Bałaban CMP 109, p. 259, and CMP 122, pp. 175, 185 requires sufficiently small parameters. These are different hypotheses from a numerical bound for the side-two quaternion pin. [Index, chunks 01, 02, 07, 15](sa-index/README.md) · [Indexed obligations](sa-index/obligations.md) · [Bałaban source record](lit-balaban.md) · [Floor-sizing quotations, §3](gap-k2-floor-sizing-opus.md)

## Exact marked integral about the stripe

**Proved.** On a finite periodic coarse four-torus, take periods at least four and an even first period as in row 1480. Fix a unit imaginary quaternion $I$, set $\epsilon_y=(-1)^{y_1}$, $V_{y2}=e^{I\epsilon_yt}$ and the other coarse links equal to one. The parameters satisfy $a=1$, $|t|\le\arcsin(1/4)$ and $x\ge100$. Write $N$ for the number of coarse sites, $n=147N$ for the real dimension of the descending-tree slice, and $W_e=\exp(Z_e)W^*_e(t)$. Take the full principal balls $|Z_e|<\pi$ on free links. Right invariance gives $dW_e=(2\pi^2)^{-1}(\sin |Z_e|/|Z_e|)^2d^3 Z_e$ there. The missing antipodes have Haar measure zero. Let
$$
 S_B(Z)=\sum_{p\in B}(1-\operatorname{Re}W_p)
       +\sum_{c\in B}(|M_c|-\operatorname{Re}(M_c V_c^{-1})),
 \qquad N_1(t)=9-\sqrt{65+16\cos t}.
$$
A positive fine plaquette, fine link or coarse bond is assigned by its base. The mean $M_c$ averages the 384 transporters from the 16 offsets and 24 coordinate orders in row 1480. Each transporter traverses the ordered offset leg, two straight steps, and the inverse translated leg. At the stripe $S_B(0)=N_1(t)$ for every block. Define
$$
 \ell_B=DS_B(0),\quad H_B=D^2S_B(0),\quad H_t=\sum_B H_B,\quad
 R_B(Z)=S_B(Z)-N_1(t)-\ell_B Z-\tfrac12 H_B[Z,Z].
$$
These finite differences define $R_B$ on the *whole* chart, including configurations with $M_c=0$. Taylor differentiability is needed only at the centre, where all the means are nonzero. Row 1490's stationarity gives $\sum_B\ell_BZ=0$ for every $Z$ on the slice. This permits extraction of the **product** of the linear exponentials. The separate $\ell_B$ must occur in the remainder definition when each block is marked. Row 1490 (5) gives $H_t\succeq \lambda\,\mathrm{Id}$ with $\lambda=1/108900$.

**Proved.** Set $h(s)=\int_{SU(2)}e^{-s(1-\operatorname{Re}q)}dq$, $k_0=1/h(x)$ and $\gamma_t=\mathcal N(0,(xH_t)^{-1})$. Let $D_B$ impose the principal balls on every link read by block $B$, $J_B$ be the product of squared sinc factors on its assigned free links, and $C_B$ be the event $|1-W_p|<1/2$ on all its assigned plaquettes. Use
$$
 F_B={\bf1}_{D_B}J_B e^{-xR_B}\prod_{c\in B}\frac{h(x)}{h(x|M_c|)},
 \qquad F_{B,C}=F_B{\bf1}_{C_B},\qquad F_{B,H}=F_B{\bf1}_{C_B^c}.
$$
Multiplying the factors cancels the quadratic in the Gaussian density and the block linear terms by stationarity. In particular
$$
 Z(V)=\frac{k_0^{4N}}{(2\pi^2)^{49N}}
       \frac{(2\pi/x)^{n/2}}{\sqrt{\det H_t}}\,
       e^{-xNN_1(t)}\,
       \mathbb E_{\gamma_t}\prod_B(F_{B,C}+F_{B,H}).
 \tag{1}
$$
The determinant depends on the stripe. For an exact hot set $T$, its posterior probability is
$$
 \frac{\mathbb E_{\gamma_t}\left[\prod_{B\in T}F_{B,H}
                      \prod_{B\notin T}F_{B,C}\right]}
      {\mathbb E_{\gamma_t}\prod_B(F_{B,C}+F_{B,H})}.
 \tag{2}
$$
The denominator is positive by a neighbourhood of the stripe. All patterns share it. The cold factor integrates its entire plaquette cut, including the part outside row 1490 (6). The vacuum and quadratic prescription of row 1480, applied to this new reference, would use $j_x(t)=\mathbb E_{\gamma_t}F_{B,C}$, $P_x(t)=\log j_x(0)+t^2(\log j_x)''(0)/2$. The finite test (5) uses only its vacuum value. For any such deterministic extraction, the normalized marked polynomial is
$$
 \mathcal Z_t(\lambda,\mu)=\mathbb E_{\gamma_t}\prod_B
  \big[1+\lambda_B(e^{-P_x(t)}F_{B,C}-1)+\mu_B e^{-P_x(t)}F_{B,H}\big].
$$
At physical mark values, multiplying by $e^{NP_x(t)}$ restores (1). The same extraction cancels from (2). In particular the normalized cold singleton is $e^{-P_x(t)}j_x(t)-1$. Self-incompatibility in the rooted KP inequality requires $|z_B|e^{u_B}\le u_B$, hence $|z_B|\le1/e$ for every choice of nonnegative $u_B$. The field-weighted test divides by $1+\theta xE_{\widehat B}$, $0<\theta\le1$, with $E_{\widehat B}$ the sum of $1-\operatorname{Re}V_p$ on the enlarged coarse support.

## An obstruction for the activity actually carried forward in row 1490 (7)

**Proved.** There are two distinct marked integrals here. Equation (7) of row 1490 explicitly keeps row 1480's integrated singleton and multiplies $1+z$ by $\exp[-x(G_1-N_1)]$. Here $G_1(t)=4t^2/9$ is the minimized Gaussian energy per block. The extraction cancels the quartic at $t=h/\sqrt x$. At **fixed** $t=1/8$, the same activity violates the field-weighted self-incompatibility budget. The witness is a coarse *site gauge variation of the fine field at fixed source*. Equation (1) defines a second marking convention, compared below.

Take $B$ at the origin of the coarse $4^4$ torus, $w=t/9=1/72$, $\beta=8w=1/9$ and $b=\beta-\sin\beta>0$. At the quadratic mean $m$ the plaquette and pin energy per block is $S(m)=8(1-\cos w)+1-\cos\beta$. Put $A=8\cos w+\cos\beta$ and $L=8\sin w-\sin\beta$. Rotating $8+e^{it}$ by $e^{-iw}$ gives real part $A$ and imaginary part $-L$. Thus
$$
 S(m)-N_1(t)=\sqrt{A^2+L^2}-A
    =\frac{L^2}{\sqrt{A^2+L^2}+A}<\frac{b^2}{16}.                 \tag{3}
$$
Indeed $0<L<b$. Strict concavity of sine between $0$ and $8w$ gives the first inequality, and $L=b-8(w-\sin w)$ gives the second. Also $\cos\beta\ge1-\beta^2/2>8/9$ and $\cos w\ge\cos\beta$, so $A>8$.

Add an Abelian fine-link gradient $I\,d\phi$ to $m$, with $\phi$ constant on each fine block. Choose its values $s/2$ at $B$, $-s/2$ at $B+e_2$, and zero elsewhere, using head minus tail for $d\phi$. The trees stay fixed and all fine plaquette products stay as at $m$. Each contour angle changes by the difference of the two base potentials. The normalized pinned Gaussian in row 1480 therefore charges the trial point the rate
$$
 \tfrac12\|d_{\rm coarse}\phi\|^2=\tfrac12(1+14/4)s^2=9s^2/4.
$$
The central edge has difference $-s$ and fourteen other edges have differences of absolute value $s/2$. There are no periodic identifications among these edges. The Gaussian rate here is relative to its mean, so it includes the quadratic energy of *all* blocks.

For the marked block, the direction-2 difference of the local quadratic and exact pin phases changes from $g(-\beta)$ to $g(-\beta-s)$, where $g(q)=q^2/2-1+\cos q$. As $g''(q)=1-\cos q\ge0$ and $g'(-\beta)=-b$, this gains at least $bs$. In direction 1, where the unperturbed mean is $r=\cos(w/2)>0$, the additional discrepancy is $q^2/2-r(1-\cos q)\ge0$. Directions 3 and 4 obey the same inequality with $r=1$. The Wilson discrepancy stays fixed. All plaquettes of $B$ are strictly cold. With $s=2b/9$, all read logs stay strictly in the principal balls since $b<1/9$ and their old lengths are at most $w$.

In the row-1480 integral restrict to a small open ball about this trial field. The assigned Haar factors are strictly positive and the normalized radial factors have uniform log rate zero by row 1480, lines 162–167. On a fixed torus the Gaussian determinant contributes zero log rate. Integrate on that ball first and shrink it after taking the lower limit. The discrepancy at $m$ is $G_1-S(m)$, the extra gain less the Gaussian cost is at least $b^2/9$, and row 1480 (7) gives $P_x^{\rm old}(t)/x\to0$. Hence the literal singleton $\widetilde z^{(7)}$ of row 1490 satisfies
$$
 \liminf_{x\to\infty}\frac1x\log(1+\widetilde z^{(7)}_{B,C}(1/8))
 \ \ge\ \frac{b^2}{9}-(S(m)-N_1(t))\ >\ \frac{7b^2}{144}>0 .     \tag{4}
$$
Its weighted size eventually exceeds $1/e$ because $1+\theta xE_{\widehat B}$ grows at most linearly on this torus. The change of centre in the *extracted energy alone* therefore fails at fixed angle. The block gradient available to a single mark is different from the one available in the periodic, translation-invariant minimization. The two limits in (4) and row 1490 (7) have different source scalings.

**Proved, the same coefficient in the nonlinear coordinates.** To transport row 1490 (7) without changing any coefficient, take $A_e(Z)=\log(e^{Z_e}W_e^*)$ inside the principal ball, and $A_e(Z)=Z_e$ outside it. Both exponential charts parametrize Haar measure on the ball up to one missing point each. The resulting map is a measure-class bijection off null sets. Put $j(z)=(\sin|z|/|z|)^2$. The change from the old normalized Gaussian to the reference in (1) has density
$$
 L_t(Z)=\sqrt{\frac{\det H_0}{\det H_t}}\,
 \exp\!\left(\tfrac x2 H_t[Z,Z]-\tfrac x2H_0[A(Z)-m,A(Z)-m]\right)
 \prod_{e:\,|Z_e|<\pi}\frac{j(Z_e)}{j(A_e(Z))}.
$$
It integrates to one. Hence the inherited singleton is exactly
$$
 1+\widetilde z^{(7)}_{B,C}
 =e^{-P_x^{\rm old}-x(G_1-N_1)}
  \mathbb E_{\gamma_t}\!\left[L_t(Z) f^{\rm old}_{B,C}(A(Z))\right].
$$
The old factor is row 1480's full local factor, including the radial amplitude. Its exact block phase is $N_1+\ell_BZ+H_B[Z,Z]/2+R_B$. The map preserves every physical plaquette label on its read chart, and keeping the exterior of the principal balls is necessary for an unmarked Gaussian link. Multiplying the full marked products gives (2) with the same hot denominator and the displayed Jacobian and determinant factors.

**Proved scope of (4).** In (1) the Gaussian uses the Hessian at $W^*$ and the local references include $\ell_B$. Introducing indeterminates in (1) changes the coefficient of a single mark compared with introducing them before changing this reference. Both prescriptions give the same partition function at physical mark values and the same (2). Their derivatives at zero marks depend on the choice of reference.

## The cold complement at the actual endpoint $x=100$

**Proved for the stripe-Hessian normalization (1).** Let $t=0$, $x=100$, $B$ the origin block, $\rho=1/97{,}574{,}400{,}000$ from row 1490 (6), and $U_B=\{\max_{e\text{ read by }B}|Z_e|\le\rho\}$. The positive normalized cold weight outside $U_B$ satisfies
$$
 e^{-P_{100}(0)}\,\mathbb E_{\gamma_0}
        [F_{B,C}{\bf1}_{U_B^c}]>1-12\cdot10^{-21}.                 \tag{5}
$$
In particular any expansion that assigns the cold complement its *own positive mark* at this radius violates the rooted self budget already at $100$. The upper bound $12\cdot10^{-21}$ also bounds the physical conditional probability of $U_B$ given any positive-probability hot pattern in which $B$ is cold, using (2).

Choose the positive direction-2 crossing link $e$ with all four tail bits equal to one. All six fine plaquettes reading $e$ have their bases in $B$. For each transverse direction the bases are the tail and the tail minus that transverse unit vector. Only the coarse direction-2 contour family based at $B$ can read this crossing link, and it crosses its face exactly once. Therefore the unmarked quadratic phases of the other blocks are independent of $Z_e$. At $t=0$ the marked Gaussian density after cancellation is proportional to the product of these unmarked Gaussians, the compact Wilson and pin weights of $B$, its Haar Jacobian and its indicators. In particular the conditional integration of this link is with Haar measure times its physical local weights. This statement holds also in the numerator of (2) with the entire hot pattern fixed.

Fix all other links. To bound the numerator with $U_B$ it suffices to consider the slices on which the other read links lie within $\rho$. For $|Z_e|\le R=1/1000$ all assigned plaquettes remain strictly cold, by telescoping their group products. The six containing $e$ have chord at most $R+3\rho$, and the rest have chord at most $4\rho$. The chart cut holds. Varying $Z_e$ from zero to $z$ changes the Wilson log weight by at most $6x|z|$. It changes $M_c$ by at most $|z|$, by the single crossing and averaging. Since $|q_0|\le1$, the log of $F(s)=\int e^{s q_0}dq$ is 1-Lipschitz. Thus the *fully normalized* log pin $x\operatorname{Re}(M_cV_c^{-1})-\log F(x|M_c|)$ changes by at most $2x|z|$. All other factors, including the other blocks' indicators in (2), are independent of this link. A zero-weight slice may be discarded in both integrals.

Compare the integral on the $\rho$-cap to the one on the $R$-cap. The ratio is at most
$$
 e^{8x(R+\rho)}\,
 \frac{\int_0^\rho\sin^2 u\,du}{\int_0^R\sin^2u\,du}
 \le 4e^{8x(R+\rho)}(\rho/R)^3<12\cdot10^{-21}.
$$
Here $u/2\le\sin u\le u$ for $0\le u\le1$, $\rho<10^{-10}$, $8x(R+\rho)<1$ and $e<3$. Restoring every slice in the denominator only improves the bound. At $t=0$, $e^{P_{100}(0)}=\mathbb E_{\gamma_0}F_{B,C}$ exactly, which yields (5). Conditioning on the fixed physical hot pattern cancels the common posterior denominator displayed in (2).

**Proved distinction.** The unsplit cold mark in (1) has expectation zero at this flat field, by its vacuum extraction. If one writes it as $(e^{-P}F_{B,C}{\bf1}_{U_B}-1)+e^{-P}F_{B,C}{\bf1}_{U_B^c}$, the two large normalized coefficients cancel. Equation (5) rules out estimating those two coefficients separately by a common absolute KP majorant. The signed cancellation is available in the unsplit mark.

## Tests of the unsplit Taylor-remainder marks

**Proved, local linear terms.** For example, in $B$ take a direction-2 crossing link with first bit zero. Its contribution to $\ell_B$ in the Cartan direction is $\epsilon_B\sin(v-t)/8=-\epsilon_B\sin v$, where $v=\arg(8+e^{it})$. Exactly one eighth of the outgoing direction-2 contours cross this link. The nonflat $(1,2)$ plaquette contributing the opposite Wilson derivative has base in $B-e_1$. The other assigned pins are aligned. This gives a single-link check that $\ell_B$ need not vanish. Removing it separately without accounting for the unmarked reference would change a singleton.

**Proved, test of Cartan site gradients with a common real lift.** For any set $T$ of marked blocks the rate in the Gaussian integral of their unshifted positive factors is
$$
 \Phi_{T,t}(Z)=\tfrac12 H_t[Z,Z]+\sum_{B\in T}R_B(Z).           \tag{6}
$$
On a real Cartan base gradient, $Z_e=I s_c$ for crossings of $c$, $s_c=\phi_{y+\mu}-\phi_y$, with zero internal logs, every Wilson term is exactly constant. On a marked bond let the unperturbed mean have length $r$ and angle $\theta$ relative to $V_c$. Its contribution after subtracting its constant and linear terms is
$$
 r\{\cos\theta(1-\cos s_c)+\sin\theta(\sin s_c-s_c)\}.
$$
The unmarked bond contributes $r\cos\theta\,s_c^2/2$. On marked bonds $|s_c|\le\pi$ by their chart. For $0\le s\le\pi$, $(s-\sin s)/(1-\cos s)$ increases to $\pi/2$ since its derivative has numerator $2(1-\cos s)-s\sin s\ge0$, by $\tan(s/2)\ge s/2$. Also $1-\cos s\ge 2s^2/\pi^2$ by concavity of sine on $[0,\pi/2]$. Here $r\ge\cos(1/70)>1/2$, $\cos\theta\ge15/16$, $|\sin\theta|\le8/35$ by row 1490. Using $\pi<4$ gives, throughout the actual chart on this family,
$$
 \Phi_{T,t}(Z)\ \ge\ \frac1{40}\sum_c s_c^2 .                    \tag{7}
$$
Indeed $(15/16-16/35)/16>1/40$, and the unmarked coefficient is larger. Thus the two-site gauge mechanism of (4) has a positive cost about the Gaussian defined by the stripe Hessian, throughout the stripe interval.

**Proved, a volume-independent full-domain bound near the flat source.** For all marked sets $T$, on the closure of their full principal charts,
$$
 \Phi_{T,0}(Z)\ge\frac{\|Z\|_2^2}{21{,}000{,}000},\qquad
 \Phi_{T,t}(Z)\ge\frac{\|Z\|_2^2}{42{,}000{,}000}
 \quad\left(|t|\le\frac1{58{,}800{,}000{,}000{,}000}\right).       \tag{8}
$$
This estimate includes hot fields and cold fields outside the convexity box. Extending the angular interval to $\arcsin(1/4)$ remains open.

At $t=0$, let $E_D$ be the block contribution to (6), exact on $T$ and the flat quadratic off $T$. Each plaquette costs half its squared group chord on an exact block or half its squared additive curl on a quadratic block. To bound an internal link, append a positive internal step to the ordered tree path from the base, then commute this last step past at most three steps to its ordered position. Each exchange crosses one elementary square. The tree transports are identity. Thus a group chord or additive link length is at most three times the largest corresponding plaquette defect in that block. The closed principal ball gives $|Z|\le(\pi/2)|1-e^Z|$. In an unmarked block the additive estimate bounds the log directly. Every internal log in $D$ consequently has length at most $6\sqrt{2E_D}$. This is a quantitative form of the square-interchange argument in row 1480, lines 182–193.

For a face from $D$ to $D'$ put $L=\sqrt{2(E_D+E_{D'})}$. Crossing values at adjacent transverse bits differ by at most $13L$ as measured by group chord or additive norm according to the tail label. The connecting plaquette is assigned to $D$ and the two internal edge lengths are at most $6L$ each. Any two crossings are at most three face edges apart. Each labelled contour uses one crossing and at most nine internal occurrences. It therefore differs from any specified crossing by at most $(3\cdot13+9\cdot6)L=93L$, also after averaging. In a quadratic tail block the mean has length at most $L$ by its pin. In an exact one, writing $U$ for the specified crossing and $r=|M|$, we have $|M-r\,1|^2=2r(r-\operatorname{Re}M)\le 2E_D$ and $|1-r|\le|U-M|$. Thus $|1-U|\le187L$, including at $r=0$. In both cases the crossing log has length at most $400L$. Summing squares over at most 32 internal edges and eight crossings per positive face bounds $\|Z\|_2^2$ by $(32\cdot72+2\cdot400^2\cdot8\cdot8)\sum_DE_D<21{,}000{,}000\sum_DE_D$. Each block appears in eight oriented face endpoint slots. This proves the flat bound with arbitrary exact/quadratic interfaces.

For the source perturbation, write $s(t,Z)$ for one plaquette or pin, $m$ for the maximum log length on its support, and $l\le10$ for the maximum path length. Each $W_e^*$ has $t$-derivative of norm at most one, since $|v'|\le1/|8+e^{it}|\le1/7$. Thus varying $t$ costs at most $21|t|$ per exact summand at any $Z$, by path telescoping, the norm triangle inequality and $|V'_c|\le1$. On $\|Y\|_{\infty,\mathrm{supp}}\le1/40$, the means have length at least $1/2$. In directions of local maximum length $m$, the first two path derivatives cost at most $lm,l^2m^2$, and a simultaneous $t$-derivative adds a factor $l$. Indeed each $t$-derivative differentiates one of the $l$ background link factors. The relative-exponential insertions obey the simplex derivative bound of row 1490. The first three norm derivatives on $|M|\ge1/2$ have bounds $1,2,24$. The chain and product rules then give
$$
 |\partial_tD_Zs(t,Y)[Z]|\le410m,\qquad
 |\partial_tD_Z^2s(t,Y)[Z,Z]|\le33{,}000m^2 .
$$
For the pin, the first bound uses $(2+1)l^2+l^2+l$ and the second uses $(24+3\cdot2+1)l^3+l^3+l^2$. Wilson terms cost at most $4^2m$ and $4^3m^2$.

A marked summand of (6) is $s(t,Z)-s(t,0)-D_Zs(t,0)[Z]$. An unmarked one is its quadratic Taylor term. For a marked support with $m\le1/40$, integrate the Hessian difference on the straight segment. The change costs at most $16{,}500|t|m^2$, also valid for an unmarked quadratic at arbitrary $m$. For a marked support with $m>1/40$ the global Lipschitz and centre derivative bounds instead give $(42+410m)|t|\le100{,}000|t|m^2$. Each free link is in at most six plaquette and eight pin supports. Summation gives $|\Phi_{T,t}-\Phi_{T,0}|\le1{,}400{,}000|t|\,\|Z\|_2^2$, proving (8).

In particular, for a fixed torus, a fixed marked pattern and $t$ in (8), the expectation of the product of its positive factors tends as $x\to\infty$ to $\cos(v/2)^{3|T|/2}$ if all its labels are cold, and to zero exponentially if it contains a hot label. To see the first limit, put $Z=Y/\sqrt{x}$ on the $\rho$-product. The limiting quadratic is $H_t$ and its normalized Gaussian integral is one. The product has a Gaussian dominator there. For the radial factor, the substitution $u=k(1-q_0)$ in sphere Haar measure gives $h(k)=c k^{-3/2}\int_0^{2k} e^{-u}u^{1/2}(2-u/k)^{1/2}du$ with a fixed positive $c$. Dominated convergence gives $h(x)/h(xr)\to r^{3/2}$ uniformly for $r$ near the positive centre lengths. There is one mean of length $\cos(v/2)$ per block. The Haar factors tend to one. Outside the product, (8) gives a fixed quadratic gap and a Gaussian tail which absorb the normalization power $x^{n/2}$. All radial and Haar amplitudes are at most one. A hot label excludes the product. This argument covers the whole integration domain.

At $t=0$ the vacuum-normalized joint moments of every nonempty set of *signed* cold and hot marks therefore tend to zero. Expanding each cold $e^{-P}F_{B,C}-1$, and using $e^{P_x(0)}\to1$ gives a finite alternating sum with limit zero. With a hot label every term vanishes. These are fixed-volume limits. The star-incompatible polymer sum at $x=100$ requires quantitative bounds.

**Proved, a residual of the unsplit cold singleton.** Even on the interval in (8), an unweighted $O(1/x)$ bound for this singleton at every fixed angle fails for any vacuum and quadratic extraction. This test eliminates the extraction without differentiating a moving cut. Write $A(t)=\cos(v(t)/2)^{3/2}$. Since $8\sin v+\sin(v-t)=0$, coefficient comparison gives $v=t/9-28t^3/2187+O(t^5)$. From $\log A=-3v^2/16-v^4/128+O(v^6)$ one obtains
$$
 \log A(t)=-t^2/432+\frac{447}{128\cdot9^4}t^4+O(t^6).
$$
For every even quadratic $P_x$, put $1+z_x(t)=e^{-P_x(t)}j_x(t)$. In the combination $\log(1+z_x(2t))-4\log(1+z_x(t))+3\log(1+z_x(0))$, the entire $P_x$ cancels. The proved full-domain limit gives $\log A(2t)-4\log A(t)+3\log A(0)$, which is strictly positive for sufficiently small fixed $t>0$ by the displayed quartic. Choose $2t$ inside (8). The three normalized activities therefore cannot all tend to zero. This excludes a vanishing unweighted budget. The absolute KP self budget $1/e$ is constant, and the curvature weight can grow with $x$ at fixed angle.

**Proved, a bound with the joint denominator retained.** Write $c_*=1/42{,}000{,}000$, $h_T$ for the number of hot labels in $T$, and $d$ for the real dimension of the union of its read links. Integrating out the unmarked exterior Gaussian gives the Schur complement precision $K_t$ on these links. The effective rate at a read vector $z$ is the minimum of (6) over its exterior, since the exact replacements read only $z$. The Gaussian determinant after this integration is $\sqrt{\det K_t}$. On the interval in (8), the effective rate is at least $c_*\|z\|^2$. To bound $K_t$, the centre Hessian per pin is at most $400m^2$ by the first two norm derivative bounds, and a plaquette costs at most $16m^2$, with incidence at most 14. Testing the exterior at zero gives $K_t\preceq6000\,\mathrm{Id}$ for the Schur complement.

Each hot witness requires $\sum_{e\in p}|Z_e|\ge1/2-1/35$ by telescoping from the stripe. Choose one assigned witness per hot block. There is no repeated plaquette, and a link occurs at most six times. Thus $\|z\|^2\ge h_T(1/2-1/35)^2/24\ge h_T/128$. Reserve half the quadratic rate for integration, and use $F_B$'s radial and Haar amplitudes at most one. This gives
$$
 \mathbb E_{\gamma_t}\prod_{B\in T}F_{B,\sigma_B}
 \le (6000/c_*)^{d/2}\exp(-c_*x h_T/256).
$$
Here $d\le735|T|$, since the read links originate in $B$ and its four positive neighbours. For the denominator in (2) integrate all coordinates in $[-1/(100\sqrt{x}),1/(100\sqrt{x})]$. Each mean exceeds $1/2$ in length and each squared sinc exceeds $1/4$. Each radial ratio is at least $2^{-27}$ by the radial bound in the proof of (9) below. The Hessian upper bound $6000 I$ also holds throughout this box by the same local derivative calculation. Stationarity gives $x\Phi_{\mathrm{all},t}\le 3000n/100^2<n$. Thus the denominator is at least
$$
 d_0^N=2^{-206N}e^{-n}
       \left(\frac{2\sqrt\lambda}{100\sqrt{2\pi}}\right)^n ,
 \qquad n=147N .
$$
In particular (2) bounds the probability of $h_T$ specified hot blocks, with any additional cold restrictions, by $d_0^{-N}(6000/c_*)^{n/2}\exp(-c_*x h_T/256)$ on (8). Unspecified labels sum to their full positive factor in the numerator. The volume cost in this estimate prevents it from pricing one hot block uniformly at the endpoint.

## One finite coupling for the violation in (4)

**Proved by hand.** An explicit, deliberately large choice is $x=10^{40n}$ with $n=147\cdot4^4=37{,}632$. The following bounds include the exact integrated vacuum and curvature subtraction.

Set $K=10^{10n}$, $c=1/21{,}000{,}000$, and let $H_0$ be the flat precision. Its norm is below $1000$ because a plaquette row costs at most $4$ times its sum of squared link norms, with incidence six, and a pin row at most $10^2$ times that sum, with incidence at most eight. Write $J(s)=j_x^{\rm old}(s/\sqrt x)$ and $D=\sqrt{\det H_0}/(2\pi)^{n/2}$. We claim
$$
 |J(0)-1|\le K/\sqrt{x},\qquad |J''(0)|\le K/\sqrt{x}.          \tag{9}
$$
Use $Y=\sqrt{x}A$, $u=\|Y\|_2$. At zero source the exact one-mark hybrid rate is $\Phi_{\{B\},0}$ in (8). On its chart both the scaled hybrid and the scaled flat Gaussian exponent are at least $cu^2$. Call their integrands $p$ (with the local Haar, radial and cut factors) and $p_0=e^{-H_0[Y,Y]/2}$, without $D$. Set $p=0$ off the chart. On $u\le\sqrt{x}/40$ all cuts pass, and Taylor's theorem costs at most $4\cdot10^6u^3/\sqrt{x}$ in the exponent, by the at most 100 local terms and the third derivative bound $32000$ from row 1490. For $k\ge1$, the ratio for $-k(\log h)'(k)$ has denominator at least $2/9$ by restriction to $[0,1]$ and numerator at most $2\int_0^\infty e^{-w}(1+w^2)dw=6$. It lies in $[0,27]$. For $r\ge1/2$ and $x\ge100$ this gives $0\le-\log(h(x)/h(xr))\le54(1-r)$, and $1-r\le10u/\sqrt{x}$. Each of the 49 squared sinc factors differs from one by at most $u/\sqrt x$ in this region. Applying $|e^{-v}-e^{-w}|\le |v-w|\max(e^{-v},e^{-w})$ gives
$$
 |p-p_0|\le5\cdot10^6(1+u)^3 e^{-cu^2}/\sqrt{x}.
$$
Outside that region the same bound follows from $u/\sqrt{x}>1/40$ and $p,p_0\le e^{-cu^2}$.

The second $s$-derivative multiplies each integrand at zero by $v^2+w$, where $v,w$ are the first and second derivatives of its log source exponential. The cuts in these *old*, unscaled identity coordinates are independent of the source. The Gaussian derivatives include the completing-square constant $x N G_1(s/\sqrt{x})$. For the origin direction-2 pin the Gaussian term $(QY)_{B2,I}$ becomes $\sqrt{x}\operatorname{Im}_I M_{B2}(Y/\sqrt{x})$, the only change in the hybrid first derivative. Both full first scores have absolute value at most $10Nu$, and their difference is at most $50u^2/\sqrt{x}$ by the path second derivative bound. In the second derivative the constant unit pin response becomes $\operatorname{Re}M_{B2}$, up to sign, costing at most $10u/\sqrt{x}$ by telescoping. The Gaussian $|w|=|2NG_1(1)-N|\le N$. On a bounded source interval at each fixed $x$, the unmarked source changes the exponent by at most a constant times $1+u$ and the marked source reads a bounded mean. A Gaussian tail times a polynomial therefore dominates the differentiated integrals. The normalized Gaussian integral is one for every $s$ and its second derivative is zero. With $N=256$, the bounds just given majorize both errors in (9) by
$$
 D\,10^{15}\int_{\mathbb R^n}(1+u)^5 e^{-cu^2}dY/\sqrt{x}.
$$
Indeed the squared-score difference is at most $1000Nu^3/\sqrt x$. The supremum of $(1+u)^5e^{-cu^2/2}$ is below $10^{30}$, using $1+u\le2\max(1,u)$ and the maximum of $u^5e^{-cu^2/2}$ at $u=\sqrt{5/c}$. The remaining Gaussian integral times $D$ is at most $(1000/c)^{n/2}<10^{6n}$. This proves (9). Conjugation gives $J'(0)=0$. For $\sqrt x\ge 2K$, $J(0)\ge1/2$, so the old extraction at $t=1/8$ obeys $|P_x^{\rm old}(t)|\le1+K\sqrt x$.

In the trial-field argument, $b>\beta^3/7>1/6000$ by the alternating sine bound. The rate margin $7b^2/144$ exceeds $10^{-9}$. Integrate the Euclidean ball of radius $\eta=10^{-16}$ about $m+I\,d\phi$. The local discrepancy minus the Gaussian quadratic cost changes by less than $5000\eta$ there. Since each read log has length below one, the gradient bound for $G_B$ in a unit Euclidean direction is $96\cdot4\cdot4+4\cdot11\cdot10$, and the Wilson and exact pin terms cost at most $96\cdot4+4\cdot20$. The Gaussian cost gradient is at most $1000(6s+\eta)<1000$ because $\|I\,d\phi\|_2=6s$. All cold and chart inequalities persist and all $r$ exceed $1/2$ by telescoping. The rate margin on the ball is therefore greater than $10^{-10}$. The Haar and radial factors together exceed $2^{-206}$ there, using $(\sin u/u)^2\ge1/4$ on $[0,1]$ and $h(x)/h(xr)\ge r^{27}$. The Gaussian density prefactor $Dx^{n/2}$ exceeds one for this $x$ by row 1490 (5). An inscribed cube gives ball volume greater than $10^{-19n}$ since $\sqrt n<200$. Consequently
$$
 1+\widetilde z^{(7)}_{B,C}(1/8)
 > 2^{-206}\,10^{-19n}\exp\{10^{-10}x-1-K\sqrt x\}.
$$
At $x=10^{40n}$, $10^{-10}x-K\sqrt x>10^{-11}x>300n$. Since $\log 10<3$, $N=256$ and $\log(2+12Nx)<12+120n$, the log of the lower bound exceeds $\log(2+12Nx)$. Division of $|\widetilde z^{(7)}|$ by any allowed $1+\theta xE_{\widehat B}\le1+12Nx$ still leaves more than $1/e$. The finite witness uses only these inequalities.

## The adjacent-block test for the unsplit coefficients

**Proved, reduction at $t=0$.** With $D=B+e_1$, write $J_T=\mathbb E_{\gamma_0}\prod_{E\in T}F_{E,C}$. The coefficient of the two cold marks in the connected logarithm is exactly $J_{\{B,D\}}/J_{\{B\}}^2-1$, by translation and the vanishing singleton. Only 301 free links enter the pair after the Schur complement. A single block reads its 49 free links and, from each positive neighbour, the 17 free internal edges and 12 crossing edges. Each internal edge occurs in an ordered offset path. The exterior crossings have incoming bit zero, transverse crossing bit one, and two unrestricted bits, in three transverse directions. Each occurs in a double-crossing plaquette based in the original block. The adjacent supports overlap on just the 29 read edges in $D$, giving $2(49+4\cdot29)-29=301$.

There is an explicit leading check on these signed integrals. In rescaled flat Gaussian variables $Y=\sqrt{x}\,Z$, let $v_i$ be the successive signed imaginary link vectors along a path. With the determinant sign convention of row 1480, the cubic log-weight insertion is
$$
 U_B=-\sum_{p\in B}\sum_{i<j<k}\det(v_i,v_j,v_k)
     -\sum_{c\in B}(QY)_c\cdot
          \operatorname{avg}_{\gamma:c}\sum_{i<j}v_i\times v_j .
$$
Indeed the imaginary part of a contour mean is $gQY+g^2\operatorname{avg}\sum_{i<j}v_i\times v_j+O(g^3)$, $g=x^{-1/2}$. Applying $|M|-\operatorname{Re}M=|\operatorname{Im}M|^2/(|M|+\operatorname{Re}M)$ gives the stated pin cubic. The Haar and radial factors start at degree two in $g$. The Wilson term and the signed minor contractions are those of row 1480, lines 39–68. Consequently
$$
 \lim_{x\to\infty}x\left(\frac{J_{\{B,D\}}}{J_{\{B\}}^2}-1\right)
       =\mathbb E[U_B U_D],\qquad Y\sim\mathcal N(0,H_0^{-1}).
$$
For the limit, expand $(F_{B,C}-1)(F_{D,C}-1)$ on $\|Y\|\le g^{-1/20}$. The third-order action contributes $gU_E$ to each factor there, with error bounded by $C g^2(1+\|Y\|)^6$ after expanding the exponential, since $g(1+\|Y\|)^3$ is uniformly small. The radial bound used in (9) and $1-|M|=O(g^2\|Y\|^2)$ give the same order for that amplitude. Outside this region the product is bounded in absolute value by the sum of the four positive subfamily integrands. Equation (8) gives a tail smaller than any power of $g$ on the fixed torus. Odd Gaussian moments give $\mathbb E U_E=0$, so the normalization and centering preserve the limit. This locates the first pair test. Its limiting coefficient alone cannot decide the finite integral at $x=100$.

**Credits and proof basis.** Tadeusz Bałaban supplied the small-field and large-field variational RG method. Roman Kotecký and David Preiss supplied the rooted polymer criterion. Ethan Sussman and Levent Alpoge, with Claude and Codex, supplied the outline, complete account and contour construction used by the preceding Q2 rows. The bundle revision is the supplied $\mathtt{31a47c543775}$. The new estimates are written arguments using finite-dimensional integration, quaternion algebra and displayed integer or rational inequalities. No machine computation is a proof premise. The stated Lean executable and a Lean command on the search path were both unavailable. The proof basis is the written derivation. This is research text awaiting a separate reader and grants no scientific or audit status.

## Next two rows and their decisive outcomes

1. **Sketched row. The exact two-block test at $x=100$.** Evaluate or enclose $J_{\{B,D\}}/J_{\{B\}}^2-1$ for the adjacent pair just specified, with its 903-dimensional Gaussian marginal, the actual radial factors and the unsplit cold cut. The rational flat precision on the $4^4$ torus admits a coarse Fourier calculation in $\mathbb Q(i)$ with 49 link indices per momentum. An endpoint interval above $1/(81e)$ in absolute value refutes a common KP bound for this translated pair activity. Shifting its first site within one star gives 81 incompatible translates of each root pair. Applying the row at the least KP weight on that orbit gives the threshold. A certified upper interval below that number removes this particular obstruction. A finite computation used to decide the inequality needs a kernel-checked certificate.
2. **Sketched row. Connected bounds with the cold complement combined.** For the exact coefficients of (1), integrate each signed cold factor before pricing its complement. Compare marked regions to the full denominator (2) through their shared boundary and sum the connected terms with the stripe covariance, starting from the explicit all-domain estimate (8). A uniform rooted row over $|t|\le\arcsin(1/4)$, $x\ge100$ would establish the remaining majorant. A single unsplit coefficient on a specified torus above its translation or self budget would refute it. The volume cost $d_0^{-N}$ in the present hot estimate identifies the loss that a local comparison must remove.
