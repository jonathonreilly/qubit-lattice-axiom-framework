lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-01T13:10Z

# Gate: gradient adversarial search of the field inequality (5.5), hard-core--independent, at dfa5622ea

Provenance: Opus 5.5, effort high, Mac mini worker, commit dfa5622ea, independent side of the firewall. Same model as the attempt, so this is not independent in model and is not an audit. A search that finds nothing does not prove (5.5). Verdicts steer research and grant no status.

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
