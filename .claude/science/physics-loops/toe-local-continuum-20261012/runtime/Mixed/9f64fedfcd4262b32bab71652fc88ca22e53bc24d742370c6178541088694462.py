"""Cell-embedded actual mixed vectors and infinite-polarization joint moments."""
import math
import numpy as np
from fixtures import packets,words,quadrature,reference_positive,continuum_cells
from reporting import arguments,Book

SETTINGS={'coarse':(8.,64.,1024,160,8192),
          'fine':(12.,96.,1792,240,16384),
          'high':(16.,128.,2560,320,32768)}

def serial(matrix):
    matrix=np.asarray(matrix)
    return {'real':matrix.real.tolist(),'imag':matrix.imag.tolist()}

def main():
    args,c=arguments(lambda p:p.add_argument('--resolution',choices=list(SETTINGS),default='coarse'))
    b=Book('microscopic_mixed_correlations',args);m=.8;v=1.3
    half,Q,nq,nx,padding=SETTINGS[args.resolution]
    fixtures=packets();wordlist=words();assigned=[wordlist[j//2] for j in range(6)]
    q,w=quadrature(nq,-Q,Q)
    pos=np.array([reference_positive(f,q,word,m,v,nx) for f,word in zip(fixtures,assigned)])
    exact_cov=2*pos.conj()@(w[None,:]*pos).T
    norms0=np.sqrt(2*np.sum(w[None,:]*np.abs(pos)**2,axis=1))
    norms1=np.sqrt(2*np.sum((w*q*q)[None,:]*np.abs(pos)**2,axis=1))
    norms2=np.sqrt(2*np.sum((w*q**4)[None,:]*np.abs(pos)**2,axis=1))
    projector_rate=norms1+(m*norms1+v*norms2)/(4*m)
    b.check('continuum_quadrature_unitarity',np.max(np.abs(norms0-1)),2e-7,resolution=args.resolution)
    for a in [.4,.2,.1,.05]:
        indices=np.arange(int(round(-half/a)),int(round(half/a)))
        D,B=c.matrices(indices,a,m,v)
        initial=np.array([f.cells(indices,a) for f in fixtures])
        zs=[];losses=[]
        for f,word in zip(initial,assigned):
            z,lost=c.lattice_word(f,word,a,D,B);zs.append(z);losses.extend(lost)
        zs=np.array(zs)
        projected=c.periodic_project(zs,indices,a,m,v,padding)
        cov=c.covariance(zs,projected)
        errors=[];squares=[]
        for j in range(6):
            cx=continuum_cells(pos[j],q,w,indices,a,m,v)
            square=float(np.vdot(zs[j],zs[j]).real+1-2*np.vdot(zs[j],cx).real)
            squares.append(square);errors.append(np.sqrt(max(0,square)))
            b.check('common_embedding_error_square',max(0,-square),2e-7,a=a,field=j,
                    raw_square=square,error=float(errors[-1]),error_over_a=float(errors[-1]/a))
        errors=np.array(errors)
        b.check('translation_outgoing_amplitude',max(losses,default=0.),2e-8,a=a)
        if a==.05:b.check('finest_vector_gross_error',np.max(errors),.4,a=a)
        pair_error=np.abs(cov-exact_cov)
        for i in range(6):
            for j in range(i+1,6):
                bound=2*(errors[i]+errors[j]+a*projector_rate[j])
                b.check('Q20_complex_pair_bound',pair_error[i,j],bound+2e-7,a=a,i=i,j=j,
                        analytic_bound=float(bound),pair_error_over_a=float(pair_error[i,j]/a))
        moment_data=[]
        for degree in [2,4,6]:
            lat=c.pfaffian(cov[:degree,:degree]);cont=c.pfaffian(exact_cov[:degree,:degree])
            delta=float(np.max(pair_error[:degree,:degree][np.triu_indices(degree,1)]))
            n=degree//2;matchings=math.prod(range(1,2*n,2));bound=matchings*n*delta*2**(n-1)
            b.check('Q21_ordered_moment_bound',abs(lat-cont),bound+2e-7,a=a,degree=degree,
                    analytic_bound=float(bound),lattice=[float(lat.real),float(lat.imag)],
                    continuum=[float(cont.real),float(cont.imag)])
            moment_data.append([float(lat.real),float(lat.imag),float(cont.real),float(cont.imag)])
        # Exact infinite-volume invariance target; finite box errors remain measured.
        common=[]
        for f in initial:
            z,lost=c.lattice_word(f,wordlist[0],a,D,B);common.append(z)
        common=np.array(common)
        common_cov=c.covariance(common,c.periodic_project(common,indices,a,m,v,padding))
        initial_cov=c.covariance(initial,c.periodic_project(initial,indices,a,m,v,padding))
        b.check('common_word_chosen_state_invariance',np.max(np.abs(common_cov-initial_cov)),2e-7,a=a)
        # Keep the generally nonzero mixed correlation change, with no false invariance check.
        b.check('mixed_covariance_finite',max(0,float(np.max(np.abs(cov-initial_cov)))-4),0,a=a,
                actual_mixed_change=float(np.max(np.abs(cov-initial_cov))))
        defects=[]
        for s,t,ell in [(.22,.19,.31),(-.18,-.21,-.27)]:
            relation_words=[([('b',s),('t',t),('b',-s)],c.q15_rhs(s,t,v),'Q15'),
                            ([('b',s),('x',ell),('b',-s)],c.q16_rhs(s,ell,v),'Q16')]
            for lhs,rhs,name in relation_words:
                left,_=c.lattice_word(initial[0],lhs,a,D,B)
                right,_=c.lattice_word(initial[0],rhs,a,D,B)
                defect=float(np.linalg.norm(left-right));defects.append(defect)
                b.check('finite_a_relation_defect_'+name,defect,.4 if a==.05 else 2.,a=a,s=s,t=t,ell=ell,
                        defect_over_a=defect/a,nonzero=bool(defect>1e-12))
        ell=.37*a
        combined,_=c.lattice_word(initial[0],[('x',ell),('x',-ell)],a,D,B)
        onecell,_=c.shift(initial[0],-1)
        b.check('floor_inverse_one_cell_identity',np.linalg.norm(combined-onecell),1e-13,a=a,
                distance_from_identity=float(np.linalg.norm(combined-initial[0])))
        b.check('resolution_comparison_payload',0,0,a=a,errors=errors.tolist(),
                error_squares=squares,covariance=serial(cov),continuum_covariance=serial(exact_cov),
                moments=moment_data,defects=defects)
    b.finish('Sparse finite boxes approximate actual infinite lattice flows. Brillouin covariance uses the supplied positive multiplier on a separately padded grid, not the finite-spin ground state. Continuum line integration uses independent flattened spacetime words and exact cell sinc factors. C5 compact polynomial packets test H2 arithmetic; the theorem is for compact smooth data. Finite parameter/spacing checks do not prove compact-uniform convergence. Each nonzero finite-a defect and mixed-state correlation change is retained. Bounds Q20/Q21 checked using measured vector/pair errors cannot alone prove their analytic rate.')

if __name__=='__main__':main()
