#!/usr/bin/env python3
"""Independent, bounded replay of the published DDO125 map diagnostics.

No author runner is imported or executed. Astropy is used only for FITS I/O.
The celestial map is reconstructed as orthographic SIN unit vectors; profiles
use direct cell selection and math.fsum. Beam eigenvalues use a scalar quadratic.
The complete frozen JSON is compared, including every repeated endpoint record.
"""
from pathlib import Path
from datetime import datetime, timezone
from html.parser import HTMLParser
import hashlib
import json
import math
import platform
import re
import warnings
import numpy as np
import astropy
from astropy.io import fits

OUT = Path(__file__).resolve().parent
SNAP = OUT/'source_snapshot'
FITS = SNAP/'fits'
LD = np.longdouble
PI = LD('3.1415926535897932384626433832795028841971693993751')
RAD = PI/180
D = LD(2590)
R0 = LD('.94')
ANN_HALF = LD('.045')
INCS = [60,63,66]
PAS = [118,120,135,150]
WIDTHS = [LD('.18'),LD('.36'),LD('.54')]
CENTERS = {'catalog': ((LD(12)+LD(27)/60+LD('41.8')/3600)*15,LD(43)+LD(29)/60+LD(38)/3600),
           'pointing':((LD(12)+LD(27)/60+LD('40.9')/3600)*15,LD(43)+LD(29)/60+LD(44)/3600)}


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def quantiles(values,qs=(0,.01,.5,.99,1)):
    a=np.sort(values)
    result=[]
    for q in qs:
        z=(len(a)-1)*q;j=int(z);t=z-j
        result.append(float(a[j]) if t==0 else (1-t)*float(a[j])+t*float(a[j+1]))
    return result


def basis(ra,dec):
    a,d=LD(ra)*RAD,LD(dec)*RAD
    radial=np.array([np.cos(d)*np.cos(a),np.cos(d)*np.sin(a),np.sin(d)],dtype=LD)
    east=np.array([-np.sin(a),np.cos(a),0],dtype=LD)
    north=np.array([-np.sin(d)*np.cos(a),-np.sin(d)*np.sin(a),np.cos(d)],dtype=LD)
    return radial,east,north


def beam_from_history(h):
    values=[]
    for line in h.get('HISTORY',[]):
        if 'CLEAN BMAJ=' in line:
            fields=line.replace('=',' ').split()
            values.append(tuple(float(fields[fields.index(key)+1]) for key in ['BMAJ','BMIN','BPA']))
    assert len(values)==1
    a,b,p=values[0]
    assert a>=b>0
    return a*3600,b*3600,p


def beam_quadratic(a,b,beam_pa,inc,disk_pa):
    c=math.cos(math.radians(beam_pa-disk_pa))
    s=math.sin(math.radians(beam_pa-disk_pa))
    q=math.cos(math.radians(inc))
    f11=a*a*c*c+b*b*s*s
    f12=(a*a-b*b)*c*s/q
    f22=(a*a*s*s+b*b*c*c)/(q*q)
    trace=f11+f22
    discriminant=math.hypot(f11-f22,2*f12)
    eigen=[(trace-discriminant)/2,(trace+discriminant)/2]
    scale=2590*math.pi/(180*3600)
    widths=[scale*math.sqrt(e) for e in eigen]
    covscale=scale*scale/(8*math.log(2))
    covariance=[[covscale*f11,covscale*f12],[covscale*f12,covscale*f22]]
    det_expected=a*a*b*b/(q*q)
    assert abs((f11*f22-f12*f12)/det_expected-1)<3e-15
    return covariance,widths


manifest=json.loads((SNAP/'evidence_v1/DOWNLOADS.json').read_text())
frozen=json.loads((SNAP/'evidence_v1/PROTOCOL_FREEZE.json').read_text())
assert frozen['protocol_sha256']==sha(SNAP/'PROTOCOL.md')
assert frozen['source_ledger_sha256']==sha(SNAP/'SOURCE_LEDGER.md')
pins=json.loads((SNAP/'evidence_v1/SOURCE_PINS.json').read_text())
for entry in pins['sources']:
    assert sha(SNAP/'official_sources'/Path(entry['path']).name)==entry['sha256']

