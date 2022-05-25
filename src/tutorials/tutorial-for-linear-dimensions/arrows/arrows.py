import ezdxf

doc = ezdxf.new('R2007', setup=True)
msp = doc.modelspace()

dim = msp.add_linear_dim(base=(3, 2), p1=(3, 0), p2=(6, 0))
dim.set_tick(size=0.25)
dim.render()

dim1 = msp.add_linear_dim(base=(7, 2), p1=(7, 0), p2=(10, 0))
dim1.set_arrows(blk=ezdxf.ARROWS.closed_filled, size=0.25)
dim1.render()

msp.add_linear_dim(
    base=(11, 2),
    p1=(11, 0),
    p2=(14, 0),
    override={
        "dimtsz": 0,  # set tick size to 0 to enable arrow usage
        "dimasz": 0.25,  # arrow size in drawing units
        "dimblk": "OPEN30",  # arrow block name
    }
).render()

doc.saveas("output/arrows.dxf")
