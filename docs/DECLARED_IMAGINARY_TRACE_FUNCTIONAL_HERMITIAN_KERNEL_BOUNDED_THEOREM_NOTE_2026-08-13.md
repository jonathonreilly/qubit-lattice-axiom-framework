---
claim_id: declared_imaginary_trace_functional_hermitian_kernel_bounded_theorem_note_2026-08-13
claim_type: bounded_theorem
claim_scope: "For the separately declared real-linear functional J(C)=Im Tr(C)/2 on M_2(C), every Hermitian matrix lies in ker J, so no Hermitian encoding f(u) can satisfy J(f(u))=u on a set containing a nonzero u. The central anti-Hermitian family A(u)=iu 1 obeys J(A(u))=u exactly. This is finite linear algebra conditional on the declared J and Hermitian restriction; it supplies no Record scalar, physical readout, formation rule, or ancilla compiler."
upstream_dependencies:
  - minimal_axioms
runner: scripts/declared_imaginary_trace_functional_hermitian_kernel_2026_08_13.py
---

# Declared Imaginary-Trace Functional: Hermitian Kernel And Anti-Hermitian Encoding

**Date:** 2026-08-13
**Type:** bounded_theorem
**Scope:** exact one-site linear algebra on `M_2(C)`, conditional on the
separately declared functional `J(C)=Im Tr(C)/2` and on a Hermitian content
restriction.
**Audit-status authority:** independent audit lane only. This note authors no
audit verdict and predicts none.
**Primary runner:**
[`scripts/declared_imaginary_trace_functional_hermitian_kernel_2026_08_13.py`](../scripts/declared_imaginary_trace_functional_hermitian_kernel_2026_08_13.py)

## Result Up Front

Let `H_2` be the real vector space of Hermitian `2x2` matrices and declare

`J(C)=Im Tr(C)/2`, for `C in M_2(C)`.

Then:

1. `H_2` is contained in `ker J`.
2. Consequently, if `U` contains a nonzero real number, there is no map
   `f:U -> H_2` satisfying `J(f(u))=u` for every `u in U`.
3. The central anti-Hermitian family `A(u)=i u 1` obeys `J(A(u))=u` for every
   real `u`, and `A(u)` is non-Hermitian whenever `u != 0`.

The negative boundary is therefore exact but deliberately narrow: it concerns
one declared functional on Hermitian matrices. It is not a no-go for other
functionals, an enlarged content space, a supplied second argument, a
multi-site encoding, or a dynamical registration process.

## Current Framework Boundary

The current Qubit axiom in
[`MINIMAL_AXIOMS_2026-06-29.md`](MINIMAL_AXIOMS_2026-06-29.md) supplies the
full one-site possibility domain with algebraic presentation `M_2(C)`. Its
current Record section says that records form; when present, a record locks one
admissible local possibility; only records are readable; readout is determined
by record content alone; and a site with no record cannot be read.

The current Record section does **not** supply a named scalar functional,
finite additivity, or a scalar value for absence. In particular, it does not
supply `J`. The functional above and the Hermitian restriction are explicit
conditions of this bounded theorem. The theorem neither restores the retired
scalar premise nor treats the zero matrix as an empty record.

## Exact Objects

Write a Hermitian matrix as

`H=((p, q+i r),(q-i r, s))`, with `p,q,r,s in R`.

Its trace is `p+s`, hence real. The density body

`D={rho in M_2(C): rho=rho^dagger, rho>=0, Tr(rho)=1}`

is a subset of `H_2`. The declared functional `J` is real-linear on all of
`M_2(C)`, but its restriction to `H_2` is the zero functional.

The identity matrix is denoted by `1`. For real `u`, set

`A(u)=i u 1`.

Then `Tr(A(u))=2iu`, so `J(A(u))=u`. Moreover
`A(u)^dagger=-A(u)`, and therefore `A(u)` is Hermitian only at `u=0`.

## Theorem 1 — Hermitian Kernel

**Claim.** `H_2` is contained in `ker J`.

**Proof.** If `H=H^dagger`, the diagonal entries of `H` are real. Therefore
`Tr(H)` is real and

`J(H)=Im Tr(H)/2=0`.

Equivalently, the real Pauli basis `{1,sigma_x,sigma_y,sigma_z}` spans `H_2`,
and `J` vanishes on all four basis elements. This proves the universal
statement, not merely the finite samples printed by the runner. `QED`

