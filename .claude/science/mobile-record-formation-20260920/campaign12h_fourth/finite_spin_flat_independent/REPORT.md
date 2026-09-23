# Independent reconstruction of the prepared flat-sector joint-spin limit

2026-09-23. A conditional ordinary-time limit can be proved for normalizable
states deliberately prepared in the physical rotor eigenspace of H2 at -4.
The limit has a quadratic electric operator, a nonzero fourth-order hopping
operator, and total formation rate 4 kappa. A next formation fills all eight
sites, after which this model's target dynamics is frozen. The finite-spin
Hamiltonian does **not** preserve the rotor flat subspace: its leading electric
correction leaks out. The proof below controls that leakage at the actual
dispersive crossings rather than postulating a gap or exact invariance.

This is a pre-candidate-source reconstruction for a selective independent
check. It is not a formal audit or a claim to have reviewed the still-unopened
candidate. The parent author was deriving that candidate personally. The only
science sources read were the permitted fast-target note/review and checked
ring-spectrum packet identified in SOURCE_IDENTITIES.json. No candidate
finite-spin author source, second-event author source, fourth-campaign
checkpoint, registry or new result summary was opened before this report.
Concise structural/proof-route progress was sent to the parent while working;
that exposure must remain disclosed when comparing the two packets.

## 1. Exact model and theorem domain

Use the oriented eight-site ring, A={0,2,4,6}, q_i in {0,+1,-1}, total charge
four, and six records. There are five plus records, one minus and two vacancies.
P requires all A occupied. Thus two B sites are occupied and two are vacant.
The Gauss condition is E_e-E_(e-1)+1_A(e)-q_e=0, with integer f=E7. A physical
basis word q and f determine all E_e=f+g_e(q), where

    g_e(q)=sum_(i=0)^e [q_i-1_A(i)],       g_7(q)=0.

The rotor P Hilbert space is H6=ell^2(Z) tensor C^36. A charge c hopping
forward on link e shifts E_e by -c, with hopping amplitude minus the link
shift amplitude. A resolved birth channel (e,c) creates c at e and -c at
e+1 on an empty edge and raises E_e by c. Its amplitude is positive. The
coherent edge channel is the positive, unnormalized sum over c=+1,-1.
These are the supplied instruments, not adjustable normalizations.

For integer S let C=S(S+1). Embed the complete finite-spin physical space
using all basis words with |f+g_e(q)|<=S for every e. The shift amplitude is
sqrt[1-E(E+k)/C] for k=+/-1 and is zero at a prohibited boundary. Define

    A_S=Pi1 T_S P,     Z_S=Pi2 T_S Pi1 T_S P,
    H2_S=-A_S^dagger A_S,
    H4_S=(A_S^dagger A_S)^2-Z_S^dagger Z_S/2,
    B_(j,S)=-P j_S Pi1 T_S P,
    R_S=sum_j B_(j,S)^dagger B_(j,S).

The target Hamiltonian is K C H2_S+delta H4_S, with K,delta,kappa>0 fixed and
epsilon^2=delta/(K C). Formation jumps are sqrt(kappa) B_(j,S).

Let F be the *physical* spectral projection 1_{-4}(H2_rotor), not the full
kernel in an exceptional angle fiber. Suppose finite-spin initial densities
rho_S are P-supported, in the six-record sector, and their embeddings converge
in trace norm to rho=F rho F. No moment bound is required on rho or rho_S for
the qualitative theorem. Then, uniformly on every fixed finite time interval,
their target densities converge in trace norm to the dynamics in Section 6.
The same holds for the no-next-formation density and the integrated next-event
time/mark distributions. The theorem is not uniform over unrelated S-dependent
states whose mass escapes to the spin cutoff.

At vector level the no-event convergence removes the scalar fast phase:
multiply the finite-spin six-record no-event vector by exp(-i 4 K C t).
At density level that common phase already cancels. The result assumes an
initial six-record density; it asserts no unrenormalized convergence of
coherences with a different record-number sector.

## 2. Compact physical flat frame and the crossings

Denote a physical state by |C_B,r,f>, where C_B is the occupied pair of B
positions in {0,1,2,3}, and r in {0,...,5} is the position of the minus in
the occupied charge word read from physical vertex zero. Put
c(r)=-1 for r=0 and +1 otherwise. Define the isometry J from
HF=ell^2(Z) tensor C^12 by

    J|0,r,f> = [|{0,1},r,f>-|{2,3},r-1 mod 6,f+c(r)>]/sqrt(2),
    J|1,r,f> = [|{0,3},r,f>-|{1,2},r,f>]/sqrt(2).             (1)

