#!/usr/bin/env python3
"""Uniformized simulation with axis feature s_i=2n-3v_i^2.

The rate parameters are u=0 and E=alpha/2 for the all-density construction.

The measured fields are density, three vector components and two axis
quadrupoles. Raw Fourier amplitudes permit paired time-correlation analysis.
"""
from pathlib import Path
from itertools import product
import argparse
import hashlib
import json
import time
import numpy as np
import numba as nb

HERE = Path(__file__).resolve().parent
VECTORS = np.array([[0, 0, 0], [1, 0, 0], [-1, 0, 0],
                    [0, 1, 0], [0, -1, 0], [0, 0, 1], [0, 0, -1]], dtype=np.int8)
FIELDS = np.column_stack((np.array([0, 1, 1, 1, 1, 1, 1]), VECTORS,
                           VECTORS[:, 0]**2 - VECTORS[:, 1]**2,
                           VECTORS[:, 0]**2 + VECTORS[:, 1]**2 - 2*VECTORS[:, 2]**2)).astype(float)


def geometry(sides, modes):
    sides = np.asarray(sides, dtype=int)
    coordinates = np.array(list(product(*(range(int(x)) for x in sides))), dtype=int)
    lookup = {tuple(x): i for i, x in enumerate(coordinates)}
    neighbors = np.empty((len(coordinates), len(sides), 3), dtype=np.int64)
    for x, coord in enumerate(coordinates):
        for axis in range(len(sides)):
            for j, displacement in enumerate([-1, 1, 2]):
                target = coord.copy()
                target[axis] = (target[axis] + displacement) % sides[axis]
                neighbors[x, axis, j] = lookup[tuple(target)]
    wavevectors = 2*np.pi*np.asarray(modes, dtype=float)/sides
    phases = np.exp(-1j * coordinates @ wavevectors.T)/np.sqrt(len(coordinates))
    return neighbors, phases, wavevectors


def rate_ceiling(u, coupling, floor, variant):
    values = []
    for l, a, b, r in product(range(7), repeat=4):
        f = VECTORS[:, 0]
        n = FIELDS[:, 0]
        feature=2*n-3*f*f
        h = u*(f[a]-f[b]) + coupling*((f[a]-f[b])*(feature[l]+feature[r])
                                      +(feature[a]-feature[b])*(f[l]+f[r]))
        values.append(floor+max(h, 0) if variant == 0 else floor+h/2)
    if min(values) < 0:
        raise ValueError('Negative rate in the declared menu')
    return float(max(values)), float(min(values))


@nb.njit(cache=True)
def single_path(seed, neighbors, phases, fields, vectors, probabilities,
                times, u, coupling, floor, variant, ceiling, epsilon):
    np.random.seed(seed)
    volume, dimensions = neighbors.shape[:2]
    modes = phases.shape[1]
    state = np.empty(volume, dtype=np.int8)
    initial_counts = np.zeros(7, dtype=np.int64)
    cumulative = np.cumsum(probabilities)
    for x in range(volume):
        label = min(np.searchsorted(cumulative, np.random.random()), 6)
        state[x] = label
        initial_counts[label] += 1
    fourier = np.zeros((modes, 6), dtype=np.complex128)
    for x in range(volume):
        for mode in range(modes):
            for obs in range(6):
                fourier[mode, obs] += phases[x, mode]*fields[state[x], obs]
    observed = np.empty((len(times), modes, 6), dtype=np.complex128)
    observed[0] = fourier
    observation = 1
    total_rate = volume*(dimensions*ceiling+6*epsilon)
    exchange_probability = dimensions*ceiling/(dimensions*ceiling+6*epsilon)
    now = 0.0
    proposals = 0
    accepted_exchanges = 0
    visible_exchanges = 0
    accepted_births = np.zeros(7, dtype=np.int64)
    while observation < len(times):
        now += -np.log(max(np.random.random(), 1e-300))/total_rate
        while observation < len(times) and times[observation] < now:
            observed[observation] = fourier
            observation += 1
        if observation == len(times):
            break
        proposals += 1
        x = np.random.randint(volume)
        if np.random.random() < exchange_probability:
            axis = np.random.randint(dimensions)
            left, y, right = neighbors[x, axis]
            l, a, b, r = state[left], state[x], state[y], state[right]
            fa, fb = vectors[a, axis], vectors[b, axis]
            sl=2*fields[l,0]-3*vectors[l,axis]**2
            sr=2*fields[r,0]-3*vectors[r,axis]**2
            sa=2*fields[a,0]-3*fa**2
            sb=2*fields[b,0]-3*fb**2
            h = u*(fa-fb)+coupling*((fa-fb)*(sl+sr)+(sa-sb)*(vectors[l,axis]+vectors[r,axis]))
            rate = floor+max(h, 0.0) if variant == 0 else floor+h/2
            if np.random.random()*ceiling < rate:
                accepted_exchanges += 1
                if a != b:
                    visible_exchanges += 1
                    for mode in range(modes):
                        phase_difference = phases[x, mode]-phases[y, mode]
                        for obs in range(6):
                            fourier[mode, obs] += phase_difference*(fields[b, obs]-fields[a, obs])
                    state[x], state[y] = b, a
        elif state[x] == 0:
            label = np.random.randint(1, 7)
            accepted_births[label] += 1
            state[x] = label
            for mode in range(modes):
                for obs in range(6):
                    fourier[mode, obs] += phases[x, mode]*fields[label, obs]
    final_counts = np.zeros(7, dtype=np.int64)
    direct = np.zeros((modes, 6), dtype=np.complex128)
    for x in range(volume):
        final_counts[state[x]] += 1
        for mode in range(modes):
            for obs in range(6):
                direct[mode, obs] += phases[x, mode]*fields[state[x], obs]
    for a in range(1, 7):
        assert final_counts[a] == initial_counts[a]+accepted_births[a]
    assert final_counts[0] == initial_counts[0]-accepted_births.sum()
    drift = np.max(np.abs(direct-fourier))
    statistics = np.array([proposals, accepted_exchanges, visible_exchanges,
                            accepted_births.sum(), initial_counts[0], final_counts[0], drift])
    return observed, statistics


