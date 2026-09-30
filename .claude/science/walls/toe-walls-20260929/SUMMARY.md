# TOE walls, 2026-09-29 — plain summary

Claude Opus 5.5 supervised; Claude Sonnet 5.5 ran the probes, attacks and kill checks. They are the same vendor family, so these checks are not independent refereeing. Nothing here is audited. `WALLS.md` has the full table.

## What was done

- **Probes.** Sixteen lane probes, one per lane, read the repository and logged every place a lane is stuck. They found 179 walls. Many were the same wall seen from different lanes, and merging those leaves 81 distinct walls: 33 blocking, 47 major and 1 minor.
- **Attacks.** Each distinct wall except the gravity wall got one attack. The attack restated the wall, listed its load-bearing premises, tried two or three routes (at least one from outside physics) and ran a pre-registered test. The gravity wall had its own exercise earlier the same day.
- **Kill checks.** Each attack then got an adversarial kill check.

## The headline

**No wall was passed.** Every wall that did not survive intact turned out to be one of two things:
- **Priced.** It is equivalent to a short list of named premises that nothing derives.
- **Misframed.** It was asking the wrong question.

After the kill checks, the distinct walls come out as:

| Outcome | Walls |
|---|---|
| Priced | 49 |
| Still standing | 22 |
| Misframed | 9 |
| Gravity wall (handled by its exercise) | 1 |

The kill checks rarely confirmed an attack as written. Three were confirmed outright: the down-quark bridge (T46), the weak-scale formula (T31) and the photon (T78). The other 77 came back **weakened**: the main conclusion held, but the attack overclaimed, mislabelled or missed work already in the repository. Several walls moved to "still standing" as a result.

## A few decisions would move most of the walls

Most priced walls share their premises. These are the premises that recur. Each needs an owner decision or a new primitive; none of them is derived.

1. **A wave.** Specifically: a covariant generator for how unrecorded content evolves between records, plus the rule for reading odds.
   - The axioms say plainly that they contain no dynamics.
   - Bell correlations force this ingredient (T08).
   - It moves T02, T08, T09, T15 and T49.
2. **An order for record formation.** This is a measure on which site forms next. It comes with two companions: no neighbouring sites forming at the same moment, and a tie between record ticks and evolution ticks.
   - It moves T01, T11, T16, T73 and the frequency half of T05.
3. **What a record is.** There are three exits, and each costs something new:
   - a record rest energy, or bonds that carry no coherence;
   - a stored supply of records to draw from;
   - collapse "flashes" as in GRW/CSL. The GRW rate still fits current experiments, but the collapse must be weighted by mass (the axioms have no mass) and act on energy bands rather than single sites.

   This choice moves T03, T07 and T10.
4. **More than one plain qubit per site: typed sites carrying extra content.** This is the most frequent price in the whole registry. It appears as:
   - edge qubits under a local constraint, which gives fermions and their minus sign (the repo already built this);
   - link qubits under the ice rule, which gives the photon and Maxwell's equations;
   - several-qubit registers, which give strong-force-type links;
   - a second carrier (gauge content times three flavours), which gives the matter content;
   - two fermion modes per site.

   It moves T15, T18, T19, T20, T25, T27 and T77–T79. It is the Qubit-axiom question again, the same one the gravity campaign ended on.
5. **One grid step equals one time step, for every field.** This gives a single light cone. It moves T14 and T68, and it ties "light bends twice the Newtonian amount" to "gravity waves travel at light speed".
6. **The metric as a degree of freedom (gravity option A).** It moves T64, T67, T70, T71 and T75.
7. **Flavour numbers as data, not derivations.** The registered realized-state primitive already records the flavour settings, orientations and generation splits as data about the actual world, not outputs of the laws.
   - The flavour settings are Koide's r = 1/2 and the lepton/down/up spread.
   - The orientations are the quark and lepton mixing orientations.
   - Several flavour walls were asking to derive something the framework's own primitive classifies as data (T23, T36, T37, T38, T40, T48, T63).

## Walls that still stand

- **The Planck-to-weak-scale bridge (T30–T33).**
  - The chain behind α_s, v and m_t works only if 16 lattice copies stay light all the way down from the Planck scale.
  - The repository's own counts give 2–4 flavours.
  - With the real flavour count, the strong coupling blows up near 6 × 10¹⁴ GeV.
  - Putting the lattice copies into the plaquette average moves the weak-scale formula from 246 GeV to about 214 GeV (4 copies) or about 235 GeV (2 copies). That shift is 100 times the quoted 0.026% match. The kill check confirmed this.
  - The formula's 16th power counts Grassmann modes. One coupling per flavour would give a 4th power, not a 16th.
