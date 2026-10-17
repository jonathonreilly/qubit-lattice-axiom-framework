# Three-site actual traveling synthesis and physical-halfline normalization

Status: new authored conditional interface, requiring a distinct check. This derives the incoming comparison from the actual real two-lip Stone formula and the checked three-site outgoing coefficient. No old-emitter rate or scalar contour bound is imported. The result is parameterized by precisely specified scalar functionals and by remaining actual local/background allowances, not a complete performance point.

## Premises and fixed scalar packet

Retain the installed three-site geometry, shared B, physical scalar c_att, real interactions, source vacuum and computational record0 preparation V of the checked attachment. Use its full background matching and source inverse on both physical windows. In particular .0027<j<.003 is the original calibration enclosure, 0<lambda<=1e−8, a1=lambda/sqrt(3), a2=lambda sqrt(8/3), kappa²=3jlambda, 0<h<=4e−6, 0<g<=1e−6, d=2j sin h, d/g<=1/2 and Theta<1 as in the checked outgoing source. No calibration is varied here.

Write E_b(k)=c_att+b+E_s(k), E_s(k)=2j−2g cos k, b=1,3. On the centered hard slow interval I_k, delta=−2g cos k=−2j cos q, and

    k_old(q)=2asin(sqrt(j/J)sin(q/2)),
    q3(delta)=(delta²−lambda²/3)(delta−kappa²m_j(delta+i0))
                                        −(8lambda²/3)delta,
    F3(q)=kappa a1a2 (2j sin q) zeta
               exp[i61q+i172k_old(q)]/[sqrt(2pi)j q3(delta)],
    t_f=exp[i(q+k)/2]sqrt(sin q sin k)/sin((q+k)/2),
    F_s(k)=t_f sqrt(g sin k/(j sin q)) F3(q(k)).       (1)

All quantities, roots and phases in (1) are exactly those of the checked three-site outgoing source. In particular the complex phase of 1/q3 is not removed. First slow site m=0 is distinct from the old gate port. The connector phase makes the scalar phase 61.5q+.5k+172k_old(q); 61 old-chain steps are not 61 slow-coordinate shifts.

Set p=int_I_k |F_s|² dk, so 0<p<=1, and F_hat=F_s/sqrt(p). The checked source supplies the exact integral and optional bound p>=1−Xi when Xi<1. This is the transmitted scalar-reference mass, not the actual seed retained mass. Denote its complete-input RAW outgoing allowance by

    E = Eout,sub = sqrt(2) Esel + Ewrong.           (2)

The source's Eout,norm is instead E+(1−sqrt(p)); these must not be silently interchanged.

## Exact actual two-lip identity and conjugation

Fix a parity and record-X sector x=±1 and use the common real old-energy/parity basis. The physical Hamiltonian, sector projection, source-vacuum embedding and coordinate inclusions are real in this basis. The new source hoppings and occupations are also real, so the replacement preserves this property. Hence entrywise conjugation of the upper resolvent COLUMN gives the lower column, with fixed conjugations on its domain and range. This is a linear coefficient-matrix relation; it does not conjugate an arbitrary complex input state. Self-adjointness alone would give a transposed rectangular relation and would not suffice for this step without the real structure.

On window I_b the retarded open slow-ray column has the form exp(ikm) A_x,b(k). Its lower boundary is exp(−ikm) conjugate(A_x,b(k)). The slow Jacobian and physical amplitude t_L have already been included in A. Equivalently, if A_tilde is the preconnector row, the Fourier coefficient is

    F_x,b(k)=i E'_q t_L(dq/dk) A_tilde_x,b/sqrt(2pi)
            =t_f sqrt(dq/dk) i E'_q A_tilde_x,b/sqrt(2pi).

Use the convention R(z)=(z−H)^{-1}; the spectral density is (R_−−R_+)/(2pi i). Because conjugate(i A)=−i conjugate(A), the represented open-ray evolution is exactly

    sum_b (1/sqrt(2pi)) int_I_k exp[−it E_b(k)]
       { exp(ikm) F_x,b(k)
          + exp(−ikm) conjugate(F_x,b(k)) } dk,
                           m>=0.                 (3)

