# VERDICT: CONFIRMED WITH CORRECTIONS

The central finite-band no-go is correct in the report's regular positive-energy
one-particle setting, but the advertised tower “iff,” the microscopic axiom
cost, and the partner/index interpretations are broader than the proofs.

## 1. Proposition 1

**Confirmed locally, with two corrections.**  At a simple point,

\[
 P_{\alpha\beta}={E_\alpha+E_\beta\over2}(Dh)_{\alpha\beta}
   +i(E_\alpha-E_\beta)a_{\alpha\beta}.
\]

Thus `[h,P]=0` uniquely fixes only the off-diagonal part

\[
a_{\alpha\beta}={i(E_\alpha+E_\beta)(Dh)_{\alpha\beta}
 \over2(E_\alpha-E_\beta)},\qquad \alpha\ne\beta,
\]

as stated at `I1_report.md:51-53`.  Every band-diagonal $a_b$ remains
arbitrary and leaves both $P_c=\partial_c(E_\alpha^2/2)$ and
$i[K_b,P_c]=-E_\alpha\partial_b\partial_c(E_\alpha^2/2)$ unchanged.  The
displayed boost at `I1_report.md:54` has therefore silently chosen the diagonal
improvement to vanish.  At an exact degeneracy, conservation fixes no component
inside the degenerate block; the formula is only an off-block/simple-spectrum
result (`I1_report.md:47,61-63`).

Once this choice is made, $K$ and $P$ are band-diagonal on every
simple-spectrum patch, and their commutator has exactly the claimed diagonal.
The worker scripts rerun byte-for-byte identically.  An independent
implementation gives conservation residual $6.28\times10^{-13}$, closure
off-diagonal $1.06\times10^{-6}$, and relative diagonal error
$2.00\times10^{-7}$; changing the sign of the improvement gives residual
$7.28\times10^2$.  It also explicitly verifies that a nonzero arbitrary
diagonal improvement changes neither $P$ nor the closure operator
(`i1_referee_checks.out:1-7`).  The worker's test is only one-dimensional,
nondegenerate, and finite-difference based (`i1_multiband_boost.py:2,33-51`),
so it does not test crossings or the global gluing step.

The necessary conclusion is “no nonzero-energy band may remain globally
isolated and periodic.”  “Touching at the zone face” at `I1_report.md:65-67`
is correct for the selected SLAC sheet and Brillouin-zone convention, but is
not invariant for arbitrary shifted centres: the touching/spectral-flow locus
can move when $\theta$ or the zone cut is moved.

## 2. Theorem 1

**The tower necessity is confirmed only after narrowing the statement.**

- The representation argument at `I1_report.md:80-86` is conditional on
  integration.  Nelson's theorem does not make integration automatic from the
  displayed commutators: one must establish a common invariant analytic-vector
  domain (in a sufficient Nelson-integrability form), essential
  self-adjointness, and the domain commutator identities.  The report assumes
  these as H-int but does not prove them.
- Given an integrated positive-energy Poincare representation, the argument is
  sound: $V_j=e^{ij\cdot P/\beta}T_j$ lies in the Poincare commutant, and each
  nontrivial Wigner component supplies all momenta $p\in\mathbb R^d$.  Folding
  $p$ modulo $2\pi\mathbb Z^d$ gives a complete reciprocal-lattice orbit and
  an unbounded energy tower.  The same global algebraic constant $\beta$
  applies to every nonzero-energy sector, whether or not sectors scatter
  (`I1_report.md:39-42,75-76`).
- The general representation is a **direct integral** of such components and
  of joint characters of the multiplicity-space $\mathbb Z^d$ action.  H-int
  alone does not imply a discrete set of $(m_j,\theta_j)$, finite
  multiplicities, or the finite list implicit at `I1_report.md:71-78`; those
  require compact-resolvent/local-finiteness assumptions.  Trivial zero-energy
  representations must also be excluded from the headline theorem.
- Under a discrete, locally finite band hypothesis, the centre-orbit step at
  `I1_report.md:88-92` is correct: on simple patches closure gives quadratics,
  periodic multiset equality matches distinct quadratics, and translation
  invariance of the centre/mass multiset forces complete
  $2\pi\mathbb Z^d$ orbits.  This rules out sub-towers.  The stated extra
  hypothesis `tr h^2 in C^2` cannot literally hold for the target tower,
  because \(\sum_n E_n(k)^2\) diverges; it should be replaced by local
  finiteness/compact-resolvent and gluing regularity.  Cubic covariance must
  preserve masses and multiplicities as well as the set of centres.
- The converse at `I1_report.md:94-98` constructs the canonical folded
  continuum, but $h_n(k)=E(k+2\pi n)$ is not literally periodic with an
  ordinary periodic $i\partial_k$ domain.  The fibre labels are shifted at a
  face.  The construction is valid after imposing this twisted boundary
  condition (equivalently, by unfolding to $L^2(\mathbb R^d)$); this is the
  rigorous content of the “Hilbert hotel.”  It proves existence of the
  canonical representation, not that arbitrary operator data with the same
  pointwise spectrum close.

