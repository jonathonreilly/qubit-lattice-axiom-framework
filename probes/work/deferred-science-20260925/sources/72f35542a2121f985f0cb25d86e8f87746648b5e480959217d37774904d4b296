"""Finite Fourier diagnostics of the independently derived quadratic form.

Exact integer statements are checked separately from floating spectral rows.
Finite-g rows use exact Gaussian characteristic functions before cutoff; the
physical compact-packet replacement is a separate tail estimate in PRE.md.
"""
from pathlib import Path
from hashlib import sha256
from itertools import product
import json
import time
import numpy as np
import magnetic_increment_control as primitive


def fourier_basis(side, vertices, edges, axes):
    nv=len(vertices);columns=[];freq=[];labels=[]
    for integer in product(range(side),repeat=3):
        if integer==(0,0,0):continue
        k=2*np.pi*np.array(integer)/side
        q=1-np.exp(-1j*k)
        # A v=0 implements outgoing-minus-incoming discrete divergence.
        _,_,vh=np.linalg.svd(q.reshape(1,3),full_matrices=True)
        polarizations=vh.conj().T[:,1:]
        omega=float(np.sqrt(np.vdot(q,q).real))
        for pol in range(2):
            column=[]
            for (a,b),axis in zip(edges,axes):
                mu=next(i for i,s in enumerate(axis) if s)
                sign=axis[mu];tail=vertices[a] if sign==1 else vertices[b]
                column.append(sign*np.exp(1j*np.dot(k,tail))*polarizations[mu,pol]/np.sqrt(nv))
            columns.append(column);freq.append(omega);labels.append([integer,pol])
    return np.asarray(columns,dtype=complex).T,np.asarray(freq),labels


def flow_row(flow,basis):
    return sum((power*basis[ed] for ed,power in flow),np.zeros(basis.shape[1],complex))


