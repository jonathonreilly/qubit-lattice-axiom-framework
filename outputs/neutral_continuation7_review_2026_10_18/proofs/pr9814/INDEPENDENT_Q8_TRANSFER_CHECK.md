<!-- Original PR9814 source SHA256 90d33e4e0240a9fc5d1e2d36cfec0171ee50c57e53e72d1f7e398bf29a56aed2. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Q8 pair-band transfer and positive dispersion

Disposition: PASS for the proposed rank-two band transfer and ordered-band dispersion bounds, conditional on the inherited uniform local normal form and the independently supplied complete order-lambda^18 source coefficient. No internal orientation gap or global-ground selection is required for these conclusions.

## Symmetry and the two-orientation matrix

Choose the horizontal minimum as flipped columns at r+/-ex and the vertical minimum at r+/-ey. Their common center r is an integer lattice site. Spatial inversion maps each centered configuration to itself, with no half-cell phase and no exchange of orientation. In the positive plane-character quotient all background-orbit amplitudes have positive sign, so inversion introduces no character phase. The supplied XX/YY/ZZ Hamiltonian is real in the physical Z basis. Choosing the local reductions equivariantly gives

 h(-q)=h(q), h(-q)=h(q)*,

and hence a real even two-by-two matrix. Separate coordinate reflections actually give evenness in each q component. C4 exchanges the two orientation basis states and equates diagonal entries at zero. Thus no off-diagonal odd-q term is allowed in this centered convention. An uncentered basis could manufacture Fourier phases, which must not be mistaken for physical linear dispersion.

On the even periodic lattice the microscopic checkerboard Z product maps lambda to -lambda. At L=10 its N0 action is the conserved total column-Z parity (five checkerboard sites per column), a scalar in the stipulated positive sector. Equivariant effective matrices are therefore even in lambda. In particular there is no lambda^15 term.

The checked two-edge enumeration gives no orientation-changing entry at lambda^14. Horizontal-pair translations have coefficients t=gamma^2/D longitudinally and 4t transversely; vertical-pair coefficients are rotated. No other two-edge final minimum occurs. The uniform bounded-displacement local expansion then gives

 h(q)-h(0)=J t lambda^14 diag(qx^2+4qy^2,4qx^2+qy^2)
             +O(J lambda^14 |q|^4+J lambda^16 |q|^2).

This statement needs the inherited spatial-moment control, not just a volume-independent operator norm. It does not set the unknown h(0) mixing to zero.

## Ordered eigenvalue bounds require no orientation gap

The leading matrix difference is bounded between Jt lambda^14 |q|^2 times identity and 4Jt lambda^14 |q|^2 times identity. The min-max principle therefore bounds the increment of each ordered eigenvalue of h(q) relative to the same ordered eigenvalue of h(0) by these endpoints, with relative o(1) corrections. This is valid even at an internal degeneracy and for any unknown q=0 mixing. It proves positive resolved increments of both ordered bands, rather than an isotropic scalar curvature coefficient or a differentiable eigenvector at a degeneracy.

For q=2pi n/R, fixed nonzero n and any fixed 1<p<2, the signal is order lambda^(14+2p). A global tail R^2 lambda^40 has relative size lambda^(26-4p), which vanishes. Exact translation symmetry lets the comparison be made in each momentum fibre. No small inter-momentum spacing is used in a projector denominator.

## Actual cluster and source

The Q8 minima have a gap (D/2)J lambda^6 to the nearest other Q8 configuration, not D J lambda^6; the latter is the gap to two well-separated single-column clusters. Uniform higher coefficients are smaller, so a rank-two endpoint cluster in each momentum fibre is isolated. Other Q charges are separated at order lambda^4 and the whole N0 band has an order-one separation from walls. The first normal-form embedding remains valid because lambda^4 R^2 tends to zero. This establishes a rank-two exact microscopic spectral cluster after the arbitrarily high fixed-order remainder is included.

An internal orientation gap is unnecessary for projection onto this cluster. The full-H cluster-projector error is at worst O(R^2 lambda^(40-6))=O(R^2 lambda^34). Even multiplying by ||C||=O(R) gives source error O(R^3 lambda^34), with exponent 34-3p>28, negligible against lambda^18. Ground errors use the larger lambda^4 gap and are smaller. Fixed-order normalized defect-creating source coefficients have the same finite-pattern Gram bound as in the Q4 proof after removal of scalar vacuum pieces.

Assuming the checked matched original-source vector is

 lambda^18 M(A+B)/sqrt(L)+o(lambda^18),

the total cluster weight is 2M^2 lambda^36/L [1+o(1)]. The earlier source calculation explicitly includes direct derivatives and ground/excited-state mixing; its nontrivial QSW connection must not be dropped when changing frames. The present transfer uses that full matched vector as input and does not independently establish completeness of its native path classification.

At q=0, C4 symmetry separates the even and odd orientation combinations exactly. The uniform original source couples to the even component only. Thus the cluster's leading weight is in its even-sector atom; the sign or size of the unknown mixing determines whether that atom is the upper or lower member. If they remain degenerate, there is still an atom with this total weight at their common energy. An assertion that two individually simple poles are separated, or that the source necessarily selects the lower ordered branch, would require an additional result and is not supplied here.

The selected positive plane fibre is an explicit state premise throughout. This argument does not select the full global ground uniformly in growing R, identify a scattering process, or supply universal coupling.

Sources reused: /tmp/neutral-eightflux-cluster-check.md, /tmp/neutral-q8-source-check.md, and the current native POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md. No shared edits or formal audit.
