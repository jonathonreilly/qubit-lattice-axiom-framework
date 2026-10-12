# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed RN2 reading is **INCONCLUSIVE, leaning FAIL**.  A narrower no-go is
proved for a global regular eigenband, but that is not the stated class in the
fixed FAIL clause.  The tower alternative remains open for interacting qubit
matter in (d=2,3).

## 1. Lemmas 1--3

**Confirmed, with one material narrowing.**  Under H-int, the positive-energy
joint spectrum is in the forward cone.  The gapped unique vacuum therefore has
joint energy-momentum zero; its one-dimensional line carries the trivial
continuous Lorentz character, giving (P\Omega=K\Omega=L\Omega=0)
(`N1_report.md:42-56`).  A massless positive-energy irreducible representation
has energies arbitrarily close to zero, so H-gap excludes it
(`N1_report.md:64-70`).

The important part of Lemma 3 is correct in the strong/domain sense: the
spectral projections of the Casimir
(\mathcal M^2=H^2-P^2/\beta) reduce the integrated Poincare representation,
and hence the boost one-parameter groups and their generators.  H-cov also
makes them invariant under lattice translations (`N1_report.md:72-80`).  What
does **not** follow is the literal sentence that a boost cannot mix a
"one-particle state" with every state one might call multiparticle.  It cannot
leave the (M_1) spectral subspace; within a degenerate fixed-mass
multiplicity space it may mix particle/composite labels.  Nor does H-gap alone
identify the entire complement with a scattering continuum of invariant mass
at least (2m).  The safe claim is spectral-subspace invariance.

## 2. Theorem 4 and the bounded-sector claim

**The representation-theoretic core is confirmed.**  If an isolated mass
eigenvalue (M_1>0) exists and the algebra integrates, its spectral subspace
decomposes into positive-energy mass-(M_1) Poincare irreducibles.  With
(V_j=U(j)^{-1}T_j) in the commutant, a simultaneous character
(e^{i\theta\cdot j}) on each multiplicity component gives

\[
 E_n(Q)=\sqrt{M_1^2+\beta|Q-\theta+2\pi n|^2},\qquad n\in\mathbb Z^d.
\]

This applies equally in an interacting GNS representation and uses no particle
number (`N1_report.md:82-95`); continuous θ-direct integrals, spin and
infinite multiplicities must be allowed, as already required by the I1 referee
(`C4_I1_referee.md:7`).  It does **not** prove that such an isolated mass
eigenvalue exists, that it has a particle interpretation, or that the tower is
realizable by bounded qubit interactions.  The runner reproduces the folded
tower kinematics, not those existence/realization claims
(`N1_report.md:97-112`).  Statements about embedding in a two-particle
continuum additionally require the corresponding scattering states and their
thresholds.

Section 2.1 is overstated.  It is false that the only (K)-invariant sectors
are spectral subspaces of the mass operator; internal-charge and multiplicity projections in
the Poincare commutant are elementary counterexamples
(`N1_report.md:150-154`).  The correct statement is: every nontrivial
Poincare-invariant positive-energy sector contains an unbounded boost orbit,
so (H) is unbounded there.  Losing number conservation removes M1-T2's
automatic fixed-(N), bounded-sector application; it does not invalidate B1
Theorem U on any bounded (K)-invariant sector that independently exists
(`C4_B1_referee.md:7`).

## 3. Theorem 5 and Corollary 6

**The theorem is correct with all of its stated hypotheses, but the corollary
and genericity claim are too broad.**  Strong conservation makes the joint
((T,H)) band projector reduce (P).  In a local (C^1) band frame,

\[
 \Pi K_b\Pi=\tfrac12\{i\partial_b,E\}+f_b(Q),\quad
 \Pi P_c\Pi=\partial_c(E^2/2),\quad
 \Pi i[K_b,P_c]\Pi=-E\,\partial_b\partial_c(E^2/2).
\]

Thus exact closure forces
(\operatorname{Hess}(E^2/2)=\beta I), contradicting periodicity.  The
symbol/sign and periodic-Hessian check are independently reproduced in
`N1_referee_checks.py:20-46`.  The result needs the report's strong/domain-valid
commutation and weak-form band core, plus its explicit
(u=E^2/2\in W^{2,1}(\mathbb T^d)) assumption
(`N1_report.md:114-129`).

