# VERDICT: NOT CONFIRMED

The worker's **minimal homogeneous, continuum-IR, \(\lambda=1\) Wess--Zumino model** does contain the stated extra pathological scalar.  That calculation is not a Dirac completion of the C3 theory, however: C3 fixes a Killing-sector Taylor coefficient, not the full local bracket or the gauge-invariant part of an effective action.  The fixed W2 result is therefore **INCONCLUSIVE**, not FAIL.

## 1. Reduction of the anomaly and Wess--Zumino consistency

- **What C3 actually fixes.** C3 proves that gravity-dependent completions vanish for a constant shift and an affine lapse, and hence fixes the first Taylor coefficient in the smearing momenta (`RC_C3_report.md:35-41,45-53,66`).  This establishes the irreducible integrated coefficient \(E_c-H_m\).  It does **not** show that
  \[
  -\sum_c\int \xi_c\,\mathcal A_c\,\partial_cN
  \]
  is the complete bracket at arbitrary smearing momentum.  The completion terms vanish in the Killing test but can contribute away from it.  W2 promotes the certificate to a full local representative at `W2_report.md:77-83` and then uses it over the whole Brillouin zone; that promotion is unproved.
- The sign statement is also narrower than reported.  In energy-diagonal free-scalar states the integrated coefficient is \(\sum_q(\cos q_c-1)\omega_q n_q\le0\), but it vanishes for a massive zero-momentum excitation and can vanish in selected directions.  Thus “every background with matter excitations” (`W2_report.md:32-35,65`) must be replaced by “backgrounds with a nonzero relevant anomaly expectation.”
- **WZ consistency of the constant-background representative is confirmed.** For constant \(a\), the commutator of variations is
  \[
  a\,\partial_t\!\int(\nabla\chi_2\!\cdot\!\nabla\epsilon_1-
  \nabla\chi_1\!\cdot\!\nabla\epsilon_2),
  \]
  a boundary term, agreeing with `scripts/w2_stueckelberg_scalar.out:1-6`.
- **The isolated ultralocal-gradient term is inconsistent, but the conclusion is overextended.** The nonzero \(\epsilon_1\partial\epsilon_2-\epsilon_2\partial\epsilon_1\) Euler residual in `scripts/w2_gradient_branch.out:1-6` confirms that this truncated term cannot by itself be an anomaly of the abelianized fields.  It does not prove that the constant-\(a\) representative is the unique full matter-dependent cocycle: the omitted completion terms and the gauge transformation of the matter/background anomaly density were not included (`W2_report.md:94-97,258-260`).

## 2. Rank calculations, lapse, and Dirac count

- The worker scripts rerun exactly and reproduce ranks \(416,624,800\) (`scripts/w2_cnumbers_and_rank.out:37-45`).
- Those finite-torus numbers use the wrong derivative for the supplied staggered constraints: `scripts/w2_cnumbers_and_rank.py:63-64,123-131` uses the site-centred symbol \(\sin p\), with eight zeroes on an even \(6^3\) torus.  The supplied gravity construction uses the edge/midpoint symbol \(2\sin(p/2)\), with no Brillouin-zone doubler (`LOCAL_FINITE_CLOCK_TENSOR_CONSTRAINTS_CUBIC_DISPERSION_AND_LINEAR_GRAVITY_BOUNDARIES_BOUNDED_THEOREM_NOTE_2026-09-14.md:95-103,299-303`).  My independent implementation reproduces the worker values with the central difference, but the edge difference gives formal model ranks \(430,750,852\), respectively (`scripts/w2_referee_checks.py:22-88`; `scripts/w2_referee_checks.out:1-11`).  The current-sector ranks are additionally only ranks of the worker's chosen mean-field rotation block, not a derivation from a specified current-carrying solution.
- The algebraic formula \(N_{\rm dof}=2N+r/2\) is correct **conditionally**: with \(4N\) independent constraints, rank \(r\), no further constraints, and the matter baseline subtracted, there are \(4N-r\) first-class and \(r\) second-class constraints.  W2 does not establish those hypotheses.  In particular, it does not run the full Dirac chain or compute the brackets with the canonical Hamiltonian; “no secondary constraints” is asserted from invertibility only (`W2_report.md:106,119-123`).  Global/reducible torus modes and the lapse/shift primary constraints also require explicit treatment before the displayed finite-volume counts are physical counts.
- Projectability follows only for a homogeneous background for which every relevant \(\mathcal A_c\) is nonzero: then \(\mathcal A_cD_cn=0\) enforces spatially constant \(n\).  Anisotropic beams, zero-momentum quanta, local zeroes, or incomplete rank can leave directional/null lapse freedom.  The unqualified statement at `W2_report.md:119-121` is too broad.

