from amzqr import amzqr


def main():
    msg = 'https://github.com'
    amzqr.run(msg, version=2, level='H',
              picture='123.gif', colorized=True)


if __name__ == '__main__':
    main()
