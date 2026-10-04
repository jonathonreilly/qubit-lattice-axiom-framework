"""Original rotor-word, finite local Fourier-clock and resource controls.

The numerical two-level Hamiltonian is a clock/controller-ledger fixture,
not the original rotor process. Universal quantifiers are proved in the paired
source note. No campaign files or prior runner outputs are scientific inputs.
Price: 10 CPU seconds, 200 MB, 120 wall seconds; largest dense matrix130.
"""
from __future__ import annotations
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS", "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"
import hashlib
import json
import math
import time
import resource
from pathlib import Path
from fractions import Fraction as F
from itertools import product, combinations
import numpy as np

AUDIT_TIMEOUT_SEC = 120
AUDIT_INPUT_PATHS = (
    "docs/AUTONOMOUS_LOCAL_SUPPLIER_OF_ORIGINAL_ROTOR_RECORDS_BOUNDED_THEOREM_NOTE_2026-09-30.md",
    "docs/LOCAL_COMPENSATION_COMMON_FIELD_RECORD_LIMIT_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/LOCAL_PAIR_FORM_AND_GENERAL_GRAPH_MAGNETIC_DYNAMICS_BOUNDED_THEOREM_NOTE_2026-09-24.md",
    "docs/CUBIC_ORIGINAL_RECORD_RESPONSE_AT_FIXED_COUPLINGS_BOUNDED_THEOREM_NOTE_2026-09-26.md",
)
REPO = Path(__file__).resolve().parents[1]
OUTPUT = REPO / "outputs/autonomous_local_original_rotor_supplier_2026_09_30.json"

