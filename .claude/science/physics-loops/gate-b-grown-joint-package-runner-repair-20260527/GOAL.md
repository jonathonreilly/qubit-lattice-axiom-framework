# Goal

Repair the conditional audit blocker on `gate_b_grown_joint_package_note`.

The blocker was a bounded numerical artifact mismatch: the source note froze
old Born values while the current SHA-pinned runner cache reports updated
values. The note also still described `GATE_B_FARFIELD_NOTE.md` as
conditional even though the current ledger has it retained-bounded.
