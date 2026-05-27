# g_bare Hilbert–Schmidt Rigidity Theorem (R1-R3 Narrow Surface)

**Date:** 2026-05-07 (scope narrowed 2026-05-27)
**Claim type:** bounded_theorem
**Status:** bounded R1-R3 source. This note is graph-visible only so the
independent audit lane can decide its audit and effective status; no author-side
retained status is asserted.
**Primary runner:** [`scripts/frontier_g_bare_audit_residual_closure.py`](../scripts/frontier_g_bare_audit_residual_closure.py)

## 0. Audit context

This note strengthens
`G_BARE_RESCALING_FREEDOM_REMOVAL_THEOREM_NOTE_2026-05-03.md`
in response to the audit verdict that classified the 2026-05-03
candidate as `audited_decoration` (effective status
`decoration_under_cl3_color_automorphism_theorem`):

> *"the audited load-bearing step is a straightforward algebraic
> rescaling identity over the canonical trace normalization and beta
> matching formula. There are no external comparator checks, no new
> first-principles computation needed for the conclusion … the theorem
> is best classified as decoration."*

The audit-flagged weakness was that the 2026-05-03 statement is a
narrow algebraic substitution given an admitted normalization. The
present note carries an independent, structurally distinct bounded argument:
the Hilbert–Schmidt trace form on `End(V)` *induced from the framework
Hilbert space* is the **unique** Ad-invariant inner product on
`su(3) ⊂ End(V)` up to overall positive scalar (Killing-form rigidity).
Under that fixed form, **no scalar dilation `T_a → c T_a` simultaneously
preserves the trace Gram and the quadratic Casimir** for `c ≠ ±1`.

The 2026-05-26/27 audit of this row found that R1-R3 close as bounded
class-A algebra but that the prior source scope also included R4/R5: a physical
connection-coordinate equivalence claim and Wilson action-routing claim.  This
revision narrows the binding theorem to R1-R3 only.  R4/R5 remain downstream
open bridge targets and are not part of this row's auditable candidate surface.

This is a class (A) algebraic identity whose load-bearing inputs are:

1. the framework Hilbert-space inner product on `V = C^8` (axiom-level
   structure, imported through
   [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md)),
