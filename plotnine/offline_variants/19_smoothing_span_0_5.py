from plotnine.data import economics
from plotnine import ggplot, aes, facet_grid, labs, geom_point, geom_smooth, xlab, ylab

g=(ggplot(economics)
        + aes(x="date", y="uempmed")
        + geom_point()
        + geom_smooth(color="red", span=0.5)
        + xlab("date (year)")
        + ylab("unemploynment"))

g.save("19.png")
