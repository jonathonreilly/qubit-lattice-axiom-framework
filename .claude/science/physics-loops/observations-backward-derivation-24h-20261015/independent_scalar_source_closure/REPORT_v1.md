# Focused independent check of scalar-source closure

The checked normalization, leading radiation fractions, mass conversion,
inverse-coordinate cancellation and weak PPN relations agree with the stated
action and approximation contract. One scope error was found in the original
negative-mass instability statement. The author's preserved version 2 corrects
it without changing the equations. This is a focused mathematical/source check,
not a formal audit, an empirical test or a compact-body realizability result.

The current source is `SCALAR_SOURCE_CLOSURE_v2.md`, SHA256
`c27e409e2c953b0a115569138e0b6357f246f8c14809b3c822789bd5869569bd`.
The reproduced primary runner remains
`check_scalar_source_closure_v1.py`, SHA256
`df0f437428fdda2d1b001899f53a2236f5e2056b1a1d33bbb803b9b6e6ddc37e`.
It deliberately binds v1, SHA256
`ae27e3d7d819a69c2b15549444415cf9385d87af2e356ecc73a7a374ce9d6754`.
All seven source identities and lossless contents are in
`SOURCE_SNAPSHOT_v1.json`; the exact v1-to-v2 delta is contained losslessly in
`SOURCE_DELTA_v1_to_v2.json`. The frozen plan/manifest match their actual inputs.
The v1 receipt must not be relabeled as a v2 execution.

## Independent reasoning and controls

`DERIVATION_BEFORE_CODE.md` and its preceding timestamp/source binding were
saved before the author's runner text was opened. The new independent code
imports no author runner. Earlier campaign checks were background, not authority
for these results.

- Varying the weak point-body mass after conformal conversion gives
  `beta=-1/sqrt(2Fstar D)` and `alpha=-1/sqrt(D)`. Canonical exchange is
  `-GT alpha1 alpha2 m1 m2 exp(-m_s r)/r`. Its force has the additional
  `1+m_s r` factor, so a finite-range potential coefficient is not the orbital
  coefficient of the constant-Gc model.
- Gaussian radial/angular separation, rather than the primary sphere
  quadrature, gives the dipole and general symmetric quadrupole contractions.
  Circular moments at arbitrary phase yield `5/96` and `1/6`. The independent
  trace control gives an additional `(tr Q''')^2/(144pi)` beyond the STF flux:
  dropping it requires the constant-trace circular-source assumption.
- Direct metric-trace/scalar-equation elimination reproduces equation (5).
  With `U=Fstar^2 V/F^2`, the on-shell conversion is
  `U_phiphi=(Fstar/F0)m_J^2`. The off-shell difference is
  `-Fstar(V_F-2V/F)[4/(F D)+D_F/D^2]`; equilibrium cannot be omitted.
  The inverse conditions `W_x=W` and `m_J^2=2(W_xx-W)/D` contain no C.
  A different analytic family, `W=w0 exp(u)+a(cosh(u)-1)`, checks this at
  arbitrary C with mass squared `2a/D`.
- The harmonic canonical energy current is `nu k |A|^2/2`; combining it with
  the Green-function multipole amplitude `k^ell` gives exponent
  `(2ell+1)/2`. Evanescent mean flux and the threshold limit vanish.
  Dipole and quadrupole thresholds occur at different orbital harmonics.
- First-order conformal metric multiplication reproduces the two Jordan
  potentials and the weak, same-environment PPN inversion. An exact rational
  counterexample holds `alpha1 alpha2=1/9` fixed while changing the leading
  scalar loss: for masses 1 and 2 and speed 1/10, charges `(1/3,1/3)` give
  `eta=1/54`, whereas `(2/3,1/6)` give `43/32`. This proves non-identification
  by the product; it does not realize both pairs as compact bodies in one action.

Dimensions are consistent in natural units: F and W have mass dimension 2,
V dimension 4, canonical phi dimension 1, beta dimension -1, and alpha,
canonical point charge q, D and loss fractions dimension 0. No absolute scalar
normalization or observational length calibration has thereby been measured.

## Original scope error and correction

V1 inferred a constant-background instability from negative local mass squared
without restricting the background. An explicit same-action-class vacuum has
`W(u)=-3 exp(u)/L^2-D u^2/(2L^2)`, `u=log(F/F0)`, and constant positive D.
It satisfies the vacuum condition, has `R=-12/L^2`, and `m_s^2=-2/L^2`.
For global AdS4, substituting `phi=exp(-i nu t)Y_lm psi(chi)/tan(chi)` into
the Klein-Gordon equation gives

    -psi'' + [l(l+1)/sin(chi)^2 + (m_s^2 L^2+2)/cos(chi)^2]psi = nu^2 psi.

At that negative mass, the potential is `l(l+1)/sin(chi)^2`. Regular-center
and reflecting fast-falloff endpoint conditions make its quadratic form
nonnegative; `l=0`, `psi=sin(2chi)` is an explicit frequency-2 mode. This
refutes a mass-sign-only curved-background scalar instability inference.
It proves neither nonlinear stability nor source realizability. V2 explicitly
requires geometry, spectrum and boundary conditions and limits the threshold
exclusion to flat positive-mass radiation, resolving the finding.

## Actual execution and limits

The independent run passed 72 controls, including 2 source-binding checks, in
0.693 s. The original primary run passed 174 controls in 0.610 s; its complete
stdout is byte-identical to the supplied 36,576-byte receipt, SHA256
`a6a0d53d65d054293b8bee455e6ef76b8b8cbbb651fb5f2ba77a63f8b335a342`.
A separate observed execution also produced identical bytes in 0.596 s and
recorded only repository reads of the runner, plan and v1 note. It recorded no
repository write. The observer is process-level Python open-event evidence,
not an operating-system sandbox claim.

All runs used Python 3.12.8, `-B`, `PYTHONDONTWRITEBYTECODE=1` and a hard 120 s
subprocess timeout. Full stdout, stderr, command arguments, elapsed/CPU cost,
peak memory and before/after input hashes are preserved in the three
`*_attempt01.*` groups. No executed checker failed or timed out. Source inputs
were unchanged during all three runs. `FAILURE_AND_CHANGE_RECORD_v1.json`
distinguishes the scientific wording finding from execution and display events.

The dependent siren substitution was checked algebraically only; the broader
propagation/readout block belongs to another check. The remaining physical
obligation is to establish the intended source's weak, unscreened, common and
nearly constant environment, or derive its body-dependent mass/charge response.
One must also register independently reconstructed action derivatives to that
environment and supply valid propagation/readout inputs. Constant charges,
circular adiabatic motion, negligible relevant curvature, `k r<<1`, the separate
conservative condition `m_s r<<1`, and no extra loss channels remain hypotheses.
The 174 synthetic controls and the independent identities supply no observation,
common-action compact-body construction, history selection or global stability
claim. No further correction is required within this focused v2 scope.
