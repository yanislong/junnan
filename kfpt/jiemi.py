#!/usr/bin/python
# -*- coding=utf-8 -*-

import requests
import chardet
import suds
import config
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

txt = "H4sIAAAAAAAAAF1RXU+DMBT9K4R37C3MAMtdlwp3s5EC0mLiEw+6mCXKEk2MP98CcwP7dj56z7ktbn8+3r3vw+fX8dRvfH4DvnfoX06vx/5t47d2FyT+VmAtsweyAu9J5gIbMnVVGuqyKicB40G2ZK8mbfZipo4wa411Pl3L8llwgAjZgkJDzZPKzrMshF1lOwCObCFcQ6zSJELgcQBJAKkH6TpK1pDMgkcLsmmFuyp3KYUybikqSFNph1ZdQ48tjUXc+CgGDquh2pLHP6RywUMeQwKpewJ+G6WrIfAiOmNdNdbdNm1hBR/EOYE7qYpOkzFyP3T7By/F2FSUTa3Z+Td+AbBp68O8AQAA"
def jiemi(baowen):
    txt = "H4sIAAAAAAAAAFWQwU7DMAyG7zxF1fuIkzFaTV6mkHqjYm1KkyL1lANMaFLpJBCIx6dllZZavvi35e+3cfv70UU/x8+v07nfxPwW4ujYv57fTv37Jm7cbpHGW3mDldJP5CQ+mKyVWNNzQ9b5PJNc8ARSSACAr4RIkQVNtG2pfU22OTgJyMISdyo/+IKsVXuS/XfXIZtJyC6wR1LZiLSVKS15bTKSMAYfWaF6HSrsflo5k1A3gzFtikqVreQAS2QzCS3VL7me9jlYemc8gBish40ryOUFSQE8WUA6ZMT5enW/hrsA/D+C7HIGmx75B2yeKUt4AQAA"
    r = requests.get(config.decode, params={'requestXml':baowen})
    print "请求返回的解密后报文:\n", r.content
    return r.content

if __name__ == "__main__":
    jiemi(txt)
    
