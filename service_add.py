import os
import sys

def main():
    path_template="tezos-reward.service_template"
    path_service = "tezos-reward.service"
    dir_path = os.path.dirname(os.path.realpath(__file__))

    if len(sys.argv)==1:
        print("ERROR: Arguments not given. See list of arguments below:")
        os.system(dir_path+"/src/main.py --help")

    with open(path_template, 'r') as template_file:
        content = template_file.read()
        content = content.replace("<ABS_PATH_TO_BASE>",dir_path)
        content = content.replace("<OPTIONS>",' '.join(sys.argv[1:]))
        with open(path_service, 'w') as service_file:
            service_file.write(content)
    cmd ="systemctl enable "+path_service
    print("Running command:'{}'".format("systemctl enable "+path_service))
    os.system(cmd)

if __name__ == '__main__':
    main()