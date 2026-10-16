# Focused independent check: moving temporal scalar history

Checker: /root/localized_history_check. The scoped formulas in
MOVING_TEMPORAL_HISTORY_WORKING_v1.md agree with my independent derivation.
I found no unresolved mathematical discrepancy in the two-IBP identity,
frequency-sign factors, fixed and rotating envelopes, or the geometric
readout term. This is a focused mathematical check, not a formal audit,
a physical trajectory determination or an observational validation.

## Order and scope

I froze the source-note hash and saved MOVING_PRECHECK_v1.md before opening
the author's moving-path checker or results. I then read the entire author
script and the complete 133-control result. Those controls were not rerun
or included in the independent total. Separate control representations
were derived and saved in MOVING_CONTROL_ORACLES_v1.md before execution.
The independent checker imports no author code.

The proof domain is the supplied stable, flat, constant-mass free
Klein-Gordon field; a prescribed C3 path with a uniform strictly
subluminal velocity bound and supplied acceleration/jerk bounds; and a
real continuous compact weight whose weak first derivative is integrable
and of bounded variation. The changing-direction result additionally
requires the supplied real C2 direction and its derivative bounds.
Schwartz data provide the direct Fourier proof; the bounded functional
has the corresponding energy-space extension. No classical trace for
arbitrary rough energy data is silently assumed.

## Distributional integration by parts

