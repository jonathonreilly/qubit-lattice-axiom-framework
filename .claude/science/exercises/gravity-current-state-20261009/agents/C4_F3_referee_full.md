# VERDICT: NOT CONFIRMED

The correct fixed-reading disposition is **F3 INCONCLUSIVE**, not bounded
FAIL.  The explicit fine-grid and explicitly coarse-grained realizations do
carry a new scale hierarchy, but the claimed Pospelov--Shang number mixes
Planck conventions and observables, the tadpole is only a scalar-toy power
count, the superlattice and dimensional-transmutation exclusions are not
no-go results, and R4 is wrongly removed from RF.  In particular, the RF lane
itself expressly includes khronometric gravity (`TESTS.md:1293-1304`).

Independent arithmetic is in `referee_checks.py:1-103` and
`referee_checks.out:1-12`.  All three worker scripts reproduce their saved
outputs, so the corrections below concern their formulas' physical use and
one slowly convergent lattice integral, not output drift.

## 1. Pospelov--Shang formula, bound, convention, and vector term

- **Formula mostly confirmed; bound not confirmed as stated.**  Eq. (55) of
  Pospelov--Shang has the three terms transcribed at `F3_report.md:63-70`,
  including the uncured `-Lambda_UV^2/(24 pi^2 M_pl^2)` vector term.  The
  paper defines `G_N=1/(8 pi M_pl^2)`, however, so its `M_pl` is the **reduced**
  Planck mass.  The worker's 1.069e10 GeV branch treats the same formula as if
  its denominator were the non-reduced Planck mass (`scripts/f3_numbers.py:11-24`).
  It is not a second Pospelov--Shang convention.
- With the packet's registered ruler `a^-1=1.221e19 GeV` as the UV cutoff and
  the Pospelov--Shang denominator `Mbar_pl=2.435e18 GeV`, solving the first
  logarithmic term alone against 2.664e-19 gives
  `M_*=2.038e9 GeV`, `2 ln(Lambda_UV/M_*)=45.027`, and
  `L_grid=5.990e9` (`referee_checks.out:1-3`).  Moreover, the F2 number is a
  **speed** difference `c_e-c_gamma` (`C4_F2_referee.md:23-29,60-62`), whereas
  Eq. (55) is a photon-minus-**scalar squared-speed** correction.  Even if one
  substitutes the electron by the scalar, conversion to a squared-speed
  difference doubles the bound and gives `M_*=2.906e9`, `L=4.202e9`
  (`referee_checks.out:4`).  The spin and sign mismatch means neither is a
  sharp photon-decay bound on the Pospelov--Shang model.  The paper's own
  `~1e10 GeV` statement is an order-of-magnitude estimate, and the full
  improved-model answer also depends on the scalar and vector scales and on
  gravity parameters.  Thus `1.07e10 / 2.1e9` is not a legitimate pair of
  convention alternatives (`F3_report.md:74-83`).
- The same convention issue makes the uncured one-grid vector term **0.1062**,
  not 0.00422: the latter follows only when the UV cutoff is also set equal to
  the reduced Planck mass (`referee_checks.out:6-7`).  The qualitative point is
  stronger and correct: every graviton component that contributes must be UV
  softened.  Pospelov--Shang explicitly identify the non-Lifshitz vector
  propagator and cure it with a higher-spatial-derivative kinetic term.
- The healthy-window compatibility survives.  For the direct-substitution
  `M_*=2.038e9` branch and the worker's `gamma=0.01`, the same GSS formula gives
  `alpha>1.69e-13` (`referee_checks.out:8`), well below the stated weak PPN
  ceiling.  The report's `2e-12` is sufficient but corresponds to its older
  `1.5e10 GeV` benchmark (`scripts/f3_numbers.out:27-28`).

## 2. R1 coefficients and self-feed

- For a dispersion `omega^2=k^2+k^6/M_*^4` on a grid with `a^-1=M_grid`, the
  dimensionless six-spatial-derivative coefficient is exactly
  `(M_grid/M_*)^4=L^4`.  Under the conditional squared-speed substitution above
  it is `3.12e38`; under direct substitution it is `1.29e39`
  (`referee_checks.out:3-4`).  The report's low endpoint `4.4e35` comes from
  the older `M_*=1.5e10` estimate, not its stated Pospelov--Shang Eq. (55)
  bound (`scripts/f3_numbers.py:38-47`; `F3_report.md:115-118`).
- The Pospelov--Shang vector cure is different: `(grad K)^2/Lambda^2` carries
  a lattice coefficient `(M_grid/Lambda)^2=L^2`, **not** `L^4`.  It need only
  turn the static `1/k^2` vector propagator into `1/k^4` to make the relevant
  loop logarithmic.  Hence the sentence that the vector term "needs the same"
  coefficient is false (`F3_report.md:117`; `referee_checks.out:9-10`).
