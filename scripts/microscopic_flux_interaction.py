#!/usr/bin/env python3
"""Exact finite Pauli centrality and numerical free-band elimination controls."""
AUDIT_TIMEOUT_SEC=120
AUDIT_INPUT_PATHS=['scripts/corner_fermion_qubit_code_genuine_cube_rotation_action_spin_half_class_2026_10_17.py']
import ast,itertools,json,sys
from pathlib import Path
import numpy as np
ROOT=Path(__file__).resolve().parents[1]

def main():
    tree=ast.parse((ROOT/AUDIT_INPUT_PATHS[0]).read_text())
    fn=next(n for n in tree.body if isinstance(n,ast.FunctionDef) and n.name=='_run_reviewed_program')
    body=[]
    for n in fn.body:
        if isinstance(n,ast.ClassDef):break
        if not isinstance(n,ast.Global):body.append(n)
    ns={'np':np,'itertools':itertools,'sys':type('Args',(),{'argv':['probe','4','1011']})()}
    exec(compile(ast.Module(body=body,type_ignores=[]),'<current corner definitions>','exec'),ns)
    vertices=ns['VERTS'];inc=ns['INC'];A=ns['A'];B=ns['Bop'];R=ns['Rop'];pm=ns['pmul']
    seen=set();edges=[]
    for q in vertices:
      for _,_,r in inc[q]:
        key=frozenset((q,r))
        if key not in seen:edges.append((q,r));seen.add(key)
    hops=[A(q,r) for q,r in edges];charges=[B(q) for q in vertices]
    loops=[ns['loop_op'](seq,ns['FLUX'][kind]) for kind,seq in ns['cycles']()]
    reps=list(set(R(v,h) for v in ns['SITES'] for h in ns['HALF']))
    # Independent binary symplectic commutator (phases cannot affect it).
    anti=lambda a,b:((a[0]&b[1]).bit_count()+(a[1]&b[0]).bit_count())%2
    counts={}
    for name,ls,rs in [('loop_hop',loops,hops),('loop_charge',loops,charges),('repetition_hop',reps,hops),('repetition_charge',reps,charges),('loop_repetition',loops,reps)]:
      counts[name]={'pairs':len(ls)*len(rs),'violations':sum(anti(a,b) for a in ls for b in rs)}
    checks={k: v['violations']==0 for k,v in counts.items()}
    checks['charge_hop_noncommuting']=sum(anti(charges[0],a) for a in hops)==6
    # Diagnostic added electric Pauli: not in the tested Hamiltonian.
    witness=next((i,p) for i in range(ns['NQ']) for p in [(1<<i,0,0),(0,1<<i,0)] if any(anti(p,l) for l in loops))
    checks['added_electric_control_changes_flux']=any(anti(witness[1],l) for l in loops)
    # Physical Z probes commute with repetition constraints but can create flux.
    # Equal-time and dynamical two-point functions vanish between different syndromes
    # in any state commuting with every loop (proof in note).
    groups={}
    for i in range(ns['NQ']):
      z=(0,1<<i,0)
      syndrome=tuple(j for j,l in enumerate(loops) if anti(z,l))
      groups.setdefault(syndrome,[]).append(i)
    checks['all_Z_probes_have_nonempty_flux_syndrome']=() not in groups
    diam=0
    for inds in groups.values():
      for i in inds:
       for j in inds:
        a=np.array(ns['SITES'][i//48]);b=np.array(ns['SITES'][j//48]);delta=abs(a-b)
        diam=max(diam,int(np.minimum(delta,4-delta).sum()))
    checks['Z_equal_syndromes_local_to_one_link']=diam<=1
    syndrome_summary={'classes':len(groups),'max_class_size':max(map(len,groups.values())),'max_coarse_L1_diameter':diam}
    # Four-mode exact Fock representation, no mean-field factorization.
    n=4;dim=2**n;c=[]
    for j in range(n):
      x=np.zeros((dim,dim),complex)
      for b in range(dim):
        if (b>>j)&1:x[b^(1<<j),b]=(-1)**((b&((1<<j)-1)).bit_count())
      c.append(x)
    def lift(a):return sum(a[i,j]*c[i].conj().T@c[j] for i in range(n) for j in range(n))
    h=np.array([[.2,.3,.07j,.11],[.3,-.4,.09,.02j],[-.07j,.09,2,.21],[.11,-.02j,.21,3]],complex)
    a=np.diag([1,-1,.5,-.5]);bb=np.ones((n,n))-np.eye(n)
    comm=lambda a,b:a@b-b@a
    closure=float(np.linalg.norm(comm(lift(a),lift(bb))-lift(comm(a,bb))))
    checks['bilinear_commutator_closure']=closure<1e-12
    e=np.linalg.eigvalsh(h);two=[b for b in range(dim) if b.bit_count()==2]
    e2=np.linalg.eigvalsh(lift(h)[np.ix_(two,two)])
    additivity=float(np.max(abs(e2-np.sort([e[i]+e[j] for i in range(n) for j in range(i+1,n)]))))
    checks['two_particle_spectrum_additive']=additivity<1e-12
    z=.17+.31j;A0=z*np.eye(2)-h[:2,:2];D=z*np.eye(2)-h[2:,2:]
    schur=np.linalg.inv(A0-h[:2,2:]@np.linalg.inv(D)@h[2:,:2])
    schur_error=float(np.linalg.norm(schur-np.linalg.inv(z*np.eye(4)-h)[:2,:2]))
    checks['exact_high_band_elimination']=schur_error<1e-12
    # Sector direct sum has zero cross-sector matrix element at any penalty.
    H=lift(h);Hz=np.block([[H,np.zeros_like(H)],[np.zeros_like(H),H+7*np.eye(dim)]])
    P=np.diag([1]*dim+[0]*dim);Q=np.eye(2*dim)-P
    phq=float(np.linalg.norm(P@Hz@Q));checks['sector_PHQ_zero']=phq==0
    # Interaction positive control: explicit new density-density term destroys free pair additivity.
    ni=[x.conj().T@x for x in c];hi=H+.37*ni[0]@ni[1]
    delta=float(np.max(abs(np.linalg.eigvalsh(hi[np.ix_(two,two)])-e2)))
    checks['added_quartic_control_detected']=delta>1e-4
    out={'scope':'Current L4 corner Pauli definitions; general quadratic identities tested on an explicit four-mode fixture, not a fitted corner spectrum. No scalar derived.', 'counts':counts,'Z_syndromes':syndrome_summary,'qubits':ns['NQ'],'vertices':len(vertices),'edges':len(edges),'loops':len(loops),'repetitions':len(reps),'electric_witness_qubit':witness[0],'bilinear_error':closure,'pair_additivity_error':additivity,'Schur_error':schur_error,'PHQ_norm':phq,'added_quartic_shift':delta,'checks':checks}
    p=ROOT/'outputs/microscopic_flux_interaction/result.json';p.parent.mkdir(parents=True,exist_ok=True);p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2));assert all(checks.values())
if __name__=='__main__':main()
