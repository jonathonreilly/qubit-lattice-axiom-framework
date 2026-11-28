# A paid reference at threshold 2T

Author: openai/gpt-6-astra/max, mac-mini-codex. Pinned source:
`6d28846d6c9052ed1937173587a32c5c9351e141`. Author derivation, not an
independent review or audit. No numerics. This removes a reference-domain
mismatch **conditionally**; it proves neither (EXT=) nor Theorem Z/DM.
Here A_i^d denotes the source's regular-chain energy 𝔸_i^d. Its
identification with the classical effective action is part of the named
class-minimum input, not an identification of the full density F_i.

## 1. Quantifiers, constants and geometry

**Implication.** Assume the stated F2-mult theorem of
`fill-cubical-extension.md`, including its Borel construction, and its
frozen-brick clause under the exact discrete hypothesis (FG). That proof
was read but is independently unchecked. Denote its absolute constant by
`A_f=C_*(4K_fill)/K_fill`, `K_fill=16pi`; this avoids confusing it with the
draft's other uses of C_a or K_0. Fix absolute numbers

    A_book >= 2 A_f,    P_book >= 1,
    b_2=P_book A_book,    T_2=b_2 T.                           (P0)

One may keep the *existing* T_2 without changing any formula range if
`T_2/T >= 2 A_f` already holds. With the literal identification C_a=A_f,
this asks only C_p>=2. If that margin was not reserved, use
A_book=2 A_f and P_book equal to the original C_p before choosing L
and a_*; relative to the identification C_a=A_f this doubles T_2.
It is not an iterated threshold change. Here P_book only records any
pre-existing margin; the present comparison uses VAL, not a path between
different sectors.

The order is: d=4, SU(2), K_fill and A_f; A_book,P_book and all other
absolute analytic constants; L large enough for the original constraints
and `C_s L^(-kappa) b_2 <= 1/4`; a_*>0 small enough for the original convex
and formula domains and 2T<=1, where T=a_*/L^2; then

    n=ceil(sqrt(K_fill/(2T))),
    t_0 >= 8n, with the compatible integer brick/mesh walls of (FG),
    d_x >= 32(n+L), and all original t_0, d_x, r_S, r_N requirements;

then the fixed loss constants and x_*(L,a_*). If a collar needs more than
8 blocks, enlarge 32 by a fixed factor before x_* is chosen. Constants
depending on T,t_0,d_x are permitted to depend on L,a_*; none may depend
on volume, level, chain depth, number of frozen components, field or x.
Only after these choices quantify over finite compatible domains, levels,
quiet data, fields, labels, chains and marks. Every x_k is >=x_* and has
the original bounded adjacent differences and monotone-envelope defect.

Frozen quiet bricks have flux <=T/2, hence <=2T. Under (FG), the mesh
refines them and no coarse cell in such a brick is selected by a plaquette
above 2T. Thus the supplied fill preserves their bonds. Compatibility of
the actual site-centred crossing-bond convention with (FG) is still
**unchecked**; arbitrary frozen bonds are not included in this implication.

## 2. Two supports with different jobs

For a field V on the domain of the current invocation set

    D={max theta(V)<=T_2},       Y(V)={cells with theta(V)>2T},
    N_pay(V)=tube(Y(V)),
    X_ref(V)=empty if V in D, and Y(V) otherwise,
    N_ref(V)=tube(X_ref(V)),     tube(empty)=empty.

Here `N_pay(V)` is a **budget region**, even at a class field. `N_ref(V)` is
the region used for the reference and the outer exploration. Define

    P(V)=V                         if V in D,
    P(V)=F2-mult_(t=2T)(V,Y(V))     otherwise.                (P1)

**Implication (reference existence, proof under the stated fill/FG input).**
Outside Y the input bound is exactly 2T. Thus F2-mult gives maximum
<=2 A_f T<=T_2, equality to V off selected cells within 8n of Y, and
equality on frozen bonds. In the class case these statements hold by
identity. The selected cells are at least 8L inside the edge of N_ref:
the tube contains the d_x/2 neighbourhood of Y, and
d_x/2-8n>=8L. Empty-boundary/full-torus cases have no collar to check.
The selector is Borel: D is closed, and the supplied fill is Borel on
the complementary branch. It depends on the level field and fixed
geometry alone, not on labels, the chain below it, or a choice of later
stopping layer compatible with that geometry. No differentiability or
gauge covariance of the selector is claimed. In particular,

    V class => P(V)=V and N_ref(V)=empty                 (P2)

holds even if V has many cells in (2T,T_2].

**Discharged (payment-set inclusion).** For every label realization,
Y(V_k) is contained in the pinned R_k: labelled cells or cells above 2T,
with the existing Haar-parent charging convention. Hence, writing
v=C_tube(d_x+t_0)^4,

    |N_pay(V_k)| <= v |Y(V_k)| <= v |R_k|.                   (P3)

