### Questions:

1. Where did that product come from? What assumption does it encode?

> The product was implied by the plate (box) containing "datapoints k". The PGM illustrates the factorisation of the joint PDF for
all variables, so if the datapoints are independent, we can write
the sampling distribution for all $y_k$'s' as the simple product
of independent terms ${\rm Pr}(y_k\,|\,y^{\rm true}_k,\sigma_k)$. In general these $y_k$ will not be *identically* distributed (as the
$\sigma_k$'s might be different, for one), but by drawing a plate we are  assuming they are *independently* distributed.


2. Why are the $\{x_k\}$ and the $\{\sigma_k\}$ always on the right hand side of the bar, but $\{y_k\}$ is sometimes on the left?

> We are taking $\{x_k\}$ and $\{\sigma_k\}$ to be *constants*, *given* to us as part of the experiment design - so all our inferences
and conditional PDFs are calculated *given* these constants.

3. What is the meaning of "$H_1$"? *Hint: notice that it too is always on the right hand side of the bar.*

> $H_1$ stands for "the model, including all of its assumptions."  The "H" comes from "hypothesis." All of our PDFs are conditional on the model, which is fine: you cannot do inference without making assumptions.

4. What functional form does the conditional PDF ${\rm Pr}(y^{\rm true}_k\,|\,x_k,m,b,H_1)$ have?

> The dot in the PGM represents a delta function PDF. It's a nice way of making explicit the deterministic parts of the model.

5. What functional form do you think we should assume for the sampling distribution, ${\rm Pr}(y_k\,|\,y^{\rm true}_k,x_k,\sigma_k,H_1)$? *Hint: imagine you were generating mock data.*

> If you're given just two numbers, representing a mean and a variance, the least committal assumption you can make is that the variable in question was drawn from a *Gaussian* with that mean and variance. We make this assumption a lot - often it turns out to be a good model, but not always.

6. What functional form should we assume for ${\rm Pr}(m,b\,|\,H_1)$?

> The answer to this will be context-dependent, and personal. Your prior knowledge of these two parameters will be different from someone
else's; likewise, what you are willing to assume will differ from others. The least you can do is state clearly your assumptions (and then expect them to be criticized). Going further, you can check your
results for robustness in a "sensitivity analysis", comparing various plausible prior assignments that others might want to make.

> In this case, I will assume a finite-width joint uniform distribution, that enforces positivity and asserts a particular order of magnitude for each parameter. More of an issue than the choice of prior in this problem is the parameterization itself: choosing the intercept parameter to be that at the mean $x$ rather than $x=0$ would probably be a better idea - but, if we have actual prior knowledge about these particular parameters, then we need to make sure we use that accurately.
