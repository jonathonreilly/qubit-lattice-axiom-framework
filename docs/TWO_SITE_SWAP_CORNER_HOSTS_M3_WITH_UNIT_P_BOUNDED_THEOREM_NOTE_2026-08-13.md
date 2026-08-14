---
claim_id: two_site_swap_corner_hosts_m3_with_unit_p_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "Conditional on the explicitly chosen standard two-site algebraic tensor construction T_2=M_2(C)⊗M_2(C)≅M_4(C), the displayed swap F is Hermitian of square I_4 and trace 2. The projector p=(I_4+F)/2 has rank 3 and is not I_4. The corner C=p M_4 p is a unital *-algebra with unit p, complex dimension 9, and is *-isomorphic to M_3(C) via the matrix units of an orthonormal basis of im(p), with ψ(I_3)=p. The displayed inclusion C↪M_4 is not unital. No physical SU(3), QCD, Qubit-rewrite, or color-selection identification is supplied or claimed."
upstream_dependencies:
  - minimal_axioms
runner: scripts/two_site_swap_corner_hosts_m3_with_unit_p_2026_08_13.py
---

# Two-Site SWAP Corner Hosts `M_3` With Unit `p`

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact conditional algebra on the explicitly supplied standard
two-factor tensor `T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)` and the rank-3 corner of
the displayed swap projector.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/two_site_swap_corner_hosts_m3_with_unit_p_2026_08_13.py`](../scripts/two_site_swap_corner_hosts_m3_with_unit_p_2026_08_13.py)

Framework context on `origin/main`: the axiom memo
[`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) only. It
supplies the one-site `M_2(C)` possibility algebra, not a composite rule.

## Result Up Front

The Qubit axiom supplies one site with possibility algebra `M_2(C)`. This
bounded note then explicitly chooses the standard algebraic tensor product
`T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)` for two displayed factors. The axioms do not
select that composite rule. In the product basis `|00>`, `|01>`, `|10>`,
`|11>` the swap operator `F` is the displayed permutation matrix below. Its
`+1` spectral projection `p = (I_4 + F)/2` is an orthogonal rank-3 projector,
not `I_4`. The corner

`C = p T_2 p = p M_4(C) p`

is a unital `*`-algebra with unit `p`, not `I_4`. It is `*`-isomorphic to
`M_3(C)` by the matrix units of an orthonormal basis of `im(p)`, and
`ψ(I_3) = p`.

This is a corner host. Its displayed inclusion in `T_2` is not unital because
the two units are `p` and `I_4`. The note supplies no physical `SU(3)` action,
QCD identification, Qubit rewrite, or color-selection map.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Conditional on the explicitly supplied standard two-factor tensor algebra and displayed swap, exact integer/Fraction identities prove the rank-3 corner, while an orthonormal basis exhibits a *-isomorphism onto M_3(C) with unit p. No physical internal-algebra identification is supplied."
trace_class: frontier_discovery
target_claim_id: null
target_blocker_text: "does the displayed two-factor swap projector define an M_3(C) corner with internal unit p rather than ambient unit I_4?"
source_of_blocker_text: frontier_question
reachability_to_target: unknown_frontier
artifact_role: theorem
next_trace_action: "test whether this exact corner lemma has a canonical downstream consumer; no physical consumer is claimed here"
conditional_surface_status: "exact conditional algebra for the explicitly chosen standard two-factor tensor construction and displayed swap; other composites, projectors, and physical identifications remain separate"
hypothetical_axiom_status: null
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Inputs And Support Boundary

- **Framework context:** Qubit supplies the full one-site possibility algebra
  `M_2(C)`.
- **Explicit bounded mathematical input:** this note chooses the standard
  algebraic tensor product of two displayed `M_2(C)` factors and identifies it
  with `M_4(C)`. That composite choice is not attributed to the four axioms and
  is not claimed to exhaust physical composites.
- **Explicit test object:** the displayed swap `F` is chosen for this theorem;
  no axiom or approved primitive selects it.
- **External physics inputs:** none. There is no measured, fitted, literature,
  normalization, scale, or observational constant.
- **Physical-identification boundary:** no map from this corner to a physical
  color degree of freedom, `SU(3)` gauge action, or QCD observable is supplied.

## Exact Objects

The current Qubit axiom names the full one-site possibility domain with
algebraic presentation `M_2(C)`. For the explicit bounded composite choice in
this note, write

