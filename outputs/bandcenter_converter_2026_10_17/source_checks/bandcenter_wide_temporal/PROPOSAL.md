# Wider nominal band: explicit temporal transfer and one sufficient onset

Status: authored analytical extension, not independently checked. At fixed kappa=1e-8 and new momentum halfwidth Delta=4e-6, the changed-domain estimates below give the conditional infinite-device curve

    error(t)<.001512+1.26e13 exp(-5.3e-16 t)
                       +1.21e11/t+q_in(t)+q_-(t)^2.

Its conditions include s_t=.0053t-64>=1 and q_-<1, with explicit scalar bounds below. One transparent sufficient candidate is T=1e17: the curve gives error(t)<.001514 for all t>=T. This is a proposed conditional onset, not an independently checked runtime, old-tolerance claim or finite-device theorem. No M is selected.

## Sources, exposure and scope

Read complete final temporal route ../bandcenter_temporal_route/PROPOSAL.md, SHA256 add82a40ddc49a7c7954ea1b087b1b1bf348e8375da072c96b2b2df1b6d2c011, and complete independent ../bandcenter_temporal_check/REVIEW.md, SHA256 6df1d5809db83393bfd449442a355a6d25f5f26b31bdecf81c3a833ae67f5a23. This includes the corrected direct conjugate-incoming initial comparison, not the earlier uncorrected packet-switch argument. Both hashes were verified.

Use final wider real-band source ../bandcenter_bandwidth_extension/PROPOSAL.md, SHA256 d79a1e9abbf0508a05169d4588539063854f0604ba8db933cf878496aa7328a2, and its check3f721b75911630e0aec48688893c6bae84a182cafaa1012c977e9e262d6e180d, both identities verified. I authored the latter check and the original weighted-profile proposal; those are explicit exposed dependencies, not a new independent review of my own work. The temporal proof and its independent check are distinct authorship. Their exact original canonical disk/source ingredients at note71c65d72570a32365ded6dacfc78308ac8429d9e8003a3731af88b5600eb45ff are reused conditionally, not regenerated or extrapolated beyond their fixed original domains.

The fixed device, two converters F=40, source/filter/junction, new input ell=20, literal K/W, exact nominal j/tau and full shared B are unchanged. Only the comparison cutoff is Delta=4e-6. Original source real halfwidth remains1e-6. No common-j drift family is considered. Applicable unchanged workflow reused. No scientific execution, solver, numerical sweep, delegation, Git/W/checkpoint/prompt/model modification occurred. One initial text read used a nonexistent temporal directory; it failed without reading or modifying any source, and the correct frozen paths above were then located/read in full. This proposal is the sole deliverable. Finite transfer is separate; no unfinished finite-transfer work was read.

## 1. Larger real band and mapped complex disks

The checked energy-margin-first inclusion gives |E(q)-E0|<2.4e-8, below the two original edge margins2.5e-8. Consequently every real q in pi/2±Delta maps inside the original source band and |k-k0|<.96e-6. All original real and radius-rho_old=1e-12 complex disks centered on that old band are available.

Take rho_q=1e-12 disks centered on the NEW real band. The explicit analytic map cos k=C0+(1-C0)cos q, with original sin k>.4, has |k'|<.25 by the same first-exit argument as the checked temporal source. Therefore each q disk maps within .25rho_q of its old real center, inside its already checked old disk. This is not a radius increase. The real center's .04e-6 old-band clearance is much larger than this displacement, although the old disk premise itself is already stated at every old-band center.

Reuse on those disks: analytic old matching inverse167, Aold41, Aold^-1<22, full exterior image2e7, filter response2100, old open two-port norm<1.003 and reflection<2e-5. Full old pretermination site kernels<3e7 and driven unit-incoming columns<2e6 also apply to the finite old buffers, whose propagation distances remain below226. They derive from exact kernel/forcing formulas, not off-real unitarity.

The wider REAL band still has all seven new signed closed roots<1/60 and gap>.18. Their disk variation is<1e-12, preserving the tighter |s|<1/60+1e-12 and the loose .02 bound. Thus An,c<7, full An<201, An^-1<22 and |exp(iq)|<1.001. All projections remain fixed in B's real basis.

## 2. Recomputed converter and return margins

