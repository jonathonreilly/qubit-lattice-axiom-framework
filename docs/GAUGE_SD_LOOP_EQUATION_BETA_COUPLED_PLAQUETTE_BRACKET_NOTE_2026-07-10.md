# Gauge SD Loop-Equation Beta-Coupled Plaquette Bracket Note

**Date:** 2026-07-10
**Claim type:** bounded_theorem
**Status:** source proposal; independent audit required. Runner `TOTAL: PASS=51 FAIL=0`.

**Claim boundary:** exact finite statements only, at `N = 3`, Wilson plaquette
weight, `beta = 6`, on the fixed truncated word set described in §3 (validity
for every finite torus with all sides `L >= 5` and for every translation- and
point-group-covariant expectation functional satisfying the listed
constraints). The machine-certified content is: (i) the two-sided `D = 2`
bracket `w_P in [-10000001/20000000, 903482039/1000000000]` with exact
rational LDLT certificates verified inside the runner; (ii) the all-ones
refutation theorem (§4) in both `D = 2` and `D = 4`; (iii) the payload,
inventory, and quadrature pins of §7. The `D = 4` interval of §6 is a
floating-point solver disclosure, NOT a certified bound: the certified `D = 4`
content of this note is only the kinematic box `w_P in [-1/2, 1]`. This note
does not compute `<P> = R_O(beta_eff)` at the reproduction-contract precision,
does not produce a certified `D = 4` bracket beyond the box, and does not
introduce any strong-coupling series, Monte-Carlo input, or literature value
as a derivation input.

Status authority: independent audit lane only. This source note does not set,
predict, promote, or demote any audit outcome.

Primary runner:
`scripts/frontier_gauge_sd_loop_equation_beta_coupled_plaquette_bracket.py`

Runner cache:
`logs/runner-cache/frontier_gauge_sd_loop_equation_beta_coupled_plaquette_bracket.txt`

No literature value, new axiom, external citation, fitted selector, or new
comparator number is imported. The comparison number `0.5934` is used under
the existing plaquette reuse license as fenced comparison context (audit-only;
it enters no equation, no bound, and no certificate). The solver stack of §6
(python 3.13.5, cvxpy 1.9.2, Clarabel 0.11.1) is disclosure metadata for the
floating-point records, not an authority: everything certified in this note is
re-verified inside the stdlib-only runner in exact rational arithmetic.

Context pointers, not one-hop authorities:
`docs/GAUGE_SCALAR_TEMPORAL_OBSERVABLE_BRIDGE_STRETCH_NOTE_2026-05-02.md`,
`docs/INDUSTRIAL_SDP_BOOTSTRAP_LATTICE_BRACKET_NOTE_2026-05-03.md`,
`docs/INDUSTRIAL_SDP_BOOTSTRAP_INFRASTRUCTURE_NOTE_2026-05-03.md`.

## One-Hop Authorities

- [GAUGE_SCALAR_KZ_BETA6_REPRODUCTION_CONTRACT_FIREWALL_2026-06-06.md](GAUGE_SCALAR_KZ_BETA6_REPRODUCTION_CONTRACT_FIREWALL_2026-06-06.md)
  for the acceptance contract this note works inside: figure-derived values
  are comparators only, and the contract names as open the construction of
  "a repo-owned SDP that adds beta-coupled loop equations". This note builds
  exactly that object and reports every item the contract requires
  (truncation, basis, normalization, objective, the beta-coupled loop
  equations, the positivity constraints, solver and version, tolerances,
  primal and dual residuals, raw solver status, and outward-rounded final
  intervals).

## 1. Setting and deliverable

Target context: the `beta = 6` completion frontier — connecting the repo's
derived plaquette structure to the nonperturbative `SU(3)` Wilson value of the
fundamental plaquette. The acceptance contract (one-hop authority above)
firewalls every figure-derived route and leaves open one constructive door: a
repo-owned semidefinite relaxation whose constraints include *beta-coupled
loop equations*, i.e. constraints in which the coupling enters through derived
Schwinger-Dyson (SD) identities of the Wilson measure rather than through any
imported number.

This note lands that object and its first exact outputs:

