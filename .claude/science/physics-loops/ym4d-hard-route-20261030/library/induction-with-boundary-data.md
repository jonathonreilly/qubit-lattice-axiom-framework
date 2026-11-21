# Induction with boundary data and a marked stopping lemma

Source revision: `45b3989670a64c7d0ce7b293a56ed6beb37dee14`.
Author: Codex, configured model and effort unchanged, 2026-11-01.
Scope: the neutral consumer of queue item 10. No producer proof is transferred
between the attempts. This is author work, **unchecked** independently, not an
audit. The operating instructions were read from that revision's Git object
because the workflow file is absent from this sparse worktree.

**Status.** I(k;D) below is a **gap**, a proposed induction contract, not a
proved extension of I(k). The split-to-cross-ratio observation and Lemma
M22.2 are **implications** with proofs below. In particular M22.2 does not
prove its marked input (MR). RC-far is untouched.

## 1. The object and its domain

Fix one map and the geometry Theta of **The interface** in
[upper-chain.md](../parts/upper-chain.md). All constants below are fixed before
level, depth, volume, region and data. They may depend on Theta and on a
specified finite derivative order; none may depend on a selected boundary's
area or on the number of nested levels. Polynomial area factors are displayed.

Let D be finitely many nested inner/outer whole-brick layer families with
specified fields on links whose **both** endpoints lie in a layer, at every
level where that layer is frozen. Include the local auxiliary variables and
all coarser parent patches needed to read quiet. Crossing links with only one
endpoint frozen stay free. Fix a deterministic convention for assigning each
local factor wholly to one side or the intervening region. Require the factor
range and the lift-patch range to fit the clearance, including at corners and
junctions. The quiet predicate is the chosen map's predicate; in the mapped
case it is relative to previously frozen D in a fixed ordering. Do not
identify it with the independent absolute-flux predicate.

Admissible D means compatible constraints, positive finite reference masses,
and quiet data on the full patches required by the map. Whether all the data
combinations needed by a consumer are admissible is the separate (FILL)
obligation. This definition does not prove positivity, local lift stability,
or uniform constants at a junction.

Write Z_k^D(V) for the **unnormalized** integral of the original augmented WW
over levels 0,...,k-1 in the free region, with level-k field V and D held
fixed. Keep factors touching the free region, including boundary plaquettes
and auxiliary-choice weights. Factors assigned wholly to the inner or outer
retained side may be removed separately; a scalar depending on both sides
may not. The identity defining the next step is

    Z_(k+1)^D(W) = integral K_k^D(W; dV,dchi_k) Z_k^(D_<k)(V).       (BD0)

Here the delta constraints and any newly frozen level-k data are included
in K_k^D. This is an unnormalized restricted integral, not an assertion that
K_k^D has total mass one. The corresponding reverse probability kernel is
formed only after its actual denominator is known positive. A conditional
law given D is not thereby a member of LL.

At k=0 this is exactly the Wilson weight and local boundary factors. It
proves (BD0) at the base by its definition. It does **not** prove the analytic,
coercive, marked or cross-ratio parts of the following contract at the base.

## 2. Proposed I(k;D) [gap]

For every such D, every allowed free region R_k, and every real V satisfying
the constraints (arbitrary in the free interior), require the following
items, uniformly in the quantified domain. The original map's bulk
coefficients/trajectory are kept; new boundary terms are tracked explicitly.

**(BD1), exact representation and classical comparison.** Give an exact
identity

    Z_k^D(V) = exp[-x_k F_k^D(V) + B_k^D(V)] G_k^D(V),   G_k^D(V)>0.

Specify F as the actual constrained classical variational problem and its
local density, with competitors matching every frozen link and parent.
Specify the entire scalar normalization in B; setting a reference value to
one is not allowed to discard a mixed dependence on the two sides of D.
Prove the map's bulk classical lower/upper comparison and its relative excess
inequality on this region, with a boundary competitor and every rough-cell
charge stated. At a regular top this includes a regular constrained centre;
near quiet faces and their junctions this is an additional stability claim.
A signed polymer expansion for G is not a lower bound on its absolute sum.

