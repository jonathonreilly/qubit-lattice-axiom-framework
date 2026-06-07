# Route Portfolio

1. Full recomputation for `lattice_3d_l2_tail_stats.py`.
   - Tried first.
   - Rejected for default audit mode: CPU-bound, silent after the old 120 s
     timeout, and mismatched to the note's narrowed frozen-log claim.

2. Frozen-log verifier for `lattice_3d_l2_tail_stats.py`.
   - Selected.
   - Checks the exact width-8 table and recomputes the tail fit from the
     frozen rows in 0.05 s.

3. Higher declared timeout plus cache refresh for existing slow runners.
   - Selected for `fm_transfer_grown_companion.py` and
     `persistent_record_matched_compare.py`.
   - Both now have fresh `status: ok` caches.
