#coding=utf-8
import json
import sys,os
reload(sys)
sys.setdefaultencoding("utf-8")


class XJson(object):
	def __init__(self,path=None):
		if path:
			self.read_json(path)
		else:
			self.content = None
		pass
	def read_json(self,path):		
		try:
			if os.path.exists(path):
				with open(path,"r") as f:
					self.content = json.load(f)
			#else,path is json string
			else:
				self.content = json.loads(path)
			self.__content = self.content.copy()
			self._content = self.content.copy()
		except ValueError,e:
			print "json file or json string syntax error,%s"%e

	def extract(self,rule):
		if not rule:
			print "rule is None or empty"
			return []

		if not self.content:
			print "json content is None,need read json first"
			return []

		rule_list = filter(lambda x:x,rule.split("/"))  
		rule_list_count = len(rule_list)

		if rule_list_count is 1:
			return self.content[rule_list[0]]
		ans = []
		self._extract(self.content,rule_list,0,ans,rule_list_count)
		return ans

	def _extract(self,content,rule_list,index,ans,rule_list_count):
		content = content[ rule_list[index] ] 
		if index+1 < rule_list_count:
			if isinstance(content,list):
				for line in content:
					self._extract(line,rule_list,index+1,ans,rule_list_count)
			else:
				self._extract(content,rule_list,index+1,ans,rule_list_count)
		else:
			ans.append(content)


def old_extract_json():
	path = "test/template2.json"
	with open(path,"r") as f:
		json_content = json.load(f)
	for result in json_content["result"]:
		for second_category in result["secondCategoryList"]:
			for third_category in second_category["list"]:
				print third_category["name"]

if __name__ == "__main__":
	t = XJson()
	t.read_json("test/template2.json")
	print "\n".join( t.extract("result/secondCategoryList/list/name") )
	#print old_extract_json()
