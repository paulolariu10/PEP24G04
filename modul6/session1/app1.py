class Product:

    def __init__(self):
        self.name, self.price, self.stock = input("Give (name, price, stock) for product:").split(',')

    def __repr__(self):
        return (f"{self.__class__.__name__}: ({self.name},{self.price},{self.stock})")

    def __str__(self):
        return (f"Nume: {self.name} \n"
                f"Pret: {self.price} \n"
                f"Stoc: {self.stock} \n"
                f"{40 * '-'}")


class Category:

    def __init__(self, name: str):
        self.category_name = name
        self.products = []

    def add_product(self):
        # product = input("give product:")
        product = Product()
        self.products.append(product)

    def __str__(self):
        return f"--- {self.category_name.capitalize()}"


class Shop:
    main_menu_message = 'Bun venit la magazinul Pycharm'
    main_menu_dict = {1: "Category", 2: "Produse", 3: "Iesire"}
    categories = [Category('pantofi'), Category('haine')]

    def products_menu(self):
        # code here
        pass

    def run(self):
        while True:
            print(self.main_menu_message)
            for key, value in self.main_menu_dict.items():
                print(f'\t{key}: {value}')
            selection = input('Alegeti optiunea:')
            if selection == '1':
                print(40 * '=' + '\n' + Category.__name__.upper().center(40, '=') + '\n' + 40 * '=')
                for category in self.categories:
                    print(category)
            elif selection == '2':
                self.products_menu()
