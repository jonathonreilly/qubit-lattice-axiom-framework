"""Same-model controls for cancellation; no physical-fit or asymptotic claim."""
import importlib.util
import math
from pathlib import Path
import unittest
from unittest.mock import patch

import numpy as np
from numpy.polynomial.legendre import leggauss
from scipy.special import erf

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "nnlo_saddle", ROOT / "scripts/lattice_nn_rescaled_C_arm_NNLO_saddle.py"
)
saddle = importlib.util.module_from_spec(spec)
spec.loader.exec_module(saddle)


def direct_aperture_moments(h, order, grid_size=6001):
    """Direct integral, independent of erf completion-of-square evaluation.

    Freeze the same supplied harness, integrate aperture [3,5], and cancel
    exp(-9/(4 alpha_pre)) analytically before squaring/normalizing. Doubling
    aperture order and refining the detector grid check the finite fixture.
    """
    c = math.exp(-0.8 * math.pi**2 / 16)
    a0 = np.exp(5j * h) / math.sqrt(3)
    apm = c * np.exp(5j * h * math.sqrt(2)) / math.sqrt(6)
    s = apm / (a0 + 2 * apm)
    pre, post = (40 / 3) * s * h, (80 / 3) * s * h
    z, w = leggauss(order)
    t = z + 1  # y_slit = 3+t, 0<=t<=2
    y = np.linspace(-5, 13, grid_size)
    amplitude = np.exp(
        -(6*t + t*t)[None, :] / (4*pre)
        - (y[:, None] - 3 - t[None, :])**2 / (4*post)
    ) @ w
    p = np.abs(amplitude)**2
    p /= np.sum(p)
    mean = p @ y
    sigma = math.sqrt(p @ ((y - mean)**2))
    return mean, sigma


class SaddleNumericsTests(unittest.TestCase):
    def test_same_model_direct_integral_and_convergence(self):
        for h in (0.25, 0.125, 0.0625, 0.03125, 0.015625, 0.0078125):
            with self.subTest(h=h):
                coarse = direct_aperture_moments(h, 90, 3001)
                fine = direct_aperture_moments(h, 180, 6001)
                np.testing.assert_allclose(coarse, fine, rtol=0, atol=2e-9)
                np.testing.assert_allclose(saddle.slit_arm_moments(h), fine,
                                           rtol=0, atol=5e-9)

    def test_old_subtraction_fails_known_fine_point(self):
        reference = direct_aperture_moments(1/64, 180)[1]
        self.assertAlmostEqual(reference, 0.311512595478453, places=12)
        self.assertAlmostEqual(saddle.slit_arm_moments(1/64)[1], reference, places=12)
        # In the erfc difference, -erf restores the old cancellation-prone
        # expression erf(u_b)-erf(u_a), without changing other model code.
        with patch.object(saddle, "scipy_erfc", side_effect=lambda z: -erf(z)):
            old_sigma = saddle.slit_arm_moments(1/64)[1]
        self.assertGreater(abs(old_sigma/reference - 1), 0.05)

    def test_original_fit_window_is_preserved(self):
        self.assertEqual(saddle.FIT_HS, (0.25, 0.125, 0.0625, 0.03125))
        direct_sigmas = [direct_aperture_moments(h, 180)[1] for h in saddle.FIT_HS]
        independent_slope = np.polyfit(np.log(saddle.FIT_HS), np.log(direct_sigmas), 1)[0]
        slope, _ = saddle.loglog_fit(saddle.FIT_HS, saddle.sigma_pred_NNLO_full)
        self.assertAlmostEqual(slope, independent_slope, places=8)
        self.assertAlmostEqual(slope, 0.52469477, places=7)


if __name__ == "__main__":
    unittest.main()
