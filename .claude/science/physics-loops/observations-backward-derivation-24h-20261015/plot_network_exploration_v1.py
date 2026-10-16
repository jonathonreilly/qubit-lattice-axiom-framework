#!/usr/bin/env python3
"""Illustrative synthetic figure for checked blocks15-16; no measured data."""
from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import json,hashlib

p=Path(__file__).resolve().parent
plt.rcParams.update({'font.family':'DejaVu Sans','font.size':11,
                     'axes.spines.top':False,'axes.spines.right':False,
                     'axes.titleweight':'bold','axes.labelcolor':'#29394b'})
fig,axes=plt.subplots(1,3,figsize=(14,4.4),layout='constrained')
blue='#1765a0';orange='#d47422';green='#25826a'
# Stable boundary is a chosen example, not a selected physical potential.
m,k,tau,C,g=1.2,1.1,.9,2.3,.8
lam=g*g/(8*C)
q=np.linspace(-1.2,1.2,151)
force_relaxed=k*q+(4*lam-g*g/(2*C))*q**3
axes[0].plot(q,k*q,color=blue,lw=3,label='Fixed linear connection')
axes[0].plot(q,force_relaxed,color=orange,lw=2,ls='--',label='Adaptive, relaxed state')
axes[0].set(title='Same static force',xlabel='Coordinate q (chosen units)',ylabel='Force (chosen units)')
axes[0].legend(frameon=False,loc='upper left',fontsize=9)
axes[0].text(.34,.04,'Allowed stability boundary chosen\nBoth curves coincide',transform=axes[0].transAxes,fontsize=9,color='#46556a',bbox=dict(facecolor='white',edgecolor='none',alpha=.92))
r=np.linspace(.02,.82,180)
axes[1].axhline(0,color=blue,lw=2,label='Fixed linear connection')
axes[1].plot(r,1-1/(1-r*r),color=orange,lw=2.5,label='Adaptive connection')
axes[1].set(title='Different dynamic response',xlabel=r'Drive rate $2\omega/\Omega$',ylabel=r'Third-harmonic coefficient $B_3/\lambda_4$')
axes[1].set_ylim(-2.15,.35)
axes[1].legend(frameon=False,loc='lower left',fontsize=9)
axes[1].text(.04,.96,'Positive drive frequency; below resonance\nPeriodic hidden response assumed',va='top',transform=axes[1].transAxes,fontsize=9,color='#46556a',bbox=dict(facecolor='white',edgecolor='none',alpha=.92))
# Different hidden states alter actual force traces. Block16 tests their common
# weak relation; this plot itself is not a fit or that proof.
tt=np.linspace(0,6,500)
qfun=lambda t:1.3+.25*np.sin(.9*t+.5)+.17*np.cos(1.53*t)+.07*np.sin(2.61*t)
qdd=lambda t:-.25*.9**2*np.sin(.9*t+.5)-.17*1.53**2*np.cos(1.53*t)-.07*2.61**2*np.sin(2.61*t)
ln=.11
for initial,color in [((.4,-.3),blue),((-.7,.2),orange),((.9,.1),green)]:
    def rhs(t,y):return [y[1],(-C*y[0]-.5*g*qfun(t)**2)/tau]
    sol=solve_ivp(rhs,[0,6],initial,t_eval=tt,rtol=1e-11,atol=1e-13)
    assert sol.success
    qq=qfun(tt);force=m*qdd(tt)+k*qq+4*ln*qq**3+g*sol.y[0]*qq
    axes[2].plot(tt,force,color=color,lw=1.7,label=str(initial))
axes[2].set(title='Unknown starts remain physical',xlabel='Time (chosen units)',ylabel='Force for the same imposed motion')
axes[2].set_ylim(0,5)
axes[2].legend(title='Initial hidden state (w, velocity)',frameon=False,fontsize=8,title_fontsize=8)
axes[2].text(.04,.96,'Different traces can obey one\npreparation-independent weak test',va='top',transform=axes[2].transAxes,fontsize=9,color='#46556a',bbox=dict(facecolor='white',edgecolor='none',alpha=.92))
fig.suptitle('A conditional neighborhood-evolution candidate',fontsize=16,fontweight='bold')
fig.supxlabel('Synthetic calculations only. The action and physical measurement mapping are assumptions; quantum outcome statistics are not derived.',fontsize=10,color='#46556a')
fig.savefig(p/'NETWORK_EVOLUTION_CANDIDATE_v1.png',dpi=170)
fig.savefig(p/'NETWORK_EVOLUTION_CANDIDATE_v1.svg')
svg=p/'NETWORK_EVOLUTION_CANDIDATE_v1.svg'
svg.write_text('\n'.join(line.rstrip() for line in svg.read_text().splitlines())+'\n')
receipt={'kind':'synthetic illustration, not empirical data','script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'sources':{name:hashlib.sha256((p/name).read_bytes()).hexdigest() for name in ['NETWORK_EVOLUTION_BLOCK15_v2.md','NETWORK_EVOLUTION_BLOCK16_v1.md']},
         'files':{name:hashlib.sha256((p/name).read_bytes()).hexdigest() for name in ['NETWORK_EVOLUTION_CANDIDATE_v1.png','NETWORK_EVOLUTION_CANDIDATE_v1.svg']}}
(p/'NETWORK_EVOLUTION_FIGURE_RECEIPT_v1.json').write_text(json.dumps(receipt,indent=2)+'\n')
print(json.dumps(receipt,indent=2))
