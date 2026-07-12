# No-Go Discipline Checklist

**Status:** `PASS`

**Negative assertion under test:** only the narrow statement that the current
Lattice, Qubit, Admissibility, and Record surface, even after granting the
named invariant `hw=1` character carrier, does not select the unit-normalized
pair `(D_act,D_pass)=(I_3,I_3)`.

The source theorem does not say that `I_3` is impossible, that every PMNS
operator is scalar, that no carrier theorem can be found, or that all PMNS
routes fail.

## N1 — Alternative route enumeration

| Route | What it attempts | Result and authority | Marker |
|---|---|---|---|
| Projector-resolution route | Obtain the carrier from `sum_i P_i X P_i` | The exact family is `sum_i P_i(alpha I_3)P_i=alpha I_3`; choosing `X=I_3` inserts the desired value. Verified by the revised runner and note §3. | `ATTEMPTED` |
| Joint-commutant route | Use all `hw=1` translations plus the supplied proper-cubic cycle | The full joint commutant is `C I_3`; it fixes scalar shape but not `alpha=1`. Verified by direct component proof, numerical nullspace rank, and independent SymPy solve. | `ATTEMPTED` |
| One-site Clifford route | Use Pauli/`Cl(3,0)` normalization to fix the `3 x 3` taste carrier | The local algebra and taste carrier have different types; [`MINIMAL_AXIOMS_2026-06-29.md`](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md) supplies no map from the former to a sector operator. The runner instantiates both and no such map is assumed. | `ATTEMPTED` |
| Admissibility route | Read the nearest-neighbor availability rule as a transfer/kinetic selector | The axiom source explicitly says Admissibility is not dynamics and chooses no Hamiltonian or transfer operator (lines 103--118). The runner also constructs a covariant varying admissibility rule held fixed across two different carrier expansions. | `ATTEMPTED` |
| Record/readout route | Use permanent records and finite additivity to normalize the carrier | Record constrains locking/readout, while source/action and physical-observable identification remain outside the axioms (axiom memo lines 128--134 and 156--173). The same record/readout model supports both carrier normalizations. | `ATTEMPTED` |
| Approved-primitive route | Use scale, kinetic isotropy, or realized-state registration to fix the unit | The [`PRIMITIVE_REGISTRY_CHECK`](../../../../docs/ai_methodology/skills/PRIMITIVE_REGISTRY_CHECK.md) shows these supply only units conversion, kinetic-form isotropy, and a pointwise state slot respectively; none supplies a PMNS carrier, selector, or dimensionless normalization. | `ATTEMPTED` |
| Existing PMNS authority route | Reuse an already audited carrier theorem | Repository search found only finite carrier/commutant and conditional response-interface results. The [`PMNS oriented-cycle note`](../../../../docs/PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md) explicitly excludes the physical carrier and primitive derivation; no matching normalization authority exists. | `ATTEMPTED` |

Seven distinct routes were tested. None refutes the conditional unit-seed
calculation; all fail only as derivations of the unit normalization from the
named premise surface.

## N2 — Wall-independence audit

The helper/closure-stack issue is removed: the revised runner imports no PMNS
helper and proves the finite support result directly. The response formulas
and support classifier are disclosed theorem definitions, not claimed axiom
outputs. Three distinct walls remain for a positive derivation of the exact
unit pair:

- `W_C` — carrier construction/type: no current-premise map creates
  `D_act,D_pass` and assigns their transformation type;
- `W_N` — normalization: even after a carrier exists and is restricted to the
  invariant scalar family, no current-premise theorem fixes both scalars to
  one;
- `W_X` — sector relation: no current-premise exchange/same-construction
  theorem equates the active and passive scalars.

| Pair | Closing first automatically closes second? | Closing second automatically closes first? | Independent? |
|---|---|---|---|
| `W_C`,`W_N` | no — a carrier map can leave its trace/scale free | no — a conditional trace/unit theorem need not construct a carrier | yes |
| `W_C`,`W_X` | no — two constructed sectors need not be exchanged | no — a conditional exchange statement need not construct either sector | yes |
| `W_N`,`W_X` | no — separately normalized sectors need not be related | no — equal scalars need not equal one | yes |

Translation/`C_3` invariance and nonsingular resolvents are explicit
hypotheses delimiting the positive scalar-family theorem, not additional walls
hidden inside the nonselection statement. The collapsed wall set is therefore
`{W_C,W_N,W_X}`. `PASS`.

## N3 — Hidden-wall scan

The required phrase scan was run over the source note, runner, and loop pack.
No hit occurs in the source note or runner for `we assume`, `by construction`,
`as is standard`, `the framework provides`, `bridge context`, `background`,
`naturally`, `obviously`, `standard QFT`, `registered`, or `canonical`.

Hits in the loop pack are non-load-bearing:

- `canonical map` appears only as the name of a failed route;
- `canonical harness` names a forbidden governance surface in the handoff;
- `canonical pack` occurs only inside the verbatim auditor quotation.

No hidden condition was promoted. `PASS`.

## N4 — Residual matching

