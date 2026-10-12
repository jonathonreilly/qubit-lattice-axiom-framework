"""R16-1 (d): combine the legs into Delta^Pa (selectrons only) and Delta^Pb (+ selectron-photino loop) on D1(1.4, 1/sqrt3).
Electron photon loop and Dirac dc_gamma from r161_mscan.out; selectron dc_gamma and partner loop from r161_partner_mscan.out
(levels (6,4), (8,6); Nref = 256) with the small-m selectron replaced by the Nref = 4096 control (r161_selectron_smallm.out,
level (6,4)) for m <= 0.05, and the (12,8) subset from r161_partner_hires.out (Nref = 4096)."""
import re
def parse(fn, pat):
    d = {}
    for line in open(fn):
        mm = re.search(pat, line)
        if mm: d[(float(mm.group(1)), mm.group(2))] = [float(x) for x in mm.groups()[2:]]
    return d
main = parse('r161_mscan.out', r'm=\s*([\d.]+) \| \((\d+,\d+)\) \| \d+,\d+ \| dc_e=\s*([-+\d.]+) \| dc_g=\s*([-+\d.]+)')
part = parse('r161_partner_mscan.out', r'm=\s*([\d.]+) \| \((\d+,\d+)\) \| dcg_2sel=\s*([-+\d.]+) \| dce_partner=\s*([-+\d.]+)')
hi = parse('r161_partner_hires.out', r'm=\s*([\d.]+) \| \((\d+,\d+)\) \| dcg_2sel\(Nref=4096\)=\s*([-+\d.]+) \| dce_partner=\s*([-+\d.]+)')
sm = {}
for line in open('r161_selectron_smallm.out'):
    mm = re.search(r'm=([\d.]+).*4096: ([-+\d.]+)', line)
    if mm: sm[float(mm.group(1))] = float(mm.group(2))
ms = sorted(set(k[0] for k in part))
print('| m | dc_gamma(2 sel) | dc_e(partner loop) R1 / R2 / R3 | Delta^Pa (R2) | Delta^Pb (R2) |')
print('|---|---|---|---|---|')
for m in ms:
    rows = []
    for lev in ('6,4', '8,6'):
        if (m, lev) in part and (m, lev) in main:
            dce, dcg = main[(m, lev)]; s2, pa = part[(m, lev)]
            if m <= 0.05 and m in sm: s2 = sm[m]
            rows.append((lev, dce, dcg, s2, pa))
    if not rows: continue
    lev, dce, dcg, s2, pa = rows[-1]
    r3 = hi.get((m, '12,8'))
    pas = ' / '.join('%+.4f' % r[4] for r in rows) + (' / %+.4f' % r3[1] if r3 else ' / —')
    print('| %g | %+.4f%s | %s | %+.4f | %+.4f |' % (m, s2, ' (q-controlled)' if m <= 0.05 else '', pas, dce - dcg - s2, dce - dcg - s2 + pa))
