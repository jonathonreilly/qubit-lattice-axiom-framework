---
claim_id: admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_bounded_theorem_note_2026-08-24
claim_type: bounded_theorem
claim_scope: "For the supplied twenty-two-edge reflected-curvature quadratic action at mu=1/1024, in the odd y/z-reflection six-edge plus one-Ward sector at spatial momentum (pi/2,0,0), the Hermitian odd-edge symbol is positive semidefinite of constant rank five on the complete temporal unit circle. The declared cross-Ward bordered inverse has a positive semidefinite rank-five edge block. Its gauge-invariant content is the covariance form on the conserved rank-five source module; the full six-coordinate KKT extension depends on the declared transverse slice. Every finite temporal source Gram is Toeplitz positive, and the matrix moments define a canonical minimal bilateral unitary GNS shift. Reflected left/right Weyl halves glue to the same full-line two-layer covariance, deriving the matrix measure from the action and declared Ward border rather than a fitted scalar metric. The exact TT subchannel has a unique strictly positive scalar measure and an infinite-dimensional cyclic unitary realization; no fixed finite-dimensional unitary can reproduce all its decaying nonzero moments. This is stationary kinematic reconstruction, not OS transfer positivity, a selected local Hamiltonian, quantum state/commutator, operational Record instrument, other sector or momentum, Newtonian limit, refinement theorem, gravity closure, axiom amendment, obligation retirement, or TOE percentage movement."
parents:
  - admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_bounded_theorem_note_2026-08-24
upstream_dependencies:
  - minimal_axioms
  - admissibility_reflected_curvature_weyl_feshbach_reflection_radical_boundary_bounded_theorem_note_2026-08-24
  - admissibility_reflected_curvature_descriptor_halfspace_source_faithful_metric_boundary_bounded_theorem_note_2026-08-24
  - admissibility_reflected_curvature_action_record_source_two_step_transfer_boundary_bounded_theorem_note_2026-08-14
runner: scripts/admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24.py
---

# Action-Glued Matrix GNS Unitary Boundary

**Type:** `bounded_theorem`

**Status:** bounded numerical/algebraic support; unaudited; no canonical axiom
is edited.

**MATRIX_GNS_VERDICT: POSITIVE_KINEMATIC_RECONSTRUCTION.**

**FINITE_DIMENSION_ALL_POWERS_VERDICT: BOUNDED_INFEASIBLE.**

**HAMILTONIAN_RECORD_VERDICT: OPEN.**

**GRAVITY_VERDICT: OPEN.**

TOE accounting: **zero obligation retirement, zero percentage movement, and
no axiom is amended**.

## Result Up Front

The action supplies substantially more than the scalar three-pole TT response
used in Blocks 181--183. On the entire temporal unit circle, its physical odd
six-edge kernel is positive semidefinite with one exact Ward null direction
and five positive directions. The one-Ward bordered inverse consequently has
a positive semidefinite rank-five edge block. This is established globally by
low-degree Bernstein certificates, not by treating a frequency grid as the
proof.

That matrix density makes every finite-support temporal Gram positive and
therefore defines a canonical minimal matrix GNS representation. Multiplying
source histories by `z` is unitary and reproduces every bilateral matrix
moment. The construction carries the complete conserved rank-five source
fiber, not only the TT covector. Its TT compression has the unique strictly
positive scalar Herglotz density already latent in the unchanged signed pole
data.

The provenance question also improves. Let `W_R` be Block 183's right
half-space Weyl form, `R` the geometric time reflection, and

\[
 \Theta=\begin{pmatrix}0&R\\R&0\end{pmatrix}.
\]

The reflected pair obeys the full-line gluing identity

\[
 C_2^{-1}=W_R+\Theta W_R\Theta-A,                    \tag{1}
\]

where `A` is the shared central two-layer action block and `C_2` is made from
the zeroth and first full-line bordered covariance moments. The relative
residual is below `1e-13`; independent centered open-chain Schur complements
converge to the same operator. Thus the matrix moments are selected by the
action, geometric reflection, and declared cross-Ward border. They are not a
post-hoc absolute-residue rule or a freely chosen Stein metric.

There are two important boundaries.

