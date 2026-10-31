# checks/ad1_criteria.md — pre-registered criteria for check ad1 (T55-K adjudication)

**Written 2026-10-28, BEFORE `checks/ad1_exp.py` existed.** Exact integer / `Fraction` arithmetic in
plain python3 `-I`; no numpy, no sympy, no BLAS; no numeric lock (DRIVE_BRIEF rule 6 exemption).

## What this gate is for, and what it cannot decide

The adjudication of T55-K is a reading of statements, and **no script can decide it**. One step of the
ruling is quantitative, however, and is load-bearing: the ruling credits NBG_A §A3's vertex count as a
surviving result, and the dependency graph it produces depends on whether the four *new* vertex
families at a nontrivial background are subcritical at the delivered weight pair. If they are not, the
(N-bg) ⟶ (background linear package) reduction fails and the graph changes.

This gate decides **only** that: whether a stated leg-counting rule, forced first to reproduce the two
exponents NORMS already carries, returns strictly negative exponents for the four new families at the
delivered pair. It decides nothing about (GAP-Z), (G♯_0-field), the slice question, or any status.

## Constants used (all pre-session; none derived in session 25)

- `d = 4`, `L = 3` (lane standing values).
- The weight pair `(θ_w^c, θ_w^r) = (2, d − 1) = (2, 3)` — HANDOFF.md, "Two target restatements":
  *"curvature θ_w^c = 2, residual θ_w^r = d − 1 = 3"*.
- `θ_A = min(1, θ_w^c − 1)` — **NORMS.md l.656-657**.
- NORMS.md l.658-663: Theorem N1-15 needs `θ_w^c ≥ 2` and `θ_w^r > 2`; the **1-derivative Wilson**
  vertex is *"exactly marginal"* at `d = 4`; the 1-derivative soft family is subcritical for `d < 5`.

**No constant from NBG_A.md, NBG_B.md or any other session-25 file appears in these criteria.** In
particular the numbers −4, −1, −8, −2 and 8, 5, 12, 6 of NBG_A §A3.2 are NOT pre-registered as targets;
the gate derives its own and compares only against the two pre-session NORMS exponents.

## The leg-counting rule under test (stated here, before the script)

A vertex family contributes an L-exponent
`E = d − (weight carried by the scalar coefficient) − (sum of the weights of its three legs)`,
where a coefficient of size `O(|X_p|)` carries `θ_w^c`, a coefficient of size `O(|ρ|)` carries `θ_w^r`,
a coefficient `1 + O(·)` carries `0`; a differentiated/background-coboundary leg carries `θ_w^c` (Wilson)
or `θ_w^r` (soft), and an undifferentiated level-k response leg carries `θ_A`. Soft families are
per-level (slope in the level index `n`); Wilson families are once.

## Pre-registered verdicts

- **ad1-A — REPRODUCTION CONTROL (must PASS or the whole gate is void).** The rule, applied to the two
  families NORMS already carries, must return: 1-derivative Wilson exponent `= d − θ_w^c − 2θ_A`, equal
  to **0 at d = 4** with `(θ_w^c, θ_A) = (2, 1)` (NORMS' *"exactly marginal"*); and 1-derivative soft
  slope `= d − θ_w^r − 2θ_A`, **strictly negative for d < 5** and `= 0 at d = 5` with `(θ_w^r, θ_A) =
  (3, 1)`. **PASS** iff both hold exactly. **If ad1-A fails, ad1-B carries no information and the gate
  is reported as void.**
- **ad1-B — THE GATE.** At `(d, θ_w^c, θ_w^r, θ_A) = (4, 2, 3, 1)`, all four new families
  (3-derivative Wilson, 0-derivative Wilson, 3-derivative soft, 0-derivative soft) have **strictly
  negative** exponents. **PASS** iff all four are `< 0`; **FAIL** if any is `≥ 0`.
- **ad1-C — DESIGNED-FAIL CONTROL (must FIRE).** Re-run ad1-B's criterion at `θ_w^c = 0`, hence
  `θ_A = min(1, −1) = −1`, holding `d = 4`, `θ_w^r = 3`. The control **FIRES** (works) iff ad1-B's
  criterion then **FAILS** — i.e. at least one new family has exponent `≥ 0`. If the criterion still
  passes at `θ_w^c = 0`, the gate is **unfalsifiable and is reported as no evidence**, whatever ad1-B
  returned.
- **ad1-D — SECOND, INDEPENDENT DESIGNED-FAIL CONTROL (must FIRE).** The rule's 3-derivative **soft**
  slope is compared against the alternative algebraic form `d − θ_w^r − 2θ_w^c − θ_A`. The control
  **FIRES** iff the two forms return **different** numbers at `(4, 2, 3, 1)` — establishing that a gate
  reading the four exponents is sensitive to which formula is used, and so is not a tautology. The
  **sign** of each is reported separately; if both are negative, ad1-B's verdict is robust to that
  choice, and that is reported as a separate line, not as a pass.

## Not success

Any verdict reached by substituting a number taken from NBG_A.md or NBG_B.md; any retuning of these
criteria after seeing output; any re-run under this id. A re-run goes under a new id with these
criteria untouched. Any probe run after seeing a result is labelled **post-hoc** in NBG_ADJ.md.