# Match every FITS filename to the actual DDO125 archive row, rather than merely
# trusting the hand-copied links JSON.
class Links(HTMLParser):
    def __init__(self):
        super().__init__();self.current=None;self.rows=[]
    def handle_starttag(self,tag,attrs):
        if tag=='tr':self.current={'text':[],'urls':[]}
        if tag=='a' and self.current is not None:
            for k,v in attrs:
                if k=='href':self.current['urls'].append(v)
    def handle_data(self,data):
        if self.current is not None:self.current['text'].append(data)
    def handle_endtag(self,tag):
        if tag=='tr' and self.current is not None:
            self.rows.append(self.current);self.current=None
lp=Links();lp.feed((SNAP/'official_sources/data_products.html').read_text())
archive_rows=[r for r in lp.rows if ''.join(''.join(r['text']).split())=='DDO125nanaronaronaronaronaro']
if not archive_rows:
    archive_rows=[r for r in lp.rows if re.match(r'^DDO\s*125\b',' '.join(' '.join(r['text']).split()))]
assert len(archive_rows)==1
official_urls=set(archive_rows[0]['urls'])
for row in manifest:
    f=FITS/Path(row['path']).name
    assert row['original_url'] in official_urls
    assert row['retrieval_url']==row['original_url'].replace('http:','https:',1)
    assert row['exit']==0 and f.stat().st_size==row['bytes'] and sha(f)==row['sha256']

metadata_receipt=json.loads((SNAP/'evidence_v1/FITS_METADATA.json').read_text())
meta_by_name={r['file']:r for r in metadata_receipt['rows']}
maps={};headers={};beam_values={};whole=[];header_evidence=[];warnings_seen=[]
spatial_keys=['NAXIS1','NAXIS2','CTYPE1','CTYPE2','CRPIX1','CRPIX2','CRVAL1','CRVAL2','CDELT1','CDELT2']
spatial_ref=None
for mode in ['nat','rob']:
    maps[mode]={};headers[mode]={}
    for product in ['Mom0CD','Mom0','Mom1','Mom2']:
        path=FITS/f'VLA-ANGST_HI_DDO125-{mode}-{product}.fits.gz'
        with warnings.catch_warnings(record=True) as caught:
            warnings.simplefilter('always')
            with fits.open(path) as hdul:
                h=hdul[0].header.copy();raw=np.squeeze(hdul[0].data).copy()
        warnings_seen.extend(str(w.message) for w in caught)
        assert h['OBJECT'].strip()=='DDO125' and h['BITPIX']==-32
        assert h['NAXIS']==4 and h['NAXIS3']==h['NAXIS4']==1
        assert raw.shape==(1024,1024) and h.get('BSCALE',1)==1 and h.get('BZERO',0)==0
        wanted={'Mom0CD':'CM^-2','Mom0':'JY/B*M/S','Mom1':'METR/SEC','Mom2':'METR/SEC'}[product]
        assert h['BUNIT'].strip()==wanted
        assert h['CTYPE1']=='RA---SIN' and h['CTYPE2']=='DEC--SIN'
        assert h.get('CROTA1',0)==h.get('CROTA2',0)==0
        assert all(not k.startswith(('CD1_','CD2_','PC1_','PC2_','PV1_','PV2_')) for k in h)
        assert h.get('EQUINOX',h.get('EPOCH'))==2000
        assert not any(k in h for k in ['BMAJ','BMIN','BPA'])
        spatial={k:h[k] for k in spatial_keys}
        if spatial_ref is None:spatial_ref=spatial
        assert spatial==spatial_ref
        meta=meta_by_name[path.name]
        assert meta['sha256']==sha(path) and meta['shape']==list(raw.shape)
        assert meta['dtype']==str(raw.dtype)
        assert meta['header_string']==h.tostring(sep='\n')
        a=raw.astype(np.float64)
        if product!='Mom0CD':a=a*0.001
        maps[mode][product]=a;headers[mode][product]=h
        valid=np.isfinite(a)
        finite=int(valid.sum());negative=int((valid&(a<0)).sum())
        assert finite==meta['finite_pixels'] and negative==meta['negative_finite_pixels']
        whole.append(dict(mode=mode,product=product,finite=finite,negative=negative,zero=int((valid&(a==0)).sum()),finite_quantiles=quantiles(a[valid])))
        b=beam_from_history(h)
        if mode in beam_values:assert b==beam_values[mode]
        else:beam_values[mode]=b
        header_evidence.append(dict(filename=path.name,sha256=sha(path),header_sha256=hashlib.sha256(h.tostring().encode()).hexdigest(),BUNIT=wanted,raw_shape=list(raw.shape),raw_dtype=str(raw.dtype),spatial=spatial,epoch=2000,BLANK=h.get('BLANK'),beam_arcsec_pa=list(b),finite=finite,negative=negative,nan=int(np.isnan(a).sum()),positive_infinity=int(np.isposinf(a).sum()),negative_infinity=int(np.isneginf(a).sum())))

