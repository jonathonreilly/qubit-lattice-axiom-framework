---
claim_id: permanent_local_gaussian_likelihood_protocol_and_dk_postselection_cost_bounded_theorem_note_2026-09-14
claim_type: bounded_theorem
claim_scope: "A supplied finite-type stage-ordered complex arithmetic circuit of total degree at most four has a fixed-period nearest-neighbor cubic realization with vertex-disjoint wires, one permanent complex-payload M2 record per active site, and a single covariant local instruction rule. Supplied Gaussian likelihood programs produce exact finite-alpha posteriors and controlled positive-window approximations, with explicit acceptance costs. The current finite Dirac-Kahler source has a checked common degree-three circuit across its four arms and two variances. A local Hodge estimate gives dimension-independent massive coercivity on the stated even-half-cover family. The source/program/schedule and conditioning are supplied; the full finite DK coordinate roster is not instantiated, and native action, Record-star probability, quantum/fermion identification and typical physical phase remain open."
upstream_dependencies: []
runner: scripts/permanent_local_gaussian_likelihood_protocol_2026_09_14.py
---

# Permanent local Gaussian likelihood programs and their conditioning costs

**Date:** 2026-09-14
**Type:** bounded_theorem
**Status:** proposed_retained

A supplied Gaussian likelihood circuit can be implemented by permanent records
that read only nearest neighbors. A periodic routing construction keeps its
wires separate, preserving the causal write order. The desired Gaussian
appears as a posterior after conditioning on later observations; finite prior
and observation-window errors, and the acceptance probability, are explicit.
The actual finite Dirac-Kahler comparison source is checked at the logical
circuit and Gaussian-algebra level. Its full physical coordinate roster is
not instantiated by the finite geometry checks.

## Status, target and premise contract

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: upstream_support
target_claim_id: admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_bounded_theorem_note_2026-08-23
target_blocker_text: "Construct a local permanent formation protocol, distinguishing its output law from a Gaussian full-conditional specification."
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Test a physically selected history law and its native Record observable; retain the explicit supplied-program and posterior-conditioning costs."
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "Explicit cubic embedding, local instruction, Gaussian conditioning and uniform source-bound derivations; the physical law and selected state are not inferred."
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

The contextual consumer is the current finite strict-neighbor compiler,
`ADMISSIBILITY_DIRAC_KAHLER_STRICT_NEIGHBOR_M2_GAUSSIAN_COMPILER_BOUNDED_THEOREM_NOTE_2026-08-23.md`,
at main revision `5deabeb698a27c2c3f68c5df685af2521ef15307`.
It supplies a static Gaussian comparison, with its native formation question
explicitly separate. This note addresses a supplied permanent likelihood
program, and does not claim to reproduce that source's original Record-star
experiment or its local formation weights. No theorem or audit status from
that contextual note is imported.

| Input | Role | Provenance | Open physical bridge |
|---|---|---|---|
| Finite circuit, stage order and coefficients | Program to be embedded | Defined below | Microscopic action selection |
| Independent complex Gaussian innovations and parameters | Reference probability model | Defined below with complex Lebesgue measure | Physical probability selection |
| Initial controls and fair causal schedule | Formation conditions | Supplied here; finite default-atom bootstrap below | Typical program and schedule selection |
| Spatial/Pauli frame correspondence and instruction alphabet | Encoding | Defined below | Physical representation identification |
| Accepted window and finite-alpha limit | Posterior selection | Chosen here, with quantified accuracy and rarity | Typical-state identification |
| Released source helper and matrix supplier | Finite source definitions | Current-main files linked below and byte-bound by the runner | Source selection |

The payloads are commuting classical complex random variables. The DK name
identifies a supplied matrix construction, not a fermion or quantum-operator
identification. The native axioms and approved primitives are not modified,
and no fitted physical observations enter this comparison.

The proof obligation graph is explicit:

| Step | Basis in this note | Consequence |
|---|---|---|
| Gaussian completion and determinant integral | Derived by block algebra and normalized densities | Exact finite-alpha posterior and arm weights |
| Positive-window bounds | Derived density, KL and convexity inequalities | Accuracy and acceptance costs |
| Separated periodic immersion and detours | Coordinate and disjoint-box proof below | Vertex-disjoint cubic wires |
| Causal levels, carrier and local instruction | Explicit stage function, Pauli algebra and decoder | One permanent nearest-neighbor write per active site |
| Local Hodge margin and covariance bound | Local quadratic forms and block covariance inequality | Uniform massive source coercivity |

