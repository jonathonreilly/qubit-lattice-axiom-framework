#!/usr/bin/env python3
"""Independent PDF content-stream/pressure check. Does not import an author runner.

Coordinates are extracted from pypdf's raw decimal content stream. Calibration
and linear interpolation use fractions; logarithms use mpmath at 70 digits.
The author JSON is read only after the independent observables are computed.
This checks a displayed vector profile, not the unresolved physical gas.
"""
from pathlib import Path
from fractions import Fraction as F
from collections import Counter
import ast
import hashlib
import json
import math
import platform
import struct
from datetime import datetime, timezone
import mpmath as mp
import pypdf
from pypdf import PdfReader
from PIL import Image

OUT = Path(__file__).resolve().parent
SNAP = OUT / 'source_snapshot'
PDF = Path('/Users/jonBridger/.codex/campaigns/observations-to-toe-24h-20261012/pressure/tmp/pdfs/lelli2012_aa19457_12.pdf')
RENDER = PDF.parent / 'figure9_page.png'
PDF_SHA = '3e32e882d9ad1b504c22fffbbca3b57bc83615c47b6629e8a356927b3e07e9b7'
RENDER_SHA = '3639b226bfd6f2069ef2ffde3d63b358c94e1da8c701d610de2502cae33653da'
mp.mp.dps = 70


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


def rat(v):
    return F(str(v))


def high(v):
    return mp.mpf(v.numerator) / v.denominator if isinstance(v, F) else mp.mpf(str(v))


def printable(v):
    return mp.nstr(high(v), 45)


def ols(xs, ys):
    n = len(xs)
    slope = (n*sum(x*y for x, y in zip(xs, ys)) - sum(xs)*sum(ys)) / (n*sum(x*x for x in xs) - sum(xs)**2)
    intercept = (sum(ys) - slope*sum(xs))/n
    return slope, intercept


def line_value(xs, ys, x):
    for j in range(len(xs)-1):
        if xs[j] <= x <= xs[j+1]:
            return ys[j] + (ys[j+1]-ys[j])*(x-xs[j])/(xs[j+1]-xs[j])
    raise ValueError('No extrapolation allowed')


def float32(v):
    return F(struct.unpack('f', struct.pack('f', float(v)))[0])


assert sha(PDF) == PDF_SHA
assert sha(RENDER) == RENDER_SHA
reader = PdfReader(PDF)
page = reader.pages[8]
assert tuple(map(rat, page.mediabox)) == (0, 0, 595, 842)
assert page.rotation == 0
ops = page.get_contents().operations
counts = Counter(op.decode() for _, op in ops)
assert 'cm' not in counts and 'Do' not in counts
colour_space = page['/Resources']['/ColorSpace']['/Cs6'].get_object()
assert colour_space[0] == '/ICCBased'
assert colour_space[1].get_object()['/N'] == 3

# Reconstruct stroked subpaths, including all source layers. No drawing index
# from the author extractor is used. Non-stroking colours are immaterial.
colour = (F(0),)*3
dash = ()
width = F(1)
path = []
subpath = []
stroked = []
stack = []
tm = None
texts = []
for index, (args, op) in enumerate(ops):
    if op == b'q':
        stack.append((colour, dash, width))
    elif op == b'Q':
        colour, dash, width = stack.pop()
    elif op == b'SCN':
        colour = tuple(map(rat, args))
    elif op == b'w':
        width = rat(args[0])
    elif op == b'd':
        dash = tuple(map(rat, args[0]))
    elif op == b'm':
        if subpath:
            path.append(subpath)
        subpath = [tuple(map(rat, args))]
    elif op == b'l':
        assert subpath
        subpath.append(tuple(map(rat, args)))
    elif op in (b'c', b're'):
        # None of the selected curve/tick candidates uses a cubic or rectangle.
        if subpath:
            path.append(subpath)
        subpath = []
    elif op in (b'S', b's', b'f', b'F', b'f*', b'n'):
        if subpath:
            path.append(subpath)
        if op in (b'S', b's'):
            for points in path:
                if len(points) >= 2:
                    stroked.append(dict(points=points, colour=colour, dash=dash, width=width, end_operation=index))
        path, subpath = [], []
    elif op == b'Tm':
        tm = tuple(map(rat, args))
    elif op == b'Tj' and tm is not None:
        texts.append(dict(text=str(args[0]), x=tm[-2], y=tm[-1]))

