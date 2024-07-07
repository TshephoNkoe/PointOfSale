import tkinter as tk
from tkinter import ttk

class MsebetsiPOS(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Msebetsi Solutions POS System")
        self.geometry("800x600")

        self.style = ttk.Style()
        self.style.theme_use("clam")
        self.style.configure("TNotebook", background="#f0f0f0")
        self.style.configure("TNotebook.Tab", background="#d1e9ff", foreground="black", padding=[10, 5], font=("Arial", 10, "bold"))
        self.style.map("TNotebook.Tab", background=[("selected", "#0080ff")])

        self.create_widgets()

    def create_widgets(self):
        # Create a notebook (tabbed interface)
        self.notebook = ttk.Notebook(self)
        self.notebook.pack(expand=True, fill="both")

        # Create start page
        self.create_start_page()

        # Create inventory tab
        self.create_inventory_tab()

        # Create checkout tab
        self.create_checkout_tab()

    def create_start_page(self):
        start_page = tk.Frame(self.notebook)
        self.notebook.add(start_page, text="Start")

        label = tk.Label(start_page, text="Welcome to Msebetsi Solutions POS System", font=("Arial", 20))
        label.pack(pady=20)

        login_button = tk.Button(start_page, text="Login", command=self.show_login)
        login_button.pack(pady=10)

    def show_login(self):
        self.notebook.select(1)  # Change the index to match the inventory tab index

    def create_inventory_tab(self):
        inventory_tab = tk.Frame(self.notebook)
        self.notebook.add(inventory_tab, text="Inventory")

        # Create a frame for search bar and categories dropdown
        search_frame = tk.Frame(inventory_tab)
        search_frame.pack(side="top", fill="x", padx=10, pady=10)

        # Create search bar
        search_label = tk.Label(search_frame, text="Search:")
        search_label.pack(side="left", padx=(0, 5))
        self.search_entry = tk.Entry(search_frame, width=30)
        self.search_entry.pack(side="left", padx=(0, 5))

        # Create category dropdown
        categories = ["All", "Laptops", "iPhones", "iPads", "iMacs", "iWatches"]
        self.category_var = tk.StringVar(value="All")
        category_dropdown = ttk.Combobox(search_frame, textvariable=self.category_var, values=categories, state="readonly")
        category_dropdown.pack(side="left", padx=(0, 5))

        # Bind events to search bar and category dropdown
        self.search_entry.bind("<Return>", self.filter_inventory)
        category_dropdown.bind("<<ComboboxSelected>>", self.filter_inventory)

        # Create a treeview for displaying inventory
        self.inventory_tree = ttk.Treeview(inventory_tab, columns=("Category", "Year", "Model Number", "Specifications", "Description", "Price", "Condition"), show="headings")
        self.inventory_tree.heading("Category", text="Category")
        self.inventory_tree.heading("Year", text="Year")
        self.inventory_tree.heading("Model Number", text="Model Number")
        self.inventory_tree.heading("Specifications", text="Specifications")
        self.inventory_tree.heading("Description", text="Description")
        self.inventory_tree.heading("Price", text="Price (ZAR)")
        self.inventory_tree.heading("Condition", text="Condition")
        self.inventory_tree.pack(side="left", fill="both", expand=True)

        # Create scrollbar for the treeview
        scrollbar = ttk.Scrollbar(inventory_tab, orient="vertical", command=self.inventory_tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.inventory_tree.configure(yscrollcommand=scrollbar.set)

        # Load inventory data
        self.load_inventory()

        # Create cart display
        self.cart_display = tk.Listbox(inventory_tab, font=("Arial", 12), height=5)
        self.cart_display.pack(side="bottom", fill="x", padx=10, pady=(10, 0))

        # Add to cart button
        add_to_cart_button = tk.Button(inventory_tab, text="Add to Cart", command=self.add_to_cart)
        add_to_cart_button.pack(side="bottom", pady=(0, 10))

    def load_inventory(self):
        # Mock inventory data
        self.inventory_data = [
            {"Category": "Laptops", "Year": "2012", "Model Number": "A1278", "Specifications": "13-inch, Core i5, 8GB RAM, 256GB SSD", "Description": "Powerful and versatile.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2013", "Model Number": "A1286", "Specifications": "15-inch, Core i7, 16GB RAM, 512GB SSD", "Description": "Built for performance.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "Laptops", "Year": "2014", "Model Number": "A1502", "Specifications": "13-inch Retina, Core i5, 8GB RAM, 512GB SSD", "Description": "Sleek and portable.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2015", "Model Number": "A1534", "Specifications": "12-inch Retina, Core M, 8GB RAM, 256GB SSD", "Description": "Compact and lightweight.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2016", "Model Number": "A1706", "Specifications": "13-inch Retina, Core i5, 8GB RAM, 256GB SSD", "Description": "Perfect for everyday use.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "Laptops", "Year": "2017", "Model Number": "A1707", "Specifications": "15-inch Retina, Core i7, 16GB RAM, 512GB SSD", "Description": "Desktop-level performance.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "Laptops", "Year": "2018", "Model Number": "A1989", "Specifications": "13-inch, Core i5, 8GB RAM, 512GB SSD", "Description": "Versatile and reliable.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2019", "Model Number": "A1990", "Specifications": "15-inch Retina, Core i9, 32GB RAM, 1TB SSD", "Description": "Maximum power for demanding tasks.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "Laptops", "Year": "2020", "Model Number": "A2141", "Specifications": "16-inch Retina, Core i9, 64GB RAM, 2TB SSD", "Description": "Ultimate performance in a notebook.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2021", "Model Number": "A2338", "Specifications": "14-inch, M1 Pro, 16GB RAM, 1TB SSD", "Description": "Ultimate power for professionals.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2022", "Model Number": "A2485", "Specifications": "16-inch, M1 Max, 32GB RAM, 2TB SSD", "Description": "Desktop-class performance in a laptop.", "Price": "", "Condition": "New"},
            {"Category": "Laptops", "Year": "2023", "Model Number": "A2578", "Specifications": "14-inch, M2, 16GB RAM, 1TB SSD", "Description": "Next-generation computing.", "Price": "", "Condition": "New"},
            # Add iPhone inventory
            {"Category": "iPhones", "Year": "2012", "Model Number": "iPhone 5", "Specifications": "4-inch Retina Display, A6 Chip, 8MP Camera", "Description": "Sleek and stylish smartphone.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2013", "Model Number": "iPhone 5S", "Specifications": "4-inch Retina Display, Touch ID, A7 Chip", "Description": "Enhanced security and performance.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPhones", "Year": "2014", "Model Number": "iPhone 6", "Specifications": "4.7-inch Retina HD Display, A8 Chip, 8MP Camera", "Description": "Bigger and better.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2015", "Model Number": "iPhone 6S", "Specifications": "4.7-inch Retina HD Display, 3D Touch, A9 Chip", "Description": "The most advanced iPhone yet.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2016", "Model Number": "iPhone 7", "Specifications": "4.7-inch Retina HD Display, A10 Fusion Chip, 12MP Camera", "Description": "Water-resistant and powerful.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPhones", "Year": "2017", "Model Number": "iPhone 8", "Specifications": "4.7-inch Retina HD Display, A11 Bionic Chip, Wireless Charging", "Description": "A new generation of iPhone.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPhones", "Year": "2018", "Model Number": "iPhone X", "Specifications": "5.8-inch Super Retina Display, Face ID, A11 Bionic Chip", "Description": "The future of the smartphone.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2019", "Model Number": "iPhone 11", "Specifications": "6.1-inch Liquid Retina Display, Dual Camera System, A13 Bionic Chip", "Description": "Just the right amount of everything.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPhones", "Year": "2020", "Model Number": "iPhone 12", "Specifications": "6.1-inch Super Retina XDR Display, A14 Bionic Chip, Ceramic Shield", "Description": "Blast past fast.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2021", "Model Number": "iPhone 13", "Specifications": "6.1-inch Super Retina XDR Display, A15 Bionic Chip, Cinematic mode", "Description": "Your new superpower.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2022", "Model Number": "iPhone 14", "Specifications": "6.1-inch Super Retina XDR Display, A16 Bionic Chip, ProMotion technology", "Description": "Next-level innovation.", "Price": "", "Condition": "New"},
            {"Category": "iPhones", "Year": "2023", "Model Number": "iPhone 15", "Specifications": "6.1-inch Super Retina XDR Display, A17 Bionic Chip, Advanced Camera System", "Description": "Pushing the boundaries of what's possible.", "Price": "", "Condition": "New"},
            # Add iPad inventory
            {"Category": "iPads", "Year": "2012", "Model Number": "iPad 3", "Specifications": "9.7-inch Retina Display, A5X Chip, 5MP Camera", "Description": "The new iPad.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2013", "Model Number": "iPad 4", "Specifications": "9.7-inch Retina Display, A6X Chip, Lightning Connector", "Description": "More power. More affordable.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPads", "Year": "2014", "Model Number": "iPad Air", "Specifications": "9.7-inch Retina Display, A7 Chip, Thin and light design", "Description": "Power isn't just for the pros.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2015", "Model Number": "iPad Air 2", "Specifications": "9.7-inch Retina Display, A8X Chip, Touch ID", "Description": "So capable, you won't want to put it down.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2016", "Model Number": "iPad Pro", "Specifications": "12.9-inch Retina Display, A9X Chip, Apple Pencil support", "Description": "Anything you can do, you can do better.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPads", "Year": "2017", "Model Number": "iPad Pro 10.5", "Specifications": "10.5-inch Retina Display, A10X Fusion Chip, ProMotion technology", "Description": "All new. All screen. All powerful.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPads", "Year": "2018", "Model Number": "iPad 6", "Specifications": "9.7-inch Retina Display, A10 Fusion Chip, Apple Pencil support", "Description": "Like a computer. Unlike any computer.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2019", "Model Number": "iPad 7", "Specifications": "10.2-inch Retina Display, A10 Fusion Chip, Smart Connector", "Description": "Just what you need. Right when you need it.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iPads", "Year": "2020", "Model Number": "iPad Air 4", "Specifications": "10.9-inch Liquid Retina Display, A14 Bionic Chip, USB-C Connector", "Description": "Powerful. Colorful. Wonderful.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2021", "Model Number": "iPad Pro M1", "Specifications": "11-inch Liquid Retina Display, M1 Chip, 5G Capability", "Description": "Take your creativity further with iPad Pro.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2022", "Model Number": "iPad 10", "Specifications": "10.2-inch Retina Display, A14 Bionic Chip, True Tone technology", "Description": "Fun just got a whole lot faster.", "Price": "", "Condition": "New"},
            {"Category": "iPads", "Year": "2023", "Model Number": "iPad Air 5", "Specifications": "10.9-inch Liquid Retina Display, A15 Bionic Chip, 5G Connectivity", "Description": "The ultimate iPad experience.", "Price": "", "Condition": "New"},
            # Add iMac inventory
            {"Category": "iMacs", "Year": "2012", "Model Number": "iMac 21.5-inch", "Specifications": "2.7GHz Quad-Core Intel Core i5, 8GB RAM, 1TB HDD", "Description": "Stunningly thin design, beautiful display.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2013", "Model Number": "iMac 27-inch", "Specifications": "3.2GHz Quad-Core Intel Core i5, 8GB RAM, 1TB HDD", "Description": "Uncompromising performance.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iMacs", "Year": "2014", "Model Number": "iMac 21.5-inch Retina", "Specifications": "3.1GHz Quad-Core Intel Core i5, 8GB RAM, 1TB HDD", "Description": "Incredible detail. Unimaginable performance.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2015", "Model Number": "iMac 27-inch Retina", "Specifications": "3.2GHz Quad-Core Intel Core i5, 8GB RAM, 1TB Fusion Drive", "Description": "Retina. Now in colossal and ginormous.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2016", "Model Number": "iMac 21.5-inch 4K Retina", "Specifications": "3.1GHz Quad-Core Intel Core i5, 8GB RAM, 1TB HDD", "Description": "The vision is brighter than ever.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iMacs", "Year": "2017", "Model Number": "iMac Pro", "Specifications": "3.2GHz 8-Core Intel Xeon W, 32GB RAM, 1TB SSD", "Description": "Power to the pro.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iMacs", "Year": "2018", "Model Number": "iMac 21.5-inch 4K Retina", "Specifications": "3.6GHz Quad-Core Intel Core i3, 8GB RAM, 1TB Fusion Drive", "Description": "Pretty. Freaking powerful.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2019", "Model Number": "iMac 27-inch 5K Retina", "Specifications": "3.0GHz 6-Core Intel Core i5, 8GB RAM, 1TB Fusion Drive", "Description": "A screen worth staring at.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iMacs", "Year": "2020", "Model Number": "iMac 27-inch Retina", "Specifications": "3.3GHz 6-Core Intel Core i5, 8GB RAM, 512GB SSD", "Description": "Pretty. Freaking powerful.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2021", "Model Number": "iMac 24-inch M1", "Specifications": "Apple M1 Chip with 8-Core CPU and 8-Core GPU, 8GB RAM, 256GB SSD", "Description": "Supercharged for creativity.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2022", "Model Number": "iMac Pro 27-inch", "Specifications": "Apple M1 Ultra Chip with 20-Core CPU and 64-Core GPU, 64GB RAM, 2TB SSD", "Description": "An entirely new iMac experience.", "Price": "", "Condition": "New"},
            {"Category": "iMacs", "Year": "2023", "Model Number": "iMac 27-inch M2", "Specifications": "Apple M2 Chip with 16-Core CPU and 32-Core GPU, 32GB RAM, 1TB SSD", "Description": "Performance. Upgraded.", "Price": "", "Condition": "New"},
            # Add iWatch inventory
            {"Category": "iWatches", "Year": "2015", "Model Number": "Apple Watch Sport", "Specifications": "38mm or 42mm, Aluminum Case, Retina Display", "Description": "Stay active. Stay healthy. Stay connected.", "Price": "", "Condition": "New"},
            {"Category": "iWatches", "Year": "2016", "Model Number": "Apple Watch Series 1", "Specifications": "38mm or 42mm, Aluminum Case, S1P Chip", "Description": "The ultimate tool for a healthy life.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iWatches", "Year": "2017", "Model Number": "Apple Watch Series 2", "Specifications": "38mm or 42mm, Aluminum or Stainless Steel Case, S2 Chip", "Description": "The perfect partner for a healthy life.", "Price": "", "Condition": "Pre-loved"},
            {"Category": "iWatches", "Year": "2018", "Model Number": "Apple Watch Series 3", "Specifications": "38mm or 42mm, Aluminum or Stainless Steel Case, S3 Chip", "Description": "Stay active. Stay healthy. Stay connected.", "Price": "", "Condition": "New"},
            {"Category": "iWatches", "Year": "2019", "Model Number": "Apple Watch Series 4", "Specifications": "40mm or 44mm, Aluminum or Stainless Steel Case, S4 Chip", "Description": "The largest Apple Watch display yet.", "Price": "", "Condition": "New"},
            {"Category": "iWatches", "Year": "2020", "Model Number": "Apple Watch Series 5", "Specifications": "40mm or 44mm, Aluminum or Stainless Steel Case, S5 Chip", "Description": "The future of health is on your wrist.", "Price": "", "Condition": "New"},
            {"Category": "iWatches", "Year": "2021", "Model Number": "Apple Watch SE", "Specifications": "40mm or 44mm, Aluminum or Stainless Steel Case, S5 Chip", "Description": "Lots to love. Less to spend.", "Price": "", "Condition": "New"},
            {"Category": "iWatches", "Year": "2022", "Model Number": "Apple Watch Series 7", "Specifications": "41mm or 45mm, Aluminum or Stainless Steel Case, S7 Chip", "Description": "The largest, most advanced Apple Watch yet.", "Price": "", "Condition": "New"},
            {"Category": "iWatches", "Year": "2023", "Model Number": "Apple Watch Series 8", "Specifications": "41mm or 45mm, Aluminum or Stainless Steel Case, S8 Chip", "Description": "The next big thing is already here.", "Price": "", "Condition": "New"},
        ]

        for item in self.inventory_data:
            self.inventory_tree.insert("", "end", values=(item["Category"], item["Year"], item["Model Number"], item["Specifications"], item["Description"], item["Price"], item["Condition"]))

    def filter_inventory(self, event=None):
        search_text = self.search_entry.get().lower()
        category = self.category_var.get()

        for row in self.inventory_tree.get_children():
            self.inventory_tree.delete(row)

        for item in self.inventory_data:
            if category == "All" or item["Category"] == category:
                if search_text in item["Description"].lower():
                    self.inventory_tree.insert("", "end", values=(item["Category"], item["Year"], item["Model Number"], item["Specifications"], item["Description"], item["Price"], item["Condition"]))

    def add_to_cart(self):
        selected_item = self.inventory_tree.selection()
        if selected_item:
            item = self.inventory_tree.item(selected_item, "values")
            self.cart_display.insert("end", f"{item[2]} - {item[4]}")

    def create_checkout_tab(self):
        checkout_tab = tk.Frame(self.notebook)
        self.notebook.add(checkout_tab, text="Checkout")

        label = tk.Label(checkout_tab, text="Checkout Page", font=("Arial", 20))
        label.pack(pady=20)

        # Create a listbox for displaying items in the cart
        cart_label = tk.Label(checkout_tab, text="Cart Items", font=("Arial", 16))
        cart_label.pack(pady=10)

        self.cart_display_checkout = tk.Listbox(checkout_tab, font=("Arial", 12), height=10)
        self.cart_display_checkout.pack(pady=10)

        # Add a button to clear the cart
        clear_button = tk.Button(checkout_tab, text="Clear Cart", command=self.clear_cart)
        clear_button.pack(pady=10)

        # Add a button to go back to inventory
        back_button = tk.Button(checkout_tab, text="Back to Inventory", command=self.show_inventory)
        back_button.pack(pady=10)

    def show_inventory(self):
        self.notebook.select(1)  # Change the index to match the inventory tab index

    def clear_cart(self):
        self.cart_display_checkout.delete(0, "end")

if __name__ == "__main__":
    app = MsebetsiPOS()
    app.mainloop()
