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

**UV-CT (draft, replaces UV-EXT; gate check pending).** Producer: hard-core. Consumer: upper-chain. The target lead owns the wording, and either part can request a change.

Exact statement: `parts/upper-chain.md`, Text section 7. In short, on one fixed physical torus of side 2 a_*:

- **CT1-CT3, sources.** A bound with an analytic local counterterm E(w) at reflection-periodic complex plaquette sources, Lipschitz at a physical scale, with E covariant and additive up to a cutoff-free tau on separated supports.
- **CT4, volume.** log Z_L(beta) >= (L/P)^4 log Z_Tor(beta) - c_F (L/a_*)^4, real and source-free.

All constants are independent of a and L. Non-vanishing of Z is not assumed. Alternatives that also close the chain: UV-LOC-C and IE_p (Theorems 7 and 6 there), and the real form of Theorem 7.8, which gives normalized exponentials rather than the linear field.

Why UV-EXT was dropped (upper-chain Theorems 3 and 4, Proposition 5): the variance of a block energy has a contact term of order a^-4 in physical units; a constant shift has zero momentum, so an explicit reflection-positive Gaussian family with one partition function has separated correlators from zero up to order a^-4; and a volume-uniform complex disc is an open infrared statement.

Credit: the form with a counterterm and position-dependent sources comes through `parts/hard-core--mapped.md` from the Sussman-Alpoge account. So the independent attempt now shares this interface wording with that account, though not its proofs.

## Model floors

model_floor worker: claude-opus-5-5@max, gpt-6-astra@max
model_floor checker: claude-opus-5-5@high, gpt-6-astra@low

The owner set Opus 5.5 as the Claude model for this target and left effort to judgment: max on the crux pushes, high at gate checks, and lower for routine work such as leaf lemmas and editing.

## Metric

Open obligations on the critical path, from `python3 scripts/lab_ops.py status <this folder>`. A new named lemma adds to it. Notes written are not progress.
