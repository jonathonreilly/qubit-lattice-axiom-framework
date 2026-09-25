from pathlib import Path
import hashlib,json,time
import mpmath as mp
start=time.perf_counter();mp.mp.dps=65
h=mp.mpf('6.62607015e-34');c=mp.mpf('299792458');e=mp.mpf('1.602176634e-19');hbar=h/(2*mp.pi)
EQ=mp.mpf('6.9e20');tau=6*hbar/(e*EQ);b=mp.mpf('1e-9')
out={'scope':'Conditional unit conversions; no experimental-state fit or exact spectral-support claim.','spectral_endpoint_rows':[{'wavelength_nm':n,'energy_eV':str(h*c/(e*mp.mpf(n)*mp.mpf('1e-9')))}for n in ['637','800']],'supplied_mean_reference_energy_ceiling_eV':'2','mean_energy_limiting_relative_excess_upper':str(4*mp.sqrt(3)*mp.mpf('2')/EQ),'conditional_tau_upper_s':str(tau),'experimental_bin_seconds':str(b),'necessary_bin_over_tau_lower':str(b/tau),'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),'elapsed_seconds':time.perf_counter()-start}
Path(__file__).with_name('EXPERIMENT_UNITS.json').write_text(json.dumps(out,indent=2)+'\n');print(json.dumps(out,indent=2))
