import numpy as np

def rejection_sampling(pdf, low, high, n_samples, *args):
    """
    This is a not-very-efficient implementation of the acceptance-rejection
    sampler. (I don't know why I even put it on github).

    Parameters
    ----------
    pdf : callable
        The analytical formulation of the density function to get samples from.
    low, high : float, float
        The support of the density or the interval where to get samples.
    n_samples : int
        Number of desired samples
    args : list
        List of additional arguments to be passed to ``pdf``.

    Returns
    -------
    accepted_samples : array
        Array containing samples from ``pdf``
    """

    x = np.linspace(low, high, n_samples)
    pdfmax = np.max(pdf(x, *args))

    if np.isnan(pdfmax) or np.isinf(pdfmax):
        raise ValueError("pdf has nan or inf values.")

    n_accepted_samples = 0
    accepted_samples = []
    while n_accepted_samples < n_samples:
        unif_x = np.random.uniform(low=low, high=high, size=n_samples)
        unif_y = np.random.uniform(size=n_samples)
        accept = np.where(unif_y <= pdf(unif_x, *args) / pdfmax)[0]
        accepted_samples = np.concatenate([accepted_samples, unif_x[accept]])
        n_accepted_samples = accepted_samples.size

    return accepted_samples[:n_samples]