# Repo search

**ON FILE (search for row 1642).** This author-only research note uses checkout `2f93929d3`.
I searched `origin/main` (`8b11ae2bb95e`), `pr/10114` (`f76f6c649cff`),
`pr/10133` (`89faef229ff6`), `pr/10134` (`1e70c7211a2c`) and
`pr/10141` (`c73ad7b177d9`). “PUR-io”, “VIR-down”, “magnetic action
deficit”, “cold thermal slope”, “toron Hamiltonian”, “Karsch coefficients”
and the follow-up for a bounded tilt of a fluctuating holonomy readout gave no hit.

| Other search terms | Relevant hit and its scope |
|---|---|
| Small-volume spectrum, zero-mode Hamiltonian, bosonic matrix Hamiltonian, compact toron | Main, `research/mass-gap/library/gap-phys-seed.md` §1.2 (row 720) and `prior/gap-small-volume-lit.md` lines 40–58 report the leading periodic-box neutral excitation at scale $g^{2/3}/L$ from nine constant modes. The scalar coefficient quoted there is numerical. Item 18 in each of `gap-crux-fp.md`, `gap-flux-exercise.md`, `gap-form-exercise.md` and item 8 in `prior/gap-seed-lit.md` use the same small-volume spectrum. None supplies a uniform transfer error. Other zero-mode hits refer to Fierz–Pauli gravity. |
| Source transport | PR 10133, `MASS_GAP_CROSSOVER_REDUCTION.md` §§2–3 gives H4 at strong coupling and H5 for weak finite-volume effective actions. MG2 (source transport) and CW (clustering across crossover) are open. |
| Smeared or flowed winding, zero-mode heat trace, straight winding holonomies | All five refs, `NATIVE_ZERO_PENALTY_L4_DELAYED_SPLITTING_NOTE` line 140 constructs a signed configuration of winding $+1$. A single configuration gives no vacuum distribution. |
| One-site Wilson transfer, one vertex, three axes, heat trace | In the pinned lane, row 1227, `gap-solve25-astra62.md` (5), (7), proves the **entire one-vertex neutral heat-trace limit**, checked in 1230 §6. My initial name search missed “one vertex”. I stopped that derivation and use its result in §2. No registry row owns the positive-flow comparison in §3. |

## 1. What the checks establish

**ON FILE (rows 1453, 1461–1465, 1527).** For fixed release witnesses, one
$\ell\in1024\mathbb N$, $n=\ell b^K$ and $u=n/512$, let
$G(t;\beta)=\sum_{i>0}(\lambda_i/\lambda_0)^t$ on the neutral sector.
The sixteen twisted partition functions in gap-k2-tool-design-fable.md §3.1
give $P_K=Z_+(2u)/Z_+(u)^2$. Infinitely often $P_K\ge457/625$ suffices.
Check 1527(ii) also permits a lower threshold with its change of aspect.
The formal seed-to-gap step is in `lean/gapchain`. The seed is open.

| Standing | Result, restriction and anchor |
|---|---|
| ON FILE, rows 1597–1609 | Check 1598 leaves the swap and carry triggers unmet. Row 1599 is a held watch. Checks 1605 and 1607 identify bounded whole-slice criteria with the seed at the stated aspects and thresholds. The specified fixed-lattice cells, raw-link swaps and short time periods fail. A one-cell estimate at *physical* separation remains open. Check 1606 shows that pinning sparse walls works in general finite-range systems. Averaging the walls again requires the original mixing estimate. Row 1604 is a literature reading, 1608 stopped and 1609 did not run. |
| ON FILE, rows 1610–1616, 1620 | Check 1612 finds an extra charged-sector and cap cost in the auxiliary cylinder. Check 1620 finds that centre projection removes the charged cost and leaves the cap and variation cost. Its proved interval shrinks in physical units. Rows 1614–1615 stopped. Check 1613 verifies finite-box regularity and the thermal transport implication of row 1610 using the partial derivative at fixed time. Strictness on the calibrated Wilson trajectory is open. |
| ON FILE, rows 1617–1623 | A common dilation of *all* ordered neutral levels by any factor $E>1$ fails on every finite Wilson box. The three proofs use the same high-level mechanism (checks 1621–1622). High-spin cutoff and finite-period errors are controlled. In the compact Gaussian comparison a cold rate of order $1/\beta$ is possible. It gives no uniform positive rate on a fixed-depth late window. Row 1623 reports no literature supplier of that rate. |
| ON FILE, rows 1624–1630 | Check 1625 verifies the signed conditional-action test. Check 1627 finds it can fail on strong-coupling Wilson boxes even where the thermal rate passes. The two-sided versions in 1628–1629 improve the loss. Check 1630 §§1.2–1.4 permits any constant $\kappa_0>0$ if $r$ is fixed first, $\ell=L_h b^r$, and the longer window covers the required cooling budget. Along a passing characteristic the accumulated speed must satisfy (RB) at *every* intermediate coupling. |
| ON FILE, rows 1631–1641 | Check 1634 validates tails and a sign only at very small bare $\beta$. Check 1635 verifies the cancellation of the hidden-energy charge and the remaining cost of rising hidden levels. Checks 1639–1640 validate upper bounds, the magnetic/anisotropy split, Gaussian comparisons and a fixed-box strong-coupling sign. The claimed reversal of the magnetic sign on the interacting band fails as a proof (1640 §2). Row 1641 closes the E1/E2 test route. |

