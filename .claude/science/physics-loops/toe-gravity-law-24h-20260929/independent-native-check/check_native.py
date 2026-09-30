#!/usr/bin/env python3
"""Independent literal-qubit and sparse-pair controls; no author imports.

Pair amplitudes on a 6^3 torus use Q[zeta]/(zeta^2-zeta+1), not floating point.
Full local/global product-state actions use hard-core bit operations.
"""
import os
from pathlib import Path
from fractions import Fraction as Q
from collections import defaultdict
from itertools import permutations,product
from dataclasses import dataclass
import json,time
for name in ('OPENBLAS_NUM_THREADS','MKL_NUM_THREADS','OMP_NUM_THREADS'):
    os.environ[name]='1'
HERE=Path(__file__).resolve().parent
RUNTIME=Path('/Users/jonBridger/.codex/campaigns/toe-gravity-law-24h-20260929')
def budget():
    assert time.time()<json.loads((RUNTIME/'DEADLINE.json').read_text())['deadline_epoch']
    assert not (RUNTIME/'STOP_REQUESTED.json').exists()

@dataclass(frozen=True)
class E:
    a:Q=Q(0)
    b:Q=Q(0)
    def __add__(self,other):
        if not isinstance(other,E):other=E(Q(other))
        return E(self.a+other.a,self.b+other.b)
    __radd__=__add__
    def __neg__(self):return E(-self.a,-self.b)
    def __sub__(self,other):return self+-other
    def __mul__(self,other):
        if not isinstance(other,E):other=E(Q(other))
        return E(self.a*other.a-self.b*other.b,
                 self.a*other.b+self.b*other.a+self.b*other.b)
    __rmul__=__mul__
    def conj(self):return E(self.a+self.b,-self.b)
    def __bool__(self):return bool(self.a or self.b)
    def serial(self):return [str(self.a),str(self.b)]
Z=E(0,1);ONE=E(1);ZERO=E()
ROOTS=[ONE]
for _ in range(5):ROOTS.append(ROOTS[-1]*Z)
assert ROOTS[-1]*Z==ONE

NAMES=['E1','E2','T12','T13','T23'];NORMS=[2,6,4,4,4]
def pair(a,b):assert a!=b;return (1<<a)|(1<<b)
# Unnormalized pair annihilators: physical shell order (+x,-x,+y,-y,+z,-z).
channels=[{pair(0,1):1,pair(2,3):-1},
          {pair(0,1):1,pair(2,3):1,pair(4,5):-2}]
for i,j in [(0,1),(0,2),(1,2)]:
    channels.append({pair(2*i+a,2*j+b):(-1)**(a+b) for a,b in product((0,1),repeat=2)})
def inner_real(p,q):return sum(v*q.get(k,0) for k,v in p.items())
assert [[inner_real(p,q) for q in channels] for p in channels]==[[NORMS[i] if i==j else 0 for j in range(5)] for i in range(5)]

def lower(state,op):
    out=defaultdict(Q)
    for bits,amp in state.items():
        for word,c in op.items():
            if bits&word==word:out[bits^word]+=amp*c
    return {k:v for k,v in out.items() if v}
def raise_pair(state,op):
    out=defaultdict(Q)
    for bits,amp in state.items():
        for word,c in op.items():
            if bits&word==0:out[bits|word]+=amp*c
    return {k:v for k,v in out.items() if v}
def projector_action(state,op,norm):
    return {k:v/Q(norm) for k,v in raise_pair(lower(state,op),op).items()}
def addstates(*states):
    out=defaultdict(Q)
    for state in states:
        for k,v in state.items():out[k]+=v
    return {k:v for k,v in out.items() if v}
def sector_action(state,selected):
    return addstates(*(projector_action(state,channels[i],NORMS[i]) for i in selected))

