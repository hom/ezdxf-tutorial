import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

dim = msp.add_linear_dim(base=(0, 3), p1=(3, 0), p2=(6.5, 0))
dim.set_limits(upper=.1, lower=.15, hfactor=.4, dec=2)
dim.render()

doc.saveas("output/limits.dxf")
