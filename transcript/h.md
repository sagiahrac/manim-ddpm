In fact, this single design choice sits right at the intersection of three well-known ideas.

From the probabilistic side — we’re doing Variational Inference, maximizing the ELBO: a lower bound on the data likelihood that has been central to probabilistic modeling for decades.

From the score-based side — that very same objective is equivalent to denoising score matching, where the model learns what’s called the score function — the gradient of the log probability — and in practice, it does that simply by predicting the noise that was added.

And from a sampling perspective — the reverse process can be expressed as Langevin dynamics, an MCMC method that moves in the direction of the score while injecting Gaussian noise, step by step guiding samples closer to the true data distribution.