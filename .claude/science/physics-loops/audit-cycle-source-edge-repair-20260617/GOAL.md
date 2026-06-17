# Goal

Remove false source-note dependency edges that currently appear in the audit
cycle inventory without changing audit verdicts, claim statuses, or scientific
content.

The repair is source-side only: peer/downstream pointers that were not
load-bearing authorities are changed from markdown links into plain/backticked
non-authority references.
