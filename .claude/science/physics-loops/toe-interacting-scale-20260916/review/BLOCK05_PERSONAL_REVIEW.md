# Personal review: real-time gauge two-point limit

2026-09-16 UTC. Same-author review, not independent review or audit.
The user requires personal execution without subagents.

Source: notes/BLOCK05_JOINT_REAL_TIME_GAUGE_TWO_POINT.md, composed on
provisional Blocks01--04 pushed at fb9a6de8584f5e0675e34d0a040a4c832e8b0ef5.

## Consequential checks

- The propagation result is not inferred from characteristic convergence.
  The note separately obtains second moments from the Q commutator and
  annihilator estimate. This also controls the nonlocal-smear approximation.
- The exact current convention is J=-partial_theta H_m. The electric
  equation is [calH,P(u)]=iZ(Su)-igJ(W_E^(1/2)u). A literal charged Gauss
  ring with CAR signs checks this against matrix commutators. Reversing
  the current sign gives a large discrepancy. The residual identity acts
  on actual ground vectors, and its smallness is a norm statement.
- The full ground-space trace is represented by Hilbert--Schmidt vectors;
  no unique finite-box ground state is assumed. The finite fixture uses
  one computed ground vector only to challenge the universal identity,
  not to establish a finite-volume ground-trace theorem.
- The kernel bound is for Omega, not M. The explicit rank-two square-root
  formula avoids differentiating eigenvectors at a band degeneracy. Its
  second derivatives are O(1/|k|), which are square integrable in three
  dimensions. The weak-derivative boundary terms vanish. Fourier
  Cauchy--Schwarz yields l1 summability, and absolute periodization gives
  the same bound on every finite torus. Reported finite kernel norms are
  diagnostic values, not fitted uniform constants.
- Duhamel is applied to one-field ground vectors with a uniformly bounded
  norm residual. The toy two-oscillator counterexample retains a fixed
  Gaussian vacuum and first moment while changing the limiting frequency;
  it demonstrates why the stronger residual was necessary. It is not a
  no-go for the actual model.
- Magnetic fields use the exact vector relation Z(v)=-iP(Mv)+small terms.
  Fejer approximations have uniformly bounded Fourier suprema and converge
  in L2. Their Omega-weighted error integrands extend continuously at zero.
  The joint g,L limit is taken first for each fixed approximation, then
  the approximation is removed. Unitarity controls the error on bounded
  time intervals without requiring the Riesz kernel to be l1.
- The result concerns fixed local two-point functions and compact time
  intervals. It does not include arbitrary gauge exponentials at different
  times, higher unbounded field products, a time window diverging with 1/g,
  or fixed-positive-g masslessness.

## Retained failures and refinement

The first run stopped with a NumPy TypeError converting a length-one array
to float. Source and traceback are retained in BLOCK05_FAILURE_01. The fix
was explicit scalar extraction, with no mathematical change.

The second run passed the identity and dynamic comparisons, then failed the
declared flux-tail threshold: at g=.6 and cutoff10 the outer-layer mass was
4.984945699760506e-16, above1e-16. Its source, output, traceback and diagnostic
are retained in BLOCK05_FAILURE_02. The electric basis was enlarged from
ceil(6/g) to ceil(8/g), without changing the threshold. At g=.6 the new
cutoff14 tail is4.159846155393039e-30. The t=1.4 propagation discrepancy
changed only from0.5658321036229421 to0.5658321036229407. The other specified
g values also passed the same tail threshold. This is numerical refinement,
not a theorem about truncations.

The final runner's assertion total includes each literal Gauss basis state
and charged transition. It is not a count of independent scientific checks.
The meaningful challenges are the current sign, exact norm residual,
finite charged propagation, square-root formula, and first-moment
counterexample. The full phase theorem is not simulated.

Disposition: complete provisional author proof for the stated two-point
domain, with selective challenges and all encountered failures preserved.
Independent mathematical review is still pending. Source/output hashes are
frozen separately; no audit verdict or main-branch promotion is asserted.
