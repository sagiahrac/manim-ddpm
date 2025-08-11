# DDPM Innovation

Now that we’ve seen how diffusion models work in general, let’s look at what the original DDPM paper brought to the table.

In standard diffusion models, the reverse step tries to directly predict the denoised image at each stage.  
The DDPM paper took a different approach.

↓ *(arrow to less noisy corgi)* with label $x_{t-1}$  
Instead of guessing the clean image, the model predicts the noise that was added — $\epsilon$.

![Noise labeled $\epsilon$](noise.png)  
This is powerful because the forward process already tells us exactly how noise was injected at every step.  
If we can recover $\epsilon$ accurately, the rest follows from a simple re-parameterization.

$$
x_t - \epsilon \quad \longrightarrow \quad x_{t-1}
$$

That’s the core innovation of DDPM: reframing denoising as **noise prediction**.  
And if you think about it, it’s a bit like skip connections in residual networks — instead of predicting the whole output, you predict just the **residual**.  

This:
- Makes training more stable  
- Aligns the loss more closely with likelihood  
- Connects directly to a widely used approach in machine learning: **denoising score matching**
