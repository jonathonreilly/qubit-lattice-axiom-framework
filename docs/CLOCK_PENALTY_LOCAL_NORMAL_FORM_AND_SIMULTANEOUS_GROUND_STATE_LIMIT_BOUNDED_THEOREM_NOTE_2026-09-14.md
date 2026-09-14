---
claim_id: clock_penalty_local_normal_form_and_simultaneous_ground_state_limit_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "For the explicitly supplied three-state principal-flux penalty Hamiltonian, an integer-graded local normal form gives an exponentially small charge-changing remainder and a volume-uniform lifetime for prepared dressed-neutral states at a sufficiently large penalty. Separately, every subsequential local limit of actual periodic ground states along simultaneous volume and penalty divergence is neutral and satisfies the constrained two-harmonic Hamiltonian ground-state condition. Neither statement identifies a finite-penalty Coulomb phase or a native law."
upstream_dependencies: []
runner: scripts/clock_penalty_local_normal_form_and_ground_state_limit_2026_09_14.py
---

# Clock penalty: local normal form and simultaneous ground-state limit

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

The specified clock Hamiltonian has two useful controlled limits. At a
sufficiently large spatial charge penalty, a local unitary transformation
makes the remaining charge-changing interaction exponentially small. This
gives a volume-uniform lifetime for states prepared in its dressed neutral
space. At every positive penalty, its actual periodic ground state has
charge-square density at most `6t/lambda`. Consequently, simultaneous large-
volume and large-penalty limits of those actual ground states are neutral
ground states of an explicitly identified constrained Hamiltonian.

The constrained Hamiltonian retains a second plaquette harmonic at finite
temporal mismatch penalty. Keeping it is necessary to study the intended
model. The two conclusions above do not establish a Coulomb phase at a
fixed finite penalty. These are author proofs awaiting independent review.

## Status, assumptions and proof map

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: direct_blocker_closure
target_claim_id: null
target_blocker_text: "Replace a volume-growing penalty perturbation estimate by local control, and justify the constrained Hamiltonian as a simultaneous limit of actual full ground states."
source_of_blocker_text: handoff
reachability_to_target: closes
artifact_role: theorem
next_trace_action: "Determine the phase of the selected constrained ground states and its stability at fixed finite penalty; keep native law selection separate."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit local graded-interaction estimates and a ground-state compactness argument for a supplied finite-state Hamiltonian."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

| Supplied datum | Role | Scope |
|---|---|---|
| Cubic geometry, original link qutrits and mod-three gauge action | Defines the complete model | Not derived from the native one-site possibility algebra |
| Positive hopping `t`, finite `mu>=0`, `K>=0`, `lambda>0` | Defines the Hamiltonian | No dimensionless coupling is selected |
| Large-penalty inequality (4) | Sufficient hypothesis of the normal form | Conservative, independent of volume; not needed for the ground-density bound |
| Initial support in the dressed neutral space | Hypothesis of the lifetime estimate | Not inferred for the actual ground state at finite penalty |
| `L_j->infinity`, `lambda_j->infinity`, fixed `t,mu,K` | Hypothesis of the actual-ground-state limit | No relative rate, unique limit or finite-penalty phase is asserted |
| Graded interaction algebra, matrix exponentials, positivity and local-state compactness | Mathematical machinery | Hypotheses and estimates are given below |

| Proof obligation | Disposition here | Further consumer |
|---|---|---|
| Local integer grades on the actual link registers | Section1 | Support-preserving inverse of the charge commutator |
| Interaction norm, convergent conjugation and finite normal-form iteration | Sections2-3 | Exponentially small remainder |
| Local dressed observables and charge-density lifetime | Section4 | Controlled prepared states |
| Exact finite-mu constrained hopping and its first correction | Section5 | Correct effective Hamiltonian |
| Actual-ground density, neutrality and constrained ground condition | Section6 | Simultaneous penalty/volume limit |
| Selected ground-state phase and finite-penalty stability | Open, not used above | Photon or Coulomb conclusions |
| Native carrier, law and Record realization | Open, not used above | Framework interpretation |

