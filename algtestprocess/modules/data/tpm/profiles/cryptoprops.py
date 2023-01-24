from enum import Enum
from typing import Dict, List

from algtestprocess.modules.data.tpm.profiles.base import ProfileTPM
from algtestprocess.modules.data.tpm.results.cryptoprops import CryptoPropResult


class CryptoPropCategory(Enum):
    RSA_1024 = "rsa_1024"
    RSA_2048 = "rsa_2048"
    ECC_P192 = "ecc_p192"
    ECC_P224 = "ecc_p224"
    ECC_P256 = "ecc_p256"
    ECC_P384 = "ecc_p384"
    ECC_P521 = "ecc_p521"
    ECC_BN256 = "ecc_bn256"
    ECC_BN638 = "ecc_bn638"
    ECC_SM256 = "ecc_sm256"
    ECC_P256_ECDSA = "ecc_p256_ecdsa"
    ECC_P256_ECDAA = "ecc_p256_ecdaa"
    ECC_P256_ECSCHNORR = "ecc_p256_ecschnorr"
    ECC_P384_ECDSA = "ecc_p384_ecdsa",
    ECC_P384_ECDAA = "ecc_p384_ecdaa"
    ECC_P384_ECSCHNORR = "ecc_p384_ecschnorr"
    ECC_BN256_ECDSA = "ecc_bn256_ecdsa"
    ECC_BN256_ECDAA = "ecc_bn256_ecdaa"
    ECC_BN256_ECSCHNORR = "ecc_bn256_ecschnorr"


class CryptoProps(ProfileTPM):

    def __init__(self):
        super().__init__()
        self.results: Dict[CryptoPropCategory, CryptoPropResult] = {}

    def add_result(self, result: CryptoPropResult):
        assert result.category
        category = result.category
        if not self.results.get(category):
            self.results[category] = result

    def free(self, categories: List[CryptoPropCategory]):
        for category in categories:
            result = self.results.get(category)
            if result:
                del result.data
