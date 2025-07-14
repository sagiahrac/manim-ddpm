from manim import *
from .base import DDPMBaseMixin

class TrainingProcessSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        
        # Title
        title = Text("Training Overview", 
                    font="TeX Gyre Termes", font_size=36, color="#FF9500")
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # Training steps
        steps = VGroup()
        
        step_texts = [
            "1. Take a clean image x₀",
            "2. Sample random timestep t",
            "3. Add noise to get xₜ",
            "4. Train network to predict the noise",
            "5. Repeat for millions of examples"
        ]
        
        colors = [WHITE, "#87CEEB", "#FF6B6B", "#90EE90", "#FFD700"]
        
        for i, (text, color) in enumerate(zip(step_texts, colors)):
            step = Text(text, font_size=24, color=color)
            steps.add(step)
        
        steps.arrange(DOWN, buff=0.5)
        steps.move_to(ORIGIN)
        
        # Animate steps appearing
        for step in steps:
            self.play(Write(step), run_time=1.2)
            self.wait(0.5)
        
        # Final message
        self.wait(1)
        final_msg = Text("Result: A generative model that can create new images!",
                        font="TeX Gyre Termes", font_size=28, color="#FFD700", weight=BOLD)
        final_msg.to_edge(DOWN, buff=1)
        self.play(Write(final_msg), run_time=2)
        
        self.wait(3)
