# Common source offset within the original processor windows

Status: new conditional author derivation requiring a distinct check. This establishes an ordered full-fiber loaded-inverse criterion and an actual installed-seed concentration bound. It keeps the original physical processor windows and background Green function unchanged. A concrete nonempty offset interval illustrates these two interfaces only; no complete-output, packet, temporal or storage performance is asserted.

## 1. Domain and exact installation

Retain the calibrated .0027<j<.003, unchanged source-free background and exact three-site geometry of the checked attachment. Impose

    0<lambda<=1e-8, 0<g<=1e-6, 0<h<=4e-6,
    d=2j sin h, d/g<=1/2,
    0<=epsilon<=1/200, |Delta|<d,
    a1²=(lambda²/3)(1+e1), a2²=(8lambda²/3)(1+e2),
    kappa²=3jlambda(1+e3), |e_i|<=epsilon,
    |r_i|<=epsilon lambda.

All amplitudes are positive real with the fixed negative exchange signs; all source detunings Delta+r_i multiply the FULL internal identity. The three source diagonals are 2j+Delta+r_i, while the port and background remain unchanged. Use the same six positive blocks as the perturbed attachment, replacing its d_i by Delta+r_i:

    j(n2+np)-kappa X_2p,
    a2(n1+n2-X_12), a1(n0+n1-X_01),
    (j+Delta+r2-a2)n2,
    (2j+Delta+r1-a1-a2)n1,
    (2j+Delta+r0-a1)n0.

Here |Delta|<d<2.4e-8, lambda<=1e-8 and j>.0027 leave these occupations positive and kappa<j. For example a2<1.64e-8, |r_i|<=5e-11, and kappa²/j²<3(1.005)1e-8/.0027<1.12e-5. Thus positivity holds on the full qubit space. Compression off all three source heads leaves exactly jnp. No vacuum scalar is added. Shared B occurs once, with B iota=iota K, and c_att is unchanged. A source-only common potential is not a global identity shift.

The two physical windows remain

    I_e=c_att+2j+e+[-d,d], e=1,3; I=I_1 union I_3.

On either window define D=(E-c_att-2j)I-B. Its selected eigenvalue is delta in [-d,d], and all complementary eigenvalues x satisfy |x|>.185. The physical background, on each record/parity sector and each lip, retains the FULL eight-dimensional estimate

    ||G(E)-m_j(D)||<=a0+b0|delta|,
    a0=8e-18, b0=46000/.0053+290/g.                    (1)

Only the emitter-free argument of the wide endpoint source is used. Its later one-site emitter constraints and density estimates are not imported. In particular the kappa here can exceed that source's one-site-emitter kappa cap; equation (1) is a property of the unchanged unloaded background, independent of the newly attached source couplings.

## 2. Shifted source factors, unshifted physical load

Set Y=D-Delta I, A_i=Y-r_i I, P_r=A0 A1-a1² I. The reference and actual ordered denominators are

    Qref=P_r[A2-kappa² m_j(D)]-a2² A0,
    Q=P_r[A2-kappa² G]-a2² A0.                         (2)

The load is m_j(D), NOT m_j(Y). At selected energy put y=delta-Delta, R=sqrt(y²+lambda²), and define

    B_eps=20epsilon+16epsilon²+4epsilon³,
    beta=3(lambda+|Delta|)/j,
    m=1-beta-B_eps,
    A_eps=(1+epsilon)²+(1+epsilon)/3.

Our domain is contained in the checked scalar common-mode domain lambda/j<=1/32, |Delta|/j<=1/4. In fact beta<3(1e-8+2.4e-8)/.0027<.000038, so m>.89956 throughout the present domain. The checked scalar bound, applied to the actual physical load m_j(Delta+y), gives

    |qref(delta)|>=m R³,
    |P_r(delta)|<=A_eps R²,
    |P_r/qref|(delta)<=A_eps/(m R).                    (3)

The latter uses |y-r_i|<=(1+epsilon)R. It is a selected reference estimate, not yet an actual matrix statement.

For a complementary D-eigenvalue x, put z=x-Delta. Since |x|>.185 and |Delta|<2.4e-8,

    |z|>.184999976>.1849, tau=lambda/|z|<6e-8.

Here the physical Weyl root is real on either exterior component and |m_j(x)|<=1/j, irrespective of the shift in the source polynomial. The same reverse-triangle calculation gives

    |qref(x)|/|z|³ >=
       [(1-epsilon tau)²-(1+epsilon)tau²/3]
       [1-(3+4epsilon)tau]
       -(8/3)(1+epsilon)tau²(1+epsilon tau) > .99.

Also |P_r(x)|<1.000001|z|². Hence on the entire complementary input space C,

    ||Qref^-1 C||<1/(.99*.1849³)<170,
    ||Qref^-1 P_r C||<1.000001/(.99*.1849)<6.           (4)

Both energy signs are covered without any oddness assumption. The physical closed root is evaluated at x, not z. These bounds include wrong-window prepared columns and all other closed internal directions.

## 3. Full-fiber ordered inverse, including arbitrary source forcing

