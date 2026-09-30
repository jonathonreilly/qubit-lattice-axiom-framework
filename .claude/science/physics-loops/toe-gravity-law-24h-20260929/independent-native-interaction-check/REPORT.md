# Independent check of the native pair-pulse interaction

No blocking mathematical error was found in the frozen interaction packet.
All **675 entries** of its three general-complex quartic matrices agree
exactly with an independently implemented calculation completed before
reading the packet. All 675 entries of the printed complex invariant
formulas also agree. The normalization, hard-core connected subtraction,
positive quartic bound, uniform remainder, and restricted trial minima
have been checked at the scope described below.

This is a focused independent check, not a formal audit/PASS, adopted
Hamiltonian, scattering result, condensate, or many-body phase statement.
The rotation comparison concerns the explicitly specified tensor-amplitude
identification whose norm agrees with the actual uniform-pair Gram. Cubic
representation content alone does not uniquely choose that identification.

## Freeze and independence

The checked author report is `native-interaction-route/REPORT.md`, SHA256
`81799e085a81f89c501aab569474d9f53a9f7ca7ecb0786ad002ef4c5c85e6ff`.
Its `quartic.json` is SHA256
`b5d72e34394cf337e3579638d63b1ad6cf7c6230cd05876abc69c0873c0aa047`.
Only anticipated freeze timing was exchanged with the author before their
freeze; no interim values or implementation were requested or read.

My independent sparse calculation finished at approximately 01:28 UTC.
The complete [pre-comparison derivation](PRECOMPARISON.md) was frozen with
SHA256 `47e8094bde1892c6186ed6e0d62e72dcc14ff1859aa2668a143797fb378a8864`,
and the independent coefficient data with SHA256
`4d4ac9e32d0d2cf80d3153ae01e8a1a49c8728c7bfeab68a50551e1d39fc8c69`.
`PRECOMPARISON_MANIFEST.json` records that the author freeze notice had
arrived but its packet had not yet been read. These files remain unchanged.

The actual native-stability operator definitions were independently
reconstructed in the preceding checks and read again as this task's input.
Read-only main refresh now gives `9d15f404c63ff5b9d877e2bdc06ea8713493ffb4`;
the frozen supplied Hamiltonian is not silently replaced by moving main.
Relevant axiom/registry/primitive bytes are checked in the source inventory.
No author code was imported or executed, including during post-freeze
comparison. The author packet's new code paths and declared resource logs
are not being recast as independently run evidence.

## Independent full-carrier reconstruction

Let `C=sum_(x,A) zeta_A Q_A(x)^dagger`, `v=C Omega`, `w=C^2 Omega`, and
`S=||v||^2`. The state `exp[t(C-C^dagger)]Omega` is an exact normalized
unitary pulse. The first relevant powers on the vacuum are

`v`, `w-S Omega`, `C^3 Omega-C^dagger w-Sv`.

The actual mobile Hamiltonian annihilates both the vacuum and every
uniform one-pair vector v. Its number conservation therefore gives

`[t^4]<H>=<w,Hw>/4`,
`[t^4]<N>=(||w||^2-2S^2)/3`, ` [t^2]<N>=2S`.

These formulas include the normalization and hard-core annihilation terms
of the unitary exponential; they do not use an unnormalized coherent
exponential or a bosonic pair algebra. The number phase reversing the pulse
also proves that both expectations are even in t.

In the common coordinates `z=(a,b,p,q,r)=(u1,u2,v12,v13,v23)`, `u3=-a-b`,
the physical unordered-edge coefficients are `u_i` on opposite edges and
`-delta_i delta_j v_ij` on orthogonal edges. The latter includes the two
shell centers of the same physical pair. Hence

`S/V=s=sum_i |u_i|^2+2 sum_(i<j)|v_ij|^2`.

For four distinct sites the amplitude of w is twice the sum of its three
perfect-matching products. Overlapping creators give zero. I evaluated the
energy using each actual annihilator square in the positive decomposition,
subtracting its disconnected amplitude algebraically before evaluating a
finite residual-pair sum. Each square kills the complete uniform-pair
family, so this subtraction is exact for every complex z.

The diagonal integer occupation term contributes only four-particle stars
with three graph neighbors around an occupied site. Its exact contribution
is a sum over 816 triples. The total independent assembly has 34 square
rows, 67,420 candidate residual pairs, and at most 88 residual sites in
one row. It stores the energy as a rational Gram form on the fifteen
monomials `z_i z_j`, `i<=j`.

For number, I used a different connected formula from the author's cycle
enumerator. For a general symmetric creation matrix M with zero diagonal,
literal hard-core matching counts give

