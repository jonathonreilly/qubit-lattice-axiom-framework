# Twelve-hour campaign: mobile records, renewed formation and the TOE

Research window: 2026-09-20 23:32:19 UTC to 2026-09-21 11:32:19 UTC.
Status: completed. The twelve-hour research window has ended and the campaign
heartbeat is paused. Final recovery packaging followed the fixed deadline.

My assessment is that this is a promising direction for investigating
mechanisms, but the present evidence does not establish a compelling theory
of everything. The campaign produced concrete local models, conditional
mathematical results, finite-size evidence and sharper tests of what remains
missing. It did not derive quantum field theory, gravity, matter or measured
constants from the axioms. Publication count and passing scripts are not
measures of progress toward that physical conclusion.

I personally chose the research directions, derived the constructions,
implemented the calculations and simulations, and assembled the publications.
One separate-context checker was used at consequential milestones. Its
reports distinguish independent reconstruction from subsequent comparison
with my code. The physics-loop/workhorse production workflow was not used.

## What changed in the scientific picture

**Motion really changes the formation question, but does not create unlimited
capacity.** A site can form a record, lose it through transport, and form
another. Under translation-invariant conservative bounded finite-range transport, no removal or
site creation, however, the expected total number of births at a fixed site
is its initial vacancy probability minus its limiting vacancy probability,
at most one. Individual sites can form repeatedly while others do not.
Uniformly positive formation hazards eventually fill finite volume. Allowing
occupied records to exchange keeps motion active after filling; vacancy-only
hopping does not provide the same escape. These statements have different
hypotheses and are not a universal ban on continuing physics.

**Unchanged records can support waves under supplied local rates.** Explicit
finite-range context exchanges preserve record contents, have positive rate
floors, and leave homogeneous products invariant. Their exact currents
support conditional acoustic and transverse curl limits. In the fifteen-state
vector example the full fourteen-field tangent has four propagating modes
and ten zero speeds at nonzero wave number and nonzero coupling. Formation
and fluctuation statements retain their own assumptions. A Maxwell-shaped
classical linear equation is not yet physical electromagnetism.

**The selection problem is now precise.** At the fully uniform fifteen-state
product, even the stronger 48-element polar/axial cubic symmetry and positive
entropy metric permit five independent first-order couplings. With only the
proper 24-element symmetry the dimension is eleven. Every member of the
five-dimensional family has a local positive whole-record realization.
Time reversal of the specified kind permits all five. Requiring preservation
of both raw-vector Gauss constraints for arbitrary remaining moments selects
the curl member. Derivative curl observables need a weaker condition and can
coexist with a longitudinal sound sector. The required constraint or closure
principle is an additional premise, not something the axioms currently select. A final
local extension supplies all eleven proper-cubic maps explicitly. It finds
that conditional closed-vector curl selection survives without spatial
reflections, while a separate nonvector sector can remain active. That
extension has its own review boundary and is outside the frozen PR 8569.

**The state matters as much as the wave equation.** Native interacting
formation creates correlations immediately; its finite-coupling law cannot
be replaced by an exact product. Controlled perturbative statements are
available, but the native finite-coupling fluctuation limit remains open.
In an explicitly ordered late-time/product limit, local curl readouts of
bounded raw fluctuations have quadratic low-wave-number power. That does
not supply a quantum vacuum. Interchanging long-time and large-volume
limits or changing the initial law would require a new argument.

**There is a plausible classical correlation route worth testing.** Exact
Gauss-preserving immutable loop moves and a constrained equilibrium ensemble
were constructed. A dilute regime has controlled short-range correlations.
At fugacity one, the separate auxiliary equilibrium sampler shows nearly
flat low-mode power through L=49 and approximate agreement between winding
variance and local spectral amplitude. This is a finite-size numerical
signal, not a proved phase or a physical formation-selected state. High
fugacity trapping, dependence between blocks, the small number of effective
blocks at L49, and one narrowly discrepant winding interval are all retained.
The complete [screen report](GAUSS_WORM_COMPLETED_SCREEN_REPORT.md) contains
the favorable and unfavorable cases and exact verification boundaries.

