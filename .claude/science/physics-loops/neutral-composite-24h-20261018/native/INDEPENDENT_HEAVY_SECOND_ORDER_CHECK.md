# Native N2 second order: singleton identity and half-column correction

Focused check of `/tmp/neutral_probe_second_order.py`, the proposed operator inequality, and completeness of N2 channels for longitudinal period four. The comparison is relative to the second-order aligned vacuum energy. No uniform growing-box remainder or selected defect radius is established here.

## 1. Singleton block identity

Write Tx for the native x hopping, with entries -1, and Ty for y hopping, with entries -s_i s_j in a fixed aligned-column background. Both are Hermitian and have norm <=2. The first-order operator is T=Tx+Ty.

The second-order native result is

    D2=-(Tx-Ty)^2/8.

The root code correctly excludes intermediate N2 states and uses the unperturbed resolvent denominator 4-2N_mid. Its +number_of_bonds/8 diagonal subtraction removes the vacuum's -1/8 per transverse-bond second-order energy.

The channel structure can also be read locally. On the singleton's layer, a first ordinary hop is an intermediate P transition and excluded; reverse ordering of a two-step path creates three singletons and has denominator -8. This gives axial-distance-two coefficient -1/8 and mixed-path coefficients with the native YY phase, +phase/8 per path. In a flat background the two mixed paths sum to +1/4; nonflat flux can change or cancel their sum. The diagonal is -1/2: the four omitted same-layer virtual bonds add +1/2 relative to vacuum, while four incident bonds on each of the two neighboring layers change their denominator from -8 to -4 and contribute -1 in total. The opposite layer contributes no diagonal difference.

At order two a singleton cannot change its majority aligned-column background: a distinct two-column background change together with the moved singleton would require at least six spin flips, while two transverse insertions flip at most four. Length-three N2 intervals are singleton configurations relative to the opposite majority column, not an additional independent branch.

## 2. Noncommuting operator inequality

Set A=Tx+2I and B=Ty+2I. Then 0<=A,B<=4I. No commutativity is needed for

    (A-B)^2 <= 2A²+2B² <=8(A+B),

because the difference in the first inequality is (A+B)^2>=0, and the second follows separately from the spectral bounds on A and B. Therefore

    T+lambda D2 >= -4I+(1-lambda)(T+4I) >=-4I

for 0<=lambda<=1. In a flat background the signed constant ground wave has Tx=Ty=-2, so D2 annihilates it and equality is attained. Hence the singleton truncated band bottom has no order-lambda² shift. This is an exact bound for T+lambda D2, not a bound on all higher native terms.

## 3. Half-column sector: eight moves, not four

The full periodic-four N2 sector also contains intervals of length two. They have even total spin-flip parity, whereas singleton/length-three states have odd parity. Native two-spin bonds conserve total parity, and the stronger z-plane parity pattern also distinguishes the sectors. Thus singleton and half-column sectors cannot mix at D2 or at any order.

The half-column first-order block is zero, but its second-order dynamics cannot be described using only a fixed aligned background. Direct physical backward/forward two-bond enumeration on a 5x5x4 torus, starting from a half interval {z=0,1}, gives:

    diagonal D2=-2;
    eight distinct off-diagonal outputs, each -1/2;
    row sum=-6.

The four familiar moves transfer the occupied half interval to a neighboring column. Four additional moves flip the complementary half at that same neighbor pair: the old column becomes fully reversed and the neighbor carries the complementary half interval. These are distinct physical output configurations. They are lost if the aligned background is artificially fixed.

The scratch control is `/private/tmp/neutral_halfcolumn_second_control.py`, obtained by using the root physical two-bond enumerator with a half-column initial bit pattern; it printed all eight targets. For example an x-neighbor move gives either [old column 0000, neighbor 0011] or [old column 1111, neighbor 1100]. Both paths have two intermediate orderings with denominator -4, hence -1/2. YY products have the same positive squared spin phase for these paired-layer operations.

Each of the sixteen transverse bonds incident on the old column has denominator -4 rather than the vacuum -8, giving diagonal -2. All other virtual diagonals cancel the vacuum subtraction. At this order the two inserted bonds must be on the same transverse edge and either the occupied or complementary two layers to leave a single N2 column. Mixed inside/outside choices leave additional walls. This exhausts the eight moves on a nondegenerate transverse graph.

The half block is therefore bounded below by -6 in D2 units by its row sum (and its finite regular connected components attain that value with the uniform positive vector). Its first-order-plus-second-order energy correction is bounded by -6lambda², not -4lambda².

## 4. Consequences and scope

For the whole N2 truncated operator the comparison is

    correction >= min(-4lambda,-6lambda²).

For 0<=lambda<=2/3 the singleton bottom -4lambda remains the lower one. In an odd global-spin-parity sector the half states are absent entirely, and the singleton lambda<=1 bound applies without this qualification.

This corrects any all-N2 use of the singleton lambda<=1 statement. It does not obstruct the root's weak-lambda argument, which only needs sufficiently small lambda and a bounded half-sector coefficient. Higher-order terms, joint growing-box control, and the proposed variational flux-patch radius remain separate estimates; no selected radius or heavy-sector gap asymptotic follows from this second-order identity alone.
