#!/usr/bin/env python3
"""Authenticate this packet's sources, actual executions, and quoted certificate."""
from pathlib import Path
import hashlib,json
import sympy as sp
HERE=Path(__file__).resolve().parent;ROOT=HERE.parent.parent
sources={
 'campaign12h_third/FINITE_FORMATION_WITH_RETAINED_FOURTH_ORDER_DYNAMICS.md':'002119d5a3f9bec171c3678cb15afdb91f7a763311ca38e6e4458ce10865572e',
 'campaign12h_fourth/second_event_independent/REPORT.md':'39e2b04f9140f10db8d8bbd178a086902d9b09f6854b0e317a663071bacf4582',
 'campaign12h_fourth/second_event_independent/operators.py':'a152167dff2cfff397397fcc56121cd9b2d79d7f412eb2e134f2f9cbbfa54c95',
 'campaign12h_fourth/second_event_independent/PRE_COMPARISON_SEAL.json':'e710cf956b2cff69afc8241757901c040a4c2f6b23516f09968cb372975bd734'}
def digest(p):return hashlib.sha256(p.read_bytes()).hexdigest()
for name,expected in sources.items():assert digest(ROOT/name)==expected
receipts=[]
for folder,prefix,script,exit_code in [(HERE,'EXPLORE','explore_fibers.py',0),
 (HERE,'QUARTER','exact_quarter_fiber.py',0),(HERE,'CUBE_POINT','cube_point_check.py',0),
 (HERE,'SECONDARY','check_prior_and_certificate.py',0),
 (HERE/'failed_attempts/domain_equality','CUBE_POINT','cube_point_check.py',1)]:
 r=json.loads((folder/(prefix+'_RECEIPT.json')).read_text())
 assert r['exit_code']==exit_code
 for key,path in [('script_sha256',folder/script),('stdout_sha256',folder/(prefix+'.stdout')),('stderr_sha256',folder/(prefix+'.stderr'))]:
  assert digest(path)==r[key]
 receipts.append({'path':str((folder/(prefix+'_RECEIPT.json')).relative_to(HERE)),'exit_code':exit_code,'bindings_verified':3})
assert (HERE/'CUBE_POINT_RESULTS.json').read_bytes()==(HERE/'CUBE_POINT.stdout').read_bytes()
assert (HERE/'SECONDARY_RESULTS.json').read_bytes()==(HERE/'SECONDARY.stdout').read_bytes()
x=sp.Symbol('lambda');data=json.loads((HERE/'CUBE_POINT_RESULTS.json').read_text());p=data['modular_certificate']['prime']
f,g=[sp.Poly.from_list([int(v) for v in row['charpoly_coefficients']],x,domain=sp.ZZ) for row in data['fibers']]
assert sp.gcd(f,g).as_expr()==1
c=x**3+25*x*x+176*x+248;r=-319*x*x-357*x+185
assert sp.Poly((437*x-475)*c+(33*x*x+135*x+15)*r-1,x,modulus=p).is_zero
assert sp.Poly(g.as_expr(),x,modulus=p).rem(sp.Poly(c,x,modulus=p))==sp.Poly(r,x,modulus=p)
for k,value in data['modular_certificate']['second_polynomial_at_zero_fiber_integer_roots'].items():assert int(g.eval(int(k)))%p==value
assert data['normalizable_localized_flux_countercontrol']['variance_H2']=='56/9'
print(json.dumps({'sources_verified':sources,'execution_receipts_verified':receipts,'results_equal_full_stdout':True,
 'report_compact_certificate_verified':True,'gcd_exact':'1','failures_preserved':1,
 'read_boundary':'Only the allowed model and own prior packet; no current author cube-point or excluded packet read.'},indent=2))
