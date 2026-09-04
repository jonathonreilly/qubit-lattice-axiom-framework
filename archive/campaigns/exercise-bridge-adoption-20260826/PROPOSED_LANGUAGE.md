# The proposed Bridge axiom language (supervisor draft, 2026-08-26 — PROPOSAL ONLY)

### Bridge / Statistical Readout

For every record-compatible class of the committed action class, the class weight equals
the limiting relative frequency of that class's record in the history index.

The class weight is the normalized read-slice Gram weight as landed:
W(S) = Sum_{a in S} G*[a,a] / Sum_b G*[b,b], where G* is the symmetrized read-slice Gram
of the committed action at the read slice of the record configuration, and S ranges over
the landed record-compatible classes (class_projectors, singleton and coarse).

Joint weights of simultaneous same-slice records are the one-shot joint weights. (This
resolves the block-171 fork by its measurement: the one-shot form is exactly
order-independent; the per-slot form carries a nonzero measured defect and is excluded.)

No admissible frame function is privileged by derivation. The Bridge is a selection:
additivity on the record lattice admits non-Gram frame valuations (the landed eps_p
norm-parity family, p = 7, 11, 5 at the measured points), and this axiom selects the
Gram weight against them by supply, not by proof.

Scope: the committed action class and its landed record structure; the site and CM-SITE
alphabets as landed. Extension beyond them is by construction only, never by assertion.

This axiom does not grant: a probability measure, sigma-additivity, or any continuum
limit-taking apparatus; a state, state-selection rule, typicality or genericity
assumption (the realized_state_primitive boundary is unchanged); any retroactive change
to the landed non-supply verdicts, which stand as the reason this axiom exists; any
joint-weight form beyond the one-shot writing; and no empirical content beyond the
stated weight-frequency equality.
