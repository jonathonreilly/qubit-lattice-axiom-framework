# VERDICT: NOT CONFIRMED

The exact examples and a useful conditional no-go survive, but the advertised
quantifier over **all** local BV completions does not.  The decisive gap is in
the claimed invariant reduction: the displayed first-order generator is only
the matter-to-matter block, not the most general field-dependent generator on
the combined gravity--matter complex.  T1 also has a false `c=0` branch as
stated.  Consequently F1 does not prove the fixed-reading FAIL for its stated
class, although it proves a narrower failure after an additional
number-preserving/block-diagonal hypothesis and the intended `e(4)` value
`c=1` are imposed.

## 1. The Killing-sector projection

**What is correct.**  On the *fixed* free BV complex `(h,phi,C)` used in the
report, evaluation on an affine Killing ghost gives `DC=0`; after setting
`h=h*=C*=0`, the only possible `phi* phi` contribution from an `s0`-exact
functional is an equation-of-motion-trivial term `phi* mu A phi`.  Thus the
bookkeeping in `F1_report.md:92-105` does define a necessary cohomological
test, and ordinary second-order counterterms, seagulls, field redefinitions,
and parity-preserving nonlinear generator/open-algebra terms do not alter that
coefficient (`F1_report.md:106-113`).  In particular, terms at least quadratic
in matter cannot descend to the selected bilinear coefficient.

**The universal claim is not proved.**  The allegedly general linearized
matter generator is specialized at `F1_report.md:121` to
`phi* X(C) phi`.  A general local field-dependent first-order generator on the
combined field space can also contain

`a_U = phi* U(C) h`,  `a_V = h* V(C) phi`.

Their antibracket has the surviving matter block

`P~(a_U,a_V) = phi* [U(C1)V(C2)-U(C2)V(C1)] phi`,

which is neither killed by `h=0` nor automatically of the form `phi* mu A
phi`.  The report supplies no cocycle/classification argument showing that all
such local off-diagonal intertwiners are absent or trivial.  They are excluded
if one adds a matter-parity/number grading, forbids quadratic gravity--matter
mixing, or assumes the Killing representation is block diagonal, but none of
those is in H1--H6 (`F1_report.md:259-265`).  This is exactly an unclosed
field-dependent-generator route, so `F1_report.md:105-128` does not establish
invariance for every completion claimed at `F1_report.md:30-36`.  Adding a
Stueckelberg pair changes `s0` itself and explicitly destroys the test, as the
report concedes at `F1_report.md:226`.

This is a proof gap, not an exhibited completion: an allowed off-diagonal
cocycle must still satisfy the free symmetry/intertwining equations.  But the
fixed FAIL requires those possibilities to be excluded, not merely left
unclassified (`TESTS.md:2249-2252`).

## 2. Killing fields and the first-moment step

The leading-homogeneous-degree argument is correct for **polynomial**
solutions.  Since the first nonzero moment of an IR-normalized local gauge map
is the continuum symmetrized gradient, the top homogeneous part of a
polynomial kernel element obeys the continuum Killing equation; hence no
degree above one survives, and the value/first moment make precisely the ten
affine fields exact kernel elements (`F1_report.md:73-85`).  The rerun of
`f1_killing_poly.py:58-84` reproduces dimensions 6 and 10 for the tested
stencils (`f1_killing_poly.out:1-16`).

This is not completeness of the full kernel for an arbitrary local gauge map.
Positive-dimensional characteristic zero sets can give infinitely many
non-polynomial solutions; the scripts establish isolated extra zeros only for
their special factorized stencils (`f1_killing_poly.py:64-84`).  The report
later adds the needed finite-zero condition in H3 and separately excludes
infinite-dimensional Killing kernels (`F1_report.md:262-263`,
`F1_report.md:271`).  Nor does the polynomial-kernel count by itself prove the
full jet-cohomology assertion at `F1_report.md:88`; fortunately, restriction
to the ten explicit affine ghosts is enough for a necessary test.

