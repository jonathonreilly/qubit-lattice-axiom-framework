# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed **B1 = FAIL (bounded)** reading is correct after narrowing the proved
scope to smooth, globally defined generators on isolated simple (or preserved
band-diagonal) free Bloch bands, and—on the local-smearing route—to cubic
Morse dispersions and regular constraint structure functions.  The report does
not prove its broadest formulations of Theorem 0, a universal Fock-space
soccer-ball theorem, or the exclusion of all DSR/κ-Poincaré constructions.

Both worker scripts reran to byte-for-byte agreement with their stored `.out`
files.  `B1_referee_checks.py` supplies a separate symbolic path for the
material corrections and for Theorem D's exact nearest-neighbour collision.

## 1. Theorem 0

**Conditionally correct, but not at the stated “any operator” generality.**
The kernel/principal-symbol argument at `B1_report.md:55-60` works if (K)
maps (C^\infty(T^d)) continuously to distributions (or belongs to an
appropriate differential/pseudodifferential class), the displayed commutators
hold as operator/distribution identities on a common invariant domain, and the
joint differentials of ((\omega,p_1,\ldots,p_d)) span almost everywhere.
After removing the part supported on equal joint spectral fibres, the diagonal
kernel has order at most one.  For a symmetric generator the proper form is

\[
K=\tfrac12\{V^a,i\partial_a\}+M_\phi+C,
\qquad [C,H]=[C,P_c]=0,
\]

not merely (V\cdot\partial+\phi+C).  In a scalar band (M_\phi) is itself
already part of the commutant.  These missing analytic/domain hypotheses matter:
an arbitrary unbounded Hilbert-space operator need not possess the distribution
kernel used in the proof.

The exclusion of ordinary finite higher moments is correct under those
hypotheses (`B1_report.md:61`).  The stronger sentence that *every* quasi-local
(K) is a first moment (`B1_report.md:62-63`) is justified only after defining
quasi-locality strongly enough that the components of (V(k)) have summable
Fourier coefficients.  Then, on a scalar band, those coefficients define
translation-covariant one-body charge densities and the claim is essentially a
Fourier reconstruction.  It is not established for arbitrary many-body or
number-changing generators.  In particular, the assertion that Bogoliubov
parts commute with (H,P) (`B1_report.md:64`) is false in general: a pairing
term (a_k^\dagger a_{-k}^\dagger) has energy commutator proportional to
\(\omega(k)+\omega(-k)\), not zero.  Such terms are outside the stated
one-particle (L^2(T^d)) theorem.

## 2. Theorem U

**Confirmed, with the domain qualification already identified by the M1
referee.**  The (A_\pm=H\pm P_b/\sqrt\beta) calculation and the norm-growth
contradiction are correct and use no first-moment representation of (K)
(`B1_report.md:67-71`; `C4_M1_report.md:118-127`).  Thus its essential
generality claim is right.

It does, however, require a (K)-invariant/reducing sector and a strong or
integrated commutator relation—e.g. (A_\pm\in C^1(K)), or a common invariant
analytic core sufficient to exponentiate.  Self-adjointness plus a merely formal
core commutator is not enough.  This is precisely why M1 supplied sector
invariance, essential self-adjointness and core preservation, and why its
referee narrowed the microscopic class (`C4_M1_referee.md:5-7`).  Subject to
that correction, bounded (H,P), β>0 and exact integrated Poincaré closure
force (H=P_b=0), for any (K).

## 3. Theorem S

**Confirmed on the infinite lattice, with convergence and convention
qualifications.**  If
(T_jh(x)T_j^{-1}=h(x+j)), then reindexing gives

\[
T_j\Big(\sum_x x_bh(x)\Big)T_j^{-1}=K_b-j_bH.
\]

The same covariance holds for
(\tfrac12\{X_b,H\}), so their difference commutes with all translations.  On
one scalar band it is multiplication by (a_b(k)), and the derivative
coefficient is therefore (V_b^a=\omega\delta_b^a)
(`B1_report.md:73-80`).  Reversing the convention for (T_j) reverses both
signs and changes nothing substantive.

“Local or not” is too broad: the sums, first moments and reindexing must exist on
a common domain (or in a controlled weak/quasi-local limit).  A finite periodic
ring also has a branch-cut boundary term.  For finite bands the translation-
invariant remainder may be a matrix multiplier and Berry/degeneracy blocks need
separate handling.  None of these qualifications changes the scalar isolated-
band conclusion.  Linearity of the lapse then makes (H[N=x_b]) this first
moment; gauging a different (Q_V) means adding a different constraint, as the
report correctly says.  The identity alone does not prove that no enlarged
constraint theory can work.