def local_checks():
    for selected in [(0,1),(2,3,4)]:
        matrix={}
        for col in range(64):
            for row,c in sector_action({col:Q(1)},selected).items():
                matrix[row,col]=c
                assert row.bit_count()==col.bit_count()
        assert all(c==matrix.get((j,i),0) for (i,j),c in matrix.items())
    filled={63:Q(1)}
    assert sector_action(filled,(0,1))=={63:Q(2)}
    assert sector_action(filled,(2,3,4))=={63:Q(3)}
    plus={pair(0,1):Q(1),pair(2,3):Q(1)}
    minus={pair(0,1):Q(1),pair(2,3):Q(-1)}
    expectations=[]
    for psi in (plus,minus):
        expectations.append(inner_real(psi,sector_action(psi,(0,1)))/2)
    assert expectations==[Q(1,3),Q(1)]
    assert {k:v*v/2 for k,v in plus.items()}=={k:v*v/2 for k,v in minus.items()}
    # All proper signed axis permutations, acting on the actual shell qubits.
    rotations=0
    for perm in permutations(range(3)):
        parity=(-1)**sum(perm[i]>perm[j] for i in range(3) for j in range(i+1,3))
        for signs in product((-1,1),repeat=3):
            if parity*signs[0]*signs[1]*signs[2]!=1:continue
            mapping={2*i+a:2*perm[i]+(a if signs[i]==1 else 1-a)
                     for i in range(3) for a in (0,1)}
            def turn(word):return sum(1<<mapping[i] for i in range(6) if word>>i&1)
            transformed=[{turn(word):c for word,c in op.items()} for op in channels]
            for j,t in enumerate(transformed):
                coeff=[Q(inner_real(op,t),NORMS[i]) for i,op in enumerate(channels)]
                reconstructed=defaultdict(Q)
                for a,op in zip(coeff,channels):
                    for word,c in op.items():reconstructed[word]+=a*c
                assert {k:v for k,v in reconstructed.items() if v}==t
                assert all(coeff[i]==0 for i in range(5) if (i<2)!=(j<2))
            rotations+=1
    assert rotations==24
    print('Literal64-state qubit operators: Hermitian number conservation, full-shell eigenvalues2,3, readout1/3,1;24 rotations.',flush=True)
    return {'local_dimension':64,'proper_rotations':rotations,'full_shell_E':2,'full_shell_T':3,
            'readout_expectations':[str(v) for v in expectations]}

def laurent_checks():
    # Complete infinite-lattice overlap coefficients from the literal shell words.
    shell=[tuple((1 if a==0 else -1) if k==i else 0 for k in range(3))
           for i in range(3) for a in (0,1)]
    def words(op,shift):
        return {tuple(sorted(tuple(shell[i][k]+shift[k] for k in range(3))
                             for i in range(6) if word>>i&1)):c
                for word,c in op.items()}
    base=[words(op,(0,0,0)) for op in channels]
    axes=[None,None,(0,1),(0,2),(1,2)]
    nonzero=[]
    for shift in product(range(-2,3),repeat=3):
        shifted=[words(op,shift) for op in channels]
        for i,j in product(range(5),repeat=2):
            actual=inner_real(base[i],shifted[j]); expected=0
            if i==j:
                if shift==(0,0,0):expected=NORMS[i]
                elif i>=2:
                    a,b=axes[i]
                    if abs(shift[a])==abs(shift[b])==1 and all(shift[k]==0 for k in range(3) if k not in (a,b)):
                        expected=1
            assert actual==expected,(shift,i,j,actual,expected)
            if actual:nonzero.append([list(shift),NAMES[i],NAMES[j],actual])
    print('Complete infinite-lattice raw Gram:',125*25,'integer comparisons;',len(nonzero),'nonzero coefficients.',flush=True)
    return {'comparison_count':125*25,'nonzero_raw_coefficients':nonzero}

def torus(L=6):
    sites=list(product(range(L),repeat=3));index={x:i for i,x in enumerate(sites)}
    def step(x,axis,sgn):
        y=list(x);y[axis]=(y[axis]+sgn)%L;return tuple(y)
    frames=[]
    for x in sites:
        mapping={2*i+a:index[step(x,i,1 if a==0 else -1)] for i in range(3) for a in (0,1)}
        local=[]
        for op in channels:
            translated={sum(1<<mapping[i] for i in range(6) if word>>i&1):c for word,c in op.items()}
            assert len(translated)==len(op)
            local.append(translated)
        frames.append(local)
    return sites,index,frames,step
