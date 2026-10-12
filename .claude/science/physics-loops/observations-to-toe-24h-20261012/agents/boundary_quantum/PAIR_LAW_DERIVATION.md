# Boundary-conditioned binary pair law

This is an explicit comparison model with a new permitted statistical premise. It is not a derived theory of quantum dynamics, a claim of novelty, or a connection to the scalar-mediator block.

Let a,b be unit setting vectors, c=a·b, θ=arccos(c), and λ have uniform prior measure dΩ/(4π) on S². Define

    A=sgn(a·λ), B=−sgn(b·λ),
    ρ_k(λ|a,b)=exp(−kcAB)/(4π Z_k(c)), k≥0.

One common k applies to every setting pair. The conditional λ statistics explicitly depend on both settings. The deterministic response functions alone therefore do not imply measurement independence.

## Normalization and correlation

The azimuth of λ projected into the a,b plane is uniform. The two opposite-sign sectors of sgn(a·λ) and sgn(b·λ) have total azimuthal measure 2θ. Thus, for S=AB,

    E₀(c)=−1+2θ/π,
    P₀(S=s)=(1+s E₀)/2.

Tilting the two masses by exp(−kcs) gives exactly

    Z_k(c)=cosh(kc)−E₀(c)sinh(kc),
    E_k(c)=[E₀ cosh(kc)−sinh(kc)]/Z_k(c)
          =tanh[atanh(E₀(c))−kc].

The last expression is interpreted by continuity at c=±1. Equivalently E_k=(w₊−w₋)/(w₊+w₋), where w₊=(1+E₀)e^(−kc)/2 and w₋=(1−E₀)e^(kc)/2. The normalized joint outcomes are

    P_k(A=u,B=v|a,b)=[1+uv E_k(c)]/4.

This result also follows by differentiating log Z with respect to kc: E_k=−∂log Z/∂(kc), treating the prior E₀ at the selected settings as fixed. The numerical check integrates the original sign-response sectors directly over azimuth, without using E₀ to construct those sectors. Across 127 separations and k∈{0,.1,.5,1,5,20}, correlation disagreement was 1.34×10⁻¹⁵, relative normalization disagreement 4.43×10⁻¹⁶, and marginal disagreement 2.23×10⁻¹⁶.

## Symmetries and limits

Under λ→−λ, both outcomes change sign, while AB and the density do not. Therefore each binary marginal is exactly 1/2 for every a,b. This proves operational no-signaling for the supplied two-party conditional distribution. It does not supply a causal mechanism for the setting dependence.

A common orthogonal transformation of a,b,λ preserves both responses and the density. Reversing a maps A→−A and c→−c, leaving cAB invariant. The same holds for b. Consequently E_k(−c)=−E_k(c), as required by outcome relabeling represented by reversal of the corresponding labeled setting vector. Exchange of the parties gives the same joint outcome statistics because the marginals are fair and E depends only on c. An output-bit flip with settings held fixed changes the representation of the correlation to −E; one must apply that convention consistently, rather than keep an unchanged singlet formula.

At k=0 the law is the triangular measurement-independent control. At c=1 it gives E=−1, at c=−1 it gives +1, and at c=0 it gives zero for every k. As k→∞, E→−sgn(c) away from c=0. In the standard CHSH geometry,

    S(k)=4 tanh[atanh(1/2)+k/√2],

which runs from 2 to 4. The quantum value 2√2 occurs at k=0.4696142810683679. Exceeding a Bell-local or quantum bound here is not a loophole in those theorems: the pair law has supplied setting-dependent hidden statistics, and no quantum-state axiom has been assumed.

For linear polarization, physical analyzer axes α,β map to Bloch vectors with relative angle 2(α−β). The Φ⁺ convention has positive cosine correlations on this real polarization plane. A consistent local output flip converts the singlet comparison to C_k=−E_k. The published scan coordinate used in the accompanying conditional fit is a separate instrument question and is not established by this geometric polarization identity.

## Exact obstruction to a shared-k cosine

For c>0, write u(c)=2 arcsin(c)/π. A shared-k law equals the quantum singlet cosine at this one interior setting precisely when

    k_Q(c)=[atanh(c)−atanh(u(c))]/c.

For Bloch separations 30°,45°,60° these values are 0.5914825806, 0.4696142811 and 0.4054651081. Thus even these three ideal correlations cannot be reproduced with one common k. As c→0, k_Q→1−2/π. As c→1, k_Q diverges. Choosing a separate k(c) would change the model into a supplied angular function and would abandon its one-parameter prediction.

An exact local distinction is stronger. For θ↓0 and finite k,

    E_k(cos θ)=−1+(2/π)e^(−2k) θ+O(θ²),
    −cos θ=−1+θ²/2+O(θ⁴).

The boundary law retains a linear cusp. A calibrated common visibility V>0 multiplies both expressions and preserves that distinction. Angular jitter convolves and rounds a cusp, so the actual analyzer-angle distribution must be independently measured and included in a prospective forward model.

## What composes and what is absent

For physically independent pairs, a separately postulated independent prior ∏ᵢdΩᵢ/(4π) and additive boundary weight ∑ᵢk cᵢ AᵢBᵢ factorize into a product of the supplied pair distributions. This establishes only that limited tensor-product analogue. Shared randomness, interacting preparation, and adaptive setting choices need separate models.

There is no general multipartite state or operation law here. In particular, blindly demanding the same singlet pair formula for all three pairs of three binary outcomes is impossible at equal settings: AB=AC=−1 entails BC=+1, while the third singlet condition requires BC=−1. A viable extension needs a specification of which multipartite preparations exist and their consistent joint distributions; this observation does not rule out all possible extensions of the pair model.

The candidate supplies neither state preparation probabilities nor sequential measurement updates, general instruments/POVMs, entanglement swapping, multipartite monogamy, field dynamics, spacetime causal dynamics, or a mechanism that produces the boundary statistics. Its exact fair two-party marginals do not settle those questions. It is an operational binary-pair alternative suitable for a multi-angle shape test, not a TOE.
