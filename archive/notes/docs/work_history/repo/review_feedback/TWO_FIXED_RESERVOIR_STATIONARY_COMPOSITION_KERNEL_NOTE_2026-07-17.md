# Two Fixed Reservoirs / Stationary Composition Kernel

Date: 2026-07-17
Authority: none
Audit: unset
Runner: `scripts/two_fixed_reservoir_stationary_composition_kernel_2026_07_17.py`

Test contract: two active fixed local reservoirs at distinct cells in the
conserved one-excitation sector; a selected symmetric bright eigenpair; one
antisymmetric lambda=1 compatibility member; an additive shifted-resolvent
profile; a spectral cross-coordinate; a
composition-safe shifted bilinear; comparison with Cycle216; separation,
theta=0 endpoint, covariance, held-out L=9, zero-mode subtraction,
normalization, selector-window, complete proper-cubic orbit-partition, and
lawful-domain controls.

## Result

The equal-coupling two-reservoir update has two independently controlled
finite-matrix constructions.

1. A numerically selected positive-phase bright eigenpair has an exactly
   additive two-source shifted-Green scalar profile on the fixed-neighbour
   fixture at every tested periodic volume L=3,...,9.
2. A zero-total-\(q\) antisymmetric \(\lambda=1\) compatibility member is
   constructed directly and satisfies the complete update on the
   fixed-neighbour fixture at every one of those sizes and at all 38 held-size
   proper-cubic separation orbits.  Its two local \(q_i\) coordinates and its
   field component are nonzero.
3. On held-out L=9, the bright eigenphase and the local gate equation extract
   the off-diagonal field response at all 38 proper-cubic orbit
   representatives of nonzero minimal-image separations.  The extracted
   coordinate agrees with the direct field resolvent.
4. With supplied nonreal coefficients on the two zero-mean point sources, the
   quadratic pairing decomposes into the two ordered self terms and two
   ordered genuinely complex cross terms, with conjugate reciprocity, to
   numerical precision.

No spectral census, multiplicity theorem, or conclusion about generic level
splitting is drawn from these two constructed members.  The selected bright
eigenphase contains a separation-dependent off-diagonal response coordinate.
The algebraic two-source composition result is scoped to two distinct,
disjoint local vertices and the declared zero-mean shifted operator.  The
runner deliberately rejects co-located vertices, whose local gates would
overlap.  Any extension to that domain must explicitly declare how overlapping
gates compose; an order or collision law is one possible route.

The finite response is

\[
 H_\mu=3(L-\mu I)^{-1},
 \qquad \mu=6(1-\cos\omega),
\]

on the zero-mean subspace.  It is close to, but not identical with,
Cycle216's \(3L^+\) at the tested nonzero \(\mu\).  Exact Cycle216 equality is
recovered only in the separately declared zero-shift comparator.

This is a finite operator result.  It is not physical energy, not gravity,
not a force or source/stress law, and the eigenphase is not a rate or clock.
There is no host-side renewal.

## Two-vertex closed update

At distinct cells \(x_1\ne x_2\), supply two reservoir directions
\(|r_1\rangle,|r_2\rangle\) and the local scalar field directions
\(|s_{x_1}\rangle,|s_{x_2}\rangle\).  Each vertex uses the same conjugate
exchange

\[
 V_i=\exp[-i\theta T_i],
 \qquad
 T_i=|r_i\rangle\langle s_{x_i}|
     +|s_{x_i}\rangle\langle r_i|.
\]

The complete one-excitation update is

\[
 U^{(2)}_\theta
 =(I_r\oplus S)V_2V_1(I_r\oplus C).
\]

Because the two cells are distinct, the two seven-dimensional vertex blocks
have disjoint support and \([V_1,V_2]=0\) exactly.  The runner checks the full
update's unitarity, norm preservation, radius-one emission from either active
cell, and the supplied scalar identity \(C|s_x\rangle=|s_x\rangle\).

No preferred host order is used for these disjoint vertices.  This statement
does not cover co-location, many excitations, moving reservoirs, or a general
collision schedule.

## Bright eigenpair and exact additive profile

Write a selected bright eigenvector as reservoir amplitudes \(a_i\) and field
amplitude \(f\):

