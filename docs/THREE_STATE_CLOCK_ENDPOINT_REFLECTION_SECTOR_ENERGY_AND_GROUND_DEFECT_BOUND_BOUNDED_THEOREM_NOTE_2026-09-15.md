---
claim_id: three_state_clock_endpoint_reflection_sector_energy_and_ground_defect_bound_bounded_theorem_note_2026-09-15
claim_type: bounded_theorem
claim_scope: "For the specified three-state clock Hamiltonian on three-dimensional periodic cubic tori of dyadic side at least four, endpoint-qutrit reflection gives a volume-independent lower bound for every integer-charge sector relative to the neutral ground energy; it implies explicit quadratic ground-state defect-density suppression and convergence of the ground-energy density as the charge penalty grows."
upstream_dependencies: []
runner: scripts/clock_endpoint_reflection_sector_bound_2026_09_15.py
---

# Endpoint reflection, charge-sector energies and ground-state defects in a three-state clock model

**Date:** 2026-09-15
**Type:** bounded_theorem
**Status:** proposed_retained

For the specified three-state clock Hamiltonian on three-dimensional periodic cubic tori of dyadic side at least four, endpoint-qutrit reflection gives a volume-independent lower bound for every integer-charge sector relative to the neutral ground energy; it implies explicit quadratic ground-state defect-density suppression and convergence of the ground-energy density as the charge penalty grows.

This is an author theorem proposal. Independent mathematical review and
formal audit are pending. The microscopic Hamiltonian, couplings and
choice of a ground state are supplied model assumptions.

## Status, exact target and imports

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "A volume-independent sector-energy inequality A_cons >= e_neutral I-c N is needed to turn the conditional quadratic ground-state defect-density estimate into an estimate for the actual supplied clock Hamiltonian."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Independently examine the endpoint-reflection proof, then address neutral-phase stiffness and photon-like spectral behavior as separate physics targets."
conditional_surface_status: "The explicitly supplied Hamiltonian, couplings, topology and dyadic sizes in the theorem."
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "A positive analytic inequality with explicit uniform constants for a specified finite-range Hamiltonian and selected ground-state limits."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The exact target is the quoted uniform sector-energy inequality and its
stated density consequences. Its prior conditional use is documented at
campaign revision `18ff8d43faa1c4078b7af27bdb93038f2a9c4de1` in
`BLOCK1_SECTOR_PROOF_SEARCH.md`. This is provenance; all necessary model
identifications and proofs are given below. The earlier local-probability
note at `9a84632e8b9e4f82969d7b4e22827d0037c51df5` proves a positive
LOWER bound for charged local patterns at finite couplings. The present
UPPER bound is compatible with it and has a distinct purpose.

| Input or obligation | Provenance and status in this proposal |
|---|---|
| Three-state original links, principal charge, hopping and penalty | Supplied model choices, defined in(1) |
| Periodic dyadic cubic tori and orientations | Explicit mathematical domain and convention |
| Ground-state selection | Supplied state question; not a formation law |
| Charge-conserving ring and physical flux quotient | Derived in section1, including all three mod-three winding restrictions |
| Endpoint qutrits and unit shifts | Exact auxiliary isometry, section2; no new physical site domain |
| Reflection positivity with the hard physical projection | Finite matrix cone and Trotter proof, sections3-4 |
| Charge-pattern comparison | Explicit finite maximization and dyadic dissemination, section5 |
| Plaquette norm and checkerboard bounds | Chain decomposition and local divergence bound, section6 |
| Actual ground-state estimates and density limits | Variational and finite-range arguments, section7 |

No observed number, field-theory phase theorem or new framework premise is
used. The framework baseline remains `docs/MINIMAL_AXIOMS_2026-06-29.md`
and its approved primitive registry at current main
`5deabeb698a27c2c3f68c5df685af2521ef15307`. The model's native realization
is additional scientific work. Standard tensor algebra, cohomology over a
finite field, Perron-Frobenius, Trotter products and variational arguments
are used with their relevant hypotheses stated in the proof.

## Supplied Hamiltonian and quantified domain

