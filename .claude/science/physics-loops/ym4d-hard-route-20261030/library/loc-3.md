lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-04T14:35Z

# loc-3: (LOC) after the s210 repair (queue row 214)

Provenance: Claude Opus 5.5 (`claude-opus-5-5`), effort max, Mac mini worker. Checkout `414c8343f`. Sussman–Alpoge outline `YM4_sketch_500.tex` and `YM3/YM3_I.tex` at `31a47c543775`, fetched by URL into a private scratch folder; "SA L" numbers refer to that file. Research text, not an audit; it grants no status. No machine computation enters any step.

Credit: Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text, for the outline and every method used here (the strip substitution, Theorem 6, the decoupled response (R9), the one interpolation of SA L17905–17918). Balaban for the strip method (CMP 119) and the large-field operation (CMP 122). Codex for `loc.md`, checked in Section 1.

## 0. What the outline does with this step

I read every outline passage that treats the locality of formed terms. Classification: **sketched**. The outline asserts (LOC) and names its method. It does not give the proof, and it lists the method's main input as open.

- SA L17453 (traces and charts) asserts that two histories with equal traces on \(W\) "produce corresponding terms with domains in \(W\)". It adds: "a term is regarded as a partial map on the fields on \(W\)". So the outline's locality is locality in the current fields (the pair), the label and the stored variables.
- SA L17541: for the strip Jacobians and the shifted quantities, "A cluster expansion as in (1d) is applied to each part."
- SA L17558–17564 (carriage): the change of background between moves gives differences that "Localisation turns ... into boundary terms". The stage difference "is localised as well".
- SA L17905–17918 gives the method: "Each walk in the response carries a parameter \(s(\Delta)\) ... Setting a parameter to zero prevents a walk from crossing that cube." Brackets in \(s\) and Schwarz's lemma in \(\lambda\) give \(f(U^{\rm old})-f(U^{\rm new})=\sum_{Y\supset X}f_Y\), \(|f_Y|\le2\mathsf ab_fe^{-(\bar\kappa-1)\mathfrak m(X,Y)}\).
- SA L5762–5800 specifies the decoupled response input (R9). "When \(s\) vanishes on separating cubes, the equations split over the remaining components, and the response on a component with no datum is zero."
- SA L17959–17966 asserts the healed-gas locality: "\(V_{\mathfrak X}(Y)\) depends on the healed family \(\mathfrak X\) only through its components inside \(Y\)".
- SA L3876–3881 states the main input as open: "The corresponding non-Abelian background and multiscale response estimates remain to be proved. This includes the decoupled response assertion numbered 1c.10".

The outline never localises with a nest of localised backgrounds. Lemma N (`s210-3.md`) and Lemma N′ (`s210-fix.md`) are the repo's own device. This note checks that device, shows where it fails, and proves the outline's walk route as an implication. So the Result is of two kinds: a check of our own text (Sections 1–4), and a proof of a step the outline sketches (Sections 5–6).
