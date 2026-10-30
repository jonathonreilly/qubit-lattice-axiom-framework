# Independent check of the determinant colour and scalar reduction

Source: [DETERMINANT_SIGN_ASTRA.md](../DETERMINANT_SIGN_ASTRA.md), all 610 lines at
`cc799d903f8ad51d6cdcd9b0328d40ea2b0a3047`, SHA256
`138610a5a7d6e63d2a2d7ce3616964b9b909acf8295df65777b3eb4a40c55d36`.
The source is the supplied four-dimensional, source-zero SU(N) Wilson step,
with odd L>=3, N>=2, and fixed kappa>0 before the volume and momentum limits.

Requested checker: OpenAI/Codex `gpt-6-astra`, `max`; actual backend identity is
not independently attested by the available tools. This is a separate restricted
context, with no authorship or prior checker verdict input; no cross-family
independence is claimed. The required c93-exported preflight returned `go`.
The unavailable ulimit memory cap was disclosed; reads remained bounded.

Methodology was read from immutable `c93fcb388b60ad7974433b2aa1cb1d366aec52ff`.
Installed skill entries were read separately. The author's earlier methodology
pin remains its historical pin. No Git mutation, target edit, audit, subworker,
scientific numerical calculation or symbolic coefficient run occurred.

[Source-only findings](../checks/gate_determinant_colour_cc799d903f_source_findings.json)
and the [exact read manifest](../checks/gate_determinant_colour_cc799d903f_source_read_manifest.json)
were frozen before opening either author packet. Necessary supplier coverage is
explicitly bounded there: complete BD; BM 26–610; FK 1–175; IC 1–314 and 586–731.
Source prose necessarily exposed status words and review-link names; linked
reviews, root fronts and GOAL narratives were not read. No label supplied a premise.

## Mathematical reconstruction

1. **The constrained saddle is preserved (90–148).** Write X_r=Log T_r and
   mu=avg X_r,1. Direct expansion gives
   `[log det W_pol]_3=(1/6)avg tr((X_r,1-mu)^3)`; degrees one and two vanish.
   Thus its real determinant phase is O(fields^3), not an assumed zero for SU(N).
   Multiplication by exp[-(log det W_pol)I/N] restores determinant one.
   Its value loss is tr(S)[1-cos(theta/N)]=O(fields^6). Sandwiching the actual
   SU maximum between this admissible value and the U maximum proves equality
   through degree five. Analyticity on the real Lie-coordinate slice gives the
   holomorphic Taylor identity by polarization. DS6 therefore has every needed
   degree-four vertex with the displayed exp(A)exp(x) and reversed inverse order.
   For SU(2), real means have quaternion form and positive determinant near I,
   providing an independent stronger control: the polar factor is already SU(2).

2. **Every colour is counted (150–255).** Completeness in the real HS basis gives
   sum T_a X T_a=-(tr X)I+X/N. With sum h_i=0 and sum h_i^2=N, the neutral
   contraction is (N-1)W0 and the ordered roots contribute
   N^2(W10+W01)-N W0. Cubic traces reduce to commutators, giving no neutral
   exchange and sum_(i!=j)(h_i-h_j)^2=2N^2. The bilinear dual F_ji produces
   one trace per ordered root, with no additional factor two.
   A root word visits only i,j, which proves the scalar/2x2 interpolation even
   though its auxiliary H_10 is not a physical traceless SU(2) background.
   Complexification uses the bilinear trace; no conjugated complex field is inserted.

3. **The measured coefficient is the literal one (54–83, 244–306).** At the full
   tree critical point, the exponential differential E satisfies
   K_coord=E^T K_intr E and det E=product j_N. Hence the coordinate Haar term
   cancels exactly once. The normalizer contributes (N^2-1)a_L.
   The mixed z_+z_- trace-log coefficient is half the seagull minus exchange;
   z_+z_-=epsilon^2/4 and BM26's second derivative give the factor 1/24 in DS15.
   The Cartan critical logarithm is odd, so no second critical variation is lost.
   For N=2,3 the formula gives 4C-B and 9C-B; solving these two equations
   reproduces DS16 and transports the actual supplier readers and Ward identity.

4. **The affine scalar calculation agrees with that projection (282–350).**
   From the paired words, R=avg cos(Fs) and c=avg cos(Fs)l give the scalar
   kernel Hessian kappa c^*c/R. Expanding this expression gives DS19, including
   both Q^*T and T^*Q, while the Wilson Hessian contributes
   -D_mu nu^*D_mu nu/(2L^4). There is no scalar linear-F vertex.
   The amplitude -log R/2 supplies a_L after the curvature normalization.
   The twelve-plane average gives w=sum_(eta!=rho)y_eta^2/(6L^2), hence exactly
   DS21, including its indefinite -kappa Re int tr(QG U^*) term.
   For the summable Hessian kernel H(r), the Ward identity rewrites the affine
   density as -F^2 sum r_nu^2 H_mu mu(r)/4=F^2 beta_mu nu/2.
   This justifies finite jets after the volume limit, without an affine torus field.

