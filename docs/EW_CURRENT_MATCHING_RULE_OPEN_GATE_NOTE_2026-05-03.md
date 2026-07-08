# EW Current Matching Rule Kappa_EW Parametrization Note

**Date:** 2026-05-03
**Claim type:** bounded_theorem
**Status:** audited-conditional narrow recut. The live claim is the exact
one-parameter `kappa_EW` EW matching parametrization on the retained Fierz/CMT
surface. This note does not derive, select, or foreclose the selector
`kappa_EW = 0`.
**Claim scope:** for every supplied `kappa_EW`, the note proves
`K_EW(kappa_EW) = T/(C + kappa_EW*S) =
1/(F_adj + kappa_EW*(1 - F_adj))`; at `N_c = 3`,
`K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)`. It computes the
`kappa_EW = 0` and `kappa_EW = 1` completions as exhibits only.
**Primary runner:** `scripts/frontier_ew_current_matching_rule_no_go.py`

## Cited Authority

- [Fierz channel note](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md)
  is cited only for its audited scope: the exact SU(`N_c`) Fierz/channel-count
  ratio `F_adj = (N_c^2 - 1) / N_c^2`, hence `F_adj = 8/9` at `N_c = 3`,
  and its explicit statement that the physical matching rule is not derived
  there.

No other load-bearing dependency is used here. The CMT and OZI inputs below are
named features of this parametrization surface, not unstated context and not
additional linked dependencies.

## Safe Statement

On the retained Fierz/CMT surface, the EW alpha-level matching factor is the
exact rational function

```text
K_EW(kappa_EW)
  = T / (C + kappa_EW S)
  = 1 / (F_adj + kappa_EW (1 - F_adj)).
```

At `N_c = 3`,

```text
K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9).
```

This is a bounded theorem about the whole named premise family. It computes
the connected-trace specialization `kappa_EW = 0` as `K_EW = 9/8`, and the
full-trace specialization `kappa_EW = 1` as `K_EW = 1`. It does not derive
`kappa_EW = 0`; the selector is supplied.

## Named Conditional Premise KAPPA-EW

```text
KAPPA-EW (named conditional premise):
the physical disconnected-current readout coefficient kappa_EW is
SUPPLIED; the connected-trace selector is the special case kappa_EW = 0.
Not derived: no landed route selects kappa_EW; this note's
parametrization covers every finite value exactly.
```

Surface features consumed by the exact lemmas:

- **FIERZ-ADJ:** `C/T = F_adj = (N_c^2 - 1) / N_c^2` and
  `S/T = 1 - F_adj = 1/N_c^2`, with `N_c = 3` for the package exhibit.
- **CMT-COLOR-BLIND:** the CMT substitution `U -> u_0 V` multiplies the
  connected and singlet two-link EW-current channels by the same `u_0^2`.
- **OZI-BOUNDED:** finite supplied `kappa_EW` keeps the singlet readout in the
  exact class `kappa_EW S/C = kappa_EW/(N_c^2 - 1) = O(1/N_c^2)`.

## Exact Identities: Coefficient Parametrization

Normalize the post-CMT channel sum to

```text
T = C + S = 1,
```

where

```text
C = F_adj = (N_c^2 - 1) / N_c^2,
S = 1 - F_adj = 1 / N_c^2.
```

Let `kappa_EW` be the physical disconnected-current readout coefficient:

```text
Pi_EW^phys(kappa_EW) = C + kappa_EW S.
```

The CMT/lattice normalization reads the total channel sum `T`. Therefore the
EW alpha-level matching factor is

```text
K_EW(kappa_EW)
  = T / Pi_EW^phys(kappa_EW)
  = 1 / (F_adj + kappa_EW (1 - F_adj)).                  (1)
```

Equivalently, `K_EW(kappa_EW) = 1 / (F_adj + kappa_EW (1 - F_adj))`.

At `N_c = 3`, equation (1) becomes

```text
K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9).
```

The formula is an exact rational parametrization. At the zero-denominator
point it records an undefined normalization exactly; it does not choose a
physical selector.

### Lemma 1. Fierz fixes channel dimensions, not the readout functional

Consumed surface feature: **FIERZ-ADJ**.

The Fierz/channel-count theorem fixes only the decomposition

```text
q qbar = 1 + adj,
dim(1) = 1,
dim(adj) = N_c^2 - 1.
```

It therefore fixes

```text
C / T = (N_c^2 - 1) / N_c^2,
S / T = 1 / N_c^2.
```

No equation in that theorem assigns the physical EW current to `C` rather than
to `C + kappa_EW S`. The value of `kappa_EW` is a statement about the
lattice-to-continuum current readout, not about representation dimension.

### Lemma 2. CMT color-blind invariance

Consumed surface feature: **CMT-COLOR-BLIND**.

