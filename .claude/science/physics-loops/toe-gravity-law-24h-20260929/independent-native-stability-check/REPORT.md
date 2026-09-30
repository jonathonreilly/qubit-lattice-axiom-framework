# Selective independent reconstruction of native stabilization

Root reconstructed the frozen native-stability-route report from the literal
hard-core pair operators and occupation projectors. No author code was imported
or executed, and no new numerical experiment is claimed. The underlying native
Gram and pair bands already have a separate independent exact check. This check
finds no blocking defect in the stabilization, finite-torus spectrum, packing,
density-onset and temporal-readout claims, with the infinite-rotation scope
clarification below. It is not a formal review/audit PASS or a gravity phase.

The author report SHA256 is
7eba7d0092eb4990f5ae1a46825e015c6edc18692c09cab69ad5cd3ed4d24ca9.
I read it completely, plus the complete original native report and preceding
independent native check. Current main source e75578f713 and the campaign's
previous direct primitive/axiom reads remain unchanged; no new physical
premise is granted. The root suggested the sharper gap formula during the
author's pass, so the gap is a jointly developed consequence with the author's
separate confirmation, not a wholly independently originated claim.

## Operator reconstruction, without a dilute approximation

For the three opposite-pair annihilators d_i, the E projection is
sum_i d_i†d_i-(sum_i d_i)†(sum_i d_i)/3. For four signed plane pair words v_a,
expand every (v_a-v_b)†(v_a-v_b): each diagonal occurs three times and each
ordered off-diagonal once with minus sign. This equals4sum_a v_a†v_a-
(sum_a v_a)†(sum_a v_a). These are identities in any operator algebra and
require no commuting-overlap approximation.

Distinct-site hard-core factors give d_i†d_i and v_a†v_a equal to products
of the two endpoint occupations. Every axial pair has one center and each
orthogonal pair two centers. The latter two signed words have the same sign
under center exchange; their diagonal count alone suffices here. On L>=5,
coordinates in[-2,2] do not identify different displacements. Summing the
positive squares therefore gives exactly2mu per unordered edge of the
18-neighbor pair graph, minus2mu times the E interaction and mu times T.
With sum_x n_x m_x=2sum_edges n_xn_y, the unrestricted identity is
H=A+mu sum_x n_x(1-m_x).

Every m_x is an integer0..18 commuting with n_x. Since x is not its own
neighbor, n_x binom(m_x,2) is exactly the sum over three distinct occupied
sites, with153 unordered neighbor pairs. Addition gives the polynomial
(1-m)+m(m-1)/2=(m-1)(m-2)/2, nonnegative at every integer0..18. This proves
all-volume positivity of V3 without diagonalizing an N-particle block.
Its star radius is2 and maximum pairwise support diameter4. Proper cube
rotations permute its neighbor set. The alternative cap obeys
1-m+(m-1)_+=1_(m=0); binom(m,2)>=(m-1)_+ pointwise. Both vanish as operators
on every N<=2 state. These facts do not select an admissibility law.

The stated iff region is also exact for the specified stabilization problem:
negative E or T pair energy at q=0 cannot be raised by an interaction zero on
that sector. Conversely the closing V3 plus nonnegative differences multiplying
sum PE and sum PT establishes positivity whenever gE<=2mu,gT<=mu.

## Ground states, sharp gap and the density scan

An E pair has opposite-word coefficients summing to zero. The A square D kills
it, every T square kills it, and each occupied endpoint has exactly one pair-
graph neighbor. Thus it is an exact closing zero vector. Centers separated by
five have closest endpoints separated by at least three in one coordinate, so
no pair graph edge connects clusters. Orthogonal choices {vacuum,E1,E2} give
3^(V/125) exact states on the stated subsequence. This is a lower bound only.

For the general positive finite-range H' argument, each local summand touches
at most one separated cluster. Its product-state expectation equals the sum
of the corresponding isolated-cluster expectations minus duplicate vacuum
expectations. Summing gives zero because the actual isolated states and
vacuum have zero energy. Positivity of the full operator then gives a kernel
vector; positivity of each summand is unnecessary. A uniform finite interaction
range is essential for positive-density packing. No classification of every
dense ground state follows.