The last display is a set count before the original Haar charges are
distributed to children. Bounded multiplicity of that distribution and
its one-level coefficient change remain part of the existing TE input.
This note does not replace an arbitrary Haar plaquette by a flux-squared
action cost.

**Discharged (why not switch the budget off).** Define, incorrectly,
the internal penalty as |N_ref(V)|. When T_2>2T, a class field can have
arbitrarily many cells in (2T,T_2]. A modification near one separate cell
that changes
whether max theta exceeds T_2 switches on all their tubes. Thus no bound
on the change of this penalty by a constant times the number of modified
plaquettes follows. Such a bound is needed by a local-energy argument.
Instead, use |N_pay(V)| in every *internal* loss. Only the fixed-top geometry
uses N_ref. In Step 4 one can weaken an estimate with |N_ref(W)| to one
with |N_pay(W)|: N_ref is a subset of N_pay and these terms are subtracted.

**Discharged (locality of the budget region).** Before brick rounding,
membership of y in tube(Y) asks whether every cell within d_x of y is
within 2d_x of Y. It therefore reads Y only within 3d_x of y. Outward
rounding to bricks adds at most a fixed multiple of t_0. Consequently

    |tube(Y) symmetric_difference tube(Y')|
       <= C_d (3d_x+C_d t_0)^4 |Y symmetric_difference Y'|.   (P4)

This is a finite-range set identity/count, not a proof of (LNC). It
removes the extra global switch from its proposed penalty.

## 3. The analytic comparison is still an input

**Gap (CI-paid^d), exact form required.** For every level i>=1, chain
c from U to V_i with the specified quiet data, let Z=Z_{i-1}(U) as in
the pinned (CI-N). The needed inequality is

    A_i^d(P(V_i)) <= A(U) - (1/16) A^Z(U)
                                   + C_W T^2 |N_ref(V_i)|. (CI-paid)

For a class V_i this is the original zero-error class-top (CI''') with
data. For a nonclass V_i it is (CI-N) with the wider, paid support.
It implies the weaker bound with N_pay(V_i) in place of N_ref(V_i).
The constants are uniform in data and depth, with C_W depending only on
the fixed absolute threshold ratio b_2 and the original absolute constants.

The paragraph proving (CI-N) at `relative-density-bound.md:281-285`
uses its support as follows: treat its inner blocks as dense; pay at most
C_s T_2^2 per target block; glue where the two parents agree and are
class; retain an inner collar; bound cost by the support's volume. All
these hypotheses hold for (P1). None requires that every support cell
itself be above T_2. Thus the **support substitution** is valid for that
argument if its analytic steps hold. It does not prove those steps,
especially their uniform-data version. In particular, the old theorem
as a narrowly worded black box is not logically the wider theorem.
Use (CI-paid) explicitly as the corrected analytic obligation.

**Implication (W1/W2 under named inputs).** Assume (CI-paid), the original
TE energy count with its Haar convention, the original patch replacement
gain uniform in quiet data, and the original trial, RF gluing, bump and
class-minimum inputs used for W1. Set V_i^#=P(V_i),
E_i=A(U)-A_i^d(V_i^#), and G_i=E_i-E_{i-1}. Then the same proof gives

    G_i >= -C_5(L) T^2 |Omega_i|,
    E_i >= (1/2) sum_{k<i} Delta_k^pi
                                  - C_W T^2 |N_pay(V_i)|, (P5)

where Omega_i includes the parent blocks meeting N_pay(V_{i-1}), R_{i-1},
and N_ref(V_i). The first uses equality of parents off the actual change
sets, which lie within these larger sets. The second averages the TE
gain from (CI-paid) and the sequential patch gains, exactly as in W2.
For a class V_i, use (CI-paid) with N_ref empty in both applications:

    E_i >= (1/2) sum_{k<i} Delta_k^pi,  if V_i is class.    (P6)

No energy optimality of a nonclass fill is asserted. Marks whose patch
gain fails are charged to R at the same or adjacent level by the pinned
rule. Conditional TE and these patch estimates, not the fill, pay them.

## 4. Own-level absorption, with constants displayed

**Discharged algebra; implication for the lattice.** Keep the exact W0
summation by parts. Substitute (P5) only with its nonnegative coefficients
<=C(L). Summing the W1 neighbourhood counts assigns at most a fixed
multiple of |N_pay(V_k)|+|R_k| to an internal level k, since a cell has
finitely many parents and each level appears only in adjacent W1 terms.
There is also a top remainder C_top(L) T^2 |N_ref(V_l)| from rho_{l-1}G_l.
Keep N_ref, not N_pay, in that term. It vanishes at a class top. At a
nonclass top enlarge Ecal_l so Ecal_l>=C_top(L) T^2 and include it in
Z's outer loss Ecal_l |N_ref(V_l)|. The *internal* loss can be enlarged to

    Lhat_{l-1}(c) = sum_{k<l} [ Ecal_k |N_pay(V_k)|
                       + C_4(L) T^2 (|N_pay(V_k)|+|R_k|) ],
    Ecal_k=C_E(L,a_*) d_x^4 log(e+x_k).                     (P7)

The reference at level zero is still U, not P(U); N_pay(V_0) in (P7) is
only a permitted overestimate of losses. No level-zero fill is required
by W0. All harmless neighbourhood multiplicities, envelope coefficients,
and the TE Haar-charge multiplicities are included in C_4,C_E.

By (P3), the cost per ordinary member of R_k is at most

    b(x_k)=v C_E d_x^4 log(e+x_k)+C_4(L) T^2(v+1).          (P8)

The analogous Haar cost has the already named fixed charging multiplier
and an adjacent x. Absorb that multiplier in b. After L,a_* are fixed,
b(x)/(x T^2) tends to zero. Choose x_* so for every x>=x_*,

    b(x) <= x c_T T^2/32,
    x >= 16 max(C_1(L), C_flow(L)),                        (P9)

where C_flow bounds adjacent |x_{k+1}-x_k|. This is possible independently
of volume and depth. For a transparent reserve for marks one may reduce
eps_q once so c_T>=24 c_S eps_q^2, strengthening the pinned factor 6.
This reduction is before t_0 and x_* are fixed.

At a class top use (P6). The bracket before losses supplies
(1/2) sum_k x-tilde_k Delta_k^pi, plus settled gains. Since
x-tilde_k>=15 x_k/16, an ordinary rough cell supplies at least
(15/32)x_k c_T T^2. Deduct the (1/32) loss reserve, at most one type-II
gain (1/8)x_k c_T T^2, and at most two charged type-I gains, each
<=(3/8)(17/16)x_k c_S eps_q^2 T^2. What remains is at least

    [15/32-1/32-1/8-51/(64*24)] x_k c_T T^2
       > (1/4) x_k c_T T^2.                              (P10)

An uncharged open type-I mark directly has coefficient >=15/32 of its
x_k c_S eps_q^2 T^2, which exceeds its required 3/8. Settled marks are
already explicit constants. The original bounded Haar allocation must
be applied before this per-paying-cell accounting. This calculation is
an implication under those gain/allocation hypotheses, not their proof.
Uncontrolled tails remain displayed, as in the original corollary.

For precision the W3 bound before the outer loss is combined is

    Trop >= x-tilde_{l-1} E_l
             +(1/2) sum_{k<=l-2}(x-tilde_k-x-tilde_{l-1}) Delta_k^pi
             -C_4(L) T^2 sum_{k<l}(|N_pay(V_k)|+|R_k|)
             -C_top(L) T^2 |N_ref(V_l)|.                  (P11)

Dropping that last term at a nonclass top would not follow from W0/W1.
At a class top it is zero even when Y(V_l) is nonempty.

**Discharged band check.** A label-0 cell in (T,2T] is neither in Y nor
necessarily in R, so it receives no automatic xT^2 term from this repair.
It can pay as a non-quiet marked brick under the patch hypothesis. A
labelled cell in that band is already in R. A cell in (2T,T_2] is in R
even when the whole field is class, and is counted at its own level in
Delta; it pays (P8) when it generates an internal budget tube. Modified
neighbours with smaller flux are charged to these generators by (P3).
Thus no new all-cells-above-T gain, and no two-level TE repair for the
unlabelled transition band, is asserted or needed.

## 5. Consumer scope

**Implication.** Use N_ref for Z's outer tube and N_pay(V_k) for (P7).
Step 4 reads the class field P(W_B) in VAL^d. Its coefficient identity
is unchanged; replacing its outer |N_ref(W_B)| loss by the larger
|N_pay(W_B)| feeds (P7). At a class top P(V)=V and N_ref=empty, while
(P6), not emptiness of Y(V), supplies the zero-error last step. Far
components outside N_ref have unchanged class parents: at a nonclass
top all cells above 2T are in N_ref, and at a class top all parents
already lie in D. This is exactly what the far-component use of DM
requires. The bracket at a nonclass top may still be negative with an
x-sized fill-energy term.

**Gap, unaffected by this algebra.** The frozen implementation of (FG),
(CI-paid^d), uniform W1 and patch gains, nested stability and C_J,
(LNC) for (P7), I^d/VAL^d and the other analytic inputs of Z remain at
their source status. Theorem DM additionally needs the stopped outer
integral and PAY/LMK estimates in `hard-core--dm.md`: the old volume
count is not repaired by changing a threshold. None of these conditions
is claimed independent of the others. The proposed replacements in the
threshold part are conditional text, not edits to those consumers.