`T_2 = M_2(C) ⊗ M_2(C) ≅ M_4(C)`

for the explicit two-factor algebra. Identify `T_2` with `4 × 4` matrices in the
product basis `|00>`, `|01>`, `|10>`, `|11>`. The two-site swap is the
permutation matrix

```
F = [[1, 0, 0, 0],
     [0, 0, 1, 0],
     [0, 1, 0, 0],
     [0, 0, 0, 1]]
```

Define `p = (I_4 + F)/2`. Explicitly

```
p = [[1,   0,   0, 0],
     [0, 1/2, 1/2, 0],
     [0, 1/2, 1/2, 0],
     [0,   0,   0, 1]]
```

The corner is `C = p M_4(C) p`. Write `{E_{ij}}_{1 ≤ i,j ≤ 3}` for the
standard matrix units of `M_3(C)`, and write `I_3` (resp. `I_4`) for the
unit of `M_3(C)` (resp. `M_4(C)`). An orthonormal basis of `im(p)` is

`|e_1> = |00>`, `|e_2> = (|01> + |10>)/√2`, `|e_3> = |11>`.

The displayed `*`-isomorphism is `ψ : M_3(C) → C`, `ψ(E_{ij}) = |e_i><e_j>`.

No axiom is edited. The tensor-composite choice and matrices `F` and `p` are
displayed mathematical inputs, not a proposed Qubit rewrite and not a
registered primitive.

## Exact Target And Obligation Graph

**Exact target.** Given the explicit standard algebraic tensor construction
`T_2 ≅ M_4(C)` and the displayed swap, decide whether its `+1` projector hosts
a copy of `M_3(C)` whose unit is `p`, and whether the displayed corner
inclusion preserves the ambient unit.

| Obligation | Role | Disposition |
|---|---|---|
| `F` Hermitian, `F^2 = I_4`, `Tr(F) = 2` | Theorem 1 | proved; runner checks |
| eigenvalues of `F` are `+1` (mult. 3) and `−1` (mult. 1) | Theorem 1 | proved as ranks of `p` and `I_4 − p` |
| `p` orthogonal projection, rank 3, `p ≠ I_4` | Theorem 2 | proved; runner checks the displayed matrix |
| `C = p M_4 p` unital `*`-algebra with unit `p`, `dim_C C = 9` | Theorem 3 | proved |
| `ψ : M_3(C) → C` a `*`-isomorphism with `ψ(I_3) = p` | Theorem 3 | exhibited on the ON basis of `im(p)` |
| displayed inclusion `C ↪ M_4` unital | Theorem 4 | fails; `p ≠ I_4` |
| physical `SU(3)`, QCD, Qubit-rewrite, or color-selection identification | out of scope | no such map is supplied or claimed |

## Theorem 1 — The two-site swap

`F` is Hermitian, `F^2 = I_4`, and `Tr(F) = 2`. The eigenvalues of `F` are
`+1` with multiplicity 3 (symmetric subspace) and `−1` with multiplicity 1
(antisymmetric subspace).

Proof. `F` is real symmetric, so `F* = F`. Direct multiplication of the
displayed matrix gives `F^2 = I_4`. The diagonal of `F` is `(1,0,0,1)`, so
the trace is `2`. The identity `F^2 = I_4` forces the minimal polynomial to
divide `x^2 − 1`, hence the only possible eigenvalues are `±1`. The `+1`
spectral projection is `p = (I_4 + F)/2` and the `−1` spectral projection is
`I_4 − p = (I_4 − F)/2`. Theorem 2 computes `rank(p) = 3` and
`rank(I_4 − p) = 1`, which are the geometric multiplicities.

## Theorem 2 — The swap projector

`p = (I_4 + F)/2` is an orthogonal projection: `p* = p = p^2`. It has
`rank(p) = 3` and `p ≠ I_4`. The displayed matrix in Exact Objects is this
`p`.

Proof. Hermiticity of `F` gives hermiticity of `p`. Then

`p^2 = (I_4 + 2F + F^2)/4 = (I_4 + 2F + I_4)/4 = (I_4 + F)/2 = p`.