Every physical adjacent occupied-B configuration appears in exactly one such
pair, with its appropriate flux translation. Hence J^dagger J=I. Directly
enumerating all legal two-hop returns through W=1 gives

    (H2_rotor+4)J=0.                                      (2)

This can also be seen by cancellation of the two opposite-B-pair outputs of
each antisymmetric pair. The direct independent enumeration checks (2) for
all twelve internal labels; translation gives it for all integer f.

In angle representation with hat psi(theta)=sum_f psi_f exp(i f theta), J is
a matrix whose entries are constants or exp(+/-i theta)/sqrt(2). It is smooth,
periodic and bounded with every derivative. The checked spectrum has twelve
flat modes generically. All additional zero eigenvectors of
G(theta)=H2(theta)+4 occur only at theta in (pi/2) Z, a set of circle measure
zero. Therefore

    F=J J^dagger                                           (3)

as a physical Hilbert-space projection. It has finite circulation range and
preserves every electric-moment core. No singular choice of individual band
eigenvectors is needed to define it across a crossing.

Write Q=I-F. Away from that crossing set, G restricted to Q is invertible.
The dispersive eigenvalues are -2 sqrt(2) cos(theta/6+pi l/12), l=0,...,23.
Consequently, if d(theta) is distance to (pi/2) Z on the circle,

    ||G_Q(theta)^-1||
       =1/[2 sqrt(2) sin(d(theta)/6)].                     (4)

This diverges linearly in 1/d; there is no uniform gap. At a crossing the
36-by-36 G has rank 22, elsewhere rank 24, while the smooth physical F always
has rank 12. The isolated extra fiber vectors carry no normalizable point
mass. The independent compact-frame and inverse controls explicitly include
the crossings and distances 10^-4 from them.

## 3. The finite-spin electric correction and its genuine leakage

Consider a legal two-hop P->Pi1->P path. At its two hops write the original
link fields as f+g and f+h, including the first hop's circulation change in h,
and their shifts as k,l in {+1,-1}. Define

    a(f)=(f+g)(f+g+k),    b(f)=(f+h)(f+h+l).

The path's H2 coefficient is

    -sqrt[(1-a/C)(1-b/C)]
       =-1+(a+b)/(2 C)+O((1+|f|)^4/C^2).                 (5)

The expansion also covers a return on the same link, where a=b and the
coefficient is exactly -1+a/C. Let D be the finite-range operator obtained
by replacing each rotor two-hop coefficient -1 with (a+b)/2. This is an
explicit polynomial electric operator on the finite-support core, with
coefficients of degree at most two in f.

The compressed operator is diagonal in the frame (1):

    D_F=J^dagger D J,
    D_F|a,r,f>=(4 f^2+beta_(a,r) f+gamma_(a,r))|a,r,f>.    (6)

| r | (beta,gamma), a=0 | (beta,gamma), a=1 |
|---|---|---|
| 0 | (-5,2) | (-8,4) |
| 1 | (-3,1) | (-5,2) |
| 2 | (0,0) | (-3,1) |
| 3 | (3,1) | (0,0) |
| 4 | (5,2) | (3,1) |
| 5 | (8,4) | (5,2) |

The table is obtained by evaluating the four return weights of each of the
two configurations in (1), taking their average, and canceling the other
flat-pair overlaps. The independent exact polynomial dictionary checks all
twelve identities for symbolic f. It is not a numerical fit at finitely
many field values.

Crucially,

    Q D J != 0,
    ||Q D J|0,0,0>||^2=5.                               (7)

The complete nonzero leakage polynomials are retained in FLAT_PROBE_RESULTS.
They are generically linear in f. Thus exact finite-S flat invariance is false
and a proof using only strong convergence H2_S->H2 would miss an order-one
electric leakage source after multiplication by C. Equation (7) is preserved
as a counterexample to that shortcut. It is compatible with dynamical leakage
vanishing over finite ordinary times because the dispersive evolution is fast.

For later bounds let F0 denote multiplication by f on H6; this is distinct
from the projection F. Extend each finite-spin operator by zero outside its
physical spin box. On the common Schwartz electric core one has constants
independent of S such that

    ||{C(H2_S-H2_rotor)-D}xi|| <= A/C ||<F0>^4 xi||,
    ||(H4_S-H4_rotor)xi|| <= A/C ||<F0>^2 xi||,
    ||(R_S-R_rotor)xi|| <= A/C ||<F0>^2 xi||.             (8)

