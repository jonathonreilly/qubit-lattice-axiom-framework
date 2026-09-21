#!/usr/bin/env python3
"""Full-state Taylor jet versus two-point response, then unfitted 3D scaling.

The finite-state and response matrices are assembled separately. Matrix
exponentials and the infinite-volume Green integral are numerical controls.
"""
from pathlib import Path
from itertools import product,combinations
import hashlib,json,time
import numpy as np
import scipy
from scipy.sparse import coo_matrix,csr_matrix,bmat,eye
from scipy.sparse.linalg import expm_multiply
from scipy.integrate import quad
from scipy.special import i0e

HERE=Path(__file__).resolve().parent
V=np.array([[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]],dtype=np.int64)


def relative_generator(side,dimension):
    origin=(0,)*dimension
    points=[r for r in product(range(side),repeat=dimension) if r!=origin]
    lookup={r:i for i,r in enumerate(points)};size=len(points)
    row=[];column=[];value=[]
    neighbors=[]
    for axis in range(dimension):
        for sign in (-1,1):
            r=[0]*dimension;r[axis]=sign%side;neighbors.append(tuple(r))
    for i,r in enumerate(points):
        degree=0
        for axis in range(dimension):
            for sign in (-1,1):
                target=list(r);target[axis]=(target[axis]+sign)%side;target=tuple(target)
                if target==origin: continue
                row.append(i);column.append(lookup[target]);value.append(1);degree+=1
        row.append(i);column.append(i);value.append(-degree)
    laplacian=coo_matrix((np.array(value,dtype=np.int64),(row,column)),shape=(size,size)).tocsr()
    assert not (laplacian-laplacian.T).nnz and np.max(abs(laplacian@np.ones(size)))==0
    source=np.zeros(size)
    for r in neighbors: source[lookup[r]]=1
    pair_weights=np.zeros(size)
    for y,z in combinations(neighbors,2):
        difference=tuple((z[i]-y[i])%side for i in range(dimension))
        assert difference!=origin
        pair_weights[lookup[difference]]+=1
    assert pair_weights.sum()==dimension*(2*dimension-1)
    return laplacian,source,pair_weights,lookup


def response(side,dimension,beta,kappa,v0,times):
    lap,source,pairs,lookup=relative_generator(side,dimension)
    size=lap.shape[0];lam=6*beta
    # D(t)=exp(-lambda*t) C(t) removes the variable coefficient in m3'.
    drift=2*kappa*side*lap.astype(float)-lam*eye(size,format='csr')
    zeros=csr_matrix((size,1))
    s2=csr_matrix(((4*beta/3)*v0*source).reshape(-1,1))
    s3=csr_matrix((-(4*beta/3)*v0*v0*source).reshape(-1,1))
    reward=csr_matrix((6*beta*v0*pairs).reshape(1,-1))
    zero_row=csr_matrix((1,size));zero=csr_matrix((1,1))
    matrix=bmat([[drift,zeros,s2,s3],[reward,csr_matrix([[-lam]]),zero,zero],
                 [zero_row,zero,csr_matrix([[-2*lam]]),zero],
                 [zero_row,zero,zero,csr_matrix([[-3*lam]])]],format='csr')
    initial=np.zeros(size+3);initial[-2:]=1
    values=expm_multiply(matrix,initial,start=float(times[0]),stop=float(times[-1]),num=len(times),endpoint=True)
    covariance=values[:,:size]*np.exp(lam*times[:,None])
    density=values[:,size]
    return covariance,density,lookup,dict(relative_states=size,sparse_nonzeros=matrix.nnz)


def full_cycle_jet(side,beta,kappa,v0,times):
    assert side==4 and beta==.2 and kappa==.75
    states=np.array(list(product(range(7),repeat=side)),dtype=np.int64)
    lookup={tuple(state):i for i,state in enumerate(states)};size=len(states)
    rows=[[] for _ in range(3)];cols=[[] for _ in range(3)];data=[[] for _ in range(3)]
    def insert(order,row,col,rate20):
        if row==col or rate20==0:return
        rows[order].extend([row,row]);cols[order].extend([col,row]);data[order].extend([rate20,-rate20])
    for row,state in enumerate(states):
        for x in range(side):
            new=state.copy();new[x],new[(x+1)%side]=new[(x+1)%side],new[x]
            insert(0,row,lookup[tuple(new)],int(20*kappa*side))
            if state[x]!=0:continue
            left,right=V[state[(x-1)%side]],V[state[(x+1)%side]]
            for a in range(1,7):
                first=int(V[a]@left);second=int(V[a]@right)
                coefficients=[1,first+second,first*second]
                new=state.copy();new[x]=a;col=lookup[tuple(new)]
                for order,coefficient in enumerate(coefficients): insert(order,row,col,4*coefficient)
    matrices=[]
    for order in range(3):
        scaled=coo_matrix((np.array(data[order],dtype=np.int64),(rows[order],cols[order])),shape=(size,size)).tocsr()
        assert np.max(abs(scaled@np.ones(size,dtype=np.int64)))==0
        matrices.append(scaled.astype(float).T/20)
    zero=csr_matrix((size,size))
    jet=bmat([[matrices[0] if row==col else matrices[row-col] if 0<row-col<3 else zero
               for col in range(4)] for row in range(4)],format='csr')
    probabilities=np.array([v0]+[(1-v0)/6]*6)
    initial=np.zeros(4*size);initial[:size]=np.prod(probabilities[states],axis=1)
    values=expm_multiply(jet,initial,start=float(times[0]),stop=float(times[-1]),num=len(times),endpoint=True).reshape(len(times),4,size)
    density=(states!=0).mean(axis=1)
    density_jet=np.einsum('tks,s->tk',values,density)
    covariance=[]
    for r in range(1,side):
        observable=np.mean(V[states,0]*V[np.roll(states,-r,axis=1),0],axis=1)
        covariance.append(values[:,1]@observable)
    # The vacancy at center 0 and its two neighbors are three distinct sites.
    conditional=(states[:,0]==0)*np.sum(V[states[:,1]]*V[states[:,-1]],axis=1)
    conditional_jet=values[:,1]@conditional
    mass_jet=values.sum(axis=2)
    assert np.max(abs(mass_jet-np.array([1,0,0,0])))<2e-12
    return density_jet,np.array(covariance).T,conditional_jet,dict(states=size,jet_states=4*size,nonzeros=jet.nnz,mass_error=float(np.max(abs(mass_jet-np.array([1,0,0,0])))))


