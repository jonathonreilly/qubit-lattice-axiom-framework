# Item 7 — the T_phys = 4 wrap-artifact re-read

Ground truth used, in order of authority:
1. `docs/ADMISSIBILITY_DIRAC_KAHLER_SCALING_PROBE_BOUNDED_THEOREM_NOTE_2026-08-21.md`
   (b165) — the wrap-mechanism section (N4, lines 240–300) and the
   structural/accidental split (lines 344–371).
2. `$S/block169_findings.md` (b169) — the **delta-parity liveness law**, which
   supersedes part of b165's mechanism section (see §C).
NO file edits.

## A. The mechanism, as b165 states it

The site-pairing corner is `herm(R Q[c-1, c+1])`, at time displacement `+2`.
The **ascending** hop path `c-1 -> c -> c+1` uses links `{c-1, c}` — the links
the region **pins** — and alone gives `E = 0`. The **descending** path uses the
**free** links `{c+1, c+2}` and lands at displacement `-2`. At `T_phys = 4`,
`2 = -2 (mod 4)`, so both land in the same block and free-link content leaks in.

| | 8x4 (T=4) | 8x6 (T=4) | 12x4 (T=6) | 16x4 (T=8) |
|---|---|---|---|---|
| free-link leakage into `Q[c-1,c+1]` | 32/32 | 32/32 | **0/48** | **0/64** |
| `E` live, x-trivial region cells | 32/64 | 32/64 | **0/96** | **0/128** |
| `E` live, non-x-trivial | 40/80 | 56/112 | **0/120** | **0/160** |
| corner `= s_t E`, `E` traceless | yes | yes | yes | yes |
| `E` a pure form in the FREE shears | yes | yes | yes | yes |

The `T_phys = 8` point is the checker's discriminator and is what kills the
"divisible by 4" and "small lattice" confounds. **"The tracelessness was never
the accident. The corner was."**

## B. Exposure table

