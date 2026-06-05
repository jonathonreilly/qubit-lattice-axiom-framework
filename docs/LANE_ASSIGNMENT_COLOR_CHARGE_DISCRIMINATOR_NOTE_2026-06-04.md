# Lane assignment — the color/charge discriminator EXPLAINS the dial-point *side* (clean correlation + a structural-direction mechanism), but not the magnitude: COLOR breaks the generation block-symmetry toward hierarchy (r>1/2), NEUTRALITY toward degeneracy (r<1/2), charged-colorless stays at the symmetric point r=1/2.

**Date:** 2026-06-04
**Type:** meta
**Claim type:** meta
**Status:** source-note proposal; analysis of the lane-assignment bit on the Record-axiom dial.
No theorem promotion, no status set — pipeline-derived `claim_type`/`audit_status`/`effective_status`
generated only after independent audit review. The candidate Record axiom is itself axiom-update-provisional.
**Authority role:** records a NEW angle on the charged-lepton `r=1/2` problem. The campaign reduced the
single-sector question "why is the charged lepton at `r=1/2`?" to two posited inputs (K-reality + block-counting
measure). This note instead asks the *comparative* question — **what sector property assigns each fermion sector
to its own dial point** — and tests the color/charge discriminator hypothesis end-to-end (correlation + mechanism).
**Runner:** [`scripts/lane_assignment_color_charge_discriminator_2026_06_04.py`](../scripts/lane_assignment_color_charge_discriminator_2026_06_04.py) (SCORECARD PASS=27 FAIL=0).
**Cache:** [`logs/runner-cache/lane_assignment_color_charge_discriminator_2026_06_04.txt`](../logs/runner-cache/lane_assignment_color_charge_discriminator_2026_06_04.txt).

## Authority disclaimer
This is a source-note proposal. The audit lane has full authority to retag, narrow, or reject it. No
PDG value is consumed as a derivation input; observed Koide `Q` values appear **only** as labelled
observational comparison (the dial-point readout `r = (3Q−1)/2`), never as fitted inputs to the mechanism.

## The dial and the open bit
The candidate Record axiom makes the generation sector-weight a **dial**:
`Q = 1/3 + (2/3) r`, with `r = |b|²/a²` the C₃ doublet/singlet power ratio (`a` = singlet coupling,
`b` = doublet coupling of the equivariant operator `H = aI + bC + b̄C²`). The point `r=1/2` is the **unique
fixed point of the singlet↔doublet block-swap** `r → 1/(4r)`, giving `Q=2/3`. Different fermion sectors occupy
different dial points. The open bit isolated by the whole arc: **which sector property pins each sector to its
point?** (Runner §0 verifies the dial identity to `1e-9` via the signed/Brannen readout, and the swap fixed point.)

## The pattern (observed Q → dial point r; labelled observational comparison only)

| sector | color rep | electric charge | dial point `r=(3Q−1)/2` | lane |
|---|---|---|---|---|
| up quarks (u,c,t) | **triplet 3** | +2/3 | **0.774** | HIERARCHY (r>1/2) |
| down quarks (d,s,b) | **triplet 3** | −1/3 | **0.597** | HIERARCHY (r>1/2) |
| charged leptons (e,μ,τ) | **singlet 1** | −1 | **0.500** | SYMMETRIC (r=1/2) |
| neutrinos (NO, m₁→0…heavy) | **singlet 1** | 0 | **0.38 → 0** | DEGENERATE (r<1/2) |

## Verdict: **PARTIAL** — discriminator-works-on-direction (clean correlation + a structural-direction mechanism); magnitude free, color-sign motivated-not-forced

### 1. The correlation is CLEAN (runner §1, all PASS)
The two-predicate map separates **all four** sectors with **no exception**:
- **color-triplet ⟺ hierarchy (r>1/2):** the two `r>1/2` sectors are *exactly* the colored ones (up, down). Clean.
- **neutral & colorless ⟺ degenerate (r<1/2):** the degenerate sector is *exactly* the electrically neutral one. Clean.
- **charged & colorless ⟺ symmetric (r=1/2):** the charged leptons are the **unique** sector with electric charge
  but no color, and they sit at the symmetric point to <0.2% (`r_lep=0.49999`). **"charged ∧ colorless ⟺ symmetric lane" is EXACT.**

