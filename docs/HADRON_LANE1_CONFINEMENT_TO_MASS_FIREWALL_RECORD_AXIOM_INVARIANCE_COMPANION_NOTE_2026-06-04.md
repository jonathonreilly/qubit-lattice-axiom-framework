# Hadron Lane 1 Confinement-To-Mass Firewall: Record-Axiom Invariance Companion

> **Key terms used in this doc** are indexed A-Z at
> [docs/KEY_TERMINOLOGY.md](KEY_TERMINOLOGY.md); each row points to the
> canonical source-of-truth doc.

**Date:** 2026-06-04
**Type:** meta (audit-companion / axiom-premise restoration evidence)
**Status:** companion-only — supplies audit-friendly evidence that the
load-bearing structural-firewall content of
[`HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md`](HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md)
is invariant under the 2026-06-04 Record-axiom adoption in
[`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md). It is
not a new theorem claim, not a status promotion, and not an attempt to
perform re-audit work. If the audit pipeline seeds this file, it is a
meta companion row; the audit lane still sets `audit_status`, and
pipeline-derived `effective_status` remains downstream of that
authority.
**Companion target:** `hadron_lane1_confinement_to_mass_firewall_note_2026-04-27`
(parent note `docs/HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md`).
**Primary companion runner:**
[`scripts/audit_companion_hadron_lane1_confinement_to_mass_firewall_record_axiom_invariance_2026_06_04.py`](../scripts/audit_companion_hadron_lane1_confinement_to_mass_firewall_record_axiom_invariance_2026_06_04.py)
**Cached log:**
[`logs/runner-cache/audit_companion_hadron_lane1_confinement_to_mass_firewall_record_axiom_invariance_2026_06_04.txt`](../logs/runner-cache/audit_companion_hadron_lane1_confinement_to_mass_firewall_record_axiom_invariance_2026_06_04.txt)

---

## Why this companion exists

The parent `bounded_theorem` `hadron_lane1_confinement_to_mass_firewall_note_2026-04-27`
is a structural negative-boundary firewall. Its load-bearing content
is the dependency-accounting statement that confinement plus the
bounded `sqrt(sigma)` readout does not determine the pion, proton, or
hadron-spectrum masses absent three named additional premises:

1. retained light-quark masses and chiral inputs for `m_pi`
   via GMOR;
2. retained hadronic-scale running/matching and standard correlator
   extraction for `m_p`, `m_n`;
3. retained dimensionless spectral coefficients `c_H` for each
   hadron family.

The parent's primary expressive structure is the channel-dependent
coefficient separation `m_H = c_H * sqrt(sigma)` with explicit
illustrative `c_pi`, `c_p` values (`0.29`, `2.02`) using the bounded
`sqrt(sigma) = 465 MeV`, plus the GMOR scope statement and the
nucleon-gate dependency list. Its companion runner
(`scripts/frontier_hadron_lane1_confinement_to_mass_firewall.py`)
verifies these channel-coefficient and dependency identities. The
ledger row carries `load_bearing_score = 8.333` and has prior
verdicts (most recently `audited_conditional`, 2026-05-23) that were
archived at note-hash bumps. Current `effective_status = unaudited`.

The 2026-06-04 framework axiom update from `MINIMAL_AXIOMS_2026-05-20.md`
to `MINIMAL_AXIOMS_2026-06-04.md` (Lattice + Quantum + Record;
explicit-owner-approved per
[`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
section 6) changes the stable `minimal_axioms` premise-node note-hash
across the framework. Even where (as here) the row was already
`unaudited` before the axiom-set adoption, audit-lane review of the
row's structural content under the new axiom set is downstream
review work. This companion supplies, for the audit lane, the
narrow machine-checkable observation that **the structural firewall
content is independent of the Record axiom**: the firewall uses only
the Lattice and Quantum axiom content (preserved verbatim across the
2026-05-20 and 2026-06-04 memos), plus standard finite-precision
arithmetic on the channel coefficients `c_pi`, `c_p`, plus the named
upstream open dependencies (Lane 3 light-quark masses, hadronic-scale
running/matching, chiral condensate/`f_pi`). The Record axiom adds a
strictly additive scalar record-readout statement —
`I(R_1 sqcup R_2) = I(R_1) + I(R_2)` — which is neither used nor
invoked anywhere in the firewall content, and which the 2026-06-04
memo itself explicitly excludes from the source/action, log-det,
and observable-bridge scope that the firewall's listed open
premises separately require.

This companion is therefore audit-friendly evidence that the
firewall's substantive content survives the axiom-set change
unchanged: the structural separation between confinement-prerequisite
support and hadron-mass retention still closes on the same listed
upstream premises, and the Record-axiom adoption neither closes the
firewall's three named gates nor opens new ones. It is not a re-audit
and does not promote status; it documents the load-bearing-step
dependency surface in machine-checkable form so the audit lane can
decide whether to honor or re-test prior verdicts on the new premise
hash.

