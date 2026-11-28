# The frozen-preserving bump needed by the excess comparison

Author: openai/gpt-6-astra/max mac-mini-codex. Source pinned at
`105283f2c2a5a306a2aff46a47dfadb7a3b6ef0e`.
Author analysis, not an independent check or audit. No numerical run.
This specifies the missing nonlinear input; it does not prove it.
Credit: the descent/lift/bump order is (f') in
`relative-density-bound.md:279`; RF and F-D are the repository's
relative-fill and fibre-inverse proposals. No paper lemma is used.

## 1. Exact constraints and the allowed variation space

**Discharged (necessary tangent equations).** Work at the REGULAR
minimal chain after descent and before the parent-restoring bump,
c_*=(U_0^*,...,U_{i-1}^*), with all retained maps M_j on their smooth
regular branches. This qualification matters: differentiating through
a change of exclusion/label branch is not allowed here. Let F_j be
the union of the frozen links at level j from ALL previous ages.
Write a right-trivialized variation as U_j(t)=U_j^* exp(t H_j+o(t)).
Differentiating exact preservation of frozen links and the chain gives

    H_j(b)=0                    (b in F_j),
    D M_j(U_j^*) H_j = H_{j+1}  (0<=j<i-1).              (TAN)

Use the fixed rooted gauge slice, with gauge transformations equal
to the identity on frozen sites. One can instead quotient the
allowed gauge directions; either convention must be kept throughout.
Denote this linear space by H_d, and let

    q_d H := D M_{i-1}(U_{i-1}^*) H_{i-1}.

A linear parent correction must lie in the range of q_d on H_d and
vanish on frozen level-i links and on parent entries required unchanged.
Let S_d be the intersection of that range with this required top
subspace. It includes any further compatibility relations of the range.
Merely vanishing on the frozen top links does not prove membership in S_d.
On fully frozen fine plaquettes every allowed variation has zero
action derivative, to every order.

**Gap (LI-d).** For the mismatches produced by the proposed fill,
prove compatibility and a local right inverse R_d:S_d->H_d with

    q_d R_d s=s,
    ||d_{U_0^*}(R_d s)_0||_2^2 <= C_b sum_B |s_B|^2,    (LI-d)

and the localized/weighted version of this inequality, with bounded
overlap over parent blocks B. Here s_B is the finite vector of parent
link angles assigned to B; double counting is bounded by dimension.
The norm on the left is fine action scale. In four dimensions the
right side is scale invariant, as the consumer requires. Gauge/graph
norm terms needed to make this an actual inverse must also be bounded.

A whole-chain tuple is used because setting H_0=0 on frozen fine
links alone does not preserve frozen data at coarser levels. Likewise
exponentiating a vector satisfying TAN preserves fine fixed links,
but does NOT by itself solve the nonlinear coarser constraints.

## 2. Exact nonlinear statement and energy cost

**Gap (R3-d/BUMP-d, the named stopping point).** Uniformly at the
actual minimal lift with data, construct an exact frozen-data chart
Phi_d(v), with Phi_d(0)=c_*, differential R_d, remaining on regular
branches and preserving all frozen links and all retained lower
chain constraints. Coordinates v are the compatible parent variables.
In local coordinates on that compatible parent manifold set

    N_d(v) = parent(Phi_d(v)) - parent(c_*) - v.

The coordinate difference here is a principal Lie-algebra log in the
fixed rooted frames, not subtraction of group elements. In parent-block
units fix a rate rho_b>0 and use the local norm

    ||v||_Y = sup_B (sum_{B'} exp[-2 rho_b dist(B,B')]
                                       |v_{B'}|^2)^(1/2).

Unlike a global l^2 ball of fixed radius, this permits many small
corrections throughout a large volume. For the needed mismatch ball,
prove

    ||N_d(v)-N_d(w)||_Y <= (1/2)||v-w||_Y,                (NL-d)

and, for the solution with parent mismatch s,

    A(U_s)-A(U_0^*)
       <= C_b sum_B [sqrt(E_B^mov(U_0^*)) |s_B|+|s_B|^2]. (COST-d)

E_B^mov sums action only on P_mov of the companion excess note,
with a fixed exponentially decaying neighborhood weight around B.
The weights must have a uniform column sum and include every
plaquette the correction changes. No frozen fine action appears
as a credit or as curvature that could be removed. All constants,
the regular chart radius and the rate must be uniform in L, x,
depth, volume and age history, after the fixed absolute thresholds
are chosen. It is enough to prove these estimates on the actual
small-mismatch family produced by descent, but that family and its
compatibility must be verified.

If the parent compatibility set is not already an affine space,
the chart on it must be built too; a linear tangent range does not
supply that chart. NL-d is an explicit quantitative nonlinear
obligation, not the assertion that finite-dimensional differentiability
has some unspecified neighborhood.

**Implication (nonlinear solve, given the stated chart/estimates).**
Assume N_d(0)=0, NL-d on ||v||_Y<=r, and ||s||_Y<=r/2. Iterating
v_{n+1}=s-N_d(v_n), starting at v_0=0, stays in that ball since
||s-N_d(v)||_Y<=r/2+||v||_Y/2. Consecutive differences decrease by a
factor 1/2, so the finite-dimensional complete space gives a limit
v=s-N_d(v), ||v||_Y<=2||s||_Y. This solves the EXACT parent equation
while Phi_d keeps the frozen data exactly. Uniqueness in the ball
follows from the same contraction. COST-d is an additional energy
estimate; it does not follow from convergence of this iteration.

**Gap (QT-d, needed before using that cost).** The trial/target must
also have small MOVABLE action on each sparse descent cube Q_r:

    E_Qr^mov(U_target^d)
       <= C_Q T^2[eps_q^2+b_2^2(r/L)^4],  r<=r_*,       (QT-d)
    C_f C_Q[eps_q^2+b_2^2(r_*/L)^4] <= kappa/4.

The support must be the one that is actually changed, and the target
must obey the parents and every frozen datum. This cannot be a bound
on all fine action beneath a frozen coarse cell: the locked-action
example disproves that version. C_Q,r_* and C_f must be absolute
(b_2 fixed), before L and the small thresholds are selected in the
allowed order. This small target estimate does not itself pay R;
the relative transport/allocation RT is still needed.

Here r_* denotes the absolute sparse radius r_{I_*} of Prop 10,
not any later fill radius that grows like T^(-1/2). Substituting
a T-dependent radius requires rechecking the displayed smallness
condition; it cannot inherit the absolute-radius argument.

**Implication (the sparse cost if all hypotheses hold).** If
E_B^mov<=C K T^2 and |s_B|<=C sqrt(K) T sqrt(f_B), COST-d is at most

    C' K T^2 sum_B [sqrt(f_B)+f_B].                       (SC)

For 0<=f_B<=1, this is at most 2 C' K T^2 sum_B sqrt(f_B).
At a sparse single fill, f_B<=C(r_*/L)^3, giving the source's
O(K T^2(r_*/L)^(3/2)) cost. Choosing L large can make this less
than a specified fraction, e.g. kappa T^2/16, of a cell's descent
gain. After MANY fills, f_B must be the actual aggregate affected
fraction and s_B the total mismatch. One also needs bounded charging
of these terms to descent gains, not an unproved linear addition of
different corrections' squared norms. Dense blocks have their own
O(T^2) cost and K reserve, as in the source. This is conditional
arithmetic, not verification of those estimates for frozen data.

## 3. Why RF and F-D do not close this step

**Discharged (source scope).** RF's displayed conclusion preserves
outer/inner fields up to a gauge and permits a parent mismatch.
It does not assert exact preservation of ALL frozen links on the
band, or supply a correction in H_d. Overwriting a frozen link
after gluing changes neighboring plaquettes and parent constraints;
its cost and compatibility require a new estimate. A usable
RF-d must provide an exactly frozen-preserving glued field and a
mismatch to which LI-d/NL-d/COST-d apply (or solve them jointly).

F-D supplies a graph-norm saddle inverse at a background satisfying
its curvature/coercivity hypotheses. Its displayed parent/frozen
constraint structure and nest weights are linear. It does not
establish Phi_d, NL-d, COST-d, QT-d, or the required R3 regularity
at the actual minimizer with quiet data. The source itself says
R3 with data at the final bump is 'Not written'. In particular a
graph norm cannot simply be renamed the L^4/H^2 control used by
the bulk R3 and composite-map argument. That uniform nonlinear
regularity is the missing bridge.

**Gap (two-age junctions).** F_j must be the UNION of both ages
before taking a variation. A correction keeping the newer brick
but moving an older one is inadmissible. A uniform proof must give
the above inverse, chart, movable target and aggregate mismatch
cost on a cube meeting both ages, with one constant, not a product
of constants per age. At different levels it must additionally
respect the different block scales in TAN. The companion cube
lemma bounds near propagation at ONE level conditional on Resp;
it supplies neither this inverse nor a sum of different-level
responses. Same-level ages do not change the union's geometry,
but they do change the nonlinear data whose uniformity is required.

## 4. Honest stop

**Gap.** No RF-d, LI-d/NL-d/COST-d or QT-d proof for these data has
been derived here. The replacement AE also lacks the relative
transport inequality RT. Consequently W2 and the DM energy branches
are not established. The elementary tangent equations and conditional
contraction/cost arithmetic above identify precisely what the bump
would have to do. They do not promote the existing linear inverse
to a nonlinear theorem. No numerical computation was needed or run.
