"""Finite graded-matrix control of number-offset identifiability.

This is a separate illustrative five-state model satisfying the proved
number identities, not a truncation or simulation of the original rotor.
The theorem for the original instrument is analytic from its exact identities.
"""
from pathlib import Path
import hashlib,json,time
import numpy as np
from scipy.linalg import expm

def run():
    number=np.array([0,0,2,2,4]); N=np.diag(number); eye=np.eye(5)
    h=np.array([[.4,.3+.2j,0,0,0],[.3-.2j,1.1,0,0,0],
                [0,0,-.6,.1-.4j,0],[0,0,.1+.4j,.9,0],[0,0,0,0,.2]],complex)
    l0=np.zeros((5,5),complex);l1=l0.copy()
    l0[2,0]=.8;l0[2,1]=.2j;l0[3,0]=-.1;l0[3,1]=.7;l0[4,2]=.5;l0[4,3]=.3j
    l1[2,0]=-.3j;l1[2,1]=.4;l1[3,0]=.6;l1[3,1]=-.2j;l1[4,2]=.2j;l1[4,3]=.9
    jumps=[l0,l1]; losses=[l.conj().T@l for l in jumps];Gamma=sum(losses)
    assert np.array_equal(N@h,h@N)
    for l in jumps: assert np.max(abs(N@l-l@N-2*l))==0
    vectors=[np.array([1,1j,0,0,0]),np.array([1,-1j,0,0,0]),np.array([1,.4j,-.5,.3+.2j,.2j])]
    vectors=[v/np.linalg.norm(v) for v in vectors];states=[np.outer(v,v.conj()) for v in vectors]
    offsets=[(0.,0.,0.),(3.,-7.,5.),(.1,1.3,-2.2),(100.,-40.,75.)]
    tilts=[(1.,1.),(np.exp(.7j),np.exp(-.3j)),(0.,0.)]
    def generator(H,weights):
        out=-1j*(np.kron(eye,H)-np.kron(H.T,eye))
        for l,q,z in zip(jumps,losses,weights):
            out+=z*np.kron(l.conj(),l)-.5*(np.kron(eye,q)+np.kron(q.T,eye))
        return out
    def characteristic(H,t,z,rho):
        evolved=expm(generator(H,z)*t)@rho.reshape(-1,order='F')
        return np.trace(evolved.reshape((5,5),order='F'))
    counting=[];energy=[];histories=[];differences=[];max_error=0.
    def power(H,rho,j):
        l=jumps[j];q=losses[j]
        return float(np.trace(rho@(l.conj().T@H@l-(q@H+H@q)/2)).real)
    def noevent(H,t):return expm((-1j*H-Gamma/2)*t)
    def history(H,marks,times,T):
        out=eye.astype(complex);previous=0.
        for mark,t in zip(marks,times):out=jumps[mark]@noevent(H,t-previous)@out;previous=t
        return noevent(H,T-previous)@out
    def pairs(z):return [float(z.real),float(z.imag)]
    for offset in offsets:
        values=np.array([offset[n//2] for n in number]);H=h+np.diag(values)
        for t in (.02,.3,1.7):
            for iz,z in enumerate(tilts):
                for ir,rho in enumerate(states):
                    x=characteristic(h,t,z,rho);y=characteristic(H,t,z,rho);error=abs(x-y)
                    assert error<2e-12;max_error=max(max_error,error)
                    counting.append({'offset':offset,'time':t,'tilt':iz,'input':ir,
                                     'reference':pairs(x),'altered':pairs(y),'difference_abs':error})
        for ir,rho in enumerate(states):
            for j,q in enumerate(losses):
                gaps=np.array([offset[(n+2)//2]-offset[n//2] if n+2<=4 else 0 for n in number])
                predicted=float(np.trace(rho@q@np.diag(gaps)).real)
                actual=power(H,rho,j)-power(h,rho,j);error=abs(actual-predicted)
                assert error<1e-12;max_error=max(max_error,error)
                energy.append({'offset':offset,'input':ir,'channel':j,'rate':float(np.trace(rho@q).real),
                               'original_power':power(h,rho,j),'altered_power':power(H,rho,j),
                               'predicted_shift':predicted,'difference_abs':error})
        original=float(np.trace(h@(states[1]-states[0])).real)
        altered=float(np.trace(H@(states[1]-states[0])).real)
        assert abs(original-altered)<1e-13
        differences.append({'offset':offset,'same_N_input_difference':original,'altered_difference':altered})
        for marks,times in [((),()),((0,),(.2,)),((1,0),(.17,.71))]:
            T=1.3;A=history(h,marks,times,T);B=history(H,marks,times,T)
            scalar_errors=[]
            for n in (0,2,4):
                P=np.diag(number==n); cuts=(0.,*times,T);k=len(marks)
                if n+2*k>4:assert np.linalg.norm(A@P)<1e-13;continue
                phase=sum(offset[(n+2*r)//2]*(cuts[r+1]-cuts[r]) for r in range(k+1))
                scalar_errors.append(float(np.linalg.norm(B@P-np.exp(-1j*phase)*A@P)))
            for ir,rho in enumerate(states):
                x=A@rho@A.conj().T;y=B@rho@B.conj().T
                error=abs(np.trace(x-y));diag_error=sum(np.linalg.norm(np.diag(number==n)@(x-y)@np.diag(number==n)) for n in (0,2,4))
                assert error<1e-12 and diag_error<1e-12
                if ir<2:assert np.linalg.norm(x-y)<1e-12
                max_error=max(max_error,error,*scalar_errors)
                histories.append({'offset':offset,'marks':marks,'input':ir,'probability':float(np.trace(x).real),
                                  'probability_difference_abs':float(error),'sector_phase_residual':max(scalar_errors),
                                  'diagonal_block_difference':float(diag_error),'full_conditional_unnormalized_state_difference':float(np.linalg.norm(x-y))})
    assert max(r['full_conditional_unnormalized_state_difference'] for r in histories if r['input']==2)>.1
    return {'scope':__doc__,'count_rows':counting,'power_rows':energy,'same_sector_rows':differences,
            'history_rows':histories,'max_checked_identity_error':float(max_error),
            'original_rotor_scientific_simulation':False,'independent_researcher_check':False,
            'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest()}

if __name__=='__main__':
    tic=time.perf_counter();out=run();out['elapsed_seconds']=time.perf_counter()-tic
    print(json.dumps(out,indent=2,allow_nan=False))
