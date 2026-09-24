# Independent PRE: harmonic lattice dispersion and conditional timing constraints

The supplied harmonic target has a polarization-independent, direction-dependent **quadratic subluminal correction** to group propagation. It can be parameterized along a fixed direction by the quadratic timing parameter used in the two specified papers. Turning that algebraic correspondence into a bound on a physical lattice spacing requires additional hypotheses absent from the repository theorem. The repository result alone supplies neither a source-to-detector theorem nor an empirical prediction for the magnitude of a timing lag.

This calculation was completed before opening any author argument or control in `photon-observation-personal`. The permitted weak-field note was read completely. Only the needed model/scaling, initial-state, moment and limit premises of its pinned electric/ring parents were reused. Their underlying proofs and numerical runs are not independently recertified here. No parent runner, observational likelihood or source-event data was run. The work uses the inherited model and reasoning effort, without delegation.

## 1. Exact inherited statement and definitions

The main source is `WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md`, at main `0e6ad8285096ed668816f18caaa6fbbfbd9c50e8`, SHA256 `651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf`.

Its target is the supplied compact rotor Hamiltonian

\[
H_{\rm rot}=K\sum_e E_e^2-J\sum_p(W_p+W_p^\dagger),
\quad \operatorname{div}E=0,
\quad K=\frac{cg^2}{2a},\quad J=\frac{c}{2ag^2}.
\]

At fixed finite cubic torus, after removing gauge and electric-winding zero directions, specified cutoff/rescaled finite Hermite packets near a flat connection have a fixed-time vector-norm harmonic approximation of order `g^2` plus an exponentially small cutoff error. Its constants depend on the packet, chart, box, spacing and time interval. The previous microscopic-to-rotor step also requires the locally dressed A-record/B-vacant preparation, growing link spin, the specified growing penalty/hopping scales and a formation rate tending to zero. A per-link fourth electric moment bound is a parent hypothesis. The circuit lemma remains provisional at this pinned revision.

The stipulated limits are spin to infinity first, then `g` to zero at fixed finite box and spacing, then `a` to zero at fixed physical periodic box and a fixed finite set of mode excitations. None of the needed constants is made uniform across all these limits or over astronomical propagation times. The continuous-time harmonic frequency is

\[
\omega(\boldsymbol\kappa)=\frac ca\Omega(a\boldsymbol\kappa),\qquad
\Omega(\mathbf k)=\sqrt{2\sum_{j=1}^3(1-\cos k_j)}.
\tag{P1}
\]

Here `k` is dimensionless lattice momentum and `κ=k/a` is a physical-coordinate wavevector. Nonzero torus momenta are understood; differentiating the explicit symbol is not differentiating a finite list of unrelated eigenvalues. Put

\[
x=a|\boldsymbol\kappa|,\qquad
\mathbf n=\boldsymbol\kappa/|\boldsymbol\kappa|,\qquad
A_4(\mathbf n)=\sum_j n_j^4\in[1/3,1].
\tag{P2}
\]

The bounds below are uniform in direction for `0<x<=1`. The origin is excluded because the positive acoustic frequency is not differentiable there; the source separately removes its zero modes.

## 2. Group propagation and polarization

Direct differentiation gives the exact harmonic group velocity

\[
v_j(\mathbf k)=c\frac{\sin k_j}{\Omega(\mathbf k)}.
\tag{P3}
\]

The curl-square symbol has eigenvalues `0, Ω^2, Ω^2`. The two physical polarizations therefore have identical frequencies and identical group velocities. There is no harmonic birefringence at any nonzero lattice momentum. This says nothing about polarization-dependent corrections in an unproved interacting/finite-parameter regime.

The vector in (P3) is generally not parallel to the wavevector. Moreover,

\[
\frac{|\mathbf v|^2}{c^2}
=\frac{\sum_j4\sin^2(k_j/2)\cos^2(k_j/2)}
       {\sum_j4\sin^2(k_j/2)}\le1.
\tag{P4}
\]

