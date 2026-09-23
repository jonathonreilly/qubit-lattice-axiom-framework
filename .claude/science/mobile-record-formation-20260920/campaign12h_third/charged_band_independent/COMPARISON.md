# Charged-band author comparison

2026-09-22. Bounded post-seal scientific comparison. **No material mathematical
error or required source correction was found.** The author's Hessian agrees
with the blind quadratic coefficient after the factor-of-two convention is
resolved. The additional all-direction bound and sign-change equivalence were
reconstructed separately below; they were not inferred from agreement on the
blind transverse family. The compact packet statement has the stated fixed-box
scope and the correct leading O(sqrt(h)) residual.

The blind REPORT remains unchanged at SHA256
`96dccc1aecdf2ca58018c23cd36f70dbbb87775c85a7e8e54683cece9bf68f0e`.
Its PRE seal remains
`4c13933f96f93217a20683f9b229d50c7e97fab28a556f90cce0226858ad3e48`.
All 33 PRE bindings authenticate, including both preserved failed/interrupted
attempts. This comparison is a separate later artifact, not part of the blind
reconstruction and not a formal audit or publication decision.

## 1. Exact source and evidence coverage

The author seal is `CHARGED_BAND_AUTHOR_SEAL.json`, SHA256
`c1c6420437307f014d547aaab23e261547d667e15eec0e736a600b0d75abf581`.
All 25 bound artifacts authenticate. The complete scientific note
`CHARGED_RECORD_EXCHANGE_BAND_FIELD_RESPONSE.md`, SHA256
`25cb71ce9816b5cbde292aa31567dea3d3bd694fae80a1d22992e785e19627ca`,
was read, including its uniform star bound, compact bundle construction,
scoped negative inference and sign-equivalence extension.

The three complete current scientific runners, every field of their complete
results, source context, all current receipts and streams, and the preserved
failed packet attempt and diagnostics were inspected. Successful stdout equals
the corresponding result bytes. The whole archived/current packet source delta
contains only the two declared cutoff changes. The earlier archived receipt
was authenticated against the archived source/streams, not their overwritten
live paths. No new author source was executed or imported.

The current runner identities are:

- `charged_record_potential_hessian_check.py`:
  `9a87946905e3259c04200c8a353e608ee6d5ae7733c617f1826ce8189c386563`.
- `charged_band_packet_check.py`:
  `2f1d9a8a834bd198d2337029ca25573d4a1d9efa2327b00592f22760251ae497`.
- `charged_band_geometry_check.py`:
  `192adb9cb90eeea831af86e57518647edbb0bed6343e9d6054e7742739b2e0ee`.

Their result identities, in that order, are
`699c7b6afa673e0cbe90f409a383855af08cacedf7879c4e5da084744887f5ba`,
`38746e8def0ffd5183ade5aca9493e853aadd6097843762f26fa768138902ec8`, and
`03e0df65745dab7d6b52e12ad52182b6f20b007336da619cc540849c00c44b31`.

The preceding homogeneous target note and its author seal match the already
checked source identities. They are needed only for optional composition: the
present Hessian and packet proof can be read directly for the supplied rotor
Hamiltonian. No new external theorem was imported. Finite-rate/repeated-
formation/locality author packets, checkpoint, registry and unrelated frontier
work remain unopened. The historical external-source reference in Section 6
was not treated as a dependency or independently re-reviewed here.

## 2. Quadratic coefficient versus Hessian

The blind report uses chi=T a as the **sum** of the two directed a-to-c paths,
whereas the author uses theta=Theta a=chi/2, their **average**. The author's
A-graph incidence is the transpose with opposite orientation to the blind
vertex-by-edge incidence. These changes do not change its cycle projector.

If Q is the blind matrix multiplying the quadratic power in

    e(a)=e(0)+a^T Q a+O(|a|^4),

then the author's true second-derivative matrix is

    M_J=2J Q.

Thus its Eq. (6), including both the curl coefficient and the projected path
coefficient, agrees exactly with the blind formula. Its constant-connection
curvature 4J n(d-1)/(n-1) is twice J times the blind quadratic eigenvalue
2n(d-1)/(n-1). Likewise omega0 sqrt(2 mu), with mu an eigenvalue of M_J/J,
equals the blind frequency 2 omega0 sqrt(lambda(Q)). There is no missing or
extra factor of two.

The complete charge-transposition derivation, neutral Dicke ground, local
simple-band condition and reduced-resolvent calculation agree. The author
correctly differentiates the actual exchanged-charge phases. It includes the
matter-relaxation subtraction, rather than replacing it by a fixed-vector
expectation. The analytic band gap is a fixed-box gap, not a claimed uniform
ferromagnet gap. The site's immutable charge remains unchanged when the
combined raising/lowering notation exchanges two records.

## 3. Independent reconstruction of the new all-direction bound

The star argument is sound and supplies a genuinely stronger bound than the
blind report's positive-definiteness proof. It does not need numerical spectra.
Using the blind path-sum convention, put

    F(a)=||C a||^2+||Pi_cycle T a||^2.

