# YM4D: research on 4D Yang–Mills (snapshot)

This section holds mathematics on 4D lattice Yang–Mills. It works on the
Sussman–Alpöge account of the 4D SU(2) theorem
([ethanwsussman/Yang--Mills-LLM-experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment),
pinned at commit `31a47c543775`), which extends the renormalization-group
program of Tadeusz Balaban.

**This is not framework science.** No axiom of this repository enters
these texts. They have no rows in the audit ledger and no audit status.
The review loop does not grade them. Words such as "frozen" and "checked"
below are this project's own terms, defined here.

## Words

- **Frozen.** A referee in a fresh session found no failing step, or one
  repairable step. The fixes were applied. The text carries
  "Status: frozen". A frozen text is a conditional theorem: it holds as an
  implication from its named imports. Its Outstanding paragraphs name
  what it does not prove.
- **Checked line by line by X.** One reading by the named model. It is
  not an audit and grants no status.

## Source

Every file here is a byte-identical copy from the working branch
`claude/ym4d-hard-route` (draft PR #10132) at commit
`af80bc9a5f58cd5b2f62c218fcdb8e2105aed972`, directory
`.claude/science/physics-loops/ym4d-hard-route-20261030/`.

The texts keep their relative links. Links to files in this snapshot work
here. Links to working files that are not in this snapshot (drafts, other
gates, the source digests) resolve on the working branch:
<https://github.com/jonathonreilly/qubit-lattice-axiom-framework/tree/af80bc9a5f58cd5b2f62c218fcdb8e2105aed972/.claude/science/physics-loops/ym4d-hard-route-20261030>

The working branch keeps its full history. Its history is never rewritten,
because the posted issues link to its commits.

## Index and status

| File | What it is |
|---|---|
| [library/t0-tree.md](library/t0-tree.md) | The proof tree for the target theorem, with a change log |
| [library/open-registry.md](library/open-registry.md) | Every open statement, with one owner and its standing |
| [library/assembly-status.md](library/assembly-status.md) | Which parts are frozen, distilled or open, and the critical path |
| [library/ym4-assembly.md](library/ym4-assembly.md) | The assembly skeleton |

## Frozen part texts

Each part has its referee report in `gates/`.

| Part | Title | Referee |
|---|---|---|
| [AG1](library/ag1.md) | Uniform rarity of old large-field regions | [gate](gates/ag1-gate.md) |
| [CL1](library/cl1.md) | Continuum limits, Euclidean Hilbert space and cones | [gate](gates/cl1-gate.md) |
| [Descent](library/descent.md) | Descent for H-M: Theorems A and B and Proposition C | [gate](gates/descent-gate.md) |
| [FP1](library/fp1.md) | The classical flat propagator package | [gate](gates/fp1-gate.md) |
| [H-M](library/hm.md) | The Gaussian matrix envelope | [gate](gates/hm-gate.md) |
| [Layer theorem](library/layer-thm-part.md) | The layer theorem the account assumes at CA-I 72392–72399, as an implication from 16 named premises | [referee](gates/layer-part-ref.md) |
| [IN1](library/in1.md) | Constant order, mass induction and first passage | [gate](gates/in1-gate.md) |
| [LG1](library/lg1.md) | Lattice Gibbs states and all mirrors | [gate](gates/lg1-gate.md) |
| [NL1 (L)](library/nl1-L.md) | Product-box holomorphy and the CI reduction | [gate](gates/nl1-L-gate.md) |
| [P82](library/p82.md) | The constrained inverse at a real curved reference | [gate](gates/p82-gate.md) |
| [PH1](library/ph1.md) | Phases, components and clustering | [gate](gates/ph1-gate.md) |
| [PR-lay](library/pr-lay.md) | Precision gap and decay at complex layered stage pairs | [gate](gates/pr-lay-gate.md) |
| [RO1](library/ro1.md) | O(4) covariance | [gate](gates/ro1-gate.md) |
| [SR1](library/sr1.md) | All-state transfer, graded bounds and growth | [gate](gates/sr1-gate.md) |
| [ST1](library/st1-r4.md) | Fourth revision, with Amendment CV | [gate](gates/st1-r4-gate.md) |
| [TP1](library/tp1.md) | Two-point extraction from imported multiscale estimates | [gate](gates/tp1-gate.md) |
| [WR1](library/wr1.md) | Wightman reconstruction per component | [gate](gates/wr1-gate.md) |

## Contributions posted to the Sussman–Alpöge repository

Each issue links its note at a fixed commit of the working branch. The
copies here are byte-identical to those commits. The issue on GitHub is
the posted record; the `-issue.md` files are the drafts it was posted from.

| Issue | Title | Note |
|---|---|---|
| [#10](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/issues/10) | Proposed proof of your constrained-minimizer lemma (CA-I §4.13) | [out-mu](library/out-mu.md) |
| [#11](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/issues/11) | Proposed proof of the starred step in your unmarked-increment lemma (CA-I §4.2) | [out-um](library/out-um.md) |
| [#12](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/issues/12) | Use your outline's ER8 radius choice in the polydisc-containment proof (CA-II §5.2) | [out-l17](library/out-l17.md) |
| [#13](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/issues/13) | Covariance-inverse remark (CA-I §4.5): a proof under a local gauge hypothesis, and two cases where (S1)–(S2) do not suffice | [out-pi](library/out-pi.md) |
| [#14](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/issues/14) | Further operator walks after CMP 99b Theorem 3.9: endpoint bounds on the PI class | [out-gw](library/out-gw.md) |

## Credit

The operators, local models and random-walk method are Tadeusz Balaban's.
The account, its labels and its line numbers are Ethan Sussman's and
Levent Alpöge's. Each text names who wrote it and who checked it.

## How this section changes

New material lands by a small curated PR built fresh off `main` at a
milestone: newly frozen parts, newly posted notes, and the updated index
files. Working state (lane drafts, queues, briefs) stays on the working
branch.