The inequality is strict away from a zero of the denominator. This is a bound on this harmonic group velocity, not a proof about signal fronts, microscopic commutators, or relativistic causality.

There is a precise packet sense of group translation. Take a finite positive-frequency Fourier superposition, with either or both transverse polarization amplitudes, supported in a wavevector ball of radius `b` about `κ0`. Suppose its convex hull avoids zero and let `M` bound the Hessian norm of `ω` there. Taylor's theorem and `|exp(iu)-exp(iv)|<=|u-v|` bound its L2 difference from its initial envelope translated by `t v(κ0)`, with the carrier phase removed, by

\[
\frac{|t|M b^2}{2}\,\|\psi_0\|_2.
\tag{P5}
\]

This is just orthogonality of the Fourier modes after bounding each phase remainder; polarization amplitudes can stay inside the envelope. It applies to the harmonic Fourier field or its one-excitation mode amplitudes. It does not assume that a finite Hermite preparation is an astrophysical photon source. A localized, approximately translating packet requires an appropriate bandwidth, and a packet on the finite torus can wrap around it. The norm error of the microscopic/compact model must be added separately and has not been controlled on a source-to-detector path.

## 3. Uniform low-wavevector remainders

The following constants are deliberately nonoptimal. Set `d=Ω(x n)^2/x^2`. Scalar Taylor bounds imply

\[
d=1-\frac{A_4x^2}{12}+r,
\quad 0\le r\le\frac{x^4}{360},
\quad 11/12\le d\le1.
\tag{P6}
\]

The nonnegative remainder follows from the sixth-order cosine remainder for `|x n_j|<=1`. Taylor expansion of the square root and inverse square root on `[11/12,1]` gives

\[
\left|\frac{\Omega}{x}-1+\frac{A_4x^2}{24}\right|
\le\frac{x^4}{400},\qquad
\left|d^{-1/2}-1-\frac{A_4x^2}{24}\right|
\le\frac{x^4}{200}.
\tag{P7}
\]

For example the two Taylor constants are bounded respectively by
`1/720+(12/11)^(3/2)/1152 < 1/400` and
`1/720+(12/11)^(5/2)/384 < 1/200`.
Also

\[
\frac{\sin(x n_j)}x=n_j-\frac{x^2 n_j^3}{6}+\rho_j,
\qquad |\boldsymbol\rho|\le x^4/120.
\]

Multiplying by the second formula in (P7) proves

\[
\left|\frac{\mathbf v}{c}-\mathbf n
-x^2\left(\frac{A_4\mathbf n}{24}
             -\frac{\mathbf n^{\circ3}}6\right)\right|
\le\frac{x^4}{40}.
\tag{P8}
\]

Indeed a sufficient coefficient is
`1/200+1/144+1/1200+sqrt(12/11)/120 < 1/40`.
Projecting along and perpendicular to `n` yields

\[
\frac{v_\parallel}{c}=1-\frac{A_4x^2}{8}+e_\parallel,
\quad |e_\parallel|\le x^4/40,
\]
\[
\frac{\mathbf v_\perp}{c}
=-\frac{x^2}{6}(\mathbf n^{\circ3}-A_4\mathbf n)
+\mathbf e_\perp,\quad |\mathbf e_\perp|\le x^4/40.
\tag{P9}
\]

In particular the group correction is three times the phase-velocity correction along the wavevector. Using the phase speed for a timing analysis would give the wrong coefficient.

Since `v_parallel/c>=17/20` and
`|n^(circ3)-A4 n|^2=sum n_j^6-A4^2<=1`, the tangential speed is at most `23 x^2/120`. The identity
`|v|-v_parallel=|v_perp|^2/(|v|+v_parallel)` then gives

\[
\left|\frac{|\mathbf v|}{c}-1+\frac{A_4x^2}{8}\right|
\le x^4/20.
\tag{P10}
\]

