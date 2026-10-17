## Fixed-spectrum endpoint orientation: complete conditional precision corollary

**Checked conditional composition.** This corollary keeps the nominal target and original delivered product seed while replacing the local emitter-endpoint block by a nearby real rotation with exactly fixed eigenvalues. For r=kappa_a/kappa0 in[1-10^-6,1], it gives complete operator bounds<.000347 infinite for t>=4e21 and<.001347 for one fixed M=2e23 device on[4e21,8e21]. The newer nominal disk onset10^19 is not transferred. Local fixed-spectrum and angular-domain algebra has a separate completed check; it does not by itself approve this full-device statement.

### Static supplied block and permitted orientation

Let kappa0=10^-8, g=J-E0>0, R=sqrt(g^2+4kappa0^2) and lambda_±=(E0+J±R)/2. Keep vacuum eigenvalue0 and double-occupation eigenvalue E0+J, and rotate only the positive one-excitation block:

    B(theta)=[[lambda_-+R sin²theta,-R sin theta cos theta],
              [-R sin theta cos theta,lambda_+-R sin²theta]].

The nominal angle is theta0=atan(2kappa0/g)/2. This is a real positive number-conserving two-qubit block on the same adjacent sites. It is a static Hamiltonian specification, not a rotation applied to the product seed. For the branch0<=theta_a<=theta0, kappa_a=R sin(2theta_a)/2 and the new matrix is

    [[E0+Delta,-kappa_a],[-kappa_a,J-Delta]],
    Delta=2(kappa_a²-kappa0²)/
             [g+sqrt(g²-4(kappa_a²-kappa0²))].

Thus Delta<=0, |Delta|<=kappa0²(1-r²)/g<8.4e-21 and |Delta|/alpha0<2.6e-6, where alpha0=kappa0²/J. The actual background endpoint diagonal is2J-Delta: the shift delta_b=-Delta is real and is NOT discarded. The scalar c_new, lead, old/source system, reference planes and graph are unchanged.

The exact one-sided allowed angle reduction is

    0<=theta0-theta_a<=w_eta,
    w_eta=[asin(s0)-asin((1-eta)s0)]/2,
    s0=2kappa0/R, eta=10^-6.

The checked local derivative bounds give eta*kappa0/R<=w_eta<=eta*kappa0/g. Exact q0,J imply g>.024, hence w_eta<4.167e-13. This upper width is NOT a sufficient error radius. A sufficient contained radius is eta*kappa0/R; the loose numerical one-sided radius3.125e-13 is sufficient because R<.032. These are sufficient structured contracts, not necessary fabrication limits.

### Actual background and the auxiliary reference

Introduce a mathematical auxiliary compensated device with the same kappa_a, E0+Delta and unchanged endpoint2J. Its reference is

    D_a=E-E0-Delta+(kappa_a²/J)z,
    F_a=i kappa_a E' z^21 rho_g/[sqrt(2pi)J D_a],
    p_a=integral_I |F_a|² dk, f_a=F_a/sqrt(p_a).

This reference is not relabeled as the exact changed-background reference. The final target remains nominal f0 and beta0, including its complete common phase. With P the real endpoint inclusion, H_b=(I-delta_b G)^-1, the ACTUAL background obeys

    R_b=R+delta_b RP H_b P^T R, G_b=G H_b,
    L_b=L H_b, R_bP=RP H_b,
    x_bg,b=x_bg+delta_b RP H_b P^T x_bg.           (FS1)

These identities use finite retarded matching kernels and preserve the full outgoing coefficient at its fixed plane. Transpose is not replaced by adjoint. Since |delta_b|<10^-20 and disk ||G||<36, ||H_b||<1+10^-18 and ||G_b-G||<1.3e-17.

The scalar changed-background reference would instead have A_b=1+(delta_b/J)z and denominator E-E0-Delta+(kappa_a²/J)z/A_b, with an additional outgoing factor1/A_b. That complex factor is charged through(FS1), not dropped as a phase or absorbed into the final target.

### Simultaneous Schur, profile and mass margins

