# VERDICT: CONFIRMED WITH CORRECTIONS

All four worker scripts reproduce their stored outputs exactly.  The canonical
Snyder coset composition fails the local additive-soft-charge condition on a
generic equal-mass elastic channel, so the second FIXED FAIL disjunct is met
under a standard Lorentz-invariant, unitary massless-helicity-2 S-matrix with
the stated leg-local pole and Ward-residue assumptions.  The report must not
promote this to an unconditional no-go for every Snyder-type gravity.

Independent checks are in `R2-6_referee_checks.py`.  In particular, at a
generic equal-mass pair the deformed total and ordinary sum both have rank four,
but the two singular values of `d(sum)` restricted to the two-dimensional
kernel of `d(oplus)` are 0.002574 and 0.002506.  Thus the additive sum does not
factor through the Snyder total even locally.  The same script independently
finds the leading noncommutativity coefficient 0.49999999, an identical-mass
symmetrised associator tending to `0.2691 a^2`, a true binary-left-fold
soccer-ball exponent 1.514 with coefficient 0.0564, and the exact-mass
MICROSCOPE large-`aM` value 0.286822.

## 1. Spectrum, covariance, and the sharp point

- `x_i=a J_i4` is a compact-circle generator, while `t=a J_04` is a
  noncompact boost generator (`R2-6_report.md:94-97`).  In the usual scalar
  Snyder realization this gives the integer lattice and continuous time; a
  genuinely spinorial `Spin(4,1)` sector has half-integer compact weights.
  Compactness by itself, however,
  proves only that a representation's spectrum is contained in the relevant
  integer/half-integer lattice; it does not prove that every unitary
  representation contains every lattice value.  The worker's finite `SO(4)`
  examples themselves contain only finite subsets (`r26_spectrum.out:2-10`).
  Thus the unqualified equality in `R2-6_report.md:95-97` needs a stated
  representation.
- The moving-observer claim is correct.  Every spacelike unit `n` is Lorentz
  conjugate to a rest-frame spatial axis, so unitary conjugacy preserves the
  spectrum and there is no contracted step.  The numerical conjugacy and
  high-precision periodicity checks are at `r26_spectrum.out:13-19` and the
  interpretation at `R2-6_report.md:102-106`.
- The algebraic joint-eigenvalue argument is correct: a joint eigenvector
  forces the rotation generators to annihilate it, covariance forces its
  eigenvalue vector to be zero, and it is then `SO(4)`-fixed
  (`R2-6_report.md:108-112`).  `(SO_0(4,1),SO(4))` is the rank-one Riemannian
  symmetric/Gelfand pair, so an irreducible unitary representation has at most
  one such vector.  This is **at most one**, not existence in every irrep and
  not uniqueness in an arbitrary reducible representation.  The safe claim is
  "the only possible joint eigenvalue is the origin, with multiplicity at most
  one per irrep," not "each observer has exactly one sharp state"
  (`R2-6_report.md:112-114`).  The conclusion that Snyder supplies no spatial
  grid of joint sharp points still follows.

## 2. Dispersion, composition, and uniqueness

- The free worldline ratio is undeformed in the stated Snyder realization
  (`r26_composition.py:303-316`; `r26_composition.out:63-65`).  A selected
  Lorentz-invariant mass-shell branch has no dimension-5 or dimension-6 LIV
  term, so the tree-level LHAASO statement is correct
  (`R2-6_report.md:116-122`).  The loop sentence is correctly only SUGGESTED.
- The coset code implements the transvection product and reproduces covariance,
  noncommutativity, nonassociativity, and the BCH remainder
  (`r26_composition_lib.py:41-81`; `r26_composition.out:1-17`).  A distinct
  numerical sample gives the `1/2` coefficient (`R2-6_referee_checks.py:112-121`).
  The quoted `0.56 a^2` is the coefficient for the worker's particular three
  momenta, not a universal constant (`r26_composition.out:10-15`).
- The centralizer argument supports local uniqueness of the
  proper-orthochronous-Lorentz-equivariant transvection section: at a timelike
  label an equivariant `h(k)` must commute with `SO(3)`, whose centralizer in
  `SO_0(3,1)` is trivial (`R2-6_report.md:77-83`).  Lorentz-equivariant chart
  changes are locally radial, `p=f(k^2)k`.  This does not establish a unique
  global composition over all de Sitter patches or uniqueness among the
  generalized/extended Snyder realizations that the report expressly excludes
  (`R2-6_report.md:85-90`).

## 3. Soccer ball and MICROSCOPE

