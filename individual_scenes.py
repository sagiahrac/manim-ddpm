"""
Individual scene files for running specific slides of the DDPM presentation.
This allows you to render individual slides instead of the full presentation.

Usage examples:
- manim individual_scenes.py TitleSlideScene -ql
- manim individual_scenes.py DiffusionIntroSlideScene -ql
- manim individual_scenes.py ProcessOverviewSlideScene -ql
- manim individual_scenes.py IntuitionSlideScene -ql
- manim individual_scenes.py ForwardDiffusionSlideScene -ql
- manim individual_scenes.py ReverseDenoisingSlideScene -ql
- manim individual_scenes.py MathematicalFormulationSlideScene -ql
- manim individual_scenes.py TrainingProcessSlideScene -ql
- manim individual_scenes.py CelebAHQDemoSlideScene -ql
- manim individual_scenes.py DDPMInnovationSlideScene -ql
"""

from manim import *
from src import *
from src.three_gaussians_3d import ThreeGaussians3D
from src.chairs_zoom_slide import ChairsZoomSlide


# Create proper scene classes for individual rendering
class A_TitleSlideScene(TitleSlide):
    pass


class B_DiffusionIntroSlideScene(DiffusionIntroSlide):
    pass


class C_CelebAHQDemoSlideScene(CelebAHQDemoSlide):
    pass


class D_DDPMInnovationSlideScene(DDPMInnovationSlide):
    pass


class ProcessOverviewSlideScene(ProcessOverviewSlide):
    pass


class ForwardDiffusionSlideScene(ForwardDiffusionSlide):
    pass


class ReverseDenoisingSlideScene(ReverseDenoisingSlide):
    pass

class DensityEvolutionSlideScene(DensityEvolutionSlide):
    pass

class ThreeGaussians3DScene(ThreeGaussians3D):
    pass

class ChairsZoomSlideScene(ChairsZoomSlide):
    pass

class BackwardTransitionSlideScene(BackwardTransitionSlide):
    pass