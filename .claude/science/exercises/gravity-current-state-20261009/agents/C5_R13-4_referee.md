# VERDICT: CONFIRMED WITH CORRECTIONS

The three campaign readings survive: **(i) PHYSICALLY NON-LOCAL in the
locality-preserving extension class \(\mathcal E\); (ii) OPEN; (iii) numerical
control only.**  The main corrections are that \(56e^2G(r)\) is a selected
vacuum-to-one-pair matrix element rather than the full fermion-space operator
norm, the proposed \(N_x\) needs a domain qualification at \(\phi_x=0\), and
the Klein--Gordon kernel used for part (iii) is not the actual commutator of
R7-1's number-conserving one-band CAR law.  None of those corrections removes
the power-law tail.

## 1. Lemma Q

**Confirmed under the report's inherited flat/group-averaged inner product.**
For the closed physical subspace of invariant horizontal forms, the adjoint of
the restricted \(Q\) is the orthogonal compression
\(Q^\sharp=P_hQ^\dagger\).  Cartan's relation makes \(Q\) preserve basic
forms.  If \(\omega\) is basic, then
\(\iota_tQ^\dagger\omega=X_t\omega\) and
\(\iota_r\iota_tQ^\dagger\omega=0\), so the vertical part of
\(Q^\dagger\omega\) has exactly the displayed one-vertical decomposition.
For horizontal \(\beta\), \(P_h(u_s\cdot\psi^\dagger)\beta=0\), and expanding
\(Q(u_s\cdot\psi^\dagger)\beta\) gives
\(\{Q,u_s\cdot\psi^\dagger\}=X_s^\dagger\).  These identities give

\[
H_q=P_hH_{\rm flat}-\frac12P_hX^\dagger g^{-1}X
\]

on basic forms, as claimed in `R13-4_report.md:82-97`.

The required rerun reproduces residuals \(7.0\times10^{-16}\),
\(8.6\times10^{-16}\), \(3.5\times10^{-16}\), and
\(1.4\times10^{-17}\), with the nontrivial controls failing and the intersite
term nonzero (`scripts/r134_oneill_fd.out:1-8`).  One implementation caveat is
that the runner's formula `1-u^\flat g^{-1}\iota_u` is not the full projector
on arbitrary forms with two or more vertical occupations
(`scripts/r134_oneill_fd.py:68-74`).  It is valid on every intermediate to
which this test applies because the algebra above bounds those intermediates
to at most one vertical occupation; it must not be reused as a general
multi-vertical projector.

## 2. Theorem NL and class \(\mathcal E\)

**The no-go is confirmed, with a coefficient and domain correction.**  Pointwise
\(W_x=\operatorname{span}(\phi_x,J\phi_x)^\perp\) is \(J\)-invariant and its
projector annihilates both \(\phi_x\) and \(J\phi_x\).  Therefore
\(N_x=\psi_x^\dagger P_{W_x}\psi_x\) commutes with every \(\iota_s\) and
\(\iota_s^\dagger\), hence with \(P_h\); the supplied Fock rerun confirms this
to \(4.4\times10^{-16}\) (`scripts/r134_nl_fock.out:1-2`).  For separated
sites, the local/box part contributes zero/super-polynomially small terms, and
the pair term gives

\[
 [[H_q,N_x],N_y]
 =2P_hg^{-1}_{xy}
   (X_x^{W\dagger}X_y^W+X_y^{W\dagger}X_x^W)P_h,
\]

as in `R13-4_report.md:115-130`.

The report's \(56e^2g^{-1}_{xy}\) is exactly the matrix element between the
normalized vacuum-plus-one-pair states: \(\|X^{W\dagger}|0\rangle\|^2=28e^2\)
for the 14-dimensional \(W\).  It is **not** the full operator norm claimed in
`R13-4_report.md:228` and mislabeled in `scripts/r134_green.py:53-55`.  Reducing
the seven independent \(J\)-pairs per site to two spin-\(7/2\) representations
gives instead