For each plaquette, before minimizing over real A-vertex phases f, the two
terms combine into twice the sum of the squared adjusted two-link paths.
Grouping these paths by their B corner counts each local unordered
perpendicular pair of incident links exactly once. At that corner the 2d
A neighbors form the complete d-partite graph with two vertices per part;
opposite directions are the missing pairs. Therefore

    F(a)=2 min_f sum_(b in B) u_b^T L_star u_b,
    u_b(a-neighbor)=a_(a->b)+f(a).

With z=2d, L_star=(z-1)I+O-11^T, where O swaps opposite directions. It has
constant eigenvalue 0, eigenvalue z-2 on vectors antisymmetric in one opposite
pair, and eigenvalue z on the d-1-dimensional pair-constant zero-sum space.
These invariant spaces are orthogonal and exhaust the 2d dimensions.
Consequently

    (z-2) min_s ||u-s1||^2 <= u^T L_star u
                              <= z min_s ||u-s1||^2.

For the lower bound, minimize both sides over the A phases and independent
B-corner constants. This is precisely the full vertex-gradient least-squares
problem. For the upper bound, insert the full least-squares minimizers before
applying the upper star estimate. These different minimization directions are
both justified; no upper/lower interchange is being assumed. The result is

    4(d-1)||P_transverse a||^2 <= F(a)
                                  <= 4d||P_transverse a||^2.

Since the two Hessian weights obey
(n-2)/(n-1) <= n/(n-1), the author's Eq. (13) follows:

    4J(d-1)(n-2)/(n-1) P_transverse
         <= M_J <= 4Jd n/(n-1) P_transverse.

The physical space here includes the harmonic directions. The constants are
independent of box volume at fixed d; n>=18 makes the lower bound positive
uniformly. This is a potential-band curvature statement. It does not supply
uniform bounds on the derivatives of the band eigenvector used in the packet
argument or prove a gap of the complete compact matter-field Hamiltonian.

A new selective control independently assembles the entire 6x10 rectangular
torus. It constructs the completed-star Gram matrix in link variables and
A-phase variables, then eliminates the latter. It separately constructs F from
curl/path incidence. Their maximum entry difference is 8.89e-16. On the full
61-dimensional physical tangent space the F spectrum runs from 4 to 8, within
floating error; the actual Hessian lies between 3.8620689655 and 7.8672188372,
inside the analytic bounds 3.8620689655 and 8.2758620690. Exact invariant-space
checks of the local star were also made at d=2,3,4,7. These are post-seal
controls of the additional claim, not repetitions of the blind axis probe.

## 4. Physical compact packet and its error

The author's packet proof matches the independent construction in the points
that matter. The full compact vertex-gauge quotient retains d harmonic
coordinates. Its tangent space has dimension (d-1)V+1. The projected integer
lattice is discrete because the gauge projector is rational. Charge-dependent
line-bundle twists are retained; a small local section supported away from
chart boundaries defines an actual physical state.

In the local parallel frame, the exact kinetic operator is the transverse
Laplacian plus the finite diagonal Coulomb matrix q^T L_vertex^+ q. Here the B
in the author's Eq. (18) is the oriented vertex-by-link divergence matrix;
it is distinct from the earlier diagonal A-graph incidence D and from the
checkerboard named B. The integer lattice exponent denotes the number of
links, not the Hessian matrix also called M. These conventions reconcile the
formulas without changing any operator.

A useful independent check of the frame is to restrict the original Gauss-
equivariant angle wavefunction to the orthogonal transverse slice. The
longitudinal electric vector is B^T(BB^T)^+q, orthogonal to the slice, so its
norm square gives exactly that Coulomb matrix. Restricting the actual path
current phases gives the same magnetic matrix (4). There is no missing local
vector potential from merely using the twisted global boundary conditions.

For u(A) the analytic lowest matter eigenvector, the prepared packet is a
cutoff times u(A) times a scaled oscillator function. The proof keeps all
three relevant errors:

- The band-energy remainder is O(|A|^4), hence O(h) after division by h and
  the scaling A=sqrt(h)x.
- The cross derivative -2 omega0 sqrt(h) grad_A u dot grad_x psi is generally
  nonzero and supplies the sufficient O(sqrt(h)) error. The second derivative
  of u and the Coulomb matrix contribute O(h).
- Cutoff derivatives and normalization errors are exponentially small for
  the stated finite Hermite combinations on fixed time intervals.

The independent PRE allowed more general Schwartz packets and obtained
polynomial cutoff-tail estimates with the same O(sqrt(h)) conclusion. The
narrower Hermite choice makes the author's exponential tail statement valid.
Self-adjointness of the finite collection of twisted compact Laplacians plus
bounded matrix potential, followed by the displayed residual/Duhamel argument,
is sufficient. No unproved exact adiabatic following is inserted.

In particular, a uniform Hessian lower bound does not turn Eq. (22) into a
volume-uniform dynamics theorem: its eigenvector derivatives still involve
the finite matter gap and chart. Nor does a localized packet construction
identify the global ground state or exclude other minima/tunneling. The source
keeps its actual conclusion at fixed box, finite time and prescribed band
preparation. Its ordered optional microscopic composition first holds h and
the box fixed, then takes the independently checked spin/dressing limit, and
only afterwards h->0. The declining formation schedule is not strengthened.

