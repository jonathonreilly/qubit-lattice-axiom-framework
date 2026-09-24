# Retained operational failure

Before `post_governance.py`, a one-off inline governance refresh used
`repo=Path.cwd().parents[3]` from the independent directory. That was the
`.claude` directory, rather than the repository root. The initial guard failed:

```
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
AssertionError: /Users/jonreilly/Documents/Codex/mobile-record-formation-20260920/.claude
```

Exit code was 1. The guard preceded all git/source reads and all output writes.
The replacement finds the ancestor containing both AGENTS.md and the science
workflow; it changes no premise hash or comparison requirement. This was an
operational path-resolution error, not a scientific test failure.
