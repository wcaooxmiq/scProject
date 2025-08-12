#!/usr/bin/env python3

import siliconcompiler as sc
from siliconcompiler.targets import freepdk45_demo

# Create chip object
chip = sc.Chip('transcendental_unit')

# Add source files
chip.input('rtl/mkTranscendentalUnit.v')
chip.input('rtl/FIFOL1.v')

# Set the top module
chip.set('design', 'top', 'mkTranscendentalUnit')

# Use FreePDK45 target
chip.use(freepdk45_demo)

# Set some basic constraints
chip.clock('CLK', period=10)  # 10ns = 100MHz

# Configure flow options - only run synthesis
chip.set('option', 'quiet', False)
chip.set('option', 'novercheck', True)
chip.set('option', 'to', ['syn'])  # Stop after synthesis

# Run the flow
chip.run()

# Display results summary
chip.summary()

print("\nSynthesis complete! Check the build directory for results.")