**Classical, quantum and measurement claims remain distinct.** The original
fourteen-label formation table fails a specified fixed-qubit communication
interface; larger-dimensional constructions and a modified one-event Born
kernel can be supplied under explicit assumptions. They do not establish
coherent repeated histories, a physical quantum carrier or a vacuum state.
Flat constrained-field spectra and zero-temperature photon spectra also
differ in established quantum-spin-ice models; this comparison is a diagnostic,
not a mapping of our record model to those systems. See
[Benton, Sikora and Shannon](https://arxiv.org/pdf/1204.1325v2).

**Correlations and transport are compatible in principle, but the desired
three-dimensional synthesis is still missing.** Local whole-record
circulations preserve supplied Gibbs weights; a separate established
one-dimensional KLS construction has correlated Gibbs weights and nonzero
transport. The first construction's contractible local cycle current and
the second construction's directional winding current cannot be conflated.
Neither supplies the joint three-dimensional state and wave theory we need.

## Reviewable milestones

Every PR below is a draft. No main merge or independent audit verdict was
applied. The PRs contain their own hypotheses, exact source identities,
reproduction evidence and limitations. Some are stacked and require their
listed parent. Combined pipeline, strict audit lint, negative-claim schema
and changed-evidence integration remain pending before landing.

| Draft PR | Result | Dependency |
|---|---|---|
|[8545](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8545)|Mobile formation law and spatial response|main|
|[8551](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8551)|Empty-start formation controls|8545|
|[8552](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8552)|Lifetime activity, filling and terminal correlations|8545|
|[8557](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8557)|Immutable acoustic context exchanges and limits|main|
|[8560](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8560)|Transverse curl sector and formation fluctuations|8557|
|[8561](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8561)|Native formation Euler law and separate cubic centering|8557|
|[8565](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8565)|Gauss loops, static dilute regime and formation locality|main|
|[8566](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8566)|Local curl readout, quantum interface and modified Born formation|8560|
|[8567](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8567)|Local Gibbs circulations and winding-transport countercontrol|main|
|[8569](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8569)|Cubic symbol classification and conditional Gauss selection|8560|

The numerical Gauss screens, staggered-sector analysis and general Gram-kernel
response calculation are also preserved locally. Their statuses differ:
the sampler/operator arguments received a separate check; the adaptive
winding diagnostic subsequently received its own separate benchmark and
compact-arithmetic check; the general Gram-response calculation remains
author-checked only. The eleven-map extension also received a separate exact check, including
simultaneous coefficient cancellation and the longitudinal readout kernel.
Its report is `proper_cubic_extension_independent/REPORT.md`. Review coverage
is not transferred between these results.

## The next highest-leverage work

1. Construct and test **one local physical process** that simultaneously
   preserves immutable contents and the intended Gauss constraints, supports
   transverse propagation, and selects the required correlated state. The
   current examples establish these properties in partly different models.
2. Supply a justified reason for the vector sector's closure or a controlled
   account of its coupling to the other conserved moments. The new exact
   classification makes this a finite set of explicit obligations.
3. Resolve the constrained ensemble's infrared behavior with mixing-aware
   large-volume evidence or a theorem, including angular and parity-sector
   structure. Then show whether physical formation reaches the relevant
   ensemble and winding sector.
4. Establish coherent quantum dynamics and the operational meaning of the
   records, beyond a single conditional probability table. A successful
   classical constrained wave model alone does not meet this obligation.

I would prioritize the joint-process/constraint problem over further tuning
of a toy wave speed. It directly tests whether the most promising pieces
can belong to the same physics.

## Recovery and verification limits

Raw worktree:
`/Users/jonreilly/Documents/Codex/mobile-record-formation-20260920`.
The current recovery state is recorded in the parent `CHECKPOINT.md` and its
source-identity manifest. The raw research branch stays local because it
contains third-party references and experimental artifacts. Approximately
5.30 GB of raw CSVs remain on disk, outside Git, with complete recorded
SHA-256 identities. Publication worktrees contain selected portable evidence.

The synchronized main source was 5d784d8ccda5268f2b7c056fcdf0d81fdb703319.
Relevant external PR arguments were read at pinned revisions; their runners
were not all independently reproduced. The exact external read boundary is
in the synchronization workspace. No editable prompt, primitive registry,
platform instruction or audit verdict was changed. The campaign's own heartbeat was paused at 11:32:27 UTC after the fixed end
time. No research extension was taken. Final local recovery identities are in
`RECOVERY_20260921_FINAL_SOURCE_IDENTITIES.json`; the completion receipt is
`CAMPAIGN_COMPLETION.json`.