Use a three-dimensional cubic torus of side L=2^m>=4. Let V=L³ be its number
of cubes, and E=3V its number of original links. Original link coordinates
a_l lie in Z3, principal plaquette integers b=principal(Fa) lie in{-1,0,1},
Q=Db/3 is the integer cube charge, and N=sum_c Q_c². For t>0, K>=0,
0<=mu<infinity and lambda>=0, the supplied Hamiltonian is

 H=A_mu+lambda N,
 A_mu=2tE I+alpha sum_p b_p²-t sum_(l,sigma) W_(l,sigma),
 alpha=3K/2,
 W_(l,sigma)|a>=exp[-mu||m_(l,sigma)(a)||²]|a+sigma e_l>,
 m=[b(a+sigma e_l)-b(a)-sigma F e_l]/3.                 (1)

## 1. Exact charge-conserving operator and the physical flux space

Pinch by the ENTIRE integer charge vector:

 A_cons=sum_q P_q A_mu P_q.

This is different from retaining only the grade-zero part for total N.
Around an original link, the four face-wrap indicators form a connected
cyclic fan. Equality Q'=Q means adjacent indicators agree. Thus either no
face wraps or all four wrap. A full wrap is exactly two unwrapped reverse
moves, with weight h=exp(-4mu). This argument holds in every integer charge
sector, not only the neutral one.

Dualize the principal face field to a spin-one field E_e on dual links,
with the orientation chosen so div E=3Q. Let T_e raise E_e by one inside
{-1,0,1}, annihilating a move past an endpoint. For a dual plaquette p let
B_p be the ordered product of T_e or T_e* around its oriented boundary.
Then, after removing the scalar2tE,

 H_cons=alpha sum_e E_e²
       -t sum_p [B_p+B_p*+h(B_p²+(B_p*)²)].             (2)

There are3V dual plaquettes. Its physical field basis consists of E with
div E=0 mod3 and zero mod-three winding flux in all three directions.
The latter constraints are essential: original periodic link coordinates
produce exact mod-three plaquette fields, not every closed field.

On this torus these constraints are sufficient by the cubical cohomology
of a torus over Z3: the three surface fluxes are its degree-two classes.
This fact has a direct finite-complex proof. For one periodic interval,
the kernel of its vertex-to-edge difference is the constants, and its
image consists exactly of edge words whose sum is zero. Thus its degree-zero
and degree-one cohomologies are each one-dimensional. Split off these two
one-dimensional spaces and the exact pairs, then tensor the three interval
complexes over the field Z3. Every summand containing an exact pair is
contractible. The degree-two remainder has three generators, paired
nondegenerately with the three coordinate two-tori. Vanishing of those
three periods is therefore precisely exactness, after local closure.
Every allowed b has the same number of original-link preimages, namely
|ker(F mod3)|. The invariant subspace for translations a->a+k with
k in ker(F mod3) has the orthonormal uniform-fiber basis labelled by b.
Each W induces its stated single flux transition in that basis, with no
extra multiplicity factor. This identifies (2) exactly there.

For the MINIMUM energy in each q sector this invariant subspace suffices.
A real matrix with nonpositive off-diagonal entries has a nonnegative
ground vector (take componentwise absolute values in its Rayleigh quotient).
Averaging this vector over ker(F mod3) is nonzero, remains in the same q
sector, and remains a ground vector because the group commutes with A_cons.
Hence the sector minimum in the full original-link Hilbert space equals
the minimum in the physical flux representation. No claim that every
original-link state is represented by a single b is needed.
The finite-temperature trace below is an auxiliary trace on this exact
invariant flux subspace. Equality with the full original-link thermal
partition function is not assumed; equality of sector minima is sufficient.

## 2. Exact endpoint qutrits and local charge registers

For every unoriented dual link {v,w}, put one auxiliary qutrit at each
endpoint, with occupancies n_(v,w),n_(w,v) in{0,1,2}. Impose

 n_(v,w)+n_(w,v)=2.                                   (3)

For a positively oriented link v->w, identify E_e=n_(v,w)-1 and
n_(w,v)=1-E_e. This is an isometry from the physical three-state link
onto the three-dimensional subspace (3). Let R+ be the UNIT shift
R+=|1><0|+|2><1|, so R+|2> is the zero vector, and R-=(R+)*. Then

 T_(v->w)=R+_(v,w) R-_(w,v)                           (4)

on (3), with both nonzero matrix elements exactly one. These are truncated
unit shifts, not canonical bosonic creation operators with square-root
occupation factors. Confusing those factors would change (1).

At a dual vertex v, the local charge is

 Q_v=[sum_(w adjacent v)(n_(v,w)-1)]/3.                (5)

