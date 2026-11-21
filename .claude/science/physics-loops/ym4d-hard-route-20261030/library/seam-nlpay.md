State of attack
===============

**gap — (NL-pay) remains undecided.** The proposed inference
"class at every level implies small total fine energy on each
top-unit cube" is false. Sections 4–5 give a hand reconstruction of
the mapped locked-pair example: arbitrarily many quiet, individually
small copies fit under one top cube, have identity parents, and are an
exact minimizer when their fine links are frozen. Every admissible
target has the same locked action. This invalidates that small-energy
application; it does not refute (NL-pay) for its specified, unfrozen
terminal-parent minimizer and trial.

**gap — first unresolved relative step, even granting Lemma U.** Local
single-field gauges give the desired critical estimate on one patch.
Combining them requires control of the covariant transition-gauge term
in (PATCH) below. An estimate based only on gradients on a disconnected
overlap is false, even for identity fields. Coordinated gauges might
avoid that example; no such construction is proved here. Lemma U itself
is recorded as an unchecked source theorem, used only in a conditional
calculation. No global relative alignment or nonlinear constants are
certified.

**discharged — task and source checkpoint.** HEAD is
`b79f4cb0c03a0256319a2a287b7ca9557a78c40e`. This is a written research
test by OpenAI Codex, not an audit or an independent model check. The
session exposes no exact model/effort receipt. The initial tracked
working tree was clean. Only this note is an authorized output; no
numerical job or subagent has been started.

**discharged — criteria, recorded before further derivation.** Read the
local estimate at its actual scale; identify whether its field is the
relative field of (ALIGN); test common gauges and the fixed parent; then
test the cube-energy hypothesis against the class and locked data. A
failure of a sufficient estimate is not a counterexample to (NL-pay).
Only if these checks succeed may the argument continue to parent
restoration, intermediate class preservation and (RATE-exact), with
the rate chosen before L. Stop at the first exact failed payment or
unproved inequality, while completing the requested locked-data and
clearance diagnostics.

**discharged — checkpoint and scope.** The proposed local payment and
the two diagnostics below are written and the source/scope checks are
complete. No parent restoration is attempted after
these failures of the proposed inference. The Sobolev source named by
Lemma U is identified there as belonging to the other attempt; its proof
has not been opened or imported. No statement below rests on numerics.

## 1. What the local theorem says, and which scaling it uses

**discharged — definitions and scaling.** Write B=L^n, n>=1, and
eta=B^-1 in top units. For a box Q of fine side N comparable to B put

    E_X(Q) = sum_(p in Q) |theta_X(p)|^2,
    E(Q) = E_U(Q)+E_T(Q),
    a_X(p) = 1-cos |theta_X(p)|.

Here theta is a principal plaquette logarithm, with length in [0,pi].
For a link logarithm h set H=h/eta; for the corresponding curvature
array set F=theta/eta^2. With lattice quadrature eta^4, exactly

    ||H||_(L^4(Q))^4 = sum_b |h_b|^4,
    ||F||_(L^2(Q))^2 = sum_p |theta_p|^2,
    ||H||_(L^2(Q))^2 = B^-2 sum_b |h_b|^2.              (SCALE)

These are definitions followed by cancellation of powers of eta,
not continuum limits. In particular the curvature energy in the
critical estimate is a sum, not its average over B^4 fine cells.
For 0<=t<=pi,

    2t^2/pi^2 <= 1-cos t <= t^2/2.                    (ANGLE)

Indeed 1-cos t=2sin^2(t/2); sin u<=u follows by integrating cos u<=1,
and sin u>=2u/pi on [0,pi/2] follows from concavity and the chord
joining its endpoints. Thus angle energy and Wilson energy differ
by fixed constants, never by a power of B.

**gap — exact target retained.** With
s_p(h)=sum_(b in boundary p)|h_b|, the requested estimate is

    sum_(p in S_0) [8B^-2 s_p(h)^2+2s_p(h)^4]
      <= C_rel(L) sum_p (K*1_(S_r(D)))(p)[a_U(p)+a_T(p)]. (NL-pay)

It asks for one alignment T^g=q.(exp(h)U), g=1 at top centres,
q supported on them, with T^g in the same terminal class-chain
fibre. The quantifiers range over every depth and volume, allowed
terminal V, its specified class minimizer U, the iterated trial T,
and required D. C_rel, the radius r in top units, and K's exponential
moment must be uniform in depth and volume; their L dependence must
be retained. The prescribed-fine-data diagnostic below is explicitly
distinguished from this terminal-parent problem.

