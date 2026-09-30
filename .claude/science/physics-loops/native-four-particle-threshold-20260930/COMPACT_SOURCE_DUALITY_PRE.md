# Compact-source threshold forms from actual removal amplitudes

Author simplification for focused checking before incorporation. This is a
proof candidate, not a review verdict. The previous threshold proof remains
unchanged in its original campaign packet. Actual model source is main
30a9461ee19a49b99fa6628fe942f08e504e8903, native density note SHA256
7180c065165cb5db45f3405fcc9711ec38145a3d2391962ed767d55f4cc25ee0.
Selected procedures remain7146fe17a76de41badcaca3c3c7cac6d11eb2a00.

## Exact joint form and physical coordinates

Use the supplied full-qubit H0, fixed mu,tau>0, infinite Z3, N=4, K=0.
The Hilbert space is l2 of actual unordered four-site translation orbits.
Every finite occupation has trivial infinite translation stabilizer. Write
a=min(tau,mu/12). The actual positive decomposition is H=S+mu D+W.
The landed gradient proof bounds S+W>=a Egrad15 BEFORE adding mu D.
Thus its equation(5) is the simultaneous form inequality

 E(psi)>=a Egrad15(psi)+mu<D>_psi.

Translate axial midpoint fields to forward anchors and discard one of the
two identical gradient copies of each plane edge. This leaves Egrad9.
Retain in each annihilation output only residual graph edges. Let d,e run
over the nine forward graph displacements 2e_i,e_i+/-e_j. Define

 (T psi)_(d,e)(r)=psi({0,e,r,r+d})

when the four sites are distinct, and zero otherwise. This field is NOT
divided by sqrt2. Each graph-residual translated output contributes once
after the ordinary K=0 orbit normalization. The physical gradient sum
therefore bounds sum_(d,e,r,j)|delta_j(T psi)_(d,e)(r)|^2.

Let Q_nm be the diagonal projection onto configurations without a perfect
matching of graph edges. A four-vertex graph with no perfect matching has
an isolated vertex or is a three-leaf star; in either case
D=sum_vertices(deg-1)(deg-2)/2>=1. Consequently the simultaneous inequality is

 E(psi)>=a sum_(d,e)||gradient(T psi)_(d,e)||_2^2
                                  +mu||Q_nm psi||_2^2.       (D1)

The two terms in(D1) were not added from separate bounds on H. They came
from disjoint positive parts S+W and mu D of its exact decomposition.
All statements first hold on finite orbit support. They also follow by
translating such a vector over expanding physical cubes and dividing its
positive quadratic forms by the number of translations. No almost-everywhere
direct-integral assertion is needed at the particular momentum K=0.

## An exact adjoint lift for every compact physical source

Split a finite-support orbit source r into r_P+r_Q by physical perfect
matchability. If S has m(S) perfect matchings, it has exactly2m(S) ordered
decompositions into two graph edges. For each ordered decomposition put its
residual edge in forward form{0,e} and its removed edge in form{r,r+d}.
Assign the field g_(d,e)(r)=r_P(S)/(2m(S)).

These coordinates are distinct: a repeated coordinate would identify the
two ordered decompositions by a nonzero translation stabilizing the finite
four-set, or would be the identical ordered decomposition. A coordinate
cannot belong to two different physical orbits. Hence

       sum_(d,e,r) conjugate(g_(d,e)(r))(T psi)_(d,e)(r)
                              =<r_P,psi>.                   (D2)

This uses all physical matching amplitudes, including multiple matchings
in the collision core. It never treats them as independent physical states.
The field g is finite because r has finite orbit support.

Let ell(k)=2sum_j(1-cos k_j), with normalized Brillouin measure, and
G_lat=ell^-1 as a quadratic form on finitely supported lattice sources.
In three dimensions ell>=4|k|^2/pi^2, so

 g0=integral_BZ ell(k)^-1 dk/(2pi)^3<=sqrt(3)pi/8<infinity.

Fourier Cauchy gives |<g,f>|^2<=<g,G_lat g>||gradient f||_2^2.
Apply it to(D2), and apply ordinary Cauchy to r_Q. Joint Cauchy on the
direct sum of these weighted output spaces, followed by(D1), gives

 |<r,psi>|^2<=C(r) E(psi),
 C(r)=||r_Q||_2^2/mu+(1/a)sum_(d,e)<g_(d,e),G_lat g_(d,e)>.
                                                               (D3)