def source_words():
    # Full six-neighbour root-star B words, retaining both input charge signs and
    # every B occupancy word. Link orientations all point outward from the root.
    actions=0
    for qa in (-1,1):
     for bs in product((-1,0,1),repeat=6):
      for b in range(6):
       for sigma in (-1,1):
        for d in range(6):
         if d==b or bs[b] or bs[d]:continue
         final=list(bs);final[b]=-sigma;final[d]=qa
         shifts=[0]*6;shifts[b]=sigma;shifts[d]=-qa
         assert sum(v!=0 for v in final)==sum(v!=0 for v in bs)+2
         assert sigma+sum(final)==qa+sum(bs)
         assert sum(shifts)==sigma-qa
         assert all(-shifts[i]==final[i]-bs[i] for i in range(6))
         assert sum(abs(v) for v in shifts)==2
         actions+=1

    assert actions == 2*6*2*5*3**4

    def births(state):
     qa,bs,es=state
     for b in range(6):
      if bs[b]:continue
      for sigma in (-1,1):
       for d in range(6):
        if d==b or bs[d]:continue
        q=list(bs);q[b]=-sigma;q[d]=qa
        e=list(es);e[b]+=sigma;e[d]-=qa
        yield sigma,tuple(q),tuple(e)
    states={(1,(0,)*6,(0,)*6)}
    layers=[len(states)]
    for j in range(1,5):
     states={new for old in states for new in births(old)}
     assert all(sum(v!=0 for v in st[1])==2*j for st in states)
     layers.append(len(states))
    assert layers[3]>0 and layers[4]==0

    # Actual coherent edge mark at Omega: retain the original sign sum in
    # the source vector before copying its edge label to an environment.
    mark_outputs=[]
    for sigma in (-1,1):
        for dest in range(1,6):
            final=[0]*6; final[0]=-sigma; final[dest]=1
            fields=[0]*6; fields[0]=sigma; fields[dest]=-1
            coherent_label=(0,)
            mark_outputs.append((sigma,tuple(final),tuple(fields),coherent_label))
    coherent_gain=[[int(a[3]==b[3]) for b in mark_outputs] for a in mark_outputs]
    resolved_gain=[[int(a[0]==b[0]) for b in mark_outputs] for a in mark_outputs]
    assert coherent_gain[0][5]==1 and resolved_gain[0][5]==0
    assert sum(coherent_gain[i][i] for i in range(10))==10

    # Literal F_a,F_c,F_c*,F_a* paths on two overlapping degree-three stars.
    # Shared B vertices 0,1; each A has one extra B. These are legal cubic subwords.
    adj=((0,1,2),(0,1,3));edges=tuple((a,b) for a in range(2) for b in adj[a])
    def hop(state,a,reverse=False):
     aq,bq,ee=state
     if not reverse:
      if not aq[a]:return
      for b in adj[a]:
       if bq[b]:continue
       aa=list(aq);bb=list(bq);e=list(ee);charge=aa[a]
       aa[a]=0;bb[b]=charge;e[edges.index((a,b))]-=charge
       yield tuple(aa),tuple(bb),tuple(e)
     else:
      if aq[a]:return
      for b in adj[a]:
       if not bq[b]:continue
       aa=list(aq);bb=list(bq);e=list(ee);charge=bb[b]
       aa[a]=charge;bb[b]=0;e[edges.index((a,b))]+=charge
       yield tuple(aa),tuple(bb),tuple(e)
    paths=0;relocations=0
    for aq in product((-1,1),repeat=2):
     for bq in product((-1,0,1),repeat=4):
      start=(aq,bq,(0,)*len(edges));out=[start]
      for a,rev in ((0,False),(1,False),(1,True),(0,True)):
       out=[v for u in out for v in hop(u,a,rev)]
      for aa,bb,ee in out:
       assert all(aa) and sum(v!=0 for v in bb)==sum(v!=0 for v in bq)
       assert sum(aa)+sum(bb)==sum(aq)+sum(bq)
       assert sum(abs(v) for v in ee)<=4
       paths+=1;relocations+=tuple(v!=0 for v in bb)!=tuple(v!=0 for v in bq)
    assert paths>0 and relocations>0


    # Complete actual axial two-star word at Omega, including every intermediate
    # field excursion. Two six-stars share exactly one B endpoint.
    unit=[tuple(int(k==i) for k in range(3)) for i in range(3)]
    near=[tuple(s*x for x in u) for u in unit for s in (-1,1)]
    centers=((0,0,0),(2,0,0))
    nb=[{tuple(a[i]+d[i] for i in range(3)) for d in near} for a in centers]
    bsites=sorted(nb[0]|nb[1]);adj=tuple(tuple(bsites.index(b) for b in sorted(v)) for v in nb)
    edges=tuple((a,b) for a in range(2) for b in adj[a])
    omega=((1,1),(0,)*len(bsites),(0,)*len(edges))
    apply_internal_cutoff=False
    out=[omega]
    for a,rev in ((0,False),(1,False),(1,True),(0,True)):
        out=[v for u in out for v in hop(u,a,rev)]
        if apply_internal_cutoff:out=[v for v in out if not any(v[2])]
    diagonal=sum(v==omega for v in out)
    expected=6*6-len(nb[0]&nb[1])
    assert diagonal==expected==35
    clipped=[omega]
    for a,rev in ((0,False),(1,False),(1,True),(0,True)):
        clipped=[v for u in clipped for v in hop(u,a,rev) if not any(v[2])]
    clipped_diagonal=sum(v==omega for v in clipped)
    assert clipped_diagonal==0
    return {'original_star_birth_words':actions,'successive_birth_layers':layers,
            'legal_three_neighbor_magnetic_subword_returns':paths,
            'B_relocations_at_fixed_count':relocations,
            'whole_axial_pair_omega_diagonal_SstarS':diagonal,
            'original_coherent_mark_cross_sign_matrix_element':coherent_gain[0][5],
            'product_zero_box_compressed_A_pair_omega':-2*diagonal,
            'individually_zero_box_truncated_hops_omega':-2*clipped_diagonal}

