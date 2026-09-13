# Protected formation graphs and the infrared carrier

Working derivation, block02, 2026-09-13. Written before its dedicated checker.
Current main b8c9d9d819911c5f3fec98b23d53355e7ff8c8bf.
Provisional comparisons are PR8086 at a3e5529b4d74f618df416747c39bf150b885e495
and PR8087 at d568433b0fb323b8d72cc76f362ed3ead6b0b8d8.
This is a proposed common free carrier, not an interacting TOE or selected law.

## 1. The precise mismatch to test

The positive-star infrared unit uses the full cubic real skew matrix
K_(r,r+e_a)=h(-1)^(sum_(b<a)r_b), with every bond present.
The formation unit reserves all x bonds on odd-y rows and uses a DIFFERENT
real scalar hopping Hamiltonian on the remaining graph. Its nonzero current
does not identify its spectrum with the full-cubic Majorana bath.

First test the direct repair of simply putting the old pi-flux signs on that
remaining graph. In the phase-adjusted eight-site cell write
s=sin(k_x/2), t=sin(k_y/2), u=sin(k_z/2),
Gamma_x=X tensor I tensor I, Gamma_y=Z tensor X tensor I,
Gamma_z=Z tensor Z tensor X, P_even_y=I tensor (I+Z)/2 tensor I.
Up to the overall sign, iK/(2h) is

    A=s Gamma_x P_even_y+t Gamma_y+u Gamma_z.

Gamma_z anticommutes with the first two terms. Grouping the y parity and
conjugating the odd-y two-by-two x block by Z reduces the xy part to

    [[s X,t I],[t I,0]].

Its absolute eigenvalues are
r_±=(sqrt(s²+4t²)±|s|)/2. Hence the two positive frequencies, each twice, are

    omega_±=2h sqrt(u²+r_±²).

The lower branch vanishes on the entire line k_y=k_z=0. Away from k_x=0
its transverse y dependence is quadratic: r_-=t²/|s|+O(t^4).
The local lower-branch weight on an even-y Majorana is
w_-=(1-|s|/sqrt(s²+4t²))/2; the odd-y weight is 1-w_-.
Thus a line-node count alone is insufficient to identify a local star's
infrared measure. The full-cubic isolated-node formula cannot simply be
copied to this changed matrix. This statement concerns the specified direct
repair only; the next construction is a surviving alternative.

## 2. A staggered matching of candidate edges

Instead reserve y-oriented candidate edges whose tail r has r_x+r_y odd.
Every vertex is incident to exactly one candidate. Protect every other edge:
all x and z bonds, and y bonds whose tail has r_x+r_y even.
The protected degree is five at each bulk vertex and the graph is connected.
A candidate has a three-edge protected detour through its +x neighbor:
the other y edge of that plaquette has opposite tail parity. No detour
contains another candidate. Thus every finite interior candidate has a
native nonbridge cycle made of that candidate and protected edges only.

On the protected graph choose positive strengths h_x,h_y,h_z and the real
skew matrix

    K_(r,r+e_x)=h_x,
    K_(r,r+e_y)=h_y (-1)^r_x if r_x+r_y is even, otherwise zero,
    K_(r,r+e_z)=h_z (-1)^(r_x+r_y).

Roles, signs and strengths are supplied conditions. No covariant state
selection, physical clock or preferred anisotropy is derived.

## 3. Literal cell symbol and its complete spectrum

Use r=2n+s, s in {0,1}³, k in [-pi,pi]³, z_a=exp(i k_a).
The symbol is assembled from actual positive and negative neighbors:
each matrix element has the real-space signed hopping times z^cell_shift.
At z_z=1 its four-by-four xy matrix, ordered 00,01,10,11, is

    [[0,h_y,a,0],
     [-h_y,0,0,a],
     [b,0,0,h_y/z_y],
     [0,b,-h_y z_y,0]],

where a=h_x(1-1/z_x), b=h_x(z_x-1).
On the xy bipartition {00,11}|{01,10}, the off-diagonal block is

    Q=[[h_y,a],[b,-h_y z_y]].

On the unit torus b=-conjugate(a) and
det Q=4h_x² sin²(k_x/2)-h_y² exp(i k_y).
Both diagonal entries of QQ* and Q*Q equal h_y²+4h_x² sin²(k_x/2).
Their off-diagonal modulus is
4h_x h_y |sin(k_x/2)| cos(k_y/2).
The z term anticommutes with the xy matrix, so the positive frequencies
are, each with multiplicity two,

    omega_±² =
      h_y²+4h_x² sin²(k_x/2)
      ±4h_x h_y |sin(k_x/2)| cos(k_y/2)
      +4h_z² sin²(k_z/2).                              (2.1)

