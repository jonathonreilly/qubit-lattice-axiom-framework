# Block24 mutation-tail source repin

The independently static-accepted Locked-forward fixture repair was committed
before target execution at
`4cd86e4171c2bd477f418f4381c764162158cb50`.

```text
f98534f07655e0de296f2060932e34aa7a600f08545f3661be2843d05accc15d  scripts/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30.py
```

The ten declared execution inputs have frozen pre-run fingerprint:

```text
7d9070dc0748121fa237a2d29dc2030028f8cec7114b614091ead7c7f867ffb7
```

The only permitted execution of this source revision is one content-bound
launch with its exact result preserved without overwrite at:

```text
logs/runner-cache/admissibility_d4_self_delimiting_forward_record_append_history_2026_08_30_terminal.txt
```

The controller may use the absent canonical path as an atomic staging location
for `runner_cache` and then move those exact bytes once to the named path. It
must capture merged stdout/stderr, reject source or declared-input changes
across execution, preserve any nonzero or timeout result, and refuse to
overwrite either path. All three earlier attempts remain preserved at their
distinct historical cache paths.

Any source or declared-input edit after this repin requires a new commit,
fingerprint, pin, and cache path before another execution. This repin is not a
runner result, audit verdict, obligation retirement, or TOE-score move.
