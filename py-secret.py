import base64, random
class secret:
  def encrypt(s, k, r=256):
    for l in range(len(k)):
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
      s = base64.b64encode(bytes(ans, 'utf-8')).decode("utf-8")
    return s

  def decrypt(s, k, r=256):
    for l in range(len(k)):
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
  return s
