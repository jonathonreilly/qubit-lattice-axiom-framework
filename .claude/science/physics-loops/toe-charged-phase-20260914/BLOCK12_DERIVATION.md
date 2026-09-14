# Collective photon-phase attack — open working derivation

Personal investigation after PR8119. Target remains an actual fixed-payload
Hamiltonian Coulomb phase, not a finite-box spectrum or static-curvature proxy.
No phase theorem, no axiom wall and no new retained status is established.

## 1. Full collective Fröhlich-Spencer mechanism being read

IHES/P/81/40, Massless phases and symmetry restoration in abelian gauge theories
and spin systems. Main paper text pp1-54 read in this block, in addition to
prior selected pp58-83. Equations with OCR omissions require rendered-page
inspection before importing constants. Pages33-38 were rendered and inspected.
The proof uses (i) duality to a noncompact Gaussian constrained by integer
currents, (ii) a positive convex ensemble reorganization into separated currents,
(iii) conditional Gaussian integration on a noninteracting subset of links,
(iv) small renormalized activities, and (v) a source-aware real translation and
Jensen estimate. Its masslessness result is a two-sided covariance comparison
for transverse one-forms, not merely a Wilson perimeter law. The Z_N argument
requires large N at a fixed Euclidean coupling and first proves Wilson and
disorder perimeter bounds. Its exact observable and limiting requirements must
be mapped separately before claiming a Hamiltonian photon pole.

A normalization discrepancy is visible in the PREPRINT's Gaussian lemma:
page36 writes exp[-sum_p (dα)_p²/(2β)], but page35/36 Eqs2.63/2.67 print
exp[-βρ²/n] after integrating one link incident on n plaquettes. Completing
the square gives exp[-βρ²/(2n)] times the shifted characteristic function.
A one-dimensional Gaussian integral will check this directly. Do not import
its numerical108 constant without rederiving it. This only changes a sufficient
constant; it is not a disproof of the established large-coupling theorem.
The published version has not yet been obtained for this comparison.

## 2. Exact block Gaussian integration

For a positive definite finite precision Q, split field coordinates into S
and R. A source exp[i(ρ_S·a_S+ρ_R·a_R)] can be integrated conditionally:

    E_S[e^(iρ_S a_S)|a_R]
      =exp[-rho_S^T Q_SS^-1 rho_S/2]
       exp[-i rho_S^T Q_SS^-1 Q_SR a_R].

Thus the remaining source is rho_R-Q_RS Q_SS^-1 rho_S. The scalar factor is
exact and positive. Gauge zero modes can be regulated first; only declared
invertible conditional blocks are used. The local one-link bound is one
special case. A block integration is useful only if its residual source and
interactions with the other currents remain controlled; dropping them is not
a renormalization proof.

Consider an infinite temporal tube of one spatial link in an anisotropic
Gaussian U(1) action, with all other links held fixed. Write its conditional
quadratic precision

    Q_tube = u I+v(2I-S-S†), u=4 beta_s, v=beta_tau.

The four spatial plaquettes give u and the two temporal plaquettes give the
one-dimensional Laplacian. Its covariance is exactly

    G_r=q^|r|/sqrt[u(u+4v)],
    q=(u+2v-sqrt[u(u+4v)])/(2v), 0<q<1.

For an isolated source m at one time, the damping is exp[-m²G0/2]. This can
be much stronger than integrating one time coordinate while holding its two
temporal neighbors fixed. But a neutral neighboring-time dipole (+m,-m)
has damping

    exp[-m²(G0-G1)],
    G0-G1=(1-u G0)/(2v).

On the actual fixed-N Wilson Hamiltonian trajectory beta_s=delta K and
beta_tau=alpha_N^-1 log[1/(delta t)] (N>2), u/v->0. Therefore
G0 diverges like1/(4sqrt(beta_s beta_tau)), while
G0-G1~1/(2 beta_tau)->0. A tube suppresses isolated net charge but does NOT
uniformly suppress the shortest neutral temporal dipoles. Gauge-invariant
closed currents can contain precisely such paired temporal profiles on
spatial links, completed by temporal-link pieces. Their residual charges and
other-link covariance must be retained; this observation alone is not a
bound on the full current's action or a no-go for collective methods.

The distinction identifies a genuine resummation task: short temporal dipoles
can accumulate while the physical clock generator stays finite. Declaring
every raw dipole dilute from an equal-time tube variance would be wrong.

## 3. Exact isolated-link resummation and the large-N coarse time scale

The exact clock electric Hamiltonian is h_E=t(2-X-X†) on Z_N. At physical time
T its positive kernel from0 to r is the periodized Skellam law

    p_T(r)=exp(-2tT) sum_(m in Z) I_(r+mN)(2tT).

