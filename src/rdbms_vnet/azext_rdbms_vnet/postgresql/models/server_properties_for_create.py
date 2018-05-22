# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ServerPropertiesForCreate(Model):
    """The properties used to create a new server.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: ServerPropertiesForDefaultCreate,
    ServerPropertiesForRestore, ServerPropertiesForGeoRestore

    :param version: Server version. Possible values include: '9.5', '9.6'
    :type version: str or ~azure.mgmt.rdbms.postgresql.models.ServerVersion
    :param ssl_enforcement: Enable ssl enforcement or not when connect to
     server. Possible values include: 'Enabled', 'Disabled'
    :type ssl_enforcement: str or
     ~azure.mgmt.rdbms.postgresql.models.SslEnforcementEnum
    :param storage_profile: Storage profile of a server.
    :type storage_profile: ~azure.mgmt.rdbms.postgresql.models.StorageProfile
    :param create_mode: Constant filled by server.
    :type create_mode: str
    """

    _validation = {
        'create_mode': {'required': True},
    }

    _attribute_map = {
        'version': {'key': 'version', 'type': 'str'},
        'ssl_enforcement': {'key': 'sslEnforcement', 'type': 'SslEnforcementEnum'},
        'storage_profile': {'key': 'storageProfile', 'type': 'StorageProfile'},
        'create_mode': {'key': 'createMode', 'type': 'str'},
    }

    _subtype_map = {
        'create_mode': {'Default': 'ServerPropertiesForDefaultCreate', 'PointInTimeRestore': 'ServerPropertiesForRestore', 'GeoRestore': 'ServerPropertiesForGeoRestore'}
    }

    def __init__(self, version=None, ssl_enforcement=None, storage_profile=None):
        super(ServerPropertiesForCreate, self).__init__()
        self.version = version
        self.ssl_enforcement = ssl_enforcement
        self.storage_profile = storage_profile
        self.create_mode = None
