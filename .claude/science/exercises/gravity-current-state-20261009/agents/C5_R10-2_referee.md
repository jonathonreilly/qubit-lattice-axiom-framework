# VERDICT: CONFIRMED WITH CORRECTIONS

The bounded **FAIL** is earned by the proper smooth-box class: the displayed
Gaussian matter and TT covariances violate both site and link reflection
positivity, and the transfer-matrix analyticity argument excludes any
time-local two-point function with the same interior non-analyticity.  The
proof needs a correct two-sided/distributional Fourier treatment; the
Grassmann claim must be conditional on a genuine graded OS reconstruction;
the tensor no-go is a statement about the specified two-point function, not
every symbol in an arbitrary interacting action; and Lemma D by itself forces
spectral accumulation, not a continuum.  Conversely, the whole-zone scalar
SLAC covariance is not merely numerically compatible with link RP: it has an
explicit positive link-reflection spectral measure.  None of these
corrections removes the stated-class no-go that supplies the fixed FAIL.

## 1. Lemma A: site/link RP, the two-sided sum, and Grassmann scope

**Confirmed after a proof repair and a scope correction.**  Assume exactly the
OS reconstruction stated at `R10-2_report.md:57-61`: time-local insertions give
matrix elements of a bounded self-adjoint one-step transfer operator
\(T\), with \(\sigma(T)\subset[-1,1]\).  For sufficiently large positive and
negative separations one has, with generally different finite complex spectral
measures,
\[
 C(n)=\int_{-1}^{1}\lambda^{n-a}\,d\nu_+(\lambda),\qquad
 C(-n)=\int_{-1}^{1}\lambda^{n-b}\,d\nu_-(\lambda).
\]
Thus the two-sided Fourier distribution, modulo a trigonometric polynomial,
is the boundary value of a sum of two resolvents,
\[
 e^{-ia\theta}\!\int\frac{d\nu_+(\lambda)}{1-\lambda e^{-i\theta}}
 +e^{ib\theta}\!\int\frac{d\nu_-(\lambda)}{1-\lambda e^{+i\theta}}.
\]
Both are holomorphic in a complex neighbourhood of every real
\(\theta_0\notin\pi\mathbb Z\).  This is the missing treatment of the
\(n<0\) half in `R10-2_report.md:102-107`.  Endpoint atoms need not give only
delta distributions for the two *separate* one-sided sums (there can be
principal-value/resolvent pieces), contrary to the shorthand at
`R10-2_report.md:107`; all such pieces are nevertheless analytic away from the
corresponding endpoint, so the conclusion survives.

The queried inequality is exactly right for real \(\theta\):
\[
 |1-\lambda e^{-i\theta}|^2
   =(\lambda-\cos\theta)^2+\sin^2\theta
   \ge \sin^2\theta,
 \qquad -1\le\lambda\le1.
\]
For complex \(\theta\) near \(\theta_0\), the report's uniform half-bound
follows by compactness/continuity, not by applying the real inequality
literally.  If \(T\ge0\), the \(\lambda=-1\) endpoint is absent and only
\(\theta=0\) must be removed.  Usui proves the scalar link-reflection
reconstruction with a self-adjoint contraction and defines the Hamiltonian
from \(T^2\); adding site RP makes \(T\ge0\).  Luescher 1977 proves a strictly
positive transfer matrix for Wilson lattice gauge theory, not for arbitrary
Grassmann laws.

For Grassmann variables the algebra, reflection, and positivity condition are
graded.  Once a fermionic/Grassmann model has the standard graded OS
reconstruction and the relevant propagator component is a matrix element of
time-local reconstructed states, the same resolvent proof applies because it
uses no positivity of \(d\nu_\pm\).  But `R10-2_report.md:48-56,235` does not
state those graded hypotheses, and its blanket parenthetical “boson or
Grassmann” is not established merely by citing Luescher.  The unconditional
result here is the bosonic/H-OS class; the fermionic extension is conditional
as just stated.  Usui's result itself is for a complex scalar field, whereas
Osterwalder--Seiler treats lattice gauge fields with fermions.

Corollary A1 is therefore sound for the positive Gaussian box covariances at
`R10-2_report.md:112-116`.  Corollary A2 is also sound in its stated narrow
sense: one strictly negative finite OS minor persists when the finitely many
correlator entries in that minor converge as \(g\to0\)
(`R10-2_report.md:117`).  It is not an exclusion of arbitrary interacting box
actions whose exact two-point functions have not been shown non-analytic.