This follows either from independent forward/backward Poisson jumps of rate t
or by Fourier diagonalization. It resums arbitrarily many short temporal
increments without a small-raw-dipole premise. At T=cN/t, the random walk
width in integer clock steps is of order sqrt(N), much less than N. In angle
units θ=2πr/N its variance is 8π²c/N. Its central Gaussian has inverse width
beta_eff=N/(8π²c); an isotropic-scale magnetic action T K is also order N
when K/t is fixed. This motivates coarse physical time of order N/t as a
possible route to a weak effective coupling at finite but large N.

That motivation is not yet a phase theorem. With magnetic plaquette terms,
exact time blocking yields joint multi-link/multi-time interactions, not just
the isolated-link heat kernel times a single plaquette weight. Replacing the
full block by that product needs a volume-uniform, source-preserving theorem.
Ordinary fixed-box Trotter convergence and finite-energy truncation do not
supply it. Nor does a small formal commutator alone justify an exact local
Baker-Campbell-Hausdorff logarithm for a block of duration proportional to N.
The next calculations quantify the single-link approximation and the actual
mixed electric/magnetic block rather than silently discard that interaction.

## 4. Full closed temporal plaquette in the Gaussian reference

The cheap paired temporal profile is not merely a gauge-noninvariant isolated
source artifact. On an infinite anisotropic Gaussian lattice use temporal
gauge at nonzero temporal momentum. Let s0²=4sin²(k0/2), s²=sum_i4sin²(ki/2)
and wi=4sin²(ki/2)/s². The covariance of A_i is

    C_ii(k0,k)=(1-wi)/(beta_tau s0²+beta_s s²)
                       +wi/(beta_tau s0²).

A unit 0i plaquette current is the boundary of that plaquette; its temporal
gauge coupling is m[A_i(t)-A_i(t+1)]. Its Gaussian action obeys

    S_0i=(m²/2) integral_BZ s0² C_ii(k0,k)
             <=m²/(2 beta_tau).

The current is closed; gauge zero modes cancel in the source. Thus for fixed
m=N on the fixed-N Wilson time trajectory, this FULL elementary current's
Gaussian characteristic damping tends to1. Integrating additional field
coordinates cannot produce a uniform suppression of these raw currents in
that same Gaussian reference. Spatial plaquette currents behave differently:
performing the temporal integral gives a factor
[beta_s s²(beta_s s²+4beta_tau)]^-1/2, so their action scales as
1/sqrt(beta_s beta_tau), rather than1/beta_tau, on that trajectory.

This eliminates one naive collective-dilution inference, not the physical
Coulomb phase. The cheap loops must be resummed or a different reference used.
The original Wilson reference itself has rapidly diffusing continuous angles
in this singular limit, so its naive Gaussian covariance is not automatically
the fixed clock Hamiltonian's physical covariance. On the matched Villain
trajectory the spatial heat kernel likewise must be kept periodized; its
bare quadratic coefficient is not its small-time cosine coefficient. The
previous transfer note already proves that distinction. No bare-coupling
product alone pays the current resummation or Hamiltonian source match.

## 5. Controlled central Gaussian approximation after exact single-link blocking

Set tT=cN, c>0 fixed. On representatives |q|<=N/2, the exact Fourier
multiplier is lambda_q=exp[-2cN(1-cos(2πq/N))]. Define the normalized sampled
periodic Gaussian g_r proportional to sum_m exp[-(r+mN)²/(4cN)]. Its Fourier
multiplier is the fully aliased Gaussian

    lambdaG_q=sum_m exp[-a(q+mN)²]/sum_m exp[-a(mN)²], a=4π²c/N.

With b=16c/N, M=floor(N/2), define

    Bcentral=(4cπ⁴/(3N³))[3sqrt(π)/(4b^(5/2))+8exp(-2)/b²],
    Balias=2exp(-aM²)/(1-exp[-a(2M+1)])
           +[2exp(-aN²)/(1-exp(-3aN²))][1+sqrt(π/a)],
    B=Bcentral+Balias.

Then max_r |p_r-g_r|<=B/N. Proof: for |x|<=π,
0<=x²-2(1-cos x)<=x⁴/12 and2(1-cos x)>=4x²/π². Hence

    0<=lambda_q-exp(-a q²)
        <=(4cπ⁴ q⁴/(3N³))exp(-bq²).

The sum of q⁴exp(-bq²) over all integer q is bounded by its integral plus
its two unimodal maxima, giving Bcentral. The omitted Gaussian residues and
the normalization denominator give Balias by geometric tails. Fourier
inversion yields the pointwise bound. No fixed alias truncation is used in
the proof.

