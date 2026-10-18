"""Exact common-coordinate curvature certificate; no observational input."""
from pathlib import Path
from fractions import Fraction as F
import json
ROOT=Path(__file__).resolve().parents[1]
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['.claude/science/physics-loops/neutral-composite-24h-20261018/native/COMMON_METRIC_BOUNDARY.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/CHARGED_COLUMN_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/POLYNOMIAL_GRID_NEUTRAL_POLE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/ISOTROPIC_BOUND_FEATURE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/SIX_FLUX_DIAGONAL_MODE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/SECONDARY_NEUTRAL_MOLECULE_PROOF.md', '.claude/science/physics-loops/neutral-composite-24h-20261018/native/TEN_LAYER_NEUTRAL_BOUND_PROOF.md']
Delta=F(5,8);g=F(12155,33554432);D=F(15,512);v=F(90,32768);b=F(15,4096);d=F(1076510135,10567230160896);kappa=4*g*g/v;K=8*g*d/Delta-16*g*g*b/Delta**2
# Each tuple is (rest coefficient, rest exponent, energy-curvature coefficient, curvature exponent).
inputs={'charged':(Delta,4,g,10),'Q4':(Delta,4,kappa/2,12),'Q8':(2*Delta,4,F(5,2)*g*g/D,14),'Q6':(F(3,2)*Delta,4,K,18),'secondary':(2*Delta,4,F(5,2)*g*g/v,12)}
slopes={name:(2*m*t,em+et) for name,(m,em,t,et) in inputs.items()}
ratios={name:dict(coefficient=str(c/slopes['charged'][0]),power=e-slopes['charged'][1]) for name,(c,e) in slopes.items() if name!='charged'}
assert [ratios[x]['power'] for x in ('Q4','Q8','Q6')]==[2,4,8]
assert all(c>0 for c,e in slopes.values())
assert slopes['secondary'][0]/slopes['Q4'][0]==F(5,2)
from math import comb
heights=[]
for L in range(10,32,2):
 gamma=F(comb(2*L-2,L-1),8**(L-1));trap=F(9*L,32768)
 heights.append(dict(L=L,ratio_coefficient=str(2*gamma/trap),ratio_power=L-8))
assert F(9*8,32768)/(2*F(comb(14,7),8**7))==F(96,143)
rows=[]
for lam in (F(1,10),F(1,100),F(1,1000)):
 rows.append(dict(lam=str(lam),ratios={n:float(F(r['coefficient'])*lam**r['power']) for n,r in ratios.items()}))
out=dict(fixed_height_checks=heights,secondary_to_Q4_ratio='5/2',L8_binding_ratio='96/143',status='bounded-support',scope='Necessary common-relativistic-dispersion test of derived leading asymptotics; not measured/front velocities or all-regime exclusion',squared_energy_slopes={n:dict(coefficient=str(c),power=e) for n,(c,e) in slopes.items()},ratios=ratios,exposed_coefficient_examples=rows)
p=ROOT/'outputs/native_common_metric_boundary/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out))
