s = ''
def main(a):
    global s 
    for i in a:
        if type(i) is list:
            main(i)
        else:
            s += str(i) 


if __name__ == '__main__':
    a = ['a',1,[12,3,['w','r',[2,'4']]]]
    main(a)
    print(s)
