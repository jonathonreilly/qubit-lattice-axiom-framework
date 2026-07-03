# g_bare Hilbert–Schmidt Rigidity Theorem (R1–R3 Bounded Algebraic Core)

**Date:** 2026-05-07 (original); 2026-05-27 (R4/R5 narrowed out of scope).
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does
not set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_g_bare_hs_rigidity_narrow.py`](../scripts/frontier_g_bare_hs_rigidity_narrow.py)

## 2026-05-27 Scope Repair

This repair takes the **narrow path**: R1-R3 stay as the load-bearing
bounded algebraic theorem; R4 (connection rescaling redundancy) and R5
(Wilson coefficient routing) are explicitly demoted to out-of-scope
companion observations that **require unsupplied retained bridge
theorems** before they can be load-bearing. No new axiom or import is
added.

This row's claim boundary until those bridges land: R1-R3 are the only
proposed load-bearing core, pending independent audit. This row **must
not** be cited for Wilson action form, running/fixed-point selection,
N_F = 1/2 from Cl(3), absolute g_bare = 1 from A1+A2, or the parent
broad g_bare derivation.

## 2026-06-06 Dependency Reroute

The load-bearing dependency for the embedding/Ad-form inputs is repointed
from `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md` to the
retained `CL3_COLOR_AUTOMORPHISM_THEOREM.md` and
`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`. No content of R1–R3 changes; the
runner is unchanged.

**Why.** The 2026-04-18 structural-normalization note is now
`effective_status = audited_renaming` (terminal: demoted because its
headline *defines* `g = 1` as the unrescaled Wilson convention rather than
deriving it). This row never used that Wilson-action / `g_bare = 1`
content (see "Non-Binding Former Claims" below); it load-bears **only** on
that note's Claim 1 (`Cl(3) → End(V) → su(3)` embedding) and Claim 2
(Ad-invariant trace-form identification), both of which the demoted note
itself flags as **exact structural support**.

**Reroute target (both retained positive-theorems).**
- Claim 1 (embedding): `CL3_COLOR_AUTOMORPHISM_THEOREM.md` realizes
  `su(3) ⊂ End(C^8)` as `M₃_sym ⊗ I₂` on the symmetric base; and
  `GRAPH_FIRST_SU3_INTEGRATION_NOTE.md` closes `su(3)` graph-canonically on
  the taste cube (the route the demoted note's own Claim 1 cites).
- Claim 2 (Ad-form): `CL3_COLOR_AUTOMORPHISM_THEOREM.md` supplies the exact
  triplet trace form `Tr[T^a T^b] = (1/2)δ^{ab}`.

So R1–R3's load-bearing inputs now stand entirely on retained surfaces.
The independent audit lane owns whether this reroute is accepted; this
note proposes it and does not assert a status change.

## 0. Audit context

This note strengthens
`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`.
The 2026-05-03 source surface is a narrow algebraic substitution given
an admitted normalization. The present note carries an independent,
structurally distinct argument:
the Hilbert–Schmidt trace form on `End(V)` *induced from the framework
Hilbert space* is the **unique** Ad-invariant inner product on
`su(3) ⊂ End(V)` up to overall positive scalar (Killing-form rigidity).
Under that fixed form, **no scalar dilation `T_a → c T_a` simultaneously
preserves the trace Gram and the quadratic Casimir** for `c ≠ ±1`.

This is a class (A) algebraic identity whose load-bearing inputs are:

1. the framework Hilbert-space inner product on `V = C^8` (axiom-level
   structure, imported through
   [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md)),
2. simplicity of `su(3)` and Killing-form rigidity (classical),
3. the Cl(3) → End(V) → su(3) embedding (the realization of
   `g_conc = su(3) ⊂ End(V) = End(C^8)`), supplied by the retained
   [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
   (the `M₃_sym ⊗ I₂` embedding on the symmetric base of the taste cube)
   and the retained
   [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
   (the graph-canonical `su(3)` closure on the taste cube). See the
   2026-06-06 dependency reroute below.

The argument does *not* reduce to the canonical Gell-Mann generators
already carrying `T_F = 1/2` (the path used by the 2026-05-03 source
surface). It uses the *form* directly, not the basis-specific
normalization.

## 1. Claim scope

> **Theorem (Hilbert–Schmidt rigidity).**
>
> Let `V` be the framework Hilbert space `C^8` with its fixed
> inner product (carried from the framework axioms via the physical
> lattice retention chain). Let `g_conc = su(3) ⊂ End(V)` be the
> derived gauge subalgebra in the canonical triplet block as fixed by
> the retained [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md)
> (`M₃_sym ⊗ I₂` embedding) and
> [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md). Let
>
> ```
> B_HS(X, Y) := Tr_{V_3}(X Y),     X, Y ∈ g_conc                      (HS)
> ```
>
> be the Hilbert–Schmidt trace form restricted to the triplet block.
>
> Then:
>
> **(R1) Uniqueness up to scalar.** `B_HS` is the unique (up to overall
> positive multiplicative scalar) Ad-invariant symmetric bilinear form
> on `su(3) = g_conc`.
>
> **(R2) Joint rigidity.** Any rescaling `T_a → c T_a` of an
> orthonormal basis `{T_a}` for the *fixed normalization* of `B_HS`
> simultaneously rescales:
> - the trace Gram by `c²`: `B_HS(c T_a, c T_b) = c² · B_HS(T_a, T_b)`,
> - the quadratic Casimir by `c²`: `Σ_a (c T_a)(c T_a) = c² · Σ_a T_a T_a`.
>
> **(R3) No nontrivial joint preservation.** No real `c ≠ ±1` preserves
> both the trace Gram and the quadratic Casimir simultaneously.
> Equivalently, there exists **no scalar dilation that lies in the
> automorphism group of the canonical inner-product structure on
> `g_conc`**.

R1-R3 are the **load-bearing in-scope content** of this row.

The earlier draft included two further claims labeled R4 and R5
(connection rescaling redundancy and Wilson-coefficient routing).
Those claims **require unsupplied retained bridge theorems** (a
physical connection-equivalence relation and a Wilson plaquette
matching surface) and are therefore **out of scope** here. They are
recorded as companion observations in §"Companion observations (out
of scope)" below and do not bind on R1-R3 closure.

The theorem **does not** claim:

- that the *normalization scalar* of `B_HS` is itself uniquely forced
  (the convention layer for the overall scalar is the subject of
  the companion note,
  `G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md`);
- that the Wilson plaquette action form is uniquely forced (a separate
  retention target; this row does not use, and is not load-bearing on,
  any Wilson-action / `g_bare = 1`-definition content);
- closure of the deeper "absolute derivation of `g_bare = 1` from A1+A2"
  Nature-grade target.

## 2. What this candidate adds beyond the 2026-05-03 candidate

| Aspect | 2026-05-03 source surface | Present R1-R3 bounded candidate |
|---|---|---|
| Load-bearing input | canonical `Tr(T_a T_b) = δ/2` from `cl3_color_automorphism_theorem` | Hilbert–Schmidt form `B_HS` from framework Hilbert space + Killing rigidity |
| Conclusion type | algebraic substitution showing `c²` shift in `β` | structural rigidity statement: no `c` preserves both trace Gram AND Casimir |
| Independent content beyond parent | minimal (parent already implies it) | **adds Killing-form uniqueness + joint preservation impossibility** |
| Why not decoration | n/a | the joint trace-AND-Casimir rigidity is **not** a one-line consequence of `cl3_color_automorphism_theorem`; it requires the simplicity of su(3) + Killing rigidity |

The 2026-05-03 candidate gave a single-form rigidity statement (only the
trace Gram). The present candidate gives a **two-form** rigidity
statement (trace Gram **and** Casimir together): under the framework's
fixed Hilbert–Schmidt structure, no real `c ≠ ±1` preserves both
forms simultaneously. The Casimir-form preservation is the additional
rigidity check supplied by this narrowed source surface.

## 3. Declared source dependencies (one hop)

| Authority | Audit-lane status | Role |
|---|---|---|
| [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md) | retained_no_go | carries the physical lattice baseline used to treat the Hilbert-space inner product as fixed framework structure |
| [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md) | retained | provides the `Cl(3) -> End(V) -> su(3)` embedding (`M₃_sym ⊗ I₂` on the symmetric base, the realization of `g_conc = su(3) ⊂ End(C^8)`) and the Ad-invariant trace form on the triplet (`Tr[T^a T^b] = (1/2)δ^{ab}`, exact) |
| [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | retained | provides the graph-canonical `su(3)` closure on the taste cube (corroborating the embedding `Cl(3) -> su(3) ⊂ End(V)`) |

These two retained positive-theorems jointly supply the embedding (Claim 1)
and the Ad-invariant form identification (Claim 2) that the present
argument load-bears on; the dependency reroute below records why the
prior single citation to the now-terminally-demoted
`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md` is replaced.
The
present theorem's load-bearing path is via the **form** rather than
via the **basis-element values**.

The standard canonical-basis value `C_F = 4/3` is re-derived in §4
from `C_F = (8/3) N_F` at `N_F = 1/2`; `SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`
is an informational cross-reference, not a load-bearing dependency.

## 4. Load-bearing step (class A)

```text
Inputs:
  V = C^8 with fixed Hilbert-space inner product (axiom-level)
  g_conc = su(3) ⊂ End(V)  (embedding from cl3_color_automorphism_theorem / graph_first_su3_integration_note, both retained)
  B_HS(X, Y) = Tr_{V_3}(X Y)  for X, Y ∈ g_conc  (HS form)

