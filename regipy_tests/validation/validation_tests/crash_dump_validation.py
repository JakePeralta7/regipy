
from regipy.plugins.system.crash_dump import CrashDumpPlugin
from regipy_tests.validation.validation import ValidationCase


class CrashDumpPluginValidationCase(ValidationCase):
    plugin = CrashDumpPlugin
    test_hive_file_name = "SYSTEM.xz"
    exact_expected_result = None

            