red = [p for p in stroked if p['colour'] == (1, 0, 0)]
candidates = [p for p in red if len(p['points']) > 20 and all(F(669) < y < F(710) for x,y in p['points'])]
assert len(candidates) == 1
chosen = candidates[0]
curve = chosen['points']
assert len(curve) == 31
assert chosen['dash'] == (F('2.751'), F('1.3755'))
assert all(curve[i][0] < curve[i+1][0] for i in range(30))
legend = [p for p in red if len(p['points']) == 2 and all(F(740) < y < F(745) for x,y in p['points'])]
assert len(legend) == 1 and legend[0]['points'][0][1] == legend[0]['points'][1][1]
assert any(t['text'] == 'DDO 125' and F(738) < t['y'] < F(741) for t in texts)

black_segments = []
for p in stroked:
    if p['colour'] == (0, 0, 0):
        black_segments.extend(zip(p['points'], p['points'][1:]))
x_ticks = sorted({a[0] for a,b in black_segments if a[0] == b[0] and a[1] == F('451.663') and F(4) < b[1]-a[1] < F(5)})
y_ticks = sorted({a[1] for a,b in black_segments if a[1] == b[1] and a[0] == F('357.536') and F(4) < b[0]-a[0] < F(5) and F(669) < a[1] < F(755)})
assert len(x_ticks) == 5 and len(y_ticks) == 3
x_labels = []
y_labels = []
for x in x_ticks:
    labels = [t for t in texts if abs(t['x']-x) < 6 and F(440) < t['y'] < F(441)]
    assert len(labels) == 1
    x_labels.append(rat(labels[0]['text']))
for y in y_ticks:
    labels = [t for t in texts if F(342) < t['x'] < F(349) and F(2) < y-t['y'] < F(3)]
    assert len(labels) == 1
    y_labels.append(rat(labels[0]['text']))
assert x_labels == list(map(F, ('0','.4','.8','1.2','1.6')))
assert y_labels == [F(0),F(5),F(10)]
top_x_ticks = sorted({a[0] for a,b in black_segments if a[0] == b[0] and a[1] == F('669.539') and F(4) < b[1]-a[1] < F(5)})
assert top_x_ticks == x_ticks

pressure = json.loads((SNAP/'pressure_receipt.json').read_text())
source = json.loads((SNAP/'source_receipt_UGC07577.json').read_text())
d = next(r for r in pressure['results'] if r['family'] == 'D')
p_needed = F(*map(int,d['necessary_max_pressure_km2_s2_rational']))
r0 = rat(d['R_kpc']) * F('2.6')/rat(source['source_row']['meta']['D'])
assert source['source_row']['meta']['D'] == 2.59
assert r0 == F(1222,1295)
sigma2 = F(64)
required_slope = p_needed/sigma2


def derive(points, xticks, yticks):
    ar, br = ols(xticks, x_labels)
    az, bz = ols(yticks, y_labels)
    radii = [ar*x+br for x,y in points]
    densities = [az*y+bz for x,y in points]
    assert all(s > 0 for s in densities)
    rows = []
    for w in map(F, ('.09','.18','.36')):
        lo, hi = r0-w/2, r0+w/2
        sl, sh = line_value(radii,densities,lo), line_value(radii,densities,hi)
        lograd = mp.log(high(hi/lo))
        ratio = high(sh/sl)
        slope = -mp.log(ratio)/lograd
        maxratio = mp.exp(-high(required_slope)*lograd)
        rows.append(dict(width_kpc=float(w), radius=[printable(lo),printable(hi)], density=[printable(sl),printable(sh)], minus_log_density_chord_slope=printable(slope), p_chord_km2_s2=printable(high(sigma2)*slope), display_ratio=printable(ratio), sustained_pressure_ratio_bound=printable(maxratio)))
    return dict(radius_coefficients=[printable(ar),printable(br)], density_coefficients_bottom_origin=[printable(az),printable(bz)], max_radius_tick_residual_kpc=printable(max(abs(ar*x+br-y) for x,y in zip(xticks,x_labels))), max_density_tick_residual=printable(max(abs(az*x+bz-y) for x,y in zip(yticks,y_labels))), trace=[[printable(r),printable(s)] for r,s in zip(radii,densities)], rows=rows)