`||w||^2-2S^2=tr[(M M^dagger)^2]`
` -4 sum_x (sum_y|M_xy|^2)^2+4 sum_(x<y)|M_xy|^4`.

A separate nontranslation-invariant seven-site control verifies this
identity by actual four-site words. For the translation convolution it
becomes the finite closed-walk expression

`kappa4=(sum_h |sum_d c_d conjugate(c_(d-h))|^2-16s^2+4u4)/3`,
`u4=(1/2)sum_d|c_d|^4`.

This checks the extensive cancellation and conjugation ordering without
reusing the author's assembly. The full derivation, exact matrices, real
invariant reduction, and support proof are preserved in the pre-comparison
artifact and scripts.

## Exact comparison of the coefficient formulas

The author's monomial labels and my integer-index monomials have the same
order after translating coordinate names. The energy denominators are both
12 and the number denominator is both 3. Every numerator entry in all three
15-by-15 matrices agrees exactly, with no tolerance.

I independently expanded the printed invariants using ten formal variables
for z and its conjugate, including the trace constraint `u3=-u1-u2` and the
author's reversed T-vector order `(v23,v13,v12)`. This reproduces every matrix
entry in equations (6), (7), and (8). In particular the one-term-per-index
definition of M4, the real-part factors, and the complex E contribution to
the number coefficient are correct. The real formulas in my pre-comparison
derivation are the corresponding specialization, not formulas obtained by
replacing all complex variables with magnitudes.

An independent coefficient-level transformation verifies all three complete
forms under each of the 24 proper cubic rotations. This is stronger than
checking a few real directions. The common phase and conjugation symmetries
also follow directly from the real Hermitian bidegree-(2,2) construction.

## Finite support and uniform remainders

The author's `L>=13` condition is safe. The connected energy support has
coordinate span at most seven; testing a possible edge against a displacement
of size at most two requires checking differences of magnitude at most nine.
Number closed walks have four displacements of size at most two. My separate
conservative common lift works for `L>=10`; the author deliberately states
a stronger side-length restriction. Neither calculation claims these exact
numerical coefficients on every smaller torus `L=5,...,9`. The pulse/Taylor
identities themselves hold there, but winding corrections need separate
treatment.

The author's local parity observation is also valid within these embedded
supports. Both sites of a residual pair in a connected defect have parity
opposite to its center. Adjacent centers therefore have disjoint residual
occupation supports. Their overlap cannot reappear by periodic identification
at the stated side length. Thus the mobility coefficient can equally be
written as six times the one-center collective defect norm. This does not
assert a global checkerboard symmetry on an odd torus.

I first established uniform sixth-order remainder bounds using six-site
local generators; the author's physical-edge decomposition gives another
valid, sharper count. A single edge term `w b_u^dagger b_v^dagger-conjugate(w)
b_u b_v` has norm `|w|`, as follows from its two-by-two vacuum/full-pair
block; it is zero on the one-particle states. Each site touches eighteen
physical pair edges. A nonzero commutator therefore has at most `18s`
possible edge terms, norm cost at most `2wmax`, and at most one new site.
This yields precisely the factor `(36wmax)^n(s)_n`.

The stated Hamiltonian density norm also reconstructs:
the squared coefficient-sum bounds of E1, E2 and each T are `2,8/3,4`.
The onsite term, attractions and 153 triples cost

`1+2(2+8/3)+3*4+153=526/3`

times mu. The fifteen gradients cost
`3*4*(2+8/3+3*4)=200` times tau. The 125-site support cube is a harmless
overestimate. Hence `h0=(526/3)mu+200tau` and both sixth-order remainder
constants in equation (18) have the correct factorials. Unitary conjugation
preserves these bounds at all remainder times; no `Vt^2<<1` assumption is
introduced. The conclusion is about finite-volume states and uniform local
expectations, not an infinite Fock-space pulse unitary.

## Positive quartic bound and restricted trial minima

Using the independently reconstructed matrices and an independent expansion
of `s^2`, I formed `f_mu-40s^2` and `f_tau-100s^2` and carried out rational
LDL factorization. Every pivot is strictly positive, and direct rational
reconstruction gives the original matrices. The full pivot lists are in
`comparison_results.json`. Thus

`mu f_mu+tau f_tau >=(40mu+100tau)s^2`

is independently confirmed. This is a sufficient positive Gram certificate
on the monomial space, so it certainly holds on the physically constrained
quadratic monomials. It does not depend on the later coercivity theorem.

The two additional minimization statements were checked algebraically:

