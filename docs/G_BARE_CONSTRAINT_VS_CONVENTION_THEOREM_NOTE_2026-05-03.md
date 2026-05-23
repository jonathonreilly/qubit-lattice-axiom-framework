# g_bare Constraint vs Convention Disambiguation Theorem

**Date:** 2026-05-03 (2026-05-18: claim_scope formalized as local
class-A result per audit verdict boundary instruction; 2026-05-23:
post-audit scope repair makes `beta = 6` an explicit local Wilson-surface
input and wires the retained Wilson-matching authority)
**Claim type:** bounded_theorem
**Claim scope (post-2026-05-23 narrowing):** the load-bearing content
of this note is **the local class-A algebraic result that "CN
[canonical normalization]" + the Wilson small-a matching relation
`beta = 2 N_c / g_bare^2` + the explicit local Wilson evaluation
surface `N_c = 3`, `beta = 2 N_c = 6` imply `g_bare = 1`**.
This is a conditional bounded algebraic identity on the declared
canonical-normalization + Wilson-matching + local-`beta = 6` surface;
it **does NOT** derive `beta = 6` from `A1 + A2`, does NOT by itself
retain `G_BARE_DERIVATION_NOTE`, and does NOT close the broader
g_bare = 1 hierarchy input.
**Status authority:** independent audit lane only.
**Status:** unaudited candidate. This note is graph-visible only so the
independent audit lane can decide whether the candidate is retained. Do not
update or promote `G_BARE_DERIVATION_NOTE.md` or downstream status surfaces
from this note unless this row, the rescaling-freedom row, and their declared
dependency chain become retained-grade through independent audit.
**Primary runner:** `scripts/frontier_g_bare_constraint_surface_check.py`

## 0. Audit context

This note is repair target #3 of the
`G_BARE_DERIVATION_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02` packet, which
identified the unresolved constraint-vs-convention ambiguity in the parent
`G_BARE_DERIVATION_NOTE.md` row. The repair target was:

> *"the decisive step identifies the canonical Cl(3) connection
> normalization with unit gauge coupling, while the note explicitly leaves
> open whether that is a constraint or a convention."*

The present note proposes a disambiguation of the two readings by exhibiting the precise
sense in which `g_bare = 1` is a structural constraint relative to a
declared bounded surface: canonical Cl(3) connection normalization,
retained Wilson small-a matching, and local Wilson evaluation at
`N_c = 3`, `beta = 6`. The honest input layer is upstream of `g_bare`
itself.

## 1. Claim scope

> **Theorem (Constraint-vs-convention disambiguation).**
> Let
> ```
> Tr(T_a T_b) = delta_{ab} / 2                                     (CN)
> ```
> be the canonical Cl(3) connection normalization on the canonical triplet
> block carried directly by `CL3_COLOR_AUTOMORPHISM_THEOREM.md`,
> use the Wilson small-a matching relation
> ```
> beta = 2 N_c / g_bare^2                                          (WM)
> ```
> on the retained rescaling-freedom / Wilson-matching surface,
> and use the inline algebraic consequence that a generator dilation
> `T_a -> c T_a` with `c != 1` violates (CN). Under (CN), the Wilson
> canonical evaluation point is taken here as the explicit local input
> `N_c = 3`, `beta = 2 N_c = 6`. Then:
>
> 1. **Structural constraint.** The unique value of `g_bare` compatible with
>    (CN) and (WM) at `N_c = 3` and `beta = 2 N_c = 6` is `g_bare = 1`. Any
>    alternative `g_bare != 1` either (a) violates (CN) by introducing a
>    `c != 1` generator dilation (forbidden by the inline (CN) check),
>    OR (b) changes the admitted local Wilson evaluation surface by
>    replacing `beta = 6` with another beta value. In either case, the
>    alternative is not a free `g_bare` convention on the same declared
>    bounded surface.
>
> 2. **Honest input layer.** The convention status of `g_bare = 1` is
>    not at `g_bare` itself; it is upstream, at the canonical
>    normalization (CN) and the local Wilson `beta = 6` surface. With (CN)
>    treated as an admitted convention (its
>    classification on the
>    `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`
>    surface), and with the local Wilson surface explicitly fixed,
>    `g_bare = 1` follows as a structural constraint, not a separate
>    convention choice.
>
> Equivalently: the framework has one canonical normalization convention
> (CN) plus one local Wilson evaluation surface (`beta = 6` at `N_c = 3`),
> and `g_bare = 1` is the algebraic value fixed by those inputs. There is
> no second, independent `g_bare` convention layer **inside that bounded
> surface**.

