"""Assemble FINAL_REPORT.md = title + one-page summary + 'How to read this' + findings + menu + assembled model + decisions.
The detailed 'Bottom line' of the draft is dropped (the summary replaces it; every item is in the sections)."""
d = open("MORNING_DRAFT.md").read()
summ = open("MORNING_SUMMARY_DRAFT.md").read().strip()
i_how = d.index("## How to read this")
body = d[i_how:]
title = "# Overnight campaign 8 (2–3 October): what your tick and moving-record ideas do\n\n*Final report. Explorations of your instincts, not positions; nothing here is adopted. Toy models and derivations, graded exact / checked / argued; seven rounds of hostile review folded in.*\n\n"
summ = summ.replace("## The night in one page", "## The night in one page", 1)
out = title + summ + "\n\n" + body
# the body's own references to "bottom-line item N" no longer resolve -> point them to the summary
out = out.replace("bottom-line item 1's limit", "the hard limit (summary item 1)")
out = out.replace("bottom-line item 4", "the gravity costs (summary item 6)")
open("FINAL_REPORT.md", "w").write(out)
import re
print("chars", len(out), "| words", len(out.split()), "| remaining 'bottom-line' refs:", len(re.findall("bottom-line", out)))
