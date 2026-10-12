# VERDICT: CONFIRMED WITH CORRECTIONS

The two mathematical lemmas survive adversarial checking.  The Lorentz-random
lattice (LRL) is also a valid stationary, simple, Poincare-invariant-in-law
point process with finite moments and a genuine Lorentz-invariant Bragg gap.
It therefore defeats the inference that spacelike Bartlett weight must occur
in an arbitrarily low-energy band.  The worker overreaches, however, in turning
that spectral counterexample into an unconditional all-orders propagation and
RZ pass.  The exact selection rule is established only for an ideal infinite,
defect-free, flat, deterministic periodic coupling and, in the stated
one-photon argument, for the 1-to-1 sector.  The report does not construct the
LR/RL steering law, its mean link kernel, finite-source transfer, inelastic
channels, curved extension, or a per-realization low-energy Lorentz test.

## 1. Theorem N-Q'

**Confirmed.**  With `psi=N(B)Omega`, covariance and vacuum invariance give
`F(t)=<psi,U(t)psi>`.  Its spectral measure is finite and supported on
`[0,infinity)` because `H>=0`.  Vacuum-level commutativity makes `F` real on a
dense set and hence everywhere by continuity.  Uniqueness of Fourier transforms
of finite measures then makes the measure reflection-symmetric, so its support
is `{0}`.  Thus every translated half-box gives the same count vector.

Repeated halving yields

`N(B)Omega = 2^n N(B_n)Omega`.

For a positive self-adjoint count with spectrum in the nonnegative integers,
functional calculus gives `N^2>=N`.  Therefore

`||N(B)Omega||^2 >= 2^n <Omega,N(B)Omega>`.

The left side is finite and independent of `n`, so the expectation is zero;
positivity and `Omega in D(N)` then imply `N(B)Omega=0`.  Each hypothesis has a
load-bearing role: semibounded energy gives one-sided spectral support;
covariance identifies the correlator and translates; vacuum commutativity makes
it real; halving additivity supplies the `2^n`; integrality supplies `N^2>=N`;
and the finite second moment prevents the left side from being infinite.

The projection identity is also correct:

`(P+Q)(P+Q-1)(P+Q-2)=PQP+QPQ-PQ-QP`.

If `spec(P+Q)` is contained in `{0,1,2}`, compression by `P` gives
`(PQP)^2=PQP`; hence
`(QP-PQP)^*(QP-PQP)=PQP-(PQP)^2=0`, and taking adjoints gives `PQ=QP`.
The exact independent check is in `referee_checks.out:1-4`.

**Correction.**  The `2P,2Q` example proves only that integer spectra of two
non-simple counts and their sum do not force commutativity when fine-scale
simplicity is removed.  It is not a covariant positive-energy counterexample to
N-Q', and it does not show that the full no-go fails without N5.  The worker
actually states this limitation at `R2-2_report.md:108-111`; it should not be
summarized as a counterexample to the theorem.

## 2. Theorem P-L' (needle theorem)

**Confirmed, with the stated stationarity and finite-local-second-moment
scope.**  An integer-valued count of mean `m` has
`Var X >= frac(m)(1-frac(m))`.  Choosing a length-`T`, width-`w` needle with
`T w^d=1/(2 rho)` therefore gives variance at least `1/4` for every `T`.

If the Bartlett spectrum away from zero were confined to
`|q_parallel|>=c|q_perp|`, the rectangular-window transform and a
translation-boundedness estimate split the variance into: a shrinking ball
whose mass tends to zero in an ergodic component; a bounded annulus of order
`1/(delta^2 T^2)`; and a tail of order
`T^-2 w^{-(d-1)}` (with a logarithm for `d=1`).  Taking
`delta=T^-1/2` and `w` proportional to `T^-1/d` makes all three vanish, a
contradiction.  Ergodic decomposition handles the general case: the only extra
zero-frequency term is the variance of the component intensity, while some
component has positive intensity.

