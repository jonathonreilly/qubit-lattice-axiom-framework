# Regge metric reduction and reciprocal source: working derivation

2026-09-13, personal campaign. Start from the corrected main Regge spectrum and
static source notes, both fully read. They explicitly leave global Laurent
identities, a correct metric lift and physical source selection open. Their
finite sampled Hessian is a supplied mathematical model, not axiom-derived gravity.
The two-weight matter note, static complete-square bridge and finite Fock source
note were also read for their exact scope; none supplies the missing common source.

Primary literature reading identified an analytical route, already known for
linearized length Regge theory: eliminate four body diagonals, ignore the null
hyperdiagonal, and use the ten axis/face lengths as discrete metric variables.
Sources: Bahr–Dittrich–He arXiv:1011.3667v2 section 6.1 and appendix A through
A.12; Dittrich arXiv:2105.10808 section IV.B.5 (PDF pages 9–10). These sections
were read directly. Their length-action identification is prior art; a new note
must not claim its discovery. Their displayed formula does not by itself verify
our exact source convention, metric image or coupling.

Proposed analytical reduction BEFORE any new matrix comparison:
Let q_S=delta(length_S squared), z_i=exp(i k_i), and for each triple A={a,b,c},

r_A=q_A - 1/2 sum_(ij subset A)(1+z_(A minus ij)) q_ij
          + 1/2 sum_(i in A)(z_j+z_k) q_i.

This candidate body constraint annihilates every exact vertex displacement
q_S=2(z_S-1) sum_(i in S)xi_i and reduces to metric additivity at k=0. The
coefficient is conjectured from local geometry and these identities, not fitted.
It still needs derivation from the actual simplex deficit derivatives.
For the ten remaining variables define h_aa=q_a and h_ab=(q_ab-q_a-q_b)/2.
Then h_aa gauge=2(z_a-1)xi_a and h_ab gauge=z_a(z_b-1)xi_a+z_b(z_a-1)xi_b.
With p_a=2sin(k_a/2), u_a=exp(i k_a/2)xi_a, the phase change
H_aa=h_aa, H_ab=exp(-i(k_a+k_b)/2)h_ab gives H gauge=i(p u^T+u p^T).
This phase change is invertible, including finite complex frequency.

Candidate Schur action: the standard quadratic Fierz–Pauli form at p, with
normalization to derive from one explicit local coefficient, plus a constant
negative body block and zero hyperdiagonal. If the actual identity holds, its
polynomial form (quartic denominator cancellation) gives exact nullity and
continued dispersion for all momenta. It would also supply a distinct dynamical
metric lift, rather than restore the disproved line-map metric intersection.

Next derive the orthoscheme local Hessian analytically and compare a small exact
fixture to the existing geometric implementation. Then derive the transported
source and static solution/gauge-invariant readouts, keeping any original matter
coupling and formation clock supplied. No theorem or physical graviton is claimed
at this working checkpoint.


First four-momentum probe: the full candidate Hessian agrees within 7e-16,
including zero and a Nyquist axis. The body block is -I/2. A separate row check
reported 1/2 because the checker used reverse body-class order relative to its
constraint rows; both full matrices were already correctly indexed. Original
probe and JSON are preserved. Align only the row order and keep the theorem
candidate unchanged. These float matches do not prove an all-momentum identity.

Analytical local route derived after this probe:
In one unit path simplex use cumulative vertices X_j=e_1+...+e_j, j=0..4.
Its barycentric gradients are n_0=-e_1, n_j=e_j-e_(j+1), n_4=e_4.
For missing pair i,j let a=n_i², c=n_j², b=n_i.n_j, and let P_ij be the
orthogonal projector onto the hinge plane. A_ij=1/2 sqrt(ac-b²).
For the simplex metric variation H,
A_ij dtheta_ij=-1/2[n_i H n_j - (b/2)(n_i H n_i/a+n_j H n_j/c)].
Also dA_ij/A_ij=tr(P_ij H)/2. Schlaefli follows directly by sum_i n_i=0.
Thus the flat Regge second variation is the sum over simplices/pairs of
(1/4)tr(P_ij H)[n_i H n_j-(b/2)(n_i H n_i/a+n_j H n_j/c)].
All coefficients are rational; no arccos or sampled derivative is needed.
The ten components H_ab follow from the ten squared edge variations by
H_aa=q_(a-1,a) and, a<b,
H_ab=(q_(a,b-1)+q_(a-1,b)-q_(a,b)-q_(a-1,b-1))/2.
This finite local identity will be summed over the 24 permutations with literal
edge-anchor phases, then reduced into seven symmetric tensor entry families.
