from pathlib import Path
import hashlib,json,time
import mpmath as mp
start=time.perf_counter();mp.mp.dps=65
EQ=mp.mpf('6.9e11')*10**9
rows=[]
for L in [6,8,16]:
 rows.append({'L':L,'reference_energy_necessary_lower_eV':str(EQ/3*mp.sin(mp.pi/L)),'strict_inequality':True})
optical=[]
for E in ['1','2','3']:
 ratio=3*mp.mpf(E)/EQ
 optical.append({'supplied_reference_energy_eV':E,'necessary_L_strict_lower':str(mp.pi/mp.asin(ratio))})
out={'scope':'Conditional arithmetic; no actual charged spectrum, empirical fit or independent verification.','benchmark_EQG_lower_eV':str(EQ),'fixed_volume_rows':rows,'optical_rows':optical,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start}
Path(__file__).with_name('FINITE_VOLUME_UNITS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
