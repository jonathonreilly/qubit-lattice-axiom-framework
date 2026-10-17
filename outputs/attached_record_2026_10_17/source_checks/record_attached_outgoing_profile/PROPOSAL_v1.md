# Candidate outgoing record-sector profile for the frozen attachment

Status: root-authored derivation awaiting independent checking. This bounds a selected outgoing retarded coefficient, not a complete all-time herald map. Actual spectral synthesis, omitted mass, incoming physical halfline contribution and local/closed outputs remain separately required.

Use the frozen attachment fbc1315e/check7df39563 and attached endpoint2b2161aa/check30bb3f38. Retain their SAME v0 reference plane, selected projection P, source S_eff,s, B_eff,s, gate return r_s=w^36 r_gate,s and denominator d_s=1-S_eff,s r_s. Record sector s=±1. Let t_gate,s denote transmission from gate input p to final output origin o. On the selected real band u=|q-pi/2|<=4e-6,

 |t_gate,s-s rho_R|<=33u, |t_gate,s|<=1,
 rho_R=-i w^22, |d_s|>.99986,
 |1-d_s|<33u(1+8e-47),
 ||B_eff,s-P B_e||<2e-48.

The exact selected final-output response to endpoint forcing is the row

 L_att,s = w^18 t_gate,s d_s^(-1) B_eff,s.

This follows by solving b_P=d_s^(-1)B_eff,s f at v0 and transmitting that outward amplitude through eighteen free edges and the gate. No extra cable factor belongs in d_s: its return r_s already includes w^36. The gate is diagonal in B, so seven closed incident channels do not create an additional selected outgoing row at the gate itself. Their backreaction is already inside B_eff,s and S_eff,s. Noncommuting source matrices retain their order.

The inherited exact endpoint row satisfies

 PB_e=-(t_new/j)w^21 (1+R_new w^42)^(-1) P+E_L,
 ||E_L||<1e-23,
 |R_new|<r0=1e-20+12u,
 |t_new-rho_n omega|<1.76e-13+1e-20+181u.

rho_n is the original fixed common converter phase; omega is the literal W eigenvalue of this old/parity column, not a refitted phase. Define the new common phase

 rho_att=w^18 rho_R rho_n=-i w^40 rho_n,
 L_target,s=-(s rho_att omega/j)w^21 P.

The norm-one scalar chain has numerator t_gate,s t_new and denominator d_s(1+R_new w^42). The transmission comparison error is at most33u+(1.76e-13+1e-20+181u), using |t_new|<=1. The denominator differs from1 by at most33u(1+8e-47)+r0+33u(1+8e-47)r0. Its absolute value exceeds .99986*(1-r0)>.9998. Adding the j-weighted E_L and B_eff errors gives the conservative actual row bound

 j ||L_att,s-L_target,s|| < 1.8e-13+260u.           (A)

For arithmetic: the unrounded slope before dividing is259 plus a product bounded by .002u, and division by .9998 keeps it below260. The floor before division is1.7600002e-13 plus less than1e-25; it stays below1.8e-13. The tiny product floor is retained, not declared zero. The source's strict zero-displacement issue is avoided by using non-strict intermediate scalar inequalities and strict positive final slack.

Attach the emitter. In the full8 coordinate inverse, selected denominator D_s and complement inverse Dcc_s are as in the checked endpoint source. The selected retarded output coefficient for prepared selected emitter vector is

 A_s(q)=-kappa [ (L_att,s)_j + kappa² (L_att,s)_C Dcc_s^(-1)(G_att,s)_Cj ]/D_s.

The complementary row has norm <(1e-23+2e-48)/.99986<2e-23, since the original scalar PB_e approximation has no complementary columns. With ||Dcc_s^-1||<6 and ||G_Cj||<2e-24, the extra numerator after multiplying by j is less than 72j kappa²*1e-47, negligible but explicitly paid below.

Let Dref=E(q)-2j+(kappa²/j)w, and A_ref=kappa rho_att w^21/(j Dref), without omega or sector sign. The checked energy-resolved bound gives

 |D_s-Dref|/|Dref| <= j(8e-18+41000u)/sin q
                  <2.5e-20+123.01u = e_D(u).

The worst e_D is below.000493. Therefore division by1-e_D is legitimate. Combining(A), |omega|=1, and the retained complementary term yields

 |A_s/A_ref-s omega|
   < [1.8e-13+260u+e_D(u)+1e-60]/[1-e_D(u)]
   < 2e-13+400u.                                  (B)

The deliberately loose final400 slope exceeds(260+123.01)/.999507; the positive floor also has slack. kappa is the fixed1e-8 and .0027<j<.003. No other coupling family is asserted.

With Fourier/energy normalization F_s=i E'(q) A_s/sqrt(2pi) and F_ref,att=i E'(q)A_ref/sqrt(2pi), (B) is unchanged. This is the outgoing retarded coefficient convention from the canonical endpoint proof. Any use as an ACTUAL spectral density requires proving the two-lip synthesis for the new graph; a profile definition alone does not do that. Record0 initialization and record1 projection contribute the half-difference, so the selected outgoing record1 coefficient (F_+-F_-)/2 differs from omega F_ref,att by at most(2e-13+400u)|F_ref,att|. The common phase is -i w^40 rho_n; total physical scalar is c_att and full old aging must remain in the actual comparison.

Reference moments are unaffected by the new unit-modulus phase. Given the previously checked realband M2<1.9e-17 on halfwidth4e-6, the selected coefficient L2 error is <2e-13+400 sqrt(1.9e-17)<1.75e-6. This is a per selected old-energy column result, not an arbitrary-input matrix bound by a maximum: combine the two potentially overlapping error columns in each parity with sqrt2 (or prove sharper orthogonality); the two conserved parities are orthogonal. Thus a conservative outgoing coefficient complete-input ceiling is2.5e-6, conditional on that source moment bound and actual common-energy synthesis.

The incoming spectral term cannot be dropped. For a real Hamiltonian the opposite spectral lip supplies a conjugate incoming coefficient with comparable L2 size. Its physical restriction to the positive output ray at t>=0 needs a separate one-sided propagation/analytic estimate; raw Parseval gives no small bound for its reference part. Nor does(B) control local record rotation, all closed tails, finite-device recurrence, repeated measurement or normalized early success. Those are the outstanding completion obligations, not implicit consequences of transmission.

Author exposure: root read attached geometry/endpoint arguments and their distinct checks in full; this is new source-exposed author mathematics. No numerical execution or external source used for this derivation. No Git science branch, physical axioms, prompts or audit state changed. A distinct check should reconstruct(A), the exact row reference plane and(B), and verify reference M2 from the unchanged wider-band source before using the numerical L2 ceiling.
