---
claim_id: cubic_nn_condition_domain_separation_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "On the six-neighbor graph of Z^3, the declared spacing-3 sites have pairwise-disjoint open neighborhoods whose union excludes the origin; any explicitly supplied product kernel with exactly those condition domains is invariant under changing only the origin coordinate, without implying stochastic independence, a binary register law, or physical Record formation."
upstream_dependencies:
  - minimal_axioms
  - admissibility_global_measure_menu_kernel_type_separation_bounded_theorem_note_2026-08-10
  - finite_dyadic_product_registration_truncated_barycenter_bounded_theorem_note_2026-08-13
runner: scripts/cubic_nn_condition_domain_separation_2026_08_13.py
---

# Cubic NN Condition-Domain Separation And Direct-Coordinate Invariance

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact six-neighbor geometry, a supplied conditional product kernel,
and invariance under changing only a coordinate outside its declared condition
domain. Statistical independence, a binary register law, and physical Record
formation remain open.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/cubic_nn_condition_domain_separation_2026_08_13.py`](../scripts/cubic_nn_condition_domain_separation_2026_08_13.py)

**Runner cache:**
[`logs/runner-cache/cubic_nn_condition_domain_separation_2026_08_13.txt`](../logs/runner-cache/cubic_nn_condition_domain_separation_2026_08_13.txt)

## Result Up Front

The finite-dyadic theorem
[`FINITE_DYADIC_PRODUCT_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md`](FINITE_DYADIC_PRODUCT_REGISTRATION_TRUNCATED_BARYCENTER_BOUNDED_THEOREM_NOTE_2026-08-13.md)
uses an explicitly supplied finite register and uniform counting law. This
note proves only a geometric fact relevant to a possible later construction:
some cubic-lattice sites can have local condition domains that omit a chosen
system coordinate and do not overlap one another.

Let `N(x)` be the open six-neighbor set in `Z^3`. For
`x_1=3e_1`, `x_2=6e_1`, and `x_3=9e_1`, the three sets `N(x_k)` are
pairwise disjoint, their union has 18 sites, and that union excludes the
origin. Consequently, if one separately supplies local kernels whose exact
arguments are the configurations on those sets and separately supplies their
product, then that product kernel is unchanged when only the origin
coordinate is changed while all 18 condition coordinates are held fixed.

That conclusion is **direct-coordinate invariance**, not stochastic
independence. A joint law on the 18 condition coordinates can correlate
disjoint supports. Averaging the conditional product over such a law can
produce perfectly correlated auxiliary outcomes. The geometry also supplies
no binary alphabet, fair margin, product-environment law, formation site,
record content map, or physical readout.

Four exact statements survive review.

1. `0∈N(e_1)`, while `0∉N(2e_1)` and `0∉N(3e_1)`. Thus the adjacent
   condition tuple exposes the origin coordinate; the two more distant tuples
   do not.
2. The declared spacing-3 family has pairwise-disjoint open neighborhoods,
   and each is disjoint from `N(0)`. Spacing 2 along the same axis fails:
   `N(0)∩N(2e_1)={e_1}`.
3. A supplied product of kernels on the spacing-3 condition domains is a
   function only of their 18-site union, so it is invariant under a change at
   the origin alone.
4. Disjoint condition domains do not force marginal independence, uniform
   binary margins, or formation. An explicit correlated-environment model
   below gives fair but perfectly correlated outputs on disjoint supports.

## Current Premise Boundary

The Lattice and Admissibility premises are quoted from
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md):

Physical sites are the points of the cubic lattice `Z^3`, with nearest-neighbor
adjacency, standard translations, and proper cubic rotations about each site.

For each site, the probability distribution over the possibilities is determined by, and varies with, the nearest-neighbor conditions.

The only use of Admissibility is to identify the local condition domain. The
axiom does not specify the kernel values or a joint law of conditions at
several sites.

The current Record boundary is:

When present, a record locks exactly one admissible local possibility.

A readout value is determined by record content alone.

A site with no record cannot be read.

Record supplies no scalar collection functional, no finite additivity, and no
value at absence. None of Record is needed for the geometry or kernel theorem.
Using the conditional outcomes as physical bits would require a binary local
alphabet, formation at the named sites, and a content/readout identification;
all remain open.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The six-neighbor listings, spacing-3 disjointness, 18-site union, direct-coordinate invariance of a supplied product kernel, and correlated-environment counterexample are finite exact statements; no independent register or Record compiler is derived."
trace_class: upstream_support
target_claim_id: admissibility_distribution_to_effect_grade_bridge
target_blocker_text: "derive an auxiliary atom-splitting law and physical event registration from the actual Admissibility and Record premises"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: theorem
next_trace_action: "Derive, rather than assume, the auxiliary kernel, its joint environment law, a binary or finite alphabet with the required margin, formation at the selected sites, and the Record content map."
conditional_surface_status: "exact for the declared cubic condition domains and an explicitly supplied product kernel; stochastic independence and physical registration remain open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Exact Objects

Write `0=(0,0,0)`, `e_1=(1,0,0)`, `e_2=(0,1,0)`, and
`e_3=(0,0,1)`. The open nearest-neighbor set is

`N(x)={x±e_1,x±e_2,x±e_3}`.

The graph distance is the taxicab metric. The executed family is

`S={3e_1,6e_1,9e_1}`.

For a configuration `η` on `Z^3`, let `η|_{N(x)}` be its restriction to the
six named coordinates. A local conditional kernel is an externally supplied
map

`K_x(a_x | η|_{N(x)})`.

For the finite theorem, also explicitly supply the conditional product

`K_S(a_1,a_2,a_3 | η)=∏_{k=1}^3 K_{x_k}(a_k | η|_{N(x_k)})`.

Neither the local kernel values nor this product factorization follows from
the lattice geometry. The product is a hypothesis whose domain can be
inspected exactly.

## Theorem 1 — Coordinate Visibility

`0∈N(e_1)` because `e_1-e_1=0`. Direct listing gives

`N(e_1)={0,2e_1,e_1±e_2,e_1±e_3}`.

By contrast,

`N(2e_1)={e_1,3e_1,2e_1±e_2,2e_1±e_3}`

and

`N(3e_1)={2e_1,4e_1,3e_1±e_2,3e_1±e_3}`,

so neither contains `0`. Hence a kernel declared on the first tuple may
directly use the origin coordinate, whereas kernels declared exactly on the
latter tuples do not receive it as an argument.

This is a statement about explicit function arguments. It does not exclude
indirect dependence through a global joint distribution, propagation, common
causes, or dynamics.

## Theorem 2 — Declared Disjoint Supports

The six-point sets `N(3e_1)`, `N(6e_1)`, and `N(9e_1)` are pairwise
disjoint and disjoint from `N(0)`. Their union therefore contains 18 distinct
sites and excludes `0`.

Spacing 3 is sufficient but not minimal for disjoint *open* neighborhoods.
The cubic graph is bipartite, so adjacent sites also have disjoint open
neighborhoods. More exactly, for distinct sites `x,y`, a common open neighbor
requires a length-two path `x→z→y`; it occurs precisely for the appropriate
distance-two displacements. Thus the earlier statement “disjoint iff distance
at least 3” is not used and is false for adjacent sites.

Along the chosen axis, spacing 2 gives the explicit contrast

`N(0)∩N(2e_1)={e_1}`.

The theorem needs only the finite listings for the declared family.

## Theorem 3 — Direct-Coordinate Invariance

Let `η` and `η'` be two global configurations that agree off the origin.
Since `0` is absent from `U=⋃_{x∈S}N(x)`, their restrictions to `U` agree.
Every local kernel receives the same six-tuple under `η` and `η'`, so the
explicitly supplied product satisfies