\[
 \big\|[[H_q,N_x],N_y]\big\|
 =213.897751074\,e^2 g^{-1}_{xy}
\]

at fixed nonzero endpoint fields on the horizontal pair sector.  The independent
calculation and the retained \(56\) matrix element are in
`R13-4_referee_checks.py:75-93,128-137` and
`R13-4_referee_checks.out:5-7`.  Thus the numerical correction strengthens the
tail.

The projector \(P_{W_x}\) is undefined at \(\phi_x=0\) and discontinuous under
an arbitrary definition there.  The stated matrix elements are legitimate on
a core of bosonic wavefunctions supported away from zero, and their supremum
is approached as that support shrinks toward zero; it is not attained at zero.
If a globally smooth bounded local observable is demanded, replace
\(P_W\) by
\(F(\phi)=\frac{|\phi|^2}{1+|\phi|^2}P_W\).  Then
\(FJ\phi=F\phi=0\), so the horizontality argument is unchanged, while the
double commutator acquires only the nonzero local factors \(f_xf_y\).  Keeping
the endpoint radii fixed and sending all intermediate site potentials to zero
still gives a constant multiple of \(1/r\).  The exact \(56G(r)\) supremum is
therefore specific to the nonsmooth projector, but the power-law obstruction
is not.

For the Green-function comparison, the entrywise resolvent monotonicity is
correct for a Dirichlet exhaustion or the transient infinite cubic lattice:
\(0\le(\Delta+V)^{-1}_{xy}\le G(x-y)\), with pointwise convergence to \(G\)
as \(V\downarrow0\).  The report should state that infrared convention;
on a finite periodic torus the zero mode must first be removed or gauge-fixed.
The rerun reproduces \(4\pi rG(r)=1.00006\) at \(r=64\)
(`scripts/r134_green.out:1-9`).

Class \(\mathcal E\) is a legitimate, necessary scope for the fixed reading:
it requires the BF law's own local gauge-invariant observables to remain local
under the extension (`R13-4_report.md:53-55`).  A finite-range extended
Hamiltonian and local representatives would make the first separated double
commutator vanish identically; a super-polynomially quasi-local decomposition
would make it super-polynomial.  The displayed \(1/r\) matrix element
contradicts either.  The result does not exclude a duality that deliberately
maps these observables to nonlocal operators, nor an extension with new
physical particles.  R12-6 is the latter: its \((\sigma,\eta)\) completion is
local/quasi-local but adds two real \(\sigma\) bosons and one fermionic mode to
the physical spectrum (`C5_R12-6_report.md:129-150`), so it is not an extension
with the same physical content.

No-go attacks considered were: quotient-measure change, smoothing/domain of
\(N_x\), infrared/gauge-zero-mode treatment, screening and finite-energy
states, the R12-6 auxiliary-field localization, and locality-changing dualities.
They narrow the statement to \(\mathcal E\) and to an operator-level/core
claim, but none removes the power law there.  Ordinary Coulomb-gauge QED is the
relevant steelman: it localizes a density--density Gauss-law term, whereas the
surviving BF term transfers a neutral fermion pair and is detected by a local
gauge-invariant observable.

## 3. Measure and metric conventions

The exact Lemma-Q formula belongs to the inherited flat measure after group
averaging, the convention explicitly fixed in `R13-4_report.md:45-51`.  With
the Riemannian quotient-volume measure instead, the adjoint gains a
mean-curvature/interior-product term.  Its anticommutator with \(Q\) is at most
fermion-bilinear (plus a first-order bosonic term), so it does not remove or
cancel the four-fermion vacuum-to-pair transfer matrix element.  Accordingly,
the **no-go is measure-robust**, but the displayed equality for the entire
Hamiltonian and double commutator should not be quoted unchanged across
measure conventions.  “Quotient metric Hamiltonian” is therefore too
ambiguous unless the measure is stated alongside it.