# Standard orthographic/SIN mapping. Since the files have zero rotation, no
# PV slant terms, and identical spatial cards, these equations close the WCS.
y,x=np.indices((1024,1024),dtype=np.int32)
h=headers['nat']['Mom0CD']
xi=(x.astype(LD)+1-LD(str(h['CRPIX1'])))*LD(str(h['CDELT1']))*RAD
eta=(y.astype(LD)+1-LD(str(h['CRPIX2'])))*LD(str(h['CDELT2']))*RAD
z=np.sqrt(1-xi*xi-eta*eta)
n0,e0,t0=basis(str(h['CRVAL1']),str(h['CRVAL2']))
ray=[xi*e0[j]+eta*t0[j]+z*n0[j] for j in range(3)]
norm_error=float(np.max(np.abs(sum(a*a for a in ray)-1)))
back_xi=sum(ray[j]*e0[j] for j in range(3))
back_eta=sum(ray[j]*t0[j] for j in range(3))
roundtrip=max(float(np.max(np.abs(back_xi/(LD(str(h['CDELT1']))*RAD)+LD(str(h['CRPIX1']))-1-x))),float(np.max(np.abs(back_eta/(LD(str(h['CDELT2']))*RAD)+LD(str(h['CRPIX2']))-1-y))))
assert norm_error<2e-14 and roundtrip<1e-8

