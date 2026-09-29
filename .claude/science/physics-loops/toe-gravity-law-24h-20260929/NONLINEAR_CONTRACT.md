# Nonlinear target and first necessary subsystem

Frozen 2026-09-29, source main `7146fe17a76de41badcaca3c3c7cac6d11eb2a00`.
Author status: open. No axiom, primitive or source status is changed.

## Conventions

Six independent real canonical pairs are `(h_jj,P_jj)` on vertices and
`(h_ij,P_ij)`, i<j, on ij-face centers. `{h_A(x),P_B(y)}=delta_AB delta_xy`.
The continuum matrix momentum has diagonal entries P_jj and off-diagonal
entries P_ij/2. Lattice spacing and ambient tick are set to one for computation;
restoring spacing divides each difference by a. K and alpha are positive.

Write D+f(x)=f(x+e)-f(x), D-f(x)=f(x)-f(x-e), Delta=D-D+.
The vertex curvature functional has derivative
`dR1[N]/dh_jj=-sum_i Delta_i N+Delta_j N`; its face derivative is
`2(N00-N10-N01+N11)`. These derivatives, linearity and R1[0]=0 define it.
`C1[N]=-K R1[N]` and
`T2[N]=sum_x N*(sum_j P_jj^2-(sum_j P_jj)^2/2)/(4alpha)
 +sum_faces A[N] P_ij^2/(8alpha)`.
`G1[xi]=sum_jj P_jj*2D-j xi_j +sum_i<j P_ij*(D+i xi_j+D+j xi_i)`.
Thus `{h,G1}=delta_xi h`, and the verified seed is
`{C1[N],T2[M]}+{T2[N],C1[M]}=G1[F0(N,M)]`, where
`F0_j=K/(4alpha)*(N_x M_(x+ej)-M_x N_(x+ej))`.
Negating both constraints would not resolve the source sign mismatch.

The entire fixed normalized face family is
`A_a[N]=a(N00+N11)+(1/2-a)(N10+N01)`, a real constant.
Nonnegative timings restrict a to [0,1/2]; the algebraic family does not.
All have the same seed. A proper quarter rotation in the face interchanges
the diagonals, sending a to 1/2-a, so full proper-cubic scalar covariance of
this fixed kinetic term requires a=1/4. Other a remain separately supplied
timing probes with the broken symmetry explicit, not silently excluded by T1.

The singular trace case alpha+3beta=0 has the primary trace constraint
sum P_jj=0. It is not covered by inversion, the ratio obstruction or this
nonsingular DeWitt branch. A separate Dirac-constraint analysis remains queued.

## Complete finite-support family to be developed

Use doubled physical coordinates: diagonal slots at 2x, ij slots at
2x+ei+ej, shift slots at 2x+ej. A radius-R density at its smearing anchor
allows EVERY phase-field slot and smearing slot whose physical Chebyshev
distance from that anchor is at most R (equivalently doubled-coordinate
distance at most 2R). R starts at 1. This defines a
particular local class, not every interpretation of 'one cell'.

Take translation-covariant polynomial densities, proper-cubic scalar/vector
covariance, real coefficients, h even and P odd under time reversal.
`C=C1+V2+T2+V3+T3+O(fields^4)`, with Vd containing all h^d monomials,
and T3 all hPP monomials in the declared ball, including displaced pairs.
The first, configuration-space relabelling class takes
`G=G1+G2+G3+O(fields^4)`, with G2 all hP and G3 all hhP monomials.
**Momentum-linearity is an extra hypothesis**, not implied by time reversal.
The complete time-reversal polynomial class also has G3 containing all P^3
monomials. That enlarged class is tested separately below.
G3 is an auxiliary necessary unknown: dropping it would silently strengthen
the mixed-bracket test, since `{G3,C1}` has field degree two.
Every placement of derivatives is represented by expanded shifted monomials.
There is no integration-by-parts deletion of a density with arbitrary lapse.
Only identical commutative monomials and translated *entire smeared
functionals* are combined; kernels are retained and recorded, not discarded
by numerical tolerance. Local canonical changes are candidate equivalences,
never assumed to preserve the support radius without a check.

