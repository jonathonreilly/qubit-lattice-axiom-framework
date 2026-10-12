# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading is **PASS WITH SCOPE**.  The free construction P1 is a real
counterexample to a *local-domain* boost no-go: on
`C_c^infinity(int(B)^N)` the generators are literally the continuum
first-order generators, the Hamiltonian preserves the box, the Lie brackets
close exactly, finite boosts agree with continuum boosts until support reaches
the box edge, and the stated free leakage bound is valid.  This is enough for
the exact wording of `TESTS.md:3252-3255`, which expressly allows fermions and
does not require interactions or a gravitational Ward identity.  It does not
give an invariant/exponentiating Poincare sector or a universally coupled
gravitational theory.  P2 is repairable as a one-dimensional BT construction,
but is **not correct as written**: the displayed boost has the opposite sign
from P1's convention and the displayed unrestricted CAR quartic sum has a
factor-of-two error.  W1--W3 also require material narrowing; no interacting
stress tensor or universal coupling has been constructed.

## Reproducibility and independent route

- Both supplied runners reproduced byte-for-byte.  SHA-256 remained
  `73ca2ce...981b2` for `r71_box_poincare_free.out` and
  `ce19424a...5503` for `r71_bt_twobody.out`.  The free residuals and leakage
  numbers are at `scripts/r71_box_poincare_free.out:10-32`; the BT dispersion,
  support, decay and scattering numbers are at
  `scripts/r71_bt_twobody.out:1-38`.
- `scripts/r71_referee_checks.py:64-103` is independent of both worker
  implementations.  It checks the boost convention, enumerates the written
  quartic operator on a finite CAR Fock space, proves a positive lower bound
  for the chosen BT mass, and checks the zero-transfer Ward cutoff.  Its
  results are at `scripts/r71_referee_checks.out:1-11`.
- The BT theorem used below is standard only after its canonical hypotheses
  are met: in canonical variables, `H=sqrt(P^2+M^2)` and the boost is fixed by
  `M,P,X,S`; see Polyzou, *Reaction Theory*, equations (136)--(140),
  <https://homepage.physics.uiowa.edu/~wpolyzou/papers/brady/main.pdf>.
  The familiar failure of naive BT cluster separability for three or more
  particles is independently documented by Keister--Polyzou,
  <https://arxiv.org/abs/1109.6575>.

## 1. Lemma L and dynamical closure

**Confirmed for P1.**  On the open box, `s(k)=k` and
`epsilon=sqrt(m^2+|k|^2)` (`R7-1_report.md:63-71`).  Multiplication and
first-order differential operators preserve compact support, so every finite
composition preserves `C_c^infinity(int(B)^N)`.  Therefore the continuum
operator identities restrict to that domain exactly, and second quantization
preserves the commutator on finite-particle vectors
(`R7-1_report.md:87-104`).  In particular, the free `H` is diagonal in
momentum and cannot move support outside the box.

**The interaction also preserves momentum support.**  At fixed total `P`, the
BT difference kernel has support in `supp(g) x supp(g)`; multiplication by the
free energy preserves the input support, while the integral term outputs only
`supp(g)`.  Total `P` is unchanged.  Hence the stated two-body domain is
invariant under `H`, and the same support argument makes the all-`N` box
subspace invariant under the pair Hamiltonian even though no all-`N`
Poincare boost is known (`R7-1_report.md:135-139,163-167,221-223`).  The
factor-of-two defect found below changes the operator's value but not this
support conclusion.

**Important qualification.**  The domain is invariant under the *infinitesimal*
first-order generators, but it is not invariant under their unitary groups for
arbitrary rapidity or rotation.  The restriction of `K` to compactly supported
box functions is not the self-adjoint generator of a unitary group on the box
Hilbert subspace.  The global torus `K` can be self-adjoint, but its flow exits
the box.  Thus this is a common invariant Lie-algebra domain, not a reducing
Poincare sector.  That distinction is exactly what avoids B1 Theorem U.

## 2. P1 and the free runner

**The algebra is exact.**  With `X_i=i partial_i`, on the box

`K_i=i(epsilon partial_i + (partial_i epsilon)/2)`.

Direct calculation gives `[K_i,k_j]=i delta_ij epsilon`,
`[K_i,epsilon]=i k_i`, and `[K_i,K_j]=-iJ_ij`; the rotation brackets then
follow from the usual orbital representation.  This independently closes the
load-bearing formulas at `R7-1_report.md:96-109`.

