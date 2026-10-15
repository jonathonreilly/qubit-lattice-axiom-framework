# Focused independent force and energy bridge check

Reviewer: `/root/force_energy_bridge_check`. This is a mathematical source and
implementation check, not a formal audit or an empirical acceptance verdict.
Root remains the scientific author. Only this independent evidence directory
was written by the reviewer.

## Source and independence

The reviewed hand derivation is `SCALAR_FORCE_ENERGY_BRIDGE_WORKING_v1.md`,
SHA-256 `5ec2ac2647b2d86b1fc699b63d4b1af6cd19c56a2d1cc73277589f8e73f85a40`.
The supplied action and response notes and moving-path note were read first;
their full identities are in `SOURCE_FREEZE_v1.json`. A hand derivation and
planned controls were frozen in `PRECHECK_v1.md` before author implementation
access. The independent checker and its 253 controls were then written and
executed before the author runner was opened. The independent code does not
import or invoke author code.

After this run I read `force_energy_bridge_check_v1.py`, SHA-256
`45ece394a7056dfac76a0b654b37b0414de62c14d59f8f7a1abb3faeea625b4e`,
and inspected its recorded result: 49 author controls, with matching note and
script source identities. I did not rerun the author suite. Final file identities
and access order are in `REVIEW_IDENTITY_v1.json`.

## Conclusion

No mathematical discrepancy was found in the exact test-particle equation,
coefficient budgets, first-derivative energy functional, shared multi-mode bound,
constant-velocity formulas, Q normalization or constant-background frame change.
The result is conditional. It provides no derivation of the supplied action,
initial scalar energy, stable physical mode spectrum, actual motion or readout.

One nonblocking presentation clarification is recommended: distinguish restoring
units on both sides from multiplying an already SI-valued right side by c².
With SI Newton G, scalar perturbation energy in joules, and a triangular
half-width Delta t in seconds, the stationary limiting bound corresponding to
(7) is

    a_phys <= sqrt(8 G_meas E_phi / [9 (c Delta t)^3]).

Here a_phys means the constant-background coordinate acceleration per second
squared used in the note, after its kinematic/readout premises. It is not an
extra assertion that this is the proper acceleration measured by a real clock.
One way to restore units is to write the dimensionless-field quadratic energy
as E_phi=(c^4/(4 pi G_bare)) E_math. The s=ct acceleration bound then has an
extra c^-2 on its right side, canceled when converting a_s to a_phys=c² a_s.
All normalizations and premise restrictions in the note remain necessary.

## Independent mathematics

1. The exact momentum equation is
   `(I+gamma² vv^T)a=-(1-v²)grad ell-v(partial_s ell+v.grad ell)`.
   Its inverse matrix is `I-vv^T`, giving exactly
   `a=-(1-v²)(grad ell+v partial_s ell)`. This agrees with the action's
   Euler-Lagrange equation. The total derivative in the intermediate momentum
   equation must not be substituted for the partial derivative in the final
   acceleration formula.

2. For `L=1-v²` and `f=n.v`, the identities
   `L'=-2v.a`, `L''=-2(a.a+v.j)`,
   `f'=n'.v+n.a`, `f''=n''.v+2n'.a+n.j`
   give the displayed derivative budgets of `P=Ln` and `R=Lf`. The estimates
   use `0<L<=1`; they do not assume favorable derivative signs. The direction
   derivative and velocity derivative terms in R2 are present.

3. In energy coordinates `(Omega q_hat,p_hat)`, define half-wave integrals
   with amplitudes `w(P.k/Omega+R)` and `w(P.k/Omega-R)` and phases
   `k.x+Omega s` and `k.x-Omega s`. The cosine/sine coefficient pair is
   `i(J_plus+J_minus)/2` and `(J_plus-J_minus)/2`. Their squared norm is
   `(|J_plus|²+|J_minus|²)/2`. Thus there is no missing factor two in the
   stated dual norm. The same envelope applies to both signs. Angular
   integration uses a full 4pi rather than pulling out a fixed direction.
   The radial integral is `(4/3) Bjet^(3/2) L0^(1/2)`, and multiplication
   by `4pi/(2pi)^3` gives the displayed `2/(3pi²)` coefficient.