The target is an exact local identity in arbitrary h,P and arbitrary smearings,
through total field degree two, for CC, GC and GG. This is an off-shell
constraint-algebra identity with a constraint-valued right side, stronger than
checking its value on the common constraint surface. The pure hypersurface
form is supplied: CC=G[F0+F1], GC=C[U0+U1], GG=G[V0+V1], to this order.
F1,U1,V1 are arbitrary h-linear, local smearing-bilinear kernels in their
declared balls; F and V are antisymmetric. The zeroth kernels U0,V0 are
unknown local bilinear kernels with their continuum limits fixed. Momentum-
dependent structure functions and additional constraint mixing are escapes
outside this class. The field-degree-two equations can be nonlinear in the
unknown coefficients (e.g. G2 times V0); they are not automatically one linear
system merely because individual densities have finite bases.

Obligations by field degree:
- CC degree 1: the checked seed. Degree 2:
  `{C1,T3}+{T3,C1}+{V2,T2}+{T2,V2}=G2[F0]+G1[F1]`.
- GC degree 0: zero. Degree 1: `{G1,C2}+{G2,C1}=C1[U0]`.
  Degree 2: `{G1,C3}+{G2,C2}+{G3,C1}=C2[U0]+C1[U1]`.
- GG degree 0: zero. Degree 1: `{G1,G2}+{G2,G1}=G1[V0]`.
  Degree 2: `{G1,G3}+{G3,G1}+{G2,G2}=G2[V0]+G1[V1]`.
Antisymmetrization with distinct smearings is implicit where required.
Canonical Poisson Jacobi is exact; the substituted, field-dependent
structure-function Jacobi identities must also be checked to the orders
justified by these jets. Truncated nested brackets do not prove missing orders.
Terms P^3 first occur at degree three (T2,T3); C4 and higher generators can
also enter that degree. They are a declared next gate, not a consequence of
degree-two success. No complete nonlinear theory is claimed from this jet.

Continuum control: C1=-K Rlinear; C2[1]=T2[1]-K R2[1] with the actual
block62 staggered quadratic symbol. At smooth fields the kinetic correction
is the cubic expansion of
`(tr(g pi g pi)-(tr(g pi))^2/2)/(4alpha sqrt(det g))`, g=I+h.
The spatial limit is -K sqrt(det g) R(g), with its sign checked against C1.
G has the continuum positive Lie action on g. The structure F tends to
K/(4alpha) g^ij(N partial_j M-M partial_j N). These are comparator
normalizations, not derived physical laws. Radius two is priced before expansion.

Proof criteria: local coefficient comparison on the infinite integer lattice
is primary. A finite-torus witness can refute a universal identity; sampled
rank success cannot prove it. Any finite-torus positive certificate needs an
explicit bound on the full residual stencil diameter and side greater than
twice that diameter (a conservative sufficient anti-alias criterion), or a
direct local coefficient lift. Sparse representations, two heavy jobs maximum,
single-thread BLAS, and deadline/stop checks apply.

## First computation: axial diagonal necessary restriction

Set all fields and smearings independent of y,z; keep only
`A=h_xx,B=h_yy,C=h_zz` and their three canonical momenta. Use shifts along x
only. This restriction is applied after forming brackets. C1 derivatives and
G1[xi_x] have only diagonal entries here, so the CC degree-two subsystem
does restrict to these variables; discarded shear/transverse derivatives do
not supply missing terms. Every 3D solution in the declared class must pass it.

For this diagnostic set alpha=1,K=4 (speed normalization, not a primitive).
`C1[N]=4 sum N Delta(B+C)`; T2 is the site DeWitt quadratic form above.
V2 and T3 use every diagonal slot at x-1,x,x+1: 45 and 405 raw monomials.
G2 on edge x+1/2 uses every hP pair at vertices x,x+1: 36 monomials.
F1 uses the six h slots at x,x+1 times `(N_x M_(x+1)-M_x N_(x+1))`.
No axial reflection or transverse-exchange coefficient reductions are imposed
initially: this enlarges the necessary system. Full cubic constraints can be
added if it survives. The face-timing parameter drops out on this sector.
Exact uniform normalization is `V2[1]=-2 sum(D+B)(D+C)`.
The summed T3 coefficients for each field-component monomial equal the
displayed continuum kinetic cubic polynomial.
For G2, the zeroth moment vanishes and first moments give the edge density
`-P_A A'-2A P_A'+P_B B'+P_C C'`.
F1's h sums are -1 for A and 0 for B,C.