`K_S(·|η)=K_S(·|η')`.

The primary runner checks this with nonconstant kernels: changing a condition
coordinate in `U` changes at least one factor, while changing only the origin
does not. This prevents the earlier vacuous test in which every local law
ignored its condition tuple.

Pairwise disjointness is not required for origin exclusion; it only makes the
18 coordinates nonoverlapping. Product factorization remains separately
supplied.

## Theorem 4 — Marginal Independence Does Not Follow

Choose one coordinate `u_k∈N(x_k)` for each of two disjoint supports. Let a
fair latent bit `L` set both distinct condition coordinates equal:
`η(u_1)=η(u_2)=L`. Let each local conditional kernel output its selected
condition bit deterministically. Conditional on `η`, the two-output kernel is
a product. After averaging over `L`,

`P(A_1=0,A_2=0)=P(A_1=1,A_2=1)=1/2`,

while both one-output margins are fair. Their product would assign `1/4` to
each diagonal pair, so the outputs are not marginally independent.

Therefore disjoint condition *coordinates* do not imply an independent joint
law on those coordinates. This counterexample leaves live a separately
derived product-environment or mixing theorem.

Likewise, fixed biased kernels show that geometry alone does not force a fair
binary margin. The Admissibility reading note says the distribution concerns
which possibility a forming record locks, conditional on formation; it does
not supply the formation site, probability, or rate.

## Exact Target And Obligation Graph

| Obligation | Status |
|---|---|
| current six-neighbor Lattice and Admissibility premises | quoted; no edit |
| current Record boundary | quoted as non-used boundary; scalar clauses absent |
| declared neighbor listings | exact finite enumeration |
| spacing-3 pairwise disjointness and 18-site union | proved by listing |
| direct-coordinate invariance | proved for supplied exact-domain kernels |
| nonconstant dependence check | executed by the primary runner |
| stochastic-independence implication | refuted by correlated environment |
| local kernels and product factorization | explicitly supplied |
| binary alphabet, fair law, formation, content map | open |
| physical registered-event compiler | open |