Assume 0<h_y<2h_x and h_z>0. The upper branch is gapped by h_y.
The only zeros of the lower branch are

    k=(±k_*,0,0), k_*=2 arcsin(h_y/(2h_x)).

Near either node its squared leading cone is

    (h_x²-h_y²/4) delta_kx² + (h_y²/4) k_y² + h_z² k_z². (2.2)

In virtual-site momentum units (cell length two), the three speeds are
sqrt(4h_x²-h_y²), h_y, 2h_z. They are equal for

    h_x=sqrt2 h, h_y=2h, h_z=h, h>0.                    (2.3)

Then k_*=pi/2 and omega_-=h|delta_k|+O(|delta_k|²) in cell units.
These tuned strengths are explicit conditions; equal cone slopes do not
derive a Minkowski time, Lorentz symmetry beyond the free germ, or dynamics
from a primitive. Boundary h_y=2h_x merges the nodes and is excluded;
h_y=0 and h_z=0 also have different zero sets and are excluded.

## 4. Local positive-frequency measure, not just dispersion

Let Pi_- be the projector onto both signs of the lower frequency.
The equal diagonals of QQ* and Q*Q imply Pi_- has every diagonal entry1/2
away from the measure-zero branch-degeneracy set. Adding z leaves those
singular subspaces invariant. The physical bipartite grading
(-1)^(s_x+s_y+s_z) anticommutes with iK and commutes with Pi_-.
Therefore the diagonal of (iK/omega_-)Pi_- vanishes, and the lower positive
projector has diagonal1/4.

In the pure Majorana Gaussian reference, a local gamma_s has squared
one-particle coefficients summing to twice this positive-projector diagonal.
Its lower-branch weight is consequently exactly1/2 for EVERY cell site.
The upper branch supplies the other1/2. These identities are projectors
on nonzero frequencies; no value is assigned at an isolated zero.

For E<h_y define mu_s([0,E]) as the one-particle energy measure of
gamma_s Omega. It is independent of s and equals

    (1/2) integral_(omega_-<=E) d³k/(2pi)³.             (2.4)

Two nodes and their local weight must both be counted. To derive the volume,
near each node use the EXACT coordinates

    U=2h_x |sin(k_x/2)|-h_y cos(k_y/2),
    V=h_y sin(k_y/2),
    W=2h_z sin(k_z/2).

Then omega_-²=U²+V²+W². The Jacobian determinant at either node is

    D=h_y h_z sqrt(4h_x²-h_y²)/4.

The inverse Jacobian is smooth in these two disjoint charts. Its linear
Taylor terms integrate to zero on the symmetric energy ball. Thus

    mu_s([0,E])=E³/(6pi² D)+O(E^5).                     (2.5)

The upper branch is absent below h_y. Compactness excludes further low-energy
regions outside the two charts. For the isotropic choice(2.3), D=h³ and
the coefficient is exactly the same local coefficient E³/(6pi²h³) as the
full-cubic pi-flux model, although the nodes, degrees and hopping strengths
are different. This coincidence has been derived from the projector and
Jacobian, not imposed as an expected coefficient.

For that choice, E<=h/4 lies entirely in the two charts. The inverse
Jacobian there is

    8 / [sqrt(8h²-(U+sqrt(4h²-V²))²)
         sqrt(4h²-V²) sqrt(4h²-W²)].

On the energy ball its value lies between1/(2h³) and2/h³:
sqrt(4h²-V²),sqrt(4h²-W²) are between7h/4 and2h;
the first radical is greater than3h/2 and at most2sqrt2 h.
The lower product bound gives inverse Jacobian<256/(147h³)<2/h³,
while its upper bound gives inverse Jacobian>=1/(sqrt2 h³)>1/(2h³).
The inverse formulas keep |k_x| strictly inside(0,pi), so there is no
missing chart branch. Consequently

    E³/(12pi²h³) <= mu_s([0,E]) <= E³/(3pi²h³),
    nu([0,E])=4 mu_s([0,E]), 0<E<=h/4.                 (2.6)

Here nu counts positive-frequency bands per eight-site cell in ONE real
Majorana sector; the lower band has multiplicity two. The factor4 is also
obtained by summing2(P_+)ss over8sites. Do not confuse nu with a local source
measure or with the doubled complex-CAR excitation count.

## 5. Common native Hamiltonian without unused zero-mode matter

Using only one Majorana per complex CAR site would leave its partner inert.
Instead put the SAME K on both Majorana species:

    H=(i/4) sum_(v,w) K_vw
      (gamma_(2v) gamma_(2w)+gamma_(2v+1) gamma_(2w+1))
     =sum_(v<w) i K_vw(c_v* c_w-c_w* c_v).

