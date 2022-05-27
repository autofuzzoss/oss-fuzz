# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
################################################################################
"""Tests for trial_build.py."""
import unittest
from unittest import mock

import trial_build


class GetProjectsToBuild(unittest.TestCase):
  """Tests for get_projects_to_build."""

  PROJECTS = ['myproject', 'myfailingproject']

  @mock.patch('trial_build._get_production_build_statuses',
              return_value={'myproject': True, 'myfailingproject': False})
  def test_force_build(self, mock_get_production_build_statuses):
    """Tests force build works."""
    del mock_get_production_build_statuses
    buildable_projects = trial_build.get_projects_to_build(
        self.PROJECTS, 'fuzzing', True)
    self.assertEqual(self.PROJECTS, buildable_projects)

  @mock.patch('trial_build._get_production_build_statuses',
              return_value={'myproject': True, 'myfailingproject': False})
  def test_get_projects_to_build(self, mock_get_production_build_statuses):
    """Tests get_projects_to_build works."""
    del mock_get_production_build_statuses
    buildable_projects = trial_build.get_projects_to_build(
        self.PROJECTS, 'fuzzing', True)
    self.assertEqual(self.PROJECTS, buildable_projects)
