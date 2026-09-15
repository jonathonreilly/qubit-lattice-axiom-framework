# Extended personal TOE campaign

The extended window ran from September 14, 2026 at 9:30:44 a.m. Eastern to
September 15 at 9:30:44 a.m. Eastern. The full extended window is complete, including the additional twelve hours.
I ran the campaign personally, without subagents.

There is promising progress, chiefly in deriving a coherent mathematical
model of fields and charge. There is still no completed TOE or demonstrated
contradiction that forces an axiom update.

The most concrete late result is a consistent quantum-style energy and time
evolution for the supplied lattice gauge model. The proposed derivation now
handles sequences of field operations, gives the same lowest external-charge
energy regardless of the path or finite history used to prepare it, and puts
that energy strictly above zero for nonzero external charge. Under additional
assumptions it also stays bounded as a test-charge pair is separated. These
statements concern the chosen model. They do not yet derive moving electrons,
an exact Coulomb force, or measured particle masses.

The earlier campaign also developed a proposed Maxwell/Gaussian field limit
for the continuous-angle version of the model. The finite-clock version has
stronger two-point and spectral results, but its full field distribution at a
fixed finite clock size is still an open proof task. Keeping that distinction
clear matters: a promising approximation is not the full desired theorem.

On the native-rule side, a concrete local matrix rule can carry out arbitrary
finite sequences of prepared one-qubit projective measurements and leave stable
records. The probability rule and preparation are supplied in that construction.
It shows a workable mechanism; it does not establish why the axioms select
Born's rule or that preparation.

Most of the useful gains came from derivations. Computation served to challenge
signs, normalizations, charge assignments and limiting formulas. Failed attempts
and deliberately broken formulas are preserved alongside successful checks.
Independent review remains necessary before relying on these proposals; repository checks
and my own finite calculations do not provide that verdict.

The next most valuable mathematical target is the full fixed-clock field law
with both defect sectors controlled. Other substantial targets are native
selection of the dynamics and calibrated quantum rule, and a genuine model of
moving charged matter. The failed estimates in this campaign do not establish
that any of those targets requires new axioms.

Reviewable milestones:

- [Coupled clock defects and exact source bounds, PR #8133](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8133).
- [Continuous-angle Maxwell limit proposal, PR #8134](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8134).
- [Matched free state and static-charge bound, PR #8140](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8140).
- [Prepared local projective histories, PR #8143](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8143).
- [Common static-charge Hamiltonian, PR #8144](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8144).
- [Field histories and positive charge-energy bounds, PR #8145](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/pull/8145).

The exact public dependencies are pinned in each proposal. The private campaign
branch is `physics-loop/toe-phase-selection-20260914`. Its science, failed probes,
reading records and retrospective remain recoverable after scratch checkouts
are removed. No axioms, primitives or editable prompt files were changed.
No author science was merged to main by this campaign, and no audit verdict
was applied. The recovery receipt records the final pushed head and checkout cleanup.
