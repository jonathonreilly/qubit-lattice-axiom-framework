"""New consequence controls; reuse the sealed independent local hop builder.

No actual-first-output author source, helper, or result is read or imported.
"""
import sys
sys.dont_write_bytecode=True
from pathlib import Path
HERE=Path(__file__).resolve().parent
PREPARED=HERE.parent/'finite_spin_flat_independent'
sys.path.insert(0,str(PREPARED))
import json,hashlib,math
from collections import defaultdict
from fractions import Fraction
import numpy as np
import scipy.sparse as sps
from scipy.sparse.linalg import expm_multiply
from scipy.integrate import simpson
from physical_builder import words,grade,offsets,hop_data,birth_data,weight,finite_operators,PWORDS
from flat_probe import flat_coord,flat_mode
from decisive_controls import TABLE,expected_h4,physical_limit

q0=tuple(1 if i%2==0 else 0 for i in range(8))

def hop(v,w,S=None):
    ret=defaultdict(Fraction if S is None else float)
    for (q,f),coef in v.items():
        for qq,d,e,k,g in hop_data(q):
            if grade(qq)==w:ret[qq,f+d]-=coef*(1 if S is None else weight(f,g,k,S))
    return {s:a for s,a in ret.items() if a}

def generic_h2(v,S=None):return {s:-a for s,a in hop(hop(v,1,S),0,S).items()}

def generic_h4(v,S=None):
    m2=generic_h2(generic_h2(v,S),S)
    z=v
    for w in (1,2,1,0):z=hop(z,w,S)
    ret=defaultdict(Fraction if S is None else float,m2)
    for s,a in z.items():ret[s]-=a/2
    return {s:a for s,a in ret.items() if a}

def first_jumps(S=None,coherent=False):
    after=hop({(q0,0):Fraction(1)},1,S)
    ret=defaultdict(lambda:defaultdict(Fraction if S is None else float))
    for (q,f),amp in after.items():
        for qq,d,e,c,g in birth_data(q):
            key=e if coherent else (e,c)
            ret[key][qq,f+d]-=amp*(1 if S is None else weight(f,g,c,S))
    return {k:dict(v) for k,v in ret.items()}

def flat_projection(v):
    # Flat coefficients use the normalized compact-frame convention of PRE.
    coords=defaultdict(complex)
    for (q,z),amp in v.items():
        fc,sign=flat_coord(q,z)
        if fc is not None:coords[fc]+=sign*complex(amp)/np.sqrt(2)
    physical=defaultdict(complex)
    for (a,r,z),amp in coords.items():
        for s,c in flat_mode(a,r,z).items():physical[s]+=amp*complex(c)/np.sqrt(2)
    return dict(physical),dict(coords)

def exact_clock_controls():
    seed={(q0,0):Fraction(1)}
    assert generic_h2(seed)=={(q0,0):Fraction(-8)}
    assert generic_h4(seed)=={(q0,0):Fraction(24)}
    expected=first_jumps()
    assert len(expected)==16 and all(sum(abs(a)**2 for a in v.values())==1 for v in expected.values())
    rows=[]
    for S in (1,2,4,8):
        h2=generic_h2(seed,S);h4=generic_h4(seed,S);js=first_jumps(S)
        assert h2=={(q0,0):-8.} and h4=={(q0,0):24.}
        assert js==expected
        rows.append({'S':S,'H2_zero_field':-8,'H4_zero_field':24,'first_resolved_channels':len(js),'total_loss_without_kappa':sum(sum(abs(a)**2 for a in v.values()) for v in js.values())})
    marks=[]
    for coherent in (False,True):
        for ch,v in first_jumps(coherent=coherent).items():
            norm2=sum(abs(a)**2 for a in v.values());fv,fc=flat_projection(v)
            flatweight=sum(abs(x)**2 for x in fc.values())/norm2
            assert abs(flatweight-.5)<1e-14
            marks.append({'coherent':coherent,'channel':str(ch),'norm_squared':float(norm2),'flat_weight':float(flatweight),'physical_vector':[{'q':list(q),'f':f,'coefficient':str(a)} for (q,f),a in v.items()]})
    return {'finite_spin_rows':rows,'all_first_marks':marks,'exact_path_result':'H2 v0=-8 v0; H4 v0=24 v0; 16 resolved unit-norm outputs (or eight coherent norm-squared-two outputs), independent of S>=1.'}

