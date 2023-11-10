from Scanner import Scanner


def main():
    a = Scanner("p1.in")
    #b = Scanner("p2.in")
    #c = Scanner("p3.in")
    #d = Scanner("p1err.in")

    a.write_constants_and_identifiers("ST.out")
    a.write_pif("PIF.out")

if __name__ == '__main__':
    main()


