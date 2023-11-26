import base64, random
from Crypto.Cipher import Blowfish
from struct import pack
class secret:
  def encrypt(s, k, r=256):
    bs = Blowfish.block_size
    cipher = Blowfish.new(k.encode(), Blowfish.MODE_CBC)
    plaintext = s.encode()
    plen = bs - len(plaintext) % bs
    padding = [plen]*plen
    padding = pack('b'*plen, *padding)
    s = cipher.iv + cipher.encrypt(plaintext + padding)
    s = base64.b64encode(s).decode("utf-8")
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

    s = ''.join(ans)
    s = base64.b64decode(bytes(s, 'utf-8'))
    bs = Blowfish.block_size
    ciphertext = s
    iv = ciphertext[:bs]
    ciphertext = ciphertext[bs:]

    cipher = Blowfish.new(k.encode(), Blowfish.MODE_CBC, iv)
    msg = cipher.decrypt(ciphertext)

    last_byte = msg[-1]
    msg = msg[:- (last_byte if type(last_byte) is int else ord(last_byte))]
    return msg.decode()
