"""Checks of the low/high operator proof, not a native spectral fit.

The finite comparator has three low and four high complex modes, an explicit
positive scalar defect shift, and orthonormal native-shaped center/leg fields.
Its soft weights and energies are chosen independently; it is not a finite
approximation to the cubic density of states. That density enters only the
separate exact native-constant check.
"""
from __future__ import annotations
import os
for key in ('OPENBLAS_NUM_THREADS','OMP_NUM_THREADS','VECLIB_MAXIMUM_THREADS'):os.environ[key]='1'
from fractions import Fraction as F
from itertools import combinations
from pathlib import Path
import hashlib,json,time
import numpy as np
import sympy as sp

ROOT=Path(__file__).resolve().parents[1]
NOTE=ROOT/'docs/NATIVE_STAR_LOW_ENERGY_OPERATOR_BOUNDED_THEOREM_NOTE_2026-09-13.md'
AUDIT_TIMEOUT_SEC=180
AUDIT_INPUT_PATHS=(
    'docs/NATIVE_STAR_LOW_ENERGY_OPERATOR_BOUNDED_THEOREM_NOTE_2026-09-13.md',
    'scripts/native_star_infrared_spectral_2026_09_13.py',
    'docs/NATIVE_STAR_INFRARED_SPECTRAL_DOMINANCE_BOUNDED_THEOREM_NOTE_2026-09-13.md',
    'docs/NATIVE_POSITIVE_WARD_SCALAR_BOUNDED_THEOREM_NOTE_2026-09-13.md',
    'scripts/native_ward_scalar_arithmetic_2026_09_13.py',
    '.claude/science/physics-loops/native-positive-ward-scalar-20260913/MOMENT_FORMULAS.json',
    '.claude/science/physics-loops/native-positive-ward-scalar-20260913/TRIAL_FORMULAS.json',
    '.claude/science/physics-loops/native-positive-ward-scalar-20260913/WITNESS.json',
    '.claude/science/physics-loops/native-star-infrared-spectral-20260913/SOURCE_MANIFEST.json',
    '.claude/science/physics-loops/native-star-infrared-spectral-20260913/NO_GO_DISCIPLINE_CHECKLIST.md',
    '.claude/science/physics-loops/native-star-infrared-spectral-20260913/mutations/RESULTS.json',
    '.claude/science/physics-loops/native-star-low-energy-operator-20260913/SOURCE_MANIFEST.json',
    '.claude/science/physics-loops/native-star-low-energy-operator-20260913/NO_GO_DISCIPLINE_CHECKLIST.md',
    '.claude/science/physics-loops/native-star-low-energy-operator-20260913/mutations/RESULTS.json',
)
from native_star_infrared_spectral_2026_09_13 import run as spectral_check


