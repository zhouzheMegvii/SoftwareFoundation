import shell

if __name__ == '__main__':
    shell.embeded_shell(['rm .*aux'])
    shell.embeded_shell(['rm makefile*'])
    shell.embeded_shell(['rm *.conf'])