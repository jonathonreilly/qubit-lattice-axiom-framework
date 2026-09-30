"""Exact integer/rational resource certificate; no large Hilbert space.

Price: <=5 CPU seconds, <=120 wall seconds, <=100 MB. Standard library only.
The earlier independently checked rotor example supplies R and its tail bound.
This script certifies the NEW clock/process/ledger parameter inequalities.
"""
import json
import math
import resource
import time
from fractions import Fraction as F
from pathlib import Path

t0, c0 = time.monotonic(), time.process_time()
campaign = Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
assert not (campaign / 'STOP_REQUESTED').exists()
assert time.time() < json.loads((campaign / 'DEADLINE.json').read_text())['deadline_epoch']

def ceil(x):
    x = F(x)
    return -(-x.numerator // x.denominator)

def ceil_log2(x):
    x = F(x)
    assert x >= 1
    q = x.numerator.bit_length() - x.denominator.bit_length()
    return q + (F(2**q) < x)

def ceil_cuberoot(z):
    lo, hi = 0, 1 << ((z.bit_length() + 2) // 3)
    while hi - lo > 1:
        mid = (lo + hi) // 2
        if mid**3 >= z:
            hi = mid
        else:
            lo = mid
    return hi

def size(z):
    assert isinstance(z, int) and z >= 0
    return {'decimal_digits': len(str(z)), 'bit_length': z.bit_length()}

N, R = 6912, 1346132804
T = Ksource = delta = kappa = F(1)
v = 2592 * N
Q = 1 + 6*N*R
h = F(2*Q*Q + 2*v)
gw, g = F(300*N), F(80*N)
p = gw * (316*Q*Q + 2*v)
alpha = 1 / (1000 * (1+h*h+p*p))
epsE = F(1,1000)
c = 7*g*g + 4*h*g
n = ceil(max(2*T*g, 5*T*T*c/alpha))
tau = T/n
ngate = N*n
s = min(tau/(8*N+4), alpha/(80*ngate*(h+1)))
sigma = min(s/2, alpha*s/(320*ngate))
ell = 4*T
vbar = 8*N/s  # 2*pi < 8
theta = min(alpha*alpha/(1600*N), epsE/(8*vbar*N))
k0 = ceil(ell*ell/(8*sigma*sigma*theta))
D = ceil(max(160*ngate*ell/(alpha*s), 64*ngate*ell/(epsE*s*s)))
M = D*D - 1
cut_target = min(alpha/5, epsE/(4*vbar))
k = max(ceil(6*vbar*T), ceil_log2(8/cut_target), 1)
r = k-1
Kclock = k0 + M*r

# Five process contributions: each <= alpha/5. The jitter has two parts.
err_sweep = T*tau*c
err_pulse = 16*ngate*s*h
err_smooth = 32*ngate*ell/(s*D)
err_jitter_center = 32*ngate*sigma/s
assert 16*N*theta <= (alpha/10)**2 # 4 sqrt(N theta) <= alpha/10
err_jitter = err_jitter_center + alpha/10
assert err_sweep <= alpha/5
assert err_pulse <= alpha/5
assert err_smooth <= alpha/5
assert err_jitter <= alpha/5
assert k >= 6*vbar*T and k >= ceil_log2(8/cut_target)
assert cut_target <= alpha/5
assert err_sweep+err_pulse+err_smooth+err_jitter+cut_target <= alpha

# Endpoint difference: 2 b0 + vc * delta_cut. Use pi<4 and vc<=vbar.
endpoint_smooth = 16*ngate*ell/(s*s*D)
endpoint_position = 2*vbar*N*theta
endpoint_cut = vbar*cut_target
assert endpoint_smooth <= epsE/4
assert endpoint_position <= epsE/4
assert endpoint_cut <= epsE/4
assert endpoint_smooth+endpoint_position+endpoint_cut <= epsE

qE = (2*R).bit_length()  # ceil log2(2R+1)
qC = (2*Kclock).bit_length()
qF = 4  # 13 resolved labels; coherent version needs 3
bA = 1+qC+2*n*qF
bB = 2+6*qE
side = ceil_cuberoot(max(bA,bB))
assert side**3 >= bA and side**3 >= bB
assert (side-1)**3 < max(bA,bB)

checks = {
  'source': {'L':24,'N':N,'R':R,'K':1,'delta':1,'kappa':1,'T':1},
  'source_bounds': {'Qmax':Q,'hbar':int(h),'Pbar':int(p),'g_sweep':int(g),'g_weighted':int(gw)},
  'alpha_denominator':size(alpha.denominator),
  'resource_sizes': {name:size(z) for name,z in {
      'n_bins':n,'original_center_gates':ngate,'packet_halfband_k0':k0,
      'Fejer_degree_M':M,'first_omitted_Dyson_order_k':k,
      'clock_halfband_K':Kclock,'clock_dimension':2*Kclock+1,
      'qubits_per_A_cell':bA,'M2_block_side':side,
      'total_M2_sites':(24*side)**3,'interaction_range_upper_M2_L1':7*side,
      'stored_real_Fourier_coefficients_upper':ngate*(2*M+1)
  }.items()},
  'local_register_qubits':{'one_link':qE,'one_clock':qC,'one_record':qF},
  'rational_bounds':{
      'sweep_over_alpha':str(err_sweep/alpha),
      'pulse_over_alpha_upper':'1/5',
      'smooth_over_alpha_upper':'1/5',
      'jitter_over_alpha_upper':'1/5',
      'cut_over_alpha_upper':'1/5',
      'endpoint_energy_error_upper':'3/4000',
      'each_source_moment_added_error_upper':'1/1000',
      'clock_ground_zero_initial_energy':'N*Kclock*(2*pi/ell)',
      'positive_total_energy_norm_upper':'hbar+2*N*Kclock*(2*pi/ell)+vbar'
  },
  'passed':True,
  'scope':'Exact NEW resource arithmetic; original rotor-tail certificate is a separately checked import, not rerun here.'
}
# Avoid printing a long rational merely showing n's ceiling slack.
checks['rational_bounds']['sweep_over_alpha'] = '<=1/5 (exact rational comparison)'
checks['wall_seconds']=time.monotonic()-t0
checks['cpu_seconds']=time.process_time()-c0
checks['peak_rss_bytes']=resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
out=Path(__file__).with_name('resource_results.json')
out.write_text(json.dumps(checks,indent=2)+'\n')
print(json.dumps(checks,indent=2))
