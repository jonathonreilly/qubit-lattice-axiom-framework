# Complete exercise argument with controlling corrections

Original source: `.claude/science/exercises/hierarchy-wall-20261018/K/REPORT.md`; exact SHA-256 `4edb39d45ddd2a01da1849374979c7f6e1e709cba32c9a28a4ec7f95adb5f62c`.

**Controlling scope:** These counterexamples control the earlier reports where their assumptions match. Comparator and observational arguments are not an exhaustive exclusion of physical mechanisms.

**Source-use boundary:** The complete argument below is preserved for inspection, including its original qualifications and counterexamples. Its old verdict labels, claims of completed reviews, operational history and numerical outputs are historical provenance only. Terminal physical exclusions and claims stronger than the controlling scope are deferred, not active conclusions. The canonical conditional exercise note and its correction register control. This attachment is not a separately promoted scientific claim and is not a fresh replay of its exploratory computations.

---

**KILL round, hierarchy wall: report**

Disclosure: I am the same model family as the route authors (Opus 5.5), so none of this counts as an independent referee.

**What I read before concluding.** The full `MINIMAL_AXIOMS_2026-06-29.md`, `PRIMITIVE_REGISTRY_CHECK.md`, `SCALE_REFERENCE_PRIMITIVE_NOTE.md` and `derivation_obligations.json` (three entries, none on the hierarchy). Then WALL.md, TESTS.md, all four reports with their scripts and outputs, and two related notes on main, block 93 and PR #8692.

**Plain summary.** No route survives intact.
- R1's main route is dead for a reason it did not consider: in three-dimensional space, localising matter on walls leaves physics in two space dimensions.
- R4's spiral escape is real, but it still needs a small number. That number is the real part of the eigenvalue, not the ratio of real to imaginary part.
- The test pre-registered for the spiral (T-SPIRAL) uses the wrong criterion and must be fixed before it is run.

## R1 (BSM-naturalness tools)

**Lemma A — WOUNDED (wording).**
- The algebra is right for a non-degenerate eigenmode of a covariant linear operator.
- The sentence "a localised mode needs a privileged site" is false. A covariant qubit chain (translations plus bond reversal, Creutz type) has a flat band with compact eigenstates on three sites, weights 0.25/0.5/0.25 (checked, K2).
- More basically, "No site is privileged" is a statement about the law. A realized state can break the symmetry spontaneously, and Lemma A says nothing about that.
- R1's next step, that walls come from records and so L is registered data, is supplied by the no-typicality clause of the realized-state primitive. It is not physics. The same clause would turn any stochastic order parameter into registered data.
- Strongest form: no explicit localisation of a non-degenerate linear mode.

**Lemma B — WOUNDED.**
- The clockwork mass matrix MᵀM has a bulk that is symmetric under bond reversal: diagonal 1+q², off-diagonal −q (checked, K1).
- The one-ended zero mode, with end ratio q^−N = 9.5e-7, comes only from the two end entries (1 and q²) differing.
- R1's w = 1 test doubles the bulk and symmetrises the ends in the same move, so it does not isolate the bulk.
- Prior art: the scalar case is already on main as block 93 T1 ("Every such weighting is symmetric in d and −d").
- Strongest form: a covariant bulk only supplies a decay length ξ, and any one-ended mode needs asymmetric terminations.

**Route 1 (two walls, e^(−L/ξ)) — KILLED as a mechanism for v or fermion masses.**
- Walls in Z³ bind modes that move in only 2+1 dimensions.
- A three-dimensional lattice of defects instead gives light fields a speed about e^(−L/ξ) of the lattice speed. That contradicts the kinetic-isotropy primitive and the measured equality of gravity-wave and light speeds.
- Separately, if L is random, v varies from place to place.
- Time-direction walls are R1's own time-arrow variant, which nucleosynthesis already kills.
- What remains is taste clockwork: a gear ratio of at least 1.5e4 over 4 links, which is a supplied ratio.

**Route 2 (local relaxion) — SURVIVES as a kill.**
- It kills only the toy, and the toy supplies its own scanner potential.
- The extrapolation to 10^29–10^33 sites is not load-bearing.

## R2 (condensed matter: tunnelling and codes)

**Lemma 2 — SURVIVES.**
- Elementary and correct: the XOR of two periodic configurations is periodic, so finite support means it is zero. The result is standard.
- Its scope is periodic vacua only.

**The claim that end states are detuned — SURVIVES my kill attempts** (checked).
- The two natural rule classes with zero second-order detuning are XOR-linear rules and "exactly k" totalistic rules.
- Neither has any finite flip: the nullity in a 5³ box is 0 (K3). The reason is that one constraint polynomial over a Laurent ring, which is an integral domain, has no finite kernel.
- Ice-like rules on extensive manifolds fail differently. Their order-n amplitude rescales the whole emergent sector's energy, which amounts to a velocity hierarchy and not a mass hierarchy. This strengthens R2's "heavy object" reading.

