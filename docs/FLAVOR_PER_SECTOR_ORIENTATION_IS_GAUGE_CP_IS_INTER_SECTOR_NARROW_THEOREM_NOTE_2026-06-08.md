# Per-Sector Flavor Orientations Are Gauge; the Physical CP Content Is the Inter-Sector Jarlskog

**Date:** 2026-06-08
**Claim type:** bounded_theorem (a gauge classification unifying mass-handedness and CP)
**Status authority:** independent audit lane only. This source note does not set,
predict, or estimate any audit verdict. Effective status is pipeline-derived after
independent audit and dependency closure.
**Primary runner:**
[`scripts/frontier_flavor_per_sector_orientation_gauge_cp_relative.py`](../scripts/frontier_flavor_per_sector_orientation_gauge_cp_relative.py)
**Cached log:**
[`logs/runner-cache/frontier_flavor_per_sector_orientation_gauge_cp_relative.txt`](../logs/runner-cache/frontier_flavor_per_sector_orientation_gauge_cp_relative.txt)
(TOTAL: PASS=11 FAIL=0)

## 0. One gauge principle for all of flavor orientation

The finite calculation below repeats the mass cyclic-handedness check:
`sign(Δ)` is odd under the shared generation-relabeling `R` (an
orientation-reversing transposition, unbroken per the retained-bounded
[`STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23`](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md)).
This note applies the same gauge principle to **CP** and unifies the two:

> Under the shared generation-relabeling `R`, **every per-sector orientation is `R`-odd
> (gauge)** — the mass handedness `sign(Δ)` **and** the within-sector CP cubic
> `I_src(H) = Im(H_{12} H_{23} H_{31})`. The **only** `R`-invariant (physical) orientation
> datum is the **inter-sector Jarlskog** `J` (the `CKM`/`PMNS` CP invariant), built from the
> relative alignment `V = U_1^† U_2` of two sectors.

Consequently the physical flavor CP content is **purely a relative, inter-sector** quantity;
the per-sector CP orientation is gauge, and the "parity bit" residual of the
[`DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20`](DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md)
is a gauge (basis-ordering) split of the physical `J`. The CP-phase **magnitude** is a
separate, already-retained object.

## 1. Inputs and live tiers (verified on `origin/main`, 2026-06-08)

| Input | Source | Live `effective_status` | Role |
|---|---|---|---|
| shared relabel `R` is an unbroken orientation-reversing gauge element (staggered `S_3`) | [`STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23`](STAGGERED_AXIS_SYMMETRY_IS_S3_NARROW_THEOREM_NOTE_2026-05-23.md) | `retained_bounded` | the gauge group |
| single-Hermitian Jarlskog reduction `J_basis = I_src/Δ_λ`, `J_σ = parity(σ)·J_basis` | [`DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20`](DM_PMNS_CP_ORIENTATION_PARITY_REDUCTION_NOTE_2026-04-20.md) | `unaudited` | the decomposition reclassified here (context, plain text) |
| CP-phase **magnitude** `cos²(δ_CKM) = 1/n_quark` | [`CKM_CP_PHASE_STRUCTURAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10`](CKM_CP_PHASE_STRUCTURAL_IDENTITY_NARROW_THEOREM_NOTE_2026-05-10.md) | `retained` | the separate magnitude |

No PDG value is load-bearing. The April-20 reduction is cited as a dependency
for the parity-bit reclassification, not as retained-grade authority. No new
axiom, import, or vocabulary.

## 2. The classification

The flavor gauge group acts by **shared** generation-relabeling — the same permutation on
every sector's mass operator simultaneously (the staggered `S_3`, retained). Its
orientation-reversing element is a transposition `R` (`det R = −1`).

**(MASS) Per-sector mass handedness is gauge.** `sign(Δ)`, `Δ = (p_0−p_1)(p_1−p_2)(p_2−p_0)`,
flips under `R` (finite check; runner `MASS_*`).

