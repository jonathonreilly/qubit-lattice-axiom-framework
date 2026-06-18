# Goal

Unblock audit handling for `assumption_derivation_ledger` by making the
existing meta-firewall runner explicit and stronger.

The branch does not audit the row, edit audit data, or convert the ledger into
an authority surface. It only registers and verifies the source boundary: the
ledger is metadata, not a proof of any ingredient status.
