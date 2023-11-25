import base64, random
class secret:
  def encode(s, k, r=256):
    sections = ""
    for i in range(0, r):
      sections += chr(i)

    lst = []
    for i in sections:
      lst.append(i)

    seed = 0
    for i in k:
      i = ord(i)
      seed += i**2 + 69*i - i
    random.seed(seed)

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
  def decode(s, k, r=256):
    s = base64.b64decode(s).decode("utf-8")

    sections = ""
    for i in range(0, r):
      sections += chr(i)

    lst = []
    for i in sections:
      lst.append(i)

    seed = 0
    for i in k:
      i = ord(i)
      seed += i**2 + 69*i - i
    random.seed(seed)

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