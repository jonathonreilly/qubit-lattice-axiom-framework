"""Independent finite spectral/optimization/arithmetic controls, no inherited code.

No rotor evolution, count simulation, parent runner, or author code is used.
Floating checks corroborate the analytic identities; they are not interval proofs.
"""
from pathlib import Path
from decimal import Decimal, localcontext
import datetime, hashlib, json, math, platform, time
import numpy as np

START = time.perf_counter()
HERE = Path(__file__).resolve().parent

def modes(side):
    indices = np.arange(side)
    squares = 4 * np.sin(np.pi * indices / side) ** 2
    xx, yy, zz = np.meshgrid(squares, squares, squares, indexing='ij')
    ss = np.sqrt(xx + yy + zz).ravel()
    numerator = (xx + yy).ravel()
    keep = ss > 0
    s = ss[keep]
    weight = numerator[keep] / (2 * side ** 3 * s)
    return s, weight

def direct_curl(side):
    # +axis edge convention, integer plaquette curl; independently constructed.
    volume = side ** 3
    def vertex(x):
        return ((x[0] % side) * side + x[1] % side) * side + x[2] % side
    def edge(x, mu):
        return 3 * vertex(x) + mu
    curl = np.zeros((3*volume, 3*volume))
    pairs = [(0,1),(0,2),(1,2)]
    for x in np.ndindex(side,side,side):
        for plane,(mu,nu) in enumerate(pairs):
            row = 3*vertex(x)+plane
            xp = list(x); xp[mu] += 1
            xq = list(x); xq[nu] += 1
            curl[row,edge(x,mu)] += 1
            curl[row,edge(xp,nu)] += 1
            curl[row,edge(xq,mu)] -= 1
            curl[row,edge(x,nu)] -= 1
    eigenvalues, eigenvectors = np.linalg.eigh(curl.T @ curl)
    positive = eigenvalues > 1e-10
    lam = eigenvalues[positive]
    s = np.sqrt(lam)
    local_row = curl[0]
    coefficients = local_row @ eigenvectors[:,positive]
    weights = coefficients**2/(2*s)
    return s, weights, eigenvalues, curl

def profile(s, weight, target):
    s0 = float(np.min(s))
    v = float(np.sum(weight))
    bright_mean = float(np.dot(s,weight)/v)
    assert s0 < target < bright_mean
    def quantities(z):
        terms = weight/(s+z)**2
        B = float(np.sum(terms))
        mean = float(np.dot(s,terms)/B)
        A = float(np.sum(weight/(s+z)))
        return mean,A,B
    lo = -s0+1e-12
    hi = 1.0
    while quantities(hi)[0] < target:
        hi *= 2
    for _ in range(100):
        mid = (lo+hi)/2
        if quantities(mid)[0] < target:
            lo=mid
        else:
            hi=mid
    z=(lo+hi)/2
    mean,A,B=quantities(z)
    amplitude=A/math.sqrt(B)
    eta=amplitude**2/v
    dual=(target+z)*A/v
    assert abs(mean-target)<2e-12
    assert abs(eta-dual)<2e-12
    return {'mean_ceiling':target,'shift_z':z,'attained_mean':mean,
            'eta':eta,'dual_upper_eta':dual,'primal_dual_gap':dual-eta,
            'mean_weighted_Cauchy_bound':target*float(np.sum(weight/s))/v,
            'bright_dark_mixture_eta':(target-s0)/(bright_mean-s0)}

