# Distinct check: three-site traveling interface

Disposition: supported as a conditional synthesis interface. No correction requested. Equations (3), (6), and (9) correctly retain both actual traveling terms, and the normalization in (8)–(10) is paid once. This does not close a complete performance theorem: actual background allowances and independently checked scalar time estimates are still required.

Checked complete changed source `three_site_traveling_interface/PROPOSAL.md`, SHA256 `75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3`. I did not author it. I authored the scalar three-site source, the new scalar reference-time proposal, and several composition ancestors, and checked the outgoing synthesis. This is a distinct check of the present interface with explicit shared exposure, not ancestral recertification or an independent check of my reference-time proof.

## Rectangular two-lip identity

For fixed real coordinate embeddings and a real sector Hamiltonian, conjugation gives C_range R_+(E) V C_domain=R_-(E)V. This is entrywise conjugation of the coefficient matrix and defines another linear map. It does not conjugate an unknown input or passive reference. Self-adjointness alone would instead relate opposite rectangular blocks by adjunction, so the real-structure hypothesis is essential. The installed real source replacement preserves the inherited hypothesis; record-X projections and the common K/parity basis can indeed be chosen real.

With the convention R=(z-H)^-1, the jump is (R_- - R_+)/(2pi i). Setting F=i E' A/sqrt(2pi) gives outgoing coefficient F and incoming coefficient conjugate(F), both with plus signs. The negative sign from conjugating i is necessary and is handled correctly. The physical time multiplier remains exp(-itE_b) on BOTH terms. It is not conjugated along with the matrix coefficient.

The source's finite-coordinate Stone argument is sound under its stated seed absolute continuity and full matching premises. Absolute continuity of the seed spectral measure implies absolute continuity of every coordinate cross measure. Fourier L2 bounds then identify the infinite open-ray vector from its finite coordinate restrictions. This is not an assertion that a stationary plane wave has finite norm. Closed/evanescent components are excluded from this open traveling representation and must be covered separately.

## Full inputs, W*, and physical energies

The checked outgoing row ideal is x*omega*F_s on the selected vacuum input, with zero ideal on wrong-window columns. Fixed real conjugation changes it to x*conjugate(omega)*conjugate(F_s). Thus the ideal incoming old multiplier is W*, exactly as stated. It cannot be replaced by W unless an additional special identity is proved; none is assumed here.

The coefficient majorants in the outgoing proof cover complementary mixing before restriction to prepared inputs. Conjugation preserves those same operator norms and L2 estimates. The two physical windows keep their actual E_b(k), including on wrong-window input columns. Only the ideal selected part factors exp(-itK); no commutation of actual H with K is used. The source uses the separate window/column bounds, so arbitrary time-dependent unit-modulus window factors do not invalidate E.

The already-paid sqrt(2) selected-column cost and wrong-window triangle cost are retained in E. Orthogonal parity and record-X sectors add no new factor; the real x recombines record0 into record1 for both ideal terms. Tensoring an arbitrary passive reference preserves the operator bounds. Since incoming and outgoing waves share the same physical halfline, their errors add by triangle inequality, giving 2E, not E and not an unproved orthogonal sum. The incoming ideal norm is precisely ||alpha_t|| because its old/reference multiplier is unitary.

## Scalar identification and normalization

The F_s, q3, first slow coordinate m=0, slow Jacobian and connector phase in this source agree exactly with the checked outgoing coefficient. The reference-time proposal at `three_site_reference_time/PROPOSAL.md`, SHA256 `d21632c8660f92e9478433bb564b357fe623aaa86c465d82537cfb28b77b315f`, defines its normalized outgoing and conjugate incoming packets using exp(-it delta). Therefore the present raw packets are exactly sqrt(p)*exp(-i2jt) times those respective packets. There is no translation, fitted phase, missing Jacobian or per-input packet change in that identification.

Consequently, IF that separate time proof is independently supported, its E_time(t) can supply J_in=min(1,E_time(t)), and its min(1,H(lambda*t)+E_time(t)) can supply C_out for its stated t>=2/lambda regime. That proof excludes m<=0; the present required complement m<0 is smaller. The latter is therefore a conservative substitution, not an indexing equality. This review checks the definitions and substitution only: I authored the time proof and do not independently certify its residue, alias or error constants here.

Parseval gives full-line norm sqrt(p), not unit physical-halfline norm. With r=||beta_t||, the exact normalization difference is 1-r, and r>=sqrt(p)*sqrt(1-C_out^2). The physical target exists when this lower bound is positive. Its normalization is a mathematical choice of comparator, not renormalization of actual output or a postselected branch. Formula (10) is the algebraic identity

    1-sqrt(p)*sqrt(1-C_out^2)
      =1-sqrt(p)+sqrt(p)*(1-sqrt(1-C_out^2)).

It correctly charges spectral transmission and spatial restriction once each. Using 2Eout,norm and then adding the whole physical normalization would double-charge transmission. The source avoids that by using the raw E and gives the correct equivalent conversion. With only a lower bound on p, using that lower bound in r_min and sqrt(p)<=1 on the incoming allowance is conservative.

## Conditional complete synthesis and limits

The single global omitted state contributes epsilon_sp once. Represented source, remaining finite/background and closed-tail terms must cover the remaining actual components; their proposed sums need no spatial or window orthogonality. In particular B_I must include every closed component on the output ray and all wrong-window recovery, even where its channel decomposition depends on the current energy window. The source explicitly requires that coverage rather than deriving it from an endpoint or scalar measure. Under those inputs, triangle inequality yields (9).

No bound for S_I or B_I is proved by this traveling interface. No scalar reference-time estimate, actual complete-state performance point, useful onset, finite cut, or resource improvement follows merely from its algebra. The optional local-source source/check is not needed for the present conditional derivation and was not recertified here. Full physical scalars and old aging remain present; a later finite-time composition must also retain them.

## Evidence reused and verification limits

The complete outgoing proposal `af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac` and my selective review `721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02` supply the unchanged coefficient estimates. Installation `4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006` / distinct check `ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d`, and inverse `7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672` / check `8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2`, are reused at their prior fully read unchanged scope. The real two-lip conventions and common real old basis were refreshed from `record_attached_alltime_composition/PROPOSAL.md`, pin `7b618a13d8094d0535ca399025ca872b54b8fdb2c9a307a0b31f521306c18e73`; none of its old temporal constants is imported.

This was an analytical check of the changed argument and its interface definitions, with exact hash checks. No scientific execution, numerical dynamics, sweep, solver, original calibration revalidation, W/Git/PR/checkpoint/prompt/model edit or delegation occurred. Exact coefficients, shared B/vacuum K identification, preparation and native physical interpretation remain supplied premises. Source identity and prior checks do not replace those premises.
