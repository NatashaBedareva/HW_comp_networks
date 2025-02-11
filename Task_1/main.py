from subprocess import check_output
import sys

import pandas as pd


def read_file(path):
    hostnames = []
    with open(path, 'r') as file:
        for line in file:
            hostnames.append(line.strip())
    return hostnames

def ping_to_csv(data,path_output):
    df = pd.DataFrame(data)
    df.columns=['host_name','average_speed']
    df.to_csv(path_output, index=False)

def main(path_input,path_output):
    data = []
    hostnames = read_file(path_input)

    for hostname in hostnames:
        out = int(check_output("ping -n 1 " + hostname).split()[-2])
        data.append([hostname, out])

    ping_to_csv(data, path_output)

if __name__=="__main__":
    if len(sys.argv) > 2:
        main(sys.argv[1], sys.argv[2])
    else:
        print("Arguments is not correct")

