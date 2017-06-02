# Licensed to the Apache Software Foundation (ASF) under one or more
# contributor license agreements.  See the NOTICE file distributed with
# this work for additional information regarding copyright ownership.
# The ASF licenses this file to You under the Apache License, Version 2.0
# (the "License"); you may not use this file except in compliance with
# the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import pytest

from tests.parser.service_templates import consume_node_cellar


@pytest.fixture
def service():
    context, _ = consume_node_cellar()
    yield context.modeling.instance


def test_execution_plugin_remote_with_operation_input(service):
    assert set(service.nodes['loadbalancer_host_1'].interfaces['Standard'].operations['create'] \
        .arguments.keys()) == set((
            'process',
            'use_sudo',
            'fabric_env',
            'script_path',
            'hide_output',
            'openstack_credential'
        ))


def test_execution_plugin_remote_with_interface_input(service):
    assert set(service.nodes['node_cellar_1'].interfaces['Maintenance'].operations['enable'] \
        .arguments.keys()) == set((
            'process',
            'use_sudo',
            'fabric_env',
            'script_path',
            'hide_output',
            'mode'
        ))
