# Rectangular field-harmonic derivation review

Bounded independent algebra and numerical-quadrature check. No empirical targets, reported fit coefficients or source parameter tables were read; illustrative positive arm amplitudes below are arbitrary. No author source edits or audit/physical-validation claim.

## Algebra

With u=x/L and b=B/Bphi, integrate exp[im(phi_center+2pi b u)] on−.5..+.5. The factor is exp(im phi_center)*sin(pi m b)/(pi m b); the odd sine contribution vanishes. Taking the real part proves the signed sinc formula and continuous value1 atzero. The m dependence is essential: it is not sinc(b) for every harmonic, nor abs(sinc(mb)). Uniform spatial harmonic density, linear imposed phase, short-junction assumptions and negligible screening are doing the physical work. Spatial variation of harmonic density would replace this sinc by the corresponding Fourier transform; the present formula is not general for an inhomogeneous junction.

The two-arm amplitude Am=d cm[Ja sinc(mba)+Jb sinc(mbb)exp(im psi)] correctly gives V=−Re sum Am exp(imphi). Under basis<n|phi>=exp(−inphi), the lower mth matrix diagonal is−Am/2 and upper is−Am*/2 (equivalently transpose/conjugate conventions may reverse these). Both must be present. This yields a Hermitian charge matrix even away from sweet spots.

Let theta=argA1 and phi_new=phi+theta. Then Am_new=Am exp(−imtheta); A1_new=|A1|. The unitary is diagonal in charge, so n and capacitive charge couplings are unchanged. Higher coefficients generally remain complex. Rotating only the first coefficient would change the potential instead of changing coordinates.

Atpsi=pi, exp(impsi)=(−1)^m: odd arm contributions subtract and even contributions add, algebraically including each signed envelope. Atzero field, Am/A1 equals cm foroddm and cm(Ja+Jb)/(Ja−Jb) forevenm, provided Ja!=Jb and the commonfactor is nonzero. Atpsi0 all contributions add. This explains relative even-harmonic enhancement near first-harmonic cancellation in the bottom convention.

## Necessary domain qualifications before reuse

The quoted ratios and phase rotation are undefined when A1=0 (equal arms atzero-field bottom, or other field cancellations). The finite potential remains well defined there; use its unnormalized complex coefficients rather than divide by A1 or take its phase. If d=0, every coefficient vanishes and no ratio extraction is meaningful. These are mathematical domain qualifications to attach if the formulas are turned into code or theorem assertions; no finite-point defect is present in the current note.

“Even add / odd subtract” is a signed amplitude identity, not guaranteed magnitude enhancement at every field. AtB=.41T withBphi,a=.8T, thearm-a second harmonic already has sinc(1.025)<0 while the other arm's second harmonic ispositive. They can therefore partially cancel despite the algebraicplus sign. Likewise “bottom/top” namespsi=pi/0 in the usual first-harmonic regime; a global frequency-minimum/maximum interpretation need not survive arbitrary signed higher harmonics or first-harmonic sign changes. The current formula should not be stretched into either claim.

## Common gap factor and center calibration

If d(B) multiplies every harmonic in both arms and the armratio/geometry/shape are already fixed, it can be absorbed into one overall Josephson energy scale at thatfield. Calibrating that scale to a directly measuredfundamental center then does not separately determine d,Ja0,Jb0. It calibrates the center; a distinct dispersion/transition observable can subsequently be predicted under the same assumptions. This cancellation fails as a one-parameter reduction for unequal arm gap factors, harmonic-dependent suppression or simultaneous d-dependent changes ofEC/cavity/transparency. Nor does it prove existence/uniqueness of the inverse center→scale solution. The note explicitly retains the armratio/geometry and other physical assumptions.

The distinction from a leadingseries-inductance harmonic proportional to the square of a first-harmonic envelope is correct within that separate mechanism's assumptions. An independently integrated local intrinsic harmonic scales with sinc(mb); generated nonlinear corrections need not.

## Independent numerical evidence

`independent_field_harmonic_check.py` uses256-point Gauss–Legendre integration overeacharm's spatial phase and1024 phase samples, with arbitraryJa=7,Jb=4 andcm=[1,−.02,.003,−.0005]. Bphi,a=.8T andBphi,b=.8*256/178T. It checksB=0,.2,.41T atpsi0,pi,.73, retaining allfour harmonics. These values are not source fitted parameters.

Spatially integrated complex coefficients agree with signed-sinc formulas within1.8e−14. Independently phase-projected13-charge matrices agree with explicit hopping matrices within1.2e−14; Hermiticity is exact to construction precision. Full harmonic phase rotation agrees within1.1e−15 and leaves charge invariant within9.2e−16. The genericpsi case preserves nonzero higher imaginary coefficients, explicitly checking why onlymakingA1real is insufficient. No empirical reads, fit, modelselection or device-geometry inference enters these tests.

The note's independence ledger appropriately distinguishes the externally motivatedBphi,a scale from a Bphi,b estimate involving target-informed arm fitting. The geometrical ratio used in this toy check is supplied, not validated as the device's penetrated width/orientation. A small algebraic residual does not resolve those imported premises or identify the microscopic correction.

## SHA256

- `FIELD_HARMONIC_DERIVATION.md`: `5f949d321a8a2a691c471e5214421f75039a33f8e0a7c5a70f0a73e998cddc52`
- `independent_field_harmonic_check.py`: `3ad8ad006c772b6781631015b5ead14b29d21a157c55b0b225267ade9ee5899d`
- `independent_field_harmonic_results.json`: `97c71518c191a642e6cb76caed32e5b439aabe4341bac0cb9c528c4d420d80a4`
- `independent_field_harmonic_check.log`: `97c71518c191a642e6cb76caed32e5b439aabe4341bac0cb9c528c4d420d80a4`