## 5. Auxiliary packet computation and precision history

The auxiliary one-coordinate model is correctly separated from the full cubic
Gauss system. I independently rebuilt its six-dimensional matter matrix and
obtained true band Hessian 4/3 and ||u'(0)||^2=5/12. These imply oscillator
frequency sqrt(8/3) and the two leading residual constants stated in the note.

A single new finite evolution used h=1/64, Fourier cutoff 144 and grid 4096,
with a different unshifted-angle FFT convention. Its Hamiltonian was assembled
from Fourier coefficient matrices and Kronecker shift operators, rather than
importing the author's coordinate loop. At time one the error was

    0.005685886436408639,

versus the author's 0.005685886437149036, a difference of -7.40e-13. The two
residual norms were 0.103511238001865 and 0.178819862387877. They give the direct
Duhamel bound 0.199638235625464. This supports the implementation and rate/sign
normalization; the loose sufficient sqrt(h) bound need not be saturated by the
actual state error. No claim of a full author sweep or full cubic evolution is
made. These floating checks are not rigorous interval enclosures.

The preserved initial author packet run really exceeded its declared 1e-9
refinement target: the recorded difference was 1.2704779004e-9. The independent
spectral-propagator diagnostic reproduced it. The complete source delta only
raises the base cutoff coefficient 8 to 12 and the refinement increment 20 to
60; it leaves the threshold, equations and scientific checks unchanged.
The corrected recorded refinement difference is below 6.6e-13. Original source,
streams, receipt and diagnostics authenticate and remain preserved. I did not
replay the failed numerical attempt or every cutoff diagnostic.

The author Hessian runner labels its two-mode 3D Ritz calculation honestly:
its subspace leakage is nonzero. The first Ritz member can agree with the
blind axis eigenvector without making the entire two-mode subspace invariant.
No dispersion eigenvalue or phase conclusion is inferred from suppressing that
leakage. The new all-direction proof removes dependence on that insufficient
ansatz. The auxiliary side-four incidence cases are finite geometry controls;
they do not enlarge the preceding microscopic theorem's period-at-least-six
hypothesis.

## 6. Independent reconstruction of the sign equivalence

For stored edge (x,i), define nu_(x,i)=sum_(j<i)x_j mod 2. On an even periodic
box, every elementary face has odd oriented nu circulation. A wrapping step
changes a relevant coordinate by 1-L_i, still odd, so the wrapping faces obey
the same parity identity. With integer E,

    T_pi=exp(i pi sum_e nu_e E_e)

is a well-defined unitary commuting with Gauss, charges and the electric
Hamiltonian. Each of the four supplied record-induced link increments is an
odd integer, including its stored-orientation sign. Modulo two their charged
phase is therefore exactly the plaquette nu parity, independent of both
transported charge signs. It follows that

    T_pi R_p T_pi^dagger=-R_p,
    T_pi H_- T_pi^dagger=H_+.

This is a full target-operator identity, not merely a Hessian equivalence. It
moves the band minimum to a periodic pi-flux connection. It does not state
that the positive-sign Hamiltonian's zero-angle minimum or a different
microscopic statistics model is unchanged.

Independent finite parity controls used boxes 8x10 and 6x6x8, checking 3,776
charge-dependent signs, including wrapping faces. All reverse as required.
The same formula on the out-of-scope 7x7 geometry fails on 28 of 196 cases.
This is a cochain countercontrol to dropping the even-box premise for this
formula, not a proposed odd-torus checkerboard model or a classification of
all alternative sign transformations. The analytic parity argument supplies
the all-size conclusion under the actual premises.

## 7. Disposition, remaining limits and evidence

No source repair is requested. The source correctly distinguishes:

- true Hessian from quadratic coefficient;
- potential curvature from the complete interacting spectral gap;
- fixed-box prepared packets from a thermodynamic phase or uniform-volume
  weak approximation;
- sign-only unitary equivalence from a derived fermionic microscopic theory;
- corroborating finite numerical controls from the analytic arguments.

The uniform bound is an additional author result confirmed here after the
blind seal. It is not attributed retroactively to the PRE derivation. The
sign-equivalence check is likewise new post-seal work. The source's scoped
negative conclusion does not exclude other bands, preparations, coupling paths
or intermediate-coupling phases. No such external sector was investigated.

`comparison_check.py` completed on its first execution. Its full result and
streams were read; no new failed comparison execution occurred. It authenticates
all 33 PRE rows, all 25 author rows and the two context identities. Exact star
invariant spaces, rectangular full-space comparison, parity controls and the
one-row auxiliary packet reconstruction are separately identified in its
result. The original independent PRE failures remain untouched.

`FINAL_SEAL.json` binds this comparison, its checker/results/receipt and all
source identities without rewriting any PRE file or author science. It records
the limited new execution coverage rather than presenting authenticated author
logs as independent calculations.
