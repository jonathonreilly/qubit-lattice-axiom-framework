# Independent reconstruction before author-code/results access

2026-09-21. The three supplied plans/operator arguments were read completely.
No author implementation, checker, production metadata, analysis code or results
has yet been opened. This is an independent reconstruction from those stated
arguments, not a blind-to-note discovery.

Let F be an admissible seven-state field, n(F) its occupied-site count and
D the signed incidence operator of the centered charge graph. A positive
axis label at midpoint x is the directed edge x-e_i -> x+e_i. With this
orientation D is exactly D2. Let

    Omega = {(F,t,h): D F = delta_t-delta_h},
    mu(F,t,h) = Z_ext^(-1) z^n(F), z>0.

A proposed head step from h to h+2s e_i adds s at the midpoint h+s e_i.
Its divergence change is delta_h-delta_(h+2s e_i), so it preserves the
constraint. Capacity allows exactly creation at an empty midpoint or
cancellation of the opposite same-axis record. Every admissible proposal
has its reverse with the same 1/6 proposal probability. Metropolis acceptance
min(1,z^Delta_n) therefore gives detailed balance for mu. Rejected proposals
stay in the same extended state.

At h=t, uniformly replacing both endpoints by a new common site preserves
mu because every closed F has exactly V equally weighted endpoint copies.
This relocation kernel need not commute with the worm-step kernel; their
composition still preserves mu. No assertion of detailed balance for the
composition is required. Endpoint relocation before each proposed move from
a closed state is valid.

For C={h=t}, the finite trace kernel at successive times in C, including
one-step returns and holds, is

    Q = M_CC + M_CO (I-M_OO)^(-1) M_OC.

Its stationary law is mu conditional on C; summing out the common endpoint
leaves pi_z(F) proportional z^n(F) 1_(D F=0). Irreducibility below ensures
finite return times on the finite state space. A deterministic every-k-th
trace visit also preserves this law when initialized stationary; neither
this observation nor stationarity proves finite-burn-in accuracy. Stopping
production while a worm is open and retaining the completed visits is not
force-closing or discarding that worm. Finite-run transients remain possible.
Dropping repeated closed configurations instead creates a jump-chain
selection bias proportional to the state-dependent departure probability.

For accessibility, every balanced occupied directed edge graph is a union
of directed cycles, allowing shared vertices and branched components.
Choose a cycle vertex as the tail. Following the cycle backward removes
one occupied edge at a time with positive acceptance. No midpoint capacity
conflict is introduced by removal. After closing, repeat on another cycle.
This reaches the empty field, and reversing the path reconstructs the
original field through admissible creations. Global tail relocation handles
all cycle components. The proof includes noncontractible winding cycles;
it does not require contractibility or a small fugacity. The same reasoning
works on even tori despite their separate charge-parity components.
For an open feasible field, directed-flow decomposition supplies a directed
path from t to h plus cycles. Removing that path backward reaches a closed
field, so there is no inaccessible open trap. These are finite positive-z
reachability statements, with no quantitative mixing time. Very small
acceptance or long return times can make them useless as practical mixing
bounds.

## Independent exact reduced-geometry discriminator

A square charge graph has four directed edges around its boundary and four
distinct midpoint slots, each in {-1,0,+1}. This differs from the proposed
one-dimensional three-site author toy. It deliberately does not test all
cubic midpoint/axis competition; that remains a source-inspection obligation.
At z=2 the full extended state space has 36 states, including 12 closed
states with their endpoint copies. Exact rational matrices verify the
step's detailed balance, relocation invariance, composite stationarity,
closed trace law and accessibility. Ordered as negative loop, empty,
positive loop, the field trace matrix is

    [59/60  1/60       0]
    [ 4/15  7/15    4/15]
    [    0  1/60   59/60].

Its invariant law is (16/33,1/33,16/33), as required by Z=1+2z^4.
Removing field self visits gives invariant law (1/4,1/2,1/4), not the target.
The independently written exact checker passed on its first execution;
full output and empty stderr are preserved.