Accordingly, “closure iff a discrete union of finite-multiplicity towers” is
too strong as written.  “Every nontrivial component of an integrated
positive-energy closure is a complete folded mass-shell tower, and the
canonical folded continuum realizes such towers” is supported.

## 3. Theorem 2

**The trace sum rule is correct.**  For finite $N$, pointwise

\[
  \sum_\alpha u_\alpha={1\over2}\sum_\alpha E_\alpha^2
  ={1\over2}\operatorname{tr}h^2.
\]

If the right-hand side is a well-defined periodic distribution, linearity of
distributional differentiation and the vanishing of the integral of a torus
derivative give

\[
 \sum_\alpha\int_{\mathbb T^d}\operatorname{Hess}u_\alpha=0.
\]

No smooth individual band labelling is needed.  Crossings merely make the
individual sorted eigenvalues nonsmooth; their distributional terms still sum
to the smooth trace.  The independent crossing example gives cyclic Hessian
sums below $1.4\times10^{-15}$ (`i1_referee_checks.out:8-9`).  The normalized
band-and-zone average of
$(\operatorname{Hess}u-\beta I)/\beta$ is therefore $-I$.  The word
“average” at `I1_report.md:109-116` should explicitly include division by
$N\operatorname{vol}(\mathbb T^d)$.

Two qualifications matter.  First, the trace identity is valid “at any
locality,” but using it as a closure no-go still needs Proposition 1's
first-moment/regularity assumptions; the identity alone is not an all-theories
no-go.  Second, at a band crossing an analytic/monodromy branch need not itself
be periodic, so its individual Hessian integral can be nonzero even though the
periodic trace sum is zero.  The partner value at `I1_report.md:118-122` is in
that branch convention.  Its script tests a prescribed $C^1$ spectral cap,
not an actual periodic matrix Hamiltonian (`i1_sumrule_partner.py:26-38`).

An $N$-cycle in one dimension can indeed be spectrally unfolded to one band
on a Brillouin zone $N$ times as long, corresponding to spacing $a/N$
(`I1_report.md:123-126`).  This is only a spectral equivalence.  It need not
preserve eigenvectors, Berry holonomy, interaction vertices, or real-space
locality, so “the same model” would be too strong.

The supplied numerical outputs reproduce exactly.  Part (a) is a cyclic
finite-difference telescoping identity (`i1_sumrule_partner.py:19-24`), and
part (c)'s exact value is analytically $-2\pi N\beta$; its increasing endpoint
roundoff at $N=27$ is not physical (`i1_sumrule_partner.out:16-21`).

## 4. Theorem 3

**Confirmed with stated regularity and a positive-energy qualification.**  For
finite $N$,
$\det T(k)=e^{-iNk}$ has winding $-N$ (the report says “$N$ times” without
orientation).  If $P(k)$ is a continuous periodic Hermitian matrix, then
$\det e^{-iP(k)/\beta}=e^{-i\operatorname{tr}P(k)/\beta}$ has the global
periodic logarithm $-\operatorname{tr}P/\beta$, hence winding zero.  Exact
closure and the first-moment translation law imply that
$V=e^{iP/\beta}T$ commutes with $K$.  On every nonzero-energy band or
persistent degenerate block, the derivative part of this commutator forces
the determinant of $V$ to be constant; isolated crossings do not change its
winding.  Thus $\operatorname{wind}\det V=0$, contradicting
$\operatorname{wind}\det T=-N$.  The independent calculation returns
$(-4,0,-4)$ for $(T,U,V)$, respectively (`i1_referee_checks.out:10-13`).

This requires the self-adjoint/domain identities needed to exponentiate $P$,
continuity and periodicity of $P(k)$, and exclusion of an identically
zero-energy block (which could carry winding without being constrained by
$K$).  Local finite-range $P$ has the required continuity.  SLAC does not,
as the report correctly notes at `I1_report.md:136-138`; the distributional sum
rule, rather than Theorem 3, is the relevant finite-$N$ check there.

## 5. Partners and decoupling

**Partly confirmed.**  A single exact global algebra has one $\beta$, so even
a dynamically decoupled nonzero-energy sector obeys the same curvature
condition.  Within one folded tower, the “bands” are momentum patches of one
Poincare orbit, not independent particle species.  A rule that makes an
amplitude vanish on one such patch but not on its Lorentz transform is not
boost covariant.  This supports `I1_report.md:142-150` for members of the same
tower and for kinematically related amplitudes.

