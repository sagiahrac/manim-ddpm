“A key bottleneck in the original DDPM is its choice to operate entirely in pixel space.
In each denoising step, the learned reverse process 
𝑝
𝜃
p 
θ
​
  — which can be a complex neural network — takes the noisy image 
𝑥
𝑡
x 
t
​
  and the timestep 
𝑡
t and predicts the mean 
𝜇
𝜃
μ 
θ
​
  and variance 
𝜎
𝜃
2
σ 
θ
2
​
  of the Gaussian distribution for the previous image in the sequence.
These are pixel-wise predictions — one mean and one variance for every pixel and channel — so their shape matches the image exactly.
This means the network processes full-resolution data at every step, and it repeats this hundreds, sometimes thousands, of times during sampling.
The result is high computational cost and slow generation compared to approaches that work in more compact representations.

A natural extension is to move the diffusion process into a latent space.
First, an encoder compresses the image into a lower-dimensional, semantically meaningful representation.
Diffusion operates on this smaller tensor — so the predicted mean and variance are also much smaller — and a decoder then reconstructs the full-resolution image.
This preserves the probabilistic framework while making sampling significantly faster and more memory-efficient, and it enables richer semantic controls.

However, this approach inherits any biases or artifacts from the autoencoder, and aggressive compression can remove fine details.
Future research could address this with joint encoder–decoder–diffusion training, adaptive compression that retains important structure, multi-scale pipelines that combine latent and pixel-space diffusion, and semantically structured latents for cleaner, more controllable edits.

In short: pixel-space DDPMs established the concept; latent diffusion improves its practicality and scope.”