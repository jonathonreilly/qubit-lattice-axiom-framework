# Secondary molecule physical pair-source check

Disposition: PASS for the displayed leading and order-lambda^2 form factor, conditional on the supplied secondary bound-band existence and orientation selection. No fitted vertex or T-matrix interpretation is needed.

Let the normalized q=0 leading state be (|3ex>+|3ey>)/sqrt(2), where |d>=R^-1 sum_r |r,r+d> is an unordered two-column translation orbit. For generic non-self-inverse k, the physical ordered pair source has orbit amplitude

 2 cos(k dot d)/[R sqrt(1-2/R^2)].

This gives the root's overall sqrt(2)/[R sqrt(1-2/R^2)] factor after multiplying each orientation amplitude by 1/sqrt(2). The d and -d orbits are the same unordered orbit and must not be counted twice; the displayed cosine convention handles this correctly.

## Complete first-hop tail

I enumerated every elementary nearest-edge XOR from {(0,0),(3,0)} in a surrounding box, then retained Q8/perimeter16 outputs. Exactly six physical moves remain:
- Two moves to relative separation (4,0), of relative-energy gap v lambda^8.
- Two moves to relative separation (3,+1) and two to (3,-1), each of gap (v/2)lambda^8.

At zero COM momentum the two boundary moves to each relative orbit add. Since the elementary hop is -Jgamma lambda^10 and the eliminated-state denominator is negative, all these tail amplitudes are positive. They are 2gamma/v times lambda^2 for |4ex>, and 4gamma/v times lambda^2 for each |3ex+/-ey>, relative to the parent horizontal amplitude. The vertical results follow by rotation.

The skew gap follows directly from local order-eight interactions: one 3-by-1 perimeter includes both columns at displacement (3,1), giving interaction -v/2, compared with the axial endpoint -v. At separation four no perimeter-eight cycle reaches both, so its connected interaction is zero and its gap is v.

No four-column Q8/perimeter16 intermediate is reachable by one edge from this pair. The exhaustive classification gives only the T tetromino or the four-column d=3 rod-plus-singleton as candidates: neither contains the initial two columns with its remaining two columns forming one nearest-neighbor edge. Direct XOR enumeration agrees. Longer rod-family members require more column changes. Other Q8 perimeters have order-lambda^6 gaps, so their tails begin at lambda^4; non-Q8 intermediates begin later. In particular the inward move to separation two is an order-lambda^4 correction, not an omitted order-lambda^2 tail.

## Physical source dressing

Both axial-separation-three pairs have 4L external YY bonds reversed by their X-column pair operator. Unlike an adjacent vertical pair, there is no shared YY edge to remove. Each reversed virtual bond contributes -lambda^2/32 to the matched wall-free overlap, giving the common amplitude 1-Llambda^2/8. Two native insertions cannot change a different full height-ten column pattern. Applying this UV correction to a tail already of order lambda^2 would only contribute at order lambda^4.

The bound-state norm correction from the first tail is order lambda^4. Combining the leading pair and tail amplitudes therefore gives exactly

 sqrt(2)/[R sqrt(1-2/R^2)] * {
 (1-Llambda^2/8)[cos(3kx)+cos(3ky)]
 +lambda^2 (2gamma/v)[cos(4kx)+cos(4ky)]
 +lambda^2 (4gamma/v)[cos(3kx+ky)+cos(3kx-ky)
                         +cos(kx+3ky)+cos(kx-3ky)] }
 +O(lambda^4/R).

This is an additive form-factor expansion, not a relative estimate at its zeros. The generic source normalization must not be reused as a unit-normalized identical-pair convention at self-inverse k.

## Uniform remainder

The source has global norm O(R^2), while each fixed-order retained connected bound-state/pair-source coefficient has bounded relative-coordinate l1 norm. The latter gives the displayed 1/R behavior; the former is used only for the final exact projector error. With absolute Hamiltonian tail R^2 lambda^M and same-fibre orientation gap lambda^20, that error is bounded by R^4 lambda^(M-20). For R~lambda^-p it is o(lambda^4/R) if M>24+5p. At p=5,M=70 the error has exponent 30, compared with exponent 9 for lambda^4/R. Source-transform tails must be retained to sufficient order in the same matched construction.

This confirms the residue of the explicitly specified physical pair operator conditional on the proved secondary eigenstate. It does not establish a rate, scattering amplitude, universal coupling, or arbitrary-state preparation. No repository edits or formal audit.

Read /tmp/neutral_secondary_motion.py and reused the analytic perimeter-sixteen classification. The first-hop enumeration also checked the root's diagonal-energy helper values 0 and -9/65536 per layer for the two kinds of intermediate.
