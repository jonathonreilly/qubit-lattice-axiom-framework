# Attack on T74: The black-hole 1/4 is a supplied count (BP); entanglement gives 1/6 without a selector

Attacker: Claude Sonnet 5.5, same vendor family as the supervisor (Opus 5.5); checks are same-family, not independent referees.

Read: `docs/MINIMAL_AXIOMS_2026-06-29.md` and `PRIMITIVE_REGISTRY_CHECK.md` (both in full); L15-W1/W3/W4; the June BP probe, coframe-carrier, Wald-Noether, Wald-Newton and area-law notes; gravity-wall packet (SUMMARY, kill3).

## Verdict in plain words
T74 is two walls glued together, and neither is really about the number 1/4. The action side (W1) equates a count (4 of 16 states) with gravity's strength, but the notes' own bookkeeping rescales that count's unit together with Newton's constant, so it says only "unit response b = 1", which is G in lattice units (T70). The entropy side (W3/W4) compares the wrong things. I ran the lane's own suggested test on the repo's own sea: its area coefficient is 0.197, 0.217 or 0.231 by cut direction, never 1/4, and it falls with mass. The wall does not pass; it dissolves into T70 and T64.

## The wall (checked)
- Plain: Black-hole entropy is a quarter of horizon area in Planck units. The framework has a "1/4" that counts 4 of 16 states of a supplied cell. Can the axioms show that count is gravity's strength, or that some lattice entropy equals it?
- Precise: from the four axioms plus registered primitives, derive (a) c_cell = 4/16 is the gravitational Lagrangian's coefficient (BP), so G_lat = 1/(4 c_cell); and/or (b) a native entropy with area coefficient exactly 1/4. Supplying b = 1 or a selector does not count.
- Real? Yes, but misgrouped. W1(i) attacks count-equals-entropy, yet the chain (`BH_QUARTER_WALD_NOETHER…:199-221`) equates c_cell with the Lagrangian coefficient and takes entropy from Wald. W3/W4 concern the other "1/4 surface", which the lane's own note says is not identified with it (`AREA_LAW_QUARTER_BROADER…:230-233`). Unsolved in `docs/`, `archive/` and the 36 open PRs.

## Load-bearing premises
| Premise | Kind | Path:line | If wrong | Tested? | Cheapest test |
|---|---|---|---|---|---|
| No action, entropy or time metric in axioms | axiom boundary | MINIMAL_AXIOMS:114-123, 176-190 | n/a | yes | none |
| BP: c_cell is the Lagrangian coefficient | supplied | WALD_NOETHER:199-221 | no link to G | June probe | `bp_algebra.py` |
| (N): unit response b = 1 | hidden (scheme) | COFRAME:325-380 | G_lat = 1/b | here | fix b via matter action (T70) |
| EH action and Wald formula | supplied physics | WALD_NOETHER:31-36 | no entropy | no (T64 stands) | none |
| Entropy = isotropic entanglement | reading | L15-W2; AREA_LAW_QUARTER_BROADER:230 | W3/W4 moot | here | orientation scan |
| Fixed cubic grid, no boosts | axiom + open gate | MINIMAL_AXIOMS:35-38, 185 | anisotropy | kill3; here | same scan |

## Routes
| Route | Approach | Premise dropped | Must believe | First artifact | Cost | Changes | Verdict |
|---|---|---|---|---|---|---|---|
| R1 induced gravity | Entanglement divergence renormalises 1/G, so S = A/(4G) is an identity (Susskind–Uglum PRD 50, 2700 (1994); Jacobson gr-qc/9404039; Solodukhin, Living Rev. Rel. 14:8) | count = action | metric, boosts, isotropic η | ratio 4ηg = 1 for one matter | high (T64) | T70, T73, T75 | dead as a pass (η anisotropic); survives as reformulation |
| R2 calibrate | LQG fixes the Immirzi parameter by demanding 1/4 (Meissner CQG 21, 5245 (2004); Domagala–Lewandowski CQG 21, 5233 (2004)) | derive 1/4 | b is one free constant | state b as the calibrated constant | a note | W1 PRICED | assumes conclusion |
| R3 misframed | Only G_lat·b is dimensionless; ask what fixes G_lat against the matter action | both targets | T70 is the wall | `bp_algebra.py` | T70's | T70, T64 | survives; blocked-equivalent to T70 |

## Test run
- Pre-registered (`T74_scratch/PREREG.md`): PASS if the native sea has η = 0.25 ± 2% in all three orientations with spread < 3%; FAIL if any orientation is > 5% off or spread > 5%. Extra readings: spread > 5%; η moves > 10% under mass.
- Scripts: `T74_scratch/{m1_slab100,m2_torus,bp_algebra,analyze}.py`, with outputs beside them.
- Model: π-flux cubic sea (all face holonomies −1; `HALF_FILLING_…2026-09-02`) plus staggered mass m. Spectrum matches E² = 4Σcos²k + m² to 6e-15.
- Result, η in nats per a², L → ∞ (torus L = 8…20):

| | (100) | (110) | (111) |
|---|---|---|---|
| m = 0 | 0.1967 | 0.2173 | 0.2308 |
| m = 1 | 0.1647 | 0.1842 | 0.1971 |

  Slab chains (Lx = 128) agree with the torus on (100) to 0.001. Orientation max/min is 1.17. Mass scan (100): η never exceeds 0.1966 and crosses 1/6 near m = 0.96. Universal m² ln m coefficient: fit 0.0127 against continuum 0.0133. Implied G = 1/(4η) = 1.27, 1.15, 1.08.
- Reading: FAIL, as pre-registered; both extra readings fire (17% spread, 16% mass shift). The area term is anisotropic and parameter-dependent; only the mass-log term is universal. Limitation: one supplied sea; the tick-unitary walker sea is untested.

## Outcome
MISFRAMED. Cheaper question: what fixes the gravitational action's coefficient in lattice units (b = 1/G_lat) against the matter action? With an Einstein–Hilbert action, S = A/(4G) holds for any G by Wald. Entanglement is expected to renormalise G, not equal 1/4. W1 is PRICED by (N): G_lat·b is invariant under b → λb, and the count gives d/2^d = 1/4 only at d = 4. Siblings moved: T70, T64, T73, T75.

## Claims and labels
- proved (landed, unaudited): 4Gc = 1 hyperbola (`BH_QUARTER_WALD_NEWTON…:33-36`); (N) rescales G (`COFRAME:372-375`).
- checked: `bp_algebra.py` (exact: G·b invariant; G = 1 iff b = 2^d/(4d)); all η values; log-mass fit; spectrum.
- suggested: R1 and R2 templates; entanglement renormalises G; W4's limit 1/6 (Widom/Sobolev), moot for the BH law.
- reading: the June probe's "BP = ruler" conflates unit conversion with dimensionless G_lat; T74 is downstream of T70/T64.
