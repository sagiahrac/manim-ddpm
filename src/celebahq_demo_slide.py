from manim import *
from .base import DDPMBaseMixin

class CelebAHQDemoSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()
        
        # Title
        title = Text("DDPM Results on CelebA-HQ", 
                    font="TeX Gyre Termes", font_size=40, color="#DDA0DD")
        title.to_edge(UP, buff=0.8)
        self.play(Write(title))
        self.wait(1)
        
        # Load the concatenated image
        try:
            # Load the full image first
            full_img = ImageMobject("media/images/celebahq_combined_6.png")
            full_img.scale_to_fit_height(5)  # Scale to fit nicely
            full_img.move_to(ORIGIN)
            
            # Show the full concatenated image briefly
            description = Text("Generated faces using DDPM (2×3 grid)", 
                             font_size=24, color="#87CEEB")
            description.to_edge(DOWN, buff=1)
            
            self.play(FadeIn(full_img), Write(description))
            self.wait(2)
            
            # Fade out description
            self.play(FadeOut(description))
            
            # Now create individual slices
            # The image is 2×3 grid, so we need to create 6 individual slices
            slice_labels = [
                "Sample 1", "Sample 2", "Sample 3", 
                "Sample 4", "Sample 5", "Sample 6"
            ]
            
            # Show each slice individually with smooth crossfade
            for i in range(6):
                # Create the slice image (same source, but we'll position it)
                slice_img = ImageMobject("media/images/celebahq_combined_6.png")
                slice_img.scale_to_fit_height(5)
                slice_img.move_to(ORIGIN)
                
                # Create label for this slice
                slice_label = Text(slice_labels[i], 
                                 font_size=24, color="#FFD700", weight=BOLD)
                slice_label.to_edge(DOWN, buff=0.8)
                
                if i == 0:
                    # First slice: fade out full image, fade in first slice
                    self.play(
                        FadeOut(full_img),
                        FadeIn(slice_img),
                        Write(slice_label),
                        run_time=1.5
                    )
                else:
                    # Subsequent slices: crossfade from previous slice
                    prev_slice = ImageMobject("celebahq_combined_6.png")
                    prev_slice.scale_to_fit_height(5)
                    prev_slice.move_to(ORIGIN)
                    
                    prev_label = Text(slice_labels[i-1], 
                                    font_size=24, color="#FFD700", weight=BOLD)
                    prev_label.to_edge(DOWN, buff=0.8)
                    
                    self.play(
                        FadeOut(prev_label),
                        FadeOut(prev_slice),
                        FadeIn(slice_img),
                        Write(slice_label),
                        run_time=1.2
                    )
                
                # Hold on each slice
                self.wait(1.5)
                
                # Store current slice for next iteration
                if i < 5:  # Don't remove the last one yet
                    current_slice = slice_img
                    current_label = slice_label
            
            # Final message
            self.wait(0.5)
            final_message = Text("High-quality, diverse face generation with DDPM", 
                               font_size=26, color="#90EE90", weight=BOLD)
            final_message.to_edge(DOWN, buff=1.5)
            
            self.play(
                FadeOut(slice_label),
                Write(final_message),
                run_time=1
            )
            
            self.wait(3)
            
        except Exception as e:
            # Fallback if image not found
            error_text = Text("Image not found: celebahq_combined_6.png", 
                            font_size=24, color=RED)
            error_text.move_to(ORIGIN)
            
            placeholder = Rectangle(width=8, height=5, color=GRAY, fill_opacity=0.3)
            placeholder.move_to(ORIGIN)
            
            self.play(FadeIn(placeholder), Write(error_text))
            self.wait(3)
