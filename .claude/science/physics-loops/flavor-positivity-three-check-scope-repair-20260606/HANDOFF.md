# Handoff

This PR repairs the row by narrowing it to the three checks actually supported
by the runner. It intentionally does not add a new axiom, does not edit audit
results, and does not claim to finish the flavor-selection problem.

Reviewer focus:

- Confirm the old exhaustion/campaign-capstone claim is gone from both note and
  runner output.
- Confirm the remaining claim is exactly the three algebraic checks.
- Confirm the refreshed runner cache matches the edited runner.
