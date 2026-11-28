**Title:** Covariance-inverse remark (CA-I §4.5): a proof under a local gauge hypothesis, and two cases where (S1)–(S2) do not suffice

Ethan and Levent,

Your [remark](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L13142-L13173) `4.5:rem-covariance-inverse-walks` cites the bounds (3.132) and the walk expansion of $\mathsf q_0=(QG_0Q^*)^{-1}$ as printed without proof in CMP 99b. [This note](https://github.com/jonathonreilly/qubit-lattice-axiom-framework/blob/94df5579a/.claude/science/physics-loops/ym4d-hard-route-20261030/library/out-pi.md) gives a proof for Balaban's literal averaging rows under a local hypothesis. It also shows that (S1) and (S2) alone do not give the inverse on your tower class.

**What the note proves (Theorem PI).** Assume (S1-loc): about each site of $\Omega_0$, a box of fixed size carries a unitary gauge with a small potential. Assume also (S2), and (S2+), which is (S2) on the bonds just outside $\Omega_0$. Then:
- $\mathsf q_0$ exists and is holomorphic in the twist. At real $U$ it is Balaban's operator.
- $\mathsf q_0$ satisfies a bound of the scale and decay form of (3.132), for the bare $G_0$.
- $\mathsf q_0$ has a local walk expansion with geometric majorants and spare factors. Two settings that agree on a walk's footprint give the same term.

The constants do not depend on depth, volume or background.

This also supplies, under the same local hypothesis, the (3.132) input listed in our issue #11.

**Where (S1) gives the local hypothesis.** On thick towers, at every site whose box lies in $\Omega_0$ (Proposition 3.1).

**Where (S1)–(S2) do not suffice.** Take $G=SU(2)$ and your conventions at [CA-I 12712–12724](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L12712-L12724) and [CA-I 11016–11023](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L11016-L11023).
- Proposition 3.2: $\Omega_0$ has a thin finger, at most 9 big blocks wide, far from $\Omega_1$. A real $U$ in (S1) and (S2) makes $\Delta_a$ singular, so $G_0$ and $\mathsf q_0$ do not exist. Balaban's restriction on CMP 99b p. 396 excludes such a finger.
- Proposition 3.3: $\Omega_0$ is any nonempty proper subset of $T_\eta$, on a box of the size Theorem PI needs. A real $U$ that differs from 1 on one field bond leaving $\Omega_0$ makes $\Delta_a$ singular. No tested cube contains that bond.

Neither proposition says anything against Balaban's own class or his Theorem 3.3.

**A reading of (3.132).** At [CA-II 54617–54619](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_II.tex#L54617-L54619) your text says that, within one layer, the exponential factor in (3.132) "does not depend on $d(y,y')$". On CMP 99b p. 422 the factor is $e^{-\delta_1 d(y,y')}$ for all $y\in\Lambda_j$, $y'\in\Lambda_{j'}$.

**Not covered.** The current-corrected $G_1$ inverse. The pointwise and Hölder bounds for $G_0$. A boundary gauge-gluing lemma. Termwise lattice covariance of the walk terms (your C1). Section 11 of the note lists which of your lines the result supplies, use by use.

Claude (Opus 5.5) wrote the proof. Codex (gpt-6-astra) checked it line by line, and its repairs are applied. Codex prepared the note from the checked proof; Claude checked it line by line against that proof, and read your cited lines and the cited Balaban pages.

We hope this helps you close the remark. It is a proposed proof for your review. It does not claim that the full account is complete.
