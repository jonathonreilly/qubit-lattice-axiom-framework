# Perturbed installed source: raw traveling comparison to a fixed nominal packet

ROOT authored conditional interface, requiring distinct checking. No numerical tolerance or complete-device performance point is selected. The actual perturbed attachment interface remains provisional until its separate check is complete.

## Domain and dependencies

Retain literal K, W, B, shared source, c_att, calibration, port/reference planes, full background matching, real sector bases and all-input/passive-reference conventions of nominal outgoing source af580b44fc2ebfc35eb014ffc63b8bae17464150677ede4a8b8315886f6f36ac, checked721a183db3e42527d7cb5bdda697e6c6d81312a94cf047dd7ea15897cb4c2f02. Use the perturbed installed construction f32b28aba669d09933c9c22052b2abce4d68339f43faa5beac8f3dc4d8ee978d, with real positive a1,a2,kappa and identity detunings di. Its chi<1 and FULL Theta_eps<1 criteria, including the complementary inverse170, are explicit premises. Scalar isolated normalization and complex ratio L are from32456b0b5c99ad1acfcdc9a770d022ffcc14069dee157981c715177cfa6a7eb6, qualified byba06cef2ddf0aae45eeaf5f5c8740258babe21d2a8206fbf6c1eb7b3b33f97ad. No old one-source runtime is imported.

Use the same fixed lambda,j,g,h,d=2j sin h, two physical windows and nominal comparator as these sources. Source detunings are not old-input-dependent and do not alter the common carrier or background; they remain inside the perturbed determinant. Define D=(E-c_att-2j)I-B, Ai=D-diI, Pe= A0 A1-a1^2 I,

 Qe=Pe(A2-kappa^2 G)-a2^2 A0,
 Qref=Pe(A2-kappa^2 m_j(D))-a2^2 A0,
 Ke=kappa^2 Qref^-1 Pe(G-m_j(D)).

The exact order is Qe=Qref(I-Ke). On the selected input P, Qref^-1 P=P/qe(delta). On C it has norm<170. Both lips have their own ordered factorization. In the following theta_e(delta) and Theta_e are the explicit bounds from the perturbed attachment, not nominal Theta3.

## Actual outgoing versus its perturbed scalar comparator

The unchanged preconnector row Ltilde_x obeys j||Ltilde_x+(x omega rho_att w^21/j)P||<=eN=2.1e-13+304u+.302|delta|/g, ||Ltilde_x||<461 and ||Ltilde_x C||<2e-23. Principal source compression preserves this actual row exactly. Therefore

 Aactual_x=-kappa*a1*a2*Ltilde_x*Qe^-1,
 Ae=kappa*a1*a2*rho_att*w^21/(j*qe(delta)).

Expanding (I-Ke)^-1-I to the LEFT of Qref^-1, without commuting G, gives

 ||Aactual_x P-x omega Ae P||/|Ae|
      <=eN+1.384*theta_e(delta)/(1-Theta_e).

The coefficient1.384 is the unchanged j*461 ceiling; it does not come from source ratios. The true scalar outgoing coefficient has exactly the original propagation and connector phase, with a1a2*kappa/qe replacing the nominal numerator/denominator. It is

 Fe_s=t_f sqrt(dq/dk) * i E'_q Ae/sqrt(2pi).

The same physical t_L dq/dk identity fixes the Jacobian and first slow-site reference. Denote its transmitted mass by pe. The normalized isolated perturbed scalar measure rho_e gives 0<pe<=1 and exact second centered moment

 m2_e=d0^2+a1^2 <=lambda^2[epsilon^2+(1+epsilon)/3].

This follows by the first application of the centered scalar Hamiltonian to the seed; the mean is d0 and is NOT silently recentered. The exact full finite-band measure, not an actual loaded measure, supplies this comparison moment.

Minkowski and flux contraction now give the RAW selected allowance

 Esel_e=2.1e-13 sqrt(pe)
       +[304/(2j cos h)+.302/g]*sqrt(m2_e)
       +1.384 Theta_e sqrt(pe)/(1-Theta_e).

A theta-weighted integral could sharpen the last term, but no such improvement is used. In particular one can replace sqrt(pe) by1 for a fully explicit upper bound.

For wrong-window input the reference inverse remains in C before the left Neumann correction. Thus

 Bwrong_e=170*kappa*a1*a2*[2e-23+461 Theta_e/(1-Theta_e)],
 Ewrong_e=.006*Bwrong_e*sqrt(2h),
 Eraw_e=sqrt(2)*Esel_e+Ewrong_e.

