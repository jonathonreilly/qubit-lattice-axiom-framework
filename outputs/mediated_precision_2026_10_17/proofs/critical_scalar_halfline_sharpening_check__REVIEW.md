# Distinct check of the scalar halfline sharpening

Conditional support; no required mathematical correction found in `critical_scalar_halfline_sharpening/PROPOSAL.md`, SHA256 `9fb115c3135c97f294783310e28c55e6b6073f076a4f66ebb9fe8d6f37e98f7d`. The same-packet stitching lemma, normalized/raw accounting, and conservative scalar numerical bounds are supported. This certifies scalar reference allowances only, not a revised actual-device onset, complete error or receiver size.

I read the full target, the complete weighted and all-late sources and their reviews, and the complete finite-point source/review furnishing the scalar enclosures. All seven source identities were refreshed and match the supplied pins. The existing exact-arithmetic finite-point calculation was not rerun or newly recertified here; its distinctly checked scalar enclosures are inputs. I reconstructed the new elementary inequalities and the direction and margins of every displayed numerical substitution.

## Same packet and restricted cutoff

The weighted numerator sqrt(sin q sin k)|t_f| equals sin q sin k/sin((q+k)/2) on this positive-angle band. Therefore both antecedents use literally the target's F, with the same fixed zeta, phase61.5q+.5k+172k_old, physical complex q3, slow dispersion and Fourier cell. The slow Jacobian has already entered sqrt(2g) and the numerator; it is not inserted again when taking the minimum of bounds. Incoming uses conjugate(F), reversed spatial phase, and the SAME positive physical time.

In the evaluation, d=rho and the physical fast-angle halfwidth is h_rho=asin(rho/(2j)). The finite-point B and v enclosures were derived for exactly that restricted band. Using the original larger4e-6 only in the positive phase ceiling P is conservative because cos(h_rho)>=cos(4e-6). It does not restore the old wider cutoff in p, B, v or the hard tails.

The weighted proof uses x=2g(k-pi/2), with physical endpoint 2g asin(rho/(2g))>=rho. Hence D=rho is a valid FIXED auxiliary cutoff. Its corresponding physical tail threshold is delta_D=2g sin(D/(2g)), slightly below rho; the source uses this threshold in U and D in the rational tail V_D. It does not confuse x and physical delta. No condition D^3/(g^2 lambda)<<1 is imported, and the full divergent rational sixth moment is not used.

## Stitching and indexing

For incoming m>=0 and outgoing m<=0, the exact-dispersion theorem permits the same J_in bound, including the outgoing m=0 summand. At vt>=1, J_in/sqrt(p)<=B/sqrt(pi p vt)=b/sqrt(t). The weighted theorem bounds these same normalized sequences by E0+a_D t, or H(lambda t)+E0+a_D t, respectively. Thus their minimum requires no packet comparison or additional error.

At t_cross=(b/a_D)^(2/3), a_D t_cross=b/sqrt(t_cross)=(a_D b^2)^(1/3). Splitting t below/above this value proves min(E0+a_Dt,b/sqrt(t))<=E0+R_cross, even though the nonzero E0 shifts the true optimal crossing. The chosen crossing is sufficient, not claimed optimal. The proof does not require t_cross to lie in the domain where both original estimates apply: the resulting inequality is used only at times satisfying that domain.

For outgoing, min(H+E,q)<=H+min(E,q). Each term z^k exp(-2z), k<=4, is nonincreasing for z>=2, so H(lambda t)<=H(lambda T) for t>=T>=2/lambda. Keeping the independent b/sqrt(t) alternative gives exactly (2). The finite-window bounds in (3) use t<=T1 only in the growing weighted term; no exact-dispersion threshold is required for that alternative. No growing dispersion estimate is extrapolated alone to all future times.

## Normalization

The full integer sequence a has norm one; the raw beta has norm sqrt(p). Since m<=0 contains the actual excluded m<0, a ceiling h for the former gives ||beta_+||^2>=p(1-h^2). It is an inequality, not an identification of the two excluded sets. Whenever h<1 the normalized physical halfline state is defined.

For beta_+ the raw-to-unit distance is exactly1-||beta_+||; for mediated beta_+/sqrt(Z0) it is exactly1-||beta_+||/sqrt(Z0). The stated ceilings follow. The1-sqrt(p) already used inside E0 proves the normalized scalar functional estimate and must not be added as another physical normalization charge after1-sqrt(p(1-h^2)/Z0). Both actual coefficient discrepancies and one actual omitted state remain separate. The use of h_left rather than a sharper m<0 bound is conservative.