The complementary projection `I_4 − p` is nonzero because `F ≠ I_4` (the
`(2,3)` entry of `F` is `1`). Hence `p ≠ I_4`. Exact rational row rank of
the displayed matrix is `3`. Equivalently, `im(p)` is spanned by the three
independent vectors `|00>`, `|01> + |10>`, `|11>`.

## Theorem 3 — The corner is `M_3` with unit `p`

The corner `C = p T_2 p = p M_4(C) p` is a unital `*`-algebra with unit `p`.
Its complex dimension is `rank(p)^2 = 9 = dim_C M_3(C)`.

The map `ψ : M_3(C) → C` defined on matrix units by
`ψ(E_{ij}) = |e_i><e_j|` is a `*`-isomorphism, and `ψ(I_3) = p`.

Proof. For any `X, Y ∈ M_4(C)`,

`(p X p)(p Y p) = p X p Y p ∈ C`, `(p X p)* = p X* p ∈ C`,

so `C` is a `*`-subalgebra of `M_4(C)`. The element `p = p I_4 p` lies in
`C`, and `p (p X p) = p X p = (p X p) p`, so `p` is the unit of `C`.

A rank-`k` orthogonal projection in `M_n(C)` has corner `p M_n p ≅ M_k(C)`
of dimension `k^2`. Here `k = 3`, so `dim_C C = 9`. The runner also computes
this dimension as the exact rational rank of the sixteen compressed matrix
units `{p E^{(4)}_{ab} p}_{1 ≤ a,b ≤ 4}`.

On the orthonormal basis `|e_1>`, `|e_2>`, `|e_3>` of `im(p)`, the operators
`|e_i><e_j|` satisfy the matrix-unit table

`|e_i><e_j| |e_k><e_l| = δ_{jk} |e_i><e_l|`, `(|e_i><e_j|)* = |e_j><e_i|`,

and each equals `p |e_i><e_j| p` because `p |e_i> = |e_i>`. Linear
independence of the nine units is the matrix-unit theorem. Therefore `ψ` is
a `*`-isomorphism onto `C`. The unit is

`ψ(I_3) = |e_1><e_1| + |e_2><e_2| + |e_3><e_3|`.

The first and third summands are the coordinate projectors onto `|00>` and
`|11>`. The middle summand is the Fraction matrix

```
|e_2><e_2| = [[0,   0,   0, 0],
              [0, 1/2, 1/2, 0],
              [0, 1/2, 1/2, 0],
              [0,   0,   0, 0]]
```

and the sum is the displayed `p`.

The same corner is available over `Q` without storing `√2`. The integer
spanning set `|w_1> = |00>`, `|w_2> = |01> + |10>`, `|w_3> = |11>` has Gram
matrix `G = diag(1, 2, 1)`. If `W` is the `4 × 3` matrix with those columns,
the map `φ(X) = W G^{-1} X W*` is a unital algebra isomorphism `M_3(C) → C`
given by integer and Fraction matrices, and `φ(I_3) = p`. It is generally not
`*`-preserving. The ON map `ψ` is the `*`-isomorphism; it is `φ` transported
along the diagonal rescaling that sends `|w_2>` to `|e_2>`. The integer
ket-bras `|w_i><w_j|` obey the matrix-unit table with structure constants
`<w_j|w_k>` and are closed under adjoint.
The runner checks `φ` as an algebra map, checks that table, and checks
`ψ(I_3) = p` by summing the three ON rank-1 projectors.

## Theorem 4 — The displayed inclusion into `M_4` is not unital

The displayed inclusion `C ↪ M_4(C)` is **not** unital: `p ≠ I_4`. It is a
corner host whose internal unit is `p`, while the ambient unit is `I_4`.

The unit of `T_2` remains `I_2 ⊗ I_2 = I_4`. A unital algebra homomorphism
`M_3(C) → T_2` would have to send `I_3` to `I_4`. The displayed `ψ` sends
`I_3` to `p`, so the composite map into `M_4(C)` is not unital. Whether some
other algebra or some other map admits a unital `M_3(C)` embedding is outside
this theorem.

## Physical-Identification Boundary

Qubit still names one-site `M_2(C)`. This note uses an explicitly supplied
two-factor tensor construction and a displayed swap. It supplies no `SU(3)`
action, QCD identification, Qubit rewrite to `M_3(C)`, or physical
color-selection map.

The four axioms do not name a three-dimensional internal algebra. Hosting
`M_3(C)` as a corner of `T_2` with unit `p` is a type fact about a displayed
projector. No claim about every possible color construction or every possible
composite is made.

