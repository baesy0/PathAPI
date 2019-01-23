#coding:utf8
import os

def Projects():
	root = "/project"
	if not  os.path.exists(root):
		return [], "경로를 찾을 수 없습니다"
	projects = []
	for p in os.listdir(root):
		if p.startswith("."):
			continue
		if os.path.isfile(root + "/" + p):
			continue
		projects.append(p)
	return projects, None

if __name__ == ("__main__"):
	plist, err = Projects()
	if err:
		print err
	print plist