| Witness | Witness residual | Present residual | Match? | Disposition |
|---|---|---|---|---|
| [`TRACE_GATE.md`](TRACE_GATE.md), blocker quotation | The runner inserted `I_3` and did not derive it from the axiom/carrier surface | Selection of the unit-normalized `hw=1` active/passive carrier | yes | exact blocker source |
| [`MINIMAL_AXIOMS_2026-06-29.md`](../../../../docs/MINIMAL_AXIOMS_2026-06-29.md), lines 103--118 and 128--134 | No Hamiltonian/transfer operator and no source/action bridge are supplied | No axiom map constructs or normalizes the carrier operator | yes | load-bearing premise boundary |
| [`PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md`](../../../../docs/PMNS_ORIENTED_CYCLE_SELECTION_STRUCTURE_NOTE.md), lines 47--60 | Its finite matrix identities do not claim a physical carrier or primitive derivation | Existing PMNS finite algebra does not close this carrier residual | yes | matching exclusion, not proof of the new theorem |
| `STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md` | Nonselection of a physical staggered kinetic/corner law | Nonselection of the PMNS `hw=1` carrier normalization | no | dropped as authority; cross-cycle analogy only |
| `GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md` | Gate-B source/boundary/regulator normalization | PMNS carrier normalization | no | dropped as authority; cross-cycle analogy only |

The actual proof is self-contained in the revised note/runner; no mismatched
prior no-go is used to boost it. `PASS`.

## N5 — Rhetoric audit

The negative phrase is restricted to one resolution:

| Resolution | Tested? | Result |
|---|---:|---|
| Per-element / one-site `M_2(C)` | no negative claim | Pauli algebra is instantiated only; the note does not say it cannot support another bridge. |
| Per-mode | no negative claim | No statement about arbitrary lattice momentum modes. |
| Per-block | yes | Exact target: a `3 x 3` endomorphism on the named `hw=1` carrier. Two formal scalar expansions of the same premise signature separate the unit normalization. |
| Active/passive pair | yes | Independent scalars are propagated; `(I,I)` and `(I/2,I/2)` are explicit same-premise formal expansions. |
| Lattice-wide dynamics | no negative claim | The note explicitly disclaims a no-go for all lattice operators/dynamics. |

The family-wide rejection statement is also restricted: it covers only
jointly invariant scalar blocks under the displayed response formulas and
excludes resolvent poles. `PASS`.

## N6 — Partial-closure path scan

Four legitimate closure paths remain visible:

1. supply the unit seed `D=I_3` explicitly; then the old projector calculation
   is an exact conditional evaluation, not an axiom derivation;
2. derive a unital carrier/source-action functor whose image of the algebra
   unit is the physical sector operator;
3. derive a normalization such as `Tr D=3` (plus a sector-exchange theorem if
   active/passive equality matters);
4. derive a non-scalar source/state tensor with a specified transformation
   type, leaving the invariant scalar-family theorem rather than contradicting
   it.

Defining "free point" to mean the unit block is a valid convention/reframe,
but it changes the result to a definition-conditioned theorem and does not
retire the physical derivation obligation. No path is mislabeled as requiring
a new axiom. Registered primitives were checked and none supplies this
dimensionless content. `PASS`.

## N7 — Steelman

Hostile reviewer steelman: *The unit matrix is the unique algebra unit on the
`hw=1` carrier, and a free theory is conventionally normalized so that its
unperturbed carrier equals that unit. The projector sum then returns `I_3`
without ambiguity; calling the normalization underdetermined mistakes the
definition of the free point for a missing dynamical theorem.*

Response: this is the strongest route and it is correct **after** adding the
unital/free-point convention. It does not defeat the narrow claim, because the
auditor's defect was precisely the presentation of that convention as a
consequence of Lattice/Qubit/Admissibility/Record. The revised note preserves
the convention-conditioned `I_3` point inside the scalar family and removes it
from the load-bearing family rejection. No live untested route remains against
the scoped nonselection statement. `PASS`.

## N8 — Cross-cycle echo

Repo search found three similar shapes:

- [`STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md`](../../../../docs/STAGGERED_DIRAC_MINIMAL_SURFACE_KINETIC_CORNER_NONFORCING_NO_GO_NOTE_2026-07-10.md)
  uses two expansions
  of one `A_min` reduct; it is currently unaudited and attacks a different
  kinetic residual. Its retirement mechanism would be a retained kinetic
  selection bridge, exactly analogous to the carrier/source-action bridge
  explicitly allowed here;
- [`GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md`](../../../../docs/GATE_B_CONTEXT_INDEPENDENCE_NO_GO_NOTE_2026-06-17.md)
  uses different normalization
  completions; it is currently unaudited and attacks a different observable;
- [`DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md`](../../../../docs/DYNAMICS_NONTRIVIALITY_SELECTION_FIREWALL_2026-06-06.md)
  distinguishes a form class from a
  selected law; it is currently unaudited and is not used as authority.

No similar wall was found to have been retired by an unconsidered convention,
primitive, or retained bridge. The only relevant retirement pattern is the
explicit import/bridge route already listed in N6. `PASS`.

## Gate result

All N1--N8 checks pass at the narrow per-block carrier-selection scope. The
source may ship as a `bounded_theorem` exact boundary. The checklist does not
authorize broader `no_go` wording.
