# Handoff

This branch repairs three audit-blocked runner lanes by demoting stale positive
closure wording to bounded-support / authority-boundary status while preserving
the exact arithmetic checks.

Claim movement:

- A2 below W2: exact source-literal arithmetic preserved; positive closure not
  certified.
- SU2 beta coefficient: exact `b_2 = 19/6` structural arithmetic preserved;
  textbook one-loop theorem left as explicit import.
- CKM/Koide cross-sector: exact `N_gen = N_color = 3` arithmetic preserved;
  positive closure not certified.

Reviewer focus:

- confirm demotion language is acceptable;
- confirm runner boundaries should be non-fatal;
- decide whether these rows can be requeued for audit as bounded support.

Do not land this as an audit verdict. The review/landing process should extract
the science and decide any queue changes separately.