geometry=[];chords=[];minimum_boundary=1.;sum_cells=0
sky_jacobian_max=0.;disk_jacobian_min=math.inf;disk_jacobian_max=0.
offsets={}
for label,(ra,dec) in CENTERS.items():
    nc,ec,tc=basis(ra,dec)
    denominator=sum(ray[j]*nc[j] for j in range(3))
    east=D*sum(ray[j]*ec[j] for j in range(3))/denominator
    north=D*sum(ray[j]*tc[j] for j in range(3))/denominator
    offsets[label]=[float(east[512,511]),float(north[512,511])]
    for inc in INCS:
        cosi=np.cos(LD(inc)*RAD)
        for pa in PAS:
            theta=LD(pa)*RAD
            major=east*np.sin(theta)+north*np.cos(theta)
            minor=(east*np.cos(theta)-north*np.sin(theta))/cosi
            radii=np.sqrt(major*major+minor*minor)
            target_radii=[R0+LD(j)*LD('.09') for j in range(-3,4)]
            selections={}
            for rr in target_radii:
                gap=np.abs(np.abs(radii-rr)-ANN_HALF)
                minimum_boundary=min(minimum_boundary,float(np.min(gap)))
                ann=np.abs(radii-rr)<ANN_HALF
                ids=np.flatnonzero(ann)
                selections[float(rr)]=ids
                # Mean values use equal SIN-grid cells, as declared by the
                # diagnostic; these bounds document the small area Jacobian.
                sky_jacobian_max=max(sky_jacobian_max,float(np.max(1/z.ravel()[ids]-1)))
                disk_weight=1/(z.ravel()[ids]*denominator.ravel()[ids]**3)
                disk_jacobian_min=min(disk_jacobian_min,float(np.min(disk_weight)))
                disk_jacobian_max=max(disk_jacobian_max,float(np.max(disk_weight)))
            for mode in ['nat','rob']:
                nh=maps[mode]['Mom0CD'].ravel();lw=maps[mode]['Mom2'].ravel()
                annuli=[]
                for rr,ids in selections.items():
                    aa=nh[ids];ww=lw[ids]
                    finite_n=np.isfinite(aa);finite_w=np.isfinite(ww)
                    nvalid=finite_n&(aa>=0)
                    pair=finite_n&(aa>0)&finite_w&(ww>=0)
                    count=len(ids);nn=int(nvalid.sum());npair=int(pair.sum())
                    s=math.fsum(float(v) for v in aa[pair])/npair
                    q=math.fsum(float(v)*float(w)*float(w) for v,w in zip(aa[pair],ww[pair]))/npair
                    sum_cells+=npair
                    annuli.append(dict(radius_kpc=rr,full_width_kpc=.09,pixels=count,valid_N_pixels=nn,paired_pixels=npair,valid_N_coverage=nn/count,paired_coverage=npair/count,negative_N_pixels=int((finite_n&(aa<0)).sum()),missing_N_pixels=int((~finite_n).sum()),missing_m2_pixels=int((~finite_w).sum()),negative_m2_pixels=int((finite_w&(ww<0)).sum()),zero_m2_paired_pixels=int((pair&(ww==0)).sum()),area_mean_N_cm2=math.fsum(float(v) for v in aa[nvalid])/nn,paired_mean_N_cm2=s,paired_mean_N_m2square=q,column_weighted_m2_rms_kms=math.sqrt(q/s)))
                bv=beam_values[mode]
                cov,bw=beam_quadratic(*bv,inc,pa)
                key=dict(mode=mode,center=label,inclination_deg=inc,PA_deg=pa)
                geometry.append({**key,'center_radec_deg':[float(ra),float(dec)],'beam':dict(sky_fwhm_arcsec=list(bv),disk_covariance_kpc2=cov,disk_principal_fwhm_kpc=bw),'annuli':annuli})
                for width in WIDTHS:
                    lo=annuli[3-int(round(float(width/LD('.18'))))]
                    hi=annuli[3+int(round(float(width/LD('.18'))))]
                    dl=math.log(float((R0+width/2)/(R0-width/2)))
                    s0,s1=lo['paired_mean_N_cm2'],hi['paired_mean_N_cm2']
                    q0,q1=lo['paired_mean_N_m2square'],hi['paired_mean_N_m2square']
                    sr,qr=s1/s0,q1/q0
                    chords.append({**key,'endpoint_spacing_kpc':float(width),'lo':lo,'hi':hi,'minus_log_density_chord':-math.log(sr)/dl,'minus_log_product_chord':-math.log(qr)/dl,'p_proxy_kms2':2*(q0-q1)/((s0+s1)*dl),'density_ratio':sr,'product_ratio':qr,'beam_max_disk_fwhm_kpc':bw[1]})

# The N_HI input is an observational conversion. Only its file consistency and
# optically-thin/Gaussian-beam numerical normalization are checked here.
conversions=[]
for mode in ['nat','rob']:
    nh=maps[mode]['Mom0CD'];m0=maps[mode]['Mom0']
    valid=np.isfinite(nh)&np.isfinite(m0)&(nh>0)&(m0>0)
    ratio=nh[valid]/m0[valid]
    median=quantiles(ratio,(.5,))[0]
    scatter=float(np.max(np.abs(ratio/median-1)))
    a,b,_=beam_values[mode];freq=headers[mode]['Mom2']['RESTFREQ']
    omega=math.pi*(a*math.pi/(180*3600))*(b*math.pi/(180*3600))/(4*math.log(2))
    kelvin_per_jy=1e-26*299792458**2/(2*1.380649e-23*freq**2*omega)
    exact_si_conversion=1.823e18*kelvin_per_jy
    rounded=1.823e18*1.222e6/((freq/1e9)**2*a*b)
    conversions.append(dict(mode=mode,paired_pixels=int(valid.sum()),column_per_Jy_beam_kms=median,max_relative_nonconstancy=scatter,approximate_atomic_beam_conversion=rounded,SI_Gaussian_conversion=exact_si_conversion,relative_to_SI_conversion=median/exact_si_conversion-1,relative_to_author_rounded_conversion=median/rounded-1))

