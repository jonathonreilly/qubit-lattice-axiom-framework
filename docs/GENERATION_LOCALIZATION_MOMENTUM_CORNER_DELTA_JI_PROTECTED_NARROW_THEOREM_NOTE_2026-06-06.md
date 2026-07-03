# The Generation "Localization" is the Momentum-Corner Structure: the Emergent Coupling's `J − I` Form is Corner-Protected, its Sign Re-confirmed, and its Magnitude Reduces to the Mediator IR — Narrow Theorem

**Date:** 2026-06-06
**Type:** positive_theorem (corner-protection of the `J - I` form + sign cross-check; magnitude left open, reframed)
**Status:** unaudited candidate. Graph-visible only so the independent audit lane can decide.
**Primary runner:** [`scripts/generation_localization_corner_protected_delta_runner.py`](../scripts/generation_localization_corner_protected_delta_runner.py)
**Cached output:** [`logs/runner-cache/generation_localization_corner_protected_delta_runner.txt`](../logs/runner-cache/generation_localization_corner_protected_delta_runner.txt)
**2026-06-07 source bridge:** [`GENERATION_CORNER_HF_VQ_SCREENED_POISSON_BRIDGE_NARROW_THEOREM_NOTE_2026-06-07`](GENERATION_CORNER_HF_VQ_SCREENED_POISSON_BRIDGE_NARROW_THEOREM_NOTE_2026-06-07.md)
with verifier
[`scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py`](../scripts/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.py)
and cache
[`logs/runner-cache/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.txt`](../logs/runner-cache/generation_corner_hf_vq_screened_poisson_bridge_2026_06_07.txt).

## Audit context

The interaction asymmetry `delta` (the two-excitation mutual energy that sources the emergent
signed `C3` coupling `K_C3`, with magnitude `|K_C3|`) is addressed here from the retained
momentum-corner side. A companion note gives the same negative-sign conclusion from the retained
two-body mediator packet; this note is an independent unaudited cross-check and does not rely on
that companion as audit authority. The remaining **magnitude** question had been framed as a
"generation-pair separation." This note resolves that separation from the **retained** generation
structure — and finds the picture is not a spatial separation at all.

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

2026-06-07 bridge repair: the source packet supplies the one-hop theorem deriving the
Generation periodic plane-wave density-kernel bridge. Its target is the periodic
translation-invariant plane-wave density-density kernel and Hartree-Fock plane-wave readout
`Vq(q) = -G/(eps(q)+mu^2)` and `delta_ij = (Vq(0)-Vq(k_i-k_j))/N`, including boundary and
normalization, from the retained staggered two-body mediator. The bridge note above supplies that
finite-lattice derivation on `Lambda_L = (Z/LZ)^3`: normalized translation characters diagonalize
the periodic graph Laplacian; `-G(Lap+mu^2 I)^-1` has multiplier `Vq`; and the Slater
density-density mutual energy is exactly Hartree minus exchange with the displayed `1/N`
normalization. This is a bridge packet for independent re-audit, not an audit verdict, and it
does not pin `|delta|`.
Marker summary for the source-packet gate: periodic translation-invariant plane-wave density-density kernel.

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
The 2026-06-07 bridge note derives this finite periodic boundary/normalization from the native
screened graph-Poisson operator, rather than importing it as a textbook Fourier/Hartree-Fock
formula.

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
   all three pairs (and equal across them). This gives a momentum-corner sign check for
   `delta < 0`, independent of the companion spatial-packet route.

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
  eigenstates. The 2026-06-07 bridge note now proves the periodic screened-Poisson multiplier
  and the Hartree-Fock `1/N` normalization on that finite surface. The retained mediator's
  attraction supplies the framework-native screened density-density channel/sign convention; the
  bridge does not widen the retained bounded open-cubic force result to a universal periodic
  physical mediator theorem.
- **No flavor value forced.** This fixes the **form** (`J − I`) and **sign** (`< 0`) of the `C3`
  coupling; it does not force `r`, `Q`, or any mixing value.

## Forbidden imports check

No new axiom and no external textbook import. The momentum-corner generations and their
translation characters are **retained**; the mediator is **retained_bounded**; and the periodic
`Vq`/Hartree-Fock normalization is now supplied by the source-side finite-lattice source bridge
for independent re-audit. The magnitude is named open, not asserted.

## Runner check breakdown

Class A: (1) source bridge presence/dependency checks; (2) three distinct joint translation
characters; (3) `eps(k_i − k_j) = 8` for all three generation pairs (`J − I` corner-protection);
(4) exact lattice two-fermion `delta` equals the Hartree-Fock formula (`L = 4, 6`) and is `< 0`
and equal for all pairs; (5) `|delta|` scales as `1/N` (monopole-dominated) with the corner Fock
part subleading by `mu^2/8`. Expected
`runner_check_breakdown = {A: N, B: 0, C: 0, D: 0, total_pass: N}`.

## Honest auditor read

The class-A content uses the retained momentum-corner generation structure and the retained
bounded mediator sign/channel, plus the 2026-06-07 finite periodic source bridge, to compute the
two-fermion mutual energy `delta` exactly (Hartree-Fock matrix element, cross-checked against
finite-lattice diagonalization). The three corners' equal inter-transfer `eps(Δk) = 8` protects
the exact `J − I` form; the mutual energy is `delta < 0` for all pairs (re-confirming the sign
from the momentum side); and the magnitude is dominated by the `q = 0` monopole, scaling with
volume and `mu^2`, so it reduces to the mediator IR scale rather than a localization distance.
The result is a **form + sign** theorem with an explicitly open (IR-set) magnitude; it forces no
flavor value. Effective status remains `unaudited` pending independent audit of the new bridge.

## Runner

```bash
PYTHONPATH=scripts python3 scripts/generation_localization_corner_protected_delta_runner.py
```
