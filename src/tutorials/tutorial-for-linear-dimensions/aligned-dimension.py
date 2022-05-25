import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_line((0, 2), (3, 0))
dim = msp.add_aligned_dim(p1=(0, 2), p2=(3, 0), distance=1).render()
doc.saveas("output/dim_linear_aligned.dxf")
