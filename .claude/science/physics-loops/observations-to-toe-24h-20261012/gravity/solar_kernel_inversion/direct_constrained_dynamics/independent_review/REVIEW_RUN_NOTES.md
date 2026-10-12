Reviewer-control development notes, 2026-10-12.

An initial whole-dictionary equality check between author v1 and v2 candidate outputs failed because v2 adds two binary64-bound fields. Inspection showed all previously present candidate fields were exactly unchanged. The final independent check compares every old field and requires exactly those two additions.

The first independent-control execution also used Python structural equality for two differently factored SymPy representations of the same derivative. It was corrected to simplify their difference and require zero. The mathematical derivative was unchanged. The subsequent complete independent run passed and its script hash is recorded in independent_dynamics_checks_v1.json. Neither development issue was a failure of the author's equations or arithmetic.