## Staggering and adjoint operator reconstruction

For an even torus define epsilon_eta(x)=(-1)^(eta.x) and
T_eta F_i(x)=epsilon_eta(x)(-1)^eta_i F_i(x). Each neighboring parity
factor contributes (-1)^eta_i, which cancels the component sign in the
divergence. Consequently D2 T_eta F=epsilon_eta D2 F. The transformation
preserves the single-axis menu, occupation and constrained weight; it is
an involution, not an immutable-record update. It also preserves the shared
capacity of separate E/B sign transformations in the two-species ensemble.

Under the stated Fourier convention the field transforms as
D_eta Fhat(k-pi eta). The finite even-volume grand covariance therefore
satisfies S(k+pi eta)=D_eta S(k)D_eta. Mean zero follows from global field
inversion. Local weak limits of these symmetric measures inherit the
symmetry; spectral measures obey the translated identity even when no
ordinary spectral density exists. An arbitrary symmetry-broken selected
state, or an odd torus across its seam, need not satisfy it. Charge vertices
split into eight parity classes on the infinite/even lattice, but midpoint
capacity couples the classes statistically.

For a separately stipulated centered Maxwell block, C0=i[s(k)]_cross is
Hermitian and G0=c[[0,C0],[-C0,0]] is skew-Hermitian. At s(k)!=0 it has
eigenvalues +/-i c|s(k)| twice each and two longitudinal zeros. Its eight
corners are zeros; degeneracies increase at c=0 or s(k)=0. The actual
constant exchange floor acts exactly on a Fourier feature by
-4 kappa sum_i sin^2(k_i/2), or N times this on the Euler clock. Thus its
nonzero corner multipliers are -4 kappa times the number of pi coordinates.
This algebra does not establish a closed actual-generator eigenmode or an
all-time damping bound in the presence of context terms.

With v_i=e^(ik_i)-1, C+=[v]_cross and C-=C+^*=-[conj(v)]_cross.
The adjoint signs follow because (d+)*=-d- and the cross matrix is skew
under transposition. Direct multiplication gives

    C+* C+ = |v|^2 I - v v*,
    C+ C+* = |v|^2 I - conj(v) v^T.

Hence G=c[[0,C-],[-C+,0]] is skew-Hermitian, conserving the real quadratic
energy. The two divergence constraints use d- dot E and d+ dot B. At
v!=0, c!=0 the four transverse eigenvalues are +/-i c|v| twice each, with
two longitudinal zeros. Here |v|^2=4 sum_i sin^2(k_i/2), so its only
Brillouin-zone frequency zero is k=0. The complex longitudinal null vectors
are v for E and conj(v) for B; confusing these conjugations would be a real
error. A fully symbolic complex-vector Gram check and an exact nontrivial
six-by-six characteristic polynomial lambda^2(lambda^2+8)^2 independently
verify signs and factors. An arbitrary-array N=4 torus check verifies all
eight staggering identities. No microscopic realization, spatial cubic
assignment, physical photon multiplicity or unique physical field follows.

## Statistical obligations still open before source comparison

Closed-state correctness does not certify equilibrium of a finite run.
Need inspect: no skipped closed self visits; no forced closure; exact capacity
and divergence; warmup/measurement clocks; reported endpoint/flux histories;
predeclared mode phases and normalization; empty/full starts kept separate;
all planned cases retained; and file/source/seed metadata.

Sixteen blocks is a reporting threshold, not an effective-sample-size or
mixing theorem. A fixed-block bootstrap can severely understate uncertainty
when dependence exceeds a block. Ratios must use paired numerator/denominator
blocks and must disclose near-zero denominators. Longer-block sensitivity,
first/last comparisons and flux changes are diagnostics, not certification.
Flat ratios at finite sizes cannot establish an infrared asymptotic, phase,
critical exponent, quantum vacuum or formation-selected law. The fugacity-one
follow-up is expressly adaptive, not an independent preregistered replication.
No production output has yet been inspected.