First, the full six-coordinate inverse block is a KKT extension. It is
invariant under genuine Ward-generator normalization, but it changes under a
different transverse gauge slice. The slice-independent physical object is
the form on conserved sources, where it equals the Moore--Penrose inverse of
the edge action. Saying that six independent physical currents have been
derived would therefore be false. The fiber has five conserved directions;
only three constant one-time vectors are conserved at every frequency, while
time-extended local currents recover the rank-five fiber.

Second, the GNS shift is a bilateral stationary history translation. It does
not become a positive self-adjoint Euclidean transfer, select a Hamiltonian or
time orientation, quantize the Gaussian covariance, or define a Record
instrument. Its spectrum is the full circle. A discontinuous Borel logarithm
can be imposed, but no continuous local logarithm is selected. Gravity and
the axioms remain open.

## Trace And Status

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_regge_tt_record_observable_inverse_amplification_refinement_gate_bounded_theorem_note_2026-08-23
target_blocker_text: "the originally promised terminal route verdict is blocked until a physical reduction/section (or an inner product inducing one) and directed state/source/observable refinement law are supplied"
source_of_blocker_text: frontier_question
reachability_to_target: supports
artifact_role: theorem
matrix_gns_verdict: positive_kinematic_reconstruction
finite_dimension_all_powers_verdict: bounded_infeasible
hamiltonian_record_verdict: open
gravity_verdict: open
next_trace_action: "extend the conserved matrix covariance over momentum and both physical TT sectors, then seek an action-selected positive-energy quantum/Record realization; do not spend another block on scalar dilation coordinates"
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs, Types, And Scope

The supplied object is the same quadratic twenty-two-edge
reflected-curvature action and odd Ward border used by Blocks 181--183, with
`mu=1/1024` and spatial momentum `(pi/2,0,0)`. It is not the neighboring
nonlinear fifteen-edge gravity/refinement carrier. The calculation recomputes
the action, orthonormal odd edge basis, right and left Ward maps, five
temporal Laurent coefficients, geometric reflection, and local TT covector
from repository inputs.

Write the bordered symbol as

\[
 B(z)=\begin{pmatrix}O(z)&\ell(z)\\
 \ell(z)^\dagger&0\end{pmatrix},\qquad |z|=1,         \tag{2}
\]

where `O` is the `6 x 6` odd-edge kernel. The lower-right zero is the supplied
Lagrange-multiplier border, not an optional regulator. The top-right vector
comes from the cross-momentum left Ward map. All statements about its
six-coordinate extension are conditional on this declared cross-Ward slice;
conserved-source amplitudes are not.

The [minimal axioms](MINIMAL_AXIOMS_2026-06-29.md) are contextual. They do not
choose this quadratic action, a Hamiltonian, a unitary branch, a quantum
commutator/state, source dictionary, Record cadence, or refinement map. No new
premise is imported and no axiom is amended.

## Global Edge Positivity And Bordered Invertibility

In the current orthonormal odd-edge basis, an exact right-Ward Laurent vector
is

\[
 a(z)=\left(
 0,\frac{z-1}{\sqrt2},\frac{1-i}{\sqrt2},
 \frac{iz-1}{\sqrt3},\frac{1-z^{-1}}{\sqrt2},
 \frac{1-iz^{-1}}{\sqrt3}\right)^T,                  \tag{3}
\]

and coefficient convolution gives `O(z)a(z)=0` below `5e-15` relative
residual. The cross-Ward border is

\[
 \ell(z)=\overline{a(z)}=\left(
 0,\frac{z^{-1}-1}{\sqrt2},\frac{1+i}{\sqrt2},
 \frac{-iz^{-1}-1}{\sqrt3},\frac{1-z}{\sqrt2},
 \frac{1+iz}{\sqrt3}\right)^T.                      \tag{4}
\]

Let `e5(O)` be the fifth elementary symmetric polynomial of the six
eigenvalues of `O`. It is a degree-four polynomial in `x=cos(theta)`. After
putting `t=(x+1)/2`, its degree-four Bernstein coefficients are

```text
297.2760546, 200.9028980, 125.3794712, 70.6725618, 36.7489428.
```

Every coefficient is strictly positive. Because (3) gives at least one null
direction, `e5>0` proves rank exactly five at every frequency. At `z=1` the
other eigenvalues are approximately

