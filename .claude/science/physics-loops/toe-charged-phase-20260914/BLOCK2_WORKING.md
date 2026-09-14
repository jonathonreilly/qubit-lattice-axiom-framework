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
