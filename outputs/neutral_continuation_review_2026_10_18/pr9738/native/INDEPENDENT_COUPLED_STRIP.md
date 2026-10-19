# Inspectable mathematical source

The argument below is supporting source under its stated hypotheses. Original checking narratives describe development history; they do not constitute a fresh capture or audit verdict. Exact original bytes remain in the recovery archive.

# Focused check: coupled coefficient model in the lower resonance strip

The algebra and perturbative scaling are correct. A uniform discrete-Airy endpoint-impedance lemma is the specific ingredient needed to turn the proposed pole-stability argument into a proof. It concerns this explicit coefficient model, not the full native Hamiltonian.

## Exact fast-block identities

Let F be the fast host plus confined arm, with d supported in the host, e the first arm site, and <d|F|d>=0. The stated model leaves Fd=K1_unconfined d, despite the arm confinement. For vA=Fd/2 and vD=-2e, resolvent algebra gives

M_AA=(z^2 Rdd-z)/4,
M_AD=-z Rde,
M_DD=4 Ree.

The host-arm coupling is -2. With host endpoint Green function G and isolated confined-arm endpoint Green function g,

Rdd=G/(1-4gG), Rde=-2gG/(1-4gG), Ree=g/(1-4gG).

Thus M_AD=2zgRdd as proposed. These identities hold for the outgoing continuation wherever the continued inverse exists. They do not require F to have a spectral gap.

The physical cross-coupling is Jz lambda^2 and the fast energy unit is Jz lambda, so the physical self-energy is Jz lambda^3 M. Dividing by the slow unit Jz lambda^2 gives delta=lambda M.

## Uniform strip estimate and analytic slow boundary

On a fixed disk of radius rho f_s around the partial slow pole, where f_s=lambda^2/8 and the disk stays a fixed fraction of its O(f_s) depth below the real axis, the corresponding fast imaginary part is of order lambda f_s, hence comparable to f_f=lambda^3/16. The previously checked transfer estimate uniformly bounds g above and away from zero there. With z=O(lambda) and the outgoing host estimate |G| comparable to log(1/lambda),

Rdd=O(1), Rde=O(1), Ree=O(1/log),
M_AA=O(lambda), M_AD=O(lambda), M_DD=O(1/log),
||delta||=O(lambda/log).

Indeed |1-4gG|>=4|gG|-1 grows, excluding a fast-block pole in this disk. The isolated arm has no nonreal poles. The disk is much smaller than its distance O(lambda) to the fast host's branch point, so a single outgoing local branch can be used.

Let G_s(E) be the outgoing two-source slow-host Green matrix, analytic and uniformly bounded near E=-2. Use

G_eff=(I-G_s delta)^-1 G_s,

which does not require G_s itself to be invertible. For small lambda the Neumann bound gives G_eff-G_s=O(lambda/log), analytically throughout the disk. In particular the endpoint self-energy changes by that amount. Cauchy estimates on a slightly smaller disk control its derivative by O((lambda/log)/f_s); it need not vary slowly on a fixed energy scale.

## Precise Airy pole condition

Write e for the full slow coefficient energy (host-shift variable E=e+4), so its arm bottom is e=-6. The arm starts at ell=3: n=ell-2>=1, hopping -1, diagonal -4+f_s(n+2). For a fixed Airy index, set

e=-6+alpha_k f_s^(2/3)+f_s w.

The needed uniform endpoint-impedance asymptotic is

m_arm(e)^-1 = (2-w)/(w-3)+o(1)

on a fixed complex neighborhood of w0=2+a, with derivative control there. Here Sigma0=G_s,AA(-2), a=Sigma0/(1+Sigma0), and neither 1+Sigma0 nor w0-3 vanishes. The limiting pole equation m_arm^-1-Sigma0=0 has root w0 and derivative (1+Sigma0)^2 with respect to w. Consequently the energy derivative is asymptotically (1+Sigma0)^2/f_s, nonzero.

There is an exact route to this lemma: the square-summable recurrence solution is proportional to J_(n+2-(e+4)/f_s)(2/f_s). The ghost-source condition therefore gives

