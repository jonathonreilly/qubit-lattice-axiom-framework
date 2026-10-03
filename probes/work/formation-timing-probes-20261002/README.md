# Formation-timing probes (2026-10-02, owner clause walk-through)

Status: exploratory probe on a supplied toy model. This is backlog material. It is not a landed claim, and it makes no physical reading.

> **Correction (2026-10-02 23:15, campaign 8).** The `own` menu rule used in B2 and D is a signalling rule. In it, the menu axis is the axis of the site's own reduced state, which is a nonlinear function of shared, steerable possibilities. A distant record's menu choice then changes the local record statistics.
>
> - Evidence: A9 Theorem 2(d), and the coordinator's independent check `campaign8-tick-moving-records-20261002/toys/verify_menu_signalling.py`. In that check the total-variation distance is 1.0 for an x–b singlet and 1.0 at most over 400 random states. The recorded-neighbour (`field`) rule stays at 3.6e-16.
> - Treat the `own` columns as an illustration of a non-physical rule only.
> - The `fixed` and `field` results stand.
> - **Revised after the campaign-8 hostile review (A16, 2026-10-02 23:45): Q7 stands.**
>   - Under straight-average rules, unrecorded neighbours may shape the odds, and with them the menu's support.
>   - What signals is taking the menu's frame (which possibilities can be locked) as a nonlinear function of unrecorded possibilities.
>   - Proposed clarification (not approved): "Recorded neighbours may set which possibilities are on offer; unrecorded possibilities shape the odds over them only as a fixed weighted average."

## The question

The owner asked, during the one-clause walk-through, whether records across the universe form on one shared tick or whether each site forms its record at its own random time. Time would still be the accumulation of records either way. A second part asked whether the answer is about the local neighbourhood or the whole universe.

The owner added a point: "when the record forms does matter because the past sets the neighborhood conditions".

The Campaign 7 package leaves four things outside the clause: the preparation, the formation schedule, the menu rule, and γ/J (see `campaign7-hard-panel-20261001/final/DECISION_DOCUMENT.md`). These probes ask which of those open timing choices leave a mark in the records. Formation times themselves are not recorded, so any mark has to show up in record contents.

## Toy model

Every part of the model is supplied for this probe. None of it is derived.

- **Sites and shared possibilities.** There are N qubit sites on a ring. The sites with no record share one joint pure state, which plays the role of their shared possibilities.
- **Preparation.** The preparation is the ground state of the ring coupling J Σ σ_j·σ_{j+1}, with J = 1. In this state every undecided site has equal odds for every menu. The state does not change until the first record forms.
- **Change between records.** Between records the state evolves by exp(−iHt) with the same coupling. A recorded site is locked. Its bonds therefore act on each unrecorded neighbour as a steady push, J n_k·σ_j, where n_k is the locked possibility (the setting called "push"). In the variant called "drop", the recorded site simply leaves the change.
- **Formation.** A record forms on a two-outcome menu with axis m. The odds are (1 ± m·r_j)/2, where r_j is the site's own part. The shared possibilities are then compressed to agree with the outcome, and the record content is ±m.
- **Menu rules.** Three rules are compared:
  - `fixed`: the menu axis is z at every site.
  - `own`: the menu axis is the axis of the site's own part, chosen at random if the site is undecided.
  - `field`: the menu axis is the direction of the summed contents of the recorded neighbours, chosen at random if there are none.
- **Simultaneous formation.** When several sites form at once, every menu is set before any of them forms, and the joint odds follow the Born rule.

Scripts: `timing_probes.py` (probes A, B1, B2, C, D) and `timing_probe_b1_short.py` (probe B1′). Logs are in `probe*.log`.

## Results

### A — Two neighbours: forming at once vs one right after the other (exact, N = 8 and 10)

1. **Fixed menu, nothing in between.** The joint record pattern is identical either way. The total-variation distance is 3e-17.
   - The first record does change the second's odds. The pattern of pairs is still the same.
   - Analogy: drawing two cards one at a time vs both at once.
2. **Fixed menu, with a gap of change in between.** The pattern can be read. Neighbour correlations for N = 8, against −0.609 when both form at once:

   | Gap (1/J) | Push | Drop |
   |---|---|---|
   | 0.3 | −0.643 | −0.450 |
   | 1 | −0.763 | −0.267 |

3. **Order alone.** Reversing which neighbour forms first, with the same gap, changes nothing to 1e-13. This setup is mirror- and flip-symmetric.
4. **Own-state menu, no gap.** Here "at once" and "one after the other" can be told apart.
   - One after the other: the second record forms on the first one's axis. Every pair is aligned, and the content correlation is c = −0.609.
   - At once: the axes are unrelated. No pair is aligned, and the correlation is c/3 = −0.20 (sampled −0.2018).

