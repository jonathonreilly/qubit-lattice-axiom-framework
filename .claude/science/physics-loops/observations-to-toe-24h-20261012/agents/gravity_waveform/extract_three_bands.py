#!/usr/bin/env python3
"""Implement the frozen development contract; no matched chirp template."""
import os
for _name in ("OPENBLAS_NUM_THREADS", "OMP_NUM_THREADS", "MKL_NUM_THREADS",
              "VECLIB_MAXIMUM_THREADS", "NUMEXPR_NUM_THREADS"):
    os.environ[_name] = "1"

import hashlib
import json
import math
from datetime import datetime, timezone
from pathlib import Path

import h5py
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import scipy
from scipy.signal import spectrogram, windows

CAMPAIGN = Path("/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012")
RUNTIME = CAMPAIGN / "gravity_measurements" / "waveform"
CONTRACT = Path(__file__).with_name("EXTRACTION_CONTRACT.md")
EXPECTED_CONTRACT_SHA = "1bb220086059126add589bb4a3f2f04c0c35044cfecd361c620157e59ddfa937"
REFERENCE_GPS = 1187008882.43
BANDS = ((48.,52.),(68.,72.),(88.,92.))
CENTERS = np.array([50.,70.,90.])


def guard():
    assert not list(CAMPAIGN.glob("*STOP_REQUESTED*")), "Campaign stop marker"
    deadline=json.loads((CAMPAIGN/"DEADLINE.json").read_text())["deadline_epoch"]
    assert datetime.now(timezone.utc).timestamp()<deadline, "Campaign deadline"
    assert hashlib.sha256(CONTRACT.read_bytes()).hexdigest()==EXPECTED_CONTRACT_SHA


def native(value):
    if isinstance(value,bytes):
        return value.decode()
    if isinstance(value,np.ndarray):
        return [native(x) for x in value.tolist()]
    if isinstance(value,np.generic):
        return native(value.item())
    if isinstance(value,dict):
        return {str(k):native(v) for k,v in value.items()}
    if isinstance(value,(list,tuple)):
        return [native(v) for v in value]
    return value


def components(t,score,threshold):
    indices=np.flatnonzero(score>=threshold)
    if not len(indices):
        return []
    groups=np.split(indices,np.flatnonzero(np.diff(indices)>1)+1)
    answer=[]
    for group in groups:
        peak=int(group[np.argmax(score[group])])
        answer.append(dict(first_center=float(t[group[0]]),last_center=float(t[group[-1]]),
                           peak_time=float(t[peak]),peak_score=float(score[peak]),
                           padded_interval=[float(t[group[0]]-.55),float(t[group[-1]]+.55)],
                           frames=int(len(group))))
    return sorted(answer,key=lambda v:v["peak_score"],reverse=True)


def calibration(detector):
    path=RUNTIME/"calibration"/f"GWTC1_GW170817_{detector[0]}_CalEnv.txt"
    data=np.loadtxt(path)
    rows=[]
    for f in CENTERS:
        values=[float(np.interp(f,data[:,0],data[:,col])) for col in range(1,7)]
        rows.append(dict(frequency_hz=float(f),median_amplitude=values[0],
                         median_phase_rad=values[1],minus_1sigma_amplitude=values[2],
                         minus_1sigma_phase_rad=values[3],plus_1sigma_amplitude=values[4],
                         plus_1sigma_phase_rad=values[5]))
    return dict(path=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
                interpolation="linear, as documented by the release",values=rows,
                limitation="envelopes alone are not a joint phase-covariance/timing-error model")


