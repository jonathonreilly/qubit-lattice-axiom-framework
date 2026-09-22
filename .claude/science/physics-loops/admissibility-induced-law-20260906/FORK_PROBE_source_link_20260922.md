# Fork probe — the source-link direction's forks against known physics (panel + supervisor synthesis; 2026-09-22)

**Owner's instruction (2026-09-21):** "probe those forks / pick the ones that map to known physics or complete the TOE."
**Method:** four independent panel lenses (lattice fermion practice; QFT vacuum and second quantization; gravitation — ADM/tetrad/scalar theories; rigor + TOE strategy), the same dossier, each delivering verdict / strongest argument / steelman / what would change their mind / next test; synthesis by the supervisor, not delegated. A first probe (the sea's induced ledger) was executed before the synthesis. Nothing here is adopted; comparators are references, never premises.

## 1. Not forks (decided by the axioms or by proved blocks)

| fork | status | in-framework reason | comparator |
|---|---|---|---|
| (iv) are the eight species all kept? | decided: all eight, four of each sense | at each zero `k = πn` the stabiliser in the 24 proper rotations fixes no vector, so no covariant `b(k)·σ` of any reach gaps any species (exact, enumerated); a two-component coin with finite reach on `Z³` has senses summing to zero (block 54 T1(d); block 71 T4); the scalar hop `a` only shifts levels | Nielsen–Ninomiya; Kogut–Susskind (8 Weyl = 4 Dirac tastes) |
| 4 (does an unrecorded amplitude source?) | decided by clause C | whatever has rate-dependent energy sources the rates (block 55 T1–T2); "readable" concerns reading | — |
| (iii) reach | decided by blocks 72–74 given (iv): reach three | the only relabelling-generated coupling with exact books, one geometry and the ledger's requirement for all eight (block 73) | point-split taste-singlet currents; the lattice's Belinfante symmetrisation |

**Tension flagged by all four lenses:** the spectrum is vector-like (four right, four left); the Standard Model is chiral. A chiral spectrum needs a larger coin (parked), a fourth direction with a wall, non-local reach, or a filling between split levels (below). The 16 branches are states of 8 fields, not 16 fields; the coincidence with a generation's 16 Weyl fields is Clifford counting, not a map.

## 2. Branches that are known physics (the "yes" branches reproduce GR's structure)

| fork | yes-branch = | evidence in the lane |
|---|---|---|
| 1 sites have clocks | the lapse; "only ratios" = the lapse is gauge | blocks 53–55 |
| (i) counted per local tick | the lapse is an undifferentiated multiplier; the Hamiltonian constraint linear in `N`; the ledger a boundary term | block 60 (every clock a multiplier; walls' term); block 75 (closed lattice: total zero) |
| (ii) blind to the coin's axes | local SO(3) frame invariance of the tetrad formulation; block 65's twist hop = the spin connection's first order | blocks 64–65; exact form needs SU(2) bond links (all four lenses) |
| 6 lengths | the spatial metric; `β = 1` = bending twice the fall | blocks 59–60, 64 |
| 7 delay | block 62's two transverse disturbances = the two polarisations; one speed iff `K = 4α` (not yet checked) | block 62 |
| 3 books balance | the Hamiltonian constraint | block 55 |
| 2 walker | a lattice Weyl fermion; the species its tastes | blocks 54, 68–70 |
| (v) both signs | the filled sea: negative branches occupied, holes source positively; block 71's chase = Bondi's runaway, a first-quantized artefact | block 71 (needs the exchange sign — see §4) |

## 3. The completion candidate, probed: the sea's induced ledger

If the negative branch is filled, `E_sea = Σ_{E<0} E = −½ tr|H_w|` is a functional of rates, frame and strains and could INDUCE the field's energy (comparator: Sakharov), removing clause C's supplied `F`, fixing `γ`, and making (i) and (ii) automatic. Executed by the supervisor (floating point; tori `6³–12³`; `scratchpad/fluid/sea_scratch*.py`):

- **Exact (one line):** a chessboard modulation of the clocks, `u = ε(−1)^{x+y+z}`, is invisible to clause B's coupling: `φ_xφ_y = 1` on every bond, so `φHφ = H`. `E_sea` is exactly unchanged at any amplitude (`0.0000` at `ε = 0.25, 0.5, 1`).
- **Exact:** under the reach-two coupling `E_sea` is even in the strain (block 70 T3(d) + tracelessness); under reach three it is not.
- Volume term `c₀ = E_sea/site = −1.193` (L = 12), weight one.
- Rates' polarisation: `Π(q) = c₀/4 + κ q²/4 + …` with **`κ = +0.095`**, isotropic to 1% across directions, converging with `L` (0.0184 → 0.0230 per `q²` from L = 6 to 12). **Nonzero ⇒ the induced energy is not counted per local tick**: it is the simplest member's stiffness (block 56; Einstein 1912; half bending), not the curvature member.
- Strain polarisation (reach three): TT modes `+0.002–0.003` per `q²`, isotropic stretch `+0.0004–0.0006`: an order of magnitude below the clocks'.
- Sign: with the volume term kept, the linearised static law is repulsive and singular at the chessboard mode (`c₀ + κ·12 ≈ −0.05`, and exactly zero by the one-line fact); with the uniform part removed (normal ordering), attractive with **`γ_ind = 1/κ ≈ 10.5`** in lattice units.

**Verdict:** the free massless one-walker sea does not induce GR's structure on this lattice; it induces what a Lorentz-violating cutoff is known to induce (a `(∇u)²` term). Fork (i) stays a genuine supplied clause; fork 8 gets a value only in a reading that gives the wrong bending. (QFT lens's own criterion: "`a = 0` is the induced-curvature prediction; `a ≠ 0` induces the simplest member's stiffness" — `a ≠ 0`.)

## 4. Imports flagged by the panel that the lane had not flagged

1. **The exchange sign.** "One record per site at a time" is hard-core exclusion (no two records at a site, any coins), not Pauli exclusion; a sea needs anticommuting composition. Test: two records on `L = 4` under the one-per-site constraint; `tr H^k` against the antisymmetrised and symmetrised free pairs.
2. **The inversion symmetry of block 54** (not an axiom symmetry) set the scalar hop `a` to zero. The axioms' own family `a₀ + 2aΣcos k + Σσ sin k` splits the eight zeros to `a₀ + 2a(3 − 2|n|)`: levels `+6a, +2a, −2a, −6a` with multiplicities 1:3:3:1, each level of ONE sense. Kramers doubling (`Θ² = −1`) at every zero for every nearest-neighbour rule. A filling between levels has chiral content at the Fermi level (comparator: Weyl semimetal) — the only axiom-allowed knob that distinguishes species.
3. **Rest energy** (fork 5): the coin-scalar hop gives offsets, not masses; a staggered site term `mε(x)`, `ε = (−1)^{x+y+z}`, anticommutes with every one-link operator and gives `(H + mε)² = H² + m²` exactly — four Dirac fermions of one mass (Kogut–Susskind mass), pairing species `n` with `n + (111)`. It breaks one-site translation: the form of a chessboard background — the lane has chessboard states (block 17). Note the chessboard in the CLOCKS is invisible (§3); the mass needs a chessboard in an on-site term.
4. **SU(2) bond links** make blindness exact (all four lenses) and — two lenses — the `Z₂` centre absorbs the species' site signs, so a link-dressed nearest-neighbour coupling might serve all eight species: to test (it would reopen (iii) toward the axiom's range).
5. **Kinetic terms**: per-tick counting as dynamics needs the constraint algebra to close: DeWitt's `β = −α` and `K = 4α` (gravitation lens); on the lattice closure may fail at `O(p²)`.

