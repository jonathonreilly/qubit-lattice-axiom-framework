#!/usr/bin/env python3
"""Inspect frozen finite-profile outputs; no source/profile/ell refitting.

The height-clock extension is declared in EXTENSION_FREEZE.json. Numeric strings
retain 45 significant digits, sufficient for these tiny response differences.
"""
from __future__ import annotations
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
import mpmath as mp
import source_profiles as s


def vec(x):
    return mp.matrix(list(map(mp.mpf,x)))


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--runtime',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    mp.mp.dps=80
    deadline=json.loads((args.runtime/'DEADLINE.json').read_text())
    assert datetime.now(timezone.utc).timestamp()<deadline['deadline_epoch']
    assert not any((args.runtime/m).exists() for m in ['STOP_REQUESTED.json','USER_STOP_REQUESTED.json','STOP_REQUESTED','USER_STOP_REQUESTED'])
    base=Path(__file__).resolve().parent
    r80=json.loads((base/'results_80dps.json').read_text())
    r60=json.loads((base/'results_60dps.json').read_text())
    f=json.loads((base/'MODEL_FREEZE.json').read_text())
    ext=json.loads((base/'EXTENSION_FREEZE.json').read_text())
    GM=s.m(ext['GM_E_m3_s2']); c=s.m(ext['c_m_s'])
    rs,ra=map(s.m,f['Earth_field_radii_m'])
    R=s.m(f['Earth_radius_m']); core=s.m(f['Earth_core_radius_fraction'])
    asymptotic_coefficient=s.m('.32')*s.m('.68')*R**2*(1-core**2)/(1-core**3)*(ra**2-rs**2)
    fe=s.full('Fe'); mantle=s.compound({'Si':1,'O':2})
    delta_test=mp.matrix([0,*map(s.m,s.old.mix({'Ti':.90,'Al':.06,'V':.04})-s.old.mix({'Pt':.90,'Rh':.10}))])
    rows=[]
    for a,b in zip(r80['results'],r60['results']):
        det80=s.m(a['three_normalized_force_rows_determinant'])
        det60=s.m(b['three_normalized_force_rows_determinant'])
        relative_precision=abs((det60-det80)/det80)
        assert relative_precision<s.m('1e-23')
        ell=s.m(a['ell_m'])
        fs=s.m(a['Earth_core_weights']['surface']['effective_force_core_fraction'])
        fa=s.m(a['Earth_core_weights']['altitude']['effective_force_core_fraction'])
        solar=s.normal(vec(a['force_rows']['Sun_1AU']))
        material=mp.det(mp.matrix([list(fe),list(mantle),list(solar)]))
        factored=(fs-fa)*material
        factor_relative=abs((factored-det80)/det80)
        assert factor_relative<s.m('1e-14')
        surfaceP=vec(a['potential_rows']['Earth_surface'])
        altitudeP=vec(a['potential_rows']['Earth_710km'])
        clocks=[]
        for label,d in [(x['vector_label'],vec(x['d_g_x_e'])) for x in a['fixed_vectors']]+[
                       ('retuned_satellite_Sun',vec(a['two_row_retunes'][0]['d_g_x_e'])),
                       ('retuned_surface_Sun',vec(a['two_row_retunes'][1]['d_g_x_e']))]:
            delta_ratio=s.m('6.95')*d[2]*GM/c**2*(s.dot(altitudeP,d)/ra-s.dot(surfaceP,d)/rs)
            clocks.append({'vector_label':label,'local_E3E2_ratio_height_difference':delta_ratio})
        stresses=[]
        nominal_d=vec(a['two_row_retunes'][0]['d_g_x_e'])
        Ea=vec(a['force_rows']['Earth_710km']); Es=vec(a['force_rows']['Earth_surface'])
        for name,values in a['solar_stress_force_rows'].items():
            sun=vec(values)
            d=s.m('.1')*s.null_x_one(Ea,sun)
            stresses.append({'solar_model':name,
                'fixed_nominal_two_null_Sun_force_contraction':s.dot(sun,nominal_d),
                'fixed_nominal_Sun_annual_Yb_k_bare_GM':s.m('6.95')*nominal_d[2]*s.dot(sun,nominal_d),
                'retuned_d_g_x_e':d,
                'retuned_surface_TiPt_scalar_product':s.dot(Es,d)*s.dot(delta_test,d)})
        rows.append({'ell_m':ell,'determinant_60_vs_80_relative_difference':relative_precision,
                     'material_determinant':material,'factored_determinant_relative_difference':factor_relative,
                     'effective_core_fraction_surface_minus_altitude':fs-fa,
                     'leading_large_ell_core_difference':-asymptotic_coefficient/ell**4,
                     'actual_over_asymptotic':(fs-fa)/(-asymptotic_coefficient/ell**4),
                     'height_clock_responses':clocks,'solar_model_stresses_not_probabilities':stresses})
        print('ell',a['ell_m'],'precision rel',mp.nstr(relative_precision,5),
              'core delta',mp.nstr(fs-fa,8),'height clock(retuned)',mp.nstr(clocks[3]['local_E3E2_ratio_height_difference'],9),flush=True)
    out={'created_at':datetime.now(timezone.utc).isoformat(),'status':'conditional theoretical responses and arithmetic checks only',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'input_hashes':{name:hashlib.sha256((base/name).read_bytes()).hexdigest() for name in ['results_80dps.json','results_60dps.json','MODEL_FREEZE.json','EXTENSION_FREEZE.json']},
         'large_ell_core_difference_coefficient_m4':asymptotic_coefficient,
         'results':rows,
         'checks':['Determinants stable to at least 23 relative decimal places between 60 and 80 working digits.',
                   'Direct three-source determinant agrees with material-row factorization to printed-output precision.',
                   'All clock predictions use the same already fixed or specified pair-retuned couplings.'],
         'limitations':['No empirical clock exclusion or instrumental sensitivity claimed.',
                        'Height-clock numbers use the supplied bare metric GM normalization and local clock-ratio response.',
                        'Solar stresses change source model; fixed-vector and separately retuned-vector results are distinct.']}
    args.output.write_text(json.dumps(s.serial(out),indent=2)+'\n')


if __name__=='__main__':
    main()