Work first in the tensor product over vertices of the local subspace
sum_w n_(v,w)=0 mod3. It has dimension243 at each degree-six vertex;
Q_v then has values-2,-1,0,1,2. Impose (3) and the three winding constraints
with a commuting diagonal projection P_phys. These auxiliary variables
are a mathematical factorization, not new physical site possibilities.

For a directed plaquette cycle v0->v1->v2->v3->v0, the ring operator is

 B_p=product_(v in cycle) K_v,
 K_v=R+_(v,next(v)) R-_(v,previous(v)).                 (6)

Each corner preserves the occupancy sum at its vertex. The entire ring
preserves (3), every Q_v and every winding flux. The electric term is
(alpha/2)sum_(v,w)(n_(v,w)-1)² on the link-constraint subspace.
The endpoint Hamiltonian therefore commutes with P_phys and restricts
exactly to (2). All operators used in this proof are finite matrices.

## 3. A spatial reflection with no shared quantum sites

Reflect across a plane BETWEEN dual vertices, with two periodic cuts;
write r for this bond reflection and L,R for the two vertex halves.
Compose r with particle-hole conjugation n->2-n on every endpoint qutrit
and complex conjugation in the occupancy basis. The resulting anti-linear
operator-algebra map theta sends

 theta(n_(v,w)-1)=-(n_(rv,rw)-1),
 theta(R+_(v,w))=R-_(rv,rw),
 theta(Q_v)=-Q_(rv).                                  (7)

There are no shared qutrit sites at the cut: the two halves of a crossing
physical link lie in different tensor factors. The link constraint will
be treated by P_phys, not silently removed.

A plaquette crossing a cut has two vertices in each half. Reflection
reverses its cyclic orientation, and particle-hole conjugation reverses
its corner shifts. The two reversals cancel. With C_p the product of the
two left corner operators,

 B_p=C_p theta(C_p),
 B_p*=C_p* theta(C_p*),
 B_p²=C_p² theta(C_p²).                               (8)

The same identity holds for the adjoint square. Every ring wholly on one
side is paired with its reflection. The endpoint Hamiltonian has the form

 H_ext=H_L+theta(H_L)-sum_a c_a C_a theta(C_a), c_a>=0, (9)

where crossing coefficients are t and th. A local term lambda Q_v² could
also be included without changing this form, though the sector comparison
below is applied before adding that penalty.

The positive reflection cone consists of finite sums sum_j d_j A_j theta(A_j),
d_j>=0, and its finite-dimensional closure. It is closed under multiplication
and addition: operators on opposite sides commute, and theta preserves
product order. Its trace is nonnegative, since
Tr[A theta(A)]=|Tr_L A|². Lie-Trotter and the exponential series show that
exp(-s H_ext) belongs to the cone for s>=0. This is the elementary finite
matrix reflection-positivity proof; no spin-isotropy theorem is imported.

## 4. The original clock's hard projection is also in the cone

This is the load-bearing physical-space check. Choose the reflection normal
to direction0; the other directions follow by symmetry.

Internal link constraints occur in left/right pairs. At a crossing link,

 1_{n_L+n_R=2}=sum_(r=0)^2 1_{n_L=r} theta(1_{n_L=r}). (10)

The local mod-three vertex condition is already in the product Hilbert
space and is preserved by theta. Consider a winding surface normal to
direction0 at one of the two cuts. Its flux modulo3 is the sum of the
signed n_L-1 on that cut, using only left endpoint variables. In the
presence of (10), the corresponding reflected condition agrees. Thus its
zero-flux projector may be represented by F_L theta(F_L), a cone element.
Modulo-three Gauss at all vertices then makes the other parallel cut flux
the same modulo3.

For a tangential winding direction j=1,2, choose its standard transverse
surface. Its links do not cross the reflection cuts. Write A_L,j for the
left portion of its flux, expressed with the left endpoint occupancies.
Reflection with particle-hole conjugation sends it to minus the right
portion. Therefore zero total flux modulo3 has the exact decomposition

 1_{Phi_j=0 mod3}
 =sum_(r in Z3) 1_{A_L,j=r mod3}
                     theta(1_{A_L,j=r mod3})          (11)

on the hard link-constraint subspace. All projectors here are diagonal and
commute. Multiplying (10), (11), the paired internal constraints and the
normal-flux condition gives a finite sum of A theta(A) equal to P_phys.
One may combine the commuting diagonal factors into a single projector A
for each cross-link occupancy tuple and pair of tangential flux classes.
This avoids any claim that an arbitrary global sector projection is
reflection positive.

