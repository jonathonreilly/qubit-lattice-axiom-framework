#!/usr/bin/env python3
"""Reviewer reconstruction of a fixed stationary reflection certificate.

No author code is imported or executed. The physical 16-state basis is built
by bit operations, without parity reduction. Newton iteration proposes the
12-dimensional closed-source square root. Two full 32-dimensional boundary
systems are certified by exact Fraction residuals. All candidate matrices
are saved so the exact inequalities can be replayed without the proposer.
This program proves no normalizable-packet or time-uniform statement.
"""
from pathlib import Path
from fractions import Fraction as Q
from math import isqrt
import hashlib
import json
import os
import resource
import sys
import time
import numpy as np
import mpmath as mp

START = time.monotonic()
ROOT = Path(__file__).resolve().parent/'old_cap_delta'
ROOT.mkdir(exist_ok=True)
resource.setrlimit(resource.RLIMIT_CPU, (90, 90))
mp.mp.dps = 90
DEN = 10**60

def ident(n):
    a = zero(n, n)
    for i in range(n):
        a[i, i] = Q(1)
    return a

def zero(n, m):
    return np.full((n, m), Q(0), dtype=object)

def norm(a):
    return max(sum(abs(x) for x in row) for row in a)

def complex_norm(re, im):
    return max(sum(abs(x)+abs(y) for x, y in zip(r, s))
               for r, s in zip(re, im))

def mpq(x):
    return mp.mpf(x.numerator)/x.denominator

def quantize(x):
    return Q(int(mp.nint(x*DEN)), DEN)

def mpmatrix(re, im=None):
    return mp.matrix([[mpq(re[i,j]) + (mp.j*mpq(im[i,j]) if im is not None else 0)
                       for j in range(re.shape[1])] for i in range(re.shape[0])])

def rounded_matrix(a):
    re = np.array([[quantize(mp.re(a[i,j])) for j in range(a.cols)]
                   for i in range(a.rows)], dtype=object)
    im = np.array([[quantize(mp.im(a[i,j])) for j in range(a.cols)]
                   for i in range(a.rows)], dtype=object)
    return re, im

def pairmul(a, b):
    return a[0]*b[0]-a[1]*b[1], a[0]*b[1]+a[1]*b[0]

def pairdiv(a, b):
    d = b[0]**2+b[1]**2
    return ((a[0]*b[0]+a[1]*b[1])/d,
            (a[1]*b[0]-a[0]*b[1])/d)

def number(x):
    return {'rational':str(x), 'approximate_float':float(x)}

def matrix_data(a):
    return [[str(x) for x in row] for row in a]

# Bounded coefficient delta: exact transcription from frozen old-cap RESULT.md.
P = {k:Q(v) for k,v in {
    'J':'0.030021107107032', 'gA':'0.996878563816670',
    'gB':'0.599319315560298', 't':'3.999349697888060',
    'lambdaA':'3.801781381581202', 'lambdaB':'2.575033765788497',
    'u':'0.544607276405587', 'mu0':'0.321494607058201',
    'mu1':'-1.459892813020969', 'tan_half_complement':'4.510351185997098'
}.items()}
q = P['tan_half_complement']
P['cos_k'] = (q*q-1)/(q*q+1)
P['sin_k'] = 2*q/(q*q+1)
J = P['J']; co = P['cos_k']; si = P['sin_k']
P['epsilon'] = 2*J*(1-co)
P['DeltaA'] = Q('2.192035527016003')
P['DeltaB'] = Q('2.186826508897014')
assert 0<P['gA']<=1 and 0<P['gB']<=1
P['scalar_reserve'] = -P['mu1']
author = json.loads((ROOT.parent/'sources/old_cap/rational_point_certificate.json').read_text())
assert P == {k:Q(v) for k,v in author['exact_parameters'].items()}
assert all(P[k]>0 for k in P if k not in ['mu1','cos_k'])
assert co*co+si*si == 1 and si>0
source_gap = min(P['DeltaA'],P['DeltaB'])-2-4*J
old_gap = 2-4*J
assert source_gap>0 and old_gap>0