| note | claim | distance-2 at T=4? | status | reason |
|---|---|---|---|---|
| b163 site_reflection_channel | **W1-163 wall**: at `s_t != 0` the mass is annihilated hyperbolically because the reflection sends slice `c+1` to time distance 2 | yes | **wrap-safe** | rests on E2 (below), which b165 re-verified at T=4/6/8; the wall is about where the MASS can reach, not where the connection leaks |
| b163 | **E2, one-line theorem** (note l.138–146): the only cover-Hodge off-diagonal is the `b`-term at time displacement `±1`, so `H_q` has displacements `{0,±1}` and *the mass never reaches time distance 2, on any carrier* | yes | **wrap-safe** | b165 measured the support at three sizes — `{0,1,3}` at T=4, `{0,1,5}` at T=6, `{0,1,7}` at T=8; at T=4 the `3` is `-1` mod 4, correctly read as ±1. Displacement 2 would require `T_phys <= 3`. Structural, dimension-free |
| b163 | E2's rider: *"the 16 distance-2 entries of the action are pure connection and vanish both at `s_t = 0` and at zero carrier shear"* | yes | **wrap-safe** | both vanishing conditions are carrier/connection conditions, not wrap conditions; b165's `E` is precisely the pure-free-shear form and is zero at either condition at every size |
| b163 | **M1 hyperbolic annihilation** — mechanism: the `(c+1,c+1)` block is mass-free, `P = [[B,C],[C*,0]]`, whole mass inside `B` | yes | **wrap-safe** | the mass-freeness is E2, structural. The *hollowness on flat carriers* also survives, because `E` is a pure form in the shears and a flat carrier has none |
| b163 | M1's **numerals**: `det C` a rational multiple of `s_t^4` in 376 of 384 flat cells, 8 vanishing cells on healed edge `(1,2)`, inertia `(4,0,4)` at every mass, census `{(4,0,4): 2256, (2,4,2): 48}` | yes | **already-scoped** | fixture counts, stated at the 8x4 bench and nowhere wider; b165's C-branch result (`dC/ds_t != 0` on every region cell of every fixture, zero exceptions) is the size-independent replacement and it agrees |
| b163 | M2 antipodal sign, mass-only inertia `(4,4,4)`, 48/48 | no | **wrap-safe** | closed OS region `{c,c+1,c+2}`; the antiperiodic minus is a lift sign, not a distance-2 congruence |
| b163 | **N4 the live `s_t = 0` PSD region** and its witness `diag(1,1,1,1,0,0,0,0)` at `(4,4,0)` | no | **wrap-safe** | at `s_t = 0` the corner is `s_t E = 0` identically, so there is no distance-2 connection content to contaminate |
| b164 zero_shear_region | **N1 block theorem at `s_t = 0`**: `(c+1,c+1)` block identically zero 384/384 *"because nothing reaches time distance 2 there"* (l.91–93) | yes (the reasoning cites distance 2) | **wrap-safe** | the citation is to E2 — the *mass* cannot reach distance 2 — combined with `s_t = 0` killing the connection. Neither leg is the wrap |
| b164 | **N2 the criterion**: PSD and mass-carrying ⟺ x-trivial, `m > 0`, shear vanishes on the two links incident to `c` | no | **wrap-safe** | proved at `s_t = 0`; b165 re-derived the site-class criterion as STRUCTURAL and the region dimension law `2 L_x (T_phys - 1)` = 24/40/36/56 at four sizes |
| b164 | N2 verification: 8064/8064 cells, 0 disagreements, 448 PSD all at `(4,4,0)` | no | **already-scoped** | 8x4 fixture counts; note's own `claim_scope` opens "on the committed four-chart shear atlas **over the 8x4 antiperiodic cover**" |
| b164 | **N6 connection theorem, BRANCH 1**: *"where `E` is nonzero — exactly the odd fixed slices, 32 of 64 region cells, matching the checker's 192 of 384 corner count — a nonzero traceless symmetric block is indefinite, so `P` fails PSD for either sign of `s_t`"* | **yes** | **WRAP-EXPOSED** | this is the confirmed artifact. `E`'s liveness is exactly the `2 = -2 (mod 4)` free-link leakage; at T=6 and T=8 branch 1 is **empty** (0/96, 0/128 x-trivial; 0/120, 0/160 non-x-trivial). The 32-of-64 / 192-of-384 counts are 8x4-only and do not generalise |
| b164 | **N6, the two-branch fence as a whole** (*"TWO BRANCHES, both exhibited … branch 2 closes every cell branch 1 does not"*) | yes | **already-scoped — and this is what saves the note** | b165 adjudicated explicitly: *"the two-branch fence saves it. NO CORRECTION-IN-SUCCESSOR is owed and none is proposed"*, and gated that against b164's own text. At `T_phys >= 6` branch 1 is empty and branch 2 covers every cell, so the **verdict** ("nothing survives switching `s_t` on") is size-independent even though branch 1's population is not |
| b164 | N6: *"the corner is exactly `s_t E` with `E` traceless in 64 of 64 and a pure form in the free shears in 64 of 64"* | yes | **wrap-safe** *(but see §C)* | tracelessness and the pure-free-shear form hold at all four b165 sizes — yes/yes/yes/yes. Only the *liveness* was the accident |
| b164 | N6: *"`C` is exactly `s_t C1` with `C1` nonzero in 64 of 64"* | no | **wrap-safe** | b165 promoted this to the size-independent obstruction: `dC/ds_t` nonzero on every region cell of every fixture, **zero exceptions** |
| b164 | N6 riders: `dB/ds_t = 0` in 64/64 (mass block is `s_t`-blind); exact affine-linearity of `P` in `s_t`, 384/384 | no | **wrap-safe** | affine-linearity is structural — every healed differential entry is bi-homogeneous of degree 1 in `(s_t, s_x)` at every size |
| b165 scaling_probe | **The wrap-artifact theorem itself** (E live at T=4, dead at T=6 and T=8) | yes, by construction | **wrap-safe** | it is the diagnosis, closed at three `T_phys` values with the `T ≡ 0 mod 4` and `T` small confounds excluded by the checker's independently-built 16x4 run |
| b165 | **Gate `P5d`**: distance-2 content "never reaches beyond `{c-1,c} ∪ {c+1,c+2}`", reported passing at 8x4, 12x4, 8x6 | yes | **already-scoped (self-disclosed vacuity)** | b165 quotes then corrects it: mod 4 those four residues are the **whole** time lattice, so the gate **cannot fail** at 8x4 or 8x6. Reported as one datum at `T_phys >= 6`, not three |
| b165 | *"The distance-2 block of `Q` is nonzero **exactly on the odd fixed slices**"* | yes | **wrap-safe** | STRUCTURAL — staggered cell parity, verified at every size and every swept edge, dimension-free |
| b165 | *"At `T_phys >= 6` … `E` vanishes on **every** cell — x-trivial and non-x-trivial alike. The wrap coincidence is the whole story of the 8x4 `E != 0`"* | yes | **wrap-safe as measured, but NOW SCOPE-AMENDED by b169** | see §C |
| b165 | The `{1: (1,), 3: (3,)}` content print computed from one edge | yes | **already-scoped** | b165 discloses it as a thin print; the all-edge content is `{c-1, c}`, reproduced under `--deep` at T=6 and T=8 |