Let A=A2-kappa²G. The source Schur matrix is

    S=[[A0,a1 I,0],[a1 I,A1,a2 I],[0,a2 I,A]].

For arbitrary full-fiber forcing (f0,f1,f2), not only the prepared seed, define

    F=a1a2 f0-a2 A0 f1+P_r f2,
    psi2=Q^-1 F,
    psi1=(f2-A psi2)/a2,
    psi0=[f1-A1 f2/a2+(A1 A/a2-a2 I)psi2]/a1.          (5)

Direct substitution into the three rows gives exactly (f0,f1,f2). In the first row, the coefficient of psi2 is Q/(a1a2). This verifies the order: G is never commuted through A0 or A1. Positive a1,a2 and invertible Q also imply trivial homogeneous kernel by the same elimination, so (5) is a full inverse of S. No inverse of a possibly resonant A_i is used. Formula (5) is not a claim of a uniform small norm for all source recovery rows.

The exact factorization is

    Q=Qref(I-Kload),
    Kload=kappa² Qref^-1 P_r [G-m_j(D)],
    Q^-1=(I-Kload)^-1 Qref^-1.                         (6)

Only Qref and P_r commute, since both are reference functions of D. Combining (1),(3),(4) proves the energy-resolved bound

    ||Kload|| <= theta(delta)
       =kappa²(a0+b0|delta|)[A_eps/(m R)+6].            (7)

The elementary inequality |delta|<=|Delta|+|y| gives the explicit sufficient uniform margin

    Theta_Delta=kappa²{
       (A_eps/m)[(a0+b0|Delta|)/lambda+b0]
                                      +6(a0+b0d)}<1.  (8)

Thus, with c=(1-Theta_Delta)m,

    ||Q^-1|| <= 1/(c R³),
    ||Q^-1 P|| <= 1/(c R³),
    ||Q^-1 C|| <170/(1-Theta_Delta).                   (9)

The selected envelope dominates 170 everywhere here: R<=sqrt((2d)²+lambda²)<5e-8 and m<=1. In the complementary estimate in (9), Qref^-1 acts on C FIRST; subsequent Neumann inversion may mix its full output into the selected row. No diagonality of the actual inverse is assumed.

Each physical lip is handled separately in the order (6). The lower-lip ordered Q need not equal the adjoint of the upper-lip Q; neither an entrywise imaginary-part shortcut nor this false adjoint identity is used. Real physical structure gives the same norm margins on both lips. Within the inherited finite matching/root-continuation hypotheses, strict margins give regular local boundary values on the retained windows and hence no uncharged singular seed mass inside them. This conclusion uses the actual background matching and regularity hypotheses, not the scalar determinant alone. Nothing here excludes actual outside atoms or other outside spectrum.

The new term b0|Delta|/lambda in (8) is real and cannot be omitted by recentering. Since kappa²=3jlambda(1+e3), its contribution is proportional to j b0|Delta|, rather than a bare |Delta|/lambda divergence after multiplication. Nevertheless b0 grows as g decreases; the scalar allowance |Delta|/j alone does not imply this loaded margin. Failure of (8) means this sufficient estimate fails, not that the actual inverse is singular.

## 4. Exact installed moment and concentration in the ORIGINAL union

Let V be the same product-seed isometry, and Pi_e project the old input onto K-energy e. Use a shifted source center ONLY for the moment calculation,

    E_e^Delta=c_att+2j+e+Delta,
    H_e^Delta=H-E_e^Delta.

On the first three source heads its prepared-vacuum diagonal is r_i. Applying H_e^Delta three times to the seed gives precisely four orthogonal head components:

    c0=r0³+a1²(2r0+r1),
    c1=-a1(r0²+r0 r1+r1²+a1²+a2²),
    c2=a1a2(r0+r1+r2),
    cp=-a1a2 kappa.

The third application FIRST reaches p. Although the centered port diagonal is now shifted by -Delta, it has not acted on that newly arrived component. No downstream contact or port diagonal enters this calculation. This is why the moment has no Delta term. This observation would not justify dropping Delta at fourth or later powers.

Consequently the exact prepared sixth central moment about E_e^Delta is

    mu6_r=c0²+c1²+c2²+(a1a2 kappa)²,
    Pi_e V*(H-E_e^Delta)^6 V Pi_e=mu6_r Pi_e,           (10)

with the usual third-power quadratic-form meaning if needed. In the present bounded one-head model the ordinary operator identity suffices. Its uniform envelope is

    mu6_r<=lambda^6 T_eps+(8/3)jlambda^5(1+epsilon)^3,
    T_eps=[epsilon³+epsilon(1+epsilon)]²
       +3(1+epsilon)(1+epsilon+epsilon²)²
       +8epsilon²(1+epsilon)².                        (11)

No source-dependent internal contact or extra source edge is allowed. Shared B iota=iota K, scalar residuals and the original prepared vacuum are essential.

The physical calibrated intervals have NOT moved. On I_e^c, the distance to E_e^Delta is at least b=d-|Delta|>0. The spectral theorem, then the triangle inequality over the two orthogonal INPUT projections, gives

    ||E_H(I^c)V|| <= min{1,sqrt(2mu6_r)/(d-|Delta|)³},
    0<=V*E_H(I^c)V
       <=min{1,2mu6_r/(d-|Delta|)^6} I_old.             (12)

