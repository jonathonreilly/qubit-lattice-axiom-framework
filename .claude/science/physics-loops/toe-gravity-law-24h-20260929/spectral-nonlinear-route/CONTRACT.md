# Frozen spectral ADM jet contract

Frozen before the calculations below: 2026-09-30, approximately 02:00 UTC.
This is an explicitly supplied continuous canonical comparator, not native
finite M2 and not a completion preserving block 112's finite-zone seed.

## Carrier and evaluation domain

The spatial torus has periods 2 pi and normalized integration measure.
There are n^3 grid sites, n=2J+1 odd. The FULL carrier has six real symmetric
metric coordinates h_A(x) and six canonical momenta P_A(x) per site,
{h_A(x),P_B(y)}=delta_AB delta_xy. Write p_A=n^3 P_A and the symmetric
matrix pi_ii=p_ii, pi_ij=p_ij/2 for i<j. Thus the normalized matrix pairing
is exactly the canonical pairing. Fourier coefficients use 1/n^3; hence
{hhat_A(k),phat_B(l)}=delta_AB delta_(k+l=0 modulo n).

D_j has multiplier i k_j for the chosen representative -J<=k_j<=J.
Products are ordinary pointwise FULL-grid products (circular Fourier
convolutions), with no band projection in the constraints or brackets.
Only the data at which identities are evaluated, and every independently
specified lapse or shift, have support |k|_infinity<=B, with 5B<=J.
Zero modes are included. Complex Fourier calculations are polarized
identities whose real slice obeys conjugate symmetry.

Half placements can be removed by the explicitly supplied canonical
Fourier map hhat_A(k),phat_A(k) -> exp(-i k.s_A) times those coefficients,
s_ii=0, s_ij=(2pi/n)(e_i+e_j)/2. A bond shift has s_j=(2pi/n)e_j/2.
Opposite-frequency phases cancel in the bracket. The odd grid has no
ambiguous Nyquist mode. Define the new constraints after this map, with
all components collocated and the same lapse at each point. Pulling them
back is nonlocal and does NOT reproduce a four-corner lapse mean or the
nearest-difference symbol of block 112.

## Supplied law

g=I+h, alpha>0, K>0, a=1/(4 alpha), s=aK. In a neighborhood where g is
positive definite, define

 C[N]=mean N [a/sqrt(det g) (tr(g pi g pi)-tr(g pi)^2/2)
                         -K sqrt(det g) R_D(g)],
 G[X]=mean pi^ij [X^k D_k g_ij+g_ik D_j X^k+g_jk D_i X^k].

R_D is the ordinary Christoffel curvature formula with EVERY derivative
replaced by the full-grid D. This specifies a finite analytic function;
no global discrete product rule is assumed. The full finite Poisson
bracket is used, including derivatives with respect to high modes set to
zero in the evaluation data.

The proposed structure is F^i(N,M)=s g^ij(N D_j M-M D_j N),
U(X,N)=X.DN, and [X,Y]^i=X.DY^i-Y.DX^i. Positive spatial Lie action fixes
all signs; they will be checked from the canonical pairing.

## Exact target and necessary fourth-order data

Degree counts EACH h and pi as one, with smearings degree zero.
Write C_[d] for the homogeneous Taylor coefficients through d=4.
G=G_[1]+G_[2] exactly, so G_[3]=0. Write F=F_[0]+F_[1]+F_[2]+...
from g^{-1}=I-h+h^2-.... The target is coefficient equality:

 * CC through field degree 3;
 * GC through field degree 3;
 * GG through its full field degree 2;
 * the structure-substituted Jacobi identities through field degree 2,
   with field dependence of F differentiated, not held fixed.

C_[4] is required: {G_[1],C_[4]} contributes to GC degree 3, and nested
brackets of degrees (4,1,1) contribute at degree 2. A C_[3]-only result
will not be called a check of those obligations.

The proof must control all variational-gradient and intermediate
contraction supports, not merely the integral of the original terms.
Expected sufficient bandwidth: a bracket of output degree r has r+2
external factors; a nested bracket has r+3. Thus the stated targets have
at most five low-band external factors. A contraction-tree proof is
required before claiming transfer of continuum identities.

## Boundaries and optional separately supplied scalar

This is not an invariant-band or all-zone first-class theorem. Products
and Hamiltonian flows can leave the evaluation band. The spectral
derivative and rephasing are spatially nonlocal. A local analytic Taylor
remainder or exact finite polynomial coefficient result is the target.

If vacuum transfer succeeds, separately test an additional canonical
scalar (phi,p), with zero background and

 C_m[N]=mean N [p^2/(2 sqrt(det g))
       +s sqrt(det g) g^ij D_i phi D_j phi/2
       +m^2 sqrt(det g) phi^2/2],
 G_m[X]=mean p X.Dphi.

This scalar is explicitly supplied, not the original walker or its record
instrument. It must include gravity--scalar cross terms and the same
bandwidth/full-bracket rules. Failure or omitted checks remain explicit.

## Closest prior work and source decision

Selected procedure/science base is 7146fe17a76de41badcaca3c3c7cac6d11eb2a00;
refreshed main is 9d15f404c63ff5b9d877e2bdc06ea8713493ffb4. Block 112 gives
flat-strain, momentum-linear CC closure for its finite nearest-difference
law. Main SOFT_SPIN2...2026-09-14 sections 6--7 give the analytic periodic
open-patch obstruction and improved-stencil infrared errors, not spectral
ADM jets. PR 9363 fd51a1f4c7f38c124d6f0f7dde396198eadf8b36 viability-map A1
asks for local fixed-seed closure and explicitly leaves nonlocal escapes;
its expected failure is not a premise here. The pack's decay-symbol and
independent-discrete reports leave nonlinear SLAC/band and enlarged
cochain normal-generator completion open. No closest source read so far
contains the present finite full-carrier coefficient-transfer theorem.
No universal novelty claim is made.

## Compute budget

Use exact sparse Fourier arithmetic with rational complex coefficients
and polynomial field-degree truncation. Do not enumerate a dense grid
carrier. Full gradients can be produced by reverse differentiation of
the sparse expression, including zero-input modes. Start with a small
axial check and then mixed-axis sparse inputs; cap a job at 180 seconds
and 1 GB estimated memory. BLAS/OpenMP threads 1. At most one job here
until root resource coordination permits otherwise. Analytic proof is
load-bearing; numerical sampling is not an identity proof.