## Corollary — No Hermitian Encoding For This Functional

**Claim.** If a set `U subset R` contains a nonzero value, no map
`f:U -> H_2` can satisfy `J(f(u))=u` for all `u in U`.

**Proof.** Theorem 1 gives `J(f(u))=0` for every `u in U`. At any nonzero
`u`, this contradicts `J(f(u))=u`. No regularity, linearity, injectivity, or
continuity assumption on `f` is needed. `QED`

This statement does not say that Hermitian matrices cannot encode a real
number for a different readout. For example, `u 1` is Hermitian and
`Re Tr(u 1)/2=u`. Changing the functional changes the theorem's premise.

## Theorem 2 — Exact Anti-Hermitian Escape

**Claim.** The map `A(u)=iu 1` satisfies `J(A(u))=u` for every real `u`, is
injective, and leaves the Hermitian subspace away from zero.

**Proof.** Directly,

`Tr(iu 1)=2iu`, and hence `J(iu 1)=u`.

Distinct real values give distinct matrices. Also
`(iu 1)^dagger=-iu 1`, which equals `iu 1` exactly when `u=0`. `QED`

More generally, for every Hermitian `H`,

`J(H+iu 1)=u`.

Thus the full `M_2(C)` domain contains an explicit formal escape. Nothing here
selects that escape as record content or supplies a process that writes it.

## Pairing Discriminator

The declared one-argument functional `J(rho)` must not be confused with a
two-argument trace pairing. Let

`rho_*=1/2`, `rho_{3/5}=diag(3/5,2/5)`, and `E_0=diag(1/2,0)`.

Then

`J(rho_*)=J(rho_{3/5})=0`,

while exact multiplication gives

`Tr(rho_* E_0)=1/4`, and `Tr(rho_{3/5} E_0)=3/10`.

The pairing varies because it has a supplied second argument. This comparison
is algebraic only. It does not identify the pairing with a physical Record
readout or derive a probability rule.

## Exact Target And Proof Obligations

**Exact target:** characterize the Hermitian restriction and one explicit
non-Hermitian right inverse of the separately declared functional `J`.

| Obligation | Disposition |
|---|---|
| pin the current one-site domain and Record boundary | linked current axiom memo |
| prove `J(H)=0` for every `H in H_2` | real trace, closed |
| exclude every map `f:U -> H_2` with `J(f(u))=u` at nonzero `u` | direct corollary, closed |
| exhibit a right inverse in the full `M_2(C)` domain | `A(u)=iu 1`, closed |
| distinguish `J(rho)` from `Tr(rho E)` | exact `1/4` and `3/10` controls, closed |
| derive `J` as a Record scalar | not claimed; open outside this theorem |
| derive a physical writing or formation process | not claimed; open outside this theorem |

The proof-obligation graph is acyclic. The mathematical leaves are elementary
trace and adjoint identities. The physical compiler is not a terminal lemma of
this theorem; it is explicitly outside the target.

## No-Go Discipline Gate

The corollary is a narrow derived negative boundary, so N1-N8 is recorded even
though the proof is universal within its two declared conditions.

### N1 — Alternative routes

| Route family | Attempt against the negative boundary | Result | Marker |
|---|---|---|---|
| arbitrary Hermitian encoding | choose any, including nonlinear or discontinuous, `f:U -> H_2` | closed by `H_2 subset ker J`; no regularity assumption is used | ATTEMPTED |
| alternative one-argument functional | replace `J` by `K(H)=Re Tr(H)/2` | live escape, but changes the declared functional; `K(u1)=u` | ATTEMPTED |
| supplied-effect pairing | use `K_E(rho)=Tr(rho E)` | live escape, but introduces a second argument and a different functional | ATTEMPTED |
| non-Hermitian one-site encoding | use `A(u)=iu1` in full `M_2(C)` | live explicit escape, but violates the Hermitian restriction | ATTEMPTED |
| enlarged product content | adjoin `[0,1]` as a separate content coordinate | live formal escape, but changes the content domain and readout map | ATTEMPTED |
| multi-site or dynamical encoding | store `u` in correlations, histories, or a writing process | live untested physical route, outside the one-site static theorem | ATTEMPTED |

There are six materially distinct object/mechanism families. Only the first is
excluded by the theorem; the other five are named live routes. The note makes
no universal physical no-go claim.

### N2 — Condition independence

