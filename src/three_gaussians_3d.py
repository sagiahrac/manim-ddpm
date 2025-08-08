from manim import *
import numpy as np


class ThreeGaussians3D(ThreeDScene):
    def construct(self):
        resolution_fa = 24
        self.set_camera_orientation(phi=75 * DEGREES, theta=-30 * DEGREES)

        # Define parameterized Gaussian function
        def multi_gaussian(u, v, stage=0):
            """Create a multimodal Gaussian that evolves over stages"""
            x, y = u, v
            
            # Special case: crazy distribution (stage -1)
            if stage == -1:
                # Create a wild, chaotic distribution with multiple peaks and waves
                z_total = 0
                # Multiple random-like peaks
                peaks = [
                    {"sigma": 0.2, "mu": [-2.0, -1.5], "height": 0.8},
                    {"sigma": 0.15, "mu": [1.8, 0.5], "height": 1.2},
                    {"sigma": 0.25, "mu": [0.3, -2.0], "height": 0.6},
                    {"sigma": 0.18, "mu": [-0.5, 1.8], "height": 1.0},
                    {"sigma": 0.12, "mu": [2.2, -0.8], "height": 0.9},
                    {"sigma": 0.22, "mu": [-1.8, 0.8], "height": 0.7},
                ]
                
                for peak in peaks:
                    d = np.linalg.norm(np.array([x - peak["mu"][0], y - peak["mu"][1]]))
                    z_gaussian = peak["height"] * np.exp(-(d ** 2 / (2.0 * peak["sigma"] ** 2)))
                    z_total += z_gaussian
                
                # Add some wave-like distortions
                wave_contribution = 0.3 * np.sin(3 * x) * np.cos(2 * y) * np.exp(-(x**2 + y**2)/8)
                z_total += max(0, wave_contribution)
                
                return np.array([x, y, z_total])
            
            # Initial parameters for 3 Gaussians - widely separated and distinct
            initial_params = [
                {"sigma": 0.3, "mu": [-1.5, 0.0], "height": 1.5},    # Left peak - tall and narrow
                {"sigma": 0.25, "mu": [1.2, 1.0], "height": 1.8},    # Top-right peak - tallest
                {"sigma": 0.35, "mu": [0.8, -1.3], "height": 1.2}    # Bottom-right peak - medium
            ]
            
            # Target parameters (unified Gaussian at center)
            target_params = [
                {"sigma": 0.8, "mu": [0.0, 0.0], "height": 1.0},     # Main unified peak
                {"sigma": 0.8, "mu": [0.0, 0.0], "height": 0.0},     # Fade out
                {"sigma": 0.8, "mu": [0.0, 0.0], "height": 0.0}      # Fade out
            ]
            
            # Interpolate parameters based on stage (0-3)
            t = stage / 3.0  # Normalize to 0-1
            z_total = 0
            
            for i in range(3):
                # Interpolate each Gaussian's parameters with smoother transitions
                sigma = initial_params[i]["sigma"] + t * (target_params[i]["sigma"] - initial_params[i]["sigma"])
                mu_x = initial_params[i]["mu"][0] + t * (target_params[i]["mu"][0] - initial_params[i]["mu"][0])
                mu_y = initial_params[i]["mu"][1] + t * (target_params[i]["mu"][1] - initial_params[i]["mu"][1])
                
                # Use smoother height transition with easing
                height_t = t ** 2 if i > 0 else 1 - (1 - t) ** 2  # Ease in for secondary peaks, ease out for main peak
                height = initial_params[i]["height"] + height_t * (target_params[i]["height"] - initial_params[i]["height"])
                
                # Calculate Gaussian value
                d = np.linalg.norm(np.array([x - mu_x, y - mu_y]))
                z_gaussian = height * np.exp(-(d ** 2 / (2.0 * sigma ** 2)))
                z_total += z_gaussian
            
            return np.array([x, y, z_total])

        # Add 3D axes with extended range for better visibility
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[0, 2, 0.5],
            x_length=10,
            y_length=10,
            z_length=6
        )

        # Create initial surface (stage 3 - unified) with extended range
        current_surface = Surface(
            lambda u, v: multi_gaussian(u, v, stage=3),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2.5, +2.5],
            u_range=[-2.5, +2.5]
        )
        
        # Style the surface with 3Blue1Brown-like styling
        current_surface.scale(2, about_point=ORIGIN)
        current_surface.set_style(fill_opacity=0.8, stroke_color=BLUE_D, stroke_width=0.5)
        current_surface.set_fill_by_value(axes=axes, colorscale=[(BLUE_E, 0), (BLUE_D, 0.2), (BLUE_C, 0.5), (BLUE_B, 0.8), (BLUE_A, 1.2)], axis=2)

        # Add axis labels
        x_label = axes.get_x_axis_label(Tex("x"))
        y_label = axes.get_y_axis_label(Tex("y"))
        z_label = axes.get_z_axis_label(Tex("density"))

        # Add title
        title = Text("Unimodal → Multimodal Evolution", font_size=32, color=WHITE)
        title.to_corner(UL)

        # Scene construction
        self.add(axes, x_label, y_label, z_label)
        self.add_fixed_in_frame_mobjects(title)
        
        # Don't show the initial helper surface - it's just for transformation setup
        
        # Rotate camera to show different angles
        self.move_camera(phi=60 * DEGREES, theta=-45 * DEGREES, run_time=2)
        self.wait(1)
        
        # Start by creating and showing the first visible surface (stage 2)
        first_visible_surface = Surface(
            lambda u, v: multi_gaussian(u, v, stage=2),
            resolution=(resolution_fa, resolution_fa),
            v_range=[-2.5, +2.5],
            u_range=[-2.5, +2.5]
        )
        
        # Style the first visible surface
        first_visible_surface.scale(2, about_point=ORIGIN)
        first_visible_surface.set_style(fill_opacity=0.8, stroke_color=BLUE_D, stroke_width=0.5)
        first_visible_surface.set_fill_by_value(axes=axes, colorscale=[(BLUE_E, 0), (BLUE_D, 0.2), (BLUE_C, 0.5), (BLUE_B, 0.8), (BLUE_A, 1.2)], axis=2)
        
        # Show the first visible surface and update title
        stage_title = Text("Stage 1: Beginning to Split", font_size=28, color=YELLOW)
        stage_title.to_corner(UL)
        self.play(Create(first_visible_surface), run_time=2)
        self.add_fixed_in_frame_mobjects(stage_title)
        self.remove(title)
        self.wait(1)
        
        # Sample a dot on the first surface
        def sample_point_on_surface(stage):
            """Sample a point on the surface based on the distribution"""
            # For demonstration, we'll sample from high-density regions
            if stage == 2:  # Beginning to split
                sample_x, sample_y = 1.0, 0.8  # Near one of the emerging peaks
            elif stage == 1:  # Moving apart
                sample_x, sample_y = -1.2, -0.2  # Near left peak
            elif stage == 0:  # Fully separated
                sample_x, sample_y = 1.2, 1.0  # Near top-right peak
            elif stage == -1:  # Chaotic
                sample_x, sample_y = 1.8, 0.5  # One of the chaotic peaks
            else:
                sample_x, sample_y = 0.0, 0.0
            
            # Calculate the z-coordinate from the surface
            surface_point = multi_gaussian(sample_x, sample_y, stage)
            z_coord = surface_point[2]
            
            return np.array([sample_x, sample_y, z_coord]) * 2  # Scale to match surface scaling
        
        # Create initial sample dot
        initial_sample_pos = sample_point_on_surface(2)
        sample_dot = Dot3D(point=initial_sample_pos, radius=0.15, color=RED)
        self.play(Create(sample_dot), run_time=1)
        self.wait(1)
        
        # Update current_surface to be the first visible one
        current_surface = first_visible_surface
        
        # Animate through remaining stages in reverse (2 → 1 → 0 → crazy)
        stage_titles = [
            "Stage 1: Beginning to Split",
            "Stage 2: Moving Apart",
            "Stage 3: Fully Separated Modes",
            "Stage 4: Chaotic Distribution!"
        ]
        
        stage_colors = [YELLOW, YELLOW, YELLOW, RED]
        surfaces = [current_surface]
        remaining_stages = [1, 0, -1]  # Going from stage 2 to 0, then to crazy (-1)
        
        for i, stage in enumerate(remaining_stages):
            # Create next stage surface with extended range
            next_surface = Surface(
                lambda u, v, s=stage: multi_gaussian(u, v, stage=s),
                resolution=(resolution_fa, resolution_fa),
                v_range=[-2.5, +2.5],
                u_range=[-2.5, +2.5]
            )
            
            # Style the new surface
            next_surface.scale(2, about_point=ORIGIN)
            next_surface.set_style(fill_opacity=0.8, stroke_color=BLUE_D, stroke_width=0.5)
            next_surface.set_fill_by_value(axes=axes, colorscale=[(BLUE_E, 0), (BLUE_D, 0.2), (BLUE_C, 0.5), (BLUE_B, 0.8), (BLUE_A, 1.2)], axis=2)
            
            # Update title
            stage_title = Text(stage_titles[i+1], font_size=28, color=stage_colors[i+1])
            stage_title.to_corner(UL)
            
            if i == 0:
                self.add_fixed_in_frame_mobjects(stage_title)
                self.remove(title)
            else:
                prev_title = Text(stage_titles[i], font_size=28, color=stage_colors[i])
                prev_title.to_corner(UL)
                self.add_fixed_in_frame_mobjects(stage_title)
                self.remove(prev_title)
            
            surfaces.append(next_surface)


        for i, surface in enumerate(surfaces[1:]):
            # Transform surface
            self.play(Transform(current_surface, surface), run_time=2)
            
            # Calculate new sample position for this stage
            current_stage = remaining_stages[i]
            
            if current_stage == -1:  # Chaotic stage - dot jumps off scene!
                # First move to the chaotic peak briefly
                chaotic_sample_pos = sample_point_on_surface(current_stage)
                self.play(sample_dot.animate.move_to(chaotic_sample_pos), run_time=0.5)
                self.wait(0.5)
                
                # Then make it "jump up" dramatically
                jump_position = chaotic_sample_pos + np.array([0, 0, 3.0])  # Jump up more moderately
                self.play(
                    sample_dot.animate.move_to(jump_position),
                    run_time=1,
                    rate_func=rush_from  # Fast acceleration upward
                )
                
                # Then fall down out of the scene
                fall_position = chaotic_sample_pos + np.array([0, 0, -15.0])  # Fall way down below
                self.play(
                    sample_dot.animate.move_to(fall_position).set_opacity(0),
                    run_time=2,
                    rate_func=rush_into  # Accelerating downward fall
                )
                # Add a dramatic pause after the "fall"
                self.wait(2)
            else:
                # Normal behavior for other stages
                new_sample_pos = sample_point_on_surface(current_stage)
                self.play(sample_dot.animate.move_to(new_sample_pos), run_time=1)
                self.wait(1)
        
        # Rotate camera again to show the final result
        self.move_camera(phi=80 * DEGREES, theta=30 * DEGREES, run_time=2)
        self.wait(1)
        
        # Final zoom out
        self.move_camera(zoom=0.8, run_time=2)
        self.wait(2)