@nb.njit(cache=True, parallel=True)
def many_paths(seeds, neighbors, phases, fields, vectors, probabilities,
               times, u, coupling, floor, variant, ceiling, epsilon):
    output = np.empty((len(seeds), len(times), phases.shape[1], 6), dtype=np.complex128)
    statistics = np.empty((len(seeds), 7))
    for index in nb.prange(len(seeds)):
        output[index], statistics[index] = single_path(
            seeds[index], neighbors, phases, fields, vectors, probabilities,
            times, u, coupling, floor, variant, ceiling, epsilon)
    return output, statistics


def run(sides, modes, probabilities, times, trajectories, seed, u=0., coupling=.5,
        floor=.05, variant=0, epsilon=0., threads=4):
    nb.set_num_threads(threads)
    neighbors, phases, wavevectors = geometry(sides, modes)
    ceiling, minimum = rate_ceiling(u, coupling, floor, variant)
    seeds = np.random.SeedSequence(seed).generate_state(trajectories)
    started = time.monotonic()
    raw, stats = many_paths(seeds, neighbors, phases, FIELDS, VECTORS,
                           np.array(probabilities), np.array(times), u, coupling,
                           floor, variant, ceiling, epsilon)
    assert np.max(stats[:, -1]) < 1e-8, 'Incremental Fourier audit failed'
    metadata = {'sides':list(sides), 'modes':np.asarray(modes).tolist(),
                'wavevectors':wavevectors.tolist(), 'probabilities':list(probabilities),
                'times':np.asarray(times).tolist(), 'trajectories':trajectories,
                'seed':seed, 'u':u, 'E':coupling, 'floor_or_K':floor,
                'variant':'minimal' if variant==0 else 'constant', 'epsilon':epsilon,
                'context_feature':'s_i=2n-3v_i^2', 'alpha_when_u_zero':2*coupling,
                'rate_ceiling':ceiling, 'rate_minimum':minimum,
                'elapsed_seconds':time.monotonic()-started,
                'max_fourier_reconstruction_error':float(np.max(stats[:, -1])),
                'total_proposals':int(stats[:, 0].sum()),
                'field_names':['density','vx','vy','vz','Qxx-Qyy','Qxx+Qyy-2Qzz'],
                'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
                'versions':{'numpy':np.__version__,'numba':nb.__version__},
                'counts_audited_on_every_path':True}
    return raw, stats, seeds, metadata


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--side',type=int,default=16)
    parser.add_argument('--trajectories',type=int,default=256)
    parser.add_argument('--seed',type=int,default=2026092101)
    parser.add_argument('--density',type=float,default=.5)
    parser.add_argument('--u',type=float,default=0.)
    parser.add_argument('--coupling',type=float,default=.5)
    parser.add_argument('--floor',type=float,default=.05)
    parser.add_argument('--variant',choices=['minimal','constant'],default='minimal')
    parser.add_argument('--epsilon',type=float,default=0.)
    parser.add_argument('--threads',type=int,default=4)
    parser.add_argument('--output',type=Path,required=True)
    args=parser.parse_args()
    # One representative from each conjugate pair in the first three shells.
    modes=np.array([[1,0,0],[0,1,0],[0,0,1],
                    [1,1,0],[1,-1,0],[1,0,1],[1,0,-1],[0,1,1],[0,1,-1],
                    [1,1,1],[1,1,-1],[1,-1,1],[1,-1,-1]])
    reference_speed=1/np.sqrt(6)
    times=np.linspace(0,2*np.pi,65)/(reference_speed*2*np.pi/args.side)
    raw,stats,seeds,metadata=run([args.side]*3,modes,
        [1-args.density]+[args.density/6]*6,times,args.trajectories,args.seed,
        args.u,args.coupling,args.floor,0 if args.variant=='minimal' else 1,
        args.epsilon,args.threads)
    args.output.parent.mkdir(parents=True,exist_ok=True)
    np.savez_compressed(args.output,fields=raw,statistics=stats,seeds=seeds,
                        times=times,modes=modes,wavevectors=np.asarray(metadata['wavevectors']))
    args.output.with_suffix('.json').write_text(json.dumps(metadata,indent=2)+'\n')
    print(json.dumps(metadata,indent=2))


if __name__=='__main__':
    main()
