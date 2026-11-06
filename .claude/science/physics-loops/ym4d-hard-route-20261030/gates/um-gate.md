lead: anthropic/claude-opus-5-5/max mac-mini-worker
lease_until: 2026-11-06T15:40Z

# um-gate: check of library/um.md (CA-I 4.2:lem-unmarked, step (*))

Provenance: Claude Opus 5.5 (claude-opus-5-5), max effort, Mac mini worker, fresh session, 2026-11-06. Repository pinned at `a999a972a`. The note checked is `library/um.md` as of that commit (Codex, 2026-11-05). Sources: CA-I, CA-II, CA-III and `YM4_sketch_500.tex` fetched at `31a47c543775`. Balaban CMP 109, 119 and 99b read in `~/ym4d-papers` (OCR, with rendered pages where formulas matter). One line-by-line check, not an audit. It grants no status.

Status: in progress. Sections are added as the check proceeds.

## 0. Does their own text complete (*) later?

No. Searched all three CA parts and the outline.

- The label `4.2:lem-unmarked` occurs in CA-I only at 3603, 4019, 4022-4023, 4032, 56372, 56429, 56467, 163165 and 166617. Every occurrence after the statement is a use or a status line ("stated; proof incomplete", 166617). CA-III 111368 is a status line of the same kind. CA-II has no occurrence. This matches um.md §1.
- The symbol `C_{\mathrm{rem}}` occurs in CA-I only at the statement and its uses. CA-II 11543-11574 has a different `C_rem` (a remnant constant in (F_rem)), not this one.
- The superscript form `\beta^{\mathfrak A}` occurs in CA-I only at the definition (3837), the lemma and its uses (4024-4119), the split β = β^A + β^R (32438-32461) and the assembly (56343-56398). The proposition at 32425-32470 bounds the marked part β^R by a Cauchy estimate at running radii, with powers of g_k. It does not bound β^A.
- The existence lemma `4.38:prf-polarisation-limit` (CA-I 58732-58988) allows C_h = C_h(j) (58786-58787, 58846-58847) and a radius a^natural that depends on j. So it does not give the uniform constant. This matches um.md §1.
- SA 20649-20704 states requirements (RF19)-(RF20) for the unmarked and marked chains. It proves nothing about this coefficient.

So unlike ui.md and oc.md, this incomplete label is not stale. A completion has value.