1. a derived one-plaquette-insertion SD identity for the `SU(3)` Wilson
   measure (§2), validated four independent ways;
2. a finite exact-rational SDP model over loop moments at `beta = 6` in
   `D = 2` and `D = 4` (§3), with every shape pin re-derived at run time;
3. a refutation theorem (§4): box + PSD kinematics alone admit the all-ones
   point, and every one of the 12 embedded SD equations cuts it off by the
   same exact margin `+4/3` — the beta-coupled equations carry information
   strictly beyond the kinematic relaxation;
4. a certified two-sided `D = 2` bracket for the fundamental plaquette moment
   at `beta = 6` (§5), with exact rational LDLT certificates embedded in and
   re-verified by the runner, and with the exact `D = 2` transfer-matrix value
   inside the bracket;
5. an honest floating-point-only `D = 4` disclosure (§6), including the
   quantified failure of exact certification at the current Gram depth.

Normalization used throughout: `w_P = <(1/3) Re Tr U_P>` for the fundamental
plaquette, so the single-variable kinematic range is `w_P in [-1/2, 1]`
(the minimum of `(1/3) Re chi_fund` on `SU(3)` is `-1/2`, at the center
element pair; the maximum is `1` at the identity).

## 2. The derived beta-coupled loop equation

For a link variable `U` appearing in loop words, left multiplication by the
`su(3)` generators and invariance of the Haar measure under `U -> e^{i t T^a} U`
yield, for any word `Tr(U V)` containing `U` once and any Wilson action with
plaquette staples `K_p` attached to `U`:

```
C2 * <Tr(U V)> = -(beta/(4N)) * sum_p [ <Tr(U V U K_p)>
                                        - (1/N) <Tr(U V) Tr(U K_p)>
                                        - <Tr(U V K_p^dag U^dag)>
                                        + (1/N) <Tr(U V) Tr(K_p^dag U^dag)> ]
```

with `C2 = (N^2 - 1)/(2N) = 4/3` at `N = 3` and `beta/(4N) = 1/2` at
`beta = 6`. The four-term bracket is the `SU(N)` completeness (Fierz) form of
`sum_a T^a (X) T^a` applied to the staple insertion; the two staple
orientations produce the daggered pair.

Validation anchors (independent of each other):

- **One-link closed form (runner gate G2).** For the one-link model
  (`V = I`, one staple `K = I`) the identity reduces to
  `(4/3) <Tr U> + (1/2) [ <Tr U^2> - (1/3) <(Tr U)^2> - 3 + (1/3) <Tr U Tr U^dag> ] = 0`
  under the recorded sign convention. Evaluated with the `SU(3)` class-measure
  quadrature of §7 at `beta = 6` the residual is `1.02e-14`; flipping the
  bracket sign gives `3.38` — the sign convention is pinned by an `O(1)`
  margin, not by tuning. During the build this same identity was checked in
  exact high-precision arithmetic to 76 and 54 digits on two independent
  parameterizations.
- **Leading strong-coupling order (documented, not re-run here).** Expanding
  the same identity to `O(beta^2)` around `beta = 0` gives a vanishing
  beta-linear term and leading residual `-beta^2/108` for the naive
  (wrong-sign) variant, and `0` for the recorded one; this was verified
  symbolically during the derivation session and is recorded here as
  provenance, not as a runner gate.
- **All-ones refutation (§4, runner gate G4):** exact rational evaluation.
- **Comb-gauge oracle (§5 context, runner gate G5):** the embedded `D = 2`
  equations hold at the actual `D = 2` Wilson measure to `<= 5.3e-15`.

Haar-moment spec correction (runner gate G1): the six `beta = 0` targets used
to validate the quadrature are `<chi> = 0`, `<|chi|^2> = 1`, `<chi^2> = 0`,
`<chi^2 chibar> = 0`, `<chi^3> = 1`, `<|chi|^4> = 2`. The build-lane spec
sheet had recorded `<chi^2 chibar> = 1`; that value is wrong — a Haar mean is
the singlet content, `chi^2 chibar` carries `SU(3)` N-ality
`1 + 1 - 1 = 1 mod 3 != 0`, and explicitly the decomposition
`3 (x) 3 (x) 3bar = 3 + 3 + 6bar + 15` contains no singlet, so the Haar mean
is `0`. The quadrature reproduces all
six corrected targets to `<= 1.1e-14`; the runner pins the corrected value and
this note records the spec bug so no later lane re-inherits it.

