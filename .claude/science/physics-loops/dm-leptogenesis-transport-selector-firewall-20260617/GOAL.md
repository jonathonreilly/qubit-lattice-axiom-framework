# Goal

Repair the source surface for
`dm_leptogenesis_pmns_transport_extremal_source_candidate_note_2026-04-16`,
which is currently `audited_numerical_match`.

The source-side issue is not the interval computation.  The issue is that the
interpolated `eta/eta_obs = 1` point can be overread as a physical selector.
This block makes the root explicitly diagnostic and adds a small no-go/firewall
showing that an intermediate-value crossing is not a source-selection theorem.

No audit verdict, ledger row, queue row, or generated audit status was changed.
