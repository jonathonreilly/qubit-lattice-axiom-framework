# Distributed tree/toric returned-work compiler — Cycle 653

Classification: **positive finite local-gate coupling; strict autonomous physical compiler open**

Authority: **none**

Audit: **unset**

Author artifact status accepted: **false**

Breakthrough: **false**

## Strongest constructive result

On L3, L6, and held-out L7, the plaquette-only cubic link code has exact rank
`2N-2` and therefore exactly `N-1` ordinary gauge qubits plus three coherent
holonomies.  Its state-carried local coordinates obey

`z(v,a) = g(v) xor g(v+e_a) xor t_a*[periodic cut]`.

Consequently the local link dressing cancels the endpoint gauge gradient and
leaves `t_a` only on the matching seam.  This geometric rule reproduces every
Cycle650 corrected matter and gauge row with zero mismatch and zero failures
over all eight topological basis sectors.  It uses no runtime global Wilson
table and never fixes `+++`.

This yields an exact finite change of encoding `E_flat P E_tree^dagger` and the
declared character/interface intertwiner
`E_local G_coarse = G_local_link_dressed E_local`.  `G_coarse` is not
redefined.  The result is not promoted to a strict physical compiler because
the complete update remains an extensive supplied schedule and the full
term-by-term intrinsic even-CAR local algebra is not synthesized.

## Route A — tree-root/link reversible message passing

| size | root factors gathered | NN primitive CNOTs | max routed distance |
|---|---:|---:|---:|
| L3 | 48 | 38928 | 265 |
| L6 | 72 | 58824 | 267 |
| L7 | 48 | 38928 | 265 |

Each positive-Z root character is coherently computed into its corresponding
physical seam-link seed.  Remote CNOTs are expanded into NN SWAP/CNOT/SWAP-back
macros; every intermediate M2 is restored.  Reverse compute after use returns
the message work.  The present relation is scheduled, not a simultaneously
commuting static local tree/link constraint set.

## Route B — flat-link gauge fixing and holonomy distribution

| size | plaquette rank | gauge+topo exponent | abstract factors | NN-routed factors |
|---|---:|---:|---:|---:|
| L3 | 52 | 29 | 473 | 1338203 |
| L6 | 430 | 218 | 6485 | 31512719 |
| L7 | 684 | 345 | 11685 | 65527239 |

Weight-four plaquette constraints are local and covariant.  Exact gauge pairs
are non-root stars with their tree-path Z duals; three loop/membrane pairs carry
arbitrary coherent holonomies.  Encoder/decoder, inverse, leakage, independent
constraint deletion, malformed redundant phase, and factor deletion controls
pass.  Local link variables, not a host parity query, carry the seam signs.

| size | matter seam rows | gauge seam rows | exact chart mismatches |
|---|---:|---:|---:|
| L3 | 27 | 27 | 0 |
| L6 | 108 | 108 | 0 |
| L7 | 147 | 147 | 0 |

## Route C — staggered/time-multiplexed local coupling

| size | logical wires transferred | sequential-depth upper bound | max transfer distance |
|---|---:|---:|---:|
| L3 | 191 | 22691117 | 1035 |
| L6 | 1514 | 603199325 | 1677 |
| L7 | 2403 | 1302483056 | 2193 |

The explicit stages are NN-routed tree decode, logical transfer, NN-routed
flat-link encode, local gradient/link dressing, and reverse temporary work.
All emitted two-site primitives have fine-L1 range one.  Placement uses a
doubled `K129` torus: old M2 coordinates are doubled, the supplied target-wire
order is assigned to six signed unit-axis ports per cell, and links occupy
exact cubic-edge midpoints.
The full routing mesh costs `17173512` M2 per coarse cell—a finite but enormous
constant—and its blank/work state plus sequential order remain supplied.

All 24 proper-cubic frames and all 576 products close by transported schedule;
there is no runtime frame selector.  Schedule covariance is not an autonomous
clock or physical time law.

## Exact inherited interface and controls

- onsite residual: `5.272e-15`
- FSWAP residual: `0.0e+00`
- Cycle219 mass residual: `2.220e-16`
- Cycle230 contact deletion residual: `0.367893067056082`
- Cycle230 seam: `6 PASS / 0 FAIL`
- plus/minus seam singular residual: `1.417e-15`
- symbolic local-link character failures: `0`

These are the exact original fixtures.  `G_local_link_dressed` is the geometric
state-carried link representation of the same seam character, not permission
to alter `G_coarse` and not a new autonomous law.

## Supplied structure and prior-art boundary

Supplied are immutable Cycle650/Cycle642/Cycle647 tableau machinery; finite
L3/L6/L7 domains; root and logical-wire order; the doubled full K129 routing
mesh and its work references; the spanning-tree gauge section; compile-time
frame transport; and the extensive gate schedule.  No global Jordan-Wigner
order, nonlocal parity service, or runtime Wilson-character lookup is used.

Flat Z2 connections, spanning-tree gauge fixing, toric holonomies, Clifford
stabilizer encoders, and NN SWAP routing are standard prior art.  The narrow
new result is their exact finite composition with the Cycle650 rank/center and
Cycle230 seam-character fixture, including the held-size and returned-work
receipts.  No broader novelty is claimed.

## Route disposition and six-wall ledger

- Route A: **finite NN reversible root/link message construction passes;
  static commuting constraint realization remains open**.
- Route B: **exact N-1+3 flat-link encoder and local character cancellation
  pass at L3/L6/held L7**.
- Route C: **complete finite NN change-of-encoding schedule passes; autonomous
  bounded-period G and term-complete local CAR representation remain open**.

| wall | movement | residual |
|---|---|---|
| `C_ref` | holonomies are arbitrary state-carried inputs | mesh blanks, gauge section, and schedule supplied |
| `C_num` | exact ranks, inverse, rows, sectors, and fixtures | no Born/empirical normalization |
| `C_wrap` | local link field replaces runtime Wilson table | autonomous topological genesis not claimed |
| `C_int` | original mass/contact/seam character composes | complete elementary G factorization remains open |
| `C_local` | every emitted compiler primitive is NN | depth scales with size; full mesh density is enormous |
| `C_source` | link/work resources counted | no source, stress, energy, or gravity identification |

## N1-N8 no-go-discipline gate

N1 records five normalized families and three additional open mechanisms. N2
keeps two independent residuals: full local algebra and autonomous scheduling.
N3 exposes the mesh, blanks, gauge section, and schedule. N4 uses Cycle650's
missing local E/coupling as an exact retired residual and rejects its distinct
nonlocal-factor witness as proof of the autonomous-law wall. N5 narrows every
negative to finite interface or schedule resolution. N6 lists three concrete
partial-closure paths. N7 steelmans a finite-color local QCA with a returned
clock band. N8 records that local E/coupling and sparse nonlocal gates were
partially retired without retiring the autonomous-law residual.

No-go status: **PASS** (checklist complete).

Broad negative gate: **FAIL / DO NOT SHIP**.

Minimum-content gate: **FAIL / DO NOT SHIP**.

Shared-obstruction gate: **FAIL / DO NOT SHIP**.

Axiom-pressure gate: **FAIL / DO NOT SHIP**.

Shared route-independent obstruction: **none**. Axiom pressure: **none**.
