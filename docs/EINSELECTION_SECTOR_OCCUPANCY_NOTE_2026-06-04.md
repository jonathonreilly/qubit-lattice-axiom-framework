# Einselection (angle C): the dial's STABLE SETTINGS + their ordering are derived; the per-sector OCCUPANCY (which setting each fermion sector sits at) stays a per-sector physical INPUT, with the color/generation discriminator identified as the open promotion path

**Date:** 2026-06-04
**Claim type:** meta
**Claim boundary:** a cross-sector reframe of the Koide `r` gate. NOT a derivation of `r=1/2` and NOT a
claim that the occupancy is forced. It establishes (i) that einselection + the C₃-charge/position/degenerate
trichotomy derive the three stable dial settings and their ordering, and (ii) that the gauge-coupling
discriminator reproduces the *observed* sector ordering but is itself not derivable from A1+A2+retained
(the color↔generation bridge it needs is an open gate). Verdict: **OCCUPANCY-IS-PER-SECTOR-INPUT** (with a
derived stability + ordering skeleton).
**Runner:** `scripts/einselection_sector_occupancy_2026_06_04.py` (SCORECARD 26/26).
**Cache:** `logs/runner-cache/einselection_sector_occupancy_2026_06_04.txt`.

## The question (angle C of the einselection campaign)