The zero-fermion reduction is exact: the four-fermion term vanishes and the
ambient Gauss-law formulation supplies the usual constraint-solving
description (`R13-4_report.md:109-113`).  For the actual box curves this is a
quasi-local, not finite-range, extension.  The report checked free propagation
but did not prove the interacting unbounded-CCR Lieb--Robinson estimate, so
the strongest fully established wording is **bosonic sector: exact
constraint-solving/quasi-local extension; registered LOCAL-EQUIVALENT at the
free commutator level**, rather than an all-interaction light-cone theorem.

## 4. Lemma V and the box leakage

**Lemma V is correct.**  Oddness plus \(2\pi\)-periodicity gives \(s(\pi)=0\).
Applying the mean-value theorem to
\(E(k)=\sqrt{m^2+s(k)^2}\) on \([b,\pi]\) gives

\[
v_{\max}\ge \frac{\sqrt{m^2+b^2}-m}{\pi-b},\qquad
b_*(m)=\frac{\pi(2m+\pi)}{2(m+\pi)}.
\]

The independent thresholds are \(b_*(0)=1.57079633\),
\(b_*(0.3)=1.70772099\), and \(b_*(0.5)=1.78647069\)
(`R13-4_referee_checks.out:1-4`).  Rerunning `r134_cone.py` reproduces
\(v_{\max}=4.1161\) for \(b=2\), \(12.4157\) for \(b=2.6\), and \(4.5691\)
for the quoted Wilson-box Dirac law (`scripts/r134_cone.out:1-11`).

