# Goal

Build a branch-local dynamics bridge from the explicit finite
pointer-non-demolition record-formation model to the normalized
record-writing isometry `W` assumed by the finite Kraus instrument algebra.

The useful target is narrow:

```text
stable finite pointer projectors
  + orthonormal record labels
  + ideal pointer-label write
    => W|psi> = sum_r (P_r|psi>) tensor |r>
    => K_r = P_r Kraus instrument
```

The goal is not to derive arbitrary physical record production, a Hamiltonian,
a probability law, or a generation/Koide dial choice.

