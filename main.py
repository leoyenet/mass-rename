import os, natsort, argparse
from sys import argv

parse = argparse.ArgumentParser(description="mass rename script mfr [new name] [path | optional]")

parse.add_argument("name", type=str, help="new name")
parse.add_argument("--path", "-p", type=str, help="path to rename", default=os.getcwd())
parse.add_argument("--ext", "-e", type=str, help="extention to skip", default="")


args = parse.parse_args()

def main():
    mass_rename_folders(args.name, args.path)

def mass_rename_folders(name, path):
    files = []
    for _, _, filenames in os.walk(path):
                
        files.extend(filenames)
        break
    files = natsort.natsorted(files, key=lambda y: y.lower())
    
    for i, file in enumerate(files):
        if args.ext and args.ext in file:
            continue
            
        if "." in file:
            ext:str = file.split(".")[-1]
            ext_sep = "."
        else: 
            ext:str = ""
            ext_sep = ""

        sep = ""
        if name:
            sep = "_"
            
        new:str = f"{name}{sep}{i}{ext_sep}{ext}"

        rename(path, file, new)
    
def rename(path, original, new):
    original = os.path.join(path, original)
    new = os.path.join(path, new)
    os.rename(original, new)
    # print(original, new)

if __name__ == "__main__":
    main()