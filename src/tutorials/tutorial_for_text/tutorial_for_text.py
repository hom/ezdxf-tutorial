import ezdxf

doc = ezdxf.new("R2018", setup=True, units=ezdxf.units.MM)
msp = doc.modelspace()

'''
msp.add_text('A Simple Text').set_pos((2, 3), align='MIDDLE_RIGHT')

msp.add_text('Text Style Example: Liberation Serif',
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 0.35
             }).set_pos((2, 6), align='LEFT')
'''

msp.add_text("AC", dxfattribs={}).set_pos((10, 10))
msp.add_text("AC", dxfattribs={
    "height": 4,
    "bold": True,
}).set_pos((0, 0))
doc.saveas('output/simple_text.dxf')