spectral=[]; bands=[]; enclosures=[]; mean_rows=[]; tails=[]
v_star=(2+math.sqrt(3))/(3*math.sqrt(3))
for side in [6,8,12,16,24,32,64]:
    s,w=modes(side); volume=side**3
    v=float(np.sum(w)); a=float(np.sum(w/s)); inv2=float(np.sum(w/s**2))
    s0=2*math.sin(math.pi/side)
    assert abs(float(np.min(s))-s0)<2e-15
    assert abs(v-float(np.sum(s))/(3*volume))<2e-14
    assert abs(a-(volume-1)/(3*volume))<2e-14
    assert abs(float(np.dot(s,w))-2)<2e-14
    lower_v=2/(math.sqrt(3)*side)/math.tan(math.pi/(2*side))
    assert v >= lower_v-2e-14 and v <= math.sqrt(6)/3+2e-14
    assert lower_v >= v_star-2e-14
    m=side//2
    harmonic_sum=sum(1/j for j in range(1,m+1))
    inverse2_bound=(12*m*(m+1)+2*harmonic_sum)/(12*side**2)
    assert inv2 <= inverse2_bound+2e-14
    lowest=abs(s-s0)<1e-10
    low_weight=float(np.sum(w[lowest]))
    assert int(np.count_nonzero(lowest))==6
    assert abs(low_weight-2*s0/volume)<2e-14
    spectral.append({'L':side,'V':volume,'complex_nonzero_momenta':len(s),
       'real_transverse_oscillators':2*len(s),'lowest_s':s0,
       'lowest_shell_real_oscillators':12,'v_local':v,'v_lower_L':lower_v,
       'v_uniform_lower':v_star,'v_upper':math.sqrt(6)/3,
       'sum_d_squared_over_s':a,'sum_d_squared_times_s':float(np.dot(s,w)),
       'sum_d_squared_over_s_squared':inv2,'inverse2_uniform_shell_bound':inverse2_bound,
       'lowest_shell_weight':low_weight,'lowest_shell_exact_weight':2*s0/volume,
       'bright_mean_s':2/v})
    for ceiling in [0.5*s0,1.005*s0,0.61,0.93,1.17,1.61,2.43,3.6]:
        keep=s<=ceiling
        vb=float(np.sum(w[keep]))
        invariant=float(np.sum(s[keep]))/(3*volume)
        assert abs(vb-invariant)<2e-14
        gap_empty=ceiling<s0
        if gap_empty: assert vb == 0
        count_bound=ceiling/(3*volume)*((2*math.floor(side*math.asin(min(ceiling/2,1))/math.pi)+1)**3-1) if ceiling<2 else None
        if count_bound is not None: assert vb<=count_bound+2e-14
        fourth=ceiling**4/24 if ceiling<=1 else None
        if fourth is not None: assert vb<=fourth+2e-14
        bands.append({'L':side,'s_ceiling':ceiling,'band_empty':gap_empty,
            'normalized_one_particle_state_feasible':not gap_empty,
            'momenta_in_band':int(np.count_nonzero(keep)),'v_band':vb,
            'eta_max':None if gap_empty else vb/v,
            'limiting_ratio_max':None if gap_empty else 1+2*vb/v,
            'count_upper_v_band':count_bound,'uniform_fourth_power_upper_v_band':fourth})
    mesh=math.sqrt(3)*math.pi/side
    for ceiling in [0.51,0.83,1.13]:
        if not (mesh<ceiling and ceiling+mesh<2): continue
        r=ceiling-mesh; R=2*math.asin((ceiling+mesh)/2)
        low=max(0,(r**4-r**6/36-4*mesh*r**3/3)/(24*math.pi**2))
        upper=(R**4+4*mesh*R**3/3)/(24*math.pi**2)
        vb=float(np.sum(w[s<=ceiling]))
        assert low<=vb+2e-14 and vb<=upper+2e-14
        enclosures.append({'L':side,'s_ceiling':ceiling,'cell_radius':mesh,
          'v_band':vb,'rigorous_formula_lower':low,'rigorous_formula_upper':upper,
          'continuum_leading_expression':ceiling**4/(24*math.pi**2)})
    if side in [6,16,32]:
        bright=2/v
        for fraction in [0.1,0.5,0.9]:
            row=profile(s,w,s0+fraction*(bright-s0));row['L']=side;mean_rows.append(row)
    if side in [16,32,64]:
        ceiling={16:.8,32:.4,64:.2}[side]
        # Add an orthogonal lowest-energy dark vector; its d component is zero.
        bright=2/v; probability=(ceiling-s0)/(bright-s0)
        mean=(1-probability)*s0+probability*bright
        eta=probability
        band_eta=float(np.sum(w[s<=ceiling]))/v
        assert abs(mean-ceiling)<2e-15 and eta>band_eta
        assert eta>ceiling**4/(24*v)
        tail_probability=probability*float(np.sum(w[s>ceiling]))/v
        assert tail_probability>0
        # A second constructive mixture uses S^{-1}d and approaches the CS slope.
        zeta_mean=a/inv2
        zeta_probability=(ceiling-s0)/(zeta_mean-s0)
        zeta_eta=zeta_probability*a*a/(inv2*v)
        assert eta<=ceiling*a/v+2e-14 and zeta_eta<=ceiling*a/v+2e-14
        tails.append({'L':side,'mean_ceiling':ceiling,'lowest_s':s0,
          'bright_tail_weight':probability,'attained_mean':mean,'eta':eta,
          'hard_band_eta_max_at_same_ceiling':band_eta,
          'hard_band_fourth_power_bound_inapplicable_to_mean_constraint':ceiling**4/(24*v),
          'probability_of_energy_above_mean_ceiling':tail_probability,
          'mean_constraint_CS_bound':ceiling*a/v,
          'inverse_energy_bright_mixture_eta':zeta_eta})

