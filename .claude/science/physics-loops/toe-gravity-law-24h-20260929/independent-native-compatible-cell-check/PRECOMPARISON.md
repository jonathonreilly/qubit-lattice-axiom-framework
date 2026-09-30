# Independent precomparison: compatible native cells

Before reading REPORT04e13444 or PERIODIC_CELL_BRIDGEb99af6fa. Root read the
contract and source bindings and has complete prior focused checks of the
actual native operator, many-particle bad-particle bounds, threshold definition,
upper trial and Neumann lower bound. Author briefs exposed the guarded-map
idea, candidate cell-gap/trial constants, low-band claim and kinetic boundary
counterexample. This is a focused reconstruction with that exposure disclosed.
No new threshold numerical result will be used as a premise.

Select every R-isolated occupied graph edge as a dimer, retaining all other
particles as an environment word. The pair/environment data uniquely recover
the actual occupation set and define a basis isometry. Removing a selected
isolated edge cannot cause another edge to become isolated: every remaining
particle was farther than R from both removed endpoints, so this pair had
not obstructed any remaining candidate. Thus guarded physical annihilation
intertwines free edge annihilation on the constrained image. Free creation
need not preserve that image; no canonical physical CCR follows.

A kinetic estimate needs more. Moving an edge across a sharp isolation guard
changes the projector, with boundary cost tied to nonisolated particles. At
fixed R its coefficient may grow like R³; averaging R over[r,2r] can save one
factor and give O(r²) times the physical energy. The actual gradient row
geometry, environment overlaps and every incidence constant must be checked.
A constant incoming N4 profile cut at a guard boundary has O(R²) gradient
surface energy while its original interaction energy stays fixed, so a uniform
O(1) kinetic-intertwining assertion would be implausible.

For a whole periodic cell with N=2n, use this isometry J and the projection P0
onto n particles in the five constant soft modes with empty bad environment.
If bad-particle probability plus nonsoft depletion is bounded by C L² H/a,
then ||(I-P0)Jpsi||² has that bound. The physical soft-image subspace is
Ran(J*P0). Its orthogonal complement Q satisfies Q J*P0=0, whence
||Qpsi||<=||(I-P0)Jpsi||. This would prove the global form H>=Delta Q,
not merely QHQ>=Delta Q, without discarding cross terms.

The physical image of an n-pair constant-mode vector equals its free-edge
wave restricted to mutually separated physical edges. For arbitrary internal
entanglement, ordered anchor coordinates still have exactly uniform product
marginals because all one-pair momenta are zero. A union bound over pairs of
anchors should give Gram>=1-binom(n,2)(2R+9)^3/L³. This proves injectivity and
rank binom(n+4,4) when the bound is positive; it does not imply unrestricted
all-N equivalence. Check bond-type anchor offsets and polar normalization.

For a separated physical frame vector, D=0 and ordinary pair removal equals
guarded removal. Its actual energy is therefore the free K2 quadratic form
of the zero-extended allowed-position wave. Only guard-boundary gradients
and onsite high-mode mismatches remain. A shell-volume bound should give
O(n(n-1)/L³) at fixed R, divided by the Gram lower bound after polar
normalization. Numerical coefficients require the actual source rows, not
counting free independent dimers without the constrained image.

If P is that physical image, A=PHP<=theta P, D=QHQ>=Delta Q, and H>=0,
then B*D^-1B<=A. For0<=z<Delta, the exact finite Schur operator obeys
0<=F(0)-F(z)<=z theta/(Delta-z). The low eigenvalues below Delta are governed
by F(z). Min-max gives exactly dim(P) low levels when theta<Delta and the
next level at least Delta. A useful comparison is
(1-theta/Delta)lambda_i(F(0))<=lambda_i(H)<=lambda_i(F(0)),
subject to checking endpoint/zero eigenvalues and the precise source statement.
This is finite-cell spectral information; identifying F(0) with a pairwise
T0 interaction uniformly in n is a NEW lemma, as is cutting a large physical
system into periodic cells without losing an order-rho² boundary energy.

For the internal d=5 reduction, direct complex-sphere monomial integration
suggests the normalized Husimi second moment identity
M2=[n(n-1)gamma2+4n P_sym(gamma1 tensor I)P_sym+2I_sym]
                                   /[(n+d)(n+d+1)].
Trace checks give n(n-1)+2n(d+1)+d(d+1) equal to the denominator. For positive
T this yields a lower bound in terms of min_z<z tensor z,T z tensor z> with
an O(n||T||) correction, without assuming condensation or a chosen coherent
channel. Compare all normalizations against the actual guarded coarse-field
functional. This elementary derivation does not import a dilute-gas theorem.

No proof or new computation is adopted by this precomparison. Full source,
constant/error, domain, Feshbach and finite control checks remain required.