- For mapping A, the soft-kick factors `aM/sinh(aM)` and `aM coth(aM)` are
  correct (`r26_composition.py:165-176`; `r26_composition.out:24-32`).  With the
  published SUEP masses 0.401706 kg and 0.300939 kg, the large-`aM` right-order
  limit is `eta=0.286822`; the report's 0.28645 uses rounded masses and is
  harmless (`r26_numbers.py:35-56`; `r26_numbers.out:8-16`).  The left ordering
  suppresses both accelerations exponentially.  These are conditional
  gravitational predictions: in addition to "one Snyder particle," they need
  a universal external impulse proportional to gravitational mass and a chosen
  ordering, neither of which Snyder kinematics alone supplies
  (`R2-6_report.md:142-154`).
- Mapping B's correction magnitudes are arithmetically right:
  `(a m_N)^2/6=9.86e-40` and the Ti/Pt nucleus-granularity difference is
  `3.47e-35` (`r26_numbers.out:18-24`).  At nucleon granularity the leading
  common nucleon factor largely cancels between bodies, so `1e-39` is a
  conservative correction scale, not a derived Ti/Pt Eotvos ratio.  Mapping B
  remains a proposed local rule, not a demonstrated Snyder QFT; the report
  acknowledges that open bridge at `R2-6_report.md:166-175`.
- `R2-6_report.md:168` incorrectly says a rigid body's constituent momenta are
  collinear; bound matter has internal/Fermi momenta, as the report's own next
  calculation assumes (`R2-6_report.md:156-164`).  Mapping B avoids the problem
  only by declaring the composite `oplus`-total nonphysical.
- The worker's "sequential" routine multiplies all representatives and projects
  only once (`r26_composition.py:192-196`); it is not a left fold of the
  nonassociative binary operation.  A true left fold is implemented at
  `R2-6_referee_checks.py:48-52` and still fits approximately `N^1.5`, but with
  coefficient 0.056 rather than 0.115 in this sample
  (`R2-6_referee_checks.py:88-104`).  Thus the qualitative soccer-ball warning
  survives, while the quoted threshold and "every bracketing" assertion are
  not established by the supplied runner.

## 4. Lemma W-S

- **Step 1.** For a scalar external leg, Lorentz covariance of the vertex and
  the soft pole gives `Q^mu=kappa(m) k^mu`; a radial chart change preserves the
  direction (`R2-6_report.md:186-189`).  For spinning legs the displayed
  `A kk+B eta` ansatz is not the general Lorentz tensor.  The same leading
  eikonal conclusion is standard only after adding the usual diagonal
  leading-pole/Weinberg soft-factor argument; it does not follow from S1 alone.
- **Step 2.** The level-set argument is correct **locally at regular points**, but
  its logical direction should be stated carefully.  Ward decoupling gives
  `ker dF subset ker dL`, where `F(k,q)=k oplus q` and
  `L=kappa_1 k+kappa_2 q`.  If both maps have rank four, their two-dimensional
  kernels coincide, so locally `L=ell(F)`; invertibility of `d ell` then gives
  `F=H(L)`.  It does not by itself prove global equality of all level sets.
  Lorentz covariance then makes `H(w)=h(w^2)w`, yielding the constant `A/B`
  criterion (`R2-6_report.md:191-196`).  The independent equal-mass Jacobian
  test at `R2-6_referee_checks.py:55-77` directly finds the required kernel
  inclusion false for Snyder.
- **Step 3.** Consequently the canonical Snyder law cannot carry a nonzero
  leg-local additive Lorentz-vector soft charge on a generic equal-mass elastic
  channel.  The worker's conservation-surface and perpendicular-component
  checks reproduce (`r26_composition.out:48-61`), and the analytic
  noncommutativity is generic (`R2-6_report.md:135-140`).  The conclusion is
  `kappa=0` for species to which those channel and regularity assumptions
  apply—not an assumption-free statement about every conceivable Snyder
  gravity.
- **Step 4.** For a commutative law, ordinary exchange of the first and third
  identical outgoing legs maps `(k3 oplus k4) oplus k5` to
  `k3 oplus (k4 oplus k5)`.  Hence a fixed-bracketing support that is ordinarily
  permutation invariant and nonzero on an open set does force associativity
  there.  But ordinary, unbraided permutation support and a fixed-bracketing
  prescription are extra assumptions not explicit in S1-S5
  (`R2-6_report.md:204-209`).  Also, the worker's cited numerical test uses
  masses 1, 0.6, and 0.8 rather than identical particles
  (`r26_symmetrised.py:34-41`).  An actual equal-mass rerun still finds a
  nonzero associator approaching `0.2691 a^2`
  (`R2-6_referee_checks.py:79-86`), so the mathematical defect is real but the
  original runner did not test the stated premise.  Testing three guessed
  charts (`r26_symmetrised.py:42-52`) cannot by itself exclude every radial
  charge map.
