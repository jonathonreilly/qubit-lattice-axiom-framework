---
claim_id: exact_terminal_counts_on_seven_site_path_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated limits; numerical controls do not establish physical selection or extend the analytic quantifiers."
upstream_dependencies:
  - minimal_axioms
  - formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24
runner: scripts/exact_terminal_counts_on_seven_site_path_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical result; unaudited.

The complete source argument and its selected companion proofs follow, with the narrow corrections documented in the combined review. Dated author-status statements, seals and numerical observations are historical provenance, not audit authority. Quantum spaces, Hamiltonians, instruments, preparations and resource assumptions are supplied mathematical premises. Fresh controls corroborate the proofs within their scope.

# Exact terminal formation counts on the seven-site path

Root analytic result, September 23, 2026. This is a theorem about the
**supplied compensated rotor target** on one finite physical path, with the
actual hop-then-formation channels. It extends the sealed independent
seven-site reconstruction in `formation_capacity_independent/REPORT.md`.
The independent packet established a first-mark branch of weight one third
into a stationary one-birth state; it did not determine the other histories.
The calculation below closes their terminal **counts** for this path.

## Model and physical sector

Take sites 0,...,6 with A={1,3,5}, B={0,2,4,6}, all six nearest-neighbor
edges, and integer electric links satisfying div E=q-1_A. Initially every
A site has charge +1, every B site is empty, and E=0. Use the compensated
target Hamiltonian

    H=K D+delta H4,  H4=-2 sum_(a<c sharing B) S_ac^*S_ac,

and either actual instrument: two resolved sign channels per edge or their
coherent sum on each edge, both with the stipulated sqrt(kappa) amplitude.
Assume K>0, delta>=0, kappa>0. The source matrices span the entire
52-dimensional physical space, with N sectors 3:1, 5:30, 7:21.
On this tree Gauss law fixes a unique integer field for each charge word.

Write Omega for the initial basis vector and Gamma=sum L_mu^*L_mu. The
source and separate reconstruction give

    D Omega=0, H4 Omega=-12 Omega, Gamma Omega=12 kappa Omega.

Hence the first birth occurs almost surely with survival
`exp(-12 kappa t)`. Conditioning on that birth, the channel weights are
time independent. The twelve resolved first vectors each have squared norm
one before the common kappa factor; the six coherent edge vectors each
have squared norm two. Total weight is twelve in either convention.

## The decisive source identities

The four resolved first vectors anchored at middle site 3, or the two
coherent middle-edge vectors, have total squared norm four and obey

    D v=0, H4 v=0, Gamma v=0.                         (1)

They remain in N=5 forever. Their two B vacancies are endpoints 0 and 6,
so a second formation is geometrically unavailable.

Each of the eight endpoint-anchored resolved vectors, or four coherent
endpoint-edge vectors, has positive-loss eigenvalue

    Gamma v=4 kappa v.                               (2)

Their combined first weight is eight. Equations (1)-(2) hold for the
**full channel vectors** in the physical Gauss space, including coherent
sign superpositions. The calculation enumerates all first channels and
the full physical N=5 sector; it does not replace actual output by an
incoherent matter-only pattern. The separate rotor-path implementation
reconstructs all 52 Gauss words, first vectors and adjoint jump actions,
then matches every first channel to the sealed independent PRE matrix.

## Why endpoint histories eventually form again

In N=5 set `H5=K D5+delta H4_5` and let M be the largest H5-invariant
subspace of ker Gamma5. Because H5 and Gamma5 are selfadjoint, M reduces
both operators. On M the no-event propagator
`exp[t(-i H5-Gamma5/2)]` is unitary. On its orthogonal complement it
decays in finite dimension: an imaginary-axis eigenvector of its generator
would have zero loss by the norm derivative, hence would be an H5
eigenvector in ker Gamma5 and belong to M; contraction forbids a nontrivial
Jordan block on the imaginary axis. Thus the probability of never seeing a
second birth from v is exactly `||P_M v||^2/||v||^2`.

Equation (2) places every endpoint first vector in a positive-eigenvalue
subspace of Gamma5, orthogonal to ker Gamma5 and therefore to M. Its
no-second-birth probability is zero, whatever K and delta do to the
waiting-time law. Equation (1) places every middle first vector in M.
There can be at most two births, because each adds two records and the
seven-site path holds at most seven. Therefore, for **both** actual
instrument conventions,

    Pr(J_infinity=0)=0,
    Pr(J_infinity=1)=1/3,
    Pr(J_infinity=2)=2/3,                            (3)

for every K>0, delta>=0 and kappa>0 in this finite target. The final
expected birth count is 5/3 and final expected record number is 19/3.
The count limit exists even if dark Hamiltonian coherences keep a density
from converging. Equation (3) asserts no universal second waiting-time
distribution and no infinite-lattice terminal count law.

## Exact controls and scope

The personal exact Krylov calculation in
`terminal_path_exact.py` first found one-third for
K/delta=0,1/3,1,2,5 and the delta=0 edge cases, for both instruments.
These parameter samples suggested (2) but do not prove generality.
The decisive `terminal_path_structural_check.py` then verified
Gamma eigenvalues zero or four on all first vectors using the root
rotor-path builder, with exact integer arithmetic and Gauss shifts; it
also matched every vector to the frozen independent 52-state matrix.
Both logged portable runs succeeded; their exact outputs, receipts and
scripts are adjacent to this note. The original research runs are also
preserved under the external campaign calculation directory. The portable
scripts find their input matrices relative to this publication unit and can
be rerun without the author's private checkout.

The independent checker who authored the PRE matrix later hit a usage limit
before writing its post-author comparison narrative. Its sealed PRE result
is still an independently constructed source. The structural proof after
PRE and its parameter-free interpretation are root work. A completed
independent post-result review of (3) is not claimed.

This conditional finite-path result shows both a real second formation and
a real unsaturated trap from the stipulated initial state. It does not
derive the compensation, formation instrument, energy source or lattice
from the native framework; it does not predict a measured particle or TOE
phenomenon. It also does not prove the same proportions on cyclic, cubic or
infinite sectors.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** the specified graph, sector, input, observable and order of limits.
- **N2 — Alternatives:** other models, initial states, instruments and resource scalings remain possible.
- **N3 — Imports:** supplied quantum and probability structures are mathematical assumptions, not new repository axioms.
- **N4 — Dependencies:** companion results retain their hypotheses; no retained grade is imported.
- **N5 — Evidence:** exact finite controls and fresh numerical diagnostics corroborate the argument; floating computations are not interval enclosures.
- **N6 — Resolution:** density convergence, energy convergence, initial power, finite time and volume limits are distinct statements.
- **N7 — Remaining work:** native selection, physical implementation and empirical identification remain separate obligations.
- **N8 — Authority:** no audit verdict or retained-grade promotion is applied.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary; it does not derive the supplied model.
- [formation_balance_and_unsaturated_dark_states_bounded_theorem_note_2026-09-24](FORMATION_BALANCE_AND_UNSATURATED_DARK_STATES_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional companion source within its stated hypotheses.

## Source and verification

Source PR #8865, frozen head `79ab61e5aee8945bf96924815c7e0f9dd4d256a5`. Original source dispositions and recovery branches are recorded in the combined receipt. Review uses the same primary session without subagents; no separate fix reviewer or formal audit is claimed.

```bash
python3 scripts/exact_terminal_counts_on_seven_site_path_2026_09_24.py
```

Fresh controls execute in a temporary directory. Full scientific stdout and generated JSON are included in the authenticated result. Historical diagnostics and deferred source remain recoverable from the original branch.