- The worker's scalar integral is algebraically sound.  From
  `int d omega/[2 pi(omega_hat^2+A)]=1/sqrt(A(A+4))`, its large-`L` discrete-time
  limit is the cubic Watson integral `<1/p_hat^2>`.  An independent
  one-dimensional Bessel representation gives **0.2527310099**, not 0.2513;
  the latter is the slowly convergent `96^3` midpoint value
  (`scripts/f3_tadpole.py:7-23`; `referee_checks.py:53-70`;
  `referee_checks.out:11`).  Independent Gauss--Legendre quadrature confirms
  the continuous-time coefficient **1.1938011242 L^2**
  (`referee_checks.out:12`).
- Those two numbers are not established graviton self-energies.  The runner
  assumes one scalar component and one `C p_hat^4 k^2` seagull, while dropping
  tensor contractions, gauge/constraint fields, Ward cancellations,
  combinatorics, and the Planck-normalization factor
  (`scripts/f3_tadpole.py:1-8`; `F3_report.md:124-133,222-226`).  It supports
  the conditional power count `O(1)` on Z4 and `O(L^2)` with continuous time,
  but not the precise natural value of the gravity speed coefficient or the
  quoted tuning fractions.  The Z4 calculation also does not establish the
  reflection-positive nonlinear gravity theory required by lane K2
  (`TESTS.md:1495-1500`).

## 3. R2 and the superlattice argument

- An **explicit** coarse graviton cell of size `ell=L a` introduces the new
  dimensionless datum `L~10^9`; the scale-reference primitive supplies only a
  ruler and no dimensionless ratio (`PRIMITIVE_REGISTRY_CHECK.md:31-54`).  That
  is a genuine hierarchy in the law.  A mere periodic modulation also folds
  microscopic bands rather than deleting them, so it does not by itself give
  the all-component UV softening demanded above (`F3_report.md:135-150`).