## 3. Stückelberg action, pole, signs, and the BD label

- The displayed \(L_{\rm WZ}\) is a valid **particular minimal solution** for the constant-\(a\), nine-term ansatz (`W2_report.md:154-169`).  It is not unique.  The combinations
  \[
  U=\Phi+\dot\pi,\qquad V=B-\pi+\dot\zeta,\qquad W=E+\zeta,
  \]
  together with \(\Psi\), are gauge invariant.  Arbitrary local quadratic functionals of them may be added without changing the anomalous variation.  The worker's ansatz omits, for example, complete \(U^2\), \(W^2\), and derivative/kinetic invariants; this is shown explicitly at `scripts/w2_referee_checks.py:115-121`.  “Uniquely fixed” is therefore false except after the unstated convention that every invariant completion coefficient is set to zero.
- **Within that minimal convention, the spectrum and signs are confirmed.** Independent elimination of \(\Phi,\Psi,\pi\) gives
  \[
  K_\zeta={a\over8M_P^2}
  [\,(2M_P^2k^2-3a)\omega^2+a k^2\,],
  \qquad
  \omega^2={a k^2\over3a-2M_P^2k^2}.
  \]
  The \(\omega^2\) coefficient is negative for all \(k\) when \(a<0\), and for the real-frequency low-\(k\) branch when \(a>0\); the high-\(k\) \(a>0\) branch is tachyonic (`scripts/w2_referee_checks.out:13-17`).  Thus the minimal model has one ghost for physical \(a<0\), and a ghost/tachyon split for \(a>0\).
- For \(a<0\), \(|\mu|^2=|a|/(2M_P^2)\) is a high-momentum band ceiling/crossover, not a mass gap: the mode is gapless at \(k=0\).  Calling it an “anomaly-set mass” without this qualification is misleading (`W2_report.md:179-184`).
- “Boulware--Deser-like” is acceptable as an analogy to loss of the Hamiltonian constraint and release of a negative-energy conformal scalar.  It is not literally the Boulware--Deser mechanism, which concerns the generic nonlinear sixth mode of massive gravity.  W2 has neither established a massive spin-2 theory nor completed the nonlinear constraint analysis (`W2_report.md:186,199-205`).

## 4. BPS \(\alpha\), \(\lambda\ne1\), and the scope of the result

- In the worker's minimal \(\lambda=1\) matrix the \(\zeta\) equation imposes \(U=\Phi+\dot\pi=0\) on the pole, so adding only \(\alpha M_P^2(\nabla U)^2\) leaves that determinant and its sign unchanged.  This part is confirmed (`scripts/w2_extra_checks.out:4-5`; `scripts/w2_stueckelberg_with_khronon_term.out:1-10`).
- This does not establish irrelevance of the BPS healthy extension.  The full nonprojectable theory contains the \(\lambda\ne1\) kinetic structure as well as \(\alpha\); the supplied F1 calculation has a healthy quadratic window for \(0<\alpha<2,\lambda>1\) (`C4_F1_report.md:156-175`), and its independent referee explicitly leaves that realization open (`C4_F1_referee.md:13-16`).  W2 itself records this as untested at `W2_report.md:188,301-302`.  The combined anomaly plus \(\lambda\ne1\) constraint/action must be recalculated; one cannot extrapolate the \(\lambda=1\) null-vector identity to a verdict on the window.
- More basically, even at \(\lambda=1\) the gauge-invariant completion ambiguity in item 3 prevents the anomaly alone from selecting the minimal action.  Thus the \(\alpha\)-only check does not close the fixed W2 question.

