# An actual stabilizer-breaking history separates eta_o on a parameter cone

Use the exact physical eta_o and geometry of8bf145d7: h=0, a=2e_y,
b0=e_y, v=3e_y, and empty-star labels1=+e_x,2=-e_x,3=-e_y,4=+e_z,5=-e_z.
Keep the same vector eta_o, exterior data and Gauss-glued30-row space.
Change only the original observed history labels: the outer coherent
mark is now a->d with d=(1,2,0)=a+e_x, and the inner coherent mark at h
is on edge4. Denote their complete ordered product by B'. It acts on
the actual bare Omega. Both labels are allowed original channels.

The two reflections no longer fix one common reflection of every such
history: the outer label breaks x reflection and the inner one breaks
z reflection. Absence of that symmetry obstruction alone is NOT used
as evidence of reachability. The following exact coefficient supplies it.

## 1. Full two-loss coefficient

We claim

    <eta_o,A_h R_2^2 B' Omega>=-24/sqrt(8).              (1)

An electric-support check makes this small calculation complete. Every
outer component initially has nonzero field on(a,d), while the test
exterior has zero field there. Only a loss centered at a can alter that
edge: each link is owned by its A endpoint. A_h acts only on h's links.
Thus at least one of the two loss factors must be R_a.

If both factors are R_a and/or R_h, their full pairing is zero by a
local symmetry. On the union of these two stars, interchange the h
neighbors+e_x and-e_x, and their h-link fields, keeping all a-star
vertices and exterior data fixed. The two stars share only b0. This is
a legal permutation of the relevant physical Gauss blocks, since all
outside fields incident to those two h neighbors are zero. R_a, R_h,
the inner edge4 and the complete outer word are invariant under this
interchange, whereas eta_o is odd. The statement includes all diagonal
and off-diagonal paths of these factors, not only chosen returns.

For a second center c other than a,h, an off-diagonal R_c changes two
outside h-star edges owned by c. Neither R_a nor the final A_h can
restore them. Hence R_c must be diagonal in every contributing path.
We may sum its exact diagonal2 l_c(l_c-1) as in33ad6409. Adding the
diagonal terms at a and h to this sum is harmless: their contributions
are separately zero by the same internal interchange.

With just one off-diagonal R_a, there is exactly one outer component
that can reach the prescribed exterior data. It is the original
coherent sign- branch with old outward destination v: initially A_a-,
B_d+,B_v+, and fields-1 on(a,d),-1 on(a,v). R_a sends A_a- to the empty
b0 and returns B_d+ to a. This yields A_a+,B_b0-,B_v+, fields+1 on(a,b0),
-1 on(a,v), and zero on(a,d), exactly the required exterior. Its complete
off-diagonal loss coefficient is6: after the outward hop there are
three vacant marked neighbors and two original signs.

No other outer component can reach this exterior with one R_a. A
different old destination leaves a wrong occupied outside site/field;
the outer sign+ cannot both supply B_b0- and restore A_a+. Those branches
can require two non-diagonal a/h factors, already canceled by symmetry.
This explicitly retains the complete outer coherent word.

Only the inner sign- component contributes to the remaining diagonal
calculation: its marked B+ is4 and its old B+ is i. The first hop later
puts A_h- into the minus position j. The inner sign+ leaves its minus
at4, outside eta_o's row support. Before and after the a-transfer, the
occupied B sets for the sign- component are respectively

    S_before={d,v,i,4},       S_after={b0,v,i,4}.         (2)

The contributing i are1,2,3,5, all disjoint from a's other neighbors,
so the transfer coefficient6 is independent of i. For any such set S,
the sum of all local diagonal losses is

    q(S)=60n-20 sum_c m_c+4 sum_c binom(m_c,2),         (3)

where m_c counts occupied B neighbors. Here sum_c m_c=24. The last
term is4 times the sum of common-A-neighbor counts over unordered B
pairs in S. The geometry gives

    q(S_before,i=1)-q(S_before,i=2)=4,
    q(S_after,i=1)-q(S_after,i=2)=0.                    (4)

