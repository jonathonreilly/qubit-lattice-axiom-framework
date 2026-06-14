# Opportunity Queue

1. `pmns_graph_first_axis_alignment_note`: direct local repair by complex
   normal-form restatement. Completed in this branch.
2. Downstream PMNS graph-first rows can be revisited after independent audit
   decides whether this row becomes clean enough to propagate.
3. Remaining conditional rows should be selected from the refreshed audit scan
   after this PR is opened; avoid mixing independent repairs into this branch.