For a number-preserving linear matter term `phi* X(C) phi`, locality does force
the affine-ghost evaluation to be `X(a)=a.F` and
`X(omega)=omega x.F+Y`, with the orbital coefficient the first moment of the
same translation convolution (`F1_report.md:121-126`).  That step is sound
with the stated summable-first-moment qualification and agrees with the
qualified Theorem S (`C4_B1_referee.md:9`).  It does not address the omitted
off-diagonal generator blocks above.

## 3. T1, the exact defects, and SLAC

On a connected regular shell patch where `f != 0`, the first two steps are
correct: `{Jf}` spans `f^perp`, so tangency gives `TS0=f^perp`, while closure
gives `d(f-ck)|TS0=0` and hence `f=ck+b` (`F1_report.md:143-145`).  For
`c != 0`, the shell is locally contained in `(ck+b)^2=r`.  A nonzero finite
Fourier sum cannot vanish on that full complex quadric: choose a null
direction outside the finitely many frequency-collision hyperplanes and a
base point whose shifted radius vector is orthogonal to it; restriction to
the resulting line is a sum of exponentials with distinct exponents.  The
worker's phrase “for every null `v`” at `F1_report.md:149` needs this
orthogonality/base-point qualification, but the argument is repairable.  An
exact separating null direction is recorded at
`F1_referee_checks.py:65-72`.

The `c=0` conclusion at `F1_report.md:151` is false as written.  Take

`A=(exp(i k0)-1)(2+cos k1)`, `S0={k0=0}`, `f=(1,0,0,0)`, `c=0`.

Then all six tangency and closure equations vanish on the regular irreducible
component `S0`, while `A` depends on both `k0` and `k1`.
`F1_referee_checks.py:49-62` verifies this exactly.  The repair is to exclude
one-directional **factors/components**, not merely actions that globally
depend on one linear combination.  This defect does not affect the intended
continuum `e(4)` target, whose IR bracket fixes `c=1`, but it invalidates the
claim that T1 covers every `c` (`F1_report.md:263-274`).

Accordingly T1 improves K2 only on the overlap with: a regular irreducible
scalar/simple shell, scalar nonzero translation action, the first-moment
rotation, and `c != 0`.  It removes K2's compact-real-shell and Wick-reality
assumptions, but it does not supersede K2 for matrix/degenerate shells or
arbitrary rotation vector fields; K2's referee already rejected that broader
scope (`C4_K2_referee.md:11`).

The exact controls are confirmed.  Independent symbolic checks give

- scalar: `(cos k_rho-1)(J sin k)_rho`;
- fermion: `(cos 2k_rho-1)(J f)_rho`;
- SLAC interior: zero because `Df=I`.

See `F1_referee_checks.py:24-46` and the reproduced worker values in
`f1_closure_theorem.out:1-18`.  On the periodic Brillouin torus the sawtooth
derivative also contains the zone-face delta term, so “SLAC zero defect” is
only the open-zone control; the face obstruction stated at
`F1_report.md:222-225` remains.

## 4. The tower

The exact rank calculation reruns as stored: the spans have dimensions
`2,4,6,8,10,12,14` through six commutators for both `sin k` and
`sin(2k)/2` (`f1_tower.out:1-4`).  Those finite ranks alone do not prove an
infinite tower, but the period argument does under its stated Hamiltonian
single-band hypotheses.  A finite-dimensional `W`-invariant function space
would restrict along every orbit to exponential polynomials with a fixed
finite exponent set.  A continuum of orbit periods therefore kills every
nonzero exponent on an open set, contradicting `Wf ~= Jk`.  The rerun also
reproduces the varying periods (`f1_tower.out:6-14`), and the use of the
no-fixed-point circle-action lemma is consistent with its qualified referee
statement (`C4_B1_referee.md:11`).

Thus the infinite-dimensional generated symmetry algebra is established for
the explicit K2/C3 symbols and for analytic Hamiltonian single bands with a
nondegenerate elliptic IR point, assuming the gauge map has finite-dimensional
Killing algebra (`F1_report.md:187-204`).  It is not proved for a general
strictly local symbol on a complex Z4 shell; the report itself calls that case
suggested and lists it as uncovered (`F1_report.md:204`,
`F1_report.md:273`).  The further statement that every independent generator
requires a new gauge field is standard for an irreducible gauging with no
unused gauge sector, but is not a proof against finite auxiliary/off-diagonal
realizations.  Therefore the tower cannot rescue the advertised all-finite-
content quantifier.

