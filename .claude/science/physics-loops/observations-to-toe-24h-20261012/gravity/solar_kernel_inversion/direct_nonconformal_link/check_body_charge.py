#!/usr/local/bin/python3
"""Direct supplied-orbit sensitivity check; separate from original execution."""
import json,math,hashlib,datetime
from pathlib import Path
import numpy as np
from scipy.integrate import quad

rows=[]
speed=6**(-.2); c=1000.;cs=speed*c;mu=.25;contrast=.001
for e in [0,.2,.6,.8]:
    def acceleration_power(E):
        u=1-e*math.cos(E)
        X=np.array([math.cos(E)-e,math.sqrt(1-e*e)*math.sin(E),0.])
        Dddot=-mu*contrast*X/np.linalg.norm(X)**3
        return float(Dddot@Dddot)*u/(2*math.pi*3*cs**3)
    actual=quad(acceleration_power,0,2*math.pi,epsabs=1e-29,epsrel=3e-13)[0]
    formula=mu**2*contrast**2/(3*cs**3)*(1+e*e/2)/(1-e*e)**2.5
    assert abs(actual/formula-1)<1e-11
    f=(1+73*e*e/24+37*e**4/96)/(1-e*e)**3.5
    GR=32/5*mu**2/c**5*f
    formula_ratio=5/96*contrast**2*speed**-3*c*c*(1+e*e/2)*(1-e*e)/(1+73*e*e/24+37*e**4/96)
    assert abs(actual/GR-formula_ratio)<1e-12
    rows.append({'eccentricity':e,'direct_power':actual,'formula_power':formula,'additional_ratio_to_GR':actual/GR})
source=Path(__file__);result={'at':datetime.datetime.now(datetime.timezone.utc).isoformat(),'status':'PASS supplied-orbit charge sensitivity only','source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),'note_sha256':hashlib.sha256(source.with_name('BODY_CHARGE_SENSITIVITY.md').read_bytes()).hexdigest(),'premise':'eta contrast is illustrative; no extended-body or passive-charge model','c':c,'cs':cs,'a':1,'G_N':1,'M':1,'mu':mu,'delta_eta':contrast,'rows':rows}
with source.with_name('evidence_v1').joinpath('BODY_CHARGE_RESULTS.json').open('x') as f:json.dump(result,f,indent=2);f.write('\n')
print(json.dumps(result,indent=2))