We do **not** force `r=1/2`. The C₃-equivariant circulant mass operator `H = aI + bC + b̄C²` on the `hw=1`
generation carrier has a one-parameter family of Koide values `Q(r) = (1+2r)/3`, `r = |b|²/a²`. Prior work
(`FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02`, `KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31`)
established that **einselection fixes which basis is monitored** — i.e. which partition is the pointer — and
that the three natural pointer settings are stable. The *single-sector* question ("what fixes `r=1/2` for
charged leptons") was reduced there to two physical inputs (K-reality + the block-counting-vs-Born measure).

This note asks the **cross-sector** question those predecessors did not: the observed sectors sit at
*different* settings —

| sector | observed `Q` | observed `r = (3Q−1)/2` | dial region |
|---|---|---|---|
| charged leptons | 0.66666 | 0.5000 | `= 1/2` |
| down quarks | 0.73143 | 0.5971 | `> 1/2` |
| up quarks | 0.84898 | 0.7735 | `> 1/2` |
| neutrinos (NO) | 0.58569 | 0.3785 | `< 1/2` |

— so **what determines which stable setting each sector einselects?** (PDG central masses; used only as a
labelled observational comparison, never as derivation input.)

## The mechanism tested

A sector einselects the pointer basis its record-forming environment **monitors**. The three settings are
the three monitored observables:

- monitor the **C₃-charge** (the gauge-invariant "which generation", the K-real central pointer
  `S = C+C² = J−I`, spectrum `{2,−1,−1}`, two record atoms counted **equally**) → equal-power-per-block
  (`det_C`) → `r=1/2` → `Q=2/3`.
- monitor real-space **position** (the *same* two blocks weighted by **dimension/rank** `(1,2)`, the Born
  `I/3` pushforward) → `det_R` → `r=1` → `Q=1`.
- **degenerate** monitoring (no sharp generation record; neutral/Majorana floor) → below the 2-block
  stationary point → `r<1/2`.

**Discriminator** (which basis does a sector's environment monitor?): the sector's **gauge coupling**.
- charged leptons: **colorless**, integer-charge, no spatial generation spread → the environment monitors
  the clean gauge-invariant C₃-charge → C₃-eigenbasis einselected → `r=1/2`.
- quarks: **colored** → the generation index is entangled with color (confinement / color flux spreads it
  over space) → the environment monitors a color–position *mixture*, not the pure C₃-charge → off `r=1/2`
  (`r>1/2`).
- neutrinos: **neutral** (Majorana candidate) → the gauge environment monitors nothing sharp on the
  generation index → degenerate floor → `r<1/2`.

## Verdict: OCCUPANCY-IS-PER-SECTOR-INPUT (with a DERIVED stability + ordering skeleton)

### DERIVED — the stable settings and their ordering
The three settings are genuine, distinct, ordered fixed points of the C₃ algebra (runner Parts 1–2):
`Q(r)` is strictly monotone (setting↔value is a bijection); `r=1/2` is the **unique** equal-power-per-block
point (`3a² = 6|b|²`) and the maximum of the binary C₃-charge-atom-share entropy (so the charge-monitored
setting is stable at `r=1/2`); `r=1` is the dimension/Born extremum (the doublet eigenvalue `1−b` vanishes,
a massless doublet); `r<1/2` is the sub-stationary degenerate floor. The C₃-charge pointer `S` commutes with
the C₃ shift, so it really is the **gauge-invariant** record; and reaching the `r=0` three-mode setting
requires the **K-odd** observable `A = i(C−C²)`, so a K-real (position/time-reversal-even) environment can
only land on `{charge, position, degenerate}` — exactly the three settings. **The degenerate < charge <
position-mixed ordering reproduces the observed `neutrino < lepton(=1/2) < down < up` ordering** (runner
Part 4), and the discriminator is **falsifiable**: charged leptons hit `r=1/2` to `10⁻⁵` (sharp, not
tautological) while quarks sit clearly above.

### INPUT — the occupancy (which sector couples to which environment) is NOT forced
The assignment is **not derivable from A1+A2+retained** (runner Part 5):
1. **The color↔generation coupling the discriminator needs is an open gate.** The `SU(3)_c` center `Z₃` on
   the fundamental color triplet has character `(3, 3ω, 3ω²)` — **not** the regular `(3,0,0)` of the
   generation C₃ (`Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10`). So "colored ⇒
   generation entangled with color/position" is an **imported bridge**, not a theorem.
2. **Einselection itself is a no-op on the value.** `H` is block-diagonal in `{P₀,P₁}` for *every* `r`
   (`‖P₀HP₁‖ ~ 10⁻¹⁶` at all observed `r`), so the pointer map places **zero** constraint on the
   inter-block power ratio — it cannot pick the environment or the value by itself.
3. **The partition selector is sector-blind.** K-reality (which selects the 2-block partition) holds
   identically at `r=1/2, 0.60, 0.77, 1` — it carries **no** sector-discriminating information.

So einselection explains the **stability** of the settings and an **ordering-consistent** discriminator, but
the **occupancy** — which environment each sector couples to — remains a per-sector physical input. The
discriminator is ordering-consistent and in-principle physical (it reproduces all four sectors' observed
bands), but it is a phenomenological *reading*, not a derivation.

## No-overreach statement
- The dial values `{2/3, 1, 1/3}` are derived from the C₃ algebra (Parts 1–2); observed `Q` entered **only**
  as Part-4 labels, never as a derivation input.
- We do **not** claim occupancy is derived. We identify exactly what would close it (a *derived*
  color/generation coupling — the regular-character bridge), verify that bridge does **not** currently hold,
  and therefore correctly decline to assert derivation.
- Honest caveat on robustness: the up-quark `r>1/2` is solid under ±30% mass-scheme variation; the
  **down-quark is marginal** (worst case `r ~ 0.50`, stays above 1/2 but only just). The qualitative
  ordering is robust; the down-quark band membership is not strongly so.

## The next paths this opens (not closing)
- **Promote the discriminator:** derive the color↔generation coupling (the open `Z₃` regular-character
  bridge) from retained structure. If that closed, the colored→position-mixed leg would be forced and
  occupancy would become derived.
- **Sharpen the colorless leg:** show that a colorless-charged sector's record-forming environment monitors
  *only* the gauge-invariant C₃-charge (no position channel), which would pin the lepton leg at `r=1/2`
  independently of the color bridge.
- **Neutrino leg:** connect the "neutral ⇒ degenerate floor" reading to a Majorana/seesaw record structure
  that predicts the observed `r<1/2` quantitatively rather than only its sign.

## Provenance (verified 2026-06-04)
- `Q(r)=(1+2r)/3` monotone; `eig(C+C²)={2,−1,−1}`; `eig(i(C−C²))={0,±√3}`; equal-power `3a²=6|b|²` at
  `r=1/2`; doublet eigenvalue `1−b→0` at `r=1`; argmax atom-share entropy `=1/2`; `‖P₀HP₁‖~10⁻¹⁶` for all
  observed `r`; `SU(3)_c` center char `(3,3ω,3ω²)≠(3,0,0)`: verified directly (runner 26/26).
- PDG central masses (charged leptons, up/down quarks, neutrino Δm² NO/IO) used only as labelled
  observational comparison.
- Anchors: `FLAVOR_EINSELECTION_2SECTOR_MODULO_KREALITY_2026-06-02` (the single-sector predecessor),
  `KOIDE_POINTER_RECORD_DEGENERACY_D3_NOTE_2026-05-31`, `Z3_CHARACTER_ISOMORPHISM_COLOR_GENERATION_OPEN_GATE_NOTE_2026-05-10`
  (open gate — the discriminator's missing premise), `KOIDE_FROBENIUS_ISOTYPE_SPLIT_UNIQUENESS_NOTE_2026-04-21`.
- This is a meta/reframe note (no audit-ledger action, no new primitive, no import). It does not load-bear on
  `closure_c_staggered_dirac_gate` or any retained closure; it sharpens the *cross-sector occupancy* layer of
  the Koide `r` gate and names its promotion path.
