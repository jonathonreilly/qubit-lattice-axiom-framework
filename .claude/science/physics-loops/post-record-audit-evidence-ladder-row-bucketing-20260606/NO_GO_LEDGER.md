# No-Go Ledger

## NG-001: Bucket to verdict

A bucket is not an audit verdict. It only identifies the evidence type a row
appears to need.

## NG-002: Read-only companion to audit edit

The runner verifies the audit ledger hash is unchanged. Any audit data edit is
out of scope.

## NG-003: Selector bucket to forced dial

Rows in `selector_or_dial_needed` need selector review. The bucket does not
force or select a generation/Koide dial.

## NG-004: Simulation bucket to p-value

Rows in `simulation_support_only` remain support-only unless they provide a
finite certificate or explicit statistical protocol.
