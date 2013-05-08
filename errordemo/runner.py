from django.test.simple import DjangoTestSuiteRunner

from nose.core import TestProgram


class BasicNoseRunner(DjangoTestSuiteRunner):
    def run_tests(self, test_labels, extra_tests=None):
        TestProgram(argv=['nosetests'])
        return self.suite_result({}, None)