**unchecked — the single-field statement exists, with the right
uniformity.** Lemma U of `lattice-uhlenbeck.md` states that there are
absolute epsilon_0,C_U>0 such that E_X(Q)<=epsilon_0^2 implies a gauge
alpha_X on Q with X^alpha_X=exp(a_X^loc) and

    ||a_X^loc||_4 + N^-1 ||a_X^loc||_2
                         <= C_U sqrt(E_X(Q)).          (U-local)

Its norms are unweighted lattice sums. Its claimed constants are
independent of N, hence of depth. Its proof uses a reflected-box
Sobolev inequality, a nonlinear gauge flow and a layer extension.
The only Sobolev file located by name is
`lattice_sobolev_box_gauge.md`; Lemma U explicitly attributes that
proof to the other attempt. I have not read it. I do not independently
certify the Sobolev input, the flow or the layer construction here.
Their source label "proved" is not a discharge in this report.

**implication — scope of the following test.** Grant (U-local) with
absolute constants. The next two sections derive exactly what it
would pay and exactly what it leaves to patch. The locked-data test
in Section 4 does not assume (U-local) at all. Thus failure of its
smallness premise remains a useful test even if the single-field
theorem is subsequently proved in full on this side.

## 2. One patch: the relative field and the actual conditional payment

**implication — a relative field on one patch, given (U-local).**
Let alpha and beta be the gauges of U and T, and write
U^alpha=exp(a), T^beta=exp(b). Put r_Q=alpha^-1 beta pointwise.
For a bond xy, direct multiplication gives

    T^(r_Q)_xy U_xy^-1
       = alpha(x)^-1 exp(b_xy) exp(-a_xy) alpha(x).

Choose h_Q to be a principal logarithm of this matrix. Thus h_Q is
an actual relative link logarithm, not either endpoint's potential
and not the linear difference of curvatures.

For Z in SU(2), |I-Z|_F=2sin(|log Z|/2), in the normalized Frobenius
norm of `seam-nonlinear.md`. By (ANGLE),
|log Z|<=(pi/2)|I-Z|_F. Integration of the derivative of exp(ta),
whose norm is |a|, gives |exp(a)-I|_F<=|a|. The triangle inequality
and unitary invariance therefore give

    |h_Q(bond)| <= (pi/2)(|a(bond)|+|b(bond)|).

Apply the triangle inequality in l^2 and l^4, then
sqrt(E_U)+sqrt(E_T)<=sqrt(2E). With C_h=pi C_U,

    ||h_Q||_4 <= C_h sqrt(E(Q)),
    N^-1 ||h_Q||_2 <= C_h sqrt(E(Q)).                  (LOCAL-REL)

The letter b in exp(b) denotes the second endpoint's logarithm;
the argument of h_Q in these estimates denotes a bond.

**discharged — parent-centre values can be split off algebraically.**
Suppose a *single* relative gauge r has already been constructed on
the required region, with T^r=exp(h)U. Let C be the set of top
centres, put q(c)=r(c)^-1 for c in C and q=1 elsewhere, and put
g=q r. Then g(c)=1 and

    T^g = q . (exp(h)U).                              (ROOT)

This is exactly the algebra of (ALIGN). It makes no logarithmic
estimate for q, and creates no extra h. If the deterministic block
map is gauge covariant with induced gauge given by restriction to
centres, its iterates give M_n(T^g)=V; each intermediate field is
gauge transformed and its plaquette angles are unchanged. That last
application is an implication of the stated covariance, not a new
proof of the map or of any interpolated field's class membership.
The identity (ROOT) by itself neither constructs r nor respects
additional prescribed fine links.

**implication — the proposed sum really would pay the seed, given
one coherent h.** Suppose a cover of the shell bonds by boxes Q has
plaquette overlap multiplicity at most m, N<=cB, and one h obeys (LOCAL-REL)
on every box, with max_Q E(Q)<=epsilon<=epsilon_0^2. A bond in four
dimensions lies in six unoriented plaquettes. For four nonnegative
numbers, Cauchy–Schwarz gives (sum x)^2<=4sum x^2, and applying it
twice gives (sum x)^4<=64sum x^4. Consequently

    sum_(p in S_0) s_p(h)^2 <= 24 sum_shell-bonds |h|^2,
    sum_(p in S_0) s_p(h)^4 <=384 sum_shell-bonds |h|^4.

