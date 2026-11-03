lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T18:45Z

# h-walk-fix: region-trace locality and single-term covariance of statement 5

Queue row 123. Pinned at commit 8fac7b660 on `claude/ym4d-hard-route`. Same-model work (Claude Opus 5.5, max). It has not been gated and has no status.

Status: in progress. Sections are written as they are finished.

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker, fresh session, repository commit 8fac7b660. Same-provider text: it repairs Claude's `h-walk.md` against Codex's `gates/h-walk-gate.md`. Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched by URL into a private scratch folder (SHA-256 d7f77d4d…4d6f, the same file as rows 103–126) and not copied here; SA nnnn are its line numbers. No numeric job was run, so the numeric lock was not needed. No subagent. Every step is written by hand.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for statement 5 and its clauses (SA 10309–10343), mechanisms (f), (g), (i) (SA 10540–10560), the bond-midpoint convention for the hypercubic tensor (SA 13191–13200), and the consumers listed in §1. Tadeusz Balaban for the cut-down-sequence method (CMP 99 (1985) 389–434, pp. 408–410), used through `h-walk.md`. OpenAI Codex for the counterexample and the visible repairs in `gates/h-walk-gate.md` §§3, 8 that this note completes.

## 1. Who reads W(c)–(d), T(d) and H3 on our chain

The failed clauses (`gates/h-walk-gate.md` §§3, 6, 8, 10 items 1, 4) are:

- **(RT) region-trace locality and canonicity:** W(c)'s "depends on S only through Omega_i ∩ [[omega]]", W(d)'s "same function under a translation carrying the data on the hull", T(d) (which inherits both), and H3's "depends on the regions only through their traces on [[omega]]" and "same function for two sequences, tori or cutoffs related on the hull";
- **(IC) single-term isometry covariance:** H3's "covariant under the lattice isometries that preserve the level-(k+1) M_1-grid, the regions and Omega_{k+1}".

The field-locality and field-holomorphy part of W(c), and the gauge-covariance part of W(d), passed the gate (§6) and are not at issue.

| Consumer | Position on our chain | What it reads | Failed clause read |
|---|---|---|---|
| `a2-full.md` Theorem VI, in the collared form of `gates/h-walk-gate.md` §9 | M (A2 item 3) | (H1), (H2) with root support, the field carrier, field holomorphy on a fixed region sequence | none (the gate's §9 says so; checked) |
| `o1-decoupled.md` Theorem B (a), (d) | N (WF room, rank 4) | field part of W(c), gauge part of W(d) | none |
| `o1-decoupled.md` Theorem C, through its Lemma C1 | N (removed-map comparison) | the term identity for walks of two **different** sequences (S and the box sequence) that agree on G^♯ | **(RT)** for W, in an instance, proved in place |
| `o1-decoupled.md` §3 (H-field), "the same walk-term argument" for H_1(s), 𝔊(s) | N | the same identity for the tree walks of Theorem T | **(RT)** for T(d), in an instance, not proved there |
| `wf-room-2.md` (WF7) removed fields | N | Theorems C, D of `o1-decoupled.md` | **(RT)**, through the row above |
| Package C, SA 17548–17556: terms with domain X ⊂ Λ_{j+1} "are built from walks and fields inside X, so the regions do not affect them … the same for every label"; SA 19523 (e): "a carried term is literally unchanged" | H (Package C, carried) | walk terms of the fluctuation form whose hull lies where two labels agree are the same function | **(RT)** for H3 |
| (3b), SA 7837: "A term localised in X is assembled from walks, potentials and tests within X … depends on neither the torus nor the cutoff"; its users: the infinite-lattice companion of a pointed member (SA 32651–32652), the torus comparison (ET9)–(ET10) (SA 26918–26930) | R (D1 producer), E | identity of terms on all tori with room | **(RT)** for H3 and W(d) |
| R9's transport, SA 10404–10405 and 10567: "transports the solution whenever the assigned walk data are transported" | N | translation transport of the specified walk data (`o1-decoupled.md` Definition D uses Theorem W at j = 0) | **(RT)** for W(d) |
| Requirement B2, SA 3937–3950: "the individual member's pointed totals are covariant under unit translations and the full hypercubic group"; SA 7581: pointed totals covariant under all isometries, "part of the definition of renormalised" | E (marginal coefficient, merged into P1), N | covariance of each localisation domain's activity, hence of the walk terms assigned to it | **(IC)** |

`sa-2.13-2.md` (line 128) and `wf-room-2.md` (line 413) mention `h-walk.md` without reading any of its clauses.

**Conclusion of the listing.** Consumers exist. Inside our library, only `o1-decoupled.md` reads (RT), and it reads an instance that its Lemma C1 proves. The outline positions that our route carries (H, N, R, and E through P1) read (RT) and (IC) in full. So the item is not stopped, and §§2–4 do the repair.

**Mechanism (i)'s symmetrisation does not replace (IC).** Its Haar mean is over real **gauge** transformations, and its mean over translations, push-forward and Montel limit (SA 10560) give one assignment for all tori. None of these averages over coordinate reflections or permutations. So the outline's own construction has to supply single-term isometry covariance, and the outline itself moves to bond midpoints for this reason when it reaches the hypercubic tensor (SA 13191: "Under reflections, lower bond starts undergo a direction-dependent integer displacement … move first to bond-midpoint coordinates").
