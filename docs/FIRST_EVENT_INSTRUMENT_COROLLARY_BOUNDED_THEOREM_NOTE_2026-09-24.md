---
claim_id: first_event_instrument_corollary_bounded_theorem_note_2026-09-24
claim_type: bounded_theorem
claim_scope: "Conditional mathematics of the explicitly supplied finite model and stated ordered limits; historical numerical tables are author observations, with fresh controls separately identified below."
upstream_dependencies:
  - minimal_axioms
  - finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24
runner: scripts/first_event_instrument_corollary_2026_09_24.py
---

**Type:** bounded_theorem
**Status:** conditional mathematical construction; unaudited.

The complete source argument below is preserved from the frozen submission. Its dated author-status statements and historical execution tables describe that submission, not an independent audit verdict. Quantum laws, enlarged site/link memories, Hamiltonians, instruments, backgrounds and preparations are supplied mathematical model assumptions. They are not new repository axioms or framework primitives. Fresh execution of the canonical runner checks the stated finite controls; finite tests alone do not establish the general proofs or limits.

# Draft corollary: information at the first formation mark

Author derivation, independent review pending. This is a proposed corollary
of the unit-rotor initially vacant-B calculation; it is not added to a reviewed
publication unit. It uses the same supplied quantum model and retains every
post-event matter and field degree of freedom.

Fix a finite simple bipartite graph and a birth edge (a,b), a in A, b in B. Let z_a be the degree of a and
B_mu=-P j_mu T P restricted to P_v (all A plus, all B vacant). Distinct
allowed old-record destinations d in neighbors(a) excluding b have orthogonal
final matter occupations. Each rotor word on the links is unitary. For a
resolved charge mark mu there is one charge output per destination. Therefore

    B_mu^dagger B_mu = (z_a-1) I_(P_v).

For a coherent edge channel, the two charge outputs are orthogonal at a,
and its normalization is the unnormalized j_++j_- used throughout. Thus

    B_edge^dagger B_edge = 2(z_a-1) I_(P_v).

These are individual-channel identities, stronger than the previously
stated sum. Degree-one channels have zero rate and are excluded when dividing
by their coefficient c_mu. For c_mu>0, V_mu=B_mu/sqrt(c_mu) is an isometry
from the initial field sector into the full post-event matter/field space.
The rate of each first mark is kappa c_mu, independent of the initial field
state. Write r=kappa sum_mu c_mu. For r>0, first time and mark in the rotor
limit factor: time is exponential with rate r, and mark probability is
kappa c_mu/r. If r=0, no first event occurs in this limit and no normalized
first-mark distribution is defined. This statement
concerns these supplied instruments in the initially vacant-B sector only.
It gives no such occupation-only law after the first event.

When r>0, for a specified pre-event density rho, retaining the mark produces the joint
state with classical blocks p_mu V_mu rho V_mu^dagger. On the known image of
a mark, V_mu^dagger recovers rho. A trace-preserving mathematical recovery
on the whole marked output space can be obtained by sending the orthogonal
complement of each image to an arbitrary fixed density. Thus formation need
not destroy the quantum field information when the complete joint output
and its mark are retained. This is logical recoverability, not an authorized
physical reversal: the recovery need not respect permanent-record number or
be a local operation available in the model. Recoverability after partial-output, mark or time erasure requires its own
analysis. No loss of input recoverability from tracing matter alone is
asserted: with all links retained, the distinct charge branches can instead
be distinguished through their orthogonal field-divergence sectors. Recovering the
initial field rather than the immediately pre-event field also requires
undoing its known intervening Hamiltonian evolution.

No external time/mark register is derived from the native axioms here.
No claim about all-mark erasure correction, later births, thermodynamic
information capacity, finite resources or a physical measurement postulate
is implied. An independent check of the individual-channel identities and
an explicit cyclic-sector Gram calculation remain before publication. The
initial review found a missing r=0 qualification; its original note and seal
are preserved under first_event_instrument_history, and this revision makes
the positive-rate normalization condition explicit. A second review finding
removed an overbroad matter-erasure loss statement; its intermediate source
and seal are also preserved. Neither repair changes the individual-channel
Gram identities or the retained-mark full-output recovery map.


## Landing scope and No-Go Discipline Gate

- **N1 — Domain:** only the model, graph, sector, preparation, observables and order of limits explicitly specified above.
- **N2 — Alternatives:** other instruments, Hamiltonians, states and scaling paths are not excluded.
- **N3 — Imports:** supplied quantum and probabilistic structures are model assumptions; the native axioms do not select them.
- **N4 — Dependencies:** named companion arguments are used within their stated scope; no audit grade is inherited.
- **N5 — Evidence:** exact finite algebra and numerical stability controls corroborate the displayed proofs. Floating spectra and propagations are not interval enclosures. Historical tables are not independently certified by their presence here.
- **N6 — Resolution:** fixed-volume, uniform-volume and ordered-limit statements keep their distinct hypotheses; no exchange of limits is inferred.
- **N7 — Remaining work:** native selection, physical implementation, energy supply, preparation and empirical identification remain separate obligations except for explicitly proved model-specific results.
- **N8 — Authority:** this source applies no audit verdict, retained grade or assembly decision.

## Imports

- [minimal_axioms](MINIMAL_AXIOMS_2026-06-29.md): repository premise boundary only; it does not derive the supplied model.
- [finite_formation_with_retained_fourth_order_dynamics_bounded_theorem_note_2026-09-24](FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md): conditional argument only within its explicit hypotheses.

Finite-dimensional linear algebra, operator calculus and the explicit inequalities above are mathematical tools. Referenced literature is attribution or context unless its actual assumptions and use are stated in the argument.

## Source and verification

Source PR #8672, frozen head `fe6dc2c5ef061fa1e0051063d49178f23b872c13`. The primary review session uses no subagents; no separate fix reviewer or formal audit is claimed. Original auxiliary packets, failed attempts and historical seals remain recoverable on the original PR branch. The combined receipt records each original path disposition.

```bash
python3 scripts/first_event_instrument_corollary_2026_09_24.py
```

The canonical wrapper executes the selected scientific controls in a fresh temporary directory, retains their generated result JSON in its stdout, and ends with TOTAL. It does not execute historical sealing or approval instructions.