def rotor_words():
    # Gaussian-integer vector implementation of a separate one-rotor graded model.
    # D_k(E)=E^2 for k<2, and 0 for the last grade: later unconfined electric fields
    # are deliberately retained. B=(grade raising)*(T_+ + T_-), A=T_+ + T_-.
    Z=(0,0);I=(0,1)
    def add(a,b):return (a[0]+b[0],a[1]+b[1])
    def mul(a,b):return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])
    PHASE=((1,0),(0,1),(-1,0),(0,-1))
    def clean(v):return {k:z for k,z in v.items() if z!=Z}
    def combine(terms):
     out={}
     for c,v in terms:
      for k,z in v.items():out[k]=add(out.get(k,Z),mul(c,z))
     return clean(out)
    def base(v,kind,R=None):
     out={}
     for (grade,e),amp in v.items():
      if kind=='B' and grade==2:continue
      if kind=='Bt' and grade==0:continue
      gr=grade+(1 if kind=='B' else -1 if kind=='Bt' else 0)
      for step in (-1,1):
       key=(gr,e+step)
       if R is None or abs(key[1])<=R:out[key]=add(out.get(key,Z),amp)
     return clean(out)
    def gamma(v,R=None):return base(base(v,'B',R),'Bt',R)
    def diagphase(v,tick):
     return {k:mul(PHASE[(tick*(k[1]**2 if k[0]<2 else 0))%4],z) for k,z in v.items()}
    def act(v,kind,tick,R=None):
     v=diagphase(v,-tick)
     if kind=='B':w=base(v,'B',R)
     else:w=combine([((0,-2),base(v,'A',R)),((-1,0),gamma(v,R))])
     return diagphase(w,tick)
    coefficient_cases=0
    for R in (2,4,6,8,12):
     for n in range(3):
      for j in range(3):
       if 4*n+2*j>R:continue
       for jump_positions in combinations(range(n+j),j):
        word=['B' if k in jump_positions else 'G2' for k in range(n+j)]
        full=cut={(0,0):(1,0)}
        for k,kind in enumerate(word):
         full=act(full,kind,(2*k+1)%4)
         cut=act(cut,kind,(2*k+1)%4,R)
        assert full==cut,(R,word,full,cut)
        coefficient_cases+=1
    # P Gamma P differs from Gamma_R at a real boundary even at grade zero.
    edge={(0,4):(1,0)}
    old={k:z for k,z in gamma(edge).items() if abs(k[1])<=4}
    correct=gamma(edge,4)
    boundary_flux=combine([((1,0),old),((-1,0),correct)])
    assert boundary_flux=={(0,4):(1,0)}


    return {'safe_rotor_Dyson_words':coefficient_cases,
            'boundary_missing_loss_flux_on_unit_input':boundary_flux[(0,4)][0]}

def rotor_resources():
    N=24**3//2;M=N//2;b=1+2*M
    v=2592*N;g=300*N;X=v+g//2;Y=g
    k=16*(X+Y+N+1);r=k-1;R=2*M+4*r+8
    assert k>=6*X
    poly=(b+4*X)**2+16*X
    qk2=(b+4*k)**2
    sh_coeff=2*poly+v
    sp_coeff=g*(316*poly+2*v)
    eh_coeff=4*qk2+3*v
    ep_coeff=4*g*(316*qk2+2*v)
    base_exp=2*Y+2*X-k
    upper_exponents={
     'marked_trace_error':3+Y-k,
     'energy_first_moment':sh_coeff.bit_length()+3+base_exp,
     'energy_second_moment':(sh_coeff*eh_coeff).bit_length()+2+base_exp,
     'source_current_first_moment':(2*sp_coeff+ep_coeff).bit_length()+1+base_exp,
     'source_current_second_moment':(sp_coeff*ep_coeff).bit_length()+2+base_exp}
    assert all(power<-100 for power in upper_exponents.values())

    return R, {'L':24,'N':N,'maximum_births':M,'v':v,'g_weighted':g,
               'x':X,'tail_start_k':k,'product_link_cutoff':R,
               'error_upper_exponents_base_2':upper_exponents}

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


