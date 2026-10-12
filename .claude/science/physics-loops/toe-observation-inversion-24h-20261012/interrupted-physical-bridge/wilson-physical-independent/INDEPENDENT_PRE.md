# Independent structural physical-propagation prepass

2026-10-12. Read only the supplied physical-bridge `TARGET.md` for this new step. No author bridge derivation, observational residual, or newly supplied local-coefficient result has been read. Earlier independently checked additive mass work is known background; its numerical coefficient is not used below. All matching coefficients in this note remain symbolic. The target SHA256 is `2dac61a376711881f1549d7f5f85554b72bd7bba912afef249fabcef1c1194d4`.

This is a structural independent check for the specified canonical continuous-time spatial Wilson theory, not an empirical exclusion, complete observation model, formal audit, or independent recalculation of any previously accepted local coefficient. A conditional local projection can be derived. A quantitatively controlled physical wave-packet relation does not follow from local coefficients alone.

## 1. Local projection with mass, charge, and clock calibration

Set the spatial cutoff to one and write `g=e_R^2`. Let the local quadratic Euclidean action near the zero-mass critical surface have fermion kernel

\[
\Gamma_E^{\rm loc}(p)=i(1+g z_t)\gamma_0p_0
 +i(a+g z_s)\sum_i\gamma_i p_i
 +(m_b+g C)+\tfrac12|\mathbf p|^2+\cdots .
\tag{1}
\]

Here `C` denotes the additive inverse-propagator mass coefficient, not an oppositely signed self-energy. The ellipsis includes nonlocal continuum terms, momentum-dependent scalar corrections, and higher spatial derivatives. Cubic symmetry makes the dimension-four spatial coefficient common to the three axes; it does not remove higher-order directional dependence. Write the local transverse photon kernel as

\[
(1+g b_E)p_0^2+(1+g b_B)|\mathbf p|^2+\cdots,
\quad c_\gamma^2=\frac{1+g b_B}{1+g b_E}.
\tag{2}
\]

Equation (2) defines a candidate local photon clock; its relation to the physical photon branch also requires the remainder analysis below. Wave-function normalization alone changes neither ratio. Define

\[
\chi=(z_s-z_t)-\tfrac12(b_B-b_E).
\tag{3}
\]

For the Minkowski continuation, set `p0=-i(E+i0)` and use the retarded boundary value. In a local truncation this gives

\[
E^2=\frac{(a+g z_s)^2}{(1+g z_t)^2}|\mathbf p|^2
 +\left(\frac{m_b+g C+|\mathbf p|^2/2}{1+g z_t}\right)^2.
\tag{4}
\]

Let `M>0` denote the calibrated dimensionless rest energy after photon-clock normalization. At this local level mass matching is

\[
m_b+g C=(1+g z_t)c_\gamma M.
\tag{5}
\]

This is a transparent way to track the counterterm; finite-mass continuum matching modifies the detailed relation in (5), not the conclusion at leading `M->0`. Crucially, the scalar Wilson cross term in (4) contains the calibrated small scalar after (5), not the negative critical bare mass by itself.

Let `c_*^2` be the coefficient of `p^2` in the clock-normalized local `E^2`, retaining the tree dimension-five mass/Wilson cross term. Then

\[
\begin{array}{ll}
a=1:& c_*^2=1+M+2g\chi+O(gM,M^2,g^2),\\
a^2=1-m_b:&c_*^2=1+g(C+2\chi)+O(gM,M^2,g^2).
\end{array}
\tag{6}
\]

Thus the massless limiting cone differences are `g chi` and `g(chi+C/2)`. The fixed `a=1` branch has no direct `-g C/2` speed term from the critical mass: inserting `m_b=-g C+M` into an uncorrected free dispersion and then forgetting the mass correction double-counts the matching. The bare curve retains `+g C/2` through its explicit kinetic coefficient `a`. Its continuation has `a>1` near negative critical mass; positive-bare-mass tree theorems cannot simply be continued as proofs.

With an ordinary weak-coupling charge calibration, `e_b^2=e_R^2+O(e_R^4)` at fixed logarithms, so substituting Thomson charge does not change (6) at this order. Large logarithms require a running/matching treatment. Matching the observed mass is still one calibration; computing `C` does not automatically add a second empirical input or a new free parameter.

The quantity `c_*` is a local dispersion coefficient, not the velocity of a massive particle at `p=0`. For `M<<r=|p|<<1`, after expanding both mass and lattice effects, the candidate radial group velocity has the structure