m_arm(e)^-1 = -J_(2-(e+4)/f_s)(2/f_s) / J_(3-(e+4)/f_s)(2/f_s).

A uniform turning-point expansion of these Bessel functions near the simple Airy zero yields the displayed rational limit; the numerator and denominator each vanish at leading Airy order, so the error must be controlled one order beyond that common zero. Merely quoting leading absolute-error Airy convergence, or a finite-lambda simple pole without a uniform derivative bound, is not enough. This is the concrete remaining analytic proof obligation if it has not already been established in the coefficient-model work.

Given that lemma, the coupling-induced self-energy perturbation epsilon=O(lambda/log) shifts the pole by O(f_s epsilon)=O(lambda^3/log) in slow units. A Rouche argument on a contour of radius K f_s epsilon around the exact partial pole works: the unperturbed inverse boundary denominator is bounded below by a constant times K epsilon, while the perturbation is O(epsilon). Analyticity on the larger rho f_s disk controls derivatives and preserves uniqueness. The displacement is o(f_s), so the pole remains in the original lower strip. In physical units this is O(Jz lambda^5/log), smaller than the O(Jz lambda^4) partial width.

The disk may be chosen using the already established partial-model pole and its positive width; it must not be chosen by presuming the unproved coupled pole's width. With that ordering there is no circular application of the transfer-strip estimate.

## Scope

This supports stability of a fixed-index partial-model resonance under the specified fast coupling once the uniform endpoint lemma is supplied. It does not supply real-axis pointwise convergence, the full dressed readout, the missing native higher coefficients, equilibrium-state selection, or a native pole theorem. If the confinement or host potential is changed so that Fd differs from the stipulated K1 d, the M identities must be recomputed rather than reused.

## Lemma closure: checked turning-point scaling

The proposed error scaling is sufficient and correct. [DLMF 10.19.8](https://dlmf.nist.gov/10.19.E8) gives the transition expansion with complex transition parameter and order in a sector about the positive real axis. For uniformity, use the uniform turning-point expansion and its complex-order extension identified in [DLMF 10.20(ii)](https://dlmf.nist.gov/10.20.ii), rather than interpreting a merely pointwise fixed-parameter asymptotic as automatically uniform. The bounded complex order offsets here stay inside that sector and in a compact turning-point neighborhood.

In detail, put x=2/f, nu_c=x-alpha*f^(-1/3)+c. Then

2^(1/3)/nu_c^(1/3)=f^(1/3)(1+O(f^(2/3))),
-2^(1/3)*(x-nu_c)/nu_c^(1/3)=-alpha+c*f^(1/3)+O(f^(2/3)).

The first Airy-derivative term in the transition expansion has absolute size O(nu_c^-1)=O(f); it cannot be discarded as identically zero, but is exactly within the proposed error. Uniformly for c in a compact complex set, the expansion therefore gives

J_(nu_c)(2/f)=f^(1/3)[Ai(-alpha+c*f^(1/3))+O(f^(2/3))]
             =f^(2/3)*c*Ai'(-alpha)+O(f).

Here alpha is a fixed simple Airy zero magnitude. For c=3-w bounded away from zero, the denominator is bounded below by a constant times f^(2/3). Dividing numerator and denominator thus gives

-J_(nu_(2-w))(2/f)/J_(nu_(3-w))(2/f)
=-(2-w)/(3-w)+O(f^(1/3)),

uniformly on compact complex w sets avoiding 3. Cauchy estimates on a slightly larger such compact set give the same O(f^(1/3)) convergence for each fixed derivative. This supplies the missing endpoint lemma and uniform nonzero pole derivative for the explicit coefficient model.

It is important that the subsequent coupling shift is measured relative to the exact partial-model pole. The O(f^(4/3)) energy error of the basic Airy approximation can exceed O(f*lambda/log); the lemma does not upgrade that approximate location to the smaller coupling-error scale. With the exact partial pole as the comparison point, the previously stated Rouche estimate remains valid. No full-native conclusion is added by this closure.
