import re
from abc import ABC, abstractmethod
from typing import Optional

from overrides import EnforceOverrides


class ProfileTPM(ABC, EnforceOverrides):
    """TPM base profile class"""

    def __init__(self):
        self.test_info = {}

    def _satinize(self, x):
        if x is None:
            return None
        return x.replace('"', '').replace(' ', '')

    @property
    def manufacturer(self) -> Optional[str]:
        return self._satinize(self.test_info.get('Manufacturer'))

    @manufacturer.setter
    def manufacturer(self, value):
        assert isinstance(value, str)
        self.test_info['Manufacturer'] = self._satinize(value)

    @property
    def vendor_string(self) -> Optional[str]:
        return self._satinize(self.test_info.get('Vendor string'))

    @vendor_string.setter
    def vendor_string(self, value):
        assert isinstance(value, str)
        self.test_info['Vendor string'] = self._satinize(value)

    @property
    def firmware_version(self) -> Optional[str]:
        fv = self._satinize(self.test_info.get('Firmware version'))
        if fv:
            assert re.match(r'\d+\.\d+\.\d+\.\d+', fv)
        return fv

    @firmware_version.setter
    def firmware_version(self, value):
        value = self._satinize(value)
        assert isinstance(value, str)
        assert re.match(r'\d+\.\d+\.\d+\.\d+', value)
        self.test_info['Firmware version'] = value

    @property
    def device_name(self) -> Optional[str]:
        m = self.manufacturer
        vs = self.vendor_string
        fv = self.firmware_version
        if not m or not fv:
            return ''
        return m + (f" {vs}" if vs else '') + f" {fv}"

    def __eq__(self, other):
        if not isinstance(other, ProfileTPM):
            return False
        return self.device_name == other.device_name

    def __lt__(self, other):
        assert isinstance(other, ProfileTPM)
        if self.manufacturer != other.manufacturer:
            return self.manufacturer < other.manufacturer

        if self.vendor_string != other.vendor_string:
            return self.vendor_string < other.vendor_string

        fv_mine = [int(x) for x in self.firmware_version.split('.')]
        fv_other = [int(x) for x in other.firmware_version.split('.')]
        for mine, their in zip(fv_mine, fv_other):
            if mine < their:
                return True
            elif mine > their:
                return False

        return False

    @abstractmethod
    def add_result(self, result):
        pass