\[
v_e-1=g\chi+I_{\rm curve}\frac{gC}{2}
 +(1-I_{\rm curve})\frac M2-\frac{M^2}{2r^2}
 +\frac32\left(\frac14-\frac{A_4}{3}\right)r^2
 +R_v,
\tag{7}
\]

where `A4=sum n_i^4`, `n=p/r`, and `I_curve` is zero or one for the two bare settings. Photon clock units are used. The coefficient of `r^2` is the common zero-mass tree value; finite-mass and radiative modifications belong in `R_v`. A finite-momentum photon has its own tree velocity correction `-A4_gamma k^2/8`, so an actual comparison needs the photon momentum and direction too. A time-of-flight experiment cannot identify its result directly with (3).

## 2. Gauge dependence and the nonlocal continuum

The literal link action is exactly gauge covariant. A Gaussian longitudinal gauge change can therefore be handled without guessing a numerator: for a pure gauge field `A=grad theta`, the position-space fermion Green function acquires endpoint phases. Expanding their Gaussian average and inverting gives at order `e^2`

\[
\delta_\xi\Gamma(p)=e^2\delta\xi\int_k\frac{
D_0(p)-D_0(p)S_0(p-k)D_0(p)}{(K^2)^2},
\tag{8}
\]

using `G^(xi)=delta/K^2+(xi-1)KK/(K^2)^2` and `K=(k0,2 sin(k_i/2))`. The form includes the seagull. A gauge-consistent infrared regulator is understood until on-shell projection. For left/right tree on-shell spinors, the variation vanishes. It changes the propagator residue and off-shell functions, not the first-order on-shell energy shift. The same conclusion follows from the lattice Ward identities. At the massless local linear order its wave-function contribution is common to temporal and spatial kinetic terms, so their difference is gauge independent. The one-loop photon polarization has no internal photon gauge parameter. These observations support (3), but do not establish a charged pole after removing the infrared regulator.

The soft continuum contribution in a Lorentz-symmetric leading reference theory has the form

\[
\Sigma_{\rm soft}(P)=A(P^2,M,\lambda)\slashed P
 +B(P^2,M,\lambda)M,
\tag{9}
\]

plus terms from irrelevant or anisotropic insertions. The scalar and wave-function functions contain thresholds, logarithms, and infrared singularities. At fixed positive `M`, their Lorentz-invariant on-shell part changes the calibrated mass and residue rather than generating a relative limiting cone. This explains why a finite anisotropic local difference can be physically relevant. It does **not** justify expanding (9) at a Euclidean origin and substituting a real on-shell energy term by term without a continuation and subtraction proof.

The required decomposition is a controlled hard local part plus soft continuum remainder, with any overlap subtraction specified. In particular the same infrared regulator, mass convention, and subtraction must be used for the temporal/spatial differences. Merely listing finite differences of derivatives does not bound the value or first derivative of the remainder on a timelike or nearly lightlike branch.

## 3. Charged states and the spectral-edge control

At nonzero infrared regulator a conventional perturbative electron pole is usable as an intermediate device. In the massless-photon infinite-volume theory an isolated exact charged-particle pole with nonzero residue cannot be assumed. Soft-photon states accumulate at the charged energy edge. A physical packet requires an infrared dressing or an inclusive preparation/detection prescription, finite resolution, and finite propagation time; the soft regulator must then be removed in that prescription. On-shell gauge cancellation is necessary but does not supply those choices.

There is a useful decisive kinematic control. In the isotropic local approximation take

\[
E_e(q)=\sqrt{M^2+c_e^2q^2},\qquad E_\gamma(k)=c_\gamma|k|.
\]

The electron-plus-photon continuum edge obeys the convolution bound

\[
E_{\rm edge}(p)\le\inf_q\{E_e(q)+c_\gamma|p-q|\}.
\tag{10}
\]

This is an equality for the noninteracting local electron/photon comparison used here, not a theorem identifying the exact interacting lattice spectrum. Norm inequalities reduce its minimization to collinear `0<=q<=p`. If `c_e>c_gamma`, put

\[
p_* =\frac{M c_\gamma}{c_e\sqrt{c_e^2-c_\gamma^2}}.
\]

The comparison edge equals `E_e(p)` for `p<=p_*`, and equals `E_e(p_*)+c_gamma(p-p_*)` for `p>=p_*`. Its upper branch has slope `c_gamma`, not `c_e`. Thus a fast high-energy electron branch must be treated as radiating; identifying a charged spectral edge with its putative superluminal packet would give the wrong object. For `c_e<=c_gamma`, this particular channel does not open. A photon can instead enter a pair continuum when `c_gamma>c_e`, at `k_*=2M/sqrt(c_gamma^2-c_e^2)` in this same local approximation.

