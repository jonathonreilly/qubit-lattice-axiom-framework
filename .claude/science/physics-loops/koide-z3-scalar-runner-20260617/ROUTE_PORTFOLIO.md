# Route Portfolio

| Route | Score | Reason | Outcome |
|---|---:|---|---|
| Replace small SciPy utilities in the existing runner with local NumPy/bisection/golden-section routines | 3 | Directly repairs the compute blocker while preserving the existing proof surface. | selected |
| Add only `Primary runner` metadata | 1 | Would still leave the runner blocked by SciPy import failure. | rejected |
| Create a new wrapper runner | 1 | Would avoid touching the old runner but leave the audited source artifact stale. | rejected |
| Claim charged-lepton tower closure | 0 | The note explicitly records the physical selector and scale gaps. | rejected |