\[
 U^{(2)}_\theta|\Psi\rangle
 =\lambda|\Psi\rangle,
 \qquad \lambda=e^{i\omega}.
\]

For each size and separation, sparse shift-invert uses the supplied target

\[
 \exp[i\sqrt2\theta/L^{3/2}]
\]

and requests exactly three candidates.  Among returned candidates with
positive phase above \(10^{-8}\), the runner selects maximum total reservoir
squared-norm weight, normalizes the vector, and fixes the common phase by
making the reservoir sum real-positive.  The supplied phase-ratio acceptance
window is

\[
 0.95<\frac{\omega L^{3/2}}{\sqrt2\theta}<0.98,
\]

and the supplied total reservoir squared-norm-weight window is \((0.44,0.47)\).
On the fixed-neighbour L=3,...,9 sweep the observed ranges are
0.956806--0.971406 and 0.447735--0.462046, respectively.  Across all 38 held
L=9 separations they are 0.956806--0.968879 and 0.447735--0.459120.  These are
runner acceptance windows and supplied selection structure, not a spectral
uniqueness theorem, physical constant, preparation mechanism, or statement
about untested sizes.

At the two vertices define

\[
 b_i=\langle s_{x_i}|Cf\rangle,
 \qquad
 q_i=(\cos\theta-1)b_i-i\sin\theta\,a_i.
\]

The runner checks both reservoir equations

\[
 \lambda a_i=\cos\theta\,a_i-i\sin\theta\,b_i
\]

and the complete field equation

\[
 (\lambda-U_f)f
 =\sum_{i=1}^2 q_i U_f|s_{x_i}\rangle,
 \qquad U_f=SC.
\]

For the symmetric bright branch, \(a_1=a_2\) and \(q_1=q_2\) within the
tested residuals.  With
\(\rho_i=\delta_{x_i}-|\Lambda|^{-1}\), the nonuniform scalar component is

\[
 \boxed{
 \phi_\perp
 =-\frac12\sum_iq_i\rho_i
 +i\sin\omega\sum_iq_i\,3(L-\mu I)^{-1}\rho_i.
 }
\]

This is a direct linear composition of the two local gate coordinates.  No
Green coefficient is fitted.  The explicit uniform component is also tested:

\[
 \overline\phi
 =\frac{q_1+q_2}{L^3}
 \left(-\frac12-i\frac{3\sin\omega}{\mu}\right).
\]

Across L=3,...,9, the maximum observed bright eigenpair residual is below
\(5.30438\times10^{-16}\), the maximum field block-equation residual is below
\(5.32383\times10^{-16}\), and the maximum normalized composition residual is
below \(4.95849\times10^{-14}\).  These are observations on the declared
finite matrices, not statements about untested sizes.

## Antisymmetric lambda=1 compatibility member

For the antisymmetric coordinate choose

\[
 q_1=-q_2,
 \qquad
 \sigma=\delta_{x_1}-\delta_{x_2}.
\]

This source has no uniform Fourier component.  At \(\lambda=1\), solve the
field equation mode by mode with the Moore-Penrose inverse on the flat
directions:

\[
 (I-U_f)f=U_f|s\rangle\sigma.
\]

The scalar projection is exactly the local coordinate
\(-\sigma/2\) for the chosen normalization.  The reservoir amplitudes are
then fixed by

\[
 a_i=-i\frac{\sin\theta}{1-\cos\theta}\,b_i.
\]

The assembled state obeys \(U^{(2)}_\theta|\Psi_a\rangle=|\Psi_a\rangle\).
After normalization, the runner recomputes both local \(q_i\) values and
checks

\[
 q_1+q_2=0,
 \qquad |q_1|=|q_2|>0,
\]

together with nonzero field squared norm and the compatibility equation

\[
 (I-U_f)f=q_1U_f|s_{x_1}\rangle+q_2U_f|s_{x_2}\rangle.
\]