It does **not** prove that every complete tower/species must interact, nor that
boost covariance makes a nonzero amplitude universal over different masses,
internal multiplicities, or different scattering invariants.  The free
$S=1$ tower and mutually decoupled full Poincare sectors are consistent.  The
statement should therefore be “a reciprocal-lattice patch of an interacting
tower cannot be deleted or independently decoupled,” not “partners that never
scatter are impossible.”  Likewise, absence of umklapp in an on-shell
$S$-matrix is weaker than full continuous-translation invariance of the
interaction Hamiltonian, so the equivalence asserted at
`I1_report.md:153-156` needs an asymptotic-completeness/Noether assumption.

## 6. Axiom cost and citations

**The one-particle cost is correct; the microscopic cost is not proved.**  A
complete tower makes the one-particle fibre infinite-dimensional and its
one-particle Hamiltonian unbounded.  A quadratic Bloch operator assembled from
uniformly bounded couplings and uniformly bounded internal degree is bounded,
as stated at `I1_report.md:162-164`; it cannot contain that tower.  Hence every
finite-component/quasi-free truncation is inexact.

This does not show that the microscopic one-site algebra must be
infinite-dimensional or that microscopic local terms must be unbounded.
Finite-dimensional qubit systems can in principle have infinitely many
extended composite species with increasing spatial support; the report itself
leaves that interacting-composite route open at `I1_report.md:179-183,191`.
The Jordan-Wigner/Majorana count at `I1_report.md:175-178` only covers a fixed
finite-component quasi-free realization.  Thus “Qubit price” is established
for an elementary on-site quadratic realization, not for every realization of
matter from the Qubit axiom.

The index citations are real but the application is not an obstruction.
[GNVW](https://arxiv.org/abs/0910.3675) gives multiplicative QCA index: a
qudit shift has index $d$, while locally implementable dynamics have index
1.  [Ranard-Walter-Witteveen](https://arxiv.org/abs/2012.00741) extends the
one-dimensional theory to approximately locality-preserving unitaries and
uses an additive/log normalization, where locally generated evolution has
index 0.  `I1_report.md:185-188` mixes those normalizations.  Blocking a finite
$L\times L$ transverse torus into one supersite does give shift index
$2^{L^2}$ in the GNVW normalization, but this is a one-dimensional reduction,
not a direct index theorem on infinite $\mathbb Z^3$.

Most importantly, $T=UV$ with trivial-index $U$ merely proves that $V$
carries the shift index.  It is not a contradiction unless one independently
proves that the many-body commutant of $(H,P,K,L)$ contains no such QCA.  The
report proves that only in the finite one-particle setting via Theorem 3; it
labels the many-body step merely “suggested” at `I1_report.md:188-192`, which is
the correct status.  The claim there that a long-range $P$ is the “remaining
way out” is consequently too strong.

The continuum-cube construction at `I1_report.md:202-216` is a valid existence
picture—continuum matter repartitioned into cubes—but it changes the one-site
algebra away from $M_2(\mathbb C)$ and uses unbounded internal differential
generators.  Its interacting no-umklapp claim additionally assumes a
continuum-translation-invariant interaction.  Calling this a “Lattice price in
substance” (`I1_report.md:194-198`) is an interpretation, not a proved axiom
classification.

## 7. Fixed-reading disposition

I1 establishes a **bounded version** of the first half of the fixed FAIL clause
at `TESTS.md:1281-1284`: in the regular, nontrivial positive-energy free
one-particle Bloch class with the stated first-moment generators, exact C1+C3
closure has no finite-$N$ realization; an integrated/discrete closure unfolds
into complete reciprocal-lattice mass-shell towers, so its one-particle fibre
is infinite and its one-particle Hamiltonian unbounded.  It does not prove that
an underlying qubit lattice cannot realize that infinite fibre through
extended interacting composites, and it does not prove a universal need for
unbounded microscopic local terms.  I1 also cannot decide lane RI by itself,
because the fixed FAIL reading conjunctively requires I3's non-decaying
coarse-cell anomaly/TT response (`TESTS.md:1277-1283`).

**Strongest correct statement.**  Under the report's first-moment definition of
boost and energy current, a nontrivial positive-energy finite-$N$ Bloch theory
cannot satisfy exact global Poincare closure: on simple band patches closure
forces the common relation
\(\operatorname{Hess}(E_\alpha^2/2)=\beta I\), while the periodic finite-band
trace sum and, for continuous $P(k)$, the determinant winding forbid closing
the patches into a finite torus fibre.  If the Lie algebra integrates to a
positive-energy unitary Poincare representation (or if a discrete locally
finite band-gluing hypothesis is imposed), every nontrivial component unfolds
into a complete reciprocal-lattice momentum tower and the canonical folded
continuum realizes it; hence every finite-band truncation is inexact and exact
closure requires an infinite-dimensional, unbounded **one-particle** fibre.
This does not establish an infinite microscopic on-site Hilbert space or
unbounded microscopic rule for interacting/composite qubit matter, and it does
not by itself satisfy the full lane-FAIL conjunction.
