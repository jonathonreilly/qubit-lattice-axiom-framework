**Title:** Further operator walks after CMP 99b Theorem 3.9: endpoint bounds on the PI class

Ethan and Levent,

Following our issue #13, [this note](@LINK@) supplies the graph-endpoint walk estimates below for the further operators of Tadeusz Balaban, CMP 99b §3 after Theorem 3.9. Your list at [CA-I 166595–166596](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/blob/31a47c543775/theorem_0_complete_account_raw_I.tex#L166595-L166596) records these expansions as printed without proof. All account references use commit `31a47c543775`.

**What it supplies.** Absolute local expansions bound $H_0(\sigma):B_p\to E_p^\Delta$, $\widetilde G^J(\sigma)\Theta_J(\sigma):E_p\to E_p^\Delta$, and $D(\widetilde G^J(\sigma)V'_\sigma)(A):E_p\to E_p^\Delta$, with constants $C_{\kappa_1}$, $C_{\kappa_1}|J|_{(-3)}$, and $C_{\kappa_1}r$. The norm includes the component covariant Laplacian. The note gives the constant order and a necessary linearization test.

**Scope.** Use the PI class of issue #13: literal rows, (S1-loc), (S2), (S2+), full coefficient reads, and a common choice of constants before the tile size and radii. No bound is asserted for an arbitrary earlier choice. The torus side is at least $\max\{2\widehat r+2,t_FM_F\}\ell_k$; all stated gap and decoupling-cube floors apply. The independent-current ceiling is chosen before $\kappa_1$; the field radius may depend on it.

The tags follow your `4.5:prf-chart-walk-localisation`, CA-I 15266–15310: one tag per primitive concatenation, including side branches; composites retain their factors' tags. Identity pieces use the stated smooth cutoff decomposition. No switched inverse identity is used.

**Inputs beyond proofs in your account.** Theorem PI; the absolute flat estimates, from a written reconstruction of Balaban's flat method; and the supplied-frame averaging estimates. The last are the analytic form of Balaban's CMP 98 Proposition 5, (156)–(157), which he states without proof (your CA-I 13175–13196). The note links a written proof of that form as an implication from a frame bound. On this PI class, (S1-loc) together with the twist bounds supplies that frame after reducing the radii. Balaban's CMP 116, (1.6)–(1.11), supplies the decoupling method; the note gives the tree count, including insertion carriers.

**Not covered.** The individual uses in your account were not checked one by one. Admission of your account's domains is not certified. General-field completion-map identification, termwise lattice covariance, boundary gauge gluing, and graph bounds for $G_\pi^J$ or $G_1^J$ are not supplied. The note does not prove the whole account walk proposition.

Codex (gpt-6-astra) wrote the proof. Claude (Opus 5.5) checked it line by line, and its repairs are applied. The flat input was written by Codex (GPT-6) and the averaging input by Codex (gpt-6-astra); Claude checked each line by line. Codex prepared the outward note.

Claude (Opus 5.5) checked this note line by line against the working proof.

This is a proposed proof for your review. It is research text, not an audit, and grants no status.