## Boundary And Imports

The August 10 type-separation note
[`ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md`](ADMISSIBILITY_GLOBAL_MEASURE_MENU_KERNEL_TYPE_SEPARATION_BOUNDED_THEOREM_NOTE_2026-08-10.md)
leaves open a physical construction that produces registered measurable event
partitions. The finite-dyadic parent
supplies the exact mathematical role of a finite uniform register. The present
theorem supplies neither missing physical object. Its only exact advance is a
finite condition-domain lemma and a warning against conflating direct
coordinate omission with stochastic independence.

No observation, fitted margin, continuum limit, quantum tensor factor,
dynamics, or Record readout is imported.

## Promotion Value Gate (V1–V5)

| # | Answer |
|---|---|
| V1 | It addresses the placement subproblem inside the open auxiliary-register route, while explicitly leaving kernel, law, formation, and content mapping open. |
| V2 | Current main contains the finite-dyadic register theorem but no landed proof of the declared cubic condition-domain family or its direct-versus-statistical independence boundary. |
| V3 | All geometry and the correlated-environment counterexample are independently finite and exact. |
| V4 | The theorem is more than a restatement of Admissibility because it enumerates the exact condition coordinates and exposes a semantic non-implication. |
| V5 | It is not a physical compiler: the supplied product kernel and missing joint environment law prevent that relabeling. |

## No-Go Discipline Gate

The negative content is narrow: geometry alone does not guarantee adjacent
origin omission, stochastic independence, a fair binary margin, or formation.
No global compiler impossibility is claimed.

### N1 — materially distinct routes

| Route | Attack | Result |
|---|---|---|
| adjacent constant kernel | ignore the visible origin coordinate | live special case; shows adjacency permits invariance but does not guarantee it |
| distance-2 or spacing-3 placement | omit the origin coordinate geometrically | succeeds for direct-coordinate invariance |
| independent environment law | separately assume independent condition coordinates | succeeds for marginal independence; extra law not derived here |
| correlated environment law | correlate distinct support coordinates through one latent bit | executed counterexample; disjoint supports alone are insufficient |
| biased local kernels | choose non-half margins | executed; geometry does not select fairness |
| formation dynamics | separately derive records at the named sites | live route outside this theorem |
| continuum or nonlattice register | use the finite-dyadic parent object directly | live different-object route |
| Moore neighborhood | replace the six-neighbor graph | different premise; diagonal distance-two visibility changes |

### N2 — wall independence

The missing joint environment law, local kernel values, formation mechanism,
alphabet, margin selector, and content map are distinct premises. This note
claims no complete wall collection and no compiler no-go.

### N3 — hidden-condition scan

The exact six-neighbor graph, spacing-3 family, local kernel domains, and
product factorization are declared. Product factorization is a hypothesis,
not a lattice consequence. Independence of the environment, binary outcomes,
uniformity, formation, and readout are not silently assumed.

### N4 — source residual matching

The current axiom memo supplies only the six-neighbor substrate and local-law
condition sentence used here. The August 10 note and finite-dyadic parent leave
the physical registered-event construction open. The residual therefore
matches current sources rather than the retired scalar Record formulation.

### N5 — resolution and rhetoric audit

| Resolution | Executed | Not claimed |
|---|---|---|
| per element | named lattice sites and explicit condition coordinates | no exhaustive alphabet classification |
| per site | local exact-domain kernels | no derived kernel values |
| per mode | no mode calculation | no spectral exhaustion |
| per block | three-site conditional product and two-site correlated counterexample | no physical register compiler |
| lattice wide | checked and not executed | no global independence or formation theorem |

### N6 — live partial-closure paths

Live routes are an independently derived environment product/mixing law, a
fair finite-alphabet selector, a formation mechanism at the selected sites,
and a Record content map. A continuum or other auxiliary object also remains
live.

### N7 — hostile steelman

**Steelman:** Pairwise-disjoint condition supports should make the auxiliary
outputs independent.

**Answer:** Disjoint coordinate labels do not factorize their joint law. The
explicit latent-bit model makes two distinct coordinates equal and yields
perfectly correlated outputs from conditionally factorized kernels. An
independent environment law would close that gap, but it is additional input.

### N8 — cross-cycle echo

The finite-dyadic parent assumes a uniform finite register. This note does not
retroactively derive that assumption; it isolates one placement condition and
shows why geometry alone is weaker than independence. The August 10 interface
therefore remains open.

**Gate disposition:** PASS for the finite geometry, direct-coordinate
invariance, and narrow non-implications above. FAIL / DO NOT SHIP for
“independent bits are derived,” “records form here,” or “the auxiliary register
compiler is closed.”

## Primary Runner

The primary runner recomputes the neighbor sets, intersection pattern,
18-site union, nonconstant-kernel origin invariance, correlated-environment
counterexample, biased-margin witness, current premise boundary, and mutation
controls. It authors no audit verdict.
