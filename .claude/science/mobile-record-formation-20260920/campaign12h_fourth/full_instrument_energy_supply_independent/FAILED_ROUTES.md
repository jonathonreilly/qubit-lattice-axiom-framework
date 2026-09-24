# Preserved failures and rejected routes

The initial executable snapshot `RUN_01_control.py` failed before execution
with `SyntaxError: unmatched ']'` in the list comprehension that lists a
vector-charge sector. `RUN_01.stderr.log`, its empty stdout and its receipt
are preserved. Removing the extra closing bracket was the only change before
`RUN_02`, which completed every assertion. No scientific conclusion came from
the failed run.

The following analytical shortcuts were rejected before PRE:

- Replacing an infinite translation by a cyclic finite shift violates exact
  energy conservation at the wrap. Its numerical negative control has
  translation-identity defect norm 5 on a five-level ladder.
- Treating the shared reservoir as freshly prepared after each step omits
  correlations. The completed sequence control retains those correlations.
- Replacing the GKLS semigroup by the naive Euler map need not be completely
  positive. Amplitude damping at step 0.2 gives Choi minimum eigenvalue
  -0.005538513813741661. The square-root Kraus step is used instead.
- Using a fixed trace error to infer microscopic energy moments under a
  diverging Hamiltonian norm is invalid. The resource choice scales the
  channel error against the desired moments.
- Promoting a scheduled finite gate sequence to an autonomous time-independent
  environment, or promoting reduced-channel convergence to equality of exact
  event-time histories, has no proof here and is not asserted.

These are route limitations under named premises, not a general reservoir
no-go. No no-go conclusion is being shipped.
