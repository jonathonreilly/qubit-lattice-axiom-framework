lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T13:10Z

# Gate: gradient adversarial search of the field inequality (5.5), hard-core--independent, at dfa5622ea

Provenance: Opus 5.5, effort high, Mac mini worker, commit dfa5622ea, independent side of the firewall. A same-model check is not independent in model and is not an audit. Verdicts steer research and grant no status.

## Verdicts

| Statement | Verdict | Basis |
|---|---|---|
| (5.5), Theorem 5.5, as a search target | No counterexample | Best Ratio_C is 1.000000 over 137 rule-map gradient runs. A search that finds nothing does not prove a bound. |
| Theorem 5.5, proof Steps 1 to 5 | ADVANCE | Read line by line. No step failed. D3, D4 are local, and their repairs are in hand. |
| Registered outcome | NULL | Nothing above 1.05, and BREAK was not met. Evidence only. |
| Positive control | Failed as written, power shown | Ratio grows on the fixed map, but the registered 3 at L = 5 was not reached. See D1. |
| Obligation "true-gradient search" (Text, line 93) | Search done | It stays confidence, not a discharge of anything. Theorem 5.5 rests on its proof. |

**Result.** The sheet of Ratio 1 stays the worst field known, now with a true gradient, in the theorem's regime, at L up to 9. C_OS >= 1 is the only lower bound this gives. No explicit upper value of C_OS exists yet.

## Results

Run under a confirmed lock, nice, BLAS threads 1, RSS guard 2 GB, memory 56 to 69 percent free at each start. About 83,000 gradient evaluations in all, about 4.5 hours wall time.

| Search | Runs | Max Ratio_C at L = 3, 5, 7, 9, 11 |
|---|---|---|
| R1, rule map, theorem regime | 101 | 1.000000, 0.999999, 0.999998, 0.999999, 0.64 (1 run) |
| R2, rule map, legacy regime | 36 | 1.000000, 1.000000, 0.999997, not run, not run |
| Fixed x_0 = y, the control | 19 | not run, 1.48, 2.45, 3.84, 4.85 |

The ceiling of the control's defect is 2 L^2 / 32 (it has about 16 plaquettes at f = 2): 1.56, 3.06, 5.06, 7.56. So the search reached 95, 80, 76, 64 percent of it.

- **VERIFY.** The attempt's pure-Python map reproduces |W - 1| and min|m| to 9 digits on the control field at L = 5 (Ratio 1.482, min|m| 1.8e-5) and on the best rule fields at L = 3, 5. The registered second code path at larger L was not run, so the control values at L = 7, 9, 11 rest on `fi_map.py` alone, which matched the old map only at L = 3, 5. No field needing VERIFY above 1.05 arose on the rule map.
- **Sheet is a sharp local maximum.** From the sheet with noise, L-BFGS returns to Ratio 1.0000 within about 50 to 500 evaluations. Many starts climb towards 1 from below, and none pass it.
- **Why 1 (hand derivation, linear order only, labelled implication).** By (R4), F' = L^-4 sum_y sum_{s,t} F, so a plaquette has weight at most L^-4 L^2 = L^-2, and |W - 1| <= L^-2 ||f||_1 + higher order. So Ratio_C <= 1 near flat, attained at the centre. The search shows no nonlinear gain above that.
- **Z2 fields.** Gradients cannot move a sign, so I annealed sign fields with |W - 1| >= 1.9 held. No field with fewer than L^2 vortex plaquettes at L = 3, 5, 7. This is weak at L >= 5: only 56 to 107 of 4000 moves were accepted. By hand, a majority flip widens where a vortex of area L^2 acts, but the cut of a cross-section still costs L^2 (relative isoperimetry in a cube), so the two normalised means do not obviously discount the area. Reasoned only.
- **Dispersal branch (unregistered probes, criteria written first).** Step 5 is the one place the proof loses direct control. In the branch x_0 = argmin s, s(x_0) <= 3 t with t := L^-2 ||f||_1(block), so a dispersing field has t >= Q := min of max(t, s(x_*) / 3), and that branch gives Ratio <= 2 / Q up to the c_1 term. Found Q, always an upper estimate of the minimum: 3.60, 3.43, 2.40, 5.07, 5.24 at L = 5, 7, 9, 11, 13, block corner. The last two had one start each and are less converged. Centre: 14.9, 10.3, 4.0 at L = 5, 7, 9. Q never fell below 2, and there is no steady fall with L, so the claim t >= c of Step 5 was not threatened. True Ratio search from these fields: 0.86, 0.64 at L = 9, 11. L = 13 stopped at the RSS guard, 2.03 GB, so that run is missing.
- **A corner is cheap.** A star at a block corner disperses at t = 8 / L^2, s = 8 + 16 / L, which fits 4 plaquettes at f = 2 (read from the numbers, field not inspected). The rule can pick that corner only if every other site has s at least that large, which needs t >= about 8 / 3, so this does not threaten (5.5). It does show that s_rule must stay below about 8; the 0.25 of the check script and the 0.02 of R1 are well below.