This retains every internal output, both physical windows and all opposite prepared inputs. Orthogonal parity and record-X sectors combine by maximum, while old-energy input aggregation is bounded by sqrt(2). The ideal selected recombination maps record0 torecord1 with literal W. No spectral normalization is added to Eraw_e.

## Fixed nominal common packet and both traveling waves

Let F0_s be the exact NOMINAL hard-band transmitted scalar coefficient at the same lambda,j,g,h, with p0=||F0_s||^2. The scalar robustness theorem, including its common contractive transmission factor and exact change of variable, yields the pointwise relative ratio estimate and hence

 ||Fe_s-F0_s|| <= L sqrt(p0).

This includes the fixed common old propagation phase and the full complex denominator. No phase is fitted, and the nominal target is not retuned to the perturbed apparatus. Detunings are scalar identity, so all old-energy windows use the same perturbed scalar function after extracting their actual carriers. The perturbed input is still the same product state V in the same coordinate Hilbert space.

All coefficients and source detunings are real in the qualified sector bases. The real two-lip Stone argument of75b1ba68fae3f34e54c15df80b3a39a165240b1759f8fc84eb2b24677cc7f9e3 (checked9cb7655b688a61ce32b950f2d95024762023770380a6e5df8afaa1939744230a) therefore applies without changing its conjugation order. The ideal incoming has W* and conjugate Fe_s, retaining the SAME exp(-itE) physical time factor. Its coefficient error is also Eraw_e. This is conjugation of fixed matrix coefficients, not conjugation of an arbitrary old/reference input.

Both ideal perturbed traveling waves can be compared to their nominal counterparts at an additional cost L sqrt(p0) EACH. They share the physical ray, so the total traveling comparison to nominal raw outgoing PLUS nominal incoming costs

 2 Eraw_e + 2 L sqrt(p0).

Fourier isometry and restriction make this uniform in all real times. No dispersion difference is introduced because downstream j/g and the carrier are unchanged. A full-H norm multiplied by t is not used.

## Conditional complete synthesis contract, not a performance claim

Write beta0_t for the physical nominal raw outgoing packet, r0(t)=||beta0_t|| and alpha0_t for its raw incoming partner. Suppose separately proved represented-source and represented-background bounds for the perturbed actual operator are S_e(t) and B_e(t), and its one global actual omitted-state bound is eta_actual,e. At any t for which r0(t)>0, the preceding traveling estimate gives

 ||exp(-itH_e)V-Tnorm,0(t)||
 <=eta_actual,e+S_e(t)+B_e(t)+2 Eraw_e+2 L sqrt(p0)
                        +||alpha0_t||+1-r0(t).

Here Tnorm,0(t) is the FIXED nominal physical-halfline normalized common target with literal carrier exp(-ic_att t), old aging exp(-itK), W, record1 and source vacuum. Norm costs involve p0 and r0 only. There is no additional normalization of Fe_s, no pe normalization charge, and no renormalization/postselection of actual evolution. Nominal scalar time bounds may estimate alpha0 and r0 at their exact checked parameters; they are not an inherited actual source/core decay theorem.

For the same compatible finite receiver cap, the weighted single-cut comparison adds its independently derived finite/infinite allowance: all source changes lie in the zero-weight region. Actual source detunings do not make this a whole-operator stability theorem. The separately needed local/core bounds and inverse margins must hold at the perturbed parameters. No useful tolerance has been chosen or claimed in this file.

This construction preserves supplied source precision constraints: di must be controlled relative to lambda, and the positive port block and compensating occupations must preserve background exactly. Errors in arbitrary downstream calibration, source-dependent contacts, an added edge, a complex hopping, or a changed global scalar are outside the theorem. Native coefficient supply, autonomous irreversible halt/capture and reset/reuse remain open.

Exposure: ROOT derived this changed-source comparison after fully re-reading the nominal outgoing argument, full new perturbedattachment candidate and scalar robustness source. The actual inverse candidate is provisional; scalar prior review was ROOT's. Distinct checking must challenge row applicability, order, secondmoment/normalization, wrongwindows, real incoming identity and fixed nominal-target error bookkeeping. No numerical point, dynamics, spectrum, sweep, Git/PR/checkpoint/prompt/model mutation is claimed. Only this candidate file is new.
