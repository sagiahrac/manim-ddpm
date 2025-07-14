from manim import *
from .base import DDPMBaseMixin

class IntuitionSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        
        # Title
        title = Text("The Core Idea", font="TeX Gyre Termes", font_size=40, color="#FFD700")
        title.to_edge(UP, buff=1)
        self.play(Write(title))
        
        # Create intuitive explanation with visual metaphor
        explanation = VGroup()
        
        line1 = Text("Imagine slowly adding noise to an image...", 
                    font_size=28, color=WHITE)
        line2 = Text("...until it becomes pure noise", 
                    font_size=28, color=WHITE)
        line3 = Text("Then learn to reverse this process", 
                    font_size=28, color="#87CEEB")
        
        explanation.add(line1, line2, line3)
        explanation.arrange(DOWN, buff=0.5)
        explanation.move_to(ORIGIN)
        
        for line in explanation:
            self.play(Write(line), run_time=1.2)
            self.wait(0.5)
        
        self.wait(2)
