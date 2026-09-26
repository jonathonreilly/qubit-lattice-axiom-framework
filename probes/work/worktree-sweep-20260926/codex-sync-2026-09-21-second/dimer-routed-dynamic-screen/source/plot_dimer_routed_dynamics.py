#!/usr/bin/env python3
"""Render all declared finite-size cells and write a bounded assessment."""
from pathlib import Path
import argparse, datetime, hashlib, json
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

HERE = Path(__file__).resolve().parent

def identity(p):
    p = Path(p)
    return dict(path=str(p.resolve()), bytes=p.stat().st_size,
                sha256=hashlib.sha256(p.read_bytes()).hexdigest())

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--analysis', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    result = json.loads((args.analysis/'RESULTS.json').read_text())
    assert len(result['cells']) == 8
    assert sum(c['histories'] for c in result['cells']) == 960
    args.output.mkdir(parents=True, exist_ok=True)
    labels = ['Mean-square propagation error', 'Transverse autocovariance',
              'Signed E–B cross covariance', 'Longitudinal autocovariance']
    colors = {16:'#b1b6bd', 32:'#8796ae', 64:'#457caf', 128:'#094777'}
    fig, axes = plt.subplots(4, 2, figsize=(11.8, 12.0), sharex=True)
    dense = np.linspace(0, 1.75, 201)
    targets = [np.zeros_like(dense), np.cos(4*np.pi*dense/7),
               np.sin(4*np.pi*dense/7), np.ones_like(dense)]
    for col, kind in enumerate(['winding', 'irregular']):
        for metric in range(4):
            ax = axes[metric, col]
            ax.plot(dense, targets[metric], color='#cc5536', ls='--', lw=1.7,
                    label='Conditional Euler-limit target', zorder=3)
            for cell in sorted((x for x in result['cells'] if x['kind']==kind), key=lambda x:x['N']):
                y = np.array(cell['mode_average']['mean'])[:, metric]
                low = np.array(cell['mode_average']['bootstrap95_low'])[:, metric]
                high = np.array(cell['mode_average']['bootstrap95_high'])[:, metric]
                ax.errorbar(cell['times'], y, yerr=np.stack([y-low, high-y]),
                            color=colors[cell['N']], marker='o', ms=4, capsize=2,
                            lw=1.5, label=f"N={cell['N']}; {cell['histories']} histories")
            ax.grid(alpha=.17)
            ax.spines[['top','right']].set_visible(False)
            ax.set_ylabel(labels[metric], fontsize=10)
            if metric == 0:
                ax.set_title(kind.capitalize()+' fixed matching', fontsize=12, pad=12)
                ax.set_ylim(-.07, 2.2)
            if metric == 1: ax.set_ylim(-1.12, 1.2)
            if metric == 2: ax.set_ylim(-.16, 1.17)
            if metric == 3: ax.set_ylim(-.16, 1.4)
            if metric == 3:
                ax.set_xlabel('Macroscopic time t (microscopic elapsed time N t)')
                ax.set_xticks([0,7/16,7/8,21/16,7/4], ['0','7/16','7/8','21/16','7/4'])
    handles, names = axes[0,0].get_legend_handles_labels()
    fig.legend(handles, names, loc='upper center', bbox_to_anchor=(.5,.948), ncol=3,
               frameon=False, fontsize=9)
    fig.suptitle('Record-color transport: finite systems remain substantially damped',
                 fontsize=16, y=.991)
    fig.text(.5,.959,'All 960 declared histories • three axis modes averaged within each history',
             ha='center', fontsize=10)
    fig.text(.5,.016,
             'Bars: pointwise 95% whole-history bootstrap intervals; no simultaneous coverage.\n'
             'Fixed γ=1, k₀=1.1; iid 14-color initialization. Lines connect observations; no fitted damping law.',
             ha='center', fontsize=9, color='#444444')
    fig.subplots_adjust(top=.865, bottom=.08, hspace=.21, wspace=.24)
    for suffix in ('png','pdf'):
        fig.savefig(args.output/('DIMER_ROUTED_DYNAMIC_SCREEN.'+suffix), dpi=180)
    plt.close(fig)

    def interval(cell, t, metric):
        x=cell['mode_average'];mu=x['mean'][t][metric]
        return f"{mu:.4f} [{x['bootstrap95_low'][t][metric]:.4f}, {x['bootstrap95_high'][t][metric]:.4f}]"
    text = '''# Finite-size record-color dynamics: completed screen

2026-09-21. Root finite numerical assessment; no formal audit or retained status.

All 960 declared histories completed with verified output receipts and without
exclusions. At the tested sizes, the color-wave signals have substantial finite
damping. The mean-square error from the conditional Euler propagator decreases
across the four tested sizes, but remains large at N=128. These data neither
establish the limit nor give a contradiction to its asymptotic statement.
No damping law or convergence exponent has been fitted.

## Protocol and measured quantities

The frozen protocol uses N=16,32,64,128 with respectively 256,128,64,32
independent histories for each of two frozen matching fixtures. One fixture
has maximal winding along the first coordinate; the other is generated from
a columnar matching by a fixed number of seeded plaquette proposals. The
second fixture is not claimed to be sampled from a uniform matching law.
The records exchange whole pairs with gamma=1, k0=1.1. Geometry is fixed.
Each history starts with independent uniform fourteen-color keys. This is
a stationary-color test, not an empty-start preparation simulation, and
does not test the new moving-geometry extension.

For each of the three positive fundamental axis modes, let z=(E,B) with
E=sqrt(7)X and B=sqrt(7)Y/2. The exact initial second moment is I_6. The
continuum predictor is U=P_L+cos(theta)P_T+sin(theta)D, where
theta=4 pi t/7, D=[[0,i C_hat],[-i C_hat,0]], and C_hat v=q_hat cross v.
The four recorded statistics are ||z_t-U z_0||^2/6,
Re[(P_T z_0)^dagger z_t]/4, Re[(D z_0)^dagger z_t]/4,
and Re[(P_L z_0)^dagger z_t]/2. Their limit targets are respectively
0, cos(theta), sin(theta), and 1. Both longitudinal components are retained.
There is no division by an observed initial sample variance.

Each independent history is the sampling unit. The plotted values average
the three mode statistics inside that history before averaging histories.
Ten thousand whole-history resamples preserve correlations among all modes,
times and components. Reported intervals are pointwise percentile 95%
intervals, not simultaneous confidence bands or selected hypothesis tests.
All individual modes and component variances are retained in RESULTS.json.

## Quarter-period observations

At t=7/8 the exact limit targets are error 0, transverse autocovariance 0,
signed cross covariance 1, and longitudinal autocovariance 1. The following
entries give mean [pointwise 95% interval].

| N | Geometry | Histories | Propagation error | Signed cross | Longitudinal |
| --- | --- | ---: | --- | --- | --- |
'''
    for c in result['cells']:
        text += f"| {c['N']} | {c['kind']} | {c['histories']} | {interval(c,2,0)} | {interval(c,2,2)} | {interval(c,2,3)} |\n"
    text += '''
The signed cross term has the predicted orientation and grows in magnitude
with the tested size at this time. Even at N=128 its intervals remain below
the unit limit target. The propagation error is about 0.73–0.78, so it would
be misleading to describe these runs as a clean undamped-wave demonstration.
The longitudinal modes also lose substantial finite-time correlation.

## Half-period observations at the largest completed size

At t=7/4 the targets are error 0, transverse autocovariance -1, signed cross
covariance 0, and longitudinal autocovariance 1.

| Geometry | Propagation error | Transverse auto | Signed cross | Longitudinal |
| --- | --- | --- | --- | --- |
'''
    for c in result['cells']:
        if c['N']==128:
            text += '| '+c['kind']+' | '+' | '.join(interval(c,4,j) for j in range(4))+' |\n'
    text += '''
The negative transverse correlations and near-zero signed cross term are
consistent with the predicted half-period phase. Their amplitudes and the
mean-square residual still show strong finite corrections. Unequal sample
counts across sizes are displayed explicitly; the two geometries are not
pooled or treated as independent draws from a geometric equilibrium.

## Verification and limits

The author analyzer authenticated every byte of all 3,840 production payloads
against the saved history receipts, then read every history JSON. It hashed
the binary endpoint states but did not decode them. Exact current, covariance,
Fourier-sign and unitary-propagator controls were frozen before aggregate
access. The complete source and all output identities are bound separately.

The selective independent implementation check reconstructed all contexts,
the generator normalization, two small logged event histories and 16
preselected production endpoints. It reproduced selected initial and final
Fourier fields with maximum complex error 5.651e-14, and checked physical
record identities. It did not replay all production trajectories or inspect
the aggregate analyzer and bootstrap. A separate aggregate check remains
pending at the time of this assessment.

The independent asymptotic theorem check and this finite screen answer
different questions. Neither establishes a physical electromagnetic field,
quantum dynamics, a geometric photon, empirical validity, or a TOE.

A fixed 16-history N=256 follow-up was declared after these N<=128 outcomes
were inspected. Its protocol, source identities, resource limit and hard
campaign deadline are separate. It is not silently appended to the original
screen or presented as an outcome-blind extension. No N=256 result was used
in this assessment.
'''
    for role,path in [('Analyzer',HERE/'analyze_dimer_routed_dynamics.py'),
                      ('Aggregate results',args.analysis/'RESULTS.json'),
                      ('Per-history values',args.analysis/'PER_HISTORY.json'),
                      ('Protocol',HERE/'DIMER_ROUTED_DYNAMIC_SCREEN_PROTOCOL.md')]:
        text += f"\n{role} SHA-256: `{identity(path)['sha256']}`.\n"
    note=HERE/'DIMER_ROUTED_DYNAMIC_SCREEN_ASSESSMENT.md'
    note.write_text(text)
    receipt=dict(created_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),
                 source=identity(__file__),analysis=identity(args.analysis/'RESULTS.json'),
                 outputs=[identity(note)]+[identity(args.output/('DIMER_ROUTED_DYNAMIC_SCREEN.'+s)) for s in ('png','pdf')],
                 visual_inspection='Pending root image inspection; this script does not establish layout quality.')
    (args.output/'PLOT_RECEIPT.json').write_text(json.dumps(receipt,indent=2)+'\n')
    print(json.dumps(receipt,indent=2))

if __name__=='__main__': main()
