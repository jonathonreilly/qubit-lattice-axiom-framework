#!/usr/bin/env python3
"""Independent receipt, score, primal and rational-certificate checks.

Does not import author modules, optimize fitted weights or solve fields.
Reconstructs galaxy LP rows from the preserved processed NPZ arrays and K.
"""
import os
for key in ('OPENBLAS_NUM_THREADS', 'OMP_NUM_THREADS', 'MKL_NUM_THREADS',
            'VECLIB_MAXIMUM_THREADS', 'NUMEXPR_NUM_THREADS'):
    os.environ[key] = '1'
import datetime as dt
from fractions import Fraction as F
import hashlib
import json
import math
from pathlib import Path
import resource
import time
import numpy as np
import mpmath as mp

HERE = Path(__file__).resolve().parent
RT = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012')
mp.mp.dps = 70

def read(p): return json.loads(Path(p).read_text())
def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for block in iter(lambda: f.read(1048576), b''): h.update(block)
    return h.hexdigest()
def dump(name, value):
    p = HERE / name
    assert not p.exists(), p
    p.write_text(json.dumps(value, indent=2) + '\n')
def guard():
    clock = read(RT/'DEADLINE.json')
    assert time.time() < clock['packaging_epoch']
    assert not any((RT/x).exists() for x in ('STOP_REQUESTED.json', 'USER_STOP_REQUESTED.json',
                  'STOP_REQUESTED', 'USER_STOP_REQUESTED', 'STOP_CAMPAIGN.json'))
def mf(v):
    f = v if isinstance(v, F) else F(float(v))
    return mp.mpf(f.numerator)/f.denominator
def ratio(f): return [str(f.numerator), str(f.denominator)]
def exact_dot(a,b): return sum((F(float(x))*F(float(y)) for x,y in zip(a,b)), F(0))
def frac(v): return F(int(v[0]),int(v[1]))