def analyze_detector(detector):
    guard()
    path=RUNTIME/f"{detector[0]}-{detector}_GWOSC_4KHZ_R1-1187008867-32.hdf5"
    with h5py.File(path,"r") as f:
        ds=f["strain/Strain"]
        strain=ds[:]
        attributes=native(dict(ds.attrs))
        meta={k:native(f["meta"][k][()]) for k in f["meta"]}
        quality={}
        for folder in ("simple","injections"):
            quality[folder]={k:dict(data=native(f[f"quality/{folder}/{k}"][()]),
                                         attrs=native(dict(f[f"quality/{folder}/{k}"].attrs)))
                             for k in f[f"quality/{folder}"]}
    fs=1/attributes["Xspacing"]
    assert fs==4096 and len(strain)==131072 and np.isfinite(strain).all()
    frequency,elapsed,power=spectrogram(strain,fs=fs,window=windows.hann(4096,sym=False),
        nperseg=4096,noverlap=3968,nfft=4096,detrend="constant",return_onesided=True,
        scaling="density",mode="psd")
    relative=elapsed+(attributes["Xstart"]-REFERENCE_GPS)
    target=(relative>=-14.75)&(relative<=-2.25)
    background=(relative>=4.5)&(relative<=13.5)
    med=np.median(power[:,background],axis=1)
    assert np.all(med>0)
    normalized=power/med[:,None]
    bands=[]
    band_scores=[]
    for low,high in BANDS:
        inband=(frequency>=low)&(frequency<=high)
        score=normalized[inband].mean(axis=0)
        threshold=max(3.,float(np.quantile(score[background],.99,method="linear")))
        found=components(relative[target],score[target],threshold)
        maxindex=int(np.argmax(score[target]))
        bands.append(dict(band_hz=[low,high],nominal_frequency_hz=(low+high)/2,
            frequency_bins=frequency[inband].tolist(),threshold=threshold,
            background_median_score=float(np.median(score[background])),
            background_99pct_score=float(np.quantile(score[background],.99,method="linear")),
            maximum_target_time=float(relative[target][maxindex]),
            maximum_target_score=float(score[target][maxindex]),
            components=found,has_threshold_component=bool(found),
            strongest_component=found[0] if found else None))
        band_scores.append(score)
    keep=(frequency>=35)&(frequency<=110)
    np.savez_compressed(RUNTIME/f"{detector}_spectrogram.npz",frequency=frequency[keep],
        relative_time=relative,power=power[keep],background_median=med[keep],
        normalized_power=normalized[keep],band_scores=np.array(band_scores),
        target_mask=target,background_mask=background)
    return dict(detector=detector,file=str(path),sha256=hashlib.sha256(path.read_bytes()).hexdigest(),
        metadata=meta,strain_attributes=attributes,quality=quality,
        calibration=calibration(detector),bands=bands,
        target_centers=[float(relative[target][0]),float(relative[target][-1])],
        target_support=[float(relative[target][0]-.5),float(relative[target][-1]+.5)],
        background_centers=[float(relative[background][0]),float(relative[background][-1])],
        source_samples=len(strain),target_frames=int(target.sum()),background_frames=int(background.sum()))


def coefficients(frequency):
    x=frequency**(-8/3)
    q=frequency**(-2)
    lam=(x[1]-x[2])/(x[0]-x[2])
    kappa=q[1]-lam*q[0]-(1-lam)*q[2]
    assert 0<lam<1 and kappa>0
    return float(lam),float(kappa)


def interval_contrast(intervals,lam,kappa):
    lo=np.array([v[0] for v in intervals])
    hi=np.array([v[1] for v in intervals])
    cmin=lo[1]-lam*hi[0]-(1-lam)*hi[2]
    cmax=hi[1]-lam*lo[0]-(1-lam)*lo[2]
    return dict(intervals=intervals,contrast_interval_s=[float(cmin),float(cmax)],
                necessary_A_interval_s_hz2=[max(0.,float(cmin/kappa)),float(cmax/kappa)],
                compatible_with_nonnegative_A=bool(cmax>=0))


def contrast_analysis(detectors):
    c=299792458.
    mu=6.42760036943869e-12
    distance=26*3.0856775814913673e22
    a=distance*c*mu*mu/(8*math.pi**2)
    lam,kappa=coefficients(CENTERS)
    f1lo,f1hi,f2lo,f2hi,f3lo=45.,55.,65.,75.,85.
    klower=3/32*f1lo**(10/3)*(f1hi**(-8/3)-f2lo**(-8/3))*(f2hi**(-8/3)-f3lo**(-8/3))
    z=(c*mu/(2*math.pi*CENTERS))**2
    exact=distance/c*np.expm1(-.5*np.log1p(-z))
    leading=a/CENTERS**2
    result=dict(mu_per_m=mu,distance_m=distance,A_s_hz2=a,nominal_frequencies_hz=CENTERS.tolist(),
        lambda_coefficient=lam,kappa_hz_minus2=kappa,predicted_contrast_s=a*kappa,
        leading_delays_s=leading.tolist(),exact_delays_s=exact.tolist(),
        maximum_relative_dispersion_expansion_error=float(np.max(abs(exact/leading-1))),
        robust_frequency_ranges_hz=[[45.,55.],[65.,75.],[85.,95.]],
        rigorous_curvature_kappa_lower_bound=klower,
        broad_timing_hull_s=[-15.30,-1.70],broad_width_s=13.60,
        broad_nominal_A_upper=13.60/kappa,
        broad_frequency_box_A_upper=13.60/klower,
        pole_to_broad_frequency_box_bound_ratio=a/(13.60/klower),
        minimum_equal_source_time_residual_to_remove_broad_contradiction_s=max(0.,(a*klower-13.60)/2),
        interpretation="conditional deterministic interval compatibility; no likelihood/significance",
        detector_component_contrasts=[])
    for detector in detectors:
        selected=[band["strongest_component"] for band in detector["bands"]]
        if all(selected):
            intervals=[v["padded_interval"] for v in selected]
            row=interval_contrast(intervals,lam,kappa)
            row["detector"]=detector["detector"]
            row["assumption"]="strongest components are the three source arrivals; competing components retained"
            result["detector_component_contrasts"].append(row)
    return result


