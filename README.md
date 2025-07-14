# DDPM Manim Presentation

A comprehensive 3Blue1Brown-style Manim presentation explaining Denoising Diffusion Probabilistic Models (DDPMs) based on the paper by Ho, Jain, and Abbeel (2020).

## 📁 Project Structure

```
ddpm-manim/
├── main.py                 # Main orchestrated presentation (all slides)
├── individual_scenes.py    # Individual scene classes for specific slides
├── pyproject.toml         # Project dependencies and metadata
├── README.md              # This file
├── src/                   # Modular slide components
│   ├── __init__.py        # Package marker
│   ├── base.py           # Shared mixin with helper methods
│   ├── title_slide.py           # Title slide module
│   ├── intuition_slide.py       # Intuition explanation module
│   ├── forward_diffusion_slide.py      # Forward diffusion process module
│   ├── reverse_denoising_slide.py      # Reverse denoising process module
│   ├── mathematical_formulation_slide.py  # Mathematical formulation module
│   └── training_process_slide.py       # Training process module
└── media/                 # Generated output videos and cache
    ├── videos/
    ├── images/
    └── Tex/
```

## 🚀 Quick Start

### Prerequisites
- Python 3.11+
- UV package manager (`pip install uv`)
- LaTeX distribution (for mathematical formulas)

### Installation & Setup
```bash
git clone <repository-url>
cd ddpm-manim
uv sync  # Install dependencies using uv
```

### Running the Complete Presentation
```bash
# Full presentation (all slides)
uv run manim main.py DDPMDemo -ql

# High quality version
uv run manim main.py DDPMDemo -qh
```

### Running Individual Slides
```bash
# Title slide only
uv run manim individual_scenes.py TitleSlideScene -ql

# Intuition explanation
uv run manim individual_scenes.py IntuitionSlideScene -ql

# Forward diffusion process
uv run manim individual_scenes.py ForwardDiffusionSlideScene -ql

# Reverse denoising process
uv run manim individual_scenes.py ReverseDenoisingSlideScene -ql

# Mathematical formulation
uv run manim individual_scenes.py MathematicalFormulationSlideScene -ql

# Training process
uv run manim individual_scenes.py TrainingProcessSlideScene -ql
```

## 📋 Slide Contents

### 1. Title Slide
- Elegant 3Blue1Brown-style title presentation
- Paper attribution and course information
- Professional typography and animations

### 2. Core Intuition Slide
- High-level explanation of the diffusion concept
- Visual demonstration: noise → neural network → clean image
- Accessible introduction to the key idea

### 3. Forward Diffusion Process
- Step-by-step visualization of noise addition
- Mathematical formulation: `q(x_t|x_{t-1})`
- Progressive image corruption sequence

### 4. Reverse Denoising Process
- Neural network denoising visualization
- Mathematical formulation: `p_θ(x_{t-1}|x_t)`
- Progressive image reconstruction sequence

### 5. Mathematical Formulation
- Key equations for forward and reverse processes
- Training objective formulation
- Formal probabilistic framework

### 6. Training Process
- Step-by-step training algorithm
- Loss computation and backpropagation
- Practical implementation overview

## 🎨 Features

### 3Blue1Brown Style
- Dark background (`#0e1419`)
- Elegant color scheme (sky blue titles, clean typography)
- Smooth animations with proper timing
- Professional mathematical typesetting

### Modular Architecture
- **Shared Base Class**: `DDPMBaseMixin` provides common helper methods
- **Individual Modules**: Each slide is a separate, self-contained module
- **Flexible Rendering**: Run full presentation or individual slides
- **Clean Imports**: Proper Python package structure

### Helper Methods (in `src/base.py`)
- `setup_3b1b_style()`: Configures 3Blue1Brown visual style
- `create_image_representation()`: Creates clean image visualizations
- `create_noisy_image()`: Creates noise-corrupted image representations

## 🛠 Development

### Project Structure Benefits
- **Modularity**: Each slide can be developed and tested independently
- **Reusability**: Shared methods in the base mixin prevent code duplication
- **Maintainability**: Clear separation of concerns and organized file structure
- **Flexibility**: Easy to add new slides or modify existing ones

### Extending the Presentation
1. Create a new slide module in `src/`
2. Inherit from `Scene` and `DDPMBaseMixin`
3. Add the slide method to `main.py` 
4. Create an individual scene class in `individual_scenes.py`

### Code Quality
- Proper imports and module structure
- 3Blue1Brown style conventions
- Clean animations using `Write()` for text and `Create()` for shapes
- Consistent typography and spacing

## 📺 Output

Generated videos are saved to:
- Full presentation: `media/videos/main/480p15/DDPMDemo.mp4`
- Individual slides: `media/videos/individual_scenes/480p15/[SlideName].mp4`

## 📚 References

- **Paper**: "Denoising Diffusion Probabilistic Models" by Ho, Jain, and Abbeel (2020)
- **Framework**: [Manim Community Edition](https://www.manim.community/)
- **Style**: Inspired by [3Blue1Brown](https://www.3blue1brown.com/)

## 🤝 Contributing

1. Follow the existing code structure and style
2. Maintain 3Blue1Brown visual conventions
3. Test individual slides before committing
4. Update documentation for new features

## 📄 License

This project is intended for educational purposes. Please respect the original paper's licensing and citation requirements.