exact_decimal = derive(curve,x_ticks,y_ticks)
# MuPDF's observed coordinate conversion is binary32 followed by a y flip.
# Reproduce that conversion only as a separate rounding comparison; all actual
# extraction above uses the independent raw PDF parser and original decimals.
binary32 = derive([(float32(x),float32(y)) for x,y in curve],list(map(float32,x_ticks)),list(map(float32,y_ticks)))

# Independent geometry/render comparison uses scalar segment projection.
img = Image.open(RENDER).convert('RGB')
iw, ih = img.size
segments = [((float(a[0]),842-float(a[1])),(float(b[0]),842-float(b[1]))) for a,b in zip(curve,curve[1:])]
distance_max = 0.0
pixel_count = 0
for yp in range(max(0,int(139*ih/842)), min(ih,math.ceil(175*ih/842))):
    for xp in range(max(0,int(359*iw/595)), min(iw,math.ceil(538*iw/595))):
        r,g,b = img.getpixel((xp,yp))
        x,y = (xp+.5)*595/iw,(yp+.5)*842/ih
        if not (r > 200 and g < 100 and b < 100 and 360 < x < 537 and 140 < y < 174):
            continue
        best = float('inf')
        for (ax,ay),(bx,by) in segments:
            vx,vy = bx-ax,by-ay
            t = max(0,min(1,((x-ax)*vx+(y-ay)*vy)/(vx*vx+vy*vy)))
            best = min(best, math.hypot(x-(ax+t*vx),y-(ay+t*vy)))
        pixel_count += 1
        distance_max = max(distance_max,best)
assert pixel_count == 820 and distance_max < .571

author = json.loads((SNAP/'evidence_v1/RESULTS.json').read_text())
assert author['source_pdf']['sha256'] == PDF_SHA
assert author['render_crosscheck']['sha256'] == RENDER_SHA
for name,h in author['source_sha256'].items():
    assert sha(SNAP/name) == h
assert sha(SNAP/'pressure_receipt.json') == author['prior_pressure_sha256']
assert sha(SNAP/'source_receipt_UGC07577.json') == author['source_metadata_sha256']
max_raw_coordinate_error = 0.0
for (a,b),stored in zip(zip(curve,curve[1:]),author['source_pdf']['raw_curve_segments_pdf_points']):
    for exact,shown in zip((a,b),stored):
        max_raw_coordinate_error = max(max_raw_coordinate_error,abs(float(exact[0])-shown[0]),abs(842-float(exact[1])-shown[1]))
assert len(author['source_pdf']['raw_curve_segments_pdf_points']) == 30
assert max_raw_coordinate_error < .00004
assert abs(high(r0)-mp.mpf(author['selected_radius']['figure_kpc'])) < mp.mpf('2e-16')
assert abs(high(p_needed)-mp.mpf(author['required_pressure_km2_s2'])) < mp.mpf('2e-13')
comparisons=[]
for er,br,ar in zip(exact_decimal['rows'],binary32['rows'],author['diagnostics']):
    p_exact=mp.mpf(er['p_chord_km2_s2']);p_binary=mp.mpf(br['p_chord_km2_s2']);p_author=mp.mpf(ar['illustrative_p_chord_km2_s2'])
    assert abs(p_exact-p_author) < mp.mpf('.003')
    assert abs(p_binary-p_author) < mp.mpf('1e-9')
    assert abs(mp.mpf(er['display_ratio'])-mp.mpf(ar['observed_plot_outer_inner_ratio'])) < mp.mpf('1e-5')
    assert abs(mp.mpf(er['sustained_pressure_ratio_bound'])-mp.mpf(ar['required_outer_inner_ratio_if_bound_holds_throughout_interval'])) < mp.mpf('1e-14')
    comparisons.append(dict(width_kpc=er['width_kpc'], exact_decimal_minus_author_p=printable(p_exact-p_author), binary32_minus_author_p=printable(p_binary-p_author)))