## 5. Stueckelberg escape

Confirmed.  With `delta pi=-xi`, the combination `h+Dpi` is invariant, and an
arbitrary local unitary-gauge functional can be Stueckelbergized.  The Ward
identity is then

`D^T (delta Gamma/delta h) - delta Gamma/delta pi = 0`,

so the compensator response absorbs the identity for arbitrary shear
coefficients.  It enforces neither `mu_E=mu_T2` nor either value separately,
exactly as stated at `F1_report.md:226`.  This is a finite-content local
trivialization, not a PASS because the required mass-fixing Ward consequence
is absent (`TESTS.md:2250`).  It also shows why the fixed-complex projection
cannot be advertised as invariant after arbitrary field-content extension.

## 6. Fixed reading and combination with F2

As submitted, F1 has not proved either FAIL disjunct for its stated universal
class: the off-diagonal finite-field generator route is open, the general Z4
tower is only suggested, and the source's N1--N8 section labels
“phi-dependent generators” closed without testing that route; its N4 is not a
prior-residual matching table and its N5 is only an assertion
(`F1_report.md:276-308`).  Under the fixed rule, that is **INCONCLUSIVE**, not
FAIL (`TESTS.md:2249-2252`).  A defensible narrower FAIL is available after
adding a fixed-field, matter-number/parity-preserving, block-diagonal Killing
representation, a regular irreducible scalar/simple shell, and the intended
`c=1` algebra.  F2 is consistent with that narrower result: its one-jet proof
finds the same matter-momentum cosine obstruction for the K2 scalar
(`F2_report_unrefereed.md:151-173`), but it explicitly assumes a graded
Noether expansion and fixed `h,phi` content (`F2_report_unrefereed.md:190-202`).
It therefore does not close F1's omitted off-diagonal/auxiliary-field route.
Moreover only the unrefereed F2 report, not its nine scripts, is present in
this packet, so its claimed all-range extension cannot serve as an independent
executable certificate here.

**No-go-discipline result: FAIL at the advertised scope.**  N1/N7 fail because
the off-diagonal finite-field intertwiner route is concrete and unclosed; N3
fails because block diagonality/matter grading and the `c != 0` component
condition are hidden hypotheses; N4 does not match each cited prior result to
the present all-completions residual; N5 supplies no per-mode/per-block/global
execution record.  N2 correctly collapses several purported routes into the
same projection wall, N6 correctly treats compensators/perfect actions as
changed realizations rather than new axioms, and N8's prior C3/K2/B1 results
support only their already-qualified subclasses.  The gate therefore permits
the narrowed conditional statement below, not the submitted universal no-go.

**Strongest correct statement:** For a fixed gravity--matter BV complex whose Killing action is block diagonal and matter-number/parity preserving, with a regular irreducible scalar/simple complex shell, a nonzero scalar translation symbol, a local IR-normalized gauge map, and the continuum `e(4)` bracket `c=1`, the affine-Killing projection is invariant under local second-order counterterms, diagonal field-dependent generators, open-algebra terms, field redefinitions, and seagulls; locality fixes the rotation's orbital part to the first moment of the translation, and tangency plus closure would force the shell into a complex quadric, which no nonzero finite Fourier kinetic symbol can contain.  The K2 scalar and naive/staggered-fermion cosine defects and the interior SLAC control are exact, and their Hamiltonian generated symmetry algebra is infinite-dimensional under the stated analytic single-band assumptions.  Stueckelberg fields can trivialize the class locally but make the Ward identity tautological and fix neither shear coefficient.  This supports a narrow fixed-field/graded **FAIL**, corroborated by F2 for the K2 scalar, but it does not establish F1's claimed FAIL over all local finite-field BV completions; that broader reading remains **INCONCLUSIVE**.
