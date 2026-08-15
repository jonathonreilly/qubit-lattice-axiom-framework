---
claim_id: f_mix0_three_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the F_cut map (1,0,1,1,0) fills 188 of the 220 three-site seeds. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_mix0_three_site_coverage_2026_08_15.py
---

# Three-Site Coverage Of The Mixed3-Silent Opp2=0 Twin Of L1

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock coverage of the displayed F_cut map
`(1, 0, 1, 1, 0)` on the twelve-vertex two-cube with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_mix0_three_site_coverage_2026_08_15.py`](../scripts/f_mix0_three_site_coverage_2026_08_15.py)

## Result up front

On the two-cube with off-patch occupancy `0`, the F_cut remaining-bit map

```text
f_mix0 = (wt1, opp2, adj2, vertex3, mixed3) = (1, 0, 1, 1, 0)
```

is L1’s `opp2=0` twin with silent mixed3. L1 itself is the remaining-bit
map `(1, 0, 1, 1, 1)`. The two maps tie on 2-site coverage inside F0
(`cov2 = 62`, #6434). They do **not** tie on 3-site coverage.

```text
cov3(f_L1) = 220
cov3(f_mix0) = 188
```

The #6437 splitter `S = {(0, 0, 0), (0, 0, 1), (2, 0, 0)}` is a miss for
`f_mix0` and is one of several 3-site misses: `220 − 188 = 32` three-site
seeds stall unfilled. This is a new number. Not leftover-character of #6437
(that named one seed). Not leftover-character of #6456 (that reported
`cov3(f0)` for the different map `(1, 1, 1, 1, 0)`). Displayed, not adopted.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed occupancy
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "cov3(f_L1)=220 is reconfirmed, the #6437 splitter is a miss for f_mix0, and cov3(f_mix0)=188 is computed exactly on the declared two-cube. The map is displayed, not adopted as a physical formation law."
trace_class: negative_route_pruning
target_claim_id: f_mix0_three_site_coverage
target_blocker_text: "report three-site coverage of the mixed3-silent opp2=0 twin of L1"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep f_mix0 displayed-only; do not promote mixed3 silence into Admissibility"
conditional_surface_status: "exact for occupancy-to-lock coverage on the twelve-vertex two-cube with off-patch occupancy 0; no physical law selection"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md).

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.
There is one fixed nearest-neighbor admissibility rule, covariant under lattice
translations and proper cubic rotations. Records form. When present, a record
locks exactly one admissible local possibility. A readout value is determined
by record content alone. A site with no record cannot be read. Admissibility
does not supply the formation site, probability, or rate. Admissibility is not
a dynamics axiom.

The following are declared finite scaffolding, not measured or fitted physics
inputs:

- the six-ray neighbor stencil
  `{+e_x,-e_x,+e_y,-e_y,+e_z,-e_z}` and the 24 proper cube rotations;
- occupancy cells `{0,1}^6`, partitioned into ten axis-type orbits;
- the cube-covariant class `F_cut` of maps with `f(empty)=f(full)=0` and
  `f(c)=f(1-c)`, leaving five free remaining bits
  `(wt1, opp2, adj2, vertex3, mixed3)`;
- the twelve-vertex two-cube `{0,1,2} × {0,1} × {0,1}`;
- occupancy-to-lock dynamics with off-patch occupancy `0` (a blank-block is a
  different rule);
- two-site seeds, of which there are `66`, and three-site seeds, of which
  there are `220`.

A seed is filled when iterated lock updates occupy all twelve vertices.

## Exact target and objects

**Theorem 1.** Reconfirm `cov3(f_L1) = 220`. The #6437 splitter
`S = {(0, 0, 0), (0, 0, 1), (2, 0, 0)}` is a miss for `f_mix0`.

**Theorem 2.** Report `cov3(f_mix0)`. The computed value is
`cov3(f_mix0) = 188`. Thirty-two of the 220 three-site seeds are unfilled.
The #6437 splitter is one of those several misses.

**Theorem 3.** Display `f_mix0`. Do not adopt `f_mix0`. Do not write
`f_mix0` into Admissibility.

## Claim scope

On the two-cube with off-patch o=0, the F_cut map (1,0,1,1,0) fills 188 of the 220 three-site seeds.
Displayed, not adopted.

## No-Go Discipline

The negative result is only that the mixed3-silent `opp2=0` twin of L1 is not
a 3-site maximizer. It is not a universal no-go against other F_cut maps or
against a later derived formation law.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| replace `f_L1` by Hamming parity | **ATTEMPTED** | Hamming disagrees with unbalanced-axis `n_μ ≠ 0` on the six-ray cells |
| treat `cov3(f_mix0)` as leftover-character of #6437 | **ATTEMPTED** | #6437 named one 3-site splitter seed; this note counts all 220 seeds |
| treat `cov3(f_mix0)` as leftover-character of #6456 | **ATTEMPTED** | #6456 reported `cov3(f0)` for the different remaining-bit map `(1, 1, 1, 1, 0)` |
| adopt `f_mix0` because it ties L1 on 2-site coverage inside F0 | **ATTEMPTED** | the 2-site tie `#6434` does not imply a 3-site tie |
| read silent mixed3 as a physical selector | **ATTEMPTED** | mixed3 silence is a remaining-bit choice, not an Admissibility derivation |
| replace off-patch occupancy `0` by a blank-block | **ATTEMPTED** | a blank-block is a different rule |

### N2 — wall independence

One type wall is claimed: `f_mix0` does not fill every three-site seed. The
#6437 seed is one miss among 32, not a second wall. No inflated wall count
is used.

### N3 — hidden-wall scan

The two-cube, off-patch occupancy `0`, remaining-bit labels, and seed families
are all declared. No full-lattice formation law, blank-block, Hamming
substitute, or adopted selector is imported.

### N4 — residual matching

The residual after #6437 and #6456 was the three-site coverage of `f_mix0`.
This note reports that new number. It neither closes a physical formation
law nor enlarges the axiom set.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — f_mix0 and f_L1 are scored on the 220 three-site seeds
per-block: executed — cov3(f_mix0) is the mixed3-silent three-site coverage on this patch
lattice-wide: not executed — no Z^3-wide formation law or physical Admissibility selector is claimed
```

### N6 — partial-closure paths

A later derived formation kernel, a larger patch, or a different off-patch
rule could change coverage counts. Those routes remain live and need not
alter the axioms.

### N7 — steelman

The strongest objection is that mixed3 silence is only a display choice and
that a physical law could still fill every three-site seed. Correct: this
note does not adopt `f_mix0` and does not claim that every F_cut map misses
those thirty-two seeds. It reports the coverage of this one displayed map.

### N8 — cross-cycle echo

#6453 named `cov3(f_L1) = 220`. #6437 named one 3-site splitter. #6456
named `cov3(f0)` for a different map. This note agrees with those surfaces
and adds only `cov3(f_mix0)`.

## Boundaries and explicit non-claims

- The theorem is conditional on the declared two-cube and off-patch occupancy
  `0`.
- `f_mix0` and `f_L1` are displayed maps in `F_cut`. Neither is adopted.
- Thirty-two unfilled three-site seeds are a patch count, not a physical rate.
- No axiom, primitive, registry, or audit verdict is edited.
- Do not write `f_mix0` into Admissibility.

## Verification

Run:

```bash
python3 scripts/f_mix0_three_site_coverage_2026_08_15.py
```

The runner enumerates the two-cube seeds, evolves occupancy-to-lock under
the two displayed maps, and checks the N1–N8 packet. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
