#! python3

import subprocess

if __name__ == "__main__":
    branches = subprocess.check_output(["git", "for-each-ref", "refs/heads", "--format=%(refname:short) %(upstream:track)"]).decode('utf-8').split('\n')[:-1]
    branches = [{"name": item.split(" ")[0], "track": item.split(" ")[1]} for item in branches]
   
    to_delete = []
   
    for branch in branches:
        if branch["track"] == "[gone]":
            to_delete.append(branch)
    
    print("Branches to delete:")
    for branch in to_delete:
        print(branch["name"])
    
    delete = input("Do you wish to delete all branches listet above? [Y/N]")
    
    if delete.lower() == "y":
        for branch in to_delete:
            print(f"Deleting: {branch['name']}")
            subprocess.run(["git", "branch", "-d", branch["name"]])
    
    print("FINNISHED")