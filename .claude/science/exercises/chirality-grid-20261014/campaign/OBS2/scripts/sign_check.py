import sys; sys.argv = ['x']
exec(open('sizes2.py').read().split("if __name__")[0])
combos = [(m, D, var) for m in ('0.1', '0.05', '0.025') for D in ('0.0', '0.5') for var in ('sym', 'int', 'ext')]
Is = {cb: loadI(96, *cb) for cb in combos}
for bname in ('B', "B'"):
    for split in ('trace', 'selective'):
        for qs in (1.0, 0.45):
            vals = {nm: [run(Is[cb], bname, split, qs, 1.0)[0][nm]['cTT'] for cb in combos] for nm in ('d', 's', 'b')}
            print(bname, split, 'qscale', qs, {nm: (f"{min(v):+.2e}", f"{max(v):+.2e}") for nm, v in vals.items()})