No open lemma is used as a proved step of these conditional mathematical
claims. The strongest unresolved physical obligation is a selected
unconditioned native history law with a validated physical observable map.
That separate target is not claimed reduced to a weaker solved lemma.

## Exact conditioning and the proper-prior perturbation

The current released source has complex variables psi=(phi,zeta) and action

    S0(psi)=c^-1 ||q phi-B zeta||^2+||zeta||^2,
    B B*=S-c I,       S=(q+q*)/2 > 0.

Its q, B, c and the four arm values are supplied, not axiom consequences.
Define d=n+k, n=dim(phi), k=dim(zeta),

    L=[[q,-B],[0,I]],       N=diag(c I_n,I_k),
    Q0=L* N^-1 L.

q is invertible and N is strictly positive. Supply independent proper complex
Gaussian roots psi~CN(0,alpha^-1 I_d), alpha>0, then independent observations

    Y=L psi+eta,            eta~CN(0,N).

Here CN(0,C) has density exp(-z*C^-1 z)/(pi^d det C) with respect to
ordinary real 2d-dimensional Lebesgue measure. Completing the square gives

    psi | Y=0 ~ CN(0,C_alpha),     C_alpha=(Q0+alpha I)^-1.

The point conditional is the continuous Gaussian version. The unconditional
root law stays the supplied independent prior. No exact equality to C0 is
claimed at finite alpha. The alpha-to-zero limit is a limit of proper priors,
not permission to treat an improper uniform prior as a probability law.

The prior/likelihood Gaussian integral, or Sylvester's determinant identity
applied to Cov(Y)=N+alpha^-1 L L*, gives

    p_alpha(Y=0)=alpha^d/[pi^d det N det(Q0+alpha I)].

For the source itself,

    det Q0=|det q|^2/c^n,
    Q0^-1=[[q^-1 S q^-*, q^-1 B],
           [B* q^-*,            I]],
    q^-1 S q^-*=(q^-1+q^-*)/2.

Thus the supplied source raw mass c^n/|det q|^2 is det(Q0)^-1. Within
each four-arm menu d and c are constant, so equal prior arm weights and
conditioning at Y=0 approach its normalized raw-mass weights as alpha->0.
Across different choices of c, det N changes: the likelihood normalization
cannot be silently discarded to claim the same cross-model weights.

For the disclosed width-four, T_cover=12, xgraded, m=1 source, n=24,
k=40 and d=64. The runner binds the released helper SHA256 and its current
Block105 supplier certificate. It checks all four arm values at c=1/2 and
c=1/3. It does not reinterpret this finite 1+1-dimensional fixture as a
three-dimensional infinite-volume physical field.

## Explicit finite-alpha bounds

If Q0>=m0 I, diagonalization gives

    1 <= det(Q0+alpha I)/det Q0 <= (1+alpha/m0)^d,
    ||C_alpha-C0|| <= alpha/m0^2.

For t>=0,

    1/(1+t)-1+log(1+t) <= t^2/2,

because the derivative of the left side is t/(1+t)^2<=t. Hence the proper
complex Gaussian KL and Pinsker bounds are

    D(CN(0,C_alpha)||CN(0,C0)) <= d alpha^2/(2m0^2),
    TV <= alpha sqrt(d)/(2m0).

One exact finite lower bound is m0=1/Tr(C0), since the largest positive
eigenvalue is at most the trace. Here Tr(C0)=k+Tr Re(q^-1), so no spectral
fit or radical full-matrix inversion is needed. Use the minimum of these
armwise lower bounds for a common menu bound.

Write w_j for the normalized target arm weights and t_j in
[(1+alpha/m0)^-d,1] for their determinant tilts. The perturbed weights are
w_j t_j/E_w(t). A rejection coupling, accepting j with probability t_j,
gives

    TV(w_alpha,w) <= 1-(1+alpha/m0)^-d <= d alpha/m0.

