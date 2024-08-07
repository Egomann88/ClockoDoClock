from mange_env_service.manage_env import check_env_correctness, incorrect_env_values, env_write_customer_service
from clockodo_service.clock import clock
import os

ENV_PATH = os.path.join(os.path.dirname(__file__), ".env")

def fill_customers_services(value_matches):
    # if API_KEY, EMAIL and SUBDOMAIN are True, while SERVICES_ID and CUSTOMERS_ID are False
    if value_matches[0] and value_matches[1] and value_matches[2] and not value_matches[3] and not value_matches[4]:
        user_input = input("Do you want to make a request to the Clockodo API to get the ID values of your services and customers? (y/n)")
        if user_input.lower() == 'y':
            env_write_customer_service(ENV_PATH, "customers", "CUSTOMERS_ID")
            env_write_customer_service(ENV_PATH, "services", "SERVICES_ID")
        return

def main():
    res = check_env_correctness()
    
    # If any of the environment variables are missing or incorrect
    if not all(res):
        incorrect_env_values(res)
        fill_customers_services(res)
        return

    # Your main logic here
    clock()


if __name__ == "__main__":
    main()