Both comparison emitter blocks already include Delta and kappa_a. Their complementary gap exceeds .18-|Delta|-.062rho-36.000001 kappa_a²>1/6, so all seven complementary inverses are<6 before their use in the resonant Schur scalar. The checked background perturbation subtraction then extends at these same shifted parameters to

    |s_b-s_c|<=1.3e-17[1+432kappa_a²+46656kappa_a^4]<1.4e-17,
    |ds_b/dE|<=35001+kappa_a²[2*35001*6*36+72*36²]<36000.

Here s_c is the auxiliary compensated self-energy, not the nominal unshifted one. Delta is constant in energy and cancels in the relative resonant denominator comparison. The outgoing numerator difference is<1.3e-17, and

    |Dj,b-Dj,c|/|D_a|<1.1e-18,
    |Fj,b/F_a-Fj,c/F_a|<2e-18.

The underlying compensated profile bound has intercept<1.761e-13 and slope<750, uniformly for this coupling range. Its unrounded slack therefore preserves

    |Fj,b/F_a-omega_p|<2e-13+750|k-k0|.           (FS2)

This does not claim unchanged epsilon_G or epsilon_L against untransformed approximations. All eight emitter coordinates and the actual complex row are retained.

Center the ACTUAL seed measure at E0+Delta and use d_a=v sigma-|Delta|. Then [Delta-d_a,Delta+d_a] lies inside the original certified energy band and d_a>d(1-2e-12). Center constants A=35,B=17,b_min=12 retain explicit margin from the comparison to -z/J and the1.4e-17 perturbation. The mass lemma's smallness remains<4e-10, its logarithm<18 and H<46. Tail<4.534e-8 plus actual regularity term<3.067e-9 gives exterior mass<4.85e-8 and amplitude<.000221. The auxiliary reference uses its separate derivative<1334, giving1-p_a<4.54e-8. All exterior spectral types, including point mass, remain charged.

The perturbed real matching inverse and unchanged single open boundary supply the same local Stone/synthesis argument. No global scattering completeness is inferred. Since |Delta|/alpha_a<2.600006e-6, the auxiliary restricted moment stays ||(k-k0)f_a||<.21kappa_a. Equation(FS2) gives mismatch<1.6e-6. Preparation pays sqrt2<1.415 for overlapping old columns within parity; outgoing fibers are orthogonal and pay2delta. Thus the complete static cost to the auxiliary packet is

    <1.415*(.000221+.0000016+.0000000454)+.0000032
     =.000318243241<.000319.                      (FS3)

### Complete source, contours and fixed nominal comparator

Use h=10^-18 and T=4e21. The unrounded background source bounds in the endpoint-perturbation interface yield ||R_bP||<4.1e11 and ||x_bg,b||<2e9. They depend on delta_b alone. Disk Cauchy with ||G_b||<36.000001 and both complementary corrections gives exact self-energy oscillation<.000038. The real imaginary factor remains>12kappa_a²; since .062h/kappa_a²<.000621, the strip margin is>6kappa_a². Thus the full emitter inverse is<.18/kappa_a² on the bottom.

Both cutoff sides retain

    |Dj,b|>=v sigma-|Delta|-.061h²-kappa_a²*36.000001
                           -6kappa_a^4*(36.000001)²>2.49e-8,

so the side inverse is<5e7. The complete source solution uses V_b=[-kappa_a R_bP;I] and all904 coordinates. The bottom estimate changes by at most1/r<1.000002 and stays C_b<5e20; the sides stay C_s<1.4e13. C subtracts ACTUAL open waves using R_inst=u^T x-1. Its closed tails retain roots<1/6 and uniform Hilbert-valued holomorphy; ||C||<=3||x||+4. No off-real unitarity is invoked.

For a0,j=conjugate(omega_p f_a), the detuned Dbar has the same exact exp(-y) imaginary sign. Its bottom bound .088/kappa_a and side44kappa_a/sigma give localized bottom<6.601e-9 and both sides<=9.24e-8, including overlap factors. Hence complete localized error<1e-7. The auxiliary incoming and outgoing contours retain h_i=sigma/2 and h_o=kappa_a²/(4J²)>2.5e-14; subtracting |Delta| leaves their cutoff margins. Both scalar tails are<1e-10, with phase113 retained, and positive target normalization costs<1e-20. These are contours of the auxiliary packet, not an unsupported substitution for the changed-background scalar denominator.