**(BD2), chart and analytic norms.** On every region where the expansion is
used, construct the chart with B=0 on frozen links and the linearized block
constraint on the free links. State its actual norm/weights and prove a
coercivity lower bound c(Theta)>0 and propagator decay at the specified rates,
uniform in the number of finer frozen levels. A bulk coercivity bound is not
a proof on a nested domain. State the tube/coordinate radius and cut, keep
its Jacobian and normalization, and prove the anchored vertex bounds on that
same domain. For example, an acceptable analytic norm has the explicit form

    sup_v sum_(Y containing v) exp(kappa_A tree(Y))
        ||e_(k,Y)^D||_rho <= E_A(Theta),                         (BD2a)

with rho>0 and kappa_A>0 fixed, plus the same norm for the actual far-field,
region and boundary-data differences. A bound on values alone is not that
difference bound. Use the relevant map's variables: the independent chart
has local origin V^# and saddle coordinate b^*; the mapped chart has its
own data-dependent lift. No equality of these charts is asserted.

**(BD3), boundary terms.** Split bulk and boundary contributions in B and
in the analytic activities. Track a boundary norm b_k (using the same
specified anchored norm as BD2) and establish a closed bound, for example

    b_(k+1) <= C_bd L^3 exp(-delta r_S) b_k + C_src,
    C_bd L^3 exp(-delta r_S) <= 1/2.                            (BD3)

Then b_k<=b_0+2C_src by induction. This arithmetic is **discharged**, but the
transition estimate and its source norm are **gaps**. The classical O(x_k)
response stays in F_k^D exactly; it cannot be inserted into C_src. A term
constant per boundary cell does not disappear merely by passing one level.
The former consumer claim that this costs only a label is withdrawn.

**(BD4), floating rough sets and marks.** Give the exact positive integral
behind any gas decomposition, the rough-set upper budget, and the
no-mandatory-face conclusion from the proved boundary stability. All rough
interior configurations are integrated. Where a regular-top log-gas is used,
prove its convergent connected expansion with uniform data sensitivity; a
signed numerator bound divided by an uncontrolled signed denominator is not
acceptable. For a marked variant Z_k^(D;M), keep the *same unmarked*
normalizing mass, original mark events, support multiplicities, entropy and
own-level energy charges. State which mark sets are allowed. To apply the
marked lemma below one needs precisely (MR) for all its extra test sets in
the available corridor. For the full-history consumer, RAR^ch under mu,
including K, remains a separate required estimate; BD4 at a regular top does
not supply it by itself.

**(BD5), the boundary comparison read by MD*.** For every shell/four-tuple
in the interface, all four shapes included, the actual middle-region
representation must admit

    log Z* = -x_j F_cl + B_vac + sum_Y e_Y                  (BD5-id)

with absolute convergence of the displayed connected sum and all boundary
normalizations retained. For Delta_IO h=h(a,b)+h(a',b')-h(a,b')-h(a',b), a
sufficient component contract is

    |Delta_IO F_cl| <= C |A|^P exp(-c_t D),
    |Delta_IO B_vac| + sum_Y |Delta_IO e_Y|
        <= C x_j |A|^P [exp(-c_t D)
                         +(z_j^cut)^(1/2)exp(-c_s D)].        (BD5)

Omit the slow term on a single-tier map. These inequalities are **gaps**,
not consequences of the definition of I(k;D) or an unmarked bulk norm.
They identify exactly what must be proved for the classical response, the
vacuum normalization and the connected activities. Their constants/rates
have the interface's dependencies and all-level margins. A same-shape
interpolation alone does not cover a four-tuple with differing shapes.

**Implication to MD*.** Under BD5-id/BD5 and FILL, apply Delta_IO to the
identity. By absolute convergence it passes through the sum, and the triangle
inequality gives the MD* envelope (enlarging C once). Since Delta_IO log Z*
is exactly log CR(Z*), no division by a signed gas or integration of far rough
boundary data occurs in this step. This proves the implication only.

**(BD6), closure and base.** Prove every item at k=0 and prove
I(k;D) => I(k+1;D) for every admissible D at once, with the same constants and
the exact restriction (BD0). A stop may then select D by a retained-side
measurable rule. Selection does not prove any hypothesis uniformly in D.
At an intermediate level the parent may have floating rough regions even
when the terminal parent is globally regular; these cases cannot be omitted.

