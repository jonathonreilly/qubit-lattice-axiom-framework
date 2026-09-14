#!/usr/bin/env python3
"""One readable complex carrier, a single local rule, and window constants.

The schedule, circuit and probability parameters are supplied. Coherent
control programs are finite positive-probability branches of the default
atom law; selecting such a branch is an explicit conditioning cost.
"""
import itertools
import json
from pathlib import Path

import numpy as np
import sympy as s


PAULI=np.array([[[0,1],[1,0]],[[0,-1j],[1j,0]],[[1,0],[0,-1]]],dtype=complex)
V=np.array([1,2,3])
ROTS=[]
for permutation in itertools.permutations(range(3)):
    for signs in itertools.product((-1,1),repeat=3):
        r=np.zeros((3,3),dtype=int)
        for i in range(3):
            r[i,permutation[i]]=signs[i]
        if round(np.linalg.det(r))==1:
            ROTS.append(r)
ORBIT={tuple(r@V):i for i,r in enumerate(ROTS)}
assert len(ORBIT)==24


def encode(role,frame,z):
    vector=(8*role+1)*(ROTS[frame]@V)
    return z*np.eye(2)+sum(vector[i]*PAULI[i] for i in range(3))


def decode(matrix):
    z=np.trace(matrix)/2
    vector=np.array([np.trace(matrix@p)/2 for p in PAULI])
    assert np.max(abs(vector.imag))<1e-10
    length=np.linalg.norm(vector.real)
    role=round((length/np.sqrt(14)-1)/8)
    assert role>=0
    orbit=tuple(np.rint(vector.real/(8*role+1)).astype(int))
    frame=ORBIT[orbit]
    assert np.linalg.norm(matrix-encode(role,frame,z))<1e-9
    return role,frame,z


def star_action(rotation,matrix):
    z=np.trace(matrix)/2
    components=np.array([np.trace(matrix@p)/2 for p in PAULI])
    vector=rotation@components
    return z*np.eye(2)+sum(vector[i]*PAULI[i] for i in range(3))


