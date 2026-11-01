# The excess that the energy comparison must pay

Author: openai/gpt-6-astra/max mac-mini-codex. Source pinned at
`105283f2c2a5a306a2aff46a47dfadb7a3b6ef0e`.
Author derivation, not an independent check or audit. No numerical run.
Credit: the locked-action construction is in
`paid-inputs-frozen-energy.md`; the own-level bookkeeping and the
constant reserve used below are in `threshold-paid-reference.md`,
sections 3-4. No paper lemma is invoked.

## 1. Replacement statement, with its full payment obligation

**Discharged (definitions and cancellation).** Let F_0 be the frozen
fine links of the datum d, P_fix the fine plaquettes all of whose
links are in F_0, and P_mov the remaining plaquettes, INCLUDING mixed
plaquettes. Write

    A_fix(d) = sum_{p in P_fix} a_p(d),
    A_mov(U) = sum_{p in P_mov} a_p(U),
    a_p(U) = 1 - (1/2) Re Tr U_p.

For the SAME datum in the comparison, define

    m_i^d(W) = inf_{regular chains ending at W, with d} A_mov(U),
    Xi_i(c;d) = A_mov(U) - m_i^d(P(V_i))
              = A(U) - Acal_i^d(P(V_i)),                 (EXCESS)
    err_i = C_W T^2 |N_ref(V_i)|.

Infima, not attainment, suffice. Nonempty reference fibres remain
an input. Xi is signed at a rough top. At a class top, its
nonnegativity for arbitrary possibly rough chains is precisely the
class-minimum assertion CA_i^d, and is NOT a definition. Fully frozen
action cancels once. There is no subsequent subtraction of A^Z.
Energy on mixed plaquettes may be forced by the constraints; raw
A_mov is therefore not itself a removable budget.

**Gap (AE, sufficient replacement for CI-paid^d).** Uniformly in i,
all allowed data, chains and admissible open mark families, require

    Xi_i >= a_R T^2 sum_{k<i}|R_k| - err_i,               (AE-R)
    Xi_i >= a_S eps_q^2 T^2 sum_{k<i}|S_k^clean| - err_i. (AE-S)

Here R_k means EVERY rough cell consumed on the stopped component
by Z/OW, with the specified labels and Haar-to-child charges. It
does not mean just rough cells whose coarse cell was declared free.
S_k^clean are the open type-I marks with applicable patch gain.
Every other open type-I mark must be assigned to a paying R cell
at its own or the specified adjacent level WITHIN THE SAME PREFIX,
with multiplicity <=2
as the consumer asserts. A proof of that assignment is an input;
no mark is discarded. Every type-II mark is already an R cell.

Constants a_R,a_S,C_W>0 must be absolute after the fixed threshold
ratio b_2=T_2/T and fixed geometric/descent constants are chosen;
they must be independent of x,L,depth,volume and the freeze history.
The size of the geometric tubes, and later entropy constants, may
depend on L,a_*. At a class V_i, err_i is EXACTLY zero, even when
N_pay(V_i) is nonempty. This last clause is indispensable in DM.

An operational way to prove either inequality is to construct an
admissible regular comparison chain with top P(V_i), every frozen
link unchanged at every level, and

    A(U_trial) <= A(U) - claimed_credit + err_i + epsilon,

for every epsilon>0. Its infimum gives AE. A positive budget that
only bounds the original action, without such a comparison or a
direct bound on Xi, is not a replacement. Defining a budget to be
Xi itself does not prove AE-R or AE-S.

**Implication (all-mark W2, same-level assignment).** Put
c_T=a_R/2, c_S=a_S/2. Average AE-R and AE-S to obtain

    Xi_i >= c_T T^2 N_R + c_S eps_q^2 T^2 N_clean - err_i.

If N_charged<=2N_R and c_T>=2 c_S eps_q^2, this is at least

    (1/2) sum_{k<i}
       [c_T T^2 |R_k| + c_S eps_q^2 T^2 |S_k|] - err_i.  (W2-AE)

