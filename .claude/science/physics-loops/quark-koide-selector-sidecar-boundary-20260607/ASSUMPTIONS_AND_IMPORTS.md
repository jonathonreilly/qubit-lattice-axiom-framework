# Assumptions And Imports

No new axiom is introduced.

Native inputs:

- Existing quark Koide comparator note and runner.
- Existing Record-selector audit sidecar and sidecar row classifier.
- Current audit ledger metadata as read-only source data.

Exposed imports that remain open:

- No framework-native quark mass scheme is derived.
- No quark scale, phase, amplitude ratio, or dial dynamics is derived.
- Charged-lepton BAE is not copied to the quark sector.
- CKM information is not turned into a mass theorem.

The sidecar runner is made tolerant of rows that advanced or were reopened after the historical selector split. It still requires each historical row to exist in the ledger, carry explicit metadata, and match a source-note anchor.
