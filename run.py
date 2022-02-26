"""
Execute the conditions microservice
"""

from conditions import CONDITIONS
import os

# Port number is required to fetch from env variable
# http://docs.cloudfoundry.org/devguide/deploy-apps/environment-variable.html#PORT
cf_port = os.getenv("PORT")

if __name__ == "__main__":

	if cf_port is None:
		CONDITIONS.run( host='0.0.0.0', port=5000, debug=True )
	else:
		CONDITIONS.run( host='0.0.0.0', port=int(cf_port), debug=True )
