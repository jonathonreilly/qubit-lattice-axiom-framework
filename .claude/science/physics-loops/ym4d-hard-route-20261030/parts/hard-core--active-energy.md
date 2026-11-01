lead: openai/gpt-6-astra/max mac-mini-codex
lease_until: 2026-11-02T11:00Z

## State of attack

**Honest stop — author derivation completed.** Pinned source:
`105283f2c2a5a306a2aff46a47dfadb7a3b6ef0e`. Author mathematics on the
mapped side, not an audit or an independent check. The independent
attempt, its good file and gates, and history-budget gates are excluded.

**Gap, energy:** the replacement is the signed excess over the SAME
constrained reference, with explicit all-R and all-mark payment.
Its first unproved step is relative transport/removability (AE-R/RT),
followed by the frozen-data RF and R3/bump. Raw unfrozen action is
not enough, because some of it may be forced by the constraints.
W2 and the two DM energy branches remain conditional.

**Discharged geometry; implication for J:** at cube side t_0/1024,
use near cutoff t_0/64. Six successive cubes would meet six bricks
in a box of width <t_0/8, impossible for the actual wall grid.
Thus the near matrix has fifth power zero. The far row sum is
bounded explicitly and absorbed. This proves Lemma J GIVEN uniform
(Resp), with a corrected constant; (Resp) itself stays a gap.

The exact statements, proofs and stopping inequalities are in:

- [`active-energy-excess-contract.md`](../library/active-energy-excess-contract.md)
- [`active-energy-frozen-bump.md`](../library/active-energy-frozen-bump.md)
- [`active-energy-junction-cubes.md`](../library/active-energy-junction-cubes.md)

No numerical job ran. Only this part and those three new library
files were written. No mapped/rarity source, axiom or ledger was
edited; no audit, subagent, commit, push, PR or external post ran.

## 1. Replacement and the three tests

**Gap (the required replacement, precisely).** With
P_mov={fine plaquettes with at least one unfrozen link}, define

    Xi_i = A_mov(U)-inf_{regular chains to P(V_i), with d} A_mov
         = A(U)-Acal_i^d(P(V_i)).

The reference has exactly the same frozen data. Require

    Xi_i >= a_R T^2 sum_{k<i}|R_k| - C_W T^2|N_ref(V_i)|,
    Xi_i >= a_S eps_q^2 T^2 sum_{k<i}|S_k^clean|
                                      - C_W T^2|N_ref(V_i)|. (AE)

Every remaining type-I mark must be assigned to a paying R cell
inside the same prefix, with the source's bounded multiplicity;
every type-II mark is an R cell. No charged cell is dropped because
its parent is frozen.
The error is zero at a class top. The companion note shows exactly
how, after a one-time reduction of c_T,c_S, these estimates give
the printed W2 coefficient 1/2 for EVERY R and open mark. AE is a
proposed sufficient replacement, not a theorem proved here.

**Discharged, locked-action test.** In the existing exact abelian
construction Xi_i=0 although A^Z>0. No term A^Z is subtracted by AE.
Subtracting frozen action from both baselines while retaining A^Z
would repeat the original contradiction. The construction has no R
cell and no free non-quiet mark, so it is not a counterexample to AE.

**Discharged special case; gap generally, adjacent mark.** In that
abelian family a separate free pair in a neighboring brick can be
non-quiet relative to its constrained lift, and removing it releases
12(1-cos b)>=24 b^2/pi^2 while every frozen link and parent stays
fixed. In general the mapped file already changes absolute quietness
to Dev_b^d, correctly removing the forced response from the event.
It still needs MARK-TAIL and an actual coercive patch replacement
with fixed links; a mark at a constrained minimizer would violate AE.
For DM the mark must also satisfy its stated two-brick clearance.

**Gap, R with partly frozen fine energy.** TE controls counts by
TOTAL fine action, so it cannot prove AE by deleting its frozen term.
A Z cell can be paid entirely by frozen action, as explicitly
constructed. I did not construct such an ACTUAL active R cell under
all the prescribed clearances, or prove it impossible. The distinction
is essential: the known field has identity parents and zero labels.
The exact missing relative statement RT requires a jointly removable
budget B_i and forced allowance H_i with

    T^2 N_R <= C_E(B_i+H_i),
    H_i <= eta T^2 N_R/C_E, eta<1,
    Xi_i >= c_D B_i - C_W T^2|N_ref(V_i)|.                (RT)

Then a_R=c_D(1-eta)/C_E, by subtraction. If a counted R were forced
at a class-top full-fibre minimizer (where Xi<=0), W2 would fail;
if forced on the whole fibre, its conditional probability would be one, so the
claimed rarity for that event would fail too. These are implications,
not a new field counterexample. A consumer could demand a stronger
quiet condition with the explicit summed forced-energy cap
(QUIET-CAP) of the note, or change the event to an excess event.
Both require new proofs and change what has been supplied so far.

## 2. Why the bump is still an honest stop

**Discharged necessary equations; gap on their solution.** The
allowed tangent chain satisfies H_j=0 on ALL frozen level-j links,
D M_j H_j=H_{j+1}, and the rooted gauge conditions. A parent mismatch
must lie in the image of the top derivative on this space. Keeping
only fine links fixed is insufficient for frozen coarser data.

The bump note states LI-d (right inverse), NL-d (a contraction bound
in a volume-uniform local parent norm), COST-d (movable action cost),
and QT-d (small movable target energy). It derives the nonlinear
solve and sparse-cost arithmetic CONDITIONAL on those inequalities.
It does not assert a chart or inequality not constructed here.
At a two-age junction these must hold for the union of the frozen
constraints, with one constant, including different-level scales.
RF allows a parent mismatch and does not supply this fixed-link
correction; F-D's graph inverse does not supply the nonlinear
regularity of the actual minimal lift. This is the explicitly
unwritten R3 with data in the source, not a discharged application.

