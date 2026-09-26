#!/usr/bin/env python3
"""Freeze an exact projection check and parameter-free winding benchmarks."""
from pathlib import Path
import argparse, datetime, hashlib, itertools, json, math
import numpy as np
import sympy as s
from scipy.sparse import coo_matrix
from scipy.linalg import expm
import dimer_routed_transport_check as base

HERE=Path(__file__).resolve().parent
TIMES=[0,7/16,7/8,21/16,7/4]

def ident(p):
    p=Path(p);return dict(path=str(p.resolve()),bytes=p.stat().st_size,
                         sha256=hashlib.sha256(p.read_bytes()).hexdigest())

def local_projection():
    words=np.array(list(itertools.product(range(14),repeat=4)),dtype=np.int64)
    l,a,b,r=words.T;rows=[]
    for axis in range(3):
        T=base.S2[axis]
        drive=T[l,a]+T[a,r]-T[l,b]-T[b,r]
        numerator=22+5*drive
        matrices=[]
        for position in range(4):
            acc=np.zeros((14,14),dtype=np.int64)
            np.add.at(acc,(a,words[:,position]),numerator)
            np.add.at(acc,(b,words[:,position]),-numerator)
            matrix=s.Matrix(acc.tolist())/(40*14**3)
            if position in (0,3):target=s.Matrix(T.tolist())/56
            else:target=(1 if position==1 else -1)*s.Rational(11,20)*(s.eye(14)-s.ones(14)/14)
            assert matrix==target
            matrices.append(str(matrix))
        rows.append(dict(axis=axis,contexts=len(words),all_four_conditional_coefficients_exact=True,
                         actual_rate_denominator=40,context_coefficient='T_delta/56 = A_delta/4'))
    return rows

def integer_complex_moment(ar,ai,br,bi):
    bound=2*len(ar)*max(int(abs(ar).max()),int(abs(ai).max()))*max(int(abs(br).max()),int(abs(bi).max()))
    assert bound<2**63
    real=ar.T@br+ai.T@bi;imag=ai.T@br-ar.T@bi
    return s.Matrix(real.tolist())+s.I*s.Matrix(imag.tolist())

def flux(q,gamma=1):
    x,y,z=q;C=np.array([[0,-z,y],[z,0,-x],[-y,x,0]],dtype=float)
    return np.block([[np.zeros((3,3)),-2*gamma*C/7],[2*gamma*C/7,np.zeros((3,3))]])

def closure_control():
    words=np.array(list(itertools.product(range(14),repeat=4)),dtype=np.int64)
    count=len(words);powers=14**np.arange(3,-1,-1);indices=np.arange(count)
    feature=np.column_stack((2*base.EV,base.BV))
    zr=feature[words[:,0]]-feature[words[:,2]]
    zi=-feature[words[:,1]]+feature[words[:,3]]
    covariance=integer_complex_moment(zr,zi,zr,zi)*s.Rational(7,16*count)
    assert covariance==s.eye(6)
    rows=[];axis=2;T=base.S2[axis]
    C=s.Matrix([[0,-1,0],[1,0,0],[0,0,0]])
    for gamma in (0,1):
        rr=[];cc=[];data=[]
        for u in range(4):
            l,a,b,r=words[:,[(u-1)%4,u,(u+1)%4,(u+2)%4]].T
            h=T[l,a]+T[a,r]-T[l,b]-T[b,r]
            rates=22+5*gamma*h
            swapped=words.copy();swapped[:,[u,(u+1)%4]]=swapped[:,[(u+1)%4,u]]
            rr.extend([indices,indices]);cc.extend([swapped@powers,indices]);data.extend([rates,-rates])
        Q40=coo_matrix((np.concatenate(data),(np.concatenate(rr),np.concatenate(cc))),shape=(count,count),dtype=np.int64).tocsr()
        assert np.max(abs(np.asarray(Q40.sum(axis=0))))==0
        assert np.max(abs(np.asarray(Q40.sum(axis=1))))==0
        dr,di=Q40@zr,Q40@zi;ddr,ddi=Q40@dr,Q40@di
        B=integer_complex_moment(dr,di,zr,zi)*s.Rational(7,16*count*40)
        second=integer_complex_moment(ddr,ddi,zr,zi)*s.Rational(7,16*count*40**2)
        flux_symbol=s.zeros(6);flux_symbol[:3,3:]=-s.Rational(2*gamma,7)*C;flux_symbol[3:,:3]=s.Rational(2*gamma,7)*C
        expected=-s.Rational(11,10)*s.eye(6)+s.I*flux_symbol/2
        assert B==expected
        R=integer_complex_moment(dr,di,dr,di)*s.Rational(7,16*count*40**2)-B*B.conjugate().T
        assert R==R.conjugate().T
        assert second==B*B-R
        if gamma==0:assert R==s.zeros(6)
        else:assert R!=s.zeros(6) and s.trace(R)>0
        eig=np.linalg.eigvalsh(np.array(R,dtype=complex))
        assert min(eig)>-1e-13
        rows.append(dict(gamma=gamma,states=count,cycle_positions=4,
                         exact_initial_covariance_identity=True,
                         exact_first_derivative=str(B),exact_memory_curvature_matrix=str(R),
                         exact_memory_trace=str(s.trace(R)),exact_second_derivative_identity=True,
                         projected_exponential_exact_in_constant_rate_case=gamma==0,
                         numerical_memory_eigenvalues=eig.tolist()))
    return rows