### 2. Color → hierarchy: the MECHANISM (direction) computes structurally (runner §2)
The framework identifies the **center `Z₃ ⊂ SU(3)_c`** (triality) with the **C₃ generation cycle**. Decomposing
the generation triplet into net-triality modes (runner §2.1–2.3, verified to `1e-12`):
- the **colorless** (totally symmetric `(1,1,1)/√3`) combination carries **zero net triality** = the **C₃ singlet**;
- the **color-phase** (triality `ω, ω²`) modes **are** the **C₃ doublet** (max net triality);
- the singlet projector `P₀` *annihilates* the triality modes; the doublet projector `P₁` *retains* them.

So **carrying color charge = living on the C₃-doublet block.** A positive color (Casimir-weighted) coupling
therefore enhances the **doublet** weight `b`, pushing `r` **above** `1/2` → hierarchy (runner §2.4: for a color
coupling `g·C₂(3)` with `C₂(3)=4/3`, the colored sector moves to `r>1/2` while the colorless one stays at `1/2`).
**The direction is structural** (it follows from triality-lives-on-the-doublet, not a free sign at the level of *which block*).

### 3. Neutrality → degenerate: the MECHANISM (direction) computes (runner §3)
A **Majorana / diagonal neutral mass is C₃-diagonal** — it contributes to the **singlet** block `a`, so `r` drops
**below** `1/2` → degenerate (runner §3.1). This matches the physics: neutrino masses are **near-degenerate**
(small splittings), so `r→0` (`Q→1/3`, democratic) as the absolute scale rises (runner §3.2), and the neutral
sector never reaches the charged `2/3` point over the cosmological window (runner §3.3).

### 4. The symmetric lane (runner §4)
**U(1)_em is generation-blind**: it commutes with `C₃` and acts as a scalar `e^{iqχ}I` on the triplet, so it
shifts `r` by **zero** (runner §4.1 — this reconciles with the retained gauge-U(1)-blindness finding: electric
charge *per se* does not move the dial). A charged-but-colorless sector therefore has **neither** the (non-abelian)
color doublet-enhancement **nor** the Majorana singlet-enhancement → it sits at the **swap-symmetric fixed point
`r=1/2`** (runner §4.2). Being at the symmetric point is equivalent to **"no net symmetry-breaking gauge structure
on the generation blocks."** And `r=1/2` is the unique self-image of the block-swap `r→1/(4r)` (runner §4.3).

### 5. Adversarial — color/charge BEATS the alternatives (runner §5)
- **|Q_em| magnitude does NOT track r:** the lepton has the **largest** |Q_em| (=1) yet the **smallest** `r`
  among the charged sectors — `|Q_em|`-ordered `r = [0.50, 0.77, 0.60, 0.38]` is **not** monotone. So the U(1)
  charge *magnitude* anti-correlates and is not the driver. **COLOR is the lane driver.**
- **Mass scale does NOT give a clean r-law** (the top is heaviest yet the up-sector `r=0.77`; `τ` gives `r=0.5`).
- The color/charge two-predicate map is the **unique clean separator** of the three lanes tested.

### 6. Swap-partner structure — a genuinely new depth (runner §6)
The **hierarchy lane (quarks, r>1/2) and the degenerate lane (neutrinos, r<1/2) are SWAP-PARTNERS** under
`r→1/(4r)`: `swap(r_up=0.774)=0.323` and `swap(r_dn=0.597)=0.419` both land on the degenerate side, and up's
swap-image `0.323` sits **inside** the neutrino band `(0, 0.38]`. The **charged-colorless lane is the unique
self-image** (fixed point). So **colored ↔ neutral are reflections of each other about the charged-lepton point** —
the symmetric lane is not just "in the middle," it is the literal involution-center separating the two gauged extremes.

## Honest residual — what is forced vs free
- **FORCED (structural):** *which block* each gauge structure weights — color → the C₃ **doublet** (triality lives
  there); Majorana/neutral diagonal mass → the C₃ **singlet**; U(1)_em → **neither** (generation-blind). This pins
  each sector's **lane (side of `r=1/2`)** and makes the charged-colorless sector the swap fixed point.