Step 1 (Killing rigidity).
  su(3) is simple, so the space of Ad-invariant symmetric bilinear forms
  on su(3) is one-dimensional (classical Killing-form rigidity). Thus
  B_HS is the unique such form up to overall positive scalar k > 0.

Step 2 (Casimir form joint).
  Fix a B_HS-orthonormal basis {T_a} normalized so that
      B_HS(T_a, T_b) = N_F · δ_{ab}                       (NF)
  for some positive scalar N_F (the convention parameter — see Section 7).
  The quadratic Casimir
      C_F · I_3 = Σ_a T_a T_a                             (CF)
  is then determined by Schur + Tr_3 evaluation:
      Tr_3(C_F · I_3) = 3 C_F = Σ_a Tr_3(T_a T_a) = 8 N_F.
  So
      C_F = (8/3) N_F.                                    (CF1)
  In particular, at N_F = 1/2 (canonical Gell-Mann), C_F = 4/3.

Step 3 (Joint rescaling identity).
  Apply T_a → c T_a, c ∈ R \ {0}. Then:
      B_HS(c T_a, c T_b) = c² · N_F · δ_{ab}              (NF rescaled by c²)
      Σ_a (c T_a)(c T_a) = c² · C_F · I_3                 (CF rescaled by c²)

Step 4 (No nontrivial joint preservation).
  For c² ≠ 1 (i.e. c ≠ ±1), both invariants change by the same factor c².
  In particular, the canonical pair (N_F, C_F) = (1/2, 4/3) is preserved
  ONLY at c² = 1. The dilation T_a → c T_a with c ≠ ±1 is therefore NOT
  an automorphism of the canonical inner-product structure on g_conc.
  (Sign flip c = -1 reverses orientation but preserves both invariants;
  this is the discrete reflection ambiguity, not a continuous rescaling.)

