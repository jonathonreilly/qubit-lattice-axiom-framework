# Block 2: massive charged loops and the gauge covariance bridge

Exploratory, personal derivation. No independently reviewed phase theorem.
Target: derive an explicit, spatial-volume-uniform Hessian bound for the
massive charged determinant in units of the Maxwell curl form. Test its
noncompact covariance consequence and the exact missing compact/Hamiltonian
bridges. Do not copy an unproved massless or finite-payload phase claim.

## Candidate direct construction

Use a finite open cubical box in Euclidean dimension d, with real link A and
m-component fermions. Let D(A)=M I+K(A), with M>0, nearest-neighbor blocks
T_xy exp(i e A_xy), ||T_xy||<=t. If q=2 d t/M<1, the log determinant has an
absolutely convergent closed-walk expansion. Pair with its complex conjugate;
log W(A)=2 Re log det D(A). Positivity here follows from invertibility and
conjugation, independently of the block-1 Hamiltonian history argument.

Every closed coordinate walk of length n in an open rectangular box bounds
an integer plaquette chain. Sorting coordinate steps and cancelling inverse
pairs suggests area <=n(n-1)/2 with a filling inside the coordinate bounding
box of the walk. This must be proved carefully, including repetitions and
boundary behavior. A variation has |delta A(gamma)|^2 bounded by filling
area times the filling-weighted curl square. Root incidence inside a radius-n
box then suggests a conservative uniform constant of the form

    |D^2 log W(A)[a,a]| <= e^2 C_d,m(q) ||d a||^2,
    C_d,m(q) <= (m/2) sum_(n>=4) n^3 (2n+1)^d q^n.

Constants and the starting n need verification; backtracking words at n=2
have zero circulation. This is a proposed bound, not yet a theorem.

If verified, a gauge-fixed noncompact measure with density
exp[-beta ||dA||^2/2] W(A) has Hessian between
(beta-e^2 C) d^*d and (beta+e^2 C) d^*d when beta>e^2 C. Integration by parts
and covariance/score Cauchy-Schwarz give the lower covariance comparison;
the upper requires the checked Brascamp-Lieb inequality. This would provide
bounds for a supplied massive Euclidean model, not a full scaling-limit or
Hamiltonian theorem. Compact cosine gauge actions are not globally convex;
periodic boxes also have winding loops and flat holonomies, so the open-box
argument must not silently replace those sectors.

## Source and novelty review so far

- Current main finite-clock and constrained-fiber KP notes were compared in
  block 1. The latter uses a different small-beta/high-mass hidden fiber.
- Main keyword search found no direct Brascamp-Lieb / gauge-determinant
  uniform-convexity note, but this is only a bounded text search, not proof
  of novelty.
- Dimock 1988, Numdam AIHPA_1988__48_4_355_0: introduction and model text
  pages 2-6 read. Many formulas are images missing from extracted text; they
  require visual inspection. The paper's full stated target is a bounded-field,
  massive, noncompact Euclidean RG theorem. Dimock-Hurd 1992 abstract announces
  removal of the field restriction, but its full source has not been recovered.

## New compact-defect probe — derivation not yet checked

Normalize compact matter charge to integer e=1. The chosen integer fillings
extend the determinant action from exact F=C A to all plaquette fields:

    L_tilde(F)=2 Re sum_(rooted gamma) a_gamma exp(i<s_gamma,F>).

For physical Villain F=C theta+2 pi n, integer n and integer filling
multiplicities make exp(i<s_gamma,F>)=exp(i gamma.theta). Thus the extension
reproduces the determinant exactly on every Villain sector; it is not a
replacement action. The same area/incidence proof bounds its full plaquette
Hessian by c_d,m(q) I, including non-closed variations. Wilson traces should
make this extension even; this needs an exact coefficient-level check, not
only evenness on closed fields. Alternatively use the explicitly evenized
four-determinant model and double the constant.

If S(F)=beta||F||^2/2-L_tilde(F) is even and its Hessian lies between
kappa I and K I, integrate over X=range C at fixed orthogonal defect y:

    R(y)=-log integral_X exp[-S(x+y)] dx.

The candidate exact marginal Hessian formula is
R''=E S_yy-Cov(S_y). Brascamp-Lieb in x and the Schur complement give
R''>=kappa I; trivially R''<=K I. Evenness gives R'(0)=0, hence the ratio of
one defect-sector integral to the defect-free integral is bounded by

    exp[-K||y||^2/2] <= Z(y)/Z(0) <= exp[-kappa||y||^2/2].

This avoids a volume factor from comparing two Gaussian partition functions
separately. For y=2 pi (I-P)n the exponent is the usual Coulomb defect energy,
with a controlled stiffness interval. Need prove the integer cochain quotient,
periodization/gauge-volume normalization, marginal identities and evenness
before claiming a compact result. The internal open-box complex differs from
the exterior Dirichlet exhaustion used for the noncompact field theorem;
keep those boundary choices separate.

This sector ratio would still not prove a compact Coulomb phase. Summing
interacting monopole sectors needs an entropy/interaction or correlation
argument. The full Villain F has dF=2 pi dn, so the Bianchi identity used in
the noncompact non-summability proof fails configuration by configuration.
Projecting to P F restores closure but makes the observable nonlocal; it
cannot silently replace a local physical field strength. Positive Fourier
type of a dual measure is also not implied by convexity or phase-weight
positivity. These are precise next proof obligations, not an axiom no-go.

## Checkpoint: compact sector bounds and the exact remaining response target

The compact derivation now includes the integer tensor contracting homotopy,
full-space Wilson trace evenness, normalized Haar periodization and a marginal
Schur-complement proof. Six exploratory families currently pass; all source,
stdout, stderr and machine-readable results are retained. A strict example
bounds mean squared defect density by 4e-27. This is an author-proposed result
for supplied massive compact U(1) Villain data, not a finite Z_N phase theorem.

Two controls sharpen the phase task: dilute large closed loops can defeat any
inference from density alone to small infrared susceptibility; and an exact
r=2 Wilson square determinant fails positive Fourier type. The actual model's
loop-energy/area response remains available and open. The next scientific
question is whether the pure-model renormalized-current machinery can be
adapted with fully checked determinant/complex-shift hypotheses. No new
axiom is forced by either bounded inference failure.
