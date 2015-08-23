from sys import argv

class Diff:    
    
    def hash_diff(self,first,second):
        hash_one = first.split(":")[2]
        hash_two = second.split(":")[2]
        if hash_one == hash_two:
            return "same"
        else:
            return "different"

    def diff_simple(self,file1,file2):
        with open(file1,"r") as f:
            first = f.read()
            with open(file2,"r") as f:
                second = f.read()
            if first == second:
                return "same file"
            else:
                return "different"

    def diff_detailed(self,file1,file2):
        with open(file1,"r") as f:
            first = f.read()
        with open(file2,"r") as f:
            second = f.read()
        if first == second:
            return "same file"
        else:
            first = first.split("\n")
            second = second.split("\n")
            lines = []
            if len(first) == len(second):
                for ind,line in enumerate(first):
                    if line != second[ind]:
                        lines.append(str(ind)+" line number in file 2 different")
            else:
                if len(first) > len(second):
                    for ind,line in enumerate(second):
                        if line != second[ind]:
                            lines.append(str(ind)+" line number in file 2 different")
                    lines.append("all lines after "+str(len(second))+" in "+file1+" are different")
                else:
                    for ind,line in enumerate(first):
                        if line != second[ind]:
                            lines.append(str(ind)+" line number in file 1 different")
                    lines.append("all lines after "+str(len(first))+" in "+file2+" are different")
            return lines



if __name__ == '__main__':
    d = Diff()
    print d.diff_detailed(argv[1],argv[2])
    print d.diff_simple(argv[1],argv[2])
