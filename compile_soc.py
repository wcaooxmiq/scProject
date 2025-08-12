#!/usr/bin/env python3

import siliconcompiler as sc
from siliconcompiler.targets import freepdk45_demo
import os

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
chip.clock('CLK', period=10)  # scProject/build/mkTranscendentalUnit/job0/syn10ns = 100MHz

# Configure flow options
chip.set('option', 'quiet', False)
chip.set('option', 'novercheck', True)
chip.set('option', 'clean', True)  # Clean previous runs
chip.set('option', 'jobname', 'job0')  # Set explicit job name

# Ensure we're in the right directory
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Run the flow
chip.run()

# Display results summary
chip.summary()

# Generate reports
chip.show()