No unmerged theorem is imported. The supplied model and earlier fixed-box
projection are provenance from the campaign at
`652ea36706f7df14f153f2d40ee900662fe73706` and proposed PR8123 at
`9a84632e8b9e4f82969d7b4e22827d0037c51df5`. The needed arguments are
reproved here. The transfer construction in PR8128 at
`a103e6f867d1ea3e0a98d7af929fc478ef691ebd` motivates the next state question
but is not a premise of this note.

## 1. Exact model and local grades

Write E, P and C for the numbers of links, faces and cubes of a finite
cubic complex. Use the oriented coboundaries G (vertex to edge), F (edge
to face) and D (face to cube), with FG=0 and DF=0 over the integers.
On original link coordinates a_l in Z/3Z, define
`principal(x)=(x+1) mod 3-1` componentwise, and

    b(a)=principal(Fa) in {-1,0,1}^P,
    Q_c(a)=(Db(a))_c/3 in {-2,-1,0,1,2},
    N=sum_c Q_c^2.

Indeed b=Fa-3u for an integer face cochain u, so Db=-3Du is divisible
by three. Six signed principal face values bound |Q_c| by two. Gauge
transformations are the permutations a->a+G phi modulo three. They leave
b, Q and all mismatch weights unchanged, and commute with the operators
below. The physical space is the image of their orthogonal group average.

