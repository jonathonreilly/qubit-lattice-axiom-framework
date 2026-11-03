lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-03T13:27Z

# a3-clauses: the complex-reference, independent-current and periodisation clauses of (1b) Theorem 4 (queue row 105)

Provenance: Anthropic Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker; checkout `8d897ee40`; Sussman–Alpoge outline `YM4_sketch_500.tex` at `31a47c543775`, fetched once into a private scratch folder (sha256 `d7f77d4d…4d6f`, the same file as `sa-map.md` and `p82-curved.md`). No Balaban text is read beyond what the cited library notes record. Research text, same-model, ungated, not an audit; it grants no status. In progress: sections are appended as they are finished.

Credit. Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the statements of (1b) Theorems 2–6, the regular-pair class with an independent current (SA 10129–10137), the operators \(R,K,Q'\), the metric \(d_{\mathbf B}\), mechanism 2's treatment of the current as an inhomogeneous term (SA 9840) and the warning that an independent-current extension must be specified (SA 5062, 11798). T. Balaban for the background-propagator architecture used through `p82-curved.md` (CMP 95, 96, 99b) and for pairs whose current is a separate variable (CMP 109, p. 262, (1.10)–(1.14), as the outline cites it). OpenAI Codex for `flat-port.md`, `a3-balaban.md` and the gates of rows 89, 99, 100; Claude for `a3-derivative.md` §§6–10 and `p82-curved.md`.

## 1. The clauses, and what this note settles

**Moves:** the last clauses left on real-critical nonlinear A3 (`FINISH.md`, "Where it stands", second bullet; `sa-ledger.md` #3; `route-decisions.md` 1 and 4.2 item 1). If they hold, (1b) Theorem 4 stands in full on the gated chain (rows 81, 84, 85, 95, 98, 100, 101, 103). If one failed, every consumer reading it would have to change.

**Which clauses.** (1b) Theorems 2–6 (SA 9658–9790) were read for complex-reference, independent-current and periodisation content.

- Theorem 2 (SA 9678–9690) concerns a real critical \(U\). It has no such clause.
- Theorem 3 (SA 9692–9732) continues in the *datum* \(B\) at a real reference \(U_0\). That is proved in `a3-derivative.md` §§6–6.1, with the complex regularity of \(\Phi\) from `a1-balaban.md` (9.2) (gates: `a3-derivative-gate.md` §6, `a1-balaban-gate.md` positive finding (c)). The reference is real, so this is not a complex-reference clause.
- Theorem 4, first paragraph (SA 9734–9740): real critical reference, whole datum polydisc. Proved in `a3-derivative.md` §7 and gated, with P82° from `p82-curved.md` (gate row 100).
- **Theorem 4, second paragraph (SA 9742):** "At a regular complex pair \((\mathbf U,\mathbf J)\), critical or not, the corresponding system has a single small solution, and this solution is analytic in the pair. Its response satisfies the bounds on \(\mathsf h\), \(\nabla\mathsf h\) and \(\dot\omega\), and the Hölder member over distances \(\le\xi_y\). The second-order members are then \((D^{\mathsf T}D+DRD^{\mathsf T})\mathsf h\), \(D(1-R)D^{\mathsf T}\mathsf h\) and \(\Delta_{\mathbf U}\mathsf h\), because away from criticality the slice condition is not available." The pair class (SA 10129–10137) has a complex part \(A'\), \(\mathbf U=e^{i\eta A'}U\), and an independent current \(\mathbf J\). So this one paragraph carries both the complex-reference clause and the independent-current clause.
- **Theorem 4, third paragraph (SA 9744):** "At \(\mathbf V_0=\mathbf 1\) on a single lattice, \(\mathsf H_k=\partial_B\mathcal H(0)\) is the periodisation of a \(\mathbb Z^4\)-invariant kernel. At the lifts of two bonds lying within half the torus of each other, it differs from that kernel by \(Ce^{-c\delta_0\ell_k/2}\) ..." This is the periodisation clause.
- Theorem 5 (SA 9746–9768) concerns complex tower configurations and cores carrying an independent current. These belong to the pointed-window admission (`sa-ledger.md` rank 4), which `a3-close.md` §2 moved out of A3; its Lemma T proves 5(a). They are not in this item.
- Theorem 6 (SA 9770–9788): (b) and (c) are real; (d) is a core statement (rank 4). No such clause.

So the item is Theorem 4, paragraphs 2 and 3. Section 2 settles paragraph 3. Section 3 builds the linear package at complex references. Section 4 specifies the pair system, which the outline leaves open, and proves paragraph 2 for it.

**State before this note.** `gates/a3-derivative-gate.md` rated `a3-derivative.md` 9.1 CORRECT-NO-ADVANCE, once for a missing inverse on the complex class and once for an unspecified independent-current operator. It rated the 9.2 periodisation estimate WRONG as stated, because strip holomorphy of a symbol gives no depth-uniform bound. `gates/p82-curved-gate.md` rated the complex-reference remark of `p82-curved.md` CORRECT-NO-ADVANCE: "analytic local coefficients do not by themselves provide the real Kato step at complex links".
