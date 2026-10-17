# Record gate center inverse: independent exact check

Disposition: support for the actual local one-lead inverse bound <26/j on the selected REAL open band, for both record sectors and all 24 gate coordinates. No correction requested. This does not certify the whole attached emitter/source inverse, complex contour, seed spectral mass or runtime. The additional full-fiber application remains conditional on the stated real closed-channel gap and correct spectral decomposition.

## Sources, exposure and computation

Read the complete proposal, check.py and RESULT.json. Verified SHA256:

- PROPOSAL.md: 3fb72f1629c0136531a41424683279a1b42f3a54bda4785359a367c018756c82.
- check.py: 776b43328bae8d0e27566e54f1145a0acf1e904fe3991b2ed127e45e24026aa1.
- RESULT.json: 84f1bc21d92da92081c925c7f7d10132f167d1d2e2633ff4125f84bc6482b358.

Also read the complete record_gate_closed_spectrum/PROPOSAL.md to check the actual chain unitary, and reused the known literal attachment matrix from record_attached_kernel/PROPOSAL.md fbc1315e90a3980f71b1580de992b64602d5085f7a8aa1a50b90683da9ce9457. I authored that attachment proposal, but did not author this inverse calculation. This checks the new root calculation after full source exposure; it is not an independent check of my attachment proposal or of all closed-spectrum claims.

Within the explicitly authorized bounded alternate computation, I performed one exact Python integer/Fraction continuant calculation, independent of SymPy inversion. It computes all inverse squared entry magnitudes from tridiagonal minors. No floating point, numerical spectrum, dynamics, parameter sweep or original check.py rerun was used. No Git/W/model/prompt/checkpoint/publication edit occurred; only this report was written. Applicable unchanged instructions/workflow are reused. The source says SymPy1.14.0 was used, but the supplied JSON does not encode that version or a full execution transcript; I do not independently certify its historical environment. The exact mathematical data were independently reproduced below.

## Twelve-site reduction

Rotate both physical lead components at every slice by the same real orthogonal Hadamard U, keeping the arm coordinates fixed. The square block -jU then becomes -jI. At the two-lead Schur boundary the self-energy is ij times the identity on both physical ports, and is invariant under this rotation. Thus the 24-site D2 at the center really is the direct sum of two 12-site matrices, not an assumed separate-arm model for an asymmetric one-lead load.

Each chain runs from terminal n=0 through arm end n=10 to transformed port n=11. On arm1 its original y=2--3 and y=5--6 edges are exactly chain bonds 2--3 and 5--6. Their four endpoint diagonals in h are3j, so E-h at E=2j has diagonal -j there. Terminal diagonal2j+jx becomes -jx, ordinary diagonals become zero, and each eliminated lead contributes +ij at n=11. Off-diagonals are positive j or sqrt(2)j because the physical hoppings are negative. This reproduces precisely the matrices constructed in check.py.

## Independent exact inverse data

For the scaled tridiagonal D, let theta_k be its leading k-site determinant, theta_0=1, and let phi_k be the trailing determinant beginning at k, phi_12=1. The recurrences are theta_k=d_(k-1)theta_(k-1)-a_(k-2) squared theta_(k-2), and the corresponding reverse recurrence for phi. All these determinants are Gaussian integers because each off-diagonal square is1 or2.

For i<=j, the inverse entry is

    R_ij=(-1)^(i+j)(product_(k=i to j-1) a_k)theta_i phi_(j+1)/theta_12.

Its squared modulus is therefore an EXACT rational number using only the product of the off-diagonal squares and squared Gaussian-integer norms. Summing these fractions, with off-diagonal entries counted twice, independently gives:

| x | arm | det D | ||R||_F squared | ||R e11|| squared | R11,11 |
|---|---|---|---|---|---|
| +1 | 0 | 1+i | 72 | 6 | (1-i)/2 |
| +1 | 1 | -2+2i | 159/2 | 13/2 | (-1-i)/2 |
| -1 | 0 | 1-i | 72 | 6 | (-1-i)/2 |
| -1 | 1 | 2+2i | 129/2 | 11/2 | (1-i)/2 |

These match the supplied result exactly and prove invertibility in each case. This alternate derivation does not treat the source's assertions or JSON as mathematical proof. The original script itself uses exact SymPy matrices, verifies D R=I and sums conjugate products; its implementation agrees with the claimed quantities.

## Physical port and one-lead removal

The physical input port is an equal-magnitude superposition of the two orthogonal transformed ports. Consequently its diagonal resolvent entry is the average of the two tabulated entries, namely -i/(2j), in either record sector. Its squared full column norm is the average of the two tabulated port-column squares divided by j squared:25/(4j squared) for x=+1 and23/(4j squared) for x=-1. There are no cross terms because the two chain ranges are orthogonal. The full Frobenius norm is at most sqrt(303/2)/j; using Frobenius as an upper bound for the operator norm is legitimate.

D2 and its inverse are complex symmetric, and the physical basis transformation is real orthogonal. Therefore the physical input row is the TRANSPOSE of the input column, with equal Euclidean norm. It is not the Hermitian adjoint column; no such false identification is needed for the rank-one operator norm.

Removing the input self-energy gives D1=D2-ij e_p e_p^T. Sherman--Morrison then yields

    R1=R2+[ij/(1-ij g2)]R2 e_p e_p^T R2.

With g2=-i/(2j), ij g2=1/2 and the denominator is exactly1/2, so the update coefficient is+2ij. Its norm is at most2j times25/(4j squared)=25/(2j). Thus ||R1||<25/j because sqrt(303/2)<25/2: squaring gives151.5<156.25. This confirms the sign, factor and strict bound without squaring the whole-matrix Frobenius norm unnecessarily.

## Real-band perturbation and full-fiber limit

For real displacement u=|q-pi/2|, |E(q)-2j|<=2ju and |exp(iq)-i|<=u. The h_x matrix is fixed, so D1 varies by at most3ju. Multiplication by the center inverse gives a Neumann parameter <75u. On u<=4e-6 it is at most.0003. Therefore

    ||D1(q)^-1||<(25/j)/(1-75u)<26/j,

where the last inequality follows already from25<26*.9997. This includes the endpoints of the specified band. The resulting recovery -j D1^-1 e_p has norm <26 into the complete 24-site gate. This proof does not assign the same bound on a complex contour; one would have to bound the complex E and root displacements on that contour explicitly.

For closed channels, the conditional centered row bound uses ||h_x-2jI||<3.415j and the lead term j|s|. With the supplied |s|<1/60 and |E-2j|>60j, their difference exceeds56j, giving the stated closed inverse ceiling. This calculation supports the implication from those gap premises without independently certifying every attachment premise. The direct sum over orthogonal B spectral fibers and conserved record sectors has norm equal to the maximum block norm; hence an actual one-open/seven-closed fiber satisfying those premises has total local recovery <26. This is not an aggregation of overlapping old-input error columns. If another channel opens or its gap changes, that application must be revisited.

The closed tail beyond its port contributes the geometric factor |s|/sqrt(1-|s| squared) times the port amplitude and is not included for free in a 24-site bound. The open scattering tail is not square-summable as a stationary column. No global source feedback, actual spectral synthesis, normalized herald guarantee or late-time behavior follows from this local inverse calculation alone. Within these limits, the proposed inverse margin is supported.
