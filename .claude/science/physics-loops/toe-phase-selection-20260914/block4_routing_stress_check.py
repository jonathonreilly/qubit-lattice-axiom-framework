#!/usr/bin/env python3
"""Extra input rosters target negative displacements and multiple home types."""
import gc
import json
from pathlib import Path
from block4_periodic_routing_check import Compiler, Edge


def main():
    cases=[]
    inputs=[
        ((4,3),[
            Edge(0,0,0,1,(1,0,0)), Edge(0,1,1,0,(0,1,0)),
            Edge(1,1,0,2,(0,0,-1)), Edge(1,2,1,0,(-1,1,-1)),
            Edge(0,3,1,1,(0,0,0))]),
        ((1,),[Edge(0,0,0,0,(-2,1,-2))]),
    ]
    for payloads,edges in inputs:
        compiler=Compiler(payloads,edges)
        p=compiler.period
        result,roster=compiler.coordinates((p,p,p))
        result.update(microcell_side=compiler.side,source_radius=compiler.radius,
                      home_payloads=payloads,edge_types=len(edges))
        assert result['ordinary_maximum']<=2
        assert result['wrap_steps']>0
        cases.append(result)
        del roster
        gc.collect()
    result=dict(cases=cases,scope='additional exact-coordinate finite falsifiers; not a proof by sampling')
    Path(__file__).with_name('BLOCK4_ROUTING_STRESS_CHECK.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
