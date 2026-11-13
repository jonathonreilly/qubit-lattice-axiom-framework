Ethan and Levent,

Your `4.2:lem-unmarked` is marked "Stated; proof incomplete at the step marked $`(\ast)`$" ([CA-I 4084–4111](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L4084-L4111)). [This note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/64be8397d/.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-um.md) ([Markdown source](https://raw.githubusercontent.com/jonathonreilly/qubit-lattice-axiom-framework/64be8397d0cbd948e6d68de25ad0473bf043e215/.claude/science/physics-loops/ym4d-hard-route-20261030/library/posted/out-um.md)) gives a proposed proof of that step: the uniform extraction argument.

Under the four hypotheses at CA-I 4040–4058, it proves both bounds for every $`l\ge1`$:

```math
|\beta_l^{\mathfrak A}-\beta_l^0|\le C_{\rm rem}\,\varepsilon_1^{\mathrm I},\qquad |\beta_l^{\mathfrak A}|\le C_\beta .
```

It uses only the constructed prefix $`g_0,\ldots,g_{l-1}`$. $`C_{\rm rem}`$ is fixed before $`\varepsilon_1^{\mathrm I}`$, and $`C_\beta`$ before $`\gamma`$.

The proof applies your Cauchy and moment method in all four scaled norms, with uniform analytic room and both response slots.

The note lists every input before the proof. These include Tadeusz Balaban's CMP 116 (2.41), and his constrained inverse-covariance expansion and bounds CMP 99b (3.132). As your `4.5:rem-covariance-inverse-walks` records, (3.132) is printed without proof. These inputs, the averaging and response estimates, and your family hypotheses stay as assumptions. The note does not prove them, and it does not prove the full renormalisation step.

Codex wrote the working proof, and a separate Claude session checked it line by line. That check found no failing step, and its three citation corrections are applied. Codex wrote this outward version, and Claude read it against the corrected proof and your cited lines.

This is a proposed proof of the starred step for your review. It does not claim that the full account is complete.

---
*Edited 2026-11-08: The math is reformatted so that GitHub renders it. The note link now points to a copy of the same note with the same reformatting, followed by its Markdown source. In that copy, links to our working files now point to those files at the note's original commit. No word, formula or claim is changed.*

