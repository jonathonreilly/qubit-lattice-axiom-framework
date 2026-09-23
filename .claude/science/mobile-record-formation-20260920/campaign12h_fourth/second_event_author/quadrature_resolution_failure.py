"""Preserved resolution assertion first attempted in a read/inspection cell.

This deliberately reproduces the recorded failure. It does not alter the
underresolved outputs or claim the 128-point grid controls eta=320,t=.7.
"""
from pathlib import Path
import json
d=json.loads(Path(__file__).with_name('SECOND_EVENT_VALIDATION_RESULTS.json').read_text())
for r in d['quadrature_rows']:
    if r['grid']!=256:continue
    match=next(x for x in d['quadrature_rows'] if x['grid']==128 and
               all(x[k]==r[k] for k in ('coherent_first','eta','t','normalizable_field')))
    assert abs(match['survival']-r['survival'])<1e-8,(r,match)