## 4. Theorem R

**The fixed-point lemma is true.**  It is a standard consequence of Borel's
theorem: for a circle action on a closed aspherical manifold, an orbit circle
injects into the fundamental group; hence an effective nontrivial action cannot
have a fixed orbit.  See Cappell–Weinberger–Yan's statement of the Borel result
([arXiv:1108.2321, lines 10-13](https://arxiv.org/abs/1108.2321)).  Coordinate
rotation on (T^d) is fixed-point-free, so it is an example supporting—not
contradicting—the lemma.

The worker's independent averaging proof at `B1_report.md:123-129` is also
sound after making two implicit steps explicit.  A fixed point makes every
orbit loop null-homotopic, so the action lifts to an (S^1)-action on
\(\mathbb R^d\) commuting with deck translations.  The averaged lift descends
to a degree-one map homotopic to the identity and is constant on nonfixed
orbits.  Off the fixed set its rank is at most (d-1); on the fixed set the map
is the identity, while the fixed set has codimension at least two for a
nontrivial effective circle action.  Sard applied to the first part, plus the
measure-zero image of the fixed set, contradicts degree-one surjectivity.

The applications need the following qualifications.

- In (d=3), complete smooth vector fields representing undeformed
  \(\mathfrak{so}(3)\) integrate to a compact rotation action.  The IR
  Poincaré chart (Dp(0)) nonsingular makes (k=0) a fixed point and makes the
  circle subgroup nontrivial.  Thus R1 is correct for the intended target, but
  “no condition on (P)” at `B1_report.md:138` is too strong.
- In (d=2), the analytic \(\mathfrak{so}(2,1)\) argument is valid.  The
  central (2\pi)-rotation fixes the open orbit of the rest point; analyticity
  makes it globally the identity, yielding a nontrivial circle action with a
  fixed point (`B1_report.md:139-141`).  Smoothness alone does not justify this
  identity-continuation step.
- The Poincaré–Hopf route is valid when (p^{-1}(0)) is isolated, but the proof
  at `B1_report.md:142-148` is compressed.  From (Dp\,W=Jp), the flow preserves
  \(|p|\) and rotates its phase.  A sufficiently small regular sublevel
  component about an isolated zero has no holes (a hole would force another
  zero of a tangent vector field), hence is a disk and the zero has index
  (+1).  Poincaré–Hopf on (T^2) then gives the contradiction.  The sampled
  “fold cells” in `b1_2d3d.out:17-22` are illustrative, not a proof at exact
  fold points.

Accordingly, Theorem R excludes a **global smooth action on the entire compact
Brillouin torus** of an undeformed Lorentz/rotation group having the usual fixed
rest point.  It does not exclude patchwise actions, punctured domains, singular
folds, band permutations/touchings, or deformations of the Lorentz subalgebra
itself.  Bisio–D'Ariano–Perinotti explicitly work on four invariant regions up
to null sets and remove a Jacobian/fold set
([arXiv:1503.01017, lines 308-380](https://arxiv.org/html/1503.01017v3)); that
is an evasion outside the theorem, not evidence for the unqualified phrase
“DSR/κ-Poincaré is impossible” at `B1_report.md:154-162`.

## 5. One-dimensional results

**Mostly confirmed, with two material overstatements.**  For a smooth even
periodic (V) and an even dispersion ω that is strictly monotone on
\([0,\pi]\) with nondegenerate endpoints,

\[
P=V\omega',\qquad F=V(V\omega')'
\]

is even and descends smoothly to a function of (H=\omega).  The Casimir and
the KG identity in `B1_report.md:85-94` are correct and the stored script
reproduces exactly.  The equivalence (V(0)=\omega(0)) additionally uses the
standard relativistic IR normalization and a choice of sign.

The orbit sum rule is exact:

\[
\int F\,dH=\int P\,P'\,dk=\tfrac12[P^2]_{0}^{\pi}=0.
\]

With positive Lorentzian IR value, it forces (F<0) somewhere.  Negativity
near the upper band edge additionally uses a nondegenerate maximum and regular
finite-order behavior of (V); it does not follow from the integral alone.
The specific “MS-type” choice (V=\omega\cos(k/2)) is not (C^1) on the
identified Brillouin circle: its derivatives at ±π have opposite signs.
`B1_referee_checks.py:35-43` gives the exact check and the smooth periodic
replacement (V=\omega(1+\cos k)).

The stored two-particle examples do show non-additivity for the KG first moment
(`b1_1d.out:29-33`), but they do not prove universal Fock-space failure.  A
counterexample to that wording is

\[
\omega=m+A(1-\cos k),\quad V=v,\quad
P=Av\sin k,\quad F=v^2(m+A-H).
\]

On a fixed-ℕ sector, \(\sum_iF_i=v^2[N(m+A)-H_{\rm tot}]\), so the additive
lift closes after admitting the central particle number.  This is verified at
`B1_referee_checks.py:24-32`.  Generic nonlinear (F), including the worker's
KG example, has the soccer-ball/non-additivity problem; closure on the full
Fock space using only (H_{\rm tot},P_{\rm tot}) remains unproved here as a
universal statement.  Exact undeformed Poincaré still requires a singular
(V) at a bounded band edge, as `B1_report.md:107` states.

## 6. Theorem D

**Confirmed in its stated Morse, single-valued-closure scope.**  Theorem S and
(i[K_a,H]=-P_a) give (P=\nabla u), and then
(i[K_a,P_b]=-\omega\,\partial_a\partial_bu)
(`B1_report.md:174-178`).  At any critical point (s), cubic partners (Rs)
have the same ((H,P)=(\omega(s),0)).  If the bracket is a single-valued matrix
(F_{ab}(H,P)), then

\[
\operatorname{Hess}u(s)=\operatorname{Hess}u(Rs)
=R\operatorname{Hess}u(s)R^T
\]

for every cubic rotation (R).  A symmetric matrix invariant under the cubic
group is proportional to the identity.  Thus every Morse critical point has
index (0) or (d), contradicting the Morse inequalities
(m_1\ge b_1(T^d)=d).  The phrase “off the O-fixed points” is unnecessary.
The exact nearest-neighbour (d=2) collision is independently reproduced at
`B1_referee_checks.py:45-56`; the random scans in `b1_2d3d.out:24-36` are only
corroboration.

The theorem does not cover non-Morse bands, band labels admitted as extra
generators, touching/degenerate bands, singular or multivalued structure
functions, or closure on an enlarged tower of charges.  These qualifications
must be part of the headline scope, not only the later open-items list
(`B1_report.md:37-43`).

## 7. Gravity and observations

**Gravity: correct only in the regular perturbative setting.**  C3 establishes
that, at flat background and matter-bilinear order, regular field-dependent
structure functions cannot contribute to that coefficient
(`RC_C3_report.md:25-41`; `RC_C3_referee.md:5-7`).  Hence the Killing sector has
c-number structure constants within the same regular constraint set.  This
does not exclude singular background dependence, changed leading generators,
or extra constraints (Q_V), all of which the C3 referee left outside scope.

The Bojowald statement needs correction.  For **holonomy corrections only**,
\(\beta=\cos(2\delta K_\varphi)\), so (K_\varphi=0) gives β=1; the
diffeomorphism brackets remain undeformed.  But Bojowald–Paily also have
inverse-triad deformations such as \(\beta=\bar\alpha^2\), which need not equal
one merely because the extrinsic curvature vanishes
([arXiv:1112.1899, lines 85-91 and 127-136](https://arxiv.org/html/1112.1899v1)).
Thus `B1_report.md:211-219` rules out the displayed holonomy-only escape on the
flat (K=0) background, not every “Bojowald-type” deformation.

**Observations: the stated tree-level comparison is correct.**  For the axis
dispersion, (E^2=k^2-a^2k^4/12+O(k^6)), so in the convention used by the
quoted time-of-flight analyses (E_{\rm QG,2}=\sqrt{12}/a)
(`B1_referee_checks.py:58-62`).  Evenness/inversion symmetry removes the linear
term.  The cited LHAASO limits (E_{\rm QG,1}>10E_{\rm Pl}) and
(E_{\rm QG,2}>6\times10^{-8}E_{\rm Pl}) are accurately reported
([LHAASO, arXiv:2402.06009](https://arxiv.org/abs/2402.06009)), as is the
GW170817 speed interval at the (10^{-15}) level
([LIGO/Virgo/Fermi/INTEGRAL, arXiv:1710.05834](https://arxiv.org/abs/1710.05834)).
At (a=\ell_{\rm Pl}), the quadratic dispersion easily passes those direct
time-of-flight bounds.  This is not an observational viability theorem for the
whole lattice theory: it assumes the relevant excitation has that even cubic
dispersion and does not address loop-induced low-energy Lorentz violation,
which the report itself leaves to other lanes (`B1_report.md:229-238`).

## 8. Fixed verdict

**FAIL (bounded) is correct, but the bound must be stated more narrowly than
`B1_report.md:26`.**  The fixed criterion is disjunctive
(`TESTS.md:1868-1871`).  For regular affine-lapse gravity on a smooth isolated
cubic Morse band, Theorem S forces the first moment and Theorem D forbids
single-valued closure on ((H,P)).  Independently, Theorem U forbids exact
undeformed Poincaré closure on any bounded (K)-invariant sector with an
integrable strong commutator, and Theorem R forbids a global smooth DSR-type
undeformed Lorentz action on the whole Brillouin torus.  Theorem 0 is not needed
for this verdict.

This is a test-setting theorem, not an axiom-level theorem: the four axioms do
not select a Hamiltonian, kinetic branch or scalar/finite-band carrier
(`MINIMAL_AXIOMS_2026-06-29.md:114-130`).  Open cases include fully deformed
non-first-moment algebras with extra constraints, patchwise/singular actions,
non-Morse or touching bands, interacting/composite matter, and unbounded
sectors.

## No-go discipline check

- **N1:** six materially different attacks were checked: arbitrary (K) under
  exact Poincaré closure; higher-moment/quasi-local classification; global DSR
  rotations; local affine lapse smearing; 1D nonlinear/Fock lifting; and
  patchwise/touching/singular/enlarged-constraint escapes.  The last class
  remains open and is excluded from the corrected no-go.
- **N2:** the independent load-bearing walls are bounded integrated closure
  (U), global smooth compact momentum topology (R), and regular local-smearing
  plus Morse cubicity (S+D).  Theorem 0 is not an additional independent wall.
- **N3:** hidden conditions found and promoted are operator domains,
  (K)-sector invariance, summability of first moments, a nondegenerate fixed
  rest point, analyticity for R2, isolated zeros for R3, Morse regularity for D,
  and regular perturbative structure functions for C3.
- **N4:** M1 T2 matches the bounded-sector residual; C3 matches only the
  regular flat-background matter-bilinear residual.  K2's broader compact-shell
  discussion is not needed and cannot enlarge B1's scope.
- **N5:** one-particle, fixed-ℕ, full-Fock, bandwise and entire-BZ statements
  were separated.  The universal Fock and universal DSR wording was narrowed.
- **N6:** patchwise DSR and adding (Q_V) constraints are genuine alternative
  structures, not “new axiom required” conclusions; they remain outside the
  tested gravity structure.
- **N7:** the strongest steelman is a fully deformed, non-first-moment algebra
  on preserved/touching bands, coupled to an enlarged constraint tower or
  defined on invariant BZ patches.  B1 does not close that route.
- **N8:** I1 and M1 explicitly left non-first-moment and embedded/touching
  sectors open (`C4_I1_referee.md:15-21`; `C4_M1_referee.md:13-15`).  B1 closes
  only the undeformed/global and regular-smearing Morse subsets.  The corrected
  bounded verdict respects those earlier openings.

## Strongest correct statement

For free matter on a smooth isolated simple Bloch band in (d=2,3), a regular
Hamiltonian-constraint smearing linear in an affine lapse necessarily generates
the first moment (K_b=\tfrac12\{X_b,H\}+a_b(k)); if
(u=\omega^2/2) is cubic-invariant and Morse, closure of
([K_a,P_b]) as a single-valued function of only ((H,P)) is impossible,
because cubic-related critical points would force every critical Hessian to be
isotropic while (T^d) requires index-one Morse critical points.  More
generally, no self-adjoint generator of any form can realize the exact
undeformed positive-β Poincaré brackets on a (K)-invariant sector where
(H,P) are bounded and the commutators exponentiate, and no nontrivial smooth
global undeformed rotation/Lorentz action with the usual fixed rest point can
act on the entire Brillouin torus.  These results establish the fixed **FAIL
(bounded)** reading, but do not exclude patchwise or singular DSR actions,
fully deformed non-first-moment algebras with extra constraints, non-Morse or
touching bands, interacting/composite matter, or unbounded sectors.
