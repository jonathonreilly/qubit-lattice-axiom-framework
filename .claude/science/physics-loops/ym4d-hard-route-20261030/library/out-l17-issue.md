**Title:** Use your outline's ER8 radius choice in the polydisc-containment proof (CA-II §5.2)

Ethan and Levent,

This issue proposes a small local repair to the proof of `5.2:lem-polydisc-containment`. The repair is your outline's ER8 argument.

At [CA-II 4378–4384](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L4378-L4384), the proof uses the inclusion with auxiliary radii equal to the target radii. The small-pairs budget at [CA-I 34058–34072](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L34058-L34072) does not justify that step. This is a gap in the inference, not a counterexample to the lemma.

Your [ER8 proof](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L6586-L6630) already gives the replacement, conditional on ER7:

$$
\alpha_0' = \frac{\alpha_0}{4K_{\rm T}},\qquad \alpha_1' = \min\Bigl(\frac{\alpha_1}{2},\ \sqrt{\frac{\alpha_0}{4K_{\rm T}}}\Bigr),
$$

with your $\epsilon_0,\epsilon_1$ from SA 6618–6619, and $K_{\rm T}$ the constant of the tower estimate. If the ceiling on each auxiliary radius holds, these radii use at most half of the target curvature budget in [Theorem 5(a)](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/YM4_sketch_500.tex#L9746-L9753).

[This note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/877743789c269744f7500a62087d21e545df72b1/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-l17.md) writes the repair in the account's notation. It gives an explicit seed constant, the true-current case, and one smaller $c_T$ for both the true-pair and the polydisc uses. It tracks the inverse powers of $c_T$ that stay in the extraction constants, and the choices that must come before the final coupling ceiling. It also writes out your tower mechanism with explicit constants, conditional on the uniform input estimates it lists.

The input derivations are checked for SU(2), with the default convention that omits inward bonds, on the stated admissible domains. The note does not prove the original curvature-only complex (1.17), the separate continuation and nesting hypotheses, or Theorem 0.

Codex wrote the working derivation, and Claude checked its parts line by line. Claude wrote this note from it, and Codex checked the note line by line. The note records each check.

This is a proposed repair at this one use site, for your review.
