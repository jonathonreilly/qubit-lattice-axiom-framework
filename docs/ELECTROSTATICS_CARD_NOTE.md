# Electrostatics Card Note

**Type:** bounded_theorem

**Date:** 2026-04-05  
**Status:** conditional scalar electrostatic-like diagnostic on the supplied ordered 3D family; independent audit required

## Artifact chain

- [`scripts/electrostatics_card.py`](../scripts/electrostatics_card.py)
- [`logs/2026-04-05-electrostatics-card.txt`](../logs/2026-04-05-electrostatics-card.txt)

The source and coupling are supplied: `f=Σ q_source*5e-5/(r+0.1)` and
`S=L(1+q_test*f)`, on fixed transfer geometry/weights with a quadratic
`|amplitude|²` detector-centroid readout. Charge-product dependence enters
through these definitions. The printed signs/scaling are finite diagnostics
of this model, not a derivation of physical charge or Maxwell dynamics.
The harness reports its observations; exit zero and its unconditional SAFE READ
text are not fail-closed proof. The values below must be inspected directly.

## Question

Can the supplied ordered-lattice machinery support a review-safe
electrostatics-style sign law, without claiming full electromagnetism?

This card stays deliberately narrow:

- fixed 3D ordered lattice family
- scalar sign-coupled source field
- weak-field charged test packet
- one null control
- one dipole orientation check
- one charge-scaling fit
- one screening-shell attenuation check

It does **not** claim Maxwell equations, gauge structure, magnetic effects, or
radiation.

## Frozen Result

On the supplied ordered family:

- sign antisymmetry:
  - `(+1, +1)` gives `-1.68719246e-04`
  - `(+1, -1)` gives `+1.68715261e-04`
  - signed antisymmetry ratio: `-1.000`
- exact cancellation / null:
  - opposite-sign superposition at the same node gives `0.00000000e+00`
  - null verdict: `PASS`
- dipole directionality:
  - `(+ at +z)` gives `+3.32055668e-05`
  - `(+ at -z)` gives `-3.32313776e-05`
  - orientation flip ratio: `-0.999`
- charge scaling:
  - fitted `|delta| ~ q^1.000`
- screening:
  - bare `|delta| = 1.68719246e-04`
  - screened `|delta| = 3.10179509e-06`
  - screening ratio: `0.018`

## Safe Read

The narrow, review-safe statement is:

- the same ordered-lattice machinery can support an electrostatic-like scalar
  sign law
- like/unlike signed model parameters give opposite centroid shifts at the displayed fixtures; physical charge and force identification are not derived
- exact opposite-sign superposition cancels to printed precision
- dipole orientation flips the sign of the response
- the charge response is linear on the tested range
- a symmetric screening shell strongly attenuates the response

## What This Is Not

- It is not a derivation of full electromagnetism.
- It is not a vector-field theory.
- It is not a claim about magnetic or radiative effects.

## Final Verdict

**conditional electrostatic-like diagnostic; no audit status assigned**