## 2. Lemma B and the O(4)-tensor argument

**Confirmed with an observable/smoothness qualification.**  On each connected
component \((0,\pi)\) and \((-\pi,0)\), the identity theorem propagates
\(F=h\) from the open box to the whole open zone
(`R10-2_report.md:119-128`).  For a scalar
\(h(\theta)=g(\theta^2+c)\), periodic \(C^1\) seam matching gives
\(2\pi g'(\pi^2+c)=-2\pi g'(\pi^2+c)\).  As \(c\) ranges through an open
interval, analyticity forces \(g\) to be constant
(`R10-2_report.md:130`).

The tensor-constant argument at `R10-2_report.md:132-135` is also correct under
its stated stronger premises: a globally real-analytic O(4)-covariant
continuum tensor (or one analytic on the connected punctured domain in the
massless case) and a smooth periodic seam.  Smooth seam equality supplies
periodicity in one direction on an open set; the multivariable identity
theorem extends it; O(4) covariance rotates the period to every vector of
length \(2\pi\); sums of such vectors generate all translations; hence the
tensor is momentum-independent, i.e. contact.  For the massless punctured
domain, paths/compositions can be chosen to avoid the isolated singular point.

Accordingly, the strongest form of `R10-2_report.md:137,141` is: no nonconstant
periodic \(C^1\) scalar (or \(C^\infty\) tensor under the global analytic and
covariance hypotheses) **two-point function of time-local observables** can be
both RP and exactly continuum-O(4) on an open box.  Axiswise W(B4) covariance
then carries the exact form through the whole open Brillouin cube.  This does
not, without an additional bridge, turn a non-analytic bare vertex or action
symbol in a general interacting law into a non-analytic observable
two-point function.

## 3. Lemmas C and D; Hankel reruns; the SLAC link-RP result

**Lemma C is correct for the stated bosonic scalar/diagonal covariance.**  A
site-RP diagonal correlator has a positive measure on \([-1,1]\), and its
Fourier kernel is a positive mixture of Poisson kernels.  The part of the
measure near \(\lambda=-1\) is maximal at \(\theta=\pi\); the part bounded
away from \(-1\) is analytic and even about that point.  It cannot produce the
upward cusp of the periodic SLAC slice when
\(h'(\pi)=2\pi g'(\pi^2+c)<0\)
(`R10-2_report.md:142-148`).  This is not a fermionic theorem as written.

**Link RP is stronger than the worker reports.**  Put \(c=a^2>0\) and
\[
 G_n=\frac1\pi\int_0^\pi\frac{\cos(n\theta)}{\theta^2+a^2}\,d\theta.
\]
A rectangular contour gives, for \(n\ge1\),
\[
 G_n=\frac{e^{-an}}{2a}
 +(-1)^{n+1}\int_0^\infty
 \frac{2y e^{-ny}\,dy}
 {(\pi^2+a^2-y^2)^2+4\pi^2y^2}.
\]
Therefore
\[
 G_{m+1}=\frac{e^{-a}}{2a}(e^{-a})^m
 +\int_0^\infty
 \frac{2y e^{-y}}{(\pi^2+a^2-y^2)^2+4\pi^2y^2}
 (-e^{-y})^m\,dy,
\]
which is the \(m\)-th moment of an explicitly positive measure on
\([-1,1]\).  Hence every matrix \([G_{1+i+j}]\) is positive semidefinite: the
free scalar whole-zone SLAC covariance is link-reflection-positive for every
fixed spatial momentum with \(c>0\).  The same scalar-slice statement applies
to the displayed nonzero-momentum TT covariance.  The independent code for
this formula is `referee_checks.py:71-89`; it matches direct Fourier
quadrature to \(1.1\times10^{-16}\) and gives a positive size-8 link Hankel
minimum in `referee_checks.out:26-28`.  Thus the finite-N wording at
`R10-2_report.md:149-152,253` can be upgraded to an exact result for this free
scalar covariance.  It still fails site RP and fails positivity of the
one-step transfer operator; its positive measure necessarily uses
\(\lambda<0\).