# Check the phase/sign convention on an exactly soluble free half-line.
top = -2*J*co
bottom = (-J*co,J*si)
detpair = (top*bottom[0]-J*J,top*bottom[1])
free_x1 = pairdiv((Q(0),top*2*J*si),detpair)
free_r = (free_x1[0]-1,free_x1[1])
z2 = pairmul((co,si),(co,si)); z4 = pairmul(z2,z2)
assert free_r == (-z4[0],-z4[1])
assert (-free_x1[0]-1,-free_x1[1]) != free_r

# Physical order old1,old2,A,B. No author's matrices or parity vectors used.
I16 = ident(16)
B = zero(16,16); VA = zero(16,16); VB = zero(16,16)
XX = zero(16,16)
for state in range(16):
    b1,b2,a,b = [(state>>shift)&1 for shift in [3,2,1,0]]
    B[state,state] = (2+(1-2*b1)*(1-2*b2)+P['DeltaA']*a+P['DeltaB']*b
                      +P['t']*(a+b)+P['u']*a*b+P['gA']*a+P['gB']*b)
    if a != b:
        B[state^3,state] -= P['t']
    B[state^8,state] += P['gA']*a
    B[state^4,state] += P['gB']*b
    VA[state,state] = P['lambdaA']+P['mu0']
    VA[state^2,state] = P['lambdaA']
    VB[state,state] = P['lambdaB']+P['mu1']
    VB[state^1,state] = P['lambdaB']
    XX[state^12,state] = Q(1)
assert np.array_equal(B,B.T)
assert np.array_equal(B@XX,XX@B)
assert np.array_equal(VA@XX,XX@VA) and np.array_equal(VB@XX,XX@VB)
vacuum = [0,4,8,12]
excited = [x for x in range(16) if x not in vacuum]
for state in vacuum:
    expected = zero(16,1)
    b1,b2 = (state>>3)&1,(state>>2)&1
    expected[state,0] = 2+(1-2*b1)*(1-2*b2)
    assert np.array_equal(B[:,state:state+1],expected)

loads = {'old1_added':2*P['gA'],'old2_added':2*P['gB'],'old_edge_separate':Q(3),
         'A':P['DeltaA']+2*P['gA']+2*P['t']+P['u']+2*P['lambdaA'],
         'B':P['DeltaB']+2*P['gB']+2*P['t']+P['u']+2*P['lambdaB'],
         'clock0':3*J+2*P['lambdaA']+P['mu0'],
         'clock1':4*J+2*P['lambdaB']+P['scalar_reserve'],'clock_tail':4*J}
assert loads == {k:Q(v['rational']) for k,v in author['added_incident_block_norms'].items()}

