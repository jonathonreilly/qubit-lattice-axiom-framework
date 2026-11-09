lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-10T02:06Z

# ch-r2: second round on CH4-AUX

Started 2026-11-09T14:06Z at commit cdc9a2fc8 on branch claude/ym4d-hard-route. Research-stage working state; no status.

(Sections follow as they are written.)

Provenance: Claude Opus 5.5 (max effort), Mac mini worker 2. Research text, not an audit, not an independent check, no status. Every deduction below is a written hand argument; searches and hashes discharge nothing.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline (SA), the complete account (CA-I, CA-II, CA-III) at `31a47c543775`, and the newer upstream files read in §1. Tadeusz Bałaban for the background, localization and large-field constructions (CMP 102, 109, 116, 119, 122a, 122b). Codex for `ch-bridge.md`, `ch-r1.md`, `prior/ch.md`, `mu.md`, `ui.md`, which this note builds on.

## 1. Repo search and sources

**Task.** FINISH row 415: second round on CH4-AUX (`ch-r1.md:355-368`, `ch-bridge.md:270-277`, `open-registry.md:23`). Not to repeat attacks A, B, C of `ch-r1.md`, nor PH 1-6 (`ph.md`) and Bridge 1-3 (`ch-bridge.md`).

**Read whole first:** `prior/ch.md`, `ch-r1.md`. Also read: `ch-bridge.md` §§1, 5-7 and Result; FINISH sections 1-84, 299-351 and rows 412-415; GOAL.md.

**Duplicate check (rule 0a).** CH4-AUX appears in `open-registry.md:23`, `t0-tree.md:347`, FINISH rows 331, 411, 412, 415. No other live lane attacks it. `open-core.md` and `l17c.md` do not name it.

**Repo prior work used here.**

| Note | Standing | Use here |
|---|---|---|
| `mu.md` §§5-6, Result | frozen; checked line by line by Claude (`gates/mu-gate.md`), first failing step none | Nesting identity of constrained minimizers, real and complex, with the curvature/current identities (6.3). Ported in §3. |
| `ui.md:549-572` | checked by Claude (`gates/ui-gate.md`), first failing step none | Proof of CA-I `4.5:lem-uniform-increment`: condition (iv) of CMP 109 is reproduced under a twist with a depth-free constant. Used in §5. |
| `ch-bridge.md` (6)-(9) | Codex, not refereed | Uniform contraction and ceiling arithmetic. Reused in §5 with a fixed system. |
| `uses-old.md:194`, `port/p4-operator.md:202`, `wd.md:49` | records | CA-I `4.5:lem-window-minimiser` (19267-19374) has a written proof at real data; `wd.md` records that the later 4.29 window proposition needs the whole window in the top stratum. |

**Primary sources read for this note** (hashes match `prior/ch.md:9-14`):

* CA-II 46131-46216 (target), 47976-48155 (links), 48156-48330 (readings), 48330-48620 (spaces and hypotheses (a)-(e)).
* CA-I 12936-13030 (class 𝔖 of the response chart), 14370-14540 (chart definition and Theorem `4.5:thm-chart-existence`), 15879-16020 (remark on condition (iv)), 19267-19300 (window-minimiser lemma), 19775-19840 (where condition (iv) is consumed), 20186-20250 (spaces), 43195-43530 and 44100-44260 (consumer radii, re-blocking step), 49480-49630 (seven entries), 73530-73640 (global carriers), 148120-148210 (CMP 122a conditions).
* **Bałaban's printed pages, read from the page images** (owner's copies in `~/ym4d-papers`, rendered with PyMuPDF; the OCR layer garbles formulas): CMP 122b pp. 370-376, CMP 122a pp. 189-191, CMP 119 pp. 261-262, CMP 109 pp. 262-263 (text layer, legible there). No earlier CH lane read CMP 122b itself: `ch-bridge.md` §7 and `prior/ch.md:164` used only the account's quotations.
* **Upstream at HEAD** `3ac0bf4f` (2026-11-09T13:10Z), listed through the GitHub API. New today: `YM4/BA/YM4_BA.tex` ("Block averaging and gauge geometry", sha256 `26f00014…`); it treats block averaging and gauges, not the localization links. `YM4/YM4_1400.tex` (sha256 `222ef1bd…`, = `2bc0658f9` copy) defines its own hereditary core with tower configurations `U_n(Z;P)=Φ_{M_{B'}(U)}((1/i)log{M_{B'}(𝐔)M_{B'}(U)^{-1}})` and bounds (YM4_1400:766-790); it does not treat the CMP 122b links (1.61)-(1.63). The Theorem 0 account moved to `YM4/Old/` with unchanged sizes.

