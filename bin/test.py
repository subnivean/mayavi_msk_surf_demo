from msk.parasurf import DemoBSplineSurf
from msk.transformations import Trsf

d = DemoBSplineSurf()
d.plot()

c = d.copy()
c.transform(Trsf("0 0 0 90 0 0"))
c.scale(0.9)
c.plot(color="blue")

filsrf, splitsurfs = c.fillet(d, radius=0.08)
filsrf.plot(color="yellow")

curledsrf = splitsurfs[1].curl("v1", 0.1, 0.06)
curledsrf.plot(color="cyan")

origin = Trsf("0 0 0 0 0 0")
origin.plot()