records=[]; witness=[]; amplitudes={}; amplitude_errors={}; mutations=[]
for s in [1,-1]:
    E=2+s+P['epsilon']
    D=B[np.ix_(excited,excited)]+(2*J-E)*ident(12)
    A=D@D-4*J*J*ident(12)
    d=1+min(P['DeltaA'],P['DeltaB'])+2*J-E
    assert d>2*J
    # Newton proposals use no eigendecomposition and no parity sector.
    Y=mpmatrix(D); Am=mpmatrix(A)
    for _ in range(12):
        Y=(Y+Am*(Y**-1))/2
        Y=(Y+Y.T)/2
    S,imag=rounded_matrix(Y)
    assert not np.any(imag) and np.array_equal(S,S.T)
    sqrt_lower=d-norm(S-D)
    true_sqrt_lower=d-2*J
    assert sqrt_lower>0
    root_residual=norm(S@S-A)
    root_error=root_residual/(sqrt_lower+true_sqrt_lower)
    # sqrt(12)/2 < 2 gives a conservative infinity norm for the F error.
    source_F_error=2*root_error

    Dr=(2-s)+2*J-E
    assert abs(Dr)>2*J
    scalar_square=Dr*Dr-4*J*J
    floor_integer=isqrt(scalar_square.numerator*DEN**2//scalar_square.denominator)
    scalar_root=Q(floor_integer,DEN)
    assert scalar_root**2<=scalar_square<(scalar_root+Q(1,DEN))**2
    scalar_F_error=Q(1,2*DEN)
    Fr=zero(16,16);Fi=zero(16,16)
    Fr[np.ix_(excited,excited)]=-(D+S)/2
    open_states=[v for v in vacuum if ((v>>3)&1)==((v>>2)&1)] if s==1 else [4,8]
    assert len(open_states)==2
    for v in vacuum:
        if v in open_states:
            Fr[v,v]=-J*co;Fi[v,v]=J*si
        else:
            Fr[v,v]=-(Dr+(1 if Dr>0 else -1)*scalar_root)/2

    Mr=zero(32,32);Mi=zero(32,32)
    Mr[:16,:16]=(E-2*J)*I16-B-VA
    Mr[:16,16:]=J*I16;Mr[16:,:16]=J*I16
    Mr[16:,16:]=Fr-VB;Mi[16:,16:]=Fi
    mm=mpmatrix(Mr,Mi);inv=mm**-1
    Nr,Ni=rounded_matrix(inv)
    gamma=complex_norm(ident(32)-(Mr@Nr-Mi@Ni),-(Mr@Ni+Mi@Nr))
    assert gamma<1
    approx_inv_bound=complex_norm(Nr,Ni)/(1-gamma)
    delta=max(source_F_error,scalar_F_error)
    assert approx_inv_bound*delta<1
    true_inv_bound=approx_inv_bound/(1-approx_inv_bound*delta)
    br=zero(32,2);bi=zero(32,2)
    for col,v in enumerate(open_states):bi[16+v,col]=2*J*si
    rhs=mpmatrix(br,bi)
    xr,xi=rounded_matrix(inv*rhs)
    state_res=complex_norm(Mr@xr-Mi@xi-br,Mr@xi+Mi@xr-bi)
    state_error=true_inv_bound*(state_res+delta*complex_norm(xr,xi))
    Rr=xr[[16+v for v in open_states],:]-ident(2)
    Ri=xi[[16+v for v in open_states],:]
    for p in [1,-1]:
        ar=(Rr[0,0]+Rr[1,1]+p*(Rr[0,1]+Rr[1,0]))/2
        ai=(Ri[0,0]+Ri[1,1]+p*(Ri[0,1]+Ri[1,0]))/2
        error=2*state_error
        amplitudes[s,p]=(ar,ai);amplitude_errors[s,p]=error
        # Flux conservation is proved analytically in REVIEW.md; this check
        # tests that the independently computed candidates respect its bound.
        assert abs(ar*ar+ai*ai-1)<=2*error+error*error
        old=next(row for row in author['channels'] if row['s']==s and row['p']==p)
        author_difference=abs(ar-Q(old['reflection_real']))+abs(ai-Q(old['reflection_imag']))
        assert author_difference<=2*(error+Q(old['reflection_error']['rational']))
    records.append({'s':s,'energy':number(E),'source_D_lower':number(d),
                    'sqrt_candidate_lower':number(sqrt_lower),'sqrt_residual':number(root_residual),
                    'sqrt_operator_error':number(root_error),'boundary_matrix_error':number(delta),
                    'inverse_residual':number(gamma),'inverse_bound':number(true_inv_bound),
                    'state_residual':number(state_res),'state_error':number(state_error)})
    witness.append({'s':s,'D':matrix_data(D),'S_hat':matrix_data(S),
                    'scalar_sqrt_lower':str(scalar_root),'M_hat_real':matrix_data(Mr),
                    'M_hat_imag':matrix_data(Mi),'N_real':matrix_data(Nr),
                    'N_imag':matrix_data(Ni),'x_hat_real':matrix_data(xr),
                    'x_hat_imag':matrix_data(xi),'rhs_real':matrix_data(br),'rhs_imag':matrix_data(bi)})
    # A physical term-drop discriminator, diagnostic only. The unchanged bulk
    # surface is retained; the lambdaA contact is removed at the entrance.
    mm_drop=mp.matrix(mm)
    for state in range(16):
        mm_drop[state,state]+=mpq(P['lambdaA'])
        mm_drop[state^2,state]+=mpq(P['lambdaA'])
    changed=(mm_drop**-1)*rhs
    values={}
    for p in [1,-1]:
        rr=(changed[16+open_states[0],0]+changed[16+open_states[1],1]
            +p*(changed[16+open_states[0],1]+changed[16+open_states[1],0]))/2-1
        values[str(p)]=[str(mp.re(rr)),str(mp.im(rr))]
    mutations.append({'s':s,'remove_lambdaA_contact_diagnostic':values})

alpha=amplitudes[-1,-1];alpha_error=amplitude_errors[-1,-1]
comparisons=[]
for s in [1,-1]:
    for p in [1,-1]:
        w=(Q(-7,25),Q(24,25)) if p==1 else (Q(1),Q(0))
        target=pairmul(alpha,w);r=amplitudes[s,p]
        bound=abs(r[0]-target[0])+abs(r[1]-target[1])+amplitude_errors[s,p]+alpha_error
        comparisons.append({'s':s,'p':p,'bound':number(bound),'reflection_real':str(r[0]),
                            'reflection_imag':str(r[1]),'reflection_certificate_error':number(amplitude_errors[s,p])})
maximum=max(Q(row['bound']['rational']) for row in comparisons)
assert maximum<Q(176,10**15)
wrong_target_lower=Q(48,25)-maximum
assert wrong_target_lower>Q('1.91')
alpha_drop=mp.mpc(*[mp.mpf(v) for v in mutations[1]['remove_lambdaA_contact_diagnostic']['-1']])
drop_errors=[]
for row in mutations:
    for p in [1,-1]:
        rr=mp.mpc(*[mp.mpf(v) for v in row['remove_lambdaA_contact_diagnostic'][str(p)]])
        ww=mp.mpc(-7,24)/25 if p==1 else mp.mpf(1)
        drop_errors.append(abs(rr-alpha_drop*ww))
assert max(drop_errors)>mp.mpf('1e-3')

witness_path=ROOT/'WITNESS.json'
witness_path.write_text(json.dumps({'exact_parameters':{k:str(v) for k,v in P.items()},
                                    'certificates':witness},indent=2)+'\n')
result={'scope':'Fixed stationary scattering fiber only; no packet or all-future theorem',
        'assembly':'Full physical 16-state bit basis; 12-state Newton square-root proposal; two 32x32 exact-residual certificates with two RHS each',
        'author_programs_imported_or_run':False,
        'source_gap_entire_vacuum_bands':number(source_gap),'old_band_separation':number(old_gap),
        'free_halfline_sign_check':'Exact r=-z^4 at reference site 1; reversed RHS fails',
        'physical_scalar_reserve':number(P['scalar_reserve']),
        'incident_block_norms':{k:number(v) for k,v in loads.items()},
        'certificate_records':records,'comparison_bounds':comparisons,
        'certified_point_error':number(maximum),
        'wrong_conjugate_W_error_lower_bound':number(wrong_target_lower),
        'dropped_lambdaA_contact_diagnostic_max_error':str(max(drop_errors)),
        'witness_file':witness_path.name,'witness_sha256':hashlib.sha256(witness_path.read_bytes()).hexdigest(),
        'arithmetic':{'exact':'fractions.Fraction','proposal':'mpmath Newton iteration and inverse','proposal_decimal_digits':mp.mp.dps,'rational_proposal_denominator':DEN},
        'dimensions':{'internal':16,'source_excited':12,'boundary':32,'right_hand_sides_per_energy':2,'energies':2},
        'limits':{'cpu_seconds':90,'parent_wall_cap_seconds':120},
        'versions':{'python':sys.version,'numpy':np.__version__,'mpmath':mp.__version__},
        'elapsed_seconds':time.monotonic()-START}
(ROOT/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps({'certified_point_error':float(maximum),
                  'largest_reflection_certificate_error':float(max(amplitude_errors.values())),
                  'largest_inverse_bound':max(float(Q(r['inverse_bound']['rational'])) for r in records),
                  'wrong_conjugate_W_error_lower_bound':float(wrong_target_lower),
                  'removed_lambdaA_contact_diagnostic_error':float(max(drop_errors)),
                  'elapsed_seconds':result['elapsed_seconds'],'dimensions':result['dimensions']},indent=2))