**The numerical claim reproduces, with two wording corrections.**  The two
inside packets give residuals from `4.8e-14` to `1.3e-11`, while the
nearest-neighbour comparator has the advertised `5.6e-2` and `1.1` defects
(`scripts/r71_box_poincare_free.out:10-15`).  But the tested packets are
Gaussians, not compactly supported packets (`scripts/r71_box_poincare_free.py:124-128`),
and the finite torus uses a branch-cut position operator.  The residual floor
therefore tests small tails and the seam, not an exact finite matrix identity.
Also, the comparator is intentionally finite-range whereas the box law has
infinite, super-polynomially decaying hopping
(`scripts/r71_box_poincare_free.out:5-9`); it is a fair illustration of the
cosine obstruction, not an equal-locality performance comparison.

## 3. P2, BT, and Lemma Sm

**BT works in the intended one-dimensional plateau after corrections.**  In
`(P,q)` variables the internal operator `M=M0+lambda|g><g|` is independent of
`P`, so it commutes with total momentum and its conjugate center coordinate.
For the chosen attractive coupling,
`M >= 2m-2||g||^2 = 0.510325648142 > 0`
(`scripts/r71_referee_checks.out:7-8`).  Thus the positive square root is
well-defined and the usual spinless BT construction applies on the plateau.
In dimensions two or three, however, a single odd rank-one `g` is not a
rotational scalar; one needs a complete rotational p-wave multiplet (or another
rotationally invariant fermionic channel).  The submitted construction is
therefore established only in `d=1`, exactly where the runner operates
(`scripts/r71_bt_twobody.py:1-18`).

**Two load-bearing defects prevent confirmation of P2 as written.**

1. P1 fixes `[K,P]=+iH` and uses `X=i partial`, but P2 prints
   `K=-{H,X_NW}/2-...` while also printing `[X_NW,P]=i`
   (`R7-1_report.md:98-100,146`).  That gives `[K,P]=-iH`, as the independent
   check records at `scripts/r71_referee_checks.out:1-2`.  The first term must
   have the sign consistent with P1 (and the spin term adjusted to the same
   convention).
2. The displayed second-quantized law uses `1/2` times an unrestricted sum over
   both incoming and outgoing ordered momenta (`R7-1_report.md:73-80`).  Since
   the odd kernel is already antisymmetric in each pair, exact CAR enumeration
   gives twice the intended two-body matrix: ratios are exactly `2` in three
   independent entries (`scripts/r71_referee_checks.out:3-6`).  The full
   ordered-pair convention needs `1/4`, or the sums must be restricted to one
   representative of each unordered pair.  The runner instead inserts `W`
   directly as a first-quantized matrix (`scripts/r71_bt_twobody.py:90-105`),
   so it cannot detect this mismatch.

There is a further construction gap in the claimed global generator: simply
multiplying the derivative-containing `K_BT-K0` by `c(P)` need not be symmetric.
A symmetrized smooth cutoff/extension is needed.  On the plateau this is a
repairable extension issue, but the report has not supplied the globally
self-adjoint interacting generator required by its own H-gen statement
(`R7-1_report.md:33,146-147`).

**Lemma Sm is otherwise correct.**  The displayed resolvent identity for
`sqrt(A)-sqrt(A0)` has the right coefficient and ordering.  Uniform positivity
and the compactly supported smooth finite-rank perturbation make the kernel
smooth in `(P,q',q)` and supported in `supp(g) x supp(g)`; Fourier transformation
then gives decay faster than any power (`R7-1_report.md:148-153`).  The runner's
two decades of decay are consistent but do not prove the asymptotic class
(`scripts/r71_bt_twobody.out:19-28`).

**The BT runner reproduces but is not an algebra check.**  The `1.2e-10`
finite-grid mass spread reproduces (`scripts/r71_bt_twobody.out:12-16`).  Since
the code defines `W` by diagonalizing `M` and taking
`sqrt(M^2+P^2)-sqrt(M0^2+P^2)` (`scripts/r71_bt_twobody.py:68-83`), constant
invariant mass on the plateau is built into the construction.  The script never
constructs `K` or checks a commutator.  Its nonzero regulated internal
t-matrix does establish a nontrivial separable interaction, but not P2's
operator algebra (`scripts/r71_bt_twobody.out:29-38`).

