# Same-carrier slow output lead: exact scalar interface candidate

Status: root-authored new candidate, not independently checked and not an attached-device theorem. This changes the output Hamiltonian and requires new actual feedback, spectral mass, phase and temporal checks. It is finite storage by slow propagation, not irreversible capture, a permanent latch or reset.

## Exact local positive realization

Take .0027<j<.003 and 0<g<j. Keep the old lead/gate output site's one-head diagonal 2j. Replace its outgoing hopping -j by -tau, tau=sqrt(jg), then use a semi-infinite lead with hopping -g and diagonal 2j on every new site. The entire shared internal operator B is unchanged at these sites.

Use the usual PSD exchange Q(-tau), Q(-g). At the old port add positive occupation (j-tau)n to compensate its changed bond diagonal. At the first slow site add (2j-tau-g)n; at every later slow site add 2(j-g)n. All coefficients are nonnegative because tau<j and g<j. Thus this same-carrier modification needs no new vacancy scalar. These are ordinary two-body exchange plus one-body positive occupations, on a straight installed path. Large onsite diagonal 2j remains; it is not a smaller full-Hamiltonian norm claim. The reference one-head Hamiltonian is bounded even on an infinite path. This does not assert a bounded infinite many-head operator.

## Scalar scattering in a common open channel

Let delta be energy relative to B-eigenvalue+2j. Define q,k in (0,pi) by

    delta=-2j cos q=-2g cos k,
    w=exp(iq), v=exp(ik).

The old half-line occupies n<=0. Write psi_n=w^n+r w^-n there; the slow sites m>=0 have psi_m=t v^m. The two boundary equations are

    tau t=j(w+r w^-1),
    t=(tau/g)v(1+r).

Their exact solution is

    r=(w-v)/(v-w^-1)
      =w sin((q-k)/2)/sin((q+k)/2),
    t=sqrt(j/g) v(1+r).

The energy-normalized transmission is

    t_flux=sqrt(g sin k/(j sin q)) t.

Current conservation gives |r|²+|t_flux|²=1. At delta=0, q=k=pi/2, r=0 and t_flux=i. The physical coefficient t is larger than1 by sqrt(j/g); it must not be mistaken for a unit-flux coefficient or used with the old momentum Jacobian.

For the concrete candidate g=10^-6 and |delta|<=d<2.4e-8, both channels are open and |delta|/(2g)<.012. Since asin has derivative at most1/sqrt(1-.012²),

    |q-k| <= |delta|/(2g sqrt(1-.012²)).

Furthermore |q-pi/2|+|k-pi/2|<.01201. Hence the reflection formula gives the conservative linear bound

    |r(delta)| < .251 |delta|/g  for delta!=0,
    r(0)=0,
    |r|<.0061 throughout the stated band.

A non-strict linear inequality includes delta=0; no positive false floor or strict zero inequality is inferred.

For orientation ONLY, the existing unnormalized scalar reference in the main j lead has moment integral u² |F|²dq<1.9e-17, u=|q-pi/2|. Since |delta|<=2j u and j<.003, its reflected REFERENCE coefficient has L2 norm at most

    (.251/g)*.006*sqrt(1.9e-17)<6.6e-6.

This is a single interface, reference-only estimate. It is not the reflection or mass bound for the full apparatus after attachment; recurrent coherent feedback is an explicit remaining obligation.

## Conditional finite length implication

Suppose the full modified infinite device is independently shown to meet an appropriate complete or successful-map theorem through a horizon 2T. Retain M slow sites and use a positive terminal cap g n_(M-1), exactly compressing the final cut. Set the finite-transfer weight to zero on all upstream sites INCLUDING the first slow site m=0, and f(m)=m on the slow lead. The strong connector tau then has zero weight difference. Only slow edges contribute, with imaginary-part row bound2g sinh(1). The existing checked weighted single-cut theorem yields

    full finite/infinite error
       <=1.2 exp[-M+4gT sinh(1)], 0<=t<=2T.

For the merely illustrative values T=10^15 and M=5*10^9, this is below1.2 exp(-2*10^8)<10^-6. The original gate port is upstream, and the M slow sites are additional; adapting the prior exact inventory gives M+236 heads and M+241 physical qubits, not M+240. Block counts must be rederived because of the added positive occupations. No claim is made that the old runtime or error theorem already applies to this changed infinite device. No equal-quality resource ratio is established.

## Decisive next calculation

At the old port the new outgoing load is -j v instead of -j w. Its difference is -j(v-w), which changes the actual gate inverse and every upstream load. Recompute the full record-sector gate response, return to the input reference plane, emitter density and common outgoing phase with the slow momentum and its group velocity. The scalar interface being matched at one energy is not enough. All closed B channels and their new roots must be paid, as must hard-band spectral mass and wrong-window input columns.

A useful first check is whether the changed gate inverse remains uniformly invertible on the complete common energy band using the previously checked26/j inverse and this rank-one load perturbation. Only then attempt actual full-device estimates. Preserve the literal old K/W and complete apparatus output; do not replace omitted modes with an unproved impedance-matching assertion.

Sources: attached kernel fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457; gate inverse3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82 and checkcebb4153f1f1f75001614110ad7597fcf5b835ddad2ab15e0d57c1e089f0f67f; scalar reference moment from corrected outgoing52bd25106f95d06b1d06b741f1183a492d169e5a4c6e85aa40ebca88404d1788 and its check44c697a5169b5cdb665e44c8b62787c2164f72537e082523e492ad535a29f026; published weighted finite-transfer note735ec540842018f17ecde72b43d102f52dd76f9df65682eaaeec64498628c429. These arguments were read in the coherent current task; none was rerun. This new interface derivation and its illustrative application require a distinct check. No new physical axiom, native supplier, measurement, numerical sweep or time-dependent switch is introduced.
