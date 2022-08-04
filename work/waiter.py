import os
import sys

# flutter 路径
flutter_path = '~/Desktop/dev/waiter'

# flutter 壳
HLWaiter_Flutter = '~/Desktop/dev/waiter/HLWaiter_Flutter'

# 原生 iOS
HLWaiter_iOS = '~/Desktop/dev/waiter/HLWaiter_iOS/Waiter'

# flutter 业务
HLWaiterElectricBikeModule_Flutter = '~/Desktop/dev/waiter/HLWaiterElectricBikeModule_Flutter'

# 原生业务
HLWaiterElectricBikeModule_iOS = '~/Desktop/dev/waiter/HLWaiterElectricBikeModule_iOS'


def open_x_code():
    ''' 打开 Xcode '''
    os.system('cd ' + HLWaiter_iOS +
              ' && open Waiter.xcworkspace')


def open_vs_code():
    ''' 打开 VSCode '''
    os.system('cd ' + flutter_path +
              ' && open -a /Applications/Visual\\ Studio\\ Code.app HLWaiter_Flutter')
    os.system('cd ' + flutter_path +
              ' && open -a /Applications/Visual\\ Studio\\ Code.app HLWaiterElectricBikeModule_Flutter')


def execute_model_command():
    os.system('cd ' + HLWaiterElectricBikeModule_Flutter +
              ' && flutter packages pub run build_runner build --delete-conflicting-outputs')


def execute_command():
    ''' 执行 flutter pub get 与 pod update 命令 '''
    os.system('cd ' + HLWaiterElectricBikeModule_Flutter +
              ' && flutter pub get')
    os.system('cd ' + HLWaiter_Flutter + ' && flutter pub get')
    os.system('cd ' + HLWaiter_iOS + ' && pod install')
    print('执行 flutter pub get 与 pod update 命令!! done 😀 \n')


def execute_model_command():
    os.system('cd ' + HLWaiterElectricBikeModule_Flutter +
              ' && flutter packages pub run build_runner build --delete-conflicting-outputs')


def main():
    show = '''
    1.打开 IDE
    2.运行 flutter pub get + pod update
    3.打开 Xcode
    4.打开 VSCode      
    5.执行生成 model 命令                                                 
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
    else:
        print('没有此功能')
        sys.exit(1)


if __name__ == '__main__':
    main()
