# The gravity wall — exercise summary (2026-09-29)

Run with the candidate exercise skill (PR #9389, commit 7e109b7b04) by
Claude Opus 5.5.
- Four route agents and four kill agents were used. All are Claude Fable
  5.1, the same vendor family, so they are not independent referees.
- The blind wall check used Claude Sonnet.
- Every claim below carries one label:
  - **proved:** a landed or sol-confirmed note;
  - **checked:** a finite or numerical test run here;
  - **suggested:** an argument not yet refereed;
  - **reading:** an interpretation.

## 1. The wall, in plain words

We want gravity to come out of the framework rather than be assumed. The
framework is a grid of sites, each holding one qubit, where records are
permanent facts.

Einstein's gravity waves have two fingerprints:
- they travel at light speed;
- they have only one shape, a stretch-and-squeeze across the direction of
  travel.

Built from finite, record-like pieces on the fixed grid, the waves always
miss one fingerprint:
- with the grid's local rules strict, they are too slow;
- with the rules loosened, they are light-fast but carry an extra sideways
  shake.

The one construction that gets both fingerprints gives every place in space
continuous numbers, its local lengths and angles. That puts geometry in
rather than deriving it.

The sideways shake is not a harmless detail. Orbiting stars would radiate
into it about as strongly as into real gravity waves. The double pulsar
rules that out unless the shake travels at more than about twelve times the
speed of the real waves.

**Why it happens, in one picture (reading).** A finite dial has a few
settings and no smooth partner to swing against.
- With strict rules, nothing is left that can swing freely over long
  distances, so the wave is slow.
- With loosened rules, other shapes swing too.

Einstein's theory avoids this because one direction in it, the overall size
of space, has energy that runs backwards, and his time rule hides that
direction. A grid sitting in its lowest-energy state cannot copy it. Forcing
it, as tried here, balances on a knife edge.

**What the evidence covers.** Small, smooth waves in the tensor model we
built ourselves; bounded theorems, unaudited. It does not cover the
framework's own one-qubit sites, strongly interacting states, or non-local
patterns.

## 2. What the exercise found

1. **The wall stands.** Five routes around it died when they were attacked,
   and three survive only as narrowed or wounded statements.
   - **Dead:** a pumped non-ground state, gravity as an equation of state of
     entanglement, induced gravity without a posited metric, "statics
     first", and the claim that the extra shake is invisible to matter.
   - **Wounded or narrowed:** the price lemma, the strong-coupling exit and
     the prediction for test A1.
   - Each dead route has a stated reason, and three have a numerical check.
     Checked (same family, unrefereed).
2. **The extra shake is observationally excluded unless it is fast.**
   Radiating sources couple to it with the same direction-averaged strength
   as to real gravity waves; this is an exact representation-theory fact.
   With probe 20's floor, the double pulsar excludes partners slower than
   about 12 times the spin-2 speed. Static sources do not couple to it,
   provided matter has a local conserved momentum density.
   Checked (same family, unrefereed).
3. **The partner half of the wall is the lattice face of Einstein's
   conformal-factor sign.** To remove the shake, the compression channel
   needs a negative weight at exactly α = −β/2.
   - At that point the spin-2 waves are pure and light-fast.
   - But the shake modes become a flat zero-frequency band, which is still
     gapless.
   - The compression mode becomes a ghost, and 1 % detuning brings back
     partners or an instability.

   The ground-state systems we built cannot supply the negative weight.
   Checked in probe 18's model by test T1; suggested in general.
4. **The price, sharpened.** With finite slots and an exact local rule, the
   stored field has no local partner variable. A light-speed graviton would
   then have to be a composite, whose extra modes some non-perturbative
   mechanism removes. None is known, and the only literature candidate
   (Gu–Wen's "N-type") is declared unreliable by its authors. Suggested, by a
   same-family kill agent with a numerical cross-check, unrefereed.
5. **Gravity from entanglement does not escape on this grid.**
   - The grid's entanglement per unit area differs by 16–18 % between cut
     orientations, so there is no single universal coefficient.
   - The derivation also needs a metric and boosts that the axioms do not
     supply.

   Checked (same family).
6. **Two lanes meet at the same wall.** The June "universal GR" lane, via
   induced gravity, and this September lane, via finite-slot tensors, both
   end at "a metric degree of freedom must be supplied". Reading, from
   landed notes.

## 3. Routes worth doing (at most three)

| Route | What you would have to believe | Cost | First test | What it would change |
| --- | --- | --- | --- | --- |
| **Write the price down once** (the price lemma plus its corollary, as a refereed note) | nothing new | a note and one referee cycle, 1–2 days | the corollary's proof and check, already in `scripts/agents/` | It turns probes 10–21 into one statement: on a fixed grid of finite sites with exact local rules, the only exits are continuous sites (option A), the rule broken at the lattice scale, or an unknown mechanism that removes a composite graviton's extra modes |
| **Price option A before choosing it** (the helicity ±1 block of the induced action) | option A is on the table | one day, in probe 6's runner | one projector | Whether a posited metric plus the grid's matter brings extra modes or direction-dependent wave speeds (the kill check already found birefringence 3.9 unless tuned), and so how many tunings A costs |
| **Name a mechanism for exit (c), or stop** | a strong-coupling mechanism exists that gaps a composite graviton's partners | open-ended | none known | everything, if found. Do not spend on it without a named mechanism |

## 4. What not to do next

- **Gravity from entanglement on the fixed cubic grid.** Its area
  coefficient depends on orientation, and it needs boosts the axioms do not
  supply.
- **"Pumped" or inverted states to cancel the shake.** That gives a knife
  edge, a ghost and a flat gapless band.
- **Recomputing the static tests** (bending, perihelion). They are already
  landed in the member programme (blocks 59, 60, 144, 145).
- **Running test A1 as a test of option A.** Its predicted residual already
  appears on the matter side (block 150). Specify it first, if at all.
- **Arguing that the extra shake is harmless.** It is not, unless it is very
  fast.

## 5. The price

Inside the tested reading (finite slots, exact local rules, local terms, a
fixed grid), Einstein's graviton needs one of three things (suggested; a
wounded lemma):
- **(a)** continuous, unbounded local variables. This is option A, and the
  only exit with a working construction (the 2026-09-24 comparator);
- **(b)** local rules broken at order one in the vacuum, with no controlled
  model;
- **(c)** a composite graviton whose extra modes are removed by a mechanism
  nobody has named.

Option B (a recorded, changeable grid) is outside this reading. It is also
the only option that could remove the fixed-grid anisotropies found here:
the entanglement coefficient and the induced birefringence. That is a
reading, not a result.

## 6. Appendix

- **The wall.** `WALL.md` has the history (step 0) and the plain and
  precise versions, the three-column split and the blind check (step 1).
- **The ledger.** `ASSUMPTIONS.md` has the load-bearing ledger (step 2),
  the route clusters and the reduction (step 3).
- **Routes.** `ROUTES.md` and `APPROACH_REGISTRY.md` have the routes, kill
  verdicts and ranking (steps 4, 6, 7).
- **Outside view.** `OUTSIDE_VIEW.md` has the literature, the lenses and the
  reframes (step 5).
- **Tests.** `TESTS.md` has the tests (step 8); `scripts/` holds T1 and the
  agents' checks.
- **Agent texts.** `agents/` has the route and kill agents' full texts.
- **Assumptions most likely to be wrong:**
  - "harmonic level suffices" (S4); only strongly correlated phases could
    change the answer;
  - "a fixed grid" (A1).
- **Assumptions most expensive to be wrong:**
  - "finite local dimension" (A2 and S2); dropping it is option A;
  - "Einstein's spectrum is the target" (S8); checked here as
    observationally required.
- **Candidates for a physics-loop PR:** the price note (route 1) and the
  induced helicity ±1 block (route 2).
- **Literature worth translating:**
  - Pretko's polarisation counting;
  - the Kapustin–Fidkowski compactness analogue;
  - the Kramer et al. 2021 radiation bound.