## 5. Vacuum, branches, observations, and strong coupling

- The one-band vacuum identity is confirmed independently:
  \(\langle E_c\rangle=-\langle T_{cc}\rangle\) and hence
  \(\langle E_c-H\rangle/V=-(\rho+p)\) (`scripts/w2_referee_checks.out:27-28`; `C4_I3_referee.md:5-11`).
- A covariant cosmological-constant counterterm leaves \(\rho+p\) invariant and cannot cancel this anomaly (`C4_I3_referee.md:10-11`).  A separate preferred-frame pressure/completion counterterm may cancel it, but W2 explicitly did not complete the sign and bracket bookkeeping (`W2_report.md:142-148`).  Accordingly, “vacuum rank 0 after counterterms” is an assumed branch, not a checked result, and the two listed branches are not exhaustive once other invariant/kinetic completions are admitted.
- The thermal scaling and vacuum numerical integrals reproduce, but the observational conclusions do not.  In the excitation-only branch no fifth-force, radiation, vacuum-decay, or strong-coupling amplitude was computed (`W2_report.md:211-216`).  The vanishing quadratic normalization as \(a\to0\) and the formal rank jump are warnings of strong coupling, but they do not derive the stated scale \(E\sim T\); that estimate assumes an uncomputed nonlinear coupling (`W2_report.md:193-195,282-286`).  Likewise, a light gapless ghost does not automatically have “tiny phase space”; ghost decay is UV- and coupling-sensitive.
- The unabsorbed-vacuum branch is pathological in the chosen minimal model, but the claim that its continuum dispersion covers the entire Planck-scale Brillouin zone extrapolates an explicitly continuum-IR calculation beyond its domain (`W2_report.md:156-158,190-192`).  “Excluded” additionally requires its matter coupling, cutoff, and decay rate.  W2 labels those statements suggested and cites only a comparator from memory (`W2_report.md:218-221,282-287`).  They cannot carry the verdict.

## 6. Fixed-reading verdict

The fixed FAIL criterion requires that the **broken theory**, not one optional WZ representative, be shown to contain a ghost/tachyon or a bound-violating anomaly-mass mode (`TESTS.md:1351-1367`).  W2 has produced a valuable pathological example, but it has not derived the full local anomaly, completed the Dirac algorithm, fixed the invariant part of the action, or tested the admitted \(\lambda\ne1\) counterroute.  Its own negative-claim record concedes that the five routes are not independent and that the strongest counterargument is untested (`W2_report.md:289-302`).  Therefore **W2 is INCONCLUSIVE under the fixed readings**, and the worker's **FAIL (bounded)** is not confirmed.

**Strongest correct statement:** For the fixed 09-14 generators and L1 single-band scalar, C3 rigorously leaves a nonzero Killing-sector coefficient \(E_c-H_m\) on states carrying nonzero lattice momentum, so exact GR constraint closure fails within C3's regular-local completion class.  If that coefficient is replaced by a homogeneous constant background and one additionally chooses the minimal \(\lambda=1\) Wess--Zumino completion with all gauge-invariant quadratic additions set to zero, the scalar sector has exactly one extra pole, \(\omega^2=a k^2/(3a-2M_P^2k^2)\), which is a ghost for the physical negative sign and becomes tachyonic above the crossover for the opposite sign; the \(\alpha(\nabla(\Phi+\dot\pi))^2\) term alone does not alter it.  The one-band vacuum identity \(\langle E_c-H\rangle=-(\rho+p)\) is exact.  These results do not show that the C3 anomaly uniquely produces that action or spectrum: the full local bracket, Dirac chain, gauge-invariant completion, vacuum counterterm, and \(\lambda\ne1\) khronometric window remain open, so the fixed W2 verdict is INCONCLUSIVE rather than bounded FAIL.
