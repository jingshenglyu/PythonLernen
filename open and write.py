# file = open('python.txt')
# text = file.read()
# print(text)
# file.close() # muss close. Otherwise always run.

# with open(r"C:\Users\Jason\Desktop\python.txt") as f:
#     print(f.read())

with open('python.txt', 'a') as f:
    f.write('hello world\n My name is Jason.\n How r u?')
# print(help(open))