Bounding a sum over the union by the sum over boxes now gives

    sum_(p in S_0) [8B^-2 s_p^2+2s_p^4]
      <= [192 c^2 C_h^2+768 C_h^4 epsilon] sum_Q E(Q)
      <= m[192 c^2 C_h^2+768 C_h^4 epsilon]
                                  sum_(union Q) (|theta_U|^2+|theta_T|^2).
                                                               (PAY-local)

The quartic step is exactly E(Q)^2<=epsilon E(Q). Using (ANGLE),
the corresponding Wilson coefficient is

    C_pay = (pi^2/2)m[192 c^2 C_h^2+768 C_h^4 epsilon].

If the union of boxes lies in S_r(D), this conditional estimate has
K=delta_0. It would be depth independent, and also L independent if
c,m,C_U,epsilon were. It is not a certificate for the actual seam:
the hypotheses of a common h and small E(Q) are still to be met.
Only the quartic contribution becomes small with epsilon; the
quadratic cutoff contribution does not.

## 3. The first relative term not supplied by local gauges

**discharged — the transition term is covariant.** On a new patch
let r_Q give h_Q as above. On its overlap O with the already treated
region let the existing gauge be r_old. To agree on O, a correction
v on Q must satisfy v|_O=r_old r_Q^-1, and the extended relative
gauge would be r'=v r_Q. Define

    D_U v(xy) := |log(v(x) U_xy v(y)^-1 U_xy^-1)|.

