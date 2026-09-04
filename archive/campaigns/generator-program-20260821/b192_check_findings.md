# Block 192 adversarial check — first-order hybridization mechanism

Date: 2026-08-25

Status: **COMPLETE — exact reconstruction, independent derivative probe, and
adversarial synthesis finished.**

## Scope and arithmetic contract

This is a scratchpad-only adversarial computation. It does not edit a landed
note, runner, audit surface, branch, commit, or ledger row.

Construction authority is restricted to:

- `docs/ADMISSIBILITY_DIRAC_KAHLER_WIDTH_FAMILY_TRANSFER_MONODROMY_BOUNDED_THEOREM_NOTE_2026-08-25.md` for the wrap-edge width family, `K_c`, `L_k`, `V`, `W`, the core conventions, and the displayed `v=1` Hodge block;
- `docs/ADMISSIBILITY_DIRAC_KAHLER_BOUNDARY_MODE_VOLUME_SENSITIVITY_BOUNDED_THEOREM_NOTE_2026-08-25.md` for the volume-profile extension, boundary table, bump construction, and touch/cross validity rule;
- the explicitly requested b191 check record only for its stated `v` convention and finite-`delta` probe data.

Fixture: `m=9/20`, `c=5/13`, `T=16`. All construction and response arithmetic
uses exact SymPy `Integer`/`Rational` entries and exact polynomial arithmetic
over `QQ`. `nsimplify` is forbidden and is not used. Decimal approximations, if
any are included later, are presentation-only evaluations of exact results.

## Target contract

Audit C1--C4 and P1--P2 exactly. The package is refuted if any displayed
derivative identity, any one of the ten proposed trace-response rationals, any
projector congruence, the sum rule, the locking inequalities/sign statements,
or the extra-position claim fails under the landed construction.

The required independent check for C1 compares the propagated differential
chain against separately rebuilt exact-rational finite differences of
`W(delta)` at two rational steps with Richardson elimination; equality to the
same hard-coded target is not accepted as an independent route.

## Findings log

### Construction controls

The independent rebuild reproduces the baseline characteristic polynomials
exactly:

- at `t0=1`, `heavy * light^2 * boundary`;
- at `t0=3`, `heavy^2 * light^2`;

with the three factors exactly as stated in the assignment. It also gives
`Ps H Ps-H=0` and `Ps Q Ps-Q^T=0` entrywise.

### C1 — derivative chain: CONFIRMED exactly

Differentiating the displayed Block-105 law at `v=1-delta` gives

```text
dB = [ -1       0         0      0 ]
     [  0   -169/144   65/144    0 ]
     [  0    65/144  -169/144    0 ]
     [  0       0         0      1 ],
```

exactly the proposed
`-E00-(169/144)(E11+E22)+(65/144)(E12+E21)+E33`.

For each bump, `dH` includes both positive anchors and the image anchors whose
`thA_s(t)=-1-t` partners are bumped, with `P4 dB P4^T` on those image anchors.
An entrywise symbolic differentiation of the full displayed profile gives

```text
nnz(dH_symbolic-dH_cell_sum) = 0,
nnz(dQ_symbolic-[m dH+dH D-D^T dH]) = 0.
```

For both bumps and both cores, all remaining defining-equation residuals are
also exactly zero:

```text
nnz(Q dG + dQ G)             = 0,
nnz(dG Q + G dQ)             = 0,
nnz(dK W + K dW - dL2)       = 0.
```

Thus `dG=-G dQ G` and `dW=K^-1(dL2-dK W)` close on both the left- and
right-inverse equations. As construction fingerprints, both requested bumps
give `nnz(dH)=56`, while `nnz(dQ)=200` for `{3,4}` and `152` for `{2,3}`;
all four requested `dW` matrices have 64 nonzero entries.

Independent route: I rebuilt `W(delta)` at exact rational
`delta=1/100,1/200`, formed exact forward differences over `QQ`, and applied
the exact first Richardson elimination `2 D(1/200)-D(1/100)`. In every one of
the four `(bump,core)` cases, the max-entry errors obeyed, by exact rational
comparison,

```text
E(1/200) < E(1/100),
E_Richardson < E(1/200).
```

No finite-difference value was fed into the derivative chain.

### C2 — the ten rationals and the sum rules: CONFIRMED exactly

The independently computed projector traces reproduce all ten proposed
rationals digit for digit:

| bump | core | factor | exact `tr(P_f dW)` |
| --- | ---: | --- | ---: |
| `{3,4}` | 1 | heavy | `840153195543/196300900625` |
| `{3,4}` | 1 | boundary | `59790687128721117/13862573301236875` |
| `{3,4}` | 1 | light | `21615004253318/12284407006475` |
| `{2,3}` | 1 | heavy | `-421462341183472199/177215545561734375` |
| `{2,3}` | 1 | boundary | `-29381217534120895221181/12514784612024119828125` |
| `{2,3}` | 1 | light | `22866757183474123654/19424018367789224675` |
| `{3,4}` | 3 | heavy | `-152770523741944777898/10738971376744546875` |
| `{3,4}` | 3 | light | `-6227354334614993838/3884803673557844935` |
| `{2,3}` | 3 | heavy | `-1495288291042/1427461510575` |
| `{2,3}` | 3 | light | `-2705696606558/2456881401295` |

The exact trace/sum values are:

| bump | core | `tr(dW) = sum_f tr(P_f dW)` |
| --- | ---: | ---: |
| `{3,4}` | 1 | `2702603990428664601847792/261056210615088396173125` |
| `{2,3}` | 1 | `-1322424657623802056150231913430788608/372647692749599431888443061718296875` |
| `{3,4}` | 3 | `-83526662690302770407422046496832/5276875808912607540299962640625` |
| `{2,3}` | 3 | `-953207325986164736/443602221410818725` |