One may further bound each Green term by g0||g_(d,e)||_1^2.
There is no identical-pair normalization factor in(D2)-(D3).

## Compact-source resolvent and physical energy completion

The actual bounded nonnegative realization satisfies 0<=H4<=16mu+144tau.
The number term is4mu, V3<=12mu, and the positive pair-gradient N2 norm is
at most24tau; conditioning on each residual pair gives its N4 norm at most
6*24tau. These bounds give the stated upper bound while S+mu D+W gives
positivity. Finite orbit support is dense in l2 and therefore in its energy
norm. Equation(D3) extends to all l2 by boundedness of H and ordinary l2
approximation.

For epsilon>0, the variational resolvent identity and(D3) imply

 0<=<r,(H4+epsilon)^-1 r>
    =sup_psi[2Re<r,psi>-E(psi)-epsilon||psi||^2]<=C(r).    (D4)

The quadratic values increase as epsilon decreases to zero, so every compact
source has a finite limit. Complex polarization defines the corresponding
bilinear form G_H(0) on all compact sources. This is a form/domain assertion,
not a bounded inverse on the full l2 space. In particular(D3) with each
coordinate delta shows that no nonzero zero-energy l2 vector exists.

Complete finite physical orbit vectors in the energy norm. Equation(D3)
makes every coordinate evaluation continuous. An energy-Cauchy sequence
therefore has a pointwise physical coefficient limit. Every actual positive
row has finite support, so its value on that limit equals the limit of the
row values; their l2 sequence is the energy-completion representative. If
all physical coefficients vanish, every row vanishes and the energy element
is zero. Thus this completion is faithfully realized as physical profiles.

Every compact r is a bounded functional on that completion by(D3), hence
has a unique Riesz energy representative. The representative is the energy
limit of(H4+epsilon)^-1r: the spectral error integrand is
epsilon^2/[lambda(lambda+epsilon)^2], dominated by1/lambda, whose integral
is finite by(D4). It can have infinite l2 norm. This argument establishes
the actual compact-source threshold response without a separate core inverse.

## Full incoming tensor, variational form and strict positivity

Let U be the real9x5 normalized uniform-pair matrix, U^T U=I. Its axial rows
are(1/sqrt2,1/sqrt6),(-1/sqrt2,1/sqrt6),(0,-2/sqrt6); each plane's own T
column has rows(-1,+1)/sqrt2. For any complex symmetric5x5 matrix A, define
the physical incoming profile Phi_A as the occupation coefficient of
(1/sqrt2)sum_ab A_ab C_a^dagger C_b^dagger Omega, with C the five uniform
normalized pair sums. It is the sum over actual matchings. On separated
edges its amplitude is sqrt2(UAU^T)_(d,e).

Every positive row of Phi_A vanishes outside a fixed collision region:
there the two disjoint graph edges solve the individual constant N2 zero
equations. Hence E(Phi_A) and F_A=H4 Phi_A are finite/compact, respectively.
For compact physical chi the affine energy is

 E(Phi_A+chi)=E(Phi_A)+2Re<chi,F_A>+E(chi).

Its infimum equals the l2-correction infimum by bounded H and compact F.
Riesz minimization in the physical energy completion yields

 T0[A]=E(Phi_A)-<F_A,G_H(0)F_A>
      =inf_(chi compact) E(Phi_A+chi).                    (D5)

The incoming row vector is finite, so the affine energy is nonnegative and
the minimizing profile exists in that completion. It is unique with fixed
incoming Phi_A, and satisfies H4 psi=0 pointwise by compact variation.
Linearity gives a Hermitian form on the full fifteen-dimensional space.

For strict positivity fix a compact chi. For each graph residual e the
actual removal field of Phi_A+chi equals sqrt2(UAU^T)_(d,e) plus a compact
field, and it vanishes at the common anchor r=0 by hard-core overlap.
The scalar capacity inequality |u(0)|^2<=g0||gradient u||_2^2 and(D1) give

 E(Phi_A+chi)>=(2a/g0)||UAU^T||_HS^2=(2a/g0)||A||_HS^2.

These row sums can be embedded in sufficiently large odd tori at fixed
compact chi and divided by volume, or read directly as finite positive
orbit-row sums. Taking the compact infimum proves

                   T0>=(2a/g0)I_15.                     (D6)

All fifteen complex directions are covered. Finite-volume Schur convergence,
numerical rational trials and any many-particle limit require their separate
arguments; none has been assumed in(D1)-(D6).
