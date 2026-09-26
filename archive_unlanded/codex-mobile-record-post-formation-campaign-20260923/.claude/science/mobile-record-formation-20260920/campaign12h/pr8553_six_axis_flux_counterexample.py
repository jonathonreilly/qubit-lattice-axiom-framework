#!/usr/bin/env python3
"""Exact scoped check of PR8553 T4 at head e07ae767d484763bd9446eb2d5c4c9b05643dd1c.

Computes all 49 ordered endpoint cases twice: from immutable streaming-event
momentum transfer and from the PR's own declared bond-flux implementation.
Also executes its family D, demonstrating the missing coverage. No repo edit.
"""
from pathlib import Path
from fractions import Fraction as F
from itertools import product
import hashlib,importlib.util,json

HERE=Path(__file__).resolve().parent
SNAPSHOT=Path('/Users/jonreilly/Documents/Codex/physics-sync-2026-09-20/pr-8553-sources')
V=[(0,0,0),(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
P=[F(x,65) for x in [18,12,3,18,2,6,6]]


def load(name,path,expected):
    assert hashlib.sha256(path.read_bytes()).hexdigest()==expected
    spec=importlib.util.spec_from_file_location(name,path);module=importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module);return module


def main():
    refuter=load('original_refuter',SNAPSHOT/'supervisor_control_block45_refuter.py',
        'bf8bc587d8742ecb6f78a479db6225ad57b3f2e4821292be59700822622738a4')
    runner=load('original_runner',SNAPSHOT/'admissibility_rule_the_wind_law_flux_theorems_inverse_square_wind_second_order_momentum_flux_force_product_of_capture_rates_2026_09_20.py',
        '203f00a3bc67ada6c2ca1fb7863f13750ce99e56e54c55625a2212a12cbd9ba8')
    assert sum(P)==1 and P[1]*P[2]==P[3]*P[4]==P[5]*P[6]
    g=[sum(P[a]*V[a][j] for a in range(7)) for j in range(3)]
    q=[P[2*j+1]+P[2*j+2] for j in range(3)]
    actual=[[F(0) for _ in range(3)] for _ in range(3)]
    source=[[F(0) for _ in range(3)] for _ in range(3)]
    scatter=[[F(0) for _ in range(3)] for _ in range(3)]
    for axis in range(3):
        left=(0,0,0);right=tuple(int(i==axis) for i in range(3));k=2*axis
        for a,b in product(range(7),repeat=2):
            probability=P[a]*P[b]
            rate=int(a==2*axis+1)+int(b==2*axis+2)
            for j in range(3): actual[axis][j]+=probability*rate*(V[a][j]-V[b][j])
            cfg={}
            if a: cfg[left]=a-1
            if b: cfg[right]=b-1
            original=refuter.bond_flux(cfg,left,k,F(1))
            for j in range(3): source[axis][j]+=probability*original[j]
            if a and b:
                loss=[F(V[a][j]) if b-1==((a-1)^1) else F(V[a][j]-V[b][j],2) for j in range(3)]
                for j in range(3): scatter[axis][j]+=probability*loss[j]
    expected=[[(q[i] if i==j else 0)-g[i]*g[j] for j in range(3)] for i in range(3)]
    assert actual==expected==source and all(v==0 for row in scatter for v in row)
    assert source[0][1]==-F(144,4225)!=0
    checks=runner.Checks();runner.family_d(checks)
    assert checks.failed==0
    result={'PR':8553,'head':'e07ae767d484763bd9446eb2d5c4c9b05643dd1c',
        'probabilities':[str(x) for x in P],'momentum':[str(x) for x in g],
        'tilted_product_witness':'Occupied weights proportional to (2,1/2,3,1/3,1,1), hence exp(lambda.s) with lambda=(log2,log3,0); opposite-pair weights equal, so the stated scattering adds zero mean flux.',
        'correct_exact_tensor':'Pi_ij=delta_ij*q_i-g_i*g_j for six-axis unit-rate streaming',
        'direct_event_tensor':[[str(x) for x in row] for row in actual],
        'original_bond_flux_tensor':[[str(x) for x in row] for row in source],
        'off_diagonal_counterexample':str(source[0][1]),
        'original_family_D_passes':checks.passed,
        'coverage_gap':'D2 and refuter W4 calculate only one-site mixed moments. The negative product of first moments contributed by exchange is omitted from their asserted conclusion about the full flux.',
        'scope':'Refutes the six-axis no-g_i_g_j statement in T4. Does not refute its anisotropy conclusion, the sphere calculation, the local continuity identities or measured sink forces.',
        'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
    (HERE/'PR8553_SIX_AXIS_FLUX_COUNTEREXAMPLE.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__': main()
