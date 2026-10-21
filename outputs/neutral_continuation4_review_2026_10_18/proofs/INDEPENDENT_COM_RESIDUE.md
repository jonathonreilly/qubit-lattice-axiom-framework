<!-- Owning original: PR9764; source SHA256 3d18d84bff043ef5b58b22f70259d615d0685fa276f0c0237f3d53ea7878011f. -->
**Source boundary:** Complete mathematical source follows. Original review dispositions, execution stories, provisional questions and PASS labels are historical annotations, not current certification. Later explicit addenda supersede earlier provisional statements. Mathematical hypotheses and conclusions are retained; terminal exclusion interpretations require separate admission and are not promoted by this source enclosure.

# Longitudinal COM original-readout residue

Disposition: PASS, conditional on the previously checked complete fixed-order COM pole and the independently checked native momentum vertices. The nonzero overlap at p=0 has an analytic proof; it need not be assumed from quadrature. Read /private/tmp/neutral_com_source_root.md and /private/tmp/neutral-com-effective-source-check.md. No repository edits or formal audit.

## Normalization and residue

The centered physical Fourier readout uses exp[ip(z+1)] at the distance-two bond midpoint and 1/sqrt(V). A same-layer two-spin flip gives -8 exp(ipz) cos(p)/sqrt(V). The first dressed source is therefore -sqrt(2)lambda cos(p)d. The verified native vertices and fast contraction give the slow-host source lambda² cos(p)/gamma times u0, with gamma=cos(p/2), u0=(A+2D)/sqrt(2). These are uniform limits only on the established outgoing lower strip with gamma bounded away from zero.

Eliminating the slow host through the -gamma A link cancels the inverse gamma in that source: the endpoint source is -lambda² cos(p) u0^T G(-2gamma)A+o(lambda²). The rescaled Airy derivative gives

 P11=f gamma/(gamma+Sigma_p)^2+o(f),
 Sigma_p=gamma² G_AA(-2gamma), f=lambda²/8.

Multiplication produces exactly

 Res(C_p)=lambda6 R(p)+o_m(lambda6),
 R(p)=gamma cos²(p)[u0^T G(-2gamma)A]^2/[8(gamma+Sigma_p)^2].

Both factors of gamma in Sigma_p and the additional gamma in the endpoint derivative are required. There is no further energy-unit factor: conversion of the resolvent and conversion of the pole denominator cancel. For the physical C_-p/C_p response the real interval-center convention gives equal real leading fiber sources before continuation; the continued pairing is the analytic transpose square, not a modulus-square or positive probability.

The same fixed-endpoint residue and localized Cauchy estimates used previously control the complete fixed-order source and finite-contact errors uniformly on a sufficiently small fixed real-p interval. The source error is generally logarithmic, not O(lambda); it still gives o(lambda6) after pairing with the O(f) endpoint residue. This does not imply differentiated-error bounds or a pointwise real-axis limit.

## Analytic proof of a nonzero overlap at p=0

Let G_free=(E+i0-H_square)^-1, g_cA=<c,G_free A>, and g00=<c,G_free c>. In the scalar hole basis c=delta0, s=sum_nearest delta/2,

 H_square c=-2s,
 H_square s=-2c-A-2D.

For b=G_hh^-1 G_hA and x=G_free(A-hb), x has zero hole components and equals the punctured response on its complement. Thus b=H_hQ x. The c row has no Q coupling, so b_c=0; the s row gives b_s=-sqrt(2)u0^T G_hole A. Equivalently the free identities give G_hA=(g_cA,-E g_cA/2), and hence

 b_s=-2g_cA/(E g00-1),
 u0^T G_hole A=sqrt(2)g_cA/(E g00-1).

At E=-2 the free Fermi curve is u+v=1, with u=cos(kx),v=cos(ky) necessarily in [0,1]. There Ahat=cos(2kx)+cos(2ky)=-4uv, strictly negative on regular arcs of positive measure. Therefore

 Im g_cA=-pi integral Ahat delta(-2-h(k)) dk/(2pi)^2 >0.

The numerator cannot vanish. The denominator is nonzero because Im g00<0 at this regular interior energy and E=-2 is nonzero. This proves the desired overlap is nonzero analytically. Also Im Sigma0<0 gives 1+Sigma0 nonzero. By continuity of the chosen local outgoing continuation, the overlap, gamma, cos(p), and denominator remain nonzero on a sufficiently small real-p neighborhood. Thus R(p) is nonzero there without a numerical lower-bound premise. The quoted p=0 decimal is a supplementary evaluation of this nonzero analytic coefficient.

The theorem remains a source residue of the complete fixed-order coefficient continuation. It does not establish the actual microscopic pole, positive isolated spectral weight, detector identification, cosmological state or a Lorentz/isotropic propagation law. A finite-time Fourier-window comparison with modulus-one phases is a separate statement and cannot itself transfer poles.
