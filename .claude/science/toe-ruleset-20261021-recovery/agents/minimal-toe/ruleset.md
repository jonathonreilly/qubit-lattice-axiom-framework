# Minimal TOE ruleset: information minimisation (draft, 2026-10-22)

Working proposal only. No premise weight; register and axioms untouched.
Runner: `runner.py` (13 PASS, 0 FAIL; `out.txt`). Cited outside theorems
(Jacobson, Gleason, Witten, Z16 bordism, Lieb flux) are **cited, not rederived here**.

## The rules (verbatim)

**P0 (Information minimisation).** The world is the shortest description that
satisfies R1-R4. No bit is stored that the rest already fixes, and any detail
the constraints leave open carries maximal entropy.

**R1 (Possibility).** There are local registers of two-valued possibilities
with complex amplitudes. One update acts the same way everywhere. It is
reversible, so no bit is ever erased, and it reaches only neighbours.

**R2 (Relations only).** Only relations are physical. Internal labels and
positions, including which direction counts as time, may be relabelled
independently at every place without changing anything. The relabelling
symmetry is as large as R4 permits.

**R3 (Records).** A fact is actual only when it is recorded, and a record is a
permanent copy. Exactly one record history is actual. Its odds are a function
of the state that the update preserves.

**R4 (Consistency and protection).** The description must stay local under
every background relabelling, so it carries no anomaly, perturbative or
global. A light degree of freedom whose lightness no symmetry or anomaly
forces would be an unexplained small number, so it is absent, gapped at the
register scale.

There are no numbers in the rules. The register scale is the unit, and the only
selectors are "shortest", "largest" and "absent".

## What the lattice is under P0 (owner steer)

The grid is kept and re-read as the shortest code for a homogeneous, local,
reversible quantum system. It is a representation; the invariant long-distance
data is the physics.

