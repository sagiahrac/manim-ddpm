We’ll start with a sample from some target data distribution — say, an image from the training set.

Let’s call it x_0.

Now, we define a process that gradually adds noise to this image over time.
This is the **forward** diffusion process, and it takes the form of a Markov chain.

In the forward process, each new image, x_t, is conditionally independent of all earlier states given x_t-1. This conditional independence is known as the Markov property, meaning the process has no memory beyond the previous state.

We’ll denote the forward process q.
At every step, we apply a gentle Gaussian perturbation to the current sample, producing the next noisier sample in the chain.
q_...

The key lies in the small b_t

"Notice how the mean of xt is just a slightly scaled-down version of x_t−1
  — it stays close, but shrinks a little with each step."

Now here’s the elegant part:
"Because the forward process is a Markov chain that adds independent Gaussian noise at each step,
every x_t can be expressed as a linear combination of the original sample x_0 and t independent Gaussian noise terms.

And since linear combinations of Gaussians are still Gaussian, that means:
every x_t remains Gaussian as well.

Thanks to this structure, we don’t need to simulate the entire chain to know the distribution at step t .
In fact, by induction, we can write it down in closed form:

q(x_t|x0)=...

Now, what is this at term?
It's defined as the product of pi(q-bt) over all previous steps.

Each of these terms is just a bit less than one — so multiplying them together gives us a scalar that steadily shrinks over time.

That means the contribution of the original sample,x_0, gets smaller and smaller as we go forward, and we converge in distribution to pure Gaussian noise:

This forward process maps complex data, like images, into a simple, known distribution — a standard Gaussian.

Why is this useful?

Because by knowing exactly how structure was lost at each step, we can attempt to learn the reverse — recovering structure from noise.

___


This sets the foundation for our generative model:
a process that begins with pure noise and learns to reverse the diffusion — one step at a time.

Each reverse step is modeled as a Gaussian distribution, but unlike the forward process — which uses fixed Gaussian noise schedules —
this time the backward process is learnable.

We’ll denote it by p_theta

p_theta = ...

At each step in the reverse chain, we sample the next image from a Gaussian whose mean and variance are predicted by our model.

Why sample instead of just taking the mean?

This sampling step is crucial. It introduces the stochasticity needed to capture the richness and diversity of the data distribution.

If we always took the mean, we’d be generating the most likely reconstruction at every step — but real data isn’t just the average of possibilities.

By chaining these learned transitions together,
we can gradually turn pure noise into something that resembles our original data.