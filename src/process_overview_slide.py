from manim import *
from .base import DDPMBaseMixin

class ProcessOverviewSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        
        # Title
        title = Text("Forward & Reverse Processes", 
                    font="TeX Gyre Termes", font_size=40, color="#DDA0DD")
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        
        # Create a visual representation of the forward process
        # Start with a clean image representation
        original_image = self.create_image_representation(BLUE, opacity=1.0, size=1.0)
        original_image.move_to(LEFT * 5)
        
        # Create progressively noisier versions
        positions = [LEFT * 2.5, ORIGIN, RIGHT * 2.5, RIGHT * 5]
        noise_levels = [0.3, 0.6, 0.9, 1.0]
        
        noisy_images = []
        for i, (pos, noise) in enumerate(zip(positions, noise_levels)):
            img = self.create_noisy_image(noise, size=1.0)
            img.move_to(pos)
            noisy_images.append(img)
        
        # Labels
        x0_label = MathTex("x_0", font_size=20, color=WHITE)
        x0_label.next_to(original_image, DOWN, buff=0.2)
        
        noise_labels = []
        for i, img in enumerate(noisy_images):
            label = MathTex(f"x_{{{i+1}}}", font_size=20, color=WHITE)
            label.next_to(img, DOWN, buff=0.2)
            noise_labels.append(label)
        
        # Show original image
        self.play(FadeIn(original_image), Write(x0_label))
        
        # Forward process arrows and noise addition
        forward_arrows = []
        for i, (img, label) in enumerate(zip(noisy_images, noise_labels)):
            if i == 0:
                start_pos = original_image.get_right() + RIGHT * 0.1
            else:
                start_pos = noisy_images[i-1].get_right() + RIGHT * 0.1
            
            end_pos = img.get_left() + LEFT * 0.1
            arrow = Arrow(start_pos, end_pos, color="#FF6B6B", stroke_width=3)
            forward_arrows.append(arrow)
            
            # Add noise symbol above arrow
            noise_symbol = MathTex(r"+\varepsilon", font_size=16, color="#FF6B6B")
            noise_symbol.next_to(arrow, UP, buff=0.1)
            
            self.play(
                Create(arrow),
                Write(noise_symbol),
                FadeIn(img),
                Write(label),
                run_time=1.2
            )
        
        # Add "Forward Process" label
        forward_label = Text("Forward Process", font_size=24, color="#FF6B6B")
        forward_label.move_to(UP * 1.5)
        self.play(Write(forward_label))
        
        self.wait(1)
        
        # Now show the reverse process
        # Create reverse arrows
        reverse_arrows = []
        for i in range(len(noisy_images)):
            if i == len(noisy_images) - 1:
                start_pos = noisy_images[i].get_left() + LEFT * 0.1
                end_pos = noisy_images[i-1].get_right() + RIGHT * 0.1
            elif i == 0:
                start_pos = noisy_images[i].get_left() + LEFT * 0.1
                end_pos = original_image.get_right() + RIGHT * 0.1
            else:
                start_pos = noisy_images[i].get_left() + LEFT * 0.1
                end_pos = noisy_images[i-1].get_right() + RIGHT * 0.1
            
            arrow = Arrow(start_pos, end_pos, color="#90EE90", stroke_width=3)
            reverse_arrows.append(arrow)
            
            # Add denoising symbol
            denoise_symbol = MathTex(r"-\varepsilon", font_size=16, color="#90EE90")
            denoise_symbol.next_to(arrow, DOWN, buff=0.1)
            
            self.play(
                Create(arrow),
                Write(denoise_symbol),
                run_time=0.8
            )
        
        # Add "Reverse Process" label
        reverse_label = Text("Reverse Process (Denoising)", font_size=24, color="#90EE90")
        reverse_label.move_to(DOWN * 2)
        self.play(Write(reverse_label))
        
        # Highlight the key insight with a box around the reverse process
        highlight_box = SurroundingRectangle(
            VGroup(*reverse_arrows), 
            color="#90EE90", 
            stroke_width=2,
            buff=0.3
        )
        self.play(Create(highlight_box))
        
        # Add final insight
        insight = Text("Learn to reverse the noise!", 
                      font_size=28, color="#FFD700", weight=BOLD)
        insight.move_to(DOWN * 3.2)
        self.play(Write(insight))
        
        self.wait(2)
