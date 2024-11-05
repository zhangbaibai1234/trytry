import tkinter as tk
from tkinter import ttk, messagebox, simpledialog

class ERPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("学校便利店 ERP 系统")
        self.root.geometry("600x400")

        # 创建首页
        self.home_frame = ttk.Frame(self.root)
        self.home_frame.pack(expand=1, fill="both")
        self.init_home_page()

        # 创建登录页面
        self.login_frame = ttk.Frame(self.root)
        self.init_login_page()

        # 创建选项卡
        self.tab_control = ttk.Notebook(self.root)

        self.inventory_tab = ttk.Frame(self.tab_control)
        self.sales_tab = ttk.Frame(self.tab_control)
        self.order_tab = ttk.Frame(self.tab_control)
        self.finance_tab = ttk.Frame(self.tab_control)

        self.tab_control.add(self.inventory_tab, text="库存管理")
        self.tab_control.add(self.sales_tab, text="销售管理")
        self.tab_control.add(self.order_tab, text="订货管理")
        self.tab_control.add(self.finance_tab, text="财务管理")

        self.tab_control.pack(expand=1, fill="both")

        # 初始化每个模块的界面
        self.init_inventory_tab()
        self.init_sales_tab()
        self.init_order_tab()
        self.init_finance_tab()

    def init_home_page(self):
        # 导入背景图片
        background_image = tk.PhotoImage(file=r"C:\Users\zhb\Downloads\下载.jpg")  # 请确保路径正确
        background_label = tk.Label(self.home_frame, image=background_image)
        background_label.image = background_image  # 保持引用
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        label = tk.Label(self.home_frame, text="欢迎来到学校便利店 ERP 系统", font=("Arial", 16), bg="white")
        label.pack(pady=20)

        login_button = tk.Button(self.home_frame, text="登录", command=self.show_login_page)
        login_button.pack(pady=10)

    def show_login_page(self):
        self.home_frame.pack_forget()
        self.login_frame.pack(expand=1, fill="both")

    def init_login_page(self):
        label = tk.Label(self.login_frame, text="登录", font=("Arial", 16))
        label.pack(pady=20)

        username_label = tk.Label(self.login_frame, text="用户名:")
        username_label.pack(pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.pack(pady=5)

        password_label = tk.Label(self.login_frame, text="密码:")
        password_label.pack(pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.pack(pady=5)

        login_button = tk.Button(self.login_frame, text="登录", command=self.login)
        login_button.pack(pady=20)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        # 这里可以添加更复杂的认证机制
        if username == "admin" and password == "admin":
            messagebox.showinfo("登录成功", "欢迎进入系统!")
            self.login_frame.pack_forget()
            self.tab_control.pack(expand=1, fill="both")
        else:
            messagebox.showerror("登录失败", "用户名或密码错误！")

    def init_inventory_tab(self):
        label = tk.Label(self.inventory_tab, text="库存管理", font=("Arial", 16))
        label.pack(pady=10)

        self.inventory_list = tk.Listbox(self.inventory_tab)
        self.inventory_list.pack(padx=20, pady=20, fill="both", expand=True)

        # 添加功能按钮
        button_frame = ttk.Frame(self.inventory_tab)
        button_frame.pack(pady=10)

        add_item_button = tk.Button(button_frame, text="添加商品", command=self.add_item)
        add_item_button.pack(side="left", padx=5)

        remove_item_button = tk.Button(button_frame, text="移除商品", command=self.remove_item)
        remove_item_button.pack(side="left", padx=5)

        stock_check_button = tk.Button(button_frame, text="库存盘点", command=self.stock_check)
        stock_check_button.pack(side="left", padx=5)

        stock_analysis_button = tk.Button(button_frame, text="库存分析", command=self.stock_analysis)
        stock_analysis_button.pack(side="left", padx=5)

    def add_item(self):
        item = simpledialog.askstring("添加商品", "请输入商品名称:")
        quantity = simpledialog.askinteger("添加商品", "请输入商品数量:")
        if item and quantity is not None:
            self.inventory_list.insert(tk.END, f"{item} - {quantity}件")

    def remove_item(self):
        selected_item_index = self.inventory_list.curselection()
        if selected_item_index:
            self.inventory_list.delete(selected_item_index)

    def stock_check(self):
        messagebox.showinfo("库存盘点", "实现库存盘点功能")

    def stock_analysis(self):
        messagebox.showinfo("库存分析", "实现库存分析功能")

    def init_sales_tab(self):
        label = tk.Label(self.sales_tab, text="销售管理", font=("Arial", 16))
        label.pack(pady=10)

        self.sales_list = tk.Listbox(self.sales_tab)
        self.sales_list.pack(padx=20, pady=20, fill="both", expand=True)

        # 添加功能按钮
        button_frame = ttk.Frame(self.sales_tab)
        button_frame.pack(pady=10)

        record_sale_button = tk.Button(button_frame, text="记录销售", command=self.record_sale)
        record_sale_button.pack(side="left", padx=5)

        analyze_sales_button = tk.Button(button_frame, text="销售数据分析", command=self.analyze_sales)
        analyze_sales_button.pack(side="left", padx=5)

    def record_sale(self):
        item = simpledialog.askstring("记录销售", "请输入销售商品名称:")
        quantity = simpledialog.askinteger("记录销售", "请输入销售数量:")
        if item and quantity is not None:
            self.sales_list.insert(tk.END, f"{item} - {quantity}件")
            messagebox.showinfo("记录销售", "销售记录已添加。")

    def analyze_sales(self):
        messagebox.showinfo("销售数据分析", "实现销售数据分析功能")

    def init_order_tab(self):
        label = tk.Label(self.order_tab, text="订货管理", font=("Arial", 16))
        label.pack(pady=10)

        self.order_list = tk.Listbox(self.order_tab)
        self.order_list.pack(padx=20, pady=20, fill="both", expand=True)

        # 添加功能按钮
        button_frame = ttk.Frame(self.order_tab)
        button_frame.pack(pady=10)

        analyze_order_button = tk.Button(button_frame, text="库存分析", command=self.order_analysis)
        analyze_order_button.pack(side="left", padx=5)

        create_order_button = tk.Button(button_frame, text="创建订单", command=self.create_order)
        create_order_button.pack(side="left", padx=5)

    def order_analysis(self):
        messagebox.showinfo("库存分析", "实现库存分析功能")

    def create_order(self):
        item = simpledialog.askstring("创建订单", "请输入订单商品名称:")
        quantity = simpledialog.askinteger("创建订单", "请输入订单数量:")
        if item and quantity is not None:
            self.order_list.insert(tk.END, f"{item} - {quantity}件")
            messagebox.showinfo("创建订单", "订单已创建。")

    def init_finance_tab(self):
        label = tk.Label(self.finance_tab, text="财务管理", font=("Arial", 16))
        label.pack(pady=10)

        self.finance_list = tk.Listbox(self.finance_tab)
        self.finance_list.pack(padx=20, pady=20, fill="both", expand=True)

        # 添加功能按钮
        button_frame = ttk.Frame(self.finance_tab)
        button_frame.pack(pady=10)

        generate_report_button = tk.Button(button_frame, text="生成财务报表", command=self.generate_financial_report)
        generate_report_button.pack(side="left", padx=5)

        view_financials_button = tk.Button(button_frame, text="查看财务状况", command=self.view_financials)
        view_financials_button.pack(side="left", padx=5)

    def generate_financial_report(self):
        messagebox.showinfo("财务报表", "实现生成财务报表功能")

    def view_financials(self):
        messagebox.showinfo("财务状况", "实现查看财务状况功能")

if __name__ == "__main__":
    root = tk.Tk()
    app = ERPApp(root)
    root.mainloop()