The closed-converter denominator/derivative argument in the temporal check remains uniform over these mapped old disks: |H'_q|<.008, real |H|>5.99J, hence the relaxed disk margin5.65J, |R_o,c|<.21, |u_c|<.042, |v_c|<.05 and |R_n,c|<.002 remain valid. The last two use the TIGHT continued root bound, not merely .02. These follow from the old/new root equations on the same gap domains and do not depend on the smaller original q cutoff.

The REAL open reflection ceiling is now1.22Delta=4.88e-6. Continue the explicit quotient from each real point, whose denominator is>.024-.03(Delta+rho_q); its disk derivative is<1.3. The additional variation is<1.3e-12. A safe disk ceiling is

    |r_o|,|r_n|<4.89e-6,
    |t_c-i|<12.01e-6,
    |u_P|<.5, |v_P|<2.5.

Transmission follows by analytic variation of its explicit phase/velocity formula from the checked real3Delta bound. Coefficients have fixed positive denominator margins; there is no off-real flux argument. The amplitude margins .49/.5 and2.5 are unchanged because the mapped real k range and new sin q remain within their previously proved inequalities.

Old closed/mixed generalized source blocks remain<1e-10 with their fixed24 propagation steps; ||So||<1.01. Closed return is<.21(.15)^80. Open return, including eighty tiny complex phase steps, is<4.90e-6. Thus the FULL return inverse is now

    ||(I-R_o Qo^(2F)So)^-1||<1.000006.             (1)

The old1.000003 ceiling is not reused. Substitution into the ordered generalized formula gives ||Sn||<1.3 and ||Tn||<600, with large slack:2.5*.5*1.01 times finite phase/return factors is below1.27, and the direct closed R_n is<.002.

For the open comparison, |t_c²+1|<=|t_c-i|(|t_c|+1)<24.021e-6 on the disks. Direct new reflection contributes<4.89e-6; the return correction is bounded using ||Sold||<1.003 and (1), with propagation<1.001, by<5e-6. Remaining closed feedback is negligible. A relaxed total converter comparison<3.7e-5 is therefore safe. Adding the old reflection2e-5 and finite phase factor gives the useful disk bounds

    |Rnew|<6e-5,   |tnew|<2.                       (2)

This explicitly replaces the old3.1e-5 disk reflection bound. No scalar center match is asserted across the complex neighborhood.

## 3. Exact projected deletion inverse and full background bounds

Define X,X0,Z exactly as in the checked endpoint/temporal sources. Still ||X-X0||<3*600*(.02)^20<2e-31. Now ||X0||<201*(6e-5)*1.001<.0121, while ||An+X||<202. A crude bound22||X0|| would no longer justify the former convenient inverse26. Instead use the EXACT diagonal structure

    Z0=An+Qn X0 Qn,
    Z0,PP=An,P[1+Rnew exp(i(2ell+2)q)],
    Z0,CC=An,c.

Therefore ||Z0,CC^-1||<22. For its OPEN inverse, |E'_new| is actually below .006000000001 on these tiny disks, so division by1-6e-5*1.001 remains<.0061. Hence ||Z0^-1||<22, and the perturbation Qn(X-X0)Qn is<3e-31; its inverse has, conservatively,

    ||Z^-1||<26,
    ||Z^-1-Z0^-1||<2e-28.                          (3)

The exact ordered Dirichlet function therefore retains ||Gend||<400 and non-scalar error<1e-22. To check the first, its scalar block is bounded by (1.001/j)(1+6e-5*1.001)/(1-6e-5*1.001)<372; the closed diagonal block is small, and the Lipschitz correction is far below1. The same202/26/2e-31 estimates handle full noncommuting corrections.

The COMPLETE pretermination site-kernel bound1e9 remains valid, with its proof updated by (1): a new open source An,P<201 induces old open incidence<.51*201; the two driven old site columns contribute<sqrt(2)*2e6, yielding<3e8. New closed source data An,c<7 times .042 carries (.15)^40 before reaching the source, and its response uses the full old closed incoming column sqrt(2)*3e7*22. Its mixed return contributions remain tiny. On old buffers, preceding propagation cancels growing closed factors into Qo^(F-m) or Qo^(2F-m). New-stub kernels remain<1000. These are complete source/block estimates, not only open output bounds. The unchanged finite-site count<250 covers all apparatus positions included here.

Consequently the selected endpoint column after deletion satisfies

    P<sqrt(250)*1e9[1+26*1.001*202]<9e13.            (4)