## Falsifiers And Mutation Targets

The predicate `p == I_4` must fail.
The predicate `rank(p) == 4` must fail.
The predicate `dim_C(C) == 9` must hold.

All three are runner-checked by constructing `p` from `F` and computing exact
rational ranks.

## No-Go Discipline Gate

The only negative theorem is local: the displayed inclusion `C ↪ M_4(C)` is
not unital because its image of the internal unit is `p ≠ I_4`. The physical
identification sentences above are non-claims: no identification map is
supplied here. This packet asserts no universal no-go for other composites,
other projectors, or other embeddings.

### N1 — materially distinct routes

Each route tries to defeat the exact claim `p ≠ I_4` by a different invariant
or object. All are checked in this cycle by the paired runner.

| Route family | Exact attack | Exact outcome | Marker |
|---|---|---|---|
| Entry equality | compare the displayed matrices entry by entry | `p_22=1/2` while `(I_4)_22=1` | **ATTEMPTED** |
| Rank invariant | compare the ranks of the candidate units | `rank(p)=3`, `rank(I_4)=4` | **ATTEMPTED** |
| Trace invariant | compare traces independently of row reduction | `Tr(p)=3`, `Tr(I_4)=4` | **ATTEMPTED** |
| Vector action | act on `v_-=|01>-|10>` | `p v_-=0`, while `I_4 v_-=v_-≠0` | **ATTEMPTED** |
| Complementary spectral projection | compute `q=I_4-p` | `q` is a nonzero rank-1 projection and `pq=0`, so `p` cannot be `I_4` | **ATTEMPTED** |
| Corner-membership test | test the ambient unit against `X=pXp` | `p I_4 p=p≠I_4`, so `I_4` is not the internal unit of the displayed corner | **ATTEMPTED** |

These are routes against one local equality. They do not enumerate routes to a
physical color theory, because no such negative claim is made.

### N2 — wall independence and collapse

There is no multi-wall claim. Rank, trace, vector action, the complement, and
corner membership are independent checks of the same obstruction, not five
walls.

| Raw pair | First closes second? | Second closes first? | Collapse |
|---|---:|---:|---|
| `rank(p)=3` / `Tr(p)=3` for this projection | yes | yes | same spectral multiplicity |
| `q` projects onto `span{v_-}` / `p v_-=0` with `v_-≠0` | yes | yes | same nonzero complementary eigenspace |
| `p≠I_4` / displayed inclusion is non-unital | yes | yes | unit-preservation definition |

Collapsed obstruction set: `{p ≠ I_4}`. No physical identification is counted
as a wall.

### N3 — hidden-condition scan

| Item | Classification |
|---|---|
| `T_2 = M_2 ⊗ M_2 ≅ M_4(C)` | explicit bounded mathematical input; not attributed to the axioms |
| displayed swap `F` | explicit test matrix, not attributed to the axioms |
| `p = (I_4+F)/2` | spectral projection of that matrix |
| ON basis of `im(p)` | explicit; middle vector uses `√2` only as a label; runner identities are Fraction/integer |
| `*` | conjugate transpose on finite matrices |
| rank | exact rational row rank |
| “corner host” | unital `*`-algebra `p M_4 p` with unit `p` |
| physical color, `SU(3)`, QCD | scope non-claims; no identification map is supplied |
| observations or fitted constants | none |

The scan found no hidden condition beyond the now-explicit composite choice
and displayed swap. No continuum limit, gauge connection, representation
theory of `SU(3)`, or empirical color quantum number is used.

### N4 — source residual matching

