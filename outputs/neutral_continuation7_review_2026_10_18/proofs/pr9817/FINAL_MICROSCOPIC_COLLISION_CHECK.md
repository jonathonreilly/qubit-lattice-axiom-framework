<!-- Original PR9817 source SHA256 8197340d5ddf84bfbfe4870498d3b4cf637f97c6c8909bb8fa1ab89bde61179a. -->
**Source boundary:** Complete mathematical source follows. Historical verdicts, replay narratives and workflow instructions are provenance only. Mathematical identities and constructive arguments retain their explicit hypotheses; an old status supplies no current certification. Earlier exploratory statements must be read with the later corrections in this unit.

# Final focused finite-collision review

Disposition: PASS within the inherited uniform native block/embedding estimates. The revised controlled-collision section of `NATIVE_PAIR_SCATTERING_PROOF.md` closes the previously identified differentiated-threshold obligation. This is not a formal audit or a claim of a fixed-lambda microscopic S matrix.

## Regular-complement lemma

The definitions earlier in the proof make the new argument valid. Set t=1 and A=W^(-1)+C, where W^(-1)=0 on the hard core and equals 1/U on the nonzero potential sites. For the full-plane Laplacian L0=4-adjacency, its finite Green constant satisfies L0 C(r-s)=delta_(r,s). Let e be the all-ones support vector and Q the orthogonal projection onto e-perpendicular.

If Q A Q has a kernel vector v in that complement, then A v=b e. Define psi(r)=b-sum_s C(r-s)v_s. Because sum_s v_s=0, the logarithmic large-distance terms cancel and psi is bounded. On core sites, A v=b e implies psi=0. On potential sites it gives psi=v/U. On all remaining sites L0 psi=0, while on the potential sites L0 psi=-v. Therefore (L0+U)psi=0 on D, with the hard-core boundary condition.

The previously proved bounded-zero-solution exclusion forces psi=0 on D. Together with its zero core values this means its full-lattice extension is identically zero, so L0 psi=-v gives v=0. This contradiction proves Q A Q invertible. Negative but nonzero entries of U cause no issue: they enter through their inverse and the independent coercivity estimate already controls the full K. No unjustified positivity of A itself is needed.

This proves the required finite-complement statement, rather than inferring it from a scalar T asymptotic. The proof's hard-obstacle matrix is a resolvent representation of the same scattering domain as the bounded decoupled-core extension; the latter's extra finite core eigenstates have no scattering channel at threshold.

## Differentiated expansion

The Fourier split and analytic Morse-coordinate argument are sufficient at every fixed derivative order. Near the single nondegenerate minimum, angular averaging makes the numerator an analytic series in the radial energy. Integrating its monomials produces the common logarithm, a finite constant matrix, and E log E corrections. The remainder retains its order under each fixed number of E d/dE derivatives. Outside the small minimum neighborhood the denominator stays bounded away from zero for small E, so differentiation is harmless.

With the established regular complement, finite-dimensional Schur inversion leaves a single logarithmic denominator. Scaled derivatives of its inverse and of the remaining blocks are uniformly bounded for E=k^2 rho, rho in a fixed compact positive interval. Plane-wave support vectors are smooth, and the scaled energy-shell density is uniformly regular on the annulus. The proof now justifies fixed-order derivatives of the outgoing scaled profile rather than differentiating an unspecified o(1).

## Collision and native transfer

For either incoming f_k or outgoing S f_k, the finite-support Cook integrand is bounded by C_N k(1+k^2|s|)^(-N). Integrating gives C_N k^(-1)(Tk^2)^(1-N). Taking T=k^(-3), N=5 gives O(k^3) on each side. Using the usual wave-operator identification S=Omega_+^dagger Omega_- for the finite-rank comparison, this yields the stated S_T estimate. Artificial core components at the finite starting time are included by the norm estimate; no projection of them is required.

The finite-volume comparison is correctly assigned to scaled coefficient evolution. With k=lambda^(1/4), T=lambda^(-3/4), and R~lambda^(-1), Schwartz spatial tails and the coefficient LR bound make periodization errors negligible. No microscopic LR estimate over time T/(J lambda^10) is claimed.

The stated matched microscopic norm errors are

    O(lambda^(5/4))+O(lambda^(M-51/4))+O(lambda^(3/4))

plus periodization/preparation/readout errors. M>=20 makes the displayed terms o(1/log(1/lambda)). The common phase subtraction, dressed state preparation, and matched free-channel readout are explicitly retained. Their scope is essential.

Finally the density 1/(4pi t), angular normalization, and T=4pi t/(L+i pi) give s0=(L-i pi)/(L+i pi). A normalized radial annular packet therefore has ||(S-I)f_k||~2pi/log(1/k^2)~4pi/log(1/lambda), consistently larger than the controlled errors. This is a coherent packet-norm signal, not a rate, cross section, or empirical force.

No remaining gap was identified in the revised finite-collision reasoning itself. Its actual-H conclusion remains conditional on the cited uniform native block and embedding estimates and the specified matched operations, exactly as stated in the proof.
