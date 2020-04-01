import os
import sys
from unittest import TestCase

from tests.e2e.test_utils import search_uuid, run

admin_access = os.environ.get('HCA_UTIL_ADMIN_ACCESS')
admin_secret = os.environ.get('HCA_UTIL_ADMIN_SECRET')


sys.path.append(os.getcwd())


class TestAdminE2E(TestCase):
    def test_e2e_admin(self):
        profile = '--profile covid-util'

        print('# Configuring covid-util\n')
        self._assert_successful_run(f'covid-util config {admin_access} {admin_secret} {profile}', verbose=False)

        print('# Creating Upload Area\n')
        upload_area = 'testuploadarea'
        output = self._assert_successful_run(f'covid-util create {upload_area} {profile}')

        upload_area_uuid = search_uuid(output)
        self.assertTrue(upload_area_uuid, 'The upload area uuid could not be found from the output')

        print('# Selecting Upload Area\n')
        self._assert_successful_run(f'covid-util select {upload_area_uuid} {profile}')

        filename = 'tests-file.txt'
        self._assert_successful_run(f'touch {filename}')

        print('# Uploading file\n')
        self._assert_successful_run(f'covid-util upload -f {filename} {profile}')

        print('# Listing file\n')
        output = self._assert_successful_run(f'covid-util list {profile}')
        self.assertTrue(filename in output, f'file {filename} was not uploaded to {upload_area}, output: {output}')

        print('# Deleting file\n')
        self._assert_successful_run(f'covid-util delete -f {filename} {profile}')

        print('# Listing file to check if it is deleted\n')
        output = self._assert_successful_run(f'covid-util list {profile}')
        self.assertFalse(filename in output, f'file {filename} was not deleted to {upload_area}, output: {output}')

        print('# Deleting upload area\n')
        self._assert_successful_run(f'covid-util delete -d {profile}', input="y\n")

        print('# Listing upload area to check if it is deleted\n')
        select_upload, output, error = run(f'covid-util select {upload_area_uuid} {profile}')
        # TODO add back when changes to this branch is released
        # the cli command should have exit code 1 when it fails
        # self.assertEqual(1, select_upload,
        #                  f'upload area {upload_area_uuid} is not deleted, output: {output}, error:{error}')

        # cleanup
        self._assert_successful_run(f'rm {filename}')

    def _assert_successful_run(self, command: str, **kwargs):
        exit_code, output, error = run(command, **kwargs)
        self.assertEqual(0, exit_code, f'output: {output}, error:{error}')
        return output
