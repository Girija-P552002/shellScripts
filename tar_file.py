import tarfile

tar_file = tarfile.open("files.tar.gz", "w:gz")
for name in ["log1.py", "reverse.sh", "sort.sh"]:
	tar_file.add(name)
tar_file.close()