Here and below constants may depend on this fixed graph and the supplied
parameters. To verify (8), for 0<=x<=1 use the exact identity

    sqrt(1-x)=1-x/2-x^2/[2(1+sqrt(1-x))^2].

On a valid path a/C,b/C lie in [0,1], and this bounds (5)'s remainder even
at a spin boundary. A forbidden whole-state or intermediate cutoff can
affect a path only if |f|>=S-M for a fixed finite offset M. There C and f^2
are bounded by a constant times <f>^4/C, so the same first bound follows
without expanding an invalid square root. Products of the at most four
bounded shifts in H4 or R have error O(<f>^2/C). There are finitely many
paths and all flux changes are bounded. The standard weighted-norm bound
for a finite-range matrix then gives (8). This explicitly handles the
unbounded field tails and the moving physical spin boxes.

## 4. Fourth-order and formation operators on the flat frame

Define H_F4=J^dagger H4_rotor J. Exhausting the four-hop paths in
(A^dagger A)^2 and the grade sequence 0,1,2,1,0 in Z^dagger Z gives

    H_F4 |0,r,f>
      =12|0,r,f>-2|1,r,f>+2|1,r-1,f+c(r)>,
    H_F4 |1,r,f>
      =12|1,r,f>-2|0,r,f>+2|0,r+1,f-c(r+1)>,             (9)

with charge-word indices reduced modulo six. Moreover

    Q H4_rotor J=0.                                     (10)

The two off-diagonal actions in (9) are adjoints of one another. They are
bounded shifts on the infinite flux space, not coefficients discarded after
a first formation. The scalar 12 delta can be removed as a further common
phase if desired, but is retained here for unambiguous comparison.

For either supplied instrument, the exact loss identity is

    R_rotor J=4J.                                       (11)

The exact check forms each B_j by one legal hop into Pi1 followed by a
birth on an empty edge, and forms B_j^dagger B_j without replacing the
coherent channel by a classical mixture. It checks all twelve frame vectors.
Translation covariance proves all integer f. Equations (9)--(11) are exact
finite combinatorial identities; the full dictionaries are evidence, while
the independent finite-S sparse-matrix controls are floating corroboration.

For completeness the limiting jump is C_j=B_(j,rotor) J from HF to H8.
Its complete action is specified without an implicit projection by

    C_(e,c)|a,r,f>
      =-j_(e,c) Pi1 T_rotor J|a,r,f>,
    C_e=C_(e,+1)+C_(e,-1)    for a coherent edge mark.     (12)

Equation (1), the legal charge hop, and the empty-edge birth rule in Section 1
determine every nonzero term of (12), including flux changes and relative
signs. The retained independent builder implements precisely those rules.
Equation (11) is equivalently sum_j C_j^dagger C_j=4 I. The individual marks
can depend on the electric/internal state and on the instrument, despite
their common total rate. The flat sector is not formation-dark.

## 5. A controlled gapless limit, including the unbounded domain

On HF put

    h_F=K D_F+delta H_F4.                                (13)

D_F is real diagonal, with 4 f^2 leading coefficient. It is self-adjoint
on D(f^2), and finite-support sequences form a core. Adding bounded H_F4
leaves that domain and self-adjointness unchanged. Every weighted space
D(<f>^m) is invariant under exp(-it h_F), with a uniform bound on compact
time intervals: the diagonal part commutes with <f>^m, and each shift in
(9) changes f by at most one, so its conjugation by the weight is bounded.
The interaction-picture Dyson bound proves this assertion for every m.
In particular an initial finite-support frame vector evolves in the common
Schwartz core, with its time derivative in that core. The same is true after J.

It remains to control the leakage in (7); compressing the generator alone
is insufficient. Define the full rotor-core no-event operator

    L=K D+delta H4_rotor-i kappa R_rotor/2.

For a finite-support frame vector xi let

    psi(t)=J exp(-2 kappa t) exp(-it h_F) xi.

Then i psi'=F L psi, and its discarded source is

    g(t)=Q L psi(t)=K Q D psi(t).                         (14)

All angle derivatives of g and g' are bounded uniformly on a fixed compact
time interval, by the just-established weighted-core bounds.

Choose a smooth periodic cutoff chi_nu that vanishes within distance nu of
the four crossings and is one beyond distance 2nu. Its derivatives of order m
are O(nu^-m). Away from the crossings define

    R_nu(theta)=chi_nu(theta)[G(theta)+F(theta)]^-1 Q(theta),

and extend it by zero through the excluded neighborhoods. It is smooth and
periodic. Equation (4), bounded derivatives of G and F, and repeated inverse
differentiation give, for each fixed m,

    ||partial_theta^m R_nu||_infinity <= A_m nu^(-m-1),
    G R_nu=chi_nu Q.                                    (15)