[Steps 5-6 retired to "Companion observations (out of scope)" below.]
```

Steps 1-4 above are the **load-bearing chain** for R1-R3 and are
class (A) — algebraic identities on the framework's fixed
Hilbert-space structure plus standard Lie-algebra rigidity. They do
NOT use the Gell-Mann basis values as input; they use the *form*
directly.

## 5. Why this is not just the 2026-05-03 source surface

The 2026-05-03 candidate's load-bearing step was a single algebraic
substitution into the canonical Gell-Mann basis values already carried
by `cl3_color_automorphism_theorem`. The present theorem's
load-bearing step is structurally different: it uses **(i)** the
Hilbert–Schmidt form itself (independent of any basis choice),
**(ii)** Killing-form rigidity for simple Lie algebras (a classical
theorem, not from `cl3_color_automorphism_theorem`), and **(iii)** the joint
trace–Casimir rigidity (a *two-form* statement that is not a
consequence of the *one-form* canonical-basis statement).

In particular, the repaired core uses:

1. Simplicity of `su(3)` to make the Ad-invariant Hilbert-Schmidt form unique
   up to the overall scalar `N_F`.
2. Schur's lemma plus trace evaluation on the fundamental block:

   ```text
   sum_a T_a T_a = (8/3) N_F I_3.
   ```

   In the canonical witness `N_F = 1/2`, this gives `C_F = 4/3`.
3. A scalar dilation `T_a -> c T_a` sends both the trace Gram and quadratic
   Casimir by the same factor `c^2`. Therefore no real `c != +/-1` preserves
   the pair `(Tr(T_a T_b), sum_a T_a T_a)` simultaneously.

Equivalently, scalar dilation is not a continuous automorphism of the fixed
trace-Casimir structure.

## Non-Binding Former Claims

The previous source also included:

- a claim that connection rescaling is only coordinate redundancy on the same
  physical connection;
- a claim that Wilson small-`a` matching routes any non-canonical basis
  rescaling into the Wilson coefficient `beta`;
- downstream wording about this row closing an absolute or physical
  `g_bare = 1` derivation.

Those statements are not part of this row's binding claim. They require
separate retained-grade bridge theorems for physical connection equivalence,
the Wilson action surface, and matching/routing. This row must not be cited as
authority for those claims.

## Direct Dependencies

| Authority | Role |
|---|---|
| [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md) | supplies the framework Hilbert-space setting used by the row |
| [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md) | retained; supplies the concrete `Cl(3) -> End(V) -> su(3)` embedding (`M₃_sym ⊗ I₂`) and the exact Ad-invariant trace form `Tr[T^a T^b] = (1/2)δ^{ab}` on the triplet |
| [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md) | retained; corroborating graph-canonical `su(3)` closure on the taste cube |
| [`SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`](SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md) | companion Casimir value/context (decoration under the retained `cl3_color_automorphism_theorem`); this repaired note also recomputes the finite matrix identity directly |

The repaired claim does not need a physical Wilson matching premise.

## Verification

Run:

```bash
python3 scripts/frontier_g_bare_hs_rigidity_narrow.py
```

The runner verifies:

1. (R1) The Hilbert–Schmidt form `B_HS` on `g_conc ⊂ End(V_3)` is
   computed explicitly and shown to be Ad-invariant (numerical Ad
   action by random `SU(3)` group elements preserves the form).
2. (R2) The Casimir `C_F = (8/3) N_F` identity is checked for several
   basis normalizations `N_F ∈ {1/2, 1, 2, 1/4}` to confirm the
   uniqueness-up-to-scalar structure.
3. (R2 cont.) The joint rescaling identity (Step 3) is verified on
   `c ∈ {1/2, √2, 2, 3}` for both invariants simultaneously.
4. (R3) The "no joint preservation" claim (Step 4) is checked: at
   every `c ≠ ±1`, both the trace Gram **and** the Casimir change
   by `c²`, and the canonical pair is recovered ONLY at `c² = 1`.

The runner deliberately does not certify Wilson-coefficient routing,
physical connection equivalence, or an unconditional `g_bare = 1`
derivation.

## Companion observations (out of scope)

The following two statements were claimed as R4 and R5 in the earlier
draft. They require **unsupplied retained bridge theorems** and
therefore cannot be load-bearing on this row's R1-R3 algebraic core.
They are recorded here as companion observations for future-work
tracking, **not** as theorem-grade content.

**(Companion C4 — was R4) Connection rescaling reduces to coordinate
redundancy.** The rescaling `A → c A` of an arbitrary connection
`A_op = Σ_a A^a T_a` is the substitution `A^a → c A^a` of
coefficients. With the operator basis `{T_a}` pinned by R3, the
connection `A_op` itself does not change under this substitution
unless we *also* dilate the generators (forbidden by R3).

**Required-but-unsupplied bridge for C4 to become load-bearing:**
a retained **physical connection-equivalence relation** identifying
the lattice connection on the framework Hilbert space with `A_op` as
above, in a sense that lets R3 propagate from generator basis to the
physical connection variables. The trace-Casimir rigidity does not
by itself derive this connection-equivalence; it must come from a
separate retained authority on the physical connection variables.

**(Companion C5 — was R5) Wilson-coefficient routing.** Under a
*non-canonical* basis with `T_a → c T_a`, the Wilson plaquette
small-`a` matching gives `β_new = c² · β_old`, leaving `g_bare`
unchanged.

**Required-but-unsupplied bridge for C5 to become load-bearing:**
a retained **Wilson plaquette action routing theorem** deriving the
small-`a` matching surface (Wilson plaquette action form, fixed
continuum kinetic term, matching prescription) from retained inputs,
so the `β = c² β` reading is more than a textbook reading of a
specific action form. The runner's numerical verification of
`β_new = c² β_old` is consistent with this reading but does not
constitute the retained Wilson-action-routing bridge.

Until those two bridges land as retained authorities, downstream
consumers must not cite this row for R4-type connection-equivalence
or R5-type Wilson-action-routing claims; only the R1-R3 bounded
algebraic core is in load-bearing scope.

Expected certificate:

```text
SUMMARY: PASS=38 FAIL=0
RUNNER STATUS: PASS
```

## Remaining convention layer

The present theorem proves rigidity up to overall scalar — what
remains a convention is the *choice* of `N_F` (equivalently `k`).
Standard physics conventions are:

| Convention | `N_F` | `C_F` | Source |
|---|---|---|---|
| Canonical Gell-Mann | `1/2` | `4/3` | particle-physics standard |
| Fundamental Killing | dimension-determined | `1` | mathematical Killing-form |
| Adjoint-trace | varies | `N_c` | gauge-theory adjoint trace |

The framework adopts the canonical Gell-Mann normalization
`N_F = 1/2`. This is a single convention scalar, not an independent
`g_bare` choice. Its convention status is documented in the companion
note
`G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md`,
which makes precise that `g_bare = 1` is a *derived constraint* given
`N_F = 1/2` and is **not** a separate convention.

## 8. Review-lane disposition (audit queued)

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Under the framework's fixed Hilbert-space inner product on the canonical
  triplet block inside V = C^8, the Hilbert-Schmidt form on
  g_conc = su(3) is the unique
  Ad-invariant inner product (Killing rigidity); no real c ≠ ±1
  preserves both the trace Gram and the quadratic Casimir
  simultaneously. The connection-rescaling and Wilson-coefficient
  routing observations (former R4/R5) are explicitly out of scope
  pending retained bridge theorems; until those bridges land the
  R1-R3 trace-Casimir rigidity is the load-bearing content. The
  earlier R4/R5 prose is preserved in the Companion-observations
  section as future-work tracking, not load-bearing claims.
historical_proposed_claim_scope_below_retired: |
  Earlier (positive_theorem) draft additionally claimed the
  connection rescaling A → c A reduces to coordinate redundancy on
  the same operator A_op and under any non-canonical basis the
  Wilson small-a matching routes the rescaling
  into β = c² · β, leaving g_bare unchanged.
proposed_load_bearing_step_class: A
declared_one_hop_deps:
  - physical_lattice_necessity_note
  - cl3_color_automorphism_theorem
  - graph_first_su3_integration_note
dependency_reroute_2026-06-06: |
  Load-bearing dependency repointed from
  g_bare_structural_normalization_theorem_note_2026-04-18 (now
  effective_status=audited_renaming, terminal: demoted for defining
  rather than deriving the Wilson-action g=1, content this row does NOT
  use) to the retained cl3_color_automorphism_theorem (Cl(3)->End(V)->su(3)
  embedding M3_sym (x) I2 + exact Ad-invariant trace form
  Tr[T^a T^b]=(1/2)delta) and graph_first_su3_integration_note
  (graph-canonical su(3) closure). R1-R3 only load-bear on Claims 1 and 2
  (embedding + Ad-form), both of which are exact structural support in the
  demoted note and are independently supplied by these retained rows.
independent_audit_required_before_effective_status_change: true
parent_update_allowed_only_after_independent_audit_accepts_child_rows: true
distinguishing_content_from_2026-05-03: |
  The 2026-05-03 candidate's load-bearing step was a single algebraic
  substitution into the canonical Gell-Mann basis (one-form rigidity).
  The present candidate's load-bearing step is the joint trace-AND-
  Casimir rigidity under the form itself (two-form rigidity), using
  Killing-form uniqueness on the simple Lie algebra su(3). This is
  not a decoration: the joint statement is not a one-line consequence
  of cl3_color_automorphism_theorem.
```