| Current piece | From P0? | Reason |
|---|---|---|
| One qubit per site | Derived | The smallest non-trivial register (R1) |
| `Z^d` nearest-neighbour grid | Derived, given d | The most compressible homogeneous graph is the Cayley graph of `Z^d` on minimal generators (2d bonds). Description length O(1) |
| `Z^3` plus tick, versus `Z^4` | Re-read | R2 says time is not privileged, so the shortest code is a 4D hypercubic (Euclidean) description. `Z^3` plus tick is its transfer-matrix slicing. This is the register's own "candidate four-dimensional update", which was not adopted |
| 2x2x2 cubes, two tilings | Derived, as representation | The smallest block partition that makes a reversible local update move information in every direction (Margolus) |
| Face phase -1 | Derived | It gives the lowest half-filled energy (Lieb flux theorem; runner E1-E2; register #9986) |
| Fewest changes, then greatest entropy (CL-2) | Derived, literally P0 | The shortest description of the next state given the last, with no unwarranted bits |
| Bound sites unrecorded (CL-2 #9970) | Derived | Recording a bit already fixed by a set's total is redundant |
| Read once | Derived | One bit is used once, so no stored duplicate |
| Vacuum standard (CL-3) | Derived | Delta-coding: describe only departures from the vacuum |
| Copy mass, window 1/8 to 2^(1+Delta), kappa, mu, splits, Regge edge registers | **Not from P0** | Dropped or supplied. Geometry is read from entanglement instead (row 7) |

## Scorecard (severe)

Key: **D** derived (sketch given) · **P** plausible (missing step named) ·
**M** missing · **S** supplied or inserted (counts as a failure) · **Prim**
primitive. "Reg" is the current register (CL-1..3, synthesis-5).

| # | Measured physics | P0-R4 | Sketch or missing step | Reg |
|---|---|---|---|---|
| 1 | Quantum mechanics | Prim | R1 postulates complex amplitudes. Reconstruction theorems are not used | Prim |
| 2 | Born rule | D | R3 requires preserved odds. For a mixing update the squared magnitude is the unique local, phase-blind, preserved reading (register relay-conservation theorem; Gleason) | D |
| 3 | Unitarity, locality | Prim | R1 | Prim |
| 4 | Classical records, complementarity | D | R3 plus P0. Records hold only non-redundant bits | D |
| 5 | Special relativity, one cone for all species | D (cond.) | With a hypercubic description every rank-2 tensor is isotropic, so every species shares one cone at dimension 4 and violation starts at dimension 6 (runner D2). The condition is the 4D reading of row 6 | S (fitted "dressed cone") |
| 6 | 3+1 dimensions | P | The smallest even D that has protected Weyl fermions and local gravitational waves (D(D-3)/2 > 0). Missing: why gravity must propagate | S (`Z^3` is an axiom) |
| 7 | General relativity | P | Entanglement equilibrium is P0's maximum entropy at fixed volume, and it gives Einstein's equations (Jacobson 2016). Missing: emergent local Lorentz invariance with gravity, and the small-ball modular Hamiltonian | P (Regge form chosen) |
| 8 | Equivalence principle | D | Geometry is the entanglement of all registers, so the coupling is universal | D (2e-33) |
| 9 | GW speed c, 2 polarisations | D (cond.) | Rows 5 and 7 | P |
| 10 | G in cell units | P | G = 1/(4 eta), with eta the entanglement per area of the content. It is computable, but the coefficient is not universal | S (fitted) |
| 11 | Why gauge fields | D | R2 relabels each place independently, and comparing neighbours then needs a connection on every link | S (rishon registers) |
| 12 | Which group | **P, partial** | Spin(10) is the largest group that is consistent on the 16 (runner A). **Missing:** the breaking to SU(3)xSU(2)xU(1). The rules' own strong dynamics points to Spin(9) (runner C), and R2's "largest" favours more symmetry, not less | S |
| 13 | Family content and charges | D | R4: protecting a Weyl fermion from a Majorana mass needs Z4. The Z4 anomaly is Z16 (cited), so the smallest content is 16 Weyl, with nu^c forced. The Z4 is the centre of Spin(10) (runner B1). Charges are the 16's branching once a subgroup is given | S |
| 14 | Chirality realised (mirror gapped) | P | Z16 = 0 allows a symmetric mirror gap. Missing: proof that 3+1D symmetric mass generation (SMG) gaps a lone 16 | M (wall) |
| 15 | Three families | **M (fails)** | P0's "shortest" predicts **one** family. N_f = 3 is the single supplied integer | M |
| 16 | Mass hierarchy, mixing | M | No structure. Couplings of order 1 at the cell scale make small ratios plausible only through transmutation | M |
| 17 | Higgs, weak scale | **M, tension** | R4 forbids an unprotected light scalar, so the 125 GeV scalar must be composite or a pseudo-Goldstone (untested). This is the hierarchy problem stated as a rule | M |
| 18 | Neutrino masses | P | nu^c is forced (row 13). A Majorana mass is allowed only after the Z4 breaks, which gives a seesaw. Missing: the breaking scale | S |
| 19 | Strong CP | M | Nothing fixes theta-bar | P (theta_gauge = 0 or pi) |
| 20 | Vacuum energy not gravitating | D | In entanglement equilibrium Lambda enters as an integration constant (Jacobson). Delta-coding agrees | D |
| 21 | Size of Lambda | M | No rule | S |
| 22 | Inflation and seeds | M | No clock | M (n_s = 1) |
| 23 | Dark matter | M | Speculation: relics of the gapped mirror sector. Abundance unknown | M |
| 24 | Arrow of time | D | R3: records only grow. Under P0 the shortest history starts with no records, which gives the past hypothesis | D |

**Counts (24 rows).**

| | D | P | M | S | Prim |
|---|---|---|---|---|---|
| P0-R4 | 9 (2 conditional) | 6 | 7 | 0 | 2 |
| Register | 5 | 3 | 6 | 8 | 2 |

The P0-R4 M column includes row 15, a falsified prediction (one family),
and row 17, which is in tension. Supplying N_f = 3 adds one S.

Register inputs census (synthesis-5): 0 of 41 continuous numbers derived, and
8 of 42 discrete choices. P0-R4 has no continuous inputs in the rules. Its
discrete outputs are 16 per family, nu^c, Spin(10) and D = 4 (P). Its one
supplied integer is N_f.

Caveat. Rows 5, 7, 9, 13 and 20 rest on cited theorems that are not rederived
here, and the gap between P0-R4 and the register is mostly in rows 11-13,
where P0-R4 replaces inserted content with selection. The low-energy group is
still **not** derived.

## Smuggling audit (anti-smuggling gate)

1. **No measured number chosen.** Pass. The rules contain no numbers.
2. **No observed structure named.** Pass for the rule text. Risk: R2's
   "largest symmetry" plus R4 can look reverse-engineered to reach Spin(10).
   The defence is that it fails where it was not tuned. It predicts one family
   and Spin(9)-type breaking, and the observed group alone fails its own
   protection test, since nu^c could take a Majorana mass (runner A5).
3. **Predictions it was not built for.**
   - (a) N_f = 1. **Falsified.**
   - (b) A right-handed neutrino exists.
   - (c) Proton decay through Spin(10) gauge bosons, if Spin(10) breaks below
     the cell scale.
   - (d) No unprotected light elementary scalar. This is in tension with the
     Higgs unless the Higgs is composite.
   - (e) Lorentz violation only at dimension 6, with a hypercubic sky pattern.
   - (f) w = -1.

   Gate result: **(3) is partly FAILED by (a).** P0's minimality clause must
   not act on repetitions, or it must be replaced by a family rule.
4. **Axioms bent.**
   - Lattice: `Z^3` becomes a 4D hypercubic description, and the grid is read
     as a representation.
   - Qubit: content is 16 Weyl modes per family per cell, not one mode per site.
   - Admissibility: kept.
   - Record: kept and sharpened (non-redundant bits only).

## Decisive calculations (cheapest first)

1. **Group selection (DONE, runner A-C).**
   - Over a 20-group catalog acting on 16 Weyl fermions, Spin(10) (dim 45) is
     the largest group with no invariant mass, Tr X^3 = Tr X = 0 and no Witten
     anomaly. The next largest is SU(2)xSO(8) (dim 31).
   - Sp(16) (dim 136) fails only through the Witten anomaly. SO(16), Spin(9),
     SU(8)xU(1) and Sp(8)xU(1) fail because a mass is allowed. SU(16),
     SU(2)xSU(8), SU(4)xSU(4) and U(1)xSpin(10) are anomalous.
   - Spin(10)'s centre acts as i on the 16, so it is the protecting Z4.
   - Negative: the most attractive channel of 16x16 is the 10 (Delta C =
     1.20 C16, against 0.13 for the 120 and -0.22 for the 126). Left to itself,
     Spin(10) tumbles to Spin(9), not to the observed group. This matches the
     register's mirror-condensate result (SO(10) -> SO(9), #9974).
   - This is a catalog diagnostic, not a classification. The full statement
     needs Dynkin's maximal-subgroup list of SU(16).
2. **Breaking rule (next, analytic).** The task is a P0-native reason for the
   unbroken group: for example, the lowest description cost of a vacuum
   orientation once Spin(10)'s 10 is tied to the hypercube's 4 + 6 structure
   (Spin(4) x Spin(6) = Pati-Salam). If it fails, row 12 stays M for the
   subgroup.
3. **Induced couplings (small numeric).**
   - Compute the entanglement area coefficient eta for one 16 on a 4D-reading
     lattice using free-fermion correlation-matrix entropies. That gives
     l_P/a.
   - Compute the induced 1/g^2 from the same content and cutoff. This is a
     prediction with no parameters for alpha at the cell scale, and for
     M_cell/M_Planck, against 1/alpha ~ 40 near 1e16 GeV.
   - Non-universality of the cutoff is the main risk.
