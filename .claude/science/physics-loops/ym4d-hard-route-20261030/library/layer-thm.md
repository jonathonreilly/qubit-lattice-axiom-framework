# The general layer theorem: ownership stop

Written 2026-11-07 by Codex gpt-6-astra on the laptop.
Checkout: `c7fbdc21a9fcb85d7d3b7d4a556ada99666c3af2`.
Research text. Not an audit. This note grants no status.

Credit: Tadeusz Balaban for the background and propagator constructions;
Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their
text, for the complete account and outline. No numerical or computer-assisted
proof is used.

Source convention: I, II and III denote the three complete-account files.
SA denotes `YM4_sketch_500.tex`. All four are in
`/Users/jonreilly/ym4d-lead/sa`, with supplied revision `31a47c543775`.
Their SHA-256 identities agree with the source-identity table in `layer-find.md`.
The source directory is not treated as a verified Git checkout.

Sources read: `GOAL.md`; FINISH's published-work, efficiency and rules
instructions; `layer-find.md` in full; `open-registry.md`'s LAYER-THM and
CA-LAYER entries; `t0-tree.md:304–324`; the outline index README navigation
and relevant rows in chunks 05, 09–11 and `obligations.md`;
`lit-balaban.md:131–168`; SA 5762–5803, 9693–9744, 10354–10464,
10562–10578; I 14376–14652, 14992–15104, 15265–15445,
15669–15764, 72373–72538, 94123–94422; and the source ranges of
U01–U34 in `layer-find.md:28–61`. The passages at I 14817–14870,
111360–111561 and 112570–112620 were also read.
The decisive repository readings are `ca-f.md:54–71`,
`stage-claude.md:149–185`, and `gates/stage-gate.md:136–163`.
Some initial combined outputs were truncated. The decisive passages listed
in the last sentence were subsequently read in bounded ranges.
`library/prior/layer-thm.md` does not exist. The entry-point file
`docs/ai_methodology/SCIENCE_WORKFLOW.md` is absent in this checkout.

**Stopped under the user's ownership rule.** The LAYER-THM row assigns this
task to `layer-thm`. An existing row assigns a necessary part of the same
target to `stage-claude`. These assignments overlap. I do not infer that
the new row revokes the existing assignment.

## Statement

The following identifies the overlap. It is not a proposed replacement
for the six-clause theorem.

`open-registry.md:960` reads:

> `CA-LAYER | Exact scope and evidence: t0-tree §5.5 | stage-claude | OPEN`

`t0-tree.md:314` specifies:

> “Full (N1)/(L), all four entries, arbitrary weights, actual completion kernels and complex range.”

This assigns the full weighted layer estimate to another lane. The
assignment is not merely about the block-data chart already available.

`ca-f.md:58–62` states the assigned input. For every admitted kernel
\((W,\sigma)\), with \(|\sigma|\le e^{\kappa_1}\), every determining set,
every admitted weight \(p\in\mathfrak M_\delta\), and two admitted data
\(d_i=(j_i,b_i)\), let \((A'_i,X_i,\mathbb H_i)\) denote the furnished
triples. The input requires

\[
\begin{aligned}
\max\{&N_y^\Delta(A'_1-A'_2),\ N_y(\mathbb H_1-\mathbb H_2),\\
 &\ell_y^3|P_1(\sigma)(A'_1-A'_2)|,
 \ell_y^3|\mathfrak m_H(\sigma)(X_1-X_2)|\}
 \le B_{\mathbb H}\|d_1-d_2\|_{\mathrm{dat},p}\,p(y).
\end{aligned}
\tag{N1}
\]

It also requires the zero datum to give the zero triple. The field datum
has its derivative norm; it is not measured only in the supremum norm.
The source then says:

> “This is the antecedent (L) of `stage-claude.md`; it is not attacked here.”

The requested clause (b) contains this exact input. I:112589–112599 says:

> “For every weight” and “any two data of the layer map”.

It then lists

\[
\|\delta A'\|_p^\Delta,\quad
\|\delta\mathbb H\|_p^\Delta,\quad
\|\delta X\|_p,\quad
\|P_1(\sigma)\delta A'\|_p,\quad
\|\mathfrak m_H(\sigma)\delta X\|_p.
\]

The next sentence states that these norms contain the four entries of
\(\mathsf N_y\). Thus the requested five-norm assertion includes (N1).
This is overlap in the mathematical quantifiers and conclusions, not
merely overlap in theorem names. It affects U16 directly and the
completion-layer use U26.

The existing chart result does not remove this overlap. I:14863–14866
describes its current-kernel bound as standing

> “in place of the fourth and fifth members”

of the quoted response estimate, namely those containing
\(D^*D\) and \(\Delta\). It does not bound all the constituent
second-order terms separately. The existing comparison in
`gates/stage-gate.md:142–157` already makes this distinction for (N1).
Its narrower result concerns block data, an exponential support weight,
and the chart's field and partner current. Repeating that result would
not prove the assigned general-datum estimate.

## Result

**Ownership stop.** The instruction to stop at another row's target applies
to the required (N1) subproblem of clause (b). No new proof attack follows
that finding. In particular, I do not manufacture three failed attacks
on a lemma already assigned elsewhere.

No clause (a)–(f), corollary, parameterised form, or current rider is
newly proved in this note. No invocation U01–U34 is newly covered.
No counterexample to the general layer theorem is claimed.

The exact stopping input is (N1), with its general field/block data,
all admitted weights, and actual complex completion kernels. It is
CA-LAYER, owned by `stage-claude`. The additional five-norm requirements
do not eliminate this necessary input. The six-clause statement and its
proof remain unwritten here because of that ownership stop.

Only `library/layer-thm.md` was written. No registry, status, prompt,
account source, or platform instruction was changed.

RESULT: stopped under the ownership rule; clause (b) includes CA-LAYER/(N1), already owned by stage-claude; no new theorem or U01–U34 coverage is claimed.
