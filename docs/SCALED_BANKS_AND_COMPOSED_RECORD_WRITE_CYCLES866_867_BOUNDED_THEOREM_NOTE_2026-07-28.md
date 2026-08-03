# Scale breaks the offset law, records become state content, and locality lives in the restore class — Cycles 866–867

Date: 2026-08-03

Authority: none

Audit: unset

Status: bounded worked results (two supervisor-authored primaries, one
worker-authored adversarial checker that refuted the middle version and
corroborates the final one; owner-directed finale of the
formation-is-the-tick program; no axiom surface touched)

Claim type: bounded_theorem

Runners:

- [`frontier_cycle866_scaled_banks_2026_07_28.py`](../scripts/frontier_cycle866_scaled_banks_2026_07_28.py)
- [`frontier_cycle867_composed_record_write_2026_07_28.py`](../scripts/frontier_cycle867_composed_record_write_2026_07_28.py)
- [`frontier_cycle866_867_finale_independent_check_2026_07_28.py`](../scripts/frontier_cycle866_867_finale_independent_check_2026_07_28.py)

Receipt:

- [`scaled_banks_composed_record_write_cycles866_867_receipt_2026_07_28.json`](../outputs/scaled_banks_composed_record_write_cycles866_867_receipt_2026_07_28.json)

Constitutional effect: none. This package changes no axiom, foundation,
Qualification, primitive, registry, policy, queue, audit result, or audit
status.

## Provenance and the in-block review chain (read this first)

This block carries an unusual history that is part of its evidence:

1. The v1 primaries ran on 2026-08-02; the owner's review found three
   real defects (hardcoded verdicts in 866; a host-side list wearing a
   dead-wire story in 867; a vacuous locality gate).
2. The v2 repairs were authored minutes before a machine reboot killed
   the session; they were recovered from the session transcript on
   2026-08-03, committed BEFORE rerunning, and reran clean.
3. The adversarial checker (worker-authored, spec'd to refute) then
   **refuted v2's certificate C implementation**: the locality walk
   sliced the synchronous word into equal-length chunks while the true
   per-step gate counts are non-uniform (32/32 sampled keys), and the
   near/far split was positional (index < width/2) rather than
   bank-membership — bank 1's block lies at indices 172–302, so the
   far arm ran ZERO perturbations. It also found REGISTER_CAP=64
   undisclosed while dropping 97.7% of write events from wire
   visibility.
4. v3 (supervisor-authored) repaired all of it: true per-step chunks,
   kernel pack-state bank membership, four declared perturbation
   classes, every cap disclosed in the emitted certificates. The
   checker, reconciled to v3 with the v2 refutation kept as a
   reproducible regression arm, now passes with ZERO refutations —
   every replay arm CONFIRMED, the probe cells corroborated
   cell-for-cell.

The physics reading changed under review, which is exactly what the
discipline is for: v2's headline "formation is globally hypersensitive"
was an artifact of the two implementation defects.

## Results up front

**Cycle 866 — the scaled-bank construction (B=3 and B=4), all five
computed gates PASS, independently replayed exactly:**

- the all-bank sync on-tick fraction FALLS with scale: 0.1416 (B=2,
  landed) → 0.058037 (B=3) → 0.048992 (B=4); checker control: the
  store cap binds on 4 and 52 lanes, and the UNCAPPED fractions
  0.05652 / 0.042678 preserve the direction;
- first-allsync reproduces the landed E2 census for 0/38 (B=3) and
  0/70 (B=4) keys — the landed two-bank tick does not re-derive from
  records at scale;
- the Cycle-865 offset law BREAKS at scale: neither the gauge
  e1-moment nor the native birth pattern is functional for the
  offsets; offsets spread to 8 (B=3) and 16 (B=4);
- pair cadences fully fragment: 3/3 and 6/6 distinct signatures
  (checker: full gap histograms give the same distinctness as the
  disclosed most_common(3) granularity);
- stamped censuses 60/38 (B=3) and 107/70 (B=4).

**Cycle 867 v3 — the composed record-write model at horizon 16,384,
all four gates PASS, independently replayed exactly:**

- record writes REALLY mutate state: slots allocated from 5,270
  structurally dead wires (of 5,668 boundary-dead; the checker
  verified the pool is never-read/never-written with zero initial
  columns), 129 slots, 92,120 wire bits set, ZERO dead-activation
  conflicts and ZERO write-once violations on the wires — with the
  disclosed semantics that zero violations certifies the fresh-slot
  allocation discipline plus non-interference (3,856,705 write events
  beyond the disclosed per-lane cap of 64 are host-log only);
- the register reproduces the annotation machinery moment-exact
  164/164; record EXISTENCE is read back from the mutated columns
  (748 lanes carry a first-slot bit — the whole census, so existence
  readback does not discriminate the 164 stamped keys; disclosed);
- **the corrected formation-locality probe** (32 lanes, 4 payload
  wires per side by kernel pack-state bank membership, four declared
  classes):
  - firing is ROBUST: one-flip fires 32/32 near AND far; late-acting
    and untouched-in-chunk classes fire everywhere they apply;
  - record CONTENT is hypersensitive: content equality 0 in every
    direct-flip class, both sides;
  - locality appears in the RESTORE class: flip-and-restore preserves
    firing and content 32/32 near versus 29/32 far — a genuine
    near/far contrast, with the 3 far failures showing
    path-dependence (a transient far perturbation can leave a
    permanent trace).

**Corrected reading:** formation firing is robust and
endpoint-determined; what is fragile is recorded content; and the
near/far structure of the model shows up in path-dependence, not in
firing. The Campaign-5 queue item "robust formation via copy
redundancy" is accordingly reframed: the open question is whether copy
redundancy protects CONTENT, and whether the restore-class contrast
scales.

## Negative-claim discipline

Every negative here is scoped: the tick non-derivation and offset-law
breakage are at the declared B=3/B=4 probe (events {0,1}, k=2, horizon
8,192, store cap 1,024 — cap binding disclosed with uncapped controls);
content-hypersensitivity is at the declared four-class, 32-lane,
4-wire-per-side sample; nothing is claimed beyond the declared
perturbation classes.

## Checker disclosure

The checker was authored by a Claude Opus 5 worker (codex quota
exhausted 2026-08-03; substitution disclosed) in an isolated context,
spec'd to refute, and it DID refute the supervisor's v2 — the
adversarial structure worked despite the shared authoring model
family. The supervisor's reconciliation edits (pins to v3, claims
table, corroboration verdict, historical framing) are disclosed in the
commit trail; the v2 refutation is kept reproducible inside the
checker as a regression arm, and an AST guard fails the checker if
either v2 defect pattern reappears in the primary. Independent audit
still required.