Use either free cubic boxes or periodic cubic boxes of side at least four.
All formulae act first on the original tensor product of link registers;
the original mod-three gauge-invariant subspace is preserved throughout.
For a signed original-link update a'=a+sigma e_l modulo three set

    m_lsigma(a)=[b(a')-b(a)-sigma F e_l]/3,
    W_lsigma |a> = exp(-mu ||m_lsigma(a)||^2) |a'>.

Here t>0, K>=0, finite mu>=0, lambda>0, and

    H=2t E I + lambda N + B,
    B=1.5 K sum_p b_p^2 - t sum_l,sigma W_lsigma.

The constant is exactly 2t per original link. Drop this scalar only in
commutators and dynamics. It is not replaced by a configuration escape rate.

Only four cubes can change Q when a given original link changes. Their edge
union has at most 33 links. Write N_l for their sum of Q_c^2, and define

    W_lsigma,r = W_lsigma 1_{N_l(a')-N_l(a)=r}.

This is an operator supported on that 33-link star. It satisfies

    [N,W_lsigma,r]=r W_lsigma,r.

The coarse bound |r|<=16 follows because each of the four cube terms lies
between zero and four. It is deliberately not the sharp possible grade
bound. Each component is a weighted partial permutation, so its norm is at
most one. For r!=0 at least one branch mismatch is nonzero, hence its norm
is at most exp(-mu). Adjoint pairs obey
W_lsigma,r^*=W_l,-sigma,-r. Every potential term has grade zero.

A fixed link lies in at most 33 such stars, by the translation and cubic
rotation symmetry of the infinite-lattice incidence count; free boundaries
only remove stars. It lies in at most four faces. For a vertical interior
link, the four-cube union is a `2x2x1` block: nine vertical links and twelve
in each transverse direction, hence33. Translation and cubic rotation
symmetry make the reverse incidence constant; counting all star/link
incidences on a torus gives33 stars per link. A free box only removes
incidences.

## 2. A fixed graded interaction norm

Use an explicit interaction representation

    A = sum_{X,r} A_{X,r},  [N,A_{X,r}]=r A_{X,r},
    ||A||_k = sup_l sum_{X containing l,r} exp(k |X|) ||A_{X,r}||.

The bound is on this chosen representation, not an assumed unique optimal
decomposition. Supports X are connected link sets. Grade splitting is kept
as part of the representation. A commutator uses support X union Y and
grade r+s; disjoint supports contribute zero. Combining terms is optional.

Let P_gr retain only grade zero. For Hermitian V having no grade-zero terms,

    I(V)=sum_{X,r!=0} V_{X,r}/r

is anti-Hermitian, has the same supports, and satisfies

    [I(V),N]=-V,  ||I(V)||_k <= ||V||_k.

P_gr and 1-P_gr contract this graded l1 norm. No spectral-gap estimate for B or
for the eventual neutral Hamiltonian is used.

For k'=k-delta>0,

    ||[A,C]||_{k'} <= [4/(e delta)] ||A||_k ||C||_k.       (1)

Proof: anchor a union at a link belonging to X or to Y. In the first case,
sum all Y intersecting X by their intersection link, giving a factor |X|;
the second gives |Y|. Use ||[A_X,C_Y]||<=2||A_X||||C_Y||,
exp(k'|X union Y|)<=exp(k'|X|)exp(k'|Y|), and
sup_{s>=0} s exp(-delta s)=1/(e delta). Grade convolution has exactly the
same l1 bound. This proves (1) for finite sums and then by absolute limits.

Distributing a total loss delta evenly across j commutators gives

    ||ad_S^j C||_{k-delta}
       <= [4j/(e delta)]^j ||S||_k^j ||C||_k.

Since j! >= (j/e)^j, if z=4||S||_k/delta<1,

    ||exp(ad_S)C-C||_{k-delta} <= z/(1-z) ||C||_k.        (2)

This is an absolutely convergent interaction expansion. Finite-volume
operator identities are ordinary matrix identities; the bounds do not grow
with the volume. Large global ||S|| is allowed. Local norm smallness is the
condition used in (2).

## 3. One step and an exponential iteration

Suppose the current operator is lambda N + D + V, with D grade zero and V
having no grade-zero terms. Put S=I(V)/lambda and conjugate by exp(S).
Here D denotes the diagonal interaction; it is distinct from the cubical
coboundary used to define Q in section1.
Using [S,lambda N]=-V exactly yields

    exp(S)(lambda N+D+V)exp(-S) = lambda N+D+R,
    R=sum_{j>=1} ad_S^j D/j!
                  + sum_{j>=1} j ad_S^j V/(j+1)!.

Set D_new=D+P_gr R and V_new=(1-P_gr)R. With d=||D||_k,
v=||V||_k, and z=4v/(lambda delta)<1, (2) gives

    ||R||_{k-delta} <= z/(1-z) (d+v).                   (3)

For the initial model take any k0>0 and the explicit bounds

    g = 66 t [1+32 exp(-mu)] exp(33 k0)
          + 6 K exp(4 k0),
    v0 = 2112 t exp(-mu) exp(33 k0).

The factor66 counts both signs and at most33 stars at an anchor link.
There is one zero grade and at most32 nonzero integer grades. The potential
contribution is four faces times its norm1.5K. These facts give the bounds
in this chosen graded representation.

They imply ||P_gr B||_{k0}+||(1-P_gr)B||_{k0}<=g and
||(1-P_gr)B||_{k0}<=v0<=g. They can be replaced by smaller verified local
norm bounds; the displayed constants deliberately retain a coarse grade
count. These are sufficient, very conservative constants; they do not locate
a useful or optimal experimental penalty. Assume

    lambda k0 >= 128 g,
    n=floor(lambda k0/(128 g)) >= 1,
    R0=16 g v0/(lambda k0-16 v0) <= v0/7.                (4)

First use one step with delta0=k0/4. Equation (3) bounds its remainder by
R0. Next use n steps, each losing delta=k0/(4n). Since lambda delta>=32g,
if d<=2g and v<=g then

    ||R|| <= [4v/(lambda delta-4v)](d+v) <= 3v/7 < v/2.

The induction closes: the first diagonal change is at most R0 and all later
changes sum to at most R0. Thus d<=g+2R0<2g, and final v<=R0 2^{-n}.
The total locality loss is k0/2. With

    U=exp(S_n)...exp(S_1)exp(S_0),

the resulting exact finite-volume identity is

    U H U^* = 2t E I + lambda N + D_* + V_*,
    [D_*,N]=0,
    ||D_*-P_gr B||_{k0/2} <= 2 R0,
    ||V_*||_{k0/2} <= v_* := R0 2^{-n},
    sum_j ||S_j||_0 <= (v0+2R0)/lambda < 2v0/lambda.     (5)

Every intermediate operator preserves the original mod-three gauge
symmetry. The construction can be made translation covariant on a torus
by retaining translated support labels. It does not make each Q_c commute
with D_*: grade zero preserves total sum Q_c^2, not the full charge vector.

This elementary route exploits bounded integer grades and does not invoke
the more general noncommuting-H0 theorem of Yin--Lucas. Its exponential
iteration is consistent with Gallone's 2026 result; it is not a claim that
the more general theorem's exponent is wrong. The proof uses the explicit
graded representation, whose initial support and closure are established
above; it does not assume that the overlapping cube terms are onsite.

## 4. Exact dressed constraints and a volume-uniform lifetime

Define Qtilde_c=U^*Q_c U, Ntilde=U^*N U, and the local defect projector
Pi_c=1_{Q_c!=0}, Pitilde_c=U^*Pi_c U. The dressed charges commute with one
another and have the original integer spectra exactly. Here is a direct
tail bound. Regard the successive conjugations as a time-ordered flow with
integrated interaction norm s=sum_j ||S_j||_{k0/2}<=2v0/lambda. In its
Dyson expansion of a local O_X with connected X, every term retains a
connected support containing X. Forget the grade labels in this estimate:
the ungraded interaction norm is bounded by the graded norm, and O need
not have a definite grade. Give all nested commutators together a loss
Delta=k0/4.
Their ordered scalar strength integrals are bounded by s^j/j!, so the
same argument as (2) bounds the sum of all nonconstant terms, with weight
exp((k0/4)|Y|), by

    [gamma/(1-gamma)] exp((k0/2)|X|) ||O||,
    gamma=4s/Delta <=32v0/(lambda k0)<=1/4.              (5a)

Every generated support contains any chosen link of X, so the anchored
interaction norm here also bounds the total weighted sum of this local
operator's terms. If a support reaches outside the graph-distance-R
neighborhood of X, its connectedness implies |Y|>=R. Dropping those terms
therefore changes U^* O_X U by at most

    [gamma/(1-gamma)] exp((k0/2)|X|) ||O|| exp(-k0 R/4).  (5b)

The truncated operator is supported in that neighborhood. Distance is in
the link graph with two links adjacent when they share a vertex. Original
stars and face boundaries are connected in this graph. This proves a
volume-independent exponential tail; it makes no claim that U itself is
close to the identity in global operator norm.

For any fixed local operator O supported on X,

    ||U^* O U-O|| <= 2 |X| ||O|| sum_j ||S_j||_0
                     <= 4 |X| ||O|| v0/lambda.          (6)

Indeed telescope the unitary automorphisms and use
||exp(-S_j)O exp(S_j)-O||<=||[S_j,O]||. Unitary conjugations are
operator-norm isometries, so no global ||U-I|| bound is needed. This yields
||Pitilde_c-Pi_c||<=48v0/lambda on a 12-link cube.

For a term V_{X,r}, only cubes intersecting X can contribute to its grade.
There are at most 4|X| such cubes, each Q_c^2 has spectrum in [0,4], so
|r|<=16|X|. Therefore

    ||[N,V_*]|| <=16 sum_{X,r}|X| ||V_{X,r}||
                   <=16 E v_*.                        (7)

If a density matrix is initially supported in U^*ker(N), then exact
Schrodinger evolution under H at real time tau obeys

    0 <= Tr(rho(tau) Ntilde) <=16 E v_* |tau|.          (8)

No assumption about this state's energy or being a ground state occurs.
On a cubic torus E=3C, giving average dressed charge-square density at most
48 v_* |tau|. If the initial state and the construction are translation
covariant, every cube has this bound individually. The dressed defect
probability is smaller than its charge square. Equation (6), the triangle
inequality on a purification, and Jensen's inequality give the bare
average defect probability bound

    (1/C) sum_c Tr(rho(tau) Pi_c)
       <= [sqrt(48 v_* |tau|)+48 v0/lambda]^2,           (9)

clipped to one. At tau=0 it is quadratic in v0/lambda. For arbitrary free
boxes replace 48 by 16E/C in the square-root term; the local rotation term
is unchanged. An individual non-translation-invariant cube is not bounded
by a global average.

Equations (8)--(9) exhibit an exponential interval for prepared dressed
neutral states, with v_*=R0 2^{-floor(lambda k0/(128g))}. They do not say
the remainder vanishes at finite lambda, or prove an infinite-time symmetry.

## 5. First effective correction and the constrained Hamiltonian

Write B_r for the global sum of initial terms of grade r. The first
generator is S0=sum_{r!=0}B_r/(lambda r). On P0=1_{N=0}, expansion through
order lambda^{-1} gives

    P0 exp(S0)(lambda N+B)exp(-S0) P0
       = P0 B P0 - lambda^{-1} P0 B (N|_{N>0})^{-1} B P0
           + O_box(lambda^{-2}).                      (10)

The negative sign is fixed by [S0,N]=-B_off/lambda. Terms [S0,B_0]
have nonzero grade and vanish between P0's. The quadratic correction is
negative semidefinite. The subscript box on the remainder is intentional;
the uniform interaction estimates are (3)--(5), not an unproved uniform
spectral perturbation statement.

The constrained first term can be identified without importing block1.
Let Z_lsigma be the partial original-link shift restricted to zero mismatch.
It preserves every Q_c and Z_lsigma^*=Z_l,-sigma. At an N=0 endpoint pair,
the wrap indicator on each face around a link must agree with the next:
Delta Q on each incident cube is the signed difference of those two
indicators. The fan is connected for free boxes and is a cycle for an
interior or periodic link. Thus either no incident face wraps or all r_l
incident faces wrap. In the latter case the initial face values are
b_p=sigma F_pl; the final values are -sigma F_pl. The transition is exactly
two unwrapped reverse shifts, including the original link residue because
-2sigma equals sigma modulo three. Consequently

    P0 W_lsigma P0
       = P0 [Z_lsigma+exp(-r_l mu) Z_l,-sigma^2] P0.    (11)

On the neutral space P0 C_mu P0=P0 B P0, where the local operator is

    C_mu=1.5K sum_p b_p^2
          -t sum_l [Z_l+Z_l^*+exp(-r_l mu)(Z_l^2+(Z_l^*)^2)],

Here Z_l=Z_l,+. This operator commutes with every cube charge on the full
coordinate space. There
are r_l=4 incident faces on a periodic cubic lattice. Finite mu retains the
second harmonic. It is not the mu-infinity first-harmonic model. Original
coordinates avoid discarding torus holonomies. No uniform comparison of
other N sectors is inferred from (10)--(11).

## 6. Actual ground states in a simultaneous volume/penalty limit

This is distinct from the prepared-state result (8). Fix finite mu>=0,
t>0 and K>=0. For each periodic L>=4 and lambda>0 the matrix H has
nonpositive off-diagonal entries and a connected configuration graph:
every single-link clock update has a strictly positive rate. Perron--
Frobenius therefore gives a unique positive normalized ground vector.
Every lattice translation and original mod-three gauge permutation
commutes with H, so this ground state is translation invariant and physical.

Write W_l=W_l,+. Each W_l has norm at most one and W_l^*=W_l,-. Thus
2I-W_l-W_l^*>=0, and K>=0 gives H>=lambda N. The gauge-averaged zero-flux
configuration is a trial vector with energy 2tE: no single link shift is a
pure gauge shift on these tori and every potential vanishes on this orbit.
The ground energy is therefore at most 2tE. Translation invariance and
E=3C give

    <Q_c^2>_{L,lambda} <= 6t/lambda                    (12)

for every cube, uniformly in L and K. For any fixed finite set of cubes R,
their commuting projectors give

    <1-product_{c in R}(1-Pi_c)> <=6t |R|/lambda.       (13)

Now take any sequence L_j->infinity and lambda_j->infinity, with no
specified relative rate. Embed each fixed local observable into sufficiently
large tori. By compactness of states on the finite-dimensional local
algebras and a diagonal subsequence, there are subsequential local limits
omega. Every such limit is translation invariant, original-gauge invariant,
and satisfies omega(Q_c^2)=0 for each cube. It is an actually neutral state,
not just one with small average charge density.

Let A be any finite-support operator commuting with every Q_c. The exact
finite-volume ground-state inequality is

    <A^*[H,A]> >= 0.

Its lambda term vanishes identically, leaving <A^*[B,A]> >=0. Only finitely
many local terms of B enter this commutator, with bounds independent of
volume and lambda. Pass to the subsequential state omega. Neutrality and
the local endpoint identity (11) imply

    omega(A^*[C_mu,A]) = omega(A^*[B,A]) >=0.            (14)

To justify the replacement, use the product of neutral projectors on the
finitely many cubes touching A and the contributing link stars. This
product acts as the identity on omega in its GNS representation, by
omega(Q_c^2)=0 and positivity. It commutes with A, and sandwiches B and
C_mu identically on those local neutral endpoints.

Equation (14) is the local ground-state condition on the constrained
algebra of operators commuting with all Q_c. Equivalently, local operators
may be sandwiched by all affected neutral projectors; that sandwich has
finite enlarged support and commutes with every cube charge. This does not
assert a ground-state condition for charge-creating operators at infinite
penalty. It constructs constrained ground states as limits of actual full
ground states without a uniform finite-lambda sector-ordering theorem.

There is no claimed unique limit, no interchange of two separately proved
limits, no conclusion about a finite-lambda Coulomb phase, and no spectral
gap estimate. The result is uniform along simultaneous divergent sequences.

## 7. Logical controls and remaining phase gap

An open Ising chain supplies a control outside the cubic clock model.
Let N=sum_i(1-Z_i Z_{i+1})/2 and perturb with -h sum_i s_i Z_i, where s_i
is +1 on the left half and -1 on the right half. All terms commute, so the
normal-form remainder is exactly zero and every prepared neutral state
remains neutral forever. Each neutral configuration has field energy zero.
The domain-matching configuration has one wall and energy lambda-h L<0
when L>lambda/h. Its ground state therefore lies outside N=0, even at an
arbitrarily small fixed local h/lambda. This is not a counterexample for
our clock geometry; it isolates why approximate constraint dynamics cannot
by itself prove ground-sector selection.

Also, the full neutral constraint space is not locally indistinguishable.
The all-zero flux configuration and a single unwrapped link curl both have
Q=0 but give b_p^2 equal to zero and one on an affected plaquette. Thus a
local-topological-order stability theorem cannot be applied to ker(N)
merely because its constraints look gauge-like. A selected ground state of
C_mu may have additional structure; that remains a separate question.


## 8. Primary literature and method boundary

The normal-form method is standard. The direct derivation above was checked
against [Gallone, arXiv:2604.13781v2](https://arxiv.org/abs/2604.13781v2),
whose full sixteen pages were read. Its Theorem1.1 treats onsite integer
number operators, while Remark1.2(vii) discusses larger supports with
strongly local perturbations. Here the cube penalties overlap. The initial
33-link supports and exact integer grades are established directly, and
commutator closure preserves those supports without repeated enlargement.
No general novelty claim is made for exponential prethermalization.

[Yin--Lucas, arXiv:2209.11242v2](https://arxiv.org/abs/2209.11242v2),
Theorem3 and Corollary4, give a more general approximate block diagonalization
with a finite remainder. [Pace--Wen, arXiv:2301.05261v5](https://arxiv.org/abs/2301.05261v5)
explicitly conjectures the exact local dressing used in its relevant
emergent-symmetry discussion. Neither is used as an exact ground-sector
selector here. The pairwise spin-coupling hypotheses in
[Bjornberg--Ueltschi, arXiv:2204.12896v2](https://arxiv.org/abs/2204.12896v2),
Theorems3.1--3.2, are not an established match to this plaquette Hamiltonian.
These references motivate comparisons; all load-bearing estimates used by
this note are derived internally.

## 9. Executable scope

The runner constructs independent cubic incidence matrices, checks all
192 link stars on a periodic side-four cube, and challenges locality by
changing coordinates outside a tested star. A complete enumeration of
531441 original one-cube link configurations verifies243 physical flux
states and equal gauge fibers of2187 configurations. It checks the inverse
commutator signs, the negative second-order correction, the retained second
harmonic, and repeated finite matrix transformations at four penalties.
The two-cube witness is independently lifted to original clock coordinates
by modular elimination. An independent Lie--Schwinger integral checks the
conjugation remainder.

The finite matrix examples use moderate penalties below the displayed
conservative uniform-theorem threshold. They challenge identities and
coefficients; they do not certify the infinite family by extrapolation.
The analytic norm proof supplies that family. A two-cube witness moves
charge while retaining its total square; an actual neutral-space observable
has both eigenvalues zero and one. Exact Ising-chain and product-rotation
controls isolate the separate ground-selection and global-fidelity claims.
No finite eigenvalue trend is called a phase proof.

## 10. Negative-boundary discipline

### N1 — Materially different mechanisms

| Route | Status | What it does or still needs |
|---|---|---|
| Integer-graded local normal form | ATTEMPTED: proved in sections2-4 | Controls dressed prepared states with nonzero finite-penalty remainder |
| Variational density and local compactness | ATTEMPTED: proved in section6 | Constructs actual neutral ground-state limits without selecting a finite-penalty block |
| Uniform charge-sector rearrangement or local repair | OPEN | Could compare the actual sector energies at fixed penalty |
| Stability of a Coulomb phase under charge-changing interactions | OPEN | Needs an actual reference phase and a checked stability mechanism |
| Local-topological-order ground-code theorem | ATTEMPTED: applicability premise fails for all of ker(N) | A local b-squared observable distinguishes neutral states; a selected ground subspace may differ |
| Native rule and Record compiler | OPEN | Could identify a framework law independently of these supplied-model estimates |

No open mechanism is declared excluded. The current counterexamples are
narrow author calculations, not an invented prior retained no-go.

### N2 — Relations among remaining obligations

Finite-penalty ground selection, the phase of a constrained ground state,
and native law selection are distinct stated obligations. Whether future
proofs of one also resolve another is not established in either direction.
No logical-independence theorem or inflated wall count is asserted. The
Ising example only proves that a general constraint-lifetime statement,
by itself, does not select the true ground sector.

### N3 — Hidden assumptions

The three-state link carrier, positive rate, finite mismatch penalty, cube
charge, original-link multiplicities and fixed electric diagonal are all
supplied explicitly. Prepared states are distinguished from true ground
states. Strong penalty is an explicit inequality with conservative
constants. Translation invariance is required to pass from an average
charge bound to an individual cube. The limit ground condition is stated
on the constrained local algebra, not on charge-creating operations.

### N4 — Residual matching

The exact two-cube witness establishes only that preserving total charge
square does not preserve each charge. The Ising chain establishes only a
failure of a generic ground-selection inference, outside this cubic clock
model. The local b-squared example establishes local distinguishability
of the full neutral space. None is a photon, phase or native-axiom no-go.
The simultaneous limit proves what it states and is not a fixed-penalty
sector theorem under another name.

### N5 — Resolution audit

The cache prints substantive per-element, per-site, per-mode, per-block and
lattice-wide scope lines. Original local updates, complete one-cube gauge
fibers, finite matrix modes and exact control blocks are executed. Infinite
volume and arbitrary perturbative order are handled in the written proof;
the runner does not execute them or infer a physical phase from them.

### N6 — Partial closure and axiom boundary

Equations(5), (8) and (12)--(14) give useful controlled constructions without
an axiom change. The finite-mu second harmonic remains present. No statement
that a retained primitive is absent is made, and no axiom, primitive,
selector or editable prompt is changed. A future finite-penalty state
estimate or native realization can add information without contradicting
these bounded conclusions.

### N7 — Steelman

A reviewer should ask why long-lived prepared states say anything about a
vacuum. Alone they do not; section6 supplies a separate actual-ground
limit and keeps its divergent-penalty qualification. A reviewer should also
insist that a charge-neutral spin-one gauge Hamiltonian need not have a
Coulomb phase. That phase remains to be demonstrated for its actual state.
The strongest remaining route is a uniform state estimate or a matched
stability theorem, not a count of successful finite matrices.

### N8 — Cross-campaign comparison

The earlier fixed-box projection and local positive bare-defect result are
compatible with this note. The normal form explains how dressed neutrality
can coexist with positive bare defects, while the simultaneous limit avoids
claiming a volume-independent finite-penalty spectral projection from an
extensive norm estimate. The positive-transfer milestone supplies a matched
regulator, not the missing state. No prior failed phase route is recycled
as an axiom obstruction.

**Gate disposition:** scoped positive theorems and explicit control
boundaries; independent review and formal audit remain pending.

## Author review record

The complete source and runner were personally reviewed. Eighteen deliberate
mathematical faults are detected, including charge and incidence errors,
inverse-denominator signs, omitted harmonics, reversed rotations, a wrong
prepared state and a missing integral weight. One challenge exposed a weak
witness check; it was repaired by independently rechecking the selected
charges and solving for their original clock coordinates. The canonical
runner cache is fresh. These are author checks, not an independent review
or a formal audit verdict. Full pipeline, strict lint and combined
current-main landing gates remain pending; no author main merge or push is
part of this packet.