## 3. The independent Lemma J item

**Discharged (new geometric derivation).** All walls of BG's actual
four-dimensional tiling are on a common grid of spacing t_0/8.
Any box narrower than that in every coordinate meets bricks sharing
one point, hence at most five bricks. A near chain of six cubes of
side h=t_0/1024, cutoff r=t_0/64, has coordinate span
5r+6h=86h<128h. Strictly decreasing brick ages would require six
distinct bricks there. This gives a cube rank in {1,...,5}, unlike
the printed point rank based on the false ball-incidence claim.

**Implication (given Resp, with explicit absorption).** Let
B=2 C_r 35^4, P=1+B+...+B^4, and

    S(rho)=sum_{m>=0} n_m exp[-rho(m-1)_+/128],
    n_0=1, n_m=(2m+1)^4-(2m-1)^4 for m>=1.

The far row sum is at most S(rho)exp[-rho t_0/(64L)]. Taking
2 C_r P S(rho)exp[-rho t_0/(64L)]<=1/2 gives

    sup_Q a(Q)<=4P eps_q^2 T^2 = 2 C_J eps_q^2 T^2,
    C_J=2P.

This is for the aligned cube partition; all translated testing
cubes are covered by at most 16 partition cubes, so C_J=32P suffices
for that convention with the same absorption condition.

This is an a priori estimate on any finite history and compatible
torus. No numerical enumeration or fixed-point existence argument
is used. It is uniform over same-level ages. Its application to
background data with arbitrarily many levels is conditional on
Resp's uniformity over those data; it is not a multilevel response
proof or a frozen-data bump proof.

## 4. W2, OW and DM: only the dependent algebra

**Implication, not a new proof of rarity.** Given AE, the mark
assignment, W1, the flow and the original support counts, W0's exact
summation by parts yields (1/2)sum_k xtilde_k Delta_k at a class top.
The companion excess note tracks the actual consumer coefficients:
g_I=3x_k c_S eps_q^2 T^2/8, g_II=x_k c_T T^2/8, and a remaining
x_k c_T T^2/4 per R. It follows the EXISTING factor-24 reserve in
`threshold-paid-reference.md`, rather than relying on equality in
the mapped factor 6. The DM class-W energy branch then prices its
level-i marks; its rough-W branch has the required remaining 1/8
rough-cell factor after reserves. All of this remains conditional
on the named inequalities and DM's other analytic inputs.

**Discharged (source comparison).** At this commit the mapped State
of attack already names Dev_b^d, relative junction stability, the
paid tubes, and the unwritten R3 bump. It still uses the false
untrimmed CI-paid^d; it has not supplied AE/RT. I followed its
relative mark definition and the existing threshold note's algebra.
No claim is made to have rediscovered those changes.

## 5. Constants and final disposition

| Constant | Dependence and status |
|---|---|
| Wall grid, rank 5, near count 35^4 | **Discharged:** dimension and fixed cube convention only; free of x,L,depth,volume |
| P,C_J,S,c_0 for J | **Implication:** C_r,rho,d and fixed incidence convention; free of x,L,depth,volume IF Resp is uniform; t_0/L>=c_0 |
| a_R,a_S,C_W,C_E,c_D,eta | **Gap:** need absolute constants after b_2 and fixed descent choices, free of x,L,depth,volume/history |
| C_b,C_Q and nonlinear radii/rates | **Gap:** same uniformity; the sparse radius is Prop 10's r_{I_*}, not a T-dependent fill radius |
| C_1,C_5,C_flow,C_4 | **Unchecked inputs:** allowed to depend on L; must be depth/volume-free |
| t_0,d_x,entropy constants,x_* | **Implication:** allowed dependence on L,a_* and already fixed absolute constants; free of depth/volume; the final DM sum also uses a fixed positive flow slope |

**Proved here:** exact frozen-action cancellation for the excess;
the special removable-mark test and the necessary minimizer tests;
the cube near-propagation bound, far row sum and absorption algebra;
the conditional payment and nonlinear-solve arithmetic.

**Conditional exactly on:** uniform Resp for Lemma J; AE-R/AE-S,
mark allocation, W1, flow and support counts for W2/OW; also the
remaining density, Z, locality/tail and counting inputs for DM;
the exact frozen chart and NL-d/COST-d for the nonlinear bump solve.

**Still open:** relative rough-cell transport/removability RT,
MARK-TAIL and uniform patch gains, RF with fixed data, R3-d and the
LI-d/NL-d/COST-d/QT-d estimates at two-age junctions, and Resp itself.
No claim that these gaps are independent. Energy work stops here;
the independent geometric item was completed as the implication above.

**Reading/work record.** Bounded reads of GOAL/FINISH; the requested
DM5 gate, paid-inputs part, frozen-energy note; Q setting, Z/DM and
OW/CI; R:233-287,325-384; F-D/BG/nest and RF statements/proofs;
the mapped State of attack, relevant kernel and R3 paragraphs;
the paid-reference coefficient passage and existing junction-response
note, plus the frozen-mesh sufficient-condition passage. The absent
working-tree methodology was read from pinned HEAD; scoped-workhorse
guidance and planning AGENTS were read without taking scientific
status from them. No forbidden attempt or gate was opened. Final
checks are source/algebra/geometry inspection and whitespace/path
checks only; no script-generated mathematical result is claimed.