4. The prescribed constant-velocity massless control admits independent
   angular antiderivatives. For `0<u<1`, define `L_u=log[(1+u)/(1-u)]`.
   The two integrals in equation (5) equal

       I_parallel = (L_u-2u)/u^3,
       I_perpendicular = [2u/(1-u²)-L_u]/u^3.

   Their u=0 limits are 2/3 and 4/3. The longitudinal `z-u` is required by
   the partial time derivative term. At the synthetic u=0.85, T=1.7,
   the full parallel squared norm is about 0.00329961; dropping that time
   term gives about 0.0501099. These are numerical controls of a prescribed
   reference path, not physical solutions for an accelerated body.

5. The finite-mode estimate uses one joint energy budget. For each mode the
   dual norm is at most Cjet; a Cauchy-Schwarz inequality over mode index
   gives `sqrt(2 q E_tot) Cjet`. The normalization of h here is kinetic-metric
   orthonormality, not rescaling the fields to remove Q. The latter change
   would also change the coupling components. The independent nontrivial-K
   checks confirm `sum alpha_j²=b^T K^-1 b` after stable mass diagonalization.

6. The Legendre energy of the specified positive quadratic scalar action is
   `2Q E_math`. This statement uses a free operator that matches the supplied
   quadratic action, with Q>0 and mu_j²>=0; the kinetic normalization alone
   does not derive mass values, positivity of a rolling-background response,
   or positivity of the full coupled gravity/matter energy.

7. Constant coordinate scaling gives
   `E_math,J=A_b E_math,E`, `Q_J=Q/A_b²`,
   `E_phi,J=E_phi,E/A_b`, `Cjet,J=A_b^-3/2 Cjet,E` and
   `a_J=A_b^-1 a_E`. The bound transforms consistently. The mass must also
   scale as `mu_J=mu_E/A_b`, and the normalized temporal window as
   `w_J(s_J)=w_E(s_J/A_b)/A_b`.

8. The action's algebra yields `q=a/J<a<1/3` in its stated domain. Given an
   actual same-background calibration with nonnegative scalar geometry
   contribution, `G_bare<=G_meas`, so `G_bare q<=G_meas/3` is valid.
   Signed geometry, environmental changes and unstable mass response do not
   establish that inequality. They are explicitly outside the substitution.

## Executed evidence

`independent_force_bridge_check_v1.py` produced 253 passing controls and zero
failures in 0.3391 seconds. Its script hash is
`0ecb1de938963e26fbd8c6165c726ba35cc5e8122b6940f37184b2206d8badfc`.
`INDEPENDENT_RESULTS_v1.json` stores every result; stdout and empty stderr are
preserved. There were no failed or interrupted attempts to suppress.

The controls include symbolic inversion and exact momentum identities; 24
independently solved Euler-Lagrange systems; four direct momentum finite
differences; full symbolic derivative evaluation on a turning three-dimensional
path with a rotating direction; and an asymmetric compact smooth window.
Sixteen wave vectors spanning massless and massive cases compare direct
cosine/sine quadrature with half-wave coefficients and their energy norm.
Further checks cover radial envelope integration, independent angular
antiderivatives, omitted-time-term witnesses, Gaussian energy with both field
and velocity data, constant-frame transformations, shared mode energies,
non-diagonal field metrics and stable mass diagonalization, the candidate
coupling ceiling, and positive/signed geometry applicability.

The largest recorded absolute difference in the numerical equality controls is
8.04e-11. One final simple tachyonic-oscillator diagnostic records why a
nonnegative-mass hypothesis is required; it is not a finite-energy spatial
counterexample or a theorem about the full nonlinear candidate. Likewise the
missing-term and signed-geometry witnesses are not author-code mutation tests.
Finite numerical controls support the analytic arguments; they do not replace
the continuum proof, quantify physical approximation errors, or certify a
measured scalar-energy budget.

## Surviving scientific premises

The ideal fixed-Jordan-mass test body and frozen flat Einstein metric are
assumed for the exact force identity. Its application to free scalar modes
then adds a leading perturbative expansion, constant mode couplings, a stable
free operator, controlled reference trajectory/direction, and finite energy.
Source response, tensor gravity, background gradients, finite-size/self-gravity,
radiation reaction and higher perturbative terms remain external to this bound.
The constant-background coordinate transformation does not calibrate a real
station clock or supply the two-way light-time operator. The archived count
products, geometry removal, actual energy budget and laboratory gravity response
must still be supplied and independently justified. No observation values or
reserved test data were opened in this check.