Indeed d and1 differ by2e_y and have one common A; d and2 have no
common A. All other pair contributions to this difference cancel.
The after set is symmetric under x reflection.

For the complete inner sign- edge4 column, eta_o's pairing with a
diagonal weight q(i) is [q(2)-q(1)]/sqrt(8). The i=3 row contributions
cancel between its two possible minus positions, and i=5 gives zero.
The two chronological positions of the diagonal loss consequently give

    (6/sqrt(8))[-4+0]=-24/sqrt(8),

proving (1). All other paths have been removed by the owned-edge support
or actual local-interchange argument, not by an assumed independent seed.

## 2. What the full Hamiltonian derivative proves

Let

    P(K,delta,kappa)=<eta_o,A_h L_2^2 B' Omega>,
    L_2=-iKD_2+i delta Q_2-(kappa/2)R_2.                (5)

This is a finite homogeneous quadratic polynomial in the three supplied
real parameters: B' Omega and every fixed-order derivative have finite
electric support. Equation(1) gives its exact coefficient

    [kappa^2]P=-6/sqrt(8)=-3/sqrt(2).                  (6)

Therefore P is not identically zero. For each fixed kappa>0 its zero
set in positive(K,delta) is contained in the zero set of a nonzero real
polynomial (use the squared absolute value), and has measure zero and
empty interior. This follows by induction/Fubini from the finite-root
property of one-variable polynomials. At every positive triple with
P!=0 the complete actual amplitude
<eta_o,A_h S_2(t) B' Omega> has a nonzero derivative of order at most2.
Its zero-order pairing vanishes by its exterior field. Hence it is
nonzero for all sufficiently small positive t. Positive interior-gap
neighborhoods and the original history expansion give a strictly
positive actual first-hop density pairing at those small total times.
The checked scalar alternative extends positivity to almost every
positive source time, with open dense positive set.

This is GENERIC-PARAMETER separation, not an assertion that the unknown
remaining quadratic coefficients cannot cancel(6) at exceptional triples.
No actual coefficients of Q^2 or the mixed terms have been computed here.

## 3. An explicit, deliberately small positive parameter cone

A sufficient cone can be stated without those other coefficients. The
initial B' Omega has electric l1 support at most4; two generator factors
give at most12. Compressing intermediate operators to that field ball
therefore preserves(5). On it D<=2(1+12)^2=338. Use the landed safe
bounds ||Q||<=38880n, ||R||<=300n, ||A_h||<=6 and ||B'Omega||<=100.
Put q=338K+38880n delta. Expansion of L_2^2 gives

    |P+(3/sqrt(2))kappa^2|
           <=600 [q^2+300n kappa q].                  (7)

For positive K,delta satisfying

    338K+38880n delta <= kappa/(10^6 n),                (8)

the right side is at most(0.180000001)kappa^2, strictly less than
(3/sqrt(2))kappa^2. Thus P!=0 throughout this explicit cone. The
finite-volume bound is intentionally coarse, not a physical choice of
parameters and not a fixed-coupling thermodynamic assertion.

## 4. Scope of the actual enlargement

The old fixed-axis history family remains exactly blind to eta_o for
all parameters. This changed pair of ORIGINAL labels breaks that family
and, by(1)-(8), separates the same genuine first-hop/source-adjoint
profile on the stated parameter set. The law and bare preparation were
not changed. The coherent outer sign- branch is essential to this short
two-loss mechanism; a resolved+ outer branch is not silently substituted.

This does not separate every profile in the eleven-dimensional local
kernel, prove a full local or global history-image rank, eliminate an
actual fast invariant module, give a time/rate/weight uniform in volume,
or establish all-positive-parameter separation. It is a finite explicit
geometric enlargement with its remaining parameter exception stated.
No scientific computation, formal review, audit or separate milestone
is claimed. A focused check of this complete coefficient is required
before reuse.