```text
0.5533545, 0.6921530, 2.5041132, 4.0703020, 9.4136641.
```

They cannot cross zero without making `e5` vanish, so `O(z)>=0` with constant
rank five on the complete circle.

The bordered determinant is also an even degree-seven trigonometric
polynomial. The Bernstein coefficients of `-det B` are

```text
756.2285582, 314.8222289, 118.2966881, 53.8952023,
50.1844728, 66.4258766, 81.9804346, 85.7475330.
```

Thus `det B<0` globally. An independent 8,192-frequency check has minimum
singular value `0.1655515` and minimum determinant magnitude `68.8769`.
Equivalently, the constraint vector couples to the one-dimensional null line
of `O` at every frequency.

## Positive Covariance And Its Exact Gauge Boundary

Let `C_ell(z)` denote the upper-left edge block of `B_ell(z)^-1`. With `O^+`
the Moore--Penrose inverse, direct KKT elimination gives the exact identity

\[
 C_\ell=P_\ell O^+P_\ell^\dagger,\qquad
 P_\ell=I-\frac{a\ell^\dagger}{\ell^\dagger a}.     \tag{5}
\]

Therefore `C_ell>=0`. It has rank five and

\[
 C_\ell\ell=0.                                      \tag{6}
\]

The five nonzero eigenvalues stay within

\[
 0.10622856\le\lambda_+(C_\ell(z))\le5.84606764     \tag{7}
\]

on the entire circle. The runner verifies (5), (6), the KKT quadratic
identity, and the dense spectral bounds independently of the Bernstein proof
for `O` and `det B`.

Equation (5) resolves exactly what is canonical. For every nonzero Ward
generator rebasing `ell -> c(z)ell`, `P_ell` and `C_ell` are unchanged. For
conserved sources

\[
 \mathcal S_z=\{j\in\mathbb C^6:a(z)^\dagger j=0\}, \tag{8}
\]

one has

\[
 j^\dagger C_\ell k=j^\dagger O^+k,
 \qquad j,k\in\mathcal S_z.                         \tag{9}
\]

Hence every conserved response is independent of the transverse slice.

The full matrix extension outside (8) is not invariant. At `theta=0.7`, the
canonical cross-Ward `C_ell` differs from the Moore--Penrose slice `O^+` by
relative Frobenius norm `0.524396`; an unconserved coordinate response changes
from `0.769628` to `0.780964`, while the TT response remains
`0.814562854528`. A local deformation `ell'=ell+(1/4)Oe0` changes the full
matrix by `0.133394` and the same unconserved response to `0.785336`, again
leaving TT invariant. A lower-right multiplier mass is even more dangerous:
at `tau=0.2` it creates a negative covariance eigenvalue near `-0.0793`.

Among constant one-time edge vectors, the intersection of (8) over the full
circle is only three-dimensional. One basis is

\[
 e_0,\quad
 (0,i\sqrt{2/3},\sqrt{2/3},1,0,0)^T,\quad
 (0,0,-\sqrt{2/3},0,i\sqrt{2/3},1)^T.               \tag{10}
\]

The TT source is the first vector. General time-extended local conserved
sources form the rank-five Laurent module (8). The remaining constant source
directions in the six-coordinate KKT extension are useful algebraically but
must not be called gauge-invariant physical currents.

## Matrix Toeplitz Positivity And GNS Reconstruction

Define the bilateral matrix moments

\[
 M_n=\int_0^{2\pi}e^{in\theta}C_\ell(e^{i\theta})
       \frac{d\theta}{2\pi},\qquad M_{-n}=M_n^\dagger. \tag{11}
\]

For every finite Laurent source history `f(z)=sum_j z^j f_j`,

\[
 \sum_{j,k}f_j^\dagger M_{j-k}f_k
 =\int f(z)^\dagger C_\ell(z)f(z)\frac{d\theta}{2\pi}
 \ge0.                                               \tag{12}
\]

This proves every finite-support block Toeplitz Gram positive semidefinite; a
finite list of matrices is not being extrapolated. The 1, 2, 4, 8, and 16
site sections independently have nullities

```text
0, 0, 2, 6, 14.
```

