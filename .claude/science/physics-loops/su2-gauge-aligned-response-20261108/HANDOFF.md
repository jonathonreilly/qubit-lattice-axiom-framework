# SU(2) gauge-aligned response: current research checkpoint

Date: 2026-11-08 (America/New_York). The original target in [GOAL.md](GOAL.md)
remains OPEN. This packet supplies bounded mathematics, not a continuum
Yang–Mills result or a formal retained-status decision.

Branch: `physics-loop/su2-gauge-aligned-response-20261108`.
Base and remotely rechecked main: `1e0d3b58dcda7f83152b0bb51729260247454d65`.
Historical draft #10133: `89faef229ff6e6bde42baad15ed8270c2f4087d8`.
The previous public author branch at `a50a62bf088b0e9fd2828e1c36f6237da71ccf99`
is preserved. No new remote publication or ancestry merge is part of this work.

## Bounded results

The quantitative domain is finite four-dimensional periodic SU(2), odd L>=3,
fine side N=L²m with m>=3, beta=u and both kernel strengths kappa u. Constants
depend on fixed L,kappa; none has been efficiently evaluated. This is a supplied
mathematical family, not a derived physical coupling flow.

| Proof | Result and limitation |
|---|---|
| [Compact forest](parts/compact-forest-exchange.md) | Exact shared-gauge Haar quotient and aligned replica exchange at arbitrary finite depth and terminal field. All source-only normalization and orbit covariance survive. Identity alone supplies no decay. |
| [Flat operator](parts/flat-two-step-bound.md) | Actual two-layer Hessian, volume-uniform slice gap, inverse decay, Schur complement and source determinant at terminal I. An auxiliary Gaussian bound, not a physical gap. |
| [Nonlinear chart](parts/nonlinear-chart-response.md) | Actual chart-conditioned covariance decay of order u^-1 and two-source/one-boundary response for C1 tests with controlled gradients, at sufficiently large u and small terminal fields. |
| [Compact energy](parts/compact-energy-coercivity.md) | All-compact two-step energy controls every retained link's distance from I, uniformly in volume, at terminal I. Composes the prior one-step filling method. |
| [Rough density](parts/rough-density-bound.md) | Actual full compact terminal-I posterior: expected energy per cell O(1/u) and rough-cell probability O(1/u), with every radial normalizer retained. |
| [Local tail](parts/local-conditional-tail.md) | Exact normalized local conditional tail with explicit exterior cost, and fixed-event real-source/boundary fourth-cumulant estimate with coefficient 26. |
| [Relative energy](parts/local-relative-coercivity.md) | Small-collar stationary field with exponential boundary penetration and global compact coercivity about that field, for arbitrary local regions. Mean-zero singularities are handled by a global Lipschitz bound. |
| [Rough components](parts/rough-component-bound.md) | Full compact terminal-I component probability <=eta(u)^|S|, eta(u)=C exp(-c u delta²), for a specified finite-range component graph. Rooted size/diameter tails hold at sufficiently large u, uniformly in volume. |

All eight suppliers are checked in fresh context at the supervising
model/effort. [Initial report](gates/forest-flat-check.md) and
[six-source report](gates/final-scope-and-local-tail-check.md) preserve findings,
corrections and exact hashes. The [relative-energy/component report](gates/relative-component-check.md)
checks the new pair and reconciles the final metadata-only header changes.
This is same-provider mathematical checking, not independent-provider review,
formal audit or numerical certification.

## Remaining original target

Combine good-region response and rough-component insertions in the SAME
normalized integral, with summable connected supports. Retain complete reader
collars, local-mean response, source-only log Q and all kernel normalizers.
Disconnected exterior contributions must cancel before summation. Even a
verified small component probability does not give a connected logarithm norm
or covariance decay between distant sources.

For invariant scalar sources at terminal I, the one-boundary coefficient vanishes
by conjugation symmetry. The next nontrivial test is the distinct-link
two-source/two-boundary fourth cumulant specified in [GOAL.md](GOAL.md), including
its correct coupling scaling and eventual complete log Q subtraction. A repeated
boundary link additionally requires the derivative-of-score term.

Compact quantitative bounds here concern terminal I; arbitrary terminal fields,
uniform depth, physical-scale/cutoff control, continuum reconstruction and the
mass gap remain open. The fixed-chart response has its separate small-terminal-
field domain. No intermediate layer is treated as a new Wilson law.

## Failed extensions and scope guards

- An initial arbitrary-bounded-test claim was false: a fixed sign test can have
  boundary response of order sqrt(u). The corrected chart theorem requires C1
  tests with controlled gradients; the independent report preserves the example.
- Gauge-variant original sources cannot be replaced by separate orbit means.
  A tree-link trace retains Haar variance 1/4 even at large u.
- The event that the whole volume is in one small chart becomes rare at fixed
  finite u. The full covariance retains both sectors and their between-sector term.
- Global partition comparisons give a rough-event bound with a loss proportional
  to total volume. That loss cannot simply be replaced by component size.
- The identity-centered local cap retains an exterior cost. Ordinary good exterior
  does not automatically absorb it. The checked relative-energy argument cancels
  the common stationary baseline and prices actual rough components using their
  exterior-event inclusion. This is a separate proof, not a correction to the old cap.

## Reuse, execution and recovery

[SOURCE_MAP.md](SOURCE_MAP.md) records exact premise matching and prior-work credit.
Luna supplied targeted inventories. The supervisor read the original definitions
and the relevant compact, conditional, inherited-chart and stationary arguments.
Search nonmatches are not absence theorems.

Root retained the selected model/effort for frontier derivation and decisions.
User-authorized medium-effort workers wrote bounded proofs in isolated managed
worktrees. The fresh-context checker independently reconstructed twisted closed
forms, the compact-to-flat gap implication, source cumulants and the global
stationary perturbation argument. Role separation alone confers no correctness.

Main preflight passed. No numerical job, new runner, pipeline, publication or
formal audit ran in this block. Vocabulary checking of the packet found
no violations. No editable prompt, axiom, workflow or platform instruction changed.
Only this research packet is added on the author branch.

Next science: prove the connected full compact two-source/two-boundary response
using these suppliers, without replacing event probabilities by a connected
logarithm norm. Exact source identities and final check hashes are in
[manifest.json](manifest.json). Worker worktrees can be recovered from their
managed archives; current proof sources and all reports are in this packet.
