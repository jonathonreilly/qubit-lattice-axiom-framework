# Goal

Repair `persistent_record_as_kraus_operator_note_2026-05-20` enough to make it independently auditable again.

The target is bounded support: attach a finite-dimensional certificate showing that a normalized linear record-writing isometry

```text
W : H_sys -> H_sys x H_record
```

induces record blocks `K_r` that satisfy the Kraus completeness relation, produce normalized selective updates, and define a CPTP unconditional channel.

This block must not claim asymptotic record-formation closure, must not change the downstream Born-rule row, and must not assign an audit verdict locally.