The pattern is exact. Because one component of (4) is a nonzero constant, any
finite Laurent vector in the pointwise radical is `ell(z)q(z)`. For an
`h`-site window there are exactly `h-2` allowed shifts of the three-tap
generator (4). This is the local KKT gauge radical, not an unexplained
numerical nullspace. On the conserved module (8), the invariant form is (9).

Complete the Laurent histories modulo this radical in the norm (12):

\[
 \mathcal H_\ell=
 \overline{\mathbb C^6[z,z^{-1}]/
 \ell(z)\mathbb C[z,z^{-1}]}.                       \tag{13}
\]

Then

\[
 U[f]=[zf],\qquad Ev=[v],\qquad E^\dagger U^nE=M_n. \tag{14}
\]

`U` is unitary because multiplication by `z` preserves (12). The matrix
measure determines the minimal cyclic representation up to unitary
equivalence. On the physical conserved-source subspace, (9) gives the
slice-independent version of the same amplitudes.

The uniform rank and bounds (7) imply that `U` has purely absolutely
continuous full-circle spectrum with multiplicity five and no point spectrum.
The source injection, three-tap radical, and history shift are kinematically
local in time.

## Reflected-Weyl Gluing And Action Provenance

Let

\[
 A=\begin{pmatrix}B_0&B_1\\B_{-1}&B_0\end{pmatrix},\qquad
 C_2=\begin{pmatrix}\widehat B^{-1}_0&
                         (\widehat B^{-1}_1)^\dagger\\
                         \widehat B^{-1}_1&\widehat B^{-1}_0
       \end{pmatrix},                               \tag{15}
\]

where `widehat B^-1_n` is the `n`th full bordered covariance moment. Block
183 constructed `W_R` from all seven endpoint chains and seven finite inside
roots. Geometric reflection gives `W_L=Theta W_R Theta`. Eliminating the two
semi-infinite exteriors while subtracting the shared central action once
gives (1).

The direct full-circle covariance and Weyl gluing agree to relative residual
below `1e-13`. Centered open chains at total depths 8, 16, 32, and 64 converge
to (1) with relative errors

```text
3.96e-3, 3.31e-5, 2.12e-9, <1e-13.
```

This closes the principal provenance gap left by the scalar Stein dilation:
the paired Weyl halves plus their action gluing reconstruct the full matrix
moments. The Block 182 positive metrics `H_alpha` remain nonunique, but they
are no longer needed to define (13)--(14).

The result remains conditional on the supplied cross-Ward/reality border.
Equation (9), not the unconserved six-coordinate extension, is invariant
under changing the transverse KKT slice.

## TT Scalar Compression And Finite-Resource Boundary

For the unchanged TT covector, only three real inside roots are visible:

```text
z = (-2.4543906999e-5, 2.9116902472e-4, 0.266171726916)
a = ( 1.5176104264e-4,-2.1745072763e-4, 0.581884811601)
```

With `m_n=sum_i a_i z_i^n`, define

\[
 \rho(\theta)=\sum_i a_i
 \frac{1-z_i^2}{1-2z_i\cos\theta+z_i^2}.            \tag{16}
\]

After clearing the positive denominators, the numerator has degree two in
`x=cos(theta)` and Bernstein coefficients

```text
0.5408429759, 0.5405894578, 0.5403360887.
```

The derivative numerator has five positive Bernstein coefficients, all above
`0.2875`. Thus `rho` is strictly increasing in `x` and

\[
 0.337174265271\le\rho(\theta)\le1.003937597428.     \tag{17}
\]

It matches the direct TT compression of `C_ell` below `4e-10`. The negative
middle residue is therefore compatible with Toeplitz/unitary positivity; it
was incompatible with Hankel/self-adjoint-transfer positivity.

The unique minimal scalar cyclic model is

\[
 \mathcal K=L^2(\mathbb T,\rho\,d\theta/2\pi),\qquad
 U=M_z,\qquad \xi=1,\qquad
 \langle\xi,U^n\xi\rangle=m_n.                      \tag{18}
\]

It is necessarily infinite-dimensional. If a fixed finite-dimensional
unitary `V`, even with distinct left and right vectors, reproduced all powers,
then

