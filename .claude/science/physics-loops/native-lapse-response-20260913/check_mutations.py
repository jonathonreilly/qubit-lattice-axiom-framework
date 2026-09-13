"""Scratch-copy challenge of each load-bearing finite check family."""
from pathlib import Path
import gzip,hashlib,json,subprocess,tempfile,time
ROOT=Path(__file__).resolve().parents[4]
PACK=Path(__file__).resolve().parent
SOURCE=ROOT/'scripts/native_lapse_source_contact_response_2026_09_13.py'
mutations=[
 ('Wilson_hopping_sign','(-PAULI[2]+1j*PAULI[0])/2','(-PAULI[2]-1j*PAULI[0])/2'),
 ('energy_vertex_factor','vertex=(a*zz+b*mm)/2','vertex=(a*zz+b*mm)/3'),
 ('contact_second_derivative','s.diff(root,eps,2).subs(eps,0)','2*s.diff(root,eps,2).subs(eps,0)'),
 ('cone_coefficient','mu**2*(1-mu**2)/(16*radius**3)','mu**2*(1-mu**2)/(8*radius**3)'),
 ('prolate_jacobian','jac=qqabs**3*(uu*uu-vv*vv)/8','jac=qqabs**3*(uu*uu-vv*vv)/4'),
 ('arithmetic_Kato_factor','chiA=-2*np.einsum','chiA=-np.einsum'),
 ('congruence_spectral_sign','positive_weights=-2*eu[:,None]','positive_weights=2*eu[:,None]'),
 ('bond_contact_factor','contact[i,j]+=-mean*factor/4','contact[i,j]+=-mean*factor/2'),
 ('all_momentum_arithmetic_factor','ca=-np.mean((enn-en)**2*(1-dot)/(4*(en+enn)))','ca=-np.mean((enn-en)**2*(1-dot)/(8*(en+enn)))'),
 ('finite_global_bound','.75*i1*ell+2e-12','.000001*i1*ell+2e-12'),
 ('actual_geometric_Hamiltonian','math.sqrt(N[ix]*N[iy])','(N[ix]+N[iy])/2'),
 ('inhomogeneous_source_lapse','reshape(vol,2).sum(axis=1)/N1','reshape(vol,2).sum(axis=1)'),
 ('native_imaginary_hop','-A01*(ident-B0*B1)/2','A01*(ident-B0*B1)/2'),
 ('current_nonzero_guard','hx[0]*hx[1]-hx[1]*hx[0]!=s.zeros(64)','s.zeros(64)!=s.zeros(64)'),
 ('Fock_CAR_sign','a[word^(1<<j),word]=(-1)**((word&((1<<j)-1)).bit_count())','a[word^(1<<j),word]=1'),
 ('candidate_protection','generators=[edgeword(*e) for e in protected]','generators=[edgeword(*e) for e in edges]'),
 ('exact_ground_lower_bound',"'-8.34999098'","'-8.34'"),
 ('direct_CAR_sign','sign = (-1)**((word & ((1 << j)-1)).bit_count())','sign = 1'),
 ('sqrt_bracket','root_floor+1, scale','root_floor-1, scale'),
 ('midpoint_trial_data',"'sign': 1,","'sign': -1,"),
]

def main():
    start=time.monotonic()
    text=SOURCE.read_text()
    rows=[]
    recovery=PACK/'mutations'
    recovery.mkdir(exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='lapse_mutation_',dir=ROOT) as folder:
        scratch=Path(folder)/'runner.py'
        for name,old,new in mutations:
            assert text.count(old)==1,(name,text.count(old))
            mutated=text.replace(old,new)
            scratch.write_text(mutated)
            result=subprocess.run(['python3',str(scratch)],cwd=ROOT,capture_output=True,timeout=60)
            row=dict(name=name,exit_code=result.returncode,
                     primary_sha256=hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
                     mutant_sha256=hashlib.sha256(mutated.encode()).hexdigest(),
                     stderr_tail=result.stderr.decode(errors='replace').splitlines()[-5:])
            for suffix,blob in [('source.py',mutated.encode()),('stdout',result.stdout),('stderr',result.stderr)]:
                (recovery/(name+'.'+suffix+'.gz')).write_bytes(gzip.compress(blob,mtime=0))
            rows.append(row)
            (PACK/'MUTATIONS.json').write_text(json.dumps(dict(rows=rows,seconds=time.monotonic()-start),indent=2)+'\n')
            print(name,result.returncode,flush=True)
            assert result.returncode!=0,(name,'mutation was not detected')
            assert b'AssertionError' in result.stderr,(name,'failure was not a scientific assertion')
    print('All declared mutations detected:',len(rows))

if __name__=='__main__': main()
