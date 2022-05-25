import ezdxf

doc = ezdxf.new('R2010', setup=True)
msp = doc.modelspace()

msp.add_linear_dim(
    base=(3, 1), p1=(3, 0), p2=(6, 0), override={
        "dimtxsty": "Standard",
        "dimtxt": 0.35,
        "dimclrt": 1,
    }
).render()
msp.add_linear_dim(
    base=(3, 2), p1=(3, 0), p2=(6, 0), override={
        "dimtxsty": "Standard",
        "dimtxt": 0.5,
        "dimclrt": 7,
    }
).render()

doc.saveas('output/text_properties.dxf')
