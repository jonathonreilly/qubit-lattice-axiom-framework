#!/usr/bin/env python3
"""Trace published figure geometry; do not treat it as raw measurement data."""
from pathlib import Path
import argparse
import hashlib
import json
import math

import fitz
import numpy as np
from PIL import Image


ROOT = Path(__file__).resolve().parent
PDF_SHA = '3e32e882d9ad1b504c22fffbbca3b57bc83615c47b6629e8a356927b3e07e9b7'


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--pdf', type=Path, required=True)
    parser.add_argument('--render', type=Path, required=True)
    args = parser.parse_args()
    assert sha(args.pdf) == PDF_SHA
    page = fitz.open(args.pdf)[8]
    drawings = page.get_drawings()
    red = drawings[51]
    assert red['color'] == (1.0, 0.0, 0.0)
    raw = [[list(a), list(b)] for kind, a, b in red['items'] if kind == 'l']
    assert len(raw) == 31
    legend = raw[0]
    assert abs(legend[0][1]-99.697998046875) < 1e-6
    segments = raw[1:]
    assert all(segments[i][1] == segments[i+1][0] for i in range(len(segments)-1))
    points = np.array([segments[0][0]] + [s[1] for s in segments])
    assert np.all(np.diff(points[:, 0]) > 0)

    # Major black tick positions read from the same page vector paths.
    # Labels were verified on the rendered complete figure.
    x_ticks = np.array([357.5360107421875, 395.08599853515625,
                        432.5679931640625, 470.1189880371094, 507.66900634765625])
    radius_ticks = np.array([0., .4, .8, 1.2, 1.6])
    y_ticks = np.array([172.46099853515625, 132.572021484375, 92.75201416015625])
    sigma_ticks = np.array([0., 5., 10.])
    xcoef = np.polyfit(x_ticks, radius_ticks, 1)
    ycoef = np.polyfit(y_ticks, sigma_ticks, 1)
    xerr = float(np.max(np.abs(np.polyval(xcoef, x_ticks)-radius_ticks)))
    yerr = float(np.max(np.abs(np.polyval(ycoef, y_ticks)-sigma_ticks)))
    assert xerr < .001 and yerr < .01
    radius = np.polyval(xcoef, points[:, 0])
    density = np.polyval(ycoef, points[:, 1])
    assert np.min(density) > 0

    # An independent rendering route: every red curve pixel should lie by
    # the original PDF polyline. This checks tracing, not empirical accuracy.
    pixels = np.array(Image.open(args.render).convert('RGB'))
    height, width = pixels.shape[:2]
    yy, xx = np.mgrid[:height, :width]
    px = (xx+.5)*page.rect.width/width
    py = (yy+.5)*page.rect.height/height
    selected = ((pixels[:, :, 0] > 200) & (pixels[:, :, 1] < 100) &
                (pixels[:, :, 2] < 100) & (px > 360) & (px < 537) &
                (py > 140) & (py < 174))
    samples = np.column_stack([px[selected], py[selected]])
    distances = np.full(len(samples), math.inf)
    for a, b in np.array(segments):
        delta = b-a
        t = np.clip((samples-a) @ delta/(delta @ delta), 0, 1)
        distances = np.minimum(distances, np.linalg.norm(samples-(a+t[:, None]*delta), axis=1))
    assert len(samples) > 200 and float(distances.max()) < .7

    prior = ROOT.parent/'nine_source_reconstruction/independent_review/snapshots/pressure_receipt.json'
    meta = ROOT.parent/'nine_source_reconstruction/independent_review/snapshots/source_receipt_UGC07577.json'
    pressure = json.loads(prior.read_text())
    required = next(r for r in pressure['results'] if r['family'] == 'D')
    source_distance = json.loads(meta.read_text())['source_row']['meta']['D']
    assert source_distance == 2.59
    r0 = required['R_kpc']*2.6/source_distance
    pmin = required['necessary_max_pressure_km2_s2_approximate']
    sigma = 8.
    required_slope = pmin/sigma**2
    rows = []
    for width_kpc in [.09, .18, .36]:
        lo, hi = r0-width_kpc/2, r0+width_kpc/2
        slow, shigh = np.interp([lo, hi], radius, density)
        slope = -math.log(shigh/slow)/math.log(hi/lo)
        rows.append({'figure_interval_kpc': [lo, hi], 'width_kpc': width_kpc,
                     'Sigma_endpoints_Msun_pc2': [float(slow), float(shigh)],
                     'log_chord_slope': slope, 'illustrative_p_chord_km2_s2': sigma**2*slope,
                     'observed_plot_outer_inner_ratio': float(shigh/slow),
                     'required_outer_inner_ratio_if_bound_holds_throughout_interval': (hi/lo)**(-required_slope),
                     'resolution_status': 'below nominal resolution' if width_kpc < .18 else 'nominal resolution scale or wider'})
    result = {'schema': 'published_hi_profile_diagnostic_v1',
              'source_pdf': {'sha256': PDF_SHA, 'url': 'https://pure.rug.nl/ws/portalfiles/portal/75866939/aa19457_12.pdf',
                             'page_zero_index': 8, 'figure': 9, 'path_index': 51, 'excluded_legend': legend,
                             'raw_curve_segments_pdf_points': segments},
              'software': {'pymupdf': fitz.VersionBind, 'numpy': np.__version__},
              'source_sha256': {n: sha(ROOT/n) for n in ['PROTOCOL.md', Path(__file__).name]},
              'prior_pressure_sha256': sha(prior), 'source_metadata_sha256': sha(meta),
              'calibration': {'x_pdf_ticks': x_ticks.tolist(), 'R_kpc_labels': radius_ticks.tolist(),
                              'y_pdf_ticks': y_ticks.tolist(), 'Sigma_labels': sigma_ticks.tolist(),
                              'x_linear_coefficients': xcoef.tolist(), 'y_linear_coefficients': ycoef.tolist(),
                              'max_radius_tick_residual_kpc': xerr, 'max_density_tick_residual': yerr},
              'render_crosscheck': {'sha256': sha(args.render), 'red_pixels_checked': len(samples),
                                    'max_distance_to_vector_line_pdf_points': float(distances.max())},
              'figure_trace': [{'R_kpc_at_2p6Mpc': float(r), 'Sigma_HI_Msun_pc2': float(s)} for r, s in zip(radius, density)],
              'selected_radius': {'campaign_kpc': required['R_kpc'], 'campaign_distance_Mpc': source_distance,
                                  'figure_distance_Mpc': 2.6, 'figure_kpc': r0},
              'illustrative_sigma_km_s': sigma, 'required_pressure_km2_s2': pmin,
              'required_log_slope': required_slope, 'required_local_scale_kpc_at_figure_distance': r0/required_slope,
              'diagnostics': rows,
              'limits': ['published polyline, not raw or deconvolved data', 'no error bars or covariance supplied',
                         'constant sigma and height supplied', 'chord is not the point derivative in the finite certificate',
                         'density-ratio comparison adds persistence-across-interval premise',
                         'no fit, no likelihood, no unconditional pressure exclusion']}
    out = ROOT/'evidence_v1';out.mkdir(exist_ok=True)
    with (out/'RESULTS.json').open('x') as f:
        json.dump(result, f, indent=2, allow_nan=False);f.write('\n')
    print(json.dumps({'radius': r0, 'required_pressure': pmin, 'diagnostics': rows,
                      'render_check': result['render_crosscheck']}, indent=2))


if __name__ == '__main__':
    main()
