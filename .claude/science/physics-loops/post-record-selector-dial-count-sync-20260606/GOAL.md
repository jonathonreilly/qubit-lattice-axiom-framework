# Goal

Repair the source/count drift blocking
`post_record_selector_dial_bucket_subdivision_2026-06-06`.

This branch is stacked on the evidence ladder count sync because the selector
subdivision source anchor now correctly depends on
`selector_or_dial_needed | 241`.