## 3. The exact SDP model (acceptance-contract mapping)

The model builder (embedded verbatim in the runner) turns a JSON equation
payload into an exact-rational constraint system. Both payloads (`D = 2`,
`D = 4`) are embedded in the runner zlib+base64 with pinned sha256 (§7) and
re-parsed at run time; every shape below is re-derived from the payload by the
runner, not asserted.

| Contract item | This note |
| --- | --- |
| Truncation | loop words up to the fixed generation set of the payload: plaquette powers `1..4`, the `1x2` rectangle (`long`/`short` insertions), and in `D = 4` the six-link `L6c1`/`L6c2` chair words, each in all point-group orbits; valid on any torus `L >= 5` (no wraparound identification at these word lengths) |
| Basis / symmetry | words canonicalized under lattice translations plus the point group generated by axis permutations and the global sign flip (order `2 * D!`: 4 in `D = 2`, 48 in `D = 4`); single-axis reflections are NOT quotiented (48, not 384, in `D = 4`), matching the equation-generation convention, so orbit constraints are never over-merged |
| Normalization | `w = <(1/3) Re Tr U_w>` per word; power moments `p_3 = <((1/3) Re Tr U_P)^3> in [-1/8, 1]`, `p_4 = <((1/3) Re Tr U_P)^4> in [0, 1]` |
| Objective | `w_P` (fundamental plaquette moment), maximized and minimized |
| Beta-coupled loop equations | `D = 2`: `SD_P_orbit1`, `SD_R12_long`, `SD_R12_short` (3 equations). `D = 4`: those plus `SD_L6c1_orbit{1,2,3}`, `SD_L6c2_orbit{1,2,3}` (9 equations). All are instances of the §2 identity at `beta = 6`, `N = 3`, with exact rational coefficients |
| Positivity constraints | 4 PSD blocks per dimension: `local_gram` (Gram matrix of loop-word vectors; dim 8 in `D = 2`, 63 in `D = 4`), `plaquette_hankel` (dim 3, moment Hankel in plaquette powers), `plaquette_localize_lo`/`_hi` (dim 2 each, localization of the plaquette moment to `[-1/2, 1]`) |
| Box constraints | per-variable exact bounds from `SU(3)` character ranges (`[-1/2, 1]` for fundamental loop averages; `[-1/8, 1]`, `[0, 1]` for `p_3`, `p_4`) |
| Model inventory (re-derived by runner gate G3) | `D = 2` `CORE_D2_beta6`: 24 variables, 6 additions (4 fresh Gram pairs + `p_3` + `p_4`), 3 equations, PSD dims `[8, 3, 2, 2]`. `D = 4` `CORE_D4_beta6`: 440 variables, 276 additions (274 fresh Gram pairs + `p_3` + `p_4`), 9 equations, PSD dims `[63, 3, 2, 2]` |
| Solver / version | floating stage: Clarabel 0.11.1 via cvxpy 1.9.2 on python 3.13.5 (§6); certification stage: exact rational LDLT inside the stdlib-only runner (no solver) |
| Tolerances / residuals / raw status | §6 tables, quoted from the raw solve records |
| Outward-rounded final intervals | §5 (`D = 2`, certified) and §6 (`D = 4`, floating disclosure) |

The bound applies to any linear functional `<.>` on the truncated word algebra
that is (a) normalized, (b) translation- and point-group-covariant on the
listed orbits, (c) PSD on the four blocks, (d) inside the character boxes, and
(e) satisfies the SD equations — in particular to every `L >= 5` torus Gibbs
expectation at `(N, beta) = (3, 6)` and to any of its thermodynamic limit
points. The relaxation direction is one-sided by construction: enlarging the
feasible set can only widen the bracket, so the certified interval is valid
for the true plaquette moment.

## 4. Refutation theorem: the equations carry beyond-kinematic content

