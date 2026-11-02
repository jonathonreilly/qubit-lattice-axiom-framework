lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-02T23:20Z

# sa-map: the Sussman-Alpoge outline mapped onto this folder

Queue row 69. Author: Anthropic claude-opus-5-5, effort max, Mac mini worker,
started 2026-11-02T11:20Z. Folder pinned at branch commit `3267555c7`.
Same-model reading: not independent in model, not a gate, not an audit, no
status. Nothing here is load-bearing until checked by hand in this folder.

**Source and credit.** Ethan Sussman and Levent Alpoge (with Claude and Codex
as authors of their text), `YM4_sketch_500.tex` in
https://github.com/ethanwsussman/Yang--Mills-LLM-experiment at commit
`31a47c543775f3f74013d06dd5d85962358f3b9e` (the head of `main` when read),
32,992 lines, sha256 `d7f77d4d...4d6f`. Line numbers below are lines of that
file. The programme it adapts is Balaban's (CMP 95, 96, 98, 99, 102, 109, 116,
119, 122); it cites those papers by number ("95", "102", ...). Its own text
says it is unvetted ("Proof outline" banners, a "dependency catalogue" of
obligations). Scripts: `checks/samap/` (a read-only locator; no numerics).

Status: in progress, written section by section.

## 0. How the outline is organised (what "open" means there)

- Main theorems: Theorem 0 (clauses (a) existence, (b) inheritance, (c) bounds
  and non-triviality, (d) uniqueness on a torus, (e) rotations) and Theorem 0'
  (volume-first limit, O(4), canonical phase decomposition, reconstruction),
  lines 6829-7042. Observable: the smeared plaquette action density O(f), only
  separated tuples, n >= 2. The trajectory is "first passage": K(beta, g) is
  the first level at which the running inverse coupling x_k enters
  [g^-2, g^-2 + B_sharp]; g is fixed small. So the continuum limit is taken at
  a fixed renormalized coupling g at physical scale 1, as in our T1.
- Dependency catalogue, lines 3757-4649 (Section "Supporting analytic results
  and proof dependencies"): eight packages A-H, each with four numbered items
  (A1-A4, ..., H1-H4). Items called "Obligation" are unproved; items called
  "Requirement" are claimed proved or derived there, sometimes only
  conditionally. H4 (line 4629) states the route: "the actual D1 and F2-F3
  proof outlines must be completed and a sequence of admissible data
  constructed".
- Index, lines 32869-32923: "Statements still to be proved, by package" lists
  the coded tasks of this item. Tags in the body: "[to be proved; Package X]"
  (16 places), "[outlined below; Section ...]" (Props 2.10, 2.13) and
  "[outlined here; Section ...]" (Lemma 7.6), "[proved here; ...]" (4.10, 4.12),
  "[cited from Balaban; ...]" (Prop 1.2 of CMP 95, Prop 8 of CMP 102).
- The coded tasks and the catalogue obligations are two layers of the same
  debt: e.g. Package C's 2.8-2.13 sit inside catalogue C1-C4, 4.11 inside D1,
  7.5/7.6/7a.1.8 inside F2-F3, Package A inside A1-A4. Both layers are mapped
  below; the catalogue obligations are the "main-line steps outlined rather
  than proved" of the task (Section 3).
