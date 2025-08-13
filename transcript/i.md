Latent diffusion is a big step forward, but there’s still room to push further.

The next natural step is a truly joint encoder–decoder–diffusion framework, trained end-to-end so that compression and generation evolve together, rather than being learned in separate stages.

In most current implementations, the encoder and decoder are trained first as a standalone autoencoder, and then kept fixed while the diffusion model is trained in that predefined latent space.
This makes training easier, but it locks the latent representation in place, preventing it from adapting to the diffusion process or letting the generator shape what gets preserved and how it’s rebuilt.

Another direction for improvement could be making the forward process itself learnable.
In standard diffusion, noise is added in a fixed way: the schedule, the distribution, and the variance are all chosen before training, and the same Gaussian noise is applied independently to every pixel and channel at each step.
Instead, the model could learn these parameters directly, or even generate them on the fly as part of the process, adapting the corruption to the structure of each sample.
This could mean per-image noise schedules, spatially varying variances, or non-Gaussian perturbations that make the reverse process easier and more data-efficient.

We could also explore adaptive compression, where the model learns to preserve the regions that carry the most semantic weight while compressing less important areas more aggressively.

Pixel-space DDPMs established the concept, latent diffusion made it practical, and the next steps aim to make it more adaptive, efficient, and capable.