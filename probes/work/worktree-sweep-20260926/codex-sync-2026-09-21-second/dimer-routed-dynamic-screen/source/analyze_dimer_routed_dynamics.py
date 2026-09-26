#!/usr/bin/env python3
"""Prespecified whole-history analysis; exact Fourier signs checked before data."""
from pathlib import Path
import argparse,datetime,hashlib,itertools,json,math,sys
import numpy as np
import sympy as s

HERE=Path(__file__).resolve().parent
SEED=202609211855
BOOTSTRAPS=10000
TIMES=np.array([0,7/16,7/8,21/16,7/4],dtype=float)
METRICS=('propagation_residual','transverse_autocovariance','signed_cross_covariance','longitudinal_autocovariance')
sha=lambda p:hashlib.sha256(Path(p).read_bytes()).hexdigest()
def ident(p):
    p=Path(p);return dict(path=str(p.resolve()),bytes=p.stat().st_size,sha256=sha(p))
def save(p,x):Path(p).write_text(json.dumps(x,indent=2,allow_nan=False)+'\n')
def cross(q):
    x,y,z=q
    return np.array([[0,-z,y],[z,0,-x],[-y,x,0]],dtype=float)
def matrices(axis,t):
    unit=np.eye(3)[axis];K=cross(unit);long=np.outer(unit,unit);trans=np.eye(3)-long
    PL=np.kron(np.eye(2),long);PT=np.kron(np.eye(2),trans)
    D=np.block([[np.zeros((3,3)),1j*K],[-1j*K,np.zeros((3,3))]])
    theta=(2/7)*(2*np.pi)*t
    U=PL+np.cos(theta)*PT+np.sin(theta)*D
    return U,D,PL,PT

def exact_controls():
    # Derive the probability-current matrix directly from S, then compare its
    # six physical moments with the prescribed cosine/cross propagator.
    vectors=[(1,0,0),(-1,0,0),(0,1,0),(0,-1,0),(0,0,1),(0,0,-1)]
    E=s.Matrix.hstack(*map(s.Matrix,vectors+[(0,0,0)]*8))
    B=s.Matrix.hstack(*map(s.Matrix,[(0,0,0)]*6+list(itertools.product([-1,1],repeat=3))))
    W=s.sqrt(7)*E.col_join(B/2);p=s.ones(14,1)/14;C=s.diag(*p)-p*p.T
    assert s.simplify(W*C*W.T)==s.eye(6)
    checks=[]
    for axis in range(3):
        unit=s.eye(3)[:,axis]
        K=s.Matrix([[0,-unit[2],unit[1]],[unit[2],0,-unit[0]],[-unit[1],unit[0],0]])
        S=s.Matrix(14,14,lambda a,b:(unit.dot(E[:,a].cross(B[:,b])+E[:,b].cross(B[:,a])))/2)
        assert S*p==s.zeros(14,1)
        A=2*s.diag(*p)*S
        flux=s.zeros(6);flux[:3,3:]=-s.Rational(2,7)*K;flux[3:,:3]=s.Rational(2,7)*K
        assert s.simplify(W*A-flux*W)==s.zeros(6,14)
        # exp(-i A Q t) in these normalized moments.
        D=s.zeros(6);D[:3,3:]=s.I*K;D[3:,:3]=-s.I*K
        assert -s.I*flux==s.Rational(2,7)*D
        PL=s.diag(*[int(i%3==axis) for i in range(6)]);PT=s.eye(6)-PL
        assert D.conjugate().T==-D and D*D==-PT and PL*D==s.zeros(6)
        for t in TIMES:
            U,DD,LL,TT=matrices(axis,float(t))
            assert np.max(abs(U.conj().T@U-np.eye(6)))<2e-15
            # Deterministic ensemble with exactly identity second moment,
            # independent of any stochastic simulation or author C++ routine.
            initial=np.sqrt(6)*np.eye(6,dtype=complex)
            final=initial@U.T
            val=observables(initial,final,axis,float(t))
            expected=np.array([0,np.cos(4*np.pi*t/7),np.sin(4*np.pi*t/7),1])
            assert np.max(abs(val.mean(axis=0)-expected))<2e-15
        checks.append(dict(axis=axis,exact_current_and_covariance=True,unitary_full_propagator=True,
                           deterministic_identity_covariance_controls=True))
    return dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      analyzer=ident(__file__),bootstrap_seed=SEED,bootstrap_draws=BOOTSTRAPS,
      checks=checks,scope='Author exact algebra and independent-form deterministic second-moment controls, performed before opening production aggregate data. These are not separate-context independent verification.')

