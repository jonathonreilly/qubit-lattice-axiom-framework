#!/usr/bin/env python3
"""Post-calculation counterexample to over-interpreting source-row rank.

Same model and inputs, no empirical fit. This is an additional algebraic family,
not one of the originally frozen finite-range witness selections.
"""
from datetime import datetime,timezone
import argparse,hashlib,json,sys
from pathlib import Path
sys.dont_write_bytecode=True
import mpmath as mp
import source_profiles as s


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--runtime',type=Path,required=True)
    p.add_argument('--output',type=Path,required=True)
    args=p.parse_args()
    mp.mp.dps=70
    deadline=json.loads((args.runtime/'DEADLINE.json').read_text())
    assert datetime.now(timezone.utc).timestamp()<deadline['deadline_epoch']
    assert not any((args.runtime/m).exists() for m in ['STOP_REQUESTED.json','USER_STOP_REQUESTED.json','STOP_REQUESTED','USER_STOP_REQUESTED'])
    path=Path(__file__).with_name('results_80dps.json')
    source=json.loads(path.read_text())
    deltaM=mp.matrix([0,*map(s.m,s.old.mix({'Ti':.90,'Al':.06,'V':.04})-s.old.mix({'Pt':.90,'Rh':.10}))])
    deltaB=s.full('Be')-s.full('Al')
    rows=[]
    for row in source['results']:
        WF={name:mp.matrix(list(map(s.m,value))) for name,value in row['force_rows'].items()}
        x=s.m('.1'); e=-deltaM[1]/deltaM[2]*x
        sun=WF['Sun_1AU']
        g=-(sun[1]*x+sun[2]*e)/sun[0]
        d=mp.matrix([g,x,e])
        assert abs(s.dot(deltaM,d))<s.m('1e-60')
        assert abs(s.dot(sun,d))<s.m('1e-60')
        rows.append({'ell_m':row['ell_m'],'d_g_x_e':d,
          'TiPt_test_contrast':s.dot(deltaM,d),
          'force_source_contractions':{name:s.dot(value,d) for name,value in WF.items()},
          'Earth_surface_BeAl_scalar_acceleration_product':s.dot(WF['Earth_surface'],d)*s.dot(deltaB,d),
          'Earth_710km_BeAl_scalar_acceleration_product':s.dot(WF['Earth_710km'],d)*s.dot(deltaB,d),
          'Sun_annual_optical_coefficient':s.m('6.95')*d[2]*s.dot(sun,d)})
        print('ell',row['ell_m'],'Earth surface BeAl product',mp.nstr(rows[-1]['Earth_surface_BeAl_scalar_acceleration_product'],10))
    out={'created_at':datetime.now(timezone.utc).isoformat(),
         'status':'additional exact conditional null family, developed after source-rank calculation',
         'script_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
         'source_results_sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
         'construction':'x=.1; e=-DeltaQme_TiPt/DeltaQem_TiPt*x; g=-(WSun_me*x+WSun_em*e)/WSun_0',
         'rows':rows,
         'meaning':['TiPt force numerators vanish at every Earth radius because their test contrast vanishes.',
                    'The Sun force-source contraction vanishes, so solar annual E3E2 and solar BeAl vanish too.',
                    'An Earth BeAl comparison supplies a nonzero independent product in this model.',
                    'A purely universal d=(g,0,0) is also invisible to all such relative composition/clock-ratio channels; distance-dependent gravity can test it.',
                    'No empirical exclusion is inferred from the printed point-test products.']}
    args.output.write_text(json.dumps(s.serial(out),indent=2)+'\n')


if __name__=='__main__':
    main()
