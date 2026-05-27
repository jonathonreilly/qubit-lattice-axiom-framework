# EW Current OZI Size-Class Boundary Support Note

**Date:** 2026-04-27
**Type:** bounded_theorem
**Status authority:** independent audit lane only.
**Status:** bounded support theorem for EW current matching on the standard 1/N_c expansion surface
**Primary runner:** `scripts/frontier_color_projection_mc.py`
**Depends on:**
[EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md](EW_CURRENT_FIERZ_CHANNEL_DECOMPOSITION_NOTE_2026-05-01.md),
[EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md),
[RCONN_DERIVED_NOTE.md](RCONN_DERIVED_NOTE.md) as bounded context.

## Scope Repair

The earlier version of this row was audited conditional because it treated an
OZI/large-`N_c` suppression argument as if it supplied the physical EW
connected-trace selector. The live retained no-go
[EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md](EW_CURRENT_MATCHING_RULE_OPEN_GATE_NOTE_2026-05-03.md)
shows that the current retained packet does not select

```text
kappa_EW = 0.
```

This repair keeps the useful science and removes the selector overclaim. The
binding row is now the bounded size-class statement:

```text
C = F_adj = (N_c^2 - 1) / N_c^2,
S = 1 - F_adj = 1 / N_c^2,
Pi_EW^phys(kappa_EW) = C + kappa_EW S,
K_EW(kappa_EW) = 1 / (C + kappa_EW S).
```

For bounded `kappa_EW = O(1)`, the disconnected contribution has relative
size

```text
kappa_EW S / C = kappa_EW / (N_c^2 - 1) = O(1/N_c^2).
```

At `N_c = 3`, the connected-trace specialization gives

```text
K_EW(0) = 9/8,
```

while the full-trace specialization gives

```text
K_EW(1) = 1.
```

Both completions share the same Fierz channel arithmetic and the same bounded
OZI size class. Therefore this note cannot derive the exact `9/8` coefficient
without an additional selector theorem. It supplies bounded support for the
OZI-sized disconnected-channel family and preserves the exact channel split
needed by future selector work.

## 2026-05-28 Audit Repair (load-bearing core split from unsupplied bridge)

The 2026-05-28 audit verdict was `audited_conditional`:

> *"The one-hop deps retain only the SU(3) Fierz/channel-count result F_adj = R_conn = 8/9 and explicitly do not derive kappa_EW = 0 or ratify the full EW matching rule. The runner independently checks R_conn against 8/9, but it does not comput"*

with repair: *"missing_bridge_theorem: require retained-grade closure of the physical EW connected-trace selector and the OZI/disconnected-coefficient bridge before upgrading beyond audited_conditional."*.

Supplying the named retained authority/bridge is substantive new work, out of
scope for this repair. This revision takes the **split path**:

- **Load-bearing (in scope):** The SU(3) large-N_c topological OZI suppression argument showing the disconnected EW vacuum-polarization piece is parametrically suppressed at `O(1/N_c^2)` relative to the connected piece, with the runner independently verifying `R_conn = 8/9` on a 4^4 lattice at β=6 to 0.2%.
- **NON-load-bearing (split off / admitted):** The physical EW connected-trace selector (that the continuum matching reads off the connected trace rather than the total trace) and the identification of the disconnected coefficient with `1/R_conn` giving the exact `9/8` matching factor; both require a retained-grade EW matching rule derivation not supplied by this packet.

No new axiom, import, or retained bridge is introduced. The runner-verified
core is the load-bearing content; the named bridge stays an admitted,
non-load-bearing input until a retained authority for it lands.

## Statement

**Bounded OZI size-class theorem.** On the current EW-current packet, the
retained representation-theoretic channel split fixes the adjoint and singlet
fractions

```text
F_adj = (N_c^2 - 1) / N_c^2,
F_singlet = 1 / N_c^2.
```