The theorem **does not** claim:

- that the canonical normalization (CN) is itself uniquely forced by the
  framework axioms (the convention-vs-derivation status of (CN) is
  precisely what the narrow convention theorem documents as an admitted
  convention);
- that the Wilson plaquette action form is uniquely forced (see Claim 3
  caveat in `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`);
- that the local Wilson evaluation surface `beta = 6` is derived from
  `A1 + A2`; `beta = 6` is an explicit bounded-surface input here;
- closure of the deeper question of whether the framework's normalization
  axioms `A4` are themselves derivable from `A1 + A2` alone.

## 2. Declared audit dependencies (one hop) — 2026-05-23 repair

| Authority | Audit-lane status | Role |
|---|---|---|
| [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md) | `retained` | carries the canonical Cl(3) / SU(3) generator normalization `Tr(T_a T_b) = delta_{ab} / 2` (CN) used in the load-bearing step. |
| [`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`](G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md) | `retained` | supplies the Wilson small-a matching relation `beta = 2 N_c / g_bare^2` and the rescaling-freedom boundary on the canonical-normalization surface. |

The 2026-05-23 audit repair intentionally wires the retained
rescaling-freedom row as a one-hop authority because the latest audit
identified the missing Wilson-matching / `beta = 2 N_c` edge as the
blocker. The additional local input `beta = 6` is not claimed to be
derived by either authority; it is the explicit bounded Wilson evaluation
surface on which this note's algebra is audited.

### 2.1 Why this repair is audit-named, not novel

The latest audited ledger row for this note recorded:

> *missing repair: dependency_not_retained: retain-grade or
> **re-architect the rescaling-freedom dependency** before re-auditing
> the broader constraint-vs-convention conclusion.*

and then refined the remaining blocker to a missing one-hop authority for
the Wilson plaquette matching / `beta = 2 N_c` normalization input. The
present revision adopts that named repair. The reasons:

- The rescaling-freedom-removal note is now retained on the audit ledger,
  so it can be used as the one-hop authority for the Wilson small-a
  matching relation (WM).
- The present note does not introduce a new axiom or new normalization
  law. It narrows the target: `beta = 6` is an explicit local Wilson
  evaluation input on this bounded surface.
- The runner already verifies the local algebra exactly with `Fraction`
  arithmetic; the repair changes the authority and scope statement, not
  the algebraic substitution.

## 3. Load-bearing step (class A)

```text
Given:
  (CN) Tr(T_a T_b) = delta_{ab} / 2     (canonical normalization; carried
                                         directly by cl3_color_automorphism)
  (WM) beta = 2 N_c / g_bare^2          (Wilson small-a matching; supplied by
                                         the retained rescaling-freedom row)
  (B6) N_c = 3 and beta = 2 N_c = 6     (explicit local Wilson evaluation
                                         surface; assumed here, not derived)
  (RR) Inline algebraic consequence of (CN), no separate one-hop dep:
       a generator dilation T_a -> c T_a with c != 1 immediately
       produces Tr((c T_a)(c T_b)) = c^2 * delta_{ab}/2 != delta_{ab}/2,
       violating (CN). Therefore under (CN), the continuum rescaling
       A -> c * A is not a free reparametrization of g_bare; it
       shifts the action coefficient beta = c^2 * beta at fixed
       g_bare. Alternative g_bare values either violate (CN) (case a,
       by this inline check) or change the local beta surface (case b).

At N_c = 3 on the explicit local Wilson surface beta = 2 N_c = 6,
the unique compatible g_bare^2 follows by exact algebra:

  g_bare^2 = 2 N_c / beta = 6 / 6 = 1                       (class A)

i.e., g_bare = 1.

For any alternative g_bare^2 != 1 at the same N_c = 3:
  case (a): the alternative requires a generator dilation T_a -> c T_a
            with c^2 = g_bare^(-2) != 1, which violates (CN).
  case (b): the alternative keeps (CN) and WM but changes the local
            Wilson evaluation surface to beta != 6.

Therefore: the unique g_bare consistent with (CN), (WM), and the local
beta = 6 Wilson surface is g_bare = 1. The honest convention/input
layer is upstream at the canonical normalization and Wilson evaluation
surface, not a separate g_bare convention on top of them.
```

The load-bearing step is class (A) — algebraic substitution into the
matching identity (WM), specialized to the canonical normalization (CN)
and the explicit local Wilson surface `N_c = 3`, `beta = 6`. The
`beta = 6` surface is a declared input of this bounded theorem, not a
derived conclusion.

