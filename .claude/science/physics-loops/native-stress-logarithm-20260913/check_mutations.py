"""Preserve effective scientific mutations of the native stress primary."""
from pathlib import Path
import gzip
import hashlib
import json
import os
import subprocess
import tempfile
import time

HERE=Path(__file__).resolve().parent
ROOT=HERE.parents[3]
SOURCE=ROOT/'scripts/native_weyl_stress_logarithm_contact_response_2026_09_13.py'
MUTATIONS=[
 ('pauli_overlap','jj=(1+n.dot(m))*u.dot(vv)','jj=(1-n.dot(m))*u.dot(vv)'),
 ('pauli_imaginary','-(n+m).dot(u.cross(vv))/2)','-(n+m).dot(u.cross(vv))/3)'),
 ('occupation_sign','(-1)**((bits&((1<<site)-1)).bit_count())','1'),
 ('path_phase','path=(1j)**(length-1)*ap','path=(-1j)**(length-1)*ap'),
 ('imaginary_hopping','-path@(np.eye(dim)-signs[0]@signs[length])/2,imag','path@(np.eye(dim)-signs[0]@signs[length])/2,imag'),
 ('path_range','if d==4:continue','if d==3:continue'),
 ('connection_quadratic','for a,b,c,j in product(range(3),repeat=4))/4','for a,b,c,j in product(range(3),repeat=4))/8'),
 ('koszul_sign','structure[a,c,b]-structure[c,b,a]+structure[b,a,c]','structure[a,c,b]+structure[c,b,a]+structure[b,a,c]'),
 ('geometric_scalar','spin,vector-axial*s.eye(2)/8','spin,vector+axial*s.eye(2)/8'),
 ('native_nodes','2+zeta_s-s.cos(kx)','2-zeta_s-s.cos(kx)'),
 ('frame_jet','s.sin(kz)*s.sin(ky)/v_s,b_s/v_s','s.sin(kz)*s.sin(ky)/v_s,b_s*v_s'),
 ('annulus_frequency','w*w*t*t+ss*ss','2*w*w*t*t+ss*ss'),
 ('sphere_moment','s.factorial2(sum(powers)+1)','s.factorial2(sum(powers)+3)'),
 ('stress_trace','tensor=s.trace(R*A4*R*B4)-s.trace(R*A4)*s.trace(R*B4)/3','tensor=s.trace(R*A4*R*B4)-s.trace(R*A4)*s.trace(R*B4)/2'),
 ('node_multiplicity','2*4*s.pi/((2*s.pi)**3*80*vel)','4*s.pi/((2*s.pi)**3*80*vel)'),
 ('dirac_normalization','2/s.pi**4/320*s.pi**2*2','2/s.pi**4/160*s.pi**2*2'),
 ('ellipsoid_fourth_moment','shell4=-(s.trace(A*L)*s.trace(B*L)+2*s.trace(A*L*B*L))/120','shell4=-(s.trace(A*L)*s.trace(B*L)+2*s.trace(A*L*B*L))/60'),
 ('ellipsoid_measure','2*4*s.pi/(4*(2*s.pi)**3*40)','2*4*s.pi/(8*(2*s.pi)**3*40)'),
 ('dispersion_division','(xx+ww)*(aa*xx+bb-aa*ww)','(xx+ww)*(aa*xx+bb+aa*ww)'),
 ('fierz_pauli_divergence','qq*qq*s.trace(A*B)-2*(A*Q).dot(B*Q)','qq*qq*s.trace(A*B)-(A*Q).dot(B*Q)'),
 ('finite_contact_scale','8*cR*s.sin(space*qq/2)**2/space**2','4*cR*s.sin(space*qq/2)**2/space**2'),
 ('one_particle_scale','s.limit(space**3*cR*qq*qq,space,0)','s.limit(cR*qq*qq,space,0)'),
 ('pair_shell','p=sphere@root.T/2;pm=p-Q/2','p=sphere@root.T/3;pm=p-Q/2'),
 ('spectral_density','np.dot(weights,J*em*ep)/(4*np.pi**2)','np.dot(weights,J*em*ep)/(8*np.pi**2)'),
 ('twisted_boundary','np.exp(2j*np.pi*twist[j]) if','np.exp(1j*np.pi*twist[j]) if'),
 ('native_finite_vertex','vertices[:,2,2]=bb/vel','vertices[:,2,2]=bb*vel'),
 ('finite_frequency','momchi[a,b]=-np.mean(gap*jj/(gap*gap+omega*omega))','momchi[a,b]=-np.mean(gap*jj/(gap*gap+4*omega*omega))'),
 ('mixed_lapse_contact','contact_mom.append(-np.mean(np.sum(nm*vec,axis=1))/4)','contact_mom.append(-np.mean(np.sum(nm*vec,axis=1))/8)'),
 ('joint_hamiltonian_contact','+sum(aa[j]*pos[j] for j in range(6))@Phi)/2','+sum(aa[j]*pos[j] for j in range(6))@Phi)/3'),
 ('native_density_contact','onsite=np.diag(np.repeat(coef*diff,2))','onsite=np.diag(np.repeat(coef*diff/2,2))'),
 ('geometric_mixed_contact','C2=-vel*qz/4*np.ones(vol)','C2=vel*qz/4*np.ones(vol)'),
]


def main():
    started=time.monotonic();original=SOURCE.read_text();sha=hashlib.sha256(SOURCE.read_bytes()).hexdigest()
    for name,old,new in MUTATIONS:
        assert original.count(old)==1,(name,'selector_count',original.count(old))
        compile(original.replace(old,new),'<mutation>','exec')
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',VECLIB_MAXIMUM_THREADS='1')
    rows=[];out=HERE/'mutation_evidence';out.mkdir(exist_ok=True)
    for name,old,new in MUTATIONS:
        mutated=original.replace(old,new);msha=hashlib.sha256(mutated.encode()).hexdigest()
        with tempfile.TemporaryDirectory(prefix='toe-stress-mutation-') as tmp:
            root=Path(tmp);(root/'scripts').mkdir();(root/'outputs').mkdir()
            source=root/'scripts'/SOURCE.name;source.write_text(mutated)
            result=subprocess.run(['python3',str(source)],capture_output=True,env=env,timeout=60)
        folder=out/name;folder.mkdir(exist_ok=True)
        for filename,data in [('source.py',mutated.encode()),('stdout',result.stdout),('stderr',result.stderr)]:
            (folder/(filename+'.gz')).write_bytes(gzip.compress(data,mtime=0))
        effective=result.returncode!=0 and b'AssertionError' in result.stderr and b'duplicate check names' not in result.stderr
        row=dict(name=name,original_sha256=sha,mutated_sha256=msha,old=old,new=new,
                 returncode=result.returncode,effective=effective,stderr_tail=result.stderr.decode()[-1800:])
        (folder/'manifest.json').write_text(json.dumps(row,indent=2)+'\n');rows.append(row)
        if not effective:
            (HERE/'MUTATIONS_INCOMPLETE.json').write_text(json.dumps(rows,indent=2)+'\n')
            raise AssertionError((name,'not an effective mathematical failure'))
    receipt=dict(source_sha256=sha,mutation_count=len(rows),all_effective=all(r['effective'] for r in rows),
                 elapsed_seconds=time.monotonic()-started,mutations=rows)
    (HERE/'MUTATIONS.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps({k:receipt[k] for k in ['source_sha256','mutation_count','all_effective','elapsed_seconds']}))


if __name__=='__main__':main()