Combining with(FS3) gives actual-to-auxiliary error<.000320. The exact auxiliary-to-nominal ratio rD0/D_a has

    eta<2.5*(2e-6+2.6e-6)=1.15e-5,
    ||f_a-f0||<=2*(1e-6+eta)/(1-eta)<.000026.

Fourier restriction is contractive; the two target normalization adjustments add<2e-20. Therefore complete infinite error to the FIXED nominal target is<.000347 for t>=T. The comparator retains exp(-ic_new t), blank emitter/other-clock/source, and exp(-itK)W on the literal old system with arbitrary passive reference. Only fixed scalar profiles are conjugated, never input coefficients.

The two-site perturbation norm is sqrt(Delta²+(kappa_a-kappa0)²)<1.1e-14, preserving radius18. Geometry and distance M+23 are unchanged. At M=50T=2e23 the finite transfer adds<.001 on[T,2T], yielding<.001347 with M+116 qubits and the same embedded infinite nominal target. Unhalved trace ceilings are .000694/.002694. No all-future finite storage follows.

### Supplier interpretation and provenance

A supplied isospectral block encodes correlated hopping and two diagonal changes without separately specifying uncertain compensation entries. It does not supply the eigenvalues natively. At fixed theta, eigenvalue errors shift the emitter diagonal by epsilon_- cos²theta+epsilon_+ sin²theta; a common shift moves both one-excitation diagonals, and is not a global phase relative to the unchanged vacuum/lead. Generic spectrum or whole-block scale errors remain outside the contract. The seed remains the original basis product state. No native identification, thermal preparation, practical resource or generic robustness claim follows.

Sources under renewal_20261017_110934:

- Full-device proposal fixed_spectrum_composition/PROPOSAL.md:167780ae8a31b3bb0dbc8daee76518390b77978105bca1e7124636feb4d1ba12; completed composition review fixed_spectrum_composition_check/REVIEW.md:4e85d1982bd8b8193874ea7dd575aa67edcb4e374e0458216c31c26ea9eaf586.
- Local fixed-spectrum interface:548c8579d603200db45c7c7f4fdd3f2cef08aee53846efe524ef94591b692057; local review:d370f70e5232904389368434a18a88407d30474b98b030a03c96e4d2e24fc7ce.
- Background perturbation proposal:8c308e8d699122318f41fc0195028f3626ba3bd14558d589b3271f16a6c7d32e; check:a7fd6b54e1be5fe21e2001d8509bf8961247ee47c506968ae0eed46db08906fd.
- fixed_spectrum_orientation_scope/QUALIFIED.md:d9b13303f9a2f0aa21ce1991748d66787f3e71b35919f845ac0765ad1be60462; review:00cc88339fbd6864bc756600403ca25bb960bc13e92ffcb8ef4920482a1dbefe.
- Canonical note used by the composition:7b59fd7cf2b8d524b4f1478d883c71070856e9377f08b901864a44867ebc3d78, root-supplied milestone dcb635da85dc22809a14ba815c2219431219c9e5; no new Git verification.

The original angular assessment25221ebc70b09702b38aa626410f7760c57968d732b2c0b620c46fda548afaa3 described an upper bound on interval width as a sufficient tolerance. The selective reviewer corrected that implication: sufficient angle-only control uses the exact width or its LOWER bound, not4.167e-13. The qualified revision also restricts eta to[0,1] and distinguishes positive kappa from its negative signed hopping entry. The original remains preserved; this draft incorporates the correction.

This draft is by the composition author, with earlier weighted/precision/component authorship exposed. It is not another independent check. The completed full-device reviewer authored the reused background-perturbation proposal and local fixed-spectrum review; this was a source-exposed check of a different author’s simultaneous integration, not a new independent origin of those components, ancestral recertification or audit. The report was read completely before this draft status update. No retained/audit status is assigned. The analytical derivation and selective reviews performed no scientific execution. Actual corroboration, if run, is reported separately and is not a proof or audit. No physical axiom or editable prompt changed.