\[
 m_n=\sum_{k=1}^r\gamma_k\lambda_k^n,
 \qquad |\lambda_k|=1.                              \tag{19}
\]

But every `|z_i|<1`, so `m_n` tends to zero. Cesaro averaging against each
distinct `lambda_k` forces every `gamma_k=0`, contradicting
`m_0=0.581819121916`. This excludes only a fixed finite-dimensional exact
all-powers unitary. It does not exclude finite-horizon unitary dilations,
finite nonunitary contractions, repeated-projection unitary colligations,
Krein models, or an infinite local environment.

## Locality, Positive Energy, Quantum, And Record Boundary

The determinant poles occur in reciprocal-conjugate pairs and remain at least
`0.44947658` radially away from the unit circle; the largest inside modulus is
`0.5505234195`. Hence the rational covariance has exponentially decaying
temporal moments. It is not finite range: for example,
`||M_34||_2` is approximately `3.61e-9` and is nonzero. The action is range
two, while its inverse covariance has an infinite tail.

This is temporal locality at one frozen spatial momentum only. It proves no
spatially local tensor factorization, causal cone, nonlinear background
propagation, or Record locality.

Toeplitz positivity is not OS or positive-semigroup positivity. The TT
compression still has

\[
 \lambda_{\min}[m_{i+j+1}]_{i,j=0}^{1}
   =-4.426\times10^{-9},\qquad
 \lambda_{\min}[m_{2(i+j)}]_{i,j=0}^{2}
   =-3.297\times10^{-7}.                             \tag{20}
\]

Thus the previously tested one-step shifted and two-step Hankel routes do not
become positive self-adjoint transfers.

The full-circle spectrum does not select a Hamiltonian branch. A continuous
real phase `h(z)` with `exp(ih(z))=z` on the full circle
would be a continuous lift of a winding-one map, which is impossible. A
positive Borel logarithm can always be imposed by a branch cut, but its phase
jump produces an algebraic `1/n` Fourier tail rather than a finite- or
exponentially-local translation-invariant generator. The stationary unitary
therefore does not establish positive energy or time orientation.

Finally, a positive covariance can describe a classical stationary Gaussian
process. No symplectic/commutator form, uncertainty-compatible quantum state,
Hermitian operator algebra, completely positive instrument, registered clock,
outcome update, or Record cadence is derived here. Those are independent
closure obligations, not semantic decorations on (14).

## Axiom Decision

No contradiction with Lattice, Qubit, Admissibility, or Record is found. The
minimal axioms deliberately leave dynamics and the Hamiltonian open. The
action-glued stationary representation is compatible with that stance, while
its failure to select positive energy or a Record instrument is a missing
dynamical construction—not evidence that an axiom is inconsistent.

No axiom is amended. If a full momentum/sector extension later remains
positive but repeatedly fails to select quantum dynamics, governance may
face a dynamics-selection addition. This one-sector theorem is too early to
make that premise constitutional.

## No-Go Discipline Gate

The only new negative statement is: **the nonzero decaying TT moment sequence
cannot be reproduced for all powers by one fixed finite-dimensional unitary.**
Equation (20) restates earlier bounded Hankel walls. Infinite matrix/scalar
GNS, finite-horizon dilation, open-channel colligation, nonunitary contraction,
Krein, changed action, other momentum, and gravity remain open.

### N1 — Alternative route enumeration

| route | executed terminal test | disposition |
|---|---|---|
| action-derived matrix Herglotz/GNS | prove full-circle matrix positivity, construct the bilateral shift, and bind all moments | `ATTEMPTED`; positive on the declared Ward border and conserved module |
| reflected Weyl gluing | reconstruct the two-layer full-line inverse independently from two half-space boundary forms | `ATTEMPTED`; agrees with direct covariance and finite open chains |
| scalar Herglotz/GNS | certify the unchanged signed TT density globally | `ATTEMPTED`; unique positive infinite-dimensional cyclic model |
| fixed finite-dimensional unitary | test all-power spectral form against decaying nonzero moments | `ATTEMPTED`; Cesaro contradiction |
| finite-horizon unitary dilation | allow dimension/resource to depend on a finite requested horizon | `OPEN`; not excluded by the all-powers argument |
| unitary colligation with repeated projection | retain a finite open channel rather than one closed unitary power | `OPEN`; not excluded |
| positive Stein contraction/Krein metric | use Blocks 182--183's finite non-self-adjoint or indefinite realizations | `ATTEMPTED`; mathematically live but not needed for matrix GNS provenance |
| wider reflection or changed action | alter the boundary embedding/action while preserving source and locality | `OPEN`; no general negative claim |