The product defining its new relative field is exactly

    T^(r')_xy U_xy^-1
      = [v(x) exp(h_Q(xy)) v(x)^-1]
                            [v(x) U_xy v(y)^-1 U_xy^-1].

The preceding chord estimate therefore bounds its principal log by
(pi/2)(|h_Q|+D_U v). For example its fourth power is at most
8(pi/2)^4(|h_Q|^4+|D_U v|^4), since (x+y)^4<=8(x^4+y^4).
Thus the new term is the fourth power of D_U v, along with its
B^-2 second moment. No curvature bound for either endpoint has
estimated this extension term.

**gap — the precise unproved patch payment.** For the transition
data actually produced by a coordinated construction, one would need
an extension, respecting the required agreement and any fixed-link
conditions, for which

    B^-1 ||D_U v||_(2,Q) + ||D_U v||_(4,Q)
          <= C_ext sqrt(E_U(Q^+)+E_T(Q^+)),
    v|_O = r_old r_Q^-1.                              (PATCH)

Here Q^+ must be an enlargement by a fixed number of top units;
C_ext and the number of patching stages must be uniform in depth,
and their L dependence must be exhibited. This is the first missing
*relative* estimate after granting (U-local). It is one specific
term in the proposed construction, not a list of replacement lemmas
or a claim that all proofs of (NL-pay) must use this construction.

**discharged — arbitrary choices of local gauges do not satisfy
(PATCH), even at zero energy.** Take a connected lattice cube Q,
U=T=1, and two disjoint nonempty subcubes O_1,O_2 as overlap. On
O_1 let r_old=1 and on O_2 let r_old=-1; choose r_Q=1. These are
legitimate local gauges of the identity field, with zero local
potentials, and all parents of the endpoint fields are identity.
Both overlap components have D_U(r_old r_Q^-1)=0. But (PATCH)
would have zero right side, forcing D_U v=0 on every bond of Q.
For U=1 this says v(x)=v(y) on each edge. Following a path between
any two sites of connected Q makes v constant, contradicting its
prescribed values 1 and -1 on O_1 and O_2.

This refutes patching based solely on the local norm estimates and
arbitrary overlap choices. It does not refute coordinated choices:
for these same identity endpoints, choosing r_Q=r_old=1 everywhere
works. Parent information or a coordinated normalization must do
actual work to remove this freedom; the example supplies no lower
bound on the best alignment's cost.

**unchecked — the existing RF claim is not (PATCH).** Lemma RF of
`lattice-uhlenbeck.md` assumes small energy on each cube of four
blocks and treats one-level parents. Its claimed output is an
interpolated field, with an explicitly allowed parent mismatch s;
its inner match is only up to a site gauge. Its Steps 2–4 assert
control of overlap constants and extensions. They do not constitute
a checked construction here for the composite parent M_n, one
relative h on S_0, or exact prescribed fine links. Nor does a fixed
number of colours at one level justify a constant iterated n times.
No RF constants are promoted to nonlinear A_s,r or M_*.

## 4. The class-to-small-energy inference fails by hand

**discharged — an identity-parent pair, reconstructed from
`paid-inputs-frozen-energy.md`.** Fix odd L>=5. Inside a parent block
centred at z, set every link to 1 except the two direction-1 links
starting at z+(0,1,0,0) and z+(0,-1,0,0). Set their values to
exp(aZ),exp(-aZ), respectively, with Z=diag(i,-i) and
0<a<min(T_class/8,pi/16). T_class here is the fine class threshold,
not the trial field T. The two links share no plaquette. A link has
two incident plaquettes in each of the other three directions, so
exactly twelve plaquettes have angle a. Hence

    E_pair=12a^2,       A_pair=e(a)=12(1-cos a)>0.       (PAIR)

All matrices commute. For the deterministic all-lines average on
these small abelian fields, its group products and principal logs
give the exact linear formula

    QH=Q_path H+Phi(y)-Phi(y'),

where Phi is the average contour integral rooted at the block
centre (mapped Text 3.1). A direction-1 line at transverse coordinate
z_2+1 is paired with the reflected line at z_2-1. Their weights are
equal, longitudinal coordinates identical, and link angles opposite.
Thus Q_path H=0; in the other directions H is zero. Reflection in
x_2=z_2 also pairs the rooted axial contours, retaining their axial
order and reversing the sign of every nonzero contribution. Thus
Phi(z)=0. Other blocks contain no nonidentity link, so their Phi
vanishes. Every parent is therefore exactly 1.

Place copies in separated parent blocks, at most one per frozen
brick below. Each parent path reads at most two such blocks, so its
angle has absolute value at most 4a<pi. There is no branch reduction;
the same cancellations hold for the sum of copies. All labels vanish
because every fine flux is below T_class, and all higher fields are
identity. This uses the all-lines, reflection-symmetric contour
average specified by the mapped construction, not an arbitrary
blocking map.

**discharged — frozen copies are quiet constrained minimizers.**
Put each copy strictly inside a different fine brick of side t_0,
with all twelve plaquettes away from its boundary; t_0>=8L leaves
room. Freeze all bonds with both endpoints in the frozen layers.
Choose a still smaller, if necessary, so that

    m_D a^2 <= eps_q^2 T_class^2,

where m_D is the fixed finite cell-incidence multiplicity times
twelve in Dev. Such an a>0 exists, independent of depth and the
number of bricks. For identity parents the unfrozen local reference
can be identity and has zero action, the minimum by nonnegativity.
When older copies are already frozen, retain them and put identity
on the new brick. This again minimizes the remaining nonnegative
action; the older frozen terms cancel in Dev. The new copy's Dev is
m_D a^2. This verifies relative quiet at each freeze. The brick
faces have identity data, so closed-face flux tests are satisfied.

Let W be the field of M copies and identity elsewhere, with its
identity chain above level zero. Every nonzero plaquette is wholly
frozen. Every field with these data has those same M e(a) units of
action, while all other action terms are nonnegative. W makes all
the latter zero. Thus, for this exact constrained problem,

    A(W)=a_d(1)=M e(a).                                (LOCK)

No uniqueness, regularity or general minimizer theorem is used.
Every admissible target with the same d, whether or not minimizing,
also has at least this locked action on those plaquettes.

**discharged — enough copies fit in a top-unit cube.** Hold L,t_0,a
and all class/quiet thresholds fixed. A fine frozen layer has a row
of bricks of thickness t_0 and arbitrarily large extent in the three
tangential directions. In a top cube of side B=L^n with B>=8t_0,
discard a t_0 strip at both ends of each tangential interval. Each
remaining interval contains at least floor(B/(4t_0)) full brick
intervals: after those two discarded strips, at least
floor(B/t_0)-4 full intervals of any translated t_0 grid remain.
This is at least floor(B/(4t_0)) for B/t_0>=8. The definition of
the tiling in `fibre-propagator.md`, Lemma BG, is recursive: each
x_3 row carries a translated x_2-row tiling, and each such row a
translated x_1 interval tiling. Apply the same lower count at each
of these three stages; the shifts do not change it. If the normal row straddles
the top cube boundary, choose the side containing at least half
its thickness. That thickness is at least 4L, so an interior parent
block and the pair fit there. Thus the nonzero plaquettes of at
least

    M_n=floor(B/(4t_0))^3

disjoint copies fit inside one top cube (or its allowed fixed
enlargement). Its angle energy is at least 12a^2 M_n and its Wilson
energy is at least e(a)M_n. Both tend to infinity with n. In
particular they exceed any fixed Uhlenbeck threshold. All levels
remain class; every parent from level one onward is identity.
Shrinking a positive T_class after L, but before depth, does not
change this conclusion.

**discharged — what this refutes, and which endpoint it does not
describe.** Class membership alone does not imply
max_Q E(Q)<=epsilon_0^2 in top units. With frozen data it can fail
even for an exact constrained minimizer, and an admissible T^d
inherits the same failure. In the literal terminal-parent problem
of `seam-nonlinear.md`, there are no separately frozen fine links.
At parent 1, identity is an admissible zero-action field; W with
M>0 is not its minimizer. The specified unconstrained trial of 1 is
also identity and would violate the nonidentity frozen bonds.
Consequently (LOCK) is not a counterexample using the specified
unfrozen U,T. Small top-cube energy for that particular U requires
an additional minimizing-field estimate, not the class test alone.

**implication — the trial's stronger flux bound would suffice for
its energy, but class alone does not.** The stated (TOP-tr) in
`parts/hard-core--excess.md` has
|theta_T(p)|<=C_7 B^-2 flux(V). If it holds, a box of fine side
N<=cB has at most 6(N+1)^4 plaquettes. Since B>=1,

    E_T(Q)<=6(c+1)^4 C_7^2 flux(V)^2.

This follows just by counting plaquettes and squaring that stronger
bound. (TOP-tr) is not rederived here, and no such pointwise
B^-2 bound has been established here for the actual minimizing U.
The distinction is between this extra smoothing estimate and a
fixed fine flux threshold, not between two normalizations of energy.

## 5. Frozen cubes, the seam and clearance

**implication — the packed row is compatible with the stated
nested-layer clearance.** Use the unshifted x_4 brick faces of the
mapped flat-slab geometry. For the upper exterior face E_j={x_4>=h_j},
choose its successive wall positions downward in

    L h_(j+1)-9t_0 <= h_j <= L h_(j+1)-8t_0.

An interval of length t_0 contains a brick wall. The outward shadow
of E_(j+1), enlarged by 3t_0 and by at most one brick for rounding,
lies in E_j. The extra exterior width is at most 10t_0, smaller
than R_B=(2/3)t_0 L for L>=61. These verify (N) and (B) at this flat
face; choose a sufficiently wide periodic slab to separate its two
faces and repeat with the opposite sign at the other face.

The frozen row lies between h_j-2t_0 and h_j, allowing a whole brick
of endpoint rounding, so its parent lies within 12t_0/L+2 of the
next wall, on the frozen side of the free region. Since t_0>=8L
and L>=61, this is less than t_0; it lies in Sigma_(j+1).
Free parents end no later than h_(j+1)-t_0, up to two parent cells
of rounding. Their shadow ends no later than
Lh_(j+1)-Lt_0+2L. The lower frozen row starts no earlier than
Lh_(j+1)-11t_0, giving clearance at least

    t_0(L-11)-2L >= t_0 L/2 > r_S L

for t_0>=8L and t_0>=4r_S. For the middle inequality, subtract
t_0 L/2: the remainder is t_0(L/2-11)-2L, which is positive
under these choices. These are purely geometric checks of the
source's stated slab/brick conventions. No energy theorem is used.
Increase the torus size with depth so the faces never meet.

The packed top cube is on the frozen side: parent containment puts
the lower frozen row under frozen higher cells. Clearance therefore
does not contradict the arbitrarily large energy there.

**discharged — identical frozen terms need no smallness for their
own replacement cost.** If every bond of a plaquette is prescribed
and X,U,T^d all retain it, then
a_X=a_U=a_T^d there. Its summand in R_D is exactly zero, on either
side of D, irrespective of how large the sum of such terms is. For
the particular equal endpoints U=T^d=W, take g=q=1 and h=0: the
left side of (NL-pay) is zero even on the heavy cube. Thus large
locked action does not by itself force a large relative field or
disprove (NL-pay).

**discharged — fixed links constrain gauges, not just energy.**
For a prescribed bond d_xy, preserving it under g means

    g(x)d_xy g(y)^-1=d_xy,
    equivalently g(y)=d_xy^-1 g(x)d_xy.

This follows by multiplying the equality on the left and right.
It ties together gauge values throughout each frozen component.
The independent choices of local gauges and the point-supported
factor q in (ROOT) do not automatically satisfy it. Mixed
plaquettes, with at least one movable bond, still enter the cost;
cancelling fully frozen plaquettes does not remove those terms.

**implication — what clearance permits, and what it does not
supply.** If a seam and all its gauge stencils are contained in an
R-neighbourhood of free level-j cells, (CL) of
`energy-by-stages.md` puts lower frozen layers at distance at least
t_0/6-R in level-j units. For R<t_0/6 this is positive. This is
the triangle inequality applied to the stated clearance, so avoiding
the packed *lower* frozen row is compatible with that geometry.
It does not control frozen bonds at level j itself.

The all-cubes application of (U-local) must therefore either avoid
heavy locked cubes in its analytic patches or replace total-energy
smallness by a proved estimate that cancels common frozen data.
Entire frozen cubes need not logically leave the physical seam:
identical fixed plaquettes already cancel. What has to leave this
particular Uhlenbeck argument is the unjustified use of their total
energy as a small quantity.

**gap — no admissible excision has been constructed.** (NL-pay)
asks for the required sets D, with all touched bonds and stencils
inside the enlarged shell. It does not state that each such shell
lies in the free-cell neighbourhood just described. Removing
frozen cubes changes that assertion and leaves mixed plaquettes to
handle. Clearance alone constructs neither a relative gauge
preserving those bonds nor an altered seam for every required D.
This is why restricting to free patches is not silently adopted as
a solution.

## 6. Stop, provenance and verification boundary

**unchecked — downstream construction.** There is no X_D in this
note, no proof that an interpolation has parent V, and no proof
that its intermediate images stay class. No nonlinear A_s,r,M_*
have been obtained. The downstream obligation remains

    2 A_s(L) M_*(L) sinh(nu r(L)) < 1,

with nu fixed before L. The conditional local C_pay is not A_s:
patching and parent-restoration costs have not been paid. The flat
constants from `seam-quadratic.md` cannot be substituted for them.

**discharged — read/write boundary.** Read GOAL and the required FINISH
sections, including
the no-computer-assisted-proof, independence and rules sections;
`seam-nonlinear.md`, `lattice-uhlenbeck.md` and
`paid-inputs-frozen-energy.md` in full. Targeted additional reads:
`seam-quadratic.md` Sections 3 and 6; `excess-seam.md` Sections 1–2;
`excess-shell-end.md`'s (GLUE-E) and definitions; the mapped Text
3.1, 5.1–5.2 and relevant map locators; the excess part's trial and
class statements in Sections 2.2–3; the setting, quiet test and
layer geometry of `quiet-boundary-rarity.md`; and Sections 1–2 of
`energy-by-stages.md`. The recursive tiling definition in
`fibre-propagator.md`, Lemma BG, was checked for the packing count;
its extension theorem is not used. Locator output is not proof verification;
unrelated source computations and claims were not used as evidence.
The absent sparse-worktree workflow was read via `git show HEAD`.
The physics-claim-reviewer skill was used for this bounded check;
its process cannot enlarge the task or confer scientific status.
No forbidden-side file or gate was opened. Only this file was
written; no script, numerical run, subagent, audit, commit, push or
post was made.

**discharged — source identities and mechanical verification.**
The principal input blobs at HEAD are

    seam-nonlinear.md          09be22675ea759ab9347ba8d2baa8a35e4301b16
    lattice-uhlenbeck.md       8b4c857ad942cc0924acb3e16df854164e064acb
    paid-inputs-frozen-energy.md
                              a1ff3b8fe1199ef333ae4154ffae855cdb9b4ff3
    energy-by-stages.md        055df383747332f293af1616da852b4a2b5368f2

HEAD remained at the pinned commit; comparison of the inspected
scientific inputs with HEAD showed no changes. Status showed only
this new note. The no-index whitespace check produced no diagnostics;
exit 1 denotes the new file's difference from `/dev/null`. These are
file checks, not mathematical or numerical verification. The complete
written argument was reread by this same author; there is no claim
of independent review.

**gap — verdict: the proposed class-to-small-cube-energy step fails
at (LOCK); (NL-pay) is undecided at the coherent relative-gauge
payment, concretely (PATCH) after granting (U-local).** The original
terminal-parent minimizing pair is not refuted. No constants are
certified for nonlinear (GLUE-E) or (RATE-exact).