**Route 2 (Chamon code) — SURVIVES as a named-number result:** the integer L. It is consistent with main's Chamon note.

## R3 (cosmological counts)

**Lemmas A and B — SURVIVE** (I re-derived the drift 1.99e-11 per year). This is the textbook Dirac large-number kill.

**Lemma C — WOUNDED, with three cuts.**
1. Unitarity (reflection positivity) is not supplied by the axioms. Irreversible record formation naturally falls into non-unitary classes whose one-point exponents sit below the bounds: percolation has β/ν = 5/48 in 2D and about 0.477 in 3D (comparator).
2. A hidden premise: the light sector already sits at a critical point, which is the tuning itself.
3. The "allowed" dimension-4 case does not set a vev, because a constant density does not move v. The Higgs-portal case with d_O = 2 needs Δ = 0.55.

**Route 2 — WOUNDED.**
- It restates the known coincidence ρ_Λ^(1/4) ≈ v²/M_Pl (literature template).
- It is a one-point fit with s free.
- It merges this wall into Lane 5 rather than removing a number.

## R4 (dynamical systems / RG)

**Lemma A — WOUNDED.**
- The bound assumes the smallest decay rate is not shared.
- With a shared rate, F = (10 − 0.1N)e^(−N) + e^(−1.5N) balances at N* = 100. That is κN* = 100 with R = 10, against a stated bound of 10.6 (checked, K4).
- In that case the extent is linear in a ratio of two amplitudes (about 40 is needed).
- "n = 16.0 exactly" is circular: it is just 16·ln(1/α_LM) ≈ L* for main's candidate.

**Lemma B — SURVIVES in 1D only.**
- In 2D, fast rotation averages the quadratic terms away, so a small real part does help, contrary to the lemma's "small exponent alone does not help".

**"A spiral needs no slow point" — WOUNDED.**
- It is true for the flow speed |β|. The radial drift, however, is slow everywhere along the path.
- The passage time is about ln(range)/|Re y| (checked, K5/K5b):

| Re y | Im y | Re/\|Im\| | Passage time T |
|---|---|---|---|
| 0.5 | 10–50 | 0.01–0.05 | 3.9–4.9 (no hierarchy) |
| 0.03 | 3–10 | 0.003–0.01 | 20–52 in 4 of 6 random draws; never gaps in 2 of 6 (supercritical case, captured by a limit cycle) |

- So the supplied number is |Re y| ≈ 0.03–0.06 in absolute units. The flow also needs |Im y| much larger than the quadratic couplings and the right sign of the Lyapunov coefficient.
- R4's own trial 1559 is not a free spiral: it lingers near an unstable limit cycle around a stable focus, so its initial condition is tuned.
- Strongest form: a near-marginal complex pair evades the 1D quadratic kill, at a tuning cost (about 1%) close to the 1D ghost's.
- Prior art R4 missed: block 93 and PR #8692 on main show that covariant scalar pair weights give detailed balance and a reflection-positive stationary law. Spirals therefore cannot appear in the reversible comparator class. Only the permanent-record class remains open.

**T-SPIRAL needs fixing before the run.**
- The readout "Re/|Im| ≤ 0.05" is wrong: the Re = 0.5 case above passes it and produces no hierarchy.
- Replace it with: |Re y| ≤ 0.06 per e-fold, |Im y| ≥ 1, the sign of the Lyapunov coefficient reported, and the result stable across block size.
- State whether the RG acts on the spacetime process or on the frozen record pattern; with absorbing states, the frozen pattern may have no non-trivial fixed point at all.
- Watch for complex pairs that are artefacts of truncation.

## Ranking (cheapest test that moves the wall)

1. **R4 spiral, via the corrected T-SPIRAL** (a few hours). Either result moves the wall. SPIRAL-ABSENT in the permanent-record class closes the last escape, within the flow class, that does not put a number in by hand. SPIRAL-NATIVE opens one.
2. **R3 Route 2: measure the one-point exponent of a native irreversible record sector** (1–2 hours). Even a match only links v to Λ.
3. **R4 Lemma A shared-rate case: look for a native two-channel balance whose amplitude ratio is about 40.** The geometric value e^(−4π²) is already mapped on main as the meron route.
4. **R2 symmetric-defect SAT search** (about 1 hour). It gives only a defect-level scale, so it does not move the v wall.
5. **R1.** No test moves the wall: the route is dead except for taste clockwork, which needs a supplied ratio.

Spot checks stayed under 0.3 GB, one process at a time, and no processes are left running. I also lowered the memory cap in my own copy of `K/scripts/capped.sh` to 290 MB. Its 400 MB setting was above the 0.3 GB limit, and my first K5 attempt was killed at 423 MB.

Files are in `/private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-toe-leverage-analysis-e8a790/af5789b9-888d-43b1-90de-58a07e0f2129/scratchpad/hierwall/K/`:
- `kill_checks.py`, `kill_checks_K1-K4.out`
- `k5_spiral.py` / `.out`
- `k5b_spiral.py` / `.out`