| Source and locator | Residual addressed there | Residual here | Match and limit |
|---|---|---|---|
| [`docs/MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md), lines 43–53 | one-site possibility algebra `M_2(C)` only | displayed two-factor corner algebra | no residual match; used only for one-site context, not as a witness |
| this note, Theorems 1–4 and paired runner | displayed `F`, `p`, corner, and unit comparison | displayed inclusion non-unitality | exact match; self-contained current-cycle calculation |

No prior no-go is used as authority. The swap identities, projector, corner
dimension, `*`-isomorphism, and unit mismatch are proved here.

### N5 — resolution and rhetoric audit

| Resolution | Executed claim | Claim not made |
|---|---|---|
| per element | entries of `F`, `p`, `I_4`, and the corner matrix units | no classification of every projector in `M_4` |
| per site | the explicitly supplied two-factor tensor object only | no framework-wide composite rule |
| per mode | the `+1` and `−1` modes of the displayed swap | no spectral exhaustion of other involutions |
| per block | the displayed corner and its inclusion in one `M_4(C)` | no physical internal-algebra identification |
| lattice-wide | checked and not executed: the theorem supplies no lattice-wide carrier | no lattice-wide existence or no-go |

The negative wording is therefore restricted to the displayed inclusion. The
runner cache carries all five canonical resolution-certificate lines with the
same boundary.

### N6 — live partial-closure paths

1. A unital embedding of `M_3(C)` into some other algebra or by some other map
   is a separate question and remains open here.
2. A different involution or a different two-site operator could host a
   different corner; this note tests only the displayed swap.
3. The traceless anti-Hermitian part of an abstract `M_3(C)` can be studied as
   a Lie algebra, but that mathematical reframe supplies no physical gauge or
   QCD identification.
4. A separate retained derivation or explicitly approved primitive could
   supply a physical internal-algebra identification; this theorem neither
   assumes nor forecloses such work.
5. Merely naming the corner “color” would be a labeling convention, not a
   derivation, so this note does not use that retirement path.

Scale reference, kinetic isotropy, and realized state were checked in the
premise registry. None is load-bearing here, and none is counted as a wall.
No new axiom is claimed to be necessary.

### N7 — concrete-mechanism steelman

The strongest objection says that `ψ:M_3(C)→C` **is** unital because
`ψ(I_3)=p`, the unit of `C`; therefore “not unital” looks false. The objection
correctly identifies a codomain ambiguity, but it does not defeat the scoped
claim. The map `ψ` is unital as a map into `C`. The composite displayed map
`M_3(C)→C↪M_4(C)` is not unital relative to the ambient codomain because it
sends `I_3` to `p≠I_4`. The terminal obligation is exactly the unit comparison,
which the six N1 routes close. Steelman disposition: **CLOSED**.

### N8 — cross-cycle echo

| Echo | Status/mechanism checked | Could it retire this obstruction? |
|---|---|---|
| `TWO_SITE_QUBIT_TENSOR_CARRIER_BRIDGE_NARROW_THEOREM_NOTE_2026-06-06.md` | supplies a distinct two-site tensor-carrier discussion and explicitly separates that surface from locality-alone composition | no; changing the composite authority does not make this displayed `p` equal `I_4` |
| `TENSOR_COMPOSITION_REQUIRES_LOCAL_TOMOGRAPHY_BEYOND_LOCALITY_NARROW_NO_GO_NOTE_2026-06-03.md` | records a composition-authority boundary, not a corner-unit calculation | no; its reframe concerns how `M_4` is supplied, not the units inside the displayed corner |
| PR #6251 as it stood on 2026-08-13 | an in-flight, unlanded top-left-pad proposal with a similar rank-3 unit mismatch | no authority is imported; this note independently recomputes the swap corner |

The search found no convention or reframe that turns the displayed rank-3
projection into `I_4`. It did find live alternative routes to physical
identification, so no broader no-go is asserted.

N1–N8 disposition: **PASS** for the exact non-unitality of the displayed
corner inclusion. The packet grants no standing to any broader negative claim.

## Excluded Broader Claims

This note makes none of the following claims:

- “color is selected by the two-site swap”
- “the axioms derive QCD or `SU(3)`”
- “`M_3(C)` is a unital factor of `T_2`”
- “Qubit should be rewritten to `M_3`”
- “an axiom update is necessary”
- “this constructs the Standard Model color algebra”

The shipped claim is only: conditional on the explicit standard two-factor
tensor construction, the displayed swap projector hosts a corner
`p M_4 p ≅ M_3(C)` whose internal unit is `p`, and the displayed inclusion
does not preserve the ambient unit `I_4`.

## Provenance

Framework context on `origin/main`: the axiom memo only. The runner binds

`AUDIT_INPUT_PATHS = (this note, docs/MINIMAL_AXIOMS_2026-06-29.md)`

as a string-literal tuple. The tracked citation manifest acknowledges the new
note node, and the paired cache is generated by `scripts/runner_cache.py`.
Neither artifact supplies an additional scientific premise.