# Analytic controls use the closed hyperbolic expression at logarithmically
# symmetric endpoints. The endpoints need not be symmetric in linear radius.
control_results=[]
rl,rh=.76,1.12
middle=math.sqrt(rl*rh);half=.5*math.log(rh/rl)
for a,b in [(0.,0.),(2.,0.),(1.2,.7),(-.5,1.5),(3.,-1.)]:
    exact=49*middle**(-b)*math.sinh((a+b)*half)/(half*math.cosh(a*half))
    s0,s1=rl**(-a),rh**(-a);q0,q1=49*rl**(-a-b),49*rh**(-a-b)
    measured=2*(q0-q1)/((s0+s1)*math.log(rh/rl))
    assert abs(exact-measured)<1e-12
    control_results.append(dict(density_exponent=a,variance_exponent=b,p_proxy_closed_form=exact,minus_log_density_chord=-math.log(s1/s0)/math.log(rh/rl),minus_log_product_chord=-math.log(q1/q0)/math.log(rh/rl),p_proxy_kms2=measured,density_ratio=s1/s0,product_ratio=q1/q0))
for pa in [0,45,90,135]:
    _,bw=beam_quadratic(12,8,-31,0,pa)
    scale=2590*math.pi/(180*3600)
    assert max(abs(bw[0]-8*scale),abs(bw[1]-12*scale))<1e-15
    _,bw=beam_quadratic(10,10,-31,60,pa)
    assert max(abs(bw[0]-10*scale),abs(bw[1]-20*scale))<1e-15
assert (8000*.001)**2==64

# Compare complete frozen output after all independent calculations. Endpoints
# repeated under chord records are also compared, not treated as trusted copies.
author=json.loads((SNAP/'evidence_v1/RESULTS.json').read_text())
for rel,h in author['input_identities'].items():assert sha(SNAP/rel)==h
for name,h in author['fits_identities'].items():assert sha(FITS/name)==h
for name,units in author['unit_conversions'].items():
    product=name.split('-')[-1].split('.')[0]
    assert units=={'raw':{'Mom0CD':'CM^-2','Mom0':'JY/B*M/S','Mom1':'METR/SEC','Mom2':'METR/SEC'}[product],'scale':1 if product=='Mom0CD' else .001}
assert set(author['warnings'])==set(warnings_seen)
differences={};mismatches=[];compared=0


def compare(expected,actual,path):
    global compared
    if isinstance(expected,dict):
        if set(expected)!=set(actual):mismatches.append(dict(path=path,key_set=[sorted(expected),sorted(actual)]));return
        for k in expected:compare(expected[k],actual[k],path+'/'+k)
    elif isinstance(expected,list):
        if len(expected)!=len(actual):mismatches.append(dict(path=path,length=[len(expected),len(actual)]));return
        for i,(x,y) in enumerate(zip(expected,actual)):compare(x,y,path+f'/{i}')
    elif isinstance(expected,(float,int)) and not isinstance(expected,bool):
        compared+=1;delta=abs(expected-actual);relative=delta/max(abs(expected),abs(actual),1e-300)
        leaf=next(part for part in reversed(path.split('/')) if not part.isdigit())
        row=differences.setdefault(leaf,dict(max_abs=0.,max_rel=0.,path_at_max_abs=path))
        if delta>row['max_abs']:row.update(max_abs=delta,path_at_max_abs=path)
        row['max_rel']=max(row['max_rel'],relative)
        if isinstance(expected,int):ok=expected==actual
        else:ok=delta<=1e-10+2e-12*max(abs(expected),abs(actual))
        if not ok:mismatches.append(dict(path=path,expected=expected,actual=actual,absolute=delta,relative=relative))
    elif expected!=actual:mismatches.append(dict(path=path,expected=expected,actual=actual))