def observables(initial,final,axis,t):
    # Rows are independent histories. This function also handles the exact
    # six-vector identity-covariance control ensemble above.
    U,D,PL,PT=matrices(axis,t)
    predicted=initial@U.T
    residual=np.sum(abs(final-predicted)**2,axis=-1)/6
    transverse=np.real(np.sum(np.conj(initial@PT.T)*final,axis=-1))/4
    crosscov=np.real(np.sum(np.conj(initial@D.T)*final,axis=-1))/4
    longitudinal=np.real(np.sum(np.conj(initial@PL.T)*final,axis=-1))/2
    return np.stack([residual,transverse,crosscov,longitudinal],axis=-1)

def aggregate(x):
    return dict(mean=x.mean(axis=0).tolist(),standard_error=(x.std(axis=0,ddof=1)/math.sqrt(len(x))).tolist())

def check_identity(row):
    assert ident(row['path'])==row,row['path']

def analyze(root,out,control_path):
    assert not out.exists();out.mkdir(parents=True)
    control=json.loads(control_path.read_text());assert control['analyzer']==ident(__file__)
    mp=root/'MANIFEST.json';dp=root/'DISPATCH.json';sp=root/'SUMMARY.json'
    manifest=json.loads(mp.read_text());dispatch=json.loads(dp.read_text());summary=json.loads(sp.read_text())
    assert summary['statuses']=={'complete_verified_receipt':960},'Incomplete or failed declared run; no selected-subset analysis.'
    assert summary['manifest']==ident(mp)==dispatch['manifest']
    assert summary['dispatch']==ident(dp)
    assert len(manifest['jobs'])==len(summary['rows'])==960
    check_identity(manifest['binary']);check_identity(dispatch['wrapper'])
    for row in dispatch['source_snapshots']:
        check_identity(row['snapshot'])
        assert row['snapshot']['sha256']==row['original']['sha256'] and row['snapshot']['bytes']==row['original']['bytes']
    for row in manifest['geometry']:check_identity(row['file'])
    jobs={(j['N'],j['kind'],j['replicate']):j for j in manifest['jobs']}
    assert len(jobs)==960
    cells={};audit_rows=[];file_count=file_bytes=0
    for row in summary['rows']:
        key=(row['N'],row['kind'],row['replicate']);job=jobs[key]
        assert row['seed']==job['seed'] and row['status']=='complete_verified_receipt'
        check_identity(row['receipt']);receipt=json.loads(Path(row['receipt']['path']).read_text())
        assert receipt['job']==job and receipt['returncode']==0 and receipt['status']=='complete_verified_receipt'
        expected={job['output']+suffix for suffix in ['', '.state','.stdout','.stderr']}
        assert {x['path'] for x in receipt['outputs']}==expected
        for item in receipt['outputs']:
            check_identity(item);file_count+=1;file_bytes+=item['bytes']
        value=json.loads(Path(job['output']).read_text())
        assert value['N']==job['N'] and value['seed']==job['seed'] and value['mode']=='production'
        K=job['N']**3//2
        assert value['pairs']==K and value['channels']==5*K and value['minimum_nontrivial_cycle']>=job['N']//2
        assert value['key_permutation_verified'] and value['counts_verified']
        assert sum(value['color_counts'])==K and len(value['color_counts'])==14
        assert 0<=value['color_changes']<=value['accepted']<=value['attempts']
        assert value['gamma']==1 and value['k0']==1.1
        assert [x['t'] for x in value['snapshots']]==TIMES.tolist()
        raw=np.asarray([x['fields'] for x in value['snapshots']],dtype=float)
        assert raw.shape==(5,3,6,2) and np.isfinite(raw).all()
        fields=(raw[...,0]+1j*raw[...,1])*np.array([math.sqrt(7)]*3+[math.sqrt(7)/2]*3)
        cells.setdefault(key[:2],[]).append((job,value,fields))
        audit_rows.append(dict(N=key[0],kind=key[1],replicate=key[2],receipt=row['receipt']))
    results=[];per_history=[];rng=np.random.default_rng(SEED)
    for (N,kind),entries in sorted(cells.items()):
        entries.sort(key=lambda x:x[0]['replicate']);R=len(entries)
        assert R=={16:256,32:128,64:64,128:32}[N]
        assert [x[0]['replicate'] for x in entries]==list(range(1,R+1))
        fields=np.stack([x[2] for x in entries]) # history,time,mode,component
        values=np.empty((R,5,3,4))
        for t,time in enumerate(TIMES):
            for axis in range(3):values[:,t,axis,:]=observables(fields[:,0,axis],fields[:,t,axis],axis,float(time))
        assert np.max(abs(values[:,0,:,0]))<1e-25
        averaged=values.mean(axis=2);flat=averaged.reshape(R,-1)
        bootstrap=np.empty((BOOTSTRAPS,flat.shape[1]))
        for start in range(0,BOOTSTRAPS,500):
            end=min(start+500,BOOTSTRAPS)
            # Each row resamples complete histories; the same weights retain
            # every mode, time and metric from the selected history together.
            counts=rng.multinomial(R,np.ones(R)/R,size=end-start)
            bootstrap[start:end]=(counts@flat)/R
        low,high=np.quantile(bootstrap,[.025,.975],axis=0)
        cell=dict(N=N,kind=kind,histories=R,times=TIMES.tolist(),metrics=list(METRICS),
          by_mode=aggregate(values),mode_average={**aggregate(averaged),
            'bootstrap95_low':low.reshape(5,4).tolist(),'bootstrap95_high':high.reshape(5,4).tolist()},
          normalized_component_variances=aggregate(abs(fields)**2),
          attempts=aggregate(np.array([x[1]['attempts'] for x in entries],dtype=float)),
          accepted=aggregate(np.array([x[1]['accepted'] for x in entries],dtype=float)),
          color_changes=aggregate(np.array([x[1]['color_changes'] for x in entries],dtype=float)),
          wall_seconds=aggregate(np.array([x[1]['wall_seconds'] for x in entries],dtype=float)),
          all_key_and_count_receipts_verified=True)
        results.append(cell)
        for r,(job,value,_) in enumerate(entries):
            per_history.append(dict(N=N,kind=kind,replicate=job['replicate'],seed=job['seed'],
              by_time_mode_metric=values[r].tolist(),attempts=value['attempts'],accepted=value['accepted'],
              color_changes=value['color_changes'],wall_seconds=value['wall_seconds']))
    save(out/'PER_HISTORY.json',dict(metric_order=list(METRICS),times=TIMES.tolist(),mode_order=['x','y','z'],rows=per_history))
    save(out/'AUTHENTICATION.json',dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
      manifest=ident(mp),dispatch=ident(dp),summary=ident(sp),history_receipts=audit_rows,
      authenticated_history_files=file_count,authenticated_history_bytes=file_bytes,
      scope='Every production output byte authenticated against its saved receipt; all JSON fields consumed. Endpoint arrays hashed here, not decoded by this analyzer. Selected independent endpoint reconstruction is separate.'))
    report=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),analyzer=ident(__file__),
      sign_controls=ident(control_path),manifest=ident(mp),summary=ident(sp),per_history=ident(out/'PER_HISTORY.json'),
      authentication=ident(out/'AUTHENTICATION.json'),bootstrap=dict(draws=BOOTSTRAPS,seed=SEED,
       unit='Independent whole history, retaining all times, modes and components',interval='Pointwise percentile 95%; no simultaneous coverage or hypothesis-test selection.'),
      expected_mode_average=[[0,float(np.cos(4*np.pi*t/7)),float(np.sin(4*np.pi*t/7)),1] for t in TIMES],
      cells=results,scope='Declared finite-size stationary dynamic screen. No fitted exponent, damping law, thermodynamic proof, physical identification or first-completion preparation claim.')
    save(out/'RESULTS.json',report)
    print(json.dumps(dict(histories=len(per_history),cells=len(cells),authenticated_files=file_count,
                         results=ident(out/'RESULTS.json'),per_history=ident(out/'PER_HISTORY.json')),indent=2))

if __name__=='__main__':
    parser=argparse.ArgumentParser();parser.add_argument('--controls-only',type=Path)
    parser.add_argument('--root',type=Path);parser.add_argument('--output',type=Path);parser.add_argument('--controls',type=Path)
    args=parser.parse_args()
    if args.controls_only:
        assert not args.controls_only.exists();save(args.controls_only,exact_controls());print('Exact Fourier sign, covariance and propagator controls passed before aggregate data access.')
    else:
        assert args.root and args.output and args.controls
        analyze(args.root.resolve(),args.output.resolve(),args.controls.resolve())
