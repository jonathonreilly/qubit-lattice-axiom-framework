# Uniform bounds at the starred step of your unmarked-increment lemma

Ethan and Levent,

[This note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/31def2a2e1cd4d8f118d253d447770370d12fbd8/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-um.md) supplies the uniform extraction argument at your `4.2:lem-unmarked` star (CA-I 4084–4111, commit `31a47c543775`).
Under the four hypotheses at CA-I 4040–4058, it gives both bounds for every $l\ge1$:
$$
 |\beta_l^{\mathfrak A}-\beta_l^0|\le C_{\rm rem}\varepsilon_1^{\mathrm I},\qquad |\beta_l^{\mathfrak A}|\le C_\beta.
$$
It uses only the constructed prefix. The constants are fixed before $\varepsilon_1^{\mathrm I}$ and $\gamma$, respectively.
It applies your Cauchy and moment method in all four scaled norms, with uniform analytic room and both response slots.
The note lists every retained input before the proof, including Tadeusz Balaban's CMP 116 (2.41) and the CMP 99b (3.132) bounds and walk expansion printed without proof.
Those inputs, the averaging and response estimates, and your family hypotheses remain conditions; the note does not prove their propagation from nothing.
Its scope is this application of your extraction method. It does not prove Balaban's unproved walk expansion or the full renormalisation step.

Codex wrote the working note. A fresh Claude session on the Mini checked it line by line: ADVANCE, with citation repairs F1–F3 now applied.
Codex wrote this outward version; Claude read it against the repaired note and your cited lines.
This is research text, not an audit, and grants no status.
