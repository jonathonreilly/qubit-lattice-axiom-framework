<!-- Original PR9790 source SHA256 6587bd9ea47cd74ec67e8d84c7b1821217dba74214af118fcc2c044fa77aefc5. -->
**Source boundary:** Complete mathematical argument follows. Historical verdicts, execution narratives and provisional instructions are provenance only. Exact identities and conditional mathematical implications remain live; no audit status or additional physical premise is conferred. Earlier exploratory statements are read with their explicit later corrections.

# Auxiliary plaquette-source expansion check

Disposition: PASS for the first-order amplitude / second-order weight in the auxiliary u expansion of the finite leading coefficient model. This is not a controlled numerical remainder estimate at the native point u=1. No shared edits or new physical coupling.

Let K(u)=-5E-4uP in the physical column-X basis, with E the sum of nearest-neighbor diagonal pair signs and P the sum of four-site plaquette flips. In the all-plus sector, a single plaquette flip changes eight exterior edge signs from +1 to -1. Its K(0) cost is 5 times16=80. The perturbing matrix element is -4u, so the ground correction is +u/20 times the sum of plaquette states. Distinct plaquette states are orthogonal on the sufficiently large periodic transverse grids under consideration. Small exceptional geometries with duplicate/wrapping plaquette supports are not covered implicitly.

Write E_Q=sum_edges cos(Q_a/2)exp(-iQ.edgecenter)E_edge and C=cos(Qx/2)cos(Qy/2). Relative to the plaquette center, its four horizontal exterior edges have centers (+/-1,+/-1/2), and its four vertical exterior edges (+/-1/2,+/-1). Each diagonal sign change is -2. Their weighted sum is exactly

 Delta E_Q=-8 C[cos(Qx)+cos(Qy)]exp(-iQ.plaquettecenter).

I independently evaluated this finite edge sum at zero and two generic momenta, agreeing to floating roundoff. This also proves the phase and cosine factors by pairing opposite edges.

For O_Q(u)=-12u C sum_p exp(-iQ.p)P_p-18E_Q, the direct vacuum-to-plaquette amplitude is -12u C exp(-iQ.p). The ground correction contributes (-18)(u/20)Delta E_Q after removing the vacuum scalar, giving +(36/5)u C[cos(Qx)+cos(Qy)]exp(-iQ.p). Thus the connected leading source vector in the continued one-plaquette sector has amplitude

 u C[(36/5)(cos(Qx)+cos(Qy))-12]exp(-iQ.p)+O(u^2).

At nonzero allowed Q, the vacuum Fourier scalar vanishes. At Q=0 it does not: the corresponding excited-state vacuum admixture is -u/20, cancelling the source's vacuum scalar and leaving precisely the difference Delta E_Q. Equivalently, apply the connected source to the corrected ground and use the block rotation; either derivation yields the same subtraction. Omitting it would incorrectly retain an extensive constant. Degeneracy within the one-plaquette sector is harmless when summing the entire cluster's weight; this is not a claim that each plaquette basis vector remains an eigenstate.

There are R^2 orthogonal plaquette images, so the cluster weight is

 R^2 u^2 C^2[(36/5)(cos(Qx)+cos(Qy))-12]^2+O_R(u^3)

at fixed R. At Q0 its coefficient is (12/5)^2=144/25=5.76 per plaquette. At zeros of the leading factor, retain an absolute error statement rather than a relative approximation. A symmetry may improve the remainder but is not needed or asserted here.

The comparison 5.8307 at u=1 versus5.76 is a numerical observation, not a certified small error from this expansion. u is a mathematical interpolation in the leading model; physical native coefficients are fixed at u=1. Restoring original microscopic source normalization still requires lambda^4/(128sqrt(V)), squared for weight. This calculation neither adds a tunable physical interaction nor proves a microscopic pole, uniform thermodynamic response, or empirical coupling.
