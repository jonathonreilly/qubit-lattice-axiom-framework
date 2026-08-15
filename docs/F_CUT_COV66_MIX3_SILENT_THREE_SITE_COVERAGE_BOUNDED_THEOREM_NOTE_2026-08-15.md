---
claim_id: f_cut_cov66_mix3_silent_three_site_coverage_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "On the two-cube with off-patch o=0, the F_cut map (1,1,1,1,0) fills 212 of the 220 three-site seeds. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov66_mix3_silent_three_site_coverage_2026_08_15.py
---

# Three-Site Coverage Of The Mixed3-Silent Cov2=66 Map

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** occupancy-to-lock coverage of the displayed F_cut map
`(1, 1, 1, 1, 0)` on the twelve-vertex two-cube with off-patch occupancy `0`.
**Audit-status authority:** independent audit lane only. This note writes no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov66_mix3_silent_three_site_coverage_2026_08_15.py`](../scripts/f_cut_cov66_mix3_silent_three_site_coverage_2026_08_15.py)

## Result up front

On the two-cube with off-patch occupancy `0`, the F_cut remaining-bit map

```text
f0 = (wt1, opp2, adj2, vertex3, mixed3) = (1, 1, 1, 1, 0)
```

fills every one of the `C(12,2) = 66` two-site seeds and fills
`212` of the `C(12,3) = 220` three-site seeds. The last remaining bit is
silent mixed3.

The 3-site maximizers named by #6453 are a different pair:

```text
L1 = (1, 0, 1, 1, 1),   cov3(L1) = 220
f1 = (1, 1, 1, 1, 1),   cov3(f1) = 220
```

f0 is not in that pair. The new number is `cov3(f0) = 212`. Not leftover-character of #6453; that named the two 3-site maximizers. Displayed, not adopted.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed occupancy
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "cov2(f0)=66 is reconfirmed and cov3(f0)=212 is computed exactly on the declared two-cube. The map is displayed, not adopted as a physical formation law."
trace_class: negative_route_pruning
target_claim_id: f_cut_cov66_mix3_silent_three_site_coverage
target_blocker_text: "report three-site coverage of the mixed3-silent cov2=66 F_cut map"
source_of_blocker_text: handoff
reachability_to_target: prunes
artifact_role: theorem
next_trace_action: "keep f0 displayed-only; do not promote mixed3 silence into Admissibility"
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
does not supply the formation site, probability, or rate.

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

**Theorem 1.** Reconfirm `cov2(f0) = 66` and
`cov3(L1) = cov3(f1) = 220`.

**Theorem 2.** Report `cov3(f0)`. The computed value is `cov3(f0) = 212`.
Eight three-site seeds stall at ten locked sites. Those eight seeds form one
geometric orbit: the two long-axis endpoints of a length-two edge together
with a middle-square face-diagonal third site. The same eight seeds fill
under both `L1` and `f1`.

**Theorem 3.** Display f0. Do not adopt f0. Do not write f0 into Admissibility.

## Claim scope

On the two-cube with off-patch o=0, the F_cut map (1,1,1,1,0) fills 212 of the 220 three-site seeds.
Displayed, not adopted.

## No-Go Discipline

The negative result is only that the mixed3-silent cov2-maximizer is not a
3-site maximizer. It is not a universal no-go against other F_cut maps or
against a later derived formation law.

No-Go Discipline disposition: **PASS**

### N1 — materially distinct route scan

| route | marker | outcome relative to the narrow target |
|---|---|---|
| replace `f_L1` by Hamming parity | **ATTEMPTED** | Hamming disagrees with unbalanced-axis `n_μ ≠ 0` on the six-ray cells |
| treat `cov3(f0)` as leftover-character of #6453 | **ATTEMPTED** | #6453 named the pair `L1` and `f1`; f0 is outside that pair |
| adopt f0 because `cov2(f0)=66` | **ATTEMPTED** | two-site maximality does not imply three-site maximality |
| read silent mixed3 as a physical selector | **ATTEMPTED** | mixed3 silence is a remaining-bit choice, not an Admissibility derivation |
| replace off-patch occupancy `0` by a blank-block | **ATTEMPTED** | a blank-block is a different rule |
| import a Hamiltonian, process, or rate as a fill certificate | **ATTEMPTED** | fill is an occupancy-to-lock count on the declared patch |

### N2 — wall independence

One type wall is claimed: f0 does not fill every three-site seed. The 2-site
maximizer pair and the 3-site maximizer pair remain separate enumerations. No
inflated wall count is used.

### N3 — hidden-wall scan

The two-cube, off-patch occupancy `0`, remaining-bit labels, and seed families
are all declared. No full-lattice formation law, blank-block, Hamming
substitute, or adopted selector is imported.

### N4 — residual matching

The residual after #6453 was the three-site coverage of the other cov2=66
map. This note reports that new number. It neither closes a physical
formation law nor enlarges the axiom set.

### N5 — certificate granularity

```text
per-element: executed — each of the 64 neighbor 6-tuples is assigned its axis-type orbit
per-site: executed — each of the twelve two-cube vertices uses the same six-direction stencil
per-mode: executed — f0, f_L1, and f1 are scored on the 66 two-site and 220 three-site seeds
per-block: executed — cov3(f0) is the mixed3-silent three-site coverage on this patch
lattice-wide: not executed — no Z^3-wide formation law or physical Admissibility selector is claimed
```

### N6 — partial-closure paths

A later derived formation kernel, a larger patch, or a different off-patch
rule could change coverage counts. Those routes remain live and need not
alter the axioms.

### N7 — steelman

The strongest objection is that mixed3 silence is only a display choice and
that a physical law could still fill every three-site seed. Correct: this
note does not adopt f0 and does not claim that every F_cut map misses those
eight seeds. It reports the coverage of this one displayed map.

### N8 — cross-cycle echo

#6453 named the two 3-site maximizers `L1` and `f1`. This note agrees with
that pair and adds only `cov3(f0)`.

## Boundaries and explicit non-claims

- The theorem is conditional on the declared two-cube and off-patch occupancy
  `0`.
- f0, f1, and `f_L1` are displayed maps in `F_cut`. None is adopted.
- Eight unfilled three-site seeds are a patch count, not a physical rate.
- No axiom, primitive, registry, or audit verdict is edited.
- Do not write f0 into Admissibility.

## Verification

Run:

```bash
python3 scripts/f_cut_cov66_mix3_silent_three_site_coverage_2026_08_15.py
```

The runner enumerates the two-cube seeds, evolves occupancy-to-lock under
the three displayed maps, and checks the N1–N8 packet. Expected summary:

```text
TOTAL: PASS>=12 FAIL=0
```