The CMT substitution `U -> u_0 V` gives the same two-link factor to every
EW-current channel:

```text
C(U) = u_0^2 C(V),
S(U) = u_0^2 S(V),
T(U) = u_0^2 T(V).
```

Consequently equation (1) is invariant under CMT scaling:

```text
T(U) / (C(U) + kappa_EW S(U))
  = T(V) / (C(V) + kappa_EW S(V)).
```

CMT can neither select `kappa_EW = 0` nor exclude `kappa_EW = 1`, because it
treats both channels uniformly.

### Lemma 3. OZI suppression class

Consumed surface feature: **OZI-BOUNDED**.

For finite supplied `kappa_EW`, the disconnected readout contribution relative
to the connected channel is

```text
kappa_EW S / C
  = kappa_EW / (N_c^2 - 1)
  = O(1/N_c^2).
```

This includes `kappa_EW = 0`, `kappa_EW = 1`, and any finite intermediate
coefficient. The OZI feature therefore supplies a suppression class, not the
exact coefficient needed to make `K_EW = 9/8`.

## Completions Exhibit

Construct two completions of the same parametrization surface:

```text
Completion A: kappa_EW = 0,  K_EW = 9/8.
Completion B: kappa_EW = 1,  K_EW = 1.
```

Both completions satisfy the exact Fierz ratio `C/T = 8/9`, the same
color-blind CMT scaling law, and the same finite-`kappa_EW`
`O(1/N_c^2)` disconnected-channel size class. They are exhibits inside the
parametrization, not a theorem that no selector derivation can exist.

## Residuals

**R-selector remains open.** A future theorem would need to derive
`kappa_EW = 0` from a lattice-current selector argument, or compute the exact
disconnected-current coefficient and show that the physical EW readout sets it
to zero.

The former broad no-go ambition is kept only as residual route inventory,
not as a claim of this note. Its five-route N1-N8 wall list lives here as an
open target:

- **N1 alternative route enumeration:** the checked route families are direct
  connected-source lifting, augmentation-ideal lifting, scalar/taste-condensate
  lifting, EW traceless-generator lifting, and source-action or carrier-ray
  support as physical color-matrix source authority.
- **N2 wall independence:** the live wall is the missing physical source or
  readout authority; closing that wall would retire the residual.
- **N3 hidden-wall scan:** current-surface phrases are scoping markers, not
  hidden premises.
- **N4 residual matching:** the witnesses all point to a separate
  `kappa_EW` selector.
- **N5 rhetoric audit:** negative wording, when used, is route-specific only.
- **N6 partial-closure scan:** physical current authority, exact
  disconnected-current computation, or a strict same-source response theorem
  remain open.
- **N7 steelman:** a future source-authority theorem could make the selector
  derivable.
- **N8 cross-cycle echo:** similar selector walls elsewhere do not transfer
  closure onto this EW matching surface.

## Citation Contract

Citation is audit-gated. This note may be cited only for the exact
`K_EW(kappa_EW)` parametrization and the two computed completions under the
named KAPPA-EW premise.

Forbidden uses:

- citing `kappa_EW = 0` as derived;
- citing this note as a no-go against future selector derivations;
- using empirical agreement after choosing `kappa_EW = 0` to fit or ratify the
  coefficient.

Safe downstream wording:

> The EW normalization lane is bounded by a named matching coefficient
> `kappa_EW`: `K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9)`. The familiar
> `9/8` alpha-level correction is the connected-trace specialization
> `kappa_EW = 0`, not an unconditional retained theorem.

Unsafe downstream wording:

> The framework derives the exact `9/8` EW color-projection correction.

## Firewall

- No observed values, PDG comparisons, or empirical agreement are used.
- No selector derivation is claimed.
- No route-pruning no-go is claimed by this recut.
- The file name and claim identity are unchanged; only the claim typing and
  live scope are narrowed.
- The one-hop dependency is the Fierz/channel note at its audited exact-ratio
  scope. CMT and OZI are named surface features consumed by lemmas, not extra
  load-bearing dependencies.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/frontier_ew_current_matching_rule_no_go.py
```

The runner verifies the exact rational arithmetic, the CMT invariance of the
free coefficient, the OZI boundedness class, the two computed completions, the
KAPPA-EW declaration, and the direct wording guardrails. Downstream wording
checks are reported in the non-fatal motivation tier.

## Audit-Lane Status

- **2026-07-08 recut:** the auditor verdict for row
  `ew_current_matching_rule_open_gate_note_2026-05-03` states that the exact
  formula `K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)` and the
  `kappa_EW = 0` versus `kappa_EW = 1` independence witness "are valid under
  the stated assumptions", and sanctions the repair: "narrow the note to the
  algebraic kappa_EW parametrization."
- This source-side recut implements only that narrow repair. It does not
  decide landings, edit audit data, or upgrade the connected-trace selector to
  a derived theorem.