The independent attempt states no I(k;D) at this scope. Its private crossing
link integration is a possible part of BD0/FILL, not BD2–BD6. Mapped's I_k^D,
Prop MD*, DM+ and paid-reference proposals address portions of this list but
retain their named gaps (in particular stability, LNC, S and LMK/PAY).
This note introduces no proof from one attempt into the other's induction.

## 3. Lemma M22.2: keeping a mark factor against one denominator

**Statement [neutral implication].** Fix an admissible geometry, a joint
positive finite hierarchy measure Lambda, and an unmarked denominator
D_0=Lambda(1)>0. Fix a nonnegative measurable mark weight h_M and a number
A_M>0. For an event E write J_M(E)=Lambda(h_M 1_E)/D_0. Original mark
indicators are a special case; they are fixed before exploration.

Choose an available corridor in which the deterministic exploration and every
witness selection of Lemma 22.1 fit, including all descendant balls and parent
patches. For all 0<=l<=j and every finite set S of allowed level-l cells with
mutual distance >7w/3, assume

    J_M(all cells of S non-quiet) <=
        A_M exp(-8w_0 lambda_l |S|).                         (MR)

The empty set is included: J_M(1)<=A_M. The constants satisfy the two explicit
entropy inequalities of Lemma 22.2, lambda_(l-1)>=lambda_l, and L>=43.
Every set produced by its shortest-path/witness argument must be allowed.
This is a real additional input, including when Lambda has frozen data D.

Then, for any separated S of allowed level-l roots,

    J_M(all roots bad_l) <= A_M [2 exp(-4w_0 lambda_l)]^|S|,
    J_M(H^c) <= A_M C(Theta)|A| exp(-lambda_j D/10),
                                            D>=28w_0.       (M22.2)

Thus a prescribed mark factor A_M can be retained in a failure mass against
one original denominator, without dividing by J_M(1).

**Proof.** Define the positive subprobability measure nu_M(E)=J_M(E)/A_M;
MR with S empty gives total mass <=1. Cauchy-Schwarz is valid for a finite
positive measure, including a subprobability. Use exactly the deterministic
bad-cell implication of Lemma 22.1, with q=ceil(L/14)>=4 and at most
N=(81w^4L^4)^q choices of q separated children per propagated root. If p_l(n)
is the supremum of nu_M(all n roots bad_l), splitting roots into directly
non-quiet and propagated roots and taking a union bound gives

    p_l(n) <= sum_(n_0+n_1=n) binom(n,n_0)
        exp(-4w_0 lambda_l n_0)
        [N^n_1 p_(l-1)(q n_1)]^(1/2).

The case n_1=0 uses p_(l-1)(0)<=1, not equality of the total mass to one.
The base follows from MR. Put rho_l=2exp(-4w_0 lambda_l). Under the entropy
inequality 2w_0 lambda_l>=log(162w^4L^4),

    (81w^4L^4 rho_(l-1))^(q/2) <= exp(-4w_0 lambda_l).

The binomial sum is therefore <=rho_l^n. Distinct roots' descendant balls
produce mutually separated selected children by the clearance/separation
argument in the deterministic lemma; this is why all those sets were
required to lie in the allowed corridor.

For failure of either exploration take its shortest bad-root path, as in
Lemma 22.2. With h=floor(3D/(28w_0)), there are at most C(Theta)|A| starting
choices and (625w^4)^h successive choices, and at least h/2 separated roots.
Thus its nu_M mass is at most

    C(Theta)|A| [625w^4 sqrt(2) exp(-2w_0 lambda_j)]^h.

The second entropy inequality w_0 lambda_j>=6log(900w^4), followed by
(11/6)w_0(3D/(28w_0)-1)>=D/10 for D>=28w_0, bounds this by the stated
exponential. Sum the two sides, absorb the factor two into C, and multiply
by A_M. No independence between levels or conditional rarity was used. []

**What MR does not follow from [gap].** Unmarked RAR^1 alone does not prove
it: a mark can force a non-quiet cell. Nor may a forced cell already in M be
charged again as a new S mark. A sufficient application of a simultaneous
marked-mass bound is to take A_M equal to its product of original mark
weights and require every additional S to be disjoint from, and separated
at the required distance from, those original marks, so M union S is an
allowed mark set. The exploration and *all* descendants must remain in that
unmarked corridor. If a source bound has a nonadditive mark budget, establish
its bound on the union before removing the original factor. In the mapped
DM+ proposal this would use its final product bound, conditional on S/LMK,
at a regular top; it does not establish an analogous bound under mu.
An exploration that hits a forced mark or leaves the available corridor has
an additional event not estimated by this lemma. Conditioning on that
exploration cannot repair a missing MR.

