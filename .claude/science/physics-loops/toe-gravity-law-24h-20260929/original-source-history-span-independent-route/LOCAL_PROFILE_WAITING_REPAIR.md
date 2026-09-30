# One genuinely missing profile is separated by the actual complete loss

This is an analytical continuation of LOCAL_PROFILE_ATTEMPT. That note
finds an eleven-dimensional missing profile space for one local zero-gap
resolved-label family, including an explicit normalized eta. Here the
FULL original waiting operator is shown to separate that particular eta.
This is not a full eleven-dimensional rank theorem. No code was run.

## 1. Fix the actual geometry and complete words

Use h=0, spectator b0=e_y, outer birth center a=2e_y and its original
marked edge to b0. The complete outer jump is resolved+ or the original
coherent edge. Its selected component phi has its old B+ at v=3e_y,
as in the previous note. Do not replace the complete word by phi in the
evolution. Label the five empty h neighbors by

    1=e_x, 2=-e_x, 3=-e_y, 4=e_z, 5=-e_z.

Keep the eight-word eta and off-diagonal matrix x from(6) of the preceding
note. In particular x13=1,x14=-1,x23=-1,x24=1, other entries zero, and
eta is normalized by1/sqrt(8). All words are real in the actual electric
basis. Let B be the complete outer jump followed by the inner jump at
h on edge1. The latter is either resolved sign- or coherent.

We prove the exact matrix elements

    <eta,A_h R_2 B Omega>= sqrt(2)      (inner resolved-),
    <eta,A_h R_2 B Omega>=-sqrt(2)      (inner coherent). (1)

Both choices for the outer instrument give these same values, with its
complete original charge alternatives retained.

## 2. Loss at centers outside h

For a W0 input and an A center c with l_c empty B neighbors, the diagonal
matrix element of its complete loss R_c is

    2 l_c(l_c-1).                                      (2)

There are l_c legal old outward destinations; after the outward hop there
are l_c-1 vacant marked neighbors and two resolved signs. A coherent edge
has the same diagonal loss. A diagonal return uses the same edge and
charge, with unit rotor weights. On the selected phi block every
off-diagonal R_c with c!=h changes an outside-h-star electric edge,
so cannot contribute to eta after A_h. This observation will be corrected
for the other outer-word components explicitly in section4.

For inner input pair {i,k} among the five neighbors, the four occupied B
sites before A_h are {b0,v,i,k}. Summing(2) over c!=h gives a real number
q(i,k). If m_c is its occupied-neighbor count, then

    2(6-m_c)(5-m_c)=60-20m_c+4 binom(m_c,2).

Here sum_(c!=h)m_c=24-3=21. Two opposite h-star neighbors have only h as
a common A neighbor; perpendicular ones have one further common A.
The outside v=3e_y shares one A with b0 but none with the other five
h neighbors. Therefore, for one constant C independent of i,k,

    q(i,k)=C+4[f(i)+f(k)+g(i,k)],                       (3)
    f(3)=0, f(1)=f(2)=f(4)=f(5)=1,
    g(i,k)=0 for opposite directions,1 otherwise.

In particular q(1,4)-q(1,3)=4.

For the resolved- inner column v_i of the previous note, the input plus
pair is {i,k}; the final minus position j comes from the last hop. Its
pairing with eta after this diagonal outside loss is

    -(1/sqrt(8)) sum_(k!=i) q(i,k)[x_(k,i)+x_(i,k)].      (4)

This follows by summing x_(j,i)+x_(j,k) over j notin{i,k} and using both
zero column sums. At i=1 it is [q(1,4)-q(1,3)]/sqrt(8)=sqrt(2).

For the resolved+ inner column u_j, either member of the final plus pair
can have been the old outward destination. Its pairing is

    (2/sqrt(8)) sum_(i!=j) x_(j,i) q(j,i).               (5)

The factor2 follows by expanding the pair sums on the four sites other
than j, using the zero row sum. At j=1 this is-2sqrt(2). Thus the coherent
column u_1+v_1 gives-sqrt(2) from the centers outside h.

## 3. The h-center loss gives zero in this pairing