This can be a loose finite bound; it is a bound, not a precision estimate.
The runner also applies the source-specific uniform margin proved below and computes the exact rational
arm weights at alpha=1/10
and 1/100. It independently conditions the full joint covariance numerically
and compares full precision log determinants to the smaller exact Schur
formula

    P_phi(alpha)=alpha I+(1+alpha) q*(S+alpha c I)^-1 q,
    det Q_alpha=(1+alpha)^(k-n) det(S+alpha c I) det P_phi(alpha)/c^n.

## Positive observation windows: accuracy and rarity

Let W_epsilon={y: |y_i|<=epsilon for all i}, a product of complex disks,
and nmin=min(c,1). Cov(Y)>=N implies Cov(Y)^-1<=N^-1. Thus, throughout
the window,

    exp(-d epsilon^2/nmin) p_alpha(0) <= p_alpha(y) <= p_alpha(0).

Its real volume is (pi epsilon^2)^d, so the acceptance probability obeys

    exp(-d epsilon^2/nmin) alpha^d epsilon^(2d)
       /[det N det Q_alpha]
    <= P(W_epsilon) <=
    alpha^d epsilon^(2d)/[det N det Q_alpha].

Both quantities are positive for finite positive alpha,epsilon. Their decay
as alpha or epsilon shrinks, and their dimension dependence, are explicit.
There is no claimed nonvanishing thermodynamic acceptance probability.

For nonzero y the posterior is CN(C_alpha L* N^-1 y,C_alpha). The identity

    N^-1/2 L C_alpha L* N^-1/2 <= I

follows from C_alpha^-1=alpha I+L*N^-1 L. The KL of this shifted Gaussian
from CN(0,C_alpha) is at most y*N^-1 y, hence at most d epsilon^2/nmin.
Convexity of KL and Pinsker give

    TV(P(psi | W_epsilon), CN(0,C_alpha))
        <= epsilon sqrt(d/(2 nmin)).

Arm weights conditioned on W_epsilon differ from those conditioned by the
zero-density prescription by at most 1-exp(-d epsilon^2/nmin), using the
same rejection coupling. Adding these explicitly controlled errors and the
finite-alpha errors bounds the joint arm/field approximation to the supplied
target. These limits construct a conditional comparison, not typical native
phase selection or a Born rule. A rare selected ensemble is a physical cost.


## Input and output of the geometric construction

Supply finitely many gate types h=0,...,H-1, each with one complex payload,
and directed edge types e from (n,h_left) to (n+delta_e,h_right), n in Z^3.
Let ||delta_e||_infinity<=R. The total incident degree at every gate type
is at most four. Supply integer stages s_h such that s_left<s_right for
every edge. This is stronger than merely acyclic behavior on one finite
cover: the same type-level DAG works on every cover.

Assume E>=1 in the wire formulas below. An edgeless program needs only
separated gate/control pairs and no routing or crossing argument.

The construction produces periodic, vertex-disjoint nearest-neighbor wires,
meeting only at their true gate endpoints. Each internal vertex stores a
single complex copy. The number of sites and the maximum wire length per
coarse cell are finite constants fixed by the input graph, independent of
the number of coarse cells. This is an existence/resource bound, not an
efficient architecture. All initial program conditions remain supplied.

## A periodic immersion with only isolated transverse crossings

Here are the coordinates, stated again so the mathematical argument does not
depend on the prior static Gaussian compiler's provisional theorem.
Set P=2R+2, C=P^3, q=ceil(sqrt(CH)), z0=8 and

    M=max(20q+20, z0+16+E C)+16.

For coarse n, let cid(n)=((n_x mod P)P+(n_y mod P))P+(n_z mod P),
j=H cid(n)+h, and put the gate at

    home(n,h)=Mn+(10+20(j mod q), 10+20 floor(j/q), z0).

Assign incident half-edges distinct directions from +x,-x,+y,-y. From a
home, its arm goes one step in that direction, one step in -z, then three
further steps in its horizontal direction. This ends at a port column
home+4 direction-e_z. Distinct arms meet only at the home. Home centers
are separated by at least twenty before scaling, including coarse seams;
port column coordinates are consequently distinct modulo M.

For e starting at n and ending at n+delta_e, join the two port columns at

    plane=max(n_z,(n+delta_e)_z)M+z0+8+e C+cid(n).

The path ascends the left column, goes in x then y on this plane, descends
the right column and reverses the right terminal arm. The plane is above
BOTH endpoints. The original path length L is bounded by

    L <= (3R+4)M+16.

