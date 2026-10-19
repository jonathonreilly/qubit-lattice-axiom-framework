<!-- Original PR9813 source SHA256 278b3af201a5fec1df0eb5e5c634390504c57c8d6f8a3fda824733bd1866c2e1. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Native orientation mixing and an isotropic bound-feature pole

Status: conditional-support. This extends the supplied fixed-L10 one-qubit slab result; it does not derive the geometry or observed scalar identification. The later REFLECTION_GROUND_SECTOR_PROOF.md proves existence of a global ground in this sector, without uniqueness. All numerical controls are exposed development.

Dependencies: [EIGHT_FLUX_BOUND_CLUSTER_PROOF.md](EIGHT_FLUX_BOUND_CLUSTER_PROOF.md), [POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md](POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md). The prior p<2 restriction was sufficient for separating the entire no-wall band. It is unnecessary for the low-energy states of interest.

## Low-energy embedding for any fixed polynomial size

Let B be a retained local wall-count normal form, N the number of walls and Hcol its N0 restriction, extended by identity on wall labels. Completing each term to whole fixed-height columns yields the form bound

 |B-2JN-Hcol_ext| <= CJlambda N.

The difference vanishes on any locally wall-free neighborhood on both sides, by termwise wall-count preservation and Hermiticity. Bounded overlaps give N, rather than area, on the right.

Apply the local bad-plaquette normal form to Hcol. Each retained term is Q-preserving and plane invariant. After subtracting its flat scalar value, its local projector sandwich is bounded by the number of nearby bad plaquettes. Summing therefore gives |D_j|<=C_j Q as a global form inequality, not only a norm estimate restricted to Q4 or Q8. For any fixed truncation order and sufficiently small lambda,

 W Hcol W† >= e0 I + J(L/128)lambda4 Q - epsilon_Q I,
 epsilon_Q<=CJ R²lambda^M.

The finite constants depend on the chosen order and fixed height, not R. In particular Hcol>=e0-epsilon_Q globally. Its identity extension has the same lower bound. Thus

 B-e0 >= J(2-C lambda)N-epsilon_Q.

The N>=2 sector starts at e0+4J-O(Jlambda)-epsilon_Q. The selected Q0/Q4/Q8 states lie e0+O(Jlambda4). Their low-energy separation from walls survives for every fixed R~lambda^-p once the final absolute remainder order M is large enough. High-Q no-wall states may overlap wall energies; no exact separation of the entire N0 band is claimed. Finite-order support remains smaller than R in every such limit. No infinite-order convergence, infinite volume at fixed lambda or uniformity in unbounded p is assumed.

The microscopic remainder and subsequent reduction tails are required to have final absolute bound CJ R²lambda^M, after all small-denominator losses. Such a fixed finite order may be chosen separately for each fixed p and target precision. Exact low-energy spectral identification, not a global N0 identification, then follows from the external wall gap and the relevant internal fibre gaps.

## Native fourth-hop orientation process

Use centered horizontal pair r±ex and vertical pair r±ey. At least four elementary edge flips connect any horizontal minimum to a vertical minimum. Shared-column cases leave two odd endpoints at Manhattan distance at least four; the other cases have minimum matching length four. This count holds separately in each physical vertical layer, so the native process requires at least forty transverse insertions.

Four leading winding hops and three Q8 nonminimum denominators give order lambda22. Fewer longer native moves have fewer enhanced denominators and cannot lower this order. Leaving Q8 replaces a lambda6 denominator by a lambda4 denominator and is later. Diagonal corrections are also later. Intermediate endpoint states are excluded from the resolvent. Canonical folded products at fourth hopping order are orientation diagonal because their two-hop factors are orientation diagonal; they cannot alter this off-diagonal coefficient.

For each intermediate configuration S divide by perimeter(S)-12 in units 2b. Exact enumeration gives the translated-center weights

 center(0,0): 9673/12000;
 each of four axial centers: 191/384;
 each of four diagonal centers: 1637/4608.

The nine weights sum to 607201/144000. Independent shortest-edge-set enumeration and all 24 edge orderings reproduce the forward syndrome recurrence. Therefore

 H_AB(q)=-J lambda22 gamma4/(2b)^3 [9673/12000
          +(191/192)(cos qx+cos qy)+(1637/1152)cos qx cos qy]+O(lambda24),
 zeta=gamma4/(2b)^3 *607201/144000 >0.

At q0 the orientation splitting is 2J zeta lambda22[1+O(lambda²)], with zeta=1.8480186599501435e-7. The lower state is C4 even and is precisely the representation created by the original uniform scalar source. No orientation-mixing interaction has been added.

## Actual isotropic pole on large transverse grids

Put t=gamma²/D. The diagonal average has momentum increment (5/2)Jt lambda14 |q|² plus O(Jlambda14|q|4+Jlambda16|q|²). The diagonal imbalance is O(Jlambda14|q|²); after diagonalizing the mixed two-state matrix its contribution to the lower eigenvalue is O(Jlambda6|q|4), using the lambda22 gap. The off-diagonal momentum correction is O(Jlambda22|q|²). Thus

 E_-(q)-E_-(0)=(5/2)Jt lambda14|q|²
  +O(Jlambda16|q|²+Jlambda6|q|4+JR²lambda^M).

Choose any fixed p>4 and q=2pi n/R, fixed nonzero n, R~lambda^-p. The relative anisotropy error is O(lambda^(2p-8)), tending to zero. Choose M>14+4p to resolve energy, and M>40+3p to transfer the original source using the crude norm bound and lambda22 projector denominator. For example p=5, M=60 gives leading energy order24, anisotropy error order26, global tail order50 and source-transfer error order23, below the source amplitude order18.

The original finite-momentum source coefficient is a finite translated-pattern sum; its endpoint vector tends to m(A+B)/sqrt(L) as q tends to zero. The lower eigenvector tends to the same symmetric combination because q²/lambda8 tends to zero. Consequently the actual lower pole has original-source atom

 (2m²/L)lambda36[1+o(1)], m=1361400132699035/945539748965690376192.

The resolved-grid quadratic dispersion coefficient is (5/2)t=1.1197700663008921e-5, multiplying Jlambda14. This is isotropy in the two transverse directions, not three-dimensional Lorentz invariance. The pole remains gapped at leading energy 2JDelta lambda4; neither masslessness nor a long-range gravitational force follows.

## Controls and unresolved imports

neutral_q8_orientation.py performs exact rational path summation. neutral_q8_isotropic_control.py evaluates only the derived two-state matrix at 220-digit precision, retaining finite-lambda deviations: at lambda=.01 the (2,1) direction differs by about 7.4 percent, while at 1e-8 it differs by about 7.8e-14. These are coefficient controls, not full-grid diagonalizations or empirical tests. Actual-grid statements rely on the analytic bounds above.

Independent reports: INDEPENDENT_ALL_POLYNOMIAL_EMBEDDING_CHECK.md and INDEPENDENT_Q8_ORIENTATION_CHECK.md. The all-history relative winding bound in UNIFORM_GROUND_SELECTION_OPEN.md remains unavailable for quantitative character splitting. The later REFLECTION_GROUND_SECTOR_PROOF.md bypasses that bound to prove existence of a global ground in this sector; uniqueness and preparation remain open. Native Hamiltonian, weak anisotropy, fixed height, measurement and units remain premises.
