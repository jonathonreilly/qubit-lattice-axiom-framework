# Yang-Mills existence along the hard-constraint route

lead: Anthropic/claude-opus-5-5/max b3f5c21a-8638-4944-b69d-c639619895d6
lease_until: 2026-10-31T21:00Z

Started 2026-10-30 at the owner's direction, on Claude. This is research-stage working state. It grants no status, and nothing here is a public claim.

**Relation to the other target.** `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` on branch `claude/ym4d-proof-draft` (PR #10114) runs the soft-kernel route under its own lead. Read it freely with `git show`. Do not edit it.

## Target contract

T1: SU(2) lattice Yang-Mills with the Wilson action has a non-trivial, reflection-positive, hypercubic-invariant limit on R^4 as the spacing goes to zero, for local gauge-invariant observables at separated points, along a coupling trajectory the proof chooses.

Later targets, not on this critical path: O(4) invariance, N >= 3, and the mass gap.

## Critical path

1. **hard-core:** all-scale UV stability for hard-constraint block RG in four dimensions, including large fields. Balaban's series (CMP 95, 96, 98, 99, 102, 109, 116, 119, 122) is the known structure. The literature carries no weight here: until rebuilt, each step is an open obligation. Raced by two attempts.
2. **upper-chain:** from the interface below to volume-free local bounds, a joint limit on R^4, and reconstruction on separated tests.
3. **witness:** non-triviality. Not started; it opens when the upper chain states what it delivers.

## Interface statements

**UV-EXT (draft).** Producer: hard-core. Consumer: upper-chain. The target lead owns the wording, and either part can request a change.

On a periodic lattice of spacing a and fixed physical side, with beta(a) on the trajectory, the Wilson partition function Z(beta + s) is non-zero for complex s in a disc, and log Z(beta + s) - log Z(beta), with any explicit subtraction the proof names, is bounded by a constant times the physical volume. The disc and the constant do not depend on a or the volume.

The scale of s is not settled. A guide, not a result: an additive shift of order one in beta = 1/g^2 changes the local dynamical scale by a fixed factor, which suggests s of order one and not a fractional shift of beta. The subtraction is not settled either.

## Model floors

model_floor worker: claude-fable-5-1@max, claude-opus-5-5@max, gpt-6-astra@max
model_floor checker: claude-fable-5-1@high, claude-opus-5-5@high, gpt-6-astra@low

## Metric

Open obligations on the critical path, from `python3 scripts/lab_ops.py status <this folder>`. A new named lemma adds to it. Notes written are not progress.
