# Block10 cold source and scope review

2026-09-13, same executing author. Independent source review remains pending.
Read the full derivation, local-to-global force checker, different nonlinear
force checker, recorded failures and literature-scope record. This pass does
not convert finite-step diagnostics into interval or all-order proofs.

The leading source sign is consistent: Delta_lat Phi in section6 means
Phi_(n+1)-2Phi_n+Phi_(n-1), whereas the inverse used for u in section7 is the
positive Laplacian 2-shift-shift^-1. The exact checker verifies Qv=J1 with
that sign. No sign repair is needed.

The C1 necessary-condition argument is valid on each fixed nondegenerate
finite torus. Writing displacement d(epsilon)=epsilon v+o(epsilon), the fixed
flat null vector kills Q d(epsilon) identically. The quadratic gradient is
epsilon² N(v)+o(epsilon²). Thus no second derivative of the family is needed.
Temporal-edge-only source work on the chosen static displacement is zero
at every amplitude. This hypothesis is stronger than arbitrary matter coupling.

The longitudinal condition is g_n²=g_(n-1)². On an odd periodic cycle, a
nonzero real constant-magnitude gradient cannot sum to zero. Even-period
balanced signs survive this particular condition. Higher-order corrections
may leave plane symmetry; the fixed null projection still applies. Added
constant first-order metrics do not change its g² coefficient: cube inversion
makes it even in g, homogeneity fixes degree two, and at g=0 the hyper-family
cubic has no derivative in the longitudinal diagonal metric direction.
This is an analytical argument, not merely the small finite fixture.

The uniform-modulus exclusion is quantified separately for a pure scalar
tangent with free constant metric modes. Do not apply it unchanged to a
wider first-order tangent or constrained global modulus problem. The local
hyperdiagonal equation itself preserves lambda=0 for every static scalar
and displacement field; it does not supply a scalar obstruction.

The repair is stronger than an isolated projection cancellation. The full
15-edge gradient N has the stated four axis entries; all other entries
vanish. The independently prescribed J2 and explicit zero-mean u solve the
entire finite Qw+N=J2 equation. Analyticity then proves the fixed-volume
O(epsilon³) remainder. The nonlinear checks challenge its coefficients and
scaling, while their finite step sizes are not a proof of convergence.
Both final code hashes and the nonlinear helper hash match the existing
passing records (24 exact checks,8 nonlinear diagnostics). No source changed
or unresolved numerical concern justifies another identical run in this pass.

The source correction is an externally supplied potential depending on a
chosen leading Phi. It is not a stress tensor derived from native matter.
In particular a leading density chosen first may require inverse-Poisson
information to construct it. The next useful derivation is a specified local
matter/support action whose own equations supply all needed virtual work.
Simply matching the source to the geometry path would not close that task.

Negative-claim packaging is deliberately still unresolved. The five-family
N1 schema cannot be counted from multiple notations or projections of this
one compatibility identity. The concrete escapes preserved here are an added
spatial stress (constructed through second order), changed leading/background
or dynamical source families, even-period balanced gradients for the single
longitudinal condition, and the surviving lambda=0 hyper equation. They are
not all ruled out; no universal no-go or axiom-forcing claim is supported.
This review does not claim an N1-N8 packet PASS or ship a negative-result PR.
A future positive second-order completion unit can state its actual equations
without promoting the historical source-family exclusion to global necessity.

No code, physical axiom, primitive, audit verdict or editable prompt changed.
