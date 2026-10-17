# Actual three-source represented local amplitude

ROOT author candidate; distinct checking required. This concerns all three source heads in the ACTUAL installed device, projected to the two retained energy windows. It does not by itself give complete output or finite receiver performance.

Use the exact installed geometry in three_site_actual_attachment/PROPOSAL.md (4278633f3436008a770088331a2424d3f42dda06d08853dfe18d9b8a6554f006), qualified by its check ede902f9c1bebc768147e459894f98610689f33655f87d01d91d07531cbd157d. Use full ordered inverse three_site_loaded_inverse/PROPOSAL.md (7a154f66dd52ce70745e010641eaa98cffab8ededbeb9972139c3cbd10135672) and check8ddded69f6c5758650c166c8adbc3c05346478e81d4636b8bc5e226f365c9ca2. Scalar reference and exact moment are three_site_product_source/PROPOSAL.md (a89025dafcb588459e88c14fa802e9e9ce2e5184aa42d9d22f6521a1dadb4823), checked c161daea2f3a126ad84baaa63d975b5d80fd3243f11ca3b1075673f62530245b. All unchanged background matching, physical roots, nominal j, K/W/B, preparation and scalar conventions remain premises. No old one-site temporal estimate is imported.

## Domain and source-column subtraction

Adopt the checked inverse domain .0027<j<.003,0<lambda<=1e-8, a1=lambda/sqrt3,a2=lambda sqrt(8/3),kappa²=3jlambda, retained |delta|<=d=2j sin h, 0<h<=4e-6,0<g<=1e-6,d/g<=.5. Complementary D eigenvalues have modulus>=.185. Write r=lambda/j,s=sqrt(1-3r),v=delta²+lambda²,a0=8e-18,b0=46000/.0053+290/g, and

 Theta=(j a0+kappa²b0)/s+6kappa²(a0+b0d)<1.

Let R=S^-1 be the three-source Schur resolvent, R0 the reference with G0=m_j(D). Let e2 denote its last source injection and e0 its seed injection. The resolvent identity, with its actual multiplication order, gives

 (R-R0)e0 = kappa² (R0 e2)(G-G0) R20,
 R20=a1a2 Q^-1.

No scalar commutation of actual G is used. The reference last-source column is

 R0 e2 = (a1a2,-a2D,D²-a1²)^T Q0^-1.

For a scalar D eigenvalue x the squared numerator is EXACTLY

 (a1a2)²+a2²x²+(x²-a1²)²=(x²+lambda²)².

Thus on the selected channel its column norm is <=1/(s sqrt(v)); on closed channels it is <6, using |q0(x)|>.99|x|³ and |x|>=.185. Hence

 ||R0 e2|| <=1/(s sqrt(v))+6.                         (1)

For a selected prepared column P, the ordered factorization gives ||Q^-1P||<=1/[(1-Theta)s v^(3/2)]. For complementary input C it gives ||Q^-1C||<170/(1-Theta). Both statements hold separately on the two physical lips. In particular

 ||(R-R0)e0 P|| <= kappa²a1a2(a0+b0|delta|)/(1-Theta)
                         *[1/(s sqrt(v))+6]/[s v^(3/2)], (2)
 ||(R-R0)e0 C|| <=170 kappa²a1a2(a0+b0|delta|)/(1-Theta)
                         *[1/(s sqrt(v))+6].            (3)

These are joint Hilbert norms of ALL THREE source components, not a seed-return estimate. The complement includes wrong-window prepared old inputs; no full8 channel has been deleted.

## Integrated Stone errors without a time derivative

Full matching and the inverse supply continuous seed boundary values on neighborhoods of both closed windows, so the represented seed spectral measure there is absolutely continuous. Apply the Stone difference between actual and reference on each window. Its operator norm at any time is bounded by the sum of the upper/lower resolvent integrals divided by2pi. Both lips have the same majorants above. Extending only the nonnegative selected integrals to the full real delta line yields

 Dsel = kappa²a1a2/[pi(1-Theta)] *
    [a0*pi/(2s²lambda³)+b0/(s²lambda²)
                         +(6/s)(2a0/lambda²+2b0/lambda)]. (4)

Here the four integrals are int v^-2=pi/(2lambda³), int |delta|v^-2=1/lambda², int v^-3/2=2/lambda², and int |delta|v^-3/2=2/lambda. No energy derivative or Markov bath is introduced into actual matching.

For a complementary prepared column, the reference jump is zero on this window: all its reference channels are closed and their physical roots real. Integrating (3) only over [-d,d] gives

 Dwrong =170 kappa²a1a2/[pi(1-Theta)] *
  [(2a0/s)asinh(d/lambda)
   +(2b0/s)(sqrt(d²+lambda²)-lambda)+12a0d+6b0d²].       (5)

Each old-energy selected input has one corresponding window. Summing the two selected errors safely costs sqrt2 Dsel; summing both wrong-window errors costs at most2 Dwrong. Orthogonal parity and record-X sectors combine by maximum, not by their number. The initial record0 is a normalized coherent combination of these sectors. Passive references preserve all operator estimates.

## Reference local decay and one global omitted-state charge

Let Qsrc project to the three physical source heads, including all internal components. Let I be the common union of both actual physical windows and V the actual product preparation. Build the comparison direct sum of identical isolated scalar three-source chains over the exact B eigenvectors with the same c_att and old-energy carrier. On the prepared vacuum it has literal old aging. Its all-three-source amplitude norm is at most

 F(lambda*t)+Evec,
 F(x)=exp(-x)*sqrt((1+x+x²/3)²+(x+x²)²/3+2x^4/9), x>=0, (6)

where Evec=sqrt(E0²+E1²+E2²) is the explicit, checked finite-band-to-cubic reference error in three_site_product_source. It is essential to retain the intermediary-site amplitudes. One may use the checked looser F(x)<=9exp(-x/2), but that is often needlessly expensive.

The isolated scalar reference has the exact sixth moment mu6=3lambda^6+(8/3)jlambda^5. Removing its two energy windows costs at most

 eta_ref=min(1,sqrt(2mu6)/d³),                         (7)

uniformly on all prepared old inputs. This conservative common-union estimate retains both energy inputs and all scalar spectral types. It is a reference truncation cost, not an actual outside-state charge.

Combining (4)-(7) gives the actual REPRESENTED local-source bound

 ||Qsrc exp(-itH) E_H(I) V||
 <= F(lambda*t)+Evec+eta_ref+sqrt2 Dsel+2 Dwrong         (8)

for all t>=0. The scalar/time carrier is irrelevant only to this norm bound; it has not been discarded from the eventual common target. If a bound on the untruncated local projection alone is wanted, add eta_actual=||E_H(I^c)V||<=min(1,sqrt(2mu6)/d³). In a complete-output decomposition eta_actual must instead be charged globally ONCE across all apparatus outputs. Formula(8) intentionally omits that global charge.

This proves only an actual local-source escape allowance tending to the stated comparison floor, conditional on distinct verification. It does not yet bound finite-core/closed-tail amplitude, physical incoming wave, common normalized outgoing packet, finite-time receiver cut, success or native halt. Those are separate obligations. No operating point or faster complete device is asserted here.

## Exposure

ROOT authored the new subtraction/integrals and earlier inverse/attachment, with access to all scalar checks and outgoing proposal. A distinct reader must check the joint-column polynomial identity, noncommuting order, both-lip use, closed-input Stone term, comparison truncation and nonduplication of global omitted mass. No new numerical dynamics, sweep, calibration, Git/canonical edit, PR, prompt, axiom or model change is part of this artifact.
