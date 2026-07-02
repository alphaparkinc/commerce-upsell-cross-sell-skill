from client import UpsellCrossSellClient
def main():
    c = UpsellCrossSellClient()
    print(c.get_offers(["phone"]))
if __name__ == '__main__':
    main()