* On pure T, `(p^2+|q_T|^2)/2-r=2 sum_(i<j)(Re(v_i conjugate(v_j)))^2>=0`.
  Substitution leaves the positive coefficient `(10/3)mu+32tau` on
  `|q_T|^2`. Two equal components in quadrature and a third zero saturate
  the bound with `q_T=0`, giving exactly `(638mu/3+592tau)p^2`. Its normalized
  value exceeds the pure E coefficient by `7mu/6+28tau`.
* On the stated mixed slice `u=(x,-x,0), v12=y`, direct substitution gives
  the reported A, B, C0 and relative-phase coefficient
  `Rphi=44mu/3-56tau`. This fixes the phase threshold at `mu=42tau/11`.
  Minimizing in the T fraction with `D0=C0-|Rphi|` gives the reported
  fraction `(2A-D0)/(2(A+B-D0))` when `mu>3tau`. In the first phase regime,
  `2A-D0=(224/3)(mu-3tau)`; in the second it is `104mu-336tau`, already
  positive throughout that regime. The interior solution lies below one.
  For `mu<=3tau` the pure E endpoint is minimal; in the subrange where the
  quadratic is concave, this follows by comparing the two endpoints, since
  B exceeds A. These are slice statements, not a minimization over all five
  complex channels or a phase boundary of H.

## The checked rotational discriminator and its limits

Under the explicitly declared tensor map

`T=[[u1,v12,v13],[v12,u2,v23],[v13,v23,u3]]`,
`s=tr(T^dagger T)`.

A 45-degree proper rotation maps the real diagonal direction
`diag(1,-1,0)` to the off-diagonal 12 direction with the same eigenvalues
and s. At pair norm density one, the exact results are

| Physical pulse | Energy coefficient at order t^4 | Number coefficient at order t^4 |
|---|---|---|
| `sum_x Q_E1(x)^dagger` | `52mu+120tau` | `-5/3` |
| `sum_x Q_T12(x)^dagger/sqrt(2)` | `54mu+156tau` | `-5/3` |

Their energy difference is strictly positive, `2mu+36tau`. Their number
expansions agree through this order. At equal small pulse density, the
leading coefficients multiplying rho squared differ by `mu/2+9tau`.
This verifies the proposed nonlinear cubic anisotropy in the specified
unrelaxed pulse family, beyond the two-particle band calculation.

The tensor convention needs to remain explicit. Cubic E plus T2 covariance
does not by itself fix the relative E/T normalization of an extension to
SO(3). The map above is compatible with the actual pair Gram. Identifying
instead the coefficients of the literal relative-momentum quadratic form
would impose a different relative scale. This is a scope qualification,
not a numerical disagreement with the author's declared map. There is no
embedding-independent exclusion of an emergent rotational phase here.

The fixed-density and chemical-potential trial consequences also follow
with their stated limits. From `rho=2s t^2+O(t^4)`,
`e=epsilon4 rho^2/(4s^2)+O(rho^3)` for a fixed nonzero direction. A pure E
pulse with `t^2=nu/[(52mu+120tau)s]` gives the uniform small-nu variational
bound `e0(nu)<=-nu^2/(52mu+120tau)+O(nu^3)`. This improves the constant in
the earlier loose pulse estimate. It does not identify the actual ground
state, its pair populations, spontaneous time-reversal breaking, or its
excitations. In particular these coefficients are not a relaxed two-pair
resolvent, scattering matrix, or scattering length.

## Evidence and remaining coverage limits

The primary independent sparse run was priced below 30 seconds and 150 MB;
it used **2.830 seconds** and **17,973,248 bytes**. A coefficientwise cubic and
real-invariant reduction used **0.188 seconds**; the complete post-freeze
matrix/invariant comparison and rational LDL checks used **0.197 seconds**.
All ran with BLAS/OMP caps of one. The source freeze, absence of a stop
sentinel, and deadline were checked before the primary run. No large
four-particle torus, dense many-body eigensolver, unmanaged worker, source
mutation, or formal review was involved.

Only this independent-check directory was written. Exact scripts, outputs,
source bindings and manifests accompany the two reports. The primary
coefficient data uses integer/Fraction arithmetic. The auxiliary complex
sample controls use bounded Gaussian-integer arithmetic with exact binary
representability; the stronger final covariance check compares every
integer coefficient and does not rely on those samples.

No full external novelty survey or independent reconstruction of the new
main/proposal theorems listed in the author's source inventory was attempted.
Those sources are not premises of the coefficient proof. No density-phase,
tensor-mode, gauge-action, or actual readable-record conclusion is supplied
by this check. No correction to the frozen coefficient matrices or the
scoped pulse conclusions is needed.
