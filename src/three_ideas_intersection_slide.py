from manim import *
from .base import DDPMBaseMixin

class ThreeIdeasIntersectionSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        self.add_sound("media/videos/individual_scenes/1080p60/H_ThreeIdeasIntersectionSlideScene-enhanced-v2.wav")
        self.wait(7)
        # Central DDPM
        ddpm_text = Text("DDPM", font_size=48, color=YELLOW, weight=BOLD)
        ddpm_text.move_to(ORIGIN + 0.5 * DOWN)
        
        # Create a hexagon around DDPM for emphasis
        ddpm_background = RegularPolygon(6, radius=1.2, color=YELLOW, fill_opacity=0.1, stroke_width=3)
        ddpm_background.move_to(ORIGIN + 0.5 * DOWN)
        
        # Position the three ideas around DDPM
        # Variational Inference - top
        vi_box = RoundedRectangle(width=2.5, height=1.25, corner_radius=0.3, color=BLUE, fill_opacity=0.2, stroke_width=2)
        vi_text = Paragraph("ELBO\nMaximization", font_size=24, color=BLUE, weight=BOLD, alignment="center")
        vi_text.move_to(vi_box.get_center())
        vi_group = VGroup(vi_box, vi_text)
        vi_group.move_to(UP * 2)
        
        # ELBO - bottom left
        elbo_box = RoundedRectangle(width=2.5, height=1.25, corner_radius=0.3, color=GREEN, fill_opacity=0.2, stroke_width=2)
        elbo_text = Paragraph("Langevin\nDynamics", font_size=24, color=GREEN, weight=BOLD, alignment="center")
        elbo_text.move_to(elbo_box.get_center())
        elbo_group = VGroup(elbo_box, elbo_text)
        elbo_group.move_to(DOWN * 2 + LEFT * 3)
        
        # Score-based - bottom right
        score_box = RoundedRectangle(width=2.5, height=1.25, corner_radius=0.3, color=RED, fill_opacity=0.2, stroke_width=2)
        score_text = Paragraph("Denoising Score\nMatching", font_size=24, color=RED, weight=BOLD, alignment="center")
        score_text.move_to(score_box.get_center())
        score_group = VGroup(score_box, score_text)
        score_group.move_to(DOWN * 2 + RIGHT * 3)
        
        # Create arrows pointing TO DDPM - three ideas converging
        arrow_vi = Arrow(
            start=vi_group.get_bottom() + 0.15 * UP,
            end=ddpm_background.get_top() + 0.15 * DOWN,
            color=BLUE,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.4
        )
        
        arrow_elbo = Arrow(
            start=elbo_group.get_right(),
            end=(ddpm_background.get_left() + ddpm_background.get_bottom()) / 2,
            color=GREEN,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        arrow_elbo.shift(LEFT * 0.1)
        
        arrow_score = Arrow(
            start=score_group.get_left(),
            end=(ddpm_background.get_right() + ddpm_background.get_bottom()) / 2,
            color=RED,
            stroke_width=4,
            max_tip_length_to_length_ratio=0.25
        )
        arrow_score.shift(RIGHT * 0.1)
        
        # Animate the three ideas appearing
        self.play(
            FadeIn(vi_group),
            run_time=1
        )
        self.wait(13)

        self.play(
            FadeIn(score_group),
            run_time=1
        )
        self.wait(16)
        
        self.play(
            FadeIn(elbo_group),
            run_time=1
        )
        self.wait(10)
        
        # Show arrows pointing to center
        self.play(
            GrowArrow(arrow_vi),
            GrowArrow(arrow_elbo),
            GrowArrow(arrow_score),
            run_time=2
        )
        self.wait(1)
        
        # Show DDPM in the center
        self.play(
            GrowFromCenter(ddpm_background),
            Write(ddpm_text),
            run_time=2
        )

        self.wait(12)

        # Final emphasis
        self.play(
            ddpm_text.animate.scale(1.2),
            ddpm_background.animate.set_stroke(width=5),
            run_time=1
        )

        self.play(
            ddpm_text.animate.scale(1 / 1.2),
            ddpm_background.animate.set_stroke(width=5),
            run_time=1
        )
        
        self.play(
            FadeOut(VGroup(ddpm_text, ddpm_background, vi_group, elbo_group, score_group, arrow_vi, arrow_elbo, arrow_score)),
            run_time=2
        )

class ThreeIdeasIntersectionSlideScene(ThreeIdeasIntersectionSlide):
    """Scene wrapper for individual_scenes.py"""
    pass