For plane-crossing time `t_parallel=D/v_parallel` and a ray distance `D` traversed with constant vector (P3), `t_ray=D/|v|`, inversion gives

\[
\left|\frac{ct_\parallel}{D}-1-\frac{A_4x^2}{8}\right|\le x^4/16,
\qquad
\left|\frac{ct_{\rm ray}}D-1-\frac{A_4x^2}{8}\right|\le x^4/10.
\tag{P11}
\]

For the first bound use `|1-v_parallel/c|<=3 x^2/20`, and for the second use `|1-|v|/c|<=7 x^2/40`, with the corresponding positive denominator bounds. These are harmonic kinematic times conditional on packet travel; they are not emission/detection observables constructed by the original model.

## 4. Energy parameterization and direction of an actual ray

Restore units by additionally identifying a photon excitation energy with `E=ℏω` and its momentum with `ℏκ`. Let `E_a=ℏc/a` and `e=E/E_a=Ω`. By (P6), `e^2<=x^2<=12 e^2/11` and `0<=x^2-e^2<=x^4/12`. Consequently

\[
\left|\frac{ct_\parallel}D-1-\frac{A_4e^2}{8}\right|\le e^4/10,
\qquad
\left|\frac{ct_{\rm ray}}D-1-\frac{A_4e^2}{8}\right|\le e^4/6.
\tag{P12}
\]

The direction in (P2) is the wavevector direction. For the ray direction `m=v/|v|`, one has
`|m-n|<=23 x^2/102`. The polynomial `A4` is Lipschitz with constant 4 on the unit ball, so replacing `A4(n)` by `A4(m)` in the second formula changes the bound by at most `46 e^4/374`. Thus a sufficient ray-direction bound is

\[
\left|\frac{ct_{\rm ray}}D-1-
 \frac{a^2 A_4(\mathbf m)E^2}{8\hbar^2c^2}\right|
\le \frac13\left(\frac{E}{E_a}\right)^4.
\tag{P13}
\]

For two allowed narrow packets traveling the same straight ray, their propagation-time difference therefore has leading term

\[
\Delta t_{\rm prop}=
\frac Dc\frac{a^2 A_4(\mathbf m)}{8\hbar^2c^2}
 (E_h^2-E_l^2)
 +O\!\left[\frac Dc\frac{E_h^4+E_l^4}{E_a^4}\right],
\tag{P14}
\]

with absolute remainder at most the displayed quartic sum divided by 3. Packet bandwidth and source/detector errors are separate. For almost equal energies this is an absolute, not a uniform relative, two-energy error bound. The positive quadratic leading term is subluminal; there is no leading linear-in-energy term.

The directions along an axis, a face diagonal and a body diagonal have `A4=1, 1/2, 1/3`. A direction-independent coefficient cannot be substituted for this entire dispersion. At leading order a single source direction can be assigned an effective parameter

\[
\boxed{\quad E_{\rm QG,2}(\mathbf m)
=\sqrt{\frac{12}{A_4(\mathbf m)}}\frac{\hbar c}{a},
\qquad s=+1.\quad}
\tag{P15}
\]

This matches the convention `v/c=1-(3/2)(E/E_QG,2)^2+...`. It also matches the quadratic term in `E^2=p^2 c^2[1-(E/E_QG,2)^2+...]`. The identification is an inference conditional on physical photon/ray assumptions, not a new interpretation silently added to the repository theorem.

## 5. Precisely what is borrowed from the timing analyses

