# Goal

Repair the current `record_axiom_audit_application_map_2026-06-06` failed
runner/cache without changing audit results.

The audit blocker was narrow: two `flavor_det_character_selection` anchor
phrases in the classifier were stale after the source note was repaired. The
goal is to make the runner check the current load-bearing source language and
refresh the cache.
