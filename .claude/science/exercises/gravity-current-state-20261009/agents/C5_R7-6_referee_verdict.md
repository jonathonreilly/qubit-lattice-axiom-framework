# VERDICT: CONFIRMED WITH CORRECTIONS

The fixed reading is **INCONCLUSIVE**.  The narrow numerical obstruction for
the submitted one-dimensional pair-sum Hamiltonian is real and is independent
of a boost ansatz, but several stronger phrasings need correction.  In
particular, the second-quantized cross-check inherits R7-1's disputed `1/2`
prefactor, the “4%” cone defect belongs to that submitted normalization, the
instant-form conclusion is conditional on an extra translation-generator
identification, and neither BT non-locality in the claimed lattice tail norm
nor the packed Hamiltonian's faster-than-power quasi-locality was actually
checked.  The worker's final INCONCLUSIVE category is therefore right; “leaning
PASS” has no evidentiary force under the fixed clause.

## 1. Naive three-body drift and the no-boost implication

- **The submitted drift reproduces.**  The worker's `L=300` values are
  `0.734266071`, `0.733713866`, and `0.732136727` at `P=0`, `0.10472`, and
  `0.20944` (`scripts/r76_threebody_naive_fermi_lam-3.0_kap0.25.out:28-30`).
  A separately written canonical-Slater-determinant construction gives the
  same values and a stable `2.129e-3` drift between `P=0` and `0.20944` for
  `L=180,240,300` (`referee_r76_checks.py:93-165`;
  `referee_r76_checks.out:4-6`).
- **It is not a plateau or leg-box artefact at the reported precision.**
  Raising the flat pair-momentum plateau from `0.8` to `1.5`, and then the leg
  box from `1.0` to `1.2`, leaves all three masses unchanged to nine printed
  decimals (`referee_r76_checks.out:5,11-12`).  This independently agrees with
  the zero shell weight and interior support in the submitted run
  (`scripts/r76_threebody_naive_fermi_lam-3.0_kap0.25.out:28-30`).
- **R7-1's normalization defect is inherited by the stated Fock check.**  The
  cross-check explicitly writes the unrestricted quartic coefficient as
  `1/2` and applies `0.5*val` (`scripts/r76_fock_crosscheck.py:2,28-55`),
  exactly the convention that the R7-1 referee found doubled and required to
  be `1/4` (`C5_R7-1_referee_verdict.md:114-122`).  Its agreement with the
  first-quantized program therefore checks common numerical embedding, not the
  repaired CAR normalization.
- **The drift is nevertheless not caused by that factor.**  A literal
  `1/4` rerun still gives a bound trimer and converges to masses
  `0.851620456`, `0.851498018`, `0.851149947`, a `4.705e-4` drift and
  `delta_low=0.01902` (`referee_r76_checks.out:7-10`).  Widening both plateau
  and box leaves it unchanged (`referee_r76_checks.out:13`).  This literal
  substitution changes the two-body mass from `0.5152956` to `0.5770080`
  (`referee_r76_checks.out:1-2`), so it is a sensitivity test, not a
  convention-free repair: a consistent `1/4` formula must also use the
  correspondingly normalized antisymmetrized two-body matrix element.  Thus
  the existence of drift is robust, while the quoted 4% cannot be presented
  as normalization-independent.
- **The boost-sign error was not inherited in the new BT algebra.**  R7-1's
  defective minus sign is identified at `C5_R7-1_referee_verdict.md:108-113`;
  R7-6 instead uses `K_BT=+{H_BT,X_0}/2` and obtains the correct positive-sign
  commutators (`R7-6_report.md:212-215`).  The naive drift calculation does
  not construct a boost at all (`scripts/r76_threebody_naive.py:3-9`).
- **The fixed-H no-boost implication is correct with its stated regularity.**
  From the three commutators, `[K,H^2-P^2]=0` exactly
  (`R7-6_report.md:163-165`).  A self-adjoint `K` whose local unitary flow
  preserves the common box domain must therefore transport an isolated bound
  state between nearby momentum fibres without changing its Casimir.  A
  genuinely nonconstant limiting trimer mass rules out every such `K`, not
  merely a pairwise boost.  The report itself correctly concedes that a bare
  commutator on a domain, without local integrability, does not suffice
  (`R7-6_report.md:307-310`).  Because the continuum nonconstancy is supported
  by converged finite-ring numerics rather than a certified error bound, the
  honest status is a strong checked obstruction, not a mathematical theorem.