## Audit Boundary

This repair is a queue-ready scope repair, not an audit verdict. It adds no
new axiom, Wilson matching convention, physical selector, fitted value, or
package-wide `g_bare` promotion.

## 10. What this theorem does NOT close

- The convention-vs-derivation status of the **overall scalar** `N_F`
  (the canonical normalization choice). This remains the genuine
  remaining convention layer; see the companion restatement note.
- The choice of the Wilson plaquette action form per se; Symanzik /
  improved actions remain outside this scope.
- The deeper question of whether `N_F = 1/2` is itself uniquely forced
  by Cl(3) algebraic structure alone — a separate Nature-grade target.

## 11. Cross-references

- `G_BARE_DERIVATION_NOTE.md` — parent
  note that may cite this candidate as the strengthened rescaling-
  removal closure after independent audit acceptance.
- `G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`
  — the 2026-05-03 candidate that the present theorem strengthens.
- `G_BARE_RIGIDITY_THEOREM_NOTE.md`
  — sister Hamiltonian-level rigidity argument; the present theorem
  is its trace–form-explicit packaging on the Wilson-action surface.
- `G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`
  — former one-hop dep for the embedding (Claim 1) and Ad-form (Claim 2);
  **superseded by the 2026-06-06 reroute** to the retained
  [`CL3_COLOR_AUTOMORPHISM_THEOREM.md`](CL3_COLOR_AUTOMORPHISM_THEOREM.md) and
  [`GRAPH_FIRST_SU3_INTEGRATION_NOTE.md`](GRAPH_FIRST_SU3_INTEGRATION_NOTE.md)
  (plain-text reference here, intentionally not a load-bearing link).
