import tkinter as tk
from tkinter import ttk, messagebox
import math

class EMICalculator:
    """EMI and Loan Eligibility Calculator with three functional tabs."""
    
    def __init__(self, root):
        self.root = root
        self.root.title("EMI and Loan Eligibility Calculator")
        self.root.geometry("900x700")
        self.root.minsize(700, 500)
        self.root.resizable(True, True)
        
        # Apply a modern-looking theme and base styles
        self.root.configure(bg='#f5f6f7')
        style = ttk.Style(self.root)
        try:
            style.theme_use('clam')
        except Exception:
            pass
        # Use a clean Windows-like font
        self.root.option_add('*Font', ('Segoe UI', 10))
        style.configure('TFrame', background='#f5f6f7')
        style.configure('TLabel', background='#f5f6f7')
        style.configure('Header.TLabel', font=('Segoe UI', 14, 'bold'), background='#f5f6f7')
        style.configure('Card.TLabelframe', background='white', borderwidth=1, relief='flat')
        style.configure('Card.TLabelframe.Label', font=('Segoe UI', 12, 'bold'))
        style.configure('Result.TLabel', font=('Segoe UI', 12, 'bold'), foreground='#148a08')
        style.configure('Accent.TButton', foreground='white', background='#0078D7')
        style.map('Accent.TButton', background=[('active', '#005A9E')])

        # Main frame to hold header and notebook
        main_frame = ttk.Frame(root)
        main_frame.pack(fill='both', expand=True, padx=10, pady=10)

        # Header: title (left) and license button (right)
        header_frame = ttk.Frame(main_frame)
        header_frame.grid(row=0, column=0, columnspan=2, sticky='ew', pady=(4, 8))
        header_frame.columnconfigure(0, weight=1)
        app_title = ttk.Label(header_frame, text="EMI and Loan Eligibility Calculator", style='Header.TLabel')
        app_title.grid(row=0, column=0, sticky='w')
        self.license_button = ttk.Button(header_frame, text="License", command=self.show_license, style='Accent.TButton')
        self.license_button.grid(row=0, column=1, sticky='e')

        # Create Notebook (Tab Container)
        self.notebook = ttk.Notebook(main_frame)
        self.notebook.grid(row=1, column=0, columnspan=2, sticky='nsew')

        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(1, weight=1)
        
        # Create three tabs
        self.tab1 = ttk.Frame(self.notebook, padding="20")
        self.tab2 = ttk.Frame(self.notebook, padding="20")
        self.tab3 = ttk.Frame(self.notebook, padding="20")
        
        self.notebook.add(self.tab1, text="Find EMI")
        self.notebook.add(self.tab2, text="Loan Eligibility")
        self.notebook.add(self.tab3, text="Duration Planner")
        
        # Initialize each tab
        self.setup_tab1_find_emi()
        self.setup_tab2_loan_eligibility()
        self.setup_tab3_duration_planner()
    
    # ============ TAB 1: Find EMI ============
    def setup_tab1_find_emi(self):
        """Tab 1: Calculate EMI from Loan Amount, Interest Rate, and Duration"""
        
        # Loan Amount
        ttk.Label(self.tab1, text="Loan Amount (₹):", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=10)
        self.loan_amount_slider_tab1 = ttk.Scale(self.tab1, from_=100000, to=10000000, orient='horizontal', length=300)
        self.loan_amount_slider_tab1.set(500000)
        self.loan_amount_slider_tab1.grid(row=0, column=1, padx=10)
        self.loan_amount_entry_var_tab1 = tk.StringVar(value="500000")
        self.loan_amount_entry_tab1 = ttk.Entry(self.tab1, textvariable=self.loan_amount_entry_var_tab1, width=12)
        self.loan_amount_entry_tab1.grid(row=0, column=2, padx=10)
        self.loan_amount_label_tab1 = ttk.Label(self.tab1, text="₹500,000", font=('Arial', 10))
        self.loan_amount_label_tab1.grid(row=0, column=3)
        self.loan_amount_slider_tab1.config(command=self.on_tab1_loan_amount_slider)
        self.loan_amount_entry_tab1.bind('<Return>', self.on_tab1_loan_amount_entry)
        self.loan_amount_entry_tab1.bind('<FocusOut>', self.on_tab1_loan_amount_entry)
        
        # Interest Rate
        ttk.Label(self.tab1, text="Annual Interest Rate (%):", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=10)
        self.interest_rate_slider_tab1 = ttk.Scale(self.tab1, from_=1, to=20, orient='horizontal', length=300)
        self.interest_rate_slider_tab1.set(8)
        self.interest_rate_slider_tab1.grid(row=1, column=1, padx=10)
        self.interest_rate_entry_var_tab1 = tk.StringVar(value="8.00")
        self.interest_rate_entry_tab1 = ttk.Entry(self.tab1, textvariable=self.interest_rate_entry_var_tab1, width=12)
        self.interest_rate_entry_tab1.grid(row=1, column=2, padx=10)
        self.interest_rate_label_tab1 = ttk.Label(self.tab1, text="8.00%", font=('Arial', 10))
        self.interest_rate_label_tab1.grid(row=1, column=3)
        self.interest_rate_slider_tab1.config(command=self.on_tab1_interest_rate_slider)
        self.interest_rate_entry_tab1.bind('<Return>', self.on_tab1_interest_rate_entry)
        self.interest_rate_entry_tab1.bind('<FocusOut>', self.on_tab1_interest_rate_entry)
        
        # Duration (Years)
        ttk.Label(self.tab1, text="Loan Duration (Years):", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky='w', pady=10)
        self.duration_slider_tab1 = ttk.Scale(self.tab1, from_=1, to=30, orient='horizontal', length=300)
        self.duration_slider_tab1.set(5)
        self.duration_slider_tab1.grid(row=2, column=1, padx=10)
        self.duration_entry_var_tab1 = tk.StringVar(value="5")
        self.duration_entry_tab1 = ttk.Entry(self.tab1, textvariable=self.duration_entry_var_tab1, width=12)
        self.duration_entry_tab1.grid(row=2, column=2, padx=10)
        self.duration_label_tab1 = ttk.Label(self.tab1, text="5 years", font=('Arial', 10))
        self.duration_label_tab1.grid(row=2, column=3)
        self.duration_slider_tab1.config(command=self.on_tab1_duration_slider)
        self.duration_entry_tab1.bind('<Return>', self.on_tab1_duration_entry)
        self.duration_entry_tab1.bind('<FocusOut>', self.on_tab1_duration_entry)
        
        # Results Frame
        ttk.Separator(self.tab1, orient='horizontal').grid(row=3, column=0, columnspan=4, sticky='ew', pady=20)
        
        results_frame = ttk.LabelFrame(self.tab1, text="Calculation Results", padding="15", style='Card.TLabelframe')
        results_frame.grid(row=4, column=0, columnspan=4, sticky='ew', pady=10)
        
        ttk.Label(results_frame, text="Monthly EMI:", font=('Arial', 11, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        self.emi_result_tab1 = ttk.Label(results_frame, text="₹0", font=('Arial', 12, 'bold'), foreground='green')
        self.emi_result_tab1.grid(row=0, column=1, sticky='w', padx=20)
        
        ttk.Label(results_frame, text="Total Amount:", font=('Arial', 11, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        self.total_amount_tab1 = ttk.Label(results_frame, text="₹0", font=('Arial', 12))
        self.total_amount_tab1.grid(row=1, column=1, sticky='w', padx=20)
        
        ttk.Label(results_frame, text="Total Interest:", font=('Arial', 11, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        self.total_interest_tab1 = ttk.Label(results_frame, text="₹0", font=('Arial', 12))
        self.total_interest_tab1.grid(row=2, column=1, sticky='w', padx=20)
        
        self.update_tab1_emi()
    
    def update_tab1_emi(self, event=None):
        """Calculate and update EMI for Tab 1"""
        loan_amount = int(self.loan_amount_slider_tab1.get())
        interest_rate = float(self.interest_rate_slider_tab1.get())
        duration_years = int(self.duration_slider_tab1.get())
        
        # Update labels
        self.loan_amount_label_tab1.config(text=f"₹{loan_amount:,}")
        self.interest_rate_label_tab1.config(text=f"{interest_rate:.2f}%")
        self.duration_label_tab1.config(text=f"{duration_years} year{'s' if duration_years != 1 else ''}")
        
        # Calculate EMI
        emi = self.calculate_emi(loan_amount, interest_rate, duration_years)
        total_amount = emi * duration_years * 12
        total_interest = total_amount - loan_amount
        
        self.emi_result_tab1.config(text=f"₹{emi:,.2f}")
        self.total_amount_tab1.config(text=f"₹{total_amount:,.2f}")
        self.total_interest_tab1.config(text=f"₹{total_interest:,.2f}")

    def parse_int_value(self, value, default, min_value, max_value):
        try:
            clean = str(value).replace(',', '').replace('₹', '').strip()
            parsed = int(float(clean))
        except (ValueError, TypeError):
            return default
        return max(min_value, min(max_value, parsed))

    def parse_float_value(self, value, default, min_value, max_value):
        try:
            clean = str(value).replace(',', '').replace('₹', '').strip()
            parsed = float(clean)
        except (ValueError, TypeError):
            return default
        return max(min_value, min(max_value, parsed))

    def on_tab1_loan_amount_slider(self, value):
        amount = int(float(value))
        self.loan_amount_entry_var_tab1.set(f"{amount:,}")
        self.update_tab1_emi()

    def on_tab1_loan_amount_entry(self, event=None):
        amount = self.parse_int_value(self.loan_amount_entry_var_tab1.get(), 500000, 100000, 10000000)
        self.loan_amount_slider_tab1.set(amount)
        self.loan_amount_entry_var_tab1.set(f"{amount:,}")
        self.update_tab1_emi()

    def on_tab1_interest_rate_slider(self, value):
        rate = float(value)
        self.interest_rate_entry_var_tab1.set(f"{rate:.2f}")
        self.update_tab1_emi()

    def on_tab1_interest_rate_entry(self, event=None):
        rate = self.parse_float_value(self.interest_rate_entry_var_tab1.get(), 8.0, 1.0, 20.0)
        self.interest_rate_slider_tab1.set(rate)
        self.interest_rate_entry_var_tab1.set(f"{rate:.2f}")
        self.update_tab1_emi()

    def on_tab1_duration_slider(self, value):
        duration = int(float(value))
        self.duration_entry_var_tab1.set(str(duration))
        self.update_tab1_emi()

    def on_tab1_duration_entry(self, event=None):
        duration = self.parse_int_value(self.duration_entry_var_tab1.get(), 5, 1, 30)
        self.duration_slider_tab1.set(duration)
        self.duration_entry_var_tab1.set(str(duration))
        self.update_tab1_emi()

    def on_tab2_earning_slider(self, value):
        amount = int(float(value))
        self.earning_entry_var_tab2.set(f"{amount:,}")
        self.update_tab2_eligibility()

    def on_tab2_earning_entry(self, event=None):
        amount = self.parse_int_value(self.earning_entry_var_tab2.get(), 50000, 10000, 1000000)
        self.earning_slider_tab2.set(amount)
        self.earning_entry_var_tab2.set(f"{amount:,}")
        self.update_tab2_eligibility()

    def on_tab2_existing_emi_slider(self, value):
        amount = int(float(value))
        self.existing_emi_entry_var_tab2.set(f"{amount:,}")
        self.update_tab2_eligibility()

    def on_tab2_existing_emi_entry(self, event=None):
        amount = self.parse_int_value(self.existing_emi_entry_var_tab2.get(), 0, 0, 200000)
        self.existing_emi_slider_tab2.set(amount)
        self.existing_emi_entry_var_tab2.set(f"{amount:,}")
        self.update_tab2_eligibility()

    def on_tab2_emi_nmi_slider(self, value):
        ratio = float(value)
        self.emi_nmi_entry_var_tab2.set(f"{ratio:.1f}")
        self.update_tab2_eligibility()

    def on_tab2_emi_nmi_entry(self, event=None):
        ratio = self.parse_float_value(self.emi_nmi_entry_var_tab2.get(), 10.0, 0.0, 50.0)
        self.emi_nmi_slider_tab2.set(ratio)
        self.emi_nmi_entry_var_tab2.set(f"{ratio:.1f}")
        self.update_tab2_eligibility()

    def on_tab2_interest_rate_slider(self, value):
        rate = float(value)
        self.interest_rate_entry_var_tab2.set(f"{rate:.2f}")
        self.update_tab2_eligibility()

    def on_tab2_interest_rate_entry(self, event=None):
        rate = self.parse_float_value(self.interest_rate_entry_var_tab2.get(), 8.0, 1.0, 20.0)
        self.interest_rate_slider_tab2.set(rate)
        self.interest_rate_entry_var_tab2.set(f"{rate:.2f}")
        self.update_tab2_eligibility()

    def on_tab2_duration_slider(self, value):
        duration = int(float(value))
        self.duration_entry_var_tab2.set(str(duration))
        self.update_tab2_eligibility()

    def on_tab2_duration_entry(self, event=None):
        duration = self.parse_int_value(self.duration_entry_var_tab2.get(), 5, 1, 30)
        self.duration_slider_tab2.set(duration)
        self.duration_entry_var_tab2.set(str(duration))
        self.update_tab2_eligibility()

    def on_tab3_loan_amount_slider(self, value):
        amount = int(float(value))
        self.loan_amount_entry_var_tab3.set(f"{amount:,}")
        self.update_tab3_planner()

    def on_tab3_loan_amount_entry(self, event=None):
        amount = self.parse_int_value(self.loan_amount_entry_var_tab3.get(), 500000, 100000, 10000000)
        self.loan_amount_slider_tab3.set(amount)
        self.loan_amount_entry_var_tab3.set(f"{amount:,}")
        self.update_tab3_planner()

    def on_tab3_interest_rate_slider(self, value):
        rate = float(value)
        self.interest_rate_entry_var_tab3.set(f"{rate:.2f}")
        self.update_tab3_planner()

    def on_tab3_interest_rate_entry(self, event=None):
        rate = self.parse_float_value(self.interest_rate_entry_var_tab3.get(), 8.0, 1.0, 20.0)
        self.interest_rate_slider_tab3.set(rate)
        self.interest_rate_entry_var_tab3.set(f"{rate:.2f}")
        self.update_tab3_planner()

    # ============ TAB 2: Loan Eligibility Calculator ============
    def setup_tab2_loan_eligibility(self):
        """Tab 2: Calculate EMI based on Earning + Existing Loan"""
        
        # Monthly Income
        ttk.Label(self.tab2, text="Monthly Income (₹):", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=10)
        self.earning_slider_tab2 = ttk.Scale(self.tab2, from_=10000, to=1000000, orient='horizontal', length=300)
        self.earning_slider_tab2.set(50000)
        self.earning_slider_tab2.grid(row=0, column=1, padx=10)
        self.earning_entry_var_tab2 = tk.StringVar(value="50000")
        self.earning_entry_tab2 = ttk.Entry(self.tab2, textvariable=self.earning_entry_var_tab2, width=12)
        self.earning_entry_tab2.grid(row=0, column=2, padx=10)
        self.earning_label_tab2 = ttk.Label(self.tab2, text="₹50,000", font=('Arial', 10))
        self.earning_label_tab2.grid(row=0, column=3)
        self.earning_slider_tab2.config(command=self.on_tab2_earning_slider)
        self.earning_entry_tab2.bind('<Return>', self.on_tab2_earning_entry)
        self.earning_entry_tab2.bind('<FocusOut>', self.on_tab2_earning_entry)
        
        # Existing EMI
        ttk.Label(self.tab2, text="Existing EMI (₹):", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=10)
        self.existing_emi_slider_tab2 = ttk.Scale(self.tab2, from_=0, to=200000, orient='horizontal', length=300)
        self.existing_emi_slider_tab2.set(0)
        self.existing_emi_slider_tab2.grid(row=1, column=1, padx=10)
        self.existing_emi_entry_var_tab2 = tk.StringVar(value="0")
        self.existing_emi_entry_tab2 = ttk.Entry(self.tab2, textvariable=self.existing_emi_entry_var_tab2, width=12)
        self.existing_emi_entry_tab2.grid(row=1, column=2, padx=10)
        self.existing_emi_label_tab2 = ttk.Label(self.tab2, text="₹0", font=('Arial', 10))
        self.existing_emi_label_tab2.grid(row=1, column=3)
        self.existing_emi_slider_tab2.config(command=self.on_tab2_existing_emi_slider)
        self.existing_emi_entry_tab2.bind('<Return>', self.on_tab2_existing_emi_entry)
        self.existing_emi_entry_tab2.bind('<FocusOut>', self.on_tab2_existing_emi_entry)
        
        # EMI/NMI Ratio
        ttk.Label(self.tab2, text="EMI/NMI Ratio (%):", font=('Arial', 10, 'bold')).grid(row=2, column=0, sticky='w', pady=10)
        self.emi_nmi_slider_tab2 = ttk.Scale(self.tab2, from_=0, to=50, orient='horizontal', length=300)
        self.emi_nmi_slider_tab2.set(10)
        self.emi_nmi_slider_tab2.grid(row=2, column=1, padx=10)
        self.emi_nmi_entry_var_tab2 = tk.StringVar(value="10.0")
        self.emi_nmi_entry_tab2 = ttk.Entry(self.tab2, textvariable=self.emi_nmi_entry_var_tab2, width=12)
        self.emi_nmi_entry_tab2.grid(row=2, column=2, padx=10)
        self.emi_nmi_label_tab2 = ttk.Label(self.tab2, text="10%", font=('Arial', 10))
        self.emi_nmi_label_tab2.grid(row=2, column=3)
        self.emi_nmi_slider_tab2.config(command=self.on_tab2_emi_nmi_slider)
        self.emi_nmi_entry_tab2.bind('<Return>', self.on_tab2_emi_nmi_entry)
        self.emi_nmi_entry_tab2.bind('<FocusOut>', self.on_tab2_emi_nmi_entry)
        
        # Interest Rate
        ttk.Label(self.tab2, text="Annual Interest Rate (%):", font=('Arial', 10, 'bold')).grid(row=3, column=0, sticky='w', pady=10)
        self.interest_rate_slider_tab2 = ttk.Scale(self.tab2, from_=1, to=20, orient='horizontal', length=300)
        self.interest_rate_slider_tab2.set(8)
        self.interest_rate_slider_tab2.grid(row=3, column=1, padx=10)
        self.interest_rate_entry_var_tab2 = tk.StringVar(value="8.00")
        self.interest_rate_entry_tab2 = ttk.Entry(self.tab2, textvariable=self.interest_rate_entry_var_tab2, width=12)
        self.interest_rate_entry_tab2.grid(row=3, column=2, padx=10)
        self.interest_rate_label_tab2 = ttk.Label(self.tab2, text="8.00%", font=('Arial', 10))
        self.interest_rate_label_tab2.grid(row=3, column=3)
        self.interest_rate_slider_tab2.config(command=self.on_tab2_interest_rate_slider)
        self.interest_rate_entry_tab2.bind('<Return>', self.on_tab2_interest_rate_entry)
        self.interest_rate_entry_tab2.bind('<FocusOut>', self.on_tab2_interest_rate_entry)
        
        # Duration
        ttk.Label(self.tab2, text="Loan Duration (Years):", font=('Arial', 10, 'bold')).grid(row=4, column=0, sticky='w', pady=10)
        self.duration_slider_tab2 = ttk.Scale(self.tab2, from_=1, to=30, orient='horizontal', length=300)
        self.duration_slider_tab2.set(5)
        self.duration_slider_tab2.grid(row=4, column=1, padx=10)
        self.duration_entry_var_tab2 = tk.StringVar(value="5")
        self.duration_entry_tab2 = ttk.Entry(self.tab2, textvariable=self.duration_entry_var_tab2, width=12)
        self.duration_entry_tab2.grid(row=4, column=2, padx=10)
        self.duration_label_tab2 = ttk.Label(self.tab2, text="5 years", font=('Arial', 10))
        self.duration_label_tab2.grid(row=4, column=3)
        self.duration_slider_tab2.config(command=self.on_tab2_duration_slider)
        self.duration_entry_tab2.bind('<Return>', self.on_tab2_duration_entry)
        self.duration_entry_tab2.bind('<FocusOut>', self.on_tab2_duration_entry)
        
        # Results Frame
        ttk.Separator(self.tab2, orient='horizontal').grid(row=5, column=0, columnspan=4, sticky='ew', pady=20)
        
        results_frame = ttk.LabelFrame(self.tab2, text="Loan Eligibility Results", padding="15", style='Card.TLabelframe')
        results_frame.grid(row=6, column=0, columnspan=4, sticky='ew', pady=10)
        
        ttk.Label(results_frame, text="Available EMI Capacity:", font=('Arial', 11, 'bold')).grid(row=0, column=0, sticky='w', pady=5)
        self.available_emi_tab2 = ttk.Label(results_frame, text="₹0", font=('Arial', 12, 'bold'), foreground='blue')
        self.available_emi_tab2.grid(row=0, column=1, sticky='w', padx=20)
        
        ttk.Label(results_frame, text="Maximum Eligible Loan:", font=('Arial', 11, 'bold')).grid(row=1, column=0, sticky='w', pady=5)
        self.max_loan_eligible_tab2 = ttk.Label(results_frame, text="₹0", font=('Arial', 12, 'bold'), foreground='green')
        self.max_loan_eligible_tab2.grid(row=1, column=1, sticky='w', padx=20)
        
        ttk.Label(results_frame, text="Total Payable Interest (Approx):", font=('Arial', 11, 'bold')).grid(row=2, column=0, sticky='w', pady=5)
        self.approx_interest_tab2 = ttk.Label(results_frame, text="₹0", font=('Arial', 12))
        self.approx_interest_tab2.grid(row=2, column=1, sticky='w', padx=20)
        
        self.update_tab2_eligibility()
    
    def update_tab2_eligibility(self, event=None):
        """Calculate and update loan eligibility for Tab 2"""
        monthly_earning = int(self.earning_slider_tab2.get())
        existing_emi = int(self.existing_emi_slider_tab2.get())
        emi_nmi_ratio = float(self.emi_nmi_slider_tab2.get()) / 100
        interest_rate = float(self.interest_rate_slider_tab2.get())
        duration_years = int(self.duration_slider_tab2.get())
        
        # Update labels
        self.earning_label_tab2.config(text=f"₹{monthly_earning:,}")
        self.existing_emi_label_tab2.config(text=f"₹{existing_emi:,}")
        self.emi_nmi_label_tab2.config(text=f"{self.emi_nmi_slider_tab2.get():.1f}%")
        self.interest_rate_label_tab2.config(text=f"{interest_rate:.2f}%")
        self.duration_label_tab2.config(text=f"{duration_years} year{'s' if duration_years != 1 else ''}")
        
        # Calculate available EMI capacity using monthly income, allowed EMI ratio, and current obligations.
        available_emi_capacity = monthly_earning * emi_nmi_ratio - existing_emi
        
        # Calculate maximum eligible loan
        # P = EMI * [((1 + r)^n - 1) / (r * (1 + r)^n)]
        monthly_rate = interest_rate / 100 / 12
        num_months = duration_years * 12
        
        if available_emi_capacity <= 0:
            max_loan = 0.0
            approx_total_interest = 0.0
        elif monthly_rate == 0:
            max_loan = available_emi_capacity * num_months
            approx_total_interest = 0.0
        else:
            max_loan = available_emi_capacity * (((1 + monthly_rate) ** num_months - 1) / (monthly_rate * (1 + monthly_rate) ** num_months))
            approx_total_interest = (available_emi_capacity * num_months) - max_loan
        
        self.available_emi_tab2.config(text=f"₹{available_emi_capacity:,.2f}")
        self.max_loan_eligible_tab2.config(text=f"₹{max_loan:,.2f}")
        self.approx_interest_tab2.config(text=f"₹{approx_total_interest:,.2f}")
    
    # ============ TAB 3: Duration Planner ============
    def setup_tab3_duration_planner(self):
        """Tab 3: Comparative chart of EMI and Interest for different durations"""
        
        # Loan Amount
        ttk.Label(self.tab3, text="Loan Amount (₹):", font=('Arial', 10, 'bold')).grid(row=0, column=0, sticky='w', pady=10)
        self.loan_amount_slider_tab3 = ttk.Scale(self.tab3, from_=100000, to=10000000, orient='horizontal', length=300)
        self.loan_amount_slider_tab3.set(500000)
        self.loan_amount_slider_tab3.grid(row=0, column=1, padx=10)
        self.loan_amount_entry_var_tab3 = tk.StringVar(value="500000")
        self.loan_amount_entry_tab3 = ttk.Entry(self.tab3, textvariable=self.loan_amount_entry_var_tab3, width=12)
        self.loan_amount_entry_tab3.grid(row=0, column=2, padx=10)
        self.loan_amount_label_tab3 = ttk.Label(self.tab3, text="₹500,000", font=('Arial', 10))
        self.loan_amount_label_tab3.grid(row=0, column=3)
        self.loan_amount_slider_tab3.config(command=self.on_tab3_loan_amount_slider)
        self.loan_amount_entry_tab3.bind('<Return>', self.on_tab3_loan_amount_entry)
        self.loan_amount_entry_tab3.bind('<FocusOut>', self.on_tab3_loan_amount_entry)
        
        # Interest Rate
        ttk.Label(self.tab3, text="Annual Interest Rate (%):", font=('Arial', 10, 'bold')).grid(row=1, column=0, sticky='w', pady=10)
        self.interest_rate_slider_tab3 = ttk.Scale(self.tab3, from_=1, to=20, orient='horizontal', length=300)
        self.interest_rate_slider_tab3.set(8)
        self.interest_rate_slider_tab3.grid(row=1, column=1, padx=10)
        self.interest_rate_entry_var_tab3 = tk.StringVar(value="8.00")
        self.interest_rate_entry_tab3 = ttk.Entry(self.tab3, textvariable=self.interest_rate_entry_var_tab3, width=12)
        self.interest_rate_entry_tab3.grid(row=1, column=2, padx=10)
        self.interest_rate_label_tab3 = ttk.Label(self.tab3, text="8.00%", font=('Arial', 10))
        self.interest_rate_label_tab3.grid(row=1, column=3)
        self.interest_rate_slider_tab3.config(command=self.on_tab3_interest_rate_slider)
        self.interest_rate_entry_tab3.bind('<Return>', self.on_tab3_interest_rate_entry)
        self.interest_rate_entry_tab3.bind('<FocusOut>', self.on_tab3_interest_rate_entry)
        
        ttk.Separator(self.tab3, orient='horizontal').grid(row=2, column=0, columnspan=4, sticky='ew', pady=15)

        # Create a scrollable area for the comparison table
        # Configure tab3 grid so the table container can expand
        self.tab3.rowconfigure(3, weight=1)
        self.tab3.columnconfigure(0, weight=1)

        table_container = ttk.LabelFrame(self.tab3, text="Duration Comparison Chart", padding="0", style='Card.TLabelframe')
        table_container.grid(row=3, column=0, columnspan=4, sticky='nsew', pady=10)

        # Canvas + vertical scrollbar
        canvas = tk.Canvas(table_container, borderwidth=0, highlightthickness=0)
        vscroll = ttk.Scrollbar(table_container, orient='vertical', command=canvas.yview)
        canvas.configure(yscrollcommand=vscroll.set)

        vscroll.pack(side='right', fill='y')
        canvas.pack(side='left', fill='both', expand=True)

        # Inner frame inside canvas where rows/headers will live
        table_inner = ttk.Frame(canvas)
        canvas.create_window((0, 0), window=table_inner, anchor='nw')

        # Update scrollregion when inner frame changes size
        def _on_frame_config(event):
            canvas.configure(scrollregion=canvas.bbox('all'))

        table_inner.bind('<Configure>', _on_frame_config)

        # Optional: enable mousewheel scrolling when cursor is over the canvas
        def _on_mousewheel(event):
            # Windows / Mac deltas differ; normalize for units
            delta = 0
            if event.delta:
                delta = -1 * int(event.delta / 120)
            elif getattr(event, 'num', None) == 4:
                delta = -1
            elif getattr(event, 'num', None) == 5:
                delta = 1
            if delta:
                canvas.yview_scroll(delta, 'units')

        canvas.bind_all('<MouseWheel>', _on_mousewheel)
        canvas.bind_all('<Button-4>', _on_mousewheel)
        canvas.bind_all('<Button-5>', _on_mousewheel)

        # Headers
        ttk.Label(table_inner, text="Duration", font=('Arial', 10, 'bold'), width=12).grid(row=0, column=0, sticky='w', padx=5)
        ttk.Label(table_inner, text="Monthly EMI", font=('Arial', 10, 'bold'), width=15).grid(row=0, column=1, sticky='w', padx=5)
        ttk.Label(table_inner, text="Total Amount", font=('Arial', 10, 'bold'), width=15).grid(row=0, column=2, sticky='w', padx=5)
        ttk.Label(table_inner, text="Total Interest", font=('Arial', 10, 'bold'), width=15).grid(row=0, column=3, sticky='w', padx=5)

        self.table_rows = []
        for i in range(1, 31):
            duration = i
            label_duration = ttk.Label(table_inner, text=f"{duration} year{'s' if duration != 1 else ''}", font=('Arial', 9))
            label_duration.grid(row=i, column=0, sticky='w', padx=5, pady=2)

            label_emi = ttk.Label(table_inner, text="₹0", font=('Arial', 9))
            label_emi.grid(row=i, column=1, sticky='w', padx=5, pady=2)

            label_total = ttk.Label(table_inner, text="₹0", font=('Arial', 9))
            label_total.grid(row=i, column=2, sticky='w', padx=5, pady=2)

            label_interest = ttk.Label(table_inner, text="₹0", font=('Arial', 9))
            label_interest.grid(row=i, column=3, sticky='w', padx=5, pady=2)

            self.table_rows.append({
                'duration': label_duration,
                'emi': label_emi,
                'total': label_total,
                'interest': label_interest
            })

        self.update_tab3_planner()
    
    def update_tab3_planner(self, event=None):
        """Calculate and update duration planner for Tab 3"""
        loan_amount = int(self.loan_amount_slider_tab3.get())
        interest_rate = float(self.interest_rate_slider_tab3.get())
        
        # Update labels
        self.loan_amount_label_tab3.config(text=f"₹{loan_amount:,}")
        self.interest_rate_label_tab3.config(text=f"{interest_rate:.2f}%")
        
        # Update table rows
        for i, row in enumerate(self.table_rows, 1):
            emi = self.calculate_emi(loan_amount, interest_rate, i)
            total_amount = emi * i * 12
            total_interest = total_amount - loan_amount
            
            row['emi'].config(text=f"₹{emi:,.0f}")
            row['total'].config(text=f"₹{total_amount:,.0f}")
            row['interest'].config(text=f"₹{total_interest:,.0f}")
    
    # ============ Helper Methods ============
    def calculate_emi(self, principal, annual_rate, years):
        """
        Calculate EMI using the formula:
        EMI = P * [r(1+r)^n] / [(1+r)^n - 1]
        where P = Principal, r = Monthly Rate, n = Number of months
        """
        if annual_rate == 0:
            return principal / (years * 12)
        
        monthly_rate = annual_rate / 100 / 12
        num_months = years * 12
        
        emi = principal * (monthly_rate * (1 + monthly_rate) ** num_months) / (((1 + monthly_rate) ** num_months) - 1)
        return emi

    def show_license(self):
        """Show an MIT license popup with ownership assigned to AVIK MUKHERJEE 2026."""
        license_text = (
            "MIT License\n\n"
            "Copyright (c) 2026 AVIK MUKHERJEE\n\n"
            "Permission is hereby granted, free of charge, to any person obtaining a copy\n"
            "of this software and associated documentation files (the \"Software\"), to deal\n"
            "in the Software without restriction, including without limitation the rights\n"
            "to use, copy, modify, merge, publish, distribute, sublicense, and/or sell\n"
            "copies of the Software, and to permit persons to whom the Software is\n"
            "furnished to do so, subject to the following conditions:\n\n"
            "The above copyright notice and this permission notice shall be included in all\n"
            "copies or substantial portions of the Software.\n\n"
            "THE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\n"
            "IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\n"
            "FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\n"
            "AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\n"
            "LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\n"
            "OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\n"
            "SOFTWARE.\n"
        )

        popup = tk.Toplevel(self.root)
        popup.title("License")
        popup.transient(self.root)
        popup.resizable(False, False)

        frame = ttk.Frame(popup, padding=12)
        frame.pack(fill='both', expand=True)

        text_widget = tk.Text(frame, wrap='word', width=72, height=18)
        text_widget.insert('1.0', license_text)
        text_widget.configure(state='disabled')
        text_widget.pack(side='top', fill='both', expand=True)

        btn_frame = ttk.Frame(frame)
        btn_frame.pack(fill='x', pady=(8, 0))
        close_btn = ttk.Button(btn_frame, text='Close', command=popup.destroy)
        close_btn.pack(side='right')


def main():
    """Main function to run the EMI and Loan Eligibility Calculator"""
    root = tk.Tk()
    app = EMICalculator(root)
    root.mainloop()


if __name__ == "__main__":
    main()
