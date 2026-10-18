# Uniform heavy-patch embedding check

PASS for the proposed fixed-height, growing-transverse-box energy estimate, with the proof details below made explicit. This is a scoped mathematical check, not an audit or a claim of an optimized physical radius. I read the proposed embedding and the existing heavy-environment check, inspected `/tmp/neutral_probe_second_order.py`, and replayed its three exact rational controls successfully.

## Embedding and locality

For height four, a column with two walls has twelve configurations. Four singleton positions times the two majority signs give eight; the four length-two configurations are represented by two chosen complementary-pair representatives times a background sign. Thus position × six internal labels × aligned-column background has exactly the correct dimension. Fix those two half-column representatives once; do not count length-three intervals again as additional singleton states.

This identification is a tensor-product identification of bases, not an assumption that the energy-minimizing heavy environment equals the vacuum environment. A local number-conserving term whose support avoids the occupied column acts identically to its vacuum-block counterpart on the background. Terms that meet that column, including the difference from background terms that would flip that column, have only finitely many outgoing position blocks at fixed perturbative order. Their entries are bounded operators on the background. The operator-valued Schur row/column sum bound therefore gives a volume-independent norm for each defect difference. Whole-column flips at order four do not invalidate this argument: height is fixed, and such flips are local in transverse coordinates.

Consequently the stated decomposition is valid in a fixed local, number-preserving SW gauge, provided the local order-two identity is included as a native coefficient derivation. The three rational controls support that identity but are not themselves an all-background proof. The local two-step calculation must establish it for arbitrary background signs (the only signs involved are on the two-step neighborhood). No extensive vacuum term may be left in the defect remainder: the order-two scalar vacuum contribution must be subtracted first, as the control script does.

Singleton and half-column sectors have opposite global physical Z parity. Flipping an entire height-four background column does not change this parity. Hence their lack of mixing follows from an exact native symmetry, stronger than an order-two observation. Distinct singleton layers can likewise be tracked by longitudinal plane parities.

## The lower bound really has no order-two loss

Write T=Tx+Ty, where Tx and Ty are self-adjoint signed directional hopping operators with norms at most two. Set A=Tx+2I and B=Ty+2I. Then 0<=A,B<=4I, and, without assuming that Tx and Ty commute,

    (Tx-Ty)^2=(A-B)^2 <= 2A^2+2B^2 <= 8(A+B)=8(T+4I).

For D2=-(Tx-Ty)^2/8 this yields

    lambda T+lambda^2 D2
      >= -4lambda I + lambda(1-lambda)(T+4I)
      >= -4lambda I.

Thus the negative D2 is controlled by the excess above the first-order hopping minimum. The claimed lower gap 4J-4Jlambda-O(Jlambda^3) follows after adding the bounded defect remainder and the common background operator, whose expectation is at least its ground energy. The half-column block has zero first-order hopping and bounded order-two correction, so cannot lower this result for sufficiently small positive lambda.

## Patch trial

Take an actual ground density matrix of the vacuum coefficient block, trace out the reset patch, and tensor the resulting outside density matrix with a flat aligned-column state in the patch. Terms fully outside retain their expectation. All nonconstant vacuum terms first occur at order four; the number of affected fixed-range terms is O(ell^2), giving a cost O(Jlambda^4 ell^2). Scalar lower-order terms contribute no cost. A fixed-width flat margin accommodates all terms through order four.

Place the normalized two-dimensional Dirichlet sine wave on an ell by ell interior square. Its first-order expectation is -4 cos(pi/(ell+1)); extension by zero creates no extra hopping expectation. Since D2 is negative semidefinite, it can be discarded in an upper estimate even if its action exits the support. The remaining defect terms have norm O(Jlambda^3). A mixed trial suffices for the variational principle; no purification or dimension factor is required.

The upper error is therefore O(J[lambda/ell^2+lambda^4 ell^2+lambda^3]). For ell proportional to lambda^(-3/4), with R proportional to lambda^(-1), the patch fits and the error is O(Jlambda^(5/2)). Together with the lower bound, this proves the proposed energy asymptotic. It does not prove that an exact heavy ground has this patch shape, this radius, or a classical exterior.

## Transfer to the actual microscopic band

The global remainder O(JVlambda^5)=O(Jlambda^3) is small enough. The vacuum-block bandwidth above its scalar part is O(Jlambda^4 R^2)=O(Jlambda^2), so its entire band stays separated from the two-wall band.

For exclusion of N>=4, explicitly use the local wall-relative estimate, not the total norm O(lambda V). At orders one through three, subtract the scalar vacuum contribution termwise. A number-preserving local term then vanishes on its wall-free neighborhood; summing its bounded local wall projectors gives a form bound C Jlambda N. At order four one can conservatively retain the total norm C Jlambda^4 V. Thus these sectors have lower energy, relative to the common scalar, at least 2JN-CJlambda N-CJlambda^4 V. This places N>=4 uniformly well above the two-wall band along the stated family. Height-four winding terms start at order four and are covered by that last estimate.

Spectral perturbation by the global remainder then moves both relevant band bottoms by O(Jlambda^3). The result is an actual microscopic band-bottom gap estimate along this family, using the local finite-order SW construction. It is not a uniform-in-volume isolated single-particle pole, a statement about an individual eigenvector radius, or identification of the prepared vacuum environment with the relaxed heavy environment.

No material obstruction found. The two necessary packaging details are the noncommutative D2 inequality above and the all-N wall-relative bound for band separation; the finite random-background controls alone should not be described as the all-background order-two derivation.

## Addendum: conditional flux bound

The proposed constant eight is valid. In the singleton block let the background-valued amplitudes be psi_i and let U_ij be the diagonal signed-link unitaries. The exact form is <T+4>=sum_edges ||psi_i-U_ij psi_j||^2. Transport around one plaquette, rooted at any vertex i, telescopes to (I-P_p)psi_i. Unitary transport preserves each gradient norm, and the four-term Cauchy–Schwarz inequality gives

    ||(I-P_p)psi_i||^2 <= 4 sum_edges_in_p ||gradient_edge||^2.

Since P_p is an involution, its bad-flux probability at that root is one quarter of the left side. Summing four roots per plaquette and then using that each edge belongs to two plaquettes gives exactly

    F=sum_(i,p incident i) <psi_i,(I-P_p)psi_i>/2 <= 8<T+4>.

Together with the nonnegative background excess and the lower operator inequality already proved, an energy excess O(Jlambda^(5/2)) above 4J-4Jlambda forces <T+4>=O(lambda^(3/2)), and hence F=O(lambda^(3/2)). The O(Jlambda^3) defect/remainder contributes only O(lambda^2) after division by Jlambda. These statements hold for mixed states by linearity as well.

State the sector qualification explicitly: this formula is for singleton amplitudes. For a general low heavy state, project onto that block (or define F to vanish on the half-column block). The half-column weight is itself O(lambda^(3/2)) in a near-minimal state, because its energy is above the singleton minimum by order Jlambda; normalization after projection changes only this order. Exact parity separates the blocks. For an actual microscopic state, first use the SW-transformed state and the controlled band projection, rather than interpreting the bare microscopic plaquette measurement as F without dressing.

F is a particle-weighted local flux-defect probability. Its decay does not prove a flat region of any deterministic radius, a domain profile, or equivalence of the entire background to the flat background. The conclusion is uniform along R proportional to lambda^(-1), with fixed perturbative order and fixed height four, as in the preceding estimate.
