A key bottleneck in the original **DDPM** is its choice to operate entirely in pixel space.  
In each denoising step, the learned reverse process $p_{\theta}$ — which can be a complex neural network — takes the noisy image $x_t$ and the timestep $t$ and predicts the mean and variance of the Gaussian distribution for the previous step in the sequence.  

These are pixel-wise predictions — one mean and one variance for every pixel and channel — so their shape matches the image exactly.  
This means the network processes full-resolution data at every step, and it repeats this hundreds, sometimes thousands, of times during sampling.  
The result is high computational cost and slow generation compared to approaches that work in more compact representations.

---

A natural extension is to move the diffusion process into a **latent space**.  
First, an encoder compresses the image into a lower-dimensional, semantically meaningful representation.  
Diffusion operates on this smaller tensor — so the predicted mean and variance are also much smaller — and a decoder then reconstructs the full-resolution image.  
This preserves the probabilistic framework while making sampling significantly faster and more memory-efficient, and it enables richer semantic controls.

However, this approach inherits any biases or artifacts from the autoencoder, and aggressive compression can remove fine details.  


Future research could address this with:

- **Joint encoder–decoder–diffusion training**
- **Adaptive compression** that retains important structure
- **Multi-scale pipelines** combining latent and pixel-space diffusion
- **Semantically structured latents** for cleaner, more controllable edits

---

**In short:** pixel-space DDPMs established the concept; latent diffusion improves its practicality and scope.