The one-particle complex hopping is iK. Its native expression is a sum of
protected terms -K_vw A_vw(I-B_v B_w)/2. Thus it belongs to the actual
protected even algebra; both real Majorana sectors have the displayed
nontrivial dispersion. The imaginary hopping and common energy convention
are explicit choices. A real scalar-hopping current from PR8087 is not
silently substituted for this Hamiltonian.

All scalar-effect native cycle pulses in the formation construction commute
with this H and intertwine its complete protected state functional branch
by branch. This follows for any polynomial in the protected A,B, not just
real hopping T. The candidate cycles still contain only one candidate.
The transverse program graph with at least two odd physical coordinates,
digital kernel and supplied enabling clocks of PR8087 remain disjoint from
native edges. Each candidate has exactly four transverse program neighbors.
Candidate tails are distinct, so its optional all-even fuel site remains
unshared. Its induction and nonexplosion mechanism therefore apply to the
new candidate set after rechecking the literal geometry.

These scalar effects provide a varying local program law and preserve matter;
they are not informative about matter. BLOCK01 supplies a finite informative
interface on a different graph. Combining informative readout, this carrier,
and arbitrarily growing supported local histories is still a separate target.

## 6. Finite parity-compatible realization of a supplied reference

The infinite pure Gaussian reference is mathematical; no infinite native
cycle-code state is presumed. For a finite connected protected bulk graph,
let rho be ANY finite density commuting with bulk fermion parity Pi.
For example, it can be the finite marginal of the doubled Gaussian bath.
Write rho_±=P_± rho P_±. Add one boundary spectator fermion with an idle
protected graph edge (zero hopping), and prepare

    rho_ext=rho_+ tensor |0><0|+rho_- tensor |1><1|.

It is positive, normalized, has even TOTAL parity, and has bulk marginal rho.
The native connected code realizes it by the faithful even-CAR dictionary.
Every bulk even observable and its correlations are unchanged; no
postselection or lower bound on marginal occupation eigenvalues is needed.
The boundary spectator does not introduce an inert species at every bulk
site. Its vertex, zero hopping and preparation are stated finite resources.

On finite observation windows, one-particle propagation in the compressed
Hamiltonian converges to the infinite protected one by the exponential-series
boundary estimate, now with
||iK||<=2h_x+h_y+2h_z=(2sqrt2+4)h<7h under(2.3).
If each observed endpoint is at graph distance d from the exterior,
the propagator-vector error for |t|<=T is at most
2 sum_(n>=d) (7hT)^n/n!.
A covariance entry differs by at most four times that tail, because the
initial finite marginal is exact. The parity extension adds no covariance
error. The idle boundary link does not affect the Hamiltonian powers.

This approximates finite-time bulk even correlations and scalar-preserving
formation histories. It does not identify finite-box spectral projectors
uniformly at zero or establish an interacting thermodynamic limit.

## 7. Author evidence and next frontier

check_block02.py passes90 exact checks. It builds the literal eight-site
Laurent matrices for both patterns, compares the row deletion to its Clifford
form, checks the matching squared-symbol and projector identities, and checks
the tangent anticommutators at both isotropic folded nodes. It also checks
the chart Jacobian,60candidate detours in a125vertex fixture, four actual
program neighbors, doubled Majorana/native current normalization, and parity
extension on a coherent mixed-parity density. The initial missing brace and
actual parser failure are preserved; no mathematical check preceded that fix.

The infinite measure follows from the displayed change of variables, not a
fitted exponent. The author reread the complete proof and checker; independent
review is pending. No retained or negative-packet PASS is asserted.

The first direct-repair failure leaves the matching construction alive and
cannot force an axiom update. The positive-star scalar and90-term transition
from the six-leg full-cubic bath are NOT transferred by an E³ local density.
The protected matching graph has five hopping legs per bulk vertex, different
defects and two nodes. Its interacting transition, source amplitude and
positive defect resolvents require a new proof or a different carrier design.

An additional author calculation unfolds the z period from two sites to one.
The4x4 symbol is iK_xy-2h_z sin(q_z) diag(1,-1,-1,1). The two folded
four-dimensional cones are four two-dimensional crossings at
(k_x,k_y,q_z)=(+/-k_*,0,0 or pi), with tangent chiralities
-sign(k_x) cos(q_z). This extra calculation is not part of the frozen90-check
result. A theorem for exactly two Weyl nodes cannot be transferred using the
folded momentum count. A direct protected-path embedding of a model matching
the literature theorem is the next route under investigation.
