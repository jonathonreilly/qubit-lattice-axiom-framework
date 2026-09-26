---
claim_id: admissibility_rule_in_the_cube_kinetic_family_relabellings_in_time_fix_the_kinetic_shape_and_the_frames_full_rate_has_four_numbers_of_which_blindness_removes_one_bounded_theorem_note_2026-09-26
claim_type: bounded_theorem
claim_scope: "WITHIN block 62's member as landed (R1, R2, the rates' multiplier u, K), with block 62's cube kinetic family T = M1 sum h'_jj^2 + M2 sum_{i<j} h'_ii h'_jj + M3 sum_{i<j} h'_ij^2 plus a coefficient N on the frame's rotation rate, and relabellings acting on the frame by d eps = -xi p^T, at one wave vector and second order in the fields: (T1) the gradient relabelling in time is a symmetry (the Lagrangian changing by a total time derivative) iff (M1, M2, M3) = (0, c, -c) with the multiplier shifting by (c/K) zeta'' (the only shift among zeta to zeta'''), N free; the transverse relabelling iff (M, 2M, 0), N = 0, no shift; both only for the zero kinetic term; (T2) quadratic forms in the frame's full rate invariant under the cube group have exactly four numbers, and blindness to coin rotations in time removes only the antisymmetric one, leaving three, so block 124's count of two uses its premise that the kinetic term is built with the metric alone; rotation blindness with the gradient demand leaves block 62's member at beta = -alpha; (T3) the survivor (0, c, -c), c = -2 alpha, has one travelling pair (transverse traceless, X = K p^2/(4 alpha)), the gradient gauge direction, drifting transverse relabellings, and a decoupled rotation block. Exact (sympy). A harvest of probe #9225 (Claude Opus 5.5, the supervisor's family) confirmed by an other-family referee (#9312); nothing adopted; no gravitational claim."
upstream_dependencies:
  - minimal_axioms
runner: scripts/admissibility_rule_in_the_cube_kinetic_family_relabellings_in_time_fix_the_kinetic_shape_2026_09_26.py
---

# In the cube kinetic family, relabellings in time fix the kinetic shape, and the frame's full rate has four numbers of which blindness removes one