### B1 / B1′ — How far "when" reaches (exact, N = 12)

B1 uses the ground-state preparation, in which every site is linked to every other.
- Site 0 forms early, and the change runs for a gap g before site d forms. The difference from forming at once grows like g² at every distance.
- The size of the effect is set by the existing links. For example, at g = 0.1:

  | d | TV |
  |---|---|
  | 1 | 0.0012 |
  | 2 | 0.0062 |
  | 4 | 0.0013 |
  | 6 | 0.0008 |

- Reversing the order changes nothing (TV ~ 1e-14, by symmetry).

B1′ uses partner-only links: an equal mixture of the two singlet-pair coverings. Both schedules end at time g.
- Records reached through a partner link plus one bond of change feel the early record at order g², with TV ≈ 0.008 at g = 0.1 for d = 2 and 3.
- Records farther out are strongly suppressed, about 100× below the ground-state case:

  | d | TV at g = 0.1 |
  |---|---|
  | 4 | 1e-5 |
  | 6 | 1e-5 |

- So the reach of "when" is the links already present in the shared possibilities, plus the distance the change carries during the gap.

### B2 — Universe-wide tick vs local timing (Monte Carlo, N = 8)

Setup: 8000 histories per schedule. Every schedule has the same mean wait of 1/J per site. The five schedules are:

| Schedule | Timing rule |
|---|---|
| Universe-wide ticks | Every site shares one tick train; at each tick an unrecorded site forms with probability ½ |
| Patch ticks | Each half of the ring shares its own tick train, with independent phases |
| Own ticks | Each site has its own tick train, with the same per-site waiting law and independent phases |
| Poisson | Random times |
| All at once | Every site forms on a single tick |

**Fixed menu.** c_r is the record correlation at distance r. Errors are ±1 SE.

| Schedule | c1 | c2 | c3 | c4 |
|---|---|---|---|---|
| Universe-wide ticks | −0.614(4) | +0.287(6) | −0.260(6) | +0.175(8) |
| Patch ticks | −0.626(4) | +0.312(6) | −0.290(6) | +0.209(8) |
| Own ticks | −0.630(4) | +0.313(6) | −0.284(6) | +0.201(8) |
| Poisson | −0.636(4) | +0.330(6) | −0.307(6) | +0.227(8) |
| All at once (= preparation) | −0.612(3) | +0.267(6) | −0.256(6) | +0.203(8) |

**Menus set by the conditions.** The three readouts are:
- v1: the neighbour content correlation.
- a1: the fraction of neighbour pairs whose records share an axis.
- naxes: the number of distinct axes among the 8 records.

| Schedule | own: v1 | own: a1 | own: naxes | field: v1 | field: a1 | field: naxes |
|---|---|---|---|---|---|---|
| Universe-wide ticks | −0.510(3) | 0.031(2) | 7.76 | −0.459(3) | 0.190(2) | 6.48 |
| Patch ticks | −0.596(3) | 0.265(5) | 6.13 | −0.496(3) | 0.248(2) | 6.01 |
| Own ticks | −0.635(4) | 1 | 1 | −0.609(3) | 0.334(2) | 5.13 |
| Poisson | −0.631(4) | 1 | 1 | −0.607(3) | 0.335(2) | 5.13 |
| All at once | −0.200(2) | 0 | 8 | −0.202(2) | 0 | 8 |

**Readings**

1. **A per-site metronome looks like pure randomness.** Own ticks match Poisson under all three menu rules. The fixed-menu gaps between them are at most 2.5 SE, and the two schedules have different waiting-time laws.
2. **Shared ticks leave a mark.** What carries the mark is exact coincidence of formation between linked sites.
   - Fixed menu: the mark is small. Universe-wide ticks against own ticks differ by Δc1 = 0.016 ± 0.005, and Δc2 through Δc4 are each about 0.025 ± 0.01. Batched formations copy more of the starting web.
   - Menu set by the conditions: the mark is large. Records that form together do not share frames. Under the own-state menu, 3% of neighbour pairs are aligned with universe-wide ticks, against 100% with own ticks.
3. **Neighbourhood-wide against universe-wide ticks is not settled at this size.** At N = 8 every bond sits next to a patch seam, so this size cannot separate the two. B1 and B1′ say the difference should be confined to the seams, where two neighbourhoods' ticks disagree.

### C — Pace (Monte Carlo, N = 8)