For an integer0<R<N/2 and
I(R)=R asinh[R/(2cN)]-2cN(sqrt[1+(R/(2cN))²]-1),

    TV(p,g)<=min{B/2,(2R+1)B/(2N)+exp[-I(R)]+(1/2)exp[-R²/(4cN)]}.

The last two terms bound the Skellam and discrete-Gaussian tails. Skellam
uses its exact moment generating function exp[2cN(cosh u-1)] and its
optimized Chernoff transform. The Gaussian denominator is at least
sqrt(4πcN) by Poisson summation; its decreasing tail is bounded by a Gaussian
integral. Taking R=ceil(sqrt(12cN log N)) for sufficiently large N yields
TV=O_c(sqrt(log N)/N), since B=O_c(N^-1/2). This is a local transfer-kernel
statement at a specified growing block time, not a thermodynamic phase.

The actual bounded checks at c=1/4,N16..512 compare the Fourier kernel,
periodized modified Bessel kernel and sampled Gaussian. At N512 the total
variation is about2.28e-4, while the deliberately conservative proved bound
is about1.23e-2. Agreement of these finite checks supports the derivation;
it does not replace the analytic tail estimates.

## 6. Magnetic coupling survives at this block scale

Let a,b>0 and the actual one-plaquette reduced clock Hamiltonian be

    H_N=a(2-X-X†)+b[1-cos(theta)], theta=2πr/N.

Here a can be4t for a square's four electric links. Set T=cN. A tempting
replacement of exp(-T H_N) is the symmetric product

    S_N=exp(-T V_N/2)exp(-T E_N)exp(-T V_N/2).

This replacement does NOT become exact merely because N grows. Rescale
x=sqrt(N)theta with mesh epsilon=2π/sqrt(N). The operator N H_N tends to

    h=4π²a p_x²+(b/2)x²=p_x²/(2m)+(m omega²/2)x²,
    m=1/(8π²a), omega=2πsqrt(2ab).

For completeness the low-eigenvalue limit can be obtained by min-max:
compactly supported smooth trial functions sampled on the mesh give the
limsup. The discrete-gradient energy of a normalized bounded-energy sequence
controls its piecewise-linear interpolants on every fixed interval, while
N b(1-cos(x/sqrt(N)))>=2b x²/π² gives tightness. Local compactness followed
by the growing-interval limit gives the liminf and no escaped low modes.
The ground state is simple. Convergence of total energy plus the separate
kinetic/potential liminf bounds gives convergence of potential energy and
uniform integrability of x²; hence its variance also converges. This is a
one-coordinate harmonic limit, not a many-link phase theorem.

The central limit kernel in section5 and the Gaussian confinement factors
also give Hilbert-Schmidt convergence of S_N to
S=exp(-c V/2)exp(-c E)exp(-c V/2). Indeed the rescaled free kernel is uniformly
bounded, and each potential factor is bounded by exp(-cb x²/π²); these
supply an integrable Gaussian majorant on the expanding (x,y) plane.
The resulting Gaussian integral operator is exactly diagonalizable. Put
Omega=c omega and gamma=2asinh(Omega/2). Its eigenvalues are
exp[-gamma(n+1/2)], and its ground precision is
m omega sqrt(1+Omega²/4). Therefore

    gap[-T^-1 log S_N]/gap[H_N] ->gamma/Omega,
    <theta²>_(ground S_N)/<theta²>_(ground H_N)
       ->1/sqrt(1+Omega²/4).

Both ratios stay different from1 at fixed c>0. At a=b=1,c=.3, their limits
are about.82404 and.60013. Direct N32,64,128,256 matrices approach these
values. Thus an isolated-link central Gaussian approximation cannot alone
justify discarding the coupled block dynamics.

There is a constructive Gaussian repair: each noncompact transverse Maxwell
mode has the exact same metaplectic correction with Omega(k)=T omega(k).
The coarse frequency is2T^-1 asinh[T omega(k)/2], and the electric/magnetic
coefficients receive respectively factors

    gamma/[Omega sqrt(1+Omega²/4)],
    gamma sqrt(1+Omega²/4)/Omega.

These are analytic functions of omega(k)² near the physical Brillouin zone
for fixed finite T times the microscopic velocity, so their Fourier kernels
decay exponentially in spatial separation. Their small-k limits are1 and
the linear dispersion survives. But this is a NONCOMPACT Gaussian identity.
Extending its source-preserving quasilocal control through finite-clock
wrapping and all charged/monopole defects remains the actual open theorem.
