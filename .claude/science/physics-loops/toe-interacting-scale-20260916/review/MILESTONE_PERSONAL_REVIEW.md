# Personal review of the joint-limit proposal

2026-09-16 UTC. Same-author review under the user's explicit instruction to
work personally without subagents. No independent acceptance is asserted.
Science baseline and refreshed origin/main:
`e0ef7cf4633034a8c1e6d57f5812cc4275bf1349`.
Planning/instruction revision: `068e916ca37b004757ad3a3c082857a91dc37215`.

## Scientific disposition

The packet contains a connected provisional model derivation, from uniform
compact-field control through the joint equal-time state to gauge two-point
and bounded neutral matter dynamics. Every scoped argument is included in
the proposed tree. The prior campaign is a source of questions and method
history, not an uncarried theorem dependency. The six final notes and their
linked proof obligations were personally examined; the individual reviews
record consequential checks and corrections.

The main restriction discovered during the work is that the free-state
conclusions require the quadratic paired Wilson matter Hamiltonian without
an extra fixed onsite charge interaction. The first compact-field lemma
allows that interaction, but its broader scope is not silently inherited.
All later notes maintain the restricted model, exact Gauss law, positive
fixed weights, specified filling and full ground-space trace.

The energy comparison is uniform in volume and does not use an inverse
finite-volume gap. Its trial is only variational, not identified with the
ground state. Compact defects remain positive terms. The Fourier dual
estimate controls pressure per volume, not a total partition function near
one. The field characteristic proof controls intervening translated states.
Matter identification treats isolated zero modes through the bounded CAR
covariance, without assuming finite-box uniqueness. Propagation uses norm
generator residuals, not energy-form convergence. The nonlocal polar
multiplier is handled by Fourier positivity and approximation; the summable
kernel theorem applies to Omega alone.

The strongest proposed gain is arbitrary joint g->0,L->infinity local
convergence with the stated finite-time extensions. This remains weaker
than a fixed-positive-g infrared construction. No particle pole at fixed g,
full nonlinear gauge evolution, finite-qubit payload, empirical prediction,
selected Hamiltonian, or axiom update is established.

## Selective check map

| Active program | Different representation / discriminating check |
|---|---|
| [Compact-field/response challenge](../evidence/block01_uniform_response_check.py) | Direct/dual integer Gaussian sums; literal CAR link spectrum; sparse cubic curl; explicit spectral decomposition and degenerate-ground counterexample |
| [Integer Gaussian and square identity](../evidence/block02_integer_gaussian_square_check.py) | Smith invariants; direct weighted spectral inverse; Fourier-core operator identity; parity-inserted dual overlap; hard-boundary discrepancy retained |
| [Tree and Slater challenge](../evidence/block02_tree_slater_check.py) | Literal paths/plaquette fills and charged Fock matrix energies; determinant fidelity curvature versus charge variance |
| [Characteristic challenge](../evidence/block03_characteristic_check.py) | Directional differentiation of differential-operator coefficients; position/Fourier covariance; direct rotor exponential versus characteristic Duhamel formula |
| [Weyl and zero-mode challenge](../evidence/block04_weyl_zero_mode_check.py) | Direct rotor exponentials on ground and excited vectors; finite zero-mode choices with equal energy but different global covariance; equal nonprojection covariance with different fourth moments |
| [Generator and propagation challenge](../evidence/block05_generator_propagation_check.py) | Actual charged Gauss/CAR matrix current; norm residual and time evolution; square-root formula versus spectral diagonalization; explicit two-mode first-moment comparison |
| [Rooted matter challenge](../evidence/block06_rooted_matter_check.py) | Rooted CAR map versus flux-shifting closing link; electric path commutator including its quadratic term; bounded-matter Duhamel comparison and reversed-time discriminator |

The [mutation record](milestone_mutation_checks.json) contains28 explicitly
perturbed temporary programs, all returning nonzero at the intended
mathematical assertion. Families cover Gaussian normalization/signs, Fock
norms, curl geometry, spectral moments, integer boundaries, weighted metrics,
positive squares, tree flows, Slater curvature, field commutators, Fourier
normalization, Duhamel coefficients, Weyl phases, zero-mode filling, purity
premises, currents, generator residuals, square-root projections, toy-mode
coupling, root electric terms, closing-link orientation and time direction.
The same-source harness is a robustness check, not independent physics
review. Analytic derivations and the differing mathematical representations
above supply the separate calculation paths.

Final packaging added timeout/input declarations and concise stdout to the
active programs, without changing their mathematical checks. All seven were
re-executed and their helper/source hashes refreshed. The two unexpected
earlier failures and their original source/traceback hashes were preserved
unchanged. Successful raw runs are not labelled audit caches. No baseline
or threshold was fitted to a desired physical value.

## Applicable conformance and explicit deferrals

The complete PR conformance spec and the physics-claim-reviewer skill were
read. Applicable source-level requirements were checked: self-contained
premises, full-surface provisional scope, proof graph and domains, meaningful
mathematical checks, deliberate perturbation rejection, helper provenance,
source/output matching, tracked-file links, vocabulary, syntax and diff
hygiene. The final manifest binds the proposed packet's bytes.

This draft adds an exploratory research packet under `.claude/science/`,
not registered source notes or retained-grade claim rows. It changes no
citation/dependency extraction policy, audit ledger, effective-status data,
claim/helper registry, prompts, skills, axioms or primitives. Formal note
registration, restricted audit packet/helper mapping, cached execution and
the integrated main-landing pipeline are deferred to an authorized promotion
path. They have not been simulated or represented as completed. The draft
is available for mathematical review, not an instruction to merge or audit.

Constructed counterexamples and numerical boundary failures are preserved
as explicitly scoped witnesses. No exhausted-route, model-wide no-go or
forced-axiom-update conclusion is shipped, so the packet does not purport
to satisfy a broad negative-claim gate by inventing untested alternatives.

No source note claims that a passing program establishes the thermodynamic
theorem. The remaining material verification limit is independent scrutiny
of the complete analytic chain. Personal review and mechanical conformance
do not supply that independence.
