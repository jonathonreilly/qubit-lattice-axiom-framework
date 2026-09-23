import json,math,cmath,pathlib
# Independent direct quadratic form/Fourier check on 3^3 using real sin/cos coordinates.
L=3; sites=[(x,y,z) for x in range(L) for y in range(L) for z in range(L)];N=len(sites); beta=2
v=[cmath.exp(2j*math.pi*x/L)/math.sqrt(N) for x,y,z in sites]
idx={s:i for i,s in enumerate(sites)}
energy=sum(abs(v[i]-v[idx[tuple((s[a]+(a==d))%L for a in range(3))]])**2 for i,s in enumerate(sites) for d in range(3))
assert abs(energy-3)<1e-12
# Random-frame projection, explicit rational spins with nonzero mean: zero mode exactly cancels algebraically.
s=[(1,0,0),(0,1,0),(0,0,1)]
M=[sum(t[a] for t in s)/3 for a in range(3)]; norm=math.sqrt(sum(t*t for t in M));u=[t/norm for t in M]
p=[[t[a]-sum(t[b]*u[b] for b in range(3))*u[a] for a in range(3)] for t in s]
zero=sum(sum(t[a] for t in p)**2 for a in range(3)); assert zero<1e-28
# N=2 independent uniform spheres at h=0: Var(m1)=1/(3N), so susceptibility N Var(m1)=1/3, finite.
# Ward derivation: D F= sum s3; D log w=-beta*h*F, hence N<m3>=beta*h*N^2<m1^2>.
# Parseval independently direct complex DFT for rational real input on 3^3.
f=[((i*7)%11-5)/7 for i in range(N)]
ff=[sum(f[i]*cmath.exp(-2j*math.pi*sum(k[a]*s[a] for a in range(3))/L) for i,s in enumerate(sites))/math.sqrt(N) for k in sites]
err=abs(sum(abs(t)**2 for t in ff)-sum(t*t for t in f));assert err<1e-12
path=pathlib.Path('/private/tmp/review-drain-20260915/drain8173-original/head/.claude/science/physics-loops/admissibility-induced-law-20260906/specs/supervisor_control_block29_kernel.out.txt')
rows=[[float(x) for x in l.split(':',1)[1].split()] for l in path.read_text().splitlines() if 'n  beta E(k)' in l]
result={'quadratic_form_energy':energy,'expected_eigenvalue':3,'variance_beta2_per_component':1/6,'vector_variance_two_components':1/3,'instantaneous_frame_zero_mode_norm_squared':zero,'parseval_error':err,'reported_combinations':len(rows),'reported_n_ge_2_min':min(min(r[1:]) for r in rows),'reported_n_ge_2_max':max(max(r[1:]) for r in rows),'finite_volume_uniform_susceptibility':1/3,'ward_correct_equation':'N E[m3] = beta h N^2 E[m1^2]','limits':'one deterministic Python standard-library run; 3^3 toy quadratic and DFT checks; no sampler/primary execution, no uncertainty inference'}
print(json.dumps(result,indent=2))
