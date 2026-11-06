<!-- Draft GitHub issue for ethanwsussman/Yang--Mills-LLM-experiment. Text from gates/out-l17-check.md edit 8, with links filled in. Not posted; needs the owner's approval of this exact text. -->

**Title:** Apply the outline's ER8 radius choice in the account's polydisc-containment proof

**Body:**

I have a proposed local clarification of `5.2:lem-polydisc-containment`, based on your outline's ER8 argument. Credit for that argument and the quadratic tower mechanism belongs to Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of your text.

At [CA-II 4378–4384](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L4378-L4384), the proof invokes the inclusion at auxiliary radii equal to the target radii. The budget in [small pairs](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L34058-L34072) does not justify that invocation. This concerns the inference, not a counterexample to the lemma.

Your [ER8 proof](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L6586-L6630) already gives the replacement, conditional on ER7: use

$$\alpha_0' = \frac{\alpha_0}{4K_{\rm T}},\qquad \alpha_1' = \min\Bigl(\frac{\alpha_1}{2},\ \sqrt{\frac{\alpha_0}{4K_{\rm T}}}\Bigr),$$

your $\epsilon_0,\epsilon_1$ at SA 6618–6619, with $K_{\rm T}$ the constant of the tower estimate.

These consume at most half the target curvature budget in [Theorem 5(a)](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L9746-L9753), provided the individual auxiliary-radius ceilings hold.

[This note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/706cddcf440abe7407cd670c2d15032edabe72bf/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-l17.md) spells out the account notation, an explicit seed constant, the true-current specialization, and a common smaller $c_T$ for the true-pair and polydisc uses. It tracks the inverse powers of $c_T$ that remain in extraction constants and the choices needed before the final coupling ceiling. It also expands your tower mechanism with explicit constants, conditional on the listed uniform input estimates.

The checked input derivations cover SU(2), default omitted-inward bonds and the stated admissible domains. The note does not establish the original curvature-only complex (1.17), the separate continuation/nesting hypotheses, or Theorem 0. Its authorship and model-review history are recorded in the linked note. The proposed change is the reduced-radius replacement at this use site.