**(CP) Per-sector CP cubic is gauge.** For a sector Hermitian `H`, the cubic orientation
`I_src(H) = Im(H_{12} H_{23} H_{31})` flips under `R` (`I_src(R H R^ᵀ) = −I_src(H)`; runner
`CP_Isrc_*`). The single-Hermitian Jarlskog `J_basis = I_src/Δ_λ` (April-20) therefore also
flips under `R` (`CP2_in_basis_Jarlskog_R_odd`), and a row permutation `σ` multiplies it by
`parity(σ)` — so the April-20 **"parity bit" is gauge-dependent** (`CP_parity_bit_*`): it is
the labeling-convention split, not a physical degree of freedom on its own.

**(PHYS) The inter-sector Jarlskog is physical.** The two-sector CP invariant
`J = Im(V_{00} V_{11} V_{01}^* V_{10}^*)`, `V = U_1^† U_2`, is **invariant** under the shared
`R` (`V → (R U_1)^†(R U_2) = U_1^† U_2 = V`), verified over 50 random sector pairs
(`PHYS_two_sector_Jarlskog_R_invariant_shared`). Since the per-sector orientation that builds
it is `R`-odd while `J` is `R`-invariant, **the physical CP content is the relative
(inter-sector) alignment**, never a per-sector orientation (`PHYS_physical_CP_is_relative`).

**(MAG) The magnitude is separate.** The CP-phase magnitude `cos²(δ) = 1/n_quark` is a
distinct, already-retained structural identity (`CKM_CP_PHASE_STRUCTURAL_IDENTITY`); this note
addresses only the orientation/gauge structure, not the magnitude.

## 3. The unified flavor-orientation picture

| Orientation datum | Under shared `R` | Status |
|---|---|---|
| mass cyclic handedness `sign(Δ)` (per sector) | odd | **gauge** (finite check here) |
| CP cubic `I_src(H)` / in-basis `J_basis` (per sector) | odd | **gauge** (this note) |
| April-20 PMNS "parity bit" `parity(σ)` | odd | **gauge** (labeling split) |
| inter-sector Jarlskog `J` (`CKM`/`PMNS`) | invariant | **physical** |
| CP-phase magnitude `cos²δ = 1/n_quark` | invariant | **physical, retained** (separate) |

So the entire **per-sector** orientation content of flavor — mass handedness and CP cubic
alike — is a gauge labeling convention; the physical flavor-orientation data is **exactly**
the inter-sector relative orientations (the Jarlskog invariants), whose **magnitudes** are
structurally derived and whose **signs** are the relative-alignment data. This is consistent
with the physical fact that **CP violation is relative** — there is no absolute single-sector
CP/handedness observable.

## 4. Scope — what this establishes and does not

**Establishes (exact / robust-finite):**
- Per-sector mass handedness and per-sector CP cubic are both `R`-odd (gauge).
- The April-20 PMNS "parity bit" is gauge-dependent (a basis-ordering split of `J`).
- The inter-sector Jarlskog `J` is `R`-invariant (physical); the physical CP content is
  purely relative.

