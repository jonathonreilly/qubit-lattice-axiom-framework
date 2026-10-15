"""Synthetic model checks, not observational calibration or independent science."""
AUDIT_TIMEOUT_SEC = 180
from pathlib import Path
import hashlib,json,math
import numpy as np
from scipy.stats import f as f_law
import cassini_error_direction as geo

HERE=Path(__file__).resolve().parent


def run():
    rng=np.random.default_rng(859783);n=40;trials=50000;alpha=.01
    G=(rng.standard_normal((trials,n))+1j*rng.standard_normal((trials,n)))/math.sqrt(2)
    # Coordinates correspond to signal P_f, carrier A, then remaining B.
    U=np.abs(G[:,1])**2;V=np.sum(np.abs(G[:,2:])**2,axis=1)
    pivot=(n-2)*U/V
    threshold=f_law.isf(alpha,2,2*(n-2));reject=pivot>threshold
    expected_se=math.sqrt(alpha*(1-alpha)/trials)
    assert abs(float(reject.mean())-alpha)<6*expected_se
    records=[dict(control='uniform_direction_carrier_tail',trials=trials,nominal=alpha,
                  observed=float(reject.mean()),six_standard_errors=6*expected_se)]
    sphere=G/np.linalg.norm(G,axis=1)[:,None]
    radii=[np.ones(trials),np.exp(rng.normal(0,3,trials)),
           1+100*np.abs(sphere[:,1])]
    # The last law intentionally makes the radius depend on direction.
    for name,R in zip(['constant_radius','lognormal_radial','direction_dependent_radius'],radii):
        e=R[:,None]*sphere
        a2=np.abs(e[:,1])**2;b2=np.sum(np.abs(e[:,2:])**2,axis=1)
        other=(n-2)*a2/b2
        assert np.array_equal(other>threshold,reject)
        assert np.allclose(other,pivot,rtol=1e-12,atol=1e-12)
        records.append(dict(control='radial_law_cancellation',law=name,trials=trials,
                            rejection_rate=float(reject.mean())))
    # Quantizer perturbation can be adversarial; enlarged-cone acceptance must
    # include every originally accepted analog vector, not merely in expectation.
    tau=geo.ratio_tau(1,n-2,alpha);q=.4
    direction=rng.normal(size=(trials,2));direction/=np.linalg.norm(direction,axis=1)[:,None]
    a=np.sqrt(U);b=np.sqrt(V)
    # Test radial perturbations with full nonnegative-norm constraint.
    da=q*direction[:,0];db=q*direction[:,1]
    aa=np.maximum(0,a+da);bb=np.maximum(0,b+db)
    original=a<=tau*b;enlarged=aa<=tau*bb+q*math.hypot(1,tau)
    assert np.all(enlarged[original])
    records.append(dict(control='quantizer_outer_ball_coverage',trials=trials,
                        originally_accepted=int(original.sum()),lost=0))
    # Exact unquantized nested-pivot independence: Dirichlet neutrality.
    amp=(n-1)*np.abs(G[:,0])**2/(U+V)
    amp_reject=amp>f_law.isf(alpha,2,2*(n-1))
    joint=float(np.mean(~reject & ~amp_reject));target=(1-alpha)**2
    assert abs(joint-target)<6*math.sqrt(target*(1-target)/trials)
    records.append(dict(control='nested_joint_coverage',trials=trials,
                        expected=target,observed=joint))
    # Data leakage counterexample: if reference g is selected from validation
    # DFT modes, the maximum contrast replaces the specified one. Conditional
    # direction symmetry after that selection no longer holds.
    modes=np.abs(G[:,1:])**2;largest=np.max(modes,axis=1)
    leaked=(n-2)*largest/(np.sum(modes,axis=1)-largest)
    leak_rate=float(np.mean(leaked>threshold))
    u=threshold/(n-2+threshold);m=n-1
    exact_leak=sum((-1)**(j+1)*math.comb(m,j)*max(0,1-j*u)**(m-1)
                   for j in range(1,min(m,math.floor(1/u))+1))
    assert leak_rate>.2 and abs(leak_rate-exact_leak)<.015
    records.append(dict(control='validation_selected_reference_failure',nominal=alpha,
                        observed=leak_rate,dirichlet_exact_probability=exact_leak,
                        explanation='Not the training-only procedure; deliberately violated conditioning.'))
    # General low/high energy ratio uses complex ranks (twice in real F df).
    r,s=16,23;L=np.sum(np.abs(G[:,1:1+r])**2,axis=1);H=np.sum(np.abs(G[:,1+r:])**2,axis=1)
    rate=float(np.mean(L/H>geo.ratio_tau(r,s,alpha)**2))
    assert abs(rate-alpha)<6*expected_se
    records.append(dict(control='color_complex_rank_F_tail',r=r,s=s,trials=trials,observed=rate))
    # Reweighting directions destroys the law; the test must be sensitive to it.
    colored=(s/r)*(4*L)/H
    bad_rate=float(np.mean(colored>f_law.isf(alpha,2*r,2*s)))
    assert bad_rate>.8
    records.append(dict(control='colored_direction_rejection_witness',observed=bad_rate,
                        explanation='Synthetic contrast-variance mismatch, not a fit of receiver noise.'))
    result=dict(role='synthetic mathematical/model controls; no observational calibration',
                source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                geometry_sha256=hashlib.sha256((HERE/'cassini_error_direction.py').read_bytes()).hexdigest(),
                seed=859783,controls=records)
    return result


if __name__=='__main__':
    r=run();p=HERE.parent/'outputs/cassini_error_direction/SAMPLING_CONTROLS_v1.json'
    p.parent.mkdir(parents=True,exist_ok=True)
    if p.exists():raise FileExistsError('preserve immutable original report')
    p.write_text(json.dumps(r,indent=2)+'\n');print(json.dumps(r,indent=2))