## Trace gate

```yaml
trace_class: upstream_support
target_claim_id: null
target_blocker_text: "formation-as-saturation / the robust-formation question: 867's hypersensitivity names the suspect (superseded framing); B-AXIS second-leg discharge needs the record-time laws at scale"
source_of_blocker_text: handoff
reachability_to_target: supports
artifact_role: runner_certificate
next_trace_action: "queue 2b reframed to content-robustness under copy redundancy; the restore-class contrast is the new discriminating instrument; 866's scale breakage prices the offset law's domain"
```

## Status fields

```yaml
actual_current_surface_status: bounded-support
target_claim_type: bounded_theorem
conditional_surface_status: null
hypothetical_axiom_status: null
admitted_observation_status: null
claim_type_reason: "exact finite certificates at declared scopes; every number independently replayed by a checker with disjoint machinery; caps disclosed with uncapped controls where they bind"
audit_required_before_effective_retained: true
bare_retained_allowed: false
```

## Imports, derived, open

### Imports

- the 719 kernel and the 863 census/annotation machinery (sha-pinned,
  imported by declaration);
- the 852-lineage census scope; everything the cited packages declare.

### Derived

- the scale behavior of the derived clock (on-tick falling, tick
  non-rederivation, offset-law breakage, cadence fragmentation);
- the composed record-write model with structural inertness and
  moment-exactness;
- the corrected locality phenomenology (robust firing, fragile
  content, restore-class contrast with far path-dependence).

### Open

- content-robustness under copy redundancy (queue 2b, reframed);
- the restore-class contrast at scale (B=3/4 composition not yet
  built);
- the rate law; the B-AXIS second leg.

## Verdict

Asked at scale, the toy stopped being polite: the offset law that
looked fundamental at two banks is a two-bank accident, and the
"hypersensitive formation" of the first composed model was two bugs
wearing a finding. What survives the checker is sharper than what it
replaced — records that are genuine state content, formation that
fires no matter what you flip, content that remembers everything, and
a locality signal that lives precisely in whether a perturbation was
still present at the edge. Independent audit still required.
