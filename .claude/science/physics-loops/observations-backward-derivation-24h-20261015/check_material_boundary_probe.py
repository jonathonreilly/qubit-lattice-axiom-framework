#!/usr/bin/env python3
"""Small conditional boundary calculation; no empirical observations."""
import hashlib,json
from pathlib import Path
import sympy as s
AUDIT_TIMEOUT_SEC = 120
p=Path(__file__).resolve().parent
x,k,rho=s.symbols('chi k rho',positive=True)
A=s.symbols('A',real=True)
f=rho/(2*k)+A/s.cos(s.sqrt(k)*x)**2
z=s.simplify(s.trigsimp(s.sqrt(k)*s.cot(s.sqrt(k)*x)*s.diff(f,x)-(2*k*f-rho)))
f0=rho/(2*k);v0=rho/2
rows={'proper_radius_transport':z,'constant_time_equation':s.simplify(-3*k*f0+rho+v0),'constant_spatial_equation':s.simplify(-k*f0+v0),'constant_scalar_equation':s.simplify(6*k/2-3*k),'divergent_amplitude':s.simplify(s.cos(s.sqrt(k)*x)**2*(f-f0)-A)}
# A constant F inconsistent with the measured stress/curvature must fail the
# source equation; a wrong potential slope must fail the scalar equation.
mutants={'wrong_constant_value':s.simplify(2*k*(2*f0)-rho),'wrong_potential_slope':s.simplify(6*k/2-6*k)}
out={'kind':'small conditional author probe; focused check pending','source_sha256':hashlib.sha256((p/'BLOCK03_BOUNDARY_PROBE_v1.md').read_bytes()).hexdigest(),'runner_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'sympy':s.__version__,'identities':{n:str(v) for n,v in rows.items()},'mutations':{n:str(v) for n,v in mutants.items()},'pass':all(v==0 for v in rows.values()) and all(v!=0 for v in mutants.values()),'empirical_validation':False}
(p/'BLOCK03_BOUNDARY_CONTROLS_v1.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
raise SystemExit(0 if out['pass'] else 1)