# Independent analytic controls for the conditional log-chord operation.
lo,hi=r0-F('.09'),r0+F('.09')
for exponent in [F(0),F(1),F(7,3),required_slope]:
    ratio=mp.exp(-high(exponent)*mp.log(high(hi/lo)))
    recovered=-high(sigma2)*mp.log(ratio)/mp.log(high(hi/lo))
    assert abs(recovered-high(sigma2*exponent)) < mp.mpf('1e-60')
for w,ss in [(F('.18'),F(0)),(F('.18'),F(1)),(F('.36'),F(64))]:
    # Constant surface density gives zero chord correction for any sigma.
    assert -high(ss)*mp.log(1)/mp.log(high((r0+w/2)/(r0-w/2))) == 0

# Clarify a possible escape-display ambiguity: runner's trailing write is one
# newline character. No author code is executed even for this syntax check.
tree=ast.parse((SNAP/'trace_profile.py').read_text())
write_literals=[ast.literal_eval(n.args[0]) for n in ast.walk(tree) if isinstance(n,ast.Call) and isinstance(n.func,ast.Attribute) and n.func.attr=='write']
assert write_literals == ['\n']

result=dict(schema='independent_hi_pressure_review_checks_v1', at=datetime.now(timezone.utc).isoformat(), disposition='PASS_SCOPED_NUMERICAL_CHECKS', software=dict(python=platform.python_version(),pypdf=pypdf.__version__,mpmath=mp.__version__), source_pdf_sha256=sha(PDF), source_render_sha256=sha(RENDER), source_snapshot_sha256={str(p.relative_to(SNAP)):sha(p) for p in sorted(SNAP.rglob('*')) if p.is_file()}, independent_check_sha256=sha(Path(__file__)), raw_pdf_content_stream=dict(operations=len(ops), colours='three-component ICCBased; red source also verified visually', selected_stroke_end_operation=chosen['end_operation'], curve_vertices=31, excluded_legend_vertices=2, x_ticks=list(map(str,x_ticks)), y_ticks_bottom_origin=list(map(str,y_ticks)), x_labels=list(map(str,x_labels)), y_labels=list(map(str,y_labels)), max_author_coordinate_rounding_error_pdf_points=max_raw_coordinate_error), exact_decimal_pdf_route=exact_decimal, binary32_conversion_comparison=binary32, arithmetic=dict(radius_kpc=printable(r0), pressure_requirement=printable(p_needed), slope_requirement=printable(required_slope), local_scale_kpc=printable(r0/required_slope)), comparisons=comparisons, render_crosscheck=dict(red_pixels=pixel_count,max_pdf_point_distance=distance_max,measurement_error_model=False), check_families=[dict(name='raw PDF red-path identity and connected legend exclusion',pass_=True),dict(name='independent labelled tick calibration and top/bottom axis agreement',pass_=True),dict(name='distance map and exact-premise chord arithmetic',pass_=True),dict(name='render geometry agreement',pass_=True),dict(name='constant/power-law analytic controls and pinned-source consistency',pass_=True)], limitation='No author runner executed; no finite-source solve, data fit, measurement likelihood, deconvolution, actual pressure inference or physical exclusion. Decimal/float comparison is arithmetic reproducibility, not an uncertainty model.')
with (OUT/'CHECK_RESULTS_v1.json').open('x') as f:
    json.dump(result,f,indent=2,allow_nan=False)
    f.write('\n')
print(json.dumps(dict(disposition=result['disposition'],comparisons=comparisons,render_crosscheck=result['render_crosscheck'],arithmetic=result['arithmetic']),indent=2))