**Theorem (all-ones refutation; runner gate G4, exact rational arithmetic).**
Let `x_1` be the assignment sending every model variable to `1` (the image of
the trivial configuration `U == I` on every link, where every loop word
evaluates to `(1/3) Tr I = 1`). Then in BOTH `D = 2` and `D = 4`:

1. `x_1` is box-feasible (`1` lies in every per-variable box, including
   `p_3 in [-1/8, 1]`, `p_4 in [0, 1]`);
2. `x_1` is exactly PSD-feasible: all 8 blocks (both dimensions) pass an
   exact integer LDLT with the zero-pivot-safe semidefinite test;
3. `x_1` violates EVERY one of the `3 + 9 = 12` SD equations, and the
   violation is the SAME exact rational on all 12: each equation's
   coefficient sum evaluates to `+4/3` (runner prints the deduplicated value
   set `['4/3']` in each dimension and cross-checks the two agree).

Reading: the box + PSD kinematics of §3 admit the frozen configuration; the
beta-coupled equations exclude it with a uniform exact margin equal to the
Casimir constant `C2 = 4/3` of §2 (at `U == I` every four-term staple bracket
cancels pairwise, leaving `C2 * 1 - 0`). This is the precise sense in which
the added equations are *beta-coupled dynamics*, not reparameterized
kinematics — and it is the mechanism behind the §5 upper bound moving off the
kinematic ceiling `1`.

Coverage-completeness diagnostic (floating, §6 records): dropping the
equations and re-solving gives optimum `0.99999999503` (`D = 2`) and
`0.9999995842951337` (`D = 4`) — numerically the kinematic ceiling. ALL
beyond-box content of this relaxation enters through the SD equations; none
leaks in through the Gram/Hankel/localization blocks at this truncation.

## 5. Certified `D = 2` bracket (exact, machine-verified)

The runner (gate G6) embeds two compact rational certificates and re-verifies
them from scratch: it recomputes every equation multiplier contraction, every
box multiplier term, and an exact LDLT PSD test of every Gram matrix, all over
`Fraction`; any nonzero residual raises. The certificate bounds are
*computed by the verifier*, then compared to the note's quoted values — the
runner would fail if this note's numbers drifted from the certified ones.

```
CERTIFIED UPPER:  903482039/1000000000  = 0.903482039
CERTIFIED LOWER: -10000001/20000000     = -0.50000005
```

- Exact pre-rounding certificate values: upper `0.9034820389495550...`
  (outward-rounded by `5.044e-11`), lower `-0.5000000414993565...`
  (outward-rounded by `8.501e-09`).
- The float solves behind the certificates both report `optimal_inaccurate`
  (§6 table); the rationalized dual certificates absorb the solver
  inaccuracy into the Gram slack (upper: `1.84e-08` above the float optimum;
  lower: `4.50e-08` below) and then verify EXACTLY — the certified bounds do
  not depend on solver status.
- **Beyond-box content (upper side):** `1 - 0.903482039 = 0.096517961`. The
  no-equations diagnostic sits at `0.99999999503`, so the entire gap off the
  kinematic ceiling is delivered by the three beta-coupled equations.
- **Floor-pinned content (lower side, disclosed):** the certified lower bound
  is `1/20000000 = 5e-08` WEAKER than the kinematic floor `-1/2`. At this
  truncation the equations do not lift the `D = 2` lower bound off the floor
  (float lower optimum `-0.49999999654`); the certificate is embedded anyway
  so the bracket is two-sided and the certification pipeline is exercised on
  both senses. The lower bound carries no beyond-box information and the note
  claims none for it.
- **Ground truth inside:** the exact `D = 2` plaquette moment (single-
  plaquette measure / comb gauge) is `w_1(beta = 6) = 0.4225317396499868`,
  reproduced by the runner's quadrature to `1.3e-14` against the build-lane
  pin `0.42253173965` (gate G7), and it lies inside the certified bracket.
  Independently, gate G5 checks a comb-gauge transfer-matrix oracle — an
  exact construction of the true `D = 2` expectations, ported to float64 from
  the mpmath build-lane original that closed end-to-end at `<= 1.64e-31` —
  against all three embedded `D = 2` equations in BOTH their raw-JSON and
  built-model forms: residuals `<= 5.4e-15`. The equations are true of the
  actual theory, not merely mutually consistent.

