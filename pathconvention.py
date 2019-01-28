
#coding:utf8
class PathConvention:
	root = "/project"
	project = ""
	seq = ""
	shot = ""
	task = ""
	user = ""
	ext = ""
	ver = 1

	def dirPath(self):
		path = [self.root, self.project, self.seq, self.shot, self.task, self.user]
		return "/".join(path)


	def fileName(self):
		return "%s_%s_%s_v%03d.%s" % (self.seq, self.shot, self.task, self.ver, self.ext)


	def fullPath(self):
		return self.dirPath() + "/" + self.fileName()


	def lin2winNet(self):
		return "Z:" + self.fullPath().replace("/", "\\")

	#ip주소로 잡을 때
	def lin2winUnc(self):
		return "\\\\10.0.0.10" + self.fullPath().replace("/", "\\")


p = PathConvention()
p.project = "circle"
p.seq = "FOO"
p.shot = "0020"
p.task = "model"
p.user = "bae"
p.ext = "md"


print p.dirPath()
print p.fileName()
print p.fullPath()
print p.lin2winNet()
print p.lin2winUnc()

if __name__ == "__main__":
	print dir(p)
