import ezdxf

doc = ezdxf.new('R12', setup=True)
msp = doc.modelspace()

msp.add_text('A Simple Text').set_pos((2, 3), align='MIDDLE_RIGHT')

msp.add_text('Text Style Example: Liberation Serif',
             dxfattribs={
                 'style': 'LiberationSerif',
                 'height': 0.35
             }).set_pos((2, 6), align='LEFT')

doc.saveas('../output/simple_text.dxf')
