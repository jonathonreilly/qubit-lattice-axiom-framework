# Yang-Mills existence along the hard-constraint route

lead: Anthropic/claude-opus-5-5/max b3f5c21a-8638-4944-b69d-c639619895d6
lease_until: 2026-11-06T02:00Z

Started 2026-10-30 at the owner's direction, on Claude. This is research-stage working state. It grants no status, and nothing here is a public claim.

**Relation to the other target.** `.claude/science/toe-ruleset-20261021/agents/ym4d-proof/` on branch `claude/ym4d-proof-draft` (PR #10114) runs the soft-kernel route under its own lead. Read it freely with `git show`. Do not edit it.

## Target contract

T1: SU(2) lattice Yang-Mills with the Wilson action has a non-trivial, reflection-positive, hypercubic-invariant limit on R^4 as the spacing goes to zero, for local gauge-invariant observables at separated points, along a coupling trajectory the proof chooses.

**Non-trivial** (draft definition by the target lead, 2026-10-31; T1 did not define it before) means both of these hold in the limit:

- **NT1, dynamics.** H is not zero on the orthocomplement of the vacuum. A correlator that is merely non-zero does not show this: a static random constant field has a non-zero connected correlator at every separation (`gates/net-tier-upper-chain-c3242879df.md`, D1).
- **NT2, interaction (revised by the target lead, 2026-10-31, after `gates/witness-3b7fd4e57.md`).** A positive identification, with no comparison class in the definition: along the trajectory, gauge-invariant correlators at scale r equal their perturbative values at leading order in the running coupling g_r, including the part that comes from the three-gluon vertex, and g_r runs to zero as r goes to zero at the one-loop rate. So a finite family at one scale is not enough; the statement has to hold across scales. Which correlators, and with what error, is for `parts/witness.md` to propose. Separation from named classes (holonomies of Gaussian potentials, strictly local composites of range small against the rectangle) is reported as a corollary with its size, not as the definition.

  *Why the earlier wording was dropped.* It asked for a difference from every law of gauge-invariant functions of a Gaussian potential. Every law on a Polish space is a push-forward of a Gaussian, so that class has to be restricted to a named map. With the map restricted, a non-trivial law is still not what the test sees: a Gaussian measure with a non-local quadratic map has the Wilson tree values on every triple of closed paths (gate D2), and a local map or a disorder mixture can meet a finite-family test with no interaction (gate D1). This revision is a draft too, and whether the running clause excludes those laws is under test in `parts/witness.md`.

**Milestone, not T1:** "UV stability on the bounded net" (`parts/upper-chain.md`, Text 10, with the repairs in the gate above). It says the coupling stays fixed at a physical scale. It is not evidence of NT2, and it is not a Haag-Kastler net.

Later targets, not on this critical path: O(4) invariance, N >= 3, and the mass gap.

## Pace

Owner's decision, 2026-10-31: usage must last the full week on each account. The two hard-core attempts run one at a time, alternating, with a rest after each cycle, and the rest follows measured usage. A second worker on the Mac mini takes the queue in `FINISH.md`, one fresh session per item, paced the same way on its own account. `parts/upper-chain.md` and `parts/witness.md` are parked at their last checkpoints, with nothing of theirs unpushed; their next tasks are queue items in `FINISH.md`.

**Workers start at `FINISH.md`.**

## Critical path

1. **hard-core:** all-scale UV stability for hard-constraint block RG in four dimensions, including large fields. Balaban's series (CMP 95, 96, 98, 99, 102, 109, 116, 119, 122) is the known structure. The literature carries no weight here: until rebuilt, each step is an open obligation. Raced by two attempts.
2. **upper-chain:** from the interface below to volume-free local bounds, a joint limit on R^4, and reconstruction on separated tests.
3. **witness:** non-triviality as defined above. Opened 2026-10-31, `parts/witness.md`.

## Interface statements

**UV-CT (draft, replaces UV-EXT).** Producer: hard-core. Consumer: upper-chain. The target lead owns the wording, and either part can request a change.

Exact statement: `parts/upper-chain.md`, Text section 7. In short, on one fixed physical torus of side 2 a_*:

- **CT1-CT3, sources.** A bound with an analytic local counterterm E(w) at reflection-periodic complex plaquette sources, Lipschitz at a physical scale, with E covariant and additive up to a cutoff-free tau on separated supports.
- **CT4, volume.** log Z_L(beta) >= (L/P)^4 log Z_Tor(beta) - c_F (L/a_*)^4, real and source-free.

All constants are independent of a and L. Non-vanishing of Z is not assumed. Alternatives that also close the chain: UV-LOC-C and IE_p (Theorems 7 and 6 there), and the real form of Theorem 7.8, which gives normalized exponentials rather than the linear field.

Why UV-EXT was dropped (upper-chain Theorems 3 and 4, Proposition 5): the variance of a block energy has a contact term of order a^-4 in physical units; a constant shift has zero momentum, so an explicit reflection-positive Gaussian family with one partition function has separated correlators from zero up to order a^-4; and a volume-uniform complex disc is an open infrared statement.

Gate at `gates/uv-ct-upper-chain-41489e4876.md`, same-model: the implications hold and UV-CT is open. CT3 carries all the separated content, E is forced close to log G, and CT4 cannot be verified at Gaussian order.

Credit: the form with a counterterm and position-dependent sources comes through `parts/hard-core--mapped.md` from the Sussman-Alpoge account. So the independent attempt now shares this interface wording with that account, though not its proofs.

**UV-OS (draft, alternative to UV-CT, not a replacement).** One-step statements at constant coupling, with no source in the RG: `parts/upper-chain.md`, Text 16. Ruling after `gates/field-tier-upper-chain-c3242879df.md`, same-model: the two are logically incomparable, so the swap is a trade and not a reduction, and both stay open. The hard core may deliver either; the induction at w = 0 is needed by both. Under UV-OS, the regular tier and the step from the mark to the moment bound hold given the clauses. The rough tier fails as written, so UV-OS does not yet deliver the moment bound: (K3) is not preserved, one clause is false in the free theory, and neither hard-core attempt comes near (GS_j)(e3).

## Model floors

model_floor worker: claude-opus-5-5@max, gpt-6-astra@max
model_floor checker: claude-opus-5-5@high, gpt-6-astra@low

The owner set Opus 5.5 as the Claude model for this target and left effort to judgment: max on the crux pushes, high at gate checks, and lower for routine work such as leaf lemmas and editing.

## Metric

Open obligations on the critical path, from `python3 scripts/lab_ops.py status <this folder>`. A new named lemma adds to it. Notes written are not progress.