For H_mu,g=gF+(mu-g)N with F>=0 and conserved N, the N=1 eigenvalue ismu,
every N>=2 energy is at leastN(mu-g), and a compact E pair attains2(mu-g).
For mu>g the exact gap is thereforemin(mu,2(mu-g)) and vacuum is unique.
For g>0, the complete two-particle minimum consists of2V E states and the T
states with cos qi cos qj=1. There is one pair(qi,qj) on odd tori and two on
even tori, with L free momenta in the third direction: multiplicities2V+3L
and2V+6L. Null Gram vectors are absent at this maximum. At g=mu/2 the one-
and two-particle minima coincide. The formulas do not use the g=0 degenerate
case, which the source correctly excludes for its multiplicity assertion.

For mu<g, the packed state has energy-(g-mu)2V/125. The operator lower bound
H_mu,g>=-(g-mu)N then implies every ground state's mean density is at least
2/125 on that subsequence. This establishes the stated discontinuous onset
bound, not a phase classification or a precise transition state.

For a uniform spin product with occupationrho, <b>=sqrt(rho(1-rho)) up to a
common phase. Expanding the E projection gives<PE>=4rho^3-2rho^4. Each of the
three T terms has expectationrho^4, since each axis difference has squared
norm2rho². Hence<2PE+PT>=8rho³-rho4. The153 triple terms contribute153rho³,
yieldingmu(rho+145rho³+rho4). This independent contraction confirms the
quoted product-state discriminator and its failure to classify entangled states.

## Mobile pairs and readout control

The gradient sum on each pair frame has Fourier weightell=2sum(1-cos q_i).
Acting on the exact pair-frame eigenvectors multiplies each channel by its
Gram norm S_A. Thus W adds tau*ell to E and tau*ell*Sij to T. The orthogonal
complement remains unchanged. At small q this gives the reported five
quadratic branches, not two linear tensor branches.

On the infinite vacuum representation, zero energy of a bounded-number vector
implies Q_A(x)psi constant in x. Cauchy-Schwarz and finite incidence bound
sum_(x,A)||Q_A(x)psi||² by a fixed constant times<N>; this remains finite.
The constant must be zero. The remaining energy ismu<N>+<V3>, forcing vacuum.
This proof does not imply finite-volume uniqueness or finite-density coercivity.
The new exact finite-volume kernel argument sent separately to the author is
not included as checked source content until its own reconstruction is complete.

In the opposite-pair three-state space, the singlet u has energy2mu and its
orthogonal E plane energy0. The plus state's overlap with u is sqrt(2/3).
At t=pi/(2mu), its coefficients become(-sqrt(2)/6,-sqrt(2)/6,-2sqrt(2)/3),
with squared values(1/18,1/18,8/9). The minus state remains in E and has no
third-pair outcome. This is a supplied Hamiltonian/Born temporal measurement
protocol, not an actual permanent-record formation law.

A uniform on-site rotation is an ordinary unitary on each finite torus,
preserving its spectrum and local positivity. On Z³ a nonzero-density rotated
vacuum generally lies in a different representation: the infinite product
should be understood as a quasi-local automorphism/state construction, not a
unitary or normal vector in the finite-particle vacuum Hilbert space used
above. Future integrated source should make this domain explicit. None of the
finite-torus stabilization results relies on that infinite product.

## Independence limits and next action

No full-carrier numerical spectrum, author64-state runner rerun, thermodynamic
phase, uniform-density inequality, actual record instrument or gravitational
identity was checked here. The analytic independent steps cover the claimed
operator/spectral consequences; the prior independent Gram proof is an explicit
shared provisional input. The smaller live question is the finite-volume common
kernel and then a volume-uniform density coercivity estimate for the specified
mobile law. That does not assume the target tensor phase. Preserve all supplied
basis, law, time, preparation and readout choices as imports.
