# Handoff

This PR repairs
`staggered_scalar_parity_lapse_coupling_external_narrow_theorem_note_2026-05-16`.

The prior audit blocker was the unprovided external bridge proving that the
displayed parity/lapse forms are the literature-correct staggered scalar
couplings. The repair removes that load-bearing claim and preserves only the
exact algebra:

- epsilon alternation;
- parity diagonal hand checks;
- lapse Hermiticity;
- parity-vs-identity difference `Phi(x) * (epsilon(x) - 1)`;
- zero-`Phi` lapse reduction;
- well/hill ordering distinction on even and odd sites.

Independent audit should evaluate this as a bounded algebra certificate only.
