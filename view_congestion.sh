#!/bin/bash

# Navigate to the routing results directory
cd /home/wcoxmiq/exp_approx/scProject/build/mkTranscendentalUnit/job_optimized/route.global/0/

# Launch KLayout with OpenROAD database support
klayout -nn /home/wcoxmiq/.sc/cache/lambdapdk-v0.1.55/lambdapdk/freepdk45/libs/*/gds/*.gds \
        reports/mkTranscendentalUnit.globalroute-error.odb

echo "If KLayout doesn't open properly, try:"
echo "openroad -gui reports/mkTranscendentalUnit.globalroute-error.odb"