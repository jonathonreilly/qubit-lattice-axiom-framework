# Independent referee report: C5 probe R9-4

## VERDICT

**CONFIRMED WITH CORRECTIONS.** The worker's narrow results are mostly sound: (H-T) follows for the stated stationary, self-commuting-output, zero-reverse-gain linear-meter dilation; S1, the logarithmic far field, channelwise positivity, the Cassini coefficient interval, OWD Eq. (27) additivity, the Wiseman--Milburn algebra, Lemma E's core spectral argument, and the correction (n\geq3) all check. The necessary corrections are substantive but scope-preserving: (H-T) is not established for every CP Gaussian CQ history; a spin-2-noise repair enters R8-3 only if additivity is also imposed; the toy does not prove that every sub-floor construction needs an entangling mediator; Lemma E is an almost-everywhere statement unless continuity is added; and the proposed (1/|s|) null-cone optimizer is not an ordinary locally finite positive spectral measure, so the quoted preferred-frame interval is only a conditional search target. Consequently the two `EXCLUDED` results are valid only for the explicitly narrowed class \(\mathcal T\) (and for the literal scalar-only-payment version of (ii)), not as exclusions of the full fixed variants in `TESTS.md:3710-3716`.

## Scope and reproducibility

The supplied script reruns exactly. Its script hash is `52b1cad36e276b4053d0448e2d594d37f4017af663618ffe60383b2e45a08347`, and both the supplied and rerun output hashes are `6851c3ff0f58e1eea41dcf210b7ee2541b740ec83d1bcd2ec7bbcf72ccfb5afa`. Independent calculations are in `r94_referee_checks.py:1-117` with output in `r94_referee_checks.out:1-42`.

I checked the no-go against, at minimum, these distinct escape routes: history-level CP without a stationary meter, reverse gain/non-nondemolition output, emission-side correlations, spin-channel separation, light-cone distributions/counterterms, loss of one-sided limits, non-Gaussian or jump instruments, and preferred-frame regulation. Several remain outside \(\mathcal T\), which is why no broad fixed-variant exclusion follows.

## Findings

### 1. Meter derivation of (H-T) and Clerk Eq. (90)

**Correct for the stated detector model; not valid for general CP Gaussian CQ histories.** The report's hypotheses are at `R9-4_report.md:39-51`, with the appropriate self-limitation at `R9-4_report.md:232-237`. [Clerk et al. Eq. (90)](https://arxiv.org/html/0810.4729) is indeed a frequency-by-frequency stationary-detector inequality, but it is

\[
\bar S_{JJ}\bar S_{BB}-|\bar S_{JB}|^2
\geq |\hbar\widetilde\chi_{JB}/2|^2[1+\Delta],
\]

not (H-T) verbatim. The simpler block inequality follows after the worker's extra detector assumptions. At fixed (p=(\omega,\mathbf k)), write (P=S_{JJ}(p)=S_{JJ}(-p)), (S_\pm=S_{BB}(\pm p)), (a=S_{JB}(p)), and (b=S_{JB}(-p)^*). Positivity of the two unsymmetrized spectral matrices gives (|a|^2\leq PS_+) and (|b|^2\leq PS_-). Self-commutation of (J) gives the equality of its two spectra; zero reverse gain and the Kubo identity give (hbar\chi_{JB}=-i(a-b)). Hence

\[
|\hbar\chi_{JB}|^2\leq P(\sqrt{S_+}+\sqrt{S_-})^2
\leq 4P\bar S_{BB}.
\]

With (F=\hbar\chi_{JB}) and (D'_0=\bar S_{BB}), this is exactly (P_JD'_0\geq |F|^2/4), equivalently the positivity of the reported (2\times2) block. The independent random spectral check has positive margin in `r94_referee_checks.out:1-4`.

