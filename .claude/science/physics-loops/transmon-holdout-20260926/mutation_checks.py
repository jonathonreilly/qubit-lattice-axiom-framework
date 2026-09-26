"""Scratch-only fault injection against the published guards; no production edits."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from pathlib import Path
import sys, json, types, tempfile, hashlib
ROOT=Path(__file__).resolve().parents[4]
sys.path.insert(0,str(ROOT/'scripts'))
import transmon_calibration_holdout_2026_09_26 as r
import transmon_resonator_model_2026_09_26 as m
import numpy as np
log=(ROOT/'logs/runner-cache/transmon_calibration_holdout_2026_09_26.txt').read_text()
result=json.JSONDecoder().raw_decode(log[log.index('{\n'):])[0]
p=np.array(result['parameters']); target=np.array([result['calibration'][k] for k in r.CAL_KEYS])
checks=[]
def reject(name,fn):
    try: fn()
    except (AssertionError,ValueError) as e:
        checks.append({'mutation':name,'detected':True,'failure':str(e)})
    else: raise RuntimeError('UNDETECTED '+name)
def module(text):
    out=types.ModuleType('scratch');exec(compile(text,'<scratch mutation>','exec'),out.__dict__);return out
source=(ROOT/'scripts/transmon_resonator_model_2026_09_26.py').read_text()
with tempfile.TemporaryDirectory() as tmp:
    original=r.DATA; r.DATA=Path(tmp)/'Experiment.csv';r.DATA.write_bytes(original.read_bytes()+b'\n')
    reject('changed upstream data byte',r.main);r.DATA=original
# Force optimizer budget exhaustion rather than silently accepting an unfit point.
original_lsq=r.least_squares
def underfit(*a,**kw): kw['max_nfev']=1;return original_lsq(*a,**kw)
r.least_squares=underfit
reject('one-evaluation uncalibrated optimizer',lambda:r.fit_calibration(target,[.25,20,7.5,.08]));r.least_squares=original_lsq
# Exercise found-root consistency with one stale root, leaving its assertion intact.
original_fit=r.fit_calibration;calls=[0]
def stale(*a,**kw):
    calls[0]+=1;pp=p.copy();pp[0]+=.01*(calls[0]==2);return pp,0.
r.fit_calibration=stale
reject('one inconsistent saved calibration root',lambda:r.construct_predictions(result['calibration']));r.fit_calibration=original_fit
bad=module(source.replace('g*scale_G*np.kron','0.5*g*scale_G*np.kron'))
direct=r.independent_predict(p)[0]
def compare_operator():
    difference=max(abs(bad.predict(p)[0]-direct))*1000
    assert difference<.001,('independent comparison MHz',difference)
reject('halve primary capacitive coupling matrix',compare_operator)
def cutoff():
    difference=max(abs(m.predict(p,14,8,2)[0]-m.predict(p,40,24,20)[0]))*1000
    assert difference<.001,('cutoff shift MHz',difference)
reject('underresolve photon and transmon basis',cutoff)
badlabels=module(source.replace("ix=[int(np.argmax(abs(vec[k*M+j,:])**2)) for k,j in targets]","ix=[0 for k,j in targets]"))
reject('collapse spectral assignment to ground level',lambda:badlabels.predict(p))
# Isolate the evaluation guard after the already verified prediction stage.
original_construct=r.construct_predictions;r.construct_predictions=lambda _:result.copy()
with tempfile.TemporaryDirectory() as tmp:
    original=r.DATA; oldhash=r.SOURCE_SHA256;r.DATA=Path(tmp)/'Experiment.csv'
    import csv,io
    rows=list(csv.DictReader(original.read_text().splitlines()))
    for row in rows:
        if row['Experiment']=='KIT':row['f05']='nan'
    stream=io.StringIO();writer=csv.DictWriter(stream,fieldnames=list(rows[0]));writer.writeheader();writer.writerows(rows)
    r.DATA.write_text(stream.getvalue());r.SOURCE_SHA256=hashlib.sha256(r.DATA.read_bytes()).hexdigest()
    reject('omit available fifth-level evaluation line',r.main)
    r.DATA=original;r.SOURCE_SHA256=oldhash
r.construct_predictions=original_construct
print(json.dumps(checks,indent=2));print('All seven injected faults detected; guard tests are not empirical evidence.')
