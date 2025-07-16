from manim import *
from .base import DDPMBaseMixin

class ProcessOverviewSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        
        # Title
        title = Text("How Diffusion Models Work", 
                    font="TeX Gyre Termes", font_size=40, color="#DDA0DD")
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(1)
        
        # Load the corgi image
        try:
            corgi_img = ImageMobject("media/images/corgi.png")
            corgi_img.scale(0.1)  # Made even smaller
        except:
            # Fallback to colored square if image not found
            corgi_img = Square(side_length=0.6, fill_color=ORANGE, fill_opacity=0.8)
        
        # Calculate equal spacing for 4 images centered on screen
        # Assuming each image is about 1.2 units wide (0.2 scale * ~6 unit original width)
        # We want equal gaps between images and from edges
        image_width = 1.2  # Approximate width of scaled corgi image
        total_images = 4
        screen_width = 12  # Approximate usable screen width (-6 to +6)
        
        # Calculate spacing: total_width = (images * image_width) + (gaps * gap_width)
        # We want 5 gaps (before first, between images, after last) to be equal
        total_image_width = total_images * image_width
        available_gap_space = screen_width - total_image_width
        gap_width = available_gap_space / 5  # 5 equal gaps
        
        # Calculate positions: start from left edge + first gap + half image width
        start_x = -screen_width/2 + gap_width + image_width/2
        spacing = image_width + gap_width
        
        corgi_img.move_to([start_x, 0, 0])
        
        # Mathematical label for original image (DDPM style)
        original_label = MathTex("x_0", font_size=24, color=WHITE)
        original_label.next_to(corgi_img, DOWN, buff=0.3)
        
        self.play(FadeIn(corgi_img), Write(original_label))
        self.wait(0.5)
        
        # Forward Process: Progressive noise addition
        forward_label = Text("Forward Process: Adding Noise", 
                           font_size=26, color="#FF6B6B", weight=BOLD)
        forward_label.to_edge(DOWN, buff=2)
        self.play(Write(forward_label))
        
        # Create sequence of increasingly noisy versions (DDPM paper style)
        images = [corgi_img]
        # Calculate remaining 3 positions with equal spacing
        positions = [
            [start_x + spacing, 0, 0],      # x₁ position  
            [start_x + 2*spacing, 0, 0],   # x₂ position
            [start_x + 3*spacing, 0, 0]    # xₜ position
        ]
        noise_levels = [0.3, 0.6, 1.0]  # 3 steps: light noise, medium noise, pure noise
        math_labels = ["x_1", "x_2", "x_T"]  # DDPM style mathematical labels
        
        for i, (pos, noise_level, math_label) in enumerate(zip(positions, noise_levels, math_labels)):
            # Create a noisy version by overlaying noise dots
            noisy_group = Group()  # Changed from VGroup to Group
            
            # Base image (getting more transparent)
            try:
                base_img = ImageMobject("media/images/corgi.png")
                base_img.scale(0.1)
                base_img.set_opacity(1 - noise_level * 0.8)  # Fade out as noise increases
            except:
                base_img = Square(side_length=0.6, fill_color=ORANGE, fill_opacity=0.8 * (1 - noise_level))
            
            noisy_group.add(base_img)
            
            # Add noise dots positioned relative to the base image
            num_noise_dots = int(noise_level * 80)  # Reduced from 100 to 80
            for _ in range(num_noise_dots):
                # Get the image bounds to place noise within the image area
                img_center = base_img.get_center()
                img_width = base_img.width * 0.8  # Use 80% of image width for noise area
                img_height = base_img.height * 0.8  # Use 80% of image height for noise area
                
                noise_dot = Dot(
                    point=[
                        img_center[0] + np.random.uniform(-img_width/2, img_width/2),
                        img_center[1] + np.random.uniform(-img_height/2, img_height/2),
                        0
                    ],
                    radius=0.015,  # Slightly smaller dots
                    color=interpolate_color(WHITE, RED, np.random.random())
                )
                noisy_group.add(noise_dot)
            
            noisy_group.move_to(pos)
            
            # DDPM-style mathematical label
            step_label = MathTex(math_label, font_size=24, color=WHITE)
            step_label.next_to(noisy_group, DOWN, buff=0.3)
            
            # DDPM-style arrow with q(x_t|x_{t-1}) notation
            start_point = images[-1].get_right() + RIGHT * 0.3
            end_point = noisy_group.get_left() + LEFT * 0.3
            
            arrow = Arrow(
                start_point,
                end_point,
                color="#FF6B6B",
                stroke_width=4,
                buff=0,
                tip_length=0.2
            )
            
            # Mathematical transition notation (DDPM paper style)
            if i < len(noise_levels) - 1:
                transition_label = MathTex(r"q(x_{t+1}|x_t)", font_size=16, color="#FF6B6B")
            else:
                transition_label = MathTex(r"q(x_T|x_{T-1})", font_size=16, color="#FF6B6B")
            
            arrow_center = (start_point + end_point) / 2
            transition_label.move_to(arrow_center + UP * 0.4)
            
            # Animate the forward step
            self.play(
                FadeIn(noisy_group, scale=0.8),
                Write(step_label),
                run_time=0.8
            )
            
            # Add arrow and transition notation after the image (so they appear on top)
            self.play(
                Create(arrow),
                Write(transition_label),
                run_time=0.6
            )
            
            images.append(noisy_group)
            self.wait(0.3)
        
        # Final noise label (DDPM style)
        pure_noise_label = MathTex(r"x_T \sim \mathcal{N}(0, I)", font_size=20, color="#FF6B6B")
        pure_noise_label.next_to(images[-1], DOWN, buff=0.8)
        self.play(Write(pure_noise_label))
        
        self.wait(2)
            
        #     # Add arrow and transition notation after the image (so they appear on top)
        #     self.play(
        #         Create(arrow),
        #         Write(transition_label),
        #         run_time=0.6
        #     )
            
        #     images.append(noisy_group)
        #     self.wait(0.3)
        
        # # Final noise label
        # pure_noise_label = Text("Pure Noise", font_size=20, color="#FF6B6B")
        # pure_noise_label.next_to(images[-1], DOWN, buff=0.6)
        # self.play(Write(pure_noise_label))
        
        # self.wait(1)
        
        # # Clear forward process labels
        # self.play(FadeOut(forward_label))
        
        # # Visual: "learning to reverse this process to generate new, high-quality data"
        # reverse_label = Text("Reverse Process: Learning to Denoise", 
        #                    font_size=28, color="#90EE90", weight=BOLD)
        # reverse_label.to_edge(DOWN, buff=2)
        # self.play(Write(reverse_label))
        
        # # Show reverse arrows (conceptual - denoising back to clean image)
        # reverse_arrows = []
        # for i in range(len(positions)-1, -1, -1):
        #     if i == 0:
        #         target = corgi_img
        #         arrow_color = "#90EE90"
        #     else:
        #         target = images[i]
        #         arrow_color = "#90EE90"
            
        #     if i < len(positions) - 1:
        #         reverse_arrow = Arrow(
        #             images[i+1].get_left() + LEFT*0.1,
        #             target.get_right() + RIGHT*0.1,
        #             color=arrow_color,
        #             stroke_width=3
        #         )
                
        #         # Denoise symbol
        #         denoise_symbol = Text("-noise", font_size=16, color="#90EE90")
        #         denoise_symbol.next_to(reverse_arrow, DOWN, buff=0.1)
                
        #         reverse_arrows.append(VGroup(reverse_arrow, denoise_symbol))
        
        # # Animate reverse arrows
        # for arrow_group in reverse_arrows:
        #     self.play(Create(arrow_group), run_time=0.8)
        
        # # Show the key insight
        # key_insight = Text("Neural Network Learns This Reverse Process!", 
        #                   font_size=28, color="#FFD700", weight=BOLD)
        # key_insight.move_to(UP * 2.5)
        
        # self.play(Write(key_insight))
        
        # # Final transformation illustration
        # transformation = VGroup()
        
        # # Random noise
        # random_noise = Text("Random\nNoise", font_size=20, color="#FF6B6B", weight=BOLD)
        # random_noise.move_to(LEFT * 2 + UP * 1.8)
        
        # # Arrow
        # transform_arrow = Arrow(LEFT*0.8 + UP*1.8, RIGHT*0.8 + UP*1.8, color="#FFD700", stroke_width=4)
        
        # # Generated corgi
        # generated_text = Text("Generated\nCorgi!", font_size=20, color="#90EE90", weight=BOLD)
        # generated_text.move_to(RIGHT * 2 + UP * 1.8)
        
        # transformation.add(random_noise, transform_arrow, generated_text)
        
        # self.play(FadeIn(transformation), run_time=2)
        
        # self.wait(3)
