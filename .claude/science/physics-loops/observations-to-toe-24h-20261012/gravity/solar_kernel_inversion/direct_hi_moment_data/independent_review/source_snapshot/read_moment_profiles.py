#!/usr/bin/env python3
"""Frozen, descriptive readout of DDO125 public moment maps; no source fit."""
from __future__ import annotations
import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import sys
import warnings
import astropy
from astropy.io import fits
from astropy.wcs import WCS
import numpy as np

HERE = Path(__file__).resolve().parent
DISTANCE_KPC = 2590.0
R0 = 0.94
CENTERS = {'catalog': ((12+27/60+41.8/3600)*15, 43+29/60+38/3600),
           'pointing': ((12+27/60+40.9/3600)*15, 43+29/60+44/3600)}
INCLINATIONS = (60, 63, 66)
POSITION_ANGLES = (118, 120, 135, 150)
WIDTHS = (0.18, 0.36, 0.54)
ANNULUS_WIDTH = 0.09

def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def beam(header):
    entries = re.findall(r'CLEAN BMAJ=\s*([\d.E+-]+) BMIN=\s*([\d.E+-]+) BPA=\s*([\d.E+-]+)',
                         '\n'.join(header.get('HISTORY', [])))
    assert len(set(entries)) == 1, entries
    major, minor, pa = map(float, entries[0])
    return np.array([major*3600, minor*3600, pa])

def tangent(ra, dec, center):
    """Exact gnomonic east/north lengths about a declared sky center."""
    a, d = np.deg2rad(ra), np.deg2rad(dec)
    a0, d0 = np.deg2rad(center)
    da = a-a0
    denom = np.sin(d)*np.sin(d0)+np.cos(d)*np.cos(d0)*np.cos(da)
    east = np.cos(d)*np.sin(da)/denom*DISTANCE_KPC
    north = (np.sin(d)*np.cos(d0)-np.cos(d)*np.sin(d0)*np.cos(da))/denom*DISTANCE_KPC
    return east, north

def projection(inclination, pa):
    i, p = np.deg2rad([inclination, pa])
    return np.array([[np.sin(p), np.cos(p)],
                     [np.cos(p)/np.cos(i), -np.sin(p)/np.cos(i)]])

def projected_beam(beam_values, inclination, pa):
    major, minor, angle = beam_values
    a = np.deg2rad(angle)
    v, w = np.array([np.sin(a), np.cos(a)]), np.array([np.cos(a), -np.sin(a)])
    C = (major**2*np.outer(v,v)+minor**2*np.outer(w,w))/(8*np.log(2))
    T = projection(inclination, pa)*DISTANCE_KPC*np.pi/(180*3600)
    disk = T@C@T.T
    return {'sky_fwhm_arcsec': beam_values.tolist(),
            'disk_covariance_kpc2': disk.tolist(),
            'disk_principal_fwhm_kpc': np.sqrt(np.linalg.eigvalsh(disk)*8*np.log(2)).tolist()}

def chord(lo, hi, rlo, rhi):
    delta = math.log(rhi/rlo)
    s0, s1 = lo['paired_mean_N_cm2'], hi['paired_mean_N_cm2']
    q0, q1 = lo['paired_mean_N_m2square'], hi['paired_mean_N_m2square']
    assert min(s0,s1,q0,q1) > 0
    return {'minus_log_density_chord': -math.log(s1/s0)/delta,
            'minus_log_product_chord': -math.log(q1/q0)/delta,
            'p_proxy_kms2': -(q1-q0)/(delta*(s0+s1)/2),
            'density_ratio': s1/s0, 'product_ratio': q1/q0}

def controls():
    # Exact formula for synthetic constant and power-law endpoint data.
    rows=[]
    for a,b in [(0,0),(2,0),(1.2,.7),(-.5,1.5),(3,-1)]:
        rlo,rhi=.76,1.12
        make=lambda r:{'paired_mean_N_cm2':r**(-a),
                       'paired_mean_N_m2square':49*r**(-a-b)}
        out=chord(make(rlo),make(rhi),rlo,rhi)
        assert abs(out['minus_log_density_chord']-a)<1e-13
        assert abs(out['minus_log_product_chord']-(a+b))<1e-13
        exact=-98*(rhi**(-a-b)-rlo**(-a-b))/(math.log(rhi/rlo)*(rlo**(-a)+rhi**(-a)))
        assert abs(out['p_proxy_kms2']-exact)<1e-11
        rows.append({'density_exponent':a,'variance_exponent':b,**out})
    assert (1000/1000)**2 == 1 and (1000)**2 != 1
    assert abs(projection(0,135).T@projection(0,135)-np.eye(2)).max()<1e-14
    return rows