**Lemma D is correct only as an accumulation theorem.**  If the reconstructed
spectral support stayed in \([-r,1]\), \(r<1\), the resolvent would be analytic
at \(\pi\), so a cusp forces support arbitrarily close to \(-1\)
(`R10-2_report.md:153-157`).  These points have
\(E=-\log|\lambda|\to0\) for the \(T^2\) Hamiltonian and alternate under a
one-step time translation.  But support accumulation can be a pure-point
sequence; Lemma D alone does not prove the “continuum” asserted at
`R10-2_report.md:153,158-159`.  For the particular SLAC covariance above, the
explicit positive measure *does* contain a continuum with density proportional
to \(y\sim E\) near zero, so the continuum statement is true for that example,
not for every covariance satisfying Lemma D.

All worker scripts rerun byte-for-byte into
`referee_rerun_r102_rp_hankel.out`,
`referee_rerun_r102_slac_link.out`, and
`referee_rerun_r102_cube_n40.out`.  An implementation-independent
double-precision adaptive-quadrature check reproduces negative site and link
minors for both proper box profiles (`referee_checks.out:1-10`), negative site
but positive link minors for SLAC (`referee_checks.out:21-28`), and the worker's
high-precision signs are stable already at small Hankel size
(`scripts/r102_rp_hankel.out:12-46`).  These are decisive necessary-condition
violations for the proper boxes, not roundoff effects.  The worker's illustrative
\((0.3,0.2,0.1)\) is not exactly a momentum of a finite spatial torus, but the
nearby allowed \(L=64\) mode \(2\pi(3,2,1)/64\) gives the same strict negative
signs (`referee_checks.out:11-20`), so this bookkeeping mismatch is harmless.

## 4. The count \(5+\Lambda\)

**Confirmed as an operator-codimension count, not as a generated-counterterm
calculation.**  The refereed K1 count gives three W(B4) mass forms and nine
kinetic forms, versus two and four under O(4), with Einstein--Hilbert the unique
gauge-invariant kinetic direction (`C4_K1_referee.md:3,9`).  Exact O(4)
therefore leaves two mass coefficients to remove and three non-EH kinetic
directions: five gauge-restoration conditions, plus the separately counted
cosmological/tadpole tuning.  This is the precise meaning of
`R10-2_report.md:188-193`.

The O(4)-ball support argument does make the abstract loop tensor O(4)-covariant
when the full integrand and shifted support remain inside the continuum box.
The cube proxy reruns as \(R-1=-0.2562\) for SLAC and
\(+1.58\times10^{-5}\) for the ball at grid \(n=40\)
(`referee_rerun_r102_cube_n40.out:2-5`), with the latter converging as grid
error in `scripts/r102_cube_anisotropy_conv.out:4-10`.  But that proxy does not
construct a complete gravitational vertex, prove a Ward identity, or show
that all five directions are generated.  As the worker acknowledges at
`R10-2_report.md:192,198,255`, “one-loop count” must mean the available generic
O(4) coefficient-space codimension.  The Euclidean-TT value \(1+\Lambda=2\)
is not the physical full-field count; K1 already rejected TT restriction as a
physical floor (`C4_K1_referee.md:3,9`).  Also, for the massless gauge target
both O(4) mass coefficients must vanish; invoking only the Fierz--Pauli ratio
at `R10-2_report.md:193` would instead describe a massive theory.

## 5. R2-4 and R2-1

**R2-4 binds conditionally, unchanged in substance.**  Its actual premises are
a positive source-tilted measure, a real finite-range/exponentially local (more
generally summable, with bounded Fourier transform near zero) source kernel,
and an isotropic unscreened \(1/p^2\) response
(`C5_R2-4_referee.md:7-30,79-81`).  Super-polynomial box kernels are summable,
so replacing an analytic symbol by a smooth box symbol does not alter the
covariance-residue proof of \(a\le1/3\), hence \(\gamma\le1/2\)
(`R10-2_report.md:214-218`).  The box construction alone does not supply the
real source bridge or unscreened-response premise, so “binds unchanged” is a
conditional statement under R2-4's W1--W3, not an automatic consequence of
box kinematics.

