import base64
import hashlib
import secrets
from typing import Optional

def scrypt_hash(password: str, salt: bytes, n: int = SCRYPT_N, r: int = SCRYPT_R,
p: int = SCRYPT_P, dklen: int = DKLEN) -> bytes:
return hashlib.scrypt(password.encode("utf-8"), salt=salt, n=n, r=r, p=p, dklen=dklen)
def verify_password(input_pw: str, stored_salt_b64: str, stored_hash_b64: str,
n: int = SCRYPT_N, r: int = SCRYPT_R, p: int = SCRYPT_P,
dklen: int = DKLEN) -> bool:
"""Return True iff input_pw matches stored hash.
- stored_salt_b64 and stored_hash_b64 are base64-encoded strings.
- Use constant-time comparison via secrets.compare_digest.
TODO: implement
"""
raise NotImplementedError