def main():
    checks=[]
    def check(name,condition,detail=None):
        assert condition,(name,detail)
        checks.append(dict(name=name,passed=True,detail=detail));print('PASS:',name,json.dumps(detail),flush=True)
    times=np.linspace(0,.7,8);beta=.2;kappa=.75;v0=.4
    jet,pairs,conditional,jetmeta=full_cycle_jet(4,beta,kappa,v0,times)
    C,m3,lookup,meta=response(4,1,beta,kappa,v0,times)
    reference=1-v0*np.exp(-6*beta*times)
    check('complete_cycle_uniform_product_baseline',np.max(abs(jet[:,0]-reference))<3e-12,jetmeta)
    check('complete_cycle_first_two_density_coefficients_vanish',np.max(abs(jet[:,1:3]))<3e-12,dict(maximum=float(np.max(abs(jet[:,1:3])))))
    pair_error=max(np.max(abs(pairs[:,r-1]-C[:,lookup[(r,)]])) for r in range(1,4))
    check('complete_cycle_first_pair_response_matches_reflected_walk',pair_error<3e-12,dict(maximum_error=float(pair_error)))
    conditional_error=np.max(abs(conditional-3*v0*np.exp(-6*beta*times)*C[:,lookup[(2,)]]))
    check('complete_cycle_vacancy_weighted_pair_projection',conditional_error<3e-12,dict(maximum_error=float(conditional_error)))
    error=np.max(abs(jet[:,3]-m3))
    check('complete_cycle_third_density_coefficient_matches_closure',error<3e-12,
          dict(maximum_error=float(error),full_generator_final=float(jet[-1,3]),closed_response_final=float(m3[-1])))
    check('positive_third_response_at_positive_times',np.all(m3[1:]>0))
    out=HERE/'native_formation_centering';out.mkdir(exist_ok=True)
    np.savez_compressed(out/'four_cycle_jet.npz',times=times,density_jet=jet,full_pair_coefficients=pairs,
                        closed_pair_coefficients=C,closed_density_coefficient=m3,full_conditional_coefficient=conditional)
    G0,error=quad(lambda t:i0e(2*t)**3,0,np.inf,epsabs=1e-11,epsrel=1e-11,limit=400)
    Astar=15*G0-3
    check('Green_integral_and_positive_star_coefficient',Astar>0 and error<1e-9,
          dict(G0=G0,Astar=Astar,quadpack_error_estimate=error,
               limit='Numerical quadrature with an error estimate, not an interval certificate.'))
    beta=.2;kappa=.75;v0=.6;times=np.linspace(0,1,11)
    z=np.exp(-6*beta*times)
    target=(4*beta*Astar/kappa)*v0*v0*z*((1-z)-v0*(1-z*z)/2)
    records=[]
    for side in (4,8,16,24,32,48,64):
        started=time.monotonic();C,m3,lookup,meta=response(side,3,beta,kappa,v0,times)
        assert np.all(m3[1:]>0)
        path=out/f'three_dimensional_L{side}.npz'
        np.savez_compressed(path,times=times,density_coefficient=m3,scaled_density_coefficient=side*m3,
            target_scaled_density_coefficient=target,adjacent_pair=C[:,lookup[(1,0,0)]],
            axial_distance_two_pair=C[:,lookup[(2,0,0)]],diagonal_pair=C[:,lookup[(1,1,0)]])
        row=dict(side=side,beta=beta,kappa=kappa,v0=v0,elapsed_seconds=time.monotonic()-started,
            scaled_final_density_coefficient=float(side*m3[-1]),target_final_coefficient=float(target[-1]),
            relative_final_deviation=float(side*m3[-1]/target[-1]-1),
            raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),**meta)
        records.append(row);print(json.dumps(row),flush=True)
        (out/'COMPLETED_CASES.json').write_text(json.dumps(records,indent=2)+'\n')
    report=dict(source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),checks=checks,
        cases=records,versions=dict(numpy=np.__version__,scipy=scipy.__version__),
        scope='Numerical complete-generator Taylor-jet controls and exact-response finite-size calculations. These do not prove the heat-kernel limit or uniformity of the Taylor remainder in the alignment parameter.')
    (HERE/'NATIVE_FORMATION_CENTERING_RESULTS.json').write_text(json.dumps(report,indent=2)+'\n')
    print('TOTAL:',len(checks),'controls and',len(records),'3D cases',flush=True)


if __name__=='__main__': main()
