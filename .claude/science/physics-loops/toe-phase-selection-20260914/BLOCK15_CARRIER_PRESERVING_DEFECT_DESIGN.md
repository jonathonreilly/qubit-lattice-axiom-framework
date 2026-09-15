# Next leverage: retain the cluster carrier in convexification

Personal active draft,2026-09-14. Dario-Wu section3pp16-36 and its charge
definition2.15 onp14 have now been read. Bauerschmidt2016 PDFpp35-40 and47-52
(printed33-38,45-50) have been read. Neither entire source has been read.

The useful mechanism is a one-step Gaussian covariance split, followed by
a convergent connected-polymer expansion. It removes the nonsummable
long-range interaction from the expansion stage and leaves a small local
perturbation of a Gaussian field. The subsequent effective-field correlations
still require homogenization. The finite-clock gauge model has both electric
and magnetic defects, so the rotator theorem is not an automatic substitute.

A bookkeeping issue must be handled in any fresh derivation. Connected
clusters have connected unions of supports. Their *sum of signed charges*
need not have connected support after cancellation. The exact logarithm
must retain the cluster's carrier U, or an equivalent marked object,
instead of assuming that the resulting Fourier charge remains connected.
This is a scope/representation issue to check explicitly, not a claim that
the cited authors' main phase theorem is false.

Concrete candidate: in Z^3, let n1 be unit x-directed edges at x=0,...,R,
y=z=0. Let n2 be minus those edges at x=1,...,R-1. Then q_i=d n_i are
integer closed2forms with connected overlapping supports. Their sum is
the two endpoint-edge curls at x=0,R, whose support is disconnected for
R>=4. The order-two Ursell factor is -1. A sparse exact cochain check
should verify closure, support connectivity and the nonzero mixed cluster
coefficient directly. A3form analogue comes from differentiating a line
of2plaquettes inZ^4, to match gauge magnetic charge degree.

Working proof strategy for a supplied closed-charge gas:

1. On the p-cell graph, adjacent cells share a(p+1)cell; this graph has a
fixed dimension-dependent degree. Connected components of a closed
integer p-form are separately closed, because every local closure equation
only touches one such component. Gaussian charge-square weights factor.
2. Split a positive covariance beta G into beta(G-cI)+beta cI with
G>=2cI. The local Gaussian integration gives exp[-2pi^2 beta c ||q||^2].
The residual charge sum is an exact hard-core polymer gas.
3. Keep each polymer charge q_i and cluster carrier U=union supp(q_i).
Bound a rooted hard-core cluster by its tree expansion, with a polymer
smallness condition derived from Gaussian integer tails and connected-set
counting. Reserve half the activity exponent for total integer mass
s=sum_i ||q_i||_1, not just ||sum_i q_i||_1.
4. For each q_i use a controlled integer filling n_i supported in its
bounding cube. Then sum_i q_i=d(sum_i n_i), and a second derivative in h
is bounded by C s^(d+2)||d*h||^2 on the cluster bounding cube. Rooted
cluster mass decay beats this polynomial and the volume of possible
anchors. Thus |D^2 V(h,h)|<=epsilon(beta)||d*h||^2 with epsilon exponentially
small, provided the filling/boundary hypotheses are established.
5. Compare with the residual Gaussian precision. On a matched Hodge
Laplacian G=H^-1, (G-cI)^-1>=H. Then Hess H_eff >=(beta^-1-epsilon)H.
This is the candidate convexity lemma, not a full Gaussian scaling theorem.

Critical checks before any claim: boundary-compatible filling and positive
Hodge Laplacian; harmonic/winding sectors; real/nonvanishing partition
function after the cluster expansion; exact source transform for the actual
score; and the simultaneous electric/magnetic finite-clock representation.
A theorem for a separately supplied closed-charge gas must say so clearly.