On the fixed-neighbour size sweep, the maximum stationary residual on
L=3,...,9 is below
\(3.5\times10^{-16}\).  The minimum local \(|q_i|\) is above 0.251, the
field squared-norm weight lies between 0.0608 and 0.0630, and the maximum
field compatibility residual is below \(3.5\times10^{-16}\).  This constructs
one antisymmetric compatibility member with zero total scalar coordinate but
nonzero local exchange and field content.  It does not claim that the
\(\lambda=1\) eigenspace is
one-dimensional, spectrally unique, exhaustive, or evidence for or against a
generic splitting pattern.

The same construction is separately tested at all 38 held-size separation
orbits.  There the maximum stationary residual is
\(4.32932\times10^{-16}\), the maximum \(|q_1+q_2|\) is
\(1.38783\times10^{-16}\), the minimum local \(|q_i|\) is 0.247854, the
field squared-norm weight lies between 0.0629353 and 0.0865804, and the
maximum field-compatibility residual is \(3.77195\times10^{-16}\).  This
held-size extension remains one explicitly constructed compatibility member
per declared pair; it is not a multiplicity census.

## Spectral cross-coordinate

Let \(h_\lambda(x-y)\) be the free-field scalar response

\[
 h_\lambda(x-y)
 =\langle s_x|(\lambda-U_f)^{-1}U_f|s_y\rangle.
\]

On the symmetric bright branch,

\[
 b_1=q_1\,[h_\lambda(0)+h_\lambda(x_1-x_2)].
\]

The local reservoir equation gives the same symmetric response using only the
known gate angle and eigenvalue:

\[
 \frac{b_1}{q_1}
 =\frac{\lambda-\cos\theta}
 {(\cos\theta-1)(\lambda+1)}.
\]

Therefore the off-diagonal response is extracted as

\[
 \boxed{
 h_\lambda(x_1-x_2)
 =\frac{\lambda-\cos\theta}
 {(\cos\theta-1)(\lambda+1)}-h_\lambda(0).
 }
\]

The self response \(h_\lambda(0)\) is supplied by the same free field walk;
it is not inferred from the pair spectrum.  The cross-coordinate therefore
uses the measured finite eigenvalue plus the supplied local gate and free
field law.  It is not a claim that the eigenphase alone determines a physical
interaction.

On held-out L=9 the runner tests the complete declared set

\[
 \mathcal S_+
 =\{(a,b,c):4\geq a\geq b\geq c\geq0,\ a>0\},
\]

and

\[
 \mathcal S_-
 =\{(a,b,-c):4\geq a>b>c>0\}.
\]

Together these are the 38 proper-cubic orbit representatives of nonzero
minimal-image separations on the L=9 torus.  The four all-distinct nonzero
absolute-coordinate triples have two proper-cubic orbits, so their second
signed representatives are retained rather than silently using an improper
inversion.  Tests at a representative do not count its rotated copies as
independent held geometries.

The runner independently partitions all \(9^3-1=728\) nonzero minimal-image
vectors under all 24 proper-cubic frames.  It obtains exactly 38 orbits and
checks that every orbit intersects the declared representative set exactly
once.  The derived orbit-size distribution is 4 orbits of size 6, 4 of size
8, 4 of size 12, and 26 of size 24.  It thereby covers all 728 nonzero
minimal-image vectors.

The maximum direct spectral cross-response residual is
\(2.10193\times10^{-15}\).  Removing the explicit uniform resolvent coordinate
recovers the zero-mean shifted cross-coordinate with maximum residual
\(1.34917\times10^{-12}\).

The bright phase is nonconstant over this declared separation list and has 34
values distinct at tolerance \(10^{-12}\).  The four signed chiral pairs
\((3,2,\pm1)\), \((4,2,\pm1)\), \((4,3,\pm1)\), and
\((4,3,\pm2)\) are inversion-related degeneracies even though each signed
member belongs to a distinct proper-cubic orbit.  Thus the result is finite
and separation-sensitive but does not distinguish those four chiral pairs.
It is not an assignment of energy, rate, force, or binding semantics.

## Composition-safe shifted bilinear

For zero-mean scalar sources \(\rho_1,\rho_2\), define the finite operator
coordinate

\[
 B_\mu(\rho,\eta)
 =\langle\rho|3(L-\mu I)^{-1}|\eta\rangle.
\]

