##
## Bulid and load Metatab data packages
## for comments and course-enrollments
##

CKAN_GROUP=education

.PHONY: wordpress
	

PACKAGE_NAMES=\
cde.ca.gov-absenteeism \
cde.ca.gov-current_expense \
cde.ca.gov-calpads_upc \
cde.ca.gov-frpm \
cde.ca.gov-caaspp \
cde.ca.gov-reimbursements

# This one is really slow, too slow to build on TravisCI
# cde.ca.gov-fitnessgram-1999e-ca

# This one is broken
# cde.ca.gov-accountability_dashboard

include include.mk