- **Scope correction.**  This establishes a need to modify this particular
  three-particle Hamiltonian (with `P=Q`) by a term invisible in the two-body
  sector—equivalently a connected three-body correction.  It is not a theorem
  that every pair-additive instant-form law fails, as the worker properly
  admits (`R7-6_report.md:201-204,311-312`).

## 2. Continuum transplant and instant form

- **The restricted-operator transplant is correct but conditional.**  If the
  dispersion, first-order generators, and interaction kernels are deliberately
  chosen to equal their continuum counterparts on a common compact invariant
  region, then their restrictions and hence their algebraic identities are the
  same (`R7-6_report.md:113-126`).  This does not show that an arbitrary lattice
  three-body problem “is the continuum one.”  More importantly, invariance of
  the region under the full packed law is only suggested
  (`R7-6_report.md:148-150`), so the full Sokolov transplant is not yet proved
  on the proposed domain.
- **The spectral step `P=Q` is valid under H-P.**  On a branch with
  `e^{iP}=T=e^{iQ}` and `||P-Q||<pi`, the logarithm is unique fibrewise, so
  `P=Q` (`R7-6_report.md:129-132`).  For a nontrivial 1+1-dimensional
  interacting representation this makes spatial translations kinematic while
  `H` and `K` are dynamical, i.e. instant form.
- **H-P is an added bridge, not a consequence of the Lattice axiom alone.**
  The report labels it a “reading” (`R7-6_report.md:73`); the axiom supplies
  lattice translations but no identification with a Poincare generator
  (`MINIMAL_AXIOMS_2026-06-29.md:35-41`), and unfixed physical structure must
  remain conditional (`MINIMAL_AXIOMS_2026-06-29.md:85-95`).  Therefore the
  strongest correct claim is “instant form is forced given H-P and the branch
  bound,” not “the axioms force instant form.”

## 3. BT non-locality and the Sokolov building block

