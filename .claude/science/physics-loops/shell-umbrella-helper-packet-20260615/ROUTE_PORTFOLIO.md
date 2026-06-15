# Route Portfolio

## Route A: Add only `Runner:` link

Not sufficient. The primary runner dynamically loads helpers; audit packets
would still omit the helper sources.

## Route B: Add explicit helper-path registration

Selected and implemented. This matches the wrapper note's purpose and keeps the
restricted audit packet complete.

## Route C: Refactor dynamic imports into static imports

Not selected. It would be higher blast radius than needed for packet
visibility.
