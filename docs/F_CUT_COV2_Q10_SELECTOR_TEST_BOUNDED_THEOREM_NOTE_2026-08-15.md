---
claim_id: f_cut_cov2_q10_selector_test_bounded_theorem_note_2026-08-15
claim_type: bounded_theorem
claim_scope: "Among the 32 F_cut maps on the two-cube with off-patch o=0, whether cov2>0 equals adj2∨vertex3∨mixed3 is reported. Displayed, not adopted."
upstream_dependencies:
  - minimal_axioms
runner: scripts/f_cut_cov2_q10_selector_test_2026_08_15.py
---

# Whether Positive 2-Site Coverage Equals Q10 Among the 32 F_cut Maps

**Date:** 2026-08-15
**Type:** bounded_theorem
**Scope:** exact occupancy-to-lock fill positivity on the twelve-vertex two-cube
with off-patch occupancy `0`, scored on the 66 two-site seeds, for the
thirty-two cube-covariant cut maps `F_cut`, against the displayed remaining-bit
predicate `Q10`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/f_cut_cov2_q10_selector_test_2026_08_15.py`](../scripts/f_cut_cov2_q10_selector_test_2026_08_15.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only.

## Result up front

Investment c10bit3 named `Q10 := (adj2=1) or (vertex3=1) or (mixed3=1)` as
the displayed 3-bit OR equal to `cov10>0`. Investment #6494 closed
`P = cov2>0`, with `P := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`. This
note tests whether `cov2>0` equals that newly named `Q10` on the same
two-site seeds. Duality is not assumed: the test does not import
`Max(k)=Max(12-k)` and does not transfer the `k=10` identity to `k=2`.

`F_cut` is the cube-covariant class of `{0,1}`-valued maps on the six
nearest-neighbor occupancy bits with `f(empty)=f(full)=0` and `f(c)=f(1-c)`.
It has five free remaining bits and size 32. Remaining bits are ordered as
`(wt1, opp2, adj2, vertex3, mixed3)`. Thus `|F_cut| = 32`.

`f_L1(c)=1` if and only if some axis is unbalanced: the signed pair
`n_μ = c_{+μ} − c_{-μ}` is nonzero. This is **not** Hamming parity
`|c|_1 mod 2`. `f_L1` is the 10-orbit reading `n ≠ 0`, not Hamming. Its
remaining-bit tuple is `(1, 0, 1, 1, 1)`.

On the two-cube with off-patch occupancy `0`, write
`cov2(f) = |{S : |S|=2 and f fills from S}|`. The boolean scored here is
`cov2(f)>0`. Then:

- Theorem 1. cov2>0 is not equivalent to `Q10` among the 32 maps. The
  lex-first remaining-bit miss is `(0, 0, 0, 0, 1)`, which has `Q10 = 1`
  and `cov2 = 0`.
- Theorem 2. `N_pos = 14`, `N_Q10 = 28`, `N_both = 14`.
- Theorem 3. `Q10` is displayed. Displayed, not adopted. Do not adopt
  `Q10`.

Do not write `Q10` into Admissibility. The extra that would have made the
`cov10>0` 3-bit OR the two-site positivity selector is not present.

## Machine status and trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The 32 F_cut maps are enumerated by remaining bits and scored exactly on the 66 two-site seeds of the two-cube. Whether cov2>0 equals Q10, and the counts N_pos, N_Q10, N_both, are finite exact facts. No physical Admissibility selector is claimed."
trace_class: frontier_discovery
target_claim_id: f_cut_cov2_q10_selector_test
target_blocker_text: "whether cov2>0 equals adj2 or vertex3 or mixed3 among the 32 F_cut maps"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded Q10 test against cov2>0; do not adopt Q10"
conditional_surface_status: "exact for occupancy-to-lock on the twelve-vertex two-cube with off-patch occupancy 0; no Z^3-wide formation law"
hypothetical_axiom_status: "not proposed; no axiom or approved primitive is added"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Premises and declared mathematical objects

The only scientific dependency is the current four-axiom authority linked
above. Lattice supplies `Z^3` with nearest-neighbor adjacency and proper cubic
rotations. Admissibility supplies one fixed nearest-neighbor rule, covariant
under those motions. Record is not used as a formation-site selector: the
dynamics here are a declared occupancy-to-lock predicate on a finite patch.
Reading notes on Admissibility state that the local law
it does not supply the formation site, probability, or rate.
Records form.
When present, a record locks exactly one admissible local possibility.
A readout value is determined by record content alone.
A site with no record cannot be read.

The following are declared mathematical scaffolding, not measured or fitted
physics inputs:

- the two-cube `T = {0,1,2} × {0,1} × {0,1}` (twelve vertices of two unit
  cubes sharing the face `x=1`);
- off-patch occupancy `0` (a neighbor of a site in `T` that is not itself in
  `T` is treated as unoccupied; a blank-block is a different rule);
- the six-direction stencil `{±e_x, ±e_y, ±e_z}` at every site;
- the 24 proper cube rotations;
- the ten axis-type orbits of `{0,1}^6` under those rotations;
- the class `F_cut` of cube-covariant maps with `f(empty)=f(full)=0` and
  complement symmetry `f(c)=f(1-c)`;
- the displayed predicate `Q10 := (adj2=1) or (vertex3=1) or (mixed3=1)`.

No observational comparator, literature constant, rate, or generator is
imported. Hamming parity is a contrast map only; it is not `f_L1`.

## Exact target and objects

**Target.** Decide whether `cov2(f)>0` equals `Q10(f)` among the 32 members
of `F_cut` on `T`. If not, name one lex-first remaining-bit miss. Report
`N_pos`, `N_Q10`, and `N_both`. Display `Q10`. Do not adopt `Q10`.

A configuration `c ∈ {0,1}^6` is a six-tuple of neighbor occupancies in
direction order `(+x,-x,+y,-y,+z,-z)`. Axis type is
`(n_unbalanced, n_both, n_empty)`, where an axis is unbalanced if its two
bits differ, both if both bits are 1, and empty if both bits are 0. Complement
swaps `n_both` with `n_empty`. The five remaining bits of `F_cut`, in the
order `(wt1, opp2, adj2, vertex3, mixed3)`, are the values on orbit types
`(1,0,2)`, `(0,1,2)`, `(2,0,1)`, `(3,0,0)`, `(1,1,1)`. Complement partners
are forced equal; empty and full are fixed at 0.

Occupancy-to-lock: from a locked set `L ⊂ T`, a site `x ∈ T \ L` locks at
the next tick if and only if `f` of its six-neighbor occupancy (off-patch
entries 0) equals 1. The map `f` fills from a seed `S` if iterating this
rule from `L_0 = S` reaches `L = T` in at most 13 ticks.

The two-site seeds are the 66 unordered pairs of vertices of `T`. Then
`cov2(f)` is the number of those pairs from which `f` fills. Write
`Q10(f) = 1` when at least one of `adj2`, `vertex3`, `mixed3` is 1.

## Theorems

### Theorem 1 — `cov2>0` is not `Q10`; lex-first miss

There are exactly 24 proper cube rotations and exactly 10 orbits on
`{0,1}^6`. The three cuts leave `|F_cut| = 32`. The unbalanced-axis map
`f_L1` is one element of `F_cut` and is not Hamming parity.

Among the 32 maps, cov2>0 is not equivalent to `Q10`. The lex-first
remaining-bit miss, in the order `(wt1, opp2, adj2, vertex3, mixed3)`, is
`(0, 0, 0, 0, 1)`: that map has `Q10 = 1` and `cov2 = 0`.

### Theorem 2 — counts

Write `N_pos` for the number of maps with `cov2>0`, `N_Q10` for the number
with `Q10=1`, and `N_both` for the number with both. Exhaustive scoring
gives

```text
N_pos = 14
N_Q10 = 28
N_both = 14
```

So every positive map is `Q10`-true, and fourteen `Q10`-true maps still have
`cov2 = 0`. The four maps with `adj2=vertex3=mixed3=0` are among the zeros
and are not misses.

### Theorem 3 — display; do not adopt `Q10`

`Q10` is displayed as the 3-bit OR `adj2∨vertex3∨mixed3`. Displayed, not
adopted. Do not adopt `Q10`. Do not write a remaining-bit formula into Admissibility.

## Exact target and obligation graph

| Obligation | Status |
|---|---|
| current Lattice / Admissibility / Record wording | quoted; no edit |
| `F_cut` as the 32 cube-covariant cut maps | enumerated by remaining bits |
| `f_L1` as unbalanced-axis / `n ≠ 0` | defined; Hamming rejected |
| two-cube, 66 two-site seeds, off-patch `o=0` | declared finite patch |
| displayed `Q10` | displayed, not adopted |
| `cov2>0` equals `Q10` | fails; lex-first miss `(0, 0, 0, 0, 1)` |
| `N_pos = 14`, `N_Q10 = 28`, `N_both = 14` | proved by exhaustive scoring |
| leftover-character of c10bit3 | refused; that was `Q10=cov10>0` |
| leftover-character of #6494 | refused; that was `P=cov2>0` |
| Max duality | refused; duality is not assumed |
| adoption of `Q10` | refused |
| physical Admissibility selector | open |

## Boundary and imports

Not leftover-character of c10bit3: that was `Q10=cov10>0` on the 66
ten-site seeds. The present object is the same displayed 3-bit OR scored
against two-site positivity, not a restatement that `Q10` equals
`cov10>0`.

Not leftover-character of #6494: that was `P=cov2>0`, with
`P := (wt1=1) and (adj2,vertex3,mixed3)≠(0,0,0)`. The present test asks
whether the weaker `Q10` also equals `cov2>0`. Duality is not assumed.

The note is not a Max(2) ranking and not a seed-table: maximizers of
`cov2` are not selected, and no seed census of a named map is compiled.

Off-patch occupancy `0` is an explicit default on this patch. A blank-block
is a different rule and is not used.

No observation, fit, continuum limit, or Hamming-as-`f_L1`
identification is imported. No `Z^3`-wide formation law is claimed.
Do not adopt `Q10`.

## Promotion value gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It answers whether `cov2>0` equals `Q10` inside `F_cut` on this patch. |
| V2 | Current main has the axiom memo, the c10bit3 naming of `Q10=cov10>0`, and the #6494 fact that `P=cov2>0`, but no landed test of `Q10` against `cov2>0`. |
| V3 | The 32 maps, 66 seeds, and occupancy-to-lock evolution are independently finite and exact. |
| V4 | The theorem is more than restating Admissibility: it scores a declared finite class against a displayed 3-bit OR. |
| V5 | Equality fails, and `Q10` is not adopted or written into Admissibility. |

## No-Go Discipline gate

The negative content is narrow: `cov2>0` is not `Q10` among the 32 `F_cut`
maps on this patch. No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| Hamming parity | identify `f_L1` with `|c|_1 mod 2` | **ATTEMPTED** |
| leftover of c10bit3 | treat the test as leftover-character of `Q10=cov10>0` | **ATTEMPTED** |
| leftover of #6494 | treat the test as leftover-character of `P=cov2>0` | **ATTEMPTED** |
| Max duality | replace the `k=2` score by `Max(k)=Max(12-k)` | **ATTEMPTED** |
| adopt `Q10` | write `adj2∨vertex3∨mixed3` into Admissibility | **ATTEMPTED** |
| blank-block off-patch | replace occupancy `0` by a blank-block | **ATTEMPTED** |

### N2 — wall independence

The failed equality, the Hamming contrast, the c10bit3 `Q10` identity, the
#6494 `P` identity, and the off-patch convention are distinct. This note
claims no complete wall collection.

### N3 — hidden-condition scan

The two-cube, the 66 two-site seeds, off-patch occupancy `0`,
occupancy-to-lock ticks, the `F_cut` remaining-bit order, and displayed
`Q10` are declared. Equality of `cov2>0` with `Q10` is not silently
assumed. Duality is not assumed.

### N4 — source residual matching

The live axiom memo supplies `Z^3`, proper cubic rotations, and one covariant
nearest-neighbor rule. The residual answered here is whether `cov2>0` equals
`Q10` on the declared patch, not leftover-character of c10bit3, not
leftover-character of #6494, and not a Max-duality ranking.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | 64 neighbor 6-tuples by axis-type orbit | no continuum occupancy |
| per site | twelve two-cube vertices, same stencil | no privileged site |
| per mode | all 32 `F_cut` maps scored on 66 seeds | no physical law selection |
| per block | `N_pos`, `N_Q10`, `N_both` on this patch | no Admissibility write-in |
| lattice wide | checked and not executed | no `Z^3`-wide formation law |

### N6 — live partial-closure paths

Live routes include a different seed family, a different off-patch rule, a
selector other than `Q10`, and any independently derived physical map from
`F_cut` into Admissibility.

### N7 — hostile steelman

**Steelman:** after `Q10=cov10>0`, the same 3-bit OR must be the two-site
positivity selector, or else duality from `k=10` to `k=2` would force it.

**Answer:** Duality is not assumed. `N_pos = 14` while `N_Q10 = 28`. The
lex-first miss `(0, 0, 0, 0, 1)` has `Q10 = 1` and `cov2 = 0`. `Q10` is
displayed, not adopted.

### N8 — cross-cycle echo

Investment c10bit3 already showed that `Q10` equals `cov10>0`. Investment
#6494 already showed that `cov2>0` is `P`. Echoing either identity is not
a substitute for testing `Q10` against `cov2>0`: the lex-first miss and
the triple `(N_pos, N_Q10, N_both)` are the new comparison facts. Duality
is not assumed.

No-Go Discipline disposition: **PASS** for the finite test and the
narrow equality failure. FAIL / DO NOT SHIP for “`cov2>0` equals `Q10`”
or “`Q10` is the physical rule.”

## Live parent quotes

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor adjacency, standard translations, and proper cubic rotations about each site.

There is one fixed nearest-neighbor admissibility rule, covariant under lattice translations and proper cubic rotations.

A site with no record cannot be read.

## Runner contract

The companion runner enumerates the 32 `F_cut` maps, scores `cov2` on the
66 two-site seeds, tests whether `cov2>0` equals `Q10`, reports the
lex-first miss `(0, 0, 0, 0, 1)`, and reports `N_pos`, `N_Q10`, and
`N_both`. Declared audit inputs are this note and the axiom memo; the
runner writes no cache and authors no audit verdict.
