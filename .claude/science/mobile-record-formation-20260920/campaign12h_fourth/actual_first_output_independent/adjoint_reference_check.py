import sys
sys.dont_write_bytecode=True
from consequence_check import *

def main():
    K,delta,kappa=.4,.7,.3;t=.6;r1=16*kappa;r2=4*kappa
    vector=first_jumps()[(0,1)]
    fv,fc=flat_projection(vector)
    ref={}
    for cut in (12,20):
        basis,H=flat_matrix(cut,K,delta);ix={s:i for i,s in enumerate(basis)}
        v=np.zeros(len(basis),complex)
        for s,a in fc.items():v[ix[s]]=a
        u=np.exp(-r2*t/2)*expm_multiply(1j*t*H,v)
        ref[cut]=physical_limit(u,basis)
    keys=set(ref[12])|set(ref[20])
    taildiff=math.sqrt(sum(abs(ref[12].get(s,0)-ref[20].get(s,0))**2 for s in keys))
    assert taildiff<1e-11
    rows=[]
    for S in (4,8,16,32):
        p,n8,H2,H4,B,R=finite_operators(S,False)
        H=K*S*(S+1)*(H2+4*sps.eye(len(p)))+delta*H4
        forward=-1j*H-kappa*R/2;adjoint=1j*H-kappa*R/2
        flat=np.array([fv.get(s,0) for s in p]);initial=np.array([vector.get(s,0) for s in p],complex);other=initial-flat
        actual=expm_multiply(t*adjoint,flat);av=dict(zip(p,actual))
        error=math.sqrt(sum(abs(av.get(s,0)-ref[20].get(s,0))**2 for s in set(av)|set(ref[20])))
        evolved=expm_multiply(t*forward,np.stack([flat,other],axis=1))
        cross=np.vdot(evolved[:,0],evolved[:,1])
        rows.append({'S':S,'adjoint_prepared_vector_error':error,'forward_flat_complement_cross_term':{'real':float(cross.real),'imaginary':float(cross.imag),'absolute_value':float(abs(cross))},'initial_flat_mass':float(np.vdot(flat,flat).real),'initial_complement_mass':float(np.vdot(other,other).real)})
    # Check the consequence reference's finite-field quadrature at two flux cutoffs.
    source=first_jumps();channels=list(source);window_results=[]
    for cut in (12,20):
        basis,H=flat_matrix(cut,K,delta);ix={s:i for i,s in enumerate(basis)}
        v=np.zeros((len(basis),len(channels)),complex)
        for j,ch in enumerate(channels):
            _,coeff=flat_projection(source[ch])
            for s,a in coeff.items():v[ix[s],j]=a
        times=np.linspace(0,t,513)
        out=expm_multiply(-1j*H-r2/2*sps.eye(len(basis)),v,start=0,stop=t,num=len(times))
        vals={1:[],2:[]}
        for vectors in out:
            # Each column is independently embedded; different first marks are mixed.
            probs={1:0.,2:0.}
            for j in range(len(channels)):
                phy=physical_limit(vectors[:,j],basis)
                for (q,f),amp in phy.items():
                    Emax=max(abs(f+g) for g in offsets(q))
                    for win in probs:
                        if Emax<=win:probs[win]+=abs(amp)**2
            for win in vals:vals[win].append(probs[win])
        factor=kappa*np.exp(-r1*(t-times))
        window_results.append({'flat_flux_cutoff':cut,'window_probabilities':{str(win):float(simpson(factor*np.array(vals[win]),x=times)) for win in vals}})
    for win in ('1','2'):assert abs(window_results[0]['window_probabilities'][win]-window_results[1]['window_probabilities'][win])<1e-11
    result={'parameters':{'K':K,'delta':delta,'kappa':kappa,'T':t},'adjoint_cutoff_state_difference':taildiff,'adjoint_and_cross_controls':rows,'consequence_reference_cutoff_controls':window_results,'scope':'Floating controls only; the adjoint theorem follows by the signed-Hamiltonian repetition of the frozen corrector proof.'}
    (HERE/'ADJOINT_REFERENCE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