For E(s)=exp(-i*psi(s)) and psi'=Omega*d,
I=-i/Omega*integral (w/d)' E and then
I=-Omega^-2*integral [(w/d)'/d]' E.
Expanding the last derivative gives exactly
w''/d^2 - 3*w'*d'/d^3 - w*d''/d^3 + 3*w*(d')^2/d^4.
The sign and coefficients are correct. The compact continuous weight
removes first boundary terms, while jumps in w' survive as atoms in w''.
For a triangle their absolute masses sum to 4/T^2. They cannot be removed
merely because the ordinary second derivative vanishes between knots.

For the positive-frequency phase d>=1-v_*. For the other frequency one
may either use |d|>=1-v_* directly or conjugate and invert k to recover
the positive form. Both yield the same envelope. The C3 path and the BV
weight justify the distributional product rule and multiplication at all
atoms. The isolated massless zero-frequency point is harmless in the
Fourier integral and is handled by the direct W0 bound.

## Energy constants and rotating direction

Along a moving path the time-integrated cosine and sine coefficients
C_k,S_k are generally complex. Their squared sum is exactly
(|I_plus|^2+|I_minus|^2)/2. There is no missing factor two or unaccounted
cross term. Reality relates opposite wave vectors. The two frequency
contributions agree after spatial integration; they need not agree for
individual wave vectors.

For fixed e, the joint energy vector gives the stated integrand with
(e.k)^2/Omega^2. The uniform phase envelope allows angular integration,
and the remaining radial integral is (4/3)*B^(3/2)*W0^(1/2).
The resulting fixed-direction coefficient 2/(9*pi^2) is correct. The
moving-path Gram matrix is not generally isotropic, but the common upper
bound for every fixed unit e controls its largest eigenvalue. Thus the
full vector average needs no extra sqrt(3).

For a rotating direction, absorb n.k/Omega into the real time amplitude.
The displayed L0,L1,L2 product bounds and B_rot follow. Its two-frequency
coefficients have odd conjugacy under k inversion, whose extra sign drops
out of their squared magnitudes. The safe angular estimate is now the
full 4*pi, giving 2/(3*pi^2). The factor-three loss in squared norm is
conservative and correctly distinguished from the fixed-direction result.
The stationary-path specialization need not saturate the sharper earlier
fixed-point norm.

## Independent execution

The independent checker ran successfully once: 61 controls in about
0.121 seconds. No failed execution or repaired scientific formula was
encountered in this focused check. The controls use several representations
different from those in the author's checker:

- A signed, asymmetric polygonal weight with five knots tests W0 as an
  absolute integral and W2 as total variation. A cubic path and a nonunit
  changing polynomial direction test all product and phase terms. The
  IBP integrand is generated from the unexpanded nested derivative,
  rather than copying the author's four-term expression. Twelve mode
  cases check both signs and both projection types. Maximum discrepancy
  was below 5.98e-16; omitting the atoms gives errors exceeding 0.63.
- A parabolic path permits an explicit inverse phase coordinate. Four
  oriented phase-coordinate quadratures agree with the original time
  integrals to below 1.58e-16, including the decreasing phase branch.
- Direct time quadrature on a finite three-dimensional spectral domain
  constructs the complex cosine/sine coefficients and real Riesz data.
  It verifies the joint energy expression, half-sum of frequency norms,
  full-vector Gram enclosure, rotating amplitude expression and real-data
  symmetry for massless and massive fixtures. The branch-integrated Gram
  differences were below 2.78e-16. These are finite-domain controls, not
  evaluations of the complete infinite-frequency norm.
- A constant vector velocity and rotating unit direction have exactly zero
  vector acceleration but a nonzero adjacent-average readout. The entire
  result is geometric: -0.1883417954, within the N1*v_* bound 0.192.
  This rejects omission of n'.v without relying on a mixed force example.
- An explicitly null path tests the boundary of the theorem. For the
  massless T=1 triangle, a forward cone contributes at least
  sinc(1/2)^4*(Lambda^2-4)/(32*pi^2) to the squared energy dual norm.
  The analytic lower bound diverges. Independent cone-coordinate
  quadrature agrees with its exact sector formula. The case lies outside
  the uniform-timelike domain; it is not a counterexample to the theorem.

The numerical quadratures are not interval certificates. The inequalities
rest on the independently saved analytic derivation. The null-path lower
bound is an explicit boundary control within the supplied continuum
operator, not a global claim about physically possible observations.

## Readout and physical limitations

The adjacent-average identity differentiates the complete supplied
product n(s).v(s), yielding n.a+n'.v. Its geometric bound requires that
the same velocity in that readout obey the stated velocity bound and that
the triangular weight be nonnegative and normalized. This is not supplied
by a record format. A changing proportionality, clock coordinate or
retarded endpoint requires additional terms and calibration.

The moving-path extension removes a mathematical fixed-point restriction
for this specified observable. It still assumes the operator, mathematical
energy budget, path/direction functions and all their kinematic bounds.
It does not derive a force law, actual spacecraft motion, physical scalar
energy normalization, measurement errors, count-to-force identification,
curved-background corrections or material response. No empirical data,
held-out products, fitted parameters or independent observation were used.

## Exact reviewed identities

All entries are SHA-256 and were verified unchanged after execution. The
report's own digest is in MOVING_REVIEW_IDENTITY_v1.json.

| File | SHA-256 |
| --- | --- |
| MOVING_TEMPORAL_HISTORY_WORKING_v1.md | 9de4f5427b7824a6b594cc64f2c782b0f15dc602b6245852e1e9c05dc6a4d3c5 |
| moving_temporal_history_check_v1.py | 73a080b441ec9848c70b3d9b1fa90f790490b08fdbaff1374e34a1a4534a2a03 |
| MOVING_TEMPORAL_RESULTS_v1.json | 9d6490fdd9c974651b89db47e062c213f13122a4ee6b3a630d45d3d9165b7597 |
| MOVING_PRECHECK_v1.md | 9f44d46c0d91ae7736da950d7cbeca9ddfba18c70720aa0146183eea349419fd |
| MOVING_CONTROL_ORACLES_v1.md | 7a6f4867349e45e86ebf2aae2b82090ae70c62938906864885b6d3446e415314 |
| independent_moving_check_v1.py | 50f434fd27f801fad78089d21b332131546c21b9793f79029f5356eb43a46a45 |
| INDEPENDENT_MOVING_RESULTS_v1.json | f61a79f3b81fe34c1f05797fe28a117f319cea8c67efc7560c6aa5ab3de1dc7b |