This proves that every such integer random measure charges every open cone
about every Euclidean hyperplane.  Choosing a timelike normal and `c<1` gives
nonzero spacelike weight.  Simplicity and Lorentz invariance are unnecessary,
so the mathematical P-L claim under the FIXED hypotheses is DERIVED.

**Scope correction.**  Spacelike support alone does not prove a nonzero value
of a particular light-coupling form factor, an in-band rate, or an
observational noise floor.  Lorentz invariance moves nonzero weight around a
spacelike mass shell, but the shell may begin at Planckian invariant momentum.
Thus the spectral theorem is DERIVED; the prose implication “so it always
scatters observable in-band light” is conditional on a coupling/observable
bridge and is not part of the proved theorem.

## 3. LRL invariance in law, arithmeticity, and cocompactness

**Confirmed, with a quotient-formulation correction.**  Put
`D=diag(sqrt(7),1,1,1)` and `J=diag(-7,1,1,1)`.  Then

`Gamma_L = D SO(J,Z) D^-1 intersect SO^+(1,3)`.

It is an arithmetic subgroup of the rational semisimple group `SO(J)`, hence a
lattice by Borel--Harish-Chandra.  The original theorem is the 1962 Annals
paper *Arithmetic Subgroups of Algebraic Groups*.  Since `J` is anisotropic
over the rationals, the Godement compactness criterion makes this lattice
cocompact.

The anisotropy proof is exact.  If an integral solution has
`n0=2^a m`, `m` odd, then
`7 n0^2 = 4^a(8b+7)`, which Legendre's three-square theorem forbids.  Equivalently,
for odd `n0` reduction modulo 8 fails, while for even `n0`, divisibility by 4
forces all three spatial integers even and gives infinite descent.  If `n0=0`,
all entries vanish.  Rational solutions clear denominators to integral ones.
The independent enumeration and the exhibited unbounded integral boost are in
`referee_checks.out:6-9` and `referee_checks.out:19-22`.

The clean probability space is the homogeneous affine-lattice quotient

`ISO^+(1,3)/(L semidirect Gamma_L)`.

Equivalently one may choose a measurable representative of `g Gamma_L` and a
conditionally Haar-uniform torus shift.  “Independent `g` and `u`” is not
literally representative-independent, but changing representatives applies a
Haar-preserving torus automorphism, so the resulting law is well defined.
Left Haar invariance gives Lorentz invariance; torus Haar invariance gives
translation invariance.  Sign-change lattice automorphisms normalize the
construction and extend it from the proper orthochronous group to all Lorentz
components.  The affine Poincare action is transitive, so the law is Poincare
ergodic, although it is not translation-ergodic because the lattice shape is a
translation-invariant random variable.

## 4. Reciprocal lattice, hard core, and Bragg gap

**Confirmed.**  With the ordinary plane-wave pairing, the reciprocal lattice is

`L7_rec = 2 pi diag(1/sqrt(7),1,1,1) Z^4`,

and for `m in Z^4`

`G^2 = (2 pi)^2[-m0^2+7(m1^2+m2^2+m3^2)]/7`.

The numerator is integral.  If it vanished, `7` would divide `m0`, and after
writing `m0=7r` one obtains
`7r^2=m1^2+m2^2+m3^2`, already excluded.  Hence every nonzero reciprocal
vector obeys `|G^2| >= (2 pi)^2/7`, with equality attained; see
`referee_checks.out:11-17`.  There is no nonzero null reciprocal vector.

For a realized lattice `gL`, reciprocal covectors transform as `g^{-T}` under
the coordinate pairing, not literally as `g`; after raising the covector with
the Minkowski metric this is the usual Lorentz action.  This notational defect
does not affect the invariant-norm gap.  Likewise, every nonzero difference
vector has integral nonzero Minkowski square, so its Euclidean norm is at least
one in every frame.  This proves the uniform hard core.  Cocompactness also
gives uniform control of the lattice shapes, and finite-window point counts are
uniformly bounded; all local moments are finite.

## 5. In-band silence and the one-realization issue

