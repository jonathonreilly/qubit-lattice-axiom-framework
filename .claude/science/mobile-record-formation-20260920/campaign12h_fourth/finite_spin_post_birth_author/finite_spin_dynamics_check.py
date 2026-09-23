"""Full finite-spin no-event motion versus the proposed prepared flat limit.

The exact finite spin imposes its physical Gauss-compatible field interval;
there is no extra numerical field truncation of that dynamics. The proposed
flat reference is truncated only at a declared Dyson-controlled circulation
boundary. No scientific assertions about the limit follow from sizes alone.
"""
from pathlib import Path
from itertools import combinations
import hashlib,importlib.util,json,time
import numpy as np
from scipy.sparse import coo_matrix,csr_matrix,eye,diags
from scipy.sparse.linalg import expm_multiply

D=Path(__file__).resolve().parent
p=D/'flat_band_spin_correction_probe.py'
assert hashlib.sha256(p.read_bytes()).hexdigest()=='50df6b9c1a41db285fc0be25830a9a4a94dc8915106cd6ef036f52fba08e4e3b'
s=importlib.util.spec_from_file_location('flat',p);fmod=importlib.util.module_from_spec(s);s.loader.exec_module(fmod)
table=json.loads((D/'FLAT_COMPRESSED_OPERATORS_RESULTS.json').read_text())['rows']
K,delta,kappa=.4,.7,.3
times=np.linspace(0,.6,4)


def charges(number):
    minus_count=(number-4)//2
    return sorted(tuple(0 if a not in occupied else -1 if a in minus else 1 for a in range(8))
                  for occupied in combinations(range(8),number)
                  for minus in combinations(occupied,minus_count))


def fields(q,f):
    E=[];value=f
    for a in range(8):
        value+=q[a]-int(a%2==0);E.append(value)
    assert E[-1]==f
    return tuple(E)


def physical_states(number,S):
    result=[]
    for q in charges(number):
        offset=fields(q,0)
        low=max(-S-e for e in offset);high=min(S-e for e in offset)
        for f in range(low,high+1):result.append((q,f))
    return result


def shift_weight(E,k,S):
    value=1-E*(E+k)/(S*(S+1))
    assert value>-1e-14
    return np.sqrt(max(0.,value))


def matrix_from_triplets(triplets,shape):
    if not triplets:return csr_matrix(shape,dtype=complex)
    row,col,data=zip(*triplets)
    return coo_matrix((data,(row,col)),shape=shape,dtype=complex).tocsr()


def finite_target(S):
    words=physical_states(6,S);ix={s:i for i,s in enumerate(words)}
    W=np.array([sum(q[a]==0 for a in [0,2,4,6]) for q,f in words])
    sectors=[np.flatnonzero(W==a) for a in [0,1,2]]
    triplets=[]
    for col,(q,f) in enumerate(words):
        E=fields(q,f)
        for source,c in enumerate(q):
            if not c:continue
            for direction in [-1,1]:
                dest=(source+direction)%8
                if q[dest]:continue
                edge=source if direction==1 else dest;k=-direction*c
                if abs(E[edge]+k)>S:continue
                qq=list(q);qq[source]=0;qq[dest]=c
                out=(tuple(qq),f+(k if edge==7 else 0))
                triplets.append((ix[out],col,-shift_weight(E[edge],k,S)))
    T=matrix_from_triplets(triplets,(len(words),len(words)))
    difference=T-T.conj().T
    assert not difference.nnz or max(abs(difference.data))<1e-14
    A=T[sectors[1]][:,sectors[0]]
    Z=T[sectors[2]][:,sectors[1]]@A
    M=A.conj().T@A
    H2=-M;H4=M@M-Z.conj().T@Z/2
    pwords=[words[a] for a in sectors[0]]
    terminal=physical_states(8,S);tx={s:i for i,s in enumerate(terminal)}
    G=csr_matrix((len(pwords),len(pwords)),dtype=complex)
    for edge in range(8):
        u,v=edge,(edge+1)%8
        for sigma in [-1,1]:
            triplets=[]
            for col,a in enumerate(sectors[1]):
                q,f=words[a]
                if q[u] or q[v]:continue
                E=fields(q,f)
                if abs(E[edge]+sigma)>S:continue
                qq=list(q);qq[u]=sigma;qq[v]=-sigma
                out=(tuple(qq),f+(sigma if edge==7 else 0))
                triplets.append((tx[out],col,shift_weight(E[edge],sigma,S)))
            j=matrix_from_triplets(triplets,(len(terminal),len(sectors[1])))
            B=-j@A;G+=B.conj().T@B
    eta=K*S*(S+1)
    centered=eta*(H2+4*eye(len(pwords),format='csr'))+delta*H4-.5j*kappa*G
    hermitian=centered+.5j*kappa*G
    difference=hermitian-hermitian.conj().T
    assert not difference.nnz or max(abs(difference.data))<1e-10
    return pwords,centered,G


