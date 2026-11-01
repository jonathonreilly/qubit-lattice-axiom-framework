lead: openai/gpt-6-astra/max macbook-codex
lease_until: 2026-11-02T13:00Z

## State of attack

**Honest stop, continuation at `25a86977f538eb6bb104f097c435b44fd42138b7`.**
Author: openai/gpt-6-astra/max macbook-codex, 2026-11-01. This is
mapped-side author work, not an independent review or an audit.
The preceding checkpoint was pinned at `105283f2c`; git retains it.
New author proofs are labelled **unchecked**, and conditional algebra
is labelled **implication** with its hypotheses. No retained status
is conferred by either label.

**Step 1: gap.** No actual-R counterexample to AE-R was obtained,
and relative rough-cell transport/removability remains unproved.
The new quadratic calculation isolates the needed reference margin:
excess is exactly the squared curvature difference on an affine
fibre, and it pays a one-level R count if the constrained reference
is uniformly below threshold. Neither that margin for the actual
SU(2) data nor the all-level payment has been proved. Two-age,
nested quiet-limit and frozen-only routes are recorded below.

**Steps 2 and 3: gap, stopped at the dependency.** MARK-TAIL and
uniform patch gains, RF with fixed data, and R3-d with
LI-d/NL-d/COST-d/QT-d at two-age junctions remain open. No proof of
them is claimed; the earlier necessary equations and conditional
bump arithmetic remain in the frozen-bump note.

**Step 4: unchecked counterexample to literal Resp.** A finite
free-edge local lift can be flat while the global unfrozen lift of
the same parents has a nonzero tail there. With no older frozen
data, Resp's right side is zero. The new note gives an explicit
quadratic solution and a finite-dimensional argument for actual
small SU(2) minimizers. A separate exact rational check of the
quadratic equations passed. A corrected Resp+ with an additive
patch tail stays a gap; given it, the cube argument yields J+.

**Next decisions.** Prove the uniform global frozen response and
local/global tail in Resp+, or change the reference/quiet test
explicitly. For AE-R, construct a compatible relative descent
with the summed forced cap (RT-certificate), or find a counted R
at a class-top full-fibre minimizer. No inference from raw frozen
or movable action will settle that question. Do not resume the
RF/R3-d chain as though AE-R or Resp+ had been supplied.

## 1. Relative energy: what the hostile tests established

The common-reference excess is

    Xi_i=A_mov(U)-inf_{regular chains to P(V_i), with d} A_mov
        =A(U)-Acal_i^d(P(V_i)).

Fully frozen action cancels. Mixed plaquettes and fine plaquettes
forced by coarser data remain in A_mov, but may have no removable
excess. The reference must retain the SAME data at every level.
At a class top P(V_i)=V_i and err_i=C_W T^2|N_ref(V_i)|=0.

**Unchecked (proved quadratic statement).** For any consistent
linear constraints C h=g, including the union of different ages,
let h_* minimize E(h)=||d h||_2^2/2. Stationarity on the affine
fibre gives

    E(h)-E(h_*)=||d(h-h_*)||_2^2/2.                    (Q-EX)

If each counted one-level cell has a plaquette above T while the
reference on that plaquette is at most alpha T, alpha<1, then

    E(h)-E(h_*) >= (1-alpha)^2 T^2 N_R/(2m),           (Q-R)

where m is the plaquette-to-cell incidence (4 for elementary
4-cubes). This is free of the number of constraints, L and volume
when alpha is fixed. It does not cover Haar charges, changing
exclusion branches, the Wilson action away from its quadratic
limit, or an all-level allocation. Proof and scope are in
[the excess-contract note, section 2A](../library/active-energy-excess-contract.md).

**Gap (routes actually tried, on paper).**

- Two-age junction: simultaneous fixed equations give Q-EX, but
  relative quietness does not bound the local lift's displacement
  from the global reference. A threshold-crossing forced response
  was neither constructed nor excluded in the actual SU(2) domain.
- Many levels at the quiet limit: the exact frozen abelian pairs
  have identity parents and create no higher R. D1's copies placed
  one level up force positive fine movable action but supply no
  rough-cell threshold crossing. Summing these actions is not a
  counterexample with R and is not excess credit.
