from manim import *
from .base import DDPMBaseMixin
import numpy as np
from PIL import Image


class CelebAHQDemoSlide(Scene, DDPMBaseMixin):
    def construct(self):
        self.setup_3b1b_style()

        pil_image = Image.open("media/images/celebahq_combined_6.png")
        img_width, img_height = pil_image.size

        # Calculate slice dimensions for 2×3 grid (2 columns, 3 rows)
        slice_width = img_width // 3
        slice_height = img_height // 2

        # Define slice positions and create cropped images
        slice_info = [
            {"pos": (0, 0), "name": "Top Left"},  # Row 0, Col 0
            {"pos": (0, 1), "name": "Top Right"},  # Row 0, Col 1
            {"pos": (0, 2), "name": "Middle Left"},  # Row 0, Col 2
            {"pos": (1, 0), "name": "Middle Right"},  # Row 1, Col 0
            {"pos": (1, 1), "name": "Bottom Left"},  # Row 1, Col 1
            {"pos": (1, 2), "name": "Bottom Right"},  # Row 1, Col 2
        ]

        # Create temporary slice image files
        slice_paths = []
        for i, slice_data in enumerate(slice_info):
            row, col = slice_data["pos"]

            # Calculate crop box (left, top, right, bottom)
            left = col * slice_width
            top = row * slice_height
            right = left + slice_width
            bottom = top + slice_height

            # Crop the slice
            slice_pil = pil_image.crop((left, top, right, bottom))

            # Save temporary slice
            slice_path = f"media/images/temp_slice_{i}.png"
            slice_pil.save(slice_path)
            slice_paths.append(slice_path)

        # Now show each slice individually
        current_slice = None

        # Add source citation at bottom right
        source_citation = Text(
            'Generated samples on CelebA-HQ 256×256\nHo et al., "Denoising Diffusion Probabilistic Models" (2020)',
            font_size=10,
            color="#888888",  # Gray color
            line_spacing=1.5,
        )
        source_citation.to_corner(DOWN + RIGHT, buff=0.3)
        self.add(source_citation)  # Add it to stay throughout the animation

        for i, (slice_path, slice_data) in enumerate(zip(slice_paths, slice_info)):
            slice_name = slice_data["name"]

            # Create the slice image
            slice_img = ImageMobject(slice_path)
            slice_img.scale_to_fit_height(4)
            slice_img.move_to(ORIGIN)

            # Add yellow frame around the image
            frame = Rectangle(
                width=slice_img.width + 0.2,  # Slightly larger than image
                height=slice_img.height + 0.2,
                stroke_color=YELLOW,
                stroke_width=2,
                fill_opacity=0,  # No fill, just border
            )
            frame.move_to(slice_img.get_center())

            # Group the image and frame together
            framed_slice = Group(slice_img, frame)

            # Create label for this slice
            slice_label = Text(
                f"{slice_name}", font_size=28, color="#FFD700", weight=BOLD
            )
            slice_label.to_edge(DOWN, buff=1)

            # Create sample description
            sample_desc = Text(
                f"Generated Sample {i + 1}", font_size=20, color="#87CEEB"
            )
            sample_desc.next_to(slice_label, DOWN, buff=0.3)

            if i == 0:
                # slice_img.set_opacity(0)
                self.play(FadeIn(framed_slice), run_time=1.5)
            else:
                # Subsequent slices: slide transition effect
                framed_slice.shift(RIGHT * 10)
                self.play(
                    current_slice.animate.shift(LEFT * 10),
                    framed_slice.animate.shift(LEFT * 10),
                    run_time=1.5,
                )

            # Hold on each slice
            self.wait(0.5)

            # Store current elements for next iteration
            current_slice = framed_slice

        # Final flourish
        self.play(FadeOut(current_slice), run_time=1)


        # text "so what changed?"

        question_text = Text(            "So what changed?",
            font="TeX Gyre Termes",
            font_size=48,
            color=WHITE,
            weight=BOLD,
        )


        self.play(Write(question_text, run_time=0.75))
        self.wait(2)
        self.play(FadeOut(question_text))

        # Clean up temporary files
        import os

        for slice_path in slice_paths:
            try:
                os.remove(slice_path)
            except:
                pass
