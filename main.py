# Copyright (c) HashiCorp, Inc.
# SPDX-License-Identifier: MPL-2.0

import hvac
import sys

# Authentication
client = hvac.Client(
    url='http://127.0.0.1:8200',
    token='dev',
)

# Writing a secret
# create_response = client.secrets.kv.v2.create_or_update_secret(
#     path='my-secret-password',
#     secret=dict(password='Hashi123'),
# )
# print(create_response)
# print('Secret written successfully.')

# Reading a secret
secret_version_response = client.secrets.kv.v2.read_secret_version(
    path='database',
    mount_point = "secretttt"
)
print(secret_version_response, "read_response")
 

# if password != 'Hashi123':
#     sys.exit('unexpected password')

# print('Access granted!')