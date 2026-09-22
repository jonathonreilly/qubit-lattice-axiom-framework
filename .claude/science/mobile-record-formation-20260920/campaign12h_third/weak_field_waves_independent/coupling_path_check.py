"""Normalization countercontrol: weak ratio alone does not fix physical time."""
from pathlib import Path
from datetime import datetime,timezone
import hashlib,json,math
import numpy as np
import sympy as sp
from scipy.linalg import eigh_tridiagonal

HERE=Path(__file__).resolve().parent
size=12
ann=sp.zeros(size)
for n in range(1,size):ann[n-1,n]=sp.sqrt(n)
x=ann+ann.T
h0=sp.diag(*[4*n+2 for n in range(size)])
v1=-x**4/12
exact=[]
for n in (0,1):
    unit=sp.eye(size)[:,n];en=4*n+2;shift=v1[n,n]
    correction=sp.zeros(size,1)
    for m in range(size):
        if m!=n:correction[m]=-v1[m,n]/(4*(m-n))
    assert sp.simplify((h0-en*sp.eye(size))*correction+(v1-shift*sp.eye(size))*unit)==sp.zeros(size,1)
    assert correction[n]==0
    exact.append({'n':n,'harmonic_energy':en,'first_energy_shift':str(shift),
                  'first_vector_correction':{str(m):str(sp.simplify(correction[m])) for m in range(size) if correction[m]}})
assert v1[1,1]-v1[0,0]==-1
rows=[]
for n in (16,32,64,128,256):
    h=1/n;cutoff=math.ceil(10/math.sqrt(h));m=np.arange(-cutoff,cutoff+1)
    diag=4*h*m*m+2/h;off=np.full(len(m)-1,-1/h)
    energies=eigh_tridiagonal(diag,off,select='i',select_range=(0,1))[0]
    gap=energies[1]-energies[0]
    # K=1,J=h^-2 multiplies the whole normalized Hamiltonian by h^-1.
    physical_gap=gap/h
    phase=np.exp(-1j*physical_gap*np.pi/2)
    rows.append({'h':h,'Fourier_cutoff':cutoff,'normalized_first_two_energies':energies.tolist(),
                 'normalized_gap':float(gap),'gap_correction_divided_by_h':float((gap-4)/h),
                 'physical_gap_at_K1':float(physical_gap),
                 'relative_phase_at_fixed_time_pi_over2':[float(phase.real),float(phase.imag)],
                 'distance_from_i':float(abs(phase-1j)),
                 'bare_harmonic_relative_phase':'1 exactly, since h=1/integer'})
assert abs(rows[-1]['gap_correction_divided_by_h']+1)<.01
assert rows[-1]['distance_from_i']<.01
out={'created_utc':datetime.now(timezone.utc).isoformat(),'status':'PASS',
     'exact_first_order_quasimode_corrections':exact,'gap_first_correction_exact':'-1',
     'fixed_physical_time':'pi/2','rows':rows,
     'meaning':'At fixed K=1 and J=h^-2, the first gap is 4/h-1+O(h). For h=1/n, the exact relative phase tends to i at time pi/2 while the uncorrected harmonic phase is 1. The report supplies the cutoff-quasimode residual argument.',
     'scope':'A one-coordinate compact cosine countercontrol for order-of-limits/time normalization, not a separate 3D theorem or phase claim.',
     'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}
text=json.dumps(out,indent=2)+'\n';(HERE/'COUPLING_PATH_RESULTS.json').write_text(text);print(text,end='')
