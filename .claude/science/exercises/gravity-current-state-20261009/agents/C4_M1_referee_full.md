# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed RM reading is met: the isolated-composite-band result is a valid
bounded obstruction in the standard first-moment setting, and that result
alone is enough for the registered FAIL at `TESTS.md:1470-1473`. T2 is also a
sound stronger obstruction after tightening its operator/domain and locality
hypotheses. T3 is a valid conditional index argument, not an unconditional
many-body theorem. Several scope statements and one numerical interpretation
need correction, but none reverses the bounded FAIL.

## 1. T1: isolated-band lemma

**Confirmed, with operator-domain and partial-band qualifications.**

- If “conserved P” means strong commutation with H (equivalently, covariance
  under the H evolution; bounded P with a valid operator commutator also
  suffices), then P commutes with every spectral projector of H. A formal
  equality `[H,P]=0` on an unspecified common core alone does not imply this.
  Thus the step at `M1_report.md:49-51` is correct under the strong/domain-valid
  reading of exact closure, but that reading should be stated.
- For a scalar isolated eigenband, translation covariance fixes the principal
  part of the compressed boost to
  `1/2 {i partial_Q, E}`. Multiplication/Berry-connection terms commute with E.
  Consequently `Pi P_c Pi = partial_c(E^2/2)`, and strong commutation removes
  the cross-projector pieces in the compressed second bracket. Hence
  `Pi i[K_b,P_c] Pi = -E partial_b partial_c(E^2/2)`, exactly as claimed at
  `M1_report.md:45-52`. A Chern-twisted frame changes only the local
  connection; the scalar energy and its Hessian are global, so it supplies no
  escape (`M1_report.md:54-56`).
- Periodicity gives `integral_T Hess(E^2/2)=0` distributionally and therefore
  mean anomaly `-beta I`. Lipschitz regularity is enough for this sum rule. It
  is enough for the bracket only after the commutator is explicitly understood
  as a weak/form identity; the report does not supply that functional-analytic
  definition. A safe theorem statement assumes `u=E^2/2` is `W^{2,1}` (or C2),
  or states the closure identity in distributions and verifies the domains.
- An integrated positive-energy Poincare representation cannot have a mass
  shell that simply terminates when an isolated bound level reaches a
  continuum. It can, however, continue as an embedded stable state or into
  another branch. Thus `M1_report.md:63` and `M1_report.md:106` exclude a
  genuinely terminating partial particle band, not every loss of spectral
  isolation. The numerical d=3 example does not by itself exclude an embedded
  continuation.

## 2. T2: bounded-sector theorem

**The abstract theorem and exponential contradiction are correct; the claimed
microscopic class needs a sharper definition.**

- With the vacuum energy consistently set to zero,
  `P=i[H,K]` gives `i[K,H]=-P`. Together with
  `i[K,P]=-beta H`, this yields
  `i[K,A_+]=-sqrt(beta) A_+` and
  `i[K,A_-]=+sqrt(beta) A_-` for
  `A_+=H+P/sqrt(beta)` and `A_-=H-P/sqrt(beta)`. The signs at
  `M1_report.md:123-127` are correct.
- On a fixed-N hard-core/qubit sector, a uniformly bounded finite-range energy
  density that preserves N term by term, after its local vacuum scalar is
  subtracted, has only O(N) non-vacuum terms. H is therefore bounded there.
  Its finite-range energy current is also a sum of O(N) bounded local terms, so
  P is bounded. Mere global number conservation is not sufficient: the chosen
  density and every boost improvement must preserve N, and the current must
  retain the stated finite-range/decay bound. This is the needed correction to
  the broad wording at `M1_report.md:129-134`.
- For that finite-range class, the Nelson step can be completed. On the
  finite-configuration core, K has finite propagation and matrix elements
  growing at most linearly in the particle coordinates. With comparison
  operator `N0=1+sum_i |X_i|^2`, one obtains the required K-versus-N0 bound and
  the Nelson commutator form bound; hence K is essentially self-adjoint. Since
  finite-range H and P preserve the core, the bounded commutator identities
  extend in graph norm and integrate to
  `exp(i eta K) A_+ exp(-i eta K)=exp(-sqrt(beta) eta) A_+` and the
  corresponding formula with both signs reversed for `A_-`.
  The report states but does not show these two Nelson estimates
  (`M1_report.md:125-126`); they depend on the finite-range/uniform-degree
  hypotheses just stated.
- Unitary conjugation preserves norm, whereas the right side scales
  exponentially for nonzero real eta. Thus both bounded operators A+ and A-
  vanish, and H=P=0. This does not prove too much: a continuum free field on a
  finite-particle sector has unbounded H and P because continuum momentum is
  unbounded, so T2 does not apply. Nor does it apply when K mixes N sectors or
  when an unbounded internal local mode is present.
- The fibre rerun reproduces `sup ||H|| = 5.83,5.94,5.98,5.99` and
  `sup ||P|| = 3.95,4.23,4.35,4.39` (`m1_fibre_bracket.out:32-36`). The printed
  analytic bound 7.0 is a bound for H only (`m1_fibre_bracket.py:63-70`), not a
  proved 7.0 bound for P. P is bounded here by the separate finite-range
  argument.

## 3. T3: conditional one-dimensional index theorem

**Confirmed as a conditional theorem, with the scattering assumption made more
explicit.**

- The convention is internally consistent at `M1_report.md:238-244`. GNVW's
  multiplicative convention has identity 1 and qubit-shift index 2. RWW uses
  the additive logarithmic normalization, with identity 0 and shift index
  `log 2`. In either convention the index group is torsion-free: positive
  rationals have no multiplicative torsion, and their logarithms form a
  torsion-free additive subgroup. Thus `q ind(V)=0` does imply `ind(V)=0`.