Horizontal planes never equal a terminal arm/home level: their residues
modulo M lie in [z0+8,z0+8+EC-1], while terminal levels have residues z0-1
or z0. Equal main planes identify edge type, source color and maximum
endpoint coarse height. For fixed edge type and source color this fixes
source n_z. Distinct such occurrences are separated by PM horizontally;
their horizontal boxes have span less than (R+1)M<PM, so they do not meet.

Port column XY residues identify their home color, gate type and port. Two
occurrences using the same column XY are separated vertically by PM; each
vertical interval has length less than (R+1)M, so they do not meet. Finite
terminal arms in separated home neighborhoods have no foreign intersection.
No path crosses a foreign home or its terminal first step.

Thus every remaining foreign crossing consists of one straight vertical
column interior and one horizontal straight segment or x/y corner. There
are no overlapping horizontal intervals or overlapping vertical intervals,
no foreign endpoint crossings, and no three-strand crossings. Quotient
covers with each coarse side a multiple of P inherit this classification:
the span bounds exclude self-aliasing, and crossings across seams are the
images of the same infinite periodic construction.

## Scale-ten detours remove all foreign intersections

Scale the entire immersion by ten. At each foreign crossing center c leave
the horizontal wire unchanged. Suppose its vertical wire is traversed in
direction d e_z, d=+1 or -1. Replace the vertical interval from c-2d e_z
to c+2d e_z with

    c-2d e_z,
    c-2d e_z+e_x,
    c-2d e_z+e_x+e_y,
    c+2d e_z+e_x+e_y,
    c+2d e_z+e_x,
    c+2d e_z.

Each displayed axis segment is filled with unit copy sites. At the crossing
height, the vertical detour lies at horizontal offset (1,1); the other wire
lies on the x/y axes through c, even at a corner. The detour's horizontal
steps occur at heights c_z+-2, where there is no original horizontal wire.
All original columns and plane heights are on the ten-grid. Detour boxes
at different crossings are therefore disjoint: distinct columns differ by
at least ten in a horizontal coordinate, or crossings on one column differ
by at least ten vertically. No detour meets an original unrelated wire.

The crossing is strictly interior to its vertical column. The distance to
its endpoints is at least ten, so the four-unit replacement is available.
Each detour increases length by exactly four. A path with original length
L has at most L-1 foreign crossings, hence final length

    L' = 10L+4(number of its detours) <= 14L.

The result is a graph subdivision with distinct physical vertices on
distinct wires, except for true shared gates. Every home has the unused
neighbor home-e_z in the scaled geometry, available as an initial control.
It lies on no wire. The formula and crossing classification are periodic;
therefore the complete finite role map repeats with physical period 10MP.

The primary runner first checks all original unit vertices, then uses a
different inclusive-integer-segment intersection calculation for the final
geometry. It rejects positive interval overlaps, foreign intersections and
control collisions, and checks each wire for repeated vertices. The doubled
cover additionally compares the complete compressed route coordinates
relative to their coarse origins against the smaller cover's role roster.
These finite challenges support the proof; their counts are not the proof.

## Causality is preserved at physical sites

Let Lmax bound every final wire length. Give a gate the integer level
s_h Lmax. On an edge beginning at stage s_left, give its j-th internal
copy the level s_left Lmax+j. Its first copy is later than its source and
its last copy is earlier than its destination, since s_right>=s_left+1
and j<L'<=Lmax. Distinct wires share no internal site, so there is no new
physical dependency from a crossing. The physical dependency graph is a
DAG on every cover, with depth at most (max s-min s)Lmax.

Attach an independent innovation to each stochastic root/observation gate;
copy/scale/sum gates are deterministic. For any fixed coherent program,
the acyclic recursion determines all written values as functions of these
innovations. Every fair causal schedule yields this same final law, even
if it chooses among currently enabled gates based on already written data.
No future innovation may be read, and fairness/completion remains assumed.
No write updates an existing record. A nearest-neighbor rule reads only
the declared parent records and may ignore other present neighbors.

For the infinite periodic type DAG, every finite set has a finite ancestor
set. Independent innovations therefore also define the infinite forward law
directly; sufficiently large covers agree on an unwrapped ancestor set.
At fixed graph depth it has finite dependence range, because disjoint
innovation ancestor sets give independent outputs. A long-range Gaussian
posterior obtained after conditioning is a different law; no uniform
postselection/infinite-volume interchange is asserted.

