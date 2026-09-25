#!/usr/bin/env python3
"""Disclosed root spectral and unit controls; no full dynamics or empirical fit."""
AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = ('docs/OPTICAL_REFERENCE_ENERGY_LIMITS_FOR_ORIGINAL_RECORD_COUNTS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/WEAK_FIELD_WAVE_PACKETS_FROM_MOBILE_RECORD_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/PHOTON_DISPERSION_OBSERVATIONAL_CONSTRAINTS_AND_LIVE_FORMATION_RESPONSE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/ORIGINAL_RECORD_CALIBRATION_AND_PREPARED_MATTER_PROBE_BOUNDED_THEOREM_NOTE_2026-09-24.md', 'docs/PREPARED_ORIGINAL_RECORD_PROBE_ENERGY_VACUUM_RESPONSE_AND_CLOCK_SCOPE_BOUNDED_THEOREM_NOTE_2026-09-24.md')
ROOT_CONTROL_SOURCES = [('finite-volume-observation-personal/finite_volume_units.py', 'a3122d014e37d26850d9f4bab7352e0de81ef7d32396c690d2314afab84385ed'), ('optical-band-response-personal/optical_band_controls.py', 'e938b4a2ab11be9c82b4dbd2ec628ab3a2823d1d137b0a7950dc6621d6d2b9ab'), ('optical-experiment-scope-personal/experiment_units.py', '0b3fa19a85d696aea138375530e750a6f660eceea30b425bda86b22495b92e26')]
RESULT_PATH = 'outputs/optical_observation_bridge_20260924/OPTICAL_OBSERVATION_RESULTS.json'
from pathlib import Path
import hashlib,json,time
import numpy as np
import mpmath as mp

def control(L):
    n=np.fft.fftfreq(L)*L
    s=4*np.sin(np.pi*n/L)**2
    D=s[:,None,None]+s[None,:,None]+s[None,None,:]
    xy=s[:,None,None]+s[None,:,None]+np.zeros((1,1,L))
    root=np.sqrt(D);weight=np.zeros_like(D)
    np.divide(xy,root,out=weight,where=D>0)
    V=L**3;v=float(weight.sum()/(2*V));normalization=float(xy.sum()/V)
    assert abs(normalization-4)<1e-12
    assert abs(v-float(root.sum()/(3*V)))<1e-12
    assert v>=1/np.sqrt(3)-1e-12
    green=np.zeros_like(D);np.divide(xy,D,out=green,where=D>0)
    w=float(green.sum()/(2*V));w_exact=(V-1)/(3*V)
    assert abs(w-w_exact)<1e-12
    rows=[]
    for eps in [.1,.2,.4,.7,1.,1.5,2.]:
        mask=(D>0)&(D<=eps**2);N=int(mask.sum());low=float(weight[mask].sum()/(2*V))
        bound=27*eps**4/128;cube=(2*int(np.floor(L*eps/4))+1)**3-1
        assert N<=cube
        assert low<=bound+1e-14
        assert low/v<=27*np.sqrt(3)*eps**4/128+1e-14
        if N:assert L*eps>=4-1e-12
        else:assert low==0
        rows.append({'epsilon':eps,'nonzero_momenta_in_band':N,'cube_count_upper':cube,'v_low':low,'v_low_upper':bound,'projected_weight_fraction':low/v,'eta_upper':27*np.sqrt(3)*eps**4/128,'normalized_band_packet_available':bool(N)})
    return {'L':L,'vertices':V,'plaquette_norm_squared':normalization,'v_p':v,'v_p_lower':1/np.sqrt(3),'w_p':w,'w_p_exact':w_exact,'rows':rows}

def volume_checks():
    start = time.perf_counter()
    mp.mp.dps = 65
    EQ = mp.mpf('6.9e11') * 10 ** 9
    rows = []
    for L in [6, 8, 16]:
        rows.append({'L': L, 'reference_energy_necessary_lower_eV': str(EQ / 3 * mp.sin(mp.pi / L)), 'strict_inequality': True})
    optical = []
    for E in ['1', '2', '3']:
        ratio = 3 * mp.mpf(E) / EQ
        optical.append({'supplied_reference_energy_eV': E, 'necessary_L_strict_lower': str(mp.pi / mp.asin(ratio))})
    out = {'scope': 'Conditional arithmetic; no actual charged spectrum, empirical fit or independent verification.', 'benchmark_EQG_lower_eV': str(EQ), 'fixed_volume_rows': rows, 'optical_rows': optical, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'elapsed_seconds': time.perf_counter() - start}
    return out


def band_checks():
    start = time.perf_counter()
    mp.mp.dps = 85
    EQ = mp.mpf('6.9e20')
    C = 27 * mp.sqrt(3) / 64
    unit = []
    for E in ['1', '2', '3']:
        eps = 6 * mp.mpf(E) / EQ
        unit.append({'supplied_E_lab_eV': E, 'epsilon_strict_upper': str(eps), 'hard_band_limiting_relative_excess_strict_upper': str(C * eps ** 4), 'mean_energy_limiting_relative_excess_strict_upper': str(2 * eps / mp.sqrt(3)), 'status': 'Conditional reference-band bound, not a measured detector rate or finite-g error certificate.'})
    result = {'scope': 'Finite Fourier consistency checks and conditional SI arithmetic; no full dynamics or interval certificate.', 'lattice_rows': [control(L) for L in (6, 8, 16, 32, 64, 96)], 'SI_rows': unit, 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'elapsed_seconds': time.perf_counter() - start}
    return result


def experiment_checks():
    start = time.perf_counter()
    mp.mp.dps = 65
    h = mp.mpf('6.62607015e-34')
    c = mp.mpf('299792458')
    e = mp.mpf('1.602176634e-19')
    hbar = h / (2 * mp.pi)
    EQ = mp.mpf('6.9e20')
    tau = 6 * hbar / (e * EQ)
    b = mp.mpf('1e-9')
    out = {'scope': 'Conditional unit conversions; no experimental-state fit or exact spectral-support claim.', 'spectral_endpoint_rows': [{'wavelength_nm': n, 'energy_eV': str(h * c / (e * mp.mpf(n) * mp.mpf('1e-9')))} for n in ['637', '800']], 'supplied_mean_reference_energy_ceiling_eV': '2', 'mean_energy_limiting_relative_excess_upper': str(4 * mp.sqrt(3) * mp.mpf('2') / EQ), 'conditional_tau_upper_s': str(tau), 'experimental_bin_seconds': str(b), 'necessary_bin_over_tau_lower': str(b / tau), 'source_sha256': hashlib.sha256(Path(__file__).read_bytes()).hexdigest(), 'elapsed_seconds': time.perf_counter() - start}
    return out

def main():
    started=time.perf_counter();root=Path(__file__).resolve().parents[1]
    result={'scope':'Disclosed finite spectral and conditional unit controls; no full process or data fit.',
      'volume':volume_checks(),'band':band_checks(),'experiment':experiment_checks(),
      'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
      'elapsed_seconds':time.perf_counter()-started,'all_assertions_passed':True}
    path=root/RESULT_PATH;path.parent.mkdir(parents=True,exist_ok=True)
    data=json.dumps(result,indent=2,allow_nan=False)+'\n';path.write_text(data);print(data,end='')
    print('TOTAL_PASS: 3')

if __name__=='__main__':main()
