"""Post-PRE authorized comparison. Does not modify/import side-effect author runners."""
from pathlib import Path
import sys,json,hashlib,runpy,math
sys.dont_write_bytecode=True
import sympy as s
import numpy as np
from scipy.sparse.linalg import expm_multiply
from finite_control import model,effective,generator,npmat,superop

HERE=Path(__file__).resolve().parent
BASE=HERE.parent
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def read(n):return json.loads((BASE/n).read_text())
seals={'FINITE_RATE_FORMATION_AUTHOR_SEAL.json':'e0f07e9879e8332d17b1e96884c8942d21db4bdb4f7fe547d0bad3ed90ddd6ab','FORMATION_LOCALITY_AUTHOR_SEAL.json':'150c0877855ba00dd7369733c0cefd0639a003cce6b290873ee59f14f415acd2'}
bound={};nrows=0
for name,h in seals.items():
    assert sha(BASE/name)==h
    for row in read(name)['artifacts']:
        p=Path(row['path']);assert p.parent==BASE
        assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']
        bound[str(p)]=row;nrows+=1
pre=json.loads((HERE/'PRE_COMPARISON_SEAL.json').read_text())
assert sha(HERE/'PRE_COMPARISON_SEAL.json')=='f86695b6172745df8dc9ba8a1bfeaa60492ef7baf63a56bc55d045c5e8db951b'
for row in pre['sources']+pre['artifacts']:
    p=Path(row['path']);assert p.stat().st_size==row['bytes'] and sha(p)==row['sha256']

# Load only the already fully read balanced runner's definitions; main is not run.
author=runpy.run_path(str(BASE/'repeated_formation_check.py'))
stored=read('REPEATED_FORMATION_RESULTS.json')
localstored=read('FORMATION_LOCALITY_RESULTS.json')
darkstored=read('REPEATED_FORMATION_DARK_RESULTS.json')
assert stored['source_sha256']==sha(BASE/'repeated_formation_check.py')
assert localstored['source_sha256']==sha(BASE/'formation_locality_check.py')
assert darkstored['source_sha256']==sha(BASE/'repeated_formation_dark_check.py')
assert darkstored['recorded_results_sha256']==sha(BASE/'REPEATED_FORMATION_RESULTS.json')
for stem,source in [('REPEATED_FORMATION','repeated_formation_check.py'),('REPEATED_FORMATION_DARK','repeated_formation_dark_check.py'),('FORMATION_LOCALITY','formation_locality_check.py')]:
    receipt=read(stem+'_CHECK_RECEIPT.json');assert receipt['returncode']==0
    assert receipt['source_sha256']==sha(BASE/source)
    for stream in ('stdout','stderr'):assert receipt[stream+'_sha256']==sha(BASE/(stem+'_CHECK.'+stream))