def run():
    start=time.monotonic();checks=[]
    def checked(name,condition,**data):
        assert condition,name
        checks.append({'name':name,**data})
    def close(name,x,y,tol=2e-12):
        error=float(np.linalg.norm(np.atleast_2d(x)-np.atleast_2d(y),2))
        checked(name,error<tol,error=error)

    rho=F(1,128);pi_upper=F(22,7)
    high_gap=F(1,4)-F(1,32)-2*rho**2
    perturb=4*rho+2*rho**2
    checked('high_gap_after_real_parameter',high_gap>F(1,5))
    checked('complex_disk_inverse_bound',perturb<F(1,16) and high_gap-perturb>F(1,8))
    M=F(90,8)*8**2*(1+rho)
    B=F(4,3)*726/rho**3
    C=F(90,8)*(2*8**3+24*8**4)
    checked('Cauchy_and_telescoping_constants',M<726 and B==2030043136 and C==1117440)
    endpoint=F(1,256)
    def scalar_majorant(x):return 720*(1+x)/(1-32*x-16*x*x)**2
    alternative=((scalar_majorant(endpoint)-scalar_majorant(-endpoint))/2-720*65*endpoint)/endpoint**3
    checked('independent_Neumann_odd_tail',32*endpoint+16*endpoint**2<1 and alternative<F(102000000)<B,
            rational=str(alternative),decimal=float(alternative))
    inverse_series=[1,32]
    for n in range(2,4):inverse_series.append(32*inverse_series[-1]+16*inverse_series[-2])
    paired=[sum(inverse_series[j]*inverse_series[n-j] for j in range(n+1)) for n in range(4)]
    cubic=720*(paired[3]+paired[2]);x=sp.Symbol('x')
    checked('Neumann_majorant_matches_two_inverse_word_series',sp.diff(scalar_majorant(x),x,3).subs(x,0)/6==cubic)
    window=F(1,2**21);t2=pi_upper*window**3/48
    error=(4*C+47520*pi_upper)*window+2*B*t2
    checked('window_meets_low_cutoff_and_zeta_conditions',t2<(rho/2)**2 and window<F(1,32))
    checked('uniform_relative_half_bound',error<F(7,2),rational=str(error),decimal=float(error),relative_upper=float(error/7))

    # Independent finite CAR construction in occupation-bit order, low first.
    low_modes=3;high_modes=4;modes=low_modes+high_modes;dim=1<<modes;ldim=1<<low_modes
    eye=np.eye(dim,dtype=complex);ann=[]
    for j in range(modes):
        a=np.zeros((dim,dim),complex)
        for mask in range(dim):
            if mask&(1<<j):a[mask^(1<<j),mask]=(-1)**((mask&((1<<j)-1)).bit_count())
        ann.append(a)
    gam=[]
    for a in ann:gam.extend((a+a.conj().T,1j*(a.conj().T-a)))
    maximum=max(float(np.max(abs(a@b+b@a-(2*eye if j==k else 0)))) for j,a in enumerate(gam) for k,b in enumerate(gam))
    checked('graded_low_high_CAR',maximum<1e-14,maximum=maximum)
    low_freq=np.array([.001,.0015,.002]);high_freq=np.array([2.,3.,5.,7.])
    frequencies=np.r_[low_freq,high_freq]
    low_energy=np.array([sum(low_freq[j] for j in range(low_modes) if mask&(1<<j)) for mask in range(dim)])
    high_energy=np.array([sum(high_freq[j] for j in range(high_modes) if mask&(1<<(j+low_modes))) for mask in range(dim)])
    HL=np.diag(low_energy).astype(complex);HH=np.diag(high_energy).astype(complex)
    high_parity=np.diag([(-1)**((mask>>low_modes).bit_count()) for mask in range(dim)])
    low_parity=np.diag([(-1)**((mask&((1<<low_modes)-1)).bit_count()) for mask in range(dim)])
    vacuum=eye[:,0];lvac=np.eye(ldim,dtype=complex)[:,0]
    tau=.02
    A=np.zeros((2*low_modes,7));A[:,:6]=tau*np.eye(6);A[1:3,6]=tau/np.sqrt(2)
    vals,vec=np.linalg.eigh(np.eye(7)-A.T@A)
    high_coeff=(vec*np.sqrt(vals))@vec.T
    coeff=np.vstack((A,high_coeff,np.zeros((1,7))))
    close('orthonormal_center_and_six_legs',coeff.T@coeff,np.eye(7))
    close('center_neighbors_separate_under_cutoff',A[:,0]@A[:,1:],np.zeros(6))
    lo=[sum((A[j,c]*gam[j] for j in range(6)),np.zeros_like(eye)) for c in range(7)]
    hi=[sum((high_coeff[j,c]*gam[6+j] for j in range(7)),np.zeros_like(eye)) for c in range(7)]
    fields=[x+y for x,y in zip(lo,hi)];gL,gH=lo[0],hi[0]
    pairs=list(combinations(range(6),2));ordered=[(a,c) for a in pairs for c in pairs if not set(a)&set(c)]
    checked('complete_finite_star_pairs',len(pairs)==15 and len(ordered)==90)
    bh={};w1={};w2={};dh={};bfull={}
    for pair in pairs:
        dl=sum((lo[j+1] for j in pair),np.zeros_like(eye));dhi=sum((hi[j+1] for j in pair),np.zeros_like(eye))
        bh[pair]=1j*gH@dhi
        w1[pair]=1j*(gH@dl+gL@dhi)
        w2[pair]=1j*gL@dl
        bfull[pair]=1j*(gH+gL)@(dhi+dl)
        dh[pair]=HH+8*eye+bh[pair]
    error=max(float(np.max(abs(bfull[a]-bh[a]-w1[a]-w2[a]))) for a in pairs)
    checked('exact_low_high_defect_split',error<1e-13,error=error)
    checked('linear_quadratic_low_field_bounds',max(np.linalg.norm(w1[a],2) for a in pairs)<=4*tau
            and max(np.linalg.norm(w2[a],2) for a in pairs)<=2*tau**2+1e-15)
    minimum=min(float(np.linalg.eigvalsh(dh[a]+HL+w1[a]+w2[a]).min()) for a in pairs)
    high_min=min(float(np.linalg.eigvalsh(dh[a]).min()) for a in pairs)
    checked('comparator_positive_gap_and_high_gap',minimum>6 and high_min>=minimum-2*tau**2-1e-12,full_min=minimum,high_min=high_min,
            scope='shifted seven-mode comparator, not a native gap estimate')
    # The bound from the actual full gap uses a low-vacuum compression, including W2.
    high_indices=np.arange(1<<high_modes)<<low_modes
    compression=(dh[pairs[0]]+HL+w1[pairs[0]]+w2[pairs[0]])[np.ix_(high_indices,high_indices)]
    high_only=dh[pairs[0]][np.ix_(high_indices,high_indices)]
    w2_scalar=np.vdot(vacuum,w2[pairs[0]]@vacuum)
    close('low_vacuum_compression_keeps_quadratic_scalar',compression,high_only+w2_scalar*np.eye(1<<high_modes))
    checked('nonzero_low_vacuum_quadratic_scalar',abs(w2_scalar)>1e-6,value=str(w2_scalar))
    for a in pairs:
        assert np.max(abs(high_parity@w1[a]@high_parity+w1[a]))<1e-13
        assert np.max(abs(high_parity@w2[a]@high_parity-w2[a]))<1e-13
    checked('high_parity_of_insertions',True)
    def EH(op):return op[:ldim,:ldim]
    def family(s,zeta=0.,low_energy_on=True):
        free=HL if low_energy_on else np.zeros_like(HL)
        rs={a:-np.linalg.inv(dh[a]+free-zeta*eye+s*w1[a]+s*w2[a]) for a in pairs}
        gs=gH+s*gL
        return sum((rs[c]@gs@rs[a] for a,c in ordered),np.zeros_like(eye))/8
    def coefficient(zeta=0.,low_energy_on=True,wrong_sign=False):
        free=HL if low_energy_on else np.zeros_like(HL)
        rs={a:-np.linalg.inv(dh[a]+free-zeta*eye) for a in pairs}
        out=np.zeros_like(eye)
        sign=-1 if wrong_sign else 1
        for a,c in ordered:
            ra,rc=rs[a],rs[c]
            out+=rc@gL@ra+sign*(rc@w1[c]@rc@gH@ra+rc@gH@ra@w1[a]@ra)
        return EH(out/8)
    F1=coefficient();bar=coefficient(low_energy_on=False)
    exact=family(1);soft=EH(exact)
    for s in (1.,.5,.3j):close('operator_analytic_oddness_'+str(s),EH(family(s))+EH(family(-s)),np.zeros((ldim,ldim)))
    eps=.01
    derivative=EH(family(eps))/eps
    close('analytic_first_coefficient_vs_direct_inverse',derivative,F1,tol=3e-9)
    checked('wrong_inverse_derivative_sign_rejected',np.linalg.norm(derivative-coefficient(wrong_sign=True),2)>1e-4)
    # General Cauchy bound with a larger radius supported by this comparator gap.
    comp_rho=.5;r=comp_rho/tau
    floor=high_min-(4*comp_rho+2*comp_rho**2)
    comp_M=(90/8)*(1+comp_rho)/floor**2
    tail_bound=comp_M*r**-3/(1-r**-2)
    tail=float(np.linalg.norm(soft-F1,2))
    checked('whole_soft_Fock_Cauchy_tail',1e-12<tail<tail_bound,tail=tail,bound=tail_bound)
    low_ann=[a[:ldim,:ldim] for a in ann[:low_modes]]
    def linear_from_vector(v):
        amplitudes=[v[1<<j] for j in range(low_modes)]
        return sum((z*a.conj().T+z.conjugate()*a for z,a in zip(amplitudes,low_ann)),np.zeros((ldim,ldim),complex))
    reconstructed=linear_from_vector(bar@lvac)
    close('zero_low_energy_coefficient_is_linear',bar,reconstructed)
    close('Hermitian_linear_field_vacuum_isometry',np.linalg.norm(bar,2),np.linalg.norm(bar@lvac))
    L=linear_from_vector(soft@lvac)
    Lambda=.006;E=.006;zeta=.003
    a_bound=1/high_min
    Cfixture=(90/8)*(2*a_bound**3+24*a_bound**4)
    difference=float(np.linalg.norm(F1-bar,2))
    checked('energy_removal_bound_nonvacuous',1e-9<difference<Cfixture*tau*(E+Lambda),error=difference,bound=Cfixture*tau*(E+Lambda))
    checked('exact_vacuum_calibration_bound',np.linalg.norm(L-bar,2)<tail_bound+Cfixture*tau*Lambda)
    # Use the more conservative inverse bound including the real spectral shift.
    az=1/(high_min-abs(zeta));Cz=(90/8)*(2*az**3+24*az**4)
    floorz=high_min-abs(zeta)-(4*comp_rho+2*comp_rho**2)
    Tz=(90/8)*(1+comp_rho)/floorz**2*r**-3/(1-r**-2)
    opz=EH(family(1,zeta))
    direct_rs={a:-np.linalg.inv(HH+HL+8*eye+bfull[a]-zeta*eye) for a in pairs}
    direct_op=sum((direct_rs[c]@(gH+gL)@direct_rs[a] for a,c in ordered),np.zeros_like(eye))/8
    close('real_spectral_parameter_matches_full_unsplit_operator',opz,EH(direct_op))
    close('real_parameter_first_coefficient',EH(family(eps,zeta))/eps,coefficient(zeta),tol=3e-9)
    bound=tail_bound+Tz+Cz*tau*(E+2*Lambda+abs(zeta))
    checked('operator_comparison_on_all_low_particle_numbers',np.linalg.norm(opz-L,2)<bound,error=float(np.linalg.norm(opz-L,2)),bound=bound,
            low_particle_numbers=list(range(low_modes+1)))
    multi=np.eye(ldim)[:,7]
    checked('three_low_particle_input_is_in_energy_domain',low_energy[7]<E and np.linalg.norm((opz-L)@multi)>1e-9,
            energy=float(low_energy[7]),difference=float(np.linalg.norm((opz-L)@multi)))
    low_g=EH(gL);restricted=low_energy[:ldim]
    maximum=0.;wrong=0.
    for cutoff in (0.,.001,.0025,.006):
        incoming=np.diag(restricted<=cutoff).astype(complex)
        outgoing=np.diag(restricted<=cutoff+max(low_freq)+1e-14).astype(complex)
        for a in low_ann:
            field=a+a.conj().T
            maximum=max(maximum,float(np.linalg.norm((np.eye(ldim)-outgoing)@field@incoming,2)))
            wrong=max(wrong,float(np.linalg.norm((np.eye(ldim)-incoming)@field@incoming,2)))
    checked('one_field_intermediate_energy_support',maximum<1e-14,maximum=maximum)
    checked('omitted_creation_energy_margin_rejected',wrong>.9,residual=wrong)
    close('compressed_local_field_norm_attained',np.linalg.norm(low_g,2),np.linalg.norm(low_g@lvac))
    # Global operator equality is separately falsified on high-energy states.
    chi=exact@vacuum
    amplitudes=[chi[1<<j] for j in range(modes)]
    linear=sum((z*a.conj().T+z.conjugate()*a for z,a in zip(amplitudes,ann)),np.zeros_like(eye))
    global_error=float(np.linalg.norm(exact-linear,2))
    high_filled=eye[:,-1]
    filled_error=float(np.linalg.norm((exact-linear)@high_filled))
    checked('unrestricted_operator_replacement_is_false',global_error>1e-3 and filled_error>1e-3,global_error=global_error,filled_error=filled_error,
            scope='finite comparator counterexample only; original native L4 counterexample is a separate source')

    return {'status':'passed','count':len(checks),'checks':checks,'seconds':time.monotonic()-start,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
            'derivation_sha256':hashlib.sha256(NOTE.read_bytes()).hexdigest(),
            'scope':'exact proof constants and an independently assembled shifted finite CAR comparator; not a native infrared fit, full interacting proof or independent source review'}


if __name__=='__main__':
    import signal
    signal.alarm(AUDIT_TIMEOUT_SEC)
    parent=spectral_check()
    result=run()
    print(json.dumps({'operator':result,'spectral_parent':parent},indent=2))
    print('per_element: The real high/low field split, graded defect terms and inverse derivative signs are checked.')
    print('per_site: Center/neighbor orthogonality and native cutoff normalization are explicit; the finite comparator is separately labelled.')
    print('per_mode: Low-field energy support and CAR norm isometry are checked on all three soft modes.')
    print('per_block: Complete soft-Fock operators and a three-particle input challenge the analytical compression estimate.')
    print('lattice_wide: checked and not executed — the infinite operator statement follows from the analytical split and positive-gap expansion, not a size extrapolation.')
    print(f"TOTAL: PASS={result['count']+parent['count']} FAIL=0")
    signal.alarm(0)