**Does NOT establish (separate / open):**
- It does **not** derive the **value** of any Jarlskog `J` or CP-phase magnitude — the
  magnitude `cos²δ = 1/n_quark` is the separate retained structural identity, and the
  relative-alignment **signs** (which fix `sin δ`'s sign) remain the genuine open flavor
  target now correctly located as inter-sector data.
- It does **not** touch the `r = 1/2` cone or the mass magnitudes `|δ| = 2/9`.
- It does **not** claim the relative orientations are gauge — they are the physical content.

## 5. Honest verdict

Pursuing the inter-sector relative orientations resolves the framing cleanly: the per-sector
orientation content of flavor — mass handedness and CP cubic — is
**gauge** under the shared generation-relabeling; the physical flavor-orientation data is
**exactly** the inter-sector Jarlskog invariants. This unifies the mass and CP sides under one
gauge principle and sharpens every per-sector "orientation/parity" residual (including the
April-20 PMNS parity bit) as gauge — relocating the genuine open target to the **inter-sector
relative orientations** (the `CKM`/`PMNS` Jarlskog signs), whose magnitudes are already
structurally derived. The physical flavor sector, after this finite gauge classification,
reads: firewalled cone `r = 1/2`, derived magnitudes `|δ| = 2/9 = L_3(1,2)`, generation
number 3, gauge per-sector orientations, and physical inter-sector relative orientations
(mixing/CP) — exactly the data CP violation is built from.

## 6. No-Go Discipline Gate

**Status:** PASS for this bounded gauge classification. It does **not** claim any CP value is
derived, that the relative orientations are gauge, or that the magnitude is unphysical.

**N1 — Alternative-route enumeration.**

| Route | Marker | Result |
|---|---|---|
| per-sector mass handedness as physical CP/orientation | RULED OUT | `R`-odd (gauge) — finite check here |
| per-sector CP cubic `I_src` / in-basis `J_basis` as physical | RULED OUT | `R`-odd (gauge) — this note |
| April-20 "parity bit" as a physical residual | RECLASSIFIED | gauge (labeling split of `J`) |
| inter-sector Jarlskog `J` | PHYSICAL | `R`-invariant; the genuine CP datum |
| CP-phase magnitude | PHYSICAL / RETAINED | `cos²δ = 1/n_quark` (separate) |

**N2 — Wall-independence.** Per-sector orientation gauge-ness (this note + companion), the
inter-sector Jarlskog values, the CP magnitudes, and the mass magnitudes are independent;
this note resolves only the gauge classification.

**N3 — Hidden-wall scan.** Uses only the shared-`R` action on Hermitians and mixings and the
definitions of `I_src`/`J`; no hidden physical-handedness premise.

**N4 — Residual matching.** The residual is relocated to the inter-sector relative-alignment
signs (the Jarlskog signs), not any per-sector orientation.

**N5 — Rhetoric audit.** The claim is gauge-ness of **per-sector** orientations and
physicality of the **inter-sector** Jarlskog; not a CP derivation.

**N6 — Partial-closure path scan.** The genuine next target is the inter-sector relative
orientations (Jarlskog signs / mixing), now isolated. No new axiom requested.

**N7 — Steelman.** A reviewer may note the two-sector `J` is trivially `R`-invariant because
`R` cancels in `U_1^† U_2`. That cancellation **is** the content: it is precisely why the
physical CP cannot be a per-sector datum (which does not enjoy the cancellation) — the CP
invariant lives only in the relative alignment.

**N8 — Cross-cycle echo.** Consistent with the retained staggered `S_3` (gauge
group), the finite mass-handedness check, the April-20 reduction (reclassified,
not overruled), and the retained CP-phase magnitude identity.

## 7. Forbidden-imports check

- **No new axioms / imports / vocabulary.** Inputs are the cited retained/retained-bounded
  rows plus standard Jarlskog/Hermitian algebra.
- **No PDG/fitted load-bearing input; no forcing of `r = 1/2`; no new transcendental.**
- The April-20 note is cited as the parity-bit source being reclassified; it is
  not used as retained-grade authority.

## 8. Command

```bash
python3 scripts/frontier_flavor_per_sector_orientation_gauge_cp_relative.py
```

Expected: `TOTAL: PASS=11 FAIL=0`. numpy + stdlib, deterministic (seeded), 3×3 throughout
(memory-safe). The runner verifies the `R`-oddness of the mass handedness and the per-sector
CP cubic, the April-20 `J_basis = I_src/Δ` reduction and its gauge parity behavior, the
`R`-oddness of the in-basis Jarlskog, the shared-`R` invariance of the two-sector Jarlskog
over 50 random pairs, and the separate CP-phase magnitude identity.