The hierarchy `M<<p<<1` alone neither excludes these channels nor selects a valid order of the weak-coupling, mass, and high-energy limits. A simple sufficient stable perturbative sector keeps the momentum away from such thresholds and, for an expansion around the Lorentz reference shell, `g p^2/M^2` small. This is a sufficient sector, not a necessary condition for all reorganized calculations. Resumming the small cone difference permits larger `p/M`, but then the thresholds and possible widths must be retained.

## 4. Independently derived local Cherenkov kernel

To avoid assuming stability if the curve coefficient is positive, a conditional leading radiation law can be derived before knowing that coefficient. Set the photon clock `c_gamma=1`, take `c=c_e>1`, `d=c^2-1`, and use the canonical local action `bar psi(i gamma0 D0+i c gamma_i D_i-M)psi`. Its spatial real-photon vertex is `e_R c gamma_i`. Higher-derivative lattice and loop corrections have not been bounded here; the following is a local-EFT leading golden-rule calculation.

For an initial momentum of magnitude `p`, let `E=sqrt(M^2+c^2p^2)`. Real emission has

\[
\cos\theta=\frac{E+d k/2}{c^2p},\qquad
0<k<K=\frac{2(c^2p-E)}d,
\tag{11}
\]

and requires `p>M/(c sqrt(d))`. With spin averaging and the two transverse photon polarizations, direct Dirac traces give

\[
\overline{|\mathcal M|^2}
=4e_R^2c^4p^2\sin^2\theta+2e_R^2c^2d k^2.
\tag{12}
\]

The canonical phase-space normalization then gives, with `alpha_R=e_R^2/(4 pi)`,

\[
\frac{d\Gamma}{dk}
=\frac{\overline{|\mathcal M|^2}}{16\pi E c^2p}
=\frac{\alpha_R}{E c^2p}
\left[c^2 d p^2-M^2-E d k+\frac{d(c^2+1)}4k^2\right].
\tag{13}
\]

This formula uses the positive-energy spinors with temporal normalization `u^dagger u=2E`; no Lorentz-invariant spatial dispersion is silently inserted into the measure. It includes hard photon fractions, not only the soft boundary. Its integral is infrared finite for real Cherenkov photons. A specified resolved-photon threshold `k_min` can be imposed directly.

Writing `B0=c^2 d p^2-M^2`, `B1=-Ed`, `B2=d(c^2+1)/4` and `F=alpha_R/(Ec^2p)`,

\[
\Gamma=F(B_0K+B_1K^2/2+B_2K^3/3),\qquad
\mathcal P=F(B_0K^2/2+B_1K^3/3+B_2K^4/4).
\tag{14}
\]

`P` is the instantaneous expected radiated energy per unit time at that momentum. For small `d`, keeping `y=M^2/(d p^2)<1` fixed away from a shifting endpoint,

\[
\Gamma=\frac{\alpha_R d p}{6}(1-y)^2(4-y)+O(\alpha_R d^2p),
\]
\[
\mathcal P=\frac{\alpha_R d p^2}{24}(1-y)^3(7-3y)
 +O(\alpha_R d^2p^2).
\tag{15}
\]

The leading no-resolved-emission probability over time `T` is `exp[-Gamma_resolved(p) T]` while momentum remains fixed, within the usual weak-coupling kinetic approximation. Subsequent hard emissions require a transport/jump calculation; replacing it by a deterministic energy trajectory is an additional approximation. If `d=O(e_R^2)`, these rates are `O(e_R^4)` despite the cone difference being `O(e_R^2)`. A formally higher-order width can matter over a long experimental flight.

These formulas do not establish an infrared-safe wave-packet theorem for the full Wilson action. To reuse them quantitatively one must control the matching remainder in both dispersion and vertex, stay in its domain, specify resolution/preparation, and compare propagation time to the resulting rate. They provide a concrete conditional alternative to a falsely stable high-energy pole.

## 5. Remainder information and exact obstruction

The tree part does have explicit uniform control. For `r<=1`, `M>=0`, `A4=sum n_i^4`, the free Wilson reference law with kinetic coefficient `a` obeys

\[
E_0(rn)^2=M^2+(a^2+M)r^2
 +\left(\frac14-\frac{a^2 A_4}{3}-\frac{M A_4}{12}\right)r^4
 +R_6,
\]
\[
|R_6|\le\left(\frac{2a^2}{45}+\frac M{360}+\frac1{24}\right)r^6,
\quad
|\partial_r R_6|\le\left(\frac{4a^2}{15}+\frac M{60}+\frac14\right)r^5.
\tag{16}
\]

