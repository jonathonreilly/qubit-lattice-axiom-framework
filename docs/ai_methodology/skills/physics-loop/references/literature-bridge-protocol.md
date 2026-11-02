# Literature Bridge Protocol

Build on published work; never let an unverified external step carry weight in
a derivation.

## When To Use

Always. Every route, lemma lane or repair starts with a literature search, run
far and wide for its statement and its method, before it builds
(`docs/ai_methodology/SCIENCE_WORKFLOW.md` section 2, rule 9). `--no-web` only
moves the search offline, marked unverified.

## Source Rules

- Prefer primary papers, official datasets, or standard mathematical
  references.
- Use current source lookup when facts may have changed or precise citations
  are needed.
- For physics/math claims, cite the exact theorem, equation, dataset, or
  experimental quantity being used.
- Do not quote long passages. Summarize the role and cite the source.
- Rebuild a literature lemma that a step needs as a credited library entry; the
  citation is attribution and carries no weight
  (`docs/ai_methodology/SCIENCE_WORKFLOW.md` section 10). Until then the step
  stays an open obligation and the item keeps its import class below. An entry
  lands with the milestone that uses it, not on its own.
- Link open papers rather than committing their PDFs.
- Record each source's access status and what was actually read. An unread
  source is not known.

## Import Classification

Every literature item must enter `ASSUMPTIONS_AND_IMPORTS.md` as one of:

- `literature theorem`;
- `standard correction`;
- `observational comparator`;
- `admitted convention`;
- `background context`;
- `non-derivation analogy`.

If a literature item supplies a load-bearing physical value or selector, the
repo claim must be marked derived-with-import, bounded support, or open unless
the loop retires that import.

## Output

Record each search first: where it looked, the exact statements found, how close
each is to ours and whether its proof is accessible. A search that finds nothing
is recorded too. Then record each item used in `LITERATURE_BRIDGES.md`:

| Source | Exact item used | Role | Import class | Affected claim | Derivation impact |
|---|---|---|---|---|---|

End each literature bridge with one sentence:

```text
This source is used as <role>; it does / does not provide derivation closure for <claim>.
```