- The spontaneous-superlattice exclusion is only an ansatz-level naturalness
  argument.  For a Landau kernel `c2 Q^2+c4 Q^4`, minimization indeed gives
  `Q^2=-c2/(2c4)`, so `Q a~10^-9` requires a coefficient ratio of order
  `10^-18` (up to the period's `2 pi`).  But no theorem shows that every
  translation-covariant nearest-neighbour law generating a long collective
  length is described by that weakly coupled gradient expansion.  Critical,
  asymptotically-free, frustrated/commensurate, and strongly collective
  mechanisms are not excluded; nor was the asserted unsuppressed folded-band
  percolation computed (`F3_report.md:143-149,247-251`).  R2 therefore fails
  as a universal superlattice argument, though the explicit-cell subcase does
  pay the hierarchy.

## 4. R3 dimensional transmutation and Weinberg--Witten

- The displayed one- and two-loop gauge-coupling arithmetic is correct in its
  scheme: generating `Lambda_h/M_grid=10^-9` needs ultraviolet alpha values of
  order 0.015--0.043 (`scripts/f3_numbers.py:48-62`;
  `scripts/f3_numbers.out:38-43`).  The species estimate is also a reasonable
  **minimal-coupling, weak-loop** power count: an ordinary hidden sector whose
  only communication with an existing Planck-stiff graviton is its stress
  tensor changes the quadratic action by order
  `C_T k^2/(16 pi^2 Mbar_pl^2)` (with representation-dependent coefficients),
  and needs a huge `C_T` at `k~M_*` (`scripts/f3_species.py:1-11`).
- **"DT cannot transfer the scale" is not established beyond that class.**
  The report itself concedes the result is one-loop/spectral power counting
  (`F3_report.md:165-179,222-225`).  It does not exclude a direct non-minimal
  portal to foliation operators, dimensional transmutation in the
  gravitational sector itself, induced-gravity/threshold matching, a critical
  sector with large anomalous dimensions, or an LV/nonlocal emergent sector.
  More pointedly, the 3+1-dimensional projectable-Horava RG literature finds
  asymptotically-free trajectories and reports a **natural hierarchy** between
  the Lorentz-violation scale and the infrared Planck mass.  That projectable
  theory is not a viable RF3 solution--F1 already rejects the projectable
  realization--but it is a direct counterexample to the claimed general RG
  obstruction.  No all-orders theorem in the packet upgrades the worker's
  loop estimate.
- Weinberg--Witten is also overstated.  It excludes an exact massless
  spin-2 composite carrying energy in a Lorentz-invariant theory with a
  suitable Lorentz-covariant conserved stress tensor; the packet itself warns
  that classic theorems hold only under their listed assumptions
  (`PRICE_NOTE.md:113-125,150-154`).  It does not exclude an LV hidden sector,
  nonlocal/holographic realization, loss of a gauge-invariant local stress
  tensor, or a hidden sector merely inducing operators for an already supplied
  graviton.  Thus it closes one conventional composite subroute, not R3.

## 5. R4 classification and lane dependence

- **R4 is an RF realization, not P0 merely because it is covariant.**  The
  registered RF question explicitly names khronometric/BPS and
  Einstein--aether gravity as preferred-foliation theories
  (`TESTS.md:1293-1304`).  In the covariant/Stueckelberg description the full
  diffeomorphism redundancy coexists with a dynamical scalar whose timelike
  gradient defines a physical foliation; unitary gauge leaves FDiff, and the
  extra khronon mode does not disappear.  The worker's inference
  "full diffeomorphisms remain, therefore not RF" confuses gauge redundancy
  with absence of a preferred physical background (`F3_report.md:170-177,216`).
- R4 is not thereby a PASS.  The worker did not construct its condensate from
  the qubit nearest-neighbour law, verify all PPN/binary/strong-coupling bounds,
  or prove that matching to grid matter adds no counterterm; it expressly says
  the lattice gauge realization was not shown (`F3_report.md:170-177`).  The
  honest status is **INCONCLUSIVE**.  But because R4 is inside RF and is an
  examined route not shown to violate a bound or need an extra hierarchy, the
  fixed FAIL gate is not met (`TESTS.md:1516-1519`).
- The directionality statement is sound but the claimed dominance is only a
  dependency reading.  Pospelov--Shang suppresses gravity-to-matter LV; it does
  not establish the reverse matter-to-gravity Ward identity, TT response, or
  graviton-speed match (`C4_E1_referee.md:13-19`).  K2 is still an unperformed
  exact-gauge/reflection-positivity test (`TESTS.md:1480-1504`), so neither
  branch of `F3_report.md:191-205` is a theorem and K2 cannot close F3.

## 6. Does a large law coefficient count as "a hierarchy beyond P0"?

**Yes, under the literal fixed reading.**  RF3 deliberately says "a hierarchy
or tuning beyond P0," not "more tunings than P0" (`TESTS.md:1516-1521`).  The
registered scale primitive supplies `a^-1=M_Pl` as a conversion only and
explicitly supplies no dimensionless ratio (`PRIMITIVE_REGISTRY_CHECK.md:31-54`).
Consequently an independently supplied `L~10^9`, `L^2`, or `L^4` is a new
dimensionless hierarchy beyond the P0 package.  It is **not automatically a
precision tuning**, an axiom contradiction, or a coefficient required to be
order one; the F2 referee already made exactly that distinction
(`C4_F2_referee.md:47-53`), and the axioms do not choose a Hamiltonian
(`MINIMAL_AXIOMS_2026-06-29.md:114-130`).  This reading validates the hierarchy
price for explicit R1/R2 parametrizations, but it cannot turn the unproved R2
and R3 exclusions or the misclassified R4 into "every examined realization."

## Strongest correct statement

On one grid, a Pospelov--Shang-type **explicit** Hořava crossover must soften
every contributing graviton component and introduces a large dimensionless
scale separation: using the paper's reduced-Planck normalization with the
packet's non-reduced Planck grid gives a conditional first-term scale of a few
`10^9 GeV`, hence `L` of a few `10^9` and a TT `k^6` coefficient of order
`10^38-10^39`; an explicitly coarse graviton cell likewise writes `L` into the
law.  These are legitimate hierarchies beyond P0, though not automatically
precision tunings.  The scalar-toy self-feed scales as `0.252731` on Z4 and
`1.193801 L^2` with continuous time, but is not a computed graviton
self-energy.  A minimally coupled weak hidden sector cannot appreciably bend a
Planck-stiff graviton without enormous central charge, yet no all-orders result
excludes gravitational RG, portals, critical transfer, or other
dimensional-transmutation mechanisms; and a dynamical khronon remains a
preferred-foliation RF theory despite covariant notation.  Therefore the
packet establishes a hierarchy for the explicit R1 and R2 subcases, not that
every examined one-grid RF realization needs one, so F3 is **INCONCLUSIVE**.

## Primary literature checked

- Pospelov--Shang, Eq. (55), vector propagator/cure, and Planck convention:
  <https://arxiv.org/pdf/1010.5249>
- BPS khronon as the dynamical preferred foliation and its covariant form:
  <https://arxiv.org/pdf/1007.3503>
- Projectable-Horava RG and the reported natural hierarchy:
  <https://arxiv.org/abs/2411.13574>
