lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-08T16:58Z

# The last-scale constants: a proof of Lemma 6.3:lem-last-scale-constants of the complete account, with a normalization correction

Draft for the owner's review (queue row 352, `wu-lsc`). It is not sent anywhere. Research text: it grants no status and makes no public claim.

**Provenance.** Claude Opus 5.5 (max effort), Mac mini worker, checkout `26443a02d`. This is a write-up of checked texts. It adds no new mathematics. Its sources are: the proof `library/lsc.md` (Codex, two rounds, frozen 2026-11-05); its round-1 check `gates/lsc-gate.md` (Claude, smaller scope); the normalization check `gates/nrm-check.md` (Codex, checked line by line by Codex); and the round-2 check `gates/lsc2-gate.md` (Claude, first failing step none). The scope limits of §9 also come from `gates/lsc-uses-check.md` (Claude) and `gates/lsc-value.md` (Codex). The outward note `library/out-lsc.md` (Codex; checked for faithfulness by Claude in `gates/out-lsc-check.md`) went to the authors as their issue #16 on 2026-11-07. This draft keeps that note's marking of printed and added parts, and its correction F3 on the symbol $B_\sharp$. The presentation changes are listed in §9, item 8. **This write-up has not been checked by the other model.**

**Sources.** CA-I, CA-II, CA-III are `theorem_0_complete_account_raw_{I,II,III}.tex`; SA is `YM4_sketch_500.tex`. All are at commit `31a47c543775`, fetched by URL for this note. Numbers are TeX source lines. Status words are the ones the account declares, in its convention at CA-I 27–46: a statement with no status sentence "is proved in full", and "a statement proved from other named statements lists them … as its explicit hypotheses". Every passage quoted below was read in a bounded excerpt.

**Credit.** The lemma, its setting and notation, and the printed proofs of its parts (b)–(e) (CA-II 63369–63833) are by **Ethan Sussman and Levent Alpoge, with Claude and Codex as authors of their text**. So are the floor mechanism (CA-II 109918–109975; SA 23504–23527), the vacuum-energy theorem and density constants of CA-I 4.36, and the convention $e^{-E}Z$ (CA-II 140916–140926; SA 23405–23415, 23515–23527). **Tadeusz Bałaban** is credited for the renormalization-group construction the account uses: the real-background theorem (CMP 102, Theorem 1), the bounds of CMP 119, and the tree estimate CMP 116 (1.26). The proof of the parts the account leaves open was written by Codex (`library/lsc.md`): the offset argument for (a), the explicit constants on one coupling window, and the completion under the original floor of clause (iii-b). The normalization correction is Codex's (`gates/nrm-check.md`); a Claude check first raised the conflict (`gates/lsc-gate.md`). Claude checked the proof line by line.

## 1. The statement in their account, and its status there

**The label.** At CA-II 63365–63367 the account prints only a remark:

> \begin{remark}\label{6.3:lem-last-scale-constants}
> The statement of this lemma is not written out here; parts of its proof are printed below.

**What is printed.** Part (b), the admissible data and the last-scale coupling (CA-II 63369–63526), with the remark on what it relies on (63528–63565). Part (c), the per-ball bound across unit rescalings (63568–63689). Part (d), the local plaquette count (63691–63798). Part (e), bare couplings tending to zero (63800–63833). The corollary `6.3:cor-volume-free-constant` follows (63836–63899).

**What is not printed.** Part (a) is cited by the proof of (b): "Let $a:=K_J-K$, which lies in $\mathcal A$ by part (a)" (63371–63372). Part (d) cites "the inequality $K\le K_J$ … derived from hypotheses (I1), (I2) and (I3) of that lemma" (63700–63701). Neither part (a) nor (I1)–(I3) appears anywhere. The proof of (b) also takes the size of the last-scale constants from the correlation theorem, as a clause (63399–63410):
\[
E_+^\sharp+C_{\rm low}\le E_J(L,\mathfrak p,\varrho;g,m)
\qquad\text{(6.3:eq-last-scale-coupling-a)},
\]
with $E_J$ "a function of the displayed arguments only". The correlation theorem (CA-II 2791–2966) says only that $E_+^\sharp$ and $C_{\rm low}$ "are constants fixed in the treatment of the last lattice" (2949–2950). Its torus-bound proof takes the lower bound as hypothesis 8, "The floor for the unsourced integral at the level $K'$" (59677), and uses it at 59815–59819. So the open content of the lemma is: part (a), a proof of the floor, and constants $E_+^\sharp$, $C_{\rm low}$ whose sum obeys (6.3:eq-last-scale-coupling-a) at $m=m^J_{\mathbb T}(g)$.

**Status.** CA-III 110895–110899 lists the inputs of the per-ball volume-free bound and ends: "the uniformity of the last-scale constants in the torus exponent. The last of these is of status 'stated; proof incomplete'." CA-II 64603 says instead: "Statements of this book whose proofs are incomplete or outstanding: none." The two declarations conflict. We follow the first: it names this lemma, and the statement is in fact not written.

**Why it matters for their main theorem.** Clause (iii-b) of Theorem 0, the per-ball volume-free bound (CA-I 2610–2620), rests on it (CA-III 110895–110899). Clause (ii), the limits on each torus and on $\mathbb R^4$, appeals to it by statement (CA-II 68362–68365). Four places read it directly: CA-II 63531–63565 (`6.3:rem-exponent-statements`), 63907–63946 (the corollary and `6.3:rem-per-ball-reading`), 64157–64283 (the proof of `6.4:thm-per-ball-bound`), and 68362–68368.

**What this note proves.** Lemma 6.3 as those four uses read it (§3), as an implication from inputs that the account states and declares proved (§8). On the way it corrects one application in CA-I: 4.33 (h4)(a) does not hold for the bare density of Definitions 1.1 and 1.5 (§2). The correction uses the account's own vacuum-normalized convention.