The collapsed condition set is `{declared J, Hermitian codomain}`.

| Pair | Removing first closes second? | Removing second closes first? | Independent? |
|---|---:|---:|---:|
| declared `J` / Hermitian codomain | no | no | yes |

Changing `J` permits a Hermitian encoding; enlarging the codomain permits the
displayed `J` encoding. Neither condition follows from the other.

### N3 — Hidden-condition scan

- `declared`: load-bearing and explicit; `J` is not attributed to Record.
- `current framework`: load-bearing only for the one-site `M_2(C)` domain and
  the no-scalar Record boundary, both linked above.
- Hermitian restriction: load-bearing and explicit in the scope, theorem, and
  machine trace.
- No phrase such as “by construction”, “naturally”, “obviously”, or “standard
  QFT” supplies an additional premise.

No hidden condition was found.

### N4 — Residual matching

No prior no-go is cited as evidence. The only load-bearing external link is
the current minimal-axiom memo, used for the `M_2(C)` domain and to state that
Record supplies no scalar functional. The algebraic negative is proved here,
so there is no borrowed residual to mismatch.

### N5 — Resolution audit

| Resolution | Executed? | Exact scope |
|---|---:|---|
| per element | yes | universal `H in H_2`, plus exact sampled mutations |
| per site | yes | one-site `M_2(C)` statement |
| per mode | not applicable | no spectral or modal decomposition is claimed |
| per block | yes | Hermitian subspace versus central anti-Hermitian line |
| lattice-wide | no | no lattice history, process, or global no-go is claimed |

The runner cache carries the matching five-line execution certificate.

### N6 — Partial-closure paths

Five live extensions are already exposed: choose another functional, supply an
effect, permit non-Hermitian content, enlarge the content domain, or construct
a multi-site/dynamical encoder. None is dismissed as requiring a new axiom.
Each needs its own supplied or derived map before it can become a physical
readout statement.

### N7 — Steelman

The strongest objection to a broader no-go is decisive: the Qubit domain is
the full `M_2(C)` algebra, not the Hermitian body, and `A(u)=iu1` is already a
right inverse of `J`. Moreover Record does not select `J` or require Hermitian
content. Therefore the algebra cannot support a claim that the framework
forbids a unit-interval encoding. This objection is why the theorem is limited
to the separately declared `J` and Hermitian codomain.

### N8 — Cross-cycle echo

The repo search found two directly relevant prior shapes. The current minimal
axiom reset removed scalar `I`/additivity/absence-value semantics, showing that
a former “framework-provided scalar” wall can disappear through premise
correction. The recently landed formation-extension theorem shows that content
constraints do not themselves supply a formation process. Both mechanisms are
applied here: no retired scalar is inherited, and no static algebra is promoted
to a physical formation or compiler statement. Older notes that still quote
the retired scalar are historical consumers, not authority for this theorem.

**No-Go Discipline status:** PASS for the narrow algebraic corollary. It does
not pass, and the note does not ship, a framework-wide or physical compiler
no-go.

## Machine Status And Trace

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
claim_type_reason: "The kernel and right-inverse statements are exact, conditional on a separately declared functional and Hermitian codomain; no physical Record readout or compiler is derived."
trace_class: negative_route_pruning
target_claim_id: declared_imaginary_trace_functional_hermitian_kernel
target_blocker_text: "determine what a separately declared imaginary-trace functional can read on Hermitian one-site matrices"
source_of_blocker_text: branch_submission_repaired_after_record_premise_reset
reachability_to_target: advances
artifact_role: theorem
conditional_surface_status: "exact finite linear algebra; physical readout and writing process remain open"
hypothetical_axiom_status: "no edit"
admitted_observation_status: null
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports And Claim Boundary

| Item | Role | Status |
|---|---|---|
| current `M_2(C)` one-site domain | framework premise | current minimal-axiom link |
| `J(C)=Im Tr(C)/2` | declared mathematical input | explicit condition; not a Record scalar |
| Hermitian codomain | declared mathematical input | explicit condition |
| trace and adjoint identities | proof | elementary exact algebra |
| `A(u)=iu1` | constructed witness | exact formal escape |
| `Tr(rho E)` examples | discriminator | exact two-argument algebra only |
| physical readout, writing process, formation site/rate | residual | open and not claimed |

No observational, fitted, measured, or literature value is used. Independent
audit remains required before any effective status may change.