5. **The potentially dangerous cross term is bounded, not assigned a sign
   (356–456).** The contour-minus-reference boundary is the stripwise translated
   axial ribbon. It has at most L sum_(eta!=rho)|y_eta|<=3Lh plaquettes, including
   their owners and orientations. Therefore U=RD, tr(RR^*)<=4r_L^2 and
   DGD^*<=I imply tr(UGU^*)<=4r_L^2.
   Completing the full root square gives det K=(kappa/L^3)det S and
   QGQ^*=P/kappa+Q_T S^-1 Q_T^*. Because Ug=0, QGU^*=Q_T S^-1 U_H^*.
   Cauchy–Schwarz then yields kappa|x|<=2r_L sqrt(kappa y), with 0<=y<=3.
   The root determinant factor survives. At q=0 there are four harmonics;
   their finite-volume contribution vanishes only after fixing positive kappa
   and taking the normalized volume limit. No prime or mode deletion is used.

6. **Constants and limit check (458–544).** The identity tr(GA)=m0-kappa tr(QGQ^*)
   gives B=-g_L-d_L y-kappa x, where g_L=(3L^2+1)/(16L^2)>0 and
   d_L=(L^4-L^2-4)/(48L^4)>0. Completing the square gives DS30 and
   kappa_star=g_L d_L/(2r_L^2), with B<=-g_L/2 on 0<kappa<=kappa_star.
   At L=3 these are exactly 119/31104 and -7/72.
   Tree fixing has operator norm at most C_T=2L^2(4L-3); its projection removes
   only the gradient already accounted for in the full Schur identity.
   The transverse alias bound gives A_H>=4|q|^2/(pi^2 L^2 C_T^2).
   The normalized enclosing four-ball integral of |q|^-2 is 1/4, proving
   y<=kappa M_L and |B+g_L|<=(d_L M_L+2r_L sqrt(M_L))kappa.
   The frozen findings' integrability wording scopes this check to dimension four;
   it is not a claim that |q|^-2 fails to be integrable in every other dimension.
   No monotonicity in kappa or estimate of charged momentum derivatives follows.

## Primary sources and author-packet check

The bounded passages in [Adams–Lee](https://arxiv.org/pdf/0709.0781v3) impose
specific scaling, denominator and infrared hypotheses. [Hasenfratz–Niedermayer](https://arxiv.org/pdf/hep-lat/9706002v1)
distinguish the finite-kappa marginal operator from the fixed-point action.
[Carena et al.](https://arxiv.org/pdf/2208.10417v1) display the scalar seagull and
non-Abelian gauge/ghost terms in different conventions. These comparisons are
supported within the recorded read coverage; none supplies this coefficient.
Bałaban and Dimock receive architectural credit through the local suppliers;
this review claims no new complete read of their original literature.

After the source freeze, both author JSON packets were read. All their displayed
source hashes, line counts, PROCESS_LIGHT identity and receipt-to-manifest hash
match the immutable objects at cc799d903f. Their result summaries agree with the
checks above. Historical authorship, retained reads, tool execution and absence
of earlier numerics remain author statements; matching bytes do not certify them.
No author verdict was adopted and no frozen finding was rewritten.

## Scoped review assessment

**LAND for the stated bounded mathematical source.** No material source defect
was established. This is source-scoped review advice, not review-loop landing
PASS, integration authorization, an audit verdict or a retained-status change.
The independent audit/pipeline and whole dependency-chain certification were not
run. The prescribed explicit-path vocabulary check is recorded in the receipt.

## Research-gate assessment

**advance**, confined to the coefficient/sign interface offered here.
Correctness: DS5–DS36 hold for the supplied model, conventions and limit order.
Strict progress: the N-dependent colour problem and scalar subtraction subproblem
are resolved; all N now share one charged m0-matrix calculation and a bounded
scalar function. This is new algebra and a signed estimate beyond BD29.
For a fixed N, the residual inequality C_L<B_L/N^2 remains exactly equivalent to
b_N<0; renaming that inequality is not additional sign progress.
The exact consumer input is
`b_N=N^2 C_L-B_L`, DS11–DS15's finite vertices, DS21's scalar integral and DS31/34's
bounds. In particular b_N/N^2-b_M/M^2=B_L(1/M^2-1/N^2)<0 for N>M>=2 on DS31.
A proved b_M<=0 there would imply b_N<0 for every larger N, but no base sign is
supplied. Inherited-class closure, repeated running, non-freeness, continuum
existence and a positive physical continuum mass gap remain open.