## C. The b169 amendment to b165's mechanism section

b169 (`block169_solve.py`, 74/74 gates, symbolic) proves a **GENERAL-`T` INDEX
THEOREM** for the corner of a *link* pairing (odd `p_t`), with
`delta := p_t - 2c - 1`:

> `C_link` is live **iff** `(delta - 1) mod T ∈ {0, 1, T-1}`, i.e.
> `delta mod T ∈ {0, 2}` for even `T` and `{0,1,2}` for odd `T`.
> Measured live counts `4, 3, 4, 3, 4` at `T = 4,5,6,7,8` — the formula matches
> at every `T`.

Two consequences for the wrap re-read:

1. **"Live at T=4, dead at T>=6" is NOT a general law about distance-2 corners.**
   It is the *site-reflection* instance of the delta-parity law. b169's committed
   table exhibits **live corners at `T_phys = 6`** — `12x4`, `p_t ∈ {5, 11}`,
   `delta = 2` — where the corner is live and the block is closed instead by the
   **zero-block lemma**. So b165's sentence *"the wrap coincidence is the whole
   story"* is true within its quantification (SITE reflections, committed `d1`,
   scalar temporal coupling — the same quantification b169 records for the
   audited closure) and **must not be read as a lane-wide statement**.
2. **The tracelessness half does not generalise either.** b169 gate C2: *all 4
   of 4 live committed link corners are NOT traceless*, and they are
   carrier-, `s_t`-, `s_x`- and holonomy-sensitive — genuine transport-carrying
   corners. So the b164 sentence "a nonzero traceless symmetric block is
   indefinite" is a theorem about the site corner only. b169 states this as a
   real correction to the *stated mechanism* of the closure, while the closure's
   *verdict* survives (staggered-alternation theorem in the `B` slot, plus the
   zero-block lemma).

**Upgraded wrap test.** b165's cheap wall was *"does `+2` stop being the same
block as `-2`?"* The b169-corrected wall is stronger and subsumes it: **does the
reflection's image `theta(c+1)` land on a PINNED link or a FREE one?** At
`T_phys = 4` the answer flips for site reflections because `2 = -2`; at
`T_phys >= 6` it can still be "free" for link reflections at `delta ≡ 2`.

## D. Provenance defect found in b165's own handoff wording

b165 N7 (line 423) names the re-read target as **"Block 163's E3
time-distance-2 entries"**. There is **no `E3` label** in either the landed
b163 note (`docs/ADMISSIBILITY_DIRAC_KAHLER_SITE_REFLECTION_CHANNEL_BOUNDED_THEOREM_NOTE_2026-08-21.md`
— its only E-label is `E2` at line 138) or the b163 runner
(`scripts/admissibility_dirac_kahler_site_reflection_channel_2026_08_21.py`
— `grep 'E3'` returns nothing). The referent is almost certainly b163's **E2**
one-line theorem plus the M1 distance-2 statements in N3, both classified above.
Documentation-only; it changes no verdict, but a follow-up pass chasing "E3"
will not find it.

## VERDICT

**One genuine wrap-exposed statement**, and it was already known and already
fenced: b164's **branch-1 population** — "`E` nonzero on exactly the odd fixed
slices, 32 of 64 region cells / 192 of 384" — is pure `2 = -2 (mod 4)`
free-link leakage and is empty at `T_phys = 6` and `8`. It is contained by
b164's own two-branch fence, which b165 gated against b164's text and
adjudicated as owing no correction; branch 2 closes every cell branch 1 does
not, so no landed **verdict** anywhere in b163/b164 is wrong. Everything else in
the two landed notes that touches time distance 2 is either **structural** (E2's
displacement support `{0,±1}`, the odd-slice support of the distance-2 block,
the `C`-branch `dC/ds_t != 0`, affine-linearity in `s_t`, the tracelessness and
pure-free-shear form of `E`) or **already fixture-scoped** in the note's own
`claim_scope`/bench language — the 8064-cell, 376/384 and 448-PSD counts are
stated at the 8x4 bench and nowhere wider, so they are safe as written and are
not flagged. b165's `P5d` vacuity is self-disclosed. The one thing that *is* new
since b165 wrote its mechanism section is b169's delta-parity liveness law: it
does not overturn a single landed numeral, but it demotes "T_phys = 4" from
*the* explanation of a live distance-2 corner to *one case* of a general index
condition, and it removes tracelessness from the general mechanism entirely.
Any successor that leans on "distance-2 corners are dead at `T_phys >= 6`"
outside the site-reflection/`d1` quantification is now wrong, and that is the
only live hazard this re-read leaves open.