All four sum-rule residuals are exactly zero.

### P1 — projector congruences and squarefree replacement: CONFIRMED

For the characteristic-polynomial multiplicities stated in the assignment, I
constructed each CRT polynomial as

```text
q_f = M_f * (M_f^-1 mod f^m) mod chi_W,
M_f = chi_W/f^m.
```

Every full-multiplicity congruence has zero polynomial residual over `QQ`:
`q_f-1` modulo its own `f^m`, and `q_f` modulo every other powered factor.
The same is true for the CRT system formed from the squarefree total. Moreover,
the squarefree total annihilates `W` entrywise, both projector families sum to
`I_8`, and

```text
P_f(full multiplicities) - P_f(squarefree total) = 0_8
```

for every factor at both cores. Hence the trace responses are unchanged; the
equality is stronger than trace-only agreement.

### C3 — locking law: REFUTED as stated

The sign statements survive: the heavy and boundary responses are both
positive for `{3,4}`, both negative for `{2,3}`, and the light response is
positive at both positions. The two heavy/boundary differences are also
exactly nonzero:

```text
{3,4}: |heavy-boundary| = 61132656/1842661567 != 0,
{2,3}: |heavy-boundary| = 56249856/1842661567 != 0.
```

But the claimed `<1% relative at BOTH bump positions` fails at `{2,3}` under
each standard normalization. The exact relative errors are

```text
relative to |heavy|:
  29387041378056000000/2289480697848894093937 > 1/100,
relative to |boundary|:
  29387041378056000000/2260093656470838093937 > 1/100,
symmetric percent difference 2|h-b|/(|h|+|b|):
  29387041378056000000/2274787177159866093937 > 1/100.
```

For `{3,4}`, all three corresponding exact ratios are below `1/100`, so this
is a one-position failure, not a convention-wide failure. The only way to make
`{2,3}` fall below 1% is the nonstandard half-sized normalization
`|h-b|/(|h|+|b|)` without the conventional factor of two.

### C4 — zero refinement: CONFIRMED, with the b191 zero identified

All ten C2 components are nonzero. The b191 `{2,3}` zero occurs at the
different core `t0=5` and is much stronger than a particular root shift or
resultant:

```text
W_{bump {2,3}, delta=1/5}(t0=5) - W_0(t0=5) = 0_8 entrywise.
```

The underlying pairings are not individually fixed:

```text
nnz(K(delta)-K(0))  = 64,
nnz(L2(delta)-L2(0)) = 60,
L2(delta)-K(delta) W_0 = 0_8.
```

Thus the exact cancellation is at the whole monodromy operator. Its first
derivative also vanishes entrywise, `dW(t0=5)=0_8`; the same finite operator
identity was independently seen at `delta=1/7`, though only `delta=1/5` was
required. It is not one of the ten requested components because those live at
`t0=1` and `t0=3`.

### P2 — extra bump `{4,5}`: allowed, but nontrivial locking does not persist

The profile is allowed at `T=16`: `{4,5}` lies in the positive-anchor domain
`{0,...,7}`, and the tested `t0=1` pairing is interior because `t0+3=4<8`.
The exact first-order triple is

```text
(heavy, boundary, light) = (0, 0, 0).
```

This is a trivial equality, not persistence of the nonzero heavy/boundary
locking mechanism. In fact the full `t0=1` monodromy is unchanged at both
`delta=1/5` and the extra exact check `delta=1/7`, even though at `delta=1/5`
both `K` and `L2` move in all 64 entries and still satisfy
`L2(delta)=K(delta) W_0` exactly.

## Verdict summary

| item | verdict |
| --- | --- |
| C1 | **CONFIRMED exactly**, including image-partner contributions and zero defining-equation residuals; independent exact-rational finite differences converge after Richardson elimination |
| C2 | **CONFIRMED exactly**: all ten rationals and all four sum rules |
| C3 | **REFUTED as stated**: sign flip and light sign stability hold, but `{2,3}` exceeds 1% under reference-relative and symmetric standard definitions |
| C4 | **CONFIRMED exactly**: ten nonzero components; the b191 zero is whole-operator invariance at `t0=5` |
| P1 | **CONFIRMED exactly**: all CRT congruences; full and squarefree projectors agree entrywise |
| P2 | `{4,5}` is **valid**, but the exact triple is **`(0,0,0)`**; nonzero locking does not persist |

Overall: **REFUTE THE PACKAGE AS STATED.** The derivative mechanism and the
ten proposed first-order components are correct, but the advertised locking
threshold is false at one of its two required positions. A repair must replace
“`<1% relative at both bump positions`” with an explicitly normalized, true
statement. Under the conventional symmetric percent difference, `{3,4}` is
below `1/100` and `{2,3}` is above `1/100`, by the exact ratios displayed
above. The extra-position result should also be recorded as an exact support
cutoff, not as persistence of nonzero heavy/boundary locking.

## Reproduction

Run:

```text
python3 /private/tmp/claude-502/-Users-jonBridger-Projects-Physics-baremetal-probes--claude-worktrees-gravity-toe-lane-work-427b0b/25068357-42e8-431c-96c9-c149512f0305/scratchpad/b192_exact_check.py
```

The checker imports no block-190 or block-191 runner. It rebuilds the carrier,
Hodge profile, glue, action, inverse, pairings, monodromy, derivatives, and CRT
projectors directly from the displayed construction. It uses no floating-point
construction arithmetic and never calls `nsimplify`.
