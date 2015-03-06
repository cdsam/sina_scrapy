import hashlib
import sys
reload(sys) 
sys.setdefaultencoding("utf-8")

class NodeData(object):
    def __init__(self):
        self.hashtable_size = 10000000
        self.links_hash_table = '0' * self.hashtable_size
        self.level = 1
        
    def bloomfilter(self,url,size):
        v0 = hash(hashlib.md5(url).hexdigest())%(size - 1)
        v1 = hash(hashlib.sha1(url).hexdigest())%(size - 1)
        v2 = hash(hashlib.sha224(url).hexdigest())%(size - 1)
        v3 = hash(hashlib.sha256(url).hexdigest())%(size - 1)
        v4 = hash(hashlib.sha384(url).hexdigest())%(size - 1)
        v5 = hash(hashlib.sha512(url).hexdigest())%(size - 1)
        return [v0,v1,v2,v3,v4,v5]
    
    def judge_duplication(self,url):
            tmp_list = self.bloomfilter(url,self.hashtable_size)
            count = 0
            for i in tmp_list: 
                if self.links_hash_table[i] == '1':
                    count += 1
            if count == 6:
                return True
            else:
                for i in tmp_list:
                    self.links_hash_table = self.links_hash_table[:i] + '1' + self.links_hash_table[i+1:]
                return False
if __name__ == '__main__':
    node = NodeData()
    dup = node.judge_duplication('http://www.baidu.com')
    dup1 = node.judge_duplication('http://www.baidu.com')
        #t = bloomfilter('http://www.baidu.com',100000000)
    print dup,dup1
    print node.level
    