The positive matrix and scalar routes are explicit alternatives to the narrow
finite-dimensional obstruction, not failed precursors concealed by it.

### N2 — Wall-independence audit

The finite-dimensional wall uses only spectral discreteness, all-power
equality, `m_n -> 0`, and `m_0 != 0`. It is independent of Hankel negativity,
Ward slicing, Weyl gluing, locality, or Record semantics. Conversely, the
Hamiltonian/Record boundary does not follow from finite dimension: the
infinite GNS exists and is positive, but its bilateral full-circle shift does
not select those physical structures.

The transverse-slice dependence is a provenance boundary, not a positivity
failure. Conserved amplitudes remain invariant by (9).

### N3 — Hidden-wall scan

The scope distinguishes: six edge coordinates versus five conserved fiber
directions; three all-frequency constant currents versus time-extended
rank-five currents; Ward normalization versus arbitrary transverse slicing;
matrix Toeplitz positivity versus scalar Hankel positivity; bilateral unitary
translation versus a positive self-adjoint semigroup; kinematic temporal
locality versus a local Hamiltonian; rational exponential correlations versus
finite-range covariance; one spatial momentum/odd sector versus the full
Brillouin zone and even sector; Gaussian positivity versus quantum CCR/state;
and a source history versus an operational Record instrument.

No grid is used as the global positivity proof. The grids cross-check the
Bernstein certificates and expose numerical gaps.

### N4 — Residual matching

| witness | witness residual | residual here | match/use |
|---|---|---|---|
| `scripts/admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24.py` edge/determinant certificates | full-circle `e5(O)>0` and `det B<0` | constant-rank action and covariance positivity | yes; primary global proof |
| same runner KKT/slice calculation | `C=P O+ P*`, Ward scaling, conserved equality, and slice counterexample | exact physical source scope | yes; primary provenance boundary |
| same runner Toeplitz sections | predicted `h-2` local radical and positive complement | all-support integral theorem | yes; independent finite-section cross-check |
| same runner reflected gluing | direct `C2^-1` versus two Weyl halves and centered open chains | action selection of matrix moments | yes; implementation-disjoint cross-check |
| Block 182 positive Stein contraction | finite source-faithful non-self-adjoint realization | environmental alternative | partial; live but nonunique |
| Block 183 raw reflection wall | site/link OS crossings fail source/radical gates | distinction from bilateral GNS | yes; explains why this result does not repair OS |

The positive gluing result is not counted as evidence for the narrow
finite-dimensional negative; the Cesaro argument stands independently.

### N5 — Rhetoric audit

No sentence says gravity is solved, unitary dynamics is selected, all six
coordinate sources are physical, positive energy is impossible in every
completion, or finite resources are universally impossible. The exact
execution resolutions are:

| resolution | executed? | statement |
|---|---|---|
| per-element | yes | the twenty-two-edge action enters through all six odd edge coordinates, one right Ward line, and the declared cross-Ward border |
| per-site | bounded | arbitrary finite temporal histories are covered at one translation-invariant spatial momentum; no inhomogeneous spatial site family |
| per-mode | bounded | the entire temporal circle and five conserved odd-edge fiber directions are covered; other spatial momenta/sectors are not |
| per-block | yes | global polynomial positivity, KKT covariance, Toeplitz/GNS construction, scalar compression, and reflected-Weyl gluing are executed |
| lattice-wide | no | no Brillouin-zone, nonlinear-background, Newtonian, refinement, quantum Record, or all-lattice theorem is claimed |

The cached stdout prints these five substantive lines verbatim.

### N6 — Partial-closure path scan