The first solver tests CC degree two plus these normalizations. It is a
necessary linear subsystem, not the full closure problem. A failure requires
an exact certificate and independent reconstruction before downstream reuse.
A solution only warrants the next mixed/Jacobi stage and full 3D lift.

## Matter and records

This initial restriction is vacuum. Success leaves all common-action matter
cross-brackets, source/shift placement, source conservation, zero modes and
actual record-birth energy/work open. Vacuum failure does not exclude a
modified phase space or an interacting branch with a non-vacuum background.
PR9363 block150 explicitly leaves cross brackets open; its walker-only
extreme-hop theorem is not used as a theorem against this full system.

## Expanded classes and actual progress (2026-09-29 23:00 UTC)

The first necessary system includes CC degree two and GC/GG degree one.
Its exact rational assembly has 501 unknowns, 702 equations, rank 306 and
195 free variables. A complete affine solution has been recombined against
every equation. A separately implemented finite-torus derivative calculation
has independently reconstructed every column and the rank (focused check,
not formal review). Thus lapse-only closure did not decide the target.

Adding GC's degree-two P^2 sector tests
`{G1,T3}+{G2,T2}=T2[U0]` in the momentum-linear class. The radius-one system
is inconsistent with a 14-row exact dual certificate. Its coefficient
equations have now been independently reconstructed. Radius two was priced
at 2,166 unknowns, 3,222 equations and 17,440 nonzero entries; sparse rational
elimination took about six seconds and yields a 706-row exact certificate.
The latter is author-only until separately checked. Neither result excludes
all local gravity, and neither is a formal review PASS.

The following enlarged classes were declared before their computations:

1. Add all G3(P^3) monomials at the bond support. Their zeroth and first
   spatial Taylor moments vanish to retain the specified continuum spatial
   generator. The mixed sector now includes `{G3(P^3),C1}`. Radius one has
   557 unknowns and gives an author 96-row exact certificate; radius two has
   2,530 unknowns and gives an author 748-row certificate. Independent checking
   is pending. The hhP part of G3 and V3 remain arbitrary because they cannot
   alter the tested P^2 sector; no proof of their other brackets is asserted.
2. Also allow CC to contain `C[Z1(P;N,M)]` and GC to contain
   `G[W1(P;xi,N)]`. Z is antisymmetric in lapses; W has no antisymmetry.
   Every allowed momentum and smearing position in the output's radius ball
   is included. Their zeroth/first Taylor moments vanish as applicable,
   preserving the supplied continuum algebra. Radius one has 620 unknowns
   and gives an author 121-row certificate. Other same-order HH and GG
   obligations remain untested; failure of this necessary subsystem needs no
   claim to have solved those obligations. Independent checking is pending.

All enumerations and certificates are in `nonlinear-evidence/`. A modular
inconsistency was used only as an inexpensive diagnostic; stated exact
certificates use rational arithmetic and direct recombination. The small
radius-one proof is being extracted by the independent checker. These are
research checkpoints with N-gate submission coverage pending, not shipped
negative-theorem packets. The normalized face family and singular trace branch
remain in scope; face timing does not enter the axial diagnostic, and an
independent singular-branch pass is active.

### Independent extension checkpoint

The radius-one cubic-momentum and constraint-mixing systems have now been
independently rebuilt by explicit finite-torus derivatives. Every557/620
column agrees, and96/121-row dual witnesses recombine to0=-1. The certificates
use no added-term continuum moment rows (indeed no continuum normalization
except the two longitudinal G2 Lie moments). They therefore survive arbitrary
low continuum moments of the new terms. See independent-axial-check/
EXTENSION_REPORT.md for exact source/input hashes and the anti-alias proof.
Radius-two full mixing has2920 columns and an author752-row exact witness;
its independent reconstruction remains active. No universal-support theorem
is inferred from these finite radii.