What does **not** follow is that every CP Gaussian CQ history admits this stationary linear, Hermitian, nondemolition, zero-reverse-gain realization with the same (F,P_J,D'_0). Stinespring dilation alone does not supply those identifications. [Layton et al.](https://arxiv.org/html/2307.02557) expressly distinguish full non-Markovian CPTP histories from the instantaneous Markovian trade-off. Their statement does not refute the conditional stationary-frequency derivation; it does refute treating it as a consequence of CP alone. Thus (H-T) remains a defining wall of \(\mathcal T\), not a general-history theorem.

### 2. Lemmas S1 and L

**S1 is exact under (H-T).** If both diagonal spectra vanish at a timelike (p), positivity of the (2\times2) block forces (F(p)=0), exactly as stated at `R9-4_report.md:104-108`. Together with Newton's (F(0^-)=1) and the assumed one-sided limits (`R9-4_report.md:39-45,110-112`), this forces a (1\to0) jump across the cone.

**The (\ln r) far field is confirmed independently.** The worker's numerical result at `scripts/r94_checks.out:1-11` reproduces exactly. A different profile admits a closed form:

\[
\operatorname{FP}\!\int_0^\infty {e^{-u}\sin[(\omega+u)r]\over u}\,du
=\sin(\omega r)\left[-\gamma_E-\tfrac12\ln(1+r^2)\right]
+\cos(\omega r)\arctan r .
\]

It therefore contains (-\sin(\omega r)\ln r+O(1)); the independent values converge to the bounded remainder (-\gamma_E) in `r94_referee_checks.out:6-16`. This verifies `R9-4_report.md:114-121` without sharing the worker's quadrature path. The literal time-varying point source should be read as a scalar radial Green-function probe; any smooth conserved radiating source with nonzero on-shell amplitude inherits the same singular radial factor.

**The counterterm claim is correct at its stated finite-order scope.** Two finite-part extensions differ by a distribution supported on the cone. A finite-order Lorentz/radial cone-supported distribution is a finite sum of normal derivatives of (delta(s)); its monochromatic far field is a polynomial in (r) multiplying (sin\omega r/r) or (cos\omega r/r). No finite polynomial cancels ((\ln r)\sin\omega r/r) for all large (r). This confirms `R9-4_report.md:120,235`, but not exclusions of infinite-order/non-tempered prescriptions, altered propagators, or histories without the one-sided-limit ansatz.

### 3. Lemma S2 and Cassini

**S2 is correct on the conserved physical sectors.** Away from the cone, the spin-2 and physical scalar Barnes--Rivers projectors are orthogonal irreducible sectors; a Lorentz-invariant kernel cannot use a scalar diagonal block to make a nonzero spin-2 off-diagonal block positive. The limiting statement at the cone follows from the assumed one-sided limits. Thus the literal model in which the GR-normalized spin-2 drift has no spin-2 decoherence/backaction noise is inconsistent under (H-T), as claimed at `R9-4_report.md:129-134`.

The sentence that *any* repair “puts the model exactly in R8-3” is too strong (`R9-4_report.md:134`). Adding spin-2 noise enters the refereed R8-3 no-go only when the direct and feedback contributions are additive. A correlated spin-2 repair belongs to variant (iii) and remains open.

**The Cassini interval is correct.** With the report's normalization,

\[
\gamma={1-2c_0/3\over1+2c_0/3}.
\]

The measured (gamma-1=(2.1\pm2.3)\times10^{-5}) is the published [Cassini result](https://doi.org/10.1038/nature01997). A two-standard-deviation interval gives (c_0\in[-5.0248,1.8750]\times10^{-5}), matching `R9-4_report.md:136-146` and `r94_referee_checks.out:18-20`. The wording “scalar pull about (5\times10^{-5})” should distinguish (c_0) from the fractional Newtonian scalar contribution (2c_0/3), whose largest magnitude here is (3.35\times10^{-5}). A trace-only drift gives no photon deflection and hence (gamma=-1), so that part is also correct.

### 4. Variant (iii): OWD, Wiseman--Milburn, and Lemma E

**OWD Eq. (27) is additive after linearized Gaussian integration.** [OWD Eq. (27)](https://arxiv.org/html/2302.07283) contains separate `ΔW D₀ ΔW` and `W̄ D₂⁻¹ W̄` quadratic forms and no mixed noise form. Linearizing `W̄ = Ah − b` and integrating `h` gives a response term plus reduced-matter noise `D₀ + G D₂ G†`, with no noise cross term. The one-mode check at `scripts/r94_checks.out:22-26` is therefore representative. This confirms `R9-4_report.md:154-160` only for the displayed Eq. (27) class, with (H-T) and a GR-normalized physical spin-2 channel added; it does not exclude OWD's framework or arbitrary non-Markovian influence kernels.

**The Wiseman--Milburn identity and toy numerics are correct.** The two generator forms agree (`scripts/r94_checks.out:28-34`), and for (c=\sqrt\kappa(1+i\mu)A), (F=\lambda A), one obtains dephasing (kappa+(\sqrt\kappa\mu-\lambda)^2) and coupling (g=2\sqrt\kappa\lambda). Setting (lambda=\sqrt\kappa\mu) gives (g/(2\mu)), below the additive AM--GM floor. The joint-meter and local-LOCC negativities in `scripts/r94_checks.out:35-40` also rerun exactly.

The inference at `R9-4_report.md:168-171` is not a theorem: these two constructions show that this joint meter entangles and this local-meter realization does not. They do not prove that every possible sub-floor correlated Gaussian history requires an entangling mediator. The report's later qualification that the qubit calculation is illustrative (`R9-4_report.md:240`) is the correct scope.

**Lemma E's spectral core is correct with measure-theoretic qualifications.** Under stationarity, Lorentz invariance, a positive 2×2 unsymmetrized spectral measure for `(B,J)`, classical `J`, zero reverse gain, finite `S̄_BB`, and nonzero matter spectral weight `W`, any nonzero emission measure on a timelike mass shell has an infinite boost-orbit integral. Finite vacuum excitation therefore requires `S_ff(−p) = 0` almost everywhere on each relevant orbit. Positivity then gives `S(−p)[1,G]ᵀ = 0`; (H-T) and finite `S̄_BB` give `S_JJ > 0`, so the 2×2 matrix is rank one rather than rank zero. Emission silence also sets the emission-side `fJ` cross spectrum to zero, and Cauchy--Schwarz on the absorption side yields `S_ff(p) S_JJ(p) ≥ |F(p)|²`, up to the report's ħ convention. This confirms the chain at `R9-4_report.md:173-184` as an almost-everywhere statement; “at every p” additionally needs continuity. Calling the remaining bath “quantum-mediated gravity” is a reasonable interpretation of the dilation, not a classification theorem for all CQ histories.

### 5. Variant (iv): (n\geq3) and the interval

**The ultraviolet correction is confirmed.** With (|F_u|^2\sim\omega^{-2n}), a spatial Gaussian, (K\sim |F_u|^2/|s|), Maxwell weight (W\sim s^2), energy factor (omega), and (d^3k) saturated at (k\sim1/\ell), the large-(omega) integrand is (omega^{3-2n}). The integral converges iff (n>2), hence (n\geq3) for integer (n). Independent integration reproduces the worker's logarithmic (n=2) growth and the (n=3) limit (0.67412) (`r94_referee_checks.out:21-27`; worker statement at `R9-4_report.md:197-208`).

**The interval arithmetic reproduces, but it is not an allowed window.** Given the assumed `ρ_GW = εLħc/(π³ℓ⁴)`, `L = 10`, the recalled cosmological density, R8-3's uncertain `A′`, and the assumed `1/ε` broadband increase in photon production, the simultaneous roots are `1.48, 2.25, 3.42×10⁻⁷ m`, exactly as reported (`R9-4_report.md:209-217`; `r94_referee_checks.out:29-34`). The upper `5×10⁻⁶ m` is only R6-4's conservative Newtonian subwindow.

There is an additional null-cone defect. The claimed exact optimizer (D'_0=c/(2|s|)) at `R9-4_report.md:202-204` is not locally integrable across a regular point of (s=0): (int_{\delta<|s|<1}ds/|s|=2\ln(1/\delta)) (`r94_referee_checks.out:36-42`). A positive distribution is a locally finite measure, so (1/|s|) is not an ordinary stationary positive spectral kernel on generic test functions. A finite-time, restricted-domain, or regulated prescription is still required, and a Hadamard finite part would not be positive. The same logarithm sits in the metric spectrum (|G_R|^2P_J\sim1/|s|). Therefore “needs no \(\mu\)” is not established, and the near-cone energy estimate depends on an unstated physical cutoff represented by (L). Together with the unbuilt CP dilation and dynamical frame (`R9-4_report.md:218-228`), this leaves only a conditional search interval, not a demonstrated viable family.

### 6. Readings and scope

The fixed rule requires `EXCLUDED` for every parameter in the stated variant (`TESTS.md:3730-3733`). Class \(\mathcal T\) adds (H-T), a stationary linear-meter structure, one-sided limits, and other walls not implied by the fixed setting (`R9-4_report.md:39-45,232-237`). Accordingly:

- **(i):** `EXCLUDED` is confirmed only in \(\mathcal T\), with a finite-order cone-supported counterterm class and a nonzero on-shell radiating source. The full fixed spacelike-noise variant is **OPEN** because general CP Gaussian histories have not been shown to obey (H-T).
- **(ii):** the literal scalar-only-payment model is inconsistent under (H-T). An **additive** spin-2-noise repair is excluded by the refereed R8-3 theorem; a correlated/non-additive spin-2 repair is **OPEN**. Thus a broad fixed-variant `EXCLUDED` is not justified outside \(\mathcal T\).
- **(iii):** **OPEN** is confirmed. OWD Eq. (27) lies in the additive conditional no-go, but emission-cancelled/correlated histories are not excluded or constructed.
- **(iv):** **OPEN** is confirmed. (n\geq3) is a correct UV condition; roughly (2\times10^{-7}) to (5\times10^{-6}\,\mathrm m) is only a conditional search interval, while the less constrained (10^{-8}) to (5\times10^{-6}\,\mathrm m) range is also a search target rather than an allowed window.

No variant is demonstrated `VIABLE`, but the campaign-wide fixed readings for (i) and broad (ii) should remain `OPEN`; the valid `EXCLUDED` statements are conditional subclass results.

## Strongest correct statement

For a translation- and Lorentz-invariant linearized Gaussian CQ model that admits a stationary linear-meter dilation with a self-commuting classical output, zero reverse gain, finite symmetrized backaction, the pointwise Fourier block inequality (H-T), the standard massless retarded propagator, and one-sided light-cone limits, spacelike-only direct and record noise force the response to vanish at timelike momentum; Newtonian normalization then creates a light-cone jump whose generic radiative field contains ((\ln r)/r), and no finite-order Lorentz/radial cone-supported counterterm cancels it. In the same class, scalar noise cannot pay for a GR-normalized spin-2 response; the literal scalar-only-payment model fails positivity, while an additive spin-2 repair inherits R8-3's golden-rule no-go. OWD Eq. (27) is additive after linearized Gaussian integration, but correlated emission-cancelled histories remain open; Lemma E shows only that a finite Lorentz-invariant vacuum rate forces almost-everywhere emission-side cancellation and a compensating absorption channel under its spectral assumptions. In a preferred frame the ultraviolet integral requires (n>2) (integer (n\geq3)), but the quoted (\sim2\times10^{-7}) to (5\times10^{-6}\,\mathrm m) range is a conditional search target because its null-cone (1/|s|) kernel needs a regulator or restricted domain and its cosmological/CP/frame inputs are unbuilt. Thus the full fixed variants (i)--(iv) remain **OPEN**, with only the stated \(\mathcal T\) subclasses of (i) and literal/additive forms of (ii) **EXCLUDED**.
