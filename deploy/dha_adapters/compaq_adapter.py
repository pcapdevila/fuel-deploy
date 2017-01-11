###############################################################################
# Copyright (c) 2015 Ericsson AB and others.
#           (c) 2016 Enea Software AB
# szilard.cserey@ericsson.com
# All rights reserved. This program and the accompanying materials
# are made available under the terms of the Apache License, Version 2.0
# which accompanies this distribution, and is available at
# http://www.apache.org/licenses/LICENSE-2.0
###############################################################################


import time
from hardware_adapter import HardwareAdapter

from common import (
    log,
    exec_cmd,
    err,
)


class CompaqAdapter(HardwareAdapter):

    def __init__(self, yaml_path, attempts=20, delay=3):
        super(CompaqAdapter, self).__init__(yaml_path)
        self.attempts = attempts
        self.delay = delay

    def get_access_info(self, node_id):
        ip = self.get_node_property(node_id, 'ipmiIp')
        username = self.get_node_property(node_id, 'ipmiUser')
        password = self.get_node_property(node_id, 'ipmiPass')
        ipmiport = self.get_node_property(node_id, 'ipmiPort')
        return ip, username, password, ipmiport

    def get_node_pxe_mac(self, node_id):
        mac_list = []
        mac_list.append(self.get_node_property(node_id, 'pxeMac').lower())
        return mac_list

    def _node_power_cmd(self, node_id, cmd):
            return

    def node_power_on(self, node_id):
        log('Power ON Node %s' % node_id)

    def node_power_off(self, node_id):
        log('Power OFF Node %s' % node_id)

    def node_reset(self, node_id):
        log('RESET Node %s' % node_id)

    def node_set_boot_order(self, node_id, boot_order_list):
        log('Set boot order %s on Node %s' % (boot_order_list, node_id))
