# Result Adjudication

The Stage-0 synchronizer proposed in Preregistration Amendment 1 does not
belong to that amendment's declared action/support-strong-fair scheduler
class.

In the six-row quotient, `FIRST_GO` has both the retry row for seam 2 and the
positive completion row for seam 1.  The synchronizing policy visits
`FIRST_GO` in every round, always chooses seam 2, and never chooses completion.
Completion is therefore recurrently enabled and selected zero times.  The
policy is nonanticipating and weakly fair with almost-sure finite delays, but
it is not action-strongly-fair.

The corrected exact result is:

- under weak finite-delay fairness, the synchronizer induces a closed
  nonterminal recurrent class and has zero absorption;
- under the preregistered action/support strong fairness, exhaustive closure
  of the six-row quotient finds no nonterminal fair recurrent class;
- for every supplied `0<p<1`, the quotient therefore absorbs almost surely;
- no expected-time, uniform-rate, infinite-volume, physical-time or
  law-selection result follows;
- the quotient binds but does not execute the local rollback-safety boundary,
  and only the retry-projector Kraus identity is compiled.

Decision class:
`positive-two-arm-action-strong-fair-quotient-absorption`.

The full local dynamic compiler remains the highest-value route.  Deterministic
component coalescence/root locking remains the precommitted fallback if the
physical table exposes an alias, orphan, restoration defect, CP failure or a
genuine action-fair nonterminal component.