## 4. Why this differs from the narrow convention theorem

The existing
`G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md`
classifies `g_bare = 1` itself as an admitted Wilson canonical-normalization
convention, settling that the narrow theorem's status row is honest about
its convention layer. The narrow convention theorem **does not** claim
that `g_bare = 1` is structurally forced; it explicitly classifies it as
a convention.

The present theorem is the complementary *constraint reading*: with the
canonical Cl(3) connection normalization (CN) and the local Wilson
`beta = 6` evaluation surface fixed, `g_bare = 1` follows as a
structural algebraic constraint, not as a separate convention. The two
readings of the parent
`G_BARE_DERIVATION_NOTE.md` are reconciled as follows:

- **Convention reading (narrow theorem):** `g_bare = 1` is itself the
  Wilson canonical convention. The convention layer is at `g_bare`.
- **Constraint reading (present theorem):** the convention/input layer is
  at the canonical Cl(3) normalization (CN) plus the local Wilson
  `beta = 6` surface. With those fixed, `g_bare = 1` is a derived
  algebraic constraint.

The two readings are not contradictory: the narrow theorem accepts the
convention status as a Wilson-action-side admission, while the present
theorem fixes the upstream CN + local beta surface and shows that
`g_bare = 1` is structurally forced on that bounded surface.

The honest disambiguation: **`g_bare = 1` is a constraint relative to the
canonical Cl(3) connection normalization and the local Wilson `beta = 6`
surface; this note does not derive either input from `A1 + A2`.**

## 5. Verification

```bash
python3 scripts/frontier_g_bare_constraint_surface_check.py
```

Verifies, in `Section E` of the runner:

1. The local Wilson surface `beta = 2 N_c = 6` for `SU(3)` is checked
   exactly via `Fraction` arithmetic as an explicit bounded input.
2. The unique `g_bare^2 = 2 N_c / beta = 1` is derived as a class (A)
   exact rational.
3. Alternative `g^2` values (`1/2`, `2`, `4`) require `beta != 6`,
   so they leave the declared local Wilson surface.
4. The input layer is explicitly identified: canonical
   `Tr(T_a T_b) = delta/2` is carried by `cl3_color_automorphism_theorem`,
   Wilson matching is carried by the retained rescaling-freedom row, and
   `beta = 6` is the local bounded surface.
5. The constraint layer is explicit: given the canonical normalization,
   retained Wilson matching, and local `beta = 6` surface, `g_bare = 1`
   is structurally forced, with no separate `g_bare` convention layer.

Representative runner checks:

```
[PASS] local Wilson surface beta = 2 N_c = 6 for SU(3) (explicit bounded input)
[PASS] given CN + WM + local beta = 6, g_bare^2 = 1 forced (exact)
[PASS] alternative g^2 = 1/2 requires beta = 12 != 6
[PASS] alternative g^2 = 2 requires beta = 3 != 6
[PASS] alternative g^2 = 4 requires beta = 3/2 != 6
[PASS] input layer: CN, retained Wilson matching, and local beta = 6 are the bounded surface
[PASS] constraint layer: given bounded surface, g_bare = 1 is structurally derived
```

## 6. Audit routing

Audit status is set only by the independent audit lane. This note may land as
an unaudited, graph-visible `bounded_theorem` candidate; retained-family
effective status requires independent audit of this row and retained-grade
closure of the declared dependency chain. The parent
`G_BARE_DERIVATION_NOTE.md` must not be updated or promoted from this
candidate before that happens.

## 7. What this candidate can support after retention

- The bounded-surface constraint-vs-convention ambiguity named on the parent
  `G_BARE_DERIVATION_NOTE.md` row, if independent audit retains this
  candidate and its dependency chain.
- A candidate answer for repair target #3 from
  `G_BARE_DERIVATION_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02`.
- A clean handoff to downstream rows depending on `g_bare = 1`: such
  rows may cite this note for the constraint reading only after retention;
  until then they should keep the current conditional/convention wording.

## 8. What this theorem does NOT close

- The convention-vs-derivation status of the canonical Cl(3) normalization
  (CN) itself.
- Derivation of the local Wilson `beta = 6` surface from `A1 + A2`.
- The choice of the Wilson plaquette action form (Symanzik / improved
  actions remain outside this scope; see
  `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md` Claim 3).
- The deeper question of whether `A4` (the framework's canonical
  normalization axiom) is derivable from `A1 + A2` alone.
- The retained promotion of `G_BARE_DERIVATION_NOTE.md` itself; this
  candidate queues one of the three named repair targets for audit but does
  not close the full promotion pathway.