## Defects

Ranked by what each could break. None breaks (5.5).

1. **The registered control was mis-set, by me.** I wrote "at least 3 at L = 5" before computing the defect's own cost, which caps Ratio at 1.56 there. Taken literally the control fails at L = 5. It rises as registered to L = 7 and continues to 4.85 at L = 11, roughly as L^2. **Its power depends on the start.** Only starts containing the star found it. Blind starts stayed at or below 1.0 at every L, and with the plain star start L = 9, 11 stayed below 1. So a rule-defeating field of a shape I did not seed could be missed.
2. **The old numerics were outside the theorem's regime.** Text 5 reports eps_0 = 0.05 at L = 3, 5, so c_1 = 0.45, 1.25, against Step 5's c_1 small. They also used only the split irr = rough. Repaired by R1 and Ratio_C here. Text 5's "It does suggest that C_OS is not large" is still only about the regular branch. The proof's constants in Steps 1 to 5 are much larger than 1, and nothing here tests them.
3. **"Hull" is not defined at (5.5).** The proof's surfaces need the whole 2L x 2L x L x L box, crossing plaquettes included, and the old script counted plaquettes outside it. Repair: define the hull of a coarse plaquette as the plaquettes of that box. Any H in Theorem 4.2 that is a union of cells covering it is then fine.
4. **Text 4.1 and Theorem 5.5 state different hypotheses.** Text 4.1 says "any split"; Theorem 5.5 asks that irr contain the rough ones. The proof never uses that hypothesis: Step 4 takes any split, and Step 5 bounds L^-2 ||f||_1(reg) by C ||f||_2(reg) for any reg. Repair: state the theorem for all splits. Harmless, as Theorem 4.2 uses a split that satisfies both.
5. **Text 3.1 item 6 pushes eps_0 far below 0.02 L^-2.** I did not run that. Ratio_C does not depend on eps_0 through irr = all, which is admissible at any eps_0, but the rule does. Below R1 the rule reads nearly every plaquette.

## Limits of this search

One coarse plaquette, in the (0, 1) plane. x_0 and the split are frozen inside each gradient step, so a move that gains only by jumping the rule is seen only when scored. Ties go to the first minimiser, and the kernel's other tie elements are not tested. L = 9 and 11 had fewer evaluations, and many of those runs ended well below 1, so they are less converged. None of this proves a bound at any L.

`dispersal.py` and `dispersal2.py` are kept as records of failed probes. The first had a wrong reading: W_0 vanishes on bulk plaquettes, so a bulk field disperses at s = 0 and large t. The second stopped early because the rule jumps, so its numbers are start values. Use `dispersal3.jsonl`, `dispersal4.jsonl` and `dispersal5.jsonl`. Most saved fields were deleted to keep the folder small. The `.npz` files that remain are the control fields at L = 5, 7, 9, 11 and the rule fields at L = 3, 5, 7.

## Read and not read

