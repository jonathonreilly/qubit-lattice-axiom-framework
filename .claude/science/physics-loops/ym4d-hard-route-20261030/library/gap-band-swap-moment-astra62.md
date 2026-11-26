# Repo search

Row 1581, research text at `3fec8ebe5`. I searched `origin/main` (`8b11ae2bb9`), `pr/10114` (`f76f6c649c`), `pr/10133` (`89faef229f`), `pr/10134` (`1e70c7211a`) and `pr/10141` (`c73ad7b177`) for replica swap, one-end moment, paired-link rotation/circle, dimer near swap, plaquette lower bounds, conditional velocity or variance, and plaquette Fisher information. The first-pass dimer hit on all five refs concerned equal binary odds in a Bloch model (`originals/7973`, winding-phase record note, lines 4 and 168). Searches for the Wilson moment and the square-contour variant returned no matching theorem. [Cycle-7973 readout](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/.claude/science/physics-loops/chirality-correction-20260909/originals/7973/docs/THE_CONTINUUM_RECORD_ALPHABET_KEEPS_THE_WINDING_PHASE_AS_RECORD_CONTENT_THE_ECHO_LAW_DOES_NOT_SUPPORT_IT_AS_A_FIELD_AND_THE_FIBRED_ODDS_REGISTER_ITS_SIGN_AS_A_FAIR_COIN_BOUNDED_THEOREM_NOTE_2026-09-04.md#L168)

- The RX8/RX9 follow-up found the identical `ym4d-proof/MANUSCRIPT_RG.md` on PRs 10114 and 10133, lines 3905–3936. Exchanging one raw link on two limiting flat orbits costs $2[1-\operatorname{Re}\operatorname{tr}(U'_eU_e^*)/2]$ at fixed depth. On main, `su2-gauge-aligned-response-20261108/parts/compact-forest-exchange.md`, (5)–(7), exchanges forest chords and expresses a covariance as half the expected product of reader differences times $\tanh(\Delta_R/2)$. Both concern endpoint exchanges. [RX8–RX9](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/f76f6c649cff7dffbab664d8976e680e8f287fe9/.claude/science/toe-ruleset-20261021/agents/ym4d-proof/MANUSCRIPT_RG.md#L3927) · [Forest exchange](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/8b11ae2bb95e641494fe75ed83d108ee712fa3a9/.claude/science/physics-loops/su2-gauge-aligned-response-20261108/parts/compact-forest-exchange.md#L123)
- In this lane, rows 1573/1574 and checks 1579/1580 give the circle and winding law. NOISE gives independent Haar relative links on forests and mean link speed $32/(15\pi)$. Check 1580, item 3b, leaves the volume order open and proves the fixed-box limit zero at $\beta\downarrow0$. [Lemma 1](gap-band-neutral-astra62.md) · [ROT, W and NOISE](gap-band-neutral-fable.md) · [Check 1580](gap-band-neutral-fable-check-astra62.md)
- Row 1155 (9) bounds the exponential moment of periodic plaquette deficits. Row 1373 gives $\mathbb E_+[\beta(1-w_p)]\le C$. The selective-fact check gives a positive volume-independent plaquette mean at fixed coupling by conditional variance. These supply the local Wilson inputs below. [Row 1155](gap-solve7-astra62.md) · [Row 1373](gap-seed3-astra62.md) · [Fixed-coupling estimate](gap-mech-selective-fact-fable-check-astra62.md)

The target-specific prior is absent. The November 8 digest treats thirteen other questions. The registry's TWO-PER and R12 concern transport between couplings. For the Sussman–Alpoge texts written with Claude and Codex (revision `31a47c543775`), the lane index points to the Wilson action at outline 238–261, the convolution and gauge-projected trace at 2195–2213 and 2313–2334, and gauge invariance at CA-I 559–584. The chunk, obligations and account-index searches found no swap-moment estimate. [Prior digest](prior/repo-search-2026-11-08.md) · [Registry](open-registry.md) · [Outline index](sa-index/README.md) · [Obligations](sa-index/obligations.md)

## Plan recorded at the start

1. Check what is already proved about the independently projected moment, the admissible circles, and the calibrated trajectory.
2. Test whether a local Wilson-field estimate can give a lower bound for the full moment. Check the order of quantifiers in the volume and weak-coupling limits.
3. Verify any bound against the neutral spectator and compact U(1) tests. Record its precise scope, or isolate the outstanding lemma and the distinct attempts made on it.

## The one-end moment of the paired-link circle

**Theorem (hand proof).** Fix the release witnesses $b,g_0$, a side $\ell\in1024\mathbb N$, $n=\ell b^K$ and $u=n/512=2v$. For the circle of rows 1573 and 1574, on the full gauge-invariant space and on the independently centre-projected replicas,
$$
               c\,\beta_K n^3\ \le\ \mathbb E j^2\ \le\ C\,\beta_K n^3
$$
for every sufficiently late $K$. Uniformly for $2\le\beta\le3$ the order is $n^3$. The argument below also gives a lower bound for other gauge-covariant circles acting separately on link dimers.

Use the symmetric magnetic sandwich of row 1573. Let $M=T^u$ or $P_0T^u$ on raw links with vertex gauge averaging, $B=M\otimes M$, and $F(X,Y)$ the real kernel of $B^{1/2}$. If $\Pi_j$ is the $j$th circle Fourier projection, the probability of winding $j$ is $\operatorname{Tr}(\Pi_j B)/\operatorname{Tr} B$. Write $X=(A,A')$, $D=\partial_s|_0$ for the circle acting on $X$, $G=-iD$, and $d\nu=F^2\,dX\,dY/\operatorname{Tr}B$. Check 1580 identifies $\mathbb E j^2=\|D_X F\|_2^2/\operatorname{Tr}B$. The $X$-marginal is the product of the two single-slice thermal laws, invariant under vertex gauges acting on either replica separately. For $w_p(A)=\tfrac12\operatorname{tr} A_{\partial p}$, its mean under $\nu$ is the spatial plaquette mean at period $u$ in the chosen projection. [Slice insertion, §1](gap-transfer.md)

Each dimer consists of two distinct links meeting at a vertex. Orient both into that vertex as in row 1573. Use ROT on each dimer at the common angle, allowing a fixed sense of rotation per dimer. Call a spatial plaquette *good* if no two of its boundary links form a dimer. This includes every plaquette for the straight dimers of both original rows. For a good plaquette, each boundary edge $e$ has a different partner extending to a vertex $v_e$ outside the plaquette. The four $v_e$ are distinct. Indeed no exterior vertex is a nearest neighbour of two different corners of an elementary square. At a single corner two different outward edges have different endpoints. The seed sides are large enough that these statements hold across the periodic boundary too.

**Lemma 1.** For every good plaquette, $\mathbb E_\nu D^2w_p=-2\,\mathbb E_\nu w_p$. Moreover the $D w_p$ for plaquettes with disjoint sets of corners and partner vertices are pairwise orthogonal in $L^2(\nu)$.

For one of the two oriented links of a dimer, set $a=A_e$, $b=A'_e$. The quaternion curve in Lemma 1 of row 1573 has the form
$$
 a(s)=\tfrac12(a+b)+\tfrac12(a-b)\cos s+\dot a(0)\sin s,
 \qquad \ddot a(0)=\tfrac12(b-a).
$$
Indeed $a(s)=m[\cos(\theta/2)-\sin(\theta/2)R_s h]$, with $h$ the fixed initial relative axis and the rotation normal perpendicular to $h$. Reversing the unit normal reverses the velocity by linearity. Quaternion inversion on the sphere is real-linear conjugation, so both derivative rules also apply in the orientation used by the plaquette word.

Average independent Haar gauge changes of the **second** replica at the four $v_e$, keeping the original pair of fields fixed while taking this average. These gauges fix all four plaquette links in each replica. For each $e$ the partner relative quaternion becomes Haar, since one of its end frames is now an independent Haar matrix. Its axis is uniform on $S^2$. The gauge at $v_e$ fixes the other three partners. Conditional on the plaquette links the oriented normal for $e$ therefore has mean zero, by uniform azimuth about its prescribed axis. The four velocities are conditionally independent under this auxiliary average. This calculation uses invariance of the measure to insert the gauges. It uses no decorrelation of Wilson fields.

In fact the finite-angle average can be evaluated. For each boundary link the auxiliary average replaces $a(s)$ by $\alpha a+(1-\alpha)b$ with $\alpha=(1+\cos s)/2$. The four auxiliary averages factor. Expand the trace of the product by real multilinearity, including quaternion conjugation for reversed links. In every term using a nonempty proper subset of second-replica edges, that subset of the four-cycle has a vertex of odd degree. A gauge sign $-1$ in the second replica there reverses the term. Thus only the all-first and all-second terms survive the full expectation. They have the same plaquette mean, giving
$$
 \mathbb E_\nu w_p\big(A(s)\big)=
 [\cos^8(s/2)+\sin^8(s/2)]\,\mathbb E_\nu w_p(A).
$$
At the quarter-turn the mean is one eighth of its starting value. At zero the second derivative is $-2\mathbb E_\nu w_p$. The bounded orbit derivatives justify differentiating under the integral. To see orthogonality, average the four gauges for $p$ with the data of the other plaquette and its partners fixed. They leave $D w_q$ unchanged and give zero for each summand of $D w_p$. This proves both assertions.

## From the local identity to the full moment

Write $a_p=\mathbb E_\nu w_p$, $b_p=\mathbb E_\nu(Dw_p)^2$. For a family $I$ of good plaquettes with disjoint corner and partner vertex sets, the **whole** thermal trace satisfies
$$
 \mathbb E j^2\ \ge\ \sum_{p\in I}\frac{a_p^2}{b_p},
 \qquad b_p\le \min\{16,32(1-a_p)\}.                         \tag{1}
$$
A zero denominator contributes zero and forces $a_p=0$.

Indeed $u=2v$ and $v\ge1$, so the kernel $F$ is a finite Wilson cylinder integral with smooth bounded pin derivatives. Each link has bounded orbit speed and acceleration on the invariant conull set. Differentiate the Haar-invariant integral of $(D w_p)(R_sX)F(R_sX,Y)^2$ at zero. Dominated convergence at fixed volume and Lemma 1 give
$$
 \frac1{\operatorname{Tr}B}\int (D w_p)F\,D_XF\,dX\,dY=a_p.
$$
The vectors $(D w_p)F/\sqrt{\operatorname{Tr} B}$ are orthogonal and have squared norms $b_p$. Bessel's inequality applied to $D_XF/\sqrt{\operatorname{Tr} B}$ proves the first bound by the winding identity of check 1580. For the second, the product $U=A_{\partial p}$ has speed at most four. On the unit quaternion sphere, the tangent gradient of $\operatorname{Re}U$ has squared norm $1-(\operatorname{Re}U)^2$. Thus $(D w_p)^2\le16(1-w_p^2)\le32(1-w_p)$ pointwise. No lower bound on a thermal vacuum weight enters (1).

There are $3n^3$ spatial plaquettes. Each of the $3n^3/2$ dimers spoils at most one of them, since two distinct incident lattice edges belong together to at most one elementary square. At least $3n^3/2$ plaquettes are good. The four corners and four partner vertices of any one of them lie within coordinate distance two of its base. Greedily select a good plaquette and discard the good plaquettes whose vertex sets intersect its own. Each choice costs at most $3\cdot9^3$ plaquettes, including itself, by counting possible bases and orientations. This gives
$$
                         |I|\ge\frac{n^3}{2\cdot9^3}.            \tag{2}
$$
The selection depends only on the matching. It works on the periodic grid and allows bent dimers as well as straight ones.

## Size of the plaquette mean in the two regimes

**At the calibrated roots.** Use the existing marked-plaquette bound. For one spatial plaquette $p$ on a rectangular periodic Wilson torus it gives $\mathbb E_{\rm per}(1-w_p)\le C_0/\beta$ for $\beta\ge1$ with $C_0\ge1$ independent of the periods, by Jensen applied to row 1155 (9). The rectangle version follows directly by taking a direction of $p$ as transfer time in the single-mark half tilt of row 1149 (16), with the rectangular trace argument of (23). Row 1373 already obtains this order in the neutral law. For a slice insertion $H=1-w_p\ge0$ one can also pass to that law directly. Since $0\le P_0T^u\le T^u$, sandwiching by $H^{1/2}$ bounds the inserted trace above by its periodic value. All eight twisted partition integrals are positive and the zero twist is the periodic one, so $Z_+(u)\ge Z^0(u)/8$. Thus, in both cases, $1-a_p\le C_*/\beta$ with $C_*=8 C_0>0$. [Rectangular tilt](gap-solve4-astra62.md) · [Half tilt (9)](gap-solve7-astra62.md) · [Projected estimate and its check](gap-seed3-check-opus.md)

For $\beta\ge2C_*$ every spatial plaquette has $a_p\ge1/2$. Equations (1) and (2) then give
$$
 \mathbb E j^2\ \ge\ \frac{\beta n^3}{256\,9^3 C_*}.             \tag{3}
$$
In particular (3) holds for **all sufficiently late $K$** with $n=\ell b^K$ and $u=n/512$ at any fixed release witnesses. Only $\beta_K\to\infty$ is used here. This applies the local estimate at the release coupling itself. [Calibration, BND-2](sa-ym4-lean-trajectory-check-astra62.md)

**On the band $2\le\beta\le3$.** The fixed-coupling plaquette-mean proof on file applies also after the temporal twist average, uniformly on this compact interval. For a fixed spatial orientation $ij$, give just this orientation coupling $t$ and write $H_{ij}=\sum_{p\parallel ij} w_p$ on the whole spacetime torus of $V=n^3u$ sites. Use Boltzmann factors with log $tH_{ij}$ plus the other oriented terms, dropping field-independent constants. Twist signs can be placed wholly on temporal plaquettes. Conditional on each twist, at $t=0$ a change of sign on all $j$-links with one fixed $i$ coordinate preserves the remaining action and reverses a prescribed $ij$ plaquette. Thus $\mathbb E_0 H_{ij}=0$ for the untwisted law and for the mixture. At $0\le t\le\beta$ its derivative is $\operatorname{Var}_t H_{ij}$.

Select the $j$-links based at sites with all four coordinates even. There are $V/16$, and no plaquette contains two. Given the twist and all other links they are independent. Each contributes to $H_{ij}$ a function of its one Haar variable $q$ from its two $ij$ staples. When the six other links of those plaquettes are within chord distance $1/24$ of the identity, that function is within $1/4$ uniformly of $2\operatorname{Re}q$, whose Haar variance is one. Its centred Haar $L^2$ norm is then at least $3/4$. Every single-link conditional density is at least $d=e^{-36}$ relative to Haar, since at most six action terms of magnitude at most three meet a link. This holds for every twist and throughout the interpolation. If $h>0$ is the Haar mass of the indicated ball, repeated conditioning gives the six-link event probability at least $(dh)^6$. On the event the conditional variance contributed by the selected link is at least $9d/16$, by minimizing the squared deviation over constants. The conditional-variance sum gives $\operatorname{Var}_t H_{ij}/V\ge (9d/256)(dh)^6$.

Spatial translations preserve each spatial plaquette expectation of a given orientation, and cyclicity gives the same expectation at each time. In the twist representation moving a spatial cut by one site is a vertex gauge on the slice, and moving its time seam across a slice applies a flat centre flip there. Both preserve its contractible plaquettes. Consequently $a_p=\mathbb E_\beta H_{ij}/V\ge a_*=(18d/256)(dh)^6>0$ throughout the band, in either projection. With the $16$ bound in (1), this proves
$$
                    \mathbb E j^2\ge\frac{a_*^2}{32\,9^3}n^3.    \tag{4}
$$
This constant is uniform in the temporal twist average. [Orientation derivative and positive-variance argument](gap-mech-selective-fact-fable-check-astra62.md)

## A matching upper bound

For ROT at its specified angular speed,
$$
                  \mathbb E j^2\le 1944\,\beta n^3.                \tag{5}
$$
The estimate uses a second cancellation under vertex gauges. Let $D_r$ move dimer $r$ only and $L_r=D_r\log F$. The function $F$ is strictly positive at finite volume. For dimers $r,s$ with disjoint vertex sets, $\mathbb E_\nu L_r L_s=0$. To verify this, expand $L_r$ over its two links and two replicas. In the summand differentiating $A_e$, average a gauge change of $A'$ at the exterior endpoint of the mate of $e$. It leaves $F$, its differential in $A_e$, and $L_s$ unchanged. For the last assertion, the gauge change commutes with the entire motion of $s$, which reads only its own two links. As in Lemma 1 the velocity of $A_e$ in the remaining summand averages to zero. For the terms differentiating $A'_e$, average a first-replica gauge at the same vertex. This proves orthogonality even though each logarithmic pin derivative can depend on the entire cylinder.

For a unit imaginary quaternion $t$ let $\partial_t$ translate a single link of one replica at $X$ by $\exp(st)$. In the pinned Wilson integral for $F$, four spatial plaquettes at half weight and one temporal plaquette at full weight see that link. This count also holds for $v=u/2=1$. Each normalized trace satisfies $\partial_t^2 w=-w$ because the link occurs only once. The second derivative of the log of the positive integral is the conditional mean of the second derivative of its exponent plus the variance of the first derivative. Include the twist label in the conditional law for the projected kernel. It follows that $\partial_t^2\log F\ge-3\beta$. Haar integration by parts gives
$$
 2\mathbb E_\nu(\partial_t\log F)^2=-\mathbb E_\nu\partial_t^2\log F
 \le3\beta,\qquad
 \mathbb E_\nu |\nabla_e\log F|^2\le9\beta/2.
$$
The gradient concerns one specified replica. This is the cylinder version of the existing Wilson one-link Fisher estimate and marginal score identity. [One-link identity and Proposition LIFT](gap-short-step-variance-fable.md) · [Row 1373, single-link Fisher bound](gap-seed3-astra62.md)

Each of the four velocities in $L_r$ has norm at most one. Cauchy–Schwarz gives $\mathbb E L_r^2\le 4\cdot4\cdot9\beta/2=72\beta$. At most eighteen dimers including $r$ can meet its three vertices, since at most six dimers use any vertex. In $\mathbb E(\sum_rL_r)^2$ use orthogonality for the disjoint dimers and $2|xy|\le x^2+y^2$ for those that meet. Equation (5) follows from $18\cdot72\beta\cdot(3n^3/2)$. Thus the order is $\Theta(\beta_K n^3)$ on the calibrated trajectory and $\Theta(n^3)$ uniformly throughout $[2,3]$. All constants in these two comparisons are independent of the matching, the side and the even time period.

## Vacuum and frame choices

Let $\Omega$ be the normalized positive vacuum on the finite spatial torus and $\Omega_2=\Omega\otimes\Omega$. Its smoothness follows by applying the smooth one-step kernel to its eigenvalue equation. The top eigenvalue is simple. Gauge and centre transformations preserve positivity and commute with $T$, so they fix $\Omega$. At fixed $n,\beta$, the normalized even powers of $T$ converge in trace norm to the vacuum projector, also after centre projection. This follows by summing the eigenvalue ratios, dominated by their summable squares. Hence the bounded plaquette means in the vacuum inherit the estimates leading to (3) and (4) by sending the *time period* to infinity first. Apply Lemma 1 and (1) directly with wavefunction $\Omega_2(X)$ and probability $|\Omega_2|^2\,dX$. This gives the same lower bounds on $\|G\Omega_2\|^2$. For the upper bound, the thermal moment contains $\|G\Omega_2\|^2$ with weight $(\lambda_0^u/\operatorname{Tr}M)^2$, which tends to one at that fixed $n,\beta$. Equation (5) is uniform in $u$. The entire vacuum second moment is carried by even harmonics, since the half-turn gives $\Omega_2\circ R_\pi=\Omega_2$. [Finite-volume vacuum, §4](gap-transfer.md) · [Vacuum contribution, item 3b](gap-band-neutral-fable-check-astra62.md)

The proofs allow any fixed matching of incident links, either orientation of the elementary rotation, and fixed orthonormal changes of the axis coordinates in which the two relative axes are compared. For the latter, rotate the coordinates into the chosen frames and pull the result back on each link. A Haar partner axis is still uniform. The velocity remains centred under the exterior gauge, the acceleration is still $(b-a)/2$, and the speed bound is unchanged.

The independent relative frame of row 1573 preserves even the **exact distribution** of $j$. For fixed $h$ let $U_h$ implement $(A,A')\mapsto(A,hA')$ on raw $L^2$. The new action is a unitary conjugate of the old one and $U_h$ commutes with $B$ for both choices of $M$. Cyclicity gives the original Fourier weight at every $j$. This holds fibre by fibre before taking the independent Haar average over $h$. Averaging the velocities before squaring would compute a different quantity. These conclusions concern the raw Haar circle. The physical-orbit chart and the clock preserving the thermal marginal in row 1573 change the action or its reference measure and require their own generator estimates. [Relative frame and thermal clock](gap-band-neutral-astra62.md)

## Changing the motion within a dimer

There is a lower bound even if the circle takes a different path between its endpoints. Assume each dimer acts only on its own four raw links, preserves their product Haar measure, commutes with simultaneous vertex gauges, and swaps its replicas at $\pi$. Allow a different such circle on each dimer. The regularity needed below is that the four quaternion coordinates for each link belong to the $L^2$ generator domain of its strongly continuous Koopman action. Bounded differentiable orbit speeds as in ROT suffice. No uniform energy or speed bound across sizes is needed for the lower estimate.

Write $a,b$ for the two replicas of one oriented edge $e$ and $c,d$ for its mate. Under four independent Haar links let $v_e=Da$ and $s_e=\mathbb E_{\rm Haar}|v_e|^2$. Then $s_e\ge1/2$. Indeed $a\circ R_\pi=b$ and $\|b-a\|_2^2=2$. In the circle Fourier decomposition the squared half-turn difference is four times the odd weight of this quaternion-valued function, which is at most $4\|Da\|_2^2$.

**The mean velocity at given $a,b$ vanishes.** Integrate out $c,d$ under Haar. Simultaneous changes of the two frames at the ends of $e$ act by arbitrary common left and right multiplication on $a,b$. They preserve the Haar integral in the mate. Hence the mean tangent velocity at $a$ must be $f(x)(b-xa)$, $x=a\cdot b$. To see this, put $a=1$ and conjugate about the imaginary axis of $b$. Only the tangent along that axis is fixed, and conjugating to any other axis gives the same coefficient. For the $L^2$ version, replace a representative $V(z)$ of the conditional vector, $z=(a,b)$, by $\int k^{-1}V(kz)\,dk$ over the compact endpoint frame group. Fubini gives the same vector almost everywhere and change of variables gives equivariance on each orbit where this integral exists. The circle commutes with its half-turn, so the conditional mean at $b$ is $f(x)(a-xb)$. For every smooth $H$ on $[-1,1]$, invariance of the four-link Haar law makes the derivative of $\mathbb E H(a(s)\cdot b(s))$ zero. Thus
$$
            \mathbb E[2(1-x^2)f(x)H'(x)]=0 .
$$
Since $H'$ can be any polynomial, the finite signed measure in this identity is zero. The exceptional $x=\pm1$ have zero Haar mass. This proves the assertion.

For a good plaquette set $s_p=\sum_{e\in\partial p}s_e\ge2$. Its mean curvature under this motion is $-s_p a_p$. Expand the plaquette word using the four differences $a_e(s)-a_e$. In a term containing just one difference apply independent first- and second-replica gauges at the outside vertex of its mate and a second-replica gauge at the nonshared end of $e$. These integrations give independent Haar $b,c,d$ and leave the first plaquette fixed. By the same endpoint covariance the mean of $a(s)$ at fixed $a$ is $r_e(s)a$. Taking its scalar product with $a$ gives
$$
 r_e(s)=1-\tfrac12\mathbb E_{\rm Haar}|a(s)-a|^2
       =1-\tfrac12 s^2 s_e+o(s^2).
$$
Terms with two differences divided by $s^2$ converge in $L^1$ to the two-velocity terms. Both replicas' gauges at the separate outside vertices average each velocity to zero at fixed boundary links. Terms with three or four differences are $o(s^2)$ in $L^1$ because two divided differences have an $L^1$-convergent product and each extra difference is bounded and tends to zero in probability. All estimates pass to the finite-box bounded density $F^2/\operatorname{Tr}B$. Real-linearity of inversion handles reversed links. This proves $\mathbb E_\nu w_p(R_sX)=a_p-s^2s_p a_p/2+o(s^2)$, where $w_p$ reads the first replica.

Smooth functions of these finitely many compact link coordinates, including $w_p,F,F^2$, are in the generator domain. The smooth chain rule applies because the squared coordinate divided differences are uniformly integrable and the bounded change of the gradient along each increment tends to zero in probability. The test $\int w_p(R_sX)F^2$ can therefore be differentiated twice by taking one derivative on $w_p$ and transferring the other to $F^2$ by Haar invariance. This gives $\int (Dw_p)F\,DF/\operatorname{Tr}B=s_pa_p/2$. Disjoint plaquette tests are orthogonal by the preceding conditional-velocity identity. The same three vertex integrations used for the one-difference term give $\mathbb E_\nu[|v_e|^2\mid (A_f)_{f\in\partial p}]=s_e$, since the averaged scalar is independent of $a$. The quaternion tangent bound now gives $\mathbb E(Dw_p)^2\le4s_p\mathbb E(1-w_p^2)$. Bessel's inequality yields
$$
           \mathbb E j^2\ \ge\ \sum_{p\in I}
             \frac{s_p a_p^2}{16\,\mathbb E(1-w_p^2)}.          \tag{6}
$$
This recovers both (3) and (4) for every circle in the stated class. If all link speeds are bounded by $L$, the proof of (5) uses the conditional-velocity identity after averaging both replicas at the outside vertex of the mate and gives $1944L^2\beta n^3$. A volume-independent moment at release therefore requires leaving this class. The independent-frame lift, which is unitarily equivalent to the original raw circle, also obeys (3).

## Purity and the comparison models

**A Wilson separation at matching parameters.** For any fixed $\beta>0$, the proof of (4) uses $d=e^{-12\beta}$ and integrates over an interval of length $\beta$. It gives $a_p\ge (9\beta d/256)(dh)^6>0$. In particular, fix $0<\beta<2/9$ and take $u=n/512$. The projected two-end estimate (4)–(5) of row 1573 gives $-\log P\to0$ as $n\to\infty$, since a polynomial in $n$ multiplies a decaying geometric tail with ratio $9\beta/2<1$. On these very same Wilson boxes (1) gives $\mathbb E j^2\to\infty$. At fixed size, sending $\beta\downarrow0$ instead gives the zero limit of check 1580. This separates the one-end demand from a passing purity on actual Wilson data. The fixed positive coupling in this example is a comparison, outside the calibrated trajectory. [Pinned comparison](gap-band-neutral-astra62.md) · [Check 1580, tests (g3) and 3b](gap-band-neutral-fable-check-astra62.md)

**Neutral spectator.** Take $T_W\otimes T_m$ with the three centre flips acting trivially on the entire spectator. The full replica swap reads $P_W P_m$. For a product of circle motions on the two factors, the generators add. The Wilson winding has mean zero by Haar integration of $D(F_W^2)$, so the product second moment is the sum of the two second moments whenever both are finite. The Wilson lower bound persists. Moving the Wilson coordinates alone would give the wrong endpoint for this test. For the independent real scalar in row 1573, one nonzero momentum oscillator gives $\limsup P_WP_m\le\tanh(\pi/512)<457/625$. The large raw moment is consistent with this failing purity and with the passing strong-coupling example above. [Corrected spectator test](gap-mech-direction4-check-astra62.md) · [Scalar comparison](gap-band-neutral-astra62.md)

**Weak four-dimensional compact U(1).** The square-contour dimer circle in row 1574 has the same volume obstruction at each fixed positive Wilson coupling, including weak coupling. For relative angles $(\phi,\psi)$ on the two links, the first link's angular velocity in one replica is, up to a fixed sign, $(2/\pi)\psi\,\mathbf 1_{|\psi|>|\phi|}$. Averaging the partner angle gives zero at fixed $\phi$. Under independent uniform $\phi,\psi$ its mean square is one, as in check 1580. At fixed first link $a$, Haar averaging the other three links gives $\mathbb E a(s)=r_e(s)a$ with $r_e(s)$ real. Indeed the angle change of $a$ is $-(\phi(s)-\phi)/2$, and reversing both relative angles reverses this change because antipodal reflection commutes with square arclength translation. These are precisely the zero-mean velocity and scalar one-link average used in (6). The divided-difference proof applies across the corners, since link speeds are bounded and derivatives exist Haar almost everywhere. On the unit circle the same gradient bound is $|\nabla\operatorname{Re} U|^2=1-(\operatorname{Re} U)^2$. Thus (6) holds with $s_p=4$. The fixed-$\beta$ orientation argument applies with $\operatorname{Var}_{\rm Haar}(2\cos\phi)=2$ and gives $\mathbb E j^2\ge c(\beta)n^3$ also in the three-half-turn projected law. This tests the local moment directly.

For an arbitrary full-swap interpolation the endpoint gives a separate test. In this U(1) projection charges $\pm2e_1$ survive. Using the periodic coset and positive Wilson-mixture inputs of row 1565, row 1573 obtains $P_{\rm even}<1/2$ at all sufficiently weak coupling at this aspect. Hence every such winding law has $\mathbb E j^2\ge(1-P_{\rm even})/2>1/4$. Projection onto exactly zero integer flux changes this comparison. [Square velocities and projection check](gap-band-neutral-fable-check-astra62.md) · [Even-charge comparison](gap-band-neutral-astra62.md) · [Check 1579, item 9](gap-band-neutral-astra62-check-opus.md)

**Five-dimensional SU(2).** The two-replica gauge average still works. A spatial slice now has $6n^4$ plaquettes and $2n^4$ dimers, so at least $4n^4$ plaquettes are good. The disjoint selection has bounded degree in four spatial dimensions. The fixed-coupling orientation-variance proof uses eight incident plaquettes per link and selects a fraction $1/32$ of the links of the prescribed orientation on the even spacetime grid. It gives the analogous $c(\beta)n^4$ obstruction. The one-end cost therefore provides no phase or dimension discrimination for a positive mass-gap argument.

By the exact winding law, $1-P=2\Pr(j\text{ odd})\le2\mathbb E j^2$. The proposed $42/625$ is sufficient, and even $84/625$ would suffice for $P\ge457/625$. Both bounds fail eventually for these circles on the calibrated roots. Odd weight remains undetermined at the calibrated roots. Two-end estimates still address that question. The new estimates are hand proofs awaiting independent review. They use no numerical or Lean computation. [Seed consumer, §3.1](gap-k2-tool-design-fable.md)

RESULT — The raw paired-link swap moment is $\Theta(\beta_K n^3)$ at every sufficiently late calibrated cutoff and $\Theta(n^3)$ uniformly on $[2,3]$, with or without independent centre projection. Every local gauge-covariant dimer circle covered by (6) has at least this lower order. The small-moment route fails. (PUR-io) and the mass gap remain open.