- **Chirality (T22, T24, T34).** A free local walker always has a mirror twin, and the Higgs doublet waits on this wall.
- **Confinement (T32).** The mass gap of pure glue at β = 6 is unproved. That is a Clay-type problem.
- **Gravity's nonlinear consistency (T66).**
  - The viability map's test A1 was expected to fail, and it *passes* for the lapse–lapse bracket at second order, in reduced 1D and 2D sectors, with range-2 rules.
  - A new planar no-go for the lapse–momentum bracket keeps the wall standing.
- **Black holes (T76).**
  - All count-threshold formation rules give frozen-state counts that grow with volume.
  - The kill check found one symmetric rule outside that class: "form unless exactly two opposite neighbours are recorded". Its frozen count is a Fibonacci number, so its logarithm grows by about 0.48 per unit of side length. That is a boundary law, the first one found, but the count vanishes once a recorded wall is present, and its process entropy is zero.
  - The walker sea's entanglement per area is 0.39–0.46 depending on cut direction, never 1/4 (T74).
- **Others still standing.** Also still standing:
  - the flavour walls T36, T37, T40 and T45, whose numbers are data rather than derivations;
  - strong CP (T43);
  - the dark-matter mass (T55) and cosmic history (T59);
  - the gravity exits (T65), the equivalence principle for composite bodies (T72), and Gauss-pattern formation (T77).
- **The photon (T78).** The electric stiffness holds up to 32³, but almost any smooth local ensemble would show that. A linear photon is not shown; the literature supports it only numerically.

## Errors found in the repository (corrections owed)

- **Route-2 E-centre readout (T47).** About 110 notes rest on it. Its target triple is an artefact of global-spline interpolation. With a local interpolation the readout is trivial at every box size.
- **Down-quark 5/6 bridge (T46, confirmed).** Quoted at a common energy it misses by about 19% (16.5σ). The 0.2% match came from mixing masses quoted at different energies.
- **Sommerfeld factor (T56).** The dark-matter Sommerfeld code has a factor-of-2 error in its argument.
- **Plaquette value (T29).** The licensed value is 0.5934; at large volume it is 0.59372.
- **Sakharov estimate (gravity probe).** The printed coefficient is off by (4π)² from the note's own matching line.
- **Dark-matter lane (T54).** It has no consistent candidate. The "gauge-singlet taste state" does not exist on the taste cube.
- **Neutrino mixing (T52).** The lane's TM2 mixing is excluded by JUNO data. TM1 fits, but it is borrowed from the literature, not derived.
- **Koide pair taken exactly (T39, supervisor re-check).** Take r = 1/2 and δ = 2/9 as exact. They then predict a muon/electron mass ratio of 206.77032. The measured value is 206.76828, so the prediction misses by 450σ at physical (pole) masses. δ = 2/9 is close (the best fit is 2/9 − 1.75×10⁻⁷), not exact. Any exact claim must say which mass scheme it holds in; QED corrections between schemes are about 10⁻³.

## New partial results worth writing up

- **Lapse–lapse closure (T66).** Second-order closure at range 2 in reduced sectors, plus the planar no-go above.
- **Record scattering (T17).** Diagonal-pair and plaquette scattering keep momentum and angular momentum exactly with one record per site. Energy current is still short by about the record density.
- **Light bending (T68).** For fields that are unchanged under small relabellings, bending = 1 + (matter speed / gravity speed)².
- **Maxwell uniqueness (T79).** Maxwell's equations survive exact reversibility, one real number per link, nearest-neighbour reach and *both* Gauss rows. The magnetic row is still supplied. With the ice rule alone, 8 candidates survive, and the "one speed" result is an artefact of the search grid.
- **Hawking temperature (T75).** T = κ/2π shows up roughly on the clocked walker when the rate crosses zero linearly, but the lowest levels are 7–11% off and converge slowly. Scale-covariant rate energies give κ = 0 unless something outside carries negative energy.
- **Chessboard threshold (T21).** The record gas forms the mass-giving chessboard exactly below bond cost 0.412.

## How much to trust this

Every attack and kill check was run by Sonnet 5.5. The supervisor (Opus 5.5) wrote down its own view before any attack returned (`SUPERVISOR_THREAD.md`) and compared afterwards (`SUPERVISOR_COMPARISON.md`). Nothing here has had an other-vendor referee.