def main():
    start = time.monotonic(); guard()
    manifest = read(HERE/'snapshot_manifest_v1.json')
    entries = {x['key']:x for x in manifest['files']}
    cert_manifest = read(HERE/'certificate_snapshot_manifest_v1.json')
    cent = {x['key']:x for x in cert_manifest['files']}
    def path(key):
        e=entries.get(key,cent.get(key))
        return HERE/e['snapshot'] if e['snapshot'] else Path(e['source'])
    def doc(key): return read(path(key))
    for e in list(entries.values()) + list(cent.values()):
        assert sha(Path(e['source'])) == e['sha256'], e['key']
        if e['snapshot']: assert sha(HERE/e['snapshot']) == e['sha256'], e['key']
    freeze,candidates,official = [doc(x) for x in ('FREEZE','CANDIDATES','RESULTS')]
    fzh,canh = entries['FREEZE']['sha256'],entries['CANDIDATES']['sha256']
    names = freeze['names']; cases = candidates['cases']; labels = [c['name'] for c in cases]
    assert names == ['NGC2976','UGC07577','KK98-251','NGC3949','NGC3972','UGC06667','UGC08837','DDO064','DDO168']
    assert labels == [f'{family}_{suffix}' for family in ['M','D'] for suffix in
                      ['galaxies_only','galaxies_external','galaxies_external_solar']]
    assert candidates['freeze_sha256'] == official['freeze_sha256'] == fzh
    assert official['candidates_sha256'] == canh
    assert candidates['all_observations_are_fit_inputs'] and freeze['all_nine_are_calibration_data']
    assert not candidates['continuous_external_optimality_claimed']
    for key,expected in freeze['identities'].items(): assert entries[key]['sha256'] == expected,key
    solver_hash=entries['field_solver']['sha256']; source_hash=entries['source_data']['sha256']
    controls=doc('controls'); assert controls['passed']
    assert controls['source_sha256']==entries['operator']['sha256']
    for c in controls['checks']: assert c['relative_error']<=c['limit']
    sources={}; lineage=[]; geometry_checks=[]
    with np.load(path('source_data')) as raw,np.load(path('target_data')) as target:
        for name in names:
            mask=np.asarray(raw[name+'_score_mask']); allr=raw[name+'_R']
            r=allr[mask]; v=target[name+'_v'][mask]; e=target[name+'_error'][mask]
            assert mask.dtype==bool and np.all(np.isfinite(r)&(r>0))
            assert np.all(np.isfinite(v)&(v>0)&np.isfinite(e)&(e>=0))
            ok=('old_operator_' if name in names[:3] else 'new_operator_')+name
            op=doc(ok); source=doc('source_receipt_'+name); field=doc('fields_'+name)
            assert candidates['operators'][name]==entries[ok]['sha256']
            assert official['field_receipts'][name]==entries['fields_'+name]['sha256']
            assert field['freeze_sha256']==fzh and field['candidates_sha256']==canh
            assert set(field['candidates'])==set(labels)
            assert np.array_equal(r,op['R_kpc']) and np.array_equal(r,field['R_kpc'])
            assert op['source_sha256']==entries['operator']['sha256']
            assert op['solver_sha256']==solver_hash and op['protocol_sha256']==entries['old_protocol']['sha256']
            assert source['source_sha256']==solver_hash and source['source_npz_sha256']==source_hash
            assert op['identity']['source_receipt_sha256']==entries['source_receipt_'+name]['sha256']
            assert op['identity']['source_npz_sha256']==source_hash
            assert source['U']==op['identity']['U']==0.5605122519882025
            assert not op['observed_velocities_read']
            if name in names[3:]:
                assert op['freeze_sha256']==fzh and op['new_protocol_sha256']==entries['protocol']['sha256']
                assert freeze['at']<op['at']<candidates['at']
            assert candidates['at']<field['at']<=official['at']
            for key,limit in [('newtonian_projection_relative',.003),('prior_full_response_relative',1e-10),
                              ('synthetic_superposition_relative',1e-11)]:
                assert op['checks'][key]<=limit
            base,refined,edge=[doc(tag+'_metadata_'+name) for tag in ['base','refined','boundary_extension']]
            for tag,meta in [('base',base),('refined',refined),('boundary_extension',edge)]:
                assert meta['cache_sha256']==entries[tag+'_geometry_'+name]['sha256']
            assert base['identity']==op['identity']
            bi,fi=base['identity'],refined['identity']
            assert {k:v for k,v in bi.items() if k!='settings'}=={k:v for k,v in fi.items() if k!='settings'}
            for key in ['nr','nc','lmax']: assert fi['settings'][key]==2*bi['settings'][key]
            for key in ['rmin','rmax','hankel']: assert fi['settings'][key]==bi['settings'][key]
            assert edge['identity']=={'base_cache_sha256':entries['base_geometry_'+name]['sha256'],
              'solver_sha256':solver_hash,'extension_factor':2,'edge_hankel_order':8192}
            with np.load(path('base_geometry_'+name)) as b,np.load(path('refined_geometry_'+name)) as f,\
                 np.load(path('boundary_extension_geometry_'+name)) as z:
                br,fr,zr=b['radius'],f['radius'],z['radius']; offset=edge['nodes_per_extension']
                assert np.array_equal(zr[offset:offset+len(br)],br)
                assert zr[0]==br[0]/2 and zr[-1]==br[-1]*2
                for data in [b,f,z]: assert np.array_equal(data['R'],r)
                assert np.array_equal(b['mr'],op['g_N'])
                for k in ['cosine','angular_weights','mr','mz','R','nc','lmax']:
                    assert np.array_equal(z[k],b[k])
                assert fr[0]==br[0] and fr[-1]==br[-1]
                # Compare one spatial component at a time; no new field computations.
                for key in ['ur','uz']:
                    bb,zz=b[key],z[key]
                    assert np.array_equal(zz[offset:offset+len(br)],bb)
                    del bb,zz
                geometry_checks.append({'name':name,'base_settings':bi['settings'],
                     'refined_settings':fi['settings'],'boundary_nodes_each_side':offset,
                     'all_interior_vectors_identical':True,'all_cache_hashes_match':True})
            sources[name]={'R':r,'v':v,'error':e,'K':np.array(op['K']),'g_N':np.array(op['g_N']),
                 'knots':np.array(op['knots_SI']),'fields':field,'raw_indices':np.flatnonzero(mask)}
            assert sources[name]['K'].shape==(len(r),20)
            assert np.array_equal(sources[name]['knots'],np.power(10.,-13+np.arange(21)/4))
            lineage.append({'name':name,'raw_count':len(allr),'scored_count':len(r),
              'excluded_raw_indices':np.flatnonzero(~mask).tolist(),'R_kpc':r.tolist(),
              'V_obs_km_s':v.tolist(),'error_km_s':e.tolist(),'operator_checks':op['checks']})
    guard()
    score_rows=[]; gates=[]; differences={'velocity':0.,'rms':0.,'t':0.,'gate':0.,'aggregate_rms':0.,'aggregate_t':0.}
    agg={}
    for case in cases:
        key=case['name']; agg[key]={}
        for name in names:
            s=sources[name]; item=s['fields']['candidates'][key]
            vectors={method:part['force'] for method,part in item['methods'].items()}
            positive=all(all(math.isfinite(g) and g>0 for g in arr) for arr in vectors.values())
            assert positive
            changes={method:max(abs(F(g)/F(b)-1) for g,b in zip(vectors[method],vectors['base']))
                     for method in ['refined','boundary']}
            p=changes['refined']<=F(.005) and changes['boundary']<=F(.003)
            assert p==item['passed']
            for m,stored in [('refined','refinement'),('boundary','boundary')]:
                differences['gate']=max(differences['gate'],abs(float(changes[m])-item['relative_changes'][stored]))
            gates.append({'candidate':key,'name':name,'positive_finite_all_three':positive,'passed':p,
              'refinement':float(changes['refined']),'boundary':float(changes['boundary'])})
            for method,gg in vectors.items():
                bins=[]; log_squares=[]
                for i,(r,v,e,g) in enumerate(zip(s['R'],s['v'],s['error'],gg)):
                    r,v,e,g=map(lambda x:F(float(x)),[r,v,e,g])
                    predicted_squared=r*g; q=predicted_squared/v**2
                    low=max(F(0),v-2*e); high=v+2*e
                    t=max(F(0),(predicted_squared-high**2)/v**2,(low**2-predicted_squared)/v**2)
                    log=mp.log10(mf(q))/2; pred=mp.sqrt(mf(predicted_squared)); log_squares.append(log**2)
                    direction='under' if predicted_squared<low**2 else ('over' if predicted_squared>high**2 else 'inside')
                    bins.append({'scored_bin':i,'raw_bin':int(s['raw_indices'][i]),'R_kpc':float(r),
                        'observed_velocity':float(v),'error':float(e),'force':float(g),'velocity':float(pred),
                        'velocity_residual':float(pred-mf(v)),'log10_velocity_residual':float(log),
                        'lower_velocity':float(low),'upper_velocity':float(high),'rectangle_t':float(t),
                        'rectangle_direction':direction})
                result={'candidate':key,'name':name,'method':method,'bins':bins,
                    'rms_log10_velocity':float(mp.sqrt(mp.fsum(log_squares)/len(bins))),
                    'required_rectangle_t':max(b['rectangle_t'] for b in bins),
                    'bins_outside_rectangle':sum(b['rectangle_direction']!='inside' for b in bins)}
                given=item['methods'][method]
                assert result['bins_outside_rectangle']==given['bins_outside_rectangle']
                for a,b in [('rms','rms_log10_velocity'),('t','required_rectangle_t')]:
                    differences[a]=max(differences[a],abs(result[b]-given[b]))
                differences['velocity']=max(differences['velocity'],max(abs(b['velocity']-v) for b,v in zip(bins,given['velocity'])))
                score_rows.append(result)
                agg[key].setdefault(method,[]).append((mp.fsum(log_squares)/len(bins),result))
    aggregates={}
    for key,methods in agg.items():
        numerical=all(x['passed'] for x in gates if x['candidate']==key)
        assert numerical==official['combined'][key]['all_field_gates_pass']
        aggregates[key]={'all_field_gates_pass':numerical,'methods':{}}
        for method,rows in methods.items():
            rs=[x[1] for x in rows]; allbins=[{'source':x['name'],**b} for x in rs for b in x['bins']]
            entry={'equal_galaxy_rms_log10_velocity':float(mp.sqrt(mp.fsum(x[0] for x in rows)/len(rows))),
               'largest_rectangle_t':max(x['required_rectangle_t'] for x in rs),
               'bins_outside_rectangle':sum(x['bins_outside_rectangle'] for x in rs),
               'galaxies_outside_rectangle':sum(x['bins_outside_rectangle']>0 for x in rs),
               'under_bins':sum(b['rectangle_direction']=='under' for b in allbins),
               'over_bins':sum(b['rectangle_direction']=='over' for b in allbins),
               'worst_rectangle_bin':max(allbins,key=lambda x:x['rectangle_t']),
               'worst_log_bin':max(allbins,key=lambda x:abs(x['log10_velocity_residual'])),
               'worst_velocity_bin':max(allbins,key=lambda x:abs(x['velocity_residual']))}
            given=official['combined'][key]['methods'][method]
            assert entry['bins_outside_rectangle']==given['bins_outside_rectangle']
            differences['aggregate_rms']=max(differences['aggregate_rms'],abs(entry['equal_galaxy_rms_log10_velocity']-given['equal_galaxy_rms_log10_velocity']))
            differences['aggregate_t']=max(differences['aggregate_t'],abs(entry['largest_rectangle_t']-given['largest_rectangle_t']))
            aggregates[key]['methods'][method]=entry
    assert max(differences.values())<1e-12,differences
    dump('independent_scores_and_gates_v1.json',{'lineage':lineage,'geometry_checks':geometry_checks,
          'gate_count':len(gates),'passed_gates':sum(x['passed'] for x in gates),'gates':gates,
          'score_row_count':len(score_rows),'score_rows':score_rows,'aggregates':aggregates,
          'maximum_absolute_discrepancies':differences})

    # Reconstruct all galaxy rows independently from observations and column receipts.
    knots=sources[names[0]]['knots']; galA=[]; galb=[]; gal_labels=[]
    for name in names:
        s=sources[name]; obs=s['v']**2/s['R']; low=np.maximum(0,s['v']-2*s['error'])**2/s['R']
        high=(s['v']+2*s['error'])**2/s['R']; kn=s['K']/obs[:,None]; baseline=s['g_N']/obs
        for side in ['upper','lower']:
            sign=1 if side=='upper' else -1
            bounds=high/obs-baseline if side=='upper' else baseline-low/obs
            for i,(coeff,rhs) in enumerate(zip(kn,bounds)):
                galA.append(list(sign*coeff)+[-1.]); galb.append(float(rhs))
                gal_labels.append({'kind':side+'_velocity_rectangle','source':name,'scored_bin':i,'R_kpc':float(s['R'][i])})
    def non_solar_matrix(case):
        sol=case['solution']; a=[row[:] for row in galA]+[[1.]*20+[0.]]; b=galb[:]+[100.]
        labels=gal_labels[:]+[{'kind':'weight_cap','cap':100}]
        if case['family']=='D':
            for j in range(20):
                row=[0.]*21; row[j]=1/np.log(knots[j+1]/knots[j])
                for k in range(j+1,20): row[k]=-1.
                a.append(row); b.append(1.); labels.append({'kind':'D_nonnegative_upper_ramp_limit','ramp':j})
        E=sol['external_newtonian_SI']
        if E is not None:
            assert E==freeze['fixed_E']==1.4915242022774435e-10
            vals=[float(np.clip(np.log(hi/E)/np.log(hi/lo),0,1)) for lo,hi in zip(knots[:-1],knots[1:])]
            a.extend([vals+[0.],[-x for x in vals]+[0.]])
            b.extend([2.64e-10/E-1,1-2e-10/E]); labels.extend([{'kind':'external_upper'},{'kind':'external_lower'}])
        return a,b,labels

    # Independent higher-precision solar-kernel integration in log(s) coordinates.
    # It checks numeric row construction, not a new continuum/measurement validation.
    E=mf(freeze['fixed_E']); GM=mf(1.32712440018e20); q=[]
    def log_integrand(x):
        s=mp.exp(x); p=4*s**4+2*s**3+3*s*s+2*s+4
        r=4*s**4-2*s**3+3*s*s-2*s+4
        numerator=s**5*(16*s**4+12*s*s+21) if s<=1 else 21*s**4+12*s*s+16
        return mp.mpf(16)/105*numerator/(r*mp.sqrt(1+s)+p*mp.sqrt(abs(1-s)))
    for lo,hi in zip(knots[:-1],knots[1:]):
        l,h=mp.log(mf(lo)/E),mp.log(mf(hi)/E)
        edges=[l]+([mp.mpf(0)] if l<0<h else [])+[h]
        integral=mp.quad(log_integrand,edges)
        q.append(E**mp.mpf('1.5')/mp.sqrt(GM)*mp.mpf(9)/8*integral/(h-l))
    cert_results=doc('certificate_RESULTS'); cert_rows=[]; primal_rows=[]; save_matrices={}
    identity_mapping={'source_sha256':'certificate_source','protocol_sha256':'certificate_protocol',
      'fit_source_sha256':'LP_component','nine_source_sha256':'source','freeze_sha256':'FREEZE',
      'candidates_sha256':'CANDIDATES','results_sha256':'RESULTS'}
    for identity,key in identity_mapping.items():
        en=entries.get(key,cent.get(key)); assert cert_results['identities'][identity]==en['sha256']
    for case in cases:
        guard(); key=case['name']; sol=case['solution']; cert=doc(key+'_certificate'); matrix=doc(key+'_matrix')
        assert cert['identities']==matrix['identities']==cert_results['identities']
        summary=next(x for x in cert_results['certificates'] if x['name']==key)
        assert summary['matrix_sha256']==cert['matrix_sha256']==cent[key+'_matrix']['sha256']
        assert summary['certificate_sha256']==cent[key+'_certificate']['sha256']
        given_a=[[float.fromhex(v) for v in row] for row in matrix['A_hex']]
        given_b=[float.fromhex(v) for v in matrix['b_hex']]
        ar,br,rl=non_solar_matrix(case); n=len(ar)
        assert ar==given_a[:n] and br==given_b[:n],key
        # Numeric zeros can have either sign; compare represented rational matrices.
        assert rl==matrix['row_labels'][:n]
        solar_err=None
        if sol['solar_bound_imposed']:
            assert len(given_a)==n+1 and matrix['row_labels'][-1]=={'kind':'solar_upper'}
            assert given_b[-1]==1 and given_a[-1][-1]==0
            solar_err=max(abs(mf(v)/(qq/mf(5.2e-27))-1) for v,qq in zip(given_a[-1][:-1],q))
            assert solar_err<mp.mpf('1e-11')
        else: assert len(given_a)==n
        assert matrix['objective']==[0]*20+[1] and matrix['variables']=='w0..w19,t >= 0'
        a=[[F(x) for x in row] for row in given_a]; b=list(map(F,given_b))
        y=list(map(frac,cert['y_rational'])); assert len(y)==len(a)==len(b)
        assert all(v<=0 for v in y)
        support=[i for i,v in enumerate(y) if v]
        # Sparse accumulation follows only the actual support, then checks every column.
        z=[sum((a[i][j]*y[i] for i in support),F(0)) for j in range(21)]
        assert z[-1]<=1
        delta=max([F(0)]+z[:-1]); yb=sum((b[i]*y[i] for i in support),F(0)); lower=yb-100*delta
        assert delta==frac(cert['weight_deficit_rational']) and 1-z[-1]==frac(cert['time_residual_rational'])
        assert lower==frac(cert['lower_bound_rational']) and lower>0
        decimal=F(cert['lower_bound_decimal_downward']); assert decimal<=lower<decimal+F(1,10**12)
        assert cert['weight_cap']==100 and a[180]==[F(1)]*20+[F(0)] and b[180]==100
        assert all(matrix['row_labels'][i]['kind'] not in ['solar_upper','external_upper','external_lower'] for i in support)
        expected_support=[{**matrix['row_labels'][i],'row':i,'y_approximate':float(y[i])} for i in support]
        assert expected_support==cert['nonzero_dual_rows']==summary['nonzero_dual_rows']
        proposed=[min(F(0),F(float.fromhex(v))) for v in cert['proposed_y_hex']]
        tau=sum((row[-1]*v for row,v in zip(a,proposed)),F(0)); scale=1/max(F(1),tau)
        assert scale==frac(cert['rescale_rational']) and y==[v*scale for v in proposed]
        cert_rows.append({'name':key,'all_non_solar_rows_reconstructed_exactly':True,
          'galaxy_rows_reconstructed':len(galA),'rows':len(a),'columns':21,
          'solar_row_max_relative_error_independent_quadrature':None if solar_err is None else float(solar_err),
          'lower_bound_decimal_downward':str(cert['lower_bound_decimal_downward']),
          'lower_bound_rational':ratio(lower),'residual_penalty_100delta':float(100*delta),
          't_coefficient':float(z[-1]),'support':expected_support,'all_support_rows_reconstructed_exactly':True})
        w=sol['weights']; x=list(map(F,w+[sol['fitted_t']]))
        assert sol['status']==0 and len(w)==20 and all(v>=0 for v in w)
        residual=[sum((aa*xx for aa,xx in zip(row,x)),F(0))-bound for row,bound in zip(a,b)]
        secondary=F(sol['fitted_t'])-F(float(sol['primary_minimum_t']+1e-8))
        maxres=max([F(0),secondary]+residual)
        assert abs(float(maxres)-sol['max_scaled_primal_violation'])<1e-12
        dvalues=[1+mp.fsum(mf(v) for v in w[j+1:])-mf(w[j])/mp.log(mf(knots[j+1])/mf(knots[j])) for j in range(20)]
        minj=min(range(20),key=lambda j:dvalues[j]); strict=min(dvalues)>0
        matrix_forces={}; offsets=[]
        for name in names:
            s=sources[name]; calculated=[F(float(gn))+exact_dot(row,w) for gn,row in zip(s['g_N'],s['K'])]
            assert all(v>0 for v in calculated)
            matrix_forces[name]=[float(v) for v in calculated]
            offsets.append({'name':name,'base_vs_matrix_relative':max(abs(float(F(g)/v-1)) for g,v in zip(s['fields']['candidates'][key]['methods']['base']['force'],calculated)),
                'offset_base_minus_matrix':[float(F(g)-v) for g,v in zip(s['fields']['candidates'][key]['methods']['base']['force'],calculated)]})
        pred_ext=None if sol['external_newtonian_SI'] is None else E*(1+mp.fsum(mf(wj)*max(mp.mpf(0),min(mp.mpf(1),mp.log(mf(hi)/E)/mp.log(mf(hi)/mf(lo)))) for wj,lo,hi in zip(w,knots[:-1],knots[1:])))
        Q=None if sol['external_newtonian_SI'] is None else mp.fsum(mf(wj)*qq for wj,qq in zip(w,q))
        if pred_ext is not None:
            assert abs(pred_ext/mf(sol['predicted_external_physical_SI'])-1)<mp.mpf('1e-14')
            assert abs(Q/mf(sol['Q2_s_minus2'])-1)<mp.mpf('1e-11')
        primal_rows.append({'name':key,'primary_minimum_t':sol['primary_minimum_t'],'secondary_fitted_t':sol['fitted_t'],
          'total_weight_independent':float(mp.fsum(mf(v) for v in w)),
          'maximum_exact_scaled_primal_violation':float(maxres),
          'maximum_violation_row':matrix['row_labels'][max(range(len(residual)),key=lambda i:residual[i])],
          'infimum_D_for_exact_binary_weights_and_knots':str(min(dvalues)),'infimum_D_ramp':minj,
          'strict_positive_D_established':strict,'Q2_independent_quadrature':None if Q is None else float(Q),
          'E_times_N_independent':None if pred_ext is None else float(pred_ext),
          'matrix_forces':matrix_forces,'base_matrix_differences':offsets})
        save_matrices[key+'_A']=np.array(ar); save_matrices[key+'_b']=np.array(br)
    np.savez_compressed(HERE/'independent_non_solar_matrices_v1.npz',**save_matrices)
    # In a linear projection the base Newtonian baseline error is independent of weights.
    offset_variations=[]
    for name in names:
        all_offsets=[next(z for z in row['base_matrix_differences'] if z['name']==name)['offset_base_minus_matrix'] for row in primal_rows]
        variation=max(max(v)-min(v) for v in zip(*all_offsets))
        assert variation<1e-9
        offset_variations.append({'name':name,'max_cross_candidate_offset_variation':variation})
    dump('independent_lp_and_certificates_v1.json',{'primal_rows':primal_rows,'certificate_rows':cert_rows,
        'solar_quadrature_method':'70-digit mpmath tanh-sinh integration in log(s), split at s=1; author helpers not imported',
        'q_coefficients_independent':[str(v) for v in q],'newtonian_projection_offset_check':offset_variations,
        'scope':'Frozen finite binary64 LP exact dual lower bounds; no refit, continuum claim or empirical validation.'})
    guard()
    outcome={'at':dt.datetime.now(dt.timezone.utc).isoformat(),'source_sha256':sha(__file__),
      'elapsed_seconds':time.monotonic()-start,'peak_rss_bytes':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
      'scored_points':sum(len(s['R']) for s in sources.values()),'gates':len(gates),'passed_gates':sum(x['passed'] for x in gates),
      'score_rows':len(score_rows),'certificate_count':len(cert_rows),'maximum_score_discrepancies':differences,
      'failed_gates':[x for x in gates if not x['passed']],
      'aggregates_refined':{k:{'all_field_gates_pass':v['all_field_gates_pass'],**v['methods']['refined']} for k,v in aggregates.items()},
      'no_author_imports':True,'no_fits_or_field_solves':True,'all_snapshot_source_hashes_matched':True}
    dump('independent_check_receipt_v1.json',outcome)
    print(json.dumps({k:v for k,v in outcome.items() if k!='aggregates_refined'},indent=2))

if __name__=='__main__': main()
