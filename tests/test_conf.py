from importlib import reload
import unittest
from unittest import mock
from status_collector import conf
import os

class ConfTest(unittest.TestCase):

    def test_read_redis_address(self):
        expected_redis_url = "redis://cache.asgard/0"
        with mock.patch.dict(os.environ, STATS_COLLECTOR_REDIS_URL=expected_redis_url):
            reload(conf)
            self.assertEqual(expected_redis_url, conf.REDIS_URL)

    def test_read_rabbitmq_configs(self):

        with mock.patch.dict(os.environ,
                    STATS_COLLECTOR_RABBITMQ_HOST="rmq.asgard",
                    STATS_COLLECTOR_RABBITMQ_USER="guest",
                    STATS_COLLECTOR_RABBITMQ_PWD="guest-pwd",
                    STATS_COLLECTOR_RABBITMQ_RK="routing_key",
                    STATS_COLLECTOR_RABBITMQ_VHOST="vhost"
                             ):
            reload(conf)
            self.assertEqual("rmq.asgard", conf.STATS_COLLECTOR_RABBITMQ_HOST)
            self.assertEqual("guest", conf.STATS_COLLECTOR_RABBITMQ_USER)
            self.assertEqual("guest-pwd", conf.STATS_COLLECTOR_RABBITMQ_PWD)
            self.assertEqual("routing_key", conf.STATS_COLLECTOR_RABBITMQ_RK)
            self.assertEqual("vhost", conf.STATS_COLLECTOR_RABBITMQ_VHOST)

    def test_read_mesos_master_address(self):
        expected_mesos_master_ip = "192.168.44.89"
        with mock.patch.dict(os.environ, STATS_COLLECTOR_MESOS_MASTER_IP=expected_mesos_master_ip):
            reload(conf)
            self.assertEqual(expected_mesos_master_ip, conf.STATS_COLLECTOR_MESOS_MASTER_IP)
