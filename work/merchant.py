#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 0.1.0

import os
import shutil

flutter_path = '~/Desktop/dev/dev_merchant'
flutter_path_merchant = '~/Desktop/dev/dev_merchant/merchant'
flutter_path_HLMerchant = '~/Desktop/dev/dev_merchant/HLMerchant'
native_path_HLMerchant_iOS = '~/Desktop/dev/dev_merchant/HLMerchant_iOS/HLMerchant'
vs_code_setting_path = '/Users/liaoshaolin/Library/Application\\ Support/Code/User'
podfile_path = '/Users/liaoshaolin/Desktop/dev/dev_merchant/HLMerchant_iOS/HLMerchant/Podfile'


def execute_command():
    ''' 执行 flutter pub get 与 pod update 命令 '''
    os.system('cd ' + flutter_path_merchant + ' && flutter pub upgrade')
    os.system('cd ' + flutter_path_HLMerchant + ' && flutter pub upgrade')
    os.system('cd ' + native_path_HLMerchant_iOS + ' && pod update')
    print('执行 flutter pub get 与 pod update 命令!! done 😀 \n')


def execute_model_command():
    os.system('cd ' + flutter_path_merchant +
              ' && flutter packages pub run build_runner build --delete-conflicting-outputs')


def open_x_code():
    ''' 打开 Xcode '''
    os.system('cd ' + native_path_HLMerchant_iOS +
              ' && open HLMerchant.xcworkspace')


def open_vs_code():
    ''' 打开 VSCode '''
    os.system('cd ' + flutter_path +
              ' && open -a /Applications/Visual\\ Studio\\ Code.app HLMerchant')
    os.system('cd ' + flutter_path +
              ' && open -a /Applications/Visual\\ Studio\\ Code.app merchant')


def open_vs_code_setting():
    os.system('cd ' + vs_code_setting_path +
              ' && open -a /Applications/Visual\\ Studio\\ Code.app settings.json')


def open_profile_directory():
    os.system('open ~/Library/MobileDevice/Provisioning\ Profiles/')


def kill_all_dart_progress():
    os.system('killall - dart')
    print('kill_all_dart_progress!! done 😀 \n')


def change_merchant_pod(is2Local=True, is2Release=False):
    text_io = open(podfile_path)
    pod_contents = text_io.read()
    text_io.close()

    electric_bike_pod_str = "pod 'HLMerchantElectricBikeModule'"
    electric_public_pod_str = "pod 'HLMerchantElectricPublicModule'"

    electric_bike_target_pod_str = "  pod 'HLMerchantElectricBikeModule', :path => '/Users/liaoshaolin/Desktop/dev/dev_merchant/HLMerchantElectricBikeModule_iOS'"
    electric_public_target_pod_str = "  pod 'HLMerchantElectricPublicModule', :path => '/Users/liaoshaolin/Desktop/dev/dev_merchant/HLMerchantElectricPublicModule'"

    if(is2Release):
        electric_bike_target_pod_str = "  pod 'HLMerchantElectricPublicModule'    , :git => 'https://gitlab.hellobike.cn/Rentmobile/HLMerchantElectricPublicModule.git', :branch => 'release'"
        electric_public_target_pod_str = "  pod 'HLMerchantElectricBikeModule'      , :git => 'https://gitlab.hellobike.cn/Rentmobile/HLMerchantElectricBikeModule_iOS.git', :branch => 'release'"

    pod_contents_list = pod_contents.split('\n')
    for i in range(len(pod_contents_list)):
        line = pod_contents_list[i]

        if line.find(electric_bike_pod_str) >= 0:
            pod_contents_list[i] = electric_bike_target_pod_str
        if line.find(electric_public_pod_str) >= 0:
            pod_contents_list[i] = electric_public_target_pod_str

    # 保存修改的内容
    new_pod_contents = '\n'.join(pod_contents_list)
    text_io = open(podfile_path, 'w')
    text_io.write(new_pod_contents)
    text_io.close()
    print('👏🏻👏🏻👏🏻 success')


