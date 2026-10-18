# Longitudinal COM pole: focused mathematical check

Disposition: PASS conditional on the separately requested native COM vertex/host identification, with one harmless support-count correction below. Read /private/tmp/neutral_com_pole_root.md. No repository edits or numerical pole grid performed.

## Scaling and normalization

With interval center (left+right)/2, moving either endpoint by one changes the center by +/-1/2. Two equal endpoint amplitudes -1/2 therefore sum to -cos(p/2)=-gamma. For real p in a sufficiently small fixed compact neighborhood of zero, gamma has a uniform positive lower bound. Given the asserted -gamma A arm-host vertex, the eliminated boundary is Sigma_p(E)=gamma^2 G_AA^hole(E), with E measured after subtracting 8-4lambda^2 and dividing by Jz lambda^2. Both factors of gamma are required.

Divide the long arm by gamma. The NN operator is -T+(f/gamma)(n+2), its energy is E/gamma and its boundary parameter is Sigma_p(E)/gamma. The Airy formula consequently returns

 E=-2gamma+alpha1 gamma^(1/3) f^(2/3)+f(2+a_p)+..., 
 a_p=Sigma_p(-2gamma)/(gamma+Sigma_p(-2gamma)).

Thus the physical Airy coefficient is alpha1 gamma^(1/3) lambda^(10/3)/4, and the width is [-Im a_p]/4 times Jz lambda^4. The frozen-boundary endpoint derivative is f gamma/(gamma+Sigma_p)^2 to leading order, hence O(f/gamma) uniformly on the chosen compact p set. There is no missing gamma in the leading width prefactor: it is already inside a_p.

## Radiation and uniform continuation

The slow square-host Fermi curve at E=-2gamma is u+v=gamma. Its critical energies remain away for gamma near1. The scalar hole basis restricts to constants there, while Ahat=2gamma^2-4uv-2 is nonconstant on regular arcs. Hence the same Schur spectral-density argument gives strictly negative Im G_AA. Continuity and compactness on a sufficiently small p neighborhood make the strict bound and hole invertibility uniform. Also Im a_p=gamma Im Sigma_p/|gamma+Sigma_p|^2<0. The slow pole therefore lies at uniform negative depth comparable to f.

The prior range-two perturbation proof extends after this rescaling: coefficients/ranges and gamma are uniformly bounded, isolated Airy spacing scales as gamma^(1/3)f^(2/3), and fixed-endpoint residues remain O(f). Higher long-arm Hermitian kinetic coefficients have a real band-bottom first-order shift; their non-Hermitian projection corrections are smaller. Thus an unspecified real fourth-order bulk shift can coexist with the explicit leading width. Merely bounding an arbitrary complex perturbation by O(lambda^2) would not establish that width; the actual real/Hermitian bulk structure and localized estimates are the needed inputs.

The fast target is z=-(4+2gamma)lambda+O(lambda^(7/3))-i Theta(lambda^3). Its separation from the fast saddle -4lambda+O(lambda^2) is -2gamma lambda+o(lambda), uniformly comparable to lambda. The finite-range Morse/log proof and corrected fast-arm strip argument therefore remain uniform after the bounded gamma rescaling, provided the separately checked native leading coupling remains nonzero. The weaker finite-contact estimate O(lambda log(1/lambda)) is sufficient and yields a physical O(Jz lambda^5 log) pole shift. As before, use its holomorphy only on the already established lower depth-f disk, not on the large Airy contour.

The closed-arm threshold stays near 8-4lambda^2, whereas the candidate slow energy is lower by 2gamma lambda^2. The fixed-order positive-slope lower bound and finite-interface support therefore retain their uniform gap and Schur estimates. No new small denominator occurs as long as p stays in this fixed neighborhood and gamma does not approach zero.

## Dispersion statement and correction

For any fixed nonzero sufficiently small p, the difference from p=0 has positive leading real term 2(1-gamma)Jz lambda^2. This establishes nonflat longitudinal dispersion of the continued coefficient pole. The formal second derivatives of the displayed terms at zero are Jz lambda^2/2 and -alpha1 Jz lambda^(10/3)/48. Uniform bounds for real p alone do NOT license differentiation of the error; the draft correctly leaves error-controlled curvature/group velocity open.

Correct the statement that translating the entire feature transversely always changes 4ell spins. A translated pair can share one column with the original pair and then changes only 2ell. The sufficient bound is at least 2ell, still growing with ell; fixed-order deep-arm transverse translation is therefore excluded. This correction does not change any COM formula or asymptotic conclusion. Endpoint contacts can carry transverse dispersion, and no all-orders immobility is implied.

The native vertex and bulk-host identification are separate inputs being checked elsewhere. Conditional on them, the mathematical extension has no additional obstruction. It remains a fixed-order compact coefficient pole, not a physical wavepacket propagation theorem, Lorentz dispersion, isotropic mediator, microscopic pole, state-selection result or cosmological identification.
