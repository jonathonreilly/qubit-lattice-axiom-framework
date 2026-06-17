# Route Portfolio

| Route | Score | Reason | Outcome |
|---|---:|---|---|
| Add a conservative contract runner for `YT_FLAGSHIP_BOUNDARY_NOTE.md` | 3 | Directly closes the queue blocker `runner_path=null` without changing audit status or overclaiming YT closure. | selected |
| Rework the old `frontier_yt_boundary_consistency.py` as the flagship runner | 1 | Existing script contains stale stronger closure/update language and SciPy dependency; higher overclaim risk. | rejected for this PR |
| Try to prove full YT UV-to-IR retained closure | 1 | High scientific value, but not tractable as a small audit unblock and would risk hidden standard-method imports. | left as future frontier lane |
| Retag the audit row manually | 0 | Forbidden by user contract; audit owns row status. | rejected |