**ON FILE (check 1635 §8).** If the time-delayed observations miss no
states, E2 is empty and E1 is precisely thermal VIR-down with a margin.
**ARGUED (rows 710 §8, 1386, 1633, 1639–1640).** Completeness of those
observations is conjectural. Given a suitably bounded anisotropy response,
the magnetic action deficit would have to supply an order-one rate.
Both the anisotropy bound and the positive deficit on the band are open.
The action sum rule identifies the observable whose typical-field sign
and size would be needed.

**ARGUED (choice for this row).** I rank C2 of row 1610 first. It has an
independent consumer, and a compact periodic Wilson reference whose thermal
spectrum can be determined without knowing the band slope. I would spend
the next comparison effort on fluctuations *discarded* by a spatial block
on this small box. A further rearrangement of E1 has no such supplier.
The following calculation concerns the hot endpoint alone.


### Scope of the prior sources

**ON FILE (rows 244, 531, 729, 1143, 1215/1221, 1273/1279, 1386/1387).**
The November 8 repository digest concerns earlier ultraviolet obligations.
The direction-specific prior file is absent at this pin. I searched FINISH,
parts, library, open-core, l17c and the registry for compact holonomies,
rotors, quartic valleys, thermal traces and flow. WMIX-SLICE, LEV-FAIL
and VIR-DOWN are the registered routes at lines 1028–1030. Rows 1143
and 1215/1221 give fixed-box bounds and a twisted normal-fibre oscillator.
Row 1273 §5 and check 1279, Lemma S, give confinement down the commuting
valleys of the noncompact quartic Hamiltonian, crediting Barry Simon.
Check 1387 points to 1215 (5) and 1227 (11) for fixed-box neutral
coalescence and explains the limitation of thin lines.

**ON FILE (SA index, rows 244, 531).** Chunks 01, 08 and 29 and obligations
lines 24 and 1498 point to outline lines 588–599, 9558–9577 and 31871–31882.
Sussman and Alpoge, with Claude and Codex, bound the classical constrained
flat quadratic operator with prescribed holonomies and exhibit a polynomial
correlator with spectral support at zero. Chunk 02, GL3 and GL8 (outline
2197–2214, 2315–2329), supplies positive convolution and the finite
gauge-projected transfer. CA-I 2705–2712 excludes a mass gap from
Theorem 0. CA-II 83289–83309 gives a covariance on the clean Gaussian
branch. CA-III 4972–4985 takes a difference of two runs on a common
scaffold. None gives the comparison in §3. The supplied source copy is
attributed to `31a47c543775` and carries no local Git metadata.
The Bałaban quotations in `lit-balaban.md` §§2–3 concern RG estimates.

## 2. The already solved reference

**ON FILE (row 1227, gap-solve25-astra62.md lines 19–95, check 1230
§6).** On a periodic spatial lattice of one vertex, write the three
$SU(2)$ links as unit quaternions $q_i=(s_i,u_i)$. The transfer in electric
normalization is $T_B=M_B C_B M_B$. Here $C_B$ convolves each link with
Haar density proportional to $\exp[B(\operatorname{Re}y-1)]$ and
$M_B=\exp[-BV/2]$ with $V=2\sum_{i<j}|u_i\times u_j|^2$.
Impose simultaneous conjugation and the three independent centre flips.
Write $\epsilon=B^{-1/3}$ and order the transfer eigenvalues downwards.
The limiting operator on rotation-invariant functions of three colour vectors is
$H=-\tfrac12\Delta+2\sum_{i<j}|x_i\times x_j|^2$, with eigenvalues
$e_0<e_1\le\cdots$. Row 1227 equations (5), (7) prove
\[
 (1-\lambda_j(B))/\epsilon\to e_j,\qquad
 \sum_{j>0}(\lambda_j(B)/\lambda_0(B))^{\lceil\tau/\epsilon\rceil}
       \to\sum_{j>0}e^{-\tau(e_j-e_0)}<\infty\quad(\tau>0).              \tag{1}
\]
That row also proves strong $L^2$ precompactness of bounded-energy vectors
in the centre-folded chart $q_i=\exp(\epsilon x_i)$, including the square
root of the Haar Jacobian. Its positive normalized vacuum converges there
to the positive vacuum $\phi_0$ of $H$. Its counting estimate (8) controls
the thermal tail in (1).

