# Conditional EOS numerical companion and historical diagnostic boundary

**Type:** bounded_theorem
**Primary runner:** `scripts/frontier_dark_energy_eos.py`
**Status:** supplied-model bookkeeping; no inherited physical closure.

The corollary `DARK_ENERGY_EOS_RETAINED_COROLLARY_THEOREM_NOTE.md`
assumes constant positive density and FRW conservation on an interval with
H != 0 (continuity may extend the result to isolated zeros). Its conditional
CPL result is `(w_0, w_a) = (-1, 0)`. The comparison sphere has `R = ell`;
the physical evolving slice has `a(t)=ell cosh(t/ell)` and gap
`Lambda sech^2(t/ell)`. The parent does not derive the physical matching.

## Preserved algebraic diagnostics

For a supplied lattice correction,
`lambda_1^latt = (3/R^2)[1-(1/4)(l_P/R)^2+...]`, fixed R and l_P give a
constant shift and zero EOS drift. A small amplitude does not bound drift
without a logarithmic derivative bound. The scalar comparison-sphere ratio
`lambda_2/lambda_1=8/3` follows from l(l+2)/R^2; it is not topological protection.

The old model comparison is conditional: R fixed gives w=-1; R proportional
to a^alpha gives w=-1+2alpha/3 under the supplied density law. This does not
exclude every alpha>0 or select a physical model. Hubble tracking plus the
particular flat Friedmann saturation assumptions forces zero remaining matter,
not a general no-go for evolving radii.

## Explicit historical runner disposition

`scripts/frontier_dark_energy_eos.py` retains its complete legacy numerical
functions and observational narrative for recovery. Those functions and the
old cache are quarantined as historical diagnostics, not present proof or a
current framework prediction. The default entry point now checks the live conditional algebra under a
120-second cap: conservation with rho>0 and H!=0; zero drift for fixed R and
l_P; rho proportional to a^(-2 alpha) giving w=-1+2alpha/3; the positive-density
counterexample delta=epsilon sin(N ln a), whose EOS drift at ln a=0 is
-epsilon N/3; and conditional flat Friedmann saturation
rho_vac=3H^2/(8 pi G) implying rho_other=0. At H=0 conservation alone does not
select w. The epsilon=1/100,N=300 example has amplitude 0.01 yet unit EOS drift.
These are exact supplied-model identities and controls, not physical selection.

All ten legacy functions and the old cache remain separately recoverable in
`archive/notes/review_feedback/pr9855-eos-2026-10-23/` and prior Git history.
Explicit `--historical-diagnostic` replays that unreviewed legacy route; it is
not authorized by the default 120-second capture and was not executed here.
The current cache covers only the new conditional checks.
No current DESI forecast, unconditional falsifiability claim, physical radius
selection, continuum spectral convergence, or retained status follows here.

Historical references remain context only:
- [smooth solution class](UNIVERSAL_QG_SMOOTH_GRAVITATIONAL_GLOBAL_SOLUTION_CLASS_NOTE.md)
- [GR diagnostic](UNIVERSAL_GR_DISCRETE_GLOBAL_CLOSURE_NOTE.md)
