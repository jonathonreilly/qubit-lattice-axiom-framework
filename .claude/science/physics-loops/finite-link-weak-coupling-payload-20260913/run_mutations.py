from pathlib import Path
import subprocess,gzip,json,hashlib,time,os
p=Path(__file__).resolve().parent;root=p.parents[3];source=root/'scripts/finite_integer_link_weak_coupling_payload_and_monopole_density_2026_09_13.py';base=source.read_text();out=p/'mutations';out.mkdir(exist_ok=True)
mutations=[
('plaquette_link_incidence',"np.sum(abs(B),axis=1),4,L=L)","np.sum(abs(B),axis=1),2,L=L)"),
('cube_face_incidence',"np.sum(abs(C),axis=1),6,L=L)","np.sum(abs(C),axis=1),4,L=L)"),
('monopole_angle_normalization',"charge=C@principal/(2*np.pi)","charge=C@principal/np.pi"),
('cube_coercivity_factor',"MONOPOLE_CUBE_FACTOR=4/3","MONOPOLE_CUBE_FACTOR=2"),
('chain_endpoint_count',"expected=np.cos(np.pi/(2*S+2))","expected=np.cos(np.pi/(2*S+1))"),
('chain_ceiling_removed',"expected=np.cos(np.pi/(2*S+2))","expected=1."),
('spectral_deficit_overestimate',"1-expected>=1/(2*(S+1)**2)","1-expected>=2/((S+1)**2)"),
('trial_expectation_too_large',"value>=np.cos(kappa)-1e-12","value>=np.cos(kappa/2)-1e-12"),
('redundant_flow_normalization',"norm,2561/32)","norm,64)"),
('exact_radical_overlap',"1345*sy.sqrt(2)/2561","1344*sy.sqrt(2)/2561"),
('onsite_filling',"np.count_nonzero(np.linalg.eigvalsh(on)<0)==2","np.count_nonzero(np.linalg.eigvalsh(on)<0)==1"),
('CAR_hermitian_bond_factor',"toarray())[-1],q,axis=axis)","toarray())[-1],q/2,axis=axis)"),
('controlled_shift_sign',"sp.kron(F,u,format='csr'))<1e-12","sp.kron(F,u.T,format='csr'))<1e-12"),
('monopole_POVM_normalization',"return .25","return .5"),
('signed_monopole_compression_sign',"return -1j*(-1.)**m/(2*np.pi*m)","return 1j*(-1.)**m/(2*np.pi*m)"),
('squaring_compression_assumed_exact',"np.trace(gap).real>1e-4","abs(np.trace(gap).real)<1e-12"),
('phase_POVM_measure_normalization',"frame@frame.conj().T/d,np.eye(d)","frame@frame.conj().T,np.eye(d)"),
('small_density_excludes_order',"density*(1-density))","0.)"),
]
manifest=[];start=time.monotonic();env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for name,old,new in mutations:
 assert base.count(old)==1,(name,base.count(old));s=base.replace(old,new);tmp=out/(name+'.py');tmp.write_text(s)
 result=subprocess.run(['python3',str(tmp)],cwd=root,env=env,capture_output=True,timeout=90)
 for suffix,data in [('source.py.gz',s.encode()),('stdout.gz',result.stdout),('stderr.gz',result.stderr)]: (out/(name+'.'+suffix)).write_bytes(gzip.compress(data,mtime=0))
 tmp.unlink();tail=result.stderr.decode()[-1500:];effective=result.returncode!=0 and b'AssertionError' in result.stderr
 manifest.append(dict(name=name,effective_mathematical_failure=effective,returncode=result.returncode,source_sha256=hashlib.sha256(s.encode()).hexdigest(),failure_tail=tail));print(name,effective,flush=True)
(p/'MUTATIONS.json').write_text(json.dumps(dict(base_sha256=hashlib.sha256(base.encode()).hexdigest(),elapsed_seconds=time.monotonic()-start,mutations=manifest),indent=2)+'\n')
assert all(v['effective_mathematical_failure'] for v in manifest)
