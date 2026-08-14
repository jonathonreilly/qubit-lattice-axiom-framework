---
claim_id: factor_swap_names_corner_not_aut_of_corner_bounded_theorem_note_2026-08-14
claim_type: bounded_theorem
claim_scope: "On the supplied host H=C^2⊗C^2, the factor-swap F is a Hermitian involution and p=(I+F)/2 is its unique rank-3 +1 spectral projection. The corner A=p M_4 p has unit p. The identity of im(p) and the displayed 3-cycle of the ON basis of im(p) extend to two elements U0, Uω of A that fix p, satisfy U_i^* U_i=p, and induce Ad_0≠Ad_ω on A. F restricts to the identity on im(p), so Ad_F=id_A. Naming p is naming the carrier, not an element of Aut(A). Live Lattice+Qubit+Record do not name the 3-cycle. No SU(3), QCD, or Qubit rewrite is supplied."
upstream_dependencies:
  - minimal_axioms
  - two_site_swap_corner_hosts_m3_with_unit_p_bounded_theorem_note_2026-08-13
runner: scripts/factor_swap_names_corner_not_aut_of_corner_2026_08_14.py
---

# Factor-Swap Names The Corner, Not Aut Of The Corner

**Date:** 2026-08-14
**Type:** bounded_theorem
**Scope:** exact identities on the supplied two-site host `H = C^2 ⊗ C^2`
and the displayed rank-3 swap corner `A = p M_4 p`. The note separates
the naming of the carrier `p` from a choice of element of `Aut(A)`.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/factor_swap_names_corner_not_aut_of_corner_2026_08_14.py`](../scripts/factor_swap_names_corner_not_aut_of_corner_2026_08_14.py)
**Parents:** the live axiom memo
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) and the
displayed swap-corner host
[`TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md`](TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md).

This is Aut of the two-site corner. It is not a 3-menu, not a unital
`M_3` factor of `M_4`, not a pairing table, and not a one-site adjoint
fork.

## Result Up Front

Write `H = C^2 ⊗ C^2` with product basis `|00>, |01>, |10>, |11>`. The
factor-swap is the linear map `F|a b⟩ = |b a⟩`. It is Hermitian and
`F^2 = I_4`. The unique rank-3 spectral projection of `F` at `+1` is

`p = (I_4 + F)/2`.

The leftover complementary projection `I_4 − p` has rank 1. The corner

`A = p M_4(C) p`

is a unital `*`-algebra with unit `p`, not `I_4`. Identifying `A` with
`End(im(p)) ≅ M_3(C)` along the orthonormal basis of `im(p)` displayed
below is a chart of that corner, reconstructed locally.

Two unitaries of `im(p)`, extended by zero on `im(I_4 − p)`, give
elements `U_i = V_i ⊕ 0 ∈ A` with `U_i^* U_i = p`:

- `V_0` is the identity of `im(p)`, so `U_0 = p`;
- `V_ω` is the 3-cycle `e0 ↦ e1 ↦ e+ ↦ e0`.

Write `Ad_i(X) = U_i X U_i^*` on `A`. Then `Ad_0(E_{00}) = E_{00}` and
`Ad_ω(E_{00}) = |e1⟩⟨e1| ≠ E_{00}`, where `E_{00} = |e0⟩⟨e0| ∈ A`. Both
maps fix the corner unit: `Ad_i(p) = p`. Therefore `Ad_0 ≠ Ad_ω` as
automorphisms of `A`.

`F` names that carrier: `p` is the rank-3 `+1` spectral projection of
the unique linear factor-swap. That names `p`, not an element of
`Aut(A)`. Control: `F` fixes each of `e0`, `e1`, `e+`, so
`F|_{im(p)} = I_{im(p)}` and `Ad_F` is `id_A`. The unique factor-swap
does not supply the 3-cycle.

Live Lattice, Qubit, and Record do not name `V_ω` or `Ad_ω`. Record
locks one local possibility per site; it does not lock a two-site
automorphism. Both `Ad` maps are displayed. No `SU(3)` action and no
QCD identification is adopted.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "Exact Fraction identities separate the rank-3 swap carrier from Aut of its corner by displaying two p-fixing automorphisms that disagree, while F restricts to the identity on im(p). Live axioms are quoted and do not name the 3-cycle."
trace_class: frontier_discovery
target_claim_id: factor_swap_names_corner_not_aut_of_corner
target_blocker_text: "whether uniquely naming the SWAP rank-3 corner already names an element of Aut of that corner"
source_of_blocker_text: handoff
reachability_to_target: advances
artifact_role: theorem
next_trace_action: "independent audit of the bounded algebraic separation; no physical Aut element is claimed"
conditional_surface_status: "exact on the supplied host H=C^2⊗C^2 and the displayed swap corner; other involutions, other bases, and physical actions remain unclaimed"
hypothetical_axiom_status: "none; F, Vω, and Ad_ω are displayed operator data and are not proposed as axiom content"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Live Parent Quotes

Quoted from the live axiom memo, without rewrite:

> The full one-site possibility domain has algebraic presentation `M_2(C)`.

> When present, a record locks exactly one admissible local possibility.

> Only records are readable. A readout value is determined by record content
> alone. A site with no record cannot be read.

> Physical sites are the points of the cubic lattice `Z^3`, with
> nearest-neighbor adjacency, standard translations, and proper cubic
> rotations about each site.

Their role is vocabulary and the local lock rule. They do not name a
two-site automorphism of `p M_4 p`.

## Inputs And Support Boundary

- **Framework dependency:** the quoted Qubit, Record, and Lattice sentences.
  Qubit is not rewritten to `M_3`.
- **Explicit theorem-domain condition:** the host `H = C^2 ⊗ C^2`, the
  linear factor-swap, and the ON basis of `im(p)` are supplied mathematical
  data. The two-factor tensor is not attributed to the four axioms.
- **Parent corner host:** the 2026-08-13 swap-corner note records that
  `A = p M_4 p` is `*`-isomorphic to `M_3(C)` with unit `p`. The
  identification is reconstructed here on the same displayed basis.
- **External empirical or literature inputs:** none.
- **Physical-identification boundary:** no `SU(3)`, QCD, color action, or
  gauge coupling is supplied or adopted.

## Exact Objects

All runner coefficients are exact `Fraction` values. The factor `√2`
labels the ON middle vector only.

In the product basis `|00>, |01>, |10>, |11>`,

```text
F = ((1,0,0,0), (0,0,1,0), (0,1,0,0), (0,0,0,1)).
```

`p = (I_4 + F)/2` is the displayed matrix

```text
p = ((1,0,0,0), (0,1/2,1/2,0), (0,1/2,1/2,0), (0,0,0,1)).
```

An orthonormal basis of `im(p)` is

```text
e0 = |00⟩
e1 = |11⟩
e+ = (|01⟩+|10⟩)/√2
```

The integer spanning set `|w0⟩ = |00⟩`, `|w1⟩ = |11⟩`,
`|w+⟩ = |01⟩+|10⟩` has Gram `diag(1,1,2)` and the same span. The runner
uses that spanning set for every `4 × 4` identity.

Identify `A` with `End(im(p)) ≅ M_3(C)` in the ordered basis
`(e0, e1, e+)`. Matrix units are `E_{ij} = |e_i⟩⟨e_j|`. In that chart,

```text
V0 = I_3
Vω = ((0,0,1), (1,0,0), (0,1,0))
```

so `V_ω e0 = e1`, `V_ω e1 = e+`, `V_ω e+ = e0`. Extend by zero on
`im(I_4 − p)`:

`U_i = V_i ⊕ 0`, hence `U_i = p U_i p ∈ A` and `U_i^* U_i = p`.
Explicitly `U_0 = p`. Conjugation on `A` is `Ad_i(X) = U_i X U_i^*`.

## Exact Target And Obligation Graph

**Exact target.** Display two automorphisms of `A` that fix `p` and
disagree, record that `F` names the carrier `p` rather than an element
of `Aut(A)`, and record that live Lattice+Qubit+Record do not name
`V_ω`.

| Obligation | Role | Disposition |
|---|---|---|
| `F^* = F = F^{-1}`, `p = (I+F)/2` rank 3 | carrier | proved; runner checks |
| `A` unital with unit `p` | carrier | reconstructed from the displayed corner |
| `Ad_0 ≠ Ad_ω` on `A`, both fix `p` | Theorem 1 | proved on `E_{00}` |
| `p` is the unique rank-3 `+1` projection of `F` | Theorem 2 | spectral calculus of a Hermitian involution |
| `F|_{im(p)} = I` and `Ad_F = id_A` | Control | proved on the spanning set |
| live Lattice+Qubit+Record name `V_ω` or `Ad_ω` | Theorem 3 | fails; sentences quoted |
| `SU(3)` or QCD as axiom content | out of scope | live memo does not name them |

## Theorem 1 — Two automorphisms of `A` disagree

`Ad_0` and `Ad_ω` are unital `*`-automorphisms of `A`, both fix `p`,
and `Ad_0 ≠ Ad_ω`.

Proof. `V_0` and `V_ω` are unitary on `im(p)`: `V_0 = I_3` and `V_ω` is
a real permutation matrix with `V_ω^* V_ω = I_3` and `V_ω^3 = I_3`.
Zero extension yields partial isometries `U_i ∈ A` with
`U_i^* U_i = p = U_i U_i^*`. Conjugation by a unitary of the corner is
a unital `*`-automorphism of `A`, and `Ad_i(p) = U_i U_i^* = p`.

Let `E_{00} = |e0⟩⟨e0| ∈ A`. Then `Ad_0(E_{00}) = E_{00}` and

`Ad_ω(E_{00}) = |V_ω e0⟩⟨V_ω e0| = |e1⟩⟨e1|`.

These rank-1 projections are distinct because `e0` and `e1` are
orthonormal. Hence `Ad_0 ≠ Ad_ω`.

## Theorem 2 — `F` names the carrier, not an element of `Aut(A)`

The linear factor-swap is the unique map sending `|a b⟩` to `|b a⟩` on
the four product-basis vectors, so its matrix is the displayed `F`.
Because `F^* = F` and `F^2 = I_4`, the only possible eigenvalues are
`±1`, and the spectral projection at `+1` is uniquely
`p = (I_4 + F)/2`. Exact rational rank gives `rank(p) = 3`. That is the
usual naming of the rank-3 swap corner.

Quote, as the content of this theorem: that names the carrier, not an
element of `Aut(A)`. Theorem 1 exhibits two distinct automorphisms of
the same unital algebra `A` that both fix `p`. Naming `p` therefore
does not select `Ad_0` over `Ad_ω`, nor the reverse.

## Theorem 3 — Live Lattice+Qubit+Record do not name `V_ω`

The quoted Lattice sentence names sites of `Z^3` and their cubic
isometries. It does not name a 3-cycle of a two-site symmetric
subspace.

The quoted Qubit sentence names one-site `M_2(C)`. It does not name
`V_ω`, `Ad_ω`, or a rewrite of Qubit to `M_3`.

The quoted Record sentences lock exactly one admissible local
possibility at a site, when a record is present, and make only records
readable. A record does not lock a two-site automorphism of `p M_4 p`.

Therefore the live axioms do not name `V_ω` or `Ad_ω`. Displaying both
`Ad` maps does not adopt `SU(3)` or QCD. The live axiom memo does not
contain `SU(3)` or QCD as axiom content.

## Control — The factor-swap is not the 3-cycle

`F` exchanges tensor factors. `V_ω` cycles a 3-basis of the symmetric
subspace. These are different maps.

Direct action on the spanning set of `im(p)`:

```text
F e0 = e0,    F e1 = e1,    F e+ = e+
```

because `F|00⟩ = |00⟩`, `F|11⟩ = |11⟩`, and
`F(|01⟩+|10⟩) = |10⟩+|01⟩`. Hence `F|_{im(p)} = I_{im(p)}`. In the
`(e0, e1, e+)` chart this restriction is `I_3`, while `V_ω ≠ I_3`.
The predicate "`F|_{im(p)}` equals `V_ω`" therefore fails.

For every `X ∈ A` one has `X = p X p` and `F p = p`, so
`F X F = X`. Thus `Ad_F` on `A` is `id_A`. The unique factor-swap
supplies the identity automorphism, not the 3-cycle.

## Honest-Auditor / Boundary

The strongest reading against the separation is that `A ≅ M_3(C)` has
a large automorphism group, so of course two automorphisms exist, and
the 3-cycle looks canonical once the basis `(e0, e1, e+)` is written
down. That reading is correct as abstract algebra and does not touch
the claim. The claim is not that `Aut(A)` is trivial. The claim is
that the factor-swap, which uniquely names `p`, induces `id_A` and
therefore does not pick an element of `Aut(A)` beyond the identity.
A different ordering of the same three rays, such as
`e0 ↦ e+ ↦ e1`, produces a different 3-cycle. The live axioms name
neither cycle.

A second reading says the corner isomorphism `A ≅ M_3(C)` already
"is" a color action. The isomorphism is a chart of a `*`-algebra with
unit `p`. It does not supply a physical frame, a compact group action
on spacetime, or a coupling. This note does not adopt `SU(3)` or QCD.

A third reading says Record could lock the 3-cycle because the cycle
is finite. Record locks one admissible local possibility at one site.
The 3-cycle is an automorphism of a two-site corner, not a local
possibility.

Boundary cases left outside the target: non-Hermitian implementers of
factor exchange, other involutions, other two-site hosts, a physical
composition rule for two sites, and any naming of a preferred element
of `Aut(A)`.

## Mutation Checks

The following predicates must fail, and the runner checks each:

1. `Ad_0 == Ad_ω`;
2. `F|_{im(p)}` equals `V_ω`;
3. the live axiom memo names `SU(3)` or QCD as axiom content.

## What This Does Not Claim

- The two-site host is not a derived physical composition rule.
- The corner is not a unital `M_3` factor of `M_4`; its unit is `p`.
- The displayed 3-cycle is not selected by Lattice, Qubit, or Record.
- No `SU(3)` action, QCD identification, or Qubit rewrite is supplied.
- No pairing table and no one-site adjoint fork is computed here.
- Existence of many automorphisms of `A` is not a physical color
  action.

These are scope boundaries, not route-exhaustion claims.

## Provenance

Framework context on `origin/main`: the axiom memo, together with the
already-landed swap-corner host note. The runner binds

```text
AUDIT_INPUT_PATHS = (
    this note,
    docs/TWO_SITE_SWAP_CORNER_HOSTS_M3_WITH_UNIT_P_BOUNDED_THEOREM_NOTE_2026-08-13.md,
    docs/MINIMAL_AXIOMS_2026-06-29.md,
)
```

as a string-literal tuple. Uniqueness of `p` as the rank-3 `+1`
projection of the displayed factor-swap is reconstructed here from
`F|ab⟩ = |ba⟩` and spectral calculus; no unmerged change is cited.