For incidence from the surviving output, the opposite-port identity phi_a(m)=iE'_new Qn^m Tn_ao u is unchanged. Its open endpoint/deleted-site amplitude<2.1 follows from(2), and its closed amplitude<4e-34 follows from twenty .02 powers. Apply OPEN inverse .0061 to the former and FULL inverse26 only to the latter, then pay the tiny inverse correction. This gives ||Gbb^-1 phi(b)||<.014, just as a newly proved bound under(2)–(3). The complete pretermination incident field remains<3e6 by the driven-column calculation. Thus

    X_bg<sqrt(250)[3e6+.014*1e9]<3e8,
    Y<2.1+202*1.001*.014<6.                         (5)

All eight coordinates remain in (4)–(5); no extra factor eight is needed in these block-column norms.

## 4. Full emitter strip and complete localized column

Use strip depth h_c=1e-13, distinct from cutoff Delta. The disk bound400 gives endpoint oscillation<=400h_c/(rho_q-h_c)<44.45. The WIDER real-band endpoint theorem still gives Im Dj>329kappa², even though its uniform relative ceiling is now1e-4. The imaginary kinetic shift costs<.0061h_c=6.1kappa²; complementary self-energy changes cost<2e-10 kappa². Thus Im Dj>278kappa² throughout the lower strip, the complement inverse stays<6 and the full emitter inverse is<1/(250kappa²).

At the new cutoff sides, real kinetic distance is d=2j sin Delta>.0053Delta=2.12e-8. Subtracting .0061h_c²,400kappa² and6kappa⁴*400² leaves>2.119e-8. The full side inverse is therefore below the former loose2e8 ceiling (indeed a5e7 ceiling would suffice). Retaining2e8 here is a checked relaxation, not an inherited unchanged domain assertion.

The exact source-forced Schur solution is

    x=[x_bg;0]+[-kappa R_bg E_end;I](-kappa De^-1 y).

Equations(4)–(5) give sqrt(1+kappa²P²)<900001. Subtract only the actual incoming/outgoing open waves, retain all finite apparatus coordinates and the entire closed output tail, and use the checked Hilbert-valued geometric-tail bound ||C||<=3||x||+4. It follows again, now on the wider real-base strip, that

    C_bottom<7e12,   C_side<1e9.                    (6)

Uniform closed-root modulus .02 gives holomorphic square-summable tails. No off-real bound |R_inst|=1 or analytic continuation of an asymptotic growing-wave norm is used.

## 5. Scalar phase, changed initial packet and localized contour

The full profile phase remains Phi(q)=21q+172k(q)+constant, with |Phi'|<64. Physical comparison also retains exp[-it(c_old+4gamma)] and exp(-itK)W. The mapped k branch is analytic with this derivative on the column disks and on the scalar-only strip |Im q|<=Delta/2; the latter follows directly from the inverse-cosine branch margin and does NOT continue the interacting source there.

The checked wider static bound is S_initial<.001510, with weighted coefficient norm delta_j=||(F_j-omega_p Fref)1_I||<9.6e-7 and p0>1-1.1e-6. For the contour packet use a0,j=conjugate(omega_p Fref/sqrt(p0)), not the former exact-outgoing target's incoming coefficient. Prove its initial bound DIRECTLY: real seed incoming coefficient is conjugate(F_j), by the actual scattering jump and reciprocity. Conjugation preserves each fixed column's coefficient L2 distance, so the wider outside mass plus delta_j plus1-sqrt(p0) proves the same .001510 initial operator ceiling after old-energy aggregation. Linear extension to arbitrary complex old/reference input does not conjugate the input amplitudes.

The real-axis identity F_j=R_inst conjugate(F_j) gives additional outgoing error<=2delta_j/sqrt(p0)<2e-6. It is paid ONCE, after this direct incoming-transform initial comparison. Output old fibers are orthogonal, so this outgoing cost needs no new sqrt(2); the initial and localized terms have already paid their within-parity overlap. Thus the static subtotal for this temporal packet is<.001512.