gkey=lambda g:(g['mode'],g['center'],g['inclination_deg'],g['PA_deg'])
ckey=lambda c:(*gkey(c),c['endpoint_spacing_kpc'])
geometry.sort(key=gkey);chords.sort(key=ckey)
assert len(geometry)==len(author['geometries'])==48
assert len(chords)==len(author['chords'])==144
compare(sorted(author['geometries'],key=gkey),geometry,'geometries')
compare(sorted(author['chords'],key=ckey),chords,'chords')
compare(author['metadata'],whole,'metadata')
compare(author['column_conversion_controls'],[{k:r[k] for k in author['column_conversion_controls'][0]} for r in conversions],'column_conversion_controls')
compare(author['synthetic_controls'],[{k:r[k] for k in author['synthetic_controls'][0]} for r in control_results],'synthetic_controls')
for row in author['wcs_pair_checks']:
    assert row['max_deg_difference']==0
assert all(author['checks'].values())
summary=[]
for mode in ['nat','rob']:
    for w in WIDTHS:
        selected=[c for c in chords if c['mode']==mode and c['endpoint_spacing_kpc']==float(w)]
        summary.append(dict(mode=mode,spacing=float(w),n=len(selected),p_range=[min(c['p_proxy_kms2'] for c in selected),max(c['p_proxy_kms2'] for c in selected)],minimum_paired_coverage=min(min(c['lo']['paired_coverage'],c['hi']['paired_coverage']) for c in selected)))
beam_summary={m:[min(g['beam']['disk_principal_fwhm_kpc'][1] for g in geometry if g['mode']==m),max(g['beam']['disk_principal_fwhm_kpc'][1] for g in geometry if g['mode']==m)] for m in ['nat','rob']}
central_widths={m:[min(g['annuli'][3]['column_weighted_m2_rms_kms'] for g in geometry if g['mode']==m),max(g['annuli'][3]['column_weighted_m2_rms_kms'] for g in geometry if g['mode']==m)] for m in ['nat','rob']}
result=dict(schema='independent_hi_moment_check_v2',at=datetime.now(timezone.utc).isoformat(),status='PASS' if not mismatches else 'FAIL_PRESERVED',independent_check_sha256=sha(Path(__file__)),software=dict(python=platform.python_version(),numpy=np.__version__,astropy=astropy.__version__),source_result_sha256=sha(SNAP/'evidence_v1/RESULTS.json'),header_evidence=header_evidence,warnings=sorted(set(warnings_seen)),geometry_method='Direct SIN unit vector, local gnomonic dot products, long-double radii; no astropy.wcs call',roundtrip_pixels=roundtrip,unit_ray_norm_error=norm_error,reference_pixel_offsets_kpc=offsets,minimum_annulus_boundary_margin_kpc=minimum_boundary,pixel_sums_compensated_entries=sum_cells,annuli=336,geometry_cases=48,chords_count=144,compared_numeric_leaves=compared,differences=differences,mismatches=mismatches,summary=summary,beam_max_fwhm_ranges_kpc=beam_summary,central_weighted_rms_ranges_kms=central_widths,area_convention=dict(equal_SIN_grid_cell_means=True,max_solid_angle_jacobian_relative_to_origin=sky_jacobian_max,disk_area_jacobian_range_relative_to_common_constant=[disk_jacobian_min,disk_jacobian_max]),column_conversion_controls=conversions,independent_closed_form_controls=control_results,metadata=whole,geometries=geometry,chords=chords,limits='Development descriptive products; no pressure inference, deconvolution, fit, significance, holdout, corrected source model, formal audit or landing.')
with (OUT/'CHECK_RESULTS_v2.json').open('x') as f:json.dump(result,f,indent=2,allow_nan=False);f.write('\n')
print(json.dumps({k:result[k] for k in ['status','roundtrip_pixels','unit_ray_norm_error','minimum_annulus_boundary_margin_kpc','compared_numeric_leaves','differences','mismatches','summary','beam_max_fwhm_ranges_kpc','central_weighted_rms_ranges_kms','area_convention']},indent=2))
if mismatches:raise SystemExit(1)