## 4. Rapidity range and leakage

**Confirmed for the free flow, with scope.**  For one momentum and an axis
boost, rapidity translates `theta=asinh(k_parallel/m_perp)`.  Requiring both
signs `|eta|` to remain in `(-b,b)` gives
`eta*=asinh(b/m_perp)-|theta|`; for a support set and many legs one takes the
infimum over its points and legs.  For a one-sided boost, the absolute value is
replaced by the distance to the relevant edge.  Negative values mean that no
nonzero symmetric range exists (`R7-1_report.md:169-174`).

Let `E_eta` be the initial points whose continuum orbit exits the exact region.
On its complement the lattice and continuum characteristic flows, including
their half-density Jacobians, coincide.  Decomposing the initial state into
good and bad parts and using unitarity gives

`||(U_lat-U_cont)psi|| <= 2||1_E_eta psi||`.

This proves the stated bound, and the four computed inequalities reproduce at
`scripts/r71_box_poincare_free.out:22-28`.  For negative rapidity `E_eta` must
use the negative-direction endpoint.  The submitted check is free and
one-body.  For an interacting BT superposition the flow speed depends on the
internal mass spectrum, so an analogous set must include spectral support in
`M`, the total-`P` plateau, and the individual-leg box.  That interacting
leakage theorem was asserted but not proved.

The electron/proton rapidity numbers are arithmetically correct conditional on
identifying the lattice scale with the Planck scale, but that scale bridge and
the sentence “every observed process” are readings, not consequences of P1
(`R7-1_report.md:185-190`; `MINIMAL_AXIOMS_2026-06-29.md:187-190`).

## 5. Relation to the boost-wall referees

The construction does not contradict any supplied no-go, but the phrase
“evades the boost wall” must mean “lies outside the global hypotheses,” not
“supplies global/integrated covariance.”

- **C3/I2:** their periodic Hessian average is global over the Brillouin torus.
  Here the Hessian is continuum only on an open box and carries its compensating
  anomaly outside (`TESTS.md:1207-1215`;
  `scripts/r71_box_poincare_free.out:1-4`).
- **I1/I3:** patches cannot be deleted or decoupled *under integrated boost
  covariance* (`C4_I1_referee.md:7,13`).  The R7 box is closed under `H` but is
  not closed under finite boosts; its edge modes are therefore not a separate
  boost-covariant sector.  I3 does not bite the local Lie-algebra statement,
  but it forbids promoting that statement to the integrated representation the
  worker declines to claim.
- **B1:** Theorem S is satisfied.  Theorem U misses because the box is not a
  reducing exponentiating `K`-sector, and Theorem R misses because no global
  Lorentz action on the torus is claimed.  The B1 referee explicitly leaves
  patchwise actions open (`C4_B1_referee.md:7-15`).
- **M1:** T1 misses P2 because the bound-state band is not globally isolated;
  T2's finite-range/exponentiating hypotheses also fail.  More basically, the
  exact brackets fail globally.  M1 therefore does not refute the patch, but it
  does refute any unqualified globally isolated/integrated reading
  (`C4_M1_referee_full.md:30-42,44-81`).
- **C1, R2-1 and RFW F1:** their relevant exclusions require analytic finite
  matrices or finite Fourier/local symbols.  The plateau functions are smooth
  but nonanalytic and have infinite Fourier support
  (`RC_C1_referee.md:11-13`; `C5_R2-1_referee_verdict.md:3,11`;
  `RFW_F1_referee_full.md:81-125`).

The no-go stress test therefore has at least five distinct attacks: periodic
Hessian averaging, bounded-sector exponentiation, reciprocal-tower patch
gluing, global torus topology, and analytic/finite-Fourier continuation.  They
collapse to two prices here: loss of integrated/global covariance and loss of
analytic/exponential locality.  The hidden additional price is loss of
universal gravitational coupling.  The proposed stress tensor omits energetic
edge modes altogether, so the “inert, non-gravitating edge sector” is not
consistent with a graviton that couples universally to total energy-momentum.
This is not prohibited by the minimal axioms, which do not supply a graviton or
source bridge (`MINIMAL_AXIOMS_2026-06-29.md:85-95,173-190`), but it means R7
has not broken the *gravitational* wall.