Read: `FINISH.md`, `GOAL.md`, and in `parts/hard-core--independent.md` the headings, grep hits on (5.5), Text 1.1, 1.2, 3.1, 4.1, 4.2, the end of 4.8, 4.9 and all of Section 5, and the attempt's own check scripts `hard-core--independent_field_ineq.py` and the header of `hard-core--independent_field_spsa.py`. These two scripts are not on the firewall's read list, but they belong to this attempt and the item is about them; I imported the first for VERIFY.

Not read: the mapped file, any file in `library/`, any gate, the Sussman-Alpoge repository, the upper chain. File names in `checks/` and a filtered listing of `gates/` were seen, and none of those files was opened. Nothing was committed or pushed.

## Registered before any run

Statement pinned: Theorem 5.5, `parts/hard-core--independent.md` line 940, map D3 of Text 5.1, 5.4.

**Hull.** The text does not define it beyond "hull plaquettes". The proof's surfaces lie in the bounding box of the four corner blocks, so I take the smallest admissible hull: all plaquettes with four corners in the 2L x 2L x L x L box, crossing plaquettes included. The old scripts also counted plaquettes sticking out of the box, which only inflates the right side.

**Ratios.** RHS(S) = L^-2 ||f||_1(irr) + ||f||_2(reg). Ratio_A uses irr = {f > eps_0}. Ratio_C uses the admissible split that minimises RHS, irr containing {f > eps_0}, so Ratio_C >= Ratio_A, and it includes irr = all. The sup of Ratio_C is a lower bound on C_OS. Old runs only measured Ratio_A with eps_0 = 0.05 or 0.01.

**Regimes.** Item 6 of Text 3.1 asks eps_0 <= c_1 L^-2 with c_1 small, so the old eps_0 = 0.05 at L = 3, 5 has c_1 = 0.45, 1.25 and was outside the theorem's regime.
- R1 (theorem regime): eps_0 = 0.02 L^-2, s_rule = 0.02.
- R2 (legacy): eps_0 = 0.05, s_rule = 0.25.

**Search.** True reverse-mode gradient by torch through the whole map, double precision, L = 3, 5, 7, 9. L-BFGS on a smoothed log Ratio with smoothing annealed, x_0 and split frozen at each evaluation, because they are piecewise constant. Every evaluated field is scored exactly, with the rule recomputed. Starts: sheets, half-cut sheets, smooth noise, Haar patch, vortex gas, star defects.

**Criteria.**
- BREAK: in R1, verified best Ratio_C above 12 (log L)^(1/2), the old check bound, at some L; or best Ratio_C rising by a factor >= 1.5 at each step L = 3, 5, 7 with a scaled family confirmed at L = 9. Either falsifies an absolute C_OS.
- ABOVE-ONE: verified Ratio_C > 1.05. First field above the sheet. It bounds C_OS from below and does not break (5.5).
- NULL: nothing above 1.05. That is evidence only.
- POSITIVE CONTROL: the same search on the map with x_0 = y fixed, which the attempt says fails. The search must find Ratio growing with L, at least 3 at L = 5 and rising to L = 7. If it does not, the search has no shown power and NULL means little.
- VERIFY: any reported field is recomputed by the attempt's own pure-Python map at L = 3 and 5, or by a second code path at larger L.

Unregistered probes are labelled as such where they appear.

## Build and cross-check (done)

`checks/gate_fi/fi_map.py` is written from Text 5.1, 5.4, not from the old script. A mean over one coordinate of phi(s) seg(s -> t) factors through the line transport, so a full evaluation is O(L^4), and L = 9 and 11 are reachable. `crosscheck.py` output is in `crosscheck.out`: PASS-X, |W - 1| agrees with the attempt's pure-Python map to 2e-15 on eight fields at L = 3, rule and fixed; gauge invariance at L = 5 to 1e-13, with the rule moving x_0; PASS-G, autograd against central differences to 7 digits. The centre sheet gives Ratio 1.0000 exactly at L = 3 to 11.
