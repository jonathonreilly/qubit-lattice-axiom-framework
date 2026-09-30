# Larger physical profile quotient: an exact local-label obstruction

This is an attempted extension beyond one winding/local-profile tower.
It preserves all earlier frozen proofs. The conclusion is a finite exact
failure of a proposed shortcut, not a failure of actual Omega reachability.
No computation or replacement initial preparation is used.

## 1. The attempted local spanning lemma

A tempting next step would be: after producing a physical star seed,
vary all original local birth labels and append the first hop; their
images should span the local first-hop range in that exterior block.
The following actual five-site profile calculation refutes this claim.
Waiting dynamics and control through other centers cannot be omitted.

Fix h=(0,0,0), L>=8 even, and its B neighbor b0=e_y. Start with the actual
ordinary original mark at a=2e_y on the edge a->e_y, resolved sign+ or its
complete coherent edge label. In its COMPLETE action on Omega, select
only for coefficient analysis the outward component a->3e_y with the
positive old charge. The resulting physical word phi has h+, B- at b0,
B+ at3e_y, all A+, and fields+1 on(a,b0),-1 on(a,3e_y). All six h-star
fields are zero. This word satisfies the actual Gauss law and occurs with
coefficient1.

Let Pi_ext project onto exactly its charge/electric data outside h's star.
These data distinguish the chosen old destination and the resolved sign:
any other outward component changes an outside field; the other coherent
sign changes the outside A charge at a. Hence

    Pi_ext b_(a,edge) Omega=phi.                         (1)

Equation(1) is a proof-space projection of the complete actual history,
not a newly supplied preparation or an observed extra label. All later
operators in this calculation act only on h's star and commute with this
exterior projection. Thus the resulting columns are exact projections of
legal complete zero-gap histories from Omega. They are not claimed to
include histories with nonzero waiting gaps.

Label the five other, initially empty B neighbors of h by E={1,2,3,4,5}.
After one ordinary birth at h and the appended first hop, b0 remains B-;
among E there are two B+ sites and one B- site. Write the normalized row
word as e_(j,{i,k}), with j the minus site and {i,k} the unordered plus
pair, all three distinct. There are5*binom(4,2)=30 rows.

These are actual physical words in ONE exterior block. For any final
star charge profile q, the six B Gauss equations fix

    E_hb(final)=E_hb(phi)-(q_b(final)-q_b(phi)).          (2)

The same final charge profile therefore has the same actual electric
fields, irrespective of the order of the two outward hops. The h Gauss
equation follows because the total star charge is conserved. No phases
on configuration edges are independently assigned.

## 2. Exact complete columns and their rank

Let u_j be the column A_h b_(h,j,+)phi and v_i the column
A_h b_(h,i,-)phi, where A_h=F_h P_(h,3). The intermediate ordinary birth
leaves exactly three occupied B neighbors, so the projection acts as1.
The old h charge is+. Literal full hopping and (2) give

    u_j=2 sum_{ {i,k} subset E\{j}, |{i,k}|=2 } e_(j,{i,k}),
    v_i=  sum_{ j!=i } sum_{ k notin{i,j} } e_(j,{i,k}). (3)

For u_j the marked B- is j; the two identical B+ outward hops can occur
in either order, giving2. For v_i the marked B+ is i, the old B+ goes to
k, and the newly made A- goes on the final hop to j; that assignment has
coefficient1. Every legal path is included. With the original unnormalized
coherent edge instrument the column is exactly u_i+v_i.

A linear combination sum_j alpha_j u_j+sum_i beta_i v_i has row

    2 alpha_j+beta_i+beta_k.                            (4)

It vanishes in all30 rows iff all beta_i equal one beta and every
alpha_j=-beta. Indeed, fixing j makes all pair sums of the other four
beta's equal; their pairwise comparisons force those four beta's equal,
and varying j forces equality of all five. Thus the resolved ten-column
family has rank9, with sole relation sum_i u_i=sum_i v_i.

For a coherent combination sum_i gamma_i(u_i+v_i), (4) becomes
2 gamma_j+gamma_i+gamma_k. The same pair comparison makes every gamma_i
equal; the remaining equation4 gamma_i=0 then makes all zero. The five
coherent edge columns have rank5.

## 3. The genuine first-hop range is already at least20-dimensional here

Keep the spectator B- at b0 and the same physical exterior data. For each
j in E and i!=j let d_(j,i) be the valid input word with h+, additional
B- at j and B+ at i, the other three E sites empty. It has exactly three
occupied star B sites and the same global H_2 input numbers as the actual
two-birth history above. Equation(2) defines its physical fields, with
the h charge retained rather than vacated. Its actual first-hop image is

    A_h d_(j,i)=sum_{k notin{i,j}} e_(j,{i,k}).          (5)

For fixed j, (5) is the vertex-to-edge incidence map of K4. If its four
column coefficients x_i satisfy x_i+x_k=0 for every pair, any triangle
forces all x_i=0. Its rank is4. Different j give orthogonal row blocks,
so these actual range vectors span a20-dimensional subspace M0 of M_h
inside the stated30-dimensional profile space.

Therefore neither the rank9 resolved family nor the rank5 coherent family
can span even M0, much less the whole first-hop range. This is a physical
range comparison, not just a count of formal charge labels.

## 4. One explicit coherent missing profile

The obstruction can be displayed as an actual eight-word vector. For
off-diagonal indices j,i in E, choose

    x_(1,3)=1, x_(1,4)=-1, x_(2,3)=-1, x_(2,4)=1,
    all other x_(j,i)=0,
    eta=8^(-1/2) sum_(j,{i,k}) (x_(j,i)+x_(j,k)) e_(j,{i,k}). (6)

There are exactly eight nonzero coefficients,+/-1, so eta has norm1.
Equation(5) shows eta in M0. Both the row sums and column sums of x are
zero. Hence, using the complete columns(3),

    <eta,u_j>=0 for every j,
    <eta,v_i>=0 for every i.                            (7)

Explicitly the u_j pairing is proportional to3 sum_i x_(j,i), while the
v_i pairing is proportional to sum_(j!=i)[2x_(j,i)+sum_k x_(j,k)]. Both
vanish. The vector therefore also annihilates every coherent u_i+v_i.
All cancellations in (6)-(7) are between Gauss-glued physical field words.

More generally the off-diagonal five-by-five matrices x with zero row
and column sums have dimension20-9=11; their images under (5) give an
11-dimensional resolved-family annihilator inside the actual range M0.
This is not an invisible subspace for the full original generator.

## 5. What this attempt does and does not resolve

The explicit eta is invisible to the specified local zero-waiting family
from the exact projected one-birth Omega history. It has NOT been shown
orthogonal to histories with waiting evolution, other initial labels,
births at other centers, or their full closed span. Pi_ext is an unobserved
proof projection; it is not an added selective preparation instrument.

The calculation defeats a proposed finite local-label completion of the
larger profile quotient, even in a source-relevant small number sector.
It does not defeat the actual first-hop density conjecture. Its concrete
next obligation is to show that the full no-event/birth control algebra
separates these eleven profile directions (or to exhibit a genuinely
invariant actual-history annihilator), with all couplings through other
exterior blocks retained. Declaring graph connectivity or taking a formal
star source right inverse does not supply that missing step.

No computational rank, generic-phase assumption, spin/volume limit,
global no-go, formal review or audit is asserted. The existing faithful
winding-tower result remains valid and does not answer this multi-profile
control question.