def plot(detectors):
    fig,axes=plt.subplots(2,2,figsize=(13,7),layout="constrained")
    for i,detector in enumerate(detectors):
        data=np.load(RUNTIME/f"{detector['detector']}_spectrogram.npz")
        t=data["relative_time"]
        target=data["target_mask"]
        values=np.minimum(data["normalized_power"][:,target],15)
        mesh=axes[i,0].pcolormesh(t[target],data["frequency"],values,shading="auto",
                                  vmin=0,vmax=15,cmap="magma")
        axes[i,0].set(ylim=(40,105),ylabel=f"{detector['detector']} frequency (Hz)",
                      title="Local power / off-source median (display clipped at 15)")
        for j,band in enumerate(detector["bands"]):
            axes[i,1].plot(t[target],data["band_scores"][j,target],label=f"{int(CENTERS[j])} Hz")
            axes[i,1].axhline(band["threshold"],alpha=.25,linestyle="--",color=f"C{j}")
        axes[i,1].set(ylabel="Five-bin mean normalized power",title="Frozen bands; dashed diagnostic thresholds")
        axes[i,1].legend()
        for ax in axes[i]:
            ax.set_xlabel("Time relative to GPS 1187008882.43 (s)")
            ax.set_xlim(-14.75,-2.25)
    fig.colorbar(mesh,ax=axes[:,0],label="Normalized power")
    fig.savefig(RUNTIME/"frozen_three_band_diagnostics.png",dpi=160)
    plt.close(fig)


def main():
    guard()
    started=datetime.now(timezone.utc).isoformat()
    detectors=[analyze_detector("L1"),analyze_detector("H1")]
    matches=[]
    for l,h in zip(detectors[0]["bands"],detectors[1]["bands"]):
        lc,hc=l["strongest_component"],h["strongest_component"]
        difference=abs(lc["peak_time"]-hc["peak_time"]) if lc and hc else None
        matches.append(dict(frequency_hz=l["nominal_frequency_hz"],
            both_have_threshold_component=bool(lc and hc),peak_difference_s=difference,
            strongest_components_match=bool(difference is not None and difference<=2.)))
    result=dict(started_utc=started,finished_utc=datetime.now(timezone.utc).isoformat(),
        contract_sha256=EXPECTED_CONTRACT_SHA,
        code_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        versions=dict(numpy=np.__version__,scipy=scipy.__version__,h5py=h5py.__version__,
                      matplotlib=matplotlib.__version__),
        transform=dict(sample_rate_hz=4096,window_samples=4096,hop_samples=128,
                       window="periodic Hann",detrend="constant within each window",
                       scaling="one-sided density",frequency_bin_hz=1,
                       global_whitening=False,glitch_subtraction=False),
        detectors=detectors,cross_detector_control=matches,
        all_strongest_controls_match=all(v["strongest_components_match"] for v in matches),
        contrast=contrast_analysis(detectors))
    plot(detectors)
    (RUNTIME/"frozen_extraction_results.json").write_text(json.dumps(native(result),indent=2)+"\n")
    print(json.dumps(dict(detectors=[dict(detector=v["detector"],bands=v["bands"]) for v in detectors],
        controls=matches,contrast=result["contrast"]),indent=2))


if __name__=="__main__":
    main()
