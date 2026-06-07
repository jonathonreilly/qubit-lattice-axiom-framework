# Math Sector Search

## Two-State Resolution Model

Finite states: `+` and `-`.

- Blend: `(1/2, 1/2)` has signed excess `0`.
- Symmetric flip: a two-state Markov transfer with equal rates has unbiased
  fixed point `(1/2, 1/2)`.
- Symmetric sink: reduces retained mass but preserves signed excess.
- Asymmetric sink: enriches the unsunk hand.
- Dynamic kinetic resolution: flip plus asymmetric sink enriches one hand, but
  the sink is the load-bearing selector.

Checked by:
`scripts/frontier_chirality_resolution_dynamics_scout_2026_06_07.py`

## Staggered One-Bond Model

Finite assignments: `gamma5 = diag(w_A, w_B)`, `w_i in {+1,-1}`.

- Without `{D,gamma5}=0`, trivial/vector-like and staggered/chiral classes both
  survive.
- With `{D,gamma5}=0`, only opposite signs survive, one class up to global sign.

This aligns with the existing staggered selector enumerator and identifies
anticommutation as the filter in the one-link matrix model.

## Orientation Torsor Model

An orientation line can host two sections.  The desired odd source vector appears
after one section is chosen, but the opposite section remains equally coherent
without a source-section theorem.

## Record Consumer Model

Record append preserves the carrier distribution and stores observed labels.  It
does not create the carrier chirality.

## Signed Readout Guardrail

A toy signed C3 readout can commute with the C3 labels.  Such a readout is a
classifier, not automatically an anticommuting chirality.
