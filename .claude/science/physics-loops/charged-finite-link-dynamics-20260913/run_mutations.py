from pathlib import Path
import subprocess,gzip,json,hashlib,time,os
p=Path(__file__).resolve().parent;root=p.parents[3];source=root/'scripts/charged_finite_link_local_dynamics_and_phase_bridge_2026_09_13.py';base=source.read_text();out=p/'mutations';out.mkdir(exist_ok=True)
mutations=[
('electric_commutator_sign',"E@u-u@E,u,K=K)","E@u-u@E,-u,K=K)"),
('upper_endpoint_defect',"u.T@u,I-pp,K=K)","u.T@u,I-pm,K=K)"),
('lower_endpoint_defect',"u@u.T,I-pm,K=K)","u@u.T,I-pp,K=K)"),
('Gauss_charge_sign',"gx=np.tile(e,256)-np.repeat(nx-2,d)","gx=np.tile(e,256)+np.repeat(nx-2,d)"),
('background_charge_count',"nx-2,d)","nx-1,d)"),
('time_reversal_flavor_action',"TR=np.kron(sig[0],I2)","TR=np.kron(sig[2],I2)"),
('nuclear_norm_underestimate',"singular.sum(),2,axis=axis)","singular.sum(),1,axis=axis)"),
('weighted_generator_missing_two',"norm(anti)<=2*J*np.sinh(lam)","norm(anti)<=J*np.sinh(lam)"),
('cutoff_Duhamel_boundary_prefactor',"bound0=2*t0*.7*np.exp", "bound0=t0*.7*np.exp"),
('tail_distance_excess',"one=np.exp(-lam*L+2*J*t*np.sinh(lam))", "one=np.exp(-lam*(L+4)+2*J*t*np.sinh(lam))"),
('Chernoff_square_sign',"np.sqrt(dist*dist-(2*J*t)**2)","np.sqrt(dist*dist+(2*J*t)**2)"),
('magnetic_metric_weight',"w=det/D**2","w=det/D"),
('canonical_electric_jacobian',"w[i]*D[i]**2/det,1","w[i]*D[i]**2,1"),
('plaquette_incidence_count',"(2*w[j]+2*w[k])/2,w[j]+w[k]","(w[j]+w[k])/2,w[j]+w[k]"),
('heat_kernel_derivative_sign',"-(5-3*sy.sqrt(5))/20)==0", "+(5-3*sy.sqrt(5))/20)==0"),
('single_flavor_cubic_phase_sign',"/4,sy.I*A,-(162*A**4", "/4,-sy.I*A,-(162*A**4"),
('single_flavor_fifth_coefficient',"-sy.I*A*(7*A*A+7*B*B-1)/4", "-sy.I*A*(5*A*A+5*B*B-1)/4"),
('quartet_phase_sign',"sy.im(total[5])+7*base*mu*mu*ss*cc", "sy.im(total[5])-7*base*mu*mu*ss*cc"),
('quartet_phase_factor',"sy.im(total[5])+7*base*mu*mu*ss*cc", "sy.im(total[5])+3.5*base*mu*mu*ss*cc"),
('weight_TR_positivity_inference',"np.angle(sign)<-.00048", "abs(np.angle(sign))<1e-12"),
]
manifest=[];start=time.monotonic();env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
for name,old,new in mutations:
 assert base.count(old)==1,(name,base.count(old));s=base.replace(old,new);tmp=out/(name+'.py');tmp.write_text(s)
 result=subprocess.run(['python3',str(tmp)],cwd=root,env=env,capture_output=True,timeout=90)
 for suffix,data in [('source.py.gz',s.encode()),('stdout.gz',result.stdout),('stderr.gz',result.stderr)]: (out/(name+'.'+suffix)).write_bytes(gzip.compress(data,mtime=0))
 tmp.unlink();tail=result.stderr.decode()[-1600:];effective=result.returncode!=0 and b'AssertionError' in result.stderr
 manifest.append(dict(name=name,effective_mathematical_failure=effective,returncode=result.returncode,source_sha256=hashlib.sha256(s.encode()).hexdigest(),failure_tail=tail));print(name,effective,flush=True)
(p/'MUTATIONS.json').write_text(json.dumps(dict(base_sha256=hashlib.sha256(base.encode()).hexdigest(),elapsed_seconds=time.monotonic()-start,mutations=manifest),indent=2)+'\n')
assert all(v['effective_mathematical_failure'] for v in manifest)