A narrower box is not by itself sufficient.  The worker's original blended
profile still has \(v_{\max}=2.307809\) at \(b=1.4\); its own output already
shows this (`scripts/r134_cone.out:21-33`).  The separate construction in
`scripts/r134_sublum.py:14-24` is what works: it controls \(|s'|\le1\), and
therefore in every dimension
\(|\nabla E|\le\sqrt{\sum_i s_i^2}/E\le1\).  Its rerun gives
\(v_{\max}=0.9927\) in three dimensions at \(b=1.4,m=0.3\)
(`scripts/r134_sublum.out:1-6`).

The reported Klein--Gordon kernel is a useful comparator but is not the
commutator of R7-1's number-conserving CAR law (`R13-4_report.md:172-175`).
For that law the one-particle kernel is
\(U(r,t)=\int e^{ikr-iE(k)t}\,dk/(2\pi)\), and the exact norm for the local even
observables is
\(\|[n_r(t),n_0]\|=|U(r,t)|\sqrt{1-|U(r,t)|^2}\).  An independent run finds
\(\sqrt t\max|U|=0.220,0.215,0.206,0.207\) at
\(t=100,200,400,800\) in \(1.2\le r/t\le1.3\) for the \(b=2\) law, confirming
the actual CAR observable has the same \(t^{-1/2}\) superluminal-window tail
(`R13-4_referee_checks.out:11-16`).  The derivative-controlled \(b=1.4\) law
drops from \(6.5\times10^{-3}\) to \(1.2\times10^{-5}\) on the same annulus
(`R13-4_referee_checks.out:17-21`).  Thus the qualitative leakage claim is
confirmed, but the table in `R13-4_report.md:197-208` must remain labeled as
Klein--Gordon-comparator numbers, not the R7-1/R9-5 commutator itself.

## 5. Part (ii), the R12-1 off-box gravity completion

**OPEN is correct.**  Within the perturbative degree assignment, a constraint
basis change of the form \(\phi C_1\), with \(\phi\) a matter bilinear, cannot
repair the degree-2 defect: \(C_1\) is pure gravity and abelian at linear
order, so both terms in \(\{C_1,\phi C_1\}\) vanish.  This confirms the narrow
“not a basis change” result in `R13-4_report.md:153-157`.

Conditionally on realizing the proposed completion, its schematic
\(E(x)K(x-y)\widehat O(y)\) term makes a lapse near \(x\) act on matter near
\(y\) with the power-law kernel (`R13-4_report.md:158-166`).  That is genuine
nonlocality of the proposed gauge generator, not merely a nonlocal solution.
But the worker overstates this as “no local observable is gauge invariant”:
the calculation only excludes local operators that fail to commute with the
defect density.  More importantly, R12-1 established only a local-germ
necessity; the gravity gate, JS/JJ kernels, midpoint phases, invariant domain,
and full physical sector are unbuilt (`C5_R12-1_referee_verdict.md:5-15`).
No local auxiliary/reference-frame formulation has been excluded.  Therefore
neither PHYSICALLY NON-LOCAL nor LOCAL-EQUIVALENT is available for (ii).

## 6. Readings and consequences for earlier box results

- **(i): PHYSICALLY NON-LOCAL in \(\mathcal E\), confirmed with the corrections
  above.**  The exact operator-norm coefficient is larger than reported; the
  retained \(56e^2G(r)\) lower-bound matrix element is enough for the fixed
  reading at `TESTS.md:4659-4662`.
- **(ii): OPEN, confirmed.**
- **(iii):** the quoted whole-zone velocities are correct; a subluminal box
  exists, but only after changing the edge interpolation, and the actual CAR
  leakage shares the worker's power law.

The earlier scoped claims **survive for a redesigned \(b<\pi/2\) box**, because
their exact algebraic content uses only equality with the continuum symbol on
an open plateau, not the old off-box interpolation.  R7-1's free Poincare
algebra and leakage-domain theorem (`TESTS.md:3398-3407`), R8-1's two-body BT
algebra (`TESTS.md:3795-3805`), R9-2's projected stress and universal fall
(`TESTS.md:3889-3896`), R9-5's flux-free qubit realization
(`TESTS.md:3917-3923`), R9-6's two-particle three-dimensional algebra
(`TESTS.md:4016-4024`), and R11-4's projected pole--dipole consequences
(`TESTS.md:4425-4436`) all retain their stated scopes after shrinking or
rescaling their compact momentum supports.  R9-6's quoted support reaches
\(1.548\), so it can fit only narrowly below \(\pi/2\) (or should be rescaled).
What does **not** transfer automatically is any old whole-zone velocity,
real-space tail constant, transition-shell number, or lattice-native numerical
residual; those require reruns for the new symbol.  The rapidity budget drops
only logarithmically, as already encoded by
\(\eta_*=\operatorname{asinh}(b/m_\perp)-|\theta|\)
(`C5_R7-1_report.md:169-188`).

## Strongest correct statement

For the charged BF quotient law with the inherited flat/group-averaged
measure, horizontal reduction necessarily adds a four-fermion neutral-pair
transfer term \(-\tfrac12P_hX^\dagger g^{-1}X\); a bounded local
gauge-invariant horizontal observable detects a nonzero \(1/r\) double
commutator, so no finite-range or super-polynomially quasi-local extension that
keeps those observables local and preserves the same physical content exists,
although the zero-fermion sector is an exact Gauss-law/constraint-solving
reduction and R12-6 localizes the interaction only by adding physical
\((\sigma,\eta)\) modes.  R12-1's gravity tail remains OPEN because only a
nonlocal local-germ generator is known, not a completed physical theory or a
class-wide no-go.  The box controls are genuinely superluminal for the used
profiles (\(v_{\max}\simeq4.1\)--\(12.4\)), with power-law leakage in the
superluminal window, but a derivative-controlled \(b<\pi/2\) Gevrey box is
subluminal; the earlier box Poincare, stress, qubit-sector, and bound-body
results survive on a correspondingly narrower plateau within their existing
scopes, while their old edge numerics do not.