- **Formal BT closure is sound after the sign correction.**  A mass operator
  independent of total momentum together with `K=+{H,X_0}/2` closes the 1+1
  algebra (`R7-6_report.md:208-217`).  The literature also confirms the
  standard distinction: BT gives an exact Poincare representation for any
  particle number but fails generator cluster properties beyond two, while
  Sokolov's recursive unitaries restore them
  ([Polyzou--Keister](https://arxiv.org/abs/1110.1367),
  [Coester--Polyzou](https://arxiv.org/abs/nucl-th/0102050)).
- **`B_a=I` at total `P=0` is confirmed.**  The submitted computation gives
  residuals about `5e-13` for all tested packets
  (`scripts/r76_packing_range.out:2-13`).  This is also the standard instant-form
  packing property: the Wigner rotations become trivial and the packing
  operator becomes the identity at zero total momentum (Keister--Polyzou,
  [review, pp. 159-160](https://homepage.physics.uiowa.edu/~wpolyzou/papers/rev.pdf)).
- **The individual packing operator is long-range in the spectator
  coordinate.**  Translating the spectator from `x=0` to `20,80,320` leaves
  `||(B_a-I)psi||` at `0.14,0.28,0.86,0.63`, rather than tending toward zero in
  the sampled range (`scripts/r76_packing_range.out:22-25`).  This is the
  expected mechanism behind BT's failure of generator clustering.  Those four
  samples do not by themselves prove an asymptotic tail for `H_BT-H_a`; the
  report correctly says that operator was not computed
  (`R7-6_report.md:222-228`).  “BT is not cluster separable” is established;
  the stronger lattice-kernel tail statement is not numerically established.
- **The pair-separation calculation reproduces and preserves norm.**  The
  values extend from `3.21e-2` at `r=40` to `8.16e-9` at `r=600`, with the
  transformed packet norm equal to one to nine decimals
  (`referee_packing_checks.py:59-108`;
  `referee_packing_checks.out:1-12`).  On exactly the worker's three points
  `80,160,320`, a fit gives `exp(-0.7788 sqrt(r))` and log-SSE `0.0388`, versus
  a power fit with log-SSE `0.0852` (`referee_packing_checks.out:13-14`).
  But over `r=40...320` the power fit is substantially better
  (`0.283` versus `2.367`; `referee_packing_checks.out:15-16`).  The data show
  steep decay for one packet; they do not determine an asymptotic
  `exp(-0.8 sqrt(r))` law or prove faster-than-power decay.
- **The full Sokolov claim remains open for this lattice law.**  Standard
  packing theory gives a formal cluster-separable three-body representation
  for sufficiently short-range interactions and requires a symmetrized product
  for identical particles
  ([Reichelt--Schweiger--Klink](https://arxiv.org/abs/1811.09405)).  Here the
  mixed/connected packed Hamiltonian was never constructed or checked
  (`R7-6_report.md:247-267`), and the faster-than-power bound is expressly only
  suggested (`R7-6_report.md:248-263`).  `nucl-th/0102050` supports recursive
  many-body interactions for cluster separability, not the missing tail bound.

## 4. Reading

- The fixed PASS clause requires an explicit three-body box law with exact
  algebra **and cluster separability, checked** (`TESTS.md:3387-3394`).  The
  worker admits that the complete packed construction has no numerical check
  and that its quasi-local tails are unproved (`R7-6_report.md:290-305`).
  PASS is therefore unavailable.
- FAIL is also unavailable: the checked obstruction is confined to one
  pair-sum family, while the standard packing construction is a formal escape
  that changes the three-body generators.  It has not been shown impossible
  to realize that escape with the registered lattice tail requirement.
- The correct registered reading is **INCONCLUSIVE**, without upgrading
  “leaning PASS” into a result.

## No-go stress test

- **N1:** six distinct escape routes were considered: a finite-ring artefact;
  repair of the `1/2` normalization; removal of plateau/box clipping; an
  arbitrary locally integrable many-body boost at fixed `H`; changing the
  kinematic momentum/form of dynamics; and changing `H` through BT/Sokolov
  many-body terms.  The first three were tested and leave a nonzero drift, the
  fourth is blocked by the Casimir commutator, and the last two lie outside the
  fixed-`H`, fixed-`P=Q` statement and prevent promotion to a universal no-go.
- **N2-N3:** the remaining assumptions are not independent “walls” but scope
  hypotheses: fixed `H`, fixed `P=Q`, an isolated positive-energy trimer, and a
  self-adjoint locally exponentiable `K`.  They must travel with the claim.
- **N4:** no prior numerical residual is used as a substitute for the present
  trimer residual.
- **N5:** the conclusion is only per the stated d=1 pair-sum family, not all
  pairwise relativistic dynamics and not all lattice three-body laws.
- **N6-N8:** a connected three-body modification and Sokolov packing are the
  explicit partial-closure route and strongest steelman.  They defeat any
  universal no-go, but not the fixed-H obstruction.  Accordingly the narrow
  checked obstruction survives and the broad no-go does not ship.

## Strongest correct statement

For the submitted d=1 three-fermion Hamiltonian obtained by summing the stated pair BT operators, the trimer invariant mass has a reproducible, finite-size-stable momentum drift that survives widening the interaction plateau and box and also survives a literal halving of the inherited unrestricted-CAR prefactor; hence, conditional on `P=Q` and on a self-adjoint boost generating a local invariant-domain flow, no boost can complete that fixed Hamiltonian to the Poincare algebra, so its three-particle sector must be changed by a connected three-body correction (the 4% figure is specific to the submitted normalization, not universal).  Given the additional H-P branch assumption, the nontrivial 1+1 law is instant-form, and standard Sokolov packing supplies a formal continuum route to exact Poincare covariance plus cluster separability.  However, the formal packed recipe was not instantiated as a complete lattice operator or numerically checked, compact-domain invariance and faster-than-power tails remain unproved, and the single packing-operator data establish only steep packet-dependent decay—not an `exp(-0.8 sqrt(r))` asymptotic.  Therefore R7-6 is **INCONCLUSIVE** under the fixed reading.
