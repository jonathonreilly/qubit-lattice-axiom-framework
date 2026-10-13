# Handwritten radiation construction: focused check

The reconstructed equations, positive on-trajectory bare Hessian, global-in-u
potential lower bound and stated fractional endpoint coefficients check out.
One error was found in the original dust-limit speed: chi'/sqrt(a) must tend
to sqrt[3/(2(1+a))]. The parent has corrected exactly that phrase in v2. The
original input and failing check remain preserved. No additional mathematical
correction is requested within this handwritten derivation's scope.

This is an independent focused mathematical check, not primary authorship,
a full numerical implementation review, a formal audit or an empirical
acceptance result. It uses the supplied Einstein action, constant a>0,
positive ideal dust/radiation and the stated constructed potentials. No Git,
PR, settings, other-chat, worker or source mutation was performed.

## Frozen source and correction

`HAND_DERIVATION_v1.md` and `PROTOCOL_v1.json` were copied exactly before the
recorded symbolic execution. Their SHA256 values are:

- v1 derivation: `b8dd9cc0e26787ba32475c93b57034a9482aba0db7559e193703ab41f47d2570`
- protocol: `bfd06bb72d44088b742c551fe2537559110c317efa26bbca53d68a52513b95a1`

The complete v2 note and correction record were subsequently read and
snapshotted. V2's SHA256 is
`4d62ed249c42ed532b41b87ebee1a482236e404463da891c77dfffbf9485f95b`;
the correction record is
`ac1fc454b38531eaa137631249151c99d30e80dfe6df424f739131f237a86a68`.
An exact string replacement reconstructs v2 from v1. No candidate equation,
potential, exponential slope or protocol changed. `SOURCE_DISPOSITIONS.json`
contains complete original/final paths, hashes, recovery locations and scope.

## Findings and evidence

1. **Original dust-speed error, resolved in v2.** Dividing dot chi^2=aS by
   Hbar^2=2(1+a)S/3 gives the corrected squared speed 3/[2(1+a)]. The original
   value was too large by a factor sqrt(2). Its radiation speed and both
   exponential steepness magnitudes were already correct.
2. **Unchanged-potential residual confirmed.** Direct elimination from
   Friedmann followed by conservation gives the quoted residual
   2aRS[(2+a)S-L]/[3((2+a)S+2L)^2]. It prevents this exact unchanged u=0 branch
   over an interval with positive conserved radiation; the isolated zero is
   not an interval solution. This is not exclusion of the full family,
   approximate branches or observed cosmology.
3. **Reconstruction and full coordinate dynamics confirmed.** The new
   Friedmann, Raychaudhuri, conservation and two scalar equations agree.
   Transforming the canonical equation independently produces the stated
   Gamma term and V_x/(gH^2) source. The off-trajectory field metric is the
   fixed function built with Hbar(S), not the evolving Hubble value. The
   exact-trajectory Friedmann denominator is positive.
4. **Potential bounds confirmed with their declared domain.** An explicitly
   positive polynomial expression for U_chichi establishes strict positive
   Hessian at u=0 for S>0. Completing the square proves V>=U/2 for every real
   u. Positive Hessian on the trajectory is not global convexity in field
   space or stability of a coupled gravitational solution.
5. **Full endpoint regularity confirmed and extended to the coefficient M.**
   Exact series inversion verifies both q^(8/3) terms in the note. The
   independently obtained M term is -992b q^(8/3)/135. The full potential's
   fractional coefficient is strictly negative for every finite real u;
   consequently the one-sided potential is C2 and non-C3, not just its u=0
   restriction. The supplied branch does not fix a continuation beyond chi_c.

`INDEPENDENT_DERIVATION.md` contains the complete algebra, field-coordinate
derivation, limiting qualifications and numerical recipe. The two executed
reviewer scripts import no parent implementation or helper.

The first symbolic run contains **30 checks: 29 pass and the original
handwritten dust-speed assertion fails**. Its corrected value is separately
verified in the same immutable result. The execution's exit 1 and complete
failure record remain in `ALGEBRA_RESULTS_v1.json` and
`ALGEBRA_EXECUTION_v1.json`; no failure or executed file was rewritten.

The second execution contains **499 passing checks**, including 54 independent
90-digit coordinate quadratures, high-precision potential curvature/determinant
checks, limiting-coefficient convergence, the full coordinate chain rule,
full-potential regularity identities and exact affected-source confirmation.
Its worst final relative coefficient error is 1.5612e-9 against the frozen
2e-7 comparison tolerance. All commands, actual timeouts, source hashes,
stdout/stderr and outputs are preserved. No reviewer execution was retried.

## Necessary scope distinctions

The new radiation-aware potential is a new construction containing b and L;
it is not a successful prediction of the unchanged dust potential. The
background and thermodynamic content are supplied. The displayed temperature,
photon statistics, massless dispersion, adiabatic conservation, illustrative
H0, matter benchmark and radiation normalization are not derived here.

The parent explicitly assigns photons-only empirical calibration, with no
implicit neutrino factor. The historical temperature and posted spectrum are
exposed development inputs or baseline-aware diagnostics. This mathematical
review checks those role boundaries; it does not verify the primary papers'
measurement numbers, the posted spectral residuals or a covariance likelihood.
The parent is separately responsible for that source comparison.

A formal dust-dominance limit does not guarantee an intermediate dust era
for every arbitrary positive b,L. At fixed b>0 the asymptotic past is
radiation dominated. The protocol's zero-radiation and zero-L values are
limiting controls; the positive-L future expansion is not applicable at L=0.

For dimensional clarity, log-density coordinates mean ln(S/S_ref) and the
corresponding fixed-reference expressions for the physical densities. This
unit convention shifts coordinate origins and does not modify the derivation.
The chart is restricted to S>0 and positive density logs, and g tends to zero
at the future endpoint. No attraction, global stability, primordial state,
entropy/baryon/neutrino origin, screening or quantum completion is established.

## Final disposition

The complete corrected handwritten v2 derivation is mathematically consistent
within the stated supplied model and open positive-density domain, subject to
the explicit limiting and regularity boundaries above. The dust-speed finding
is resolved by the exact separately preserved correction. The future parent
implementation and empirical calibration are not covered by this result.
`RECEIPT.json` binds every review artifact and final source identity while
retaining the original adverse evidence.