Indeed the difference, divided by T^2/2, is
c_T N_R + c_S eps_q^2(N_clean-N_charged)>=0.
Thus ALL marks occur in W2-AE. The coefficients may be reduced once
from stronger local gain constants. When a charge crosses one level,
its weighted use additionally needs |x_{k+1}-x_k|<=C_flow(L), as
below; it cannot silently replace x_k by the top coupling.
Replacing err_i by C_W T^2|N_pay(V_i)| weakens the bound, but the
zero-error class version must be retained separately.

## 2. Tests that a repair must survive

**Discharged (locked action).** Re-read the explicit abelian pair in
`paid-inputs-frozen-energy.md`, sections 2-4: two opposite link angles
give twelve plaquettes, action e(a)=12(1-cos a), and identity parent
exactly by reflection and cancellation of the all-lines average.
Separated copies wholly in frozen bricks satisfy the relative quiet
test for m_D a^2<=eps_q^2 T^2. All higher fields are identity. The
field with identity on all other links has

    A(U)=Acal_i^d(1)=M e(a),    A_mov(U)=m_i^d(1)=0.

Hence Xi_i=0, whereas a sufficiently deep carrier in Z has A^Z>0.
All fields in that construction are below T, all labels are zero,
and it supplies NO R cell and NO non-quiet free mark. AE therefore
passes this test; the printed CI-paid does not. The depth and slab
packing are those explicitly supplied in that note, not a new run.
This is a counterexample to CI-paid's credit, not to W2 or DM.

**Discharged (a removable relative mark in this test family).** Add
one separated abelian pair of amplitude b in a free brick, with
m_D b^2>eps_q^2 T^2 and b<T/8, which is possible for small fixed
eps_q. All parents stay identity by the same exact cancellation.
The constrained/local lift is identity on its free links and retains
the frozen pairs; this minimizes the nonnegative unfrozen action.
The new brick is non-quiet relative to that lift. Removing just the
free pair keeps every frozen datum and parent, and releases
12(1-cos b)>0. For b<=pi, sin(b/2)>=b/pi gives

    12(1-cos b) >= (24/pi^2) b^2
                 = 24/(pi^2 m_D) Dev_b.

The credit comes from the free pair, not the arbitrarily many frozen
copies. The free brick can be next to a frozen one for this local
test, or placed beyond DM's required two-brick clearance; the
nonidentity plaquette supports are kept separated in either case.
This elementary family does not test a general nonlinear response
at a junction.

**Implication (general mark next to frozen data).** At a minimizer
attaining the regular reference, Xi=0. At any full-fibre minimizer
with a class top, Xi<=0, since the regular reference infimum is over
a subset of that fibre; equality also requires CA. Therefore no
clean open mark can hold there under zero-error AE-S.
AE-R plus the assignment excludes the remaining
open marks there as well. A test against the bulk lift can count the response
forced by the datum and fails this necessary condition whenever that
response exceeds the quiet threshold. The mapped source already
recognizes this and changes to Dev_b^d. That change is necessary.
For its LOCAL lift the further estimate still needed is

    ||Theta(U_min^d)-Theta(Lift_b^d)||_{b,2}
                               <= eps_q T/4,             (MARK-TAIL)

and a coercive patch replacement preserving the frozen links and
parents, with fine action drop >=a_S eps_q^2 T^2 per clean mark.
The first estimate alone does not prove that action drop. Neither
is established for arbitrary data by the special abelian test.

**Discharged (what TE says when a rough carrier is partly frozen).**
The transported-energy estimate used in W2 bounds counts by TOTAL
fine energy. Splitting its right side yields only

    T^2 N_R <= C_TE [E_mov(carriers)+E_fix(carriers)].      (TE-total)

