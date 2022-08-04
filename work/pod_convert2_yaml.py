
def main():
    file_path = '/Users/liaoshaolin/Desktop/Podfile.lock'
    with open(file_path, encoding='utf-8') as file_object:
        contents = file_object.readlines()
    for content in contents:
        line = content.rstrip()
        if '  -' == line[:3] and '/' not in line:
            target_name_left_index = line.find('- ')
            version_left_index = line.find('(')
            version_right_index = line.find(')')
            target_name = line[target_name_left_index +
                               1: version_left_index].strip()
            target_version = line[version_left_index +
                                  1: version_right_index].strip()
            print(f"{target_name} \t {target_version}")
            write(target_name, target_version)


def write(name, version):
    file_name = '/Users/liaoshaolin/Desktop/hellobike_pod.yaml'
    with open(file_name, 'a') as file_object:
        str = f'''- module: {name}
  description: {name}
  department: null
  pod: {name}
  subspec: null
  version: {version}
  git: null
  commit: null
  release: true
  source: false
'''
        file_object.write(str)


if __name__ == '__main__':
    main()