- `SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`
  — informational cross-reference for the canonical-basis Casimir
  value. The value is re-derived in §4 for this row, so this file is
  not a load-bearing dependency.
- `G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md`
  — companion note that uses the present rigidity to disambiguate the
  convention layer (overall `N_F` scalar) from the constraint layer
  (`g_bare = 1`).
## 12. Honest scoping summary

The novelty of the present theorem over the 2026-05-03 candidate is
the **joint two-form rigidity** (R1-R3): under the framework's fixed
Hilbert–Schmidt form, no scalar dilation `T_a → c T_a` with `c ≠ ±1`
preserves both the trace Gram and the quadratic Casimir
simultaneously. Killing-form rigidity (uniqueness of the Ad-invariant
form on simple `su(3)` up to scalar) is the additional structural
input that lifts the argument out of the decoration tier.

The connection-equivalence and Wilson-action-routing readings (former
R4/R5) are explicitly **out of scope** pending retained bridge
theorems — they appear as companion observations only. The R1-R3
algebraic core is the load-bearing content; nothing in the present
row by itself derives the Wilson action form, the small-`a` matching
surface, or the absolute `g_bare = 1` reading from R1-R3 alone.

The remaining convention layer is the **overall scalar `N_F`** that
sets the normalization of the Hilbert–Schmidt form. Once `N_F = 1/2`
is admitted as the canonical Gell-Mann convention, `g_bare = 1`
follows as a structural constraint **conditional on** the
out-of-scope Wilson-action-routing bridge becoming retained. The
deeper question — whether `N_F = 1/2` itself is forced by Cl(3)
alone — is separately tracked as a Nature-grade target.
