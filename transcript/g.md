[Title appears: “DDPM Innovation”]
“Now that we’ve seen how diffusion models work in general, let’s look at what the original DDPM paper brought to the table.”

[Noisy corgi with label 
𝑥
𝑡
x 
t
​
  appears]
“In standard diffusion models, the reverse step tries to directly predict the denoised image at each stage.
The DDPM paper took a different approach.”

[Arrow down to corgi with fewer dots, label 
𝑥
𝑡
−
1
x 
t−1
​
 ]
“Instead of guessing the clean image, the model predicts the noise that was added — 
𝜖
ϵ.”

[Extra noise separates to the right, minus sign appears, noise labeled 
𝜖
ϵ]
“This is powerful because the forward process already tells us exactly how noise was injected at every step.
If we can recover 
𝜖
ϵ accurately, the rest follows from a simple re-parameterization.”

[Hold on 
𝑥
𝑡
−
𝜖
→
𝑥
𝑡
−
1
x 
t
​
 −ϵ→x 
t−1
​
 ]
“That’s the core innovation of DDPM: reframing denoising as noise prediction.
And if you think about it, it’s a bit like skip connections in residual networks — instead of predicting the whole output, you predict just the residual.
It makes training more stable, the loss more aligned with likelihood,
and connects directly to a widely used approach in machine learning: denoising score matching.