The `D = 2` bracket is deliberately reported at its honest width. The exact
`D = 2` value is known independently (comb gauge); the point of §5 is not the
number but the *pipeline*: at this Gram depth the certified interval
`[-0.50000005, 0.903482039]` demonstrates, in exact arithmetic, that
beta-coupled loop equations produce strictly-beyond-kinematic certified
bounds. That is the contract door, opened.

## 6. `D = 4` floating-point disclosure (NOT certified)

**Certified `D = 4` content of this note: the kinematic box
`w_P in [-1/2, 1]` only.** Everything else in this section is a raw
floating-point record, disclosed per the acceptance contract, and none of it
is a derivation output.

Solver stack: Clarabel 0.11.1 via cvxpy 1.9.2, python 3.13.5, default
tolerances. cvxpy emitted its compilation warning "Constraint #880 contains
too many subexpressions" on the `D = 4` model (record kept verbatim in the
raw solve JSON). Raw records (`schema` fields, per-side status, iterations,
and residuals) are quoted below from the solve files.

| solve | status | optimum (float) | max equality resid | max primal violation | min PSD eig | dual stationarity |
| --- | --- | --- | --- | --- | --- | --- |
| `D=2` upper | `optimal_inaccurate` | `0.9034820205210564` | `2.7e-13` | `2.7e-13` | `-4.1e-25` | `3.7e-09` |
| `D=2` lower | `optimal_inaccurate` | `-0.49999999654264193` | `7.9e-17` | `1.7e-09` | `-1.7e-09` | `1.4e-08` |
| `D=4` upper | `optimal_inaccurate` | `0.9999986557099539` | `3.3e-16` | `6.9e-15` | `-6.9e-15` | `4.0e-07` |
| `D=4` lower | `optimal_inaccurate` | `-0.4999999360750449` | `2.1e-14` | `2.2e-09` | `-2.2e-09` | `1.3e-07` |
| `D=4` no-equations diagnostic | (diagnostic) | `0.9999995842951337` | — | — | — | — |

Why the `D = 4` floats are not certified here — quantified: the float margins
to the kinematic box are hair-thin (`1 - 0.9999986557 = 1.34e-06` on the
upper side, `6.4e-08` on the lower side), while the dual-side inaccuracy that
exact certification must absorb into the Gram slack is `~4.0e-07` per the
table, spread across a 63-dimensional block. Running the same
rationalize-and-absorb certification used in §5 on the `D = 4` records
produces certified bounds that land OUTSIDE the box — upper
`1.0000002983566258` at denominator cap `10^7`, `~1.00000031` at cap `10^10`;
lower `-0.5000004220856789` at cap `10^10` (a 14192-digit-numerator
certificate that verifies exactly and is weaker than the floor). Increasing
the rational precision does not help, because the obstruction is the dual
infeasibility of the float solution, not the rounding. So at this Gram depth
the exactly-certifiable `D = 4` statement is the box, and this note says so
rather than embedding a decorative certificate.

The `D = 4` float interval `[-0.4999999361, 0.9999986557]` does contain the
fenced comparator `0.5934` (audit-only context, one-hop authority's license;
gate G7 checks the comparator lies inside the certified `D = 4` content, i.e.
the box). No claim beyond the box is made in `D = 4`.

What this opens (named dial): the Gram DEPTH. The `D = 4` word basis behind
the 63-dim `local_gram` block is the shallowest one that carries all 9
equations. The next path this opens is a deeper Gram basis (longer words in
the Gram vectors, keeping the same 9 equations) and/or a `D = 4` solve
converging to `optimal` (not `optimal_inaccurate`) so the §5
rationalize-and-absorb certification closes in `D = 4` the way it closes in
`D = 2`; the §5 pipeline needs no modification to consume such a solution —
the runner's verifier is dimension-agnostic and already builds and pins the
full `D = 4` model.

## 7. Runner gate map (51 checks)

Stdlib-only (no numpy/scipy/sympy/mpmath/cvxpy at run time); embedded
payloads re-checked against pinned sha256 of the raw bytes at every run:

