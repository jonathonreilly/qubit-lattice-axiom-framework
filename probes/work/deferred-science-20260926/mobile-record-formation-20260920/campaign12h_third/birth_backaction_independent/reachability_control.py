#!/usr/bin/env python3
"""Contrast dark-state existence with empty-start accessibility on the square."""
import sys
sys.dont_write_bytecode = True
from pathlib import Path
import json
import sympy as s
from check import one_color_operators

HERE = Path(__file__).resolve().parent
edges = [(0,1),(1,2),(2,3),(0,3)]
H,L = one_color_operators(4,edges,edges,1,1,0)
v = s.zeros(16,1)
v[5],v[10] = 1,-1
dark = v*v.T/2
assert L.conjugate().T*dark.vec() == s.zeros(256,1)
empty = s.zeros(16)
empty[15,15] = 1
assert (dark*empty).trace() == 0
for x,y in edges:
    output_mask = 15 ^ (1<<x) ^ (1<<y)
    assert v[output_mask] == 0
result = {'square_dark_projector_is_conserved_without_monitoring':True,
          'empty_initial_dark_weight':'0',
          'each_first_birth_state_dark_overlap':'0',
          'consequence':'The specified square dark state is inaccessible from the all-vacant square without monitoring. Its existence alone does not show empty-start failure. The separate N4-torus matching history supplies the required positive reachability witness.'}
(HERE/'REACHABILITY_CONTROL_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result,indent=2))
