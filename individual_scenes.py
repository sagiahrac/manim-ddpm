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
"""

from manim import *
from ddpm_manim import TitleSlide, DiffusionIntroSlide, ProcessOverviewSlide, IntuitionSlide, ForwardDiffusionSlide, ReverseDenoisingSlide, MathematicalFormulationSlide, TrainingProcessSlide

# Create proper scene classes for individual rendering
class TitleSlideScene(TitleSlide):
    pass

class DiffusionIntroSlideScene(DiffusionIntroSlide):
    pass

class ProcessOverviewSlideScene(ProcessOverviewSlide):
    pass

class IntuitionSlideScene(IntuitionSlide):
    pass

class ForwardDiffusionSlideScene(ForwardDiffusionSlide):
    pass

class ReverseDenoisingSlideScene(ReverseDenoisingSlide):
    pass

class MathematicalFormulationSlideScene(MathematicalFormulationSlide):
    pass

class TrainingProcessSlideScene(TrainingProcessSlide):
    pass