- **S5.** Exact Lorentz covariance alone does not force gauge decoupling.  A
  unitary Lorentz-invariant S-matrix containing a genuine massless helicity-2
  Wigner particle does: Lorentz transformations shift covariant polarization
  representatives by pure-gauge terms, whose S-matrix contribution must
  vanish.  Thus S5 is justified only together with the standard asymptotic
  S-matrix, locality/unitarity, and helicity assumptions; in a
  noncoassociative theory lacking such an S-matrix it remains a substantive
  hypothesis (`R2-6_report.md:179-185,221-225`).
- **General form.** A Ward identity requires an additive Lorentz-vector charge
  on the physical conservation support.  It forces the full binary law to be
  commutative and associative only when that charge is locally full-rank/
  injective, the same binary law is iterated, and ordinary permutation and
  bracketing assumptions hold.  The unqualified sentence at
  `R2-6_report.md:211` is too broad.  If a group-valued law really obeys
  `Q(g1 g2)=Q(g1)+Q(g2)` on the group, then the factorization through
  `G/[G,G]` is correct; connected simple `SO_0(4,1)` has no nonzero continuous
  homomorphism to `(R^4,+)`, while `AN(3)` has one-dimensional abelianization
  (`R2-6_report.md:212-214`).  Extending an on-shell Ward identity to a global
  group homomorphism is an additional richness assumption.

## 5. Boost wall and finite fibre

- The boost-wall conclusion is correct.  Snyder momenta transform under the
  undeformed Lorentz algebra, mass-shell momentum is unbounded, and the de
  Sitter momentum manifold is not a Brillouin torus, so the bounded-sector and
  torus hypotheses of the B1 obstructions fail (`R2-6_report.md:227-237`;
  `C4_B1_referee.md:7-15`).  This does not construct the open gravitational
  hypersurface-deformation algebra (`R2-6_report.md:239`).
- Snyder itself supplies no `Z^3` set of joint sharp sites, so it cannot realize
  the Lattice and per-site Qubit axioms as written
  (`MINIMAL_AXIOMS_2026-06-29.md:35-53`; `R2-6_report.md:243-254`).  Nontrivial
  unitary representations of connected noncompact simple `SO_0(4,1)` are
  infinite-dimensional.  An `M_2(C)` internal tensor factor can still be added
  per particle, as the report says; what is excluded is its interpretation as
  the finite fibre of Snyder-provided spatial sites.

## 6. FIXED verdict

`TESTS.md:2626-2629` makes FAIL disjunctive.  Mapping A is only a conditional
macroscopic rule and mapping B remains unconstructed as a full QFT, so neither
alone settles the probe.  The second disjunct is nevertheless met in the
bounded canonical setting: the Battisti-Meljanac/coset conservation law cannot
support a nonzero exact leg-local additive soft-graviton charge on generic
regular elastic channels under S1-S4 plus the standard massless-helicity-2
S-matrix content of S5.  The symmetrised 2-to-3 extension and the global
"every conservation law" language require the corrections above and are not
needed for that bounded FAIL.

## Strongest correct statement

For the canonical four-momentum Snyder transvection product on de Sitter
momentum space, and assuming a standard unitary Lorentz-invariant S-matrix with
a genuine massless helicity-2 particle, nonzero hard amplitudes on generic
regular deformed-conservation surfaces, leg-local soft poles, and the exact
Ward-residue identity, Lorentz covariance makes each leading scalar-leg soft
charge a mass-dependent multiple of its momentum, while the rank-four Ward
condition requires the Snyder total locally to factor through that additive
charge; the explicit order-`a^2` law and an independent fiber-Jacobian test show
that it does not, so the coupling must vanish on such channels and R2-6 is
**FAIL (bounded)** under the FIXED second disjunct.  Snyder still has
  representation-dependent spectra contained in the integer or half-integer
  compact-weight lattice for each spatial coordinate, continuous time in the
  standard representation, no lattice of
joint sharp points, exact tree-level Lorentz dispersion, and no B1 boost wall;
the result does not exclude braided/non-leg-local soft structures, linear
vertex conservation, nonstandard theories without the usual S-matrix, massive
or nonparticle gravity, or extended momentum spaces with a suitable abelian
quotient.
