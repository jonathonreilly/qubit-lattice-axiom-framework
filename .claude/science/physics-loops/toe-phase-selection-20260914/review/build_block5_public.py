#!/usr/bin/env python3
"""Assemble one public runner from personally checked mathematical prototypes."""
from pathlib import Path
import re

PACK=Path(__file__).resolve().parent.parent
DELIVERY=Path('/Users/jonreilly/Documents/Codex/toe-causal-gaussian-likelihood-20260914')
STEM='permanent_local_gaussian_likelihood_protocol_2026_09_14'


def main_body(filename,name):
    text=(PACK/filename).read_text().split('\ndef main():',1)[1].split("\n\nif __name__",1)[0]
    text=re.sub(r'^    Path\(__file__\).*\n','',text,flags=re.M)
    text=re.sub(r'^    print\(json.dumps\(.*\n','',text,flags=re.M)
    returned='rows' if filename=='block5_causal_wire_check.py' else 'result'
    return '\ndef '+name+'():'+text+'\n    return '+returned+'\n'


def main():
    sections=['''#!/usr/bin/env python3
"""Supplied local permanent Gaussian likelihood programs and posterior costs.

All new geometry, carrier, Gaussian and bound checks are defined here. The
two declared scientific inputs define the current finite source matrices;
their historical theorem/audit claims are not invoked. The constructed roots
are commuting complex random variables. Source, program, schedule and later
conditioning are supplied; no native action, Born law or phase is selected.
"""
from collections import Counter, defaultdict
from dataclasses import dataclass
from hashlib import sha256
from itertools import product
import itertools
import json
from math import isqrt
from pathlib import Path
import sys

import numpy as np
import sympy as s

AUDIT_TIMEOUT_SEC = 180
AUDIT_INPUT_PATHS = (
    'scripts/admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10.py',
    'scripts/admissibility_dirac_kahler_shifted_origin_frame_gauge_nonuniform_hodge_overlap_2026_08_14.py',
)
INPUT_SHA256 = (
    '8d2e071da05f0e540c8ec061b5dbea6cb996040a33b90efcd2f6e11b73d52cd2',
    '5499cc2c1a75f19e07b717aeb6c9ef7779c45e1c5757d84701c5d88ca92bf445',
)
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'scripts'))
import admissibility_dirac_kahler_strict_neighbor_m2_gaussian_compiler_released7333_fixture_2026_09_10 as source
''']
    geometry=(PACK/'block4_periodic_routing_check.py').read_text()
    sections.append(geometry[geometry.index('@dataclass'):geometry.index('    def coordinates(')])
    wires=(PACK/'block5_causal_wire_check.py').read_text()
    wires=wires[wires.index('SCALE=10'):wires.index('\ndef main():')]
    wires=wires.replace('    print(json.dumps(result,indent=2),flush=True)\n','')
    sections.append(wires)
    sections.append(main_body('block5_causal_wire_check.py','causal_wire_checks'))
    local=(PACK/'block5_local_rule_window_check.py').read_text()
    sections.append(local[local.index('PAULI='):local.index('\ndef main():')])
    sections.append(main_body('block5_local_rule_window_check.py','local_rule_window_checks'))
    likelihood=(PACK/'block5_dk_likelihood_check.py').read_text()
    sections.append(likelihood[likelihood.index('def clean('):likelihood.index('\ndef main():')])
    sections.append(main_body('block5_dk_likelihood_check.py','dk_likelihood_checks'))
    sections.append(main_body('block5_source_coercivity_check.py','source_coercivity_checks'))
    sections.append('''
def main():
    for path,expected in zip(AUDIT_INPUT_PATHS,INPUT_SHA256):
        assert sha256((ROOT/path).read_bytes()).hexdigest()==expected, ('source input drift',path)
    result=dict(causal_wires=causal_wire_checks(),
                local_rule_and_windows=local_rule_window_checks(),
                supplied_dk_likelihood=dk_likelihood_checks(),
                uniform_source_coercivity=source_coercivity_checks(),
                scientific_input_paths=list(AUDIT_INPUT_PATHS),
                status='author_checked; independent_review_pending',
                open='source/program/schedule selection, typical phase, original native Record-star weights, quantum or fermion identification')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
''')
    output='\n\n'.join(sections).replace('block5-coercivity','source-coercivity').replace('block5-likelihood','source-likelihood')
    target=DELIVERY/'scripts'/f'{STEM}.py'
    target.write_text(output)
    print(target)


if __name__=='__main__':
    main()