## 5. Picks and order

1. Block 76 — the sea's induced ledger (exact parts + the numbers of §3).
2. Block 77 — the axioms' own generator: the `a`-term's 1:3:3:1 single-sense split; the staggered mass `mε`.
3. Block 78 — SU(2) bond links: exact blindness; species at nearest-neighbour reach.
4. Block 79 — hard-core against Pauli: two records under one-per-site.
Then: constraint-algebra closure (`β = −α`, `K = 4α`); the `K = 4α` speed check for fork 7.

## 6. Layman sentences offered by the lenses (not adopted; for the owner)
- "Every place keeps its own time and counts the field's energy in its own ticks, and that alone is why gravity is Einstein's and not Newton's." (gravitation)
- "Empty space is already full — every site holds all the negative-energy ways a record could move — so a particle is one more way filled and an antiparticle is one way left empty, and both weigh and fall the same." (QFT; §3 says the full sea does not by itself supply the field's energy)
- "The lattice cannot tell left from right, and a walker weighs something at rest only where the sites beneath it alternate like a checkerboard." (lattice)

## 7. Results of the probe blocks (2026-09-22, after the synthesis)

| block | PR | what it settled |
|---|---|---|
| 76 | #8611 | The free massless sea, booked as the field's term, induces a **clock stiffness** `κ = 0.095` (not per-tick: block 56's member, `γ_ind = 10.5`), a negative volume term `c₀ = −1.193` (repulsive and singular at the chessboard mode if kept), and almost no lengths' stiffness. Exact: a chessboard of clocks is invisible to clause B (`φ_xφ_y = 1`); the reach-two sea is even in the strain. **The induction route does not give the curvature member; fork (i) stays a supplied clause.** |
| 77 | #8612 | The axioms' own family (block 54's inversion dropped): the scalar hop splits the eight species into levels `a₀ + 2a(3 − 2|n|)`, 1:3:3:1, each level of one sense, gaps none, breaks the exchange maps, keeps the reversal of motion. A staggered on-site term `mε` anticommutes with every odd-step operator (walk, `a`-hops, frame, twist, reach-three strain) and **commutes with the reach-two term**: `(H + mε)² = H² + m²`, `φ(H + mε)φ = φHφ + mwε` — a rest energy timed by the local clock; with the `a`-term one heavy and three light massive pairs. The massive walker falls as a slow body; the massive sea is still clock-dominated. **Fork 5 has a nearest-neighbour mechanism inside `M₂(ℂ)`, at the price of a background.** |
| 78 | #8613 | "One record per site at a time" is an **interaction**: two records under exclusion have `tr H²/dim = 2/3, 3/4, 4/5, 5/6` (rings 4–7) against the free antisymmetric (`6/7 …`) and free symmetric (`10/9 …`) pairs; the exchange sign is invisible at second order; the free pair's energy is additive, the hard-core pair's is not. **Block 76's free sea is a comparator; the framework's sea, if any, is interacting.** |

**Standing after the probe.** Of the three completion candidates in §3–4, the induction of the field's energy from a sea is negative for the free sea (76) and not yet computable for the axioms' interacting sea (78); rest energy has a mechanism (77); the SU(2)-link question (§4.4) and the constraint-algebra closure (§4.5) are not yet built — loaded to the probes queue. The forks that remain the owner's are unchanged in number and sharper in content: how far a rule may reach; whether the eight kinds are all present; which amplitudes are present and how records compose (the exchange sign); whether a staggered background exists.