## 9. Honest scoping summary

The genuine science: the parent's "constraint or convention?" question is
ambiguous because it conflates the `g_bare` value with upstream surface
choices. On the bounded surface audited here, the upstream inputs are:
the canonical Cl(3) connection normalization `Tr(T_a T_b) = delta/2`,
the Wilson small-a matching relation, and the local Wilson evaluation
`beta = 6` at `N_c = 3`. Once those inputs are fixed:

- the retained rescaling-freedom / Wilson-matching row supplies (WM), and
  this note's runner still checks the inline case-(a) consequence of (CN):
  a generator dilation `T_a -> c T_a` changes the canonical trace
  normalization and cannot rescue an alternative `g_bare`;
- changing `g_bare` while preserving (CN) and (WM) changes the declared
  local Wilson surface from `beta = 6` to another beta value (case b);

so the unique compatible value is `g_bare = 1`, derived as a class (A)
algebraic constraint.

What this theorem is honestly **not**: a derivation of (CN), WM, or the
`beta = 6` Wilson surface from `A1 + A2`. If retained by independent audit,
this theorem would close only the *relative* constraint reading on that
bounded surface; the *absolute* derivation of `g_bare = 1` from `A1 + A2`
alone is a strictly stronger Nature-grade target outside the present scope.

## 10. Cross-references

Under the 2026-05-23 repair, the declared one-hop dependencies are
`cl3_color_automorphism_theorem` and
`g_bare_rescaling_freedom_removal_theorem_note_2026-05-03` (linked in §2).
The remaining
cross-references are reader pointers (plain text, not load-bearing for
the citation graph):

- Parent: `G_BARE_DERIVATION_NOTE.md` — may cite this candidate only after
  this row and its dependency chain are retained by independent audit.
- `G_BARE_DERIVATION_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md` — the
  demotion / status correction packet that names the three repair targets.
- `G_BARE_CANONICAL_CONVENTION_NARROW_THEOREM_NOTE_2026-05-02.md` — the
  complementary convention-reading narrow theorem (g_bare = 1 itself
  classified as an admitted Wilson convention). The two readings are
  reconciled in Section 4 above.
- `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md` — the
  broader Cl(3) -> End(V) -> su(3) -> Wilson chain.
- `G_BARE_RIGIDITY_THEOREM_NOTE.md` — upstream rigidity theorem (no scalar
  dilation of T_a, used in the inline rescaling-freedom case-(a) check).
- `MINIMAL_AXIOMS_2026-04-11.md` — `A4` records the canonical normalization
  as the framework's normalization-and-evaluation surface input. The
  present theorem clarifies the relationship between `A4` and `g_bare = 1`.

## 11. Current audit-lane disposition (informational)

This row previously returned `audited_conditional`. The pre-repair
chain-closure rationale recorded in the ledger was:

> *The algebra closes locally, but the one-hop rescaling-freedom-removal
> authority is not retained-grade; it is currently an audited decoration
> boxed under `cl3_color_automorphism_theorem`.*

At that time, the rescaling-freedom row did not provide a retained one-hop
authority for the present row. On the 2026-05-23 main surface, that row is
now retained and can be wired directly for the Wilson small-a matching
relation. The local algebra (class A substitution into the Wilson matching
identity) is unchanged; the source repair updates the authority chain and
narrows the beta surface.

The **2026-05-23 repair** (see §2 above and the date header) addresses
the latest audit's `missing_dependency_edge` result in two ways:
it wires the now-retained rescaling-freedom / Wilson-matching note as a
load-bearing one-hop authority, and it narrows the claim so the local
`beta = 6` Wilson surface is an explicit input rather than a purported
derived consequence of the cited dependency packet. Whether this repair is
accepted is, of course, set by independent audit on this revised row, not
by this note.

Independent of this row, the audit lane has a separate Ward-route program
that reaches `g_bare = 1` via different upstream authorities — see
`G_BARE_TWO_WARD_REP_B_INDEPENDENCE_THEOREM_NOTE_2026-04-19.md`
(now `retained_bounded`) and
`G_BARE_TWO_WARD_SAME_1PI_PINNING_THEOREM_NOTE_2026-04-19.md`
(`audited_conditional`; see-also cross-reference, not a load-bearing
dependency — backticked to break cycle-0001 in the citation graph).
That route is **not** the rescaling-freedom path
this note depends on; it is a parallel disambiguation that does not change
this row's intrinsic dep chain. Cross-reference only — the present theorem
remains scoped to the rescaling-freedom reading and is not promoted by the
parallel Ward-route work.