| live path | current partial closure | terminal missing object |
|---|---|---|
| conserved matrix GNS | action-glued positive rank-five stationary covariance and exact bilateral shift | momentum/sector extension, Hamiltonian/time orientation, quantum algebra/state, Record instrument |
| scalar TT GNS | unique strictly positive spectral measure | full physical-source law and operational observable semantics |
| positive Stein contraction | finite source-faithful contraction with nonunique metric coordinates | action-selected repeated-interaction environment and Record channel |
| wider reflection/OS | nearest-layer raw crossings failed but wider Laurent family remains open | positive self-adjoint quotient with source and locality |
| IR/refinement extension | none supplied by this frozen-momentum block | Newtonian residue/dispersion and exact fine/coarse intertwiners |

The matrix result retires the narrower uncertainty over arbitrary-support
Toeplitz positivity and action provenance for the declared border. It retires
no TOE obligation.

### N7 — Steelman

**Hostile reviewer:** A bilateral GNS construction is automatic once a
positive matrix density is found, and the full six-coordinate density still
depends on a KKT slice. This could be a classical stationary Gaussian process,
not gravity or quantum dynamics. A different unitary colligation might give a
finite operational environment without contradicting the all-powers no-go,
and a full momentum-dependent action could select a local Hamiltonian even
though the frozen full-circle shift has no continuous logarithm.

This steelman is correct. The nontrivial retained content here is the global
action-derived positivity, exact conserved-source scope, and reflected-Weyl
gluing—not the abstract GNS theorem alone. It defeats any broader no-go or
gravity-closure claim, so none ships. It does not defeat the narrow
finite-dimensional fixed-unitary contradiction.

### N8 — Cross-cycle echo

| earlier result | later disposition | application here |
|---|---|---|
| Blocks 74/181 signed TT residues and negative Hankel minors | survived as an OS/self-adjoint-transfer wall | now explicitly separated from positive Toeplitz/unitary reconstruction |
| Block 182 positive Stein contraction | showed exact moments need not be discarded | promoted to the correct unitary question, but its nonunique metric is bypassed by matrix action data |
| Block 183 positive Weyl boundary | changed the boundary response and kept an environmental route open | paired halves now reconstruct the full-line matrix covariance by gluing |
| Block 183 site/link reflection obstruction | ruled out only declared nearest-layer raw crossings | not promoted against bilateral GNS or wider reflection |
| prior Dirac--Kahler data-built reflection repair | showed hostile carriers can admit positive action-selected swaps | forces changed embeddings/actions to remain open |

No successful repair is ignored and no old wall is generalized beyond its
carrier.

**N1--N8 status: PASS for the fixed finite-dimensional exact all-powers
unitary infeasibility only.**

## Reproduction And Evidence Contract

Primary runner:

```bash
python3 scripts/admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24.py
```

Required mutations:

```bash
for mutation in ward_input edge_action_input border_coupling_input covariance_input moment_input scalar_weight_input gluing_input note_boundary; do
  TOE_MUTATION="$mutation" python3 scripts/admissibility_reflected_curvature_action_glued_matrix_gns_unitary_boundary_2026_08_24.py
done
```

Each mutation changes one Ward, edge-action, border-coupling, covariance,
matrix-moment, scalar-residue, reflected-gluing, or landing-boundary input
before its relevant calculation. Baseline must finish with
`TOTAL: PASS=8 FAIL=0`; every mutation must finish with exactly one failed
check. The canonical cache is generated only through the repository cache
envelope and remains non-authoritative until independent audit.

## Boundary And Next Action

This block is significant positive route progress without TOE score movement.
It establishes an action-glued stationary Hilbert/unitary reconstruction for
the entire conserved odd-edge source fiber at one hostile momentum. The
finite scalar dilation search should stop: the unique scalar and matrix GNS
objects are known, and fixed finite dimension is exactly excluded.

The next highest-leverage campaign is momentum/sector closure of the conserved
matrix positivity and gluing identity. The first kill tests are global
positivity/rank stability, a momentum-local conserved source module, both TT
polarizations, Newtonian/static residue reachability, and compatibility of
the GNS intertwiners across momentum/refinement. In parallel, one should test
whether the full action supplies a quantum commutator and local positive-energy
or repeated-interaction Record law. A fitted bath, arbitrary branch-cut
Hamiltonian, or relabeling of the stationary Gaussian covariance does not
count.
