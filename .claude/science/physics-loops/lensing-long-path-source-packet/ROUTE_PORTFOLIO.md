# Route Portfolio

## Route A: Primary runner imports long-path packet

Status: chosen.

Import `lensing_long_path_test.py` from the primary analytical runner and check
the SHA-pinned cache for the short-path facts named by the audit blocker.

## Route B: Manifest-only repair

Status: insufficient.

The manifest already passed on main, but the audited row still had no helper
source path. The primary runner needed to expose the long-path packet directly.

## Route C: Detector-centroid derivation

Status: not attempted.

This is broader science and remains the honest open bridge.