This version deliberately pays Cauchy-Schwarz at each branching step, as the
unmarked lemma does. A proposed sharper recursion with no square roots reads
an additional all-leaf-set mass bound; it is not obtained from one-level MR
by saying the children are independent.

## 4. Source reconciliation and verification limits

Line references in this table are to the pinned **input** at 45b398967,
before the in-place edit. U means parts/upper-chain.md; QBR means
library/quiet-boundary-rarity.md. These are source mismatches and local
repairs, not new gate verdicts.

| Requested issue | Source mismatch and disposition |
|---|---|
| Mapped D1–D3; DM consumer section | U:844,1233,1494–1506 asserted inadequate depth/quiet/mu delivery. U now separates arbitrary-depth regular tops, mu, non-quiet from nonregular, and retains full HS joint rarity. DM+: statements only, no S/LMK or mu proof. |
| Mapped D5 | U:842,845 had only a fast exponential; U:1410–1430 already had a slow profile. Both local clauses now carry H_j; Proposition 17.2 also retains the slow tier and the exploration failures. Their transport margins remain unchecked. QBR/HS-T tails with only g^2 are not silently promoted. |
| Mapped D6 and quiet Requests | U:1458 example w_0=3 conflicted with its clearance; mapped:1041 writes b=t_0 in a different unit. Consumer now uses b=t_0/L, w=6t_0; mapped's t_0-layer theorem still has to cover these shapes. U:1227,1456,1529 used the obsolete mapped flux definition. |
| Mapped D7/D10(c) | U:450 used support volume, :431 used v eta^-4, :87 had an old range, :846 asked an unused additive Q^reg. Local repairs use neighbourhood volume, all Tor cells, full range and derivative Q. U's old delivery/covariance requests are superseded; mapped:300 already states the site-plane covariance. |
| Independent D6 | U:837,842 conflated GS smallness and rarity; :869 needs GS(c) beyond n_L. Errors are split and the large-n clause is explicitly still required. Independent:102,852–856 declines the full UV-OS package and retains the small-support smoothing restriction. |
| Independent D7/D9 | U:431 count fixed. U:1083 chart origin/mean now V^#/b^*. U:1089's curvature-domain step is replaced by a tube-disc argument on unwrapped cubes; wrapping use remains unproved. U:1219 omitted private local choices, present in independent:950–954. UV-CT cutoff wording is refinement-neutral; its narrower scalar-source class is still not the full W contract. |
| Fourth-form 4–6 and DEC geometry | U:820,831,1252–1270 had already repaired mixtures, factor two, finite floor sum. They are retained; U:1430's duplicate infinite sum is fixed too. U:1225 needed FILL separately; U:1325 needed n tied to m. Active statements now contain these qualifications. |
| New library notes / optional step 4 | FLOW-UL/END and RC/MC are explicit inputs, not new proofs. I(k;D) is now written as BD0–BD6; only the stated split-to-MD* implication and M22.2 conditional proof are supplied. RC-far, the generated joint induction and Q(n)/cumulant sums remain open. |

Read scope: GOAL/FINISH; all requested gate defects and DM's consumer section;
bounded U statements and their affected consumer arguments; the two attempts'
current Requests and needed map/chart/deliverable statements; the specified
flow/current/history notes; DM+ and paid-reference statements. Adjacent source
proof text exposed by bounded reads was not used to certify a producer or
transferred to the other attempt. No independent review, numerical experiment,
audit, commit, push or PR was run. No producer file or prompt file was edited.
The partial pullback and unreproved producer estimates remain visible rather
than being supplied by this contract.

Final mechanical checks (2026-11-01): HEAD remains the pinned revision; only
upper-chain.md and this new note are changed. The original first line and
the complete Earlier state block are unchanged, the lease is correct, and
`git diff --check` passes. These checks establish edit scope and formatting,
not the open mathematical estimates.