## A single covariant rule and readable matrix carriers

For each nonnegative integer role r in a finite alphabet and proper-cubic frame R use

    M=z I+(8r+1)(R(1,2,3)).sigma.

Trace decodes the one complex value. The traceless vector has norm
(8r+1)sqrt(14), which decodes r; the free orbit decodes R. These are
disjoint closed affine complex planes in M2(C). Proper rotations act by
ordinary Pauli conjugation; coordinates and the supplied frame co-rotate.
The identity sigma(u)sigma(v)=(u.v)I+i sigma(u cross v) shows directly
that every proper rotation preserves products and adjoints. Equivalently,
quarter-turns U_j=(I-i sigma_j)/sqrt(2) generate the required conjugations.
The codec chooses a downstream instruction representation, not a privileged
physical spinor or selected action.

A role contains its outgoing direction/next-role table, required incoming
roles, and its finite gate instruction. In a valid program neighborhood,
the parent tags identify one target role and frame; the rule requires all
its parents and evaluates that instruction. Gaussian gates push the specified
one-complex Gaussian into its role plane; deterministic gates use a point
mass there. Other neighbors are irrelevant data. On conflicting/unrecognized
neighborhoods the rule can use a fixed proper-rotation-invariant default
distribution. This defines one answer on every neighborhood; along the
supplied causal program only the stated instruction cases are exercised.
Translations and proper rotations commute with the decoder and these tables.

Initial controls, coefficients, Gaussian parameters and a causal formation
schedule are presently supplied. A finite auxiliary bootstrap can make the
initial controls themselves supported formation outcomes: at an empty
neighborhood let the default law draw uniformly from the finite control
roles and all 24 frames, with complex payload zero. Control sites are
pairwise nonadjacent, so they may form first with independent draws. Any
specified coherent finite control pattern has positive probability, a
product of the corresponding atom probabilities. Conditioning on that
pattern gives the protocol used above, with an additional rare-program
conditioning cost. Selecting a typical program, initial state and formation
schedule is a separate research task. Only finite coherent-program
probabilities are evaluated here.

## Application to the supplied DK likelihood circuit

The actual finite linear map L has a common union roster of 208 coefficient
positions across all four arms and both c choices. Keep a scale gate even
when its coefficient is zero. Binary fanout and sum trees then give the same
768-node, 848-edge, degree-three, depth-nine circuit in every case. The
runner checks the topology digest independently of the coefficient digest
and reproduces every row of L exactly.

Any finite circuit is a special case of the geometric input: make each gate
a separate type, let all displacements be zero and replicate the whole
circuit on coarse cells. Its type stages give the required DAG. The universal
coordinate proof therefore applies, with finite constants depending on this
supplied circuit. The full DK physical coordinate roster has not yet been
instantiated by the finite geometry runner; its tested graphs are smaller
three-axis DAGs. This distinction must stay explicit unless that additional
certificate is built.

Combining this construction with the preceding Gaussian conditioning proof gives a
conditional local permanent likelihood protocol for the supplied source,
with a proper-prior perturbation and explicit positive-window accuracy and
acceptance costs. It does not reproduce the earlier native Record-star
experiment or derive its local formation weights, and it does not turn the
source determinant into an unconditioned physical Born law.

## A local Hodge estimate that survives pinning and the fold

Restrict to the released helper's cubic-plaquette construction on an even
spatial width and a temporal cover length divisible by four. The latter
ensures that translation by the half-cover preserves the selected 2x2
differential tiling, including nonzero temporal coefficient. The actual
T_cover=12 fixture and the T_cover=16 challenge satisfy this condition.
An explicit out-of-domain T_cover=10, width-four, nonzero temporal-coefficient
probe has sixteen nonzero entries in Kq+Kq*: the half-tiling condition is
substantive, not a cosmetic restriction on the parameter list.

Supply volumes v in [5/6,13/6] and shears |s|<=3/5, with the source's local
plaquette Hodge entries

    nu=v,    mu=1/v,    a=v/(1-s^2),    b=-vs/(1-s^2).

