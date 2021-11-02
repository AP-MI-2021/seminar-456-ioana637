from Domain.cofetarie import create_cofetarie
from UI import run_console
from Tests import run_all_tests

def main():
    cofetarie = create_cofetarie()
    run_console(cofetarie)

run_all_tests()
main()
