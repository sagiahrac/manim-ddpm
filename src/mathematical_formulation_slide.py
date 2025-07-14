from manim import *
from .base import DDPMBaseMixin

class MathematicalFormulationSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        
        # Title
        title = Text("Mathematical Foundation", 
                    font="TeX Gyre Termes", font_size=36, color="#DDA0DD")
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # Key equations with explanations
        equations = VGroup()
        
        # Forward process equation
        eq1_title = Text("Forward Process:", font_size=24, color="#FFD700")
        eq1 = MathTex(r"x_t = \sqrt{\bar{\alpha}_t} x_0 + \sqrt{1-\bar{\alpha}_t} \varepsilon")
        eq1.set_color("#87CEEB")
        
        # Loss function
        eq2_title = Text("Training Objective:", font_size=24, color="#FFD700")
        eq2 = MathTex(r"L = \mathbb{E}_{t,x_0,\varepsilon} \left[ ||\varepsilon - \varepsilon_\theta(x_t, t)||^2 \right]")
        eq2.set_color("#FF6B6B")
        
        # Sampling
        eq3_title = Text("Sampling:", font_size=24, color="#FFD700")
        eq3 = MathTex(r"x_{t-1} = \frac{1}{\sqrt{\alpha_t}} \left( x_t - \frac{\beta_t}{\sqrt{1-\bar{\alpha}_t}} \varepsilon_\theta(x_t, t) \right) + \sigma_t z")
        eq3.set_color("#90EE90")
        
        # Arrange equations
        for i, (title, eq) in enumerate([(eq1_title, eq1), (eq2_title, eq2), (eq3_title, eq3)]):
            eq_group = VGroup(title, eq)
            eq_group.arrange(DOWN, buff=0.3)
            equations.add(eq_group)
        
        equations.arrange(DOWN, buff=0.8)
        equations.move_to(ORIGIN)
        
        # Animate each equation
        for eq_group in equations:
            self.play(
                Write(eq_group[0]),
                Write(eq_group[1]),
                run_time=2
            )
            self.wait(1)
        
        self.wait(2)