Since P_phys commutes with H_ext, the physical finite-temperature functional

 Z^{-1} Tr[P_phys exp(-s H_ext) F theta(F)]>=0           (12)

for any left operator F follows from cone multiplication and the trace
identity. Its Cauchy-Schwarz inequality is therefore available on the
exact zero-mod-three-winding flux subspace identified in section1.

## 5. Sector chessboard inequality, with the charge sign retained

Let Z_s(q)=Tr[P_phys exp(-s H_ext) product_v 1_{Q_v=q_v}].
All charges commute with H_ext. If a pattern has no states, set Z_s(q)=0.
Reflection Cauchy-Schwarz gives

 Z_s(q)² <= Z_s(q^L) Z_s(q^R),                         (13)

where q^L keeps the left pattern and installs minus its reflected pattern
on the right; q^R is the analogous right dissemination. The minus sign
is fixed by (7), not discarded.

Write epsilon_v=(-1)^(v0+v1+v2) and r_v=epsilon_v q_v. A bond reflection
flips this spatial parity, so it acts on r by ordinary reflection with no
sign. Let q^(k)_v=epsilon_v k, k in{-2,-1,0,1,2}, and let
Z_s^(k)=Z_s(q^(k)). The chessboard inequality to prove is

 Z_s(q) <= product_v [Z_s^(r_v)]^(1/V).                (14)

Here is a finite max argument rather than an assumed limiting theorem.
All five disseminated patterns are physically feasible. For k=0 take E=0.
For |k|=2 take occupancies zero at even vertices and two at odd vertices,
or the particle-hole image. For |k|=1 select one perfect matching in each
coordinate direction, taking the positive-direction edges whose base has
an even coordinate in that direction. Put m_e=1 on their union and zero
elsewhere. Set the occupancy at the EVEN endpoint of each link to m_e
and at its ODD endpoint to2-m_e. Link sums are two, even vertex sums are
three and odd vertex sums nine, giving Q_v=-epsilon_v; particle-hole gives
the other sign. Their winding fluxes
vanish because each transverse plane has balanced even/odd parity.

Subtract from log Z_s(q) the average sum_v log Z_s^(r_v)/V, calling the
result f(q). The subtracted term obeys exactly the same averaging under
q->(q^L,q^R), so (13) gives2f(q)<=f(q^L)+f(q^R).
There are finitely many charge patterns; ignore infeasible ones, whose
f is minus infinity. Choose a maximizer. Since each reflected value is
at most that maximum, both reflected patterns are again maximizers.
Starting with one vertex, repeatedly reflect the half containing a uniform
block of the r labels to double that block along successive coordinates.
For an interval[0,l-1] in the coordinate being doubled, reflect in the
bond plane l-1/2 and keep the half[l-L/2,l-1] modulo L. For l<=L/2 that
half contains the interval and its reflection supplies[l,2l-1]. Other
coordinates are unchanged. This gives an explicit doubling prescription.
On L=2^m this fills the torus after finitely many doublings. Every step
preserves maximality. The final constant-r pattern has f=0. Thus the
maximum is zero, proving(14). The dissemination geometry is separately checked on L=4 and L=8;
arbitrary non-dyadic sizes are not claimed.

Global particle-hole conjugation gives Z_s^(k)=Z_s^(-k). Taking
-s^-1 log and then s->infinity in finite dimension yields

 E(q) >= (n0/V)e0 + (n1/V)e1 + (n2/V)e2,               (15)

where ni counts vertices with |q_v|=i and ei is the minimum energy in
the uniform checkerboard-|q|=i sector of(2). Here e0 is the actual neutral
sector minimum, including the original clock's winding restrictions.

## 6. Bounding only the disseminated sectors is sufficient

For one plaquette, B moves along chains of length at most three in the
four-link electric cube. A length-three chain has adjacency matrix

 [0,1,h; 1,0,1; h,1,0]

for B+B*+h(B²+(B*)²). Its spectral radius is

 rho(h)=[h+sqrt(h²+8)]/2.                             (16)

The two-state chain has radius one and the singleton zero; rho(h) is
larger. Thus each plaquette term is bounded below by-t rho(h).
The neutral basis state E=0 has expectation zero in(2), so e0<=0.

Since E_e²=|E_e| for spin one,

 sum_e E_e² >=(1/2)sum_v |div E(v)|.

