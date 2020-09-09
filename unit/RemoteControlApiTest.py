import unittest
import subprocess  # skipcq: BAN-B404
from RemoteControlApi import ERROR_MESSAGE_RESOURCE_NOT_FOUND


class RemoteControlApiTest(unittest.TestCase):
    """This class tests the REST RemoteControlApi. The start of an AMiner instance and of the RemoteControlApi is not the task of this class
    and must be done beforehand."""
    cmd = ['curl', '-i', '-H', "Accept: application/json", '-H', "Content-Type: application/json", '-X', 'GET']
    config_property_addr = 'http://127.0.0.1:8000/config_property/%s'

    def test1get_config_property(self):
        property_name = 'MailAlerting.MaxEventsPerMessage'
        # skipcq: BAN-B603, PYL-W1510
        res = subprocess.run(self.cmd + [self.config_property_addr % property_name], capture_output=True)
        self.assertIn(b'200 OK', res.stdout)
        self.assertIn(b'content-type: application/json', res.stdout)
        self.assertIn(b'{"%s":1000}' % property_name.encode('utf-8'), res.stdout)

        property_name = 'AMinerUser'
        # skipcq: BAN-B603, PYL-W1510
        res = subprocess.run(self.cmd + [self.config_property_addr % property_name], capture_output=True)
        self.assertIn(b'200 OK', res.stdout)
        self.assertIn(b'content-type: application/json', res.stdout)
        self.assertIn(b'{"%s":"aminer"}' % property_name.encode('utf-8'), res.stdout)

        property_name = 'LogResourceList'
        # skipcq: BAN-B603, PYL-W1510
        res = subprocess.run(self.cmd + [self.config_property_addr % property_name], capture_output=True)
        self.assertIn(b'200 OK', res.stdout)
        self.assertIn(b'content-type: application/json', res.stdout)
        self.assertIn(b'{"%s":["file:///tmp/syslog"]}' % property_name.encode('utf-8'), res.stdout)

        property_name = 'NoneExistentConfigProperty'
        # skipcq: BAN-B603, PYL-W1510
        res = subprocess.run(self.cmd + [self.config_property_addr % property_name], capture_output=True)
        self.assertIn(b'404 Not Found', res.stdout)
        self.assertIn(b'content-type: application/json', res.stdout)
        self.assertIn(b'{"ErrorMessage":%s}' % ERROR_MESSAGE_RESOURCE_NOT_FOUND.replace(b'\\\\', b'\\') % property_name.encode('utf-8'),
                      res.stdout)
