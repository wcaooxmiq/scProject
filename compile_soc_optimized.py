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
chip.clock('CLK', period=10)  # 10ns = 100MHz

# Configure flow options
chip.set('option', 'quiet', False)
chip.set('option', 'novercheck', True)
chip.set('option', 'clean', True)
chip.set('option', 'jobname', 'job_optimized')  # Unique job name

# Optimized density for performance while avoiding congestion
# Start with 0.65-0.7 (default is often 0.7-0.8)
chip.set('constraint', 'density', 0.65)

# Minimal core margin increase (just enough to help routing)
chip.set('constraint', 'coremargin', 1.2)  # Small increase from default 1.0

# Set placement density slightly lower to give router more space
chip.set('tool', 'openroad', 'task', 'floorplan', 'var', 'place_density', ['0.65'])

# Fine-tune routing resources - adjust global routing layer adjustments
chip.set('tool', 'openroad', 'task', 'global_route', 'var', 'global_routing_layer_adjustment', ['metal2:0.4'])
chip.add('tool', 'openroad', 'task', 'global_route', 'var', 'global_routing_layer_adjustment', ['metal3:0.4'])

# Enable timing-driven global placement
chip.set('tool', 'openroad', 'task', 'global_placement', 'var', 'timing_driven', ['true'])
chip.set('tool', 'openroad', 'task', 'global_placement', 'var', 'routability_driven', ['true'])

# Increase routing effort
chip.set('tool', 'openroad', 'task', 'global_route', 'var', 'overflow_iterations', ['200'])

# Run the flow
chip.run()

# Display results summary
chip.summary()

# Generate reports
chip.show()