**Narrow exact statement confirmed.**  A deterministic Poincare-covariant
field coefficient built only from a fixed realization inherits every
translation in `gL`; it is periodic.  An ideal infinite, defect-free periodic
linear propagation problem therefore conserves Bloch four-quasimomentum modulo
the reciprocal lattice.  Sums of reciprocal transfers remain reciprocal at
all perturbative orders.  For a one-photon `1 to 1` transition between
future-null momenta of frequencies at most `omega_max`, a nonforward transfer
has

`0 < q^2 <= 4 omega_max^2`,

while a collinear frequency change is null.  If
`4 omega_max^2 < (2 pi)^2/7`, neither can equal a nonzero reciprocal vector.
Thus ideal plane-wave `1 to 1` in-band mixing is exactly absent in that model.

**The report's broader “exactly zero at all orders, every realization, and RZ
passes trivially” is not established.**  Poincare covariance of an unspecified
functional does not by itself supply a linear wave equation, asymptotic states,
convergence of its orbit sums, or exclusion of substrate excitations and
inelastic/multiphoton channels.  Finite crystals, defects, switching of the
coupling, curvature, and boundaries break the exact reciprocal delta-comb; a
finite truncation has continuous off-Bragg leakage, as the elementary check at
`referee_checks.out:24-29` illustrates.  Forward `q=0` effects and virtual
Bragg mixing can also modify the dispersion or phase without appearing in the
incoherent Bragg rate.  The worker itself leaves steering and the mean kernel
open at `R2-2_report.md:255-261`, so no RL/RZ observable has actually been
computed.

A realization is not a conventional crystal with a unique rest frame: its
stabilizer is the conjugate arithmetic group `g Gamma_L g^-1`, which contains
unbounded boosts.  Nevertheless it breaks the continuous Lorentz group to a
discrete subgroup and has a realization-specific Bragg pattern.  Ensemble
invariance cannot average that pattern away in our one realization.  Borel
density means finite-rank polynomial tensors invariant under the arithmetic
group are Lorentz-invariant, so a dimension-four preferred tensor is not
automatic; this is consistent with O1's finding that continuous Lorentz
symmetry was not proved necessary.  But analyticity/convergence and the actual
matter/gravity effective operators are open.  Therefore LRL has not been shown
to satisfy the per-realization O1 bounds; nor has it been shown to violate them.

## 6. Labels and strongest correct statement

Both mathematical lemmas receive **DERIVED**: N-Q' under its explicit
positive-energy, covariance, vacuum-commutativity, halving-additivity,
integrality, and finite-second-moment assumptions; and P-L' for stationary
integer random measures of positive intensity and finite local second moments.
LRL is not a counterexample to P-L or to the FIXED **REFUTED** criterion,
because it has nonzero spacelike spectrum.  It is a valid counterexample to the
stronger spectral inference that such support must reach every low-energy band.
It is only a conditional counterexample to the physical “every steering
substrate makes RZ-level in-band noise” clause, because an ideal periodic
one-particle coupling would be silent but the required steering law and
observational bridge have not been constructed.

**Strongest correct statement.**  Positive energy plus an invariant vector,
covariant nonnegative integer counts with finite vacuum second moments,
vacuum-level commutativity, and additivity on the vacuum under temporal halving
force every count to annihilate the vacuum; independently, every stationary
integer-valued random measure of positive intensity and finite local second
moments has Bartlett weight in every cone about every hyperplane and hence, in
the Lorentz-invariant case, some spacelike weight.  Neither theorem puts that
weight in a prescribed sub-Planckian band: the cocompact arithmetic LRL based
on `-7n0^2+n1^2+n2^2+n3^2` is Poincare-invariant in law, has a uniform hard
core, and has no Bragg support for `0<|q^2|<(2pi)^2/7` or on the nonzero null
cone.  This proves an in-band spectral gap and exact ideal one-to-one Bloch
selection, but not an all-orders observational RZ pass or a viable event route,
because steering, finite-source/curved propagation, inelastic sectors,
convergent effective dynamics, and per-realization O1 bounds remain open.