**R2-1 binds only in a weaker sense than `R10-2_report.md:219-222` sometimes
suggests.**  Lemma A closes the specific attempt to use a *proper smooth-box
observable covariance* inside an RP theory, and Lemma D gives an analogous
infinite low-energy spectral price in the SLAC corner.  It does not restore
R2-1's exact H5 premise: globally periodic real-analytic finite-dimensional
one-particle Hamiltonian/charge matrices.  Analyticity of Euclidean
correlators only off the \(k_\mu\in\pi\mathbb Z\) hyperplanes neither constructs
those matrices nor carries analyticity through the pole/residue extraction.
The worker correctly concedes that Theorem T must be rederived
(`R10-2_report.md:220-221`), and the prior referee likewise limits it to the
globally analytic finite-fibre setting
(`C5_R2-1_referee_verdict.md:3,9-11`).  The SLAC spectral accumulation is not
itself R2-1's pure-point ladder theorem.

## 6. Fixed reading and exact scope

**The fixed reading is FAIL (bounded).**  PASS requires one explicit
reflection-positive Euclidean Z4 law with box-exact symbols and no more than
mass plus cosmological tuning at one loop (`TESTS.md:3977-3986`); none is
provided.  FAIL is independently met by the stated proper-box class:

- translation-invariant bosonic lattice laws admitting the standard site- or
  link-OS transfer reconstruction;
- with a time-local two-point covariance non-analytic at an interior box edge,
  including the displayed positive Gaussian smooth-plateau scalar and TT
  covariances; and
- perturbations whose finitely many correlator entries converge to those
  Gaussian values, so the exhibited strict negative minor persists.

The stronger smooth O(4) two-point-function formulation in section 2 is also
valid.  The no-go does **not** cover arbitrary interacting actions solely
because a bare symbol or vertex is box-shaped; arbitrary Grassmann laws without
the graded reconstruction hypotheses; or the nonsmooth whole-zone SLAC
corner.  Indeed the free scalar SLAC corner is exactly link-RP, though it has a
negative one-step transfer branch and a gapless time-alternating continuum and
does not furnish the requested low-tuning interacting graviton law.  Since the
fixed FAIL requires a no-go only in a stated class, these exclusions do not
change the verdict.

## Strongest correct statement

For any translation-invariant Euclidean lattice law whose relevant time-local bosonic two-point functions admit the standard OS representation by a bounded self-adjoint one-step transfer contraction, each fixed-spatial-momentum Fourier slice is distributionally real-analytic away from \(k_4=0,\pi\) (away only from \(0\) when the transfer operator is nonnegative); therefore the displayed proper smooth-plateau Gaussian box covariances, and sufficiently small correlator-continuous perturbations detected by their strict finite negative minors, fail both site and link RP, while a nonconstant periodic \(C^1\) scalar or suitably analytic \(C^\infty\) O(4)-tensor two-point function cannot be exactly continuum-O(4) on an open box.  The nonsmooth whole-zone scalar SLAC covariance is the sharp exception: it fails site RP but is exactly link-RP, with an explicit positive spectral measure containing \(\lambda<0\) continuously up to \(-1\), hence alternating \(T^2\)-energies down to zero at every nonzero spatial momentum.  If RP is abandoned and the complete loop integrand is confined to an O(4) ball inside the box, the registered full-field gauge-restoration codimension falls from 11 to 5, plus the separate cosmological tuning, not to the fixed PASS threshold of 2; this is a coefficient-space count rather than proof that all five counterterms are generated.  R2-4's \(\gamma\le1/2\) result remains conditional on its real, summable source bridge and unscreened positive response, while R2-1's exact globally analytic finite-fibre theorem is not rederived—only its proper-smooth-box escape is closed and a related SLAC spectral price is established.

## Literature checked

- K. Usui, *A Note on Reflection Positivity and the
  Umezawa--Kamefuchi--Kallen--Lehmann Representation of Two Point Correlation
  Functions*, arXiv:1201.3415: scalar link-RP reconstruction, self-adjoint
  contraction, Hamiltonian from \(T^2\), and positivity after adding site RP.
- M. Luescher, *Construction of a selfadjoint, strictly positive transfer
  matrix for Euclidean lattice gauge theories*, Commun. Math. Phys. 54
  (1977) 283--292, DOI 10.1007/BF01614090: Wilson lattice gauge theory, not a
  general Grassmann theorem.
- K. Osterwalder and E. Seiler, *Gauge Field Theories on a Lattice*, Ann.
  Phys. 110 (1978) 440--471, DOI 10.1016/0003-4916(78)90039-8: physical
  positivity for lattice Yang--Mills and fermion fields in its stated class.