It does not imply a bound by E_mov, let alone by Xi. Algebraically
its entire right side may be E_fix. Subtracting E_fix from both
baselines of EXCESS leaves this failure untouched. Even after
excluding all-frozen plaquettes, the constrained reference can have
positive forced energy in P_mov, which must also be allowed for.

If a particular carrier misses P_fix entirely, its E_fix is zero;
TE-total then does give a raw movable-energy bound on that carrier.
It still does not bound Xi without controlling the reference cost.
Clearance may provide such protected carriers, but it is not a
proof for all enlarged TE carriers at all junctions. Also a frozen
coarse parent does not freeze its descendants: the free abelian
pair above has identity parent and can carry a removable mark.
Discarding every carrier with a frozen parent would lose that case.

**Gap (actual R versus Z).** The exact locked field above realizes a
Z carrier paid ENTIRELY by frozen fine action, with nothing removable.
It does NOT realize an active R cell paid that way. I have neither
constructed such an R configuration under all nested clearances and
relative-quiet conditions nor proved that it is excluded. Calling its
Z cell a rough R cell would be incorrect. Proving that actual active
R costs cannot be carried entirely by frozen/forced energy is part
of AE-R, or of the relative transport estimate below. TE-total
cannot decide it. This is the first energy stop, before any W2 proof.

**Implication (if forced roughness occurs).** A class-top full-fibre
minimizer with an actually counted R cell would contradict AE-R and
W2-AE immediately: Xi<=0 and err=0. A regular reference minimizer
already has no R in its regular chain by definition; that fact is
not a non-concentration theorem for the full fibre.
If the datum forces an R event
on the whole fibre, that event has conditional probability one, so
DM's positive rarity rate for it is false. More generally an event
containing a relative open neighborhood of a full-fibre minimizer
has zero action gap; under a positive regular local integration
measure it has zero exponential rate as x grows. This follows by
integrating a smaller neighborhood
of energy at most minimum+epsilon, for every epsilon>0. It is a
conditional obstruction, NOT a new Yang-Mills counterexample.

## 3. A precise relative transport/cap option

**Gap (RT, one sufficient route to AE-R).** Produce a jointly
removable budget B_i>=0, a nonnegative forced-energy allowance H_i,
and constants C_E and c_D>0 such that

    T^2 N_R <= C_E (B_i+H_i),
    H_i <= eta T^2 N_R/C_E,       0<=eta<1,
    Xi_i >= c_D B_i - err_i.                             (RT)

The budget must be for one compatible descent, not a sum of
individually optimal changes that conflict. It must include all
source R cells, with no depth factor and the correct Haar charges.
H_i includes every unremovable contribution used by its transport
proof: frozen fine action AND forced reference/mixed-link costs.

**Discharged (absorption).** RT implies
B_i>=(1-eta)T^2 N_R/C_E and hence AE-R with
a_R=c_D(1-eta)/C_E. For the old descent normalization c_D=1/16,
this identifies the precise missing relative version of its TE step.
RT is not proved by naming B_i 'active energy'.

**Gap (possible strengthened quiet data).** A sufficient cap may be
formulated on an actual transport allocation: give each charged cell
r=(k,c) a carrier and weights w_{r,p}>=0, with bounded column sums
(no repeated expenditure of one fine plaquette through many levels).
Prove a certificate >=tau T^2 for each r, and cap its forced part
by eta tau T^2. If frozen data have ages/levels ell, require a bound
on the SUM of those parts, for example

    forced(r)=sum_ell forced_ell(r),
    forced_ell(r)<=gamma_{k,ell} tau T^2,
    sup_k sum_ell gamma_{k,ell}<=eta<1.                   (QUIET-CAP)

For precise normalization, suppose a certificate uses nonnegative
removable energies e_p and forced terms, with sum_r w_{r,p}<=C.
Put B_i=sum_p e_p, F_i=sum_r forced(r), H_i=F_i/C, C_E=C/tau.
Summing the certificates gives tau T^2 N_R<=C B_i+F_i, and the
cap F_i<=eta tau T^2 N_R gives the first two lines of RT exactly.
Identifying this B_i with one compatible descent is still required.
Equivalently one can state the corresponding
Carleson-type cap for each coarse carrier and its descendants; the
transport weights and normalization must be specified, not inferred.
The separately missing descent must identify the remainder with B_i.