def cinner(p,q):return sum((v.conj()*q.get(k,ZERO) for k,v in p.items()),ZERO)
def clean(p):return {k:v for k,v in p.items() if v}
def frame_action(state,frames,selection):
    out=defaultdict(E)
    for local in frames:
        for j in selection:
            op=local[j];amp=sum((c*state.get(word,ZERO) for word,c in op.items()),ZERO)*Q(1,NORMS[j])
            if not amp:continue
            for word,c in op.items():out[word]+=c*amp
    return clean(out)

def global_checks():
    L=6;sites,index,frames,step=torus(L);volume=len(sites)
    qs=[(0,0,0),(1,0,0),(2,1,0),(3,0,0),(0,3,0),(1,2,3),(3,3,3),(2,2,2)]
    results=[];nulls=0
    for momentum in qs:
        budget();states=[]
        for j in range(5):
            st=defaultdict(E)
            for x,local in zip(sites,frames):
                phase=ROOTS[sum(a*b for a,b in zip(momentum,x))%6]
                for word,c in local[j].items():st[word]+=c*phase
            states.append(clean(st))
        cos=[]
        for m in momentum:
            value=(ROOTS[m]+ROOTS[m].conj())*Q(1,2)
            assert value.b==0;cos.append(value.a)
        grams=[Q(1),Q(1),1+cos[0]*cos[1],1+cos[0]*cos[2],1+cos[1]*cos[2]]
        for i,st in enumerate(states):
            expected_norm=E(volume*NORMS[i]*grams[i])
            assert cinner(st,st)==expected_norm
            if grams[i]==0:assert not st;nulls+=1
            for j in range(i):assert cinner(st,states[j])==ZERO
            eact=frame_action(st,frames,(0,1));tact=frame_action(st,frames,(2,3,4))
            assert eact==(st if i<2 else {})
            assert tact==({k:v*grams[i] for k,v in st.items()} if i>=2 else {})
            # Independently check every occupied pair word avoids NN repulsion.
            for word in st:
                occupied=[a for a in range(volume) if word>>a&1]
                assert len(occupied)==2
                x,y=[sites[a] for a in occupied]
                distance=sum(min((a-b)%L,(b-a)%L) for a,b in zip(x,y))
                assert distance!=1
        results.append({'momentum_units_pi_over_3':momentum,'Gram':[str(x) for x in grams]})
    # Full unrestricted carrier action on checkerboard and fully occupied states.
    cb=sum(1<<i for i,x in enumerate(sites) if sum(x)%2==0)
    full=(1<<volume)-1
    energies={}
    for label,bits in [('checkerboard',cb),('full',full)]:
        ecoeff=Q(0);tcoeff=Q(0)
        for local in frames:
            for j,op in enumerate(local):
                acted=projector_action({bits:Q(1)},op,NORMS[j])
                assert not acted or set(acted)=={bits}
                if j<2:ecoeff+=acted.get(bits,Q(0))
                else:tcoeff+=acted.get(bits,Q(0))
        nn=sum(bool(bits>>index[x]&1 and bits>>index[step(x,i,1)]&1)
               for x in sites for i in range(3))
        energies[label]={'number':bits.bit_count(),'E_projector_sum':str(ecoeff),
                         'T_projector_sum':str(tcoeff),'NN_pairs':nn,
                         'critical_energy_mu1':str(bits.bit_count()-2*ecoeff-tcoeff),
                         'common_eigenvector':True}
    assert energies['checkerboard']=={'number':volume//2,'E_projector_sum':str(Q(volume)),
         'T_projector_sum':str(Q(3*volume,2)),'NN_pairs':0,'critical_energy_mu1':str(Q(-3*volume)),
         'common_eigenvector':True}
    print('6^3 physical-site torus:',len(qs)*5,'exact band/channel controls;',nulls,'null channels.',flush=True)
    print('Full-carrier product-state actions:',json.dumps(energies),flush=True)
    return {'L':L,'physical_qubits':volume,'tested_channel_momenta':len(qs)*5,'null_channels':nulls,
            'momenta':results,'product_states':energies}

def main():
    budget();start=time.time();local=local_checks();laurent=laurent_checks();glob=global_checks()
    out={'local':local,'laurent':laurent,'global':glob,'elapsed_seconds':time.time()-start}
    (HERE/'results.json').write_text(json.dumps(out,indent=2)+'\n')
    print('Elapsed seconds:',out['elapsed_seconds'],flush=True)
if __name__=='__main__':main()