These bounds follow from elementary sine/cosine Taylor remainders and `0<=W<=r^2/2`, `|W'|<=r`. They are bounds on the specified tree reference, not bounds on the interacting remainder after calibration.

For a one-real-photon low-energy channel, the full-torus photon inequality `omega(k)>=2|k|/pi` on `[-pi,pi]^3` ensures `|k|<=pi E_initial/2`. Thus low-energy emission forces photon and outgoing momentum into a small neighborhood of the physical corner. This gives a useful domain control for a perturbative real-emission calculation. It does not by itself prove the exact interacting spectrum or bound virtual hard-loop remainders.

The full physical bridge still needs all of the following concrete information: (i) a hard/soft decomposition of the renormalized retarded two-point functions for positive calibrated mass, with uniform bounds on the remainder and its first momentum/energy derivatives on the chosen branch; (ii) cancellation/factorization of infrared terms before removing the regulator, with an explicit packet or inclusive observable; (iii) a demonstrated domain in `M`, `p`, cutoff, logarithms, and distance from thresholds; (iv) if unstable, the relevant dispersion and vertex error bounds and propagation kernel. At finite regulator an implicit-root estimate needs control of both `R` and `partial_E R`; a divergent residue factor cannot simply be treated as a bounded error when the regulator is removed.

Even before the loop remainder, isolating a dimension-four splitting of size `|g chi|` requires comparing it with the explicit `r^2` lattice and `M^2/r^2` mass effects, and with the `M` term for fixed `a=1`. A renormalizable Cherenkov kernel with constant `d` needs `r^2<<d` or an explicit inclusion of the quartic dispersion in its shell. The condition `r<<1` alone is insufficient when `d` is itself small. Near a threshold, error bounds must be compared to the opening margin, not only to the total energy.

Local derivative coefficients do not determine this information. Higher-derivative terms with zero constant and linear jets can have arbitrarily different finite-momentum effects unless their coefficients are bounded, and nonlocal continuation additionally controls branch cuts. The action fixes those terms in principle; this is a precise missing calculation, not an extra free parameter or a claim of impossibility.

A safe order for a proof is: fix the action, positive calibrated mass, coupling and specified external momenta; use a gauge-consistent infrared regulator and perform retarded on-shell projection; factor or inclusively cancel the soft terms with fixed resolution/time; remove the regulator; only then take any small-mass, high-energy or cutoff asymptotic with explicit uniform estimates. Other orders can be valid if separately justified. Taking the massless Euclidean derivative first and calling the result a physical speed supplies none of these uniformity guarantees.

## 6. Planned independent controls

The accompanying script will use explicit four-by-four Dirac matrices to check the local mass/clock projection, directly trace transverse emission amplitudes and numerically integrate their phase space, compare the continuum-edge minimization with (10), and stress the directional tree remainder bounds. These controls address the independent structural statements above. They cannot manufacture the missing full-action retarded/infrared remainder bound. Arbitrary control coefficients will be used; no author matching values or observational residuals enter.

## 7. Completed controls and exposure record

The first and only runner attempt completed successfully: `TOTAL: PASS=10 FAIL=0`. The immutable `independent_projection_run1.log` retains all outputs. Its controls include direct local-Hamiltonian eigenvalues (maximum projected coefficient-slope error `3.97e-9`), common field-rescaling invariance, 100 on-shell gauge-factor contractions, 124 continuum-edge minimizations, 200 explicit transverse spinor traces, 40 numerical rate/power phase-space integrations, small-splitting rate limits, 5,000 tree remainder checks, and 10,000 full-torus photon-momentum checks. Matrix rate/power integrals and closed formulas agree to relative `2.8e-14`; the energy-conservation check is below `9.3e-14`. These are controls of the stated equations, not evidence for an uncomputed physical remainder.

During this prepass the parent reported that its author on-shell gauge comparison and local-EFT radiation calculation had been completed and frozen, with author identity in `author-freeze-v1.json`. No author formula, coefficient value, or file from that packet was read before this freeze. Two checker messages sent earlier explained the critical-mass projection and charged spectral edge; the parent records that these preceded its final exposition. The final author/checker prose is consequently not wholly mutually blind, although this derivation and its rate formula were developed before author-formula exposure. The numerical control values `C=0.70`, `zt=0.13`, `zs=-0.09`, `bE=0.11`, `bB=-0.07` are arbitrary algebraic test inputs, not matching results or observational fits.