This inverse is used only after the physical flat projection is removed.
Define a small corrector and trial vector by

    zeta_S(t)=-(K C)^-1 R_nu g(t),
    v_S(t)=psi(t)+zeta_S(t).                             (16)

For the exact finite-spin no-event evolution on H6 use the zero-extended
Hamiltonians/losses and add the scalar 4 K C I:

    M_S=K C(H2_S+4I)+delta H4_S-i kappa R_S/2.

Its propagator exp(-it M_S) is a contraction, and the physical spin box is
reducing. Outside that box the extension is only a harmless scalar phase;
for sufficiently large S a finite-support physical initial vector lies inside
the box exactly. Equations (8) imply

    M_S=K C G+L+E_S,
    ||E_S z|| <= A/C ||<F0>^4 z||                        (17)

on the common core. The residual of (16) is exactly

    (i partial_t-M_S)v_S
      =-(1-chi_nu)g+(i partial_t-L)zeta_S-E_S v_S.        (18)

The first term has norm O(nu^1/2): g is bounded pointwise and the excluded
set has measure O(nu). This is the step that accounts for the crossings;
they are not deleted from the evolving state. The other terms obey

    ||zeta_S||+||partial_t zeta_S|| <= A C^-1 nu^-1,
    ||L zeta_S|| <= A C^-1 nu^-3,
    ||E_S v_S|| <= A(C^-1+C^-2 nu^-5).                   (19)

For (19), D is a matrix differential operator of order at most two in angle,
with smooth bounded coefficients; <F0>^4 requires at most four derivatives.
Equations (15) and the smooth-core bounds therefore suffice. No global
self-adjoint realization of the off-flat polynomial D is being assumed:
it is used here only on this explicit core, while M_S generates the exact
contractive evolution and h_F is already self-adjoint.

Choose nu=C^-1/8. The right sides of (18)--(19), and the initial/final
corrector defects, tend to zero. A nonoptimal uniform compact-time core bound
is O(C^-1/16). Duhamel against the exact contraction exp(-it M_S) proves

    exp(-it M_S) J xi -> J exp(-2 kappa t)exp(-it h_F)xi  (20)

uniformly on bounded time intervals for every finite-support xi. This proves
decoupling even though (7) rules out exact finite-spin invariance and (4)
rules out a uniform gap. It does not interchange a fixed-spin secular average
with the large-spin limit.

Density of finite-support frame vectors and contractivity extend (20) to
every normalizable frame vector. Finite-rank approximation and contraction
extend the density statement to every trace-class flat density and to every
convergent embedded initial sequence specified in Section 1. This final
extension requires no finite electric moment, but does not inherit a uniform
rate over all such states. The smooth-core rate is merely a proof bound,
not an empirically fitted or optimal exponent.

## 6. Limiting electric, fourth-order and formation dynamics

Write rho=J varrho J^dagger with tr varrho=1. The no-next-event density is

    sigma_6(t)=exp(-4 kappa t)
      J exp(-it h_F) varrho exp(it h_F) J^dagger.         (21)

The mark-j probability by time T is

    p_j(T)=kappa integral_0^T exp(-4 kappa t)
       tr[C_j exp(-it h_F) varrho exp(it h_F) C_j^dagger] dt. (22)

The total survival is exp(-4 kappa t), so the next waiting time for this
prepared-sector limit is exponential with rate 4 kappa. The conditional
six-record state retains the nontrivial Hamiltonian (13), including its
quadratic electric table and the flux/internal shifts (9).

After a next formation all eight sites are occupied, with six plus and two
minus records. Every legal hop and birth is blocked. Therefore H2,H4 and
all subsequent B vanish on H8, at finite S as well as for rotors. The full
limiting density is the sum of (21) and

    sigma_8(T)=kappa sum_j integral_0^T exp(-4 kappa t)
       C_j exp(-it h_F) varrho exp(it h_F) C_j^dagger dt.  (23)

No eight-record evolution needs to be inserted after the integrand. Strong
convergence of the bounded B_(j,S) and their adjoints, (20), finite-rank trace
approximation and dominated integration justify (22)--(23) in trace norm.
The same argument allows a finite event/mark register. This gives the actual
prepared-sector dissipative limit, not just a no-jump formal generator.

## 7. Microscopic transfer and the first-mark boundary