## Conservative numerical substitutions

All following use the checked baseline enclosures, with g=5e-8 fixed, lambda<3.10e-18, rho<3.94e-11 and rho>3.93e-11. They do not independently vary the actual correlated supplier tuple; they bound it by its existing enclosures.

- D/(2g)<.000394. The sine remainder gives alpha_D>=1-(.000394)^2/6>.999999974. Together with3lambda/j<3.45e-15 this implies s alpha_D^3>.99999992.
- Since2j cos(4e-6)>.0053, P<5e6+102.78/.0053<5.02e6. Using sqrt3>1.7 gives P lambda/sqrt3<9.155e-12. Adding3lambda/j<3.45e-15 and the quadratic term<5.4e-21, then dividing by m_D>.99999992, stays below9.21e-12. The quadratic term's dominant part is lambda^2*11/(8g^2)<5.286e-21; its j part is negligible within the stated ceiling.
- The lower bound delta_D>.999999974*(3.93e-11) gives lambda/delta_D<8e-8. The sharp-tail prefactors are below one, and (8e-8)^(5/2)<1.82e-18. V_D has the same safe ceiling. For aliases, lambda/(2pi g)<1e-11 and its prefactor is below3, yielding a bound below1e-27. Since1-sqrt(p)<=1-p<2.065e-15, these contributions plus E_c give E0<9.3e-12.
- The upper quantity16(3.10e-18)^5(3.94e-11)/(3pi) is below2.006e-98, using pi>3.14. Since24g^2=6e-14, its square root divided by6e-14 is below2.37e-36. Thus the displayed a_D ceiling has slack.
- Using B<780135, p>1-2.065e-15, v>9.9999992e-8 and pi>3.14 gives b^2<1.94e18. Multiplication gives a_D b^2<4.5978e-18, while(1.67e-6)^3=4.657463e-18. Hence R_cross<1.67e-6.
- At z=20 the continuous part of the H-square bracket is118174+1/3. The discrete part is(2lambda/(3g))*160000<6.7e-6. Their sum is below344^2=118336. The finite positive exponential series through degree12 at5 exceeds148; hence exp(20)>148^4=479785216 and H(20)<7.18e-7.
- Therefore E0+R_cross<1.7e-6 and H(20)+E0+R_cross<2.4e-6. The onset20/lambda is above2/lambda and1/v, and20/(3.09e-18)<6.473e18. These establish the all-late scalar claims with strict slack.
- On20/lambda<=t<=40/lambda, t<1.295e19 and a_Dt<3.07e-17. Thus E0+a_Dt<1e-11 and H(20)+E0+a_Dt<7.2e-7. Finally1-sqrt(p(1-h^2))<=1-p+h^2: using7.2e-7 gives less than5.20465e-13<5.21e-13; using2.4e-6 gives less than5.762065e-12<5.763e-12.

The comparison to the baseline scalar threshold is accurate as a comparison of sufficient scalar estimates. It does not prove an earlier actual complete-device point: local/source/mediator terms, both actual raw errors, the physical seed factor and the new finite-window cut would all still need composition.

## Exposure and limits

Exact refreshed premises: weighted d41e468ffec769a9f5a36a7796999366fddf04ff2b42c1a8083c20e46f243d36/check809c0e0b452b4d913d5750f3aa184473c4d4b20132de7a73b919e8d0be5415ac; all-late7044e77bcf2d944a3f1b4286b885691fd9f88e733a6ab49514111af5acbc5966/check4ba80afbbc2301fbb4e23aafe59f85b3a85ebdab160101f970774d0383139247; baseline243c172226f2a509ce9ba11686763ebc2e754f52a8b5a4e98d6ab4424c0ca20d/check080266c4b4f7d0b26ef2d366582961221a91294ed207f615bc29d7fbf4d1223d.

I authored the original scalar source/reference-time work and checked the weighted, outgoing and traveling refinements. I did not author this stitching source or the baseline finite-point calculation. The unchanged residue, alias and calibration premises are reused through their scoped checked evidence, not claimed as newly independent ancestral validation. This is a distinct reconstruction of the new stitching and arithmetic with shared model/source exposure.

No defect was found within the assigned scalar scope. No actual apparatus composition, new source preparation, numerical dynamics, quadrature, parameter sweep, root solve, author-calculation rerun, canonical/W/Git/PR/checkpoint/prompt/model change or delegation occurred. Only this review was written. Identity checks establish source revision, not empirical or retained-audit status.