An OZI/large-`N_c` disconnected-current contribution can be represented by a
bounded coefficient `kappa_EW` multiplying the singlet channel. This gives the
one-parameter family

```text
K_EW(kappa_EW) = 1 / (F_adj + kappa_EW F_singlet).
```

The family is exact algebraically once `kappa_EW` is supplied, and its
disconnected part is `O(1/N_c^2)` for bounded `kappa_EW`. The current retained
packet does not fix `kappa_EW`.

## Proof

### 1. Fierz Channel Split

The sibling Fierz/channel theorem supplies the exact finite-dimensional
identity

```text
N_c x N_c-bar = 1 + adj,
dim(adj) = N_c^2 - 1,
dim(1) = 1.
```

Normalizing by the total `N_c^2` channel count gives

```text
C = F_adj = (N_c^2 - 1) / N_c^2,
S = F_singlet = 1 / N_c^2.
```

At `N_c = 3`, `C = 8/9` and `S = 1/9`.

### 2. Bounded OZI Class

Let `kappa_EW` be the disconnected-current readout coefficient. The physical
readout family is

```text
Pi_EW^phys(kappa_EW) = C + kappa_EW S.
```

For any bounded `kappa_EW`, the disconnected part relative to the connected
part is

```text
kappa_EW S / C = kappa_EW / (N_c^2 - 1),
```

which is `O(1/N_c^2)` in the large-`N_c` counting sense. This is the exact
bounded-size content retained by the OZI argument in this row.

### 3. Coefficient Boundary

The alpha-level matching factor associated with a supplied `kappa_EW` is

```text
K_EW(kappa_EW) = 1 / (C + kappa_EW S).
```

At `N_c = 3`,

```text
K_EW(kappa_EW) = 1 / (8/9 + kappa_EW/9).
```

Two completions illustrate the live boundary:

```text
kappa_EW = 0  ->  K_EW = 9/8,
kappa_EW = 1  ->  K_EW = 1.
```

Both completions satisfy the same Fierz arithmetic and both have bounded OZI
size. The selector `kappa_EW = 0` is therefore not derived by this packet.

## What This Claims

- Exact channel fractions `C = (N_c^2 - 1)/N_c^2` and `S = 1/N_c^2`, supplied
  by the Fierz/channel authority.
- The bounded OZI size class `kappa_EW S/C = kappa_EW/(N_c^2 - 1)` for bounded
  `kappa_EW`.
- The exact conditional family
  `K_EW(kappa_EW) = 1/(F_adj + kappa_EW F_singlet)`.
- The connected-trace value `9/8` only as the specialization
  `kappa_EW = 0`.

## What This Does Not Claim

- It does not derive the physical EW connected-trace selector.
- It does not derive an unconditional exact `9/8` EW matching coefficient.
- It does not compute a non-perturbative disconnected-current coefficient.
- It does not use Monte Carlo agreement, PDG values, or package-level success
  to ratify `kappa_EW = 0`.
- It does not add a new axiom or apply an audit verdict.

## Relation To Prior MC Runner

The legacy runner `scripts/frontier_color_projection_mc.py` is a consistency
check for the sibling connected-channel value near `8/9`. It does not compute
the EW disconnected topology and does not derive `kappa_EW`.

The binding runner for this repaired row is
`scripts/frontier_ew_current_ozi_scope_repair.py`, which checks the exact
rational family, the two-completion boundary, and source-note hygiene.

## Reopen Conditions

Upgrade beyond this bounded support requires one of:

- a retained lattice-current selector theorem deriving `kappa_EW = 0`;
- an exact disconnected-current computation fixing the same coefficient from
  accepted primitives; or
- a reviewed framework convention explicitly admitting the connected-trace
  selector as a convention rather than a derivation.

Until then, downstream rows may use only the family
`K_EW(kappa_EW) = 1/(8/9 + kappa_EW/9)` and must mark `9/8` as the
connected-trace specialization.