def auto_commit_mock_code():
    # 修改这个变量即可
    # option+command+c 复制路径
    need_copy_file_path = '/Users/liaoshaolin/Desktop/mock_work_dic/josn_mock/登录注册/city_list_register.json'

    if not os.path.exists(need_copy_file_path):
        print('拷贝目标文件路径异常')
        return

    arr = need_copy_file_path.split('/')
    need_copy_file_name = arr[-1]
    git_branch_name = 'shaolin/data_local_mock'
    temp_path = '/Users/liaoshaolin/Desktop' + '/temp'
    print(f'temp_path:{temp_path}')
    if os.path.exists(temp_path):
        shutil.rmtree(temp_path)
    os.mkdir(temp_path)
    os.chdir(temp_path)
    # --depth 1: 不会 clone 所有历史，1 表示克隆最近的一次commit
    success = os.system(
        f'git clone -b {git_branch_name} --depth 1 ssh://git@gitlab.hellobike.cn:10022/Rentmobile/merchant.git')
    print(f'clone 结果：{success}')
    mock_path = temp_path + '/merchant/mock'
    copy_command = f'cp -R {need_copy_file_path} {mock_path}'
    print(f'copy_command:{copy_command}')
    os.system(copy_command)
    os.chdir('merchant')
    os.system('git add .')
    os.system(f'git commit -m "feat：+ {need_copy_file_name}"')
    os.system('git push')
    shutil.rmtree(temp_path)
    print('👏🏻👏🏻👏🏻 success')


def excuse_flutter_run():
    os.system('cd ' + flutter_path_HLMerchant + ' && flutter run')
    os.system('cd ' + native_path_HLMerchant_iOS + ' && pod update')


def excuse_flutter_clean():
    os.system('cd ' + flutter_path_merchant + ' && flutter clean')
    os.system('cd ' + flutter_path_HLMerchant + ' && flutter clean')


def setup_jpush_environment():
    ''' 项目调整为推送环境，丢手机给测试测推送 '''
    flutter_export_environment_path = '/Users/liaoshaolin/Desktop/dev/dev_merchant/HLMerchant/.ios/Flutter/flutter_export_environment.sh'
    generated_path = '/Users/liaoshaolin/Desktop/dev/dev_merchant/HLMerchant/.ios/Flutter/Generated.xcconfig'

    content1 = 'export "FLUTTER_BUILD_MODE=release"'
    content2 = 'FLUTTER_BUILD_MODE=release'

    add_content_at_last(flutter_export_environment_path, content1)
    add_content_at_last(generated_path, content2)

    print('👏🏻👏🏻👏🏻 setup_jpush_environment success')


def add_content_at_last(path, content):
    ''' 在尾部添加内容 '''

    # 获取内容
    text_io = open(path)
    contents = text_io.read()
    text_io.close()

    # 添加内容
    contents_list = contents.split('\n')
    contents_list[-1] = content

    # 保存修改的内容
    new_contents = '\n'.join(contents_list)
    text_io = open(path, 'w')
    text_io.write(new_contents)
    text_io.close()

    print('👏🏻👏🏻👏🏻 add_content_at_last success')


def main():
    show = '''
    功能列表：
    1.打开 IDE
    2.运行 flutter pub get + pod update
    3.打开 Xcode
    4.打开 VSCode      
    5.执行生成 model 命令
    6.打开 VSCode setting.json 
    7.打开描述文件目录
    8.杀掉所有 Dart 进程 
    9.change_pod_2_local 
    10.change_pod_2_release   
    11.auto_commit_mock_code   
    12.excuse_flutter_run
    13.excuse_flutter_clean       
    14.setup_jpush_environmen                                                                                                
    '''

    print(show)

    choice_function = input('请选择:')

    if choice_function == '1':
        open_x_code()
        open_vs_code()
    elif choice_function == '2':
        execute_command()
    elif choice_function == '3':
        open_x_code()
    elif choice_function == '4':
        open_vs_code()
    elif choice_function == '5':
        execute_model_command()
    elif choice_function == '6':
        open_vs_code_setting()
    elif choice_function == '7':
        open_profile_directory()
    elif choice_function == '8':
        kill_all_dart_progress()
    elif choice_function == '9':
        change_merchant_pod(is2Local=True)
    elif choice_function == '10':
        change_merchant_pod(is2Release=True)
    elif choice_function == '11':
        auto_commit_mock_code()
    elif choice_function == '12':
        excuse_flutter_run()
    elif choice_function == '13':
        excuse_flutter_clean()
    elif choice_function == '14':
        setup_jpush_environment()
    else:
        print('没有此功能')
        sys.exit(1)


if __name__ == '__main__':
    main()