The conjugate denominator on q=x-iy has imaginary part -sin x[2j sinh y+(kappa²/j)exp(-y)]. It remains pole-free. Reference normalization is now improved, and the same conservative bottom |a0|<.003/kappa holds. The NEW cutoff real margin is>.0053Delta, giving side coefficient170kappa/Delta. Phase growth exp(64h_c)<1.001 is covered in these coefficients. Both sides and the Fourier/old-energy factors give

    E_loc(t)<=1.5[Delta*(.003/kappa)*C_bottom exp(-vth_c)
                      +(170kappa/Delta)*C_side/(vt)],
    v=.0053.

Substituting Delta=4e-6 and(6) yields the UPDATED curve

    E_loc(t)<1.26e13 exp(-5.3e-16t)+1.21e11/t.       (7)

The bottom coefficient grows by four; the side coefficient decreases by four (rounded upward). Neither effect is omitted.

## 6. Wider scalar tails and positive normalization

Let s_t=.0053t-64>=1. For the incoming scalar use h_i=Delta/2=2e-6. The conjugate denominator stays pole-free; its bottom coefficient170kappa/h_i and cutoff coefficient170kappa/Delta remain justified by the exact formula. For the outgoing negative half-line use h_o=kappa²/(4j²), with the unchanged exact imaginary lower margin>165kappa² and bottom coefficient .006/kappa. C is not continued to either scalar height.

Both cutoff edges, Fourier normalization, full Phi derivative and geometric/reciprocal-square lattice sums give

    q_in(t)<=170kappa Delta h_i^(-3/2) exp(-s_t h_i)
                                  +300kappa/[Delta sqrt(s_t)],
    q_-(t)<=.006 Delta/[kappa sqrt(h_o)] exp(-s_t h_o)
                                  +300kappa/[Delta sqrt(s_t)]. (8)

These are the same derived contour formulas with their ACTUAL new widths and heights. Convenient explicit relaxations at kappa=1e-8, using j<.003, are

    q_in(t)<.003 exp(-2e-6 s_t)+.75/sqrt(s_t),
    q_-(t)<1.5e6 exp[-s_t/(3.6e11)]+.75/sqrt(s_t). (9)

Here h_o>1/(3.6e11), sqrt(h_o)>1.66e-6 and the corresponding bottom prefactor is<1.5e6. The full normalized reference packet has norm one. Once q_-<1, positive normalization of its output-half-line restriction costs1-sqrt(1-q_-²)<=q_-²; no physical state is postselected and no negative-tail mass is silently deleted.

The complete proposed infinite operator curve is therefore

    error(t)<.001512+E_loc(t)+q_in(t)+q_-(t)^2,      (10)

under s_t>=1 and q_-<1. All common phases, old aging, source/emitter/complement coordinates and passive references remain explicit.

## 7. One transparent sufficient candidate, no search

Choose the single onset candidate T=1e17. This is derived from the displayed curve, not a numerical sweep or an alleged optimum. For t>=T, all terms decrease and s_t>5e14. The localized side is<1.21e-6. The bottom exponent is at least53. An elementary witness e>8/3, (8/3)^5>130 and130^5>3e10 gives e^53>130^10*18>1.62e22, so the localized bottom is<1e-9.

For incoming scalar bottom, 2e-6s_t>1e9 and e^-a<=2/a² give a contribution<6e-21. The shared scalar side is<.75/sqrt(5e14)<3.75e-8. The outgoing bottom exponent exceeds70, and e^70>2^70>1e21 makes its contribution<1.5e-15. Hence each scalar norm is<4e-8 and q_-²<1.6e-15. All validity conditions in(10) hold.

Consequently, for every t>=T,

    error(t)<.001512+1.21e-6+1e-9+4e-8+1.6e-15
             <.001514.                            (11)

This is a conditional sufficient infinite-device vector/isometry error, with unhalved trace ceiling<.003028 if that metric is desired. It is not the older .0013 tolerance and does not assert improved resources. The choice is intentionally transparent rather than optimized. A separate finite-transfer argument can later combine a predeclared horizon with this curve; no finite M, endcap placement decision or all-future finite halt is inferred here.

## Required check and limitations

Selective independent checking should focus on the new complex reflection/return ceilings, exact projected Z0 inverse, survival of complete driven-column P/X/Y bounds, widened cutoff coefficients and the direct incoming-packet comparison. The original-width proof remains separately valid and has not been rewritten. This extension is authored and not independently checked; the separate finite hopping-only transfer work is neither presumed nor duplicated. Native supplied data, physical units, common-j drift, differential errors and fixed-nominal robustness remain open scope.