- Frozen-only roughness: a fully prescribed rough plaquette is
  fixed on the whole fibre. It refutes AE-R only if its cell is
  counted AND the prescribed history passes the quiet tests. The
  assertion that later quiet data have flux <=T/2 already reads
  ST/J; it cannot independently exclude this case. Mixed and
  coarse-forced plaquettes require the same reference comparison.

**Gap (first stopping inequality).** For actual R certificates r,
including their own-level labels and Haar charges, find one descent
budget B_i>=0 and nonnegative removable/forced parts with

    tau T^2 <= removable(r)+forced(r),
    sum_r removable(r) <= C B_i,
    sum_r forced(r) <= eta tau T^2 N_R,  0<=eta<1,
    Xi_i >= c_D B_i-err_i.                            (RT-certificate)

This gives a_R=c_D(1-eta)tau/C. The constants must be absolute after
the fixed threshold ratio/descent choices, free of x,L,depth,volume
and both ages. Ordinary TE controls total energy and proves neither
the summed forced cap nor the last line. D1's maximal free carriers
also need bounded overlap of ENLARGED supports across scales and
a constrained target; disjoint cells alone do not provide these.
No change to quiet, a cap, or the consumer's R has been adopted.
If an admissible forced R is found, such a change is necessary.

## 2. Resp: the independent item

**Unchecked (author counterexample, all steps written).** See
[the response-tail note](../library/active-energy-response-tail.md).
At one blocking step, prescribe a small abelian parent link only in
a slab beyond the finite local patch. The local patch sees identity
parents, so its free-edge minimum is flat. At quadratic order the
full four-dimensional minimizer reduces, by transverse averaging
and Jensen, to the periodic scalar problem with block means mu_j.
Its interface slopes satisfy

    b_L p_{j-1}+a_L p_j+b_L p_{j+1}=mu_j-mu_{j-1},
    b_L=(L^2-1)/(6L), a_L=(2L^2+1)/(3L).

For even M and one nonzero mean, the exact periodic Green function
has alternating nonzero entries, and p_j=G_{j-j_*}-G_{j-j_*-1}
is nonzero at EVERY interface. Its tail decays but does not vanish.
A block-tree gauge bound, compactness, and comparison with an EXACT
abelian trial show that the actual SU(2) minimizing curvature,
divided by its amplitude, converges to that quadratic curvature.
This uses finite-dimensional constants, not a uniform R3 theorem.

Freeze the first brick with identity data. An explicit field with
those data and the prescribed parent exists, and Dev=0 there.
Resp compares its flat local lift with the global lift, but has
an empty older-data sum. Its left side is positive and its right
side zero. No C_r fixes this. There are no R cells in the example,
so it gives no negative conclusion about AE-R or rarity of R.

