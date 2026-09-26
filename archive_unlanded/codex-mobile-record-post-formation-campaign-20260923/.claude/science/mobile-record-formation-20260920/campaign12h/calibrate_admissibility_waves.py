#!/usr/bin/env python3
"""Calibrate the new birth/profile sampler against complete four-cycle laws."""
from pathlib import Path
from itertools import product
import hashlib,json
import numpy as np
from scipy.sparse import coo_matrix
from scipy.sparse.linalg import expm_multiply
import admissibility_wave_sim as sim

HERE=Path(__file__).resolve().parent
OUT=HERE/'admissibility_wave_calibration'


def generator(j,epsilon):
    words=np.asarray(list(product(range(7),repeat=4)),dtype=np.int8)
    powers=np.array([7**3,7**2,7,1]);lookup={tuple(word):i for i,word in enumerate(words)}
    f=np.array([0,1,-1,0,0,0,0]);feature=np.array([0,-1,-1,2,2,2,2])
    velocities=np.array([[0,0,0],[1,0,0],[-1,0,0],[0,1,0],[0,-1,0],[0,0,1],[0,0,-1]])
    rows=[];cols=[];data=[]
    for number,word in enumerate(words):
        outgoing=0.
        for x in range(4):
            y=(x+1)%4;l=word[(x-1)%4];a=word[x];b=word[y];r=word[(x+2)%4]
            drive=.5*((f[a]-f[b])*(feature[l]+feature[r])+(feature[a]-feature[b])*(f[l]+f[r]))
            if a!=b:
                rate=.05+max(drive,0);dest=number+(b-a)*powers[x]+(a-b)*powers[y]
                rows.append(number);cols.append(dest);data.append(rate);outgoing+=rate
            if a==0:
                for born in range(1,7):
                    rate=epsilon
                    for neighbor in ((x-1)%4,(x+1)%4):
                        rate*=1+j*np.dot(velocities[born],velocities[word[neighbor]])
                    dest=number+born*powers[x]
                    rows.append(number);cols.append(dest);data.append(rate);outgoing+=rate
        rows.append(number);cols.append(number);data.append(-outgoing)
    Q=coo_matrix((data,(rows,cols)),shape=(len(words),len(words))).tocsr()
    assert np.max(np.abs(Q@np.ones(len(words))))<1e-12
    return words,Q


def main():
    OUT.mkdir(exist_ok=True)
    times=np.linspace(0,4,21);modes=np.array([[0],[1],[2]])
    probabilities=np.array([.5]+[1/12]*6)
    # All cases and sample counts are fixed before any comparisons.
    cases=[dict(name='uniform_birth_homogeneous',j=0.,amplitude=0.,seed=2026092210),
           dict(name='positive_neighbor_profile',j=.5,amplitude=.12,seed=2026092211),
           dict(name='strong_neighbor_profile',j=.9,amplitude=.12,seed=2026092212),
           dict(name='negative_neighbor_profile',j=-.5,amplitude=.12,seed=2026092213)]
    plan=dict(cases=cases,trajectories=8192,epsilon=.08,times=times.tolist(),
              gate='Each nondegenerate standardized mean error below5.5; calibration sanity gate, not a confidence certificate.',
              simulator_sha256=hashlib.sha256(Path(sim.__file__).read_bytes()).hexdigest())
    (OUT/'PLAN.json').write_text(json.dumps(plan,indent=2)+'\n')
    results=[]
    for case in cases:
        words,Q=generator(case['j'],.08)
        x=np.arange(4);density=.5+case['amplitude']*np.cos(2*np.pi*x/4)
        px=np.column_stack((1-density,np.repeat((density/6)[:,None],6,axis=1)))
        initial=np.prod(px[np.arange(4)[None,:],words],axis=1)
        assert abs(initial.sum()-1)<1e-13
        phase=np.exp(-2j*np.pi*x[:,None]*modes[:,0]/4)/2
        values=np.einsum('xm,sxo->smo',phase,sim.FIELDS[words])
        flat=values.reshape(len(words),-1)
        probability=expm_multiply(Q.T,initial,start=times[0],stop=times[-1],num=len(times),endpoint=True)
        exact_mean=probability@flat
        exact_power=probability@(np.abs(flat)**2)
        # Density/vector two-time correlations for the nonzero fundamental.
        initial_weight=initial[:,None]*np.conj(values[:,1,:2])
        weighted=expm_multiply(Q.T,initial_weight,start=times[0],stop=times[-1],num=len(times),endpoint=True)
        exact_cross=np.einsum('tsa,sb->tab',weighted,values[:,1,:2])
        raw,stats,seeds,metadata=sim.run([4],modes,probabilities,times,8192,case['seed'],
            epsilon=.08,threads=2,birth_j=case['j'],density_amplitude=case['amplitude'],density_mode=[1])
        rawflat=raw.reshape(len(raw),len(times),-1)
        cross=np.einsum('na,ntb->ntab',np.conj(raw[:,0,1,:2]),raw[:,:,1,:2]).reshape(len(raw),len(times),4)
        sample=np.concatenate((rawflat.real,rawflat.imag,np.abs(rawflat)**2,cross.real,cross.imag),axis=2)
        exact=np.concatenate((exact_mean.real,exact_mean.imag,exact_power,exact_cross.reshape(len(times),4).real,exact_cross.reshape(len(times),4).imag),axis=1)
        observed=sample.mean(axis=0);se=sample.std(axis=0,ddof=1)/np.sqrt(len(sample))
        discrepancy=np.abs(observed-exact);mask=se>1e-13
        maximum=float(np.max(discrepancy[mask]/se[mask]))
        assert np.max(discrepancy[~mask],initial=0)<1e-11
        name=case['name'];path=OUT/(name+'.npz')
        np.savez_compressed(path,fields=raw,statistics=stats,seeds=seeds,times=times,
                            exact=exact,observed=observed,standard_error=se)
        metadata_path=OUT/(name+'.json');metadata_path.write_text(json.dumps(metadata,indent=2)+'\n')
        result=dict(case=name,maximum_estimated_standardized_error=maximum,passed=maximum<5.5,
                    source_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                    raw_sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                    metadata_sha256=hashlib.sha256(metadata_path.read_bytes()).hexdigest(),
                    exact_state_count=len(words),nondegenerate_comparisons=int(mask.sum()))
        results.append(result);print(json.dumps(result),flush=True)
        (HERE/'ADMISSIBILITY_WAVE_CALIBRATION.json').write_text(json.dumps(dict(plan=plan,results=results),indent=2)+'\n')
    assert all(r['passed'] for r in results),'Calibration gate failed; preserve all cases before diagnosis.'


if __name__=='__main__': main()