The authenticated parent theorem supplies an O(epsilon) fixed-graph target
approximation uniformly in S and over initial P densities, including finite
mark registers. With epsilon^2=delta/(K C), that error tends to zero. Thus
the deterministic prepared-six-record initial-state version of (21)--(23)
also transfers to the parent microscopic model and its integrated next-event
probabilities. This uses the full-W fixed-graph theorem; it does not apply
the separate cubic pre-first-birth field corollary to this eight-site ring.
No microscopic trajectory simulation was run in this packet.

This theorem does not say that a first formation prepares F. The checked ring
spectrum gives flat probability exactly 1/2 for both prescribed first-mark
outputs for every normalizable pre-event field density. The remaining half
and possible flat/dispersive coherences are present in the actual output.
Projecting onto F and renormalizing is an additional specified preparation or
selection, not an automatic consequence of the mark. No statement here
controls the whole unselected output under the joint ordinary-time scaling.

Likewise, the parent deterministic-initial-density estimate alone does not
give a uniform normalized conditional restart at a microscopic random first
event followed by a flat-selection instrument. Such a stopping/selection
transfer is separate. The prepared initial-state theorem just established
must not be reported as that stronger claim. No volume limit, native selection
of the quantum laws, energy reservoir, three-dimensional photon phase,
empirical match or TOE closure follows.

## 8. Independent evidence, repairs and source identities

The independent physical builder starts from all 168 six-record charge words,
infers their Gauss fields, and retains all 36 P words. Its finite-spin matrices
assemble A, Z and birth matrices on complete physical spin boxes. It imports
no author runner, prior independent builder or candidate code. The symbolic
path calculation and the finite sparse A^dagger A/Z^dagger Z assembly use
different operator-construction routes, with a common locally checked hop rule.
This is disclosed; it is not two wholly independent software implementations.

The exact controls include all twelve frame identities, their full symbolic
electric polynomials, H4 invariance and coefficients, both loss identities,
the nonzero leakage counterexample (7), and 576 Gauss-preserving hop checks.
The crossing control compares the compact projection with the separate wedge
mode construction and tests (4), including points 10^-4 from a crossing.
The largest compact-versus-wedge projection error on the declared grid is
below 6.6e-15. Those inverse/projector numbers are floating checks; the
derivation and exact finite identities are the mathematical argument.

For K=0.7,delta=1.1,kappa=0.4 a three-mode compact initial superposition was
propagated with the complete finite-spin no-event operators for S=4,8,16,32
at t=0,0.05,0.15,0.4. At t=0.4 the respective state-norm errors are about
0.6033,0.2367,0.1067,0.06634. The S=32 survival is 0.52887956 against the
limiting 0.52729242; its physical flat leakage norm is about 0.06471. Thus
these finite spins are not presented as already negligible-error regimes.
The limiting flux cutoffs 12 and 20 differ by at most 5.17e-14 in state norm
on this grid. This is floating convergence evidence for one preparation,
not an interval certificate or a proof for generic initial states.

For a compact frame mode, C times the error in the scaled H2 correction
tends toward 0.5 over that spin grid, consistent with (8); H4 and loss errors
also decrease. Dynamic propagation was checked for the resolved instrument.
Both rotor instruments were checked exactly, and a finite-S coherent loss
control was also run. No coherent full dynamic grid or microscopic grid
was run; neither is used to prove the analytic instrument-independent limit.

One numerical diagnostic issue was found after the initial successful run:
subtracting two almost equal squared norms created spurious 10^-8 time-zero
density/leakage diagnostics despite exactly equal input vectors. The original
source, complete result and actual run streams/receipt remain preserved as
decisive_controls_pre_stable.py, DECISIVE_RESULTS_pre_stable.json and
decisive.*. The final runner computes the orthogonal vector residual directly
and uses the equivalent stable rank-two distance formula. Its time-zero
diagnostics are below 2.4e-16. No physics parameter, target, scientific
coefficient or acceptance tolerance was changed by this repair.

The original combined source display was too large and was truncated. Before
derivation, the complete permitted fast review and both ring reports were
reread in bounded individual displays, so no load-bearing source disposition
rests on the truncated view. Only the explicitly permitted source files were
authenticated; transitive files outside that boundary were not silently opened.
Their previous source-bound reviews are reused at the identified seals.

All actual executable commands have stdout, stderr and timing/source-hash
receipts. SOURCE_IDENTITIES.json records the exact assigned source hashes,
instruction identities and origin/main revision. No Git mutation, audit,
publication, external message or onward delegation was performed. Only this
assigned independent directory was written. PRE_COMPARISON_SEAL.json freezes
this reconstruction and its evidence before candidate-author source access.