def clock_resources(R):
    N = 24**3//2
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
    actual_packet_tail_upper = ell*ell/(4*(2*k0+1)*sigma*sigma)
    assert actual_packet_tail_upper <= theta
    D = ceil(max(160*ngate*ell/(alpha*s), 64*ngate*ell/(epsE*s*s)))
    M = D*D - 1
    cut_target = min(alpha/5, epsE/(4*vbar))
    k = max(ceil(6*vbar*T), ceil_log2(8/cut_target), 1)
    r = k-1
    Kclock = k0 + M*r
    assert Kclock-k0 >= M*r

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
      'scope':'Exact finite apparatus arithmetic composed with the rotor certificate recomputed in this runner.'
    }
    # Avoid printing a long rational merely showing n's ceiling slack.
    checks['rational_bounds']['sweep_over_alpha'] = '<=1/5 (exact rational comparison)'

    # Geometry is derived from actual six-star intersections, not a copied count.
    unit=[tuple(int(k==i) for k in range(3)) for i in range(3)]
    near=[tuple(s*x for x in u) for u in unit for s in (-1,1)]
    centers={tuple(a[i]+b[i] for i in range(3)) for a in near for b in near}-{(0,0,0)}
    origin=set(near);counts={}
    for c in centers:
        other={tuple(c[i]+d[i] for i in range(3)) for d in near}
        nB=len(origin|other);counts[nB]=counts.get(nB,0)+1
    whole_pair_qubits=24+66*qE
    assert whole_pair_qubits==max(2+nB*(2+6*qE) for nB in counts)
    assert counts=={10:12,11:6}
    checks['magnetic_union_B_counts']=counts
    checks['whole_magnetic_pair_qubits_upper']=whole_pair_qubits
    return checks

def clock_matrix_fixture():
    X=np.array([[0.,1.],[1.,0.]])
    G=np.eye(2)-X # positive log-like local drive, norm2; does not commute with h.
    h=np.diag([0.,2.]);T=.6;k0=2

    def fixture(K):
     d=2*K+1
     shift=np.diag(np.ones(d-1),-1)
     shift[0,-1]=0.0
     pcheck=np.diag(np.arange(-K,K+1))
     assert np.array_equal(pcheck@shift-shift@pcheck,shift)
     f=.5*np.eye(d)-.25*(shift+shift.T) # compression of (1-cos x)/2 >=0
     pc=np.diag(np.arange(d,dtype=float))
     hs=np.kron(np.eye(d),h);hc=np.kron(pc,np.eye(2));inter=np.kron(f,G)
     H=hs+hc+inter
     assert np.linalg.eigvalsh(f)[0]>=-1e-13
     ev,Q=np.linalg.eigh(H);assert ev[0]>=-1e-13
     psi=np.zeros(2*d,dtype=complex)
     for j in range(-k0,k0+1):psi[2*(j+K)]=1/math.sqrt(2*k0+1)
     out=Q@(np.exp(-1j*T*ev)*(Q.conj().T@psi))
     energy=lambda A,v:float(np.vdot(v,A@v).real)
     changes={name:energy(A,out)-energy(A,psi) for name,A in [('system',hs),('clock',hc),('interaction',inter),('total',H)]}
     assert abs(changes['total'])<1e-10
     ledger_balance=changes['system']+changes['clock']+changes['interaction']
     assert abs(ledger_balance)<1e-10
     assert changes['system']>1e-5
     assert abs(changes['system']+changes['clock'])>1e-5 # deleting controller interaction fails.
     # The unshifted clock convention permits vector comparison across cutoffs.
     out*=np.exp(1j*K*T)
     return out,changes,float(ev[0])
    ref,_,_=fixture(32)
    rows=[]
    for K in (6,8,10):
     vec,ledger,ground=fixture(K)
     pad=np.zeros_like(ref);pad[2*(32-K):2*(32+K+1)]=vec
     err=np.linalg.norm(pad-ref)
     k=K-k0+1
     # Exact geometric upper bound for the infinite factorial tail at 2T=6/5.
     x_exact=F(6,5)
     tail_upper=x_exact**k/math.factorial(k)/(1-x_exact/(k+1))
     vector_bound=math.nextafter(float(2*tail_upper),math.inf)
     assert err<=vector_bound+1e-12
     rows.append({'K':K,'dimension':2*(2*K+1),'joint_vector_error_vs_K32':float(err),'proved_vector_tail_upper':vector_bound,'floating_comparison_allowance':1e-12,'energy_changes':ledger,'minimum_total_energy':ground})


    return rows