Both signs inside the braces are plus. All cross-window input columns remain inside each F_x,b, carrying that window's physical E_b, not the input's energy label.

The complete matching and strict inverse margins supply seed absolute continuity on neighborhoods of the closed windows, including endpoints. Cross spectral measures into finite ray coordinates are then absolutely continuous, so Stone applies to (3). The L2 coefficient bounds and Fourier isometry yield an l2 halfline vector, and its equality with the actual open component follows from equality on every finite coordinate restriction. Closed channels on the same ray are not hidden in (3): their evanescent tails belong to the separate background allowance below.

## Full-input incoming comparison

On the selected vacuum column the ideal coefficient is x omega F_s, with omega the literal W eigenvalue. On wrong-window inputs its ideal coefficient is zero. The checked outgoing proof controls all these columns together by (2), including resonance-induced complementary mixing. Entrywise conjugation preserves operator norms and each L2 majorant used in that proof. It therefore gives the SAME E for the incoming coefficient discrepancy. In passing to time-dependent waves, each physical-window phase still has modulus one; the proof's separate selected/wrong-window estimates and aggregation remain valid. It is not necessary, and would be wrong, to conjugate exp(−itE_b) into a negative-time evolution.

The ideal incoming coefficient is x conjugate(omega) conjugate(F_s). Since the common old basis is real and W diagonal there, its old multiplier is W*, not W. The record-X multiplier x is real and recombines initial record0 into record1 in both reference traveling terms. Actual coefficient errors may contain either record value and are bounded before any projection. Orthogonal parity/record-X sectors combine by maximum, while the already-paid two old-energy and wrong-window costs remain in E. Arbitrary passive references preserve these operator bounds.

Define the RAW scalar halfline packets

    beta_t(m)=(1/sqrt(2pi)) int_I_k F_s(k)
                         exp[ikm−itE_s(k)] dk,
    alpha_t(m)=(1/sqrt(2pi)) int_I_k conjugate(F_s(k))
                         exp[−ikm−itE_s(k)] dk,
                            m>=0.                (4)

Then the ideal outgoing and incoming maps are respectively

    Traw(t)=exp(−it c_att) Jout[beta_t tensor exp(−itK)W],
    Tin(t)=exp(−it c_att) Jout[alpha_t tensor exp(−itK)W*]. (5)

Jout supplies source vacuum and record1 with first slow coordinate m=0. The notation includes the identity on any passive reference. W commutes with K in the ideal common basis; no analogous commutation with actual H is assumed. The entire phase in (5), including the 2j carrier inside (4), remains physical.

For the represented open traveling part U_open,I,

    ||U_open,I − Traw − Tin|| <= 2E,
    ||U_open,I − Traw|| <= 2E + ||alpha_t||.       (6)

Outgoing and incoming waves occupy the same physical halfline and are not generally orthogonal. Their coefficient discrepancies must therefore be added. The incoming norm equals its scalar norm because the old/reference multiplier is unitary; it cannot be absorbed into the W outgoing target.

## Precisely needed scalar bounds and normalization

A separate scalar derivation may supply either raw J_raw(t)>=||alpha_t|| or normalized J_in(t)>=||alpha_t||/sqrt(p). These are bounds for exactly (1),(4), including the hard endpoints and m=0. No change of q3 to a Markov cubic, phase removal or auxiliary source formula is implicit. If J_in is normalized, use J_raw=sqrt(p)J_in.

For outgoing concentration extend the Fourier sequence beta_t to all integer m and define

    C_out(t) >= ||1_{m<0} beta_t||/sqrt(p),
                       0<=C_out(t)<=1.           (7)

The full lattice Fourier norm is sqrt(p) by Parseval after extending F_s by zero to [−pi,pi]. Consequently the physical-halfline norm r(t)=||beta_t|| satisfies

    r(t)>=r_min(t)=sqrt(p) sqrt(1−C_out(t)²).      (8)

