# Block 9: local integer normal form for the supplied penalty Hamiltonian

Status: personal working derivation, 2026-09-14. Not independently reviewed.
This is a new attack on controlled constraint dressing, not a ground-state
selection or Coulomb-phase theorem. No axioms or native law are changed.

## Why this route

Block 8 now matches a positive transfer to the actual supplied clock
Hamiltonian. The next unresolved object is its state. Pace--Wen 2301.05261v5
explicitly conjectures the exact local dressing it uses (pages 1--5 read).
Yin--Lucas 2209.11242v2, Theorem 3 and Corollary 4, instead gives a nonzero
prethermal remainder. Its hypotheses and proof are being checked; it is not
an exact-symmetry or ground-sector theorem. The pairwise-spin assumptions of
Bjornberg--Ueltschi 2204.12896v2, Theorems 3.1--3.2, do not directly match
our plaquette hopping. We therefore derive a simpler integer-graded local
normal form directly for this model. Literature is context, not a proof
premise of the algebra below.

Subsequent primary-source search found Gallone, *On Exponentially Long
Prethermalization Timescales in Isolated Quantum Systems*, arXiv:2604.13781v2
(2026-09-08). All sixteen pages were read in extracted text. Its normal-form
strategy, fixed interaction norm, commutator estimate and finite optimal
iteration agree with the structure independently written below. Theorem1.1
assumes onsite integer number operators; Remark1.2(vii) discusses larger
supports with strongly local perturbations. The present model has overlapping
cube penalties, so an onsite theorem is not simply imported. Our initial
33-link support and exact grade labels are checked explicitly and then
preserved by commutators. No novelty claim is made for normal-form or
prethermal machinery. The contribution sought here is its checked use for
this precise principal-flux Hamiltonian and its prepared-state bounds.

The useful opportunity is that N=sum_c Q_c^2 has an integer spectrum and
commuting local terms, even though their supports overlap. Decomposing the
initial hopping into its N grades once avoids repeatedly enlarging supports
when inverting ad_N. Nested commutators add grades and take unions of
overlapping supports. This could provide exponentially accurate conservation
of a dressed total penalty, uniformly with volume. It still cannot identify
which N block minimizes the energy.

## 1. Exact model and local grades

On a finite cubic complex use original three-state link coordinates a_l,
the boundary maps F (edge to face) and D (face to cube), and

    b(a)=principal(Fa) in {-1,0,1}^P,
    Q_c(a)=(Db(a))_c/3 in {-2,-1,0,1,2},
    N=sum_c Q_c^2.

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
only remove stars. It lies in at most four faces. These counts still need
an independent explicit geometric check before packaging.

## 2. A fixed graded interaction norm

Use an explicit interaction representation

    A = sum_{X,r} A_{X,r},  [N,A_{X,r}]=r A_{X,r},
    ||A||_k = sup_l sum_{X containing l,r} exp(k |X|) ||A_{X,r}||.

The bound is on this chosen representation, not an assumed unique optimal
decomposition. Supports X are connected link sets. Grade splitting is kept
as part of the representation. A commutator uses support X union Y and
grade r+s; disjoint supports contribute zero. Combining terms is optional.

Let P retain only grade zero. For Hermitian V having no grade-zero terms,

    I(V)=sum_{X,r!=0} V_{X,r}/r

is anti-Hermitian, has the same supports, and satisfies

    [I(V),N]=-V,  ||I(V)||_k <= ||V||_k.

P and 1-P contract this graded l1 norm. No spectral-gap estimate for B or
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
Using [S,lambda N]=-V exactly yields

    exp(S)(lambda N+D+V)exp(-S) = lambda N+D+R,
    R=sum_{j>=1} ad_S^j D/j!
                  + sum_{j>=1} j ad_S^j V/(j+1)!.

Set D_new=D+P R and V_new=(1-P)R. With d=||D||_k,
v=||V||_k, and z=4v/(lambda delta)<1, (2) gives

    ||R||_{k-delta} <= z/(1-z) (d+v).                   (3)

For the initial model take any k0>0 and the explicit bounds

    g = 66 t [1+32 exp(-mu)] exp(33 k0)
          + 6 K exp(4 k0),
    v0 = 2112 t exp(-mu) exp(33 k0).

They imply ||P B||_{k0}+||(1-P)B||_{k0}<=g and
||(1-P)B||_{k0}<=v0<=g. They can be replaced by smaller verified local
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
    ||D_*-P B||_{k0/2} <= 2 R0,
    ||V_*||_{k0/2} <= v_* := R0 2^{-n},
    sum_j ||S_j||_0 <= (v0+2R0)/lambda < 2v0/lambda.     (5)

Every intermediate operator preserves the original mod-three gauge
symmetry. The construction can be made translation covariant on a torus
by retaining translated support labels. It does not make each Q_c commute
with D_*: grade zero preserves total sum Q_c^2, not the full charge vector.

This elementary route exploits bounded integer grades and does not invoke
the more general noncommuting-H0 theorem of Yin--Lucas. Its exponential
iteration is consistent with Gallone's 2026 result; it is not a claim that
the more general theorem's exponent is wrong. The support and graded-norm
hypotheses still need full author review before this is packaged.

## 4. Exact dressed constraints and a volume-uniform lifetime

Define Qtilde_c=U^*Q_c U, Ntilde=U^*N U, and the local defect projector
Pi_c=1_{Q_c!=0}, Pitilde_c=U^*Pi_c U. The dressed charges commute with one
another and have the original integer spectra exactly. Here is a direct
tail bound. Regard the successive conjugations as a time-ordered flow with
integrated interaction norm s=sum_j ||S_j||_{k0/2}<=2v0/lambda. In its
Dyson expansion of a local O_X with connected X, every term retains a
connected support containing X. Forget the grade labels in this estimate:
the ungraded interaction norm is bounded by the graded norm, and O need
not have a definite grade. Give all nested commutators together a loss Delta=k0/4.
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

## 5. First effective correction and finite falsifiers to build

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

Thus C_mu=P0 B P0 on the neutral space is the restriction of the local
operator

    C_mu=1.5K sum_p b_p^2
          -t sum_l [Z_l+Z_l^*+exp(-r_l mu)(Z_l^2+(Z_l^*)^2)],

which commutes with every cube charge on the full coordinate space. There
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

Each W_l has norm at most one and W_l^*=W_l,-. Thus
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

Its lambda term vanishes identically, leaving <A^*[B,A]>>=0. Only finitely
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

Build independent checks of: 33-star/4-cube geometry, full original-link
grade locality and partial-permutation norms, cube gauge reduction, exact
grade inverse signs, second-order correction, repeated finite matrix normal
form, local-unitary bound, majorant inequalities, bare versus dressed
probabilities, and the following logical control.

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

## Open obligations

Check the full graded-norm proof, especially exponential iteration and
telescoping local conjugations and the direct Dyson tail bound (5b).
Check all geometry on independent incidence construction. Then decide if
this is useful enough for a bounded milestone. Actual ground-state sector,
Coulomb correlations, photon dispersion, and native law selection remain
separate open obligations. Continue the personal campaign to its deadline.