- The passage from one-particle phases to `V^q=1` is valid only if all
  one-particle V spectrum consists of q-th roots for one common finite q, V
  acts covariantly on the asymptotic creation operators, and the corresponding
  in-states are complete. Under those assumptions, V acts on an n-particle
  in-state by the product of its one-particle phases, so V^q is the identity on
  a dense complete scattering space. The unique vacuum fixes its remaining
  scalar phase, and faithfulness of the spin-chain GNS representation then
  gives the identity automorphism.
- These requirements are stronger than ordinary lattice Haag-Ruelle
  construction. The report itself acknowledges that Haag-Ruelle must be built
  using the quasi-local continuous translations generated by P and that this
  convergence is assumed (`M1_report.md:230-246`). The cited lattice
  Haag-Ruelle paper constructs scattering for the native lattice translations;
  it does not establish this extra convergence or asymptotic completeness.
  Accordingly T3 is correctly useful only with those assumptions, and it does
  not cover irrational centres, massless sectors, failure of completeness, or
  d >= 2 (`M1_report.md:250-256`).

Primary convention checks: GNVW, arXiv:0910.3675; RWW,
arXiv:2012.00741; Bachmann-Dybalski-Naaijkens, arXiv:1412.2970.

## 4. Numerical and exact checks

**The verdict-bearing numbers reproduce.**

- All four supplied scripts were rerun. The periodic FFT/finite-difference
  sums give mean anomaly `-1.000000` for the isolated bands
  (`m1_twobody.out:9-44`, `m1_nbody1d.out:11-46`). This number is also an exact
  periodic telescoping identity, so it is not dependent on the eigenvalue
  solver.
- Independent adaptive quadrature plus implicit differentiation of the 1D KG
  Green-function equation gives `beta_b = 0.975851886, 0.864721731,
  0.599312581, 0.368821504` for `U=-0.2,-0.5,-1,-1.5`, agreeing with
  `m1_twobody.out:9-32`.
- For the nearest-neighbour pair,
  `E_b(Q)=2(m+2t)-sqrt(U^2+16t^2 cos^2(Q/2))` gives exactly
  `A(pi)=-4/|U|` when `m=1,t=1/2,beta=1`, reproducing -16, -8, -4 and -2
  (`m1_nbody1d.out:11-22`).
- The XXZ closed form independently gives the printed maxima and bandwidths
  through n=4 and tends to `J sinh eta`; the finite-box diagonalization agrees
  at about `1e-14` (`m1_nbody1d.out:48-56`). The string family is bounded and
  flattens, so it is not the unbounded reciprocal-lattice tower.
- The two-particle fibre numbers and the interacting-current leakage reproduce
  (`m1_fibre_bracket.out:13-36`). They support the examples, while T2 supplies
  the general finite-N obstruction.
- The Pauli-string output reproduces exact C1 for XX/XXZ and symmetric TFIM and
  a nonzero longer-range C3 residual (`m1_integrable_boost.out:8-34`). However,
  the quoted `0.71-0.83` residual ratios are obtained by an unconstrained least
  squares fit (`m1_integrable_boost.py:69-79`), and every printed fitted beta is
  negative (`m1_integrable_boost.out:10,14,18,22,29,33`) whereas T2/C3 require
  `beta>0`. For beta positive the residual is at least the norm of
  `i[K,P]`; at beta=1 the rerun ratios are 2.236, 1.826, 1.528, 1.291, 1.275 and
  1.517. Thus the integrable models fail more strongly than the report's table
  suggests. Also, once `[H,P]=0`, conservation of `i[K,P]` follows directly
  from Jacobi, so the zero at `m1_integrable_boost.out:39-43` is not an
  independent integrability test, though the longer range is consistent with
  the higher-charge interpretation.

## 5. Fixed-reading disposition

The registered FAIL asks for a proof or check that composite bands obey the
sum rule with averaged anomaly `-beta`, or an equivalent obstruction, for the
stated classes (`TESTS.md:1470-1473`). T1 supplies exactly that for globally
isolated positive-energy composite eigenbands under strong conserved-current,
first-moment closure; the explicit two-, three-, and four-body and XXZ examples
check it. T2 validly enlarges the excluded class to canonical finite-range,
termwise-number-conserving empty-vacuum models on fixed finite-N sectors. T3 is
additional conditional one-dimensional support and is not needed for the
fixed FAIL. Therefore **FAIL (bounded) is correct**.

**Strongest correct statement.** Under a first-moment boost with domain-valid strong conservation of the energy current, every globally isolated positive-energy scalar composite band on the Brillouin torus has compressed current `grad(E^2/2)`; exact C3 closure would require `Hess(E^2/2)=beta I`, while torus periodicity forces the band-and-zone averaged anomaly to be exactly `-beta I`, so no such band closes for `beta>0`, independently of binding, spatial size, internal fibre dimension, or Chern twisting. Moreover, for a uniformly finite-range bounded energy density that preserves an empty-vacuum occupation number term by term, with finite-range N-preserving boost improvements, H and P are bounded and the first-moment K is essentially self-adjoint on every fixed finite-N sector; exact closure then forces that sector to be trivial. In 1D an additional index contradiction follows only under a common rational denominator for all tower centres, the required quasi-local continuous-translation scattering covariance, a unique gapped vacuum, and asymptotic completeness. These results do not exclude non-first-moment generators, non-number-conserving embedded/touching sectors in d >= 2, irrational centres, massless sectors, or unbounded continuum finite-N sectors.