def main():
    roots=[(0,0,0),(2,0,0),(2,2,0),(0,2,0)]
    observations=[(1,0,0),(2,1,0),(1,2,0),(0,1,0)]
    controls=[(x,y,1) for x,y,z in roots]
    positions=roots+observations+controls
    parent={i:[8+i] for i in range(4)}
    parent.update({4+i:[i,(i+1)%4] for i in range(4)})
    output={i:[] for i in range(12)}
    for child,pp in parent.items():
        for p in pp:
            output[p].append(child)
            assert sum(abs(a-b) for a,b in zip(positions[child],positions[p]))==1
    delta=lambda a,b:np.array(a)-np.array(b)
    innovations={i:complex((17*i+3)/13,(11*i-2)/19) for i in range(8)}
    expected={i:innovations[i] for i in range(4)}
    expected.update({4+i:expected[(i+1)%4]-expected[i]+innovations[4+i] for i in range(4)})
    rng=np.random.default_rng(539201)
    default_atoms=tuple(itertools.product(range(8,12),range(len(ROTS))))
    default_weight=s.Rational(1,len(default_atoms))
    assert sum(default_weight for _ in default_atoms)==1
    checks=0
    maximum_error=0.
    def rule(site,records):
        # Only the six actual nearest records are read. A candidate target is
        # inferred from an incoming neighbor's finite role/direction table.
        neighbors={}
        for ax in range(3):
            for sign in (-1,1):
                step=np.zeros(3,dtype=int);step[ax]=sign
                point=tuple(np.array(site)+step)
                if point in records:
                    try:
                        decoded=decode(records[point])
                    except (AssertionError,KeyError):
                        return None
                    if decoded[0] not in range(12):
                        return None
                    neighbors[point]=decoded
        candidates=set()
        for point,(r,frame,z) in neighbors.items():
            for child in output.get(r,()):
                target=tuple(np.array(point)+ROTS[frame]@delta(positions[child],positions[r]))
                if target==site:
                    candidates.add((child,frame))
        enabled=[]
        for child,frame in candidates:
            values=[]
            for p in parent[child]:
                point=tuple(np.array(site)+ROTS[frame]@delta(positions[p],positions[child]))
                data=neighbors.get(point)
                if data is None or data[:2]!=(p,frame):
                    break
                values.append(data[2])
            else:
                mean=0j if child<4 else values[1]-values[0]
                enabled.append((child,frame,mean,1.))
        return enabled[0] if len(enabled)==1 else None
    # None denotes the rotation-invariant default: all 4 control roles and
    # all 24 frames with z=0, each atom probability 1/96. It is not a missing
    # distribution; the supplied schedule executes the Gaussian cases only
    # after conditioning on the coherent control program.
    for frame,rotation in enumerate(ROTS):
        origin=np.array([13,-7,5])
        physical=[tuple(rotation@np.array(p)+origin) for p in positions]
        for i in range(12):
            z=complex((i+1)/7,-(i+3)/11)
            r,f,decoded=decode(encode(i,frame,z))
            assert (r,f)==(i,frame) and abs(decoded-z)<1e-12
        for other in ROTS:
            z=.375-.625j
            composite=ORBIT[tuple(other@rotation@V)]
            maximum_error=max(maximum_error,float(np.linalg.norm(
                star_action(other,encode(11,frame,z))-encode(11,composite,z))))
        left=np.array([[1+2j,3-4j],[5+6j,-7+8j]])
        right=np.array([[2-3j,-4+5j],[6-7j,8+9j]])
        assert np.linalg.norm(star_action(rotation,left@right)-star_action(rotation,left)@star_action(rotation,right))<1e-10
        assert np.linalg.norm(star_action(rotation,left.conj().T)-star_action(rotation,left).conj().T)<1e-10
        assert {(r,ORBIT[tuple(rotation@ROTS[f]@V)]) for r,f in default_atoms}==set(default_atoms)
        for _ in range(8):
            records={}
            for i in range(4):
                assert rule(physical[8+i],records) is None
                # The chosen value is one of the 96 positive default atoms.
                records[physical[8+i]]=encode(8+i,frame,0j)
            assert all(sum(abs(a-b) for a,b in zip(x,y))>1 for x,y in itertools.combinations(records,2))
            pending=set(range(8))
            while pending:
                ready=[]
                for i in pending:
                    action=rule(physical[i],records)
                    if action is not None:
                        assert action[:2]==(i,frame)
                        ready.append((i,action))
                assert ready
                i,action=ready[int(rng.integers(len(ready)))]
                assert physical[i] not in records
                records[physical[i]]=encode(i,frame,action[2]+innovations[i])
                pending.remove(i)
            for i in range(8):
                assert abs(decode(records[physical[i]])[2]-expected[i])<1e-12
            checks+=1
    assert maximum_error<1e-10
    for rotation in ROTS:
        bad=star_action(rotation,np.array([[1+2j,3+4j],[5+6j,7+8j]]))
        assert rule((0,0,0),{(1,0,0):bad}) is None

    # Exact diagonal complex-Gaussian disk probabilities challenge the window
    # dimension and pi normalization independently of the determinant code.
    window_rows=[]
    alpha=s.Rational(1,5)
    linear=s.diag(s.Rational(3,2),s.Rational(2,3))
    noise=s.diag(s.Rational(1,2),s.Rational(4,3))
    covariance=noise+linear*linear.H/alpha
    precision=alpha*s.eye(2)+linear.H*noise.inv()*linear
    p0_without_pi=1/covariance.det()
    assert s.cancel(p0_without_pi-alpha**2/(noise.det()*precision.det()))==0
    for epsilon in (s.Rational(1,100),s.Rational(1,2),s.Rational(2)):
        actual=s.prod(1-s.exp(-epsilon**2/covariance[i,i]) for i in range(2))
        high=epsilon**4*p0_without_pi
        exponent=2*epsilon**2/min(noise.diagonal())
        low=s.exp(-exponent)*high
        assert float(low)<=float(actual)<=float(high)
        window_rows.append(dict(epsilon=str(epsilon),acceptance=float(actual),
                                lower_bound=float(low),upper_bound=float(high)))
    # A complex shifted Gaussian equals two real Gaussians with covariance
    # C/2. Their elementary real KL independently fixes the factor of two.
    c=s.Rational(3,7);mean=s.Matrix([s.Rational(2,3),s.Rational(-4,5)])
    real_kl=(mean.T*(s.eye(2)*c/2).inv()*mean)[0]/2
    complex_kl=(mean.dot(mean))/c
    assert real_kl==complex_kl
    # Attainment of the sharp tilt inequality, not only an upper-bound test.
    a,b=s.Rational(1,4),s.Rational(9)
    probability=(b-s.sqrt(a*b))/(b-a)
    mu=probability*a+(1-probability)*b
    tv=(probability*abs(a/mu-1)+(1-probability)*abs(b/mu-1))/2
    sharp=(s.sqrt(b)-s.sqrt(a))/(s.sqrt(b)+s.sqrt(a))
    assert s.simplify(tv-sharp)==0
    result=dict(complex_codec_roles=12,frames=24,star_action_compositions=576,
                maximum_star_action_error=maximum_error,causal_schedules_checked=checks,
                same_rule_reads_six_neighbors=True,records_written_once=True,
                default_control_atoms=len(default_atoms),
                algebra_product_and_star_checks=48,
                coherent_four_control_program_probability=str(default_weight**4),
                complex_disk_window_checks=window_rows,
                independent_real_complex_kl=str(real_kl),sharp_tilt_bound_attained=str(sharp),
                scope='Supplied program and fair schedule; coherent finite controls and later observations are conditioned on, not typical-state or Born selection')
    Path(__file__).with_name('BLOCK5_LOCAL_RULE_WINDOW_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