delta=s.Rational(13,10);kappa=s.Rational(7,10)
models={'star_2':model(3,{0},[(0,1),(0,2)]),'star_4':model(5,{0},[(0,1),(0,2),(0,3),(0,4)]),'two_A_path':model(4,{0,2},[(0,1),(2,1),(2,3)])}
mappingrows=[];localrows=[]
for name,m in models.items():
    am=author['tree_model'](None if name=='two_A_path' else int(name[-1]))
    byq={q:i for i,(E,q) in enumerate(m['states'])};dim=len(m['states']);R=s.zeros(dim)
    for col,(q,E) in enumerate(am['states']):
        i=byq[tuple(q)];R[i,col]=1
        expected=list(m['states'][i][0])
        if name=='two_A_path':expected[1]*=-1
        assert tuple(expected)==tuple(E)
    assert R.T*m['T']*R==s.Matrix(am['T'])
    assert R.T*m['W']*R==s.Matrix(am['W'])
    inv=next(x for x in stored['inventories'] if x['model']==name)
    assert inv['physical_basis']==[{'q':list(q),'E':list(E)} for q,E in am['states']]
    for e,(tail,head) in enumerate(am['edges']):
        for ci,c in enumerate((-1,1)):
            ownc=c if tail in am['A_sites'] else -c
            ownj=m['Js'][2*e+(0 if ownc==1 else 1)]
            assert R.T*ownj*R==s.Matrix(am['resolved'][2*e+ci])
        assert R.T*m['coherent'][e]*R==s.Matrix(am['coherent'][e])
    losslist=[]
    for coh in (False,True):
        kind='coherent' if coh else 'resolved'
        P,X,Z,H,Js=effective(m,delta,kappa,coh)
        C=P.T*R[:,list(map(int,am['p']))]
        aH,aJs,*_=author['effective'](am,kind,float(delta),float(kappa))
        assert np.max(np.abs(aH-npmat(C.T*H*C)))<1e-13
        # Author jumps have the immaterial overall opposite sign and reversed charge order.
        if coh:order=list(range(len(Js)))
        else:
            order=[]
            for e,(tail,head) in enumerate(am['edges']):
                for c in (-1,1):
                    ownc=c if tail in am['A_sites'] else -c
                    order.append(2*e+(0 if ownc==1 else 1))
        assert all(np.max(np.abs(aJ+npmat(C.T*Js[i]*C)))<1e-13 for aJ,i in zip(aJs,order))
        # Exact local decomposition, independently assembled from hole projectors.
        Hsum=s.zeros(P.cols);Jsum=[s.zeros(P.cols) for _ in Js]
        bare=m['coherent' if coh else 'Js']
        for a in am['A_sites']:
            Qa=s.diag(*[int(w==1 and q[a]==0) for (E,q),w in zip(m['states'],m['Ws'])])
            Xa=Qa*X
            Hsum+=(P.T*(delta*m['T'])*Xa+Xa.H*(delta*m['T'])*P)/2
            for i,j in enumerate(bare):Jsum[i]+=s.sqrt(kappa)*P.T*j*Xa
        assert s.simplify(H-Hsum)==s.zeros(P.cols)
        assert all(s.simplify(a-b)==s.zeros(P.cols) for a,b in zip(Js,Jsum))
        G=s.simplify(sum((j.H*j for j in Js),s.zeros(P.cols)))
        losslist.append(G)
        source=next(x for x in localstored['controls'] if x['model']==name and x['instrument']==kind)
        rows=source['basis_state_formation_rates']
        if rows:
            assert len(rows)==P.cols
            ids=[i for i,w in enumerate(m['Ws']) if not w]
            ownpos={m['states'][i][1]:j for j,i in enumerate(ids)}
            for row in rows:
                q=tuple(row['q']);k=sum(x==0 for x in q[1:])
                prediction=2*k*(k-1)*kappa*delta**2/(delta**2+kappa**2*(k-1)**2) if k else 0
                assert s.simplify(G[ownpos[q],ownpos[q]]-prediction)==0
                assert s.simplify(prediction-s.sympify(row['rate']))==0
        localrows.append({'model':name,'instrument':kind,'exact_star_decomposition':True,'stored_basis_rates_checked':len(rows)})
    assert losslist[0]==losslist[1]
    mappingrows.append({'model':name,'complete_basis_size':dim,'all_bare_T_W_and_birth_operators_equal_after_mapping':True,'path_orientation_note':'middle electric field and charge-mark orientation reversed' if name=='two_A_path' else 'same orientation','effective_H_and_jumps_equal_up_to_common_jump_sign':True})

print('Source identities, complete-basis mappings and local decomposition verified.',flush=True)
# Difference between this packet's trace-normalized map and author's raw map.
m=models['two_A_path'];equivalence=[]
for coh in (False,True):
    P,X,Z,H,Js=effective(m,delta,kappa,coh);J0=[s.sqrt(kappa)*j for j in m['coherent' if coh else 'Js']]
    for i in range(P.cols):
        for j in range(P.cols):
            r=s.zeros(P.cols);r[i,j]=1
            correction=-P*(X.H*X*r+r*X.H*X)*P.T/2
            assert generator(delta*m['W'],J0,correction)==s.zeros(P.rows)
            raw=X*r*X.H+Z*r*P.T+P*r*Z.H
            first=X*r*P.T+P*r*X.H
            L1first=-s.I*delta*(m['T']*first-first*m['T'])
            assert s.simplify(generator(delta*m['W'],J0,raw)+L1first-P*generator(H,Js,r)*P.T)==s.zeros(P.rows)
    equivalence.append({'instrument':'coherent' if coh else 'resolved','matrix_units':P.cols**2,'normalization_difference_fast_annihilated':True,'author_unnormalized_identity_exact':True})

# Exact spectral weights reconstructed from own PRE electric operators.
m=models['star_4'];p3=[i for i,w in enumerate(m['Ws']) if w==0 and m['Ns'][i]==3]
q3=[i for i,w in enumerate(m['Ws']) if w==1 and m['Ns'][i]==3]
q1=[i for i,w in enumerate(m['Ws']) if w==1 and m['Ns'][i]==1]
g=m['states'].index(((0,0,0,0),(1,0,0,0,0)))
A=m['T'].extract(q3,p3);M=A.T*A
lams=[0,1,2,3,5,6];projs={}
for lam in lams:
    E=s.eye(18)
    for mu in lams:
        if mu!=lam:E=E*(M-mu*s.eye(18))/(lam-mu)
    assert E*E==E and M*E==lam*E
    projs[lam]=E
weights={}
for kind in ['resolved','coherent']:
    vecs=[j.extract(p3,q1)*m['T'].extract(q1,[g]) for j in m['Js' if kind=='resolved' else 'coherent']]
    rho=sum((v*v.T for v in vecs),s.zeros(18))/24
    weights[kind]={lam:s.trace(E*rho) for lam,E in projs.items()}
    assert {str(k):str(v) for k,v in weights[kind].items()}==darkstored['instruments'][kind]['spectral_weights']

