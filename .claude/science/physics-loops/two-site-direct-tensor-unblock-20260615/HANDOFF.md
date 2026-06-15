# Handoff

This PR removes the conditional `MULTISITE_PAULI_GROUP` dependency from the
two-site tensor/local-tomography chain.

The two-site note now constructs the needed Pauli products directly on
`C^2_x tensor_C C^2_y`; the local-tomography note routes directly through
retained per-site and finite-block tensor-product inputs. Both companion
runners check retained dependency status and exact matrix algebra.

Local pipeline simulation made both edited rows `unaudited` and ready for
audit, moving `retained_pending_chain` from 20 to 18 and ready rows from 1 to
3. No generated audit verdict/status files are part of the PR.
