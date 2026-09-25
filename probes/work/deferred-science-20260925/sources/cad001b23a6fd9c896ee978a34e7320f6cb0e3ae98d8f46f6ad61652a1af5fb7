from pathlib import Path
import hashlib,json,time
import mpmath as mp

start=time.perf_counter();mp.mp.dps=70
h=mp.mpf('6.62607015e-34');e=mp.mpf('1.602176634e-19');c=mp.mpf('299792458')
hbar_GeV_s=h/(2*mp.pi*e*10**9)
rows=[]
for label,limit in [('MAGIC2017','5.9e10'),('LHAASO2024_v2_ML_MINOS','6.9e11')]:
    tau=6*hbar_GeV_s/mp.mpf(limit)
    rows.append({'benchmark':label,'E_QG2_lower_GeV':limit,
      'orientation_independent_necessary_a_upper_m':str(c*tau),
      'necessary_tau_upper_seconds':str(tau),
      'status':'Conditional published timing conversion; no selected scale or new fit.'})
out={'scope':'SI arithmetic only; inequalities proved analytically in the root note.',
     'rows':rows,'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
     'elapsed_seconds':time.perf_counter()-start}
Path(__file__).with_name('UNIT_CONVERSIONS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