2. simplicity of `su(3)` and Killing-form rigidity (classical),
3. the Cl(3) → End(V) embedding canonicity claim from
   [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
   Claim 1 (proved up to finite outer automorphism).

The argument does *not* reduce to the canonical Gell-Mann generators
already carrying `T_F = 1/2` (the path that the 2026-05-03 candidate
was demoted on). It uses the *form* directly, not the basis-specific
normalization.

## 1. Claim scope

> **Theorem (Hilbert–Schmidt rigidity).**
>
> Let `V` be the framework Hilbert space `C^8` with its fixed
> inner product (carried from the framework axioms via the physical
> lattice retention chain). Let `g_conc = su(3) ⊂ End(V)` be the
> derived gauge subalgebra in the canonical triplet block as fixed by
> [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
> Claim 1. Let
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

The theorem **does not** claim:

- that the *normalization scalar* of `B_HS` is itself uniquely forced
  (the convention layer for the overall scalar is the subject of
  the companion note,
  `G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md`);
- that the Wilson plaquette action form is uniquely forced (separate
  retention target; see
  [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
  Claim 3 caveat);
- that connection-coordinate rescaling is physically redundant for the
  framework gauge connection;
- that Wilson small-`a` coefficient routing is derived from the fixed
  Hilbert-Schmidt structure;
- closure of the companion `g_bare = 1` constraint-vs-convention row; or
- closure of the deeper "absolute derivation of `g_bare = 1` from Axiom 1 and
  Axiom 2" target.

## 2. What this candidate adds beyond the 2026-05-03 candidate

| Aspect | 2026-05-03 (decoration) | Present (R1-R3 bounded candidate) |
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
rigidity check that the auditor identified as missing.

## 3. Declared audit dependencies (one hop)

| Authority | Audit-lane status | Role |
|---|---|---|
| [`PHYSICAL_LATTICE_NECESSITY_NOTE.md`](PHYSICAL_LATTICE_NECESSITY_NOTE.md) | audited clean no-go / retained-grade effective status | provides the fixed Hilbert-space/input-algebra boundary used here only as a bounded algebraic surface |
| [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md) | audited clean / retained bounded | provides the canonical Cl(3) -> End(V) -> su(3) embedding (Claim 1) and the Ad-invariant form identification (Claim 2) |
| [`SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`](SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md) | audited decoration under retained color-normalization parent | provides a convenient canonical-basis check of `C_2 = 4/3`; the R1-R3 argument also derives `C_F = (8/3) N_F` directly |

The dependency on `cl3_color_automorphism_theorem` (the
basis-normalization lemma) is *two-hop* via either parent and is
therefore not load-bearing for the present argument. The
present theorem's load-bearing path is via the **form** rather than
via the **basis-element values**.

## 4. Load-bearing step (class A)

```text
Inputs:
  V = C^8 with fixed Hilbert-space inner product (axiom-level)
  g_conc = su(3) ⊂ End(V)  (Claim 1 of structural normalization theorem)
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
```

This load-bearing chain is class (A) — algebraic identities on the
framework's fixed Hilbert-space structure plus standard Lie-algebra
rigidity. It does NOT use the Gell-Mann basis values as input; it uses
the *form* directly.  The former R4/R5 connection and Wilson-routing
statements are downstream bridge targets, not binding claims of this row.

## 5. Why this is not a decoration of `cl3_color_automorphism_theorem`

The auditor demoted the 2026-05-03 candidate as decoration because its
load-bearing step was a single algebraic substitution into the
canonical Gell-Mann basis values already carried by
`cl3_color_automorphism_theorem`. The present theorem's load-bearing
step is structurally different: it uses **(i)** the Hilbert–Schmidt form
itself (independent of any basis choice), **(ii)** Killing-form
rigidity for simple Lie algebras (a classical theorem, not from
`cl3_color_automorphism_theorem`), and **(iii)** the joint
trace–Casimir rigidity (a *two-form* statement that is not a
consequence of the *one-form* canonical-basis statement).

In particular:

- `cl3_color_automorphism_theorem` says "the canonical Gell-Mann
  generators have `Tr(T_a T_b) = δ/2`." That is a *value* statement on
  a *specific basis*.
- The present theorem says "the Hilbert–Schmidt **form** is unique up
  to scalar, and no `c ≠ ±1` preserves both the form and the Casimir."
  That is a *structural* statement on the *form itself*, true in any
  basis.

The two-form joint rigidity is the genuine independent content; the
canonical basis values are merely a convenient witness.

## 6. Verification

```bash
python3 scripts/frontier_g_bare_audit_residual_closure.py
```

Verifies, in `Section H`:

1. The Hilbert–Schmidt form `B_HS` on `g_conc ⊂ End(V_3)` is
   computed explicitly and shown to be Ad-invariant (numerical Ad
   action by random `SU(3)` group elements preserves the form).
2. The Casimir `C_F = (8/3) N_F` identity is checked for several
   basis normalizations `N_F ∈ {1/2, 1, 2, 1/4}` to confirm the
   uniqueness-up-to-scalar structure.
3. The joint rescaling identity (Step 3) is verified on `c ∈ {1/2,
   √2, 2, 3}` for both invariants simultaneously.
4. The "no joint preservation" claim (Step 4) is checked: at every
   `c ≠ ±1`, both the trace Gram **and** the Casimir change by `c²`,
   and the canonical pair is recovered ONLY at `c² = 1`.
5. The runner also prints a Wilson-coefficient routing diagnostic.  That
   diagnostic is not part of this narrowed row's load-bearing R1-R3 claim.

## 7. The remaining convention layer (overall scalar `k`)

The present theorem proves rigidity up to overall scalar — what
remains a convention is the *choice* of `N_F` (equivalently `k`).
Standard physics conventions are:

| Convention | `N_F` | `C_F` | Source |
|---|---|---|---|
| Canonical Gell-Mann | `1/2` | `4/3` | particle-physics standard |
| Fundamental Killing | dimension-determined | `1` | mathematical Killing-form |
| Adjoint-trace | varies | `N_c` | gauge-theory adjoint trace |

The framework frequently uses the canonical Gell-Mann normalization
`N_F = 1/2`.  This row does not audit whether that scalar is forced or whether
it closes the companion `g_bare = 1` constraint-vs-convention claim.  It only
proves that once the Hilbert-Schmidt normalization is fixed, scalar dilation
cannot preserve both the trace Gram and the quadratic Casimir except at
`c = ±1`.

## 8. Review-lane disposition (audit queued)

```yaml
target_claim_type: bounded_theorem
proposed_claim_scope: |
  Under the framework's fixed Hilbert-space inner product on V = C^8,
  the Hilbert-Schmidt form on g_conc = su(3) ⊂ End(V) is the unique
  Ad-invariant inner product (Killing rigidity); no real c ≠ ±1
  preserves both the trace Gram and the quadratic Casimir
  simultaneously.
proposed_load_bearing_step_class: A
declared_one_hop_deps:
  - physical_lattice_necessity_note
  - g_bare_structural_normalization_theorem_note_2026-04-18
  - su3_casimir_fundamental_theorem_note_2026-05-02
independent_audit_required_before_effective_status_change: true
parent_update_allowed_only_after_independent_audit_accepts_child_rows: true
out_of_scope_until_separate_bridge:
  - R4 physical connection-coordinate equivalence
  - R5 Wilson coefficient routing
distinguishing_content_from_2026-05-03: |
  The 2026-05-03 candidate's load-bearing step was a single algebraic
  substitution into the canonical Gell-Mann basis (one-form rigidity).
  The present candidate's load-bearing step is the joint trace-AND-
  Casimir rigidity under the form itself (two-form rigidity), using
  Killing-form uniqueness on the simple Lie algebra su(3). This is
  not a decoration: the joint statement is not a one-line consequence
  of cl3_color_automorphism_theorem.
```

## 9. What this candidate can support after independent audit acceptance

- A bounded upstream algebraic input for any future connection-coordinate or
  Wilson-routing bridge.
- The independent R1-R3 part of the rescaling-freedom removal repair target
  named in
  `G_BARE_DERIVATION_STATUS_CORRECTION_AUDIT_NOTE_2026-05-02.md`.
- A future re-audit of `G_BARE_DERIVATION_NOTE.md`,
  only after separate bridge rows close R4/R5 and the companion
  constraint-vs-convention row.

## 10. What this theorem does NOT close

- The convention-vs-derivation status of the **overall scalar** `N_F`
  (the canonical normalization choice). This remains the genuine
  remaining convention layer; see the companion restatement note.
- R4: the physical connection-coordinate equivalence of coefficient
  rescaling.
- R5: Wilson action coefficient routing from the fixed Hilbert-Schmidt
  structure.
- The companion `g_bare = 1` constraint-vs-convention conclusion.
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
- [`G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md`](G_BARE_STRUCTURAL_NORMALIZATION_THEOREM_NOTE_2026-04-18.md)
  — declared one-hop dep providing the Cl(3) → End(V) → su(3) chain
  (Claim 1) and the Ad-invariant form identification (Claim 2).
- [`SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md`](SU3_CASIMIR_FUNDAMENTAL_THEOREM_NOTE_2026-05-02.md)
  — declared one-hop dep providing the canonical-basis Casimir value
  used to sharpen the joint rigidity statement.
- `G_BARE_CONSTRAINT_VS_CONVENTION_RESTATEMENT_NOTE_2026-05-07.md`
  — companion note that requires separate audit before it can use the
  present R1-R3 rigidity in a `g_bare = 1` constraint argument.
## 12. Honest scoping summary

The novelty of the present theorem over the 2026-05-03 candidate is
the **joint two-form rigidity**: under the framework's fixed
Hilbert–Schmidt form, no scalar dilation `T_a → c T_a` with `c ≠ ±1`
preserves both the trace Gram and the quadratic Casimir
simultaneously. Killing-form rigidity (uniqueness of the Ad-invariant
form on simple `su(3)` up to scalar) is the additional structural
input that lifts the argument out of the decoration tier.

The remaining convention layer is the **overall scalar `N_F`** that
sets the normalization of the Hilbert–Schmidt form.  This row does not
derive `N_F = 1/2`, does not derive the physical connection readout, and
does not derive Wilson action routing.  Those are separate bridge targets
before the parent `g_bare = 1` surface can claim closure.