The |Q|=1 checkerboard sector therefore has electric energy at least
(3alpha/2)V and

 e1 >= [3alpha/2-3t rho(h)]V.                         (17)

For |Q|=2 every incident electric contribution must be saturated and have
the same sign. In endpoint variables every vertex has all six occupancies
zero or all six equal to two. Every corner K_v annihilates this state,
so e2=3alpha V>=0. Combining(15)-(17) gives the operator bound

 H_cons >= e0 I-c n1 >= e0 I-c N,
 c=max(0,3t rho(exp(-4mu))-3alpha/2).                  (18)

The scalar2tE may be restored on both sides without changing c. The
sector-minimum argument in section1 transfers this operator lower bound
to the full original-link Hilbert space. Its constants do not depend on L.
It does not require proving e1>=e0 at every K,mu.

## 7. Consequence for the actual finite-penalty ground state

Write A_mu=A_cons-V_mix. The mixed-wrap term is a sum over original links
of real symmetric operators V_l with norm at most v=2t exp(-mu). Let R_l
indicate any nonzero integer charge on the four incident cubes. Then
(I-R_l)V_l(I-R_l)=0. For p_l=<R_l> in any normalized state,

 |<V_l>|<=2v sqrt(p_l(1-p_l))+v p_l
         <=2v sqrt(p_l)+v p_l.

Every cube has twelve original links, so sum_l p_l<=12<N>. Consequently

 |<V_mix>|<=2v sqrt(12E<N>)+12v<N>.                    (19)

A neutral ground vector of A_cons is an admissible variational trial for
H with the same energy e_neutral, because P0 V_mix P0=0. Combining this
upper bound with(18)-(19), if lambda>c+12v, gives for every ground state

<N>/E <=48v²/(lambda-c-12v)².                        (20)

The zero-<N> case is included without dividing by zero. Since E=3V, the
average cube charge-square density is at most144v²/(lambda-c-12v)².
At finite mu all original single-link hopping amplitudes are positive,
so the finite configuration graph is connected. Perron-Frobenius then
gives a unique positive ground vector; translation invariance makes the
same cube bound hold at every cube. The local nonzero-charge probability
is no larger than its charge square. Clip probability bounds at one.

Any subsequential local quantum-state limit of these dyadic periodic ground
states inherits the same cube bound. It is an infinite-volume ground state
for the supplied finite-range interaction: for every local operator O,
the finite-volume inequality <O*[H,O]>>=0 passes to the limit, since its
commutator contains only finitely many terms near the support of O. This
constructs a selected class of ground-state limits; it does not assert that
every boundary condition or every infinite-volume ground state is selected.

For mu=infinity, V_mix=0 and(18) implies exact ground neutrality whenever
lambda>c. That boundary case uses the limiting Hamiltonian, not a finite-mu
claim of exact absence of defects.

The same inequality also controls the actual energy density. Set
Delta=lambda-c-12v>0 and x=<N>. Completing the square in
Delta x-2v sqrt(12E x) gives

 0<=e_neutral-E_ground(H)<=12v² E/Delta.               (21)

The error per original link is uniform in L. This differs from the earlier
fixed-box Schur bound whose denominator required lambda>e_neutral, an
extensive condition. The new statement concerns ground energy and defect
density, not all low-energy eigenvectors or imaginary-time operators.

There is also a useful reference-state fact. For any fixed J>c,
A_cons+J N has only neutral ground states by(18). Its charged-sector
threshold is at least e_neutral+2(J-c): on a torus sum_v Q_v=0, so a
nonzero charge pattern has N>=2. This threshold belongs to the exactly
charge-conserving reference operator. At finite mu the actual H contains
V_mix and has no such exact charge-sector decomposition.

Both actual and reference ground-energy densities have thermodynamic limits
along the dyadic tori. For the reference, choose one fixed J>c; its finite
ground energy equals e_neutral for every L, yet it is an ordinary bounded
finite-range Hamiltonian on the full original-link tensor product. Group
three positive-direction link registers into each original unit cell.
Cutting interactions between large cubes changes operator norm by at most
a constant times the total cut area. Tensoring minimizing states on the
separate cubes gives the matching variational bound in the other direction.
Tiling by cubes of side k and then taking the enclosing side to infinity
bounds the upper/lower density gap by O(1/k). Letting k grow proves existence;
periodic and open cuts differ by O(L²). The same argument applies directly
to actual H. The uniform per-link estimate(21) passes to these limits.
No uniqueness of an infinite-volume phase is inferred from energy-density
convergence.