def predictions():
    rows=[]
    for N in (16,32,64,128,256):
        for axis in range(3):
            Q=2*np.pi*np.eye(3)[axis];k=Q/N
            displacement=base.AXES-np.array([1,0,0])
            phase=displacement@k
            damping=2*1.1*float(np.sum(np.sin(phase/2)**2))
            effective=np.sum((np.sin(2*phase)-np.sin(phase))[:,None]*base.AXES,axis=0)/2
            B=-damping*np.eye(6)-1j*flux(effective)
            alternative=-damping*np.eye(6,dtype=complex)
            for delta,z in zip(base.AXES,phase):
                alternative+=.5j*(np.sin(z)-np.sin(2*z))*flux(delta)
            assert np.max(abs(alternative-B))<1e-14
            unit=np.eye(3)[axis];long=np.outer(unit,unit)
            PL=np.kron(np.eye(2),long);PT=np.eye(6)-PL
            D=-1j*flux(unit)/(2/7)
            expected=[]
            for time in TIMES:
                continuum=expm(-1j*flux(Q)*time)
                projected=expm(N*time*B)
                value=[2-float(np.trace(continuum.conj().T@projected).real)/3,
                       float(np.trace(PT@projected).real)/4,
                       float(np.trace(D.conj().T@projected).real)/4,
                       float(np.trace(PL@projected).real)/2]
                if time==0:assert np.max(abs(np.array(value)-[0,1,0,1]))<1e-14
                assert value[0]>=-1e-13
                expected.append(value)
            rows.append(dict(N=N,axis=axis,microscopic_damping=damping,
                             effective_wavevector=effective.tolist(),times=TIMES,
                             projected_benchmark=expected))
    return rows

def main():
    parser=argparse.ArgumentParser();parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args();assert not args.output.exists();args.output.mkdir(parents=True)
    local=local_projection();print('exact local conditional projections passed',flush=True)
    closure=closure_control();print('exact finite-cycle memory-curvature controls passed',flush=True)
    values=predictions();print('all 15 winding size/mode predictions frozen without aggregate access',flush=True)
    result=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                sources=[ident(HERE/name) for name in (Path(__file__).name,
                   'DIMER_ROUTED_FINITE_WAVELENGTH_PROJECTION.md','dimer_routed_transport_check.py')],
                local_projection=local,closure_control=closure,predictions=values,
                metric_order=['propagation_residual','transverse_autocovariance','signed_cross_covariance','longitudinal_autocovariance'],
                timing='Post-outcome after original mode averages, frozen before per-axis comparison and before any N256 observable access.',
                scope='Exact projection and finite curvature controls; exponentiated projected generator is an unproved closure benchmark for gamma=1, with no fitted parameter.')
    (args.output/'RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps({'result':ident(args.output/'RESULTS.json'),'memory_traces':[r['exact_memory_trace'] for r in closure]},indent=2))

if __name__=='__main__':main()
