lead: anthropic/claude-opus-5-5/high mac-mini-worker
lease_until: 2026-11-02T23:53Z

# Literature search: the large-field position and the four lanes of sa-map Section 5

Queue row 74, `lit-large-field`. Pinned at commit 199fac1cb. In progress; sections are added as they are written.

Author: Anthropic claude-opus-5-5, effort high, Mac mini worker, started
2026-11-02T23:53Z. Same-model reading: not independent in model, not a gate, not
an audit, no status. A literature search finds statements and proofs. It
verifies nothing. Every statement listed below is **unchecked here** until it is
rebuilt by hand in `library/` and gated, per "Build on published work" in
FINISH.md.

## 0. Scope and how the search ran

The four statements are the four lanes of `library/sa-map.md` Section 5, all
written in the symbols of Sussman and Alpoge's outline `YM4_sketch_500.tex`
at `31a47c543775` (cloned read-only to a scratch directory; this was still the
head of `main` on 2026-11-02):

- **S1 (`sa-floor`).** Floor screening and renewed tests of the R operation:
  a new mark pays outside the old floor F (l. 18334-18415), and item (4) of
  "One action and many claimants" (l. 17712).
- **S2 (`sa-seam-response`).** Healing across seams. A layered,
  seam-crossing response bound (their A3, (1b) Theorems 3-4, l. 9693-9745),
  which feeds the ten-term remainder R_X of Prop 2.8 and the resummation of
  Prop 2.10.
- **S3 (`sa-order`).** One simultaneous order of constants (C4, Theorem 2.11,
  l. 19435-19470).
- **S4 (`sa-count`).** The genealogy count (Prop 2.6, l. 17719; count over
  generations l. 18475-18604) and the label sum with the logarithm (Prop 2.13).

Sources searched: Balaban's series (CMP 85-122, plus his later N-vector
large-field papers); Dimock's expositions (Balaban RG I-III; scalar QED_3;
QED_3 I-III); Balaban-Feldman-Knörrer-Trubowitz (bosonic many-body); Balaban-
Imbrie-Jaffe and King (Higgs); Magnen-Rivasseau-Sénéor (YM_4 with an infrared
cutoff); Federbush (phase cells); Gawedzki-Kupiainen; Brydges and
Bauerschmidt-Brydges-Slade (large-field regulators); recent probabilistic and
stochastic-quantisation work (Chatterjee, Cao, Chevyrev, Chandra-Hairer-Shen);
the Sussman-Alpoge repository (YM4 outline, YM3_I/II, QED3, QCD3, and the raw
Theorem 0 account); the two other public projects its README lists
(`marikgoldstein/scalar-qed-existence`, `pmaronow/3d-ym-torus`); arXiv and
news for anything since mid-2026.

**Access.** arXiv full texts were downloaded to a scratch directory outside the
repository and read as text; no PDF is committed. **Balaban's CMP papers (all
of 95-122) are behind a bot check at Project Euclid and a paywall at Springer
from this machine; per the rules I stopped there.** Everything said below about
the inside of CMP 122a/b comes either from the abstracts or from secondary
accounts (the outline's own page citations, Dimock's remarks), and is labelled
so. A reader with library access should check those page claims first.

**Other news.** OpenAI announced on 2026-10-26 a claimed existence proof for
four-dimensional Yang-Mills (with a Lean formalisation reported done
2026-10-16). Nothing of it is public: per news reports the artefacts are
withheld pending a review panel. It gives us nothing to read or credit. The
Sussman-Alpoge README refers to it and says their work continues.