The excluded sites are m<=−1, not m<=0. A scalar estimate using the larger excluded set is conservative but must be stated as such. When r_min>0, Tnorm=Traw/r(t) is a unit-norm common-target isometry. Its exact distance from Traw is 1−r(t), bounded by 1−r_min. This is normalization of an ideal physical-halfline packet, not conditioning or renormalizing actual output.

Suppose separately established actual represented bounds are S_I(t) for all three source heads and B_I(t) for the remaining finite coordinates and all closed tails. Let epsilon_sp>=||E_H(I^c)V|| be the SINGLE global actual omitted-state allowance. Then (6) and spatial decomposition give the conditional synthesis interface

    ||exp(−itH)V − Traw(t)||
       <= epsilon_sp + S_I(t) + B_I(t) + 2E + J_raw(t),
    ||exp(−itH)V − Tnorm(t)||
       <= epsilon_sp + S_I(t) + B_I(t) + 2E
                           + J_raw(t) + 1−r_min(t). (9)

One may insert the checked represented local-source bound for S_I; its reference truncation term is not another actual omitted charge. B_I must cover all remaining components, without counting the source heads again. Equation (9) is not closed until those inputs are available.

With normalized scalar bounds the last terms are explicitly

    2E + sqrt(p) J_in(t)
      + (1−sqrt(p))
      + sqrt(p)[1−sqrt(1−C_out(t)²)].              (10)

This displays spectral transmission loss and halfline concentration loss exactly once. Applying 2 Eout,norm and then also charging 1−r_min would unnecessarily pay the spectral normalization twice. For a bound expressed using Eout,norm, (10) equals

    2 Eout,norm − (1−sqrt(p)) + sqrt(p) J_in(t)
                       + sqrt(p)[1−sqrt(1−C_out(t)²)].

It is simpler to retain the raw E in (9)–(10). If only a p lower bound is known, use it in r_min; retain the exact p or upper bound sqrt(p)<=1 for the incoming factor. No numerical Jin/Cout or onset is asserted here.

## Remaining scope, sources and exposure

No scalar contour is proved in this artifact. The required functions are precisely the conjugate incoming hard-band norm and outgoing negative-halfline norm in (4),(7). Actual complex continuation is not inferred from a scalar contour. Even with these scalar bounds and local-source decay, complete background escape and any finite-cut transfer remain separate proofs. No full performance point, old-emitter runtime, finite receiver size, success probability, permanent halt, repeated monitoring, native supplier or optimality is claimed.

Read complete three-site outgoing source `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac` and distinct check `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02`. Read complete wide composition `5275860cb241a358d53460e88183879009a9899de7172c7c3b2e75629eb42fba` as a synthesis template only, and refreshed the real two-lip/conjugation argument of attached composition `7b618a13d8094d0535ca399025ca872b54b8fdb2c9a307a0b31f521306c18e73`. The unchanged wider outgoing row source is `593ed5c43008a40101cfc5a9c8243d7190ea7a3f822becbd9644f30b5f74d606`, scoped check `55de89b5d0536b0ce8028e4a346feb29bcf073f6012dd9cb9e6c01a5d76ead77`. These sources are used for their stated real-band identities, not one-site temporal constants.

Installation source/check are `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006` / `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`; ordered inverse source/check `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672` / `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`. Optional local-source input is `three_site_local_escape/PROPOSAL.md`, `0340895610d3a5ef709dd8a03c1bc5872c8f34cf00f21053c00adcc3d706468d`, with my check `e19767c8092fb856a3c24cb279f621deea38d69d65c41bef4a1aea44bad23074`.

I authored this interface and previously authored or reviewed multiple narrower scalar/emitter/composition ancestors; I checked the current attachment, inverse and local-source interface. Root requested the conjugation and normalization qualification. This is exposed author derivation, not an independent check of itself or blind revalidation of those ancestors. A distinct check is required, particularly of fixed real conjugation, W*, physical window phases, both traveling factors and normalization bookkeeping. No numerical dynamics, sweep, solver, contour computation, delegation, W/Git/PR/checkpoint/prompt/model change or publication occurred. Only this proposal was created.
