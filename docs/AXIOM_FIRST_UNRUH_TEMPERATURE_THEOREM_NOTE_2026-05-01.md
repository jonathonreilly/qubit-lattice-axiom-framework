# Conditional KMS time-rescaling identity

**Date:** 2026-05-01; scope corrected 2026-10-24
**Type:** bounded_theorem
**Runner:** `scripts/axiom_first_unruh_temperature_check.py`
**Scope:** a supplied KMS state under a positive rescaling of its supplied automorphism group. The historical filename does not assert a framework derivation of the physical Unruh effect.

## Explicit mathematical premises and theorem

Let A be a C*-algebra, alpha_s a strongly continuous one-parameter group of *-automorphisms of A, omega a state, and beta0>0. Assume omega is beta0-KMS for alpha with the following convention: for every A,B in the algebra there exists F_AB bounded and continuous on the closed strip 0<=Im z<=beta0, analytic on its interior, with

```text
F_AB(t) = omega(A alpha_t(B)),
F_AB(t+i beta0) = omega(alpha_t(B) A),   t real.
```

For every a>0 define gamma_tau=alpha_(a tau). Then gamma is strongly continuous and omega is beta0/a-KMS for gamma.

**Proof.** The group law and continuity of gamma follow from those of alpha and continuity of tau -> a tau. Define G_AB(z)=F_AB(a z). Since a>0, multiplication by a maps the closed strip of height beta0/a onto the original closed strip, including its two oriented boundaries. Boundedness and continuity are inherited, and composition with the complex-linear map preserves interior analyticity. For every real t,

```text
G_AB(t) = omega(A gamma_t(B)),
G_AB(t+i beta0/a) = F_AB(a t+i beta0)
                 = omega(gamma_t(B) A).
```

These are exactly the KMS boundary conditions at beta0/a. This proves the conditional theorem. Positivity is essential to this strip-orientation argument; zero and negative a are outside the stated domain. The theorem does not construct omega or establish its initial KMS property. It does not assert a trace-class Gibbs density matrix for an arbitrary algebra.

## Supplied Rindler interpretation and units

One may specialize to beta0=2pi. To interpret alpha physically as boosts, additionally supply Minkowski geometry, a right-wedge observable algebra, a state identified as the chosen vacuum, its beta0=2pi KMS property, and the matching oriented dimensionless boost flow. None of these identifications follows from a scalar dispersion expansion or is established here as a framework consequence.

In natural units, the supplied coordinates t=xi sinh eta and x=xi cosh eta give ds²=-xi² d eta²+d xi²+dy²+dz². At fixed xi=1/a, proper time is tau=eta/a. Direct differentiation gives partial_eta=x partial_t+t partial_x and partial_tau=a partial_eta. Real rapidity eta is not periodic. Smooth single-cover Euclidean polar geometry has angular period2pi, but geometry alone does not establish the state's KMS analyticity or boundary condition.

Under the supplied physical interpretation, beta0=2pi gives beta_time=2pi/a and the formal natural-unit temperature a/(2pi). For acceleration a_SI>0 in SI units the boost rate is a_SI/c, so

```text
beta_time = 2pi c/a_SI                 (seconds),
beta_energy = beta_time/hbar          (inverse joules),
T = 1/(k_B beta_energy) = hbar a_SI/(2pi c k_B) (kelvin).
```

Using the runner's supplied constants, a_SI=c/(1ns) gives approximately0.001215662471207031K, not the historical200K. The Earth-gravity example is approximately4e-20K. These are evaluations of the supplied formula, not detector predictions or observations.

## Scope withdrawal and recovery

The previous U1–U4 framework-Unruh/Bisognano–Wichmann conclusions are withdrawn from this owner's current result. Physical vacuum selection, positive boost-generator attribution, a general wedge Gibbs density matrix, a modular-operator derivation and detector/Hawking/Hartle–Hawking conclusions are not established here. Their absence from this proof is not an impossibility result. No new physical primitive or framework axiom is registered.

The old Lorentz, KMS, Hawking and axiom references were historical attempted premises; none supplies the assumed state in the theorem above. Complete earlier source, runner and recorded outputs remain recoverable at commit `087c6fc4387ae8a97db91d8351e0d21a7d54ef9b` and the original9849 recovery. The unchanged parent and atomic/anomaly readers are outside this isolated correction.

## Verification limits

The primary preserves the earlier finite numerical predicates and thresholds: assigned2pi consistency, reciprocal/linear temperature arithmetic, SI scale and two equal assigned diagonal matrices. The latter is not a modular-operator test. Added exact rational checks exercise general beta0/a, oriented strip/boundary substitution and positive-domain rejection; SI checks exercise time/energy conversion and the1ns correction. Finite checks do not prove analyticity or the arbitrary-algebra theorem, whose proof is above. Any numerical failure remains a failure; no tolerance is relaxed. No current execution result is asserted until an actual source-bound capture is made.
