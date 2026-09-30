# Supervisor thread vs worker results

The worker-tier rule says the supervisor runs its own thread on farmed-out work and compares. Before any attack came back, I (Opus 5.5) wrote down my view in `SUPERVISOR_THREAD.md` (13:45Z). This file compares that view with what the Sonnet 5.5 attacks and kill checks found.

## Where my pre-registered view held

| Wall | My expectation | What happened |
|---|---|---|
| T30 | The chain needs all 16 tastes light down to v. That conflicts with 6 flavours. | The attack priced the wall at "a taste switch-off law". The kill check found the repo counts 2–4 flavours, so the wall stands. My arithmetic (α(v) ≈ 0.111 with 16 tastes; a Landau pole near 6 × 10¹⁴ GeV with 6) matched the kill. |
| T18 / T19 | Exact bosonization or string-net fermions escape, at the price of typed sites. | The attack on T18 missed this. I steered the kill check to it, and it found the edge-qubit exit (BKSF, Wen) already built in the repo. The exit replaces the sign with a choice of constraint. |
| T03 | Reading B is GRW/CSL: rate λ and length r_C, Born by construction, non-unitary. | The attack listed GRW/CSL but never ran it. I steered the kill check to it, and it confirmed a third exit. The price is larger than my "two constants": the collapse must be mass-weighted and band-diagonal, with records as flashes, and the model is nonrelativistic. |
| Shared price | The typed cell complex (vertex, edge, face and cube roles) recurs across walls. | It recurs in T18, T19, T25, T27, T77–T79, T15 and T20. It is the most frequent price in the registry. |
| T01 / T11 | One clause gives both the formation order and the clock. It is covariant but randomised. | T11's kill check prices the clock at the order measure, no adjacent co-formation, and a tie between the record tick and the evolution tick. T01's measure is the cheapest form of that. |
| T21 | Mass needs a staggered (two-sublattice) term or M₄(C). | The attack found that the record gas makes the chessboard below g = 0.412, which is the staggered background by another route. |

## Where it was wrong or incomplete

| Wall | My expectation | What happened |
|---|---|---|
| T39 | Not pre-registered. | My own re-check found the exact pair (r = 1/2, δ = 2/9) misses the muon/electron ratio by 450σ at pole masses, so any exact claim needs a named mass scheme. |
| T38 | Priced at "uniform weight per isotype". | The kill check found that the registered `realized_state_primitive` already books r as data, so the right label is misframed. I had not checked the primitive registry against the flavour walls. The same miss affects T36, T37, T40 and T48. |
| T02 | Misframed as a derivation target. | Both the attack and the kill check called it priced. We agree on the substance: adopt a clause. The labels differ only in wording. |
| T05 / T06 | Priced at Busch's premise (non-contextual additivity over the effect algebra). | Close. The owner memo already has the matching two-clause package, and abundance comes back as readouts in every direction plus rotation covariance. |

## What the worker tier missed, as a pattern

Of 80 kill checks, 77 weakened their attack, 3 confirmed it (T31, T46, T78) and none overturned it. The recurring faults:

1. **Prior art.** Most attacks missed landed notes that already had their result. Examples: T08 (the PR box), T11, T13, T24 (block 82), T28, T35, T51, T57, T63 and T79 (PR #7984).
2. **Standard literature exits.** Attacks missed GRW/CSL (T03), bosonization and string-net fermions (T18), the overlap Weyl-measure route to chirality (T22, found by the kill), and the staggered index theorem (T43, where the attack presented it as new). They also searched too narrow a class: T76 searched only count-threshold rules, and the kill found a covariant rule outside that class whose frozen count scales with the boundary.
3. **Over-labelling.** Attacks called walls misframed or priced where the honest label was stands, or a narrower price. About twenty walls were relabelled after their kill checks.
4. **Test power and pre-registration.**
   - Several tests could not fail: T13, T34 and T05.
   - Some pre-registered bands missed and were rerun afterwards: T43, T75 and T07.
   - Some inputs were recalled from memory. For T46 they turned out right.
5. **Wrong object.** T74 ran a π-flux model instead of the walker sea, a factor of 2. T31 and T30 used the wrong flavour count.

Sonnet 5.5 kill checks were effective. They caught nearly all of these faults, and several ran independent reimplementations. The T47 kill found the spline artefact, which is the most useful single correction in the campaign.

**Allocation lesson.** Sonnet is good for breadth, and a kill round is necessary rather than optional. Two changes would help the next run:
- The attack brief should require a prior-art search with named grep targets.
- The primitive registry should be checked before labelling any wall.

The supervisor should keep steering kill checks toward standard exits the attack missed. That steering produced the three most useful kill checks: T03, T18 and T43.
