import json,sys
for f in sys.argv[1:]:
    try: r=json.loads(open(f).read().strip().splitlines()[-1])
    except Exception as e: print(f,'n/a'); continue
    if 'logrho_bar' not in r: print(f,'running'); continue
    s=f"{f}: bar {r['logrho_bar']:.3f}({r['err_bar']:.3f}) simp {r['logrho_simp']:.3f}({r['err_simp']:.3f}) simpI {r['logrho_simp_improved']:.3f}({r['err_simp_improved']:.3f}) {r['sec']}s"
    if 'spin_plus_half' in r:
        s+=f" | half +{r['spin_plus_half']:.2f}({r['spin_plus_half_err']:.2f}) -{r['spin_minus_half']:.2f}({r['spin_minus_half_err']:.2f}) 3/2 +{r['spin_plus_3h']:.4f}({r['spin_plus_3h_err']:.4f}) -{r['spin_minus_3h']:.4f}({r['spin_minus_3h_err']:.4f}) hi +{r['spin_plus_hi']:.1e}({r['spin_plus_hi_err']:.1e}) -{r['spin_minus_hi']:.1e}({r['spin_minus_hi_err']:.1e})"
    print(s)
