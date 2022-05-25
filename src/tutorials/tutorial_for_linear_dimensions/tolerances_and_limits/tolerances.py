import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

dim = msp.add_linear_dim(base=(0, 3), p1=(3, 0), p2=(6.5, 0))
dim.set_tolerance(.1, hfactor=.4, align=0, dec=2)
dim.render()

dim1 = msp.add_linear_dim(base=(0, 3), p1=(7, 0), p2=(10.5, 0))
dim1.set_tolerance(.1, hfactor=.4, align=1, dec=2)
dim1.render()

dim2 = msp.add_linear_dim(base=(0, 3), p1=(11, 0), p2=(14.5, 0))
dim2.set_tolerance(.1, hfactor=.4, align=2, dec=2)
dim2.render()

dim3 = msp.add_linear_dim(base=(0, 3), p1=(15, 0), p2=(18.5, 0))
dim3.set_tolerance(upper=.1, lower=.15, hfactor=.4, align=2, dec=2)
dim3.render()

doc.saveas("output/tolerances.dxf")