def clock_words_and_records():
    k0=2
    # Exact Gaussian-integer interaction-picture words with the true nonwrapping
    # shifts. All intermediate magnitudes here are below 2^53.
    def act(vec,tick,K=None):
     out={}
     roots=(1,1j,-1,-1j)
     for (m,s),v in vec.items():
      for dm,c in ((0,2),(-1,-1),(1,-1)):
       for sp,sgn in ((s,1),(1-s,-1)):
        mp=m+dm
        if K is not None and abs(mp)>K:continue
        phase=roots[(tick*((mp+2*sp)-(m+2*s)))%4]
        key=mp,sp;out[key]=out.get(key,0)+c*sgn*phase*v
     return {k:v for k,v in out.items() if v}
    words=0
    for K in range(3,9):
     for n in range(K-k0+1):
      full=cut={(m,0):1 for m in range(-k0,k0+1)}
      for j in range(n):
       full=act(full,2*j+1);cut=act(cut,2*j+1,K)
      assert full==cut
      assert all(z.real.is_integer() and z.imag.is_integer() for z in map(complex,full.values()))
      assert all(max(abs(z.real),abs(z.imag))<2**53 for z in map(complex,full.values()))
      words+=1
    K=4;d=2*K+1
    S=np.diag(np.ones(d-1),-1);P=np.diag(np.arange(-K,K+1))
    assert np.array_equal(P@S-S@P,S)
    wrap=S.copy();wrap[0,-1]=1
    wrap_def=P@wrap-wrap@P-wrap
    assert wrap_def[0,-1]==-(2*K+1)

    # Matched-record code: conjugated copying preserves it at every partial pulse,
    # not merely at the completed collision. Exact integer matrices suffice.
    dF=3
    copy=np.zeros((dF*dF,dF*dF),dtype=int)
    for f0 in range(dF):
     for e0 in range(dF):copy[f0*dF+(e0+f0)%dF,f0*dF+e0]=1
    gf=np.eye(dF,dtype=int);gf[0,1]=gf[1,0]=-1
    gfe=copy@np.kron(gf,np.eye(dF,dtype=int))@copy.T
    code=np.diag([int(f0==e0) for f0 in range(dF) for e0 in range(dF)])
    assert np.array_equal(copy.T@copy,np.eye(dF*dF,dtype=int))
    assert np.array_equal(gfe@code,code@gfe)
    assert gfe[0,dF+1]==-1 # a genuine offdiagonal matched-label transition
    assert all(gfe[row,col]==0 for row in range(dF*dF) for col in range(dF*dF)
               if code[row,row] != code[col,col])


    return {'protected_clock_prefix_words':words,
            'wrapped_shift_boundary_commutator_defect':int(wrap_def[0,-1]),
            'matched_code_commutator_norm_squared':int(np.sum((gfe@code-code@gfe)**2)),
            'actual_matched_label_transition':int(gfe[0,dF+1])}

def main():
    t0,c0=time.monotonic(),time.process_time()
    # Ancestral scientific source identities and the package-local note are
    # read for explicit binding. Inline operators are tested below; hashes
    # alone do not establish those operators or their physical interpretation.
    identities={p:hashlib.sha256((REPO/p).read_bytes()).hexdigest() for p in AUDIT_INPUT_PATHS}
    result={'scope':'Conditional original rotor-word, clock-module and finite resource checks; no native selection or full-torus numerical simulation.',
            'scientific_source_identities':identities,
            'package_local_integrity_reads':['paired source note; source hashes only'],
            'source_words':source_words(),
            'rotor_prefix_and_loss':rotor_words()}
    R,result['rotor_resources']=rotor_resources()
    result['clock_resources']=clock_resources(R)
    result['clock_matrix_fixture']=clock_matrix_fixture()
    result['clock_prefix_and_record_code']=clock_words_and_records()
    result['execution']={'wall_seconds':time.monotonic()-t0,
                         'cpu_seconds':time.process_time()-c0,
                         'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss}
    OUTPUT.parent.mkdir(parents=True,exist_ok=True)
    OUTPUT.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))
    print('per_element: checked exact original birth shifts and individual clock momentum prefixes.')
    print('per_site: checked complete cubic-star labels and charge/field changes on all local occupancy words.')
    print('per_mode: checked compressed Fourier shifts, protected Dyson words and the matched record code.')
    print('per_block: checked actual overlapping-star compression and a separate finite controller-energy fixture.')
    print('lattice_wide: checked symbolic finite-torus resource bounds; no full torus matrix was executed.')
    print('TOTAL: PASS=6 FAIL=0 (six check groups; finite evidence for the paired conditional proof)')

if __name__=='__main__':
    main()