Each plaquette contributes one quarter of diag(nu,[[a,b],[b,a]],mu).
Each lattice scalar occupies each of the four plaquette positions once.
Using 2|xy|<=|x|^2+|y|^2 in each off-diagonal pair, its lower row margin
is bounded by

    gamma=(5/6+6/13+2(5/6)/(1+3/5))/4=243/416 > 1/2.

The upper absolute row sum is at most

    Gamma=(13/6+6/5+2(13/6)/(1-3/5))/4=71/20.

The source pin replaces the odd block by v I, so it respects these same
bounds. Antiperiodic folding is restriction to the half-translation's minus
subspace under the normalized isometry x -> (-x,x)/sqrt(2). The Hodge and
selected differential commute with that half-translation in the stated
domain, so its quotient is the corresponding compression. Consequently

    gamma I <= Hq <= Gamma I

on every such cover. Possible edge identifications or cancellations at small
covers reduce the absolute off-diagonal row sum and do not invalidate the
quadratic form bounds. The argument is local; no size fit is involved.

The connection Kq=i(Hd+d*H) after restriction is anti-Hermitian. Thus
q=m Hq+Kq, m>0, has Hermitian part S=mHq and

    Re(x*q x)>=m gamma ||x||^2,
    ||q^-1||<=1/(m gamma).

For c=m/2 or m/3, the source signed-edge Gram factor exists on the full
union edge roster. Its onsite residuals obey

    S_ii-c-sum_(j!=i)|S_ij| >= m gamma-c > 0.

Columns for edges absent from a particular arm are simply zero. Hence
BB*=S-cI exactly throughout this disclosed family. Source selection and
matching an arbitrary-cover physical program are separate research tasks.

## Uniform coercivity of the joint likelihood precision

The joint target covariance is

    C0=[[W,D],[D*,I]],   W=Re(q^-1),   D=q^-1 B.

It satisfies W-DD*=c q^-1 q^-*>0 and ||W||<=1/(m gamma). Therefore

    (x,y)*C0(x,y)
       <= (sqrt(||W||)||x||+||y||)^2
       <= (1+1/(m gamma)) (||x||^2+||y||^2).

This proves the dimension-independent lower bound

    Q0 >= [m gamma/(1+m gamma)] I.

At m=1 the bound is 243/659, much stronger than the finite trace bound used
in the first likelihood probe. It applies to both c choices and every arm
in the stated Hodge range. It degenerates as m->0, and is not a massless
phase estimate. The direct full-matrix checks use varied cover, width, shear
sign and mass, and independently compare C0 with the action precision.

## Determinant comparisons should cancel common bulk factors

For positive Q_j>=m0 I, define the finite-alpha logarithmic tilt

    g_j(alpha)=log det(Q_j+alpha I)-log det Q_j.

The derivative formula and resolvent identity give

    g_j(alpha)-g_k(alpha)
      = integral_0^alpha Tr[(Q_j+tI)^-1-(Q_k+tI)^-1] dt.

If Delta=Q_j-Q_k has rank at most r and norm at most delta, then

    |g_j-g_k| <= r delta alpha/[m0(m0+alpha)].

Indeed the inverse difference has rank at most r and norm at most
delta/(m0+t)^2; integrate its trace bound. This is uniform in dimension
when the perturbation rank, size and m0 bounds are uniform. The input
localized-perturbation hypotheses must be checked for a chosen source family;
the current finite runner does not certify them for arbitrary DK covers.

For exact finite arm tilts t_j=exp(-g_j) in [a,b], normalized reweighting
of any prior menu w has the sharp universal bound

    TV(w_j t_j/E_w t,w_j) <= (sqrt(b)-sqrt(a))/(sqrt(b)+sqrt(a))
                         = tanh(log(b/a)/4).

If a=b the weights are identical and the bound is zero. Otherwise,
to prove it, put mu=E_w t. Convexity bounds E|t-mu| by the chord joining
its values at a,b. Dividing by 2mu gives
(b-mu)(mu-a)/(mu(b-a)), whose maximum occurs at mu=sqrt(ab).
This proves the bound for every menu, without knowing the detailed prior.
It is attained by a two-point endpoint distribution with that mean.

Combining with the preceding local resolvent bound gives

    TV <= tanh(r delta alpha/[4m0(m0+alpha)])

when all pairwise perturbations meet the stated r,delta bounds. This avoids
bounding each extensive determinant separately. It is a conditional stability
estimate, not a determinant-selection principle.