s_real,w_real,eigenvalues,curl=direct_curl(6)
s_fourier,w_fourier=modes(6)
expected=np.sort(np.repeat(s_fourier**2,2))
spectral_error=float(np.max(abs(np.sort(s_real**2)-expected)))
assert len(s_real)==2*(6**3-1)==430
assert spectral_error<3e-13
v_error=abs(float(np.sum(w_real))-float(np.sum(w_fourier)))
inv_error=abs(float(np.sum(w_real/s_real))-float(np.sum(w_fourier/s_fourier)))
assert max(v_error,inv_error)<3e-13
mean_check=[]
bright=2/float(np.sum(w_fourier));s0=float(np.min(s_fourier))
for fraction in [.1,.5,.9]:
    target=s0+fraction*(bright-s0)
    real=profile(s_real,w_real,target); fourier=profile(s_fourier,w_fourier,target)
    delta=abs(real['eta']-fourier['eta']);assert delta<3e-12
    mean_check.append({'fraction':fraction,'real_eta':real['eta'],'Fourier_eta':fourier['eta'],'difference':delta})
direct={'L':6,'curl_shape':list(curl.shape),'integer_row_norm_squared':float(np.dot(curl[0],curl[0])),
        'zero_eigenvalues':int(np.count_nonzero(abs(eigenvalues)<1e-10)),
        'positive_eigenvalues':len(s_real),'max_squared_frequency_error':spectral_error,
        'real_vs_Fourier_v_error':v_error,'real_vs_Fourier_inverse_weight_error':inv_error,
        'mean_optimization_comparisons':mean_check}

SI=[]; example_gaps=[]
with localcontext() as ctx:
    ctx.prec=85
    D=Decimal
    pi=D('3.141592653589793238462643383279502884197169399375105820974944592307816406286208998628034825342117068')
    h=D('6.62607015e-34');c=D('299792458');charge=D('1.602176634e-19')
    hbar_eVs=h/(2*pi*charge)
    vstar=(2+D(3).sqrt())/(3*D(3).sqrt())
    s16=(2-(2+D(2).sqrt()).sqrt()).sqrt()
    for label,EminGeV in [('MAGIC_Table6_systematics','5.9e10'),('LHAASO_v2_ML_MINOS','6.9e11')]:
        Emin=D(EminGeV)*D(10)**9
        amax=6*hbar_eVs*c/Emin
        for Eopt in [D(1),D(2),D(3)]:
            argument=3*Eopt/Emin
            # Positive arcsin series; omitted O(argument^7) is negligible here.
            arcsin=argument+argument**3/6+3*argument**5/40
            threshold=pi/arcsin
            ceiling=6*Eopt/Emin
            SI.append({'benchmark':label,'E_QG_lower_GeV':EminGeV,'illustrative_optical_energy_eV':str(Eopt),
              'necessary_spacing_upper_m':str(amax),'necessary_L_strict_lower_rounded':str(threshold),
              'necessary_site_count_strict_lower_rounded':str(threshold**3),
              'continuum_wavelength_hc_over_E_m':str(h*c/(charge*Eopt)),
              'dimensionless_reference_energy_ceiling_upper':str(ceiling),
              'hard_band_limiting_ratio_excess_upper':str(ceiling**4/(12*vstar)),
              'mean_energy_limiting_ratio_excess_upper':str(2*ceiling/(3*vstar)),
              'scope':'Conditional necessary SI bounds; not selected parameters, charged-spectrum gaps, finite-g accuracy or empirical exclusion.'})
        for side,smin in [(6,D(1)),(16,s16)]:
            example_gaps.append({'benchmark':label,'L':side,
                'necessary_reference_gap_lower_eV':str(Emin*smin/6)})

result={'scope':'Independent static finite-volume spectral identities, pure-packet energy-constraint optimization and conditional SI arithmetic. No full dynamics or author code.',
 'environment':{'python':platform.python_version(),'numpy':np.__version__},
 'direct_real_curl':direct,'spectral_rows':spectral,'hard_band_rows':bands,
 'finite_volume_enclosure_rows':enclosures,'exact_mean_constraint_rows':mean_rows,
 'mean_tail_counterexamples_to_band_substitution':tails,'SI_rows':SI,
 'small_graph_reference_gap_rows':example_gaps,
 'arithmetic_limits':'Floating spectral controls are not interval enclosures. Decimal SI rows are rounded arithmetic using 85 digits and a stated pi literal, not statistical precision.',
 'author_or_parent_runners_executed':0,
 'source_sha256':hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
 'elapsed_seconds':time.perf_counter()-START,
 'completed_utc':datetime.datetime.now(datetime.timezone.utc).isoformat()}
data=json.dumps(result,indent=2,allow_nan=False)+'\n'
(HERE/'CONTROL_RESULTS.json').write_text(data)
print(data,end='')