def flat_reference(cut):
    basis=[(kind,r,f) for kind in range(2) for r in range(6) for f in range(-cut,cut+1)]
    ix={s:i for i,s in enumerate(basis)}
    triplets=[]
    for col,(kind,r,f) in enumerate(basis):
        # Exact table has known integer coefficients; evaluate that polynomial
        # with an isolated SymPy symbol substitution, not Python eval.
        import sympy as sp
        row=next(a for a in table if a['kind']==kind and a['r']==r)
        expression=sp.sympify(row['electric_quadratic'])
        symbol=next(iter(expression.free_symbols))
        electric=float(expression.subs(symbol,f))
        triplets.append((col,col,K*electric-2j*kappa))
        for term in row['H4_terms']:
            target=(term['kind'],term['r'],f+term['circulation_shift'])
            if target in ix:triplets.append((ix[target],col,delta*int(term['coefficient'])))
    H=matrix_from_triplets(triplets,(len(basis),len(basis)))
    seeds=[(1,1,1),(0,0,0)]
    initial=np.zeros((len(basis),len(seeds)),complex)
    for col,seed in enumerate(seeds):initial[ix[seed],col]=1
    A=-1j*H
    propagated=expm_multiply(A,initial,start=times[0],stop=times[-1],num=len(times),traceA=A.diagonal().sum())
    # In interaction picture of the diagonal, each flux-changing step is
    # bounded by the off-diagonal H4 norm 4 delta; reaching the cut requires
    # at least cut-max|f_initial|+1 such steps. Comparing both full and
    # truncated Dyson terms gives twice the individual tail bound.
    # An exact rational geometric upper bound covers the infinite tail;
    # rounding the final float upward preserves this bound.
    import math
    n0=cut-max(abs(s[2]) for s in seeds)+1
    x=4*delta*float(times[-1])
    from fractions import Fraction
    x_upper=math.ceil(x)
    assert x_upper<n0+1
    exact_bound=Fraction(2*x_upper**n0*(n0+1),math.factorial(n0)*(n0+1-x_upper))
    tail=math.nextafter(float(exact_bound),math.inf)
    return basis,propagated,seeds,tail


def embedding(pwords,flat_basis):
    ix={s:i for i,s in enumerate(pwords)}
    triplets=[]
    for col,(kind,r,f) in enumerate(flat_basis):
        C=[(0,1),(1,2)][kind]
        state=fmod.state(C,r,f)
        for (q,E),coef in fmod.flat({state:1.}).items():
            key=(q,E[-1])
            if key in ix:triplets.append((ix[key],col,float(coef)*np.sqrt(2)))
    return matrix_from_triplets(triplets,(len(pwords),len(flat_basis)))


def main():
    flat_basis,limit,seeds,tail=flat_reference(32)
    rows=[]
    for S in [4,8,12,16,24,32]:
        started=time.monotonic()
        pwords,H,G=finite_target(S)
        J=embedding(pwords,flat_basis)
        initial=J@limit[0]
        assert np.max(abs(initial.conj().T@initial-np.eye(len(seeds))))<1e-13
        A=-1j*H
        actual=expm_multiply(A,initial,start=times[0],stop=times[-1],num=len(times),traceA=A.diagonal().sum())
        controls=[]
        for ti,t in enumerate(times):
            reference=J@limit[ti]
            for col,seed in enumerate(seeds):
                norm=float(np.vdot(actual[ti,:,col],actual[ti,:,col]).real)
                limnorm=float(np.vdot(limit[ti,:,col],limit[ti,:,col]).real)
                overlap=np.vdot(actual[ti,:,col],reference[:,col])
                error2=max(0.,norm+limnorm-2*overlap.real)
                expected=np.exp(-4*kappa*t)
                assert abs(limnorm-expected)<1e-11
                controls.append({'t':float(t),'initial_flat_label':list(seed),'state_norm_error':float(np.sqrt(error2)),
                                 'finite_spin_survival':norm,'flat_limit_survival':limnorm,
                                 'survival_error':abs(norm-expected)})
        row={'S':S,'eta':K*S*(S+1),'epsilon':float(np.sqrt(delta/(K*S*(S+1)))),
             'physical_P_dimension':len(pwords),'generator_nnz':H.nnz,
             'elapsed_seconds':time.monotonic()-started,'controls':controls}
        rows.append(row)
        print(json.dumps({'S':S,'Pdim':len(pwords),'elapsed_seconds':row['elapsed_seconds'],
                          'max_state_error':max(x['state_norm_error'] for x in controls)}),flush=True)
    out={'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'parameters':{'K':K,'delta':delta,'kappa':kappa},'flat_reference_cut':32,
         'flat_reference_Dyson_tail_norm_bound':tail,'rows':rows,
         'scope':'Author finite-spin convergence controls for two prepared flat vectors, not a proof or a full first-output replacement.'}
    p=D/'FINITE_SPIN_DYNAMICS_RESULTS.json';assert not p.exists();p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))


if __name__=='__main__':main()