The requested versions are [MAGIC, arXiv:1709.00346v1](https://arxiv.org/pdf/1709.00346v1) and [LHAASO, arXiv:2402.06009v2](https://arxiv.org/pdf/2402.06009v2). The latter has a later version; it was not substituted for the expressly requested v2. The following are the papers' reported limits, not new fits.

**MAGIC.** Equation 1 uses the group-velocity convention in (P15), with positive sign for subluminal propagation. Its parametrization suppresses rotational anisotropy. The Crab distance is `2.0±0.5 kpc`; its phase timing uses a period near `33.7 ms`. Table 6 gives these 95% bounds in GeV:

| Order/sign | Without systematics | Including systematics |
|---|---:|---:|
| Linear, subluminal | `7.8e17` | `5.5e17` |
| Linear, superluminal | `6.4e17` | `4.5e17` |
| Quadratic, subluminal | `8.0e10` | `5.9e10` |
| Quadratic, superluminal | `7.2e10` | `5.3e10` |

Only the quadratic subluminal row matches this harmonic correction. The analysis uses reconstructed energies above 400 GeV. Its studied systematics include response, background, spectral/pulse-shape and distance effects; arbitrary intrinsic energy-dependent pulse-position drift is expressly excluded from those systematic bounds. Thus the systematics-inclusive row is still conditional on source-emission modeling. [MAGIC, Eq. 1 and Sections 4.3–5, Tables 5–6](https://arxiv.org/pdf/1709.00346v1).

**LHAASO v2.** Equations 1–5 specify the dispersion, its group derivative, the cosmological lag kernel, and `η1=s E_Pl/E_QG,1`, `η2=10^-15 s E_Pl^2/E_QG,2^2`. They use `z=0.151`, flat Lambda-CDM with `H0=67.36 km/s/Mpc`, `Omega_m=0.315`. Equations 6–8 specify a broken-power-law light curve, evolving spectral index, and response/EBL-weighted counts; in Eq. 8 the lag shifts the light curve, while the displayed spectral factors retain their stated time argument. The ML fit uses this model, Poisson counts and bias subtraction with shuffled events. Its selected Table I columns are:

| ML/MINOS parameter | Lower endpoint | Best fit | Upper endpoint |
|---|---:|---:|---:|
| `η1` | `-0.11` | `0.003` | `0.12` |
| `η2` | `-0.31` | `0.01` | `0.32` |

The corresponding reported subluminal lower scales are `1.0e20` and `6.9e11 GeV` (superluminal: `1.1e20`, `7.0e11`). These are ML/MINOS, not the distinct calibrated columns. The text also reports an EBL sensitivity study; this does not bound arbitrary intrinsic cancellation. [LHAASO v2, Eqs. 1–8, Section III.B and Table I](https://arxiv.org/pdf/2402.06009v2).

A small printed-number discrepancy is preserved: using the paper's approximate `E_Pl=1.22e19 GeV` and the printed `η2=0.32` gives `6.8200e11 GeV`, not exactly the table's `6.9e11 GeV` (about 1.17% apart). Conversely the latter gives `η2=0.312623...`. The table may reflect additional internal precision/conventions, but that explanation is not established here. The two printed values must not be asserted to be exact numerical inverses.

Under all the bridge assumptions below, a monotone reparameterization of the selected published coefficient limit yields these arithmetic translations:

| Reported quadratic subluminal scale | Bound on `a sqrt(A4)` | Conservative bound on `a` with unknown orientation |
|---|---:|---:|
| MAGIC including systematics, `5.9e10 GeV` | about `1.16e-26 m` | about `2.01e-26 m` |
| LHAASO v2 ML/MINOS, `6.9e11 GeV` | about `9.91e-28 m` | about `1.72e-27 m` |

The last column uses `A4>=1/3`; it is not an isotropic average. The underlying statistical qualifications remain attached. Using the printed LHAASO `η2=0.32` instead gives `a sqrt(A4)<1.0023e-27 m`. The table translation above deliberately uses the printed energy-scale bound. These are conditional parameter constraints, not estimates of `a` and not empirical confirmations of the construction.

Unit conversion uses `ℏc=1.973269804593...e-16 GeV m`, calculated from the [BIPM defining SI constants](https://www.bipm.org/en/measurement-units/si-defining-constants). The cosmological numerical control uses the exact conventional parsec `(648000/pi) au`, with `au=149597870700 m`, as documented in [IAU 2015 resolutions, B2 note 4 and B3 note 4](https://iauarchive.eso.org/static/resolutions/IAU2015_English.pdf).

## 6. The cosmological hypothesis is substantive

The finite static torus does not specify an expanding spacetime or its preferred lattice frame. If one additionally postulates geometric optics in a flat FLRW background, standard local redshift `E(z)=(1+z)E_obs`, and a physical spacing `a_phys(z)` and lattice-frame direction `m(z)`, the leading lag would be

\[
\Delta t_{\rm prop}=\frac{E_h^2-E_l^2}{8\hbar^2c^2}
\int_0^{z_s}\frac{a_{\rm phys}(z)^2 A_4(\mathbf m(z))(1+z)^2}{H(z)}\,dz.
\tag{P16}
\]

The factor follows by fixing the comoving path: at first order the arrival delay is the integral of the fractional speed deficit against `dz/H(z)`. There is no additional source-redshift prefactor outside that integral for the propagation term. Formula (P16) is an added geometric-optics correspondence, not a theorem imported from the static repository result. A full error bound also needs control of the postulated propagation/redshift prescription, not merely the local dispersion remainder.

If the physical spacing and lattice-frame direction are constant along the ray, (P16) is exactly the paper's leading quadratic kernel under (P15). If instead the lattice has constant comoving spacing, `a_phys(z)=a0/(1+z)`, the factors cancel and the kernel becomes `integral dz/H(z)`. These are inequivalent extensions of the same static formula. At the paper's redshift and cosmology the independently computed kernels are

\[
I_0=6.6645841267\times10^{16}\ {\rm s},\qquad
I_2=7.7077839349\times10^{16}\ {\rm s},\qquad I_2/I_0=1.15652887.
\]

The original note does not select either extension. A changing lattice orientation, peculiar velocities or curved/lensed paths would require further specification. Thus one cannot use the cosmological energy-scale bound as a spacing bound without naming the cosmological lattice hypothesis.

## 7. Missing hypotheses and decisive limits of the bridge

1. **Physical identification and parameters.** The model must describe actual vacuum photons, with a physical meter/second/energy calibration, `E=ℏω`, and the observed low-frequency speed identified with `c`. A persistent nonzero `a`, its preferred frame and orientation must be physical quantities, rather than a freely chosen regulator. The construction does not select `a`, `c` or `g`. Its final `a->0` limit eliminates this correction.
2. **State and phase.** Astrophysical radiation must lie in a regime controlled by the prepared flat-connection, zero-electric-winding harmonic sector. A stable vacuum photon phase, relevant occupations, interactions with charged matter and emission/detection couplings are not established. Equal harmonic polarizations do not establish all finite-parameter polarization properties.
3. **Limits and accumulated errors.** Finite-spin, dressing, live-formation and nonlinear compact-field errors must remain smaller than the proposed quadratic dispersion effect across the relevant energies, bandwidths, distance and duration. The ordered finite-box/fixed-time theorem does not provide that quantitative statement or permit an uncontrolled simultaneous limit. An `O(g^2)` vector error alone is not an `O(a^2 E^2)` frequency or timing error.
4. **Propagation and detectors.** A packet/ensemble transport and detection-time observable must connect mode phases to arrival statistics. Bandwidth spreading, stochastic emission, absorption/scattering, detector response and any microscopic noise require control. Equation (P5) is the harmonic approximation to a translated envelope, not that connection.
5. **Emission-time nuisance.** An observed lag is a sum of source and propagation contributions (with cosmological time dilation for a source-frame lag). If an arbitrary energy-dependent source lag is allowed, it can cancel a propagation lag. A null timing result then gives no model-independent finite bound on `a`. The quoted published confidence limits retain their emission/light-curve assumptions; the repository has no source model removing this ambiguity.
6. **Cosmology and direction.** For the GRB one must choose the expansion law, local energy redshift, proper/comoving spacing rule and orientation transport, as well as how the preferred lattice frame relates to measured directions and boosts. Along one effectively fixed ray, anisotropy can be absorbed into (P15); the full cubic theory is not the globally isotropic ansatz. The Crab comparison avoids the cosmological expansion kernel but still needs the physical frame and source hypotheses.

These are named gaps in a particular observation bridge, not a proof that no such bridge can be constructed. No physical assumptions are adopted as new repository axioms. Neither a null result nor a small allowed spacing validates the microscopic mechanism or its premise selection.

## 8. Independent controls, provenance and verification limits

`dispersion_controls.py` was independently written from the displayed symbol and SI definitions. One run completed, exit 0, in about 0.399 seconds of wrapper time (about 0.170 seconds internal), with empty stderr. Full source, all 18 rows, output JSON and identical stdout are retained; source SHA is `8b45196ba4a106f6f8be0454312602a03abfeedda372dac00be5858f785b8d01`.

The controls use six directions and `x=1, 0.1, 0.001`. They compare the analytic velocity with high-precision differentiation, build the three-row complex curl symbol independently, check its two equal transverse eigenvalues, verify each stated remainder inequality on those points, and retain a nonparallel group-velocity example. They evaluate the deliberately wrong phase-speed replacement (delay coefficient ratio approaching `1/3`) and the isotropic `A4=1` replacement (axis/body-diagonal ratio approaching `3`). The unit conversion and cosmological integral use two different quadrature procedures; the printed-number inversion discrepancy is retained rather than normalized away. These finite checks support algebra/implementation; the uniform estimates are proved above. They are not interval proofs or analyses of telescope data.

The exact Git scientific source identities, all at the pinned main revision, are:

| Source snapshot | SHA256 |
|---|---|
| Weak-field note | `651fa7cfd816ca5df8c401959458b7590c2f6ec706af437ef3ce31accb7d3ccf` |
| Electric/magnetic parent | `eb5e31ae7e76f80383c454bf3e01ec98df2f503e93f04159b1cc11545d9996b4` |
| Uniform local ring parent | `d5c5b7119cde0679ddd023904bb26d08adf31b3f6a201d877f95d604fa7b99d4` |

The retrieved primary PDF identities are:

| Requested source | Retrieval start UTC, 2026-09-24 | SHA256 |
|---|---|---|
| MAGIC `1709.00346v1` | `18:30:15.355026` | `7b01528216cb47bad4f59ac8e8c63be66de01a917b5f03c1d40a36877b4b0ba8` |
| LHAASO `2402.06009v2` | `18:30:15.843529` | `ee06a3a04a9306b0c0c1382e1675dd7df5514777fc13c569a64db7e35bcfcad9` |

Both successful responses were HTTP 200 at the requested versioned arXiv URLs. The PDFs and complete page text extractions, retrieval headers/logs, unit sources and conversion definitions are retained and hashed by the evidence seal. The first urllib PDF request failed with HTTP 406; the subsequent curl retrieval succeeded. The old IAU URL returned 404; its official archived URL succeeded. Both failures remain recorded. Pypdf warned about rotated text; equation/table values were cross-checked against the arXiv web PDF text, and no omitted rotated figure text is used. A failed MAGIC web screenshot is recorded. No truncated tool output is relied on as complete evidence; affected requested equations, tables and premise passages were subsequently read through the retained extraction or untruncated source ranges.

Applicable instruction/skill copies have the previously read, unchanged hashes recorded in `SOURCE_PINS.json`. The newly inspected material consists only of the permitted main notes, the specified primary observation papers, and authoritative unit definitions. No author candidate, current campaign checkpoint or other active checker packet was opened. No publication, prior packet, audit/retained state or existing seal was modified. This PRE stops at sealing, pending any separate source release.
