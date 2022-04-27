#! /usr/bin/python
import os

print("**************** Re-configure Site details ******************")
os.system(". venv/bin/activate && python -c 'import setup_facility_details;  "
          "setup_facility_details.get_facility_name()'")
print("**************** FINISHED ******************")