Setup: Poisson times, fixed menu, 8000 histories per pace. The preparation's own correlations, c1 through c4, are −0.6085, +0.261, −0.2519 and +0.1988.

| Mean wait (1/J) | Push: c1 | Push: c2 | Push: c4 | Drop: c1 | Drop: c2 | Drop: c4 |
|---|---|---|---|---|---|---|
| 0.03 | −0.610(3) | +0.265(6) | +0.196(8) | −0.606(3) | +0.256(6) | +0.203(8) |
| 0.1 | −0.618(3) | +0.274(6) | +0.203(8) | −0.595(3) | +0.237(6) | +0.183(8) |
| 0.3 | −0.617(4) | +0.286(6) | +0.197(8) | −0.544(4) | +0.166(6) | +0.130(7) |
| 1 | −0.632(4) | +0.320(6) | +0.206(8) | −0.419(4) | +0.022(5) | +0.039(7) |
| 3 | −0.650(4) | +0.352(6) | +0.243(8) | −0.362(4) | −0.024(5) | −0.013(7) |
| 10 | −0.657(4) | +0.365(6) | +0.256(8) | −0.353(4) | −0.032(5) | −0.023(7) |

**Readings**

1. **Pace is a readable dial.**
   - Fast formation: the records copy the starting web.
   - Slow formation: the records settle into a different pattern.
2. **The push/drop choice decides which way slow formation moves.**
   - Push: the locked records keep acting and build more order, with c1 reaching −0.66.
   - Drop: the starting web washes out, with c1 reaching −0.35 and c2 about 0.
3. **No Zeno freezing.** Zeno freezing needs repeated looks at the same site, and the one-record-per-site rule excludes that. Fast formation simply copies the starting web.

### D — Triggered formation (Monte Carlo, N = 8)

Setup: an unrecorded site forms at rate γ0 + γ1·(number of recorded neighbours). Each trigger strength is calibrated so the mean per-site time stays at 1/J, and each run uses 8000 histories. The mean time gap between neighbouring formations is 1.0/J with no trigger, 0.48/J at 3× and 0.16/J at 30×.

| Trigger | fixed: c1 | fixed: c4 | field: a1 | field: naxes | own: a1 |
|---|---|---|---|---|---|
| 0× (independent) | −0.637(3) | +0.201(8) | 0.332(2) | 5.14 | 1 |
| 3× | −0.645(4) | +0.224(8) | 0.536(3) | 3.49 | 1 |
| 30× | −0.649(3) | +0.240(8) | 0.824(2) | 1.80 | 1 |

**Readings**

1. **Fixed menu.** The mark is small. Between 0× and 30× the record correlations shift by 0.01 to 0.04, at 2 to 3.4 SE.
2. **Menu set by the recorded neighbours.** The mark is large. Triggered records grow outward from a few seeds and form large aligned patches: 82% of neighbour pairs are aligned with 1.8 distinct axes, against 33% and 5.1 without triggering.
3. **Own-state menu.** There is no mark. On this preparation the first record already sets the axis for every site.

## What the probes say (toy-model level)

1. **No change and a fixed menu: "when" is invisible.** If nothing shifts between records and the menu is fixed, the order and simultaneity of formation leave no mark at all. This holds exactly, because compressions at different sites commute.
   - "The past sets the conditions" is real here: an earlier record changes the odds of later ones.
   - But it adds nothing beyond the links the shared possibilities already carried.
2. **"When" becomes readable in two ways only:**
   - Through the change that happens between records. This covers gaps, pace (a real dial) and triggering.
   - Through menus that are set by records already formed. Here "at once" and "in sequence" can be told apart even with no gap.
3. **Per-site timing looks like pure randomness.** A per-site metronome cannot be told apart from random times. What can be read is exact coincidence of formation between linked sites, and how much change occurs between linked formations.
4. **Reach.** The timing of a record matters as far as the existing links in the shared possibilities extend, plus the distance the change carries during the gap. Far-apart, unlinked records have no readable order, which is relativity-like.
5. **The timing choice is coupled to other open choices.** It depends on the menu rule and on how a locked record acts on the change between records (push or drop). The package leaves both open.

The next owner question these probes raise: is the menu of a forming site set by its conditions, including recorded neighbours, or is it fixed? Admissibility's support/menu reading bears on this; it is not decided here.

## Caveats

- Rings are small (N = 8 to 12), and the change crosses the whole ring in about 1/J.
- The Monte Carlo figures carry statistical errors, quoted as one standard error. Nothing here is certified.
- The preparation, the coupling, the push/drop treatment of locked sites, and the three menu rules are all supplied choices.
