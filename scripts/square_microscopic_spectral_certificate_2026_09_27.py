"""Exact finite-case bounds for a supplied square law and first-order approximation."""
import os
os.environ['OPENBLAS_NUM_THREADS']='1'
from fractions import Fraction as F
import json
import numpy as np
from scipy.linalg import eigh_tridiagonal
from square_schur_proposals_2026_09_27 import spectrum
from square_rational_inertia_2026_09_27 import certify
from square_rotor_tail_2026_09_27 import count_below as rotor_count
from square_corrected_tail_2026_09_27 import count_below as corrected_count, coefficients

AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
 '.claude/science/physics-loops/measured-corrections-20260927/CORRECTED_OPERATOR_BOUNDS_DRAFT.md',
 '.claude/science/physics-loops/measured-corrections-20260927/EXACT_SCHUR_AND_CALIBRATION_DRAFT.md',
 '.claude/science/physics-loops/measured-corrections-20260927/JOINT_CORRECTION_DRAFT.md',
 '.claude/science/physics-loops/measured-corrections-20260927/SPECTRAL_CERTIFICATES_DRAFT.md',

 'docs/SQUARE_MICROSCOPIC_SPECTRAL_CERTIFICATE_BOUNDED_THEOREM_NOTE_2026-09-27.md',
 'docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md',
 'scripts/square_schur_proposals_2026_09_27.py',
 'scripts/square_rational_inertia_2026_09_27.py',
 'scripts/square_rotor_tail_2026_09_27.py',
 'scripts/square_corrected_tail_2026_09_27.py',
)

def enclose_infinite(K,delta,x=None):
    L=20 if x is None else 30
    if x is None:
        n=np.arange(-L,L+1,dtype=float)
        diagonal=4*float(K)*n*n-4*float(delta)
        off=np.full(2*L,-2*float(delta))
        count=lambda E:rotor_count(L,K,delta,E)
    else:
        diagonal=[float(coefficients(n,K,delta,x)[0]) for n in range(-L,L+1)]
        off=[float(coefficients(n,K,delta,x)[1]) for n in range(-L,L)]
        count=lambda E:corrected_count(L,K,delta,x,E)
    guesses=eigh_tridiagonal(diagonal,off,select='i',select_range=(0,6),tol=1e-12)[0]
    intervals=[]
    for j,guess in enumerate(guesses):
        lo=F(str(guess))-F(1,10**9);hi=F(str(guess))+F(1,10**9)
        counts=(count(lo),count(hi))
        if counts!=(j,j+1):raise ValueError(('Uncertified infinite-domain bracket',j,counts))
        intervals.append((lo,hi))
    return dict(energy_intervals=[[str(a),str(b)] for a,b in intervals],
                gap_intervals=[[str(a-intervals[0][1]),str(b-intervals[0][0])] for a,b in intervals[1:]],
                endpoint_inertia_counts=[[j,j+1] for j in range(7)],L=L)

def differences(first,second):
    return [[F(a)-F(d),F(b)-F(c)] for (a,b),(c,d) in zip(first['gap_intervals'],second['gap_intervals'])]

def main():
    cases=[]
    for delta in (F(1),F('31.607246')):
        K=F(1);rotor=enclose_infinite(K,delta)
        for S in (20,50,120):
            proposed=spectrum(S,float(K),float(delta))
            micro=certify(S,K,delta,proposed['energies'])
            x=delta/(K*S*(S+1));approx=enclose_infinite(K,delta,x)
            dr=differences(micro,rotor);da=differences(micro,approx)
            bound=max(abs(v) for interval in da for v in interval)
            cases.append(dict(S=S,K=str(K),delta=str(delta),x=str(x),microscopic=micro,rotor=rotor,approximate=approx,
                microscopic_minus_rotor_gap_intervals=[[str(a),str(b)] for a,b in dr],
                microscopic_minus_approximate_gap_intervals=[[str(a),str(b)] for a,b in da],
                maximum_absolute_gap_error_upper_bound=str(bound)))
    print(json.dumps(dict(cases=cases,scope='exact rational finite-case enclosures; no uniform asymptotic or empirical claim'),indent=2))
    print('TOTAL: PASS=3 FAIL=0 - finite-spin inertia, infinite-rotor tail enclosure, corrected-operator tail enclosure; counts are computation checks, not empirical evidence.')
if __name__=='__main__':main()