---

## Scope and boundary

This companion makes one narrow auditable observation:

**(C1) Record-axiom invariance of the confinement-to-mass firewall.**
The parent's load-bearing structural content depends only on:

1. the channel-dependent coefficient separation
   `m_H = c_H * sqrt(sigma)` and its explicit illustrative arithmetic
   `c_pi ~= 0.29`, `c_p ~= 2.02` at `sqrt(sigma) = 465 MeV` and
   `m_pi = 134.98 MeV`, `m_p = 938.27 MeV` (parent's "Why One Scale
   Is Not A Spectrum" section);
2. the GMOR statement `m_pi^2 f_pi^2 = (m_u + m_d) Sigma` and its
   dependency on light-quark masses, `f_pi`, and the chiral
   condensate `Sigma` — none of which is retained in the framework's
   current Lane 3 / chiral-SB inventory (parent's "Pion Gate"
   section);
3. the nucleon-gate dependency list (Lane 3 light-quark masses;
   hadronic-scale `alpha_s` running/matching; lattice-QCD-equivalent
   correlator extraction; dimensionless spectral coefficients) —
   none of which is retained (parent's "Proton / Neutron Gate"
   section);
4. the import-class accounting table that classifies each input as
   `retained structural theorem` (confinement), `bounded bridge`
   (`sqrt(sigma) ~= 465 MeV`), `retained quantitative lane`
   (`alpha_s(M_Z)`), or `open dependency` (light-quark masses)
   (parent's "Inputs And Import Roles" table).

None of items 1-4 use the Record axiom's additive scalar
record-readout content. They use only:

- the Lattice axiom (the `Z^3` lattice / index structure inherited
  via the parent's framework reference chain);
- the Quantum axiom (one-qubit / `Cl(3,0)` local algebra; the SU(N_c)
  gauge organization on the lattice site set);
- standard finite-precision arithmetic on the channel coefficients;
- standard reading of the framework ledger for retention status of
  the listed open premises.

**(C1) is the only auditable companion observation.** The three
upstream open dependencies that the parent explicitly names (Lane 3
light-quark masses; hadronic-scale running/matching and correlator
extraction; per-channel dimensionless spectral coefficients `c_H`)
remain open exactly as in the parent note. This companion does
**not**:

- close or weaken any of the three open upstream premises;
- re-audit `hadron_lane1_confinement_to_mass_firewall_note_2026-04-27`
  or any other ledger row;
- introduce a new minimal-axiom statement (the
  explicit-owner-approved axiom set is fixed at
  `MINIMAL_AXIOMS_2026-06-04.md`);
- change the parent's claim scope, claim type, or admitted-context
  inputs (the two `Hypothesis set used (axiom-reset 2026-05-03)`
  gates — staggered-Dirac realization, `g_bare = 1` — are unchanged);
- assert anything about Record-axiom content or its scope;
- modify the audit ledger, the audit queue, or any status field.

The audit lane decides whether (C1) is sufficient evidence to
re-honor the previous verdicts on the new premise hash or whether a
fresh per-site audit is warranted.

---

## The Record axiom is not used by the load-bearing step

The Record axiom (`MINIMAL_AXIOMS_2026-06-04.md` section "Record")
says:

> When a finite record-readout surface is specified, its scalar record
> functional is additive over disjoint record collections:
>
>     I(R_1 sqcup R_2) = I(R_1) + I(R_2)
>
> with `I(empty) = 0` after an explicit additive-baseline convention.

The 2026-06-04 memo's scope statement is explicit about what the
Record axiom does *not* supply:

> This axiom supplies only additive scalar record readout. It does not
> supply a rule for record production, persistence,
> measurement/decoherence, Born weights, P2/modulus/phase-blindness,
> log-det structure, time arrow, system composition, normalization/scale,
> source/action identification, `AC_phi_lambda`, theta, or arbitrary
> observable identification.

The parent's load-bearing firewall content defines no record surface,
asks no question about scalar record additivity, and writes no record
functional `I(.)`. It performs:

- the algebraic separation `m_H = c_H * sqrt(sigma)` followed by
  dimensional-analysis arithmetic to extract `c_pi`, `c_p` from
  observed hadron masses (numerical comparators only, never used as
  derivation inputs);
- the GMOR-formula statement (a textbook chiral-SB identity, used as
  a scope statement about what would be required to close `m_pi`);
- the nucleon-gate dependency list (a structural enumeration of
  required upstream premises, none of which is the Record axiom);
- the import-class accounting table that names each input's role and
  retention status by direct reference to current framework ledger
  citations (`CONFINEMENT_STRING_TENSION_NOTE.md`,
  `ALPHA_S_DERIVED_NOTE.md`, Lane 3 firewall).

None of these load-bearing steps invoke a record functional, a
record-additivity statement, a record collection, or a Record-axiom
citation. The parent's headline conclusion ("Then no retained
hadron-mass closure follows unless the branch also supplies [the
three listed premises]") is a structural dependency-graph statement,
not a record-readout statement. The Record axiom would have to supply
at least one of those three named upstream premises to alter the
firewall's content — and the 2026-06-04 memo's own scope statement
explicitly excludes it from doing so (Record does not supply
log-det structure, source/action identification, normalization/scale,
or arbitrary observable identification, all of which are required to
discharge the three open premises). So the firewall is invariant
under the axiom-set change.

This invariance is what the companion runner verifies block-by-block:
every load-bearing arithmetic and dependency check passes using only
Lattice + Quantum content plus standard finite-precision arithmetic
and standard ledger reading, and a "Record-axiom counterfactual"
block confirms that the structural firewall content is unchanged
whether or not a Record-axiom statement is appended.

---

## Companion runner block plan

`scripts/audit_companion_hadron_lane1_confinement_to_mass_firewall_record_axiom_invariance_2026_06_04.py`
verifies the Record-axiom invariance of the structural firewall.
Each block runs as an independent numeric / structural check;
nothing is hard-coded against an expected target value beyond
elementary arithmetic and direct ledger / note reading. The runner
reports `PASS` / `FAIL` per check; the cached output records the run.

Block 1 — Channel coefficient `c_pi = m_pi / sqrt(sigma) ~= 0.29`.
Computes `c_pi = 134.98 / 465.0` and verifies the parent's stated
value to two-significant-figure precision (`|computed - 0.29| < 0.01`).
Uses only the PDG `m_pi` numerical comparator and the bounded scale
`sqrt(sigma) = 465 MeV`; no Record axiom content appears.

Block 2 — Channel coefficient `c_p = m_p / sqrt(sigma) ~= 2.02`.
Computes `c_p = 938.27 / 465.0` and verifies the parent's stated value
to two-significant-figure precision (`|computed - 2.02| < 0.01`).

Block 3 — Coefficient separation `c_pi != c_p`. Verifies the parent's
structural point that the two channel coefficients differ by an order
of magnitude (`c_p / c_pi > 5`), proving "channel-dependent
coefficients are not fixed by confinement alone".

Block 4 — GMOR-formula symbolic structure. Verifies (symbolically)
that the GMOR identity `m_pi^2 f_pi^2 = (m_u + m_d) Sigma` is a
4-variable expression in `m_pi`, `f_pi`, `(m_u + m_d)`, `Sigma`,
and that knowledge of any 3 leaves the 4th underdetermined absent
external input. Mirrors the parent's "Pion Gate" closure-dependency
statement.

Block 5 — Nucleon-gate enumeration. Confirms that the parent's
nucleon-gate dependency list contains the four named items
(Lane 3 light-quark mass retention; hadronic-scale `alpha_s` running
and matching; lattice-QCD-equivalent correlator extraction;
dimensionless spectral coefficients), as a structural scan of the
parent note's "Proton / Neutron Gate" section.

Block 6 — Import-class accounting table parse. Reads the parent
note's "Inputs And Import Roles" table and verifies each row carries
one of the expected import-class tokens
(`retained structural theorem`, `bounded bridge`,
`retained quantitative lane`, `open dependency`, `comparator`).

Block 7 — "What This Retires" enumeration. Confirms the parent's
three retired implications (`confinement => retained hadron masses`;
`bounded sqrt(sigma) => retained m_pi or m_p`;
`standard lattice-QCD methodology exists => framework has derived
m_p`) appear verbatim in the parent's text, so the firewall's
negative-boundary content is recoverable from the note.

Block 8 — Safe-vs-cannot-claim discipline. Verifies the parent's
"Safe Wording" section contains both a "Can claim" list (4 items)
and a "Cannot claim" list (4 items); structural assurance that the
firewall expresses both the supported scope and the forbidden
extrapolations.

Block 9 — Record-axiom usage check. A static-source scan of the
parent note verifies that the load-bearing firewall content does not
invoke a record functional `I(.)`, a record additivity statement, a
record collection, or a Record-axiom citation. The check enumerates
the phrase set `{"I(R_1", "I(R)", "scalar record",
"record functional", "record-readout", "additive record",
"additive scalar record", "MINIMAL_AXIOMS_2026-06-04"}` over the
parent's load-bearing sections and confirms zero matches.

Block 10 — Record-axiom counterfactual. Re-runs Blocks 1-3 inside
an explicit "Record axiom is asserted" outer scope and an explicit
"Record axiom is not asserted" outer scope; verifies that the
load-bearing channel coefficients `c_pi`, `c_p` are identical in
both runs. The counterfactual is a tautology at the calculation
level (no Record-axiom content enters the arithmetic), which is
precisely the substantive content of (C1).

Block 11 — Quantum/Lattice content preservation across the
historical 2026-05-20 and current 2026-06-04 minimal-axioms memos;
Record axiom scope explicitly excludes log-det / source/action /
observable bridges (the bridges that would otherwise be needed to
discharge the firewall's three open premises).

Block 12 — Independent recomputation of channel coefficients via two
alternative input pairs. Cross-checks `c_pi` and `c_p` with the
exact ratio computation and confirms the parent's two-significant-
figure values are reproduced regardless of trivial rounding choices
on `sqrt(sigma)` within the bounded interval.

Total: 12 blocks; the exact PASS / FAIL count is recorded in the
SHA-pinned cached runner output.

---

## Audit-pipeline boundaries

This companion asserts no theorem claim and no status promotion. The
companion source and runner read as `meta` audit-companion evidence.
Per [`docs/audit/README.md`](audit/README.md) (the auditor sets
`claim_type`, the auditor sets `audit_status`, and the pipeline
derives `effective_status`), no status field changes are implied by
this PR. The audit lane decides whether to re-honor prior verdicts on
the new premise hash; this companion only supplies machine-checkable
evidence on whether the new Record axiom disturbs the firewall's
load-bearing content.

The Record-axiom-invariance observation here is structurally narrow:
it does not extend to any downstream claim that consumes the parent's
firewall output, nor does it discharge the parent's two
`Hypothesis set used (axiom-reset 2026-05-03)` open gates
(staggered-Dirac realization and `g_bare = 1`). Each downstream claim
must be examined independently against the new axiom-set premise
hash. Other rows recently axiom-invalidated under the same hash
change are out of scope of this companion and should be examined
separately as the audit lane reaches them.

---

## Audit-ordering and integration

This companion does not migrate the parent's
`STAGGERED_DIRAC_REALIZATION_GATE_NOTE_2026-05-03.md` / `MINIMAL_AXIOMS_2026-05-03.md`
citations to `MINIMAL_AXIOMS_2026-06-04.md`. The 2026-06-04 memo
preserves the Lattice and Quantum content verbatim and adds the
Record axiom as a strictly additive non-overlapping statement;
the parent's load-bearing content uses only the Lattice + Quantum
content. A separate citation-migration PR (if desired) can refresh
the parent note's reference column; this companion is independent of
that text update and is content-only.

This companion's load-bearing-step invariance observation depends only
on the Quantum and Lattice content being preserved across the two
memos — verified in Block 11 — and on the Record axiom adding a
strictly additive non-overlapping statement — confirmed by direct
reading of `MINIMAL_AXIOMS_2026-06-04.md` section "Record" and by
the memo's own explicit scope-exclusion list (Record does not supply
the log-det / source/action / observable bridges required to
discharge the firewall's three open premises).

---

## References

- Parent note:
  [`HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md`](HADRON_LANE1_CONFINEMENT_TO_MASS_FIREWALL_NOTE_2026-04-27.md)
- Parent runner:
  `scripts/frontier_hadron_lane1_confinement_to_mass_firewall.py`
- Parent audit history snapshot:
  `docs/audit/data/audit_ledger.json` row
  `hadron_lane1_confinement_to_mass_firewall_note_2026-04-27`
  (`load_bearing_score = 8.333`; `previous_audits` includes
  `audited_clean` 2026-04-28 and `audited_conditional` 2026-05-23,
  both archived at successive parent note-hash bumps; current
  `effective_status = unaudited`)
- Upstream open premises (unchanged by this companion):
  Lane 3 light-quark masses; hadronic-scale `alpha_s` running and
  matching; lattice-QCD-equivalent correlator extraction and
  dimensionless spectral coefficients; chiral condensate / `f_pi`
  for GMOR; staggered-Dirac realization gate; `g_bare = 1`
- New framework axioms:
  [`MINIMAL_AXIOMS_2026-06-04.md`](MINIMAL_AXIOMS_2026-06-04.md)
- Predecessor framework axioms (still authoritative for local-algebra
  content): [`MINIMAL_AXIOMS_2026-05-20.md`](MINIMAL_AXIOMS_2026-05-20.md)
- Axiom-minimality policy and explicit-owner-approval ledger:
  [`docs/audit/AXIOM_MINIMALITY_POLICY.md`](audit/AXIOM_MINIMALITY_POLICY.md)
- Audit lane authority statement:
  [`docs/audit/AUDIT_LANE_AUTHORITY.md`](audit/AUDIT_LANE_AUTHORITY.md)