def loss_controls():
    rows=[]
    for S in (1,2,4,8,16):
        p,n8,H2,H4,B,R=finite_operators(S,False)
        diag=R.diagonal();off=R-sps.diags(diag)
        off.eliminate_zeros()
        assert off.nnz==0
        assert min(diag)>=-1e-14 and max(diag)<=4+1e-14
        opposites=[]
        for j,(q,f) in enumerate(p):
            C=tuple(i//2 for i in range(1,8,2) if q[i])
            if C in ((0,2),(1,3)):opposites.append(abs(diag[j]))
        assert max(opposites,default=0)==0
        rows.append({'S':S,'P_dimension':len(p),'loss_diagonal_min':float(min(diag)),'loss_diagonal_max':float(max(diag)),'off_diagonal_nonzero_entries':off.nnz,'opposite_B_pair_max_loss':float(max(opposites,default=0)),'B_flux_shifts_at_most_one':all(abs(n8[i][1]-p[j][1])<=1 for b in B.values() for i,j in zip(*b.nonzero()))})
        assert rows[-1]['B_flux_shifts_at_most_one']
    return rows

def flat_matrix(cut,K,delta):
    basis=[(a,r,z) for a in range(2) for r in range(6) for z in range(-cut,cut+1)];ix={s:i for i,s in enumerate(basis)}
    rr=[];cc=[];vv=[]
    for j,(a,r,z) in enumerate(basis):
        beta,gamma=TABLE[a][r];rr.append(j);cc.append(j);vv.append(K*(4*z*z+beta*z+gamma))
        for s,c in expected_h4(a,r,z).items():
            if s in ix:rr.append(ix[s]);cc.append(j);vv.append(delta*c)
    return basis,sps.csc_matrix((vv,(rr,cc)),shape=(len(basis),len(basis)))

def window_indices(p,R):return [i for i,(q,f) in enumerate(p) if max(abs(f+g) for g in offsets(q))<=R]

def dynamic_controls():
    K,delta,kappa=.4,.7,.3;T=.6;r1=16*kappa;r2=4*kappa
    source=first_jumps();channels=list(source)
    fb,hf=flat_matrix(12,K,delta);fix={s:i for i,s in enumerate(fb)}
    fv=np.zeros((len(fb),len(channels)),complex)
    for j,ch in enumerate(channels):
        _,fc=flat_projection(source[ch])
        for s,a in fc.items():fv[fix[s],j]=a
    rows=[]
    for S in (4,8,16):
        p,n8,H2,H4,B,R=finite_operators(S,False);ix={s:i for i,s in enumerate(p)}
        v=np.zeros((len(p),len(channels)),complex)
        for j,ch in enumerate(channels):
            for s,a in source[ch].items():v[ix[s],j]=a
        gen=-1j*(K*S*(S+1)*(H2+4*sps.eye(len(p)))+delta*H4)-kappa*R/2
        results=[]
        # Nested Simpson grids inspect quadrature error; neither is used as a proof.
        for n in (257,513):
            times=np.linspace(0,T,n)
            actual=expm_multiply(gen,v,start=0,stop=T,num=n,traceA=gen.diagonal().sum())
            ref=expm_multiply(-1j*hf-r2/2*sps.eye(len(fb)),fv,start=0,stop=T,num=n)
            noevent=np.sum(abs(actual)**2,axis=(1,2))
            # Sum channels each have birth source coefficient kappa.
            factor=kappa*np.exp(-r1*(T-times))
            p6=float(simpson(factor*noevent,x=times))
            wresults=[]
            for win in (1,2):
                inds=window_indices(p,win)
                av=np.sum(abs(actual[:,inds,:])**2,axis=(1,2))
                rf=[]
                # Compact J embeds into physical basis; compute each reference window exactly.
                jrr=[];jcc=[];jvv=[];windex={p[i]:j for j,i in enumerate(inds)}
                for col,(a,r,z) in enumerate(fb):
                    for state,c in flat_mode(a,r,z).items():
                        if state in windex:jrr.append(windex[state]);jcc.append(col);jvv.append(complex(c)/np.sqrt(2))
                J=sps.csc_matrix((jvv,(jrr,jcc)),shape=(len(inds),len(fb)))
                for vv in ref:rf.append(np.sum(abs(J@vv)**2))
                exactlocal=float(simpson(factor*np.array(rf),x=times))
                measured=float(simpson(factor*av,x=times))
                wresults.append({'electric_window':win,'physical_window_dimension':len(inds),'actual_N6_window_probability':measured,'flat_consequence_window_probability':exactlocal,'difference':measured-exactlocal})
            results.append({'time_points':n,'N6_probability':p6,'windows':wresults})
        g=r1/(r1-r2)*(np.exp(-r2*T)-np.exp(-r1*T));a=1-np.exp(-r1*T);h=a-g
        rows.append({'S':S,'T':T,'quadratures':results,'guaranteed_N6_lower_bound':float(g),'asymptotic_N6_upper_bound':float((a+g)/2),'predicted_local_N6_total_mass':float(g/2),'predicted_local_total_mass':float((1+np.exp(-r1*T))/2),'N8_lower_lim_bound':float(h/2),'N8_finite_spin_upper_bound':float(h)})
        print('dynamic S',S,'refined N6',results[-1]['N6_probability'],'windows',results[-1]['windows'],flush=True)
    return {'parameters':{'K':K,'delta':delta,'kappa':kappa},'rows':rows,'status':'Floating quadrature-refined finite-spin corroboration. The compactness/commutation proof, not these grids, establishes the consequence.'}

def main():
    assert hashlib.sha256((PREPARED/'FINAL_SEAL.json').read_bytes()).hexdigest()=='4bbbdcf3fa5a12181ccaf4e9ad09ec5dfb82fe4a078d5256ccad67caedf10cfe'
    result={'first_clock':exact_clock_controls(),'finite_spin_loss_bounds':loss_controls(),'dynamics':dynamic_controls()}
    print('per_element: Exact local hop and creation coefficients are checked; no broader primitive claim is tested.')
    print('per_site: All eight sites and all sixteen resolved first marks enter the clock and loss checks.')
    print('per_mode: The physical flat mass is checked for every first mark; isolated angle fibers are not preparations.')
    print('per_block: Four-, six-, and eight-record sector clocks and bounds are the explicitly tested number blocks.')
    print('lattice_wide: Only the fixed eight-site ring is resolved; no larger-volume no-limit claim is executed.')
    (HERE/'CONSEQUENCE_RESULTS.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