No [H,K]=0 or orthogonality of the two omitted output images is assumed. Computational record0 remains coherent and arbitrary passive-reference tensoring preserves the bounds. This includes all output coordinates and all outside spectral types. It is an ACTUAL installed measure bound, not a scalar return-density assertion.

The moment statement is independent of (8) and of emission success. It remains valid under a compatible finite downstream cap, without transferring the infinite-ray boundary inverse to the finite spectrum. Any later complete-state synthesis must charge (12) once globally. As |Delta| approaches d the sufficient concentration bound deteriorates, even though the scalar common-mode model may remain well conditioned.

## 5. A nonempty offset interval for these two interfaces only

To show that the inequalities are not vacuous, take the already used source and background scales

    lambda=1e-13, g=5e-8, h=4e-6, epsilon=1e-6,
    |Delta|<=1e-10, |r_i|<=1e-19,

with the same fixed calibrated j throughout .0027<j<.003. No time, receiver length, output error or target waveform is selected. This is an inverse/concentration illustration, not a performance point.

Elementary uniform enclosures give

    2.15e-8<d<2.4e-8, b0<5.81e9,
    kappa²<9.000009e-16,
    beta<1.113e-7, B_eps<.000020000017,
    m>.99997988, A_eps/m<1.333364.

Then (8) is bounded by

    9.000009e-16 * {
       1.333364 * [(8e-18+.581)/1e-13+5.81e9]
                      +6[8e-18+5.81e9*2.4e-8]}
       <.0071<1.                                      (13)

The complement contribution is below 7.54e-13. The strict rounding in (13) is deliberately coarse. It holds simultaneously for every allowed tuple and either sign of Delta.

Also (11) gives mu6_r<8.000026e-68, while d-|Delta|>2.14e-8. Since sqrt(2mu6_r)<4.000007e-34 and (2.14e-8)^3>9.80e-24, equation (12) yields

    ||E_H(I^c)V||<4.1e-11.                             (14)

Thus the certified interface permits a common offset up to 10^9 times the residual bound epsilon lambda, and up to 1000 lambda, while retaining the original physical windows. This comparison concerns source common mode versus differential residual precision only. It neither relaxes arbitrary diagonal errors to 1e-10 nor claims unchanged complete output against a nominal zero-offset packet. The scalar source already shows that packets separated by many linewidths can have small overlap.

## 6. Remaining transfer obligations and source exposure

Equations (8)–(12) are the result. The unchanged calibrated processor is sampled at physical delta, not at y; all original downstream phase and W-error envelopes depend on that physical energy. A later common-mode packet target must retain the supplied offset, actual old aging, literal W and c_att. Recentring a scalar determinant supplies neither local/core escape nor the outgoing/incoming rows, physical-halfline normalization, quantitative time estimates or finite complete-output performance. Those arguments would need to be derived with their Delta dependence. The existing zero-offset complete tolerance ceiling is not transferred here.

The exact sources read/refreshed for this derivation are:

| Source | SHA256 |
|---|---|
| three_site_common_mode_source/PROPOSAL.md | 5076c3e9eb2683cdb8c9ad99bb002bc52ff242fdb9a6419d20e6acc22520b7fb |
| three_site_common_mode_source_check/REVIEW.md | af2e768b78e337f1f11d982ea83fdb1d6270f6b646ccb0895b79fd6613d44ffb |
| three_site_perturbed_attachment/PROPOSAL.md | f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d |
| three_site_perturbed_attachment_check/REVIEW.md | 0fd4a54559c48af641f9c90baa326e78a7bcc51f9428d0384ab6c7cc0252447d |
| slow_lead_wide_endpoint/PROPOSAL.md | c4c99408686166ba4d80bc973f5c22afdd1185bbf38e4539512dc26afd5cd5e3 |
| slow_lead_wide_endpoint_check/REVIEW.md | c6cc2ed747956e70bba1a7af3a5d65d3d36a7f708367727cb6f5e8a74386feb5 |

The common-mode and perturbed attachment sources/checks were read in full; the unchanged endpoint §§1–2 were refreshed and its previously fully read check reused at the verified identity. The original geometry/B/calibration dependency remains 71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff within that scope, not recalibrated here. No new local/core comparison is imported from the previously authored local/core extension.

I authored the scalar common-mode source and several scalar/local ancestors, but not the perturbed attachment or its distinct check. Root suggested investigating the original-window route; its proposed mechanism was reconstructed, not used as evidence. This is source-exposed author derivation and needs a distinct check of the shifted complementary bounds, arbitrary-forcing order, two lips, port arrival moment and arithmetic. No blind independence or retained-status certification is claimed.

Only this proposal was written. No numerical spectrum, parameter sweep, dynamics, scientific runner, numerical integration, W/Git/PR/checkpoint/prompt/model change or delegation occurred. Native coefficient supply, unknown-offset fixed-target tolerance, arbitrary apparatus errors and permanent halt remain outside the result.
