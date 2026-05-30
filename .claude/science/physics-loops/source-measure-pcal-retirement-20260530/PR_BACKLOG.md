# PR Backlog

PR should be opened after commit/push.  Required checks passed:

```text
python3 scripts/frontier_source_measure_pcal_rn_cocycle.py
python3 scripts/frontier_source_measure_pcal_cumulant_mobius.py
python3 scripts/frontier_source_measure_sharp_record_tangent_space.py
python3 scripts/frontier_source_measure_pcal_retirement_synthesis.py
```

Then push branch:

```text
git push -u origin physics-loop/source-measure-pcal-retirement-block01-20260530
```

and open a review PR titled:

```text
[physics-loop] source-measure P-cal RN cocycle exact-support
```

Recommended title after synthesis:

```text
[physics-loop] source-measure P-cal exact-support synthesis
```