**ON FILE (rows 1227/1230, 1273/1279).** The compact reference, its gap,
its entire thermal trace and the noncompact limiting oscillator are already
covered. I stopped the duplicate one-site target on locating row 1227.
Section 4 builds on it by restoring fluctuating nonzero modes in the
measurement as well as in the thermal trace. In particular the proposal
does not impose the same fine link everywhere. Row 1227 after (8) proves
that this bare homogeneous restriction gives the wrong thermal time.

## 3. A target on the actual hot Wilson box

**GUESSED (hot-box comparison).** Fix one weak physical box $L_h$, an allowed
release calibration $g_0$, and a **box** inverse coupling $B$ chosen once,
independently of $K$. The bare inverse coupling on the fine lattice is
$\beta_{K+r}$, which diverges. Set $d=3$ and
\[
 \tau_0=\log(2)/(e_1-e_0),\qquad q=\lceil\tau_0 B^{1/3}\rceil .
\]
By (1) we may take $B$ large enough that the first excited ratio of the
one-site transfer at time $q$ lies in $[2/5,3/5]$. This time resolves a
slow excitation. The reference already has $G(q)>4/21$ there.

Use the ground-state representation of each neutral transfer. If $\Omega$
is its normalized positive vacuum, the stationary slice law is
$\pi=\Omega^2\,d\mu$, and its Markov operator on invariant functions is
$D f=(\lambda_0\Omega)^{-1}T(\Omega f)$. Denote the fine operator by
$D_n$ and the reference by $D_B$. Let $\pi_B$ be the reference vacuum law.
On the fine spatial slice, run the Wilson gradient flow for $(n/128)^2$
lattice time units, with the spatial action without $\beta$ and the round
link metric, as in row 1624 line 45. From a common base point read the
three winding holonomies of the flowed field, $Y$. This choice of winding
observables differs from the contractible squares in row 1624.
Let $\nu_n$ be the law of $Y$ in the fine vacuum. The centre flips and
simultaneous conjugation act on the triple as in §2. On invariant functions use
\[
 J_n f(x)=
   \sqrt{\frac{d\pi_B}{d\nu_n}(Y(x))}\, f(Y(x)).
\]
This is an isometry by change of measure. Both densities with respect to
product Haar are strictly positive at finite $n,B$. The finite-time flow
is a diffeomorphism of a compact manifold. Before flow, vary one link
on each of the three edge-disjoint lines to change that product arbitrarily
with the other two fixed. Product Haar gives the three products independent
Haar laws, and pushing forward a strictly positive smooth slice density
preserves equivalence. One can take the quotient by both symmetries throughout.

The proposed estimate, at $n=L_h b^{K+r}$ and $\beta_{K+r}$ on an infinite
subsequence, is
\[
 \big\|D_n^{\,qn}-J_nD_B^{\,q}J_n^*\big\|_{\rm HS}\ \le\ 1/10 .       \tag{2}
\]
Choose $L_h$ in the allowed side class so $\ell=L_h b^r$ is a multiple of
1024. The matching of $B$ to this box is a physical assertion in (2).
It does not follow from the definition of the bare coupling.

**PROVED (consumer).** On a passing box let $p_1$ be the largest excited
eigenvalue of $D_n^{qn}$. The min–max principle and
$\|\cdot\|_{\rm op}\le\|\cdot\|_{\rm HS}$ give
$3/10\le p_1\le7/10$. Thus at the comparison time the fine box still
has $G(qn;\beta_{K+r})\ge3/10>4/21$. Moreover
$\|D_n^{qn}\|_{\rm HS}\le M:=\|D_B^q\|_{\rm HS}+1/10$.
Consequently
\[
 G(2jq n;\beta_{K+r})\le (7/10)^{2j-2}M^2,\qquad j\ge1 .             \tag{3}
\]
Indeed every excited eigenvalue $p$ obeys $p^{2j}\le(7/10)^{2j-2}p^2$.
Choose $j$ so the right side is at most $1/10$. This gives a fixed
hot cooling aspect $\alpha_h=2jq$. Choose $r$ **after** $B,q,j$ and a
trial $\kappa_0>0$, **before** $K$. Check 1630 §1 gives a window width
at least $sr-W(r)$, where $s>0$ is the calibrated mean increment and
$W(r)=O(1+\log r)$ uniformly in late $K$. Take
$\kappa_0(sr-W(r))\ge\log(512\alpha_h)$.
Then $t_h=(n/512)\exp[\kappa_0(\beta_{K+r}-\beta_K)]\ge\alpha_h n$.

