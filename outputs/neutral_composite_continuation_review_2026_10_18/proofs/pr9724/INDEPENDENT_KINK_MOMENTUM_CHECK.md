# Supporting mathematical source

Original: `.claude/science/physics-loops/neutral-composite-24h-20261018/native/INDEPENDENT_KINK_MOMENTUM_CHECK.md`, SHA256 `6221d468d063f066b407dbc0175bb478156a32c393607b6bacf4f1e547573379`. This extract preserves the mathematical argument and its limitations; historical execution descriptions are not fresh evidence. Current promotion boundaries: `docs/work_history/repo/review_feedback/NEUTRAL_CONTINUATION_BOUNDARIES_2026-10-18.md`. Original report and verdict history are recoverable in the archive manifest.

# Conditional general-momentum kink self-energy check

The proposed real self-energy, leading full linewidth, and small-q curvature are algebraically correct for the specified effective half-line model. This report independently derives them; it does not independently derive the supplied native coefficients or establish a native thermodynamic resonance. No root files were edited.

Take q in the principal interval (-pi,pi), c=cos(q/2)>0, u=cos q, t=2c, and lambda=Jperp/Jz. Fix q away from pi while lambda tends to zero. Let g(z)=(z-A)^(-1), where A is the half-line hopping-t operator. Its boundary resolvent is (z-sqrt(z²-4t²))/(2t²), continued with the retarded sign. At z=0+i0:

g00=-i/t, g10=-1/t, g12=0, g11=0, g11'=-1/t².

The last three identities follow directly from the half-line resolvent recurrences; in particular g12 must not be replaced by the bulk nearest-neighbor Green function.

## Real shift, including B

Write w1=-sqrt(2)|1> and w2=-sqrt(2)c|0>+c|2>/sqrt(2). Through order lambda³,

Sigma=lambda² <w1,g(z)w1> + lambda³[<w1,g B g w1>+2<w1,g w2>]+...,

with z=-2lambda at the necessary leading side energy. For B=alpha A²+beta I+delta P0, use g²=-g' and g A² g=z²g²-2zg+I. Thus at zero energy

(g B g)11=alpha+(beta+delta)/t²,

and beta+delta=1/4, alpha t²=-u/4. Including z=-2lambda gives

G11=lambda[2/t²+alpha+(beta+delta)/t²]+O(lambda²)
    =lambda(9-u)/(4t²)+O(lambda²).

The cross term is 2<w1,g w2>=4c g10-2c g12=-4c/t=-2. Therefore

Re Sigma=lambda³[(9-u)/(2t²)-2]+...
        =lambda³(1-9u)/(4(1+u))+... .

The B insertion is required for this coefficient. The supplied host C begins too high to affect this order. Evaluating at the shifted pole rather than -2lambda changes this result only at higher order, provided the fixed-q perturbation expansion remains regular.

## Width and its zero

B00=alpha t²+beta+delta=(1-u)/4 and B02=alpha t²=-u/4. The host boundary scattering equation is

z phi0=t phi1+lambda[(1-u)phi0/4-u phi2/4]+O(lambda²).

At z=-2lambda, phi2=-phi0+O(lambda), so phi1=-9lambda phi0/(4t)+O(lambda²). The complete supplied side-to-on-shell vertex then is

<w,phi>=lambda² sqrt(2)[9/(4t)-3c/2]phi0+O(lambda³)
        =3sqrt(2)(1-2u)lambda² phi0/(8c)+O(lambda³).

The unperturbed boundary spectral density is rho0(0)=1/(pi t). Consequently the FULL linewidth (-2 Im pole, not its half-width) is

Gamma/Jperp=2pi rho0(0)|3sqrt(2)(1-2u)lambda²/(8c)|²+...
           =9(1-2u)²lambda^4/(32c³)+... .

At q=0 this gives 9lambda^4/32 and Re Sigma=-lambda³. At q=±pi/3 the displayed amplitude cancels. This is only a zero of the leading decay coefficient. It does not prove an exact bound state in the continuum, protected zero width, or absence of higher-order/additional-channel decay. A joint q-near-cancellation/lambda limit needs a new expansion. The host C correction does not alter the displayed on-shell amplitude because it first changes phi1 at order lambda²; it may matter at the next order, especially at this cancellation.

## Physical energy and curvature

Taking the supplied native side-diagonal fourth-order difference -73/192 as input gives the displayed resonance-center expansion

E(q)=8Jz-2Jperp²/Jz+(Jperp^4/Jz³)[-73/192+(1-9cos q)/(4(1+cos q))]+higher orders.

The rational self-energy coefficient expands as -1+(5/16)q²+O(q^4). Therefore the conditional small-q curvature is +(5/16)Jperp^4/Jz³. I verified this derivative independently. I did not independently rederive the native -73/192 coefficient; agreement at finite L8/10/12 is supplied evidence, not an all-size proof in this report. A curvature of a resonance center does not itself identify a stable particle or a relativistic scalar dispersion.

## Scope and continuum limits

For a finite ring/relative chain all eigenvalues remain real and discrete. Width requires an infinite-volume continuum limit or a controlled approximation to it; artificial numerical broadening is not intrinsic decay. The leading coefficient assumes the supplied side/host coefficients continue to that half-line, the source-accessible channel is complete to this order, no omitted channels contribute comparably, and the effective expansion is uniform enough to control the resonance limit. Finite matrix extraction alone does not settle those assumptions.

Near q=pi, t approaches zero, the side energy need not lie inside the host band, and the stated fixed-q expansion becomes nonuniform. The c^-3 expression must not be extrapolated there. If a momentum convention allows c<0, gauge the hopping sign and use the positive boundary DOS 1/(pi|t|); the displayed c³ formula presumes the principal interval above.

Physical original-observable dressing determines visibility independently of this Hamiltonian linewidth. None of these calculations supplies a physical detector vertex, a cosmological scalar, observed data, or an exact native bound state.
