# Neutrino Γ₁ W-source application bridge (narrow theorem)

**Date:** 2026-07-09

**Status:** source-side proposal — independent audit lane owns the verdict

**Type:** bounded_theorem

**Primary runner:** [`scripts/frontier_neutrino_gamma1_wsource_application_bridge_2026_07_09.py`](../scripts/frontier_neutrino_gamma1_wsource_application_bridge_2026_07_09.py)

**Cached output:** [`logs/runner-cache/frontier_neutrino_gamma1_wsource_application_bridge_2026_07_09.txt`](../logs/runner-cache/frontier_neutrino_gamma1_wsource_application_bridge_2026_07_09.txt)

## Claim

Given the two named premises P1 and P2, the following are exact theorems of
finite linear algebra on C^16:

- **P1 (family identification):** the C^16 Y/Γ₁ pair is the neutrino
  Higgs/source readout family. This is a readout-identification admission
  class.
- **P2 (comparator point):** the free comparator point is the scalar baseline
  `D = m I_16` on the declared block. This is a declared comparator choice,
  not derived from the observable-principle note.
- **T1 (selection):** `W[jY] = 0` identically in `j`, because
  `det(m I_16 + jY) = m^16` and `Y` is nilpotent. The W functional registers
  no response along the raw chiral bridge `Y` alone.
- **T2 (activation):** `W[jΓ₁] = 8 log|1 - j^2/m^2|`; equivalently,
  `spec(Γ₁) = {+1 (x8), -1 (x8)}`. The Hermitian completion is the
  direction W registers.
- **T3 (normalization as W-response):**
  `-m^2 W''(0)/16 = Tr(Γ₁† Γ₁)/16 = 1`. The weak-coupling per-mode
  trace normalization is the per-mode quadratic W-response coefficient at
  the declared comparator point.
- **T4 (chiral-half ratio):**
  `Tr(Y† Y)/Tr(Γ₁† Γ₁) = 1/2`; the HS-norm ratio is `1/sqrt(2)`.
- **T5 (additivity instance):**
  `W[j(Γ₁ ⊕ Γ₁)] = 2 W[jΓ₁]`. This instantiates the
  observable-principle additivity property
  `W[J_1 ⊕ J_2] = W[J_1] + W[J_2]`.

## Setup

The source definition in
[`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
is, verbatim:

> `W[J] = c(log det(D+J) - log det D)`, so that `W[0]=0`.

For the conventional `c = 1` representative it then states, verbatim:

> `W[J] = log |det(D+J)| - log |det D|`.

P2 fixes `D = m I_16` with `m > 0` on the declared block. This echoes that
the repaired packet
`DM_NEUTRINO_BOSONIC_NORMALIZATION_OBSERVABLE_PRINCIPLE_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
treats `mI`-determinant formulas as scalar-baseline diagnostics. The
comparator choice is a premise here.

The C^16 construction is copied from
`scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py`:

```python
    I2 = eye(2)
    SX = Matrix([[0, 1], [1, 0]])
    SZ = Matrix([[1, 0], [0, -1]])

    G0 = kron(SZ, SZ, SZ, SX)
    G1 = kron(SX, I2, I2, I2)
    G2 = kron(SZ, SX, I2, I2)
    G3 = kron(SZ, SZ, SX, I2)
    I16 = eye(16)

    GAMMA5 = G0 * G1 * G2 * G3
    # GAMMA5 is Hermitian and involutive and anticommutes with G0..G3.

    # Chiral projectors
    P_L = (I16 + GAMMA5) / 2
    P_R = (I16 - GAMMA5) / 2

    Y = P_R * G1 * P_L
    Y_dag = Y.H
```

Thus `gamma_5 = GAMMA5`, `Γ₁ = G1`, `Y = P_R Γ₁ P_L`, and
`Γ₁ = Y + Y†` on the declared block.

## Derivation sketch

Nilpotency gives `Y^2 = 0`, so every eigenvalue of `Y` is zero and
`det(m I_16 + jY) = m^16`. Therefore T1 follows from the baseline-subtracted
W definition.

The exact construction gives `{gamma_5, Γ₁} = 0` and `Γ₁^2 = I_16`.
Together with `Tr(Γ₁) = 0`, this yields
`spec(Γ₁) = {+1 (x8), -1 (x8)}` and hence
`det(m I_16 + jΓ₁) = (m^2 - j^2)^8`. Substitution into W gives T2
where the determinant is nonzero.

Twice differentiating at the origin gives
`d^2/dj^2 log|det(m I_16 + jΓ₁)| at j=0 = -Tr(Γ₁^2)/m^2 = -16/m^2`.
Since `Tr(Γ₁† Γ₁) = 16`, T3 follows. The exact traces
`Tr(Y† Y) = 8` and `Tr(Γ₁† Γ₁) = 16` give T4. Finally,
block-diagonal determinant factorization gives T5.

## Boundary / honest scope

- P1 is a readout-identification admission (register-not-read class); NOT
  derived here.
- P2 is a declared comparator choice; this note does not derive that the
  scalar baseline stands in for a real-D block.
- No physical `y_nu/g_weak` readout value is certified here.
- The Schur/Majorana/Z₃ activation content of the 2026-04-15 packet is NOT
  addressed by this bridge; this note supplies the W-application and
  normalization-response step only.
- No dynamics, no probability, no time content.

## Citation graph

- [`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md`](OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md)
  supplies the W functional and its additivity property.
- `DM_NEUTRINO_BOSONIC_NORMALIZATION_THEOREM_NOTE_2026-04-15.md` is packet
  context.
- `DM_NEUTRINO_BOSONIC_NORMALIZATION_OBSERVABLE_PRINCIPLE_BRIDGE_NARROW_THEOREM_NOTE_2026-05-16.md`
  is repaired-packet context.
- `scripts/audit_companion_dm_neutrino_bosonic_normalization_observable_principle_bridge_exact_2026_05_16.py`
  supplies the copied exact construction.

## Runner summary

- Group A checks the source needles, the premise labels, and markdown-link
  hygiene.
- Group B checks the exact C^16 construction: nilpotency, Hermitian
  completion, anticommutation, and both trace norms.
- Group C checks the determinant identities, the exact spectrum, a rational
  W instance, and block-diagonal additivity.
- Group D checks the exact quadratic response, independent finite-difference
  convergence, per-mode normalization, and the chiral-half ratio.
- Group E contains the matching REJECTOR controls: E1 detects that a
  non-nilpotent matrix-unit perturbation breaks selection; E2 detects the
  factor-four response of the rescaled source `2Γ₁`; E3 detects failure of
  the direct-sum identity for a cross-block coupled source.