Each inner input has three occupied star B sites, hence three empty ones.
The exact local loss is R_h=4 F_h*F_h on that occupancy sector. Therefore
the contribution after A_h is4 F_h F_h* applied to the corresponding
output column u_i or v_i. Compressing to the30-row space with the
spectator B- retained, H=F_h F_h* has diagonal4 and unit off-diagonal
entries for moving one of the other three particles to either empty
site with its charge unchanged. A move of the spectator leaves this
compression; returning that spectator supplies one of the four diagonal
terms. Literal row counting gives

    H u_j=7u_j+sum_l u_l-2v_j,
    H v_i=6v_i+sum_l u_l-u_i                            (6)

within this compression. Thus eta, which annihilates every u_j and v_i,
also annihilates the complete h-loss contribution. This calculation keeps
all local charge transfers; it does not replace F_h F_h* by a number.

## 4. Restore every component of the original outer jump

There are four other outward destinations d of the outer center a,
besides v, with the marked b0 excluded. For its resolved+ component each
such word has outside field-1 on(a,d), instead of(a,v). The only loss
term that can change those exterior data into the eta block is R_a:
it first sends the A+ to v, then returns the B+ from d to a. Its matrix
element is6, since a initially has two occupied B neighbors and after
the outward hop has three empty marked choices, with two signs.

No newly filled h neighbor is a neighbor of a, apart from the fixed
spectator b0, so this6 is independent of every inner profile and mark
sign. The four missing outer components therefore contribute24 times
the SAME original local output column u_1, v_1 or u_1+v_1. Each has zero
pairing with eta. Other centers cannot alter the needed edges owned by
a, and A_h acts only on h's links, so there are no other exterior repairs.

For the coherent outer mark, the sign- branch has outside A_a- and
B_b0+. To reach the required exterior A_a+ it would also need R_a, but
the necessary outward hop from A_a- puts the wrong charge and opposite
field on(a,v). The final A_h cannot repair that exterior site or field.
Hence it contributes zero. This proves that equations(4)-(6) computed
from phi give the FULL-word values(1), not values for a substituted seed.

## 5. Actual positive-time separation and relevant adjoint range

Write L_2=-iKD_2+i delta Q_2-(kappa/2)R_2. All matrices, eta and B Omega
are real in the physical basis. The D and Q pairings therefore contribute
only imaginary parts to <eta,A_h L_2 B Omega>. Equation(1) proves

 Re <eta,A_h L_2 B Omega>=-kappa/sqrt(2)  (resolved-),
 Re <eta,A_h L_2 B Omega>= kappa/sqrt(2)  (coherent).    (7)

Since kappa>0, neither can vanish for ANY supplied positive K,delta.
The zero-order pairing is zero, but the actual amplitude
<eta,A_h S_2(t)B Omega> has a nonzero first derivative at0. Finite-field
domain estimates justify its Taylor remainder. It is consequently nonzero
at all sufficiently small positive t. These are boundary histories of
the actual two-birth block at total time t; continuity to positive initial
and intervening gaps supplies a positive-measure history neighborhood.
Thus <eta,A_h rho_2(s)A_h*eta>>0 for all sufficiently small positive s.
The already checked scalar alternative then makes it positive for almost
every s>0, with open dense positive set. No size of that weight is claimed.

This profile is also in the relevant post-source adjoint span. Let
K_(e,+)=F_h j_(h,e,+). Let psi_(j,e) be the physical full-star output with
b0-, minus sites j,e among E and plus on the other three E sites, keeping
the same exterior data. It is mixed and in the actual loss kernel.
Then K_(e,+)*psi_(j,e) is the sum of the three e_(j,{i,k}) rows whose
plus pair lies in E\{j,e}. Zero row sums give exactly

    eta=-(1/sqrt(8)) sum_(j!=e) x_(j,e)
                                      K_(e,+)*psi_(j,e). (8)

For a coherent edge, K_e* has the same action on these tests because
psi_(j,e) has B- at the marked e, killing its other sign component.
Thus(8) also uses original coherent labels. Since eta already belongs
to M_h, the actual range projection does not change this identity.

Equations(7)-(8) separate one previously missing physical, multi-profile
adjoint direction with the COMPLETE original dynamics. They do not prove
separation of its entire eleven-dimensional family, the whole local
profile range, arbitrary exterior fields or a common dark vector for
all source labels. In particular this does not establish generic fast
observability or close the full source-image criterion. It is a concrete
inter-center waiting mechanism that a larger quotient proof must retain.
