# Preserved mechanical link-check failure

A scratch Python regex check exited1 at its path assertion. It used `re.findall(r"\]\(([^)]+)\)", note_text)` on all source text, without excluding indented code. The two actual prose Markdown links resolved correctly; the third match was `rho` from the displayed mathematical expression `D[n_x](rho)`, not a Markdown dependency. The terminal output was `AssertionError`; no source or generated cache changed.

The corrected narrow check filters indented/fenced code before extracting prose links and records the two actual tracked regular targets in LINKS.json. This agrees with the earlier complete schema2 discovery. The failed regex was a mechanical parsing error, not a missing mathematical dependency; it is preserved here rather than counted as a successful check.
