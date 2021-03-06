##
## Bulid and load Metatab data packages
## for comments and course-enrollments
##

GROUPS=cde.ca.gov
TAGS=education

#WP_SITE=local
WP_SITE=data.sandiegodata.org

S3_BUCKET=library.metatab.org

PACKAGE_NAMES=\
cde.ca.gov-current_expense \
cde.ca.gov-calpads_upc \
cde.ca.gov-frpm \
cde.ca.gov-caaspp \
cde.ca.gov-reimbursements \
cde.ca.gov-cacfp_sites \
cde.ca.gov-schools  \
cde.ca.gov-enrollment \
sandiegodata.org-sd_demo_links-ca \
census.gov-district_demo-ca


BROKEN=\
cde.ca.gov-absenteeism 


# This one is really slow, too slow to build on TravisCI
# cde.ca.gov-fitnessgram-1999e-ca

# This one is broken
# cde.ca.gov-accountability_dashboard


include $(shell mp mk)