## 2. What CMP 122b prints for the three links

These are readings of Bałaban's printed text. They correct no statement of the account; they add the original wording that the account cites.

**(2a) Every link output is a localized constrained minimizer.** CMP 122b p. 374, (1.63):
\[
 U_{k,\Lambda}=U(\mathbf B_k(Y_3),M^{\cdot}(U_{k,\Lambda}))
 =U\bigl(\mathbf B_k(Y_3),\ ((u_{k,\Lambda})_-)^{-1}e^{i\tilde Q(\eta\mathbf H_k)}R((u_{k,\Lambda})_+)M^{\cdot}(U_k)\restriction_{(Y_3^0)^c\cap Y_3},\ V''\restriction_{\Lambda^c\cap Y_3},\ V^{(\Lambda)}_\Lambda\bigr),
\]
with \(\mathbf H_k=\mathbf H_k(-\tfrac1i\log V'_k\restriction_\Lambda)\) by (1.64). The same form holds at link 3, (1.62) on p. 373, with \(\mathbf B_1(Y_2)=\mathbf B(Y_2)\cup\mathbf B_1\) and \(\mathbf H_{\mathbf B_1}\), and at link 2, (1.61) on p. 373, with \(\mathbf B''_k(Y_1)=\mathbf B(Y_1)\cup\mathbf B''_k\) and \(\mathbf H''_k\). Bałaban (p. 373): "Y_1 \ Y_1^0 is a boundary layer at the boundary ∂Y_1, of the width 2M_1 at most, for the corresponding scale."

Consequence used below. The link-4 output is
\[
 w_3(\sigma)=U\bigl(\mathbf B_k(Y_3),D_\sigma\bigr),               \tag{2.1}
\]
a minimizer for **one fixed** determining system. The switches \(\sigma=\sigma^{(4)}\) enter only through \(\mathbf H_k(\sigma)\) in the data \(D_\sigma\) on the boundary layer \((Y_3^0)^c\cap Y_3\). The constraint rows do not depend on \(\sigma\); only their prescribed values do. On \(Y_3^0\) the data are \(V''\) and \(V^{(\Lambda)}\), which after the substitution of \((\mathbf U,\mathbf J)\) become \(M^{\cdot}(\mathbf U)\) and \(V^{(\Lambda)}(M^k(\mathbf U))\) (p. 374, last paragraph).

**(2b) Bałaban claims no stage-space membership for intermediate outputs.** CMP 122b p. 375: "the regularity properties of the configuration (1.63) are almost the same, as the regularity properties of \(U(\mathbf B_k(Y_3),(M^{\cdot}(\mathbf U)\restriction_{\Lambda^c},V^{(\Lambda)}(M^k(\mathbf U))))\)". The same words are used for (1.62). The only precise statement is (1.65), for the composite: \((\mathbf U,\mathbf J)\in\tilde U^c_k(Y_4,\tilde\alpha_0,\tilde\alpha_1)\mapsto U^0_k(\mathbf U,\mathbf J)\in\tilde U''^c_k(Y_1,\tilde\alpha_0,\tilde\alpha_1)\), "proved already, in a slightly less general form, in the proof of the equality (1.89) [IV] ... we do not repeat them here".

**(2c) Where the auxiliary clauses come from, and who reads them.** CMP 109 p. 263, after condition (iv) ((1.15)-(1.16)): "The last condition (iv) is connected with the fact that in some important constructions in the next sections we have to substitute the functions (1.15) in place of the variables U, J." The same page shows (i)-(iii) at smaller constants imply (iv), through CMP 102b Proposition 9 (CA-I 15912-15925 quotes this). CMP 122a p. 191: the stage spaces descend in \(n\), and "if \(\mathbf U\) is an element of the space \(\tilde U^{(n+1)c}_k\), then \(\exp i\eta\mathbb H^{(n)}_k(\cdot)\mathbf U\) is an element of the space \(\tilde U^{(n)c}_k\) ... we will not repeat it". CMP 119 p. 262: newly created terms "are defined on slightly larger spaces, with the coefficients in their definition bigger by β multiplied by a corresponding number".

**(2d) A dictionary difference, recorded only.** CA-II 48057 says link 2 "uses the determining set \(\mathbf B_k(Y_1)\)". CMP 122b (1.61) prints \(\mathbf B''_k(Y_1)=\mathbf B(Y_1)\cup\mathbf B''_k\). CA-I 73572 also writes \(\mathbf B''_k(Y^{\rm tr}_1)\). Nothing below depends on this; `prior/ch.md:67` already flags the decoration.