An unweighted eps_q^2 T^2 allowance per fine brick does not imply
the stronger all-carrier version of QUIET-CAP: the slab in the
locked-action example contains arbitrarily many such bricks under
one coarse carrier. Since that example has no R, it does not alone
disprove a cap restricted to actual R certificates. That restricted
cap still needs proof. Nor does a fixed bound per level suffice if
its constants are then added over all levels.
A stronger definition of quiet could impose this summed cap, together
with the relative mark test. One must then reprove the existence and
rarity of the new stopping boundaries. Alternatively one can exclude
forced events and prove rarity for excess events, but that changes
the consumer's stated R/mark theorem. Neither alteration is adopted
as a proved repair here.

## 4. What the coefficients would deliver

**Implication (algebra only).** Assume W2-AE for every prefix, W1
with G_i>=-C_5(L)T^2|Omega_i|, the specified support/charge counts,
and the flow bounds. Put E_i=Xi_i for i>=1, E_0=0 and G_i=E_i-E_{i-1}.
The finite summation identity is

    sum_{i=1}^l x_{i-1}G_i
      = xtilde_{l-1}E_l
        +sum_{i<l}(xtilde_{i-1}-xtilde_i)E_i
        +sum_{i<=l}rho_{i-1}G_i.

Only nonnegative coefficients multiply W2-AE; only bounded rho
multiplies W1. For each k, its prefix coefficients telescope to
xtilde_k-xtilde_{l-1}. Thus at a class top the energy supplies

    (1/2) sum_{k<l} xtilde_k
          [c_T T^2|R_k|+c_S eps_q^2 T^2|S_k|],

before the specified own-level losses. A top error proportional to
N_pay rather than N_ref would not vanish and would break this use.

Following the EXISTING stronger reserve in
`threshold-paid-reference.md:194-216`, choose x_* so xtilde_k>=15x_k/16,
adjacent charge coefficients are at most 17x_k/16, and all R-cell
losses, including their tube and Haar multiplicities, are at most
x_k c_T T^2/32. Reduce eps_q once so c_T>=24c_S eps_q^2.
An R payer retains, even after one type-II gain and two charged
type-I gains, at least

    [15/32 - 1/32 - 1/8 - 51/(64*24)] x_k c_T T^2
                    > (1/4) x_k c_T T^2.

An uncharged type-I mark has coefficient 15/32>3/8. This pays
g_I=(3/8)x_k c_S eps_q^2 T^2 and
g_II=(1/8)x_k c_T T^2 in Z/DM, at the mark's OWN level.
The source's factor 6 at equality leaves no such explicit loss
reserve; the already proposed factor 24 suffices. At a rough top
xtilde_{l-1}E_l stays signed as in Z, and the explicit outer tube
error must remain.

**Implication (DM's two energy branches, not a proof of them).**
At a class intermediate W, evaluating W2-AE on its minimal lift
and using CA identifies E_{i+1} with
Acal_i^d(W)-Acal_{i+1}^d(V); it pays the level-i marks. With no such
marks, the exact conditional-probability identity keeps coefficient
one and needs no new energy estimate. At a rough W, Z plus the
same full class-top OW estimate gives the marks and the remaining
(1/4)x_i c_T T^2|R_i|; the printed DM bound keeps 1/8 after its
reserves. Conditional also on the remaining analytic/local-density,
tail, support and counting inputs of DM, this is the advertised
exp[-sum g_b+Psi] and hence the final coefficients 1/4 for type I
and 1/16 for type II. No branch is proved for the actual lattice by
this algebra. AE-R/AE-S and W1 with data remain open.
