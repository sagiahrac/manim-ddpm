There’s another reason we sample: during inference, we start from a point drawn randomly from a standard Gaussian $ \mathcal{N}(0, I) $ — far from the data.

The reverse process must then navigate back through a sequence of intermediate distributions.

But not all of these are fully captured during training.

If we only followed the mean path, we’d risk drifting off course — especially in regions the model hasn’t learned well —

and passing through points that lead to poorly shaped or meaningless Gaussians in the next step.

> Sampling keeps the reverse process aligned by exploring more regions of the learned data distribution.