def control(side):
    base=Path(__file__).parent
    path=base/f'LAURENT_DATA_L{side}.json';data=json.loads(path.read_text())
    vertices=data['vertices'];edges=data['edges'];axes=data['signed_axes']
    phi,omega,labels=fourier_basis(side,vertices,edges,axes)
    rank=len(omega)
    # Check every Fourier vector's Gauss condition, norm and curl eigenvalue
    # through local coordinate matrices; this is not an author mode builder.
    divergence=np.zeros((len(vertices),len(edges)))
    for ed,(a,b) in enumerate(edges):divergence[a,ed]=1;divergence[b,ed]=-1
    _,_,_,neighbors,_,eid,_=primitive.graph(side)
    aset=set(neighbors)
    crows=[]
    index={tuple(x):i for i,x in enumerate(vertices)}
    def segment(x,y):
        if x in aset:return eid[x,y],1
        return eid[y,x],-1
    for x0 in vertices:
        for mu in range(3):
            for nu in range(mu+1,3):
                loop=[]
                for sm,sn in ((0,0),(1,0),(1,1),(0,1)):
                    x=x0.copy();x[mu]=(x[mu]+sm)%side;x[nu]=(x[nu]+sn)%side
                    loop.append(index[tuple(x)])
                f=()
                for x,y in zip(loop,loop[1:]+loop[:1]):
                    ed,s=segment(x,y);f=primitive.add(f,ed,s)
                crows.append(f)
    curl_phi=np.asarray([flow_row(f,phi) for f in crows])
    # Avoid a second large full spectral decomposition.
    curl_adjoint_phi=np.zeros_like(phi)
    for f,row in zip(crows,curl_phi):
        for ed,k in f:curl_adjoint_phi[ed]+=k*row
    mode_checks={"orthonormality_max_residual":float(np.max(np.abs(phi.conj().T@phi-np.eye(rank)))),
                 "divergence_max_residual":float(np.max(np.abs(divergence@phi))),
                 "curl_eigenvalue_max_residual":float(np.max(np.abs(curl_adjoint_phi-phi*omega**2))),
                 "expected_transverse_rank":2*(side**3-1),"actual_rank":rank}
    assert max(mode_checks[k] for k in mode_checks if k.endswith('residual'))<1e-11
    mask=np.asarray([a/b for a,b in data['electric_mask']]);missing=1-mask
    terms=data['defect_cosines']
    alpha=np.asarray([t['cos_coefficient'] for t in terms],float)
    cphi=np.asarray([flow_row(t['flow'],phi) for t in terms])
    relative_factor=np.concatenate((np.sqrt(missing[missing>0,None]/2)*phi[missing>0],
                                     np.sqrt(alpha[:,None]/8)*cphi/omega),axis=0)
    gram=relative_factor@relative_factor.conj().T
    maxloss=float(np.linalg.eigvalsh(gram)[-1])
    unique=np.unique(np.round(omega,12))
    bands=[]
    for upper in unique[:min(7,len(unique))]:
        selected=omega<=upper+1e-10
        block=relative_factor[:,selected]
        rho=float(np.linalg.eigvalsh(block@block.conj().T)[-1])
        nk=int(np.sum(selected))//2
        sufficient=(133/3)*nk/side**3
        bands.append({"max_reference_frequency_times_tau":float(upper),"momentum_count":nk,
                      "transverse_mode_count":int(np.sum(selected)),
                      "trace_bound_loss":sufficient,"actual_largest_relative_loss_floating":rho,
                      "minimum_actual_to_reference_ratio_floating":1-rho})
    central=next(t for t in terms if t['cos_coefficient']==170)
    central_integer=np.zeros(len(edges),dtype=np.int64)
    for ed,k in central['flow']:central_integer[ed]=k
    curl_c=np.asarray([sum(k*central_integer[ed] for ed,k in f) for f in crows],dtype=np.int64)
    central_norm2=int(central_integer@central_integer)
    curl_norm2=int(curl_c@curl_c)
    assert central_norm2==4 and curl_norm2==28
    projection=phi.conj().T@central_integer
    denom=float(np.sum(omega*np.abs(projection)**2))
    f=np.sqrt(omega)*projection/np.sqrt(denom)
    reference=float(np.sum(omega*np.abs(f)**2))
    r=np.sqrt(omega)*f
    kinetic_loss=float(np.sum(missing*np.abs(phi@r)**2)/2)
    magnetic_loss=float(np.sum(alpha*np.abs(cphi@(f/np.sqrt(omega)))**2)/8)
    actual=reference-kinetic_loss-magnetic_loss
    witness={"definition":"f=Omega^(1/2)c_p/sqrt(<c_p,Omega c_p>)",
             "exact_c_p_norm_squared":central_norm2,"exact_curl_c_p_norm_squared":curl_norm2,
             "c_p_Omega_c_p_floating":denom,"reference_energy_times_tau":reference,
             "kinetic_loss_times_tau":kinetic_loss,"magnetic_loss_times_tau":magnetic_loss,
             "actual_increment_limit_times_tau":actual,
             "exact_analytic_upper_bound_times_tau_numerator":-312,
             "bound_denominator_c_p_Omega_c_p_floating":denom,
             "actual_to_reference_ratio":actual/reference}
    # Exact Gaussian characters, not physical compact finite-g vectors.
    prepared_rows=np.asarray([flow_row(t['flow'],phi) for t in data['prepared_polynomial'] if t['flow']])
    coefficients=np.asarray([t['coefficient'] for t in data['prepared_polynomial'] if t['flow']])
    variances=np.sum(np.abs(prepared_rows)**2/omega,axis=1)/2
    excess=np.abs(prepared_rows@(f/np.sqrt(omega)))**2
    finiteg=[]
    kinetic=reference/2-kinetic_loss
    for g in (.2,.1,.05,.025):
        magnetic=float(-np.sum(coefficients*excess*np.exp(-g*g*variances/2))/8)
        inc=kinetic+magnetic
        finiteg.append({"g":g,"uncompacted_Gaussian_increment_times_tau":inc,
                        "error_from_limit":inc-actual,"error_over_g_squared":(inc-actual)/(g*g)})
    return {"side":side,"input_data_sha256":sha256(path.read_bytes()).hexdigest(),
            "mode_checks":mode_checks,"relative_form_rank_bound":relative_factor.shape[0],
            "global_minimum_actual_to_reference_ratio_floating":1-maxloss,
            "bands":bands,"exact_negative_witness":witness,"finite_g_Gaussian_rows":finiteg}


def main():
    start=time.perf_counter()
    rows=[control(side) for side in (6,8)]
    print(json.dumps({'rows':rows,'floating_spectral_results_are_not_interval_certificates':True,
                      'source_sha256':sha256(Path(__file__).read_bytes()).hexdigest(),
                      'elapsed_seconds':time.perf_counter()-start},indent=2))


if __name__=='__main__':main()