## 6. Ward claims

**W1 is a correct free on-shell identity only on a narrower `chi=1` subbox.**
The algebra `q_mu F^{mu nu}=0` is correct for equal-mass on-shell legs, and
`s(q)=q` on the cutoff support makes the spatial lattice contraction identical
to it (`R7-1_report.md:194-202`).  At zero transfer, however, the proposed
operator integrates to

`sum_k chi(k)^2 epsilon(k) n_k`,

not `H0` on all of `D_B`; a box momentum outside `supp(chi)` gives zero instead
of its positive energy (`scripts/r71_referee_checks.out:9-11`).  It equals
`H0` only after the matter domain is narrowed to where `chi=1`.  It never
includes the interaction `W`, contrary to an interacting reading of
`integral T00=H` at `R7-1_report.md:203`.

**W2 is not established for the interacting law.**  Exact additive momentum
and energy conservation do not construct the interaction contribution to
`T^{mu nu}` or its graviton vertex.  The displayed soft matrix element is a
free one-body vertex.  The R6-1 referee already emphasized that exact collision
momentum alone is not a graviton Ward identity
(`C5_R6-1_referee_verdict.md:29-33`).

**W3 survives only as a free global-affine algebra statement.**  P1 supplies
the free affine Poincare brackets.  P2 cannot supply the interacting part until
its sign and normalization are repaired, and even repaired BT covariance is a
global two-body representation, not the missing local density/constraint
algebra.  **W4 remains open**, as the report correctly states
(`R7-1_report.md:205-213`).  Accordingly R7 supplies no exact universally
coupled linearized graviton on the lattice.

## 7. Fermionic clause and fixed reading

The intended fermionic clause is met.  R7's fixed PASS text expressly says
“fermionic allowed, as for R6-1” (`TESTS.md:3252-3255`).  One CAR mode per site
has two local states and one-site algebra `M_2(C)`, but cross-site composition
is graded.  That distinction defeated R6-1 only because R6-1's governing
setting separately required the ungraded spin tensor product
(`C5_R6-1_referee_verdict.md:17-19`).  R7 deliberately removes that ambiguity.

The exact fixed PASS clause asks for an explicit finite-per-site law, exact
Poincare algebra on a stated box sector, a rapidity range, a leakage bound and a
check.  P1 alone supplies all five.  It does **not** ask for interacting all-`N`
closure, gauge fields, pair creation, loops, W1--W4, or a universal graviton.
Therefore the correct registered reading is **PASS WITH SCOPE**, not
INCONCLUSIVE.  The scope must say: graded CAR; continuous time; free algebra at
all finite particle numbers; nonanalytic super-polynomial/subexponential
tails; local-domain rather than integrated box covariance; interacting P2 not
confirmed as written and in any case only two-body/d=1 after repair; no gauge
fields, pair creation, loop protection, local-lapse algebra, or universal
gravitational coupling (`R7-1_report.md:244-270`).

## 8. Strongest correct statement

There exists an explicit one-CAR-mode-per-site, continuous-time lattice Hamiltonian with smooth periodic but nonanalytic, super-polynomially quasi-local hopping whose dispersion equals `sqrt(m^2+|k|^2)` on an open momentum box, such that on finite-particle `C_c^infinity` wavefunctions supported there the first-moment boosts, momentum and rotations satisfy the undeformed Poincare **Lie algebra exactly**; its finite boost agrees with the continuum flow until the support reaches the box boundary, with `eta*=asinh(b/m_perp)-|theta|` for a single axis-boosted leg and `||(U_lat-U_cont)psi||<=2||1_E psi||`.  This is a genuine patchwise/local-domain counterexample to claims that no box can carry exact infinitesimal boosts, and it lies outside the supplied global, integrated, analytic and finite-Fourier no-gos.  It is not a reducing or exponentiating Poincare sector and not an exact gravitational theory: the submitted two-body BT theorem has a boost-sign error and a CAR factor-of-two error (though a corrected `d=1` BT construction is available), the Ward vertex equals the energy only on a narrower free `chi=1` subbox and omits interaction and edge energy, W4 is open, and inert non-gravitating edge modes violate universal gravitational coupling.  Hence the fixed reading is **PASS WITH SCOPE**, while the broad claims of an interacting P2 as written or of breaking the gravitational boost wall are not confirmed.
