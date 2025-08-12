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

# Configure flow options
chip.set('option', 'quiet', False)
chip.set('option', 'novercheck', True)
chip.set('option', 'clean', True)
chip.set('option', 'jobname', 'job_low_congestion')  # Unique job name

# More aggressive congestion reduction
# Lower density to give much more routing space
chip.set('constraint', 'density', 0.45)

# Increase core margin significantly
chip.set('constraint', 'coremargin', 1.5)

# Set lower placement density
chip.set('tool', 'openroad', 'task', 'floorplan', 'var', 'place_density', ['0.45'])

# Aggressive routing layer adjustments to reduce congestion
chip.set('tool', 'openroad', 'task', 'global_route', 'var', 'global_routing_layer_adjustment', ['metal2:0.2'])
chip.add('tool', 'openroad', 'task', 'global_route', 'var', 'global_routing_layer_adjustment', ['metal3:0.2'])
chip.add('tool', 'openroad', 'task', 'global_route', 'var', 'global_routing_layer_adjustment', ['metal4:0.15'])
chip.add('tool', 'openroad', 'task', 'global_route', 'var', 'global_routing_layer_adjustment', ['metal5:0.15'])

# Enable timing-driven placement with routability focus
chip.set('tool', 'openroad', 'task', 'global_placement', 'var', 'timing_driven', ['true'])
chip.set('tool', 'openroad', 'task', 'global_placement', 'var', 'routability_driven', ['true'])
chip.set('tool', 'openroad', 'task', 'global_placement', 'var', 'routability_check_overflow', ['20'])

# Increase routing iterations and efforts
chip.set('tool', 'openroad', 'task', 'global_route', 'var', 'overflow_iterations', ['300'])
chip.set('tool', 'openroad', 'task', 'global_route', 'var', 'allow_congestion', ['true'])

# Use congestion-aware detailed placement
chip.set('tool', 'openroad', 'task', 'detailed_placement', 'var', 'padding', ['2'])

# Run the flow
chip.run()

# Display results summary
chip.summary()

# Generate reports
chip.show()