Self-adjointness on the tested pole-free domain gives conjugate reciprocity,

\[
 B_{12}=B_{21}^*.
\]

Linear composition is retained in its full ordered complex form.  For the
nontrivial numerical probe, the supplied coefficients are
\(\alpha=1+0.5i\) and \(\beta=-0.3+0.8i\), so
\(\rho_1=\alpha\rho_{x_1}\) and \(\rho_2=\beta\rho_{x_2}\):

\[
 B_\mu(\rho_1+\rho_2,\rho_1+\rho_2)
 =B_{11}+B_{12}+B_{21}+B_{22}.
\]

The runner preserves all four terms as complex numbers, requires a nonzero
imaginary cross coordinate, computes the left side independently, and tests
both the four-term expansion and
\(B_{12}-B_{21}^*\) at every held separation.  Any reduction to
\(2\operatorname{Re}B_{12}\) is a consequence only after that reciprocity
test; it is not built into the measurement.  “Composition-safe” here means
only this algebraic bilinear/additive identity for two distinct fixed vertices
in the declared zero-mean one-excitation finite problem.

Across all 38 representatives, the maximum four-term expansion residual is
\(3.79052\times10^{-15}\), the maximum conjugate-reciprocity residual is
\(3.55445\times10^{-16}\), and the minimum absolute imaginary part of
\(B_{12}\) is \(2.37398\times10^{-4}\).

It does not supply an on-shell action, physical potential, force law, stress
source, backreaction, or a many-body interaction law.

## Honest Cycle216 comparison

At each bright eigenphase the two-source route uses
\(3(L-\mu I)^{-1}\), whereas Cycle216's static comparator is \(3L^+\).
The runner keeps two error notions distinct:

1. the source-specific profile ratio
   \(\|H_\mu\rho-3L^+\rho\|_2/\|3L^+\rho\|_2\); and
2. the relative operator bound \(\mu/(\ell_{\min}-\mu)\) on the complete
   zero-mean subspace.

The first depends on the selected point source.  The second is a uniform bound
on the declared subspace.  Across fixed-neighbour L=3,...,9, and across all
38 held cubic-orbit representatives, the measured source-specific ratio is
below the corresponding operator bound and \(0<\mu<\ell_{\min}\).

At held-out L=9 the fixed-neighbour source-specific ratio is
\(1.36745\times10^{-3}\), while its operator bound is
\(2.12310\times10^{-3}\).  The finite shifted cross-coordinates are explicitly
different from the Cycle216 cross-coordinates.  For example, at separation
\((1,0,0)\) they are approximately \(0.1840188194\) and
\(0.1838162867\), respectively.

At the separately declared \(\mu=0\) mathematical comparator, the two
zero-mean profiles and their pair quadratic pairing agree with Cycle216's
\(3L^+\) block at all 38 held separations.  This equality is only an identity
between the declared zero-mean comparator operators and sources.  It is not an
identity for the active two-reservoir update, gate amplitudes, or eigenstate.
The active selected bright eigenstate has \(\mu>0\), so the zero-shift
comparator is not relabeled as its finite response.

Across the 38 zero-shift checks, the maximum left-profile residual is
\(2.21456\times10^{-16}\), the maximum translated right-profile residual is
\(3.54311\times10^{-16}\), and the maximum pair-bilinear residual is
\(2.22045\times10^{-15}\).

## Endpoint, covariance, zero-mode, and normalization controls

- Setting either supplied local angle to zero reduces the remaining active
  block exactly to the appropriately translated one-reservoir update.  The
  inactive reservoir stays stationary.  This is a supplied theta=0 parameter
  endpoint, not a theorem selecting or deleting a candidate law.
- Setting both angles to zero leaves the complete two-reservoir subspace
  stationary.
- The full pair update and transformed bright eigenstate are checked under all
  24 proper-cubic frames, using a nonaxial separation \((2,1,0)\).
- All 27 pair origins on the L=3 torus form a translated covariant defect
  family.
- Every Cycle216 comparison source has explicit zero-mode subtraction.
- If \(|\Psi\rangle\mapsto c|\Psi\rangle\), then both \(q_i\mapsto cq_i\)
  and \(\phi\mapsto c\phi\).  The normalized two-source tail is invariant
  under that joint scaling and rephasing; neither \(q_i\) is independently
  normalization-invariant.
