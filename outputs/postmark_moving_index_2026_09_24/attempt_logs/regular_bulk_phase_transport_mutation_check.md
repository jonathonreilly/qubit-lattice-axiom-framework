# Regular-bulk phase-transport runner mutation checks

These author-side mutations were applied in memory after importing the paired runners; no source files were edited by the mutation step.

- Replaced the displayed local second-order polynomial by zero: rejected by second-order trace coefficient identity.
- Added one to the Berry-connection formula: rejected by symbolic Berry connection identity.
- Shifted the selected local eigenphase branch by pi: rejected by positive-flux eigenbasis normalization.

These checks test fail-closed behavior only. They are not independent review receipts or formal audit results.
