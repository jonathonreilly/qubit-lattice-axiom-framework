# Observable-Principle T1-d Downstream Citation Firewall

**Date:** 2026-06-17
**Type:** bounded support / source-scope firewall
**Claim type:** bounded_theorem
**Status authority:** independent audit lane only. This source note does not
set or predict an audit outcome.
**Primary runner:** [`scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py`](../scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py)

## Purpose

`OBSERVABLE_PRINCIPLE_FROM_AXIOM_NOTE.md` is still conditional on the declared
T1-d readout-identification Boundary. The 2026-06-16 independence no-go proves
that T1-d is not derivable from the current Lattice, Quantum, and Record axioms
plus determinant block algebra.

That means downstream source notes and runners must not call the parent
observable principle, the `log|det|` generator, or the determinant scalar
readout "retained" merely by citing the parent row. This note repairs the
explicit high-risk citations that did so.

## Firewall Rule

For current source consumers, use wording such as:

```text
conditional T1-d observable boundary
conditional T1-d log|det| generator
conditional T1-d scalar observable boundary
```

Do not use:

```text
retained observable principle
retained log|det|
retained scalar observable principle
retained axiom-native scalar generator
```

unless a later independent audit/approval actually changes the effective
status of the T1-d readout-identification bridge.

## Scope

This repair does not derive T1-d, add a new axiom, register a new premise, or
retag any audit row. It only prevents downstream citations from laundering the
conditional parent into retained-grade language.

Historical raw AI-dispatch transcripts are not edited by this firewall. They
remain archival, not current source authority.

## Verification

Run:

```bash
PYTHONPATH=scripts python3 scripts/frontier_observable_principle_t1d_downstream_citation_firewall_2026_06_17.py
```

Expected:

```text
TOTAL: PASS=<N> FAIL=0
VERDICT: observable-principle T1-d downstream citation firewall passes.
```
