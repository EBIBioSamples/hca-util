from pathlib import Path

# when true, displays exception details; otherwise user-friendly error message
DEBUG_MODE = True

MAX_DIR_DEPTH = 5

# user home directory
USER_HOME = str(Path.home())

# aws config and credentials files
AWS_CONFIG_FILE = USER_HOME + '/.aws/config'
AWS_CREDENTIALS_FILE = USER_HOME + '/.aws/credentials'

AWS_SECRET_NAME = 'hca/util/secret'

# default profile uses credentials from [DEFAULT_PROFILE] section of AWS_CREDENTIALS_FILE
# and config from [profile DEFAULT_PROFILE] section of AWS_CONFIG_FILE
DEFAULT_PROFILE = 'hca-util'
DEFAULT_REGION = 'us-east-1'

# local state for user
LOCAL_STATE_FILE = USER_HOME + '/.hca-util'

# 2 IAM user types: admin and (normal) user
# in the context of hca, admin=wrangler and user=contributor
IAM_USER = 'HCAContributor'
IAM_ADMIN = 'HCAWrangler'

AWS_ACCOUNT = '871979166454'
