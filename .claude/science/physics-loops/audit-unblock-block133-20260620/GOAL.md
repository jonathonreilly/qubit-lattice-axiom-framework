# Goal

Make runner-path canonicalization preserve nested `scripts/...` subpaths from
stale absolute worktree paths.

Before this block, paths like:

```text
/tmp/old-worktree/scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py
```

stayed absolute and stale even though the checked-out repo has:

```text
scripts/corrections/yt_p1_delta_r_corrected_bound_memsafe.py
```

This block updates the three local canonicalizers that audit packet rendering,
helper dependency discovery, and precompute cleanup use.