**ON FILE (rows 1610, 1613, 1630), with the margin in (3).** The further
hypothesis is thermal VIR-down at this rate on the cold portion of
$t(\beta)=u\exp[\kappa_0(\beta-\beta_K)]$. In those variables it says
$\partial_\beta G+\kappa_0t\,\partial_tG\ge0$. If it holds whenever
$G\le4/21$ on the characteristic, (3) and the last-crossing argument give
$G(u;\beta_K)\le1/10$. No crossing from above $4/21$ can end at $1/10$
with nonnegative derivative after the last crossing. Time monotonicity
justifies using (3) at the longer $t_h$. Now
$P_K\ge(1+G(u;\beta_K))^{-2}\ge100/121>457/625$ on the **same** side.
In particular, with $\alpha_*(\beta)=n^{-1}\inf\{t\ge1:G(t;\beta)\le4/21\}$,
these hypotheses entail the running budget
$\kappa_0(\beta-\beta_K)\ge\log_+(512\alpha_*(\beta))$ at every
intermediate coupling (check 1630, RB). Proving that transport on the
Wilson band is a separate open problem.

**PROVED (what (2) tests besides purity).** Its left side depends on
eigenfunctions and on fine states orthogonal to the coarse variables.
Let $k_n$ be the kernel of $D_n^{qn}$ relative to the stationary probability
on the invariant quotient. Under two independent stationary slices
$X,X'$, put $k_c=\mathbb E[k_n(X,X')\mid Y(X),Y(X')]$ (with quotient
observations). Write $h^2=d\pi_B/d\nu_n$ and let $k_B$ be the kernel of
$D_B^q$. The squared norm in (2) is exactly
\[
 \mathbb E\,|k_n-k_c|^2+
 \big\|k_c(y,y')-h(y)k_B(y,y')h(y')\big\|^2_{L^2(\nu_n\otimes\nu_n)}. \tag{4}
\]
This is orthogonal projection in $L^2$ of the pair. The first term includes
every discarded fluctuation. Agreement of a collection of measured coarse
correlations bounds neither term by itself.

A thermal seed or even purity one does not imply (2) as a transfer
criterion. For example, the Wilson transfer at $\beta=0$ has rank one
on every box, so its purity is one at each positive time. For **any**
isometric identification its distance in (2) is at least $2/5$ by the
second eigenvalue. One can take strictly positive couplings on each fixed
box close to zero by continuity of the continuous kernels in Hilbert–Schmidt
norm and of their isolated top eigenvalue. Conversely (2) uses the hot
coupling only. In an abstract positive transfer family one may keep that
operator and add two nearly equally weighted levels at the cold end
(e.g. a two-state Markov factor, rank one at the hot end, with excited
ratio $\exp(-1/n^2)$ at the cold end). Its cold purity has limit superior at most
$1/2$, since product purities multiply and each is at most one. Taking the hot embedding to include
the constant spectator makes the hot norm identical. Thus the proposed
component is not a spectral rewriting of the seed. These separations do
not settle logical strictness within the **one calibrated isotropic Wilson
trajectory**. I cannot prove that converse fails there.


### 3.1 A necessary test on one Wilson slice

**PROVED.** Write $p=\lambda_1(D_B^q)$ and let
$A_n=\int\sqrt{d\pi_B\,d\nu_n}$. The error in (2), even in operator norm,
is at least
\[
                         (1-p)\sqrt{1-A_n^2}.                         \tag{5}
\]
In the fine Hilbert space, $D_n^{qn}1=1$ and the unit top vector of
$S=J_nD_B^qJ_n^*$ is $J_n1$. Its inner product with $1$ is $A_n$.
On its perpendicular space $I-S\ge (1-p)I$. Apply $D_n^{qn}-S$ to $1$.
In particular (2) requires $A_n^2\ge15/16$, using $p\le3/5$.
This single-slice comparison can be tested before estimating a two-ended
kernel. It has no sufficiency claim.

**ON FILE (row 1145 §1, checks 1146 and 1361).** At a fixed physical
mesh, the unflowed straight winding transports approach independent Haar
on the calibrated fine torus. The bound is uniform in the other links
and in the time length and passes to the vacuum. Row 1145 already uses
this to reject a transplant of fixed-box holonomies.

**PROVED (application to (2)).** Choose a fixed $z>0$ so the Haar mass
of $S_z=\{|\operatorname{Im}q_1|\le z\}$ is below $1/32$.
By the reference vacuum localization of row 1227, $\pi_B(S_z)>15/16$ for
sufficiently large $B$. With zero flow the preceding on-file result gives
$\nu_n(S_z)<1/16$ eventually. Splitting the affinity over $S_z$ and its
complement gives $A_n\le1/2$ by Cauchy–Schwarz. Thus (5) is at least
$\sqrt3/5>1/10$ on actual late Wilson boxes with this readout. This is a
consequence of row 1145 for the proposed norm. The positive-flow test
has a different marginal and is open.

**PROVED (a scale-sensitive observable of the reference law).** In its
vacuum, $\min(1,B^{2/3}|\operatorname{Im}q_1|^2)$ converges in law and in
both bounded moments to $\min(1,|x_1|^2)$ under the density $|\phi_0|^2$
of the quartic ground state. This follows from the strong vacuum convergence
in row 1227, using $|\operatorname{Im}\exp(\epsilon x)|=\sin(\epsilon|x|)$. The limiting variance is positive since $\phi_0>0$ on sets both
inside and outside the unit ball in $x_1$. If the magnetic factor $M_B$
is set to one in the very same $SU(2)$ transfer, the vacuum is Haar and
the variance tends to zero. The distinction reads a field law with the
group, dimension, centre and observable held fixed.


## 4. Building the comparison with spatial fluctuations present

**PROVED (product model with a fluctuating readout).** The following
benchmark includes *all* nonzero spatial momenta and lets them perturb
the measured holonomy. It uses the compact vacuum from row 1227. It
does not assume a projection onto its excited eigenvectors is available
in the observation.

Use a three-dimensional spatial grid of side $n\ge4$. In addition to the
three compact links $U$, take three independent colours of the zero-mode-free
transverse Gaussian lattice photon. Here colour rotates all fields together.
The stationary law is the product of
the compact Wilson vacuum at $B$ and the Gaussian vacuum of stiffness $B$.
Over one box length let the transfer be $D_{B,\mathrm{all}}\otimes D_{\rm ph}^n$
in stationary variables. The first factor is the same compact transfer
acting before the simultaneous colour projection. Keep the centre-even
joint colour singlets. In particular, a pair of coloured factors coupled
to a singlet is included. Denote this restricted one-box transfer by $D_*$
and write $J_0 f(U,\xi)=f(U)$.

Put $\sigma=128^{-2}$. Run the linear spatial heat flow on the transverse
field for time $\sigma n^2$. Its three-colour value on link $(x,i)$ is
$A_i^\sigma(x)$. Take the **ordered product** of $\exp A_i^\sigma(x)$
along the $i$th winding line from the origin, in path order, and call it
$H_{\xi,i}$. Read $Y_i=U_i H_{\xi,i}$. This places the compact holonomy
at the seam. Each readout is an exact product of noncommuting matrices.
The field being flowed is Gaussian and independent of $U$. Use the
isometry $J$ of §3 for this $Y$. Then, for $q=q(B)$ above,
\[
 \lim_{B\to\infty}\ \sup_{n\ge4}
       \|D_*^q-J D_B^q J^*\|_{\rm HS}=0 .                            \tag{6}
\]
This asks the noisy observable to recover the operator and also charges
the thermal weight of states it discards.

**PROVED (size and time scales in (6)).** For a nonzero centred integer
momentum $m$ write $\widehat k^2=4\sum_j\sin^2(\pi m_j/n)$ and
$\omega=2\operatorname{arsinh}(\widehat k/2)$. The stationary variance of
one transverse Fourier coordinate is $(2B\sinh\omega)^{-1}$ (row 1638
§1, checked in 1640 §2, or direct Gaussian completion of the square).
With the unitary spatial Fourier transform, the diagonal transverse
projector satisfies $0\le P_{ii}(m)\le1$. Thus, at any spatial link,
\[
 \mathbb E|A_i^{\sigma,1}(x)|^2=
 \frac{1}{2B n^3}\sum_{m\ne0}
        \frac{P_{ii}(m)e^{-2\sigma n^2\widehat k^2}}{\sinh\omega}
 \le\frac1{8B n^2}\sum_{m\in\mathbb Z^3\setminus\{0\}}
               \frac{e^{-32\sigma |m|^2}}{|m|}.
\]
Here the superscript $1$ denotes one colour and
$\sinh\omega\ge\widehat k\ge4|m|/n$ in the centred zone.
Bi-invariance and Cauchy–Schwarz give
$d(H_{\xi,i},1)^2\le n\sum_{x\text{ on line}}|A_i^\sigma(x)|^2$.
This bound holds in path order, with arbitrary correlations along the line.
The mean squared displacement of the triple is $O(B^{-1})$, uniformly
in the grid. Its root mean square is smaller than the reference vacuum
width $\epsilon=B^{-1/3}$ by a factor $O(B^{-1/6})$.

All Gaussian modes must also be counted in the thermal trace. The photon eigenvalue ratios are products of
$e^{-k\omega}$, $k\ge0$ for each oscillator (rows 1618, 1622).
There are at most six real oscillator labels per momentum when counted
over the whole centred grid. Since $\widehat k\le2\sqrt3$,
$\omega\ge c|m|/n$ with $c>0$ independent of $n$. The log of
$\operatorname{Tr}(D_{\rm ph}^{2qn})$ is at most
$6\sum_{m\ne0}-\log(1-e^{-2cq|m|})=O(e^{-c' q})$ for $q\ge1$
with $c'>0$. This follows by summing over unit shells, each with at most
$C(k+1)^2$ momenta. The squared Hilbert–Schmidt norm after subtracting
the photon vacuum projector is that trace minus one.

For the compact factor before the colour projection a polynomial bound
suffices. Integrating the single-link weight over the group ball of radius
$B^{-1/2}$ gives a normalizer at least $cB^{-3/2}$, since the Haar
volume has that order and the weight is bounded below on the ball. With
three links and $M_B\le1$, the unprojected Haar kernel is everywhere
at most $C B^{9/2}$. Its Hilbert–Schmidt norm obeys the same bound.
The full top eigenfunction is positive and unique and hence invariant
under centre flips and colour, so its eigenvalue is the $\lambda_0$ of
(1). Since $T_B/\lambda_0$ is a contraction and $\lambda_0\to1$,
$\|D_{B,\mathrm{all}}^q\|_{\rm HS}\le C' B^{9/2}$ for $q\ge1$.
This polynomial times the exponentially small photon residual tends to
zero at $q\asymp B^{1/3}$. Project the tensor product onto joint singlets.
Its photon-vacuum part is exactly $J_0D_B^qJ_0^*$. Compression reduces
the residual norm, including the contribution from coloured pairs.

**PROVED (stability of the density correction).** It remains to replace
$J_0$ by $J$. Write $\psi_j$ for normalized Haar-space reference neutral
eigenfunctions, $\psi_0>0$, and $f_j=\psi_j/\psi_0$. Let $H_\xi$ be
the triple of ordered group products, independent of $U$,
and let $\mathbb E_\xi$ integrate over the Gaussian vacuum.
For fixed $j$, uniformly along any sequence of grids,
\[
 \mathbb E_\xi\|\psi_j(\,\cdot\,H_\xi^{-1})-\psi_j\|_{L^2(dy)}^2=o(1).
                                                                    \tag{7}
\]
Indeed the compactness in row 1227 gives a subsequence on which the
rescaled eigenfunctions converge strongly. Approximate their limit in
$L^2$ by a smooth compactly supported function and lift it back with the
chart Jacobian of §2. The lift has invariant-gradient norm $O(1/\epsilon)$.
Haar translation and integration along the shortest group geodesic bound
its squared translation error by $C\epsilon^{-2}\mathbb E d(H_\xi,1)^2
=O(B^{-1/3})$. The approximation error on either side has unchanged
$L^2$ norm. Taking it to zero proves (7) on the subsequence.
Every sequence has such a subsequence, which gives the asserted limit.

Change variables to $y=UH_\xi$ in product Haar and Gaussian measure.
Let $b(y)^2=\mathbb E_\xi\psi_0(yH_\xi^{-1})^2$ and
$w(y,\xi)=\psi_0(yH_\xi^{-1})/b(y)$, so $\|w(y,\cdot)\|_2=1$.
Multiplication by the original vacuum converts the two embedded vectors
$J_0 f_j,J f_j$ to
$\psi_j(yH_\xi^{-1}),\,\psi_j(y)w(y,\xi)$, respectively. At $j=0$,
\[
 \psi_0(y)\|1-w(y,\cdot)\|_2
 \le 2\|\psi_0(yH_\xi^{-1})-\psi_0(y)\|_2 .
\]
To verify this, insert $b(y)w$ and use
$|b(y)-\psi_0(y)|\le\|\psi_0(yH_\xi^{-1})-\psi_0(y)\|_2$.
At other fixed $j$, approximate $\psi_j$ by a bounded multiplier times
$\psi_0$ in $L^2$, uniformly along the converging subsequence, to any
prescribed accuracy. In the rescaled chart the limit ground state is
positive almost everywhere. Truncate the ratio of the two limiting
functions on a large compact set, then pull that bounded multiplier
back. Strong convergence of both vectors bounds the approximation error.
Since $\|1-w(y,\cdot)\|_2\le2$, the ground-state estimate and (7) now give
$\|(J-J_0)f_j\|\to0$. This handles the actual density correction, which
could be large on rare values of $Y$.

Multiply the last squared norm by $(\lambda_j/\lambda_0)^{2q}$ and sum over
$j$. It is bounded by four before multiplication. Equation (1) and convergence
of each fixed level make the weighted tails uniformly small as $B\to\infty$.
This gives $\|(J-J_0)D_B^q\|_{\rm HS}\to0$. Expanding the difference between
$JD_B^qJ^*$ and $J_0D_B^qJ_0^*$ costs at most twice this norm.
Together with the photon estimate it proves (6). No computation enters the proof.

### 4.1 An interaction allowed by the comparison

**PROVED (stability under a bounded joint potential over one box time).**
On the same joint invariant space let $\mu$ be the product stationary law.
Allow a real invariant potential $W(U,\xi)$ with
$\|W-c_{B,n}\|_\infty\le\delta_B$, uniformly in the grid, for some scalar
$c_{B,n}$. Suppose $q\delta_B\to0$. Form $S=e^{-W/2}D_*e^{-W/2}$ and
let $\lambda,\omega>0$ be its top eigenvalue and normalized eigenvector
in $L^2(\mu)$. The finite-grid kernel is strictly positive and compact.
Use its ground-state Markov operator $D_W$ on $\omega^2\mu$ and form
$J_W$ from the *new* law of the same ordered products $Y$. Then (6)
holds with $D_W,J_W$ in place of $D_*,J$. For instance
$W=B^{-1/2}F(U)G(\xi)$ couples the two sets of variables when $F,G$
are bounded, nonconstant invariant functions. The scale in this theorem
is per box time.

Subtract the scalar from $W$, which preserves $D_W$. The Rayleigh quotient
on $1$ and the multiplier norm give $e^{-\delta_B}\le\lambda\le e^{\delta_B}$.
By positivity of the kernels and integration over the $q-1$ inner
slices, the kernel of $\lambda^{-q}S^q$ lies between $e^{-2q\delta_B}$
and $e^{2q\delta_B}$ times the kernel of $D_*^q$. Hence their
Hilbert–Schmidt distance is at most $(e^{2q\delta_B}-1)\|D_*^q\|_{\rm HS}=o(1)$.
By (6) and the reference bound, the spectrum of $D_*^q$ off its
constant vector lies in $[0,3/5+o(1)]$. Applying the distance bound
to $\omega$ gives $\|(I-D_*^q)\omega\|_2=o(1)$. Its component orthogonal
to $1$ tends to zero. Positivity and normalization give $\|\omega-1\|_2=o(1)$.

Multiplication by $\omega$ maps the new stationary space unitarily to
$L^2(\mu)$ and sends $J_W f$ to $(Jf)v$, where
$v=\omega/\sqrt{\mathbb E_\mu(\omega^2\mid Y)}$.
Conditionally on $Y$, $\|v\|_2=1$ and
$\|v-1\|_2\le2\|\omega-1\|_2$ by the reverse triangle inequality
for the denominator. Thus $\|v-1\|_{L^2(\mu)}=o(1)$.
For fixed $j$, the preceding bounded-multiplier argument approximates
$J_0 f_j$ in $L^2(\mu)$ by uniformly bounded functions along every
converging subsequence. Since $\|(J-J_0)f_j\|_2=o(1)$, clipping the
$Y$-measurable $J f_j$ at a sufficiently large fixed level has arbitrarily
small $L^2$ cost along that subsequence. For its bounded part multiply the
bound by $\|v-1\|_2$. For its tail use
$\|v-1\|_{2\mid Y}\le2$. This proves $\|(v-1)J f_j\|_2=o(1)$.
Summing with the same thermal tail as in (6) and applying the unitary
map proves the assertion uniformly in $n$. In particular the comparison
can survive a change in both the dynamics and the observed vacuum law.
No such bound on the Wilson effective potential is established here.


## 5. Where the comparisons fail, and the next Wilson estimate

**PROVED (the weak four-dimensional compact Gaussian test).** In the
zero-monopole, zero-magnetic-flux compact Gaussian $U(1)$ law of rows
1618/1622 the spatial flux rotor has energy $|Q|^2/(2\beta n)$.
With the three half-turns imposed, $Q=\pm2e_1$ both survive. At fixed $q$,
their eigenvalue ratio at time $qn$ is $e^{-2q/\beta}\to1$.
This violates the upper bound $7/10$ in the consumer of (2) before invoking
band transport. With the *entire* continuous centre imposed in this Gaussian
model, only the nonzero-momentum photons remain. Their largest excited
ratio is $e^{-qn\omega_{\min}}\le e^{-c q}$, which violates the **lower**
bound $3/10$ for the large fixed $B$ used here. These tests compare excitation
weights. Merely counting surviving centre representations would give neither.

**PROVED conditional on the on-file periodic Villain input (rows 1565,
1571 A2–A3, 1573, 1579 item 9).** The literal half-turn test also excludes
(2) for weak interacting Wilson $U(1)$ at the cooling aspect in (3).
Here is the change of geometry needed in using those rows. Fix an integer
$\alpha=2jq\ge1$ before the fine cutoff. Use $w=\alpha n$ and take $n$ even.
In the current argument of row 1565 lines 153–205 the harmonic shift has
$\|h\|^2=w/n=\alpha$. For a support of size $s<n/8$, the coordinate
filling still lifts since the shortest period is $n$. This gives the same
phase-square bound $81s^3\|\rho\|^2/n^4$. There are at most $4V/s$
disjoint supports, $V=\alpha n^4$. For $s\ge n/8$ use the phase bound
$\pi^2$ and $V\le\alpha(8s)^4$. Thus in the displayed bound for
$M_\gamma$ of that row the first coefficient is multiplied by $\alpha$
and the factor $512^3$ in the second can be replaced by $\alpha$.
For fixed $\alpha$ the remaining two exponentially convergent series
tend to zero as the Villain stiffness $\gamma\to\infty$. All periods are even, as
required in the cited current expansion. The same offset-uniform bound
gives adjacent-coset geometric-mean factor
$d_{\gamma,\alpha}=\exp[-\alpha/(2\gamma)-M_{\gamma,\alpha}/2]\to1$.
Row 1573's step-two log second difference now gives
$Z_{\rm even}(w)\ge(1+2d_{\gamma,\alpha}^4)Z_{Q=0}(w)$.
The offset mixture in row 1565 (6) transfers this to Wilson cosine for
all sufficiently large bare $\beta$, with $\gamma$ fixed first. Since
$\lambda_0^w\le Z_{Q=0}(w)$, the result is $G(w)>1$ once
$2d_{\gamma,\alpha}^4>1$. This contradicts (3) at the chosen $\alpha$.
The estimate reads the thermal masses of the two translated cosets and
uses their **weak-law weights**. The periodic Villain current expansion
itself retains the source-check qualification of 1571. This extension
makes no claim for interacting $U(1)$ projected to all $Q=0$.

**ARGUED (weak five-dimensional $SU(2)$).** Adding a fourth spatial direction preserves
the commutator terms in the local model. Their presence alone cannot
settle this comparison. What would fail is the **upper** bound
$p_1\le7/10$ if a neutral slow holonomy survives on the hot box with
$n m_1^{(5)}\to0$, since then $p_1=e^{-qn m_1^{(5)}}\to1$ for every
fixed $q$. The prediction $n m_1^{(5)}=O((\beta n)^{-1/3})$ in check
1613 is **GUESSED** for the interacting law. Its scale comes from a
dimensionless inverse coupling growing like $\beta n$ in a weak
five-dimensional box. For comparison, the same Gaussian line calculation
in §4 with $d$ spatial directions has one-link prefactor $n^{-d}/(2\beta)$,
and expected squared ordered-line displacement at most $C_{d,\sigma}/(\beta n^{d-3})$. This follows by
the Fourier sum over $d$ momentum components with $d-1$ transverse polarizations.
A running coupling of the four-dimensional theory is essential to a
finite nonzero width in physical units as the bare $\beta_K$ increases.
I cannot prove the required law on the five-dimensional interacting
boxes, or assert that this is where that theory must fail instead of
VIR-down. An independent gapless neutral scalar with $n m_{\rm zero}\to0$
also violates the upper bound, even in a product retaining every $SU(2)$
commutator (the spectator test of row 1553).

**PROVED (an affordable first necessary estimate).** Fix $0<a_0<a_1$
so that the positive limiting quartic vacuum puts more than $31/32$ of
its mass in $a_0<|x_1|<a_1$. Such a pair exists by absolute continuity
and tightness. By (1) and the strong vacuum limit of row 1227, for all
sufficiently large fixed $B$ the corresponding annulus
$a_0B^{-1/3}<|\operatorname{Im}Y_1|<a_1B^{-1/3}$ has reference mass
greater than $15/16$. The two boundary spheres have zero mass.
Total variation is at most $\sqrt{1-A_n^2}$ by applying Cauchy–Schwarz
to $(\sqrt p-\sqrt r)(\sqrt p+\sqrt r)$ for the two densities $p,r$.
Hence (2) requires **at least $11/16$ of the fine vacuum** in that
annulus. The calculation (6) passes this test even with the line noise.
Zero flow fails it eventually for sufficiently large $B$ by row 1145.
An independent unobserved slow factor preserves that marginal while
changing the spectrum, so the test alone cannot give a thermal conclusion.

**ARGUED (next attack).** In a weak physical Wilson box, first bound the
probability of this annulus for **one flowed winding holonomy**. A bound
below $11/16$ on all late boxes rejects this particular choice of
reference and flow at the tested parameters. A passing bound measures a
necessary piece of the field law. To prove (2), the two costs in (4)
would still have to fit their *combined* budget $1/100$. After integrating
the nonconstant modes, the remaining costs include their conditional thermal
weight, their change of the compact transfer, and the distortion of the
compact variable by the nonlinear Wilson flow. Section 4 controls the full
photon trace and its ordered-line readout. Section 4.1 also permits a
nonseparable box-time potential of oscillation $o(B^{-1/3})$ in that
benchmark. For the Wilson law even the one-slice annulus bound is open.

**RESULT — (d), a comparison tool at the small-box end of T-down.**
ON FILE, rows 1227/1230 already prove the periodic one-site spectrum and heat trace. Section 4 uses their theorem.
PROVED by hand, if the flowed-holonomy comparison (2) holds on Wilson boxes it supplies HOT and requires a single-slice annulus probability of at least $11/16$.
PROVED, the comparison error tends uniformly to zero with all free transverse modes perturbing the ordered winding products. This persists under a bounded joint box-time potential of oscillation $o(B^{-1/3})$ (§§4–4.1).
PROVED given the cited periodic Villain input, weak compact Wilson $U(1)$ fails at each fixed cooling aspect $\alpha=2jq$ used here, on the late tail.
PROVED from row 1145, the unflowed Wilson readout fails. GUESSED for weak interacting 5D, the upper spectral bound fails if a neutral level has $nm_1\to0$.
GUESSED on actual 4D Wilson boxes, the positive-flow comparison remains open. VIR-down, PUR-io and the gap are open. No numerical proof step, Lean run or independent check of this row.
