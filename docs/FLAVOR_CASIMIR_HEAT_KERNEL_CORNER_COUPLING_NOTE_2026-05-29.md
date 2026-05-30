# Flavor — Casimir heat kernel gives r=tanh⁴(t); modulus relocated to the Casimir time

**Date:** 2026-05-29
**Claim type:** native-structure lead / honest characterization (NOT a
derivation, NOT a promotion). Import-free (the heat kernel on the corner cube is
the canonical Casimir object); identification with the generation mass matrix is
a **candidate**, not established.
**Runner:** `scripts/flavor_casimir_heat_kernel_corner_coupling_2026_05_29.py`
(+ cache). Follows the capstone
`FLAVOR_FERMION_VACUUM_NO_SELECTION_CAPSTONE_NOTE_2026-05-29.md`, which relocated
the origin of `b` to the action structure / a non-fermionic sector.

## The native object
The fermion vacuum will not generate the corner coupling `b` (three computations).
So look at the **Casimir-native action structure** directly. The canonical
Casimir object on the framework's `(Z₂)³` corner cube is the **heat kernel**
`K_t = e^{-tΔ}` on the cube graph Q₃ (the bare Laplacian `Δ` is the `t→0`
action; the heat kernel is its resolvent — no import).

On Q₃, `K_t(d) = ((1+u)/2)^{3-d}((1-u)/2)^d`, `u=e^{-2t}`, `d`=Hamming distance.
Restricting to the hw=1 generation triplet: diagonal `a=K_t(0)`, off-diagonal
(all pairs at `d=2`) `b=K_t(2)`. The induced Yukawa `Y=a I + b(J−I)` gives

```
Q = 1/3 + (2/3) r ,   r = (b/a)² ,   b/a = tanh²(t)   ⟹   r = tanh⁴(t).
```

## Finding — first native structure where r=½ is a clean interior point
- As `t` runs `0→∞`, `r = tanh⁴(t)` sweeps `(0,1)` — the **full Koide range** —
  from one clean native object. `r=½` (Q=2/3) appears at a specific interior
  point: `b/a = tanh²(t) = 2^{-1/2} = 1/√2 = 0.7071` (equivalently
  `tanh(t) = 2^{-1/4} = 0.8409`), at `t = 1.2242`. This contrasts sharply with
  the fermion vacuum, which drives `r→0`. *(Correction, verified to 1e-15: `b/a`
  is `1/√2`, matching the consolidation note; an earlier draft mislabeled it
  `2^{-1/4}`, which is `tanh(t)`, not `b/a`. `r=½`, Q=2/3 unaffected.)*
- **But it is not a derivation.** The heat-kernel time `t` is a free modulus;
  `r=½` just re-expresses the unforced ratio `b/a` as an unforced `t`. The naive
  `t=1` (Casimir time `∼ g_bare=1`) gives `Q=0.558`, **not** 2/3; no derived `t`
  lands on 1.224.

## Honest status
A clean native **characterization**, `r = tanh⁴(t)` — the simplest one-parameter
native form for the Koide ratio found in this campaign — but it **relocates the
single modulus from `b/a` to the Casimir time `t`**, it does not eliminate it.

Two things it does buy:
1. A concrete next question for the bridge-gap action: **what fixes `t`** (the
   Casimir proper time / the generation self-energy scale)? If the derived
   `g_bare=1` action sets `t`, the value follows; the naive `t=1` does not give
   2/3, so the answer (if 2/3) requires a non-naive `t`.
2. It confirms, from yet another native angle, that `r=½` is a **modulus**, not a
   dynamically-forced number — consistent with the campaign's measure /
   chiral-grading-input conclusion, now with the cleanest functional form.

**Caveat (load-bearing):** the identification of the generation mass matrix with
the cube heat kernel is a *candidate* — a position-cube object vs the
momentum-corner generations. So this is a **lead on the bridge-gap action**, not
a result about the leptons. No false closure; no claim that 2/3 is derived.