```
sd_equations_beta6_2d.json  b512c0fbb43e568c4adc333ff5f7146ab183140ccc21aabea1f478811fc6e4f1
sd_equations_beta6_4d.json  bed5ead58e68dcb5f2b7dd10af2c304231a7494604171bc6a2de44051bbb5e8d
cert_2d_upper_compact.json  733b45e35f0a986d5341e201962d197e8387eb94290a017e245b238825ad3776
cert_2d_lower_compact.json  d66b660f180809e89e220c332c60ad5006253b0147bec2cac9323918657a877d
```

- **G1 (6 checks):** `SU(3)` class-measure quadrature reproduces the six
  corrected Haar moments at `beta = 0` to `<= 1.1e-14` (tolerance `1e-9`),
  including the spec-bug correction `<chi^2 chibar> = 0`.
- **G2 (1):** one-link `beta = 6` SD residual `1.02e-14` under the recorded
  sign convention.
- **G3 (14):** payload meta pins (`D`, `N = 3`, `beta = 6`, `L_min = 5`);
  JSON inventories `19/165` variables, `3/9` equations, one `const`; model
  names; PSD dims `[8,3,2,2]`/`[63,3,2,2]`; model inventories
  `(24,6,3)`/`(440,276,9)`; the 12 equation ids; objective `w_P` in both;
  fresh Gram pairs `(4, 274)`.
- **G4 (13):** all-ones refutation theorem, §4, exact rational: box
  feasibility, 8 exact LDLT PSD passes, per-dimension uniform violation
  `+4/3`, cross-dimension agreement.
- **G5 (10):** comb-gauge oracle self-checks (4, vs the quadrature) and all
  three `D = 2` equations in raw-JSON and built-model form, residuals
  `<= 5.4e-15` (tolerance `1e-10`).
- **G6 (2):** exact rational verification of both embedded `D = 2`
  certificates; bounds match the §5 values exactly.
- **G7 (5):** exact `D = 2` value matches its pin and lies inside the
  certified bracket; certified upper strictly `< 1`; certified lower
  `<= -1/2` (disclosed epsilon); fenced `D = 4` comparator inside the
  certified `D = 4` content (the box).

## 8. Boundary / honest auditor read

- **What is certified:** the `D = 2` bracket of §5 (exact rational
  certificates re-verified at every run), the §4 refutation theorem (exact
  rational), and the §7 pins. Nothing else.
- **What is NOT certified:** any `D = 4` statement beyond the kinematic box.
  The §6 numbers are floating-point disclosures with `optimal_inaccurate`
  statuses, reported because the acceptance contract demands raw solver
  honesty, not because they carry certified weight.
- **This note does not complete the `beta = 6` gate.** The gate's target is
  the reproduction of the nonperturbative `D = 4` plaquette value; this note
  lands the contract-named machinery (repo-owned, beta-coupled, exactly
  certifiable) and proves its content is beyond-kinematic, with the certified
  beyond-box bracket so far in `D = 2` only. The `D = 4` beyond-box
  certification is the next step on the named dial (§6), not a claim of this
  note.
- **The `D = 2` lower bound is floor-pinned:** `-0.50000005` is epsilon-weaker
  than the trivial floor `-1/2`; it demonstrates two-sided certification
  plumbing, not lower-side physics content, and the note claims none.
- **Truncation honesty:** the bracket width (`~0.90` upper vs exact `0.4225`)
  is the honest price of the shallow word set; the §5 point is exact
  beyond-kinematic certification through beta-coupled equations, not a tight
  interval. Tightness improves on the Gram-depth dial; no tightness beyond
  the printed interval is claimed.
- **Comparator fencing:** `0.5934` appears only in gate G7's box-membership
  check and in §6 prose, both explicitly audit-context; it enters no
  constraint, objective, certificate, or derived number.
- **Spec-bug disclosure:** the corrected Haar target `<chi^2 chibar> = 0`
  (§2) is itself derived (N-ality / no singlet in `3 (x) 3 (x) 3bar`),
  runner-pinned, and flagged so downstream lanes inherit the correction.

🤖 Generated with [Claude Code](https://claude.com/claude-code)