**Gap (corrected analytic input).** Retain a common global reference
and write

    ||Theta(Lift_b^d)-Theta(W_ref)||_Q^2
      <= C_r sum_{older Q'} exp[-2 rho dist(Q,Q')/L]a(Q')
         +tau_b(Q)^2,
    sup tau_b(Q)^2 <= kappa_tail eps_q^2 T^2.          (Resp+)

Uniform bounds for the global frozen response and for the difference
between the local and global constrained lifts suffice, by the
squared triangle inequality. They are still open, including their
existence/regularity hypotheses and all nested histories. Changing
W_ref to a patch-dependent reference is another possible repair,
but J would then need comparisons between those references.

**Implication (J+).** The existing cube geometry has near rank <=5,
N_0=35^4 and far row sum S(rho) exp[-rho t_0/(64L)]. With
B=2C_r N_0, P=1+B+B^2+B^3+B^4 and
D=2C_r S(rho)exp[-rho t_0/(64L)], Resp+ and relative quietness imply

    sup_Q a(Q)<=4P(1+kappa_tail) eps_q^2 T^2,  PD<=1/2.

Thus C_J=2P(1+kappa_tail) for the aligned partition, or
32P(1+kappa_tail) for all translated testing cubes. The amended
[active-energy cube note](../library/active-energy-junction-cubes.md)
records the implication. No nonlinear response estimate follows
from the geometric summation.

## 3. Constants and dependent work

| Constant/result | Dependence and standing |
|---|---|
| Q-EX coefficient 1/2; Q-R coefficient (1-alpha)^2/(2m) | Unchecked author proof; m and the assumed margin alpha only; free of x,L,depth,volume and number of affine constraints |
| Scalar tail q_L and Green amplitude | Unchecked explicit formula; 0<q_L<2-sqrt(3), amplitude depends on L,M,distance; no separation-uniform lower bound claimed |
| SU(2) small-amplitude limit | Unchecked finite-geometry proof; constants and the amplitude threshold may depend on L and volume; one level suffices for the zero-RHS contradiction |
| C_r,rho,kappa_tail for Resp+ | Gap: must be free of x,L,depth,volume/history; allowed patch size selected before x |
| P,C_J for J+ | Implication: C_r,rho,kappa_tail,d and fixed incidence convention only, if their uniformity holds; requires t_0/L large enough |
| a_R,a_S,C_W,C_E,c_D,eta; bump C_b,C_Q/radii | Gaps: absolute after the fixed choices, free of x,L,depth,volume/history |
| Flow/support and entropy constants | Inherited inputs, not reverified here; may depend on L,a_*, must be depth/volume-free as their consumers require |

**Implication (previous dependent algebra only).** AE-R and AE-S
with a same-prefix mark assignment give all-mark W2 after reducing
the gains once. With W1, the flow and the support counts, the
summation-by-parts/constant-reserve argument gives OW's own-level
payments. DM additionally requires its density, locality/tail and
counting inputs. These remain conditional exactly as specified in
the excess-contract note. The frozen-bump note's nonlinear solve
requires its exact frozen chart, compatible mismatch and NL-d;
its claimed cost additionally requires COST-d and QT-d. None of
these inputs was supplied by the present scalar calculation.

## 4. Verification and recovery record

**Unchecked (checks actually run).** One exact rational job compared
separately assembled fine-site KKT and interface-slope systems for
(L,M)=(3,12),(5,12),(7,12),(5,16), with zero and constant controls.
Every registered exact equality and nonzero tail condition passed.
This verifies finite scalar algebra, not nonlinear SU(2), two-age
junctions, the actual patch radius or AE-R. The new note's analytic
formula covers arbitrary even M; its SU(2) passage is an author proof
without an independent reader. No failed run was discarded.

Criteria, runner and full preflight/acquire/run/release logs are in
`checks/active-energy/`. Acquire was confirmed before the nice job;
BLAS thread variables were 1. OS address/data caps were unavailable,
so the runner used its 2 GiB RSS stop at every elimination pivot;
peak RSS was 17,186,816 bytes. The numeric lock was released.

Read: GOAL/FINISH; the active-energy part and its three library
notes; repair-gate-105283f2c, especially D1; Q's Setting/ST/J and
R/mark definitions (lines 1-95); frozen-energy construction; the
paid-inputs junction note; TE and descent (relative-density-bound
233-288,325-385); F-D/BG/nest (fibre-propagator 110-173); mapped
Text 3.1 and the relevant 5.1/5.2 passages. Scoped searches located
these statements. No claim to have reviewed the entire mapped part,
all of its consumers or the full linear/nonlinear R3 proof is made.
The absent methodology files were read with git show at pinned HEAD;
the user's fixed source, write scope and stop instruction govern this
bounded task. No paper or external proof was imported.

The independent attempt, its good file, gates on it and all
history-budget gates were not opened. No mapped/quiet-boundary-rarity
file, axiom, ledger or prompt was edited. No audit, subagent, commit,
push, PR or external post was made. Source identities and final
path/whitespace checks are recorded in `checks/active-energy/`.

## 5. Final disposition

**Proved in this author derivation (unchecked by an independent
reader):** Q-EX; Q-R with its stated reference margin; the nonzero
quadratic tail and its minimizing SU(2) small-amplitude limit, hence
the counterexample to literal tail-free Resp.

**Conditional exactly on:** Resp+ with uniform constants, relative
quietness and the cube geometry for J+; the affine quadratic model
and reference margin for Q-R; the unchanged AE/assignment/W1/flow
and other named analytic inputs for W2/OW/DM; the frozen chart and
bump inequalities for the nonlinear correction.

**Still open:** AE-R/RT-certificate (no actual-R counterexample
found), MARK-TAIL and uniform patch gains, RF with fixed data,
R3-d and LI-d/NL-d/COST-d/QT-d at two-age junctions, and corrected
Resp+. These gaps are not asserted independent. Stop here.
