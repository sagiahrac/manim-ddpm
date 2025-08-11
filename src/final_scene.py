from manim import *
from .base import DDPMBaseMixin




class NeuralNetworkFade(Scene, DDPMBaseMixin):
    def image_from_path(self, path, scale=0.2):
        """Load an image from a given path and scale it."""
        img = ImageMobject(path)
        img.scale(scale)
        return img
    
    def framed_image(self, image, color=YELLOW, buff=0.05):
        """Create a framed image with a surrounding rectangle."""
        frame = SurroundingRectangle(image, color=color, buff=buff, stroke_width=2)
        framed_image = Group(image, frame)
        return framed_image
    
    def add_grid_to_image(self, image, grid_color=WHITE, opacity=0.3, lines_per_axis=8):
        """Add a grid overlay to an image."""
        # Get image bounds
        height = image.height
        width = image.width
        center = image.get_center()
        
        # Create grid lines
        grid_lines = VGroup()
        
        # Vertical lines
        for i in range(lines_per_axis + 1):
            x_pos = center[0] - width/2 + (i * width / lines_per_axis)
            line = Line(
                start=[x_pos, center[1] - height/2, 0],
                end=[x_pos, center[1] + height/2, 0],
                color=grid_color,
                stroke_width=4
            ).set_opacity(opacity)
            grid_lines.add(line)
        
        # Horizontal lines
        for i in range(lines_per_axis + 1):
            y_pos = center[1] - height/2 + (i * height / lines_per_axis)
            line = Line(
                start=[center[0] - width/2, y_pos, 0],
                end=[center[0] + width/2, y_pos, 0],
                color=grid_color,
                stroke_width=4
            ).set_opacity(opacity)
            grid_lines.add(line)
        
        return grid_lines
    
    def create_dot_vector(self, center, blue_dots=3, brown_dots=1, dot_radius=0.1, spacing=0.3):
        """Create a vector representation using colored dots."""
        total_dots = blue_dots + brown_dots
        vector_group = VGroup()
        
        # Create a list of colors to randomize
        colors = [BLUE] * blue_dots + [ORANGE] * brown_dots
        import random
        random.shuffle(colors)
        
        # Create dots with randomized colors
        for i in range(total_dots):
            y_pos = center[1] + (total_dots/2 - i - 0.5) * spacing
            dot = Circle(radius=dot_radius, color=colors[i], fill_opacity=1.0)
            dot.move_to([center[0], y_pos, 0])
            vector_group.add(dot)
        
        # Add vector brackets
        bracket_height = total_dots * spacing
        left_bracket = Line(
            start=[center[0] - 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] - 0.2, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        right_bracket = Line(
            start=[center[0] + 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] + 0.2, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        
        # Add bracket tops and bottoms
        left_top = Line(
            start=[center[0] - 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] - 0.15, center[1] + bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        left_bottom = Line(
            start=[center[0] - 0.2, center[1] - bracket_height/2, 0],
            end=[center[0] - 0.15, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        right_top = Line(
            start=[center[0] + 0.2, center[1] + bracket_height/2, 0],
            end=[center[0] + 0.15, center[1] + bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        right_bottom = Line(
            start=[center[0] + 0.2, center[1] - bracket_height/2, 0],
            end=[center[0] + 0.15, center[1] - bracket_height/2, 0],
            color=WHITE, stroke_width=3
        )
        
        brackets = VGroup(left_bracket, right_bracket, left_top, left_bottom, right_top, right_bottom)
        
        return VGroup(vector_group, brackets)
    
    def create_decoder_shape(self):
        """Create a visual decoder representation using shapes."""        
        # Define trapezoid vertices - proper decoder shape
        top_left = ORIGIN + 0.5 * LEFT + 1.5 * UP
        top_right = ORIGIN + 0.5 * RIGHT + 1.75 * UP
        bottom_right = ORIGIN + 0.5 * RIGHT + 0.25 * UP
        bottom_left = ORIGIN + 0.5 * LEFT + 0.5 * UP
        
        # Create the trapezoid
        trapezoid = Polygon(
            top_left, top_right, bottom_right, bottom_left,
            color=PURPLE, 
            stroke_width=3, 
            fill_opacity=0.2,
            fill_color=PURPLE
        )
                
        return trapezoid
    
    def create_encoder_shape(self):
        """Create a visual encoder representation using shapes (mirrored decoder)."""        
        # Define trapezoid vertices - mirrored decoder shape (wider at bottom)
        top_left = ORIGIN + 0.5 * LEFT + 1.75 * UP
        top_right = ORIGIN + 0.5 * RIGHT + 1.5 * UP
        bottom_right = ORIGIN + 0.5 * RIGHT + 0.5 * UP
        bottom_left = ORIGIN + 0.5 * LEFT + 0.25 * UP
        
        # Create the trapezoid
        trapezoid = Polygon(
            top_left, top_right, bottom_right, bottom_left,
            color=GREEN_A, 
            stroke_width=3, 
            fill_opacity=0.2,
            fill_color=GREEN_A
        )
                
        return trapezoid
    
    def craete_nn(self):
        input_layer = VGroup(*[Circle(radius=0.3, color=BLUE) for _ in range(3)])
        input_layer.arrange(DOWN, buff=0.5)
        input_layer.shift(LEFT * 3)
        
        # Hidden layer (4 nodes)
        hidden_layer = VGroup(*[Circle(radius=0.3, color=GREEN) for _ in range(5)])
        hidden_layer.arrange(DOWN, buff=0.4)
        
        # Output layer (2 nodes)
        output_layer = VGroup(*[Circle(radius=0.3, color=RED) for _ in range(3)])
        output_layer.arrange(DOWN, buff=0.6)
        output_layer.shift(RIGHT * 3)
        
        # Create connections
        connections = VGroup()
        
        # Input to hidden connections
        for input_node in input_layer:
            for hidden_node in hidden_layer:
                line = Line(input_node.get_center(), hidden_node.get_center(), 
                          stroke_width=2, color=GRAY)
                connections.add(line)
        
        # Hidden to output connections
        for hidden_node in hidden_layer:
            for output_node in output_layer:
                line = Line(hidden_node.get_center(), output_node.get_center(),
                          stroke_width=2, color=GRAY)
                connections.add(line)
        
        # Group all neural network components
        neural_network = VGroup(connections, input_layer, hidden_layer, output_layer)
        neural_network.scale(0.5)
        return neural_network
    
    def construct(self):
        self.setup_3b1b_style()

        encoder = self.create_encoder_shape()
        decoder = self.create_decoder_shape()
        neural_network = self.craete_nn()

        # Position the encoder and decoder
        encoder.move_to(LEFT * 0.75 + UP * 1.5)
        decoder.move_to(RIGHT * 0.75 + UP * 1.5)
        neural_network.move_to(UP * 1.5)

        encoder.scale(0.3)
        decoder.scale(0.3)
        neural_network.scale(0.25)

        full_framework = VGroup(encoder, decoder, neural_network)
        

        self.play(
            FadeIn(full_framework),
        )


        q_phi = MathTex(r"q_\phi(x_t | x_{t-1})", color=WHITE, font_size=32)
        self.play(
            Write(q_phi),
        )

        beatles = self.image_from_path("beatles_neg.png", scale=0.4)
        beatles_framed = self.framed_image(beatles, color=YELLOW, buff=0.05)
        beatles_framed.move_to(ORIGIN + 1.5 * DOWN)

        self.play(
            FadeIn(beatles_framed),
        )