The primary likelihood calculation uses its exact rational determinant ratios to
calculate a,b and this tighter bound for the actual four-arm menus. It does
not infer a volume-uniform numerical bound from those finite ratios.


## Finite evidence and verification boundaries

The primary runner is
`scripts/permanent_local_gaussian_likelihood_protocol_2026_09_14.py`.
Its canonical evidence is
`logs/runner-cache/permanent_local_gaussian_likelihood_protocol_2026_09_14.txt`.
It declares a 180-second envelope. Assertions fail by nonzero exit; finite
checks challenge the accompanying arguments and do not confer retained status.

| Family checked | Actual finite content |
|---|---|
| Cubic causal geometry | Three-axis and negative-displacement degree-three DAGs on 4^3 coarse cells; a doubled 8x4x4 cover checks the same local role map |
| Matrix rule | Twelve roles, all 24 proper-cubic frames, 576 star-action compositions and 192 causal schedules of a four-root/four-observation program |
| Positive windows | Exact two-complex-variable disk acceptance probabilities, independent real/complex KL normalization and attainment of the sharp tilt bound |
| Supplied DK likelihood | Width four, temporal cover twelve, xgraded background, mass one, four Record values, c=1/2 and 1/3; exact common 768-node/848-edge circuit and exact determinants at alpha=1/10 and 1/100 |
| Source coercivity | Temporal covers twelve and sixteen, widths four and eight, masses 1/10, one and seven, positive and negative shears; direct full-cover compression and independent joint covariance/precision comparisons |

For the three-axis base geometry, 272 transverse crossings are removed from
192 wires; the final graph has 1,302,016 internal copy sites and maximum wire
length 9,868. The negative-displacement case removes 144 crossings and has
1,859,584 internal copy sites and maximum length 16,364. The doubled first
case has 2,604,032 internal copy sites and the same maximum path length.
These are large but fixed resources per coarse cell. Exact segment geometry
represents every integer copy vertex without allocating one matrix per site.

The single local-rule example uses one of 96 default control atoms at each
of four separated control sites. Its specified coherent program probability
is 1/84,934,656, before the later observation-window selection. This is a
finite illustrative cost, not a universal rate for all source programs.

The two scientific input paths are
[released finite source helper](../scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py)
and the
[current EX/ET matrix supplier](../scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py).
Their respective SHA256 values are
`8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2`
and
`5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445`.
The used supplier content is the displayed EX/ET matrices and shift lifts.
Historical parent-note status fields and historical runners are not executed
as evidence for this theorem. The envelope binds both declared inputs and
the primary source bytes. There are no ignored-file scientific dependencies.

The mathematical conclusion is the supplied posterior protocol and its
cost bounds. The premise table and scope above retain the distinct physical
research questions. Independent mathematical review remains pending.

## Author review record

The full changed argument and primary runner were personally read against the
current source helper, used matrix definitions and current axiom wording.
The hypotheses include degree at most four, a common type stage order,
compatible coarse periods, positive alpha and noise, and the even-half-cover
condition in the uniform source theorem. The full DK coordinate roster and
original native Record-star experiment remain outside the finite certificate.

The canonical primary run exited zero in 31.463 seconds under its declared
180-second envelope. Twelve deliberate source faults each produced an
AssertionError: an axis-only detour, shared terminal direction, reused edge
planes, lost imaginary payload, transposed star action, wrong observation
sign, unnormalized control atoms, wrong real/complex KL factor, wrong
likelihood cross sign, arm-dependent circuit roster, wrong antiperiodic
compression and an overstrong precision lower bound. The frozen primary
SHA256 is `8c309572e83ef500171c44d93ed6dc992daf034b881b199f054239613e369482`.
These are author fault checks, not independent mathematical review.

Distinct checks use unit-point versus interval geometry, acyclic innovation
recursion versus observed matrix records, exact disk integrals and real
Gaussian KL, exact Schur determinants versus full joint covariance, and
full-cover compression versus the supplied quotient. No theorem is inferred
from a count of successful checks. No helper-runner registry change is
required: all checks are in the primary, with two declared current inputs.
Independent source review, full validation on the integrated landing tree,
and any later formal audit remain pending. This author run supplies no audit
verdict or retained status.
