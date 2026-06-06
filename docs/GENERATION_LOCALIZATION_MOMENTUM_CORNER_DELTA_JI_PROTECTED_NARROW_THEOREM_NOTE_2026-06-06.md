# The Generation "Localization" is the Momentum-Corner Structure: the Emergent Coupling's `J − I` Form is Corner-Protected, its Sign Re-confirmed, and its Magnitude Reduces to the Mediator IR — Narrow Theorem

**Date:** 2026-06-06
**Claim type:** positive_theorem (corner-protection of the `J − I` form + sign cross-check; magnitude left open, reframed)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/generation_localization_corner_protected_delta_runner.py`](../scripts/generation_localization_corner_protected_delta_runner.py)
**Cached output:** [`logs/runner-cache/generation_localization_corner_protected_delta_runner.txt`](../logs/runner-cache/generation_localization_corner_protected_delta_runner.txt)

## Audit context

The interaction asymmetry `delta` (the two-excitation mutual energy that sources the emergent
`C3` coupling `|K|`) has its **sign** fixed negative by the retained two-body mediator (the
companion sign theorem). Its **magnitude** was reduced to the "generation-pair separation." This
note resolves that separation from the **retained** generation structure — and finds the picture
is not a spatial separation at all.

Retained inputs:
[`THREE_GENERATION_OBSERVABLE_THEOREM_NOTE`](THREE_GENERATION_OBSERVABLE_THEOREM_NOTE.md)
(`retained`),
[`THREE_GENERATION_STRUCTURE_NOTE`](THREE_GENERATION_STRUCTURE_NOTE.md) (`retained_bounded`),
[`THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10`](THREE_GENERATION_HW1_DISTINCT_TRANSLATION_CHARACTERS_NARROW_THEOREM_NOTE_2026-05-10.md)
(`retained`): the three generations are the `hw=1` Brillouin-zone corners
`k1=(π,0,0), k2=(0,π,0), k3=(0,0,π)`, distinguished by three distinct joint **translation
characters** under `(T_x, T_y, T_z)` — they carry **no spatial separation**. The mediator is the
retained
[`STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11`](STAGGERED_SELF_CONSISTENT_TWO_BODY_NOTE_2026-04-11.md)
(`retained_bounded`).

## Safe statement

Because the generations are momentum corners, `delta` is **not** a propagator evaluated at a
spatial separation; it is the two-fermion **mutual energy** of two corner excitations
interacting through the retained mediator `V(r) = −G (L + mu^2)^{-1}` (attractive). For two plane
waves `k_i, k_j` (a Slater determinant) with translation-invariant `V`, the mutual energy is
**exact**:
```
delta_ij = ( Vq(0) − Vq(k_i − k_j) ) / N ,     Vq(q) = −G/(eps(q) + mu^2),
eps(q) = sum_mu 2(1 − cos q_mu),               N = lattice volume.
```

**Theorem.**

1. **Distinct translation characters.** The three corners carry three distinct joint
   `(T_x, T_y, T_z)` sign characters `(−1,+1,+1), (+1,−1,+1), (+1,+1,−1)` — the retained
   "translations separate the generations."

2. **The `J − I` form is corner-symmetry-protected.** Every generation **pair** has the *same*
   inter-corner transfer `eps(k_i − k_j) = 8` (each pair differs by two `π`-flips). The exchange
   is therefore identical across all three pairs, so the second-order coupling keeps the **exact
   `C3` (`J − I`) form** — protected by cubic corner symmetry, not assumed.

3. **`delta < 0` — sign re-confirmed from the momentum picture.** The exact lattice two-fermion
   mutual energy matches the Hartree–Fock formula (verified `L = 4, 6`) and is **negative** for
   all three pairs (and equal across them). This re-confirms `delta < 0` **independently** of the
   spatial-packet route of the companion sign theorem.

4. **The magnitude reduces to the mediator IR, not the localization.** `|delta|` is dominated by
   the `q = 0` **monopole** (Hartree `≈ −G/(N mu^2)`); it scales with the lattice volume `N` and
   the IR parameter `mu^2`, **not** with any localization distance. The corner-dependent (Fock)
   part `≈ +G/(8N)` is subleading by `mu^2/8`. So the corner structure fixes the **form** and the
   **sign**; the **magnitude** is set by the mediator IR scale `(G, mu^2)` and the system size,
   and stays **open** — consistent with the wide-window robustness of the flavor pattern.

So the generation "localization" question resolves to the retained momentum-corner structure,
which protects the `J − I` form and re-confirms `delta < 0`, while the magnitude is correctly an
**IR / mediator-scale** question rather than a localization one.

## The genuine open piece (and the route this opens)

The magnitude `|delta|` reduces to the mediator's IR monopole `G/mu^2` and the system size — it
is **not** pinned by the generation structure. So the open thread is the **IR completion** of
the mediator (the physical `mu^2`, `G`, and the effective volume/normalization), not a
localization distance. This is the same "actual emergent coupling" IR scale already named open;
the present result removes the localization degree of freedom from it and shows the wide-window
robustness frame is the correct one (the magnitude can range over the IR scale while the form and
sign are fixed).

## Boundary (honest)

- **Form + sign, not magnitude.** It proves the `J − I` corner-protection and re-confirms
  `delta < 0`; it does **not** pin `|delta|` (the magnitude is IR/volume-set, explicitly open).
- **Pure-corner idealization for the magnitude scaling.** The `1/(N mu^2)` scaling is for
  maximally-delocalized (exact translation-character) generations; a partially-localized
  completion would rescale the magnitude — another reason the magnitude is open. The **form** and
  **sign** results do not depend on this.
- **Periodic lattice for the exact plane-wave check.** Used so the momentum corners are exact
  eigenstates; the retained mediator's attraction (the sign) is boundary-independent. The
  `J − I` corner-protection (`eps(Δk) = 8` for all pairs) is a statement about the corner momenta
  and is boundary-independent.
- **No flavor value forced.** This fixes the **form** (`J − I`) and **sign** (`< 0`) of the `C3`
  coupling; it does not force `r`, `Q`, or any mixing value.

## Forbidden imports check

No new axiom and no new import. The momentum-corner generations and their translation characters
are **retained**; the mediator is **retained** (`retained_bounded`). The two-fermion mutual
energy (Hartree–Fock matrix element of the retained density–density interaction) is exact
arithmetic, cross-checked against exact finite-lattice diagonalization. The magnitude is named
open, not asserted.

## Runner check breakdown

Class A: (1) three distinct joint translation characters; (2) `eps(k_i − k_j) = 8` for all three
generation pairs (`J − I` corner-protection); (3) exact lattice two-fermion `delta` equals the
Hartree–Fock formula (`L = 4, 6`) and is `< 0` and equal for all pairs; (4) `|delta|` scales as
`1/N` (monopole-dominated) with the corner Fock part subleading by `mu^2/8`. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content uses the retained momentum-corner generation structure and the retained
mediator to compute the two-fermion mutual energy `delta` exactly (Hartree–Fock matrix element,
cross-checked against finite-lattice diagonalization). The three corners' equal inter-transfer
`eps(Δk) = 8` protects the exact `J − I` form; the mutual energy is `delta < 0` for all pairs
(re-confirming the sign from the momentum side); and the magnitude is dominated by the `q = 0`
monopole, scaling with volume and `mu^2`, so it reduces to the mediator IR scale rather than a
localization distance. The result is a **form + sign** theorem with an explicitly open
(IR-set) magnitude; it forces no flavor value. Effective status remains `unaudited`.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/generation_localization_corner_protected_delta_runner.py
```