def law(t,d,k,kind,degree):
    r0=2*degree*(degree-1)*k*d*d/(d*d+k*k*(degree-1)**2)
    p0=math.exp(-r0*t)
    if degree==2:return {'0':p0,'1':1-p0}
    b=2*k*d*d/(d*d+k*k);p1=float(weights[kind][0])*(1-p0)
    for lam,w in weights[kind].items():
        if not lam or not w:continue
        r=b*lam
        p1+=float(w)*(r0*t*p0 if abs(r-r0)<1e-12 else r0*(p0-math.exp(-r*t))/(r-r0))
    return {'0':p0,'1':p1,'2':1-p0-p1}

all_errors=[];energy_identity_errors=[];all_rows=0
for group in stored['full_dynamics_checks']:
    degree=int(group['model'][-1]);eps=group['epsilon'];d=group['delta'];k=group['kappa']
    for row in group['rows']:
        all_rows+=1
        prediction=law(row['time'],d,k,group['instrument'],degree)
        all_errors.extend(abs(prediction[a]-v) for a,v in row['effective_event_count_probabilities'].items())
        for key in ['actual_event_count_probabilities','effective_event_count_probabilities']:
            assert abs(sum(row[key].values())-1)<3e-11 and min(row[key].values())>-3e-11
        assert abs(row['trace_norm_error']/eps-row['error_over_epsilon'])<1e-13
        energy=sum(2*int(a)*v for a,v in row['effective_event_count_probabilities'].items())
        energy_identity_errors.append(abs(energy-row['effective_energy_over_Delta']))
        assert abs(row['actual_energy_over_Delta']-energy)<=degree*row['trace_norm_error']+eps*degree+1e-10
assert max(all_errors)<3e-12 and max(energy_identity_errors)<3e-12

# Independent full Liouvillian reconstruction of only the two explicitly quoted endpoints.
numeric=[]
for kind in ['coherent','resolved']:
    m=models['star_4'];d=1.3;k=.7;eps=.025;t=2.;dim=len(m['states'])
    initial=np.zeros((dim,dim),complex);initial[g,g]=1
    P,X,Z,H,Js=effective(m,delta,kappa,kind=='coherent');Pn=npmat(P)
    L=superop(d*npmat(m['W'])/eps**2+d*npmat(m['T'])/eps,[math.sqrt(k)*npmat(j)/eps for j in m['coherent' if kind=='coherent' else 'Js']])
    rho=expm_multiply(t*L,initial.reshape(-1,order='F'),traceA=t*L.diagonal().sum()).reshape((dim,dim),order='F')
    Le=superop(npmat(H),[npmat(j) for j in Js]);small=Pn.T@initial@Pn
    target=Pn@expm_multiply(t*Le,small.reshape(-1,order='F'),traceA=t*Le.diagonal().sum()).reshape(small.shape,order='F')@Pn.T
    err=float(np.abs(np.linalg.eigvalsh((rho-target+rho.conj().T-target.conj().T)/2)).sum())
    full=[i for i,n in enumerate(m['Ns']) if n==5]
    p2=float(np.trace(rho[np.ix_(full,full)]).real)
    ref=next(z for z in stored['full_dynamics_checks'] if z['model']=='star_4' and z['instrument']==kind and z['epsilon']==eps)['rows'][-1]
    assert abs(p2-ref['actual_event_count_probabilities']['2'])<3e-11
    assert abs(err-ref['trace_norm_error'])<3e-11
    numeric.append({'instrument':kind,'epsilon':eps,'time':t,'independent_full_probability':p2,'independent_trace_error':err,'probability_difference':abs(p2-ref['actual_event_count_probabilities']['2']),'error_difference':abs(err-ref['trace_norm_error'])})

out={'author_seal_rows_authenticated':nrows,'author_unique_bound_paths':len(bound),'pre_bindings_unchanged':len(pre['sources'])+len(pre['artifacts']),'excluded_different_scaling_packet':'Authenticated only: FINITE_RATE_RENEWED_FORMATION_EXACT_STAR.md and its different-scaling checker/results/logs/spec. No theorem disposition given.','basis_and_rate_mapping':mappingrows,'locality':localrows,'embedding_equivalence':equivalence,'exact_spectral_weights':{k:{str(a):str(b) for a,b in v.items()} for k,v in weights.items()},'stored_effective_count_rows_checked':all_rows,'maximum_effective_count_difference':max(all_errors),'maximum_effective_energy_identity_difference':max(energy_identity_errors),'selective_full_liouvillian_reconstruction':numeric,'author_scientific_sources_modified':False,'author_grid_rerun':False}
(HERE/'COMPARISON_RESULTS.json').write_text(json.dumps(out,indent=2)+'\n')
print(json.dumps(out,indent=2))
