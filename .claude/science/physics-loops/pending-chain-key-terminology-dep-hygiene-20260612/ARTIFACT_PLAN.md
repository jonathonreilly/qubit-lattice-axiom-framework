# Artifact Plan

- Source notes: remove non-load-bearing glossary Markdown citations from the
  eight affected theorem notes.
- Verification: rebuild the citation graph in memory and confirm zero
  `key_terminology` edges from the targeted rows.
- Verification: rerun all eight primary runners under the bundled Python
  runtime.
- Delivery: one review PR against `main`.