Corollary 6 drops that last hypothesis, so the dual sentence "closure implies
every eigenprojection is discontinuous" is not established by Theorem 5
(`N1_report.md:131-136`).  It should say that closure excludes every global
eigenband having both a (C^1) projection and the stated (W^{2,1})/domain
regularity.  Calling the class "generic" is also unsupported.  The cited
Bachmann--Dybalski--Naaijkens Haag--Ruelle paper assumes the difficult
existence of a smooth, fibre-isolated mass shell on an **open momentum set**;
it does not supply a norm-(C^1) eigenprojection over the whole torus.  Such
local shell patches may exist away from a tower face, so BDN is not wholly
inapplicable; it simply does not provide the global periodic band needed for
T1 (`N1_report.md:34-37,136,290-294`).

## 4. The expected route

**The substantive objection is confirmed, but "circular" should be replaced
by "assumes the disputed global spectral premise."**  Gap plus asymptotic
completeness does not imply a globally isolated smooth Bloch band.  Conditional
on exact integrated closure, any isolated mass eigenspace instead decomposes
into complete folded towers, whose finite-rank energy-sorted branches meet at
zone faces (`N1_report.md:22-28,82-112`).  Assuming a global regular band and
then applying T1 proves a valid conditional no-go, but cannot exclude the tower
case.  Local Haag--Ruelle patches and cluster decomposition do not restore the
missing global periodic projector (`N1_report.md:138-146`).

## 5. Lemma F and the (d\ge2) index route

**Step 1 is confirmed only under every listed condition; Lemma F is not proved
by this report.**  Integrated closure, H-cov, asymptotic completeness for the
continuous-(P) particles, and a common denominator (q) for all tower
centres give (V_j^q=1), hence

\[
 \tau_{q e_b}=\operatorname{Ad}e^{-iqP_b/\beta}
\]

on the simple quasilocal algebra (`N1_report.md:158-168`).  There is a harmless
but real normalization error at `N1_report.md:178`: to obtain this exponent use
either time (q/\beta) with generator (P_b), or time (q) with generator
(P_b/\beta), not time (q/\beta) with generator (P_b/\beta)
(`N1_referee_checks.py:49-61`).

For a strict tube automorphism, the volume-versus-boundary GNVW scaling is
sound.  For the actual Lieb--Robinson flow, however, the needed statement is
precisely the unproved approximate Lemma B: closeness to the identity only on
the growing interior tensor factors must give a dimension-uniform bound on the
one-dimensional ALPU index after all tail and window errors are included
(`N1_report.md:177-196`).  The one-dimensional RWW robustness theorem and the
Choi mutual-information formula do not by themselves prove this transverse
partial-factor estimate.  The sketch is plausible and has the right scaling,
but it cannot promote Lemma F or the broad class to FAIL.  Irrational centres,
failure of AC, and absence of isolated mass point spectrum remain outside Step
1 (`N1_report.md:199-207`).

## 6. Verdict under the fixed readings

The fixed FAIL clause requires impossibility for the stated RN2 class
(`TESTS.md:1980-1993`).  The report proves only a proper regular-band subclass,
while its own tower steelman remains unclosed.  Therefore the probe is
**INCONCLUSIVE, leaning FAIL**, with a separately recordable bounded FAIL for
the global (C^1+W^{2,1}) eigenband class.  The no-go stress test reaches the
same result: multiple routes were examined, but the BDN/global-projector
residual is mismatched and the tower/index counter-route remains actionable.

## Strongest correct statement

Assume exact commutators integrate to a positive-energy Poincare
representation and obey first-moment lattice covariance.  Then the gapped
vacuum is invariant, every fixed-mass spectral subspace is boost- and
lattice-translation-invariant, and each of its irreducible multiplicity
components folds into a complete reciprocal-lattice tower, without any
particle-number assumption.  Independently, exact closure is impossible if
the theory contains a nonzero global joint ((T,H)) eigenband whose projector
is (C^1), whose (u=E^2/2) lies in (W^{2,1}(\mathbb T^d)), and for which
the strong/weak-domain commutators used in the compression are valid.  Neither
a gap plus asymptotic completeness nor lattice Haag--Ruelle supplies that
global band hypothesis, and the proposed (d\ge2) index extension still lacks
its dimension-uniform approximate tube lemma; hence RN2 remains inconclusive,
though the regular-band subclass is a rigorous bounded no-go.