## 8. Finite challenges and their resolution

The single self-contained primary runner is `scripts/clock_endpoint_reflection_sector_bound_2026_09_15.py`. It reads no
repository scientific inputs or package integrity files. It uses NumPy,
SymPy and Python's standard library. Its finite checks challenge the
analytic proof by distinct constructions:

| Proof step | Executed finite challenge |
|---|---|
| Hodge orientation and original-clock quotient | Independently built curl and divergence on an L=4 torus; mod-three ranks126,63,66 establish finite kernel/image equality with all three periods |
| Clock pinching and both ring harmonics | 288 original single-link moves plus three forced neutral full-wrap moves; all mismatch grades appear |
| Endpoint normalization and truncation | Exact one-link isometry and 1,944 four-link transition comparisons across six crossing orientations |
| Physical projection in the reflection cone | 24 actual clock fields, 72 nonzero-winding controls, 24 broken-endpoint controls and three isolated crossing-link controls, across all reflection normals |
| Reflection positivity and Cauchy-Schwarz | Nine projected nine-dimensional matrix models with complex left operators; an explicit wrong-hopping-sign matrix has a negative reflection form |
| Checkerboard feasibility and dissemination | Ten physical checkerboard fields and 16 arbitrary-label dissemination cases on L=4 and L=8, including exact label-count averaging |
| Plaquette spectral constant | Symbolic characteristic polynomial and independent full81-dimensional matrices at h=0,1/7,1/2,1 |

The full many-body partition function, all-volume cone identity and
thermodynamic limits are analytic arguments. The finite runner does not
execute these general theorems. The five resolution lines in its stdout
make that distinction explicit. In particular, its local spectral calculation
checks a plaquette norm, not a many-body excitation spectrum.

Reproduce the finite checks with:

```bash
python3 scripts/clock_endpoint_reflection_sector_bound_2026_09_15.py
```

The canonical output is
[the primary runner cache](../logs/runner-cache/clock_endpoint_reflection_sector_bound_2026_09_15.txt).
Source mutations, exact source identities and author conformance checks are
recorded in the branch-local handoff. No helper runner or unmerged theorem
input is needed to reproduce this review unit.

## 9. Scope and strongest remaining question

The stated sector and density inequalities have an explicit proof within
the specified model, dyadic periodic topology and coupling domain. No open
terminal lemma is supplied in place of the sector comparison; independent
review of the argument remains pending. Arbitrary lattice sizes, alternative
boundary conditions and other gauge sectors are outside the theorem's
quantified domain.

For the broader physics program, the next load-bearing question is whether
the actual neutral spin-one plaquette Hamiltonian has a nonzero stiffness
and an appropriate photon-like spectral limit at any of the target finite
couplings. The present estimates concern defect density and ground energy.
A stiffness theorem, a many-body gap statement, a native formation law,
matter and gravity require additional derivations. These are scope limits,
not an exclusion of other mechanisms or a proposal to change the axioms.

## Review record

The complete derivation was cold-read personally after construction. That
pass checked the local mod-three endpoint space, exact link matching,
normal and tangential winding projections, cone multiplication, charge-sign
dissemination, finite maximization, and the transfer from auxiliary sector
minima to the full original-link Hilbert space. It also re-derived the
constants in the two variational inequalities and checked the locality
needed for thermodynamic energy densities. No fatal gap was identified in
that author pass; this assessment is provisional.

Fourteen deliberate changes to the primary mathematical checks were tested:
dual-base shift, particle-hole sign, corner reflection sign, normal winding,
tangential winding, crossing-link matching, cyclic endpoint shifts, unit
shift amplitude, dissemination plane, checkerboard sign, plaquette spectral
radius, a missing cohomology period, wrap normalization and crossing hopping
sign. Each of those fourteen altered runner copies terminated with a
relevant AssertionError; the execution receipt records the actual results
against the final runner.
The finite negative reflection forms are explicit counterexample witnesses
for the specified altered matrices.

This is author work performed without subagents. Independent scientific
review, the combined current-main landing checks and formal audit are
pending. No audit verdict or main landing is written by this proposal.

## Historical evidence

The [historical packet](work_history/repo/review_feedback/pr8135-clock-endpoint-evidence/pr8135-HANDOFF.md) preserves the original proof, source and author-review records, with their original scope and execution limits. It is provenance, not a current independent review or an audit verdict.
