# EMI and Loan Eligibility Calculator

A modern-looking EMI and loan eligibility calculator application built with Python and Tkinter.

This project helps users calculate monthly EMI, total payment, and total interest using loan amount, interest rate, and tenure inputs. It also includes a loan eligibility estimator and a duration comparison chart with scroll support.

## Features

- Find monthly EMI, total amount, and total interest
- Adjustable loan amount, interest rate, and duration
- Loan eligibility estimation based on income, existing EMI-to-income ratio, and tenure
- Duration planner with comparison table for multiple loan tenures
- Dual input controls: sliders and text fields synchronized together
- License popup with MIT ownership declaration
- Modern UI styling with card-style panels and responsive layout

## Requirements

- Python 3.12 or later
- Tkinter (included with standard Python installations on Windows)

## Installation

1. Clone or download the repository.
2. Create a virtual environment in the project folder:

```powershell
cd "E:\Git Projects\EMI and Loan Eligibility Calculator"
python -m venv .venv
```

3. Activate the virtual environment:

```powershell
& .\.venv\Scripts\Activate.ps1
```

4. If you want, upgrade pip:

```powershell
python -m pip install --upgrade pip
```

## Running the App

While the virtual environment is active, run:

```powershell
python emi_and_loan_eligibility_calculator.py
```

## Packaging as an Executable

To create a standalone Windows executable with PyInstaller:

```powershell
pyinstaller --onefile --windowed --add-data "LICENSE;." --name "EMI and Loan Eligibility Calculator" emi_and_loan_eligibility_calculator.py
```

After packaging, the executable will be available in the `dist` folder.

## Project Files

- `emi_and_loan_eligibility_calculator.py` — main application source file
- `LICENSE` — MIT license, copyright 2026 AVIK MUKHERJEE
- `PRIVACY.md` — privacy policy and data usage notes
- `.gitignore` — ignores virtual environments, build artifacts, and sensitive files
- `README.md` — project overview and usage instructions

## Privacy

This application includes a privacy policy. See [PRIVACY.md](PRIVACY.md) for details.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