- The lawful domain requires L>=3, exactly two distinct in-torus reservoir
  positions, two supplied angles, and the one-excitation sector.  Aliased,
  co-located, mistyped, out-of-torus, and wrong-sector fixtures are rejected.

## Supplied structure inventory

Supplied:

1. the Cycle214/215 six-direction field coin, one-edge stream, uniform scalar
   direction, and coin-vertex-stream order;
2. two distinct fixed reservoir M2 vertices, their positions, and equal local
   angle \(\theta\) from the already supplied \(\beta=-0.3\) and
   \(\kappa=0.8\);
3. the conserved one-excitation sector and finite periodic volumes L=3,...,9;
4. the positive shift-invert target
   \(\exp[i\sqrt2\theta/L^{3/2}]\), three returned candidates, positive-phase
   filter, maximum-total-reservoir-squared-norm selection, normalization, and
   real-positive reservoir-sum phase convention;
5. the phase-ratio acceptance window \((0.95,0.98)\), total reservoir
   squared-norm-weight window \((0.44,0.47)\), and positive-phase cutoff
   \(10^{-8}\);
6. fixed-neighbour L=3,...,8 as training sizes and held-out L=9;
7. all 38 held-size proper-cubic orbit representatives listed by the set
   definition above and the independent all-728-vector orbit-partition test;
8. the complex probe coefficients \(\alpha=1+0.5i\) and
   \(\beta=-0.3+0.8i\);
9. the zero-mean comparison convention, Moore-Penrose convention with
   `rcond=1e-11` for the constructed antisymmetric compatibility member, and
   Cycle216's \(3L^+\) comparator; and
10. every numerical tolerance stated by the runner.

Derived on that supplied finite problem:

1. the numerically selected bright eigenpairs and their stationary
   basis-component squared norms;
2. the exact additive two-source shifted profile and explicit uniform
   component;
3. one exactly constructed zero-total-\(q\) antisymmetric \(\lambda=1\)
   member with nonzero local \(q_i\), nonzero field weight, and an explicit
   compatibility residual;
4. extraction of the off-diagonal field response from the bright eigenvalue,
   supplied gate, and supplied free self response;
5. the ordered complex four-term shifted bilinear and conjugate reciprocity;
6. the finite, controlled comparison with Cycle216; and
7. theta=0 endpoint, proper-cubic, complete held-size orbit-partition,
   translation, held-size, zero-mode, normalization, and lawful-domain
   controls.

Not earned or attempted:

1. physical energy, Hamiltonian density, eigenphase-as-rate, clock
   normalization, force, gravity, stress, source mass, or a physical
   interaction potential;
2. any matter Hilbert space or matter/contact dynamics: no matter or contact
   update is implemented, including the Cycle230 contact block;
3. a physical-M2 compiler or intertwiner for the Cycle230 coarse CAR cell;
   there is no whole-compiler claim;
4. a carried or moving source interface, source recoil, radiation reaction,
   retarded selection, or many-excitation closure;
5. co-located-vertex ordering, a general many-source theorem, or a physical
   state-preparation mechanism;
6. a claim outside the tested sizes and separation list; and
7. occurrence, Record formation, a Born rule, axiom change, or audit
   authority.

## Disposition

The fixed-reservoir extension succeeds at exact additive two-source
composition and at a finite shifted bilinear cross-coordinate.  Separately,
one antisymmetric \(\lambda=1\) compatibility member is constructed with
zero total \(q\) but nonzero local \(q_i\) and field content.  No generic
spectral-splitting conclusion is drawn.

This is not a route-independent obstruction and creates no axiom pressure.
Two concrete, nonexclusive next tests are a matter-controlled reservoir
interface and a controlled symmetry-breaking local parameter.  Either probe
could test how the antisymmetric compatibility member, reciprocity, and
composition change without importing a host-selected source schedule; moving,
many-source, and collision-aware routes remain open rather than being ruled
out here.

No axiom, foundation, Qualification, primitive, registry, policy, queue, or
audit-status surface was edited.