**Date:** 2026-09-26
**Type:** bounded_theorem
**Status:** bounded-support (exact at one wave vector and second order in the fields; a harvest of probe #9225, confirmed by an other-family referee in #9312; nothing adopted or registered; unaudited)

This note works within blocks 62, 101 and 124 as landed on main (the member, its kinetic family, the rate as a multiplier and blindness to coin rotations in time); it reports which kinetic terms of the cube family the relabellings in time allow, and how many numbers the frame's full rate carries; nothing is adopted and no gravitational claim is made.
No bridge, Born-weight, plane-or-sum or gravity statement enters this note as a premise; this note does not fire wake condition 1 of the parked statistical-bridge decision.
No value, constant or theorem is imported as authority; the standard mathematical imports are named at definition level.

## Result up front

Block 124 (landed) showed two things. Blindness to coin rotations that vary in time leaves block 62's two kinetic numbers. And no ratio of them makes a transverse relabelling in time a symmetry. This note, a harvest of a probe result another model family has confirmed, does the same in the cube's own kinetic family, with the frame's rotation rate included.

- **T1: each relabelling in time fixes the shape.**
  - A gradient relabelling is a symmetry only for `(M₁, M₂, M₃) = (0, c, −c)`, with the rates' multiplier shifting by `(c/K)ζ''`.
  - A transverse one is a symmetry only for `(M, 2M, 0)`, with no rotation-rate term and no shift.
  - Only the zero kinetic term satisfies both.
- **T2: four numbers, and blindness removes one.** With the cube's symmetry, the frame's full rate allows exactly four quadratic numbers. Blindness to coin rotations in time removes only the antisymmetric one and leaves three. So block 124's count of two uses its stated premise that the kinetic term is built with the metric alone. That premise is not a consequence of blindness.
- **T3: what the survivor carries.** The survivor `(0, c, −c)` has:
  - one travelling pair, transverse and traceless;
  - the gradient gauge direction;
  - drifting transverse relabellings;
  - a decoupled rotation block.

In plain terms: the rules for resetting clocks pin down the member's kinetic energy up to one number, but only once blindness to the coin's axes and the metric-only premise are both in place. Blindness alone leaves one more number free.

## Premises and declared objects

- **Axioms.** The axioms memo (`docs/MINIMAL_AXIOMS_2026-06-29.md`) was read in full on 2026-09-26.
  - "No possibility is privileged." "No site is privileged."
  - "Admissibility is not a dynamics axiom."
  - The member, its kinetic family and the relabellings are supplied clauses. Nothing is adopted.
- **The member** (block 62, landed): `R₁ = p² tr h − p·h·p` and `R₂`, the rates' multiplier `u`, and `K`, with the Lagrangian `L = T + K(uR₁ + R₂)`. The frame is `E = 1 + ε`, with `h = −(ε + εᵀ)` and rotation part `ω`.
- **The cube kinetic family** (block 62): `T = M₁ Σ h'_jj² + M₂ Σ_{i<j} h'_ii h'_jj + M₃ Σ_{i<j} h'_ij²`, plus `N Σ ω'_ij²`.
- **Relabellings.** `δε = −ξ pᵀ`. The gradient kind is `ξ ∝ p ζ(t)`; the transverse kind is `ξ = (p × b) ζ(t)`.
- **Block 124** (landed): the kinetic term is "a constant-coefficient ultralocal quadratic form in `V` built with the metric alone".
- **Standard imports, named at definition level.**
  - The variational derivative, which annihilates total derivatives.
  - Invariant theory of the cube group on 3 × 3 matrices.
  - Minors of a matrix pencil.
  - Exact symbolic algebra.

## Theorem T1 — each relabelling in time fixes the shape

*Statement.*
- **Gradient.** With `δh = ppᵀζ(t)` and `u → u + Σ_{n≤3} c_n ζ^{(n)}`, the Lagrangian changes by a total time derivative iff `(M₁, M₂, M₃) = (0, c, −c)` and `u → u + (c/K)ζ''`. The change is then `d(cζ′R₁)/dt`, and `N` is free.
- **Transverse.** With `ξ = (p × b)ζ(t)`, it changes by a total derivative iff `(M₁, M₂, M₃) = (M, 2M, 0)`, `N = 0`, and there is no shift. The Lagrangian is then unchanged.
- **Both.** Only `(0, 0, 0)` with `N = 0`.

*Proof.* Every variational derivative of the change must vanish, and the explicit total derivative gives the converse (runner B1). ∎

## Theorem T2 — four numbers, and blindness removes one

*Statement.*
- Quadratic forms in the frame's full rate `V` (nine components) invariant under the cube group (`V → RVRᵀ`) are exactly the span of `Σ V_jj²`, `Σ V_iiV_jj`, `Σ sym(V)_ij²` and `Σ antisym(V)_ij²`, with no cross term.
- Blindness to coin rotations in time, `V → V + (antisymmetric)`, holds iff the antisymmetric coefficient vanishes. That leaves three numbers.
- Block 124's count of two therefore uses its premise that the kinetic term is built with the metric alone.
- The gradient demand leaves `N` free, and the transverse demand forces `N = 0`. Rotation blindness together with the gradient demand leaves block 62's member at `β = −α`.

*Proof.* Invariance under a quarter turn, a third turn about the body diagonal, and inversion. Then the coefficients' conditions (runner C1). ∎

## Theorem T3 — what the survivor carries

*Statement.* Take the survivor `(0, c, −c)` with `c = −2α`.
- At the rational wave vectors `p = (1,2,2)` and `(2/5, 1/3, −3/7)`, the `(h, u)` pencil `XA + C` has normal rank 6.
- The gcd of its maximal minors has the double root `X = p²/4`, which is the travelling transverse traceless pair, and otherwise only `X = 0`.
- The gradient gauge vector, `(ppᵀ, u = 2αX/K)`, is null at every `X`.
- The rotation block decouples, with determinant `(2NX)³`.

*Proof.* Minors of the pencil and its null space at `X = p²/4` (runner D1). ∎

## What this settles and what it does not

- **Settled.** In the cube family, the relabellings in time fix the kinetic term's shape up to one number, and the gradient and transverse demands are incompatible. Blindness to coin rotations removes exactly one of the four cube numbers.
- **For landed block 124.** Its count of two rests on its stated metric premise, which is not a consequence of blindness. The landed note states that premise, so no correction to it is owed.
- **Not settled.**
  - Orders beyond the second in the strain.
  - A field for the drifting transverse relabellings.
  - What fixes `α/K`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "block 124's kinetic count and relabellings in time in the cube family (probes task relabelling-blindness-in-the-cube-kinetic-family)"
source_of_blocker_text: probes task J:derive:relabelling-blindness-in-the-cube-kinetic-family
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "orders beyond the second; a field for the drifting transverse relabellings"
conditional_surface_status: "one wave vector; second order in the fields; the cube kinetic family with the rotation-rate coefficient"
hypothetical_axiom_status: "the member, its kinetic family and the relabellings are supplied; nothing adopted"
admitted_observation_status: null
audit_required_before_effective_retained: true
```

## Prior art and what is new

- **Blocks, as landed.**
  - Block 62: the member and its kinetic family.
  - Block 101: the rate as a multiplier.
  - Block 124: blindness in time leaves two kinetic numbers under the metric premise, and no ratio makes a transverse relabelling a symmetry.
- **Probes.**
  - #9225, worker `w-macbookpro9927a-jf51d`, Claude Opus 5.5, the supervisor's own model family, found T1–T3. Its T1 agrees with block 124 T5 by an independent derivation.
  - #9312, a Grok worker, another model family, refereed it: "HIT: confirmed - gradient relabelling fixes (0, c, -c) with shift (c/K) zeta'', transverse relabelling fixes (M, 2M, 0) with no shift, and only the zero term satisfies both."
- **In the literature.**
  - The supermetric whose ratio `β = −α` is (DeWitt).
  - Reference only.
- **New here.** The harvest, with T2's observation about block 124's premise.
- **Provenance.** Found by the supervisor's family and confirmed by another family.

## Exact target and obligation graph

Target: the cube kinetic family under relabellings in time and coin blindness. The obligations are:
- (O1) the premise (A3);
- (O2) the relabellings (B1);
- (O3) the cube numbers and blindness (C1);
- (O4) the survivor's modes (D1).

## No-Go Discipline Gate

The note's negative sentences:
- no nonzero cube kinetic term keeps both relabellings in time;
- blindness alone does not reduce the cube family to two numbers.

### N1 — Attack routes and the scope they leave
Attack routes, each tested here:
1. *A multiplier shift rescues both.* The shift up to `ζ'''` is included, and only the zero term survives (B1). ATTEMPTED.
2. *Cube invariance allows cross terms that blindness kills.* There are no cross terms (C1). ATTEMPTED.
3. *The survivor has more travelling modes.* Only the transverse traceless pair travels (D1). ATTEMPTED.

Scope left open:
- higher orders;
- other fields.

### N2 — Wall-independence audit
No no-go wall of the repository is used.

### N3 — Hidden-wall scan
- The note was re-read for "we assume", "by construction", "as is standard", "the framework provides", "background", "naturally", "obviously", "registered" and "canonical".
- One wave vector and second order in the fields are declared.

### N4 — Per-citation table
| Citation | Role | Load-bearing? |
|---|---|---|
| `minimal_axioms` | no possibility or site privileged; no dynamics in the axioms | yes |
| blocks 62, 101, 124 (landed) | the member, the multiplier, the premise | yes (124 quoted, A3) |
| probe #9225 and referee #9312 | the result and its confirmation | yes (ported, rerun) |

### N5 — Resolution audit
| Claim | per_element | per_site | per_mode | per_block | lattice_wide |
|---|---|---|---|---|---|
| "the shape fixed; four numbers, blindness removes one; one travelling pair" | executed: the variational conditions | executed: the cube forms | executed: the pencil at two wave vectors | executed: the union of demands | not executed: higher orders; other fields |

### N6 — Partial-closure paths and primitive scan
No registered primitive is used; nothing is proposed for registration.

### N7 — Steelman
- *Objection:* "This only restates block 124."
  - *Reply:* T1 agrees with block 124 T5 by an independent derivation.
  - T2 is new. In the cube's own family, blindness leaves three numbers, not two, so block 124's metric premise is doing work.

### N8 — Cross-cycle echo
- Block 124: two numbers under the metric premise.
- This note: three under the cube's symmetry and blindness alone.

## Falsifiers

- A nonzero cube kinetic term keeping both relabellings in time.
- A fifth cube-invariant quadratic number, or a cross term.

## Boundaries and non-claims

- One wave vector.
- Second order in the fields.
- The cube family with the rotation-rate coefficient.
- Nothing is adopted and no gravitational claim is made.

## Imports

- `minimal_axioms`. Blocks 62, 101 and 124 (landed), restated and quoted.
- Named standard imports, at definition level:
  - the variational derivative;
  - invariant theory of the cube group;
  - minors of a pencil;
  - exact symbolic algebra;
  - the supermetric (DeWitt), as a comparator.

## Review record

- **Who and when.** Supervisor-run harvest block (Claude Opus 5.5), 2026-09-26, during the owner's 12-hour campaign.
- **Provenance.** Probe #9225 (Claude Opus 5.5), refereed by #9312 (a Grok worker, another family). The supervisor ported the probe's exact checker.
- **Before writing.** The own prior-art check covered memory, open PRs and main. It found block 124 and its premise, and no earlier harvest.
- **Mutation census.** At least one mutation per science family, each failing in its own family, and two in family F.

## Verification

```bash
PYTHONPATH=scripts python3 scripts/admissibility_rule_in_the_cube_kinetic_family_relabellings_in_time_fix_the_kinetic_shape_2026_09_26.py
```

Expected: `TOTAL: PASS=11 FAIL=0`.