- **NOT FORCED:** the coupling **magnitudes** (hence the up/down split — up and down share the **same** color rep
  `3` yet have different `r`, so color fixes the *side*, not the *value*; the up/down magnitude split needs a
  **second, weak-isospin axis**), and the **sign** of the color coupling (the triality-on-doublet structure
  *motivates* a positive sign — adding color adds doublet weight — but does not *force* the coupling positive at
  the dynamical level). One free coupling per sector still fits any `r`.

So this is a **structural mechanism for the lane assignment**, not a closed quantitative derivation of the dial points.

## The paths this opens (not closing)
1. **Derive the color-coupling sign.** Triality-lives-on-the-doublet suggests the color contribution *adds* doublet
   weight (positive). A dynamical argument that the color-Casimir contribution to the generation operator is sign-definite
   would upgrade §2 from "direction computes" to "hierarchy forced for colored sectors."
2. **The second (weak-isospin) axis** for the up/down magnitude split — both quarks are colored (same lane) but
   `r_up≠r_dn`; the splitting tracks `T₃` / the up/down doublet structure, an orthogonal handle on the *value within* a lane.
3. **A neutral-sector structural reason** that the diagonal/Majorana mass dominates (drives `r<1/2`) — i.e. why the
   neutral sector's generation operator is singlet-weighted. This is the degenerate-lane analog of the color argument.
Closing any of these promotes "lane assignment" from **correlation + direction** to a quantitative prediction; none of
them is the single-sector `r=1/2` block-counting/K-reality gate — they are the **comparative** (cross-sector) handles.

## Relation to the campaign's two-input reduction
The single-sector arc reduced "charged-lepton `r=1/2`" to (1) K-reality (the 2-block partition) and (2)
block-counting vs Born (the value within the 2-block structure). This note is **orthogonal and complementary**: it
does not re-attack those two inputs; it explains why **other sectors leave `r=1/2`** (color/Majorana push off the
fixed point) and why the **charged-colorless** sector is the one with no net push. The symmetric-lane occupancy of
the charged leptons is here re-read as "the unique sector whose gauge structure weights neither generation block"
= the swap fixed point.

## What this note does and does NOT claim
- **DOES:** establish (i) the clean four-sector correlation `color/charge ⟷ lane`; (ii) the structural fact that
  net triality lives on the C₃-doublet and colorless on the C₃-singlet (Z₃-center = C₃); (iii) the *direction* of
  the color→hierarchy and neutrality→degenerate shifts; (iv) the U(1)_em-blindness reconciliation pinning
  charged-colorless at `r=1/2`; (v) the swap-partner (hierarchy↔degenerate reflection) structure.
- **Does NOT:** derive the coupling magnitudes, the up/down split, the exact `r` values, or the *sign* of the color
  coupling from dynamics; does NOT close the single-sector `r=1/2` gate (K-reality / block-counting); does NOT
  consume PDG values as derivation inputs (observed `Q` is labelled observational comparison only); does NOT
  promote any sibling claim or set any audit status; does NOT depend on the staggered-Dirac realization gate.

## Stale-citation flags (verify against the live ledger before citing as load-bearing)
- `FLAVOR_BOTH_READINGS_CHARGE_SELECTS_NOTE_2026-05-30` (the det_C/det_R **sector ordering** leptons<down<up<rank-1;
  the gauge-U(1) generation-blindness finding this note reuses for the symmetric-lane reconciliation).
- `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02` (the single-sector two-input reduction this note is
  orthogonal to: K-reality + block-counting-vs-Born).
- `FLAVOR_R_HALF_IS_THE_RECORDS_FLOW_SEPARATRIX_2026-06-02` (r=1/2 = unstable separatrix; the swap fixed-point reading).
- `LHCM_MATTER_ASSIGNMENT_SU3_BLOCK_REPRESENTATION_NARROW_THEOREM_NOTE_2026-05-17` (color lives on Sym²; colorless
  on Anti² — the block-carrier substrate for "color = doublet, colorless = singlet").
- `CL3_TASTE_GENERATION_THEOREM` (the hw=1 C₃ generation orbit; Z₃ cyclic structure).
- `FLAVOR_ASYMMETRY_2OVER9_FORCED_WEIGHT_2026-05-31` (the C₃ regular-rep singlet/trace-free decomposition).
- `koide_c3_generator_rephasing_obstruction` (retained); `koide_emergent_time_eta_conjugation_parity` (retained_bounded).
The candidate Record axiom is axiom-update-provisional; this note's dial framing inherits that provisionality.