def main():
    ap=argparse.ArgumentParser();ap.add_argument('--data-dir',type=Path,required=True)
    ap.add_argument('--out',type=Path,required=True);args=ap.parse_args()
    manifest=json.loads((HERE/'evidence_v1/DOWNLOADS.json').read_text())
    expected={Path(x['path']).name:x['sha256'] for x in manifest}
    maps={}; headers={}; units={}; identities={}; warning_text=[]
    with warnings.catch_warnings(record=True) as caught:
        warnings.simplefilter('always')
        for mode in ['nat','rob']:
            maps[mode]={};headers[mode]={}
            for product in ['Mom0CD','Mom0','Mom1','Mom2']:
                f=args.data_dir/f'VLA-ANGST_HI_DDO125-{mode}-{product}.fits.gz'
                assert sha(f)==expected[f.name], f
                identities[f.name]=sha(f)
                with fits.open(f) as hd:
                    h=hd[0].header.copy();x=np.squeeze(hd[0].data).astype(float)
                assert x.shape==(1024,1024)
                wanted='CM^-2' if product=='Mom0CD' else ('JY/B*M/S' if product=='Mom0' else 'METR/SEC')
                assert h['BUNIT'].strip()==wanted, (f,h['BUNIT'])
                if product!='Mom0CD':x=x/1000
                maps[mode][product]=x;headers[mode][product]=h;units[f.name]={'raw':wanted,'scale':1 if product=='Mom0CD' else .001}
        ref=WCS(headers['nat']['Mom0CD'],naxis=2)
        y,x=np.indices((1024,1024));ra,dec=ref.all_pix2world(x,y,0)
        points=np.array([[0.,0.],[511.,512.],[1023.,1023.],[421.5,619.5],[700.,200.]])
        sky=ref.all_pix2world(points,0)
        roundtrip_error=float(np.max(abs(ref.all_world2pix(sky,0)-points)))
        assert roundtrip_error<1e-7
        wcs_errors=[]
        for mode in maps:
            for product in maps[mode]:
                wr=WCS(headers[mode][product],naxis=2)
                err=float(np.max(abs(wr.all_pix2world(points,0)-sky)))
                assert err<1e-10
                wcs_errors.append({'mode':mode,'product':product,'max_deg_difference':err})
        warning_text=sorted(set(str(w.message) for w in caught))
    metadata=[];conversions=[];geometries=[];chords=[]
    for mode in maps:
        m=maps[mode];density=m['Mom0CD'];m2=m['Mom2']
        bv=beam(headers[mode]['Mom2'])
        for product in m:
            assert np.max(abs(beam(headers[mode][product])-bv))<1e-12
            a=m[product];valid=np.isfinite(a)
            metadata.append({'mode':mode,'product':product,'finite':int(valid.sum()),
                             'negative':int((valid&(a<0)).sum()),'zero':int((valid&(a==0)).sum()),
                             'finite_quantiles':np.quantile(a[valid],[0,.01,.5,.99,1]).tolist()})
        mask=np.isfinite(density)&np.isfinite(m['Mom0'])&(m['Mom0']>0)&(density>0)
        ratios=density[mask]/m['Mom0'][mask]
        ratio=float(np.median(ratios));scatter=float(np.max(abs(ratios/ratio-1)))
        assert scatter<3e-6
        approximate_conversion=1.823e18*1.222e6/((headers[mode]['Mom2']['RESTFREQ']/1e9)**2*bv[0]*bv[1])
        assert abs(ratio/approximate_conversion-1)<.02
        conversions.append({'mode':mode,'paired_pixels':int(mask.sum()),'column_per_Jy_beam_kms':ratio,
                            'max_relative_nonconstancy':scatter,'approximate_atomic_beam_conversion':approximate_conversion})
        valid_N=np.isfinite(density)&(density>=0)
        paired=valid_N&(density>0)&np.isfinite(m2)&(m2>=0)
        for label,center in CENTERS.items():
            east,north=tangent(ra,dec,center)
            for inc in INCLINATIONS:
                for pa in POSITION_ANGLES:
                    T=projection(inc,pa)
                    radius=np.hypot(T[0,0]*east+T[0,1]*north,T[1,0]*east+T[1,1]*north)
                    radii=sorted({R0,*[R0+s*w/2 for w in WIDTHS for s in [-1,1]]})
                    annuli=[]
                    for r in radii:
                        ann=abs(radius-r)<ANNULUS_WIDTH/2;n=int(ann.sum());sn=ann&valid_N;sp=ann&paired
                        nN=int(sn.sum());npair=int(sp.sum());assert n>0 and nN>0 and npair>0
                        S=float(np.mean(density[sp]));Q=float(np.mean(density[sp]*m2[sp]**2))
                        annuli.append({'radius_kpc':r,'full_width_kpc':ANNULUS_WIDTH,'pixels':n,'valid_N_pixels':nN,
                            'paired_pixels':npair,'valid_N_coverage':nN/n,'paired_coverage':npair/n,
                            'negative_N_pixels':int((ann&np.isfinite(density)&(density<0)).sum()),
                            'missing_N_pixels':int((ann&~np.isfinite(density)).sum()),
                            'missing_m2_pixels':int((ann&~np.isfinite(m2)).sum()),
                            'negative_m2_pixels':int((ann&np.isfinite(m2)&(m2<0)).sum()),
                            'zero_m2_paired_pixels':int((sp&(m2==0)).sum()),
                            'area_mean_N_cm2':float(np.mean(density[sn])),
                            'paired_mean_N_cm2':S,'paired_mean_N_m2square':Q,
                            'column_weighted_m2_rms_kms':math.sqrt(Q/S)})
                    beaminfo=projected_beam(bv,inc,pa)
                    key={'mode':mode,'center':label,'inclination_deg':inc,'PA_deg':pa}
                    geometries.append({**key,'center_radec_deg':list(center),'beam':beaminfo,'annuli':annuli})
                    for width in WIDTHS:
                        lo=min(annuli,key=lambda v:abs(v['radius_kpc']-(R0-width/2)))
                        hi=min(annuli,key=lambda v:abs(v['radius_kpc']-(R0+width/2)))
                        out=chord(lo,hi,lo['radius_kpc'],hi['radius_kpc'])
                        chords.append({**key,'endpoint_spacing_kpc':width,'lo':lo,'hi':hi,**out,
                                       'beam_max_disk_fwhm_kpc':beaminfo['disk_principal_fwhm_kpc'][1]})
    assert len(geometries)==48 and len(chords)==144
    synthetic=controls()
    inputs={str(f.relative_to(HERE)):sha(f) for f in [Path(__file__),HERE/'PROTOCOL.md',HERE/'SOURCE_LEDGER.md',HERE/'METADATA_RESOLUTION.md',HERE/'evidence_v1/DOWNLOADS.json']}
    result={'status':'descriptive exposed moment-product diagnostics, conditional physical interpretation',
            'environment':{'python':sys.version,'astropy':astropy.__version__,'numpy':np.__version__},
            'input_identities':inputs,'fits_identities':identities,'unit_conversions':units,'warnings':warning_text,
            'metadata':metadata,'column_conversion_controls':conversions,'wcs_roundtrip_error_pixels':roundtrip_error,
            'wcs_pair_checks':wcs_errors,'synthetic_controls':synthetic,'geometries':geometries,'chords':chords,
            'checks':{'input_hashes_units_shape':True,'WCS_roundtrip_common_projection':True,'beam_history_consistency':True,
                      'column_Mom0_conversion':True,'synthetic_constant_power_law_and_units':True,'all_frozen_geometries_reported':True},
            'limits':'No intrinsic sigma_R, pressure measurement, confidence interval, independent pixel samples, deconvolution, holdout success or galaxy exclusion.'}
    with args.out.open('x') as f:json.dump(result,f,indent=2);f.write('\n')
    for mode in ['nat','rob']:
        for width in WIDTHS:
            rows=[v for v in chords if v['mode']==mode and v['endpoint_spacing_kpc']==width]
            print(mode,width,'p_proxy range',min(v['p_proxy_kms2'] for v in rows),max(v['p_proxy_kms2'] for v in rows),
                  'min paired coverage',min(min(v['lo']['paired_coverage'],v['hi']['paired_coverage']) for v in rows))
    print('PASS six metadata/numerical families;144 chords,48 geometry cases; no physical acceptance test.')

if __name__=='__main__':main()
