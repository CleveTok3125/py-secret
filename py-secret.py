import base64, random, os
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet
class secret:
  def encrypt(s, k, r=256):
    backend = default_backend()
    salt = os.urandom(32)
    kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=salt,
      iterations=100000,
      backend=backend
    )
    fernet = Fernet(base64.urlsafe_b64encode(kdf.derive(k.encode())))
    s = fernet.encrypt(text.encode())
    s = base64.b64encode(bytes(s, 'utf-8')).decode("utf-8")
    #
    sections = ""
    for i in range(0, r):
      sections += chr(i)

    lst = []
    for i in sections:
      lst.append(i)
      
    random.seed(k)

    mixed = []
    while len(lst) > 0:
      random_element = random.randint(0, len(lst)-1)
      deleted_element = lst.pop(random_element)
      mixed.append(deleted_element)

    ans = []
    for i in s:
      not_in_case = True
      for j in range(0, len(sections)-1):
        if i == sections[j]:
          not_in_case = False
          ans.append(mixed[j])
      if not_in_case:
        ans.append(i)

    ans = ''.join(ans)
    ans = base64.b64encode(bytes(ans, 'utf-8')).decode("utf-8")
    return ans
  def decrypt(s, k, r=256):
    s = base64.b64decode(s).decode("utf-8")
    backend = default_backend()
    salt = os.urandom(32)
    kdf = PBKDF2HMAC(
      algorithm=hashes.SHA256(),
      length=32,
      salt=salt,
      iterations=100000,
      backend=backend
    )
    fernet = Fernet(base64.urlsafe_b64encode(kdf.derive(k.encode())))
    s = fernet.decrypt(s).decode()
    #
    s = base64.b64decode(s).decode("utf-8")

    sections = ""
    for i in range(0, r):
      sections += chr(i)

    lst = []
    for i in sections:
      lst.append(i)
      
    random.seed(k)

    mixed = []
    while len(lst) > 0:
      random_element = random.randint(0, len(lst)-1)
      deleted_element = lst.pop(random_element)
      mixed.append(deleted_element)

    ans = []
    for i in s:
      not_in_case = True
      for j in range(0, len(mixed)-1):
        if i == mixed[j]:
          not_in_case = False
          ans.append(sections[j])
      if not_in_case:
        ans.append(i)

    ans = ''.join(ans)
    return ans
